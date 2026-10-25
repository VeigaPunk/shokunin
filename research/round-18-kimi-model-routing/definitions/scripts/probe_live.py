#!/usr/bin/env python3
"""Live probes for the R18 definitions audit (M2).

Three suites, each bounded and one-request-per-cell:

  effort <value>  minimal completion carrying the effort value the *client*
                  would send for that protocol (verified against the client's
                  own wire shape, see ANALYSIS.md section 3):
                    openai            -> {"reasoning_effort": value}
                    anthropic         -> {"output_config": {"effort": value}}
                    openai_responses  -> {"reasoning": {"effort": value}}
                    kimi              -> {"thinking": {"effort": value}}
                  An `invalid-control` token probes each lane once with a value
                  that is in no model's support_efforts, separating "this lane
                  validates the value" from "this lane ignores the field".

  tool <lane>     completion with exactly one tool schema and tool_choice set;
                  records whether a well-formed tool call comes back. Closes the
                  census's "tool calling untested" gap.

  image <lane>    a tiny PNG in the first user message of a minimal completion;
                  one negative control on a model that does NOT declare image_in.

Pass 1 ran with max_tokens=16 and a 1x1 PNG. Both floors turned out to be wrong
for the interesting lanes (thinking models spend the whole budget on reasoning
and emit no tool call; several lanes reject images under 8-11 px), so pass 2
re-runs the inconclusive cells with max_tokens=256 and a 32x32 PNG. Pass 1 is
kept in raw/ because the size-floor error messages are themselves evidence of
image processing (the lane inspects dimensions before refusing).

A browser User-Agent is sent: without one, opencode-go's WAF answers
"error code: 1010" to every request (evidence in ANALYSIS section 5).

Usage:  python3 scripts/probe_live.py [effort|tool|image|all|pass2]
"""
import base64
import json
import os
import ssl
import struct
import sys
import time
import urllib.error
import urllib.request
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

TIMEOUT = 90
DEAD_LANES = {"managed:kimi-code"}  # OAuth store empty -> 401 on every path (census D1)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/141.0.0.0 Safari/537.36")


def png(side):
    """A solid-colour PNG of side x side, built here so no binary is committed."""
    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))
    ihdr = struct.pack(">IIBBBBB", side, side, 8, 6, 0, 0, 0)
    raw = b"".join(b"\x00" + b"\x40\x80\xc0\xff" * side for _ in range(side))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def b64(side):
    return base64.b64encode(png(side)).decode()


TOOL_SCHEMA = [{
    "type": "function",
    "function": {
        "name": "r18_echo",
        "description": "Echo a string back.",
        "parameters": {
            "type": "object",
            "properties": {"text": {"type": "string", "description": "text to echo"}},
            "required": ["text"],
        },
    },
}]

TOOL_SCHEMA_ANTHROPIC = [{
    "name": "r18_echo",
    "description": "Echo a string back.",
    "input_schema": {
        "type": "object",
        "properties": {"text": {"type": "string", "description": "text to echo"}},
        "required": ["text"],
    },
}]

TOOL_SCHEMA_RESPONSES = [{
    "type": "function",
    "name": "r18_echo",
    "description": "Echo a string back.",
    "parameters": {
        "type": "object",
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
    },
}]

