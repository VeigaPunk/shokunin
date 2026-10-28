# tameshi — round 56 (hyaku run 11, attempt 4)

L1 `TameshiR56a4`. Lane repo `/home/vgpnk/Projects/shokunin/tameshi-shokunin`. Base
`981c5e8b20a2ada6a4f83464cff8a64fecdd9aa1`; original freeze `c3e2ca9f`, operative freeze
`21eb3c63cd0f3190c0deeb8953c6c91c7742cd68` (one pre-scoring amendment, recorded in
`.ufo/evidence/round-56/freeze.json` and mirrored in `contract.json`); content commit C0
`c0137451f5b7f22d65f748fc69f1b181f55e1378`; measured revision REV
`1b44bace0974157f6b6b969f44acd4ce7d2b1661`; lane HEAD (pushed) `c34e2b1486714ad6c1c6cbe706599ddfc9d60d55`.
Attempts 1–3 each ended without a report (watchdog `lane-dead-no-report tameshi round=56`); attempt 4
inherited their committed work and waves, swept the leftovers, ran the controls and the deciding run,
and wrote this record. Inherited-and-reused: contract, counters, gate, C0, the re-key bind
(`c1dd23b3`), waves w1/w2/w3 (108 seats, all re-verified through their committed deliverables).
Inherited-and-discarded: nothing; the uncommitted `spec-w3.json`, wave-3 deliverables, five >1 MiB
wave receipts and the lesson edit were committed as wave evidence (`caf6742a`, `888d342e`).

**Declared claims (2, frozen before data).**
- **C1, calibration** (the lowest non-retired axis, row asserted 8 while the monitor read 6): re-read and
  re-key the eighteen headings the round-55 edits cost, bind them at C0, and restate the standing row to
  the monitor's reading. Counter `.ufo/evidence/round-56/c1/measure.py`.
- **C2, operability**: `tools/receipt-revision-gate.py` bound into the lane's deciding path, the rule
  stated in QUALITY 107 / a sourced knowledge entry / SKILL `## Standing rules` / a registry cell, and the
  gate shown refusing the real round-54 and round-55 receipts. Counter `.ufo/evidence/round-56/c2/measure.py`.
Sourced claim (§2b.4): C2 rests on S281 (in-toto Statement v1), opened this round. Exploratory claims: none.

## Work performed

- **C1 — eighteen headings re-read, re-keyed, bound.** Wave-2 reader seats `T56W2Read01`…`Read18` each
  read one frozen heading at C0 and filed a report whose `section_sha256` the counter re-derives
  (`w2/T56W2Read*.json`); the frozen binder wrote one `rekey-r56-c0137451f5b7` directory into the
  round-21 ledger (`bind.sh`, `integration/binder.stdout`, commit `c1dd23b3`). 12 readers filed empty
  findings; six headings carry 13 findings that the L1 adjudicated `gap-minor` and did **not** repair
  (`integration/reader-adjudication.md`, `integration/resolutions.json`) — a repair would change the C0
  section bytes and void the readers. The 13 are stale pointers and failing examples inside the
  re-bound sections: the binding certifies a re-read, not a clean section.
- **C1 — the standing row restated.** The calibration row now says 8 at `c1dd23b3f83f`, the commit
  where the monitor reads 8; the counter's arm 6 reads it. Correction at `8c20d5c3`: the row's evidence
  cell began `Round-21`, which the frozen counter's lowercase `round-21` predicate cannot match
  (`w3/T56W3ExecControlsA.md`, `c1/measure.py:275`); the text was fixed, the counter stayed frozen.
- **C2 — gate, rule, refusals.** `tools/receipt-revision-gate.py` (19-case selftest, 11 codes), QUALITY
  criterion 107, `corpus/knowledge/receipt-revision-binding.md` (cites S281), SKILL.md `## Standing rules`
  row, registry cell — all in C0. The counter's arms 2–4 show the gate refusing the real receipts:
  round-54 `CTL_POS_c1` (`RECEIPT_REV_CONTENT_DRIFT`; the old path's `DECIDING_RUN_EXIT=0` is on record,
  `old-gate-accepted=True`), the round-54 control set (`RECEIPT_REV_UNRESOLVABLE`) and the round-55 C2
  verdict (`RECEIPT_REV_ABSENT`) — `after/c2.stdout`.
