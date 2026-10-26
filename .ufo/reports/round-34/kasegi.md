# kasegi round 34 — report

Lane: `kasegi-shokunin` (bounty & security research, axes depth + coverage). L1: `KasegiR34a2`
(attempt 2). Attempt 1 (`KasegiR34`) died mid-work without a report (`lane-dead-no-report kasegi
round=34` at `2026-10-26T03:15:20-03:00`); this attempt inherited, re-verified and landed the same
frozen claims unchanged.

## Work performed

The round declares **two claims**, frozen by attempt 1 in
`.ufo/waves/round-34/claims.json` (claims-freeze commit `29f606d`, base `014ee2d`):

- **C1 — depth:verifiability (score 4, held):** the nine round-33 verifier-routed defects
  R1–R9 land with runnable closure checks: `corpus/instruments/r-defect-closure.sh` prints
  `closed=9/9 exit=0` and `--selftest` prints `cases=9 failures=0`; `capture-binding-check.py
  --selftest` prints `cases=23 failures=0`; `kill-rule-check.py` prints `survivors=0`;
  SCORECARD.md carries 0 `<LANE_HASH>` markers; the round-32 manifest carries only strict-UTC
  `fetched_utc`; S040-live.txt has an orphan listing; QUALITY R20 gains the per-id note and
  pre-freeze satisfiability is recorded (R22); the round-33 lesson carries the R7 erratum;
  frontier rule A is bidirectional; the junk twin is committed under `c2-controls/` and its
  fabricated sentence is rejected.
- **C2 — coverage (score 7, held):** Frontier F17 admitted 16→17 (Immunefi Vulnerability
  Severity Classification System v2.2 — Web3/smart-contract bounty severity classification),
  registry row S051 added (tier A, mined, opened 2026-10-26), knowledge entry
  `corpus/knowledge/immunefi-vscs-v2-2-smart-contract-severity.md` cites `source: S051`,
  harness prints `entries=20 pass=20 exit=0` incl. `PASS F17 … ids=S051`, `source-recheck`
  S051 exits 0, census exits 0 (W04 S028/S029 only).

Work items (all evidence under `kasegi-shokunin/.ufo/waves/round-34/`):

- **Wave** — one v2 wave `kasegi-r34-build`, 65 seats (executor 19, reviewer 13, scribe 10,
  mutation-tester 7, scout 5, critic 5, connector 3, sentinel 2, simplifier 1), dispatched by
  attempt 1 through the inline spawn handoff (`wave1.ready` → `wave1.ready.dispatched`; dispatch
  commit `206e5108`; spec `wave1-spec.json`, 65 items). Attack share 27/65 = 41.5%. Receipts in
  `wave1/`. No `wave1-results.json` exists — attempt 1 ended before the dispatcher finalized
  results; the 65 receipts are the evidence (one name-vs-file swap: `ScribeReportDraft-2.md`
  supplements `ScribeReportDraft.md`). `ExecRegressionC1.md` landed at 06:16Z, after the
  integration commit, and is committed in `c1c6a5f`.
- **C1 build + attack** — `r-defect-closure.sh` (R1–R9, selftest judge rejects forged/short
  reports; `ExecRDefectClosureSuite.md`, `MutRSuiteChecks.md` nine one-limb mutants killed
  two-sided); `capture-binding-check.py` hardened to 23 cases (per-file binding, nested dir,
  strict-UTC, dup-record, dual-https, rejected anchor, summary-only rejection;
  `ExecCaptureBindingHarden.md`, `MutManifestField.md`, `MutCaptureBindingLimbs.md`);
  `kill-rule-check.py` kills the two frozen-rule survivors plus per-file-binding-removal, with
  four controls rejected (`ExecKillRuleCheck.md`, `MutKillRuleMutants.md`, `MutSelftestSummary.md`,
  `CritOverclaim.md`); scorecard markers replaced and erratum 2 appended (`ExecScorecardMarkers.md`,
  `ExecErratum2.md`); round-32 manifest normalized (`ExecManifestR32Normalize.md`); S040 orphan
  listed (`ExecS040Orphan.md`); QUALITY/lesson errata (`ExecQualityAppends.md`,
  `ExecLessonErrata.md`); rule A bidirectional (`ExecFrontierBidirectional.md`, `MutFrontierRuleA.md`).
- **C2 build + attack** — F17 entry drafted and reviewed (`ExecRegistryAppend.md`,
  `ExecSnapshotR34.md`, `ScribeEntryF17.md`, `RevEntryF17.md` ADMIT, `RevRowS051.md`), live
  re-captures byte-identical (`ScoutImmunefiLive.md`, `CritC2Kill.md`), harness after
  (`ExecHarnessAfter.md`), junk-twin control committed and its fabricated sentence rejected
  (`ExecDoNothingReject.md`, `RevJunkTwin.md`, `RevC2BeforeAfter.md` §8; dispute on the
  as-frozen phrasing recorded in the lesson § Gate), C2 mutants killed with one documented
  anchor-window survivor (`MutC2Entry.md`).
