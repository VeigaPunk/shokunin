# kotoba — round 96 report (KotobaR96, attempt 1, Linux host, omp)

Lane repo `kotoba-shokunin`, branch `master`. Base `0f66016a3b35cf1e25c67caf8cf371996805cbb8` →
final lane tip `74fa240b5fb3ef4a7b0507f36f12127db264a33d` (`git ls-remote origin refs/heads/master`
prints `74fa240b5fb3ef4a7b0507f36f12127db264a33d`). Verdicts belong to the non-author closure.

## Work performed

Declared claims: **one**. **C1 — depth** (the lowest owned non-retired axis, score 9): the
dispatch-prompt checker's self-test (`verifiers/verify_dispatch_prompts.py --self-test`, the executable
proof of SKILL.md § Dispatch-prompt fidelity checklist boxes `dispatch.04`/`dispatch.08`) kills eleven
frozen survivors `t01..t11` of a pre-freeze mutant sweep. Sourced on S271 and S272, opened this round.

- **Inherited state.** No earlier attempt of round 96 (`.ufo/watchdog.log`: one `launch kotoba
  round=96 … attempt=1`, no `lane-dead-no-report kotoba round=96`); lane clean at base; no
  `corpus/lessons/operator-*.md`. `corpus/lessons/round-95-verifier-spotcheck.md` read; its six routed
  defects are dispositioned in `plans/round-96.md` § Inherited state (defect 1 → lesson Gate amendment;
  2 → committed f3/f4 controls + MutTesterCounterV4 matrix; 4 → f2 crash world committed and
  recompile/bytecode worlds attacked by ExecCounterForgeryR96; 3, 5 carried; 6 orchestrator-side).
- **Pre-freeze sweep.** 22 hand mutants of `verify_dispatch_prompts.py`, 18 survive the 56-assertion
  self-test (`.ufo/waves/round-96/receipts/recon-sweep.txt`; the plan's "17" is corrected in
  `plans/round-96-addendum-1.md` A1).
- **Freeze** `679775abb9277a7b8d17f060b0f5b4ced2b127b6`: `plans/round-96.md`; v4 counter
  `verifiers/fixtures/round-96/selftest-kills.py` (sha256 `1711b68f…13b2b2`: the round-95 v3 rules on a
  claim table naming instrument + failure prefix; the code decoy climbs an `elif` arm to its if-chain);
  control-world builder `verifiers/fixtures/round-96/build-forgeries.py` and five patches; pre-data
  receipts `.ufo/waves/round-96/receipts/` (`redbefore-c1-base.txt`, `poscontrol-r95c1-base.txt`,
  `forgery-f1..f5-*.txt`, `predraft-elif-decoy.txt`, `base-box-proof.txt`, `census-before.txt`,
  `sources-opened.txt`, `freeze-shas.txt`).
