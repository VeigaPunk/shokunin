# kama round 86 — rendered-cell identity, mutant owning arms and pin origin

## Work performed

Declared claims (fresh-start round after three rejected closures r83/r84/r85; the current pause was
lifted once by the operator, run-15 amendment 11, history retained):

- **C1 calibration** (lowest assigned axis, 7 of 10) — a self-assessment cell counts only when it is
  *rendered*, and the head authority cell is graded as one coupled assertion (revision + command +
  receipt bytes read at that revision).
- **C2 operability** (8 of 10) — every declared mutant of the debt selftest maps to a declared owning
  arm, and each completed summary reconciles with its arm population and failure-line cardinality.
- **C3 freshness** (8 of 10) — pin-recheck rows corroborate against the live upstream bytes at the
  declared URL and line range, separating remote origin from the local extract pair's hash integrity.

Frozen plan `plans/round-86-claims.md`, frozen counter `.ufo/waves/round-86/count.py`, freeze
`c07e1f909414aafb2d8de5605a81fd3bd4e3550e`; base `3ff23da3f291ce8abf7bf5c54f9abacec67e3e8d`.

**Round disposition: honest stop, not admitted.** C2 and C3 verify on their frozen predicates (C3 with
a disclosed origin limit); C1's numeric target is met but the instrument is falsified against its own
predicate by two false greens the terminal wave reproduced and the L1 re-ran. No axis is harmed; the
work, the falsification and the routed repairs are reported below rather than argued away.

- **Inherited state.** This round had three earlier attempts that died without a report after landing
  real work (watchdog `lane-dead-no-report kama round=86` at 21:52, 21:58 and 22:31; the tip they left
  is `bafae7af`, message "preserve in-flight work … L1 died on provider failure; not a landed round").
  Everything re-verified was reused: the frozen plan and counter, `tools/round86-rendered-cells.py`,
  `tools/round86-mutant-owners.py`, `tools/round86-pin-origin.py`, the before/after receipts, the wave
  evidence of w1/w2, `corpus/lessons/round-86.md`, `corpus/QUALITY.md` KQ139, the SOURCES rows and the
  SCORECARD/LOG round-86 sections. Nothing was discarded: no inherited artefact contradicted its own
  receipt on re-measurement. The tree was clean at this attempt's start (`tracked=0 untracked=0`,
  `ahead=0`). Evidence: `.ufo/waves/round-86/measured/terminal/commands.json`, this report's commit table.
- **C1** — `tools/round86-rendered-cells.py` selects the first top-level *rendered* authority paragraph
  and the first top-level calibration row (HTML comments, backtick/tilde fences including container
  fences, backtick info strings, `round-<N> correction` blocks and non-column-0 lines are not cells),
  then grades three coupled facts. The two live cells were repaired in place: the banner now names the
  round-86 terminal gate receipt `0f8a0980` with the exact token, and the calibration row names the
  newest committed closure by round number. Evidence: `tools/round86-rendered-cells.py:56-82`,
  `SCORECARD.md:6,18`, `.ufo/waves/round-86/measured/terminal/c1.out`, `c1-selftest.out`,
  `c1-mutants.out`.
- **C2** — `tools/round86-mutant-owners.py` maps M2/M3/M4/M5/M6 to their owning arms
  (`note-deletion-equals-subject`, `note-deletion-above-subject`, `note-subject-exact-summary`,
  `arm-count`, `summary-cardinality`) and reconciles each run's summary with the ARMS line and the
  printed failure lines; `tools/round81-append-debt.py` gained `EXPECTED_ARMS`, the
  `APPEND_DEBT_SELFTEST_ARMS` line and an arm-count assertion while keeping its round-81 summary shape.
  Evidence: `tools/round86-mutant-owners.py`, `.ufo/waves/round-86/measured/terminal/c2.out`,
  `c2-selftest.out`.
