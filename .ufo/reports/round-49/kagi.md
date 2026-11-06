# kagi round 49 (attempt 1) — report

Lane: `kagi-shokunin` (secrets & vault ops), branch `master`. Lane final hash (ls-remote verified after the last lane commit): **`6c624dc54708afadf77bd13b58263f6c2195b71c`**. Shape: one v1 build wave of 13 seats (run-15 band 8–16); no residual call; no wave 2. Round total: 13 seats. WAVE-DONE received from the orchestrator with all 13 seats settled (`.ufo/waves/round-49/build-results.json`, 13 results, each with a final output). Dead seats: none.

Commits:

- Predeclaration `082bfb3f6baa2407df2a23c0489043495b4dce4d`. No amendment.
- Candidate `a74ae538d3426ec04c045200e18e0e3cb2540035`.
- Landing (wave evidence, legs, receipts) `318458a7ed456af71ce178957990e2e12c156cf8`.
- Final receipts `6c624dc54708afadf77bd13b58263f6c2195b71c`.

Claim BASE `89afe91878f10805921d3caa67d28d21b33226da` (the round-48 verifier spot-check tip). No earlier attempt of this round exists (`.ufo/watchdog.log` holds only the attempt-1 launch line for round 49).

## Work performed

Declared claims (two):

- **C1 — operability, capability acquisition.** The lane executes the OpenBao token and lease mechanics that `corpus/knowledge/vault-openbao-token-lease-lifecycle.md` documents from S016. Counter `C1_OPENBAO_TRIAL`, BASE 0 (absent), target 5. Each test T1–T5 must read HOLDS against a real OpenBao 2.7.2 `bao server -dev` and BROKEN under its own falsifier shim.
- **C2 — calibration.** The lane's stated self-counts agree with the observed repo state. Counter `C2_SELF_COUNTS` over six frozen keys of `python3 corpus/self-counts.py`, BASE 6 (3 STALE stamp counts, 3 SETUP declaration counts), target 0.
- **Axis duty.** All six axes sit at 9. A capability entered in round 48, so the stagnation nudge does not fire. Every axis is tied lowest, so both claims work a lowest axis (`plans/round-49.md` §Axes).

Work items:

- **Tool installed.** OpenBao v2.7.2, official GitHub release tarball → `~/.local/bin/bao` (sha256 `9c5f3628…41b788`). The tarball sha256 equals its `checksums.txt` line (`sha256sum -c` OK) and the GitHub asset digest; `checksums.txt` equals its asset digest. The `.gpgsig`/`.sigstore.json` signatures were **not** verified. pacman stayed paused. Reason: the C1 trial. Receipt `.ufo/waves/round-49/controls/tool-install.txt`.
- **Frozen plan and instruments** (`082bfb3f`): `plans/round-49.md`, `plans/round-49-c1.sh`, `plans/round-49-c2.sh`, `plans/round-49-controls.sh`, fixtures `.ufo/waves/round-49/controls/fixtures/`.
  - Pre-freeze controls ran and were committed before any seat scored: `CONTROLS: ALL-MATCH (match=19 mismatch=0)` (`controls/controls-prefreeze.txt`).
  - C1: do-nothing 0, reference 5, constant-HOLDS 0, real bao forced onto PATH 0, no entry section 0, T1 after-check removed 4, entry naming 2.7.1 0, unpinned bao SETUP, trial printing a token 0, silent producer SETUP.
  - C2: do-nothing 6, reference 0, entry deleted SETUP, stamp row deleted SETUP, `self-counts.py` changed SETUP, counts only 3, docs only 3, count written 999 → 1, frozen key row removed SETUP.