- **Wave `r96-w1`** (11 seats, results `.ufo/waves/round-96/r96-w1-results.json`, seat reports
  `.ufo/waves/round-96/w1/*.md`): ExecArmsR96 built 22 behavioural `rec(...)` arms (56 → 78
  assertions; `w1/ExecArmsR96.md`); ScribeCorpusR96 appended S271/S272 and the lesson scaffold;
  ReviewerArmsR96 and CriticClaimR96 hand-applied each mutant and named the failing `self-test FAIL:`
  assertion (`w1/ReviewerArmsR96.md` § 2; `w1/CriticClaimR96.md`, failure counts 2,1,1,2,3,2,1,1,1,3,5
  identical to the counter's); ReviewerCounterV4 reproduced every pre-data receipt; SentinelScopeR96
  confirmed scope, production byte-identity and identical live dispatch verdicts at base and candidate;
  ExecCounterForgeryR96 built eight new forgery worlds (three classes read MET — addendum A3);
  MutTesterCounterV4 ran 18 counter variants × 7 controls (M10, the elif climb removed, flips every c1
  world to could-not-evaluate); MutTesterDispatchR96 ran 19 new mutants (15 survive — routed);
  ConnectorOverlapR96 proved the floors entry is a minimum (`check_assertion_floors.py:685`) and no
  instrument pins the file's bytes; ScoutSourcesR96 re-opened both sources byte-identically.
- **Integration** (`plans/round-96-addendum-1.md`, A1–A6): sweep count, POSIX word count (22), counter
  bounds (stateful fakes g7/g8 and recompile-compare g3 read MET on v4 with no behavioural arm; g2b is
  the carried v3 bound), exit ladder carried, v4 drops the v3 `r94c1` table, three arm labels corrected
  before landing (behaviour unchanged).
- **Planner seat:** held by the L1 (the validator rejects `planner`); the planning data-walk rode
  ConnectorOverlapR96 Part 3.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → one untracked
  `w4lines.txt` (mtime 2026-11-05 16:57, before this round, no kotoba/r96 content) — not this lane's,
  left untouched. No misroot.
- **Scratch:** `/fast/scratch/hyaku/kotoba-r96` removed after landing.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `679775abb9277a7b8d17f060b0f5b4ced2b127b6` | freeze — plan, v4 counter, builder + five forgery patches, pre-data receipts | § Round 96, "Claim as frozen", "Pre-data controls" |
| `801dd9bc6075d8c4f53c1cfdf9c4c7d3000c72c2` | landing — `verifiers/verify_dispatch_prompts.py` self-test arms (+128 lines inside `self_test()`), S271/S272, `corpus/lessons/round-96.md`, README index row, addendum 1 | § Round 96, "Landing", "Integration" |
| `762859df70721a73b7a65a1e5ff5d78d874f9aa6` | record — lesson settlement, `corpus/QUALITY.md` Q86, LOG, SCORECARD (round-96 annotation, round-97 intentions), landing receipts | § Round 96, "No-harm at landing", "Frontier step" |
| `74fa240b5fb3ef4a7b0507f36f12127db264a33d` | wave evidence — spec/dispatch/ready/results, 11 seat outputs, generator | § Round 96, "Wave" |

All four printed `landed <hash>` from `jj-lane.sh` after remote verification; `jj-lane.sh state` →
`local=remote=74fa240b… ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

**C1** — counting command `python3 -B verifiers/fixtures/round-96/selftest-kills.py c1 <rev>`:

- before, at base `0f66016a` (`.ufo/waves/round-96/receipts/redbefore-c1-base.txt`):
  `C1 targets killed 0 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`
  → `C1-PREDICATE-UNMET`, rc 1 (the do-nothing control).
- after, at landing `801dd9bc6075d8c4f53c1cfdf9c4c7d3000c72c2` (`receipts/landing/c1-counter.txt`):
  `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`
  → `C1-PREDICATE-MET`, rc 0. Self-test `0 failure(s) over 56 assertions` → `0 failure(s) over 78 assertions`.
- controls: positive `r95c1` MET at base and landing; forgery worlds f1–f5 all UNMET pre-data (f2/f3
  `run errors 1`, f4 honest REPORTED-FAILURE).
- no-harm at landing (`receipts/landing/`): round-95 counter `c1`/`r94c1` MET; round-93
  `c1-killpin-rev.sh` MET; round-92 `controls-run.sh` `shortcuts refused 2 of 2; honest held 2 of 2`;
  `--box-proof` `boxes proven 2`; live run `dispatch.04` 1191 PASS/6 FAIL/22 N/A and `dispatch.08` 1172/10/29
  — identical to the base reading (SentinelScopeR96); gate registry `74 of 74 … phantom 0`; floors
  self-test `0 failure(s) over 176 assertions`; tip battery `guards 5 of 5; tip battery exit 0: 3 of 6`
  (same reds as the round-95 landing; floors gate 264.9 s inside its cap); SKILL.md 600 lines, `git diff
  --stat 0f66016a master -- SKILL.md PROVINCE.md SHONEN.md` empty.
- Disclosed bound (A3): the v4 counter reads MET on three no-arm forgery classes, so the kill evidence
  is the counter reading **and** the hand-applied, named-assertion kills of two independent seats.

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`:
  round start rc 0 (`receipts/census-before.txt`, 34 `W04`, 0 `E`); round end rc 0, last line
  `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, 34 `W04` (none new).
- Rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 196 → 198. Added by tier:
  A 2 — S271 PIT "Mutation operators" (Conditionals Boundary; grounds t04), S272 POSIX.1-2024 XCU 2.6.2
  Parameter Expansion (braces optional; grounds t01–t03). Both opened 2026-11-06 by the L1, re-opened
  byte-identically by ScoutSourcesR96 and ScribeCorpusR96; located quotes in `corpus/lessons/round-96.md`
  § Gate. Rows touched old→new: none (append-only).
- Same-round rejects: mutmut docs (reverse boundary direction not stated, HTML line 523), GNU Bash
  manual (host unreachable, HTTP 000); BASH(1) and Stryker "Supported mutators" recorded as
  corroboration/not written. Round-95 Ant reject reason amended append-only (closure defect 1).
- Sourced claim: C1 cites S271/S272 (plan § C1 "Sourced", landing arm comment cites XCU 2.6.2).
- Mined mistake: `decoy-builder-cuts-elif-chain` (`corpus/lessons/round-96.md` § Mistakes) — evidence
  `receipts/predraft-elif-decoy.txt`; captured-by the counter's compile guard; fix v4 rule 2, shown able
  to fail (MutTesterCounterV4 M10 removes the climb → every c1 world `C1-NOT-EVALUATED`); criterion Q86.
- Assimilation: none (this round takes no `merge/kotoba/` theme). considerthese: `considerthese/2026-10-26.md`
  re-read, no proposal implemented (lesson § Considerthese gives each proposal's current measure).
- Wave evidence bytes (Q82): `du -sb .ufo/waves/round-96` 1941368 vs round-95 719539 and round-94
  611324 (2026-11-06); the growth is the seats' saved source HTML copies and forgery receipts.

## Trend verdicts

- **expansion: unchanged** — no `knowledge/` entry admitted; S271/S272 are registry rows cited by plan
  and lesson.
- **quality: improved** — the province instrument's self-test now kills eleven behaviours it missed
  (0 of 11 → 11 of 11 at `801dd9bc`) with production code byte-identical and every no-harm reading held.
- **discernment: improved** — two sources admitted with located quotes and two same-round rejects on
  observed facts; the round-95 Ant reason corrected per the closure; three counter bounds found by the
  wave disclosed rather than absorbed (A3); mined mistake into Q86.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SHONEN.md:5`; the Dispatch-prompt fidelity boxes `dispatch.04`/`dispatch.08` now carry a self-test that kills 11 of 11 frozen mutants (`.ufo/waves/round-96/receipts/landing/c1-counter.txt`); SKILL.md unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence `LOG.md` § Round 96 (freeze → wave → landing → no-harm, lane-run; no non-author credit claimed).
- [~] Instructions executable by an agent without oral context — evidence `corpus/lessons/round-8-aggregator-box3-coldrun.md`; untouched this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `PROVINCE.md` § Adjacent; unchanged this round (`git diff --stat 0f66016a master -- PROVINCE.md` empty); ConnectorOverlapR96 found no sibling dispatch-prompt checker (`.ufo/waves/round-96/w1/ConnectorOverlapR96.md`).

## Extras

- Round shape: one v1 wave `r96-w1`, 11 seats (executor 2, scout 1, scribe 1, connector 1, reviewer 2,
  mutation-tester 2, critic 1, sentinel 1; attack 5 of 11 = 45 %); no residual call; round total 11;
  dead seats 0 (all 11 settled with reports; `r96-w1-results.json` carries no status field per seat).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- Open L0 questions: none new.
