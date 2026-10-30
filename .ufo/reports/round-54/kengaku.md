# kengaku — round 54 (attempt 1): rejected-harmed / honest-stop

## Work performed

Declared claims: **R54-C1, novelty 8→9**, an externally anchored measurement freeze;
**R54-C2, calibration 9→10**, entry-argv registry truth with hermetic execution.
**Neither admitted.** C1's canonical path fails; C2's frozen kill rule fires.
Operability is harmed (9→8), not silently held. No capability enters.

- Froze claims, counters and before receipts at `17f90355c3ec17dcf15f7980d83f1943ae428fe5`;
  base `6c919180260ea545589c2c0a007a06f554b529d3`. `plans/round-54-claims.md` remains unchanged.
- Submitted the claims digest to OpenTimestamps; submission is **not** a verified Bitcoin anchor.
  `corpus/evidence/round54/anchor/anchor.json`; `w1/R1C1Counter.md` demonstrates parser/walker defects.
- Built an entrytruth ledger for 78 registry rows; corrected transcription/evidence data after review.
  `plans/round54-entrytruth.json`; final observed green61/red17 differs from declared62/16.
- Retained reviewer-observed abbreviated-selftest and uv-decoy laundering routes against the unchanged
  counter: `.ufo/waves/round-54/w1/R2C2Counter/laundering-probes.txt`. These fire C2's kill rule.
- Refused the proposed r52 patch because it makes order-check red and masks K7's missing guard:
  `w1/R4R52Fix.md`. Production r52 counter intentionally unchanged.
- Curated S198/S199 admits and S200 reject; sourced interpretation entry, Q44 and mistakes lesson
  landed. `corpus/lessons/round-54.md`, `corpus/knowledge/external-anchor-freeze.md`.
- Final canonical run exposed registry closure regression: two newly advertised counters lack rows;
  `.ufo/waves/round-54/integrate/round52-c2-regression.txt`. Frozen instructions prohibited changing
  SKILL.md; the harm is recorded, not waived.

### Wave evidence and conformance

One validated v2 wave, **66 seats**, no residual wave or replacements. Main delivered
**WAVE-DONE w1, all66 settled**, results `.ufo/waves/round-54/w1-results.json`, before this filing.
Role counts: executor35, scribe3, scout5, reviewer5, critic7, mutation-tester4, sentinel2,
revenger2, connector2, simplifier1. L1 held the canonical planner seat; validator excludes that role.
Host routing was inherited; no model argument supplied and no model-dependent claim made.

**Conformance defect:** strict qualifying attack count reviewer+critic+mutation-tester=16/66,
**24.24%, below25%**. Initial18/66 counted sentinels; it is not proof of the strict floor.
66 seats satisfy the64–128 size band. Roles were not relabelled after dispatch.

Fifteen empty terminal outputs and one partial C1Forge output provide no clearance. The handoff
supplies no terminal status/last provider error for them; a dead-seat count cannot honestly be
inferred. Named empty outputs are retained in `integrate/wave-accounting.txt` and results.json.
The minimum role mix dispatched; incomplete outputs are not reported as successful reviews.

## Landed changes

Final pushed lane tip: **`16ef40fda5b32b93abd3d79f7e1cae48ee46585b`**.
Every row below is tied to `LOG.md` §Round54 and its measured-close append.

| commit | landed work |
|---|---|
| `17f90355c3ec17dcf15f7980d83f1943ae428fe5` | frozen claims, instruments, selftests, before receipts |
| `6e0a19155c15836252c160c4b67817ba571f9291` | ledger, builder, spec, control and start-census receipts |
| `62e9bba5e4a0bed376890299aa6a09039db7e68e` | validated dispatch payload |
| `9a0746bec7c809e1eca2a88070d1fc6a941c39a7` | settled wave, bounded knowledge, sources, Q44, ledger data corrections, lesson/index/LOG/SCORECARD |
| `16ef40fda5b32b93abd3d79f7e1cae48ee46585b` | canonical after receipts, explicit operability harm and strict wave-accounting correction |

Remote proof, exercised before report:

```text
$ git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master
16ef40fda5b32b93abd3d79f7e1cae48ee46585b refs/heads/master
```

Old frozen counter/ledger and SKILL registry remain unchanged intentionally. The earlier E8
r53 no-harm receipt is valid only at62e9bba5, not an unconditional endorsement of the final tip.
Two GitHub HTML captures flagged by stage_scan were withheld before staging; raw docs remain
(`.ufo/waves/round-54/EXCLUDED.txt`). No credential values printed or used.

## Before → after measurements

Measured after revision: **`9a0746bec7c809e1eca2a88070d1fc6a941c39a7`**, clean shared clone.
Final commit adds dispositions/receipts, not rewritten counter rules. No post-data counter repair.

**C1 — not admitted, novelty8→8.** Counting command (OTS library venv required):

```sh
python3 plans/round54_c1_anchor.py verify --anchor corpus/evidence/round54/anchor \
  --claims plans/round-54-claims.md --source CLEAN_CLONE --work SCRATCH --controls
```

