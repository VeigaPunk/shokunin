# mado — round 18 (hyaku phase 2, attempt 1)

Lane `mado-shokunin`, branch `master`. Baseline `d9a5a18e17cd3a68b52148fcc01c4a30e340ba98` →
lane tip **`b7148a1eec4f9726b09a7679261ec6e8f5a74c58`** (landed and pushed by
`scripts/hyaku/jj-lane.sh`; `state … local=remote=b7148a1… ahead=0 behind=0`).
The lane VCS is jj-colocated, and every lane commit went through the helper.

## Work performed

Declared claims (pre-registered at `d3a0000`, `SCORECARD.md` "Round 18 — declared claims"):
**C1 calibration** (the lowest axis, literal lesson-citation fraction), **C2 coverage**
(rubric V, P3 Walker + P5 themes/wallpapers), and **C3 operability: capability
acquisition** (the tripwire frozen replay, routed R17-V4). There is no exploratory claim.

- **Outside spot-check R17-V1..V5, how each was handled.**
  - V1 and V2 became lesson M1 and QUALITY criterion 24 (producer identity on receipts), checked by `.ufo/waves/round-18/receipt-check.py`. That check gives 33/33 (exit 0) and reads the six round-17 receipts as `MISSING_PROVENANCE`. The real-transcript receipts were re-cut with a `RECEIPT … tool_sha256= measured_commit=` header (`evidence/final/tripwire-r13..r16.txt`, anchor). An erratum was appended to `lessons/round-17.md`. Carry-over with labels: tool `7a98720e…` is `f71ccbe`, the round-17 before→after row; `962919ce…` is the `0ab1ccc` landed tool.
  - V5 became M2 and QUALITY criterion 25, checked by `measure-mutants.py` (`evidence/measure-mutants.json`). All six tightenings bite: the loose instrument `a280b3ab…` credits each mutant and the tight one `de4c422b…` rejects it.
  - V3: fetch receipts went to `.ufo/waves/round-18/fetch/*/receipts.jsonl`. 329 licensed bodies were committed and 103 kept digest-only (`fetch/RETENTION.json`). `fetch-verify.py` now credits a row only from 200 receipts and flags `CONFLICT`s.
  - V4 is C3.
- **jj audit / trial: fixed, or why not.**
  - Fixed. F10/F14 in `tools/mado-verify.sh`: `pipefail` inside the substitution, per-verb stub rc knobs, and scenarios OM9/OM10 (+17 assertions). The PIN was re-cut `cd1d73d7…` → `20714096…` with a 10/10 KILLED sweep (`evidence/regression-recut.txt`, red-before `evidence/gate-rc-redbefore.txt`).
  - Fixed. `.ufo/state/` (and `__pycache__/`) added to `.gitignore`.
  - Not fixed, F6/R2 (HEAD vs tip): the rows fail closed, and the drafted `refs/heads/master` fix would give a false PASS after an omarchy `git switch` (w2 `CriticJjDisposition`).
  - Not fixed, F9 (`.git` file): `rev-parse --git-dir` would walk up to `$HOME/.git`.
  - Not fixed, F16 landedness: fleet-owned, served by the helper `state`.
  - Not fixed, F17 (old jj log runs): that store is gone, and the current op log has only helper verbs.
  - Final table: `.ufo/waves/round-18/w2/reports/ReviewJjDispositionFinal.md`.
- **C2.**
  - Notes: `corpus/knowledge/walker-route-r18.md` (P3) and `theme-route-r18.md` (P5), with SOURCES rows S072–S095.
  - Non-author re-opening: 24/24 rows re-opened, all agree (lesson `round-18.md` § Gate).
  - Corrections from wave 2: the live-behaviour wording in the theme note was fixed, and an elephant inference was marked `[INF]`. A `SKILL.md` erratum covers the moved walker 2.17.0 → 2.17.2 pins.
- **C3.**
  - `tools/mado-tripwire.py --frozen DIR` was added; the snapshot is `.ufo/waves/round-18/frozen/` (5 inputs, 8 findings, 3 known misses) plus provenance.
  - Hardening: reachability checks, unknown and duplicate keys, a symlinked frozen dir, and pacman operators the parser cannot read now fail safe to `host_mutation`.
  - Registry: a new `mado-tripwire-frozen` row (gate); the `--scan` entry stays a probe. A SKILL erratum states the scope.
