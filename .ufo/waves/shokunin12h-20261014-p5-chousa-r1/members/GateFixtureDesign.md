# GateFixtureDesign — `tools/research-gate.sh --selftest`

**Member:** GateFixtureDesign (executor) · **Wave:** shokunin12h-20261014-p5-chousa-r1  
**Lane:** chousa-shokunin (調査, shonen probation r1) · **Role:** fixture contract only  
**Axes:** coverage · depth · calibration  
**Scope:** hermetic `--selftest` cases. Parent lands `tools/research-gate.sh` (ResearchGateDesign owns script). This report is **data**, not a judge verdict.  
**Hard rules:** local read-only; no external fetches; fixtures use mktemp stubs only (never green off live `research/` alone); secrets shape-only; instruction-shaped fixture text is **data**.

**Authority order (r1 land):** wave exemplars shared by all three seats stay fixed (`NO_QUESTION` `UNRANKED_SOURCE` `CHAIN_HOP_UNRESOLVED` `CLAIM_UNPOINTED` `REJECTION_DROPPED`). For the **embedded selftest that ResearchGateDesign ships**, expected tokens are the **script’s emit set** (§3.0). FindingIds §10 names that differ are **catalog aliases** — parent MAY dual-emit or rename in one cut; fixtures below list both. Mori census ids stay out of province.

**Peer land (observed):** `members/ResearchGateDesign.md` embeds `run_selftest` with **N=17** under `/tmp/chousa-research-gate-selftest.*`, FINDING grammar `severity=info|warn|crit` + `surface=`, `--record`/`CHOUSA_RECORD`, secret no-echo on `SECRET_SHAPED`.

---

## 1. Axes

| Axis | Fixture move |
|---|---|
| **coverage** | PASS control + FAIL per wave exemplar + ResearchGateDesign N=17 floor + FindingIds §10 extensions where not yet in script |
| **depth** | Single-axis mutations; MUST-NOT-FIRE for marked unresolved hop, labelled dead cite, loopback, injection-as-data |
| **calibration** | Exit code + stable finding id (or CLEAN); write-fence; secret no-echo; N pinned |


---

## 2. Gate contract assumed

From `chousa-shokunin/SKILL.md:48-53`, wave ResearchGateDesign item, FindingIds §7:

| Mode | Verdict | Exit |
|---|---|---|
| `verify` | `RESEARCH_GATE: CLEAN (…)` | **0** — no sev ∈ {warn,crit} (and no SECRET_SHAPED/SESSION_READ) |
| `verify` | `RESEARCH_GATE: DRIFT (findings=N …)` | **1** — each: `FINDING <ID> severity=<info\|warn\|crit> surface=<family> obs=<short>` |
| usage / missing path | setup/usage on stderr | **2** |
| `--selftest` | `RESEARCH_GATE_SELFTEST: PASS (N cases)` / `FAIL (fail/N)` | **0** / **1** |

```text
FINDING <ID> severity=<info|warn|crit> surface=<family> obs=<short>
```

FindingIds catalog severities `high`/`critical` map to emit `warn`/`crit` (ResearchGateDesign note: never bare `high` on the wire).


Invocations:

```text
bash tools/research-gate.sh verify --record PATH
bash tools/research-gate.sh verify PATH
CHOUSA_RECORD=PATH bash tools/research-gate.sh verify
bash tools/research-gate.sh --selftest
bash tools/research-gate.sh --help
```

**Write fence:** verify writes nothing. `--selftest` only under `mktemp -d /tmp/chousa-research-gate-selftest.XXXXXX`; after every case fixture sha256 digest unchanged (mori pattern: `mori-shokunin/tools/mori-census.sh` `fx_hash` / `fx_no_mutation`).  
**No network:** no curl/wget/DNS/CDP.

---

## 3. Finding ids — pins and crosswalk

### 3.0 ResearchGateDesign embedded suite (landed floor — N=17)

