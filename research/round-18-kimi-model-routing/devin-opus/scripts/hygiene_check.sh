#!/usr/bin/env bash
# Secrets-hygiene gate for the M10 (devin-opus) artifacts.
#
#   bash scripts/hygiene_check.sh
#
# Same design as the census/definitions/battery gates already in this round: scan
# every file under this scope directory for
#   * the credential prefix spellings present in ~/.kimi-code/config.toml,
#   * the auth-scheme spelling used on the wire,
#   * distinctive fragments of every real api_key in the config,
#   * every custom-header *value* from the config,
#   * distinctive fragments of OAuth tokens living in this shell's env.
#
# The pattern literals for the first group are assembled from adjacent fragments so
# this checker's own source does not contain the strings it hunts for, which keeps
# the scan honest across the whole tree (checker and probe scripts included).
# Pattern values are written to a mktemp file outside the scope dir and never
# echoed; only labels are printed.
#
# Exit status 0 = clean (0 hits), 1 = at least one hit.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG="${KIMI_CONFIG:-$HOME/.kimi-code/config.toml}"
export KIMI_CONFIG="$CONFIG"

PREFIX_A="s""k-"
PREFIX_B="Bea""rer "
PREFIX_C="oc_""sk_"

PATFILE="$(mktemp)"
LABELS="$(mktemp)"
trap 'rm -f "$PATFILE" "$LABELS"' EXIT

add_pattern() { printf '%s\n' "$2" >>"$PATFILE"; printf '%s\n' "$1" >>"$LABELS"; }

add_pattern "credential-prefix-A" "$PREFIX_A"
add_pattern "auth-scheme-spelling-B" "$PREFIX_B"
add_pattern "credential-prefix-C" "$PREFIX_C"

while IFS= read -r key; do
  [ "${#key}" -ge 24 ] || continue
  add_pattern "api_key-head8" "${key:0:8}"
  add_pattern "api_key-mid16" "${key:8:16}"
  add_pattern "api_key-tail16" "${key: -16}"
done < <(grep -oP '^\s*api_key\s*=\s*"\K[^"]+' "$CONFIG" | grep -v '^$' | sort -u)

while IFS= read -r val; do
  [ "${#val}" -ge 8 ] || continue
  add_pattern "custom-header-value" "$val"
done < <(python3 - <<'PY'
import os, tomllib
with open(os.environ["KIMI_CONFIG"], "rb") as fh:
    cfg = tomllib.load(fh)
for _name, prov in (cfg.get("providers") or {}).items():
    for _h, v in (prov.get("custom_headers") or {}).items():
        print(v)
PY
)

for var in OPENAI_CODEX_TOKEN XAI_OAUTH_TOKEN; do
  val="${!var:-}"
  [ "${#val}" -ge 24 ] || continue
  add_pattern "env-$var-mid16" "${val:4:16}"
  add_pattern "env-$var-tail16" "${val: -16}"
done

echo "scope dir  : $HERE"
echo "config     : $CONFIG"
echo "config sha : $(sha256sum "$CONFIG" | cut -d' ' -f1)"
echo "patterns   : $(wc -l <"$PATFILE") (values never printed)"
echo

paste -d'|' "$LABELS" "$PATFILE" | while IFS='|' read -r label pattern; do
  count=$(grep -rIlF -e "$pattern" "$HERE" 2>/dev/null | wc -l)
  printf '  %-28s files_matched=%s\n' "$label" "$count"
done
echo

hits=$(grep -rInF -f "$PATFILE" "$HERE" 2>/dev/null)
hit_count=$(printf '%s' "$hits" | grep -c .)
echo "TOTAL HIT LINES: $hit_count"
if [ "$hit_count" -ne 0 ]; then
  echo "--- offending lines (file:line:content) ---"
  printf '%s\n' "$hits"
  exit 1
fi
echo "RESULT: CLEAN (0 hits)"
exit 0