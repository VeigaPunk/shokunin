# tsukuroi — round 50 (hyaku run 11, attempt 1)

Lane: `tsukuroi-shokunin` (host operability & system repair). L1: `TsukuroiR50`.
Base `b866a1d3d26616119a089f1a69b080136becc17b` → freeze `43bcce06e28fe53b6f2e358a1225bb2b1b536b22`
→ pre-data amendment `8029cdba1049df25632c91a23c8db4eefb54be5f` → wave evidence `39e694934cf6c56434987edc730e8b3580a251f3`
→ integration `b7fb30a03afc0fa764f7b3ccffb1974930aa6b0f` → registry/calibration restatement `9c5d6b436e599c7809ffe458e973cd14d410bb51`
→ final lane tip `fb5a1d8625f058a8549ff74746ee863596acd245` (`git ls-remote origin refs/heads/master` prints it).

Round shape: **one v2 wave (`w1`), 71 seats** under policy v2 (band 64–128): reviewer 19, critic 18, executor 10,
scout 9, scribe 5, mutation-tester 4, connector 2, sentinel 2, revenger 1, simplifier 1. Attack roles counted
per the frozen policy definition (reviewer + critic + mutation-tester): 41/71 = 57.7%. Dispatched 71, 71 results
entries, 64 seat report files, **0 dead seats**, no replacements and no residual call. Seven settled seats have a
final output in `w1-results.json` but no `<seat>.md` report file: `R50MutCounterC`, `R50ScoutLiveTip`,
`R50RevCounterC3`, `R50ExecPriorCounters`, `R50Simplifier`, `R50CritGR2Host`, `R50RevScopeSiblings`; their outputs
remain in the orchestrator handoff and are not counted as report files. The L1 holds the planner seat (the
validator rejects `planner` as a swarm role; a bounded planning walk rode connector/scout items).

## Work performed

Declared claims (three causally separable claims on distinct axes; frozen in
`.ufo/waves/round-50/frozen/FROZEN.md`):

1. **C1 — depth (lowest tied axis, 8):** apply the four round-49 corrections to
   `corpus/knowledge/btrfs-scrub-grounding-r45.md`, repair the C1 citation/distinct-body instrument, then have a
   new 18-seat cohort re-read GR1–GR3. The cohort found blocking negatives on every row; the frozen claim is
   honestly **FAIL**, not narrowed after data.
2. **C2 — operability (sourced: S256, opened 2026-10-28):** replace the census selftest's early-exit
   `printf | grep -q` / `head -n1` checks with a full-read matcher and add `(R50-C2)` (167 → 168 cases). The
   frozen measurement is **PASS** on the actual census bytes; the counter's liar-census and spelling-evasion
   limits are reported.
3. **C3 — adjacency (lowest tied axis, 8):** add pinned-blob and live-tip content legs plus a stub-failure leg to
   the ADJ table counter. The default lane table measures **PASS**; its override path and semantic-quote limits
   are reported.

Work items (71; reports are under `.ufo/waves/round-50/w1/`):

- **C1 correction verification and counted cohort** — `R50ExecGRCorr.md`, `R50RevCorr.md`,
  `R50RevGR{1,2,3}{a,b,c}.md`, `R50CritGR{1,2,3}{a,b,c}.md`. GR1: 5 `holds`, 1 `partly` (`R50RevGR1b`,
  missing `* ` in the `cmdline.c:147` quote). GR2: 2 `holds`, 4 `partly` (`R50RevGR2c`, `R50CritGR2a/b/c`):
  `by SR7` misattributes the cancel path, the narrowed ioctl inference still overstates pre-call behavior and
  copy-back failure, S242's declared ranges omit cited `scrub.c:3094-3095`, `:3109`, `:3114`, `:3138`, and the
  progress-query condition is the device's scrub context, not replace state. GR3: 6 `partly`, on S237's
  undeclared `scrub.c:439` and `:1546` citations. All four round-49 corrections were present, but the new
  counter records `verdicts_ok 0`; no admission mark was written (`after/c1-final.json`, `R50RevGR1b.md`,
  `R50CritGR2b.md`, `R50CritGR3a.md`).
