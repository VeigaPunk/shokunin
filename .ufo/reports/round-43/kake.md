# kake round 43 — report (attempt 1 of 1 this session)

Lane: kake-shokunin. Round base: `61046fcffa23898cd93b7a5a0af4906dac9926c9` (round-42 closure
spot-check). Lane HEAD at report: `a377c5d0b98e7d5f28171bc47096e9592ac989a5` (settle commit;
freeze `b49cba9c`, wave artifacts `eddbbf6`, registry `7c07079`). Round 42 stays
rejected-honest-stop (C1 NOT MET; freeze-provenance defect). This round owned the routed
closure repairs and re-ran C1 under a counter frozen before ANY seat scores.

## Work performed

Declared claims (2, one per owned axis), both frozen at `b49cba9c` before any seat scored:

1. **C1 — operability**: the held round-42 build (`020bc457`, tool `914ebdee…`) meets the frozen
   counter v4 (`1c3b9661…`) on three independent seeds, and no live-seat control meets v4.
   Predicate (byte-identical in the SCORECARD section, `c43_count_v4.py:78-80` and every
   receipt): *met: the tool's exit code and output equal the round-41 tool's on every generated
   run, and its median CPU time on each of the five timing shapes is at most 2.0 times the
   round-40 tool's.* Counting command:
   `python3 -B .ufo/waves/round-43/c43_count_v4.py --root . --revision <rev> --out <receipt>`.
   **Verdict: NOT MET** — frozen kill rule (1) fires (below).
2. **C2 — freshness**: the two misroot-survivor citations (round-29 `FieldsAndCounts.md`,
   round-33 `ScoutPinsFlagAccuracy.md` at their fleet paths) declared absent; §paths gate exit
   1→0. Counting command: `node scripts/freshness-sweep.mjs --section=paths`. **Verdict:
   verified with bounds** (paths-only; before/after receipts committed).

Work items: counter v4 built from v3 by `build_v4.py` (run F + timing-shape classes per the
round-42 lesson Mistake-5 fix criteria) and frozen with nine L1 receipts
(`.ufo/waves/round-43/verification/freeze/`); C2 annotations (round-29.md:104, round-33.md:45,
pins 63→65, movement census); registry-arithmetic correction with the able-to-fail checker;
SOURCES S129/S130 (tameshi r33 verification fixtures, kama r29 self-assessment-at-writing —
sibling adjacency imports); lesson Mistakes 7–11; one v2 wave `kake-r43-w1` (66 seats)
dispatched orchestrator-inline after the freeze; settle corrections; this report.

## Landed changes

- `SCORECARD.md` — "Round 43 — C1 and C2 declared (frozen before any seat scores)"; "wave
  attack results, verdict and corrections"; "final kill-rule tally correction"
  (`a377c5d0`, freeze `b49cba9c`).
- `LOG.md` — round-43 entry + settle correction (`a377c5d0`).
- `corpus/lessons/round-43.md` — Gate (S129/S130), Mistakes 7–8 (freeze) and 9–11 (settle),
  Gate locator erratum (`a377c5d0`).
- `corpus/knowledge/claim-count-derivation.md`, `corpus/README.md` index row, S129/S130 in
  `corpus/SOURCES.md` (freeze commit `b49cba9c`).
- `corpus/lessons/round-29.md`, `round-33.md` — annotation rows; `.ufo/waves/round-30/w2/
  CriticC1Scope.md`, `.ufo/waves/round-34/w1/CriticFrontierNovelty.md` — movement-census notes
  + superseding +2 corrections (`a377c5d0`).
- `.ufo/waves/round-43/` — counter v4, build_v4.py, controls-r42 (four committed r42 control
  tools + hashes), registry_count_check.py, freeze receipts, L1 re-scores
  (`verification/l1-rescores/`), wave spec/taskCall/dispatch log with settle line, 50 seat
  reports (`w1/`), census/sweep receipts with `.exit` companions.
- Tool installs: none.

## Before → after measurements

