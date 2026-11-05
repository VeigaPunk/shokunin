# kumitate round 89 — receipt-bind v3: a scorer that tells the candidate which arm it is measuring

Lane `kumitate-shokunin`, hyaku run 15, **round 89 attempt 2**, Linux host, 2026-11-04.
Lane base `a5d2503393fc5646acb6468888d8b12a445bf62d`; freeze `adfc2f55675f760eaf8b59f80033f926500cd951`
(plan + 30-arm probe + 22 pre-data controls); wave spec/dispatch `9c3b64e44024869937a827d588fe1b75e6692ef7`;
integration **M = `7a8afb5fa02975e75cb2f33faf6d211a9680fc92`**; final lane tip `082f01a4db1ba4ddae67a155e9cf21ba3d3306f2`.
Attempt 1 of this round left only `.ufo/waves/round-89/open/census-start.txt` (no commit, no report); it is
reused as the attempt-2 round-start census and nothing else was inherited.

## Work performed

**Declared claim (1): C1 — operability, capability acquisition `receipt-bind` v3**
(contract `kumitate-receipt-bind-v3`). Operability is the lane's lowest non-retired axis (integer 9,
terminal under the frozen `f_O`); the stagnation nudge is active (saturation line 9, window N = 3, last
verified capability row `counter-receipt` v3 in round 86), so the round is a capability move.
Verdict: **UNMET** by the frozen kill rule — reported, not prettified. No second claim, no exploratory
claim.

- **Freeze.** `.ufo/waves/round-89/plan.md` (claim, 30 arms, kill rule, harm rules, limits) +
  `.ufo/waves/round-89/probe/probe89-c1.mjs` + 22 pre-data controls, committed at `adfc2f55`.
  The probe draws every fixture body, directory name, commit message and outside-directory name from a
  12-hex nonce at run time; the fixture repository holds three commits (A, B, C=HEAD), a staged body
  that differs from both HEAD and the worktree, a dirty worktree, an untracked instrument and a
  committed mode-120000 symlink.
- **Pre-data controls** (`controls/table.txt`, `controls/ctl-*.txt`): the do-nothing control (v2)
  **27/30** — failing exactly `alias-proc-root`, `bom-rev`, `symlink-instrument`; v2's worktree twin
  14/30; v1 19/30; blanket refusal 2/30; absent tool scored nothing; and **every one of the nine
  round-88 kill-rule constructions below terminal** (`c2-head-default` 24, `e2-index-default` 24,
  `ctl-abs-disk` 26, `d-fixture-gated-boundaries` 19, `f1-size-after-read` 26, `f4-textual-escape` 26,
  `f5-loose-limit` 26, `f6-dup-equal-ok` 26, `nogit-overfit` 17 of 30).
- **Instrument v3 landed** (`scripts/receipt-bind.mjs`, sha256 `37201ad0…`, contract
  `kumitate-receipt-bind-v3`; selftest 59 → **68** arms): real-path lane membership decided on the
  token's **parent** (so `/proc/self/root<lane>/scripts/x.mjs` is in-lane and an absolute in-lane
  *symlink* token is still seen as a link), `SYMLINK_INSTRUMENT` for a mode-120000 blob at the judged
  rev and for a symlinked external instrument, one leading U+FEFF stripped before field parsing, and
  the receipt read on one `O_NOFOLLOW` descriptor (`fstat` + read). The candidate is the wave's
  `K89ExecInst` output (`build/K89ExecInst/receipt-bind-v3.mjs`, `receipt-bind-v3.diff`), verified by
  the L1: `RECEIPT_BIND_SELFTEST: PASS held=68/68`, `C89_C1: HELD held=30/30`.
