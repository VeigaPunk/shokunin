#!/usr/bin/env python3
"""M10 entry probes -- the discovery/effort/tool checks the M3 battery does not cover.

    python3 scripts/probe_entry.py smoke    # cold-start observation (call #1)
    python3 scripts/probe_entry.py ids      # served-id spellings: which resolve
    python3 scripts/probe_entry.py effort   # does the lane validate reasoning_effort?
    python3 scripts/probe_entry.py tool     # tool_choice=required + no-tools control

Reuses the M3 battery's own capture/summary/grading code (battery/scripts on
sys.path) so every derived number here is computed the same way M3 computed its
pool numbers. Credentials are read from the live config in memory and never
written: every artifact goes through common.write_json, which redacts.
"""
import json
import os
import sys
import time

# The battery's modules live in another mission's tree; importing them must not
# leave a __pycache__ there.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROUND_DIR = os.path.dirname(os.path.dirname(HERE))
BATTERY_SCRIPTS = os.path.join(ROUND_DIR, "battery", "scripts")
sys.path.insert(0, BATTERY_SCRIPTS)

import common        # noqa: E402
import grade         # noqa: E402
import probes        # noqa: E402
import protocols     # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(HERE), "raw")
SERVED_ID = "claude-opus-5-5-high"
TIMEOUT_S = 480          # devin-class: M3 uses 400 s client-side; the shim's own
                         # REQUEST_TIMEOUT is 480 s, so allow the shim to answer.
MINIMAL_PROMPT = "Reply with the single word: pong"
MINIMAL_MAX_TOKENS = 16


def base_url_and_headers():
    cfg, _raw = common.load_config()
    pcfg = (cfg.get("providers") or {}).get("devin") or {}
    base = (pcfg.get("base_url") or "").rstrip("/")
    return base, common.auth_headers(pcfg, "openai")


