#!/usr/bin/env python3
"""Stdlib mock endpoint for the R18 battery smoke test.

Serves the openai, openai_responses and anthropic shapes the runner uses, and
streams SSE the way the real lanes do. Behaviour is selected by the model id in
the request, so one mock exercises every path the runner must handle:

    *-good      incremental stream, correct answers, usage block
    *-burst     correct answers, all deltas flushed in a single burst
    *-dead      429 with a quota body
    *-noauth    401
    *-silent    200 but no content deltas at all (empty stream)
    *-timeout   accepts the request and never answers
    *-fences    correct answers wrapped in markdown fences (format break)
    *-wrong     well-formed but wrong answers
    *-notools   answers the tool probe in prose instead of a tool call

    python3 scripts/mock_server.py [port]
"""
import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import probes  # noqa: E402

CHUNK_CHARS = 24
CHUNK_DELAY_S = 0.006


def behaviour(model):
    for suffix in ("good", "burst", "dead", "noauth", "silent", "timeout",
                   "fences", "wrong", "notools"):
        if model.endswith("-" + suffix) or model.endswith("/" + suffix):
            return suffix
    return "good"


def answer_for(probe_id, behaviour_name):
    if probe_id == "warmup":
        return "READY"
    if probe_id == "perf":
        text = probes.MOCK_PERF_ANSWER
    else:
        probe = probes.by_id(probe_id)
        text = probe["mock_answer"] if probe else "ok"
    if text is None:
        text = "The weather tool would be used here."
    if behaviour_name == "wrong":
        text = "WRONG"
    elif behaviour_name == "fences":
        text = "```\n%s\n```" % text
    return text