# lane, alias, effort value
EFFORT_PLAN = [
    ("hyper", "hyper/qwen3.7-max", "minimal"),
    ("hyper", "hyper/qwen3.7-max", "low"),
    ("hyper", "hyper/qwen3.7-max", "medium"),
    ("hyper", "hyper/qwen3.7-max", "high"),
    ("hyper", "hyper/glm-5.2", "xhigh"),
    ("hyper", "hyper/glm-5.3", "max"),
    ("hyper", "hyper/qwen3.7-max", "invalid-control"),
    ("alibaba-token-plan", "alibaba-token-plan/qwen3.8-max", "xhigh"),
    ("alibaba-token-plan", "alibaba-token-plan/deepseek-v4.1-flash", "max"),
    ("alibaba-token-plan", "alibaba-token-plan/qwen3.8-max", "invalid-control"),
    ("zai-coding-plan", "zai-coding-plan/glm-5.3-flash", "max"),
    ("zai-coding-plan", "zai-coding-plan/glm-5.3-flash", "invalid-control"),
    ("opencode-go", "opencode-go/claude-haiku-5-5", "max"),
    ("opencode-go", "opencode-go/qwen3.8-max", "xhigh"),
    ("opencode-go", "opencode-go/qwen3.8-max", "invalid-control"),
    ("opencode-go", "opencode-go/kimi-k3", "max"),
    ("opencode-go", "opencode-go/grok-4.7", "xhigh"),
    ("opencode-go", "opencode-go/gpt-6-luna", "invalid-control"),
    ("xai-oauth", "xai-oauth/grok-4.5", "xhigh"),
    ("xai-oauth", "xai-oauth/grok-4.5", "max"),
    ("xai-oauth", "xai-oauth/grok-4.5", "invalid-control"),
    ("openai-codex", "openai-codex/gpt-6.1-sol", "max"),
    ("openai-codex", "openai-codex/gpt-6.1-sol", "invalid-control"),
    ("devin", "devin/swe-2", "max"),
    ("cursor", "cursor/composer-2.5-fast", "max"),
]

# pass 2: opencode-go was WAF-blocked in pass 1; add the cursor control
EFFORT2_PLAN = [r for r in EFFORT_PLAN if r[0] == "opencode-go"] + [
    ("cursor", "cursor/composer-2.5-fast", "invalid-control"),
    ("devin", "devin/swe-2", "invalid-control"),
]

# pass 4: the off_effort value sent as a request value. The client never transmits
# it (it is not a field the client knows), so this asks the *lane* what it makes of
# the value the config claims -- once on a lane that validates values, once on a
# lane that ignores them.
EFFORT4_PLAN = [
    ("hyper", "hyper/qwen3.7-max", "none"),
    ("opencode-go", "opencode-go/hy3", "none"),
]

# lane, alias  (pass 1: max_tokens 16)
TOOL_PLAN = [
    ("alibaba-token-plan", "alibaba-token-plan/deepseek-v4.1-flash"),
    ("zai-coding-plan", "zai-coding-plan/glm-5.3-flash"),
    ("hyper", "hyper/qwen3.8-flash"),
    ("opencode-go", "opencode-go/glm-5.3-flash"),
    ("opencode-go", "opencode-go/qwen3.8-flash"),
    ("openai-codex", "openai-codex/gpt-6.1-sol"),
    ("xai-oauth", "xai-oauth/grok-4.5"),
    ("devin", "devin/swe-2"),
    ("cursor", "cursor/composer-2.5-fast"),
    ("ds-flash-cascade", "cascade/deepseek-v4.1-flash"),
    ("glm-flash-cascade", "cascade/glm-5.3-flash"),
]

# pass 3: the client never sends tool_choice at all (it sends `tools` and lets the
# model decide -- mock capture), so force-choice is not the client's shape. These
# rows re-probe, without it, the two cells pass 2 could not settle.
TOOL3_PLAN = [
    {"lane": "opencode-go", "alias": "opencode-go/qwen3.8-flash", "tool_choice": False,
     "tag": "client-shape"},
    {"lane": "opencode-go", "alias": "opencode-go/claude-haiku-5-5", "tool_choice": False,
     "tag": "client-shape"},
    {"lane": "hyper", "alias": "hyper/qwen3.8-flash", "tool_choice": False, "tag": "repeat"},
]

