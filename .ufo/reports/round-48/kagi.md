# kagi round 48 (attempt 1) — report

Lane: `kagi-shokunin` (secrets & vault ops), branch `master`. Lane final hash (ls-remote verified after the last lane commit): **`f01b729d00fe04e5d9530f802f44c812f873de9c`**. Shape: one v1 build wave of 13 seats (run-15 band 8–16); no residual call; no wave 2. Round total: 13 seats, all settled (WAVE-DONE received; `.ufo/waves/round-48/build-results.json`, 13 seats, every report ends `SEAT-STATUS: complete`). Dead seats: none.

Commits:

- Predeclaration `164f0ea5ed8b76a671f9b076158d1d8022881813`.
- Amendment A1 `52991e5da64cbacaa724b28b407cf5765fd21b41`. It was made before any seat ran.
- Candidate `877558299cbac333013672827b974be4e5ea6bf4`.
- Landing (wave evidence, candidate legs, receipts) `7ce3fe70bd01983ae496bda1df51cdd36453df79`.
- Final receipts `f01b729d00fe04e5d9530f802f44c812f873de9c`.

Claim BASE `76da518fcc3029e738648bd6fd4ba5571df01c1c` (the round-47 verifier spot-check tip). No earlier attempt of this round exists (`.ufo/watchdog.log` holds only the attempt-1 launch line).

## Work performed

Declared claims (two):

- **C1 — operability, capability acquisition.** The lane now executes the SOPS/age access and rotation mechanics that `corpus/knowledge/sops-age-key-rotation.md` documents. Counter: `C1_SOPS_AGE_TRIAL`, BASE 0, target 5.
  - Each of five tests has to read HOLDS against the real sops 3.13.3 and age-keygen v1.3.2.
  - Each test also has to read BROKEN under its own falsifier shim.
- **C2 — calibration.** The evidence readings stated in `SCORECARD.md` §Capabilities match what the commands actually print. Counter: `C2_CAPABILITY_READINGS`, BASE 3 mismatches, target 0.
- **Axis duty.** All six axes sit at 9, which is the saturation line, and no capability has entered since round 40. The stagnation nudge therefore fires (`SCORECARD.md` §Saturation: line 9, N = 3). It waives the lowest-axis obligation, so C1 is the capability move. C2 still works calibration, an owned axis tied for lowest.

Work items:

- **Tools installed.** Both are official GitHub release binaries placed in `~/.local/bin`; pacman stayed paused.
  - sops v3.13.3: sha256 `e5bec334…7fef6b`. It matches `sops-v3.13.3.checksums.txt` (`sha256sum -c` OK) and the GitHub asset digest.
  - age and age-keygen v1.3.2: the tarball sha256 `cbe24006…6ac10` equals the asset digest. The sigsum `.proof` was downloaded but **not verified**, because no verifier is installed.
  - Reason: the C1 trial. Receipt: `.ufo/waves/round-48/controls/tool-install.txt`.
- **Frozen plan and instruments** (`164f0ea5`): `plans/round-48.md`, `plans/round-48-c1.sh`, `plans/round-48-c2.sh`, `plans/round-48-controls.sh` and the fixtures under `.ufo/waves/round-48/controls/fixtures/`.
  - Pre-freeze controls ran and were committed before any seat scored: `CONTROLS: ALL-MATCH (match=16 mismatch=0)` (`controls/controls-prefreeze.txt`).
  - C1 controls: do-nothing 0, reference 5, constant-HOLDS 0, PATH-bypass 0, no entry section 0, silent producer SETUP, weakened T5 4, wrong-version entry 0, unpinned binary SETUP, printed identity 0.
  - C2 controls: do-nothing 3, reference 0, deleted pairs 3, readings outside the section 3, partial 2, wrong number 1.
