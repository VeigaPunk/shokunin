# kasegi — round 79 report (attempt 1, run-15 fresh start)

Lane HEAD (pushed, `git ls-remote origin refs/heads/master`): `cdade13cc65c84073922bd01c2fc1ff17b4c4b29`.
Freeze: `9d0b1eb0709e47c3c6decc09138b5012a8968924`. Base: `d16d2124fd5262f5a8088aa598f1e628f897d3ab`.

## Work performed

Declared claims (frozen in `.ufo/waves/round-79/claims.json` at `9d0b1eb0`):
- **C1 — depth:verifiability** (the lowest non-retired axis, 4; nominal per QUALITY R58). Target: the recheck-cwd census successor. The selftest reports `cases=15 failures=0`, a nonexistent TMPDIR is refused with rc 2, and the frozen 19-row mutant battery reports `killed=19`. **Verdict: NOT VERIFIED.**
- **C2 — coverage** (8). Target: admit Frontier F55, the OSV.dev `POST /v1experimental/determineversion` contract, on S113. The source row was opened this round; this is the round's sourced claim. **Verdict: VERIFIED.**

Work items:
- Fresh start: I read the rejected closures r76, r77 and r78 and their spot-checks before the freeze (`kasegi-shokunin/corpus/lessons/round-7{6,7,8}-verifier-spotcheck.md`). Routed r78 defects addressed: item 1, the Q12 reject reason, gets an appended correction at `corpus/lessons/round-79.md:37`. Item 4, the placement of the seven S112 quotes, is handled by citing the F54 Gate table at `corpus/lessons/round-79.md:36`. Items 2 and 3 (the K-X2 class and M77-3) were the C1 target.
- Pre-freeze controls were executed and committed in the freeze commit (`kasegi-shokunin/.ufo/waves/round-79/controls/`):
  - base battery: `killed=0` of 19 (18 not derived), rc 1;
  - forgery stub: `survived=8`, rc 1;
  - r78 candidate: `killed=6`, rc 1;
  - counter toy selftest: rc 0;
  - base with a nonexistent TMPDIR: rc 1 with a traceback;
  - C2 counters: FRONTIER-CENSUS rows 54, knowledge 92, and the S113 source-recheck at rc 0.
- C1 build (L1, before the freeze): candidate `.ufo/waves/round-79/c1/recheck-cwd-census.py`, sha256 `eda49d32…091f2f`. It adds gate predicates tested in both polarities and a `gate-wiring` limb that parses its own `check()` calls. Counter: `c1/mutbat.py`. Table: `c1/mutant-table.json`.
- C1 scoring:
  - `w1/ExecC1Battery.md`, two runs: `MUTBAT … baseline=ok rows=19 killed=18 survived=0 dirty=1 notderived=0`, rc 1.
  - L1 re-run: `.ufo/waves/round-79/l1/L1-battery-r79.txt`, same result.
  - Cause: K-T1's assertion FAIL detail contains the caught `exception=FileNotFoundError` text. The frozen substring classifier (`c1/mutbat.py:41`) labels that row `EXCEPTION-KILL counted=no`.
  - Under the kill rule, C1 is NOT VERIFIED. I made no amendment after scoring, and the candidate is not landed.
  - P1, P4 and P5 hold: `w1/ExecC1Battery.md` and `w1/ExecC1RealTree.md`. The real-tree census is conformant at 92 entries, byte-identical to base.
  - Independent confirmation: `w1/ReviewC1.md:20` (blocker 1).
- C1 attack findings, all routed and none changing a verdict:
  - `w1/MutC1Hunt.md`: 30 mutants outside the table; 7 real-gap survivors.
  - `w1/ReviewEquiv.md`: half A holds (r78 K-X2 is equivalent); half B breaks (2 surviving single transforms).
  - `w1/CriticClaims.md` (b) and (f): the classifier is a free-text rule; P7's `/tmp` grep counts the docstring.
  - `w1/SentinelC1.md`.
- C2:
  - Capture `corpus/source-snapshots/round-79/S113.txt` (sha256 `f4bce053…8ebf`) with manifest (eight quotes).
  - Entry `corpus/knowledge/osv-determineversion-cc-library-versioning.md`, drafted by `ScribeEntry`. The two major findings in `w1/ReviewC2.md` were fixed before landing.
  - B0–B7 met on the mirror (`w1/ExecC2Gate.md`) and re-run by the L1 on the landed tree (see measurements below).
  - B6 paraphrase check: 8 novel, 0 held (`w1/ScoutDistinct.md`).
