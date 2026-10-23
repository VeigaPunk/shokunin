# tsukuroi — round 32 report (attempt 1, 2026-10-23)

Lane `tsukuroi-shokunin`, base `58cc2e0bfaa4580d47f6817537c8d5c82dbe9c92`. Lane tip: `efe6d135a557ce61186b94045831e75e12c1492a` (helper `landed efe6d135a557ce61186b94045831e75e12c1492a`, pushed). Author verdict: **honest stop.** C2 met its target. C1 met its target, but a post-data shortcut control also meets it, so C1 is not verified.

## Work performed

The round declared two claims in `SCORECARD.md` "## Round 32 — declaration, attempt 1" (commit `fe1ae02c`):

- **C1 — adjacency.** The surface is the census output. The census prints `HANDOFF ADJ-04 mori` lines for dated kill-event clusters and for boot-0 coredump entries. The counter is `tools/score-census-handoff-r32.py` and the predicate is `routed`.
- **C2 — operability.** The surface is the child environment of the eleven git-running tools. Those tools move from a deny-list to an allow-list. The counter is `tools/probe-child-env-allowlist-r32.py` and the predicate is `leaking`.

Anti-loop: rounds 30 and 31 were rejected because a content-free control reached a depth counter. This round makes no depth claim, and both counters score code behaviour on inputs generated at score time.

Work items:

- **Repairs routed by the round-31 spot-check.** Each item is in `corpus/lessons/round-32.md` § Routed defects.
  - Base receipts for eight gates: `.ufo/waves/round-32/measure/base-58cc2e0b/`.
  - The round-31 "as at base" pause-gate claim now has a receipt: `.ufo/waves/round-32/l1/r31-base-pause-gate-2077e2fa.jsonl` (exit 1, `GATE-PREMISE`).
  - The K6 receipt was re-issued through `run-receipt.py`: `w1/ExecK6Reissue/c1-K6-reissued.jsonl`, 8 of 8, exit 0.
- **Counters.** Both were built before the freeze by the w0build executors: `fe1ae02c`.
- **Pre-data control wave (w1, 34 seats).** Three findings changed the counters before any data seat ran; each change is an appended SCORECARD amendment:
  - `f28442cb`: C1 v2 adds a live-host conjunct, after a fixture-gated census passed v1 (K9 v1 receipt: 24/24, exit 0).
  - `44c8eee5`: C1 v3 adds two live views (plain, and a seeded coredump thinning) with live parity. C2 probe v2 widens random name lengths to 2–200, after the shape-keyed H4 passed probe v1.
  - All controls were re-scored under the final counters before data (`.ufo/waves/round-32/controls/final/`, README).
- **Data, three executors.**
  - C1: ExecHandoffCensus (census HANDOFF lines; selftest 97 → 101).
  - C2: ExecAllowA and ExecAllowB (twelve builders use `CHILD_ENV_BASE` plus builder-set names).
  - Integration commit: `4ac5ebaa`.
- **Falsify wave (w2, 34 seats).** Reruns, 12 per-tool reviews, mutation tests, source re-opens and record audits. Findings are in the lesson § Wave-2 results.
  - Repairs: IN-109 `found_line` after the census line shift (check-adjacency-anchors had failed at `b8bf1507`), and the owed-statements registry write scope. Commit `83b017c2`.
  - Post-data shortcut K11 found: `.ufo/waves/round-32/controls/postdata/K11/`.
- **Frontier and records.**
  - Source rows S174–S179, QUALITY 82, and Mistakes R32-FIXTURE-GATEABLE, R32-BASE-RECEIPT-MISSING, R32-CRITIC-CARD-BUILD and R32-POSTDATA-SHORTCUT.
  - Appends to `SKILL.md` (R32-H1, R32-H2, R32-E1, round32 registry), to `PROVINCE.md` (ADJ-04 handoff lines) and to LOG.
  - The axes and capabilities tables were refreshed: check-self-assessment went from exit 1 at the base (K10) to exit 0.

## Landed changes

Each change below is in the `LOG.md` "Round 32" entry. All commits are lane commits made through `jj-lane.sh`, in this order:

| Commit | Change |
|---|---|
| `fe1ae02c` | declaration, counters, base receipts |
| `f28442cb` | first pre-data amendment |
| `5dc2c9e7` | first control receipts |
| `44c8eee5` | second pre-data amendment |
| `462e40a7` | final C1 control receipts |
| `4e685163` | final C2 control receipts |
| `4ac5ebaa` | data integration: census, twelve builders, S174–S179, QUALITY 82, lesson, SKILL/PROVINCE/LOG, axes |
| `b8bf1507` | after receipts and capabilities table |
| `83b017c2` | wave-2 repairs |
| `11d762bc` | measured outcome, lesson wave-2 section, SKILL cell corrections |
| `efe6d135` | final tip gate receipts, census end, last wave-2 evidence |

## Before → after measurements

Final counters: C1 scorer v3 sha256 `f45136c3…`, C2 probe v2 sha256 `d43f95ed…`, both at `44c8eee5`. Every measurement is a `run-receipt.py` receipt.

**C1.** `python3 tools/score-census-handoff-r32.py --revision <REV>`

| Revision | routed | live_consistent | Exit | Receipt |
|---|---|---|---|---|
| `44c8eee5` (base census, K0) | 8 of 24 | false | 1 | `controls/final/K0` |
| `4ac5ebaa` | 24 of 24 | true | 0 | `measure/after-4ac5ebaa/c1-declared.jsonl` |
| `b8bf1507` | 24 of 24 | true | 0 | `measure/final-b8bf1507/c1-declared.jsonl` |