- **Controls, run to completion in two generations.** Phase A `CONTROLS_A: 7/7` (do-nothing, rekey-removed,
  fabricated reader hash, restated row 9, gate binding arm removed, fabricated receipt). The first
  phase-B run (bootstrap, PIN `8c20d5c3`) scored `CONTROLS_B: 1/2`: `CTL_POS_c2` printed
  `own=own-receipts-missing`, because C2's arm 5 reads the round's own committed control receipts, which
  cannot exist before the first controls run — a design flaw no pre-data run had caught. The bootstrap
  receipts were committed (`caf6742a`), and the same frozen `controls.sh` re-ran at `888d342e`, which
  carries them: `CONTROLS_A: 7/7`, `CONTROLS_B: 2/2` (`integration/controls-final-888d34.stdout`;
  `control/controls-{a,b}.stdout` hold generation 2, `control/BOOTSTRAP.txt` names both). No frozen
  byte moved (`FROZEN_UNCHANGED=1`).
- **Deciding run, one invocation.** `deciding-run.sh … 1b44bace … 21eb3c63` → `FREEZE_INTEGRITY: OK files=12
  amendments=1`, gate 0b `receipts=2 ok=2 refused=0 verdict=PASS`, 15/15 no-harm monitors `ok`, precheck
  `lost=0 ok`, `CENSUS exit=0`, both counters `total=0`, gate 0c `PASS`, `DECIDING_RUN_EXIT=0`
  (`.ufo/evidence/round-56/after/`, committed `18bbdab7`). Both counters were re-run at the landed
  lane tip `2fec07ec` and read `total=0` again (`integration/tip-c1.stdout`, `tip-c2.stdout`).
- **Wave findings that changed the round** (all cited to deliverables): `T56W1CritC2` found the C2 docs arm
  read the wrong SOURCES column (`C2_R56_PASS` unreachable) — repaired by amendment 1 before any score;
  `T56W2CritDoNothingC2` reached `C2_R56_PASS=true` with two 79-byte stub receipts and with a borrowed
  round-54 receipt whose `rev=` was rewritten (see C2 below); `T56W2RevSources` found the S282 gate quote
  absent from its source, `T56W2Read17` + the page-wide sweep found 57 of 61 distinct SKILL line ranges
  stale (the C0 `+13` insertion shifted 125 of 155 anchors), `T56W2Read07` found this round's own standing-rules
  table states a false code for `role=verdict --paths` (F2), `T56W3Led13` found 13 of the 18 bound entries carry
  false `external_inputs` digest labels (L1 re-derived: 13 entries, 19 labels, `SOURCES.md` 13 and `QUALITY.md` 6).
- **Source re-opens by the L1** (`integration/l1-source-reopen.txt`): S281 quote confirmed; the S282 Gate
  quote withdrawn and replaced in the lesson's errata; the DSSE candidate re-opened and excluded without a row.
- **considerthese**: `considerthese/2026-10-28.md` proposal 1 (receipt-existence linter) mined into QUALITY 107's
  revision half; the quote half is declared unmined with a demonstrating receipt
  (`w1/T56W1ScribeQuality-receipts/107-scope-gap-fabricated-line.txt`). Proposals 2–5 untouched.
- **Round shape.** Three v1 waves, **108 seats total** (band 64–128; waves 37 + 34 + 37, each inside the v1
  32–64 band): w1 `executor 10, scribe 9, reviewer 6, scout 4, critic 3, mutation-tester 2, connector 1,
  sentinel 1, simplifier 1`; w2 `reviewer 25, executor 4, critic 2, sentinel 1, mutation-tester 1, connector 1`;
  w3 `reviewer 22, executor 6, critic 3, mutation-tester 2, scribe 2, sentinel 1, connector 1`. Round role
  mix: reviewer 53, executor 20, scribe 11, critic 8, mutation-tester 5, scout 4, connector 3, sentinel 3,
  simplifier 1; attack seats (reviewer, critic, mutation-tester, sentinel) 69 of 108 = 63.9 % (≥25 %).
  Planner seat held by the L1 (validator rejects `planner`); no residual call; wave 1 dispatched by L1
  `TameshiR56` (15:41), wave 2 by `TameshiR56a3` (16:35), wave 3 by `TameshiR56a3` (17:54), every wave via the
  orchestrator's `.ready` handoff. All 108 result rows are present in `w{1,2,3}-results.json`; no seat died.
  Two seats returned a result that names a report file they never wrote to the lane: `T56W3ExecC1Run`
  (no `.md` anywhere in the lane; its result string in `w3-results.json` is the record) and `T56W3Led13`
  (wrote it at the fleet root — misroot, below). Two reader seats (`T56W2Read04`, `Read15`) first ended
  before their reports; the same identities were resumed and completed (no replacement,
  `integration/w2-resume-completions.txt`).
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): one file of this lane's
  seats at the fleet root, `.ufo/waves/round-56/w3/T56W3Led13.md` — copied byte-exact into the lane (`cmp`
  clean), the fleet copy deleted, committed in `2fec07ec`. The rest of the sweep is other lanes' or the
  orchestrator's (`.scratch/`, `lane3/`, `o.bin`, `oldrep1.out`, `oldrep2.out`) and was not touched. One
  self-inflicted misroot: an `edit` of `SCORECARD.md` with a relative path resolved against the fleet root
  and appended 18 lines to the fleet `SCORECARD.md`; reverted from `HEAD` bytes (`git diff --stat` empty
  afterwards), then applied to the lane file by absolute path.

