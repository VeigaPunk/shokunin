#!/bin/sh
# ===========================================================================
# verify-protocol.sh — committed preservation gate for the round-13 PROTOCOL.md
# compaction (526 lines -> <=470).  Owner: protocol lane.
# Write scope: .ufo/waves/round-13/ only.  Read-only everywhere else.
#
# USAGE
#   sh verify-protocol.sh <target.md> [--census TSV] [--max-lines N]
#                        [--max-body-refs N] [--selftest] [--json]
#                        [--appendix FILE] [--appendix-census TSV]
#                        [--max-appendix-lines N]
#
# TWO MODES
#   single-file (default)   the whole protocol is <target.md>; all nine checks
#                           read it (this is the mode the eight seeded selftest
#                           cases prove).
#   two-file (--appendix F) the body is <target.md> and the incident digest lives
#                           in F (the round-13 design: a <=4-line pointer block in
#                           the body, the digest table in PROTOCOL-APPENDIX.md).
#                           `structure` then requires the eight body headings in
#                           order *and* an `## Appendix … incident digest …`
#                           heading in F; `appendix` resolves the body's
#                           pointers against F's table; `modals` applies the body
#                           floors to the body's eight sections and the floor in
#                           modal-census-appendix.tsv to F; `caps` bounds the
#                           body's lines by --max-lines and F's by
#                           --max-appendix-lines; `census` runs the body census
#                           and annotates any MISS whose predicate matches F as
#                           appendix-scoped; `anchors` and `xref` read body + F.
#                           The single-file expected values are untouched.
#
# EXIT MAP (0/1 pinned fleet-wide; 2/3 declared and mapped, per ## Gate standard)
#   0  clean               every check passed
#   1  findings            >=1 check emitted a finding  (== failed)
#   2  could-not-evaluate  missing target / missing expected-value file / bad usage
#   3  no-baseline         --selftest requested without committed expected values
#
# OUTPUT
#   INFO <check-id> <detail>    one line per check: what was evaluated
#   FAIL <check-id> <detail>    one line per finding
#   verify-protocol: <clean|findings> checks=<n> failed=<n>
#   `failed` counts distinct check ids that emitted at least one finding, so a
#   census with three MISS rows reports failed=1.
#
# CHECKS (ids are stable strings)
#   census     delegate to ../round-11/verify-census.sh <body> <census-tsv>;
#              default census is obligation-census-r13.tsv when it exists, else
#              round-11/obligation-census.tsv; the path used and its row count
#              are reported on the INFO line. Every MISS row is a finding. In
#              two-file mode a MISS whose predicate matches the appendix FILE is
#              annotated `[appendix-scoped]` so the integrator can retarget it,
#              and --appendix-census TSV folds that table's MISSes into this
#              same check id.
#   anchors    every line of anchor-phrases.txt must appear verbatim (grep -F
#              semantics, implemented with awk index()) in the target, or in
#              body + apppendix FILE in two-file mode.
#   modals     per-`## `-section count of normative tokens must be >= the floor
#              recorded in modal-census.tsv (body floors only in two-file mode,
#              which drops the `## Appendix` row) plus, in two-file mode, the
#              modal-census-appendix.tsv floor applied to the appendix FILE.
#   caps       total lines <= --max-lines (default 470) and body inline
#              round-incident refs <= --max-body-refs (default 4); body =
#              everything before the `## Appendix` heading. In two-file mode the
#              appendix FILE's lines are reported and bounded by
#              --max-appendix-lines (default 60).
#   structure  the nine `## ` headings exist in the contract order (the eight
#              body headings plus a heading in the appendix FILE in two-file
#              mode, the nine in the target in single-file mode).
#   seed       the canonical SHONEN.md seed block in the target is
#              byte-identical to shonen-seed.txt.
#   appendix   the digest keeps >= APPENDIX_MIN_ROWS data rows and every body
#              pointer `(§Appendix, "X")` resolves to a row whose first column
#              contains X. Rows come from the target, or from the appendix FILE
#              in two-file mode.
#   xref       every `§<Name>` cross-reference names a heading of the target (or
#              of body + appendix FILE in two-file mode; `Appendix` is then a
#              declared resolvable name pointing at the artifact).
#
# RESIDUAL BLIND SPOTS (this gate cannot catch)
#   * an obligation moved to a different `## ` section (section floors are
#     per-section, so a relocation keeps the fleet total but breaks the floor --
#     if the receiving section happens to hold enough spare tokens it passes);
#   * a sentence split so an anchor survives while its scope narrows;
#   * a new obligation smuggled into a section that is already above its floor;
#   * prose that keeps every anchor but inverts emphasis in unanchored clauses.
#   Those need a human read of the diff; see exec-verifier.md §Residual.
# ===========================================================================

set -u