- **C1 candidate** (`a74ae538`):
  - `corpus/openbao-token-trial.sh`. Seat K49ExecTrial hardened the frozen reference: cleanup on EXIT/INT/TERM/HUP kills only its own server PID, the server start retries on fresh random 127.0.0.1 ports, and the script is shellcheck-clean. Grammar and test logic are unchanged (`build/K49ExecTrial/diff-vs-reference.patch`).
  - The entry gains `## Measured (round 49 — OpenBao 2.7.2 dev server, 127.0.0.1, throwaway tokens)`, append-only (0 removed lines). K49ScribeEntry drafted it with a supersession note for `:9` and §How kagi uses this, and a "Does not establish" list (dev mode, one host, one release, no Vault, no Kubernetes).
  - Review narrowings from K49ReviewerTrial (all five tests rated measures or measures-with-narrowing):
    - T1: the refusal text is `permission denied`. Expiry is attributed by isolation; a 60 s token survives the same window.
    - T2: the granted value is `auth.lease_duration`. Without the cap the same renewal is granted 3600.
    - T3: the refusals carry `batch tokens cannot be renewed` and `batch tokens cannot be revoked`, even for root.
    - T4: `orphan=true` is specific to the userpass route.
    - T5: contrasted. Under a 30 m token the same lease survives 5 s.
  - A SCORECARD capability row and a `PROVINCE.md` "Core, round 49" bullet.
- **C2 candidate** (`a74ae538`; seat K49ExecC2 patch, applied by the L1):
  - `corpus/knowledge/iso-11770-3-edition-status.md` gains `Reverify: R21-02` and its parenthetical (appended lines only), plus one stamp row.
  - `corpus/README.md:65,67`, `SKILL.md:46` and `PROVINCE.md:73` now state 124 stamps and 33/3/36 declarations. The history parentheticals are kept.
  - Ledger rows R12-03 (`^122$` → `^124$`) and R14-01 (prefix → full literal `entries=36 row_linked=33 …`) were migrated with journal `.ufo/waves/round-49/expectation-migrations.json`. `corpus/expect-journal.sh` → `EXPECT_JOURNAL: CLEAN (changed=2 journaled=2)`.
  - One terminal restamp names all 124 paths. Per K49Connector E1/E2, the count was computed after the ISO row landed: 124, not 123.
- **End-to-end domain trial** (learning by doing): `bash corpus/openbao-token-trial.sh --work <scratch>` on this host → `OPENBAO_TRIAL: HOLDS holds=5 broken=0 error=0 bao=v2.7.2`, rc 0. The server was a throwaway in-memory dev server; its random root token stayed in scratch and was deleted.
- **Non-claim work.**
  - E48-1 appended to `plans/round-47.md`, which closes round-48 routed item 2.
  - Erratum E49-1: the round-48 quote word counts (closure D2), with a counting rule.
  - M49-2 records closure D1 (the completion form).
  - QM61.
