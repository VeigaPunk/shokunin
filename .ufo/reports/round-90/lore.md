# fleet report — lore r90 (round-90, world-bible lane)

Lane: `lore-shokunin` · Repo HEAD measured: `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (`ca7f9ef`).
Baseline: `e97613cc276f5fa9cac49ff1900798cf6863c020` (`e97613c`, r89 closure).
Wave: 33 work seats (`.ufo/waves/round-90/`: 33 seat reports + `wave-spec.md` + 24 seat-prefixed
patches; supplementary batch M5/C9/W3/SE3 included) + a follow-up judging wave
(`.ufo/waves/round-90/followup/`) that was still landing artifacts while this report was drafted.
**Snapshot cutoff for this report: `2026-10-17T07:01-03:00`, 32 artifacts** — the directory kept
growing after the cutoff; the later `JCAL2`/`JCAL4`/`JCOV1`/`JCOV2`/`JDEP2`/`CB1`/`H2`/`H4` `.md`
reports are listed but only cited where actually read. Every measurement below is taken on the
delivered tree at `ca7f9ef` — never on intent, never on a scratch patch. Scratch for probes only:
this seat `/tmp/P1-r90/`.

Tree state at measure: HEAD `ca7f9ef` at every check; `git status --porcelain` at `06:55:25` was
empty (the work commit is clean). During the follow-up wave the working tree gained only: the
untracked `followup/` artifacts; one in-place update of the tracked `followup/Q1-r90-debt.json`
(`21698 → 25869` bytes; `git diff --stat` → `109 insertions(+), 84 deletions(-)`; a follow-up seat's
delivered-tree revision, uncommitted at this cutoff); and `?? corpus/tools/__pycache__/` (a sibling
seat importing `support_check.py` as a module; running it as a script does not create it — JCAL1
Finding 7). No tracked file was modified at the commit and no seat committed.

Protocol checks (this seat, per the dependency rule — two 60 s wait-checks, then work with what
exists and note gaps): #1 `2026-10-17T06:55:25-03:00` (1 artifact: `followup/Q1-r90-debt.json`);
#2 `06:57:27` (2: `+H2-delta.json`); stabilization `06:59:17` (14); cutoff `07:00:24` (27) → `07:01`
(32). HEAD `ca7f9ef` at every check.

**Axis verdicts: `PENDING-L1` — the setter of verdicts is L1.** Judge recommendations recorded so
far (recommendations, not rulings): JCAL1 **calibration improved (bounded)**; JCOV5 **coverage
improved (bounded)**; JDEP3 depth sub-verdicts — R10 appendix + register no-false-entry boundary
**improved**, cross-cluster referent state **unchanged — correctly empty**, new-artifact referent
hygiene **unchanged — no harm**, register operability **unprovable-but-better**; Q2 process findings
only (no craft verdict). No harm was measured this round on any axis; the bounds and debts below are
recorded, not netted away.

## Work performed

Three claims were declared for round 90 (`.ufo/waves/round-90/wave-spec.md`), one per owned axis,
plus a supplementary batch (M5 span fix, C9 tick-gating ruling, W3 C7-receipt repair, SE3 sentinel)
that the spec's closure amendments record:

- **C1 — calibration** (lowest-axis obligation continues): repair the two r89 hedged shapes — the
  FN-2 qualifier is gated on non-null ids and on identity-dependent comparisons only, so
  `from_holder: null` chains and tick findings return to definite wording while genuinely
  unresolved non-null holder identities stay qualified; durable fixtures pin FN-1's raw-present half
  (`to_holder`, `from_holder`, `source_id`) and a ≥3-cause valid-key record; the FN-2 pair joins the
  canonical census manifest so the qualification is regression-visible. Prior 160 tuples preserved
  except enumerable deltas, 0 exit changes.
- **C2 — coverage**: in-corpus claim→excerpt maps with R9 delivery modes for both clusters (r87
  22 facts; r88-m3 map); ONE reproducible support command whose exit code + `N/N` print is the
  receipt, span-enforced (the M5 fix after M4's attack) and rejecting paraphrase/summary as
  source-text support.
- **C3 — depth**: JDEP2's three undecided sub-cases get decided governance — R8 (plausible but
  unrecorded influence), R9 (translator known, source/version unknown), R10 (matching name/ID,
  different occasions) — as merged appendices; the cross-cluster register re-verified correctly
  absent.

Work items and evidence pointers:

- **C1 implementation + fixtures** — landed by `ca7f9ef`: `corpus/fixtures/check_bible.py`
  (`1 file changed, 4 insertions(+), 11 deletions(-)` vs `e97613c`) composed from
  `patches/X2-c1-nullonly.patch` + `patches/X3-c1-tickonly.patch` per seat C9's ruling, plus four new
  fixture dirs. Candidates `X1.md`/`X2.md`/`X3.md`; scout `S1.md`; before-state reproducer `B3.md`
  (+ `patches/B3-before-state.json`); fixture author `F1.md` (+ `patches/F1-fixtures.patch`);
  critics `C5.md`/`C6.md`; delta predictor `C8.md` (+ `patches/C8-delta.json`); wording panel `E1.md`
  (+ `patches/E1-r90-wording.md`); ruling `C9.md` (+ `patches/C9-rerun-probes.sh`).
- **C2 maps + command** — landed by `ca7f9ef`: `claim-excerpt-map.md` in both clusters (M1/M2),
  `corpus/tools/support_check.py` + `corpus/tools/README.md` (M3, span fix M5:
  `patches/M5-span-fix.patch`); script verifier/attacker `M4.md`; span-fix `M5.md`; connector
  `K1.md` (+ `patches/K1-d1-crossrefs.patch`); scouts `S2.md`; discipline critic `C7.md` (+ repair
  `W3.md`).
- **C3 appendices** — landed by `ca7f9ef`: `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
  (+37 lines, 0 deletions: `### R8/R9/R10 appendix … (decided r90)` at lines 28/40/49 + provenance
  paragraph at 61). Drafts `D1.md`/`D2.md` (+ `patches/D1-decisions.md`, `patches/D2-decisions.md`);
  merger recommendation `R1.md`; cross-verifier `T1.md`; register re-verification `J3.md`; wording
  `E2.md` (+ `patches/E2-wording.md`).
