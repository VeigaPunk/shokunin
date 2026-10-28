# kaidoku — round 45

**Claims declared (2, distinct tied-lowest axes, frozen before data at `f762b727`):**

- **R45-C1 / depth** — `SKILL.md` `## Queue-drain craft` rule block 22: a freeze-integrity
  decision table (`trigger | arm | exit | receipt`, 10 rows, every exit cell in `{0,1,2}`)
  and its interpreter `tools/round-45/frozen-path-preflight.py`, which gains the arms the
  round-44 closure routed missing (worktree `--check-dirty`, `--require-pathspec` for a
  directory freeze, the `restored` classifier, and an `--selftest` with a red case per arm).
- **R45-C2 / calibration** — the `SKILL.md` instrument registry vs the instruments the two
  most recent frozen claim files name: six rows, first-cell path equality, an exit-code cell
  naming `0`/`1`/`2`, scored against `tools/round-45/registry-scope.json`.

Both predicates are **met by their frozen counters** at the measured revision
`f59565b782c18b0eb691bec12f52d2f80d9f5032` (amendment A3). **Both counters are also shown
non-discriminating by wave-1 attacks** — a 44-line C1 artefact and a six-fenced-row C2
artefact each score `met_target: true` (`R45W1CritC1`, `R45W1CritC2`). The landed artefacts
themselves are genuine and were read independently by those seats and by the L1; the weak
link is the measure. The round reports that state rather than claiming clean admission, and
routes the exact hardening (R45-CL13, R45-CL14).

## Work performed

- **Freeze before data.** `plans/round-45-claims.md` states each claim as one predicate whose
  every clause is a value its own instrument computes, with the do-nothing controls and the
  kill rule; `tools/round-45/{frozen-path-preflight.py,c1-counter.py,c2-counter.py}` and
  `tools/round-45/registry-scope.json` landed in the same commit (`f762b727`). Control
  receipts committed at `9ff920cd`: `controls/ctl-c1-0-do-nothing.json` (exit 1,
  `rule_blocks 21`), `controls/ctl-c2-0-do-nothing.json` (exit 1, six unregistered),
  `controls/ctl-c2-0-base-unevaluable.json` (exit 2 — the instrument does not exist at the
  base), and the three selftest receipts (preflight 11/0, c1 9/0, c2 7/0).
- **R45-C1 landed** at `e715263c`: block 22, ten rows, six resolving citations (eight after A2/A3
  added two `plans/`/lesson mentions), `S140` and the interpreter cited. Command A at that commit read `citation_resolved_rules 21/22`,
  `depth_score 9.55` — the depth proxy counts only `corpus/knowledge/` references and block 22
  had none, so the first landing would have harmed the axis it claimed to improve. **Amendment
  A1** (`1f4b27f8`) cites
  `corpus/knowledge/2026-10-25-r34b-pre-freeze-shortcut-replay-gate-stop.md:40-66` and the proxy
  returns `22/22`, `depth_score 10.0`. The predicate was not changed.
- **R45-C2 landed** at `e715263c` as `### Round-44/45 instrument registry`: six rows whose
  first cell is the exact repo-relative path, each with an exit map naming `0`/`1`/`2`, each
  read from the tool's source. Two are the rows the round-44 closure routed as missing; the
  four others are the rest of the claim-carrying set, enumerated by the scope file.
- **Freeze-integrity instrument.** `tools/round-45/frozen-path-preflight.py` rebuilt with arms
  `commit`, `restored`, `blob`, `dirty`, `pathspec` and an 11-case selftest. On real history it
  reproduces the round-44 loss: `--freeze c48f8a4b --rev c86ea508 --pathspec
  tools/round-44/control-fixtures/ --freeze-path tools/round-44/control-fixtures
  --require-pathspec` exits 1 with the eight `control-fixtures` paths in `touched`
  (`.ufo/waves/round-45/l1/preflight-c86ea508.json`), and over this round's **two** frozen
  pathspecs from `f762b727` to A3 it exits 0 `clean`
  (`…/l1/preflight-at-A3-both.json`; the same call at A2 is `…/l1/preflight-at-A2-both.json`).
