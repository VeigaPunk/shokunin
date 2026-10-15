#!/usr/bin/env python3
"""Request shaping and SSE parsing for the three protocols the pool uses.

Parsing returns timings as well as text: the battery's headline numbers are
derived here so that the runner stays a thin loop over models and probes.
"""
import json

MIN_DECODE_SPAN_MS = 50
REASONING_TEXT_LIMIT = 4000


def build_body(probe_id, prompt, model_id, protocol, stream,
               max_tokens, tools=None, tool_choice=None, codex=False):
    body = {"model": model_id, "stream": stream}
    if protocol == "anthropic":
        body.update({"max_tokens": max_tokens,
                     "messages": [{"role": "user", "content": prompt}]})
        if tools:
            body["tools"] = [{"name": t["function"]["name"],
                              "description": t["function"]["description"],
                              "input_schema": t["function"]["parameters"]}
                             for t in tools]
        return body

    if protocol == "openai_responses":
        body.update({
            "max_output_tokens": max_tokens,
            "input": [{"type": "message", "role": "user",
                       "content": [{"type": "input_text", "text": prompt}]}],
        })
        if tools:
            body["tools"] = [{"type": "function", "name": t["function"]["name"],
                              "description": t["function"]["description"],
                              "parameters": t["function"]["parameters"]}
                             for t in tools]
            if tool_choice:
                body["tool_choice"] = tool_choice
        if codex:
            # M1 D6: the codex lane rejects store=true, refuses a non-streaming
            # request, and rejects any `temperature` field outright.
            body["store"] = False
        return body

    body.update({"max_tokens": max_tokens, "temperature": 0,
                 "messages": [{"role": "user", "content": prompt}]})
    if protocol == "openai":
        body["stream_options"] = {"include_usage": True}
    if tools:
        body["tools"] = tools
        if tool_choice:
            body["tool_choice"] = tool_choice
    return body


def _usage_tokens(usage, key_a, key_b):
    if not isinstance(usage, dict):
        return None
    for key in (key_a, key_b):
        if isinstance(usage.get(key), int):
            return usage[key]
    return None


def completion_tokens(usage):
    return _usage_tokens(usage, "completion_tokens", "output_tokens")


def prompt_tokens(usage):
    return _usage_tokens(usage, "prompt_tokens", "input_tokens")


def reasoning_tokens(usage):
    if not isinstance(usage, dict):
        return None
    details = usage.get("completion_tokens_details") or usage.get("output_tokens_details")
    if isinstance(details, dict) and isinstance(details.get("reasoning_tokens"), int):
        return details["reasoning_tokens"]
    return None


