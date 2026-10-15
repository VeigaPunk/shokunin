#!/usr/bin/env python3
"""Streaming smoke: TTFT and decode throughput (TPS) per provider lane.

    python3 scripts/probe_stream.py [config.toml]

Operator add-on. One streaming request per lane with a fixed identical short
prompt and max_tokens ~ 64, so the lanes are compared on the same draw:

  TTFT  = ms from request send to the first content-bearing chunk
  TPS   = (completion_tokens - 1) / ((last_token - first_token) / 1000)

Server-side `usage.completion_tokens` is the preferred TPS denominator; when a
lane streams no usage block the observed delta count is used instead and the
basis is recorded explicitly.

Streaming is *not forced*: a lane that answers with one complete JSON body, or
errors on `stream: true`, is recorded as not streaming rather than retried into
submission. Captures land in raw/stream-<lane>.json.

These are smoke-level numbers from a single small draw per lane; the powered
n>=2 benchmark belongs to the M3 battery.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_chat  # noqa: E402
import requests  # noqa: E402

PROMPT = "Count from 1 to 30, space separated, numbers only. No other text."
MAX_TOKENS = 64
DEFAULT_TIMEOUT_S = 120
PROVIDER_TIMEOUT_S = {"devin": 300, "cursor": 300}
MAX_LINES = 20000
# Minimum first-token→last-token span for a TPS figure to mean anything.
MIN_DECODE_SPAN_MS = 50


def body_for(model_id, protocol, stream, codex=False):
    b = {"model": model_id, "stream": stream}
    if protocol == "anthropic":
        b.update({"max_tokens": MAX_TOKENS, "temperature": 0,
                  "messages": [{"role": "user", "content": PROMPT}]})
    elif protocol == "openai_responses":
        b.update({"max_output_tokens": MAX_TOKENS,
                  "input": [{"type": "message", "role": "user",
                             "content": [{"type": "input_text", "text": PROMPT}]}]})
        if codex:
            # The Codex backend rejects store=true outright and refuses any
            # non-streaming request; probe_stream already streams.
            b["store"] = False
    else:
        b.update({"max_tokens": MAX_TOKENS, "temperature": 0,
                  "messages": [{"role": "user", "content": PROMPT}]})
        if protocol == "openai":
            b["stream_options"] = {"include_usage": True}
    return b


def extract(line, protocol):
    """(kind, text, usage) for one SSE line; kind is content|reasoning|None."""
    if not line.startswith("data:"):
        return None, None, None
    payload = line[5:].strip()
    if not payload or payload == "[DONE]":
        return None, None, None
    try:
        obj = json.loads(payload)
    except Exception:  # noqa: BLE001
        return None, None, None
    if not isinstance(obj, dict):
        return None, None, None

    usage = obj.get("usage") if isinstance(obj.get("usage"), dict) else None
    if usage is None and isinstance(obj.get("message"), dict) \
            and isinstance(obj["message"].get("usage"), dict):
        usage = obj["message"]["usage"]
    # The Responses protocol reports usage on the terminal `response.completed`
    # event, nested under `response`, not at the top level.
    if usage is None and isinstance(obj.get("response"), dict) \
            and isinstance(obj["response"].get("usage"), dict):
        usage = obj["response"]["usage"]

    if protocol == "anthropic":
        delta = obj.get("delta") or {}
        if isinstance(delta, dict):
            if delta.get("text"):
                return "content", delta["text"], usage
            if delta.get("thinking"):
                return "reasoning", delta["thinking"], usage
        return None, None, usage

    if protocol == "openai_responses":
        t = obj.get("type")
        if t == "response.output_text.delta" and obj.get("delta"):
            return "content", obj["delta"], usage
        if t in ("response.reasoning_summary_text.delta",
                 "response.reasoning_text.delta") and obj.get("delta"):
            return "reasoning", obj["delta"], usage
        return None, None, usage

    choices = obj.get("choices")
    if isinstance(choices, list) and choices:
        ch0 = choices[0] or {}
        delta = ch0.get("delta") or {}
        if isinstance(delta, dict):
            if delta.get("content"):
                return "content", delta["content"], usage
            if delta.get("reasoning_content"):
                return "reasoning", delta["reasoning_content"], usage
        if ch0.get("text"):
            return "content", ch0["text"], usage
    return None, None, usage


def completion_tokens_from(usage):
    if not isinstance(usage, dict):
        return None
    for k in ("completion_tokens", "output_tokens"):
        if isinstance(usage.get(k), int):
            return usage[k]
    return None


def probe(provider, protocol, model_id, url, headers, timeout):
    body = body_for(model_id, protocol, True, codex=(provider == "openai-codex"))
    record = {
        "provider": provider, "protocol": protocol, "model_id": model_id,
        "method": "POST", "url": url, "timeout_s": timeout,
        "prompt": PROMPT, "max_tokens": MAX_TOKENS,
        "auth_headers_sent": sorted(h for h in headers
                                    if h.lower() in common.SECRET_HEADER_NAMES),
        "request_body": body,
    }
    started = time.monotonic()
    t_first_content = t_first_reasoning = t_last = None
    content_parts, reasoning_parts = [], []
    usage = None
    line_count = 0
    try:
        with requests.post(url, headers=headers, json=body, timeout=timeout,
                           stream=True) as resp:
            record["status"] = resp.status_code
            record["response_headers"] = probe_chat.probe_models.safe_headers(resp.headers)
            ctype = resp.headers.get("Content-Type") or ""
            record["content_type"] = ctype or None
            raw_lines = []
            for line in resp.iter_lines(decode_unicode=True):
                if line is None:
                    continue
                # iter_lines only decodes when the response advertises a charset;
                # a shim that forwards no Content-Type yields raw bytes.
                if isinstance(line, bytes):
                    line = line.decode("utf-8", "replace")
                line_count += 1
                if len(raw_lines) < 200:
                    raw_lines.append(line)
                if line_count > MAX_LINES:
                    break
                kind, text, u = extract(line, protocol)
                if u:
                    usage = u
                if kind and text:
                    now = time.monotonic()
                    if kind == "content":
                        if t_first_content is None:
                            t_first_content = now
                        content_parts.append(text)
                    else:
                        if t_first_reasoning is None:
                            t_first_reasoning = now
                        reasoning_parts.append(text)
                    t_last = now
            record["sse_line_count"] = line_count
            record["raw_preview"] = common.redact("\n".join(raw_lines)[:1500])
    except requests.exceptions.Timeout:
        record["status"] = "timeout"
        record["error"] = "no response within %ds" % timeout
    except Exception as exc:  # noqa: BLE001
        record["status"] = "error"
        record["error"] = "%s: %s" % (type(exc).__name__, exc)

    total_s = time.monotonic() - started
    if record.get("status") == 200 and not content_parts and not reasoning_parts:
        # No incremental deltas: either a single JSON body (local shims) or an
        # unparsed stream. Try the body as one complete response.
        record["streaming_supported"] = False
        record["note"] = "no incremental content deltas observed"
    else:
        record["streaming_supported"] = bool(content_parts or reasoning_parts)

    record["content_chars"] = sum(len(p) for p in content_parts)
    record["reasoning_chars"] = sum(len(p) for p in reasoning_parts)
    record["content_delta_count"] = len(content_parts)
    record["reasoning_delta_count"] = len(reasoning_parts)
    record["content_sample"] = "".join(content_parts)[:200]
    record["ttft_content_ms"] = (round((t_first_content - started) * 1000)
                                 if t_first_content else None)
    record["ttft_reasoning_ms"] = (round((t_first_reasoning - started) * 1000)
                                   if t_first_reasoning else None)
    record["total_ms"] = round(total_s * 1000)
    record["usage"] = usage
    record["usage_completion_tokens"] = completion_tokens_from(usage)
    record["usage_prompt_tokens"] = (usage or {}).get("prompt_tokens") \
        or (usage or {}).get("input_tokens")

    span_ms = ((t_last - t_first_content) * 1000
               if (t_last and t_first_content) else None)
    record["decode_span_ms"] = round(span_ms) if span_ms is not None else None
    tokens = record["usage_completion_tokens"]
    if tokens is None:
        tokens = len(content_parts) or None
        record["tps_basis"] = "observed_content_deltas" if tokens else None
    else:
        record["tps_basis"] = "server_usage_completion_tokens"
    # A decode span below MIN_DECODE_SPAN_MS means the lane delivered its tokens in
    # one buffered burst rather than incrementally, so a TPS derived from it is an
    # artefact of measurement, not throughput. Report it as not derivable instead.
    if tokens and tokens > 1 and span_ms and span_ms >= MIN_DECODE_SPAN_MS:
        record["tps"] = round((tokens - 1) / (span_ms / 1000.0), 2)
    else:
        record["tps"] = None
    if record["tps"] is not None:
        record["tps_note"] = "single small draw; decode span excludes TTFT"
    elif span_ms is not None and span_ms < MIN_DECODE_SPAN_MS:
        record["tps_note"] = ("not derivable: stream was not incrementally flushed "
                              "(decode span %s ms < %d ms)" % (round(span_ms), MIN_DECODE_SPAN_MS))
    else:
        record["tps_note"] = "not derivable (no incremental deltas or <2 tokens)"
    return record


def load_stream(provider):
    path = os.path.join(common.RAW_DIR, "stream-%s.json" % common.slug(provider))
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    only = [p for p in (sys.argv[2].split(",") if len(sys.argv) > 2 else []) if p]
    cfg = common.load_config(path)
    providers = cfg.get("providers", {})
    models = cfg.get("models", {})

    by_provider = {}
    for mid, mcfg in models.items():
        by_provider.setdefault(mcfg.get("provider"), []).append((mid, mcfg))

    summary = []
    for pname, pcfg in providers.items():
        if only and pname not in only:
            continue
        entries = by_provider.get(pname, [])
        if not entries:
            continue
        groups = {}
        for _mid, mcfg in entries:
            groups.setdefault(common.effective_protocol(pcfg, mcfg), []).append(mcfg)
        default_protocol = common.effective_protocol(pcfg)
        ordered = [default_protocol] + sorted(p for p in groups if p != default_protocol)
        probes = []
        for protocol in ordered:
            # Prefer a flash/cheap entry: the streaming probe should not spend
            # the flagship model's quota.
            pick = next((m for m in groups[protocol]
                         if "flash" in str(m.get("model"))), groups[protocol][0])
            url = probe_chat.chat_url(common.effective_base_url(pcfg, pick), protocol)
            headers = common.auth_headers(pcfg, protocol)
            rec = probe(pname, protocol, pick.get("model"), url, headers,
                        PROVIDER_TIMEOUT_S.get(pname, DEFAULT_TIMEOUT_S))
            probes.append(rec)
            print("%-24s %-18s %-24s status=%-7s stream=%-5s ttft=%-7s tps=%-7s ctok=%s" % (
                pname, protocol, rec["model_id"], rec.get("status"),
                rec.get("streaming_supported"), rec.get("ttft_content_ms"),
                rec.get("tps"), rec.get("usage_completion_tokens")))
            if rec.get("error"):
                print("    error: %s" % rec["error"])
        common.write_json("stream-%s.json" % common.slug(pname), {"probes": probes})
        summary.extend(probes)

    # Rebuild from every stream-<lane>.json on disk rather than from the in-memory
    # list, so a filtered re-run of a single lane cannot truncate the summary.
    on_disk = []
    for pname in providers:
        data = load_stream(pname)
        if data:
            on_disk.extend(data.get("probes", []))
    common.write_json("stream-summary.json", {"probes": on_disk})


if __name__ == "__main__":
    main()
