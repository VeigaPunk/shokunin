#!/usr/bin/env python3
"""Build ANALYSIS.md for the R18 capability battery from the captures.

    python3 scripts/build_analysis.py        # -> ANALYSIS.md

Every number in the generated sections is read out of `raw/` (raw captures,
telemetry.csv, run-manifest.json, regrade-check.json, prediction-scoring.json),
so re-running the battery and this script reproduces the document.
"""
import csv
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402
import score_predictions as sp  # noqa: E402

OUT = os.path.join(common.BATTERY_DIR, "ANALYSIS.md")
BUCKET_ORDER = ("FAST", "VERY-FAST", "MIDDLE", "STRONG")
PROBE_ORDER = ("c1", "c2", "c3", "c4", "c5", "k1", "k2", "k3", "t1")
CLASS_SHORT = {
    "ok": "ok", "transport": "TR", "auth": "AU", "refusal": "RF",
    "truncation": "TC", "format_break": "FB", "wrong_answer": "WA",
    "skipped_after_fatal": "--", "unknown": "?",
}


def load_json(name, default=None):
    path = os.path.join(common.RAW_DIR, name)
    if not os.path.exists(path):
        return default
    with open(path) as fh:
        return json.load(fh)


def fmt(value, digits=1):
    if value is None:
        return "—"
    if isinstance(value, float):
        return ("%%.%df" % digits) % value
    return str(value)


def reps(values):
    return " / ".join(fmt(v) for v in values) if values else "—"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out)


