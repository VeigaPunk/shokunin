# FindingIds — chousa stable finding-id vocabulary (r1 contract)

**Lane:** chousa-shokunin (調査) — deep-research *method*; detect and report only on a research record.
**Role of this document:** the compare contract a later `tools/research-gate.sh` run diffs against; GateFixtureDesign / ResearchGateDesign consume these ids.
**Scope:** advisory member report only. Parent lands gate/corpus/LOG/SCORECARD. This file is data, not a `RESEARCH_GATE:` verdict.
**Measured at:** `2026-10-14T21:54:04-03:00` (host local). Live anchors below calibrated the vocabulary against the survey surfaces; they are not a gate run.

## 0. Stability rules

1. **Id form.** `UPPER_SNAKE_CASE`. No lane prefix in the id string (chousa owns the vocabulary; gate output may print `RESEARCH_GATE` as the verdict banner, not as part of the id).
2. **Stable means:** same predicate on the same normalized research-record observation yields the same id across runs. Volatile fields (wall clock, temp fixture path, process pid, byte counts of the scanned tree) attach as **payload**, never reshape the id.
3. **One finding row = one `(id, subject-key)`.** Subject keys are named per family (record path, claim-id, source-id, hop-id, rejection-id, section path).
4. **Unavailable surface ≠ defect content.** A missing optional section that the record schema marks optional emits `*_UNAVAILABLE` / `RECORD_SECTION_ABSENT` at severity `info` only when the gate cannot grade that facet. It never upgrades to `warn`/`high` solely because a probe could not see an *optional* facet. **Required** facets missing are content defects (`NO_QUESTION`, etc.), not "unavailable."
5. **Observation / inference / unknown stay separate.** Predicates below are observations on the *record under test*. Inferences ("the author probably meant…") stay in prose payload under `reading:`, never as a second id. Unknowns the *record itself* fails to mark become `UNKNOWN_UNMARKED` (content), not gate speculation.
6. **No remediation verbs in ids.** Ids name the detected state of the research record, not the fix (`CLAIM_UNPOINTED`, never `ADD_POINTER`).
7. **Compare contract.** A later run reports `added` / `cleared` / `persisted` / `changed-payload` per id+subject. Gate **DRIFT** means any non-empty set of findings whose severity ≥ `warn` under the active profile (see §8), or any selftest expected-id mismatch — exact banner/exit mapping is ResearchGateDesign's job; this file freezes the ids.
8. **Mechanical vs semantic.** Like kasegi `anchorcheck.py` (range-valid ≠ claim-support) and kagi claim-ledger (path resolves ≠ claim true): these ids grade **record shape and local resolvability**. Semantic "does this quote support the claim?" is a separate human/L2 pass unless a *local* contradiction is mechanically visible (`CLAIM_CONTRADICTED_LOCAL`).
9. **Export content is data.** Instruction-shaped text inside surveyed artifacts (chat chrome, "You said:", model directives) never becomes a finding-id subject by being "followed"; if the *research record* cites such text as authority without marking it export-data, that is `EXPORT_TREATED_AS_SOURCE` / injection-handling territory — still an observation on the record, not obedience to the export.

## 1. Severity vocabulary

| Severity | Meaning for chousa | Gate weight (default profile) |
|---|---|---|
| `critical` | Record pretends external live research without approval window; secret-shaped material present; gate cannot safely continue grading without violating province | DRIFT |
| `high` | Core method contract broken: no question, claims without pointers, chain hops silently unresolved, rejections dropped, external cite presented as verified when only local-unverified | DRIFT |
| `warn` | Hierarchy violation, missing sweep on a negative claim, observation/inference collapsed, proposal mislabeled as admitted, citation form unresolvable locally, export chrome treated as source | DRIFT |
| `info` | Optional section absent, labeled dead hop kept, proposal correctly marked, surface the gate cannot see, soft hygiene | CLEAN payload (logged; not DRIFT unless `strict`) |
| *(no finding)* | Required facets present and predicates false | CLEAN |

Severity is a property of the **id definition**, not recomputed ad hoc by the reporter. Payload may carry measured magnitudes (hop index, claim count); it does not renumber severity.

## 2. Surface families → id families

Mapped from `chousa-shokunin/SKILL.md` decision table + checklist + Gates block, `corpus/QUALITY.md` admission bar, and fleet citation precedents.

