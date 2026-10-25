#!/usr/bin/env python3
"""R18 capability battery runner (stdlib only).

    python3 scripts/run_battery.py [--config PATH] [--models a,b] [--concurrency 4]

Runs, per pool model and in this order: an optional devin-class warm-up, two
sequential `perf` reps (TTFT/TPS headline), then the correctness corpus (c1-c5,
k1-k3, t1). Models run with bounded concurrency; a single model's probes always
run sequentially so its own concurrency is never a variable.

One attempt per model on a dead lane: if the first measured probe fails with a
transport or auth class (or an outright shape rejection), the model's remaining
probes are recorded as `skipped_after_fatal` and nothing is retried.
"""
import argparse
import csv
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402
import probes  # noqa: E402
import protocols  # noqa: E402

TELEMETRY_COLUMNS = [
    "model", "bucket", "provider", "protocol", "probe", "rep", "measured",
    "status", "failure_class", "passed", "elapsed_ms", "ttft_content_ms",
    "ttft_reasoning_ms", "first_decoded_ms", "decode_span_ms", "tps",
    "completion_tokens", "prompt_tokens", "reasoning_tokens", "finish_reason",
    "content_delta_count", "streaming_supported", "content_chars", "error",
]
LOCK = threading.Lock()

DEFAULT_TIMEOUT_S = 120
SHIM_TIMEOUT_S = 300
PROVIDER_TIMEOUT_S = {
    "glm-flash-cascade": 400,
    "devin": 400,
    "cursor": SHIM_TIMEOUT_S,
    "openai-codex": SHIM_TIMEOUT_S,
    "xai-oauth": SHIM_TIMEOUT_S,
    "ds-flash-cascade": SHIM_TIMEOUT_S,
}
DEVIN_CLASS_PROVIDERS = {"glm-flash-cascade", "devin"}
CONTENT_LIMIT = 20000


def plan_for(entry):
    plan = []
    if entry.get("provider") in DEVIN_CLASS_PROVIDERS:
        plan.append({"probe_id": "warmup", "kind": "warmup", "measured": False,
                     "rep": 0, "prompt": probes.WARMUP_PROMPT,
                     "max_tokens": probes.WARMUP_MAX_TOKENS,
                     "grade": {"type": "exact", "expect": "READY"}})
    for rep in (1, 2):
        plan.append({"probe_id": "perf", "kind": "perf", "measured": True,
                     "rep": rep, "prompt": probes.PERF_PROMPT,
                     "max_tokens": probes.PERF_MAX_TOKENS,
                     "grade": None})
    for probe in probes.CORRECTNESS_PROBES:
        item = dict(probe)
        item["probe_id"] = probe["id"]
        item["measured"] = True
        item["rep"] = 1
        plan.append(item)
    return plan


def body_for(item, entry, model_override):
    return protocols.build_body(
        item["probe_id"], item["prompt"], model_override, entry["protocol"],
        stream=True, max_tokens=item["max_tokens"],
        tools=item.get("tools"), tool_choice=item.get("tool_choice"),
        codex=(entry["protocol"] == "openai_responses"))


