#!/usr/bin/env bash
# Deterministic metadata-only regression fixtures. No agents/providers/live state.
# Run: bash scripts/hyaku/wave-slot-selftest.sh
# Every file and gate reservation is confined to a temporary scratch directory.
set -euo pipefail
SELF_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
python3 - "$SELF_DIR/wave-live.py" "$SELF_DIR/wave-slot.sh" <<'PY'
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

counter, gate = sys.argv[1:]
BASE = 1_700_000_000
TAIL = 256 * 1024
passed = total = 0


def check(label, actual, expected):
    global passed, total
    total += 1
    if actual == expected:
        passed += 1
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}: expected {expected!r}, got {actual!r}")


def message(role, reason=None, at=BASE):
    m = {"role": role, "timestamp": at * 1000}
    if reason is not None:
        m["stopReason"] = reason
        m["completedAt"] = at * 1000
    return {"type": "message", "timestamp": at, "message": m}


def exit_record(at=BASE + 1):
    return {"type": "custom", "customType": "session_exit", "timestamp": at,
            "data": {"reason": "completed", "kind": "terminal", "recordedAt": at}}


def encode(rows):
    return b"".join(json.dumps(r).encode() + b"\n" for r in rows)


def count(directory):
    p = subprocess.run([sys.executable, counter, str(directory)],
                       capture_output=True, text=True, timeout=10)
    if p.returncode or p.stderr or not p.stdout.rstrip("\n").isdecimal():
        return (p.returncode, p.stdout, p.stderr)
    return int(p.stdout)


