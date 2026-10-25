# mado round 35 — report

Lane: `mado-shokunin`. Round: 35 (attempt 2 of 2; attempt 1 froze the predicates and died without a report).
Campaign: hyaku (百) phases 3–6. Lane axes: coverage + operability (desktop and compositor craft).

## Work performed

**Declared claims (frozen at `19e4ab3171c1540c40d6b12097745af98053b07d` before any data, two claims on
distinct axes, both on tied-lowest non-retired axes):**

- **C1 — coverage**, the idle-lock control surface: three admitted knowledge entries and eight registry
  rows S203–S210, adopted from `shokuknow/merge/mado/` and re-grounded in-round. Counter
  `PRED-C1-r35-v1`, target `closed_entries=3 AND closed_rows=8 AND open_cites=0`.
- **C2 — calibration**, the lane's own evidence ledger: retire the r34 dead word-bound clause, split the
  `S_ISLNK`/`O_NOFOLLOW` pair, re-issue the frozen-blob ledger at the round-34 tip. Counter
  `PRED-C2-r35-v1`, target `uncovered=0 AND retired=1 AND toctou_declared=1 AND ledger_tip_ok=1`.

Round shape: **two v1 waves, 64 + 40 = 104 seats**, one batched `task` call per wave, both validated under
`scripts/hyaku/ufo-wave-policy.json` (band 32–64; wave 1 was dispatched by attempt 1 under policy v2 at 64,
wave 2 under v1 at 40). Role mix — wave 1: executor 13, scout 12, reviewer 11, critic 8, scribe 7,
connector 4, mutation-tester 3, sentinel 2, revenger 2, simplifier 2. Wave 2: reviewer 21, executor 3,
mutation-tester 3, critic 3, sentinel 2, revenger 2, scout 2, scribe 2, simplifier 1, connector 1. The §3
planner seat is held by the L1; the validator rejects a `planner` seat, so the bounded planning data-walk
rode the `connector`/`revenger` items.

- **Frozen instruments.** `c1/frozen.json` + `c1/count.py`, `c2/frozen.json` + `c2/count.py`,
  `c1/clauses.json` (9 controlled live clauses, 1 `not-load-bearing`, 1 retired), eleven committed control
  receipts under `.ufo/waves/round-35/controls/`, and the re-issued blob ledger
  `.ufo/waves/round-35/ledger/RevFrozenBlobs-r35.md`. Evidence: `.ufo/waves/round-35/registration.md`;
  freeze commit `19e4ab3`.
- **C1 data landed** at `02088b4`: `corpus/knowledge/idle-lock-never-asked-r12.md`,
  `idle-lock-chain-armed-r14.md`, `idle-lock-offered-in-the-bar-r15.md`; rows S203–S210 at
  `corpus/SOURCES.md:205-212`; eight host receipts at `.ufo/waves/round-35/fetch/S20{3..9}.receipt.txt` and
  `S210.receipt.txt`.
- **C1 measured.** `python3 -I .ufo/waves/round-35/c1/count.py --root . --frozen
  .ufo/waves/round-35/c1/frozen.json` → `closed_entries=3 closed_rows=8 open_cites=0 verdict=TARGET_MET`
  exit 0 at `02088b4`, re-run unchanged after every errata append and at the tip `7b745a1`.
