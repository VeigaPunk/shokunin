# revenger — round 94 (hyaku run 15, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`. Final lane hash
**`0035a44e5e807d4c03edf0d11b8a396861b90665`** (`git ls-remote origin refs/heads/main` prints it;
`jj-lane.sh state` reports `local=remote`, `ahead=0 behind=0`). Stale-lane: respawn-per-round driver;
no other mission of this lane is open.

## Work performed

Declared claims (frozen at `060a8e87d6de6b31f91b58524ab0fcad88ae5431`, `reports/round-94/claims.md`):

- **C1 — coverage, knowledge-map ground K (the lowest non-retired owned axis).** Coverage row C15 moves
  `uncovered` → `held` through the re-grounded tool-landscape entry. Before 10/15 (6.7), after 11/15 (7.3).
- **C2 — calibration.** The routed successor counter (v3) and its forgery battery kill the routed classes
  that the frozen r93 v2 counter still passes. Red-before 8/8 runnable reach + 1 receipt-backed; after
  12/12 frozen classes killed.

No capability acquisition, no exploratory claim. Both claims work distinct axes; they are separable
(C1's counter does not read the battery trees; C2's battery builds its own trees from the freeze archive).

Work items, each with its evidence pointer:

- Load order: `skill://shokunin`, canonical `MISSION.md`, `AXES.md`, the lane `SKILL.md`, `PROVINCE.md`,
  `SCORECARD.md`, `SHONEN.md`, round-93 claims and spot-check (`corpus/lessons/round-93-verifier-spotcheck.md`,
  6/6 agree), the r93 critic's 12 findings (`.ufo/waves/round-93/w1/CriticR93/findings.md`), the r93 counter.
- Round-start census: `scripts/sources-census.sh validate --root … revenger` exit 0, 21 W01 + 13 W04, 0 E
  (`reports/round-94/controls/census-round-start.log`).
- Entry re-grounding in the freeze bytes: `corpus/knowledge/round-72-tool-landscape.md` gains source header
  lines S498/S499, a Q17 decision row; the r73 erratum section is byte-identical.
- Drift checks (S498 ⇐ S054, S499 ⇐ S075): `.ufo/waves/round-94/w1/ScoutReopen/drift-verdicts.md` — both
  **no drift**; `ExecReceipts/fetch-sha-compare.md` — two independent fetches, byte-identical, `cmp` exit 0.
- Counter v3: `reports/round-94/c1_k_admit_counter3.py` (14 legs; `--self-test` `SELFTEST_C1V3=pass legs=14`,
  exit 0; `reports/round-94/controls/selftest-c1v3.log`).
- Battery v3: `reports/round-94/forge_battery3.py` (`--stage red-v2` committed as
  `reports/round-94/controls/battery3-red-v2.log`; `--stage full` at freeze `controls/battery3-full-at-freeze.log`).
- Do-nothing controls: `controls/c1v3-do-nothing.log` (freeze) and `controls/c1v3-do-nothing-base.log`
  (landing-era base `--rev 9876cb38…`): `C1_C15_HELD=fail`, exit 1.
- Wave `revenger-r94-w1`, one v1 wave, 13 seats; spec `.ufo/waves/round-94/w1-spec.json`; validator
  `plan` and `run` exit 0 (`w1-plan.out`, `w1-dispatch.json`); ready file `w1.ready`; WAVE-DONE received
  (`w1-results.json`, 13 results with nonempty final output).
- Critic pass `.ufo/waves/round-94/w1/CriticR94/findings.md`: 27 attacks; the frozen twelve reproduce 12/12;
  17 forgeries outside the frozen set pass v3 (H1 indented status line; H2 receipts' fetch honesty not
  checked; H3 C15 cell substring; M1–M10). All routed to r95; none amends a frozen byte (kumitate r42).
- Mutation pass `MutationR94/mutants.md`: 14 one-point mutants of the v3 legs — 12 KILLED, 2 SURVIVED
  (`C1_REGISTRY` has no leg of its own; `C1_QUOTES` is only the receipt check). Both recorded as findings.
- Sentinel `SentinelScope/audit.md`: one gitignored `corpus/__pycache__` pyc from a seat's un-flagged Python
  run (F1) — removed; no sudo, sysctl, pacman, network outside the named URLs; scratch not over the bound.
- considerthese proposal 2 re-measured (`ConnectorOverlap/measurement-r94.tsv`): r90–r93 → **0 of 8** clean.
  Baseline only; not adopted.
- Landing: `corpus/knowledge/round-72-tool-landscape.md` `admission-status: candidate` → `admitted` (the single
  status line; the digest is invariant under that flip, verified by `C1_VOTES … digest=01d51059…` before and
  after); `corpus/README.md` C15 → `held`; `corpus/SOURCES.md` S498/S499 appended after S497; votes
  `reports/round-94/votes/*.json`; quote receipts `reports/round-94/quote-receipts/`; `SKILL.md` gains the two
  probe registry rows.