with tempfile.TemporaryDirectory(prefix="wave-slot-selftest.") as scratch:
    root = Path(scratch)
    fixtures = root / "fixtures"
    fixtures.mkdir()

    def fixture(label, rows, expected, artifact=None, raw=None):
        directory = fixtures / label
        directory.mkdir()
        transcript = directory / "seat.jsonl"
        transcript.write_bytes(encode(rows) if raw is None else raw)
        if artifact is not None:
            md = directory / "seat.md"
            md.write_text("completed\n" if artifact else "", encoding="utf-8")
            os.utime(md, (BASE + artifact, BASE + artifact))
        check(label, count(directory), expected)
        return directory

    fixture("active-empty-md", [message("user")], 1, artifact=0)
    fixture("failed-terminal-empty-md", [message("assistant", "error"), exit_record()],
            0, artifact=0)
    fixture("error-without-exit", [message("assistant", "error")],
            0, artifact=0)
    fixture("aborted-without-exit", [message("assistant", "aborted")], 0)
    fixture("success-usage-metadata", [message("assistant", "stop"),
            {"type": "model_usage", "timestamp": BASE + 10, "stopReason": "stop"},
            {"type": "custom", "customType": "system-prompt-digest",
             "timestamp": BASE + 11, "data": "fixture-only"}], 0, artifact=1)
    revived = [message("assistant", "stop"), exit_record(),
               message("user", at=BASE + 10),
               message("assistant", "toolUse", at=BASE + 11)]
    fixture("revived-stale-md", revived, 1, artifact=2)
    fixture("revived-new-terminal", revived + [exit_record(BASE + 12)],
            0, artifact=2)
    fixture("revived-incoming", [exit_record(),
            {"type": "custom_message", "customType": "irc:incoming",
             "timestamp": BASE + 10, "content": "fixture-only"}],
            1, artifact=2)
    fixture("revived-tool-start", [exit_record(),
            {"type": "custom", "customType": "tool_execution_start",
             "timestamp": BASE + 10, "data": {"toolCallId": "fixture"}}],
            1, artifact=2)
    fixture("revived-tool-result", [exit_record(), message("toolResult", at=BASE + 10)],
            1, artifact=2)
    fixture("error-then-user", [message("assistant", "error"),
            message("user", at=BASE + 10)], 1)
    fixture("missing-success-artifact", [message("assistant", "stop")], 1)
    fixture("stale-success-artifact", [message("assistant", "stop", at=BASE + 10)],
            1, artifact=2)
    iso = message("assistant", "stop")
    iso["timestamp"] = "2023-11-14T22:13:20.000Z"
    fixture("iso-success-timestamp", [iso], 0, artifact=1)
    fallback = message("assistant", "stop")
    del fallback["timestamp"]
    fixture("completed-at-fallback", [fallback], 0, artifact=1)
    tied = fixture("timestamp-tie-setup", [message("assistant", "stop")], 0, artifact=1)
    os.utime(tied / "seat.md", (BASE, BASE))
    check("equal-artifact-time-conservative", count(tied), 1)
    invalid_time = message("assistant", "stop")
    invalid_time["timestamp"] = 10 ** 1000
    del invalid_time["message"]["timestamp"]
    del invalid_time["message"]["completedAt"]
    fixture("invalid-success-time-conservative", [invalid_time], 1, artifact=1)
    fixture("terminal-usage-only", [exit_record(), {"type": "model_usage"}], 0)
    fixture("empty-transcript", [], 1, artifact=1)
    fixture("unknown-record", [{"type": "unrecognized"}], 1, artifact=1)
    fixture("incomplete-custom-metadata", [{"type": "custom"}], 1, artifact=1)
    fixture("incomplete-after-terminal", [], 1, artifact=1,
            raw=encode([exit_record()]) + b'{"type":"message"')
    fixture("malformed-after-terminal", [], 1, artifact=1,
            raw=encode([exit_record()]) + b'not-json\n')
    fixture("malformed-before-terminal", [], 0,
            raw=b'not-json\n' + encode([exit_record()]))
    huge = {"type": "custom", "customType": "session_exit", "data": "x" * (TAIL + 32)}
    fixture("oversized-terminal-unknown", [huge], 1, artifact=1)
    prefix = encode([{"type": "message", "message": {"role": "assistant",
                     "content": "x" * (TAIL + 32)}}])
    fixture("oversized-leading-terminal-visible", [], 0,
            raw=prefix + encode([exit_record()]))
    fixture("oversized-leading-revival-visible", [], 1, artifact=2,
            raw=prefix + encode([exit_record(), message("user", at=BASE + 10)]))
    fixture("oversized-last-line-unknown", [], 1, artifact=1,
            raw=encode([exit_record()]) + b'x' * (TAIL + 32))

    nested = root / "nested"
    (nested / "parent" / "child").mkdir(parents=True)
    (nested / "parent.jsonl").write_bytes(encode([message("user")]))
    (nested / "parent" / "child" / "active.jsonl").write_bytes(encode([message("user")]))
    (nested / "parent" / "failed.jsonl").write_bytes(encode([exit_record()]))
    check("recursive-nested-agents", count(nested), 2)

    outside = root / "outside"
    outside.mkdir()
    (outside / "active.jsonl").write_bytes(encode([message("user")]))
    (outside / "closed.jsonl").write_bytes(encode([exit_record()]))
    safe = root / "safe"
    safe.mkdir()
    (safe / "linked-directory").symlink_to(outside, target_is_directory=True)
    check("no-symlink-subtree-follow", count(safe), 0)
    (safe / "linked.jsonl").symlink_to(outside / "closed.jsonl")
    check("symlink-transcript-conservative", count(safe), 1)
    os.mkfifo(safe / "fifo.jsonl")
    check("fifo-transcript-nonblocking", count(safe), 2)
    (safe / "directory.jsonl").mkdir()
    check("nonregular-transcript-conservative", count(safe), 3)
    mdlink = fixture("success-artifact-placeholder", [message("assistant", "stop")], 1)
    (mdlink / "seat.md").symlink_to(outside / "active.jsonl")
    check("symlink-artifact-conservative", count(mdlink), 1)
    linked_root = root / "linked-root"
    linked_root.symlink_to(outside, target_is_directory=True)
    p = subprocess.run([sys.executable, counter, str(linked_root)],
                       capture_output=True, text=True, timeout=10)
    check("symlink-root-refused", (p.returncode, p.stdout), (2, ""))

    # Basic gate integration uses no live directory and cannot wait on capacity.
    state = root / "state"
    state.mkdir()
    empty = root / "empty-session"
    empty.mkdir()
    (state / "wave-cap").write_text("240\n", encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if not k.startswith("HYAKU_")}
    env.update(HYAKU_STATE=str(state), HYAKU_SESSION_DIR=str(empty),
               HYAKU_WAVE_MIN_AVAIL_MB="0", HYAKU_WAVE_REVIVED="99")

    def call_gate(*args, extra=None):
        return subprocess.run(["bash", gate, *args], env=env | (extra or {}),
                              capture_output=True, text=True, timeout=10)

    p = call_gate("status")
    check("state-target-unchanged", p.returncode == 0 and
          "live_estimate=0 " in p.stdout and "cap=240 cap_source=state" in p.stdout and
          "manual_reserve=0" in p.stdout, True)
    p = call_gate("status", extra={"HYAKU_WAVE_CAP": "241"})
    check("environment-target-priority", p.returncode == 0 and
          "cap=241 cap_source=environment" in p.stdout, True)
    p = call_gate("status", extra={"HYAKU_WAVE_MANUAL_RESERVE": "003"})
    check("explicit-manual-reserve", p.returncode == 0 and
          "live_estimate=3 " in p.stdout and "manual_reserve=3" in p.stdout, True)
    p = call_gate("acquire", "fixture", "wave", "2", "0")
    check("acquire-scratch-reservation", p.returncode == 0 and
          p.stdout.startswith("granted lane=fixture wave=wave seats=2 live=0 pending=0 cap=240"), True)
    p = call_gate("release", "fixture", "wave")
    check("release-scratch-reservation", (p.returncode, (state / "wave-slots").read_text()), (0, ""))

    p = subprocess.run([sys.executable, counter, ""], cwd=empty,
                       capture_output=True, text=True, timeout=10)
    check("empty-counter-session-refused", (p.returncode, p.stdout), (2, ""))
    missing_env = env.copy()
    del missing_env["HYAKU_SESSION_DIR"]
    p = subprocess.run(["bash", gate, "status"], env=missing_env, cwd=empty,
                       capture_output=True, text=True, timeout=10)
    check("missing-session-status-refused", (p.returncode, p.stdout), (2, ""))
    p = subprocess.run(["bash", gate, "acquire", "fixture", "missing", "2", "0"],
                       env=missing_env, cwd=empty,
                       capture_output=True, text=True, timeout=10)
    check("missing-session-acquire-refused",
          (p.returncode, p.stdout, (state / "wave-slots").read_text()), (2, "", ""))

print(f"selftest {passed}/{total}")
sys.exit(0 if passed == total else 1)
PY
