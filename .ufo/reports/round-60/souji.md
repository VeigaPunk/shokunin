# souji round 60 — freeze-record substance binding (C1) and atomic receipt writing (C2)

Lane: `souji-shokunin` (`/home/vgpnk/Projects/shokunin/souji-shokunin`). Round 60, attempt 1.
Base `1e8bfd87a9f6ea9a1db4ad34f6e4cdd2b218bcd4`; lane tip `d05a00019835dee5b9bb8fe738add080434c4d67`
(`git ls-remote origin refs/heads/master` prints it). Axes owned: calibration, operability, coverage.

Fresh start honoured: the retained rejected closures of r56 (`8c27791a`), r57 (`dcbcd05c`) and r58
(`87430107`) and the rejected r59 (`24a07fd8`) were read with their non-author spot-checks before any
claim was declared. No rejected claim is re-declared: this round lands no visibility-parser repair, no
receipt *gate* and no registry-classification repair. Both claims were frozen only after their no-work
controls were executed and committed, and the base values in the frozen predicate are the measured ones.

## Work performed

**Declared claims (2, causally separable, distinct axes):**

- **C1 — calibration (7, lowest owned axis; claim type: capability acquisition).** The freeze checker
  `tools/souji-freeze-check.py` gains an opt-in `--substance` arm that binds each claim's `Control:`
  receipt to (a) the declared `Counter:` path, (b) that counter's committed blob digest at the freeze
  commit, (c) a full-40 revision that `git merge-base --is-ancestor` reports as a strict ancestor of the
  freeze commit, and (d) a `command=` that names the counter as an argv token. Without the flag the
  tool's stdout, stderr and exit are byte-identical to base bytes.
- **C2 — operability (8; successor to the rejected r57 C2 on a different surface — writing, not
  checking).** `tools/souji-receipt-write.py` publishes a receipt through a same-directory temp file,
  `fsync` and `link(2)`, and refuses an existing or racing output, a dirty worktree, an over-bound
  capture, a short or non-commit revision, an instrument absent at the revision, and an out directory
  that resolves outside the lane root.

**Work items (each with its evidence pointer):**

- Freeze checker substance arm delivered by `S60ExecFreezeArm`; integrated as
  `tools/souji-freeze-check.py`; default path byte-identical over the selftest and three real
  preregistrations (`census/round-60/wave/w1/S60ExecFreezeArm/byte-identical.txt`), `--selftest`
  `cases=41 pass=41`, `--selftest --substance` `cases=12 pass=12`.
- Frozen 8-case matrix + runner delivered by `S60ExecMatrix`, integrated as
  `census/round-60/c1-matrix.tsv`, `census/round-60/matrix/`, `census/round-60/build-matrix.py`,
  `census/round-60/c1-counter.py`; the counter rebuilds each case repo in scratch and re-checks its
  pinned ancestor/freeze hashes (`census/round-60/wave/w1/S60ExecMatrix/base-run.txt`).
- Receipt writer delivered by `S60ExecRecorder` (`tools/souji-receipt-write.py`, `--selftest`
  `cases=12 pass=12`) and its 8-case fixture by `S60ExecRecorderFix`
  (`tests/fixtures/r60-receipt-write.py`).
- Pre-freeze controls delivered by `S60ExecControls`
  (`census/round-60/wave/w1/S60ExecControls/{do-nothing,positive,forgery}-c{1,2}.txt`), then re-executed
  by the L1 through the new writer so the frozen `Control:` receipts are themselves bound:
  `census/round-60/controls/c1-do-nothing.txt` (`new_forgeries=5`, `EXIT=1`) and
  `census/round-60/controls/c2-do-nothing.txt` (`pass=4 fail=4`, `EXIT=1`), both at
  `3b5525099356e15ff9d17b7fbd2835c2d3512eee`.
- Sources opened and drafted by `S60ScoutSources`; the L1 re-opened every cited page and wrote the
  rows: `corpus/SOURCES.md` S288 (admit) and S289 (reject); S110/S213/S214/S251 re-opened with cells
  unchanged; captures and digests in `census/round-60/sources/`.
- Knowledge entry `corpus/knowledge/freeze-record-substance-binding.md` (F1) — decision table of the
  five forgery classes against the label-only grammar, and what the binding still cannot prove.
  `S60ScribeEntry`'s second draft (`atomic-receipt-write.md`) was refused as duplicate F4 ground; the
  refusal is recorded in the lesson.
- Attacks: `S60ReviewerFreeze` (11 probes, incl. kind-only, cross-claim copy, rename-identical decoy,
  fenced/indented decoys, duplicate revs, tag revision), `S60ReviewerRecorder` (18 attacks, incl. two
  TOCTOU racers, symlinked out dir, SIGKILL/SIGTERM residue, bound bypass, dirty-tree bypasses),
  `S60CriticRound` (12 findings against Q99/Q100/Q102/Q120), `S60MutMutation` (15 mutants),
  `S60SentinelRound` (out-escape, dirty bypass, git-env probes), `S60ConnectorRound` (sibling overlap),
  `S60ScoutFrontier` (frontier, census, mistake sweep, package presence).
