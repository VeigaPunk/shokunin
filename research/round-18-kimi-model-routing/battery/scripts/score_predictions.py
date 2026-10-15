#!/usr/bin/env python3
"""Score the ex-ante predictions against the measured battery.

    python3 scripts/score_predictions.py

Reads `predictions/PREDICTIONS.json` and the graded captures, then reports, per
model: TTFT point error (predicted minus observed median, ms), TPS point error,
pass-count error out of the 9 correctness probes, and whether the predicted
failure mode is the one that showed up. Ordering and global claims are scored
hit / miss / unprovable. A claim is unprovable when a lane it needs produced no
usable measurement — a quota-dead lane cannot lose a latency race.
"""
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402

CORRECTNESS_IDS = ("c1", "c2", "c3", "c4", "c5", "k1", "k2", "k3", "t1")
BUCKETS = ("FAST", "MIDDLE", "STRONG")
PREDICTION_FAILURE_MAP = {
    "transport (devin cold start, first request blocks)": "transport",
    "transport (devin cold start, first request blocks); format_break (tool probe: lane is annotated CHAT-ONLY)": "transport",
    "format_break (tool probe: lane is annotated CHAT-ONLY)": "format_break",
    "format_break (tool probe: capabilities declare no tool_use)": "format_break",
    "truncation (always_thinking lane may spend the whole correctness budget on reasoning)": "truncation",
    "truncation (thinking lane)": "truncation",
    "truncation (always_thinking: census sec.5 hyper row returned finish_reason=length on an 8-token cap)": "truncation",
    "auth (429 insufficient_quota on the first request; remainder skipped)": "auth",
}


def prediction_class(text):
    if text in PREDICTION_FAILURE_MAP:
        return PREDICTION_FAILURE_MAP[text]
    low = (text or "").lower()
    for name in ("transport", "auth", "refusal", "truncation", "format_break",
                 "wrong_answer"):
        if name in low:
            return name
    return "none"


def measured(records):
    out = {}
    for record in records:
        if record.get("measured") is False:
            continue
        out.setdefault(record["pool_id"], []).append(record)
    return out


def summarize(by_model):
    summary = {}
    for pool_id, records in by_model.items():
        perf = [r for r in records if r.get("probe_id") == "perf" and r.get("status") == 200]
        ttfts = [r["ttft_content_ms"] for r in perf if r.get("ttft_content_ms") is not None]
        firsts = [r["first_decoded_ms"] for r in perf if r.get("first_decoded_ms") is not None]
        tpss = [r["tps"] for r in perf if r.get("tps") is not None]
        correctness = [r for r in records if r.get("probe_id") in CORRECTNESS_IDS]
        passed = sum(1 for r in correctness if (r.get("grade") or {}).get("pass"))
        classes = [((r.get("grade") or {}).get("failure_class") or "unknown")
                   for r in correctness]
        request_classes = [((r.get("grade") or {}).get("failure_class"))
                           for r in records if (r.get("grade") or {}).get("request_level")]
        failing = [c for c in classes if c not in ("ok", "skipped_after_fatal")]
        if request_classes and all(c in ("auth", "transport", "skipped_after_fatal")
                                  for c in classes):
            dominant = request_classes[0]
        elif failing:
            dominant = statistics.mode(failing)
        else:
            dominant = "none"
        content_median = round(statistics.median(ttfts), 1) if ttfts else None
        first_median = round(statistics.median(firsts), 1) if firsts else None
        # The operator's TTFT is a content token. An always-thinking lane can
        # spend the whole fixed budget on reasoning and never emit one, so the
        # ranking metric falls back to the first token of any kind and every row
        # states which basis it used.
        if content_median is not None:
            used, basis = content_median, "content"
        elif first_median is not None:
            used, basis = first_median, "first_decoded(reasoning-first)"
        else:
            used, basis = None, "none"
        summary[pool_id] = {
            "bucket": records[0].get("bucket"),
            "ttft_median": content_median,
            "ttft_reps": ttfts,
            "ttft_reasoning_median": round(statistics.median([r["ttft_reasoning_ms"]
                                                              for r in perf
                                                              if r.get("ttft_reasoning_ms") is not None]), 1)
            if any(r.get("ttft_reasoning_ms") is not None for r in perf) else None,
            "ttft_first_median": first_median,
            "ttft_used": used,
            "ttft_basis": basis,
            "tps_median": round(statistics.median(tpss), 2) if tpss else None,
            "tps_reps": tpss,
            "pass_count": passed,
            "graded": len(correctness),
            "measured_graded": sum(1 for r in correctness if not r.get("skipped")),
            "dominant_class": dominant,
            "classes": {c: classes.count(c) for c in sorted(set(classes))},
            "prompt_tokens": max([r.get("prompt_tokens") or 0 for r in perf] or [0]),
            "incremental": any(stream_mode(r) == "incremental" for r in perf),
            "burst": any(stream_mode(r) == "burst" for r in perf),
            "stream_modes": [stream_mode(r) for r in perf],
            "statuses": sorted({r.get("status") for r in records
                                if r.get("status") is not None}),
        }
    return summary