- **Boundary / census / record** — baseline censuses `B1.md`/`B2.md` (+ `patches/B*-tuples.json`,
  byte-identical, sha256 `80bdc3b45ea785ea7e04dea776d95da0bd6dad088f60ae95100f21039cae42ad`);
  landing record `W1.md` (+ `patches/W1-landing-record.patch`); scribe `W2.md`
  (+ `patches/W2-{log,scorecard,report}-r90.*`); sentinels `SE1.md`/`SE3.md`; debt auditor + r91
  planner `Q1.md` (+ `followup/Q1-r90-debt.json`, `patches/Q1-r91-proposal.md`).
- **Follow-up judging at cutoff** (32 artifacts; folded-in here: `JCAL1.md` + `JCAL1-delta.json`,
  `JDEP3.md` + `JDEP3-probes.json`, `JCOV5.md` + `JCOV5-probes.json`, `Q2.md`, and the machine
  receipts `H3-r90-mutations.json`, `H4-census.json`, `H4-lineage.json`, `H4-probes.json`,
  `JCAL5-delta.json`, `JCOV3-denominators.json`; landed-but-not-yet-folded at cutoff:
  `CB1.md`, `H2.md`, `H4.md`, `JCAL2.md`, `JCAL4.md`, `JCOV1.md`, `JCOV2.md`, `JDEP2.md` and the
  JSON receipts alongside them). The updated `followup/Q1-r90-debt.json` records delivered-tree
  closure verdicts `verified 19 / partial 9 / open 13 / bound 7 / carried 4 / not claimed 1` and
  7 new debts `Q90-001…` (in-place working-tree revision; uncommitted at this cutoff).

## Landed changes

