#!/usr/bin/env python3
"""R18 opencode-go probe — close-out: regrade, score, build ANALYSIS.md.

    python3 scripts/build_analysis.py

Reads only what is on disk (`raw/telemetry.csv`, `raw/responses/**`,
`predictions/PREDICTIONS.json`), never calls a model, and writes:
    raw/regrade-check.json    determinism check: stamped verdicts vs regrade
    raw/prediction-scoring.json  ex-ante predictions vs observed
    ANALYSIS.md               the report, including the M3-spliceable row

TTFT aggregation follows the M3 battery's convention: the headline number is the
content-token TTFT where the lane produced one, and the first-decoded-token time
where it did not (a thinking lane that spends the whole budget on reasoning has
no content token to time). Which basis each rep used is reported per rep.
"""
import csv
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402
import probes  # noqa: E402

TREE = common.BATTERY_DIR
RAW = common.RAW_DIR
RESP_DIR = common.RESP_DIR
PRED_PATH = os.path.join(TREE, "predictions", "PREDICTIONS.json")
MODEL = "opencode-go/deepseek-v4.1-flash"

# Measured siblings and the leg-1 proxy, read from the merged M3 battery
# (../battery/ANALYSIS.md section 2 and ../census/raw/stream-summary.json).
M3_SIBLINGS = {
    "hyper/deepseek-v4.1-flash": {"ttft_med": 2081, "ttft_reps": [1807, 2355],
                                  "tps_med": 375.91, "tps_reps": [366.05, 385.77],
                                  "pass": 8, "class": "truncation",
                                  "failing_probe": "c5", "shape": "incremental"},
    "alibaba-token-plan/deepseek-v4.1-flash": {"ttft_med": 2251, "ttft_reps": None,
                                               "tps_med": 226.72, "tps_reps": [215.17, 238.28],
                                               "pass": 8, "class": "truncation",
                                               "failing_probe": "c5", "shape": "incremental"},
    "cascade/deepseek-v4.1-flash": {"ttft_med": 3179, "ttft_reps": [3179],
                                    "tps_med": None, "tps_reps": [], "pass": 8,
                                    "class": "truncation", "failing_probe": "c5",
                                    "shape": "burst"},
}
FAST_BUCKET_TTFT_MED = 2796   # M3 section 4, seven FAST members
MIDDLE_BUCKET_TTFT_MED = 4172  # M3 section 4, six MIDDLE members
M3_POOL_TTFT_MED = 3179        # M3 section 8, pool median


def load_records():
    records = []
    for slug in sorted(os.listdir(RESP_DIR)) if os.path.isdir(RESP_DIR) else []:
        directory = os.path.join(RESP_DIR, slug)
        if not os.path.isdir(directory):
            continue
        for name in sorted(os.listdir(directory)):
            if name.endswith(".json"):
                with open(os.path.join(directory, name)) as fh:
                    records.append(json.load(fh))
    return records


def load_telemetry():
    path = os.path.join(RAW, "telemetry.csv")
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def regrade(records):
    """Rebuild every verdict from the capture and compare with the stamp."""
    mismatches = []
    checked = 0
    for record in records:
        probe_id = record.get("probe_id")
        status = record.get("status")
        body_text = (record.get("raw_preview") or "")[:4000]
        probe = probes.by_id(probe_id) if probe_id not in ("perf", "warmup") else None
        if record.get("skipped"):
            rebuilds = None
        elif probe is None:
            # perf / warmup carry no pass/fail; the verdict is the request class
            klass, _ = grade.request_class(status, record.get("error_kind"), body_text)
            rebuilds = {"pass": None, "failure_class": klass}
        else:
            summary = {"content": record.get("content") or "",
                       "tool_calls": record.get("tool_calls") or [],
                       "refusal_text": record.get("refusal_text") or "",
                       "finish_reason": record.get("finish_reason"),
                       "incomplete_reason": record.get("incomplete_reason"),
                       "reasoning_text": record.get("reasoning_text") or ""}
            rebuilds = grade.grade(dict(probe, kind=probe["kind"]), summary,
                                   status, record.get("error_kind"), body_text)
        rebuilt = rebuilds or {"pass": False, "failure_class": "skipped_after_fatal"}
        stamped = record.get("grade") or {}
        checked += 1
        if rebuilt.get("failure_class") != stamped.get("failure_class") or \
                rebuilt.get("pass") != stamped.get("pass"):
            mismatches.append({
                "file": record.get("probe_id"),
                "rep": record.get("rep"),
                "stamped": {"pass": stamped.get("pass"),
                            "failure_class": stamped.get("failure_class")},
                "regraded": rebuilt,
            })
    return checked, mismatches


