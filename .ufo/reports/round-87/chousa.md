# chousa — round 87 report

Round 87 (attempt 1). Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`.
Base `6495ef88` (round-86 landing + its non-author spot-check). Final lane tip `1f29e67b403c52386fac3a3c7a2fabcc64e1109c`
(local == remote).

**Round shape:** one v1 wave, **12 seats** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16) — 4 executor,
1 mutation-tester, 2 reviewer, 1 critic, 1 sentinel, 1 scout, 1 connector, 1 scribe. **Attack share 5/12 = 41.7 %**
(mutation-tester, 2 reviewer, critic, sentinel; the gate's `ATTACK_ROLES` set including the connector is 6/12 = 50 %).
**Residual call: none. Round total: 12 seats. Dead seats: 0.** Every seat returned a report and a receipt set.

## Work performed

The round declares **two claims on two distinct axes**, one on the lowest scored non-retired axis:

- **C1 `C1-BATTERY-R87` — operability** (lowest scored non-retired axis; the historical 3/10 is held, not re-scored).
  Capability + repair: the record battery's 203 class becomes every qualifying committed refetch row instead of one, the
  reject-form 203 class is added, and the verdict is leg-accounted so a dropped leg append or a denial-shape mutant
  changes the verdict. The subject tool's `url/unreach` form stops accepting a 2xx as a failed transfer.
- **C2 `C2-CURATION-R87` — calibration.** Per-entry located-quote count floors, a warrant-linkage leg over all 17
  decision rows, and a registry-`teaches`-against-own-capture leg whose flagged row must be disposed as superseded.

Work items, each with its evidence pointer:

- Frozen claims and pre-freeze repairs: `corpus/evidence/round87/claims.md`, `claims.json`,
  `corpus/evidence/round87/instrument-pins.txt`, `plans/round-87.md`. Freeze `c033577b`.
- Egress approval table committed **before** the first fetch: `corpus/evidence/round87/egress-approval.md` at
  `b7db0714` (`2026-11-08T06:50:27Z`).
- One fetch, inside the table: `S216` re-open, HTTP 200 at `2026-11-08T06:50:40Z`; both `raw_sha256`
  (`d431760660ea…`) and `txt_sha256` (`ec14fa3499c2…`) are byte-identical to round 86's attempt
  (`corpus/evidence/round57/refetch.tsv`, `S216` rows 1 and 2), so nothing about the capture moved.
- Registry delta: `S216.used-by` extended; `S218` appended (`own-work`, tier A, `mined`) as the contract the `TEACHES`
  leg enforces — `corpus/SOURCES.md:229-231`.
- The unreach repair: `tools/gate-records.py:248-253` (any 2xx is a successful response, never a failed transfer).
- Successor battery `corpus/evidence/round87/gate-records-r87.py` — `_qualifying_203` plus an independent
  `count_203_rows`, `build_d1_203_admits`, `build_d2_203_rejects`, `EXPECTED_LEGS = 15`, two mutants derived from the
  subject tool's own bytes and a derivation-negative probe.
- Successor curation counter `corpus/evidence/round87/curation-r87.py` — `FLOOR`, `WARRANT`, `TEACHES` legs, leg
  accounting.
- Control batteries: `mutate-r87.py` (counter and tool mutants), `curation-r87-controls.py` (the four routed
  forgeries), `harm-recheck.py` (committed records); independent expectations in
  `corpus/evidence/round87/controls/expected.tsv`; receipts in `controls/receipts/`.
- Lesson `corpus/lessons/round-87.md` (`## Gate`, `## Claim outcomes`, `## What the instruments measure`,
  `## Mistakes` ×7, `## Corrections` ×3, eight-row `## Spot-check intake`, `## Trends`); criteria
  `corpus/QUALITY.md` 182–189; `SCORECARD.md` round-87 verdict and round-88 plan; `LOG.md` round-87 entry;
  `corpus/README.md` coverage rows.
- Wave evidence: `.ufo/waves/round-87/{w1-spec.json,w1-dispatch.json,w1.ready,w1-results.json,claim-falsification.tsv,w1/}`.

## Landed changes

