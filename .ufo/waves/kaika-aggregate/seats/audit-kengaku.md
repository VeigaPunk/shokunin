# audit-kengaku — round-12 aggregate, lane `kengaku-shokunin`

Read-only audit of `/home/vgpnk/Projects/shokunin/kengaku-shokunin` at its committed
HEAD. No child repo was edited, staged, or committed; the only write in this seat is
this file. Lane round derived from committed `LOG.md`; gate run with `--snapshot` on
the exact HEAD. Census-shaped counts below are **provisional** pending the parent's
census parser fix (indented Markdown source rows): do not freeze or publish them.

## Revision under audit

```
$ git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin rev-parse HEAD
a42bb40c1767e1ac24394fadda7301ae5409e7ae
$ git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin status --porcelain
<no output>   (exit 0; clean tree, no untracked files)
```

HEAD subject: `round-24 verifier spot-check (integrator, kaika): non-author admit/reject
sample + adjudication` (changes 1 file: `corpus/lessons/round-24-verifier-spotcheck.md`).

**Round selector derivation.** `LOG.md` line 231 is the last round heading:
`## Round 24 — sources registry + sourced expansion; learning from the lane's own
mistakes (kaika, 2026-10-19)`; no round-25 heading exists (`grep -n '^## ' LOG.md`).
The gate's `--round` therefore = **24**. (Gate default is 9; that run is reported
separately because r10 is selector-sensitive.)

## Gate run — primary (derived selector 24)

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/kengaku-shokunin \
    a42bb40c1767e1ac24394fadda7301ae5409e7ae --round 24
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=24
# expect kengaku-shokunin@a42bb40 ABSENT (no committed expected verdict for this revision)
# tree kengaku-shokunin revision=a42bb40c1767e1ac24394fadda7301ae5409e7ae dirty=0 mode=snapshot
... 73 CR-kengaku-shokunin-rN-M finding lines ...
# note kengaku-shokunin r7: 15 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kengaku-shokunin r7 under-coverage (not a finding): 179/240 corpus files carry no index row
# note kengaku-shokunin extracted with: git archive a42bb40c1767e1ac24394fadda7301ae5409e7ae | tar -x -C <tmp>
# verdict kengaku-shokunin failed findings=73 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
$ echo "EXIT=$?"   → EXIT=1
```

Machine-readable stats (`--json`, same command): `files=241`,
`rules={r2:0, r4:69, r7:0, r8:3, r10:1, shonen:0}`.

### Verdict

**NOT CONFORMANT at `a42bb40c1767e1ac24394fadda7301ae5409e7ae`** — gate exit **1**
(`failed`: one or more implemented CORPUS.md rule findings). Failed rule IDs:
**r4** (69 findings), **r8** (3), **r10** (1). r2, r7, and the SHONEN form check
produced 0 findings. This is conformance only as to the implemented rules (limitations
§8); it is not a whole-corpus semantic verdict.

### Secondary run — gate default selector (9)

Same command without `--round`:

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/kengaku-shokunin \
    a42bb40c1767e1ac24394fadda7301ae5409e7ae
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# verdict kengaku-shokunin failed findings=72 rules=r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)     → observed EXIT=1
```

The r10 row is therefore purely selector-driven; the lane's derived round is
24, so the primary row above is the one that stands.

## Exact failed findings

r8 and r10, verbatim from the gate:

```
CR-kengaku-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1 owner=aggregator at a42bb40 literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-9-aggregator-corpus-verdict.md:20 first4="pass" len=17 (CORPUS.md:43)
CR-kengaku-shokunin-r8-2: credential-class kv-secret occurrences=1 lines=1 files=1 owner=lane at a42bb40 literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[evidence/round12-fleet/grader_r12_draft.py] first=evidence/round12-fleet/grader_r12_draft.py:2224 first4="toke" len=17 (CORPUS.md:43)
CR-kengaku-shokunin-r8-3: credential-class op-ref occurrences=5 lines=3 files=2 owner=aggregator at a42bb40 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:56 first4="op:/" len=5 (CORPUS.md:43)
CR-kengaku-shokunin-r10-1: no corpus/lessons/round-24-aggregator-*.md — the round-24 review duty has no emitted lesson (CORPUS.md:21)
```

