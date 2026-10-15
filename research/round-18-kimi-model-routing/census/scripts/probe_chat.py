#!/usr/bin/env python3
"""One minimal chat completion per provider (and per declared protocol), recorded.

    python3 scripts/probe_chat.py [config.toml]

Bodies are capped at 8 output tokens with temperature 0. The request shape is
chosen from the protocol the config declares for that model: openai ->
/chat/completions, anthropic -> /v1/messages, openai_responses -> /responses,
kimi -> /chat/completions. Raw captures land in raw/chat-*.json with credential
headers stripped; the `usage` block and rate-limit headers are kept verbatim
because they are the quota evidence.

Three extra probes target ids that the /models listing did NOT serve, to tell a
genuinely wrong id apart from an incomplete listing.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_models  # noqa: E402
import requests  # noqa: E402

DEFAULT_TIMEOUT_S = 60
PROVIDER_TIMEOUT_S = {"devin": 180, "cursor": 180}

UNRESOLVED_ID_PROBES = [
    ("alibaba-token-plan", "glm-5"),
    ("zai-coding-plan", "glm-5.3-highspeed"),
    ("opencode-go", "deepseek-v4-flash"),
]


def chat_url(base_url, protocol):
    if protocol == "anthropic":
        return base_url + "/v1/messages"
    if protocol == "openai_responses":
        return base_url + "/responses"
    return base_url + "/chat/completions"


def chat_body(model_id, protocol):
    if protocol == "anthropic":
        return {"model": model_id, "max_tokens": 8, "temperature": 0,
                "messages": [{"role": "user", "content": "ping"}]}
    if protocol == "openai_responses":
        return {"model": model_id, "max_output_tokens": 8, "temperature": 0,
                "input": "ping"}
    return {"model": model_id, "max_tokens": 8, "temperature": 0,
            "messages": [{"role": "user", "content": "ping"}]}


def shape(body):
    """Which response features the caller can actually rely on."""
    out = {
        "parsed_json": isinstance(body, dict),
        "reasoning_content_present": False,
        "usage_fields": [],
        "finish_reason": None,
        "content_preview": None,
        "error_type": None,
        "error_message": None,
    }
    if not isinstance(body, dict):
        out["content_preview"] = (body or "")[:200] if isinstance(body, str) else None
        return out
    if isinstance(body.get("usage"), dict):
        out["usage_fields"] = sorted(body["usage"].keys())
    err = body.get("error")
    if err is not None:
        if isinstance(err, dict):
            out["error_type"] = err.get("type") or err.get("code")
            out["error_message"] = str(err.get("message"))[:300]
        else:
            out["error_message"] = str(err)[:300]
    choices = body.get("choices")
    if isinstance(choices, list) and choices:
        c0 = choices[0] or {}
        out["finish_reason"] = c0.get("finish_reason")
        msg = c0.get("message") or {}
        if isinstance(msg, dict):
            out["reasoning_content_present"] = bool(msg.get("reasoning_content"))
            content = msg.get("content")
            if content:
                out["content_preview"] = str(content)[:200]
    for blk in (body.get("content") or []):
        if isinstance(blk, dict) and blk.get("type") == "thinking":
            out["reasoning_content_present"] = True
    for item in (body.get("output") or []):
        if isinstance(item, dict) and item.get("type") == "reasoning":
            out["reasoning_content_present"] = True
        if isinstance(item, dict) and item.get("type") == "message":
            for c in item.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "output_text":
                    out["content_preview"] = str(c.get("text"))[:200]
    return out


def probe(provider, protocol, model_id, base_url, headers, purpose, timeout):
    url = chat_url(base_url, protocol)
    record = {
        "provider": provider,
        "protocol": protocol,
        "model_id": model_id,
        "purpose": purpose,
        "method": "POST",
        "url": url,
        "timeout_s": timeout,
        "auth_headers_sent": sorted(h for h in headers if h.lower() in common.SECRET_HEADER_NAMES),
        "request_body": chat_body(model_id, protocol),
    }
    started = time.time()
    try:
        resp = requests.post(url, headers=headers, json=record["request_body"], timeout=timeout)
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = resp.status_code
        record["response_headers"] = probe_models.safe_headers(resp.headers)
        record["body"] = common.parse_body(resp.content)
    except requests.exceptions.Timeout:
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "timeout"
        record["error"] = "no response within %ds" % timeout
        record["body"] = None
    except Exception as exc:  # noqa: BLE001
        record["latency_ms"] = round((time.time() - started) * 1000)
        record["status"] = "error"
        record["error"] = "%s: %s" % (type(exc).__name__, exc)
        record["body"] = None
    record["shape"] = shape(record["body"])
    return record


def load_chat(provider):
    path = os.path.join(common.RAW_DIR, "chat-%s.json" % common.slug(provider))
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    only = [p for p in (sys.argv[2].split(",") if len(sys.argv) > 2 else []) if p]
    cfg = common.load_config(path)
    providers = cfg.get("providers", {})
    models = cfg.get("models", {})

    by_provider = {}
    for mid, mcfg in models.items():
        by_provider.setdefault(mcfg.get("provider"), []).append((mid, mcfg))

    summary = []
    for pname, pcfg in providers.items():
        if only and pname not in only:
            continue
        entries = by_provider.get(pname, [])
        if not entries:
            continue
        groups = {}
        for mid, mcfg in entries:
            groups.setdefault(common.effective_protocol(pcfg, mcfg), []).append((mid, mcfg))

        probes = []
        default_protocol = common.effective_protocol(pcfg)
        ordered = [default_protocol] + sorted(p for p in groups if p != default_protocol)
        for protocol in ordered:
            mid, mcfg = groups[protocol][0]
            headers = common.auth_headers(pcfg, protocol)
            purpose = ("provider-default-protocol" if protocol == default_protocol
                       else "declared-protocol-variant")
            probes.append(probe(pname, protocol, mcfg.get("model"),
                                common.effective_base_url(pcfg, mcfg), headers,
                                purpose, PROVIDER_TIMEOUT_S.get(pname, DEFAULT_TIMEOUT_S)))

        payload = {
            "provider": pname,
            "declared_protocols": sorted(groups),
            "model_entries": len(entries),
            "probes": probes,
        }
        common.write_json("chat-%s.json" % common.slug(pname), payload)
        for p in probes:
            print("%-24s %-18s %-28s status=%-7s %5sms reasoning=%-5s usage=%s" % (
                pname, p["protocol"], p["model_id"], p["status"], p["latency_ms"],
                p["shape"]["reasoning_content_present"], ",".join(p["shape"]["usage_fields"]) or "-"))
        summary.append({"provider": pname, "probes": probes})

    extras = []
    if not only:
        for pname, model_id in UNRESOLVED_ID_PROBES:
            pcfg = providers.get(pname)
            if pcfg is None:
                continue
            protocol = common.effective_protocol(pcfg)
            extras.append(probe(pname, protocol, model_id, common.effective_base_url(pcfg),
                                common.auth_headers(pcfg, protocol),
                                "unresolved-in-models-listing",
                                PROVIDER_TIMEOUT_S.get(pname, DEFAULT_TIMEOUT_S)))
        common.write_json("chat-unresolved-id-checks.json", {"probes": extras})
        print("--- unresolved-id checks ---")
        for p in extras:
            print("%-24s %-18s %-28s status=%-7s %5sms error=%s" % (
                p["provider"], p["protocol"], p["model_id"], p["status"], p["latency_ms"],
                p["shape"]["error_message"] or "-"))

    # Rebuild the summary from every chat-<lane>.json on disk rather than from the
    # in-memory list, so a filtered re-run of a single lane cannot truncate it.
    on_disk = []
    for pname in providers:
        data = load_chat(pname)
        if data:
            on_disk.append({"provider": pname, "probes": data.get("probes", [])})
    common.write_json("chat-summary.json", {"summary": on_disk})


if __name__ == "__main__":
    main()