- **Frontier step (mistakes).** Lesson rows M1–M8; M4 (L1 passed on an untested audit fix recipe), M7 (HTML digests used as anchors) and M8 (dead seats) are this round's.

## Landed changes

LOG entry `## 2026-10-20 — round 18: producer identity, P3/P5 sourced routes, tripwire frozen replay`.

| commit | content |
|---|---|
| `d3a00003` | pre-registration + start census |
| `4c103b55` | wave-1 integration: frozen mode, gate F10/F14 + PIN re-cut, P3/P5 notes, S072–S095, QUALITY 24–26, lesson, round-17 erratum, registry rows |
| `abfbf35b` | receipts at `4c103b5` (measure before/after, re-cut, frozen, harm watch) |
| `be886a3c` | wave-2 integration: frozen hardening, receipt-check STALE/ancestry, fetch-verify 200-only/CONFLICT, committed licensed bodies + RETENTION, note/SKILL/QUALITY corrections |
| `a210241b` | final receipts at `be886a3`, lesson Gate (24 GATE lines), M7/M8, SCORECARD results, LOG |
| `b7148a1e` | residual w3 checks + errata, final receipts bound (33/33) |

Inherited state: no `lane-dead-no-report mado round=18` line exists, so this was attempt 1. The L1 session exited once on an Anthropic 429 at 16:15Z and was resumed by the orchestrator with the same identity. The work the 12 interrupted wave-2 seats left uncommitted was re-verified and kept:
- the tripwire hardening, completed by L1 (unknown/duplicate keys, symlinked dir, 4 fixtures);
- the fetch-verify fix;
- the RETENTION manifest (L1 added seat/body fields);
- the GateRerun receipts.

Nothing was discarded. One L1 normalisation: `fetch/ReopenS077/receipts.jsonl` body paths were reduced to basenames.

## Before → after measurements

| claim | command | before @ `d9a5a18` | after @ `4c103b5` / final `be886a3` |
|---|---|---|---|
| C1 calibration | `python3 .ufo/waves/round-17/measure.py REV` (c1) | 15/23 = 6.5217 | 18/26 = 6.9231 (semantic 18/23 → 21/26) |
| C2 coverage, rubric V | same (c2) | 4/6 = 6.6667 | 6/6 = 10.0000 |
| C3 capability | `python3 -I tools/mado-tripwire.py --frozen .ufo/waves/round-18/frozen` | usage exit 2 (`evidence/tripwire-frozen-before.txt`) | `frozen_match` exit 0; tamper `snapshot_tampered` exit 2; frozen suite 31/31 (the `abfbf35` tool fails 14/31) |

Receipts: `evidence/measure-before.json.txt`, `measure-after.json.txt` and `evidence/final/*`.

Tool shas, labelled: tripwire `962919ce…` (`d9a5a18`), `c87a31ef…` (`4c103b5`), `c1ae45a7…` (`be886a3`, final). Gate `fba82a66…` → `c9fb0cef…`.

Harm watch at `be886a3`: `HARM_WATCH: PASS` (`evidence/final/harm-watch-summary.txt`).
- Gate selftest 372 → 389/389, regression 10/10, classifier 52/52.
- Tripwire suites: 9/9, 16/16, 33/33, 30/30, frozen 31/31, failsafe 1/1.
- U 7/7, navigation 32/32 → 34/34, census exit 0.

## Sources & frontier

