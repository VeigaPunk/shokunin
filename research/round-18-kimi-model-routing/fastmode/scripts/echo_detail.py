#!/usr/bin/env python3
"""Event-level echo detail for the fast-mode probe's two key variants.

    python3 scripts/echo_detail.py [config.toml]

The main probe keeps only the last `service_tier` echo per stream plus a
3000-char preview, which is not enough to answer "did the backend service the
priority request at priority?" -- the first echo (response.created) and the
last echo can differ, and the preview does not reach the later events. This
script re-issues the two key variants once each at the minimal cost (same D6
shape, max_output_tokens 16, prompt "ping") and stores every SSE data line, so
the echo can be read event by event and quoted.

Output: raw/echo-detail.json -- no key material; the request header map is
redacted the same way the probe redacts it.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_fastmode as pf  # noqa: E402

VARIANTS = [
    {"name": "omit", "patch": {}},
    {"name": "priority", "patch": {"service_tier": "priority"}},
]


def event_echoes(capture):
    """Every event carrying a service_tier value, in stream order."""
    echoes, data_lines = [], []
    for index, (text, _when) in enumerate(capture["lines"]):
        if not text.startswith("data:"):
            continue
        payload = text[5:].strip()
        if not payload or payload == "[DONE]":
            continue
        data_lines.append(payload)
        try:
            obj = json.loads(payload)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(obj, dict):
            continue
        response = obj.get("response") if isinstance(obj.get("response"), dict) else {}
        if isinstance(response.get("service_tier"), str):
            echoes.append({
                "line_index": index,
                "event_type": obj.get("type"),
                "sequence_number": obj.get("sequence_number"),
                "service_tier": response["service_tier"],
                "status": response.get("status"),
            })
    return echoes, data_lines


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    base_url = cfg["providers"][pf.PROVIDER]["base_url"].rstrip("/")
    url = base_url + "/responses"
    headers = common.request_headers(cfg, pf.PROVIDER)
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    records = []
    for variant in VARIANTS:
        body = pf.build_body(pf.ACCEPT_PROMPT, pf.ACCEPT_MAX_TOKENS, variant["patch"])
        capture = common.post_streaming(url, headers, body, pf.TIMEOUT_S)
        echoes, data_lines = event_echoes(capture)
        stream = pf.parse_capture(capture)
        summary = pf.summarize(stream)
        records.append({
            "variant": variant["name"],
            "patch": variant["patch"],
            "url": url,
            "method": "POST",
            "request_headers_sent": common.redact_headers(headers),
            "request_body": body,
            "request_body_json": json.dumps(body),
            "status": capture["status"],
            "error": capture["error"],
            "error_kind": capture["error_kind"],
            "response_headers": capture["response_headers"],
            "service_tier_echoes": echoes,
            "summary": {k: summary[k] for k in (
                "echoed_service_tier", "ttft_content_ms", "sse_event_count",
                "completion_tokens", "prompt_tokens")},
            "data_line_count": len(data_lines),
            "data_lines": data_lines,
        })
        print("%-9s status=%s echoes=%s last=%s events=%d" % (
            variant["name"], capture["status"],
            [(e["event_type"], e["service_tier"]) for e in echoes],
            summary["echoed_service_tier"], summary["sse_event_count"]))

    out = common.write_json("echo-detail.json", {
        "mission": "M5 r18-codex-fast-mode-probe",
        "model": pf.MODEL,
        "url": url,
        "config_json_digest_16": common.config_digest(cfg),
        "started_at_utc": started,
        "record": records,
    })
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
