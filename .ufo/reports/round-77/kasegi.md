# kasegi — round 77 report (attempt 1)

Lane: kasegi (depth + coverage, bounty and security research). Lane repo `kasegi-shokunin`, branch `master`. Lane HEAD at report time: `dd2e7dfbbf5d903305ec2d02a5354dd64d48ef67` (pushed; `git ls-remote origin refs/heads/master` = same). Watchdog: `launch kasegi round=77 … attempt=1`; no `lane-dead-no-report kasegi round=77` line, so this is the first attempt.

**Outcome: both declared claims NOT VERIFIED as declared. Honest stop. No axis score moved; nothing landed in the instrument or the knowledge tree.**

## Work performed

**Declared claims (2), frozen before any seat scored** (`.ufo/waves/round-77/claims.json`, freeze commit `539a43877809bd90b6f506e8fd24a6d871598cd5`, base `2e53fc74776824898b5c5eb914aeddc19a091157`):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4; nominal per QUALITY R58). Amend `corpus/instruments/recheck-cwd-census.py` so the case-6 RESULT limb is a consumed assertion behind a four-check gate; selftest six cases → twelve checks; five named mutant kills. **Verdict: NOT VERIFIED.** The named kill rule holds (K-M1..K-M5 all rc 1, K-M2 by assertion). The frozen statement "the case-6 RESULT limb becomes load-bearing" is falsified: consumer-side neutering (`clean_ok = True`, X1), gate-consume body neutering (X2) and relabel-detection body neutering (K-M8) each still exit 0 with `selftest cases=12 failures=0`. I reproduced X1 and X2 independently (`w1/RevengerInherited-run-X1-consumer-const.txt`, `…-X2-gateconsume-bool.txt`), and K-M8 came from MutC1 (`w1/MutC1.md`). The candidate was not landed.
- **C2 — coverage** (score 8). Admit frontier F54 on S112, the OSV.dev `POST /v1/querybatch` contract. **Verdict: NOT VERIFIED.** The B0/B5 quote receipts pass (13/13 located, `controls/c2-prerecheck-r77.txt`, rc 0). Predicate B6 (distinctness, a kill-rule clause) fails: Q07 (version rule, `S112.txt:35`), Q08 (400 Bad Request, `S112.txt:36`) and Q12 (threading variance, `S112.txt:170`) restate substance already held in admitted F51 (`corpus/knowledge/osv-post-v1-query-contract.md:21` and `:47`; `corpus/source-snapshots/round-73/S108.txt:40,41,136`). Per the rule that a miss is an honest stop, the claim was not narrowed after scoring. The knowledge entry was not admitted; the S112 row stays `queued` at `corpus/SOURCES.md:124`.

**Work items, each with its evidence pointer:**

1. Round-start load and state: lane SCORECARD, PROVINCE, corpus/README (`## Frontier`), r76 lesson and spot-check; round-start census `kasegi ok`, exit 0 (`.ufo/waves/round-77/controls/sources-census-start-r77.txt`).
2. Source capture S112 (OSV `POST /v1/querybatch`): `corpus/source-snapshots/round-77/S112.txt` (216 lines, sha256 `f3ca0465…0907`), manifest `corpus/source-snapshots/round-77/manifest.json` (13 quotes), R126 pre-freeze dry run rc 0 (`controls/c2-prerecheck-r77.txt`).
3. Base counters, do-nothing control: `controls/c1-donothing-selftest-r77.txt` (base `cases=6 failures=0`, rc 0); `controls/c1-base-realtree-census-r77.txt` (`entries=91 … restoration_only=0`, conformant, rc 0); `controls/c2-base-counters-r77.txt`.
4. C1 candidate `.ufo/waves/round-77/c1-amended-reference.py` (sha256 `18bfc439…8833`), built and rebuilt by four seats (ExecC1Verify, MutC1, SentinelC1, ReviewC1). First build failed `gate-checkids` (self-inclusion, M77-1); fixed; all receipts from the fixed bytes.
5. C1 mutant battery: five named transforms (`.ufo/waves/round-77/c1-mutant-transforms.md`, committed derivations in `controls/m1..m5`), all rc 1 with the expected classes (`w1/ExecC1Verify.md` table; MutC1 independent rebuild matched). Extra probes: K-M6, K-M7 killed; K-M8 survived (MutC1).
6. C1 survivor reproduction: X1 and X2 (RevengerInherited, reproduced by the L1; receipts above). Red-before: the r76 candidate's survivor `.ufo/waves/round-76/controls/m2b-conjunct-removed.py --selftest` still prints `cases=8 failures=0`, rc 0 (`controls/c1-redbefore-r76-survivor-r77.txt`, ExecReplay).
7. C2 counters at the freeze: registry 111 → 112, knowledge 91 unchanged, `knowledge-expected` 93/91 sort-clean, frontier `rows=53 admitted=53`, `capture-binding-check records=91 bound=91` (`controls/c2-base-counters-r77.txt`, `w1/ExecC2Counters.md`).
8. C2 distinctness: R114 subject sweep and R125 admitted-entry sweep, per clause (`w1/ScoutSurface.md`, `w1/ScoutSurface.distinctness-verdicts-r77.txt`, `w1/ReviewC2.md`). Three clauses restate held ground; the rest are new. This is the failure that stopped C2.
9. Endpoint leads: the four sibling OSV endpoint pages return HTTP 200 at the S111-navigation slugs (`get-v1-vulns/`, `post-v1-determineversion/`, `get-v1-importfindings/`, `post-v1-ubuntu-binary-to-source/`); the morning slugs were 404 (the L1 used wrong slugs). Recorded as leads, not admitted (`w1/ScoutSurface.md`).
10. Assimilation and collision check: staged `merge/kasegi/SOURCES.append.md` holds S031–S124, not S001–S094 as frozen B7 assumed; 82 ids collide with the 112-row registry, including `S112` (TC260). Nothing appended (`w1/ConnectorOverlap.md`, `ConnectorOverlap.collisions.txt`; `RevengerInherited-staged-id-collision.txt`). Routed to L0.
11. Considerthese: nothing new since `considerthese/2026-10-26.md`; none fits (`w1/ConnectorOverlap.md` §2).
12. Manifest anchor audit: Q04 (anchor 30, quote on 31) and Q05 (anchor 31, quote on 32) pass only because `source-recheck.py` checks a four-line window (`w1/ExecC2Counters.md` F1). Routed to L0; the frozen manifest is not edited.
13. Lesson: `corpus/lessons/round-77.md` (Gate, Counters, Mistakes M77-1..M77-9, Routed defects R-77-A..F).
14. Scorecard and log: `SCORECARD.md` round-77 section; `LOG.md` round-77 entry.

