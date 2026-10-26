# souji round 29 (attempt 1) — report

Lane HEAD (pushed, `git ls-remote origin refs/heads/master` equal): `48e2e95f380090c2e587b8c39a0a7ec1ef32185c`. Base `691dd29211c53d0ef94fa072394cb9c8a69fe92e`; frozen preregistration commit `b8cb4b31ce80e2e3314b88e85d40ea9873180804` (`census/round-29/records/preregistration.txt`, controls `records/controls.tsv`, digests `records/frozen-digests.txt`).

## Work performed

Declared claims: **C1 calibration** (declared records agree with committed bytes), **C2 operability** (wave-evidence receipts verify over committed bytes), **C3 coverage** (F3 duplicate-verdict entries, sourced, assimilated from `merge/souji/`). Axes calibration 7 (lowest), operability 8, coverage 8; distinct, causally separable by landing commit; `python3 -B tools/souji-axis-check.py` `claims=3 flags=0` (`records/axis-check-before.txt`).

- Frozen counters and do-nothing/junk controls committed before any wave seat scored (b8cb4b3): C1 base `k1=6 k2=4 mismatches=10`, C2 `failed=152 uncovered=14`, C3 `0 entries / 139 rows`; junk states 6/10/68/12, 152→uncovered 14, floor 3.
- One v2 wave, 68 seats (below). Wave-1 attackers showed the frozen counters were beatable (Reviewer44 composite no-work state; Critic51 empty K2 marker; Reviewer40; Reviewer43). I landed **stricter-only amendments A1-A4** (`records/amendments.txt`) before each claim's measured commit; `census/round-29/controls-amended.sh` → `records/controls-amended.tsv`: frozen v1 counters accept the composite, amended instruments reject it (C1 `mismatches=11`, C2 `lost=152 fidelity=11 floor_violations=1 tool_unchanged=1`, C3 4 legs red).
- C1 (8aaacf5): 9 SOURCES cell edits on 6 rows (`corpus/lessons/round-29.md` old→new table), 4 append-only `R29-CORRECTION` blocks (LOG.md, SCORECARD.md, lessons/round-28.md), instrument `tools/souji-registry-agreement.py` v2 + fixture `tests/fixtures/r29-registry-agreement.py` (20 cases; v1 tool 8/20, mutant 15/20: `records/c1-fixture-red-before.txt`).
- C2 (b862007): `tools/souji-wave-evidence-capture.sh` v2 (nested `.gitignore`/`.gitattributes`/`.git` stored `.captured`, `excluded.tsv`, `symlinks.tsv`, `--verify --rev`), fixture 15 cases (base tool 8/15: `records/c2-fixture-red-before.txt`), r26 recaptured (1381 records), r29 captured by the same tool.
- C3 (1dc6785): `corpus/knowledge/duplicate-verdict-identity.md`, `duplicate-verdict-byte-equality.md`, rows S216-S219, snapshots `census/round-29/sources/`, slice/verdicts, README F3 row, PROVINCE note, SKILL classify row + 3 gate rows, QUALITY Q60-Q62.
- Lesson `corpus/lessons/round-29.md` (Gate, Findings, Receipts, Residuals, Mistakes, Wave); LOG entry; SCORECARD Round 29 table, capability rows, r30 plan.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no pathspec): untracked entries are `.tower/`, `.ufo/waves/round-30/`, `demo-cwd.txt` and tracked `.ufo/state/*`, `.ufo/watchdog.log` — none carries souji r29 content; nothing copied or deleted. Fleet `.git` was deleted/restored by a stray seat of another lane before my wave spawned (Main's message).
- Inherited: tracked `.ufo/waves/round-26/w1/ScribeGateDraft.md` edited by a parked r26 seat after a mis-addressed kasegi message; diff kept `records/stray-r26-scribegatedraft.diff`, file restored from the branch before recapture. `considerthese/` absent; no `operator-*.md` lessons present.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: counters, controls, start census, prereg | LOG Round 29 | b8cb4b31ce80e2e3314b88e85d40ea9873180804 |
| C1 repairs, corrections, v2 instrument, fixture, amendments A1-A3 | LOG Round 29 | 8aaacf518d0dc9292d5258abf7d74bdaea1b76e7 |
| C2 capture tool v2, fixture, r26 recapture | LOG Round 29 | b86200714069022954a3b498cf697d894119b45e |
| C3 entries, rows, sources, slice, docs, QUALITY/SKILL, A4 | LOG Round 29 | 1dc678500c92164b0b2bea82b934dd03d1dfbf38 |
| lesson, SCORECARD, LOG, r29 wave capture, end census | LOG Round 29 | de874ee86fcaee212bbf4a9bfa4bf49d953ccb8b |
| pointer repairs in QUALITY/SKILL | — | f4326a8799a78fa1bd6dbb5c1cb5f12adabaeb28, 48e2e95f380090c2e587b8c39a0a7ec1ef32185c |

## Before → after measurements

| claim | counting command | before (base) | after | measured commit |
|---|---|---|---|---|
| C1 | `python3 -B tools/souji-registry-agreement.py --root . --rev <full40> --list-rev b8cb4b31…` | `k1=6 k2=4 mismatches=10` rc 1 | `k1=0 k2=0 mismatches=0` rc 0 (frozen v1 and amended v2) | 8aaacf5…; re-run at 1dc6785…, 48e2e95… (`records/final-tip-measure*.txt`) |
| C2 | `python3 -B census/round-29/c2-counter.py --root . --rev <full40>` | `manifests=3 failed=152 uncovered=14 floor_violations=0` rc 1 | `manifests=3 failed=0 uncovered=0 floor_violations=0` rc 0; at tip `manifests=4` same zeros; v2 `lost=0 fidelity=0 tool_unchanged=0` (base `fidelity=11`); `--verify --rev` r26/r29 `failed=0 uncovered=0` | b862007…; tip de874ee…, f4326a8… |
| C3 | `git grep -lE '^ground: F3' <rev> -- corpus/knowledge/ \| wc -l`; row-count grep; `souji-coverage-agreement.py`; `souji-gate-check.py` (frozen args); `sources-census.sh validate`; `census/round-29/c3-integrity.py` | `0`; `139`; `grounded=13 mapped=13 dangling=0 mismatches=0` | `2`; `143`; `grounded=15 mapped=15 dangling=0 mismatches=0`; gate `entries=2 ok=2 slice_verdicts=8 slice_total=8 fail=0`; census rc 0; integrity 9/9 (4 red at base) | 1dc6785…; tip f4326a8… |

Verdicts: C1 verified on its frozen predicate; C2 verified; C3 verified. Honest disclosures (all in the lesson/SCORECARD): K1 is registry self-consistency, not a SCORECARD/SHONEN count (calibration claim only partly binds the self-assessment files); C3's `0→2` counts newly tagged entries (the held F3 entry has no `ground:` header; Critic49); the first A3 capture design excluded `.git` fixtures by digest only and was changed to byte-preserving `.git.captured` to meet the stricter floor; the landing gate at the tip still prints `findings=2` (two parser false positives on tokens inside the Q60 check cell, `census/round-`) plus `COULD-NOT-EVALUATE` (routed r28 defect 3, not addressed); the frozen prereg's SUMMARY literals omit the trailing `rev=`. No owned score changed (7/8/8). No axis harm found; the round makes no admission claim — the non-author closure rules.

## Sources & frontier

- Rows before→after: 139 → 143 — `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (git show base vs tip). Census before `records/census-start.txt` (rc 0, 35 W04), after `records/census-end.txt` (rc 0, 36 W04: one more duplicate-URL warning for S216 vs S114, no E03/E04).
- Rows added by tier: A=3 (S216 statx, S218 link, S219 cmp), B=1 (S217 Broder), all `mined`, opened 2026-10-25, quotes in the lesson `## Gate`.
- Rows touched old→new (status/used-by only): S022, S024, S025, S075, S076, S215 — table in `corpus/lessons/round-29.md`.
- Assimilation: theme **F3 duplicate verdicts** from `/home/vgpnk/Projects/shokuknow/merge/souji/` (2 entries, re-grounded; 7 staged F3-adjacent entries rejected with flips; read-only). Id lists: `records/assimilation/reg-ids` (139), `staged-ids` (134), `collisions` (31: S109-S132, S152, S210-S215); renumber map by document: campaign S117→S216 statx, S118→S217 Broder, S122→S218 link, S136→S219 cmp; guard proved on a 2/3-space indented fixture, 4-space ignored, column-zero-only pattern false-green. Quarantine slice (8 rows, `records/quarantine-slice`, `slice-verdicts.tsv`): campaign S118 hand-checked and adopted as S217 via the Princeton PDF; 7 carried from r24, three re-opened. `considerthese/`: absent in this lane.
- Mined mistake (`## Mistakes`): number-drift (r26 receipt "2 malformed" vs 152 absent), reference-drift (S215), attribution (self-ruled miss), vacuous (frozen counters beatable), two scope incidents (SwarmExecutor17 scratch clone `origin` = lane, push landed and was restored; stray parked-seat edit). Fixes shown red-before at base. QUALITY Q60-Q62 added citing the lesson.
- Sourced claim: C3 rests on S216-S219. Frontier advanced: F3 gains two entries (still frontier; no receipt class — operator decision).

## Trend verdicts

- expansion — improved: two admitted entries on F3 ground with tool-checked novelty tokens, two new capability rows; caveat above on the `0→2` baseline.
- quality — improved: r26 receipt now verifies over committed bytes (152→0), registry mismatches 10→0, S215/S024/S025 etc. re-grounded; no admitted entry failed re-check.
- discernment — unprovable-but-better pending the non-author spot-check (none on record); the lane's own attacks produced A1-A4 and Q60-Q62 grounded in lesson Mistakes.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md classify row and gate rows added; `corpus/SOURCES.md` S216-S219; `corpus/lessons/round-29.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md Round 29 entry; `census/round-26/waves` recapture `records=1381 failed=0 uncovered=0`.
- [~] Instructions executable by an agent without oral context — `census/round-29/c2-counter.py`, `tools/souji-registry-agreement.py`, `tests/fixtures/r29-registry-agreement.py` 20/20, `tests/fixtures/r28-wave-evidence-capture.sh` 15/15.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE Round 29 boundary note; SwarmScout37 sibling scan `census/round-29/waves/w1/deliver-sibling-overlap.tsv` (no sibling claims F3).

## Round shape, seats, extras

- Shape: **one v2 wave** `souji-r29-w1`, **68 seats**, round total 68, no residual call. Mix: executor 21, scribe 10, critic 8, reviewer 8, scout 7, mutation-tester 6, connector 3, sentinel 2, simplifier 2, revenger 1; flash roles 44/68; attack seats 22/68. L1 held the planner seat (data walk + freeze). Dead seats: none (68/68 reports and `w1-results.json`; its `status` field is empty for every seat). Dispatch queued behind the host cap ~70 min; one dispatcher TypeError re-driven by Main.
- Routed r28 defects: 1 → C2, 2 → C1, 3 → not addressed (landing gate over committed reports; planned r30), 4 → prereg shapes (two `rev=` omissions found), 5 → C1, 6 → prose + Q60 only.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- Open L0 questions: none appended.
- Sentinel61/62: no credential-shaped material in the newly committed r26/r29 receipts (fabricated fixtures only).