- **Do-nothing controls** — `c1-controls/` (fake suite prints `closed=9/9 exit=0`, rejected by
  the suite judge; fake kill rule `CTL-fake-killrule` rejected `opaque differs=1`) and
  `c2-controls/` (shape checker passes the junk twin 3/3 by design; the fabricated sentence
  fails `source-recheck` against the committed capture, `MISMATCH reason=quote-not-found`, exit 1).
- **Non-claim frontier items** — assimilation id-collision guard re-run (`assimilation/`:
  reg_ids=51, staged_ids=94, collisions=21, S031..S051; guard shown load-bearing on an indented
  row), quarantine slice re-derived (7 rows: 0 adopted / 2 refused / 5 unreachable), standing
  refusals re-measured with flips unmet → **Assimilation: none adopted**; considerthese
  `2026-10-25.md` proposal 6 mined → QUALITY R23; mistakes M34-1/M34-2 (frozen) +
  M34-3/M34-5/M34-6 minted in `mistakes-erratum-1.md`.
- **L1 integration** (this attempt) — re-ran every frozen counter on the integrated bytes
  (`wave1/L1Integration.md` + `.raw`), landed the SHONEN-owed PROVINCE F17 amendment and the
  SKILL re-verify correction, synced `knowledge-expected.txt` to 46 entries, appended QUALITY
  R25, verified strays absent, committed (`4b0a9f2`), then finalized lesson + LOG (`4eafa84`,
  `c1c6a5f`).

## Landed changes

Every landing is tied to the round-34 `LOG.md` entry (commit `4eafa84`, post-entry note
`c1c6a5f`) and named commits:

| Change | Commit |
|---|---|
| Wave spec/dispatch (`wave1-spec.json`, `wave1-dispatch.json`, `wave1.ready(.dispatched)`, plan/run logs) | `206e5108` (attempt 1) |
| Claims freeze (`claims.json`, `census-before.txt`, `c1-controls/`, `c2-controls/`) | `29f606d` (attempt 1) |
| C1 instruments: `r-defect-closure.sh`, `kill-rule-check.py`, hardened `capture-binding-check.py` (892 lines, 23 cases), bidirectional `frontier-recheck-count.py` | `4b0a9f2` |
| C2: F17 entry, S051 registry row, `round-34/S051.txt` capture + manifest, README/province frontier rows | `4b0a9f2` |
| SCORECARD round-34 section (claims, erratum 1 disclosure, marker corrections), SHONEN, QUALITY R22–R25, SOURCES S051, lessons (round-33 R7 erratum, round-34), manifests (round-26/32), LOG round-34 entry | `4b0a9f2` + `4eafa84` |
| Claims erratum 1, assimilation guard outputs, mistakes erratum, L1 integration receipts, late `ExecRegressionC1.md` | `4b0a9f2` + `c1c6a5f` |
| L1 integration edits: PROVINCE F17 append, SKILL re-verify correction, `knowledge-expected.txt` 46 entries, QUALITY R25 | `4b0a9f2` |

## Before → after measurements

Measured against the integration commit `4b0a9f2` (bytes identical to the pre-commit tree; L1
re-run `wave1/L1Integration.md`; independently `wave1/ExecRegressionC1.md` at quiescent digest
`6ed34f48…`).

**C1 (depth:verifiability).** Before (base `014ee2d`, `census-before.txt`): `r-defect-closure.sh`
absent (`ls_exit=2`); `capture-binding --selftest cases=11`; skip-selftest and accept-record-without-url
mutants survive the frozen kill rule; `<LANE_HASH>`=2; round-32 `fetched_utc=2026-10-25T23:14:00-03:00` ×2;
S040-live.txt unbound; QUALITY R20 "exactly one" present; rule A one-directional; no junk twin.
After: `closed=9/9 exit=0` (base `closed=0/9 exit=1`); `--selftest cases=9 failures=0`;
`capture-binding --selftest cases=23 failures=0`, plain `records=41 bound=41 unbound=0 exit=0`
(erratum 1 reading; the frozen `40` literal was a round-33 snapshot count); `kill-rule-check`
`mutants=3 killed=3 survivors=0` + `gates=7 failed=0`; `<LANE_HASH>` count 0; strict-UTC only
(`fetched=2`, no offset); `orphans=1 orphan=S040-live.txt`; R20 per-id note + R22 pre-freeze
step recorded; R7 erratum appended; rule A bidirectional; junk twin committed and sentence
rejected. Kill rule: none of the six counting commands deviated (`ExecRegressionC1.md` §2 table).

