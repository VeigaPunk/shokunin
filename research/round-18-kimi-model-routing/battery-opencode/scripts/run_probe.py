#!/usr/bin/env python3
"""R18 opencode-go deepseek probe runner (stdlib only).

    python3 scripts/run_probe.py [--model opencode-go/deepseek-v4.1-flash]

Measures exactly one lane, resolved from `[models.<id>]` even when that entry is
absent from the live `[secondary_model.models]` table (which is why the M3
battery never reached it). The plan, request bodies, timing derivation, grading
and telemetry schema are the M3 battery's (`../battery/scripts`), so the result
splices into that table: two sequential perf reps, then the 9 correctness
probes, one attempt per dead lane, no loops.

The one transport delta is the opencode-go constraint M2 documented: the lane
sits behind Cloudflare and answers a scripted user agent with `403 error code:
1010`, so every request carries a browser user agent (class recorded, never a
fingerprint or a credential).
"""
import argparse
import csv
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402
import probes  # noqa: E402
import protocols  # noqa: E402

DEFAULT_MODEL = "opencode-go/deepseek-v4.1-flash"
TELEMETRY_COLUMNS = [
    "model", "bucket", "provider", "protocol", "probe", "rep", "measured",
    "status", "failure_class", "passed", "elapsed_ms", "ttft_content_ms",
    "ttft_reasoning_ms", "first_decoded_ms", "decode_span_ms", "tps",
    "completion_tokens", "prompt_tokens", "reasoning_tokens", "finish_reason",
    "content_delta_count", "streaming_supported", "content_chars", "error",
]
DEFAULT_TIMEOUT_S = 120
CONTENT_LIMIT = 20000
BROWSER_UA_PROVIDERS = {"opencode-go"}


def resolve_lane(cfg, model_id):
    """Resolve a `[models.<id>]` entry without requiring pool membership."""
    mcfg = (cfg.get("models") or {}).get(model_id)
    if not mcfg:
        raise SystemExit("no [models.%s] entry in the config" % model_id)
    provider = mcfg.get("provider")
    pcfg = (cfg.get("providers") or {}).get(provider, {})
    protocol = mcfg.get("protocol") or pcfg.get("type") or "openai"
    base_url = (mcfg.get("base_url") or pcfg.get("base_url") or "").rstrip("/")
    in_pool = model_id in (cfg.get("secondary_model", {}).get("models") or {})
    bucket = "UNLABELLED"
    if in_pool:
        bucket = common.bucket_of(cfg["secondary_model"]["models"][model_id])
    return {
        "pool_id": model_id,
        "provider": provider,
        "model_id": mcfg.get("model"),
        "protocol": protocol,
        "base_url": base_url,
        "bucket": bucket,
        "in_live_pool": in_pool,
        "capabilities": mcfg.get("capabilities", []),
        "reasoning_key": mcfg.get("reasoning_key"),
        "provider_cfg": pcfg,
    }


def plan_for(entry):
    plan = []
    for rep in (1, 2):
        plan.append({"probe_id": "perf", "kind": "perf", "measured": True,
                     "rep": rep, "prompt": probes.PERF_PROMPT,
                     "max_tokens": probes.PERF_MAX_TOKENS, "grade": None})
    for probe in probes.CORRECTNESS_PROBES:
        item = dict(probe)
        item["probe_id"] = probe["id"]
        item["measured"] = True
        item["rep"] = 1
        plan.append(item)
    return plan


def grade_slug(item):
    return "%s-r%s" % (item["probe_id"], item["rep"]) if item.get("rep") \
        else item["probe_id"]


