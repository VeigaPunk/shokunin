# audit-tameshi — aggregator round 12, lane `tameshi-shokunin` (seat `KaikaAggregateR12.AuditTameshi`)

Read-only audit. No child repo file was edited, staged, or committed. Only write: this note.
All paths absolute; lane read from its original location `/home/vgpnk/Projects/shokunin/tameshi-shokunin`
(not from a `.tower` worktree).

## 1. Verdict at named HEAD

**Verdict: `not conformant` at `a21e9104723e7a46b794b03b8fdcdd1455696f7e`** — gate exit `1` (failed),
`findings=83`, failed rules `r4`, `r8`, `r10`.

> `# verdict tameshi-shokunin failed findings=83 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen`
> `# process-exit 1 (failed)`

This is a **gate-rule-literal** verdict only: the gate evaluates r2/r4/r7/r8-literal/r10/SHONEN form; r1/r3/r5/r6/r9,
verifier independence, and SHONEN claim truth are **declared not-evaluated** (gate header, rules-not-evaluated block).
A gate failure is not a whole-corpus semantic judgement, and a clean SOURCES structure below is not conformance.

### Exact commands and outputs

```sh
git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin rev-parse HEAD
# a21e9104723e7a46b794b03b8fdcdd1455696f7e          exit 0

git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin status --porcelain
# (empty)                                            exit 0   -> dirty=0

cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
     /home/vgpnk/Projects/shokunin/tameshi-shokunin a21e9104723e7a46b794b03b8fdcdd1455696f7e
# # corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# # expect tameshi-shokunin@a21e910 ABSENT (no committed expected verdict for this revision)
# # tree tameshi-shokunin revision=a21e9104723e7a46b794b03b8fdcdd1455696f7e dirty=0 mode=snapshot
#   ... 83 CR- findings ...  (81 r4, 1 r8, 1 r10)
# # verdict tameshi-shokunin failed findings=83 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# # process-exit 1 (failed)                          exit 1
# note line: extracted with: git archive a21e9104723e7a46b794b03b8fdcdd1455696f7e | tar -x -C <tmp>
```

Round selector: the gate default is `--round 9`. The lane's own committed round is **fleet round 1** —
`LOG.md` tail sections `## 2026-10-19 — fleet round 1, phase-2 corrections (same round)` and
`## 2026-10-19 — fleet round 1, post-review fixes (orchestrator adjudication)`; `corpus/lessons/round-1.md:1`
(`# Fleet round-1 lesson — tameshi-shokunin (2026-10-15)`); `corpus/README.md` (`Fleet round-1 status`).
So both selectors were run:

```sh
node .ufo/waves/round-9/corpus-gate.mjs --snapshot <dir> a21e9104... --round 1
# # ... round-selector=1
# CR-tameshi-shokunin-r10-1: no corpus/lessons/round-1-aggregator-*.md — the round-1 review duty has no emitted lesson (CORPUS.md:21)
# # verdict tameshi-shokunin failed findings=83 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# # process-exit 1 (failed)                          exit 1
```

Selector sensitivity: **identical finding set and exit** (`83`; `r4,r8,r10`) under `--round 1` and `--round 9`;
only the r10 message's round number changes. The verdict does not depend on the selector. Round 1 is the
selector the committed LOG supports; round 9 is the gate's default.

Determinism: the gate was invoked three times in this seat (default selector twice, `--round 1` once) —
83 findings, r4=81 / r8=1 / r10=1 every time.

### Findings (exact IDs, distribution recomputed from the gate's own output)

- **r4** `CR-tameshi-shokunin-r4-1` … `-81` (81 findings) — "count claim with no backticked command", canonical
  surfaces only. Per file: `knowledge/fleet-suite-census.md` 10; `verification-patterns-fleet.md` 9;
  `gates-survey-kumitate.md` 8; `mutation-case-tsukuroi-census.md` 8; `mutation-case-mado-verify.md` 5;
  `gates-survey-kagi.md` 4; `mutation-case-kumitate-claims.md` 4; `service-standing-state.md` 4;
  `arm-class-matrix.md` 3; `closeout-r11.md` 3; `fleet-kill-rate-ledger.md` 3; `mutation-case-kimi-census.md` 3;
  `operator-runbook.md` 3; `lessons/round-1.md` 3; `lessons/round-10.md` 3; `README.md` 2;
  `mutation-case-kagi-census.md` 2; `mutation-case-kagi-checklist.md` 2; `self-hardening-r6.md` 1;
  `service-limits.md` 1. Total 81.
