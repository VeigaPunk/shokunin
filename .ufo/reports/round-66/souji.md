# souji — round 66 (attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/souji-shokunin`. Lane HEAD (pushed, `ls-remote` = `b238ab1da21776c2c6e9286a8fd20e0343a14131`). Landed candidate writer `c13fbb4e1b563a78278ddc14316c20252e9a6d8d`. Freeze attempt 2 `02cc660965e027c6c6390604e50702bb06377b2e`.

## Work performed

Declared claims (2, distinct axes; frozen in `census/round-66/preregistration-attempt2.txt`):

- **C1 — operability (receipt-binding surface).** The receipt writer refuses caller-injected `GIT_CONFIG_*` and object-redirect environment routes, pins the config routes on every git call, records full permission bits (setuid, setgid, sticky) in the in-run snapshot, and refuses a same-content symlink retarget, on a frozen 28-row matrix. Lowest-axis rule not applicable (C2 is the lowest-axis claim).
- **C2 — calibration (lowest owned axis, score 7; bookkeeping-file surface).** The SKILL.md statement population `s1`–`s5` agrees with the writer bytes under the live-marker read, and the round-66 counter kills the M-ENV mutant that the round-65 counter scored as live (round-65 M10).

Work items, with evidence:

- Protocol load: MISSION.md, AXES.md, lane SKILL/PROVINCE/SCORECARD/QUALITY/README, lessons 64–65 and the round-65 spotcheck (`corpus/lessons/round-65-verifier-spotcheck.md`, closure: both r65 claims verified, no axis harmed). Routed r65 items were mapped in the critic seat's table (`.ufo/waves/round-66/w1/S66CriticClaims/critic.md` §1).
- Frozen instruments: `census/round-66/c1-counter.py` (28 rows, `c1-matrix.tsv`), `c2-counter.py` (M10 token repair, `RETURN_LITERAL`), `c2-statements.tsv`, `c2-mutate.py` (M-ENV recipe). Commit `4576f101a9200206de00ef00923dd38a7b2dbc7d`.
- Do-nothing controls: `census/round-66/controls/c1-do-nothing.txt` (base writer, `new_forgeries=8`, EXIT 1), `c2-do-nothing.txt` (`findings=1`, EXIT 1). Commit `4864c01f112c9f423def430d9b6e01bdc0e21f36`.
- Freeze chronology errors, disclosed (lesson M1, M2): freeze attempt 1 `5d17a5de` landed with a headerless C2 control (`--substance`: 4 findings); an in-place append `01bc1e16` edited that frozen file, restored by `a81280e1`; the freeze was re-issued at a new path (attempt 2) with the header-complete control. No candidate existed before attempt 2.
- Wave `w1` (10 seats, policy v1 band 8–16, attack share 5/10): see the Wave section below and `census/round-66/wave/w1/`.
- Candidate integration (L1): `tools/souji-receipt-write.py` copied from the executor's bytes (sha256 `a8c47d36…97fc`, verified against CANDIDATE-READY), reviewed by the L1 against the spec (env gates presence-based and name-only; every git call pinned; mode mask `0o7777`; GIT_INDEX_FILE block shape kept; three additive selftest cases). Committed `c13fbb4e`.
- Measurements at `c13fbb4e` (below).
- Mutation kill power: wave `S66MutKill` built eight mutants of the candidate; four killed (K1, K2, K5, K8), four survived (K3, K4, K6, K7). L1 re-measured M-ENV at the landed revision in a scratch clone (mutant commit `0c8c5f4b`, scratch only, identity `S66Seat`).
- Residual-route probe, committed: `census/round-66/probes/w2-w3-env-probe.sh` and `.txt` — W2 `GIT_COMMON_DIR` route open on the candidate (accepted rc 0; a tracked mode change hidden); W3 writer under `git -c` refused on the candidate (`RECEIPT-ENV-CONFIG-SET`, rc 2; base rc 0).
- Sources: S298 (git(1) ENVIRONMENT VARIABLES) and S299 (git-config(1)), opened 2026-11-05, HTTP 200. Captures and quotes in `census/round-66/sources/`; the knowledge entry `corpus/knowledge/caller-env-routes-receipt-writer.md` cites both.
- Lesson `corpus/lessons/round-66.md` (claims, gate, Mistakes M1–M8, named limits, routed items, verdicts), LOG entry, SCORECARD round-66 table and capability row, QUALITY Q128 and Q129 (Q129 corrected append-only in the lesson), SKILL.md round-66 section.