- **Corpus.** `corpus/SOURCES.md` +5 rows (S255–S258 admitted A/mined, S259 rejected B, 192 → 197);
  new entry `corpus/knowledge/receipt-lane-membership-and-link-binding.md`; `corpus/QUALITY.md` **Q82**
  (a scorer may not hand the candidate its own fixture's identity); lesson
  `corpus/lessons/round-89.md` (Method / Gate / four `## Mistakes` / Limits); README map rows for the
  new entry, the lesson and the round-88 spotcheck.
- **Routed-debt repairs landed** (from `K89ExecDebt`, verified by the L1): `scripts/spotcheck-adopt.mjs`
  `appendPin` indent + the stale `check-map-orphan` fixture (**selftest 33/34 → 34/34 PASS**);
  `.ufo/pins/counter-pins.json` `readme-map` re-pin (`COUNTER_PINS: CLEAN pins=45`); the round-88
  spotcheck's README row + `readme-map` covered entry (`README_MAP: CLEAN files=227 rows=227`);
  `scripts/omp-census.mjs` `config-pre` family widened for the operator's pre-edit copies
  (**`OMP_CENSUS: DRIFT findings=7 → 2`**, both residuals operator-owned, L0 filed).
- **Wave.** ONE v1 wave of **13 seats** under `ufo-wave-policy.json` (band 8–16): 4 executors, 2
  scribes, 1 scout, 1 reviewer, 2 critics, 1 mutation-tester, 1 sentinel, 1 connector; attack 4/13 =
  31 % under the dispatcher's own `ATTACK` set; 1 connector. Validated `READY_HANDOFF: READY … seats=13
  resumes=0 total=13 attack=4/13 connector=1`. **Dead seats: 4** — `K89ScribeSources`,
  `K89ScribeLesson`, `K89Critic` (opening narration only, no deliverable) and `K89Sentinel` (no report
  file; its harness and receipts were captured and reviewed by the L1, `w1/K89Sentinel.md`). No seat
  was replaced. The L1 holds the canonical §3 planner seat (the validator rejects `planner`).
- **Kill rule fired (the round's central finding).** Two seats independently constructed tools that
  reach `C89_C1: HELD held=30/30` while skipping claimed behaviour, and the L1 re-ran both:
  `build/K89Review/cand-probe-keyed.mjs` — computes nothing, reads the `--dir` basename
  (`<arm>-<12 hex>`) and prints that arm's expected verdict — and `build/K89Review/cand-skip-mode.mjs`
  — a blob-*shape* test instead of the git mode test plus a literal `/proc/self/root` prefix strip. A
  third seat (`K89Labrat`) built a label-only oracle that holds 30/30 over three nonce draws and two
  judged revisions, and proved the defect is the label by re-running its construction against a
  *labelless* probe copy of its own (4/30). The instrument is stronger than the scorer on inputs the
  scorer never drew: the reviewer's D1 (committed mode-120000 symlink with a space in its target) and
  D3 (in-lane instrument through a symlinked ancestor before a dirty worktree) read
  `SYMLINK_INSTRUMENT` / `CLEAN` on the integrated v3 where both constructions read `CLEAN` /
  `DRIFT external=1` (`build/K89Review/demos.txt`), and the v3 candidate closes an **absolute** in-lane
  symlink-token gap the probe has no arm for (`build/K89ExecInst/abs-symlink-check.txt`).
- **Stale-lane line.** Respawn-per-round driver; no other mission of this lane is open. The round
  opened 20:36 -03:00 (attempt 2) and completed inside one driver tick window; it was *progressing*
  throughout (lane commits `adfc2f55`, `9c3b64e4`, `7a8afb5f`, plus the seat artifacts under
  `.ufo/waves/round-89/`).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec): no
  untracked file names this lane or round 89. The only non-`.scratch` untracked entries at the fleet
  root are `.ufo/reports/round-60/souji.md` and a 24-byte file `after` from 2026-11-03 20:05 whose
  content ("== SCORECARD diff base-") names neither this lane nor this round — not mine, left in place
  and named here. `.ufo/reports/round-84/kama.md` is modified by another lane; untouched.
- **Tool installs.** None this round (no `uv`/`npx`/binary install, no pacman transaction — the pause
  stands).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| Plan + 30-arm probe + 22 pre-data controls + round-open gates | "Round 89" (freeze paragraph) | `adfc2f55675f760eaf8b59f80033f926500cd951` |
| w1 spec + validated dispatch + ready handoff + plan attack-set amendment | "Round 89" (wave paragraph) | `9c3b64e44024869937a827d588fe1b75e6692ef7` |
| `scripts/receipt-bind.mjs` v3 (68-arm selftest), S255–S259, knowledge entry, Q82, lesson, README map, SKILL rows, SCORECARD declaration + stanza re-pin, `spotcheck-adopt` + `omp-census` + `counter-pins` repairs, all 13 wave reports/artifacts, close runner | "Round 89" (landed-instrument, corpus and routed-debt paragraphs) | `7a8afb5fa02975e75cb2f33faf6d211a9680fc92` (M) |
| Close battery receipts at M + measured disposition | "Round 89 — measured disposition" | `082f01a4db1ba4ddae67a155e9cf21ba3d3306f2` |

Every change above is inside `kumitate-shokunin`; nothing was pushed anywhere but the lane remote and
the fleet repo. Domain source trees were read only.

## Before → after measurements

One claim, one counting command (frozen before data, `.ufo/waves/round-89/plan.md`):

```
node .ufo/waves/round-89/probe/probe89-c1.mjs --lane <LANE> --work <SCRATCH> --rev <REV>
```

| reading | value | receipt |
|---|---|---|
| **before** (do-nothing: committed v2 at base `a5d2503`) | `C89_C1: UNMET held=27/30` exit 1, failing `alias-proc-root`, `bom-rev`, `symlink-instrument` | `controls/ctl-base-v2-at-rev.txt` |
| **after** (M = `7a8afb5f`) | `C89_C1: HELD held=30/30` exit 0, twice, byte-identical (`PROBE_DETERMINISM SAME`) | `close/probe1.txt`, `close/probe2.txt` |
| worktree twin at M | `C89_C1: UNMET held=15/30` exit 1 | `close/twin.txt` |
| instrument selftest | `RECEIPT_BIND_SELFTEST: PASS held=68/68` (59 at base) | `close/bind-selftest.txt` |
| close receipts | `RECEIPT_BIND: CLEAN matched=18 mismatched=0 unchecked=0 external=1` over the 18 receipts at that run, every receipt counted (`BIND_CASE … ALL`; a later re-run reads 19 because the receipt is itself a receipt) | `close/bind.txt` |
| **kill rule** | **fired**: three seat-constructed controls at 30/30 (`cand-probe-keyed`, `cand-skip-mode`, labrat's label-only oracle) | `build/K89Review/probe-cand-probe-keyed.txt`, `probe-cand-skip-mode.txt`, `build/K89Labrat/` |
| proxy | `PROXY: MATCH --strict` (C2 224 → 227, `pin.receipt-bind` re-pinned) | `close/proxy.txt` |
| checklists | `CHECKLIST: 43/46 pass` at M (36/46 at open; reds 723, 725-at-open, 737, 741, 746, 748, 755, 756 — the spotcheck-adopt repair turned 746/748 green) | `close/checklists.txt` |
| sources | `SOURCES_CHECK: CLEAN rows=197`; `SOURCE_CAPTURE: CLEAN captures=86`; census exit 0 | `close/sources-check.txt`, `close/source-capture.txt`, `close/census.txt` |
| plan-before-ready / ready-handoff | `close/plan.txt`, `close/ready.txt` (both committed receipts) | — |

**Verdict: C1 UNMET — rejected-honest-stop, no capability row.** The frozen kill rule is written
against the scorer's score, and the scorer is an output-text oracle that names its own arms. Axes:
operability 9 unchanged; every coverage row 10 unchanged; no axis harmed.

## Sources & frontier

`SOURCES.md` rows **192 → 197** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`);
tier histogram A=165 B=22 C=10, status `queued` 13 / `mined` 156 / `rejected` 28.