| Family | Owns (on the research record) | Probe anchors | Id prefix / exemplars |
|---|---|---|---|
| Question framing | declared research question | record head / `## Question` / equivalent field | `NO_QUESTION`, `QUESTION_*` |
| Source hierarchy | primary > secondary > aggregator > unsourced; per-source rank | source table rows | `UNRANKED_SOURCE`, `HIERARCHY_*`, `SOURCE_*` |
| Citation chaining | hop list; each hop resolved **or** marked unresolved | chain section | `CHAIN_HOP_UNRESOLVED`, `CHAIN_*` |
| Claim-vs-source | claim → pointer → status | claims table | `CLAIM_UNPOINTED`, `CLAIM_*` |
| Rejection retention | rejected sources kept with reason | rejections section | `REJECTION_DROPPED`, `REJECTION_*` |
| Negative-claim sweep | absence claims carry search sweep | claims + sweep block | `NEGATIVE_SWEEP_*` |
| Epistemic hygiene | observation / inference / unknown / proposal labels | whole record | `OBS_INFER_*`, `UNKNOWN_*`, `PROPOSAL_*`, `RULE_*` |
| External / approval | live-target window; approval table | record meta + approval rows | `EXTERNAL_*`, `APPROVAL_*` |
| Citation form / pointer | path:line, stamp, labeled-dead, ephemeral URI | cite tokens | `CITE_*`, `POINTER_*` (aligned with kagi/kasegi classes, chousa-owned names) |
| Export / injection | chat-export treated as instruction or as primary | provenance fields | `EXPORT_*` |
| Secrecy | credential/session material | whole record + paths touched | `SECRET_*` |
| Record shape / meta | required sections, schema, selftest | gate internals | `RECORD_*`, `GATE_*`, `SELFTEST_*` |

## 3. Finding-id catalog

Each row: **id**, severity, surface, subject key, observation predicate that **produces** the finding, and what is **not** this finding.

### 3.1 Question framing

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `NO_QUESTION` | `high` | record head | `record=<path>` | No declarative research question is present (no `## Question` / `question:` / equivalent required field, or field empty/whitespace-only) | Question present but vague → `QUESTION_UNFALSIFIABLE` if it cannot be checked; multi-question blob without primary → `QUESTION_UNSCOPED` |
| `QUESTION_UNSCOPED` | `warn` | question field | `record=<path>` | Question field lists multiple independent inquiries with no declared primary / stop condition | Single scoped question |
| `QUESTION_UNFALSIFIABLE` | `warn` | question field | `record=<path>` | Question is pure preference/metaphor with no observable stop criterion and not labeled `opinion` | Labeled opinion; or operational "what does local artifact X say about Y" |
| `QUESTION_SECTION_UNAVAILABLE` | `info` | schema | `record=<path>` | Gate profile marks question optional (should not be default for chousa) and section missing | Default profile: missing question is `NO_QUESTION`, not unavailable |

**Exemplar (prompt):** `NO_QUESTION` is normative.

**Live calibration (observation, not verdict):** the three survey exports embed the operator prompt under `You said:` (`research/deep-research-2026-09-28/A-shokunin-tradition.md:35`, `B-…:35`, `C-…:35`) but are **chat transcripts**, not chousa research records. A gate run over those files as-if-records would fire `NO_QUESTION` on record-shape grounds **and** `EXPORT_CHROME_PRESENT` / provenance ids — unless a wrapping record declares the export as *survey material* with an explicit question. `research/README.md:1-17` states provenance of the harvest; it is an index, not a method record.

### 3.2 Source hierarchy

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `UNRANKED_SOURCE` | `high` | source table | `record=…;source=<id\|row>` | A cited/used source row has no rank tier in `{primary, secondary, aggregator, unsourced}` (or lane-declared equivalent) | Rank present even if wrong → `HIERARCHY_MISLABEL` |
| `HIERARCHY_MISLABEL` | `warn` | source table | `source=<id>` | Rank present but contradicts local evidence class (e.g. bare host label `arxiv.org` / `コトバンク` marked `primary` while only an export mention exists locally) | Unranked |
| `AGGREGATOR_AS_PRIMARY` | `warn` | source table | `source=<id>` | SKILL error pattern: aggregator quoted as primary (`chousa-shokunin/SKILL.md` error table) — tier `primary` on a row whose own type is aggregator/summary | Correctly tiered aggregator |
| `SOURCE_TABLE_ABSENT` | `high` | record | `record=<path>` | Record makes claims or cites material but has no source table/section at all | Empty table with explicit "no sources yet" + `UNKNOWN` markers may be `info` under draft profile; default: high if any claim exists |
| `SOURCE_UNSOURCED_CLAIM_ROW` | `warn` | source table | `source=<id>` | Row tier is `unsourced` but the row is still used to support a verified-status claim | Unsourced row only listed under rejections or unknowns |
| `SOURCE_DUPLICATE_ID` | `warn` | source table | `source=<id>` | Two source rows share the same stable source-id | Distinct ids |

