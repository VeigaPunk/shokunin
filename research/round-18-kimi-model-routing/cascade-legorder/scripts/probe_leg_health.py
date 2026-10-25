#!/usr/bin/env python3
"""Direct single-lane health probe (no shim in the path).

    python3 probe_leg_health.py --provider alibaba-token-plan --model deepseek-v4.1-flash --out raw/leg-health-<name>.json
    python3 probe_leg_health.py --provider alibaba-token-plan --model deepseek-v4.1-flash --out out.json --triplet  # probes key 1, 2, 3

Reads the provider's base_url/api_key from ~/.kimi-code/config.toml inside this
process. The key is never printed, logged, or written to the capture: only the
status, the relayed response headers, the body (which carries the provider's own
quota message when it refuses) and the request shape leave it.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import tomllib
import urllib.error
import urllib.request

CONFIG = os.path.expanduser("~/.kimi-code/config.toml")


def probe(provider_cfg: dict, model: str, timeout: int = 60) -> dict:
    url = provider_cfg["base_url"].rstrip("/") + "/chat/completions"
    body = {"model": model, "max_tokens": 8, "temperature": 0,
            "messages": [{"role": "user", "content": "ping"}]}
    headers = {"Content-Type": "application/json"}
    key = provider_cfg.get("api_key")
    if isinstance(key, str) and key:
        headers["Authorization"] = "Bearer " + key
    headers.update({k: v for k, v in (provider_cfg.get("custom_headers") or {}).items()})
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers=headers)
    rec = {"url": url, "model": model, "auth_header_sent": "Authorization" in headers,
           "request_body": body}
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            rec["status"] = resp.status
            rec["headers"] = dict(resp.headers)
    except urllib.error.HTTPError as exc:
        rec["status"] = exc.code
        rec["headers"] = dict(exc.headers)
        raw = exc.read()
    except Exception as exc:  # noqa: BLE001
        rec["status"] = "error"
        rec["error"] = "%s: %s" % (type(exc).__name__, exc)
        raw = b""
    rec["latency_ms"] = round((time.time() - started) * 1000)
    try:
        rec["body"] = json.loads(raw)
    except Exception:
        rec["body"] = raw.decode("utf-8", "replace")[:2000]
    return rec


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--triplet", action="store_true",
                    help="also probe <provider>-2 and <provider>-3 (the other keys of the same plan)")
    args = ap.parse_args()

    with open(CONFIG, "rb") as fh:
        cfg = tomllib.load(fh)
    providers = cfg.get("providers", {})

    names = [args.provider]
    if args.triplet:
        names += [args.provider + "-2", args.provider + "-3"]
    doc = {"config": CONFIG, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "probes": []}
    for name in names:
        pcfg = providers.get(name)
        if pcfg is None:
            print("%-28s (no such provider in config.toml)" % name)
            continue
        rec = probe(pcfg, args.model)
        rec["provider"] = name
        doc["probes"].append(rec)
        err = ""
        if isinstance(rec.get("body"), dict):
            e = rec["body"].get("error")
            err = (e.get("message") if isinstance(e, dict) else str(e))[:160] if e else ""
        print("%-28s status=%-6s %5sms %s" % (name, rec["status"], rec["latency_ms"], err))

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
