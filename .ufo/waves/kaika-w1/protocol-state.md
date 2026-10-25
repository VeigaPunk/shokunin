# kaika W1 — STATE dossier — fleet-root `protocol` lane

Read-only research artifact. Author: `W1ProtocolLane`. Date: 2026-10-19.
Lane bounds: leaf member, no subagent dispatch, no repo edits, no git mutations.

Evidence base: `/home/vgpnk/Projects/shokunin`, branch `master`, HEAD `31baf5c`
(`git rev-parse --short HEAD`), clean tree (`git status --porcelain | wc -l` -> 0).
The lane's registry home is the protocol section of root `SCORECARD.md` above
`## Aggregator lane` (`PROTOCOL.md:384`), and its log is root `LOG.md`.

**Read this before the scores: at HEAD the registry home and the protocol log do not
exist.** Root `SCORECARD.md` and `LOG.md` are byte-identical to `kotoba-shokunin`'s
HEAD files, replaced by commit `31baf5c` (HEAD). The last fleet versions are at
`0b1ac3b` (the last commit that edits them; the same bytes are at HEAD's parent
`12f2da5`), which is the evidence base for every protocol-lane score and log claim
below. See Defect D1. Peer `W1Drift` independently reported the clobber and the
round-14 evidence deletion; both were re-verified here (`git show --stat e20f4fa`,
`git ls-tree b2f2efa`, `git show ab707d9:MANIFEST.json`).

## 1. Identity

- **Lane / domain.** `protocol`; fleet-meta domain: "protocol soundness, gate
  integrity" (`MISSION.md:21`; `scripts/shokunin-watchdog.sh` `LANE_AXES[protocol]`).
  Main-repo lane: `cwd` is the fleet root, not a child repo (`MISSION.md:21`).
- **Rank.** Not a roster lane. `MANIFEST.json` roster ids:
  `kasegi kengaku kake kumitate kotoba kagi kama audio game-dev-2d game-dev-3d lore
  revenger kaidoku` (`python3 -c "import json;print([r['id'] for r in
  json.load(open('MANIFEST.json'))['roster']])"`). It is the integrator-of-record:
  "integrator-of-record instantiated (protocol lane; MANIFEST rounds append
  authorized)" (`MANIFEST.json`, round-10 entry notes).
- **Repo / branch / HEAD.** `/home/vgpnk/Projects/shokunin`, `master`, `31baf5c`
  (2026-10-19T17:03:23-03:00); HEAD's parent is `12f2da5`, which still carries
  the fleet ledgers; `0b1ac3b` (2026-10-16T22:39:52-03:00) is the last commit that
  edits them.
- **Last round with evidence.**
  - Highest report: `.ufo/reports/round-15/protocol.md` (38 lines, 2026-09-29;
    gate-integrity 8 -> 9). Implementation commit `3687e5a` ("round-15"), report
    commit `bdff08b` ("round-15 report").
  - Fleet LOG at `0b1ac3b` has protocol-lane entries for rounds 10, 11, 12 and 15
    (`git show 0b1ac3b:LOG.md | grep -c '^## .*protocol lane'` -> 4); rounds 13 and
    14 have no LOG entries.
  - SCORECARD at `0b1ac3b`: gate-integrity last changed round 15; protocol-soundness
    last changed round 13 (`git show 0b1ac3b:SCORECARD.md | sed -n '24p;25p'`).
  - **Ledger hint 13 resolved.** The last row carrying an explicit
    `lane_rounds[protocol]` value is entry 45 (round-15 closure), value `13`
    (`MANIFEST.json` `rounds[45].lane_rounds`). Later protocol rows are
    round-keyed and carry no `lane_rounds`: entry 52 (round 15, `in-flight`),
    entry 53 (round 14, `failed`), entry 55 (round 13, `failed`), all closed
    `2026-09-29T00:34:00-03:00`. So "13" is the last recorded lane counter, not
    the last work round.
  - **Next round is contested.** SCORECARD planned "Round 16"; the driver counter
    `.ufo/state/protocol.round` is `14`, and the driver launches `n+1` when the
    round-`n` report exists (`scripts/shokunin-watchdog.sh:99-112`). `report_of
    protocol 14` is true (the 340-byte marker), so the driver would launch
    **round 15 again** - and `.ufo/reports/round-15/protocol.md` already exists.
    Counter, reports and planned number disagree. See Defect D5.

## 2. Axes and scores

Scores are the protocol lane's recorded claims at `0b1ac3b`; this wave did not
re-execute the gates. Static re-checks are named.