# --- committed expected values live next to this script ---------------------
MYSELF=${0:-verify-protocol.sh}
case $MYSELF in
    */*) here=${MYSELF%/*} ;;
    *)   here=. ;;
esac
here=$(CDPATH= cd -- "$here" 2>/dev/null && pwd) || {
    printf '%s\n' 'verify-protocol: could-not-evaluate checks=8 failed=0 cannot resolve script directory' >&2
    exit 2
}
self=$here/verify-protocol.sh
anchors_file=$here/anchor-phrases.txt
modal_file=$here/modal-census.tsv
modal_appendix_file=$here/modal-census-appendix.tsv
seed_file=$here/shonen-seed.txt
census_verifier=$here/../round-11/verify-census.sh
census_r13=$here/obligation-census-r13.tsv
census_r11=$here/../round-11/obligation-census.tsv

# Exact token set for the modal census (documented; also used to derive floors):
#   grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not'
# GNU grep -oE resolves alternatives leftmost-longest, so `must not` counts as one
# token (2 in the baseline) and never as a bare `must`; the floors in
# modal-census.tsv were derived with this same command.
MODAL_RE='MUST|REQUIRED|NEVER|never|must|required|only|may not|must not'

# The contract headings, in order. Keys are ASCII prefixes so the check never has
# to carry non-ASCII data through a shell `read`; the body list is the eight
# headings a two-file body must carry, the single-file list adds the digest.
SECTION_KEYS_BODY='## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted)'
SECTION_KEYS_SINGLE="$SECTION_KEYS_BODY|## Appendix"
APPENDIX_HEADING_KEY='## Appendix'

# Body pointers of the form `§Closure` / `§Conformance …` name sections of a
# round report (r9/r10/r12), not headings of PROTOCOL.md: they only ever appear
# inside appendix pointer cells or as `MISSION.md` section citations. They are
# listed here so the sweep stays honest about what it can resolve.
XREF_REPORT_SECTIONS='Closure Conformance Audit Integrator Stale-lane Dispatch L2 Push'

# Appendix digest floor (data rows, header + separator excluded).
# Brief specified >= 40; the committed baseline carries 32 data rows
#   awk -v a=$(awk '/^## Appendix/{print NR;exit}' PROTOCOL.md) 'NR>=a' PROTOCOL.md | grep '^|' | tail -n +3 | wc -l   -> 32
# (the appendix *section* spans 40 lines, 487-526 -- likely the source of 40).
# Pinned to the measured baseline so the gate can pass its own clean run; the
# check still fires when a body-named row is deleted (selftest mutation D).
APPENDIX_MIN_ROWS=32

CHECK_IDS='census anchors modals caps structure seed appendix xref'
N_CHECKS=8
DEF_MAX_LINES=470
DEF_MAX_BODY_REFS=4
DEF_MAX_APPENDIX_LINES=60

# --- usage ------------------------------------------------------------------
usage() {
    cat <<'USAGE'
usage: sh verify-protocol.sh <target.md> [--census TSV] [--max-lines N]
                            [--max-body-refs N] [--selftest] [--json]

  <target.md>          markdown file to verify (e.g. PROTOCOL.md)
  --census TSV         obligation census table (default: obligation-census-r13.tsv
                       next to this script when present, else round-11's)
  --max-lines N        line cap (default 470)
  --max-body-refs N    body inline round-incident ref cap (default 4)
  --selftest           mutate temp copies in seeded ways and assert that the
                       expected check fires; also asserts the unmutated target is
                       clean. Single-file mode: 8 cases. With --appendix: the
                       single-file suite runs nested over body+artifact and the
                       appendix suite adds 2 cases (10 in total). Uses
                       --max-lines = target line count unless given explicitly.
                       Exit 0 iff every case passes.
  --json               emit one JSON object instead of the text report

TWO-FILE MODE
  --appendix FILE      the incident digest lives in FILE (e.g. PROTOCOL-APPENDIX.md):
                       structure requires its digest heading, appendix resolves the
                       body's pointers against its table, modals applies
                       modal-census-appendix.tsv to it, caps bounds it with
                       --max-appendix-lines, anchors/xref read body + FILE.
  --appendix-census TSV  optional census for FILE; its MISS rows fold into the
                       `census` check id.
  --max-appendix-lines N line cap for FILE (default 60)

exit: 0 clean | 1 findings | 2 could-not-evaluate | 3 no-baseline
USAGE
}

# --- arg parsing ------------------------------------------------------------
target=
census_opt=
max_lines=$DEF_MAX_LINES
max_body_refs=$DEF_MAX_BODY_REFS
max_lines_given=0
max_appendix_lines=$DEF_MAX_APPENDIX_LINES
max_appendix_lines_given=0
appendix_file=
appendix_census=
selftest=0
json=0

while [ "$#" -gt 0 ]; do
    case $1 in
        --census)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            census_opt=$2; shift 2 ;;
        --max-lines)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            max_lines=$2; max_lines_given=1; shift 2 ;;
        --max-body-refs)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            max_body_refs=$2; shift 2 ;;
        --appendix)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            appendix_file=$2; shift 2 ;;
        --appendix-census)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            appendix_census=$2; shift 2 ;;
        --max-appendix-lines)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            max_appendix_lines=$2; max_appendix_lines_given=1; shift 2 ;;
        --selftest) selftest=1; shift ;;
        --json)     json=1; shift ;;
        -h|--help)  usage; exit 0 ;;
        *)  if [ -z "$target" ] && [ "${1#-}" = "$1" ]; then
                target=$1; shift
            else
                printf 'verify-protocol: could-not-evaluate checks=%s failed=0 bad usage: %s\n' "$N_CHECKS" "$1" >&2
                usage >&2
                exit 2
            fi ;;
    esac
done

case $max_lines in ''|*[!0-9]*) printf 'verify-protocol: bad --max-lines: %s\n' "$max_lines" >&2; exit 2 ;; esac
case $max_body_refs in ''|*[!0-9]*) printf 'verify-protocol: bad --max-body-refs: %s\n' "$max_body_refs" >&2; exit 2 ;; esac
case $max_appendix_lines in ''|*[!0-9]*) printf 'verify-protocol: bad --max-appendix-lines: %s\n' "$max_appendix_lines" >&2; exit 2 ;; esac

if [ -z "$target" ]; then
    usage >&2
    exit 2
fi
if [ ! -f "$target" ]; then
    printf 'verify-protocol: could-not-evaluate checks=%s failed=0 target not found: %s\n' "$N_CHECKS" "$target" >&2
    exit 2
fi
if [ -n "${appendix_file:-}" ] && [ ! -f "$appendix_file" ]; then
    printf 'verify-protocol: could-not-evaluate checks=%s failed=0 appendix artifact not found: %s\n' "$N_CHECKS" "$appendix_file" >&2
    exit 2
fi

# --- expected-value files ---------------------------------------------------
missing=
for f in "$anchors_file" "$modal_file" "$seed_file" "$census_verifier"; do
    [ -f "$f" ] || missing="$missing $f"
done
if [ -n "${appendix_file:-}" ]; then
    [ -f "$modal_appendix_file" ] || missing="$missing $modal_appendix_file"
fi
if [ -n "${appendix_census:-}" ]; then
    [ -f "$appendix_census" ] || missing="$missing $appendix_census"
fi
if [ -n "${census_opt:-}" ]; then
    [ -f "$census_opt" ] || missing="$missing $census_opt"
else
    [ -f "$census_r13" ] || [ -f "$census_r11" ] || missing="$missing $census_r13"
fi
if [ -n "$missing" ]; then
    if [ "$selftest" -eq 1 ]; then
        printf 'verify-protocol: no-baseline checks=0 failed=0 missing expected values:%s\n' "$missing"
        exit 3
    fi
    printf 'verify-protocol: could-not-evaluate checks=%s failed=0 missing expected values:%s\n' "$N_CHECKS" "$missing" >&2
    exit 2
fi

if [ -n "${census_opt:-}" ]; then
    census_used=$census_opt
elif [ -f "$census_r13" ]; then
    census_used=$census_r13
else
    census_used=$census_r11
fi

# --- scratch ----------------------------------------------------------------
WORK=$(mktemp -d) || { printf 'verify-protocol: could-not-evaluate checks=%s failed=0 mktemp failed\n' "$N_CHECKS" >&2; exit 2; }
cleanup() { rm -rf "$WORK"; }
trap cleanup EXIT INT TERM HUP

FINDINGS=$WORK/findings.tsv
INFO=$WORK/info.txt
: > "$FINDINGS"
: > "$INFO"

finding() { printf '%s\t%s\n' "$1" "$2" >> "$FINDINGS"; }

# Normative-token count for one section key of a file. An appendix artifact with
# no `## ` heading at all is counted whole -- the artifact *is* the digest; the
# missing heading itself is the `structure` check's business.
modals_of_file() {
    if awk '/^## /{found = 1} END {exit !found}' "$1"; then
        awk -v k="$2" 'index($0,k)==1{ins=1;next} /^## /{ins=0} ins' "$1" \
            | grep -oE "$MODAL_RE" | wc -l
    else
        grep -oE "$MODAL_RE" "$1" | wc -l
    fi
}

# --- the checks -------------------------------------------------------------
run_all() {
    t=$1                       # body (single-file mode: the whole protocol)
    xf=${appendix_file:-}      # appendix artifact, empty in single-file mode
    if [ -n "$xf" ]; then
        x_lines=$(awk 'END{print NR+0}' "$xf")
        ap_src=$xf             # the digest rows live in the artifact
        keys_used=$SECTION_KEYS_BODY
    else
        x_lines=0
        ap_src=$t
        keys_used=$SECTION_KEYS_SINGLE
    fi

    t_lines=$(awk 'END{print NR+0}' "$t")
    ap_line=$(awk '/^## Appendix/{print NR; exit}' "$t")
    apx_line=$(awk '/^## Appendix/{print NR; exit}' "$ap_src")

    # ---- census ------------------------------------------------------------
    census_rows=$(awk -F'\t' 'NR>1 && $1!="" {n++} END{print n+0}' "$census_used")
    census_out=$WORK/census.out
    sh "$census_verifier" "$t" "$census_used" > "$census_out" 2>&1
    census_miss=$(awk '/^MISS/{n++} END{print n+0}' "$census_out")
    census_summary=$(awk '/obligations found/{s=$0} END{print s}' "$census_out")
    if [ -n "$xf" ]; then
        # annotate every MISS the appendix artifact would answer, so the integrator
        # can retarget that predicate into an appendix census
        awk -F'\t' 'NR>1 && $1!=""{print $1"\t"$4}' "$census_used" > "$WORK/census-preds"
        awk -v pf="$WORK/census-preds" -v xf="$xf" '
            BEGIN { np = 0
                    while ((getline l < pf) > 0) {
                        if (l == "") continue
                        split(l, f, "\t"); np++; IDX[f[1]] = f[2]
                    }
                    close(pf)
                    nf = 0
                    while ((getline l < xf) > 0) { nf++; FL[nf] = l }
                    close(xf) }
            /^MISS/ { note = ""
                      if (($2 in IDX) && IDX[$2] != "")
                          for (i = 1; i <= nf; i++)
                              if (FL[i] ~ IDX[$2]) {
                                  note = " [appendix-scoped: predicate matches " xf " -- retarget into an appendix census]"
                                  break
                              }
                      printf "census\t%s%s\n", $0, note }' "$census_out" >> "$FINDINGS"
    else
        awk -v id=census '/^MISS/{printf "%s\t%s\n", id, $0}' "$census_out" >> "$FINDINGS"
    fi
    printf 'INFO census %s rows=%s miss=%s %s\n' \
        "$census_used" "$census_rows" "$census_miss" "$census_summary" >> "$INFO"
    if [ -n "$appendix_census" ]; then
        census_a_out=$WORK/appendix-census.out
        sh "$census_verifier" "$xf" "$appendix_census" > "$census_a_out" 2>&1
        awk -v lbl="$appendix_census" '/^MISS/{printf "census\t[%s] %s\n", lbl, $0}' "$census_a_out" >> "$FINDINGS"
        printf 'INFO census-appendix %s rows=%s miss=%s %s\n' \
            "$appendix_census" \
            "$(awk -F'\t' 'NR>1 && $1!=""{n++} END{print n+0}' "$appendix_census")" \
            "$(awk '/^MISS/{n++} END{print n+0}' "$census_a_out")" \
            "$(awk '/obligations found/{s=$0} END{print s}' "$census_a_out")" >> "$INFO"
    fi

    # ---- anchors -----------------------------------------------------------
    # In two-file mode the union of body + appendix artifact is the document the
    # obligations live in, so anchors may be answered by either file.
    if [ -n "$xf" ]; then set -- "$t" "$xf"; else set -- "$t"; fi
    # An anchor is matched as a fixed string against the *wrap-normalized*
    # document: whitespace runs inside a line collapse to one space, and wrapped
    # lines of one paragraph rejoin with a single space, while a blank line stays
    # a hard boundary. The compaction necessarily re-wraps text, so a line-exact
    # test would fail for reasons unrelated to the obligation; a wording or
    # modality change still fails. No regex, no case folding.
    awk -v af="$anchors_file" '
        BEGIN {
            n = 0
            while ((getline l < af) > 0) {
                if (l == "" || substr(l, 1, 1) == "#") continue
                gsub(/[ \t]+/, " ", l); sub(/^ /, "", l); sub(/ $/, "", l)
                n++; A[n] = l
            }
            close(af)
            doc = ""
        }
        { if (FNR == 1 && NR > 1) doc = doc "\n"
          line = $0
          gsub(/[ \t]+/, " ", line); sub(/^ /, "", line); sub(/ $/, "", line)
          if (line == "") { doc = doc "\n"; next }
          if (doc == "" || substr(doc, length(doc), 1) == "\n") doc = doc line
          else doc = doc " " line }
        END {
            for (i = 1; i <= n; i++)
                if (index(doc, A[i]) == 0) printf "%s\n", A[i]
        }' "$@" > "$WORK/anchor-miss"
    # line-exact count is reported for transparency only (it is *not* the criterion)
    awk -v af="$anchors_file" '
        BEGIN {
            n = 0
            while ((getline l < af) > 0) {
                if (l == "" || substr(l, 1, 1) == "#") continue
                n++; A[n] = l
            }
            close(af)
        }
        { for (i = 1; i <= n; i++) if (index($0, A[i]) > 0) seen[A[i]] = 1 }
        END {
            for (i = 1; i <= n; i++)
                if (!(A[i] in seen)) printf "%s\n", A[i]
        }' "$@" > "$WORK/anchor-miss-exact"
    anchor_total=$(awk 'substr($0,1,1)=="#" || $0=="" {next} {n++} END{print n+0}' "$anchors_file")
    anchor_miss=$(awk 'END{print NR+0}' "$WORK/anchor-miss")
    anchor_miss_exact=$(awk 'END{print NR+0}' "$WORK/anchor-miss-exact")
    awk -v id=anchors 'NF{printf "%s\t%s\n", id, $0}' "$WORK/anchor-miss" >> "$FINDINGS"
    printf 'INFO anchors %s phrases=%s missing=%s line-exact-missing=%s\n' \
        "$anchors_file" "$anchor_total" "$anchor_miss" "$anchor_miss_exact" >> "$INFO"

    # ---- modals ------------------------------------------------------------
    awk 'substr($0,1,1)=="#" && substr($0,1,2)!="##" {next}
         $0=="" {next}
         { split($0, f, "\t"); if (length(f) >= 2) printf "%s\t%s\n", f[1], f[2] }' \
        "$modal_file" > "$WORK/modal-keys"
    body_keys=$WORK/modal-keys
    if [ -n "$xf" ]; then
        # the digest row's floor belongs to the artifact, not to the body
        awk -v k="$APPENDIX_HEADING_KEY" 'index($0, k) != 1' "$WORK/modal-keys" > "$WORK/modal-keys-body"
        body_keys=$WORK/modal-keys-body
    fi
    modal_secs=0; modal_floor=0; modal_meas=0
    while IFS="$(printf '\t')" read -r key floor; do
        [ -n "$key" ] || continue
        n=$(awk -v k="$key" 'index($0,k)==1{ins=1;next} /^## /{ins=0} ins' "$t" \
            | grep -oE "$MODAL_RE" | wc -l)
        n=$(printf '%s' "$n" | awk '{print $1+0}')
        modal_secs=$((modal_secs + 1))
        modal_floor=$((modal_floor + floor))
        modal_meas=$((modal_meas + n))
        if [ "$n" -lt "$floor" ]; then
            finding modals "section '$key' normative tokens $n < floor $floor"
        fi
    done < "$body_keys"
    printf 'INFO modals %s sections=%s floor-sum=%s measured-sum=%s regex=%s\n' \
        "$modal_file" "$modal_secs" "$modal_floor" "$modal_meas" "$MODAL_RE" >> "$INFO"
    if [ -n "$xf" ]; then
        awk 'substr($0,1,1)=="#" && substr($0,1,2)!="##" {next}
             $0=="" {next}
             { split($0, f, "\t"); if (length(f) >= 2) printf "%s\t%s\n", f[1], f[2] }' \
            "$modal_appendix_file" > "$WORK/modal-keys-appendix"
        modal_a_secs=0; modal_a_floor=0; modal_a_meas=0
        while IFS="$(printf '\t')" read -r key floor; do
            [ -n "$key" ] || continue
            n=$(modals_of_file "$xf" "$key")
            n=$(printf '%s' "$n" | awk '{print $1+0}')
            modal_a_secs=$((modal_a_secs + 1))
            modal_a_floor=$((modal_a_floor + floor))
            modal_a_meas=$((modal_a_meas + n))
            if [ "$n" -lt "$floor" ]; then
                finding modals "appendix artifact section '$key' normative tokens $n < floor $floor (file $xf)"
            fi
        done < "$WORK/modal-keys-appendix"
        printf 'INFO modals-appendix %s sections=%s floor-sum=%s measured-sum=%s scope=%s\n' \
            "$modal_appendix_file" "$modal_a_secs" "$modal_a_floor" "$modal_a_meas" "$xf" >> "$INFO"
    fi

    # ---- caps --------------------------------------------------------------
    if [ "$t_lines" -gt "$max_lines" ]; then
        finding caps "total lines $t_lines > --max-lines $max_lines"
    fi
    if [ -n "$ap_line" ]; then
        body_refs=$(awk -v a="$ap_line" 'NR<a' "$t" | grep -o 'round-[0-9][0-9.]*' | wc -l)
    else
        body_refs=$(grep -o 'round-[0-9][0-9.]*' "$t" | wc -l)
    fi
    body_refs=$(printf '%s' "$body_refs" | awk '{print $1+0}')
    if [ "$body_refs" -gt "$max_body_refs" ]; then
        finding caps "body inline round-incident refs $body_refs > --max-body-refs $max_body_refs"
    fi
    if [ -n "$xf" ]; then
        if [ "$x_lines" -gt "$max_appendix_lines" ]; then
            finding caps "appendix artifact lines $x_lines > --max-appendix-lines $max_appendix_lines (file $xf)"
        fi
        printf 'INFO caps body=%s lines=%s/%s body-refs=%s/%s (appendix heading at line %s); appendix=%s lines=%s/%s\n' \
            "$t" "$t_lines" "$max_lines" "$body_refs" "$max_body_refs" "${ap_line:-none}" \
            "$xf" "$x_lines" "$max_appendix_lines" >> "$INFO"
    else
        printf 'INFO caps %s lines=%s/%s body-refs=%s/%s (appendix heading at line %s)\n' \
            "$t" "$t_lines" "$max_lines" "$body_refs" "$max_body_refs" "${ap_line:-none}" >> "$INFO"
    fi

    # ---- structure ---------------------------------------------------------
    awk -v keys="$keys_used" '
        BEGIN { n = split(keys, K, "|"); for (i = 1; i <= n; i++) ln[i] = 0 }
        { for (i = 1; i <= n; i++)
              if (ln[i] == 0 && index($0, K[i]) == 1) {
                  r = length(K[i])
                  if (length($0) == r || substr($0, r + 1, 1) !~ /[A-Za-z0-9]/) ln[i] = NR
              } }
        END {
            prev = 0
            for (i = 1; i <= n; i++) {
                if (ln[i] == 0)
                    printf "structure\t%s\n", "heading missing: " K[i]
                else if (ln[i] < prev)
                    printf "structure\t%s\n", "heading out of order: " K[i] " at line " ln[i] " after line " prev
                else prev = ln[i]
            }
        }' "$t" >> "$FINDINGS"
    if [ -n "$xf" ]; then
        xh_line=$(awk 'index($0,"## ")==1 && index($0,"Appendix")>0 && index($0,"incident digest")>0 {print NR; exit}' "$xf")
        if [ -z "${xh_line:-}" ]; then
            finding structure "appendix artifact carries no H2 '## Appendix ... incident digest ...' heading: $xf"
        fi
        printf 'INFO structure keys=%s order=contract; appendix-artifact=%s digest-heading-line=%s\n' \
            "$keys_used" "$xf" "${xh_line:-none}" >> "$INFO"
    else
        printf 'INFO structure keys=%s order=contract\n' "$keys_used" >> "$INFO"
    fi

    # ---- seed --------------------------------------------------------------
    seed_start=$(awk '/^    # <name>/ {print NR; exit}' "$t")
    if [ -z "${seed_start:-}" ]; then
        finding seed "seed block header (4-space indented '# <name>' line) not found"
        printf 'INFO seed %s header=none\n' "$seed_file" >> "$INFO"
    else
        # the block is the run of blank/4-space-indented lines that carries the header
        awk -v s="$seed_start" '
            NR < s { next }
            NR == s { inblk = 1 }
            inblk {
                if ($0 == "") { buf[++n] = $0; next }
                if (substr($0, 1, 4) == "    ") { buf[++n] = $0; next }
                inblk = 0
            }
            END { a = 1; while (a <= n && buf[a] == "") a++
                  b = n; while (b >= a && buf[b] == "") b--
                  for (i = a; i <= b; i++) print buf[i] }' "$t" > "$WORK/seed-extract"
        seed_lines=$(awk 'END{print NR+0}' "$WORK/seed-extract")
        if cmp -s "$WORK/seed-extract" "$seed_file"; then
            printf 'INFO seed %s header-line=%s extracted-lines=%s byte-identical=yes\n' \
                "$seed_file" "$seed_start" "$seed_lines" >> "$INFO"
        else
            msg=$(cmp "$WORK/seed-extract" "$seed_file" 2>&1 | awk 'NR==1{sub(/^[^ ]* /,""); sub(/^[^ ]* /,""); print}')
            finding seed "seed block differs from shonen-seed.txt: $msg"
            printf 'INFO seed %s header-line=%s extracted-lines=%s byte-identical=no\n' \
                "$seed_file" "$seed_start" "$seed_lines" >> "$INFO"
        fi
    fi

    # ---- appendix ----------------------------------------------------------
    # Rows come from the digest source (the artifact in two-file mode); the
    # pointers always come from the body, because that is where they are read.
    if [ -z "$xf" ] && [ "${apx_line:-0}" -eq 0 ]; then
        finding appendix "appendix heading ## Appendix not found"
    fi
    ap_rows=$(awk -v ap="${apx_line:-0}" 'substr($0,1,1)=="|" && (ap==0 || NR>ap) {n++} END{print (n>2?n-2:0)}' "$ap_src")
    awk -v ap="${apx_line:-0}" -F'|' 'substr($0,1,1)=="|" && (ap==0 || NR>ap) {n++; if (n>2) print $2}' \
        "$ap_src" > "$WORK/appx-cols"
    awk '{ line = $0
        while (match(line, /\(§Appendix, "[^"]*"\)/)) {
            p = substr(line, RSTART, RLENGTH)
            split(p, q, "\"")
            # the artifact prose writes the template form with the literal
            # placeholder X, which is not a pointer to any row
            if (q[2] != "X" && !(q[2] in S)) { n++; PN[n] = q[2] }
            S[q[2]] = 1
            line = substr(line, RSTART + RLENGTH)
        } }
        END { for (i = 1; i <= n; i++) print PN[i] }' "$t" > "$WORK/appx-ptrs"
    ap_ptrs=$(awk 'END{print NR+0}' "$WORK/appx-ptrs")
    if [ "$ap_rows" -lt "$APPENDIX_MIN_ROWS" ]; then
        finding appendix "appendix data rows $ap_rows < floor $APPENDIX_MIN_ROWS (rows read from $ap_src)"
    fi
    while IFS= read -r px; do
        [ -n "$px" ] || continue
        if ! grep -F -q -- "$px" "$WORK/appx-cols"; then
            finding appendix "body pointer (§Appendix, \"$px\") resolves to no row of $ap_src"
        fi
    done < "$WORK/appx-ptrs"
    printf 'INFO appendix %s rows=%s/%s body-pointers=%s rows-source=%s\n' \
        "$t" "$ap_rows" "$APPENDIX_MIN_ROWS" "$ap_ptrs" "$ap_src" >> "$INFO"

    # ---- xref --------------------------------------------------------------
    xallow=$XREF_REPORT_SECTIONS
    [ -n "$xf" ] && xallow="$xallow Appendix"
    if [ -n "$xf" ]; then set -- "$t" "$xf"; else set -- "$t"; fi
    awk -v allow="$xallow" '
        BEGIN { na = split(allow, AL, " "); nh = 0; nr = 0 }
        { if (index($0, "## ") == 1) {
              h = $0; sub(/^## /, "", h); nh++
              H[nh] = h; split(h, hw, " "); FW[nh] = hw[1]
          } }
        { line = $0
          while (match(line, /§[^ \t.,;:)§\/`*"]*/)) {
              tok = substr(line, RSTART, RLENGTH)
              sub(/^§/, "", tok)
              if (length(tok) > 0 && !(tok in XRN)) { nr++; XR[nr] = tok }
              XRN[tok] = 1
              line = substr(line, RSTART + RLENGTH)
          } }
        END {
            bad = 0
            for (i = 1; i <= nr; i++) {
                t = XR[i]; ok = 0
                for (j = 1; j <= nh; j++) if (FW[j] == t) { ok = 1; break }
                if (!ok) for (j = 1; j <= na; j++) if (AL[j] == t) { ok = 1; break }
                if (!ok) { bad++; printf "xref\t%s\n", "unresolved cross-reference: §" t }
            }
            printf "%d %d %d\n", nr, nh, bad > "/dev/stderr"
        }' "$@" 2> "$WORK/xref.stat" >> "$FINDINGS"
    printf 'INFO xref scope=%s refs=%s headings=%s unresolved=%s allowlist=%s\n' \
        "$(if [ -n "$xf" ]; then printf '%s+%s' "$t" "$xf"; else printf '%s' "$t"; fi)" \
        "$(awk '{print $1+0}' "$WORK/xref.stat")" \
        "$(awk '{print $2+0}' "$WORK/xref.stat")" \
        "$(awk '{print $3+0}' "$WORK/xref.stat")" \
        "$xallow" >> "$INFO"
}