Wave `w1` (10 seats, all settled with output, dead seats: none; `census/round-66/wave/w1-results.json` and `.ufo/waves/round-66/w1-results.json`):

- `S66ExecWriter` (executor): candidate bytes and a frozen-counter run in a scratch clone; CANDIDATE-READY.
- `S66MutKill` (mutation-tester): kill matrix 4/8 (survivors named above), K0 control matches the frozen do-nothing.
- `S66ReviewerDesign` (reviewer): no HIGH or MEDIUM on the candidate; LOW items recorded (frozen docstring overstates base behaviour, M6).
- `S66ReviewerC2` (reviewer): MEDIUM-1, the M10 selftest case is vacuous (binds row s3); LOW-1, `RETURN_LITERAL` matches five non-refusal literal returns (no marker effect).
- `S66CriticClaims` (critic): C1 unprovable as worded (`GIT_COMMON_DIR`, `GIT_CONFIG_GLOBAL` "refuses" wording, setgid unmeasured); C2 would-reject (not separable from C1; s5 scope overreach); routed-item table.
- `S66SentinelScope` (sentinel): no HIGH or MEDIUM; env values not echoed; `GIT_CONFIG_GLOBAL` repoint cannot read or write a real global config; LOW-3 (other git-resolution names unrefused).
- `S66ScoutSources` (scout): git captures, quotes with byte offsets (re-sliced by L1: all match), absences table.
- `S66ScribeEntry` (scribe): drafts (entry, s5 literal, SOURCES rows, lesson skeleton); the L1 wrote the landed versions.
- `S66ConnectorOverlap` (connector): no sibling overlap; shokuknow souji merge package has no overlapping theme.
- `S66RevengerProbe` (revenger): probes P1–P9 on git 2.56.0 (`census/round-66/wave/w1/S66RevengerProbe/probe.txt`).

Seat-level note: `S66ReviewerDesign.md` contains some garbled passages (wording fragments unrelated to the round). The L1 verified the substantive findings (candidate sha, HIGH/MEDIUM absence) independently and does not rely on the garbled parts.

## Landed changes

| change | commit | LOG entry | evidence |
|---|---|---|---|
| Frozen instruments (C1 counter and matrix, C2 counter and population, M-ENV recipe) | `4576f101a9200206de00ef00923dd38a7b2dbc7d` | Round 66 entry, "Freeze chronology" | `census/round-66/c1-counter.py` sha `273d6fc9…`, `c2-counter.py` sha `ac2157e6…` |
| Do-nothing controls (header-complete C2) | `4864c01f112c9f423def430d9b6e01bdc0e21f36` | same | `census/round-66/controls/` |
| Freeze attempt 1 (superseded) | `5d17a5deaf75328439fe66ae19b06d4b0151391e` | same | `census/round-66/preregistration.txt` (restored bytes) |
| Freeze attempt 2 (operative) | `02cc660965e027c6c6390604e50702bb06377b2e` | same | `census/round-66/preregistration-attempt2.txt`; `freeze-check --substance` `claims=2 findings=0` |
| Candidate writer, SKILL r66 section, QUALITY Q128/Q129 | `c13fbb4e1b563a78278ddc14316c20252e9a6d8d` | same | `tools/souji-receipt-write.py`; `corpus/QUALITY.md` lines 340–345 |
| Records, sources, probe, wave mirror, knowledge entry, S298/S299, lesson, LOG, SCORECARD | `b238ab1da21776c2c6e9286a8fd20e0343a14131` | same | `census/round-66/**`, `corpus/SOURCES.md` lines 257–258, `corpus/knowledge/caller-env-routes-receipt-writer.md`, `corpus/lessons/round-66.md` |

Named corrections landed in the same commit: lesson M3 pointer; LOG Tools line (no sysctl attributed to this round). The wave's S66ReviewerDesign garbled passages are left as filed (wave evidence, not edited).

## Before → after measurements

**C1** (counting command: `python3 -B census/round-66/c1-counter.py --root . --matrix census/round-66/c1-matrix.tsv --base-rev 045e103478fa4a7eff77db2cab5b9e2f26959a0a --rev <commit> --tool tools/souji-receipt-write.py --work DIR`):

