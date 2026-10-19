#!/bin/sh
# classify.sh — classify every hunk of the 31baf5c clobber of the fleet root
# ledgers (SCORECARD.md, LOG.md) as kotoba bytes vs candidate fleet entries.
#
# Read-only (git reads only; scratch in mktemp). Re-runnable from the lane
# worktree root:
#   sh .ufo/waves/round-16/clobber/classify.sh
#
# Every repository command uses `git -C "$ROOT"` — this harness's `cd` is
# unsafe (can fail silently into the fleet root), so the script never relies
# on the ambient cwd beyond the one explicit, fail-closed root resolution.
#
# Revisions:
#   PRE    = 12f2da5  last good fleet ledger bytes (= last edit 0b1ac3b)
#   POST   = 31baf5c  the clobber commit (kotodama-shokunin backlog sweep)
#   KOTOBA = b7470d7  kotoba-shokunin "round 36" — blob-identical source of the
#                     31baf5c ledger contents (3fc970db / 99de619d)
#
# Hunk rule: every added line of a hunk present verbatim in the kotoba blob
# (including a pure-deletion hunk, vacuously) classifies the hunk as
# "kotoba-bytes"; any added line absent from the kotoba blob makes the hunk a
ROOT=$(git rev-parse --show-toplevel) || exit 2
# Fail closed if resolved from the wrong repo (e.g. the fleet root): this
# script only exists inside the lane worktree.
[ -f "$ROOT/.ufo/waves/round-16/clobber/classify.sh" ] || {
    echo "!! run from the lane worktree root (resolved ROOT=$ROOT)" >&2
    exit 2
}
#

ROOT=$(git rev-parse --show-toplevel) || exit 2
cd "$ROOT" || exit 2   # belt-and-braces only; all git calls below pin -C "$ROOT"

PRE=12f2da5
POST=31baf5c
KREV=b7470d7
KREPO=/home/vgpnk/Projects/shokunin/kotoba-shokunin

TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT

GRAND_CARRY=0

for f in SCORECARD.md LOG.md; do
    echo "================================================================"
    echo "FILE: $f"
    echo "----------------------------------------------------------------"

    echo "-- git diff --numstat $PRE $POST -- $f"
    git -C "$ROOT" diff --numstat "$PRE" "$POST" -- "$f"

    git -C "$KREPO" show "$KREV:$f" > "$TMP/kfile" 2>/dev/null || {
        echo "!! could not read kotoba $KREV:$f"
        exit 2
    }
    git -C "$ROOT" diff -U0 "$PRE" "$POST" -- "$f" > "$TMP/diff"

    # Extract added lines (diff body '+' lines only, never '+++ ' headers).
    grep '^+' "$TMP/diff" | grep -v '^+++ ' | cut -c2- > "$TMP/added"

    echo "-- blob equality"
    b_post=$(git -C "$ROOT" rev-parse "$POST:$f")
    b_koto=$(git -C "$KREPO" rev-parse "$KREV:$f")
    if [ "$b_post" = "$b_koto" ]; then eq=IDENTICAL; else eq=DIFFERENT; fi
    echo "   $POST:$f      = $b_post"
    echo "   kotoba $KREV:$f = $b_koto"
    echo "   => $eq"

    hunks=0; k_hunks=0; f_hunks=0
    cur_a=0; cur_k=0; cur_abs=0; cur_hdr=""

    flush() {
        [ -z "$cur_hdr" ] && return 0
        hunks=$((hunks + 1))
        if [ "$cur_abs" -eq 0 ]; then
            cls="kotoba-bytes"; k_hunks=$((k_hunks + 1))
        else
            cls="fleet-entry"; f_hunks=$((f_hunks + 1))
        fi
        echo "   hunk $hunks $cur_hdr added=$cur_a in_kotoba=$cur_k absent=$cur_abs => $cls"
    }

    while IFS= read -r line; do
        case $line in
            @@*)
                flush
                cur_hdr=$line; cur_a=0; cur_k=0; cur_abs=0
                ;;
            +++\ *)
                : ;;  # file header "+++ b/<file>" — never a body line
            +*)
                cur_a=$((cur_a + 1))
                body=${line#+}
                if grep -qxF -- "$body" "$TMP/kfile" 2>/dev/null; then
                    cur_k=$((cur_k + 1))
                else
                    cur_abs=$((cur_abs + 1))
                fi
                ;;
        esac
    done < "$TMP/diff"
    flush

    echo "-- hunk classification: $hunks total, $k_hunks kotoba-bytes, $f_hunks fleet-entry"

    # Whole-file verbatim tally over every added line.
    n_k=0; n_a=0
    : > "$TMP/absent"
    while IFS= read -r l; do
        if grep -qxF -- "$l" "$TMP/kfile" 2>/dev/null; then
            n_k=$((n_k + 1))
        else
            n_a=$((n_a + 1))
            printf '%s\n' "$l" >> "$TMP/absent"
        fi
    done < "$TMP/added"
    n_t=$(wc -l < "$TMP/added")
    echo "-- added lines: $n_t total; $n_k present verbatim in kotoba $KREV:$f; $n_a absent (candidate fleet entries)"
    if [ "$n_a" -gt 0 ]; then
        echo "   ABSENT LINES (carry-forward candidates):"
        sed 's/^/   | /' "$TMP/absent"
    fi
    GRAND_CARRY=$((GRAND_CARRY + n_a))

    # Fleet ## headings at PRE absent verbatim at POST.
    git -C "$ROOT" show "$PRE:$f"  | grep '^## ' > "$TMP/h_pre"  2>/dev/null || :
    git -C "$ROOT" show "$POST:$f" | grep '^## ' > "$TMP/h_post" 2>/dev/null || :
    : > "$TMP/hlost"
    while IFS= read -r h; do
        grep -qxF -- "$h" "$TMP/h_post" 2>/dev/null || printf '%s\n' "$h" >> "$TMP/hlost"
    done < "$TMP/h_pre"
    n_h=$(wc -l < "$TMP/hlost")
    echo "-- '## ' headings at $PRE absent verbatim at $POST: $n_h"
    sed 's/^/   /' "$TMP/hlost"
    echo
done

echo "================================================================"
echo "CARRY-FORWARD SET: $GRAND_CARRY added lines absent from kotoba bytes"
if [ "$GRAND_CARRY" -eq 0 ]; then
    echo "=> every added line across both ledgers is kotoba $KREV bytes;"
    echo "   nothing of the fleet record survived inside the clobber."
fi
exit 0
