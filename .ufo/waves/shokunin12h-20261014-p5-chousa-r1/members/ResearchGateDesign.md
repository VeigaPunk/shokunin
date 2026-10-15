# ResearchGateDesign — `tools/research-gate.sh`

**Member:** ResearchGateDesign (executor) · **Wave:** shokunin12h-20261014-p5-chousa-r1  
**Lane:** chousa-shokunin (shonen probation r1) · **Role:** design only — parent lands the file  
**Axes:** coverage · depth · calibration  
**Measured:** 2026-10-15T01:12:00Z (UTC) · local read-only; no external fetches  
**Lane HEAD (seed):** `02a615a93a3cfa7583bc165700522709cd47089e` · fleet short: `a9f4d25`  
**Peers consumed:** FindingIds · GateFixtureDesign · RecordShape · SecrecyAudit  
**Severity note:** FINDING lines use only `info|warn|crit` (GateFixtureDesign). FindingIds catalog `high` maps into `warn` or `crit` here — never emit bare `high` (would not flip DRIFT).

Advisory only. Not a judge verdict. Parent cuts script to `chousa-shokunin/tools/research-gate.sh`.

---

## 0. Axes

| Axis | Move kept |
|---|---|
| **coverage** | SKILL five teeth + FindingIds exemplars + secrecy/session denylist + external approval + export-as-data |
| **depth** | Parses RecordShape/GateFixtureDesign Markdown sections; hop resolved-or-marked; rejections kept with reason; negative sweeps required |
| **calibration** | Preferred FINDING ids = FindingIds/GateFixtureDesign spellings; CLEAN never with SECRET_SHAPED; path opens allowlisted only; README CDP 9222 is provenance, not a hop |

---

## 1. Contract

| Item | Value |
|---|---|
| Path | `chousa-shokunin/tools/research-gate.sh` |
| Modes | `verify` (default) · `--selftest` · `--help` |
| Record input | `--record PATH` · positional PATH · or `CHOUSA_RECORD` |
| Root | `--root` / `CHOUSA_ROOT` (pointer resolve root; default cwd) |
| Verdict | `RESEARCH_GATE: CLEAN\|DRIFT (findings=N drift=M …)` |
| Selftest rollup | `RESEARCH_GATE_SELFTEST: PASS (N cases)` / `FAIL (fail/N)` |
| Exit | `0` CLEAN/selftest-pass · `1` DRIFT/selftest-fail · `2` setup/usage |
| FINDING line | `FINDING <ID> severity=<info\|warn\|crit> surface=<family> obs=<short>` |
| Write scope | verify: **zero files**; selftest: `mktemp -d /tmp/chousa-research-gate-selftest.XXXXXX` only |
| Network | none |
| Secrets | on hit print **path:line class=… only** — never matched span, never hash of secret bytes |
| Path opens | allowlist only (§5). Denylist → `SESSION_READ`, not opened. `research/README.md` CDP/9222 text is provenance prose, never a hop |

### Method teeth → preferred finding ids

| Contract clause | Preferred id | Sev emitted |
|---|---|---|
| Question declared | `NO_QUESTION` | crit |
| Sources ranked | `UNRANKED_SOURCE` · `SOURCE_TABLE_ABSENT` · `HIERARCHY_PRIMARY_LIE` | warn |
| Chain hops resolved-or-marked | `CHAIN_HOP_UNRESOLVED` · `CHAIN_ABSENT` | warn |
| Claims pointed | `CLAIM_UNPOINTED` · `CLAIM_TABLE_ABSENT` · `POINTER_EPHEMERAL` · `POINTER_UNRESOLVED` | warn |
| Rejections kept | `REJECTION_DROPPED` · `REJECTION_REASON_ABSENT` | warn |
| Negative sweep | `NEGATIVE_WITHOUT_SWEEP` | warn |
| Obs/inference split | `OBS_INFERENCE_COLLAPSE` | warn |
| External window | `EXTERNAL_WITHOUT_APPROVAL` | crit |
| Secrecy | `SECRET_SHAPED` · `SESSION_READ` | crit |
| Schema | `RECORD_SCHEMA_INVALID` | warn |
| Export chrome | `EXPORT_CHROME_PRESENT` | info |

**r1 emits preferred spellings only** (no IRC alias dual-emit).

### CLEAN vs DRIFT

- **CLEAN** — required sections present; sources tiered; chain hops in allowed status set (unresolved family has notes/reason); non-opinion claims pointed; `## Rejections` present; negatives swept; zero `warn|crit`; **zero** `SECRET_SHAPED`/`SESSION_READ`.
- **DRIFT** — any `warn|crit` finding.
- **Exit 2** — bad CLI / missing record / mktemp failure.

### Central survey finding

Raw `research/deep-research-2026-09-28/{A,B,C}-*.md` are chat-export transcripts (`research/README.md:6-8`), **not** research-records. Gate → DRIFT (`RECORD_SCHEMA_INVALID` / `NO_QUESTION` / export chrome). That is the method signal.

---

## 2. Record grammar

Accept GateFixtureDesign headings; RecordShape aliases in parentheses:

- `## Meta`
- `## Question`
- `## Sources` (`## Source table`)
- `## Chain` (`## Chains`)
- `## Claims`
- `## Negatives` / `## Sweeps`
- `## Rejections`
- `## Unknowns`
- `## Rules`
- `## Approval` (`## Approvals`)
- optional `## Stop`

Banner optional: `# research-record v1` or `<!-- chousa-record: v1 -->`.