- **r8** `CR-tameshi-shokunin-r8-1` — `credential-class op-ref occurrences=4 lines=4 files=2 owner=lane`;
  `files=[knowledge/gates-survey-kagi.md,knowledge/service-limits.md]`, `first=knowledge/gates-survey-kagi.md:111`.
  Independently reproduced by grep: `gates-survey-kagi.md:111, :396, :613`, `service-limits.md:128`
  (`grep -n 'op://' knowledge/gates-survey-kagi.md knowledge/service-limits.md` → exactly those 4 lines, exit 0).
- **r10** `CR-tameshi-shokunin-r10-1` — no `corpus/lessons/round-<R>-aggregator-*.md`. Routes to the
  **aggregator** (the filename pattern is the aggregator's per-round review duty), not to the lane.
- Rules that produced **no** finding: **r2** (lessons cite round + evidence), **r7** (phantom index rows),
  **shonen** form. r7 emitted two notes only: `1 backticked path template(s)/glob(s) skipped` and
  `under-coverage (not a finding): 2/26 corpus files carry no index row`.

### What the r4 findings actually are (spot-checked, exact matched substrings)

I re-applied the gate's own regex (`corpus-gate.mjs:267`) to the flagged lines and printed the matched substring:

- `README.md:42` → match `19 notes`; its command sits on the **next** line
  (`README.md:43` = `` `for f in corpus/knowledge/*.md; … | wc -l` → 13 at `4eb4cf3`. ``). Rule-literal fail
  (the rule is line-scoped); the command is present one line below.
- `knowledge/arm-class-matrix.md:418` → `1000 commits`; `fleet-suite-census.md:633` → `1186 lines`;
  `mutation-case-*.md` → `8/10 (80 %)`-style kill-rate lines: **substantive** counts with the pin elsewhere.
- Pattern artifacts (digit+noun labels, not count claims): `lessons/round-10.md:4` → `11, seat`;
  `verification-patterns-fleet.md:1` → `1, lane`; `lessons/round-1.md:462` → `3 line` ("box 3 line breadth");
  `lessons/round-1.md:430` → `25 words` (a **table header** `| id | source @ commit | accessed | quote (≤25 words) | location |`).
  These are rule-literal true, intent false — reported as observed, not smoothed.

## 2. Gate limitations (named)

Declared not-evaluated by the gate itself: **r1** (is a token a source — semantic), **r3** (falsifiability),
**r5** (negative claim carries its sweep — proximity heuristic refused), **r6** (quote names its location —
surface lives outside the repo), **r9** (corrections-never-rewrites; unavailable in `--snapshot` mode, which
grades a `git archive` tree with no history), **box-3 verifier independence**, **SHONEN box truth**.
Additionally `r8`'s schematic-vs-real classification is declared could-not-evaluate (needs a vault read;
operator-gated) — the literal occurrence findings stand regardless. Observed-by-me limitations:

1. **Stale `CORPUS.md:NN` citations in findings.** The gate's message text cites rule lines that the current
   fleet `CORPUS.md` no longer carries: r2 is at `:25` (gate says `:19`), r4 at `:34` (`:28`), r7 at `:46` (`:40`),
   r8 at `:49` (`:43`), r10 at `:61` (`:21`) — `grep -n` on `/home/vgpnk/Projects/shokunin/CORPUS.md`
   (`24/25` sources rules, `34` count rule, `39` negative claim, `42` quote, `46` index row, `49` no credential,
   `53` corrections, `61` round verdict, `156` provenance trio). Rule **IDs** remain the operative key;
   the printed line numbers are metadata drift, so cite rules by ID in the ledger.
2. **r8 occurrence set is meta-reference, not secret material.** All four literals are prose *about* the token
   class (e.g. `service-limits.md:128`: "…any `op://` reference path, any vault item…"; `gates-survey-kagi.md:396`:
   "for `op://` and refuses — so the gate can never resolve a reference"). The rule (`CORPUS.md:49`) bars
   "vault ref paths (`op://…`)" from every corpus literally, and the gate's `# note` says the classification is
   exit-2-class abstention; a reader must adjudicate rule-intent vs literal hit. Verdict stands as literal fail.
