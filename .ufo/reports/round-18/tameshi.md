# tameshi — round 18 report (hyaku phase 2, attempt 1)

Lane `tameshi-shokunin`, branch `master`. Dispatch tip `183f87b899e6cae46be98d251cbc87fb5118f6ca`; final pushed lane tip **`4b7c6823a462f5ea2eafcb262275300a545f3ed7`**. Helper state: local=remote, ahead=0 behind=0, detached HEAD, tracked=0 untracked=0. No promotion or independent admission is claimed.

## Work performed

Declared claims (2):
- **C1 — depth (lowest owned numeric axis), 7 → 8:** an eighth recorded mutation case, kumitate `scripts/sources-check.mjs` at `0acb7752d19058b953ebbeba253b1e35f6548de5`, leg `js-sources-check`. Verdict: **verified at its bounded counting rule**, pending outside closure.
- **C2 — operability, unscored:** close the eleven named round-17 routed defects with failure-backed evidence: seven surviving guard removals, evidence-disposition G2/G3 under jj, registry non-finite timeouts and session/group escape, bash-witness Git-environment leakage. Verdict: **verified for the eleven probes**, not comprehensive hardening.

Calibration 8 is a no-harm monitor, not a third claim. No stagnation waiver or new capability was needed.

Work and evidence (lane-relative paths below):
- C1 spec and predictions landed **before** any registered mutant run (`93d22aa21a144a0e2833b1be74718d15060f002b`, 19:40:21Z; sweep 19:41:29Z). Sweep: **5/10 killed, 5 survived, 0 inconclusive, 10/10 predictions held**. Eight pristine controls matched byte-for-byte. Evidence: `.ufo/evidence/round-18/sources-check/`; `corpus/knowledge/mutation-case-kumitate-sources-check.md` and appended ER8 corrections.
- Case-8 regression embedding includes the exact registered spec, recorded verdict table, hermetic suite string and eight-leg selftest invariants. Actual final execution: `final/regression.stdout` → **cases=8 passed=8**, zero flips. Five killed-mutant attributions were retained; four survivors differ off-suite and S_KIND differs only in help output. See `sources-check/attribution/`, `survivor-probes/`, w2 `KilledAttribution.md`, `KumitateRouting.md`. Kumitate was never edited or pushed.
- `tools/evidence-disposition.py`: tag-object and symlink-mode cases; a shared provenance anchor uses a bound lane's branch tip, refuses unbound detached jj, and permits a contained detached non-jj historical checkout. Selftest **63/63**. Historical manifests/receipts remain unchanged. Evidence: w1 `X06DispositionGuards.md`, w2 `MutateDisposition18.md`.
- `tools/registry-check.py`: detached-clone and short-revision tests, finite timeout validation, descendant cleanup across setsid/setpgid, bounded pipe draining and normal-exit daemon cleanup. Wave 2 found finite enormous timeouts still crashed; final timeout range is **(0, 86400]**, selftest **48 cases**. Scratch-creation failure now maps to exit 2. Evidence: w1 `X05RegistryCheck.md`, w2 `ReviewSkillDiff.md`, `CR47.md`, `final/registry-selftest.stdout`.
- `tools/bash-witness-study.py`: prefix-filter inherited GIT_* on both subprocess paths; private fixture root, config isolation and hooks-off fixture writes. Selftest **43/43**. New round-18 v2 manifests waive its original pinned bytes at `4acc607`; round-17 rows remain visible as superseded, not relabelled. Final disposition exits **0 clean / 1 producer_before failed**. Evidence: w1 `X07BashWitnessScrub.md`, w2 `ReviewMigration.md`, `final/disposition.stdout`, `before.stdout`.
- Promoted the collector to `tools/trace-inputs.py`; three exact previously surviving removals now each fail one behavioral case. Selftest **30/30**. Frozen round-17 collector bytes remain unchanged; its registry row is explicitly superseded. Round-18 measurement/assembler selftests **98/98**, **80/80**. Evidence: w1 `X04TraceInputs.md`, `X08ColdreadKit.md`, `final/`.
- R17-KNOW-EXIT, CMD-BIND, CITATIONS: entry-local append-only errata, named G5 breadth/hole7/89-vs94 corrections, five ER-jj2 notes, proper superseding source rows, canonical SHONEN. Retained claim: **input-keyed evidence, not declared/required-command coverage**. QUALITY29–36 have appended wave-2 corrections rather than silently rewritten rules. Evidence: `corpus/lessons/round-18.md`, `corpus/QUALITY.md`, w2 `ReviewAppendOnly.md`, `ReviewQuality18.md`.
- Many corpus appends after wave 2 invalidated reads. Existing reviewer identities were resumed; after provider cancellations, the L1 completed **17 final sections** with actual isolated executions and traced source/receipt audits (`w3/L1Residual.md`, `coldread/traces/L1/`). This is **not a wholly blind or independent cold-read**. Strict committed evidence nonetheless measures **60/60, restraint8**, no overrides.
- Planner seat was held by the L1; bounded planning/recon rode scouts, connectors and revengers. The wave validator does not accept a planner role.

