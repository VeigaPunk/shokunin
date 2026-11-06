# kagi round 47 (attempt 1) — report

Lane: `kagi-shokunin` (secrets & vault ops), branch `master`. Lane final hash (ls-remote verified after the last lane commit): **`f199abc7ae2fe94c31d395721e231dd243b36e6e`**. Shape: one v1 build wave of 12 seats (run-15 band 8–16); no residual call; no wave 2. Round total: 12 seats, all settled (WAVE-DONE received; `.ufo/waves/round-47/build-results.json`). Dead seats: none.

Commits: predeclaration `b020d978bac91284a431710148ebb7a7950eaab8`; candidate `412efc7738b70600108b325925df76b976609de4`; landing (wave evidence, candidate-side legs, measured receipts) `7cb82e73ad7dd793be939728c68bd9f3630210a5`; final receipts (sweep, census end) `f199abc7ae2fe94c31d395721e231dd243b36e6e`. Claim BASE `252ef1cac9f41d84639c0d1f211d0e0911196112`.

## Work performed

Declared claims (two, on the lane's two axes):

- **C1 calibration.** The lane-local census `bash corpus/sources-census.sh` clears its 3 BASE findings: S094 and S099 used-by-nocite, plus S099 missing fetch provenance. The registry stays intact, and the S099 provenance is bound to the fleet git blob `75dd2612:.ufo/prompts/kagi-round-44.md`. Target 3. This closes round-46 closure routed item 5.
- **C2 freshness.** Each of the 11 fired Vault/OpenBao release-clock rows (S012–S016, S021–S026) has its teaching quote located in a live capture fetched on or after 2026-11-06, recorded in the new `corpus/fired-reverify.tsv`. The release-clock gate stays CLEAN. Target 11. This closes round-46 lesson routed item 4.
- Axis duty: all six axes tie at 9, so each claim works a tied-lowest axis. The stagnation nudge was not invoked.

Work items:

- **Frozen plan and instruments** (`b020d978`): `plans/round-47.md`, `plans/round-47-c1.sh`, `plans/round-47-c2.sh`, `plans/round-47-controls.py`.
  - Pre-freeze controls were executed and committed before any seat scored: 17 controls, `CONTROLS: ALL-MATCH (match=17 mismatch=0)` (`.ufo/waves/round-47/controls/controls-prefreeze.txt`).
  - C1 controls: do-nothing 0, reference 3, used-by narrowing 0, hand-written provenance 0, row deletion 0, silent census SETUP, fix plus a new finding 0.
  - C2 controls: do-nothing 0, reference 11, ledger without captures 0, round-36 dates 0, future dates 0, quote swap 0, verdict unset 0, clock gate broken 0, normalizer missing SETUP.
  - Named ceiling K2-C: hand-typed in-window times score 11.
  - BASE receipts: `controls/c1-base.txt`, `c2-base.txt`, `census-start.txt`, `instrument-sha256.txt`.
- **C1 candidate** (`412efc77`; material from seat K47ExecC1):
  - `source:` lines prepended to `corpus/lessons/round-43.md` (S094) and `round-44.md` (S099). They are prepended rather than appended because `round-44.md` has no trailing newline, so an end-of-file append would rewrite its last line.
  - An S099 row in `corpus/source-fetches.tsv`.
  - A capture `.ufo/waves/round-47/capture/S099.body`, byte-identical to the fleet blob (sha256 `e62e259c…1b80c`, 97077 bytes).
- **C2 candidate** (`412efc77`; material from seat K47ExecC2):
  - `corpus/fired-reverify.tsv` with 11 rows, all `teaching-holds` (`build/K47ExecC2/teaching-notes.md`).
  - 11 captures fetched 2026-11-06T19:34:14–15Z.
  - Three lane live legs agree on the sha256 of all 11: L1 at 19:29:56Z, K47ExecC2, and K47ReviewerLive at 19:34:42Z.
- **Non-claim curation:**
  - S040/S041 had an overdue recheck (`2026-11-05`). After a live re-open (K47ExecS040, K47ScoutSources) it moves to `90d`.
  - SCORECARD erratum E47-1 corrects the round-46 miscount (closure routed 1).
  - Terminology fix M47-2 (closure routed 2): a lane seat's re-fetch is now called "the lane's independent live leg", not "non-author".
  - QM58 added.
  - The round-47 calibration row now carries the operator-routed reds R25-02/R29-01/R29-02, so self-description SD5 goes 3 → 0.
- **Pre-candidate attacks:**
  - Reviewer K47RP-01..08, critic D-1..D-7, ceiling critic, mutation-tester and sentinel S-01..S-08 all found the same class: the counters execute the measured tree's own census, normalizer and gate, so a stubbed instrument scores each target.
  - These attacks became candidate-side legs L1–L8 (`.ufo/waves/round-47/final/candidate-legs.sh`), all PASS at the candidate. L1 was shown able to fail (`final/leg-l1-negative.txt`). No frozen sentence changed.
- **Planner mapping:** the L1 held the planner seat. The validator rejects `planner`, and also `labrat`; the labrat hypothesis ran as critic K47CriticCeiling.
- **Tooling and refusal boundary:**
  - No tool was installed or upgraded, pacman stayed paused, and no host sysctl was changed.
  - No secret value, token, `op://` path or vault field was read or written. Every fetch was a public GET (sentinel `build/K47Sentinel.md`).

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Predeclaration: plan, counters, controls, BASE receipts | `b020d978bac91284a431710148ebb7a7950eaab8` | `LOG.md` Round 47 |
| Candidate: C1 source lines + S099 provenance/capture; C2 ledger + 11 captures; S040/S041 recheck; SCORECARD E47-1 + post-move; QM58; lesson `corpus/lessons/round-47.md`; manifest rows; stamps | `412efc7738b70600108b325925df76b976609de4` | `LOG.md` Round 47 |
| Landing: wave evidence (12 seats), candidate legs, `final/measured-at-candidate.txt` | `7cb82e73ad7dd793be939728c68bd9f3630210a5` | `LOG.md` Round 47 (verdict line points at the final receipt) |
| Final receipts: sweep BASE/landing, census end | `f199abc7ae2fe94c31d395721e231dd243b36e6e` | `LOG.md` Round 47 |

## Before → after measurements

| Claim | Counting command | BASE `252ef1ca…` | Candidate `412efc77…` |
|---|---|---|---|
| C1 calibration | `bash plans/round-47-c1.sh <rev>` | `value=0 cleared=0 new=0 intact=1 bound=0` (`SOURCES_CENSUS: FAILED (findings=3 rows=102)`) | `value=3 cleared=3 new=0 intact=1 bound=1` (`SOURCES_CENSUS: CLEAN (rows=102 …)`) |
| C2 freshness | `bash plans/round-47-c2.sh <rev>` | `value=0 reverified=0 gate=1` | `value=11 reverified=11 gate=1` (`RELEASE_CLOCK: CLEAN (on_release=29 bound=29 unbound=0 observed=29 fired=13 derived=15)`) |

Candidate-side legs (`bash .ufo/waves/round-47/final/candidate-legs.sh 412efc77…`): every leg reads PASS.

- L1 instruments are byte-identical to BASE.
- L2 lessons have minus=0.
- L3 `release-clocks.tsv` is unchanged.
- L4 registry source cells are unchanged.
- L5 the ledger header is exact.
- L6 the bodies are mode 100644 and first added by the candidate.
- L7 none of the 11 capture blobs is among the BASE blobs (0/11).
- L8 the live legs agree.

Gates at the candidate:

- `CLAIMS_DECLARED: CLEAN (claims=21)` with self-test `PASS (12 cases)`.
- `RELEASE_CLOCK_SELFTEST: PASS (116 cases)`.
- `QUOTE_LOCATE: CLEAN located=8`.
- `ANCHOR_PINS: CLEAN`.
- `STAMP_DRIFT: rows=123 drift=0`.

Harm check:

- The self-description sweep, run like-for-like in a scratch archive, reads BASE n=7 → landing n=4 (`final/sweep-base.txt`, `final/sweep-landing.txt`).
- In the lane checkout the sweep also lists five layout-dependent SD6 lines. They sit on pre-existing citations that point at fleet paths, and the note in `sweep-base.txt` explains them.
- Fleet census: `kagi ok` rc 0.

Kill rules: none fired.

## Sources & frontier

- **Registry rows:** 102 → 102, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`:**
  - Round start: rc 0, `kagi ok` (`.ufo/waves/round-47/controls/census-start.txt`).
  - Round end: rc 0, `kagi ok` (`final/census-end.txt`).
  - The lane-local census moved FAILED (3) → CLEAN.
- **Rows added by tier:** A 0, B 0, C 0.
- **Rows touched old→new:**
  - S040 `recheck` `2026-11-05` → `90d`.
  - S041 `recheck` `2026-11-05` → `90d`.
  - Both are logged in `corpus/lessons/round-47.md` §Gate.
  - Provenance (not a registry row): an S099 row was added to `corpus/source-fetches.tsv`.
- **Sourced claims:**
  - C1 rests on S099 and S094.
  - C2 rests on S012–S016 and S021–S026.
  - Every one of these rows was opened 2026-11-06. The lesson §Gate carries the URL, access date, sha256 and a located quote of ≤25 words for each.
- **Mistakes mined:**
  - M47-1: SCORECARD miscount (captured-by none; SD10 shown able to fail, routed).
  - M47-2: "non-author" applied to a lane seat.
  - M47-3: the counters trust candidate-owned instruments (QM58; leg L1 shown able to fail).
  - M47-4: a stale "never re-checked" premise for S012.
- **Misroot sweep:** fleet `git status --porcelain` shows only ` M .scratch/run15-state.json` and `?? .scratch/run15-wrapup/…`. Both are orchestrator-owned, and nothing from this lane's seats is there.
- **Assimilation:** none. No `merge/kagi/` theme matches (`build/K47ScoutSources.md` §2).
- **Considerthese:** no new file after `2026-10-26.md`, and none of its four proposals was taken (`build/K47ScribeLesson/considerthese.md`).
- **Frontier rows advanced:** none.

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry or registry row.
- **quality: improved.**
  - The 11 fired rows' teaching was re-verified on the served Vault 2.2.1 / OpenBao 2.7.2 docs.
  - The lane census is CLEAN again.
  - The SCORECARD miscount was corrected by erratum.
  - Self-description mismatches dropped from 7 to 4.
- **discernment: improved.**
  - `on-release` was refused for S040/S041 because it would read UNBOUND.
  - Amendment B was refused as lane-only evidence.
  - Rejecting the narrowed `used-by` (K1-F1) was a frozen control.
  - QM58 is lesson-backed.

Critic rulings for the operator, recorded and not softened (`build/K47CriticClaims.md`):

- C1 is "weakened as calibration": it fixes registry self-description, not a score cell.
- Both claims are "falsified as a measurement" by the instrument-stub class. For this candidate, leg L1 answers that class, but the frozen counters do not, by themselves, entail the fix.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md:48` (release-clock decision row). No non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md:20` (round-3 pipeline). This round's re-verification of 11 Vault/OpenBao doc teachings is a domain fetch task, not the vault pipeline.
- [~] Instructions executable by an agent without oral context. Evidence: `bash plans/round-47-c2.sh <rev>` and `bash .ufo/waves/round-47/final/candidate-legs.sh <rev>` both run with no context.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: connector `.ufo/waves/round-47/build/K47Connector.md` found no sibling Vault/OpenBao rows and no sibling census tooling.

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Wave evidence and WAVE-DONE

Wave `kagi-r47-build`, one v1 wave, 12 seats:

- executor 3: K47ExecC1, K47ExecC2, K47ExecS040
- scribe 1: K47ScribeLesson
- scout 1: K47ScoutSources
- connector 1: K47Connector
- reviewer 2: K47ReviewerPlan, K47ReviewerLive
- critic 2: K47CriticClaims, K47CriticCeiling
- mutation-tester 1: K47MutCounters
- sentinel 1: K47Sentinel

Attack share is 5/12 = 42 %. Dispatch went through `build-dispatch.json` (spawn 12); `build.ready` became `build.ready.dispatched`. WAVE-DONE was received and all seats settled; no seat died.

## Open questions

No new L0 question. Earlier kagi L0 lines are routed around, not treated as answered.

Routed to round 48:

- Counter amendments: BASE-pinned instruments, header check, URL pin, Amendment A, duplicate-row refusal, and URL/quote-based target sizing.
- SD10.
- S098 is a rejected row that still carries `on-release`.

## Verdict on the round

C1 (0 → 3) and C2 (0 → 11) each measured at their frozen target at the candidate. No frozen kill rule fired, and all eight candidate legs read PASS. No axis was harmed. The non-author closure rules on admission.