def tool_arguments(probe):
    return json.dumps({"city": "Paris"})


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):  # keep the smoke log clean
        pass

    def _read_body(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:  # noqa: BLE001
            return {}

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_sse_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()

    def _write_chunk(self, text):
        data = text.encode()
        self.wfile.write(("%x\r\n" % len(data)).encode() + data + b"\r\n")
        self.wfile.flush()

    def _end_chunks(self):
        self.wfile.write(b"0\r\n\r\n")
        self.wfile.flush()

    def _emit(self, text):
        self._write_chunk(text)

    def do_GET(self):
        self._send_json(200, {"data": [{"id": "mock"}], "object": "list"})

    def do_POST(self):
        body = self._read_body()
        model = str(body.get("model") or "mock-good")
        mode = behaviour(model)
        path = self.path

        if mode == "noauth":
            self._send_json(401, {"error": {"message": "Invalid Authentication",
                                            "type": "invalid_authentication_error"}})
            return
        if mode == "dead":
            self._send_json(429, {"error": {
                "message": "Your token-plan 1-month quota has been exhausted.",
                "type": "insufficient_quota"}})
            return
        if mode == "timeout":
            time.sleep(120)
            return

        text = self._prompt_text(body, path)
        probe_id = probes.detect_probe(text)
        answer = answer_for(probe_id, mode)
        wants_tool = probe_id == "t1"

        if path.endswith("/responses"):
            problem = self._codex_shape_problem(body)
            if problem:
                self._send_json(400, {"error": {"message": problem}})
                return
            self._respond_responses(model, answer, probe_id, wants_tool, mode)
        elif path.endswith("/messages"):
            self._respond_anthropic(model, answer, wants_tool, mode)
        else:
            self._respond_openai(model, answer, wants_tool, mode, body)

    def _codex_shape_problem(self, body):
        """Mirror the codex lane's shape rules (M1 defect D6)."""
        if not isinstance(body.get("input"), list):
            return "Input must be a list"
        if body.get("store") is not False:
            return "Store must be set to false"
        if body.get("stream") is not True:
            return "Stream must be set to true"
        if "temperature" in body:
            return "Unsupported parameter: temperature"
        if int(body.get("max_output_tokens") or 0) < 16:
            return ("Invalid 'max_output_tokens': integer below minimum value. "
                    "Expected a value >= 16")
        return None

    def _prompt_text(self, body, path):
        if path.endswith("/messages") or path.endswith("/chat/completions"):
            for message in reversed(body.get("messages") or []):
                if message.get("role") == "user":
                    content = message.get("content")
                    return content if isinstance(content, str) else json.dumps(content)
            return ""
        for item in body.get("input") or []:
            if isinstance(item, dict):
                for part in item.get("content") or []:
                    if isinstance(part, dict) and part.get("type") == "input_text":
                        return part.get("text") or ""
        return ""

    def _chunks(self, text):
        return [text[i:i + CHUNK_CHARS] for i in range(0, len(text), CHUNK_CHARS)] or [""]

    def _respond_openai(self, model, answer, wants_tool, mode, body):
        self._send_sse_headers()
        chunks = self._chunks(answer)
        if mode == "burst":
            time.sleep(0.05)
            for chunk in chunks:
                self._emit("data: " + json.dumps(
                    {"choices": [{"delta": {"content": chunk}, "index": 0}]}) + "\n\n")
        elif mode == "silent":
            pass
        else:
            for chunk in chunks:
                self._emit("data: " + json.dumps(
                    {"choices": [{"delta": {"content": chunk}, "index": 0}]}) + "\n\n")
                time.sleep(CHUNK_DELAY_S)
        tool_payload = None
        if wants_tool and mode != "notools":
            tool_payload = {"choices": [{"index": 0, "delta": {"tool_calls": [
                {"index": 0, "id": "call_mock_1",
                 "function": {"name": "get_weather",
                              "arguments": json.dumps({"city": "Paris"})}}]}}]}
            self._emit("data: " + json.dumps(tool_payload) + "\n\n")
        finish = "tool_calls" if wants_tool and mode != "notools" else "length" \
            if body.get("max_tokens") == 1 else "stop"
        self._emit("data: " + json.dumps(
            {"choices": [{"index": 0, "delta": {}, "finish_reason": finish}]}) + "\n\n")
        usage = {"prompt_tokens": 48, "completion_tokens": max(1, len(answer) // 4),
                 "total_tokens": 48 + max(1, len(answer) // 4)}
        self._emit("data: " + json.dumps({"choices": [], "usage": usage}) + "\n\n")
        self._emit("data: [DONE]\n\n")
        self._end_chunks()

    def _respond_responses(self, model, answer, probe_id, wants_tool, mode):
        self._send_sse_headers()
        self._emit("data: " + json.dumps(
            {"type": "response.created", "response": {"id": "resp_mock"}}) + "\n\n")
        for chunk in self._chunks(answer):
            self._emit("data: " + json.dumps(
                {"type": "response.output_text.delta", "delta": chunk}) + "\n\n")
            if mode != "burst":
                time.sleep(CHUNK_DELAY_S)
        output = [{"type": "message", "role": "assistant", "content": [
            {"type": "output_text", "text": answer}]}]
        if wants_tool and mode != "notools":
            item = {"type": "function_call", "name": "get_weather",
                    "call_id": "call_mock_1", "arguments": json.dumps({"city": "Paris"})}
            output.append(item)
            self._emit("data: " + json.dumps(
                {"type": "response.output_item.done", "item": item}) + "\n\n")
        self._emit("data: " + json.dumps({
            "type": "response.completed",
            "response": {"id": "resp_mock", "status": "completed",
                         "output": output,
                         "usage": {"input_tokens": 24, "output_tokens":
                                   max(1, len(answer) // 4), "total_tokens": 24 + len(answer) // 4}},
        }) + "\n\n")
        self._end_chunks()

    def _respond_anthropic(self, model, answer, wants_tool, mode):
        self._send_sse_headers()
        self._emit("data: " + json.dumps(
            {"type": "message_start", "message": {"usage": {"input_tokens": 30}}}) + "\n\n")
        if wants_tool and mode != "notools":
            self._emit("data: " + json.dumps({"type": "content_block_start",
                                              "content_block": {"type": "tool_use",
                                                                "name": "get_weather",
                                                                "id": "toolu_mock"}}) + "\n\n")
            self._emit("data: " + json.dumps({"type": "content_block_delta", "delta": {
                "type": "input_json_delta",
                "partial_json": json.dumps({"city": "Paris"})}}) + "\n\n")
        else:
            for chunk in self._chunks(answer):
                self._emit("data: " + json.dumps({"type": "content_block_delta",
                                                  "delta": {"type": "text_delta",
                                                            "text": chunk}}) + "\n\n")
                if mode != "burst":
                    time.sleep(CHUNK_DELAY_S)
        self._emit("data: " + json.dumps({"type": "message_delta", "delta": {
            "stop_reason": "end_turn"}, "usage": {"output_tokens":
                                                  max(1, len(answer) // 4)}}) + "\n\n")
        self._end_chunks()


def serve(port):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


if __name__ == "__main__":
    listen = int(sys.argv[1]) if len(sys.argv) > 1 else 8799
    srv = serve(listen)
    print("mock server on 127.0.0.1:%d" % listen, flush=True)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        srv.shutdown()