| change | LOG bullet | commit |
|---|---|---|
| Egress approval table + plan | 2 | `b7db07140791ab071de49743687e6d330edabc2e` |
| Freeze: claims, two counters, three control batteries, expectations, pre-freeze receipts, pins, the unreach repair | 3 | `c033577b4fb840553f3e10e40aa77c724abe0bca` |
| Landing: registry (`S216` used-by, `S218`), lesson, QUALITY 182–186, SCORECARD, LOG, README coverage, candidate receipts | 4–5 | `e6e920a4e6988287c31e89b3e920a118b569ae52` |
| Wave w1 spec (12 seats) + validated dispatch + ready handoff | 6 | `abf7ea58a5bbb7380c7f73ea4571a0f17b295258` |
| Integration: wave results (12 seats, 0 dead), falsification ledger, six amendments, the scribe audit's corrections (Mistakes 5–7, QUALITY 187–189, intake rows reconciled), landing-revision and census receipts | 7 | `1f29e67b403c52386fac3a3c7a2fabcc64e1109c` |
| Report (fleet repo) | — | filed after this table was written; cited in the closure, not in itself |

## Before → after measurements

**C1 operability.** Counting command:

```sh
S=$(mktemp -d -p /fast/scratch/hyaku) && git -C /home/vgpnk/Projects/shokunin/chousa-shokunin archive <rev> | tar -x -C "$S" \
  && python3 -B "$S/corpus/evidence/round87/gate-records-r87.py" --root "$S" --repo /home/vgpnk/Projects/shokunin/chousa-shokunin --work "$S"
```

- **Before** (committed controls): `D2_REFUSED=0/3 … MUT_UNREACH_DERIVED=0 LEGS=11/15` / `GATE_RECORDS_R87=FAIL`,
  exit 1, with the pre-round-87 tool (`controls/receipts/c1-k0-donothing.txt`); the round-86 instrument prints
  `D1_FORGES=1` and no `D2_` field at all (`c1-k0b-frozen-instrument.txt`).
- **After** at `e6e920a4` (re-measured at the integration tip `1f29e67b`):
  `TOOL=present POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=362/362 EXPECTED_CODE=362/362 EMPTY_REFUSED=1/1
  RC=4/4 SETUP=1/1 D1_EXPECTED=3 D1_FORGES=3 D1_REFUSED=3/3 D2_FORGES=3 D2_REFUSED=3/3 MUT_ADMIT_DERIVED=1
  MUT_ADMIT_KILLED=1 MUT_UNREACH_DERIVED=1 MUT_UNREACH_KILLED=1 DERIVE_NEG=1 LEGS=15/15` / `GATE_RECORDS_R87=PASS`,
  exit 0 (`corpus/evidence/round87/after/c1-after.txt`).
- Mutants: `MUTANTS_KILLED=4/4 TOOL_MUTANTS_CAUGHT=2/2 EQUIVALENT_ON_TREE=1/1` (`after/c1-mutants-landing.txt`).
  Harm: `files=11 records=28 moved=0` at landing — the freeze-time count was `files=10 records=27`, the extra record
  being this round's own lesson line (`controls/receipts/c1-harm-unreach.txt`, `after/` re-run).
- **Narrowed by plan Amendment 4** on the wave's own artifacts (`R87ReviewerC1` §a–c, `R87CriticClaims` §c,
  `R87MutCounter` A2/A4/A6/A8): see "what the instruments measure" below.

**C2 calibration.** Counting commands:

```sh
python3 -B corpus/evidence/round87/curation-r87.py --root /home/vgpnk/Projects/shokunin/chousa-shokunin
python3 -B corpus/evidence/round87/curation-r87-controls.py --root /home/vgpnk/Projects/shokunin/chousa-shokunin --work DIR
```

- **Before**: the frozen round-86 counter accepts all four routed forgeries — `FORGERY_REFUSED=4/4
  R86_ACCEPTED_FORGERY=4/4` (`controls/receipts/c2-controls.txt`) — and has no leg of the three new classes
  (`c2-d0-donothing.txt` → `CURATION_R86=PASS`).
- **After** at `e6e920a4`: `SUPERSEDED_LIVE=0 UNENTAILED_TERM=0 MODIFIED_DEF_CITED=1 QUOTES_LOCATED=20/20
  Q_FLOORS=search-transparency-reporting-r84.md=13/13 floor13,provenance-recording-r85.md=7/7 floor7 WARRANT_OK=17/17
  TEACHES_CHECKED=1 TEACHES_FLAGGED=1 TEACHES_UNRESOLVED=0 LEGS=7/7` / `CURATION_R87=PASS`, exit 0
  (`after/c2-after.txt`); controls `CONTROLS=PASS`, `FORGERY_REFUSED=4/4` (`after/c2-controls-landing.txt`).
- **Narrowed by plan Amendments 1, 2, 3 and 6** on four wave artifacts: see below.

### What the instruments measure, and what they do not

