#!/usr/bin/env python3
"""Capture what the real client transmits, per declared config field.

This is the evidence behind ANALYSIS.md section 3. A scratch HOME holds a
synthetic kimi-code config whose only provider is scripts/mock_provider.py; the
shipped client (~/.kimi-code/bin/kimi) is run once per test model, and the
request it sends is recorded. Zero quota is spent: the upstream is loopback.

Test models isolate one declared field each (default_effort, the
[models.<alias>.overrides] table, off_effort, max_output_size, support_efforts
fallback, protocol overrides, capability lists). Two config flavours are run:

  global_max  -- [thinking] effort = "max", as the live config has it
  no_global   -- the same config with that line removed

Usage:  python3 scripts/probe_client_semantics.py [--kimi PATH]
Writes: raw/client-semantics.json
"""
import argparse
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

KIMI = os.path.expanduser("~/.kimi-code/bin/kimi")
SCRATCH = "/tmp/r18-defs-client-semantics"

# alias -> extra [models.*] fields (provider is always "mock")
TEST_MODELS = {
    "plain": {},
    "offnone": {"support_efforts": ["low", "high", "max"], "off_effort": "none",
                "default_effort": "high"},
    "noonf": {"support_efforts": ["low", "high", "max"], "default_effort": "high"},
    "offeffs": {"support_efforts": ["low", "high", "max"], "off_effort": "none"},
    "override": {"support_efforts": ["low", "high", "max"],
                 "overrides": {"default_effort": "low"}},
    "xhigh": {"support_efforts": ["low", "medium", "xhigh"]},
    "onlymax": {"support_efforts": ["max"]},
    "onlylow": {"support_efforts": ["low"]},
    "lowhigh": {"support_efforts": ["low", "high"]},
    "allof": {"support_efforts": ["minimal", "low", "medium", "high"], "off_effort": "none"},
    "wide": {"support_efforts": ["minimal", "low", "medium", "high", "xhigh", "max"]},
    "maxout": {"max_output_size": 64000},
    "imgonly": {"capabilities": ["image_in", "thinking"]},
    "notools": {"capabilities": ["thinking"]},
    "toolgated": {"capabilities": ["image_in", "video_in", "audio_in", "thinking",
                                   "always_thinking", "tool_use", "dynamically_loaded_tools"]},
    "anthropic": {"protocol": "anthropic", "max_output_size": 12345,
                  "support_efforts": ["low", "high"]},
    "anthropic2": {"protocol": "anthropic", "support_efforts": ["low", "medium", "xhigh"]},
    "responses": {"protocol": "openai_responses", "max_output_size": 32000,
                  "support_efforts": ["low", "medium", "xhigh"]},
}

TOML_SCALARS = {str: lambda v: '"%s"' % v, int: lambda v: str(v), bool: lambda v: str(v).lower()}


def toml_value(v):
    if isinstance(v, list):
        return "[ " + ", ".join(toml_value(x) for x in v) + " ]"
    return TOML_SCALARS[type(v)](v)


def build_config(port, global_effort):
    lines = [
        'default_model = "mock/plain"',
        'default_permission_mode = "auto"',
        "",
        "[providers.mock]",
        'type = "openai"',
        'base_url = "http://127.0.0.1:%d/v1"' % port,
        'api_key = "mock-local"',
        "",
        "[providers.mockkimi]",
        'type = "kimi"',
        'base_url = "http://127.0.0.1:%d/v1"' % port,
        'api_key = "mock-local"',
        "",
        '[models."mockkimi/kmock"]',
        'provider = "mockkimi"',
        'model = "kmock"',
        "max_context_size = 262144",
        'capabilities = [ "thinking", "tool_use" ]',
        'support_efforts = [ "low", "high", "max" ]',
        'default_effort = "max"',
        "",
        '[models."mockkimi/kimiout"]',
        'provider = "mockkimi"',
        'model = "kimiout"',
        "max_context_size = 262144",
        "max_output_size = 12345",
        'capabilities = [ "thinking", "tool_use" ]',
        "",
    ]
    for alias, extra in TEST_MODELS.items():
        caps = extra.get("capabilities", ["thinking", "tool_use"])
        lines += ['[models."mock/%s"]' % alias, 'provider = "mock"', 'model = "%s"' % alias,
                  "max_context_size = 1000000",
                  'capabilities = [ %s ]' % ", ".join('"%s"' % c for c in caps)]
        for k, v in extra.items():
            if k in ("overrides", "capabilities"):
                continue
            lines.append("%s = %s" % (k, toml_value(v)))
        if "overrides" in extra:
            lines += ['', '[models."mock/%s".overrides]' % alias]
            for k, v in extra["overrides"].items():
                lines.append("%s = %s" % (k, toml_value(v)))
        lines.append("")
    lines += ["[thinking]", "enabled = true"]
    if global_effort:
        lines.append('effort = "%s"' % global_effort)
    lines += ["", "[secondary_model]", 'default_model = "mock/plain"', ""]
    return "\n".join(lines)


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def run_one(kimi, home, alias, capdir, timeout=90):
    shutil.rmtree(capdir, ignore_errors=True)
    os.makedirs(capdir, exist_ok=True)
    env = dict(os.environ, HOME=home)
    try:
        subprocess.run([kimi, "-p", "hello", "-m", alias], env=env, timeout=timeout,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       cwd=os.path.dirname(home))
    except subprocess.TimeoutExpired:
        return None, "client timed out"
    frames = []
    for name in sorted(os.listdir(capdir)):
        with open(os.path.join(capdir, name)) as fh:
            rec = json.load(fh)
        if isinstance(rec.get("body"), dict) and "model" in rec["body"]:
            frames.append({"path": rec["path"], "body": common.redact(rec["body"]),
                           "headers": rec["headers"]})
    return (frames[0] if frames else None), (None if frames else "no request captured")