- **Wave 2 falsified the instruments and the text, and both were handled honestly.** Evidence:
  `.ufo/waves/round-35/w2/reports/` (38 reports), `CritVacRecheck.md`, `RevRowsDigest.md`,
  `CritControls.md`, `RevQuoteWords.md`, `MutC2Real.md`, `RevTipLedger.md`, `RevC2Tip.md`,
  `RevQuoteS203/4/5/6/7/8/9/10.md`, `RevEntryR12/14/15.md`, `CritAxisClaims.md`, `RevLessonGate.md`,
  `RevCensus.md`, `RevIndex.md`, `RevSelftest.md`, `RevRowsUsedBy.md`, `RevCollision.md`,
  `RevQuarantineSlice.md`, `RevIdRemap.md`, `MutCensusRow.md`, `RevShonen.md`, `RevReadmeFrontier.md`,
  `RevLogEvidence.md`, `ScoutConsiderthese.md`, `SentProvenance.md`, `SimplifyRows.md`, `RevScorecard.md`,
  `RevReportShape.md`, `RevQuoteS204.md`.
  - The C1 counter is **shape-scored**: `count.py:174` computes the receipt digest and never reads it, so
    fabricated receipts at the frozen paths print `TARGET_MET`. The two cribs are committed
    (`.ufo/waves/round-35/controls-content/c1-shape-only/`, `c1-fabricated-payload/`); a one-line repair on
    a scratch copy (`.ufo/waves/round-35/scratch-evidence/L1DigestFix/count-fixed.py`) keeps the real root and
    `controls/golden` at `TARGET_MET` and turns both cribs to `TARGET_MISSED closed_entries=0 closed_rows=0
    open_cites=8` exit 1.
  - The C2 claim's **substance is falsified**: `ledger_tip_ok` scores `TARGET_MET` on the round-34 defect
    itself (stale `fa7ba113`), `uncovered=0` is fail-open on clause deletion, covered-receipts are token
    greps, and the pinned round-34 tip is disputed (`dff3941` was master for 0:17:37; the last
    round-34-labelled commit is `6d754bd`).
  - Ten append-only errata bullets across the three entries falsified or corrected five distinct claims, three of them inferences:
    "the operator never toggled" (the journal shows the daemon's scope consumed at
    `2026-10-23T19:24:38-03:00` and restarted at `22:14:11`; zero `omarchy-toggle` lines is a null
    channel), the 150 s step being a lock (`omarchy-launch-screensaver` has no lock call), and "built not
    to remember" (the toggle is process-shaped; `autostart.conf:1` re-arms it). Evidence: the three entries'
    `### Errata` blocks; `w2/reports/RevQuoteS204.md`, `RevEntryR14.md`, `RevEntryR15.md`, `RevQuoteS210.md`.
