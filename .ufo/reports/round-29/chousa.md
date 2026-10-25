# chousa — round 29 report

Lane `chousa-shokunin`, attempt 1 (in-session hyaku L1). Base `6c5eb1466f2b8abbd3de576389037f435016d07b`; final lane tip `7692bf13a3e4bc4a75e23793e268a3288356ec50` (pushed; `jj-lane.sh state` → ahead 0, behind 0). Dates are UTC.

## Work performed

Declared claim (one): **C1, operability (lowest scored axis, SCORECARD.md:7), capability acquisition.** It adds a new command, `tools/quote-reopen.py verify`. The command re-opens located quotes against the live URL of their `corpus/SOURCES.md` row and returns `VERBATIM`, `ABSENT`, `TOO_LONG`, `NO_SOURCE` or `UNREACHABLE`. The axis is named by the surface the round changes, a new runnable command. This is a different surface from the path-denylist work of rounds 26 to 28: `tools/research-gate.sh` is byte-identical.

- Repair first (round-28 spot-check D1 to D5): see the lesson's `## Spot-check intake` (`chousa-shokunin/corpus/lessons/round-29.md`). D3 got dated append-only corrections in LOG, SCORECARD and the round-28 lesson (landed in `30c9d24d`). D1 and D2 got `corpus/evidence/round29/prose-check.py` and QUALITY criterion 23; the check exits 1 on `lessons/round-28.md` and 0 on the new prose.
- The predicate, counter and fixture were frozen before data (`corpus/evidence/round29/claims.md`, `c1-count.py`, `corpus/fixtures/quote-reopen-r29/`): v1 at `f9fd6d6c`, v2 at `12244431`, v3 at `aa5e1a31`.
- Pre-data control wave of 8 seats. v1 was voided when a label-keyed replay met 82/82 (`.ufo/waves/round-29/controls/CtlLabelKeyed/receipt.json`). v2 was voided when a seed replay met 130/130 on committed seeds. v3 removes caller seeds. Its control receipts (28) were committed at `66bf1b93`; the best is 126/130 (casefold without a boundary), and the best no-fetch cheat reached 115/130.
- Tool built by an executor seat and landed at `30c9d24da1815e01e161ed2f52d5f951005cc2b8` (tool SHA-256 `72a3ad47…54fea`). It includes the sentinel fetch hardening.
- Knowledge entry `corpus/knowledge/quote-reopen-r29.md`, SKILL decision-table, checklist and Gates rows, QUALITY criteria 23 to 25, and sources S046 to S049 (`30c9d24d`, `7692bf13`).
- Falsify wave of 33 seats: re-derivation, 11 held-out seats (33 earlier Gate quotes), 6 mutants, an N-version differential, loopback conformance, security, 4 row attacks, knowledge and repair reviews, no-harm and claim-design critics. Findings are in the lesson `## Falsify wave findings`.
- L0 question filed on the fetch scope (fleet commit `8d77e6c1`).

## Landed changes

| Commit | Content | LOG entry |
|---|---|---|
| `f9fd6d6c` | v1 freeze: claims, counter, fixture, do-nothing receipt | LOG.md Round 29 |
| `12244431` | v1 control receipts; v2 freeze | same |
| `8026fe60` | v2 control receipts (including the seed-replay 130/130 that voided v2) | same |
| `aa5e1a31` | v3 freeze (no caller seed) | same |
| `66bf1b93` | v3 control receipts, before data | same |
| `30c9d24d` | `tools/quote-reopen.py`, knowledge entry, S046 to S049, QUALITY 23 to 25, prose-check, D3 corrections | same |
| `b18b3ec9` | after receipts and build-wave reports | same |
| `7692bf13` | lesson, SCORECARD, LOG, README, SKILL, SOURCES search log, falsify evidence | same |

## Before → after measurements

C1 counting command, run from the lane root, verbatim:
`python3 corpus/evidence/round29/c1-count.py -- python3 tools/quote-reopen.py verify`

