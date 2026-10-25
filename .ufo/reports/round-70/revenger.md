# revenger — round 70 report (hyaku run 7, fresh-start round, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`, final lane hash **f645e1fb16cd9b22f732dbccb940744763b7c222** (`git ls-remote origin refs/heads/main` prints it; adjudicated tip `ca6a1ff04950bc4a9b5fa66dcf782fc7a43ed7e3`).

## Work performed

Declared claims (pre-registration `dbacce212d798d1ec5bb59e03ff91d577eed0283`, `reports/round-70/claims.md`; tighten-only amendment A1 `reports/round-70/claims-amendment-A1.md`, declared before any wave-2 seat scored):
- **C1 — coverage, knowledge-map ground K (lowest criterion, 5.7): C05 fifth pass → FALSIFIED, honest stop.**
- **C2 — calibration: lane self-assessment vs observed state, `SELF_MISMATCH` 9 → 0 (new tool `corpus/self_assessment_check.py`) → verified as declared.**
- **C3 — freshness: retained r68 entry re-derives against a digest-pinned historical script, `EMB_R68` problems 7 → 0 → verified as declared.**
Claim type: all measured; none exploratory; no capability row entered the table (instruments registered in `SKILL.md` §Gate registry).

- Fresh-start read: r67/r68/r69 closures and spot-checks (`corpus/lessons/round-6{7,8,9}-verifier-spotcheck.md`); r69 was `rejected-harmed` (freshness/operability). Inherited leftover V1 (`.ufo/waves/round-69/R69CounterReplay.md`) committed under the pre-registration commit; no earlier r70 attempt existed.
- Instruments: new frozen counter `reports/round-70/measure.py` (sha256 `488f95aa…c88c76`; exit 0/1/2, crash never exit 1, M50 repair), eight do-nothing/gaming controls (`reports/round-70/controls/A-H`), red-before `measure-before.log`.
- Build: v5 C05 candidate generated from command stdout (`.ufo/waves/round-70/build-entry.py`), `corpus/fixtures/apk-r65/entry_checks.py` (8 derivation flags), spec snapshots, `corpus/lint_entry.py`, gate pin rule + command confinement, README/SHONEN/SCORECARD repairs.
- Wave 1 (40 seats) pre-gated; its findings (11 prose defects, checker gaps, pin holes, controls I/J/K reaching frozen predicates) drove v5.1 and amendment A1 (`controls/I,J,K`, `measure-a1.py` sha256 `96feeaa0…2e87191`).
- Wave 2 (45 fresh seats) gated lane commit `17ee7f87`: 16 Q decisions, 3 FAIL (Q04, Q11b, Q13 — entry `:119`, `:152`, `:282`, `:310`), 13 PASS/n-a. Kill rule executed: README C05 unchanged, entry `admission-status: rejected`, every other byte kept.
- Round shape: **two v1 waves, 85 seats** (40 + 45), 0 dead seats, no residual call. W1 roles: reviewer 3, critic 9, executor 5, mutation-tester 5, scribe 4, scout 8, connector 3, simplifier 1, sentinel 1, revenger 1 (m_flash roles 52.5 %). W2: reviewer 11, critic 13, executor 10, mutation-tester 3, scout 4, revenger 1, sentinel 1, connector 2 (m_flash 55.6 %, attack share 64 %). §3 planner seat held by this L1; data walk by `R70W1ConnLedger`. Results: `.ufo/waves/round-70/w1-results.json`, `w2-results.json`.
- Assimilation: considerthese `2026-10-25.md` proposals 4 (Q-map completeness → `lint_entry.py` QMAP) and 2 (generate from stdout → `build-entry.py`) acted on; `2026-10-24.md` proposal 3 (hit-rate ledger) in the lesson (two seat derivations disagree on 2 of 18 rows, recorded). `merge/revenger/` theme (fixity/Unblob + SWGDE): nothing adopted (see Sources & frontier).
- Lane-owned stale-statement repairs found by dogfooding the checker: README Q-range and Known gaps, SHONEN box 1 (`[x]`→`[~]`, digest removed) and box 4, SCORECARD erratum (`e1d22caf`, V3, V4, phantom seat `W2ReviewSeparability`).
- Tool installs by this L1: none. (Seat `R70W1IndependentRead` installed `androguard` 4.1.4 via `uv tool` and used preinstalled `apktool` 3.0.3.) Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain -uall` shows no revenger r70 file at the fleet root (only the orchestrator's `.ufo/state/revenger.report-baseline`, not mine). Stale-lane: respawn-per-round driver; no other mission of this lane open.

## Landed changes (each tied to LOG.md "Round 70" and to a commit)

| change | commit |
|---|---|
| pre-registration: claims, frozen counter, controls, red-before, treated tools (checker, lint, gate pin rule, pinned r68 script), r69 leftover resolved | `dbacce2…` |
| v5 candidate + `entry_checks.py` + spec snapshots + generator | `aa1842f…` |
| wave-1 integration: v5.1, A1 + controls, hardened gate/checker/lint, README/SHONEN/SCORECARD repairs, S048/S049 | `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` |
| adjudication: entry rejected, README C05 row evidence, Q16, lesson `corpus/lessons/round-70.md`, SCORECARD "Round 70", LOG, SKILL rows, gate wiring leg + `wiring-red-before.log`, census, wave evidence | `ca6a1ff04950bc4a9b5fa66dcf782fc7a43ed7e3` |
| after receipt `reports/round-70/measure-after.log` | `f645e1fb16cd9b22f732dbccb940744763b7c222` |

## Before → after measurements

Counting command (every claim; absolute path, any cwd): `T=$(mktemp -d) && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <commit> corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C $T && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py $T` and the same with `measure-a1.py`. Before: `reports/round-70/measure-before.log` (base `3f5edbc206351232a3d2d801334dd930499ccaf5`) and `before-treated-tools-on-base.log`; after: `reports/round-70/measure-after.log` (tip `ca6a1ff`), exit 0.

| claim | before → after | verdict |
|---|---|---|
| C1 | `K_HELD_BACKED` 8/14 → 8/14; `C05_STATUS` uncovered → uncovered; `HOLDS_C1_V5` no → no | **falsified — honest stop** (Q04, Q11b, Q13 FAIL; kill rule executed) |
| C2 | `SELF_MISMATCH` 9 (SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0) → 0; `SELF_MUTANTS_KILLED` n/a → 6/6; `HOLDS_C2_V5` no → yes; `A1_C2` no → yes | **verified as declared**, limits named (SM classes are bounded; SM3/SM4 are 0 because overstatement was removed; an env-override hybrid survives both counters) |
| C3 | `EMB_R68` problems 7 → 0 (17 blocks); `EMB_R65` 1 → 1; `EMB_PIN_MUTANT_KILLED_ATTRIBUTED` n/a → 1/1; `HOLDS_C3_V1` no → yes; `A1_C3` no → yes | **verified as declared** |
| holds | `HOLD_REPLAY` 10/10, `GATE_SELFTEST` 0, `F_COVERAGE` 5/8, `FRESH_ROWS` 18/18 both ends; `HOLDS_OK_V7` yes | unchanged |

The round is not admitted (C1 falsified); no axis harmed. Open: operator rules.

## Sources & frontier

- SOURCES rows 47 → 49 — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Added: S048 (docs, tier A, supersedes S045's locator), S049 (docs, tier A, supersedes S043's repo path), both opened this round by this L1 (live fetch, digests in the lesson `## Gate`). Touched old→new: used-by of S032, S034, S038, S041, S047 gained the round-70 entry (logged in the lesson); S043/S045 unchanged (superseded, not rejected). Frontier rows advanced: none held (C05 still uncovered).
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`: start exit 0 (rows 47, four W04), end exit 0 (rows 49, five W04: +S048 duplicate url by design). `.ufo/waves/round-70/census-before.txt`, `census-after.txt`.
- Sourced claim: C1 rests on S038/S032/S034/S041/S047/S048/S049, re-opened this round (non-author scouts and this L1 re-fetched S038, S032/S034, S043, S045 live; all byte-identical to snapshots except two chrome lines).
- Mistakes mined (`corpus/lessons/round-70.md` `## Mistakes`): M51 reference-drift (captured by SM5), M52 vacuous frozen predicate (fixed by A1), M53 prose credit beyond printed output (new criterion Q16).
- Assimilation (item 10): id guard proven and run (registry 47 ids, staged 155, round-start collisions 1: S047; renumber map in lesson); quarantine slice 26 rows, S054/S099 hand-checked UNVERIFIED-REACHABLE, staged Unblob rows PRESENT. Decisions: REJECT Unblob draft entry (`R70W2AssimGateA`/`B`), REJECT package `swgde-custody-authority-and-normative-scope.md` as staged, ADMIT scope-only for the narrowed SWGDE digest-scope claims (no entry written). Zero rows/entries appended. considerthese present (latest `2026-10-25.md`).

