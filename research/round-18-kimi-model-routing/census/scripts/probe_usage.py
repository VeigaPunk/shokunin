#!/usr/bin/env python3
"""Usage/quota evidence for the first two provider lanes in config table order.

    python3 scripts/probe_usage.py [config.toml]

Lanes: `managed:kimi-code` and `alibaba-token-plan` (key 1).

Two signal sources, both using only the credentials already in the config:
  1. the `usage` block and rate-limit headers of the minimal chat probe already
     recorded in raw/chat-<lane>.json (read, not re-issued -- no extra quota),
  2. a bounded set of GETs against plausible usage/account paths on the lane's
     own base_url host. Paths are *probed and reported*, never assumed to exist.

Writes raw/usage-<lane>.json.
"""
import json
import os
import sys
import time
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_models  # noqa: E402
import requests  # noqa: E402

TIMEOUT_S = 5
LANES = ["managed:kimi-code", "alibaba-token-plan"]

# Relative to the lane's declared base_url, plus host-root variants.
BASE_URL_PATHS = ["/usage", "/user/balance", "/dashboard/billing/usage", "/quota", "/account/usage"]
ORIGIN_PATHS = ["/usage", "/v1/usage"]


def body_shape(body):
    if isinstance(body, dict):
        return {
            "top_level_keys": sorted(body.keys()),
            "preview": json.dumps(body)[:300],
        }
    if isinstance(body, str):
        return {"top_level_keys": None, "preview": body[:300]}
    return {"top_level_keys": None, "preview": None}


def get(url, headers):
    rec = {"method": "GET", "url": url,
           "auth_headers_sent": sorted(h for h in headers
                                       if h.lower() in common.SECRET_HEADER_NAMES)}
    started = time.time()
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT_S)
        rec["latency_ms"] = round((time.time() - started) * 1000)
        rec["status"] = resp.status_code
        rec["response_headers"] = probe_models.safe_headers(resp.headers)
        body = common.parse_body(resp.content)
        rec["body_shape"] = body_shape(body)
    except requests.exceptions.Timeout:
        rec["latency_ms"] = round((time.time() - started) * 1000)
        rec["status"] = "timeout"
        rec["body_shape"] = {"top_level_keys": None, "preview": None}
    except Exception as exc:  # noqa: BLE001
        rec["latency_ms"] = round((time.time() - started) * 1000)
        rec["status"] = "error"
        rec["body_shape"] = {"top_level_keys": None, "preview": "%s: %s" % (type(exc).__name__, exc)}
    return rec


def chat_evidence(lane):
    """Pull usage + rate-limit headers out of the already-captured chat probe."""
    path = os.path.join(common.RAW_DIR, "chat-%s.json" % common.slug(lane))
    if not os.path.exists(path):
        return {"source": path, "available": False,
                "note": "run scripts/probe_chat.py first"}
    with open(path) as fh:
        data = json.load(fh)
    out = {"source": os.path.basename(path), "available": True, "probes": []}
    for p in data.get("probes", []):
        body = p.get("body")
        usage = body.get("usage") if isinstance(body, dict) else None
        rate_headers = {k: v for k, v in (p.get("response_headers") or {}).items()
                        if "ratelimit" in k.lower() or k.lower() in
                        ("retry-after", "x-request-id", "request-id")}
        out["probes"].append({
            "model_id": p.get("model_id"),
            "status": p.get("status"),
            "latency_ms": p.get("latency_ms"),
            "usage": usage,
            "usage_present": isinstance(usage, dict),
            "rate_limit_headers": rate_headers,
            "shape": p.get("shape"),
        })
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    providers = cfg.get("providers", {})
    results = []

    for lane in LANES:
        pcfg = providers.get(lane)
        if pcfg is None:
            results.append({"lane": lane, "error": "provider not present in config"})
            continue
        protocol = common.effective_protocol(pcfg)
        base_url = common.effective_base_url(pcfg)
        headers = common.auth_headers(pcfg, protocol)
        origin = "{u.scheme}://{u.netloc}".format(u=urlparse(base_url))

        urls = [base_url + p for p in BASE_URL_PATHS] + [origin + p for p in ORIGIN_PATHS]
        seen, probes = set(), []
        for url in urls:
            if url in seen:
                continue
            seen.add(url)
            probes.append(get(url, headers))

        record = {
            "lane": lane,
            "auth": "oauth" if pcfg.get("oauth") else "api_key",
            "api_key_present": bool(pcfg.get("api_key")),
            "protocol": protocol,
            "base_url": base_url,
            "chat_probe_evidence": chat_evidence(lane),
            "account_endpoint_probes": probes,
        }
        common.write_json("usage-%s.json" % common.slug(lane), record)
        results.append(record)
        print("=== %s (%s) ===" % (lane, record["auth"]))
        for p in probes:
            print("  %-3s %-70s %s" % (p["status"], p["url"], p["body_shape"]["preview"] or ""))
        ev = record["chat_probe_evidence"]
        if ev.get("available"):
            for p in ev["probes"]:
                print("  chat usage: model=%s status=%s usage=%s" % (
                    p["model_id"], p["status"], json.dumps(p["usage"])))

    common.write_json("usage-summary.json", {"lanes": results})


if __name__ == "__main__":
    main()