- **Wave 1 falsified the measures before data** (40 seats, `.ufo/waves/round-45/w1/`). The
  load-bearing findings, each with its receipt:
  - `R45W1CritC1` — ten forgery fixtures; the cheapest green artefact is 44 lines with garbage
    rows, four line-less citations and a 4-line stub interpreter (`fx-a6-cheapest-green`).
    Also: header-cell substring match, marker counted per block not per occurrence, block
    count inflated by a top-level `- **…**` line inside a body, `IndexError` on a heading
    without the trailing space (exit 1 with empty stdout instead of 2).
  - `R45W1CritC2` — the cheapest bypass is six fenced table rows with embedded paths and a
    junk exit cell anywhere in `SKILL.md`; rows under no registry heading, in a fence or in an
    HTML comment register; first-wins dedupe is order-dependent; the exit-cell rule passes
    `0 rows, 1 column, 2 bytes`; a scope path absent at every revision registers.
    `R45W1C1SelftestFromFreeze` §4 names six further predicate-text gaps (A1–A6).
  - `R45W1RevFreezeCommit` F1 — **HIGH**: both counters' freeze arm is `git log --name-only`,
    which prints no diff for a merge commit, so a merge's own resolution edit on a frozen path
    is invisible (probe `fixtures/evil_merge_probe.sh`: preflight 1, both counters 0). The
    measured range has no merge, so the score stands; the fix cannot land this round because
    the counters are frozen.
  - `R45W1C1CounterMutants` / `R45W1C2CounterMutants` — the counters' own selftests have
    coverage holes: `rule_blocks >= 22` and a deleted marker-presence reason survive the c1
    selftest; `endswith` and any-cell lookups survive the c2 selftest.
  - `R45W1SrcGitDiffTree` F2/F5 — two record numbers were wrong and are corrected in A2 (the
    S141 quote is 20 words, not 23; the round-end census prints 14 `W04`, not 16).
  - `R45W1PreflightReplay`, `R45W1PreflightDirtyReplay` — the gate is red on the real
    `c86ea508` sweep (eight paths) and on the dirty-worktree precursor, and clean on a clean
    range; without `--pathspec` it fails closed (542 touched, of which the same eight).
  - `R45W1RevS150` — the round-44 S150 fabrication-class refusal is confirmed five for five.
- **Sources opened** (`S140`, `S141`) and the **S138 `opened`-cell over-claim corrected**
  append-only with a live top-URL fetch — see **Sources & frontier**.
- **Record.** `LOG.md` round-45 entry + claim ledger; `SCORECARD.md` `## Round 45` + the A2
  re-measurement paragraph; lesson `corpus/lessons/round-45.md` (three mined mistakes, the
  source Gate, R45-CL1..CL14). `SHONEN.md` untouched.
- **Waves.** Two v1 waves under `ufo-wave-policy.json` (band 32–64): wave 1 = 40 seats
  dispatched, of which 25 produced artefacts (18 `report.md` + 7 `row.md`/`receipt.md`
  deliverables) and 15 produced nothing; wave 2 = 36 seats. Exact seat names, role mix and the
  no-output list are under **Round shape and seats**.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `plans/round-45-claims.md` — both claims, controls, kill rules, frozen paths, satisfiability preflight | `LOG.md` `## 2026-10-28 — round 45` | `f762b727` |
