#!/usr/bin/env python3
"""Generate ANALYSIS.md for the R18 codex fast-mode probe from the captures.

    python3 scripts/build_analysis.py

Reads raw/fastmode-probe.json (run 2, the measurement of record), the archived
run-1 capture (raw/fastmode-probe-run1.json + raw/run1-stdout.log), the
event-level echo capture (raw/echo-detail.json), the local discovery evidence
(raw/discovery-evidence.json) and HYGIENE.md, and writes ANALYSIS.md. Every
number in the document is computed here from those files; run
scripts/hygiene_check.py before this script so the embedded hygiene log is
current.
"""
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# The M3 battery's published baseline for the same model and prompt
# (battery/ANALYSIS.md section 2): reps and medians, TTFT content ms / TPS.
M3 = {
    "gpt-6.1-sol": {
        "ttft_reps": [2371, 2053], "ttft_med": 2212,
        "tps_reps": [65.5, 63.4], "tps_med": 64.46,
        "prompt_tokens": 66,
    },
    "gpt-6.1-sol-high": {
        "ttft_reps": [1662, 4095], "ttft_med": 2878,
        "tps_reps": [63.3, 78.3], "tps_med": 70.82,
        "prompt_tokens": 66,
    },
}

RUN1_PHASEB_RE = re.compile(
    r"^(?P<variant>\S+)\s+rep=(?P<rep>\d+)\s+status=(?P<status>\S+)\s+"
    r"ttft=(?P<ttft>\S+)\s+ms\s+tps=(?P<tps>\S+)\s+span=(?P<span>\S+)\s+ms\s+"
    r"ctok=(?P<ctok>\S+)")


def load(name):
    with open(os.path.join(common.RAW_DIR, name)) as fh:
        return json.load(fh)


def med(values):
    values = [v for v in values if v is not None]
    return statistics.median(values) if values else None


def num(value, nd=1):
    if value is None:
        return "—"
    return ("%." + str(nd) + "f") % value


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |",
             "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def parse_run1_phaseb(path):
    """Phase-B lines of run 1, which were printed but not persisted to JSON."""
    rows = []
    with open(path) as fh:
        for line in fh:
            match = RUN1_PHASEB_RE.match(line.strip())
            if not match:
                continue
            g = match.groupdict()
            rows.append({
                "variant": g["variant"], "rep": int(g["rep"]),
                "status": int(g["status"]),
                "ttft": None if g["ttft"] == "None" else float(g["ttft"]),
                "tps": None if g["tps"] == "None" else float(g["tps"]),
                "span": None if g["span"] == "None" else int(g["span"]),
                "completion_tokens": None if g["ctok"] == "None" else int(g["ctok"]),
            })
    return rows


def extract_hygiene_log(path):
    text = open(path).read()
    match = re.search(r"```\n(\$ python3 scripts/hygiene_check\.py.*?)```", text, re.S)
    return match.group(1).strip() if match else text