# pass 2: 256-token budget so reasoning cannot swallow the call; opencode-go un-blocked;
# two extra rows separate "schema rejected" from "tool_choice rejected" on hyper.
TOOL2_PLAN = [
    {"lane": "alibaba-token-plan", "alias": "alibaba-token-plan/deepseek-v4.1-flash"},
    {"lane": "zai-coding-plan", "alias": "zai-coding-plan/glm-5.3-flash"},
    {"lane": "hyper", "alias": "hyper/qwen3.8-flash"},
    {"lane": "hyper", "alias": "hyper/qwen3.8-flash", "tool_choice": False,
     "tag": "no-tool_choice"},
    {"lane": "hyper", "alias": "hyper/qwen3.8-max", "tool_choice": False, "tag": "no-tool_choice"},
    {"lane": "opencode-go", "alias": "opencode-go/glm-5.3-flash"},
    {"lane": "opencode-go", "alias": "opencode-go/qwen3.8-flash"},
    {"lane": "openai-codex", "alias": "openai-codex/gpt-6.1-sol"},
    {"lane": "ds-flash-cascade", "alias": "cascade/deepseek-v4.1-flash"},
    {"lane": "glm-flash-cascade", "alias": "cascade/glm-5.3-flash"},
]

# lane / alias / png side  (1x1 in pass 1; 4th row is the negative control)
IMAGE_PLAN = [
    ("hyper", "hyper/qwen3.8-27b", 1),
    ("zai-coding-plan", "zai-coding-plan/glm-5.3-flash", 1),
    ("alibaba-token-plan", "alibaba-token-plan/qwen3.8-flash", 1),
    ("opencode-go", "opencode-go/mimo-v2.5", 1),
    ("opencode-go", "opencode-go/deepseek-v4-flash-vision-exp", 1),
    ("xai-oauth", "xai-oauth/grok-4.5", 1),
    ("zai-coding-plan", "zai-coding-plan/glm-5-turbo", 1),
]

# pass 2: 32x32, because 1x1 is below several lanes' minimum image size
IMAGE2_PLAN = [
    ("hyper", "hyper/qwen3.8-27b", 32),
    ("alibaba-token-plan", "alibaba-token-plan/qwen3.8-flash", 32),
    ("xai-oauth", "xai-oauth/grok-4.5", 32),
    ("zai-coding-plan", "zai-coding-plan/glm-5-turbo", 32),   # negative control
    ("opencode-go", "opencode-go/mimo-v2.5", 32),
    ("opencode-go", "opencode-go/deepseek-v4-flash-vision-exp", 32),
]


def url_for(base_url, protocol):
    if protocol == "anthropic":
        return base_url + "/v1/messages"
    if protocol == "openai_responses":
        return base_url + "/responses"
    return base_url + "/chat/completions"


def build_payload(protocol, model_id, kind, value=None, max_tokens=16,
                  png_side=1, tool_choice=True):
    """The wire shape the client itself uses for each protocol (client-verified)."""
    text = "Reply with the single word: pong"
    tool_prompt = "Echo the text 'ping' using the r18_echo tool."
    if protocol == "anthropic":
        body = {
            "model": model_id,
            "max_tokens": max_tokens,
            "system": "You are a test harness.",
            "messages": [{"role": "user", "content": [{"type": "text", "text": text}]}],
            "stream": False,
        }
        if kind == "effort":
            body["output_config"] = {"effort": value}
        elif kind == "tool":
            body["messages"] = [{"role": "user", "content": [{"type": "text", "text": tool_prompt}]}]
            body["tools"] = TOOL_SCHEMA_ANTHROPIC
            if tool_choice:
                body["tool_choice"] = {"type": "tool", "name": "r18_echo"}
        elif kind == "image":
            body["messages"] = [{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png",
                                             "data": b64(png_side)}},
                {"type": "text", "text": "Describe this image in one word."},
            ]}]
        return body

    if protocol == "openai_responses":
        body = {
            "model": model_id,
            "input": [{"role": "user", "content": [{"type": "input_text", "text": text}]}],
            "store": False,
            "stream": True,
        }
        if kind == "effort":
            body["reasoning"] = {"effort": value}
        elif kind == "tool":
            body["input"] = [{"role": "user", "content": [{"type": "input_text", "text": tool_prompt}]}]
            body["tools"] = TOOL_SCHEMA_RESPONSES
            if tool_choice:
                body["tool_choice"] = "required"
        elif kind == "image":
            body["input"] = [{"role": "user", "content": [
                {"type": "input_image", "image_url": "data:image/png;base64," + b64(png_side)},
                {"type": "input_text", "text": "Describe this image in one word."},
            ]}]
        return body

    body = {
        "model": model_id,
        "messages": [{"role": "user", "content": text}],
        "max_tokens": max_tokens,
        "stream": False,
    }
    if kind == "effort":
        body["reasoning_effort"] = value
    elif kind == "tool":
        body["messages"] = [{"role": "user", "content": tool_prompt}]
        body["tools"] = TOOL_SCHEMA
        if tool_choice:
            body["tool_choice"] = {"type": "function", "function": {"name": "r18_echo"}}
    elif kind == "image":
        body["messages"] = [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": "data:image/png;base64," + b64(png_side)}},
            {"type": "text", "text": "Describe this image in one word."},
        ]}]
    elif kind == "kimi-effort":
        body["thinking"] = {"type": "enabled", "effort": value}
    return body


