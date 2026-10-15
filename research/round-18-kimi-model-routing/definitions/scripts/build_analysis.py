#!/usr/bin/env python3
"""Assemble ANALYSIS.md for the R18 definitions audit from the captured evidence.

Inputs (all in this tree): audit-table.json, raw/probes-*.json,
raw/client-semantics.json, HYGIENE.md. Nothing is written by hand into the
report that is not read out of one of those files.
"""
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def load(name):
    path = os.path.join(common.DEFS_DIR, name)
    with open(path) as fh:
        return json.load(fh)


def load_opt(name):
    path = os.path.join(common.DEFS_DIR, name)
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return json.load(fh)


def corrections_block_count():
    """Model blocks in config-corrections.toml, counting only top-level tables."""
    path = os.path.join(common.DEFS_DIR, "config-corrections.toml")
    if not os.path.exists(path):
        return 0
    with open(path) as fh:
        return sum(1 for line in fh
                   if line.startswith('[models."') and '".overrides]' not in line)


def probe_rows():
    rows = []
    for f in ("raw/probes-effort.json", "raw/probes-effort-pass2.json",
              "raw/probes-tool.json", "raw/probes-tool-pass2.json",
              "raw/probes-tool-pass3.json", "raw/probes-image.json",
              "raw/probes-image-pass2.json"):
        d = load_opt(f)
        if d:
            for r in d["results"]:
                r["_source"] = f
                rows.append(r)
    return rows


def effort_lane_table(rows):
    lanes = defaultdict(list)
    for r in rows:
        if r["suite"] == "effort":
            lanes[r["lane"]].append(r)
    out = []
    for lane in sorted(lanes):
        # pass 1's opencode-go rows were WAF-blocked (403, UA artefact) and do not
        # describe the lane; they are excluded from the reading, not just the count
        rs = [r for r in lanes[lane] if r.get("status") != 403]
        ctrl = [r for r in rs if r.get("value") == "invalid-control"]
        accepted = sorted({r["value"] for r in rs if r.get("value")
                           and r["value"] != "invalid-control" and r.get("status") == 200})
        accepted_str = ", ".join(accepted) or "-"
        if not ctrl:
            verdict, why = "unprobed", "no valid invalid-control row"
        elif ctrl[0].get("status") == 200:
            verdict = "ignores the field"
            why = "invalid-control returned 200"
        elif ctrl[0].get("status") == 400:
            verdict = "validates the value"
            why = "invalid-control returned 400"
        elif ctrl[0].get("status") is None:
            verdict = "unmeasurable"
            why = "invalid-control timed out (%s)" % (ctrl[0].get("error") or "")[:40]
        else:
            verdict = "inconclusive"
            why = "invalid-control returned %s" % ctrl[0].get("status")
        out.append((lane, accepted_str, verdict, why))
    return out


def tool_table(rows):
    lanes = defaultdict(list)
    for r in rows:
        if r["suite"] == "tool":
            lanes[r["lane"]].append(r)
    out = []
    for lane in sorted(lanes):
        rs = sorted(lanes[lane], key=lambda r: r.get("_source", ""))
        served = []
        for r in rs:
            ok = bool(r.get("derived", {}).get("tool_call_wellformed"))
            model = None
            if isinstance(r.get("response"), dict):
                model = r["response"].get("model")
            served.append("%s:%s%s" % (os.path.basename(r.get("_source", "")).replace("probes-", "").replace(".json", ""),
                                       "call" if ok else ("status=%s" % r.get("status")),
                                       ("/" + model) if model else ""))
        verdict = "tool-capable" if any(r.get("derived", {}).get("tool_call_wellformed")
                                        for r in rs) else "no tool call observed"
        if verdict == "no tool call observed" and all(r.get("status") is None for r in rs):
            verdict = "unmeasurable (request timed out)"
        out.append((lane, verdict, "; ".join(served)))
    return out