- **Amendment A1** (`52991e5d`, before any seat). The C1 secret kill rule matched its own instruments, so it now reads the key-shaped ERE `AGE-SECRET-KEY-1[0-9A-Z]{58}` (`plans/round-48.md` §Amendment A1; mistake M48-2; QM59).
- **C1 candidate** (`87755829`):
  - `corpus/sops-age-trial.sh`: seat K48ExecTrial hardened the frozen reference fixture (SOPS_* sweep, umask, `--work` arity, shellcheck-clean). The test logic and output grammar are unchanged.
  - The entry gets `## Measured (round 48 — sops 3.13.3, age-keygen v1.3.2, …)` with T1–T5, appended only.
  - Supersession note: the "Nothing here was executed" scope sentence is superseded for these five mechanisms (K48CriticClaims D-13).
  - T2 states its limit (K48RT-02). The new-data-key half was measured by an unwrapped-key hash probe: `5b56e5aa…` → `fd34d55b…` across `rotate`, and unchanged across `updatekeys` (`build/K48ReviewerTrial-dek-probe.sh`).
  - Measured narrowings, from K48CriticCeiling:
    - B1: removing a key group needs the old threshold's identities; otherwise `updatekeys` exits 128 and the removed key keeps access.
    - B2: when the edited rule no longer matches the file, `updatekeys` exits 1.
    - B3: an edited MAC makes decrypt exit 51.
    - B4: `rotate --add-age/--rm-age` matches the round-22 Clarification.
  - Also new: a SCORECARD capability row and a `PROVINCE.md` core bullet.
- **C2 candidate** (`87755829`):
  - One current-readings line inside `SCORECARD.md` §Capabilities: K02 `located=8 rows=8`, K07 `claims=23` (revision-bound, and the line says so), K10 `PASS (12 cases)`.
  - The historical rows are kept.
  - `SKILL.md:826` changes `PASS (8 cases)` → `PASS (12 cases)`.
  - No gate byte changed (seat material from K48ExecC2).
- **End-to-end domain trial** (learning by doing): `bash corpus/sops-age-trial.sh` on this host gives `SOPS_AGE_TRIAL: HOLDS holds=5 broken=0 error=0 sops=3.13.3 age-keygen=v1.3.2`, rc 0 (`final/measured-at-candidate.txt`).
- **Attacks and their answers.**
  - Reviewers K48RP-01..08 and K48RT-01..08, critics D-1..D-13 and B1–B4, mutation-tester (17 mutants) and sentinel S-01..S-09.
  - Their findings became candidate-side legs LA–LE (`final/candidate-legs.sh`), all PASS at the candidate and at the landing.
  - Leg LA was shown able to fail: on the critic's shim-detecting trial it reads `LEG LA FAIL binary-inspection-tokens=4` (`final/leg-la-negative.txt`).
  - No frozen sentence changed.
- **Planner mapping.** The L1 held the planner seat; the validator rejects `planner` and `labrat`.
- **Refusal boundary.** Every age identity was a throwaway generated in scratch and deleted with it. No vault, `op`, account or real key was touched. Sentinel S-04/S-05 confirm this: 0 key-shaped strings, and the trial never opens the caller's key paths. No host sysctl was changed.

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Predeclaration: plan, counters, controls, fixtures, BASE receipts, install receipt | `164f0ea5ed8b76a671f9b076158d1d8022881813` | `LOG.md` Round 48 (first bullet) |
| Amendment A1: C1 secret kill rule reads a key-shaped ERE | `52991e5da64cbacaa724b28b407cf5765fd21b41` | `LOG.md` Round 48 (first bullet) |
| Candidate: trial; entry §Measured; capability row; PROVINCE core line; current-readings line; SKILL.md:826; S103/S104 + fetch rows + captures; QM59/QM60; lesson `corpus/lessons/round-48.md`; LOG; manifest rows 48 C1/C2; stamps | `877558299cbac333013672827b974be4e5ea6bf4` | `LOG.md` Round 48 |
| Landing: wave evidence (13 seats), legs LA–LE + negative, measured-at-candidate, census end; round-48 calibration row names the routed reds | `7ce3fe70bd01983ae496bda1df51cdd36453df79` | `LOG.md` Round 48 (verdict line points at `final/`) |
| Final receipts: measured at landing, sweep BASE/landing | `f01b729d00fe04e5d9530f802f44c812f873de9c` | `LOG.md` Round 48 |

