# souji — round 65 (attempt 1)

## Work performed

Declared claims (2, distinct axes; frozen at `census/round-65/preregistration.txt`, freeze `d2850b3eb160ae65c1c65b93753dfec7f4153b45`):

- **C1, operability.** The receipt writer refuses (a) untracked-visibility concealment of the `status.showUntrackedFiles` config key, (b) an in-run permission-bit flip under `--allow-dirty`, (c) an in-run symlink retarget inside an untracked directory, and (d) a caller-set `GIT_INDEX_FILE` naming a nonexistent path. Frozen 19-row matrix; target `new_forgeries=0 new_honest=5 class_mismatches=0 regress=PASS`, EXIT 0. Scope is the status key, not the ignore routes (named limit).
- **C2, calibration** (lowest owned axis, score 7). Four SKILL.md statements about the writer agree with its bytes under a live-marker (anchored) read; target `findings=0 verdict=PASS`, EXIT 0.

Frontier step: git-config(1) `status.showUntrackedFiles` opened this round and admitted as S297 (`corpus/knowledge/untracked-visibility-concealment.md`; captures and slice-asserted offsets under `census/round-65/sources/`).

Work items (each with its evidence pointer):

- Instruments, probes and the M1/M5 realizability probes: `census/round-65/c1-counter.py`, `c1-matrix.tsv`, `c2-counter.py`, `c2-statements.tsv`, `census/round-65/probes/` — commit `2761f0aa4d2431b4b9abb4aa997dd3116b0b25b8`.
- Do-nothing controls and SHA pin: `census/round-65/controls/`, `census/round-65/SHA256SUMS.txt` — commit `3c5bfdc0db50785cb7b2ec60e509facf2d7e9f25`.
- Freeze: `census/round-65/preregistration.txt`; `freeze-check --substance` at the freeze → `SUMMARY claims=2 findings=0` (`census/round-65/records/freeze-check-substance-at-freeze.txt`) — commit `d2850b3eb160ae65c1c65b93753dfec7f4153b45`.
- Writer landing (C1) — `tools/souji-receipt-write.py` — commit `022cf9791ec83ca6c854733c66c84705016f4d67`. SKILL.md statements (C2) — commit `40a371d8232e89e4f50d3ece4ff8779f44c0ee4c`.
- Freeze chronology arm (`tools/souji-freeze-check.py --chronology`) — commit `16da2445088ccca15aa32c66841d878ee57a8706` (landed after the freeze; lesson M7).
- Writer docstring key-scope correction (wording only; lesson M5) — commit `af81553f23086e3fa7556d552a0d26d4a995c216`.
- SKILL.md in-run scope qualification after the frozen literal (literal kept byte-contiguous; lesson M9) — commit `494c00df5325fb5f4128d4d56548973d12c6d710`.
- S297 registry row, knowledge entry, QUALITY Q124–Q127 (Q126 and Q127 narrowed to measured scope, lesson M12/M5), LOG and SCORECARD round-65 entries, source captures — commit `a3f98054dee105fb029cfd509ada149e70dd7592`; QUALITY narrowing and SCORECARD erratum — commit `0f2fefb175f2d931cea7dc1fd7af3654d38a9401`.
- Round lesson `corpus/lessons/round-65.md` (claims, gate, mistakes M1–M12, erratum, named limits, routing), S291 `used-by` old→new, wave evidence mirror `census/round-65/wave/w1/` — commits `ef00ac570c499b5944f514abe487ebeb6f0a6f7d`, `a46e07496ddffeca19eaa8a963687dfb32cd17f9`, `494c00df5325fb5f4128d4d56548973d12c6d710`.
- Measured receipts at the final revision `494c00df`: `census/round-65/records/c1-after-494c00df.txt`, `census/round-65/records/c2-after-494c00df.txt`; receipts at earlier measured revisions retained (`c1-after-af81553f.txt`, `c2-after-af81553f.txt`, `c1-after.txt`, `c2-after.txt`). Receipts committed at `6147f02503138982ae28aa64826fc490127d2b31`; residue removal at `f6358d2cc28e8fefa28ab343f561e38e0867d791`.

Wave w1 (one v1 wave, 9 seats, policy v1 band 8–16; ready file `.ufo/waves/round-65/w1.ready`, dispatch `w1-dispatch.json`, results `w1-results.json`, WAVE-DONE received): executor 1 (`S65ExecScore`), mutation-tester 1 (`S65MutKill`), reviewer 2 (`S65ReviewerDesign`, `S65ReviewerC2`), critic 1 (`S65CriticClaims`), sentinel 1 (`S65SentinelScope`), scout 1 (`S65ScoutSources`), scribe 1 (`S65ScribeEntry`), connector 1 (`S65ConnectorOverlap`). Attack share 5/9. Planner seat held by the L1 (validator refuses a planner role). No residual call. Round total 9 seats. Dead seats: none (all 9 settled with output). Seat outputs: `census/round-65/wave/w1/` (committed mirror; `.ufo/waves/` is gitignored).