**Sources cols:** id, tier, pointer (tier ∈ primary|secondary|aggregator|unsourced|rejected|export|fleet-gate|proposal).  
**Chain cols:** hop, from, to, status ∈ resolved|unresolved|rejected|blocked-no-fetch|labelled-dead|not-applicable (+ notes/reason).  
**Claims cols:** id, kind ∈ observation|inference|negative|opinion|proposal|unknown, text, pointer, status, sweep.  
**Rejections cols:** id, ref, reason (non-empty).

---

## 3. Output shape

```
research-gate r1 — ts=<ISO8601Z> — mode=verify — record=<path>
FINDING NO_QUESTION severity=crit surface=question obs=missing ## Question body
…
RESEARCH_GATE: DRIFT (findings=N drift=M questions=Q sources=S chains=H claims=C negatives=N rejections=R approvals=A)
```

Selftest last line: `RESEARCH_GATE_SELFTEST: PASS (N cases)`.

---

## 4. Selftest matrix (GateFixtureDesign pin)

Work root: `/tmp/chousa-research-gate-selftest.XXXXXX` only.

| Case | Exit | Token |
|---|---|---|
| pass-control | 0 | `RESEARCH_GATE: CLEAN` |
| pass-hop-marked-unresolved | 0 | `CLEAN` |
| fail-no-question | 1 | `FINDING NO_QUESTION` |
| fail-unranked-source | 1 | `FINDING UNRANKED_SOURCE` |
| fail-chain-hop-unresolved | 1 | `FINDING CHAIN_HOP_UNRESOLVED` |
| fail-claim-unpointed | 1 | `FINDING CLAIM_UNPOINTED` |
| fail-rejection-dropped | 1 | `FINDING REJECTION_DROPPED` |
| fail-negative-without-sweep | 1 | `FINDING NEGATIVE_WITHOUT_SWEEP` |
| fail-obs-inference-collapse | 1 | `FINDING OBS_INFERENCE_COLLAPSE` |
| fail-hierarchy-primary-lie | 1 | `FINDING HIERARCHY_PRIMARY_LIE` |
| fail-pointer-ephemeral | 1 | `FINDING POINTER_EPHEMERAL` |
| fail-external-without-approval | 1 | `FINDING EXTERNAL_WITHOUT_APPROVAL` |
| fail-secret-shaped | 1 | `FINDING SECRET_SHAPED` + obs has `class=` and **must not** contain planted value |
| fail-session-read | 1 | `FINDING SESSION_READ` |
| fail-schema | 1 | `FINDING RECORD_SCHEMA_INVALID` |
| setup-no-record | 2 | setup |
| setup-missing-file | 2 | setup |

Floor **N=17**. Secret plant = synthetic only (`sk-fxdemo_not_real_0000`); never live token.

---

## 5. Path allowlist / denylist (SecrecyAudit)

**Allow (metadata `test -f` only; never print file body in findings):** record path; paths under `CHOUSA_ROOT`; when root is fleet, also lane `chousa-shokunin/**`, the four `research/` survey files, and named precedents (`claim-ledger.sh`, `anchorcheck.py`, `citation-bases.md`) for existence checks.

**Deny → `SESSION_READ` (do not open):** `op.env`, `*.env`, `server.token`, `credentials/`, `~/.omp/**`, chrome-profile/Cookies, URLs with port 9222 or `/json`.

**README:6 CDP 9222** = provenance prose, not a hop. No connect.

---

## 6. Full script (parent lands at `chousa-shokunin/tools/research-gate.sh`)