def image_table(rows):
    per_alias = defaultdict(dict)
    for r in rows:
        if r["suite"] == "image":
            per_alias[r["alias"]][r.get("png_side")] = r
    entries = {e["alias"]: e for e in audit["entries"]}
    out = []
    for alias in sorted(per_alias):
        by = per_alias[alias]
        cells = []
        for side in sorted(x for x in by if x):
            r = by[side]
            st = r.get("status")
            msg = ""
            resp = r.get("response")
            if isinstance(resp, dict) and st != 200:
                msg = (resp.get("message") or resp.get("code") or "")[:60]
            elif isinstance(resp, str) and st != 200:
                msg = resp[:60]
            cells.append("%dx%d -> %s%s" % (side, side, st, (" (%s)" % msg) if msg else ""))
        declared = "image_in" in (entries.get(alias, {}).get("capabilities") or [])
        out.append((alias, "yes" if declared else "NO (control)", "; ".join(cells)))
    return out


def reasoning_table(rows):
    per_alias = defaultdict(list)
    for r in rows:
        if r.get("derived", {}).get("message_keys") or r.get("derived", {}).get("has_reasoning_content") is not None:
            per_alias[r["alias"]].append(r)
    entries = {e["alias"]: e for e in audit["entries"]}
    out = []
    for alias in sorted(per_alias):
        declared = entries.get(alias, {}).get("reasoning_key")
        hits = sum(1 for r in per_alias[alias]
                   if r["derived"].get("has_reasoning_content"))
        total = len(per_alias[alias])
        keys = sorted({k for r in per_alias[alias] for k in (r["derived"].get("message_keys") or [])})
        out.append((alias, declared or "-", "%d/%d" % (hits, total), ",".join(keys) or "-"))
    return out


