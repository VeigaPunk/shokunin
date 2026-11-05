# kengaku — round 93 report (hyaku run 15, attempt 1, L1 KengakuR93; fresh start)

Lane `kengaku-shokunin`, branch `master`. BASE `28e9f8bf4e8a68b1a34babfa71be9de595b78c4e` →
final lane tip **`7b8719f3eefb3f560add5dd3367b67b7a50a45da`** (`git ls-remote origin
refs/heads/master` → `7b8719f3…`, `jj-lane.sh state` → `ahead=0 behind=0`, tree clean).
Measured tip for both frozen predicates: C `22972a317185216596b3dfe1c189e98d1eb86787`.

## Work performed

Declared claims (frozen at F `d8d0a4b8`, `plans/round-93-claims.md`):
**R93-C1 — coverage** (the lowest-scoring non-retired axis, held at its L0 cap 7): an eleventh
located offline replay of a pinned Terminal-Bench 2.0 grader, `schemelike-metacircular-eval`.
**R93-C2 — calibration** (held at ceiling 10) **+ capability `freeze-integrity gate`**: a gate that
counts mismatches between what a claims file asserts was frozen and what the repository holds.

- **Fresh-start reading.** Rounds 90/91/92 were `rejected-honest-stop` (MANIFEST 1333, 1342, 1361;
  spot-checks `corpus/lessons/round-9{0,1,2}-verifier-spotcheck.md` read). Root failure shared:
  instruments edited after freeze / after first scored run (r92 M8), and a host-irreproducible
  control (r92 M13). Round order chosen to answer it: P1 instruments `17cb9337` → P2 controls
  executed against P1 `0e77e98f` → F frozen claims with a 9-row `frozen-instruments` sha256
  table `d8d0a4b8` → official receipt + ledger flip + SOURCES C `22972a31` → measurement. No
  tabled instrument changed after F (`.ufo/waves/round-93/L1/c2-tip.txt` W4 `summary=(9, 9, 0)`;
  confirmed by three wave seats).
- **Member choice from the ledger's class arithmetic.** Opened four candidates live:
  `query-optimize` (ledger `external-db-required`), `financial-document-processor` (S295,
  rejected), `large-scale-text-editing` (S296, rejected: vim absent, pacman paused),
  `schemelike-metacircular-eval` (chosen: `timing-wall` was the thinnest class, 3 of 9).
  All 139 task files fetched, HTTP 200; capture `corpus/evidence/round93/graders/schemelike-metacircular-eval/` (P1).
- **Probe** `plans/round93_scheme_probe.py` (P1): bwrap with tmpfs root (host `/usr`,`/etc`
  read-only, `--unshare-all`, injectable `--bwrap`), stages captured `interp.py` + an eval.scm
  variant derived from the captured reference solution, calls the grader's own `test_interp()`
  unmodified; 8 cases × 5 legs. Receipt `corpus/evidence/round93/scheme-probe.txt` (C): 8/8
  `ok=True`, mismatches 0.
- **Grader findings fixed by the cases** (receipt lines): C07 `P,-,-,-,0` — with no test programs
  `test_interp()` returns 1 before any assert, so the grader passes with no evaluator; C04
  `F,19,44,63,0` — one primitive (`*`→`+`) changed leaves 19 of 63 passing; C05 `F,0,63,63,0`
  and C08 `F,56,7,63,0` — the one-line trailing-True normalization is brittle; C06 `F,0,1,1,1` —
  the 60 s through-eval timeout wall.
- **C2 gate** `plans/round93_freeze_integrity.py` and counter `plans/round93_c2_counter.py` (P1),
  four forgery gates `plans/round93_c2_forgeries/*.py`. On the lane's real round-92 history the
  gate prints `FREEZE-INTEGRITY instruments=4 intact=1 broken=3` (round92_c2_conformance.py
  touched=4, round92_burndown.py touched=3, round91_counter_pin.py touched=1) — the breach the
  round-92 closure re-measured.
- **Pre-freeze controls (P2, `.ufo/waves/round-93/L1/controls/README.md`)**: C1 BASE rc 1 (all 9
  legs red); C1 forged ledger flip rc 1 (only L7 passes); C1 sandbox outage rc 2; C2 BASE rc 1
  (tool absent); four C2 forgeries rc 1 (always-intact W1+W2, always-broken W1+W2, bytes-only W2
  edit-revert, log-only W2 lying-table); positive: real gate W1–W3 pass at P1.
