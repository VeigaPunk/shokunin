# mori — round 47 report (L1 MoriR47, attempt 1)

Lane HEAD (pushed): `356fb94a5bdc3d206b30072744711067d18f8140` — `git -C mori-shokunin ls-remote origin refs/heads/master` prints this hash.
Entering tip `2d85e33d14198d388fd3cda9cc15ec07e57e7a53`; freeze `63eecf2738db96f46b0bd02b1b2dfd66787493d0`.

## Work performed

The round declared two claims:

- **C1 (calibration):** SKILL.md registry self-test pins reproduce from committed bytes.
- **C2 (depth):** the Linux v7.2 OOM tracepoint catalogue (FR13).

Both work a lowest-scoring axis (depth, freshness and calibration tie at 5), so the stagnation nudge did not apply. The contract, both counters and the controls were frozen at `63eecf27` before any seat ran (`.ufo/waves/round-47/contract.md`).

Work items:

- **C1 instrument.** I built `tools/mori-pin-check.py` v1. It reads pins only from each gate table's `self-test` cell and re-runs the bound `--selftest` inside a `git archive` export. It replaces round 46's `count-repins.py`, which matched text anywhere in the row (r46 closure routed defect 1). This also mines `considerthese/2026-10-25.md` suggestion 1.
- **C1 repair.** `SKILL.md:912` pinned `MORI_SOURCES_APPENDONLY_SELFTEST pass=15 fail=0`, but the tool prints `pass=22`. The pin went stale at the round-41 freeze `d72ac167` (`w1/RevPinHistory.md`). Lane commit `4dea3d09` fixed it.
- **C1 v2.** Wave-1 seats turned the frozen v1 green on junk edits: rebinding the pin's command, inline `-c` echo, weakened pins, hidden or duplicate rows, stale echoes, fenced tables and digest path escape (`w1/CritC1Predicate.md`, `w1/SentPinExec.md`, `w1/RevPinCheckCode.md`). The hardened v2 landed in `4dea3d09` and `af2250d8`. Its selftest passes 34/34. The committed junk variants score green under v1 (`evidence/v1-junk/`) and unmet under v2 (`evidence/v2/`).
- **C2 entry.** `corpus/knowledge/oom-tracepoints-r47.md` lists eight `TRACE_EVENT`s with their field sets and emitting functions, plus the reaper lifecycle and the attribution boundary: the kernel's events name the victim, never the culprit. The counter is `.ufo/waves/round-47/count-c2.py`. New source rows: S475, S476, S477 (host tracefs, read with `sudo -n` only) and S478 (ROMA full text). The C2 data landed in `4dea3d09`.
- **Quality bar.** Added QUALITY 123 (pins are calibrated only when re-run from committed bytes) and QUALITY 124 (a count of kernel objects needs the command that enumerates them). Both cite `corpus/lessons/round-47.md` M1–M3.
- **Assimilation.** One theme, FR13, from `shokuknow/merge/mori/`:
  - Admitted: staged S507's document, as lane S478, re-opened by me.
  - Refused: the staged entry's claim of "exactly three" tracepoints, and staged S501 (the lane already holds it as S262).
  - Collisions: 4 (S471–S474).
  - Quarantine slice: 3 rows, all marked unverifiable; none appended (lesson Gate).
- **Round-46 spot-check routes.** Defect 1: `count-repins.py` is retired and replaced. Defect 2: the hard-coded `rows=4` is gone with it. Defect 3: the `.scratch/MutMissing/`, `MutStaleC1/` and `MutStaleC2/` directories are deleted. Defect 4: no promotion is claimed.
- **Inherited state.** Inherited only the untracked r46 debris listed above, which I deleted; there was no earlier attempt.
- **Misroots.** The W1 sweep found none (`w1/ExecMisrootBaseline.md`: `MORI_MISROOT_CLEAN`).
- **Round shape:** two v1 waves.
  - **w1 (build + first falsifiers): 42 seats.** Roles: scribe 12, executor 12, reviewer 4, mutation-tester 4, scout 3, critic 3, connector 2, sentinel 1, simplifier 1. m_flash share 59%, attack share 26%. 41 reports are on disk. MutPinSemanticCell's report was never written because the orchestrator's kernel restarted (`w1-results.json`). That seat is also believed to have edited the tracked tool; the orchestrator restored it (lesson M4).
  - **w2 (falsify): 37 seats.** Roles: executor 14, reviewer 7, mutation-tester 5, scribe 4, critic 3, connector 2, simplifier 1, scout 1. m_flash share 51%, attack share 41%. All 37 settled (`w2-results.json`) with 37 reports on disk. Three seats returned after the first filing of this report:
    - `CritV2Junk` found five new structural false-green classes against v2 on the real registry: an un-hyphenated `selftest` header, Unicode homoglyph prefixes, an archived tool copy pinned on a brand-new row, and a fenced replacement. These limit the v2 capability row and are routed to round 48.
    - `MutV2Rebound`: the rebound conjunct is killed by the selftest.
    - `ScoutMisroot`: `MORI_MISROOT_CLEAN`.
  - **Round total: 79 seats.** No residual call. I held the planner seat. No seat died with an error at report time.
- **Tool installs:** none.

## Landed changes

Each commit is tied to the `LOG.md` "Round 47" entry:

- `63eecf27` — freeze: contract, `mori-pin-check.py` v1, `count-c2.py`, controls, v7.2 source copies, collision/quarantine scratch.
- `4dea3d09` — data:
  - `SKILL.md:912` repair, pin-check v2 and two registry rows;
  - the C2 entry, S475–S478, and S005 moved from `queued` to `mined`;
  - QUALITY 123–124, README FR13 block, lesson, w1 evidence.
