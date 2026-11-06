# chousa — round 82 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`. Base `142b6f0c08e645ef9507f6d880be44e518c39043`
(round-81 tip, closed `rejected-honest-stop`). Final lane tip **`03b586d1b8dc493623a2b758170307444bfc42be`**, confirmed by
`git ls-remote origin refs/heads/master`. L1: `ChousaR82`. Earlier attempts: none (`.ufo/watchdog.log` holds no
`lane-dead-no-report chousa round=82` line). The lane was clean at start (`jj-lane.sh state`: tracked=0 untracked=0).

## Work performed

Declared claims (frozen at `57c0d167`, `corpus/evidence/round82/claims.md`):
- **C1 operability.** This is the lowest-scored non-retired axis (historical 3/10). The claim: `tools/research-gate.sh`
  refuses the round-81 K2 forms and a declared, closed placeholder class through the SKILL.md item-2 and item-4 Run lines,
  which stay unchanged.
- **C2 depth.** Sourced on S008 (re-opened) and on S209, S210 and S211. The claim: one new knowledge entry on question
  framing, with every decision row warranted by a quote located in a capture taken this round.

Work items:
- **Fresh-start reads.** Read the r79, r80 and r81 spot-checks; their routed defects are in `claims.md` §Fresh-start.
  - Every predicate is a fixed command over committed bytes.
  - Positive controls were kept, so a gate that refuses everything still scores FAIL.
- **Egress table before any fetch.** `corpus/evidence/round82/egress-approval.md` was committed at `5d792e1e`
  (19:41:56Z). The first fetch row is 19:42:03Z (`corpus/evidence/round57/refetch.tsv:152-156`), so round-81 routed
  defect 3 is closed. Five GETs returned HTTP 200: S008, S209, S210, S211 and S028.
- **Prefreeze instruments and controls**, committed at `38f5af82` and run before the freeze; receipts are in
  `corpus/evidence/round82/controls/`, with `CONTROLS_AS_EXPECTED=14/14`.
  - Instruments: the counters `k2-gate-r82.py` and `depth-r82.py`, a 50-row C1 manifest of records, and the C2 control
    fixtures.
  - C1 controls: do-nothing, blanket-refuse, keyed-finding and keyed-Run-line. All score FAIL.
  - C2 controls: do-nothing, the r81 filler pair, fabricated quotes, stale sources, duplicate cells, four rows,
    placeholder cells and unregistered sources. All score FAIL.
  - The positive control scores PASS. The stated salad boundary also scores PASS: the counter does not check meaning, so
    that check was left to the K3 reviewer.
- **Prefreeze discovery.** R81ReviewerC2's record `r4-07` is described as "flip empty", but its bytes carry a complete
  rejection. The described defect was therefore built as `r4-07b`, and r4-07 became a positive control.
- **Candidate landing `b4a41d25`.**
  - Gate changes, with 5 new selftest cases:
    - `sweep_is_placeholder` added.
    - Sections with a heading containing "reject" are now read.
    - `SWEEP_NEGATIVE_UNRESOLVED` added for unresolved negative claims.
  - New entry `corpus/knowledge/question-framing-frames-r82.md` (11 quotes, 9 rows).
  - Registry rows S209–S211 added; S008 and S028 moved from queued to mined.
  - Crossmark addendum to the r81 correction entry; this closes routed defect 6.
  - README index updated.
