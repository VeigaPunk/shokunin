# kaika W3 — non-author verification: tameshi fleet round 1

Reviewer: `W3ReviewTameshi` (fresh orchestrator-dispatched task; non-author). Read-only. Scratch was `/tmp/kaika-verify/tameshi/` (deleted at end).
Lane: `tameshi-shokunin`, branch `kaika/round`, base `4eb4cf319`, round head `121696bf9` (content `c7986cd`). Report: `fleet-ledger/.ufo/reports/round-1/tameshi.md`.
Working tree at review: clean (`git -C <lane> status --short` → empty).

## 0. Recommendation

**ADMIT WITH CONDITIONS.** Every numeric claim reproduces at both revisions. The census and the credential sweep are clean. Both new knowledge entries pass the header bar, their rechecks run, and their numbers reproduce from the evidence files. Nothing harms an axis.

Conditions (append-only corrections; none reopens the measurements):
1. Relabel the trend self-verdict `quality: improved` → `unchanged` (defect M2).
2. Relabel frontier F1 and F2 from `held` → `partly held` (M3).
3. SCORECARD K1/K2 "Measured commit" cells are pointer text, not hashes; the K2 counting command names the superseded v1 census (L1, L2).
4. The lesson `## Gate` spot-check reads `pending` by design. The orchestrator appends the Section 5 result.
Calibration: pin **8**, not 10. Do not promote any SHONEN box to `[x]`; all four stay `[~]`.

## 1. Checks

### Check 1 — Provenance: PASS
`git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 4eb4cf319..121696bf9` →
```
121696b tameshi-shokunin <tameshi@shokunin.local> | tameshi-shokunin <tameshi@shokunin.local> | round-1: phase-2 corrections …
c7986cd tameshi-shokunin <tameshi@shokunin.local> | tameshi-shokunin <tameshi@shokunin.local> | round-1: close fleet round 1 …
```
Both commits carry the lane identity as author and committer.

### Check 2 — Append-only: PASS
`git -C <lane> diff -U0 4eb4cf319..121696bf9 -- LOG.md corpus/lessons corpus/QUALITY.md | grep -nE '^-[^-]'` → no output (zero deleted or modified prior lines).
Numstat: `LOG.md 82/0`, `corpus/lessons/round-1.md 208/0` (new file), `corpus/QUALITY.md 22/0`, `PROVINCE.md 27/0`, `corpus/README.md 67/0`.
Other ledgers, for completeness: `SCORECARD.md 73/1` (the single deletion is the `| — none yet — |` capability placeholder). `SHONEN.md 3/3`, the box-3 status and evidence lines (the round's claim) and the box-4 evidence line. `corpus/SOURCES.md` is a new file.
`SKILL.md` and `tools/` are byte-unchanged: `git diff --quiet 4eb4cf319..121696bf9 -- SKILL.md tools/` is clean, and `sha256(SKILL.md @ 4eb4cf319) = 33e3009c…0f81 = sha256(SKILL.md @ 121696bf9)`.

### Check 3 — Claims: all counting commands re-run at both revisions

Each command was run as `git -C <lane> show "$REV:<path>" | …` with `REV=4eb4cf319` and `REV=121696bf9`. Directory-level counts were run on `git archive` extracts.

| Claim | Command (verbatim core) | 4eb4cf319 (before) | 121696bf9 (after) | Report says | Verdict |
|---|---|---|---|---|---|
| K1 calibration | command C: `git show "$REV:SHONEN.md" \| python3 -c '…asserted_mark_upper_bound=min(8,2*m.count("~"))…'` | `boxes=4 checked=0 asserted=3 untouched=1 asserted_mark_upper_bound=6` | `boxes=4 checked=0 asserted=4 untouched=0 asserted_mark_upper_bound=8` | 6 → 8 candidate | **verified** as a count. Pin is the reviewer's call (Section 2). |
| K1 support | `git show "$REV:corpus/QUALITY.md" \| grep -cE '^[0-9]+\.'` | 5 | 10 | 5 → 10 | **verified** |
| K2 sources-registry | `git show "$REV:corpus/SOURCES.md" \| grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | absent (exit 1) | 44 | 0 → 44 | **verified** |
| K2 tiers/status | fleet `sources-census.sh census <lane>` | — | `rows 44; tier A 37 · B 5 · C 2; mined 12 · queued 29 · rejected 3; missing 0` | A37 B5 C2; mined12 queued29 rejected3 | **verified** |
| K2 census (contract v1 + H4) | `bash .ufo/evidence/kaika-round-1/sources-census-v2.sh` (cwd = lane) | — | `SOURCES_CENSUS: CLEAN (contract v1 + H4 id-or-path)`, `count=25` (informational), exit 0 | exit 0 CLEAN | **verified** (v2). See L2: the SCORECARD K2 row names v1. |
| K2 contract validate | `bash <fleet-census>/scripts/sources-census.sh validate <lane>` | — | see Check 4: exit **1** on this host, exit **0** under `TZ=UTC` | "contract census clean" | **conditional**. Passes only with `TZ=UTC`. Tool defect M1. |
| Guardrail D (depth) | `git show "$REV:tools/mutate-and-run.sh" \| python3 -c '…recorded_cases…'` | `recorded_cases=6 depth_score=6` | `recorded_cases=6 depth_score=6` | unchanged | **verified** |
| Expansion: index | `for f in corpus/knowledge/*.md; do b=${f##*/}; grep -qF "knowledge/$b" corpus/README.md \|\| echo "$b"; done \| wc -l` | 13 (of 19 files) | 0 (of 21 files) | 13 → 0 | **verified** |
| Expansion: headers | `head -5 "$f" \| grep -c '^source:'` per file | 0/19 | 2/21 | 0/19 → 2/21 | **verified** |
| Capability: mutation runner | `bash tools/mutate-and-run.sh --selftest` (scratch copy of `tools/` @ 121696bf9) | — | `MUTATE_SELFTEST: 80/80 pass`, exit 0 | demo | **verified** (re-run) |
| Capability: regression ledger | `bash tools/mutate-and-run.sh --regression` | — | not re-run (needs sibling repos at pins). Evidence: `capability-demo/h1b-regression.exit` = 0; `…stdout:35` = `REGRESSION: PASS (cases=6 passed=6; …)` | demo | **evidence-only**, not re-run |
| Credentials (Check 7) | see Check 7 | — | none | — | pass |

Two informational values: the `https?://` hit count in `SKILL.md PROVINCE.md corpus` is 0 at base and 4 at head. All four are SOURCES, README, and knowledge citations, as designed.