## Before → after measurements

| Claim | Counting command | BASE `76da518f…` | Candidate `87755829…` (and landing `7ce3fe70…`) |
|---|---|---|---|
| C1 operability (capability) | `bash plans/round-48-c1.sh <rev>` | `C1_SOPS_AGE_TRIAL: value=0 absent=1 pins=1` (`controls/c1-base.txt`) | `value=5 discriminating=5 pins=1 setup_ok=1 nosecret=1 real_rc=0 none_rc=2`, T1–T5 `real=HOLDS,shim=BROKEN,entry=1` (`final/measured-at-candidate.txt`; landing identical, `final/measured-at-landing.txt`) |
| C2 calibration | `bash plans/round-48-c2.sh <rev>` | `C2_CAPABILITY_READINGS: value=3 keys=10` (K02, K07, K10 DIFF; `controls/c2-base.txt`) | `value=0 keys=10`, all ten keys MATCH (candidate and landing) |

Kill rules at the candidate (`final/measured-at-candidate.txt`):

- The entry has 0 removed lines.
- 0 key-shaped strings (A1).
- The BASE gates `corpus/*.sh`/`*.py` and `plans/round-39-c*.sh` are byte-identical. The only path the name-status lists is `A corpus/sops-age-trial.sh`, C1's new artifact. I read the C2 rule's "changes any byte of `corpus/*.sh`" as the BASE gate set, which `controls/instrument-sha256.txt` enumerates. That reading is stated here for the closure to rule on.
- `claims-declared.tsv` and `quote-bodies.tsv` have 0 removed rows.
- The append-only files have 0 removed lines.
- Both counters exit 0.
- No kill rule fired.

The instruments are byte-identical from predeclaration to candidate (`git diff --stat` empty), so the M47-3/QM58 instrument-trust class does not apply.

Harm checks:

- The self-description sweep, run like-for-like on git archives, reads BASE `n=4` → landing `n=4` (`final/sweep-base.txt`, `final/sweep-landing.txt`).
- The candidate archive read `n=20` (`final/sweep-candidate.txt`). The extra lines are SD6 citations of `.ufo/waves/round-48/` evidence that only landed with the landing commit, plus SD5 3, which the landing fixed by naming R25-02/R29-01/R29-02 in the round-48 calibration row.
- `python3 corpus/self-counts.py` gives the same output at BASE and at the candidate: `SELF_COUNTS: POLICY (claims=63 stale=3 …)`. The pre-existing stamps 122 vs 123 is routed.
- Lane gates at the candidate:
  - `SOURCES_CENSUS: CLEAN (rows=104 …)`
  - `CLAIMS_DECLARED: CLEAN (claims=23)`
  - `RELEASE_CLOCK: CLEAN (on_release=29 … fired=13 …)`
  - `QUOTE_LOCATE: CLEAN located=8 rows=8`
  - `ANCHOR_PINS: CLEAN (pins=4)`

Named ceilings (recorded and not closed):

- C1, shim detection. A trial that inspects the binary and answers BROKEN only under the shims reads 5 on the frozen counter (K48CriticCeiling, K48CriticClaims D-3). Leg LA answers this for this candidate and is shown able to fail.
- C1, T2's observable. On its own it cannot separate a new data key from fresh nonces (K48RT-02). The probe measured it separately.
- C2, K07 is revision-bound. It decays by +2 claims per round (D-12).
- C2, section parsing. A duplicated, fenced or commented `## Capabilities` heading escapes the section reader (K48RP-02, D-9). Leg LC shows the candidate uses none of these shapes.
- Mutation results (`build/K48MutCounters.md`): the frozen controls kill 6/11 C1 and 4/6 C2 mutants.
  - Survivors: the setup_ok conjunct, DUP-as-HOLDS, the T1/T3 shim swap, the SETUP_OK exit half, substring MATCH, and the timeout-as-0 case.
  - Each survivor has a proposed killing control, routed.
  - Leg LD checks the candidate's single-line and no-sops behaviour directly.