**Exemplar:** `UNRANKED_SOURCE`.

**Live calibration:** A/B/C cite via bare host fragments (`A:68-72` `コトバンク`, `A:83` `adachi-hanga.com`, `B:51,72` `arxiv.org`, `C:82,90,100` nihonkiin/kotobank) with **no** resolvable path:line inside the export and **no** rank column — as research *content* this is the defect class the hierarchy rule targets; the gate grades a *record* that must re-state those sources with ranks.

### 3.3 Citation chaining

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `CHAIN_HOP_UNRESOLVED` | `high` | chain | `record=…;hop=<n\|id>` | A hop is neither (a) resolved to a local artifact pointer the gate can open, nor (b) explicitly marked `unresolved` / `broken` / labeled-dead with reason | Hop marked unresolved with reason → no finding (or `info` `CHAIN_HOP_MARKED_UNRESOLVED` for census only if profile wants positive marks) |
| `CHAIN_HOP_MARKED_UNRESOLVED` | `info` | chain | `hop=<id>` | Hop explicitly marked unresolved **with** reason — compare-fodder, default not DRIFT | Silent break → `CHAIN_HOP_UNRESOLVED` |
| `CHAIN_ABSENT` | `high` | record | `record=<path>` | Record asserts multi-hop dependence ("X cites Y cites Z") or lists transitive support but has no chain section | Single-hop direct claim-with-pointer only (chain optional) |
| `CHAIN_DEAD_LINK_SILENT` | `high` | chain | `hop=<id>` | SKILL pattern "chain ends at a dead link" without recording the hop — same family as `CHAIN_HOP_UNRESOLVED`; prefer this id when the hop target is explicitly a URL/path that fails local resolve and no mark exists | Marked dead |
| `CHAIN_SKIP_HOP` | `warn` | chain | `hop=<id>` | Chain jumps from hop *n* to *n+2* without stating the middle hop was out of scope | Contiguous hops or explicit skip reason |
| `CHAIN_STOP_WITHOUT_REASON` | `warn` | chain | `chain=<id>` | Chain terminates before a primary while stop rule / reason absent | Stop reason present (`loopback-only`, `approval-pending`, `marked-unresolved`) |

**Exemplar:** `CHAIN_HOP_UNRESOLVED`.

**Live calibration:** Export "Sources: Web search" chrome (`A:109-110`, `B:100-101`, `C:154-155`) is not a hop list. A reconstructed chain from claim → `arxiv.org` bare token has no openable local target → any record that copies that form without `unresolved` marks must fire `CHAIN_HOP_UNRESOLVED` (and usually `CITE_UNRESOLVED_LOCAL`).

### 3.4 Claim-vs-source

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `CLAIM_UNPOINTED` | `high` | claims | `record=…;claim=<id>` | Claim row lacks a resolvable pointer (artifact path, path:line, stamp id, evidence id, or explicitly `unverified-local`) | Pointer present but broken → `CITE_UNRESOLVED_LOCAL` / `POINTER_STALE`; status missing → `CLAIM_STATUS_ABSENT` |
| `CLAIM_STATUS_ABSENT` | `warn` | claims | `claim=<id>` | No verification status in `{verified, contradicted, unresolved, unverifiable-locally, opinion, proposal}` | Status present |
| `CLAIM_STATUS_INVALID` | `warn` | claims | `claim=<id>` | Status token not in the allowed set | — |
| `CLAIM_VERIFIED_WITHOUT_LOCAL` | `high` | claims | `claim=<id>` | Status is `verified` but pointer does not resolve locally **or** no quoted span is present for local check | `verified` with local path:line + span; or status is `unverifiable-locally` |
| `CLAIM_CONTRADICTED_LOCAL` | `high` | claims | `claim=<id>` | Local material at the pointer **directly** contradicts the claim text (mechanical string/section mismatch the gate is written to detect) | Mere absence of support → `CLAIM_UNPOINTED` or status should be `unresolved` |
| `CLAIM_TABLE_ABSENT` | `high` | record | `record=<path>` | Record body asserts factual findings but has no claims section/table | Pure method/process note with zero factual claims (rare; must declare `claims: none`) |
| `CLAIM_OPINION_UNMARKED` | `warn` | claims | `claim=<id>` | QUALITY.md bar: non-falsifiable preference not marked `opinion` | Marked opinion |
| `CLAIM_AVERAGE_OF_DISAGREE` | `warn` | claims | `claim=<id>` | SKILL pattern: two sources disagree and the claim averages/merges them into one asserted fact without reporting both | Both sides reported as separate claims or one rejection |

