#!/bin/sh
# One-pass obligation-preservation test for the round-11 PROTOCOL.md compaction.
# Usage: verify-census.sh <target-file> [census.tsv]
# Exit 0 iff every census predicate hits the target. Any MISS = obligation lost.
target=${1:?usage: verify-census.sh <target-file> [census.tsv]}
census=${2:-"$(dirname "$0")/obligation-census.tsv"}
total=0; miss=0
while IFS="$(printf '\t')" read -r id sec obl pred; do
    [ "$id" = "id" ] && continue
    [ -z "$id" ] && continue
    total=$((total + 1))
    if grep -qE "$pred" "$target"; then
        printf 'PASS %s\n' "$id"
    else
        printf 'MISS %s [%s] %s\n' "$id" "$sec" "$obl"
        miss=$((miss + 1))
    fi
done < "$census"
printf '\n%d/%d obligations found; %d MISSING\n' "$((total - miss))" "$total" "$miss"
[ "$miss" -eq 0 ]