### Check 4 — SOURCES: PASS with one tool-environment caveat

`bash <fleet-census>/scripts/sources-census.sh validate <lane-dir>` on this host:
```
tameshi-shokunin	E08	S001 opened=2026-10-19
… (44 E08 lines, S001–S037 and S040–S046) …
EXIT=1
```
With `TZ=UTC` (same command):
```
tameshi-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tameshi-shokunin/corpus/SOURCES.md
EXIT=0
```
Root cause, reproduced: `date -d 2026-10-19 +%s` → `1792378800` (local UTC−03), while `TZ=UTC date -d …` and `gawk mktime(…,1)` give `1792368000`. The tool compares `epoch(opened)` computed with local-time `date -d` (census script line 245) against `today_s` computed as UTC (line 80). On a negative-offset host, today's date is "future". So E08 fires for every row opened today. The lane's data is valid. The defect is M1 (fleet-census tool, not the lane).

`bash .ufo/evidence/kaika-round-1/sources-census-v2.sh` (cwd = lane) → `SOURCES_CENSUS: CLEAN (contract v1 + H4 id-or-path)`, exit **0**.
Census totals (fleet census): `rows 44 · tier.A 37 · tier.B 5 · tier.C 2 · status.mined 12 · status.queued 29 · status.rejected 3 · missing 0`.

Re-opened rows (six external rows, sampled per contract rule 1 and check 4):