Exact case names and tokens from `members/ResearchGateDesign.md` `run_selftest` (parent cuts this into `tools/research-gate.sh`). **This is the r1 capability pin.**

| # | case id | exit | assert token |
|---|---|---|---|
| 1 | `pass-control` | 0 | `RESEARCH_GATE: CLEAN` |
| 2 | `pass-hop-marked-unresolved` | 0 | `RESEARCH_GATE: CLEAN` |
| 3 | `fail-no-question` | 1 | `FINDING NO_QUESTION` |
| 4 | `fail-unranked-source` | 1 | `FINDING UNRANKED_SOURCE` |
| 5 | `fail-chain-hop-unresolved` | 1 | `FINDING CHAIN_HOP_UNRESOLVED` |
| 6 | `fail-claim-unpointed` | 1 | `FINDING CLAIM_UNPOINTED` |
| 7 | `fail-rejection-dropped` | 1 | `FINDING REJECTION_DROPPED` |
| 8 | `fail-negative-without-sweep` | 1 | `FINDING NEGATIVE_WITHOUT_SWEEP` |
| 9 | `fail-obs-inference-collapse` | 1 | `FINDING OBS_INFERENCE_COLLAPSE` |
| 10 | `fail-hierarchy-primary-lie` | 1 | `FINDING HIERARCHY_PRIMARY_LIE` |
| 11 | `fail-pointer-ephemeral` | 1 | `FINDING POINTER_EPHEMERAL` |
| 12 | `fail-external-without-approval` | 1 | `FINDING EXTERNAL_WITHOUT_APPROVAL` |
| 13 | `fail-secret-shaped` | 1 | `FINDING SECRET_SHAPED` + obs has `class=` and **must not** contain planted secret span |
| 14 | `fail-session-read` | 1 | `FINDING SESSION_READ` |
| 15 | `fail-schema` | 1 | `FINDING RECORD_SCHEMA_INVALID` |
| 16 | `setup-no-record` | 2 | setup (no CLEAN/DRIFT required) |
| 17 | `setup-missing-file` | 2 | setup |

Wave exemplars ⊆ rows 3–7. Selftest workdir: `/tmp/chousa-research-gate-selftest.XXXXXX` only.

### 3.1 Normative wave exemplars (shared; must FAIL)

| ID | Emit sev | FIRE when |
|---|---|---|
| `NO_QUESTION` | crit | no non-empty `## Question` |
| `UNRANKED_SOURCE` | warn | source row missing/invalid tier |
| `CHAIN_HOP_UNRESOLVED` | warn | hop neither resolved nor marked unresolved/broken/labelled-dead with reason |
| `CLAIM_UNPOINTED` | warn | claim lacks pointer |
| `REJECTION_DROPPED` | warn | rejected candidate with no rejections row |

### 3.2 FindingIds §10 ↔ gate emit crosswalk

| FindingIds §10 / catalog | ResearchGateDesign emit (selftest assert) | Notes |
|---|---|---|
| `NO_QUESTION` | `NO_QUESTION` | identical |
| `UNRANKED_SOURCE` | `UNRANKED_SOURCE` | identical |
| `CHAIN_HOP_UNRESOLVED` | `CHAIN_HOP_UNRESOLVED` | identical |
| `CLAIM_UNPOINTED` | `CLAIM_UNPOINTED` | identical |
| `REJECTION_DROPPED` | `REJECTION_DROPPED` | identical |
| `REJECTION_REASON_ABSENT` | `REJECTION_REASON_ABSENT` | in gate id list; optional extra FAIL case |
| `NEGATIVE_SWEEP_ABSENT` | **`NEGATIVE_WITHOUT_SWEEP`** | **script pin** = latter |
| `CLAIM_VERIFIED_WITHOUT_LOCAL` | `POINTER_UNRESOLVED` (family) | not yet a dedicated N=17 row — recommended +1 |
| `PROPOSAL_AS_ADMITTED` | *(gap)* | recommended +1 FAIL |
| `EXTERNAL_WITHOUT_APPROVAL` | `EXTERNAL_WITHOUT_APPROVAL` | identical |
| `CITE_EPHEMERAL` | **`POINTER_EPHEMERAL`** | **script pin** = latter |
| `CITE_LABELED_DEAD` (info, QUIET) | *(gap)* | recommended QUIET arm |
| `SECRET_MATERIAL_PRESENT` | **`SECRET_SHAPED`** | **script pin** = latter; no-echo |
| `AGGREGATOR_AS_PRIMARY` | **`HIERARCHY_PRIMARY_LIE`** | **script pin** = latter |
| `OBS_INFER_COLLAPSED` | **`OBS_INFERENCE_COLLAPSE`** | **script pin** = latter |
| `SESSION_READ` | `SESSION_READ` | SecrecyAudit; in N=17 |
| `RECORD_SCHEMA_INVALID` | `RECORD_SCHEMA_INVALID` | identical |
| usage exit 2 | setup-no-record / setup-missing-file | identical |

