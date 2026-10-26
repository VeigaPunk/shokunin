# tabi — round 31 report (hyaku run 8, attempt 2, L1 TabiR31a2)

Lane repo `tabi-shokunin`, branch `master`. Baseline `96a2d1a3e04a1d482a1bd8bfa97343bcc2acf3bc` → final lane tip
`70e84a1058f1b2232c8e66f50732ec4bd369f908` (pushed; `git ls-remote origin refs/heads/master` prints it). Claims
measured at `cad607b7104ff1668f1c8c847c3c0b720ec3e7d9`. The one later commit adds only `.ufo/waves/round-31/` files,
and neither counter reads them. Not a fresh-start round: round 30's closure was admitted
(`corpus/lessons/round-30-verifier-spotcheck.md`). Its routed defects are handled under the claims (claims.json
`priorClosure`).

**Attempt history.** Attempt 1 (L1 TabiR31) froze the claims (`9505a10e`), landed the work (`48604835`) and ran W1. It
then died in the orchestrator host crash (~08:50 -03) before its W2 spawned. The orchestrator abandoned W2 unspawned
and salvaged the wave state in `ae15a37e`.
- **Reused after re-verification:** claims, controls, freeze receipts, the 32 W1 reports and the attempt-1
  measurements. Both frozen counters are byte-identical at `ae15a37e`, C1 reads 13/13 live with failing 0, C2 reads
  mismatches 0, and all six no-harm checks are green (`.ufo/waves/round-31/measure/a2-reverify-at-ae15a37.txt`).
- **Discarded:** the `w2` wave as a dispatch, because it is spent. Its 32 items were redispatched unchanged as `a2w1`.
- **Not reused:** the `<MEASURED>` placeholders in the a2w1 LOG draft. The L1 wrote the LOG entry itself.

## Work performed

Declared claims (frozen before data in `9505a10eb80b2a0b273ebaba3f7f872ad302192d`, `.ufo/waves/round-31/claims.json`):

- **C1 — depth** (lowest-axis tie at 8; this is the sourced claim). The new entry
  `corpus/knowledge/rate-signal-decision-table.md` is a decision table from observable rate and crawl signals to a
  driver action. Every row carries the source's own number. Counter: `scripts/check-decision-table.mjs` with `--live`.
- **C2 — calibration** (a lane axis). Self-assessment counter v2 reads the self-test tallies stated in `SKILL.md` and
  `corpus/README.md` and takes each gate's own summary line as the oracle. The nine stale statements it found are
  corrected append-only.

Work items:

- Freeze: two counters, five C1 controls and four C2 controls, plus the assimilation collision check, all landed in
  `9505a10e`. Receipts are in `.ufo/waves/round-31/baseline/README-receipts.md`.
- C1: rows D1–D13 cite S119 (RFC 9309), S121 and S122 (GitHub REST docs). S120 (RFC 6585) is cited in prose only.
  Receipts and bytes are under `corpus/evidence/round-31/decision-table/` (`48604835`).
- C2: eight appended corrections in `SKILL.md` and one in `corpus/README.md` (`48604835`). The routed
  `SCORECARD.md:1523` correction is also in `48604835`.
- QUALITY criteria 80–81 (`48604835`). Criterion 82 supersedes 81's unenforced clause (`cad607b7`).
- Attempt-2 integration of the a2w1 findings (`cad607b7`):
  - entry errata: `rate-signal-decision-table.md` §Errata
  - README corrections to the round-31 rows: `corpus/README.md:688-705`
  - correction of the stale word-numeral tally at `SKILL.md:1559`: `SKILL.md:2604-2610`
  - lesson §Attempt 2, with a dispositions table and mistake M11: `corpus/lessons/round-31.md:296-356`
  - SCORECARD disposition: `SCORECARD.md:1570-1603`
  - LOG entry: `LOG.md:2063-2120`
- Wave evidence and final measurements: `70e84a10`, under `.ufo/waves/round-31/a2w1/` and
  `.ufo/waves/round-31/measure/`.

Round shape: **two v1 waves** under policy `ufo-wave-policy.json`. Both validated with empty `*-validate.stderr` and
were dispatched through the inline handoff (`w1.ready` by TabiR31, `a2w1.ready` by TabiR31a2).
- **W1** (attempt 1, build plus first falsifiers): 32 seats — 9 executor, 9 scribe, 5 critic, 3 reviewer,
  2 connector, 2 mutation-tester, 1 scout, 1 sentinel. m_flash roles 24/32; attack roles 10/32. All 32 reports are on
  disk. There is no `w1-results.json`, because the dispatcher never finalized W1 before the crash.
