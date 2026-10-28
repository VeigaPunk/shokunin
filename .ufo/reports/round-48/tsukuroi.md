# Tsukuroi — round 48 (attempt 2)

## Work performed

Declared claims: **C1 operability** (spaced-TMPDIR selftest fixture placement and signal cleanup), **C2 depth** (counted admission of GR1–GR3), and **C3 calibration** (zero mismatches in the fixed 27-check self-assessment). Freeze: `ae99f021b76f8eb1c8805d32d80644464afb1ff6`; base: `5fdf062f969292736e36513e39f98b1b8de43635`.

- **C1 — implementation and falsification:** removed the `/tmp` fallback for disallowed TMPDIR characters and resolves a dirty TMPDIR through an open-directory fd alias; added signal exit traps and pinning selftest cases. Counter plus pre-data battery: `tools/score-selftest-tmpdir-r48.py`, `.ufo/waves/round-48/controls/battery-summary-r48-c1.jsonl`; six C1 legs passed at frozen census blob sha256 `375aa7370f84b0ee9d4630e2cd34165c1403901e3266db603ffa43f3a76e2426` (`.ufo/waves/round-48/after/c1-final.json`). Non-author review, edge matrix, SIGINT/TERM probes, descriptor collision probes, syscall audit, live-output comparison and predecessor-gate comparison are in `.ufo/waves/round-48/w2/TRevFix.md`, `TRevPortable.md`, `TExecEdgeChars.md`, `TExecSignals.md`, `TExecFdHold.md`, `TExecStrace.md`, `TExecLiveKill.md` and `TExecAdjSelf.md`.
- **C2 — sourced depth claim and honest stop:** froze a row-binding counter with S240 `ioctl.c` digest-pinned and independently counted 18 reviewer/critic report files in the single w2 wave. Result at integration commit `76066487148483c8cc00ff4fe45f543e9e9e46c2`: `structural_ok=1, quotes_ok=3, verdicts_ok=1, marks_ok=0, FAIL` (`.ufo/waves/round-48/after/c2-final.json`). GR1 had a current-hash `partly` (R48CritGR1a), GR2 had two current-hash `partly` verdicts (R48RevGR2a, R48CritGR2a), GR3 held; the claim was not admitted and no admission marks or depth score were added. The exact dissent and proposed corrections remain in those counted reports and the other counted reports under `.ufo/waves/round-48/w2/`.
- **C3 — calibration:** corrected the current self-assessment values after the freeze exposed K10/K13/K17 (lesson files 70→71; census cases 164→166 in the axes and capability rows). At measurement commit `71493caa5cf5dce1c109b69ba526989d17723a7d`, `python3 tools/check-self-assessment.py --revision 71493caa5cf5dce1c109b69ba526989d17723a7d` returned `checked=27, mismatches=0, status=PASS` (`.ufo/waves/round-48/after/c3-final.json`).
- **Frontier / sourced evidence:** reopened S240 live (2026-10-28, sha256 `7b3488f2f83563134fec1a3d40c4149a5fe3606de6628cd33f7897fd4534ba01`, byte-identical to the pin); S251 was re-opened by SScoutProcFd; S253 POSIX.1-2024 and S255 Bash Reference Manual were admitted; S254 community Q&A was rejected with a flip condition. Registry, Gate and old→new `used-by` evidence: `corpus/SOURCES.md:249-264`, `corpus/lessons/round-48.md:12-21,33-40`. Attempt 1's `w1` was an invalid pre-freeze 32-seat dispatch, stopped by the orchestrator. Its outputs are void incident evidence only, never scored; disclosure and preserved records are `.ufo/waves/round-48/w1/INCIDENT.md` and `w1-results.json`.
- **Census and mistake handling:** start/end receipts are `.ufo/waves/round-48/before/sources-census-start.txt` and `after/sources-census-end.txt`; the exact command at each boundary was `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`, exit 0 both times. Each output contains 40 W04 duplicate-URL warnings and ends `tsukuroi ok <lane>/corpus/SOURCES.md`; the end registry has IDs through S255 (three rows appended: tiers A, C-rejected, A). Full byte outputs are in the cited committed receipts. The mined process/calibration/source/counter mistakes and fixes are in `corpus/lessons/round-48.md:23-40`.
- **Wave:** one v2 wave, `w2`, validated and handed off as one 71-seat dispatch; 16 reviewer, 14 critic, 15 executor, 15 scout, 4 mutation-tester, 2 sentinel, 2 connector, 3 scribe; 34 attack-role seats (47.9%); L1 held planner. All 71 seat reports and the settled handoff are committed under `.ufo/waves/round-48/w2/` and `.ufo/waves/round-48/w2-results.json`; no residual call. Attempt-1 w1 is excluded from these figures.
- **Curation decisions:** `Assimilation: none` (the staged shokuknow package was not adopted; source package is read-only). ScoutConsider mined the current proposal list; no proposal was implemented because the frozen claims were not to be widened.

## Landed changes

All lane changes below are tied to the Round 48 LOG entry (`LOG.md`, heading “Round 48”, lines 1688–1700); every helper result was a verified `landed` line.