| Row | Tier / status | Gate quote (lesson) | Re-open result |
|---|---|---|---|
| S001 Stryker mutant states (docs) | A / mined | "Mutation score detected / valid * 100" (lessons:360) | `curl` → page contains `detected / valid * 100` and `killed + timeout`. Anchor §Metrics / §Mutant states present. **Match.** |
| S004 cargo-mutants (outcomes) | A / mined | "This is inconclusive about test coverage and no action is needed" (lessons:363) | `curl` → both halves present in §Mutant outcomes. **Match.** |
| S006 shmutant README @ `7eefc73…` | A / mined | "The suite went red on its witness. The test detects the defect." (lessons:365) | `curl` pinned blob, sha256 `dc0051c7…178a3` = witness-entry digest. Line 29 reads "The suite went red **on its witness**. The test detects the defect." **Match** (bold markup only). |
| S029 mutate4bash | C / rejected | "Timeouts, invalid syntax, and compile errors return status 1; surviving mutants return status 2" (lessons:388) | `curl` → text present (markup-split). **Match.** |
| S046 pbt-bibliography | C / rejected | "This bibliography aims to cover the literature on property-based testing (PBT) à la Haskell QuickCheck." (lessons:396) | `curl` → text present. **Match.** |
| S045 Elhage, two kinds of testing | B / queued | "This change didn't break anything that was previously known to work." (lessons:395) | `curl` → "previously known to work" in §Novelty. The source uses a curly apostrophe (`didn’t`); the Gate uses a straight one. Typographic only (L7). |

Tier-C rows are not sole support: `grep -rnE 'S029|S030|S046' corpus/knowledge corpus/README.md corpus/QUALITY.md` → no output.

### Check 5 — Discernment spot-check: see Section 5 table.

### Check 6 — New knowledge entries: PASS with defects M2/M3 (labels)

Both entries carry `source:`, `verified-at:`, `recheck:`. Recheck commands re-run:
- `mutation-score-semantics.md`: `curl -fsSL 'https://stryker-mutator.io/docs/…/mutant-states-and-metrics/' | grep -c 'detected / valid'` → `1`. Matches the recorded `(ran; 1)`.
- `witness-scoped-kill-verdict.md`: `curl -fsSL https://raw.githubusercontent.com/BWBama85/shmutant/main/README.md | grep -c 'not on its witness'` → `1`. Matches.

Claims versus sources:
- Stryker "detected = killed + timeout" and "Timeout counted as detected": confirmed in the fetched page.
- Stryker NodeStatus enum: `"enum": ["Killed", "Survived", "NoCoverage", "CompileError", "RuntimeError", "Timeout", "Ignored", "Pending"]` (S002 master, line 92). Matches the entry's "eight statuses".
- mutmut 3.8.0 CPU-limit fix: HISTORY.rst line 23 (`Fix mutants stopped by the CPU-time limit being reported as killed instead of timed out (#565)`), under the `3.8.0` heading (line 4 of the grep). Matches.
- S006 verdict grammar: all four pinned-README quotes match (pinned README lines 29–46).
- Six recomputed rows in `mutation-score-semantics.md`: re-derived from the table's `k/s/i`: 8/10, 8/10, 6/10, 4/10, 7/15, 7/10. Match the entry and `mutate-and-run.sh:84-92`.
- `witness-scoped-kill-verdict.md` numbers: `declared.tsv` sha256 `32241b02…fe9dd` = the declared digest. `js-kimi-census.results.tsv`: 8 KILLED, 2 SURVIVED, 0 inconclusive, and `case-labels.tsv` failing-label sets match the entry's table. Control log `control.out` is green.

### Check 7 — Credentials: PASS
`git -C <lane> diff 4eb4cf319..121696bf9 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1). A broader pattern without the alnum suffix (`op://|BEGIN … PRIVATE KEY|ghp_|AKIA|xox[baprs]-`) also returned nothing.

### Check 8 — Report: PASS
Required sections are present in order: Work performed; Landed changes; Before → after measurements; SHONEN; Sources & frontier; Mistakes; Trend verdicts; L0 questions; Integrator notes. The report cites the round commits `c7986cd` and `121696bf9`. No `[x]` appears. All four SHONEN boxes are `[~]` with pointers that resolve: `reports/round-1-calibration.md#box-1…box-4` (headings at lines 71/105/132/167), and `reports/round-1-kaika-coldread.md` (281 lines). LOG anchors resolve: `LOG.md:551` = "fleet round 1 closes"; `LOG.md:614` = "phase-2 corrections". `corpus/README.md:60-61` = the F1/F2 coverage rows. `PROVINCE.md:22` = the Core/Frontier/Adjacent section.

## 2. Per-axis recommended verdicts

