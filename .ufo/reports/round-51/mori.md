# mori — round 51 report (attempt 1, L1 MoriR51)

Lane `mori-shokunin`, branch `master`. Entering tip `aa3af1ec3118ee7766dfce1d9709ce3c0c3f6bfd`; freeze `4677910e`;
data `87e0c374`; wave spec `b504cb17`; integration `7c0b6232`, `70e68cdd` (measured revision); receipts `a5087527`;
final lane tip `8e3df7e562e8051cf9074f76520fd02404793a23` (SHONEN pointer; `git ls-remote origin refs/heads/master`
prints it).

## Work performed

Declared claims (frozen at `4677910e`, `.ufo/waves/round-51/contract.md`): **C1 — operability**: a `--rev` pin
re-execution by `tools/mori-pin-check.py` leaves nothing in the repo it reads when it is killed, holds with the lane
path hidden, and classes every mismatch `env` or `stale` (routed defect 1 of the round-50 spot-check;
`considerthese/2026-10-26.md` suggestion 1). **C2 — depth** (a lowest axis, tied at 5): what `/proc/meminfo`'s
`MemAvailable` is at kernel v7.2. The entry is `corpus/knowledge/memavailable-estimate-r51.md`, with rows S492–S496.
C2 adds an entailment arm: every claim row needs a vote from a wave seat that is not the L1 (routed defect 4). No
exploratory claim and no capability row.

- Census at round start: rc 0, 22 W04 (`.ufo/waves/round-51/evidence/census-start.txt`).
- Five source copies were fetched and pinned by sha256 (`corpus/evidence/sources-r51/`). Sweep at `aa3af1ec`:
  `si_mem_available`, `totalreserve`, `wmark_low`, `folio_is_file_lru`, `34e431b0` and `show_mem.c` have 0 hits.
  `merge/mori/` has nothing on MemAvailable (`evidence/sweep-memavailable.txt`).
- Freeze `4677910e`, before any seat ran: both counters, six C1 controls (do-nothing, scratch-only, conform-only,
  class-only, always-env, witness) and their receipts (`evidence/freeze-sha256.txt`, 21 files). The relocation
  witness showed why the export had sat inside the repo: three pinned instruments read git objects, and `master`,
  from the tree they run in (`evidence/control-c1-scratch-only.txt`: `reloc_mismatch=3`).
- Data `87e0c374`:
  - pin-check v5: it measures a shared clone placed under scratch and tags each mismatch `class=env` or `class=stale`;
  - `conform.py` takes its lane path from its own location;
  - SKILL and SHONEN pins;
  - the entry and rows S492–S496.

  At the data commit C1 is met (`evidence/c1-at-data.txt`). C2 fails only on `failed=entailment`
  (`evidence/c2-at-data.txt`).
- Wave `w1`: 68 seats, policy v2, validated rc 0. It covered entailment votes (7 reviewer and 4 critic seats, two
  votes per row), attacks on both claims and frontier drafting. Reports are in `.ufo/waves/round-51/w1/`, results in
  `w1-results.json`.
- Integration (`7c0b6232`, `70e68cdd`):
  - rows 6, 12, 14 and 15 now carry the replacement text that the voting seat wrote and voted `entailed`;
  - prose fixes:
    - only the census prints `MemAvailable/MemTotal`;
    - not every meminfo line is in kB;
    - the input changes from 2014 to v7.2 are listed with dates;
    - the entry says what a host recomputation needs;
    - the tsukuroi boundary is corrected;
  - pin-check v5.1:
    - the default scratch is `$TMPDIR` if it lies outside the repo, else `/var/tmp` (v5 put a ~330 MB tree in `/tmp`);
    - a `--scratch` inside the repo exits 2;
    - the tree's `master` is set to the measured revision;
    - four class corrections;
    - selftest grows from 119 to 125;
  - lesson `corpus/lessons/round-51.md`, QUALITY 137–140, the README round-51 block and SKILL `## Round51`;
  - the SCORECARD Axes cells for depth and calibration now lead with the round-50 closure;
  - LOG and SCORECARD round 51.
- Vote audit (`evidence/entail-voters.txt`): every vote line is listed with its file. No file outside the 11
  ENTAILMENT seats carries a vote line. Report hashes at WAVE-DONE are in
  `evidence/w1-reports-sha256-at-wave-done.txt`.