- Adjudication: `corpus/lessons/round-94.md` (Gate, Mistakes M1–M7, corrections, frontier, census,
  assimilation none, considerthese); `LOG.md` and `SCORECARD.md` round-94 sections; control and battery logs.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `060a8e87d6de6b31f91b58524ab0fcad88ae5431` (freeze) | claims, v3 counter, v3 battery, controls, red-before, entry re-grounding (S498/S499 header lines, Q17 row), `freeze-base.txt`, census-start | `LOG.md` Round 94 (adjudication entry) |
| `60b5e8e36325b3decdc8ce46041216cdafd1166e` (landing) | admission flip; C15 → held; S498/S499 rows; three votes; quote receipts; wave evidence `.ufo/waves/round-94/`; SKILL probe rows | Round 94 entry, "Landing" bullets |
| `0035a44e5e807d4c03edf0d11b8a396861b90665` (adjudication) | `corpus/lessons/round-94.md`; `LOG.md`; `SCORECARD.md` round-94 section; `reports/round-94/controls/*` after-logs | Round 94 entry |

No change to `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/live/`, `corpus/fixtures/` (empty diff against the
base). The frozen r93 counters and the v3 counter/battery/claims are byte-identical from freeze to tip
(`git diff --quiet 060a8e87 0035a44e -- …`: same for all six instrument and claims paths).

## Before → after measurements

**C1 — coverage K.** Before: `K_HELD_BACKED=10/15` (score 6.7; C15 `uncovered`). After: `11/15` (7.3; C15 `held`).

- Counting command (landing): `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 60b5e8e36325b3decdc8ce46041216cdafd1166e`
  → `C1_K_HELD_BACKED=11/15`, `C1_VERDICT=pass`, exit 0 (`reports/round-94/c1-after.log`). Every leg passes.
- Do-nothing base: `--rev 9876cb38c5415fbc86336a26a68e05680c397fd5` → `C1_C15_HELD=fail`, `C1_VERDICT=fail`, exit 1.
- Measured commits: base `9876cb38c5415fbc86336a26a68e05680c397fd5` → freeze `060a8e8` → landing `60b5e8e3`.
- Verdict: **met on the frozen counter; not admitted until the non-author closure.** All three votes are
  lane-internal (dispatched by this lane); per LEARNING.md they are not non-author. Critic H2/H3 contest the
  receipts' and the C15 cell's strength; both routed to r95.

**C2 — calibration.** Red-before (committed, freeze): `RED_V2_VERDICT=pass`, `V2_REACH_NEW=8/8 runnable + 1
receipt-backed` — the frozen v2 counter still passes every re-runnable critic vector of the eight classes; F13
(role mismatch) is receipt-backed only (A28/A29 were critic-interactive; `controls/battery3-red-v2.log`).

- Counting command (landing): `PYTHONUTF8=1 python3 -B reports/round-94/forge_battery3.py --stage full`
  → `V3_KILLS=12/12`, `POS_C1V3=pass` (real lint and embedded checker), `DO_NOTHING_C1V3=fail-as-required`,
  `HOLD_R93_BATTERY=pass`, `BATTERY3_VERDICT=pass`, exit 0 (`reports/round-94/battery3-after-full.log`).
- Measured commits: as C1.
- Verdict: **met on the frozen predicate; not admitted until the non-author closure.** Contested by the critic's
  17 residual vectors (routed to r95 with their closes), and the claim sentence "kills the routed forgery
  classes" is a named-vector statement (the critic's W8/W9).

Other criteria (no claim): F4 11/11, M 3/3, A1 3/3, A1v2 5/5 — base holds only, not re-run at landing.

## Sources & frontier

- **SOURCES before → after:** 497 → **499** rows. Counting command:
  `grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md` → 497 (base) / 499 (tip); census
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → **exit 0** at round start
  (21 W01 + 13 W04, 0 E) and **exit 0** at round end (21 W01 + 13 W04, 0 E; `reports/round-94/controls/census-round-{start,end}.log`).
- **Rows added by tier:** S498 tier A, S499 tier A (both `mined`, `docs`, opened 2026-11-05, `used-by`
  `corpus/knowledge/round-72-tool-landscape.md`). Tier histogram A 448 → 450, B 21 → 21, C 28 → 28.
- **Rows touched old→new:** none (append-only; no status, recheck or used-by change in place).
- **Frontier rows advanced:** C15 `uncovered` → `held` (`corpus/README.md`).
- **Sourced claim:** C1 rests on S498 and S499 (§2b.4), each opened this round with a located ≤25-word
  quote (`corpus/lessons/round-94.md` Gate table; receipts `reports/round-94/quote-receipts/`).
- **Assimilation:** none. `merge/revenger/` remains in mass id drift (**155** staged ids collide with the registry:
  `.ufo/waves/round-94/w1/ExecCensus/collisions`); L0 `revenger | round-91` is unanswered. Nothing adopted.
- **considerthese:** proposal 2 measured (0 of 8 clean over r90–r93, `ConnectorOverlap/measurement-r94.tsv`); not adopted.

## Trend verdicts

