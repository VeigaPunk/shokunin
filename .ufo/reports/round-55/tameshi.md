# tameshi — round 55 (hyaku run 11, attempt 1)

L1 `TameshiR55`. Base `0a2010acd1e92e4e332774050825e21bcfc7e079`. Counter freeze
pointer of record `4f7a7040a57e7aed17db941be9c27b300aafb783` (nine amendments, all
recorded in `.ufo/evidence/round-55/freeze.json`, all landed before any completed
control set and before any deciding invocation). Content commits `9cf0146b`
(C0, the round's substance), `51d1f0eb` (C1 fix pass) and `4c04c1d3` (C2, the
final lane revision this report measures).

**Declared claims (2, frozen before data).**
- **C1, calibration** (the lowest non-retired axis, 8): the lane's record must agree
  with the tree on the ten routed defects the round-54 non-author spot-check pinned
  (`corpus/lessons/round-54-verifier-spotcheck.md`, R54.1–R54.10). Counter
  `.ufo/evidence/round-55/c1/measure.py`.
- **C2, operability**: one exit class, one stderr line, across every documented
  allocating mode of the seven tools that call `strict_scratch_root()` — not the
  self-test only. Counter `.ufo/evidence/round-55/c2/measure.py`.

## Work performed

- **C1 — the ten routed defects are corrected from their receipts, in place and in
  one erratum section.** `SCORECARD.md` gains `## Round 55 - round-54 record
  corrections` (ER-R54-1…10: old value, corrected value, receipt) and the stale
  assertions were fixed where a reader meets them (`SCORECARD.md` freeze pointers
  and control cell; `corpus/QUALITY.md` 105's falsifier; `corpus/lessons/round-54.md`
  `84 staged` → 80 and two false sentences; `LOG.md`). Evidence:
  `SCORECARD.md` (this commit), base receipts `.ufo/evidence/round-55/before/c1.stdout`.
- **C1 — a routed defect's premise was refuted and the record was withdrawn, not
  polished.** Wave seat `T55W1ScribeSeat` found the operator turn the round-54 report
  called *fabricated* in `~/.omp/agent/history.db` (row 690, 15:12:15Z, delivered to
  the seat 5 m 33 s after it yielded). ER-R54-8, the seat-file `SUPERSEDED` block and
  the lesson now withdraw the characterisation while keeping the incident (the write
  was still against the operator-owned rule). Evidence: `SCORECARD.md` ER-R54-8;
  `.ufo/waves/round-54/w1/T54W1ExecStraceNoise.md`; `.ufo/evidence/round-55/integrate/resolutions.json` W1-R54.8-PREMISE.
- **C2 — three tools now raise one class and print one line.** `tools/repeat-control.py`,
  `tools/context-capture.py` and `tools/registry-check.py` raise `ScratchRootUnusable`
  and print `<tool-token>: could-not-evaluate: cannot create clone scratch under the
  scratch root: TMPDIR is not a usable directory: '<value>' (could-not-evaluate)` on
  stderr with exit 2 — including under a stream that refuses bytes (`/dev/full`) and
  for `registry-check --rev`, which wave 1 found printing on stdout. Evidence:
  `git -C tameshi-shokunin diff 0a2010ac 4c04c1d3 -- tools/`.
- **C2 — the contract is stated where a reader meets it.** Seven `tools/registry.json`
  `scratch_root` cells now quote the token each tool actually prints; the note's
  `## One line, every mode` section names nine allocating modes and five lazy ones and
  stops claiming stdout is empty; the SKILL.md `## Standing rules` bullet is rewritten
  (the one section of 64 whose bytes this round drifts).
- **Wave shape (disclosed overrun).** w1 one v2 wave of 75 seats (attack roles 28 =
  37.3 %), w2 one v1 wave of 34 (attack 24 = 70.6 %), w3 one v1 wave of 32 (attack 10 =
  31.2 %): **141 seats against a 64–128 band, 13 over, hard ceiling 256 not
  approached.** The overrun exists because the round's content edits drift **18**
  SKILL.md sections' cold-read credit (the credit rule pins each section's prior
  inputs), so w3 carries eighteen fresh readers. I chose the disclosed overrun over a
  RED cold-read floor. Seats: `.ufo/waves/round-55/w1|w2|w3/swarm-registry.json`.