| Axis | Score (recorded) | Recorded evidence | Static re-check this wave |
|---|---:|---|---|
| gate-integrity | 9 (was 8) | `0b1ac3b:SCORECARD.md:24`; round-15 report `.ufo/reports/round-15/protocol.md:1` | `.ufo/waves/round-15/closure-check.py` exists; sha256 `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` (`sha256sum`) matches the report; 25 fixture dirs (`find .ufo/waves/round-15/fixtures -mindepth 2 -maxdepth 2 -type d \| wc -l`); 2 frozen `expected.json`; 171 files in the wave dir. Selftest 27/27, generator 37/37, mutants 7/7 are **recorded, not re-run**. |
| protocol-soundness | 8 (held) | `0b1ac3b:SCORECARD.md:25`; last change "round 13" | Recorded "470 lines + 48-line appendix"; current `wc -l -c PROTOCOL.md PROTOCOL-APPENDIX.md` -> `513 44449` and `51 14390`. `.ufo/waves/round-13/verify-protocol.sh` exists; the 8 checks / 169-of-169 census / 61 anchors were **not re-run**. The recorded size and the "registry home remains unresolved" clause are stale (see D8). |

- **Lowest non-retired axis:** protocol-soundness, **8** vs gate-integrity **9**
  (`0b1ac3b:SCORECARD.md:24-25`). A next round must put at least one claim here.
- **Saturation:** undeclared. The section says "to be declared by the protocol lane
  on its next round" (`0b1ac3b:SCORECARD.md` §Saturation). No saturation line and no
  stagnation window N exist, so the stagnation-nudge waiver cannot be evaluated.
- **Capabilities:** **0** rows. The section exists with a header and no capability
  row (`0b1ac3b:SCORECARD.md` §Capabilities; `grep -cE '^\| [a-zA-Z]'` over the
  section -> 1, the header; data rows 0). Round 15 demonstrably ran a gate, but the
  table was added by the 2026-10-16 rollout after that round, so nothing is
  pre-claimed.
- **Planned claims (as written):**
  1. "Round 16 (protocol-soundness, now the lower axis at 8): resolve §Gate
     standard's registry-home contradiction for the two main-repo lanes, then
     register the closure gate at that declared home and re-run every registry
     citation" (`0b1ac3b:SCORECARD.md` §Planned).
  2. Gate-integrity residuals queued: encode git trackedness in frozen prompt
     evidence; classify untracked prompt names; decide whether non-closure payloads
     need schema validation.
  3. Operator-side, unchanged: `report_of()` completes on file existence,
     `.gitignore`, runtime `.ufo/state/*` plus `.ufo/watchdog.log`.
  Note: planned item 1 is **half-landed** in text (`PROTOCOL.md:384` defines the
  main-repo registry home; `PROTOCOL-APPENDIX.md:51` records the round-14 cutover)
  but is recorded as unresolved in the score row and then erased at HEAD by D1.
- **Axis-vocabulary defect.** `AXES.md` defines six axes and none is
  `gate-integrity` or `protocol-soundness` (`grep -c 'gate-integrity\|protocol-soundness'
  AXES.md` -> 0). `MISSION.md` assigns them (`grep -c` -> 1) and `SCORECARD.md`
  scores them (`0b1ac3b:SCORECARD.md` -> 14 hits). The lane's scores are therefore
  not re-derivable against `AXES.md`; this is the protocol lane's own instance of
  the D-78 class (kotoba's `consistency`, kengaku's `novelty`). See D7.

## 3. Corpus, lessons and evidence

The protocol lane has **no lane corpus**. Counts:

- `corpus/` at root: absent (`ls -d corpus` -> No such file). `corpus/README.md`,
  `corpus/QUALITY.md`, `corpus/knowledge/`, `corpus/lessons/`: 0.
- Root `SKILL.md`, `PROVINCE.md`, `QUALITY.md`, `SHONEN.md`: all absent
  (`for f in ...; do [ -e "$f" ] ...` -> absent each). `SOURCES.md`: absent at root
  (`find . -name SOURCES.md -not -path './.git/*'` -> 6 hits, all
  `audio-shokunin/corpus/live/r9{1,5,8}-scout/sources/SOURCES.md` and their worktree
  copies; none is the campaign contract).
- Protocol reports: **14** files (`find .ufo/reports -maxdepth 2 -name protocol.md
  | wc -l` -> 14; no round 2). Two are markers: round 13 = 275 B, round 14 = 340 B
  (`wc -c`), each with 0 headings (`grep -c '^## '` -> 0). Round 15 = 38 lines.
- Evidence: `.ufo/waves/round-15` = 171 files, 25 fixture dirs, 2 frozen baselines;
  `.ufo/waves` = 1,646 files, 19 MB (`find ... | wc -l`; `du -sh`); `.ufo/reports`
  = 2.6 MB.
- Appendix: `PROTOCOL-APPENDIX.md` has 44 lines beginning `|` (`grep -c '^|'` ->
  44, header included). One row, "Registry home" at line 51, points at
  `.ufo/waves/round-14/registry-home-rerun/before.json` - **absent** (D3).
- Recheck/source fields: there are no `corpus/knowledge/` entries, so
  `source:`/`verified-at:`/`recheck:` coverage is 0/0/0 and "overdue recheck before
  2026-10-19" is not measurable. The three `recheck:` hits under `.ufo/waves` and
  `.ufo/reports` (`grep -rl 'recheck:' ... | wc -l` -> 3) are scout artifacts, not a
  lane corpus.