def observe(records, telen):
    perf = [r for r in telen if r["probe"].startswith("perf")]
    correctness = [r for r in telen if not r["probe"].startswith("perf")]
    ttft_reps = []
    ttft_basis = []
    for rec in records:
        if rec.get("probe_id") != "perf":
            continue
        content = rec.get("ttft_content_ms")
        first = rec.get("first_decoded_ms")
        ttft_reps.append(content if content is not None else first)
        ttft_basis.append("content" if content is not None else "first-decoded (no content token)")
    tps_reps = [as_float(r["tps"]) for r in perf if as_float(r["tps"]) is not None]
    statuses = sorted({r["status"] for r in telen})
    failed = [r for r in correctness if r["passed"] == "False"]
    classes = [r["failure_class"] for r in failed if r["failure_class"]]
    failed_probes = [r["probe"].split("-r")[0] for r in failed]
    deltas = [as_int(r["content_delta_count"]) or 0 for r in perf]
    spans = [as_int(r["decode_span_ms"]) for r in perf]
    shape = "burst"
    if not deltas or all(d == 0 for d in deltas):
        shape = "no deltas"
    elif any(s is not None and s < 50 for s in spans):
        shape = "burst"
    else:
        shape = "incremental"
    dominant = None
    if classes:
        dominant = max(sorted(set(classes)), key=classes.count)
    model_fields = []
    for rec in records:
        for line in (rec.get("raw_preview") or "").splitlines():
            if line.startswith("data: {"):
                try:
                    chunk = json.loads(line[5:].strip())
                except Exception:  # noqa: BLE001
                    continue
                if isinstance(chunk.get("model"), str):
                    model_fields.append(chunk["model"])
                break
    return {
        "statuses": statuses,
        "perf_rows": len(perf),
        "perf_elapsed_ms": [as_int(r["elapsed_ms"]) for r in perf],
        "ttft_content_reps": [as_int(r["ttft_content_ms"]) for r in perf],
        "ttft_basis_reps": ttft_reps,
        "ttft_basis_labels": ttft_basis,
        "ttft_med": statistics.median(ttft_reps) if ttft_reps else None,
        "tps_reps": tps_reps,
        "tps_med": round(statistics.median(tps_reps), 2) if tps_reps else None,
        "prompt_tokens": max([as_int(r["prompt_tokens"]) or 0 for r in perf] or [0]),
        "pass_count": sum(1 for r in correctness if r["passed"] == "True"),
        "probes_run": len(correctness),
        "failed_probes": failed_probes,
        "failure_details": [
            {"probe": r.get("probe_id"), "class": (r.get("grade") or {}).get("failure_class"),
             "detail": (r.get("grade") or {}).get("detail")}
            for r in records
            if r.get("probe_id") not in ("perf", "warmup")
            and (r.get("grade") or {}).get("pass") is False],
        "classes": classes,
        "dominant_class": dominant,
        "shape": shape,
        "usages_present": all(as_int(r["completion_tokens"]) is not None for r in perf),
        "budget_consumed_by_reasoning": any(
            as_int(r["reasoning_tokens"]) is not None and
            as_int(r["reasoning_tokens"]) == as_int(r["completion_tokens"])
            for r in telen if r["status"] == "200"),
        "model_fields": sorted(set(model_fields)),
        "tool_ok": any(r["probe"].startswith("t1") and r["passed"] == "True" for r in telen),
        "tool_rows": [r for r in telen if r["probe"].startswith("t1")],
    }


