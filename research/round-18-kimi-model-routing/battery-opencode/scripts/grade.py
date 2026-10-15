#!/usr/bin/env python3
"""Deterministic grading for the R18 battery.

One implementation, used twice: the runner stamps a failure class onto every
telemetry row as it lands, and `grade.py --report` rebuilds the same verdicts
from the raw captures. Nothing here calls a model.

Failure-class taxonomy (fixed by the mission):
    transport     no response, socket/timeout/protocol error, or HTTP 5xx
    auth          401 / 403, or a 429 whose body reports exhausted quota
    refusal       the lane declines in words (or returns a refusal field)
    truncation    answer absent or cut off: empty content, finish_reason length,
                  or the output budget consumed by reasoning tokens
    format_break  the request shape was rejected (4xx that is not auth) or the
                  answer breaks the requested format with no usable value
    wrong_answer  a well-formed answer carrying the wrong value
    ok            graded pass
"""
import json
import re

REFUSAL_MARKERS = (
    "i can't", "i cannot", "i can not", "i'm sorry", "i am sorry", "i won't",
    "i will not", "unable to", "cannot assist", "can't help", "cannot help",
    "as an ai", "i must decline", "not able to help",
)
AUTH_STATUS = {401, 402, 403}
SHAPE_STATUS = {400, 404, 405, 406, 415, 422, 501}


def normalize(text):
    out = (text or "").strip()
    out = re.sub(r"^```[A-Za-z0-9_+-]*\s*\n?", "", out)
    out = re.sub(r"\n?```\s*$", "", out)
    out = out.strip()
    if len(out) >= 2 and out[0] == out[-1] and out[0] in "\"'`":
        out = out[1:-1].strip()
    out = re.sub(r"\s+$", "", out)
    return out


def _strip_trailing_period(text):
    if len(text) > 1 and text.endswith(".") and not text.endswith(".."):
        return text[:-1].rstrip()
    return text


def _empty(summary, probe):
    return not summary.get("content") and not summary.get("tool_calls")


def _refusal(summary):
    text = ((summary.get("content") or "") + " " + (summary.get("refusal_text") or "")).lower()
    return any(marker in text for marker in REFUSAL_MARKERS)


def _is_truncated(summary):
    return (summary.get("finish_reason") == "length"
            or summary.get("incomplete_reason") == "max_output_tokens")


def request_class(status, error_kind, body_text):
    """Class for anything decided before the model's content is examined."""
    if status is None:
        return "transport", "no response (%s: %s)" % (error_kind, (body_text or "")[:200])
    if status in AUTH_STATUS:
        return "auth", "HTTP %s" % status
    if status == 429:
        low = (body_text or "").lower()
        if "quota" in low or "insufficient" in low or "exhausted" in low:
            return "auth", "HTTP 429 quota exhausted"
        return "transport", "HTTP 429 rate limited"
    if status >= 500:
        return "transport", "HTTP %s" % status
    if status in SHAPE_STATUS:
        return "format_break", "HTTP %s request shape rejected" % status
    if status != 200:
        return "transport", "HTTP %s" % status
    return None, None


def _grade_exact(probe, text):
    expect = probe["grade"]["expect"]
    if probe["grade"].get("strip_spaces"):
        text = text.replace(" ", "")
        expect = expect.replace(" ", "")
    observed = normalize(text)
    if _strip_trailing_period(observed) == expect:
        return True, "exact match"
    if observed.lower() == expect.lower():
        return False, "case mismatch against %r (observed %r)" % (expect, observed[:120])
    return False, "expected %r, observed %r" % (expect, observed[:120])


def _grade_json(probe, text):
    observed = normalize(text)
    try:
        parsed = json.loads(observed)
    except Exception as exc:  # noqa: BLE001
        return False, "output is not JSON (%s): %r" % (type(exc).__name__, observed[:120])
    expect = probe["grade"]["expect"]
    if parsed == expect:
        return True, "json match"
    return False, "expected %s, parsed %r" % (json.dumps(expect), json.dumps(parsed)[:120])


def _grade_lines(probe, text):
    observed = [line.strip() for line in normalize(text).splitlines() if line.strip()]
    expect = probe["grade"]["expect"]
    if observed == expect:
        return True, "line match"
    return False, "expected %r, observed %r" % (expect, observed[:6])


def _grade_no_char(probe, text):
    observed = normalize(text)
    char = probe["grade"]["char"]
    if len(observed) < probe["grade"]["min_chars"]:
        return False, "answer too short to grade (%d chars): %r" % (len(observed), observed[:120])
    if char.lower() in observed.lower():
        return False, "forbidden letter %r present: %r" % (char, observed[:120])
    return True, "constraint held"


def _grade_code_cases(probe, text):
    code = normalize(text)
    namespace = {}
    try:
        exec(compile(code, "<battery>", "exec"), namespace)  # noqa: S102 - grader
    except Exception as exc:  # noqa: BLE001
        return False, "code did not compile (%s): %r" % (type(exc).__name__, code[:160])
    func = namespace.get("rev")
    if not callable(func):
        return False, "no callable named rev in the output"
    for argument, expected in probe["grade"]["cases"]:
        try:
            got = func(argument)
        except Exception as exc:  # noqa: BLE001
            return False, "rev(%r) raised %s" % (argument, type(exc).__name__)
        if got != expected:
            return False, "rev(%r) returned %r, expected %r" % (argument, got, expected)
    return True, "%d cases pass" % len(probe["grade"]["cases"])


