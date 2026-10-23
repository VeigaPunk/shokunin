# chousa — round 30 report

Lane `chousa-shokunin`, base `a3a3710e3d0adf2f95882292f17b5093e3baf97c`, lane tip
`b9ed43c64e373b98176dd6e03f0c8259c21122fb` (pushed; `jj-lane.sh state`: ahead 0, behind 0).
Dispatched 02:39Z; report 03:52Z. Dates UTC.

## Work performed

Declared claims (both on routed spot-check items only, D3 and D7 — the anti-loop note allows a
D-list-only round):

- **C1 — coverage:** the edge class of HTML pages that omit `</head>` in
  `tools/quote-reopen.py` (contract v2 item 1). Predicate: `python3 corpus/evidence/round30/c1-count.py`
  prints `QUOTE_REOPEN_HEADLESS_MATCH=106/106`.
- **C2 — operability (lowest scored axis):** the fetch bounds the tool states hold under slow
  senders (sentinel T4) and DNS rebinding (T1) (contract v2 items 2-4). Predicate:
  `python3 corpus/evidence/round30/c2-count.py` prints `QUOTE_REOPEN_FETCH_BOUND_MATCH=27/27`.

Work items:

- Design and freeze before data: claims, loopback harness and two counters
  (`corpus/evidence/round30/{claims.md,qr_harness.py,c1-count.py,c2-count.py}`). v1 `f42906d7`;
  v2 `6b1c5177` (L1 found class-revealing URLs); C2 v3 `7908ce2a` (a control met v2 20/20,
  `.ufo/waves/round-30/controls/CtlShapeKeyed/receipt-dns-header-c2-run1.json`); v4 `abfdf932`
  (C1 no-reader control reached 104/106; C2 slow-ok terminator gap); wording `00cf2365`,
  `60d51f79`. Every change was before any candidate was scored (`falsify/CriticClaimsAfter.md`
  finding 1).
- Pre-data control wave (8 seats): under v4 no control met either counter (best C1 84/106, best
  C2 18/27); receipts `a0bc50b7` and earlier under `.ufo/waves/round-30/controls/`.
- Tool: C2 fetch layer `33dd643f` (ExecC2Fetch), end-of-stream fix `bd43bd53` after a measured
  24/27 (`measure/revA-c2-run1.json`), C1 head boundary `49b2aa30` (ExecC1Head). Tool SHA-256
  `47a657e7…1201`.
- Sources S050-S056 opened this round (W3C HTML 5.2 dated REC; Python socket, http.client, ssl,
  ipaddress docs), cited by `corpus/knowledge/quote-reopen-r30.md` (`a9d3a05a`, corrected
  `fc97f43b`).
- Routed defects: D1 and D2 corrections in `SCORECARD.md`/`LOG.md`, D4 in
  `corpus/lessons/round-25.md`, D5 in `corpus/lessons/round-29.md`, D6 snapshot-control code and
  manifest under `.ufo/waves/round-30/build/ExecD6Snapshot/` (`0dc6e81c`), D3 mutants killed on
  the landed tool (104, 66, 86 of 106), QUALITY 26-29 (`a9d3a05a`), checker
  `corpus/evidence/round30/rerun-check.py` (`RERUN_RECEIPTS=5/6`, exit 1).
- Falsify wave (37 seats), evidence `.ufo/waves/round-30/falsify/` (`fc97f43b`).

## Landed changes

| Commit | Change | LOG |
|---|---|---|
| `f42906d7`, `6b1c5177`, `bf657822`, `7908ce2a`, `dad857af`, `00cf2365`, `abfdf932`, `60d51f79`, `a0bc50b7` | frozen design versions, control receipts, build spec | LOG.md Round 30 |
| `33dd643f`, `bd43bd53`, `49b2aa30` | tool: C2 fetch layer, end-of-stream fix, C1 head boundary | LOG.md Round 30 |
| `0dc6e81c` | after receipts, build-wave reports | LOG.md Round 30 |
| `a9d3a05a` | S050-S056, knowledge entry, QUALITY 26-29, SKILL rows, README, D1/D2/D4/D5 corrections, lesson | LOG.md Round 30 and the D2 correction |
| `fc97f43b`, `b9ed43c6` | falsify evidence, C2 reported as a miss, Gate corrections, SCORECARD Round 30, misroot fix | LOG.md Round 30 |

## Before → after measurements