## Trend verdicts

- **expansion: unchanged** — no admitted entry, K 8/14, C05 uncovered; two source rows added with a rejected-candidate consumer (no credit).
- **quality: improved** — evidence: C3 (`EMB_R68` 7 → 0, r69 freshness harm repaired, `measure-after.log`), checker/gate/lint hardened against 18+ attacker-found classes, three stale self-assessment statements corrected, Q16 added; no admitted entry fails its bar.
- **discernment: improved** — the lane's own wave found the C1 defects (Q04/Q11b/Q13) and executed the kill rule without repair; A1 closed three reachable controls before scoring; M51–M53 mined. Closure to confirm by spot-check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane attestation only (`revenger-r64.R64ReviewSkill`, a lane seat; r64 bytes via `git show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md`); `SHONEN.md:5-16`; box was `[x]`, honestly demoted this round (SM4); `R70W2ShonenReview` HONEST.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `reports/round-64/measure-after.log`, `corpus/live/runs/round-63/`; no producer rerun; `SHONEN.md:17-21`.
- [~] Instructions executable by an agent without oral context — `R64ExecSkillRun`; this round `R70W2HoldSweep` re-ran all self-tests green; no independent outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `R70W2SentinelFinal` CONTAINED, `PROVINCE.md` unchanged, ADJ-06 reported-not-absorbed; one false README-parenthetical claim in the box corrected; no non-author verifier named.

Open L0 questions: none new; round-68 C7 and round-69 instrument-repair questions (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:156,160`) remain unanswered and were not pre-empted.
