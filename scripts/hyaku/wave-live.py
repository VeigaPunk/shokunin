#!/usr/bin/env python3
"""Count potentially active agents, emitting only one decimal integer.

Usage: python3 wave-live.py SESSION_DIR

Read at most 256 KiB + one boundary byte per JSONL, never transcript bodies
from .md files. JSONL append order wins: session_exit and assistant error /
aborted close a run; subsequent user, assistant, tool or incoming custom_message
activity reopens it. A final successful assistant also needs a nonempty regular
.md artifact strictly newer than that message (equal timestamps are ambiguous).
Usage and custom bookkeeping do not reopen a completed run. No transcript
content is executed or printed.

Unknown, incomplete, unreadable, changing or oversized decisive records count
as active. A truncated leading line is skipped: a later complete terminal marker
can still settle the run. If all decisive history fell outside the bounded tail,
count active rather than trusting an old artifact. Walk nested agent directories
without following symlinks; nonregular *.jsonl entries count conservatively.
This is a snapshot estimate, not a scheduler/process liveness oracle.
"""
import datetime
import json
import math
import os
import stat
import sys

TAIL_BYTES = 256 * 1024
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
FILE_FLAGS = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC


def open_directory(path):
    """Resolve every component without following directory symlinks."""
    fd = os.open("/" if os.path.isabs(path) else ".", DIR_FLAGS)
    try:
        for part in path.split(os.sep):
            if part in ("", "."):
                continue
            child = os.open(part, DIR_FLAGS, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def timestamp(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            if math.isfinite(value):
                return value / 1000 if value > 100_000_000_000 else value
        except OverflowError:
            return None
    if isinstance(value, str):
        try:
            dt = datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
            if dt.tzinfo is not None:
                return dt.timestamp()
        except (ValueError, OverflowError, OSError):
            pass
    return None


def success_artifact(dir_fd, name, record, message):
    when = timestamp(record.get("timestamp"))
    if when is None:
        when = timestamp(message.get("completedAt"))
    if when is None:
        when = timestamp(message.get("timestamp"))
    if when is None:
        return False
    try:
        artifact = os.stat(name[:-6] + ".md", dir_fd=dir_fd, follow_symlinks=False)
    except OSError:
        return False
    return (stat.S_ISREG(artifact.st_mode) and artifact.st_size > 0
            and artifact.st_mtime > when)


def tail_active(data, dir_fd, name):
    if not data or not data.endswith(b"\n"):
        return True
    # Reverse order lets a complete final exit supersede earlier malformed / huge
    # activity, while malformed data AFTER an exit cannot accidentally free a seat.
    for line in reversed(data.split(b"\n")):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except (ValueError, UnicodeError, RecursionError):
            return True
        if not isinstance(record, dict):
            return True
        kind = record.get("type")
        if kind == "session_exit":
            return False
        if kind == "custom":
            custom = record.get("customType")
            if not isinstance(custom, str) or not custom:
                return True
            if custom == "session_exit":
                return False
            if custom == "tool_execution_start":
                return True
            # Custom entries store bookkeeping; delivered messages have their own
            # custom_message entry type, not this metadata-only type.
            continue
        if kind == "message":
            message = record.get("message")
            if not isinstance(message, dict):
                return True
            if message.get("role") == "assistant":
                reason = message.get("stopReason")
                if reason in ("error", "aborted"):
                    return False
                if reason == "stop":
                    return not success_artifact(dir_fd, name, record, message)
            return True
        if kind == "custom_message":
            return True
        if kind in ("model_usage", "credential_pin", "session", "model_change",
                    "thinking_level_change", "compaction", "branch_summary",
                    "session_info", "label"):
            continue
        return True
    return True


def agent_active(dir_fd, name):
    try:
        fd = os.open(name, FILE_FLAGS, dir_fd=dir_fd)
        try:
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode):
                return True
            offset = max(0, before.st_size - TAIL_BYTES)
            data = os.pread(fd, TAIL_BYTES + 1, max(0, offset - 1))
            if offset:
                boundary = data.find(b"\n")
                data = data[boundary + 1:] if boundary >= 0 else b""
            active = tail_active(data, dir_fd, name)
            after = os.fstat(fd)
            current = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
            # Appends/replacement during inspection invalidate a terminal snapshot.
            stable = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
            return active or any(
                (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns) != stable
                for s in (after, current))
        finally:
            os.close(fd)
    except OSError:
        return True


def count_agents(dir_fd):
    total = 0
    try:
        with os.scandir(dir_fd) as entries:
            for entry in entries:
                if entry.name.endswith(".jsonl"):
                    total += agent_active(dir_fd, entry.name)
                    continue
                try:
                    if not entry.is_dir(follow_symlinks=False):
                        continue
                    child = os.open(entry.name, DIR_FLAGS, dir_fd=dir_fd)
                    try:
                        total += count_agents(child)
                    finally:
                        os.close(child)
                except OSError:
                    total += 1  # Unreadable subtree: do not silently report zero.
    except OSError:
        total += 1
    return total


def main():
    if len(sys.argv) != 2 or not sys.argv[1]:
        print("usage: wave-live.py SESSION_DIR", file=sys.stderr)
        return 2
    try:
        fd = open_directory(sys.argv[1])
        try:
            total = count_agents(fd)
        finally:
            os.close(fd)
    except (OSError, RecursionError):
        print("wave-live: cannot inspect session directory safely", file=sys.stderr)
        return 2
    print(total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