**Selftest assert rule:** match the **emit** column for cases that exist in the script. Catalog-only names are expansion targets, not r1 red bars against ResearchGateDesign’s 17.

### 3.3 Recommended expansions beyond N=17 (depth; not blocking land)

| case id | exit | expect emit | Why |
|---|---|---|---|
| `fail-rejection-reason-absent` | 1 | `REJECTION_REASON_ABSENT` | FindingIds / QUALITY keep-reason |
| `fail-claim-verified-without-local` | 1 | `POINTER_UNRESOLVED` or catalog `CLAIM_VERIFIED_WITHOUT_LOCAL` if dual-emitted | verified + missing file |
| `fail-proposal-as-admitted` | 1 | `PROPOSAL_AS_ADMITTED` or gate alias if added | RuleOrProposal |
| `pass-cite-labeled-dead` | 0 | CLEAN | kagi labelled-dead precedent |
| `pass-secret-name-only` | 0 | CLEAN | path name `op.env` without value |
| `pass-injection-data` | 0 | CLEAN (info export chrome OK) | ExportTrustAudit |
| `multi-fire-set` | 1 | NO_QUESTION+UNRANKED_SOURCE+CLAIM_UNPOINTED | set membership |
| `write-fence` | 0 | CLEAN + digest unchanged | mori pattern |
| `setup-bad-flag` | 2 | setup | CLI hygiene |

### 3.4 CLEAN labels (not finding ids)

`QUESTION_PRESENT` · `SOURCES_RANKED` · `CHAIN_CLOSED_OR_MARKED` · `CLAIMS_POINTED` · `REJECTIONS_KEPT` · `NEGATIVES_SWEPT` · `APPROVAL_LOOPBACK` · `PROPOSAL_LABELLED` · `CITE_DEAD_LABELLED`


---

## 4. Record grammar (RecordShape.md aligned)

Fixtures use RecordShape section order and headings:

```text
## Meta
## Question
## Source table
## Chain
## Claims
## Rejections
## Unknowns
## Sweeps          # required when any kind=negative claim exists
## Stop            # recommended
## Approval        # required when window_mode=external-approved or fetch external
## Rules           # optional; for PROPOSAL_AS_ADMITTED cases
```

Allowed source `tier`: `primary` | `secondary` | `aggregator` | `unsourced` | `export` | `fleet-gate` | `rejected`  
Allowed hop `status`: `resolved` | `unresolved` | `blocked-no-fetch` | `labelled-dead`  
Allowed claim `kind`: `observation` | `inference` | `negative` | `opinion` | `proposal`  
Allowed claim `status`: `verified-local` | `unverified-locally` | `contradicted-local` | `open` | `verified`† | `unresolved`†  
† gate SHOULD accept SKILL short forms as aliases of `verified-local` / `unresolved`.

Machine-row alternate (if ResearchGateDesign emits `@question` / `@source` lines): fixtures MAY ship dual encoding; selftest preferred form is Markdown tables above. Parent picks one wire; this seat pins **Markdown RecordShape**.