- **C1 instrument attacks** — `R50CritCheatC1.md`, `R50SentForge.md`, `R50LabParse.md`,
  `R50RevCounterC1.md`, `R50MutCounterA.md`, `R50MutCounterB.md`, `R50ExecMarkCounter.md` report binding,
  provenance, parser and forged-cohort limits. The seat-written results JSON plus report shapes are not proof that
  the cited lines support the verdict; cited limitations remain explicit.
- **C2 matcher and source** — `R50ExecMatcher.md`, `R50ExecRaceProbe.md`, `R50ScoutCensusFlake.md`,
  `R50CritCheatC2.md`, `R50RevCounterC2.md`, `R50MutCounterC.md`, `R50ScoutGrepSource.md`,
  `R50ScribeLessonC2.md`. The amended census uses a full-read awk matcher; the 168-case selftest passes twice
  (`after/c2-final.json`). A 5-/12-line liar census can satisfy the C2 counter and an equivalent `${out}` pipe
  spelling evades its lexical scan (`R50CritCheatC2.md`, `R50RevCounterC2.md`), so its PASS is not standalone
  proof. S256 opened GNU grep(1): “Exit immediately with zero status if any match is found, even if an error was
detected” (raw HTML lines 201–205; digest and quote in `corpus/SOURCES.md` and `corpus/lessons/round-50.md`).
- **C3 adjacency** — `R50ExecAnchorContent.md`, `R50ScoutLiveTip.md` (result output present; no report file),
  `R50RevCounterC3.md` (result output present; no report file), `R50CritCheatC3.md`, `R50MutCounterD.md`,
  `R50ConnOverlap.md`, `R50RevScopeSiblings.md` (result output present; no report file). The default check is
  `quote_at_pin_ok 9`, `live_quote_ok 9`, `stub_fails 1`, `anchors_checker_rc 0` (`after/c3-final.json`). The
  critic showed a false displayed OUT-009 locator can pass and an adapted fabricated sibling set can pass via
  caller overrides; byte-substring checks do not prove semantic entailment.
- **Sources/frontier** — `R50ScoutReopenS240.md`, `R50ScoutReopenS242.md`, `R50ScoutReopenS247.md`,
  `R50ScoutGrepSource.md`, `R50ScoutProvenance.md`, `R50ScribeSourcesGate.md`, `R50ExecCensusSources.md`,
  `R50ScoutConsider.md`. S240 re-opened byte-identically at sha256 `7b3488f2…ba01`; S256 added as a tier-A row.
  The staged package was not adopted: 57 source IDs collide.
- **No-harm, self-assessment and conformance** — `R50RevNoHarm.md`, `R50ExecSelfAssess.md`,
  `R50SentScope.md`, `R50RevSeparability.md`, `R50CritTrends.md`, `R50CritVacuity.md`, `R50CritCounterDiff.md`,
  `R50RevengerBase.md`, `R50ExecPriorCounters.md` (result output present; no report file),
  `R50ScoutHostSurface.md`, `R50ReviewerReport.md`, `R50CritReportClaims.md`, `R50Simplifier.md` (result output
  present; no report file), `R50ScribeSkill.md`, `R50ScribeReadme.md`, `R50ScribeMistakes.md`,
  `R50ScribeLessonC2.md`. The no-harm review found the 167→168 change would break the round-49 exact-count
  fd-band counter; it was made forward-compatible (`cases >= 167`) and re-measured PASS at 168. Three new gate
  registry rows were added; the final coverage gate still reports six pre-existing missing tools, with no new
  round-50 counter missing.
- **Pre-data controls** — 17 controls, all as declared at amendment revision `8029cdba` and committed with the
  wave dispatch (`39e69493`): C1 9 controls, C2 4, C3 4; see
  `.ufo/waves/round-50/controls/battery-summary-r50-c{1,2,3}.jsonl`. Three control failures during the first
  amendment pass (K1 incorrectly included a cohort, C2 still had one `$pkgline` pipe site and the comment-blind
  lexical scan counted its own comment, C3 inherited the shifted IN-109 anchor) were repaired before any seat
  scored (`.ufo/waves/round-50/frozen/FROZEN.md`, “Freeze amendment 1”).
