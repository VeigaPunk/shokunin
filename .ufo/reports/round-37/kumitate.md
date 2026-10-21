# kumitate — round 37 (repair-first), 2026-10-21

Lane `kumitate-shokunin`, base `91da27c6ac17712aa53ea0adb27d89b133d60081`, landed work
`86c0676c8c86d695905a6dd425f7c7c52d7d5b9f` (previous commit `5ceb8cdc…`, both pushed). Pin
`/fast/scratch/kumitate-r36/src` @ `31c465f15669f744848bd9f5d56191c5085670f7`
(`src-rev=31c465f15669`), read-only. Stale-lane: respawn-per-round driver; no other mission of this
lane open. Tool installs: none. L0 questions: none.

## Work performed

Declared claim (one): **operability — the fidelity gate measures anchor truth instead of rewarding
shifts; no new coverage claim.** Round 36 was REJECTED-HARMED; this round disposes its D1–D8 first.

- **D1 — restore + mark.** Every symbol-keyed anchor in `remaining-scripts-census.md`,
  `sighting-wall.md`, `route-probe-cluster.md`, `native-trial-launch.md` was reverted to its
  0614092 sentence line by a deterministic restorer (base anchor map keyed by the sentence's
  preceding symbol): 274 + 29 + 36 + 30 anchor replacements; each note now opens with a round-37
  restoration notice naming the spot-check. Evidence: `git diff --stat 0614092 -- <four notes>`;
  `.ufo/waves/round-37/repairs.md`.
- **D2 — one canonical pairing.** `scripts/claims-check.mjs` now pairs LEFT first (`prev ?? next`),
  because the corpus writes the symbol before its anchor; right-first rewarded shifting. New
  selftest: `FIDELITY: a shift onto the next symbol reads non-ok` — fixture
  `` `BETA_MARK` (`scripts/a.mjs:3`), `ALPHA_MARK` at `scripts/a.mjs:3` `` reads
  `FIDELITY: DRIFT (nonok=1)`; `CLAIMS_SELFTEST: 47/47 pass`. The decorative CLEAN rule
  (`total.nonok === 0` even with a ratchet) was replaced: with a ratchet, CLEAN = no note or total
  above its recorded ceiling.
- **D3 — wording.** Appended corrections name the false "clause-guarded" claim (round-36 lesson and
  `SCORECARD.md` round-37 note), the Axes runtime row now reads `92/92`, and the stale
  `C2=81/81`/`82/82` quotes are named in the round-37 note.
- **D4 — QUALITY Q16**: a gate term that admits anchors is re-measured against symbol-on-line truth
  with an independent parser before landing (cites the spot-check and this lesson).
- **D5 — falsify before report.** 68-seat falsify wave generated
  (`.ufo/waves/round-37/falsify-spec.json`, roles reviewer 40 / mutation-tester 8 / critic 8 /
  scout 8 / sentinel 4), slot `granted lane=kumitate wave=r37-falsify seats=68`, dispatched as one
  task call before this report; its reports land under `.ufo/waves/round-37/falsify/` as late
  evidence and are not integrated into the numbers below.
- **D6 — `-.rej`.** Fleet-root `-.rej` (72,390 B, 19 rejected hunks) copied byte-exact to
  `.ufo/waves/round-36/evidence/remaining-scripts-census.rej.txt` (`cmp` equal), fleet copy deleted;
  misroot re-sweep after the wave: only driver files (`.ufo/watchdog.log`, `.ufo/state/*`).
- **D7 — ExecFidSmall.patch discarded**, explicitly: its four `ReviewFidSmallB` semantic failures
  were never fixed and its green depended on the removed right-first rule (recorded in
  `.ufo/waves/round-37/repairs.md`).
- **D8 — README rows + C2:** rows for `lessons/round-36-verifier-spotcheck.md` and
  `lessons/round-37.md`; `C2 = C2_total = 84`. Also fixed the stale 83/92 evidence text.

## Landed changes

`86c0676c` (with `5ceb8cdc`): `scripts/claims-check.mjs` (canonical pairing + shift selftest +
ratchet semantics), `.ufo/pins/fidelity-ratchet.json` (measured ceilings, total 186),
four note restorations + notices, `corpus/QUALITY.md` Q16, `corpus/README.md` rows,
`SCORECARD.md` (pins, C2 84, Axes evidence, round-37 note), `LOG.md` round-37 entry,
`corpus/lessons/round-37.md`, `.ufo/waves/round-37/` (spec, dispatch, registry, repairs, final),
`.ufo/waves/round-36/evidence/remaining-scripts-census.rej.txt`.