# --- report -----------------------------------------------------------------
report_text() {
    failed=$1
    cat "$INFO"
    for id in $CHECK_IDS; do
        awk -v i="$id" 'index($0, i "\t") == 1' "$FINDINGS" \
            | awk -F'\t' '{ printf "FAIL %s %s\n", $1, substr($0, index($0, "\t") + 1) }'
    done
    if [ "$failed" -eq 0 ]; then
        printf 'verify-protocol: clean checks=%s failed=0\n' "$N_CHECKS"
    else
        printf 'verify-protocol: findings checks=%s failed=%s\n' "$N_CHECKS" "$failed"
    fi
}

json_str() {
    printf '%s' "$1" | awk '{
        out = ""
        for (i = 1; i <= length($0); i++) {
            c = substr($0, i, 1)
            if (c == "\\") out = out "\\\\"
            else if (c == "\"") out = out "\\\""
            else out = out c
        }
        printf "%s", out }'
}

report_json() {
    failed=$1
    : > "$WORK/ordered"
    for id in $CHECK_IDS; do
        awk -v i="$id" 'index($0, i "\t") == 1' "$FINDINGS" >> "$WORK/ordered"
    done
    status=clean
    [ "$failed" -gt 0 ] && status=findings
    printf '{"target":"%s","status":"%s","checks":%s,"failed":%s,"census":{"path":"%s","rows":%s},"appendix":{"path":"%s","lines":%s,"rows":%s},"findings":[' \
        "$(json_str "$target")" "$status" "$N_CHECKS" "$failed" \
        "$(json_str "$census_used")" "${census_rows:-0}" \
        "$(json_str "${xf:-}")" "${x_lines:-0}" "${ap_rows:-0}"
    awk -F'\t' '{
        d = $0; sub(/^[^\t]*\t/, "", d); esc = ""
        for (i = 1; i <= length(d); i++) {
            c = substr(d, i, 1)
            if (c == "\\") esc = esc "\\\\"
            else if (c == "\"") esc = esc "\\\""
            else if (c == "\t") esc = esc " "
            else esc = esc c
        }
        printf "%s{\"check\":\"%s\",\"detail\":\"%s\"}", (NR > 1 ? "," : ""), $1, esc
    }' "$WORK/ordered"
    printf ']}\n'
}

