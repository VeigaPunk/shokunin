# audit — kasegi-shokunin (round 12 aggregator sweep)

Seat: `KaikaAggregateR12.AuditKasegi`. Lane audited: `/home/vgpnk/Projects/shokunin/kasegi-shokunin`
(original repo, not a worktree). All commands below ran read-only against that
path; the only write is this note. Machine-readable corpus-gate source:
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`
(gate id `corpus-gate-v1`, run from the fleet-aggregate worktree root).

**Verdict at the named revision: NOT CONFORMANT** — `corpus-gate-v1` exits `1`
(failed) at `13a51920068c48c0c5b3c8c81d5af0df6d4ea337`, under both the derived
lane-round selector and the gate default. This is a gate verdict on its
implemented rule subset, not a whole-corpus semantic judgement.

## 1. Revision and cleanliness (exact)

```
$ git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin rev-parse HEAD
13a51920068c48c0c5b3c8c81d5af0df6d4ea337
exit=0
$ git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin status --porcelain
(no output)
exit=0, 0 lines
$ git -C ... rev-parse --abbrev-ref HEAD
master
```

HEAD subject: `round-22 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication`.

## 2. Round selector used (and why)

Derived from the lane's committed `LOG.md`: the last round entry is
`## Round 22 — 2026-10-19 — kaika: QUALITY bar, source registry, frontier, provenance disclosure`
(`LOG.md:1046`), and the newest commits are round-22 commits. The gate's
`--round` selector only feeds the r10 check, so both selectors were run:

| run | selector | findings | rules | exit |
|---|---|---|---|---|
| A | gate default `--round 9` (no `--round`) | 62 | r2, r4, r8 | 1 |
| B | derived lane round `--round 22` | 63 | r2, r4, r8, r10 | 1 |

The 1-finding delta is exactly r10 and is selector-driven (§6). Default
selector was **not** silently assumed; run A is reported for completeness.

## 3. Exact commands and outputs

Run A:

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/kasegi-shokunin \
    13a51920068c48c0c5b3c8c81d5af0df6d4ea337
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect kasegi-shokunin@13a5192 ABSENT (no committed expected verdict for this revision)
# tree kasegi-shokunin revision=13a51920068c48c0c5b3c8c81d5af0df6d4ea337 dirty=0 mode=snapshot
...62 CR-kasegi-shokunin-* finding lines...
# note kasegi-shokunin r7: 5 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kasegi-shokunin r7 under-coverage (not a finding): 36/65 corpus files carry no index row
# note kasegi-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one's examples")
# note kasegi-shokunin extracted with: git archive 13a51920068c48c0c5b3c8c81d5af0df6d4ea337 | tar -x -C <tmp>
# verdict kasegi-shokunin failed findings=62 rules=r2,r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

Run B: identical invocation plus `--round 22`; first line becomes
`round-selector=22`; verdict line:

```
# verdict kasegi-shokunin failed findings=63 rules=r2,r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

Per-rule tally at run B (`grep -c`/`uniq -c` over the output): r2=3, r4=56,
r8=3, r10=1. No r7 finding; no SHONEN finding.

## 4. Exact failed rules and finding IDs

### r2 (CORPUS.md:25, "`lessons/` entries cite the round and the evidence")

```
CR-kasegi-shokunin-r2-1: lessons/round-10.md carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)
CR-kasegi-shokunin-r2-2: lessons/round-12.md carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)
CR-kasegi-shokunin-r2-3: lessons/round-13.md carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)
```

Verified by reading all three files in full:

- `round-10.md` (read: 1,723 B): cites round 10; its only commit-adjacent text is
  line 20 "commit + file + captured-source sha256" — it names **no** hash, report,
  or LOG line.
- `round-12.md` (2,752 B): the only hex-ish token is `bh953b65628b4e` (line 27),
  a workspace directory name, not a revision.
- `round-13.md` (3,780 B): line 3-4 says "Round 12 ended without a commit in
  either repo (kasegi HEAD was still round-11; the r12 report sat untracked…)"
  — it discusses a missing commit but records no revision or report path.

The three findings are genuine under the rule as written. All three *do* cite
their own round, so the finding is the evidence pointer only.

### r4 (CORPUS.md:34, "A count carries its command")

56 findings, all of the gate's shape "count-noun regex matched, line contains no
backtick". Distribution (`grep -oE '^CR-kasegi-shokunin-r4-[0-9]+: [^:]+'` tally):

```
12 knowledge/ufo-workspaces.md
 7 README.md
 5 knowledge/target-checkouts.md
 3 lessons/round-4-aggregator-audit.md
 3 lessons/round-22.md
 3 knowledge/submitted-registry.md
 3 knowledge/source-tree-loss-2026-09-28.md
 2 lessons/round-5-aggregator-audit.md
 2 knowledge/mission-ledger.md
 2 knowledge/mission-control.md
 2 knowledge/claim-package-contract.md
 2 knowledge/claim-anatomy-sample.md