## Landed changes

Every change is tied to **LOG.md, “Round 18 — eighth recorded case, routed-defect closure”**, beginning at line1085. Citable helper `landed` hashes:

| Landed revision | Change |
|---|---|
| `93d22aa21a144a0e2833b1be74718d15060f002b` | C1 pre-registration and census start |
| `aee4f3658f977b2f02a55403ef8b285daad7b23a` | C2 ruler and open=11 base receipt, before fixes |
| `58e5d53d6a638fb72042d1f6607b24018aa299a8` | build, entries, errata, sources, wave1 |
| `e08271ae789c562cb466f986d6202b33d7276a2a` | registry migration; **not** the earlier build commit's failing registry |
| `01d586ddbc5fcd78659557c4e93a6ee8517b87d1` | ruler v2, both base/after receipts; v1 error retained |
| `9ee1c8046295baf6c133c8d43b8315d562498aea` | wave2 fixes/reports/traces, timeout cap, eighth ledger row |
| `4acdeac9e482b4379d9c99290feb1d9546a67eb2` | lesson and re-read base |
| `921ef8077440f90d092aab4b9fdc750a45de1224` | retained re-reads and final dating/interval fixes |
| `5923d89ac491ec3d296905561a8ab0faf3fda65a` | missing S076 lesson citation, correction-row Gate quotes, receipt D/N rule |
| `a9c94c5c3a3ae857d7ee25e54fe4cf0f53fbbaa4` | final registry receipts, including failed stale-scratch-ref run |
| `a134a09d15c23b2c2f0373482bb36c292c175ea5` | assembled ledger; strict intermediate **59/60** retained |
| `a85f7107c4167cd9968248722256fcaf617fc30c` | final T2 input refresh; strict **60/60** |
| `4b7c6823a462f5ea2eafcb262275300a545f3ed7` | SCORECARD, LOG, census, final receipts |

## Before → after measurements

1. **C1:** SCORECARD command D (`:73`, read pinned runner blob), or `python3 .ufo/evidence/round-18/measure.py --rev REV`:
   - `183f87b…`: `recorded_cases=7 depth_score=7` (w1 `S05CommandDBaseline.md`, w2 `RerunC1.md`).
   - `a85f710…`, re-counted at final `4b7c682…`: **8 / depth8**, header/calls/tuples **8/8/8**. Final isolated regression exits0, **8/8 passed**. Header count alone is not enough; the guardrail is mandatory.
2. **C2:** `python3 .ufo/evidence/round-18/defect-probes.py --rev REV` using the same v2 ruler:
   - base `183f87b…`: **open11 closed0 total11**, exit0 (`c2-probes-v2-183f87b.txt`).
   - `e08271a…`, independently re-executed at `01d586d…` and final tool revision `921ef807…`: **open0 closed11 total11**, exit0 (`final/probes.stdout`). P01–P07 each have pristine0/mutant1.
   - v1→v2 changed only jj availability on PATH and the fixture's `lane.branch` binding. Both sides were re-run; wave2 critics accepted equal application. The v1 tip's three errors are retained, not scored as closed.
3. **No-harm monitors:** final branch-aligned scratch run `python3 tools/registry-check.py --rev 5923d89… --json` → **31/31 held, four superseded**, exit0 (`final/registry-branch-aligned.stdout`). Earlier **32/32, three superseded** predates supersession of the old collector row. Strict `measure.py --rev a85f710… --explain` → **60/60, box3 true, restraint8, overrides_used=false**, exit0 (`final/measure-final-60.json`); the same no-override count at final `4b7c682…` returned **60/60,8**, exit0.

Claims are separable at their measurement boundaries: the runner-only C1 survives removing C2 files; defect-probe inputs do not depend on case8. W2 `CriticSeparability.md` tested synthetic cuts. They share a build commit; the registry no-harm monitor intentionally exercises both, so they are not commit-level independent.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
- Start: **exit0**, W04 for S047/S048 only (`.ufo/evidence/round-18/census-start.txt`). Rows62, A54 B6 C2, mined35 queued24 rejected3.
- End: **exit0**; same two W04 plus four explicit superseding-row duplicate-URL warnings S075–S078 (`census-end.txt`). Rows**76**, A**67** B**7** C2, mined**48** queued**23** rejected**5**, malformed0. Counting rule is the frozen pipe-table census; w2 `CensusAndState.md` independently verifies the intermediate72-row state; final measurement JSON contains the final histograms.
- Added14 rows: **13 tierA, one tierB**. S065–S074: JSON, RFC8259, prctl rejected, subreaper, setsid, ProGit(B), working-copy rejected, open, pycache, symbolic-ref. S075–S078 supersede S060/S061/S068 anchors and S072's overbroad teaches. All URLs/access dates/located ≤25-word quotes are in lesson Gate and its addendum.
- S008 `queued→mined`, used-by `—→case8 entry`; S001/S052/S056/S057 each gained that entry in used-by. Changes logged old→new in the lesson. Original row cells otherwise preserved; corrections use new superseding rows. Footer replacement was disclosed, then the old pointer restored and new pointers appended.
- Sourced C1 rests on opened S001/S008; C2 on S065–S074 and corrections. Reopening seats verified quotes and identified locator/scope defects, retained in their reports.
- No F1–F10 frontier ground moved to Core. F3 has eight matching controls for **one case**, not all gates. Mistakes and demonstrated falsifiers: lesson `## Mistakes`, wave2 amendment and final census-citation repair.