- **expansion: improved.** One admitted entry on previously uncovered coverage-map ground (C15), backed by
  sourced rows opened this round (`corpus/lessons/round-94.md` Gate). Measured: K 10/15 → 11/15.
- **quality: improved.** The two registered sources behind the entry were re-opened against live main and
  found unchanged in their scope cells (S498, S499: no drift; two byte-identical fetches). Contested:
  the receipt leg checks internal consistency, not fetch provenance (critic H2, routed to r95).
- **discernment: improved on the frozen predicate.** The frozen v3 battery kills 12/12 named classes where the
  frozen v2 counter reached 8/8 runnable + 1 receipt-backed. Contested by 17 residual passing vectors
  (routed). Pending the non-author closure per LEARNING.md; no non-author verdict exists in this round.

## SHONEN

`grep -c '^## SHONEN'` on this report: 1.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` (gate registry rows incl. the two round-94 probes; `corpus/SOURCES.md` S498/S499). No non-author verifier of the current bytes; not promoted.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 94 entry; `corpus/lessons/round-94.md`; `reports/round-94/c1-after.log`.
- [~] Instructions executable by an agent without oral context — pointer: `reports/round-94/c1_k_admit_counter3.py --self-test` (`SELFTEST_C1V3=pass legs=14`, `reports/round-94/controls/selftest-c1v3-after.log`). No outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` byte-unchanged (`git diff --stat 9876cb38..0035a44e -- PROVINCE.md` empty); the r93 ADJ-06 note stays reported, not absorbed.

No `[x]` line: no non-author verifier has checked any box this round.

## Round shape, seats and dead seats

- One v1 wave, **13 seats** (band 8–16): scout ×2 (ScoutReopen, ScoutErrata), scribe ×1 (ScribeLesson),
  executor ×4 (ExecReceipts, ExecBattery, ExecCensus, ExecFrozen), reviewer ×2 (ReviewerGate, ReviewerBlind),
  critic ×1 (CriticR94), mutation-tester ×1 (MutationR94), connector ×1 (ConnectorOverlap), sentinel ×1 (SentinelScope).
- Attack share: reviewer ×2 + critic ×1 + mutation-tester ×1 = 4/13 = **30.8 %** (≥25 %). Connector: 1 (≤2).
- Residual call: none. Round total: **13**.
- Planner seat: the L1 holds the canonical planner seat; the validator rejects a planner in a wave.
- Dead seats: **none** — 13 of 13 settled with nonempty final output (`w1-results.json`).
- Seat routes: each seat ran on the route `task.agentModelOverrides` gave its role at spawn; no model was passed. No claim depends on a seat's answering model.
- Caveat on the wave's independence: the three voters and the critic are lane-dispatched; the non-author closure is still required.

## Open L0 questions

- `revenger | round-91` (assimilation: 155 staged-id collisions) — still open in `.ufo/l0-questions.md`. No new question appended this round; the lane routed around it.

## Misroot sweep and inherited state

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec): two entries, neither a revenger round-94 write:
  `M .scratch/run15-state.json` (orchestrator-owned run state; not touched) and `?? .ufo/closure-kaidoku-r92.json`
  (a sibling lane's closure; not touched). **No misroot to copy.**
- Inherited: the r93 spot-check and its routed items are worked this round (v3 counter; considerthese measurement).
  The r92 votes remain lane-internal per the r93 correction; nothing re-bound.
- The `-B` note: one seat's un-flagged Python run left a gitignored `corpus/__pycache__` pyc (sentinel F1); removed.

## Tool installs

None. No package was installed or upgraded in this round by this lane or its seats; the validator and the lane's
own Python 3.14 were used as installed.

## Scratch

Lane scratch lived under `/fast/scratch/hyaku/revenger-r94/` (per-seat trees and the L1's own probes). The L1 removed that whole tree after landing (`rm -rf`). No citation points into it: every cited artifact is in the lane tree or the wave directory. The frozen instruments read `HYAKU_SCRATCH` and never write under `/tmp`. The `battery3` and `c1v3` roots named in `SKILL.md` and the battery source are re-run paths, not evidence.

## Honesty notes

- The C1 and C2 verdicts are met **on their frozen predicates**. Neither is admitted until a non-author verifier
  reads the landed bytes; all three gate votes and the critic pass are lane-internal.
- Claims wording that overreached, now recorded as errata (predicates unaffected): the claims name a leg
  `C1_REGISTRY` the counter does not have (M6, `corpus/lessons/round-94.md`); the round-start census count in
  the claims reads `15 W04` where the measured count is 13 (M7). The frozen claims bytes are not edited.
- The red-before's F13 reach is receipt-backed, not re-run (the two critic vectors were interactive).
- One committed attack driver from r93 hardcodes a reaped scratch root; the battery now recreates the bare
  dirs before the red re-run (M1). The original failing log was in `/tmp` and is not cited.
- Open defects routed to r95 with their closes: indented `admission-status` false green (critic H1), receipt
  fetch provenance (H2), C15 cell substring (H3), the registry leg (M6), S-id regex and n/a vocabulary (M5/M6),
  and the spec-template `-B` rule (M5).
