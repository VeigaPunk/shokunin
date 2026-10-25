#!/usr/bin/env python3
"""Local discovery evidence for the R18 codex 'ultra' effort probe (no quota).

    python3 scripts/collect_discovery.py

Collects, reproducibly, where the candidate effort values come from:

1. The codex model catalog cache (`~/.codex/models_cache.json`) -- the same
   source M5 used for `service_tiers`; here for `supported_reasoning_levels`.
2. The codex CLI binary's embedded fallback catalog -- the models-manager JSON
   blob compiled into the binary, which declares the same reasoning levels
   without any network fetch.
3. The kimi-code client binary: whether the effort value set is closed on the
   client side (it is not: `support_efforts` is a free-form string array and
   non-Kimi providers receive effort strings without client-side mapping).
4. The oauth shim in the request path: whether any effort rewrite is enabled
   (SHIM_FIX_EFFORT, read from the running process environment).
5. The live config's two codex aliases as the template for a new variant entry
   (api_key excluded by construction -- the key is never read into this file).

Every string written here has been checked against the config's credential
values by scripts/hygiene_check.py; the collector itself never prints a
credential.
"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

CATALOG_PATH = os.path.expanduser("~/.codex/models_cache.json")
CODEX_BIN = (
    "/home/vgpnk/.local/share/mise/installs/node/26.12.0/lib/node_modules/"
    "@openai/codex/node_modules/@openai/codex-linux-x64/vendor/"
    "x86_64-unknown-linux-musl/bin/codex"
)
KIMI_BIN = os.path.expanduser("~/.kimi-code/bin/kimi")
SHIM_PATH = os.path.expanduser("~/.local/share/oauth-shim/shim.py")
SHIM_PID_CMD = "systemctl --user show codex-shim -p MainPID"

CONFIG_PATH = common.CONFIG_PATH


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gather_catalog():
    with open(CATALOG_PATH) as fh:
        cat = json.load(fh)
    models = {}
    for model in cat.get("models", []):
        levels = model.get("supported_reasoning_levels") or []
        models[model.get("slug")] = {
            "supported_reasoning_levels": [lvl.get("effort") for lvl in levels],
            "level_descriptions": {lvl.get("effort"): lvl.get("description")
                                   for lvl in levels},
            "default_reasoning_level": model.get("default_reasoning_level"),
        }
    return {
        "path": CATALOG_PATH,
        "sha256": sha256_file(CATALOG_PATH),
        "fetched_at": cat.get("fetched_at"),
        "etag": cat.get("etag"),
        "client_version": cat.get("client_version"),
        "models": models,
    }


def gather_codex_binary():
    data = open(CODEX_BIN, "rb").read()
    blob = None
    start = data.find(b'{\n  "models": [')
    if start < 0:
        start = data.find(b'{"models": [')
    if start >= 0:
        depth = 0
        buf = []
        for i in range(start, min(len(data), start + 1_200_000)):
            c = data[i]
            buf.append(c)
            if c == ord("{"):
                depth += 1
            elif c == ord("}"):
                depth -= 1
                if depth == 0:
                    blob = bytes(buf)
                    break
    embedded = None
    if blob is not None:
        try:
            parsed = json.loads(blob.decode("utf-8"))
            embedded = {
                "blob_bytes": len(blob),
                "models": {
                    m.get("slug"): {
                        "default_reasoning_level": m.get("default_reasoning_level"),
                        "supported_reasoning_levels": [
                            lvl.get("effort") for lvl in
                            (m.get("supported_reasoning_levels") or [])],
                        "multi_agent_reasoning_effort": m.get("multi_agent_reasoning_effort"),
                        "display_name": m.get("display_name"),
                    }
                    for m in parsed.get("models", [])
                },
            }
        except Exception as exc:  # noqa: BLE001
            embedded = {"error": "%s: %s" % (type(exc).__name__, exc)}
    enum_ctx = None
    m = re.search(rb"minimallowmediumxhighmaxultra(?:persistent)?", data)
    if m:
        enum_ctx = m.group(0).decode("utf-8", "replace")
    ultra_matches = [m.start() for m in re.finditer(rb'"effort": "ultra"', data)]
    return {
        "path": CODEX_BIN,
        "sha256": sha256_file(CODEX_BIN),
        "embedded_catalog": embedded,
        "effort_enum_string_context": enum_ctx,
        "quoted_effort_ultra_matches": len(ultra_matches),
    }


def gather_kimi_binary():
    data = open(KIMI_BIN, "rb").read()
    quoted_ultra = len(re.findall(rb'"ultra"', data))
    support_efforts_hits = len(re.findall(rb'support_efforts', data))
    default_effort_hits = len(re.findall(rb'default_effort', data))
    off_effort_hits = len(re.findall(rb'off_effort', data))
    hint = None
    m = re.search(rb"Non-Kimi providers receive effort strings[^`]{0,220}", data)
    if m:
        hint = m.group(0).decode("utf-8", "replace")
    schema = None
    m = re.search(rb"support_efforts: array\(string\(\)\)\.optional\(\),\s*"
                  rb"default_effort: string\(\)\.optional\(\)", data)
    if m:
        schema = m.group(0).decode("utf-8", "replace")
    opus = None
    m = re.search(rb'LATEST_OPUS_THINKING_EFFORTS\$1 = \[[^\]]{0,200}\]', data)
    if m:
        opus = re.sub(rb"\s+", b" ", m.group(0)).decode("utf-8", "replace")
    return {
        "path": KIMI_BIN,
        "sha256": sha256_file(KIMI_BIN),
        "quoted_ultra_strings": quoted_ultra,
        "support_efforts_string_occurrences": support_efforts_hits,
        "default_effort_string_occurrences": default_effort_hits,
        "off_effort_string_occurrences": off_effort_hits,
        "non_kimi_effort_hint": hint,
        "config_schema_fragment": schema,
        "latest_opus_efforts_fragment": opus,
    }


def gather_shim():
    env = {}
    pid = None
    out = os.popen(SHIM_PID_CMD).read().strip()
    if out.startswith("MainPID="):
        pid_txt = out.split("=", 1)[1].strip()
        if pid_txt.isdigit() and int(pid_txt) > 0:
            pid = int(pid_txt)
    if pid is not None:
        try:
            raw = open("/proc/%d/environ" % pid, "rb").read()
            for entry in raw.split(b"\0"):
                if not entry:
                    continue
                if b"=" not in entry:
                    continue
                k, v = entry.split(b"=", 1)
                k = k.decode("utf-8", "replace")
                v = v.decode("utf-8", "replace")
                if k in ("SHIM_PORT", "SHIM_UPSTREAM", "SHIM_MODELS",
                         "SHIM_MAX_CONCURRENT", "SHIM_FIX_EFFORT"):
                    env[k] = v
                elif k == "SHIM_TOKEN_CMD":
                    env[k] = "<redacted: command prints an OAuth token>"
        except OSError as exc:
            env["read_error"] = str(exc)
    src = open(SHIM_PATH).read()
    fix_effort_lines = [ln.strip() for ln in src.splitlines()
                        if "FIX_EFFORT" in ln][:4]
    return {
        "path": SHIM_PATH,
        "sha256": sha256_file(SHIM_PATH),
        "main_pid": pid,
        "environment": env,
        "fix_effort_source_lines": fix_effort_lines,
    }


def gather_config_entries():
    import tomllib
    with open(CONFIG_PATH, "rb") as fh:
        cfg = tomllib.load(fh)
    provider = cfg["providers"]["openai-codex"]
    provider_safe = {k: v for k, v in provider.items() if k != "api_key"}
    models = cfg.get("models", {})
    wanted = ["openai-codex/gpt-6.1-sol", "openai-codex/gpt-6.1-sol-high",
              "openai-codex/gpt-6-luna"]
    entries = {}
    for alias in wanted:
        if alias in models:
            entry = dict(models[alias])
            entry.pop("api_key", None)
            entries[alias] = entry
    thinking = cfg.get("thinking")
    secondary = cfg.get("secondary_model")
    return {
        "path": CONFIG_PATH,
        "file_sha256": common.config_file_sha256(CONFIG_PATH),
        "json_canonical_digest_16": common.config_digest(cfg),
        "provider_openai_codex": provider_safe,
        "aliases": entries,
        "thinking": thinking,
        "secondary_model": secondary,
    }


def main():
    evidence = {
        "mission": "M8 r18-codex-ultra-strong-entry",
        "codex_model_catalog": gather_catalog(),
        "codex_cli_binary": gather_codex_binary(),
        "kimi_client_binary": gather_kimi_binary(),
        "oauth_shim": gather_shim(),
        "live_config": gather_config_entries(),
    }
    out = common.write_json("discovery-evidence.json", evidence)
    print("wrote %s" % out)
    cat = evidence["codex_model_catalog"]
    sol = cat["models"].get("gpt-6.1-sol", {})
    print("catalog fetched_at=%s etag=%s" % (cat.get("fetched_at"), cat.get("etag")))
    print("catalog gpt-6.1-sol levels=%s default=%s" % (
        sol.get("supported_reasoning_levels"), sol.get("default_reasoning_level")))
    emb = (evidence["codex_cli_binary"]["embedded_catalog"] or {}).get("models", {})
    print("embedded gpt-6.1-sol levels=%s default=%s" % (
        (emb.get("gpt-6.1-sol") or {}).get("supported_reasoning_levels"),
        (emb.get("gpt-6.1-sol") or {}).get("default_reasoning_level")))
    print("kimi client quoted 'ultra' strings: %d" % (
        evidence["kimi_client_binary"]["quoted_ultra_strings"]))
    print("shim env: %s" % evidence["oauth_shim"]["environment"])
    return 0


if __name__ == "__main__":
    sys.exit(main())