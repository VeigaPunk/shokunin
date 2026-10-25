# kaika W1 — STATE dossier — lane `kake` (web properties & publishing)

Date: 2026-10-19. Repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (read-only).
Shape: STATE (lane-internal, context §Dossier shapes). `web_search` was not needed and
was not used. No gate was re-run to decorate this report; every measured number below is
either a filesystem count taken in this session or a value recorded by the lane with its
own command and pointer.

Wave-2 readers: this is the STATE half only. External current-art research for `kake`
lives in the ART scout's `local://kaika-w1-kake-art.md`; no `SOURCES.md` rows exist in
this artifact.

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| id / name | `kake` / `kake-shokunin` | `MANIFEST.json` roster row (`repo: kake-shokunin`) |
| Domain | web properties & publishing — `ds4cc.com`, `kimi.page/pro` mirrors, Pages deploys | `PROVINCE.md:3` |
| Rank | `shonen` (minted 2026-09-28) | `MANIFEST.json` roster row |
| Branch / HEAD | `master` / `cb807bc8d8bc` (2026-10-17T00:29:01-03:00) | `git branch --show-current`; `git rev-parse --short=12 HEAD`; `git log -1` |
| Commits | 37 | `git rev-list --count HEAD` |
| Working tree | clean — 0 entries | `git status --porcelain=v1 \| wc -l` |
| Remote | `https://github.com/VeigaPunk/kake-shokunin.git` | `git remote -v` |
| Required files | `SKILL.md`, `PROVINCE.md`, `LOG.md`, `SHONEN.md`, `AGENTS.md`, `SCORECARD.md`, `corpus/` all present | `git ls-files` |
| `MINT.md` | absent; round-20 LOG records it as absent inventory, and it is not in `PROTOCOL.md` §File contract | `ls MINT.md` → No such file; `LOG.md:481` |

### Last round with evidence

**Last admitted round: 19.** The fleet ledger hint ("max recorded round 19") is verified:

- Fleet ledger: the maximum `lane_rounds.kake` across all `MANIFEST.json` `rounds[]`
  entries is **19** — 10 entries carry a `kake` lane round; the last is the 2026-10-14
  twelve-hour-program closure (`lane_rounds: {"kagi":19,"kake":19,"kama":4,"kasegi":20,"kengaku":16,"kotoba":19}`).
  Command: `python3 -c "import json;m=json.load(open('MANIFEST.json'));print(max(r['lane_rounds']['kake'] for r in m['rounds'] if 'kake' in (r.get('lane_rounds') or {})))"` → `19`.
- Entries naming `kake` in `lane_rounds` after 2026-10-14: **0** — same script with
  `... and str(r.get('date',''))>'2026-10-14'` → `0`.
- Lane record: `LOG.md:433` `## 19 — re-census round (freshness axis-move)`;
  `SCORECARD.md:70` move-log row 19; fleet report `.ufo/reports/round-19/kake.md`
  (3,211 B — `wc -c`); lane lesson `corpus/lessons/round-19-recensus.md`.

### Round 20 — recorded attempt, not admission

The lane records a **round-20 attempt that is blocked/unadmitted**, so "max recorded 19"
and "lane is at 20" are both true at different scopes:

- `SCORECARD.md:90` `## Round 20 attempt — local verdicts, not round admission`;
  `SCORECARD.md:17-19`: "**Round 20 remains unadmitted.** Freshness is the chosen LIVE
  axis (10/10 tie with operability); no numeric rating or verified-round count advances."
- `LOG.md:470,491,544,568` — round-20 reconciliation, local proof, shape-only erratum,
  blocked handoff. `LOG.md:589` — 2026-10-16 SCORECARD-conformance scaffold commit.
- Lane-local report `.ufo/reports/round-20/kake.md` (10,341 B — `wc -c`), tracked.
- `.ufo/round-20/continuation.json`: `"actualRound": 20`, `"roundComplete": false`,
  `"verifiedRoundsAdded": 0`, `"retiredDriverLaunchCounter": {"observedDispatchValue": 16,
  "isVerifiedCompletedRoundCount": false}`.
- Next round is **20, resumed** — `LOG.md:542` "a fresh session resumes this actual round,
  not round 21."

