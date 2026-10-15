#!/usr/bin/env python3
"""Timestamped SSE read trace -- proves a streaming probe streams.

M9 (round 18). The shim relays the serving leg's bytes as-is and flushes every
read, so "did the client see separate arrivals over time" is a transport fact
about the SERVING LEG, not about the shim. M3 recorded the cascade lane as
burst-flushed when the devin leg answered; this script is how the zai-leg
re-measure was taken.

Usage: probe_stream_trace.py <url> [model] [max_tokens]
Prints one line per read: elapsed_ms  bytes  cumulative.
"""
import json
import sys
import time
import urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else \
    "http://127.0.0.1:8793/v1/chat/completions"
model = sys.argv[2] if len(sys.argv) > 2 else "glm-5.3-flash"
max_tokens = int(sys.argv[3]) if len(sys.argv) > 3 else 96

payload = {
    "model": model,
    "messages": [{"role": "user", "content": "Reply with exactly one word: pong"}],
    "max_tokens": max_tokens,
    "stream": True,
}
req = urllib.request.Request(
    url, data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"})

t0 = time.time()
reads = []
with urllib.request.urlopen(req, timeout=120) as resp:
    print("status=%d content-type=%s" % (resp.status,
                                         resp.headers.get("Content-Type")))
    total = 0
    while True:
        chunk = resp.read(256)
        if not chunk:
            break
        total += len(chunk)
        reads.append((time.time() - t0, len(chunk), total))
        if len(reads) <= 5 or len(reads) % 10 == 0:
            print("read %4d  t=%.3fs  +%4dB  cum=%dB"
                  % (len(reads), reads[-1][0], len(chunk), total))

if len(reads) >= 2:
    span_ms = (reads[-1][0] - reads[0][0]) * 1000
    print("reads=%d  decode_span_ms=%.1f  total_bytes=%d  wall=%.3fs"
          % (len(reads), span_ms, total, reads[-1][0]))
    print("transport=%s" % ("incremental" if span_ms >= 50 else "burst"))