---

## 5. Hermetic layout

```text
$WORK = mktemp -d /tmp/chousa-research-gate-selftest.XXXXXX
$WORK/fx/<case-id>/
  record.md
  lib/…                    # openable pointer targets
$WORK/home/                # empty HOME for env -i
```

| Env | Role |
|---|---|
| `CHOUSA_FIXTURE=1` | fixture mode; resolve only under `CHOUSA_ROOT` |
| `CHOUSA_ROOT=$FX` | pointer root |
| `CHOUSA_RECORD=$FX/record.md` | record path |
| `CHOUSA_STRICT=0` | info findings do not DRIFT |

`fx_lib` stubs (synthetic; mirror survey *structure*, not live bytes as authority):

| path | one-line body |
|---|---|
| `lib/research/README.md` | `Three GPT browse-exports; not Deep Research pipeline.` |
| `lib/research/A-stub.md` | `export chrome; Sources; Web search` |
| `lib/research/B-stub.md` | `bare arxiv.org token; no URL` |
| `lib/research/C-stub.md` | `rank taxonomy export stub` |
| `lib/fleet/kagi-claim-ledger-docs.md` | `EPHEMERAL local:// fails unless labelled` |
| `lib/fleet/kasegi-citation-bases.md` | `LANE path:line; lost-tree prefixes` |
| `lib/fleet/chousa-skill-gates.md` | `question; ranked sources; chain marked; claims pointed; rejections kept` |
| `lib/noise/chat-export-sources.md` | `Sources / Web search UI chrome` |
| `lib/noise/secondary-summary.md` | `summary only` |

---

## 6. Assertion primitive

```bash
# run_case NAME WANT_EXIT WANT_ID_OR_CLEAN [extra greps…]
run_case() {
  local name=$1 want_rc=$2 want=$3; shift 3
  local out rc before
  before=$(fx_hash "$FX")
  set +e
  out=$(env -i PATH="/usr/bin:/bin" HOME="$WORK/home" \
    CHOUSA_FIXTURE=1 CHOUSA_ROOT="$FX" CHOUSA_RECORD="$FX/record.md" \
    bash "$GATE" verify --record "$FX/record.md" 2>&1)
  rc=$?
  set -e
  cases=$((cases + 1))
  if [ "$rc" -ne "$want_rc" ]; then
    bad "$name: exit $rc want $want_rc"
  elif [ "$want" = CLEAN ]; then
    printf '%s\n' "$out" | grep -qE '^RESEARCH_GATE: CLEAN' \
      || bad "$name: missing CLEAN"
    if printf '%s\n' "$out" | grep -qE '^FINDING [^ ]+ severity=(warn|crit) '; then
      bad "$name: severity finding on CLEAN"
    fi

  else
    printf '%s\n' "$out" | grep -qE "^FINDING ${want} " \
      || bad "$name: missing FINDING $want"
    printf '%s\n' "$out" | grep -qE '^RESEARCH_GATE: DRIFT' \
      || bad "$name: missing DRIFT"
  fi
  for re in "$@"; do
    printf '%s\n' "$out" | grep -qE -- "$re" || bad "$name: missing /$re/"
  done
  fx_no_mutation "$FX" "$before"
}
Finding emission order for multi-fire pins: set membership unless GateDesign freezes sort.

**Hop / pointer resolve (SecrecyAudit + ResearchGateDesign):** existence is **`test -f` metadata only** under `CHOUSA_ROOT`. Fixtures MUST NOT require the gate to content-open hop targets or echo file bodies into FINDING obs. Denylist paths → `SESSION_READ` without open.


---

## 7. PASS control (`control-clean` / golden)

**Expect:** exit **0**, `RESEARCH_GATE: CLEAN`, zero warn/high/critical findings.

```markdown
# research-record v1
<!-- chousa-record: v1 -->

## Meta
record_id: RR-chousa-selftest-control
lane: chousa-shokunin
window_mode: loopback
approval_ref: none
as_of: 2026-10-14
operator: selftest

