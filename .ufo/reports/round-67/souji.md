# souji — round 67 (attempt 1)

Lane: `souji-shokunin` (branch `master`). Base `3639087917eaeb28719d7603110a6ec22782100e`. Lane HEAD at report time `485b3b00679d086ba846939349d451ad15d69824` (pushed; `ls-remote origin refs/heads/master` matches). Freeze `4c61efcbe8c4e7586590c76965e5b1b29a1fa9a7` (`census/round-67/preregistration-attempt4.txt`). Wave `w1` (one v1 wave, 10 seats; WAVE-DONE received, results `census/round-67/wave/w1-results.json`). Lesson `corpus/lessons/round-67.md`.

## Work performed

Declared claims (two, distinct axes, both frozen at `4c61efcb`):

- **C1 — operability** (receipt-binding surface; Q59 neutral). The receipt writer value-checks a caller-injected `GIT_COMMON_DIR` against the repository's own common directory: a mismatching or empty value refuses with `RECEIPT-ENV-COMMONDIR-MISMATCH`, an equal value is accepted (W3). **Verdict: verified on its frozen predicate; a named fail-closed trade (relative value, writer cwd ≠ root) is open for the operator; two clauses of the claim text (every git call scrubs; empty value refuses) are not measured by the frozen matrix and are not counted as passes.**
- **C2 — calibration** (lowest owned axis, score 7; bookkeeping file). The statement counter and population, with the redirect claim checked through its claim token, flag the round-66 `s5` class overreach at the pinned historical state and kill the reverted-rule and enum-weakened counter mutants. **Verdict: verified on its frozen predicate; a detection of a historical overreach, not a 0–10 movement (score unchanged).**
- Frontier step (§2b): one sourced claim (C1 rests on S300, opened this round); one knowledge entry (`corpus/knowledge/common-dir-route-receipt-writer.md`); mined mistakes M1–M11 (`corpus/lessons/round-67.md` `## Mistakes`); census recorded before and after.

Work items (evidence in brackets):

