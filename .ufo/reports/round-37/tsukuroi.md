# tsukuroi — round 37 report (hyaku run 7; attempt 2 filed by L1 `TsukuroiR37a2`)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`. Base: `564db0b614b2914de5452f9ebd537a0653ae1de5`. Final lane hash: `c231d0bbc0aba3f9f1a08b588cd5a338d9c46e98`. Pre-report gate: `git ls-remote origin refs/heads/master` printed `c231d0bbc0aba3f9f1a08b588cd5a338d9c46e98	refs/heads/master`.

Attempt 1 (L1 `TsukuroiR37`) declared and froze the claims, ran the round's only wave and landed commits `083cd0c`…`a3cf2ef`, all pushed. It filed no report. Attempt 2 inherited those commits and ran the frozen claims unchanged. It re-measured them at the tip, repaired one misroot, corrected one count, landed `c231d0b` and filed this report. Attempt 2 dispatched no wave. Every claim was already adjudicated by wave-1 falsifiers, so another wave would have padded the round.

## Work performed

Declared claims (SCORECARD.md "Round 37 — declaration", commit `083cd0c`; C3 corrected before freeze at `b8ededd`):

- **C1, operability:** probe VERSION 8 (`tools/probe-child-env-allowlist-r37.py`) makes the livefive battery executable, non-vacuous and able to tell leaking tools from clean ones on five live tools. It repairs the round-36 routed defects S1, S3, S4 and the parameter-`env` rule.
- **C2, depth:** the round-36 journalctl-v262 note is correction-complete per the closure's routed list: 15-term predicate, `-F` truncation vs unchanged `-N` under `-n`, action-override row. Counter: `tools/check-journalctl-v262-corrections.py`.
- **C3, calibration:** the self-assessment matches the measured tree. Counter: `tools/check-self-assessment.py`, 27 fixed checks, mismatches 0 at the measured tip. This is the pre-freeze correction of the original verified-rate-ledger claim.

Work items:

- **Declaration and pre-data control.** `083cd0c`, `b8ededd`, `89bb8af` (wave spec plus do-nothing control receipt). Ordinals at base: operability 9, depth 8, coverage 9, freshness 9, calibration 9, adjacency 8 (SCORECARD.md:1857-1863).
- **C1: probe V8 frozen.** `29b22df`, probe sha256 `9aee085b45d7566d6ce398733c10d3d87ae29bce107c4bd13fcdffcb4854b064`. V7 control at base crashes (`.ufo/waves/round-37/before/v7-livefive-base.err`). The V8 livefive reading is clean (`before/v8-livefive-baseline.jsonl`).
- **C2: note corrections and finite checker.** `543a7ce`, then `718cc8f` and `d621b71` (counter corrections to the note's actual identifier spelling, mined as R37-C2-COUNTER-REFERENCE-DRIFT).
- **C3: self-assessment re-derived.** `d06cedb`, `ee36f9e`, `5124bf3`, `0e5f70f`, `3c456a5`, `2118d1f`. Capability evidence pointers that an intermediate table dropped were restored at `a3cf2ef` (SCORECARD.md:2084).
- **Assimilation (§10), errno theme.** `8936643`, `e2e32de`, `a3cf2ef`. Gate in `corpus/lessons/round-37.md:5-24` and `:72-74`, with scratch evidence in `.ufo/waves/round-37/assimilation/`.
- **Wave 1 (64 seats).** Attempt 1 integrated the falsifiers at `5e270ad` and `a3cf2ef`. All three author verdicts moved to **not verified** (SCORECARD.md:2093-2101).
- **Attempt 2 re-measurement at `a3cf2ef`.** C2 counter 0 mismatches, exit 0, selftest 7/7. C3 counter 27 checked, 0 mismatches, exit 0. Census 207 rows, exit 0. Receipts are in `.ufo/waves/round-37/attempt2/`; commit `c231d0b`.
- **Attempt 2 re-check at final tip `c231d0b`** (run, not committed): C3 `checked 27, mismatches 0, PASS`; C2 `3 checked, 0 mismatches, PASS`.
- **Misroot repair.** The fleet root held `corpus/knowledge/journalctl-v262-field-filter-r36.md`, a W1 seat draft of the C2 note, probably from Build7C239 [inference]. It is preserved byte-exact at `.ufo/waves/round-37/misroot/corpus/knowledge/…` (sha256 `c65a8d41…223ac3`, `cmp` equal). The fleet copy and its empty `corpus/` directories are deleted. The draft was not placed at the note's lane path, because that would overwrite the committed C2 note with an unreviewed edit. Recorded as R37-MISROOT-NOTE-DRAFT in `corpus/lessons/round-37.md`.
- **Inherited untracked files.**
  - Reused: `.ufo/waves/round-37/after/c3-after-a3cf.json`. Attempt 2 produced an identical result; the file is committed in `c231d0b`.
  - Discarded: `.ufo/waves/round-37/w1/C32Ledger218/fixture-before/.ufo/waves/round-35/w1/ScribeC2Draft/pacman-54d9411.tar.gz`. It is byte-identical (`cmp`) to the committed round-35 original.
- **Round-36 verifier spot-check, routed items.**
  - §6.1 (probe V8): C1.
  - §6.2 (note corrections): C2.
  - §6.3 (LOG stamp `04:4043Z`): erratum at LOG.md:1391.
  - §6.4 (Gate reject sample): this round's Gate records 2 rejected staged entries and 12 quarantine verdicts.
  - No round-36 disagreement is left without a fix.
- **Planner seat.** The L1 holds the canonical §3 planner seat, because the validator rejects `planner`. The planning data-walk rode the scout and connector items.

## Landed changes

| Change | LOG.md entry | Commit(s) |
|---|---|---|
| Declaration, pre-freeze C3 correction, wave spec plus control | LOG "Round 37 — declaration" ff. | `083cd0c`, `b8ededd`, `89bb8af` |
| Self-assessment and capability table corrections | LOG round-37 entries | `d06cedb`, `ee36f9e`, `5124bf3`, `0e5f70f` |
| errno assimilation (S200-S207), quarantine gate | LOG round-37 assimilation entries, LOG.md:1427-1429 | `8936643`, `e2e32de`, `a3cf2ef` |
| C2 note corrections and counter | LOG.md:1395-1403 | `543a7ce`, `718cc8f`, `d621b71` |
| C1 V8 freeze, current assessment | LOG.md:1405 | `29b22df` |
| Measured outcomes, lesson, V7 control, C3 receipts | LOG.md:1409-1425 | `6dbfe32`, `3c456a5`, `2118d1f` |
| W1 integration after WAVE-DONE | LOG.md:1431-1435 | `5e270ad`, `a3cf2ef` |
| Attempt-2 re-verification, misroot repair, seat-count erratum | LOG.md:1437-1439 | `c231d0b` (helper: `landed c231d0bbc0aba3f9f1a08b588cd5a338d9c46e98`) |

Not mine and untouched: the operator commits `09045c5` and `f0b8f7a` (considerthese reflections).

## Before → after measurements

- **C1 (operability).**
  - Counter: `python3 tools/probe-child-env-allowlist-r37.py --revision <REV> --set livefive`.
  - Before: V7 direct livefive at `564db0b614` exits 1 with `RuntimeError: cannot create local master branch` and prints no summary (`before/v7-livefive-base.err`).
  - After: V8 at instrument tip `29b22df` over base: 5 targets, 15 pairs, `leaking=0`, `harness_errors=[]`, exit 0.
  - Kill rule fired: C17S407's V-B2 variant (ambient PATH via `shutil.which`) also reads clean, and the V8 `get_exec_path` source rule misses it (`.ufo/waves/round-37/w1/C17S407.md:15-44`). Per-fix mutant receipts were not delivered.
  - **Verdict: not verified.**
- **C2 (depth).**
  - Counter: `python3 tools/check-journalctl-v262-corrections.py --revision <REV>`.
  - Before at `564db0b614`: 15 mismatches, exit 1 (`before/c2-before.json`).
  - After at `d621b71`: 0, exit 0. Re-measured 0 at `a3cf2ef` (`attempt2/c2-at-a3cf2ef.json`) and at `c231d0b`.
  - Reviewers found two gaps. The counter does not assert the declared "rejection line stays verbatim" conjunct. The action-override case is order-dependent beyond the tested row (`w1/Review1Causal153.md:60-83`, `w1/C24ActionOverride12.md:34-80`).
  - **Verdict: not verified.**
- **C3 (calibration).**
  - Counter: `python3 tools/check-self-assessment.py --revision <REV>`.
  - Before at `564db0b614`: 27 checked, 5 mismatches, exit 1 (`before/c3-before.json`).
  - After at `29b22df`: 0, exit 0. Re-measured 0 at `a3cf2ef` and `c231d0b`.
  - The count checks K07-K11 depend on files the other claims change, so C3 is not causally separable as frozen. Its after-value moved 0 → 5 mid-round (`w1/Review1Causal153.md:13-39`, `w1/C34Ledger420.md:27-43`).
  - **Verdict: not verified.**

No ordinal moved. Every verdict above is the author's. Admission is the non-author closure's call.

## Sources & frontier

- **Census, round start** (attempt 1, `corpus/lessons/round-37.md:28`): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` gave 199 rows, 31 W04, `tsukuroi ok`, exit 0.
- **Census, round end** (attempt 2): same command gave 207 rows, 33 W04, `tsukuroi ok`, exit 0 (`.ufo/waves/round-37/attempt2/sources-census-round-end.txt`). Row count: `grep -cE '^ {0,3}\| *S[0-9]{3}' corpus/SOURCES.md` → 207.
- **Rows added:** 8 (S200-S207), all tier A, status `mined`. S206 and S207 are own-work captures. No existing row's status, recheck or used-by changed.
- **Assimilation: theme "errno discrimination"** from `merge/tsukuroi/`.
  - Admitted staged entry: `errno-contract-variance-r37.md` (S202-S207).
  - Lane-authored, source-derived note: `mount-errno-contract-r37.md` (S200-S201).
  - Rejected staged entries:
    - `errno-name-discrimination-r25.md`: duplicates admitted ground and has no QUALITY check.
    - `mount-errno-contract-r26.md`: would revive the round-12/13 CX2 `CAP_SYS_ADMIN`→`EPERM` contradiction.
  - Gate: `corpus/lessons/round-37.md:9-22` and `:72-74`.
- **Id collision check:**
  - Ids: `reg-ids` 199, `staged-ids` 147, `collisions` 0.
  - Guard proven first on an indented fixture: `assimilation/indented-fixture/collisions` = `S002`.
  - Renumbering is by document; adopted rows continue at S200 (SCORECARD.md:2080).
  - Scratch gate: `sources-census.sh validate --file …/assimilation/validate/corpus/SOURCES.md` exit 0.
- **Quarantine slice:** 12 data rows (`assimilation/quarantine-slice.txt`), each with a verdict (`assimilation/quarantine-decisions.md`): S211 and S213 refused as quoted; S225 unreachable; 9 no-locator rows unverifiable. None appended.
- **considerthese:** mined `considerthese/2026-10-23.md`, proposal "Verified-rate ledger". It was not implemented, and the reason is recorded in `corpus/lessons/round-37.md:64-66`. The newest file, `2026-10-25.md`, was not mined this round.
- **Sourced claim:** C2 rests on S199 (pinned systemd v262 NEWS), opened on 2026-10-25 (SCORECARD.md:2070-2072). C1's planned S200/S201 citation is superseded (SCORECARD.md:2045).
- **Mined mistakes** (`corpus/lessons/round-37.md` `## Mistakes` and attempt-2 Mistakes):
  - R37-STALE-SELFASSESS-COUNTS
  - R37-ROLE-TAXONOMY-MISMATCH
  - R37-C2-COUNTER-REFERENCE-DRIFT
  - R37-MISROOT-NOTE-DRAFT
  - R37-SEAT-REPORT-COUNT (62 of 64 seat reports, not 63)

## Trend verdicts

- **expansion: unchanged.** The new errno notes and S200-S207 refine snapshot/journal ground the lane already holds. The round-36 closure ruled the same way on owned ground (`corpus/lessons/round-36-verifier-spotcheck.md` §5). No new coverage-map surface is claimed.
- **quality: improved** (author-side). The C2 note now carries the routed corrections: counter 15 → 0 mismatches, selftest 7/7. The V7 direct-mode crash is gone in V8. Capability pointers dropped mid-round were restored at `a3cf2ef`. None of this certifies C1, C2 or C3.
- **discernment: improved** (author-side). The lane applied its own kill rules: all three claims are filed **not verified** on falsifier evidence. It rejected 2 of 3 staged entries with flip conditions and gave each of the 12 quarantine rows a verdict. It also corrected its own over-claims: the "3 admitted" declaration and the 63-report count. The outside spot-check is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SHONEN.md:5-6 (SKILL.md:38-50, :90-141, :2028-2036, :179-209). No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: SHONEN.md:7-8 (`corpus/knowledge/host-health-report-r3.md`, `corpus/knowledge/adjacency-handoffs-fleet-r1.md` §3). No non-author verifier.
- [~] Instructions executable by an agent without oral context. Evidence: SHONEN.md:9-10 (`corpus/knowledge/executor-test-sufficiency.md:15-20`). The whole-SKILL retest is still unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: SHONEN.md:11-12 (PROVINCE.md:44-52, :121-146). Kaidoku/revenger ownership is still unruled.

## Report extras

- **Round shape:** one v2 wave, `w1`, 64 seats. It was validated under `ufo-wave-policy-v2.json` (`w1-dispatch.json` counts: spawn 64, total 64), dispatched by the orchestrator at 2026-10-25T16:04:04 (`w1.ready.dispatched`), and WAVE-DONE was received by attempt 1.
- **Role mix:** scribe 20, executor 12, reviewer 9, critic 8, scout 5, connector 4, mutation-tester 4, revenger 2.
  - m_flash roles: 42/64 (executor and scribe alone: 32/64).
  - Attack seats (reviewer, critic, mutation-tester): 21/64, which is 33%.
- **Round total:** 64 seats. No residual call; no attempt-2 wave.
- **Dead or no-report seats:** 2 of 64. `C27N15` (mutation-tester) and `Review3Causal355` (reviewer) left no report. Their last error text cannot be recovered: `w1-results.json` holds `output: null` for all 64 rows, with the note that the orchestrator kernel restarted mid-wave. Seat answering models were likewise not retained, and no claim depends on one.
- **Validator refusal before dispatch:** `w1-invalid-role-refusal.json` (`labrat` is `unknown_role`). The item was re-planned, not split.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed two untracked fleet-root paths.
  - `corpus/` was this lane's misroot; it is repaired as described above.
  - `.ufo/waves/round-30/wave1/ScribeLesson.md` belongs to another lane's round-30 lesson (47-row registry) and was left untouched.
- **L0 questions:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none by either L1 attempt. The seat reports that mention tooling record none.
