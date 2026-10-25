# kaika W3 — non-author verification: kake round 20 (resume)

Reviewer: W3ReviewKake (fresh orchestrator-dispatched reviewer; not the lane's L1/L2 seats).
Lane commit: `02b6dd05037376e9fe3af64640d172e0426d397a` (`02b6dd050`), branch `kaika/round`, base `cb807bc8d`.
Fleet report: `.ufo/reports/round-20/kake.md` (ledger worktree). Scratch under `/tmp/kaika-verify/kake/` (deleted at end).
Method: `git archive` of base and head into scratch; `git clone` of the lane at `02b6dd050` for replay (lane untouched; no writes, no branch switches).

## Verdict (recommendation)

**ADMIT with conditions.** All three claims reproduce on their own counting commands. Provenance, census, credential sweep: clean. Two conditions and one correction before the orchestrator records closure:

1. Append-only (check 2) is violated literally: 17 prior lesson lines were rewritten in place (suffix tails), plus suffix edits to knowledge files, SKILL.md and README and 5 deleted SCORECARD state lines. Every altered base line is preserved once the tails are stripped (mechanically checked), so the lane's own `Append-only tails` criterion passes. Orchestrator must either waive this exception on the record or order a re-land with tails on new lines.
2. The report's Expansion basis is wrong (3 of the 4 entries are supersessions of covered ground, not new ground). Verdict stands on the capability row + the one frontier entry; the sentence must be corrected.
3. C1 is gate-green by annotation: the stale set itself did not move (missSet 55 → 55). Record C1 as "verified on its counting command; underlying cited-path set unchanged", not as a freshness gain in substance.

## 1. Provenance (check 1) — PASS

Command: `git log --format='%h %an <%ae> | %cn <%ce> | %s' cb807bc8d..02b6dd050`
Output: `02b6dd0 kake-shokunin <kake@shokunin.local> | kake-shokunin <kake@shokunin.local> | round-20: resume — citation-local debt cleared, confinement proof closed, curated source registry`
One round commit; author and committer are the lane identity. Branch `kaika/round`. `git branch -r --contains 02b6dd050` printed nothing → not pushed (consistent with the "No push" rule the report names).

## 2. Append-only (check 2) — FAIL-literal / PASS-criterion

Command: `git diff --numstat cb807bc8d 02b6dd050 -- LOG.md corpus/lessons corpus/QUALITY.md`
Output: `41 0 LOG.md` · `10 0 corpus/QUALITY.md` · `138 0 corpus/lessons/round-20.md` · `4 4 round-17.md` · `1 1 round-18.md` · `1 1 round-4-aggregator-audit.md` · `1 1 round-4.md` · `1 1 round-6-aggregator-audit.md` · `9 9 round-7.md`.

- LOG.md and QUALITY.md: additions only. round-20.md: additions only.
- Prior lines altered (all in-place suffix appends, `*[r20 citation-local …]*` or `**[r20-correction …]**`):
  - `corpus/lessons/round-17.md` — 4 lines (the `~/DIRMAP.md` and `~/projects` bullets, W6 note, §2 coverage-gap line; diff hunk `@@ -10,15 +10,15 @@`).
  - `corpus/lessons/round-18.md:32` — 1 line (`--selftest regressed …`).
  - `corpus/lessons/round-4-aggregator-audit.md` — 1 line (`grep -o 'code: [0-9]*'` bullet).
  - `corpus/lessons/round-4.md:1-7` — 1 line (`Cites:` header).
  - `corpus/lessons/round-6-aggregator-audit.md:45-52` — 1 line (`zip-exclude chain` row).
  - `corpus/lessons/round-7.md:9,17-19,37-41` — 9 lines (correction tails on the no-orphan proof and the two-direction paragraph).
- Mechanical stripped-diff check (python difflib over `git show cb807bc8d:<f>` vs `git show 02b6dd050:<f>`; tails removed by regex `\s?\*{1,2}\[r20.*?\]\*{1,2}`): every altered line in the six lesson files above is equal to its base line after tail removal — 17/17.
- Mid-path defect: `corpus/lessons/round-18.md:32` — the tail is inserted inside the code span `` `~/Projects/ `` so the rendered text reads `~/Projects/ [annotation] webzites/fleet` on the next line; the cited path is split.
- Other files touched by suffix tails (same stripped check, all equal): `corpus/knowledge/{drift-detection, fire-journal-codes, fleet-registry, free-read-verbs(2), freshness-sweep, ghp-subpath-spotcheck, probe-delta-alerting(2), publish-channels(5), publish-queue, sitemap-orphan-audit(8), speedrun-pipeline}.md` = 11 files / 27 lines; `corpus/README.md` 3/3; `SKILL.md` 9 tails + row 212 (tail appended at the end of the gate-registry row and one new paragraph, a pure append on re-inspection).
- Not suffix-only: `SCORECARD.md` — 5 deleted lines (`| — none yet — |` capability placeholder; the "none enter through this rollout" sentence; the 3-line saturation placeholder), replaced by the round's capability row and saturation declaration. SCORECARD is a state file, not in the append-only list; the replacement is a state update, but the report does not disclose it as a rewrite.
- `PROVINCE.md`: additions only (`git diff --numstat`: `42 +`). `scripts/freshness-sweep.mjs`: code change (C2), expected.
- `corpus/knowledge/freshness-pins.json`: not in the diff (pins untouched, as claimed).

## 3. Claims (check 3) — C1 verified (caveat), C2 verified, C3 verified

Commands run on `/tmp/kaika-verify/kake/{base,head}` (git archive trees) and `/tmp/kaika-verify/kake/clone` (lane clone at 02b6dd050).

**C1 freshness** — `node scripts/freshness-sweep.mjs --section=paths`

| | base cb807bc8d | head 02b6dd050 | report claim |
|---|---|---|---|
| exit | 1 | 0 | 1 → 0 — verified |
| verdict line | `VERDICT: DRIFT — §paths: 7 unannotated miss · 0 NOT in pins.pathsMissSet (exit 1)` | `VERDICT: OK (exit 0)` | verified |
| drift | 7 | 0 | 7 → 0 — verified |
| declaredAbsent | 48 | 55 | 48 → 55 — verified |
| missSet | 55 | 55 | 55 → 55 — verified |
| set-delta miss | `no new miss` | `no new miss` | newMissing 0 — verified |
| unannotated locations | 26 (sum of `N of M cites unannotated`: 2+5+1+1+4+8+5) | — | 26 — verified |
| annotations in tree | — | `grep -rhoF -- '[r20 citation-local' corpus SKILL.md` → 26 | 26/26 — verified |

Caveat: the 55 cited paths that are absent are still absent and unverifiable (`missSet` unchanged); C1 moved them from "unannotated" to "annotated historical record". Verdict: verified on the counting command; the substantive stale set is unchanged.

**C2 operability** — selftest and mutation replay

- `HOME=$(mktemp -d) KAKE_SELFTEST_DIR=$(mktemp -d) node scripts/freshness-sweep.mjs --selftest`: base `selftest: 14/14 passed`, regions `B19,B1095,E1166,B1346,E1348,B1366,E1368`; head `selftest: 15/15 passed`, regions `B1154,E1225,B1515,E1517`; head e2 line: `caught 26/26 mutants · apis 31/31 pin=match`. Matches report.
- `node .ufo/round-20/resume/confinement-mutants.mjs` at the clone: `MUTANTS cb807bc: killed 0/25 survived 25/25`; `MUTANTS working-tree: killed 25/25 survived 0/25`. Matches report (0/25 → 25/25).
- `node .ufo/round-20/replay-proof.mjs` at the clone: `CITATION_LOCALITY_PROOF: PASS (cases=7, failures=0)`. Matches report.
- `--section=paths --json --offline`: old program (base) and new program (head) on the same tree differ only in a `note` field (`repoRoot via override (script-derived: …/base)`) produced by my invocation path; the paths/offline payloads are otherwise identical. Verified modulo that harness artifact.
- Named residuals (child-process `execFileSync`, aliasing, bracket access) survive on both revisions — the report says so (`confinement-reviewer-recipe.txt`); the claim is scoped correctly ("direct fs write APIs").
- Not re-run: the post-land probe `confinement-mutation-probe.txt` (9/18 → 8 survivors re-run killed) — outside the declared counting commands.

Verdict: verified.

**C3 capability** — registry census

- `bash …/fleet-census/scripts/sources-census.sh validate <lane>` → `kake-shokunin	ok	…/corpus/SOURCES.md`, exit 0.
- Contract commands, run literally in the lane tree: rows `18`; malformed `0`; tiers `A=16 C=2`; status `mined=14 queued=2 rejected=2`; duplicate ids: none; enum/tier-inflation: none; mined used-by missing paths: none.
- Tier × kind: A — spec 3, docs 8, code 3, dataset 1, own-work 1; C — docs 1 (S017), community 1 (S018). Matches report.
- Mined-row citations (python: each `mined` row's id must appear in each used-by file): 16 row→file pairs, 16 confirmed, 0 missing.
- Superseded literals (`sh .ufo/round-20/resume/old-strings.sh`): head `0`; base (run from base tree, same script) `9` — 2+1+2+1+1+2 per literal. Matches report (9 → 0).
- Correction tails: `grep -rhoF -- '[r20-correction' corpus SKILL.md README.md PROVINCE.md` → 27, in 7 files. Matches.
- Capability row present: `SCORECARD.md:191` `| Curated source registry | …`. Matches.

Verdict: verified.

## 4. SOURCES (check 4) — PASS; rows re-opened 18/18

Census exit 0 (above). Re-opened sources (curl to scratch, quotes grepped):

| Row | Opened | Gate quote / location | Result |
|---|---|---|---|
| S001 (tier A, code) | `action.yml` @5f327015 and @7b1f4a76 | `include-hidden-files` description, line 18 ("Include hidden files and directories … Excludes .git and .github regardless."); archive exclusions lines 37–39 `--exclude=.[^/]*`; v4.0.0 @7b1f4a76 lines 33–35 `--exclude=".[^/]*"`; default `"false"` line 20 | verbatim — pass |
| S002 (tier A, code) | release v4.0.0, v5.0.0 | "Potentially breaking change: hidden files (specifically dotfiles) will not be included in the artifact"; v5 "feat: add include-hidden-files input" | verbatim — pass |
| S003 (A, docs) | GitHub Pages publishing source | "You can publish your site when changes are pushed to a specific branch, or you can write a GitHub Actions workflow…" | verbatim — pass |
| S004 (A, docs) | custom workflows | "compressed gzip archive containing a single tar file"; "under 10GB in size and should not contain any symbolic or hard links" | verbatim — pass |
| S005 (A, docs) | managing custom domain (`.md`) | Step 4, custom Actions workflow: "no CNAME file is created, and any existing CNAME file is ignored and is not required." | verbatim — pass; recheck count `2` |
| S006 (A, docs) | Jekyll defaults | "Start with `_`, `.`, or `#`"; "End with `~`"; "Are located in a folder called `/node_modules` or `/vendor`" | verbatim — pass |
| S007 (A, docs) | Pages REST API | `build_type` enum `legacy, workflow, null`; `protected_domain_state`; body param `cname string or null` | fields pass; gate quote "`cname`: required, string or null" is **not verbatim** (page reads "cname string or null") — minor |
| S008 (A, docs) | GNU tar texi @cfdb891 | line 8587–8588 "Default is @option{--no-anchored} for exclusion members and @option{--anchored} inclusion members."; line 8602 "When wildcards match slash (the default for exclusion members)" | verbatim (texinfo markup) — pass; but served-set entry labels "GNU tar 1.35": `grep -c 1\.35 tar.texi` = 0 (file uses `@value{VERSION}`) — unsourced version label; SOURCES anchor says 8478-8617, gate says 8478-8603 (both contain the quotes) — minor |
| S009 (A, code) | nginx release-1.28.0 `ngx_http_core_module.c` | `ngx_http_set_etag` line 1682; `ngx_sprintf(… "\"%xT-%xO\"" …)` lines 1708–1710 | pass; `grep -cF '%xT-%xO'` = 1 |
| S010 (A, spec) | RFC 9110 | line 3574 "An entity tag is an opaque validator"; line 3407 "A strong validator might change for reasons other than a change to…"; line 3459 "…one-second resolution, might be a weak validator" | pass |
| S011 (A, spec) | RFC 9309 | line 351–352 "The rules MUST be accessible in a file named "/robots.txt" … in the top-level path of the service"; line 395 "crawler MAY access any resources"; line 402 "MUST assume complete disallow" | pass |
| S012 (A, spec) | sitemaps.org | "The location of a Sitemap file determines the set of URLs…" | pass |
| S013 (A, docs) | Google sitemap build | "unless you submit your sitemap through Search Console, a sitemap affects only descendants of the parent directory" (markup spacing only); "Last updated 2026-07-08 UTC" | pass |
| S014 (A, own-work) | `scripts/freshness-sweep.mjs:404-411` | comment "Annotation window = the citing line ±2 (spec), with every *citation* on the citing line blanked" — lines 404–408 at head | pass (own gate output reproduced in §3) |
| S015 (A, docs) | Pages limits | "Published GitHub Pages sites may be no larger than 1 GB." | pass |
| S016 (A, dataset, queued) | `pages.github.com/versions.json` | `"jekyll":"3.10.0"`, `"github-pages":"232"` | pass |
| S017 (C, rejected) | Astro deploy guide | "Add a ./public/CNAME record to your project." (step under "Change your GitHub URL to a custom domain"); page uses `withastro/action` (4) and `deploy-pages` (2) | pass — the rejection context is an Actions deploy |
| S018 (C, rejected) | DebugBear article | "Mozilla released version 114 of Firefox on the 14th of October 2025." (heading "INP support in Firefox 114") | pass — the article itself carries the version error; Firefox 144.0 release notes: "October 14, 2025" and "PerformanceEventTiming.interactionId" under Web Platform |

Other checks: `corpus/knowledge` lists `S014` in `freshness-sweep.md` (used-by) ✓. `S001`/`S002` tier-A scope is the action's own code/release; the entry's `[INFERENCE]` on tar depth is labelled ✓.

## 5. Discernment spot-check (check 5, `LEARNING.md`)

| # | Candidate | Gate decision | Re-opened evidence | Verdict | Reason |
|---|---|---|---|---|---|
| 1 | `corpus/knowledge/ghp-custom-domain.md` | admit | S005 step 4 context verbatim (custom Actions workflow → CNAME ignored); recheck argv returns `2` | **agree** | Claim scoped to workflow publishing and explicitly says it does not establish the lane's current mode; falsifier named; `build_type` debt named |
| 2 | S017 Astro `public/CNAME` (rejected, tier C) | reject | Astro guide instructs `./public/CNAME` for an `withastro/action` deploy; GitHub's custom-workflow docs say a CNAME file is ignored | **agree** | Tier-A GitHub docs outrank the framework guide for the Actions case; the flip is stated |
| 3 | S018 DebugBear "Firefox 114" (rejected, tier C) | reject | DebugBear says "version 114 … 14th of October 2025" (its own error); Firefox 144.0 notes carry `interactionId` | **agree** | Version/date conflict resolved by tier-A release notes; registry admits no number from the tier-C source |
| 4 | `corpus/knowledge/crawl-scope-per-host.md` (admit, frontier) | admit | RFC 9309 quotes at lines 351–352, 395, 402 | **agree** | Host-root scope and 4xx/5xx semantics match the RFC; lane population (3 project sites) reproduced by the recheck |
| 5 | `corpus/knowledge/ghp-etag-anatomy.md` (admit, with `[INFERENCE]` on backend identity) | admit | nginx lines 1708–1710; RFC 9110 lines 3407, 3459; `printf`/`date` recheck → `79453`, `2026-09-24T02:55:35Z` | **agree** (with a note) | Format match is labelled as weak inference; the admitted claim (ETag is not identity) is what RFC 9110 supports |
| 6 | Scout's eight GHP "refined/unverifiable" observations (not admitted) | not admitted → frontier | — (would need live reads; live probing is out of scope) | **agree** | Holding them as frontier rather than corrections is the stated discipline |

Sample: 1 admit + 2 rejects + 2 extra admits + 1 held-back set — all agree. Small n: discernment `improved` on this sample.

## 6. New knowledge entries (check 6) — PASS

| Entry | `source:` / `verified-at:` / `recheck:` | Recheck run | Claim vs source |
|---|---|---|---|
| `ghp-served-set.md` | present | `for v in v3.0.1 v4.0.0 main …grep -cF -- '.[^/]*'` → `v3.0.1 0`, `v4.0.0 3`, `main 3`; `--exclude=.github` loop → `3 3 3` | matches S001/S002 (one minor: "GNU tar 1.35" label unsourced, §4) |
| `ghp-custom-domain.md` | present | `curl …managing-a-custom-domain….md \| grep -cF 'any existing `CNAME` file is ignored'` → `2` | matches S005/S007; named debt (build_type unknown) is honest |
| `ghp-etag-anatomy.md` | present | `printf '%d\n' 0x1365d` → `79453`; `date -u -d @$((0x6ab49127))` → `2026-09-24T02:55:35Z`; nginx `grep -cF '%xT-%xO'` → `1` | matches S009/S010; LOG.md:161-163 records `79,453B … etag 6ab49127-1365d` ✓ |
| `crawl-scope-per-host.md` | present | RFC `grep -cF 'top-level path of the service'` → `1`; population `grep -oE 'veigapunk\.github\.io/[A-Za-z0-9-]+/' SKILL.md corpus/knowledge/fleet-registry.md \| sed … \| sort -u \| wc -l` → `3` (charter-ufo-fsd, lucario, plazir-15-site) | matches S011–S013 |

Each entry maps to QUALITY criteria and names debt (no live probe). The 4 entries cite `mined` rows ✓.

## 7. Credentials (check 7) — PASS

`git diff cb807bc8d 02b6dd050 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1). Broader `op://|BEGIN … PRIVATE KEY|ghp_|AKIA|xox[baprs]-` count → `0`.

## 8. Report (check 8) — PASS with conformance defects

- Present: `Work performed`, `Landed changes`, `Before → after measurements`, `SHONEN`, plus `Sources & frontier`, `Mistakes`, `Trend verdicts`, `L0 questions`, `Integrator notes`.
- Order defect: `SHONEN` appears after `Trend verdicts`; §4 lists it fourth in order (minor).
- SHONEN: four `[~]`, zero `[x]`, each with a resolvable pointer ✓.
- Round commit cited (`02b6dd05037376e9…`) ✓; LOG.md:600, lesson lines 146/182/241, QUALITY.md 14–20, PROVINCE.md 10/20/28/39, SCORECARD.md 19/191/197, freshness-sweep.mjs 1078/1505 — all resolve at `02b6dd050` ✓.
- Report says "Push: none" and names the precedence ✓; the commit is not on any remote branch ✓.
- Mistakes table: 16 base classes (M1–M11, A1–A4, T1) + 4 new (R1–R4); 7 criteria each citing its lesson ✓.

## Per-axis verdicts (axes the lane scores: operability, freshness)

- **freshness** — `improved` on the gate's terms (C1 verified; drift 7 → 0, 26 → 0 unannotated). Substance caveat: missSet 55 → 55; no cited path was repaired or re-verified. Score stays 10 (ceiling; `HOLD 10`). Recommend SCORECARD row record the caveat.
- **operability** — `improved` (C2 verified: selftest 14 → 15, mutant kill 0/25 → 25/25, replay-proof PASS 7/7; residual bypasses named). Score stays 10 (`HOLD 10`).
- **capability (curated source registry)** — `entered` (census exit 0; contract commands clean; 16 A / 2 C; 14 mined, all cited).
- No axis harmed on the evidence.

## Trend verdicts

- **Expansion — `improved`, basis must be corrected.** The report says 4 entries cover "ground the coverage map did not hold". Evidence: base `corpus/README.md:26` already covers "GHP orphan impossibility proof (deploy = full-tree artifact)"; base `corpus/knowledge/publish-channels.md:9` already says the CNAME file pins the domain; base `corpus/knowledge/publish-queue.md:255-261` already covers the ETag anomaly. Those three are supersessions (quality trend), not new ground. Only `crawl-scope-per-host.md` enters uncovered/frontier ground. The verdict still holds via the admitted capability row and the frontier entry (LEARNING.md counts both under expansion).
- **Quality — `improved`.** 27 source-backed correction tails (verified by count); the superseded-literal count 9 → 0 (verified); the stripped-diff check passes for every altered base line; 4 knowledge entries with reproduced rechecks. Caveat: C1's "freshness" is annotation-level (see above).
- **Discernment — `improved` on a small sample.** 3 of 3 sampled gate decisions agree on re-open (§5). Learned classes captured as QUALITY criteria (7) with lesson citations.

## Defects by severity

Medium
- M1. Append-only literal breach: 17 prior lesson lines rewritten in place (round-17 ×4, round-18 ×1, round-4-aggregator-audit ×1, round-4 ×1, round-6-aggregator-audit ×1, round-7 ×9); 27 knowledge-file lines and SKILL.md/README suffix tails; 5 SCORECARD state lines deleted. Content preserved (stripped check: all equal), so the lane's `Append-only tails` criterion passes. Orchestrator ruling needed (waiver vs re-land with pure appends).
- M2. Expansion basis overstated (3 of 4 entries are supersessions of covered ground). Verdict stands; text must change.
- M3. C1 is gate-green by annotation: `missSet 55 → 55`, `declaredAbsent 48 → 55`. The report's `freshness improved` should carry this caveat in the SCORECARD row.

Low
- L1. `corpus/lessons/round-18.md:32` — annotation inserted inside a code span, splitting `~/Projects/webzites/fleet` in rendered text.
- L2. Report §4 order: `SHONEN` placed after `Trend verdicts`.
- L3. S007 gate quote "`cname`: required, string or null" is not verbatim; the page reads "cname string or null".
- L4. `ghp-served-set.md` "GNU tar 1.35": version not in the cited file (`@value{VERSION}`); S008 anchor range (8478-8617) disagrees with the gate's (8478-8603).
- L5. SCORECARD edits replace placeholder lines (capability placeholder, saturation placeholder) without a rewrite note in the report.

## Verification gaps (not run or not verifiable)

- Post-land mutation probe (`confinement-mutation-probe.txt`, 9/18 → 8 re-run killed) — not re-run.
- Reviewer/critic/mutation-tester subagent outputs — not reviewed as evidence; this review is independent of them.
- No live-target reads (out of scope for kake; documentation-only). `ds4cc`/`plazir` workflow pins and `build_type` remain unknown (the lane's named debt).
- Harness note: my JSON comparison differed only by the `note` field of my own invocation path, not by any lane output.

## Admit / reject recommendation

**Admit with conditions:** C2 and C3 verified; C1 verified on its command with caveat M3; no axis harmed; provenance, census, credential sweep clean. Conditions: (a) M1 ruled by the orchestrator (recommend waiver recorded in LOG with the stripped-diff evidence, or a re-land with pure appends); (b) M2 text corrected in the report; (c) L3/L4 quote fixes in the knowledge entry and SOURCES anchor. None of these blocks the claims themselves.

## Scratch

`/tmp/kaika-verify/kake/` removed after this file was written.