- **Attacks and their answers.**
  - **K49CriticClaims.** Rulings, recorded unsoftened:
    - C1 "as measured" is **falsified**: a 7-line trial that reads the counter's PATH (`*/bin/sh[1-5]:*`) scores `value=5` without starting a server.
    - The C1 after-state is **weakened**: "its entry documents" is broader than T1–T5.
    - The C1 axis **holds**.
    - C2 is **weakened**: 3 of the 6 keys are a real gate repair; the other 3 are revision-bound counts.
    - Separability **holds**.
  - **K49CriticCeiling.** It forged both counters:
    - C1: a 13-line identity-detecting trial reads `value=5`.
    - C2: repointing the R12-03/R14-01 commands at a stub reads `value=0`, because `claim-ledger.tsv` is not frozen.
  - **Its legs.**
    - `leg-c1-transparency.sh` logs every `bao` argv and requires executed mechanics with no identity reads. It reads **PASS** on the candidate (`identity_reads=0 holds=5 calls=33`) and FAIL on both C1 forgeries.
    - `leg-c2-live-sources.sh` reads **FAIL** on the candidate: `source-redefined: R12-03 R14-01`. Its code compares whole ledger rows, so it refuses the journaled expect migrations. Its header states the rule as "command column byte-identical". Every count that leg re-derives matched the stated counts; only the whole-row check failed.
    - I ran the header's stated rule as an L1 leg, `final/leg-c2-source-commands.sh`. It reads **PASS** on the candidate (commands identical, journal CLEAN) and **FAIL** on the forgery shape (`command-redefined` ×2, journal `REFUSED (violations=4)`), in `final/leg-c2-source-commands.txt`. The closure rules on which reading binds.
  - **K49ReviewerPlan.**
    - K49RP-1: C2 false green. The source rows are unpinned (the same class as the CriticCeiling forgery).
    - C1 has no false green beyond the named ceiling.
    - K49RP-2: a shim-wedged trial burns 600 s (false red, latency).
    - K49RP-3: orphan containment depends on the EXIT trap.
  - **K49MutCounters.** 12 mutants: 7 killed, 5 survived. The survivors are C1 DUP→HOLDS, NONE→BROKEN and drop setup_ok, and C2 drop G5 and MIN_LINES 0. Each survivor has a proposed killing control, run against both the frozen counter and the mutant (`build/K49MutCounters.md` §4).
  - **K49Sentinel.**
    - S-01 and S-04–S-08 PASS: no token in output, loopback-only bind, caller tokens cannot reach the trial, and 0 token-shaped strings in committed round files.
    - S-02 LOW: the dev root token and the userpass password sit in local argv.
    - S-03 LOW: NOSECRET misses about 1 in 5 batch-token shapes. The candidate prints none.
  - **K49Connector.** No sibling lane holds OpenBao/Vault token ground. It flagged E1–E7:
    - E1/E2/E3/E6 were acted on: the terminal restamp, 124 not 123, the R12-03 migration, and the entry scope sentence.
    - E4/E5 are answered by the routed red census below.
- **Orphaned dev servers (defect found and fixed in-round, routed).** At ~21:43Z I found 8 round-49 `bao server -dev` processes. They were bound to 127.0.0.1 only, and had been re-parented after their trial shells died during seat attack runs; I terminated them. Per K49ReviewerPlan's attribution: 5 from K49CriticClaims, 2 from K49Sentinel, 1 from K49ReviewerPlan. Record: `final/orphan-servers.txt`, with token arguments redacted. Cause: the trial's EXIT-trap cleanup does not run on SIGKILL (K49RP-3). After my repeat counter run the host had 0 dev servers (`final/c1-repeat-candidate.txt`).
- **Planner mapping.** The L1 held the planner seat; the validator rejects `planner`.
- **Refusal boundary.** Every OpenBao server was a throwaway dev server with a random root token kept in scratch. No vault, `op`, account or real credential was touched. No host sysctl changed. One seat receipt, `build/K49ReviewerPlan-receipts/hang-orphan.txt`, carried two dead dev-server root-token arguments; I redacted them before landing. The only token-shaped strings left in committed round-49 files are the documentation example tokens inside the public OpenBao docs page captures (`build/K49ExecSources/S016.body`, `build/K49ScoutSources/openbao-tokens-20261106.body`).

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Predeclaration: plan, counters, controls, fixtures, BASE receipts, install receipt | `082bfb3f6baa2407df2a23c0489043495b4dce4d` | `LOG.md` Round 49 (first bullet) |
| Candidate: trial; entry §Measured; capability row; PROVINCE core line; ISO entry Reverify + stamp; stated counts; R12-03/R14-01 migrations + journal; terminal restamp; S105 + fetch row + capture; QM61; lesson `corpus/lessons/round-49.md`; LOG; manifest rows 49 C1/C2; E48-1 append | `a74ae538d3426ec04c045200e18e0e3cb2540035` | `LOG.md` Round 49 |
| Landing: wave evidence (13 seats: spec, dispatch, results, reports), legs, measured-at-candidate, kill rules, census end, verify BASE/candidate, sweep BASE/candidate, BASE gate readings, orphan-server record, lesson landing addendum | `318458a7ed456af71ce178957990e2e12c156cf8` | `LOG.md` Round 49 (verdict line points at `final/`) |
| Final receipts: measured at landing, sweep at landing | `6c624dc54708afadf77bd13b58263f6c2195b71c` | `LOG.md` Round 49 |