C1's verdict is a conjunction of 15 legs appended exactly once plus a frozen `EXPECTED_LEGS`, with two independent
width derivations. That changes the verdict for a **deleted leg append** and a **denial-shape mutant** (both round-86
`M2`/`M5` shapes), and refuses a class narrowed on one side. It does **not** catch a leg expression detached from its
measurement while every append and detail string survives (`R87ReviewerC1` E1/E4/E7), nor a two-point stub that credits
both mutants without building one (`R87CriticClaims` §c). The class the legs bound is "a committed refetch row with a
successful non-200 attempt, a stored capture hashing to the row's `txt_sha256` and a quotable line" — three rows at
this base, all 203; the code does not gate on `203` itself (`R87ReviewerC1` §a). All of this is stated in Amendment 4
and in C1's restated named limit.

C2's floors are **counts of located rows** (13 and 7), so a deleted row and a truncated table fail, while a substituted
table whose count is restored by a verbatim one-word quote passes (`R87ExecC2Forge` A1c/A1d) and so does replacing an
*uncited* row with a relabelled duplicate of a cited one (`R87CriticClaims` caseG). The warrant sharing test is per
row, not per qid (`R87ReviewerC2` F1), and the `TEACHES` disposition is structural — the superseder's status is not
consulted (`R87ReviewerC2` F2, where a `rejected` superseder disposes the flagged row). Amendments 1, 2, 3 and 6 record
each narrowing and route the count semantics to round 88.

A `R87MutCounter` class worth naming: four C2 counter mutants (`B1`, `B2`, `B3`, `B8`) survive **on the landing tree**
because no instance of their class fails there; the legs are load-bearing on the control mirrors, where the four routed
forgeries are refused 4/4. Amendment 5 records that a mutation battery scored only against the landing tree cannot
certify a leg whose class is unrepresented in it.

## Sources & frontier

Census command (frozen in `CORPUS.md`), run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- **Start** (`corpus/evidence/round87/census-start.txt`, `computed_against=6495ef88`, re-derived from the base
  archive): `exit 0`, 217 rows, the five pre-existing `W04` duplicate-url warnings (`S051`, `S053`, `S073`, `S074`,
  `S075`).
- **End** (`corpus/evidence/round87/census-end.txt`, `computed_against=e6e920a4`): `chousa ok …/corpus/SOURCES.md`,
  `exit 0`, 218 rows, the same five `W04` warnings, none introduced this round.
- Honest note on ordering: the start receipt was generated after the landing commit (the base state is correct by
  construction because the archive *is* the base, but the file order is end-then-start). Recorded as lesson Mistake 7
  and QUALITY 189; both receipts are committed in the integration commit and carry `computed_against=`.

