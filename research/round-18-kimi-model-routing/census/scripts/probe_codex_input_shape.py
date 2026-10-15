#!/usr/bin/env python3
"""Follow-up probe: find the request shape the openai-codex lane actually accepts.

    python3 scripts/probe_codex_input_shape.py

scripts/probe_chat.py sent `"input": "ping"` to
http://127.0.0.1:8789/backend-api/codex/responses and got HTTP 400
`{"detail": "Input must be a list"}`. That is a *probe shape* problem, not proof
that the lane is broken, so this script walks a small ladder of Responses-API
shapes and stops at the first one the backend accepts. Every attempt is recorded
so the defect list can quote the exact rejection.

Kept separate from probe_chat.py so its one-probe-per-provider contract stays
intact. Writes raw/chat-openai-codex-input-list.json.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_chat  # noqa: E402
import requests  # noqa: E402

URL = "http://127.0.0.1:8789/backend-api/codex/responses"
MODEL = "gpt-6.1-sol"
TIMEOUT_S = 180

LIST_INPUT = [
    {"type": "message", "role": "user",
     "content": [{"type": "input_text", "text": "ping"}]}
]

VARIANTS = [
    ("bare-string-input",
     {"model": MODEL, "max_output_tokens": 8, "temperature": 0, "input": "ping"}),
    ("list-input",
     {"model": MODEL, "max_output_tokens": 8, "temperature": 0, "input": LIST_INPUT}),
    ("list-input-store-false",
     {"model": MODEL, "max_output_tokens": 8, "temperature": 0,
      "input": LIST_INPUT, "store": False}),
    ("list-input-store-false-stream-true",
     {"model": MODEL, "max_output_tokens": 8, "temperature": 0,
      "input": LIST_INPUT, "store": False, "stream": True,
      "instructions": "Reply with one word."}),
    ("stream-true-no-temperature",
     {"model": MODEL, "max_output_tokens": 8, "input": LIST_INPUT,
      "store": False, "stream": True}),
    ("stream-true-minimal",
     {"model": MODEL, "input": LIST_INPUT, "store": False, "stream": True}),
]


def sse_summary(text):
    """Event types and usage from a text/event-stream body."""
    events, usage = [], None
    for line in (text or "").splitlines():
        line = line.strip()
        if line.startswith("event:"):
            events.append(line[6:].strip())
        elif line.startswith("data:"):
            payload = line[5:].strip()
            if not payload or payload == "[DONE]":
                continue
            try:
                obj = json.loads(payload)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(obj, dict):
                if obj.get("type"):
                    events.append(obj["type"])
                inner = obj.get("response")
                if isinstance(inner, dict) and isinstance(inner.get("usage"), dict):
                    usage = inner["usage"]
                if isinstance(obj.get("usage"), dict):
                    usage = obj["usage"]
    return events, usage


def attempt(variant, body, headers):
    record = {
        "provider": "openai-codex",
        "protocol": "openai_responses",
        "model_id": MODEL,
        "purpose": "input-shape-follow-up",
        "variant": variant,
        "method": "POST",
        "url": URL,
        "timeout_s": TIMEOUT_S,
        "auth_headers_sent": sorted(h for h in headers
                                    if h.lower() in common.SECRET_HEADER_NAMES),
        "request_body": body,
    }
    started = time.time()
    try:
        resp = requests.post(URL, headers=headers, json=body, timeout=TIMEOUT_S)
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = resp.status_code
        record["response_headers"] = probe_chat.probe_models.safe_headers(resp.headers)
        if "event-stream" in (resp.headers.get("Content-Type") or ""):
            events, usage = sse_summary(resp.text)
            record["sse_event_types"] = sorted(set(events))
            record["sse_event_count"] = len(events)
            record["sse_usage"] = usage
            record["body"] = common.redact(resp.text[:1500])
        else:
            record["body"] = common.parse_body(resp.content)
    except requests.exceptions.Timeout:
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "timeout"
        record["body"] = None
    except Exception as exc:  # noqa: BLE001
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "error"
        record["error"] = "%s: %s" % (type(exc).__name__, exc)
        record["body"] = None
    record["shape"] = probe_chat.shape(record["body"])
    return record


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    headers = common.auth_headers(cfg["providers"]["openai-codex"], "openai_responses")

    probes, accepted = [], None
    for variant, body in VARIANTS:
        record = attempt(variant, body, headers)
        probes.append(record)
        detail = ""
        if isinstance(record["body"], dict):
            detail = str(record["body"].get("detail")
                         or record["body"].get("error") or "")[:120]
        print("%-36s status=%-7s %6sms %s" % (
            variant, record["status"], record["latency_ms"], detail))
        if record["status"] == 200:
            accepted = variant
            break

    common.write_json("chat-openai-codex-input-list.json", {
        "accepted_variant": accepted,
        "probes": probes,
    })
    print("accepted variant: %s" % (accepted or "NONE (all shapes rejected)"))


if __name__ == "__main__":
    main()