def run_probe(entry, item, provider_cfg, base_url, model_override, timeout,
              overall_deadline):
    url = common.chat_url(base_url, entry["protocol"])
    headers = common.auth_headers(provider_cfg, entry["protocol"])
    body = body_for(item, entry, model_override)
    capture = common.post_streaming(url, headers, body, timeout,
                                   overall_deadline=overall_deadline)
    summary = protocols.parse_capture(capture, entry["protocol"])
    body_text = "".join(line for line, _ in capture["lines"])[:4000]
    verdict = {"pass": None, "failure_class": None, "detail": "not graded",
               "request_level": False}
    if item.get("grade"):
        verdict = grade.grade(dict(item, kind=item["kind"]), summary,
                              capture.get("status"), capture.get("error_kind"),
                              body_text)
    else:
        # The perf probes carry no pass/fail, but a transport or quota failure
        # is still the lane's verdict and must drive the one-attempt rule.
        klass, detail = grade.request_class(capture.get("status"),
                                            capture.get("error_kind"), body_text)
        if klass:
            verdict = {"pass": None, "failure_class": klass, "detail": detail,
                       "request_level": True}
    content = summary.get("content") or ""
    record = {
        "pool_id": entry["pool_id"],
        "provider": entry.get("provider"),
        "model_id": entry.get("model_id"),
        "model_sent": model_override,
        "protocol": entry["protocol"],
        "bucket": entry.get("bucket"),
        "base_url": common.redact_text(base_url),
        "probe_id": item["probe_id"],
        "probe_kind": item["kind"],
        "rep": item.get("rep"),
        "measured": item.get("measured", True),
        "prompt": item["prompt"],
        "max_tokens": item["max_tokens"],
        "tools_sent": bool(item.get("tools")),
        "tool_choice": item.get("tool_choice"),
        "request_body": common.redact(body),
        "url": capture.get("url"),
        "timeout_s": timeout,
        "auth_headers_sent": sorted(name for name in headers
                                    if name.lower() in common.SECRET_HEADER_NAMES),
        "status": capture.get("status"),
        "error": capture.get("error"),
        "error_kind": capture.get("error_kind"),
        "elapsed_ms": capture.get("elapsed_ms"),
        "response_headers": capture.get("response_headers"),
        "content_type": (capture.get("response_headers") or {}).get("Content-Type"),
        "content": content[:CONTENT_LIMIT],
        "content_truncated": len(content) > CONTENT_LIMIT,
        "reasoning_chars": summary.get("reasoning_chars"),
        "reasoning_text": summary.get("reasoning_text"),
        "refusal_text": summary.get("refusal_text"),
        "tool_calls": summary.get("tool_calls"),
        "usage": summary.get("usage"),
        "finish_reason": summary.get("finish_reason"),
        "response_status": summary.get("response_status"),
        "incomplete_reason": summary.get("incomplete_reason"),
        "streaming_supported": summary.get("streaming_supported"),
        "sse_event_count": summary.get("sse_event_count"),
        "sse_line_count": capture.get("line_count"),
        "raw_preview": common.redact_text(capture.get("preview") or ""),
        "grade": verdict,
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    for key in ("ttft_content_ms", "ttft_reasoning_ms", "first_decoded_ms",
                "decode_span_ms", "tps", "tps_basis", "tps_note",
                "completion_tokens", "prompt_tokens", "reasoning_tokens",
                "content_delta_count", "reasoning_delta_count"):
        record[key] = summary.get(key)
    return record


def telemetry_row(entry, record):
    return {
        "model": entry["pool_id"], "bucket": entry.get("bucket"),
        "provider": entry.get("provider"), "protocol": entry["protocol"],
        "probe": record["probe_id"] + ("" if record["probe_id"] == "perf"
                                       and not record.get("rep")
                                       else "-r%s" % record.get("rep")),
        "rep": record.get("rep"), "measured": record.get("measured"),
        "status": record.get("status"),
        "failure_class": (record.get("grade") or {}).get("failure_class"),
        "passed": (record.get("grade") or {}).get("pass"),
        "elapsed_ms": record.get("elapsed_ms"),
        "ttft_content_ms": record.get("ttft_content_ms"),
        "ttft_reasoning_ms": record.get("ttft_reasoning_ms"),
        "first_decoded_ms": record.get("first_decoded_ms"),
        "decode_span_ms": record.get("decode_span_ms"),
        "tps": record.get("tps"),
        "completion_tokens": record.get("completion_tokens"),
        "prompt_tokens": record.get("prompt_tokens"),
        "reasoning_tokens": record.get("reasoning_tokens"),
        "finish_reason": record.get("finish_reason"),
        "content_delta_count": record.get("content_delta_count"),
        "streaming_supported": record.get("streaming_supported"),
        "content_chars": len(record.get("content") or ""),
        "error": (record.get("error") or "")[:200],
    }


def skipped_record(entry, item, reason):
    return {
        "pool_id": entry["pool_id"], "provider": entry.get("provider"),
        "model_id": entry.get("model_id"), "protocol": entry["protocol"],
        "bucket": entry.get("bucket"), "probe_id": item["probe_id"],
        "probe_kind": item["kind"], "rep": item.get("rep"),
        "measured": item.get("measured", True), "prompt": item["prompt"],
        "max_tokens": item["max_tokens"], "status": None,
        "grade": {"pass": False, "failure_class": "skipped_after_fatal",
                  "detail": reason},
        "skipped": True, "skip_reason": reason,
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def run_model(entry, cfg, args, state):
    provider_cfg = cfg.get("providers", {}).get(entry.get("provider"), {})
    base_url = args.mock_base or entry.get("base_url") or ""
    model_override = entry.get("model_id")
    if args.mock_base:
        behaviour = state["mock_map"].get(entry["pool_id"], "good")
        model_override = "%s-%s" % (model_override, behaviour)
    timeout = args.timeout if args.mock_base else \
        PROVIDER_TIMEOUT_S.get(entry.get("provider"), DEFAULT_TIMEOUT_S)
    directory = os.path.join(common.RESP_DIR, common.slug(entry["pool_id"]))
    os.makedirs(directory, exist_ok=True)
    plan = plan_for(entry)
    fatal_reason = None
    transport_failures = 0
    for item in plan:
        if fatal_reason:
            record = skipped_record(entry, item, fatal_reason)
        else:
            if args.deadline_min and time.time() > state["deadline"]:
                record = skipped_record(entry, item, "run deadline reached")
            else:
                record = run_probe(entry, item, provider_cfg, base_url,
                                   model_override, timeout, args.deadline_min * 60)
        path = os.path.join(directory, "%s.json" % grade_slug(item))
        common.write_json(path, record)
        row = telemetry_row(entry, record)
        with LOCK:
            state["rows"].append(row)
            if state["writer"] is not None:
                state["writer"].writerow(row)
                state["csv_file"].flush()
            state["done"] += 1
            print("[%3d/%3d] %-45s %-8s %-7s %-16s %s" % (
                state["done"], state["total"], entry["pool_id"],
                item["probe_id"] + ("-r%s" % item.get("rep") if item.get("rep") else ""),
                row["status"], row["failure_class"],
                ("pass" if row["passed"] else "") if row["passed"] is not None else ""),
                flush=True)
        verdict = (record.get("grade") or {})
        if item.get("measured") and not record.get("skipped") and \
                verdict.get("request_level"):
            klass = verdict.get("failure_class")
            detail = record.get("error") or verdict.get("detail") or ""
            if klass in ("auth", "format_break"):
                fatal_reason = ("lane refused at %s with class %s (%s); no retry"
                                % (item["probe_id"], klass, str(detail)[:160]))
            elif klass == "transport":
                transport_failures += 1
                if transport_failures >= 2:
                    fatal_reason = ("two consecutive transport failures, last at %s (%s)"
                                    % (item["probe_id"], str(detail)[:160]))


def grade_slug(item):
    return "%s-r%s" % (item["probe_id"], item["rep"]) if item.get("rep") \
        else item["probe_id"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=common.CONFIG_PATH)
    parser.add_argument("--models", default="", help="comma-separated pool ids")
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    parser.add_argument("--deadline-min", type=int, default=0)
    parser.add_argument("--mock-base", default="")
    parser.add_argument("--mock-map", default="")
    parser.add_argument("--outdir", default=common.RAW_DIR)
    args = parser.parse_args()

    cfg, raw = common.load_config(args.config)
    config_digest = common.config_sha256(raw)
    entries = common.pool(cfg)
    if args.models:
        wanted = {m.strip() for m in args.models.split(",") if m.strip()}
        entries = [e for e in entries if e["pool_id"] in wanted]
    entries = [e for e in entries if not e.get("unresolved")]

    os.makedirs(common.RESP_DIR, exist_ok=True)
    csv_path = os.path.join(args.outdir, "telemetry.csv")
    csv_file = open(csv_path, "w", newline="")
    writer = csv.DictWriter(csv_file, fieldnames=TELEMETRY_COLUMNS)
    writer.writeheader()

    mock_map = {}
    if args.mock_map:
        with open(args.mock_map) as fh:
            mock_map = json.load(fh)
    total = sum(len(plan_for(e)) for e in entries)
    state = {"rows": [], "writer": writer, "csv_file": csv_file, "done": 0,
             "total": total, "mock_map": mock_map,
             "deadline": time.time() + args.deadline_min * 60 if args.deadline_min else 0}

    print("battery run: %d models, %d requests, concurrency %d, config sha256 %s"
          % (len(entries), total, args.concurrency, config_digest), flush=True)
    started = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(run_model, entry, cfg, args, state): entry
                   for entry in entries}
        for future in futures:
            try:
                future.result()
            except Exception as exc:  # noqa: BLE001
                print("model thread failed: %s: %s" % (type(exc).__name__, exc),
                      flush=True)
    csv_file.close()

    manifest = {
        "argv": sys.argv,
        "config_path": args.config,
        "config_sha256": config_digest,
        "config_core_sha256": common.core_digest(cfg),
        "models": [e["pool_id"] for e in entries],
        "requests_planned": total,
        "requests_recorded": len(state["rows"]),
        "concurrency": args.concurrency,
        "mock_base": args.mock_base or None,
        "reps": 2,
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
        "finished_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "duration_s": round(time.time() - started, 1),
        "telemetry_csv": os.path.relpath(csv_path, os.path.dirname(common.BATTERY_DIR)),
    }
    common.write_json(os.path.join(args.outdir, "run-manifest.json"), manifest)
    print("done: %d/%d requests in %.0fs -> %s"
          % (len(state["rows"]), total, time.time() - started, csv_path), flush=True)


if __name__ == "__main__":
    main()