- Seats that ran pre-fix instruments left residue in the lane. It was deleted (`evidence/w1-lane-residue-deletion.txt`).
- Planner seat: held by the L1, because the validator rejects `planner`.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `4677910eae6df3dabd38fe9a0daf1945146a1110` | freeze: contract, counters, controls with witness bytes, receipts, source copies | Round 51 header |
| `87e0c374537557754bf71dd68036ded3ddc6699c` | data: pin-check v5, `conform.py`, SKILL/SHONEN pins, entry, S492–S496 | Round 51 C1/C2 bullets |
| `b504cb1701568a0038aab9d98ec13d28eff801da` | wave spec and dispatch, at-data receipts | Round 51 header |
| `7c0b6232fcc567eaadfaed60ad94cce3e5fd20bd` | integration 1: entry rows and prose, v5.1, SKILL Round51, QUALITY 137–140, README, lesson, Axes cells, the reports on disk at that point | Round 51 C1/C2, Frontier |
| `70e68cdd28c44a95039b9175a947e15664618351` | integration 2: all 68 reports, results file, LOG/SCORECARD round 51, SHONEN pointers, lesson additions, vote-audit and residue receipts | Round 51 (`LOG.md:2765-2805`) |
| `a50875278f3d57ba44d6b02fc37e77f9409dcc5f` | receipts at `70e68cdd`: `c1-at-landed.txt`, `c2-at-landed.txt`, `census-end.txt` | Round 51 C1/C2 bullets |
| `8e3df7e562e8051cf9074f76520fd02404793a23` | SHONEN's LOG pointer now spans the whole entry | Round 51 |

## Before → after measurements

- **C1**: `python3 .ufo/waves/round-51/count-c1.py R [--scratch DIR]`.
  - Before (`aa3af1ec`): `C1=unmet kill_residue=12547 relocated=unmet reloc_mismatch=1 classified=bad
    selftest=pass=114,fail=0 failed=kill_residue,relocated,classified`, exit 1 (`evidence/control-c1-do-nothing.txt`).
  - After (`70e68cdd`): `C1=met kill_residue=0 relocated=met reloc_mismatch=0 classified=ok selftest=pass=125,fail=0
    failed=-`, exit 0 (`evidence/c1-at-landed.txt`; also met at `87e0c374` and `7c0b6232`).
  - Controls (before data): all five non-witness controls are unmet. During the met run's arm B, the relocated registry
    run printed `PIN_CHECK=met tally_pins=36 … env=0 stale=0`.
- **C2**: `python3 .ufo/waves/round-51/count-c2.py R`.
  - Before (`aa3af1ec`): `C2=unmet claims=0 … pins=bad … failed=entry_absent,pins`, exit 1
    (`evidence/control-c2-do-nothing.txt`). At data: `failed=entailment`.
  - After (`70e68cdd`): `C2=met claims=21 located=21 quote_missing=0 bad_rows=0 sources=5 source_rows=ok pins=ok
    provenance=ok entailed=21 dissent=0`, exit 0 (`evidence/c2-at-landed.txt`).
  - Selftest: `C2_SELFTEST pass=34 fail=0`.
- Named limits. The counters are frozen; the details are in the lesson section `## Wave w1 — integrated findings`.
  - C1: arm A kills at only one moment and runs the revision's code without a sandbox. Arm B checks only the exit code
    and the last line. Arm D parses the printed tally. No control isolates a single arm: 7 of 9 single-arm mutants keep
    every control verdict.
  - C2: any `.md` not named `MoriR51*` can vote, lines inside fences count, and one vote per row is enough. Rows 6, 12,
    14 and 15 carry one vote each, from the seat that wrote the replacement. A vote records a seat's judgment; it does
    not prove the claim.

## Sources & frontier

- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0, 22 W04
  (`evidence/census-start.txt`); end rc 0, 23 W04 (`evidence/census-end.txt`). The new W04 is S492, which shares
  S082's URL at a different scope.
- Rows: `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,}'` goes from 264 to 269. All five new
  rows are tier A (S492 docs, S493–S496 code), status `mined`, opened 2026-10-26, with Gate quotes in
  `corpus/lessons/round-51.md`.
- Rows touched old→new: the S492 scope wording (an in-round row; logged in the Gate).
- Frontier: the entry covers resource-runway ground the coverage map did not hold (README round-51 block); FR8 stays
  open.