3. **r4 is line-scoped and pattern-scoped** (`COUNT_NOUN_RE`, `corpus-gate.mjs:450-463`): it cannot see a
   wrapped command and fires on table headers/labels (examples above). 81/83 findings are r4, so the rule
   mix dominates the verdict; the review notes this without re-adjudicating it.
4. `--snapshot` never reads the child's history: append-only claims cannot be graded in this mode
   (I graded those separately, §5, from the local git history of the original repo).

## 3. SOURCES structural observations (`corpus/SOURCES.md`, 131 lines)

Binding contract: `SOURCES-CONTRACT-v1.md`, cited in `SOURCES.md:4` by bare filename. It exists **outside**
this repo (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, plus copies in the
fleet-aggregate/fleet-ledger/fleet-sources-hardening worktrees); `grep -rn 'SOURCES-CONTRACT'` over the lane
tree returns only that one prose mention. Shape/section order matches `CORPUS.md` §Shape: Registry → Paths →
Search log → Leads (unopened) → Id allocation (`SOURCES.md:8, 57, 63, 101, 123`).

**Census — PROVISIONAL.** Parent direction: a census parser fix for indented Markdown source rows is in
progress elsewhere; totals below are **not final** and must be re-derived after `FINAL LANES READY`.
Canonical commands (from `CORPUS.md` §Census) over the graded tree, results as observed:

| check (command) | result |
|---|---|
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | **44** rows |
| malformed rows (`NF!=13`, contract's awk) | **0** |
| status histogram | mined **12** · queued **29** · rejected **3** (= 44) |
| tier histogram | A **37** · B **5** · C **2** (= 44) |
| duplicate ids / id-format violations / cells containing extra `\|` | none / none / none |
| mined `used-by` paths that do not exist in tree | **none** (all 12 mined rows carry paths) |
| `used-by` = `—` | all 29 queued + all 3 rejected; no mined row |
| `anchor` cells without a numeric revision token; `opened` non-ISO; `recheck` values | none; none; `{90d,180d,365d,730d,on-release}` |

Id space is honest about its hole: rows are S001–S037 and S040–S046, and `## Id allocation` states
"S038–S039 allocated, never written, retired — never reused or renumbered". Registry row count 44 matches
`S001–S037`(37) + `S040–S046`(7) exactly.

Other structural observations (evidence-bearing, non-smoothing):

- The provenance of the graded files is itself declared in-tree: `README.md` §Known gaps names 19 unheadered
  pre-round entries, `SKILL.md:14-15`/`:133-135` staleness, and stale ledger successors — all as debt, not as
  passes. `README.md` §Frontier status correction (appended) demotes F1/F2 from `held` to `partly held` after
  the orchestrator adjudication; the demotion is written as an append, and the table above it is left in place.
- Citation hygiene inside the registry: the own-work/gate rows carry commit **and** blob sha256 prefixes
  (`S031`–`S037`), and `S032`–`S037` pin sibling fleet repos at exact commits
  (`kumitate 175de6ba` ×2 — S032, S037; `kagi fecee874` ×2 — S033, S036; `tsukuroi 165307fe` — S034;
  `mado eead56b2` — S035).
  Those pins were **not** re-opened in this seat (read-only audit of this lane; the gate reads only this lane's tree).
- `## Search log` (3 bullets) records identified/screened/included/excluded counts and a stop rationale per sweep,
  and records one access caveat instead of smoothing it: S020's canonical Springer URL returned an anti-bot body,
  so the quote is taken from the authors' hosted copy (canonical DOI kept in `source`).
- `## Leads (unopened)` = 16 bullets and is explicitly "a lead is not evidence and never a row"; no lead is used
  as evidence anywhere in the graded tree, and the id block says the six opened this round moved out of the list.
- Index coverage (substring-grep method, same as the gate's own note): of the 26 non-README `.md` files under
  `corpus/`, exactly **2** carry no coverage-map row — `lessons/round-10.md` and
  `lessons/round-1-verifier-spotcheck.md`; the gate printed the same count (`2/26`) as a note, not a finding.
  Method caveat: `QUALITY.md`/`SOURCES.md` match **prose mentions** in `README.md`, not index rows.
- `## Gate` sections (`CORPUS.md` §Layout requires one per `lessons/round-<N>.md`): `round-1.md` 2,
  `round-10.md` 1, `round-1-verifier-spotcheck.md` 0 (its filename is not `round-<N>.md`). Observed, not scored.

## 4. Study path — one directly evidenced reading sequence

`corpus/SOURCES.md` §Paths, bullet 1, verbatim:

> **Mutation verdict semantics and validity** — S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007:
> learn the vocabulary first (states, schema, outcomes), then the verdict grammar (witness), then what makes a
> verdict untrustworthy (flakiness, subsumption), and finish with equivalence from the cheapest filter to an LLM agent.

Mechanically checked against the registry in the same file (each id exists; status read from column 8):

| leg | id | source (short) | status |
|---|---|---|---|
| 1 | S001 | Stryker mutant states + metrics (docs) | mined |
| 2 | S002 | mutation-testing-report-schema.json (spec) | mined |
| 3 | S004 | cargo-mutants book, §Using the results | mined |
| 4 | S006 | shmutant README (witness grammar) | mined |
| 5 | S011 | flaky tests vs mutation verdicts (ISSTA 2019) | **queued** |
| 6 | S010 | subsumption threat validity (ISSTA 2016) | **queued** |
| 7 | S009 | Trivial Compiler Equivalence (ICSE 2015) | **queued** |
| 8 | S007 | Mutation-Guided LLM Test Generation at Meta | **queued** |

So the path is a plan whose first four legs are realized: their `used-by` cells point at the two admitted
entries `corpus/knowledge/mutation-score-semantics.md` (S001, S002, S004, S005, S006) and
`corpus/knowledge/witness-scoped-kill-verdict.md` (S006), which `README.md` §Frontier maps to F1/F2 — status
corrected to `partly held`. Legs 5–8 are opened-but-unmined (`queued`), i.e. the path's back half is the
stated next work, not a completed reading. The other two Paths bullets (`Golden and hermetic fixtures for CLI
gates`; `Reduction and generation of fixtures`, 7 ids each) are **entirely `queued`**: plans, not evidence.

Usability note for the aggregator index: the Paths bullets are `- **Title** — S… → S…` lines that a
row-oriented census parser does not count as rows; the ids they name are only resolvable against the Registry
table (this seat resolved them that way, 22/22 ids present).

## 5. Provenance frontmatter scan (parent directive, bounded)

Scope: first 6 lines of each `corpus/knowledge/**/*.md` (21 files at this HEAD).

- **Full trio (`source:` + `verified-at:` + `recheck:`) present in exactly 2 files**:
  - `mutation-score-semantics.md` — `source:` S001/S002/S004/S005/S006 with URLs, sections and fetch dates;
    `verified-at: 2026-10-19`; `recheck: 180d — \`curl -fsSL 'https://stryker-mutator.io/…/mutant-states-and-metrics/' | grep -c 'detected / valid'\` (ran; 1)`.
  - `witness-scoped-kill-verdict.md` — `source:` S006 @ commit `7eefc730…` with fetched-at `2026-10-19T22:03:41Z`
    and SHA-256 `dc0051c7…`; `verified-at: 2026-10-19`; `recheck: 90d — \`curl -fsSL …/shmutant/main/README.md | grep -c 'not on its witness'\` → 1 (2026-10-19; main branch, so a README drift away from the pinned commit shows as 0)`.
- The other **19** knowledge files carry none of the three keys in their first 6 lines — consistent with
  `README.md` §Known gaps ("0 of 19 open with `source:`/`verified-at:`/`recheck:`") and `QUALITY.md` 10
  ("old entries: named debt").
- **Ephemeral-pointer check: none.** No `recheck:`, `source:` or `verified-at:` value in those files points at
  `.tower/worktrees` or `/tmp` (regex `\.tower/worktrees|/tmp` over the parsed values → no hits). Both recheck
  values are re-runnable network commands with a cadence, not scratch-path pointers — **no provenance/fidelity
  finding of the `/tmp`-or-worktree class for this lane**.
- Supporting append-only check (from local history, not the snapshot): `git log --numstat -- corpus/QUALITY.md`
  → `8 0` (round 0) and `22 0` (fleet round 1) — zero deletions, so `QUALITY.md`'s "Criteria 1–5 are unchanged"
  holds at the diff level; `git log --numstat -- corpus/SOURCES.md` → `121 0` and `10 0` — SOURCES.md has never
  had an in-place edit at all (contract rule 2's in-place allowance is unused). `QUALITY.md` criteria 6–10 each
  cite an existing mistake id: MK-2…MK-7 all present in `lessons/round-1.md:281-286` (`grep -c` = 4/1/2/2/2/5).

## 6. Repo identity and commit-read feasibility after the jj migration

All reads used the **original** path `/home/vgpnk/Projects/shokunin/tameshi-shokunin` (no retired worktree).

- `git rev-parse HEAD` → `a21e9104723e7a46b794b03b8fdcdd1455696f7e`; `HEAD^{tree}` → `34dbf7ca2a09185930146e3033547e3da03bbdc5`;
  `git status --porcelain` → 0 lines (re-checked after every read step, including after the jj commands).
- Revision-bound identity for reproductions: `git archive --format=tar a21e9104723e7a46b794b03b8fdcdd1455696f7e | sha256sum`
  → `99509b720ab2cd1663c7009c62a9c793306dabaecdd90ed649ae83dfcc8fa132`. The gate itself extracted the graded tree the
  same way (`# note … extracted with: git archive a21e910… | tar -x -C <tmp>`), so **commit-read at this exact
  revision works** and produced the tree this note grades.
- History is intact and readable: `git log --oneline -3` → `a21e910 round-1 verifier spot-check (integrator, kaika)…`,
  `01b358c round-1: post-review fixes`, `121696b round-1: phase-2 corrections — census v2 + Gate quotes for S031-S037…`;
  `git ls-tree -r --name-only HEAD -- corpus` → 27 files (21 knowledge + 3 lessons + README + QUALITY + SOURCES).
- jj state (colocated): `.git` is a real directory; `.jj/repo/` and `.jj/working_copy/` exist;
  `git for-each-ref` shows `refs/heads/master a21e910` plus four jj keep refs
  (`refs/jj/keep/{4db5670,4eb4cf3,a21e910,c950c71}`).
  `jj --ignore-working-copy -R . status` → `The working copy has no changes.`; working-copy commit
  `notxzlxy c950c710 (empty) (no description set)` whose parent is `slktqtpp a21e9104 master | round-1 verifier
  spot-check…`; `jj --ignore-working-copy bookmark list` → `master: slktqtpp a21e9104`.
  **Reading git HEAD is still the correct content identity**: jj's extra WC commit is empty, and jj itself
  reports no working-copy changes.
- **Limits found (these bound every revision claim in this note):**
  1. **The graded revision is local-only.** `git rev-list --count refs/remotes/origin/master..HEAD` → **4**;
     `refs/remotes/origin/master` = `4eb4cf3`. A reader who fetches `https://github.com/VeigaPunk/tameshi-shokunin.git`
     gets `4eb4cf3`, which is **not** `a21e9104` and cannot reproduce this verdict. Revision citations must name
     the local commit, and the ledger must not equate them.
  2. Snapshot mode grades a history-free `git archive` tree, so append-only / authorship claims (r9-class) are
     not checkable there — graded separately above from local history (§5).
  3. jj command side effects: the first `jj log` in this seat ran **without** `--ignore-working-copy` (jj may
     refresh `.jj/working_copy` metadata on any command). Tracked bytes were verified unchanged — `git status
     --porcelain` was empty before and after, and the graded archive digest above was produced after that call.
     All later jj queries used `--ignore-working-copy`.
  4. `.gitignore` = `.ufo/interactive-sessions/` only; nothing suppresses `corpus/` or `.jj` tracking, so
     porcelain cleanliness is a real content signal here.

## 7. Scope of what I did not check

Not checked (out of the assigned scope, stated so no reader over-reads this note): no semantic re-verification
of any `knowledge/` claim or of the recorded kill rates; no re-open of the sibling-repo pins (S032–S037);
no build/test/lint run in the lane (forbidden by the wave contract); no re-derivation of the census beyond the
provisional numbers in §3; the other 18 knowledge-file bodies were read only for the bounded checks above;
gate internals were read only to describe r4/r8/r10 (no re-adjudication of the 81 r4 rows one by one —
I characterized them by pattern and spot-check, not by exhaustive re-litigation).