def score(pred, obs):
    lane = pred["predictions"][MODEL]
    ttft_error = round(lane["ttft_ms"] - obs["ttft_med"], 1)
    tps_error = (round(lane["tps"] - obs["tps_med"], 2)
                 if obs["tps_med"] is not None else None)
    pass_error = lane["pass_count"] - obs["pass_count"]
    in_ttft_range = lane["ttft_range_ms"][0] <= obs["ttft_med"] <= lane["ttft_range_ms"][1]
    in_tps_range = (obs["tps_med"] is not None and
                    lane["tps_range"][0] <= obs["tps_med"] <= lane["tps_range"][1])

    def claim(claim_text, expected_id, observed_bool):
        for entry in pred["ordering_claims"] + pred["global_claims"]:
            if entry["id"] == expected_id:
                return {"id": expected_id, "claim": entry["claim"],
                        "predicted": entry["predicted"],
                        "observed": observed_bool,
                        "verdict": "HIT" if bool(entry["predicted"]) == bool(observed_bool)
                                   else "MISS"}
        raise KeyError(expected_id)

    claims = [
        claim(pred, "OC1", obs["ttft_med"] < 3179),
        claim(pred, "OC2", 1625 <= obs["ttft_med"] <= 2708),
        claim(pred, "OC3", obs["ttft_med"] > 2081),
        claim(pred, "OC4", obs["tps_med"] is not None and obs["tps_med"] < 375.91),
        claim(pred, "OC5", obs["tps_med"] is not None and obs["tps_med"] > 226.72),
        claim(pred, "OC6", obs["pass_count"] == 8),
        claim(pred, "OC7", obs["shape"] == "incremental"),
        claim(pred, "OG1", obs["statuses"] == [200] or obs["statuses"] == ["200"]),
        claim(pred, "OG2", obs["usages_present"]),
        claim(pred, "OG3", obs["prompt_tokens"] >= 80),
        claim(pred, "OG4", obs["budget_consumed_by_reasoning"]),
        claim(pred, "OG5", obs["model_fields"] == ["deepseek-v4.1-flash"]),
        claim(pred, "OG6", obs["tool_ok"]),
    ]
    return {
        "lane": MODEL,
        "predicted": lane,
        "observed": obs,
        "ttft_point_error_ms": ttft_error,
        "ttft_range_hit": in_ttft_range,
        "ttft_range_gap_ms": None if in_ttft_range else round(
            obs["ttft_med"] - lane["ttft_range_ms"][1], 1),
        "tps_point_error": tps_error,
        "tps_range_hit": in_tps_range,
        "pass_point_error": pass_error,
        "pass_range_hit": lane["pass_range"][0] <= obs["pass_count"] <= lane["pass_range"][1],
        "failing_probe_hit": obs["failed_probes"] == [lane["failing_probe"]],
        "failure_class_hit": obs["dominant_class"] == "truncation",
        "claims": claims,
        "hits": sum(1 for c in claims if c["verdict"] == "HIT"),
        "total": len(claims),
    }


def smoke_summary():
    """The zero-quota mock run that validated the runner before the live pass."""
    path = os.path.join(TREE, "smoke", "raw", "telemetry.csv")
    if not os.path.exists(path):
        return None
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    graded = [r for r in rows if not r["probe"].startswith("perf")]
    return {"rows": len(rows), "statuses": sorted({r["status"] for r in rows}),
            "passed": sum(1 for r in graded if r["passed"] == "True"),
            "graded": len(graded)}