- **C3** — `tools/round86-pin-origin.py` re-reads each anchor header, recomputes the digest over the
  stored body, fetches the declared URL and compares the stored body with the upstream range byte for
  byte. Evidence: `tools/round86-pin-origin.py`,
  `.ufo/waves/round-86/measured/terminal/c3.out`, `c3-selftest.out`.
- **Waves (round total 36 seats; 3 validated v1 waves; no residual call).** w1 12 seats (3 executor,
  2 mutation-tester, 2 reviewer, 1 critic, 1 scout, 1 scribe, 1 connector, 1 sentinel; attack 5/12) and
  w2 12 seats (2 reviewer, 1 critic, 2 mutation-tester, 3 executor, 1 scout, 1 scribe, 1 sentinel,
  1 connector; attack 5/12) ran in the inherited attempts and are recorded here as this round's
  evidence; w3 12 seats (3 reviewer, 2 mutation-tester, 2 executor, 1 critic, 1 scribe, 1 scout,
  1 sentinel, 1 connector; attack 6/12) attacked the terminal record at `bafae7af`. All three waves
  validate under `ufo-wave-policy.json` (band 8–16). No planner seat is dispatched — the validator
  refuses the role and the L1 holds the canonical planner seat; no seat of any wave is replaced.
  Evidence: `.ufo/waves/round-86/{w1,w2,w3}-spec.json`, `{w1,w2,w3}-dispatch.json`,
  `{w1,w2}-results.json`, `w3.ready`, `w3.ready.dispatched`.
- **What the waves changed in the delivered instruments.** w1 `RV01ClaimsReview` proved the gate fact
  read the receipt at the *graded* revision instead of the revision the banner names (fixtures f1/f4):
  the instrument now reads `git show R:path` and `revision-carries-no-receipt` holds it. w2
  `MT01SelectorMutants` proved the four `*-shadow` arms were vacuous — the stale live cell was emitted
  first, so a selector with fence/comment/correction/column-0 exclusion disabled still passed and five
  mutants survived; the fixture now emits the shadow first, and 10/10 source mutants are killed by named
  arms. w2 `EX02GateArms` proved the C2 commit had turned frozen gate arm 11 red by extending the
  debt-selftest summary line; the summary keeps its round-81 shape. w2 `CR01SizingControl` produced the
  receipts that disclose the counter's worktree-execution limit. Evidence:
  `.ufo/waves/round-86/w1/out/RV01ClaimsReview/`, `w2/out/MT01SelectorMutants/findings.md`,
  `w2/out/EX02GateArms/EX02GateArms.md`, `w2/out/CR01SizingControl/`.
- **Disclosed seat-output defects (not hidden).** w2 `CR01SizingControl` returned a 159-character
  summary that is almost entirely whitespace; its 26 receipt files are the evidence and are committed.
  w1 `MT01MutantOwners` (180 chars), w1 `MT02SummaryForgery` (114 chars), w2 `RV02MutantOrigin` (571)
  and w2 `CN01OverlapScan` (967) are thin summaries over committed artefacts. The results files carry
  only `name`/`agent`/`output`, so per-seat status, ids and error text are **unestablished** rather than
  fabricated. No seat died in a way the results record shows. Evidence: `w1-results.json`,
  `w2-results.json`.
