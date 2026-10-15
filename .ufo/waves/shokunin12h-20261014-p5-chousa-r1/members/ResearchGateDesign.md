# ResearchGateDesign — `tools/research-gate.sh`

**Member:** ResearchGateDesign (executor) · **Wave:** shokunin12h-20261014-p5-chousa-r1  
**Lane:** chousa-shokunin (shonen probation r1) · **Role:** design only — parent lands the file  
**Axes:** coverage · depth · calibration  
**Measured:** 2026-10-15T00:55:14Z (UTC) · local read-only; no external fetches  
**Lane HEAD (seed):** `02a615a93a3cfa7583bc165700522709cd47089e` · fleet short: `a9f4d25`  
**Peer ack:** GateFixtureDesign — path arg / `CHOUSA_RECORD`; `FINDING <ID>`; `RESEARCH_GATE: CLEAN|DRIFT`; `RESEARCH_GATE_SELFTEST: PASS (N cases)`; exits 0/1/2; hermetic mktemp; one PASS + one FAIL per defect class.

Advisory only. Not a judge verdict. Parent cuts script to `chousa-shokunin/tools/research-gate.sh`.

---

## 0. Axes (godspeed)

| Axis | Move kept |
|---|---|
| **coverage** | All five SKILL checklist teeth + hard boundaries + schema/ephemeral/secret classes; survey artifacts named as expected-DRIFT controls |
| **depth** | Line-oriented `@chousa` grammar with resolvable pointers; hop status must be resolved **or** marked unresolved-with-reason; rejections are first-class rows, not silence |
| **calibration** | CLEAN only when every severity-bearing class is quiet; exit 2 never greened; proposal ranks do not count as primary evidence; chat-export “sources” without machine rows are SCHEMA_MISSING, not free passes |

---

## 1. Contract (from SKILL.md + wave)

| Item | Value |
|---|---|
| Path | `chousa-shokunin/tools/research-gate.sh` |
| Modes | default / `verify` · `--selftest` · `--help` |
| Record input | positional `RECORD` **or** env `CHOUSA_RECORD` (exactly one required in verify) |
| Verdict line | `RESEARCH_GATE: CLEAN\|DRIFT (findings=N drift=M …)` |
| Selftest rollup | `RESEARCH_GATE_SELFTEST: PASS (N cases)` / `FAIL (fail/N)` |
| Exit | `0` CLEAN (or selftest pass) · `1` DRIFT (or selftest fail) · `2` setup/usage |
| Write scope | **selftest temp dir only** (`mktemp -d /tmp/research-gate-selftest.XXXXXX`); verify creates **zero** files |
| Remediation | **none** — detect and report only |
| Secrets | shape-only; never prints secret-shaped values (redacts match text) |
| Network | none — no curl/wget; external URL pointers without `@approval` → DRIFT |

### Method teeth (SKILL.md:42-46 + §Gates:50-53)

| # | Contract clause | Finding id(s) when broken |
|---|---|---|
| 1 | Question declared | `QUESTION_MISSING` |
| 2 | Sources ranked | `SOURCE_NONE` · `SOURCE_UNRANKED` · `SOURCE_RANK_INVALID` · `SOURCE_PTR_MISSING` |
| 3 | Chain hops resolved-or-marked | `CHAIN_NONE` · `CHAIN_HOP_OPEN` · `CHAIN_REASON_MISSING` |
| 4 | Claims pointed | `CLAIM_NONE` · `CLAIM_UNPOINTED` · `CLAIM_LAYER_INVALID` · `EPHEMERAL_POINTER` |
| 5 | Rejections kept (with reason) | `REJECTION_NONE` · `REJECTION_WITHOUT_REASON` |
| 6 | Negative claim carries sweep | `NEGATIVE_WITHOUT_SWEEP` |
| 7 | Hard boundaries | `EXTERNAL_UNAPPROVED` · `BOUNDARY_KASEGI` · `BOUNDARY_KENGAKU` · `SECRET_SHAPE` |
| 8 | Schema present | `SCHEMA_MISSING` |

### CLEAN vs DRIFT (calibration)

- **CLEAN** — schema present; question non-empty; ≥1 ranked source with pointer; ≥1 claim with pointer + valid layer; every chain hop `status=resolved` or `status=unresolved` **with** `reason=`; every `@negative` carries `sweep=`; ≥1 `@rejection` row (use `reason=none-recorded` only when the record explicitly states no source was rejected — empty omission is `REJECTION_NONE`); no severity findings.
- **DRIFT** — one or more severity-bearing `FINDING` lines (`severity=warn|crit`).
- **Exit 2** — bad CLI, missing record path, unreadable record, selftest harness cannot build temp root. Never a silent CLEAN.

### Central survey finding (must not be papered over)

The three fleet artifacts under `research/deep-research-2026-09-28/` are **chat-export transcripts** (`research/README.md:6-8`). They contain a natural-language question and prose claims, but:

- **zero** `path:line` machine citations (measured scan 2026-10-15),
- bare domain labels (`コトバンク`, `arxiv.org`, `nihonkiin.or.jp`) without resolvable revision pins,
- no ranked source table, no hop ledger, no kept rejection rows in gate grammar.

Under this gate they are **expected DRIFT** via `SCHEMA_MISSING` (and would cascade into the other classes if forced through a loose prose parser). That is the round's method signal: harvest ≠ research record.

Precedents this gate inherits as **evidence of fleet citation discipline** (not copied logic blindly):

- `kagi-shokunin/corpus/claim-ledger.sh` header exit map and “dead citation must be labelled where cited” (`claim-ledger.sh:31-45`, `:82`)
- `kasegi-shokunin/corpus/instruments/anchorcheck.py` + `corpus/knowledge/citation-bases.md` — bases named, lost anchors prefixed, never silent rewrite (`citation-bases.md:9-67`)

