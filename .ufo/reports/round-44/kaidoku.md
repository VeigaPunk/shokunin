# kaidoku — round 44

## Work performed

Declared claims, frozen at `c48f8a4bfd449300c975668e59aae5b5538b6a84` (`plans/round-44-claims.md`):
**R44-C1 — coverage**, moving `squashfs_v1`/`squashfs_v2` (SquashFS v1.0/v2.0, both byte orders) from
Frontier to Core through REA 6.5.0 `extract-firmware` on four committed unblob 26.6.4 fixtures with
an independent `/usr/bin/unsquashfs` 4.7.5 oracle; **R44-C2 — calibration**, a frozen 80-entry rubric
of the lane's own self-assessment statements with three concrete repairs. Owned axes coverage/depth/
calibration were tied at 10 at round start, so C1 works coverage and C2 calibration; they are
causally separable (C1 reads receipts/PROVINCE/README/its entry/SOURCES S138–S139; C2 reads
SCORECARD/SHONEN/README/SKILL and its own rubric). The L1 held the canonical §3 planner seat
(validator rejects `planner` as a swarm role); bounded planning data-walks rode scouts, connectors
and revengers.

Attempt 2 of the round. Attempt 1 froze the claims, ported both counters, ran wave 1 (37 seats),
took the C1/C2 scores, landed the C1 honest-stop documents and made 14 of the round's 15 commits,
then stopped on the run wrap-up at 09:57 (last own commit `55bcce69`). It left 74 paths dirty, and
the fleet orchestrator's non-author lane sweep committed them at 10:43:43 as `c86ea508` (author stamp
09:57:16, committer 10:43:43). This attempt re-verified every inherited artifact before reusing it (below) and
completed the round.

- **Inherited state re-verified, then reused.** Claim freeze and both counters are byte-identical to
  the freeze blobs; the four C1 after-receipts carry `parameters.output_directory` under
  `/fast/scratch/hyaku/kaidoku-r44/probe-R44C1Run/…` and evidence ids minted over that provenance;
  wave 1 is 37/37 settled in `r44-w1-results.json` with no dead seats. Re-run receipts this attempt:
  C1 at `55bcce69` → `carriers_matched 4`, `met_target false`, exit 1 (`.ufo/waves/round-44/l1/c1-score-at-55bcce69.json`);
  C2 at `55bcce69` → `entries_evaluated 80`, `mismatches []`, `frozen_path_changed []`, exit 0
  (`.ufo/waves/round-44/l1/c2-score-at-55bcce69.json`); both at the lane tip `c86ea508` → exit 2
  `frozen_path_changed` (`…/c1-score-at-tip.json`, `…/c2-score-at-tip.json`). Nothing inherited was
  discarded; the unbound v2.1 exploration assets stay excluded from the claim, as frozen.
- **R44-C1 — measured 4/4, honest stop, no promotion.** The four receipts publish every oracle
  regular file at its exact relative path with matching sha256/size and zero gaps
  (`corpus/evidence/round-44/c1/{v1le,v1be,v2le,v2be}/after.json`; counter-met precursor
  `corpus/evidence/round-44/c1/counter-at-4cc1.json`). The frozen claim nevertheless requires
  `parameters.output_directory` to name **both** a committed `corpus/evidence/round-44/c1/` path
  (controls amendment) and the `/kaidoku-r44/` scratch segment (predicate). The clause was
  **unrealized by this round's receipts**, not literally unsatisfiable (wave 2's H2 variant shows a
  composite path naming both strings scores `met_target true`; that is a naming loophole, not a
  provenance). At `55bcce69` the counter returns `met_target false`, exit 1, with
  `province_core_section`/`province_core_row`/`frontier_note` false. The alternative reading — keep
  the predicate's scratch clause as the operative one and treat the amendment sentence as describing
  the control fixture — would let the `4cc1ac11` receipt stand as `met`; the round did not take it,
  because the amendment sentence is a requirement on the receipt, not on the control, and promoting
  on the looser reading would assert a Core row the frozen claim text can be read to forbid. Both
  readings are recorded here for the non-author closure. Wave 2 supplied the causal precision
  (`.ufo/waves/round-44/w2/R44W2Preflight.md` D-5): the frozen counter implements only the scratch
  clause (`provenance_ok()` requires an absolute path containing `/kaidoku-r44/` and no `..`), so the
  `55bcce69` red is exactly the three withdrawn documentation bindings (`failing: []`), not
  provenance — the score was withdrawn under the claim text, not rejected by the instrument. The
  landing was promoted and then withdrawn: the Core row was live at `4cc1ac11`/`9d3d1862` and the
  counter returned `met_target true` at `4cc1ac11`; it was withdrawn at `55bcce69`, so "measured, not
  promoted" is a final-state statement, not a description of the intermediate state. The strict
  reading is also not literally "unsatisfiable": a composite scratch path
  (`…/kaidoku-r44/x/corpus/evidence/round-44/c1/<id>`) satisfies both prose clauses and the counter —
  a naming loophole, not a legitimate provenance. `PROVINCE.md`, `corpus/README.md` and the entry now
  record "measured, not promoted" (`55bcce69`). Two further C1 limits are carried: the counter-time
  REA rerun stops a census-only authored envelope but a projection-matched authored envelope passes
  every carrier clause (R44-CL3, still open), and the claim's clause binding the runner's tree to the
  committed evidence copy is unimplemented — the counter reads only `after.json` (R44-CL8;
  `w2/R44W2C1PosArm.md`, `w2/R44W2C1Satisfy.md` D-2).
