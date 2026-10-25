# audit-revenger — revenger-shokunin corpus conformance audit (aggregator round 12)

- Seat: `KaikaAggregateR12.AuditRevenger`. Read-only audit; this note is the only write.
- Lane under audit: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (original checkout, not a worktree copy).
- Revision under audit: `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` (HEAD at audit time; subject `round-1 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication`).
- Gate: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs` (`corpus-gate-v1`).
- Session stamp: `2026-10-19T23:47:22Z` (`date -u '+%Y-%m-%dT%H:%M:%SZ'`).
- **Verdict: `not conformant` at `cf02419`, per gate exit `1`; failed rule ids `r4` (2 findings) and `r10` (1 finding).**
- Census caveat: every count below is revision-bound and **provisional**. The parent has a census-parser fix in flight for indented Markdown source rows; no final census total is frozen or published here.

## 1. Identity and worktree state

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse HEAD
cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97
$ echo $?
0
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain
$ echo $?
0
```

`status --porcelain` produced no output: the worktree is clean. The gate's own tree line confirms the graded bytes are an archive of the commit, not the worktree:

`# tree revenger-shokunin revision=cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 dirty=0 mode=snapshot`

## 2. Canonical gate run and verdict

Command (cwd `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`):

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/revenger-shokunin cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97
```

Observed output, verbatim:

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect revenger-shokunin@cf02419 ABSENT (no committed expected verdict for this revision)
# tree revenger-shokunin revision=cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 dirty=0 mode=snapshot
CR-revenger-shokunin-r4-1: knowledge/tool-validation-by-function-and-version.md:88 count claim with no backticked command: "standard; §3 notes it does not address processing speed, eas" (CORPUS.md:28)
CR-revenger-shokunin-r4-2: lessons/round-1.md:68 count claim with no backticked command: "Access date 2026-10-19 for every row. Quotes ≤25 words, verb" (CORPUS.md:28)
CR-revenger-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
# note revenger-shokunin r7: 2 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note revenger-shokunin r7 under-coverage (not a finding): 447/465 corpus files carry no index row
# note revenger-shokunin extracted with: git archive cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 | tar -x -C <tmp>
# verdict revenger-shokunin failed findings=3 rules=r4,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Observed exit status: `1` (`failed` in the gate's verdict map: 0 clean, 1 failed, 2 could-not-evaluate, 3 frozen-expectation drift).

Exit-3 is not in play: the `# expect revenger-shokunin@cf02419 ABSENT` line means the frozen expectation file (`.ufo/waves/round-9/corpus-gate.expected.json`, `frozen_round: 9`) contains no entry for this repo@revision, so this is a fresh measurement, not a drift reproduction. Enumeration: `node -e "… Object.keys(j.frozen) …"` → 8 keys (`kasegi-shokunin@b7180b0`, `kengaku-shokunin@f09ff1f`, `kake-shokunin@a209441`, `kake-shokunin@4c9a985`, `kumitate-shokunin@7a099b2`, `kotoba-shokunin@63ceba7`, `kagi-shokunin@4b8c018`, `kagi-shokunin@4391b3b`), all legacy lanes; `revenger_entry 0`.

### Round-selector derivation

The lane's committed LOG states its steered fleet round (tail section `Fleet round-1 kaika continuation — claims, landing, measurement (2026-10-19)`):

> Round identity: orchestrator steer table (fleet `.ufo/waves/kaika/steer.md`, row `revenger | 1`) steers this lane to fleet round 1.

The referenced fleet row exists at `.ufo/waves/kaika/steer.md:30`:

```
| revenger | 1 | fleet round-1 continuation blocked (`MISSING_BINDING`) | lane handoff at the lane's `.ufo/reports/round-1/revenger.md` |
```

The gate's `--round` selector is the **aggregator** round whose review duty r10 checks, not the lane's own round. The canonical run therefore uses the gate default `9` (equal to `frozen_round: 9`). Selector sensitivity, same snapshot:

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot … cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 --round 1
  … CR-…-r4-1 / CR-…-r4-2 identical; CR-…-r10-1 names round-1; process-exit 1 (failed)  → GATE_EXIT=1
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot … cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 --round 12
  … CR-…-r4-1 / CR-…-r4-2 identical; CR-…-r10-1 names round-12; process-exit 1 (failed) → GATE_EXIT=1