**Wave.** One v1 wave, `kasegi-r77-w1`, 13 seats (`.ufo/waves/round-77/w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json`): executor×3 (ExecC1Verify, ExecC2Counters, ExecReplay), scout (ScoutSurface), scribe×2 (ScribeSources, ScribeEntry), connector (ConnectorOverlap), reviewer×2 (ReviewC1, ReviewC2), critic (CriticClaims), mutation-tester (MutC1), sentinel (SentinelC1), revenger (RevengerInherited). Attack seats 5/13 (reviewer×2, critic, mutation-tester, sentinel) plus the revenger's reverse-engineering. Dead seats: **0** (13/13 returned output, no error field). Seat count 13, within the 8–16 band. The planner seat is the L1, which is the validator's frozen-topology rule. No residual call. The L2 floor (≥8 in one batched dispatch) is met by the wave.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `539a43877809bd90b6f506e8fd24a6d871598cd5` | freeze: claims.json, C1 reference and transforms, controls (m1..m5, do-nothing, red-before, R126 receipt), S112 capture and manifest, S112 registry row (`queued`) | round-77 entry |
| `4a1ab1cdb12d8b7937a21f292dcc79530866b67a` | record C1 and C2 NOT VERIFIED: `SCORECARD.md` round-77 section, `LOG.md` round-77, `corpus/lessons/round-77.md`, wave evidence | round-77 entry |
| `dd2e7dfbbf5d903305ec2d02a5354dd64d48ef67` | final wave results and late scribe drafts (C2 entry drafted, not admitted) | round-77 entry |

Not landed (by design): `corpus/instruments/recheck-cwd-census.py` (base bytes, `e666ae11…ab52a21a`); `corpus/knowledge/` (91 entries, unchanged); `corpus/README.md` and `PROVINCE.md` (no F54 block); `knowledge-expected.txt` (unchanged). The S112 row is `queued`, not `mined`.

## Before → after measurements

Each command is run in the lane checkout at the commit named.

**C1 (depth:verifiability, 4 → 4, delta 0; NOT VERIFIED)**

| measure | before (base `2e53fc74`) | after (candidate, not landed) | command |
|---|---|---|---|
| selftest | `selftest cases=6 failures=0`, rc 0 | `selftest cases=12 failures=0`, rc 0 on the candidate; survives X1, X2, K-M8 | `python3 -B <counter> --selftest` |
| real-tree census | `RECHECK-CWD entries=91 … restoration_only=0`, conformant, rc 0 | identical (candidate not landed) | `TMPDIR=<scratch>/tmp python3 -B <counter> --root . --lane <lane>` |
| named mutants | — | K-M1..K-M5 each rc 1 (expected classes) | `controls/m*.py --selftest` |

**C2 (coverage, 8 → 8, delta 0; NOT VERIFIED)**

