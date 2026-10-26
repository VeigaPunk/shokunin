# tabi — round 32 report (hyaku run 9, attempt 1; L1 TabiR32)

Lane HEAD `8fa57d29ed8a4eab9412782087f9a869399b7896` (`git ls-remote origin refs/heads/master` prints it). Baseline
`d805d1d6132430118b206a848b85753ab35d1014`. Measured revision `08086884d425b879f020af82fc6e57180e991a3e`.

## Work performed

The round declared two claims, frozen before data in `4181fffb` (`.ufo/waves/round-32/claims.json`):
- **C1 — coverage + capability acquisition (sourced).** WebDriver BiDi moves from docs-held to runtime-held on this host (chromium and chromedriver 154.0.8037.97, loopback fixture).
- **C2 — calibration.** Frozen counter v3 adds the `m4-nudge-state` class. It also refuses a failed self-test as an oracle.

The stagnation nudge was active. Every axis was ≥ saturation 8, and no capability entered the table in rounds 29–31. That waived the lowest-axis (adjacency 8) obligation, so the round was a frontier/capability move.

- Two counters: `scripts/check-bidi-runtime.mjs` (new) and `scripts/check-selfassessment.mjs` v3.
  - Landed in `2f8535c5`.
  - A pre-freeze control run exposed a chromium singleton-socket overflow under a deep TMPDIR. The fix landed before the freeze in `5ad1fcbf`.
  - Red/green receipt: `.ufo/waves/round-32/measure/c1-socket-path-red-green.txt`.
- Controls were scored before data (`.ufo/waves/round-32/baseline/README-receipts.md`):
  - C1: do-nothing 0. Docs-only 0. Browserless forgery 16 offline but 0 with `--live`. Counter-as-driver 0.
  - C2: do-nothing 18. Delete-words leaves 15 and fails the deletion leg. Uncited correction 18.
- C1 build:
  - Independent driver `scripts/bidi-loopback-round32.mjs`.
  - Two cold runs, `corpus/evidence/round-32/bidi/receipt.json`. Both runs give the same first screenshot (sha256 `ee0edeba…51eca5`).
  - Entry `corpus/knowledge/webdriver-bidi-runtime-round-32.md`, with R1–R17 verdicts, the gaps, limits and wave-2 corrections.
  - Matrix addendum at the end of `corpus/knowledge/webdriver-bidi-capability-matrix.md`.
  - SKILL section with transport choice per row, the bootstrap recipe and error signatures.
  - README frontier row, plus the capability row `webdriver-bidi-runtime` (SCORECARD, Capabilities — round 32).
- C2 build:
  - Append-only corrections at the end of SCORECARD.md, SKILL.md, corpus/README.md and LOG.md.
  - The three nudge statements (`SCORECARD.md:1473`, `:1515`, `:1576`) now read "nudge was active", with each round's own axes line cited.
  - 15 stale v3 tallies (41/41) corrected.
  - `LOG.md:2072` corrected by hand (the counter does not read it).
- Frontier step:
  - SOURCES rows S123–S126.
  - Lesson `corpus/lessons/round-32.md`: Gate, plus Mistakes M1–M10.
  - QUALITY criteria 83–86.
  - Routed round-31 defects 1–7 dispositioned (claims.json `priorClosure`).
  - Carried errata 27 → 16 (lesson, §Carried round-31 errata).
- Waves (shape: two v1 waves):
  - w1 build + first falsifiers: 36 seats — 12 scribe, 8 executor, 5 critic, 3 reviewer, 3 connector, 2 scout, 2 mutation-tester, 1 sentinel. m_flash 26/36.
  - w2 falsify: 34 seats — 18 critic, 6 reviewer, 3 executor, 3 mutation-tester, 2 connector, 1 scout, 1 sentinel. m_flash 22/34.
  - Round total 70. No residual call. Dead seats 0 (`w1-results.json`, `w2-results.json`: 36/36 and 34/34 outputs).
  - The L1 held the canonical planner seat. The planning data-walk rode the scout ScoutRoutedDefects and the connectors ConnFrontier and ConnTrendsAndNext.
- Wave-2 harm found and repaired. `scripts/check-release-pins.mjs` went green → red at `b234a589` because S125 entered as `on-release` with a tag pin (w2 RerunNoHarm). S125's `recheck` was changed in place from `on-release` to `90d` (logged in the lesson, M10). At `0808688` the gate reads `population=23 unresolved=0` (`measure/noharm-at-0808688.txt`).

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `2f8535c5` | counters + SKILL registry rows | LOG round-32 entry (ledger) |
| `5ad1fcbf` | pre-freeze counter fix (chromium TMPDIR) | same |
| `4181fffb` | claims.json, controls, baseline receipts | same |
| `b234a589` | C1 entry, driver, receipt, S123–S126, C2 corrections, lesson, QUALITY 83–86, w1 evidence | same |
| `08086884` | wave-2 corrections (S125 recheck; entry, matrix, README and SKILL corrections), lesson M6–M10, disposition, w2 evidence | LOG round-32 disposition paragraph |
| `8fa57d29` | measurements at `0808688`, census end, w2 results | — |

