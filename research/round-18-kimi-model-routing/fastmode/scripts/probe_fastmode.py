#!/usr/bin/env python3
"""R18 fast-mode probe: `service_tier` variants against the openai-codex lane.

    python3 scripts/probe_fastmode.py [config.toml]

Phase A (acceptance): one minimal request per variant -- D6 shape (list
`input`, `store:false`, `stream:true`, no `temperature`, `max_output_tokens`
16) with prompt "ping" -- recording the exact request bytes, HTTP status, the
error body when rejected, the response's own `service_tier` echo and whether
the request was serviced. Variants: omit (baseline), default, flex, priority,
plus `fast` and `auto` (both discovered in the local codex CLI's own docs /
catalog and the backend's default echo) and an invalid-value control that
separates "the backend validates this field" from "the backend ignores it".

Phase B (measurement): for every variant Phase A serviced, two sequential reps
of the M3 battery performance probe -- identical fixed prompt, 256 tokens,
server-side usage completion tokens -- with TTFT/TPS derived exactly as the
battery derives them (see protocols.py there): TTFT is content-only, the
decode span starts at the first delta of any kind, TPS is
(completion_tokens - 1) / decode_span, and a span under 50 ms with deltas is
recorded as burst, not as a throughput number.

Quota politeness: the codex lane is the user's ChatGPT plan, so Phase A is one
attempt per variant (rejections cost nothing; acceptance is bounded by 16
tokens), Phase B is n=2 reps, and a 401/403/429 wall stops the run instead of
retrying. No loops, no concurrency, no retries.
"""
import hashlib
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

MODEL = "gpt-6.1-sol"
PROVIDER = "openai-codex"
TIMEOUT_S = 300
MIN_DECODE_SPAN_MS = 50

# The M3 battery's fixed performance prompt, verbatim (battery/scripts/probes.py),
# so every number here is comparable with the battery baseline.
PERF_PROMPT = (
    "You are answering a latency measurement probe. Follow it exactly. "
    "Task: output the integers from 1 to 150 inclusive, in ascending order, "
    "separated by single spaces, on one single line. Output digits and spaces "
    "only. Do not add any explanation, preamble, punctuation, or trailing text."
)
PERF_MAX_TOKENS = 256
EXPECTED_PERF_OUTPUT = " ".join(str(n) for n in range(1, 151))

ACCEPT_PROMPT = "ping"
ACCEPT_MAX_TOKENS = 16

# Phase A variants. `source` records where the candidate came from; `patch` is
# merged into the D6-shaped body.
VARIANTS = [
    {
        "name": "omit",
        "patch": {},
        "source": "mission baseline (M2/M3 shape, no service_tier field)",
        "note": "baseline",
    },
    {
        "name": "default",
        "patch": {"service_tier": "default"},
        "source": "mission/briefing: Responses-API service_tier value",
    },
    {
        "name": "flex",
        "patch": {"service_tier": "flex"},
        "source": "mission/briefing: Responses-API service_tier value",
    },
    {
        "name": "priority",
        "patch": {"service_tier": "priority"},
        "source": "user's ask; codex model catalog service_tiers[].id for "
                  "gpt-6.1-sol (name 'Fast', '2x speed, increased usage')",
    },
    {
        "name": "fast",
        "patch": {"service_tier": "fast"},
        "source": "codex CLI binary docs: service_tier \"fast\" or \"priority\"; "
                  "catalog additional_speed_tiers ['fast']",
    },
    {
        "name": "auto",
        "patch": {"service_tier": "auto"},
        "source": "backend default echo: captures show response.service_tier='auto' "
                  "when the request omits the field",
    },
    {
        "name": "invalid-control",
        "patch": {"service_tier": "r18-invalid-tier"},
        "source": "control, M2 methodology: a value no lane serves distinguishes "
                  "validated acceptance from ignored acceptance",
    },
]


def build_body(prompt, max_tokens, patch):
    body = {
        "model": MODEL,
        "stream": True,
        "store": False,
        "max_output_tokens": max_tokens,
        "input": [{
            "type": "message", "role": "user",
            "content": [{"type": "input_text", "text": prompt}],
        }],
    }
    body.update(patch)
    return body