- **Assimilation/considerthese** — the 0–3-space collision guard found 57 staged IDs in common; its indented
  `  | S200 |` proof yields 1 collision while the column-zero-only extractor yields 0. The lane and staged ID
  sets are contiguous `S001–S256` (256 IDs) and `S200–S346` (147 IDs); collision IDs are `S200–S256` (57).
  Renumber map: none, because no package rows were adopted. `R50ScoutConsider.md` identifies the open
  counter-attack scoreboard proposal in `considerthese/2026-10-26.md:18`; it was mined, not implemented.
- **Misroot sweep** — `git -C /home/vgpnk/Projects/shokunin status --porcelain` found no file attributable to
  tsukuroi round 50. It listed other work (`lane3/`, `.scratch/` closure/case files, `o.bin`, `oldrep1.out`,
  `oldrep2.out`); these were inspected as unrelated and left untouched.

## Landed changes

Each item is recorded under `LOG.md` “Round 50 — declaration” / “measured outcome and closure facts” and landed
through `jj-lane.sh`:

- Freeze, claims and counters: `43bcce06e28fe53b6f2e358a1225bb2b1b536b22`.
- Pre-data freeze amendment (last pipe assertion, comment-aware idiom count, IN-109 repin):
  `8029cdba1049df25632c91a23c8db4eefb54be5f`.
- Validated one-wave v2 dispatch and pre-data controls: `39e694934cf6c56434987edc730e8b3580a251f3`.
- Integrated entry gate status, lesson, S240 `used-by`, S256, QUALITY 94, SKILL/README/SCORECARD/LOG records and
  71-seat results: `b7fb30a03afc0fa764f7b3ccffb1974930aa6b0f`.
- Gate registry/current-axis restatement: `9c5d6b436e599c7809ffe458e973cd14d410bb51`.
- Final receipts and current score/trend accounting: `fb5a1d8625f058a8549ff74746ee863596acd245` (lane `master`
  remote verified at this hash; `ahead=0`, `behind=0`).

No package/host state was modified and no tools were installed or updated. Actual model-answering metadata was not
present in the wave results file; no claim relies on a model identity.

## Before → after measurements

1. **C1 / depth — FAIL (not narrowed).** Command:
   `python3 tools/check-scrub-admission-r50.py --revision <REV> --wave-dir .ufo/waves/round-50/w1 --results-file .ufo/waves/round-50/w1-results.json --dispatch-file .ufo/waves/round-50/w1-dispatch.json`.
   Before at base `b866a1d3`: `structural_ok 1, corr_ok 0, quotes_ok 3, verdicts_ok 0, seats_ok 0, marks_ok 0`
   (`before/c1-at-base.json`). After at frozen row bytes `8029cdba` with the settled cohort/results: `structural_ok 1,
   corr_ok 1, quotes_ok 3, verdicts_ok 0, seats_ok 18, marks_ok 0`, FAIL (`after/c1-final.json`). The corrections
   landed; the target predicate did not. The 18-seat negative rules were frozen and not weakened.
2. **C2 / operability — measured PASS, instrument limit reported.** Command:
   `python3 tools/check-selftest-matcher-r50.py --revision <REV> --scratch <DIR>`.
   Before at `b866a1d3`: `idiom_sites 7, base_misses 20/20, full_misses 0, cases 167, pass_runs 2, case_ok 0`,
   FAIL (`before/c2-at-base.json`). After at census bytes `8029cdba`: `idiom_sites 0, base_misses 19/20, full_misses 0,
   cases 168, pass_runs 2, case_ok 1`, PASS; both runs printed 168/168 PASS (`after/c2-final.json`). The actual
   census matcher works; a stub can still print the expected lines and pass the counter (`R50CritCheatC2.md`).
3. **C3 / adjacency — measured PASS, instrument limit reported.** Command:
   `python3 tools/check-adjacency-table-r50.py --revision <REV>`.
   Before: the round-49 shape counter at base `b866a1d3` accepts a fabricated shape-valid province and registry
   (`before/c3-r49-stub.json`: PASS; shape legs `7/7`, no content legs). After at `8029cdba` on the actual lane
   table: `adj_rows 7, linked_rows 7, bare_ranges 0, anchors_ok 7, registry_ok 7, anchors_checker_rc 0,
   quote_at_pin_ok 9, live_quote_ok 9, stub_fails 1`, PASS (`after/c3-final.json`). Caller overrides can still
   supply a coordinated fabricated table/sibling tree; the tool does not prove semantic quote entailment.