def run_probe(entry, item, base_url, model_override, timeout, overall_deadline,
              user_agent):
    url = common.chat_url(base_url, entry["protocol"])
    headers = common.auth_headers(entry["provider_cfg"], entry["protocol"])
    body = protocols.build_body(
        item["probe_id"], item["prompt"], model_override, entry["protocol"],
        stream=True, max_tokens=item["max_tokens"],
        tools=item.get("tools"), tool_choice=item.get("tool_choice"),
        codex=(entry["protocol"] == "openai_responses"))
    capture = common.post_streaming(url, headers, body, timeout,
                                    overall_deadline=overall_deadline,
                                    user_agent=user_agent)
    summary = protocols.parse_capture(capture, entry["protocol"])
    body_text = "".join(line for line, _ in capture["lines"])[:4000]
    verdict = {"pass": None, "failure_class": None, "detail": "not graded",
               "request_level": False}
    if item.get("grade"):
        verdict = grade.grade(dict(item, kind=item["kind"]), summary,
                              capture.get("status"), capture.get("error_kind"),
                              body_text)
    else:
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
        "in_live_pool": entry.get("in_live_pool"),
        "base_url": common.redact_text(base_url),
        "reasoning_key": entry.get("reasoning_key"),
        "user_agent_class": common.UA_CLASS,
        "user_agent_sent": user_agent or None,
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=common.CONFIG_PATH)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    parser.add_argument("--deadline-min", type=int, default=45)
    parser.add_argument("--outdir", default=common.RAW_DIR)
    parser.add_argument("--mock-base", default="",
                        help="loopback mock endpoint, for the zero-quota smoke")
    parser.add_argument("--mock-behaviour", default="good",
                        help="mock behaviour suffix appended to the model id")
    args = parser.parse_args()

    cfg, raw = common.load_config(args.config)
    config_digest = common.config_sha256(raw)
    entry = resolve_lane(cfg, args.model)
    base_url = args.mock_base or entry["base_url"]
    model_override = entry["model_id"]
    if args.mock_base:
        model_override = "%s-%s" % (model_override, args.mock_behaviour)
    user_agent = common.BROWSER_UA if entry["provider"] in BROWSER_UA_PROVIDERS else None
    directory = os.path.join(common.RESP_DIR, common.slug(entry["pool_id"]))
    os.makedirs(directory, exist_ok=True)

    csv_path = os.path.join(args.outdir, "telemetry.csv")
    csv_file = open(csv_path, "w", newline="")
    writer = csv.DictWriter(csv_file, fieldnames=TELEMETRY_COLUMNS)
    writer.writeheader()

    plan = plan_for(entry)
    deadline = (time.time() + args.deadline_min * 60) if args.deadline_min else 0
    fatal_reason = None
    transport_failures = 0
    rows = []
    print("opencode probe: %s via %s (%s), %d requests, config sha256 %s"
          % (entry["pool_id"], entry["provider"], entry["protocol"], len(plan),
             config_digest), flush=True)
    print("user agent class: %s; endpoint %s"
          % (common.UA_CLASS if user_agent else "default", common.redact_text(base_url)),
          flush=True)
    started = time.time()
    for item in plan:
        if fatal_reason:
            record = skipped_record(entry, item, fatal_reason)
        elif deadline and time.time() > deadline:
            record = skipped_record(entry, item, "run deadline reached")
        else:
            record = run_probe(entry, item, base_url, model_override, args.timeout,
                               args.deadline_min * 60 if args.deadline_min else None,
                               user_agent)
        common.write_json(os.path.join(directory, "%s.json" % grade_slug(item)), record)
        row = telemetry_row(entry, record)
        rows.append(row)
        writer.writerow(row)
        csv_file.flush()
        print("[%2d/%2d] %-12s %-6s %-16s %s" % (
            len(rows), len(plan), grade_slug(item), row["status"],
            row["failure_class"],
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
    csv_file.close()

    manifest = {
        "argv": sys.argv,
        "config_path": args.config,
        "config_sha256": config_digest,
        "config_core_sha256": common.core_digest(cfg),
        "models": [entry["pool_id"]],
        "lane": {k: v for k, v in entry.items() if k != "provider_cfg"},
        "requests_planned": len(plan),
        "requests_recorded": len(rows),
        "reps": 2,
        "user_agent_class": common.UA_CLASS if user_agent else None,
        "ua_constraint": ("M2 definitions ANALYSIS section 1: opencode-go answers a "
                          "scripted user agent with 403 error code 1010 (Cloudflare); "
                          "a browser user agent returns 200"),
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
        "finished_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "duration_s": round(time.time() - started, 1),
        "telemetry_csv": os.path.relpath(csv_path, os.path.dirname(common.BATTERY_DIR)),
    }
    common.write_json(os.path.join(args.outdir, "run-manifest.json"), manifest)
    print("done: %d/%d requests in %.0fs -> %s"
          % (len(rows), len(plan), time.time() - started, csv_path), flush=True)


if __name__ == "__main__":
    main()