1. Protocol load: `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md`, protocol files, `skill://shokunin`, `skill://swarm`, `skill://godspeed`; lane `SCORECARD.md` planned r67 row, `corpus/QUALITY.md`, `corpus/README.md` Frontier, lessons r66 and the r66 verifier spot-check [`LOG.md` r66 entry; `corpus/lessons/round-66-verifier-spotcheck.md`].
2. Routed round-66 defects handled (lesson `## Routed to round 68`): new frozen counter fixing M4/M6 [`census/round-67/c1-counter.py` docstring, `census/round-67/c2-counter.py`]; route sweep for `GIT_COMMON_DIR` as a frozen row (W1–W3) with repository-local `core.fileMode`, `GIT_NAMESPACE`, `GIT_CEILING_DIRECTORIES` as probes or proposals; scope-falsifiable class population row and the s4 note (M5/M7) [`census/round-67/c2-statements.tsv`]; kill-power fixtures K3/K4/K6/K7 proposed as PK3, PK4, PK6, PK7, decision `fixture-proposed` [`census/round-67/wave/w1/S67MutKill/k67-decision.md`]; receipt grammar fixed [counter `--receipt` emits the measured `rev=`]; Q129 superseded by Q130 [`corpus/QUALITY.md` line 346].
3. Instruments built and pre-freeze checked: C1 counter (31 rows: the 28 r66 rows unchanged plus W1–W3) and matrix `census/round-67/c1-matrix.tsv`; C2 counter, population and two mutant recipes `census/round-67/c2-mutate.py`; both counters' selftests and mutant kills checked before freeze [instruments commit `05eb2cee`; `census/round-67/probes/l1-w2-repro.md`, P4 records the vacuous M10 draft caught by the reverted-rule mutant].
4. Controls: C1 do-nothing (base bytes in the new slot) `census/round-67/controls/c1-do-nothing.txt` (commit `d544e75a`); C2 do-nothing at the pinned state, the round-66 counter `census/round-67/controls/c2-do-nothing-r66.txt`, plus the r67 counter at the round-66 base `c2-do-nothing.txt` (commit `832a4d43`).
5. Freeze chronology: attempt 1 `832a4d43` (superseded, M6), attempt 2 `b3aa70fe` and attempt 3 `d874bf0d` (checker-rejected population digest, superseded, M1), attempt 4 `4c61efcb` = THE FREEZE. `tools/souji-freeze-check.py --substance --chronology` → `SUMMARY claims=2 findings=0`, rc 0; `tools/souji-axis-check.py` → `claims=2 flags=0`, rc 0 [re-run at HEAD `485b3b00`].
6. Wave `w1` (one v1 wave, 10 seats, band 8–16, validated under `scripts/hyaku/ufo-wave-policy.json`): `S67ExecWriter` (executor) built the candidate, selftest 37/37, frozen trial met [`census/round-67/wave/w1/S67ExecWriter/report.md`]; `S67MutKill` (mutation-tester) killed the frozen matrix's survivors by proposed fixtures [`S67MutKill/k67-decision.md`]; `S67ReviewerDesign` (reviewer) no HIGH [`S67ReviewerDesign/report.md`]; `S67ReviewerC2` (reviewer) confirmed the M4 kill, the M5 enumeration defect, and a base-state control issue [`census/round-67/wave/w1/S67ReviewerC2.md`]; `S67CriticClaims` (critic) found the unmeasured scrub and empty-value clauses, the relative-value base error, the overstated enumeration, and the C2 do-nothing revision issue [`S67CriticClaims/report.md`]; `S67SentinelScope` (sentinel) found no HIGH and two MEDIUM counter-hermeticity defects (ambient `GIT_COMMON_DIR`, replace refs) [`S67SentinelScope/scope.md`]; `S67ScoutSources` (scout) captured git `setup.c`/`environment.c`/`worktree.c`/`git.adoc` at tag v2.56.0 and the quotes [`S67ScoutSources/quotes.tsv`]; `S67ScribeEntry` (scribe) verified the freeze digests and found the registry K1 defect [`S67ScribeEntry.md`]; `S67ConnectorOverlap` (connector) found no sibling overlap and no assimilation theme [`S67ConnectorOverlap/shokuknow-scan.md`]; `S67RevengerProbe` (revenger) measured host git's env behaviour, P1–P5 [`S67RevengerProbe/probes.tsv`].
7. Candidate landed as `tools/souji-receipt-write.py` at `f70da577eb1e1624cc63ab8fd0468565927d9b6a` (sha256 `b811ee2a7a67d8d3ea6d00fb3a44780ccb807113b9eeaf28f09e01448715a725`, verified against `SHA256SUMS`). L1 selftest on landed bytes: `SELFTEST cases=37 pass=37 fail=0`, EXIT 0. Frozen C1 measured at `f70da577` [`census/round-67/records/c1-after.txt`].
8. Frozen C2 measured at the pinned state `c13fbb4e` [`census/round-67/records/c2-after.txt`], kill receipts [`records/c2-mutant-reverted-selftest.txt`, `records/c2-mutant-enumweak.txt`, `records/c2-selftest.txt`].
9. Relative-value and scrub probes, committed as evidence (P-rel1: cwd ≠ root trade; P-rel2: the critic's W4 shape) [`census/round-67/probes/relative-value-probes.txt`]: base writes a receipt over a dirty poisoned tree (rc 0), the landed candidate refuses (rc 2, dirty class, no receipt). The protection there is the scrub, which the frozen matrix does not measure.
10. Registry and corpus: S300 row appended (tier A, mined; `corpus/SOURCES.md` line 259); S298 `used-by` extended by one path to satisfy the K1 bidirectional rule (scribe finding, lesson M11); knowledge entry, lesson, README frontier, SKILL `## Round 67` section and gate rows, SCORECARD round-67 table and planned bullets, LOG `## Round 67` entry.
11. Fleet: L0 question on the relative-value trade appended and committed (`ca47fecf`, fleet repo) [`.ufo/l0-questions.md`, `souji | round-67` line].
12. Defects I found in my own work and corrected (all in the lesson, none hidden): an empty `PUT` that emptied the lesson file (recovered by a full rewrite); a hand-typed digest transcription (M1); a vacuous M10 selftest draft (M2); a false named limit about repository-local `core.excludesFile` (M3, probe PK3 re-checked by this lane); the "enumeration-bound" overstatement (M7); a claim text that names the scrub clause the frozen matrix does not measure (M9; the claim was written before the critic measured the gap, and it is now named as unmeasured rather than counted as a pass).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `tools/souji-receipt-write.py`: value-checked caller `GIT_COMMON_DIR`, scrubbed on every git call; selftest 37/37 | `LOG.md` `## Round 67`, "Landed" bullet | `f70da577eb1e1624cc63ab8fd0468565927d9b6a` |
| frozen instruments: C1 counter, 31-row matrix, C2 counter, population, mutant recipes, L1 probe P4 | `LOG.md` "Claims"/"Freeze chronology" | `05eb2cee2794e42559c5ba15c3ebfdf7caecfee5` |
| do-nothing controls (C1, C2 r66 and r67-at-base) | "Controls" | `d544e75a…`, `832a4d43…` |
| preregistration attempts 1–4 (attempts 1–3 superseded, kept) | "Freeze chronology" | `832a4d43…`, `b3aa70fe…`, `d874bf0d…`, freeze `4c61efcbe8c4e7586590c76965e5b1b29a1fa9a7` |
| measured records: C1 after, C2 after, selftest, mutant kill receipts | "Measured" | `2771b02ee1cb8bd40ef458a29ac7a0ed6574f7dd` |
| knowledge entry, S300 row, lesson, README frontier, SKILL r67 section and gate rows, Q130, SCORECARD round-67 table, LOG entry | "Landed" | `e41f022f0dd018390fa68c7edab1dff734fcfc4f` |
| committed relative-value probe record (P-rel1, P-rel2); lesson M4/M9 evidence re-pointed | "Named limits", M9 | `36200ad87b169a7b17f244f3d67d8bb573426f07` |
| wave evidence mirror (`.ufo/waves/` is gitignored; mirror under `census/round-67/wave/`) and references re-pointed | "Landed" | `11a96e07d40c0d34a76f1637a6a288cde1380953` |
| close-out: S298 `used-by` (K1), lesson M1/M11 and reviewer limits, LOG correction, late seat outputs mirrored | "Corrections found at wave close" | `485b3b00679d086ba846939349d451ad15d69824` |
| fleet L0 question (relative-value trade) | "Named trade" | fleet `ca47fecf14d0353b50a918bca67842e5c9356dd0` |

## Before → after measurements

**C1 (operability; receipt-binding).** Counting command (re-runnable; `env -u` removes ambient repository-redirect variables):

    env -u GIT_COMMON_DIR -u GIT_NO_REPLACE_OBJECTS python3 -B census/round-67/c1-counter.py --root . --matrix census/round-67/c1-matrix.tsv --base-rev 3639087917eaeb28719d7603110a6ec22782100e --rev f70da577eb1e1624cc63ab8fd0468565927d9b6a --tool tools/souji-receipt-write.py --work DIR

- Before (base bytes in the new slot, `census/round-67/controls/c1-do-nothing.txt`): `SUMMARY matrix=31 base_forgeries=2 base_honest=6 new_forgeries=2 new_honest=6 class_mismatches=2 regress=PASS`, `EXIT=1`. W1 and W2 accept on base.
- After (`census/round-67/records/c1-after.txt`, rev `f70da577`): `SUMMARY matrix=31 base_forgeries=2 base_honest=6 new_forgeries=0 new_honest=6 class_mismatches=0 regress=PASS`, `EXIT=0`. W1 and W2 refuse `RECEIPT-ENV-COMMONDIR-MISMATCH`; W3 accepts.
- Frozen counter `instrument_sha256=69f11706ce98fe0c635bdbec7f24d8be5d1a36a54c4c5cfa1d019c362aa136b2`; matrix `5d26b341…`.
- Score: operability 8, unchanged (no reproducible 0–10 mapping for a receipt-binding row).
- Named trade (not counted as an improvement): a relative `GIT_COMMON_DIR` with the writer cwd ≠ root refuses where base accepted (`P-rel1`: base rc 0, candidate rc 2; fail-closed, no accepted redirect). Operator ruling requested (L0).
- Not measured by the frozen matrix (not counted): every git call scrubs; empty value refuses. Probe P-rel2 shows the scrub is load-bearing on the relative shape.

**C2 (calibration; bookkeeping file).** Counting command:

    env -u GIT_NO_REPLACE_OBJECTS -u GIT_COMMON_DIR python3 -B census/round-67/c2-counter.py --root . --tsv census/round-67/c2-statements.tsv --tsv-rev 05eb2cee2794e42559c5ba15c3ebfdf7caecfee5 --rev c13fbb4e1b563a78278ddc14316c20252e9a6d8d

- Before (round-66 counter, same state, `census/round-67/controls/c2-do-nothing-r66.txt`): `SUMMARY rows=5 findings=0 verdict=PASS`, `EXIT=0`.
- After (`census/round-67/records/c2-after.txt`): `FINDING SCOPE-OVERREACH s5: … claim redirects_closed needs writer markers cdred; writer blob lacks them`, `SUMMARY rows=5 findings=1 verdict=FAIL`, `EXIT=1`.
- Kill power, reverted-rule mutant (`census/round-67/c2-mutate.py --mutant reverted-rule`; `records/c2-mutant-reverted-selftest.txt`): `SELFTEST-CASE m10-s5-assertion-line-not-live: findings=0 want=1 MISMATCH`, `SELFTEST pass cases=17 fail=1`, `EXIT=1`. The declared counter's own selftest: `SELFTEST pass cases=17 fail=0`, `EXIT=0` (`records/c2-selftest.txt`).
- Kill power, enum-weakened mutant (`--mutant enum-weakened`; `records/c2-mutant-enumweak.txt`): `SUMMARY rows=5 findings=0 verdict=PASS`, `EXIT=0` at the pinned state.
- Commit measured against: `c13fbb4e1b563a78278ddc14316c20252e9a6d8d` (pinned historical; the instruments are `05eb2cee`).
- Score: calibration 7, unchanged.

## Sources & frontier

- **SOURCES.md, before → after.** Counting command (round start and round end, both recorded): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`. Round start: exit 0, output `souji ok …/corpus/SOURCES.md`; `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 222. Round end: exit 0, output `souji ok …/corpus/SOURCES.md`; the count → 223; malformed-row `awk` count 0. The `W04` duplicate-URL warnings are pre-existing and status-neutral.
- **Rows added by tier.** One row, S300, tier A (code, scope common-dir resolution; `mined`). S298 and S299 are unchanged except for one `used-by` path (below).
- **Rows touched, old→new.** S298 `used-by` (index 11 only): `corpus/knowledge/caller-env-routes-receipt-writer.md` → `corpus/knowledge/caller-env-routes-receipt-writer.md, corpus/knowledge/common-dir-route-receipt-writer.md`. Reason: the knowledge entry cites S298 in its `source:` line, and the K1 bidirectional rule requires the `used-by` side (found by the scribe seat; lesson M11). Status, recheck and every other cell unchanged (checked by comparing cells of the old and new line).
- **Frontier rows advanced.** The F4-adjacent common-dir route entered as frontier (not core): `corpus/README.md` `### Frontier (r67 GIT_COMMON_DIR route)`, backed by the knowledge entry.
- **Sourced claim (§2b item 4).** C1's rule rests on S300 through the knowledge entry it lands: the `setup.c` quote `const char *git_env_common_dir = getenv(GIT_COMMON_DIR_ENVIRONMENT); if (git_env_common_dir) { strbuf_addstr(sb, git_env_common_dir); return 1; }` (13 words) and the git(1) contract quote (22 words), whitespace-normalized against the captures.
- **Gate.** URL, access date (2026-11-05), capture hashes and located quotes are in `corpus/lessons/round-67.md` `## Gate`.
- **Assimilation: none.** `considerthese/` absent (`test -d`). The shokuknow souji package holds no matching theme (scribe and connector: `census/round-67/wave/w1/S67ConnectorOverlap/shokuknow-scan.md`); its id range collides with this registry and nothing was appended.
- **Coverage agreement.** `tools/souji-coverage-agreement.py` at the tip: grounded 27, mapped 27, dangling 0, mismatches 0 (scribe seat).

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry (`corpus/knowledge/common-dir-route-receipt-writer.md`) on the `GIT_COMMON_DIR` route, which the coverage map did not hold (round-66 W2 named it open), its `source:` citing mined rows S300 and S298. Net new frontier ground, one row added. Evidence: `corpus/knowledge/common-dir-route-receipt-writer.md`, the S300 row, `corpus/README.md` r67 frontier.
- **quality: improved, with a named trade.** The round-66 entry's false named limit (repository-local `core.excludesFile` stays open) is corrected by probe PK3 (`corpus/lessons/round-67.md` M3); the overstated enumeration wording is corrected (M7; Q130); the scrub and empty-value clauses are named as unmeasured (M9). The trade (relative value, cwd ≠ root, fail-closed) is reported and routed to the operator; under AXES a trade is not an improvement, so the admission waits on that ruling.
- **discernment: improved.** The non-author seats (critic, reviewer C2, sentinel, scribe) disagreed with four L1 statements; each disagreement became a lesson row and a grounded criterion or a named limit (M4, M7, M9, M11; QUALITY Q130). The admits and rejects of this round's gate decisions still need a non-author spot-check at closure; this report does not claim it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md `## Round 67` section and gate rows (commit `e41f022f0dd018390fa68c7edab1dff734fcfc4f`); `corpus/SOURCES.md` S300 row.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 67` (C1 candidate landed and measured, C2 measured at the pinned state; commit `485b3b00679d086ba846939349d451ad15d69824`).
- [~] Instructions executable by an agent without oral context — `census/round-67/c1-counter.py`, `census/round-67/c2-counter.py` with their selftests and records under `census/round-67/records/`; SKILL.md `## Round 67` gate rows.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round; `corpus/lessons/round-67.md` `## Named limits` (considerthese absent; shokuknow scan none matches).

Note: the SHONEN marks stay `[~]`. No `[x]` was written: no non-author verifier has checked these boxes on this round's evidence.

## Stale-lane line

Stale-lane: no. The respawn-per-round driver; no other mission of this lane is open.

## Tools

None installed or upgraded this round (no pacman transaction, no sysctl or sudo change by this lane; host git 2.56.0 used as found; `pacman` remains paused host-wide).

## Round shape, wave, seats

- Shape: one v1 wave, 10 seats, band 8–16 under `scripts/hyaku/ufo-wave-policy.json`. No residual call. Round total: 10 seats.
- Attack share: 5 of 10 (reviewer ×2, critic, sentinel, mutation-tester) ≥25%. Connector seats: 1 (≤2). Planner: held by the L1 (the validator refuses a planner role).
- Role mix: executor 1, mutation-tester 1, reviewer 2, critic 1, sentinel 1, scout 1, scribe 1, connector 1, revenger 1.
- Conformance defect (disclosed): the protocol's minimum split names three executors; this wave had one executor, and the claims did not need more builders. Recorded for the route-map owner.
- Dead seats: none. All 10 seats returned final output (`census/round-67/wave/w1-results.json`). Two seats (`S67ReviewerC2`, `S67ScribeEntry`) reported after the L1 had begun the paperwork; their output is integrated in the lesson.
- Routing: `task.agentModelOverrides` is operator-owned; no seat was given a model argument by the L1.

## Open L0 questions

- `souji | round-67 |` relative `GIT_COMMON_DIR` trade (fail-closed refusal where round 66 accepted; choose (a) keep fail-closed, (b) resolve root-relative, or (c) a frozen row next counter). Lane routed around it; no answer assumed.
- Round-66 L0 360 (honest-run refusal under `git -c`) and 362 (wording of `GIT_CONFIG_GLOBAL`) still open; not changed here.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` before filing: `M .scratch/run15-state.json` (orchestrator-owned; not touched), `?? .ufo/closure-kaidoku-r92.json` (another lane's closure file; not touched), and `M .ufo/l0-questions.md` (this lane's L0 line, committed as `ca47fecf`). No seat wrote into the fleet root; nothing moved.

## Pre-report gate

`git -C souji-shokunin ls-remote origin refs/heads/master` → `485b3b00679d086ba846939349d451ad15d69824 refs/heads/master`. The lane's final hash matches. `census/round-67/` evidence is committed; `census/round-67/wave/` mirrors the wave because `.ufo/waves/` is gitignored.

## Scratch

`/fast/scratch/hyaku/souji-r67/` removed after landing; every receipt and probe the report cites lives in the lane under `census/round-67/`.

## Named limits and remaining debt

Full list in `corpus/lessons/round-67.md` `## Named limits`. The main ones: the relative-value trade (operator); the scrub and empty-value clauses unmeasured by the frozen matrix; the C2 base-state target shape and the do-nothing control at `045e1034` (the no-work arm is the round-66 counter at the pinned state); `REDIRECT_ENUM` documentation-only; the M4 revert family; the counter's ambient-environment hermeticity (sentinel M1/M2); `GIT_NAMESPACE` and `GIT_CEILING_DIRECTORIES` unrefused; submodule contexts unmeasured.
