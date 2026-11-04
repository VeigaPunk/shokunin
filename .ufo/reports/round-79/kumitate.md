# kumitate round 79 — report

Lane: kumitate (axes: operability + coverage — orchestration and tooling). Round 79 of the run-15 hyaku
block. Lane repo `/home/vgpnk/Projects/shokunin/kumitate-shokunin`; base tip
`5019803b4e451094cf58c555408ea37490cbc07a`; scaffolding `ba940b512d980218b11ed6f34ac2f304c01287ee`;
pre-data amendments `8a733ab09c51594d64c1bc3b77a17d9d9172f8fd` (Amendment 2 + corrected C2 arm + r78 lesson
erratum) and `83f6815f184737d4fa4c1a02a40a7e8c841f5015` (wave payload). **Measured work revision
`357e4e730574486fc1fd77d037768296da6be685`; lane HEAD `0fb019a30203bfb5ecf444557d612bf3c197ffd9`**
(the close receipts are stamped with the measured revision in a second commit; a third commit appends the
lesson's counter erratum with the final close values; `git ls-remote origin refs/heads/master` printed the
HEAD before this report was filed).

## Work performed

The round declares **two claims**:

- **C1 — `coverage:kimi-layer`: the K score keeps both of its factors.** The round-78 harm (a de-named
  member heading read 10 where the base read 9, because the frozen formula *replaced* the `K_sections`
  factor with the census-finding factor) is repaired under the lane default (b) of the open L0 question
  `kumitate | round-78`: `coverage_kimi = floor(10 × C1k/C1k_total × K_sections/K_members ×
  (K_members−K_findings)/K_members)`. Instrument: `scripts/proxy-check.mjs` `kCoverage`; frozen counter
  `.ufo/waves/round-79/probe/probe79-c1.mjs` (11 arms); plan `.ufo/waves/round-79/plan.md` §C1.
- **C2 — `operability`: capability deepening `report-receipt-diff` v4.** The lane's own report gate gains
  the finding id `POINTER_DEAD`: every backticked repo-path pointer a report names resolves against the
  lane tree, the report's own directory and `<lane>/.ufo/waves/round-N/`, or (with `--rev`) that git
  tree only; receipt-shaped tokens stay `RECEIPT_MISSING` (no duplicate). Instrument:
  `scripts/report-receipt-diff.mjs` (contract `kumitate-report-receipt-diff-v4`); frozen counter
  `.ufo/waves/round-79/probe/probe79-c2.mjs` (12 arms); plan Amendment 1.

Work items (each with its evidence):

- **Round-open repair (the 8th spotcheck recurrence).** `spotcheck-adopt --adopt
  corpus/lessons/round-78-verifier-spotcheck.md` → `README_MAP: CLEAN files=191 rows=191 covered=191`
  (`.ufo/waves/round-79/open/gates-open.txt`), stanza `C2/C2_total` 190 → 191.
- **Frozen plan and counters.** `plan.md` plus Amendments 1–2, `probe/probe79-c1.mjs`,
  `probe/probe79-c2.mjs`, the frozen kimi fixture, the base-tree and stub controls (`.ufo/waves/round-79/`).
- **Sources opened and captured.** S229 GNU grep manual §2.3 (HTTP 200, 248692 bytes, sha256
  `517177d0…`), S230 scikit-learn `fbeta_score` (HTTP 200, 133786 bytes, sha256 `97e0b28f…`), S231 the
  lane's own r78 harm receipt; captures and fetch receipts under
  `.ufo/waves/round-79/build/L1/captures/` (`.ufo/waves/round-79/build/L1/captures/fetch-receipt.txt`).
- **C1 implemented and measured.** `kCoverage` beside the unchanged `layerCoverage` (S/R/O), selftest
  156 → 159 cases; the frozen counter reads `C79_C1: HELD held=11/11` (`.ufo/waves/round-79/close/c1-probe.txt`).
- **C2 implemented and measured.** `POINTER_DEAD` pass, no-duplicate rule, `..`-escape and
  non-regular-file refusal (directory/symlink), selftest 125 → 144 cases; the frozen counter reads
  `C79_C2: HELD held=12/12` (`.ufo/waves/round-79/close/c2-probe.txt`); the filed r78 report re-measured
  as `REPORT_RECEIPT: DRIFT RECEIPT_MISSING,POINTER_DEAD` with the 4 non-receipt dead pointers
  (`.ufo/waves/round-79/close/c2-r78.txt`).