- **R44-C2 — met at the measured revision.** The three `## Owned axes` statements (coverage count,
  depth count, craft range) are corrected with dated `c2-correction` markers appended to
  `SCORECARD.md`; the frozen 80-entry rubric re-derives every asserted value at `55bcce69` with
  `mismatches []` and exit 0 (the committed receipt `corpus/evidence/round-44/c2/c2-score-9d3d.json`
  measures `9d3d1862`, exit 0; the `55bcce69` derivation is the re-run
  `.ufo/waves/round-44/l1/c2-score-at-55bcce69.json`).
- **Freeze-integrity defect found and fixed (M44-2).** Attempt 1 mutated 8 files under the frozen
  `tools/round-44/control-fixtures/` in the worktree at 09:50 — seven minutes before its honest stop,
  so the graded surface was already non-frozen while `55bcce69` scored — and the fleet sweep
  committed them at 10:43:43 as `c86ea508` (it added no file under `tools/round-44/`). Both counters
  exit 2 at the tip (`c86ea508` and the current `8bb1090a`; C1 lists 8 paths, C2 lists 8 after the
  M44-3 revert of the SCORECARD append); C2 evaluates 0 entries there, and a 2 counts toward no
  target. The 8 files are the positive control's four receipts, its knowledge-entry
  fixture and two manifests — regenerated control inputs — so the control ledger is reproducible only
  at or before `55bcce69` and no control arm can run at the tip. The admissible measured revision is
  therefore `55bcce69` — the last clean ancestor — and the round says so instead of scoring at the
  tip. Candidate fix (unwired, pathspec-scoped script): `tools/round-45/frozen-path-preflight.py`, shown
  red at `c86ea508` (exit 1, 8 touched paths, `.ufo/waves/round-44/l1/preflight-c86ea508.json`), red
  at the current tip `8bb1090a`, and green at `55bcce69` (exit 0, `…/preflight-55bcce69.json`), plus
  green on all 12 claim frozen pathspecs at `55bcce69` and red on them at `c86ea508`; criterion
  QUALITY 86. Blind spots named: a pathspec matching nothing at FREEZE green-lights, the no-pathspec
  default evaluates only the commit walk, and there is no dirty-tree arm. Wave 2 attacked the gate itself
  (`R44W2Preflight.md`): correct on merge, evil-merge, `-s ours`, mode-only, delete/rename and
  modify-then-restore cases; defects D-1 (a pathspec matching nothing at FREEZE green-lights), D-2
  (the no-pathspec descent is undocumented) and D-3 (the tool is not wired into the commit sequence)
  are routed to round 45.
- **Record landed.** `corpus/lessons/round-44.md` (mistakes M44-1 `stale-premise` and M44-2
  `freeze-violation`, each with a fix shown able to fail; Gate with S138/S139 URL+date+≤25-word
  located quote, one admit and one reject arm; routed defects R44-CL1…CL6; all 28 debt ids
  re-listed), `LOG.md` round-44 entry, `SCORECARD.md` `## Round 44` section with the planned
  round-45 item, `corpus/QUALITY.md` row 77.
