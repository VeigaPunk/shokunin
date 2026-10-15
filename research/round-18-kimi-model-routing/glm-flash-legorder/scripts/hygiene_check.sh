#!/usr/bin/env bash
# hygiene_check.sh <dir> -- fail (exit 1) if any file under <dir> carries a
# credential-shaped token. Mirrors census/scripts/hygiene_check.sh: shape-based
# patterns so it catches any secret, not just the two keys known to exist.
set -uo pipefail
DIR="${1:-.}"
PAT="/[0-9a-fA-F]{32}\.[A-Za-z0-9]{16}/,
/sk-[A-Za-z0-9._-]{16,}/,
/(Bearer )[A-Za-z0-9._-]{16,}/,
/\"[A-Za-z0-9._-]{32,}\":/"
HITS=0
while IFS= read -r f; do
  out=$(grep -nEH "$PAT" "$f" 2>/dev/null) && { printf '%s\n' "$out"; HITS=$((HITS+1)); }
done < <(find "$DIR" -type f ! -path '*/.git/*')
if [ "$HITS" -eq 0 ]; then
  echo "HYGIENE OK: 0 credential-shaped hits under $DIR"
  exit 0
fi
echo "HYGIENE FAIL: $HITS file(s) with credential-shaped tokens" >&2
exit 1
