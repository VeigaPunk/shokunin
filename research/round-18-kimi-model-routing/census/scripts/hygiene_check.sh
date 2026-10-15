#!/usr/bin/env bash
# Secrets-hygiene gate for the R18 census artifacts.
#
#   bash scripts/hygiene_check.sh
#
# Scans every file under this census directory for
#   * the credential prefix spellings that appear in ~/.kimi-code/config.toml,
#   * the auth-scheme spelling used on the wire,
#   * distinctive fragments of every real api_key in the config,
#   * every custom-header *value* from the config,
#   * distinctive fragments of the OAuth tokens present in this shell's env.
#
# Design notes:
#   * The pattern literals for the first group are assembled from adjacent shell
#     fragments on purpose. That keeps this checker's own source free of the
#     strings it hunts for, so the scan can cover the whole tree -- checker and
#     probe scripts included -- without matching itself.
#   * Key/header values are read from the config at runtime into a mktemp file
#     outside the census dir. Pattern *values* are never echoed, only labels.
#   * Header *names* (e.g. the session header name) are deliberately NOT patterns:
#     the raw captures legitimately record which credential headers were sent,
#     and a name is not credential material. Their values are covered above.
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

# Fragments of every configured api_key: head, middle and tail slices.
while IFS= read -r key; do
  [ "${#key}" -ge 24 ] || continue
  add_pattern "api_key-head8" "${key:0:8}"
  add_pattern "api_key-mid16" "${key:8:16}"
  add_pattern "api_key-tail16" "${key: -16}"
done < <(grep -oP '^\s*api_key\s*=\s*"\K[^"]+' "$CONFIG" | grep -v '^$' | sort -u)

# Every custom-header value declared in the config (credential-bearing).
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

# Fragments of OAuth tokens that live in the environment (never in config).
for var in OPENAI_CODEX_TOKEN XAI_OAUTH_TOKEN; do
  val="${!var:-}"
  [ "${#val}" -ge 24 ] || continue
  add_pattern "env-$var-mid16" "${val:4:16}"
  add_pattern "env-$var-tail16" "${val: -16}"
done

echo "census dir : $HERE"
echo "config     : $CONFIG"
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