def _usage_tokens(usage, key_a, key_b):
    if not isinstance(usage, dict):
        return None
    for key in (key_a, key_b):
        if isinstance(usage.get(key), int):
            return usage[key]
    return None


def completion_tokens(usage):
    return _usage_tokens(usage, "completion_tokens", "output_tokens")


def prompt_tokens(usage):
    return _usage_tokens(usage, "prompt_tokens", "input_tokens")


def reasoning_tokens(usage):
    if not isinstance(usage, dict):
        return None
    details = usage.get("completion_tokens_details") or usage.get("output_tokens_details")
    if isinstance(details, dict) and isinstance(details.get("reasoning_tokens"), int):
        return details["reasoning_tokens"]
    return None


class Stream:
    """Accumulates one Responses-API SSE stream: deltas, usage, timings, echo."""

    def __init__(self, t0):
        self.t0 = t0
        self.content = []
        self.reasoning = []
        self.refusal = []
        self.usage = None
        self.finish_status = None
        self.incomplete_reason = None
        self.error_text = None
        self.echoed_service_tier = None
        self.echoes = []
        self.event_types = []
        self.sse_events = 0
        self.parse_errors = 0
        self.t_first_content = None
        self.t_first_reasoning = None
        self.t_first_delta = None
        self.t_last_delta = None

    def _touch(self, when):
        if self.t_first_delta is None:
            self.t_first_delta = when
        self.t_last_delta = when

    def feed(self, text, when):
        if not text or not text.startswith("data:"):
            return
        payload = text[5:].strip()
        if not payload or payload == "[DONE]":
            return
        try:
            obj = json.loads(payload)
        except Exception:  # noqa: BLE001
            self.parse_errors += 1
            return
        if not isinstance(obj, dict):
            return
        self.sse_events += 1
        kind = obj.get("type")
        if kind:
            self.event_types.append(kind)
        usage = obj.get("usage") if isinstance(obj.get("usage"), dict) else None
        nested = obj.get("message") or obj.get("response")
        if isinstance(nested, dict):
            if usage is None and isinstance(nested.get("usage"), dict):
                usage = nested["usage"]
            tier = nested.get("service_tier")
            if isinstance(tier, str):
                self.echoed_service_tier = tier
                self.echoes.append({
                    "event_type": kind,
                    "sequence_number": obj.get("sequence_number"),
                    "service_tier": tier,
                    "status": nested.get("status"),
                })
        if usage:
            self.usage = usage

        if kind == "response.output_text.delta" and obj.get("delta"):
            self.content.append(obj["delta"])
            if self.t_first_content is None:
                self.t_first_content = when
            self._touch(when)
        elif kind in ("response.reasoning_summary_text.delta",
                      "response.reasoning_text.delta") and obj.get("delta"):
            self.reasoning.append(obj["delta"])
            if self.t_first_reasoning is None:
                self.t_first_reasoning = when
            self._touch(when)
        elif kind == "response.refusal.delta" and obj.get("delta"):
            self.refusal.append(obj["delta"])
            self._touch(when)
        elif kind == "response.function_call_arguments.delta":
            self._touch(when)
        elif kind == "response.completed":
            response = obj.get("response") or {}
            if isinstance(response.get("usage"), dict):
                self.usage = response["usage"]
            self.finish_status = response.get("status")
        elif kind == "response.incomplete":
            response = obj.get("response") or {}
            self.incomplete_reason = (response.get("incomplete_details") or {}).get("reason")
        elif kind in ("response.failed", "error"):
            response = obj.get("response") or {}
            err = response.get("error") or obj.get("error") or {}
            if isinstance(err, dict):
                self.error_text = err.get("message") or err.get("code") or str(err)
            else:
                self.error_text = str(err)