- **C1 — `corpus/fixtures/check_bible.py`** (delivered sha256
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`) and four new fixture dirs:
  `r90-c1-rawpresent-from`, `r90-c1-rawpresent-to`, `r90-c1-rawpresent-source`,
  `r90-c1-three-causes` (each with README + five section JSONs). Commit **`ca7f9ef`**.
- **C2 — two maps + tool**: `corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md` (sha256
  `8c1b600d…`) and `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md` (sha256 `d314d22e…`);
  R9 mode lines added to the five r87 excerpt files and to `fictional-excerpts.md`;
  `corpus/tools/support_check.py` (sha256 `66a3c4bb…`) + `corpus/tools/README.md`. Commit
  **`ca7f9ef`**.
- **C3 — appendices**: `corpus/knowledge/r88-sourced-inspiration-decision-table.md` +37/−0 (merged
  from D1/D2 per R1's recommendation; provenance line at :61). Commit **`ca7f9ef`**.
- **Wave evidence — `.ufo/waves/round-90/`** (33 seat reports + `wave-spec.md` + 24 patches).
  Commit **`ca7f9ef`**; `git diff --name-only e97613c ca7f9ef | sed 's#/.*##' | sort | uniq -c` →
  `36 corpus`, `59 .ufo` (95 files, +12619/−11). Single commit, author = committer =
  `lore-shokunin <lore@shokunin.local>`.
- **Not committed (open for the integrator):** the entire `.ufo/waves/round-90/followup/` judging
  wave (32 artifacts at cutoff, untracked; `Q1-r90-debt.json` additionally modified in place);
  `corpus/tools/__pycache__/` (untracked residue, not produced by the delivered commands).
- **Round record:** `git diff --name-only e97613c ca7f9ef -- LOG.md SCORECARD.md SHONEN.md PROVINCE.md
  README.md l0-questions.md` → empty. Drafts only: `patches/W2-log-r90.proposal.md`,
  `patches/W2-scorecard-r90.proposal.md` (both banner themselves PROPOSAL ONLY, all verdicts
  PENDING-L1), `patches/W2-report-r90.skeleton.md`. No `l0-questions.md` append was authorized or
  made this round.
- **No push:** `git rev-list --left-right --count origin/main...main` → `0 9` (9 ahead, 0 behind).

## Before → after measurements

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless noted.

### Freeze-then-verify (r88-I1) — the delivered checker vs X2+X3 composed

```sh
$ mkdir -p /tmp/P1-r90/compose/corpus/fixtures
$ git show e97613c:corpus/fixtures/check_bible.py > /tmp/P1-r90/compose/corpus/fixtures/check_bible.py
$ git show ca7f9ef:.ufo/waves/round-90/patches/X2-c1-nullonly.patch > /tmp/P1-r90/compose/X2.patch
$ git show ca7f9ef:.ufo/waves/round-90/patches/X3-c1-tickonly.patch > /tmp/P1-r90/compose/X3.patch
$ cd /tmp/P1-r90/compose && patch -p1 < X2.patch && patch -p1 < X3.patch
patching file corpus/fixtures/check_bible.py
patching file corpus/fixtures/check_bible.py
Hunk #1 succeeded at 321 (offset 2 lines).
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ (repo) git show ca7f9ef:corpus/fixtures/check_bible.py | sha256sum   # commit blob
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
$ (repo) sha256sum corpus/fixtures/check_bible.py                      # working tree
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

**PASS — byte-identical, no mismatch, no blocking finding.** Independently reproduced with the same
hash by C6.md (its X2+X3 composition replay), JCAL1.md, JDEP3.md, JCOV5.md, Q2.md and JCAL5-delta.json;
the baseline checker re-measured as `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
matches Q1/C8/SE1 records. **Receipt-provenance nuance (named debt D-c9-receipt, not a freeze
failure):** seat C9's committed `patches/C9-rerun-probes.sh` reconstructs the **X1** candidate
(patch `6d37eccf…`, checker `12866e73…`), not the delivered composition. I re-ran the script (exit 0,
its own hash assertions hold) and then ran its four probe cases against the delivered checker:
3 of 4 outputs agree with the script's X1 outputs; the `tick-relevant-unresolved` case diverges —
X1 returns a qualified tick, the delivered composition returns the definite
`provenance tick 1 must be greater than previous tick 3` (the C9-ruling reading). C6 measured the
same divergence and C9's report states the script "confirms its behavior, not the ruling". The
delivered artifact is the ruled composition; the X1-binding harness is the receipt that does not
bind to the shipped bytes.

### Census and delta (measurement, not an axis claim)

Census harness (`/tmp/P1-r90/census.py`): every immediate `corpus/fixtures/*` dir run as
`python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` with the repo root as cwd; records
`(exit, stdout sha256, violation count, stderr non-empty)`. Baseline reference: the committed
`patches/B1-tuples.json` (160 dirs; B2's file is byte-identical).

```sh
$ python3 /tmp/P1-r90/census.py . /tmp/P1-r90/deliv-tuples.json
root=/home/vgpnk/Projects/shokunin/lore-shokunin dirs=164 exits={0: 32, 1: 132} violations=417 stderr_nonempty=0

$ delta vs patches/B1-tuples.json
baseline dirs 160  delivered dirs 164
new 4 ['corpus/fixtures/r90-c1-rawpresent-from', 'corpus/fixtures/r90-c1-rawpresent-source',
 'corpus/fixtures/r90-c1-rawpresent-to', 'corpus/fixtures/r90-c1-three-causes']
gone 0 []
changed 0 exit_changes 0 count_changes 0 hash_changes 0
exit hist base {0: 32, 1: 128} -> head {0: 32, 1: 132}
violations base 399 -> head 417; new-dir finding sum = 18   (5+4+5+4, each exit 1)
```

- **Delta enumerable: `changed=0, new=4, missing=0, exit_changes=0, stderr_changes=0`.** 160/160
  baseline tuples byte-identical (stdout hash compared, not just exits). The identity
  `417 − 399 = 18` equals the summed findings of the four new dirs exactly.
- Reproduced independently: JCAL1 (plus a baseline-checker-on-head replay: 0 mismatches, and a
  two-run determinism guard, 0 diffs), JCAL5 (sorted/shuffled order-independence), H4
  (`H4-census.json`), C8 (candidate-level, X1), Q2. The two cluster dirs that gained `.md` files are
  in the census and stayed byte-identical — `check_bible.py` reads only `<section>.json`, so no `.md`
  edit can move a tuple (JCAL1 root-cause note).

### C1 — calibration

**The two r89 hedged shapes, before → after (this seat's probes, built from
`corpus/fixtures/r89-fn2-unresolved-chain-break`; baseline checker extracted from `e97613c` to
`/tmp/P1-r90/base/check_bible.py`):**

```
$ python3 <baseline|delivered> check_bible.py /tmp/P1-r90/probes/<case>
case: null-from-chain
  BEFORE: VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon;
          possible provenance chain break, not a definite identity mismatch: expected from_holder
          'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry
          this id, but only 0 is in the resolved index)
  AFTER:  VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got None
case: tick-relevant-unresolved
  BEFORE: VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon;
          holder identity is not uniquely resolvable: expected from_holder 'f3-dup' …;
          provenance tick 1 must be greater than previous tick 3
  AFTER:  VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
case: chain-unresolved (genuinely unresolved non-null holder) — BEFORE = AFTER, character for
      character: '…possible provenance chain break, not a definite identity mismatch: expected
      from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1
      is in the resolved index); got 'mira''  [must stay qualified — PASS]
case: unrelated-duplicate-tick — BEFORE = AFTER: '…tick: provenance tick 1 must be greater than
      previous tick 3'  [must stay definite — PASS]
```

All four exit 1, stderr empty. B3-before-state.json's baseline receipts match my BEFORE outputs;
JCAL1's five-case matrix adds the scope control (`null-to-then-nonnull-from` is rejected upstream as
`malformed record (invalid to_holder)`, so the X2 null gate covers exactly and only the reachable
null input — `from_holder`). X3.md/C5.md probe sets agree; C8's final X1 census is the separate
candidate measurement (below).

**Durable fixtures (C1(ii)).** The four new dirs pin the FN-1 raw-present wording and the ≥3-cause
joined summary; F1.md's declared after-state replays byte-for-byte on the delivered checker (my
census confirms: `rawpresent-from` 5 findings, `rawpresent-to` 5, `rawpresent-source` 4,
`three-causes` 4; the `three-causes` first-stop line names all three latching causes in validation
order). Note the wording these fixtures pin **already existed at `e97613c`** (F1: "the unpatched
checker already emits…"; my census: these dirs are new, but no baseline fixture output moved) — they
are durable regression pins, not the r90 delta itself. The r90 wording delta is exercised only by
scratch probes; the follow-up ledger's new debt **Q90-001** flags exactly this regression
invisibility.

**FN-2 census registration (C1(iii)).** `r89-fn2-control` (exit 1, 1 violation) and
`r89-fn2-unresolved-chain-break` (exit 1, 2 violations) are both rows of `B1-tuples.json` and of my
delivered census — the r89 bound "FN-2 is invisible to the manifest" is closed.

**Candidate record (context, not delivered):** X1 (the unshipped alternative, patch `6d37eccf…`)
changes one tuple of 160 (`r87-probe-source-prefix` stdout, 0 exit changes; C8/C6/S1 reproduce) and
keeps a tick-identity hedge that X3 removes; the delivered composition has an empty 160-tuple delta
(C6) and the four probes above. C6 measured the two candidates' semantic difference; C9's ruling and
the spec's closure amendment ("SHIP the integer-only tick reading (X2 null-gate + X3 tick-gating
composed)") selected the delivered reading, with the X1 gate named as the r91 falsification path.

### C2 — coverage

**Maps.** r87: `claim-excerpt-map.md` (57 lines) — 5 excerpt declarations + 22 rows (6 entity
claims E1–E6, 4 relations R1–R4, 4 timeline T1–T4, 8 hymn clauses H1–H8), every row and declaration
`verbatim`, with a "Full D1 crosswalk" note covering the remaining `first_appearance` pointer and the
`entities[2]` claim via H4. r88-m3: `claim-excerpt-map.md` (41 lines) — 3 declaration rows + 10 JSON
rows (P1–P4, E1–E4, T1–T2), all `verbatim`; the Spence passage is `verbatim` with `external-only`
confined to the underlying K'iche text (the M5 correction; the K1-flagged r89 mislabel is repaired).
Two source-to-fictional symbolism comparisons are separate bullet entries, not part of the 10-row
denominator.

**The single support command (delivered, this seat's runs):**

```sh
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS        [exit=0]
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS        [exit=0]
$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase;
  9:A modern paraphrase says … the tide-mark had been moved to the west stair.
SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
RESULT PASS        [exit=0]
```

**Span enforcement (D-M4-1 closed on the delivered tree).** Scratch copy of the r87 cluster with the
E1 locator mutated `:7 → :6`:

```sh
$ python3 corpus/tools/support_check.py /tmp/P1-r90/span-attack/cluster   # mutated copy
FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, …; span=6; outside-span=7
SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
FAIL: E1: anchor hit outside declared line span 6 (hit lines: 7)        [exit=1]
```

M4's original attack (pre-fix) passed at 22/22; M5's three attacks (wrong-line, duplicate-hit,
missing-span) and my attack now fail closed. JCOV5's independent controls add: paraphrase row counts
0 source support; a `verbatim` row against a declared `paraphrase` excerpt fails with exit 1; the
same bytes count differently only by declared mode. Bounds: the checker is lexical preflight
(`grep -nF` substring anchors; mid-word matches pass — JCOV5 ND-2); it does not verify
translation/version identity or whole-claim fidelity (its README states this); the receipt is
per-cluster (`22/22` + `10/10`, no aggregate invocation — M4 D-M4-2, resolved as per-cluster by the
delivered README); and the r87 `22/22` counts 22 mapped rows, while the D1 JSON denominator
(7+7+4+4=22) is covered via the map's stated co-mapping — keep the two denominators named (C7).

### C3 — depth

**Decided appendices (delivered, lines 28/40/49 + provenance :61; +37/−0).** `grep -n` on the
delivered table:

```
28:### R8 appendix — plausible but unrecorded influence (decided r90)
40:### R9 appendix — translator known, source/version unknown (decided r90)
49:### R10 appendix — matching name/ID, different occasions (decided r90)
61:(Provenance: merged from seats D1/D2 per seat R1's recommendation; retroactivity checked —
65:## Integration boundary
```

- **R8:** a dated neutral `possible influence: unverified` note records uncertainty, not influence;
  R2 (no source used) requires BOTH the creator's no-source account AND the editor finding no
  contrary source-specific evidence AND only a commonplace motif; the
  `external-only / unverified inspiration` marker is reserved for established general-motif use;
  only the affected detail is withheld.
- **R9:** translator name alone with the source/version link unverified **FAILS R5 support**; keep
  `Delivery mode: translation`, record `Source text/version: unidentified; unverified`; the narrow
  exception permits support only for a claim about an identified translation when a reliable
  bibliographic record ties the passage and translator to a named work — never original wording.
- **R10:** shared names/IDs trigger comparison but do not prove identity; dismissed overlaps go to
  the incoming cluster README under `## R10 comparison outcomes`; unresolved candidates also to
  `l0-questions.md`; the live register is reserved for a source-backed shared referent, field, and
  occasion with incompatible assertions — its first real entry awaits a genuine conflict.

Merged per R1's recommendation (D1's appendix packaging + D2's safer gates); T1's cross-verification
replayed the JDEP2 cases and confirmed no retroactive reclassification (r87 ETCSL marker,
r88-m3 Spence passage, Hara/Sen local contradiction unaffected).

**Register correctly absent.** `corpus/knowledge/cross-cluster-contradictions.md` absent at
`e97613c` and `ca7f9ef` (`git cat-file -e` fatal on both — JDEP3); no README carries an
`## R10 comparison outcomes` section (correct: no incoming cluster landed); the r89 demo file is
byte-identical to baseline. Empty intersections across entity/source/timeline ids, place ids,
relation tuples, whole-word text, and map anchor strings (JDEP3/J3/T1/R1/Q1, this seat's
`register_present False`). The four r90 fixtures and two maps introduce no shared referent
(JDEP3 F2: shared ids involving an r90 dir = `{}`; no cluster nouns; disjoint anchors).

**Bounds:** the R8/R9 new branches have no durable demo fixtures and the `translation` mode is
unexercised by delivered rows (JCOV5 §7); the register's file/format conventions and the
"landed-clusters vs fixture-directories" scoping rule remain unstated (JDEP3 named debt); the R10
comparison-outcomes section is unexercisable until an incoming cluster lands.

### Round record, SHONEN, documentation parity

- Round record unchanged at `ca7f9ef` (see Landed changes); W2's drafts banner PROPOSAL ONLY with
  all verdicts PENDING-L1.
- `SHONEN.md` unchanged (`git diff --stat e97613c ca7f9ef -- SHONEN.md` → empty); four boxes at
  `SHONEN.md:5,6,8,9`; no `[x]` anywhere (details below).
- **Named documentation-parity recurrence (JCAL1 Finding 6):** `corpus/fixtures/README.md` carries
  per-round sections for 87/88/89 but **no Round 90 section** — `grep -n "r90-c1"` returns nothing,
  so the four new fixtures are indexed nowhere in the top-level fixture README (each new fixture
  does carry its own in-directory README). Same defect class r89's closure repaired; fix is one
  paragraph at the r91 closure. Adjacent carried residue: `reference-ledger.md`'s Spence row still
  sits outside the table (JDEP3 note; Q89-020), and the K1 cross-reference debt below.

## SHONEN

`SHONEN.md` is unchanged this round; four boxes at `SHONEN.md:5,6,8,9`. **No `[x]` is claimed** —
no named non-author verifier has executed the lane's instructions cold. Boxes use `[~]`/`[ ]` only:

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists, cited
  sources* — **unchanged**. `test -e SKILL.md` → absent; the governance material lives in
  `corpus/knowledge/` (R8–R10 appendices at :28/:40/:49, the R9 demo fixture, the R10 worked
  example), not in a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* —
  **lane assertion retained; evidence improves but its own pointer stays stale**. The clause is
  satisfied by the round-87 (`LOG.md:1699`) and round-88 (`LOG.md:1908`) records; round 90 adds a
  third end-to-end set (164-dir census, 4 durable fixtures, 22/22 + 10/10 receipts, decided
  appendices) but r90's own LOG entry is **not** appended — drafts only
  (`patches/W2-log-r90.proposal.md`). The box's evidence pointer still cites round-1 only.
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* — **unchanged;
  cannot move without a cold non-author verifier**. For the move: the support command is now a
  reproducible receipt with span enforcement (this seat re-ran it; JCOV5's controls), the maps carry
  explicit R9 declarations, and the decided appendices carry owners and triggers. Against: the
  r90 fixtures README gap, the K1 cross-reference not landed in the governance table, and the
  register's unexercised paths. Either way the box needs a named non-author execution.
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — **lane assertion
  retained; evidence strengthened**. `PROVINCE.md` bytes unchanged at both commits; all 95 changed
  paths are under `corpus/` (36) or `.ufo/` (59); no chousa/kotodama content is copied into
  `corpus/` (`grep -rn 'chousa' corpus/` → rc 1; JCOV5's sibling-adjacency review finds both new
  artifacts inside lore's province with rejected-fit reasoning per sibling); the K1 lines, where
  they landed (wave artifact only), say "not a transfer of lore authority".

## Verdicts (ruled by L1 at closure)

calibration **improved (bounded)** — hedged shapes repaired per seat C9's integer-only tick
ruling; 0 changed + 4 new of 164 dirs, 0 exit changes, six independent censuses, freeze PASS
(delivered checker == X2+X3 composed, `ff9fd2aa…`). Bounds: no discriminating durable fixture
(Q90-001, first r91 item); C9's reading carries a named falsification path; the
unresolved-expected-side sub-case stays qualified (under-claim, F5).

coverage **improved (bounded)** — in-corpus maps + the span-enforced support command
(`r87 22/22`, `r88-m3 10/10`, paraphrase retelling-only, wrong-line fails closed), receipts
reproduced by five judges. Bounds: `22/22` counts rows (14 JSON + 8 editorial, 2 prose-only
disclosed); two silent-failure vectors named for r91 hardening; modes are self-declared.

depth **improved (bounded)** — R8/R9/R10 sub-cases decided (merged per R1); register correctly
absent. The third documentation-parity harm (boundary doc drift on the C9 ruling + ~30 anchors
+ falsified fixture claims) was repaired at closure from CB1's verified refresh and is
recorded transparently here, in SCORECARD.md, and in LOG.md — not netted.

**Round admitted** — every claim verifies; no unresolved trade.
## Findings & named debt

- **D-c9-receipt (provenance).** `patches/C9-rerun-probes.sh` binds the **X1** candidate
  (`6d37eccf…`/`12866e73…`), not the delivered composition (`ff9fd2aa…`); its four probes agree with
  the delivered checker on 3/4 and diverge on `tick-relevant-unresolved` (X1 qualified, delivered
  definite — the ruled reading). Disclosed by C9 and C6; the committed ruling harness is therefore a
  losing-patch receipt, not a shipped-artifact receipt. The delivered artifact itself verifies
  (freeze-then-verify PASS).
- **D-x1-alternative (r91 falsification path).** X1's gate (tick qualification when a compared
  non-null holder is unresolved; its first-record branch unchanged) remains unshipped; promote it in
  r91 only if a case emerges where tick order genuinely needed identity context (C9/C8/JCAL1).
- **D-q90-001 (follow-up ledger).** Regression invisibility: no durable fixture distinguishes the
  baseline from the delivered checker (0 changed tuples; the four new fixtures pin pre-existing
  wording); the repaired shapes are exercised only by scratch probes. Also 6 further new debts in the
  updated `followup/Q1-r90-debt.json` (uncommitted in-place revision).
- **D-k1 (cross-reference not landed).** K1's two chousa cross-reference lines are delivered only in
  the wave-stage `patches/D1-decisions.md:60-61`; `grep -rn 'chousa' corpus/` → rc 1, so the
  governing table's appendices carry none. Q89-047's delivered-governance half remains open
  (JCOV5 ND-1).
- **D-anchor-substring (JCOV5 ND-2).** Delivered anchors are plain `grep -nF` substrings; mid-word
  occurrences pass. Named for future authoring; current receipts unaffected (all delivered anchors
  are clause/space bounded).
- **D-r90-readme.** No Round 90 section in `corpus/fixtures/README.md`; the four new fixtures are
  indexed nowhere in the top-level README (JCAL1 F6; recurrence of an r89-repaired class).
- **D-c2-denominators.** r87 `22/22` counts 22 mapped rows (14 JSON + 8 hymn) with the JSON
  denominator covered via the map's crosswalk; r88 `10/10` covers the ten JSON rows with the two
  symbolism comparisons separate (4/4 anchors); per-cluster commands, no aggregate. Keep the
  denominators explicit in any closure text.
- **D-r8-r9-demo.** No durable demo fixtures for the new R8/R9 branches; `translation` unexercised by
  delivered rows; the `## R10 comparison outcomes` section is unexercisable until an incoming
  cluster lands; register file/format conventions and the landed-clusters scoping rule remain
  unstated (JDEP3 named debts).
- **D-process (Q2, R90-P1…P5).** Roster counts 32 declared / 29 enumerated / 33 delivered (prose, not
  data); landing-record cutoff bias (0/12 dependent seats inside the 20-minute window; supplementary
  batch carried the round's verification for the second round running); poll protocol loses its own
  terminal receipt (8/21 polling seats with cap defects; 5 killed at exactly their own 1200 s
  deadline; 3 restarts with 73 s–4 m54 s gaps); `/tmp` inode ceiling (one seat blocked; 20 residue
  entries, 2137 files); the C9 composition has no seat-owned artifact (verified this round by
  freeze-then-verify — the r89-I2 hash-stamped freeze still does not exist). Q2 names three
  measurable r91 fixes (poll helper with margin+TERM trap; roster-as-data + validator; scratch
  budget + closure sweep).
- **D-pycache.** `corpus/tools/__pycache__/` untracked residue (sibling seats import the tool; not
  the delivered commands; Q89-044 — no `__pycache__` ignore in `.gitignore`).
- **Q1 r90 debt ledger.** 53 rows re-audited on the delivered tree by the updated follow-up revision:
  `verified 19 / partial 9 / open 13 / bound 7 / carried 4 / not claimed 1` + 7 new `Q90-*` debts;
  r91 axis selection remains conditional on L1's verdict over the frozen tree (no scalars inferred
  from counts).
- **No push, no registry write, no sibling-repo write.** The `followup/` wave (32 artifacts at
  cutoff) and the in-place `Q1-r90-debt.json` revision are left for the integrator's commit decision.

## Pointers

- Wave reports + patches: `lore-shokunin/.ufo/waves/round-90/` (33 seat reports + `wave-spec.md`,
  24 seat-prefixed patches).
- Follow-up artifacts: `lore-shokunin/.ufo/waves/round-90/followup/` (32 files at the
  `2026-10-17T07:01-03:00` cutoff; still landing).
- Work commit: `lore-shokunin@ca7f9ef` (baseline `e97613c`). No push (9 ahead of `origin/main`).
- Uncommitted: `.ufo/waves/round-90/followup/` (untracked) + the in-place `Q1-r90-debt.json`
  revision + `corpus/tools/__pycache__/`.
- Round-record drafts: `patches/W2-log-r90.proposal.md`, `patches/W2-scorecard-r90.proposal.md`,
  `patches/W2-report-r90.skeleton.md`.
- Debt ledger / r91 planner: `followup/Q1-r90-debt.json` (updated revision), `patches/Q1-r91-proposal.md`
  (+ `Q1.md`).
- MANIFEST closure entry draft: `.ufo/waves/round-90/followup/P1-manifest-entry.json`.
- Seat report + receipts for this writer: `.ufo/waves/round-90/followup/P1.md`,
  `followup/P1-measurements.json`.

## Handoff

- **Delivered revision and verification scratch:** `ca7f9ef`; scratch `/tmp/P1-r90/` (`census.py`,
  `compose/` X2+X3 composition, `base/` baseline checker, `x1/` X1 tree, `probes/` four probe
  fixtures, `span-attack/` mutated map copy). This seat re-ran, on the delivered tree: the
  freeze-then-verify composition (PASS, `ff9fd2aa…`), the 164-dir census + delta vs
  `patches/B1-tuples.json` (0 changed + 4 new, 0 exit changes, 417−399=18), the four probe cases on
  both checkers, the support command on both clusters + the paraphrase demo (22/22, 10/10,
  retelling-only; all exit 0), and the span-enforcement attack (fail-closed, exit 1). Every figure in
  "Before → after measurements" is this seat's observed output; the machine-readable bundle is
  `followup/P1-measurements.json`.
- **Integrated claim artifacts:** C1 — `corpus/fixtures/check_bible.py` + 4 fixture dirs; C2 — two
  `claim-excerpt-map.md` + excerpt mode lines + `corpus/tools/support_check.py` + README; C3 —
  R8/R9/R10 appendices in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`.
- **Judging coverage at cutoff:** folded-in here — JCAL1 (calibration judge, read in full), JDEP3
  (depth judge, read in full), JCOV5 (coverage judge, read in full), Q2 (process, read in full), plus
  the machine receipts H3/H4/JCAL1-delta/JCAL5/JCOV3 and the updated Q1 ledger's counts; landed but
  not yet folded — CB1, H2, H4, JCAL2, JCAL4, JCOV1, JCOV2, JDEP2 (and pending seats beyond the
  cutoff). The follow-up wave was still landing after the cutoff; late arrivals should be folded by
  the integrator/L1 before closure.
- **Remaining TODOs (L1):** rule the three axes on the frozen tree (recommendations on record:
  calibration improved (bounded), coverage improved (bounded), depth sub-verdicts per JDEP3) and the
  admission mode; decide the repair list — the r90 fixtures README section (JCAL1 F6), the K1
  cross-reference into the governance table if wanted (JCOV5 ND-1), register conventions (JDEP3),
  and the process fixes Q2 names for r91; rule whether the C9 receipt-provenance nuance
  (D-c9-receipt) changes any closure text; decide the fate of the uncommitted `followup/` wave and
  the in-place `Q1-r90-debt.json` revision; commit the round record (`W2` drafts) if admitted.
- **Overall round assessment:** the declared C1/C2/C3 claims verify on the delivered tree with
  independent reproduction — freeze-then-verify PASSES with no mismatch; the census delta is exact
  (0 changed + 4 new of 164, 0 exit changes); the support command's `N/N` receipts reproduce with
  span enforcement and R9 rejection; the three appendices are decided and the register is correctly
  absent. The bounds and debts above (receipt provenance, regression invisibility, documentation
  parity, unexercised governance paths, process) are measured and left for L1 rather than netted
  away. No admission, score, or axis verdict is claimed here.

## Closure addendum (L1)

- [to be filled by L1: verdicts, repairs applied, admission decision, closure commit]

## Closure addendum (L1, 2026-10-17)

- **Lore closure commit (this round's record):** SCORECARD/LOG round-90 sections; the
  doc-parity repair (CB1's verified r90 refresh applied; source-prefix anchors re-pinned
  :343/:326/:337; chousa crossrefs landed in the canonical table — the work commit's "added"
  claim became true here; pycache gitignore + sweep; three-causes README qualified;
  capabilities row-2 evidence updated to the corpus-resident commands; fixtures README Round
  90 section), the follow-up wave's revised debt ledger, and all follow-up artifacts.
- **Post-repair census re-verified:** 164 dirs, 32/132, 0 changed — the repair batch is
  prose-only.
- **Substrate note:** the follow-up wave ran entirely on `opencode-go/deepseek-v4.1-flash`
  (hyper exhausted since r89). `/tmp` inode exhaustion shaped several seats' methods
  (documented in their reports; Q2's P3 targets it for r91).
- No push, no registry write, no sibling-repo write. L0 unchanged (K1: no new line needed).
