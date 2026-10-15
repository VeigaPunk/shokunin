#!/usr/bin/env bash
# Secrets-hygiene gate for the R18 definitions audit (mission M2).
#
# Two independent scans over every file in this tree (raw captures included):
#   1. exact match against every credential value in the live config -- the
#      decisive test, since it covers the actual keys rather than a pattern
#   2. generic credential shapes (prefixes, bearer tokens, key=... assignments)
#
# Key values are read from the config in-process and never printed, echoed into
# an argument list, or written to a file. Only counts leave this script.
#
#   bash scripts/hygiene_check.sh            # scan, print summary, write HYGIENE.md
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

python3 - <<'PY' | tee /tmp/r18-defs-hygiene.txt
import json, os, re, sys, tomllib

DEFS = os.path.dirname(os.path.abspath("."))
CP = os.path.expanduser("~/.kimi-code/config.toml")
# prefixes assembled from fragments so this script does not itself contain a
# credential-shaped literal and the scan stays exact
PREFIXES = ("s" + "k-", "s" + "k-sp-", "oc_" + "sk_")
SHAPES = [
    ("credential prefix", re.compile("(?:" + "|".join(re.escape(p) for p in PREFIXES) + r")[A-Za-z0-9._\-]{8,}")),
    ("bearer token", re.compile(r"(?i)\bBea" + r"rer [A-Za-z0-9._\-]{16,}")),
    ("assigned secret", re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|secret|password)\s*[=:]\s*[A-Za-z0-9._\-]{12,}")),
]

with open(CP, "rb") as fh:
    cfg = tomllib.load(fh)

exact = []
NON_SECRET_HEADER = re.compile(r"(?i)^(openai-beta|originator|anthropic-version|x-request-id)$")
for pid, pc in cfg.get("providers", {}).items():
    if pc.get("api_key"):
        exact.append(("provider %s api_key" % pid, pc["api_key"]))
    for name, v in (pc.get("custom_headers") or {}).items():
        # a custom header is credential-bearing only if it names one; OpenAI-Beta
        # and originator are plain protocol headers, not secrets
        if re.search(r"(?i)(auth|key|token|secret|session|cookie)", name) \
                and not NON_SECRET_HEADER.match(name):
            exact.append(("provider %s header %s" % (pid, name), v))
for svc, sc in cfg.get("services", {}).items():
    if sc.get("api_key"):
        exact.append(("service %s api_key" % svc, sc["api_key"]))

files = []
for root, dirs, names in os.walk(DEFS):
    dirs[:] = [d for d in dirs if d != ".git"]
    for n in names:
        p = os.path.join(root, n)
        if os.path.getsize(p) < 4_000_000:
            files.append(p)

print("scan root:        %s" % DEFS)
print("files scanned:    %d" % len(files))
print("distinct configured credential values tested: %d" % len({v for _, v in exact}))
print()

total = 0
for label, value in exact:
    hits = []
    needle = value.encode()
    for p in files:
        with open(p, "rb") as fh:
            if needle in fh.read():
                hits.append(os.path.relpath(p, DEFS))
    total += len(hits)
    print("exact  %-44s hits=%d %s" % (label, len(hits), ",".join(hits[:5])))

print()
for label, rx in SHAPES:
    n = 0
    where = []
    for p in files:
        try:
            with open(p, "r", errors="replace") as fh:
                text = fh.read()
        except Exception:
            continue
        m = rx.findall(text)
        if m:
            n += len(m)
            where.append("%s(%d)" % (os.path.relpath(p, DEFS), len(m)))
    total += n
    print("shape  %-44s hits=%d %s" % (label, n, ",".join(where[:5])))

print()
print("TOTAL HITS: %d" % total)
print("RESULT: %s" % ("PASS -- no credential value or credential-shaped string in any artifact"
                      if total == 0 else "FAIL -- investigate the hits above"))
sys.exit(0 if total == 0 else 1)
PY
status=${PIPESTATUS[0]}
{
  echo "# Secrets hygiene -- R18 definitions audit"
  echo
  echo "Gate: \`bash scripts/hygiene_check.sh\` scans every file in this tree, raw"
  echo "captures included, for (1) the exact credential values in the live config and"
  echo "(2) generic credential shapes."
  echo
  echo "Credential values are read from the config inside the scan process and are"
  echo "never printed, passed as arguments, or written to disk; only counts leave it."
  echo
  echo '```'
  cat /tmp/r18-defs-hygiene.txt
  echo '```'
  echo
  echo "Exit status: ${status} (0 = clean). Probe captures record credential header"
  echo "names with a \`<redacted:len=N>\` marker instead of values"
  echo "(see scripts/common.py \`redact_headers\`)."
} > HYGIENE.md
exit ${status}