## Before → after measurements

| Claim | Counting command | BASE `89afe918…` | Candidate `a74ae538…` and landing `318458a7…` |
|---|---|---|---|
| C1 operability (capability) | `bash plans/round-49-c1.sh <rev>` | `C1_OPENBAO_TRIAL: value=0 absent=1 pins=1` (`controls/c1-base.txt`) | `value=5 discriminating=5 pins=1 setup_ok=1 nosecret=1 real_rc=0 none_rc=2`; T1–T5 `real=HOLDS,shim=BROKEN,entry=1` at both (`final/measured-at-candidate.txt`, `final/measured-at-landing.txt`); a repeat at the candidate reads the same (`final/c1-repeat-candidate.txt`) |
| C2 calibration | `bash plans/round-49-c2.sh <rev>` | `C2_SELF_COUNTS: value=6 keys=6 lines=63` (3 STALE, 3 SETUP; `controls/c2-base.txt`) | `value=0 keys=6 lines=63`, six keys OK; `SELF_COUNTS: POLICY (claims=63 stale=0 … policy=2 setup=0)` at both |

Kill rules at the candidate (`final/kill-rules.txt`):

- The entry has 0 removed lines.
- 0 files carry the dev-root-token shape.
- The frozen instruments are unchanged from predeclaration to candidate (`git diff --stat` empty).
- The R25-02/R29-01/R29-02 rows are byte-identical to BASE.
- 0 ledger rows were removed.
- The append-only files have 0 removed lines.
- Ledger `verify` at the candidate prints no STALE or MISSING stamp line (`final/verify-candidate.txt`).
- No kill rule fired.

Harm checks:

- **Ledger `verify` (clean clones).**
  - BASE: `CLAIM_LEDGER: POLICY (claims=86 policy=3 stamped=123)` with 15 FAIL (`final/verify-base.txt`).
  - Candidate: `stamped=124` with 13 FAIL (`final/verify-candidate.txt`). R12-03 and R14-01 (C2's surface) and R36-01 left the FAIL list; no row entered it.
- **Lane gates, BASE (`final/gates-base.txt`) → candidate:**
  - `SOURCES_CENSUS: CLEAN`: rows 104 → 105.
  - `CLAIMS_DECLARED: CLEAN`: claims 23 → 25.
  - `QUOTE_LOCATE: CLEAN located=8 rows=8`: unchanged.
  - `ANCHOR_PINS: CLEAN (pins=4)`: unchanged.
  - `RELEASE_CLOCK: CLEAN (on_release=29 …)`: unchanged.
  - `DOC_AUDIT`: BROKEN → CLEAN.
- **Self-description sweep on git archives:** BASE `n=4` (`final/sweep-base.txt`) → landing `n=4` (SD6=3, SD8=1; `final/sweep-landing.txt`). The candidate archive read `n=22` (`final/sweep-candidate.txt`); the extra 18 are SD6 citations of `.ufo/waves/round-49/` evidence that landed only with the landing commit.

Named ceilings (recorded, not closed):

- C1, shim detection by PATH or binary identity. For this candidate it is answered by `leg-c1-transparency.sh`, not by the counter.
- C1, NOSECRET shape coverage (S-03).
- C1, dev mode on one host and one release.
- C1, orphan containment on SIGKILL.
- C2, the source rows are unpinned. For this candidate it is answered by `leg-c2-source-commands.sh`.
- C2, the stamp count is revision-bound.
- The five mutation survivors.

## Sources & frontier

- **Registry rows:** 104 → 105 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- **Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`:**
  - Round start: rc 0, `kagi ok` (`controls/census-start.txt`).
  - Round end: rc 0, `kagi ok` (`final/census-end.txt`).
  - The lane-local census reads CLEAN at both ends (104 → 105).
- **Rows added by tier:** A 1, B 0, C 0.
  - S105: OpenBao PKI API docs, `https://openbao.org/docs/api/secret/pki/`, opened 2026-11-06, HTTP 200.
  - Decoded sha256 `9fa76939…5e5c1123`, 620683 B; capture `.ufo/waves/round-49/capture/S105.body`.
  - Located quote, 14 words by `wc -w`, rendered-text-v1 count 1: "Specifies if certificates issued/signed against this role will have OpenBao leases attached to them".
  - Used by `corpus/lessons/round-49.md`; fetch row in `corpus/source-fetches.tsv`.
- **Rows touched old→new:** none.
- **Rows re-opened:** S016, live on 2026-11-06. The body is byte-identical to the round-47 capture, the rendered-text digest equals the 2026-10-21 capture's, and four teaching quotes locate with count 1.
- **Sourced claim:** C1 rests on S016 (re-opened) and S105 (opened this round). The entry's §Measured and the lesson's `source:` line cite them.
- **Rejected** (recorded in the lesson §Gate):
  - The OpenBao v2.7.2 release page as a new row: it duplicates S093. Flip: S093's capture is lost.
  - An S016 fetch-row refresh: it is coupled to `inrow-pins.tsv` and the quote manifest. Flip: all three move in one commit.
- **Frontier advanced:** the round-21 documented-only OpenBao token ground is now executed ground, recorded as the `PROVINCE.md` "Core, round 49" bullet.
- **Mistakes mined** (`corpus/lessons/round-49.md` §Mistakes):
  - M49-1: the round-45 entry landed undeclared and unpinned; `docs` is BROKEN from `072bb0b`. Captured-by: QM35/R14-01 existed, but no round 45–48 plan ran `docs`. Fix: C2 plus QM61; the check reads FLAG on `072bb0b` and CLEAN on the repaired tree.
  - M49-2: the round-48 report said "every report ends `SEAT-STATUS: complete`" (it held for 5/13 reports and 4/13 outputs). Captured-by none. Fix: a FLAG→CLEAN check.
  - M49-3: the round-48 quote word counts are 6 and 13, not 8 and 12. Fix: E49-1 with a counting rule, plus a FLAG→CLEAN check.
  - Landing addendum: the orphaned dev servers, routed.
- **Ledger red census (QM32/QM57):** 15 FAIL and 3 POLICY at BASE, enumerated in the lesson §Routed. R12-03 and R14-01 were migrated inside C2; the rest are routed.
- **Misroot sweep:** fleet `git status --porcelain` shows only ` M .scratch/run15-state.json` and `?? .scratch/run15-wrapup/misroot-cff0b4cb/`. Both are orchestrator-owned; nothing from this lane's seats is there.
- **Assimilation:** none. `shokuknow/merge/kagi/` stages 81 entries, and none is on OpenBao/Vault tokens, leases or self-count calibration (L1 grep; K49ScoutSources §1.2).
- **considerthese:** none taken. The newest file is `2026-10-26.md`; its four proposals are operator policy, bookkeeping, or a premise that no longer reproduces (lesson §considerthese).

## Trend verdicts

- **expansion: improved.**
  - New executed ground: the OpenBao token/lease mechanics run on this host for the first time.
  - A new capability row: the OpenBao token/lease lifecycle trial, first working round 49.
  - One new tier-A registry row, S105.
- **quality: improved.**
  - The entry's OpenBao rows are measured, with review narrowings (the T5 contrast, the T1 refusal text).
  - `docs` moved from BROKEN to CLEAN.
  - Two ledger rows were migrated with a journal, and ledger FAIL rows dropped from 15 to 13.
  - QM61 added.
- **discernment: improved.**
  - The lane's self-counts agree with the repo again: 6 → 0.
  - One admit and two rejects, each with a flip condition.
  - The critics' rulings (C1 "falsified as measured" by PATH-reading, C2 "weakened") are recorded unsoftened, with legs shown able to fail.
  - The contradiction between one seat leg's code and its header is reported, not smoothed over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md:46` (the decision-table stamp count is now true, C2) and `corpus/knowledge/vault-openbao-token-lease-lifecycle.md` §Measured (round 49), whose error signatures are `permission denied` and `batch tokens cannot be revoked`. No non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` Round 49 records the OpenBao token/lease trial on a throwaway dev server, `OPENBAO_TRIAL: HOLDS holds=5` (`.ufo/waves/round-49/final/measured-at-landing.txt`). No non-author verifier yet.
- [~] Instructions executable by an agent without oral context. Evidence: `bash corpus/openbao-token-trial.sh --work <dir>` and `bash plans/round-49-c1.sh <rev>` both run with no context (`final/measured-at-landing.txt`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: K49Connector found no sibling OpenBao/Vault token ground (`.ufo/waves/round-49/build/K49Connector.md` §1). The PROVINCE core bullet names one host, one release and dev mode.

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Wave evidence and WAVE-DONE

Wave `kagi-r49-build`, one v1 wave, 13 seats:

- executor 3: K49ExecTrial, K49ExecC2, K49ExecSources
- scribe 2: K49ScribeEntry, K49ScribeLesson
- scout 1: K49ScoutSources (spawned as `K49ScoutSources-2`)
- connector 1: K49Connector
- reviewer 2: K49ReviewerPlan, K49ReviewerTrial
- critic 2: K49CriticClaims, K49CriticCeiling
- mutation-tester 1: K49MutCounters
- sentinel 1: K49Sentinel

Attack share is 5/13 = 38 %. The spec validated under `ufo-wave-policy.json` (band 8–16) and was dispatched through `build-dispatch.json` (spawn 13). `build.ready` became `build.ready.dispatched`; the wave filled in tranches of 5 and then 8.

WAVE-DONE was received with all 13 seats settled.

Completion form, stated exactly per M49-2:

- 13/13 results carry a final output.
- The literal `SEAT-STATUS: complete` appears in 5/13 outputs (K49ExecTrial, K49ExecSources, K49ScribeLesson, K49CriticClaims, K49Sentinel).
- It ends 4/13 report files.
- K49ExecTrial and K49ReviewerPlan also confirmed completion by message to the L1.

## Tool installs

- OpenBao v2.7.2 (`bao`): official GitHub release tarball → `~/.local/bin/bao`. The checksums file and asset digests were verified; the signatures were not. Reason: the C1 trial.
- Seats: K49ExecTrial ran shellcheck 0.11.0 (`build/K49ExecTrial/shellcheck.txt`). Install provenance is recorded in that seat's report, not re-checked by the L1.

## Open questions

No new L0 question. Earlier kagi L0 lines are routed around, not treated as answered.

Routed to round 50 (lesson §Routed and landing addendum):

- **Ledger rows outside C2.**
  - Drifted or red, FAIL: R11-08, R13-01, R21-02, R22-03, R24-05, R24-06, R24-15, R31-02, R33-02, R34-03, R38-01.
  - Operator-routed: R25-02 FAIL; R29-01, R29-02 and R38-03 POLICY.
- **C1 counter amendments:**
  - non-identifying shim directories plus a PATH-reader control;
  - NOSECRET widened to batch-token shapes;
  - process-group kill of the dev server;
  - controls for the survivors.
- **C2 counter amendment:** freeze the source-row commands.
- **Carried:** SD10, S098, the Vault-lease MDX normalizer gap, and the capture redaction convention.

## Verdict on the round

At the candidate and at the landing, C1 (0 → 5) and C2 (6 → 0) each measured at their frozen target, with the instruments byte-identical to the predeclaration. No kill rule fired.

Two attacks are put to the closure:

- C1 carries a critic ruling of "falsified as measured" on the counter's PATH-reading ceiling. For this candidate it is answered by a leg shown able to fail.
- C2 carries a seat leg that FAILs on its own code while passing its stated rule. I ran that stated rule as an L1 leg, which is shown able to fail.

The harm measures above show no harmed axis: the self-description sweep is unchanged at n=4, ledger FAIL rows went 15 → 13, and every lane gate is CLEAN. The non-author closure rules on admission.