Wave findings and their dispositions (full list in `corpus/lessons/round-65.md`):

- Independent reproduction (S65ExecScore, clean clone): C1 and C2 targets reproduced; writer selftest 30/30; C1 selftest 8/8; C2 selftest 13/13; r60 regress `pass=8 fail=0`; freeze-check default output byte-identical over 34 preregistrations.
- HIGH, C2 kill-power (M10): the emission token `return` matches `returncode`; deleting the env refusal gives `findings=0`. C1 kills it. Recorded; round 66.
- HIGH, C1 kill-power (M11): a same-content symlink retarget survives a read-through mutant; not a matrix row. Recorded; round 66.
- HIGH, mode claim (M12): permission bits only (`& 0o777`); setuid, setgid and sticky are invisible. Q126 narrowed; round 66.
- HIGH, sentinel F1 (M5): `GIT_CONFIG_*` and ignore routes (`core.excludesFile`, `.git/info/exclude`, `.gitignore`) defeat the dirty check for non-status keys. Writer docstring key-scope corrected; behaviour fix routed round 66.
- HIGH, prereg false sentence (M7): the frozen preregistration says `--chronology` landed pre-freeze; it did not. Erratum appended (`R65-ERRATUM-PREREG`), prereg bytes unchanged.
- Q59 instrument refused (M8): no MACHINE BLOCK in the prereg; axis judged by hand. Disclosed.
- MEDIUM: N4 dual-seed fixture masks instrument-resolution behaviour; TSV pin is not anti-launder; env-value echo in `RECEIPT-INDEX-ENV-SET` (sentinel F4); counter excerpt bound (F5). Routed round 66.

## Landed changes

| commit | change | LOG / SCORECARD / QUALITY / SKILL tie |
|---|---|---|
| `2761f0aa` | instruments, probes | LOG Round 65 |
| `3c5bfdc0` | do-nothing controls, SHA pin | LOG Round 65 |
| `d2850b3e` | preregistration (freeze) | LOG Round 65 |
| `022cf979` | writer concealment refusals; SKILL statements | LOG Round 65; SKILL Round 65 |
| `40a371d8` | S2 after-literal wrap fix (SKILL.md) | LOG Round 65 (M3) |
| `16da2445` | freeze-check `--chronology` arm | SCORECARD capability row (Round 65); lesson M7 |
| `af81553f` | writer docstring key-scope correction (wording only) | LOG Round 65 (M5); QUALITY Q127 |
| `a3f98054` | S297 row, knowledge entry, Q124–Q127, captures, LOG and SCORECARD | LOG Round 65; SOURCES S297 |
| `ef00ac57` | round-65 lesson, S291 `used-by`, wave mirror | corpus/lessons/round-65.md |
| `0f2fefb1` | Q126/Q127 narrowed; SCORECARD erratum and kill-power dispositions | SCORECARD Round 65 corrections |
| `a46e0749` | wave-close mistakes M7–M12, erratum, named limits | corpus/lessons/round-65.md |
| `494c00df` | SKILL in-run scope qualification (literal unchanged); reviewer named limits; wave mirror refresh | SKILL Round 65; lesson |
| `6147f025` | round-65 receipts (final rev) | census/round-65/records |
| `f6358d2c` | removal of reviewer selftest scratch residue from the mirror | census/round-65/wave |

No writer behaviour changed after `40a371d8` except the docstring at `af81553f`. Behaviour fixes (`GIT_CONFIG_*` isolation, ignore-route refusal, `refs/replace`, env-value echo, symlink and setuid kill rows, `return` token) are routed to round 66.

## Before → after measurements

| claim | before (do-nothing, base bytes `4a43a4d9`) | after (measured rev `494c00df`) | counting command | evidence |
|---|---|---|---|---|
| C1 writer concealment refusals (19 rows) | `new_forgeries=12 new_honest=5 class_mismatches=12`, EXIT 1 (`census/round-65/controls/c1-do-nothing.txt`) | `new_forgeries=0 new_honest=5 class_mismatches=0 regress=PASS`, EXIT 0 (`census/round-65/records/c1-after-494c00df.txt`) | `python3 -B census/round-65/c1-counter.py --root . --matrix census/round-65/c1-matrix.tsv --base-rev 4a43a4d919c5b51ae9be859a1266ce4b11337b0b --rev 494c00df5325fb5f4128d4d56548973d12c6d710 --tool tools/souji-receipt-write.py --work DIR` | `494c00df` (writer bytes = `af81553f` = `40a371d8` except docstring at `af81553f`) |
| C2 live-marker statement agreement (4 rows) | `findings=2 verdict=FAIL` (s2 SCOPE-OVERREACH, s4 GOVERNED-STATEMENT-UNRESOLVED), EXIT 1 (`census/round-65/controls/c2-do-nothing.txt`) | `findings=0 verdict=PASS`, EXIT 0 (`census/round-65/records/c2-after-494c00df.txt`) | `python3 -B census/round-65/c2-counter.py --root . --tsv census/round-65/c2-statements.tsv --tsv-rev 2761f0aa4d2431b4b9abb4aa997dd3116b0b25b8 --rev 494c00df5325fb5f4128d4d56548973d12c6d710` | `494c00df` |