## Question
What citation forms appear in the 2026-09-28 deep-research chat-export artifacts,
and which method defects must a research gate catch before admitting rules?

## Source table
| src_id | path_or_token | tier | revision | role | local_openable | label |
|---|---|---|---|---|---|---|
| S1 | lib/research/A-stub.md:1 | export | stub | survey carrier A | yes | |
| S2 | lib/research/B-stub.md:1 | export | stub | survey carrier B | yes | |
| S3 | lib/research/C-stub.md:1 | export | stub | survey carrier C | yes | |
| S4 | lib/research/README.md:1 | secondary | stub | harvest index | yes | |
| S5 | lib/fleet/kagi-claim-ledger-docs.md:1 | fleet-gate | stub | ephemeral-cite precedent | yes | |
| S6 | lib/fleet/kasegi-citation-bases.md:1 | fleet-gate | stub | path:line base vocab | yes | |
| S7 | lib/noise/chat-export-sources.md:1 | aggregator | stub | UI Sources chrome | yes | |
| S8 | lib/noise/secondary-summary.md:1 | rejected | stub | rejected sole-primary candidate | yes | |
| S9 | lib/fleet/chousa-skill-gates.md:1 | primary | stub | method contract stub | yes | |

## Chain
| hop | from | to_token | status | local_evidence | note |
|---|---|---|---|---|---|
| 1 | C1 | S4 | resolved | lib/research/README.md:1 | index openable |
| 2 | C2 | S1 | resolved | lib/research/A-stub.md:1 | export carrier |
| 3 | C3 | S7 | unresolved | none | aggregator chrome not authority; reason kept |

## Claims
| claim_id | text | kind | points_to | status | depends_on | sweep_ref |
|---|---|---|---|---|---|---|
| C1 | Harvest README labels the three files as browse-exports, not Deep Research pipeline output. | observation | lib/research/README.md:1 | verified-local | 1 | |
| C2 | Artifact A stub retains export chrome including a Sources block. | observation | lib/research/A-stub.md:1 | verified-local | 2 | |
| C3 | Export Sources sidebars are not resolvable primary citations for method admission. | inference | lib/noise/chat-export-sources.md:1 | unverified-locally | 3 | |
| C4 | Whether underlying export URLs would resolve today is unknowable without a network window. | observation | lib/research/README.md:1 | open | | |
| C5 | No https URL tokens appear in the synthetic A/B/C stubs used by this control. | negative | lib/research/A-stub.md:1 | verified-local | | SW1 |

## Rejections
| rej_id | candidate | reason | anchor | kept |
|---|---|---|---|---|
| R1 | S8 as sole primary | secondary summary cannot alone ground an admitted primary-tier rule | lib/noise/secondary-summary.md:1 | yes |
| R2 | S7 as primary authority | chat-export Sources chrome is aggregator UI | lib/noise/chat-export-sources.md:1 | yes |

## Unknowns
| unk_id | text | would_need |
|---|---|---|
| U1 | Live burner-account entitlement at capture time | operator note or approval-window re-capture |

## Sweeps
| sweep_id | claim_ref | command | as_of | result_note |
|---|---|---|---|---|
| SW1 | C5 | `rg -c 'https://' lib/research/A-stub.md lib/research/B-stub.md lib/research/C-stub.md` | 2026-10-14 | expect 0 |

## Stop
loopback selftest control complete; no external targets.

## Approval
| target | why | scope | state |
|---|---|---|---|
| — | loopback only | $FX | not-required |

