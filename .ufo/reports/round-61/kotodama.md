# kotodama — round 61 report (hyaku phase 4, attempt 1, L1 KotodamaR61)

Lane base `942abdf4`; lane tip `c587cd57b5e2d981468b8877d327cf3599e47e5b` (pushed; `jj-lane.sh state`: local = remote, ahead 0). Instruments revision 0 `106df397` (dry-run `78ad4b17`); revision 1 and freeze `2f4f8a40`; O landed `675d59af`; C landed `efbee29c` (measured revision); records `ae8e393e`, `c587cd57`.

## Work performed

Declared claims (`reports/round-61/claims.json`, frozen at `2f4f8a40`):

- **C — coverage (sourced claim):** frontier → core. A new culture-material entry on footwear, `corpus/knowledge/culture-material/footwear-codes-terminology.md`, citing new rows S652-S692, one S-id per bullet line. Predicate `ACCEPT-C-61: every leg above prints PASS.` (14 legs). **Verdict: MISSED** — LOCATE 40/41 (S671).
- **O — operability (capability acquisition):** `tools/check-cited-lines.py`, the R60-M6 clause-scoping lint (MULTI-ID / TABLE-ID). Predicate `ACCEPT-O-61: every leg above prints PASS.` (6 legs). **Verdict: PASS.**

Anti-loop: rounds 58-60 failed on blind support of multi-row and lead-in packets in the amulets entry. This round did not re-enter that entry, opened a different frontier area (footwear; 0 filename and 0 topic-line owners at base, `ScoutOwners.md`), ran no blind support leg as a predicate, and reviewed support one row and one clause per seat with no carried context (wave 2, review-only). No allow-list pilot was needed because no seat was confined by a predicate.

Work items:

- Repair first (round-60 spot-check §5, all seven items): corrections recorded in `corpus/lessons/round-61.md` (`## Spot-check intake`, `## Corrections to the round-60 report`), `SCORECARD.md` round-60 correction rows, `LOG.md` round-61 entry; landed `ae8e393e`. Figures re-derived from committed bytes; two of the spot-check's own figures were corrected in turn: pypdf was used through `uv run --with` by **seven** seats, not five (`.ufo/waves/round-60/w1-a3/AuditA3R15.md:95`, `CtlRubberStampA3.md:149` in addition to the five), and the S646 finding is SupportB60 **P01**, not P07 (`.ufo/waves/round-60/support/planted-key.json`).
- Instruments: `reports/round-61/accept-c.py`, `accept-o.py`, `reopen-quote.py`, `claims.json`, base list; dry-run receipt `reports/round-61/telemetry/declaration-dry-run.txt` (`106df397`, `78ad4b17`).
- Pre-data control wave (wave 1, 36 seats): ten controls met revision 0 and each forced a change in revision 1 (`2f4f8a40`): LINK restatement rule (CtlCJunkLines), TOPIC strong/weak split (CtlCOffTopic), NFKC and spaced ids (CtlCMultiId), FRESH query/fragment/mobile strip (CtlCCopiedRows), echo/base64/private-host refusals (CtlCEchoUrls, MutCounterC), O selftest clause dropped and tool run outside the lane (CtlOSelftest, CtlOKeyed, CtlOHonest), lookalikes beside real ids (CtlOParsing), ERR no-args (CtlODoNothing). L1 re-score receipts `reports/round-61/telemetry/controls-c-rescore.txt`, `controls-o-rescore.txt` (a subset; the other forcing receipts are the wave-1 reports committed at the freeze).
- Build: ten scribes opened 42 sources; 41 registered as S652-S692 (`corpus/SOURCES.md`, landed `efbee29c`), one rejected (Gate below). Entry assembled with six anchor groups and a six-decision table; README row and totals 235 → 236.
- O build: ExecLintTool wrote the tool (selftest 26/26), landed `675d59af` after one docstring edit that removed the string `round-61` (revision 1's INDEP list).
- Measurement: `reports/round-61/telemetry/final-measures.txt` — the first and sole authoritative runs at `efbee29c`.
- Falsify (wave 2, 47 seats): 41 one-row one-clause reviewers (S652-S692), ReviewLocateS671, CriticFreezeC, MutToolO, ReviewRerunO, CriticClaimO, ReviewContainment (`.ufo/waves/round-61/w2/`). Findings in `corpus/lessons/round-61.md` `## Falsify wave findings`.
- Records: QUALITY criterion 15 (clause-scoped cited lines; scope narrowed after CriticClaimO), lesson with Gate, mistakes R61-M1..M7, routed defects; landed `ae8e393e`, `c587cd57`.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `106df397` | instruments revision 0, claims, base list, census start | round 61 entry |
| `78ad4b17` | separability manifest, declaration dry-run receipt | round 61 entry |
| `2f4f8a40` | revision 1 (freeze), control receipts, wave-1 spec and reports | round 61 entry, "Pre-data controls" |
| `675d59af` | claim O: `tools/check-cited-lines.py` | round 61 entry, "Claims" |
| `efbee29c` | claim C: footwear entry, S652-S692, README row | round 61 entry, "Claims" |
| `ae8e393e` | lesson, QUALITY 15, SCORECARD, LOG, round-60 corrections, final measures, separability, census end, kind-cell fix | round 61 entry, "Records" |
| `c587cd57` | wave-2 reports and registry, falsify findings and errata, QUALITY 15 wording, SCORECARD wording | round 61 entry, "Waves" |

## Before → after measurements

- **C** — `python3 -B reports/round-61/accept-c.py`. Before (observed at revision 0 `106df397`, `declaration-dry-run.txt`): `ACCEPT-C-61: FAIL` (SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE). After at `efbee29c` (`final-measures.txt`): SET, SWEEP, FLOOR (`cited=41`), RANGE, STATUS, OPENED, USEDBY, ACCESS, LINES, TOPIC, LINK, COPY, FRESH PASS; `LOCATE FAIL located=40 cited=41 need=41 at=2026-10-23T09:58Z not_located=['S671: https://americanindian.si.edu/collections-search/object/NMAI_26904 HTTPError; https://web.archive.org/web/20250612214229id_/…` ; `ACCEPT-C-61: FAIL`, exit 1. **MISSED** under the frozen kill rule; nothing amended. Cause (ReviewLocateS671): the live URL is a Cloudflare challenge (403, met not passed) and the row's single Wayback capture erred at measure time while the archive was rate-limiting; the capture locates on later diagnostic runs, which do not change the verdict. The declared separability check later re-ran C's acceptance in a temporary copy (10:02Z) without a `C-><base>` finding; that is a dependency check, not a receipt.
- **O** — `python3 -B reports/round-61/accept-o.py`. Before (revision 0, tool absent): `ACCEPT-O-61: FAIL` (all six legs). After at `efbee29c`: TOOL, INDEP, GEN (92/92), CLEAN, ERR (missing 2, invalid UTF-8 2, no args 2), REAL (603/603, amulets line 95 `S612,S613` in the reference) PASS; `ACCEPT-O-61: PASS`, exit 0. ReviewRerunO: 5/5 PASS on an independent clone.
- Separability: `python3 -B tools/check-claim-separability.py reports/round-61/separability-manifest.json` → one finding `O->C via export` (the literal `S652` in the tool's selftest case at `tools/check-cited-lines.py:152` matches C's id-block regex; a fixture id, not a citation); no dynamic dependency (`reports/round-61/telemetry/separability.txt`).

## Sources & frontier

- Rows: `git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'` → 577 at `942abdf4`, 618 at `c587cd57`. Added by tier: A 27, B 13, C 1 (S687, the sole support of its line: a QUALITY defect routed to round 62). All 41 `mined`, opened 2026-10-23, used-by the footwear entry.
- Rows touched old→new: none outside the new block; three new rows' kind cells corrected `news` → `docs` before filing (S655, S658, S681; R61-M7).
- Census: start `exit=0` (`reports/round-61/telemetry/census-start.txt`); end run 1 `exit=1` (three E05 kind lines), run 2 `exit=0` after the kind fix (`census-end.txt`, both runs kept).
- Frontier advanced: footwear moved from frontier to a landed (not admitted) entry; sourced claim C rests on S652-S692.
- Mined mistakes: R61-M1..M7 (`corpus/lessons/round-61.md` `## Mistakes`).

## Trend verdicts

- **expansion: unchanged** — the surface moved (knowledge files 235 → 236, 41 opened rows), but claim C missed its frozen predicate, so no admitted expansion.
- **quality: improved** — claim O passed: the lane gained a runnable lint for the R60-M6 defect (603 base findings, 0 on the new entry), backed by QUALITY criterion 15 and shown able to fail (exit 1 on the amulets entry).
- **discernment: improved (author-side)** — ten pre-data controls met revision 0 and each forced a change before data; the one-row one-clause review found two real over-reaches (S666 dropped hedge, S692 closed list) and one caption-only quote (S665) that the mechanical legs passed; the round-60 corrections also corrected two figures in the outside spot-check; the miss is reported under the frozen rule.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:5`; no non-author verifier on record.
- [~] End-to-end domain task logged — `LOG.md` round 61: source opening → entry → frozen measure (missed on one fetch) plus a landed tool (passed). No non-author verifier.
- [~] Instructions executable without oral context — wave-2 seats worked from one row and one clause each (`.ufo/waves/round-61/w2/Row*.md`). No non-author verifier.
- [~] No cross-domain bleed — ConnectSiblings found no sibling owner of footwear or a cited-line lint (`.ufo/waves/round-61/w1/ConnectSiblings.md`); the entry hands canon to lore (§5). No non-author verifier.

## Gate

The lesson's `## Gate` lists all 41 new rows with URL, access date and quote. Real rejects this round:

- Bata Shoe Museum Arctic-footwear quote "Traditional designs are geometric but more contemporary boots feature highly curvilinear patterns." — not registered: homonym-prone `boots` only (TOPIC revision 1) and a 4-content-word clause (LINK minimum 5).
- Web Japan Nipponia (403), Smithsonian bound-feet shoes (403, no capture), UBC `kamiik` search URL (locator `search-url` refusal) — not used.
- Review-only rejects in wave 2: S666 CLAUSE NOT-SUPPORTED (hedge "we have" dropped), S692 CLAUSE NOT-SUPPORTED (closed an "etc." list), S665 QUOTE NOT-LOCATED as body text (caption only). Recorded, not repaired (the measured entry stays as landed); routed to round 62.
- Pre-data: ten controls met revision 0 (listed above) and were rejected by revision 1; CtlCQuoteDump, CtlCNoReader and CtlOKeyed a2 remain declared residuals (`claims.json` `known_residuals_after_controls`, `review_only`).

## Round shape and seats

Shape: default two v1 waves. Wave 1 (controls + build) 36 seats: 12 scribe, 11 mutation-tester, 9 executor, 1 scout, 1 connector, 1 critic, 1 reviewer. Wave 2 (falsify) 47 seats: 44 reviewer, 2 critic, 1 mutation-tester. No residual call. Round total 83. Planner seat: the L1 (validator rejects `planner`); the planning data-walk rode ScoutOwners. Dead seats: none; refusals: none. Wave 1 was first sized at 42 and waited 3600 s at the gate (`live_estimate` 62 of cap 100) before being re-sized to its 36 genuine items (R61-M6).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. `pypdf==5.4.0` ran ephemerally through `uv run --no-project --with` (existing uv) inside the frozen locator during the L1's counter runs and in seats ScribeSrc04, ScribeSrc10, CtlCHonestPdf, RowS664, RowS682; no pacman transaction.
- Misroot sweep: ScribeSrc01 wrote its report to the fleet root; copied byte-exact to the lane (`cmp` 0), fleet copy deleted (R61-M5). Other untracked fleet-root files predate this round and carry no kotodama round-61 content (ReviewContainment).
- Open L0 questions: none new (freshness stays paused by the round-11 question).