- Six pre-freeze repairs driven by those attacks (recorded as SCORECARD round-60 amendments 1–3):
  counter summary prints both arms; conflicting duplicate binding lines refused; command matched as an
  argv token; publish switched from `os.replace` to `link(2)` (TOCTOU); out directory confined to the
  lane root (`--allow-outside` opt-out); `rev` must name a commit object (tag OID refused); stale
  `<out>.*.tmp` swept on the next write.
- Frozen predicate `census/round-60/preregistration.txt` (commit
  `2670e96af1b81c7aa793acc34d40361b4beecff8`), including the critic's mandatory correction: C2's base is
  the measured `pass=4`, not the `3/8` the wave prompt assumed.
- The round's own freeze record under the arm it lands:
  `tools/souji-freeze-check.py --substance --prereg census/round-60/preregistration.txt --rev 2670e96a`
  → `SUMMARY claims=2 findings=0`, exit 0.
- Round-end census: `scripts/sources-census.sh validate --root … souji` exit 0
  (`census/round-60/records/sources-after.txt`), registry rows 211 → 213.

## Landed changes

| commit | carries | LOG entry |
|---|---|---|
| `3b5525099356e15ff9d17b7fbd2835c2d3512eee` | substance arm, receipt writer, 8-case fixture, C1 matrix + counter, C2 population, source captures, S288/S289, knowledge entry, lesson skeleton | LOG.md `## Round 60` bullets 1–2 |
| `2670e96af1b81c7aa793acc34d40361b4beecff8` | frozen predicate + the two bound red controls | LOG.md bullet 2 (freeze hash) |
| `b38c60ee400954dd6d79c5f9052cb8994939bad6` | SCORECARD round-60 measurements + two capability rows, LOG entry, SKILL rows for both instruments, final lesson, durable wave evidence `census/round-60/wave/` + `wave-SHA256SUMS` | LOG.md `## Round 60` bullets 3–6 |
| `e51dc9d88de762ca783ecc22659c04ad2f0a9ffa` | `used-by` separator fix in S288, round-end census receipt, census section in the lesson | LOG.md `## Round 60` curation bullet |
| `2ec7f4607a5eaf89af0db7405c53f1be217f3901` | refused duplicate knowledge draft recorded in the lesson | LOG.md `## Round 60` curation bullet |
| `d05a00019835dee5b9bb8fe738add080434c4d67` | settled wave results and final seat reports (`census/round-60/wave/`, `wave-SHA256SUMS` 365 rows) | LOG.md `## Round 60` wave bullet |

Every one of these is on `origin/master`; `git ls-remote origin refs/heads/master` prints
`d05a00019835dee5b9bb8fe738add080434c4d67`.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 | `python3 -B census/round-60/c1-counter.py --root . --matrix census/round-60/c1-matrix.tsv --base-tool-rev 1e8bfd87a9f6ea9a1db4ad34f6e4cdd2b218bcd4 --rev <full40> --work DIR --new-tool tools/souji-freeze-check.py` | `new_forgeries=5 new_honest=3`, `EXIT=1` (do-nothing arm, `--new-arm plain`, base tool bytes) — `census/round-60/controls/c1-do-nothing.txt` | `new_forgeries=0 new_honest=3 stubs=REJECTED`, `EXIT=0` — `census/round-60/records/c1-after.txt` | before at `3b55250…`, after at `2670e96a…` |
| C2 | `python3 -B tests/fixtures/r60-receipt-write.py --tool <tool> --work DIR` | `pass=4 fail=4`, `EXIT=1` against `census/round-57/record-receipt.sh` — `census/round-60/controls/c2-do-nothing.txt` | `pass=8 fail=0 control=ALWAYS-WRITE-REJECTED,ALWAYS-REFUSE-REJECTED`, `EXIT=0` against `tools/souji-receipt-write.py` — `census/round-60/records/c2-after.txt` | before at `3b55250…`, after at `2670e96a…` |

Numeric axis scores unchanged (calibration 7, operability 8, coverage 8): the lane has no reproducible
0–10 mapping and the closure rules admission. Capability rows entered: "freeze-record substance binding"
and "atomic receipt writing", both first-working round r60, both demonstrated by the commands above.

## Sources & frontier