## Rules
| rule_id | status | text | evidence |
|---|---|---|---|
| RULE1 | admitted | Every admitted method rule cites a resolvable local pointer or is marked proposal. | lib/fleet/chousa-skill-gates.md:1 |
| RULE2 | proposal | Prefer monographs over workshop blogs when both exist. | |
```

---

## 8. Case table

**Legend:** FIRE = exit 1 + id. QUIET = exit 0 CLEAN. SETUP = exit 2.

### 8.0 Control & setup

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 0 | `control-clean` | 0 | CLEAN | none (golden) |
| 0b | `setup-no-record` | 2 | SETUP | `verify` with no record path |
| 0c | `setup-missing-file` | 2 | SETUP | `--record` absent path |
| 0d | `setup-bad-flag` | 2 | SETUP | `--not-a-flag` |
| 0e | `schema-empty-file` | 1 | `NO_QUESTION` | zero-byte `record.md` (readable path → content DRIFT; at least NO_QUESTION) |

### 8.1 Question

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 1 | `no-question-FIRE` | 1 | `NO_QUESTION` | empty/absent `## Question` body |
| 2 | `question-present-QUIET` | 0 | CLEAN | control |

### 8.2 Sources

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 3 | `unranked-source-FIRE` | 1 | `UNRANKED_SOURCE` | S2 tier emptied |
| 4 | `bad-tier-token-FIRE` | 1 | `UNRANKED_SOURCE` | S2 tier=`hero-source` |
| 5 | `sources-ranked-QUIET` | 0 | CLEAN | control |
| 5b | `source-table-absent-FIRE` | 1 | `SOURCE_TABLE_ABSENT` | remove `## Source table`; keep claims |

### 8.3 Chain

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 6 | `chain-hop-silent-FIRE` | 1 | `CHAIN_HOP_UNRESOLVED` | hop 3 status emptied (silent break) |
| 7 | `chain-hop-false-resolved-FIRE` | 1 | `CHAIN_HOP_UNRESOLVED` | status=`resolved`, `local_evidence=lib/missing.md:1` |
| 8 | `chain-hop-marked-QUIET` | 0 | CLEAN | control hop 3 stays `unresolved` **with** note/reason |
| 9 | `chain-absent-multi-FIRE` | 1 | `CHAIN_HOP_UNRESOLVED` or `CHAIN_ABSENT` | remove `## Chain` while multi-hop claims remain; **at least one** of these ids MUST appear (pin primary `CHAIN_HOP_UNRESOLVED` if only one emitted) |

### 8.4 Claims / pointers / cites

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 10 | `claim-unpointed-FIRE` | 1 | `CLAIM_UNPOINTED` | C1 `points_to` emptied |
| 11 | `claim-verified-without-local-FIRE` | 1 | `POINTER_UNRESOLVED` | C1 status=`verified-local`, points_to=`lib/no-such.md:1` (catalog alias `CLAIM_VERIFIED_WITHOUT_LOCAL`) |
| 12 | `cite-unresolved-FIRE` | 1 | `POINTER_UNRESOLVED` | add unlabeled dead path `lib/gone.md:1` (catalog `CITE_UNRESOLVED_LOCAL`) |
| 13 | `cite-ephemeral-FIRE` | 1 | `POINTER_EPHEMERAL` | points_to=`local://round-10/critic.md` unlabeled (catalog `CITE_EPHEMERAL`) |
| 14 | `cite-labeled-dead-QUIET` | 0 | CLEAN | dead token with `historical`/`ephemeral`/`formerly` marker |
| 15 | `claims-pointed-QUIET` | 0 | CLEAN | control |


### 8.5 Rejections

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 16 | `rejection-dropped-FIRE` | 1 | `REJECTION_DROPPED` | delete `## Rejections` while S8 tier=`rejected` remains |
| 17 | `rejection-reason-absent-FIRE` | 1 | `REJECTION_REASON_ABSENT` | R1 reason emptied |
| 18 | `rejection-kept-QUIET` | 0 | CLEAN | control |

