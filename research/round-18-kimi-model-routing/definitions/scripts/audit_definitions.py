#!/usr/bin/env python3
"""Build the R18 definitions audit table and the config-only defect classes.

Reads ~/.kimi-code/config.toml, emits:
  audit-table.json  -- machine-readable table over every [models.*] entry
  audit-table.md    -- the same table as markdown, grouped by provider

Everything here is derived from the config itself; defects that need probe
evidence are attached by scripts/build_analysis.py from raw/probes-*.json.
"""
import json
import os
import sys
import time
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# Field names to count in the client binary, and the ONE method used for every
# row. An earlier revision of this table mixed `grep -c -o` (which counts
# matching *lines*, not matches) with `grep -o | wc -l`, and one row (`protocol`)
# was never measured at all; the table now computes every row with the command
# below, which is the one stated in ANALYSIS.md section 1.
BINARY_PATH = os.path.expanduser("~/.kimi-code/bin/kimi")
BINARY_FIELDS = ["max_context_size", "max_output_size", "max_input_size",
                 "support_efforts", "default_effort", "off_effort", "reasoning_key",
                 "capabilities", "display_name", "protocol", "overrides"]
BINARY_COUNT_METHOD = "grep -a -o '<field>' %s | wc -l" % BINARY_PATH


def binary_field_hits(path=BINARY_PATH):
    """Occurrence count per field name, all rows by one method (BINARY_COUNT_METHOD).

    The count is the number of times the byte string occurs anywhere in the
    binary, so a nonzero row means "this name exists in the client", not "this
    many declarations" -- occurrences inside longer identifiers are included.
    The load-bearing reading is zero vs nonzero.
    """
    import subprocess
    out = {}
    for field in BINARY_FIELDS:
        try:
            proc = subprocess.run(["grep", "-a", "-o", field, path],
                                  stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            out[field] = proc.stdout.count(b"\n")
        except OSError:
            out[field] = None
    return out


def binary_identity(path=BINARY_PATH):
    import hashlib
    try:
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        stat = os.stat(path)
        return {"path": path, "sha256": digest, "size": stat.st_size,
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(stat.st_mtime))}
    except OSError:
        return {"path": path, "sha256": None, "size": None, "mtime": None}

MODEL_FIELDS = ["provider", "model", "protocol", "base_url", "max_context_size",
                "max_input_size", "max_output_size", "capabilities",
                "support_efforts", "default_effort", "off_effort", "reasoning_key",
                "display_name"]