- Coverage map / frontier: `corpus/README.md` and `PROVINCE.md` do not exist, so
  coverage-map rows = 0 and `## Frontier` rows = 0. This is not a small corpus; it
  is a **missing corpus home** for a lane whose campaign deliverable D1 assumes
  `corpus/SOURCES.md` (D6).

## 4. Mistakes mined (7)

No lane-owned `QUALITY.md` or `SKILL.md` exists (`find . -maxdepth 1 \( -name
QUALITY.md -o -name SKILL.md \) | wc -l` -> 0), so "already captured by a lane
criterion" is answered against the fleet contract (`PROTOCOL.md`,
`PROTOCOL-APPENDIX.md`, `CORPUS.md`, `LEARNING.md`) and marked accordingly.

1. **Marker accepted as a round (r13, r14).**
   - Evidence: `.ufo/reports/round-13/protocol.md` 275 B, `.ufo/reports/round-14/
     protocol.md` 340 B, 0 headings; MANIFEST entries 53/55 record both `failed`;
     the driver completes on `report_of()` existence
     (`scripts/shokunin-watchdog.sh:45`).
   - Captured? `PROTOCOL.md` report contract has a marker rule, and the appendix has
     "Marker vs report" rows; the **actuator** still completes on existence, so the
     rule is not executable at the driver.
   - Proposed criterion: a report without `## Before -> after measurements` and a
     cited commit is `failed`; add it to the closure gate's report screen, not just
     to prose.

2. **Dead evidence pointers for the round-14 cutover.**
   - Evidence: `PROTOCOL-APPENDIX.md:51` cites
     `.ufo/waves/round-14/registry-home-rerun/before.json`; the
     `registry-home-rerun/` directory is empty (`find ... -type f | wc -l` -> 0),
     and all four cited files (`before.json`, `dispatch.json`, `integration.md`,
     `critic.md`) are absent (4/4). The LOG entry also cites them
     (`0b1ac3b:LOG.md:749`).
   - Captured? `PROTOCOL.md` Evidence standard and appendix "Evidence standard" row
     say a claim names a resolvable source; no gate checks SCORECARD/APPENDIX paths.
   - Proposed criterion: every evidence path in `SCORECARD.md` and
     `PROTOCOL-APPENDIX.md` must resolve at the landing commit; add a path check to
     the registry gate.

3. **Commit-message overclaim with a swallowed fatal.**
   - Evidence: appendix row "Durability commit | 13": `fcefcf5` claimed 11 prompts +
     2 orphan reports + two wave dirs while its diff carried 8 files; a `git add`
     aborted on a mistyped pathspec and `2>/dev/null` swallowed the fatal; corrected
     in `b5fff81` (both commits exist: `git cat-file -t` -> commit).
   - Captured? No gate covers commit-message counts.
   - Proposed criterion: commit messages either omit file counts or are checked
     against `git show --numstat`; never silence a bulk-add failure.

4. **Counter/report collision.**
   - Evidence: `.ufo/state/protocol.round` = 14; the next launch is 15
     (`scripts/shokunin-watchdog.sh:99-112`); `.ufo/reports/round-15/protocol.md`
     already exists (`test -e` true). `closure-check.py` contains 0 occurrences of
     "collision" (`grep -c collision` -> 0).
   - Captured? Row identity in `PROTOCOL.md` covers ledger keying, not the driver
     counter; other lanes filed L0 counter questions (kumitate r17, kotoba r16), but
     no protocol-lane line exists.
   - Proposed criterion: a preflight fails when `state + 1` collides with an
     existing report or when the state/report/planned numbers disagree.

5. **Scores on axis names `AXES.md` does not define.**
   - Evidence: `grep -c 'gate-integrity\|protocol-soundness' AXES.md` -> 0;
     `0b1ac3b:SCORECARD.md` -> 14 hits; `MISSION.md` -> 1.
   - Captured? `AXES.md` says protocol/aggregator own "fleet-level axes" but does not
     define them; the D-78 L0 line covers kotoba/kengaku, not this lane.
   - Proposed criterion: every SCORECARD axis name resolves to an AXES.md definition
     or a SCORECARD-declared sub-axis mapping with a definition.

