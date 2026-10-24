# kotodama — round 64 report

Lane: kotodama-shokunin (jj-colocated). Round 64, attempt 1 of launch 5 (attempts 1–4 of earlier launches died to orchestrator OOM/session freezes/dispatch error; their uncommitted work was inherited, re-verified, reused where sound and discarded where not — both classes named below). Base `ff30a205`; declaration `097c21d` (attempt-1, re-verified); measured at `95c9194e` (claim-C land); records tip and lane HEAD at report time: **`8bab271c691c6b1006da95316a24ae1958ec01e2`** (pushed; `jj-lane.sh state`: local=remote, ahead=0).

## Work performed

Declared claims (1–3, frozen predicates in `reports/round-64/claims.json`):

- **C / coverage (sourced):** language socialization & acquisition unowned (0 filename owners, 0 topic-line owners at base) → one new linguistics entry + 26 mined rows S718-S743 + six disposition rows S744-S749. Predicate: `ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS`.
- **O / operability (counter hardening):** redirect-edge/drip properties unpinned at round 63 → frozen counter pins EDGE_SCHEMEREL/USERINFO/HTTPS/MALTARG/SLASHLESS/308/5TH200 + DRIP + fail-closed `--only` + m5 isolation; unchanged tool passes; ten mutants kill their pinned legs. Predicate: `ACCEPT-O-64: every leg prints PASS`.
- **Ca / calibration (bookkeeping):** round-63 closure routed defects 1,2,3,4,8,9,10 unresolved → each repaired and leg-verified. Predicate: `ACCEPT-CA-64: every leg prints PASS`.

Work items (evidence pointers):

- Wave 1 (build+verify, one batched call, 32/32 seats): completed rows S723/S740 (ExecRowS723/S740), derived `readme-row.txt` (ExecIntegrate, sha `5cc72712…`), full rev3 O receipt + mut-o/edge-o/control-o + ten mutant sources (ExecCounterO), census receipt (ScribeCensus), lesson + report + Gate fragments (Scribes), sibling-overlap scan (ConnectorOverlap), blind-support ring ~50 live verdicts (ReviewSupportA–D), registry/entry/counter attacks (ReviewerRegistry, ReviewerEntry, CriticEntrySweep, ReviewerCounterC/O2, CriticClaims/Ca/O, Sentinels, RevengerCounter), separability proof (ReviewerSeparability), SHONEN survey (ReviewerSHONEN).
- L1 integration: skeleton line-4 range fix, `readme-row.txt`, S687 flip mined→queued (old→new logged), assembler filename-order insertion fix (integrate-w2.py rev1, forcing seat findings F3/D8), real-tree assembly via integrate-w2.py (643→675 rows; entry 81 lines; README 237→238 with known-gaps bullet; sweep exit 0).
- Wave 2 (falsify+repair, one batched call, 32/32 seats): row repairs — S719 hedge restored, S729 re-sourced (Neer et al. 2025; was duplicate of S718), S739 re-anchored to Results, S747 anchor made honest (403 not-located), S722 locator fix, S728/S742 hedges, S735 bounded; four stamped pre-data counter revisions (RevCounters: accept-c rev2+rev3, accept-ca rev2, accept-o rev4→rev5); verification ring (RevVerifyC/O2/Ca, SupS719/729/739/735, RegFinalAudit, CounterDrift, CriticRowsFinal/Receipts/ClaimsJson, SeparabilityRe, GateFinal, LessonFinal, ReportFrag2, OReceiptFresh, CaReceipts, FrontierAudit, UrlSafetyFinal, OverlapRe).
- Residual repair call (6 seats, one ordinary task call): CriticRowsFinal RF1–RF5 corrections (S721/S726/S737 tier A→B with honest scopes; S723/S740 teaches ≤25 words) + ResVerifyRows final audit.
- Records: claims.json statement patch (disposition rows), revisions.txt provenance corrections, final acceptance runs, census end, LOG/SCORECARD/lesson.

## Landed changes