- **Wave w1.** 13 seats, validated rc 0 (`.ufo/waves/round-82/w1-validate.rc`). Results are in `w1-results.json`
  (13/13 returned output). Findings:
  - **C1 K2 fired.** Records with a repeated `##` heading pass, because `load_sections` keeps only the last body
    (`R82ExecForms.md` §1–2; `R82ReviewerGate.md` F1). A placeholder claim-sweep cell also passes when a sweep row
    points back to the claim (`R82ExecRepro.md`, `R82CriticClaims.md` §4.1).
  - **C1 K3 fired.** Four record shapes that carry no K2 form are newly refused: a mixed `where` set, a Negatives carrier,
    a `why` column, and a criteria table (`R82ReviewerGate.md` F2/F3; `R82CriticClaims.md` §4.2).
  - `R82ExecHarm` checked 571 lane records. All 66 that pass at base and are refused at landing carry a K2 form, so there
    is no record-level harm.
  - **C2 K3 fired** on row 1's Never cell (`R82ReviewerEntry.md`).
  - C2 K2 held: 13 of 13 quotes are in their captures and also live (`R82ExecReopen.md`). C2 K4 held
    (`R82ScoutNovelty.md`).
  - Mutation testing: the gate patch killed 15 of 23 mutants, and the C2 counter's control set killed 5 of 11
    (`R82MutationGate.md`).
  - End-to-end trial (`R82ExecTrial.md`): a question-framing research record ran through checklist items 1, 2 and 4 and
    `verify-all`, all CLEAN. Its three mutated twins were each refused with the expected finding id.
- **Post-scoring repairs** at `51a5dee8`. These do not rescue either claim.
  - The gate now refuses duplicate sections, refuses a placeholder claim cell, drops placeholder tokens from mixed
    `where` sets, accepts Negatives carriers, and applies a schema guard to sections under a "reject" heading.
  - Selftest: 283 cases PASS.
  - Re-running the wave's attack records (`corpus/evidence/round82/repair/rerun-*.txt`): in-class records refused rose
    from 182/185 to 185/185, and the 8 reviewer and critic records went from 0/8 to 8/8.
  - Entry rows 1 and 7 repaired; S008 and S210 cells repaired; QUALITY 163 added.
- **Integration** at `03b586d1`: lesson, SCORECARD verdict and r83 plan, LOG entry, README note, and the wave evidence.
- **Planner seat.** I, as L1, held the canonical §3 planner seat; the validator rejects `planner` as a wave role.

## Landed changes

| commit (`landed`) | contents | LOG.md entry |
|---|---|---|
| `5d792e1e953649e801d9bf1f64093b1f0d4dac8c` | egress table (before any fetch) + census-start | Round 82 |
| `38f5af8268b2807811dded3d7d7221ff3f509495` | captures, refetch rows, counters, manifest, records, control fixtures | Round 82 |
| `57c0d16795db97ed09b69034e335e725ce577285` | freeze: claims, instrument pins, 14 control receipts | Round 82 |
| `b4a41d251b488f06b4a6ab01a11bc12ce72edd20` | scored landing (gate, entry, registry, README, SKILL notes) | Round 82 |
| `46dd1dc31e55c5a9133a0da47e22f8b598946cf1` | after receipts + w1 spec/dispatch/validate | Round 82 |
| `51a5dee828c55192dfe112e84d7b2f1d1d95d2cf` | post-scoring repairs, QUALITY 163, rerun receipts | Round 82 |
| `03b586d1b8dc493623a2b758170307444bfc42be` | integration + wave evidence + census-end + G02 final | Round 82 |

## Before → after measurements

| claim | counting command | before | after (at `b4a41d25`) | verdict |
|---|---|---|---|---|
| C1 operability | `D=$(mktemp -d -p /fast/scratch/hyaku) && git archive <rev> \| tar -x -C "$D" && python3 -B "$D/corpus/evidence/round82/k2-gate-r82.py" --root "$D"`; plus `bash tools/research-gate.sh --selftest` | `K2_REFUSED=0/11 HOLD_REFUSED=9/9 CLASS_REFUSED=2/24 POSITIVE=5/6` `FAIL` rc 1 (at `38f5af82`); selftest 275 | `11/11 9/9 24/24 6/6` `K2_GATE=PASS` rc 0; selftest `PASS (280 cases, 0 skipped)` | **falsified by K2 and K3 (honest stop)** |
| C2 depth | same archive; `python3 -B "$D/corpus/evidence/round82/depth-r82.py" --root "$D"` | `DEPTH_R82 entries=0` `FAIL` rc 1 | `entries=1 ok_entries=1 rows=9 located_quotes=11 fresh_sources=4` `PASS` rc 0 | **falsified by K3 (honest stop)** |