- Before (tool absent, v3 counter): `QUOTE_REOPEN_MATCH=0/130`, exit 1 (`.ufo/waves/round-29/controls/before-do-nothing-v3.json`, seed 8324306809653312270).
- After, measured on landed `30c9d24d`, re-run twice by the L1: `QUOTE_REOPEN_MATCH=130/130`, `counter_exit=0` (seeds 1858171162794361068 and 11266274748383853032; `.ufo/waves/round-29/measure/after-run1.json`, `after-run2.json`). Wave 2 re-ran it independently 6 more times, each 130/130.
- Round-1 operability scale, no-harm re-run: `VERDICT_BEARING_EXPORTS=3/3` (score 3 → 3). `research-gate.sh` SHA-256 is `ac1315dd…5835765` and unchanged.
- Limit, reported and not re-scaled: an offline snapshot verifier also scores 130/130 (`falsify/CriticClaimDesign.md`), so the counter shows correct verdicts against current pages but not that the fetch was live. Liveness evidence comes from the loopback harness (`falsify/OfflineConformance.md`, 65 of 65 with only the address guard disabled) and from code review. This control was found after data. The operator rules on it.

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`: start `chousa ok` exit 0; end `chousa ok` exit 0. The CORPUS.md manual census went from rows 45 to 49, malformed 0 to 0, tier A 39 B 1 C 5 to A 43 B 1 C 5, status mined 22 queued 19 rejected 4 to mined 26 queued 19 rejected 4. No duplicates and no missing used-by. Added: 4 rows, all tier A (S046 W3C Text Quote Selector, S047 WICG text fragments, S048 UAX 15, S049 Python html.parser), each mined and used by `knowledge/quote-reopen-r29.md`. No existing row changed. The URLs, access dates and quotes are in the lesson `## Gate`. Frontier advanced: re-opening quotes against live registered sources is new held ground. The sourced claim cites S046 to S049. The mined mistakes are in the lesson `## Mistakes`.

## Trend verdicts

- **expansion: improved.** One new capability on uncovered ground (capabilities table, round 29), resting on mined rows S046 to S049.
- **quality: improved.** QUALITY criteria 23 to 25 were added and D1 to D3 repaired. 33 earlier Gate quotes were re-opened (27 `VERBATIM`, 3 `ABSENT`, 3 `UNREACHABLE`; `falsify/ScoutFreshnessH.md`).
- **discernment: unchanged.** Author view only; the outside spot-check is pending.

## Gate

- Rejected: "a `VERBATIM` verdict shows the quote supports the claim or that the source is true". The reason: S046 and S047 define location, not support (QUALITY 8).
- Rejected before data: design v1, because a label replay met 82/82, and design v2, because a seed replay met 130/130.

## Round shape and accounting

The round ran as two v1 waves plus a pre-data control call: controls 8 (ordinary task call: 4 critic, 4 mutation-tester), build 32 (validated v1), falsify 33 (validated v1). The round total is 73. One seat died: CriticPredicate, a safety-filter refusal (`code=cyber_policy`), held and not retried. The §3 planner seat is held by the L1; the planning data-walk rode ConnectorPlanWalk. Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tools installed: none. Misroot sweep: none (the untracked fleet-root files all predate this round). Page-body caches written by seats were moved to `/fast/scratch/hyaku/chousa-r29/moved-page-bodies/` and not committed. Open L0 question: the fetch scope of `quote-reopen`. Launch was 01:03Z; the report was written at about 02:30Z.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources: `SKILL.md` r29 decision row, Gates row (lane assertion)
- [~] At least one end-to-end domain task executed and logged in LOG.md: LOG.md Round 29; 33 earlier Gate quotes re-opened (lane assertion)
- [~] Instructions executable by an agent without oral context: `python3 corpus/evidence/round29/c1-count.py -- python3 tools/quote-reopen.py verify` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate): `falsify/CriticNoHarm.md`; L0 question on the fetch scope (lane assertion)