- **Round shape.** Two v1 waves under `scripts/hyaku/ufo-wave-policy.json` (band 32–64, `maxLanes`
  256). Wave 1: 37 seats, settled 37/37, 0 dead (`.ufo/waves/round-44/w1/`, `r44-w1-results.json`);
  roles executor 8, scribe 8, scout 7, reviewer 4, critic 3, connector 3, revenger 1, sentinel 1,
  mutation-tester 1, simplifier 1 (wave-1 settlement is a post-freeze fact: the results file is
  committed in `c86ea508`). Wave 2: 42 seats attacking the landing and the record, 17
  attack-role seats (reviewer/critic/mutation-tester = 40.5%; round 25/79 = 31.6% on the policy's
  attack set), dispatched 2026-10-28T11:18:59-03 in one `task` call from
  `.ufo/waves/round-44/w2.ready`, WAVE-DONE received; **42/42 settled, 0 dead**, results
  `.ufo/waves/round-44/r44-w2-results.json`. Round total 79 seats, no residual call
  (`.ufo/waves/round-44/w2/R44W2ScribeSeats.md` §1 re-derives every number from the
  spec/dispatch/registry files).
- **Wave 2 (falsification).** 42 seats attacked the landing at `55bcce69` and the record, one seat per
  item, reports under `.ufo/waves/round-44/w2/`. Confirmed independently: the C1 score values
  (`carriers_matched 4`, `met_target false`, exit 1, `failing []`, `frozen_path_changed []`, counter
  blob equal at freeze and REV; `R44W2C1Rescore.md`); the C2 score (80 evaluated, `mismatches []`,
  exit 0; `R44W2C2Rescore.md`, `R44W2Preflight.md`); the four receipts' published sets against the
  `unsquashfs` oracle (`R44W2C1ReceiptAudit.md`, `R44W2C1Oracle.md`); S138/S139 live upstream with the
  manifest digests reproduced 10/10 (`R44W2Sources.md`); census 137 → 139 and schema (`R44W2Census.md`);
  `Assimilation: none` (`R44W2Assim.md`); no misrooted seat file (`R44W2Misroot.md`); attempt 1's
  timeline and the fleet sweep commit (`R44W2RevAttempt1.md`); the toolchain all pre-existing
  (`R44W2ScoutTool.md`). Falsified or corrected, and acted on in the record: the "unsatisfiable / no
  real run" sentence (wave-2 H2 shows a composite path scores `met_target true` —
  `R44W2C1Satisfy.md` V5), the causal reading of the `55bcce69` red (the three withdrawn document
  bindings, not provenance — `R44W2Preflight.md` D-5), the commit attribution of `c86ea508` (attempt
  1's dirty tree, committed by the fleet sweep — `RA-1`), the SCORECARD append as a second violation
  (reverted, `R44W2C1Satisfy.md` D-3 / M44-3), the QUALITY row number (renumbered 86/87,
  `R44W2Quality77.md`), the claim's unimplemented runner tree-binding (`R44W2C1Satisfy.md` D-2 /
  R44-CL8), the counter's partial immunity to a projection-matched envelope (`R44W2C1PosArm.md` /
  R44-CL3), the freeze set narrower than the claim (`R44W2C2Freeze.md` F-1..F-3 / R44-CL7), the
  freeze-tree-scoped observables (`R44W2ConnDefects.md` R45-07 / R44-CL9), the preflight gate's own
  blind spots (`R44W2Preflight.md` D-1..D-3), and C2's bound-edit arm not implementing "a later
  restore does not un-block" (`R44W2Distill.md` C-3 / R44-CL10). The last two seats also corrected the
  record: the entry and lesson cited the oracle manifest's digest as `4bc53dbb…` where the committed
  file hashes `06a72dd5…` (`R44W2Record.md` D-1 — entry corrected in `1eab9950`; the entry is not a
  frozen path), the QUALITY rows are now table rows 86/87 rather than appended bullets (D-2), the
  round-start census is 13 W04 warnings (D-3), and two LOG citations were repaired (D-5, D-6). No
  wave-2 finding overturned either claim verdict at the measured revision (`R44W2Record.md` §2:
  "reproduces exactly").
- **Frontier step.** `corpus/SOURCES.md` 137 → 139 rows (S138 unblob `__output__` expected trees,
  tier A dataset; S139 squashfs-tools releases, tier A docs/tool), both opened in-round and both
  cited by the C1 entry; census exit 0 at round start and end; assimilation `none`;
  `considerthese/` absent (`.ufo/waves/round-44/w1/R44Quarantine.md`, `R44SrcOracle.md`).

## Landed changes