- **W3 settlement and its findings** are recorded in *Before → after measurements* (the subsection
  "What the terminal wave falsified about the evidence") and in `SCORECARD.md` §Round 86 ("Round-86 w3
  terminal falsification"); seat status and dead seats are reported there from `w3-results.json`.
- **Inherited append-only debt accepted, not zeroed.** 15 rows in `registry/append-only-late.tsv`
  accept the four round-84/85 SCORECARD in-place events (`3e93febb`, `65665250` twelve rows,
  `c0d7fbd8`, `948dec78`), each row naming its commit subject and the deletion round it accepts; this
  closed the inherited red gate arm for the round-86 audit. Evidence: `registry/append-only-late.tsv`,
  `measured/terminal/gate.out` (`APPEND_DEBT round=86 … unaccepted=0 bad_rows=0`).
- **Boundaries.** No live serving endpoint, service, route, config or credential was touched; registered
  consumers keep their last recorded `DEAD`, which is not a readiness claim. No domain source tree,
  sibling lane or fleet file was written. Fleet-root misroot sweep (`git status --porcelain -uall` at
  this attempt's start and again at the w3 audit): one modified orchestrator file
  (`.scratch/run15-state.json`, run-state churn for nine lanes) and one unattributed 0-byte stray
  `mo.tip` whose content names no lane or round; no untracked file attributable to this round's seats,
  so nothing was copied or deleted. Evidence: w3 `SN01ScopeAndMisroot` item 1.

## Landed changes

Every commit below was landed through `scripts/hyaku/jj-lane.sh commit … --as kama` (the helper printed a
`landed <hash>` line for each) and is tied to the LOG.md `## Round 86` entry.

| Landed lane commit | Change / LOG tie |
|---|---|
| `c07e1f909414aafb2d8de5605a81fd3bd4e3550e` | Frozen plan, frozen counter and the three before/no-work controls — LOG.md §Round 86 (motivation, base, controls) |
| `f4c7acaa0563d1cf813fff90e4b927494a88091f` | w1 spec, dispatch and ready handoff (12 seats) |
| `67eddac89f44e768b670301ea0feff06e766f32d` | Live cells repaired by rendered identity, CommonMark fence/indent sources opened, lesson landed — LOG.md §Round 86 C1 paragraph |
| `c5d71b7a0455f8f2b46593f6ef48cc92ca765670` | Rendered-cell and debt-summary arms repaired, inherited append debt accepted, w2 falsification recorded — LOG.md §Round 86 wave-settlement paragraph |
| `da580634ee73b58cdea108e301a11e181d424ae7` | The three round-86 instruments named on the PROVINCE surface |
| `1018ed2b873f8d4c1ecead66c1047d33aa6c17d4` | Three round-86 capabilities mirrored into the canonical table, surface hash re-anchored, table separator repaired |
| `1bfcd49fd1eba6a1919b73388d8c9a644163e340` | C2 reconciliation clauses the classifier skipped (ARMS population, stderr) implemented |
| `d80d0896eaae111d7d7c6a34d0898ecc1e7a8ab9` | Cell bound to the newest receipt path, declared arm population pinned, mutant driver added |
| `7a21aaa167a0c1df81e7fca9d95364433ec36997` | Container fences and backtick info strings excluded, with a control and a mutant for each |
| `c5a324430fb0ef04dc9d886f997d7cdacc083f7b` | Terminal selftest and mutant counts corrected in the record |
| `bafae7afb41843564ac2468d28beb8e0bb98e8e6` | In-flight work preserved at the run-15 wrap-up (earlier attempt died on provider failure) |
| `d05f6d01a4b39d1ef60043ab123a7ef50085f5b0` | Three claims bound to the terminal measurement, considerthese proposal 3 mined into KQ139, w3 dispatched — LOG.md terminal-measurement paragraph |
| `ec541687f1af45b4b7b7ff2e7514771f0c28ad41` | w3 dispatcher stderr recorded (empty) |
| `0f8a09802fef5a311881db7ee26461a5d68158e7` | Terminal gate receipt (`arms=13 failed=0 uncommitted=0`) and its argv/exit record |
| `239a8f39e33e252a44bb16c7202de6cd674f4614` | Head authority banner re-bound to the round-86 terminal gate receipt; round-start census receipt — LOG.md terminal paragraph |
| `84e6f4573c2a0120def1cb8a37821a8c000686bb` | Final re-measurement of the three claims at the banner tip (`newest_gate=86`) |
| `0fec2861d579ac70e38525e7b753da8fe226d5a2` | M3 tally corrected against its receipt, superseded C2 after-receipt noted, w3 findings routed into the round-87 plan |
| `f43a7ee58ccbff0859f807d6a7eb1d5854eeeff8` | KQ140 added, w3 mistakes mined into the lesson, the three pending debt events disclosed, round-end census recorded |
| `019fadc0a60b1c6e4af62c51b4487c7e091f1ea9` | SCORECARD §Round 86 "w3 terminal falsification" subsection |
| `4189145a6eb4d7a8dd64f308510a17bff0a5f312` | w3 seat outputs committed (11 of 12 seats written at that point) |
| `cef1d7217348b089def61b3a31395fffd7048455` | C1 recorded as falsified (fence-closer and disposition-oracle false greens reproduced), C2/C3 verdicts, M9/M10, round-87 items 4/5/7 |
| `10cffc8b82b729cfd9cb628d8c42305cfe8bd5d2` | w3 seat reports and the relocated lane-root seat stray |
| `421ef5971ad4056d42158571f9ca0cad9b79148a` | Post-repair gate re-check recorded as `terminal/gate-recheck.txt` (13/13 green) |
| `2fb3871412b7555d13125d0ab45ec49f142dea02` | M11 (lane-root seat stray) recorded in the lesson |

Final pushed lane hash: **`84e6f4573c2a0120def1cb8a37821a8c000686bb`**
(`git -C /home/vgpnk/Projects/shokunin/kama-shokunin ls-remote origin refs/heads/master` printed it;
`jj-lane.sh state` reported `ahead=0 behind=0`). Publication commits after that point are named in the
final row of this section when they land.

## Before → after measurements

Run from the lane root. `$R` is the declared before revision; the after receipts are at
`.ufo/waves/round-86/measured/terminal/` with argv/stdout/stderr/exit for every leg in `commands.json`.
Before receipts are `.ufo/waves/round-86/measured/before/`, measured at base `3ff23da3f291…`.

```sh
python3 .ufo/waves/round-86/count.py c1 --repo . --rev 239a8f39e33e252a44bb16c7202de6cd674f4614 \
  --work /fast/scratch/hyaku/kama-r86/l1/c1
# before (3ff23da3f291…): RENDERED_CELLS facts=3 mismatches=3 gate=0 closure=0 disposition=0 newest_gate=85 newest_closure=85 ; exit1
# after  (239a8f39…):      RENDERED_CELLS facts=3 mismatches=0 gate=1 closure=1 disposition=1 newest_gate=86 newest_closure=85 ; exit0
python3 .ufo/waves/round-86/count.py c2 --repo . --rev 239a8f39e33e252a44bb16c7202de6cd674f4614 \
  --work /fast/scratch/hyaku/kama-r86/l1/c2
# before: DEBT_MUTANT_OWNERS mutants=5 killed=3 escaped=2 invalid=0 arms=unknown cardinality=ok owners=3/5 ; exit1
# after:  DEBT_MUTANT_OWNERS mutants=5 killed=5 escaped=0 invalid=0 arms=34 cardinality=ok owners=5/5 ; exit0
python3 .ufo/waves/round-86/count.py c3 --repo . --rev 239a8f39e33e252a44bb16c7202de6cd674f4614 \
  --work /fast/scratch/hyaku/kama-r86/l1/c3
# before: could-not-evaluate: no tools/round86-pin-origin.py at 3ff23da3… ; exit2
# after:  PIN_ORIGIN rows=5 verified=5 mismatch=0 unreachable=0 bad=0 ; exit0
```

- **C1 calibration: numeric target met, claim NOT verified — the instrument is falsified against its
  own predicate.** `mismatches=3 → 0`, `gate=1 closure=1 disposition=1`, exit 1 → 0; selftest 17 arms
  0 fail (11 at the freeze); `RENDERED_CELLS_MUTANTS mutants=10 killed=10 escaped=0`; the base tree
  prints the three mismatches. But the w3 wave produced two reproductions of a false green, both
  re-run by the L1 on this host:
  1. **fence closer** — `SB01SectionDraft` probe `P-A`: a top-level fence opened with three backticks and the info string `markdown`
     and a list-marker line (`-` then three backticks) inside it. `cmark` 0.31.2 (`cmark -t xml SCORECARD.md`) renders lines 4–8 as
     `code_block` content (fence closes at line 9), so the *rendered* cells are the stale round-84 ones;
     the selector treats that list-marker line as the closer, reads the in-fence round-85 cells and prints green.
     My re-run of `tools/round86-rendered-cells.py --repo <fixture> --rev <fixture-commit>` selects the
     in-fence cell (`… gate declared round=85 …`), i.e. the "fence-free" clause of the frozen predicate
     does not hold for this construct. Evidence: `.ufo/waves/round-86/w3/out/SB01SectionDraft/probes/`;
     my reproduction `/fast/scratch/hyaku/kama-r86/l1/f1` (scratch, not citable) — the committed fixture
     and its script are the citation.
  2. **disposition oracle** — `disposition_of()` returns the first word in a fixed order found anywhere
     in the closure body; a body that mentions `rejected-harmed` about another round makes the tool
     expect `rejected-harmed`, and a row naming `round85 rejected-harmed` grades `disposition=1`. My
     re-run reproduces `disposition=1` on that fixture. The live round-85 closure contains no
     `rejected-harmed`, so the committed record's number is unaffected — the class is.
  Score 7 → 7, no numeric move claimed. The claim's kill rule does not fire on an existing control, but
  the predicate is not implemented; the round therefore records the honest stop rather than a
  numeric-green admission.
- **C2 operability: verified.** `killed=3/escaped=2 → killed=5/escaped=0 owners=5/5`, `arms=34`
  declared and reconciled, pristine `APPEND_DEBT_SELFTEST pass=34 fail=0`, selftest 13/0. Production
  grading bytes unchanged outside the selftest (`tools/round81-append-debt.py` DEFECT tape: round-85
  receipts' three actual kills stay). `SB01SectionDraft` F6 independently probed the classifier and
  found no false green; the forged-subject class is disclosed below. Score 8 → 8.
- **C3 freshness: verified (capability acquisition), with a disclosed origin limit.** `rows=5
  verified=5` live against upstream; the `fabricated-hash-consistent` arm is refused as `mismatch` and
  `digest-lie` as `bad` (selftest 7/0), so hash-consistency alone is not origin. Limit
  (`SB01SectionDraft` F7, code-confirmed at `tools/round86-pin-origin.py:95-118,136-160`): the URL
  fetched is the anchor header's own `url=`, and `grade()` never reads the row's `engine`/`ref`/`newest`
  columns, so an anchor that declares a fabricated URL and a fetch serving those bytes grades
  `verified` (probe P-H), and a row declaring `ref=b11755` whose anchors name `b7200` also grades
  `verified` (probe P-G). Committed data is consistent (all ten header refs match the register rows), so
  the tip verdict is unaffected; the *claim* that the row's declared upstream is what got checked is
  not established. Score 8 → 8.
- **Full gate at the terminal tree** (`0f8a09802fef5a311881db7ee26461a5d68158e7`, clean):
  `python3 tools/pre-report-gate.py --repo . --round 86 --tip master` printed
  `PRE_REPORT round=86 arms=13 failed=0 uncommitted=0`, exit 0 — every arm green, including the
  inherited append-debt arm (`APPEND_DEBT round=86 events=80 accepted=53 late=27 pending=3 unaccepted=0
  bad_rows=0`) that round 85's terminal gate reported red (`failed=1`). Receipt
  `.ufo/waves/round-86/measured/terminal/gate.out`. Two transient reds observed while the receipt files
  themselves were untracked (`round-scope` stray / `round-clean`) are recorded in `LOG.md` and are not a
  gate result.
- **Disclosed limit, not amended.** The frozen counter executes the instrument bytes from `--repo`'s
  working tree, not from `--rev`: a tampered worktree instrument prints a green line at any revision
  (w2 `CR01SizingControl` `c1-tamper-green-at-base.out`; w3 `CR01DoNothingControl` `T1`/`T2` reproduce
  it at the base for C1 and C2). C3's `--rev` leg is a *presence* gate only — `T4` exits 2 at the base
  while `T5` prints the target from a base tree carrying a stub at the instrument path. The counter is
  frozen before data, so it is not patched after scoring; the final measurement ran on a clean tree
  whose worktree bytes equal the graded revision's. Routed to round 87 item 2.

### What the terminal wave falsified about the evidence (disclosed, not repaired)

- **C1 — falsified: two false greens reproduced by the L1.** (a) *Fence closer.* A top-level fence
  whose content includes a list-marker line (`-` then three backticks): `cmark` 0.31.2 renders the following authority/row lines as
  code, so the *rendered* cells are stale, while `select_cells` treats that list-marker line as the closer and
  reads the in-fence cells — the frozen "fence-free rendered cell" clause does not hold for that
  construct. Fixture and script: `.ufo/waves/round-86/w3/out/SB01SectionDraft/probes/`
  (`P-A-list-marker-fence.md`, `probe_c1.py`); my re-run selected the in-fence cell. (b) *Disposition
  oracle.* `disposition_of()` returns the first word of a fixed order found anywhere in the closure
  body, so a body mentioning another round's `rejected-harmed` makes the tool expect `rejected-harmed`
  and a row naming `round85 rejected-harmed` grades `disposition=1`; reproduced. On the committed
  artifact neither construct occurs, so the *number* stands, but the predicate is not implemented.
  **C1 is not verified.** Separately, four rules are unarmed (`MT01SelectorMutants` `MD`/`ME` survive,
  `MC` dies only incidentally, probe `P1` shows the "first `## Axes` section" clause unenforced).
  All of it is routed to round 87 items 4 and 7; the frozen counter and instrument bytes are not
  patched after scoring. Evidence: `w3/out/MT01SelectorMutants/findings.md`,
  `w3/out/SB01SectionDraft/` (F1, F2, F5).
- **C2 — consistency is sufficient, not necessary, to escape.** w3 `MT02ForgeryArms` ran 18 probes:
  `a1`, `a2`, `b3`, `b6`, `b9`, `c2` and `d` escape; `b6`/`b9` need only an ARMS line printed in a shape
  outside the frozen regex, because "cannot parse" is silently equal to "absent". A fully consistent
  forged *subject* (`F_forged_green.py`, 30 distinct arms, four deleted, owning FAIL lines string-matched
  from its own source) makes the committed CLI print the exact frozen target line and exit 0. This is
  the class the lesson disclosed in advance (M6) — the terminal line proves the printed output
  reconciles, never that the committed selftest owns 34 live arms. **The record's own terminal line is
  not forged:** the counter replay on committed bytes is the before-red/after-green pair shown above.
  If the closure reads C2's frozen kill clause "a cardinality clause that a forged summary can satisfy"
  as covering a forged *subject instrument*, then C2 is not verified; the round records that reading
  rather than arguing it away, and routes the hardening to round 87 item 5.
- **The frozen kill rules, so the closure rules on the same words.** C1: “any remaining mismatch, or
  any control that stops discriminating.” C2: “any survivor, invalid execution, pristine regression, or
  a cardinality clause that a forged summary can satisfy.” C3: “any mismatch/unreachable/bad row, or a
  fabricated hash-consistent extract that grades `verified`.” On the delivered bytes no existing
  control stopped discriminating (`contradictory-receipt`, `revision-carries-no-receipt`,
  `fabricated-hash-consistent`, `digest-lie` all red) and C2 has no survivor among its five declared
  mutants. C1 nevertheless fails as an implementation of its own predicate (the fence-closer and
  disposition-oracle false greens above, reproduced), and the round is therefore **an honest stop, not
  an admission**, even though the counter prints green. C3's limitation (self-declared origin) is
  disclosed as a scope of the capability, not a kill-rule breach.
- **Record repairs made from the wave, never claimed as new wins.** The mined M3 tally said `7/7`
  against a receipt that prints `mutants=10 killed=10`; corrected in place with a dated clause (KQ133).
  `measured/after/c2.out` is an intermediate receipt that prints an `arms=` suffix the terminal bytes
  cannot print (the summary lost it in `c5a32443`); it is marked superseded and the terminal receipts
  are the ones cited. Evidence: `w3/out/CR01DoNothingControl/20-record-number-audit.out`.

## Sources & frontier

Rows opened and landed this round (all three are reads of the published CommonMark 0.31.2
specification, re-opened by the L1 on 2026-11-04; these are documentary reads, not endpoint samples):

| Row | URL | Located quote (≤25 words) | Decision |
|---|---|---|---|
| S576 (re-opened; `used-by` extended) | https://spec.commonmark.org/0.31.2/#atx-headings | §4.2: “The opening # character may be preceded by up to three spaces of indentation.” | admit — grounds the 0–3-space correction/heading rule |
| S578 (new, tier A, mined) | https://spec.commonmark.org/0.31.2/#fenced-code-blocks | §4.5: “A fenced code block begins with a code fence, preceded by up to three spaces of indentation.” | admit — grounds fence exclusion |
| S579 (new, tier A, mined) | https://spec.commonmark.org/0.31.2/#indented-code-blocks | §4.4: “An indented chunk is a sequence of non-blank lines, each preceded by four or more spaces of indentation.” | admit — grounds the column-0 selection rule |

Rows touched old → new: S576 `used-by` `corpus/lessons/round-85.md` →
`corpus/lessons/round-85.md, corpus/lessons/round-86.md`; S576 `status`/`recheck`/`opened` unchanged
(re-opened the same day). S578 and S579 enter at `status=mined`, `opened=2026-11-04`,
`recheck=on-release`, `used-by=corpus/lessons/round-86.md`. No earlier row cell was rewritten (the
registry is append-only; `corpus/SOURCES.md` diff over the round consists only of those cells).

**Sourced claim.** The claim this round grounded in rows opened this round is C1 (S576/S578/S579 supply
the heading, fence and indented-code rules its selector rests on). Because C1 is falsified, the round
does not claim that sourced-claim credit as a verified claim; the sources themselves were independently
checked this round by w3 `RV03SourcesFrontier` (each quote occurs exactly once and inside its own
anchor's section span in the fetched 0.31.2 page; cell word counts 14/17/18; row cells parse; no other
row changed — `w3/out/RV03SourcesFrontier/findings.md` items 1–3). S498 is flagged there as a
pre-existing paraphrase row of the same URL (not touched this round, not claimed).

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
# round start at base 3ff23da3f291…: exit 0, 317 rows — kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
# this attempt's start:            exit 0, `ok` line (receipt measured/terminal/census-start.out)
# round end:                       exit 0, `kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md`
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file corpus/SOURCES.md
# before: rows 317, tier.A 302, tier.B 11, tier.C 4, mined 284, queued 8, rejected 25
# after:  rows 319, tier.A 304, tier.B 11, tier.C 4, mined 286, queued 8, rejected 25
```

Warnings are retained, not suppressed: pre-existing `W01` (S481 tier-C/mined) and cross-scope `W04`
duplicate-URL warnings — 1 `W01` and 115 `W04` lines at the tip, among them S031, S575, S576, S578 and
S579, because the census compares URLs without anchors. **Registry frontier rows advanced: 0** — the same eight ids are `queued` at
base and at tip (`S021 S022 S023 S025 S029 S059 S074 S086`), S578/S579 enter at `mined`, and
`registry/pin-recheck-rows.tsv` is unchanged. What advances is the frontier *capability*: C3 turns the
round-83/84 `holds` verdicts (two committed extracts agreeing with each other) into origin
corroboration against live upstream bytes, so the R84V3/R85V3 open limitation now has a counter that
can fail on it. `corpus/README.md` §Frontier is otherwise unchanged. Evidence: w3
`SB01SectionDraft/sections.md` (B), `RV03SourcesFrontier/findings.md`.

`Assimilation: none` — the `corpus-expansion-1` package at `/home/vgpnk/Projects/shokuknow/merge/kama/`
was read read-only; staged serving/cache/router themes do not implement the frozen three-cell or
mutant-owner populations, so no entry, id, row or citation was adopted and no campaign tool was run.
`considerthese/2026-10-26.md` proposal 3 ("keep a running count of counters that a shortcut can
satisfy") was mined into `corpus/QUALITY.md` **KQ139** — a control arm is admitted only when its subject
sits inside the population the arm tests, and a summary-format change must be checked against every
frozen consumer of that line. Proposals 1, 2 and 4 stay unimplemented and are not claimed.

## Trend verdicts

- **expansion — improved.** Three capabilities entered `SCORECARD.md`'s repertoire through a round that
  demonstrates them running (`rendered-cell-identity`, `mutant-owning-arms`, `pin-origin-corroboration`,
  first-working round 86; `SCORECARD.md:5358-5360`), which `LEARNING.md` §trends counts as expansion
  even with no new `knowledge/` entry. Coverage axis unchanged (9), no new province ground claimed.
- **quality — improved, with a falsified claim reported.** The delivered artifacts are strictly
  stronger than the base: the two live self-assessment cells are repaired, two frozen instruments now
  reject constructs they previously accepted (10/10 selector mutants killed against 5 survivors; M5/M6
  killed), the debt selftest keeps its round-81 summary shape while gaining a declared arm population,
  and the gate is green (13/13) where round 85 left it red (`failed=1`). The limit is named, not hidden:
  the terminal wave falsified C1's instrument against its own predicate (fence-closer and
  disposition-oracle false greens), found four unarmed C1 rules and a forgeable C2 subject, and all of
  it is disclosed above and routed to round 87 — a weaker property is not claimed in place of a
  stronger one, and the round is an honest stop rather than an admission on a green counter. Evidence:
  `measured/terminal/{c1-mutants,c2.out,gate.out}`; `w3/out/MT01SelectorMutants/findings.md`,
  `w3/out/MT02ForgeryArms/findings.md`, `w3/out/SB01SectionDraft/` (F1, F2, F6, F7).
- **discernment — improved.** Every routed defect from the three rejected closures is answered by a
  counter that can fail (R85V1 → C1 rendered cells, R85V2 → C2 owning arms/cardinality, R85V3/R84V3 →
  C3 origin), the round's own false greens were learned into `QUALITY.md` KQ139 from a mined mistake
  rather than patched after scoring, and the terminal wave's adverse findings were filed as limits
  (including the reading under which C2 fails) instead of being argued away. Non-author verification of
  this round is the closure session's duty and is not claimed here.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author
  assertion; `SCORECARD.md`/`PROVINCE.md` edits this round name the three instruments
  (`PROVINCE.md` surface list), no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 86 records the
  three measured instruments and the live upstream-origin fetches; no non-author mark.
- [~] Instructions executable by an agent without oral context — the three counters run from their
  committed `--help`/PREDICATE text and `measured/terminal/commands.json`; independent execution review
  remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touches only lane-owned
  self-assessment cells, the lane's own debt selftest and its own pin register; sibling provinces
  (routing, credentials, service repair) untouched; no non-author mark.

Stale-lane: single steered mission, round 86 of the kama lane, progressed through committed work; no
second kama mission is open and no other lane's repo was written.

Tool installs: none. No pacman transaction was attempted (host-wide pause respected), no `uv tool`, no
`npx` install, no binary downloaded, no service or config changed.
