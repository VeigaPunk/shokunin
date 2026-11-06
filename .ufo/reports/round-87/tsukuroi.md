# tsukuroi — round 87 report (attempt 2)

L1: TsukuroiR87a2 (attempt 2). Attempt 1 (L1 TsukuroiR87) froze the claims, landed the candidate and the entry,
and dispatched wave w1. It ended mid-wave when the orchestrator kernel restarted (watchdog
`lane-dead-no-report tsukuroi round=87`, 20:22:42 -03). Attempt 2 inherited the uncommitted lesson draft, the
uncommitted QUALITY 124 draft and all w1 files. It re-checked each one before use: the drafts were rewritten
before landing, and the w1 files are landed as wave evidence. It received WAVE-DONE for w1, integrated the wave,
measured, and landed the round. Lane `master` tip: `3ba37eb0a3c2b17e535bb68891cf63047f4fbce8`. `git ls-remote origin
refs/heads/master` prints this hash.

## Work performed

Declared claims, frozen by attempt 1 at `5eb8b157` and run unchanged (`SCORECARD.md` "Round 87 — declaration"):

- **C1 (measured; operability; sourced S350–S353).** `tools/check-limine-pins.py` implements the frozen Limine
  v12.9.4 pin rule set R1–R7. Target: 22/22 families in three consecutive runs of
  `tools/limine-pin-battery-r87.py` at the landed tip.
- **C2 (exploratory; depth).** Knowledge entry `corpus/knowledge/limine-pin-plane-r87.md` (+ `.json`), rows
  LP1–LP8. Verdict comes from a non-author `unprovable-but-better` judgment (the hyaku closure).

Work items:

- **Rejection-history and spot-check reads.** Attempt 1's lesson table covers r86 spot-check routed 1–5
  (`corpus/lessons/round-87.md` "Inputs read"). Attempt 2 closed routed 3 with the append-only `R87-REG-1` block
  (`SKILL.md` "Round-87 correction"). Routed 4 is mistake M2 below; this report is filed once.
- **Wave w1 integration** (`.ufo/waves/round-87/w1/`; seat final texts recovered from the session store into
  `w1/finals/`, because `w1-results.json` holds no output after the restart):
  - ExecReplicate: C1 replicated 22/22 ×3 in a clean room at `cefb4188`. All 25 freeze controls match their frozen
    counts (`w1/ExecReplicate.md` §2–3). It found two out-of-predicate risks: ESP path traversal and non-UTF-8
    bytes.
  - ReviewGate: patch plus probe suite (`w1/ReviewGate/proposed-patch.diff`). Landed byte-identical to
    `w1/ReviewGate/check-limine-pins.proposed.py` at `46d48a71`.
  - ReviewEntry: 6 rows support, 2 partial (LP2, LP5). It also found an anchor gap on LP7/S354 and an unpinned
    trunk sentence in Limits (`w1/ReviewEntry.md` F1–F4). All four were fixed at `46d48a71`.
  - ExecLints: registry gap 136/138 (`w1/ExecLints.md`). Rows landed and corrected; now 138/138.
  - ScribeLesson: drafts of QUALITY 124 (repaired), M1/M2 and R87-REG-1 (`w1/ScribeLesson/`), all landed.
  - MutGate: 26/30 gate mutants killed. m05, m24 and m25 are battery gaps; m01 is equivalent
    (`w1/MutGate/receipts/mutants-table.md`). Routed as R87-R5.
  - MutBattery: battery `--selftest` survivors M3–M7, fixture answer leaks, and a reference-delegating forger that
    reads 22/22 (`w1/MutBattery.md` §2–6). Routed as R87-R1..R3, because the battery is frozen.
  - CriticClaims (receipts only): 17 one-clause forgers written from the battery docstring. Ten of them (g01–g08,
    g10, g14) read 22/22 in all three runs (`w1/CriticClaims/receipts/*.json`). This is mistake M3 and QUALITY 125.
