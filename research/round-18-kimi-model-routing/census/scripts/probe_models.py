#!/usr/bin/env python3
"""Probe GET {base_url}/models for every provider and record the served ids.

    python3 scripts/probe_models.py [config.toml]

One GET per provider (5s timeout), plus supplementary GETs for every distinct
model-level `base_url` override so a per-model transport that differs from its
provider is probed too. Raw captures land in raw/models-<provider>.json with
Authorization and api_key material stripped; only rate-limit / tracing response
headers keep their values.
"""
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import requests  # noqa: E402

TIMEOUT_S = 5

SAFE_HEADER_RE = re.compile(
    r"^(content-type|content-length|date|server|retry-after"
    r"|x-request-id|x-oai-request-id|request-id|x-trace-id|traceparent|cf-ray"
    r"|x-models-etag"
    r"|x-ratelimit-.*|ratelimit-.*|anthropic-ratelimit-.*|x-should-retry"
    r"|x-amzn-requestid|x-envoy-[a-z-]*"
    # x-codex-* carries the ChatGPT-plan quota telemetry we want as evidence;
    # turn-state is a per-turn opaque blob, so it stays redacted.
    r"|x-codex-(?!turn-state)[a-z-]*)$",
    re.I,
)
UNSAFE_SUBSTRINGS = ("auth", "session", "key", "token", "cookie", "secret")


def safe_headers(headers):
    """Header map safe to persist: allow-listed names keep their value.

    The allow-list is consulted *first*. Otherwise a name like
    `x-ratelimit-limit-tokens` would be redacted merely for containing the word
    "token", hiding real quota telemetry that the census is supposed to capture.
    Nothing on the allow-list carries credential material, so this ordering is
    strictly safer for evidence and no less safe for secrets.
    """
    out = {}
    for name, value in headers.items():
        low = name.lower()
        if SAFE_HEADER_RE.match(low):
            out[name] = value
        elif any(s in low for s in UNSAFE_SUBSTRINGS):
            out[name] = "<redacted:len=%d>" % len(value)
        else:
            out[name] = "<len=%d>" % len(value)
    return out


def extract_ids(body):
    if isinstance(body, dict) and isinstance(body.get("data"), list):
        return [d.get("id") for d in body["data"] if isinstance(d, dict) and d.get("id")]
    if isinstance(body, dict) and isinstance(body.get("models"), list):
        return [d.get("id") or d.get("name") for d in body["models"] if isinstance(d, dict)]
    return []


def probe(provider_name, url, headers, kind, note=None):
    record = {
        "provider": provider_name,
        "kind": kind,
        "method": "GET",
        "url": url,
        "auth_headers_sent": sorted(h for h in headers if h.lower() in common.SECRET_HEADER_NAMES),
    }
    if note:
        record["note"] = note
    started = time.time()
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT_S)
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = resp.status_code
        record["response_headers"] = safe_headers(resp.headers)
        record["body"] = common.parse_body(resp.content)
        record["served_ids"] = extract_ids(record["body"])
        record["served_id_count"] = len(record["served_ids"])
    except requests.exceptions.Timeout:
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "timeout"
        record["error"] = "no response within %ds" % TIMEOUT_S
    except Exception as exc:  # noqa: BLE001 - census wants the failure recorded
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "error"
        record["error"] = "%s: %s" % (type(exc).__name__, exc)
    return record


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    providers = cfg.get("providers", {})
    models = cfg.get("models", {})

    index = {}
    for mid, mcfg in models.items():
        pname = mcfg.get("provider")
        if not pname:
            continue
        index.setdefault(pname, []).append(mid)

    summary = []
    for pname, pcfg in providers.items():
        base_url = common.effective_base_url(pcfg)
        protocol = common.effective_protocol(pcfg)
        headers = common.auth_headers(pcfg, protocol)
        probes = [probe(pname, base_url + "/models", headers, "provider-base-url")]

        overrides = sorted({
            m["base_url"] for m in models.values()
            if m.get("provider") == pname and m.get("base_url")
            and m["base_url"].rstrip("/") != base_url
        })
        for ov in overrides:
            probes.append(probe(pname, ov.rstrip("/") + "/models", headers,
                                "model-base-url-override", note="declared on model entry"))

        if pname == "openai-codex":
            probes.append(probe(pname, "http://127.0.0.1:8789/v1/models", headers,
                                "shim-static-route",
                                note="shim SHIM_MODELS static list; provider base_url points at /backend-api/codex"))

        configured = sorted({models[mid].get("model") for mid in index.get(pname, [])})
        resolved = sorted({i for p in probes for i in p.get("served_ids", [])})
        payload = {
            "provider": pname,
            "protocol": protocol,
            "configured_model_ids": configured,
            "configured_model_id_count": len(configured),
            "resolved_model_ids": sorted(set(configured) & set(resolved)),
            "unresolved_model_ids": sorted(set(configured) - set(resolved)),
            "probes": probes,
        }
        common.write_json("models-%s.json" % common.slug(pname), payload)
        summary.append({
            "provider": pname,
            "protocol": protocol,
            "primary_status": probes[0]["status"],
            "primary_latency_ms": probes[0]["latency_ms"],
            "served_id_count": probes[0].get("served_id_count", 0),
            "configured_ids": len(configured),
            "resolved_ids": len(payload["resolved_model_ids"]),
        })
        print("%-24s %-18s status=%-8s served=%-5s configured=%-4s resolved=%s" % (
            pname, protocol, probes[0]["status"],
            probes[0].get("served_id_count", "-"), len(configured),
            len(payload["resolved_model_ids"])))

    common.write_json("models-summary.json", {"summary": summary})


if __name__ == "__main__":
    main()