def stream_mode(record):
    """How a lane delivered its stream, counting reasoning deltas as deltas.

    A thinking lane that streams 254 reasoning deltas and no content is
    incremental, not silent; conflating the two would label it 'no deltas'
    while its TPS was still derivable from the same stream.
    """
    deltas = (record.get("content_delta_count") or 0) + (record.get("reasoning_delta_count") or 0)
    span = record.get("decode_span_ms")
    if not deltas:
        return "no-deltas"
    if span is None or span < 50:
        return "burst"
    return "incremental"


def argmin(keys, values, want_min=True):
    present = [(k, values[k]) for k in keys if values.get(k) is not None]
    if not present:
        return None
    return (min if want_min else max)(present, key=lambda kv: kv[1])[0]


def score_ordering(observed, preds, by_model):
    ttft = {k: v["ttft_used"] for k, v in observed.items()}
    tps = {k: v["tps_median"] for k, v in observed.items()}
    all_ids = list(observed)
    fast = [k for k, v in observed.items() if v["bucket"] in ("FAST", "VERY-FAST")]
    middle = [k for k, v in observed.items() if v["bucket"] == "MIDDLE"]
    strong = [k for k, v in observed.items() if v["bucket"] == "STRONG"]

    def cmp_lt(a, b):
        if ttft.get(a) is None or ttft.get(b) is None:
            return None
        return ttft[a] < ttft[b]

    def fastest(keys):
        return argmin(keys, ttft, True)

    def slowest(keys):
        return argmin(keys, ttft, False)

    def median_of(keys):
        vals = [ttft[k] for k in keys if ttft.get(k) is not None]
        return statistics.median(vals) if vals else None

    results = []

    def add(claim_id, verdict, evidence):
        results.append({"id": claim_id, "verdict": verdict, "evidence": evidence})

    idx = {c["id"]: c for c in preds["ordering_claims"]}

    def verdict_from(claim_id, outcome, evidence):
        if outcome is None:
            add(claim_id, "unprovable", evidence)
        elif outcome == idx[claim_id]["expect"]:
            add(claim_id, "hit", evidence)
        else:
            add(claim_id, "miss", evidence)

    a, b = "cascade/deepseek-v4.1-flash", "cursor/composer-2.5"
    verdict_from("O1", cmp_lt(a, b), "%s=%s ms, %s=%s ms" % (a, ttft.get(a), b, ttft.get(b)))
    f_fast = fastest(fast)
    verdict_from("O2", None if f_fast is None else (f_fast == "hyper/deepseek-v4.1-flash"),
                 "fastest FAST by TTFT: %s" % f_fast)
    s_fast = slowest(fast)
    verdict_from("O3", None if s_fast is None else (s_fast == "cascade/glm-5.3-flash"),
                 "slowest FAST by TTFT: %s" % s_fast)
    f_mid = fastest(middle)
    verdict_from("O4", None if f_mid is None else (f_mid == "xai-oauth/grok-4.5"),
                 "fastest MIDDLE by TTFT: %s" % f_mid)
    s_mid = slowest(middle)
    verdict_from("O5", None if s_mid is None else (s_mid == "alibaba-token-plan/qwen3.8-flash"),
                 "slowest MIDDLE by TTFT: %s" % s_mid)
    c1, c2 = "openai-codex/gpt-6.1-sol", "openai-codex/gpt-6.1-sol-high"
    verdict_from("O6", cmp_lt(c1, c2), "%s=%s ms, %s=%s ms" % (c1, ttft.get(c1), c2, ttft.get(c2)))
    fastest_fast = fastest(fast)
    if fastest_fast is None or not (middle or strong):
        add("O7", "unprovable", "no cross-bucket pair with two measurements")
    else:
        verdict_from("O7", ttft.get(fastest_fast) < min(
            [ttft[k] for k in middle + strong if ttft.get(k) is not None] or [float("inf")]),
            "fastest FAST %s=%s ms vs fastest MIDDLE/STRONG %s"
            % (fastest_fast, ttft.get(fastest_fast),
               argmin(middle + strong, ttft, True)))
    fastest_mid, fastest_strong = fastest(middle), fastest(strong)
    if fastest_mid is None or fastest_strong is None:
        add("O8", "unprovable", "one bucket has no TTFT measurement")
    else:
        verdict_from("O8", ttft[fastest_mid] < ttft[fastest_strong],
                     "%s=%s ms vs %s=%s ms" % (fastest_mid, ttft[fastest_mid],
                                               fastest_strong, ttft[fastest_strong]))
    med_fast, med_mid = median_of(fast), median_of(middle)
    if med_fast is None or med_mid is None:
        add("O9", "unprovable", "a bucket has no TTFT measurement")
    else:
        verdict_from("O9", med_fast < med_mid,
                     "FAST median %s ms vs MIDDLE median %s ms" % (med_fast, med_mid))
    if ttft.get("cascade/glm-5.3-flash") is None or not (middle or strong):
        add("O10", "unprovable", "no TTFT for the devin-class lane or no cross-bucket pair")
    else:
        others = [ttft[k] for k in middle + strong if ttft.get(k) is not None]
        verdict_from("O10", (not others) or ttft["cascade/glm-5.3-flash"] > max(others)
                     if others else None,
                     "cascade/glm-5.3-flash=%s ms vs slowest MIDDLE/STRONG %s=%s ms"
                     % (ttft.get("cascade/glm-5.3-flash"),
                        argmin(middle + strong, ttft, False),
                        ttft.get(argmin(middle + strong, ttft, False) or "")))
    top_tps = argmin(all_ids, tps, False)
    verdict_from("O11", None if top_tps is None else (top_tps == "xai-oauth/grok-4.5"),
                 "highest derivable TPS: %s (%s)" % (top_tps, tps.get(top_tps or "")))
    p1, p2 = "alibaba-token-plan/deepseek-v4.1-flash", "alibaba-token-plan/qwen3.8-flash"
    if tps.get(p1) is None or tps.get(p2) is None:
        add("O12", "unprovable", "TPS not derivable on one side (%s=%s, %s=%s)"
            % (p1, tps.get(p1), p2, tps.get(p2)))
    else:
        verdict_from("O12", tps[p1] > tps[p2],
                     "%s=%s vs %s=%s tok/s" % (p1, tps[p1], p2, tps[p2]))
    stable = True
    evidence = []
    for pool_id, value in observed.items():
        reps = [r for r in by_model[pool_id]
                if r.get("probe_id") == "perf" and r.get("status") == 200]
        if len(reps) < 2:
            continue
        flags = [stream_mode(r) for r in reps]
        if len(set(flags)) > 1:
            stable = False
            evidence.append("%s: %s" % (pool_id, flags))
    verdict_from("O13", stable, "; ".join(evidence) or "every lane kept one streaming mode")
    if tps.get(c1) is None or tps.get(c2) is None:
        add("O14", "unprovable", "TPS not derivable on one side")
    else:
        spread = abs(tps[c1] - tps[c2]) / min(tps[c1], tps[c2])
        verdict_from("O14", spread <= 0.25, "spread %.0f%% (%.2f vs %.2f tok/s)"
                     % (spread * 100, tps[c1], tps[c2]))
    return results