| Axis | Lane self-verdict | Recommended | Evidence |
|---|---|---|---|
| depth | unchanged | **unchanged** (6 → 6) | Guardrail D, both revs |
| coverage | unchanged (unpinned) | **unchanged** | No coverage measurement; PROVINCE Core unchanged (append-only) |
| operability | unchanged | **unchanged** | `tools/` byte-unchanged; selftest 80/80 re-run in scratch copy |
| freshness | unchanged (unpinned) | **unchanged** | Stale ledger legs `tsukuroi`/`mado` remain stale (corpus/README.md:96-97); SKILL stale sentences flagged in README and lesson, not in SKILL (L4) |
| calibration | improved (candidate 8) | **improved: 0 → 8, pin 8.** Each of the four `[~]` is a restrained, durable-evidence assertion at its stated scope. Box 3 is the weakest (L5). No `[x]`. | Command C, both revs (Check 3). `[~]` lines are scope-bounded in `SHONEN.md:9-12` |
| adjacency | unchanged | **unchanged** | PROVINCE appended only; S030 rejected as adjacent-domain, reported not absorbed |

## 3. Trend verdicts

- **expansion — lane: improved → recommended: improved (agree).** Two admitted knowledge entries cover frontier F1/F2. Each cites `mined` rows and has its own coverage-map row (`corpus/README.md:60-61`). Unindexed 13 → 0 (Check 3). Caveat: the F1/F2 "held" labels overreach (M3).
- **quality — lane: improved → recommended: unchanged (disagree).** LEARNING defines `improved` as an entry *re-verified, deepened, or superseded*, with freshness shown. No pre-round entry was re-verified, deepened, or superseded. The 19 pre-round entries still have no `verified-at:` (README:91-95). The two stale legs remain stale (README:96-97). What did improve is the bar (QUALITY 6–10) and the index. Those are real, but they are not the quality trend's observable (M2).
- **discernment — lane: pending → recommended: improved, provisional (agree).** The sampled admit and reject both agree (Section 5). The sample is N=1 per side, which is the LEARNING minimum. Three self-verdict overstatements (M2, M3, L9) should be recorded as lesson items.

## 4. Defects by severity

**Medium (3)**
- **M1 — fleet-census `validate` is TZ-dependent. Outside the lane.** `sources-census.sh` `row_pass` `epoch()` (line 245) uses local `date -d`; `TODAY_S` (line 80) is UTC via gawk. On UTC−N hosts every row opened today fires E08. Repro: default host → exit 1 with 44 E08. `TZ=UTC` → `ok`, exit 0. Fix: compute `epoch()` as UTC (`TZ=UTC date -d`, or gawk `mktime(…,1)`). Owner: fleet-census.
- **M2 — `quality: improved` self-verdict is unsupported.** See Section 3. Recommended: `unchanged`, with the index fix and QUALITY 6–10 recorded as the bar change.
- **M3 — frontier status `held` overstated.** README:78 says F1 is `held (round 1)`, but the entry's own next move (schema validation) is `U` (validator unavailable). F2 (README:79) is `held`, but the entry states "for this pinned JS leg only". Recommended: `partly held (1 leg)` for both.

**Low (7)**
- **L1 — SCORECARD K1/K2 "Measured commit" is pointer text, not a hash.** K1 reads `round-1 kaika commit (hash in .ufo/reports/round-1/tameshi.md, fleet ledger)`. K2 reads `same`. The report has the hashes (`121696b`), so add them to SCORECARD.
- **L2 — SCORECARD K2 counting command names the superseded v1 census.** It says `bash .ufo/evidence/kaika-round-1/sources-census.sh`, which ER-K6 identifies as the run that printed 25 no-id-cite lines and was called clean. The capability row uses v2. Point the K2 row at `sources-census-v2.sh`.
- **L3 — capability rows.** The mutation runner and regression ledger enter this round with "first-working round" = historical round 3 / 7 / 10. AXES says rows enter through a round that demonstrates them. Record "entered fleet round 1" alongside the historical origin.
- **L4 — SKILL stale statuses.** The marks live in `corpus/README.md` Known gaps and lesson ER-K5. `SKILL.md:14-15` and `:133-135` carry no marker. The wording "marked rather than left silent" is accurate for the index only.
- **L5 — box 3 text is broader than its evidence.** The box text ("Instructions executable by an agent without oral context") is unchanged. The scope qualifier sits in the evidence line (`SHONEN.md:9-12`). The seat took the harness route, and the page directs sweep writes through it (`SKILL.snapshot.md:829–847`, cited in the cold-read report). Acceptable at the stated scope. Narrow the box text or split it in a later round.
- **L6 — `ground:` pointers resolve only in the fleet-ledger worktree.** The headers cite `tameshi-art.md §4`, a dossier outside the lane repo.
- **L7 — S045 quote apostrophe.** Gate uses `didn't`; source uses `didn’t`. Typographic only.