def _grade_tool(probe, summary):
    calls = summary.get("tool_calls") or []
    spec = probe["grade"]
    if not calls:
        if _refusal(summary):
            return False, "refused instead of calling a tool", "refusal"
        return False, "no tool_calls block emitted", "format_break"
    call = calls[0]
    if call.get("name") != spec["expect_name"]:
        return False, "called %r, expected %r" % (call.get("name"), spec["expect_name"]), "format_break"
    raw_arguments = call.get("arguments") or ""
    try:
        parsed = json.loads(raw_arguments)
    except Exception:  # noqa: BLE001
        return False, "arguments are not valid JSON: %r" % raw_arguments[:120], "format_break"
    if not isinstance(parsed, dict):
        return False, "arguments are not a JSON object: %r" % raw_arguments[:120], "format_break"
    value = str(parsed.get(spec["expect_arg_key"], "")).lower()
    if spec["expect_arg_value"] not in value and value not in spec["expect_arg_value"]:
        return (False, "arguments %s do not carry the requested city" % json.dumps(parsed)[:120],
                "wrong_answer")
    return True, "well-formed tool call", "ok"


GRADERS = {
    "exact": _grade_exact,
    "json_exact": _grade_json,
    "lines_exact": _grade_lines,
    "no_char": _grade_no_char,
    "code_cases": _grade_code_cases,
}


def has_fence(text):
    return "```" in (text or "")


def grade(probe, summary, status, error_kind, body_text):
    """Verdict for one probe response.

    `request_level` marks a verdict the lane itself is answerable for (a refused
    request shape, a quota wall, a dead socket) as opposed to a verdict about
    this model's answer to this question. Only request-level verdicts trigger
    the runner's one-attempt rule; a fenced answer to c1 must not stop the
    battery for that model.
    """
    if summary.get("skipped"):
        return {"pass": False, "failure_class": "skipped_after_fatal",
                "detail": summary.get("skip_reason") or "skipped", "request_level": True}
    klass, detail = request_class(status, error_kind, body_text)
    if klass:
        return {"pass": False, "failure_class": klass, "detail": detail,
                "request_level": True}
    verdict = _grade_content(probe, summary)
    verdict["request_level"] = False
    return verdict


def _grade_content(probe, summary):
    content = summary.get("content") or ""
    # A probe whose instruction forbids markdown is failed on sight of a fence:
    # the format contract is part of what is being measured, so normalising the
    # fence away would grade a different question than the one asked.
    if probe.get("grade", {}).get("no_fences") and has_fence(content):
        return {"pass": False, "failure_class": "format_break",
                "detail": "answer wrapped in a markdown code fence: %r" % content[:120]}

    if probe["kind"] == "tool":
        passed, detail, klass = _grade_tool(probe, summary)
        if passed:
            return {"pass": True, "failure_class": "ok", "detail": detail}
        if klass == "wrong_answer":
            return {"pass": False, "failure_class": "wrong_answer", "detail": detail}
        if _is_truncated(summary) and _empty(summary, probe):
            return {"pass": False, "failure_class": "truncation", "detail": detail}
        return {"pass": False, "failure_class": klass, "detail": detail}

    if _empty(summary, probe):
        if _refusal(summary):
            return {"pass": False, "failure_class": "refusal",
                    "detail": "declined: %r" % (summary.get("content") or "")[:120]}
        if _is_truncated(summary) or summary.get("reasoning_text"):
            return {"pass": False, "failure_class": "truncation",
                    "detail": "no content (finish_reason=%s, reasoning_chars=%s)"
                              % (summary.get("finish_reason"), summary.get("reasoning_chars"))}
        return {"pass": False, "failure_class": "format_break", "detail": "empty response body"}

    passed, detail = GRADERS[probe["grade"]["type"]](probe, content)
    if passed:
        return {"pass": True, "failure_class": "ok", "detail": detail}
    if _refusal(summary):
        return {"pass": False, "failure_class": "refusal", "detail": detail}
    if _is_truncated(summary):
        return {"pass": False, "failure_class": "truncation",
                "detail": "%s (finish_reason=length)" % detail}
    grade_type = probe["grade"]["type"]
    if grade_type in ("json_exact", "lines_exact", "code_cases"):
        return {"pass": False, "failure_class": "format_break", "detail": detail}
    return {"pass": False, "failure_class": "wrong_answer", "detail": detail}


def load_records():
    """Every raw capture on disk, flattened to one record per request."""
    import os
    records = []
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "raw", "responses")
    for slug in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        directory = os.path.join(root, slug)
        if not os.path.isdir(directory):
            continue
        for name in sorted(os.listdir(directory)):
            if not name.endswith(".json"):
                continue
            path = os.path.join(directory, name)
            with open(path) as fh:
                record = json.load(fh)
            record["_file"] = path
            records.append(record)
    return records
