#!/usr/bin/env python3
"""Build census/manifest.json: redacted machine-readable provider + model inventory.

    python3 scripts/build_manifest.py [config.toml]

Every provider is enumerated with its transport (type/protocol), base_url, auth
kind and credential *shape* (present? length? digest?) -- never the credential
value itself. Every [models.*] table is enumerated with its effective protocol
and effective base_url, since model-level `protocol` / `base_url` overrides win
over the provider's.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def provider_record(name, pcfg):
    key = pcfg.get("api_key") or ""
    rec = {
        "name": name,
        "type": pcfg.get("type", "openai"),
        "base_url": pcfg.get("base_url", ""),
        "auth": "oauth" if pcfg.get("oauth") else ("api_key" if key else "none"),
        "api_key_present": bool(key),
        "api_key_len": len(key),
        "key_digest": common.key_digest(key),
        "custom_header_names": sorted((pcfg.get("custom_headers") or {}).keys()),
    }
    if pcfg.get("oauth"):
        rec["oauth"] = {
            "storage": pcfg["oauth"].get("storage"),
            "key_ref": pcfg["oauth"].get("key"),
            "oauth_host": pcfg["oauth"].get("oauth_host"),
        }
    return rec


def model_record(mid, mcfg, providers):
    pname = mcfg.get("provider")
    pcfg = providers.get(pname, {})
    protocol = common.effective_protocol(pcfg, mcfg)
    base_url = common.effective_base_url(pcfg, mcfg)
    rec = {
        "id": mid,
        "provider": pname,
        "model": mcfg.get("model"),
        "protocol": protocol,
        "base_url": base_url,
        "base_url_overridden": bool(mcfg.get("base_url")),
        "display_name": mcfg.get("display_name"),
        "max_context_size": mcfg.get("max_context_size"),
        "max_output_size": mcfg.get("max_output_size"),
        "capabilities": mcfg.get("capabilities", []),
        "support_efforts": mcfg.get("support_efforts"),
        "default_effort": mcfg.get("default_effort"),
        "reasoning_key": mcfg.get("reasoning_key"),
    }
    if mcfg.get("overrides"):
        rec["overrides"] = mcfg["overrides"]
    return {k: v for k, v in rec.items() if v is not None}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    providers = cfg.get("providers", {})
    models = cfg.get("models", {})

    prov_records = [provider_record(n, p) for n, p in providers.items()]
    model_records = [model_record(m, c, providers) for m, c in models.items()]

    by_provider = {}
    for m in model_records:
        by_provider.setdefault(m["provider"], []).append(m["id"])
    for p in prov_records:
        p["model_count"] = len(by_provider.get(p["name"], []))
        p["distinct_served_models"] = sorted({m["model"] for m in model_records
                                              if m["provider"] == p["name"]})

    by_protocol = {}
    for m in model_records:
        by_protocol[m["protocol"]] = by_protocol.get(m["protocol"], 0) + 1

    distinct_base_urls = sorted({m["base_url"] for m in model_records})

    manifest = {
        "generated_at": subprocess.run(["date", "-Is"], capture_output=True, text=True).stdout.strip(),
        "config_path": path,
        "config_sha256_16": common.config_digest(cfg),
        "config_mtime": subprocess.run(["stat", "-c", "%y", path],
                                       capture_output=True, text=True).stdout.strip(),
        "redaction": (
            "api_key values, Authorization header values and custom-header values are "
            "NOT present in this file; only presence/length/sha256 digest are recorded"
        ),
        "default_model": cfg.get("default_model"),
        "secondary_model_default": (cfg.get("secondary_model") or {}).get("default_model"),
        "secondary_model_entry_count": len(
            (cfg.get("secondary_model") or {}).get("models") or {}),
        "totals": {
            "providers": len(prov_records),
            "model_entries": len(model_records),
            "distinct_provider_model_pairs": len({(m["provider"], m["model"]) for m in model_records}),
            "models_by_protocol": by_protocol,
            "distinct_model_base_urls": len(distinct_base_urls),
        },
        "providers": prov_records,
        "models": model_records,
    }

    out = os.path.join(common.CENSUS_DIR, "manifest.json")
    with open(out, "w") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    print("wrote %s" % out)
    print("providers=%d model_entries=%d" % (len(prov_records), len(model_records)))


if __name__ == "__main__":
    main()
