# kaika W1 — kengaku-shokunin STATE dossier

Lane: `kengaku` — LLM/model research & evaluation. Repo:
`/home/vgpnk/Projects/shokunin/kengaku-shokunin` (read-only in this wave).
Measured 2026-10-19 against `master` @ `99cf615ca730293ae82a9f0a6d15169b5ac08863`
(clean worktree, `git status --porcelain | wc -l` → 0; `git rev-list --count
origin/master..master` → 0).

Method: lane-internal read of git objects, tracked files, frozen tables and
receipts; `test -e` on declared host paths; `ss -ltn 'sport = :34113'` (no
listener); one read-only `python3 plans/attrib_probe.py block-sha --frozen
plans/attrib-r23-frozen.md` (exit 0); one `--help` on the census probe. No web
research was needed for this shape, so no `SOURCES.md` rows and no tiers are
created here. No live target traffic, no installs, no repo writes besides this
artifact. `grader.py` was **not** re-run (no re-run to decorate a report); its
last recorded verdict is cited with its round. The full round-16 61-citation
sweep was not repeated; two live instances were spot-checked (D09, D14).

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| Domain | LLM/model research & evaluation | `MANIFEST.json` roster entry `kengaku`; `PROVINCE.md:1` |
| Rank | **shonen** (not promoted) | `MANIFEST.json` roster `"rank": "shonen"`; no promotion record in fleet `rounds[]` |
| Branch / HEAD | `master` / `99cf615ca730293ae82a9f0a6d15169b5ac08863` | `git branch --show-current`; `git rev-parse HEAD` |
| Last admitted round | **22** | `SCORECARD.md:519` §Round 22; `LOG.md:184` §Round 22; evidence commit `8a08483`, records commit `407156f` |
| Fleet ledger | fleet round 25 maps `lane_rounds.kengaku = 22`, `closed_at 2026-10-16T13:25:00Z` | `MANIFEST.json` `rounds[]`; max over all kengaku lane records = 22 |
| Next number | **23** to record the executed-but-unadmitted round 23; **24** only after 23 is recorded | round-17 precedent: a blocked attempt consumed 17, the next round was 18 |
| Promotion checklist | 4 boxes `[~]`, 0 boxes `[x]` | `grep -c '\[~\]' SHONEN.md` → 4; `grep -c '\[x\]' SHONEN.md` → 0 |

### Round 23 is executed and unadmitted