- **Dry runs before freeze** (`.ufo/waves/round-93/L1/dryrun-1.txt`, `dryrun-2.txt`, in P2): two
  mechanism-derived predictions refuted (lesson M1) and frozen as observed vectors.
- **Wave w1** (one v1 wave, 11 seats; spec/dispatch committed `fb79ef74`, results `5cc54ef5`):
  re-measurements, forgery extension, mutation test, historical freeze census, source
  re-verification, sentinel review; findings W-1…W-9 in `corpus/lessons/round-93.md`.
- **Frontier step:** SOURCES S290–S296 (C), lesson `corpus/lessons/round-93.md` (Gate, M1–M4),
  QUALITY Q73/Q74 (`5cc54ef5`).
- **Round-92 routed defects** — disposition table in the lesson: #1 claimed (C2); #5 met by
  construction (`--bwrap`, control rc 2); #2/#3/#4/#6 not claimed, routed to round 94; #7
  operator-owned.

## Landed changes

All via `jj-lane.sh` (`landed` lines); LOG.md round-93 entry covers each.

| commit | what | LOG.md |
|---|---|---|
| `17cb9337` | P1: capture, probe, case table, C1 counter, gate, C2 counter, forgeries | round-93 entry, "Order this round" |
| `0e77e98f` | P2: executed controls, dry runs, round-start census | "R93-C1"/"R93-C2" bullets (controls) |
| `d8d0a4b8` | F: frozen claims + `frozen-instruments` table | round-93 entry header |
| `22972a31` | C: official receipt, ledger flip 36→37, SOURCES S290–S296 | "R93-C1", "Sources & frontier" |
| `fb79ef74` | D: tip receipts, lesson M1–M3, SCORECARD section, LOG entry, wave spec | "Wave w1" |
| `5cc54ef5` | E: wave w1 integrated, routed findings, same-round corrections, QUALITY Q73/Q74 | "Wave w1 outcome" |
| `7b8719f3` | final-tip C2 re-run, round-end census, strace digest | "Wave w1 outcome" |

## Before → after measurements

**R93-C1** — `python3 plans/round93_c1_replay.py --lane . --rev <rev> --work DIR`
- before, BASE `28e9f8bf` (`controls/c1-base.txt`): `LEGS L1=fail … L9=fail`, `TARGET
  executed_rows=36 member=schemelike-metacircular-eval located=0 executed=0 cases=0 legs=0
  mismatches=0 defects=9`, `PREDICATE R93-C1 fail`, rc 1.
- after, measured at C `22972a31` (`L1/c1-tip.txt`): `LEGS L1=pass … L9=pass`, `TARGET
  executed_rows=37 member=schemelike-metacircular-eval located=1 executed=1 cases=8 legs=40
  mismatches=0 defects=0`, `PREDICATE R93-C1 pass`, rc 0. Class cells: timing-wall 3→4/9,
  subprocess-exec 13→14/45, stdout-inspection 11→12/29, file-artifact 27→28/76.
- Self-verdict: **met on its frozen predicate**. Independent re-runs at T: ExecC1Rerun
  (`w1/ExecC1Rerun/c1-rerun.txt`), CriticClaims (`w1/CriticClaims/receipts/`), both rc 0.

**R93-C2** — `python3 plans/round93_c2_counter.py --lane . --rev <rev> --work DIR`
- before, BASE (`controls/c2-base.txt`): `TOOL absent`, W1–W4 fail, `PREDICATE R93-C2 fail`, rc 1.
- after, measured at C `22972a31` (`L1/c2-tip.txt`): `W1 pass rc=1 summary=(4, 1, 3)`, `W2 pass`
  (5/5), `W3 pass`, `W4 pass freeze=d8d0a4b849f3 rc=0 summary=(9, 9, 0)`, `TARGET legs_passed=4
  of 4`, `PREDICATE R93-C2 pass`, rc 0. Re-run at final tip `7b8719f3`: same, rc 0
  (`L1/c2-final-tip.txt`).
- Self-verdict: **met on its frozen predicate**, with routed scope limits from the wave: three
  seat-built forgeries pass the counter 4/4 (W-1), mutants m06/m13 survive (18/25 killed, W-4),
  latent TREESAME-merge false-intact and second-block defects in the gate (W-2, W-3). None affects
  T. Capability row scoped to linear history with one table block.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
  - round start: exit **0**, `kengaku ok`, 281 registry rows (30 pre-existing W04 warnings)
    (`.ufo/waves/round-93/L1/census-start.txt`).
  - round end: exit **0**, `kengaku ok`, 288 rows (`.ufo/waves/round-93/L1/census-end.txt`).
