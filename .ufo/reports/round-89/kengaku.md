# kengaku — round 89 (hyaku run 15, attempt 2)

Lane `kengaku-shokunin`, branch `master`. Lane tip at report time: `c3f81f72495476db1f4e36706d2855347077fa36` (`git -C kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash). Measured revision for the counters: `00462b596f517cc70528f1773c20eac7dd530bfd` (plans bytes unchanged to `c3f81f72`: `git diff --stat 00462b59 c3f81f72 -- plans/` prints nothing). Attempt 2 is L1 `KengakuR89a2`. Attempt 1 (`KengakuR89`) dispatched wave `w1` and ended at 05:21 without a report (`.ufo/watchdog.log`: `lane-dead-no-report kengaku round=89`).

## Work performed

**Declared claims (frozen at `d1c4f1b0`, unchanged since):** two claims, both on the frozen predicates in `plans/round-89-claims.md`.
- **R89-C1 — coverage** (lowest non-retired axis, held at its L0 cap 7): a seventh located offline replay of the Terminal-Bench 2.0 member `polyglot-rust-c` (counter `plans/round89_c1_replay.py`, eight frozen cases, nine legs). Count move: ledger executed 32 → 33 of 88.
- **R89-C2 — calibration** (held at ceiling 10): the Q66 v2 counter `plans/round89_claim_figures.py` (pinned record table, KNOWN check on the claimed value, selftest in the predicate path, four control fixtures). Count move: 4 of 4 controls red, tip green.
- No exploratory claim. Frontier step: one sourced row, S278, cited by C1.

Work items, with evidence:
- **Protocol load:** `skill://shokunin`, canonical `PROTOCOL.md`, `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md` (kimi-shokunin checkout), lane `SCORECARD.md`, `SHONEN.md`, `corpus/lessons/round-89.md`.
- **Handover:** `.ufo/waves/round-89/w1.ready` (l1 `KengakuR89`) was dispatched at 05:10:10 (`w1.ready.dispatched`; `63d61d0f`). Attempt 2 told `KengakuR89` by message to forward `WAVE-DONE` and not integrate. It forwarded once, at `WAVE-DONE kengaku r89 w1: all 11 seats settled`, results `.ufo/waves/round-89/w1-results.json`. No second integration occurred.
- **Freeze check:** `git diff --stat d1c4f1b0 master -- plans/round-89-claims.md plans/round89-cases.json` prints nothing (claims and case table byte-identical to the freeze).
- **C1 re-measured at tip (attempt 2):** `python3 plans/round89_c1_replay.py --lane . --rev 00462b59… --work DIR` → `TARGET executed_rows=33 member=polyglot-rust-c located=1 executed=1 cases=8 legs=8 mismatches=0 defects=0`, `PREDICATE R89-C1 pass`, rc 0. Evidence: `.ufo/waves/round-89/attempt2/c1-tip-attempt2.txt`.
  - An earlier attempt-2 run in the same session failed at L6 (`DEFECT L6-reproduce probe re-run rc=2 produced no observation block`, rc 1) while `/proc/sys/user/max_user_namespaces` read `0` and `bwrap` returned ENOSPC. It is kept verbatim as `attempt2/c1-tip-attempt2-first-run-host-sysctl-0.txt`. The host later read `122865` and `bwrap` ran. This lane changed no host setting; the value's origin is outside this lane (Main's notice). Recorded as Mistake 5.
- **C2 re-measured at tip (attempt 2):** `python3 plans/round89_claim_figures.py --lane . --rev 00462b59… --work DIR` → `RECORDS claims=17 files=8 records=56 checked=56 matched=55 mismatches=1 prose=0`, `DEFECTS n=0`, `PREDICATE R89-C2 pass`, rc 0; `--controls` → `CONTROL doctored-claimed red`, `CONTROL deleted-figure red`, `CONTROL doctored-key red`, `CONTROL selftest-in-path red`, `CONTROL tip green`, `PREDICATE R89-C2-CONTROLS pass red=4 of 4 tip=green`, rc 0. Evidence: `attempt2/c2-tip-attempt2.txt`, `attempt2/c2-controls-attempt2.txt`.
- **Do-nothing controls (BASE):** C1 at `192e809d`: `TARGET executed_rows=32 … located=0 … defects=4`, `PREDICATE R89-C1 fail`, rc 1 (`.ufo/waves/round-89/L1/c1-base.txt`; reproduced by ExecCtrlC1 control 2). C2: the round-88 counter on the three attack fixtures measured `pass`, `pass`, `fail` (`w1/ExecCtrlC2/round88-baseline.txt`).
- **Wave w1 — one v1 wave, 11 seats, all settled** (`w1-results.json`; spec `w1-spec.json`; dispatch `w1-dispatch.json`):