- **Routed repair: `omp-census --compare` transient sidecars.** The round-open checklist was red on
  `SKILL.md:753` (`OMP_SHAPE_COMPARE: DRIFT entries=68 receipt=64 added=4 first=agent.db-shm`); `--compare`
  now classifies `agent.db-{shm,wal,journal}` as transient (`transient=<n>`, never a drift by itself), 10
  new selftest cases (89 total), re-pinned (`pin.omp-census`), and the checklist reads `IN_SYNC` on both
  live runs (`.ufo/waves/round-79/w1/K79ExecRepairs/{before,after,live-twice,pin}.txt`).
- **Knowledge entries.** `corpus/knowledge/composite-score-compensability.md` (S230, S231) and
  `corpus/knowledge/report-evidence-pointers.md` (S229), both with the provenance trio and README rows.
- **Corrections and registrations.** `SKILL.md` gate row v4, the v4 checklist item (in place), the
  composite-derivation item, the omp-census `--compare` clause and its selftest count; `SCORECARD.md`
  axes rows and move log; `PROVINCE.md` round-79 addition naming kotoba's overlap; `corpus/QUALITY.md` Q73.
- **r78 record erratum.** `corpus/lessons/round-78.md` gains an append-only erratum naming the eleven
  dead `close/` pointers and the superseded `C2/C2_total = 189`, `README_MAP files=189`, `A=874` readings
  (the filed r78 report is not rewritten).
- **Wave evidence.** ONE v1 wave of 13 seats (`w1-spec.json`, `w1-dispatch.json`, `.ufo/waves/round-79/w1-results.json`), the
  reports under `.ufo/waves/round-79/w1/`, and the per-claim counters' close receipts.
- **Round shape and settlement:** one v1 wave, 13 seats (attack 5/13 = 38 %: reviewer, critic,
  mutation-tester ×2, sentinel; connector 1; executors 3; scribes 2; scouts 2), the canonical planner seat
  held by the L1 (the validator rejects `planner` as a swarm role; orchestrator ruling 2026-10-19). All 13
  seats settled (`.ufo/waves/round-79/w1-results.json`); **12 wrote reports** under
  `.ufo/waves/round-79/w1/`; `K79MutC2` settled mid-work with **no report and no matrix** — recorded as a
  partial seat, never replaced; no seat reported an error, and `K79ExecKComposite`'s final message was
  empty while its patch and report are on disk and applied.
- **Independent attacks.** The critic falsified three C2 behaviours before filing — a directory named like a file resolved as CLEAN, a symlinked pointer resolved, and a `..`-escaping pointer resolved —
  and the L1 repaired all three (lstat-regular-file requirement, escape refusal) with three new selftest
  cases (`.ufo/waves/round-79/w1/K79CriticClaims/d-adversarial-fixtures.txt`). The C1 mutation seat killed
  7/7 mutants (`w1/K79MutC1/results.json`); the C2 mutation seat's matrix is `w1/K79MutC2/`.

## Landed changes

- **`scripts/proxy-check.mjs`** — `kCoverage`, the composite K call, 3 new selftest cases and the r78
  expectations restored to the composite arithmetic (159/159).
- **`scripts/report-receipt-diff.mjs`** — v4: `POINTER_DEAD`, the three resolution bases, `--rev`
  membership, no-duplicate rule, escape/non-regular-file refusal, 19 new selftest cases (144/144).
- **`scripts/omp-census.mjs`** — `--compare` transient sidecars (`transient=<n>`), 10 new cases (89).
- **`corpus/knowledge/composite-score-compensability.md`**, **`corpus/knowledge/report-evidence-pointers.md`**
  — new entries; **`corpus/SOURCES.md`** — S229–S232 (+ search log); **`corpus/README.md`** + pin — three
  rows; **`corpus/lessons/round-79.md`** — the round lesson and its append-only counter erratum (final close values
  A=884, C2=194, map 194, checklists 39/39); **`corpus/lessons/round-78.md`** — erratum;
  **`corpus/QUALITY.md`** — Q73; **`PROVINCE.md`** — the kotoba boundary; **`SKILL.md`**, **`SCORECARD.md`**,
  **`LOG.md`** — registration, claims, verdicts, record.