- Rows added (all tier A, all opened 2026-11-05): admitted S290 grader, S291 interp.py, S292
  reference solution, S293 63 test programs (dataset); rejected S294 test.sh (network wrapper),
  S295 financial-document-processor, S296 large-scale-text-editing (flips stated).
- Rows touched old→new: none of the pre-existing rows; S293/S295/S296 (added this round) corrected
  in round after ScribeQuality SQ-2…SQ-4 (size 4.2 MB → 4,002,650 B; "not captured" → round-52
  capture paths; S293 recipe) — disclosed in the lesson W-7.
- Frontier rows advanced: population ledger executed 36 → 37 of 88 (TB2 grader frontier).
- Sourced claim: R93-C1 rests on S290–S293 (`plans/round-93-claims.md` "Source").
- Mistake mined: `corpus/lessons/round-93.md` M1 (mechanism predictions, shown able to fail in
  dry run 2), M2 (round-92 post-freeze edits, now measured), M3 (exit-code collision), M4
  (author-chosen forgeries bound the counter; routed).
- Assimilation: none (`merge/kengaku/` held by L0 `kengaku | round-54`). considerthese: no
  proposal taken; `considerthese/2026-11-05.md` proposal 2 (root of trust) named as the gate's
  residual in the lesson.

## Trend verdicts

- **expansion: improved** — executed ledger 36 → 37 of 88 with a new class cell move (timing-wall
  3 → 4); 4 admitted + 3 rejected rows, census exit 0 at both ends.
- **quality: improved** — a new runnable gate shown able to fail (W1 broken=3 on real history;
  battery 10/10; four forgeries red) and two lesson-backed QUALITY criteria Q73/Q74; limits:
  W-1…W-4 routed, so the operator/closure may rule `unchanged`.
- **discernment: improved** — the lane's past self-assessment mismatches are now counted by a
  command (W1: 3 for round 92; census W-8: rounds 85/86/89/91), the round's own is 0 (W4), and
  two wrong mechanism predictions were recorded rather than hidden; three of the lane's own cell
  errors were caught by its wave and corrected with disclosure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` (unchanged this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-93 entry; `corpus/evidence/round93/scheme-probe.txt`
- [~] Instructions executable by an agent without oral context — `plans/round-93-claims.md` counting commands, re-run by ExecC1Rerun/CriticClaims (`.ufo/waves/round-93/w1/`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:151`; ConnectorOverlap (`.ufo/waves/round-93/w1/ConnectorOverlap.md`): no sibling duplicates the gate, all complements

## Round shape, seats, other

- Shape: ONE v1 wave `w1`, **11 seats** (policy band 8–16): executor 3 (ExecC1Rerun, ExecC2Rerun,
  ExecFreezeCensus), scout 1 (ScoutSources), connector 1, scribe 1 (ScribeQuality), reviewer 2
  (ReviewerC1, ReviewerC2), critic 1, mutation-tester 1, sentinel 1. Attack share 4/11 = 36 %.
  No residual call. Round total 11. §3 planner seat held by the L1 (validator rejects planner);
  planning data-walk rode ExecFreezeCensus/ConnectorOverlap.
- Dead seats: **ReviewerC1** (reviewer) — empty final output, no file written, results note
  `None`; not replaced. ScoutSources wrote its fetch manifest/results (68/68 byte-identical) but
  no report.md.
- Seat-written large file: `w1/SentinelProbe/receipts/strace-main.log` (15.4 MB) not committed;
  its sha256 is `.ufo/waves/round-93/L1/strace-main.sha256`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only orchestrator
  `.scratch/` files, `.ufo/l0-questions.md` (other lanes' lines) and `w4lines.txt` (content is a
  number list naming no lane/round of mine) — none written by my seats; nothing moved.
- Scratch: `/fast/scratch/hyaku/kengaku-r93` removed after landing.
- Tool installs: none (L1 and, per their reports, all seats; ExecC1Rerun used a pre-existing
  uv-managed CPython 3.13.16). pacman untouched; no sysctl changes.
- Open L0 questions: none new; open `kengaku | round-90/91/92` lines routed around, not answered.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