- **Census before:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` →
  exit 0, registry rows 211 (`census/round-60/records/sources-before.txt`).
- **Census after:** same command → exit 0, registry rows 213
  (`census/round-60/records/sources-after.txt`); row count by
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 213.
- **Rows added by tier:** A1 (`S288` Python `os.replace`, mined) / B0 / C0; one rejection `S289`
  (cross-filesystem rename inference, flip: place the temp beside the output).
- **Rows touched old→new:** none — S110, S213, S214 and S251 were re-opened this round with their
  status/recheck/used-by cells left byte-identical (deliberate: the ground is already held, and a
  re-dated cell would claim a freshness move the round did not make). One in-round E11 was found and
  fixed: `used-by` is split on commas, so the S288 cell's `; ` separator read as one dangling path;
  that is mined as a second mistake in the lesson.
- **Frontier rows advanced:** F1 gains `freeze-record-substance-binding.md` (entries held, no promotion
  to Core). F4 gained no entry: its held `origin-record-exclusivity-r28.md` ground is what the writer
  applies, and the scribe's duplicate draft was refused.
- **Assimilation:** none — `/home/vgpnk/Projects/shokuknow/merge/souji/` was checked and not adopted
  (the r46 mass-id-drift hold is retained). `considerthese/` is absent from the lane root.
- **Sourced claim:** C1's entry and this round's registry cite `S288` (opened 2026-11-04) and the
  re-opened `S251`; both carry the L1's own access date and located quotes in `corpus/lessons/round-60.md`
  `## Gate`.

## Trend verdicts

- **expansion — unchanged.** Registry +2 rows, one F1 entry on ground the lane did not hold (receipt
  binding, as distinct from the held strict-descendant rule). No new province, no Core promotion, no
  package adoption; the refused duplicate draft is part of the record.
- **quality — improved.** Two instruments that were debt became gates: the freeze checker now refuses
  five label-only forgery states it accepted at base (`new_forgeries` 5 → 0 on frozen bytes), and the
  receipt writer publishes atomically and refuses eight writer-side hazards the r57 recorder accepted
  (`pass` 4 → 8). The six attack-driven repairs landed *before* the freeze, and the round's own record
  scores `findings=0` under the arm it lands.
- **discernment — improved.** The fresh start's prerequisite was met by execution, not assertion: red
  controls committed before the predicate, base values taken from the instruments (C2's base is the
  measured 4/8, contradicting the prompt's 3/8 — the critic caught it and the freeze uses the measured
  value). Five surviving mutants and the reviewers' residual attacks are reported as named limits for
  r61 rather than absorbed.

## SHONEN

- `[~]` SKILL.md decision tables / error patterns / checklists with cited sources — `SKILL.md`
  "Round 60" section (two gate rows, verdict maps), `corpus/knowledge/freeze-record-substance-binding.md`
  decision table, S288/S289.
- `[~]` At least one end-to-end domain task executed and logged — this round's two claims, executed at
  `2670e96a…` and logged in `LOG.md` `## Round 60`.
- `[~]` Instructions executable by an agent without oral context — the two entry commands in `SKILL.md`
  reproduce both after-states from committed bytes (`census/round-60/records/`).
- `[~]` No cross-domain bleed, `PROVINCE.md` accurate — the writer is a lane-local receipt tool; no
  cleanup, credential or host authority was acquired. `PROVINCE.md` unchanged and still accurate.

## Round shape, seats, dead seats, extras

- **Shape:** ONE validated v1 wave (policy band 8–16, `ufo-wave-policy.json`), 14 spawn lanes, 0 resume.
  Role mix: executor 5, scout 2, reviewer 2, scribe 1, critic 1, mutation-tester 1, sentinel 1,
  connector 1. Attack share 4/14 (28.6 %); connector seats 1 (≤2). L1 held the canonical planner seat
  (the validator rejects `planner`); the bounded planning data-walk rode `S60ScoutFrontier`.
- **Round total:** 14 seats; no residual `task` call; **no dead seat** — the orchestrator's
  `w1-results.json` reports 14/14 settled, preserved byte-for-byte as `census/round-60/wave/` with
  `census/round-60/wave-SHA256SUMS` (365 rows). No seat was replaced.
- **Seat defects (honest):** two seats returned no findings text — `S60ScoutSources` and
  `S60SentinelRound` ended mid-narration with their file artifacts in place (the census receipts and
  three probe scripts). Their work is therefore *not* counted as evidence: the source rows and the
  Gate were written by the L1 from its own re-opened pages, and the sentinel's three probes
  (`probe-writer-out-escape.py`, `probe-writer-dirty-bypass.py`, `probe-fixture-gitenv.py`) are
  preserved as unread artifacts for r61. The reviewer seats independently covered out-escape and
  dirty-tree bypass.
- **Inherited state:** no uncommitted round-60 lane work existed at base (the fleet's
  `round-60: souji dispatch evidence` commit is the prompt file only); nothing was inherited or reverted.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows orchestrator
  `.scratch/` state, the shared L0 file, a sibling kama report and the pre-existing `after` file — no
  souji seat wrote into the fleet root, so nothing was copied or deleted.
- **Tool installs:** none; no pacman transaction; all scratch under `/fast/scratch/hyaku/souji-r60`
  (removed by the L1 after landing).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **L0 questions:** none opened this round.