r4 findings, exact `file:line` (69; every line is a count-noun match with no
backticked command on the same line, per the gate's line-local rule):

```
README.md: 23
knowledge/agent-time-horizon-and-task-validity.md: 33
knowledge/attrib-r21.md: 177, 259
knowledge/bailian-cli-telemetry.md: 53
knowledge/bench-arena-round7-noise-n25.md: 59, 97
knowledge/bench-arena-task27-timeout-anatomy.md: 4, 40
knowledge/eval-design-digest-2.md: 91
knowledge/eval-design-digest-3.md: 87
knowledge/kimi-model-routing-round18.md: 49, 102, 103, 105, 129, 190, 198
knowledge/probe-battery-r19.md: 6, 39, 46, 119, 150, 169, 195, 201, 207, 209, 233, 310, 341, 354, 355, 358, 367, 379, 480, 482, 495, 497, 498, 521, 523
knowledge/telemetry-run-design.md: 37, 38, 39, 40
lessons/2026-10-16-round19-freeze-chain.md: 4, 58, 63
lessons/2026-10-16-round20-grid-closure.md: 104
lessons/2026-10-16-round21-attribution-freeze-surface.md: 192
lessons/round-11.md: 34
lessons/round-12.md: 21
lessons/round-13-coverage.md: 31
lessons/round-24.md: 85
lessons/round-4-aggregator-audit.md: 16, 47
lessons/round-4.md: 20
lessons/round-5-aggregator-audit.md: 5, 15, 30, 64
lessons/round-5.md: 14, 38
lessons/round-6-aggregator-audit.md: 120
lessons/round-7.md: 28
lessons/round-8-aggregator-box3-coldrun.md: 27
lessons/round-8.md: 44
```

Concentration: 25/69 are in `knowledge/probe-battery-r19.md`; 26 distinct files carry
r4 findings.

## Verification of the failed findings (mechanically re-derived, not adjudicated)

**r4 precision.** I re-ran the gate's own `COUNT_NOUN_RE` (extracted verbatim from
`corpus-gate.mjs:267`) over each cited line. Shape classes: 60 prose lines, 9 Markdown
table rows (e.g. `knowledge/probe-battery-r19.md:119,150,195,233,495,497,498`,
`lessons/round-24.md:85` — the latter matches `25 words` in a table *header*), and
**4 provably non-count matches** where the digit is part of a round designator:

```
README.md:23                                         "round-16 citation"
lessons/2026-10-16-round21-attribution-freeze-surface.md:192  "round-19 file"
lessons/round-5-aggregator-audit.md:30               "round-5 commit"
lessons/round-6-aggregator-audit.md:120              "round-9 probes"
```

So the r4 row is a literal rule-4 hit set (CORPUS.md:34-38 wants
`<number> — <command> <date>`), with at least 4/69 mechanically spurious matches; the
remaining 65 are genuine line-local "count with no adjacent backticked command" under
the gate's implementation. Whether each is a *rule violation in intent* is semantic and
not decided here.

**r8 literal re-check.** Using the gate's own patterns:
`op://` occurrences = 5 on 3 lines in 2 files — `lessons/round-5-aggregator-audit.md:56`
(1), `lessons/round-9-aggregator-corpus-verdict.md:9` (2), `:20` (2); every match is the
bare string `op://` inside a quoted sweep command (`grep -rn 'op://' …`,
`git grep -n 'op://' …`), `maxseg=0` (no vault path segment). The two `kv-secret`
matches are `password=|token='` (a quoted grep alternation, round-9 lesson:20) and
`token = {"brier": "brier", …` (a Python dict of field names,
`evidence/round12-fleet/grader_r12_draft.py:2224`). No secret value was observed. The
gate declares this classification could-not-evaluate and keeps the literal findings as
failed; that is the gate's own contract, not my adjudication.