- Every control that skips the work reads exit 1 under v3: K1 0, K2 9, K3 9, K4 0, K6 24 with live false, K7 12, K9 24 with live false, K10 24 with live false.
- The positive control K8 reads 24/true/0.
- **Post-data K11 reads 24 of 24, live_consistent true, exit 0.** It uses wrong statistics in fixtures and cached host constants on live. Verdict: not verified.

**C2.** `python3 tools/probe-child-env-allowlist-r32.py --revision <REV>`

| Revision | leaking | Exit | Receipt |
|---|---|---|---|
| `fe1ae02c` | 11 of 11 | 1 | `measure/c2-before-fe1ae02c….jsonl` |
| `4ac5ebaa` | 0 of 11 | 0 | `measure/after-4ac5ebaa/c2-declared.jsonl` |
| `b8bf1507` | 0 of 11 | 0 | `measure/final-b8bf1507/c2-declared.jsonl` |

- The round-31 regression guard stays at 0 of 33.
- Controls: H1, H2, H3 and H4 read 11; H6 reads 1. The positive control H5 (empty environment) reads 0.
- Limit: the probe does not inject names on its exclusion list (HOME, TZ, TERM and the others). MutAllowlist confirms: mutants keeping HOME, TZ or TERM, and one dropping PATH, survive.
- Verdict: target met.

**Gates at tip `11d762bc`** (`measure/final-tip/`): adjacency-anchors 0, self-assessment 0, registry-coverage 0, recheck-commands 0. At `b8bf1507`: census selftest 101/101 exit 0; pause-gate 1, as at base, with a base receipt; report-red-causes 0.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`

- Start: exit 0 (`.ufo/waves/round-32/l1/census-start.txt`).
- End: exit 0, last line `tsukuroi ok` (`l1/census-end.txt`).
- Rows: 173 → 179, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

Rows added by tier:

| Tier | Rows | Status |
|---|---|---|
| A | S174 glibc 2.44 `unsecvars.h`; S175 bash 5.3 `BASH_ENV`; S176 man-pages 6.19 `environ(7)`; S177 systemd v262 `systemd-coredump` | mined |
| A | S178 cgroup-v2 `memory.events` | **rejected**, redundant with S138 |
| C | S179 Stack Overflow | **rejected**, advice contradicts the contract |

- Rows touched old → new: none.
- Sourced claim: C2 (S174–S176), with C1's dated/cumulative rule citing S177 and S138.
- Frontier: adjacency handoff lines are now executable, but delivery is unaddressed (mori declares no intake).

## Trend verdicts

- **expansion: `unchanged`.** C1 is not verified, and `PROVINCE.md` gains a handoff note but no new surface.
- **quality: `improved`.** C2's twelve builders no longer pass arbitrary ambient names; 12 reviewers found output identical. check-self-assessment went FAIL → PASS. Every base-compared gate has a receipt. One harm (IN-109) was found by wave 2 and repaired before landing.
- **discernment: `improved`.** The pre-data control wave caught three shortcuts before data. The post-data K11 was reported as a failure of C1, not narrowed away (Mistake R32-POSTDATA-SHORTCUT). The real rejects are S178 and S179, and RevSourcesRejects agrees with both.

## SHONEN

- [~] SKILL.md decision tables, cited sources: rows R32-H1, R32-H2 and R32-E1, with source columns S138 and S174–S177. RevProvinceSkillC1 reviewed them as a seat, not as a promotion verifier.
- [~] End-to-end domain task logged: the live census run now prints the handoff lines (`w2/ScoutLiveHandoff/census-live.out`). There is no non-author replay.
- [~] Instructions executable without oral context: counter and probe docstrings, and the R32-E1 check command. There is no non-author replay.
- [~] No cross-domain bleed: the ADJ-04 note keeps the OS finding with tsukuroi. Mori's declaration was re-read at `a45850f0` (ScoutMoriHead). ConnSiblingOverlap found no overlap claim.

## Round shape, seats and process

- **Shape:** a control-first pair of v1 waves, plus ordinary executor calls. Round total: **73 seats**.
- **Seats per call:**

  | Call | Seats | Roles |
  |---|---|---|
  | w0build | 2 | executor |
  | w1 (pre-data controls, recon, sources) | 34 | 10 critic, 9 mutation-tester, 7 scribe, 3 reviewer, 2 scout, 1 sentinel, 1 connector, 1 executor |
  | data | 3 | executor (1 + 2) |
  | w2 (falsify) | 34 | 25 reviewer, 4 critic, 2 mutation-tester, 2 sentinel, 1 scout |

- **Planner seat:** held by the L1.
- **Holds** (safety filter; findings not used as evidence): CtlC1Peek, CritPredicateC2 and CritPredicateC1. The L1 rebuilt CritPredicateC1's idea itself as K9 and scored it.
- **Cancelled at settle:** SentinelHandoffLine and SentinelAllowResidual.
- **Dead seats:** none.
- **Critic and reviewer cards** forbid edits and runtimes. The L1 scored the critics' control patches itself (R32-CRITIC-CARD-BUILD).
- **Misroot sweep:** none from this lane.
- **Inherited state:** none.
- **Installs:** none, by the L1 or any seat. The pacman pause held.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **L0 questions:** none.
- **Gate (real reject):** S178 (redundant) and S179 (tier C).

### Owed to the next round

- A C1 counter that varies every counted class and plants distractors.
- `_revision.clean_env` and `v4shapes` still copy the ambient environment.
- Probe exclusion-list names are untested.
- The census comment at line 500.
- S175 and S177 qualifiers.