**Exemplar:** `CLAIM_UNPOINTED`.

**Checklist anchors:** `chousa-shokunin/SKILL.md` checklist "Every claim carries a resolvable pointer"; `corpus/QUALITY.md:3-4`.

### 3.5 Rejection retention

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `REJECTION_DROPPED` | `high` | rejections | `record=…;rejection=<id\|hash>` | Body or chain shows a source/candidate was considered and discarded, but rejections section lacks that entry **or** entry lacks reason | Rejection present with reason |
| `REJECTION_REASON_ABSENT` | `high` | rejections | `rejection=<id>` | Rejection row exists but reason empty | Reason non-empty |
| `REJECTION_SECTION_ABSENT` | `warn` | record | `record=<path>` | Record has ≥1 negative disposition in prose ("I could not substantiate…") and no rejections section | All negatives are formal rejection rows; or record explicitly `rejections: none` after a documented empty sweep |
| `REJECTION_SILENT_OVERWRITE` | `high` | rejections | `rejection=<id>` | Errata/append-only bar violated: a prior rejection removed or reason rewritten in place without append-only errata block | Append-only errata |

**Exemplar:** `REJECTION_DROPPED`.

**Live calibration:** A:47 and C:53,109 state negative findings ("haven't found evidence that jin'i-ryū…", "no authoritative attestation…"). A proper research record must keep those as rejection/negative-claim rows with sweeps — silence in a derived corpus note would be `REJECTION_DROPPED` / `NEGATIVE_SWEEP_ABSENT`.

### 3.6 Negative-claim sweep

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `NEGATIVE_SWEEP_ABSENT` | `high` | claims/sweep | `claim=<id>` | Claim is negative/absence ("no attestation of X") without a sweep block (what was searched, where, as-of stamp, local commands) | Sweep present |
| `NEGATIVE_SWEEP_EMPTY` | `warn` | sweep | `claim=<id>` | Sweep header present but zero commands/paths listed | Non-empty sweep |
| `NEGATIVE_SWEEP_UNRUNNABLE` | `warn` | sweep | `claim=<id>;cmd=<n>` | Sweep lists only external-network commands while record is loopback-only / no approval — and does not mark them `blocked-external` | Commands local-runnable or explicitly `blocked-external` |
| `NEGATIVE_SWEEP_NO_ASOF` | `info` | sweep | `claim=<id>` | Sweep lacks as-of timestamp/revision | Stamp present |

**SKILL / QUALITY anchors:** "A negative claim carries its search sweep"; QUALITY rejection kept.

### 3.7 Epistemic hygiene (observation / inference / unknown / proposal)

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `OBS_INFER_COLLAPSED` | `warn` | record body | `record=…;span=<loc>` | A sentence/section mixes raw observation and inference without labels, where the schema requires separation (e.g. labeled blocks or column `kind=`) | Separated; or free prose method essay under draft profile with explicit disclaimer |
| `UNKNOWN_UNMARKED` | `warn` | record | `span=<loc>` | Text acknowledges ignorance ("unknowable locally") but no `unknowns` entry | Listed under unknowns |
| `UNKNOWNS_SECTION_ABSENT` | `info` | record | `record=<path>` | Optional unknowns section missing and no unknown-shaped claims detected | — |
| `PROPOSAL_AS_ADMITTED` | `warn` | rules/claims | `rule=<id>` | Statement needs external source or lacks local path:line anchor but is not marked `proposal` (wave rule: admitted rule cites local artifact or is `proposal`) | Marked `proposal`; or carries path:line |
| `PROPOSAL_UNFALSIFIABLE` | `info` | proposal | `rule=<id>` | Proposal lacks stated falsification condition (SearchStrategyTaxonomy peer may require) | Falsification present |
| `RULE_EVIDENCE_MISSING` | `warn` | rules | `rule=<id>` | Rule claims an anchor that is empty, non-resolving, or points outside declared bases without label | Anchor resolves |
| `ERRATA_NOT_APPEND_ONLY` | `high` | errata | `record=<path>` | QUALITY.md:4 violated — errata edited destructive history | Append-only blocks |