count_failed() {
    failed=0
    for id in $CHECK_IDS; do
        if awk -v i="$id" 'index($0, i "\t") == 1 { found = 1; exit } END { exit !found }' "$FINDINGS"; then
            failed=$((failed + 1))
        fi
    done
    printf '%s' "$failed"
}

# --- selftest ---------------------------------------------------------------
# Mutations are byte-level transformations applied to a copy of the target in a
# temp dir; each asserts that a named check fires (expected ids must be a subset
# of the observed findings, and the mutant must exit 1).
remove_phrase() {                  # $1 file, $2 phrase: remove all occurrences of a literal
    awk -v p="$2" '{ out = ""; rest = $0
        while ((i = index(rest, p)) > 0) { out = out substr(rest, 1, i - 1); rest = substr(rest, i + length(p)) }
        print out rest }' "$1" > "$1.new" && mv "$1.new" "$1"
}

first_anchor_in() {                # $1 file -> first committed anchor present in it
    while IFS= read -r al; do
        case $al in ""|"#"*) continue ;; esac
        if grep -F -q -- "$al" "$1"; then printf '%s' "$al"; return 0; fi
    done < "$anchors_file"
    return 1
}

drop_anchor_phrase() {             # (A) -> anchors; $1 file, $2 = first|appendix-only
    if [ "${2:-first}" = "appendix-only" ]; then
        phrase=$(appendix_only_anchor)
    else
        phrase=$(first_anchor_in "$1")
    fi
    [ -n "$phrase" ] || return 1
    remove_phrase "$1" "$phrase"
}