## Landed changes

| commit | what | LOG / record |
|---|---|---|
| `c3e2ca9f`, `21eb3c63` | freeze and amendment 1 of the claim instruments | `freeze.json`; `LOG.md` `## 2026-10-28 — round 56` |
| `c0137451` (C0) | rule in SKILL `## Standing rules`, QUALITY 107, knowledge entry, SOURCES S281/S282, registry cell, before-receipts, lesson | `corpus/lessons/round-56.md` |
| `c1dd23b3`, `2f5512a8`, `8c20d5c3` | the re-key bind, the row restated, scorecard predicates corrected | `SCORECARD.md` `## Round 56` |
| `caf6742a`, `888d342e` | wave-3 deliverables, bootstrap control receipts, five >1 MiB receipts named as files | `control/BOOTSTRAP.txt` |
| `1b44bace` (REV) | final control receipts (`CONTROLS_A 7/7`, `CONTROLS_B 2/2`) | `integration/controls-final-888d34.*` |
| `18bbdab7` | deciding-run receipts, `DECIDING_RUN_EXIT=0` | `SCORECARD.md` `### Round 56 results` |
| `2fec07ec` | results: SCORECARD after rows, LOG entry, lesson attempt-4 record, swept misroot file | `LOG.md`, lesson `## Attempt 4` |
| `c34e2b14` | tip receipts (both counters `total=0` at `2fec07ec`, census exit 0) | `integration/tip-*`, `census-end.*` |

Fleet repo: this report (`fleet-commit.sh --as tameshi`). Pre-report gate:
`git ls-remote origin refs/heads/master` → `c34e2b1486714ad6c1c6cbe706599ddfc9d60d55`.

## Before → after measurements

Counting commands: `python3 .ufo/evidence/round-56/c1/measure.py --lane LANE --rev REV --work EMPTY_DIR --explain`
and the same for `c2/measure.py`, run by `deciding-run.sh` from the bytes at REV `1b44bace`
(`after/c1.stdout`, `after/c2.stdout`) and again at the lane tip `2fec07ec` (`integration/tip-c{1,2}.stdout`).

| claim | before (base `981c5e8b`, `before/`) | after (REV `1b44bace`) | verdict |
|---|---|---|---|
| C1 calibration | `credited=46 lost=18 rekeyed=0/18 readers=0/18 monitor=6/46 unstable=0 restate=8 total=5 C1_R56_PASS=false` | `credited=64 lost=0 rekeyed=18/18 readers=18/18 monitor=8/64 unstable=0 restate=8 total=0 C1_R56_PASS=true` | **measured pass.** Do-nothing controls below target: `CTL_0` total 5, `CTL_SKIP` 4, `CTL_FAB` 1, `CTL_RESTATE` 1; `CTL_POS` 0 at the revision it certifies. |
| C2 operability | `selftest=14/14 … docs=0/4 total=2 C2_R56_PASS=false` at the original freeze; `error=gate-missing total=1` at base | `selftest=19/19 red54=RECEIPT_REV_CONTENT_DRIFT red54b=RECEIPT_REV_UNRESOLVABLE red55=RECEIPT_REV_ABSENT own=PASS docs=4/4 total=0 C2_R56_PASS=true` | **reached on the counter; not admitted as a measured improvement.** The claim-sizing rule (§9) needs a target a do-nothing control cannot reach, and `T56W2CritDoNothingC2` reaches it with a stub or rev-rewritten borrowed receipt. The counter and target were not changed after data. The real refusals (arms 2–4) and the 19-case selftest are genuine; the "own receipts really came from a controls run" half is not established by any counter (digest sidecars narrow it only for honest producers). The operator rules. |

What the counters cannot see (frozen in the contract): C1 — whether a reader read its section (a
fabricated report with a computed hash passes arm 4); C2 — whether a receipt that names the certified
revision was produced by the run it claims. Two further limits found in-round: 13 of 18 bound ledger entries
mislabel `external_inputs` digests (the counter does not read them), and six headings are bound with 13
adjudicated, unrepaired minor findings. No-harm: 15/15 monitors `ok` at REV (`after/no-harm.stdout`).

