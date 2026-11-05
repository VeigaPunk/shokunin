# souji — round 68 (attempt 1)

Lane `souji` · repo `/home/vgpnk/Projects/shokunin/souji-shokunin` · base `e3c174a807e76859a89b49ff276beacf5484cd57` · lane HEAD at filing `800dfcbdd8556abf131145e2ca3dcad43482354d` (pushed; `ls-remote` checked before this report was committed) · measured writer candidate `f70da577eb1e1624cc63ab8fd0468565927d9b6a` (writer unchanged this round).

## Work performed

**Declared claims (2; frozen at `census/round-68/preregistration.txt`, freeze `8b393b1911558932eab29e74635361256afdd6e3`).**

- **C1 — calibration (lowest owned axis, score 7; bookkeeping file).** Declared-protection mismatches over the 14-mutant writer battery: mutants the frozen counter does not refute. Target after: 0 mismatches, candidate `EXIT=0`. Before: 7 of 14 refuted by the frozen round-67 counter (the do-nothing arm).
- **C2 — operability (bookkeeping file).** Verdict flips between the clean and the ambient environment of the same counter. Target after: 0 flips, both runs `EXIT=0`. Before: 35 flips with the round-67 counter.
- **Frontier step (not a claim).** Source S301 (git-replace(1)) opened this round; C1's PK6 row rests on it (sourced claim, CORPUS §2b item 4). Mistake mined: `corpus/lessons/round-68.md` § Mistakes M1–M4 (classes and captured-by in that table).

**Round shape.** One v1 wave, `w1`, of **12 seats** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16): planner held by the L1 (the validator refuses a planner role), 1 connector, 3 executors, 2 scouts, 1 scribe, 2 reviewers, 1 critic, 1 mutation-tester, 1 sentinel. Attack seats 5 of 12 (42%). Residual call: none. Dead seats: none (12 of 12 settled with output; `w1-results.json`). Seats were spawned inline by the orchestrator from `w1.ready` (`WAVE-DONE souji r68 w1`, 12 seats settled). Seat output and reports: `census/round-68/records/wave-w1/` (mirror of `.ufo/waves/round-68/`, which is gitignored).

**Work items, with evidence pointers.**