Lane commits after the last ledgered round: `f405166`, `9825b2a`, `f2e6b21` (2026-10-15,
round 20), `02e9b6e` (2026-10-16, SCORECARD conformance scaffold), `cb807bc` (2026-10-17,
ignore interactive session logs). None has a fleet `rounds[]` row. For a blocked round a
closure row is not owed; the conformance scaffold and the ignore commit are repo hygiene,
but the ledger/lane divergence is recorded as defect **D8** below.

---

## 2. Axes

Owned axes are `operability + freshness` (`SCORECARD.md:3`; `MISSION.md:25`
`kake: { cwd: kake-shokunin/, axes: "operability + freshness (web properties)" }`).

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| operability | **10** | `SCORECARD.md:12` — every free-read verb live-executed; r12 closed the last 4; 31-file state sha guard identical; exit predicates pinned to code | r12 |
| freshness | **10** | `SCORECARD.md:13` — r17 HOLD 10; standing instrument caught W6 before repair; 160-claim inventory re-run, 15/15 stale repairs held | r17 |

Both scores are explicitly **legacy**, not a fresh proof: `SCORECARD.md:5-6` says
"The numeric ratings below are legacy round-17/18 assessments, not a fresh proof that the
current corpus is clean." The round-20 local verdicts are separate (`SCORECARD.md:101-102`):
freshness `improved locally; blocked/unadmitted`; operability `unchanged`.

- **Lowest non-retired axis:** a **10/10 tie**. There is no measured ordering between the
  two; round 20 broke the tie on the falsifiable false-green defect, not on a score gap.
- **Retired:** the *free-read-verb audit sub-surface* of operability (saturated r12,
  `SCORECARD.md:78-86`). Both owned axes remain open (`SCORECARD.md:87-88`).
- **Saturation line + stagnation window N:** **not declared** — `SCORECARD.md:152-154`
  defers it "to be declared by the lane on its next round per `AXES.md` §The stagnation nudge".
  With both axes at the ceiling, the stagnation-nudge condition cannot be evaluated.
- **Capabilities:** **0 rows** — `SCORECARD.md:143-149` carries the empty
  `| — none yet — |` row.