- `174a2c793a1e27cd1be29b30ccddcef6507a8a89` — C1 census fix and the C1/C2 frozen counters.
- `d7843b3a433dc4892601d026d4eb98af122493ff` — IN-109 anchor repin 2593→2642; corrected C1 counter summary-line match.
- `ae99f021b76f8eb1c8805d32d80644464afb1ff6` — frozen claims, counters, controls, and disclosed void-w1 incident record.
- `23f85377433c42240aeb2e5f2ed99918a1419f0a` — validated w2 spec and dispatch (71 seats).
- `76066487148483c8cc00ff4fe45f543e9e9e46c2` — settled w2 seat reports and orchestrator results.
- `a7e2b391d159ad14107eb21389555729c414edb8` — lesson, sources curation, scorecard outcome, start/end census receipts and measured C1/C2 evidence.
- `67dfd8aa59eb2364a0b28fde4349f44ad0870d00` — scorecard self-assessment K14/K15 restatement and source-census evidence.
- `8717d8e9ecbbf776fd80b602a74218e51f7b11a8` — settled w1 void records, L1 S240 fetch, and outcome receipts.
- `71493caa5cf5dce1c109b69ba526989d17723a7d` — final claim outcome and initial zero-mismatch C3 measurement.
- `6256760d1382ce4ce20fcba830d4b2912cfbf12b` — final C3 receipt and measured outcome. `jj-lane.sh state` reported `local=remote`, `ahead=0`, `behind=0`; `git ls-remote origin refs/heads/master` returned this exact hash.

## Before → after measurements

1. **C1 operability** — Command: `python3 tools/score-selftest-tmpdir-r48.py --revision ae99f021b76f8eb1c8805d32d80644464afb1ff6` (counter reads the census blob frozen at that revision). Before: K0 base blob `adb1b4ce2325c38da2acbb815d820d3d8d6a0dd45b34796d808590c8ab32ce41` failed: `pass_ok=0, loc_ok=3, clean_ok=4, failfast_ok=1, term_ok=0, static_ok=0` (164 cases). After: frozen fix sha `375aa737…e2426`, `pass_ok=4, loc_ok=4, clean_ok=4, failfast_ok=2, term_ok=1, static_ok=1`, PASS. Commit measured: `ae99f021b76f8eb1c8805d32d80644464afb1ff6`; final reproduction receipt `.ufo/waves/round-48/after/c1-final.json`. K0/K2/K3/K4 and K-pass controls all matched expectations (5/5).
2. **C2 depth** — Command: `python3 tools/check-scrub-admission-r48.py --revision <REV>`. Before at base `5fdf062f…`: `structural_ok=1, quotes_ok=3, verdicts_ok=0, marks_ok=0, FAIL`. After at integration commit `76066487148483c8cc00ff4fe45f543e9e9e46c2`: `structural_ok=1, quotes_ok=3, verdicts_ok=1, marks_ok=0, FAIL`. Target required all three rows and all three marks; it was not met. The control battery scored 14/14 expected outcomes (`controls/battery-summary-r48-c2.jsonl`). Measured commit: `76066487148483c8cc00ff4fe45f543e9e9e46c2`.
3. **C3 calibration** — Command: `python3 tools/check-self-assessment.py --revision <REV>` (unchanged 27 checks). Before at base `5fdf062f…`: checked 27, mismatches 1 (K10); at freeze, 3 (K10/K13/K17). After at `71493caa5cf5dce1c109b69ba526989d17723a7d`: checked 27, mismatches 0, PASS. Measured commit: `71493caa5cf5dce1c109b69ba526989d17723a7d`; final receipt `.ufo/waves/round-48/after/c3-final.json`. The C3 battery scored 5/5 expected outcomes.

No axis ordinal moved; depth remained 8 and operability/calibration remained 9. The lane reports the failed C2 claim honestly rather than claiming round admission.

## Sources & frontier

- Start census: source registry IDs S001–S252. Command exit 0; receipt `.ufo/waves/round-48/before/sources-census-start.txt` (40 W04 warnings, final output `tsukuroi ok /home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md`).
- End census: IDs through S255. Same command exit 0; receipt `.ufo/waves/round-48/after/sources-census-end.txt` (40 W04 warnings and same final `ok` line). Added by tier: S253 spec/A mined and S255 docs/A mined; S254 community/C rejected and retained with reason + flip condition. Touched old→new: S240 `used-by` now includes the lesson after live 2026-10-28 re-open; S251 `used-by` now includes the lesson after a live re-open (same pinned digest). Existing S250 Bash source row was re-opened; S252 was used to assess the mktemp duplicate candidate. Frontier rows advanced: S253, S254, S255; S240/S251 rechecks recorded. `Assimilation: none`.
- The census outputs are preserved byte-for-byte in the two receipt files above; both exit codes are 0. Start/end counts and warning totals are included here so the outputs are independently locatable and reproducible.

## Trend verdicts

- **expansion — unchanged:** no new knowledge entry was admitted; source-registry curation is not corpus expansion (CORPUS rule 4). Evidence: `corpus/lessons/round-48.md` Gate; no new `corpus/knowledge/` file.
- **quality — improved:** C1 spaced-TMPDIR fixture handling now passes the frozen six-leg counter, and the live census output/exit code matched base after digit stripping (w2 `TExecLiveKill.md`). C2 depth work remains unadmitted; no false positive is claimed.
- **discernment — improved:** C2's frozen counter retains the current-hash `partly` verdicts and rejects admission; C3 remeasurement corrected 3 observed mismatches to 0. Evidence: `after/c2-final.json`, `after/c3-final.json`, controls summaries.

Stale-lane: none — respawn-per-round; no other mission is open. Tool installs/updates: none. L0 questions: none.

## SHONEN

[~] SKILL.md decision tables, error patterns, checklists, citations — author evidence: `SKILL.md:38-50,90-141,2028-2036`; non-author verification remains owed.
[~] End-to-end domain task logged — `corpus/knowledge/host-health-report-r3.md`, historical evidence in `LOG.md` round 3; this round adds no new end-to-end host task.
[~] Instructions executable without oral context — `corpus/knowledge/executor-test-sufficiency.md:15-20,106-136`; whole-current-SKILL retest remains unexecuted.
[~] No cross-domain bleed — `PROVINCE.md:44-52,75-83,121-152`; contested ownership remains routed, not absorbed.
