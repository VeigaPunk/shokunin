# chousa — round 56 report

Lane: chousa-shokunin. Round start `f2b15b482062b4ad60f35377f039e2a2cfe33d67` (round-55 salvage); claim base `e5a3795191601797613eb986b36fa0b1a73fe6a1` (the late round-55 `w1-results.json`, committed under round 55) → final lane hash `b804147b55f17c78e082e05eca0eadbab47f3320` (`git -C chousa-shokunin ls-remote origin refs/heads/master` → `b804147b…`). Freeze `41c58925580af6be22049f13cfde234c5475b858`. No external fetch (L0 `8d77e6c1` open). Report filed after `WAVE-DONE chousa r56 w1` (all 69 seats settled).

## Work performed

Declared claims (frozen in `corpus/evidence/round56/claims.md`): **C1 operability** (lowest scored axis, 3/10) — the build-spans gate's clause coverage (the nine `R55MutC1Counter` mutants) and two hook bypasses; **C2 depth** (sourced) — the 灰色文献 source row of 药品临床综合评价工作流程指南, by document (rows S127–S130, held S118).

- Protocol load and closure intake (`corpus/lessons/round-55-verifier-spotcheck.md` §6, orchestrator note). Round-55 settlement: late `w1-results.json` committed under round 55 — `e5a37951`.
- Freeze `41c58925`: frozen driver `corpus/evidence/round56/c1-count.py`, gate `c1-gate.py` (round-55 counter + `_posixsubprocess.fork_exec`, `os.chdir`), probes `probes/p1-forkexec.py`, `p2-dirfd.py`, `c2-count.py`, before/control receipts in `controls/`, census start, §10 scratch `.ufo/waves/round-56/assimilation/`. Three pre-freeze counter fixes found by the L1's own controls are disclosed in `claims.md` ("Pre-freeze counter fixes").
- C1 candidate `46e1758f` — `corpus/evidence/round56/battery/` (seven violator builders, one unpinned oracle copy).
- Wave spec/dispatch `0c2f4ce5` (`.ufo/waves/round-56/gen-w1-spec.py`, `w1-spec.json`, `w1-dispatch.json`).
- C2 integration `99eff0ec`: entry `corpus/knowledge/grey-literature-field-china-r42.md`, rows S127–S130 (`corpus/SOURCES.md`), S118 `used-by`, 23 quotes built by `tools/build-spans.py` (`corpus/evidence/round56/quotes.tsv`, `spans.tsv`, held manifest `held/`), lesson `corpus/lessons/round-56.md` `## Gate`; round-55 lesson corrections D3/D4 (`corpus/lessons/round-55.md` `## Corrections`).
- After-measurements `2ceb4049` (`c1-measure-after.txt`, `c2-measure-after.txt`).
- W1 integration `98977070`: the journal row moved from 表 10 to 表7 (waves `R56GroundJournal`, `R56DraftGate`, `R56CritCurrency`), QUALITY 106–109, lesson Mistakes rows 1–3, SKILL.md rows (`build-spans` re-registered as a gate; round-56 counters), r40 `#### Corrections (round 56)`, round-55 corrections from the carried W2 items.
- C2 re-measured after the fix, SCORECARD verdict/capability/plan, LOG, README — `e129c9e4`; later carried-W2 corrections `751edb3f`; settled wave evidence, Mistakes row 4, QUALITY 110, cache-deletion incident `9d402b0e`; census end `b804147b`.
- Round shape: **one v2 wave, W1 = 69 seats** (policy v2): 33 round-56 items + the **36 never-dispatched round-55 W2 items, dispatched unchanged** (except scratch root) — none retired. Role mix: critic 16, reviewer 12, executor 11, scribe 10, mutation-tester 9, scout 6, connector 3, sentinel 2; attack share 37/69 (54 %). No residual call. **Round total 69.** Planner seat held by the L1 (no planner role in the validator).
- Seats without a report file (final output only in `w1-results.json`): `R56CritC1Forge` ("not a valid forge measurement": `CANDIDATE=0/2 … ('ENV', 2)`), `R56MutC2Counter` (reasoning fragment, no result: "We have got a candidate integration commit after assignment freeze…"), `R55W2ReviewC1Claims` and `R55W2ReviewRows` (reasoning fragments), `R55W2CritGate` (valid JSON finding, integrated). `R56MutC1Driver` INCONCLUSIVE (cache deleted mid-run). No seat replaced. 21 seat scratch dirs were left under `/fast/scratch/hyaku/chousa-r56/` (seat defect, §7); the L1 removed the tree after landing.
- Incident: the shared read-only capture cache `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/.qcache/` was deleted at about 02:16:49 -03 (git-ignored, not restorable from git; no chousa seat output names a delete). This round's after-receipts precede it (02:08:29, 02:15:51). L0 question filed — fleet `a714799f`; Main notified.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| round-55 late `w1-results.json` (round-55 settlement) | LOG "Round 56" intake | `e5a37951` |
| freeze: claims, driver, gate, probes, C2 counter, controls, census start, §10 scratch | LOG "Round 56" | `41c58925` |
| C1 candidate: battery | same | `46e1758f` |
| W1 spec/dispatch | same | `0c2f4ce5` |
| C2 entry, rows S127–S130, S118 used-by, quotes/spans, lesson Gate; round-55 D3/D4 corrections | same | `99eff0ec` |
| C1/C2 after-measurements | same | `2ceb4049` |
| W1 integration (表7 fix, QUALITY 106–109, SKILL rows, Mistakes 1–3, r40 and round-55 corrections) | same | `98977070` |
| C2 re-measure; SCORECARD, LOG, README | same | `e129c9e4` |
| round-55 correction line (later W2 reports) | same | `751edb3f` |
| `w1-results.json`, 64 seat reports, ready markers; Mistakes row 4, QUALITY 110, incident; SCORECARD post-wave notes | same | `9d402b0e` |
| census end | same | `b804147b` |