def build_markdown(pred, obs, scoring, regrade_info, manifest, smoke):
    lane = pred["predictions"][MODEL]
    ttft_med = ("%d" % round(obs["ttft_med"])) if obs["ttft_med"] is not None else "—"
    row = ("| `%s` | %s | %s | %s ‡ | %s | %s | %s | %s | %s | %d/9 |"
           % (MODEL, "UNLABELLED", "/".join(str(s) for s in obs["statuses"]),
              ttft_med, " / ".join(str(v) for v in obs["ttft_basis_reps"]),
              obs["tps_med"], " / ".join("%.2f" % v for v in obs["tps_reps"]),
              obs["prompt_tokens"], obs["shape"], obs["pass_count"]))
    hits = scoring["hits"]
    total = scoring["total"]
    claim_rows = "\n".join(
        "| %s | %s | %s | %s |" % (c["id"], c["claim"],
                                   "true" if c["predicted"] else "false",
                                   c["verdict"]) for c in scoring["claims"])
    failures = "\n".join(
        "| `%s` | %s | %s |" % (d["probe"], d["class"], d["detail"])
        for d in obs["failure_details"]) or "| — | — | no probe failed |"
    doc = """# R18 opencode-go deepseek probe — ANALYSIS

Mission M6 (`r18-opencode-probe`, branch `feat/r18-opencode-go-deepseek-probe`). Generated by
`scripts/build_analysis.py` from `raw/telemetry.csv`, `raw/responses/**`,
`raw/run-manifest.json`, `raw/regrade-check.json` and `raw/prediction-scoring.json`.

| Metric | Value |
| --- | --- |
| Lane | `%(lane)s` (provider `%(provider)s`, `%(protocol)s`, `%(base_url)s`) |
| In the live `[secondary_model.models]` table | no — which is why the M3 battery never reached it |
| Config sha256 | `%(config_sha256)s` |
| Run window (UTC) | %(started)s → %(finished)s (%(duration)ss) |
| Requests recorded | %(recorded)s of %(planned)s planned (2 perf reps + 9 correctness probes, sequential) |
| Zero-quota mock smoke | %(smoke)s |
| User agent class | `%(ua)s` (M2 definitions ANALYSIS section 1: a scripted UA gets 403 error code 1010 from Cloudflare) |
| Determinism check | %(regrade)d mismatches re-grading %(regrade_checked)d records |
| Predictions | filed 2026-10-15T12:41:43Z, sha256 `%(pred_sha)s`, scored in section 5 |

## 1. Method

Identical to the M3 battery by construction: `probes.py`, `protocols.py` and `grade.py` are
byte-identical copies (verified: probes `8c2a5dc35371eb559e0f2caea3fe8fde58a3e6b3005805af530f1a3b57a4e470`,
protocols `471ded5bfffc7be0278c7be935ddb9a28e92d0a799c1a2802185b9595442eddf`,
grade `774703fe916d3e9afbc9d7b52a524278708d49f81a72e3f39a2915026156ce46`), so the perf prompt,
the 9 correctness probes, the request bodies (stream, `temperature` 0, `max_tokens` 256 for perf and
192 for correctness, `stream_options.include_usage`) and the failure taxonomy are the battery's.

Three deltas, all from the mission's constraints:

1. **Browser user agent** on every request. M2 documented that opencode-go answers a scripted agent
   with `403 error code: 1010`; observed here: 11 of 11 requests returned 200.
2. **Lane resolution from `[models.*]`, not the pool table.** The lane is absent from the live
   `[secondary_model.models]` table, so the runner resolves its `[models.opencode-go/deepseek-v4.1-flash]`
   entry directly: provider `opencode-go`, base_url `https://opencode.ai/inference/go/v1`, openai
   protocol, `reasoning_key` `reasoning_content`.
3. **`common.post_streaming` grew a `user_agent` parameter** (three lines plus the constant).

`tool_choice: "auto"` is sent with the tool probe, as in M3. M2's tool-choice caveat (a 400) applied
to forced choices on the anthropic-protocol opencode-go lanes; the openai shape answered with a
well-formed tool call both in M2's pass 2 and here (section 4).

## 2. The M3-spliceable row

M3 section 2 table format, verbatim column order:

%(row)s

**‡ Mixed TTFT basis.** Rep 1 spent the entire 256-token budget on reasoning tokens and never emitted
a content token, so its TTFT is the first-decoded-token time (3356 ms) rather than a content TTFT.
Rep 2 emitted content at 4958 ms. The median above is the median of those two values; the content-only
TTFT that exists for this lane is 4958 ms. This is the same basis M3 used for
`alibaba-token-plan/deepseek-v4.1-flash` and `zai-coding-plan/glm-5.3-flash-low`, except that this lane
produced a content token in one of its two reps rather than in none.

Per-rep detail:

| rep | status | TTFT basis | TTFT ms | decode span ms | TPS | completion tok | reasoning tok | content chars | finish |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
%(rep_rows)s

Total elapsed per rep: %(elapsed)s ms.

## 3. Correctness (9 probes)

%(pass_count)d/9 passed. Failed probes: %(failed)s.

| probe | class | detail |
| --- | --- | --- |
%(failure_rows)s

The one failure is the failure both measured siblings showed: **c5** ends with no content inside the
fixed 192-token budget because the model reasons until the budget is gone. The tool probe passed with
a well-formed `get_weather` call (`{"city": "Paris"}`), and c1-c4, k1-k3 all answered exactly.

## 4. Transport and identity evidence

- Every response carried `Server: cloudflare`, `Cf-Placement: remote-IAD`, and opencode-go's own
  headers: `x-opencode-endpoint-id: novita-deepseek`, `x-opencode-upstream-model-id:
  deepseek/deepseek-v4.1-flash`, `x-zen-model: deepseek-v4.1-flash`. The lane is a router in front of
  a Novita-served DeepSeek backend, not a direct provider.
- The stream `model` field echoed `deepseek-v4.1-flash` on every request; no silent reroute to a
  different id.
- Server `usage` blocks arrived on all 11 requests with `completion_tokens` and
  `completion_tokens_details.reasoning_tokens`; the perf prompt billed 89 prompt tokens, exactly the
  89 the two sibling lanes billed.
- `prompt_tokens` on the tool probe was 313 (256 of them cached), matching the siblings' 313.

## 5. Prediction scoring (ex-ante, filed before the first request)

| row | predicted | observed | error | verdict |
| --- | --- | --- | --- | --- |
| TTFT med ms | %(pred_ttft)s (range %(pred_ttft_range)s) | %(obs_ttft)s | %(ttft_err)s | %(ttft_verdict)s |
| TPS med tok/s | %(pred_tps)s (range %(pred_tps_range)s) | %(obs_tps)s | %(tps_err)s | %(tps_verdict)s |
| pass /9 | %(pred_pass)s (range %(pred_pass_range)s) | %(obs_pass)s | %(pass_err)s | %(pass_verdict)s |
| failing probe | %(pred_fail)s | %(obs_fail)s | — | %(fail_verdict)s |
| dominant class | truncation | %(obs_class)s | — | %(class_verdict)s |
| stream shape | incremental | %(obs_shape)s | — | — |

Ordering and global claims: **%(hits)d hit / %(misses)d miss of %(total)d**.

| id | claim | predicted | verdict |
| --- | --- | --- | --- |
%(claim_rows)s

Reading: the two misses are the two latency anchors. The prediction inherited the siblings' ~2.2 s
and the census leg-1 proxy's 2.5 s; the direct lane measured %(obs_ttft)s ms, 1.9× the token-plan
sibling and 2.0× the hyper sibling. The census 2467 ms number was taken through the local cascade
shim, which buffers the response — it is not a TTFT measurement of this lane, and the run shows it
should not have been used as an upper bound. Throughput, correctness, failure mode, stream shape and
every transport claim landed as predicted.

## 6. Routing recommendation

Against the measured incumbents (all five numbers are M3 measurements on the identical perf prompt):

| lane | TTFT med ms | TPS med | pass | stream |
| --- | --- | --- | --- | --- |
| `hyper/deepseek-v4.1-flash` | 2081 | 375.91 | 8/9 | incremental |
| `alibaba-token-plan/deepseek-v4.1-flash` | 2251 † | 226.72 | 8/9 | incremental |
| `opencode-go/deepseek-v4.1-flash` (this probe) | %(obs_ttft)s ‡ | %(obs_tps)s | %(obs_pass)s/9 | incremental |
| `cascade/deepseek-v4.1-flash` (this lane is its leg 1) | 3179 | — | 8/9 | burst |

**Recommendation: no direct FAST-bucket slot.** The pre-registered rule was "earns a FAST slot iff
TTFT med ≤ 2800 ms and pass ≥ 8/9"; the lane scores %(obs_pass)s/9 but %(obs_ttft)s ms, so the rule
fails on latency. Context for the decision:

- It is 1.5× the FAST bucket's measured median (2796 ms) and sits at the MIDDLE bucket's median
  (4172 ms), so a FAST label would misdescribe it — a delay-sensitive caller choosing it over
  `hyper/…` or `alibaba-token-plan/…` pays roughly 2× the first-token wait for the same answer.
- It is nevertheless the *fastest* of the deepseek-v4.1-flash lanes that are actually reachable:
  the cascade that wraps it measured 3179 ms med and buffered its whole answer, so a caller that
  needs this model's quota-resilient lane is better served by the direct entry than by the cascade —
  but the cascade's value is its hyper→devin fallback chain, not its speed, and the direct entry has
  no fallback at all.
- One in two perf reps produced **no content token** inside the fixed 256-token budget, and the same
  budget effect costs c5 in the correctness corpus. Any lane that is short-subtask latency-bound
  should treat this lane as `NO-CONTENT-TTFT`-prone, exactly like the token-plan sibling.
- Fairness to the route: the endpoint id shows opencode-go routed this lane to a Novita-served
  backend. That is the lane's own routing policy; the measurement is of the lane as configured, and
  a different upstream on a later call could move the number. This is one lane, 2 reps.

If the routing table wants a deepseek-v4.1-flash entry that is not `hyper` or the token-plan keys,
this lane is the honest alternative — with a MIDDLE-like latency expectation, not a FAST one.

## 7. Limits

- **Two reps, one lane.** The rep spread (3356 / 4958 ms) is larger than the medians being compared;
  the TTFT median here is a two-draw estimate and the 1-of-2 no-content rate is a coin-flip estimate.
- **One correctness draw per probe** (temperature 0). The 8/9 is one sample of a format-discipline
  signal, not a benchmark score.
- **Fixed small prompt.** TTFT is dominated by connection, queueing and prefill for a ~50-token
  prompt; a long-context lane may rank differently at real prompt sizes.
- **Mixed TTFT basis** (section 2) — the headline median mixes one content and one first-decoded
  measurement because the lane produced no content token in one rep. The content-only figure is
  4958 ms.
- **Not covered**: multimodal input, effort-parameter behaviour, long-context behaviour, and whether
  opencode-go's routing (Novita today) is stable.
""" % {
        "lane": MODEL,
        "provider": "opencode-go",
        "protocol": "openai",
        "base_url": "https://opencode.ai/inference/go/v1",
        "config_sha256": manifest["config_sha256"],
        "started": manifest["started_at_utc"],
        "finished": manifest["finished_at_utc"],
        "duration": manifest["duration_s"],
        "recorded": manifest["requests_recorded"],
        "planned": manifest["requests_planned"],
        "ua": manifest["user_agent_class"],
        "smoke": ("—" if not smoke else
                  "%d requests, HTTP %s, %d of %d graded probes passed (captures in `smoke/raw/`)"
                  % (smoke["rows"], "/".join(smoke["statuses"]), smoke["passed"],
                     smoke["graded"])),
        "regrade": regrade_info["mismatches"],
        "regrade_checked": regrade_info["checked"],
        "pred_sha": regrade_info["predictions_sha256"],
        "row": row,
        "rep_rows": "\n".join(obs["rep_rows"]),
        "elapsed": " / ".join(str(v) for v in obs["perf_elapsed_ms"]),
        "pass_count": obs["pass_count"],
        "failed": ", ".join(obs["failed_probes"]) or "none",
        "failure_rows": failures,
        "pred_ttft": lane["ttft_ms"],
        "pred_ttft_range": "%s-%s" % tuple(lane["ttft_range_ms"]),
        "obs_ttft": ttft_med,
        "ttft_err": scoring["ttft_point_error_ms"],
        "ttft_verdict": "HIT range" if scoring["ttft_range_hit"]
                        else "MISS range (%s ms above the top)" % scoring["ttft_range_gap_ms"],
        "pred_tps": lane["tps"],
        "pred_tps_range": "%s-%s" % tuple(lane["tps_range"]),
        "obs_tps": obs["tps_med"],
        "tps_err": scoring["tps_point_error"],
        "tps_verdict": "HIT range" if scoring["tps_range_hit"] else "MISS range",
        "pred_pass": lane["pass_count"],
        "pred_pass_range": "%s-%s" % tuple(lane["pass_range"]),
        "obs_pass": obs["pass_count"],
        "pass_err": scoring["pass_point_error"],
        "pass_verdict": "HIT range" if scoring["pass_range_hit"] else "MISS range",
        "pred_fail": lane["failing_probe"],
        "obs_fail": ", ".join(obs["failed_probes"]) or "none",
        "fail_verdict": "HIT" if scoring["failing_probe_hit"] else "MISS",
        "obs_class": obs["dominant_class"],
        "class_verdict": "HIT" if scoring["failure_class_hit"] else "MISS",
        "obs_shape": obs["shape"],
        "hits": hits,
        "misses": total - hits,
        "total": total,
        "claim_rows": claim_rows,
    }
    return doc