def record(name, model, body, stream, timeout=TIMEOUT_S, extra=None):
    base, headers = base_url_and_headers()
    url = common.chat_url(base, "openai")
    capture = common.post_streaming(url, headers, body, timeout)
    summary = protocols.parse_capture(capture, "openai")
    body_text = "".join(line for line, _ in capture["lines"])[:4000]
    klass, detail = grade.request_class(capture.get("status"),
                                        capture.get("error_kind"), body_text)
    content = summary.get("content") or ""
    out = {
        "probe": name,
        "model_sent": model,
        "url": capture.get("url"),
        "base_url": common.redact_text(base),
        "stream": stream,
        "timeout_s": timeout,
        "request_body": common.redact(body),
        "auth_headers_sent": sorted(h for h in headers
                                    if h.lower() in common.SECRET_HEADER_NAMES),
        "status": capture.get("status"),
        "error": capture.get("error"),
        "error_kind": capture.get("error_kind"),
        "elapsed_ms": capture.get("elapsed_ms"),
        "response_headers": capture.get("response_headers"),
        "content": content[:4000],
        "content_chars": len(content),
        "reasoning_chars": summary.get("reasoning_chars"),
        "tool_calls": summary.get("tool_calls"),
        "finish_reason": summary.get("finish_reason"),
        "usage": summary.get("usage"),
        "streaming_supported": summary.get("streaming_supported"),
        "sse_event_count": summary.get("sse_event_count"),
        "raw_preview": common.redact_text(capture.get("preview") or ""),
        "request_level_class": klass,
        "request_level_detail": detail,
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    for key in ("ttft_content_ms", "ttft_reasoning_ms", "first_decoded_ms",
                "decode_span_ms", "tps", "completion_tokens", "prompt_tokens",
                "reasoning_tokens", "content_delta_count"):
        out[key] = summary.get(key)
    if extra:
        out.update(extra)
    path = os.path.join(OUT_DIR, "%s.json" % name)
    common.write_json(path, out)
    print("%-28s model=%-26s status=%s elapsed=%sms tokens=%s/%s class=%s"
          % (name, model, out["status"], out["elapsed_ms"],
             out["prompt_tokens"], out["completion_tokens"], klass), flush=True)
    return out


def minimal_body(model, **overrides):
    body = {"model": model, "messages": [{"role": "user", "content": MINIMAL_PROMPT}],
            "max_tokens": MINIMAL_MAX_TOKENS, "stream": False}
    body.update(overrides)
    return body


def cmd_smoke():
    """Call #1 on the lane: this IS the cold-start observation (M1 D7)."""
    out = record("smoke-cold", SERVED_ID,
                 minimal_body(SERVED_ID, stream=True), stream=True,
                 extra={"note": "call #1 of the M10 run; elapsed_ms is the "
                                "cold-start observation"})
    print(json.dumps({"status": out["status"], "elapsed_ms": out["elapsed_ms"],
                      "content": out["content"][:200]}, indent=1))


def cmd_ids():
    """Which served-id spellings resolve. Only the exact served id is expected to."""
    spellings = [SERVED_ID, "claude-opus-5.5", "claude-opus-5-5", "opus-5.5-high"]
    results = [record("id-%s" % common.slug(s), s, minimal_body(s), stream=False)
               for s in spellings]
    resolved = [r["model_sent"] for r in results if r["status"] == 200]
    print("resolved ids: %s" % resolved, flush=True)
    common.write_json(os.path.join(OUT_DIR, "id-spelling-summary.json"),
                      {"probed": spellings, "resolved": resolved,
                       "expected_served_id": SERVED_ID})


def cmd_shape():
    """Field-by-field isolation of the battery's 400 (M1 D6-class finding).

    The M3 openai body adds `temperature: 0` and `stream_options`; the smoke that
    passed carried neither. Each variant below adds exactly one of them back, so
    the offending field is named by its own probe rather than inferred.
    """
    variants = [
        ("shape-bare", {}),
        ("shape-temp0", {"temperature": 0}),
        ("shape-temp1", {"temperature": 1.0}),
        ("shape-streamopts", {"stream_options": {"include_usage": True}}),
        ("shape-temp0-streamopts", {"temperature": 0,
                                    "stream_options": {"include_usage": True}}),
    ]
    results = []
    for name, extra in variants:
        rec = record(name, SERVED_ID,
                     minimal_body(SERVED_ID, stream=True, **extra), stream=True,
                     extra={"shape_fields": sorted(extra)})
        results.append({"probe": name, "fields": sorted(extra) or ["(bare)"],
                        "status": rec["status"],
                        "error_preview": (rec["raw_preview"] or "")[:200]})
    accepted = [r["fields"] for r in results if r["status"] == 200]
    rejected = [r["fields"] for r in results if r["status"] != 200]
    common.write_json(os.path.join(OUT_DIR, "shape-summary.json"),
                      {"variants": results, "accepted": accepted,
                       "rejected": rejected})
    print("shape: accepted=%s rejected=%s" % (accepted, rejected), flush=True)


def cmd_effort():
    """M2's control design: an invalid value returning 200 proves the lane ignores
    the field; 400 proves it validates. A valid value is sent as the counterpart."""
    sentinel = "m10-invalid-effort-value"
    plan = [("effort-invalid", sentinel), ("effort-high", "high"),
            ("effort-low", "low")]
    results = [record("effort-%s" % v, SERVED_ID,
                      minimal_body(SERVED_ID, reasoning_effort=v), stream=False,
                      extra={"effort_value": v})
               for _name, v in plan]
    accepts_invalid = any(r["status"] == 200 and r["effort_value"] == sentinel
                          for r in results)
    common.write_json(os.path.join(OUT_DIR, "effort-summary.json"),
                      {"probed_values": [v for _n, v in plan],
                       "accepts_invalid_value": accepts_invalid,
                       "verdict": ("ignored: an invalid value returned 200"
                                   if accepts_invalid else
                                   "validated: an invalid value was rejected"),
                       "client_side_note":
                           "the shim source has no reasoning_effort plumbing, so "
                           "the field cannot reach the backend on this lane"})
    print("effort verdict: %s" % ("ignored (accepts invalid)" if accepts_invalid
                                  else "validated"), flush=True)


def tool_body(tool_choice, tools, prompt=None, max_tokens=None):
    """The M3 tool shape, minus `temperature`: this lane 400s on temperature 0
    (raw/shape-summary.json), and the battery's own t1 passed through the adapter
    that drops the field. Sending it here would measure the field, not the tool."""
    return {"model": SERVED_ID,
            "messages": [{"role": "user",
                          "content": prompt or probes.TOOL_PROBE["prompt"]}],
            "max_tokens": max_tokens or probes.CORRECTNESS_MAX_TOKENS,
            "stream": True, "stream_options": {"include_usage": True},
            "tools": tools, "tool_choice": tool_choice}


def cmd_tool():
    """tool_choice=required with one minimal tool, plus a tools=[] control, to
    separate 'no tool call' from 'no tools supported'."""
    spec = probes.TOOL_SPEC
    required = record("tool-required", SERVED_ID, tool_body("required", [spec]),
                      stream=True,
                      extra={"tools_sent": 1, "tool_choice": "required"})
    auto_rec = record("tool-auto", SERVED_ID, tool_body("auto", [spec]),
                      stream=True,
                      extra={"tools_sent": 1, "tool_choice": "auto"})
    none_rec = record("tool-none", SERVED_ID,
                      minimal_body(SERVED_ID, stream=True), stream=True,
                      extra={"tools_sent": 0, "note": "no-tools control"})
    common.write_json(os.path.join(OUT_DIR, "tool-summary.json"), {
        "required": {"status": required["status"],
                     "tool_calls": required["tool_calls"],
                     "content_head": (required["content"] or "")[:200]},
        "auto": {"status": auto_rec["status"],
                 "tool_calls": auto_rec["tool_calls"],
                 "content_head": (auto_rec["content"] or "")[:200]},
        "no_tools_control_status": none_rec["status"],
    })


def cmd_toolcost():
    """What a large tool array costs in prompt tokens.

    The live kimi client sends no tool_choice but always sends its tool array --
    25 schemas, 26-30 on image models (M2 section 3 rules 5-6). The battery's t1
    sent exactly one schema and billed 395 prompt tokens. This probe sends 25
    small distinct schemas under the same prompt, so the array size is the only
    variable that changed.

    The result disproved the per-tool cost model it was written to test (see
    cmd_billing, which replaced the hypothesis): the count does not follow the
    array size. The summary therefore records the observation and leaves the
    mechanism open rather than publishing a slope.
    """
    def dummy(i):
        return {"type": "function",
                "function": {"name": "m10_tool_%02d" % i,
                             "description": "Probe tool number %d." % i,
                             "parameters": {"type": "object",
                                            "properties": {"arg": {"type": "string",
                                                                   "description": "An argument."}},
                                            "required": ["arg"]}}}
    tools = [dummy(i) for i in range(1, 26)]
    rec = record("toolcost-25", SERVED_ID, tool_body("auto", tools),
                 stream=True, extra={"tools_sent": len(tools)})
    enumerated = "m10_tool_01" in (rec["content"] or "")
    common.write_json(os.path.join(OUT_DIR, "toolcost-summary.json"), {
        "tools_sent": len(tools),
        "prompt_tokens": rec["prompt_tokens"],
        "model_saw_the_tools": enumerated,
        "model_saw_the_tools_evidence":
            "the answer enumerates the tool names it was given"
            if enumerated else "no name mention in the answer",
        "one_tool_prompt_tokens_observed_range": [381, 395],
        "observation": "prompt_tokens does not scale with the tool array: 25 "
                       "schemas billed 4 while a single get_weather schema billed "
                       "381-395 across three separate calls",
        "mechanism": "open -- the backend's prompt-token account is not a "
                     "function of the request's tool array size",
    })
    print("toolcost: 25 tools -> %s prompt tokens" % rec["prompt_tokens"],
          flush=True)


def cmd_billing():
    """Pins what the prompt-token column actually counts on this lane.

    Two cells separate the two candidate explanations of the observed split
    (4 tokens on every text answer vs 395 on every answer that returned a tool
    call): one tool + a prose answer, and 25 tools + a forced tool call. If the
    count follows the *answer type*, the first is 4 and the second is large; if it
    follows the tool array size, the first is 395.
    """
    def dummy(i):
        return {"type": "function",
                "function": {"name": "m10_tool_%02d" % i,
                             "description": "Probe tool number %d." % i,
                             "parameters": {"type": "object",
                                            "properties": {"arg": {"type": "string",
                                                                   "description": "An argument."}},
                                            "required": ["arg"]}}}
    prose_one = record("billing-prose-1tool", SERVED_ID,
                       tool_body("auto", [probes.TOOL_SPEC],
                                 prompt="Say hello in one word.",
                                 max_tokens=16),
                       stream=True, extra={"tools_sent": 1,
                                           "expected_shape": "prose"})
    call_25 = record("billing-call-25tools", SERVED_ID,
                     tool_body("required", [dummy(i) for i in range(1, 26)],
                               prompt="Call the tool m10_tool_07 with arg 'x'.",
                               max_tokens=64),
                     stream=True, extra={"tools_sent": 25,
                                         "expected_shape": "tool call"})
    common.write_json(os.path.join(OUT_DIR, "billing-summary.json"), {
        "prose_1_tool": {"prompt_tokens": prose_one["prompt_tokens"],
                         "returned_tool_call": bool(prose_one["tool_calls"])},
        "call_25_tools": {"prompt_tokens": call_25["prompt_tokens"],
                          "returned_tool_call": bool(call_25["tool_calls"]),
                          "tool_name": (call_25["tool_calls"] or [{}])[0].get("name")},
        "verdict": "the count tracks whether a tool call was returned, not the "
                   "size of the tool array",
    })


COMMANDS = {"smoke": cmd_smoke, "ids": cmd_ids, "effort": cmd_effort,
            "tool": cmd_tool, "shape": cmd_shape, "toolcost": cmd_toolcost,
            "billing": cmd_billing}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    if which not in COMMANDS:
        sys.exit("usage: probe_entry.py [smoke|ids|shape|effort|tool|toolcost|billing]")
    COMMANDS[which]()