**C2 (coverage).** Before: frontier 16, registry rows 50, S051 rows 0, entries citing S051 0,
harness `entries=19 pass=19 exit=0`, source-recheck S051 `manifest UNAVAILABLE reason=missing`
exit 2, knowledge entries 45. After: frontier 17, rows 51, S051 rows 1, entries citing S051 1,
harness `entries=20 pass=20 exit=0` incl. `PASS F17 … ids=S051`, source-recheck S051 exit 0
(18 assertions; Q9/Q17 `occurrences=2` anchored), knowledge entries 46, census exit 0 (W04
S028/S029 only). Kill rule: none triggered (junk twin does not pass source-recheck; not admitted).

## Sources & frontier

`corpus/SOURCES.md` before→after: **50 → 51 rows** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 51). Rows added by tier: **1 × A** (S051 — Immunefi VSCS v2.2, `https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/`, kind docs, scope Immunefi's own classification, anchor `S051.txt:46`/`:75`, teaches the 5-level scale + direct-theft criterion, status mined, opened 2026-10-26, recheck 90d, used-by the F17 entry). Rows touched old→new: none (append-only; the only in-place change is S051's own new row). Frontier rows advanced: **F16 → F17** (`corpus/README.md` F17 row at :361; `PROVINCE.md:75` F17 amendment). Census before→after:
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → exit 0 both
(`census-before.txt`; L1 after-run, W04 S028/S029 only). Sourced claim: C2 rests on S051 opened
this round (source-recheck exit 0, capture `round-34/S051.txt` `4fd8ed98…`, live re-opens
byte-identical 05:33/05:35/05:42Z).

Assimilation: **none** (no staged entry's flip set fully met; verdicts per row in the lesson §
Gate, `ScribeAssimilationGate.md`, `ScoutPackageThemes.md`). Id-collision guard run with the
0–3-space pattern: `collisions=21` (S031..S051) — adoption is by document, never by number.
Quarantine slice: 7 rows re-derived, 0 adopted / 2 refused / 5 unreachable.

## Trend verdicts

- **expansion: `improved`** — one admitted knowledge entry (F17) on coverage-map ground the lane
  did not hold, `source:` citing the mined tier-A row S051 opened this round; frontier 16→17;
  capability table unchanged (no new capability row this round; instruments were deepened, not
  new repertoire).
- **quality: `improved`** — nine verifier-routed defects R1–R9 each gained a runnable,
  fail-closed closure check (`closed=9/9`; suite selftest 9/9; capture-binding 23/23; kill-rule
  3/3 with 4 controls rejected); the two frozen-rule survivors are killed; `recheck-audit.py`
  `strict pass=46/46`; no admitted entry failed a re-check (S051 re-opened live, byte-identical);
  stale re-verify pins corrected (SKILL.md:1091, manifests, expected list).
- **discernment: `improved`** — the round-33 verifier's R1–R9 routed defects were all landed
  and are closed by the suite (the gate agreed with the outside spot-check on the routed set);
  M34-1 (overstatement) and M34-2 (marker drift) became lesson-backed criteria/R24 rows; M34-3
  grounded a new criterion (R25); the junk-twin dispute is recorded with both readings, not
  adjudicated by the lane.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SHONEN.md:5` (density 201.2/201.7, anchorcheck 0 bad, 12 in-range; SKILL.md:1091 correction
  applied; box 1 `[~]`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:21`
  (no new domain task this round; closest executed measurement is the capture-binding check
  41/41 + 23-case selftest; box stays `[~]`).
- [~] Instructions executable by an agent without oral context — `SHONEN.md:34` (F17 entry
  `recheck:` command runs; `recheck-audit.py` `strict pass=46/46`, `expect=present expected=46
  missing=0 unexpected=0 exit=0` now clean).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:54` (PROVINCE untouched
  except the F17 frontier append at :75; sibling sweep no contested scope; box stays `[~]`).

## Stale-lane

Attempt 1 launched `2026-10-26T02:24:07-03:00`, terminated `03:15:20` without a report; attempt 2
launched `03:15:22`, inherited the wave outputs, re-verified and landed — progressing throughout
(commits `4b0a9f2`, `4eafa84`, `c1c6a5f`).

## Tools installed

None. No tool installed or upgraded this round; pacman untouched (paused host-wide per the
guard).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at round end: the only untracked fleet
file is `.ufo/state/disk-guard.log` (driver-owned; untouched). The attempt-1 seat strays
(`baseline-plain.txt` fleet root, `selftest-baseline.txt` lane root) were already absent at
integration (M34-6 fix verified); the `CritC1Kill` fleet-root receipt stray was self-reported,
byte-copied into the lane and deleted in attempt 1. No fleet-root deletion was needed this
attempt.

## L0

`kasegi | round-32 |` (re-dispatch vs L1-only landing) remains open; not blocking this round.
No new L0 question filed.