- Before (do-nothing, base bytes in the new slot; measured at base `045e1034`): `SUMMARY matrix=28 base_forgeries=8 base_honest=5 new_forgeries=8 new_honest=5 class_mismatches=8 regress=PASS`, `EXIT=1` (`census/round-66/controls/c1-do-nothing.txt`).
- After (measured at `c13fbb4e`): `SUMMARY matrix=28 base_forgeries=8 base_honest=5 new_forgeries=0 new_honest=5 class_mismatches=0 regress=PASS`, `EXIT=0` (`census/round-66/records/c1-after.txt`). Forgeries 8 → 0; honest accepts 5/5 kept.
- Writer selftest on landed bytes: `cases=33 pass=33 fail=0` (`census/round-66/records/writer-selftest.txt`).

**C2** (counting command: `python3 -B census/round-66/c2-counter.py --root . --tsv census/round-66/c2-statements.tsv --tsv-rev 4576f101a9200206de00ef00923dd38a7b2dbc7d --rev <commit>`):

- Before (do-nothing, base `045e1034`): `SUMMARY rows=5 findings=1 verdict=FAIL`, `EXIT=1` (s5 absent at base; `census/round-66/controls/c2-do-nothing.txt`).
- After (`c13fbb4e`): `SUMMARY rows=5 findings=0 verdict=PASS`, `EXIT=0` (`census/round-66/records/c2-after.txt`).
- Kill power on M-ENV (scratch mutant `0c8c5f4b` at the landed revision; `census/round-66/records/c2-mutant-m-env.txt`): round-66 counter `findings=1 verdict=FAIL` (`SCOPE-OVERREACH s2`, `env=0`), EXIT 1; round-65 counter `findings=0 verdict=PASS`, EXIT 0 (the round-65 M10 survival, reproduced). Before of the repair = the round-65 result; after = the round-66 result.
- C2 selftest `cases=14 pass=14` (the M10 case inside is vacuous, see below).

Both frozen predicates are met. Neither is admitted as harm-free (below).

**Named defects found by the wave and disclosed (not fixed in this round):**

- **Vacuous M10 selftest case** (`S66ReviewerC2` MEDIUM-1): `m10-returncode-line-not-live` binds row s3, so it passes with the repair reverted. Q129's check text is corrected by append in the lesson; the frozen counter is not amended. Routed r67.
- **`GIT_COMMON_DIR` route open on the candidate** (W2, `census/round-66/probes/w2-w3-env-probe.txt`): base and candidate both accept a tracked 755→644 change when `GIT_COMMON_DIR` points at a copy whose config sets `core.fileMode=false` (rc 0, no `--allow-dirty`). The same config key in the repository's own config is the same read. Not in the six frozen names. Routed r67.
- **Honest-run refusal cost** (W3, same probe): a writer launched with `GIT_CONFIG_PARAMETERS` set (git sets it for children of `git -c`) is refused by the candidate (rc 2, `RECEIPT-ENV-CONFIG-SET`) and accepted by base (rc 0). A trade under AXES.md; operator ruling.
- **Kill power of C1**: four of eight mutants survive the frozen matrix (K3 and K4 redundant for E3; K6 and K7 need fixtures no row creates).
- **C2 scope overreach**: s5 "closed for the caller-injected config and object-redirect routes" is universal and C2 cannot falsify it (critic items 1, 5; the W2 route above is the falsifier). The population is frozen; the scope is restated in the SKILL section and the entry's named limits.
- **Receipt grammar, C1 after-receipt**: `census/round-66/records/c1-after.txt` begins with `rev=045e103…` (the counter writes the base revision first; the measured revision is in `command=`). `tools/souji-freeze-check.py --chronology` therefore reports `RECEIPT-MEASURED-BEFORE-FREEZE` for C1 (`SUMMARY claims=2 findings=1`, rc 1 at `b238ab1d`). C2's after-receipt begins with the measured revision and passes. The receipt is not edited in place; the counter's receipt grammar is routed r67.

## Sources & frontier

- SOURCES before → after: 220 → 222 rows. Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`. Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` rc 0 before and after (`ok`).
- Rows added by tier: S298, S299 — tier A (docs, git-scm.com). Rows touched old→new: none (S297 unchanged).
- Entry `corpus/knowledge/caller-env-routes-receipt-writer.md` (`status: mined`, F4-adjacent receipt hygiene). Sourced claim (CORPUS.md §2b item 4): C1 rests on S298/S299 through this entry.
- Frontier rows advanced: none. No coverage-map row in `corpus/README.md` changed.
- Assimilation: none (`considerthese/` absent; the shokuknow souji merge package read read-only, no overlapping theme).
- Mined mistakes: `corpus/lessons/round-66.md` § Mistakes M1–M8 (captured-by recorded per row; M4, M5 not captured by any criterion, routed).