# floor(2^k / 10) for k in 10..30: the exact values a "10x unit slip" produces.
APPROX_TENTH = {2 ** k // 10: 2 ** k for k in range(10, 31)}

# defect = wrong or inoperative declaration worth correcting
# note   = true behaviour worth recording, not itself wrong
# verify-later = real-world claim this audit could not spend quota to settle
TRIAGE = {
    "DEF-1": "defect",
    "DEF-2a": "defect",
    "DEF-2b": "defect",
    "DEF-2c": "defect",
    "DEF-2d": "defect",
    "DEF-2e": "defect",
    "DEF-2f": "defect",
    "DEF-3a": "defect",
    "DEF-3b": "defect",
    "DEF-3c": "defect",
    "DEF-3d": "note",
    "DEF-4a": "defect",
    "DEF-4b": "note",
    "DEF-5": "defect",
    "DEF-6a": "note",
    "DEF-6b": "verify-later",
    "DEF-7": "defect",
    "DEF-8": "note",
}


def flatten(alias, pid, pc, mc):
    overrides = mc.get("overrides") or {}
    return {
        "alias": alias,
        "provider": pid,
        "provider_type": pc.get("type"),
        "model": mc.get("model"),
        "protocol": common.effective_protocol(pc, mc),
        "protocol_source": "model" if mc.get("protocol") else "provider",
        "base_url": common.effective_base_url(pc, mc),
        "base_url_source": "model" if mc.get("base_url") else "provider",
        "provider_base_url": (pc.get("base_url") or "").rstrip("/"),
        "max_context_size": mc.get("max_context_size"),
        "max_input_size": mc.get("max_input_size"),
        "max_output_size": mc.get("max_output_size"),
        "capabilities": list(mc.get("capabilities") or []),
        "support_efforts": list(mc.get("support_efforts") or []),
        "default_effort": mc.get("default_effort"),
        "default_effort_override": overrides.get("default_effort"),
        "off_effort": mc.get("off_effort"),
        "reasoning_key": mc.get("reasoning_key"),
        "display_name": mc.get("display_name"),
        "has_overrides_table": bool(overrides),
        "unknown_fields": sorted(set(mc) - set(MODEL_FIELDS) - {"overrides"}),
    }


def detect_defects(entries, cfg):
    defects = []
    global_effort = (cfg.get("thinking") or {}).get("effort")

    # --- D1  unregistered fields -------------------------------------------
    for e in entries:
        for f in ("off_effort", "max_input_size"):
            if e.get(f) is not None:
                defects.append({
                    "id": "DEF-1", "class": "unregistered field",
                    "alias": e["alias"], "field": f, "value": e[f],
                    "evidence": ["binary_field_hits", "client_wire_capture"],
                    "detail": ("`%s` appears 0 times in the client binary and the "
                               "client's own request body is unchanged when it is set "
                               "(mock capture, ANALYSIS section 3)." % f),
                })

    # --- D2  implausible numeric caps --------------------------------------
    for e in entries:
        ctx, out, inp = e["max_context_size"], e["max_output_size"], e["max_input_size"]
        if ctx and out and out == ctx // 10:
            defects.append({"id": "DEF-2a", "class": "formula-derived cap",
                            "alias": e["alias"], "field": "max_output_size",
                            "value": out,
                            "detail": "equals floor(max_context_size/10) = floor(%d/10); looks generated, not measured" % ctx,
                            "evidence": ["config"]})
        if out in APPROX_TENTH and out != ctx:
            defects.append({"id": "DEF-2a", "class": "formula-derived cap",
                            "alias": e["alias"], "field": "max_output_size",
                            "value": out,
                            "detail": ("equals floor(2^%d/10) = %d -- a decimal/binary unit slip, "
                                       "not a measured cap (declared max_context_size is %s)"
                                       % (APPROX_TENTH[out].bit_length() - 1, APPROX_TENTH[out], ctx)),
                            "evidence": ["config"]})
        if ctx and out and out >= ctx:
            defects.append({"id": "DEF-2b", "class": "cap inconsistency",
                            "alias": e["alias"], "field": "max_output_size",
                            "value": out,
                            "detail": "max_output_size >= max_context_size (%d >= %d)" % (out, ctx),
                            "evidence": ["config"]})
        if ctx and inp and inp + (out or 0) > ctx:
            defects.append({"id": "DEF-2c", "class": "cap inconsistency",
                            "alias": e["alias"], "field": "max_input_size+max_output_size",
                            "value": [inp, out],
                            "detail": "max_input_size + max_output_size = %d > max_context_size %d"
                                      % (inp + (out or 0), ctx),
                            "evidence": ["config"]})
        if ctx and inp and inp == ctx and out:
            defects.append({"id": "DEF-2d", "class": "cap inconsistency",
                            "alias": e["alias"], "field": "max_input_size",
                            "value": inp,
                            "detail": "max_input_size == max_context_size, leaving no room for output",
                            "evidence": ["config"]})
        if ctx is None and inp is None and out is None:
            defects.append({"id": "DEF-2e", "class": "missing limits",
                            "alias": e["alias"], "field": "max_context_size",
                            "value": None,
                            "detail": "no size fields declared at all",
                            "evidence": ["config"]})
        if ctx and not out and e["provider_type"] == "kimi":
            defects.append({"id": "DEF-2f", "class": "missing output cap",
                            "alias": e["alias"], "field": "max_output_size",
                            "value": None,
                            "detail": ("kimi-protocol lane: with no max_output_size the client "
                                       "sends max_completion_tokens = max_context_size - 193 "
                                       "(mock capture, ANALYSIS section 3)"),
                            "evidence": ["config", "client_wire_capture"]})

    # --- D3  effort declarations ------------------------------------------
    for e in entries:
        sup, de, ov, off = e["support_efforts"], e["default_effort"], \
            e["default_effort_override"], e["off_effort"]
        eff_default = ov or de
        if eff_default and sup and eff_default not in sup:
            defects.append({"id": "DEF-3a", "class": "effort not declared",
                            "alias": e["alias"], "field": "default_effort",
                            "value": eff_default,
                            "detail": "default_effort %r is not in support_efforts %s" % (eff_default, sup),
                            "evidence": ["config"]})
        if global_effort and sup and global_effort not in sup:
            defects.append({"id": "DEF-3b", "class": "global effort overrides model",
                            "alias": e["alias"], "field": "support_efforts",
                            "value": sup,
                            "detail": ("global [thinking] effort=%r is sent as-is even though "
                                       "the model declares %s (mock capture, ANALYSIS section 3)"
                                       % (global_effort, sup)),
                            "evidence": ["config", "client_wire_capture"]})
        if off is not None:
            defects.append({"id": "DEF-3c", "class": "unregistered field",
                            "alias": e["alias"], "field": "off_effort", "value": off,
                            "detail": "inert: no wire effect observed, 0 binary hits",
                            "evidence": ["client_wire_capture", "binary_field_hits"]})
        if sup and not eff_default:
            defects.append({"id": "DEF-3d", "class": "effort fallback",
                            "alias": e["alias"], "field": "default_effort", "value": None,
                            "detail": ("no default_effort: client picks support_efforts[floor(n/2)] "
                                       "= %r (mock capture)" % sup[len(sup) // 2]),
                            "evidence": ["config", "client_wire_capture"]})

    # --- D4  protocol / base_url ------------------------------------------
    for e in entries:
        if e["base_url_source"] == "model" and e["base_url"] != e["provider_base_url"]:
            if not e["base_url"].endswith("/v1") and e["protocol"] != "anthropic":
                defects.append({"id": "DEF-4a", "class": "base_url mismatch",
                                "alias": e["alias"], "field": "base_url",
                                "value": e["base_url"],
                                "detail": ("model-level base_url differs from the provider's and does "
                                           "not end in /v1 while protocol=%s" % e["protocol"]),
                                "evidence": ["config", "census D8"]})
        if e["protocol"] == "anthropic" and not e["base_url"].endswith("/v1"):
            defects.append({"id": "DEF-4b", "class": "base_url doc trap",
                            "alias": e["alias"], "field": "base_url",
                            "value": e["base_url"],
                            "detail": ("anthropic protocol posts to {base_url}/v1/messages, so the "
                                       "override is correct for chat but {base_url}/models 404s "
                                       "(census D8)"),
                            "evidence": ["config", "census D8"]})

    # --- D5  duplicate model ids with divergent declarations --------------
    by_model = defaultdict(list)
    for e in entries:
        by_model[e["model"]].append(e)
    for model_id, group in sorted(by_model.items()):
        if len(group) < 2:
            continue
        caps = {tuple(sorted(g["capabilities"])) for g in group}
        outs = {g["max_output_size"] for g in group}
        ctxs = {g["max_context_size"] for g in group}
        protos = {g["protocol"] for g in group}
        if len(caps) > 1 or len(outs) > 1 or len(ctxs) > 1 or len(protos) > 1:
            defects.append({
                "id": "DEF-5", "class": "cross-provider divergence",
                "alias": ", ".join(sorted(g["alias"] for g in group)),
                "field": "model=%s" % model_id,
                "value": {"max_context_size": sorted(x for x in ctxs if x),
                          "max_output_size": sorted(x for x in outs if x),
                          "protocols": sorted(protos),
                          "capability_sets": sorted("+".join(c) for c in caps)},
                "detail": ("the same served model id is declared %d times with different "
                           "limits, protocols or capabilities across providers" % len(group)),
                "evidence": ["config"]})

    # --- D6  capability claims -------------------------------------------
    for e in entries:
        if "tool_use" not in e["capabilities"]:
            defects.append({"id": "DEF-6a", "class": "capability claim",
                            "alias": e["alias"], "field": "capabilities",
                            "value": e["capabilities"],
                            "detail": ("tool_use not declared, but the client sends the tool array "
                                       "regardless of this capability (mock capture) -- only "
                                       "image_in/video_in change the payload"),
                            "evidence": ["config", "client_wire_capture"]})
        for cap in ("audio_in", "video_in"):
            if cap in e["capabilities"]:
                defects.append({"id": "DEF-6b", "class": "unverified capability",
                                "alias": e["alias"], "field": "capabilities", "value": cap,
                                "detail": "%s declared; no payload of that kind was sent (verify-later)" % cap,
                                "evidence": ["config"]})

    # --- D7  unentitled / dead ids from the census -----------------------
    census_dead = {
        "alibaba-token-plan/glm-5": "403 access denied (census D3)",
        "alibaba-token-plan-2/glm-5": "403 access denied (census D3)",
        "alibaba-token-plan-3/glm-5": "403 access denied (census D3)",
        "zai-coding-plan/glm-5.3-highspeed": "429 plan does not include it (census D3)",
    }
    for alias, why in census_dead.items():
        if alias in cfg.get("models", {}):
            defects.append({"id": "DEF-7", "class": "unentitled id",
                            "alias": alias, "field": "model",
                            "value": cfg["models"][alias].get("model"),
                            "detail": why, "evidence": ["census D3"]})
    # lanes that are dead wholesale
    for lane, why in (("managed:kimi-code", "401: OAuth store 0 bytes (census D1)"),
                      ("alibaba-token-plan-2", "429 quota exhausted (census D2)"),
                      ("alibaba-token-plan-3", "429 quota exhausted (census D2)")):
        n = sum(1 for e in entries if e["provider"] == lane)
        defects.append({"id": "DEF-7", "class": "dead lane", "alias": lane,
                        "field": "provider", "value": n, "detail": why,
                        "evidence": ["census D1/D2"]})

    # --- D8  alias / duplicate-alias hygiene ------------------------------
    pair_counts = Counter((e["provider"], e["model"]) for e in entries)
    for (pid, mid), n in sorted(pair_counts.items()):
        if n > 1:
            aliases = sorted(e["alias"] for e in entries if e["provider"] == pid and e["model"] == mid)
            with_ov = [e["alias"] for e in entries
                       if e["provider"] == pid and e["model"] == mid and e["has_overrides_table"]]
            defects.append({"id": "DEF-8", "class": "duplicate alias pair",
                            "alias": ", ".join(aliases), "field": "provider+model",
                            "value": "%s/%s x%d" % (pid, mid, n),
                            "detail": ("same provider+model served by %d aliases; override-pinned: %s"
                                       % (n, with_ov or "none")),
                            "evidence": ["config"]})
    return defects


def main():
    cfg = common.load_config()
    raw = cfg.get("models", {})
    entries = [flatten(a, mc.get("provider"), cfg["providers"].get(mc.get("provider"), {}), mc)
               for a, mc in raw.items()]
    defects = detect_defects(entries, cfg)
    hits = binary_field_hits()

    payload = {
        "config_path": common.CONFIG_PATH,
        "config_file_sha256": common.config_file_digest(),
        "config_json_digest_16": common.config_digest(cfg),
        "counts": {
            "providers": len(cfg.get("providers", {})),
            "model_entries": len(entries),
            "distinct_provider_model_pairs": len({(e["provider"], e["model"]) for e in entries}),
            "entries_with_off_effort": sum(1 for e in entries if e["off_effort"] is not None),
            "entries_with_max_input_size": sum(1 for e in entries if e["max_input_size"] is not None),
            "entries_without_max_output_size": sum(1 for e in entries if e["max_output_size"] is None),
            "global_thinking_effort": (cfg.get("thinking") or {}).get("effort"),
        },
        "binary_field_hits": hits,
        "binary_count_method": BINARY_COUNT_METHOD,
        "binary_identity": binary_identity(),
        "effort_values_declared": sorted({v for e in entries for v in e["support_efforts"]}),
        "off_effort_values": sorted({e["off_effort"] for e in entries if e["off_effort"]}),
        "default_effort_values": sorted({x for e in entries
                                         for x in (e["default_effort"], e["default_effort_override"])
                                         if x}),
        "entries": entries,
        "defects": defects,
        "triage_counts": dict(Counter(TRIAGE.get(d["id"], "note") for d in defects)),
    }

    # markdown view
    lines = ["# config audit table", "",
             "Config: `%s`  " % common.CONFIG_PATH,
             "file sha256 `%s`  " % payload["config_file_sha256"],
             "json-canonical digest/16 `%s`" % payload["config_json_digest_16"], "",
             "| # | alias | provider | proto | model | ctx | in | out | caps | efforts | dflt | off | rkey |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    last_provider = None
    for i, e in enumerate(entries, 1):
        if e["provider"] != last_provider:
            lines.append("| | **%s** (%s) | | | | | | | | | | | |"
                         % (e["provider"], e["provider_type"]))
            last_provider = e["provider"]
        eff = "%s" % ("+".join(x[:4] for x in e["support_efforts"]) or "-")
        dflt = e["default_effort_override"] or e["default_effort"] or "-"
        if e["default_effort_override"]:
            dflt += "*"
        lines.append("| %d | `%s` | %s | %s | `%s` | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            i, e["alias"], e["provider"], e["protocol"], e["model"],
            e["max_context_size"] or "-", e["max_input_size"] or "-",
            e["max_output_size"] or "-",
            "+".join(c[:12] for c in e["capabilities"]) or "-",
            eff, dflt, e["off_effort"] or "-", e["reasoning_key"] or "-"))
    lines += ["", "`*` = pinned via `[models.<alias>.overrides]`.", ""]
    with open(os.path.join(common.DEFS_DIR, "audit-table.md"), "w") as fh:
        fh.write("\n".join(lines))

    counts = Counter(d["id"] for d in defects)
    tri = Counter(TRIAGE.get(d["id"], "note") for d in defects)
    # apply triage to the in-memory copies already written above in the same order
    for d in defects:
        d["triage"] = TRIAGE.get(d["id"], "note")
    with open(os.path.join(common.DEFS_DIR, "audit-table.json"), "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print("entries:", len(entries), "findings:", len(defects), "triage:", dict(tri))
    for k, v in sorted(counts.items()):
        print("  %-6s %-11s %d" % (k, TRIAGE.get(k, "note"), v))


if __name__ == "__main__":
    main()
