#!/usr/bin/env python3
"""Probe the ds-flash-shim cascade and identify the leg that served.

    python3 probe_cascade.py --out raw/<name>.json [--port 8791] [--model deepseek-v4.1-flash]

Sends GET /health, GET /v1/models, one non-streaming and one streaming chat
completion, and records status, latency, the full relayed response-header set and
the body. The serving leg is identified from response-header signatures (the shim
relays every non-hop-by-hop upstream header, so the answering provider's gateway
headers reach the caller verbatim):

  alibaba-token-plan  server: istio-envoy, x-envoy-upstream-service-time, req-arrive-time/resp-start-time
  hyper               server: Google Frontend, x-ratelimit-limit-day/hour, traceparent
  opencode-go         CF-RAY, x-opencode-endpoint-id, x-opencode-upstream-model-id, x-zen-model

The shim's own stderr log names the leg even more directly (`leg=N/<name> OK`);
the caller captures that slice of the journal alongside the raw JSON.

No credential material is read, written or printed by this script.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request

LEG_SIGNATURES = (
    ("alibaba-token-plan", ("x-envoy-upstream-service-time", "req-arrive-time",
                            "resp-start-time", "istio-envoy")),
    ("hyper", ("x-ratelimit-limit-day", "x-ratelimit-limit-hour", "traceparent",
               "google frontend")),
    ("opencode-go", ("x-opencode-endpoint-id", "x-opencode-upstream-model-id",
                     "x-zen-model", "cf-ray")),
)

HOP = {"transfer-encoding", "connection", "keep-alive", "content-length"}


def identify(headers: dict) -> dict:
    """Name the leg whose signature is present; report every match, not just the first."""
    low = {k.lower(): str(v) for k, v in headers.items()}
    el = {k: low.get(k) for k in low}
    hits = {}
    for leg, markers in LEG_SIGNATURES:
        found = [m for m in markers if m in el]
        hits[leg] = found
    named = [leg for leg, found in hits.items() if found]
    return {"leg_by_signature": named[0] if len(named) == 1 else None,
            "signature_matches": hits,
            "ambiguous": len(named) > 1}


def record_headers(headers) -> dict:
    out = {}
    for k, v in headers.items():
        if k.lower() in HOP:
            continue
        out[k] = v
    return out


def call(url, method="GET", body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            return {"status": resp.status, "latency_ms": round((time.time() - started) * 1000),
                    "headers": record_headers(resp.headers), "raw": raw}
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        return {"status": exc.code, "latency_ms": round((time.time() - started) * 1000),
                "headers": record_headers(exc.headers), "raw": raw,
                "error_body": raw.decode("utf-8", "replace")[:2000]}


def body_of(rec):
    raw = rec.pop("raw", b"")
    try:
        return json.loads(raw)
    except Exception:
        return raw.decode("utf-8", "replace")[:2000]


def stream_call(url, body, timeout=180):
    """Read an SSE stream, recording TTFT, first-byte latency, byte count and a tail preview."""
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Content-Type": "application/json",
                                          "Accept": "text/event-stream"})
    started = time.time()
    out = {"ttft_ms": None, "first_byte_ms": None, "bytes": 0,
           "events": 0, "content_started": False}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            out["status"] = resp.status
            out["headers"] = record_headers(resp.headers)
            buf = b""
            while True:
                chunk = resp.read(4096)
                if not chunk:
                    break
                if out["first_byte_ms"] is None:
                    out["first_byte_ms"] = round((time.time() - started) * 1000)
                out["bytes"] += len(chunk)
                buf += chunk
                while b"\n\n" in buf:
                    frame, buf = buf.split(b"\n\n", 1)
                    out["events"] += 1
                    text = frame.decode("utf-8", "replace")
                    if out["ttft_ms"] is None and ("content" in text or "reasoning" in text):
                        payload = [l[6:] for l in text.splitlines() if l.startswith("data: ")]
                        if any(p.strip() and p.strip() != "[DONE]" for p in payload):
                            out["ttft_ms"] = round((time.time() - started) * 1000)
                    if "content" in text:
                        out["content_started"] = True
            out["total_ms"] = round((time.time() - started) * 1000)
    except urllib.error.HTTPError as exc:
        out["status"] = exc.code
        out["headers"] = record_headers(exc.headers)
        out["error_body"] = exc.read().decode("utf-8", "replace")[:2000]
    except Exception as exc:  # noqa: BLE001
        out["status"] = "error"
        out["error"] = "%s: %s" % (type(exc).__name__, exc)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--port", type=int, default=8791)
    ap.add_argument("--model", default="deepseek-v4.1-flash")
    ap.add_argument("--base", default=None, help="override host:port base, e.g. 127.0.0.1:8791")
    args = ap.parse_args()

    base = "http://%s" % (args.base or ("127.0.0.1:%d" % args.port))
    chat_body = {"model": args.model, "max_tokens": 8, "temperature": 0,
                 "messages": [{"role": "user", "content": "ping"}]}
    stream_body = dict(chat_body, stream=True, stream_options={"include_usage": True})

    doc = {"base": base, "model": args.model, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}

    health = call(base + "/health")
    doc["health"] = health | {"body": body_of(health)}
    doc["health_legs"] = (doc["health"]["body"] or {}).get("legs") if isinstance(doc["health"]["body"], dict) else None

    models = call(base + "/models")
    doc["models"] = models | {"body": body_of(models)}

    chat = call(base + "/v1/chat/completions", "POST", chat_body)
    doc["chat"] = chat | {"body": body_of(chat)}
    doc["chat"]["identity"] = identify(doc["chat"]["headers"])

    doc["stream"] = stream_call(base + "/v1/chat/completions", stream_body)
    doc["stream"]["identity"] = identify(doc["stream"]["headers"])

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True)
        fh.write("\n")

    print("health legs:      %s" % (doc["health_legs"],))
    print("models:           status=%s ids=%s" % (
        doc["models"]["status"],
        [m.get("id") for m in (doc["models"]["body"] or {}).get("data", [])] if isinstance(doc["models"]["body"], dict) else doc["models"]["body"]))
    for key in ("chat", "stream"):
        rec = doc[key]
        idn = rec["identity"]
        print("%-7s status=%-4s latency=%-6s leg=%-18s marks=%s" % (
            key, rec["status"], rec.get("latency_ms") or rec.get("total_ms"),
            idn["leg_by_signature"], ",".join(m for ms in idn["signature_matches"].values() for m in ms) or "-"))
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