- Sourced claim: C2 rests on S492–S496.
- Mistakes mined (lesson `## Mistakes`):
  - M1: hidden location dependence;
  - M2: the round-50 residue producers;
  - M3: two seat reports misrooted to the fleet root.
- Assimilation: none. `merge/mori/` holds no staged entry or row on MemAvailable (`evidence/sweep-memavailable.txt`).
- considerthese: `considerthese/2026-10-26.md` suggestion 1 (env versus stale) is implemented in C1 (arm C).

## Trend verdicts

- **expansion: improved.** One entry on resource-runway ground the lane did not hold: the sweep found 0 hits for the
  formula's terms. Five mined tier-A rows.
- **quality: improved.**
  - Pin re-execution no longer writes into the repo it reads, and it holds with the lane path hidden (C1 before and
    after).
  - Every row of the depth claim carries a recorded entailment vote.
  - Votes caught four overclaims, and the rows were replaced before landing.
- **discernment: unprovable-but-better.** The entailment arm and the Gate's admit and reject decisions (S082 not
  widened; a non-primary blog refused) are left for the non-author closure to judge.

## SHONEN

[~] SKILL.md decision tables, error patterns, checklists with sources — `SKILL.md:1069-1141` (Round51: runway decision row, pin mismatch classes); `corpus/QUALITY.md:1252-1352`
[~] an end-to-end domain task executed and logged — `LOG.md:2765-2805` (Round 51); `.ufo/waves/round-51/evidence/c2-at-landed.txt`
[~] instructions executable without oral context — `python3 tools/mori-pin-check.py --selftest` (125/125); `python3 tools/mori-unlanded-check.py --selftest` (17/17); receipts `.ufo/waves/round-51/evidence/selftests/`
[~] no cross-domain bleed — `corpus/knowledge/memavailable-estimate-r51.md` Boundaries (OS state is tsukuroi's to diagnose and the operator's to change); `.ufo/waves/round-51/w1/Mo51ConnSiblings.md` (tsukuroi adjoins; its `kill-oom-boundary-r33.md:30` should re-read its Shmem cell)

## Extras and defects

- Round shape: one v2 wave `w1` of 68 seats.
  - Roles: executor 18, reviewer 14, critic 12, scribe 9, sentinel 4, mutation-tester 3, connector 3, scout 2,
    simplifier 2, revenger 1.
  - m_flash roles 34/68; attack roles 29/68.
  - All 68 seats settled with a report and an output in `w1-results.json`. Dead seats: 0.
  - No residual call. Round total: 68.
- Misroots: two seat reports (`Mo51CritEntail12.md`, `Mo51ConnSiblings.md`) were written at the fleet root. The
  orchestrator moved them into the lane at 19:52 -03 with their bytes unchanged (lesson M3). The final sweep
  (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) shows no mori file at the fleet root. Seat scratch
  `/fast/scratch/hyaku/mori-r51` was removed. One seat, `Mo51CritContractFreeze`, had left a `tmp/` directory there,
  which counts as that seat's defect.
- Round-50 routed defects:
  - 1 → C1;
  - 2 → one v2 wave, 68 seats;
  - 3 (successor calibration counter, K4 beyond SHONEN) not done; routed to round 52 and named as a deviation in
    LOG.md;
  - 4 → the entailment arm;
  - 5 → the deviations are named in LOG.md;
  - 6 → the operator's.
- Round-40 freeze: `conform.py` no longer matches `round-40/evidence/freeze-r40.txt` (`5025b966…` → `7f5174d5…`).
  Round-40 receipts are still measured with the frozen bytes (see the lesson and LOG).
- Notes for the operator (fleet-owned files; mori did not edit them):
  - `scripts/hyaku/inline-dispatcher.py:133` fails open when `/proc/meminfo` is unreadable.
  - Its `MEM_MIN_GB` is actually in GiB.
  - The two hyaku gates hold different floors on the same line: 4 GiB and 6144 MiB.

  Details: `.ufo/waves/round-51/w1/Mo51ExecDispatcherGate.md`.
- Stale-lane: respawn-per-round driver; no other mori mission is open.
- Tool installs: none (the L1 installed nothing, and every seat report that mentions tooling says nothing was
  installed).
- Open L0 questions: none.