- **Residual clause probe, run by the L1 outside the counter** (`.ufo/waves/round-87/after/residual-diff/`). On 11
  inputs, each of which separates one forger from CriticClaims' independent base gate, the candidate gate equals
  the base 11/11. The pre-hardening gate also reads 11/11. With forgers g07, g10 and g01 as the candidate, the
  probe disagrees on 1, 2 and 1 inputs respectively, rc 1 each (`controls.txt`), so the probe can fail.
- **Sources.** S350/S354 anchors corrected. Limine trunk `CONFIG.md` and `common/lib/uri.c` re-opened; they stay
  rejected for this host and are kept as context only (`.ufo/waves/round-87/after/src-trunk/`).
- **Live host check, read-only, one `sudo` step.** `--live` at the tip reads rc 1, `LP-MISMATCH` on lines 30 and 38
  with consequence `prompt`. The `/boot` b2sum list digest is `0f6acc28…` before and after, and `cmp` reports the
  lists identical (`.ufo/waves/round-87/after/live-receipt-landed.txt`).
- **Planner seat:** held by the L1 (the validator refuses `planner`).

## Landed changes

Every change is in LOG.md "Round 87" (the attempt-1 freeze, candidate and entry blocks, and the attempt-2 block).

| Commit | Content |
|---|---|
| `5eb8b157` | freeze: battery r87, pinned Limine v12.9.4 and binutils sources, controls ×3, declaration (attempt 1) |
| `a097bd9d` | candidate `tools/check-limine-pins.py` (attempt 1) |
| `cefb4188` | entry LP1–LP8, SOURCES S350–S354, first live receipt (attempt 1) |
| `46d48a7115fd19156f8916e72e8c460968d32f44` | gate ESP confinement, UTF-8 handling and usage exit 64; entry LP2/LP5/LP7/Limits fixes; S350/S354 anchors; registry rows and R87-REG-1; QUALITY 124 repaired; w1 evidence and seat finals; residual probe; trunk context |
| `3ba37eb0a3c2b17e535bb68891cf63047f4fbce8` | measured outcome; lesson (Gate addendum, w1 summary, Mistakes M1–M3, routed R87-R1..R6); QUALITY 125; LOG; README frontier; live and census receipts |

## Before → after measurements

- **C1** — `python3 tools/limine-pin-battery-r87.py --gate tools/check-limine-pins.py`, measured at `46d48a71`.
  - Before (freeze `5eb8b157`): do-nothing K1 (gate absent) 0/22 ×3; K2 (lane boot-chain gate) 0/22 ×3; forgers
    f1–f4 at 0/0/2/6 out of 22; near-miss controls N01–N18 at 1–21/22; reference P0 22/22
    (`.ufo/waves/round-87/before/controls/controls-summary.txt`).
  - After: 22/22 `met` rc 0 in three consecutive runs, in a clean clone at the tip
    (`.ufo/waves/round-87/after/measured/c1-receipt.txt`, `c1-run{1,2,3}.json`).
  - Battery sha256 `f2551c8e…989d` equals the freeze manifest. Gate sha256 at the tip is `e3b0fab4…7352`.
    Self-tests: gate 15/15, battery 5/5, both rc 0.
  - Verdict: **met** on the frozen predicate. The 10 R1–R7 clauses bent by CriticClaims' forgers g01–g08, g10 and
    g14 are uncertified by this counter (M3, QUALITY 125).
- **C2** — exploratory, no counting command. Before: `git grep -n -i 'hash_mismatch_panic\|uri_resolve' 220c86e3 --
  corpus/knowledge tools` is empty. After: entry LP1–LP8 at `46d48a71`. Verdict: pending the non-author closure.
  ReviewEntry is a lane seat and is advisory only.

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
  - Before: pre-round tip `220c86e3`, replayed on a full archive (`after/census-before-replay.txt`): rc 0,
    349 rows, 52 W04. Attempt 1's live round-start capture (`before/census-before.txt`) shows the same 52 W04 and
    no E code, but did not record the rc.
  - After: tip `3ba37eb0`: rc 0, 354 rows, 52 W04, `tsukuroi ok`.