**Observed, not lane-owned, not touched:** a stray `bash: ` directory at the fleet root, and fleet-root strays noted in the report's Integrator notes.

**Methodological caveat (not a defect; recorded for discernment):** the witness split classifies D1 as killed-on-witness using the declared label `UNLISTED: a 19th lane file…`. That label is one of 16 failing labels for that mutant (`D1.out` FAIL lines: 16 + VERDICT), and the declared "green fixture → CLEAN" label recurs in D1 and D3. The rule is applied consistently. The result says the declared witnesses are present, not that they are specific. The entry's scope statement ("for this pinned JS leg only") already covers this.

**L9 — inconsistent rejection reason.** S029's rejection cites "8 commits and 0 stars at open" (SOURCES:40). Admitted S006 is "0 stars" too (SOURCES:17). The decisive reasons (no per-row verdict contract; S006 covers the ground) stand. Drop the popularity clause.

**L8 — process (not a defect).** The lesson `## Gate` spot-check reads `pending` by design (lessons:306-308). The non-author result belongs there and is the orchestrator's to append.

## 5. Discernment spot-check (LEARNING.md)

| # | Entry | Gate | Verdict | Reason |
|---|---|---|---|---|
| 1 | `corpus/knowledge/witness-scoped-kill-verdict.md` | admit | **agree** | Header trio present. Recheck runs to `1`. Declared digest `32241b02…fe9dd` matches `declared.tsv`. The 8 / 0 / 2 split reproduces from `results.tsv` and `case-labels.tsv`. Contamination is disclosed in E1 and the entry. Disagreement inside the entry: `held` (M3). |
| 2 | `corpus/knowledge/mutation-score-semantics.md` | admit | **agree** | Header trio present. Recheck runs to `1`. Six recomputed rows reproduce from the case tables. Quotes match fetched S001/S002/S004. Disagreement: `held` for F1 (M3). |
| 3 | `SOURCES` S029 mutate4bash (tier C) | reject | **agree** (with L9) | Tier C is lead-only per the contract. The decisive reason stands: no per-row verdict contract, and S006 covers the ground. Drop the star/commit clause. |
| 4 | `SOURCES` S046 pbt-bibliography (tier C, community) | reject | **agree** | Community is never tier A. Tier C is never sole support. No knowledge entry cites it. Flip condition is recorded. |
| 5 | Rule "count Timeout as a kill" (rejected in the Gate) | reject | **agree** | Stryker's policy (`killed + timeout`, confirmed in S001) is different. The contract needs red plus full count (SKILL.md:189-194). The entry records the flip condition. |

Spot-check result for the lesson: `agree` on 2 admits and 3 rejects (LEARNING minimum: 1 admit and 1 reject; the sample is small). Three self-verdict overstatements are open lesson items: M2, M3, L9.

## 6. Admit / reject recommendation

- **Admit:** K1 calibration (pin 8; no `[x]`), K2 sources-registry capability (after L1/L2 pointer fixes), `mutation-score-semantics.md`, `witness-scoped-kill-verdict.md`.
- **Reject:** none. Every rejected candidate in the Gate stands on its stated reason, with the L9 clause dropped.
- **Conditions before close:** M2 and M3 relabels, L1 and L2 pointer corrections, the orchestrator's spot-check entry appended to the lesson Gate. Fleet-census M1 goes to the census owner, not this lane.

## 7. Not done / verification gaps

- `--regression` not re-run (needs sibling repos at pinned revisions). Evidence reviewed: `h1b-regression.exit` = 0 and stdout:35 `REGRESSION: PASS (cases=6 passed=6; …)`.
- Cold-read and witness sweeps not re-executed (seat-level, sibling-dependent). Their recorded tables were reviewed; counts and hashes match.
- Own/gate rows S031–S037 were not re-opened (their pins are sibling-repo blobs). Sampled six external rows only.
- The fleet-census tool was run from its worktree as-is; no edits were made to it.