def score_global(observed, preds, records):
    results = []

    def add(claim_id, outcome, evidence):
        expect = next(g["expect"] for g in preds["global_claims"] if g["id"] == claim_id)
        verdict = "hit" if outcome == expect else "miss"
        results.append({"id": claim_id, "verdict": verdict, "expect": expect,
                        "observed": outcome, "evidence": evidence})

    answered = [k for k, v in observed.items() if any(
        r.get("status") == 200 and (r.get("content") or r.get("tool_calls"))
        for r in records if r["pool_id"] == k)]
    add("G1", len(answered) == len(observed),
        "%d of %d models answered something (silent: %s)"
        % (len(answered), len(observed),
           sorted(set(observed) - set(answered))))
    ttft = {k: v["ttft_median"] for k, v in observed.items()}
    medians = {}
    for bucket in BUCKETS:
        vals = [ttft[k] for k, v in observed.items()
                if v["bucket"] == bucket and ttft.get(k) is not None]
        medians[bucket] = statistics.median(vals) if vals else None
    known = {k: v for k, v in medians.items() if v is not None}
    fastest_bucket = min(known, key=known.get) if known else None
    add("G2", fastest_bucket == "FAST",
        "bucket TTFT medians: %s -> fastest %s" % (
            {k: round(v, 1) if v is not None else None for k, v in medians.items()},
            fastest_bucket))
    bursts = [k for k, v in observed.items() if v["burst"] and not v["incremental"]]
    add("G3", len(bursts) >= 3, "lanes whose stats are burst-only: %d %s"
        % (len(bursts), sorted(bursts)))
    codex_ok = all(any(r.get("status") == 200 for r in records
                       if r["pool_id"] == model)
                   for model in ("openai-codex/gpt-6.1-sol", "openai-codex/gpt-6.1-sol-high"))
    add("G4", codex_ok, "codex models answering 200: %s" % codex_ok)
    overhead = max([v["prompt_tokens"] for k, v in observed.items()
                    if k == "cascade/glm-5.3-flash"] or [0])
    add("G5", overhead > 10000, "cascade/glm-5.3-flash max prompt_tokens %s" % overhead)
    tool_4xx = [k for k, v in observed.items() if any(
        r.get("status") and r.get("status") >= 400 for r in records
        if r["pool_id"] == k and r.get("probe_id") == "t1")]
    add("G6", bool(tool_4xx), "lanes rejecting the tool probe with HTTP >=400: %s" % tool_4xx)
    return results