The predecessor no-harm battery (`R50RevNoHarm.md`) found three new registry misses and two self-assessment count
mismatches at the freeze, plus the round-49 fd-band exact-count regression. After the three tool rows were added,
`check-registry-coverage.py --revision 9c5d6b4` still reports six pre-existing missing tools (base also had six),
no round-50 counter among the missing set; `check-self-assessment.py --revision 9c5d6b4` is PASS, 27 checks,
0 mismatches; and `check-fd-band-r49.py --revision 9c5d6b4` is PASS at 168 cases with the compatibility predicate
`cases >= 167`. Receipts are committed in `.ufo/waves/round-50/after/`.

## Sources & frontier

Command at both round start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.

- Before: exit **0**, 255 rows, 40 W04 warnings (`.ufo/waves/round-50/before/sources-census-start.txt`).
- After: exit **0**, 256 rows, 40 W04 warnings (`.ufo/waves/round-50/after/sources-census-end.txt`).
- Added by tier: one tier-A docs row, S256 (GNU grep(1)); no new rejection row.
- Touched: S240 remains `mined`, recheck `on-release`; `used-by` changed from `corpus/knowledge/btrfs-scrub-record-r43.md, corpus/knowledge/btrfs-scrub-record-r44.md, corpus/lessons/round-48.md` to those three plus `corpus/knowledge/btrfs-scrub-grounding-r45.md`. S256's `used-by` is the round-50 lesson. No other status/recheck/used-by change.
- S240 was re-fetched at `https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/fs/btrfs/ioctl.c?h=v7.2.11`, 5,678 lines, sha256 `7b3488f2f83563134fec1a3d40c4149a5fe3606de6628cd33f7897fd4534ba01`, byte-identical to the pin; S256 was fetched at `https://man7.org/linux/man-pages/man1/grep.1.html`, sha256 `d6f07a7f75c6275f6986df2501d355ebd22fa1475ce50dc6039f1fb028d6a3c2`, quote raw HTML lines 201–205.
- Frontier rows advanced: **0**. No knowledge entry was admitted; the scrub rows stay pending and storage record content/running state and NVMe SMART remain Frontier.
- Assimilation: **none**. Lane IDs `S001–S256` (256) and staged IDs `S200–S346` (147); overlap `S200–S256` (57); renumber map **none** because nothing was adopted. The scratch guard proved an indented collision is found (1) where the column-zero-only extractor finds 0. `considerthese/2026-10-26.md:18` counter-attack scoreboard proposal was mined and not implemented.

## Trend verdicts

- **expansion — unchanged:** no new knowledge entry admitted; no province Frontier row advanced. S256 is registry curation, not coverage expansion.
- **quality — harmed:** the round's GR2 correction still overstates what the ioctl returns before it reaches `btrfs_scrub_dev`; the new counted row findings are explicitly recorded, but the erroneous clause remains in the frozen row pending a later round. No admission mark was written.
- **discernment — unprovable-but-better:** the counted cohort exposed the GR1 quote-prefix omission, S242/S237 range gaps, and GR2 attribution/inference defects; QUALITY 94 records the general rule. This is not the required outside sample: every dispatched seat is lane-authored, so independent non-author discernment remains pending.

## SHONEN

[~] Box 1 — decision tables, error patterns and cited checklist: `SKILL.md:1-190`, `corpus/QUALITY.md:184`.
[~] Box 2 — end-to-end task executed and logged: `tools/tsukuroi-census.sh --selftest` → PASS 168/168; `LOG.md` Round 50 outcome.
[~] Box 3 — instructions executable without oral context: `SKILL.md` update-safety checklist and `tools/tsukuroi-census.sh` selftest.
[~] Box 4 — no cross-domain bleed; province remains accurate: `PROVINCE.md` Core/Frontier/Adjacent; no sibling scope absorbed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 questions: none. No tool installs or updates.