| Seat | Role | Verdict (final output) |
|---|---|---|
| ExecCtrlC1 | executor | FINDINGS 2: host sysctl at run time (F1); the forged-receipt recipe did not exercise L3, the claim-file variant 4b does (F2). Controls 1–5b in `w1/ExecCtrlC1/controls.txt`. |
| ExecCtrlC2 | executor | C2 do-nothing measured; mispredict on the doctored-key fixture recorded (`round88-baseline.txt`). |
| ExecProbeR89 | executor | PASS: probe observation identical across three runs; containment and no-HOME/TMPDIR reads checked (`w1/ExecProbeR89/report.md`). |
| ReviewerR89a | reviewer | FINDINGS 1 (process disclosure: the case table's `predicted` column was read before the blind derivation; restaged; 8/8 vectors agree). |
| ReviewerR89b | reviewer | FINDINGS 1: F6 — a doctored after-figure (`ids=8` → `ids=9`, `plans/round-85-claims.md`) stays green; the counter pins before-figures only. Spec anchor anomaly (the item's "digit 4 in ids=8" does not exist). |
| CriticR89 | critic | FINDINGS 9 (3 MAJOR): F1 frozen C2 Move (d) "pinned to its blob sha at the freeze commit" is not implemented; F2 disclosure gap (the sysctl window was not in committed bytes; now corrected, Mistake 5); F3 control `selftest-removed-from-path` is implemented as `selftest-in-path`. Six MINOR wording/predicate mismatches (F4–F9). |
| MutTesterR89 | mutation-tester | FINDINGS 10: 13 mutants. C1 killed M6 on the tip; M1–M5, M7 survive the tip predicate (killed only by fixtures; M2/M5 have no real-harness fixture). C2 killed N2, N3, N5; N1 (label-only), N4 (print-only guard) and N6 (traceback, no verdict) survive. `w1/MutTesterR89/mutants.md`. |
| SentinelR89 | sentinel | FINDINGS 10 (3 High, 1 Medium, 6 Low): H1 regenerated record table passes after a deleted before-figure; H2 KNOWN/claimed edit with a regenerated table passes C2; H3 an echo probe with `TRUSTED_TOOL_SHA` rewritten in the same commit passes C1. All forged commits exist only in the sentinel's scratch clone. Lows L1–L6. |
| ScoutR89 | scout | Next-round candidate set: 24 unexecuted ledger members with captured grader bytes at the tip, sha-cross-checked (`w1/ScoutR89/next.md`). No claim. |
| ConnectorR89 | connector | PASS 0: sibling-overlap scan over 20 lanes; holds the TB2 grader-replay standard; no sibling owns an evidence-replay gate (`w1/ConnectorR89/overlap.md`). |
| ScribeR89 | scribe | S278 gate note: live HTTP 200, 1638 B, sha `baed5e4d…` matches the captured copy (`w1/ScribeR89/gate-note.md`). Knowledge draft not admitted this round. |

- **Seat counts:** 11 spawn seats. Roles: executor 3, reviewer 2, critic 1, mutation-tester 1, sentinel 1, scout 1, connector 1, scribe 1. Attack seats (reviewer, critic, mutation-tester, sentinel) 5 of 11 = 45 %. Connectors 1. The planner mapping is the L1 (validator rejects planner as a swarm role). **Residual call:** none. **Round total:** 11 seats. **Dead seats:** none in `w1`. The attempt-1 L1 `KengakuR89` is recorded dead (`lane-dead-no-report`, 05:21).
- **Answering models:** `w1-results.json` does not record the answering model per seat; none is claimed here.
- **Frontier and corpus:** S278 (see Sources & frontier); eleven mistakes in `corpus/lessons/round-89.md` (Mistakes 1–11; 5–11 are attempt 2) and round-90 routing in the same file.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists `.scratch/run15-state.json` (orchestrator-owned, not touched), `.ufo/l0-questions.md` (this report's L0 line) and nothing written by a kengaku seat. No misroot copy was needed.

## Landed changes

| Commit | Content | Log / evidence |
|---|---|---|
| `d1c4f1b0` | freeze: claims and case table (attempt 1) | `plans/round-89-claims.md` |
| `0e6bb05f` | instruments: probe, C1 counter, Q66 v2, pinned record table, probe receipt (attempt 1) | — |
| `000b7d1c` | C2 control fixes (mkdir, vacuity guard, deleted-figure marker); ledger `polyglot-rust-c` executed; S278 admitted; round-89 lesson (attempt 1) | `corpus/lessons/round-89.md` Mistakes 1–4 |
| `63d61d0f` | wave-1 spec, validated dispatch, ready handoff (attempt 1) | — |
| `a9b8a1a0` | S278 registry row closed so census is exit 0 (attempt 1) | `corpus/SOURCES.md` |
| `07191241` | SCORECARD and LOG round-89 entries; SKILL.md registry rows (attempt 1) | `LOG.md` line 3386; `SCORECARD.md` round-89 rows |
| `00462b59` | QUALITY Q67 (control batteries must be shown non-vacuous and able to fail) | `corpus/QUALITY.md` (appended) |
| `c3f81f72` | attempt-2 integration: lesson Mistakes 5–11 and round-90 routing; LOG attempt-2 entry; wave evidence `w1/` (11 seats), `w1-results.json`, `attempt2/` counter outputs; inherited round-88 `w1-results.json` (untracked leftover, committed under this round) | `LOG.md` line 3398; `corpus/lessons/round-89.md` |

L0 question appended (this report's commit): `kengaku | round-89 | Operator ruling needed on R89-C2 …` (`.ufo/l0-questions.md`).

## Before → after measurements

**R89-C1 (coverage).** Counting command: `python3 plans/round89_c1_replay.py --lane <lane> --rev <rev> --work <dir>`; measured at `192e809d` (BASE) and `00462b59` (tip, attempt 2).
- Before (BASE `192e809d`): `TARGET executed_rows=32 member=polyglot-rust-c located=0 executed=0 cases=0 legs=0 mismatches=0 defects=4`, `PREDICATE R89-C1 fail`, rc 1.
- After (tip `00462b59`): `TARGET executed_rows=33 member=polyglot-rust-c located=1 executed=1 cases=8 legs=8 mismatches=0 defects=0`, `PREDICATE R89-C1 pass`, rc 0.
- Ledger (`plans/grader-population-ledger.json`): executed 32 → 33 of 88; `shell-exec` 1 → 2 of 6; `stdout-inspection` 8 → 9 of 29; `subprocess-exec` 10 → 11 of 45.
- Controls on the frozen predicate (tip-based): ledger-only (receipt removed) → rc 1, `DEFECT L1-receipt`; forged-receipt, claim-file variant 4b (LANE_TIP not an ancestor) → rc 1, `DEFECT L3-tip`; forged-probe (echo) → rc 1, `DEFECT L9-tool`; positive → rc 0.
- Verdict: **verified on its frozen predicate.** Residuals: the pass depends on the host allowing user namespaces (Mistake 5); the counter's pins can be rewritten by one commit (Mistake 9, sentinel H3); leg-disabling mutants survive the tip predicate (MutTesterR89 M1–M5, M7).

**R89-C2 (calibration, ceiling 10).** Counting command: `python3 plans/round89_claim_figures.py --lane <lane> --rev <rev> --work <dir> --controls`.
- Before (round-88 counter on the round-89 attack fixtures, `ExecCtrlC2/round88-baseline.txt`): doctored-claimed `pass`, deleted-figure `pass`, doctored-key `fail`. Two of three attack fixtures undetected. Mispredict: the frozen "0 of 4 red" was wrong for the doctored-key fixture.
- After (tip `00462b59`): `RECORDS claims=17 files=8 records=56 checked=56 matched=55 mismatches=1`, `DEFECTS n=0`, `PREDICATE R89-C2 pass`, rc 0; controls `red=4 of 4 tip=green`, `PREDICATE R89-C2-CONTROLS pass`, rc 0.
- Axis score: held at ceiling 10 (count move, per the frozen claim).
- Verdict: **verified on its frozen predicate, with a frozen-text defect** (Mistake 10). Move element (d), "pinned to its blob sha at the freeze commit", is not implemented (CriticR89 F1); control `selftest-removed-from-path` is implemented as `selftest-in-path` (F3). The C2 after-figure is unchecked (ReviewerR89b F6); the record table and KNOWN set can be rewritten by one commit (Sentinel H1/H2). The operator ruling is requested (L0).

**Round admission.** Both claims verify on their frozen predicates; no axis is harmed (coverage held at 7, calibration at 10). I am not admitting the round on the claim text alone: C2's frozen Move element (d) overclaims, so admission is held on the operator ruling (L0 line). Ledger flip (`polyglot-rust-c` executed) is part of C1.

## Sources & frontier

- Counting command (round start, attempt 1, and round end): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → `kengaku ok`, exit 0 (warnings W04 for pre-existing duplicate URLs across scopes; warnings allowed).
- Manual census before (`git show 192e809d:corpus/SOURCES.md`): 269 rows; tier A 239, B 24, C 6; status mined 244, queued 8, rejected 17.
- Manual census after (`corpus/SOURCES.md` at `c3f81f72`): `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 270 rows; tier A 240, B 24, C 6; status mined 245, queued 8, rejected 17.
- Rows added by tier: A +1 (S278, `https://raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/polyglot-rust-c/tests/test_outputs.py`, scope "member replay only"; opened 2026-11-05, HTTP 200, 1638 B, sha256 `baed5e4d…92f9` equal to the round-52 capture; located quote `assert polyglot_files == ["main.rs"], (` at line 19; re-verified by ScribeR89).
- Rows touched old→new: none. Frontier advanced: S278 `mined` (cited by `corpus/lessons/round-89.md`, `corpus/evidence/round89/`, and the C1 claim).
- Sourced claim: R89-C1 rests on S278.
- Knowledge entries admitted: none this round (the ScribeR89 draft is not appended). Expansion trend credit: none.
- Assimilation: none (`merge/kengaku/` remains held by L0 `kengaku | round-54`; nothing appended). considerthese item 1 (`considerthese/2026-10-26.md`) mined in the lesson, not implemented.
- Mistake mined: the lesson's `## Mistakes` 1–11 (classes `vacuous`, `landing`, `figure-not-measured`, `environment`, `spec-error`, `process-contamination`, `self-pinned instrument`, `frozen-text`, plus the disclosure gap).

## Trend verdicts

- **expansion: unchanged.** No knowledge entry added (`git diff --stat 192e809d master -- corpus/knowledge` prints nothing); one member executed on the coverage surface (ledger 32 → 33), counted under coverage, not expansion.
- **quality: unchanged.** No depth, freshness or operability score moved. Q67 was added to `corpus/QUALITY.md` (appended bytes, `00462b59`), grounded in the controls; it is not a measured move.
- **discernment: improved.** Counter-side controls: round-88 counter 1 of 3 red on the attack fixtures → round-89 counter 4 of 4 red, tip green (`attempt2/c2-controls-attempt2.txt`). Caveats: the counters are not tamper-resistant (Sentinel H1–H3), and the after-figure is unchecked (F6); this is not a claim that the instrument is forgery-proof.

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md (lane author assessment; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:3398 (attempt-2 re-run of the replay and control battery at the tip; attempt-1 entry LOG.md:3386)
- [~] Instructions executable by an agent without oral context — corpus/lessons/round-8-aggregator-box3-coldrun.md:48
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md:151

## Stale-lane

Stale-lane: no other mission of this lane is open. Attempt 1 is closed by `lane-dead-no-report` (05:21); its wave `w1` settled (`WAVE-DONE`, results file present).

## Tool installs

None. No tool was installed, upgraded or changed on this host by this lane (ScoutR89 recorded `uv 0.13.0` and `bwrap 0.13.1` as already present). No pacman transaction.

## Open L0 questions

- `kengaku | round-89 | Operator ruling on R89-C2 (frozen text, element (d) unimplemented; control naming) and on the instrument pin forgeability (Sentinel H1–H3). Round admission held on this ruling.` (`.ufo/l0-questions.md`)

## Scratch and cleanup

Seat scratch trees were removed by their seats after copying transcripts into the wave dir. The L1 removes `/fast/scratch/hyaku/kengaku-r89/` after this report lands.