Census command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`.
- Start (`evidence/census-start.txt`): exit 0, with the three historical W04 (S030/S042/S045).
- End (`evidence/census-end.txt`): exit 0, same three W04.

Rows changed 71 → 95. All 24 added rows are tier A: 21 web rows (docs/code at tags walker v2.17.2, elephant v2.22.1, omarchy v3.8.4 and swaybg v1.2.2, plus docs.rs xdg) and 3 host rows (S090/S091/S095). Histograms: A 64 → 88, mined 56 → 80.

Rows touched old→new (same round, before first landing): S092–S095 `recheck` `on-change; …` → `on-release`/`90d`.

Frontier: P3 and P5 move onto documentary sourced ground. README Frontier bullet and index rows updated.

Sourced claim: C2 rests on rows opened this round (S072–S095).

Known defect M7: S094's secondary anchor cites per-fetch GitHub HTML digests, so `fetch-verify` exits 1 on 4 `CONFLICT`s. Its credited raw URL reproduces. A superseding row is planned for round 19.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries on ground the map did not hold (P3, P5), both sourced from mined rows that 24 non-author re-opens confirmed. They are documentary routes, not behaviour.
- **quality: improved.**
  - The gate's false "local edit" arm was fixed, with a red-before receipt and a re-cut.
  - Receipts now name their producer, and fetch bodies are committed or digest-pinned.
  - Same-round overclaims were corrected.
  - Freshness debt (walker pins) has an erratum; no score is claimed for it.
- **discernment: improved.** The R17-V1..V5 outside disagreements became lesson rows M1/M2 and QUALITY 24/25 (plus routed fixes). F10 from the outside jj audit became M3/QUALITY 26. Each check fails on a real `d9a5a18` artifact. Residual critic W3CriticC1Final ruled C1 admit-narrowly. Outside non-author verification is still the closure's job.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry rows `mado-tripwire-frozen` and five probes; errata at EOF (author assertion).
- [~] At least one end-to-end domain task executed and logged in LOG.md — no new desktop task this round (host pause); historical LOG round 3.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/walker-route-r18.md` § Safe observation; `theme-route-r18.md` § Safe observation.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged. w2 `ConnProvinceScope` recommends a path-root refinement for `~/.config/omarchy/**` (round 19); no sibling claims it.

## Waves, seats, routing

- **Wave 1:** 88 seats, validated under policy v2 (`.ufo/waves/round-18/w1/{spec,dispatch,record}.json`). Mix: scout 26, executor 16, reviewer 12, scribe 10, connector 8, critic 5, revenger 4, sentinel 3, simplifier 2, mutation-tester 2. Dead seats: 0.
- **Wave 2 (falsify):** 73 seats. Mix: scout 24, reviewer 18, executor 9, critic 5, mutation-tester 4, connector 4, scribe 4, sentinel 2, revenger 2, simplifier 1. 14 ended without a report:
  - CriticAdmission and CriticHonestyW2 hit Anthropic 429.
  - 12 stopped at L1 session exit on the same 429: FetchVerifyFix, FetchBodyPolicy, TwFrozenHarden, GateRerun, ReviewWalkerUnknowns, ReviewQuality2426, ReviewLesson18, ReviewSkillRegistry, ReviewGateDiff, ReviewTripwireDiff, ReviewFrozenExpected, RevengeOldWalkerNotes.
  - ScribeReportDraft failed on a Cursor usage limit after writing its draft.
  - None was respawned.
- **Residual w3:** 6 seats through one ordinary `task` call (≤8 rule, reviewer 4 + critic 2) over the final commit. No third 64-seat wave was run because the round budget left 39 seats.
- **Round total:** 167 seats.
- **Planner seat:** held by L1. The planning data-walk rode connector/reviewer items (RevPreReg18, RevSeparability18).
- **Routing** (by role, no model parameter): seats spawned before the mid-round re-routing kept their original routes (m_flash, m_swe, m_haiku, m_opus, m_sol).

## Other required lines

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by L1 or any seat that reported (gitleaks was already at `/usr/bin/gitleaks`).
- Misroot sweep: fleet `git status --porcelain` showed no mado seat files. Seats RevR17V1Facts, RevJjTrialFindings, SrcOmarchyBackground, ReopenS081/S083/S087/S089 and ReviewReadme had written reports to the fleet root and moved them into the lane themselves. L1 removed the empty fleet `.ufo/waves/round-18/` directories. This is recorded as lesson M5.
- Host:
  - `/var/log/pacman.log:3161-3169` records `pacman -U zcode-3.16.2` at 13:23 -03 during this round.
  - No mado tool call issued it; the seat-transcript scan was clean in covered forms (`evidence/final/tripwire-r18-seats.txt`).
  - The actor is `[UNK]` and the matter is operator-owned. R15-V1 stays operator-owned.
- Fence slips disclosed by seats: `git status --porcelain` in the lane (JjDisposition, ReopenS090, W3TripwireFinal); one read-only `git cat-file` inside the omarchy checkout (SrcOmarchyBackground). No lane byte changed.
- L0 questions: none filed.
- Admission is not asserted. A non-author closure is required.
