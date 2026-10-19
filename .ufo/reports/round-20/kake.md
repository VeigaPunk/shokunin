# kake — round 20 (resume) report

Lane: `kake-shokunin` (web properties & publishing). Round 20 resumed in a fresh session per the
lane's own handoff (`LOG.md:542`) and the orchestrator steer table (`.ufo/waves/kaika/steer.md`, kake
row). Lane worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kake-shokunin`, branch
`kaika/round`, base `cb807bc`, **lane commit `02b6dd05037376e9fe3af64640d172e0426d397a`** (author
`kake-shokunin <kake@shokunin.local>`). Collision check before work: no `round-20/kake.md` in the fleet
root or ledger worktree; lane `LOG.md` did not close round 20.

**Push:** none. The standing operator rule "No push" overrides MISSION.md's commit-then-push; the lane
commit is local on `kaika/round` and this report is left for the integrator to commit.

## Work performed

Declared claims (1–3, distinct axes):

- **C1 — freshness:** clear the round's citation-local debt (§paths gate exit 1 → 0) by annotating
  each deleted-source citation in place, without re-pinning.
- **C2 — operability:** close the r19 write-confinement weakness in the freshness gate's self-test
  (exact region markers + mutation case).
- **C3 — capability acquisition:** a curated source registry (`corpus/SOURCES.md`, contract v1) whose
  mined rows back four new knowledge entries and the appended corrections of two contradicted
  standing claims (GHP "served set = origin/main tree"; "CNAME file sets the domain").

Work items:

- **L2 swarm, one batched call, 10 seats** (planner, connector, scout, scribe, reviewer, critic,
  4 executors); every prompt leads with `/skill:godspeed` + the verbatim `directive.md` bytes
  (sha256 recorded); no model passed. Executor seats died on provider limits (`resource_exhausted`,
  then `turn_rate_limit_exceeded`) and were re-spawned as fresh batched spawns; a 3-seat post-land
  review batch (reviewer, critic, mutation-tester) followed. Record:
  `.ufo/round-20/resume/swarm-dispatch.json` (lane commit `02b6dd0`).
- **C1:** 26/26 locations annotated (target + dated absence event + "historical record, not an
  executable instruction"), made reader-visible (inside the last table cell on table rows); ledger
  `.ufo/round-20/resume/citation-disposition.json`; pins file unchanged (`git diff cb807bc --
  corpus/knowledge/freshness-pins.json` empty).
- **C2:** `writeConfinement()` at `scripts/freshness-sweep.mjs:1078`; case `e2` at `:1505`; process
  replay `.ufo/round-20/resume/confinement-mutants.mjs`; evidence
  `.ufo/round-20/resume/{confinement-before,confinement-after,confinement-reviewer-recipe,confinement-mutation-probe}.txt`.
- **C3:** `corpus/SOURCES.md` (`## Registry` :5, `## Paths` :28, `## Search log` :35, `## Leads` :45);
  entries `corpus/knowledge/{ghp-served-set,ghp-custom-domain,ghp-etag-anatomy,crawl-scope-per-host}.md`
  (each opens `source:`/`verified-at:`/`recheck:`); 27 appended `r20-correction` tails across 7 files;
  gate quotes `.ufo/round-20/resume/sources-gate.md`; census `.ufo/round-20/resume/sources-census-final.txt`.
- **Contract repairs (supporting, not claims):** `PROVINCE.md` Core/Frontier/Adjacent/Surfaces
  (`:10,:20,:28,:39`); `corpus/README.md:60-63` continuation restored (dropped in `dd4eabf`, text from
  `cd5b381`); SCORECARD saturation line + window (`SCORECARD.md:197`), capability row (`:191`),
  round-21 plan (`:17`); 7 `QUALITY.md` criteria (`corpus/QUALITY.md:14-20`); SKILL pointer to
  `corpus/SOURCES.md` and gate-registry row update.
- **Pre-commit catches by the L1:** S009 anchor (W1 lead said line 1671; `grep -nF '%xT-%xO'` at
  nginx `481d28cb` → 1708); an inserted backtick and dropped table pipes in append-only lines
  (stripped-diff check, now criterion `Append-only tails`); duplicate executor seat overwrite of the
  ledger (rebuilt from the tails, 27/27 reconciled).

## Landed changes

