#!/usr/bin/env python3
"""Follow-up probes that the first pass could not settle.

    python3 scripts/probe_rechecks.py [config.toml]

1. token-plan keys 2 and 3 returned 429 `insufficient_quota` on qwen3.7-max.
   Re-probe the *fast* model each lane is actually routed to
   (deepseek-v4.1-flash) to establish whether the whole lane is exhausted or
   just the flagship model. Exhausted lanes reject without burning quota.
2. The devin lane's chat probe hit the 180s timeout. Re-probe once with a 300s
   ceiling to separate a cold `devin acp` start from a permanently dead path.

Writes raw/recheck-*.json.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_chat  # noqa: E402
import requests  # noqa: E402

QUOTA_RECHECKS = [
    ("alibaba-token-plan-2", "deepseek-v4.1-flash"),
    ("alibaba-token-plan-3", "deepseek-v4.1-flash"),
]
DEVIN_RETRY_TIMEOUT_S = 300


def post(provider, model_id, timeout, purpose, cfg):
    pcfg = cfg["providers"][provider]
    protocol = common.effective_protocol(pcfg)
    url = probe_chat.chat_url(common.effective_base_url(pcfg), protocol)
    headers = common.auth_headers(pcfg, protocol)
    body = probe_chat.chat_body(model_id, protocol)
    record = {
        "provider": provider, "protocol": protocol, "model_id": model_id,
        "purpose": purpose, "method": "POST", "url": url, "timeout_s": timeout,
        "auth_headers_sent": sorted(h for h in headers
                                    if h.lower() in common.SECRET_HEADER_NAMES),
        "request_body": body,
    }
    started = time.time()
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=timeout)
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = resp.status_code
        record["response_headers"] = probe_chat.probe_models.safe_headers(resp.headers)
        record["body"] = common.parse_body(resp.content)
    except requests.exceptions.Timeout:
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "timeout"
        record["error"] = "no response within %ds" % timeout
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

    quota = [post(p, m, 60, "quota-lane-fast-model-recheck", cfg)
             for p, m in QUOTA_RECHECKS]
    common.write_json("recheck-quota-lanes.json", {"probes": quota})
    for r in quota:
        print("%-24s %-22s status=%-5s %sms err=%s" % (
            r["provider"], r["model_id"], r["status"], r["latency_ms"],
            r["shape"]["error_message"] or "-"))

    # Opt-in: on the first pass the devin chat path timed out twice (180 s, then
    # 300 s) on a cold shim. Later probes returned in seconds, so re-running this
    # leg is only worth 300 s when the cold-start question comes back.
    if os.environ.get("R18_DEVIN_RETRY") == "1":
        devin = post("devin", "swe-2", DEVIN_RETRY_TIMEOUT_S, "cold-start-retry", cfg)
        common.write_json("recheck-devin-chat.json", {"probes": [devin]})
        print("%-24s %-22s status=%-5s %sms" % (
            "devin", "swe-2", devin["status"], devin["latency_ms"]))


if __name__ == "__main__":
    main()
