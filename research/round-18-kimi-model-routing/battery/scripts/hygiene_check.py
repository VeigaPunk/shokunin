#!/usr/bin/env python3
"""Secrets hygiene scan for the R18 battery tree.

    python3 scripts/hygiene_check.py [root]

Reads every credential the config declares and greps the battery tree for it,
plus generic credential shapes, so the artifacts can be shown to carry no key
material. Never prints a credential: hits are reported by file and by which
class of pattern matched. Exit status is the number of offending files
(capped at 125) so the check fails loudly.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

AUTH_VALUE_RE = re.compile(
    r"(?i)authorization\W{1,4}(?![<\"]?(redacted|<redacted))"
    r"[\"']?\s*[A-Za-z][A-Za-z0-9+/=._-]{11,}")
GENERIC_PREFIX_RE = re.compile(
    "(?:" + "|".join(re.escape(p) for p in common.CREDENTIAL_PREFIXES) + ")"
    "[A-Za-z0-9._\\-]{10,}")
SKIP_DIRS = {".git", "__pycache__"}
SKIP_SUFFIXES = (".pyc", ".png", ".jpg", ".gz", ".zip")


def key_material(path):
    cfg, _raw = common.load_config(path)
    values = []
    for name, provider in (cfg.get("providers") or {}).items():
        key = provider.get("api_key")
        if key:
            values.append((name, key))
    return values


def scan(root, values):
    hits = []
    scanned = 0
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
            for provider, key in values:
                if key and key in text:
                    classes.add("literal key from provider %s" % provider)
            if GENERIC_PREFIX_RE.search(text):
                classes.add("credential-shaped string")
            # The header-value heuristic is about captures. In source files the
            # assignment `headers[...] = AUTH_SCHEME + key` is the code that
            # builds the header, so matching it there is noise; a real key
            # pasted into source still trips the two checks above.
            if not name.endswith((".py", ".sh")) and AUTH_VALUE_RE.search(text):
                classes.add("auth header carrying a value")
            if classes:
                hits.append((os.path.relpath(path, root), sorted(classes)))
    return scanned, hits


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else common.BATTERY_DIR
    values = key_material(common.CONFIG_PATH)
    scanned, hits = scan(root, values)
    print("hygiene scan over %s" % root)
    print("files scanned: %d" % scanned)
    print("credentials checked: %d (values never printed)" % len(values))
    if not hits:
        print("hits: 0")
        return 0
    print("hits: %d" % len(hits))
    for path, classes in hits:
        print("  %s: %s" % (path, "; ".join(classes)))
    return min(len(hits), 125)


if __name__ == "__main__":
    sys.exit(main())