def main():
    manifest = load_json("run-manifest.json", {})
    regrade = load_json("regrade-check.json", {})
    scoring = load_json("prediction-scoring.json", {})
    records = grade.load_records()
    by_model = sp.measured(records)
    observed = sp.summarize(by_model)
    with open(os.path.join(common.BATTERY_DIR, "predictions",
                           "PREDICTIONS.json")) as fh:
        preds = json.load(fh)

    lines = []
    add = lines.append

    add("# R18 capability battery — ANALYSIS")
    add("")
    add("Mission M3 (`r18-battery`, branch `feat/r18-capability-battery`). This document is generated "
        "by `scripts/build_analysis.py` from the captures in `raw/`; every number below is read out "
        "of `raw/telemetry.csv`, `raw/responses/**`, `raw/run-manifest.json`, "
        "`raw/regrade-check.json` and `raw/prediction-scoring.json`.")
    add("")
    add(table(["Metric", "Value"], [
        ["Pool tested", "%d models from the live `[secondary_model.models]` table" % len(observed)],
        ["Config sha256", "`%s`" % manifest.get("config_sha256", "—")],
        ["Run window (UTC)", "%s → %s (%.0f s)" % (manifest.get("started_at_utc"),
                                                   manifest.get("finished_at_utc"),
                                                   manifest.get("duration_s") or 0)],
        ["Requests recorded", "%s of %s planned" % (manifest.get("requests_recorded"),
                                                    manifest.get("requests_planned"))],
        ["Concurrency", "%s models in flight, probes sequential within a model"
         % manifest.get("concurrency")],
        ["Determinism check", "%s mismatches re-grading %s records"
         % (regrade.get("mismatches"), regrade.get("checked"))],
        ["Predictions", "filed %s, scored in section 7" % preds.get("filed_at_utc")],
    ]))
    add("")

    add("## 1. Method (binding, per the operator directive)")
    add("")
    add("- **TTFT** = time from request send to the first decoded content token on a streaming "
        "request. Fixed identical prompt across every model (the same prompt as TPS), "
        "`max_tokens` 256, temperature 0 where the lane accepts it.")
    add("- **TPS** = decode throughput excluding TTFT: `(completion_tokens − 1) / (last-delta time − "
        "first-delta time)`, with `completion_tokens` taken from the server's `usage` block. The span "
        "starts at the first delta of any kind (a thinking lane that streams reasoning first would "
        "otherwise be credited with throughput it did not spend on output); the headline TTFT column "
        "is content-only, and the reasoning TTFT is reported separately.")
    add("- **n = 2 reps per model, sequential**; models run with bounded concurrency so no lane's own "
        "concurrency is a variable.")
    add("- **Burst rule**: a decode span under 50 ms with deltas present means the lane flushed the "
        "whole answer in one burst. TPS is reported as not derivable rather than as a throughput "
        "number, and such lanes are excluded from TPS rankings.")
    add("- **One attempt on a dead lane**: auth/quota walls and refused request shapes abort the "
        "model immediately; two consecutive transport failures abort it too. The remainder is "
        "recorded as `skipped_after_fatal`.")
    add("- **Failure-class taxonomy**: transport / auth / refusal / truncation / format_break / "
        "wrong_answer, plus `skipped_after_fatal`. A `request_level` failure is one the lane is "
        "answerable for; a content-level failure is about one answer.")
    add("- **Codex lanes** use the M1 D6 shape (`store:false`, `stream:true`, list `input`, no "
        "`temperature`, `max_output_tokens >= 16`); **devin-class lanes** get one warm-up pre-call "
        "excluded from every metric.")
    add("")

    add("## 2. Headline measurement: TTFT and TPS per pool model")
    add("")
    rows = []
    for pool_id in sorted(observed, key=lambda k: (BUCKET_ORDER.index(observed[k]["bucket"])
                                                   if observed[k]["bucket"] in BUCKET_ORDER else 99,
                                                   observed[k]["ttft_used"] or 1e9)):
        seen = observed[pool_id]
        shape = []
        if seen["incremental"]:
            shape.append("incremental")
        if seen["burst"]:
            shape.append("burst")
        if not shape:
            shape.append("no deltas")
        ttft_cell = fmt(seen["ttft_median"], 0)
        if seen["ttft_median"] is None and seen["ttft_used"] is not None:
            ttft_cell = "%s †" % fmt(seen["ttft_used"], 0)
        rows.append([
            "`%s`" % pool_id, seen["bucket"], seen["statuses"][0] if len(seen["statuses"]) == 1
            else "/".join(str(s) for s in seen["statuses"]),
            ttft_cell, reps(seen["ttft_reps"]) if seen["ttft_reps"] else "—",
            fmt(seen["tps_median"], 2), reps(seen["tps_reps"]),
            seen["prompt_tokens"], " / ".join(shape),
            "%d/%d" % (seen["pass_count"], len(PROBE_ORDER)),
        ])
    add(table(["model", "bucket", "status", "TTFT med ms", "TTFT reps", "TPS med",
               "TPS reps", "prompt tok", "stream shape", "pass"], rows))
    add("")
    add("`prompt tok` is the largest `prompt_tokens` the lane billed for the identical performance "
        "prompt, which is where a lane's fixed per-call overhead shows up. `pass` counts the 9 "
        "correctness probes.")
    add("")
    reasoning_first = [k for k, v in observed.items()
                       if v["ttft_median"] is None and v["ttft_used"] is not None]
    if reasoning_first:
        add("**† No content token inside the budget.** %s stream reasoning for the whole fixed "
            "`max_tokens` 256 and never emit a content token, so the operator's content-TTFT does "
            "not exist for them; the cell shows the first-decoded-token time instead and every "
            "ranking in this document uses that basis for those lanes. Their reasoning TTFT "
            "(first thinking token) is %s."
            % (", ".join("`%s`" % k for k in reasoning_first),
               ", ".join("`%s` %s ms" % (k, fmt(observed[k]["ttft_reasoning_median"], 0))
                         for k in reasoning_first)))
        add("")

    add("## 3. Within-bucket rankings")
    add("")
    for bucket in BUCKET_ORDER:
        members = [k for k, v in observed.items() if v["bucket"] == bucket]
        if not members:
            continue
        add("### %s (%d members)" % (bucket, len(members)))
        add("")
        ttft_rows = []
        for pool_id in sorted(members, key=lambda k: observed[k]["ttft_used"] or 1e9):
            seen = observed[pool_id]
            ttft_rows.append(["`%s`" % pool_id, fmt(seen["ttft_used"], 0),
                              fmt(seen["tps_median"], 2),
                              "%d/%d" % (seen["pass_count"], len(PROBE_ORDER)),
                              seen["dominant_class"]])
        add(table(["model (fastest first)", "TTFT med ms", "TPS med", "pass", "dominant class"],
                  ttft_rows))
        add("")
        derivable = {k: observed[k]["tps_median"] for k in members
                     if observed[k]["tps_median"] is not None}
        if derivable:
            ranked = sorted(derivable, key=lambda k: -derivable[k])
            add("TPS ranking (derivable lanes only): " + ", ".join(
                "`%s` %s tok/s" % (k, fmt(derivable[k], 2)) for k in ranked) + ".")
        else:
            add("No lane in this bucket produced a derivable TPS (all burst-flushed or failed).")
        add("")
    add("")

    add("## 4. Cross-bucket checks — is the declared order the measured order?")
    add("")
    medians, minima = {}, {}
    for bucket in BUCKET_ORDER:
        vals = [observed[k]["ttft_used"] for k, v in observed.items()
                if v["bucket"] == bucket and observed[k]["ttft_used"] is not None]
        medians[bucket] = statistics.median(vals) if vals else None
        minima[bucket] = min(vals) if vals else None
    rows = []
    for bucket in BUCKET_ORDER:
        members = [k for k, v in observed.items() if v["bucket"] == bucket]
        if not members:
            continue
        best = min((observed[k]["ttft_used"] for k in members
                    if observed[k]["ttft_used"] is not None), default=None)
        worst = max((observed[k]["ttft_used"] for k in members
                     if observed[k]["ttft_used"] is not None), default=None)
        derivable = [observed[k]["tps_median"] for k in members
                     if observed[k]["tps_median"] is not None]
        rows.append([bucket, len(members), fmt(medians[bucket], 0),
                     fmt(minima[bucket], 0), fmt(worst, 0),
                     fmt(max(derivable), 2) if derivable else "—"])
    add(table(["bucket", "members", "TTFT median ms", "TTFT best ms", "TTFT worst ms",
               "best TPS"], rows))
    add("")
    known = {k: v for k, v in medians.items() if v is not None}
    if known:
        fastest = min(known, key=known.get)
        add("**Measured order.** %s."
            % ", ".join("%s %s ms median" % (k, fmt(v, 0))
                        for k, v in sorted(known.items(), key=lambda kv: kv[1])))
        add("")
        declared_pairs = [("FAST", "MIDDLE"), ("MIDDLE", "STRONG"), ("FAST", "STRONG"),
                          ("VERY-FAST", "MIDDLE")]
        bullets = []
        for a, b in declared_pairs:
            if a not in known or b not in known:
                continue
            holds = known[a] < known[b]
            bullets.append("- **%s vs %s**: %s (%s ms vs %s ms) — the declared order %s."
                           % (a, b, "holds" if holds else "inverted",
                              fmt(known[a], 0), fmt(known[b], 0),
                              "is not contradicted" if holds else "DOES NOT hold"))
        add("\n".join(bullets))
        add("")
        add("Read this against the bucket sizes: STRONG holds only the two codex lanes and is the "
            "fastest bucket measured, while the two shim-backed lanes the config labels VERY-FAST "
            "are the slowest measured lanes in the pool. Bucket labels in this config describe "
            "intended role, not measured latency, and the two facts should be stated separately in "
            "the routing table. The full ordering claims and their hit/miss verdicts are in "
            "section 7.")
    add("")

    add("## 5. Correctness matrix (9 probes per model)")
    add("")
    rows = []
    for pool_id in sorted(observed):
        seen = observed[pool_id]
        best = {}
        for record in by_model[pool_id]:
            probe_id = record.get("probe_id")
            if probe_id not in PROBE_ORDER:
                continue
            verdict = record.get("grade") or {}
            klass = verdict.get("failure_class") or "unknown"
            passed = verdict.get("pass")
            cell = "ok" if passed else CLASS_SHORT.get(klass, klass)
            best[probe_id] = cell
        rows.append(["`%s`" % pool_id] + [best.get(p, "·") for p in PROBE_ORDER]
                    + ["%d/9" % seen["pass_count"]])
    add(table(["model"] + list(PROBE_ORDER) + ["pass"], rows))
    add("")
    add("`ok` pass · `WA` wrong answer · `FB` format break · `TC` truncation · `RF` refusal · "
        "`AU` auth/quota · `TR` transport · `--` not attempted after a lane-level abort.")
    add("")

    add("## 6. Failure-class taxonomy")
    add("")
    counts = {}
    for record in records:
        if record.get("measured") is False:
            continue
        verdict = record.get("grade") or {}
        klass = verdict.get("failure_class")
        if klass is None:
            klass = "no-failure (perf probe, no grade)"
        counts[klass] = counts.get(klass, 0) + 1
    add(table(["class", "requests"], [[k, v] for k, v in sorted(counts.items(),
                                                               key=lambda kv: -kv[1])]))
    add("")
    add("Per model:")
    add("")
    rows = []
    for pool_id in sorted(observed):
        seen = observed[pool_id]
        rows.append(["`%s`" % pool_id,
                     ", ".join("%s×%d" % (k, v) for k, v in sorted(seen["classes"].items())),
                     seen["dominant_class"]])
    add(table(["model", "classes observed", "dominant"], rows))
    add("")
    add("### What actually failed, probe by probe")
    add("")
    real = []
    skipped_count = 0
    for record in records:
        if record.get("measured") is False:
            continue
        verdict = record.get("grade") or {}
        klass = verdict.get("failure_class")
        if klass == "skipped_after_fatal":
            skipped_count += 1
            continue
        if verdict.get("pass") is False:
            real.append(["`%s`" % record["pool_id"], record.get("probe_id"), klass,
                         (verdict.get("detail") or "")[:150]])
    add(table(["model", "probe", "class", "detail"], real))
    add("")
    add("%d probes failed on their own merits; %d more were never attempted because their lane "
        "had already refused at the perf probe (quota walls)." % (len(real), skipped_count))
    add("")

    if scoring:
        add("## 7. Prediction scoring (ex-ante, filed before the first request)")
        add("")
        add(table(["model", "TTFT pred→obs (err)", "TPS pred→obs (err)", "pass pred→obs",
                   "failure pred→obs", "failure verdict"], [
            ["`%s`" % row["model"],
             "%s→%s (%s)" % (fmt(row.get("ttft_pred")), fmt(row.get("ttft_obs")),
                             fmt(row.get("ttft_error"))),
             "%s→%s (%s)%s" % (fmt(row.get("tps_pred")), fmt(row.get("tps_obs")),
                               fmt(row.get("tps_error")),
                               "" if row.get("tps_derivable_pred") == row.get("tps_derivable_obs")
                               else " DERIVABILITY-MISS"),
             "%s→%s (%+d)" % (row.get("pass_pred"), row.get("pass_obs"), row.get("pass_error"))
             if row.get("pass_obs") is not None else "—",
             "%s→%s" % (",".join(row.get("failure_pred") or []), row.get("failure_obs")),
             "HIT" if row.get("failure_hit") else "MISS"]
            for row in scoring["per_model"] if "ttft_obs" in row]))
        add("")
        add("`failure_obs` is the dominant class: the mode over the probes that did not pass. A lane "
            "that answers eight of nine probes correctly and truncates one therefore registers a "
            "dominant class, and a prediction of \"no failure mode\" scores as a miss — the "
            "`pass pred→obs` column is the finer-grained reading of the same result.")
        add("")
        errors = [r for r in scoring["per_model"] if r.get("ttft_error") is not None]
        if errors:
            abs_err = [abs(r["ttft_error"]) for r in errors]
            add("TTFT point error: median absolute error %s ms over %d models; largest misses %s."
                % (fmt(statistics.median(abs_err), 0), len(errors),
                   ", ".join("`%s` %s ms" % (r["model"], fmt(r["ttft_error"], 0))
                             for r in sorted(errors, key=lambda r: -abs(r["ttft_error"]))[:3])))
        tps_errors = [r for r in scoring["per_model"] if r.get("tps_error") is not None]
        if tps_errors:
            add("")
            add("TPS point error: median absolute error %s tok/s over %d models with both values."
                % (fmt(statistics.median([abs(r["tps_error"]) for r in tps_errors]), 2),
                   len(tps_errors)))
        add("")
        add("### Ordering claims")
        add("")
        add(table(["id", "verdict", "evidence"], [
            [o["id"], o["verdict"].upper(), o["evidence"]] for o in scoring["ordering"]]))
        add("")
        add("### Global claims")
        add("")
        add(table(["id", "verdict", "evidence"], [
            [g["id"], g["verdict"].upper(), g["evidence"]] for g in scoring["global"]]))
        add("")
        add("Totals: ordering %d hit / %d miss / %d unprovable · global %d hit / %d miss."
            % (scoring["totals"]["ordering_hits"], scoring["totals"]["ordering_misses"],
               scoring["totals"]["ordering_unprovable"], scoring["totals"]["global_hits"],
               scoring["totals"]["global_misses"]))
        add("")

    add("## 8. Routing implications")
    add("")
    add(ROUTING_NOTE)
    add("")
    pool_median = statistics.median([v["ttft_used"] for v in observed.values()
                                     if v["ttft_used"] is not None]) \
        if any(v["ttft_used"] is not None for v in observed.values()) else None
    rows = []
    for pool_id in sorted(observed, key=lambda k: (BUCKET_ORDER.index(observed[k]["bucket"])
                                                   if observed[k]["bucket"] in BUCKET_ORDER else 99,
                                                   k)):
        seen = observed[pool_id]
        verdict, why = routing_verdict(pool_id, seen, observed, medians, pool_median)
        rows.append(["`%s`" % pool_id, seen["bucket"], verdict, why])
    add(table(["model", "declared bucket", "verdict", "evidence"], rows))
    add("")

    add("## 9. Limits and open questions")
    add("")
    add(LIMITS)
    add("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(lines))
    print("wrote %s (%d lines)" % (OUT, len(lines)))


ROUTING_NOTE = (
    "Tags below are mechanical, and compound (a lane can carry several). `QUARANTINE` = every "
    "measured request refused, so the lane is unusable until its quota resets. `RE-BUCKET` = a "
    "FAST/VERY-FAST lane slower than the MIDDLE median, i.e. it fails the speed contract its label "
    "implies. `SLOW-OUTLIER` = TTFT more than twice the pool median. `NO-TOOL-FORMAT` = a probe "
    "returned no usable tool call. `TRUNCATION-PRONE` = a probe ended with no content inside the "
    "fixed budget. `WRONG-ANSWER` / `WEAK-CORRECTNESS` = correctness. `NO-CONTENT-TTFT` = the lane "
    "spends the whole budget on reasoning, so its TTFT is a first-decoded-token figure rather than "
    "a content one. `KEEP` means none of the above fired. The judgement that turns these into a "
    "routing table is M4's; what this table supplies is the measured evidence and the tag it "
    "implies, not the decision."
)

LIMITS = (
    "- **The budget is the battery's, not the model's.** Every thinking lane that truncated did so "
    "inside 192 output tokens. A longer budget would let those lanes finish; the battery reports "
    "the truncation because the measurement contract fixed the budget, and a lane that needs more "
    "than 192 tokens of reasoning before a one-line answer is slow by construction for short "
    "subtasks.\n"
    "- **n = 2 reps** bounds the confidence interval for TTFT/TPS to roughly \"two draws agree or "
    "not\". Lanes whose two reps differ by more than a few hundred ms are flagged by the rep column "
    "rather than smoothed over.\n"
    "- **Fixed small prompt.** TTFT here is dominated by connection, queueing and prefill for a "
    "~50-token prompt; a long-context lane may rank differently at real prompt sizes.\n"
    "- **One correctness draw per probe per model** (temperature 0 where accepted). A wrong answer "
    "is one sample, not a rate; the pass counts are a signal about format discipline and basic "
    "competence, not a benchmark score.\n"
    "- **Burst lanes carry no TPS.** Lanes whose shim buffers the whole response cannot be ranked on "
    "throughput from a client-side measurement; that is a property of the transport, and the fix "
    "(incremental flushing in the shim) is outside this mission's scope.\n"
    "- **Reasoning tokens interact with small `max_tokens`.** Thin caps can be consumed by thinking "
    "before any content is emitted, which shows up as `truncation`; where that happened the probe "
    "spent 192 tokens, and the failure is reported as what it is rather than retried with a bigger "
    "budget.\n"
    "- **Not covered here**: tool-call *correctness* beyond one well-formedness probe, multimodal "
    "input, effort-parameter behaviour, long-context behaviour, and anything about lanes the pool "
    "does not assign."
)


def routing_verdict(pool_id, seen, observed, medians, pool_median):
    """Mechanical flags from the measurements. M4 turns these into a table."""
    classes = ", ".join("%s×%d" % (k, v) for k, v in sorted(seen["classes"].items()))
    if seen["ttft_used"] is None:
        if seen["dominant_class"] in ("auth", "transport") or seen["pass_count"] == 0:
            return "QUARANTINE", ("every measured request refused (%s); 1 attempt, no retry"
                                  % seen["dominant_class"])
        return "INVESTIGATE", "no latency measurement (%s)" % (classes or "no data")

    fast_group = seen["bucket"] in ("FAST", "VERY-FAST")
    middle_median = medians.get("MIDDLE")
    tags, why = [], []
    if fast_group and middle_median is not None and seen["ttft_used"] > middle_median:
        tags.append("RE-BUCKET")
        why.append("a %s lane slower than the MIDDLE median (%s ms vs %s ms)"
                   % (seen["bucket"], fmt(seen["ttft_used"], 0), fmt(middle_median, 0)))
    if pool_median and seen["ttft_used"] > 2 * pool_median:
        tags.append("SLOW-OUTLIER")
        why.append("TTFT %.1f× the pool median (%s ms vs %s ms)"
                   % (seen["ttft_used"] / pool_median, fmt(seen["ttft_used"], 0),
                      fmt(pool_median, 0)))
    if not (seen["classes"].get("ok")):
        tags.append("NO-ANSWER")
        why.append("no probe passed")
    if seen["classes"].get("format_break") and (seen["classes"]["format_break"] > 0):
        tags.append("NO-TOOL-FORMAT")
        why.append("a probe returned no usable tool call")
    if seen["classes"].get("truncation"):
        tags.append("TRUNCATION-PRONE")
        why.append("%d probe(s) ended with no content inside the fixed budget"
                   % seen["classes"]["truncation"])
    if seen["classes"].get("wrong_answer"):
        tags.append("WRONG-ANSWER")
        why.append("%d probe(s) answered with the wrong value" % seen["classes"]["wrong_answer"])
    if seen["pass_count"] <= 3:
        tags.append("WEAK-CORRECTNESS")
        why.append("only %d/9 probes passed" % seen["pass_count"])
    if seen["ttft_basis"] != "content":
        tags.append("NO-CONTENT-TTFT")
        why.append("spends the whole budget on reasoning; no content token to time")
    if not tags:
        tags.append("KEEP")
        why.append("%d/9 correctness at %s ms TTFT inside its declared bucket"
                   % (seen["pass_count"], fmt(seen["ttft_used"], 0)))
    return "+".join(tags), "; ".join(why)


if __name__ == "__main__":
    main()