Owned scores unchanged (calibration 7, coverage 8, operability 8). The lane has no reproducible 0–10 mapping; numeric deltas are 0. Both claims verify on their frozen predicates, and both carry the HIGH kill-power gaps listed above. Admission is for the non-author closure.

## Sources & frontier

- `corpus/SOURCES.md` rows before→after: 219 → 220. Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Round-end conformance: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` → exit 0, `ok` (re-run after the S291 edit).
- Rows added by tier: A +1 (S297; tier A, docs). Rows touched old→new: S291 `used-by` `corpus/knowledge/skip-worktree-concealment.md` → `corpus/knowledge/skip-worktree-concealment.md, corpus/knowledge/untracked-visibility-concealment.md`.
- Frontier rows advanced: S297 (`mined`; cited by `corpus/knowledge/untracked-visibility-concealment.md`). No coverage-map ground newly held (`corpus/README.md` unchanged). The knowledge entry is grounded adjacent to F1/F4 (receipt hygiene).
- Sourced claim: C1's V1/V2 rows and the knowledge entry's rule cite S297 (`no - Show no untracked files.`, text offset 299360, slice assertion PASSED; `all - Show also individual files…`, offset 299437, PASSED).
- Assimilation: none. `considerthese/` does not exist (`test -e` exit 1). `shokuknow/merge/souji/MERGE-REPORT.md` read read-only: one adjacent theme named (`fleet-config-scope-resolved-r26`), not adopted; its id state (108 rows, first id S109) is stale against this registry.
- Routed frontier: `:(top)` code-kind row (operator L0 still open).

## Trend verdicts

- **expansion: unchanged.** One admitted knowledge entry and one admitted source row (S297), grounded adjacent to F1/F4, not on uncovered coverage-map ground. Evidence: `corpus/SOURCES.md` S297; `corpus/knowledge/untracked-visibility-concealment.md`.
- **quality: improved.** On the frozen matrix the base writer forges 12 of 14 refusal rows and the landed writer forges 0 with all 5 honest accepts preserved. C2 findings went 2 → 0, with SKILL statements corrected and then qualified (in-run scope). No admitted entry fails its bar; the knowledge entry is key-scoped to match the measured bytes. Evidence: `census/round-65/records/c1-after-494c00df.txt`, `c2-after-494c00df.txt`. Harm check: the writer's honest-run behaviour is unchanged on every probed honest shape (reviewer design #10). The HIGH kill-power gaps are open and named; they are not counted as improvement.
- **discernment: unchanged** (non-author spot-check pending). The outside checks disagreed with the lane's own wording and process in five places (M5 docstring overclaim, M7 false prereg sentence, M9 in-run overclaim, M10 `return` token, M12 mode scope). Each is a mined lesson row, a QUALITY criterion (Q126/Q127 narrowed; Q125 added), or a routed item. The learning-path condition "disagreement becomes a lesson that adds a grounded criterion" is met in form; the trend is held at unchanged until the closure's sampled admit and reject agree with the gate.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Round-65 table; corpus/SOURCES.md S297.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md Round 65 entry; measured C1/C2 at `494c00df`.
- [~] Instructions executable by an agent without oral context — `census/round-65/c1-counter.py --selftest`; `census/round-65/c2-counter.py --selftest`; `census/round-65/records/`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `census/round-65/wave/w1/S65ConnectorOverlap.md` (sibling scan: no souji-ground overlap; sibling counters with needle-presence checks named by path for their own lanes).

## Other report items

- Stale-lane: none. Respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. No pacman transaction; no host sysctl touched; no signal sent to a foreign process.
- Dead seats: none (9 of 9 settled with output).
- Misroot sweep (fleet root, run at filing): `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `M .scratch/run15-state.json` and `?? .ufo/closure-kaidoku-r92.json`. Neither was written by a souji seat (orchestrator-owned and another lane's closure); left in place. No souji-authored file at the fleet root.
- Pre-report gate: `git -C souji-shokunin ls-remote origin refs/heads/master` → `f6358d2cc28e8fefa28ab343f561e38e0867d791`, equal to the lane's final landed hash.
- Scratch: `/fast/scratch/hyaku/souji-r65/` removed at filing.
- Open L0 questions (existing, not re-asked): `:(top)` code-kind row; planner-seat validator limitation; MACHINE BLOCK for preregistrations (Q59 instrument refusal, M8). No new L0 line appended this round.
- Stale-state note: the counters and preregistration pin `census/round-65/c1-counter.py` sha `6401b35d…`, `c2-counter.py` sha `afd4cb54…`; both unchanged through `f6358d2c`.