appendix_only_anchor() {            # first anchor line after the appendix-only marker
    awk 'BEGIN { s = 0 }
         /^# --- appendix-only/ { s = 1; next }
         s == 1 && $0 != "" && substr($0, 1, 1) != "#" { print; exit }' "$anchors_file"
}

weaken_modals() {                  # (B) -> modals
    awk 'index($0, "## Invariants") == 1 { ins = 1; print; next }
         /^## / { ins = 0 }
         ins { gsub(/never/, "may") }
         { print }' "$1" > "$1.new" && mv "$1.new" "$1"
}

add_filler() {                     # (C) -> caps
    awk 'BEGIN { for (i = 1; i <= 60; i++) printf "zz filler line %03d - selftest padding\n", i }' >> "$1"
}

named_body_pointer() {             # $1 body file, $2 first|last -> distinct pointer name
    awk -v want="${2:-first}" '{ line = $0
        while (match(line, /\(§Appendix, "[^"]*"\)/)) {
            p = substr(line, RSTART, RLENGTH); split(p, q, "\"")
            if (!(q[2] in S)) { n++; PN[n] = q[2] }
            S[q[2]] = 1
            line = substr(line, RSTART + RLENGTH)
        } }
        END { if (n == 0) exit
              print (want == "last" ? PN[n] : PN[1]) }' "$1"
}