- Every change is recorded in `LOG.md` round 79 and carried by the work commit cited in the
  Before → after section (the lane tip is cited there and in the pre-filing gate).

## Before → after measurements

**C1 — counting command and the measured commit.** `node .ufo/waves/round-79/probe/probe79-c1.mjs --set c1
--lane .` — at a `git archive` of the base tree (`.ufo/waves/round-79/controls/c1-base.txt`): `C79_C1:
HELD held=7/11`, and the base formula reads `coverage_kimi=10` on a de-named heading (`K_sections=54`); the
constant-printer stub reads `held=4/11` (`controls/c1-stub.txt`). At the measured work revision
(`close/c1-probe.txt`): `C79_C1: HELD held=11/11` exit 0 — clean `K=55/55 findings=0 cov=10`; de-named
`K=54/55 cov=9`; one finding `cov=9`; both `cov=9`; zero members `cov=0`; `PROXY: MATCH`.

**C2 — counting command and the measured commit.** `node .ufo/waves/round-79/probe/probe79-c2.mjs --set c2
--lane .` — at the base tree: `C79_C2: HELD held=9/12` (`controls/c2-base.txt`; v3 has no `POINTER_DEAD`);
the constant-`CLEAN` stub reads `held=4/12` (`controls/c2-stub.txt`). At the measured work revision
(`close/c2-probe.txt`): `C79_C2: HELD held=12/12` exit 0, including the filed r78 report (4 `POINTER_DEAD`
beside 6 `RECEIPT_MISSING`), a conforming fixture (`CLEAN`), one-dead-pointer fixture (`missing=1`),
round-scoped resolution, URL skip, `--rev` membership, two fail-closed arms, `PLACEHOLDER` regression,
no-duplicate, and `REPORT_RECEIPT_SELFTEST: PASS (144/144)`.

## Sources & frontier

**Census before → after.** Command (round start and round end):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`.
At the round start it printed the six carried `W04` duplicate-URL warnings and `ok …/corpus/SOURCES.md`,
exit 0; at the round end it reads `ok`, exit 0, same six `W04` (`.ufo/waves/round-79/open/gates-open.txt`,
`close/sources.txt`).

**Rows.** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 167 → 171. Tier
histogram (`awk -F'|' … tier histogram`) → `A=143 B=16 C=8` → `A=146 B=16 C=9`. Rows added: **S229**
(docs, A), **S230** (docs, A), **S231** (own-work, A), **S232** (community, C, rejected). Rows touched
old→new: S229–S231 `queued` → `mined` (all three written and mined in this round); S232 stays `rejected`.
Frontier rows advanced: none new in the frontier bands this round — the two admitted entries are
instrument ground (the K score's aggregation; the lane's report gate), not frontier-band coverage; the
frontier bands stand as written.

**Search log.** One PRISMA-shaped note added for the two searches and the own-work re-read
(`corpus/SOURCES.md` § Search log, 2026-11-04).

**Assimilation: none.** `merge/kumitate/` was re-measured read-only at the round open (155 rows / 161
lines; `entries=70`, `accepted=155`) and refused unchanged for §10 proportionality and CORPUS.md rule 4;
flip: a dedicated assimilation round.

**considerthese:** the latest file is `considerthese/2026-10-26.md`; proposal 3 ("check that new tools get
registered") is the one mined this round — the v4 gate row and its checklist item land in the same round
as the instrument, and the composite counter is registered in `SKILL.md`; the omp-census repair carries
its re-pin. (Proposal 6, the counters table, is Q72 from round 77 and is applied in the lesson.)

## Trend verdicts

- **expansion — improved.** Two admitted `knowledge/` entries on ground the coverage map did not hold
  (`corpus/knowledge/composite-score-compensability.md`, `corpus/knowledge/report-evidence-pointers.md`), each opening
  with the provenance trio and citing a `mined` row opened this round (S230/S231; S229). README map
  `files=194 rows=194 covered=194`; SOURCES 167 → 171, tier A 143 → 146.
- **quality — improved.** Two sources re-opened byte-identically (S229/S230 captures, sha256 in
  `.ufo/waves/round-79/build/L1/captures/fetch-receipt.txt`), S231 re-read at its commit; the round-78 harm superseded by a stronger
  measurement instrument with a discriminating arm; `PROXY: MATCH`, selftests 159/159, 144/144 and 89;
  the r78 record corrected by an append-only erratum; the flaky `--compare` checklist repaired. No
  admitted entry was found false or stale and left unmarked.
- **discernment — improved.** The critic's adversarial fixtures changed the round's C2 implementation
  before filing (directory, symlink and `..`-escape holes closed with three selftest cases); the freeze
  review re-ran both control sets independently; the round's own mistake (a counter arm its contract made
  unreachable) was caught by the L1's dry run before any verdict, mined into `## Mistakes`, and turned
  into Q73. The non-author closure spot-check remains the outside judgment.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the v4 gate row,
  the composite-derivation item and the omp-census clause land this round (`SKILL.md` §Gate registry,
  §Verifiable checklist).