Every lane change is recorded in `LOG.md` (`## 2026-10-28 — round 44`) and lands on the lane's `main`
branch through `jj-lane.sh`:

- Exploratory v2.1 assets and the frozen carriers/oracle: `b33a4738`, `c1ff9e89`; wave-1 probe
  receipt: `2081dc06`; freeze-review corrections: `7ed97668`, `b2a1bd91`.
- Claim freeze, counters, rubric, controls and `tools/round-44/`: `c48f8a4b`.
- C1 REA receipts: `fee6e98a`; C1 evidence and coverage mapping: `4cc1ac11`; C1 Core docs and the
  three calibration corrections: `9d3d1862`; score receipts: `75a5cb42`; frozen control receipts:
  `e9e3abd1`; C1 honest stop: `55bcce69`; post-freeze control fixtures and unsettled wave evidence:
  `c86ea508`.
- This attempt: lesson, `LOG.md` (which carries the round-44 claim ledger), `QUALITY.md` 86 and 87,
  `tools/round-45/frozen-path-preflight.py`, the wave-2 spec/dispatch and the measured-revision
  receipts: `8bb1090a`. That commit also appended a `## Round 44` section to `SCORECARD.md`, which the
  frozen C2 rubric binds as an exact 8-line append; wave 2 caught it as a second
  `frozen_path_changed` path (M44-3), and the final commit restores `SCORECARD.md` to the
  `55bcce69` blob with the ledger in `LOG.md` (the rubric's own note authorises landing it
  elsewhere).
- Wave-2 integration and the final lane commit: see below.
- Record corrections (attribution, C1 cause, C2 limits, QUALITY 86/87) and the `SCORECARD.md`
  revert: `923fa87`; wave-2 evidence and the final-tip score receipts: `f370592`; the last wave-2
  artifact: `4503fb78`.
- Late-seat integration (wave-2 `Record`/`Distill`): `1eab9950`.
- Final lane commit: `1eab9950cd9e586f6010cdea3e6ab61f0d327ec8`;
  `git -C kaidoku-shokunin ls-remote origin refs/heads/main` returns it.

## Before → after measurements

- **R44-C1 (coverage) — not met; honest stop, measured 4/4.** Before: at the freeze the counter exits
  1 with `carriers_matched 0` and every documentation binding false (CTL-C1-0 and six counterfactual
  reds plus one positive arm, `.ufo/waves/round-44/controls/summary.json`, `e9e3abd1`). Receipt
  revisions: `controls/summary.json` and `l1/c1-score-4cc1.json` live at `c86ea508` (the fleet sweep),
  so a reader re-deriving `55bcce69` will not find them there. After:
  `carriers_matched 4`, `met_target false`, exit 1 at `55bcce69` — every carrier binding true, the
  three documentation bindings false because the frozen output-directory clauses cannot both hold.
  Counting command: `python3 -I -B tools/round-44/c1-counter.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev 55bcce69c2f4854958d054bcab6d5f0c6fb8a6ac --freeze c48f8a4bfd449300c975668e59aae5b5538b6a84 --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --work <SCRATCH> --json-out <OUT>`.
  Measured at `55bcce69`; receipt `.ufo/waves/round-44/l1/c1-score-at-55bcce69.json`.
- **R44-C2 (calibration) — met at `55bcce69`.** Before: the rubric's base census carries the three
  named mismatches (coverage count `133/133` vs 137/137, depth count `20/20` vs 21/21, craft range
  `81-449` vs `81-543`) with the per-entry verdict vector in the frozen rubric census
  (`.ufo/waves/round-44/controls/c2/receipt.json`). After: `entries_evaluated 80`, `mismatches []`,
  `frozen_path_changed []`, `met_target true`, exit 0. Counting command:
  `python3 -I -B tools/round-44/c2-counter.py --root <LANE> --rev 55bcce69 --freeze c48f8a4b --work <SCRATCH> --json-out <OUT>`.
  Measured at `55bcce69`; receipt `.ufo/waves/round-44/l1/c2-score-at-55bcce69.json`. Limits stated:
  (i) the same claim is inadmissible at the lane tip (`c86ea508` and later) under its own freeze
  rule — see the freeze-integrity paragraph above; (ii) the instrument's freeze check is narrower
  than the claim's `## Frozen paths`: six claim-frozen families, including
  `plans/round-44-claims.md` and `corpus/SOURCES.md`, score green under a post-freeze mutation, so
  `frozen_path_changed []` certifies the instrument's set, not the claim's clause
  (`R44W2C2Freeze.md` §2–§3; routed R44-CL7); (iii) the three corrected observables are
  **freeze-tree-scoped** — at `55bcce69` command A derives 138/138 because C1's entry landed, and the
  lane's older REV-evaluating R38 counter exits 1 with five mismatches there; the frozen rubric
  evaluates that surface at the freeze tree by design, so the score stands and the scope is stated
  here rather than implied (wave-2 R45-07; routed R44-CL9). The 80/80 values themselves are
  unaffected — `git log c48f8a4..55bcce69` over those paths is empty.