- **Rows added by tier:** A +5 (S350–S354, `mined`).
- **Rows touched, old → new:** S350 anchor gains `267-268, 272-274`. S354 anchor `189-190` → `188-191`.
  Status, recheck and used-by are unchanged.
- **Rejected:** Limine trunk `CONFIG.md`, re-opened with trunk `uri.c` raw 92, kept as context (lesson Gate).
- **Sourced claim:** C1 (S350–S353) and C2 (S350–S354); all five rows were opened this round.
- **Frontier advanced:** README "Round 87 — Limine path-pin plane" (new ground plus four frontier bullets).
- **Mined mistakes:** M1 `R87-INTENT-RULE-NOT-TOOL-RULE`, M2 `R87-FILED-BYTES-SWEEP-NOT-RUN`,
  M3 `R87-RULESET-CLAUSES-UNMAPPED`.
- **Assimilation:** none. The claims were frozen before attempt 2. considerthese: not mined this round (latest
  file `considerthese/2026-10-26.md`).

## Trend verdicts

- **expansion — unprovable-but-better.** New sourced ground: the Limine pin plane and +5 tier-A rows (349 → 354).
  Whether this is new ground is a judgment, not a count.
- **quality — improved.**
  - Registry coverage 136/138 → 138/138.
  - Header gate 103/103.
  - The gate now confines paths to the ESP; this is probed, and the `traversal` self-test case can fail.
  - QUALITY 124 has a decidable exit map, and QUALITY 125 was added.
  - The r86 registry over-generalisation is corrected by R87-REG-1.
- **discernment — improved.**
  - The lane's own critic showed the counter certifies only part of R1–R7. The report and SCORECARD say so
    (10 clauses uncertified) instead of reading 22/22 as full implementation.
  - The candidate's behaviour on those clauses is reported as separate, non-counter evidence.

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists / cited sources. Evidence: registry rows `limine-pins`
  and `limine-pin-battery-r87`, and `R87-REG-1`, in `SKILL.md` at `46d48a71`. Non-author verification is owed.
- [~] End-to-end domain task logged in LOG.md. Evidence: LOG.md "Round 87" covers host pins → Limine rules → gate
  `--live` (rc 1 on lines 30 and 38) → the entry's Operator actions.
- [~] Instructions executable without oral context. Evidence: gate and battery docstrings, `--selftest` modes, and
  the entry's `recheck:` line. No no-oral-context retest was run.
- [~] No cross-domain bleed. Evidence: PROVINCE.md is unchanged. ConnectorOverlap's sibling scan
  (`w1/ConnectorOverlap/sibling-scan.txt`) was left unfinished at the restart.

## Round shape and extras

- **Shape:** one v1 wave, w1, dispatched by attempt 1, with 12 seats: executor 2, mutation-tester 2, critic 2,
  reviewer 2, scout 2, scribe 1, connector 1. Attack seats: 6 of 12. No residual call. Round total: 12.
- **Seat outcomes.** All 12 settled. The orchestrator kernel restart at 19:24:53 cut off six seats mid-work:
  - CriticClaims, ReviewGate and ConnectorOverlap left receipts on disk.
  - CriticLimine, ScoutSources and ScoutRepair left nothing on disk.
  - Their last text is in `w1/finals/`. No seat was replaced.
- **Misroot sweep:** fleet `git status --porcelain` shows only the orchestrator's `.scratch/run15-wrapup/…`. There is
  no misroot from this lane. ScoutRepair's final text says it removed its own fleet-root scratch files.
- **Scratch:** `/fast/scratch/hyaku/tsukuroi-r87` was removed after landing.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** `tsukuroi | round-86 | HOST INCIDENT` — the pins on lines 30 and 38 still mismatch. The
  repair belongs to the operator.