- Rows added by tier: **A 4** (S255 `proc_pid_root(5)`, S256 POSIX `realpath(3)`, S257 `gitformat-index`,
  S258 The Unicode Standard 15.0 ch.3 — all `mined`, `used-by`
  `corpus/knowledge/receipt-lane-membership-and-link-binding.md`); **B 1 rejected** (S259 `git-ls-tree`,
  reason + flip recorded in the row and in the lesson's `## Gate`).
- Rows touched old→new: **none** — no existing `status`, `recheck` or `used-by` cell changed this round
  (so no old→new log line is owed).
- Frontier rows advanced: the lane's own instrument ground (operability), not a corpus frontier band —
  `corpus/README.md` `## Frontier` unchanged; the round's expansion credit is 0 new admitted
  `knowledge/` entries on uncovered ground (the new entry deepens the existing receipt-binding band,
  which is core ground since round 87).
- Census before → after (`scripts/sources-census.sh validate --root … kumitate`): at round start
  `exit 0`, `kumitate ok …/corpus/SOURCES.md` with 7 pinned `W04` duplicate-url warnings
  (`open/census-start.txt`); at round end the same command exits 0 with the same 7 `W04`
  (`close/census.txt`).
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kumitate` was not adopted (the claim,
  the probe investigation and the routed-debt repairs filled the round); `considerthese/2026-10-26.md`
  (latest) re-checked — ideas 1/2/3/4/6 are already implemented as Q75/Q76/Q68/Q69/Q72, idea 5 is
  outside this province.

## Trend verdicts

- **expansion — unchanged.** No admitted `knowledge/` entry on ground the coverage map did not hold
  (the new entry deepens the existing receipt-binding band), no frontier band moved into core, no
  capability row (the claim is UNMET), assimilation none. +4 admitted source rows and +1 rejection in
  bands the map already holds are curation, not expansion.
- **quality — improved.** Independently visible: the instrument gained real-path membership, a
  mode-120000 refusal and BOM tolerance, its hermetic suite grew 59 → 68 arms, and two gate repairs
  turned red suites green (`SPOTCHECK_ADOPT_SELFTEST: PASS (34/34)`, was 33/34; `COUNTER_PINS: CLEAN`,
  was 1 bad pin; `README_MAP: CLEAN`, was 4 findings; `OMP_CENSUS` findings 7 → 2 with the two
  residuals operator-owned). Tempered: the capability is UNMET, so this is instrument and gate quality,
  not a capability.
- **discernment — improved.** The lane honoured its own frozen kill rule against its own 30/30
  predicate, recorded the three constructions that fired it, wrote the failure into **Q82** as a
  grounded criterion instead of narrowing the rule, and recorded four dead seats with no credit. The
  non-author agree/disagree on this round's gate decisions is the closure's.

## SHONEN

`grep -c '^- \[' SHONEN.md` → 4 boxes; one line per box, `[~]` = asserted by the author with a pointer.

- [~] **Box 1 — SKILL.md decision tables, error patterns, checklists, cited sources:** the gate
  registry row for `receipt-bind` is v3 now (`SKILL.md` registry row, contract
  `kumitate-receipt-bind-v3`) and checklist item "Receipt-subject binding" names the 68-case suite and
  the round-89 frozen scorer; every new token cites S255–S258 through
  `corpus/knowledge/receipt-lane-membership-and-link-binding.md`.
- [~] **Box 2 — at least one end-to-end domain task executed and logged:** `LOG.md` "Round 89" records
  the freeze, the instrument integration, the corpus and the routed-debt repairs, and the close battery
  at M (`close/*.txt`, 17 receipts bound).
- [~] **Box 3 — instructions executable without oral context:** `corpus/lessons/round-89.md` and the
  knowledge entry carry the commands and the located quotes; the probe's own header documents its
  fixtures (with the one stale sentence disclosed in the lesson's `## Mistakes`).
- [~] **Box 4 — no cross-domain bleed, PROVINCE.md accurate:** the round touched only this lane's own
  instrument, corpus and pins; the connector's sibling scan found only adjacent, not absorbed, ground
  (`w1/K89Connector.md`); no `PROVINCE.md` edit was needed and none was made.

Promotion stays operator-owned; no box is marked `[x]` because no named non-author verifier has
reviewed this round yet.