## Before → after measurements

All measurements are at `08086884`, in a clean clone with porcelain 0. Both frozen digests are byte-identical, and the frozen-counter diff is 0 files (`measure/provenance-0808688.txt`).

- **C1.** Command: `node scripts/check-bidi-runtime.mjs --rev <REV> --baseline d805d1d6132430118b206a848b85753ab35d1014 --entry corpus/knowledge/webdriver-bidi-runtime-round-32.md --live --json`.
  - Result: population 0 → 16, admitted 0 → 16, failing 0, binding null, exit 0 (`measure/c1-live-at-0808688.json`).
  - **Target met (≥ 14, failing 0).**
  - Plain counts beside the gate (`measure/c1-distinct-at-0808688.json`): 16 distinct ids, 2 distinct transcript digests, driver digest ≠ gate digest, exit 0.
  - Disclosed hole: the frozen gate admits a synthetic transcript with one real screenshot spliced in, and the plain counts do not close that case (w2 CritForgeryRecheck, RerunDistinct). The `feasibilityDisclosed` sentence in claims.json is false as written (lesson M2).
  - Independent re-runs: RerunC1Live (twice, byte-identical) and RerunDriver (a third driver run reproduced the digest).
- **C2.** Commands: `node scripts/check-selfassessment.mjs --rev <REV> --json` and `git diff --numstat 4181fffb <REV> -- SKILL.md corpus/README.md SCORECARD.md LOG.md`.
  - Result: mismatches 18 → 0 (m4 3 → 0), exit 0. Deleted lines 0 (LOG 110/0, SCORECARD 91/0, SKILL 143/0, README 52/0) (`measure/c2-at-0808688.json`, `measure/c2-numstat-at-0808688.txt`).
  - **Target met.**
  - Disclosed split: 15 of the 18 were induced by v3's own case growth.
  - Disclosed instrument holes: loose supersession, plus 5 v3 selftest survivors (lesson M6). The corrections are load-bearing: 7/9 correction mutants were killed (w2 MutC2Corrections).
- **No-harm.** `measure/noharm-at-0808688.txt`: every offline gate and self-test exits 0, including release-pins 23/23, gate-registry nonconformant 0, and sources clean at 126 rows.

## Sources & frontier

- Rows 122 → 126. Counting command: `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md` (fleet census below). Added: S123, S124, S125, S126, all tier A, all `mined`.
- Rows touched old → new: S125 `recheck` `on-release` → `90d`. S119 is untouched; S123 supersedes its anchor month.
- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  - Start: `tabi ok`, exit 0, 19 W04 (`baseline/census-start.txt`).
  - End: `tabi ok`, exit 0, 20 W04 (`measure/census-end.txt`; the new W04 is S123 sharing S119's URL across scopes).
- Frontier advanced: "WebDriver BiDi" docs-held → runtime-held on chromium 154 loopback (`corpus/README.md` round-32 block).
- Sourced claim: C1. The entry's `source:` cites S124, S125 and S126; the gate's s1 check enforces it.
- Mistake mined: M1 `stale-premise` (the nudge statements), plus M2–M10.
- Assimilation: none. No `merge/tabi/` theme was taken, and this lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.** One entry was admitted on ground the coverage map did not hold (BiDi runtime), citing three `mined` rows opened this round. One capability row entered. One frontier item moved.
- **quality: improved.** S123 supersedes S119's month. S124, S125 and S126 were re-opened byte-identical by w2.
  - The w2 CritTrendVerdicts "harmed" finding at `b234a589` was corrected before measurement. The R12 "unmeasured" sentence and the matrix collector clauses contradicted this round's own evidence; both now carry dated corrections.
  - The release-pins red was repaired at `08086884`.
  - Carried precision defects are listed in the lesson (CritNewNumbers: 5 numbers; CritEntry: 10). None changes a verdict.
- **discernment: improved.**
  - Gate admits: S123–S126.
  - Gate rejects: the Chrome-docs page, the classic editor's draft, the `webSocketUrl`-as-classic attribution, and R16.
  - Every mistake has a criterion or a fix, shown able to fail: QUALITY 83–86 with red states in `baseline/` and `measure/`.
  - The outside non-author spot-check is owed to the closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` round-32 section, which adds a transport decision table and error signatures (non-author verifier not yet on record).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the BiDi loopback journey, `corpus/evidence/round-32/bidi/receipt.json`, LOG round-32 entry.
- [~] Instructions executable by an agent without oral context — the bootstrap recipe in the SKILL round-32 section was executed by w2 RerunDriver (a lane-dispatched seat, not a non-author).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; w2 CritAdjacency found no sibling ground absorbed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1. w1 ExecPyClient used `websockets` 17.3 through `uv run --with` (ephemeral, official PyPI); nothing was installed on the host.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.ufo/reports/round-48/tameshi.md` (another lane's, untouched); no tabi misroot. Scratch `/fast/scratch/hyaku/tabi-r32` removed.
Open L0 questions: none.