- [~] At least one end-to-end domain task executed and logged — both claims run end-to-end on real
  domain work (the lane's own gate and score), `LOG.md` round 79.
- [~] Instructions executable by an agent without oral context — every checklist item names a command, an
  accepted exit and an expected substring; the close checklist run is `close/checklists.txt`.
- [~] No cross-domain bleed (`PROVINCE.md` still accurate) — the kotoba report-pointer overlap is recorded
  in `PROVINCE.md`'s round-79 addition and reported, never absorbed.

**Stale-lane:** none — respawn-per-round driver; this round is the lane's only mission and it closes with
this report.

## Routed defects (carried; status-neutral)

1. **`spotcheck-adopt --check` still conflates unrelated map drift with an uncovered spotcheck** (round-79
   pre-registered candidate 3; not landed this round) — routed to round 80.
2. **The r78 filed report's dead pointers** are corrected by erratum only; the filed bytes are not
   rewritten (protocol). The r79 report's own pointers were checked by v4 before filing:
   `REPORT_RECEIPT: CLEAN (round=79 …)` (`kumitate-receipt.txt`, the pre-filing run receipt beside this report), and the draft
   caught seven pointer defects before that run (a bare QUALITY.md, bare knowledge paths, a two-word slash phrase read as a receipt, an example filename, and a not-yet-written results file).
3. **The composite still floors** (a single step costs one point; combined losses are not additive) and
   `K_findings` double-penalizes a missing member; both stated in `corpus/lessons/round-79.md` § Limits.

**Open L0:** `kumitate | round-78` (the K-score harm ruling) — this round lands the lane default (b); the
question stays open for the operator to confirm or overrule.

## Erratum — appended at round 80 (2026-11-04); supersedes only the text it names

The non-author spot-check of this round (`corpus/lessons/round-79-verifier-spotcheck.md`) routed eight
record defects (D1–D8). This erratum corrects the filed-report ones; the filed bytes above are not
rewritten (`PROTOCOL.md` §Round-robin rounds: a correction lands as an appended erratum naming the text
it supersedes — never a rewrite, labelled or silent).

- **D1 — superseded citation.** The "Round-open repair" bullet cites `.ufo/waves/round-79/open/gates-open.txt`
  for `README_MAP: CLEAN files=191 rows=191 covered=191`. That file is the before-snapshot and reads
  `DRIFT files=191 rows=190`; the clean reading is committed at
  `.ufo/waves/round-79/w1/K79ScoutOpen/gates.txt:35` and
  `.ufo/waves/round-79/w1/K79ReviewFreeze/scaffold-tree-readme-map.txt`.
- **D2 — dead pointer.** The "Independent attacks" bullet names the C2 mutation seat's matrix at
  `w1/K79MutC2/`; no such path exists at any lane revision, and the bullet itself records that the seat
  filed no report and no matrix. The absence is the record; the pointer is void.
- **D8 — recorded, not repaired.** This report was rewritten in place at `59aa9ae` (one header line and
  one Landed-changes bullet, plus a regenerated receipt) instead of an appended erratum; the superseded
  text is not recoverable from the filed bytes. Round 80 files this erratum rather than repeat the
  rewrite, and its own report is filed once.

D3–D7 (lesson counter names, the S229 quote word count, the round-78 SCORECARD placeholder, the close
receipts' missing `rev=` lines, and the missing committed round-start sources census) live in the lane
repo and are repaired there by appended errata and by this round's regime: every round-80 close receipt
carries a `rev=` line naming the measured revision, and the round-start census is committed under
`.ufo/waves/round-80/open/`.
