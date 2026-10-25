# kotoba — STATE dossier (kaika W1, 2026-10-19)

Lane: `kotoba-shokunin`, repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Wave role: read-only STATE probe. No repo edits, no git mutation, no web research.
Only write made: this artifact.

Measurement pin: `git rev-parse HEAD` → `78ee57e5ed6fa409476dabea6bd8146ba37425dd`; `git rev-parse 'HEAD^{tree}'` → `07a170787d6a1ea3460fb0ae0661d2296b68a301`; `git log -1 --format='%ci'` → `2026-10-19 17:09:18 -0300`. `git status --porcelain=v1 | wc -l` → 0. All commands below were run at this pin, from the lane repo root unless stated.

Tool availability: `web_search` was **not** used (STATE dossier needs none). Gates were executed read-only (`PYTHONDONTWRITEBYTECODE=1 python3 -B`, `TMPDIR=/tmp`); none wrote into the repo.

---

## 1. Identity

| Field | Value | Command / pointer |
|---|---|---|
| Domain | prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity | `PROVINCE.md:3` |
| Rank | `shonen` | `python3 -c "import json;m=json.load(open('../MANIFEST.json'));print([r['rank'] for r in m['roster'] if r['id']=='kotoba'])"` → `['shonen']` |
| Minted | 2026-09-28 | same roster object, `"minted": "2026-09-28"` |
| Branch / HEAD | `master` / `78ee57e5ed6…` | `git branch --show-current`; `git rev-parse HEAD` |
| Working tree | clean | `git status --porcelain=v1 \| wc -l` → 0 |
| Lane ledger rows | 22 kotoba rows in `../MANIFEST.json` `rounds[]`; **1 admitted** (round 44) | `python3 -c "import json;m=json.load(open('../MANIFEST.json'));k=[x for x in m['rounds'] if isinstance(x,dict) and 'kotoba' in json.dumps(x.get('lane_rounds',{}))];print(len(k),[x['round'] for x in k if x.get('admitted') is True])"` → `22 [44]` |
| Ledger row types | 15 `closure`, 6 `closure-correction`, 1 `retroactive-closure` | same list, `collections.Counter(x.get('type') for x in k)` → `Counter({'closure': 15, 'closure-correction': 6, 'retroactive-closure': 1})` |

**Last closed round: 45 — REJECTED.** Fleet row (`MANIFEST.json`) verdict: `"depth": "improved-bounded (held-out hunt: 14 of 25 r41 doors now reject exit 2 on 13b6d791; … 11 still open; 9.5 not supported; depth holds 9)"`, `admitted: false`. Lane records agree: `LOG.md` § Round 45 and `.ufo/reports/round-45/kotoba.md` ("14 of the 25 r41-open doors now reject exit 2, 11 still exit 0"; 42 seats; C2/C3 verified). The laundering-class arc is the subject of rounds 37–46.

**Round 46: attempted, WIP, not closed — this is the one place the fleet ledger hint ("max recorded 45") under-describes the lane.**
- Committed as `36ab0d3` "round 46 (WIP): comparator hardening C1/C2/C3 candidate — floors 255->328, scope-file contract tightened, 13 new fixture suites", merged by `78ee57e`.
- No lane report: `test -e .ufo/reports/round-46/kotoba.md` → **absent** (`.ufo/reports/` holds round-20…round-45 only; `ls .ufo/reports | tail`).
- No fleet ledger row: `grep -c 'round 46' ../MANIFEST.json` → **0**.
- The only round-46 document is `.ufo/round-46/drafts-report-skeleton.md`, whose landing cells are `[PENDING]` and whose C3 verdict is `unproven / not improved` (line 38).
- Claims file `.ufo/round-46/claims.json`: `round 46`, `seats 40`, axes depth (9, owned) / operability (8.5) / calibration (8.5); provider `openai-codex/gpt-6-luna-max` (devin fallback recorded).

**Next round number:** 46 if the round is resumed/closed with its existing claims; 47 if r46 is closed as an attempted rejection and a fresh round opens. The fleet ledger cannot be appended from this wave either way. The lane's own next-round plan is `.ufo/round-46/claims.json`, not `SCORECARD.md` (see §2).

---

## 2. Axes

Scores are SCORECARD's, read verbatim; every row carries its own evidence pointer.