1. Protocol and lane load: `skill://shokunin`, canonical SHOKUNIN/PROTOCOL/MISSION/AXES/CORPUS/LEARNING read from `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/`; lane SCORECARD, PROVINCE, SKILL, QUALITY, corpus README and lessons r67 and r67 spot-check read (`corpus/lessons/round-67-verifier-spotcheck.md`). Routed items from round 67 dispositioned in the lesson § Routed.
2. Instruments (pre-freeze, commit `8e4e84cc`): `census/round-68/c1-counter.py` (42 rows: the round-67 31 rows plus W4, W5, W6, PK3, PK3h, PK4, PK4h, PK6, PK6h, PK7, PK7h; clean environment also scrubs `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_CEILING_DIRECTORIES`); `census/round-68/c1-matrix.tsv`; `census/round-68/mutate-writer.py` (byte-copy of the S67MutKill recipe `k67-mutants.py`); `census/round-68/battery/SHA256SUMS` (candidate `b811ee2a…` and 14 mutants). Selftest `SELFTEST cases=8 pass=8 fail=0`, `EXIT=0` (`census/round-68/controls/r68-selftest.txt`).
3. Do-nothing controls (pre-freeze, commits `8e4e84cc`, `485e370d`): the frozen r67 counter over the candidate and the 14 mutants (`census/round-68/controls/r67-counter-battery/index.txt`: 7 refuted, survivors K3, K4, K6, K7, M-CD-EMPTY, M-CD-NCABS, M-CD-ROOTREL); the r67 counter clean and ambient (`census/round-68/controls/ambient/`: flips 35); the declared r68 counter with the base writer, clean and ambient (`census/round-68/controls/c1-do-nothing.txt`, `c2-do-nothing-ambient.txt`: both `EXIT=1`, no error rows).
4. Pre-freeze probes (not claim evidence): the full 42-row counter on the candidate, which surfaced one `NameError` (M2) and one fixture defect (W4 `new=accept`, M3); both fixed before freeze.
5. Freeze (`8b393b19`): `tools/souji-freeze-check.py --substance` → `SUMMARY claims=2 findings=0` (dry run in a scratch clone first). Chronology check at the freeze: the only findings are `AFTER-MISSING`, which the after-arm closes.
6. C1 after-arm (seat `S68ExecAfterArm`; L1 recheck, below): battery sha256 15/15 match; candidate `EXIT=0`, `SUMMARY matrix=42 base_forgeries=2 base_honest=11 new_forgeries=0 new_honest=11 class_mismatches=0 regress=PASS`; 14 of 14 mutants `EXIT=1` with zero `new=error` rows (`census/round-68/records/c1-after/`, `summary.tsv`).
7. C2 after-arm (seat `S68ExecAmbient`; L1 recheck by diff): clean `EXIT=0`, ambient `EXIT=0`, flips `0` (`census/round-68/records/c2-after/`); the do-nothing remains `EXIT=1`.
8. L1 independent recheck of CAND, K1 and M-CD-SCRUB (`/fast/scratch/hyaku/souji-r68/l1recheck/`): SUMMARY and CASE lines identical to the seat's receipts.
9. Attacks (wave, results in `census/round-68/records/wave-w1/seats/`): critic `S68CriticClaims` (kill rule BROKEN on label-only and over-refusal refutations; C1 denominator BROKEN, partial); reviewer `S68ReviewerCounter` (PASS on the checks; W4 fixture path defect recorded as F2, LOW by the seat's grade and material for the reading of W4); mutation-tester `S68MutTester` (4 counter mutants: W5 cwd rule inert; W4 mode change and W6 flip noticed by both predicates; scrub removal noticed only by C2); sentinel `S68Sentinel` (no HIGH; `HOME`/`XDG_CONFIG_HOME` unscrubbed MEDIUM-1); reviewer `S68ReviewerSources` (quotes and schema PASS); scout `S68ScoutDeclared` (HIGH: 14 of 30 declared writer protections have no battery mutant); scout `S68ScoutReplace` (both quotes SUPPORTED; the decisive scratch experiment: `GIT_NO_REPLACE_OBJECTS=1` changes `git show`, `cat-file` and `status`); connector `S68Connector` (assimilation none; sibling overlap; the L1 could not reconcile the seat's GIT_NAMESPACE probe with the writer blob, which has zero occurrences of `GIT_NAMESPACE`, so that claim is not relied on).
10. Trial (seat `S68ExecTrial`, 9/9 PASS): clean, dirty-refused and dirty-with-`--allow-dirty` runs on `8b393b19`, `f70da577` and `c13fbb4e`; the lane verifier rejects writer receipts (routed).
11. Knowledge: `corpus/knowledge/replace-ref-receipt-writer.md` (scribe draft `S68Scribe`, checked by the L1 for every line citation); registry row S301 (`corpus/SOURCES.md:260`).
12. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only ` M .scratch/run15-state.json`, an orchestrator-owned file this lane does not touch. No seat wrote a file into the fleet root. Nothing copied or removed.
13. Scratch: `/fast/scratch/hyaku/souji-r68/` (L1 probes, controls, battery, seat scratch removed by the seats; L1 probe directories removed at landing).
14. Tools: none installed or upgraded by any seat or by the L1. No pacman transaction. No sysctl, sudo or kernel parameter change (the 2026-11-05 incident is not attributed to this round by any receipt here).
15. Stale-lane: none (respawn-per-round driver; no other mission of this lane is open).
16. Inherited state: the watchdog log shows `launch souji round=68` (attempt 1) and no earlier attempt of this round; no uncommitted lane-authored leftovers existed at round start.
17. L0: two questions appended to `.ufo/l0-questions.md` (round-68 C1 kill rule; writer receipt verifier). The round-67 relative-value question stays open and routed around.

## Landed changes

Lane commits (all `jj-lane.sh`, branch `master`, pushed):