6. **Root ledger replacement under a "bookkeeping" commit.**
   - Evidence: `sha256sum SCORECARD.md` equals
     `git -C kotoba-shokunin show HEAD:SCORECARD.md | sha256sum`
     (`a4ec5348...`); `LOG.md` equals kotoba's (`998274c0...`); `git diff --numstat
     31baf5c^ 31baf5c -- SCORECARD.md LOG.md` -> `165 395` and `1356 845`; commit
     message says "LOG/SCORECARD/l0-questions bookkeeping catch-up".
   - Captured? `PROTOCOL.md` lane write scope and the appendix "Lane write scope"
     row (kagi carried a main-repo file) cover a lane overstepping; no gate checks
     root ledger identity.
   - Proposed criterion: a root-ledger commit must preserve the fleet header and the
     protocol registry section; fail closed if the header is a lane header or the
     section disappears.

7. **Cutoff-bounded gate score without its live residual in the score row.**
   - Evidence: round-15 report boundary says "Final smoke saw post-cutoff exit 1 /
     debt 10" (`.ufo/reports/round-15/protocol.md`, §Boundary), while the
     SCORECARD gate-integrity row records only the frozen 17 -> 0 movement
     (`0b1ac3b:SCORECARD.md:24`).
   - Captured? The report names the boundary; `PROTOCOL.md` requires a verdict to
     name its revision, and the score row does cite round 15, but not the residual.
   - Proposed criterion: a cutoff-bounded score row names the cutoff, the live
     residual and the command that measured it.

## 5. Contract defects (12)

D1. **Root `SCORECARD.md` and `LOG.md` are kotoba's files at HEAD.**
   - `head -1 SCORECARD.md` -> `# kotoba-shokunin — Scorecard`; proper
     `git show 0b1ac3b:SCORECARD.md | head -1` -> `# shokunin (main repo) — Scorecard`.
     `head -1 LOG.md` -> `# kotoba-shokunin — Iteration Log`.
   - SHA equality with `kotoba-shokunin` HEAD for both files (commands in M6).
   - Sizes: current SCORECARD 59,226 B / 208 lines; proper 62,148 B / 438 lines.
     Current LOG 131,795 B / 1,356 lines; proper 64,287 B / 845 lines
     (`wc -c`, `wc -l`, `git show | wc`).
   - **Already flagged before it was committed.** `ab707d9`'s kotoba r42 MANIFEST
     note (entry 274) records "fleet-root LOG.md + SCORECARD.md are
     uncommitted-overwritten with kotoba-derived content (mtime 07:35, pre-dates
     this session...)" and leaves them "untouched per boundary". `31baf5c` then
     committed the overwrite.
   - Effect: the protocol lane has **no log** and **no scorecard** at HEAD; every
     protocol SCORECARD/LOG claim below is historical (`0b1ac3b`) until repaired.

D2. **Registry home and aggregator section absent at HEAD.**
   - `grep -c '^## Aggregator lane' SCORECARD.md` -> 0 at HEAD; `0b1ac3b` -> 1.
   - `grep -cE '^\| closure-check \|' SCORECARD.md` -> 0 at HEAD; `0b1ac3b` -> 1.
   - `PROTOCOL.md:384` requires the main-repo registry section; the gate's registered
     home is gone.

D3. **Round-14 cutover evidence is empty at HEAD but recoverable.**
   - `.ufo/waves/round-14/registry-home-rerun/` has 0 files at HEAD; 4/4 cited files
     absent (`find ... -type f | wc -l`; per-file `test -e`).
   - `e20f4fa` ("souji: remove 96 pushed-receipt checkpoint artifacts", 2026-10-18)
     deleted 12 files / 1,438 lines from that directory
     (`git show --stat e20f4fa -- .ufo/waves/round-14/registry-home-rerun`).
   - All 12 are present at `b2f2efa` (`git ls-tree -r --name-only b2f2efa --
     .ufo/waves/round-14/registry-home-rerun | wc -l` -> 12); the recovered
     `before.json` records `protocol_registered_closure_gates=0` and
     `root_SKILL_exists=False` at measured commit `99efc52` (24-line file).
   - `PROTOCOL-APPENDIX.md:51` still cites `before.json`; `0b1ac3b:LOG.md:749` cites
     `before.json`, `dispatch.json`, `integration.md`, `critic.md`.
   - The directory itself survives, so a naive `test -d` passes; a `test -e` on the
     cited files fails. Recovery is a restore/repoint, not a re-authorship.

D4. **Round 14 has three contradictory descriptions.**
   - `.ufo/waves/round-14/plan.md` (2026-09-28): "protocol-soundness compaction".
   - `0b1ac3b:LOG.md:749` (2026-10-15): "round 14 protocol relaunch:
     registry-home cutover".
   - `.ufo/reports/round-14/protocol.md`: "mid-move on the 'tracked-runtime' axis
     item at ~63% context".
   - No single round-14 record reconciles them; the report is a marker.

D5. **Ledger / counter / planned-number collision.**
   - Last protocol row: entry 52, round 15, `in-flight`, closed
     `2026-09-29T00:34:00-03:00`; no later row.
   - Terminal statuses: entry 53 (round 14 `failed`), entry 55 (round 13 `failed`).
     Entry 53's round 14 is the 2026-09-28/29 attempt; the 2026-10-15 registry-home
     relaunch reuses number 14 and has **no** closure row (W1Drift confirms; the
     last protocol row is entry 52, round 15).
   - `.ufo/state/protocol.round` = 14; driver next = 15; report 15 exists; SCORECARD
     planned 16. `test -e .ufo/reports/round-15/protocol.md` -> true.
   - The round-15 score (gate-integrity 9) is therefore not ledger-closed; the driver
     would reuse the number and could complete on the stale report.