| `tools/round-45/frozen-path-preflight.py` — arms commit/restored/blob/dirty/pathspec, 11-case selftest | same | `f762b727` |
| `tools/round-45/c1-counter.py` — R45-C1 predicate, 9-case selftest | same | `f762b727` |
| `tools/round-45/c2-counter.py` + `registry-scope.json` — R45-C2 predicate, 7-case selftest | same | `f762b727` |
| wave-1 spec/dispatch/registry + do-nothing controls | same | `9ff920cd` |
| `SKILL.md` rule block 22 (marker `<!-- freeze-integrity-table v1 -->`, ten rows) | same | `e715263c` |
| `SKILL.md` `### Round-44/45 instrument registry` — six rows | same | `e715263c` |
| `corpus/SOURCES.md` — S140, S141 | same | `e715263c` |
| `corpus/lessons/round-45.md` — M45-1/M45-2, Gate, routed defects | same | `e715263c` |
| `SKILL.md` amendment **A1** — block 22 cites the pre-freeze gate entry | same (`Amendment A1`) | `1f4b27f8` |
| `LOG.md` + `SCORECARD.md` round-45 record; four score receipts | — (the ledger) | `abfeda50` |
| wave-2 spec/dispatch/registry | same | `faa875bc` |
| `SKILL.md` + lesson amendment **A2** — quote/W04 corrections, CL6–CL12, block-22 precision | same (`Amendment A2`) | `fedd11bf` |
| A2 re-measurement in `SCORECARD.md`/`LOG.md` + A2 score receipts | same | `14340d41` |
| lesson M45-3 + R45-CL13/CL14 (`proxy-only-target`) | same | `92b4970c` |
| `SKILL.md` + lesson amendment **A3** — `c1-run.sh` row corrected, arm-isolation limit and `--dirty-pathspec` false-clean stated, CL15/CL16 | same (`Amendment A3`) | `f59565b7` |
| **A3 is the measured revision**: `SCORECARD.md`/`LOG.md` A3 record + A3 receipts + the regenerated wave-2 dispatch | same | `1d04c6af` |
| lesson route **R45-CL17** (the frozen scope sentence over-attributes "instrument") | same | `a63d109f` |
| **wave-1 falsification record**: 25 seat directories/reports, `r45-w1-results.json`, `w2.ready` | same | `0ee50aaf` |
| wave-2 record corrections, M45-1 evidence, CL18–CL21 | same | `e00b9f6b` |
| wave-2 seat reports (34) and its registry | same | `ef3edf4b` |

Every round-45 lane commit, in order, for the closure to walk: `f762b727` (freeze), `9ff920cd`
(wave-1 dispatch + controls), `e715263c` (landing), `1f4b27f8` (A1), `abfeda50` (record), `faa875bc`
(wave-2 spec), `fedd11bf` (A2), `14340d41` (A2 re-measure), `92b4970c` (M45-3/CL13-14), `f59565b7`
(A3 = measured revision), `1d04c6af` (A3 record + wave-2 re-dispatch), `a63d109f` (CL17), `0ee50aaf`
(wave-1 evidence), `e00b9f6b` (wave-2 record corrections), `ef3edf4b` (wave-2 seat reports),
`b142b76b` (the A3 two-pathspec gate receipt), `17ce00f0` (CL22/CL23), `84cb9da5` (SCORECARD trends
restated), plus the wave-2 seat reports committed at `ef3edf4b` and the report commit itself on the
fleet repo. `git log --format='%h %s' f762b727..main` at filing prints them all.
| wave-1/wave-2 seat reports (wave evidence) | same | final lane commit named under **Round shape and seats** |

`SHONEN.md` untouched; the only fleet-root edit is the permitted two-line `l0-questions.md` append (no template or script was edited).

## Before → after measurements

| claim | before (do-nothing control) | after (measured) | counting command | measured commit |
|---|---|---|---|---|
| R45-C1 / depth | exit 1 at the freeze: `rule_blocks 21 != 22`, `block22_present 0`, `block22_rows 0`, `block22_refs 0` (`.ufo/waves/round-45/controls/ctl-c1-0-do-nothing.json`) | exit 0: `rule_blocks 22`, `block22_present 1`, `block22_rows 10`, `block22_refs 8`, `block22_unresolved_citations []`, `block22_cites {S140 true, interpreter true}`, `preflight_selftest {cases 11, failures 0}`, `frozen_path_changed []`, `met_target true` (`…/l1/scores/c1-at-A3.json`; `rule_blocks 22`, `block22_rows 10`, `unresolved []` and `met_target true` at `e715263c`, `1f4b27f8`, `fedd11bf` and A3, while `block22_refs` grew 6 → 7 (A1) → 8 (A2/A3) as citations were added) | `python3 -I -B tools/round-45/c1-counter.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --freeze f762b727 --rev f59565b7 --json-out <OUT>` | `f59565b7` (A3) |
| R45-C2 / calibration | exit 1 at the freeze: `unregistered` = all six scope paths, `registered []`, `thin []`, `scope_size 6` (`…/controls/ctl-c2-0-do-nothing.json`); exit 2 at the base `scope file absent at rev` (`…/controls/ctl-c2-0-base-unevaluable.json`) | exit 0: `registered` all six, `unregistered []`, `thin []`, `scope_size 6`, `frozen_path_changed []`, `met_target true` (`…/l1/scores/c2-at-A3.json`; the four receipts at the earlier revisions report the same six registered paths, `unregistered []`, `thin []`) | `python3 -I -B tools/round-45/c2-counter.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --freeze f762b727 --rev f59565b7 --json-out <OUT>` | `f59565b7` (A3) |