- `6f3e0b24` — instruments + wave evidence: counters (C rev3 `979050ce…`, O rev5 `cdee063e…`, Ca rev2 `d0787979…`), claims.json, telemetry (incl. red rev4 receipt `fed0ded2…`), `.ufo/waves/round-64/` (nw1/nw2 specs+taskcalls, rows/, w1/ 32 reports, w2/ 62 reports, res/ 6 reports), `reports/round-63/telemetry/revisions.txt` corrections. LOG entry: this file, round-64 waves bullet.
- `95c9194e` — claim-C lands: `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, `corpus/SOURCES.md` (+32 rows, S687 flip), `corpus/README.md` (index/counts/footer/known-gaps). LOG entry: round-64 final measures.
- `8bab271c` — records: lesson `corpus/lessons/round-64.md` (Gate 32 rows + disposition evidence; mistakes R64-M1..M19), SCORECARD round-64 table, LOG final measures + routed residuals, `final-measures-{c,o,ca}.txt`, `census-end.txt`, `controls-c.txt`.
- Inherited, re-verified and reused: attempt-1 declaration/counters/dry-run receipts, 30 row contributions, stage components, bookkeeping repairs (LOG/SCORECARD/corpus-LOG), w1/w2 specs. Inherited and discarded: stale `stage/rows.txt`+`stage/bullets.json` (pre-repair row states — assembly uses live `rows/*/row.txt`; staleness recorded in lesson + SupS739/S739 notes), the duplicate S729 Farran source, the fabricated S747 anchor, the attempt-1 22-leg truncated O receipt (preserved as `final-measures-o-rev3.txt` after re-verification; the killed-run receipt class is R64-M17).

## Before → after measurements

- **C:** base `ff30a205`: `python3 -B reports/round-64/accept-c.py` FAIL (dry-run-c.txt: FILE/ROWS/APPEND/NOHARM/SWEEP/LIVE). After at `95c9194e`: **PASS 11/11** — `python3 -B reports/round-64/accept-c.py --root .` → `ACCEPT-C-64: PASS`, exit 0 (`reports/round-64/telemetry/final-measures-c.txt`); NOHARM diff = exactly the new entry; LIVE subset S718/S723/S728/S733/S738/S743 6/6. Counts: corpus 237→238 (`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`), linguistics 29→30, registry 643→675 (census receipts). Controls: do-nothing dry-run-c.txt FAIL; stub control `controls-c.txt` FAIL (ROWS/RESTATE/ONEID/APPEND, exit 1).
- **O:** round-63 counter: 0 EDGE_/DRIP legs (`git show 097c21d:reports/round-63/accept-o.py | grep -c 'EDGE_\|DRIP'` → 0); `--only NOSUCHLEG` exited 0. After at `95c9194e` (counter rev5 `cdee063e…`): **PASS 23/23** — `python3 -B reports/round-64/accept-o.py --root .` → `ACCEPT-O-64: PASS`, exit 0 (`final-measures-o.txt`, sha `8e5c7ade…`; independent copy `final-measures-o-rev5.txt` sha `1cb15569…`); MUT `bad=[] mutants=10`, m5 isolation `EDGE_SCHEMEREL PASS / EDGE_SLASHLESS FAIL`; tool `c0f10a84…` byte-equal to base `ff30a205`. Controls: red rev4 receipt `final-measures-o-rev4.txt` (MUT FAIL, m5 `IndentationError` — three independent rebuilds); do-nothing docstring patch leaves GEN green while all ten mutants die (`control-o.txt`, CriticO).
- **Ca:** base `ff30a205`: `python3 -B reports/round-64/accept-ca.py` FAIL all 7 legs (dry-run-ca.txt). After at `95c9194e`: **PASS 7/7** — `ACCEPT-CA-64: PASS`, exit 0 (`final-measures-ca.txt`). Per-defect evidence: `w2/ReviewerCa.md` (independent re-derivation of all seven), `w2/CaReceipts.md`, `reports/round-63/telemetry/revisions.txt` (with in-place provenance corrections).

## Sources & frontier

- Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` — start (round open, `census-start.txt`): **643 rows, exit 0**; mid (`census-wave1.txt`): 643, exit 0; end (`census-end.txt`): **675 rows, exit 0** (`kotodama ok`).
- Rows added by tier (staged set, per `res/ResVerifyRows.md`): mined 26 = **A 14 / B 12**; disposition 6 = A 1 / B 4 / C 1 (rejected 3: S744/S745/S747; queued 3: S746/S748/S749). End registry tier/status histogram: A=421 B=244 C=10; mined=592 queued=61 rejected=22.
- Rows touched old→new: S687 `mined → queued` (used-by already `—`; the only in-place change; logged old→new in the lesson). No other existing row changed (NOHARM + `git diff ff30a205 -- corpus/SOURCES.md` = 1 changed line + 32 appends).
- Frontier rows advanced: S718–S743 mined with used-by the new entry; S744–S749 disposition rows carry the round-63 reject-curation defect 7; all 32 Gate rows in `corpus/lessons/round-64.md` with URL, access date 2026-10-23 and ≤25-word located quotes (three disposition rows annotated NOT LOCATED with their re-open evidence; S747 carries no quote — honest).
- Sourced claim: **C** rests on rows opened this round — the entry's 26 bullets cite S718–S743, one S-id per line, and the Gate records each row's URL/access date/quote.

## Trend verdicts

- **expansion: improved** — corpus 237→238 on previously unowned ground (0 filename/topic owners verified by sweep commands, `w1/ConnectorOverlap.md`, `w2/FrontierAudit.md`); registry +32 rows.
- **quality: improved** — 11/11+23/23+7/7 frozen-predicate passes; blind-support ring re-established every repaired row (S719/729/735/739 SUPPORTED post-repair; the ring's NOT-SUPPORTED and duplicate findings were repaired, not amended away); tier inflation corrected (S721/S726/S737 → B).
- **discernment: improved** — the wave ring scored its own work: four counter blind spots (citation vacuity, teaches-copy, NITS token gameability, m5 exactness) were found by attackers and repaired pre-data with forcing receipts; post-scoring gaming surfaces and the "exactly their pinned leg" overgeneralization are disclosed, not prettified (LOG routed residuals; claims.json statement patched).

## SHONEN

- Box 1 `[~]` — SKILL.md decision tables/error patterns unchanged this round; census exit 0 re-measured (`census-wave1.txt`); stale round-56 figure in SKILL line 6 noted (`w1/ReviewerSHONEN.md`). Pointer: SKILL.md:20/468/522, `w1/ReviewerSHONEN.md`.
- Box 2 `[~]` — end-to-end round: claims declared → waves → integration → acceptance → records, logged in LOG.md round-64 entries; pointer: LOG.md round-64, `reports/round-64/telemetry/final-measures-*.txt`.
- Box 3 `[~]` — cold-executability evidence: 70 seat reports + counters executed from written specs/committed bytes alone; `accept-ca.py --root .` re-ran PASS in a fresh seat (`w1/ReviewerSHONEN.md`, `w2/RevVerifyCa.md`); remaining conditions named there.
- Box 4 `[~]` — province accuracy: PROVINCE.md unchanged; two sibling-overlap scans (w1/w2) verdict in-lane, one-way lore handoff in the entry's final section; contested scope: none found. Pointer: `w1/ConnectorOverlap.md`, `w2/OverlapRe.md`.
- (`[x]` on any box requires a non-author reviewer; none claimed — the round-63 spotcheck's boxes 3–4 answer is filed above as `[~]` with pointers.)

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (host curl/python3/pdftotext/uv only; seats recorded zero installs; pacman untouched per host-wide pause).
- **L0 questions:** none new this round.
- **Dead seats:** `CriticRevC` (wave 2) — provider cyber-policy refusal on its attack phrasing; last error text: "This content was flagged for possible cybersecurity risk (code=cyber_policy)"; its attack set was absorbed by RevVerifyC (controls re-run on final bytes). Attempt-1 dead seats (orchestrator losses) named in the lesson.
- **Wave-shape note:** operator steer mid-round (next dispatch onward): one v2 wave of 64 seats under `ufo-wave-policy-v2.json`; this round kept its validated v1 32+32 shape per the steer's carve-out.