def salient(frame):
    """The fields the audit reasons about, pulled out of whatever shape was sent."""
    if frame is None:
        return {}
    b = frame["body"]
    out = {"path": frame["path"], "model": b.get("model"),
           "tools": len(b.get("tools") or []),
           "stream": b.get("stream")}
    for key in ("reasoning_effort", "max_tokens", "max_completion_tokens"):
        if key in b:
            out[key] = b[key]
    if isinstance(b.get("output_config"), dict):
        out["output_config.effort"] = b["output_config"].get("effort")
    if isinstance(b.get("reasoning"), dict):
        out["reasoning.effort"] = b["reasoning"].get("effort")
    if isinstance(b.get("thinking"), dict):
        out["thinking.effort"] = b["thinking"].get("effort")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kimi", default=KIMI)
    args = ap.parse_args()
    kimi = args.kimi

    port = free_port()
    scratch = os.path.join(SCRATCH, "home")
    capdir = os.path.join(SCRATCH, "cap")
    os.makedirs(os.path.join(scratch, ".kimi-code"), exist_ok=True)

    server = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                           "mock_provider.py"),
                               "--port", str(port), "--cap", capdir],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.0)

    results = []
    try:
        for flavour, global_effort in (("global_max", "max"), ("no_global", None)):
            cfg_path = os.path.join(scratch, ".kimi-code", "config.toml")
            with open(cfg_path, "w") as fh:
                fh.write(build_config(port, global_effort))
            for alias in list(TEST_MODELS) + ["mockkimi/kmock", "mockkimi/kimiout"]:
                full = alias if alias.startswith("mockkimi/") else "mock/%s" % alias
                frame, err = run_one(kimi, scratch, full, capdir, timeout=90)
                row = {"flavour": flavour, "alias": full,
                       "declared": ({"provider_type": "kimi"} if alias.startswith("mockkimi/")
                                    else dict(TEST_MODELS[alias],
                                              **({"global_effort": global_effort}
                                                 if global_effort else {}))),
                       "sent": salient(frame), "error": err}
                results.append(row)
                sent = row["sent"]
                print("%-10s %-14s -> effort=%-9r max_tokens=%-7r tools=%s" % (
                    flavour, row["alias"],
                    sent.get("reasoning_effort") or sent.get("output_config.effort")
                    or sent.get("reasoning.effort") or sent.get("thinking.effort"),
                    sent.get("max_tokens") or sent.get("max_completion_tokens"),
                    sent.get("tools")), flush=True)
    finally:
        server.terminate()
        server.wait(timeout=10)

    with open(os.path.join(common.DEFS_DIR, "raw", "client-semantics.json"), "w") as fh:
        json.dump({
            "generated_by": "scripts/probe_client_semantics.py",
            "kimi_binary": kimi,
            "scratch_config_note": ("synthetic config; the only credential in it is the literal "
                                    "'mock-local' for a loopback provider"),
            "results": results,
        }, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print("wrote raw/client-semantics.json (%d rows)" % len(results))


if __name__ == "__main__":
    main()