**What these numbers do and do not establish.** They establish that the landed bytes satisfy
the frozen predicates and are unreachable by a do-nothing control (scored above) and by the
structural red cases the selftests carry (relabelled 21-block craft section, thin three-row
table, citation past EOF, missing `S140`, failing interpreter selftest; six rows naming other
tools, a bare `non-zero` exit cell, a five-path scope). They do **not** establish that a
cheapest forgery cannot reach the target: wave 1 showed it can (44-line C1 artefact; six
fenced C2 rows), and the round reports that as the measure's defect, not the landing's
(R45-CL13, R45-CL14). The genuine half is independently read: `R45W1CritC1` read the ten rows
and confirmed each arm matches the interpreter's five arms and that the interpreter's eleven
fixtures are real; `R45W1CritC2` read the six rows and confirmed exact first cells and real
verdict maps.

Axis proxies (command A): coverage `10.0 → 10.0` — `knowledge_files 138`, `mapped 138`,
`missing []`, `dangling []` at A2 (no domain surface added); depth `10.0 → 10.0` — rule blocks
`21 → 22` with `citation_resolved_rules 22/22` (the landing alone read `21/22`, `depth_score
9.55`; A1 repaired it, and A2 keeps `22/22` with `block22_refs 8`); calibration
`10.0 → 10.0` — `unregistered 6 → 0`. No axis is harmed; no proxy rises above the ceiling, so
the moves are countable row/block changes, not score increases.

## Sources & frontier

**SOURCES rows before → after:** 139 → 141
(`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`). Round-start census:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
→ `kaidoku ok`, exit 0, **14** `W04` duplicate-URL warnings. Round-end census: same command,
`kaidoku ok`, exit 0, **14** `W04` — S140/S141 add no new duplicate-URL warning; the class was
classified by `R45W1CensusDupClass` (every current `W04` is a same-URL scope variant, four of
them deliberate CORPUS-rule-2 supersession rows). An earlier draft of the lesson said 16; A2
corrects it to the measured value.

**Rows added, by tier:** 2 rows, both tier A, both `docs`, both opened this round, both cited
by block 22, quotes in `corpus/lessons/round-45.md:20-28`:

- **S140** `https://git-scm.com/docs/git-status` — HTTP 200, 99,934 bytes, page sha256
  `903e31c5…9c59ad9`, anchor `Porcelain Format Version 1`:
  "guaranteed not to change in a backwards-incompatible way between Git versions or based on
  user configuration … ideal for parsing by scripts" (21 words, excluding the elision marker).
- **S141** `https://git-scm.com/docs/git-diff-tree` — HTTP 200, 256,810 bytes, page sha256
  `f81c1e31…0c9640`, anchor `-z` / raw output format:
  "When --raw, --numstat, --name-only or --name-status has been given, do not munge pathnames
  and use NULs as output field terminators." (20 words; A2 corrects an earlier 23).