This is the largest identity fact of the lane, and the fleet hint ("max
recorded round 22") is **confirmed** against the lane's own records:

- Registered at the close of round 22 as the next move: "r23 registered:
  opencode-go forcing via the stream-path header leg-selection"
  (`SCORECARD.md:543-545`; `LOG.md:197-199`).
- Work exists: WIP commits `a2ff634` (instrument/draft), `f9337d5` (two stream
  receipts), `6f31d23` (v3 frozen table). The v3 table is `plans/attrib-r23-frozen.md`,
  `FROZEN: 2026-10-16T13:45:47Z sha256:1b2d6a01bfa431ec4e78bf89fd989f9ad500d10bb78634362a3c0e3bce794f87`; the pin reproduces today
  (`block-sha` exit 0).
- Scored receipt: `corpus/evidence/attrib-r23-stream.log` — 30 stream trials
  `13:46:41–13:49:28Z`; `ACCURACY: 30/30 = 1.000` (`:234`); `GT counts:
  {"alibaba-token-plan": 6, "hyper": 24}` (`:233`); target clause
  `STREAM TARGET opencode-go: on-target GT n=0 ... -> FAIL` (`:239`).
- But: `grep -cE '^#+ .*23' SCORECARD.md LOG.md` → `0` and `0`; no
  `.ufo/reports/round-23/kengaku.md` in the lane or the fleet repo; fleet
  `MANIFEST.json` has no kengaku `lane_rounds = 23` record. Only drafts exist
  under `.ufo/rounds/round-23/goal-wave/` (3 files, 60,078 B, with 12
  `[PARENT:` placeholders in the verdict draft).

Consequence: the lane's last **admitted** round is 22; the last **executed**
round is 23, and its target claim failed. Under `AXES.md` ("A round is admitted
only if every claim verifies"), round 23's honest disposition is a recorded
NOT-ADMITTED/honest-stop, not silence. The draft itself says: "the coverage
clause is NOT MET (opencode-go 0 on-target)" (`.ufo/rounds/round-23/goal-wave/log-entry-draft.md`).

---

## 2. Axes

The lane records numeric scores only through round 14; rounds 15–22 record
verdicts, not numbers. The table below is the last numeric state, with the
post-r14 verdicts so wave 2 can see the drift between the two conventions.

| Axis | Last numeric | Pointer | Post-r14 verdicts |
|---|---|---|---|
| novelty *(owned)* | **7** | `SCORECARD.md:162` (r14) | r21 improved; r19/r20/r22 unchanged |
| calibration *(owned)* | **8** | `SCORECARD.md:163` (r14, held for the r12/r13 breach) | r19 improved; r20 improved; r21/r22 unchanged |
| depth | **9** | `SCORECARD.md:168` (held, anti-double-count) | r19/r20/r21/r22 improved |
| coverage | **7** | `SCORECARD.md:165` (held by the unresolvable-surface cap) | r19/r20 improved narrowly; r22 improved |
| operability | **8** | `SCORECARD.md:164` | r21 improved narrowly; r22 improved |
| freshness | **8** | `SCORECARD.md:166` | r19/r20/r21/r22 improved narrowly |
| adjacency | **8** | `SCORECARD.md:167` | unchanged in all four |

- **Lowest non-retired axis:** coverage **7** tied with novelty **7**
  (`SCORECARD.md:162,165`). Retired: none (`SCORECARD.md:266-273`).
- **Obligation status:** r21 (novelty) and r22 (coverage) name a tied-lowest
  axis; r19 and r20 claim only calibration (8) and neither names the lowest
  axis or a stagnation waiver (`SCORECARD.md:416-482`). That is a protocol
  defect, not a score judgement (M16).
- **Saturation line / stagnation window N:** not declared. Exact text:
  "The lane's saturation line + stagnation window N are to be declared by the
  lane on its next round per `AXES.md` §The stagnation nudge; not asserted by
  this conformance change." (`SCORECARD.md:555-557`).
- **Capabilities:** **0 rows** — the table is the placeholder
  "— none yet —" (`SCORECARD.md:547-553`). r21/r22 demonstrated a running
  capability (blind leg attribution, then forced-fallback coverage); the table
  should have been backfilled, and the placeholder says rows enter only through
  a demonstrating round.
- **Planned claims:** stale. `SCORECARD.md:252-264` still says "The round-13
  re-dispatch selects **coverage (7)**, tied with novelty (7)" and prescribes a
  source-availability inventory; the actually registered next round is r23
  stream-path coverage (`:543-545`). The `planned` field therefore does not
  describe the next round's claims.
- **Move log:** one row only, round 16 (`SCORECARD.md:363-367`).
- **Confidence:** contains a stale check count — "All 149 checks recompute"
  (`SCORECARD.md:305`) against `733 checks` at `:164` and `CHECKS n=733` at
  `:198`. Round-16 audit named the same line as `:302`; it moved, not fixed.

Numeric-score caveat: because r19–r22 recorded verdicts instead of scores, a
reader cannot re-derive whether coverage/novelty are still 7 or whether the
"improved" verdicts were meant to be +1. Any wave-2 claim that touches the
lowest axis must first re-derive the number (C2).

---

## 3. Corpus

All commands run from the lane root on 2026-10-19.

| Measure | Value | Command |
|---|---|---|
| knowledge files | **27** | `ls corpus/knowledge/*.md \| wc -l` |
| knowledge index rows | **24** | `grep -c '^| `knowledge/' corpus/README.md` |
| lessons files | **24** | `ls corpus/lessons/*.md \| wc -l` |
| lessons index rows | **19** | `grep -c '^| `lessons/' corpus/README.md` |
| evidence dirs / rows | **12 / 12** | `find corpus/evidence -mindepth 1 -maxdepth 1 -type d \| wc -l`; `grep -c '^| `evidence/' corpus/README.md` |
| root evidence logs | **28, 0 indexed** | `ls corpus/evidence/*.log \| wc -l`; per-file `grep -qF` loop → 0 |
| plans files / index refs | **8 / 0** | `ls plans/ \| wc -l`; `grep -c 'plans/' corpus/README.md` |
| `QUALITY.md` | **absent** | `test -e corpus/QUALITY.md` → false |
| `SOURCES.md` | **absent** (wave-2 artifact) | `test -e corpus/SOURCES.md` → false |
| coverage-map rows | **11** | `awk '/^## Coverage map/{f=1;next}/^## /{f=0}f&&/^- /{c++}END{print c}' corpus/README.md` |
| `## Frontier` rows | **0** (heading absent) | `grep -c '^## Frontier' corpus/README.md` |
| open-gap rows | **12** | `awk '/^## Open gaps/{f=1;next}/^## /{f=0}f&&/^- /{c++}END{print c}' corpus/README.md` |

Unindexed knowledge (3): `attrib-prior-art-r21.md`, `attrib-r21.md`,
`probe-battery-r19.md`. Unindexed lessons (5):
`2026-10-16-round19-freeze-chain.md`, `2026-10-16-round20-grid-closure.md`,
`2026-10-16-round21-attribution-freeze-surface.md`,
`2026-10-16-round22-leg-coverage-forcing.md`,
`2026-10-16-round23-stream-surface.md`.

### Header / gate contract

| Field | Compliance | Command |
|---|---|---|
| `source:` first-line field | **0/27** | `grep -lE '^source:' corpus/knowledge/*.md \| wc -l` |
| `verified-at:` | **0/27** | `grep -lE '^verified-at:' corpus/knowledge/*.md \| wc -l` |
| `recheck:` | **12/27** | `grep -lE '^recheck:' corpus/knowledge/*.md \| wc -l` |
| all three (full triad) | **0/27** | per-file loop on the three patterns |
| lessons `## Gate` | **1/24** | `grep -lE '^## Gate' corpus/lessons/*.md \| wc -l` (only `round-13-coverage.md:24`) |
| lessons named `round-<N>.md` | **11/24** | `ls corpus/lessons/ \| grep -cE '^round-[0-9]+\.md$'` |

The 12 `recheck:` commands carry **no date or cadence** (0 matches for a
`YYYY-MM-DD` in those lines), so none is "overdue by date"; the fields
themselves are the defect. Every one of the 12 roots is absent today:

```
for p in ~/Projects/webzites/repos/llm-wiki ~/archive/bench-arena \
         ~/bench-arena ~/.bailian ~/Projects/bounties/ledger/telemetry.jsonl; do
  test -e "$p" && echo "present $p" || echo "absent $p"; done
# → all five absent
```

Additional declared surfaces (today): `~/.config/systemd/user/qwen-coder.service`
absent; `~/.config/llama/qwen-coder-godspeed.jinja` absent; no listener on
`:34113`; `~/.local/share/ds-flash-shim/shim.py` **present**, sha256
`42d86d99…` (byte-matches the r22/r23 pins). `grader.py` and every
`corpus/evidence/round*/` tree are present.

`PROVINCE.md` (9 surface rows; `grep -c '^| [A-Z]' PROVINCE.md` → 10 including
the header): **6 of 9 rows cite at least one path absent today** — wiki,
bench-arena, `:34113` + unit + template, ledger, `~/.bailian` (two rows).
Rows 7 (own probe artifacts) and 8 (in-repo gate) resolve; row 9 (public
literature) is URL-based and was not fetched. The header says "re-verified
round 14, 2026-09-29" (`PROVINCE.md:8`) while the round-13 receipt and today's
`test -e` disagree. That is a live dead-pointer defect (D09), already named in
`corpus/lessons/round-16-recensus.md:21-40`.

---

## 4. Mistakes mined

Class key: PRED = prediction/ordering; LAND = landing/durability; MEAS =
measurement/instrument; PROC = process/role; STOP = honest-stop/gap; DISC =
discernment gate. "Captured" is a sweep of the lane's own rules: `SKILL.md`
(`grep -ic` in parentheses) and `corpus/QUALITY.md` (absent → **0 criteria**).

| ID | Class | Mistake and evidence pointer | Captured by | Proposed criterion (when none) |
|---|---|---|---|---|
| M01 | PRED | r8 ran 78 jobs with no ex-ante predictions (`SCORECARD.md:277`; `lessons/round-8.md`) | SKILL anti-pattern 4 (`:75`) + checklist item 1 (`:558`) | — |
| M02 | LAND | r9 count `0/12` falsified as `0/17`; `LOG.md:9` rewritten in place (`lessons/round-9.md`; `SCORECARD.md:75`) | Not captured: `grep -ic 'append-only' SKILL.md` → 0 | Corrections are new entries; every count carries its command |
| M03 | LAND | r8 landed `results.jsonl` was a `raw`-stripped working copy (`SCORECARD.md:280-288` confidence) | SKILL anti-pattern 14 (`:127`) + rule 9 (`:429`) | — |
| M04 | MEAS | first `grader.py` failed its own M0 control (bogus predicted-vs-observed check); fixed by a preregistration anchor (`SCORECARD.md:133`; `evidence/round10-fleet/INTEGRATOR-NOTES.md`) | SKILL anti-pattern 13 (`:120`) | — |
| M05 | LAND | r12/r13 produced but did not commit/index/log; calibration held at 8 (`SCORECARD.md:163`; `lessons/round-14.md`) | Partial: rule 9 says land bytes; `grep -ic 'index parity' SKILL.md` → 0 | A round closes only when LOG + SCORECARD + index rows + report exist |
| M06 | PROC | r16 probe was spawned as a nested child by a seat, forbidden by the leaf contract; recorded and not relied on (`lessons/round-16-recensus.md:15-19`) | Not captured: `grep -ic 'leaf' SKILL.md` → 0 | Lane-dispatched children can advise, never supply evidence |
| M07 | STOP | r17 blocked at route admission, 0 native dispatches, 0 verified-round credit (`SCORECARD.md:369-414`; `.ufo/round-17/route-blocker.json`) | Protocol-level; lane recorded zero credit | Keep: blocked attempt = explicit zero credit |
| M08 | PRED | r19 BR-1: first freeze raced an author re-base (compute-then-write TOCTOU); repaired by re-freeze after double-read (`SCORECARD.md:426-431`; `plans/probe-battery-r19.md`) | Partial: anti-pattern 5 (`:80`) says freeze before scored runs; `grep -ic TOCTOU SKILL.md` → 0 | Double-read stability guard + re-freeze before the first dependent request |
| M09 | PROC | r19 runner-leg-opencode sent two live requests before the battery existed; self-filed and excluded (`SCORECARD.md:435-437`) | Not captured: `grep -ic 'pre-battery' SKILL.md` → 0 | No live request before the frozen battery file exists |
| M10 | LAND | r20 `git-add` pathspec error left scorer §10 + template + lesson uncommitted; repaired `96b8962` (`LOG.md:178-180`) | Not captured: `uncommitted` appears once, not as a rule | Commit explicit paths; verify `git status` at close |
| M11 | MEAS | r21 three matcher defects, fixed pre-adjudication and recorded (`SCORECARD.md:483-518`) | Partial: anti-pattern 13 (`:120`) | Matcher mutation battery before scoring |
| M12 | STOP | r22 opencode-go forcing starved (0 on-target) and 4 seats were lost; gap named, not redefined (`SCORECARD.md:519-546`) | Not captured: no forcing pre-flight rule | Pre-flight a forcing mechanism against the target model class; name lost seats |
| M13 | PRED | r23 scratch-driver trials (13:38–13:39Z) predate the v3 freeze (13:45:47Z) and ran under v2; unscored characterization (`.ufo/rounds/round-23/goal-wave/scorecard-verdict-draft.md:307`) | Same gap as M08 | Tag pre-freeze runs as unscored; never cite them as coverage |
| M14 | LAND | r23 executed (scored 30/30, target FAIL) but no LOG/SCORECARD section, no report, drafts with 22 `[PARENT:` slots (`grep -cE '^#+ .*23'` → 0/0) | Not captured | Every executed wave gets a LOG entry even on FAIL (r20 P9 precedent) |
| M15 | DISC | No outside non-author spot-check has ever run; `QUALITY.md` absent; r19–r22 all say "discernment unchanged" (`lessons/round-13-coverage.md:42-45`) | Not captured: `grep -ic 'non-author' SKILL.md` → 0 | `QUALITY.md` bar + a named non-author spot-check of one admit and one reject per round |
| M16 | PROC | r19/r20 claim calibration (8) while coverage/novelty sat at 7; no stagnation waiver recorded (`SCORECARD.md:416-482`; `AXES.md` lowest-axis clause) | Not captured: SKILL has no round-contract section | Round header records the chosen lowest axis and any tie-break/waiver |
| M17 | LAND | r16 audit found 61 live citations to deleted paths; named debt remains in `PROVINCE.md:12-17` and `SCORECARD.md:305` (`lessons/round-16-recensus.md:21-40`) | Partial: ledger is marked historical in SKILL (`:237-242`); no province rule | Mark absent surfaces in `PROVINCE.md` in the same round |
| M18 | PROC | `SHONEN.md` evidence blocks are multi-line prose; canonical form allows one indented evidence line per box; 0 `[x]` (`SHONEN.md:5-12`; `PROTOCOL.md` file contract) | Protocol form; no lane rule | Regenerate verbatim; one evidence line per box |

What is already well captured (do not re-teach): prediction ordering (M01),
freezing the harness (M08 partial), mutation-testing graders (M04/M11),
deriving every stored SUMMARY from committed bytes (M03), landing run bytes
(M03), paired contrasts and ordered tests (SKILL rules 10–11, `:433-450`),
absorbing critic defects pre-hash (rule 13, `:460`). The recurring uncaptured
family is **closure/landing** (M05, M10, M14, M17) and **discernment** (M15).

---

## 5. Contract defects

| ID | Defect | Evidence (command → result) |
|---|---|---|
| D01 | `corpus/QUALITY.md` absent; the learning path's quality gate has no bar | `test -e corpus/QUALITY.md` → false; `CORPUS.md` layout and `LEARNING.md` require it; named debt since `lessons/round-9.md` and `SCORECARD.md:397` |
| D02 | Knowledge entries do not open with `source:` / `verified-at:` / `recheck:` | 0/27, 0/27, 12/27 (commands in §3) |
| D03 | Lessons do not carry `## Gate` | 1/24 |
| D04 | Lessons deviate from `round-<N>.md` naming | 11/24 exact |
| D05 | Index parity broken both ways | knowledge 24 rows vs 27 files; lessons 19 vs 24 |
| D06 | 28 root-level evidence logs are unindexed (the README table covers only dirs) | `ls corpus/evidence/*.log \| wc -l` → 28; loop → 0 indexed |
| D07 | `plans/` is unindexed, including the headline frozen tables r19/r21/r22/r23 and `attrib_probe.py` | `ls plans/ \| wc -l` → 8; `grep -c 'plans/' corpus/README.md` → 0 |
| D08 | `corpus/README.md` has no `## Frontier` section | `grep -c '^## Frontier' corpus/README.md` → 0 |
| D09 | `PROVINCE.md` has no Core/Frontier/Adjacent sections and 6/9 surface rows cite absent paths; header still says re-verified 2026-09-29 | `grep -nE '^#+ .*(Core\|Frontier\|Adjacent)' PROVINCE.md` → none; `test -e` on rows 12–17 roots → absent; `PROVINCE.md:8` |
| D10 | Axis scores are numeric only through r14; r19–r22 are verdict-only; move log has one row | `SCORECARD.md:162-168`; `:363-367`; `:416-558` |
| D11 | Capabilities table empty although r21/r22 demonstrated a running capability | `SCORECARD.md:547-553` |
| D12 | Saturation line and window N undeclared | `SCORECARD.md:555-557` |
| D13 | `planned` field stale (round-13 coverage text) while r23 is the registered next round | `SCORECARD.md:252-264` vs `:543-545` |
| D14 | Confidence section still says "All 149 checks" against 733 elsewhere | `SCORECARD.md:305` vs `:164`, `:198` |
| D15 | Round reports for 19–22 exist only lane-local; the canonical fleet report path is absent | `ls kengaku-shokunin/.ufo/reports/` → only `round-17`; `MANIFEST.json` cites `kengaku-shokunin/.ufo/rounds/round-22/kengaku.md`; `PROTOCOL.md:138` names `.ufo/reports/round-<N>/<id>.md` |
| D16 | Round 23 is unrecorded: no LOG/SCORECARD section, no report; WIP commits a2ff634 / f9337d5 / 6f31d23 are tracked but unindexed; drafts carry 22 `[PARENT:` occurrence slots (12 in the verdict draft) | `grep -cE '^#+ .*23' SCORECARD.md LOG.md` → 0/0; `.ufo/rounds/round-23/goal-wave/` |
| D17 | `SHONEN.md` violates canonical form (multi-line evidence per box) and has no `[x]` verifier | `SHONEN.md:5-12`; `PROTOCOL.md` SHONEN seed block and marks clause |
| D18 | `SKILL.md` frontmatter lacks the contract's quoted triggers, anti-trigger and sibling-arbitration note | `SKILL.md:1-5`; `PROTOCOL.md` file contract row `SKILL.md` |
| D19 | Lane round 18 (2026-10-15 digest landing) has no SCORECARD section and no `MANIFEST.json` lane_round record; it exists only in LOG and one knowledge/evidence pair | `LOG.md:85-135`; `MANIFEST.json` kengaku `lane_rounds` jump 16 → 19 |

Held, not defects (reported so wave 2 does not chase them):

- Worktree clean and pushed (`git status --porcelain` 0; `origin/master..master` 0).
- `.ufo/interactive-sessions/` (3 files) is gitignored; no `__pycache__` on disk.
- `corpus/evidence/` dirs and `grader.py` resolve; `coverage_census.py --help` exits 0.
- Bloat is real but not a correctness defect: `LOG.md` 51,906 B / 206 lines /
  longest line 8,679 chars; `SCORECARD.md` 65,792 B / 558 lines; `SKILL.md`
  51,245 B / 640 lines; `grader.py` 274,855 B / 5,737 lines; 277 tracked files,
  6.66 MB (`git ls-files -z | xargs -0 wc -c`). The long LOG lines are the
  practical cost: one entry is one paragraph, so diffs and citation by line are
  brittle.

---

## 6. Proposed round

Shape: 3 claims on distinct axes; claim 1 satisfies the lowest-axis obligation
(coverage 7, tied with novelty 7). Each claim is causally separable: records,
scores, and quality bar can land independently.

### C1 — coverage (lowest, 7): put the executed rounds into the lane's own index

The lane ran 19, 20, 21, 22 and 23; only their evidence exists, not their
index/record surface. Precedent for a coverage claim that holds at 7 under the
unresolvable-surface cap: `lessons/round-13-coverage.md` ("the coverage anchor
remains 7 under the existing declared-but-unresolvable-surface cap").

Before → after (pasteable):

```bash
# knowledge rows / files: 24/27 -> 27/27
grep -c '^| `knowledge/' corpus/README.md; ls corpus/knowledge/*.md | wc -l
# lessons rows / files: 19/24 -> 24/24
grep -c '^| `lessons/' corpus/README.md; ls corpus/lessons/*.md | wc -l
# root evidence logs: 0/28 -> 28/28
for f in corpus/evidence/*.log; do grep -qF "$(basename "$f")" corpus/README.md && echo x; done | wc -l
# plans rows: 0/8 -> 8/8
grep -c 'plans/' corpus/README.md
# records: 0 -> 1 in each
grep -cE '^#+ .*23' LOG.md SCORECARD.md
test -e .ufo/reports/round-23/kengaku.md && echo present
```

Do not inflate the verdict: coverage stays **7** while 6/9 `PROVINCE.md` rows
are unresolvable; record `improved narrowly` + the cap, exactly as r13 did.
This claim needs no `SOURCES.md` rows.

### C2 — calibration (8): make scores re-derivable and adjudicate round 23

Two things currently cannot be re-derived: the post-r14 axis numbers and
round 23's disposition. Both are calibration failures by `AXES.md`.

Before → after:

```bash
# numeric axis rows with a command, post-r14: 0/7 -> 7/7
# (target rows use the plain `| axis | score | ...` shape)
grep -cE '^\| (novelty|calibration|depth|coverage|operability|freshness|adjacency) \| [0-9]+' SCORECARD.md
# round-23 record: 0 -> >=1 in each
grep -c 'Round 23' LOG.md SCORECARD.md
# disposition line: 0 -> 1
grep -cE 'NOT-ADMITTED|not admitted' LOG.md
```

Required content: re-derive each axis from its rubric (±1 per verified claim),
or explicitly mark the axis "verdict-only, no numeric"; record r23 as
NOT-ADMITTED with the receipt's `opencode-go n=0 -> FAIL` (`attrib-r23-stream.log:239`);
declare the saturation line and window N (`SCORECARD.md:555-557` requires this
on the next round). Do not invent r19–r22 numbers the rubric cannot reproduce.

### C3 — depth (9): create the missing quality bar and admit one entry under it

`QUALITY.md` is the learning path's second step and has never existed. Mine it
from the 18 mistakes above; each criterion cites the lesson that produced it and
the sweep command that tests it. Then admit the r23 stream-mechanism fact as the
first entry that clears the bar (the mechanism is already pinned in
`plans/attrib-r23-frozen.md` and `corpus/evidence/attrib-r23-stream.log:1-12`).

Before → after:

```bash
test -e corpus/QUALITY.md && grep -cE '^- \*\*' corpus/QUALITY.md   # absent/0 -> present/>=8
# full-triad knowledge entries: 0/27 -> 1/28 (new entry: source, verified-at, recheck)
for f in corpus/knowledge/*.md; do
  s=$(grep -cE '^source:' "$f"); v=$(grep -cE '^verified-at:' "$f"); r=$(grep -cE '^recheck:' "$f")
  [ "$s" -gt 0 ] && [ "$v" -gt 0 ] && [ "$r" -gt 0 ] && echo "$f"
done | wc -l
```

The entry's `recheck` can be reproducible today without a live model:
`python3 plans/attrib_probe.py block-sha --frozen plans/attrib-r23-frozen.md`
(exit 0, `1b2d6a01…`) and `sha256sum ~/.local/share/ds-flash-shim/shim.py`
(`42d86d99…`, matches the pin).

Which claims `SOURCES.md` serves: **none**. All three are record/tool/quality
moves over in-repo evidence; `corpus/SOURCES.md` is a wave-2 artifact and is
not a prerequisite. New knowledge entry: exactly one (the stream-mechanism
entry above); the rest of C1/C2/C3 is index, score and quality-bar work.

---

## 7. Conflicts for the canonical judge (verbatim)

K1 — operator stop vs rounds 20–22 running.

- `MANIFEST.json`, fleet round 22 note: "OPERATOR STOPPED the 10-round run
  after r19 (rounds 20-28 do not run)."
- `LOG.md:148-149`: "The operator cancelled the 10-round goal after this
  round; rounds 20-28 do not run."
- `MANIFEST.json`, fleet rounds 23/24/25: `lane_rounds.kengaku` = 20/21/22,
  all `"closed"`.

No resolution inferred; the record contains both the stop and three later
admitted rounds.

K2 — surfaces resolve vs absent.

- `SCORECARD.md:222` (round 15): "`~/archive/bench-arena` — resolves;
  `~/Projects/webzites/repos/llm-wiki` — resolves."
- `corpus/lessons/round-16-recensus.md:21-23`: "`~/Projects/webzites/repos/llm-wiki`
  (SSOT) absent; `~/archive/bench-arena` and `~/bench-arena` absent."
- 2026-10-19 `test -e`: both absent.

K3 — gate size.

- `SCORECARD.md:305`: "All 149 checks recompute stored-vs-derived from
  committed bytes."
- `SCORECARD.md:164`: "733 checks"; `:198`: "`CHECKS n=733 mismatches=0`".

K4 — report path.

- `MANIFEST.json`, fleet round 25: "Report:
  kengaku-shokunin/.ufo/rounds/round-22/kengaku.md."
- `PROTOCOL.md:138`: "Every dispatched lane writes its report at
  `.ufo/reports/round-<N>/<id>.md` in the main repo."

K5 — round 23 premise (sequencing, not a contradiction).

- `corpus/lessons/2026-10-16-round23-stream-surface.md:9-10`: "no round-23
  artifact has landed" (written 13:33Z).
- Receipts landed 13:45–13:49Z and commits `a2ff634/f9337d5/6f31d23` exist.
  The lesson itself says landed receipts supersede it; no contradiction, but
  the lesson's unconfirmed-premise leftover is now stale and unmarked.

---

## 8. Behavior, gates, touched surfaces, out of scope

- Behavior: the lane measures model/eval claims with frozen, hashed
  preregistrations, an offline replay gate, and append-only corrections. Its
  recent behavior is strong on measurement discipline and weak on closure:
  rounds are executed faster than they are recorded.
- Gates: `grader.py` — last recorded `CHECKS n=733 mismatches=0
  errata_pinned=1`, `VERDICT: PASS`, exit 0; `--selftest` S0–S7 PASS
  (`SCORECARD.md:198`; `.ufo/round-17/gates.json`; `lessons/round-16-recensus.md:6-9`). Not re-run here.
  `attrib_probe.py block-sha` on the v3 table was run and passed today
  (`1b2d6a01…`, exit 0). `coverage_census.py --help` exits 0.
- Touched surfaces (read-only): lane git objects and tracked files; every
  declared host path via `test -e`; `ss` for port 34113; shim sha256; fleet
  `MANIFEST.json`, `AXES.md`, `CORPUS.md`, `MISSION.md`, `LEARNING.md`,
  `PROTOCOL.md`; fleet report directories.
- Out of scope / not done: no web fetch, no `SOURCES.md`, no live model or
  proxy traffic, no `grader.py` re-run, no full 61-citation sweep, no edits to
  the lane, the fleet, other lanes, the judge, or any product code; no commits
  or pushes. This artifact is the only write.

Artifact: `/home/vgpnk/Projects/shokunin/local/kaika-w1-kengaku-state.md`