All in lane commit `02b6dd05037376e9fe3af64640d172e0426d397a`; LOG entry `LOG.md:600`
("2026-10-19 — round 20 resume (kaika campaign): three claims landed"); lesson
`corpus/lessons/round-20.md:146` (§Round-20 resume), `:182` (§Gate — round-20 resume), `:241` (§Mistakes).

- C1 corpus annotations — `SKILL.md`, `corpus/README.md`, 9 knowledge files, 6 lessons (LOG.md:600 bullet "C1").
- C2 script change — `scripts/freshness-sweep.mjs` (LOG.md:600 bullet "C2").
- C3 registry, 4 entries, 27 correction tails (LOG.md:600 bullet "C3").
- PROVINCE/README/QUALITY/SCORECARD/SKILL contract repairs (LOG.md:600 bullet "Supporting").

## Before → after measurements

Before = base `cb807bc` (recorded `.ufo/round-20/resume/{paths-before.txt,selftest-before.txt}` at
round open, and `.ufo/round-20/resume/confinement-before.txt`); after = re-run on clean worktree at
`02b6dd0` (porcelain 0 lines).

| Claim | Counting command | Before (cb807bc) | After (02b6dd0) |
|---|---|---|---|
| C1 freshness | `node scripts/freshness-sweep.mjs --section=paths` | exit 1; drift 7 targets / 26 unannotated locations; declaredAbsent 48; missSet 55; newMissing 0 | exit 0 (`VERDICT: OK`); drift 0; declaredAbsent 55; missSet 55; `set-delta miss: no new miss` |
| C2 operability | `HOME=$(mktemp -d) KAKE_SELFTEST_DIR=$(mktemp -d) node scripts/freshness-sweep.mjs --selftest` ; `node .ufo/round-20/resume/confinement-mutants.mjs` | 14/14; regions `B19,B1095,E1166,B1346,E1348,B1366,E1368`; mutants killed 0/25 | 15/15; regions `B1154,E1225,B1515,E1517`; `MUTANTS working-tree: killed 25/25` (cb807bc 0/25); replay-proof `PASS (cases=7, failures=0)`; `--section=paths --json` and `--offline --json` identical old vs new program on the same tree |
| C3 capability | contract v1 census (lines 66-81) ; `sh .ufo/round-20/resume/old-strings.sh` ; `grep -rnF '**[r20-correction' SKILL.md corpus \| wc -l` | no registry; superseded literals uncorrected 9; correction tails 0 | rows 18, malformed 0, `A=16 C=2`, `mined=14 queued=2 rejected=2`, dup/enum/missing all empty, every mined id cited by its used-by file; literals 0; tails 27 |

## Sources & frontier