def summarize(stream):
    completion = completion_tokens(stream.usage)
    span_ms = None
    if stream.t_first_delta is not None and stream.t_last_delta is not None:
        span_ms = round((stream.t_last_delta - stream.t_first_delta) * 1000)
    tps, tps_note = None, None
    if completion is not None and span_ms is not None:
        if span_ms < MIN_DECODE_SPAN_MS:
            tps_note = ("burst: decode span %d ms < %d ms; throughput not derivable"
                        % (span_ms, MIN_DECODE_SPAN_MS))
        elif span_ms > 0:
            tps = round((completion - 1) / (span_ms / 1000.0), 2)
    elif span_ms is None:
        tps_note = "no deltas"
    if completion is None:
        tps_note = (tps_note + "; " if tps_note else "") + "no server usage completion tokens"
    content = "".join(stream.content)
    return {
        "content": content,
        "content_truncated": len(content) > 600,
        "content_head": content[:600],
        "content_delta_count": len(stream.content),
        "reasoning_chars": len("".join(stream.reasoning)),
        "reasoning_delta_count": len(stream.reasoning),
        "refusal_text": "".join(stream.refusal)[:400] or None,
        "usage": stream.usage,
        "completion_tokens": completion,
        "prompt_tokens": prompt_tokens(stream.usage),
        "reasoning_tokens": reasoning_tokens(stream.usage),
        "response_status": stream.finish_status,
        "incomplete_reason": stream.incomplete_reason,
        "stream_error": stream.error_text,
        "echoed_service_tier": stream.echoed_service_tier,
        "echoes": stream.echoes,
        "sse_event_count": stream.sse_events,
        "sse_event_types": sorted(set(stream.event_types)),
        "parse_errors": stream.parse_errors,
        "ttft_content_ms": (round((stream.t_first_content - stream.t0) * 1000)
                            if stream.t_first_content is not None else None),
        "ttft_reasoning_ms": (round((stream.t_first_reasoning - stream.t0) * 1000)
                              if stream.t_first_reasoning is not None else None),
        "first_decoded_ms": (round((stream.t_first_delta - stream.t0) * 1000)
                             if stream.t_first_delta is not None else None),
        "decode_span_ms": span_ms,
        "tps": tps,
        "tps_basis": "server_usage_completion_tokens" if tps is not None else None,
        "tps_note": tps_note,
    }


def parse_capture(capture):
    stream = Stream(capture["t0"])
    for text, when in capture["lines"]:
        stream.feed(text, when)
    return stream