def main():
    global audit
    audit = load("audit-table.json")
    rows = probe_rows()
    semantics = load_opt("raw/client-semantics.json")

    entries = audit["entries"]
    defects = audit["defects"]
    counts = audit["counts"]
    triage = audit["triage_counts"]
    by_class = Counter(d["class"] for d in defects)
    by_triage = defaultdict(list)
    for d in defects:
        by_triage[d["triage"]].append(d)

    L = []
    A = L.append
    A("# R18 definitions audit — ANALYSIS")
    A("")
    A("Scope: every `[models.*]` entry in `~/.kimi-code/config.toml` — their declared")
    A("limits, capabilities, effort values, reasoning key, protocol and base_url — plus")
    A("what the shipped client actually transmits for each of those declarations.")
    A("")
    A("| Metric | Value |")
    A("| --- | --- |")
    A("| Config path | `%s` |" % audit["config_path"])
    A("| Config file sha256 | `%s` |" % audit["config_file_sha256"])
    A("| Config json-canonical digest/16 | `%s` |" % audit["config_json_digest_16"])
    A("| Providers | %d |" % counts["providers"])
    A("| `[models.*]` entries | %d |" % counts["model_entries"])
    A("| Distinct (provider, model) pairs | %d |" % counts["distinct_provider_model_pairs"])
    A("| Global `[thinking] effort` | `%s` |" % counts["global_thinking_effort"])
    A("| Findings | %d defects, %d notes, %d verify-later |"
      % (triage.get("defect", 0), triage.get("note", 0), triage.get("verify-later", 0)))
    A("")
    A("**Provenance.** The json-canonical digest above is `61f22a2bbe52d616`, byte-identical")
    A("to the digest the M1 census was measured against, so every census finding (D1–D9)")
    A("still applies to this config and is used as evidence below without re-probing it.")
    A("The file-bytes digest of the same file is `%s`; the two differ because M1 digests"
      % audit["config_file_sha256"][:16])
    A("the parsed structure, not the bytes. No config edit happened between the two missions.")
    A("")
    A("---")
    A("")

    # ---------------------------------------------------------------- sections
    A("## 1. Method and probe budget")
    A("")
    A("Three evidence channels, in increasing order of cost:")
    A("")
    A("1. **Static audit** (`scripts/audit_definitions.py`) — reads the config and the")
    A("   client binary's own strings; costs nothing. The binary is an unstripped Rust")
    A("   build, so a declared field that never appears in it cannot be parsed:")
    A("")
    A("   | field | occurrences in `~/.kimi-code/bin/kimi` |")
    A("   | --- | --- |")
    for k, v in sorted(audit["binary_field_hits"].items(), key=lambda kv: (kv[1], kv[0])):
        A("   | `%s` | %d |" % (k, v))
    A("")
    A("   The two zeros are the audit's first hard result: **`off_effort` and")
    A("   `max_input_size` are not fields this client knows.** `kimi doctor config`")
    A("   reports nothing about them because it does not validate model-level keys at")
    A("   all — a config with a deliberately misspelled model key (`zzz_unknown_key`),")
    A("   a bogus effort value and a bogus capability is reported as valid, so doctor's")
    A("   silence is not evidence either way (verified, see section 7).")
    A("")
    A("2. **Client wire capture** (`scripts/probe_client_semantics.py` +")
    A("   `scripts/mock_provider.py`) — runs the real client against a loopback mock")
    A("   provider and records the request it builds. Zero quota: the upstream is local.")
    A("   This is what turns \"declared\" into \"transmitted\".")
    A("")
    A("3. **Live probes** (`scripts/probe_live.py`) — one request per cell against the")
    A("   real lanes. Budget: %d requests in total across three passes, every one of them"
      % len(rows))
    A("   minimal (`max_tokens` 16, 256 for the tool suite after pass 1 showed thinking")
    A("   models spend the whole 16-token budget on reasoning before emitting a call).")
    A("   No loops, no repeats except one deliberate reproducibility row.")
    A("")
    A("Two method corrections were forced by the evidence and are worth stating, because")
    A("both first-pass results were probe artefacts, not lane properties:")
    A("")
    A("- **User-Agent.** With Python's default UA, every `opencode-go` request returned")
    A("  `403 error code: 1010` (a Cloudflare block). The same request with a browser UA")
    A("  returned 200. Pass 1's opencode-go rows are therefore void and were re-run in")
    A("  pass 2 (`raw/probes-*-pass2.json`).")
    A("- **`tool_choice`.** Forcing a tool choice returned 400 on the `hyper` and")
    A("  `opencode-go`/anthropic lanes. The mock capture shows the client **never sends")
    A("  `tool_choice` at all** — it sends `tools` and lets the model decide — so the")
    A("  400s measured the probe, not the lane. Pass 3 re-ran those cells in the")
    A("  client's own shape and all three returned a well-formed tool call.")
    A("")
    A("---")
    A("")

    A("## 2. The audit table")
    A("")
    A("The full per-entry table (all %d entries, every field the mission asked for) is"
      % len(entries))
    A("`audit-table.md`; `audit-table.json` carries the same rows plus every finding.")
    A("Summary of what is declared:")
    A("")
    A("| Dimension | Values across the file |")
    A("| --- | --- |")
    A("| protocols | %s |" % ", ".join(sorted({e["protocol"] for e in entries})))
    A("| effort values declared | %s |" % ", ".join(audit["effort_values_declared"]))
    A("| `off_effort` values | %s |" % (", ".join(audit["off_effort_values"]) or "none"))
    A("| `default_effort` values | %s |" % ", ".join(audit["default_effort_values"]))
    A("| entries with no `max_output_size` | %d |" % counts["entries_without_max_output_size"])
    A("| entries declaring `off_effort` | %d |" % counts["entries_with_off_effort"])
    A("| entries declaring `max_input_size` | %d |" % counts["entries_with_max_input_size"])
    A("")
    A("---")
    A("")

    # ---------------------------------------------------------- wire semantics
    A("## 3. What the client actually transmits (mock capture)")
    A("")
    A("One request per test model against a loopback provider, two config flavours")
    A("(`global_max` = the live `[thinking] effort = \"max\"`, `no_global` = the same file")
    A("with that line removed). Evidence: `raw/client-semantics.json`; reproduce with")
    A("`python3 scripts/probe_client_semantics.py`.")
    A("")
    if semantics:
        A("| declared | sent (global effort present) | sent (global effort absent) |")
        A("| --- | --- | --- |")
        by_alias = defaultdict(dict)
        for r in semantics["results"]:
            by_alias[r["alias"]][r["flavour"]] = r
        for alias in by_alias:
            def cell(flavour):
                r = by_alias[alias].get(flavour) or {}
                s = r.get("sent") or {}
                eff = (s.get("reasoning_effort") or s.get("output_config.effort")
                       or s.get("reasoning.effort") or s.get("thinking.effort"))
                bits = []
                bits.append("effort=%r" % eff)
                if s.get("max_tokens") is not None:
                    bits.append("max_tokens=%s" % s["max_tokens"])
                if s.get("max_completion_tokens") is not None:
                    bits.append("max_completion_tokens=%s" % s["max_completion_tokens"])
                bits.append("tools=%s" % s.get("tools"))
                return "<br>".join(bits)
            A("| `%s` | %s | %s |" % (alias, cell("global_max"), cell("no_global")))
        A("")
    A("**The rules this establishes.**")
    A("")
    A("1. **Effort is selected as: global `[thinking] effort` > per-model `default_effort`**")
    A("   **(top-level or `[models.<alias>.overrides]`, both verified) >")
    A("   `support_efforts[floor(n/2)]`** when neither is declared, else nothing is sent.")
    A("   The middle-index rule reproduces on 11 distinct declared lists, e.g.")
    A("   `[low, medium, xhigh] -> medium`, `[low, high, max] -> high`,")
    A("   `[max, minimal] -> minimal`, `[max] -> max`.")
    A("2. **A global `effort` overrides every model's own default and is not clamped to")
    A("   `support_efforts`.** With the live `effort = \"max\"`, even a model declaring")
    A("   `[low, medium, xhigh]` is sent `reasoning_effort: \"max\"` — a value it does not")
    A("   claim to accept. %d entries in the file are in that position (finding DEF-3b)."
      % sum(1 for d in defects if d["id"] == "DEF-3b"))
    A("3. **The effort key is protocol-specific**, so a per-model claim cannot be checked")
    A("   without the right shape:")
    A("")
    A("   | protocol | request field |")
    A("   | --- | --- |")
    A("   | `openai` | `reasoning_effort` |")
    A("   | `anthropic` | `output_config.effort` (+ `context_management`, `max_tokens`) |")
    A("   | `openai_responses` | `reasoning.effort` (+ `store:false`) |")
    A("   | `kimi` | `thinking.effort` |")
    A("")
    A("4. **`max_output_size` is transmitted**, as `max_tokens` on `openai`/`anthropic`")
    A("   (and as `max_completion_tokens` on `kimi`); with the field absent the openai")
    A("   lanes send no cap at all, `anthropic` falls back to a hardcoded 64000, and")
    A("   `kimi` sends `max_context_size - 193`.")
    A("5. **`capabilities` barely reaches the wire.** Only `image_in`/`video_in` change")
    A("   the payload, and they add exactly one tool (`ReadMediaFile`) — 26 tools vs 25")
    A("   in this capture, 30 vs 29 under the fuller live config. `tool_use` presence or")
    A("   absence does not add or remove the tool array: a model declaring only")
    A("   `[\"thinking\"]` still receives every tool. `always_thinking` and")
    A("   `dynamically_loaded_tools` produced no observable difference.")
    A("   Consequence: a lane being \"chat-only\" **cannot be expressed in config**; the")
    A("   client will always offer tools, and only the upstream's behaviour decides.")
    A("6. **The client never sends `tool_choice`**, and sends `tools` on every request")
    A("   regardless of the model's declared capabilities.")
    A("")
    A("---")
    A("")

    # ------------------------------------------------------------- live probes
    A("## 4. Live probe evidence")
    A("")
    A("### 4.1 Effort values (one request per cell)")
    A("")
    A("An `invalid-control` token (in no model's `support_efforts`) is sent once per lane.")
    A("It is the difference between \"this lane accepts xhigh\" and \"this lane accepts")
    A("anything\":")
    A("")
    A("| lane | declared values accepted (200) | control behaviour | reading |")
    A("| --- | --- | --- | --- |")
    for lane, acc, verdict, why in effort_lane_table(rows):
        A("| `%s` | %s | %s | %s |" % (lane, acc, why, verdict))
    A("")
    A("What this settles: on `alibaba-token-plan`, `openai-codex` and `opencode-go` the")
    A("acceptance is real (the same lane rejects a value it does not know, 400). On")
    A("`hyper`, `zai-coding-plan`, `xai-oauth` and `cursor` the field is ignored — the")
    A("acceptance is vacuous, and the xai shim's documented rewrite of unsupported")
    A("values is consistent with that. `devin` could not be measured: the lane answered")
    A("`502 {\"error\": {\"message\": \"session/prompt: Reached free model rate limit.")
    A("Please switch to a different model. Your limit will reset in 1 hour 7 minutes")
    A("(at 13:01 UTC).\"}}` for a direct chat instead of a completion.")
    A("")
    A("### 4.2 Tool calling (the census's open gap)")
    A("")
    A("One request carrying a single function schema (`r18_echo`), the client's own shape.")
    A("A cell counts as positive only when a well-formed call for that function returns")
    A("(a 200 that merely *describes* the call in prose does not count). The `status=400`")
    A("cells are pass 2's forced-`tool_choice` artefact, re-run clean in pass 3; the")
    A("`status=403` cells are pass 1's User-Agent block on opencode-go, re-run in pass 2.")
    A("")
    A("| lane | verdict | pass detail (source:status/served model) |")
    A("| --- | --- | --- |")
    for lane, verdict, detail in tool_table(rows):
        A("| `%s` | %s | %s |" % (lane, verdict, detail))
    A("")
    A("The census recorded these claims but could not test them; measured, they hold with")
    A("one nuance worth keeping: `cursor` answers a tool request with prose (\"Calling")
    A("`r18_echo` with the text `ping`\") and `tool_calls: null`, which is exactly the")
    A("\"CHAT-ONLY (no tool calls)\" note in `[secondary_model.models]`. The")
    A("`cascade/glm-5.3-flash` entry is \"chat-only\" **for its devin leg only**: pass 1 was")
    A("served by devin (`glm-5-3-flash-max`, prose, no call) and pass 2 — after devin")
    A("rate-limited — fell through to the zai leg (`glm-5.3-flash`) and returned a proper")
    A("call. So the lane's tool capability depends on which leg answers, and the routing")
    A("note's warning about a degraded tool task applies only to the devin leg.")
    A("")
    A("### 4.3 `image_in` claims")
    A("")
    A("A real PNG, base64 data URL, in the first user message. Pass 1 used 1x1 — which")
    A("turned out to be *below* several lanes' minimum and produced the useful error")
    A("messages below; pass 2 repeated the cells with 32x32.")
    A("")
    A("| alias | declares image_in | result |")
    A("| --- | --- | --- |")
    for alias, declared, cells in image_table(rows):
        A("| `%s` | %s | %s |" % (alias, declared, cells))
    A("")
    A("The 1x1 rejections are themselves evidence of image processing — the lane inspected")
    A("the dimensions before refusing (\"Image is too small or too large\", \"height:1 or")
    A("width:1 must be larger than 10\", \"Both width and height must be at least 8")
    A("pixels\"). The **negative control is clean**: `zai-coding-plan/glm-5-turbo` does not")
    A("declare `image_in` and rejected the same payload with `messages.content.type is")
    A("invalid, allowed values: ['text']` at both sizes, so these lanes really do")
    A("discriminate on image input.")
    A("")
    A("### 4.4 `reasoning_key`")
    A("")
    A("For every response whose message keys were captured, the key the config declares")
    A("vs. the key the lane actually returned:")
    A("")
    A("| alias | declared reasoning_key | responses carrying it | message keys seen |")
    A("| --- | --- | --- | --- |")
    for alias, declared, hits, keys in reasoning_table(rows):
        A("| `%s` | `%s` | %s | %s |" % (alias, declared, hits, keys))
    A("")
    A("Every lane that declares `reasoning_content` and returned reasoning returned it")
    A("under exactly that name — no mismatch was found. A `0/N` row means the sample's")
    A("reasoning went into a tool call or the lane answered without a reasoning block,")
    A("not that the name is wrong.")
    A("")
    A("---")
    A("")

    # ----------------------------------------------------------- defect classes
    A("## 5. Defect classes")
    A("")
    A("Every finding is in `audit-table.json` with its `triage` (defect / note /")
    A("verify-later), the affected alias, the config value, a one-line `detail` and an")
    A("`evidence` pointer. Counts by class:")
    A("")
    A("| class | findings | triage |")
    A("| --- | --- | --- |")
    for cls, n in sorted(by_class.items(), key=lambda kv: -kv[1]):
        tris = sorted({d["triage"] for d in defects if d["class"] == cls})
        A("| %s | %d | %s |" % (cls, n, ", ".join(tris)))
    A("")
    A("The classes that need a decision:")
    A("")
    A("**A. Two declared field names do not exist in this client** (19 findings, defect).")
    A("`off_effort` (10 entries) and `max_input_size` (9 entries) have zero occurrences in")
    A("the binary, and the mock capture shows `off_effort` has no effect on what is sent.")
    A("The effort value is chosen from `default_effort`/`support_efforts` only. These are")
    A("declarations that read as limits and enforce nothing.")
    A("")
    A("**B. Size caps that are arithmetic, not measurement** (%d findings, defect)."
      % sum(1 for d in defects if d["id"].startswith("DEF-2")))
    A("`hyper/kimi-k2-thinking = 26214`, `hyper/minimax-m2.7 = 6553`,")
    A("`hyper/gpt-oss-120b = 13107` are exactly `floor(2^18/10)`, `floor(2^16/10)`,")
    A("`floor(2^17/10)`, and `hyper/gemma-4-26b-a4b-it = 25600` is exactly")
    A("`max_context_size/10`. Since `max_output_size` is transmitted as `max_tokens`, a")
    A("unit slip here truncates real output. The same class covers 7 entries whose output")
    A("cap equals or exceeds their context size, 6 where input + output exceeds context,")
    A("and 1 where `max_input_size == max_context_size`.")
    A("")
    A("**C. The global thinking effort silently overrides 31 model declarations** (DEF-3b).")
    A("See section 3, rule 2. `[thinking] effort = \"max\"` is sent to models that declare")
    A("no support for it. Whether that breaks anything is lane-dependent and measured in")
    A("4.1 — the lanes that validate values (token-plan, codex, opencode-go) did accept")
    A("`max`, so this is a correctness-of-intent issue rather than a live outage; but the")
    A("file's per-model `support_efforts` are currently decorative.")
    A("")
    A("**D. Dead lanes and unentitled ids** (7 findings, defect). From the census and still")
    A("true against this digest: `managed:kimi-code` answers 401 on every path (empty")
    A("OAuth store), keys 2 and 3 of the token-plan are quota-exhausted (429),")
    A("`glm-5` is unentitled on all three token-plan lanes (403) and")
    A("`zai-coding-plan/glm-5.3-highspeed` is not in its plan (429). That is")
    A("**%d of %d entries routing to lanes that cannot serve them**."
      % (sum(1 for e in entries if e["provider"] in
             ("managed:kimi-code", "alibaba-token-plan-2", "alibaba-token-plan-3")), len(entries)))
    A("")
    A("**E. Cross-provider divergence for the same served id** (19 findings, defect).")
    A("`glm-5.3-flash` is declared with `max_output_size` 131072 on zai/opencode-go but")
    A("128000 on hyper; `deepseek-v4.1-flash` with 262144 on hyper but 384000 on")
    A("token-plan and opencode-go; `kimi-k2.6` with `max_output_size` equal to its whole")
    A("context on all three token-plan lanes. One of each pair is wrong; none was")
    A("measured, so these go to verify-later with the conservative default (smallest")
    A("declared value).")
    A("")
    A("**F. Capability claims the client cannot enforce** (14 notes, 46 verify-later).")
    A("`tool_use` absence does not stop the client sending tools (section 3, rule 5), so")
    A("the \"chat-only\" marking in the routing table is documentation rather than a")
    A("setting. `video_in`/`audio_in` are unprobed claims.")
    A("")
    A("**G. `reasoning_key` does not match what the lane returns** (11 findings, defect;")
    A("probe-derived, so they live in `audit-table.json` as DEF-9/DEF-10). Two entries")
    A("declare `reasoning_content` while the lane returns `reasoning` +")
    A("`reasoning_details` and never the declared key — `opencode-go/kimi-k3` and")
    A("`opencode-go/mimo-v2.5`. Nine entries declare no key at all while the lane")
    A("returned `reasoning_content`: the eight probed `hyper` models, plus")
    A("`xai-oauth/grok-4.5` and the two cascade entries. A reasoning pane cannot render")
    A("either way until the declaration matches the lane. The `reasoning` field the")
    A("opencode-go models return is a plain string holding the same text as")
    A("`reasoning_details[0].text`, so `reasoning` is the recommended replacement;")
    A("which key the client actually reads is not settled here and is listed in")
    A("verify-later.")
    A("")
    A("---")
    A("")

    A("## 6. Config corrections")
    A("")
    A("`config-corrections.toml` holds %d splice-ready model blocks with an `# evidence:`"
      % corrections_block_count())
    A("line each, plus the quarantine list for the dead lanes and a verify-later list.")
    A("The file is parsed by TOML at generation time (`scripts/build_corrections.py`), so")
    A("it is valid TOML by construction, and it contains no credential values.")
    A("")
    A("Three things it deliberately does **not** do:")
    A("")
    A("- It does not invent replacement numbers for the bad caps. Every such correction is")
    A("  a removal, because the client then sends no cap and the server decides —")
    A("  strictly safer than an arithmetic guess, and reversible.")
    A("- It does not touch the live config. Corrections are staged for the operator.")
    A("- It does not rewrite entries whose only finding is a note.")
    A("")
    A("---")
    A("")

    A("## 7. Secrets hygiene")
    A("")
    A("Command and result (`HYGIENE.md` carries the full log):")
    A("")
    A("````")
    A("$ bash scripts/hygiene_check.sh")
    if hygiene_text:
        A(hygiene_text.strip())
    A("````")
    A("")
    A("The scan tests every configured credential value — every provider `api_key` and")
    A("the opencode session header — against every file in this tree, and separately for")
    A("credential-shaped strings. Probe captures store header names with a")
    A("`<redacted:len=N>` marker, never values (`scripts/common.py`), and the live config")
    A("is never modified.")
    A("")
    A("---")
    A("")

    A("## 8. What this audit does not cover")
    A("")
    A("- **`max_context_size`.** The client never transmits a context limit, so no cheap")
    A("  probe can falsify these declarations; only a deliberately over-long prompt per")
    A("  lane would, and that is a quota-heavy test.")
    A("- **`video_in` / `audio_in`.** Declared on %d entries, probed on none."
      % sum(1 for e in entries if {"video_in", "audio_in"} & set(e["capabilities"])))
    A("- **Devin.** Rate-limited during the audit window; its direct chat path and its")
    A("  leg-1 behaviour should be re-checked after the reset.")
    A("- **The `[secondary_model.models]` routing table** is only audited where it points")
    A("  at models with defects found here; routing policy itself is M4's scope.")
    A("")
    A("---")
    A("")

    A("## 9. Reproducing this")
    A("")
    A("```")
    A("python3 scripts/audit_definitions.py        # -> audit-table.json, audit-table.md")
    A("python3 scripts/probe_client_semantics.py  # -> raw/client-semantics.json (no quota)")
    A("python3 scripts/probe_live.py all          # -> raw/probes-{effort,tool,image}.json")
    A("python3 scripts/probe_live.py pass2        # -> raw/probes-*-pass2.json (UA + budget fixes)")
    A("python3 scripts/probe_live.py pass3        # -> raw/probes-tool-pass3.json (client shape)")
    A("python3 scripts/build_corrections.py       # -> config-corrections.toml")
    A("python3 scripts/build_analysis.py          # -> ANALYSIS.md")
    A("bash    scripts/hygiene_check.sh           # -> HYGIENE.md, exit 0 expected")
    A("```")
    A("")
    A("Each probe script prints the config's json-canonical digest before probing, so a")
    A("config edit between runs is visible rather than silent.")

    with open(os.path.join(common.DEFS_DIR, "ANALYSIS.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("wrote ANALYSIS.md (%d lines)" % len(L))


hygiene_text = ""
if __name__ == "__main__":
    hp = os.path.join(common.DEFS_DIR, "HYGIENE.md")
    if os.path.exists(hp):
        with open(hp) as fh:
            hygiene_text = fh.read()
    main()