### 3.8 External window / approval

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `EXTERNAL_WITHOUT_APPROVAL` | `critical` | meta | `record=<path>` | Record reports live external fetch / non-loopback research while approval state is missing, `pending`, or `denied` | Approval `granted` with scope covering the target; or pure loopback/local |
| `EXTERNAL_SCOPE_EXCEEDED` | `critical` | approval | `target=<id>` | Fetch/target outside the approved scope limit column | Inside scope |
| `APPROVAL_TABLE_ABSENT` | `warn` | record | `record=<path>` | Record plans or references a future external window but has no approval table (SKILL: approval table is itself a deliverable) | Loopback-only record that never mentions external |
| `APPROVAL_STATE_INVALID` | `warn` | approval | `row=<id>` | Approval state not in `{pending, granted, denied, expired, withdrawn}` | Valid state |
| `LIVE_FETCH_IN_LOOPBACK` | `critical` | meta/commands | `record=<path>` | Sweep or method lists executed `curl`/`wget`/browser fetch against non-loopback while mode is loopback-only | Documented blocked commands |

**Province anchors:** `chousa-shokunin/PROVINCE.md:10-12`; `SKILL.md` Boundaries.

### 3.9 Citation form / pointer resolvability

Aligns with fleet evidence without stealing kagi/kasegi id strings (lane-owned vocabulary; precedents are behavioral).

| id | sev | surface | subject | Produces when | Not this id when | Fleet precedent (behavior) |
|---|---|---|---|---|---|---|
| `CITE_UNRESOLVED_LOCAL` | `high` | cite token | `record=…;cite=<token>` | Citation token does not resolve under declared local bases | Resolves; or line labeled dead/historical/ephemeral-marked per policy | kagi `UNRESOLVED` → fail unless labeled (`claim-ledger.sh` citations mode) |
| `CITE_EPHEMERAL` | `high` | cite token | `cite=<token>` | Token is session-scoped (`local://`, `artifact://`, `agent://`, `proc://`) without durable restatement | Durable path/stamp | kagi `EPHEMERAL` |
| `CITE_LABELED_DEAD` | `info` | cite token | `cite=<token>` | Dead cite correctly labeled on the citing line (scratch\|ephemeral\|formerly\|historical\|removed\|…) | Unlabeled dead → `CITE_UNRESOLVED_LOCAL` | kagi labeled stale counted not failed |
| `CITE_FORM_BARE_HOST` | `warn` | cite token | `cite=<token>` | Cite is bare host/label (`arxiv.org`, `コトバンク`) with no path, id, or URL path usable locally | Full URL path + local capture; or marked unresolved hop | survey A/B/C forms |
| `CITE_FORM_BARE_TITLE` | `warn` | cite token | `cite=<token>` | Title-only bibliographic mention used as support pointer | Tied to resolvable artifact |
| `POINTER_STALE` | `warn` | pointer | `claim=<id>;path=` | Stamp/sha/line pin no longer matches file (stamp verify fail) | Stamp OK | kagi `STALE` / kasegi pin drift |
| `POINTER_PAST_EOF` | `warn` | pointer | `path:line` | File exists but line range past EOF | In range | kasegi `PAST-EOF` |
| `POINTER_MISSING_FILE` | `high` | pointer | `path=` | Path not found at base | Found | kasegi `MISSING-FILE` |
| `POINTER_BASE_ABSENT` | `info` | pointer | `base=` | Declared base tree absent; historical prefix policy applies | Base present | kasegi `BASE-ABSENT` / `LOST-RECORDED` |
| `POINTER_LOST_RECORDED` | `info` | pointer | `cite=` | Explicit `[lost-tree]` / `[lost-base]` style mark; non-openable by design | Unmarked lost path treated as live | kasegi `LOST-RECORDED` |
| `POINTER_NO_REVISION` | `warn` | claim/source | `claim=<id>` | SKILL "Reuse a finding: cite artifact + revision read" — pointer has path but no revision/stamp when the surface is mutable | Immutable blob pin or stamp row | kagi stamps.tsv pattern |

### 3.10 Export trust / injection handling

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `EXPORT_CHROME_PRESENT` | `info` | provenance | `record=<path>` | Record wraps or is a chat export (nav chrome, "You said:", model UI) — noted for readers | Clean method record |
| `EXPORT_TREATED_AS_SOURCE` | `warn` | claims/sources | `source=<id>` | Export UI chrome or prompt-shaped text cited as primary authority without `kind=export-data` | Marked export-data / survey-material |
| `EXPORT_INSTRUCTION_FOLLOWED` | `critical` | meta | `record=<path>` | Record's method section shows the author executed instruction-shaped text found *inside* an artifact (province: data never instruction) | Quoted as data with handling note |
| `PROVENANCE_UNKNOWN_UNMARKED` | `warn` | provenance | `record=<path>` | Producer/model/session unknowable locally and not listed under unknowns | Marked unknown |