- **Census conformance.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin mado` → exit 0 before (192 rows) and after (200 rows), the same seven
  pre-existing `W04` warnings on old ids. Evidence: `corpus/lessons/round-35.md` §Gate.
- **Misroot swept.** Seat `RevLogEvidence` wrote its report at the fleet root; copied byte-exact into the
  lane, `cmp`-verified, fleet copy deleted. Recorded as M35-3.
- **Round-34 spotcheck honoured.** All four routed defects are addressed: the dead word bound is retired and
  replaced by a live `gate-quote-word-bound` clause; the `S_ISLNK` walk is load-bearing with
  `controls/c1-entry-symlink` and `O_NOFOLLOW` is declared `not-load-bearing` with its reason; the tip label
  is re-issued at `ledger/RevFrozenBlobs-r35.md`; the stale merge-package id remap stays campaign-side (L0
  `ae2c52b8`), and this round's own id work derived every id by document.
- **considerthese** mined read-only: 6 files / 41 proposals, 20 still unimplemented
  (`w2/reports/ScoutConsiderthese.md`). No proposal was implemented this round; the one proposal the round
  overlaps (the idle third of the arc gap ledger) is partially reflected and the ledger is never cited by
  the registration — recorded, not absorbed.

## Landed changes

Every change is committed inside the lane repo (jj-colocated; the helper committed and pushed):

| Commit | Carries | LOG entry |
|---|---|---|
| `19e4ab3` | the freeze: both predicates, both counters, the clause ledger, eleven control receipts, eight fetch receipts, `ledger/RevFrozenBlobs-r35.md`, `registration.md` | `LOG.md` round-35 entry, paragraph "Work" (freeze) |
| `02088b4` | the C1 data: three entries, eight rows S203–S210, the README index rows + frontier bullet, QUALITY criteria 55/56, the lesson, the wave-1 evidence and the wave specs | `LOG.md` round-35 entry, paragraph "Work" (data + counters) |
| `4f35c80` | the wave-2 falsifications as errata: three entries' errata blocks, row-cell corrections, README/frontier corrections, the committed content cribs, the 38 wave-2 reports, `scratch/L1DigestFix`, SCORECARD and LOG | `LOG.md` round-35 entry, paragraph "Then wave 2 attacked…" and "Honest notes" |
| `7b745a1` | the axis republication in the gate's own format, plus the wave-2 reports that landed after the first pass | `LOG.md` round-35 entry, "Honest notes" (the stale-publication paragraph) |
| `4efaf63` | the 235 seat evidence files checkpointed under `.ufo/waves/round-35/scratch-evidence/`; the 3.2 GB of mutant/crib working trees dropped | cleanup, not a claim: the trees were scratch, and every report's quoted command + output survives in the checkpoint |
| `b632f0b` | the last two seat reports (`SentBoundary`, `ConnOverlap`), the seats' revised reports, and the restored digest-repair receipt | the final tally in "Work performed" |
| `ca870e9`, `1bb25c7` | the seats' post-sweep revisions and rebuilt evidence folded into `scratch-evidence/` (261 files across 59 seat dirs); no scratch tree left in the lane | the cleanup paragraph |

Lane tip at closure: the tip named by `git -C mado-shokunin rev-parse master` at read time (the lane kept moving as seats finished; see the sweep list below) (`ahead=0`, working tree clean). The tip moved twelve times inside round 35 — `02088b4` data, `4f35c80` errata, `7b745a1` axis republication, then evidence-and-closure sweeps — which is the provenance defect `SentBoundary` routed.

**Evidence pin.** The C1 data is pinnable at `4f35c80`: `git diff --numstat 4f35c80..1bb25c7 -- corpus/knowledge corpus/SOURCES.md` is empty, and every later lane commit touched only documentation, seat reports and the evidence checkpoint. Wave-2 seats scored a tree that moved under them — seven round-35 commits, six during the wave — which `SentBoundary` records as the round's provenance defect: the registration froze *claims and counters*, not the list of paths the round would write, so errata and the content cribs are lane-authored files absent from its ledger. The counters were re-run after every errata append and at the tip, which is why the verdicts above are not byte-stale. (subsequent seat report revisions are named by `git log --oneline -1 -- .ufo/waves/round-35/w2/reports`)

## Before → after measurements

- **C1 (coverage).** Command:
  `python3 -I .ufo/waves/round-35/c1/count.py --root . --frozen .ufo/waves/round-35/c1/frozen.json`.
  Before, at `19e4ab3`: `closed_entries=0 closed_rows=0 open_cites=8 verdict=TARGET_MISSED` exit 1.
  After, at `02088b4` and re-run at `7b745a1`: `closed_entries=3 closed_rows=8 open_cites=0
  verdict=TARGET_MET` exit 0. Registry rows `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'
  corpus/SOURCES.md` → 192 → 200; knowledge notes → 47 → 50. **Verdict: ADMITTED, with three routed
  defects** (shape-scored counter, dead `digest` clause, pre-data `golden` rows differ from the shipped
  registry).
- **C2 (calibration).** Command:
  `python3 -I .ufo/waves/round-35/c2/count.py --repo . --frozen .ufo/waves/round-35/c2/frozen.json`.
  Before, round-34 tip: `PRED-C2-r35-v1 error=clause-ledger-missing` exit 2. After, at `02088b4`:
  `uncovered=0 retired=1 toctou_declared=1 ledger_tip_ok=1 verdict=TARGET_MET` exit 0. **Verdict: the
  counter passes and the claim's substance is falsified — NOT ADMITTED, operator ruling required**
  (`MutC2Real` M3a/M3c/M3d, `RevTipLedger` control C, `RevC2Tip` F1–F5).
- **No axis harmed (measured).** `python3 -I quality/check-index.py --repo . --rev master` →
  `MADO_INDEX: rev=… indexed=50/50 missing=0 dangling=0 duplicates=0 coverage=10.0000/10` exit 0.
  `python3 -I quality/check-axis-scores.py --repo . --rev master` →
  `MADO_AXIS: checked=3 mismatched=0 rev=7b745a1d…` exit 0 (navigation 50/50, calibration 43/43,
  operability 12/12). `bash tools/mado-verify.sh --selftest` → `MADO_SELFTEST: 460/460 assertions passed`
  (`w2/reports/RevSelftest.md`). During the 15 minutes between the data commit and the republication the
  axis gate read `mismatched=2`; that is recorded in SCORECARD, not hidden.

## Sources & frontier

**Assimilation: yes** — one theme (the idle-lock control surface), from `/home/vgpnk/Projects/shokuknow/merge/mado/`
(read-only; nothing written, no campaign tool run there).

- **Row count before → after:** 192 → 200. Command:
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → `192` at `19e4ab3`, `200` at
  `02088b4`/`7b745a1`.
- **Census before → after:** `sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` →
  exit 0 before, exit 0 after (both pasted with the seven `W04` lines in `corpus/lessons/round-35.md` §Gate).
- **Rows added by tier:** 8 rows, all `own-work`, all tier **A**, all `status=mined`, `opened 2026-10-24`
  (S203–S210). Rows touched old→new: **0** — no existing row's `status`/`recheck`/`used-by` changed; four of
  the new rows' `scope`/`teaches` cells were corrected in-round to match the entry errata.
- **Frontier rows advanced:** the idle-lock **offer** (consumer half) moves from unknown to measured ground;
  the frontier bullet is `corpus/README.md` §"Round-35 idle-lock offer route". Transitions, lock success,
  hyprlock config, rendered pixels, notification history and the operator's preference stay open.
- **Gate records:** every new row has path, access date 2026-10-24 and a located quote ≤25 words that is a
  contiguous substring of its receipt (word counts 14/13/17/13/15/14/13/15). ≥1 admit and ≥1 reject with
  reason + flip are in `corpus/lessons/round-35.md` §Gate.
- **Id remap by document:** S315→S203, S316→S204, S327→S205, S335→S206, S336→S207, S337→S208, S340→S209,
  S342→S210. The registration's own list (`S309, S310, S321, S329, S330, S331, S334, S336`) is **wrong in
  seven of eight** — recorded as M35-1 with the two-sided `comm` output (14 lines) and the mechanism (ids
  from a superseded staging base, uniform +6).
- **Id collisions:** pre-append 0 (192 vs 147); post-append 8, exactly S203–S210, because the merge package
  allocated the same ids from a 192-row snapshot to different documents. Unresolved and campaign-owned; the
  guard-can-fail proof is `assimilation/guard/collisions`.
- **Quarantine (absent-defect register):** the mado slice is 13 data rows (6 `payload-absent` + 7
  never-checked), re-derived this round (`RevQuarantineSlice.md`); **nothing adopted from the slice**, and
  two numeric collisions with S205/S209 are different documents.
- **considerthese:** mined, nothing implemented (see Work performed).

## Trend verdicts

- **Expansion — `improved`.** Registry 192 → 200 rows, notes 47 → 50, and a surface that had only scattered
  file-byte mentions now carries measured ground (setup path, chain liveness, menu, dated copies, toggles
  directory). Adjacency work ran (register-slice re-derivation, sibling scan) and stayed inside
  `PROVINCE.md`; no sibling ground was absorbed.
- **Quality — `improved`, with a named harm routed.** Depth: three entries with OBS/INF/UNK separation and
  eight sourced rows; freshness: all eight receipts re-opened and re-hashed 2026-10-24/25, 8/8 matching their
  frozen digests; operability: index gate 50/50, axis gate `mismatched=0`, suite 460/460. The harm is the
  instrument itself: C1's `TARGET_MET` is shape closure, not measurement, and C2's observables are
  fail-open. Both are recorded as criteria 55/56 and as round-36 claims rather than repaired in a frozen
  predicate.
- **Discernment — `improved`.** The round falsified its own claim (C2 not admitted), withdrew three
  inferences from its own admitted entries, entered **no** capability row (the proposed "clause-ledger audit"
  would misdescribe a fail-open instrument), and reported the 15-minute axis-staleness window it caused.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this
  round; the stated pointer resolves to `corpus/knowledge/executor-test-sufficiency.md`, which attests box 3
  more than box 1 (`w2/reports/RevShonen.md`). No named non-author verifier added.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — unchanged; `VER-M3` lives in the
  round-4 LOG block, not the round-3 block the box cites.
- `[~]` Instructions executable by an agent without oral context — unchanged; the pointer fits, independence
  is the only bar.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — unchanged; the self-audit's evidence half
  resolves, its `VER-M4B` grep does not.

No box moved, nothing was self-promoted (`grep -c '\[x\]' SHONEN.md` → 0).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none by the L1. One seat used `uv run --with fonttools` (fontTools 4.67.0, ephemeral, PyPI)
for a Nerd Font glyph-coverage check. No pacman transaction was run anywhere (host-wide pause respected).

Open L0 questions: none new. Campaign-side remains open: the merge package's staged S203–S210 collide with
the lane's S203–S210 (different documents) and must be renumbered past S210 before any future adoption; L0
`ae2c52b8` (stale merge-package id remap) still stands.

Cleanup: `.ufo/waves/round-35/scratch/` (3.2 GB of per-mutant trees, crib copies and clones) was deleted after its top-level text evidence was copied into `.ufo/waves/round-35/scratch-evidence/` (235 files plus the three late seats' trees, committed at `4efaf63` and `b632f0b`). Seat reports that cite a `scratch/...` path should read it under `scratch-evidence/`; a seat that rebuilt its scratch after the sweep had the rebuild folded in the same way. Two caveats stated rather than glossed: the checkpoint is a *snapshot* of each seat's top-level (and second-level) evidence files, not a full copy — per-mutant trees, clones and anything deeper were dropped — so a report citing a file the checkpoint does not carry must be read against its own inlined output; and a rebuild is not evidence, so a seat that reconstructed a file from its transcript should pin the hash of what it wrote, as `RevQuoteS210` did.

Dead/no-report seats: wave 2 dispatched 40; **40 wrote reports** (`SentBoundary` and `ConnOverlap` landed
last, after the first tally; the report was amended rather than the count prettified). Wave 1: 64 dispatched,
64 reports (inherited from attempt 1). No seat died and none was replaced.

The last two seats' findings: `ConnOverlap` scanned all 21 lane registries and found **no sibling holds**
`omarchy-toggle-idle`, the waybar idle indicator, `hypridle` or `omarchy-first-run` — three siblings
(tsukuroi `ADJ-03`/`OUT-004`, game-dev-3d, kotoba) route that ground to mado and none claims it.
`SentBoundary` found **no write outside the lane and the report path** (fleet containment, `shokuknow`
HEAD unchanged, no sibling repo touched) and recorded a concurrency warning that matters for every cited
number: the lane HEAD moved four times during wave 2, so a reviewer's command run at 03:29 and the same
command at 03:45 do not describe the same tree.

Reviewed-but-not-adopted capacity: `MutC1Real` ran 28 counter runs and found all ten live clauses
verdict-dead under clause-dropping on a `TARGET_MET` baseline (a degenerate polarity — each is still
killable by violating the clause, 10/10 `TARGET_MISSED`), and `SimplifyRows` proved by arithmetic that no
row may be deleted: the frozen target is a bijection over the eight sids. Both are round-36 material.