**Rows 217 → 218.** Added by tier: one tier-A row, `S218` (`own-work`). Rows touched old→new: `S216.used-by`
`corpus/evidence/round86/claims.md` → `corpus/evidence/round86/claims.md, corpus/evidence/round87/claims.md` (logged in
the lesson's `## Gate`). No `status`, `recheck` or any immutable cell edited; no supersession edge added. Frontier rows
advanced: `S216` re-opened and now grounds two classes instead of one; `S024` is disposed rather than read, and the
`TEACHES` leg enforces that disposition.

**Assimilation: none.** No `merge/chousa/` theme and no `considerthese/` proposal was adopted; the wave-4
quarantine-first duty was discharged in an earlier round and nothing new was staged. The campaign's `corpus/SOURCES.md`
delta this round is curation (one `own-work` row, one `used-by` extension), not adopted package material.

**Conformance notes.** (1) The round-86 spot-check's conformance note 2 — a truncated run-15 quote in the dispatched
prompt — is carried: `.ufo/prompts/chousa-round-87.md:143` ends `…shokunin style bu…`, byte-identical to the round-86
prompt, so the defect is the operator-owned template's. (2) `corpus/README.md`'s frontier prose still ends at round 6;
this round appends a coverage section and does not rewrite another round's prose, so the carried defect is named and
now indexed. (3) The egress table's own closure sentence is defective (wrong column name and a vacuous bound); it is
recorded as lesson Mistake 6 and QUALITY 188 and the committed table is **not** edited.

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | **unchanged** | 97 knowledge files before and after (`ls corpus/knowledge/*.md \| wc -l`); one `own-work` registry row added. The round's gain is in the instruments, and this line says so instead of converting a row into ground. |
| quality | **improved** | six routed repairs across two instruments; 362 forgeries refused with expected codes; four round-86 forgeries now refused with named legs; 28 committed records move no verdict; eight criteria mined (QUALITY 182–189), four from this round's own findings and four from its wave's artifacts. |
| discernment | **improved** | every one of the wave's six attack seats produced a finding that reached the plan as a numbered amendment or a named limit, and none was argued away: the round withdrew one of its own sentences (`M2` credit shape "measured KILLED"), restated its named limit at the measured width, and published three defects in its own artifacts (the egress closure predicate, the census ordering, the README miscount) instead of leaving them to the closure. |

## SHONEN

`SHONEN.md` is untouched this round; each box carries the lane's own assessment (`[~]` with a resolvable pointer), no
box is claimed checked, and no promotion is claimed. A non-author verifier is required for any `[x]`.

- [~] **Real decision tables, error patterns, checklists with cited sources** — `SKILL.md` decision table (rows
  r24–r62), `## Error patterns`, `## Checklist (executable)`; this round's `corpus/evidence/round87/controls/expected.tsv`
  and the two counters' leg tables; `corpus/QUALITY.md` 182–189. Lane assertion; no non-author verifier named this round.
- [~] **At least one end-to-end domain task executed and logged** — the round's gate work is end-to-end
  (`gate-records-r87.py` over 15 frozen + 5 fresh positives and 362 forgeries; `curation-r87.py` over 17 decision rows
  and 218 registry rows; four forgery controls; a 28-record harm sweep), logged in `LOG.md` round 87. Lane assertion.
- [~] **Instructions executable by an agent without oral context** — `tools/lane-preflight.py` →
  `PREFLIGHT=8/8 FAILED=none ENV=none SKIPPED=none`; both counters run from a bare `git archive` with only
  `--root`/`--repo`/`--work`. Lane assertion.
- [~] **No cross-domain bleed, `PROVINCE.md` still accurate** — `PROVINCE.md` untouched; `R87ConnectorSiblings` scanned
  every sibling for HTTP-status, record-schema and quote-floor ground, found no conflict and nothing stricter, and
  nothing was absorbed. Lane assertion.

## Wave settlement

All 12 seats settled; 0 died; `PREFILE-FALSIFICATION: pass claims=2 rows=15 attack_seats=6 findings=0` (exit 0).

| seat | role | verdict on the seat's own item |
|---|---|---|
| `R87ExecRepro` | executor | both predicates reproduce at landing from a clean archive; 14 pins verify; harm `moved=0` |
| `R87ExecHarm` | executor | 28 committed records across 11 lessons, `moved=0`; the only genuine unreach record unchanged |
| `R87ExecForge` | executor | every 203-class forgery refused with its expected code; acceptances are out of class |
| `R87ExecC2Forge` | executor | **C2 fired** — A1c/A1d accepted forgeries (Amendment 2) |
| `R87MutCounter` | mutation-tester | C1 held / C2 held; A2/A4/A6/A8 survive as the printed-field class; B1–B3/B8 equivalent on tree (Amendments 4, 5) |
| `R87ReviewerC1` | reviewer | **C1 fired on wording** — non-200 class, `LEGS` counts appends, limit narrower than measured (Amendment 4) |
| `R87ReviewerC2` | reviewer | **C2 fired on wording** — F1 warrant sharing per row (Amendment 1), F2 disposition ignores status (Amendment 3) |
| `R87CriticClaims` | critic | C1 held / C2 held; the `M2` credit shape survives (Amendment 4), caseG restores the floor (Amendment 6) |
| `R87SentinelScope` | sentinel | C1/C2 held; F1 egress clean, F2 the table's closure predicate is vacuous (Mistake 6), F5 census receipts uncommitted (Mistake 7) |
| `R87ScoutRegistry` | scout | C2 held — the `teaches` population, over-fire and supersession chains re-derived over 218 rows |
| `R87ConnectorSiblings` | connector | C1/C2 held — no sibling owns this ground; nothing stricter, nothing absorbed |
| `R87ScribeLesson` | scribe | audited the lesson: four findings on the Gate block and four on the Mistakes/intake, all applied (Mistakes 5–7, QUALITY 187–189, intake rows reconciled) |

## Tooling

No tool was installed or upgraded this round: `python3` (stdlib), `git`, `curl` via the lane's own
`tools/capture-fetch.py`, and `node` for the wave validator were already present. pacman untouched (host-wide pause
respected); no host sysctl, no service, no `sudo`.

## Stale-lane

`Stale-lane: respawn-per-round driver; no other mission of this lane is open.` This round is round 87 of 100; attempt 1.

## Process notes

- Scratch: every seat and the L1 used `/fast/scratch/hyaku/chousa-r87/…`; nothing under `/tmp`; the L1 tree is removed
  after landing.
- Misroot sweep before filing: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
  `.scratch/` and another writer's `.ufo/l0-questions.md` edit; no chousa seat wrote outside the lane.
- Pre-file gate: `python3 scripts/hyaku/prefile-falsification.py --lane chousa --round 87` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=15 attack_seats=6 findings=0`, exit 0.
- No L0 question was opened this round; nothing was blocked on an operator decision.