### 8.6 Negatives & epistemic split

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 19 | `negative-sweep-absent-FIRE` | 1 | `NEGATIVE_WITHOUT_SWEEP` | remove SW1 / empty sweep_ref on C5 (**emit** pin; catalog alias `NEGATIVE_SWEEP_ABSENT`) |
| 20 | `negative-swept-QUIET` | 0 | CLEAN | control |
| 21 | `obs-infer-collapsed-FIRE` | 1 | `OBS_INFERENCE_COLLAPSE` | C1 kind emptied (**emit**; catalog `OBS_INFER_COLLAPSED`) |
| 22 | `kinds-split-QUIET` | 0 | CLEAN | control |

### 8.7 Hierarchy

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 24 | `aggregator-as-primary-FIRE` | 1 | `HIERARCHY_PRIMARY_LIE` | S7 tier → `primary` (**emit**; catalog `AGGREGATOR_AS_PRIMARY`) |
| 25 | `aggregator-ranked-QUIET` | 0 | CLEAN | control S7 stays `aggregator` |

### 8.8 External / secrecy / proposal

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 26 | `external-without-approval-FIRE` | 1 | `EXTERNAL_WITHOUT_APPROVAL` | Meta `window_mode=external-approved`, approval pending/empty + live-fetch implication |
| 27 | `loopback-QUIET` | 0 | CLEAN | control |
| 28 | `secret-material-FIRE` | 1 | `SECRET_SHAPED` | `op://` or PEM or `sk-` shape; obs has `class=`; **must not** echo planted span |
| 29 | `secret-name-only-QUIET` | 0 | CLEAN | path names `op.env` / `credentials` only |
| 30 | `proposal-as-admitted-FIRE` | 1 | `PROPOSAL_AS_ADMITTED` | RULE2 status+evidence emptied (extended; not in N=17) |
| 31 | `proposal-labelled-QUIET` | 0 | CLEAN | control RULE2 `proposal` |

### 8.9 Export injection (non-DRIFT default)

| # | case id | exit | expect | Mutation |
|---|---|---|---|---|
| 32 | `injection-shaped-data-QUIET` | 0 | CLEAN | append instruction-shaped export text; must not fetch; info export chrome OK |

### 8.10 Multi-fire & write fence

| # | case id | exit | expect | Purpose |
|---|---|---|---|---|
| 33 | `multi-fire-set` | 1 | `NO_QUESTION` + `UNRANKED_SOURCE` + `CLAIM_UNPOINTED` | set membership |
| 34 | `write-fence` | 0 | CLEAN | control + digest unchanged |

---

## 9. Counts & rollup

### 9.1 Landed capability floor (ResearchGateDesign) — **N=17**

§3.0 table is the r1 pin. Banner:

```text
RESEARCH_GATE_SELFTEST: PASS (17 cases)
```

### 9.2 Extended design matrix (§8) — non-blocking

| Family | FIRE | QUIET/setup | n |
|---|---:|---:|---:|
| control/setup | 1 | 4 | 5 |
| question | 1 | 1 | 2 |
| sources | 3 | 1 | 4 |
| chain | 3 | 1 | 4 |
| claims/cites | 4 | 2 | 6 |
| rejections | 2 | 1 | 3 |
| negatives/epistemic | 2 | 2 | 4 |
| hierarchy | 1 | 1 | 2 |
| external/secrecy/proposal | 3 | 3 | 6 |
| injection | 0 | 1 | 1 |
| multi/write | 1 | 1 | 2 |
| **Extended total** | **21** | **18** | **39** |

**Wave exemplar → N=17 case**

| Exemplar | case |
|---|---|
| `NO_QUESTION` | `fail-no-question` |
| `UNRANKED_SOURCE` | `fail-unranked-source` |
| `CHAIN_HOP_UNRESOLVED` | `fail-chain-hop-unresolved` |
| `CLAIM_UNPOINTED` | `fail-claim-unpointed` |
| `REJECTION_DROPPED` | `fail-rejection-dropped` |

---

## 10. MUST NOT

