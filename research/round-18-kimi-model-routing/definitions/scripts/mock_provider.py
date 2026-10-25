#!/usr/bin/env python3
"""A local stand-in provider that records what the real client transmits.

Started by scripts/probe_client_semantics.py on a loopback port; answers the
three protocol shapes the client may speak and writes every request body it
receives into --cap, with credential headers replaced by a length marker.

    python3 scripts/mock_provider.py --port 8899 --cap /tmp/cap

Never prints or stores a credential value: the client's own key for this
provider is the literal "mock-local".
"""
import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SECRET_HEADERS = ("authorization", "x-api-key", "cookie", "set-cookie")


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    cap = "/tmp/r18-defs-cap"
    counter = [0]

    def log_message(self, *args):
        pass

    def _record(self, body):
        os.makedirs(self.cap, exist_ok=True)
        Handler.counter[0] += 1
        rec = {
            "path": self.path,
            "headers": {k: ("<redacted:len=%d>" % len(v) if k.lower() in SECRET_HEADERS else v)
                        for k, v in self.headers.items()},
            "body": body,
        }
        path = os.path.join(self.cap, "%03d.json" % Handler.counter[0])
        with open(path, "w") as fh:
            json.dump(rec, fh, indent=2, sort_keys=True)

    def do_POST(self):
        length = int(self.headers.get("content-length") or 0)
        raw = self.rfile.read(length)
        try:
            body = json.loads(raw or b"{}")
        except Exception:
            body = {"_unparsed": raw.decode("utf-8", "replace")[:2000]}
        self._record(body)
        stream = bool(body.get("stream"))
        if "/messages" in self.path:
            payload = {"id": "msg_1", "type": "message", "role": "assistant", "model": "mock",
                       "content": [{"type": "text", "text": "pong"}], "stop_reason": "end_turn",
                       "usage": {"input_tokens": 1, "output_tokens": 1}}
        elif "/responses" in self.path:
            payload = {"id": "resp_1", "object": "response", "created_at": 0, "model": "mock",
                       "status": "completed",
                       "output": [{"type": "message", "id": "m1", "role": "assistant",
                                   "status": "completed",
                                   "content": [{"type": "output_text", "text": "pong",
                                                "annotations": []}]}],
                       "usage": {"input_tokens": 1, "output_tokens": 1, "total_tokens": 2}}
        else:
            payload = {"id": "c1", "object": "chat.completion", "created": 0, "model": "mock",
                       "choices": [{"index": 0, "message": {"role": "assistant", "content": "pong"},
                                    "finish_reason": "stop"}],
                       "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        if stream:
            self.send_response(200)
            self.send_header("content-type", "text/event-stream")
            self.send_header("connection", "close")
            self.end_headers()
            if "/responses" in self.path:
                events = [
                    ("response.created", {"type": "response.created",
                                          "response": dict(payload, status="in_progress")}),
                    ("response.output_text.delta", {"type": "response.output_text.delta",
                                                    "delta": "pong"}),
                    ("response.completed", {"type": "response.completed", "response": payload}),
                ]
            elif "/messages" in self.path:
                events = [
                    ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                             "delta": {"type": "text_delta", "text": "pong"}}),
                    ("message_stop", {"type": "message_stop"}),
                ]
            else:
                events = [
                    ("chat.completion.chunk", {"id": "c1", "object": "chat.completion.chunk",
                                               "created": 0, "model": "mock",
                                               "choices": [{"index": 0,
                                                            "delta": {"role": "assistant",
                                                                      "content": "pong"},
                                                            "finish_reason": "stop"}]}),
                ]
            for name, data in events:
                self.wfile.write(("event: %s\ndata: %s\n\n" % (name, json.dumps(data))).encode())
                self.wfile.flush()
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        else:
            out = json.dumps(payload).encode()
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(out)))
            self.end_headers()
            self.wfile.write(out)

    def do_GET(self):
        self._record({"GET": self.path})
        out = json.dumps({"object": "list",
                          "data": [{"id": "mock-model", "object": "model"}]}).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8899)
    ap.add_argument("--cap", default="/tmp/r18-defs-cap")
    args = ap.parse_args()
    Handler.cap = args.cap
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