| commit | what | LOG entry |
|---|---|---|
| `8e4e84cc` | pre-freeze instruments, battery, r67 do-nothing battery receipts | `LOG.md` Round 68 (claims) |
| `485e370d` | pre-freeze single red do-nothing receipts (C1, C2 ambient) | `LOG.md` Round 68 |
| `8b393b19` | freeze: `census/round-68/preregistration.txt` | `LOG.md` Round 68 |
| `800dfcbd` | after-arm records, wave evidence, S301 row, knowledge entry, QUALITY Q131–Q132, SKILL round-68 section and registry rows, SCORECARD round-68 measurements and r69 plan, corpus README frontier, lesson, LOG entry | `LOG.md` Round 68 |

Changes tied to LOG entries: the counter `census/round-68/c1-counter.py` (C1 and C2; LOG Round 68 "Claims"); the battery and matrix (C1); the knowledge entry `corpus/knowledge/replace-ref-receipt-writer.md` and S301 in `corpus/SOURCES.md` (frontier step; LOG Round 68 "Sources"); QUALITY Q131 and Q132 (LOG Round 68 "Attack findings"); SCORECARD capability row `writer mutant battery with outcome split (r68)` and the round-68 measurements (LOG Round 68). No writer byte changed (`tools/souji-receipt-write.py` at `f70da577`).

Fleet repo (`fleet-commit.sh --as souji`): this report and the two L0 lines (see below).

## Before → after measurements

**C1 — calibration (declared-protection mismatches over the 14-mutant battery).**

- Counting command (after): `python3 -B census/round-68/c1-counter.py --root . --matrix census/round-68/c1-matrix.tsv --base-rev 3639087917eaeb28719d7603110a6ec22782100e --rev f70da577eb1e1624cc63ab8fd0468565927d9b6a --tool tools/souji-receipt-write.py --work DIR` (candidate), and the same with `--new-tool <mutant>` for each battery member.
- Counting command (before, do-nothing arm): the same with `census/round-67/c1-counter.py` and the 31-row matrix.
- Before: **7 of 14 refuted** (mismatches 7); survivors K3, K4, K6, K7, M-CD-EMPTY, M-CD-NCABS, M-CD-ROOTREL (`census/round-68/controls/r67-counter-battery/index.txt`).
- After: **14 of 14 refuted**, mismatches **0**; candidate `SUMMARY matrix=42 base_forgeries=2 base_honest=11 new_forgeries=0 new_honest=11 class_mismatches=0 regress=PASS`, `EXIT=0` (`census/round-68/records/c1-after/summary.tsv`).
- Measured against: candidate `f70da577`; instruments `8e4e84cc`; freeze `8b393b19`.
- Qualification (named, not a pass): of the 14 refutations, 10 are forgeries (a receipt written over a refused state), 2 are over-refusals (M-CD-NCABS, M-CD-NCRAW), 2 are label-only (K1, M-CD-ROOTREL). W4 refutes nothing behaviourally (its poisoned copy is built at the wrong path, Q132).

**C2 — operability (verdict flips, clean vs ambient environment).**

- Counting command: `env GIT_COMMON_DIR=/nonexistent-r68-probe GIT_NAMESPACE=r68probe GIT_CEILING_DIRECTORIES=/nonexistent-r68-probe python3 -B census/round-68/c1-counter.py --root . --matrix census/round-68/c1-matrix.tsv --base-rev 3639087917eaeb28719d7603110a6ec22782100e --rev f70da577eb1e1624cc63ab8fd0468565927d9b6a --tool tools/souji-receipt-write.py --work DIR` against the clean run; flips `diff <(grep -E '^(CASE|SUMMARY|REGRESS|EXIT=)' CLEAN) <(grep -E '^(CASE|SUMMARY|REGRESS|EXIT=)' AMBIENT) | grep -c '^[<>]'`.
- Before (r67 counter): **35 flips**; ambient run `EXIT=2` (`census/round-68/controls/ambient/r67-ambient.txt`; clean `EXIT=0`).
- After (r68 counter): **0 flips**; clean `EXIT=0`, ambient `EXIT=0` (`census/round-68/records/c2-after/`); the do-nothing under ambient `EXIT=1`.
- Measured against: candidate `f70da577`; freeze `8b393b19`.
- Qualification: the tuple is three variables; `HOME`, `XDG_CONFIG_HOME`, `GIT_TRACE*` and `GIT_DISCOVERY_ACROSS_FILESYSTEM` are outside it (sentinel MEDIUM-1, LOW-1, LOW-3).