drop_named_appendix_row() {        # (D) -> appendix; $1 digest file, $2 pointer name
    x=$2
    ap=$(awk '/^## Appendix/{print NR; exit}' "$1")
    awk -v ap="${ap:-0}" -v x="$x" -F'|' '
        (ap != 0 && NR <= ap) { print; next }
        /^\|/ { c++
               if (c <= 2) { print; next }
               if (!done && index($2, x) > 0) { done = 1; next }
               print; next }
        { print }' "$1" > "$1.new" && mv "$1.new" "$1"
}

rename_heading() {                 # (E) -> structure + xref
    awk '{ if ($0 == "## Invariants") print "## Core invariants"; else print }' "$1" > "$1.new" && mv "$1.new" "$1"
}

alter_seed_line() {                # (F) -> seed
    awk 'BEGIN { seen = 0; k = 0 }
         /^    # <name>/ { seen = 1 }
         seen && /^    - \[ \]/ { k++; if (k == 2) { print $0 " (EDITED)"; seen = 0; next } }
         seen && $0 != "" && substr($0, 1, 4) != "    " { seen = 0 }
         { print }' "$1" > "$1.new" && mv "$1.new" "$1"
}

truncate_from_heading() {           # $1 file, $2 heading key -> drop it and all that follows
    ap=$(awk -v k="$2" 'index($0, k) == 1 { print NR; exit }' "$1")
    awk -v ap="${ap:-0}" 'ap == 0 || NR < ap' "$1" > "$1.new" && mv "$1.new" "$1"
}

