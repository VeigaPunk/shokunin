# mori — round 37 report (L1 MoriR37, attempt 1)

Lane: `mori-shokunin` (fleet root `/home/vgpnk/Projects/shokunin`). Entering tip
`842a32074b5c7972e9728f3f629d83eb92f127c2`. Scored tip `e57c58b5`; final lane tip
`5dff52a1ba4e76b8a30f2557a09239b9568b5680` (pushed, `ahead=0 behind=0`).

## Work performed

Round claims (declared in the frozen contract, each on a distinct axis, causally separable):

- **C1 — calibration (score 5, tied lowest):** the C2 gate measurement must discriminate a real-arm
  memoizer (r36 w2/RevNgC2 N1) and enforce the tool's per-id `changed`/`deleted` grammar (r36
  w2/MutC2Deleted limit 3). Claim type: measured. Predicate P-C1 is verbatim in
  `.ufo/waves/round-37/contract.md`.
- **C2 — freshness (score 5, tied lowest):** the source-drift probe's two fetch policies landed at
  `8ff9bba` (4 MiB bounded read; post-redirect public-destination check) are named, mutation-killable
  selftest arms, and the corpus binds them. Claim type: measured. Predicate P-C2 verbatim in the
  same contract.

Work items (one bullet each, evidence pointer):

- Freeze before data: contract + both counters + three negative fixtures pinned in
  `.ufo/waves/round-37/evidence/freeze-r37.txt` (blob `7518fef8` count-c1, `6213cf9a` count-c2;
  sha256 `86699627`/`71c72929`), committed at `e57c58b5`.
- C1 counter `.ufo/waves/round-37/count-c1.py`: blind arm (24 run-time histories, summary **and**
  per-id lines), real arm (lane history 6bd57097 / base f10a320d), new **challenge** arm (run-time
  history in real-arm clothing: lane path under `.ufo/waves/round-37/scratch`, lane git identity,
  lane SOURCES title), and three negative fixtures (`memo-n1`, `const`, `summary-only`) that must be
  rejected. Evidence: `evidence/c1-after.txt`, `evidence/c1-after-tip.txt`.
- C1 before receipts, using the round-36 frozen counter on the same fixtures:
  `evidence/c1-before-memo.txt` (`C2=met` for the memoizer), `evidence/c1-before-summary.txt`
  (`C2=met` for the summary-only printer).
- C2 counter `.ufo/waves/round-37/count-c2.py`: eight checks over committed bytes — `tool_present`,
  `selftest` (6 named arms), `cap_kill`, `redirect_kill`, `knowledge`, `capability`, `readme`,
  `live`. Evidence: `evidence/c2-after.txt`, `evidence/c2-after-tip.txt`, `evidence/c2-before.txt`.
- Drift tool: two named arms added to `--selftest` (`huge_cap`, `redirect_private_refused`) with a
  literal 4 MiB fixture body so a mutated cap cannot resize the fixture (`tools/mori-source-drift.py:398-415`).
- Knowledge entry `corpus/knowledge/source-drift-hardening-r37.md`: the two policies, their code
  lines, the named arms and mutation kills, the live run, and five disclosed limits.
- Five source rows S221–S225 opened this round, copies under `corpus/evidence/sources-r37/`, quotes
  and locations in `corpus/lessons/round-37.md` `## Gate`.
- README: coverage-map rows for `knowledge/source-drift-r36.md` (the missing row) and
  `knowledge/source-drift-hardening-r37.md`, plus a `## Round-37 coverage additions` section.
- SCORECARD: Round-37 declaration + measured outcome, two capability rows (`real-arm challenge
  counter`, `source-drift re-fetch probe`), and the calibration/freshness evidence cells now name
  round 37.
