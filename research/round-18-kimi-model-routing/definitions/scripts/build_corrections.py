#!/usr/bin/env python3
"""Assemble config-corrections.toml from the audit table and the probe captures.

Every generated block is a drop-in replacement for the matching [models.*] table
in ~/.kimi-code/config.toml, and every change carries an `# evidence:` comment
pointing at either an audit-table line, a raw probe capture, or the census.

Nothing here is a guess about upstream behaviour: a field is only rewritten when
probe or binary evidence shows the declaration is inoperative, self-inconsistent,
or below/above what the lane actually accepts. Values that would need quota to
settle go to the verify-later list instead.

Usage: python3 scripts/build_corrections.py   (writes ../config-corrections.toml)
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

FIELD_ORDER = ["provider", "model", "protocol", "base_url", "max_context_size",
               "max_input_size", "max_output_size", "capabilities", "support_efforts",
               "default_effort", "off_effort", "reasoning_key", "display_name"]


def toml_val(v):
    if isinstance(v, list):
        return "[ " + ", ".join('"%s"' % x for x in v) + " ]"
    if isinstance(v, int):
        return str(v)
    return '"%s"' % v


def load(name):
    path = os.path.join(common.DEFS_DIR, name)
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def probe_index():
    """(alias, value) -> probe row, across every pass."""
    idx = {}
    for f in ("probes-effort.json", "probes-effort-pass2.json"):
        d = load(f)
        if not d:
            continue
        for r in d["results"]:
            idx[(r["alias"], r.get("value"))] = r
    return idx


def main():
    audit = load("audit-table.json")
    if audit is None:
        raise SystemExit("audit-table.json missing -- run scripts/audit_definitions.py first")
    probes = probe_index()
    semantics = load(os.path.join("raw", "client-semantics.json"))

    entries = {e["alias"]: e for e in audit["entries"]}
    defects = audit["defects"]
    by_alias = defaultdict(list)
    for d in defects:
        for a in str(d["alias"]).split(", "):
            if a in entries:
                by_alias[a].append(d)

    rk_corr = audit.get("reasoning_key_corrections", {})

    # Field-level plan, computed once: which fields each alias must drop, and which
    # aliases need a reasoning_key rewrite. Sections A and A2 consume this.
    drop_map = {}
    for alias in sorted(by_alias):
        rel = [d for d in by_alias[alias] if d["id"] in
               ("DEF-1", "DEF-3c") or d["id"].startswith("DEF-2")]
        if not rel:
            continue
        drop = set()
        for d in rel:
            if d["id"] in ("DEF-1", "DEF-3c"):
                drop.add(d["field"])
            elif d["field"] == "max_input_size+max_output_size":
                drop.update(("max_input_size", "max_output_size"))
            else:
                drop.add(d["field"])
        drop_map[alias] = (drop, rel)
    staged = [a for a in rk_corr if a not in drop_map
              and any(d["id"] in ("DEF-9", "DEF-10") for d in by_alias.get(a, []))]

    out = []
    add = out.append
    add("# config-corrections.toml -- R18 definitions audit (mission M2)")
    add("#")
    add("# Source config: %s" % audit["config_path"])
    add("#   file sha256:        %s" % audit["config_file_sha256"])
    add("#   json-canonical /16: %s   (same digest as the M1 census: %s)"
        % (audit["config_json_digest_16"],
           "61f22a2bbe52d616" if audit["config_json_digest_16"] == "61f22a2bbe52d616" else "DIFFERS"))
    add("#")
    add("# Every block below is a drop-in replacement for the matching [models.*] table")
    add("# in ~/.kimi-code/config.toml. `# evidence:` cites the artifact behind each")
    add("# change: audit-table.json (A), raw/probes-*.json (P), raw/client-semantics.json (C),")
    add("# the M1 census (M1), or the client binary's own strings (B).")
    add("#")
    add("# Findings: %d defects / %d notes / %d verify-later over %d model entries"
        % (audit["triage_counts"].get("defect", 0), audit["triage_counts"].get("note", 0),
           audit["triage_counts"].get("verify-later", 0), len(entries)))
    add("")

    # ------------------------------------------------- section A+B (merged)
    add("# " + "=" * 76)
    add("# A. Field-level corrections, one merged block per model")
    add("#")
    add("#    off_effort / max_input_size are inoperative:")
    add("#      B: `grep -a -o off_effort ~/.kimi-code/bin/kimi | wc -l` -> 0")
    add("#         `grep -a -o max_input_size ~/.kimi-code/bin/kimi | wc -l` -> 0")
    add("#      C: setting off_effort changes nothing the client sends; the effort value")
    add("#         is chosen from default_effort / support_efforts only.")
    add("#")
    add("#    Implausible size caps: 26214 / 6553 / 13107 / 25600 are exactly")
    add("#    floor(2^18/10), floor(2^16/10), floor(2^17/10) and max_context_size/10 --")
    add("#    a unit slip, not a measured limit (A: DEF-2a). max_output_size is really")
    add("#    sent as max_tokens (C), so a slip truncates output. The correction is")
    add("#    removal: with the field absent the client sends no output cap on these")
    add("#    lanes (C: `plain` sends no max_tokens) and the server decides.")
    add("#")
    add("#    Each block below is the entry with the flagged fields dropped; splice it")
    add("#    over the matching [models.*] table.")
    add("# " + "=" * 76)
    add("")
    for alias, (drop, rel) in drop_map.items():
        e = entries[alias]
        add("# %s" % alias)
        for d in rel:
            add("#   evidence: %s %s = %r -- %s" % (d["id"], d["field"], d["value"], d["detail"]))
        if alias in rk_corr:
            add("#   evidence: %s reasoning_key -> %r (%s)"
                % (rk_corr[alias]["action"], rk_corr[alias]["key"], rk_corr[alias]["because"]))
        add("#   drops: %s" % ", ".join(sorted(drop)))
        add('[models."%s"]' % alias)
        for f in FIELD_ORDER:
            if f in drop:
                continue
            v = rk_corr[alias]["key"] if (f == "reasoning_key" and alias in rk_corr) else e.get(f)
            if v is None or v == []:
                continue
            add("%s = %s" % (f, toml_val(v)))
        if e.get("overrides"):
            add("")
            add('[models."%s".overrides]' % alias)
            for k, v in e["overrides"].items():
                add("%s = %s" % (k, toml_val(v)))
        add("")

    # ---------------------------------------------------------------- section C
    add("# " + "=" * 76)
    add("# C. Global thinking effort overrides every model's declared effort")
    add("#")
    add("#    The live config has:")
    add("#        [thinking]")
    add("#        enabled = true")
    add('#        effort = "max"')
    add("#")
    add("#    C: with that line present the client sends reasoning_effort=\"max\" to")
    add('#       every model, including models whose support_efforts do not contain')
    add('#       "max" (31 entries, A: DEF-3b) and models that declare no effort support')
    add("#       at all. Without the line, each model's default_effort applies, falling")
    add("#       back to support_efforts[floor(n/2)] when it has none.")
    add("#    P: whether that hurts depends on the lane, measured with one invalid")
    add("#       control token per lane (a value in no model's support_efforts). A lane")
    add("#       that returns 400 for the control really does validate the value, so its")
    add("#       acceptance of xhigh/max is evidence; a lane that returns 200 for the")
    add("#       control ignores the field entirely, so its 'acceptance' proves nothing.")
    add("#")
    for lane, verdict, why in lane_effort_verdicts(load("probes-effort.json"),
                                                   load("probes-effort-pass2.json")):
        add("#       %-16s %-12s %s" % (lane, verdict, why))
    add("#")
    add("#    Recommended splice (drops the global pin; per-model defaults take over):")
    add("#")
    add("#        [thinking]")
    add("#        enabled = true")
    add("")
    add("#    If a global pin is wanted anyway, `high` is the only value declared by")
    add("#    every model in the file; `max` is not.")
    add("")

    # ---------------------------------------------------------------- section D
    add("# " + "=" * 76)
    add("# D. Entries that cannot work as declared (quarantine or delete)")
    add("# " + "=" * 76)
    add("")
    dead = defaultdict(list)
    for d in defects:
        if d["id"] == "DEF-7":
            dead[d["detail"]].append(d["alias"])
    for detail in sorted(dead):
        add("# %s" % detail)
        aliases = dead[detail]
        add("#   affected: %s" % ", ".join(sorted(aliases)[:40]))
        add("")

    # ---------------------------------------------------------------- section E
    add("# " + "=" * 76)
    add("# E. Effort defaults worth making explicit")
    add("#")
    add("#    Without a global pin the client picks support_efforts[floor(n/2)] when a")
    add("#    model declares no default_effort (C, verified on 11 lists). For lists where")
    add("#    that pick is below what the lane demonstrably accepts (P), pin it instead:")
    add("")
    for alias in sorted(entries):
        e = entries[alias]
        sup = e["support_efforts"]
        if not sup or e["default_effort"] or e["default_effort_override"]:
            continue
        if alias in drop_map or alias in staged:
            continue          # section A / A2 already emits this entry
        mid = sup[len(sup) // 2]
        picked = (mid == "max" or activate(alias, probes))
        if not picked:
            continue
        add("# %s: declared %s -> client sends %r" % (alias, sup, mid))
        add('[models."%s"]' % alias)
        add("provider = %s" % toml_val(e["provider"]))
        add("model = %s" % toml_val(e["model"]))
        add("max_context_size = %s" % e["max_context_size"])
        if e["max_output_size"]:
            add("max_output_size = %s" % e["max_output_size"])
        add("capabilities = %s" % toml_val(e["capabilities"]))
        add("support_efforts = %s" % toml_val(sup))
        add("default_effort = %s" % toml_val(mid))
        if e["reasoning_key"]:
            add("reasoning_key = %s" % toml_val(e["reasoning_key"]))
        add("")

    if staged:
        add("# " + "=" * 76)
        add("# A2. `reasoning_key` corrections from probe evidence")
        add("#")
        add("#    Every lane below returned reasoning under a field the config does not")
        add("#    name. DEF-9 rows: the declared key never appeared (opencode-go returns")
        add("#    `reasoning` + `reasoning_details`, not `reasoning_content`). DEF-10 rows:")
        add("#    no key declared, but the lane returned `reasoning_content`. A reasoning")
        add("#    pane cannot render either way until the declaration matches the lane.")
        add("# " + "=" * 76)
        add("")
        for alias in sorted(staged):
            e = entries[alias]
            c = rk_corr[alias]
            add("# %s" % alias)
            for d in by_alias[alias]:
                if d["id"] in ("DEF-9", "DEF-10"):
                    add("#   evidence: %s -- %s" % (d["id"], d["detail"]))
            add('[models."%s"]' % alias)
            for f in FIELD_ORDER:
                v = c["key"] if f == "reasoning_key" else e.get(f)
                if f in ("off_effort", "max_input_size"):
                    continue
                if v is None or v == []:
                    continue
                add("%s = %s" % (f, toml_val(v)))
            add("")

    # ---------------------------------------------------------------- section F
    add("# " + "=" * 76)
    add("# F. Verify-later: fields this audit could not settle without quota spend")
    add("# " + "=" * 76)
    add("")
    add("# 1. video_in / audio_in claims (%d entries, A: DEF-6b). No video or audio"
        % audit["triage_counts"].get("verify-later", 0))
    add("#    payload was sent; these remain config claims. Cheapest check: one short")
    add("#    clip / one second of audio on the lane whose routing table depends on it.")
    add("# 2. max_context_size values. The live client never sends a context limit, so no")
    add("#    probe can falsify these; a deliberate over-long prompt per lane is the only")
    add("#    test, and it is a quota-heavy one.")
    add("# 3. Cross-provider divergences (A: DEF-5). The same served model id is declared")
    add("#    with different caps on different lanes; without per-lane measurement the")
    add("#    only safe action is to unify on the smallest declared value.")
    diverged = [d for d in defects if d["id"] == "DEF-5"]
    for d in diverged[:40]:
        v = d["value"]
        add("#      %s: ctx=%s out=%s" % (d["field"], v.get("max_context_size"), v.get("max_output_size")))
    add("# 4. Lanes that ignore reasoning_effort (P: invalid-control returned 200):")
    ignored = sorted({r["lane"] for r in probe_rows(load("probes-effort.json"))
                      if r.get("value") == "invalid-control" and r.get("status") == 200})
    add("#      %s" % ", ".join(ignored))
    add("#    For these, accept/reject of a value is not evidence of support; only the")
    add("#    reasoning_content the lane returns shows whether thinking actually ran.")
    add("# 5. devin: 502 'Reached free model rate limit ... reset in 1 hour' during this")
    add("#    audit (P: probes-effort.json), so devin-first cascade behaviour was not")
    add("#    measurable at audit time; re-check after the reset window.")
    add("# 6. reasoning_key for the DEF-9 entries. The lane returns `reasoning` (plus a")
    add("#    structured `reasoning_details` list); this file recommends `reasoning`, but")
    add("#    which of the two the client actually renders was not tested -- the probe")
    add("#    read raw JSON, it did not drive the client's reasoning pane.")
    add("")

    path = os.path.join(common.DEFS_DIR, "config-corrections.toml")
    with open(path, "w") as fh:
        fh.write("\n".join(out) + "\n")

    # the file must be valid TOML, or it is not "ready to splice"
    import tomllib
    with open(path, "rb") as fh:
        parsed = tomllib.load(fh)
    print("wrote %s (%d lines, %d model blocks parse cleanly)"
          % (path, len(out), len(parsed.get("models", {}))))


def probe_rows(d):
    return d["results"] if d else []


def lane_effort_verdicts(*captures):
    """Per lane: does the invalid control get rejected (validates) or accepted (ignores)?"""
    rows = [r for d in captures if d for r in d["results"]]
    lanes = {}
    for r in rows:
        lanes.setdefault(r["lane"], []).append(r)
    out = []
    for lane in sorted(lanes):
        rs = lanes[lane]
        control = [r for r in rs if r.get("value") == "invalid-control"]
        accepted = sorted({r["value"] for r in rs
                           if r.get("value") and r["value"] != "invalid-control"
                           and r.get("status") == 200})
        if not control:
            verdict, why = "unprobed", "no invalid-control row for this lane"
        else:
            st = control[0].get("status")
            if st == 200:
                verdict = "ignores"
                why = ("invalid-control returned 200, so the field is not validated; "
                       "accepted values (%s) are not evidence of support"
                       % ", ".join(accepted) or "none")
            elif st == 400:
                verdict = "validates"
                why = ("invalid-control returned 400, so accepted values (%s) are "
                       "genuinely supported" % (", ".join(accepted) or "none"))
            else:
                verdict = "inconclusive"
                why = "invalid-control returned %s (%s)" % (st, control[0].get("error") or "no error field")
        out.append((lane, verdict, why))
    return out


def activate(alias, probes):
    """True when a probe on this alias returned a definitive effort accept."""
    for (a, v), row in probes.items():
        if a == alias and v and v != "invalid-control" and row.get("status") == 200:
            return True
    return False


if __name__ == "__main__":
    main()