## Sources & frontier

SOURCES: rows 140 → 142 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` at `981c5e8b` → tip).
Added by tier: A 2 — S281 in-toto Statement v1 (`mined`, used-by `corpus/knowledge/receipt-revision-binding.md`,
opened 2026-10-28, located quote ≤25 words in the lesson `## Gate`) and S282 SLSA build provenance (`rejected`
with reason and flip). Touched rows old→new: none besides the two additions; S283 is the next unused id.
Frontier rows advanced: the receipt-to-revision binding question (sources search log entry
2026-10-28, 3 identified / 3 screened / 1 included). The DSSE protocol page was opened and excluded without a
row (reason and flip in the lesson Gate). Corrections: the S282 Gate quote in the lesson was not in its source
and is superseded by the L1's re-opened passage (errata, `integration/l1-source-reopen.txt`).
Census (frozen manual command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`):
start `exit 0` (`.ufo/evidence/round-56/census-start.{stdout,exit}`, 16 warnings) → end `exit 0`
(`.ufo/waves/round-56/integration/census-end.{stdout,exit}`, 16 warnings: 15 W04 duplicate-URL, 1 W01 S101 tier-C; no errors).
Assimilation: none from `shokuknow` `merge/tameshi/` this round (the frozen claims did not fit a package theme);
`considerthese/2026-10-28.md` proposal 1 mined as above. Quarantine and id-collision checks therefore not applicable.
Coverage-map debt: `corpus/knowledge/receipt-revision-binding.md` is not indexed in `corpus/README.md`
(a pinned re-key input; indexing after C0 would void the readers) — no expansion credit claimed; round 57.
Mined mistakes (≥1): lesson `## Mistakes` (three round-55 classes) and `## Attempt 4` (four more).

## Trend verdicts

- **expansion: improved, narrowly.** One new tool (`tools/receipt-revision-gate.py`), one sourced knowledge
  entry, a QUALITY criterion, two registry rows (140 → 142); coverage-map index not updated, so no
  coverage-map credit. Evidence: `after/no-harm.stdout` `registry-rows-not-below-140 142`.
- **quality: improved on the monitored floor, with one named unmonitored harm.** Cold-read floor 46/64 → 64/64
  (`after/coldread-precheck.stdout`). Against that, the C0 SKILL insertion made 125 of 155 page-local anchors
  stale by 13 and the section findings above were bound, not repaired (lesson `## Round-57 deferrals`). The frozen
  no-harm monitors do not see this; the operator should rule whether it is a harm.
- **discernment: improved.** The round's own wave seats refuted the round's own claims in the open: the C2
  do-nothing attack, the false S282 quote, a false statement in the round's own SKILL table (F2), the
  mislabelled ledger digests — all recorded rather than patched post-data.

## Residuals (reported, not fixed)

- Round 57 repair list: SKILL page-local anchors (heading/function anchors, F1); SKILL byte-identity between C0
  and the deciding revision enforced in the deciding path (R1); the `## Standing rules` role→code table (F2,
  Read07); `corpus/README.md` index; `external_inputs` digest labels; the 13 adjudicated reader findings.
- Open L0 questions: none appended.
- R55.7 (a non-lane seat writing in the lane tree) stays partially disposed — the lane cannot fence a closure
  harness's own seats.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, no non-author verifier; this round changed one `## Standing rules` row whose role→code cell is false (F2, `T56W2Read07`), so the box stays `[~]` (`reports/round-1-calibration.md#box-1`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's two claims, their receipts and the deciding run are in `LOG.md` `## 2026-10-28 — round 56` and `.ufo/evidence/round-56/after/`; no independent promotion verifier
- [~] Instructions executable by an agent without oral context — input-keyed monitor restored to 64/64 `box3=true` at REV (`after/c1.stdout`); the 18 readers are lane-dispatched seats (not a non-author verifier) and 13 minor findings are bound unrepaired
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touched only lane files; the one fleet-root write (an accidental `SCORECARD.md` append) was reverted and the swept seat file moved into the lane

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none this round (no seat reported an install; no pacman use).

## Round end state

Lane HEAD `c34e2b1486714ad6c1c6cbe706599ddfc9d60d55`, pushed; `git ls-remote origin refs/heads/master` agrees.
Round verdict: **C1 measured pass; C2 counter reached but not admitted (do-nothing control reaches the target);
no frozen byte changed after data.** Non-author closure and operator rulings remain required.