## Before → after measurements

- **C1** `python3 corpus/evidence/round56/c1-count.py` — before (gate = round-55 counter, battery = round-55 controls) `CANDIDATE=2/2 KILLED=1/9 DENIED=0/2 C1=FAIL` (`controls/c1-before.txt`); controls HOOKONLY `KILLED=1/9 DENIED=2/2`, JUNK (incl. alternating FLIP forge) `KILLED=1/9`, EMPTY `KILLED=1/9`, all FAIL (`controls/c1-controls.txt`) → after `CANDIDATE=2/2 KILLED=9/9 DENIED=2/2 C1=PASS`, two runs, measured at lane master `99eff0eca3d7440aeb96a9afac6a421759b4f704` (receipt header of `corpus/evidence/round56/c1-measure-after.txt`; C1 inputs unchanged since `46e1758f`).
- **C2** `python3 corpus/evidence/round56/c2-count.py` — before `ENTRIES=0/1 BOUND=0/4 … C2=FAIL` (`controls/c2-before.txt`); STAGED `REF_ID_UNBOUND=3 BOUND=0/4`, REWRITE `BOUND=3/4 QUOTE_ROWS=0` FAIL (`controls/c2-controls.txt`) → after `ENTRIES=1/1 BOUND=4/4 GUIDELINE_BOUND=yes NEW_GROUND=1/1 QUOTE_ROWS=23 CAPTURE_BOUND=23/23 ANCHOR_BOUND=4/4 INFERENCE_GROUNDED=1/1 C2=PASS`, measured at lane master `98977070993e2f39bc09f0379607e290c294d870` (receipt header of `corpus/evidence/round56/c2-measure-after.txt`).

## Sources & frontier

SOURCES rows 126 → 130 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); added S127 (B, the ttbz 征求意见稿), S128 (B, its 编制说明), S129 (A, the 中国药房 2025 publication), S130 (B, the centres' 2020 管理指南); touched S118 `used-by` (old: r48, r50 entries → new: + `grey-literature-field-china-r42.md`, logged in the lesson Gate). Census start/end `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` exit 0, five pre-existing W04 (`census-start.txt`, `census-end.txt`). Assimilation: theme = the grey-literature source row of the drug clinical comprehensive evaluation workflow guideline; staged r42 admitted narrowed (S168→S127, S156=S169→S128, S155→S129, S157→S130 by document); staged r44 refused (same theme, overlapping documents; flip recorded); collisions 45, guard proven (`.ufo/waves/round-56/assimilation/guard-proof.txt`); quarantine rows on theme URLs 0. Frontier advanced: what a Ⅰ级/A beside a source category grades; table placement from layout (QUALITY 109); gate clause coverage. considerthese: swept, none fits (`R56ScoutConsiderthese`).

## Trend verdicts

- **expansion — improved**: one entry on ground absent at base (`git grep -c 中国循证医学中心 e5a37951 -- corpus/knowledge` → exit 1; 6 occurrences in the entry), four new documents bound.
- **quality — improved**: the 36 never-run round-55 falsify items ran and their narrowings are appended (r40 corrections, round-55 lesson); `build-spans` is a registered gate whose every round-55 clause is shown able to fail; this round's own table misattribution was caught and fixed before filing; QUALITY 106–110.
- **discernment — unprovable-but-better** pending the non-author closure: r42 admitted with five narrowings, r44 refused; wave entailment attacks (`R56CritEntail`, `R56CritCurrency`) carried; three C1 driver attacks did not measure (open, not survived).

Stale-lane: respawn-per-round driver; no other mission of this lane open. Tool installs: none to PATH; seats used `uv run --with pypdf` (pypdf 6.21.2) and pdfplumber in uv caches; `pdftotext` 26.08.0 already installed. Open L0: `8d77e6c1` (fetch), cache deletion (`a714799f`).

## SHONEN

- [~] Craft rows: SKILL.md `build-spans` gate row and round-56 counters row (`chousa-shokunin/SKILL.md:144-145`); QUALITY 106–110.
- [~] Logged rounds: LOG.md "Round 56" with `corpus/evidence/round56/c1-measure-after.txt` and `c2-measure-after.txt`.
- [~] Runnable checks: `c1-count.py`, `c1-gate.py`, `c2-count.py`, `controls/build-c1-junk.py`, `controls/build-c2-controls.py` with receipts under `corpus/evidence/round56/`.
- [~] Province fit: evaluation content and grading systems reported as adjacent (`corpus/knowledge/grey-literature-field-china-r42.md` Unknown; `R56ReviewProvince`, `R56ConnSiblings` 0 overlaps).