def main():
    with open(os.path.join(common.BATTERY_DIR, "predictions",
                           "PREDICTIONS.json")) as fh:
        preds = json.load(fh)
    records = grade.load_records()
    by_model = measured(records)
    observed = summarize(by_model)
    per_model = []
    for pool_id, prediction in preds["predictions"].items():
        seen = observed.get(pool_id)
        if seen is None:
            per_model.append({"model": pool_id, "note": "not measured"})
            continue
        row = {
            "model": pool_id, "bucket": seen["bucket"],
            "ttft_pred": prediction["ttft_ms"], "ttft_obs": seen["ttft_used"],
            "ttft_obs_basis": seen["ttft_basis"],
            "ttft_error": (None if prediction["ttft_ms"] is None or seen["ttft_used"] is None
                           else round(prediction["ttft_ms"] - seen["ttft_used"], 1)),
            "ttft_in_range": (None if prediction["ttft_range_ms"] is None
                              or seen["ttft_used"] is None
                              else prediction["ttft_range_ms"][0] <= seen["ttft_used"]
                              <= prediction["ttft_range_ms"][1]),
            "tps_pred": prediction["tps"], "tps_obs": seen["tps_median"],
            "tps_error": (None if prediction["tps"] is None or seen["tps_median"] is None
                          else round(prediction["tps"] - seen["tps_median"], 2)),
            "tps_derivable_pred": prediction["tps_derivable"],
            "tps_derivable_obs": seen["tps_median"] is not None,
            "pass_pred": prediction["pass_count"], "pass_obs": seen["pass_count"],
            "pass_error": prediction["pass_count"] - seen["pass_count"],
            "pass_range_hit": prediction["pass_range"][0] <= seen["pass_count"]
                              <= prediction["pass_range"][1],
            "failure_pred": [prediction_class(f) for f in prediction["failure_modes"]]
                            or ["none"],
            "failure_obs": seen["dominant_class"],
            "failure_hit": (seen["dominant_class"] in
                            ([prediction_class(f) for f in prediction["failure_modes"]] or ["none"])
                            or (seen["dominant_class"] == "none"
                                and not prediction["failure_modes"])),
            "observed": seen,
        }
        per_model.append(row)
    report = {
        "scored_at_utc": None,
        "config_sha256": preds["config_sha256"],
        "per_model": per_model,
        "ordering": score_ordering(observed, preds, by_model),
        "global": score_global(observed, preds, records),
    }
    report["totals"] = {
        "models_scored": sum(1 for r in per_model if "ttft_obs" in r),
        "ttft_point_errors_ms": [r["ttft_error"] for r in per_model
                                 if r.get("ttft_error") is not None],
        "tps_point_errors": [r["tps_error"] for r in per_model
                             if r.get("tps_error") is not None],
        "pass_point_errors": [r["pass_error"] for r in per_model if "pass_error" in r],
        "ordering_hits": sum(1 for o in report["ordering"] if o["verdict"] == "hit"),
        "ordering_misses": sum(1 for o in report["ordering"] if o["verdict"] == "miss"),
        "ordering_unprovable": sum(1 for o in report["ordering"]
                                   if o["verdict"] == "unprovable"),
        "global_hits": sum(1 for g in report["global"] if g["verdict"] == "hit"),
        "global_misses": sum(1 for g in report["global"] if g["verdict"] == "miss"),
    }
    common.write_json(os.path.join(common.RAW_DIR, "prediction-scoring.json"), report)
    print("scored %d models" % report["totals"]["models_scored"])
    print("ordering: %d hit / %d miss / %d unprovable"
          % (report["totals"]["ordering_hits"], report["totals"]["ordering_misses"],
             report["totals"]["ordering_unprovable"]))
    print("global: %d hit / %d miss"
          % (report["totals"]["global_hits"], report["totals"]["global_misses"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
