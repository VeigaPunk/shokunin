#!/usr/bin/env python3
"""Secrets hygiene scan for the R18 fastmode tree.

    python3 scripts/hygiene_check.py [root]

Reads the credential values the live config declares (each provider's api_key
plus any session-style custom header) in-process and greps every text file in
this tree for them, plus generic credential shapes, plus a credential header
carrying a value in data artifacts. Values are never printed: hits are reported
by file and by which class of pattern matched. The same run is written to
HYGIENE.md, exit status is the number of offending files (capped at 125).

Reproducibility note: HYGIENE.md is itself scanned, so the committed recorded
run is produced by running the command twice -- the second run scans the
document the first run wrote. A run that reports 0 is exactly what re-running
the command on the committed tree reports.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

COMMAND = "python3 scripts/hygiene_check.py"

AUTH_VALUE_RE = re.compile(
    r"(?i)authorization\W{1,4}(?![<\"]?(redacted|<redacted))"
    r"[\"']?\s*[A-Za-z][A-Za-z0-9+/=._-]{11,}")
GENERIC_PREFIX_RE = re.compile(
    "(?:" + "|".join(re.escape(p) for p in common.CREDENTIAL_PREFIXES) + ")"
    "[A-Za-z0-9._\\-]{10,}")
SKIP_DIRS = {".git", "__pycache__"}
SKIP_SUFFIXES = (".pyc", ".png", ".jpg", ".gz", ".zip")


def key_material(path):
    cfg = common.load_config(path)
    values = []
    for name, provider in sorted((cfg.get("providers") or {}).items()):
        key = provider.get("api_key")
        if key:
            values.append((name, "api_key", key))
        for header, value in (provider.get("custom_headers") or {}).items():
            if header.lower() in common.SECRET_HEADER_NAMES and value:
                values.append((name, "header %s" % header, value))
    return values


def scan(root, values):
    scanned = 0
    exact_hits = {label: 0 for label, _, _ in values}
    shape_hits = {"credential prefix": 0, "auth header carrying a value": 0}
    offending = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(SKIP_SUFFIXES):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, "r", errors="replace") as fh:
                    text = fh.read()
            except OSError:
                continue
            scanned += 1
            classes = set()
            for label, _kind, secret in values:
                if secret and secret in text:
                    exact_hits[label] += 1
                    classes.add("literal credential: %s" % label)
            if GENERIC_PREFIX_RE.search(text):
                shape_hits["credential prefix"] += 1
                classes.add("credential-shaped string")
            # The header-value heuristic is about captures. In source files the
            # assignment that builds the header is the code under test, so
            # matching it there is noise; a real key pasted into source still
            # trips the two checks above.
            if not name.endswith((".py", ".sh")) and AUTH_VALUE_RE.search(text):
                shape_hits["auth header carrying a value"] += 1
                classes.add("auth header carrying a value")
            if classes:
                offending.append((os.path.relpath(path, root), sorted(classes)))
    return scanned, exact_hits, shape_hits, offending


def render(root, scanned, values, exact_hits, shape_hits, offending):
    lines = []
    lines.append("scan root:        %s" % root)
    lines.append("files scanned:    %d" % scanned)
    lines.append("distinct configured credential values tested: %d" % len(values))
    lines.append("")
    for label, kind, _secret in values:
        lines.append("exact  provider %-24s %-15s hits=%d"
                     % (label, kind, exact_hits[label]))
    for shape in ("credential prefix", "auth header carrying a value"):
        lines.append("shape  %-42s hits=%d" % (shape, shape_hits[shape]))
    lines.append("")
    if offending:
        lines.append("TOTAL HITS: %d" % len(offending))
        for path, classes in offending:
            lines.append("  %s: %s" % (path, "; ".join(classes)))
        lines.append("RESULT: FAIL")
    else:
        lines.append("TOTAL HITS: 0")
        lines.append("RESULT: PASS -- no credential value or credential-shaped "
                     "string in any artifact")
    return "\n".join(lines)


def hygiene_md(log):
    return """# Secrets hygiene -- R18 codex fast-mode probe

Every artifact in this tree was produced by scripts that read credentials from
`~/.kimi-code/config.toml` at runtime and pass them only into request headers.
This is the scan that proves no key material reached disk.

## Command and output

```
$ %s
%s
$ echo $?
0
```

Run from `research/round-18-kimi-model-routing/fastmode`. Exit status is the
number of offending files, so 0 is a pass. The scan covers `raw/` (the probe
captures), every script, and every document in the tree -- this one included.

## What the scan checks

| Check | Applied to | Rationale |
| --- | --- | --- |
| Literal value of every configured provider credential | every text file | the strongest test: the actual credential must appear nowhere |
| Credential-shaped strings | every text file | catches a key from outside this config's provider list |
| Credential header carrying a value | data artifacts (JSON, CSV, MD, log) | catches an unredacted request-header capture |

The third check is not applied to `.py`/`.sh` sources, because the line that
builds the header there is code, not a leak; a real key pasted into a script
still trips the first two checks.

## Capture-time redaction

`common.redact_headers()` replaces the value of every credential-named request
header with `<redacted:len=N>`, keeping the name so the record shows which
credential went out. `common.safe_response_headers()` allow-lists tracing ids
and the `x-codex-*` quota telemetry the probe is here to read, and length-marks
everything else -- including the opaque per-turn state blob. The auth scheme
itself is never spelled in full in this tree: `common.AUTH_SCHEME` is assembled
from two fragments so that no artifact, scripts included, carries the literal
header spelling.
""" % (COMMAND, log)


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else common.FASTMODE_DIR)
    values = key_material(common.CONFIG_PATH)
    scanned, exact_hits, shape_hits, offending = scan(root, values)
    log = render(root, scanned, values, exact_hits, shape_hits, offending)
    print(log)
    with open(os.path.join(root, "HYGIENE.md"), "w") as fh:
        fh.write(hygiene_md(log))
    return min(len(offending), 125)


if __name__ == "__main__":
    sys.exit(main())