| measure | before (base `2e53fc74`) | after (freeze `539a4387`, no admission) | command |
|---|---|---|---|
| registry rows | 111 | 112 (S112 `queued`) | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` |
| knowledge entries | 91 | 91 | `ls corpus/knowledge/*.md \| wc -l` |
| frontier | `FRONTIER-CENSUS rows=53 admitted=53 closed=53 problem-rows=0 registry=111` | `… registry=112` (no new row admitted) | `python3 corpus/instruments/frontier-recheck-count.py` |
| capture binding | `records=90 bound=90 unbound=0` | `records=91 bound=91 unbound=0` | `python3 corpus/instruments/capture-binding-check.py` |
| S112 quotes | — | 13/13 located, rc 0 | `python3 corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-77/manifest.json --source S112` |

**Depth:density** — not targeted; not re-measured; held at 9 (`r15`).

## Sources & frontier

- **SOURCES.md rows, before → after:** 111 → 112 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at `539a4387`). Malformed rows 0 (`awk` NF!=13 check). Duplicate ids 0. Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` rc 0 at start and at the lane tip, with the six inherited W04 duplicate-url warnings unchanged.
- **Rows added by tier:** A = 1 (S112, `docs`, `queued`). B = 0. C = 0.
- **Rows touched old → new:** none. S112 was added at the freeze with `status = queued`, `used-by = —`; it stays `queued` (C2 was not admitted). Registry changes for S112 are recorded in the lesson's Gate.
- **Frontier rows advanced:** none. F01–F53 unchanged; F54 not admitted.
- **Sourced claim:** C2 rests on S112 (opened 2026-11-05 at `12:22:10Z`). It is refused, so no admitted entry rests on it. C1 is instrument work.
- **Assimilation:** none (82 staged-id collisions; S112 collides with staged `TC260`; routed to L0).
- **considerthese:** none fits.
- **Corpus census (frontier step, §2b.2):** round-start `sources-census.sh validate … kasegi` exit 0; round-end rerun at the lane tip: exit 0 (see the `SOURCES:` line below).

SOURCES: rows 111 → 112 (one A-tier row, `queued`); frontier unchanged at 53/53; assimilation none.

## Trend verdicts

- **expansion: unchanged.** Knowledge 91 → 91; frontier 53 → 53. The S112 row is `queued`, not an admitted entry on uncovered ground (`corpus/lessons/round-77.md` § Gate).
- **quality: unchanged.** No admitted entry was superseded, re-verified or found stale. The instrument is byte-identical to base. Two named quality defects are recorded and routed rather than landed: the consumer-side gate survivors (M77-6) and the anchor-window rule (M77-7).
- **discernment: unchanged.** Gate decisions with outside checks: CriticClaims and ReviewC2 independently agree with the refusal of C2 (B6) and with the C1 falsification; the reject lines in the lesson are named with flip conditions. There was no admit to spot-check this round, so no admit-side agreement is claimed. The non-author closure is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author assertion; outside verification required (SKILL.md). Evidence pointer: `SKILL.md` gate-registry rows and `corpus/lessons/round-77.md`.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — not done this round (no authorized end-to-end bounty task; former roots absent; live-target testing refused). Evidence pointer: `corpus/lessons/round-61.md`.
- [~] Instructions executable by an agent without oral context — the census and counter commands above run from committed bytes (`.ufo/waves/round-77/controls/`). Evidence pointer: `corpus/lessons/round-77.md` § Counters.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — Scope unchanged; OSV ground stays bounty-adjacent source documentation; no sibling corpus absorbed (`w1/ConnectorOverlap.md` §3). Evidence pointer: `PROVINCE.md`.

## Other report items

- **Stale-lane:** no other mission of this lane is open; the wave's seats all settled (13/13).
- **Tool installs:** none. The round used only the existing host tools (`python3`, `git`, `jj`, `curl`); the authorization was read but nothing was installed or upgraded.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `M .scratch/run15-state.json` and `?? .ufo/closure-kaidoku-r92.json`, which do not name this lane or round; left untouched (not kasegi-authored, and `.scratch/` is orchestrator-owned). No fleet-root file was written by a kasegi seat.
- **Inherited state:** none. `.ufo/waves/round-77/` was created this attempt.
- **Open L0 questions (appended to `.ufo/l0-questions.md`):** (a) staged shokuknow `S112` (TC260) collision and the wrong frozen B7 premise (S031–S124, not S001–S094); (b) source-recheck anchor window vs exact-line semantics (Q04/Q05).
- **Frozen-record defect (not edited):** `claims.json` line 4 `frozen_at 2026-11-05T12:45:00Z` postdates the freeze committer stamp (`12:35:02Z`) and the dispatch marker (`12:39:55Z`). Recorded as M77-8; the frozen bytes stay as committed.
- **Pre-report gate:** `git ls-remote origin refs/heads/master` = `dd2e7dfbbf5d903305ec2d02a5354dd64d48ef67` (the final lane hash, recorded above).

## Carry-forward (for round 78 and successors)

1. C1 successor: freeze consumer-side and check-body neutering as named classes with red-before on the amended bytes (R-77-B); refuse a missing TMPDIR (R-77-A); document or fix the anchor window (R-77-D).
2. C2 successor: run the R125 admitted-entry sweep before writing predicates; claim only the batch-specific clauses (Q01–Q06, Q09–Q11, Q13) (R-77-C); resolve the staged S112 id with the operator first (R-77-E).
3. Freeze checklist: a dry run and a distinctness sweep as named steps before the claims file is written (M77-4, M77-5).