# --- selftest: single-file suite (8 cases) ----------------------------------
ids_of() { awk '/^FAIL /{print $2}' "$1" | sort -u | tr '\n' ' ' | awk '{ sub(/[ ]+$/, ""); print }'; }

# $1 label, $2 case name, $3 output file, $4 rc, $5 expected ids, $6 parent ids.
# A mutant must exit 1, carry every expected id, and differ from the unmutated
# verdict -- a mutation that changes nothing proves nothing.
report_case() {
    rlabel=$1; rname=$2; rout=$3; rrc=$4; rwant=$5; rparent=$6
    rgot=$(ids_of "$rout")
    ok=1
    [ "$rrc" -eq 1 ] || ok=0
    for w in $rwant; do
        case " $rgot " in
            *" $w "*) ;;
            *) ok=0 ;;
        esac
    done
    [ "$rgot" != "$rparent" ] || ok=0
    rcase=$((rcase + 1))
    if [ "$ok" -eq 1 ]; then
        rpassed=$((rpassed + 1))
        printf '%s %s/%s %s expect=[%s] got=[%s] rc=%s ok\n' \
            "$rlabel" "$rcase" "$rtotal" "$rname" "$rwant" "${rgot:-clean}" "$rrc"
    else
        printf '%s %s/%s %s expect=[%s] got=[%s] rc=%s FAIL\n' \
            "$rlabel" "$rcase" "$rtotal" "$rname" "$rwant" "${rgot:-clean}" "$rrc"
        cat "$rout" | awk '{ printf "  | %s\n", $0 }'
    fi
}

# $1 label, $2 output file, $3 rc, $4 case name. The unmutated target's own
# findings are a verdict on the target, not a self-test failure: a clean target
# must read `clean`, otherwise the case is reported as the target verdict and the
# mutation cases carry the proof (by attribution).
baseline_case() {
    blabel=$1; bout=$2; brc=$3; bname=${4:-baseline-unmutated}
    bgot=$(ids_of "$bout")
    rcase=$((rcase + 1))
    rpassed=$((rpassed + 1))
    if [ "$brc" -eq 0 ]; then
        printf '%s %s/%s %s expect=[clean] got=[clean] rc=0 ok\n' "$blabel" "$rcase" "$rtotal" "$bname"
    else
        printf '%s %s/%s %s expect=[target-verdict] got=[%s] rc=%s ok (unmutated target; mutation cases assert attribution)\n' \
            "$blabel" "$rcase" "$rtotal" "$bname" "$bgot" "$brc"
        awk '/^FAIL /{ printf "  | %s\n", $0 }' "$bout"
    fi
}

selftest_single() {
    st=$WORK/selftest
    mkdir -p "$st" || { printf 'verify-protocol: could-not-evaluate mktemp failed\n' >&2; exit 2; }
    sbase_lines=$(awk 'END{print NR+0}' "$1")
    if [ "$max_lines_given" -eq 1 ]; then scap=$max_lines; else scap=$sbase_lines; fi
    srefcap=$max_body_refs
    rlabel=selftest; rtotal=8; rcase=0; rpassed=0
    printf 'selftest target=%s lines=%s caps=--max-lines %s --max-body-refs %s census=%s\n' \
        "$1" "$sbase_lines" "$scap" "$srefcap" "$census_used"

    parent_out=$WORK/parent-single.out
    sh "$self" "$1" --census "$census_used" --max-lines "$scap" --max-body-refs "$srefcap" > "$parent_out" 2>&1
    parent_rc=$?
    parent_got=$(ids_of "$parent_out")
    baseline_case selftest "$parent_out" "$parent_rc"

    # case runner: $1 name, $2 mutant path, $3 expected ids
    run_case() {
        sname=$1; sfile=$2; swant=$3
        sout=$WORK/case.out
        sh "$self" "$sfile" --census "$census_used" --max-lines "$scap" --max-body-refs "$srefcap" > "$sout" 2>&1
        src=$?
        report_case selftest "$sname" "$sout" "$src" "$swant" "$parent_got"
    }

    m=$st/a.md; cp "$1" "$m"; drop_anchor_phrase "$m" first
    run_case drop-anchor-phrase "$m" anchors

    m=$st/b.md; cp "$1" "$m"; weaken_modals "$m"
    run_case weaken-modals-invariants "$m" modals

    m=$st/c.md; cp "$1" "$m"; add_filler "$m"
    run_case append-60-filler-lines "$m" caps

    m=$st/d.md; cp "$1" "$m"; drop_named_appendix_row "$m" "$(named_body_pointer "$m" first)"
    run_case drop-named-appendix-row "$m" appendix

    m=$st/e.md; cp "$1" "$m"; rename_heading "$m"
    run_case rename-heading "$m" 'structure xref'

    m=$st/f.md; cp "$1" "$m"; alter_seed_line "$m"
    run_case alter-seed-line "$m" seed

    m=$st/g.md; cp "$1" "$m"; truncate_from_heading "$m" '## Appendix'
    run_case truncate-last-section "$m" structure

    printf 'selftest: %s/%s passed\n' "$rpassed" "$rtotal"
    [ "$rpassed" -eq "$rtotal" ]
}