---

## 2. Record grammar — `research-record/v1`

Machine lines may sit anywhere in a Markdown (or plain) research record. Prose is ignored except for boundary/secret shape scans. One directive per line. Fields are `key=value` tokens; `::` begins free text to end-of-line.

```
@chousa schema=research-record/v1
@question <non-empty text>
@source id=S1 rank=primary|secondary|aggregator|unsourced|proposal ptr=<token> [title=...]
@chain  id=H1 from=<claim-or-source-id> to=<token> status=resolved|unresolved [reason=...]
@claim  id=C1 ptr=<token> layer=observation|inference|unknown|proposal status=verified|contradicted|unresolved :: <text>
@negative id=N1 sweep=<token> :: <negative claim text>
@rejection id=R1 reason=<non-empty> :: <rejected source or claim>
@approval id=A1 scope=loopback|external window=<id-or-none> status=granted|denied|n/a [note=...]
```

### Pointer (`ptr=`) classes

| Shape | Gate treatment |
|---|---|
| `S[0-9A-Za-z_-]+` (source id) | OK iff matching `@source` exists |
| `path:line` or `path:line-line` (relative) | OK if file exists under `CHOUSA_ROOT` (default: cwd / lane root) **or** line carries a dead-marker (`scratch|ephemeral|historical|unresolved|lost-tree|lost-base|proposal`) |
| `http://` / `https://` | Requires `@approval` with `scope=external` and `status=granted`; else `EXTERNAL_UNAPPROVED` |
| `local://` `artifact://` `agent://` `proc://` | `EPHEMERAL_POINTER` unless same-line dead-marker |
| empty / missing | `SOURCE_PTR_MISSING` / `CLAIM_UNPOINTED` |

### Rank vocabulary (SKILL decision table)

`primary` > `secondary` > `aggregator` > `unsourced`.  
`proposal` is admitted as a **label**, never as substitute primary evidence for a `status=verified` claim (verified + ptr→proposal source → `SOURCE_RANK_INVALID` on the claim path via claim check noting proposal ceiling — implemented as claim ptr to proposal-ranked source with `status=verified` → finding on claim).

### Layer vocabulary (SKILL: observation / inference / unknown)

`layer=` required on every `@claim`. Invalid → `CLAIM_LAYER_INVALID`.

---

## 3. Output shape (stable compare)

```
research-gate r1 — ts=<ISO8601Z> — mode=verify|selftest — record=<path>
FINDING <ID> severity=<info|warn|crit> obs=<one-line>
…
RESEARCH_GATE: CLEAN|DRIFT (findings=N drift=M questions=Q sources=S chains=H claims=C negatives=N rejections=R approvals=A)
```

Selftest final line (last non-empty):

```
RESEARCH_GATE_SELFTEST: PASS (N cases)
```

or `FAIL (fail/N)`.

---

## 4. Hermetic `--selftest` (fixture contract shared with GateFixtureDesign)

- Work root: `mktemp -d /tmp/research-gate-selftest.XXXXXX` only; `trap rm -rf`.
- Each case writes one record file under `$WORK/records/`, runs verify against it, asserts **exit + substrings** (`RESEARCH_GATE:` verdict and/or `FINDING <ID>`).
- **No** live fleet paths, **no** network, **no** reads outside `$WORK` + the script itself.
- Minimum matrix (GateFixtureDesign expands ids/names; this script embeds the same classes):

| Case | Want exit | Want token |
|---|---|---|
| `pass-control` | 0 | `RESEARCH_GATE: CLEAN` (no FINDING) |
| `fail-schema` | 1 | `FINDING SCHEMA_MISSING` |
| `fail-question` | 1 | `FINDING QUESTION_MISSING` |
| `fail-source-none` | 1 | `FINDING SOURCE_NONE` |
| `fail-source-rank` | 1 | `FINDING SOURCE_RANK_INVALID` |
| `fail-source-ptr` | 1 | `FINDING SOURCE_PTR_MISSING` |
| `fail-chain-open` | 1 | `FINDING CHAIN_HOP_OPEN` |
| `fail-chain-reason` | 1 | `FINDING CHAIN_REASON_MISSING` |
| `fail-claim-ptr` | 1 | `FINDING CLAIM_UNPOINTED` |
| `fail-claim-layer` | 1 | `FINDING CLAIM_LAYER_INVALID` |
| `fail-negative-sweep` | 1 | `FINDING NEGATIVE_WITHOUT_SWEEP` |
| `fail-rejection-none` | 1 | `FINDING REJECTION_NONE` |
| `fail-rejection-reason` | 1 | `FINDING REJECTION_WITHOUT_REASON` |
| `fail-ephemeral` | 1 | `FINDING EPHEMERAL_POINTER` |
| `fail-external` | 1 | `FINDING EXTERNAL_UNAPPROVED` |
| `fail-boundary-kasegi` | 1 | `FINDING BOUNDARY_KASEGI` |
| `fail-boundary-kengaku` | 1 | `FINDING BOUNDARY_KENGAKU` |
| `fail-secret-shape` | 1 | `FINDING SECRET_SHAPE` |
| `setup-no-record` | 2 | usage/setup on stderr |
| `pass-unresolved-hop` | 0 | `CLEAN` (hop marked unresolved+reason) |

Embedded N at design time: **20 cases** (1 multi-pass + 17 defect/setup + 2 pass arms). Parent/GateFixtureDesign may raise N; pin exact N in SCORECARD when landed.

---

## 5. Boundary refusals (enforced)