| Claim | Command (lane root) | Before | After | Verdict |
|---|---|---|---|---|
| C1 | `python3 corpus/evidence/round30/c1-count.py` | 78/106 twice on the round-29 tool (`controls/before-c1-v4-run{1,2}.json`) | 106/106 on `49b2aa30`: 2 L1 runs (`measure/after-c1-run{1,2}.json`) and every falsify re-run (9 in RerunC1A/B/C, 14 in CriticClaimsAfter) | **met** |
| C2 | `python3 corpus/evidence/round30/c2-count.py` | 12/27 twice (`controls/before-c2-v4-run{1,2}.json`) | 27/27 on 41 of 44 fresh-seed runs of `49b2aa30`; **26/27 on 3** (`falsify/RerunC2B/run2.json`, `run4.json`, `extra16.json`): a slow-ok item refused about 0.07 s after its own DEADLINE | **not met** (kill rule: any other value is a miss; not re-scaled). RerunC2B attributes it to the frozen harness's listen backlog of 5 (18/18 at 27/27 with backlog 128 in scratch); that is a counter defect, but the predicate stands as frozen |

No harm: the round-29 counter scored 130/130 on the landed tool, `research-gate.sh` unchanged,
round-1 command 3/3 (`falsify/NoHarmR29Counter.md`). Operability scale 3 → 3.

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`: start `chousa ok`,
exit 0 (49 rows); end `chousa ok`, exit 0, with two W04 warnings (S051/S050 and S053/S052 share a
page URL). Rows 49 → 56; added 7, all tier A (2 spec, 5 docs), status `mined`, used by
`corpus/knowledge/quote-reopen-r30.md`; tiers A 43 → 50; mined 26 → 33. Rows touched: none of the
existing rows; S050 scope and S055 teaches corrected after re-open. Gate reject: the undated
`https://www.w3.org/TR/html52/` URL (redirects to an unregistered host). Gate quote error caught:
S052 (corrected in the lesson). Frontier advanced: pages omitting `</head>` moved to held ground
(C1). Mined mistakes: seven, in `corpus/lessons/round-30.md ## Mistakes`. Sourced claim: C1 rests
on S050 and S051, opened this round.

## Trend verdicts

- **expansion: improved** — C1 measured on new ground, S050-S056 cited.
- **quality: unprovable-but-better** — D1-D6 repaired and reviewed (`falsify/ReviewCorrections.md`),
  QUALITY 26-29 pass their checks (`falsify/ReviewQuality30.md`); but C2 missed and one Gate quote
  (S052) needed a correction.
- **discernment: unchanged** — four controls forced pre-data redesigns, yet the round's own C2
  counter failed the landed candidate under load; no outside judgment yet.

## SHONEN

- [~] SKILL.md decision tables, error patterns, cited sources — `SKILL.md` r30 rows (lane assertion)
- [~] End-to-end task logged — `LOG.md` Round 30; `falsify/LiveS047After.md` (lane assertion)
- [~] Executable without oral context — `python3 corpus/evidence/round30/c1-count.py` re-run by 4 seats (lane assertion)
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; adjacency note on kotodama's `reopen-quote.py` in `falsify/ConnectorKagiPin.md` (report, never absorb)

## Round shape and accounting

Default two v1 waves plus a pre-data control call: controls 8 (ordinary task call: 4 critic,
4 mutation-tester), build 32 (validated v1: 16 scribe, 6 executor, 4 scout, 2 critic, 1 each
connector, reviewer, revenger, simplifier), falsify 37 (validated v1: 11 reviewer,
10 mutation-tester, 8 scout, 5 critic, 1 sentinel, 1 simplifier, 1 connector). Round total 77.
The §3 planner seat is held by the L1. Dead seats (holds, not retried): CriticHarnessIntegrity
(`code=cyber_policy`), CtlShapeKeyed on its follow-up (cyber refusal, after its v2 result),
CriticS047Live (HTTP 429 quota). Containment notes: ReviewContractV2 followed one redirect to
html.spec.whatwg.org and disclosed it; ConnectorKagiPin misrooted its report to the fleet root
(moved into the lane, fleet copy deleted). Third-party page bodies and the 1.4 MB scratch
inventory were kept out of the lane (`/fast/scratch/hyaku/chousa-r30/`). Stale-lane:
respawn-per-round driver; no other mission of this lane is open. Tools installed: none.
Open L0 question: fetch scope (fleet `8d77e6c1`), unanswered; this round opened only registered
hosts. Carried: resolver and dial time outside DEADLINE, uncancelled hop timers
(`falsify/SentinelFetchLayer.md`), the MutHeadNoText survivor, 2xx challenge pages, IPv6.
