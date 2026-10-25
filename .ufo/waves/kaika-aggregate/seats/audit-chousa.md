# audit-chousa — lane audit of `chousa-shokunin` at `d730ae4`

Seat: `KaikaAggregateR12.AuditChousa`. Measured 2026-10-19T23:47Z.
Scope: `/home/vgpnk/Projects/shokunin/chousa-shokunin` only (the original lane
directory, not a retired worktree). All child-repo access was read-only.
No file in the lane was written, staged, or committed. The only write of this
seat is this note.

## 1. Revision and tree state

Exact commands (cwd `/home/vgpnk/Projects/shokunin`):

```
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin rev-parse HEAD
  -> d730ae4c33989ad9c8535764d4cae77b4db869f6   (exit 0)
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin status --porcelain
  -> (no output)                                 (exit 0; clean tree)
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin log -1 --format='HEAD=%H%nsubject=%s%ncommit_date=%cI%nauthor=%an <%ae>'
  -> HEAD=d730ae4c33989ad9c8535764d4cae77b4db869f6
     subject=round-24 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication
     commit_date=2026-10-19T19:17:22-03:00
     author=protocol-shokunin <protocol@shokunin.local>
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin rev-parse --abbrev-ref HEAD
  -> master
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin rev-parse 'HEAD^{tree}'
  -> a1f5d697cb894ce6f3b8fd0ec01a88b42ef92eb5
```

The tree is clean, so the working tree equals the named commit. The gate
snapshot was taken from that commit (`git archive <commit> | tar -x -C <tmp>`
inside the gate), not from a worktree checkout.

## 2. Round derivation and gate selector

The committed `LOG.md` is explicit about the lane's current round:

- `LOG.md:816` — `## 2026-10-19 — round-24 opening (loop 2 round 1): claims, before-receipts, dispatch`
- `LOG.md:822` — `## Round 24 — landing (kaika campaign, tower worktree `kaika/round`, 2026-10-19)`
- `LOG.md:824` records the landing's measured HEAD as `ab19cff`; the current HEAD
  `d730ae4` is the next commit, whose subject names `round-24 verifier spot-check`.

Selector used: **`--round 24`**, derived from the committed LOG as above. For
transparency the gate defaults are also recorded:

- `--round <N>` defaults to **9** (`corpus-gate.mjs` registry: "the round whose
  aggregator lesson r10 requires").
- The parent's campaign label is "aggregator round 12". I therefore also ran
  `--round 12` and the default (no `--round`); results in §3.

The r10 check looks only for `corpus/lessons/round-<R>-aggregator-*.md` in the
graded tree. This lane carries **zero** `*-aggregator-*.md` lessons at this HEAD
(`git ls-tree -r --name-only HEAD -- corpus/lessons | grep -i aggregator` ->
no output, fallback echo `(none)`), so r10 fires for every selector; only the
round number in the finding text changes.

## 3. Gate runs — exact commands and observed output

Gate: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`
(gate id `corpus-gate-v1`).

### 3.1 Primary run (LOG-derived selector)

```
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/chousa-shokunin d730ae4c33989ad9c8535764d4cae77b4db869f6 --round 24
```

Observed (exit code of the `node` process observed directly as `1`):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=24
# expect chousa-shokunin@d730ae4 ABSENT (no committed expected verdict for this revision)
# tree chousa-shokunin revision=d730ae4c33989ad9c8535764d4cae77b4db869f6 dirty=0 mode=snapshot
CR-chousa-shokunin-r4-1 ... CR-chousa-shokunin-r4-61   (61 findings, §5.1)
CR-chousa-shokunin-r7-1 ... CR-chousa-shokunin-r7-6     (6 findings, §5.2)
CR-chousa-shokunin-r10-1                                 (1 finding, §5.3)
CR-chousa-shokunin-shonen-1                              (1 finding, §5.4)
# note chousa-shokunin r7: 31 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note chousa-shokunin r7 under-coverage (not a finding): 78/174 corpus files carry no index row
# note chousa-shokunin extracted with: git archive d730ae4c33989ad9c8535764d4cae77b4db869f6 | tar -x -C <tmp>
# verdict chousa-shokunin failed findings=69 rules=r4,r7,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Machine-readable totals from a re-run of the same snapshot/selector with
`--json` added, then parsed:
`EXIT=1 STATS={"files":175,"rules":{"r2":0,"r4":61,"r7":6,"r8":0,"r10":1,"shonen":1}}`.
`files=175` is the gate's walk of `corpus/` (TEXT_EXT only). r2 and r8 produced
no findings at this revision.

### 3.2 Selector-sensitivity runs

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/chousa-shokunin d730ae4c33989ad9c8535764d4cae77b4db869f6 --round 12 | grep -E '^(# corpus-gate|# verdict|# process-exit|CR-.*r10)'
  -> # corpus-gate-v1 — ... round-selector=12
     CR-chousa-shokunin-r10-1: no corpus/lessons/round-12-aggregator-*.md — the round-12 review duty has no emitted lesson (CORPUS.md:21)
     # verdict chousa-shokunin failed findings=69 rules=r4,r7,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
     # process-exit 1 (failed)

node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/chousa-shokunin d730ae4c33989ad9c8535764d4cae77b4db869f6 | grep -E '^(# corpus-gate|# verdict|# process-exit|CR-.*r10)'
  -> # corpus-gate-v1 — ... round-selector=9
     CR-chousa-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
     # verdict chousa-shokunin failed findings=69 rules=r4,r7,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
     # process-exit 1 (failed)
```

Caveat stated honestly: these two runs were piped through `grep`, so the shell
`$?` observed was grep's `0`; the gate's own printed line in each run is
`# process-exit 1 (failed)`. The primary run (§3.1) was not piped and its
process exit was directly observed as `1`.

Selector conclusion: exit and finding counts are selector-invariant at this
HEAD; `--round` changes only the r10 finding text.

## 4. Verdict

**not conformant** at `chousa-shokunin` HEAD
`d730ae4c33989ad9c8535764d4cae77b4db869f6` — gate exit **1 (failed)**.

Exact failed rule IDs from the gate verdict line:
**`r4`, `r7`, `r10`, `shonen`** (69 findings: r4=61, r7=6, r10=1, shonen=1).
Rules implemented but producing zero findings at this revision: r2, r8.

This is the gate's mechanical verdict per `CORPUS.md` as implemented; it is not
a whole-corpus semantic verdict (see §8).

## 5. Finding inventory at `d730ae4`

Note on paths: the gate's `README.md`, `knowledge/…`, `lessons/…` are relative
to `corpus/` (i.e. `corpus/README.md`, `corpus/knowledge/…`, `corpus/lessons/…`).

### 5.1 r4 — count claim with no backticked command on the same line (61)

Complete id/location inventory; each finding text is
`<file>:<line> count claim with no backticked command: "<60-char excerpt>" (CORPUS.md:28)`.
Full text is reproduced byte-for-byte by re-running the §3.1 command.

| id | location(s) |
|---|---|
| r4-1..3 | `README.md`:61, 256, 358 |
| r4-4 | `knowledge/anchor-boundaries-r4.md`:233 |
| r4-5..6 | `knowledge/archived-export-intake.md`:49, 59 |
| r4-7 | `knowledge/archives-verified-r9.md`:134 |
| r4-8..11 | `knowledge/audit-r11.md`:12, 47, 140, 220 |
| r4-12 | `knowledge/claim-support-states-r24.md`:22 |
| r4-13..14 | `knowledge/denylist-r22.md`:4, 28 |
| r4-15 | `knowledge/fenced-anchor-r23.md`:4 |
| r4-16 | `knowledge/fenced-heading-r17.md`:4 |
| r4-17..35 | `knowledge/hardening-r10.md`:104, 160, 231, 283, 305, 394, 414, 450, 453, 455, 484, 506, 541, 549, 552, 554, 557, 570, 587 |
| r4-36..37 | `knowledge/hardlink-alias-r13.md`:37, 46 |
| r4-38 | `knowledge/html-comment-r20.md`:4 |
| r4-39..40 | `knowledge/json-delimiter-r24.md`:43, 67 |
| r4-41 | `knowledge/pointer-boundary-r21.md`:4 |
| r4-42..43 | `knowledge/reference-integrity-r7.md`:132, 155 |
| r4-44 | `knowledge/root-slash-boundary-r15.md`:4 |
| r4-45..46 | `knowledge/scope-phrase-gap-r18.md`:4, 40 |
| r4-47 | `knowledge/sweep-symlink-r19.md`:4 |
| r4-48..50 | `lessons/2026-10-16-archive-scale-controls-and-ledger.md`:127, 161, 162 |
| r4-51..52 | `lessons/2026-10-16-gate-behavioral-baseline.md`:196, 267 |
| r4-53..56 | `lessons/2026-10-16-verify-all-composition.md`:14, 213, 227, 297 |
| r4-57..59 | `lessons/2026-10-16-verifying-conversion-not-original.md`:72, 117, 156 |
| r4-60 | `lessons/2026-10-19-hardlink-alias-boundary.md`:13 |
| r4-61 | `lessons/round-24.md`:44 |

Representative exact finding lines (verbatim from the run):

```
CR-chousa-shokunin-r4-1: README.md:61 count claim with no backticked command: "snapshot): 40 entries — 28 knowledge notes and 12 lessons" (CORPUS.md:28)
CR-chousa-shokunin-r4-12: knowledge/claim-support-states-r24.md:22 count claim with no backticked command: "| source | anchor | verbatim (≤25 words) |" (CORPUS.md:28)
CR-chousa-shokunin-r4-21: knowledge/hardening-r10.md:305 count claim with no backticked command: "Counts (71 rows): **by-design 38 · carried 25 · closed 3 · f" (CORPUS.md:28)
CR-chousa-shokunin-r4-60: lessons/2026-10-19-hardlink-alias-boundary.md:13 count claim with no backticked command: "count rule is O(1), deterministic, fails closed. Case 101 pi" (CORPUS.md:28)
CR-chousa-shokunin-r4-61: lessons/round-24.md:44 count claim with no backticked command: "verbatim, ≤25 words." (CORPUS.md:28)
```

Precision observations (evidence, not adjudication — the parent adjudicates):

- `lessons/2026-10-19-hardlink-alias-boundary.md:13` matches because the gate's
  count-noun list includes `pins`, and the line reads `Case 101 pins the
  legit-family refusal…` — `pins` is a verb here, not the count noun.
- `knowledge/claim-support-states-r24.md:22` and `lessons/round-24.md:44` are
  threshold phrases (`≤25 words`), not count claims.
- `README.md:61` is a continuation line: the owning commands
  (`ls corpus/knowledge/*.md | wc -l`, `ls corpus/lessons/*.md | wc -l`) sit on
  the following lines; the gate is line-scoped.
- `README.md:256` is a continuation line of a multi-line paragraph; the only
  backticked token nearby is the file pointer `knowledge/hardening-r10.md` on
  line 255, not a command, and the flagged line (raw text: `rounds 2–9 plus the
  r1-origin debts in 71 rows (by-design 38 · carried 25 ·`) carries no backtick.
- `knowledge/hardening-r10.md:305` etc. state ledger counts whose re-count
  command lives in surrounding prose/fences, not on the flagged line.

### 5.2 r7 — index row names a file absent from the graded tree (6)

Verbatim (all in `corpus/README.md`):

```
CR-chousa-shokunin-r7-1: index row names evidence/boundary-r4-20261016T002701Z-attacks.log — absent from the graded tree (README.md:95, CORPUS.md:40)
CR-chousa-shokunin-r7-2: index row names evidence/boundary-r4-20261016T002701Z-attacks.log — absent from the graded tree (README.md:286, CORPUS.md:40)
CR-chousa-shokunin-r7-3: index row names evidence/boundary-r4-20261016T002701Z-chain.log — absent from the graded tree (README.md:97, CORPUS.md:40)
CR-chousa-shokunin-r7-4: index row names evidence/boundary-r4-20261016T002701Z-claims.log — absent from the graded tree (README.md:96, CORPUS.md:40)
CR-chousa-shokunin-r7-5: index row names evidence/boundary-r4-20261016T002701Z-live.log — absent from the graded tree (README.md:94, CORPUS.md:40)
CR-chousa-shokunin-r7-6: index row names evidence/boundary-r4-20261016T002701Z-selftest.log — absent from the graded tree (README.md:98, CORPUS.md:40)
```

Independent check at the same HEAD (read-only):

```
git -C /home/vgpnk/Projects/shokunin/chousa-shokunin ls-tree -r --name-only HEAD -- corpus/evidence | grep -i boundary-r4
  -> 5 output lines (compacted): corpus/evidence/boundary-r4-20261016T003332Z-{attacks,chain,claims,live,selftest}.log
git ... ls-tree -r --name-only HEAD | grep 002701
  -> (no committed path contains 002701)
grep -n "002701\|003332" corpus/README.md
  -> only 002701 hits (lines 94-98, 286); no 003332 hit
```

So the six rows are genuine phantom rows: they name a superseded stamp
(`T002701Z`), while the standing committed cut at this HEAD is `T003332Z` and is
cited nowhere in `corpus/README.md`. The gate's own note says 31 backticked
templates/globs were skipped and that 78/174 corpus files carry no index row
(under-coverage is a note, not a finding).

### 5.3 r10 — round's aggregator lesson absent (1)

```
CR-chousa-shokunin-r10-1: no corpus/lessons/round-24-aggregator-*.md — the round-24 review duty has no emitted lesson (CORPUS.md:21)
```

At this HEAD, `corpus/lessons/` contains lane lessons (`round-1.md`,
`round-24.md`, `round-24-verifier-spotcheck.md`, and the dated 2026-10 lessons)
and no `*-aggregator-*` file. With `--round 12` / default `--round 9` the same
finding names `round-12` / `round-9` respectively (§3.2).

### 5.4 shonen — canonical form (1)

```
CR-chousa-shokunin-shonen-1: SHONEN.md:1 header line deviates from the canonical seed: got "# chousa — Promotion checklist", expected "# chousa-shokunin — Promotion checklist" (modulo <name>=chousa-shokunin)
```

The rest of `SHONEN.md` passed the form checks: 4 canonical box lines, all
unmarked `[ ]`, no evidence lines, no extra lines, trailing newline present.
Fleet convention observed at the 21 original lane roots
(`for f in /home/vgpnk/Projects/shokunin/*-shokunin/SHONEN.md; do head -1 "$f"; done | sort | uniq -c`):
16 use `# <repo>-shokunin — Promotion checklist`; `chousa` and `kaidoku` use
`# <short-name> — Promotion checklist`; `audio`, `game-dev-2d`, `game-dev-3d`
use `# SHONEN — probation`. Which `<name>` spelling is canonical is not decided
by the gate; the gate uses the directory basename.

## 6. SOURCES structural observations (provisional)

Parent direction in force: a census parser fix for indented Markdown source
rows is in progress elsewhere; **none of the counts below are final census
totals** and they must not be published as such. They are revision-bound
observations at `d730ae4`, re-derivable by the commands shown.

File present: `corpus/SOURCES.md` (83 lines at this HEAD).

```
grep -c '^| S0' corpus/SOURCES.md        -> 18
awk -F'|' '/^\| S0/{print NF}' corpus/SOURCES.md | sort | uniq -c
  -> 18 x NF=13                          (every registry row: 11 cells + edge pipes)
awk -F'|' '/^\| S0/{gsub(/ /,"",$9); print $9}' corpus/SOURCES.md | sort | uniq -c
  -> 8 mined / 7 queued / 3 rejected
awk -F'|' '/^\| S0/{gsub(/ /,"",$5); print $5}' corpus/SOURCES.md | sort | uniq -c
  -> 14 A / 1 B / 3 C
awk ... empty status/scope/opened      -> no output (none empty)
grep -n sections                        -> ## Paths:30, ## Search log:46, ## Leads (unopened):72
grep -c '^- [A-Z].*— S0'                -> 4 Paths bullets
```

Observed row shape: each registry row is a **single-line** Markdown table row
(`| S0…`), not an indented list entry. Whether the pending parser fix changes
how this shape is counted is not evaluated here.

Ids used in the `## Paths` bullets (`S001 S002 S003 S004 S005 S006 S007 S008
S009 S010 S011 S012 S013 S017`) all resolve to registry rows; registry rows not
named in any path: `S014 S015 S016 S018`. Search log is bounded (3 entries,
included counts 13/3/2 as written there); Leads are explicitly unopened and are
**not** used as evidence in this note.

### 6.1 Extracted study path (directly evidenced)

`corpus/SOURCES.md:36-39`, verbatim:

```
- Following a citation chain — S003 → S005 → S006 → S007 → S010: trace to the
  original context, then expect fidelity loss per hop, split access, relevance,
  and support, keep support distinct from truth, and evaluate each claim in its
  full retrieval context.
```

Resolved against the registry rows (name / tier / status / `teaches` cell; all
rows state `opened 2026-10-19`):

1. **S003** — SIFT (The Four Moves), Mike Caulfield — docs, A, mined —
   https://hapgood.us/2019/06/19/sift-the-four-moves/ — "The four moves: stop,
   investigate the source, find better coverage, and trace claims, quotes, and
   media back to the original context."
2. **S005** — Chen, Teplitskiy, Jurgens, The Noisy Path from Source to Citation
   — paper, A, mined — https://aclanthology.org/2025.acl-long.1534/ — "Citation
   fidelity varies measurably and low fidelity at one hop predicts lower
   fidelity downstream — the telephone effect."
3. **S006** — Onweller et al., Cited but Not Verified — paper, A, mined —
   https://arxiv.org/html/2605.06635v1 — "Split citation checks into link
   accessibility, topical relevance, and factual support — three separately
   failable checks."
4. **S007** — Li et al., DeepResearch Bench II — paper, A, mined —
   https://arxiv.org/html/2601.08536v3 — "Whether a citation supports a claim
   is separate from whether the cited information is correct."
5. **S010** — Xu et al., CiteEval — paper, A, **queued** —
   https://aclanthology.org/2025.acl-long.1574/ — "NLI-style binary support is
   a suboptimal proxy; evaluate citations across the full query, retrieval, and
   generated-answer context."

Evidence status: the sequence is the lane's declared reading order, and the
`teaches` text is the lane's claim about each opened source. I did not re-open
the external URLs (no network in this audit), so anchors/quotes were not
independently re-verified; the registry says each row was opened 2026-10-19.

## 7. Provenance frontmatter scan of `corpus/knowledge/*.md` (parent direction)

Bounded to the provenance keys `source:`, `verified-at:`, `recheck:`.

```
grep -rn "^source:" corpus/knowledge/          -> 29 matches in 28 files
                                                  (archived-export-intake.md carries 2: lines 2 and 16)
grep -rL "^recheck:" corpus/knowledge/*.md      -> 3 files:
   corpus/knowledge/archives-verified-r9.md
   corpus/knowledge/audit-r11.md
   corpus/knowledge/gate-baseline-r8.md
grep -rn "\.tower/worktrees\|/tmp" corpus/knowledge/
   -> corpus/knowledge/chain-resolution-r3.md:213  ("...this seat's own python, `/tmp` only; ...")
   -> corpus/knowledge/gate-baseline-r8.md:186     ("bash tools/research-gate.sh --pin /tmp/<new>.txt ..." inside a fence)
```

Round-24 entries (the four admitted this round) carry all three keys; exact
`recheck:` values:

- `corpus/knowledge/citation-chain-fidelity-r24.md:5` —
  `recheck: 90d (`bash tools/research-gate.sh verify-chain corpus/fixtures/chain-r3.md --root ..` confirms the resolve-only boundary at the then-current gate; re-open S005 §4/§6 and the S003 section for revisions)`
- `corpus/knowledge/claim-support-states-r24.md:5` —
  `recheck: 90d (re-open S006 §3.3 and S007 §2.1 — a new arXiv version may renumber or rephrase the anchors; `grep -n 'None of the five proves' corpus/README.md` for the known-gaps bullet)`
- `corpus/knowledge/contextual-source-admission-r24.md:4` —
  `recheck: on-release (S004, Cochrane Handbook — v6.5 / chapter last updated Oct 2019 as read); 365d (S002 commitments page, S003 post)`
- `corpus/knowledge/json-delimiter-r24.md:5` —
  `recheck: 90d (`bash tools/research-gate.sh --selftest` — cases 134–136 pin the arms; re-open S013 §3 for a format revision)`

**No `recheck:` value points into `.tower/worktrees` or `/tmp`.** The two
ephemeral-path hits above are (a) historical prose describing an independent
check run in `/tmp` and (b) a fenced template command with a `/tmp/<new>.txt`
placeholder — neither is a provenance `recheck:` value, and both are historical
bytes left unchanged per instruction.

Cycle check (observed, no semantic tier judgment): the four r24 entries cite
only `mined` rows, and the registry's `used-by` cells for all 8 mined rows map
exactly onto those entries — S001→`json-delimiter-r24.md`; S002/S004→
`contextual-source-admission-r24.md`; S003→`contextual-source-admission-r24.md`
and `citation-chain-fidelity-r24.md`; S005→`citation-chain-fidelity-r24.md`;
S006/S007→`claim-support-states-r24.md`; S013→`json-delimiter-r24.md`.

The three files lacking `^recheck:` are exactly the legacy headers the lane's
own round-24 lesson names as its open defect (M-13 in
`corpus/lessons/round-24.md`, "the 3 legacy headers are queued r25"). This is
reported as an observation, not a gate rule: the gate-graded rules r2/r8
produced no finding here, and `QUALITY.md` criterion 6 binds entries admitted
from round 24 on.

## 8. Gate limitations and declared not-evaluated (from the gate's own registry)

- Not evaluated by the gate at all: **r1** (source citation — semantic), **r3**
  (falsifiable/opinion — semantic), **r5** (negative claim carries its sweep —
  needs negation+proximity parsing), **r6** (quote names its location — needs
  the quoted surface outside the repo), **r9** (append-only/no-cross-lane-edit
  — history-dependent; snapshot mode grades a `git archive` tree with no
  history). Also not evaluated: **verifier independence** (whether an `[x]`
  rests on a non-author) and **SHONEN semantics** (whether a box claim is true).
- **r8** is literal-text only; the schematic-vs-real classification of a
  credential-shaped match is declared could-not-evaluate (needs a vault read).
  At this revision r8 emitted no finding.
- **r4** is a line-scoped regex over a fixed count-noun list: it skips lines
  containing a backtick and fires on thresholds, continuation lines, and
  noun/verb collisions (concrete examples in §5.1). The 61 r4 findings are the
  mechanical count, not 61 adjudicated defects.
- **r7** grades phantom rows only (file without row is a note: 78/174); 31
  path templates/globs were skipped. The 6 findings here are independently
  confirmed stale names (§5.2).
- **r10** checks only the presence of a file matching
  `corpus/lessons/round-<R>-aggregator-*.md`; it cannot judge the round
  review's content. The `--round` selector is caller-chosen (default 9); at
  this HEAD the result is the same for 24/12/9 because the lane has no
  aggregator lesson for any round.
- **shonen** checks canonical form only (header/boxes/marks/evidence-line
  shape/trailing newline); the one finding is the header name. "Only a
  non-author may write `[x]`" is not checkable from the tree.
- **Frozen-expectation drift (exit 3)** was not exercised: the gate printed
  `# expect chousa-shokunin@d730ae4 ABSENT (no committed expected verdict for
  this revision)`. Exit precedence 2 > 3 > 1 > 0 therefore resolved to 1.
- The gate's verdict is per-repo, lane-local evidence and is **not** a
  whole-corpus semantic-conformance verdict, and not a SHONEN truth verdict.

## 9. Limits of this audit

- Only `chousa-shokunin` was inspected, at the single revision named above.
- Inspected committed surfaces: `corpus/SOURCES.md`, `corpus/README.md`,
  `corpus/QUALITY.md` (there is no root `QUALITY.md`; `wc -l QUALITY.md` ->
  "No such file or directory", exit 1), root `README.md`, root `SHONEN.md`, the
  lessons implicated by r4 findings, and the round-24 lesson.
- `corpus/README.md` is 505 lines; only the regions implicated by gate findings
  were read in full (plus the coverage-map/round-4/limit-trail regions).
- No network; external sources in `SOURCES.md` were not re-opened and their
  anchors were not independently verified.
- No builds, tests, lint, or formatting were run. The gate's own `--selftest`
  was not run (out of scope); only `--snapshot` mode was used.
- Counts in §6 are revision-bound observations pending the parent's census
  parser fix and are explicitly **not** final totals. No numeric score was
  produced or implied.