**Central round finding (must stay visible):** `research/README.md:7-8` states these are browse-enabled GPT-6-Astra responses, **not** Deep Research pipeline; export citations are unverified. Any corpus rule that treats A/B/C bare cites as verified primary without restatement is itself `PROPOSAL_AS_ADMITTED` / method error.

### 3.11 Secrecy

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `SECRET_MATERIAL_PRESENT` | `critical` | record | `record=<path>;kind=` | Credential/session/token-shaped values (not shapes) appear in the record | Shape-only placeholders (`<token>`, `redacted`) |
| `SECRET_PATH_TOUCHED` | `critical` | gate/meta | `path=` | Record or gate config points at credential paths (`op.env`, `server.token`, `credentials/`, oauth dumps) for content read | Path mentioned as refuse-list only |
| `SECRET_SHAPE_OK` | `info` | record | `record=<path>` | Explicit shape-only note present — documentation/selftest aid, normally silent | — |

**Province:** secrets shape-only; kagi owns custody.

### 3.12 Scope boundary (cross-lane)

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `SCOPE_KASEGI_ABSORBED` | `warn` | record | `span=` | Bounty-program claim-package scope absorbed into chousa method record | Routed to kasegi; mentioned as boundary only |
| `SCOPE_KENGAKU_ABSORBED` | `warn` | record | `span=` | Model-quality / eval claims absorbed | Routed to kengaku |
| `SCOPE_ORCHESTRATION_ABSORBED` | `info` | record | `span=` | Dispatch/orchestration procedure presented as research method | Routed to kumitate; brief pointer OK |

### 3.13 Record shape / gate meta

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `RECORD_SCHEMA_INVALID` | `high` | record | `record=<path>` | Required top-level shape missing beyond single-field cases (cannot parse sections the gate requires) | Parseable |
| `RECORD_SECTION_ABSENT` | `info` | record | `record=…;section=` | Named **optional** section absent | Required missing → specific high id |
| `RECORD_PATH_UNREADABLE` | `info` | gate | `path=` | Target path unreadable (permission/IO) — unavailable, not content DRIFT by itself | Readable empty defect record |
| `GATE_PROFILE_UNKNOWN` | `info` | gate | `profile=` | Unknown profile name; falls back to default | Known profile |
| `SELFTEST_EXPECTED_MISMATCH` | `high` | fixtures | `case=<name>` | `--selftest` expected id set ≠ actual | Match |
| `SELFTEST_EXIT_MISMATCH` | `high` | fixtures | `case=<name>` | Expected exit ≠ actual | Match |
| `GATE_USAGE` | *(exit 2, not a finding id)* | CLI | — | Bad flags / setup — exit 2, no `RESEARCH_GATE` content verdict | — |

## 4. Clean (non-finding) states — named for selftest NO-FIRE cases

These are **not** finding ids. GateFixtureDesign asserts they produce **empty** finding lists (or info-only under default profile):

| clean label | observation |
|---|---|
| `QUESTION_DECLARED` | Non-empty scoped question field |
| `SOURCES_RANKED` | Every source row has a valid tier |
| `CHAIN_CLOSED_OR_MARKED` | Every hop resolved locally or marked unresolved with reason |
| `CLAIMS_POINTED` | Every claim has pointer + status |
| `REJECTIONS_KEPT` | Every discarded candidate has reason row; or explicit empty after sweep |
| `NEGATIVES_SWEPT` | Every negative claim has local-runnable or blocked-external sweep |
| `PROPOSALS_LABELED` | Unanchored rules marked `proposal` |
| `LOOPBACK_ONLY` | No external fetch; approval absent OK |
| `EXPORT_AS_DATA` | Export material marked `export-data` / survey-material |
| `SECRETS_SHAPE_ONLY` | No secret values |

## 5. Exemplars from the prompt (normative)

| exemplar | status in this catalog |
|---|---|
| `NO_QUESTION` | §3.1 `high` |
| `UNRANKED_SOURCE` | §3.2 `high` |
| `CHAIN_HOP_UNRESOLVED` | §3.3 `high` |
| `CLAIM_UNPOINTED` | §3.4 `high` |
| `REJECTION_DROPPED` | §3.5 `high` |

SKILL.md Gates line maps 1:1:

| SKILL contract phrase | Primary finding id(s) |
|---|---|
| question declared | `NO_QUESTION` |
| sources ranked | `UNRANKED_SOURCE`, `SOURCE_TABLE_ABSENT`, `HIERARCHY_MISLABEL` |
| chain hops resolved-or-marked | `CHAIN_HOP_UNRESOLVED`, `CHAIN_DEAD_LINK_SILENT` |
| claims pointed | `CLAIM_UNPOINTED`, `CLAIM_VERIFIED_WITHOUT_LOCAL` |
| rejections kept | `REJECTION_DROPPED`, `REJECTION_REASON_ABSENT` |