## Trend verdicts

- **Expansion: improved (lane assessment).** Eighth case plus two source-headed notes and S008 mined; no broader frontier claim.
- **Quality: improved, bounded.** Registered outcomes preserved, eleven exact routed probes closed, actual eighth-case replay and survivor witnesses retained. This is not a clean-bill-of-health judgment: 18 new mutation survivors, probe-breadth gaps and process ownership limitations remain named.
- **Discernment: improved.** Wrong exit claims, overbroad command-binding language, missing ledger row, bad correction mechanics and failed intermediate measurements were surfaced and repaired or explicitly routed. Calibration score remains8, no promotion.

## SHONEN

- [~] Box1 — real tables/patterns/checklists/sources: `reports/round-1-calibration.md#box-1`; lane assertion only.
- [~] Box2 — end-to-end task logged: `reports/round-1-calibration.md#box-2`; case8 adds another demonstrated task.
- [~] Box3 — `.ufo/evidence/round-18/coldread/ledger.json`, strict60/60 at `a85f710…` and final tip; **17 sections L1-completed**, not independent/blind promotion evidence.
- [~] Box4 — `reports/round-1-calibration.md#box-4`; read-only sibling scope. No named non-author promotion verifier, no `[x]`.

## Waves, cancellations, conformance and incidents

- Validated **w1:73** (20 scout,18 scribe,10 executor,10 reviewer,5 critic,5 connector,3 revenger,2 sentinel); **w2:93** (61 reviewer,11 scout,6 executor,6 critic,4 mutation-tester,2 sentinel,2 connector,1 simplifier). **166 new seats total**; registries/specs/assignments committed. No role/model parameter was hardcoded.
- **Residual-shape conformance defect:** after post-wave edits, 38 existing reviewer identities were individually resumed, not dispatched as a third validated wave or a ≤8-seat residual task batch. No new seats were added; this still exceeds the addendum's ordinary residual shape. Driver/report completion is not admission.
- At recovery, 15 jobs showed **cancelled**: SiblingImpact; CR18,42,47; CR06,25,32,33,35,43,44,46,48,49,50. Some had written partial/complete artifacts before cancellation. Parent reported **Anthropic429**; no per-seat provider error text was delivered, so it is not attributed to every cancellation. **No cancelled seat was respawned/replaced.** L1 completed reachable checks itself.
- Report exclusions are explicit: malformed w2 CR39/CR47 and w3 CR42 JSON were not laundered into the final ledger; retained originals remain committed. Included reports: assembler exit0, no rejected reports. The final score is the narrower input-keyed predicate, not proof that every required command was executed.
- R17 incident remains preserved in its lesson/report. R18 RerunC2After created then removed an empty live-lane `.ro-test` (17:29:07–27, its own report); several seats used live `git status` without `--no-optional-locks`. These are disclosed safety deviations, not sanctioned patterns. No ad hoc Git recovery plumbing was used this round.
- Final fleet misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only `.ufo/watchdog.log` and driver `.ufo/state/*.report-baseline`; none was touched. No inherited uncommitted work at dispatch; previous non-author spotcheck remained untouched.
- **Tool acquisition:** S19 fetched **c8 12.0.0**, ephemeral `npx -y c8`/official npm, for coverage; version recovered from its npm cache package metadata. No persistent L1 install, pacman transaction, routing change or REA use.
- **Stale-lane:** same round18 identity resumed after provider failure; no next round started and no other tameshi mission opened.
- **Open L0:** helper-owned recovery procedure, appended/pushed in fleet **`36500aa8b9b4a753370c808bfefb567b7f8b2497`**. Fleet/operator scope; never normalize ad hoc plumbing.

## Named residuals

SCORECARD round18 and `guard-kill-closure.md` EG-3 list 18 mutation survivors; P08 non-master and P11 object-directory coverage; unimplemented required-command binding; direct round16-measure GIT_* leak (registered wrapper scrubs); adopted-orphan signalling/same-tick PID reuse; unconfined canary tool; load-sensitive tsukuroi replay; deferred simplifications and older successor/environment/confinement debts. No claim closes these by prose. SiblingImpact was cancelled; no complete new cross-lane impact audit is claimed. Owner recommendations are retained in `w2/KumitateRouting.md`; no sibling changes were made.