## Trend verdicts

- **expansion: unchanged.** Two registry rows and one knowledge entry on F4-adjacent ground; no coverage-map ground moved, no frontier row advanced.
- **quality: improved, with a named trade.** Frozen-matrix forgeries 8 → 0; honest accepts kept 5/5; the `git -c` refusal cost (W3) and the open `GIT_COMMON_DIR` route are recorded and not hidden. Operator ruling needed on the trade.
- **discernment: unchanged.** The M-ENV kill moved from 0 to 1 on the round-65 mutant, but the vacuous selftest guard and the s5 overreach are disclosed defects that this round's frozen predicates could not repair.

Claim admission (for the operator to rule; no verdict is pre-empted):

- C1: frozen target met at `c13fbb4e`. Not admitted as harm-free: `GIT_COMMON_DIR` open (measured), `git -c` trade (measured), setgid unmeasured, receipt-grammar finding under `--chronology`.
- C2: frozen target met at `c13fbb4e`; M-ENV kill measured. Not admitted as scope-correct: the critic's would-reject on the s5 literal stands (named limit).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` round-66 section (gate-registry rows for `c1-counter.py` and `c2-counter.py`); `corpus/SOURCES.md` S298–S299; `corpus/lessons/round-66.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` Round 66 entry (candidate landed and measured end to end, freeze chronology, wave, probe).
- [~] Instructions executable by an agent without oral context — evidence: the counter commands above run from the committed bytes (`census/round-66/records/c1-after.txt`, `c2-after.txt`, `c2-mutant-m-env.txt`); `census/round-66/probes/w2-w3-env-probe.sh`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` receipt-writer surfaces unchanged; connector overlap scan `.ufo/waves/round-66/w1/S66ConnectorOverlap.md` (no sibling overlap); `census/round-66/wave/w1/S66ConnectorOverlap.md`.

No box is marked `[x]`: no non-author verifier has checked any box this round.

## Wave / round shape

- Round shape: one v1 wave, 10 seats (band 8–16), dispatched via ready-file handoff (`.ufo/waves/round-66/w1.ready`, orchestrator `w1.ready.dispatched`); WAVE-DONE received; results `.ufo/waves/round-66/w1-results.json`.
- Seat-role mix: executor 1, mutation-tester 1, reviewer 2, critic 1, sentinel 1, scout 1, scribe 1, connector 1, revenger 1. Attack seats 5/10 (50%). Planner held by the L1 (validator refuses planner).
- Residual call: none. Round total: 10 seats. Dead seats: none.
- Spec and dispatch: `census/round-66/wave/w1-spec.json`, `w1-dispatch.json`, `make-spec.py`.

## Misroot sweep and fleet-root state

`git -C /home/vgpnk/Projects/shokunin status --porcelain` (run before this report): ` M .scratch/run15-state.json`, `?? .ufo/closure-kaidoku-r92.json`, `?? cases_A.json`. The first two are orchestrator and another lane's files. `cases_A.json` is another lane's file (member `llm-inference-batching-scheduler`, revision `2fd12b88…`, written 12:05); this lane's seats wrote no fleet-root file. Left untouched.

## Stale-lane

No other mission of this lane is open (respawn-per-round); nothing left in progress.

## Tool installs

None. No pacman transaction. The host git (2.56.0) and Python (3.14.8) were used as found.

## Open L0 questions

Appended to `.ufo/l0-questions.md` (see the fleet-commit below):

1. `souji | round-66 |` operator ruling on the honest-run refusal trade: a writer launched under `git -c` is refused since round 66 (`RECEIPT-ENV-CONFIG-SET`, rc 2 vs base rc 0).
2. `souji | round-66 |` scope of the repository-local keys (`core.fileMode`, `core.excludesFile`) and `GIT_COMMON_DIR` for the clean-tree check (round 67 routing depends on it).
3. `souji | round-66 |` wording of C1's GIT_CONFIG_GLOBAL route ("refuses" in the claim vs repoint in the candidate and the frozen E3 class).

## Pre-report gate

- `git -C souji-shokunin ls-remote origin refs/heads/master` → `b238ab1da21776c2c6e9286a8fd20e0343a14131` (final lane hash).
- Lane `jj-lane.sh state`: `local=b238ab1d… remote=b238ab1d… ahead=0 behind=0`.
- `grep -c '^## SHONEN'` on this report: 1.
