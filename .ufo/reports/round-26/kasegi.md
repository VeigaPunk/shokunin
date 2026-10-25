# Kasegi round 26 report

## Work performed

Declared claims: C1, depth:verifiability (lowest non-retired axis, score 4 held), recheck-audit gate conformance — registry row, committed selftest receipt, restated fix-control, whole-entry-deletion soundness; C2, coverage (score 7 held), admits F11 “ISO/IEC 29147/30111 division-of-labour” (assimilation, S041 capture).

- **C1 (R25-2/3/4 + lane-declared deletion gap):** landed `--expect` expected-list contract in `corpus/instruments/recheck-audit.py` (instrument digest `3fc0d751…`; selftest 15 cases, 0 failures, exit 0); SKILL.md `## Gates & probes registry` row (gate|probe, verdict map, `--selftest` spelling, pinned-value path, write scope, owner); regenerated `.ufo/waves/round-26/c1-receipt-index.txt` at the landed digest with the selftest line (fixes the R25-2 cross-reference: round-25 index line 4 has no selftest line); restated fix-control #3 excluding the retained `round-24.md:77` line (R25-4); deletion fixture now exits 1 naming the missing entry. Evidence: `.ufo/waves/round-26/c1-receipt-index.txt`, `c1-instrument-digest.txt`, `c1-live.json`, `c1-controls/e1-selftest-live.txt`, `c1-controls/a5-*.txt` (landed-bytes mutants), wave1/ExecAuditFix.md, wave2/AttackA1-A9/A5/A7/I1.
- **C2 (F11 + assimilation):** captured S041 = JPCERT/CC 2026 partnership guideline (pdf kind; `e18acbf9…`, 147,267 B, 7 manifest-pinned quotes); appended SOURCES row S041; admitted F11 frontier row; wrote two re-grounded knowledge entries (`iso-29147-and-30111-division-of-labour.md`, `iso-29147-divergence-and-clause-crosswalk.md`), both Q1-Q9-conformant per independent audits (SimplYagni, AttackC1/C2); deduplicated F11-1's two F10-B re-quotes to cross-references per the round-25 duplication standard; R25-5 resolution recorded (S040 final URL `https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html`, 2-hop redirect, instrument UA required) in `## Registry changes`. Evidence: `corpus/source-snapshots/round-26/{S041.txt,S040-live.txt,manifest.json}`, `corpus/SOURCES.md`, wave1/ExecCaptureS041.md/ExecManifestRecheck.md/ScribeSourcesAppend.md, wave2/AttackB5/B6/C1/C2/C3/E2.
- **R25-1 compliance:** claims.json frozen at `1b076fa7` before any measurement/dispatch; byte-equal at close (sha `343e568e…`); corrections land as separate appended files.
- **Wave 1:** `kasegi-r26-build`, 35 seats; roles executor 8, scribe 7, scout 5, connector 4, mutation-tester 3, critic 3, revenger 2, sentinel 2, simplifier 1. **5 seats were lost to 429 rate-limit at spawn** (input-token limit exceeded): ConnUsedbyMap, ScribeEntryDivision, ScribeEntryCrosswalk, RevS040Fingerprint, SentContract — none produced partial outputs before failing. Recovery: the two scribe deliverables are present in the lane and passed independent quality audits (the wave-1 scribe items died before output; the equivalent files landed from a same-spec sibling spawn that was cancelled after reconciliation; L1 verified content); the used-by map was completed by wave-2 seat AttackZ1; the S040 fingerprint by AttackE2; the contract checklist by AttackG1. Wave 2: `kasegi-r26-falsify`, 36 seats; roles reviewer 16, critic 4, mutation-tester 5, sentinel 2, scout 2, connector 2, revenger 2, executor 1, scribe 1, simplifier 1; all 36 reports landed, 0 dead. Total: 71 dispatched seats (35+36), 5 rate-limit losses recovered as described. The L1 held the planner seat and ran the integration closure (4 blocker resolutions). Evidence: `.ufo/waves/round-26/{wave1,wave2}/`, `wave1-spec.json`, `wave2-spec.json`, dispatch JSONs.
- **Tool installs/upgrades:** none. Pacman was not used; no tools were installed by any seat (pdftotext already present).

## Landed changes

- C1 gate registry row, instrument expected-list change, receipts, controls, and lesson/SCORECARD updates — LOG.md round 26; lane commit `a04cc6c103c61c3d75465e0ec374a7af3dcf3601`.
- C2 F11 admission: S041 capture + manifest + row, two entries, README/SCORECARD/PROVINCE updates, assimilation gate — LOG.md round 26; lane commit `a04cc6c103c61c3d75465e0ec374a7af3dcf3601`.
- R25-1..R25-5 routed-defect closures and integration closures (receipt regeneration, census E09/E11 fix, F11 name alignment, expected list 39) — LOG.md round 26 and lesson §Integration closure; lane commit `a04cc6c103c61c3d75465e0ec374a7af3dcf3601`.
- Lane HEAD cited in LOG.md — lane commit `a04cc6c103c61c3d75465e0ec374a7af3dcf3601`.

## Before → after measurements

