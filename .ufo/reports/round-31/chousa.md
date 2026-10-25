# chousa — round 31 report

Lane HEAD `25c5bb7045df744ddf20b29729625656f375faca` (pushed; `jj-lane.sh state`: ahead=0 behind=0).
Base `be7b8d8d`. Round shape: default two v1 waves plus a pre-data control wave (ordinary task
call). L1 holds the §3 planner seat; the planning data-walk rode ScoutFrontierInventory (scout).

## Work performed

Declared claims (frozen in `chousa-shokunin/corpus/evidence/round31/claims.md`, v1 `d78d1889`, v2 `8070f92b`):
- **C1 coverage** — edge class "a claim names its line or line range" in `tools/research-gate.sh verify-claims` (`"line"`; mislocated + `CLAIM_LINE_MISMATCH`). Frontier → core: README Round26 item "pairing a span's occurrence with a named pointer line".
- **C2 operability** (lowest scored axis; the only scored axis, `SCORECARD.md:7`) — `SKILL.md` checklist item 1's revision clause made runnable for every claim carrying a `"sha256"` pin (stale + `CLAIM_SOURCE_REVISION_MISMATCH`).

Anti-loop honoured: `tools/quote-reopen.py` untouched.

- Control wave (10 seats) broke v1 three ways before data: trim validator met C2 on some seeds, endpoint-only binder met C1 (`controls/CtlShortcutC1/endpoint-exact-*`), counters ignored findings → v2 `8070f92b`; v2 re-score committed `86188116` (C1 max 116, C2 max 118, oracles 120).
- C1 landed `c17948a7`; C2 landed `6d0ae19f`; post-falsify C2 fixes `65d00cfc` and `23536590` (final gate SHA-256 `0bc318b3…1258`).
- Routed D1–D8 repaired append-only (`corpus/lessons/round-31.md` intake table); D2 backlog-128 receipts committed (`.ufo/waves/round-31/build/ExecD2Backlog/bl/`, manifest; mechanism stays `[INFERENCE]`).
- Fleet-report-only D-list items (cannot be edited by the lane): round-30 report cited `7908ce2a` for C2 v3 (counter bytes are `bf657822`), omitted `dad857af`, stated 03:52Z while the commit is 03:50:30Z, and said "four controls" (three findings, two control-forced redesigns).
- Mistakes mined (lesson `## Mistakes`, 9 rows): S052 Gate quote (D7, QUALITY 30), random sub-variants (QUALITY 31), verdict-only counter (QUALITY 32), endpoint shortcut, seat edit reaching the lane gate, L1 run during that window.

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `d78d1889` | design v1 + counters | LOG Round 31 |
| `8070f92b` | design v2 (pre-data) + v1 control receipts | LOG Round 31 |
| `86188116` | v2 control re-score receipts | LOG Round 31 |
| `c17948a7` | C1 gate change | LOG Round 31 |
| `6d0ae19f` | C2 gate change + SKILL checklist run line | LOG Round 31 |
| `ee1024fd` | measurements, S057–S059, knowledge entries, D1–D8, QUALITY 30–32 | LOG Round 31 |
| `ad20a66e` | lesson, registries | LOG Round 31 |
| `65d00cfc`, `23536590` | C2 falsify fixes; SCORECARD/LOG/README; chronology correction | LOG Round 31 |
| `25c5bb70` | lesson falsify findings, falsify evidence | LOG Round 31 |

## Before → after measurements

| Claim | Counting command (lane root) | Before | After | Measured against |
|---|---|---|---|---|
| C1 | `python3 corpus/evidence/round31/c1-count.py` | `LINE_BINDING_MATCH=50/120` (base gate) | `120/120` ×2 on `c17948a7`, ×2 on `6d0ae19f`, ×2 on final gate (`measure/after-c1-run{7,8}-final.json`) | `c17948a7`, `23536590` |
| C2 | `python3 corpus/evidence/round31/c2-count.py` | `REVISION_BINDING_MATCH=50/120` | `120/120` ×2 on `6d0ae19f`, ×2 on final gate | `6d0ae19f`, `23536590` |

Falsify re-runs: 0 runs below 120/120 (RerunSeedSweep31: 30 seeds per counter). Separability 50/120 both cross cells. Operability score 3 → 3 (delta 0, observable beside it). No harm: selftest 215 → 228 PASS, claims-r2 17/17, chain-r3 17/22, r1 observable 3/3 (NoHarmAfter31).

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`: start `chousa ok` exit 0 (2× W04); end `chousa ok` exit 0 (same 2× W04). Rows 56 → 59; tier A 50 → 53 (B 1, C 5); mined 33 → 36, queued 19, rejected 4. Added: S057 RFC 5147 (rfc-editor.org), S058 W3C SRI 2016 REC, S059 Python hashlib — each re-opened by a falsify seat, quote verbatim, tool `VERBATIM`. Rows touched old→new: none. Frontier: README Round31 disposition (line binding + revision pin to held ground). Sourced claim: C1 cites S057, C2 cites S058/S059. L0 fetch-scope question (fleet `8d77e6c1`) still open; only registered hosts were opened.

## Trend verdicts

- **expansion: improved** — two edge classes of claim-vs-source verification moved to held ground (C1, C2), with S057–S059.
- **quality: unprovable-but-better** — D1–D8 repaired, QUALITY 30–32 with shown-able-to-fail checks, CriticEdgeC2's three contract violations fixed in-round; survivors remain (non-string fields, nested keys, selftest gaps), so not `improved`.
- **discernment: improved** — pre-data control wave forced v2 before any candidate scored; chronology audited from receipts (CriticChronology31); one falsify finding rejected with receipts (ReviewQuality31 on QUALITY 32).

## Gate

Real rejects: (1) the extensionless RFC URL (301, empty body) rejected as a fetch, S057 opened as `.txt` instead; (2) ReviewQuality31's claim that QUALITY 32 uses a non-frozen counter — rejected, receipts bind `c3aca35d…`; (3) CtlShortcutC1's v2.1 counter change — rejected, no control meets v2.

## SHONEN

- [~] Real decision tables, error patterns, checklists, cited sources — `SKILL.md` checklist item 1 run line; knowledge entries cite S057–S059 (no non-author verifier yet)
- [~] End-to-end domain task logged — `LOG.md` Round 31; `.ufo/waves/round-31/measure/`
- [~] Executable without oral context — `python3 corpus/evidence/round31/c{1,2}-count.py`; selftest PASS (228)
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; ConnectorPost31 holds

## Seats

Control 10 (7 critic, 3 mutation-tester; 7 resumed for the v2 re-score), build 33 (7 executor, 15 scribe, 5 scout, 1 connector, 1 reviewer, 1 critic, 1 sentinel, 1 revenger, 1 mutation-tester), falsify 34 (12 reviewer, 9 critic, 5 mutation-tester, 5 scout, 1 sentinel, 1 connector, 1 revenger). Round total 77. Dead seats: none. Cancelled at settle deadline: CriticEdgeC1, CriticKnowledgeOverclaim31. Contained breach: CriticSeparability31's edit reached the lane gate 04:26:19–04:26:45.9Z, restored by the seat (disclosed in claims.md). Misroot sweep: none.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none.