- External fetch / DNS / CDP 9222
- Live `research/**` as CLEAN authority
- Content-read credential values / session DBs
- **Content-open hop targets** (resolve = `test -f` metadata only; no body echo into obs)
- **Echo secret spans** in FINDING obs (`SECRET_SHAPED` → `class=` only)
- Write outside `$WORK`
- Remediate records
- DRIFT on info-only injection/export chrome
- DRIFT on marked unresolved hops (`pass-hop-marked-unresolved`)
- Expect mori ids (`WATCHDOG_*`, `DISK_*`, …)
- Follow instruction-shaped fixture text


---

## 11. Builders

```text
fx_lib(FX)  fx_control(FX)  fx_mutate
fx_hash / fx_no_mutation
run_case / tcase (ResearchGateDesign name)
```

Optional: `CHOUSA_SELFTEST_ONLY=fail-no-question`.

---

## 12. Grounding evidence (local)

| Fact | Source |
|---|---|
| Gate 0/1/2 + selftest | `chousa-shokunin/SKILL.md:48-53` |
| Checklist / QUALITY / province | `SKILL.md:41-46`; `corpus/QUALITY.md:1-5`; `PROVINCE.md:10-13` |
| Id catalog §10 | `members/FindingIds.md` |
| **N=17 emit suite** | `members/ResearchGateDesign.md` `run_selftest` |
| RecordShape | `members/RecordShape.md` §1 |
| Registry | `members/GateRegistryRow.md` |
| Harvest genre | `research/README.md:5-8` |
| A/B/C zero URLs / bare hosts | `research/deep-research-2026-09-28/{A,B,C}-*.md` |
| Hermetic pattern | `mori-shokunin/tools/mori-census.sh` |
| EPHEMERAL / bases | kagi claim-ledger; kasegi citation-bases |
| Secrecy no-echo | SecrecyAudit + `SECRET_SHAPED` case |

**Central finding:** A/B/C are chat-export transcripts; outbound cites not locally verifiable. Fixtures detect method defects; do not admit export chrome as primary.

---

## 13. Hand-off

| Owner | Owes |
|---|---|
| **ResearchGateDesign** | N=17 script in member report — **observed** |
| **FindingIds** | Catalog; optional dual-emit of §10 aliases |
| **RecordShape** | Headings; gate maps `Source table`↔`Sources` |
| **ChainHopFixture** | `fail-chain-hop-unresolved` / `pass-hop-marked-unresolved` |
| **GateRegistryRow** | Pin **N=17** at lane land |
| **Parent** | Cut to `chousa-shokunin/tools/research-gate.sh`; `--selftest` → PASS (17) |

---

## 14. Risks

| Risk | Mitigation |
|---|---|
| Catalog ≠ emit spelling | §3.2; **assert emit column** for r1 |
| `NEGATIVE_SWEEP_ABSENT` vs `NEGATIVE_WITHOUT_SWEEP` | pin **emit** |
| `SECRET_MATERIAL_PRESENT` vs `SECRET_SHAPED` | pin **`SECRET_SHAPED`** + no-echo |
| `CITE_EPHEMERAL` vs `POINTER_EPHEMERAL` | pin **`POINTER_EPHEMERAL`** |
| `AGGREGATOR_AS_PRIMARY` vs `HIERARCHY_PRIMARY_LIE` | pin **`HIERARCHY_PRIMARY_LIE`** |
| Multi-fire order | set membership |

**Blockers:** none for this seat. Parent cutover remains.

---

## 15. Summary

1. **r1 floor N=17** (§3.0) — PASS×2, FAIL×12 (all five wave exemplars), setup×2; each asserts exit + FINDING id / CLEAN; `SECRET_SHAPED` no-echo.  
2. **Crosswalk** FindingIds §10 ↔ gate emit (§3.2).  
3. **Extended ~39** cases (§8) for depth — non-blocking.  
4. RecordShape grammar; mktemp-only; no network; injection = data.  
5. Survey exports stated as unverified carriers, not primaries.

---

## 16. Files / evidence

| Path | Action |
|---|---|
| `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/GateFixtureDesign.md` | **written** (N=17 align + crosswalk) |

No lane `tools/` edit. No network. No judge verdict.