def perform(url, headers, body, timeout=TIMEOUT_S):
    """One request; returns (record_core, summary) with redacted evidence."""
    capture = common.post_streaming(url, headers, body, timeout)
    stream = parse_capture(capture)
    summary = summarize(stream)
    body_json = json.dumps(body)
    record = {
        "url": url,
        "method": "POST",
        "request_headers_sent": common.redact_headers(headers),
        "request_body": body,
        "request_body_json": body_json,
        "request_body_sha256": hashlib.sha256(body_json.encode()).hexdigest()[:16],
        "status": capture["status"],
        "error": capture["error"],
        "error_kind": capture["error_kind"],
        "elapsed_ms": (round((capture["lines"][-1][1] - capture["t0"]) * 1000)
                       if capture["lines"] else None),
        "response_headers": capture["response_headers"],
        "response_preview": capture["preview"][:3000],
        "serviced": (capture["status"] == 200 and (
            summary["content_delta_count"] > 0
            or summary["reasoning_delta_count"] > 0
            or "response.completed" in summary["sse_event_types"])),
    }
    return record, summary


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    base_url = cfg["providers"][PROVIDER]["base_url"].rstrip("/")
    url = base_url + "/responses"
    headers = common.request_headers(cfg, PROVIDER)
    window_start = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    print("config json-canonical digest/16: %s" % common.config_digest(cfg))
    print("config file sha256: %s" % common.config_file_sha256(path))
    print("url: %s   model: %s" % (url, MODEL))

    phase_a, phase_b = [], []
    abort_reason = None

    # ---- Phase A: acceptance sweep -------------------------------------
    print("\nPhase A -- acceptance (max_output_tokens=%d, prompt %r)"
          % (ACCEPT_MAX_TOKENS, ACCEPT_PROMPT))
    for variant in VARIANTS:
        body = build_body(ACCEPT_PROMPT, ACCEPT_MAX_TOKENS, variant["patch"])
        record, summary = perform(url, headers, body)
        record.update({
            "phase": "A", "variant": variant["name"], "patch": variant["patch"],
            "source": variant["source"], "note": variant.get("note"),
            "summary": summary,
        })
        phase_a.append(record)
        detail = ""
        if summary.get("stream_error"):
            detail = summary["stream_error"][:120]
        elif record["status"] != 200:
            match = re.search(r'"(?:detail|message)"\s*:\s*"([^"]{0,140})',
                              record["response_preview"] or "")
            detail = (match.group(1) if match
                      else (record["response_preview"] or "")[:120])
        print("%-16s status=%-5s %6sms serviced=%-5s tier_echo=%-9s %s" % (
            variant["name"], record["status"], record["elapsed_ms"],
            record["serviced"], summary.get("echoed_service_tier"), detail))
        if variant["name"] == "omit" and not record["serviced"] and (
                record["status"] != 400):
            abort_reason = ("baseline (omit) not serviced: status=%s error=%s"
                            % (record["status"], record["error_kind"]))
            break
        if record["error_kind"] == "connect" and len(
                [r for r in phase_a[-2:] if r.get("error_kind") == "connect"]) >= 2:
            abort_reason = "two consecutive transport failures"
            break

    if abort_reason:
        print("ABORT after Phase A: %s" % abort_reason)

    # ---- Phase B: measurement for accepted variants ---------------------
    accepted = [r for r in phase_a if r["serviced"]]
    if not abort_reason:
        print("\nPhase B -- measurement (M3 perf probe, max_output_tokens=%d, n=2)"
              % PERF_MAX_TOKENS)
        stop_b = False
        for record_a in accepted:
            if stop_b:
                break
            variant = next(v for v in VARIANTS if v["name"] == record_a["variant"])
            for rep in (1, 2):
                body = build_body(PERF_PROMPT, PERF_MAX_TOKENS, variant["patch"])
                record, summary = perform(url, headers, body)
                content = (summary["content"] or "").strip()
                record.update({
                    "phase": "B", "variant": variant["name"], "rep": rep,
                    "patch": variant["patch"],
                    "summary": summary,
                    "output_ok": content == EXPECTED_PERF_OUTPUT,
                    "output_prefix_ok": EXPECTED_PERF_OUTPUT.startswith(content[:200]),
                })
                phase_b.append(record)
                print("%-16s rep=%d status=%-5s ttft=%s ms tps=%-8s span=%s ms "
                      "ctok=%-4s burst=%s output_ok=%s" % (
                          variant["name"], rep, record["status"],
                          summary["ttft_content_ms"], summary["tps"],
                          summary["decode_span_ms"], summary["completion_tokens"],
                          bool(summary["tps_note"] and "burst" in summary["tps_note"]),
                          record["output_ok"]))
                if record["status"] in (401, 403, 429):
                    stop_b = True
                    abort_reason = ("Phase B walled at rep %d of %s: status=%s"
                                    % (rep, variant["name"], record["status"]))
                    break
                if record["status"] != 200:
                    break  # one attempt per rep; move to the next variant

    run = {
        "mission": "M5 r18-codex-fast-mode-probe",
        "model": MODEL,
        "provider": PROVIDER,
        "url": url,
        "config_json_digest_16": common.config_digest(cfg),
        "config_file_sha256": common.config_file_sha256(path),
        "window_start_utc": window_start,
        "window_end_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "accept_prompt": ACCEPT_PROMPT,
        "perf_prompt": PERF_PROMPT,
        "abort_reason": abort_reason,
        "variants": [{k: v for k, v in var.items()} for var in VARIANTS],
        "phase_a": phase_a,
        "phase_b": phase_b,
    }
    out = common.write_json("fastmode-probe.json", run)
    print("\nwrote %s (%d phase-A records, %d phase-B records, abort=%s)"
          % (out, len(phase_a), len(phase_b), abort_reason))


if __name__ == "__main__":
    main()