## Sources & frontier

- **Census.** Ran `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  at both ends. Start: exit 0 (`.ufo/waves/round-82/census-start.txt`). End: exit 0 (`census-end.txt`). Both show the
  same five W04 warnings that were there before.
- **Registry rows:** 208 → 211, counted with `grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`.
  - Added by tier: A +3 (S209, S210, S211, all mined).
- **Rows touched (old → new).** Every change is logged in `corpus/lessons/round-82.md` `## Gate`.
  - S008: queued → mined; anchor rewritten; used-by — → the new entry.
  - S028: queued → mined; anchor rewritten; used-by — → `correction-retraction-status-r81.md`.
- **Frontier advanced.**
  - Question framing is now knowledge. It was queued at S008 since round 1.
  - S028 is dispositioned.
  - S009, S017 and S019 stay queued.
- **Sourced claim:** C2 rests on S008, S209, S210 and S211, all opened this round.
- **Mined mistake:** the r4-07 description did not match the record's bytes. The fix is shown able to fail
  (`corpus/evidence/round82/mistake-r4-07.txt`, QUALITY 163). Two L1 mistakes are also recorded in the lesson.
- **Assimilation:** none. The `merge/chousa` package still has 111 colliding ids out of 114 staged.
- **considerthese:** read `2026-11-05.md` and `2026-11-06.md`. The open proposal ("one open Gate-record S-id per daily
  review") was not implemented; the reason is in the lesson.

## Trend verdicts

- **expansion: improved.**
  - Knowledge went from 94 to 95 entries. The new question-framing entry covers ground that no base entry or sibling held
    (K4 held; `R82ConnectorSiblings.md`).
  - The Crossmark addendum was added.
  - Registry went from 208 to 211 rows.
- **quality: improved.**
  - At the final tip the gate refuses all 185 in-class wave records, keeps every positive record passing, and passes 283
    selftest cases.
  - 66 real catches on lane history, with no harm at the record level.
  - The entry's overreach was repaired.
  - The claims themselves stay falsified.
- **discernment: improved.**
  - Both claims are filed as honest stops on the wave's own findings, without arguing the letter of the kill rules.
  - The prefreeze check caught a mis-described round-81 record before it was frozen as a control, and QUALITY 163 now
    names that class.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists and cited sources. Evidence: the item-2 and
  item-4 notes for round 82 (`SKILL.md` checklist) and `corpus/knowledge/question-framing-frames-r82.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence:
  `.ufo/waves/round-82/w1/R82ExecTrial.md`, LOG Round 82.
- [~] Instructions executable by an agent without oral context. Evidence: `corpus/evidence/round82/after/` and
  `repair/k2-gate-repaired.txt`.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `.ufo/waves/round-82/w1/R82SentinelScope.md` and
  `R82ConnectorSiblings.md`.

## Extras

- **Round shape:** one v1 wave of 13 seats (band 8–16) and no residual call, so the round total is 13.
  - Roles: executor ×5, reviewer ×2, and one each of critic, mutation-tester, scout, connector, scribe and sentinel.
  - Attack seats: 4 of 13 (31%). Connector seats: 1.
  - Dead seats: 0.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Misroot sweep:** ran `git -C /home/vgpnk/Projects/shokunin status --porcelain`. No untracked fleet-root file comes
  from this round; `.scratch/run15-wrapup/` belongs to the orchestrator and was not touched. Scratch
  `/fast/scratch/hyaku/chousa-r82` was removed.
- **Open L0:** nothing new. The general fetch-scope question `8d77e6c1` is still open; this round routed around it with
  the egress table.