- **a2w1** (attempt 2, falsify): 32 seats — 9 critic, 9 executor, 7 reviewer, 2 mutation-tester, 2 connector,
  2 scribe, 1 scout. m_flash roles 20/32; attack roles 18/32. `a2w1-results.json` has 32 entries, each with output.
  Every item names what it attacks.
- Round total **64**; no residual call; dead seats **0**.
- The §3 planner seat is held by the L1, because the validator rejects `planner`. The planning walk rode the W1
  scout and connectors.
- Routing follows the run-8 role map; no `model` was passed.

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `9505a10eb80b2a0b273ebaba3f7f872ad302192d` | claims freeze, counters, controls, SKILL registry rows, freeze-time SCORECARD corrections | §Round 31 ledger |
| `486048356f0712e4396588c9dab58cd419243120` | C1 entry, rows S119–S122, receipts; C2 corrections; SCORECARD:1523 correction; QUALITY 80–81; lesson | §Round 31 ledger |
| `ae15a37ee8aa43964179a676a087604368cd1c41` | orchestrator salvage of attempt-1 wave state (not L1-authored) | §Round 31 (attempt history) |
| `cad607b7104ff1668f1c8c847c3c0b720ec3e7d9` | a2w1 integration: entry errata, README/SKILL corrections, QUALITY 82, lesson attempt-2 + M11, SCORECARD, LOG (measured revision) | §Round 31 (this entry) |
| `70e84a1058f1b2232c8e66f50732ec4bd369f908` | a2w1 evidence and results, re-verification receipt, final measurements, census end | named in report |

## Before → after measurements

All after-readings were taken in a clean `git clone --shared` at `cad607b7` (porcelain 0) with the frozen digests
verified and 0 `scripts/` files changed since the freeze. Provenance: `.ufo/waves/round-31/measure/measured-provenance.txt`.

- **C1** — `node scripts/check-decision-table.mjs --rev <REV> --baseline 96a2d1a3e04a1d482a1bd8bfa97343bcc2acf3bc --entry corpus/knowledge/rate-signal-decision-table.md --live --json`
  (sha256 `d15f3bd7…f6832`).
  - **Before**, at the freeze tree: population 0, admitted 0, exit 1, entry absent (`baseline/c1-J1-do-nothing.json`).
  - **After**, at `cad607b7`: population **13**, admitted **13**, failing **0**, live true, exit 0
    (`measure/c1-live-at-cad607b.json`). The offline reading is the same.
  - The same reading holds at `48604835` and at `ae15a37e`. Target admitted ≥ 10 with failing 0: **met**.
  - Controls: do-nothing 0; old rows 0; self-quote 2 offline but 0 live; invented thresholds 0; package-as-is
    population 0.
  - Disclosed: the counter is gameable by repetition and by non-threshold numbers (lesson M10, W1
    CritC1Axis/CritC1Counter). a2w1 CritC1Verdict reads 12 distinct sourced thresholds in the landed rows, and 10 under
    the harshest criterion-80 reading. ExecC1Distinct counts 13 distinct (source, quote) pairs.
- **C2** — `node scripts/check-selfassessment.mjs --rev <REV> --json` (sha256 `143d66ff…2fce`), plus
  `git diff --numstat 9505a10e <REV> -- SKILL.md corpus/README.md SCORECARD.md LOG.md`.
  - **Before**, at the freeze tree: mismatches 9, exit 1 (`baseline/c2-J1-do-nothing.json`).
  - **After**, at `cad607b7`: mismatches **0**, exit 0, couldNotEvaluate 103, superseded 29
    (`measure/c2-at-cad607b.json`). Numstat shows LOG 59/0, SCORECARD 39/0, SKILL 30/0, README 44/0, so **0 deleted
    lines** (`measure/c2-numstat-freeze-to-cad607b.txt`). **Met.**
  - Controls: delete-lines is not verified under the kill rule; uncited correction reads 12; wrong-document citation
    reads 9.
  - Disclosed: the window cannot read word-numeral or `cli_cases=` tallies, it reads a failed self-test's count
    (M11), and a merged two-bullet correction still clears (a2w1 MutC2Corrections, 6/7 mutants killed).