**Rows touched old → new:** S138's `opened` cell was over-claimed in round 44 (descendant
contents-API listings, not the row's own top URL — the closure's routing item 4). CORPUS rule 2
forbids editing that column, so the correction is append-only in the lesson's `### S138
correction` paragraph, with this round's live top-URL fetch as its receipt; `status` (`mined`)
and `recheck` (`180d`) are unchanged and no `used-by` row was added because no round-45 claim
cites S138. Caveat from `R45W1SrcS138Fix` F1: a `github.com` page's sha256 is not a page
identity (two fetches differ in 667 bytes of per-request nonce), so the evidence is the located
quote and the listed paths, not an HTML digest. S140/S141 enter as `mined` / `on-release` /
`used-by corpus/lessons/round-45.md`.

**Frontier rows advanced:** none — no domain surface moved. `PROVINCE.md` and
`corpus/knowledge/` are byte-unchanged from the base to A2.

**Assimilation: none.** The round-44 quarantine refusals stand (S150 fabrication-class,
re-confirmed live by `R45W1RevS150`; S113/S136/S147 present with anchor caveats; S117
unverifiable), and no admitted round-45 entry cites a staged row. `considerthese/` is absent in
this lane.

## Trend verdicts

- **expansion — unchanged.** No knowledge entry, no PROVINCE movement; the two new rows
  document a Git-documentation instrument.
- **quality — improved, on the artefact only; the distiller's objection accepted.** Stated
  support: `SKILL.md` now carries a ten-row decision table whose interpreter is red on real
  history (the `c86ea508` sweep, eight paths) and green on the round's own frozen range, with an
  11-case selftest. The wave-2 `R45W2Distill` seat falsified the *first* wording's other two
  supports — the registry credit belongs to calibration, and "the depth proxy held at 22/22" is a
  hold, not an improvement — so they are struck. Bound: the table's "actionable" test is
  structural (R45-CL13/CL14), the gate has a false-clean under `--dirty-pathspec` (R45-CL15) and
  a freeze-path-only blind spot (R45-CL18).
- **discernment — improved, with the distiller's rewording accepted.** Stated support: wave 1
  attacked both measures *before* data and found the discrimination defects and the HIGH
  merge-blindness; the record was corrected from seat measurements three times (A1's depth-proxy
  harm, A2's quote/`W04` counts, wave 2's `block22_refs` growth / wave-2 size / l0-append
  sentence); and the round mined the counterexample to its own control set (M45-3). The distiller
  struck the earlier "third slot" (the A1 self-catch, which is ordinary verification) and named
  R44-CL10 as the real third item; R44-CL10 is **only partly closed** — the `restored`
  classifier exists but is not arm-isolating (R45-CL15) and is blind to a freeze-path-only tamper
  (R45-CL18) — which is stated, not counted as closed.

## SHONEN

- `[~]` **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  block 22 (`<!-- freeze-integrity-table v1 -->`, 10 rows, 8 resolving citations, S140 +
  interpreter cited) at A2; `c1-counter` reports `block22_rows 10`,
  `block22_unresolved_citations []`.
- `[~]` **At least one end-to-end domain task executed and logged in LOG.md** — this round ran
  no domain task (instrument and record work); standing evidence is the round-42 SquashFS v3
  recursion (LOG round-42 entry, `eb8215ac`), unchanged this round.
- `[~]` **Instructions executable by an agent without oral context** — block 22's table is
  executed by `tools/round-45/frozen-path-preflight.py`; the selftest runs from the bytes at
  the measured revision (`preflight_selftest {cases 11, failures 0}` in the c1 receipt).
- `[~]` **No cross-domain bleed (PROVINCE.md still accurate)** — `PROVINCE.md` is byte-unchanged
  from the base to A2; no capability, Core row or adjacency claim was added this round.

## Wave 2 falsification record (after data)

`R45W2Distill` read 34 of the 35 peer reports and classified them: **2 claim-falsifying (both trend
labels, both adjudicated below), 30 instrument-defect, 22 record/format, 17 routed ids restated**.
Its headline is the round's strongest single statement: **no seat falsified either claim
predicate** — 11 independent seats reproduce exit 0 / `met_target true` with the recorded field
values at `e715263c`, `1f4b27f8`, `fedd11bf`, A3 and the record tip, and both mutation-testing seats
say so in their own words.

Wave 2 = 36 seats (dispatch `1d04c6af`), 34 with reports at the record; `R45W2Immutable` and
`R45W2Distill` produced no artefact. What the seats established:

- **The scores reproduce.** `R45W2C1Rerun` re-runs the C1 counter at A1, the landing and A3
  (exit 0, identical receipt apart from `block22_refs`), and re-scores the freeze control
  byte-identically (exit 1, five failing clauses). `R45W2C2Rerun` and `R45W2MutC2Landing` re-run
  the C2 counter at `e715263c`, A1, A3, `a63d109f` and `0ee50aaf` (exit 0, `registry_rows 45`,
  `unregistered []`, `thin []`). `R45W2CommandA` reproduces command A (`138/138`, `22/22`).
- **The landed bytes are what the claims describe, and the mutations that matter are killed.**
  Deleting a registry row (C2 m1) and renaming its first cell to a basename (m2) both flip the
  counter red; deleting the dirty arm or the pathspec check breaks the preflight selftest.
- **Both predicates remain non-discriminating** (R45-CL13/C14, confirmed and extended): eight pure
  filler rows, a relabelled round-42 triage table, a marker block that is not block 22, and six
  fenced rows under a non-registry heading all score `met_target: true`; the C2 counter keeps the
  first of two duplicate rows, and a scope path that exists at no revision registers.
- **New HIGH instrument defect — R45-CL18.** A path named only by `--freeze-path` is never in
  `touched` (the log is pathspec-scoped), so a tamper-then-**restore** of it exits 0 `clean` where
  block 22's row 1 declares 1; `--require-pathspec` also checks only tree freeze-paths. The round's
  own invocation (both pathspecs) is unaffected. `R45W2RestoredArm` A6 adds R45-CL19: a
  tamper+restore squashed into one commit is invisible by construction.
- **Record corrections (R45-CL21).** Wave 2 refuted three statements in the first record drafts —
  "every earlier measurement reports the same values" (`block22_refs` grew 6 → 7 → 8), "wave 2 = 32
  seats" (36), and "no fleet-root file edited" (the permitted l0 append) — all corrected in
  `e00b9f6b`. It also found the wave-2 spec/dispatch committed at `faa875bc` still carries the
  pre-A2 "16 W04" sentence; that file is frozen evidence and was not rewritten.
- **House format (R45-CL20).** The registry table is 7 columns while `PROTOCOL.md`'s schema is 8
  (`entry command` absent); widening it needs a counter change first because the exit column is
  index 3.
- **Security (R45-CL22/CL23).** No shell injection anywhere (four `subprocess.run` sites, all list
  argv), and a normal run writes only its `--json-out` and its scratch — but `--json-out
  ../../SKILL.md` overwrites the graded surface and an output path on a frozen file writes even on
  exit 2; and a newline/tab pathname is recorded C-quoted, so the `restored` arm is dead for it.
  Both routed; neither is exercised by this round's own commands.

## Round shape and seats

- Shape: **two v1 waves** under `ufo-wave-policy.json` (band 32–64). Wave 1 = 40 seats
  (dispatch `9ff920cd`; ledger `.ufo/waves/round-45/r45-w1-results.json`, 40 rows), wave 2 = 36
  seats (dispatch regenerated at `1d04c6af`); round total 76, inside the 64–128 band. Wave 1 settled as **25 artefacts / 15 no-output seats**: the no-output
  names are `R45W1CritSweepClass`, `R45W1RevControls`, `R45W1SentDeepRead`, `R45W1ProbeTmp`,
  `R45W1InhSweepEvidence`, `R45W1InhTipCounters`, `R45W1InhQualityRows`, `R45W1InhCommandA`,
  `R45W1InhBlockCount`, `R45W1InhSkillTail`, `R45W1ConnFleetOwnership`, `R45W1SimplDedupe`,
  `R45W1RevengerSweepPath`, `R45W1ScribeLessonDraft`, `R45W1DistillPredicates` — **15 job-cap
  losses**: the orchestrator filled the wave against the host's 100-job ceiling, these seats
  never spawned, and their ledger rows carry `output: null` (`r45-w1-results.json`, confirmed by
  the orchestrator's `WAVE-DONE`). No seat was replaced. The 25 that produced output are 12
  executor, 3 mutation-tester, 3 scout, 3 reviewer, 2 scribe and 2 critic seats (8 of 25 attack
  roles). Wave 1 role mix: 17 executor, 5 scout, 4 reviewer, 4 critic, 3 mutation-tester,
  3 scribe, 1 sentinel, 1 connector, 1 simplifier, 1 revenger. Wave 2 role mix: 10 reviewer,
  8 executor, 5 critic, 4 mutation-tester, 3 sentinel, 2 scribe, 1 scout, 1 simplifier,
  1 connector, 1 revenger (22 of 36 attack seats, 61%). Wave 2 settled with **35 reports of 36
  seats at filing** (`R45W2Distill` landed; `R45W2Immutable` was still running when this report was
  filed and its row is recorded as pending, not backfilled).
- Dead seats: **15 in wave 1** and **0 confirmed in wave 2** (`R45W2Immutable` was still running at
  filing; `R45W2Distill` settled), all
  recorded with `output: null` in the ledgers or as missing seat dirs; none was backfilled. Wave-1
  ledger `.ufo/waves/round-45/r45-w1-results.json` (40 rows, 25 non-empty); wave-2 ledger
  `.ufo/waves/round-45/r45-w2-results.json` when the orchestrator writes it at settlement.
- The §3 L2 floor is met inside wave 1; the L1 holds the canonical planner seat (the validator
  rejects `planner` as a swarm role), with bounded data-walks riding
  `R45W1InhSkillTail`, `R45W1RegScopeAudit` and `R45W1RevengerSweepPath`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` was read before this
  report. Three untracked fleet-root files exist — `o.bin` (2026-10-27 16:58, a Cloudflare
  challenge page) and `oldrep1.out` / `oldrep2.out` (2026-10-28 09:10/09:11, a host selftest
  transcript) — all predating this round's 12:20 launch; none names `kaidoku` or `round-45`, so
  no seat of this round misrooted, and none was touched. Wave-2 seat `R45W2Misroot` re-runs the
  sweep.