| Refusal | Enforcement |
|---|---|
| No external fetch | no network tools; URL ptr without approval = DRIFT |
| No kasegi absorb | record body matching bounty-program / claim-package scope markers without `@chousa` boundary waive → `BOUNDARY_KASEGI` |
| No kengaku absorb | model-quality / LMSYS / arena-rating scope markers → `BOUNDARY_KENGAKU` |
| No secret values | secret-shaped assignments redacted; finding only |
| No remediation | never rewrites the record |
| Selftest write fence | only under `$WORK` |

Waive form (explicit, countable — not a silent bin):

```
@chousa boundary-waive=kasegi reason=citing-out-of-province-refusal-only
```

Without `reason=` the waive is ignored and the boundary finding still fires.

---

## 6. Full script (parent lands at `chousa-shokunin/tools/research-gate.sh`)

```bash
#!/usr/bin/env bash
# research-gate.sh — chousa method-contract gate (probation r1).
#
# Domain: whether a research RECORD satisfies the reusable deep-research method
# (question, ranked sources, chain hops resolved-or-marked, pointed claims,
# kept rejections, negative sweeps) without crossing hard boundaries.
# Product: FINDING lines + RESEARCH_GATE: CLEAN|DRIFT. Never remediates.
#
# Verdict: RESEARCH_GATE: CLEAN|DRIFT
# Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
# Selftest: RESEARCH_GATE_SELFTEST: PASS (N cases) | FAIL (fail/N)
#
# Record input: positional path, or CHOUSA_RECORD env.
# Grammar: research-record/v1 machine lines (@chousa/@question/@source/@chain/
# @claim/@negative/@rejection/@approval). See member report ResearchGateDesign.
#
# Env:
#   CHOUSA_RECORD   record path when no positional given
#   CHOUSA_ROOT     pointer resolution root (default: cwd)
#   CHOUSA_NOW_EPOCH pin clock for ts (selftest)
#
# Finding ids (stable):
#   SCHEMA_MISSING QUESTION_MISSING
#   SOURCE_NONE SOURCE_UNRANKED SOURCE_RANK_INVALID SOURCE_PTR_MISSING
#   CHAIN_NONE CHAIN_HOP_OPEN CHAIN_REASON_MISSING
#   CLAIM_NONE CLAIM_UNPOINTED CLAIM_LAYER_INVALID
#   NEGATIVE_WITHOUT_SWEEP
#   REJECTION_NONE REJECTION_WITHOUT_REASON
#   EPHEMERAL_POINTER EXTERNAL_UNAPPROVED
#   BOUNDARY_KASEGI BOUNDARY_KENGAKU SECRET_SHAPE
#
# Live/verify writes nothing. --selftest writes only under
# /tmp/research-gate-selftest.XXXXXX and removes it on EXIT.
#
set -euo pipefail

VERSION=research-gate-r1
SELF=$(readlink -f -- "${BASH_SOURCE[0]}" 2>/dev/null || {
  p=$0
  case "$p" in /*) printf '%s' "$p" ;; *) printf '%s' "$PWD/$p" ;; esac
})
SCRIPT_DIR=$(cd -- "$(dirname -- "$SELF")" && pwd)
LANE_ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)

MODE=verify
RECORD_ARG=""
ROOT=${CHOUSA_ROOT:-$PWD}
NOW_EPOCH=${CHOUSA_NOW_EPOCH:-}
if [[ -z $NOW_EPOCH ]]; then NOW_EPOCH=$(date +%s); fi
TS_UTC=$(date -u -d "@$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null \
  || date -u -r "$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null \
  || date -u +%Y-%m-%dT%H:%M:%SZ)

N_FINDINGS=0
N_DRIFT=0
ROLL=CLEAN
declare -a FINDING_LINES=()

N_QUESTION=0 N_SOURCE=0 N_CHAIN=0 N_CLAIM=0 N_NEG=0 N_REJ=0 N_APPR=0
SCHEMA_OK=0
BOUNDARY_WAIVE_KASEGI=0
BOUNDARY_WAIVE_KENGAKU=0
HAS_EXTERNAL_APPROVAL=0

declare -A SOURCE_RANK=()
declare -A SOURCE_PTR=()
declare -A SOURCE_SEEN=()

usage() {
  cat <<'EOF'
usage: research-gate.sh [--selftest] [--help] [RECORD]
       research-gate.sh verify [RECORD]

  RECORD           path to a research-record/v1 file (or set CHOUSA_RECORD)
  verify           default mode — validate one record
  --selftest       hermetic fixtures under /tmp/research-gate-selftest.*;
                   exit 0 pass, 1 fail, 2 setup
  --help           this text

Verdict: RESEARCH_GATE: CLEAN|DRIFT (findings=N drift=M …)
Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
Read-only verify; selftest writes only its mktemp tree.
EOF
}

die_usage() { printf 'research-gate: %s\n' "$1" >&2; usage >&2; exit 2; }

emit_finding() { # id severity observation
  local id=$1 sev=$2 obs=$3
  N_FINDINGS=$((N_FINDINGS + 1))
  FINDING_LINES+=("FINDING $id severity=$sev obs=$obs")
  case "$sev" in
    warn|crit)
      N_DRIFT=$((N_DRIFT + 1))
      ROLL=DRIFT
      ;;
  esac
}

# --- field tokenizer: key=value tokens before optional ':: text' --------------
# Sets: KV_<key> globals listed in want; REST_TEXT for free text after ::
REST_TEXT=""
clear_kv() {
  REST_TEXT=""
  KV_id=; KV_rank=; KV_ptr=; KV_status=; KV_layer=; KV_reason=; KV_sweep=
  KV_from=; KV_to=; KV_scope=; KV_window=; KV_title=; KV_note=; KV_schema=
  KV_boundary_waive=
}

parse_fields() { # line-without-directive
  local body=$1
  clear_kv
  if [[ $body == *'::'* ]]; then
    REST_TEXT=${body#*::}
    REST_TEXT=${REST_TEXT##+([[:space:]])}
    body=${body%%::*}
  fi
  # shellcheck disable=SC2086
  local tok
  for tok in $body; do
    case "$tok" in
      id=*) id_val=${tok#id=}; KV_id=$id_val ;;
      rank=*) KV_rank=${tok#rank=} ;;
      ptr=*) KV_ptr=${tok#ptr=} ;;
      status=*) KV_status=${tok#status=} ;;
      layer=*) KV_layer=${tok#layer=} ;;
      reason=*) KV_reason=${tok#reason=} ;;
      sweep=*) KV_sweep=${tok#sweep=} ;;
      from=*) KV_from=${tok#from=} ;;
      to=*) KV_to=${tok#to=} ;;
      scope=*) KV_scope=${tok#scope=} ;;
      window=*) KV_window=${tok#window=} ;;
      title=*) KV_title=${tok#title=} ;;
      note=*) KV_note=${tok#note=} ;;
      schema=*) KV_schema=${tok#schema=} ;;
      boundary-waive=*) KV_boundary_waive=${tok#boundary-waive=} ;;
    esac
  done
}

DEAD_MARK_RE='scratch|ephemeral|historical|unresolved|lost-tree|lost-base|proposal|formerly|removed|relocat'
EPHEM_RE='^(local|artifact|agent|proc)://'
URL_RE='^https?://'
SECRET_RE='(api[_-]?key|password|secret|token|bearer|authorization)[=:][[:space:]]*[^[:space:]]+'

line_has_dead_mark() {
  local line=$1
  grep -qiE "$DEAD_MARK_RE" <<<"$line"
}

ptr_is_ephemeral() {
  [[ $1 =~ $EPHEM_RE ]]
}

ptr_is_url() {
  [[ $1 =~ $URL_RE ]]
}

ptr_is_source_id() {
  [[ $1 =~ ^S[A-Za-z0-9_-]+$ ]]
}

# Strip optional backticks around ptr
norm_ptr() {
  local p=$1
  p=${p#\`}; p=${p%\`}
  p=${p#\'}; p=${p%\'}
  p=${p#\"}; p=${p%\"}
  printf '%s' "$p"
}

# Resolve path:line under ROOT; return 0 if file exists (line numbers not EOF-checked in r1)
ptr_file_resolves() {
  local p=$1 rel file
  p=$(norm_ptr "$p")
  rel=${p%%:*}
  [[ -n $rel && $rel != "$p" || -n $rel ]] || return 1
  # bare source ids handled elsewhere
  ptr_is_source_id "$p" && return 1
  ptr_is_ephemeral "$p" && return 1
  ptr_is_url "$p" && return 1
  file=$rel
  case "$file" in
    /*) [[ -f $file ]] && return 0; return 1 ;;
  esac
  if [[ -f $ROOT/$file ]]; then return 0; fi
  if [[ -f $LANE_ROOT/$file ]]; then return 0; fi
  return 1
}

check_ptr() { # ptr raw_line context_id -> may emit findings; echo class
  local ptr=$1 line=$2 ctx=$3
  ptr=$(norm_ptr "$ptr")
  if [[ -z $ptr ]]; then
    echo empty
    return
  fi
  if ptr_is_ephemeral "$ptr"; then
    if line_has_dead_mark "$line"; then
      echo ephemeral-marked
    else
      emit_finding EPHEMERAL_POINTER warn "ctx=$ctx ptr=$ptr needs dead-marker on same line"
      echo ephemeral
    fi
    return
  fi
  if ptr_is_url "$ptr"; then
    if [[ $HAS_EXTERNAL_APPROVAL -eq 1 ]]; then
      echo url-approved
    else
      emit_finding EXTERNAL_UNAPPROVED crit "ctx=$ctx ptr=$(printf '%.60s' "$ptr") no @approval scope=external status=granted"
      echo url-blocked
    fi
    return
  fi
  if ptr_is_source_id "$ptr"; then
    if [[ -n ${SOURCE_SEEN[$ptr]+x} ]]; then
      echo source-id
    else
      emit_finding CLAIM_UNPOINTED warn "ctx=$ctx ptr=$ptr source id not declared"
      echo source-missing
    fi
    return
  fi
  # path-like
  if ptr_file_resolves "$ptr"; then
    echo path-ok
    return
  fi
  if line_has_dead_mark "$line"; then
    echo path-marked
    return
  fi
  emit_finding CLAIM_UNPOINTED warn "ctx=$ctx ptr=$ptr unresolved path (no file under CHOUSA_ROOT, no dead-marker)"
  echo path-missing
}

# --- verify one record -------------------------------------------------------
verify_record() {
  local record=$1
  [[ -n $record ]] || die_usage "record path required (positional or CHOUSA_RECORD)"
  [[ -f $record ]] || die_usage "record is not a file: $record"
  [[ -r $record ]] || die_usage "record is unreadable: $record"

  local line lineno=0 dir body
  N_QUESTION=0 N_SOURCE=0 N_CHAIN=0 N_CLAIM=0 N_NEG=0 N_REJ=0 N_APPR=0
  SCHEMA_OK=0 BOUNDARY_WAIVE_KASEGI=0 BOUNDARY_WAIVE_KENGAKU=0 HAS_EXTERNAL_APPROVAL=0
  SOURCE_RANK=() SOURCE_PTR=() SOURCE_SEEN=()
  FINDING_LINES=() N_FINDINGS=0 N_DRIFT=0 ROLL=CLEAN

  # pass 0: approvals + schema + waives (so later ptr checks see approval)
  while IFS= read -r line || [[ -n $line ]]; do
    lineno=$((lineno + 1))
    case "$line" in
      @chousa*)
        parse_fields "${line#@chousa}"
        if [[ ${KV_schema:-} == research-record/v1 ]]; then SCHEMA_OK=1; fi
        if [[ ${KV_boundary_waive:-} == kasegi && -n ${KV_reason:-} ]]; then
          BOUNDARY_WAIVE_KASEGI=1
        fi
        if [[ ${KV_boundary_waive:-} == kengaku && -n ${KV_reason:-} ]]; then
          BOUNDARY_WAIVE_KENGAKU=1
        fi
        # bare @chousa schema=… also:
        if [[ $line == *"schema=research-record/v1"* ]]; then SCHEMA_OK=1; fi
        ;;
      @approval*)
        parse_fields "${line#@approval}"
        N_APPR=$((N_APPR + 1))
        if [[ ${KV_scope:-} == external && ${KV_status:-} == granted ]]; then
          HAS_EXTERNAL_APPROVAL=1
        fi
        ;;
    esac
  done <"$record"

  if [[ $SCHEMA_OK -eq 0 ]]; then
    emit_finding SCHEMA_MISSING crit "no @chousa schema=research-record/v1 line"
  fi

  # pass 1: body secret + boundary scans (whole-file)
  local blob
  blob=$(<"$record")
  if grep -qiE "$SECRET_RE" <<<"$blob"; then
    emit_finding SECRET_SHAPE crit "secret-shaped assignment present (values not printed)"
  fi
  if [[ $BOUNDARY_WAIVE_KASEGI -eq 0 ]]; then
    if grep -qiE '\b(bug[[:space:]]*bounty|claim[[:space:]]*package|vdp-disclosure|bounty-map)\b' <<<"$blob"; then
      emit_finding BOUNDARY_KASEGI crit "bounty-program scope markers without boundary-waive=kasegi reason="
    fi
  fi
  if [[ $BOUNDARY_WAIVE_KENGAKU -eq 0 ]]; then
    if grep -qiE '\b(model[[:space:]]*quality|lmsys|arena[[:space:]]*score|mmlu|hellaswag)\b' <<<"$blob"; then
      emit_finding BOUNDARY_KENGAKU crit "model-quality scope markers without boundary-waive=kengaku reason="
    fi
  fi

  # pass 2: structural directives
  lineno=0
  while IFS= read -r line || [[ -n $line ]]; do
    lineno=$((lineno + 1))
    case "$line" in
      @question*)
        body=${line#@question}
        body=${body##+([[:space:]])}
        if [[ -z $body ]]; then
          emit_finding QUESTION_MISSING warn "line=$lineno empty @question"
        else
          N_QUESTION=$((N_QUESTION + 1))
        fi
        ;;
      @source*)
        parse_fields "${line#@source}"
        N_SOURCE=$((N_SOURCE + 1))
        if [[ -z ${KV_id:-} ]]; then
          emit_finding SOURCE_UNRANKED warn "line=$lineno @source missing id="
          continue
        fi
        SOURCE_SEEN[$KV_id]=1
        if [[ -z ${KV_rank:-} ]]; then
          emit_finding SOURCE_UNRANKED warn "line=$lineno id=$KV_id missing rank="
        else
          case "$KV_rank" in
            primary|secondary|aggregator|unsourced|proposal)
              SOURCE_RANK[$KV_id]=$KV_rank
              ;;
            *)
              emit_finding SOURCE_RANK_INVALID warn "line=$lineno id=$KV_id rank=$KV_rank"
              ;;
          esac
        fi
        if [[ -z ${KV_ptr:-} ]]; then
          emit_finding SOURCE_PTR_MISSING warn "line=$lineno id=$KV_id missing ptr="
        else
          SOURCE_PTR[$KV_id]=$(norm_ptr "$KV_ptr")
          # source ptr checks (ephemeral/url/path)
          local pc
          pc=$(check_ptr "$KV_ptr" "$line" "source:$KV_id")
          # remap empty path findings already emitted; source-specific empty:
          if [[ $pc == empty ]]; then
            emit_finding SOURCE_PTR_MISSING warn "line=$lineno id=$KV_id empty ptr"
          fi
        fi
        ;;
      @chain*)
        parse_fields "${line#@chain}"
        N_CHAIN=$((N_CHAIN + 1))
        case "${KV_status:-}" in
          resolved) ;;
          unresolved)
            if [[ -z ${KV_reason:-} ]]; then
              emit_finding CHAIN_REASON_MISSING warn "line=$lineno id=${KV_id:-?} unresolved hop missing reason="
            fi
            ;;
          "")
            emit_finding CHAIN_HOP_OPEN warn "line=$lineno id=${KV_id:-?} missing status="
            ;;
          *)
            emit_finding CHAIN_HOP_OPEN warn "line=$lineno id=${KV_id:-?} status=${KV_status} not resolved|unresolved"
            ;;
        esac
        ;;
      @claim*)
        parse_fields "${line#@claim}"
        N_CLAIM=$((N_CLAIM + 1))
        local cid=${KV_id:-line-$lineno}
        case "${KV_layer:-}" in
          observation|inference|unknown|proposal) ;;
          "")
            emit_finding CLAIM_LAYER_INVALID warn "line=$lineno id=$cid missing layer="
            ;;
          *)
            emit_finding CLAIM_LAYER_INVALID warn "line=$lineno id=$cid layer=${KV_layer}"
            ;;
        esac
        if [[ -z ${KV_ptr:-} ]]; then
          emit_finding CLAIM_UNPOINTED warn "line=$lineno id=$cid missing ptr="
        else
          local pclass
          pclass=$(check_ptr "$KV_ptr" "$line" "claim:$cid")
          if [[ $pclass == empty ]]; then
            emit_finding CLAIM_UNPOINTED warn "line=$lineno id=$cid empty ptr"
          fi
          # verified claims may not rest solely on proposal-ranked source
          local pp
          pp=$(norm_ptr "$KV_ptr")
          if [[ ${KV_status:-} == verified ]] && ptr_is_source_id "$pp"; then
            if [[ ${SOURCE_RANK[$pp]:-} == proposal ]]; then
              emit_finding SOURCE_RANK_INVALID warn "claim=$cid status=verified ptr=$pp rank=proposal (proposal is not verified evidence)"
            fi
          fi
        fi
        ;;
      @negative*)
        parse_fields "${line#@negative}"
        N_NEG=$((N_NEG + 1))
        if [[ -z ${KV_sweep:-} ]]; then
          emit_finding NEGATIVE_WITHOUT_SWEEP warn "line=$lineno id=${KV_id:-?} negative claim missing sweep="
        fi
        ;;
      @rejection*)
        parse_fields "${line#@rejection}"
        N_REJ=$((N_REJ + 1))
        if [[ -z ${KV_reason:-} ]]; then
          emit_finding REJECTION_WITHOUT_REASON warn "line=$lineno id=${KV_id:-?} rejection missing reason="
        fi
        ;;
      @approval*) ;;
      @chousa*) ;;
    esac
  done <"$record"

  # aggregate emptiness (only if schema present — else SCHEMA_MISSING dominates)
  if [[ $SCHEMA_OK -eq 1 ]]; then
    if [[ $N_QUESTION -eq 0 ]]; then
      emit_finding QUESTION_MISSING warn "no non-empty @question line"
    fi
    if [[ $N_SOURCE -eq 0 ]]; then
      emit_finding SOURCE_NONE warn "no @source rows"
    fi
    if [[ $N_CLAIM -eq 0 ]]; then
      emit_finding CLAIM_NONE warn "no @claim rows"
    fi
    if [[ $N_CLAIM -gt 0 && $N_CHAIN -eq 0 ]]; then
      # claims without any chain: allowed only if every claim ptr is direct source/path
      # r1 policy: require at least one chain row when ≥1 claim (forces hop discipline)
      emit_finding CHAIN_NONE warn "claims=$N_CLAIM but no @chain hops (declare hop or mark unresolved)"
    fi
    if [[ $N_REJ -eq 0 ]]; then
      emit_finding REJECTION_NONE warn "no @rejection rows (keep rejects with reason=; use reason=none-recorded if none)"
    fi
  fi

  # print
  printf '%s %s — ts=%s — mode=verify — record=%s\n' \
    "research-gate" "$VERSION" "$TS_UTC" "$record"
  local f
  for f in "${FINDING_LINES[@]+"${FINDING_LINES[@]}"}"; do
    printf '%s\n' "$f"
  done
  printf 'RESEARCH_GATE: %s (findings=%d drift=%d questions=%d sources=%d chains=%d claims=%d negatives=%d rejections=%d approvals=%d)\n' \
    "$ROLL" "$N_FINDINGS" "$N_DRIFT" "$N_QUESTION" "$N_SOURCE" "$N_CHAIN" \
    "$N_CLAIM" "$N_NEG" "$N_REJ" "$N_APPR"

  if [[ $ROLL == CLEAN ]]; then return 0; fi
  return 1
}

# --- selftest ----------------------------------------------------------------
run_selftest() {
  local WORK cases=0 failures=0
  WORK=$(mktemp -d /tmp/research-gate-selftest.XXXXXX) \
    || die_usage "mktemp failed for selftest"
  trap 'rm -rf -- "$WORK"' EXIT
  mkdir -p "$WORK/records" "$WORK/src"
  # a real local file for path ptr resolution
  printf 'fixture source line one\nline two\n' >"$WORK/src/primary.md"
  export CHOUSA_ROOT="$WORK"
  export CHOUSA_NOW_EPOCH="$NOW_EPOCH"

  write_rec() { # name heredoc-via-stdin
    local name=$1
    cat >"$WORK/records/$name.md"
  }

  # shared PASS body pieces
  local HDR mon
  HDR='@chousa schema=research-record/v1'

  tcase() { # name want_rc want_substr
    local name=$1 want_rc=$2 want=$3
    local rc=0 out
    cases=$((cases + 1))
    set +e
    out=$(verify_record "$WORK/records/$name.md" 2>&1)
    rc=$?
    set -e
    if [[ $rc -eq $want_rc && $out == *"$want"* ]]; then
      printf 'ok-case  %-2d %-28s exit=%d\n' "$cases" "$name" "$rc"
    else
      printf 'FAIL-case %-28s exit=%d want=%d token=%s\n' "$name" "$rc" "$want_rc" "$want"
      printf '%s\n' "$out" | sed 's/^/    | /'
      failures=$((failures + 1))
    fi
  }

  # --- pass-control ---
  write_rec pass-control <<EOF
$HDR
@question When does an apprentice earn domain independence in Japanese craft tradition?
@source id=S1 rank=primary ptr=src/primary.md:1 title=fixture-primary
@source id=S2 rank=secondary ptr=src/primary.md:2 title=fixture-secondary
@claim id=C1 ptr=S1 layer=observation status=verified :: nenki-ake marks term completion in some trades
@chain id=H1 from=C1 to=S1 status=resolved
@negative id=N1 sweep=dict-web-zero-hits-jiniryuu :: jin'i-ryu is not an attested artisan rank
@rejection id=R1 reason=coined-system-term-not-tradition :: jin'i-ryu presented as inherited rank
@approval id=A1 scope=loopback window=none status=n/a
EOF
  tcase pass-control 0 'RESEARCH_GATE: CLEAN'

  # --- pass-unresolved-hop ---
  write_rec pass-unresolved-hop <<EOF
$HDR
@question What is the hop status when the cited URL is dead?
@source id=S1 rank=secondary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=unknown status=unresolved :: downstream primary not recovered
@chain id=H1 from=C1 to=https://example.invalid/primary status=unresolved reason=dead-link-not-fetched
@rejection id=R1 reason=none-recorded :: no source rejected beyond unresolved hop
@approval id=A1 scope=loopback window=none status=n/a
EOF
  # note: to= URL on chain is not auto-checked as claim ptr; CLEAN expected
  tcase pass-unresolved-hop 0 'RESEARCH_GATE: CLEAN'

  # --- fail-schema ---
  write_rec fail-schema <<'EOF'
# just prose, no machine schema
Someone said something on the web.
EOF
  tcase fail-schema 1 'FINDING SCHEMA_MISSING'

  # --- fail-question ---
  write_rec fail-question <<EOF
$HDR
@question
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-question 1 'FINDING QUESTION_MISSING'

  # --- fail-source-none ---
  write_rec fail-source-none <<EOF
$HDR
@question Q?
@claim id=C1 ptr=src/primary.md:1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=src/primary.md:1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-source-none 1 'FINDING SOURCE_NONE'

  # --- fail-source-rank ---
  write_rec fail-source-rank <<EOF
$HDR
@question Q?
@source id=S1 rank=legendary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-source-rank 1 'FINDING SOURCE_RANK_INVALID'

  # --- fail-source-ptr ---
  write_rec fail-source-ptr <<EOF
$HDR
@question Q?
@source id=S1 rank=primary
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-source-ptr 1 'FINDING SOURCE_PTR_MISSING'

  # --- fail-chain-open ---
  write_rec fail-chain-open <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=pending
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-chain-open 1 'FINDING CHAIN_HOP_OPEN'

  # --- fail-chain-reason ---
  write_rec fail-chain-reason <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=unresolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-chain-reason 1 'FINDING CHAIN_REASON_MISSING'

  # --- fail-claim-ptr ---
  write_rec fail-claim-ptr <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-claim-ptr 1 'FINDING CLAIM_UNPOINTED'

  # --- fail-claim-layer ---
  write_rec fail-claim-layer <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=vibes status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-claim-layer 1 'FINDING CLAIM_LAYER_INVALID'

  # --- fail-negative-sweep ---
  write_rec fail-negative-sweep <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@negative id=N1 :: no such thing
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-negative-sweep 1 'FINDING NEGATIVE_WITHOUT_SWEEP'

  # --- fail-rejection-none ---
  write_rec fail-rejection-none <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
EOF
  tcase fail-rejection-none 1 'FINDING REJECTION_NONE'

  # --- fail-rejection-reason ---
  write_rec fail-rejection-reason <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 :: dropped source with no reason field
EOF
  tcase fail-rejection-reason 1 'FINDING REJECTION_WITHOUT_REASON'

  # --- fail-ephemeral ---
  write_rec fail-ephemeral <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=local://round-1/scratch.md layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-ephemeral 1 'FINDING EPHEMERAL_POINTER'

  # --- fail-external ---
  write_rec fail-external <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=https://example.com/paper.pdf
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-external 1 'FINDING EXTERNAL_UNAPPROVED'

  # --- fail-boundary-kasegi ---
  write_rec fail-boundary-kasegi <<EOF
$HDR
@question How do bug bounty claim packages rank?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: claim package triage
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-boundary-kasegi 1 'FINDING BOUNDARY_KASEGI'

  # --- fail-boundary-kengaku ---
  write_rec fail-boundary-kengaku <<EOF
$HDR
@question What is the model quality arena score?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: lmsys rating discussed
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
EOF
  tcase fail-boundary-kengaku 1 'FINDING BOUNDARY_KENGAKU'

  # --- fail-secret-shape ---
  write_rec fail-secret-shape <<EOF
$HDR
@question Q?
@source id=S1 rank=primary ptr=src/primary.md:1
@claim id=C1 ptr=S1 layer=observation status=verified :: x
@chain id=H1 from=C1 to=S1 status=resolved
@rejection id=R1 reason=none-recorded :: n/a
# accidental paste: api_key=EXFIL-SHOULD-NOT-PRINT-THIS-VALUE
EOF
  tcase fail-secret-shape 1 'FINDING SECRET_SHAPE'

  # --- setup-no-record (exit 2) ---
  cases=$((cases + 1))
  set +e
  out=$(verify_record "" 2>&1)
  rc=$?
  set -e
  if [[ $rc -eq 2 ]]; then
    printf 'ok-case  %-2d %-28s exit=%d\n' "$cases" "setup-no-record" "$rc"
  else
    printf 'FAIL-case %-28s exit=%d want=2\n' "setup-no-record" "$rc"
    printf '%s\n' "$out" | sed 's/^/    | /'
    failures=$((failures + 1))
  fi

  if [[ $failures -eq 0 ]]; then
    printf 'RESEARCH_GATE_SELFTEST: PASS (%d cases)\n' "$cases"
    exit 0
  fi
  printf 'RESEARCH_GATE_SELFTEST: FAIL (%d/%d cases)\n' "$failures" "$cases"
  exit 1
}

# --- CLI ---------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h) usage; exit 0 ;;
    --selftest) MODE=selftest; shift ;;
    verify) MODE=verify; shift ;;
    --root)
      [[ $# -ge 2 ]] || die_usage "--root needs a path"
      ROOT=$2; shift 2
      ;;
    --)
      shift; break ;;
    -*)
      die_usage "unknown flag: $1" ;;
    *)
      if [[ -n $RECORD_ARG ]]; then die_usage "multiple record paths"; fi
      RECORD_ARG=$1
      shift
      ;;
  esac
done

case "$MODE" in
  selftest) run_selftest ;;
  verify)
    RECORD_PATH=${RECORD_ARG:-${CHOUSA_RECORD:-}}
    verify_record "$RECORD_PATH"
    ;;
  *) die_usage "unknown mode: $MODE" ;;
esac
```