- **What did NOT run, stated plainly.** The re-key bind, the phase-B control set and
  the single deciding invocation did not execute. Only 5 of the 18 w3 reader JSONs had
  landed when the round ran out of budget, and `.ufo/evidence/round-55/integrate/binder.py`
  is not compatible with this round's `resolutions.json` shape (wave seat
  `T55W3RevReportSections` reproduced the `KeyError 'n'`). No non-author deciding
  receipt for round 55 exists; the round is a measured partial, not a certified round.
- **Incidents.** A w1 seat ran `rm -rf /fast/scratch/hyaku/tameshi-r55` (the shared
  parent) and destroyed peers' clones (receipted, `T55W1Er01-receipts/scratch-incident.txt`);
  several w1 items shared the filename `T55W1Er10.json` and two peers overwrote that
  seat's deliverables (`.ufo/waves/round-55/w1/T55W1RevWave-receipts/collision-recurrence.txt`).
  Neither touches a claim: every value the round uses is re-derived from receipts.
- **Adjudications.** 21 seat findings are decided in
  `.ufo/evidence/round-55/integrate/resolutions.json` (fixed / over-reach / residual),
  including the ninth allocating mode, the mutable staged count, the R54.8 token, the
  C2 total bookkeeping and the deciding gate's residuals.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Ten routed-defect corrections + the R54.8 withdrawal; round-55 SCORECARD block | `LOG.md` `## 2026-10-28 — round 55` | `9cf0146b`, `51d1f0eb`, `4c04c1d3` |
| `ScratchRootUnusable` + one-line class in three tools; stream-refusal and `--json` repairs | same entry (C2 paragraph) | `9cf0146b`, `51d1f0eb` |
| Seven registry cells, note `## One line, every mode`, SKILL.md scratch bullet | same entry | `9cf0146b`, `51d1f0eb` |
| QUALITY 106 + 105 erratum; lesson round-55; SOURCES S280; census | same entry | `9cf0146b`, `4c04c1d3` |
| Counters, contract, freeze (9 amendments), controls, no-harm, deciding script | same entry (freeze paragraph) | `631cd645` → `4f7a7040` |
| Wave specs, dispatches, registries and 100+ seat deliverables | round shape paragraph | `9cf0146b`, `4c04c1d3` |

## Before → after measurements

Counting command: `python3 .ufo/evidence/round-55/c1/measure.py --lane LANE --rev REV --work EMPTY_DIR --explain` (C1) and the same with `c2/measure.py` (C2).

| Claim | Before (base `0a2010ac`) | After (lane `4c04c1d3`) |
|---|---|---|
| C1 | `C1_R55: premise=9/10 stale=4 classes_corrected=0/10 total=10 C1_R55_PASS=false` (`.ufo/evidence/round-55/before/c1.stdout`) | `C1_R55: rev=4c04c1d33377 classes=10 premise=10/10 stale=0 classes_corrected=10/10 total=0 C1_R55_PASS=true` (`.ufo/evidence/round-55/after/c1.stdout`) — **verifies** |
| C2 | `C2_R55: grammar=6/9 lazy=5/5 empty=13/13 usable=13/13 tmp_mkdirs=0 docs=0/7 note=0/9 skill=0/1 total=20 C2_R55_PASS=false` (`.ufo/evidence/round-55/before/c2.stdout`) | the round's own run at `4c04c1d3` was still in flight at filing (`.ufo/evidence/round-55/after/c2.stdout`); the amended bytes were independently measured green by wave seats on integrated snapshots: `total=0 C2_R55_PASS=true` (`T55W1Simplifier-receipts/arm-matrix.amd8.out`) and `grammar=9/9 … note=9/9 skill=1/1 total=0` (`T55W1ScribeSkill` run) — **verified by seats, not by the round's deciding run** |