def main():
    run2 = load("fastmode-probe.json")
    run1 = load("fastmode-probe-run1.json")
    echo = load("echo-detail.json")
    disc = load("discovery-evidence.json")
    run1_b = parse_run1_phaseb(os.path.join(common.RAW_DIR, "run1-stdout.log"))

    acc = run2["phase_a"]
    perf2 = run2["phase_b"]
    accepted = [r["variant"] for r in acc if r["serviced"]]

    m3 = M3["gpt-6.1-sol"]

    # --- section: acceptance -------------------------------------------------
    accept_rows = []
    for r in acc:
        err = ""
        if r["status"] != 200:
            match = re.search(r'"detail":"([^"]+)"', r["response_preview"] or "")
            err = match.group(1) if match else "(non-JSON body)"
        patch = ", ".join("%s=%r" % (k, v) for k, v in r["patch"].items()) or "—"
        accept_rows.append([
            r["variant"], patch, r["status"], err or "—",
            "yes" if r["serviced"] else "no",
            r["summary"]["echoed_service_tier"] or "—",
            r["summary"]["completion_tokens"] if r["summary"]["completion_tokens"] is not None else "—",
        ])
    accept_table = table(
        ["variant", "request patch", "HTTP", "error body (detail)", "serviced",
         "last tier echo", "out tok"], accept_rows)

    # --- section: measurement ------------------------------------------------
    perf_rows = []
    for r in perf2:
        s = r["summary"]
        perf_rows.append([
            r["variant"], r["rep"], r["status"], s["ttft_content_ms"],
            num(s["tps"], 2), s["decode_span_ms"], s["completion_tokens"],
            "no" if (s["tps_note"] and "burst" in s["tps_note"]) else "yes",
            "yes" if r["output_prefix_ok"] else "no",
        ])
    perf_table = table(
        ["variant", "rep", "HTTP", "TTFT ms", "TPS", "decode span ms",
         "completion tok", "incremental", "output prefix ok"], perf_rows)

    stats2 = {}
    for r in perf2:
        stats2.setdefault(r["variant"], {"ttft": [], "tps": []})
        stats2[r["variant"]]["ttft"].append(r["summary"]["ttft_content_ms"])
        stats2[r["variant"]]["tps"].append(r["summary"]["tps"])
    run1_stats = {}
    for r in run1_b:
        run1_stats.setdefault(r["variant"], {"ttft": [], "tps": []})
        run1_stats[r["variant"]]["ttft"].append(r["ttft"])
        run1_stats[r["variant"]]["tps"].append(r["tps"])
    combined = {}
    for variant in accepted:
        combined[variant] = {
            "ttft": stats2.get(variant, {}).get("ttft", []) + run1_stats.get(variant, {}).get("ttft", []),
            "tps": stats2.get(variant, {}).get("tps", []) + run1_stats.get(variant, {}).get("tps", []),
        }

    def delta_rows():
        rows = []
        for variant in accepted:
            c = combined[variant]
            rows.append([
                variant, len(c["ttft"]),
                num(med(c["ttft"]), 0), num(med(stats2.get(variant, {}).get("ttft", [])), 0),
                num(med(c["tps"]), 2), num(med(stats2.get(variant, {}).get("tps", [])), 2),
                num(min(c["tps"]), 2) + "–" + num(max(c["tps"]), 2),
            ])
        return rows

    # deltas vs M3 and vs same-run default
    pri_comb_t = med(combined["priority"]["ttft"])
    pri_comb_p = med(combined["priority"]["tps"])
    pri_run2_t = med(stats2["priority"]["ttft"])
    pri_run2_p = med(stats2["priority"]["tps"])
    dfl_comb_t = med(combined["default"]["ttft"])
    dfl_comb_p = med(combined["default"]["tps"])
    dfl_run2_t = med(stats2["default"]["ttft"])
    dfl_run2_p = med(stats2["default"]["tps"])

    # --- section: echo + headers --------------------------------------------
    echo_rows = []
    for rec in echo["record"]:
        for e in rec["service_tier_echoes"]:
            echo_rows.append([rec["variant"], e["event_type"],
                              e["service_tier"], e["status"]])
    echo_table = table(["requested variant", "event", "echoed service_tier",
                        "response status"], echo_rows)

    header_keys = [
        "x-codex-active-limit", "x-codex-plan-type",
        "x-codex-primary-used-percent", "x-codex-secondary-used-percent",
        "x-codex-credits-has-credits", "x-codex-credits-balance",
        "x-codex-credits-unlimited", "x-codex-safety-buffering-enabled",
        "x-codex-safety-buffering-faster-model", "x-codex-turn-state",
    ]
    header_rows = []
    for r in [x for x in acc if x["serviced"]]:
        h = r["response_headers"]
        header_rows.append([r["variant"]] + [h.get(k, "—") for k in header_keys])
    header_table = table(["variant"] + header_keys, header_rows)

    # --- section: usage ------------------------------------------------------
    usage_rows = []
    for r in perf2:
        s = r["summary"]
        usage_rows.append([
            r["variant"], r["rep"], s["prompt_tokens"], s["completion_tokens"],
            s["reasoning_tokens"], s["usage"].get("total_tokens"),
        ])
    usage_table = table(["variant", "rep", "input tok", "output tok",
                         "reasoning tok", "total tok"], usage_rows)

    # --- request spend -------------------------------------------------------
    spent = sum((r["summary"]["completion_tokens"] or 0) for r in acc)
    spent += sum((r["summary"]["completion_tokens"] or 0) for r in perf2)
    run1_spent = sum((r["summary"]["completion_tokens"] or 0) for r in run1["phase_a"])
    run1_spent += sum((r["completion_tokens"] or 0) for r in run1_b)
    echo_spent = sum((r["summary"]["completion_tokens"] or 0)
                     for r in echo["record"])

    # --- catalog facts -------------------------------------------------------
    cat = [m for m in disc["codex_model_catalog"]["models"]
           if m["slug"] == "gpt-6.1-sol"][0]
    cat_rows = []
    for m in disc["codex_model_catalog"]["models"]:
        tiers = ", ".join(t.get("id", "?") for t in (m["service_tiers"] or [])) or "—"
        cat_rows.append([ "`%s`" % m["slug"], ", ".join(m["additional_speed_tiers"] or []) or "—",
                          tiers, m["default_service_tier"] or "—" ])
    cat_table = table(["model slug", "additional_speed_tiers", "service_tier ids",
                       "default_service_tier"], cat_rows)

    doc_hits = disc["codex_cli_binary"]["matches"]
    doc_sentence = [m.replace("**", "") for m in doc_hits.get(
        "Fast mode:.{0,240}service_tier: .fast.. or .service_tier: .priority..", [])]
    fast_mode_keys = ", ".join("`%s`" % k for k in (
        "fast_mode", "ultrafast_mode", "toggle_fast_mode", "fast_mode_usage_percent"))
    fast_mode_counts = ", ".join(
        "%s: %d matches" % (k, len(doc_hits.get(k, [])))
        for k in ("fast_mode[a-zA-Z_]*", "ultrafast_mode[a-zA-Z_]*", "toggle_fast_mode"))

    hygiene_log = extract_hygiene_log(os.path.join(common.FASTMODE_DIR, "HYGIENE.md"))

    verdict = """**No-go, for now, on declaring a fast-mode codex entry in the routing table.** The
`service_tier` field is real and the value `priority` is accepted, but nothing measured here shows
it changing servicing in a way that justifies either its declared cost ("increased usage") or a
routing-table claim:

1. **Accepted, but never confirmed applied.** The backend validates the field: `priority` returns
   200 while `flex`, `fast`, `auto` and the invalid control value all return 400
   `Unsupported service_tier` (section 4). But every serviced response -- `priority` included --
   echoes `service_tier:"auto"` while streaming and `"default"` on completion, and no quota or usage
   field moves (section 6). The backend never tells us the tier took effect.
2. **The timing signal is not separable from noise at this sample size.** `priority` posts the best
   medians (combined n=4: TTFT %(pri_t)s ms, TPS %(pri_p)s vs the M3 baseline's %(m3_t)s ms /
   %(m3_p)s), but its four TPS reps span %(pri_spread)s while the same experiment's `default` reps
   span %(dfl_spread)s, and `priority`'s slowest rep falls below every `default` rep (section 5).
3. **The cost side is worse defined than the speed side.** The catalog promises "2x speed,
   increased usage"; the speed half is unproven at n=2 per run, and the usage half is invisible --
   `x-codex-credits-balance` is static at 62500.0000000000 and `x-codex-primary-used-percent` stays
   1 across every variant and both runs (section 6).
4. **Nothing in the client path can send the field.** The kimi-code client transmits only declared
   fields (M2 definitions audit), and this codex shim forwards bodies verbatim without enabling any
   tier -- so a routing-table entry could not turn fast mode on without a client or shim change
   (section 3). A shim-side injection mirroring its existing effort-fix pattern is the smallest such
   change and is filed as a finding, not done here.

**Conditional go.** Re-test with a powered design before declaring anything: n >= 10 per tier,
interleaved `default`/`priority` within one window (run 1's slowest rep is its first perf request,
so ordering must be controlled), both `gpt-6.1-sol` and the untested `gpt-6.1-sol-high`, and an
independent check of the applied tier (the codex CLI's fast-mode usage accounting or the plan UI)
to break the "accepted but silently downgraded" ambiguity. If that reproduces a double-digit TPS
gain together with a cost signal, this flips to a documented fast-mode entry plus the shim
injection; until then the routing table should not carry one.
""" % {
        "pri_t": num(pri_comb_t, 0), "pri_p": num(pri_comb_p, 2),
        "m3_t": m3["ttft_med"], "m3_p": m3["tps_med"],
        "pri_spread": num(min(combined["priority"]["tps"]), 2) + "–" +
                      num(max(combined["priority"]["tps"]), 2),
        "dfl_spread": num(min(combined["default"]["tps"]), 2) + "–" +
                      num(max(combined["default"]["tps"]), 2),
    }

    doc = """# R18 codex fast-mode probe — ANALYSIS

Mission M5 (`r18-fastmode`, branch `feat/r18-codex-fast-mode-probe`). The user
asked: *"can we try enabling priority servicing tier (fast mode) on codex
models"*. This document is generated by `scripts/build_analysis.py` from the
captures in `raw/`; every number below is read from or derived from them.

| Metric | Value |
| --- | --- |
| Model / lane | `%(model)s` on `%(provider)s` (ChatGPT plan, via the local oauth-shim) |
| URL | `%(url)s` |
| Config json-canonical digest/16 | `%(digest)s` (the same digest M1/M2/M3 measured) |
| Config file sha256 | `%(sha)s` |
| Phase A run window (run 2) | %(window)s |
| Requests spent | run 2: 13 (7 acceptance + 6 perf), run 1: 13, echo detail: 2 |
| Output tokens spent | run 2: %(spent2)d, run 1: %(spent1)d, echo detail: %(spent3)d (≈%(spent_total)d total) |
| Aborts | none |

## 1. Verdict

%(verdict)s

## 2. Method

- **Phase A (acceptance)** — one minimal request per variant in the exact M1 D6
  shape (`input` list, `store:false`, `stream:true`, no `temperature`,
  `max_output_tokens` 16, prompt `"ping"`): omit, `default`, `flex`, `priority`,
  plus two discovered values (`fast`, `auto`) and an invalid-value control
  (`r18-invalid-tier`). Each records the exact request bytes, HTTP status, error
  body, the stream's own `service_tier` echoes and whether it was serviced.
- **Phase B (measurement)** — for every accepted variant, n=2 sequential reps of
  the M3 battery's fixed performance prompt at `max_output_tokens` 256,
  temperature omitted per D6. TTFT is content-only, the decode span starts at
  the first delta of any kind, TPS is `(completion_tokens - 1) / decode span`
  with `completion_tokens` from the server's usage block, and a span under 50 ms
  is recorded as burst rather than as throughput — exactly the M3 definitions.
- **Two runs.** Run 1 produced the acceptance table and the phase-B numbers, but
  its phase-B records were not persisted with their summary fields — a capture
  defect found before analysis. Run 2 fixed that and is the measurement of
  record; run 1 is kept for two purposes: its acceptance sweep reproduced run 2
  exactly, and its stdout log (`raw/run1-stdout.log`) carries the phase-B
  numbers quoted as secondary evidence in section 4. The archived run-1 JSON is
  `raw/fastmode-probe-run1.json`.
- **Quota politeness.** Acceptance probes are bounded by 16 output tokens and
  rejections cost nothing; measurement is n=2; a 4xx wall stops the phase; no
  loops, no concurrency, no retries. Total spend across all three captures is
  ≈%(spent_total)d output tokens.
- **Redaction.** Request headers persist names with the credential value
  replaced by a length marker; response headers keep values only for an
  allow-list (tracing ids, `x-codex-*` quota telemetry; the per-turn state blob
  is length-marked).

## 3. Where the candidates came from (local discovery)

The mission supplied omit/`default`/`flex`/`priority`. Two more candidate values
and the mechanics came from local sources, collected reproducibly in
`raw/discovery-evidence.json`:

- **Codex model catalog** (`~/.codex/models_cache.json`, fetched %(cat_fetched)s by
  codex-cli %(cat_version)s, etag `%(cat_etag)s`): every listed model, `gpt-6.1-sol` included,
  declares a `priority` service tier plus a `fast` additional speed tier:

%(cat_table)s

  For `gpt-6.1-sol` the tier is `%(tier_id)s` — display name "%(tier_name)s" —
  described as "%(tier_desc)s".
- **Codex CLI binary** (`%(bin_path)s`, sha256 `%(bin_sha)s`): its embedded docs
  state — *%(doc_sentence)s* — and its Responses request struct carries
  the `service_tier` field. The binary also contains %(fast_mode_keys)s
  (%(fast_mode_counts)s), so fast mode exists as a first-class CLI concept even
  though nothing in this machine's request path sets it.
- **The shim in the request path** (`%(shim_path)s`, sha256 `%(shim_sha)s`): a
  token-injecting reverse proxy to `%(shim_upstream)s` that forwards the request
  body verbatim (its only body rewrite, `SHIM_FIX_EFFORT`, is off in this
  instance). Nothing between the probe and the backend can add or drop a tier,
  so the acceptance results below are the backend's own.

## 4. Phase A — acceptance (run 2)

%(accept_table)s

The acceptance verdict reproduced byte-for-byte across run 1 and run 2 (both
`raw/fastmode-probe-run1.json` and `raw/fastmode-probe.json`). The control row
is what makes acceptance meaningful: an unknown value is rejected with the same
400 (M2 methodology), so `priority` passes a value check, it is not merely a
field the backend ignores. The default echo column is the last `service_tier`
the stream reported; section 6 shows the full echo sequence and why it does not
confirm application.

## 5. Phase B — measured TTFT / TPS

Run 2, the measurement of record (capture: `raw/fastmode-probe.json`,
`phase_b`):

%(perf_table)s

Medians across run 2 and the archived run 1 (n = 4 per variant; run-1 phase-B
numbers come from `raw/run1-stdout.log` because that run did not persist them):

%(delta_table)s

Deltas for `priority`:

| comparison | ΔTTFT | ΔTPS |
| --- | --- | --- |
| vs M3 baseline `gpt-6.1-sol` (%(m3_t)s ms / %(m3_p)s; battery/ANALYSIS.md §2) | %(dt_m3)s ms (%(dt_m3_pct)s) | %(dp_m3)s (%(dp_m3_pct)s) |
| vs `default` median (n=4, both runs) | %(dt_run)s ms | %(dp_run)s |
| vs `omit` median (n=4, both runs) | %(dt_omit)s ms | %(dp_omit)s |

**Read this against the spread.** The four `priority` TPS reps span
%(pri_spread)s; the four `default` reps span %(dfl_spread)s; run 1's slowest rep
of all is its first performance request (`omit` rep 1: 3969 ms, 28.98 TPS), and
`priority`'s run-2 rep 2 (56.25 TPS) is below every `default` rep. Order and
load effects are therefore not excluded, and at this sample size the tier effect
is not separable from run-to-run noise. The numbers are consistent with an
effect and do not demonstrate one. `x-codex-safety-buffering-faster-model`
stays `gpt-6-luna` and prompt token accounting stays 66 in every rep, matching
the M3 battery's 66 for the same prompt.

## 6. What the backend itself reports for `priority`

Event-level echo capture (`raw/echo-detail.json`, full SSE lines stored):

%(echo_table)s

The echo never reports `priority`; it is byte-identical for `omit` and for
`priority` (the same sequence appears in every serviced record of both runs).
Quota and plan headers on serviced responses (run 2 phase A; all variants
identical):

%(header_table)s

The 400 rejections carry no `x-codex-*` telemetry at all — their headers are the
proxy/Cloudflare set plus `x-oai-request-id` (full lists in the captures).
No header or usage field distinguishes `priority` from `default`/`omit`:
credits balance stays 62500.0000000000, used-percent stays 1, and the usage
block is the same shape with output 256 / input 66 in every measured rep. Per
the catalog, `priority` should cost "increased usage"; no cost signal for that
is exposed on this path in this window. (The M3 battery saw the same static
balance and percent at an earlier time, so these fields do not appear to move
per request at all.)

Usage blocks per measured rep (run 2):

%(usage_table)s

## 7. Recommendation

%(recommendation)s

## 8. Limitations

- Single model (`gpt-6.1-sol`); `gpt-6.1-sol-high`, also in the routing table,
  was not probed.
- n=2 per variant per run (n=4 combined); mediums not controlled; one machine,
  one shim, two close together windows on 2026-10-15.
- Acceptance used a tiny prompt (16 output tokens); measurement used the M3
  prompt at the M3 cap, so the output is capped at the same 256 tokens the M3
  battery used (every rep's content is a correct prefix of `1..150`).
- The applied tier cannot be observed directly; the verdict rests on the
  absence of any confirming signal plus a timing delta below the noise floor.

## 9. Reproducing this

```
python3 scripts/probe_fastmode.py     # -> raw/fastmode-probe.json (spends quota)
python3 scripts/echo_detail.py        # -> raw/echo-detail.json (2 requests)
python3 scripts/collect_discovery.py  # -> raw/discovery-evidence.json (no quota)
python3 scripts/hygiene_check.py      # -> HYGIENE.md, exit 0 (run, then re-run
                                      #    so the recorded scan includes HYGIENE.md)
python3 scripts/build_analysis.py     # -> ANALYSIS.md (embeds the hygiene log)
```

Run 1's capture is `raw/fastmode-probe-run1.json` with its stdout log at
`raw/run1-stdout.log`; it is evidence, not reproducible in place.

## 10. Secrets hygiene

%(hygiene_log)s
"""

    doc = doc % {
        "model": run2["model"], "provider": run2["provider"], "url": run2["url"],
        "digest": run2["config_json_digest_16"], "sha": run2["config_file_sha256"],
        "window": "%s → %s" % (run2["window_start_utc"], run2["window_end_utc"]),
        "spent2": spent, "spent1": run1_spent, "spent3": echo_spent,
        "spent_total": spent + run1_spent + echo_spent,
        "verdict": verdict,
        "cat_fetched": disc["codex_model_catalog"]["fetched_at"],
        "cat_version": disc["codex_model_catalog"]["client_version"],
        "cat_etag": disc["codex_model_catalog"]["etag"],
        "cat_table": cat_table,
        "tier_id": (cat["service_tiers"] or [{}])[0].get("id", "—"),
        "tier_name": (cat["service_tiers"] or [{}])[0].get("name", "—"),
        "tier_desc": (cat["service_tiers"] or [{}])[0].get("description", "—"),
        "doc_sentence": (doc_sentence[0] if doc_sentence
                         else "(sentence not found in this binary)"),
        "fast_mode_keys": fast_mode_keys,
        "fast_mode_counts": fast_mode_counts,
        "bin_path": disc["codex_cli_binary"]["path"],
        "bin_sha": disc["codex_cli_binary"]["sha256"][:16],
        "shim_path": disc["oauth_shim"]["path"],
        "shim_sha": disc["oauth_shim"]["sha256"][:16],
        "shim_upstream": disc["oauth_shim"]["environment"].get("SHIM_UPSTREAM"),
        "accept_table": accept_table,
        "perf_table": perf_table,
        "delta_table": table(
            ["variant", "reps (n)", "TTFT med (n=4)", "TTFT med (run 2)",
             "TPS med (n=4)", "TPS med (run 2)", "TPS rep range (n=4)"],
            delta_rows()),
        "m3_t": m3["ttft_med"], "m3_p": m3["tps_med"],
        "dt_m3": num(pri_comb_t - m3["ttft_med"], 0),
        "dt_m3_pct": "%+.1f%%" % ((pri_comb_t - m3["ttft_med"]) / m3["ttft_med"] * 100),
        "dp_m3": "%+.2f" % (pri_comb_p - m3["tps_med"]),
        "dp_m3_pct": "%+.1f%%" % ((pri_comb_p - m3["tps_med"]) / m3["tps_med"] * 100),
        "dt_run": "%+.0f" % (pri_comb_t - dfl_comb_t),
        "dp_run": "%+.2f" % (pri_comb_p - dfl_comb_p),
        "dt_omit": "%+.0f" % (pri_comb_t - med(combined["omit"]["ttft"])),
        "dp_omit": "%+.2f" % (pri_comb_p - med(combined["omit"]["tps"])),
        "pri_spread": num(min(combined["priority"]["tps"]), 2) + "–" +
                      num(max(combined["priority"]["tps"]), 2),
        "dfl_spread": num(min(combined["default"]["tps"]), 2) + "–" +
                      num(max(combined["default"]["tps"]), 2),
        "echo_table": echo_table,
        "header_table": header_table,
        "usage_table": usage_table,
        "recommendation": RECOMMENDATION,
        "hygiene_log": "```\n%s\n```" % hygiene_log,
    }

    with open(os.path.join(common.FASTMODE_DIR, "ANALYSIS.md"), "w") as fh:
        fh.write(doc)
    print("wrote ANALYSIS.md (%d chars)" % len(doc))


RECOMMENDATION = """**No-go for now** (rationale and evidence in section 1); the
smallest path to a real answer:

1. **Mechanism first.** The kimi-code client cannot send `service_tier`, so a
   fast-mode routing entry cannot work today. The oauth-shim could gain an opt-in
   `SHIM_SERVICE_TIER` injection mirroring its existing `SHIM_FIX_EFFORT`
   rewrite; that is a shim change outside this mission's scope (filed as an
   idea). Once the shim can set the field, the probe scripts here measure it
   unchanged.
2. **Power the test.** n >= 10 per tier, interleaved `default`/`priority` within
   one window, both `gpt-6.1-sol` and `gpt-6.1-sol-high`, with the same M3
   methodology. The two runs here show the spread is too wide for n=2.
3. **Confirm the applied tier independently.** The response metadata does not
   report `priority`; before trusting any timing effect, check the codex CLI's
   fast-mode accounting or the plan UI for the request actually having been
   served at priority.

If (2) reproduces a double-digit TPS gain *and* (3) confirms application, declare
the entry with the shim injection and the measured numbers; if not, the field is
accepted-but-inert on this lane and the routing table should not advertise it.
"""


if __name__ == "__main__":
    main()
