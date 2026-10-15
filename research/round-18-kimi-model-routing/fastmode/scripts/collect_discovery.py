#!/usr/bin/env python3
"""Collect the local-discovery evidence behind the fast-mode variants.

    python3 scripts/collect_discovery.py

Three local sources explain where the candidate `service_tier` values came
from and why the probe could reach the backend at all:

  1. the codex CLI's model catalog cache (~/.codex/models_cache.json), which
     declares gpt-6.1-sol's service tier id ('priority', display name 'Fast');
  2. the codex CLI binary itself, whose embedded docs name the wire values
     `service_tier: "fast"` / `service_tier: "priority"` and whose Responses
     request struct carries the `service_tier` field;
  3. the local oauth-shim fronting chatgpt.com, which forwards request bodies
     verbatim -- it only swaps in a fresh OAuth token -- so any field the
     probe sends reaches the backend unchanged.

Writes raw/discovery-evidence.json. No credential material: the shim's token
command is recorded as a redacted marker, env values are filtered to the
SHIM_* configuration keys, and code excerpts that would spell the auth scheme
in full are summarised instead of quoted.
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

CODEX_CACHE = os.path.expanduser("~/.codex/models_cache.json")
CODEX_PKG = os.path.expanduser(
    "~/.local/share/mise/installs/node/26.12.0/lib/node_modules/@openai/codex")
CODEX_BIN = os.path.join(
    CODEX_PKG,
    "node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex")
SHIM = os.path.expanduser("~/.local/share/oauth-shim/shim.py")

BINARY_PATTERNS = [
    r'Fast mode:.{0,240}service_tier: .fast.. or .service_tier: .priority..',
    r'.{0,120}default_service_tier.: .priority.,',
    r'speed_tier[a-zA-Z_]*',
    r'fast_mode[a-zA-Z_]*',
    r'ultrafast_mode[a-zA-Z_]*',
    r'toggle_fast_mode',
    r'x-codex-[a-z-]*',
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def catalog_evidence():
    with open(CODEX_CACHE) as fh:
        cache = json.load(fh)
    models = []
    for m in cache.get("models", []):
        models.append({
            "slug": m.get("slug"),
            "visibility": m.get("visibility"),
            "supported_in_api": m.get("supported_in_api"),
            "additional_speed_tiers": m.get("additional_speed_tiers"),
            "service_tiers": m.get("service_tiers"),
            "default_service_tier": m.get("default_service_tier"),
        })
    return {
        "path": CODEX_CACHE,
        "fetched_at": cache.get("fetched_at"),
        "etag": cache.get("etag"),
        "client_version": cache.get("client_version"),
        "models": models,
    }


def binary_evidence():
    matches = {}
    for pattern in BINARY_PATTERNS:
        proc = subprocess.run(
            ["grep", "-aoE", pattern, CODEX_BIN],
            capture_output=True, text=True, errors="replace")
        found = []
        for line in proc.stdout.splitlines():
            line = line[:300]
            if line and line not in found:
                found.append(line)
            if len(found) >= 25:
                break
        matches[pattern] = found
    version = None
    pkg_path = os.path.join(CODEX_PKG, "package.json")
    if os.path.exists(pkg_path):
        with open(pkg_path) as fh:
            version = json.load(fh).get("version")
    return {
        "path": CODEX_BIN,
        "sha256": sha256_file(CODEX_BIN),
        "package_version": version,
        "matches": matches,
    }


def shim_evidence():
    with open(SHIM) as fh:
        source = fh.read()
    skip_block = re.search(
        r"for k, v in self\.headers\.items\(\):(.*?)\n\n", source, re.S)
    env = {}
    pids = subprocess.run(["pgrep", "-f", "oauth-shim/shim.py"],
                          capture_output=True, text=True).stdout.split()
    for pid in pids:
        try:
            raw = open("/proc/%s/environ" % pid, "rb").read()
        except OSError:
            continue
        for pair in raw.split(b"\0"):
            if pair.startswith(b"SHIM_"):
                name, _, value = pair.decode("utf-8", "replace").partition("=")
                if name == "SHIM_TOKEN_CMD":
                    value = "<redacted: command prints an OAuth token>"
                env[name] = value
        break
    return {
        "path": SHIM,
        "sha256": sha256_file(SHIM),
        "role": "token-injecting reverse proxy to chatgpt.com; request bodies "
                "are forwarded verbatim (no field rewriting)",
        "effort_rewrite_enabled": bool(env.get("SHIM_FIX_EFFORT")),
        "forwarded_header_exclusions_excerpt": skip_block.group(1).strip()
        if skip_block else None,
        "environment": env,
    }


def main():
    evidence = {
        "mission": "M5 r18-codex-fast-mode-probe",
        "collected_at_utc": __import__("time").strftime("%Y-%m-%dT%H:%M:%SZ",
                                                       __import__("time").gmtime()),
        "codex_model_catalog": catalog_evidence(),
        "codex_cli_binary": binary_evidence(),
        "oauth_shim": shim_evidence(),
        "client_custom_headers": None,
    }
    cfg = common.load_config(common.CONFIG_PATH)
    evidence["client_custom_headers"] = {
        "provider": "openai-codex",
        "headers": sorted((cfg["providers"]["openai-codex"].get("custom_headers") or {}).keys()),
        "source": "~/.kimi-code/config.toml, json-canonical digest %s"
                  % common.config_digest(cfg),
    }
    out = common.write_json("discovery-evidence.json", evidence)
    print("wrote %s" % out)
    print("catalog models: %d" % len(evidence["codex_model_catalog"]["models"]))
    for pattern, found in evidence["codex_cli_binary"]["matches"].items():
        print("binary %-46s matches=%d" % (pattern, len(found)))
    print("shim env keys: %s" % sorted(evidence["oauth_shim"]["environment"].keys()))


if __name__ == "__main__":
    main()