Scores: none changed (calibration 7, coverage 8, operability 8). Neither verdict is a 0–10 move.

## Sources & frontier

- **SOURCES.md rows, before → after.** Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → **223 → 224**. Malformed (`awk -F'|' … NF!=13`) → 0 after. Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`: start rc **0** (223 rows); end rc **0** (`souji ok …/corpus/SOURCES.md`, 224 rows; the W04 duplicate-URL warnings are pre-existing and status-neutral).
- **Rows added by tier.** A: 1 (S301, git-replace(1), `docs`, scope: the DESCRIPTION default rule only). B: 0. C: 0.
- **Rows touched, old → new.** None. S298 and S300 cells unchanged.
- **Frontier rows advanced.** 1: `corpus/README.md` `### Frontier (r68 replace-ref route)` (F4-adjacent, not Core); knowledge `corpus/knowledge/replace-ref-receipt-writer.md` (mined source S301, sourced claim: C1's PK6 row).
- **Mistakes mined.** 4 (`corpus/lessons/round-68.md` § Mistakes M1–M4; M1, M2 and M4 have captured-by "none"; M3 has captured-by "none").
- **Assimilation: none.** `considerthese/` absent (`test -d`); connector `S68Connector/connector.md`: no shokuknow `merge/souji/` staged theme matches the round's claims. The shokuknow staged package carries a stale 108-row baseline with ids colliding with this registry (S109–S236); nothing was appended from it.

## Trend verdicts

- **expansion: improved.** One admitted `knowledge/` entry (`replace-ref-receipt-writer.md`) on ground the coverage map did not hold (`grep -i replace corpus/README.md` finds no replace-ref route), citing the mined row S301. Admission is subject to the non-author check below.
- **quality: unchanged.** No admitted entry was superseded or re-verified this round, and the instrument changes are not entry quality. The counter's W4 row is mis-built (Q132), which this round records rather than repairs.
- **discernment: unchanged.** No non-author spot-check was run this round. The lane's own dispatched seats (critic, reviewer, sentinel) produced two QUALITY criteria (Q131 kill-rule split, Q132 fixture path), but a subagent the lane dispatched is still the lane (LEARNING.md), so these do not count as the outside check. The admitted entry's admits and rejects await a non-author spot-check (the reject to be checked: "git ls-files -v honours replace refs", rejected as SILENT in the docs).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Round 68 registry rows (`r68 writer mutant battery (C1)`, `r68 ambient-environment check (C2)`); `corpus/SOURCES.md` S301; `corpus/lessons/round-68.md` Gate
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 68 (battery of 14 writer mutants and the ambient check, run on the real landed writer; trial on three real lane revisions, `census/round-68/records/wave-w1/seats/S68ExecTrial/trial.md`)
- [~] Instructions executable by an agent without oral context — `census/round-68/preregistration.txt` (commands and expected outputs); `census/round-68/c1-counter.py --selftest` (`census/round-68/controls/r68-selftest.txt`); `census/round-68/records/c1-after/summary.tsv`; `census/round-68/records/c2-after/`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` (Core/Frontier unchanged); `corpus/README.md` `### Frontier (r68 replace-ref route)`; connector `S68Connector/connector.md` (no sibling overlap in scope)

No box is `[x]`: no non-author verifier has checked any box this round.

---

Stale-lane: none (respawn-per-round driver; no other mission of this lane is open).
Tools: none installed or upgraded this round (no pacman transaction).
Round shape: one v1 wave of 12 seats (`w1`), residual 0, dead seats 0, round total 12.
Routed to round 69: see `corpus/lessons/round-68.md` § Routed (items 1–10).