D6. **No corpus or lane files at the fleet root.**
   - `corpus/`, `SKILL.md`, `PROVINCE.md`, `QUALITY.md`, `SHONEN.md` absent
     (commands in §3). `PROTOCOL.md` file contract lists `SKILL.md`, `PROVINCE.md`,
     `LOG.md`, `SHONEN.md`, `AGENTS.md`, `corpus/`, `SCORECARD.md` for every
     shokunin repo. The round-14 registry-home amendment (2026-10-15) exempts only the root
     `SKILL.md` for registry purposes (`PROTOCOL.md:384-387`; Appendix:51), not the
     rest. Either add a main-repo clause or the lane is out of contract.
   - Consequence for the campaign: `corpus/SOURCES.md` (D1) has no lane home here.

D7. **Fleet-meta axis names are undefined in `AXES.md`.**
   - `grep -c 'gate-integrity\|protocol-soundness' AXES.md` -> 0; SCORECARD 14;
     MISSION 1. The six-axis table (depth, coverage, operability, freshness,
     calibration, adjacency) does not include the two axes this lane scores.
   - The round-14 decision record maps them ad hoc: protocol-soundness is "mapped to
     AXES.md depth/calibration"; gate-integrity "maps to operability/calibration"
     (`b2f2efa:.ufo/waves/round-14/registry-home-rerun/decision.md`). The mapping is
     not in `AXES.md` or the SCORECARD, so a registry-home reader cannot re-derive it.

D8. **Protocol-soundness evidence is stale and its stated blocker is resolved.**
   - Recorded: 470 + 48 lines, 8 checks, 169/169, 61 anchors
     (`0b1ac3b:SCORECARD.md:25`).
   - Current: `513 44449` + `51 14390` (`wc -l -c`). The growth includes the
     operator-mandated multi-claim amendment `84bade0` and the registry-home row.
   - The same row says "§Gate standard's registry home for a main-repo lane remains
     unresolved", while `PROTOCOL.md:384` now defines it and Appendix:51 records the
     cutover. The score is held, but the evidence pointer no longer describes the
     tree.
   - The recovered round-14 `integration.md` is stronger: the archival round-13
     verifier's "historical 470-line budget was already exceeded by the baseline
     505-line body", and that round "does not advertise that verifier as current
     conformance authority or renew its historical clean tally"
     (`b2f2efa:.ufo/waves/round-14/registry-home-rerun/integration.md`). The
     SCORECARD row cites a verifier its own round-14 record disclaims; the
     8/169/61 figures need a fresh run or a retired status.

D9. **Campaign D3 contract is absent.**
   - `grep -c 'SOURCES' CORPUS.md LEARNING.md templates/round-prompt.md PROTOCOL.md
     PROTOCOL-APPENDIX.md` -> 0 for every file.
   - `grep -ci 'mistake' CORPUS.md LEARNING.md templates/round-prompt.md PROTOCOL.md`
     -> 0 for every file.
   - `grep -ci 'research\|curat' templates/round-prompt.md` -> 0; the prompt has 5
     sections (`grep -c '^## '` -> 5) and no curation/research step.
   - `scripts/sources-census.sh` absent; `ls scripts` -> `shokunin-watchdog.sh` only.

D10. **Canonical protocol repo lags.**
   - `/home/vgpnk/Projects/kimi-shokunin` HEAD `bc7d690` (2026-10-13); fleet HEAD
     `31baf5c` (2026-10-19).
   - 5 of 6 protocol files differ (`cmp -s`; CORPUS.md is identical):
     PROTOCOL.md (6 added / 14 removed vs canonical, `git diff --no-index
     --numstat`), PROTOCOL-APPENDIX.md (0/3), AXES.md (7/51), MISSION.md (3/8),
     LEARNING.md (4/7). `templates/round-prompt.md` differs (11/35; fleet 4,920 B,
     canonical 3,356 B, `wc -c`). Total differing files in the D3/D5 set: **6**
     (`for f in ...; do cmp -s ...; done | wc -l` -> 6).
   - Canonical `skills/shokunin/SKILL.md` has 0 `SOURCES` hits, 0 multi-claim hits,
     0 mistake hits (`grep -c`), and canonical `templates/round-prompt.md` has 0
     research/curation hits.

D11. **Runtime state is tracked in git.**
   - `git ls-files .ufo/state | wc -l` -> 64; `git ls-files .ufo/watchdog.log | wc -l`
     -> 1. The appendix's "Tracked runtime" row recorded 16 state files at r10; the
     surface grew to 64. Known operator-side debt, not this lane's write scope.

D12. **Stray artifact from a failed redirect.**
   - `find . -maxdepth 1 -name 'bash*' -printf '%P|%y\n'` -> `bash: |d` (directory
     name ends with a space).
   - It contains `home/vgpnk/Projects/shokunin/souji-shokunin/tests/tools/
     souji-verify.sh: No such file or directory`, a 10,139-byte file whose name is
     the shell error message (`find "bash: " -maxdepth 8 -printf '%y|%p\n'`;
     `ls -la` on the tools dir).
   - Hidden from `git status` because the only descendant path matches the
     `*-shokunin/` ignore rule; not tracked.

## 6. Proposed round (for wave 2; 2 claims, distinct axes)

Round number: **16 by SCORECARD**, but the driver would launch 15 until the counter
is reconciled (D5). The round's Claim 2 includes that repair; do not let the driver
reuse 15. The lowest non-retired axis is protocol-soundness 8, so Claim 1 works it.