- QUALITY 106 (a measurement's discrimination is checked against an arm-detector, not only a
  constant) and 107 (a tool interface's per-id lines are checked, not only its summary).
- Routed r36 debt (d): `tools/mori-round17-jj-regressions.py`'s `jj_config_redirected` assertion is
  scoped to the testable redirect property and requires the jj file when a sandbox carries a jj
  workspace. Evidence: `evidence/r17-jj-selftest-r37.txt` (exit 0; the pre-fix 9/204 red is r36
  `w2/ExecCensusRegression.md`).
- Routed r36 debts (e)–(h): repo-relative lane paths in new evidence (`display_path`), `tool_timeout`
  as a distinct state with SIGTERM→SIGKILL and a 5 s grace, `mkdtemp` scratch per arm, and the
  nine-row drift prose re-verified at `corpus/knowledge/source-drift-r36.md:24-33`.
- Wave: one v2 wave built, validated and returned (see *Round shape*). No dispatch from this session
  (orchestrator-inline contract).

## Landed changes

| change | commit | LOG tie |
|---|---|---|
| freeze + both counters + three fixtures; drift entry; S221–S225; README/SCORECARD rows; scoped r17-jj assertion; `--selftest` named arms | `e57c58b5` | `LOG.md` Round 37 entry (declared claims, freeze pins, before/after) |
| C1/C2 receipts, measured outcome, QUALITY 106/107, lesson `round-37`, LOG entry, wave spec/plan/taskCall | `bcf65505` | same entry (verdicts, capability rows, census) |
| dispatch log + final-tip re-scores (`C1=met` seed 5097152322487907681, `C2=met`) | `5dff52a1` | same entry (round shape, debts) |

No axis score was moved; the SCORECARD diff from `842a320` to `5dff52a1` is additive (Round-37
section, capability rows, two evidence-cell clauses).

## Before → after measurements

| claim | axis | before (command, output) | after (command, output) | measured commit |
|---|---|---|---|---|
| C1 | calibration 5 | `python3 .ufo/waves/round-36/count-c2.py bf0df77 --tool .ufo/waves/round-37/fixtures/memo-n1.py --seed 11` → `C2=met`, exit 0 (`evidence/c1-before-memo.txt`); same with `fixtures/summary-only.py --seed 12` → `C2=met`, exit 0 (`evidence/c1-before-summary.txt`) | `python3 .ufo/waves/round-37/count-c1.py e57c58b5` → blind 24/24, real pass, challenge pass, `negative memo-n1.py rejected (challenge: …)`, `const.py rejected`, `summary-only.py rejected`, `C1=met`, exit 0, seed 13985344346805549517 (`evidence/c1-after.txt`); re-scored at `bcf65505` → `C1=met`, exit 0, seed 5097152322487907681 (`evidence/c1-after-tip.txt`) | `e57c58b5`, re-scored at `bcf65505` |
| C2 | freshness 5 | `python3 .ufo/waves/round-37/count-c2.py 842a320` → `selftest FAIL` (4 unnamed arms), `cap_kill FAIL`, `redirect_kill FAIL`, `knowledge FAIL`, `capability FAIL`, `readme FAIL`, `live FAIL`, `C2=unmet`, exit 1 (`evidence/c2-before.txt`) | `python3 .ufo/waves/round-37/count-c2.py e57c58b5` → all eight checks PASS, `C2=met`, exit 0 (`evidence/c2-after.txt`); re-scored at `bcf65505` → `C2=met`, exit 0 (`evidence/c2-after-tip.txt`) | `e57c58b5`, re-scored at `bcf65505` |

Live demonstration for the C2 capability: `python3 tools/mori-source-drift.py --root .` →
`MORI_SOURCE_DRIFT rows=220 fresh=49 excerpt=0 drifted=9 unavailable=0 no-copy=162`, exit 1
(`evidence/drift-live-r37.txt`). It is a demonstration, not a freshness verdict (QUALITY 105).

## Sources & frontier

- Census (contract command):
  `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
  → round start exit 0 (`evidence/census-start.txt`, 220 rows, W04 duplicate-URL lines only), round
  end exit 0 (`evidence/census-end.txt`, 225 rows, same W04 set). Row count command:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `220` at `842a320`,
  `225` at `5dff52a1`.
- Rows added (5): S221 (spec, A, mined), S222 (docs, B, mined), S223 (docs, A, mined), S224 (docs,
  A, mined), S225 (spec, A, mined). Tier/kind: A=4, B=1; spec=2, docs=3; status all `mined`.
- Rows touched old→new: **none** — no existing row's `status`, `recheck` or `used-by` cell was edited
  (rule 2 old→new log is empty by construction, stated in `corpus/lessons/round-37.md`).
- Gate: every new row carries URL, access date 2026-10-23 and a located ≤25-word quote in the lesson
  Gate table; copies are committed under `corpus/evidence/sources-r37/`.
- Frontier rows advanced: none. The source-drift technique is coverage ground (README coverage map),
  not a frontier row; its limits are now enumerated in the hardening entry rather than left implicit.
  FR1–FR14 are untouched by this round.

## Trend verdicts

- **expansion: improved** — five source rows and one knowledge entry enter coverage ground that had
  no registry rows (redirect/SSRF/ptrace semantics), each cited by a new entry; row count 220 → 225.
- **quality: improved** — the drift probe's two policies are now named, each killed by its own
  mutation (`cap_kill`, `redirect_kill`), and the entry states five limits with sources; QUALITY 106
  and 107 convert the r36 routed defects into standing criteria.
- **discernment: improved** — the round's own two fixture defects (a mutation fixture that resized
  itself; a memoizer fixture that did not reproduce the class it named) are mined as M1/M2 with the
  correction and the observable that caught them, and the r36 closure's routed defects (a)–(h) each
  have a named disposition (two as claims, one fixed and re-run green, four as counter properties or
  a re-verified prose check). Proposed verdicts; the closure judges.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — not touched
  this round; round-37 ground is in `corpus/knowledge/source-drift-hardening-r37.md` and QUALITY 106/107,
  and a non-author verifier can resolve every pointer there.
- [~] At least one end-to-end domain task executed and logged — the C1/C2 counters ran end to end at
  two tips and the receipts are committed (`evidence/c1-after*.txt`, `c2-after*.txt`); LOG.md Round 37
  records them.
- [~] Instructions executable by an agent without oral context — `contract.md` + `count-c1.py`/
  `count-c2.py` docstrings + `--selftest` arms are self-contained; the wave context repeats absolute
  paths and bounds.
- [~] No cross-domain bleed — PROVINCE.md untouched; the connector seats' sibling scans are in the
  validated wave (not yet returned); the round edits no sibling or operator file.

## Round shape (wave accounting)

- **One v2 wave** (alternative shape), policy `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128,
  `maxLanes` 96, hard ceiling 256): **73 seats**, validated `plan` exit 0, `counts: spawn 73`.
  Role mix: executor 24, reviewer 10, scout 8, scribe 7, critic 6, mutation-tester 5, connector 4,
  revenger 4, sentinel 3, simplifier 2. Attack roles (reviewer+critic+mutation-tester) = 21/73 =
  **28.8% ≥ 25%**. Round total 73 ≤ 128.