## 6. Owner routing (report-only; chousa does not remediate foreign lanes)

| id pattern | Owner of repair (not this gate) |
|---|---|
| `NO_QUESTION`, `QUESTION_*`, `UNRANKED_*`, `HIERARCHY_*`, `CHAIN_*`, `CLAIM_*`, `REJECTION_*`, `NEGATIVE_*`, `OBS_*`, `UNKNOWN_*`, `PROPOSAL_*`, `RULE_*`, `RECORD_*` | record author / chousa corpus maintainers |
| `EXTERNAL_*`, `APPROVAL_*`, `LIVE_FETCH_*` | operator (approval window) |
| `CITE_*`, `POINTER_*` | record author; mechanical kin to kagi/kasegi/kumitate cite disciplines |
| `EXPORT_*`, `PROVENANCE_*` | record author + survey harvester notes |
| `SECRET_*` | kagi custody; chousa refuses content |
| `SCOPE_KASEGI_*` | kasegi |
| `SCOPE_KENGAKU_*` | kengaku |
| `SCOPE_ORCHESTRATION_*` | kumitate |
| `SELFTEST_*`, `GATE_*` | chousa gate maintainers |

## 7. Compare algorithm (contract)

Input: previous receipt `F0`, current receipt `F1`, each a set of `{id, subject, sev, payload}`.

```
key(f)            = id + "\0" + subject
added             = keys(F1) - keys(F0)
cleared           = keys(F0) - keys(F1)
persisted         = keys(F0) ∩ keys(F1)
changed-payload   = persisted where payload_norm differs
```

`payload_norm` drops volatile fields (`measured_at`, absolute temp paths, raw byte counts) and keeps stable loci (`claim-id`, `hop-id`, relative record path, status tokens).

Gate banner (ResearchGateDesign owns exact string; ids stable regardless):

- `RESEARCH_GATE: CLEAN` — no findings with sev ∈ {`warn`,`high`,`critical`} (default profile); selftest green when run.
- `RESEARCH_GATE: DRIFT` — any such finding, or selftest id/exit mismatch.
- exit `0` CLEAN · `1` DRIFT · `2` setup/usage (not a finding id).

Ordered finding emission for selftest pins: deterministic sort by `(id ASC, subject ASC)` so expected lists are stable (same spirit as aggregator `CR-<repo>-<rule>-<n>` ordinals and mori compare keys).

## 8. Profiles (gate knobs; ids unchanged)

| profile | effect |
|---|---|
| `default` | DRIFT on sev ≥ `warn` |
| `strict` | DRIFT on sev ≥ `info` except pure `CITE_LABELED_DEAD`, `POINTER_LOST_RECORDED`, `POINTER_BASE_ABSENT`, `CHAIN_HOP_MARKED_UNRESOLVED`, `EXPORT_CHROME_PRESENT`, `SECRET_SHAPE_OK` |
| `shape-only` | only §3.1–3.5 core contract ids + secrecy criticals weigh |
| `loopback` | `EXTERNAL_*` / `LIVE_FETCH_*` always in scope; external URL resolve never attempted |
| `draft` | `SOURCE_TABLE_ABSENT` / `CLAIM_TABLE_ABSENT` downgraded to `warn` if record declares `status: draft` (proposal until GateDesign confirms) |

## 9. Out of vocabulary (explicit non-ids)

Do **not** invent findings for:

- bounty program scoring or claim-package validity (kasegi)
- model benchmark / quality grades (kengaku)
- fleet dispatch liveness, wave settlement, OOM (mori)
- credential vault health (kagi) beyond shape refusal
- "should fetch URL X" remediation phrased as an id
- truth of off-host primary sources when local material is absent — use `unresolvable` / `unverifiable-locally` statuses and `CITE_UNRESOLVED_LOCAL`, never a fake `CLAIM_VERIFIED_*` success id
- aesthetic rank metaphors from survey *content* (jin'i-ryū, dan/kyū) as method defects — content routes via CraftVsContent; method ids stay craft-only

## 10. Selftest minimum id coverage (for GateFixtureDesign)

Each id below **must** appear in at least one FAIL fixture case; CLEAN fixture must fire **none** of the high/warn set:

| case intent | expect exit | must include finding id |
|---|---|---|
| golden record | 0 | *(empty drift set)* |
| missing question | 1 | `NO_QUESTION` |
| source without rank | 1 | `UNRANKED_SOURCE` |
| hop broken silent | 1 | `CHAIN_HOP_UNRESOLVED` |
| claim without pointer | 1 | `CLAIM_UNPOINTED` |
| rejection without row/reason | 1 | `REJECTION_DROPPED` or `REJECTION_REASON_ABSENT` |
| negative claim, no sweep | 1 | `NEGATIVE_SWEEP_ABSENT` |
| verified but local-missing | 1 | `CLAIM_VERIFIED_WITHOUT_LOCAL` |
| proposal unlabeled | 1 | `PROPOSAL_AS_ADMITTED` |
| external without approval | 1 | `EXTERNAL_WITHOUT_APPROVAL` |
| ephemeral cite | 1 | `CITE_EPHEMERAL` |
| labeled dead cite only | 0 | `CITE_LABELED_DEAD` optional info; no DRIFT |
| secret value present | 1 | `SECRET_MATERIAL_PRESENT` |
| usage error | 2 | no content finding required |

## 11. Provenance anchors (this drafting run)

| claim | path / command | class |
|---|---|---|
| measure timestamp | `date -Iseconds` → `2026-10-14T21:54:04-03:00` | observation |
| SKILL decision table + errors + checklist + gates | `chousa-shokunin/SKILL.md:15-52` | source |
| QUALITY admission bar | `chousa-shokunin/corpus/QUALITY.md:1-5` | source |
| province refuses | `chousa-shokunin/PROVINCE.md:1-15` | source |
| research harvest note (not Deep Research; burner browse) | `research/README.md:5-16` | source |
| export A structure / bare cites | `research/deep-research-2026-09-28/A-shokunin-tradition.md` (109 lines; e.g. :35 question-in-prompt, :68-83 bare hosts) | observation on survey material |
| export B arxiv bare hosts | `…/B-multiagent-knowledge.md:51,72` | observation |
| export C negative attestation + bare hosts | `…/C-rank-taxonomy.md:53,109,82-100` | observation |
| kagi citation classes (UNRESOLVED/EPHEMERAL/labeled) | `kagi-shokunin/corpus/claim-ledger.sh:40-44,76-78,987-994` | fleet precedent |
| kasegi anchor verdict separation | `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-21,58-61` | fleet precedent |
| citation base vocabulary | `kasegi-shokunin/corpus/knowledge/citation-bases.md` | fleet precedent |
| mori FindingIds stability pattern | `.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/FindingIds.md` | form precedent |
| gate standard: exit + stable finding-id selftest | fleet PROTOCOL gate standard (via round-12/13 compact cites in `.ufo/waves`) | fleet precedent |
| wave contract surfaces | `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/spec.json` context + FindingIds item | assignment |

## 12. Limits

- This report does **not** implement `tools/research-gate.sh` and does not claim a live `RESEARCH_GATE: CLEAN|DRIFT` verdict.
- Semantic claim-support beyond mechanical local contradiction remains L2; id `CLAIM_CONTRADICTED_LOCAL` only fires when the gate's declared mechanical rule matches.
- Hierarchy tier names are fixed here; PrimarySourceHierarchy may refine *examples* without renaming ids.
- Approval column schema is owned by ApprovalTable; ids only freeze state tokens and absence predicates.
- Survey artifacts A/B/C are **inputs to method design**, not passing research records; applying this vocabulary directly to raw exports without a wrapping record is expected to DRIFT heavily — that DRIFT is educational calibration, not a slur on the harvest.
- No external fetches were performed. No product code, judge, commit, or gate binary was modified.
- Conflicts for the Rust judge: none observed between SKILL exemplars and this catalog; GateDesign may collapse `CHAIN_DEAD_LINK_SILENT` into `CHAIN_HOP_UNRESOLVED` at implement time **only if** selftest expected lists are updated in the same change — until then both names stay reserved and implementors SHOULD emit `CHAIN_HOP_UNRESOLVED` as the primary id for silent breaks.

---

### Axes (self-check against wave)

| axis | how this member pushed it |
|---|---|
| coverage | Full catalog over SKILL checklist + QUALITY bar + external/secrecy/export/scope + citation-form fleet parity; five prompt exemplars normative; selftest minimum matrix |
| depth | Per-id produce/not-produce predicates, subject keys, severity, clean NO-FIRE labels, compare algorithm, profiles |
| calibration | Live export bare-cite and negative-claim anchors separated from inferences; unavailable≠defect; mechanical≠semantic; proposal thresholds labeled; raw exports ≠ records |
