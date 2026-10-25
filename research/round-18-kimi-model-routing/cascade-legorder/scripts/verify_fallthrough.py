#!/usr/bin/env python3
"""Prove the cascade's fallthrough behaviour against the LIVE shim code.

    python3 verify_fallthrough.py --out raw/fallthrough-verification.json

Spawns throwaway `shim.py` instances on scratch ports, each with leg URLs
overridden to local stubs (or to a dead port) and, where a scenario needs it, a
single real upstream in the final position. Every scenario is then driven with
one tiny chat request and judged on three signals: the caller-visible response,
the instance's own leg log (`leg=N/<name> FAIL reason=...`), and the stub's
request log (which legs were actually contacted, in order).

Real upstream traffic is exactly one 8-token request in the scenarios marked
"real" (hyper once, opencode-go once); the other scenarios are fully local.

No credential material is printed or written: stub legs are configured with
placeholder keys, and captures keep the shim's own log lines only.
"""

from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SHIM = os.path.expanduser("~/.local/share/ds-flash-shim/shim.py")
DEAD = "http://127.0.0.1:9/v1/chat/completions"  # discard port: instant connection refused

STUBS = {
    "429": (429, b'{"error":{"message":"rate limit exceeded"}}'),
    "500": (500, b'{"error":{"message":"internal error"}}'),
    "quota200": (200, b'{"error":{"message":"Your token-plan 1-month quota has been exhausted."}}'),
    "400": (400, b'{"error":{"message":"bad request: unsupported parameter"}}'),
}


class Stub:
    """A one-route upstream that answers a fixed status/body and logs each call."""

    def __init__(self, mode: str):
        self.mode = mode
        self.status, self.body = STUBS[mode]
        self.calls: list[dict] = []
        calls = self.calls
        mode_status, mode_body = self.status, self.body

        class H(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):  # silence
                pass

            def do_POST(self):
                length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(length) if length else b""
                try:
                    body = json.loads(raw or b"{}")
                except Exception:
                    body = {}
                calls.append({"path": self.path, "model": body.get("model"),
                              "authorization_present": "Authorization" in self.headers})
                self.send_response_only(mode_status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(mode_body)))
                self.end_headers()
                self.wfile.write(mode_body)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.port = self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    @property
    def url(self) -> str:
        return "http://127.0.0.1:%d/v1/chat/completions" % self.port

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class Shim:
    """A throwaway shim.py instance with per-leg env overrides."""

    def __init__(self, port: int, legs: dict):
        env = dict(os.environ)
        env["DS_SHIM_PORT"] = str(port)
        for idx, spec in legs.items():
            env["DS_LEG%d_NAME" % idx] = spec["name"]
            # Only stub legs get a URL override; a leg named for a real provider
            # keeps the endpoint the rewritten shim.py already carries.
            if "url" in spec:
                env["DS_LEG%d_URL" % idx] = spec["url"]
            # Only stub legs get placeholder credentials; a leg named for a real
            # provider keeps the credential the rewritten shim.py already carries.
            if spec.get("key"):
                env["DS_LEG%d_KEY" % idx] = spec["key"]
            if spec.get("session"):
                env["DS_LEG%d_SESSION" % idx] = spec["session"]
            env["DS_LEG%d_MODEL" % idx] = spec.get("model", "")
        self.port = port
        self.proc = subprocess.Popen([sys.executable, SHIM], env=env,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        deadline = time.time() + 10
        while time.time() < deadline:
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.3):
                    return
            except OSError:
                time.sleep(0.05)
        raise SystemExit("scratch shim on %d did not come up" % port)

    def stop(self) -> str:
        self.proc.terminate()
        try:
            out, _ = self.proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            self.proc.kill()
            out, _ = self.proc.communicate()
        return out or ""


def chat(port: int, model: str = "deepseek-v4.1-flash", stream: bool = False) -> dict:
    body = {"model": model, "max_tokens": 8, "temperature": 0,
            "messages": [{"role": "user", "content": "ping"}]}
    if stream:
        body["stream"] = True
    headers = {"Content-Type": "application/json"}
    if stream:
        headers["Accept"] = "text/event-stream"
    req = urllib.request.Request("http://127.0.0.1:%d/v1/chat/completions" % port,
                                 data=json.dumps(body).encode(), method="POST",
                                 headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw = resp.read()
            return {"status": resp.status, "headers": dict(resp.headers),
                    "body": raw.decode("utf-8", "replace")[:600]}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "headers": dict(exc.headers),
                "body": exc.read().decode("utf-8", "replace")[:600]}
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "error": "%s: %s" % (type(exc).__name__, exc)}


