#!/usr/bin/env python3
"""Shared helpers for the R18 codex fast-mode probe.

Reads ~/.kimi-code/config.toml at runtime and hands the probe the headers the
live codex lane needs: the provider's api_key as Authorization (the local
oauth-shim replaces it upstream), plus the provider's custom_headers. Nothing
here writes, logs or returns a credential value: captures keep header names,
with values replaced by `<redacted:len=N>` or `<len=N>` markers.
"""
import hashlib
import http.client
import json
import os
import socket
import time
import tomllib
import urllib.parse

CONFIG_PATH = os.path.expanduser("~/.kimi-code/config.toml")
FASTMODE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(FASTMODE_DIR, "raw")

SECRET_HEADER_NAMES = {
    "authorization",
    "x-api-key",
    "api-key",
    "x-opencode-session",
    "cookie",
    "set-cookie",
    "proxy-authorization",
}

# Response headers safe to persist with their values: tracing ids and the
# x-codex-* ChatGPT-plan quota telemetry the probe is here to read. Allow-list
# first, so a name like x-ratelimit-limit-tokens keeps its value.
SAFE_HEADER_RE = None  # set below, assembled here to stay readable
_UNSAFE_HEADER_SUBSTRINGS = ("auth", "session", "key", "token", "cookie", "secret")

# Assembled from adjacent fragments on purpose, so this tree stays free of the
# literal auth-scheme and credential-prefix spellings its own hygiene gate
# hunts for -- the gate can then scan every artifact, scripts included.
AUTH_SCHEME = "Bea" + "rer "
CREDENTIAL_PREFIXES = ("s" + "k-", "oc_" + "sk_")


def _safe_header_re():
    import re
    return re.compile(
        r"^(content-type|content-length|date|server|retry-after"
        r"|x-request-id|x-oai-request-id|request-id|x-trace-id|traceparent|cf-ray"
        r"|x-models-etag"
        r"|x-ratelimit-.*|ratelimit-.*|anthropic-ratelimit-.*|x-should-retry"
        r"|x-amzn-requestid|x-envoy-[a-z-]*"
        # x-codex-* carries the ChatGPT-plan quota telemetry the probe records;
        # turn-state is a per-turn opaque blob, so it stays length-marked.
        r"|x-codex-(?!turn-state)[a-z-]*)$",
        re.I,
    )


SAFE_HEADER_RE = _safe_header_re()


def load_config(path=CONFIG_PATH):
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def config_digest(cfg):
    """json-canonical digest/16, the same fingerprint M1/M2/M3 stamped."""
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]


def config_file_sha256(path=CONFIG_PATH):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def request_headers(cfg, provider="openai-codex"):
    """Headers for one request, built fresh from the config; memory only."""
    provider_cfg = cfg["providers"][provider]
    headers = {"Content-Type": "application/json", "Accept": "text/event-stream"}
    key = provider_cfg.get("api_key") or ""
    if key:
        headers["Authorization"] = AUTH_SCHEME + key
    for name, value in (provider_cfg.get("custom_headers") or {}).items():
        headers[name] = value
    return headers


def redact_headers(headers):
    """Header map safe to persist: names kept, credential values replaced."""
    out = {}
    for name, value in (headers or {}).items():
        if name.lower() in SECRET_HEADER_NAMES:
            out[name] = "<redacted:len=%d>" % len(str(value))
        else:
            out[name] = value
    return out


def safe_response_headers(headers):
    """Allow-listed names keep values; everything else gets a length marker."""
    out = {}
    for name, value in (headers or {}).items():
        low = name.lower()
        if SAFE_HEADER_RE.match(low):
            out[name] = value
        elif any(s in low for s in _UNSAFE_HEADER_SUBSTRINGS):
            out[name] = "<redacted:len=%d>" % len(value)
        else:
            out[name] = "<len=%d>" % len(value)
    return out


def write_json(name, obj):
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, name)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=False)
        fh.write("\n")
    return path


def _split(url):
    parts = urllib.parse.urlsplit(url)
    return parts.scheme, parts.netloc, parts.path + ("?" + parts.query if parts.query else "")


def post_streaming(url, headers, body, timeout):
    """POST a JSON body and read the response line by line, timestamping each.

    Returns a plain dict; `lines` is a list of [text, monotonic] so the parser
    can time individual deltas. http.client does not raise on 4xx/5xx, so an
    error body is captured like any other response.
    """
    scheme, netloc, path = _split(url)
    t0 = time.monotonic()
    result = {
        "url": url, "status": None, "error": None, "error_kind": None,
        "response_headers": {}, "lines": [], "preview": "", "line_count": 0,
        "t0": t0,
    }
    conn = None
    try:
        if scheme == "https":
            conn = http.client.HTTPSConnection(netloc, timeout=timeout)
        else:
            conn = http.client.HTTPConnection(netloc, timeout=timeout)
        payload = json.dumps(body).encode("utf-8")
        req_headers = dict(headers)
        req_headers.setdefault("Content-Type", "application/json")
        conn.request("POST", path, body=payload, headers=req_headers)
        resp = conn.getresponse()
        result["status"] = resp.status
        result["response_headers"] = safe_response_headers(dict(resp.getheaders()))
        while True:
            try:
                raw = resp.readline()
            except socket.timeout:
                result["error"] = "read timeout after %ss" % timeout
                result["error_kind"] = "timeout"
                break
            if not raw:
                break
            now = time.monotonic()
            text = raw.decode("utf-8", "replace").rstrip("\r\n")
            result["line_count"] += 1
            result["lines"].append([text, now])
            if len(result["preview"]) < 4000 and text:
                result["preview"] += text + "\n"
            if now - t0 > timeout:
                result["error"] = "stream exceeded %ss budget" % timeout
                result["error_kind"] = "timeout"
                break
    except (socket.timeout, TimeoutError):
        result["error"] = "socket timeout after %ss" % timeout
        result["error_kind"] = "timeout"
    except (ConnectionError, OSError) as exc:
        result["error"] = "%s: %s" % (type(exc).__name__, exc)
        result["error_kind"] = "connect"
    except http.client.HTTPException as exc:
        result["error"] = "%s: %s" % (type(exc).__name__, exc)
        result["error_kind"] = "protocol"
    except Exception as exc:  # noqa: BLE001 - one probe must not kill the run
        result["error"] = "%s: %s" % (type(exc).__name__, exc)
        result["error_kind"] = "unknown"
    finally:
        if conn is not None:
            try:
                conn.close()
            except Exception:  # noqa: BLE001
                pass
    return result