- Validator role mapping (recorded per the orchestrator ruling): `labrat` and `distiller` are
  frozen-topology seats in the validator's `SWARM_ROLES`, so the three bounded-probe items ride
  **executor** seats and the dedupe item rides a **scribe** seat; the **planner** seat is the L1's
  canonical §3 seat (no planner item exists or is allowed).
- Spec/plan/taskCall: `.ufo/waves/round-37/w1-spec.json`, `w1-plan.json`, `w1-taskcall.json`
  (73 tasks, 82,884 bytes); validation log `w1-validate.log` (empty stderr, exit 0).
- Wave slot: `granted lane=mori wave=mori-r37-w1 seats=73 live=75 pending=0 cap=256` (acquired
  2026-10-23T17:07Z).
- **Dispatch:** none from this session — per the orchestrator-inline contract the validated
  `taskCall` is returned to the orchestrator, which dispatches it and relays seat outputs. Dead
  seats: none to report from this session (no seat was dispatched here); the wave's returns are
  therefore not part of this report.
- Gates L2 floor: ≥1 planner (L1), 1 connector (4), 3 executors (24), 1 scribe (7), 1 scout (8),
  1 reviewer (10), 1 critic (6) — all inside the single v2 wave.

## Inherited state, misroot, installs, open questions, stale lane

- **Inherited state:** nothing uncommitted from an earlier attempt of round 37 (no
  `lane-dead-no-report mori round=37` line in the watchdog log for this round). Untracked `.scratch/`
  in the lane is the disclosed operator item, untouched.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) → 34
  entries, all modified driver state / operator files or strays that do not name mori or round-37
  (`0`, `AGENTS.md`, `bm.json`, `live*.html`, `nama.html`, `s395.txt`, `scripts/hyaku/__pycache__/`,
  two `.bak` files, `.omp/mcp.json`, round-34 wave files). No mori round-37 seat file was misrooted
  (no seat ran from this session); nothing was copied or deleted.
- **Tool installs:** none this round (no pacman transaction; python3 + git only).
- **Open L0 questions:** none new. Operator-owned items carried unchanged: LOG.md:1801 setting value,
  `refs/jj/keep 3b19cac`, `.scratch/`, SHONEN promotion review.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