### Claim 1 - protocol-soundness (lowest axis): codify and propagate the corpus/source contract (campaign D3 + D5)

**What lands.** `CORPUS.md`, `LEARNING.md`, `templates/round-prompt.md` and the
`PROTOCOL.md` file-contract table gain the campaign D3 contract: a
`corpus/SOURCES.md` registry (append-only rows; `S###` ids; kind/tier/status
vocabulary; opened/recheck/used-by; counting commands), a mistake-mining section in
`corpus/lessons/round-<N>.md`, and a required research/curation step in the round
prompt with an output path and a row-count floor. The main-repo lane case is decided
explicitly: protocol and aggregator either get a root `corpus/SOURCES.md` or a
named registry section; the current text cannot leave D1 without a home (D6).
Canonical `kimi-shokunin` is brought to the same text (D5 deliverable, if wave 3 has
not already done it).

**Before -> after (counting commands):**
- Fleet docs naming the contract: `grep -lE 'SOURCES\.md|mistake mining|research
  step' CORPUS.md LEARNING.md templates/round-prompt.md PROTOCOL.md | wc -l` -> **0**
  before; **4** after.
- SOURCES facet: `grep -ci 'SOURCES\.md' CORPUS.md LEARNING.md
  templates/round-prompt.md PROTOCOL.md` -> `0 0 0 0` before; each >=1 after.
- Mistake facet: `grep -ci 'mistake' CORPUS.md LEARNING.md templates/round-prompt.md
  PROTOCOL.md` -> `0 0 0 0` before; each >=1 after.
- Research step: `grep -ci 'research\|curat' templates/round-prompt.md` -> **0**
  before; >=1 after.
- Canonical propagation: `for f in PROTOCOL.md PROTOCOL-APPENDIX.md AXES.md
  MISSION.md CORPUS.md LEARNING.md; do cmp -s "$f"
  "/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/$f" || echo "$f";
  done | wc -l` -> **5** before, plus
  `cmp -s templates/round-prompt.md
  /home/vgpnk/Projects/kimi-shokunin/templates/round-prompt.md || echo
  round-prompt.md` -> 1, total **6**; **0** after.
- Evidence recovery: `test -e .ufo/waves/round-14/registry-home-rerun/before.json`
  -> false before; true after restoring the 12 files from `b2f2efa` (or repointing
  Appendix:51 and LOG:749 to the recovery path). Count:
  `git ls-tree -r --name-only b2f2efa -- .ufo/waves/round-14/registry-home-rerun |
  wc -l` -> **12** recoverable.

**Falsifier.** Fails if any document names `SOURCES.md` without a lane path, row
schema and counting command; if the round prompt adds prose but no output artifact
or row-count floor; if the main-repo lane case is left implicit; if any of the 6
canonical files still differs after the claim; or if the round-14 evidence pointer
still targets an empty path.

**Verification.** Non-author reviewer (a fresh reviewer, not a subagent the lane
dispatched; `LEARNING.md` §Discernment) checks the before/after commands and reads
the new text. This is measurable and does not need an exploratory claim.

### Claim 2 - gate-integrity: restore the registry home and fail closed on counter/report collision and canonical drift

**What lands.** Restore the fleet-root `SCORECARD.md`/`LOG.md` from the last fleet
bytes (`0b1ac3b`) without losing any post-`0b1ac3b` content that belongs at root;
restore the protocol registry section above `## Aggregator lane` with the
`closure-check` row; reconcile `.ufo/state/protocol.round` to the last landed round
(15) so the next dispatch is 16; add a `round_counter_collision` probe to
`.ufo/waves/round-15/closure-check.py` (0 occurrences today) with a fixture where
`state + 1` already has a report; add a canonical-drift check that compares the D3
file set against `kimi-shokunin` and names every differing file.

**Before -> after (counting commands):**
- Registry row: `grep -cE '^\| closure-check \| gate \|' SCORECARD.md` -> **0**
  before; **1** after.
- Header identity: `head -1 SCORECARD.md` -> `# kotoba-shokunin — Scorecard` before;
  `# shokunin (main repo) — Scorecard` after.
- Collision: `n=$(cat .ufo/state/protocol.round); test -e
  ".ufo/reports/round-$((n+1))/protocol.md" && echo collision || echo clear` ->
  `collision` before; `clear` after (state reconciled to 15, next 16).
- Gate probe: `grep -c 'round_counter_collision' .ufo/waves/round-15/closure-check.py`
  -> **0** before; >=1 after; the new fixture must exit `1` on a planted collision
  and `0` on the clean fixture, and the selftest must stay at its recorded 27/27
  (or grow by exactly the new fixture count).
- Canonical drift: the same `cmp` loop as Claim 1 -> **6** differing before; **0**
  after the sync, or the gate reports the 6 names.

**Falsifier.** Fails if the registry row exists but its entry command does not
resolve at HEAD, if the header is still a lane header, if the collision probe
passes on the planted fixture, if the gate selftest count regresses, or if the
restored ledger drops a protocol/aggregator section that existed at `0b1ac3b`.

