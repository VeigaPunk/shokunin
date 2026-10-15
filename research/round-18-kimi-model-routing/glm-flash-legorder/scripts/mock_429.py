#!/usr/bin/env python3
"""Tiny OpenAI-shaped mock that always answers with a rate-limit error.

Used by scratch_failover_test.sh to exercise the shim's 429 -> next-leg path
without touching the operator's live zai quota.
Usage: mock_429.py <port>
"""
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class H(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass

    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(n)
        body = json.dumps({"error": {"code": "1305",
                                     "message": "rate limit reached (mock)"}}
                          ).encode()
        self.send_response_only(429)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), H).serve_forever()