def send(url, headers, payload, timeout=TIMEOUT):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    for k, v in headers.items():
        req.add_header(k, v)
    req.add_header("content-type", "application/json")
    req.add_header("user-agent", UA)
    ctx = ssl.create_default_context()
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            raw = resp.read()
            return resp.status, raw, int((time.time() - started) * 1000), None
    except urllib.error.HTTPError as e:
        raw = e.read()
        return e.code, raw, int((time.time() - started) * 1000), None
    except Exception as e:  # timeout, connection reset, TLS
        return None, None, int((time.time() - started) * 1000), "%s: %s" % (type(e).__name__, e)


def derive(status, body, protocol, raw_text=""):
    """Everything the audit reads out of one response, so the raw capture stays raw."""
    out = {"status": status}
    if isinstance(body, dict):
        msg = None
        if protocol == "anthropic":
            blocks = body.get("content") or []
            out["content_block_types"] = [b.get("type") for b in blocks if isinstance(b, dict)]
            out["tool_call_wellformed"] = any(
                b.get("type") == "tool_use" and b.get("name") == "r18_echo"
                for b in blocks if isinstance(b, dict))
            msg = {b.get("type"): b for b in blocks if isinstance(b, dict)}.get("text")
            out["message_keys"] = sorted(body.keys())
        elif protocol == "openai_responses":
            items = body.get("output") or []
            out["output_item_types"] = [i.get("type") for i in items if isinstance(i, dict)]
            out["message_keys"] = sorted(body.keys())
            out["tool_call_wellformed"] = any(
                i.get("type") == "function_call" and i.get("name") == "r18_echo"
                for i in items if isinstance(i, dict))
        else:
            choices = body.get("choices") or []
            if choices:
                m = choices[0].get("message") or {}
                msg = m
                out["message_keys"] = sorted(m.keys())
                tc = m.get("tool_calls") or []
                out["tool_call_wellformed"] = bool(
                    tc and (tc[0].get("function") or {}).get("name") == "r18_echo")
                out["finish_reason"] = choices[0].get("finish_reason")
            out["top_keys"] = sorted(body.keys())
            if msg is not None:
                out["has_reasoning_content"] = bool(
                    isinstance(msg, dict) and msg.get("reasoning_content"))
        out["usage"] = body.get("usage")
    elif isinstance(body, str):
        out["body_text_preview"] = body[:300]
        if "r18_echo" in body or "function_call" in body:
            out["tool_call_wellformed"] = '"name":"r18_echo"' in body.replace(" ", "") \
                or "function_call" in body
    if raw_text and "r18_echo" in raw_text:
        out["sse_mentions_tool"] = "r18_echo" in raw_text
    return out