**Why these two and not three.** `AXES.md`: "two claims on one axis in one round
count as one claim." D3 and D5 are both protocol-soundness, so they are one claim
with two facets. A third claim on protocol-soundness would be the same claim; a
third on gate-integrity would merge with Claim 2. Two distinct axes is the correct
shape. D4 (`scripts/sources-census.sh`) is a fleet instrument for wave 2; this round
should consume it after it lands, not duplicate it.

## 7. Campaign deliverable fit (asked mapping)

| Campaign deliverable | Fits as | Axis | Counting command (before -> after) |
|---|---|---|---|
| SOURCES contract | Claim 1 | protocol-soundness 8 | `grep -lE 'SOURCES\.md' CORPUS.md LEARNING.md templates/round-prompt.md PROTOCOL.md \| wc -l` 0 -> 4 |
| Mistake mining | Claim 1 (same claim, separate measurement) | protocol-soundness 8 | `grep -ci 'mistake' CORPUS.md LEARNING.md templates/round-prompt.md PROTOCOL.md` 0 0 0 0 -> each >=1 |
| Research step in the round prompt | Claim 1 (same claim, separate measurement) | protocol-soundness 8 | `grep -ci 'research\|curat' templates/round-prompt.md` 0 -> >=1 |
| Canonical sync | Claim 1 propagation facet, or the wave-3 D5 writer; **not** a separate same-round claim | protocol-soundness 8 | `for f in ...; do cmp -s ...; done \| wc -l` 6 -> 0 |
| (prerequisite, not one of the four) registry-home/counter repair | Claim 2 | gate-integrity 9 | `grep -cE '^\| closure-check \| gate \|' SCORECARD.md` 0 -> 1; collision -> clear |

**Which new knowledge entries the claims serve.** No corpus entry can be admitted
until Claim 1 defines the main-repo corpus home. Two candidate entries (not written
this wave):
1. `protocol-round-counter-collision` - claim: the driver's `state + 1` collides
   with an existing report; source `scripts/shokunin-watchdog.sh:99-112`,
   `.ufo/state/protocol.round` = 14, `test -e` result; recheck: rerun the `test -e`
   command; clears `QUALITY.md` by being falsifiable with a command.
2. `registry-home-clobber` - claim: commit `31baf5c` replaced root
   `SCORECARD.md`/`LOG.md` with kotoba's HEAD bytes; source: SHA-256 equality and
   `git diff --numstat 31baf5c^ 31baf5c`; recheck: rerun both hashes; clears the bar
   the same way.

## 8. Conflicts (verbatim, for the canonical judge)

1. **Header identity.** `SCORECARD.md:1` current: `# kotoba-shokunin — Scorecard`.
   `0b1ac3b:SCORECARD.md:1`: `# shokunin (main repo) — Scorecard`. Same for
   `LOG.md:1` (`# kotoba-shokunin — Iteration Log` vs the fleet log at `0b1ac3b`).
2. **Registry home.** `PROTOCOL.md:384`: "For main-repo lanes (`protocol`,
   `aggregator`), it is the explicitly lane-owned registry section in root
   `SCORECARD.md`". `0b1ac3b:SCORECARD.md:25`: "§Gate standard's registry home for a
   main-repo lane remains unresolved."
3. **Protocol size.** `0b1ac3b:SCORECARD.md:25`: "`PROTOCOL.md` 470 lines plus
   `PROTOCOL-APPENDIX.md` 48 lines". Current `wc -l`: `513` and `51`.
4. **Round 14.** `0b1ac3b:LOG.md:749`: "round 14 protocol relaunch: registry-home
   cutover". `.ufo/reports/round-14/protocol.md`: "mid-move on the
   \"tracked-runtime\" axis item at ~63% context". `.ufo/waves/round-14/plan.md`:
   "protocol-soundness compaction".
5. **Round 15 closure.** `MANIFEST.json` entry 52: round 15, `in-flight`, closed
   `2026-09-29T00:34:00-03:00`. `.ufo/reports/round-15/protocol.md` exists and the
   SCORECARD records gate-integrity 9 from round 15. Entry 53's round 14 `failed`
   is the old attempt; the 2026-10-15 registry-home relaunch under the same number
   has no row.
6. **Next round.** `0b1ac3b:SCORECARD.md` §Planned: "Round 16". `.ufo/state/
   protocol.round`: `14` (driver next `15`). `.ufo/reports/round-15/protocol.md`
   exists.
7. **Round-14 evidence.** `PROTOCOL-APPENDIX.md:51` cites
   `.ufo/waves/round-14/registry-home-rerun/before.json`; the file and its three
   sibling citations are absent at HEAD (0 files). `e20f4fa` deleted 12 files /
   1,438 lines; the same 12 are present at `b2f2efa` (`git ls-tree`).
8. **The 470-line verifier.** `0b1ac3b:SCORECARD.md:25` calls the round-13
   two-file verifier "clean on 8 checks, obligation census 169/169, 61 anchors".
   `b2f2efa:.ufo/waves/round-14/registry-home-rerun/integration.md`: the
   "historical 470-line budget was already exceeded by the baseline 505-line
   body", and the round "does not advertise that verifier as current conformance
   authority or renew its historical clean tally".