- C1 counting command. Before (do-nothing, `ref41-base.json`, seed 43001): not met — equal
  11/11, T1 4.207, T2 1.917, T3 1.152, T4 1.228, T5 7.047. After (build ×3,
  `build-{1,2,3}.json`, seeds 9325990526163 / 265206435053987 / 269853680553917): met ×3,
  equal 11/11; per receipt: T1 1.005/1.009/1.004, T2 1.201/1.250/1.213, T3 1.334/1.318/1.327,
  T4 1.266/1.252/1.211, T5 1.105/1.144/1.215 (per-source numbers; no receipt is mixed with
  rerun maxima — routed repair 6). Reproduced by seat `ExecRerunBuild` on three fresh seeds.
  **Round verdict: NOT MET** — 27 witnessed live-seat controls meet v4 while judging URL
  values differently from the round-41 tool (head/tail windows ×5, port-length gates ×3,
  case-fold memos ×4, band memos ×5, host tables ×3, port-digit caches ×2, 48-cp prefix cache
  ×1, build mutants ×4); L1 re-scored 18 of 27 with fresh seeds, all met 11/11
  (`verification/l1-rescores/`); kill-rule receipts of record `w1/CtlHeadTail.md`,
  `w1/CtlPortLen.md`, `w1/CtlCaseMemo.md`, `w1/CtlRepeat.md`, `w1/CtlHostTable.md`,
  `w1/CtlPortValue.md` + the MutBuild* survivor sections. The four round-42 controls are all
  red under v4 (×8 reruns, `w1/ExecRerunControls`); the timing channel held (×3 failed
  attacks, `w1/CtlTiming`); the build itself remains verified on the evidence. Reported, never
  relabelled.
- C2 counting command. Before (`sweep-before.txt`): exit 1, "2 unannotated miss · 2 NOT in
  pins.pathsMissSet". After (`sweep-after-at-7c07079.txt` + `.exit`): exit 0, VERDICT OK.
- Registry arithmetic (routed repair 1): re-derived 119→128 rows, mined +7, rejected +2 at
  `1ef7a0e9`→`5949e66ffe`; freeze transition 128→130 (mined +2) receipted
  (`registry-count-r43-freeze-claims.json`, exit 0); checker red on r42 claims / green on r43.

## Sources & frontier