10 files x 1
```

Representative exact lines:

```
CR-kasegi-shokunin-r4-1: README.md:5 count claim with no backticked command: "its source. No generic filler. [r22 correction: this holds f" (CORPUS.md:28)
CR-kasegi-shokunin-r4-2: README.md:44 count claim with no backticked command: "| Lessons (r22 correction) | lessons/round-1.md … lessons/ro" (CORPUS.md:28)
CR-kasegi-shokunin-r4-47: lessons/round-22.md:72 count claim with no backticked command: "27 rows, all opened 2026-10-19 by the sources executor; the " (CORPUS.md:28)
```

Spot-checked lines confirm the mechanical predicate: README lines 5, 44, 51,
118, 130, 131, 150 each contain exactly 0 backticks and a matching count-noun.
**Calibration:** these are *format* hits, not proven unreproducible counts. The
lane's own append-only correction convention ("[rNN correction: …]" prose with
arrowed old→new numbers) concentrates the findings in correction markers
(round-12/13/14/22 and the matched knowledge files). Two demonstrated error
directions in the proxy:

- false pass: README.md:132 contains `3d28a716` (a commit short hash), so it
  passes the "has a backtick" test although the line is a count/repair claim;
- false fail: README.md:131 ("grep tallies (strict 9→4 files; naive
  471/61→402/91; …)") carries its command in the referenced round-13 lesson,
  not on the same line; the gate cannot see adjacent-line commands.

### r8 (CORPUS.md:49-52, "No credential material, ever … including this one's examples")

```
CR-kasegi-shokunin-r8-1: credential-class kv-secret occurrences=2 lines=2 files=2 owner=lane at 13a5192 literal_shaped=0/2 :: classification=could-not-evaluate ... files=[instruments/density.py,instruments/resolve.py] first=instruments/density.py:52 first4="TOKE" len=34 (CORPUS.md:43)
CR-kasegi-shokunin-r8-2: credential-class op-ref occurrences=6 lines=4 files=3 owner=aggregator at 13a5192 maxseg=0 :: classification=could-not-evaluate ... files=[lessons/round-5-aggregator-audit.md,lessons/round-6-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:50 first4="op:/" len=5 (CORPUS.md:43)
CR-kasegi-shokunin-r8-3: credential-class op-ref occurrences=2 lines=2 files=1 owner=lane at 13a5192 maxseg=0 :: classification=could-not-evaluate ... files=[instruments/citation-survival.tsv] first=instruments/citation-survival.tsv:127 first4="op:/" len=5 (CORPUS.md:43)
```

Verified:

- **r8-1 is a shape false positive.** Both hits are the same Python line, a regex
  constant named `TOKEN`:
  `corpus/instruments/density.py:52` and `corpus/instruments/resolve.py:83`:
  `TOKEN = re.compile(r"`([^`\n]+)`")`. The gate's `kv-secret` regex
  (`corpus-gate.mjs:282`) matches `token\s*[=:]\s*\S{8,}` case-insensitively, so a
  code identifier trips it. The gate itself reports `literal_shaped=0/2`
  (its `isLiteralShaped` test rejects parentheses/quotes/backslashes). No
  credential material in the matched text.
- **r8-2/r8-3 are literal `op://` mentions with zero path segments**
  (`maxseg=0`), i.e. no vault-shaped reference at all. All occurrences are
  self-describing sweep prose or census rows: `round-5-aggregator-audit.md:50`
  ("credentials sweep ✓ (0 `op://`;"), `round-6-aggregator-audit.md:31` ("the
  single `op://` hit is a literal"), `round-9-aggregator-corpus-verdict.md:18`
  and `:40` (table cells quoting `git grep -n 'op://' b7180b0 -- corpus/`),
  `instruments/citation-survival.tsv:127` (a census token-kind row whose key is
  the scheme) and `:944` (a quoted grep command).
- Under CORPUS.md's **literal** wording ("stay out of every corpus, including
  this one's examples") these are genuine rule violations; **credential reality
  is not established**. The lane's own `round-9-aggregator-corpus-verdict.md:18`
  already recorded rule 8 as "FAIL-literal / PASS-intent" with 2 schematic hits
  at `b7180b0`; the count is now 8 (6 in aggregator-named lessons + 2 in the
  TSV). The set is **self-amplifying**: each audit lesson that quotes the sweep
  adds another literal occurrence.
- Ownership note: r8-2 is routed `owner=aggregator` **by filename pattern**
  (`round-\d+-aggregator-*`), not by authorship; the bytes live in this lane's
  tree at this revision.

### r10 (CORPUS.md:27, selector-dependent)

```
CR-kasegi-shokunin-r10-1: no corpus/lessons/round-22-aggregator-*.md — the round-22 review duty has no emitted lesson (CORPUS.md:21)
```

Ownership clarification: r10 asks whether the **aggregator's** round-22 review
lesson was filed into this lane's corpus. The lane's own round-22 lesson **does
exist** (`corpus/lessons/round-22.md`, 25,300 B, includes a `## Gate` section
covering S001–S027). What is absent is a file matching `round-22-aggregator-*`.
So r10-1 is an aggregator-side artifact gap in the lane tree at this revision,
not evidence that kasegi failed to write its round lesson. No
`round-22-aggregator-*` exists; the newest aggregator-named lesson is
`round-9-aggregator-corpus-verdict.md`.

## 5. Direct observation the gate does not implement: missing `## Gate` sections

CORPUS.md:19 requires every `lessons/round-<N>.md` to carry a `## Gate` section
(candidates, admitted, rejected with reasons, spot-check result). This rule is
**not** in `rules-implemented`. Measured at HEAD:

```
$ ls corpus/lessons/*.md | wc -l
26
$ ls corpus/lessons/round-[0-9]*.md | grep -cE 'round-[0-9]+\.md$'
15
$ grep -l '^## Gate' corpus/lessons/*.md | wc -l
4
$ grep -L '^## Gate' corpus/lessons/*.md | wc -l
22
```

The four with `## Gate`: `round-8-aggregator-box3-coldrun.md`,
`round-17-mirror-relocation.md`, `round-21-routing-blocked.md`, `round-22.md`.
The 22 without include the three r2-flagged lessons (`round-10`, `round-12`,
`round-13`) and `round-22-verifier-spotcheck.md`. Practice improved in the last
three authored rounds but the corpus-wide requirement is unmet — **22/26 lesson
files at 13a5192**.

Related direct defect in README's own index row (`corpus/README.md:44`):
it states `(25 files; gaps at 2, 16, 18, 19)`. At this revision the directory
holds **26** `.md` files, and exact `round-<N>.md` names are absent for
2, 16, 17, 18, 19, 20, 21 (rounds 17/20/21 exist under descriptive filenames,
which the same row's prose acknowledges). The count is off by one and the gap
list is only valid under content-counting. Likely the row was written before
`round-22-verifier-spotcheck.md` landed, but at the committed revision the
claim does not reproduce. This is the underlying number defect behind r4-2.

## 6. Gate-side defect: stale CORPUS.md line citations

Every implemented rule's `(CORPUS.md:N)` citation in the output points at the
wrong line of the current `CORPUS.md` (fleet-aggregate worktree):

| rule | gate cites | actual rule text |
|---|---|---|
| r2 | CORPUS.md:19 | `:25` — "`lessons/` entries cite the round and the evidence (LOG.md round, commit, report)." (line 19 is the *different* `## Gate` rule) |
| r4 | CORPUS.md:28 | `:34` — "**A count carries its command.**" (line 28 is blank) |
| r8 | CORPUS.md:43 | `:49` — "**No credential material, ever.**" (line 43 is the "quote names its location" bullet) |
| r10 | CORPUS.md:21 | `:27` — "The aggregator reviews every corpus each round…" (line 21 is blank) |

Consequence for the round's ledger: citing "(CORPUS.md:19)" for an r2 failure
sends a reader to the `## Gate` section requirement. The finding texts are
correct; the rule references are not. This is a gate/registry defect, not a
lane defect — reported so the parent does not copy the citations forward.

## 7. SOURCES structural observations (lane-local, reproduced)

`corpus/SOURCES.md` was inspected in full, then the **canonical census**
committed in `CORPUS.md:133-154` was run verbatim from the lane root
(`cd /home/vgpnk/Projects/shokunin/kasegi-shokunin`). Exact outputs:

```
--- rows ---
27
--- malformed (expect 0) ---
0
--- tier hist ---
A=25 C=2
--- status hist ---
mined=15 queued=10 rejected=2
--- dup ids (expect empty) ---
--- enum/tier-inflation (expect empty) ---
--- mined used-by missing (expect empty) ---
```

All seven recorded values in `lessons/round-22.md` §Gate census reproduce
exactly. Structural observations beyond the census:

- **Status semantics hold.** All 15 `mined` rows carry a `used-by` path that
  resolves in-tree (`awk` census above printed nothing missing); all 10
  `queued` and 2 `rejected` rows use `—`.
- **Rejected form holds.** S026 (CISA Gold Eagle, tier C) and S027 (HN item,
  tier C) both open their `teaches` with `REJECTED: <reason>; flip: <what would
  change the verdict>`.
- **Tier discipline holds.** A=25, C=2; no `community` row carries tier A.
- **Contract rule 1 record present.** `lessons/round-22.md` `## Gate` table
  covers exactly S001–S027 (set-equal to the registry rows; verified by id
  extraction on both files), each with URL, `accessed 2026-10-19`, a quote and a
  location. **I did not re-open any URL**, so quote verbatimness is not verified
  here (the lesson's own L1/critic re-open statement is a lane claim).
- **Search log** has 6 entries, each carrying identified/screened/included/
  excluded counts plus a stop rationale; two exclusions state their reason
  (S026, S027). PRISMA-inspired fields are present, not merely asserted.
- **Leads** lists 3 unopened items (Big Sleep tracker, ISO/IEC 29147+30111,
  UK AISI). These were **not** used as evidence anywhere in this audit.
- **Paths** declares three reading sequences; only one is composed entirely of
  `mined` rows (§8). The other two traverse `queued` rows (S016–S024, S025) and
  are prospective reading plans, not evidence.
- `SOURCES.md` contains **0** lines that would trip the gate's r4 predicate if
  r4 graded that file (it does not — §9). No `op://` occurs in `SOURCES.md`
  itself; the lane's r8-3 hits are in `instruments/citation-survival.tsv`.

## 8. Extracted study / reading sequence (directly evidenced)

Verbatim from `corpus/SOURCES.md` §Paths:

> CVSS severity and CWE prioritization — S002 → S001 → S013 → S014 → S015:
> learn the metric semantics and scoring language before examining the Top 25
> dataset method, interpretation and dated rank list.

Per-node registry evidence at HEAD (all five are `mined`, i.e. every step is an
opened source, not a lead):

| step | row facts | anchor | used-by (exists) |
|---|---|---|---|
| S002 | FIRST CVSS v4.0 Specification, kind `spec`, tier A, mined, opened 2026-10-19 | "Introduction and Assessment; Document Version 1.2" | `corpus/knowledge/cvss-v4-severity-and-vector.md` |
| S001 | FIRST CVSS v4.0 User Guide, `docs`, A, mined, 2026-10-19 | "CVSS Base Score (CVSS-B) Measures Severity, not Risk; Document Version 1.2" | `corpus/knowledge/cvss-v4-severity-and-vector.md` |
| S013 | MITRE 2025 CWE Top 25 Methodology, `docs`, A, mined, 2026-10-19 | "LLM Mapping Suggestions, CNA Expert Collaboration, Removal of CWE Mapping Normalization and Scoring; page last updated 2026-01-23" | `corpus/knowledge/cwe-top25-2025-methodology.md` |
| S014 | MITRE 2025 Key Insights, `docs`, A, mined, 2026-10-19 | "Mapping Usage and Abstraction; page last updated 2025-12-10" | `corpus/knowledge/cwe-top25-2025-methodology.md` |
| S015 | MITRE 2025 Top 25 list, `dataset`, A, mined, 2026-10-19 | "2025 CWE Top 25 … CWE-79 row; page last updated 2025-12-15" | `corpus/knowledge/cwe-top25-2025-methodology.md` |

Reusability: the two landing entries are committed and each cites its own source
ids — `cvss-v4-severity-and-vector.md` cites S001/S002, and
`cwe-top25-2025-methodology.md` cites S013/S014/S015 (verified by id extraction
from both files). So the path terminates in in-tree notes, not only in external
URLs. What is **directly evidenced** is: row existence, tier/status/opened, the
anchors, and the used-by resolution. What is **lane curation** is the ordering
rationale (learn scoring language before the dataset method), which rests on the
`teaches` fields, not on an external authority. No step crosses an unopened
lead.

## 9. Bounded provenance-frontmatter scan (parent request)

Scope: `corpus/knowledge/**/*.md` at 13a5192 (30 files). Checked for column-0
`source:`, `verified-at:`, `recheck:` and for ephemeral paths in those values.

- **30/30 files carry all three keys.** 5 files carry them top-of-file
  (directly under the H1, lines 2–4): the five round-22 entries
  `cvss-v4-severity-and-vector.md`, `coordinated-disclosure-timelines.md`,
  `authorization-safe-harbor-and-scope.md`, `ai-assisted-finding-validation.md`,
  `cwe-top25-2025-methodology.md`.
- **25 files carry them in an appended `## Provenance (round-22 correction,
  appended)` block**, `source:` at lines 33–485 (e.g. `policy-access-playbook.md:33`,
  `triage-thresholds.md:485`). This matches `QUALITY.md`'s declared legacy
  disclosure form and README's "25 legacy / five round-22" split; it also
  preserves the R6 line-anchor requirement (nothing inserted at line 2).
- **No `source:` / `verified-at:` / `recheck:` value names an ephemeral path.**
  `grep -rn -E "^(recheck|source|verified-at):" corpus/knowledge/ | grep -E
  "\.tower/worktrees|/tmp"` → **no output**.
- **Fidelity observation (body prose, not provenance fields):** two legacy
  entries cite ephemeral scratch bases as their evidence base:
  `claim-anatomy-sample.md:5` (`/tmp/kasegi-r14/select20.sh`), `:8`
  (`/tmp/kasegi-r14/scout-anatomy-20.md`, `/tmp/kasegi-r14/raw20-dump.txt`), and
  `source-tree-loss-2026-09-28.md:8, :159, :171, :241`
  (`/tmp/kasegi-r15/sentinel-forensics.md`, `/tmp/kasegi-r15/ev-smoke`,
  `/tmp/kasegi-r15/resolve.py`, `/tmp/kasegi-r15/`). These are unreceiptable
  scratch paths inside `/tmp`; README's row says the r14 selection "script
  preserved", but I did not verify that preservation in-tree. Reported as a
  provenance/fidelity observation, **not** as a gate rule or semantic verdict.
  Historical evidence text was left unchanged (read-only lane).
- Observed in passing while deriving the round (outside my assigned inspect set):
  `LOG.md:1061-1062` names a `/tmp` scout-sweep record as motivating evidence.
  Same class of ephemeral basis; not counted in the totals above.

## 10. Named gate limitations (so this verdict is not over-read)

1. **Implemented subset only:** r2, r4, r7, r8-literal, r10, SHONEN *form*.
   r1/r3/r5/r6/r9 are not implemented; verifier independence and SHONEN *truth*
   are declared could-not-evaluate by the gate itself. `SHONEN.md` emitted no
   finding here, which means sole canonical-form conformance (4 boxes, marks,
   evidence lines, no stray lines); its four boxes are all unchecked at HEAD, so
   promotion is not claimed — truth untested.
2. **r4 surface and predicate:** grades `README.md`, `knowledge/*.md`,
   `lessons/*.md` only — `SOURCES.md`, `QUALITY.md`, and `instruments/` are
   ungraded. Predicate is count-noun regex ∧ no backtick on the same line; it
   never checks that the backtick is a *command* or that the command reproduces
   the number, and cannot see a wrapped command on an adjacent line (§4 shows
   both false-pass and false-fail).
3. **r2 predicate:** a regex for 7–40 hex chars, `.ufo/reports/`, or `LOG.md`,
   applied per file. Prose like "the report" fails; any incidental hex-looking
   word would pass. Round-citation is per file, not per entry.
4. **r7:** checks README index rows only; skipped 5 template/glob paths
   containing `* < { ~ $ …` (this includes the `instruments/{density.py,…}` row,
   so that row's members are ungraded); 36/65 corpus files carry no index row is
   a note, not a finding.
5. **r8:** literal text over `corpus/` files with known text extensions, unit =
   occurrences; reality classification is could-not-evaluate by design; the
   value-shape heuristic false-positives code identifiers (§4).
6. **r10:** filename existence only — any content passing the glob satisfies it;
   and the 62 vs 63 delta is entirely the selector.
7. **No frozen expectation for this revision:** `# expect … ABSENT` — exit-3
   drift detection was not exercised at 13a5192.
8. **Snapshot fidelity:** grading reads a `git archive` extraction of the named
   commit (`dirty=0`), so worktree/untracked content is out of scope by
   construction. No export-ignore concern in this lane: `git ls-files | grep -c
   gitattributes` → `0`.
9. **No source-truth check:** nothing in the gate evaluates quote verbatimness,
   URL reachability, or the SOURCES registry contract. §7's census reproduction
   is a separate lane-local check using the contract's own committed commands,
   not a gate rule.

## 11. Provisionality

Fleet census/parser work for indented Markdown source rows is in progress
elsewhere. Every number in this note is a **lane-local fact at
13a5192** (27 SOURCES rows, 26 lesson files, 30 knowledge entries, 63/62 gate
findings). None of it is a frozen fleet census total; do not aggregate it before
the parent's exact `FINAL LANES READY` signal. Nothing here was published to
README/LOG/SCORECARD/MANIFEST or any gate script.

## 12. What I did not do

No URL re-open; no lane instrument run (`density.py`, `resolve.py`,
`anchorcheck.py`, `test_resolve.py`); no anchorcheck base-equality
re-derivation (the `LOG.md` r22 claim is recorded as a lane claim, not verified
by me); no build/test/lint/format; no verifier-independence or SHONEN-truth
adjudication; no mutation of any child repo (only `read`/`grep`/`awk`/`git`
read commands above). The only file written is this note.