## 9. Counts and commands (one line per count)

- Protocol lane rows: 0 at HEAD; 1 at `0b1ac3b` - `grep -cE '^\| closure-check \|'
  SCORECARD.md`; `git show 0b1ac3b:SCORECARD.md | grep -cE '^\| closure-check \|'`.
- Protocol reports: 14 - `find .ufo/reports -maxdepth 2 -name protocol.md | wc -l`.
- Marker reports: 2 - `wc -c .ufo/reports/round-13/protocol.md
  .ufo/reports/round-14/protocol.md` -> 275, 340.
- Protocol LOG entries at `0b1ac3b`: 4 - `git show 0b1ac3b:LOG.md | grep -c
  '^## .*protocol lane'`.
- Root ledger replacement: 165/395 and 1356/845 - `git diff --numstat 31baf5c^
  31baf5c -- SCORECARD.md LOG.md`.
- Round-15 evidence: 171 files, 25 fixtures, 2 frozen baselines - `find
  .ufo/waves/round-15 -type f | wc -l`; `find .ufo/waves/round-15/fixtures
  -mindepth 2 -maxdepth 2 -type d | wc -l`; `find .ufo/waves/round-15/frozen
  -maxdepth 2 -name expected.json | wc -l`.
- Gate hash: `0ac440f7...9a778c` - `sha256sum .ufo/waves/round-15/closure-check.py`.
- Appendix table lines: 44 - `grep -c '^|' PROTOCOL-APPENDIX.md`.
- Round-14 rerun dir: 0 files at HEAD, 4/4 cited files absent; 12 files / 1,438
  lines deleted by `e20f4fa`, recovered at `b2f2efa` - `find
  .ufo/waves/round-14/registry-home-rerun -type f | wc -l`; per-file `test -e`;
  `git show --stat e20f4fa -- .ufo/waves/round-14/registry-home-rerun`;
  `git ls-tree -r --name-only b2f2efa -- .ufo/waves/round-14/registry-home-rerun |
  wc -l` -> 12.
- Root missing lane files: 5 checks, all absent - `for f in corpus SKILL.md
  PROVINCE.md QUALITY.md SHONEN.md; do test -e "$f" || echo missing; done`.
- Axis-name mismatch: 0 AXES hits, 14 SCORECARD hits, 1 MISSION hit - `grep -c`.
- D3 gaps: 0 SOURCES, 0 mistake, 0 research - `grep -ci`.
- Canonical delta: 6 files - `cmp` loop plus the round-prompt `cmp`.
- Tracked runtime: 64 state files, 1 watchdog - `git ls-files | wc -l`.
- Stray file: 10,139 B - `wc -c "bash: /home/.../tools/souji-verify.sh: No such
  file or directory"` (path contains the literal error text).

## 9.5 Surfaces read (no writes)

- Root: `SCORECARD.md`, `LOG.md` (current and `0b1ac3b` blobs), `MANIFEST.json`
  (294 entries; protocol rows 44/45/52/53/55), `PROTOCOL.md`,
  `PROTOCOL-APPENDIX.md`, `AXES.md`, `MISSION.md`, `CORPUS.md`, `LEARNING.md`,
  `templates/round-prompt.md`, `scripts/shokunin-watchdog.sh`.
- Fleet evidence: `.ufo/reports/round-{1,3..15}/protocol.md` (14 files),
  `.ufo/waves/round-{13,14,15}`, `.ufo/l0-questions.md`, `.ufo/state/protocol.round`,
  `.ufo/waves/round-15/closure-check.py` and its fixtures/frozen dirs; `b2f2efa`
  and `e20f4fa` blobs for the round-14 evidence recovery/delete trail.
- Siblings: `kotoba-shokunin` HEAD blobs for the clobber hash comparison;
  `/home/vgpnk/Projects/kimi-shokunin` HEAD `bc7d690` plus
  `skills/shokunin/protocol/*`, `skills/shokunin/SKILL.md`,
  `templates/round-prompt.md`.
- No file outside `local://kaika-w1-protocol-state.md` was written.

## 10. Limits / not performed

- No gate re-execution: `closure-check.py` selftest (recorded 27/27), generator
  37/37, mutation 7/7, and `verify-protocol.sh` (8 checks, 169/169 census, 61
  anchors) are **recorded** claims; only static existence/hash/fixture counts were
  re-checked. The round-15 score remains cutoff-bounded (live smoke debt 10).
- No web research was assigned to this ticket; `SOURCES.md` rows written: 0. This is
  a STATE dossier, not an ART survey.
- The protocol lane has no lane corpus, so no `source:`/`verified-at:`/`recheck:`
  rows and no coverage-map/frontier rows exist to audit.
- No repo edits, git mutations, installs, commits, pushes, or canonical writes were
  made. The clobber and counter collision are reported, not repaired.
- Artifact path: `local://kaika-w1-protocol-state.md`.