- **`SCORECARD.md` planned claims:** none. `## Planned` (`SCORECARD.md:15-59`) is an
  unblock/decision list ("Host owner / integrator unblock", "Kake unblock", "Receipt
  unblock") plus a labelled historical round-18/19 plan. It contains **no 1–3 claims with
  axis, falsifiable before→after and counting command**, which `AXES.md:25-27` requires.

---

## 3. Corpus

| Item | Count | Command |
|---|---:|---|
| `corpus/knowledge/*.md` entries | **17** | `ls corpus/knowledge/*.md \| wc -l` |
| Pinned-baseline JSON | **1** (`freshness-pins.json`) | `ls corpus/knowledge/*.json \| wc -l` |
| `corpus/lessons/*.md` entries | **22** | `ls corpus/lessons/*.md \| wc -l` |
| — lane-authored `round-*.md` (non-aggregator) | **15** | `ls corpus/lessons/round-*.md \| grep -v aggregator \| wc -l` |
| — aggregator audit lessons | **7** | `ls corpus/lessons/*aggregator* \| wc -l` |
| Lessons carrying a `## Gate` section | **2** (round-20; round-8-aggregator-box3-coldrun) — **1/15 lane-authored** | `grep -l '^## Gate' corpus/lessons/*.md` |
| `QUALITY.md` admission criteria | **5** rows (`Citation-local absence`, `Replayable claim`, `Missing substrate stays visible`, `Admission authority`, `Shape-only probe environment`) | `awk '/^\| Criterion /{f=1;next}f&&/^\| /{print}' corpus/QUALITY.md \| wc -l` |
| Coverage-map data rows | **19** | `awk '/^## Coverage map/{f=1;next}/^## /{f=0}f&&/^\| /{n++}END{print n-1}' corpus/README.md` |
| `## Frontier` bullets | **3** | `awk '/^## Frontier/{f=1;next}/^## /{f=0}f' corpus/README.md \| grep -cE '^- '` |
| Handoffs | **1** (`corpus/handoffs/cmdProbe-merge-fix.md`) | `ls corpus/handoffs/` |
| Pinned values | **43** pins, pin round **18**, `updated` 2026-10-14 | `python3 -c "import json;d=json.load(open('corpus/knowledge/freshness-pins.json'));print(d['round'],len(d['pins']))"` → `18 43` |
| Scripts | `freshness-sweep.mjs` **1,377** lines; `probe-delta.mjs` **159** lines | `wc -l scripts/*.mjs` |
| Tracked files | **100** | `git ls-files \| wc -l` |
| Corpus bytes | **268,081 B** | `du -sb corpus` |

Index integrity: **17/17** knowledge Markdown files have a coverage-map row
(session script comparing filenames to `knowledge/<file>` in `corpus/README.md` →
`unindexed: []`).

### Entry-frontmatter sweep (defect D4)

`CORPUS.md:17` requires each knowledge entry to open with `source:`, `verified-at:` and
`recheck:`. Current state:

| Field | Files carrying it | Command |
|---|---:|---|
| `source:` (literal lowercase form) | **0/17** | `grep -lE '^source:' corpus/knowledge/*.md \| wc -l` |
| `Source:` (capitalised variant actually used) | **7/17** | `grep -lE '^Source:' corpus/knowledge/*.md \| wc -l` |
| `verified-at:` | **0/17** | `grep -lE '^verified-at:' corpus/knowledge/*.md \| wc -l` |
| `recheck:` | **0/17** | `grep -lE '^recheck:' corpus/knowledge/*.md \| wc -l` |

**Overdue `recheck:` before 2026-10-19: 0 identifiable — not because entries are current,
but because no entry carries a `recheck` field or horizon at all.** `grep -rilE 'recheck' corpus/`
returns 1 hit, and it is prose in `corpus/lessons/round-9-aggregator-corpus-verdict.md:11`
("The read-only timer recheck remains consistent…"), not a frontmatter field. Overdue
freshness is therefore unmeasurable at entry granularity; the standing `freshness-sweep.mjs`
pins are the only executable re-check mechanism (`corpus/knowledge/freshness-sweep.md`).

### Frontier content

All three `## Frontier` bullets are blockers/debt, **not an unexplored domain area**
(`corpus/README.md:79-88`): (1) complete the round-20 audit after host bindings;
(2) repair/qualify individual deleted-source citations; (3) obtain a non-author spot-check.
Nothing in the frontier names new external ground, so the **expansion** trend has no
declared target and round 20 correctly reports it `unchanged`.

---

## 4. Mistakes mined

11 classes. "Captured by" is the criterion/rule that already covers the class, with the
sweep actually run in this session; "gap" means no current `QUALITY.md` criterion or
`SKILL.md` rule covers it.

| # | Class | Evidence pointer | Captured by / gap |
|---|---|---|---|
| M1 | **False green in the citation gate** — target-wide OR let an absence note on one occurrence hide an unannotated instruction elsewhere | `corpus/lessons/round-20.md` §Trigger→action; `.ufo/round-20/baseline-proof.json`; fixed by `f405166` | Captured: `QUALITY.md:9` (`Citation-local absence`), `SKILL.md:199-205`. Sweep `grep -ic 'unannotated' corpus/QUALITY.md` → 1 |
| M2 | **Shape-only evidence violation** — controlled fixture env values serialised in proof output; corrected by erratum, not rewrite | `corpus/lessons/round-20.md` §Shape-only erratum; `.ufo/round-20/redaction-validation.json`; commits `f405166`→`9825b2a` | Captured: `QUALITY.md:13`. Sweep `grep -ic 'shape-only' corpus/QUALITY.md` → 1 |
| M3 | **Authority inflation avoided** — 32 rendered scopes are not a dispatched wave; launch counter 16 is not a completed-round count | `.ufo/round-20/wave/validation.json` (`nativeTaskCalls:0`, `dispatched:false`); `LOG.md:470-489` | Captured: `QUALITY.md:12` reject column. Sweep `grep -ic 'launch counter' corpus/QUALITY.md` → 1 |
| M4 | **Self-source proof weakness (open)** — a write planted as the first statement of a later function survives the selftest's write-confinement assertion (scratch mutant, not patched) | `corpus/lessons/round-19-recensus.md` §Independent-audit erratum | **Gap**: `grep -ic 'confinement' corpus/QUALITY.md` → 0; the single `SKILL.md` hit (line 212) is a gate-registry row, not a rule. Proposed criterion in §6 |
| M5 | **Dead-path population disagreement (open)** — lane-granular sweep measures 77 live deleted-path citations; the fleet-level sweep reported 8, with a coarser method | `corpus/lessons/round-19-recensus.md` §Dead-path sweep ("measures **77 live citations** of deleted paths … not the 8 the fleet-level sweep reported") | **Gap**: `grep -ic 'dead path' corpus/QUALITY.md corpus/SKILL.md` → 0/0. Proposed criterion in §6 |
| M6 | **Stale live prose beyond the named sites** — r19 falsified "only `SKILL.md:59/:111` are stale" and the claim that every `origin-work` cite is marked | `corpus/lessons/round-19-recensus.md` §Audit detail; remaining debt is the r20 measured 26 unannotated locations / 7 targets | Partly captured: `QUALITY.md:9` covers citations; **no rule covers stale counts** (SCORECARD `14-vs-30` children). The affected table is now banner-qualified as historical (`freshness-sweep.md:1-6`) and the SCORECARD block is labelled "Historical round-18/19 plan" (`SCORECARD.md:32`) |
| M7 | **Clock-mix erratum (historical)** — r13 wrote `06:00:36Z` (the journal `Starting` line) as the history `at`; corrected in r14 | `LOG.md:31-33` | Captured by append-only erratum; no criterion needed (correct behaviour) |
| M8 | **"Byte-frozen" misclaim (historical)** — raw sha varies per fetch via Cloudflare cfemail re-encoding; valid metric is the normalised sha | `LOG.md:42-44` | Captured by append-only erratum; metric now named in the note |
| M9 | **Journal start-time misread (historical)** — r5 recorded `03:32:06`, corrected to `04:14:50` | `SCORECARD.md:74` move-log row 10; `LOG.md` round-10 entry | Captured by append-only correction |
| M10 | **Proposed merge guard refuted (historical)** — r11's cmdProbe F1 guard failed on the `probe <id> --all` edge; corrected rather than shipped | `SCORECARD.md:72`; `corpus/handoffs/cmdProbe-merge-fix.md` | Captured by handoff + refutation record |
| M11 | **No outside spot-check (open, authority)** — round 20 has no independent non-author review of one admit and one reject; discernment stays `unchanged` | `corpus/lessons/round-20.md` §Gate/Outside spot-check; `SCORECARD.md:112` | Captured as named debt (`QUALITY.md:12` grounding; Frontier bullet 3), but not executable in-lane |

Tally: **3 captured by r20 criteria (M1–M3), 2 open criterion gaps (M4, M5), 1
partially-captured standing debt (M6), 4 historical append-only corrections (M7–M10),
1 authority debt that cannot be closed in-lane (M11).**

ART-reported corpus falsifications (GHP served-set, `CNAME` under Actions, the `CNAME`
servability prediction) are tracked as cross-wave conflicts in §7, not counted here until
a lane round re-opens the primary sources.

---

## 5. Contract defects

| # | Defect | Evidence (command / pointer) | Severity |
|---|---|---|---|
| D1 | `SCORECARD.md` `planned` is not a claim set | `SCORECARD.md:15-59`; `AXES.md:25-27` requires 1–3 claims with axis + measurables; no counting commands present | contract |
| D2 | Saturation line + stagnation window undeclared | `SCORECARD.md:152-154`; `AXES.md:66-73` | contract |
| D3 | Capabilities table empty while both owned axes sit at 10 and saturation is undeclared — the stagnation nudge is undecidable | `SCORECARD.md:143-149`; `AXES.md:57-73` | contract |
| D4 | Knowledge frontmatter fields absent (0/17 `source:`, 0/17 `verified-at:`, 0/17 `recheck:`; 7/17 use `Source:`) | §3 commands; `CORPUS.md:17`, `LEARNING.md:52-60` | corpus contract (fleet-wide pattern: sampled siblings also fail — kagi 7/21 `source`/`Source`, kama 0/9, kumitate 1/38, 0 `verified-at`/`recheck` in all three) |
| D5 | Lesson `## Gate` sections absent in 14/15 lane-authored lessons | `grep -l '^## Gate' corpus/lessons/*.md` → 2 files; `CORPUS.md:18` | corpus contract |
| D6 | `PROVINCE.md` is 334 B and carries only Domain/Owns/Refuses — no Core/Frontier/Adjacent split and no resolvable work surfaces | `wc -c PROVINCE.md` → 334; `LEARNING.md:66-71`; `PROTOCOL.md:415` ("Domain boundary: what it owns, what it refuses, its work surfaces"); sibling `kagi-shokunin/PROVINCE.md` carries a resolved `## Surfaces` census | contract |
| D7 | Round-20 report is lane-local, not at the fleet contract path | `ls .ufo/reports/round-20/kake.md` (lane, 10,341 B) vs fleet `ls .ufo/reports/round-20/` → `kasegi.md kotodama.md`; `PROTOCOL.md:453` puts lane reports in the fleet `.ufo/reports/round-<N>/<id>.md`. Blocked-round handoff, but the path deviation stands | conformance |
| D8 | Fleet ledger has no `kake` row after 2026-10-14 while the lane advanced 5 commits (round-20 work/correction/handoff, conformance scaffold, ignore) | §1 commands; `MANIFEST.json` sweep → 0 entries after 2026-10-14 | conformance/drift |
| D9 | Dead pointers remain live: **7 targets / 26 locally unannotated locations / 8 unresolved**, `newMissing:0` | `python3 -c "import json;d=json.load(open('.ufo/round-20/citation-debt.json'));print(d['counts'],d['unannotatedOccurrences'],d['filesScanned'])"` → `{'resolve':5,'declaredAbsent':48,'declaredAbsentIndirect':3,'drift':7,'unresolved':8,...} 26 43`. Per target: `~/DIRMAP.md` 2; `~/Projects/plazir-15-site` 5; `~/Projects/ufofsdbeta-kimi-review` 1; `~/Projects/webzites` 1; `.../webzites/bin/webzites.mjs` 4; `.../webzites/scripts/kimi-surface.mjs` 8; `~/projects` 5 | freshness debt |
| D10 | Bloat: `LOG.md` 57,570 B/598 lines; `SKILL.md` 33,229 B/375; `free-read-verbs.md` 33,101 B/474; `publish-queue.md` 25,250 B/277; `freshness-sweep.mjs` 83,971 B/1,377 lines | `du -b`/`wc -l` per file; `corpus` 268,081 B total | hygiene |
| D11 | Ignored runtime payload is the largest artifact on disk: `.ufo` 4,852,704 B, of which `.ufo/interactive-sessions/` 4,525,305 B | `du -sb .ufo`; `du -sb .ufo/interactive-sessions`; `.gitignore` line 1. Correctly ignored and never read per plan; only present-on-disk bulk | hygiene (not tracked) |
| D12 | `SHONEN.md` matches the canonical template byte-for-byte modulo repo name, but carries no verifier marks; the round-20 report's `## SHONEN` has 3 `[~]` and 1 `[ ]`, zero `[x]` | `diff` against `PROTOCOL.md` seed (clean); `.ufo/reports/round-20/kake.md:131-141` | expected for shonen (no defect) |
| D13 | No credential material found; the 3 `op://` hits are schematic sweep-pattern text already adjudicated | `grep -rE 'op://' corpus/ \| wc -l` → 3, all inside fenced examples (`round-5-aggregator-audit.md:54`, `round-6-aggregator-audit.md:56`, quoted in `round-9-aggregator-corpus-verdict.md:8`); no secret values printed | clean, with known CORPUS rule-8 literal conflict (operator-side) |
| D14 | Uncommitted changes | `git status --porcelain=v1 \| wc -l` → 0 | clean |
| D15 | `corpus/README.md:60` is truncated mid-sentence: `- kimi `apiv2` authenticated ops are capability-recorded but intentionally` — no predicate, no pointer, and no continuation line | `sed -n '60p' corpus/README.md` (verified in this session; line ends at "intentionally") | index defect |

---

## 6. Proposed round

Resume **round 20** (do not advance to 21). Only two axes are scored-owned, and two claims
on one axis count as one (`AXES.md:25-27`), so the maximum honest claim set is **two**.
Exploratory claims are unavailable: no named non-author reviewer exists to admit
`unprovable-but-better` (`AXES.md:36-44`). No capability claim is proposed because no new
capability has a passing demonstration (`AXES.md:57-64`).

### C1 — freshness: disposition every measured citation-debt location

- **Target:** the 7 targets / 26 locally unannotated locations in
  `.ufo/round-20/citation-debt.json`. Each is either repaired to a verified surviving
  source or locally annotated under P1's documented rule; 8 unresolved targets get a
  named operator restore-or-retire action, never a re-pin.
- **Falsifiable before→after:** `node scripts/freshness-sweep.mjs --section=paths` —
  before: exit **1**, `VERDICT: DRIFT — §paths: 7 unannotated miss · 0 NOT in
  pins.pathsMissSet`; `--section=paths --json`: `drift 7`, `unannotatedOccurrences 26`,
  `newMissing 0` (recorded argv/exit in `.ufo/round-20/acceptance.json`).
  After: exit **0**, drift **0**, unannotated **0**, `newMissing 0`.
- **Counting command (pasteable):**
  `node scripts/freshness-sweep.mjs --section=paths; node scripts/freshness-sweep.mjs --section=paths --json`
- **Second leg (ART-fed; wave-2 verification required):** correct the standing GHP
  platform-semantics claims that `local://kaika-w1-kake-art.md` §4 (K1–K3) reports
  contradicted by primary docs: (a) `corpus/README.md:53`, `SKILL.md:227`,
  `corpus/lessons/round-7.md:23` and `sitemap-orphan-audit.md`'s "served set ≡
  `origin/main` tree" vs `actions/upload-pages-artifact`'s `.git`/`.github`
  always-exclusion and, from v4.0.0, dotfile exclusion, plus Jekyll skips on branch
  builds; (b) `corpus/knowledge/publish-channels.md:9` and `SKILL.md:16` "`CNAME` file
  pins `ds4cc.com`" vs GitHub's statement that the repo `CNAME` is ignored under Actions
  publishing. `ghp-subpath-spotcheck.md:83` ("never servable") stays untouched until a
  free-read `GET /CNAME` settles it. The round-7 lesson is append-only: correct it with a
  new annotation, never by rewriting the lesson.
- **Second-leg before→after:** before, the old claim strings are live —
  `grep -rnF 'served set ≡' corpus SKILL.md` → 2;
  `grep -rnF 'full tree snapshot' corpus SKILL.md` → 1;
  `grep -rnF 'full-tree artifact' corpus SKILL.md` → 2;
  `grep -rnF 'CNAME` file pins' corpus SKILL.md` → 1;
  `grep -rnF 'CNAME` = ds4cc.com' corpus SKILL.md` → 1 (measured in this wave).
  After: each site is replaced by corrected wording or annotated as superseded, and the
  replacement cites the `SOURCES.md` row (S001/S002/S005/S007 in the ART draft). This leg
  is **reported, not verified, by STATE** — W1ArtKake opened S001–S007/S030; this dossier
  did not re-open them.
- **Guardrails:** do not grow `pathsMissSet`, do not re-pin to go green
  (`QUALITY.md:11`, `Missing substrate stays visible`); an annotation must not assert a
  deleted recipe is executable (`QUALITY.md:16`).
- **Knowledge/lesson output:** new entry `corpus/knowledge/citation-debt-disposition.md`
  (per-location disposition ledger; `source:` = `citation-debt.json` plus this round's
  gate run; `verified-at:` = work commit; `recheck:` = the two commands above), and an
  update to the `Citation-local absence` coverage row. This claim needs **no
  `SOURCES.md` row**: an external "where to learn more" registry cannot substitute for a
  deleted local publishing source, and no external source is required to close local
  citation debt.

### C2 — operability: close the r19 confinement-assertion weakness

- **Target:** make the `freshness-sweep.mjs` selftest's write-free proof cover the whole
  source file, so the r19 scratch-mutant bypass (write planted as the first statement of
  a later function survives the check) fails closed. The mutation becomes a permanent
  self-test case against a temporary copy; `HOME`/`KAKE_SELFTEST_DIR` isolation and
  shape-only recording are preserved (`QUALITY.md:13`).
- **Falsifiable before→after:** before, the mutant passes while the selftest reports
  `14/14` (`.ufo/round-20/acceptance.json`; r19 recorded `13/13` at `20d1311`);
  after, `node scripts/freshness-sweep.mjs --selftest` exits 0 with a **new named case**
  and tally `15/15`, and removing that case (or re-introducing the planted write) makes
  the selftest fail. The proof region is named by `grep -n 'BEGIN' scripts/freshness-sweep.mjs`
  so a reader can see the covered span.
- **Counting command (pasteable):**
  `node scripts/freshness-sweep.mjs --selftest; grep -n 'BEGIN' scripts/freshness-sweep.mjs`
- **Output:** updated `SKILL.md` gate-registry row (`SKILL.md:212`), the same runbook, and
  a `QUALITY.md` criterion: *self-source confinement proofs must name their covered
  region and fail on a planted write at every top-level statement position* (this also
  closes M4).

### Admission prerequisites (not claims)

Round 20 can only be **admitted** if, in addition, (a) the host owner supplies the
required existing content/audit/connector alias bindings with the Antigravity→ZFL
fallback (`routing-blocker.json`), (b) the saved complete 32-scope wave is dispatched
(`.ufo/round-20/wave/{spec,plan,rendered-not-dispatched,validation}.json`; 32 distinct
scopes, currently `dispatched:false`, `nativeTaskCalls:0`), and (c) a non-author
spot-checks at least one admit and one reject (`LEARNING.md:37-50`). Without them the
round must again stop honestly with zero credit. None of these is executable in this
read-only wave.

---

## 7. Conflicts and gate disagreements (verbatim)

1. **Round number, two scopes.** Fleet ledger max = 19; lane records a round-20 attempt.
   Lane: `"actualRound": 20`, `"roundComplete": false`, `"verifiedRoundsAdded": 0`
   (`.ufo/round-20/continuation.json`); SCORECARD: "**Round 20 remains unadmitted.**"
   (`SCORECARD.md:17`). Both stand; next round = 20 resume (`LOG.md:542`).
2. **Dead-path population.** Round-19 lesson: "measures **77 live citations** of deleted
   paths at this revision — not the 8 the fleet-level sweep reported, whose method was
   coarser." Round-20 gate: `7` targets / `26` locally unannotated occurrences
   (`.ufo/round-20/citation-debt.json`). These are **different contracts** — live
   citations of deleted paths vs locally unannotated occurrences under P1 — so they must
   not be reported as a single number until a round reconciles scope and unit (M5).
3. **"Every origin-work cite is marked" is false.** Round-19 lesson: "`SCORECARD.md:22`'s
   'every `origin-work` cite is marked absent-historical' is false — `keeper-timer-inert.md:91`
   and `publish-queue.md:167` are unmarked and present-tense." Current bytes show an
   inline r18 annotation at `keeper-timer-inert.md:91`, while `publish-queue.md:167` is now
   a different (historical-baseline) line; closure of this specific pair is **not proven
   by a command in this session**. The gate's 26-location debt is the standing measure.
4. **`pathsMissSet` size.** Runbook check-id table still says "`pathsMissSet` (10 entries,
   r17)" (`freshness-sweep.md:49`) while the r18 repair records `pathsMissSet 10→55`
   (`SCORECARD.md:64`) and the pins file is round 18. The runbook now carries a banner
   declaring the table baselines historical (`freshness-sweep.md:1-6`); the pins file is
   authoritative. Not a live contradiction, but the table's "pinned baseline" column is
   stale prose inside a live runbook.