- Overlap: `w1/ConnectorOverlap.md` finds F55 unique across the fleet. M79-1 partly duplicates the lane's r46 equivalence concept; that is noted in the lesson.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, C1 candidate/counter/table, controls, S113 capture + manifest, S113 row added `queued` | `LOG.md` § Round 79 | `9d0b1eb0709e47c3c6decc09138b5012a8968924` |
| F55 entry; S113 `queued→mined`; README F55 row; PROVINCE F55 line; knowledge-expected | `LOG.md` § Round 79 | `cdade13cc65c84073922bd01c2fc1ff17b4c4b29` |
| Lesson `corpus/lessons/round-79.md` (M79-1, M79-2); QUALITY R128, R129; SCORECARD § Round 79; wave evidence `.ufo/waves/round-79/` | `LOG.md` § Round 79 | `cdade13cc65c84073922bd01c2fc1ff17b4c4b29` |

Not landed: the C1 candidate. `corpus/instruments/recheck-cwd-census.py` stays at base sha256 `e666ae11…`, and M77-3 stays open.

## Before → after measurements

- **C1** (measured against the frozen candidate; `9d0b1eb0`):
  - Counting command: `python3 -B .ufo/waves/round-79/c1/mutbat.py --target <counter> --table .ufo/waves/round-79/c1/mutant-table.json --expect-cases 15 --work $SCRATCH`.
  - Before (base `e666ae11`): `killed=0` (notderived 18, dirty 1), rc 1.
  - After (candidate `eda49d32`): `killed=18 dirty=1`, rc 1.
  - Target was `killed=19` with rc 0. Score 4 → 4.
- **C2** (measured at freeze `9d0b1eb0` → landing `cdade13c`):
  - Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
  - FRONTIER-CENSUS rows 54 → 55 (admitted 55, closed 55, problem-rows 0, registry 113).
  - Knowledge 92 → 93; registry 113 → 113.
  - `git diff 9d0b1eb0 cdade13c -- corpus/SOURCES.md`: 1 row changed, 0 added, 0 removed.
  - Other checks: capture-binding `unbound=0`; recheck-audit `expected=93 missing=0 unexpected=0`; sources-census rc 0. Coverage score held at 8, because the denominator is operator-owned.

## Sources & frontier

- `corpus/SOURCES.md` rows: 112 → 113. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Rows added by tier: A +1 (S113, docs; opened 2026-11-06, live HTTP 200, 30242 raw bytes).
- Rows touched old→new: S113 status `queued`→`mined`, used-by `—`→`corpus/knowledge/osv-determineversion-cc-library-versioning.md`.
- Frontier advanced: F55 admitted (54 → 55). R-77-F still has two endpoints open.
- Census at round start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → `kasegi ok`, six inherited W04 warnings (S028, S029, S072, S076, S080, S085), exit 0.
- Census at round end (after landing): same command → `kasegi ok`, the same six W04 warnings, exit 0.
- Mined mistakes:
  - M79-1, equivalent mutant frozen as a required kill (captured-by: none). Fix: R128, with a pair shown able to fail: r78 K-X2 has a zero normalized diff, while r79 K-X2b is killed.
  - M79-2, substring exception classifier (captured-by: none). Fix: R129.
- Assimilation: none (82 staged-id collisions; L0 lines 353–354 still open). `considerthese/` was read, and no proposal fits a frozen claim.

## Trend verdicts

- **expansion: improved.** One new admitted entry (F55) on ground no admitted entry held: 0/8 literal matches, 8 novel by paraphrase (`w1/ScoutDistinct.md`).
- **quality: unchanged.** No admitted entry was superseded or re-verified. The census successor did not land. R128 and R129 are grounded criteria, not a measured quality move.
- **discernment: unprovable-but-better.** One wrong r78 reject reason (Q12) is corrected by an appended bullet, and three rejects are recorded with reasons (S113 lines 37, 39, 64). A non-author judgment is still pending; this verdict is self-assessed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SKILL.md`; untouched this round.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched (`corpus/lessons/round-61.md`; considerthese 2026-10-26 proposal 2 still open).
- [~] Instructions executable by an agent without oral context — evidence `corpus/knowledge/osv-determineversion-cc-library-versioning.md` recheck line (source-recheck rc 0).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `PROVINCE.md` F55 end-of-file line; scope unchanged.

## Other report items

- **Round shape:** one v1 wave `w1` of 13 seats (validated under `ufo-wave-policy.json`; `.ufo/waves/round-79/w1-dispatch.json`).
  - Roles: executor×3, scribe×2, scout×1, reviewer×3, critic×1, mutation-tester×1, sentinel×1, connector×1.
  - Attack seats: 5/13 (38 %).
  - Dead seats: 0. All 13 filed reports (`w1-results.json`, 13 seats).
  - Residual call: none. Round total: 13.
- **Planner mapping:** the L1 held the planner seat; there was no planner swarm role.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked `versions.html` and `w4lines.txt`. Neither names kasegi or round 79, so they were not written by my seats and were left untouched.
- **Scratch:** `/fast/scratch/hyaku/kasegi-r79` removed after landing.
- **Open L0 questions (routed around, not answered):** kasegi R-77-D (anchor-window semantics) and R-77-E (staged S112 id collision), `.ufo/l0-questions.md:353-354`.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