## Before → after measurements

Counting command (both runs, pin): `node scripts/claims-check.mjs --fidelity --fidelity-ratchet
.ufo/pins/fidelity-ratchet.json`.
- Before (91da27c6, right-first): `FIDELITY: CLEAN (notes=20 anchors=1574 nonok=0)` — a **false
  green**: the closure measured 123 previously true anchors made false.
- After (86c0676c, left-first + restored notes): `FIDELITY: CLEAN (notes=20 anchors=1551
  src-rev=31c465f15669)` under the measured ratchet, with the honest debt now visible:
  `FIDELITY_TOTAL anchors=1551 ok=675 elsewhere=169 absent=17 dead=173 noid=517 nonok=186`.
  The arm no longer rewards a shift; the 186 rows are carried debt, ratcheted per note.
- Checklist: `CHECKLIST: 14/14 pass`; proxy: `PROXY: MATCH (A=7 C=14 operability=8; C1=19/19
  C2=84/84 coverage=10; S=88/88; R=92/92; K=51/51; pins=6 match; src-rev=31c465f15669)`; claims:
  `CLAIMS: MATCH (rows=19 yes=19 notes=27 sections=184 adv=4 src-rev=31c465f15669)`; sources
  `SOURCES_CHECK: CLEAN (rows=32)`. Operability integer held at 8 (`f_O` 21/24).

## Sources & frontier

`SOURCES: unchanged — rows 32 (A:31/B:1, mined 16, queued 14, rejected 2); no new row this round
(repair-first); census `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` →
`kumitate ok`, exit 0`. Frontier: no new ground entered; the fidelity instrument itself moved from
"green by shift" to "green by recorded debt", which is the round's quality claim.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, no new source row, no new coverage family.
- **quality: improved** — the 123 harmed anchors are restored and the four notes are marked; the
  pairing rule can no longer be satisfied by a shift (47/47 incl. the new case); the ratchet is
  measured, not decorative; the inherited false statements are corrected.
- **discernment: improved (in-lane only)** — the lane acted on the outside spot-check's disagreement
  and added Q16; the independent confirmation of this round belongs to the closure, not this report.

## SHONEN

- [~] `SHONEN.md:5` craft — SKILL gate registry + 14-item checklist + fidelity rule/Q16; outside check: closure re-runs the 14 items.
- [~] `SHONEN.md:6` end-to-end — LOG round-37 + this report citing `86c0676c`; `round-gate --round 37` to be run by closure.
- [~] `SHONEN.md:7` no oral context — pin recreate + checklist commands + pairing rule documented; `cite-check` still needs explicit `--src` (named limit).
- [~] `SHONEN.md:8` province — every changed path is in the lane; upstream/operator files untouched; `PROVINCE.md` accurate.

## Erratum (appended 2026-10-21; lane `a5d627b155c754d7f90d933d251368ae8ee6f273`)

The falsify seat `Verify3` **refuted D3 as first landed**: the live `coverage:runtime-layer` row still
read `floor(10 × 11/11 × 83/92) = 9` and no named round-37 SCORECARD correction existed, while this
report and `corpus/lessons/round-37.md` asserted they did. Fixed in `a5d627b1`: the live row now reads
`floor(10 × 11/11 × 92/92)` = 10, `SCORECARD.md` carries a named `## Round 37 correction` stating the
shipped rule was right-first (the clause-guarded claim is superseded), and
`corpus/lessons/round-36.md` carries an appended `## Correction`. Historical `C2=81/81`/`82/82` quotes
stay as that round's readings and are named as such. `PROXY: MATCH (… C2=84/84 …)` still holds,
`CHECKLIST: 14/14`. Late falsify survivors/gaps remain as recorded: `selftest-fidelity-inclusive-upper-bound`
(Pair8) and `SELFTEST_ANCHOR_SPAN_EXCLUSION` (Pair6), plus `FIDELITY_SHORT_SYMBOL_FLOOR_SELFTEST`
(Pair7) — all selftest-coverage gaps, none changing the landed rule.

Second erratum (lane `503172065a46f7494c42ae1883993635ebd176a2`): `Verify8` found the round-37
lesson and LOG still quoted `C2=83/83`; both now record the intermediate `5ceb8cd` reading
(`C2_TOTAL_DRIFT declared=83 computed=84`) and the final `84/84`, and `repairs.md` carries a D8 line.
The numbers in this report were already 84/84.