```

The verdict is selector-insensitive: exit `1` at selectors 1, 9, and 12.

## 3. Findings, item by item

| finding id | rule | location | observation | adjudication |
|---|---|---|---|---|
| `CR-revenger-shokunin-r4-1` | r4 | `corpus/knowledge/tool-validation-by-function-and-version.md:88` | matched token `3 notes`; line has 0 backticks | literal-detector artifact (section reference, not a count claim) |
| `CR-revenger-shokunin-r4-2` | r4 | `corpus/lessons/round-1.md:68` | matched token `25 words`; line has 0 backticks | literal-detector artifact (quote-length cap, not a count claim) |
| `CR-revenger-shokunin-r10-1` | r10 | `corpus/lessons/` | no `round-<selector>-aggregator-*.md` at selectors 1, 9, 12 | true absence in the child repo and in the aggregator's wave lesson dirs |

### r4-1 — exact line and match

`git show cf02419:corpus/knowledge/tool-validation-by-function-and-version.md` lines 86–90:

```
86|
87|- SWGDE guidance is consensus best practice for forensic labs, not a binding
88|  standard; §3 notes it does not address processing speed, ease of use, or
89|  personnel training. The lane adopts it as a claim shape, not as authority.
90|- The r7 evidence is one fixture pair (js-r3 / js-r7-v2) and one comparison
```

Detector reproduction with the gate's own regex (`corpus-gate.mjs:267`), run from the lane root against the committed bytes:

```
$ node -e '… COUNT_NOUN_RE …; line = file.split("\n")[87] …'
k:88 match= "3 notes" backticks= 0
```

The matched substring is `3 notes` inside `§3 notes it does not address…`: a section reference parsed as `<number> <count-noun>` (`notes?` is in the noun list). Rule 4's intent — "a count carries its command" — is not engaged; there is no corpus count on the line. The finding is a literal-detector artifact, but it is a real failed finding under the gate as implemented.

### r4-2 — exact line and match

`git show cf02419:corpus/lessons/round-1.md` lines 66–70:

```
66|### Sources opened this round (contract rule 1)
67|
68|Access date 2026-10-19 for every row. Quotes ≤25 words, verbatim.
69|
70|- S001 `.ufo/waves/kaika-r1/scout-freshness.md` — own-work; table row 7: "server key `rea`, package `rea-agents@6.5.0`".
```

Same reproduction: `l:68 match= "25 words" backticks= 0`. The matched substring is the quote-length cap `≤25 words`; it is a contract limit, not a corpus count. Same artifact class as r4-1. The count on line 68 (`2026-10-19`) is a date, not a count claim.

### r10-1 — absence check

`git ls-tree --name-only cf02419:corpus/lessons/`:

```
.gitkeep
2026-10-12-r1-provider-gap.md
round-1-verifier-spotcheck.md
round-1.md
```

No `round-<N>-aggregator-*.md`. I also checked the aggregator's own placement, because round 10 emitted its per-repo verdicts into the wave tree instead of the child repo:

```
$ ls .ufo/waves/round-9/lessons/ .ufo/waves/round-10/lessons/
round-9/lessons:  round-9-aggregator-corpus-verdict-{kagi,kake,kasegi,kengaku,kotoba,kumitate}.md
round-10/lessons: {kagi,kake,kasegi,kengaku,kotoba,kumitate}-shokunin-round-10-aggregator-corpus-verdict.md
$ grep -rl "revenger" .ufo/waves/*/lessons/
.ufo/waves/round-10/lessons/kagi-shokunin-round-10-aggregator-corpus-verdict.md
.ufo/waves/round-10/lessons/kotoba-shokunin-round-10-aggregator-corpus-verdict.md
```

The two grep hits reference the round-10 seat named `revenger-rule4-intent.md`, not `revenger-shokunin`. No per-repo aggregator verdict for this lane exists under either placement (inside the graded repo or in the aggregator wave tree): the r10 finding is a true absence, not a location artifact.

## 4. SOURCES.md structural observations (revision-bound; provisional totals)

Reproduction (exact command run from the lane root; reads the committed blob, not the worktree):

```
$ python3 -c "
import subprocess,re
H='cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97'
t=subprocess.run(['git','-C','.','show',H+':corpus/SOURCES.md'],capture_output=True,text=True).stdout
rows=[l for l in t.split('\n') if re.match(r'^\|\s*S\d{3}\s*\|',l)]
ids=re.findall(r'^\|\s*(S\d{3})\s*\|',t,re.M)
c=lambda l,i:[x.strip() for x in l.strip().strip('|').split('|')][i]
print('rows',len(rows),'unique',len(set(ids)),'sequential',ids==['S%03d'%i for i in range(1,len(ids)+1)])
print('status',{s:sum(c(l,7)==s for l in rows) for s in {c(l,7) for l in rows}})
print('tier',{s:sum(c(l,3)==s for l in rows) for s in {c(l,3) for l in rows}})
print('recheck-empty',sum(c(l,9) in ('','—','-') for l in rows),'opened-malformed',sum(not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',c(l,8)) for l in rows))
ub=sorted({p for l in rows for p in re.findall(r'corpus/[A-Za-z0-9_./-]+',c(l,10))})
print('used-by',len(ub),'missing',[p for p in ub if subprocess.run(['git','-C','.','cat-file','-e',H+':'+p],capture_output=True).returncode!=0])
paths=t.split('## Paths')[1].split('## Search log')[0]
for l in [x for x in paths.split('\n') if x.startswith('- ')]:
    seq=re.findall(r'S\d{3}',l); print('path',seq,'valid',all(s in ids for s in seq))
"
```

Observed output:

```
rows 15 unique 15 sequential True
status {'queued': 1, 'rejected': 2, 'mined': 12}
tier {'C': 1, 'A': 14}
recheck-empty 0 opened-malformed 0
used-by 6 missing []
path ['S003', 'S004', 'S007', 'S014'] valid True
path ['S006', 'S005', 'S014'] valid True
path ['S009', 'S010', 'S011', 'S013'] valid True
path ['S002', 'S001'] valid True
```

Structural observations:

- 15 registry rows, ids `S001`–`S015`, unique and sequential, 11 columns each (min = max = 11).
- Status distribution: `mined` 12, `queued` 1, `rejected` 2. Tier distribution: `A` 14, `C` 1.
- Every row carries a non-empty `recheck:` and a well-formed `opened` date. The round-2 post-review fix is visible in the bytes: S008 `recheck` `on-release`, S012 `180d`, no `—`.
- All 6 distinct `used-by` corpus paths exist at the graded revision (`git cat-file -e` exits 0 for every one; `missing []`).
- All four `## Paths` sequences reference ids present in the registry.
- Headings present: `## Registry`, `## Paths`, `## Search log`, `## Leads (unopened)`. The Leads section is explicitly unopened material and was not used as evidence below.
- **Provisional**: the 15-row total and the gate's `447/465` under-coverage count are counts of committed text at this revision; they are subject to the parent's in-flight census-parser fix for indented Markdown source rows and are not frozen.

## 5. One directly evidenced study path

Extracted from `corpus/SOURCES.md` `## Paths` at `cf02419`:

**`decoding a resource name field` — `S009 → S010 → S011 → S013`**

Rows from the committed registry (all `mined`, tier `A`):

| id | source + anchor | teaches (registry text) |
|---|---|---|
| S009 | Microsoft PE Format — `The .rsrc Section` and its four subsections; page ms.date 2026-09-10, git_commit_id 55e845e9f3a6a3261f59a2f460f61edc25ffcdd5 | Exact offsets, sizes, high-bit flag semantics and the Type/Name/Language tree rule needed to decode a resource tree. |
| S010 | Unicode 18.0.0 ch. 3 — §3.8 Surrogates, §3.9 Unicode Encoding Forms, §3.9.2 UTF-16 (D71–D91, Table 3-5, C10); release dated 2026-09-16, version page still carries a preliminary-draft banner | The definitions that make a lone surrogate code unit ill-formed, so observed name bytes can be classified from the spec. |
| S011 | Python `codecs` docs — `Error Handlers` table, `surrogatepass` row; 3.15.0 documentation | Which documented decode mode rejects and which preserves a lone surrogate, to reproduce parser-like behavior. |
| S013 | Saved r59 REA record — `corpus/live/runs/round-59/inspection.stdout.json`; Evidence `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`; file SHA-256 `bf7922db…`; `LEDGER.md:3` | One parser run's observed acceptance of an unpaired-surrogate resource name, kept as the falsifier of the r59 refusal prediction. |

Terminal-row check — the path ends in a byte-identified saved record, not a lead:

```
$ git cat-file -e cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97:corpus/live/runs/round-59/inspection.stdout.json ; echo $?
0
$ git show cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97:corpus/live/runs/round-59/inspection.stdout.json | sha256sum
bf7922dbda2bc2dd817eaa13652f04e19c10ed8701feab5790a8703d55f22c0f  -
$ git show …:corpus/live/runs/round-59/inspection.stdout.json | wc -c
4853
```

The reproduced digest equals the registry's claimed `bf7922db…`. S013's `used-by` names `corpus/knowledge/pe-resource-directory-layout.md` and `corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md`; both exist at HEAD (covered by the `used-by missing []` check).

Reading sequence as the registry states it: where the name field lives (S009) → whether its bytes are well-formed (S010) → which documented decode mode preserves or rejects them (S011) → the saved parser run that accepted an ill-formed name (S013).

Not used as evidence: the four `## Leads (unopened)` entries (ISO/IEC 27042 HTTP 403; individual NIST CFTT reports; SWGDE 18-F-002; the REA firmware guide).

## 6. Knowledge frontmatter provenance scan (parent direction)

Command (from the lane root, committed blobs):

```
$ for f in $(git ls-tree --name-only cf02419:corpus/knowledge/); do echo "===== $f ====="; git show cf02419:corpus/knowledge/$f | grep -nE '^(source|verified-at|recheck):'; done
```

Observed: all six knowledge entries (`2026-10-12-rea-readiness-checklist.md`, `digest-scope-versus-provenance.md`, `pe-resource-directory-layout.md`, `seed.md`, `tool-validation-by-function-and-version.md`, `utf16-unpaired-surrogates-in-resource-names.md`) carry at least one `source:`, one `verified-at:`, and one `recheck:` line. The two pre-contract entries (`seed.md`, readiness checklist) each carry `source:` S001/S002, `verified-at: 2026-10-19`, and a `recheck:` command line.

Bounded sweep for the requested class:

```
$ git grep -nE '\.tower/worktrees|/tmp/' cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97 -- corpus
cf02419:corpus/live/runs/round-10/extraction.json:1: … "output_root":"/tmp/rea-extracted-249be596-…" …
cf02419:corpus/live/runs/round-11/outer-extraction.json:1: … "output_root":"/tmp/rea-extracted-2ebcfedb-…" …
cf02419:corpus/live/runs/round-32/reviewer.md:15: … save as `/tmp/check-pe-r32-review.py` …
cf02419:corpus/live/runs/round-5-review.md:3: … read `/tmp/mission-revenger-standing.md` …
cf02419:corpus/live/runs/round-57/result-review.md:4: … read `/tmp/mission-revenger-standing.md` …
cf02419:corpus/live/runs/round-58/reviewer.md:5: … read `/tmp/mission-revenger-standing.md` …
```

- **No `recheck:` value points into `.tower/worktrees` or `/tmp`.** Every sweep hit is inside `corpus/live/runs/**` — saved reviewer transcripts and saved provider output — not frontmatter. **Requested-class finding: none** (bounded negative; sweep above).
- Those hits are historical evidence kept byte-preserved and are explicitly outside the requested class; recorded only so a reader does not mistake them for live provenance.
- Adjacent observation (not the requested class, not a gate rule): the same saved `live/runs` JSON also carries an old host path `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/...` and `/tmp/rea-extracted-<uuid>` output roots. Historical bytes; unchanged.
- Two `recheck:` values are pointer-style rather than a single command: `pe-resource-directory-layout.md` → `python3 -B -` on the entry's `## Reproduce` block; `2026-10-12-rea-readiness-checklist.md` → "the `probe` column below, plus `node --version; npm --version; binwalk --version; unblob --version; jadx --version`". Both resolve inside the committed repo; neither is ephemeral.

## 7. Index / anchor observations (not gate findings)

- `corpus/README.md:9` describes QUALITY.md as "admission criteria Q01–Q10"; the committed QUALITY.md contains 11 criterion rows (Q01–Q11, with Q11 superseding Q08). Command: `git show cf02419:corpus/QUALITY.md | grep -cE '^\| Q[0-9]+ '` → `11` (exit 0). Description drift only; r7 grades paths, r4 skips the line because it contains backticks.
- `corpus/README.md:12` lists `2026-10-12-r1-provider-gap.md` and `round-1.md`; `corpus/lessons/round-1-verifier-spotcheck.md` also exists at HEAD (`git ls-tree --name-only cf02419:corpus/lessons/`). The gate declares under-coverage a `# note`, not a finding.
- README's own count carries its command and reproduces: `Rows 14 — \`grep -cE '^\| C[0-9]+ ' corpus/README.md\``; re-run at HEAD → `14` (exit 0).
- S014 anchor fidelity: the registry says round 8 result `:105-109` at `8bbcb4e`. Actual boundaries at that commit: round-8 declaration heading `:102`, result heading `:107`, result block `:107-110`. Command and excerpt:

```
$ git show 8bbcb4e:LOG.md | awk 'NR>=100 && NR<=112 {printf "%d|%.110s\n", NR, $0}'
105|- Owned axes: calibration target, depth and coverage guardrails. Reviewer wave spec: `graph-delta-review`, rev
107|## Round 8 result — bounded analyst-side parent-graph delta (2026-10-12)
110|- Per-axis verdicts: calibration **improved** for reproducible analyst-side saved-parent comparison; depth **u
```

The cited span `:105-109` starts on the last declaration line and omits the final verdict line (`:110`). r6 is declared not-evaluated by the gate; this is an anchor observation, not a rule finding.

## 8. Gate limitations (named) and what a pass would not mean

- Implemented checks: r2, r4, r7, r8, r10, SHONEN form. Declared not evaluated (gate header and `REGISTRY.not_evaluated`): r1, r3, r5, r6, r9, verifier independence, the box-3 non-author test, and SHONEN box truth.
- r4 is a literal regex (`corpus-gate.mjs:267`), reproduced above; it fires on `3 notes` (a section reference) and `25 words` (a quote-length cap). A r4 pass would not mean every count carries its command.
- r7 skips template/glob spans. The skip predicate (indexed extension plus `[*<>{}~$…]` or `...`) selects exactly two README spans: `["verify_*.py","verify_*icon*.py"]` (`git show cf02419:corpus/README.md | node -e '…'` → that JSON; README contains no `timestamp` template, `grep -c` → 0). The gate's counter reports 2 skipped, which predicate-set equality accounts for; attributing each count to its span is `[INFERENCE]` from that equality, not from an instrumented counter. Under-coverage (`447/465`, provisional) is a note by construction.
- r2 selects lessons by the regex `round-(\d+)` in the filename; `corpus/lessons/2026-10-12-r1-provider-gap.md` carries no `round-<N>` token and is silently not graded.
- r10 is filename-only (`^lessons/round-<R>-aggregator-.+\.md$`) and location-bound to `corpus/lessons/` inside the graded child repo. It cannot see the aggregator's wave-level lesson dirs, and snapshot mode grades a `git archive` tree with no history, so history-dependent checks (r9 authorship) are unavailable by design.
- r8 scans every text file for credential-shaped bytes, reports occurrences, and declares schematic-vs-real classification `could-not-evaluate`. It reported no findings for this lane.
- SHONEN finding count: `node … --snapshot … | grep -c 'CR-.*-shonen-'` → `0` (grep exit `1` = no matching lines). Form only; the check does not establish that any box claim is true.
- The gate's SHONEN evidence line carries no mark/verifier findings at this revision; that is a form result, not a verifier-independence result.
- The frozen registry (`frozen_round: 9`) covers six legacy lanes. `revenger-shokunin@cf02419` has no committed expectation, so this run is a fresh measurement and cannot be a drift reproduction (exit 3 not applicable).
- A gate pass, and the clean SOURCES structure above, would not establish whole-corpus semantic conformance. The verdict here is not conformant, so that caveat is moot for the exit code but still bounds what the other checks prove.

## 9. Scope, non-applicable role checks, residuals

- Read-only: no child-repo edit, stage, or commit; no README/LOG/SCORECARD/report/MANIFEST/gate/script changed. Only this note was written. No builds, tests, lint, or formatting run.
- `lsp` device is not mounted in this seat (`read xd://lsp` → `No such tool: xd://lsp`; the mounted-device list contains no lsp). Semantic caller/definition/diagnostics checks were therefore unavailable; the text and structural checks above are not presented as semantic proof.
- No canonical runtime, same-identity rerouting, saturation claim, or resume path (`resume_continuity_v1`) exists in this seat's scope — a read-only corpus audit invokes no runtime, routes no agent, and mutates no preflight — so those reviewer-role checks are **not applicable** rather than passed.
- Residual risk: (a) census totals are provisional pending the parent's parser fix; (b) the r4 findings are adjudicated at intent level only — gate bytes were not changed, so the exit-1 verdict stands; (c) every observation is bound to `cf02419` (and `8bbcb4e` where the LOG anchor is cited); (d) the S014 anchor observation and the README description drift are reported as observations, not as gate rules or semantic verdicts.