| Axis | Score | Owned? | Evidence pointer (SCORECARD line) |
|---|---:|---|---|
| depth | 9 | yes | r45 held-out hunt: 14/25 doors closed, 11 open; 9.5 not supported (`SCORECARD.md:28`) |
| consistency (calibration sub-axis) | 10 | yes (declared sub-axis) | r15: two own box annotations corrected, disagreements recorded not averaged (`SCORECARD.md:29`) |
| coverage | 8.5 — was 8.0 | advisory | r15 re-measure of r14's opencode extraction (`SCORECARD.md:30`) |
| operability | 8.5 — was 8.0 | advisory | r45: `expected`/`expected_value` alias conflict + non-string status closed (`SCORECARD.md:31`) |
| freshness | 8 | advisory | r43: census doc reconciled post-r44 (`SCORECARD.md:32`) |
| calibration | 8.5 — was 8.0 | advisory | r46 candidate: scoped-out reason/evidence/probe-target drift reject `exit 2` (`SCORECARD.md:33`) |
| adjacency | 8.0 — was 7.5 | advisory | r26: routing-replay guard reads JSON pin; ack 0/5 (`SCORECARD.md:34`) |

**Lowest non-retired axis — two readings, both recorded because the protocol does not define "owns" against advisory axes.**
- *Owned-only reading* (the lane's own saturation note restricts the nudge to owned axes, `SCORECARD.md:253-264`): lowest is **depth 9** (consistency 10).
- *All-axes reading*: lowest is **freshness 8.0**, tied with **adjacency 8.0**; nothing is retired (`## retired`: "None", `SCORECARD.md:113-115`).
- Recommendation: a freshness claim also restores the red gates (§5), so it satisfies either reading without touching depth's exhausted claim.

**Saturation.** Line `10.0` on owned axes — "Saturation line: 10.0 on the owned axes", `SCORECARD.md:232`. Nudge **dormant** (depth 9 < 10), `SCORECARD.md:264`. Stagnation window N = 3; last refresh is the **round-27** text (`SCORECARD.md:264`), while the capabilities table has had **no row since round 29** (`grep -c` of capability data rows → 2: substrate-pin guard r23, assertion-floor guard r29). The window field is therefore stale by its own definition (rounds 30+ entered no row); it does not fire only because the nudge's first condition (all owned axes ≥ line) is false.

**Capabilities count: 2** (`awk` over `## Capabilities` rows matching `substrate`/`assertion` → 2; header excluded).

**SCORECARD `planned`.** The section is a second log, not a plan: **24** paragraphs match `^\*\*Round [0-9]+ completed` (`grep -c` → 24) plus **6** `**Next: round N**` lines (`grep -cE '^\*\*Next: round' SCORECARD.md` → 6; lines 72, 78, 82, 90, 94, 98), out of chronological order (r40 at line 72, r42 at 78, r41 at 82, r45 at 90, r46 at 94, r44 at 98). Its last entry for the current round is r46; no r47 claims are pre-registered anywhere. The real next-round claims live in `.ufo/round-46/claims.json`.

---

## 3. Corpus

| Metric | Count | Command |
|---|---:|---|
| `corpus/knowledge/` files | 35 (34 `.md` + 1 `.json` companion) | `ls corpus/knowledge \| wc -l` → 35; `ls corpus/knowledge/*.md \| wc -l` → 34 |
| `corpus/lessons/` files | 19 | `ls corpus/lessons/*.md \| wc -l` |
| Coverage-map data rows | 51 | `awk '/^\| Area \| File \| Basis \|/{f=1;next} f&&/^\|---/{next} f&&/^\|/{c++;next} f&&!/^\|/{exit} END{print c}' corpus/README.md` |
| `## Frontier` rows | **0** | `grep -c 'Frontier' corpus/README.md` → 0 |
| `corpus/QUALITY.md` | **absent** | `test -e corpus/QUALITY.md; echo $?` → 1 |
| Entries missing any of `source:`/`verified-at:`/`recheck:` | **32 of 34** | `for f in corpus/knowledge/*.md; do grep -qE '^[[:space:]]*source:' "$f" && grep -qE '^[[:space:]]*verified-at:' "$f" && grep -qE '^[[:space:]]*recheck:' "$f" \|\| echo "$f"; done \| wc -l` → 32 |
| Each metadata field, files carrying it | `source:` 2, `verified-at:` 2, `recheck:` 2 | `grep -lE '^[[:space:]]*source:' corpus/knowledge/*.md \| wc -l` → 2 (same for the other two) |
| Lessons with `## Gate` | **2 of 19** | `grep -l '^## Gate' corpus/lessons/*.md \| wc -l` → 2 |
| Corpus Markdown files seen by the gate | 54 | `python3 -B verifiers/verify_corpus_integrity.py` → "73 FILE-column patterns over 54 md files" |

The 2 conforming knowledge entries are `harness-independent-round41-census.md` and `sibling-citation-routing-round16.md`; the other 32 open with prose ("Sourced 2026-09-28" or "Falsifiable claims …, observed …") and carry no machine-readable `source:`/`verified-at:`/`recheck:` block — a direct violation of `CORPUS.md:17` ("Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`").

**Overdue `recheck:`.** No entry carries a date-valued recheck (only two procedural rechecks exist), so "overdue by date" is unmeasurable for 32/34. The one recheck that names a runner path **is dead**: `harness-independent-round41-census.md:3` instructs `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py`, and `test -e .ufo/round-45/drafts` → absent (`ls .ufo/round-45/drafts` → "No such file or directory"). The live checklist gate fails on exactly this citation (`LOG.md:2111`), see §5.

**Corpus gates at HEAD (live):**
- `python3 -B verifiers/verify_corpus_integrity.py` → `exit 0`, `9/9 checks pass`; `tracked=55 unindexed=0 stale=0 missing=0`; `report_dead=0/38`, `commit_total=27`, `unresolvable=0 nonhash=0`.
- `python3 -B verifiers/verify_corpus_independent.py --json` → `exit 0`, same counts, `PASS`/`INFO` rows.
- Note: `verifiers/corpus-baseline.json` top-level `measured_against.head` is still `d85982d`, `as_of 2026-09-29` (`head -6`), although the file was last edited at `d374d3b` (2026-10-19) — the per-round refresh notes inside are current, the headline provenance is stale.

**LOG completeness:** distinct round numbers 0–46 appear in `LOG.md` (`grep -oiE 'round [0-9]+' LOG.md | tr A-Z a-z | sed 's/round //' | sort -n | uniq`), **except 8 and 42** (`for i in $(seq 1 46); do grep -qiE "round $i([^0-9]|$)" LOG.md || echo $i; done` → `8 42`). Round 8 is admitted as never written in `corpus/README.md:49` ("LOG.md round-8 entry (never written — see the lesson)"); round 42 has **no** LOG entry — its only record is the SCORECARD `planned` paragraph and the `MANIFEST.json` row.

---

## 4. Mistakes (mined)

Legend: "captured?" means an existing `corpus/QUALITY.md` criterion or `SKILL.md` rule already covers the class. `QUALITY.md` does not exist (`test -e` → 1), so "QUALITY" is always ✗; the sweep therefore tests `SKILL.md` and the anti-pattern table only.

Sweep commands used for every row: `grep -ci '<term>' SKILL.md`, `grep -ci '<term>' corpus/knowledge/fail-closed-and-anti-patterns.md`, and `grep -l recheck verifiers/*.py` (no output — no instrument reads a `recheck:` line).

| # | Class | Evidence pointer | Captured? | Proposed criterion (if not) |
|---|---|---|---|---|
| M1 | **Payload closed, class survives** (laundering arc) — r39 F-2, r40 F-3', r43 `heldout-expected-only-full-copy`, r45 doors outside the census | `LOG.md` § Round 39/40/43/45; `MANIFEST.json` rows 39–45; r45 report "11 still exit 0" | ✗ — `grep -ci 'held-out' SKILL.md` → 0; `grep -ci 'launder' …` → 1 (prose only, no rule) | "A closure claim names the *class* and the held-out hunt that failed to find a surviving shape; closing the declared payload is `improved-bounded`, not closed." |
| M2 | **Finite census sold as exhaustive** — r41 "complete-census" condition; r46 C1 ruling "not demonstrably bounded", duplicate-ID/status still exit 0 on both frozen and candidate | `SCORECARD.md:80` (r41 calibration annotation); `.ufo/round-46/scouts/C1.md` (via `LOG.md:2228`) | ✗ — same sweep, 'census' appears 4× in SKILL.md but all are corpus/render censuses | "An exhaustive claim names the generator of the door space and the seed; a saved 46-arm set is a measurement, not a bound." |
| M3 | **Record contradicts the tree it describes** — SCORECARD calls the r46 comparator "uncommitted candidate" while `git show HEAD:verifiers/compare_harness_independent.py \| sha256sum` = `ccf41c23…` (committed at `36ab0d3`) | `SCORECARD.md:33` vs HEAD blob hash | ✗ — `grep -ci 'uncommitted' SKILL.md` → 0 | "Every record names the commit that contains the bytes it describes; 'uncommitted' is a claim a reader verifies with `git show <ref>:<path>`." |
| M4 | **Dead recheck/source command** — r45 claims "recheck runs"; runner pruned; live gate fails | r45 report line 29 (`C3` row: "recheck runs"); `LOG.md:2111` "each exited 2 because the referenced runners are absent"; checklist FAIL | ✗ — `grep -l recheck verifiers/*.py` → no output (no instrument reads `recheck:`); `trigger.citation_resolves` scans SKILL.md, `governance.citation_resolves` scans LOG/SCORECARD, neither scans knowledge recheck lines | Extend an instrument to resolve **every** `recheck:` command in `corpus/knowledge/*.md`; pruning a runner is then a red gate, not a silent dead citation. |
| M5 | **Fix that harms** — r38 C2 closed two residuals but introduced a None-path crash | `SCORECARD.md` move-log row 38: "fix introduced a None-path crash + malformed-field arm survives: C2 fails as declared (harm)" | Partly — `AXES.md` "no axis is harmed" rule; no SKILL row | "A fix ships its own regression arm before the claim is scored; a new crash class in the fix is harm, not partial progress." |
| M6 | **Seat denominator overstated** — r40 entry says `41/41 seats`; the frozen claims file declares `seats: 40`, 41 files are scout fragments | `SCORECARD.md:80` (r41 annotation, second copy `:222`): "The 41 files are committed scout fragments, not proof of 41 declared/complete seats absent an amended dispatch roster" | Partly — "a count carries its command" rule; the correction was appended but the original line stands | "A seat count is `completed/declared` from the claims file; a scout-file count is a different number and is labelled so." |
| M7 | **SHONEN canonical-form drift** — 50 lines for a 4-box template; multi-line notes where PROTOCOL allows one evidence line per box; all four `[~]`, no `[x]` | `SHONEN.md` (4 boxes at lines 5, 16, 22, 41; `wc -l` → 50); `PROTOCOL.md:417` canonical form | ✗ as a lane rule; carried as standing debt ("SHONEN form", `SCORECARD.md:94`) | Regenerate `SHONEN.md` byte-for-byte from the template before any next-round claim; marks live one evidence line. |
| M8 | **Fleet-root identity contamination** — fleet `LOG.md` and `SCORECARD.md` are kotoba lane files, committed into the main repo | `head -1 ../LOG.md` → `# kotoba-shokunin — Iteration Log`; `head -1 ../SCORECARD.md` → `# kotoba-shokunin — Scorecard`; `grep -c kotoba ../SCORECARD.md` → 38; last commit `31baf5c` ("fleet backlog commit … uncommitted artifact sweep") | ✗ — protocol-owned files; r42 flagged it pre-commit, now committed | Cross-domain: fleet-level guard that the main-repo LOG/SCORECARD first line names the fleet/protocol lane, not a child lane. Route to integrator; do not edit from this lane. |
| M9 | **Gate regressions found one round late** — omp rebuilt 18.12.3 under a green r45 battery | r45 report: "gates … green at landing … surfaces 7/7; pins 3/3; checklist 10×PASS"; live today: 5/7, 1/3, 9/10 (§5); `LOG.md` S2 records the 18.12.3 string diff | ✗ — the pin guard detects, but nothing schedules the re-derivation | "A substrate rebuild makes freshness red until the extraction is re-derived and re-pinned; 'no rebaseline' is an open debt, not a pass." |
| M10 | **README frontmatter-marker leak** — lane front door shows the folded-scalar marker | `README.md:6` → `**Domain:** >`; `wc -l README.md` → 14 (still the mint seed, tells readers SKILL.md is absent on shonen lanes while SKILL.md is 521 lines) | ✗ — `governance.citation_resolves` covers LOG/SCORECARD only, not README | Lint README header fields (reject a bare block-scalar indicator `>`, `>-` or `\|` as the value; Domain equals PROVINCE domain) — already proposed in `considerthese/2026-10-19.md` §4, never landed. |
| M11 | **Honest stops recorded correctly** (not defects) — r19 recensus (no scalar), r20 dispatch-blocked (all axes unchanged), r42 no-dispatch breather (`admitted: null`, notes "no swarm, no axis move") | `LOG.md` § Round 19/20; `MANIFEST.json` row 42 | n/a | Keep; these are the pattern to preserve. |
| M12 | **Non-author gate disagreements** — aggregator audits r1/4/5/6/9; box-3 cold run `[~]` with B1/B2; r13 revert of `[x]` under PROTOCOL:65; r15 two own annotations misstated | `corpus/lessons/round-{1,4,5,6,9}-aggregator-*.md`, `round-8-aggregator-box3-coldrun.md`; `SHONEN.md:7-15` | Partly — the attribution rule (PROTOCOL:65) exists and was applied | Keep the attribution discipline; the remaining gap is that no external witness has re-run the *current* box map (8 executed / 0 delegated / 33 unexecuted, `corpus/README.md:64`). |
| M13 | **Frontmatter gate is structural, not semantic** — the gate says so itself; a strict loader can reject a file this box PASSes. Peer `W1ArtKotoba` reports strict Psych `safe_load` fails 12/18 sibling `*-shokunin/SKILL.md` frontmatters (plain-scalar `description:` containing `': '`), unopened by me. kotoba's own frontmatter **passes** Psych, but its description carries `<skills>` (peer opened https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices § "Skill structure" Note: description "Cannot contain XML tags"; rule not opened by me) | `verifiers/verify_skill_checklist.py:67-76` ("Limit: a structural parse, not semantic YAML validation"), repeated `:194`; `ruby -ryaml -e 'YAML.safe_load(File.read("/tmp/kotoba-fm.txt"))'` → `safe_load OK keys=["description", "name"]`, `desc has <skills>: true`; `grep -n '<skills>' SKILL.md` → line 14 (inside frontmatter) | ✗ — no semantic check, and no XML-tag rule (`grep -cin 'xml' verifiers/verify_skill_checklist.py` → 2, both cmark-oracle comments) | Add a `trigger.frontmatter_semantic` box using the loader's own parser plus a description XML-tag rule; keep the structural box as the fast pre-check. |

---

## 5. Contract defects

**Missing required files / surfaces**
1. `corpus/QUALITY.md` — required by `CORPUS.md:12` ("`QUALITY.md` — the shokunin's own quality bar") and `LEARNING.md:13`; `test -e corpus/QUALITY.md` → exit 1. Consequence: no lane-specific admission bar; every "does a rule capture this?" answer in §4 is structurally ✗.
2. `corpus/README.md` `## Frontier` — required by `LEARNING.md:59`; `grep -c 'Frontier' corpus/README.md` → 0. The coverage map has a `## Known gaps` section but no frontier list.
3. `PROVINCE.md` Core / Frontier / Adjacent — required by `LEARNING.md:68`; the file is 6 lines (`wc -l` → 6), seed form: domain, owns, refuses. No declared work surfaces; no frontier inventory ("`PROVINCE.md` carries no frontier inventory", `SCORECARD.md:260`).

**Identity / seed drift**
4. `README.md` is the mint seed: `**Domain:** >` at line 6 (the YAML folded-scalar marker leaked into a public header) and lines 12–14 still say SKILL.md is "absent on lanes still in shonen seed form" — the lane's SKILL.md is 521 lines / 34111 bytes (`wc -l -c`).
5. Rank remains `shonen`; `SHONEN.md` all four boxes `[~]`, no `[x]`; the only non-author verdict is the aggregator's round-8 box-3 `[~]` (B1/B2 fixed in r13, never re-run by a non-author).

**Bloat (sizes with commands)**
6. `LOG.md` — 2298 lines / 418078 bytes (`wc -lc LOG.md`).
7. `SCORECARD.md` — 264 lines / 108084 bytes (`wc -lc SCORECARD.md`); its `planned` section carries 24 completed-round paragraphs + 6 Next lines (§2), duplicating LOG.
8. `.ufo/` — 122 MB, **9527 tracked files** (`du -sh .ufo`; `git ls-files .ufo | wc -l`), of which `.ufo/round-46/` alone is 52 MB / **8050 tracked files** (`du -sh .ufo/round-46`; `git ls-files .ufo/round-46 | wc -l`) versus `.ufo/round-45` at 403 tracked files. The WIP round's evidence bundle is 20× the previous round's.
9. Total tracked files: 9892 (`git ls-files | wc -l`).

**Dead pointers**
10. `LOG.md:2111` cites `.ufo/round-45/drafts/v10/post-r44-hunt.py`; the path does not exist (round-45 drafts pruned; `ls .ufo/round-45/drafts` → No such file). This is the only live checklist failure: `governance.citation_resolves` FAIL, 9 PASS / 1 FAIL, `exit 1`.
11. The same dead path is `harness-independent-round41-census.md:3`'s `recheck:` command — a corpus entry whose freshness cannot be rechecked.
12. `verifiers/corpus-baseline.json` headline `measured_against.head` = `d85982d` / `as_of 2026-09-29` while last edited `d374d3b` (2026-10-19) — stale provenance, green counts.
13. U1 also records a doc/command mismatch: the R37 §6 null-echo command "exited 2 (doc expects exit 1)" (`LOG.md:2111` block, U1 entry).

**Live gate battery at HEAD (all run today, read-only)**
| Gate | Command | Exit | Detail |
|---|---|---:|---|
| corpus integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 0 | `9/9 checks pass`; tracked=55, unindexed=0, report_dead=0/38, commit_total=27 |
| corpus independent | `python3 -B verifiers/verify_corpus_independent.py --json` | 0 | all PASS/INFO rows |
| skill checklist | `python3 -B verifiers/verify_skill_checklist.py --json` | 1 | 9 PASS / 1 FAIL — `governance.citation_resolves` at `LOG.md:2111` |
| surfaces | `python3 -B verifiers/verify_surfaces.py --json` | 1 | 5 PASS / 2 FAIL — `surfaces.literal_present` ("8 loader literal(s) not verifiable"), `surfaces.no_uncovered_class` ("0 loader class(es) extracted … baseline declares 8") |
| substrate pins | `python3 -B verifiers/check_substrate_pins.py` | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`; opencode pin PASS |
| assertion floors | not rerun (needs full self-test battery; r46 records 9/9 at `ccf41c23`) | — | r46 evidence: `10/150/91/87/1597/62/104/328/150` |

The omp drift is not a mystery: S2 recorded the installed binary moved to `omp/18.12.3` with fresh strings differing from the saved 18.12.2 dump (`LOG.md` S2 entry), and I1 recorded "surfaces 5/7 with OMP extraction failures; pins 1/3 with OMP SHA/mtime drift and no rebaseline" (`LOG.md` I1 entry). What is missing is the **re-derivation + re-pin** round, not the observation.

**Uncommitted changes / stray artifacts**
14. `git status --porcelain=v1` → 0 lines (clean). Ignored entries: 7 (`git status --porcelain --ignored=matching | wc -l` → 7): `.ufo/interactive-sessions/`, `verifiers/__pycache__/`, and `.ufo/round-{37,38,41,46}/…/__pycache__/`. No tracked `__pycache__` (`git ls-files | grep -E '__pycache__|\.pyc$' | wc -l` → 0). Nothing to report as a user change.
15. `considerthese/2026-10-19.md` (8.0 KB) and `plans/` (12 KB, 2 files) are lane-local documents outside `corpus/`; the corpus gate passes (they are not index subjects), but `considerthese/` is a new tracked Markdown class the index does not account for.

**Report-location split**
16. Lane reports for rounds 20–45 exist only in the lane repo (`.ufo/reports/round-N/kotoba.md`, 25 dirs); at the fleet root, `ls ../.ufo/reports/round-*/kotoba.md | wc -l` → **17** (older rounds), and `../.ufo/reports/round-45` is absent. `PROTOCOL.md:453` places the lane report at `.ufo/reports/round-<N>/<id>.md`; the two locations have diverged, so a reader following the protocol text finds no report for the last two rounds.

**Own frontmatter violates the loader-doc rule (peer-reported rule; local observation)**
17. `SKILL.md`'s frontmatter `description` contains the literal `<skills>` token (line 14). Peer `W1ArtKotoba` opened https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices § "Skill structure" (Note: description "Cannot contain XML tags"; Anthropic-specific — the agentskills.io spec has no such rule). The rule was not opened by me (STATE scope, no web), so the *consequence* is unverified; the *presence* is measured. The lane's own frontmatter box cannot see it — it is a structural parse with no tag rule (`verifiers/verify_skill_checklist.py:67-76,194`; `grep -cin 'xml'` → 2 cmark-oracle comments only). This is the lane's domain failing on its own front door, the same class as the README marker leak (M10).

---

## 6. Conflicts for the canonical judge (verbatim)

1. **Committed vs "uncommitted".** `SCORECARD.md:33`: "C3's scoped-out metadata drift classes verified on the **uncommitted candidate**". Against it: `git show HEAD:verifiers/compare_harness_independent.py | sha256sum` → `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d`, i.e. the described bytes are committed at `36ab0d3`, and worktree bytes are identical.
2. **Two verdicts for the same C3 work.** `.ufo/round-46/drafts-report-skeleton.md:38`: "Disposition and calibration verdict: **unproven / not improved**; calibration remains 8.5." vs `SCORECARD.md:33`: "fixtures now reject those changes exit 2 as `scope reason drift`, `scope evidence drift`, and `scope probe target drift`" (verified on the candidate). Later LOG entries (P4, Y1, B2) side with the candidate but explicitly bound the result and withhold whole-round closure.
3. **"Recheck runs" vs a dead runner.** `.ufo/reports/round-45/kotoba.md:29`: C3 after-state "**reconciled to post-r44** (append-only closed-at-sha marks; **recheck runs**)". Against it: `LOG.md:2111` "each exited 2 because the referenced runners are absent"; live `verify_skill_checklist.py` FAIL at that citation. The r45 calibration row still reads verified at 8.5.
4. **Ledger vs lane round numbering.** `../MANIFEST.json` has no kotoba row above 45 (`grep -c '"kotoba": 46' ../MANIFEST.json` → 0); the lane has committed round-46 WIP work (`36ab0d3`) and 47 LOG entries headed "Round 46" (`grep -cE '^## .*Round 46' LOG.md` → 47). Round 46 is neither admitted nor rejected in the canonical ledger.
5. **Fleet-root files vs PROTOCOL ownership.** Fleet `LOG.md`/`SCORECARD.md` are kotoba lane documents (`head -1` both "kotoba-shokunin"; `grep -c kotoba ../SCORECARD.md` → 38), committed at `31baf5c`. PROTOCOL: only `protocol`/`aggregator` keep root `SCORECARD.md`/`LOG.md` (line 453-454). No ruling is on record; r42 flagged it before the commit.
6. **r46 C1 census ruling vs round state.** `.ufo/round-46/scouts/C1.md` (via `LOG.md:2228`): "the broader census boundary **not demonstrably bounded**"; duplicate-ID/status ordering still exits 0 on frozen and candidate. This coexists with r46's C1 registered after-condition in `claims.json` (planted-CWD arm exit 2, honest join 24/24) — the registered claim is narrower than the census question the round also asked.

---

## 7. Proposed round (for wave 2 / lane r47 — or r46-resume)

Lowest non-retired axis: freshness 8.0 (all-axes) / depth 9 (owned-only). The proposal takes freshness, because it satisfies both readings via the gate battery and does not extend depth's 10-round arc. All three claims are distinct axes; claim 1 is the lowest-axis claim.

### C1 — freshness 8.0: "Re-derive, then re-pin the omp substrate"
- **Before (measured today):** surfaces 5/7 exit 1 (`surfaces.literal_present`: 8 loader literals unverifiable; `surfaces.no_uncovered_class`: 0 extracted of 8 declared); pins 1/3 exit 1 (`omp_binary_sha256`, `omp_binary_mtime`); checklist 9/10 exit 1 (dead r45 runner).
- **After target:** extract the 8 omp loader-group literals and their call shapes from the installed `omp/18.12.3` (the S2-observed rebuild), record version + sha256 + the extraction rules, **only then** re-pin `verifiers/baseline.json`/pins; replace the census `recheck:` with a live command (or restore the pruned runner). Gates: surfaces 7/7 exit 0; pins 3/3 exit 0; checklist 10/10 exit 0.
- **Counting commands:** the three gate invocations above, before and after, with exit codes; plus `git status --porcelain=v1` at each boundary and the new pin values.
- **Anti-laundering clause:** a re-pin without re-derivation is not a freshness move — the pin guard exists to catch silent substrate movement, and the archive's own anti-pattern table says a warning without a signature teaches nothing (`SKILL.md:349-355`). The claim fails as declared if the extractor is widened to whatever the new dump happens to contain without naming the call shape (the r21 vacuity class).
- **Score:** 8 → 8.5 requires a non-author re-run (rubric band 8.5); without it the score holds at 8 with the gates green.

### C2 — calibration / consistency sub-axis 8.5: "Close the r46 record honestly"
- **Before:** no round-46 report (`test -e .ufo/reports/round-46/kotoba.md` → 1); no ledger row (`grep -c 'round 46' ../MANIFEST.json` → 0); SCORECARD says "uncommitted candidate" for committed bytes (`grep -c 'uncommitted candidate' SCORECARD.md` → 1, line 33); scaffold and SCORECARD disagree on C3 (§6.2).
- **After target:** the report lands last with per-claim landed/verdict cells and the commit hashes; the integrator appends the `MANIFEST.json` row; SCORECARD's wording is reconciled in an append-only erratum that names `36ab0d3` and resolves the C3 conflict one way with evidence; the dead recheck citation is fixed by C1.
- **Counting commands:** `grep -c 'uncommitted candidate' SCORECARD.md` 1 → 0; `test -e .ufo/reports/round-46/kotoba.md; echo $?` 1 → 0; `grep -c '"kotoba": 46' ../MANIFEST.json` 0 → 1 (integrator action); `python3 -B verifiers/verify_skill_checklist.py --json` exit 1 → 0.
- **Why it is a claim, not bookkeeping:** the r46 work already moved operability/calibration evidence; leaving the record split means two authoritative artifacts disagree about whether C3 is verified — the lane's own calibration sub-axis is exactly "a claim is scored on whether it says what it can support" (`SCORECARD.md:12-14`).

### C3 — adjacency 8.0 (optional, exploratory): "Re-route the three owner packets"
- **Before:** r16adj routes `r16adj-route-{kake,kasegi,kumitate}` unacknowledged, live ack 0/5 on every surface (`SCORECARD.md:34`, r22 measure; delta 0 at r26).
- **After:** either an acknowledgment appears or a ruling is recorded at L0; the measure is re-run with the same command and the delta reported verbatim.
- **Verification:** an exploratory claim verifies only as `unprovable-but-better` with a named **non-author** reviewer on record (`AXES.md` § Working the axes); if no acknowledgment and no ruling arrives, the honest verdict is `unchanged` and the claim is not counted.
- **Alternative if the lane insists on depth:** close the duplicate-ID/status ordering door that r46's own C1 ruling says still exits 0 on both frozen and candidate — but depth is not the lowest axis and the round already carries the open r46 depth claim; it would duplicate, not advance.

**Serving artifacts (wave-2 lane writes):**
- C1 → new `corpus/knowledge/substrate-repin-round47.md` (version + sha256 + extraction rules + re-pin gate). `SOURCES.md` rows it needs: installed omp 18.12.3 binary (kind `tool`, tier A, `recheck: on-release`); `verifiers/verify_surfaces.py` + baseline (kind `code`, tier A); `PROTOCOL.md` §Gate standard (kind `spec`, tier A).
- C2 → new `corpus/knowledge/round46-record-reconciliation.md`. `SOURCES.md` rows: `PROTOCOL.md` §File contract/§Gate standard (spec, A); `MANIFEST.json` (dataset, A).
- C3 → new `corpus/knowledge/adjacency-ack-round47.md`. `SOURCES.md` row: `.ufo/l0-questions.md` (own-work, A).
- New corpus entries must open with `source:`/`verified-at:`/`recheck:` and be indexed in `corpus/README.md`; the corpus gate will fail otherwise (`tracked=55` baseline).

---

## 8. Artifacts and limits

- Artifact: `local://kaika-w1-kotoba-state.md` (this file).
- Lane evidence read: `PROVINCE.md`, `README.md`, `AGENTS.md`, `SHONEN.md`, `SKILL.md`, `SCORECARD.md`, `LOG.md`, `corpus/README.md`, `corpus/knowledge/*` (list + metadata sweep), `corpus/lessons/*` (list + `## Gate` sweep), `.ufo/round-46/claims.json`, `.ufo/round-46/drafts-report-skeleton.md`, `.ufo/reports/round-45/kotoba.md`, `verifiers/corpus-baseline.json`, `verifiers/floors-registry.json` (head), `considerthese/2026-10-19.md`, `plans/` (listing).
- Fleet evidence read: `MANIFEST.json` (roster + kotoba rows), `MISSION.md` (kotoba row), `AXES.md`, `PROTOCOL.md` (§Gate standard, §File contract, lane-report rule), `CORPUS.md`, `LEARNING.md`, `.ufo/l0-questions.md` (tail), fleet-root `LOG.md`/`SCORECARD.md` (identity), `.ufo/reports/` layout.
- **Not measured:** the comparator join, floors guard, and full self-test battery (floors registry `10/150/91/87/1597/62/104/328/150`) were not re-run (r46 evidence covers them at `ccf41c23`); no web research (STATE scope); no source edits; no git operations. Gate runs are at one pin only; the substrate can move under the lane again (as it did at r45→r46).
- **Peer-supplied, not reproduced here:** the strict-YAML sweep over 18 sibling `SKILL.md` files (Ruby Psych `safe_load`; the peer confirms no Python version exists) and the Claude XML-tag rule (peer-opened URL above) come from `W1ArtKotoba`'s messages; my local checks cover kotoba only (Ruby Psych parses its frontmatter; the `<skills>` token is present).
- **Read-only compliance:** the only write is this artifact; no repo file, git index, ref, or sibling repository was touched.