---

## 7. Survey artifact expected results (calibration anchors)

| Artifact | Gate expectation (when pointed at without conversion) | Why |
|---|---|---|
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | DRIFT · `SCHEMA_MISSING` | chat export; no `@chousa` grammar; 0 path:line cites |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | DRIFT · `SCHEMA_MISSING` | same; arxiv bare labels only |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | DRIFT · `SCHEMA_MISSING` | same; dictionary/web labels only |
| `research/README.md` | DRIFT · `SCHEMA_MISSING` | index, not a research record |

A future corpus note that **converts** one export into `research-record/v1` (ranking Kotobank/dictionary as secondary/aggregator, marking jin'i-ryu rejection with sweep, pinning local README lines as the operator correction surface) is how chousa **admits** method knowledge — the export itself stays evidence of the failure mode, not a CLEAN record.

---

## 8. External-approval table (round deliverable shape)

Any rule needing a live external source stays `proposal` until an operator row exists:

| window_id | target_class | example | status | operator | notes |
|---|---|---|---|---|---|
| *(none yet)* | — | — | loopback-only default | — | SKILL.md:33-36; PROVINCE.md external refusal |

Gate: `@approval id=… scope=external status=granted window=…` is the only machine unlock for `http(s)` pointers. Designing the human table is in-province; filling it with live fetches is **out** of this wave.

---

## 9. Registry row draft (for GateRegistryRow peer / parent)

| Field | Value |
|---|---|
| **name** | `research-gate` |
| **kind** | `gate` |
| **entry** | `bash tools/research-gate.sh VERIFY_RECORD` (cwd = `chousa-shokunin/`) |
| **verdict map** | `0` → clean (`RESEARCH_GATE: CLEAN`) · `1` → failed (`RESEARCH_GATE: DRIFT`) · `2` → could-not-evaluate (setup/usage) |
| **self-test** | `bash tools/research-gate.sh --selftest` → `RESEARCH_GATE_SELFTEST: PASS (N cases)` |
| **pinned-value path** | embedded selftest case table in `tools/research-gate.sh`; optional `corpus/fixtures/research-gate-selftest.expected.md` |
| **write scope** | live/verify: **zero files**; selftest: `/tmp/research-gate-selftest.*` only |
| **owner** | `chousa` |

---

## 10. Risks / blockers / non-goals

| Item | Notes |
|---|---|
| **Prose-only records** | r1 does not NLP-parse chat exports; conversion to `@` directives is author work. Honest: exports FAIL schema. |
| **Line EOF checks** | r1 resolves file existence only; PAST-EOF class is **proposal** (kasegi `anchorcheck.py` is the precedent to lift later). |
| **Chain `to=` URL** | not full ptr-checked in r1 (status+reason is the tooth); proposal to unify with `check_ptr`. |
| **GateFixtureDesign** | may rename cases or raise N; finding **id strings** above are the pin — reconcile on parent land. |
| **extglob** | `parse_fields` uses `${var##+([[:space:]])}` — needs `shopt -s extglob` on some bash builds; parent should add `shopt -s extglob` near `set -euo pipefail` if landing on strict bash. **Patch note for parent:** insert `shopt -s extglob` after `set -euo pipefail`. |
| **No subagent / no land** | this seat writes only this report path. |
| **tools/ absent** | lane has no `tools/` yet — parent creates on land. |

### Parent land checklist

1. `mkdir -p chousa-shokunin/tools`
2. Write script from §6; add `shopt -s extglob` immediately after `set -euo pipefail`
3. `chmod +x tools/research-gate.sh`
4. Run `bash tools/research-gate.sh --selftest` — expect `RESEARCH_GATE_SELFTEST: PASS (20 cases)` exit 0
5. Optionally point verify at a converted corpus record once one exists
6. Pin N + finding-id list on SCORECARD / corpus note
7. Do **not** expect CLEAN on raw `research/deep-research-2026-09-28/*`

---

## 11. Evidence retained (local only)

| Path | Role |
|---|---|
| `chousa-shokunin/SKILL.md:14-53` | decision table, checklist, gate stub |
| `chousa-shokunin/corpus/QUALITY.md:1-5` | admission bar (rejection kept, layers split) |
| `chousa-shokunin/PROVINCE.md:1-14` | hard refuses |
| `research/README.md:1-17` | export provenance (not Deep Research pipeline) |
| `research/deep-research-2026-09-28/{A,B,C}-*.md` | survey material; chat chrome + unverified citations |
| `kagi-shokunin/corpus/claim-ledger.sh:1-96` | exit/verdict/selftest discipline precedent |
| `kasegi-shokunin/corpus/knowledge/citation-bases.md:1-120` | base vocabulary + lost-prefix precedent |
| `kasegi-shokunin/corpus/instruments/anchorcheck.py:130-280` | anchor classes precedent |
| GateFixtureDesign IRC ack | CLI/finding/selftest spelling alignment |

---

**End of advisory report.** No judge verdict claimed. Script provided for parent land only; no remediation; no external fetch.
