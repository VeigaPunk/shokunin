# mori — round 37 report (L1 MoriR37, attempt 1)

Lane: `mori-shokunin` (fleet root `/home/vgpnk/Projects/shokunin`). Entering tip
`842a32074b5c7972e9728f3f629d83eb92f127c2`. Scored tip `e57c58b5`; final lane tip
`e33bb561712b32f46861362a3fa43762fa70ae4f` (pushed, `ahead=0 behind=0`).

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
| S225 source copy named explicitly (1.9 MiB; the directory form skips new files over 1 MiB — lesson M5) | `52d636d5` | `LOG.md` Round 37 entry (lesson M1–M5) |
| lesson M5 appended | `4bec58eb` | same entry |
| LOG lesson range M1–M5 + S225 packaging note | `c31076ed` | same entry |
| wave-1 seat reports + lesson M6 (bytecode hygiene) + lane-wide `__pycache__`/`*.pyc` ignore | `0a05f7e6` | `LOG.md` Round 37 entry (lesson M1–M6) |
| wave-1 corrections: receipt erratum (command + repo-relative paths), C2 axis → operability, debt (f) reopened, content-free and SentTools dispositions, lesson M7–M9, LOG receipt support | `5631efa9` | same entry (corrections + receipts) |
| A1–A3: counter v2 drawn arm + challenge title, counter v3 attribution check, 225-row drift receipt, SKILL r37 registry rows, index-clean records, lesson M10 | `4bfa0490` | same entry (amendments A1–A3) |
| A1–A3 receipts (`C1=met` seed 20261024, `C2=met` `touches_tool=True`) + freeze v3 + SCORECARD/LOG re-score | `a1875349` | same entry |
| A1 predicate of record appended to the contract + drawn-arm replay pin in the C1 receipt | `e33bb561` | same entry |

No axis score was moved; the SCORECARD diff from `842a320` to `5dff52a1` is additive (Round-37
section, capability rows, two evidence-cell clauses).

## Before → after measurements

| claim | axis | before (command, output) | after (command, output) | measured commit |
|---|---|---|---|---|
| C1 | calibration 5 | `python3 .ufo/waves/round-36/count-c2.py bf0df77 --tool .ufo/waves/round-37/fixtures/memo-n1.py --seed 11` → `C2=met`, exit 0 (`evidence/c1-before-memo.txt`); same with `fixtures/summary-only.py --seed 12` → `C2=met`, exit 0 (`evidence/c1-before-summary.txt`) | **counter v2 (amendment A1)** at `4bfa0490`: `python3 .ufo/waves/round-37/count-c1.py 4bfa0490 --seed 20261024` → blind 24/24, real pass, **drawn arm pass** (`rev=842a32074b base=3c2fe8c3eb`), challenge pass, three negatives rejected, `C1=met`, exit 0 (`evidence/c1-after-v2.txt`). v1 receipts kept as history: `evidence/c1-after.txt` (seed 13985344346805549517) and `c1-after-tip.txt` | `4bfa0490` (v2); v1 at `e57c58b5`/`bcf65505` |
| C2 | **operability 7** (re-attributed from freshness by w1/CritC2Axis; see corrections) | `python3 .ufo/waves/round-37/count-c2.py 842a320` → `selftest FAIL` (4 unnamed arms), `cap_kill FAIL`, `redirect_kill FAIL`, `knowledge FAIL`, `capability FAIL`, `readme FAIL`, `live FAIL`, `C2=unmet`, exit 1 (`evidence/c2-before.txt`) | **counter v3 (amendments A2/A3)** at `4bfa0490`: `python3 .ufo/waves/round-37/count-c2.py 4bfa0490` → all eight checks PASS, `knowledge … cited_commit=True touches_tool=True`, `live PASS` (225-row sentence), `C2=met`, exit 0 (`evidence/c2-after-v3.txt`); v1/v2 receipts kept as history (`c2-after.txt`, `c2-after-tip.txt`) | `4bfa0490` (v3); v1/v2 at `e57c58b5`/`bcf65505` |

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
  and 107 convert the r36 routed defects into standing criteria. Disclosed limit: P-C2's content half
  is token-checkable (w1/CritC2ContentFree), so the claim verifies on the frozen predicate but does not
  prove the corpus content.
