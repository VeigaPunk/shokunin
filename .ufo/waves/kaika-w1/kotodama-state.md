# STATE dossier — lane `kotodama` (kaika W1, 2026-10-19)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only this wave).
Scope: linguistic-cultural worldbuilding — conlangs + diachronic staging, myth/symbol
systems, era models, costume/material-culture lexicon, naming; hands off to lore's
world bible. All counts below were measured this session at HEAD unless marked
*filed receipt*.

## 1. Identity

- **Domain** (PROVINCE.md): "linguistic-cultural worldbuilding (言霊, kotodama — the coupling
  of word and world-spirit)" — conlang design/diachronic staging, mythic-symbolic systems,
  era/period models, costume terminology, naming systems, for fictional worlds.
- **Git**: branch `main`, HEAD `c42d675` (2026-10-19 17:03:11 -0300, "round-49 framing …
  64-seat dispatch on key-3 402'd (insufficient funds) — framing artifacts only").
  Clean tree — `git status --porcelain=v1 | wc -l` → **0**.
- **Rank**: minted 2026-10-17 by explicit operator directive (MINT.md, direct-quote branch
  of the mint bar). Probation: ">=3 verified rounds before a roster row" (MINT.md §Probation).
  **Roster row still withheld** — kotodama is absent from fleet `MANIFEST.json` `roster`
  (json filter → `[]`); `SHONEN.md` promotion checklist is all `[ ]` (4/4 unchecked).
  With 35 admitted rounds the probation bar is far exceeded; the unchecked promotion
  checklist is the remaining gate. Identity-consistent, but stale.
- **Last round: 48 — ADMITTED** (loop 2, position 2; C+Ca improved). Evidence:
  `LOG.md:3918` header; SCORECARD r48 table; `reports/round-48/validation.json`
  (`acceptance_checks_passed: true`, `verdict: 'admitted'`); fleet
  `.ufo/reports/round-48/kotodama.md` agrees ("Verdict: ADMITTED — C improved + Ca improved").
  **Fleet-ledger hint verified**: max kotodama round in fleet `MANIFEST.json` `rounds[]` = **48** ✓.
- **Next round: 49 — declared, dispatch-blocked.** `reports/round-49/claims.json`
  (declared 2026-10-19T20:20Z, baseline `78f77a6`, loop 2 position 3): C+Ca "declared FRESH
  via freshness gate (2nd live use)"; 64-seat opencode-go key-3 dispatch 402'd
  (`telemetry/dispatch-declared.json`); `.scratch/r49-items.json` holds the 64-seat plan.
  No seat output; no corpus delta yet.
- **Round census** (from `grep -n '^## ' LOG.md` headers, deduped by round number; r45 is
  kotoba's round, absent here): **48 kotodama rounds — 35 admitted, 12 not admitted**
  (r2, r4, r7, r11, r13 operator-skipped, r17, r22, r36, r42, r43, r44, r47).
  Raw header greps over-count (72 round-mention headers / 40 'admitted' / 12
  rejected-or-failed) because amendments and H3 sub-entries reuse round numbers; the
  deduped per-round list above is the census. Fleet `MANIFEST.json` per-lane kotodama
  rows exist only from r43 onward (closure rows 33–42 carry `lanes.kotodama='ok'`);
  the r46 audit reconciled 12 loop-1 rows row-for-row, zero discrepancies.

## 2. Axes

Six axes (fleet AXES.md): depth, coverage, operability, freshness, calibration, adjacency.

Latest per-axis state = round 48 table (SCORECARD tail; all *filed receipt*):

| axis | r48 verdict | evidence pointer |
|---|---|---|
| coverage | improved (C) | cartography entry landed, 223→224; `python3 -B reports/round-28/readme/sweep.py` → rows 224 files 224 |
| calibration | improved (Ca) | README dup-H1 2→1; over-build class fixed-with-evidence; `tools/check-readme-heading.py` selftest 8/8 |
| operability | unchanged | freshness gate's first live use recorded as gate success, not a claim |
| depth | unchanged | not claimed |
| adjacency | unchanged | not claimed |
| freshness | unchanged — **paused** | not claimed; pause in force |

- **Lowest non-retired axis**: freshness *historically* ("Freshness is historically the
  lowest non-retired axis" — SCORECARD head); freshness axis-move claims **paused since
  r11** pending L0 ruling (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47`:
  "Freshness axis-move claims are paused until ruled"). In-play, r49's declared reasoning:
  "Coverage is the lowest non-retired axis" (`reports/round-49/claims.json`). Freshness
  was actively claimed and improved in r9/r10 before the pause.
- **Saturation**: "No retirement. Legacy saturation line 8 and stagnation window 3 remain
  historical policy" (SCORECARD §Saturation and retired axes).
- **Capabilities: 12** — main `## Capabilities` table 9 rows + r8 addendum 1
  (`d2-typed-labels`) + r9 addendum 1 (`culture-d3-acceptance`) + prose addendum 1
  (`assemble-d4-typed`, SCORECARD:189). Counted by section scan of SCORECARD.md.
- **SCORECARD planned claims**: two `## Planned` H2 sections (lines 686, 691) are **stale**
  (round-13-era and round-36/37-era text). Current plan lives in
  `reports/round-49/claims.json` + `.scratch/r49-{items,claims-candidates,checks}.json`.

## 3. Corpus

- **Knowledge: 224 entries** — `find corpus/knowledge -name '*.md' | wc -l` → 224.
  Partitions: civilizations 94, culture-material 26, linguistics 25, myth-symbol 26,
  synthesis 29, verification 24 (sum 224). Matches README rev-2.5 footer vector
  `25/26/26/29/24/94` and the r48 sweep (*filed receipt*: rows 224 files 224,
  topic_mismatch 0, footer_ok, exit 0).
- **Lessons: 33 top-level files** — `ls corpus/lessons/*.md | wc -l` → 33 (matches the
  lessons-README rev-3 stamp "33 (2026-10-19)"); 137 `.md` recursive including
  triage-fragment dirs; 350 `## ` headings recursive
  (`grep -rh '^## ' corpus/lessons --include='*.md' | wc -l`). **The operator hint
  "lessons 179" matches nothing at HEAD** — 179 was the *knowledge* count in rounds 5–6
  (SCORECARD r5/r6 tables: "179 → 179 knowledge entries"); treat the hint as stale.
- **QUALITY.md: 5 criteria** — provenance, calibration, coupling, usability, canon hygiene
  (`grep -c '^[0-9]\.' corpus/QUALITY.md` → 5). Rejections kept with reasons (criterion 6th
  paragraph) — "a rejection is evidence of taste".
- **Coverage map**: `corpus/README.md` rev 2.5, 589 lines; partition sections at lines
  190/218/247/275/307/334; 224 index rows vs 224 files (sweep, filed receipt).
- **Frontier**: `## Known gaps (frontier)` (README:431) — **12 bullets**
  (`sed -n '431,589p' corpus/README.md | grep -c '^- '` → 12): civ recheck residuals
  (15 r5 + 11 r6 + r7 partials), fleet-header conformance, round-4 unpinned outputs,
  cultural-permission/name-screening/lore-receipt/promotion-review outside evidence,
  historical acceptance-runner whitelists, plus superseded/historical records kept as record.
- **Header conformance** (fleet profile `source:`/`verified-at:`/`recheck:` vs the lane's
  older `- topic:`/`- sources:`/`- couples:` profile — python scan of first 2500 chars of
  each entry): missing `source:` **152**, missing `verified-at:` **133**, missing
  `recheck:` **148** of 224. Lane profile: `- topic:` 224/224, `sources` 204/224,
  `couples:` **93/224** — 131 entries carry no couples line, a QUALITY-criterion-3 gap
  (criterion says an entry that couples nothing "must say so"). Matches frontier bullet
  "Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck`
  header" (README §Known gaps). The three-readings disagreement (64/3/0 of 179 on
  2026-10-17) is a recorded open integrator question, reported not absorbed.
- **Overdue `recheck:`**: 1 dated recheck before today —
  `corpus/knowledge/civilizations/ottoman.md` (2026-10-17). Most `recheck:` lines are
  conditional cadences ("whenever X changes"), not dates. New-style entries (r48
  `cartography-and-mapmaking.md`) carry the full header with sha256-pinned sources —
  the exemplar contract.

## 4. Mistakes (rejected / harmed / honest-stop, errata, gate disagreements)

| round | class | evidence | captured? |
|---|---|---|---|
| r2, r4 | rejected (historical) | SCORECARD head: "including rejected rounds 2 and 4" | lessons/round-2-adjacency.md, round-4-sol-fixes-and-audits.md |
| r7 | closed failed: acceptance recorded false — "the F claim's wrong rejection, a preservation failure" (README §Known gaps, D3 bullet) | `reports/round-7/validation.json` `acceptance_checks_passed: false` | append-only correction pattern (r22 correction entry) |
| r11 | REJECTED, F failed as declared: ≥95% 24h hash-stability threshold "failed at 0.778 purely because build rounds 10/11 legitimately changed the tree" (l0-questions.md:47) | LOG r11 header; L0 row | **open** — freshness paused until operator rules; no QUALITY/SKILL criterion |
| r13 | operator-skipped | SCORECARD r16 note "r13 operator-skipped" | — |
| r17, r22 | REJECTED on claim D (×2) | LOG headers 1081, 1156; r18 "repairs the r17 rejection" | lessons/round-17.md, round-22.md + correction entry |
| r33 | F-C13-1 incident: filed receipts written in-tree during the wave (restored; record filed) | LOG:3548 | **captured** — absolute rule + `tools/harness/receipt_guard.py` (r14) + targets.json "ABSOLUTE: never run reports/round-*/run-validation.py in-tree" |
| r35 | README apply left two `__E3_PLACEHOLDER__` lines (removed r37) | LOG r37 "Integrator repairs"; SCORECARD:680 | **gap** — sweep was green; heading control covers headings only; proposed: sweep placeholder-token grep |
| r36 | NOT ADMITTED on D, honest stop: premise falsified — register-form domain "already closed by rounds 26/27" (LOG:3676) | `reports/round-36/validation.json` exit 1 | **captured** — `claims-freshness.py` (r47) now flags stale premises at declaration |
| r36 | repeat F-C13-1 breach (seat ran r35 runner in-tree ~25s, final state clean) | LOG r36 "Conformance incident" | captured (same as r33) |
| r42 | NOT ADMITTED on C: C01/C04 authored the same lithic register; declared 27/224, delivered 26/223 | LOG:3804; validation receipt `0a0b20f6…` | **gap** — no QUALITY criterion for gap-ownership sweep before authoring; r49 checks add `topic_owner_absent` probe |
| r42 | incident: two existing entries (animal-symbolism, plant-symbolism) momentarily overwritten by stale path proposals; census arithmetic caught it; restored byte-exact | LOG r42 "Incident" | **gap** — receipt_guard covers validation.json only, not corpus entries; proposed: pre-commit corpus census/ownership gate |
| r43 | NOT ADMITTED on O+C: "claims O and C were declared on premises false at baseline … (not re-measured before dispatch)" — R01-43-12 | LOG r43; `reports/round-43/validation.json` | **captured** — `tools/harness/claims-freshness.py` selftest 62/62, live uses r48/r49 |
| r44 | NOT ADMITTED on C+Ca: carried-candidate collision (dream slug already named r42 K02:216); "not carried" ruled strict (R01-44-09) | LOG r44; SCORECARD r44 table | **gap** — ruling on record, no durable criterion; r49 ownership probes partial |
| r44 | provider defects: antigravity lane aborted twice; opencode-go `reasoning_content` API defect (18 failed seats) | LOG r44 Trigger | telemetry availability-close records; class recurs (hyper 402 r36, key-3 402 r49) |
| r47 | NOT ADMITTED on C: over-build — "790 lines vs live partition max 221 with 9 blocking defects" (R03 B1–B9) | LOG r47; `review/R03-c-content.md` | dispositioned fixed-with-evidence (`calib/queue-successor-r48.json`); **no QUALITY size criterion** — proposed: right-size discipline (≤~250 lines / 1.08× partition max, worked example must pass) |
| r9 | adjacency conformance defect: two out-of-lane writes (fleet-root v09-myth.md + junk PDF), swept/remediated; X03 missed it | SCORECARD r9 adjacency row | recorded; boundary audits (r46 A) now cover |
| r10 | integrator caught + reverted a worker rewrite of filed round bytes (r9 validation.json, r8 run-validation.py) | SCORECARD r10 calibration row | captured — receipt_guard + append-only audits |
| errata | r5 phonetics erratum (bibliography only); r6 Vedic-timing + Persian access/locator errata (appended, original bytes preserved); SKILL error-pattern erratum 2026-10-19 retiring anchors TL-01/TL-02/FIELD_DEFAULT | README frontier; SKILL Error patterns | captured — corrections-as-new-entries discipline |
| readings | header-conformance three readings (64/3/0 of 179) | LOG r43-era; QUALITY-adjacent | open integrator question, reported not absorbed ✓ |
| readings | D1 register-test/form-typology contradiction — resolved r48 (star chart + cosmogram as "doctrinal-correspondence boundary form") | LOG r48; fleet report | resolved with recorded act |

No `harmed` axis verdict appears in any r33–r48 record — rejections are honest stops with
improved side-claims recorded without averaging into an accept (per-essence behavior).

## 5. Contract defects

- **Required files present**: SKILL.md, PROVINCE.md, SCORECARD.md, LOG.md, SHONEN.md,
  `corpus/README.md`, `corpus/QUALITY.md`, `corpus/knowledge/`, `corpus/lessons/` ✓
  (root listing). Extra lane files: MINT.md, AGENTS.md, REGIMEN.md, templates/, examples/ —
  mint/regimen records, plausibly in-contract.
- **Roster/promotion tension**: 35 admitted rounds but roster row withheld and SHONEN
  checklist 0/4 checked. Probation bar (≥3 verified rounds) long exceeded; promotion is
  gated on the checklist + named non-author verifier. Not a defect, but stale state worth
  a wave-2 decision.
- **Stray artifacts**:
  - Nested empty `kotodama-shokunin/kotodama-shokunin/` (contains only an empty
    `reports/`; `find kotodama-shokunin -type f` → 0 files; untracked, invisible to git) —
    leftover of a nested checkout; safe to delete by the integrator (not touched this wave).
  - `out/` — empty, untracked, **not in .gitignore** (gitignored set: `.ufo/state`,
    `.ufo/watchdog.log`, `*.log`, `__pycache__/`, `/reports/supplement-opencode-1/scratch/`,
    `.scratch/`).
  - `tools/__pycache__/` — gitignored, present on disk.
- **Bloat** (sizes with commands):
  - `.scratch/` **66GB** untracked (`du -sh .scratch`), 2433+ entries — workspace scratch,
    gitignored; the dominant disk consumer.
  - `reports/` **440MB** on disk / 2637 tracked files; `reports/supplement-opencode-1`
    alone 384MB on disk (its `scratch/` is ignored). Tracked repo total **81MB**
    (`git ls-files -z | xargs -0 du -ch | tail -1`); 3466 tracked files.
  - Ledger sizes: LOG.md 3945 lines / 246.5KB; SCORECARD.md 952 lines / 104.8KB;
    `corpus/README.md` 589 lines / 142.3KB; SKILL.md 732 lines / 86.2KB.
  - Oversized tools: `tools/exercise-handoff-e2e.py` 240.1KB, `tools/d2-typed-labels.py`
    190.4KB, `tools/check-gate-battery.py` 64.9KB.
- **Duplicate-heading defect class** (the class r48 fixed in README, r49 Ca queues):
  - `corpus/README.md` carries a duplicate `revision: 2.0` block —
    `grep -c '^revision: 2\.0' corpus/README.md` → **2** (r49 Ca premise, verified).
  - **New finding this session**: SCORECARD.md has **two** `## Planned` H2 sections —
    `grep -c '^## Planned' SCORECARD.md` → **2** (lines 686, 691), both stale. Same class;
    candidate for a successor Ca round.
- **Lessons record stops at round 32**: 33 lesson files cover rounds 1–32 + supplement;
  regimen-2 rounds 33–48 (16 rounds) have **no** `corpus/lessons/` files — scribe records
  now live in `reports/round-N/scribe/` (e.g. `reports/round-48/scribe/S01–S03`). Either
  the convention moved (undocumented) or the append-only lesson record lags 16 rounds.
  The lessons README (round-25 era) still claims "one file per round that ran".
- **Dead pointers**: none found in a 4-file spot check (`reports/round-28/readme/sweep.py`,
  `reports/supplement-opencode-1/22-label-representation.md`,
  `corpus/knowledge/verification/to-verify-triage-protocol.md`,
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` — all exist).
- **Uncommitted changes**: 0. **Fleet-side artifacts**: `.ufo/reports/round-48/kotodama.md`
  present and consistent; mint scope `.ufo/scopes/kotodama-mint-20261017/mint-roster-scan.json`
  present. 4 kotodama rows in fleet `.ufo/l0-questions.md` (r2, r8, r9, r11) — r11 owns the
  freshness pause.

## 6. Proposed round (r49 — already declared FRESH; dispatch-blocked)

Staged in `reports/round-49/claims.json` + `.scratch/r49-{claims-candidates,checks,items}.json`,
both premises re-verified this session:

1. **C / coverage (the lowest non-retired axis in play, freshness paused)** — land ONE
   right-sized `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` on the
   verified-fresh subsistence-production gap; total 224→225, culture-material 26→27,
   README rev 2.6. Falsifiable before→after: before `find corpus/knowledge -iname '*hunt*'
   -o -iname '*forag*' -o -iname '*subsist*' | wc -l` → **0** (re-verified) and
   `grep -rniE '^- topic:.*(hunt|forag|subsisten)' corpus/knowledge/` → only a lexicon
   field + a seasonal-cycle row (2 false-positive topic hits, per r49 checks); after →
   sweep `rows 225 files 225`, exit 0. ≤~250-line discipline per the r48 cartography
   precedent. **Serves**: one new knowledge entry + its SOURCES.md rows (external shelf
   will carry `(to-verify)` locators like the cartography entry's).
2. **Ca / calibration** — remove the residual duplicate `revision: 2.0` README block
   (`grep -c '^revision: 2\.0' corpus/README.md` → 2 → 1) as a recorded act; extend
   `tools/check-readme-heading.py` (or file a durable note) so duplicate revision-prose
   blocks are caught. **Serves**: README hygiene; no new knowledge entry.
3. **Freshness (blocked, for wave 2)** — the 152/133/148 header-conformance gap
   (§3) is the natural freshness-axis claim the moment the r11 L0 ruling lifts the pause;
   a per-entry header backfill would be a falsifiable before→after with the python scan
   as counting command. Until ruled, freshness claims stay paused — the lane correctly
   routes coverage as the lowest in-play axis instead.

**Dispatch blocker**: opencode-go key-3 402 insufficient funds (last commit message;
`telemetry/dispatch-declared.json`). Round 49 is framed with zero seat output — a
provider-availability blocker, not a lane defect.
