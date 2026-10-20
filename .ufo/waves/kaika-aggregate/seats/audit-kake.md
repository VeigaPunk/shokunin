# audit-kake — kake-shokunin corpus audit @ 7e17c66

Seat: KaikaAggregateR12.AuditKake (aggregator round 12, kaika fleet-aggregate).
Subject: original repo `/home/vgpnk/Projects/shokunin/kake-shokunin` (not a worktree).
Scope: gate conformance at one named revision, SOURCES structural observations, one
evidenced study path, and the parent-requested provenance-frontmatter scan.
Status of numbers below: **revision-bound to `7e17c663b8713daac27774d49d87c4d44ea30747`;
no census totals are frozen here** (parent direction: census parser fix in progress; final
census waits for `FINAL LANES READY`).

## 1. Revision binding

```
$ git -C /home/vgpnk/Projects/shokunin/kake-shokunin rev-parse HEAD
7e17c663b8713daac27774d49d87c4d44ea30747

$ git -C /home/vgpnk/Projects/shokunin/kake-shokunin status --porcelain
(no output; 0 lines; exit 0)
```
Re-checked after the scan work: HEAD unchanged, porcelain still 0 lines. The lane was never
written by this seat (read-only contract held).

Round derivation (used for the gate's `--round`): `LOG.md:641` heading
`## Round 20 — post-review fixes (2026-10-19)`, `LOG.md:600`
`## 2026-10-19 — round 20 resume (kaika campaign): three claims landed`, and the committed
`.ufo/round-20/` tree. HEAD's own message is
`round-20 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication`.
=> selector `--round 20`. The gate's documented default is 9 (`corpus-gate.mjs:45`); both
runs are recorded in §2 so the selector's effect is visible.

## 2. Gate run (exact)

Primary run (derived round):

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/kake-shokunin \
    7e17c663b8713daac27774d49d87c4d44ea30747 --round 20
```

Observed head lines (verbatim):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=20
# expect kake-shokunin@7e17c66 ABSENT (no committed expected verdict for this revision)
# tree kake-shokunin revision=7e17c663b8713daac27774d49d87c4d44ea30747 dirty=0 mode=snapshot
...
# note kake-shokunin r7: 2 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kake-shokunin r7 under-coverage (not a finding): 22/48 corpus files carry no index row
# note kake-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one's examples")
# note kake-shokunin extracted with: git archive 7e17c663b8713daac27774d49d87c4d44ea30747 | tar -x -C <tmp>
# verdict kake-shokunin failed findings=54 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Exit: **1** (`failed`). `expect … ABSENT` means exit 3 (frozen-expectation drift) did not
apply; this is a live rule failure, not drift.

Selector sensitivity run (same revision, gate default round):

```
$ node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/kake-shokunin \
    7e17c663b8713daac27774d49d87c4d44ea30747
...
# verdict kake-shokunin failed findings=53 rules=r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```
Exit 1, 53 findings. The only delta is `CR-kake-shokunin-r10-1` (round 20's aggregator
lesson absent); a round-9 aggregator lesson exists
(`corpus/lessons/round-9-aggregator-corpus-verdict.md`).

## 3. Verdict

**not conformant** at `7e17c663b8713daac27774d49d87c4d44ea30747` (gate exit 1).

Failed rule IDs and finding ids:

| rule | findings | ids |
|---|---|---|
| r4 (CORPUS.md:28) | 52 | `CR-kake-shokunin-r4-1` … `CR-kake-shokunin-r4-52` |
| r8 (CORPUS.md:43) | 1 | `CR-kake-shokunin-r8-1` (occurrences=3, lines=3, files=3, owner=aggregator, maxseg=1) |
| r10 (CORPUS.md:21) | 1 | `CR-kake-shokunin-r10-1` |

Rules that ran with **no** finding: r2, r7, shonen. Declared not-evaluated by the gate
(not by me): r1, r3, r5, r6, r9, box-3 verifier independence, shonen truth. The gate does
**not** turn this into a whole-corpus semantic verdict; neither do I.

## 4. r4 detail (52) — what actually fired

Implementation read from the gate (`corpus-gate.mjs:449-466`): a line is exempt if it
contains **any** backtick (`if (l.includes('`')) continue;`), so the finding class is
"count-noun phrase on a line with zero inline code". Verified mechanically: **0 of the 52
flagged lines contains a backtick**.

Distribution: README.md 1, `knowledge/` 31, `lessons/` 20.

Per-file line numbers (from the gate's own finding text):

- `README.md`: 11
- `knowledge/fleet-registry.md`: 8
- `knowledge/free-read-verbs.md`: 7, 90, 126, 414, 433, 457
- `knowledge/freshness-sweep.md`: 32, 104, 133
- `knowledge/ghp-served-set.md`: 2
- `knowledge/ghp-subpath-spotcheck.md`: 37, 85
- `knowledge/keeper-timer-inert.md`: 158
- `knowledge/kimi-subpath-audit.md`: 34, 35, 41
- `knowledge/ops-automation.md`: 23, 31, 90, 118, 119
- `knowledge/probe-delta-alerting.md`: 40, 42, 45, 106, 107
- `knowledge/publish-queue.md`: 74, 162
- `knowledge/sitemap-orphan-audit.md`: 12
- `knowledge/vault-properties.md`: 73
- `lessons/round-1-aggregator-audit.md`: 63; `round-10.md`: 31; `round-12.md`: 43;
  `round-16.md`: 9; `round-19-recensus.md`: 58; `round-20.md`: 150, 194, 201, 230, 237;
  `round-4-aggregator-audit.md`: 10, 16, 34; `round-5-aggregator-audit.md`: 66;
  `round-6-aggregator-audit.md`: 32, 54, 120; `round-6.md`: 4, 18, 44.

Class A — mechanically not a count claim (matched token is an identifier/date/version
attributive or a column header). Exact revision-bound lines:

| location | line | regex match |
|---|---|---|
| `corpus/README.md:11` | `round-20 citation-locality lesson; independent spot-check still owed.` | `20 citation` |
| `knowledge/free-read-verbs.md:7` | `(all read 2026-09-28, line pins re-verified post-draft), plus a live read of` | `28, line` |
| `knowledge/free-read-verbs.md:414` | `log. 18-of-21 probe coverage is **by-design url filtering, not a coverage` | `21 probe` |
| `knowledge/ghp-served-set.md:2` | `verified-at: 2026-10-19 (v4.0.0 commit 7b1f4a7; current action commit 5f327015)` | `.0 commit` |
| `knowledge/publish-queue.md:74` | `- **PQ-12 pin persist — and the loop caught its first transition (r14` | `12 pin` |
| `knowledge/publish-queue.md:162` | `(the 09-26 pin survived <24h before the 09-27T06:22Z ENTER; beats land` | `26 pin` |
| `lessons/round-4-aggregator-audit.md:16` | `because the round-4 commit shipped it.` | `4 commit` |
| `lessons/round-5-aggregator-audit.md:66` | `16:16:15, one minute *after* this lane's 16:15:02 commit — heading exempt,` | `02 commit` |
| `lessons/round-20.md:201` | `\| id \| URL (accessed 2026-10-19) \| quote (≤25 words) \| location \|` | `25 words` |

Class B — genuine count/ratio claims, evidence not on the same line (sample, verbatim):
`free-read-verbs.md:90` (`history **76 → 77 lines**`; the command `probe ds4cc-com --json`
sits on line 87), `ops-automation.md:23` (`**78 rows** … r16 re-read`),
`kimi-subpath-audit.md:34` (`63 files 09-23 …`), `round-6.md:18`
(`**0 true rot** across 2 352 paths`; file-level `Cites:` + evidence pointer at line 4),
`round-19-recensus.md:58` (`The other 322 hits …`; sweep path named just above),
`round-20.md:150` (`one batched call of 10 seats …`), `round-20.md:230` (`the 26 notes`),
`round-20.md:237` (`all 18 rows are new this round`).

Class C — lines that *quote* a superseded value while correcting it:
`knowledge/fleet-registry.md:8` (`Audit correction: round-1 said "20 rows" — the registry
has 21`), `round-16.md:9` (`r10 measured "60/60 paths resolve" and froze it`),
`freshness-sweep.md:32` (`r10's "60/60 paths`).

Class D — table rows carrying counts: `sitemap-orphan-audit.md:12` and
`round-6-aggregator-audit.md:54` (`2 352 paths, 0 rot`).

Proximity measure (mine, mechanical): 33 of the 52 flagged lines have a backticked token on
the adjacent non-blank line; 19 have none adjacent. This is proximity, not semantics.
Conclusion for the parent: the r4 failures are **real under the rule as implemented**
(line-scoped, any-backtick exemption) but they are bookkeeping failures; at least 9 of the
52 are not count claims at all, and 3 more quote a superseded number as part of a
correction. They do not establish that any number is wrong.

## 5. r8 detail (1 finding, 3 occurrences)

Gate row, verbatim:

```
CR-kake-shokunin-r8-1: credential-class op-ref occurrences=3 lines=3 files=3 owner=aggregator at 7e17c66 maxseg=1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-6-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:54 first4="op:/" len=5 (CORPUS.md:43)
```

Exact revision-bound lines (one `op://` literal each; `grep -rIl 'op://' corpus/` returns
exactly these three files, total 3):

- `corpus/lessons/round-5-aggregator-audit.md:54` —
  ``clean (`grep -rn 'op://' corpus/` → 0; `speedrun-pipeline.md` denylist``
- `corpus/lessons/round-6-aggregator-audit.md:56` —
  ``| credential sweep (R8) | `grep -rnE 'op://\|sk-[A-Za-z0-9]{16,}\|BEGIN [A-Z ]*PRIVATE KEY\|ghp_[A-Za-z0-9]{20,}\|eyJ[A-Za-z0-9_-]{20,}' corpus/` | …``
- `corpus/lessons/round-9-aggregator-corpus-verdict.md:8` —
  `… landed corpus has exactly two `op://` occurrences (…), both schematic sweep-pattern examples …`

Observations:
1. All three are aggregator-owned by the gate's own ownership rule (`round-<N>-aggregator-*`).
   No lane-authored knowledge/lesson file carries the literal.
2. The gate declares schematic-vs-real **could-not-evaluate**; the literal-text rule still
   fails per CORPUS.md:43 ("including this one's examples"). I did not attempt a vault read.
3. Self-reference: round-9's verdict says "exactly two" occurrences; at HEAD the count is
   three because that verdict line itself contains the literal. The count field is a live
   measurement, not a stale one.
4. I quote the gate's `maxseg=1` field verbatim; the raw literals show no
   `/`-separated `vault/item/field` tail, but I did not re-derive the shape measure.

## 6. r10 detail (1)

Gate matcher (`corpus-gate.mjs:445`): `^lessons/round-<R>-aggregator-.+\.md$`; at R=20
nothing matches.

Observed at HEAD: `corpus/lessons/round-20-verifier-spotcheck.md` exists and is titled
`# round-20 — non-author verification and spot-check (orchestrator, kaika)`, self-describing
as `Written by the integrator, not the lane`. Its name does not carry the `aggregator` token.
Whether that file satisfies CORPUS.md:21's round-review duty is a semantic/filename-policy
question the gate explicitly does not decide; I report the presence and the name mismatch,
and leave the ruling to the parent/integrator. The lane's own `corpus/lessons/round-20.md`
also does not match.

## 7. SOURCES.md structural observations (separate from gate rules)

File: `corpus/SOURCES.md`, 66 lines at HEAD. Parsed mechanically; no edits.

- Registry: 18 rows, ids `S001`–`S018` contiguous, 11 columns on every row, no empty
  `opened` cell. Status = 14 `mined`, 2 `queued` (S015, S016), 2 `rejected` (S017, S018).
  Tier column values are only `A` (16 rows) and `C` (S017, S018) — **no row carries tier B**.
- Paths section: 4 named sequences. Id references are S001–S014 plus S017; every referenced
  id resolves to a registry row (0 dangling). Unreferenced ids are S015, S016 (queued) and
  S018 (rejected) — consistent with their status, not a defect.
- Search log: three tallies `8/8/8/0`, `5/5/5/0`, `5/5/5/0` = 18 identified / 18 screened /
  18 included / 0 excluded, matching the 18 registry rows. The log's own definition limits
  "included" to "retained as a registry row".
- `used-by`: 8 distinct `corpus/...` paths; all resolve at HEAD (0 missing).
- Anchor spot-check (one row, bounded): S014 claims `scripts/freshness-sweep.mjs:404-411`
  and `:1021-1044`. `grep` at 404-411 found
  `// Annotation window = the citing line ±2 (spec), with every *citation*` /
  `// on the citing line blanked` at 405-406; at 1018-1046 found
  `const sections = opt.section ? [opt.section] : SECTIONS;` (1040) and
  `runSections({ … })` (1042). Both halves of S014's anchor resolve. The other 17 rows'
  anchors were **not** re-verified (bounded scope; several require network).
- Cross-reference gap (not a gate rule; no tier check exists): `QUALITY.md:22` says
  "Source tiers (A/B/C, scoped per claim) are defined in `corpus/SOURCES.md`", but
  SOURCES.md has no tier-definition block — its headings are Registry / Paths / Search log /
  Leads, and its only tier prose is line 3, "Tiers are scoped to the row's stated topic, not
  global judgments." No definition of A, B or C appears in the file, and no row uses B.
  Routing this is the parent's call.
- Leads: 17 unopened lead lines, explicitly headed `## Leads (unopened)`. **None was used as
  evidence in this note.**

## 8. Study path extracted (directly evidenced, one sequence)

Verbatim from `corpus/SOURCES.md` §Paths (line 30 at HEAD):

> GHP served-set semantics — S003 → S004 → S001 → S008 → S002 → S006: establish branch
> versus Actions publishing, learn the artifact contract, inspect the pinned archive action,
> apply GNU tar's matching defaults, then account for the v4/v5 dotfile change and contrast
> the legacy Jekyll path.

Evidence that the sequence is real rather than a lead:
- All six ids resolve to registry rows (programmatic check, 0 dangling).
- All six rows are tier `A` and status `mined`, each with a pinned anchor: S001 tag
  `7b1f4a7…` / main `5f327015…`, S002 tags `7b1f4a7…` and `fc324d3…`, S008 GNU tar master
  `cfdb891…`, S003/S004/S006 dated `fetched 2026-10-19`.
- The sequence terminates in `corpus/knowledge/ghp-served-set.md`, which exists at HEAD,
  whose provenance line reads `source: S001, S002, S003, S004, S006, S008 (corpus/SOURCES.md)`
  — exactly the six ids — and which is indexed by the README coverage-map row
  "GHP served-set semantics (r20) | `knowledge/ghp-served-set.md`".
- Limit: I did **not** re-fetch the remote URLs or re-open the remote files (no network
  re-verification; the lane's own QUALITY.md bars presenting an old HTTP result as current).
  The sequence is evidenced as a committed registry path, not as freshly re-verified truth.

## 9. Provenance frontmatter scan (parent addendum, bounded)

Scanned all 21 `corpus/knowledge/*.md` at HEAD for lowercase `source:` / `verified-at:` /
`recheck:` (whole file, not just head).

- Exactly **4 of 21** carry the triple, each exactly once — the round-20 entries:
  `crawl-scope-per-host.md`, `ghp-custom-domain.md`, `ghp-etag-anatomy.md`,
  `ghp-served-set.md`. The other 17 use older prose-style provenance (e.g.
  `fleet-registry.md:6` `Source: \`~/Projects/webzites/fleet/fleet.config.json\``).
- Ephemeral-path check: **0 of 21** files has a `recheck:` value pointing into
  `.tower/worktrees`, `/tmp` or `/var/tmp`; a full-text scan of the four r20 entries found
  no `.tower/worktrees`, `/tmp` or `/home/...` path at all. The parent's flagged failure mode
  does not materialize in this lane.
- Exact `recheck:` values of the four entries:
  - `crawl-scope-per-host.md`: `on RFC or project-site inventory change — curl -fsSL https://www.rfc-editor.org/rfc/rfc9309.txt | grep -cF 'top-level path of the service'`
  - `ghp-custom-domain.md`: `on Pages behavior or docs change — curl -fsSL 'https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.md' | grep -cF 'any existing \`CNAME\` file is ignored'`
  - `ghp-etag-anatomy.md`: `on recorded ETag or source revision change — printf '%d\n' 0x1365d; date -u -d @$((0x6ab49127)) +%FT%TZ`
  - `ghp-served-set.md`: `on action release or workflow change — for v in v3.0.1 v4.0.0 main; do printf '%s ' "$v"; curl -fsSL "https://raw.githubusercontent.com/actions/upload-pages-artifact/$v/action.yml" | grep -cF -- '.[^/]*'; done`
- Informational adjacency (NOT a rule, NOT a verdict): 94 `/tmp/...` occurrences across 19
  corpus files (largest: `knowledge/free-read-verbs.md` 46, `handoffs/cmdProbe-merge-fix.md`
  10, `lessons/round-6-aggregator-audit.md` 10). These are historical evidence pointers in
  body prose, not `recheck:` values; none points into `.tower/worktrees` (0 occurrences
  corpus-wide). One absolute home path sits in a pin: `freshness-pins.json:38`
  `"plazirSourceDir": "/home/vgpnk/Projects/plazir-15-site"` — durable-looking, not
  ephemeral; its existence was not checked (outside this seat's scope).

## 10. Gate limitations (named, not glossed)

1. **Not evaluated**: r1, r3, r5, r6, r9; box-3 verifier independence; shonen claim truth.
   Reasons are the gate's own (`corpus-gate.mjs:80-118`): semantic judgement, unavailable
   province tree, proximity ambiguity, external quoted surfaces, no history in snapshot mode.
2. **r4 is line-scoped and backtick-any**: any inline code span exempts a line, and the
   count-noun regex fires on version/date/round-number attributives (9 demonstrated cases in
   §4 Class A). 52 findings ≠ 52 wrong numbers.
3. **r8** reports literal occurrences; schematic-vs-real is declared could-not-evaluate
   (needs an operator-gated vault read). The literal findings still fail the rule.
4. **r10** is a filename-pattern presence check only — not whether the round review was done
   or whether a differently named file discharges it (see §6).
5. **Snapshot mode** grades a `git archive` tree with no history, so the gate's own r9
   authorship sub-check would be unavailable in exactly this mode.
6. **r7** grades phantom rows only. Under-coverage is a note (22/48 corpus files unindexed);
   the gate reports 2 skipped template paths. README contains 7 backticked tokens carrying
   skip-class characters (`probe <id> --all`, `round-{1,3,4,5,6,7,8,9,10,12,16,17,18}.md`,
   `--zip-exclude='assets/*.mp4'`, `~/Projects/webzites/reports/r9-stale-markers.md`,
   `node ~/Projects/webzites/bin/webzites.mjs`, `~/Projects/webzites/bin/webzites.mjs`,
   `~/Projects`), so the skip counter is per index-row path candidate, not per token.
7. **This seat ran `--snapshot` only** (no live mode, no `--all` fleet mode, no selftest).
   Only this lane was graded.

## 11. What I did not do

- Did not re-run or verify any build/test/lint (out of contract).
- Did not open the lane's scripts beyond the bounded S014 anchor check, and did not audit
  knowledge-claim truth, freshness-sweep results, or the round-20 proofs.
- Did not use unopened Leads as evidence.
- Did not edit, stage or commit anything in `kake-shokunin`; the only write is this note.
- Did not adjudicate this verdict; the parent is sole coordinator/integrator/adjudicator.