- **discernment: improved** — the round's own five defects (two fixtures, one packaging/bytecode, one path-hygiene repeat, one redundant wave trio) (a mutation fixture that resized
  itself; a memoizer fixture that did not reproduce the class it named) are mined as M1/M2 with the
  correction and the observable that caught them, the 11 wave-1 FAILs are each dispositioned above (three turned into corrections, two into reopened/open items), and the r36 closure's routed defects (a)–(h) each
  have a named disposition (two as claims, one fixed and re-run green, four as counter properties or
  a re-verified prose check); one of them, (f), is reopened as an operator-owned tradeoff rather than
  claimed closed, and one attribution error (M10) was found by the wave and corrected at its root. Proposed verdicts; the closure judges.

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
- [~] No cross-domain bleed — PROVINCE.md untouched; connector returns landed (`w1/ConnChousa.md`
  PASS: the probe stays inside mori's detection/report province, the S205 method line intact) and the
  round edits no sibling or operator file.

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
  `taskCall` was returned to the orchestrator, which dispatched it inline and relayed seat outputs.
  **Wave-1 returns landed at this report's final commit: 62 of 73 reports** (46 PASS, 16 FAIL; the
  remaining seats arrive through the orchestrator and are collected by the closure). Reports:
  `.ufo/waves/round-37/w1/*.md`. **Dead seat:** `ExecR17JJBattery` completed without writing a report
  (its own background-job attempt hit the 100-job limit); the r17-jj battery is covered by
  `w1/RevR17JJ.md` (PASS, a mutant turns exactly the nine `jj_config_redirected` assertions red) and
  by `evidence/r17-jj-selftest-r37.txt`. `w1-plan.json` records `agentId: null` for every member
  (inline-dispatch bookkeeping, the same side effect round 36 saw).
- **Wave-1 FAILs and dispositions (16; the first 11 were dispositioned before the first report commit):**
  `CritC2Axis` → C2 re-attributed to operability (freshness not claimed as moved); `CritC2ContentFree` →
  P-C2's content half is token-checkable, the claim is reported as verified on the frozen predicate
  **with a disclosed content-discrimination gap** and the content-anchor arm is routed to round 38
  (lesson M9); `CritDebtDisposition` → (e) closed only by the erratum, (f) **reopened** as an
  operator-owned policy tradeoff (SIGTERM→grace→SIGKILL is a trade, not the requested restructuring);
  `ScoutPriorRound` → r36 freeze-pointer addendum, `ExecGateRound` superseded, frozen-byte residuals
  named; `ScoutSentData` + `SentData` → receipt erratum; `ScoutWaveSpec` → M7 (three seats on one
  loop body); `ScribeLog` → missing receipt support (census rows, pre-fix red, copy size, scores);
  `ScribeQuality` → QUALITY 106's quote now matches the receipt's spacing; `ScribeScorecard` → every
  receipt now carries its `command:` line; `SentTools` → HIGH accepted-by-design (the counters execute
  the tool under test — that is the measurement; the trust boundary is the caller's `--repo`/`--tool`),
  MEDIUM (`count-c2.py` `show()` git reads have no timeout/size bound) and LOW (relative `--tool`
  validates and executes from different directories) routed to round 38, both needing a counter
  re-freeze.
- **Later wave-1 FAILs and dispositions:** `RevC1Challenge` (HIGH: the challenge title self-labelled
  "(challenge arm)" and the fixed real arm's published constant let an identity/clothing-keyed memoizer
  pass) → **amendment A1**: the challenge title is the lane's real title verbatim and the counter runs a
  **run-time-drawn ancestor rev** whose answer is not published; re-scored `C1=met` (`evidence/c1-after-v2.txt`),
  with the rev-literal residual disclosed. `ExecDriftLive` (the live receipt was the entering 220-row sweep
  and the prose said nine rows) → **amendment A2**: `drift-live-r37.txt` is the 225-row tip sweep
  (`rows=225 fresh=53 … drifted=10 …`), the 220-row sweep is `drift-live-r37-start.txt`, and the entry/README
  now name ten rows (S223's footer clock; S211 class). `ExecKnowledgeCheck` (adjacent finding: the hardening
  is `1caa242`, not `8ff9bba`) → **amendment A3**: every artifact corrected, and the counter reconstructs the
  commit and requires `touches_tool=True`. `ExecLessonGate` (S225 quote line range) → range widened to
  `:8355-8356`. `ExecIndexClean` (QUALITY 103's per-landing record missing) → records appended to the dispatch
  log. `ScribeReport` (S225 copy and live-receipt tip) → both reconciled as above. `ScoutReportContract`
  (SHONEN box wording) → box 4 now names the landed connector report.
- **A1 predicate of record:** the contract's v1 P-C1 blockquote stands as the declared-before-data text;
  the v2 predicate (drawn arm) is appended verbatim under *A1 predicate of record* with the counter blob
  `3e15f9fd…`, and the C1 receipt names its lane tip (`4bfa0490`) because the drawn arm draws from
  `git rev-list HEAD` (w1/ExecC1Seed43 R2).
- **Other wave-1 corrections:** the two `.ufo/waves/round-37/__pycache__/*.pyc` paths in the freeze
  commit are lesson M6 (removed at `bcf65505`; `.gitignore` now ignores `__pycache__/`/`*.pyc`); the
  evidence receipts now carry `command:` lines and repo-relative paths (`redacted:` per file, same
  measured output). C2's operability re-attribution and debt (f) are appended to the frozen contract
  and to SCORECARD rather than edited into the frozen cells.
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