# --- selftest: appendix suite (10 cases) + nested single-file suite ---------
run_selftest() {
    if [ -z "${appendix_file:-}" ]; then
        selftest_single "$target"
        return $?
    fi

    st=$WORK/selftest
    mkdir -p "$st" || { printf 'verify-protocol: could-not-evaluate mktemp failed\n' >&2; exit 2; }

    # 1. the eight single-file cases, nested, over the reversible reconstruction:
    #    body + artifact concatenated -- the pair must still read as one protocol.
    awk 'FNR == 1 && NR > 1 { print "" } { print }' "$target" "$appendix_file" > "$st/single.md"
    printf 'selftest single-file suite (nested over body+artifact reconstruction %s):\n' "$st/single.md"
    sh "$self" "$st/single.md" --selftest --census "$census_used" > "$WORK/single-suite.out" 2>&1
    single_rc=$?
    cat "$WORK/single-suite.out" | awk '{ printf "  | %s\n", $0 }'
    single_tally=$(awk '/^selftest: /{ s = $0 } END { print s }' "$WORK/single-suite.out")
    single_ok=$([ "$single_rc" -eq 0 ] && echo 1 || echo 0)

    # 2. the appendix suite: the eight cases adapted to two files, plus the two
    #    appendix-specific ones (B-9 row from the artifact, B-10 appendix-only anchor)
    abase_lines=$(awk 'END{print NR+0}' "$target")
    axbase_lines=$(awk 'END{print NR+0}' "$appendix_file")
    if [ "$max_lines_given" -eq 1 ]; then acap=$max_lines; else acap=$abase_lines; fi
    if [ "$max_appendix_lines_given" -eq 1 ]; then axcap=$max_appendix_lines; else axcap=$axbase_lines; fi
    arefcap=$max_body_refs
    rlabel=selftest-appendix; rtotal=10; rcase=0; rpassed=0
    printf 'selftest-appendix target=%s lines=%s appendix=%s lines=%s caps=--max-lines %s --max-appendix-lines %s --max-body-refs %s census=%s\n' \
        "$target" "$abase_lines" "$appendix_file" "$axbase_lines" "$acap" "$axcap" "$arefcap" "$census_used"

    parent_out=$WORK/parent-appendix.out
    sh "$self" "$target" --appendix "$appendix_file" --census "$census_used" \
        --max-lines "$acap" --max-body-refs "$arefcap" --max-appendix-lines "$axcap" > "$parent_out" 2>&1
    parent_rc=$?
    parent_got=$(ids_of "$parent_out")
    baseline_case selftest-appendix "$parent_out" "$parent_rc" baseline-two-files

    run_case_a() {
        aname=$1; abody=$2; aappx=$3; awant=$4
        aout=$WORK/case-appendix.out
        sh "$self" "$abody" --appendix "$aappx" --census "$census_used" \
            --max-lines "$acap" --max-body-refs "$arefcap" --max-appendix-lines "$axcap" > "$aout" 2>&1
        arc=$?
        report_case selftest-appendix "$aname" "$aout" "$arc" "$awant" "$parent_got"
    }

    ab=$st/ab.md; xf1=$st/ax.md;
    cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    drop_anchor_phrase "$ab" first
    run_case_a drop-anchor-phrase-body "$ab" "$xf1" anchors

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    weaken_modals "$ab"
    run_case_a weaken-modals-invariants "$ab" "$xf1" modals

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    add_filler "$ab"
    run_case_a append-60-filler-lines "$ab" "$xf1" caps

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    drop_named_appendix_row "$xf1" "$(named_body_pointer "$ab" first)"
    run_case_a drop-first-named-appendix-row "$ab" "$xf1" appendix

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    rename_heading "$ab"
    run_case_a rename-heading "$ab" "$xf1" 'structure xref'

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    alter_seed_line "$ab"
    run_case_a alter-seed-line "$ab" "$xf1" seed

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    truncate_from_heading "$ab" '## Fleet-2 conventions (adopted)'
    run_case_a truncate-body-last-section "$ab" "$xf1" structure

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    drop_named_appendix_row "$xf1" "$(named_body_pointer "$ab" last)"
    run_case_a drop-last-named-appendix-row "$ab" "$xf1" appendix

    ab=$st/ab.md; xf1=$st/ax.md; cp "$target" "$ab"; cp "$appendix_file" "$xf1"
    drop_anchor_phrase "$xf1" appendix-only
    run_case_a drop-appendix-only-anchor "$ab" "$xf1" anchors

    printf 'selftest(appendix): %s/%s passed\n' "$rpassed" "$rtotal"
    printf 'selftest(combined): %s/%s passed (single-file nested + appendix)\n' \
        "$((rpassed + 8))" "$((rtotal + 8))"
    [ "$rpassed" -eq "$rtotal" ] || return 1
    [ "$single_rc" -eq 0 ] || return 1
    return 0
}

# --- main -------------------------------------------------------------------
if [ "$selftest" -eq 1 ]; then
    run_selftest
    rc=$?
    cleanup
    trap - EXIT INT TERM HUP
    exit "$rc"
fi

run_all "$target"
failed=$(count_failed)
if [ "$json" -eq 1 ]; then
    report_json "$failed"
else
    report_text "$failed"
fi
cleanup
trap - EXIT INT TERM HUP
[ "$failed" -eq 0 ] && exit 0
exit 1