`corpus/SOURCES.md` rows before → after: 128 (at `61046fc`) → 130 (at `b49cba9c`); counting
commands: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` and
the CORPUS.md manual census over `git show <rev>:corpus/SOURCES.md` (both exit 0, receipts
`census-after-r43.txt` + `.exit`, `census-at-7c07079.txt` + `.exit`). Added by tier: A +2
(S129 tameshi r33 verification-fixture method, S130 kama r29 self-assessment-at-writing;
both sibling adjacency imports opened 2026-10-23, quotes verbatim — locator erratum appended
to the lesson). Touched old→new: none. Frontier rows advanced: none (S126/S127 re-opened by
`w1/ScoutReopen`: S127 byte-equal, S126 footer-clock churn only, quotes hold). Rejections:
none this round. Mined mistakes: 7–11 in `corpus/lessons/round-43.md` (7 registry arithmetic
imported from the r42 closure; 8 unannotated misroot cites; 9 stale prose numbers; 10 counter
generator defects; 11 kill-rule (3) text ambiguity). Sourced claim: C1's freeze pattern cites
S129; the registry correction cites S130 (via `claim-count-derivation.md`).

## Trend verdicts

- **expansion: unchanged** — no capability enters the SCORECARD table; registry growth is
  curation inside the existing SOURCES capability. (The 27 meeting controls are quality
  signal, not expansion.)
- **quality: improved with bounds** — counter v4 closes all four round-42 control classes
  (red ×8 reruns) and the timing channel held; the build/determinism/harm evidence reproduces
  (`w1/ExecRerunBuild`, `w1/ReviewCounterDet`, `w1/ReviewHarmUnchanged`); the wave named the
  remaining generator blind spots with witnesses and red receipts; the checker overclaim and
  the prose/number drift were disclosed (`w1/ReviewQualityV`, `w1/RevengerFreeze`).
- **discernment: improved locally (outside spot-check owed)** — 27 meeting controls reported
  by seats and confirmed by L1 re-scores, not relabelled; Mistake 9 disclosed against the
  lane's own interest; the r42 arithmetic correction re-derived independently
  (`w1/RevengerMath`, `w1/ExecCensus`).

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists with cited sources — round-43
  freeze pattern + kill-rule design committed at `b49cba9c`; wave `w1/ReviewCounterDiff`
  verified the transform byte-for-byte. (Author-side; a non-author verifier remains owed.)
- [ ] End-to-end domain task executed and logged — C1 (the repricing) is NOT MET for the
  second consecutive round; the LOG records the negative honestly.
- [~] Instructions executable without oral context — counter v4 + receipts reproduce
  deterministically from the committed bytes (`w1/ReviewCounterDet`).
- [~] No cross-domain bleed — PROVINCE untouched; `w1/ConnectorOverlap` scanned all siblings
  (S129/S130 are named imports with quotes; kama r23 named as nearest prior art).

## Round shape and waves

Shape: **one v2 wave** (policy v2 band 64–128), 66 seats, dispatched orchestrator-inline per
the round-43 inline mechanic (zero dispatches from the L1 session; the L1 validated the spec,
acquired the wave slot, and parked). Seat-role mix: attack 50/66 (75.8%) — 17
mutation-tester, 13 reviewer, 7 scout, 5 critic, 4 revenger, 1 sentinel, 1 simplifier,
2 scribe-falsify; build 16 — 14 executor, 3 scribe, 1 connector. The §3 planner seat is held
by the L1 (frozen topology); planning data-walks rode the connector/scout items. Returned:
50 reports (3 late, folded); dead 15 with no output delivered (named in the settle line,
`w1-dispatch-log.txt`); 1 live at settle (CtlPrefixCache — scratch receipt + L1 re-score
stand, report folded to closure); 0 refused. Round total: **66 seats**. No residual call
(the verdict is determined by the returned seats; further seats would be padding). Wave-slot
grant: `granted lane=kake wave=kake-r43-w1 seats=66 live=81 pending=0 cap=256`.

## Stale-lane and extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Freeze order (routed repair 2): counter, predicate, kill rules, control classes and all L1
  receipts committed at `b49cba9c`, before the wave taskCall left the lane (`w1/CriticFreezeOrder`
  conformant; `w1/RevengerCounterLineage` confirmed single-version lineage).
- Dispatch log (routed repair 4): `w1-dispatch-log.txt` carries the dispatch line with the
  wave-slot grant and the settle line.
- Per-source T2 numbers (routed repair 6): quoted per receipt above; the round-42 report's
  mixed range is corrected by this report, not by editing filed bytes.
- H4 (routed repair 3): stays qualified, in-class only (`w1/ReviewHarmUnchanged` verified the
  qualification text and that v4 changes only inputs, not the tool).
- Misroot sweep: no kake round-43 file at the fleet root; one tameshi r34 seat file
  (`.ufo/waves/round-34/w1/ReviewDevReceipts.md`, amendment-6 evidence) sits at the fleet
  root — another lane's write, left untouched and reported here.
- Open L0 questions: none appended. Operator-owned items from the r42 closure stay operator
  (foreign-authored commit `5076e26` confirmation; the exploratory-presentation option).
- Full-sweep debt (disclosed by `w1/ExecSweepFull`): §armed is red at the round base
  (PQ-2/sitemap/plazir gates) — pre-existing, outside the C2 paths-only claim, owner unchanged.

## Admission note

Every claim verifies or fails on its frozen counter: C1 fails kill rule (1) — reported, not
relabelled; C2 verifies with its disclosed bounds. No axis is observed harmed: the build,
harm H1–H5 and the round-42 rejection stand on committed evidence; round 42 stays
rejected-honest-stop. Driver completion is not admission; independent non-author verification
remains required. The r44 hardening list (generator-level long-port+defect cells,
explicit-default-port and empty-path pairs, ≥45-cp prefix cuts, non-degenerating ASCII +
non-ASCII/Kelvin fold pairs, validity-only memo and band coverage, kill-rule (3) text,
control-before-build sequencing) is recorded in SCORECARD.