**r10.** `corpus/lessons/` at HEAD contains `round-24.md` and
`round-24-verifier-spotcheck.md` but no file matching `^lessons/round-24-aggregator-.+\.md$`.
The committed non-author lesson is `round-24-verifier-spotcheck.md` (17 lines, added by
HEAD `a42bb40`), which does not match the glob. Owner attribution for the
`round-<N>-aggregator-*` pattern is aggregator-side by the gate's own owner rule
(`owner=aggregator` in the r8 rows) and by `corpus/README.md:72-73,77` (rows for the
round-6/8/9 aggregator lessons say "committed by the aggregator per `../PROTOCOL.md`;
this lane writes only this index row" / "aggregator-owned file, indexed here only"). Round-24 gate obligations that *are* visible in-lane:
`round-24.md` has its `## Gate` section (`round-24.md:56`), and the review verdict is
recorded in `round-24-verifier-spotcheck.md`; the gate's r10 check cannot see either
under the mandated filename.

## SOURCES.md structural observations (mechanical; provisional)

File: `corpus/SOURCES.md` (70 lines at HEAD).

- Registry (`## Registry`, line 19): 26 rows `S001`–`S026`, ids unique and contiguous,
  every row exactly 11 pipe-delimited cells (matching the 11-column header). `awk
  -F'|' '/^\| S[0-9]/ {print NF-2}'` → `11` for all rows.
- Enumerations: status ∈ {`mined` 18, `queued` 5, `rejected` 3}; tier ∈ {`A` 24,
  `C` 2}; no `B`, no `watch` (the intro's declared vocabulary is
  `queued|mined|rejected` and holds). Both tier-C rows (S023, S026) are `rejected`, so
  no admitted row stands on a C source.
- `used-by` pointers: the five distinct `corpus/knowledge/*.md` targets all exist at
  HEAD; `corpus/evidence/round24-sources/gate.md` (105 lines) and
  `corpus/evidence/round24-census/{base-99cf615,after}.txt` exist in `git ls-tree HEAD`.
- Contract join: each of the five round-24 knowledge entries' `source:` line names only
  rows that are tier A and status `mined` (S001/S002/S004; S005/S006/S013/S014; S007/S008;
  S009–S012; S015–S019) — a mechanical Q2-shaped check, not an admission verdict.
- Paths (`## Paths`, line 50): five chains at lines 52-56; every id in every chain
  resolves to a registry row. Two chains contain unread hops: `contamination audit`
  ends at S022 (`queued`); `agentic evidence` includes S020 and S021 (both `queued`).
  The fully-read chains are `judge calibration`, `statistical reporting`, and
  `saturation and lifecycle`.
- Intro paragraph (lines 3-5) classifies S001–S019 (ART dossier), "S020+ are new leads",
  S024–S025 (own gate outputs). S026, added by post-review commit `e21f9ea` as a
  superseding rejection of S023, is not classified there (its own row and
  `round-24.md:136` do describe it). Minor documentation-completeness observation.

**LOG/registry divergence (fidelity finding, not a gate rule).** `LOG.md:244-246`
states `SOURCES.md` has "25 rows re-opened today, `A=24 C=1`, `mined=18 queued=5
rejected=2`". At HEAD the registry is 26 rows, `A=24 C=2`, `18/5/3`
(`git show <rev>:corpus/SOURCES.md | awk -F'|' '/^\| S[0-9]/ …'`). The LOG figures
reproduce exactly at `94da19e` (25 rows, 24 A / 1 C, 18/5/2); the change landed in
`e21f9ea` (+S026), and
`git diff --stat 94da19e..HEAD -- corpus/SOURCES.md LOG.md corpus/README.md` → only
`corpus/SOURCES.md | 43 ++++++-------` (22 insertions, 21 deletions); `LOG.md` was not
touched. The 26-row state is asserted in `round-24-verifier-spotcheck.md:17`
("capability `sources-registry` (26 rows, census ok)") but the LOG census paragraph was
not corrected or errata'd. This is exactly the class QUALITY.md R1/R5 names
(`corpus/QUALITY.md:86` and `:90`); it does not affect the gate verdict (LOG is not a
graded surface).

## Provenance frontmatter scan (parent-requested, bounded)

Scope: `corpus/knowledge/*.md` (32 files) + `corpus/SOURCES.md`; keys `source:`,
`verified-at:`, `recheck:` at line start (case-insensitive), whole-file scan.

- The five round-24 entries each open with the full triad at lines 1-3, e.g.
  `corpus/knowledge/contamination-detection-and-transparency.md:1-3`:
  `source: S001 — …; S002 — …; S004 — …` / `verified-at: 2026-10-19` /
  `recheck: 2027-01-17 (90d) — re-open the three URLs and re-verify the quoted
  sentences; check for post-training detector evaluations before any new model-family
  contamination claim`. The other four use the same dated `2027-01-17 (90d) — …`
  action form (`agent-time-horizon-and-task-validity.md:3`,
  `benchmark-saturation-and-lifecycle.md:3`, `llm-judge-calibration.md:3`,
  `paired-eval-uncertainty-reporting.md:3`).
- **Ephemeral-path check: 0 hits.** No `recheck:` value and no `source:`/
  `verified-at:` value in `corpus/knowledge/` contains `/tmp/`, `.tower/`, or
  `worktrees`; `git grep -nE '^(source|verified-at|recheck):.*(/tmp/|\.tower/|worktrees)'
  HEAD -- corpus/knowledge corpus/SOURCES.md` → 0 lines. `SOURCES.md` recheck values
  are 19×`2027-01-17`, 4×`on-release`, 3×`90d`; none is a path.
- Legacy coverage: 5 files have all three keys, 8 have two, 7 have one, **12 have none**
  (5 open with `**Source basis:**`, 7 have no provenance line in the first six lines).
  17 `recheck:` lines exist in `knowledge/` overall; the legacy ones are
  `test -e ~/…` probes, not ephemeral paths. CORPUS.md:18 says every `knowledge/` entry
  opens with the triad; that literal statement does not hold for 27/32 files. This is
  reported as an observation only — QUALITY.md Q1 (`corpus/QUALITY.md:15`) is scoped to
  newly admitted entries ("Created round 24").
- Affirmative: `corpus/knowledge/` contains 0 lines naming `.tower/` or
  `worktrees/`. 40 lines mention `/tmp/…` as **historical run evidence** (e.g.
  `attrib-r21.md:492,548,614,647-648`, `bench-arena-fresh-run.md:37-40,75-80`,
  `bench-arena-round12-ladder.md:197`), none in a triad or `recheck:` line; those were
  left unchanged per the parent's instruction.

## Extracted study-path (directly evidenced, `corpus/SOURCES.md:53`)

```
- judge calibration — S012 → S009 → S010 → S011: canonical bias catalogue, then the
  newer scoring-prompt and rubric-order biases, then the correction method that prices
  sensitivity/specificity and calibrates intervals.
```

All four hops resolve to registry rows (S012 at `SOURCES.md:34`, S009 at `:31`,
S010 at `:32`, S011 at `:33`), all tier A, all status `mined`, and each has a receipt row
with URL, access date, ≤25-word quote, location and sha256 in
`corpus/evidence/round24-sources/gate.md:17-20` (verified present at HEAD). This is a
reading sequence backed by opened, receipted rows — not a Lead. It is not an assessment
of whether the ordering is good (semantic, out of scope). Secondary note: the
`contamination audit` chain (`SOURCES.md:52`) ends on S022, which is `queued`, so that
chain is a reading plan with one unread hop, not a fully read sequence.

## Gate limitations (named)

1. **Exit-3 drift is unavailable here.** `# expect kengaku-shokunin@a42bb40 ABSENT`;
   `corpus-gate.expected.json` has a frozen entry only for `kengaku-shokunin@f09ff1f`.
   The verdict rests solely on exit 1 findings; no frozen-verdict reproduction exists
   for this revision.
2. **Not-evaluated rules.** Per the gate's own registry: r1 (source citation), r3
   (falsifiability), r5 (negative claim carries its sweep), r6 (quote location), r9
   (append-only / no cross-lane edits), verifier independence, and SHONEN *truth* are
   declared not evaluated. No gate pass/fail says anything about them.
3. **r8 classification is could-not-evaluate** by construction (needs an
   operator-gated vault read). The three findings stand as literal-text failures; the
   gate never guesses schematic-vs-real.
4. **r10 is a filename-glob presence check only**, keyed to `--round`; the gate does not
   derive the lane's round. Demonstrated selector sensitivity: round 24 → 73 findings
   (r4,r8,r10); default round 9 → 72 findings (r4,r8). A caller who omits `--round`
   silently tests a round the lane left at round 9.
5. **r4 is line-local**: it requires a backticked command on the same line, so table
   rows and round designators match (4/69 provably non-count, 9/69 table rows), and
   25/69 sit in one long file. It is a literal floor, not a count-claim judgement.
6. **r7 grades phantom rows only**; under-coverage is a note, not a finding
   (`179/240 corpus files carry no index row`, provisional per the parent's census
   directive). 15 backticked path templates were skipped.
7. **`--snapshot` grades a `git archive` tree** with no history, so r9's one mechanical
   sub-check (author identity on lesson commits) is unavailable in exactly the mode
   whose verdict names a revision. `dirty=0` confirms graded bytes = committed bytes;
   no live-tree untracked corpus file was included.
8. **Rule-line citations in the gate text are stale against CORPUS.md at this
   revision.** CORPUS.md sha256 `626022a402dd099e2e2b84e049631469138ee671d10a562207e2b7a70a8f7858`
   (identical in the main repo and in the gate's worktree). Actual rule lines: r2→24-25,
   r10→27, r4→34-38, r7→46-48, r8→49-52, r9→53-56; the finding text cites :19, :21,
   :28, :40, :43 (e.g. `CORPUS.md:21` is a blank line). The checks' semantics match the
   rules; only the printed citations do not resolve. Ledger rows quoting
   `(CORPUS.md:NN)` from gate output should be treated as gate-version text, not as
   line pointers into CORPUS.md `626022a4`.
9. **Registry provenance gap in the gate itself** (gate's own header): the aggregator
   lane has no `SKILL.md`, so the gate's registry row lives inside the gate file
   (routed defect, D-120 class). Not a lane defect.
10. **Census counts provisional** per parent direction (indented Markdown source-row
    parser fix in flight); the row/status/tier numbers above are measurements at
    `a42bb40`, not final census totals.

## Residual risk and verification gaps

- Scope was one lane: I did not open the other 20 lane repos, so I cannot say whether
  the missing `round-24-aggregator-*.md` is systemic or kengaku-specific; the r10 row
  routes to the aggregator's emission duty on in-lane attribution evidence only.
- No URL in `SOURCES.md` was re-fetched (offline audit): quote text, anchors, and the
  sha256/byte counts in `corpus/evidence/round24-sources/gate.md` were verified to
  *exist and parse*, not to match live bytes or the current web.
- The r4 shape classification (prose/table/round-ref) is my mechanical re-derivation,
  not the gate's output and not a semantic adjudication of the count claims.
- No lane script was executed (`grader.py`, `plans/round24_census.sh`) — no builds,
  tests, or runs per assignment; the LOG's `CHECKS n=733` and census outputs were read,
  not reproduced.
- `corpus/QUALITY.md` Q1-Q10/R1-R10 were read as the lane's own bar; no admission
  verdict is emitted here (semantic, and the parent is sole adjudicator).
