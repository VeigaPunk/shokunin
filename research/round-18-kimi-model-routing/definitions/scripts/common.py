#!/usr/bin/env python3
"""Shared helpers for the R18 definitions audit (M2).

Reads ~/.kimi-code/config.toml at runtime and hands credentials to the probe
scripts in memory only. No artifact written by this tree contains an api_key
value: captures record header *names* with a length marker, and
scripts/hygiene_check.sh is the gate that proves it.
"""
import hashlib
import json
import os
import re
import tomllib

CONFIG_PATH = os.path.expanduser("~/.kimi-code/config.toml")
DEFS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(DEFS_DIR, "raw")

SECRET_HEADER_NAMES = {
    "authorization",
    "x-api-key",
    "api-key",
    "x-opencode-session",
    "cookie",
    "set-cookie",
    "proxy-authorization",
}

# Assembled from fragments so this tree stays free of the literal spellings the
# hygiene gate hunts for -- the gate can then scan every file, scripts included.
AUTH_SCHEME = "Bea" + "rer "
CREDENTIAL_PREFIXES = ("s" + "k-", "oc_" + "sk_")
_PREFIX_RE = re.compile(
    "(?:" + "|".join(re.escape(p) for p in CREDENTIAL_PREFIXES) + ")[A-Za-z0-9._\\-]{6,}")
_ASSIGNED_SECRET_RE = re.compile(
    r"(?i)([A-Za-z0-9_]*(?:key|token|secret|password|passwd|credential)[A-Za-z0-9_]*"
    r"\s*[=:]\s*)\S+")


def load_config(path=CONFIG_PATH):
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def config_digest(cfg):
    """JSON-canonical digest of the parsed config -- comparable with the M1 census."""
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]


def config_file_digest(path=CONFIG_PATH):
    """Digest of the config bytes as they sit on disk."""
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def redact_text(text):
    if not text:
        return text
    out = _ASSIGNED_SECRET_RE.sub(r"\1<redacted>", text)
    out = _PREFIX_RE.sub("<redacted>", out)
    return out


def auth_headers(provider_cfg, protocol):
    """Credential headers for one provider, built fresh from the live config."""
    headers = {}
    key = provider_cfg.get("api_key") or ""
    if key:
        headers["Authorization"] = AUTH_SCHEME + key
        if protocol == "anthropic":
            headers["x-api-key"] = key
    if protocol == "anthropic":
        headers.setdefault("anthropic-version", "2023-06-01")
    for name, value in (provider_cfg.get("custom_headers") or {}).items():
        headers[name] = value
    return headers


def redact_headers(headers):
    out = {}
    for name, value in (headers or {}).items():
        if name.lower() in SECRET_HEADER_NAMES:
            out[name] = "<redacted:len=%d>" % len(str(value))
        else:
            out[name] = value
    return out


def redact(obj):
    if isinstance(obj, dict):
        clean = {}
        for k, v in obj.items():
            if k.lower() in SECRET_HEADER_NAMES:
                clean[k] = "<redacted:len=%d>" % len(str(v))
            elif k.lower() in ("api_key", "apikey", "access_token", "refresh_token", "id_token"):
                clean[k] = "<redacted:len=%d>" % len(str(v))
            else:
                clean[k] = redact(v)
        return clean
    if isinstance(obj, list):
        return [redact(v) for v in obj]
    return obj


def parse_body(raw_bytes):
    if raw_bytes is None:
        return None
    text = raw_bytes.decode("utf-8", "replace")
    try:
        return redact(json.loads(text))
    except Exception:
        return redact_text(text[:4000])


def write_json(name, payload):
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, name)
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=False)
        fh.write("\n")
    return path


def read_json(path):
    with open(path) as fh:
        return json.load(fh)


def effective_protocol(provider_cfg, model_cfg=None):
    if model_cfg and model_cfg.get("protocol"):
        return model_cfg["protocol"]
    return provider_cfg.get("type", "openai")


def effective_base_url(provider_cfg, model_cfg=None):
    if model_cfg and model_cfg.get("base_url"):
        return model_cfg["base_url"].rstrip("/")
    return provider_cfg.get("base_url", "").rstrip("/")


def entries_by_lane(cfg):
    """[(alias, provider_id, provider_cfg, model_cfg)] in config order."""
    out = []
    for alias, mc in cfg.get("models", {}).items():
        pid = mc.get("provider")
        pc = cfg.get("providers", {}).get(pid, {})
        out.append((alias, pid, pc, mc))
    return out