- Tool installs: **none** (no pacman transaction; the host-wide pause was respected).
- Stale-lane: none — the round was dispatched once and this is its only mission.

## Admission position

The two frozen predicates are met at A3 and the landed artefacts are genuine by independent
read, but **neither instrument is a discriminator** (R45-CL13/C14) and both counters' freeze arm
is merge-blind (R45-CL6). The round therefore reports `met (instrument non-discriminating)` and
does not ask for clean admission: the operator/closure rules. Scheduled round-46 work is the
re-freeze that pins the interpreter sha256, requires line selectors inside the validated path
set, exact header cells and marker counts for C1, and a marker-bound registry section with
exact cell-0 equality and `tool_present_at_rev` for C2, plus `-m --diff-merges=first-parent` in
both freeze arms.

## Open questions (L0)

- **L0-0 (operator, infrastructure).** The in-session dispatcher was not running for this round:
  the orchestrator consumed both `.ready` files by hand, wave 1 lost 15 of 40 seats to the shared
  job ceiling, and no wave ledger was written until it was asked for. The lane-side round contract
  assumes a live dispatcher with capacity tranches; a round that loses 37% of a wave to the cap and
  files after a manual settlement cannot claim the same evidence weight as one that does not.
- **L0-1 (operator/integrator).** Placing the freeze-integrity gate inside the fleet's sweep or
  pre-push path is not a lane edit: `scripts/hyaku/{jj-lane.sh,inline.sh,fleet-commit.sh}` are
  read-only for a lane, and round 44's loss came from a non-author sweep. The lane-side arms
  landed and are proven red; the decision is whether the fleet helper should call a
  lane-provided gate before a sweep. Honest bound (wave-2 `R45W2RevSweepPath` A5): the gate was
  run on the round's own frozen paths at the freeze and again over the A2/A3 ranges, **not**
  before each of the round's 14 commits — the substitute is a discipline, not a hook. Routed as R45-CL1 and appended to
  `.ufo/l0-questions.md`; the round does not block on it.