def leg_lines(log: str) -> list[str]:
    return [l.split(None, 2)[-1] for l in log.splitlines() if " leg=" in l]


def signature(headers: dict) -> str:
    low = {k.lower() for k in headers}
    if "x-envoy-upstream-service-time" in low or "req-arrive-time" in low:
        return "alibaba-token-plan"
    if "x-ratelimit-limit-hour" in low:
        return "hyper"
    if "x-opencode-endpoint-id" in low:
        return "opencode-go"
    return "unidentified"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    stubs = {mode: Stub(mode) for mode in STUBS}
    doc = {"shim": SHIM, "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "stub_ports": {m: s.port for m, s in stubs.items()},
           "dead_url": DEAD, "scenarios": []}

    scenarios = [
        ("connection refused on legs 1-2 -> leg 3 (real opencode-go) serves",
         {1: {"name": "dead-leg1", "url": DEAD}, 2: {"name": "dead-leg2", "url": DEAD},
          3: {"name": "opencode-go"}}, "real", False,
         "dead legs produce connection errors; the chain advances to the real third leg"),
        ("stub legs 429 -> 500 -> 200-with-quota-marker: all fail, caller receives the LAST leg's response",
         {1: {"name": "stub-429", "url": stubs["429"].url},
          2: {"name": "stub-500", "url": stubs["500"].url},
          3: {"name": "stub-quota200", "url": stubs["quota200"].url}}, "local", False,
         "both documented failure classes fire and the exhausted chain hands back the last leg verbatim"),
        ("stub leg 1 200-with-quota-marker -> leg 2 (real hyper) serves",
         {1: {"name": "stub-quota200", "url": stubs["quota200"].url},
          2: {"name": "hyper"}, 3: {"name": "dead-leg3", "url": DEAD}}, "real", False,
         "a 200 whose body carries a quota marker is treated as a failure and the next leg answers"),
        ("stub leg 1 answers 400 (terminal) -> chain does NOT advance",
         {1: {"name": "stub-400", "url": stubs["400"].url}, 2: {"name": "stub-429", "url": stubs["429"].url},
          3: {"name": "stub-500", "url": stubs["500"].url}}, "local", False,
         "non-200 outside the failure set is handed straight to the caller; legs 2-3 stay untouched"),
        ("[stream] stub leg 1 200-with-quota-marker -> leg 1 is ACCEPTED, no advance",
         {1: {"name": "stub-quota200", "url": stubs["quota200"].url},
          2: {"name": "stub-429", "url": stubs["429"].url},
          3: {"name": "stub-500", "url": stubs["500"].url}}, "local", True,
         "on stream=true the leg is chosen from headers only, so a 200 body marker is invisible: "
         "the caller receives that body as the stream (documented consequence, no failover)"),
        ("[stream] stub leg 1 429 -> leg 2 (real hyper) serves",
         {1: {"name": "stub-429", "url": stubs["429"].url},
          2: {"name": "hyper"}, 3: {"name": "dead-leg3", "url": DEAD}}, "real", True,
         "status-based failures do fail over on the streaming path"),
    ]

    try:
        for title, legs, kind, stream, why in scenarios:
            port = free_port()
            calls_before = {m: len(s.calls) for m, s in stubs.items()}
            shim = Shim(port, legs)
            try:
                resp = chat(port, stream=stream)
            finally:
                log = shim.stop()
            stub_hits = {m: [c for c in stubs[m].calls[calls_before[m]:]] for m in stubs}
            stubs_contacted = [m for m, hits in stub_hits.items() if hits]
            rec = {
                "title": title, "kind": kind, "stream": stream, "why": why, "port": port,
                "response": {"status": resp.get("status"), "signature": signature(resp.get("headers", {})),
                             "body": resp.get("body")},
                "shim_leg_log": leg_lines(log),
                "stubs_contacted": stubs_contacted,
                "stub_call_counts": {m: len(h) for m, h in stub_hits.items() if h},
            }
            doc["scenarios"].append(rec)
            print("== %s" % title)
            print("   response status=%s signature=%s" % (rec["response"]["status"], rec["response"]["signature"]))
            for line in rec["shim_leg_log"]:
                print("   shim: %s" % line)
            print("   stub legs contacted: %s" % (stubs_contacted or "none"))
    finally:
        for s in stubs.values():
            s.stop()

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())