5. **`~/Projects` children, 14 vs 30.** `SCORECARD.md:41` says "now holds 14 children"
   inside the block labelled "Historical round-18/19 plan (not current measurements)";
   the r19 receipt measured 30. Qualified by label, not repaired.
6. **Red gate vs regression.** Round-20 verdict line (both path and offline runs):
   "VERDICT: DRIFT — §paths: 7 unannotated miss · 0 NOT in pins.pathsMissSet (exit 1)".
   SCORECARD: "Normal path/offline gates remain usefully red, not suppressed"
   (`SCORECARD.md:102`). The red exit is the debt, not a new regression (`newMissing 0`).
7. **Report location.** Fleet contract path `.ufo/reports/round-20/kake.md` is absent
   (fleet dir: `kasegi.md`, `kotodama.md`); the lane-local file of the same path exists
   (10,341 B). Recorded as D7.
8. **No gate disagreement in r19.** The independent audit re-ran the gates green
   (13/13, offline partial exit 0, explicit-bad exit 2, no HOME residue) and its
   disagreement was a **coverage** finding (M4), recorded in the lesson rather than
   silently patched.

### Cross-wave conflicts reported by the ART scout (`W1ArtKake`)

Provenance: `local://kaika-w1-kake-art.md` §2 and §4 (K1–K3), which opened the cited
primary sources in its own session. **STATE confirms the lane-side line citations below
and did not re-open the external sources.** These are conflicts for wave 2 / the Rust
judge, not verified corrections.