- `af2250d8` — v2 closes `RevPinCheckCode` M1/M3/L1 (PIN_CHECK_SELFTEST 34/34).
- `68d66ca5` — after-receipts and w1 results.
- `dd17d927` — w2 evidence, SCORECARD/LOG round 47, lesson w2 findings, census end.
- `356fb94a` — w2 settled: results, the three late reports, lesson note.

## Before → after measurements

All after-values were measured at `af2250d8`, whose measured files are identical at `dd17d927`.

- **C1.** Counting command: `python3 <git show 63eecf27:tools/mori-pin-check.py> --repo <lane> --rev R --min-tally-pins 26 --baseline-rev 2d85e33…`. The frozen v1 sha256 is `e3ef425a…`.
  - Before (at `2d85e33`): `PIN_CHECK=unmet tally_pins=26 digest_pins=5 mismatches=1`, rc 1 (`evidence/control-c1-donothing.txt`).
  - After: `PIN_CHECK=met tally_pins=28 digest_pins=5 mismatches=0 unparsed=0 no_command=0 dropped=0`, rc 0 (`evidence/after-c1-v1-frozen.txt`; re-run by `w2/ExecRerunC1v1.md`).
  - **Verdict: unprovable.** The same frozen scorer is also green on 5 junk variants (`evidence/v1-junk/`; `w2/ExecV1JunkGreen.md`; `w2/CritC1Verdict.md`).
  - The landed change itself touched no command span (`w2/ExecDiffScope.md`). It also passes v2 (`evidence/after-c1-v2.txt`), but v2 does not replace the frozen scorer.
- **C2.** Counting command: `python3 .ufo/waves/round-47/count-c2.py R`.
  - Before (at `2d85e33`): `C2=unmet … failed=entry_absent,pins,source_row` (`evidence/control-c2-donothing.txt`).
  - After: `C2=met events=8 rows=8 name_mismatch=0 field_mismatch=0 callsite_mismatch=0 pin_mismatch=0 source_row=ok provenance=ok`, rc 0 (`evidence/after-c2.txt`; re-run by `w2/ExecRerunC2.md`).
  - Junk controls stay unmet: the staged entry fails on `table`, and the three-row claim gives `name_mismatch=5` (`evidence/control-c2-*-at-freeze.txt`).
  - **Verdict: verified (proposed)**, with the limits recorded in lesson M5.
  - Facts held under attack: `w2/ExecEntryFacts.md`, `RevEntryLifecycle.md`, `CritC2Depth.md`, `RevSourcesRows.md`.
- **No harm across axes.** `w2/RevAxisHarm.md` found SCORECARD's Axes table unchanged and no deletions.

## Sources & frontier

- **Registry rows: 247 → 251.** Counting command: `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'`, at `2d85e33` and at `68d66ca5`.
- **Tier counts:** A 216 → 220, B 14, C 17.
- **Status counts:** mined 196 → 201, queued 25 → 24, rejected 26.
- **Added:** S475 (code A), S476 (code A), S477 (own-work A), S478 (paper A).
- **Touched:** S005 status `queued` → `mined`, used-by `—` → the entry.
- **Frontier:** FR13 advanced (catalogue held; resident tracing stays frontier).
- **Census:**
  - Start: `mori ok`, rc 0, 19 W04 warnings (`evidence/census-start.txt`).
  - End: `mori ok`, rc 0 (`evidence/census-end.txt`). The one added W04 is S476's `oom_kill.c` URL, which S003 also uses.
  - Append-only gate: `round_changed=[]` (`evidence/after-appendonly.txt`).
- **Assimilation:** theme FR13. Admitted S507 → S478; refused the staged entry and staged S501. Collisions S471–S474 were resolved by document. Renumber map: staged S507 → lane S478, nothing else appended.
- **considerthese:** 2026-10-25 suggestion 1 became `tools/mori-pin-check.py` and QUALITY 123.

## Trend verdicts

- **expansion: improved.** One new admitted entry on FR13 ground the lane did not hold (it previously had only the abstract-level S262/S005), citing mined rows S475–S478 (`w2/ScribeTrends.md`, `w2/ConnTrendCross.md`).
- **quality: unchanged.** No entry was superseded or re-verified. S005 was re-opened and is byte-identical; that is a status change, not a re-verification of an entry.
- **discernment: unchanged**, pending the non-author spot-check. QUALITY 123 and 124 are lesson-backed. The in-round C1 honest stop follows the round-46 discipline.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:914-939` (Round47 registry section); `corpus/QUALITY.md:1026-1048`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:2667-2687`
- [~] Instructions executable by an agent without oral context — `tools/mori-pin-check.py --selftest` (34/34); `SKILL.md:938-939`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-16` unchanged; `corpus/knowledge/oom-tracepoints-r47.md` Boundaries (read-only, no tracer enabled)

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Open L0 questions: none.

Routed to round 48:
- v2 structural false greens (`w2/CritV2Junk.md` FG1–FG5): key the floor and baseline on table identity, and require ASCII prefixes;
- a successor `count-c2.py` with a used-by arm, matching of rows indented 0–3 spaces, and one path per cell;
- v2 selftest arms for symlink containment, the argv sub-checks and case-insensitive unparsed detection (`w2/MutV2*.md`);
- checks for line-count pins and truncated digests;
- lesson F4 citation precision (`w2/RevLesson.md`).