def run_suite(name, rows, kind, cfg, max_tokens=16, png_side=1, out_name=None):
    lanes = cfg["providers"]
    results = []
    for row in rows:
        if isinstance(row, dict):
            lane, alias, tag = row["lane"], row["alias"], row.get("tag")
            value, mt = row.get("value"), row.get("max_tokens", max_tokens)
            side, tc = row.get("png", png_side), row.get("tool_choice", True)
        else:
            lane, alias = row[0], row[1]
            value = row[2] if len(row) > 2 and kind != "image" else None
            tag = None
            if kind == "image" and len(row) > 2:
                side = row[2]
            else:
                side = png_side
            mt, tc = max_tokens, True
        mc = cfg["models"].get(alias)
        if mc is None:
            results.append({"lane": lane, "alias": alias, "value": value,
                            "error": "alias not present in config"})
            continue
        pid = mc["provider"]
        pc = lanes.get(pid, {})
        protocol = common.effective_protocol(pc, mc)
        base = common.effective_base_url(pc, mc)
        if pid in DEAD_LANES:
            results.append({"lane": lane, "alias": alias, "value": value,
                            "provider": pid, "protocol": protocol,
                            "skipped": "lane unreachable per census D1 (401)", "status": 401})
            continue
        model_id = mc.get("model") or alias
        eff_kind = "kimi-effort" if (kind == "effort" and protocol == "kimi") else kind
        payload = build_payload(protocol, model_id, eff_kind, value, mt, side, tc)
        headers = common.auth_headers(pc, protocol)
        url = url_for(base, protocol)
        status, raw, ms, err = send(url, headers, payload)
        raw_text = (raw or b"").decode("utf-8", "replace")
        body = common.parse_body(raw)
        row_out = {
            "suite": name, "lane": lane, "alias": alias, "provider": pid,
            "protocol": protocol, "url": url, "model_id": model_id,
            "value": value, "tag": tag, "max_tokens": mt, "png_side": side if kind == "image" else None,
            "status": status, "ms": ms, "error": err,
            "request_headers": common.redact_headers(headers),
            "request_body": common.redact(payload),
            "response": body,
            "derived": derive(status, body, protocol, raw_text),
        }
        results.append(row_out)
        d = row_out["derived"]
        flags = [k for k in ("tool_call_wellformed", "has_reasoning_content", "sse_mentions_tool")
                 if d.get(k)]
        print("%-16s %-44s %-16s status=%-5s %6sms %s" % (
            name, alias, value or tag or "", status, ms,
            ",".join(flags) or (err or (d.get("finish_reason") or ""))), flush=True)
        time.sleep(0.4)
    common.write_json(out_name or "probes-%s.json" % name, {
        "suite": name,
        "config_json_digest_16": common.config_digest(cfg),
        "generated_by": "scripts/probe_live.py",
        "user_agent": UA,
        "note": "headers redacted (<redacted:len=N>); no credential value is stored",
        "results": results,
    })
    return results


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    cfg = common.load_config()
    print("config json-canonical digest/16:", common.config_digest(cfg), flush=True)
    if which in ("effort", "all"):
        print("\n== effort suite ==", flush=True)
        run_suite("effort", EFFORT_PLAN, "effort", cfg)
    if which in ("tool", "all"):
        print("\n== tool suite ==", flush=True)
        run_suite("tool", TOOL_PLAN, "tool", cfg)
    if which in ("image", "all"):
        print("\n== image suite ==", flush=True)
        run_suite("image", IMAGE_PLAN, "image", cfg)
    if which == "pass3":
        print("\n== tool suite (pass 3, client shape without tool_choice) ==", flush=True)
        run_suite("tool", TOOL3_PLAN, "tool", cfg, max_tokens=256,
                  out_name="probes-tool-pass3.json")
    if which == "pass4":
        print("\n== effort suite (pass 4, the off_effort value) ==", flush=True)
        run_suite("effort", EFFORT4_PLAN, "effort", cfg,
                  out_name="probes-effort-pass4.json")
    if which == "pass2":
        print("\n== effort suite (pass 2) ==", flush=True)
        run_suite("effort", EFFORT2_PLAN, "effort", cfg, out_name="probes-effort-pass2.json")
        print("\n== tool suite (pass 2, max_tokens=256) ==", flush=True)
        run_suite("tool", TOOL2_PLAN, "tool", cfg, max_tokens=256,
                  out_name="probes-tool-pass2.json")
        print("\n== image suite (pass 2, 32x32 png) ==", flush=True)
        run_suite("image", IMAGE2_PLAN, "image", cfg, out_name="probes-image-pass2.json")


if __name__ == "__main__":
    main()