- **Owned-axis observables (command A at the tip `c86ea508`).** `knowledge_files=138`, `mapped=138`,
  `missing []`, `dangling []`, `coverage_score 10.0`; `rule_blocks 21`, `citation_resolved_rules 21`,
  `depth_score 10.0` (recipe: `SCORECARD.md` `## Measurement recipes` command A). Round start
  `c29360e3`: 137 knowledge files, 137 mapped. Calibration's moving quantity is the 3 → 0 mismatch
  count over the frozen 80-entry rubric.

## Sources & frontier

- `corpus/SOURCES.md`: **137 → 139 rows**. Counting command:
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (137 at
  `c29360e3ba5381a5ab69e372d0d9577970f85018`, 139 at the tip). Round-start census
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
  → `kaidoku ok`, exit 0, 14 W04 duplicate-URL warnings; round-end receipt
  `.ufo/waves/round-44/l1/sources-census-end.txt` → `kaidoku ok`, exit 0, the same 14 warnings
  (S138's W04 is a within-scope URL already cited by an evidence pointer, not a duplicate id).
- Rows added by tier: **tier A: 2** — S138 (unblob 26.6.4 SquashFS `__output__` expected trees,
  dataset; 22 members fetched, manifest `corpus/evidence/round-44/oracle/manifest.json`, `failures: []`)
  and S139 (squashfs-tools releases, docs/tool; grounds `/usr/bin/unsquashfs` 4.7.5). Both landed in
  the freeze commit `c48f8a4b` with `used-by` naming `2026-10-28-r44-squashfs-v1v2-core`.
- Rows touched old→new: **none** — no existing row's `status`, `recheck` or `used-by` cell changed in
  `c29360e3..55bcce69`.
- Frontier rows advanced: **none** — R44-C1 stopped, so `squashfs_v1`/`squashfs_v2` remain Frontier;
  `PROVINCE.md` and `corpus/README.md` say "measured, not promoted". Still Frontier:
  `squashfs_v2_nonstandard`, `squashfs_v3_broadcom`, `squashfs_v3_nonstandard`, gzip v3 bodies, v4
  Broadcom, LE AVM members, AVM kernels, nested sub-images below depth 1.
- Assimilation: `none` — the kaidoku package has no round-44 entry, and the five-row quarantine slice
  was re-derived byte-identically to round 43 (sha256 `7383a90e…28e6a`) with all five rows hand-checked
  live (S150 fabrication-class, S113/S136/S147 present-with-anchor, S117 unverifiable); none appended.
- `considerthese/`: absent in this lane.

## Trend verdicts

- **Expansion — improved.** One new knowledge entry on previously unmapped handler-family ground
  (`corpus/knowledge/2026-10-28-r44-squashfs-v1v2-core.md`) plus two admitted tier-A sources
  (S138/S139), with the honesty that the entry records a measurement, not a promotion
  (`55bcce69`).
- **Quality — improved.** Two instrument defects the round had walked into are now named with
  executable evidence and one is fixed with a demonstrated red/green gate: the claim's
  output-directory contradiction (R44-CL2) and the post-freeze write into a frozen directory
  (M44-2 → `tools/round-45/frozen-path-preflight.py`, QUALITY 86); the round also refuses the 4/4
  precursor as a promotion (`55bcce69`, `.ufo/waves/round-44/l1/*.json`).
- **Discernment — improved (lane-internal evidence only).** The round demoted its own green
  precursor score and disclosed that its tip fails its own freeze rule instead of reporting the
  tip score; the C2 rubric's 80 entries were re-derived rather than asserted. Dispatched seats are
  the lane, so the non-author closure spot-check remains required and no outside verifier is claimed.

## SHONEN

- [~] Box 1 — decision tables, error patterns, checklists with citations: `SKILL.md` rule blocks
  21/21 cite resolvable ranges (command A at `c86ea508`); the round's new instrument is
  `tools/round-45/frozen-path-preflight.py` with a red/green pair (`.ufo/waves/round-44/l1/preflight-*.json`).
- [~] Box 2 — end-to-end domain task logged in LOG.md: four frozen SquashFS v1/v2 fixtures through
  REA 6.5.0 `extract-firmware` against `unsquashfs` 4.7.5, 4/4 carrier match
  (`corpus/evidence/round-44/c1/`); `LOG.md` round-44 entry; honest stop on promotion.
- [~] Box 3 — instructions executable by an agent without oral context: the two frozen counters, the
  six-plus-one C1 controls and the 80-entry C2 rubric run from committed bytes with documented exit
  codes (`tools/round-44/`, `.ufo/waves/round-44/controls/`); a fresh attempt re-ran both counters
  at the measured revision and reproduced the recorded verdicts.
- [~] Box 4 — no cross-domain bleed: `PROVINCE.md` Frontier language now says measured-not-promoted
  for `squashfs_v1`/`squashfs_v2`; the `## Adjacent` refusal region is untouched; no safety or
  compatibility claim is made (S139 grounds tool identity only).

**Stale-lane:** progressing — launch `2026-10-28T11:09:13-03:00` (driver `hyaku-inline`,
`attempt=2` for round 44); lane commits land through `1eab9950`; no other mission of this lane is
open. Both waves settled before this report: wave 1 37/37, wave 2 42/42 (WAVE-DONE received), 0 dead
seats, no residual call. One process note: the run hit its request budget while the last two wave-2
seats still ran, so they were asked to settle and their findings (`R44W2Record.md`,
`R44W2Distill.md`) were integrated into `1eab9950` before filing; no report number rests on an
unsettled seat.

**Non-author closure:** the integrator's spot-check landed as lane commit `e1724c32`
(`corpus/lessons/round-44-verifier-spotcheck.md`) on top of `1eab9950`. It re-ran both frozen
counters at `55bcce69` and confirms both verdicts; it adopts the same falsifier corrections recorded
above (the exit-1 cause is the three withdrawn bindings, "unsatisfiable" is false, C2's restore clause
and freeze set are unimplemented); its one conformance defect — the two late-seat reports and the
final LessonGate text uncommitted at judging — was resolved deliberately by `1eab9950` before its
commit, so the lane worktree is clean. The lane tip is now `e1724c32`; this attempt's last commit is
`1eab9950`. It also corrects one number: `c86ea508` swept **432 paths** (400 A / 32 M, 8 under the
frozen fixtures), not the 74 porcelain lines the record first wrote.

**Tooling:** no explicit L1 installation or upgrade and no pacman transaction by the L1 (pacman
remains paused by the operator guard). Toolchain in use, all pre-existing and re-pinned by wave 2
against `tools/round-44/carriers.json` (`.ufo/waves/round-44/w2/R44W2ScoutTool.md`): `rea-agents`
6.5.0 (npx cache, `package.json` mtime 2026-10-27), `unblob` 26.6.4 (`uv tool`), `/usr/bin/unsquashfs`
4.7.5 (`squashfs-tools 4.7.5-1`, Arch), `7z` 26.04 (`7zip 26.04-1`, which provides `p7zip`), `sasquatch`
4.5.1 (`~/.local/bin`, prior round), `diffutils` 3.12-2. `backhand`/`backhand-cli` are **not on PATH**;
the wave-1 v2ns probe used a scratch-only `cargo install --root` of `backhand-cli` 0.25.5 plus a
scratch `pip` venv (PySquashfsImage 0.9.0), both removed with their scratch trees. No host binary was
changed this round; the `npx` cache lookup touched the cache directory mtime only (round-43 note
stands: the hydration event itself is not retained).

**L0:** no kaidoku round-44 question was opened. The existing host-recovery/pacman-pause question
remains operator-owned and unanswered; nothing in this round required a pacman transaction.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` reported
`?? .scratch/closure-mado-r50.json`, `?? .scratch/source-routing-queue.md` (orchestrator-owned run
state, untouched) and `?? o.bin`, `?? oldrep1.out`, `?? oldrep2.out` (not this lane's: a 5,867-byte
HTML page dated 2026-10-27 and two host health-check outputs dated 2026-10-28 09:10, none containing
`kaidoku` or `round 44`). No seat-authored round-44 file was found at the fleet root.