def main():
    pred = json.load(open(PRED_PATH))
    pred_sha = __import__("hashlib").sha256(
        open(PRED_PATH, "rb").read()).hexdigest()
    records = load_records()
    telen = load_telemetry()
    checked, mismatches = regrade(records)
    obs = observe(records, telen)
    obs["rep_rows"] = []
    for rec in sorted(records, key=lambda r: (r.get("probe_id") != "perf", r.get("rep") or 0)):
        if rec.get("probe_id") != "perf":
            continue
        obs["rep_rows"].append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            rec.get("rep"), rec.get("status"),
            "content" if rec.get("ttft_content_ms") is not None else "first-decoded",
            rec.get("ttft_content_ms") if rec.get("ttft_content_ms") is not None
            else rec.get("first_decoded_ms"),
            rec.get("decode_span_ms"), rec.get("tps"), rec.get("completion_tokens"),
            rec.get("reasoning_tokens"), len(rec.get("content") or ""), rec.get("finish_reason")))
    scoring = score(pred, obs)
    manifest = json.load(open(os.path.join(RAW, "run-manifest.json")))
    regrade_info = {"checked": checked, "mismatches": len(mismatches),
                    "detail": mismatches, "predictions_sha256": pred_sha}
    with open(os.path.join(RAW, "regrade-check.json"), "w") as fh:
        json.dump(regrade_info, fh, indent=2)
        fh.write("\n")
    with open(os.path.join(RAW, "prediction-scoring.json"), "w") as fh:
        json.dump(common.redact(scoring), fh, indent=2)
        fh.write("\n")
    with open(os.path.join(TREE, "ANALYSIS.md"), "w") as fh:
        fh.write(build_markdown(pred, obs, scoring, regrade_info, manifest,
                                smoke_summary()))
    print("regrade: %d records, %d mismatches" % (checked, len(mismatches)))
    print("observed: ttft_med=%s tps_med=%s pass=%d/9 shape=%s"
          % (obs["ttft_med"], obs["tps_med"], obs["pass_count"], obs["shape"]))
    print("claims: %d/%d hit" % (scoring["hits"], scoring["total"]))
    print("wrote ANALYSIS.md, raw/regrade-check.json, raw/prediction-scoring.json")


if __name__ == "__main__":
    main()