- SOURCES rows: 0 → 18 — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Added by tier: A 16 (spec 3, docs 8, code 3, dataset 1, own-work 1 — scoped), C 2 (rejected: S017
  Astro `public/CNAME` step, flip = GitHub docs honoring CNAME under Actions; S018 DebugBear "Firefox
  114", flip = a tier-A confirmation). Status: mined 14, queued 2 (S015 Pages limits, S016 versions.json).
- Rows touched old→new: none (all rows new this round).
- `## Paths`: 4 study sequences (served-set semantics, custom-domain ownership, validators + crawl
  hygiene, citation freshness). `## Search log`: 3 bounded passes (fixed candidate sets from the W1
  ART dossier, re-opened; identified/screened/included/excluded counts recorded).
- Frontier advanced: GHP platform semantics (ART U1) → Core (`PROVINCE.md:10`); crawl scope per host
  (U3) → first entry; ETag mechanism (U2) → `ghp-etag-anatomy.md`. Remaining frontier:
  canonical/JS-rendered canonicals, CWV/CrUX, WCAG 2.2, Jekyll/base paths, Render deploys
  (`PROVINCE.md:20`, `corpus/README.md` §Frontier).

## Mistakes

- Classes mined: 16 at base (M1–M11 lane, A1–A4 ART-reported, T1 truncation) + 4 new this round
  (R1 anchor copied from a lead; R2 append-only text altered while appending; R3 duplicate writer
  seat; R4 gate-stuffing risk) — `corpus/lessons/round-20.md:241`.
- Criteria added (7, each citing its lesson): Absence annotation content, Platform mechanism,
  Validator is not identity, Self-source confinement, Population unit named, Index continuity,
  Append-only tails — `corpus/QUALITY.md:14-20`. M7–M10 stay historical append-only corrections.

## Trend verdicts

- **Expansion: improved** — 4 knowledge entries on ground the coverage map did not hold, each citing a
  mined tier-A row (`corpus/README.md` coverage rows "(r20)"); before 0 entries cited any SOURCES row.
- **Quality: improved** — C1 (26 debts dispositioned, gate exit 0), C2 (mutants 0/25 → 25/25; post-land
  mutation probe 9/18 → all 8 re-run survivors killed), 27 source-backed corrections.
- **Discernment: improved locally, unverified** — 2 rejected sources with flips; 8 scout observations
  held back as frontier rather than "corrected"; critic/reviewer findings applied before commit. The
  outside spot-check (≥1 admit, ≥1 reject, ≥3 rows re-opened) is the orchestrator's.

Per-axis self-verdicts (pending non-author verification): freshness improved (HOLD 10); operability
improved (HOLD 10); capability entered (curated source registry). No owned axis observed harmed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` gate registry row + SOURCES pointer (lane `02b6dd0`); `corpus/SOURCES.md`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:600` (C1 citation dispositions, prepared + verified; publishing stays operator-gated)
- [~] Instructions executable by an agent without oral context — `.ufo/round-20/resume/old-strings.sh`, `confinement-mutants.mjs`, census commands in `sources-census-final.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:28` §Adjacent (tabi/chousa/kagi/kama; contested profile lease left to the integrator)

## L0 questions

- kake | round-20 | Restore or retire the deleted publishing sources (`~/Projects/webzites`, `~/Projects/ds4cc-marketplace`, `~/Projects/plazir-15-site`) and the probe history? The corpus now marks every citation historical; it cannot verify recipes without them.
- kake | round-20 | Authorize free reads: `GET /repos/<owner>/<repo>/pages` (`build_type`, `cname`) for the ds4cc and plazir Pages repos, `GET https://ds4cc.com/CNAME`, and `https://veigapunk.github.io/robots.txt` — they settle the CNAME and crawl-scope predictions.

## Integrator notes

- Harness: `cd` silently ran this L1's first (read-only) command in the fleet root — `git log`, `git
  status`, `ls`, `wc`, `grep` only; no writes outside scope. All later commands used `cwd`/absolute paths.
- Harness: `write proc://W2RoundKake.K4xCitations/kill` reported "Cancelled" but the agent kept editing
  lane files afterwards (reported to `xd://report_issue`); the L1 reconciled its edits before commit.
- Provider exhaustion on the executor route (named per the orchestrator note); claims were not shrunk.
- ART dossier `kake-art.md:84,215,369` (its S011) cites nginx `release-1.28.0` `:1671`; the line is 1708 at commit
  `481d28cb` (defect in the W1 artifact, corrected lane-side).
- Fleet `kaika-w1/freshness.md:160-168` counts kake "unannotated dead paths" with a different unit
  (relative `scripts/kimi-surface.mjs` style cites) than the lane gate's P1 contract — not
  reconcilable as one number (new criterion `Population unit named`).
- Contested scope: the the-musketeer Chrome profile lease (`SKILL.md:161`, kagi `PROVINCE.md:43`,
  `connect-sources.md:113`) stays with the integrator.
- Lane-local `.ufo/reports/round-20/kake.md` (2026-10-15 blocked attempt) remains in the lane; this
  file is the fleet-path report (STATE D7). No MANIFEST row exists for kake after 2026-10-14 (D8).


## Post-review fixes

**Lane commit `9639ec7` — `round-20: post-review fixes`**, author/committer
`kake-shokunin <kake@shokunin.local>`. Same round, no new claims; no push.
This section supersedes the earlier broad results wherever they conflict.
Non-author review: W3ReviewKake re-opened all 18 source rows and reproduced
C1/C2/C3 at `02b6dd0`; the orchestrator required the corrections below.

### Append-only restoration and bounded C1

- All 17 prior lesson/knowledge files retain every `cb807bc` original line
  byte-for-byte in order. The 23 prior-file platform suffixes were removed
  and expressed as EOF correction blocks citing original base lines.
  Current-state SKILL/README tails remain permitted. Two files had no
  terminal LF at base; appending requires adding a separating LF, with the
  original terminal text unchanged (`freshness-sweep.md`,
  `round-6-aggregator-audit.md`).
- Main ruled option B: pure standalone notes after citing lines; after tables
  only when within ±2. No table was split and the scanner was not changed.
  **C1 is improved-bounded, annotation only: 22/26 cleared; 4 remain**.
  `TZ=UTC node scripts/freshness-sweep.mjs --section=paths --json` → exit **1**,
  drift **3** targets / **4** unannotated locations, `newMissing=[]`.
  MissSet **55→55**: no source was restored, no historical recipe re-verified.
- Intentionally uncleared: `drift-detection.md:73`, `fleet-registry.md:53`,
  `free-read-verbs.md:317`, `round-6-aggregator-audit.md:48`; an adjacent note
  would split a table, and the table end is outside the local window.
- The previous gate-green 26/26 result belongs to `02b6dd0` only. The prior
  9→0 literal and 27-tail counts are historical layout metrics, not claims
  about the corrected append-only layout. No gate weakened to recover green.

### Anchor-integrity proof

The committed census command is in
`kake-shokunin/.ufo/round-20/resume/post-review-anchors.json` (`scope.gitGrepCommand`):
HEAD-tracked literal filename/path:line and range pointers, including
committed `.ufo` JSON/TXT, markdown and scripts. **728 occurrences**, 367
source lines / 22 files; **148 moved occurrences (120 grouped rows)**;
**942 expanded target-line comparisons, zero mismatches**. No literal
current-state SKILL/README/SCORECARD repoints were needed. Every moved
pointer gets an explicit old→new correction row in the appended
`corpus/lessons/round-20.md` §Inbound-pointer correction register; frozen
evidence remains a snapshot, not rewritten. LOG gets two explicit errata:
its old `free-read-verbs.md:373` → `:374` and
`fire-journal-codes.md:7-13` → `:8-14`. This proof covers literal line
pointers, not semantic links. Original-line subsequence counts and the
four table-distance cases are recorded in
`.ufo/round-20/resume/post-review-restoration.txt`.

### SCORECARD and sources

- Restored the four deleted narrative/history lines: the rollout sentence
  and three-line saturation deferral. The empty capability placeholder was
  a current-value cell, intentionally replaced by the demonstrated registry
  row; it was not a historical measurement row. This is now disclosed in
  SCORECARD and the appended lesson/LOG.
- Appended S007 quote-format correction: schema transcription is not an
  exact rendered-page quotation. The source field claim remains supported.
  Appended S008 correction: “GNU tar 1.35” is withdrawn — the pinned texinfo
  source uses `@value{VERSION}` and does not prove that release label. Exact
  exclusion quote lines are 8587–8588 and 8602. Errata live in
  `ghp-custom-domain.md`, `ghp-served-set.md`, and `sources-gate.md`.
  No SOURCES row cells were modified; no status/recheck/used-by transitions.
- Required validator (after correction):
  `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kake-shokunin`
  → `kake-shokunin ok`, **exit 0**. Registry remains 18 rows. Credential
  sweep of staged changes printed nothing (grep exit 1).

### Final narrowed verdicts

- **Freshness:** improved-bounded, HOLD 10 — annotation coverage only;
  26→4 unannotated locations, 7→3 drift targets, exit remains 1; absent set
  unchanged at 55. Remaining four locations are explicit debt, not hidden.
- **Operability:** improved on the tested population (the C2 code is
  unchanged by this follow-up). Coverage is bounded: aliased/bracket calls,
  split-line calls, metadata/fd writes and child-process writes unchecked;
  0/25→25/25 process mutants is not a universal write-safety proof.
- **Capability:** source registry entered (18 rows, UTC census exit 0).
- **Expansion:** capability row plus `crawl-scope-per-host` frontier entry.
  The three other entries supersede already-covered ground and improve
  quality; they are **not** three additional expansion entries.
- **Discernment:** non-author sample agrees (W3ReviewKake); historical errors
  and all corrections preserved. SHONEN remains `[~]` (no promotion claim).

L0 disposition: the operator may restore/retire the missing publishing
sources; the four table-window locations remain uncleared. Main decides
round admission on these bounded results. The original “Append-only tails”
criterion is preserved as rejected history, explicitly superseded by the
orchestrator ruling in `corpus/QUALITY.md` §Post-review append-only ruling.