- **C1, depth:verifiability, score 4 held.** Instrument digest c3c19adc… (round-25 pinned) → 3fc0d751… (landed). Registry row: `grep -cE '^\| [^|]+\| gate\|probe ' SKILL.md` 0 → 1 (SKILL.md:981). Selftest receipt line `grep -cE 'selftest cases=' .ufo/waves/round-26/c1-receipt-index.txt` 0 → 1 (`selftest cases=15 failures=0 exit=0` at the landed digest). Fix-control #3 restated (BRE alternation, excluding `round-24.md:77`) 1 → 0 (without the exclusion: 1, the retained historical line). Deletion fixture (whole-entry delete on scratch corpus with committed expected list) exit 0 (`lines=36 total=36`) → exit 1 with `missing=corpus/knowledge/multiparty-vulnerability-coordination.md` (`expect=present expected=39`). Live audit at close: `lines=39 total=39 pass=39 exit=0 expect=present missing=0 unexpected=0`. Counter commands in claims.json; note the frozen `\|`-under-`-E` spelling is vacuous on this host (documented in lesson §Mistakes and wave2/AttackA4).
- **C2, coverage, score 7 held.** Frontier admitted 10 → 11 (awk command in claims.json). Entries citing a row first registered this round (precise S041-only): 0 → 2. Frozen S04x grep reads 3 (round-25 S040 overmatch documented). Census exit 0 before and after. `frontier-recheck-count.py`: 12/12 (round 25) → 14/14 exit 0. Kill rule (no orphan row; census exit 0) satisfied; the orphan-row converse (reverse-E11) is not instrumented — recorded as wave-3 hardening in wave2/AttackB8.

## Sources & frontier

Start census (round-26 base): exit 0, 40 rows (S001–S040), W04 S028/S029 (pre-existing). End census: exit 0, 41 rows (S001–S041), tier A=38/B=1/C=2, mined=29/queued=9/rejected=3, same two pre-existing W04 warnings, no new warning/error codes. Counting command at both boundaries:

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`

Rows added: one tier-A row S041 (JPCERT/CC 2026 guideline); S040 recheck cell restored to cadence-only `180d` with the final-URL/UA prose recorded under `## Registry changes` (E09 fixed). Frontier advanced by F11 (admitted); 11/11 admitted. Assimilation: one theme (ISO/IEC 29147/30111 division of labour), two staged entries adopted re-grounded (S076/S064 → S041 by document); rejects: `vendor-cvd-policy-crosswalk-2026-10-23.md` (F20 absent, Q7 prose recheck, Q3 four-vs-two) and `chinese-criminal-thresholds-and-authorisation.md` (F12 absent, Q2/Q4/Q1/Q7), each with a flip condition. Collision check: reg=40 staged=94 collisions=10 (S031–S040); adopted id continues the registry at S041, citations re-pointed by document. The derived kasegi absent-defect-register slice (7 rows): S065 fetched quote-located; S068 already-mined-legacy (round-25 S040); S037/S054 fetched no-quote (payload-absent, re-quote required); S048/S069/S070 unfetchable. Evidence: `.ufo/waves/round-26/assimilation/` (ids, collisions, slice), wave1/ScoutQuarantine.md, `s3-inventory.txt`, wave2/AttackJ1.

## Trend verdicts

- **expansion — improved.** F11 adds the international-standard division-of-labour ground (S041) with two source-backed entries and one new tier-A row; sibling overlap scan found no lane holds this ground (kake's security.txt explicitly declines handling scope; revenger's JPCERT hit is a conference deck host).
- **quality — improved.** The deletion-soundness gap is closed by a committed expected-list contract; the gate is registered, its selftest receipt is committed at the instrument's own digest, and the fix-control is restated; census/frontier/audit all green at close.
- **discernment — improved.** Re-grounding corrected the staged anchor deltas (図1 caption p.46 not 45; §4 on p.49–50; 参考1 p.54–55), resolved quote line-wrap splits into pinned fragments (Q1a/Q1b, Q2a/Q2b), and the F11-1 duplication vs F10 was caught and fixed by cross-referencing.

## Cross-domain

PROVINCE.md remains accurate (F11 sentence appended; F01–F10 unchanged). Connector seat scanned all 20 sibling lanes + kimi skills for the F11 theme: zero thematic hits outside kasegi (two distinct adjacent entries documented); no sibling corpus was edited. Lane-local `recheck:`/expected-list conventions remain lane-local; no fleet-standard changes made. Evidence: `.ufo/waves/round-26/wave1/ConnOverlap.md`, `c1-overlap.txt`, `c3-usedby.txt`, PROVINCE.md.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists/sources — SKILL.md `## Gates & probes registry` row; density 154.0/652/19 with anchorcheck bad=0 (round-26 measured); lesson round-26.
- [~] End-to-end domain task logged — LOG.md round 26; C1 gate conformance receipts and C2 F11 source-grounded entries.
- [~] Executable instructions without oral context — live audit 39/39 exit 0 (`expect=present expected=39`); frontier harness 14/14 exit 0; selftest 15/15; receipts committed in `.ufo/waves/round-26/c1-receipt-index.txt`.
- [~] No cross-domain bleed — PROVINCE.md F01–F11; wave1/ConnOverlap.md reports no sibling overlap and names adjacency.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none. No open L0 question was filed.

Lane HEAD at report time: `a04cc6c103c61c3d75465e0ec374a7af3dcf3601`.