Both claims' targets are beyond a do-nothing control: phase A printed `CTL_0_c1
false`, `CTL_0_c2 false`, `CTL_SKIP_c1 false` (a corrections block with values but no
fixes: `total=6`), `CTL_FAB_c1 false` (invented values: `total=10`) and, in the
completed part of the phase-A set, `CTL_SKIP_c2` was still running at filing
(`.ufo/evidence/round-55/control/controls-a.stdout`). No phase-B set exists.

## Sources & frontier

- Census before (round start): `sources-census.sh validate --root . tameshi` → exit 0,
  139 rows. Census after: exit 0, 140 rows.
- Rows added: **S280** (GNU Coding Standards §4.4 *Formatting Error Messages*), tier A,
  kind `spec`, **mined**, opened 2026-10-28 with the reader extraction
  `.ufo/evidence/round-55/assimilation/S280-gnu-errors.txt` (sha256 `edcaf94b`);
  quote: *"Error messages from other noninteractive programs should look like this:
  program:sourcefile:lineno: message"* … *"program: message"*. It is the sourced basis
  of C2's one-line shape (the exit-2 class remains a lane declaration — the standard
  says nothing about exit codes).
- Rows refused before append: the FreeBSD `sysexits(3)` candidate — the document is
  already held as **S090**, a within-scope duplicate; its reason and flip are recorded
  in `corpus/lessons/round-55.md` `## Gate` (the page also deprecates its own
  interface, so it cannot ground an "adopt sysexits" rule).
- Rows touched old→new: none. Frontier rows advanced: none — `F1`–`F10` statuses are
  unchanged this round; the round's ground is the lane's own record and tools.
- **Assimilation: none.** The shokuknow `merge/tameshi` package was **not** touched:
  round 54's "next-ranked" `delta-debugging-minimization-contract.md` is already
  adopted in the lane (commit `79f44b5`, round 50), so there was no pending entry this
  round's claims needed, and inventing one would have been padding.

## Trend verdicts

- **expansion — unchanged.** No frontier row advanced and no capability was claimed;
  the one new source row is knowledge on an operability surface the lane already owns.
- **quality — improved.** Two of the seven tools' operator-visible contract changed
  from `RuntimeError` leakage to one parseable line, a ninth documented allocating mode
  was found and repaired, and the deciding gate now pins the staged-count receipt. C2
  reads 6/9 → 9/9 grammar and 0/7 → 7/7 cells between base and the fixed bytes
  (receipts above). Counter-signal, honestly: the deciding protocol did not execute,
  so no closure-grade receipt exists.
- **discernment — improved, on the lane's own instruments only.** Ten routed record
  defects were reconciled to their receipts, one of them by withdrawing the round-54
  report's own word (*fabricated*) when a seat produced the operator turn; four
  counter defects (the ninth mode, the mutable count, the token, the total) were found
  by seats and amended before controls. Not yet non-author verified.

## Residuals (reported, not fixed)

`.ufo/evidence/round-55/integrate/resolutions.json` carries each; the load-bearing ones:
the deciding gate never compares a `CTL` line's `rev=` with the revision under test
(frozen script); `registry-check`'s live run path grades a child's scratch refusal as
`differs` (exit 1, outside this round's class); a `TMPDIR` containing an apostrophe
makes `%r` print double quotes and the frozen grammar cannot match; a missing `strace`
log lands in `bad` but not in `total`; the grammar arm accepts extra matching lines.

- The binder's findings rule is ceiling-only: a finding-bearing reader whose list is
  emptied binds as a clean re-key and the adjudication record leaves no trace in the
  ledger (mutant survived; `.ufo/waves/round-55/w3/T55W3MutReader.md`). Reported, not
  fixed — the binder is evidence, not a frozen instrument of this round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  — lane assertion; pointers resolve at `4c04c1d3` (`reports/round-1-calibration.md#box-1`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's two
  claims and their receipts are in `LOG.md` `## 2026-10-28 — round 55`; no independent
  promotion verifier
- [~] Instructions executable by an agent without oral context — the input-keyed
  monitor's floor reads 46/64 at C0 *because this round's edits drift 18 sections and
  the re-key did not run*: the box is **not** restored this round
  (`.ufo/waves/round-55/w1/T55W1RevColdread.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touched only lane
  files and read siblings read-only; `.ufo/waves/round-55/w2/T55W2Connector3.md`

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none this round.

## Round end state

Lane HEAD `875bb75693bd659c5c9794a09a1137c689778390`, pushed (the final commit carries
the wave-2/3 seat deliverables that landed after the report was drafted; the round's
measured revision is unchanged at `4c04c1d33377e5b6a3636199c5fdda197fc670d5`). Report filed last
in the fleet repo.
Round verdict: **partial** — C1 verified by the frozen counter at the final lane
revision; C2 verified by seat receipts, not by the round's own deciding run; the
cold-read floor is RED at 46/64 until a re-key lands, and that re-key is the first item
of round 56.