- **No-harm** at `cad607b7` (`measure/noharm-at-cad607b.txt`):
  - gate registry nonconformant 0 (21 gates)
  - release-pins resolved 23/23
  - s106 valid
  - frontier-admission population 2, admitted 2, unchanged
  - sources gate clean, 122 rows
  - census exit 0
  - a2w1 ExecNoHarmTip: no gate is green at the freeze and red at the landing.

## Sources & frontier

Census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
- Start: exit 0, `tabi ok`, 19 W04 (`.ufo/waves/round-31/baseline/census-start.txt`).
- End: exit 0, `tabi ok`, 19 W04 (`.ufo/waves/round-31/measure/census-end.txt`).

- **Rows** 118 → 122 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by tier: A 4
  (S119, S120 spec; S121, S122 first-party docs scoped to GitHub's own API). Status mined 94 → 98. URLs, access times
  and located quotes are in the lesson §Gate.
- **Touched old→new:** none to existing rows. The S119 anchor's "June 2022" (the bytes say September 2022) is recorded
  as an erratum and not edited in place; a superseding row is planned for round 32.
- **Frontier:** "Rate/ToS surface for site-interaction records" now has sourced thresholds on the rate half (D6–D13)
  and robots/crawl bounds (D1–D5) filed provisionally. Runtime and the ToS half stay open (`corpus/README.md:685`,
  corrected at `:690-694`).
- **Sourced claim:** C1 rests on S119, S121 and S122, all opened 2026-10-26.
- **Mistake mined:** `corpus/lessons/round-31.md` §Mistakes M1–M10 and §Mistakes — attempt 2, M11 (fix: criterion 82;
  red state: a2w1 RevQuality probe).
- **Assimilation: none.** Staged S126 stays refused (round-27 register id drift). S121 and S122 were opened by
  document with the lane's own fetches, not adopted from the package.
  - Lane ids 118, staged ids 148, collisions 17 (S102–S118), none adopted.
  - Guard proof: `.ufo/waves/round-31/w1/ExecAssimGuard/`.
  - Quarantine slice 38 rows, register sha unchanged since round 27, no row adopted.
- **considerthese/:** no such directory in this lane.

## Trend verdicts

- **expansion: improved.** One admitted entry on ground the lane did not hold: sourced numeric thresholds for the
  driver's next action, where before the lane held signal vocabulary only. It cites three mined rows opened this
  round. The frontier row advanced.
- **quality: improved.** Every row was re-verified live by a seat that did not fetch its receipt (a2w1 RowAttack*,
  Refetch*). Nine stale tally statements and the `SKILL.md:1559` word-numeral tally were corrected. Every prose or
  record defect a2w1 found is marked by an appended erratum, and none is left unmarked. No admitted entry failed its
  re-check.
- **discernment: improved.** Round-30 spot-check routed defects 1–2 became counter v2 and an appended correction. A
  disagreement between criterion 81 and the counter became lesson M11 and criterion 82. Counter holes are disclosed,
  not hidden. The non-author closure spot-check is still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `tabi-shokunin/SKILL.md:697` (approval table), `:1598-1617`; new sourced-threshold table `corpus/knowledge/rate-signal-decision-table.md` D1–D13; no non-author verifier this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2, §7; `LOG.md` round-3 entry
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (executor was a lane-dispatched seat)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19` unchanged; a2w1 ConnAdjacency: D1–D5 driver-side per kake's split, mori S041/S042 disjoint purpose, nothing absorbed

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1; seats reported none.
Open L0 questions: none new. The round-27 tabi question on S114/S140 stays open and was routed around.
Defects of this round (for the closure):
- Five a2w1 seats left scratch dirs under `/fast/scratch/hyaku/tabi-r31/`: ExecC1Distinct, RevLesson, RevSourcesRows,
  RowAttackD11D12 and RowAttackD9D10, about 145 MB each. The L1 removed them after landing.
- W1 has no results.json, because the dispatcher never finalized it in attempt 1.
- 27 W1 findings are carried to round 32 (`.ufo/waves/round-31/a2w1/ScribeErrata/errata.md`).
- Misroot sweep: `git status --porcelain` on the fleet root shows no seat-written untracked file. The only one,
  `.ufo/state/disk-guard.log`, is driver-owned.