1. **GHP served-set claim (reported contradicted).** Lane sites, all verified here:
   `corpus/README.md:53` ("served set ≡ `origin/main` tree"), `corpus/README.md:26`
   ("GHP orphan impossibility proof (deploy = full-tree artifact)"), `SKILL.md:227`
   ("deploy artifact = full tree snapshot"), `corpus/lessons/round-7.md:23`, plus
   `corpus/knowledge/sitemap-orphan-audit.md` (cited by ART). ART's primary-doc finding:
   `actions/upload-pages-artifact` always excludes `.git` and `.github`, and from v4.0.0
   excludes dotfiles unless `include-hidden-files: true` — S001: "Include hidden files
   and directories (those starting with a dot) in the artifact. Excludes .git and .github
   regardless."; S002: "Potentially breaking change: hidden files (specifically dotfiles)
   will not be included in the artifact". Branch builds additionally run Jekyll, which
   skips `_`, `.`, `#`, `~`, `node_modules`, `vendor` (S007: "Start with `_`, `.`, or
   `#`"). ART states the **orphan direction still holds**; the **coverage direction**
   (every tree path is served) does not. This also predicts `ghp-subpath-spotcheck.md:83`
   ("never servable") is false, because `CNAME` is not in the exclusion set — **predicted,
   not verified**; a free-read `GET /CNAME` must settle it before any edit.
2. **Custom-domain claim (reported contradicted).** Lane sites verified here:
   `corpus/knowledge/publish-channels.md:9` "`CNAME` file pins `ds4cc.com`" and
   `SKILL.md:16` "(`CNAME` = ds4cc.com)". ART's primary-doc finding: under Actions
   publishing the repository `CNAME` is ignored and the domain is a Pages setting —
   S005: "If you are publishing from a custom GitHub Actions workflow, no CNAME file is
   created, and any existing CNAME file is ignored"; S003: "A CNAME file in your
   repository file does not automatically add or remove a custom domain."; S026 exposes
   `build_type` (`legacy`|`workflow`), `cname`, `protected_domain_state`.
3. **Index truncation (verified here).** `corpus/README.md:60` ends mid-sentence at
   "intentionally" — recorded as **D15**.
4. **Consequence for the proposed round.** The two doc-fed items are a **second leg of
   C1** (freshness, same axis) with the old-string counts already measured; the `CNAME`
   served-path prediction and the `build_type` free read remain named checks, not claims.
   Corrections must use `SOURCES.md` rows and, for `lessons/round-7.md`, a new
   annotation — never a rewrite.

---

## 8. Provenance

- Read (lane): `PROVINCE.md`, `SKILL.md`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`,
  `AGENTS.md`, `corpus/README.md`, `corpus/QUALITY.md`, all 17
  `corpus/knowledge/*.md` through count/frontmatter sweeps plus header reads of 4 entries, `corpus/lessons/round-19-recensus.md`,
  `corpus/lessons/round-20.md`, `.ufo/round-20/{acceptance,baseline-proof,candidate-proof,
  citation-debt,continuation,receipt-binding,redaction-validation,routing-blocker}.json`,
  `.ufo/round-20/wave/{validation,spec}.json`, `.ufo/reports/round-20/kake.md`,
  `plans/wwkd-round-20-citation-locality.md`.
- Read (fleet): `MANIFEST.json` (`roster`, `rounds[]`), `PROTOCOL.md` (§Round-robin,
  §Evidence standard, §Gate standard, §File contract, §Invariants), `AXES.md`,
  `LEARNING.md`, `CORPUS.md`, `MISSION.md` (lane axis table, push scope),
  `.ufo/round-19/kake.md`, `.ufo/reports/round-20/` listing, `.ufo/l0-questions.md`
  (kake rows), and the ART scout's `local://kaika-w1-kake-art.md` (§1–§4, §7–§8) for
  cross-wave conflicts only — its external sources S001–S007/S030 were **not** re-opened
  by STATE.
- Commands used for counts are inlined beside each number. Gate verdicts are **recorded
  values** from `.ufo/round-20/acceptance.json`, not re-runs in this wave.
- No repository write, no git mutation, no install, no external request, no live-target
  probe. The sole write is this artifact: `local://kaika-w1-kake-state.md`.

### One-line handoff for wave 2

`kake` is a shonen at HEAD `cb807bc8d8bc` with both owned axes legacy-scored 10/10, no
declared saturation line, no planned claims, and an unadmitted round-20 attempt whose
measurable debt is **7 targets / 26 locally unannotated citations**, blocked on host role
bindings and a non-author spot-check. The next honest moves are C1 (clear the citation
debt without re-pinning) and C2 (close the selftest confinement weakness), then resume
round 20 with the complete 32-scope wave. ART adds two reported platform-semantics
contradictions (GHP served-set exclusions; `CNAME` ignored under Actions) and one
prediction (`CNAME` never servable) to C1's second leg; re-open the cited primary docs
before correcting, and keep the append-only lesson discipline.