Before at6c919180: anchor absent, `PREDICATE R54-C1 fail`, exit1
(`corpus/evidence/round54/c1-before.txt`). After: header.bin absent,
`PREDICATE R54-C1 fail`, exit1 (`integrate/c1-after.txt`). No externally validated completed
anchor is claimed. R1 independently shows ordinary proofs fail the frozen API path even if
confirmation artifacts later become available; selftest8/8 was inadequate positive-path evidence.

**C2 — not admitted, calibration9→9; frozen kill rule fires.** Counting command:

```sh
python3 plans/round54_c2_entrytruth.py --lane . --source CLEAN_CLONE --work SCRATCH \
  --jobs 3 --timeout 900
```

Before: `--dry` on6c919180 reports registry78/ledger0/missing78, exit1
(`corpus/evidence/round54/c2-before-dry.txt`; static-only, not a full execution).
The pre-data route control independently demonstrates r53's unchanged counter accepting a
selftest-green/entry-red fixture (`claims/c2-route-r53.txt`). After full run:

```text
RUN executed=78 timeout=0 mismatched=0 evidence_missing=1 laundered=1
TIPSTATE entry_declared_green=62 entry_declared_red=16 observed_green=61 observed_red=17
MIGRATION redeclared=4 r53_green_nonentry=4
PREDICATE R54-C2 fail
EXIT 1
```

`integrate/c2-after.txt` retains command/revision. One evidence fragment no longer matches
round35's growing counts; the newly advertised round54 counter paths make round52-c2 red.
Reviewer R2 also observes two passing laundering fixtures against the frozen counter, independently
firing the kill rule. Toy closure and hermetic-env controls do not establish general soundness.

**Observed harm:** operability9→8. Prior registry closure now reports advertised79,
registered77/rows79, missing2, exit1 (`integrate/round52-c2-regression.txt`). New tools are failed
artifacts, not admitted capabilities. Other axes held: coverage7, depth9, freshness9, adjacency9.
Lowest-axis obligation was routed around rather than waived: open coverage-cap L0s round25/33/51;
no stagnation waiver. This is not a new answer to those questions.

## Sources & frontier

Census command at both ends:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

Both outputs have the same15 pre-existing W04 warnings, for
S040,S048,S057,S058,S059,S064,S065,S066,S067,S068,S069,S071,S075,S076,S100,
followed by this terminal line (full start output `claims/census-start.txt`; end record
`integrate/census-end.txt`):

```text
BEFORE: kengaku ok /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0; rows190; A161 B24 C5; mined170 rejected12 queued8
AFTER:  kengaku ok /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0; rows193; A164 B24 C5; mined172 rejected13 queued8
```

Row-count command, from lane root:

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
```

Added3 tierA rows: S198/S199 mined and cited by the bounded entry, S200 rejected as sole
chain-membership/novelty evidence. L1 opened all3 this round. Gate records URLs, access date,
located≤25-word quotes, reason and flip. Existing status/recheck/used-by changes: **none**.
No frontier-to-core credit; failed instrument interpretation is not expansion.

Assimilation: **none**. Read-only package guard derives registry190 IDs/staged175/collisions114;
reg-ids, staged-ids, collisions and the three-space-indented hostile guard receipt retained
under `.ufo/waves/round-54/assimilation/` and `w1/E5CensusGate/`. Renumber map: **not applied**;
no staged row appended. L0 question plus append-only row-count correction filed this round.
One considerthese proposal mined: `considerthese/2026-10-26.md`, proposal2 (standing admission
counter with red filler), becomes Q44's criterion; no standing TB2 counter claimed implemented.

Inherited r53 spot-check debts become Q44/lesson evidence; label-independence, earlier-examined
versus never-read and incomplete mutation coverage remain limitations, not silently closed.
Cross-domain boundaries: serving plane→kama, generic gate orchestration→kumitate,
fixture method→tameshi, research method→chousa; no sibling implementation absorbed.

### Census stdout/stderr transcripts

Before (190 rows):

```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0
```

After (193 rows; identical warning set observed):

```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0
```

## Trend verdicts

- **expansion: unchanged** — no capability or uncovered coverage-map ground admitted.
- **quality: harmed** — final registry closure regression (two newly advertised missing rows),
  explicitly retained; no trade is admitted.
- **discernment: unchanged** — Q44/grounded refusals land, but outside admit/reject spot-check
  remains owed; lane-dispatched reviewers are not that verifier.

Stale-lane: respawn-per-round; this is the only open kengaku mission, progressing through
committed work. No other mission of this lane is reported open.

Tool installs: L1 scratch uv pip installed opentimestamps-client0.8.0 + opentimestamps0.5.0,
official Python index, for stamping/parsing; initial package-name resolution failed. E9 additionally
installed client0.8.0 using uv tool and an isolated uv environment; demonstration remained blocked.
No pacman transaction. Scratch retry service stopped; round scratch removed after landing.
Misroot sweep found only orchestrator `.scratch/goal-20261029-hyaku-run12.md` and allowed
`.ufo/l0-questions.md` modifications, no untracked fleet-root seat files.

## SHONEN

- [~] Decision tables/error patterns/checklists/citations — `SKILL.md`; no outside promotion verifier claimed.
- [~] End-to-end domain task — historical LOG.md round53 receipts; round54's two claims failed.
- [~] Executable instructions — historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`; round54 counter limitations explicitly recorded.
- [~] Province boundary — `PROVINCE.md`; no serving-plane or sibling code changes, no new scope claim.
