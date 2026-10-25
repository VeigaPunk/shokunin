#!/bin/sh
# mutate.sh -- proof that `root-ledgers.py --selftest` can fail.
#
# Copies the gate and its data dir (.ufo/gates/root-ledgers/) into a temp
# tree, applies each mutant via a single python string-replace on the COPY
# only, and runs --selftest on every mutant (expecting exit 1) plus the
# unmodified copy (expecting exit 0). Prints `mutants killed K/M` and
# exits 0 iff K == M and the unmodified copy passed.
#
# Run from anywhere; paths resolve relative to this file. POSIX sh.
set -u

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/../../../.." && pwd)
GATES="$ROOT/.ufo/gates"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Replace exactly one occurrence of $2 with $3 in file $1 (the temp copy).
apply_mutant() {
    FILE=$1 OLD=$2 NEW=$3 python3 - <<'PY'
import os
path = os.environ["FILE"]
src = open(path, encoding="utf-8").read()
old, new = os.environ["OLD"], os.environ["NEW"]
assert src.count(old) == 1, "anchor not unique: %r" % old
open(path, "w", encoding="utf-8").write(src.replace(old, new, 1))
PY
}

# run_mutant NAME OLD-ANCHOR NEW-TEXT
run_mutant() {
    M=$((M + 1)); name=$1; old=$2; new=$3
    mkdir -p "$TMP/$name/.ufo"
    cp -r "$GATES" "$TMP/$name/.ufo/" || exit 2
    gate="$TMP/$name/.ufo/gates/root-ledgers.py"
    if ! apply_mutant "$gate" "$old" "$new"; then
        echo "mutant $name: ANCHOR MISSING"
        exit 2
    fi
    python3 "$gate" --selftest >/dev/null 2>&1
    rc=$?
    if [ "$rc" -eq 1 ]; then
        K=$((K + 1))
        echo "mutant $name: killed (exit 1)"
    else
        echo "mutant $name: SURVIVED (exit $rc)"
    fi
}

# Unmodified copy must self-test clean.
mkdir -p "$TMP/unmodified/.ufo"
cp -r "$GATES" "$TMP/unmodified/.ufo/" || exit 2
python3 "$TMP/unmodified/.ufo/gates/root-ledgers.py" --selftest >/dev/null 2>&1
base_rc=$?

K=0
M=0

# Each mutant disables exactly one check or flips one comparison.
run_mutant scorecard-header-flip \
    'if sc_header != pinned["scorecard_header"]:' \
    'if sc_header == pinned["scorecard_header"]:'
run_mutant log-header-flip \
    'if log_header != pinned["log_header"]:' \
    'if log_header == pinned["log_header"]:'
run_mutant registry-check-disable \
    'if reg_idx is None:' \
    'if reg_idx is not None:'
run_mutant aggregator-check-disable \
    'if agg_idx is None:' \
    'if agg_idx is not None:'
run_mutant ordering-flip \
    'if reg_idx >= agg_idx:' \
    'if reg_idx < agg_idx:'
run_mutant row-prefix-swap \
    'l.startswith(row_prefix)' \
    'l.startswith(agg_prefix)'
run_mutant header-pin-echo \
    'sc_header = sc_lines[0] if sc_lines else ""' \
    'sc_header = pinned["scorecard_header"]'
run_mutant fence-tracking-disable \
    'sc_lines = mask_fences(scorecard_text.splitlines())' \
    'sc_lines = scorecard_text.splitlines()'
run_mutant duplicate-check-disable \
    'if reg_count > 1:' \
    'if reg_count > 2:'

echo "mutants killed $K/$M"
if [ "$K" -eq "$M" ] && [ "$base_rc" -eq 0 ]; then
    exit 0
fi
if [ "$base_rc" -ne 0 ]; then
    echo "unmodified copy selftest exit $base_rc (want 0)" >&2
fi
exit 1
