#!/usr/bin/env python3
"""R18 codex 'ultra' reasoning-effort probe: `reasoning.effort` against openai-codex.

    python3 scripts/probe_ultra.py [config.toml]

Wire shape: the M1 D6 shape (list `input`, `store:false`, `stream:true`, no
`temperature`, `max_output_tokens >= 16`) plus the effort field for the
`openai_responses` protocol -- `reasoning: {"effort": <value>}` (M2 s3 rule 3).

Phase A (acceptance): one minimal request per candidate effort value --
`high`, `xhigh`, `max`, `ultra` (declared by the codex catalog and CLI at the
time of the run) -- plus an invalid-effort control that separates "the backend
validates this field" from "the backend ignores it" (M2 s4.1 shows openai-codex
validates: control 400). Records the exact request bytes, HTTP status, the
error body when rejected, whether the request was serviced, the response's own
`reasoning` echo and the usage block.

Phase B (measurement): the M3 battery methodology, on the M3 battery's own
fixed performance prompt at max_output_tokens 256, n=2 sequential reps, for
every accepted value at or above the current high pin, plus a same-window
no-effort control (`omit`) because the M3 high-pin baseline was itself measured
without an effort field on the wire (battery/scripts/protocols.py builds the
codex body with no `reasoning` key). TTFT is content-only, the decode span
starts at the first delta of any kind, TPS is (completion_tokens - 1) /
decode_span with completion tokens from the server usage block, and a span
under 50 ms is recorded as burst rather than as throughput.

Quota politeness: the codex lane is the operator's ChatGPT plan. Phase A is one
attempt per value (rejections cost nothing; acceptance bounded by 16 tokens),
Phase B is n=2 and bounded at 256 tokens per rep, and a 401/403/429 wall stops
the run instead of retrying. No loops, no concurrency, no retries.
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
# merged into the D6-shaped body. The four effort values are the top rungs of
# the catalog's supported_reasoning_levels for gpt-6.1-sol (low/medium/high/
# xhigh/max/ultra); only values >= the current high pin are in scope.
def effort_patch(value):
    return {"reasoning": {"effort": value}}


VARIANTS = [
    {
        "name": "high",
        "patch": effort_patch("high"),
        "source": "live sol-high pool entry pins high (overrides.default_effort); "
                  "catalog supported_reasoning_levels[2]",
        "note": "current high pin",
    },
    {
        "name": "xhigh",
        "patch": effort_patch("xhigh"),
        "source": "catalog supported_reasoning_levels[3]; live support_efforts list",
    },
    {
        "name": "max",
        "patch": effort_patch("max"),
        "source": "catalog supported_reasoning_levels[4]; accepted by this lane in "
                  "M2 s4.1; live support_efforts list",
    },
    {
        "name": "ultra",
        "patch": effort_patch("ultra"),
        "source": "codex catalog (models_cache.json fetched 2026-10-15) and codex CLI "
                  "binary embedded catalog: supported_reasoning_levels[5], "
                  "\"Maximum reasoning with automatic task delegation\"",
    },
    {
        "name": "invalid-control",
        "patch": effort_patch("r18-invalid-effort"),
        "source": "control, M2 methodology: a value no lane serves distinguishes "
                  "validated acceptance from ignored acceptance",
    },
]

# Phase B order: the no-effort control first (same-window baseline), then the
# accepted candidates in ascending effort order.
OMIT = {
    "name": "omit",
    "patch": {},
    "source": "same-window control: no `reasoning` key, byte-identical to the M3 "
              "battery's codex body shape",
}


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
        self.echoes = []
        self.echoed_reasoning = None
        self.echoed_model = None
        self.completed_output_item_types = None
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
            reasoning = nested.get("reasoning")
            model = nested.get("model")
            if kind in ("response.created", "response.in_progress",
                        "response.completed"):
                self.echoes.append({
                    "event_type": kind,
                    "sequence_number": obj.get("sequence_number"),
                    "model": model,
                    "reasoning": reasoning,
                    "status": nested.get("status"),
                })
            if kind == "response.created":
                if isinstance(reasoning, dict):
                    self.echoed_reasoning = reasoning
                if isinstance(model, str):
                    self.echoed_model = model
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
            output = response.get("output")
            if isinstance(output, list):
                self.completed_output_item_types = [
                    item.get("type") for item in output if isinstance(item, dict)]
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
        "reasoning_head": "".join(stream.reasoning)[:300] or None,
        "refusal_text": "".join(stream.refusal)[:400] or None,
        "usage": stream.usage,
        "completion_tokens": completion,
        "prompt_tokens": prompt_tokens(stream.usage),
        "reasoning_tokens": reasoning_tokens(stream.usage),
        "response_status": stream.finish_status,
        "incomplete_reason": stream.incomplete_reason,
        "stream_error": stream.error_text,
        "echoed_reasoning": stream.echoed_reasoning,
        "echoed_model": stream.echoed_model,
        "echoes": stream.echoes,
        "completed_output_item_types": stream.completed_output_item_types,
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
    """One request; returns (record, summary) with redacted evidence."""
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


def detail_from(record, summary):
    if summary.get("stream_error"):
        return summary["stream_error"][:120]
    if record["status"] != 200:
        match = re.search(r'"(?:detail|message)"\s*:\s*"([^"]{0,140})',
                          record["response_preview"] or "")
        return (match.group(1) if match
                else (record["response_preview"] or "")[:120])
    return ""


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
        print("%-16s status=%-5s %6sms serviced=%-5s reasoning_echo=%-40s %s" % (
            variant["name"], record["status"], record["elapsed_ms"],
            record["serviced"], json.dumps(summary.get("echoed_reasoning"))[:40],
            detail_from(record, summary)))
        if record["status"] in (401, 403, 429):
            abort_reason = ("Phase A walled at %s: status=%s"
                            % (variant["name"], record["status"]))
            break
        if record["error_kind"] == "connect" and len(
                [r for r in phase_a[-2:] if r.get("error_kind") == "connect"]) >= 2:
            abort_reason = "two consecutive transport failures"
            break

    if abort_reason:
        print("ABORT after Phase A: %s" % abort_reason)

    # ---- Phase B: measurement for accepted values >= high -----------------
    accepted = [r["variant"] for r in phase_a
                if r["serviced"] and r["variant"] != "invalid-control"]
    if not abort_reason:
        order = [OMIT] + [v for v in VARIANTS if v["name"] in accepted]
        print("\nPhase B -- measurement (M3 perf probe, max_output_tokens=%d, n=2; "
              "omit control first)" % PERF_MAX_TOKENS)
        stop_b = False
        for variant in order:
            if stop_b:
                break
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
                print("%-6s rep=%d status=%-5s ttft=%-6s tps=%-8s span=%-6s "
                      "ctok=%-4s rtok=%-4s rdeltas=%-3s output_ok=%s" % (
                          variant["name"], rep, record["status"],
                          summary["ttft_content_ms"], summary["tps"],
                          summary["decode_span_ms"], summary["completion_tokens"],
                          summary["reasoning_tokens"], summary["reasoning_delta_count"],
                          record["output_ok"]))
                if record["status"] in (401, 403, 429):
                    stop_b = True
                    abort_reason = ("Phase B walled at rep %d of %s: status=%s"
                                    % (rep, variant["name"], record["status"]))
                    break
                if record["status"] != 200:
                    break  # one attempt per rep; move to the next variant

    run = {
        "mission": "M8 r18-codex-ultra-strong-entry",
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
        "variants": [{k: v for k, v in var.items()}
                     for var in (VARIANTS + [OMIT])],
        "phase_a": phase_a,
        "phase_b": phase_b,
    }
    out = common.write_json("ultra-probe.json", run)
    print("\nwrote %s (%d phase-A records, %d phase-B records, abort=%s)"
          % (out, len(phase_a), len(phase_b), abort_reason))


if __name__ == "__main__":
    main()