```bash
#!/usr/bin/env bash
# research-gate.sh — chousa research-record method gate (probation r1).
#
# Validates Markdown research records: question, ranked sources, chain hops
# resolved-or-marked, pointed claims, kept rejections, negative sweeps;
# hard bounds on external fetch, secrecy, session paths.
#
# Verdict: RESEARCH_GATE: CLEAN|DRIFT
# Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
# Selftest: RESEARCH_GATE_SELFTEST: PASS (N cases) | FAIL (fail/N)
#
# FINDING <ID> severity=<info|warn|crit> surface=<family> obs=<short>
#
# Preferred ids: NO_QUESTION UNRANKED_SOURCE SOURCE_TABLE_ABSENT
#   HIERARCHY_PRIMARY_LIE CHAIN_HOP_UNRESOLVED CHAIN_ABSENT
#   CLAIM_UNPOINTED CLAIM_TABLE_ABSENT POINTER_EPHEMERAL POINTER_UNRESOLVED
#   REJECTION_DROPPED REJECTION_REASON_ABSENT NEGATIVE_WITHOUT_SWEEP
#   OBS_INFERENCE_COLLAPSE EXTERNAL_WITHOUT_APPROVAL SECRET_SHAPED
#   SESSION_READ RECORD_SCHEMA_INVALID EXPORT_CHROME_PRESENT
#
# Secrecy: print path:line class=<name> only — never span.
# Opens: allowlist metadata only; denylist → SESSION_READ.
# research/README CDP 9222 is provenance, not a hop.
#
set -euo pipefail
shopt -s extglob

VERSION=research-gate-r1
SELF=$(readlink -f -- "${BASH_SOURCE[0]}" 2>/dev/null || {
  p=$0; case "$p" in /*) printf '%s' "$p" ;; *) printf '%s' "$PWD/$p" ;; esac
})
SCRIPT_DIR=$(cd -- "$(dirname -- "$SELF")" && pwd)
LANE_ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)

MODE=verify
RECORD_ARG=""
ROOT=${CHOUSA_ROOT:-$PWD}
STRICT=${CHOUSA_STRICT:-0}
AGG_ERE=${CHOUSA_AGGREGATOR_ERE:-'aggregator|wikipedia|secondary-summary|chat-export-sources'}
NOW_EPOCH=${CHOUSA_NOW_EPOCH:-}
[[ -n $NOW_EPOCH ]] || NOW_EPOCH=$(date +%s)
TS_UTC=$(date -u -d "@$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null \
  || date -u -r "$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null \
  || date -u +%Y-%m-%dT%H:%M:%SZ)

N_FINDINGS=0 N_DRIFT=0 ROLL=CLEAN
declare -a FINDING_LINES=()

N_Q=0 N_SRC=0 N_CH=0 N_CL=0 N_NEG=0 N_REJ=0 N_APPR=0
HAS_META=0 HAS_SOURCES_SEC=0 HAS_CHAIN_SEC=0 HAS_CLAIMS_SEC=0
HAS_REJ_SEC=0 HAS_NEG_SEC=0 HAS_APPROVAL_SEC=0 HAS_SWEEP_SEC=0
SCHEMA_HINT=0 WINDOW_EXTERNAL=0 APPROVAL_GRANTED=0 REJECT_MARKERS=0

usage() {
  cat <<'EOF'
usage: research-gate.sh [--selftest] [--help]
       research-gate.sh verify [--record PATH] [--root PATH]
       research-gate.sh [--record PATH] [--root PATH]

  RECORD via --record, positional, or CHOUSA_RECORD.
Verdict: RESEARCH_GATE: CLEAN|DRIFT
Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
EOF
}

die_usage() { printf 'research-gate: %s\n' "$1" >&2; usage >&2; exit 2; }

emit_finding() { # id severity surface obs
  local id=$1 sev=$2 surface=$3 obs=$4
  N_FINDINGS=$((N_FINDINGS + 1))
  FINDING_LINES+=("FINDING $id severity=$sev surface=$surface obs=$obs")
  case "$sev" in
    warn|crit) N_DRIFT=$((N_DRIFT + 1)); ROLL=DRIFT ;;
    info) [[ $STRICT == 1 ]] && { N_DRIFT=$((N_DRIFT + 1)); ROLL=DRIFT; } ;;
  esac
}

declare -A SEC_BODY=()
declare -a SEC_ORDER=()

load_sections() {
  local file=$1 line sec=""
  SEC_BODY=(); SEC_ORDER=()
  while IFS= read -r line || [[ -n $line ]]; do
    if [[ $line =~ ^##[[:space:]]+(.*)$ ]]; then
      sec=$(printf '%s' "${BASH_REMATCH[1]}" | sed 's/[[:space:]]*$//')
      case "$sec" in
        "Source table") sec="Sources" ;;
        Chains) sec="Chain" ;;
        Approvals) sec="Approval" ;;
      esac
      SEC_ORDER+=("$sec")
      SEC_BODY[$sec]=""
      continue
    fi
    [[ -z $sec ]] && continue
    SEC_BODY[$sec]+="$line"$'\n'
  done <"$file"
}

table_rows() {
  local sec=$1 body row
  body=${SEC_BODY[$sec]-}
  [[ -n $body ]] || return 0
  local -a headers=()
  local header_done=0
  while IFS= read -r row; do
    [[ $row == \|*\|* ]] || continue
    local inner=${row#|}
    inner=${inner%|}
    if [[ $header_done -eq 0 ]]; then
      if [[ $inner =~ ^[[:space:]]*-+ ]]; then
        header_done=1
        continue
      fi
      if [[ ${#headers[@]} -eq 0 ]]; then
        IFS='|' read -r -a headers <<<"$inner"
        local i
        for i in "${!headers[@]}"; do
          headers[$i]=$(printf '%s' "${headers[$i]}" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | tr 'A-Z' 'a-z')
        done
        continue
      fi
    fi
    [[ $inner =~ ^[[:space:]]*-+ ]] && continue
    local -a cols=()
    IFS='|' read -r -a cols <<<"$inner"
    local j out=""
    for j in "${!headers[@]}"; do
      local c=${cols[$j]-}
      c=$(printf '%s' "$c" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
      out+="${headers[$j]}=$c"$'\t'
    done
    printf '%s\n' "$out"
  done <<<"$body"
}

cell() {
  local row=$1 key=$2
  key=$(printf '%s' "$key" | tr 'A-Z' 'a-z')
  case "$key" in
    rank) key=tier ;;
    src_id) key=id ;;
    path_or_token|path|points_to) key=pointer ;;
    to_token) key=to ;;
  esac
  local e k v
  IFS=$'\t' read -r -a ents <<<"$row"
  for e in "${ents[@]}"; do
    [[ $e == *'='* ]] || continue
    k=${e%%=*}; v=${e#*=}
    k=$(printf '%s' "$k" | tr 'A-Z' 'a-z')
    case "$k" in
      rank) k=tier ;;
      src_id) k=id ;;
      path_or_token|path|points_to) k=pointer ;;
      to_token) k=to ;;
    esac
    if [[ $k == "$key" ]]; then printf '%s' "$v"; return 0; fi
  done
  printf ''
}

section_nonempty_prose() {
  local sec=$1 line body=${SEC_BODY[$sec]-}
  [[ -n $body ]] || return 1
  while IFS= read -r line; do
    [[ -z ${line//[[:space:]]/} ]] && continue
    [[ $line == \|* ]] && continue
    [[ $line == \<!--* ]] && continue
    return 0
  done <<<"$body"
  local n
  n=$(table_rows "$sec" | grep -c . || true)
  [[ ${n:-0} -gt 0 ]]
}

norm_ptr() {
  local p=$1
  p=${p#\`}; p=${p%\`}
  printf '%s' "$p"
}

ptr_file_part() {
  local p; p=$(norm_ptr "$1")
  printf '%s' "${p%%:*}"
}

is_ephemeral_ptr() {
  [[ $(norm_ptr "$1") =~ ^(local|artifact|agent|proc|history):// ]]
}

is_url_ptr() {
  [[ $(norm_ptr "$1") =~ ^https?:// ]]
}

is_session_url() {
  local p; p=$(norm_ptr "$1")
  [[ $p =~ :9222(/|$) || $p =~ /json(/|list)?$ ]]
}

DEAD_MARK_RE='ephemeral|scratch|historical|unresolved|lost-tree|lost-base|formerly|removed|relocat|labelled-dead|blocked-no-fetch|proposal'

line_has_mark() { grep -qiE "$DEAD_MARK_RE" <<<"$1"; }

is_denylist_path() {
  local f; f=$(ptr_file_part "$1")
  case "$f" in
    *op.env|*.env|*server.token*|*credentials/*|*/oauth/*) return 0 ;;
  esac
  [[ $f == *chrome-profile* || $f == *Cookies* || $f == *"Login Data"* ]] && return 0
  [[ $f == *'/.omp/'* || $f == *'/.config/'* || $f == *'/.local/state/'* ]] && return 0
  return 1
}

ptr_resolves_meta() {
  local p f
  p=$(norm_ptr "$1")
  is_ephemeral_ptr "$p" && return 1
  is_url_ptr "$p" && return 1
  is_denylist_path "$p" && return 1
  f=$(ptr_file_part "$p")
  [[ -z $f ]] && return 1
  if [[ $f != /* ]]; then
    [[ -f $ROOT/$f || -f $LANE_ROOT/$f ]] && return 0
    return 1
  fi
  local root_r
  root_r=$(cd -- "$ROOT" 2>/dev/null && pwd -P || printf '%s' "$ROOT")
  case "$f" in
    "$root_r"/*) [[ -f $f ]] && return 0 ;;
  esac
  return 1
}

check_pointer() {
  local ptr=$1 row=$2 surface=$3 ctx=$4
  ptr=$(norm_ptr "$ptr")
  if [[ -z $ptr ]]; then
    emit_finding CLAIM_UNPOINTED warn "$surface" "ctx=$ctx empty pointer"
    return 1
  fi
  if is_session_url "$ptr" || is_denylist_path "$ptr"; then
    emit_finding SESSION_READ crit secrecy "ctx=$ctx path=$(ptr_file_part "$ptr") denied (not opened)"
    return 1
  fi
  if is_ephemeral_ptr "$ptr"; then
    if line_has_mark "$row"; then return 0; fi
    emit_finding POINTER_EPHEMERAL warn "$surface" "ctx=$ctx ptr_class=ephemeral unlabeled"
    return 1
  fi
  if is_url_ptr "$ptr"; then
    if [[ $APPROVAL_GRANTED -eq 1 && $WINDOW_EXTERNAL -eq 1 ]]; then return 0; fi
    emit_finding EXTERNAL_WITHOUT_APPROVAL crit approval "ctx=$ctx url pointer without approved external window"
    return 1
  fi
  # declared source id (S1, …) is a valid pointer once Sources pass filled SRC_TIER
  if [[ $ptr =~ ^S[A-Za-z0-9_-]+$ ]]; then
    if [[ -n ${SRC_TIER[$ptr]+x} ]]; then return 0; fi
    emit_finding POINTER_UNRESOLVED warn "$surface" "ctx=$ctx source_id=$ptr not in ## Sources"
    return 1
  fi
  if ptr_resolves_meta "$ptr"; then return 0; fi
  if line_has_mark "$row"; then return 0; fi
  emit_finding POINTER_UNRESOLVED warn "$surface" "ctx=$ctx ptr=$(printf '%.80s' "$ptr") missing under CHOUSA_ROOT"
  return 1
}

scan_secrets() {
  local file=$1 lineno=0 line class
  while IFS= read -r line || [[ -n $line ]]; do
    lineno=$((lineno + 1))
    class=""
    if [[ $line =~ op:// ]]; then class=op_uri
    elif [[ $line =~ Bearer[[:space:]]+[A-Za-z0-9._~+/=-]{8,} ]]; then class=bearer
    elif [[ $line =~ sk-[A-Za-z0-9_]{10,} ]]; then class=sk_prefix
    elif [[ $line =~ ghp_[A-Za-z0-9]{20,} ]]; then class=ghp_prefix
    elif [[ $line =~ github_pat_[A-Za-z0-9_]{10,} ]]; then class=github_pat
    elif [[ $line =~ AKIA[A-Z0-9]{12,} ]]; then class=aws_akia
    elif [[ $line =~ BEGIN[[:space:]]+OPENSSH[[:space:]]+PRIVATE[[:space:]]+KEY ]]; then class=ssh_key
    elif [[ $line =~ BEGIN[[:space:]]+([A-Z]+[[:space:]]+)?PRIVATE[[:space:]]+KEY ]]; then class=pem_key
    elif [[ $line =~ server\.token=[[:graph:]]+ ]]; then class=server_token_assign
    elif [[ $line =~ api[_-]?key=[[:graph:]]+ ]]; then class=api_key_assign
    elif [[ $line =~ password=[[:graph:]]+ ]]; then class=password_assign
    fi
    if [[ -n $class ]]; then
      emit_finding SECRET_SHAPED crit secrecy "path=$file:$lineno class=$class"
    fi
  done <"$file"
}

verify_record() {
  local record=$1
  [[ -n ${record:-} ]] || die_usage "record path required (--record, positional, or CHOUSA_RECORD)"
  [[ -e $record ]] || die_usage "record not found: $record"
  [[ -f $record ]] || die_usage "record is not a regular file: $record"
  [[ -r $record ]] || die_usage "record unreadable: $record"

  FINDING_LINES=(); N_FINDINGS=0; N_DRIFT=0; ROLL=CLEAN
  N_Q=0 N_SRC=0 N_CH=0 N_CL=0 N_NEG=0 N_REJ=0 N_APPR=0
  HAS_META=0 HAS_SOURCES_SEC=0 HAS_CHAIN_SEC=0 HAS_CLAIMS_SEC=0
  HAS_REJ_SEC=0 HAS_NEG_SEC=0 HAS_APPROVAL_SEC=0 HAS_SWEEP_SEC=0
  SCHEMA_HINT=0 WINDOW_EXTERNAL=0 APPROVAL_GRANTED=0 REJECT_MARKERS=0

  if head -n 5 -- "$record" | grep -qE 'research-record v1|chousa-record: v1'; then
    SCHEMA_HINT=1
  fi

  load_sections "$record"

  local s
  for s in "${SEC_ORDER[@]+"${SEC_ORDER[@]}"}"; do
    case "$s" in
      Meta) HAS_META=1 ;;
      Sources) HAS_SOURCES_SEC=1 ;;
      Chain) HAS_CHAIN_SEC=1 ;;
      Claims) HAS_CLAIMS_SEC=1 ;;
      Rejections) HAS_REJ_SEC=1 ;;
      Negatives) HAS_NEG_SEC=1 ;;
      Approval) HAS_APPROVAL_SEC=1 ;;
      Sweeps) HAS_SWEEP_SEC=1 ;;
    esac
  done

  if [[ $HAS_META -eq 0 && $HAS_SOURCES_SEC -eq 0 && $HAS_CLAIMS_SEC -eq 0 && $SCHEMA_HINT -eq 0 ]]; then
    emit_finding RECORD_SCHEMA_INVALID warn meta "no research-record sections/banner detected"
  fi

  if grep -qE '^(Skip to content|ChatGPT|You said:)' "$record"; then
    emit_finding EXPORT_CHROME_PRESENT info export "chat-export chrome lines present (data, not instruction)"
  fi

  if [[ $HAS_META -eq 1 ]]; then
    if grep -qiE 'window_mode:[[:space:]]*external|fetch:[[:space:]]*(external|live)|origin=external-live' <<<"${SEC_BODY[Meta]}"; then
      WINDOW_EXTERNAL=1
    fi
  fi
  if grep -qiE 'fetch=external|window=live-external|origin=external-live|window_mode[[:space:]]*[|][[:space:]]*external' "$record"; then
    WINDOW_EXTERNAL=1
  fi

  if [[ $HAS_APPROVAL_SEC -eq 1 ]]; then
    local arow st
    while IFS= read -r arow; do
      [[ -z $arow ]] && continue
      N_APPR=$((N_APPR + 1))
      st=$(cell "$arow" state)
      [[ -z $st ]] && st=$(cell "$arow" status)
      case "$(printf '%s' "$st" | tr 'A-Z' 'a-z')" in
        approved|granted) APPROVAL_GRANTED=1 ;;
      esac
    done < <(table_rows Approval)
  fi
  if [[ $WINDOW_EXTERNAL -eq 1 && $APPROVAL_GRANTED -eq 0 ]]; then
    emit_finding EXTERNAL_WITHOUT_APPROVAL crit approval "external/live window without approval state=approved|granted"
  fi

  scan_secrets "$record"

  if [[ -z ${SEC_BODY[Question]+x} ]]; then
    emit_finding NO_QUESTION crit question "missing ## Question section"
  else
    if section_nonempty_prose Question; then N_Q=1
    else emit_finding NO_QUESTION crit question "## Question present but empty"
    fi
  fi

  declare -g -A SRC_TIER=()
  if [[ $HAS_SOURCES_SEC -eq 0 ]]; then
    emit_finding SOURCE_TABLE_ABSENT warn sources "missing ## Sources / ## Source table"
  else
    local srow id tier ptr
    while IFS= read -r srow; do
      [[ -z $srow ]] && continue
      N_SRC=$((N_SRC + 1))
      id=$(cell "$srow" id); [[ -z $id ]] && id="row$N_SRC"
      tier=$(cell "$srow" tier | tr 'A-Z' 'a-z')
      ptr=$(cell "$srow" pointer)
      if [[ -z $tier ]]; then
        emit_finding UNRANKED_SOURCE warn sources "source=$id missing tier"
      else
        case "$tier" in
          primary|secondary|aggregator|unsourced|rejected|export|fleet-gate|proposal)
            SRC_TIER[$id]=$tier
            [[ $tier == rejected ]] && REJECT_MARKERS=$((REJECT_MARKERS + 1))
            ;;
          *) emit_finding UNRANKED_SOURCE warn sources "source=$id tier=$tier not in allowed set" ;;
        esac
      fi
      if [[ -z $ptr ]]; then
        emit_finding UNRANKED_SOURCE warn sources "source=$id missing pointer"
      else
        local fpart; fpart=$(ptr_file_part "$ptr")
        if [[ ${tier:-} == primary ]]; then
          if grep -qiE "$AGG_ERE" <<<"$fpart $srow"; then
            emit_finding HIERARCHY_PRIMARY_LIE warn sources "source=$id primary but aggregator-class path/class"
          fi
          local cls; cls=$(cell "$srow" class | tr 'A-Z' 'a-z')
          [[ $cls == aggregator ]] && emit_finding HIERARCHY_PRIMARY_LIE warn sources "source=$id primary with class=aggregator"
        fi
        check_pointer "$ptr" "$srow" sources "source:$id" || true
      fi
    done < <(table_rows Sources)
    if [[ $N_SRC -eq 0 ]]; then
      emit_finding SOURCE_TABLE_ABSENT warn sources "## Sources has no data rows"
    fi
  fi

  if [[ $HAS_CLAIMS_SEC -eq 0 ]]; then
    emit_finding CLAIM_TABLE_ABSENT warn claims "missing ## Claims"
  else
    local crow cid kind ptr st sweep
    while IFS= read -r crow; do
      [[ -z $crow ]] && continue
      N_CL=$((N_CL + 1))
      cid=$(cell "$crow" id); [[ -z $cid ]] && cid="C$N_CL"
      kind=$(cell "$crow" kind | tr 'A-Z' 'a-z')
      ptr=$(cell "$crow" pointer)
      st=$(cell "$crow" status | tr 'A-Z' 'a-z')
      sweep=$(cell "$crow" sweep)
      if [[ -z $kind ]]; then
        emit_finding OBS_INFERENCE_COLLAPSE warn claims "claim=$cid missing kind="
      else
        case "$kind" in
          observation|inference|negative|opinion|proposal|unknown) ;;
          *) emit_finding OBS_INFERENCE_COLLAPSE warn claims "claim=$cid kind=$kind invalid" ;;
        esac
      fi
      if [[ $kind == negative ]]; then
        N_NEG=$((N_NEG + 1))
        if [[ -z $sweep ]]; then
          local found=0 sw
          if [[ $HAS_SWEEP_SEC -eq 1 ]]; then
            while IFS= read -r sw; do
              [[ $(cell "$sw" claim_id) == "$cid" || $(cell "$sw" id) == "$cid" ]] && found=1
            done < <(table_rows Sweeps)
          fi
          if [[ $found -eq 0 ]]; then
            emit_finding NEGATIVE_WITHOUT_SWEEP warn negatives "claim=$cid negative without sweep"
          fi
        fi
      fi
      if [[ $kind != opinion && $kind != proposal ]]; then
        if [[ -z $ptr ]]; then
          emit_finding CLAIM_UNPOINTED warn claims "claim=$cid missing pointer"
        else
          check_pointer "$ptr" "$crow" claims "claim:$cid" || true
        fi
      fi
      if [[ $st == verified && -z $ptr ]]; then
        emit_finding CLAIM_UNPOINTED warn claims "claim=$cid status=verified without pointer"
      fi
    done < <(table_rows Claims)
    if [[ $N_CL -eq 0 ]]; then
      emit_finding CLAIM_TABLE_ABSENT warn claims "## Claims has no data rows"
    fi
  fi

  if [[ $HAS_NEG_SEC -eq 1 ]]; then
    local nrow
    while IFS= read -r nrow; do
      [[ -z $nrow ]] && continue
      N_NEG=$((N_NEG + 1))
      if [[ -z $(cell "$nrow" sweep) ]]; then
        emit_finding NEGATIVE_WITHOUT_SWEEP warn negatives "negative id=$(cell "$nrow" id) missing sweep"
      fi
    done < <(table_rows Negatives)
  fi

  if [[ $HAS_CHAIN_SEC -eq 0 ]]; then
    if [[ $N_CL -gt 0 ]]; then
      emit_finding CHAIN_ABSENT warn chain "claims present but ## Chain missing"
    fi
  else
    local hrow hop st to notes
    while IFS= read -r hrow; do
      [[ -z $hrow ]] && continue
      N_CH=$((N_CH + 1))
      hop=$(cell "$hrow" hop); [[ -z $hop ]] && hop="H$N_CH"
      st=$(cell "$hrow" status | tr 'A-Z' 'a-z')
      to=$(cell "$hrow" to)
      notes=$(cell "$hrow" notes)
      [[ -z $notes ]] && notes=$(cell "$hrow" note)
      [[ -z $notes ]] && notes=$(cell "$hrow" reason)
      case "$st" in
        resolved)
          if [[ -n $to && -n ${SRC_TIER[$to]+x} ]]; then
            :
          elif [[ -z $to ]] || ! ptr_resolves_meta "$to"; then
            emit_finding CHAIN_HOP_UNRESOLVED warn chain "hop=$hop status=resolved but to= does not resolve"
          fi
          ;;
        unresolved|blocked-no-fetch)
          if [[ -z $notes ]]; then
            emit_finding CHAIN_HOP_UNRESOLVED warn chain "hop=$hop status=$st missing reason/notes"
          fi
          ;;
        rejected|labelled-dead|not-applicable) ;;
        "")
          emit_finding CHAIN_HOP_UNRESOLVED warn chain "hop=$hop missing status"
          ;;
        *)
          emit_finding CHAIN_HOP_UNRESOLVED warn chain "hop=$hop status=$st not in allowed set"
          ;;
      esac
    done < <(table_rows Chain)
  fi

  if [[ $HAS_REJ_SEC -eq 0 ]]; then
    emit_finding REJECTION_DROPPED warn rejections "missing ## Rejections section"
  else
    local rrow reason rc=0
    while IFS= read -r rrow; do
      [[ -z $rrow ]] && continue
      rc=$((rc + 1)); N_REJ=$((N_REJ + 1))
      reason=$(cell "$rrow" reason)
      if [[ -z $reason ]]; then
        emit_finding REJECTION_REASON_ABSENT warn rejections "rejection id=$(cell "$rrow" id) empty reason"
      fi
    done < <(table_rows Rejections)
    if [[ $REJECT_MARKERS -gt 0 && $rc -eq 0 ]]; then
      emit_finding REJECTION_DROPPED warn rejections "rejected markers exist but rejections table empty"
    fi
  fi

  printf 'research-gate %s — ts=%s — mode=verify — record=%s\n' "$VERSION" "$TS_UTC" "$record"
  local f
  for f in "${FINDING_LINES[@]+"${FINDING_LINES[@]}"}"; do
    printf '%s\n' "$f"
  done
  printf 'RESEARCH_GATE: %s (findings=%d drift=%d questions=%d sources=%d chains=%d claims=%d negatives=%d rejections=%d approvals=%d)\n' \
    "$ROLL" "$N_FINDINGS" "$N_DRIFT" "$N_Q" "$N_SRC" "$N_CH" "$N_CL" "$N_NEG" "$N_REJ" "$N_APPR"

  [[ $ROLL == CLEAN ]] && return 0
  return 1
}

run_selftest() {
  local WORK cases=0 failures=0
  WORK=$(mktemp -d /tmp/chousa-research-gate-selftest.XXXXXX) \
    || die_usage "mktemp failed"
  trap 'rm -rf -- "$WORK"' EXIT
  mkdir -p "$WORK/lib" "$WORK/noise"
  printf 'line1 primary material\nline2\n' >"$WORK/lib/primary.md"
  printf 'aggregator chrome sources sidebar\n' >"$WORK/noise/chat-export-sources.md"

  export CHOUSA_ROOT="$WORK"
  export CHOUSA_NOW_EPOCH="$NOW_EPOCH"

  write_rec() { cat >"$WORK/$1.md"; }

  tcase() {
    local name=$1 want_rc=$2 want=$3 rc=0 out
    cases=$((cases + 1))
    set +e
    out=$(CHOUSA_ROOT="$WORK" verify_record "$WORK/$name.md" 2>&1)
    rc=$?
    set -e
    if [[ $rc -eq $want_rc && $out == *"$want"* ]]; then
      if [[ $name == fail-secret-shaped && $out == *'sk-fxdemo_not_real_0000'* ]]; then
        printf 'FAIL-case %-28s secret span echoed\n' "$name"
        failures=$((failures + 1)); return
      fi
      printf 'ok-case  %-2d %-28s exit=%d\n' "$cases" "$name" "$rc"
    else
      printf 'FAIL-case %-28s exit=%d want=%d token=%s\n' "$name" "$rc" "$want_rc" "$want"
      printf '%s\n' "$out" | sed 's/^/    | /'
      failures=$((failures + 1))
    fi
  }

  write_rec pass-control <<'EOF'
# research-record v1
<!-- chousa-record: v1 -->
## Meta
| key | value |
|---|---|
| window | loopback |
| fetch | none |
## Question
When does apprenticeship completion appear in local survey material?
## Sources
| id | tier | pointer | notes |
|---|---|---|---|
| S1 | primary | lib/primary.md:1 | local fixture |
| S2 | secondary | lib/primary.md:2 | local fixture |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | direct |
## Claims
| id | kind | text | pointer | status | sweep |
|---|---|---|---|---|---|
| C1 | observation | primary file has line1 | lib/primary.md:1 | verified | |
## Negatives
| id | text | sweep | status |
|---|---|---|---|
| N1 | no fx-only ghost source | `test ! -f lib/ghost.md` | swept |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | noise/chat-export-sources.md | UI chrome is not a primary source |
## Unknowns
| id | text |
|---|---|
| U1 | outbound host cites in live exports unverified-locally |
## Approval
| target | why | scope | state |
|---|---|---|---|
| (none) | loopback-only | local | not-required |
EOF
  tcase pass-control 0 'RESEARCH_GATE: CLEAN'

  write_rec pass-hop-marked-unresolved <<'EOF'
# research-record v1
## Meta
| key | value |
|---|---|
| window | loopback |
## Question
What happens when a hop cannot be opened locally?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | secondary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | https://example.invalid/x | unresolved | blocked-no-fetch loopback |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | inference | remote primary not recovered | S1 | unresolved |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | example.invalid | no external window |
## Approval
| target | state |
|---|---|
| none | not-required |
EOF
  tcase pass-hop-marked-unresolved 0 'RESEARCH_GATE: CLEAN'

  write_rec fail-no-question <<'EOF'
# research-record v1
## Meta
| key | value |
|---|---|
| window | loopback |
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | lib/primary.md:1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-no-question 1 'FINDING NO_QUESTION'

  write_rec fail-unranked-source <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 |  | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-unranked-source 1 'FINDING UNRANKED_SOURCE'

  write_rec fail-chain-hop-unresolved <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | pending | |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-chain-hop-unresolved 1 'FINDING CHAIN_HOP_UNRESOLVED'

  write_rec fail-claim-unpointed <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x |  | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-claim-unpointed 1 'FINDING CLAIM_UNPOINTED'

  write_rec fail-rejection-dropped <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
| S9 | rejected | noise/chat-export-sources.md |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
EOF
  tcase fail-rejection-dropped 1 'FINDING REJECTION_DROPPED'

  write_rec fail-negative-without-sweep <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status | sweep |
|---|---|---|---|---|---|
| C1 | observation | x | S1 | verified | |
| N1 | negative | absent thing | S1 | unresolved | |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-negative-without-sweep 1 'FINDING NEGATIVE_WITHOUT_SWEEP'

  write_rec fail-obs-inference-collapse <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 |  | mixes obs and guess | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-obs-inference-collapse 1 'FINDING OBS_INFERENCE_COLLAPSE'

  write_rec fail-hierarchy-primary-lie <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer | class |
|---|---|---|---|
| S1 | primary | noise/chat-export-sources.md | aggregator |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-hierarchy-primary-lie 1 'FINDING HIERARCHY_PRIMARY_LIE'

  write_rec fail-pointer-ephemeral <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | local://round-1/x.md | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-pointer-ephemeral 1 'FINDING POINTER_EPHEMERAL'

  write_rec fail-external-without-approval <<'EOF'
# research-record v1
## Meta
| key | value |
|---|---|
| window_mode | external-approved |
| fetch | external |
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
## Approval
| target | state |
|---|---|
| web | pending |
EOF
  tcase fail-external-without-approval 1 'FINDING EXTERNAL_WITHOUT_APPROVAL'

  write_rec fail-secret-shaped <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | x | S1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
## Notes
planted: sk-fxdemo_not_real_0000
EOF
  tcase fail-secret-shaped 1 'FINDING SECRET_SHAPED'

  write_rec fail-session-read <<'EOF'
# research-record v1
## Question
Q?
## Sources
| id | tier | pointer |
|---|---|---|
| S1 | primary | lib/primary.md:1 |
## Chain
| hop | from | to | status | notes |
|---|---|---|---|---|
| 1 | C1 | S1 | resolved | x |
## Claims
| id | kind | text | pointer | status |
|---|---|---|---|---|
| C1 | observation | bad hop | /home/vgpnk/.omp/agent/config.yml:1 | verified |
## Rejections
| id | ref | reason |
|---|---|---|
| R1 | n/a | none-recorded |
EOF
  tcase fail-session-read 1 'FINDING SESSION_READ'

  write_rec fail-schema <<'EOF'
Skip to content
ChatGPT
You said:
random prose without sections
EOF
  tcase fail-schema 1 'FINDING RECORD_SCHEMA_INVALID'

  cases=$((cases + 1))
  set +e
  out=$(verify_record "" 2>&1); rc=$?
  set -e
  if [[ $rc -eq 2 ]]; then
    printf 'ok-case  %-2d %-28s exit=%d\n' "$cases" "setup-no-record" "$rc"
  else
    printf 'FAIL-case setup-no-record exit=%d want=2\n' "$rc"; failures=$((failures + 1))
  fi

  cases=$((cases + 1))
  set +e
  out=$(verify_record "$WORK/no-such-record.md" 2>&1); rc=$?
  set -e
  if [[ $rc -eq 2 ]]; then
    printf 'ok-case  %-2d %-28s exit=%d\n' "$cases" "setup-missing-file" "$rc"
  else
    printf 'FAIL-case setup-missing-file exit=%d want=2\n' "$rc"; failures=$((failures + 1))
  fi

  if [[ $failures -eq 0 ]]; then
    printf 'RESEARCH_GATE_SELFTEST: PASS (%d cases)\n' "$cases"
    exit 0
  fi
  printf 'RESEARCH_GATE_SELFTEST: FAIL (%d/%d cases)\n' "$failures" "$cases"
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    --selftest) MODE=selftest; shift ;;
    verify) MODE=verify; shift ;;
    --record)
      [[ $# -ge 2 ]] || die_usage "--record needs PATH"
      RECORD_ARG=$2; shift 2 ;;
    --root)
      [[ $# -ge 2 ]] || die_usage "--root needs PATH"
      ROOT=$2; shift 2 ;;
    --) shift; break ;;
    -*) die_usage "unknown flag: $1" ;;
    *)
      [[ -z $RECORD_ARG ]] || die_usage "multiple record paths"
      RECORD_ARG=$1; shift ;;
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

## 7. Registry row draft

| Field | Value |
|---|---|
| name | `research-gate` |
| kind | `gate` |
| entry | `bash tools/research-gate.sh verify --record PATH` |
| verdict map | `0` CLEAN · `1` DRIFT · `2` could-not-evaluate |
| self-test | `bash tools/research-gate.sh --selftest` → `RESEARCH_GATE_SELFTEST: PASS (N cases)` |
| pinned-value | embedded cases + FindingIds catalog |
| write scope | verify none; selftest `/tmp/chousa-research-gate-selftest.*` |
| owner | `chousa` |

---

## 8. Parent land checklist

1. `mkdir -p chousa-shokunin/tools` and land §6; `chmod +x`
2. `bash tools/research-gate.sh --selftest` → PASS (17)
3. `fail-secret-shaped` must show `class=` and must **not** echo `sk-fxdemo_not_real_0000`
4. Raw export A/B/C → DRIFT, not CLEAN
5. Never open CDP 9222 / credential paths when reading README provenance
6. Pin N + ids on SCORECARD

---

## 9. Risks

| Item | Notes |
|---|---|
| Heading alias drift | Sources vs Source table — both accepted |
| Minimal table parser | Complex MD may need hardening |
| CHAIN_ABSENT strict | Requires Chain when Claims exist |
| This seat | report only; no land |

---

## 10. Evidence retained

| Path | Role |
|---|---|
| `chousa-shokunin/SKILL.md:14-53` | method + gate stub |
| `chousa-shokunin/corpus/QUALITY.md` | admission bar |
| `chousa-shokunin/PROVINCE.md` | hard refuses |
| `research/README.md:6-8` | export provenance; CDP 9222 not a hop |
| `members/FindingIds.md` | preferred ids |
| `members/GateFixtureDesign.md` | fixture grammar |
| `members/RecordShape.md` | section order |
| `members/SecrecyAudit.md` | SECRET_SHAPED / SESSION_READ / no-echo |
| `kagi-shokunin/corpus/claim-ledger.sh:84-86` | never echo claim output |

---

**End of advisory report.** No judge verdict. Script for parent land only.