class Stream:
    """Accumulates a response stream: text, tool calls, usage and timings."""

    def __init__(self, t0, protocol):
        self.t0 = t0
        self.protocol = protocol
        self.content = []
        self.reasoning = []
        self.refusal = []
        self.tool_calls = []
        self.usage = None
        self.finish_reason = None
        self.status_field = None
        self.incomplete_reason = None
        self.t_first_content = None
        self.t_first_reasoning = None
        self.t_first_tool = None
        self.t_last_delta = None
        self.content_deltas = 0
        self.reasoning_deltas = 0
        self.events = 0
        self.parse_errors = 0
        self.json_body = None

    def _touch(self, when):
        self.t_last_delta = when

    def _tool(self, index):
        while len(self.tool_calls) <= index:
            self.tool_calls.append({"id": None, "name": None, "arguments": ""})
        return self.tool_calls[index]

    def feed(self, text, when):
        if not text or not text.startswith("data:"):
            return
        payload = text[5:].strip()
        if not payload or payload == "[DONE]":
            return
        try:
            obj = json.loads(payload)
        except Exception:  # noqa: BLE001
            self.parse_errors += 1
            return
        if not isinstance(obj, dict):
            return
        self.events += 1
        usage = obj.get("usage") if isinstance(obj.get("usage"), dict) else None
        nested = obj.get("message") or obj.get("response")
        if usage is None and isinstance(nested, dict) and isinstance(nested.get("usage"), dict):
            usage = nested["usage"]
        if usage:
            self.usage = usage
        self._feed_protocol(obj, when)

    def _feed_protocol(self, obj, when):
        if self.protocol == "anthropic":
            kind = obj.get("type")
            if kind == "content_block_delta":
                delta = obj.get("delta") or {}
                if delta.get("text"):
                    self._content(delta["text"], when)
                elif delta.get("thinking"):
                    self._reasoning(delta["thinking"], when)
                elif delta.get("partial_json"):
                    tool = self._tool(0)
                    tool["arguments"] += delta["partial_json"]
                    self._touch(when)
            elif kind == "content_block_start":
                block = obj.get("content_block") or {}
                if block.get("type") == "tool_use":
                    tool = self._tool(0)
                    tool["name"] = block.get("name")
                    tool["id"] = block.get("id")
                    if self.t_first_tool is None:
                        self.t_first_tool = when
                    self._touch(when)
            elif kind == "message_delta":
                delta = obj.get("delta") or {}
                if delta.get("stop_reason"):
                    self.finish_reason = delta["stop_reason"]
            return

        if self.protocol == "openai_responses":
            kind = obj.get("type")
            if kind == "response.output_text.delta" and obj.get("delta"):
                self._content(obj["delta"], when)
            elif kind in ("response.reasoning_summary_text.delta",
                          "response.reasoning_text.delta") and obj.get("delta"):
                self._reasoning(obj["delta"], when)
            elif kind == "response.refusal.delta" and obj.get("delta"):
                self.refusal.append(obj["delta"])
                self._touch(when)
            elif kind == "response.function_call_arguments.delta":
                tool = self._tool(0)
                tool["arguments"] += obj.get("delta") or ""
                self._touch(when)
            elif kind == "response.output_item.added" or kind == "response.output_item.done":
                item = obj.get("item") or {}
                if item.get("type") == "function_call":
                    tool = self._tool(0)
                    tool["name"] = item.get("name") or tool["name"]
                    tool["id"] = item.get("call_id") or tool["id"]
                    if item.get("arguments"):
                        tool["arguments"] = item["arguments"]
                    if self.t_first_tool is None:
                        self.t_first_tool = when
                    self._touch(when)
            elif kind == "response.completed":
                response = obj.get("response") or {}
                for item in response.get("output") or []:
                    if isinstance(item, dict) and item.get("type") == "function_call":
                        tool = self._tool(0)
                        tool["name"] = item.get("name") or tool["name"]
                        tool["id"] = item.get("call_id") or tool["id"]
                        if item.get("arguments"):
                            tool["arguments"] = item["arguments"]
                        if self.t_first_tool is None:
                            self.t_first_tool = when
                if response.get("status"):
                    self.status_field = response["status"]
                if isinstance(response.get("usage"), dict):
                    self.usage = response["usage"]
            elif kind == "response.incomplete":
                response = obj.get("response") or {}
                self.incomplete_reason = (response.get("incomplete_details") or {}).get("reason")
            return

        choices = obj.get("choices")
        if not isinstance(choices, list) or not choices:
            return
        choice = choices[0] or {}
        if choice.get("finish_reason"):
            self.finish_reason = choice["finish_reason"]
        delta = choice.get("delta")
        if not isinstance(delta, dict):
            delta = choice.get("message") if isinstance(choice.get("message"), dict) else {}
        if delta.get("content"):
            self._content(delta["content"], when)
        elif delta.get("reasoning_content"):
            self._reasoning(delta["reasoning_content"], when)
        elif delta.get("reasoning"):
            self._reasoning(delta["reasoning"], when)
        if delta.get("refusal"):
            self.refusal.append(delta["refusal"])
        for call in delta.get("tool_calls") or []:
            if not isinstance(call, dict):
                continue
            tool = self._tool(call.get("index") or 0)
            if call.get("id"):
                tool["id"] = call["id"]
            function = call.get("function") or {}
            if function.get("name"):
                tool["name"] = function["name"]
            if function.get("arguments"):
                tool["arguments"] += function["arguments"]
            if self.t_first_tool is None:
                self.t_first_tool = when
            self._touch(when)

    def _content(self, text, when):
        if not self.content:
            self.t_first_content = when
        self.content.append(text)
        self.content_deltas += 1
        self._touch(when)

    def _reasoning(self, text, when):
        if not self.reasoning:
            self.t_first_reasoning = when
        self.reasoning.append(text)
        self.reasoning_deltas += 1
        self._touch(when)

    def adopt_json_body(self, text):
        """A lane that answers with one complete JSON document instead of SSE."""
        try:
            obj = json.loads(text)
        except Exception:  # noqa: BLE001
            return False
        if not isinstance(obj, dict):
            return False
        if isinstance(obj.get("usage"), dict):
            self.usage = obj["usage"]
        if isinstance(obj.get("output"), list):
            for item in obj["output"]:
                if isinstance(item, dict) and item.get("type") == "message":
                    for part in item.get("content") or []:
                        if isinstance(part, dict) and part.get("type") == "output_text":
                            self.content.append(part.get("text") or "")
                if isinstance(item, dict) and item.get("type") == "function_call":
                    tool = self._tool(0)
                    tool["name"] = item.get("name")
                    tool["id"] = item.get("call_id")
                    tool["arguments"] = item.get("arguments") or ""
        choices = obj.get("choices")
        if isinstance(choices, list) and choices:
            choice = choices[0] or {}
            message = choice.get("message") or {}
            if message.get("content"):
                self.content.append(message["content"] if isinstance(message["content"], str)
                                     else json.dumps(message["content"]))
            if message.get("reasoning_content"):
                self.reasoning.append(message["reasoning_content"])
            for call in message.get("tool_calls") or []:
                tool = self._tool(call.get("index") or 0)
                tool["id"] = call.get("id")
                tool["name"] = (call.get("function") or {}).get("name")
                tool["arguments"] = (call.get("function") or {}).get("arguments") or ""
            if choice.get("finish_reason"):
                self.finish_reason = choice["finish_reason"]
        self.json_body = True
        return bool(self.content or self.tool_calls)

    def finish(self):
        content = "".join(self.content)
        reasoning = "".join(self.reasoning)
        tools = []
        for tool in self.tool_calls:
            tools.append({"id": tool["id"], "name": tool["name"],
                          "arguments": tool["arguments"]})
        first_decoded = self.t_first_content or self.t_first_reasoning or self.t_first_tool
        span = None
        if first_decoded and self.t_last_delta and self.t_last_delta > first_decoded:
            span = (self.t_last_delta - first_decoded) * 1000.0
        tokens = completion_tokens(self.usage)
        tps = None
        basis = None
        if tokens is not None:
            basis = "server_usage_completion_tokens"
        elif self.content_deltas > 1:
            tokens = self.content_deltas
            basis = "observed_content_deltas"
        note = None
        if tokens and tokens > 1 and span and span >= MIN_DECODE_SPAN_MS:
            tps = round((tokens - 1) / (span / 1000.0), 2)
        elif span is not None and span < MIN_DECODE_SPAN_MS:
            note = ("not derivable: stream was not incrementally flushed "
                    "(decode span %d ms < %d ms)" % (round(span), MIN_DECODE_SPAN_MS))
        else:
            note = "not derivable: no incremental deltas or fewer than 2 tokens"
        return {
            "content": content,
            "reasoning_text": reasoning[:REASONING_TEXT_LIMIT],
            "reasoning_chars": len(reasoning),
            "refusal_text": "".join(self.refusal),
            "tool_calls": tools,
            "usage": self.usage,
            "completion_tokens": completion_tokens(self.usage),
            "prompt_tokens": prompt_tokens(self.usage),
            "reasoning_tokens": reasoning_tokens(self.usage),
            "finish_reason": self.finish_reason,
            "response_status": self.status_field,
            "incomplete_reason": self.incomplete_reason,
            "ttft_content_ms": (round((self.t_first_content - self.t0) * 1000)
                                if self.t_first_content else None),
            "ttft_reasoning_ms": (round((self.t_first_reasoning - self.t0) * 1000)
                                  if self.t_first_reasoning else None),
            "ttft_tool_ms": (round((self.t_first_tool - self.t0) * 1000)
                             if self.t_first_tool else None),
            "first_decoded_ms": (round((first_decoded - self.t0) * 1000)
                                 if first_decoded else None),
            "decode_span_ms": round(span) if span is not None else None,
            "content_delta_count": self.content_deltas,
            "reasoning_delta_count": self.reasoning_deltas,
            "sse_event_count": self.events,
            "sse_parse_errors": self.parse_errors,
            "content_chars": len(content),
            "tps": tps,
            "tps_basis": basis,
            "tps_note": note,
        }


def parse_capture(capture, protocol):
    """Turn a common.post_streaming() result into a Stream summary."""
    stream = Stream(capture["t0"], protocol)
    for text, when in capture["lines"]:
        stream.feed(text, when)
    if stream.events == 0 or (not stream.content and not stream.tool_calls):
        body = "".join(line for line, _ in capture["lines"]).strip()
        if body:
            stream.adopt_json_body(body)
    summary = stream.finish()
    summary["streaming_supported"] = bool(
        stream.content_deltas or stream.reasoning_deltas or stream.tool_calls)
    return summary