## Sources & frontier

- **Registry rows:** 102 → 104 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- **Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`:**
  - Round start: rc 0, `kagi ok` (`.ufo/waves/round-48/controls/census-start.txt`).
  - Round end: rc 0, `kagi ok` (`.ufo/waves/round-48/final/census-end.txt`).
  - The lane-local census reads CLEAN at both ends (rows 102 → 104).
- **Rows added by tier:** A 2, B 0, C 0.
  - S103: the SOPS v3.13.3 release page, decoded body sha256 `8dbbadc0…`, 177586 B, capture `.ufo/waves/round-48/capture/S103.body`.
  - S104: the age v1.3.2 release page, sha256 `652f8c81…`, 154312 B.
  - Both were opened 2026-11-06 and carry located quotes of 8 and 12 words. They are used by `corpus/lessons/round-48.md`, whose `source:` line cites both; fetch rows are in `corpus/source-fetches.tsv`.
- **Rows touched old→new:** none.
- **Rows re-opened:** S009, S010 and S011 were re-opened live on 2026-11-06. Their bodies are byte-identical to the round-21 captures, the footer still reads 2026-05-15 / 9b7b84e, and each quote is located with count 1 (`build/K48ScoutSources/located-quotes.txt`).
- **Sourced claim:** C1 rests on S009, S010 and S011 (re-opened this round), which the entry's §Measured cites per test, and on S103/S104 (opened this round).
- **Frontier advanced:** the round-21 documented-only SOPS ground is now executed ground, recorded as a `PROVINCE.md` "Core, round 48" bullet.
- **Mistakes mined** (`corpus/lessons/round-48.md` §Mistakes):
  - M48-1: capability-table readings drifted. Captured-by none. Fixed by the C2 counter, which is shown able to fail by K2-F4 → 1. Also QM60.
  - M48-2: the kill rule matched its own instruments. Captured-by none. Fixed by A1 and QM59. The ERE is shown matching a fabricated fixture while finding 0 matches in the instrument tree (`build/K48ScribeLesson/m48-2-receipt.txt`).
  - M48-3: the round-47 C2 header says "no successor row", which is false for S012/S013/S014/S016. Erratum E48-1 is in the lesson, and a checker reads FLAG on the original and CLEAN on the corrected copy.
- **Misroot sweep:** fleet `git status --porcelain` shows only ` M .scratch/run15-state.json` and `?? .scratch/run15-wrapup/misroot-cff0b4cb/`. Both are orchestrator-owned; nothing from this lane's seats is there.
- **Sentinel S-08 (recorded, not scrubbed).** The committed GitHub release captures S103/S104 each carry a logged-out page's `authenticity_token` and `auth_hydro_click_hmac` (`"logged_in":false`). They grant no access, and round 38 already committed captures of the same class. I kept the raw bytes because the fetch rows bind their sha256. A redaction convention (redacted body plus raw digest) is routed.
- **Assimilation:** none. K48ScoutSources read `shokuknow/merge/kagi/MERGE-REPORT.md` and found no SOPS/age or capability-table theme.
- **considerthese:** none taken. The newest file is still `2026-10-26.md`; its proposals are operator policy, bookkeeping, or a premise that no longer reproduces (lesson §considerthese).

## Trend verdicts

- **expansion: improved.**
  - New executed ground: the SOPS/age mechanics run on this host for the first time.
  - A new capability row: the SOPS/age access-vs-rotation trial, first working in round 48. It is the first new capability since round 40.
  - Two new tier-A registry rows, S103 and S104.
- **quality: improved.**
  - Two `[INFERENCE]` readings in the entry are now measured: T3 (history copies) and T4 (creation-rule edits).
  - Three narrowings are measured: B1–B3.
  - The new-data-key claim is measured by the key-hash probe.
  - S009–S011 were re-verified byte-identical.
  - Lane census, claims-declared, release-clock, quote-locate and anchor-pins are all CLEAN.
- **discernment: improved.**
  - The capability table's self-description agrees with the executed readings, 3 → 0.
  - Rejected: a separate checksums-file row, and the unverified sigsum proof as a provenance row (lesson §Gate).
  - The vacuous kill rule was caught and amended before data (QM59).
  - The critic's rulings are recorded unsoftened: C1 "weakened" on forgery resistance and on its claim sentence (D-3, D-6), C2 "falsified at the claim's sentence" by section-shape forgeries (D-9), and K07 durability "weakened" (D-12). The closure rules on them.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md:826` (claims-declared gate row, corrected this round) and `corpus/knowledge/sops-age-key-rotation.md` §Measured (error signatures rc 128/1/51 measured). No non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` Round 48 records the SOPS/age encrypt → updatekeys → rotate → key-group trial on sops 3.13.3 with `SOPS_AGE_TRIAL: HOLDS holds=5` (`final/measured-at-candidate.txt`). No non-author verifier yet.
- [~] Instructions executable by an agent without oral context. Evidence: `bash corpus/sops-age-trial.sh --work <dir>` and `bash plans/round-48-c1.sh <rev>` both run with no context (`final/measured-at-landing.txt`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: connector `.ufo/waves/round-48/build/K48Connector.md` found no sibling SOPS/age ground and only mechanism prior art to cite (chousa PATH-shim cells, kumitate proxy drift). The PROVINCE core bullet names one host and one version pair.

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Wave evidence and WAVE-DONE

Wave `kagi-r48-build`, one v1 wave, 13 seats:

- executor 3: K48ExecTrial, K48ExecC2, K48ExecSources
- scribe 2: K48ScribeEntry, K48ScribeLesson
- scout 1: K48ScoutSources
- connector 1: K48Connector
- reviewer 2: K48ReviewerPlan, K48ReviewerTrial
- critic 2: K48CriticClaims, K48CriticCeiling
- mutation-tester 1: K48MutCounters
- sentinel 1: K48Sentinel

Attack share is 5/13 = 38 %. The spec validated under `ufo-wave-policy.json` (band 8–16) and was dispatched through `build-dispatch.json` (spawn 13). `build.ready` became `build.ready.dispatched`, and WAVE-DONE was received with all 13 seats settled. Dead seats: none.

## Tool installs

- sops v3.13.3 (official GitHub release binary → `~/.local/bin/sops`; checksum-file and asset-digest verified). Reason: the C1 trial.
- age and age-keygen v1.3.2 (official GitHub release tarball → `~/.local/bin`; asset-digest verified; sigsum proof unverified). Reason: the C1 trial.
- Seats installed nothing (seat reports).

## Open questions

No new L0 question. Earlier kagi L0 lines are routed around, not treated as answered.

Routed to round 49 (lesson §Routed):

- SD10 and E48-1, appended where the plan text lives.
- S098, a `rejected` row that still carries `on-release`.
- The open reds R25-02/R29-01/R29-02.
- The Vault-lease MDX normalizer gap.
- C1/C2 counter amendments: K48RP-01 timeout, K48RP-02 section, and the mutation survivors.
- Self-counts stamps 122 vs 123.
- A capture redaction convention (S-08).

## Verdict on the round

At the candidate, C1 (0 → 5) and C2 (3 → 0) each measured at their frozen target, with the instruments byte-identical to the predeclaration. No frozen kill rule fired. The C2 kill-rule reading is the one stated under the measurements. Legs LA–LE pass at the candidate and the landing. The self-description sweep is unchanged at n=4, so no axis was harmed. The non-author closure rules on admission.
