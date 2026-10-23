# kotodama — round 60 (hyaku phase 4, attempt 3, L1 KotodamaR60A3)

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `9c82a6eb`, lane tip `dc149b039efe8dd2025cf16430024f2c160dc608` (pushed; `jj-lane.sh state`: local=remote, ahead=0, tracked=0, untracked=0).

## Work performed

Declared claim: **one measured claim, D (depth, sourced, S648-S651)** — the amulets entry `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` re-entered under a new pre-data freeze, its four round-59 over-reach propositions restored in source-scoped wording, the whole 47-id entry re-judged by blind seats under ACCEPT-D-60 (`reports/round-60/accept-d.py`, predicate in `reports/round-60/claims.json`). Plus routed repairs of the round-59 spot-check (records, not claims). **Verdict: D MISSED** (ACCEPT-D-60 FAIL at the measured revision).

- Inherited state: attempts 1-2 had landed revisions 0-4 (`b60e6d4e`..`f39e5ea2`); their uncommitted build (entry edits, rows S648-S651, captures, 35 wave reports, specs) was treated as untrusted scratch. Captures re-fetched byte-identical (`reports/round-60/telemetry/captures-refetch.txt`); every entry line re-audited by 16 fresh seats; attempt-2 reports and specs moved out of the lane uncited (`dc149b03`).
- Counter revisions 5-9, each before any data seat and each forced by a committed receipt: revision 5 CONFINED allow-list (`14e64138`); 6 exact 24-seat roster + dissent scan over every frozen seat after CtlNarrowA3 CONTROL-MET (`b9faed93`); 7 EVIDENCE (a SUPPORTED verdict must quote >= 10 words of the row's pinned page text not in its packet) after CtlKeyedLabelA3 CONTROL-MET (48/48 planted found by a packet-only program) (`b9faed93`); 8 novelty and page-specific spans after MutEvidenceA3 CONTROL-MET (`09be1e16`); 9 `\/` deny after RescoreConfineA3 (`a56b04fc`). Rationale for each: `claims.json` `revision_note_5`..`_9`.
- Pre-data control receipts: wave 1 `.ufo/waves/round-60/w1-a3/` (40 seats, scored revision 5); residual call `.ufo/waves/round-60/resid-a3/` (6 seats; revision-7 and revision-9 re-scores all NONE-MET: RescoreNarrowA3-r9, RescoreKeyedLabelA3-r9, CtlLaneReaderA3-r9, RescoreConfineA3-r9); L1 function-level re-score of MutEvidenceA3's fixtures under revision 8 (`reports/round-60/telemetry/evidence-r8-rescore.txt`: packet-only generator 3/141 → 0/141 counted).
- Build `1cd9db7c`: S648-S651 rows and lines (S648 rescoped to "The IDD article" after AuditA3R15); 19 base lines narrowed per AuditA3R01-R16 and ScoutPlacementA3; 47 cited pages pinned as text (`reports/round-60/captures/pages/`).
- Freeze `47f27bd0` (`freeze_note`; packet-key hash `reports/round-60/planted-key.sha256`, key kept outside the lane until the wave settled).
- Data: support wave (24 blind Support seats + 11 falsify seats), final measure `reports/round-60/telemetry/final-measure.txt`: SET, LINES, OLDWORD, ROWS, PINNED, JUDGED PASS; **SUPPORT FAIL** — 14 NOT-SUPPORTED on mapped ids (S612 ×3, S613 ×3, S646 ×2, S604, S610, S615, S628, S631, S649 unreachable), 13/24 seats qualified (11 voided by CONFINED: 5 `deny:chr(`, 5 `bash-cwd-outside-sandbox`, 1 `kotodama`). Nothing amended; the judged entry stays as built.
- Routed round-59 spot-check defects 1-6: SCORECARD correction table and LOG correction entry (C MISSED; separability artifact), round-59 errata (R59-M5, CtlKeyedLabels59 dropped with reason, registry label, run 2 FAIL), QUALITY criterion 14 (`tools/check-judged-object.py`, shown failing on round 59's bytes); `__pycache__` removed (`reports/round-60/telemetry/pycache-removed-a3.txt`). ReviewRecordsA3: all six routed (`.ufo/waves/round-60/support/ReviewRecordsA3.md`).

## Landed changes

| commit | change | LOG |
|---|---|---|
| `14e64138` | revision 5 | LOG round 60 |
| `b9faed93` | revisions 6-7, pinned pages, wave-1 receipts | LOG round 60 |
| `1cd9db7c` | claim D build (entry, S648-S651, captures) | LOG round 60 |
| `09be1e16` | revision 8 | LOG round 60 |
| `a56b04fc` | revision 9, L1 evidence re-score | LOG round 60 |
| `47f27bd0` | freeze; records (SCORECARD/LOG corrections, errata, QUALITY 14, lesson) | LOG round-59 correction + round 60 |
| `dc149b03` | support verdicts, final measure, separability, census end, records | LOG round 60 |

Earlier round-60 commits by dead attempts: `b60e6d4e`, `0e494ff2`, `819bf084`, `1f04b2d7`, `35de1f9c`, `f39e5ea2`.

## Before → after measurements

- Claim D: `python3 -B reports/round-60/accept-d.py` — FAIL at the claim base `b9faed93` (SET, LINES, ROWS, PINNED, JUDGED, SUPPORT; `reports/round-60/telemetry/before-measure.txt`) → **FAIL** at the measured revision `dc149b03` (SUPPORT only; `final-measure.txt`, counter sha256 `cf068177…`). Target PASS not reached: **MISSED**.
- Separability: `python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json` (base `b9faed93`) → 1 finding, `D-><base>` (D fails on its own lands; no D→REC dependency) (`reports/round-60/telemetry/separability.txt`).

## Sources & frontier

- `corpus/SOURCES.md` rows 573 → 577 (`git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'` at `9c82a6eb` and `dc149b03`); added S648 (paper, B), S649 (docs, A), S650 (docs, B), S651 (docs, A), all mined, used-by the amulets entry, each superseding a round-59 rejected row on the same page; Gate lines with URL, access date and quote in `corpus/lessons/round-60.md` `## Gate`. Rows touched old→new: none (S602/S616/S623/S643 stay rejected).
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`: start exit 0 (`reports/round-60/telemetry/census-start.txt`), end exit 0 (`census-end.txt`; W04 warnings only).
- Mined mistakes: R60-M1..M7 (`corpus/lessons/round-60.md` `## Mistakes`); sourced claim: D rests on S648-S651.

## Trend verdicts

- expansion: **unchanged** — no new entry or file (235 knowledge files before and after); four rows added only as superseding rows.
- quality: **unprovable-but-better** — 19 base lines narrowed to their pages and four propositions restored without the rejected over-reach (pre-freeze audits; ReopenRowS648-S651A3 HOLDS), but the blind SUPPORT leg failed, so no admitted improvement.
- discernment: **improved (author-side)** — five pre-data controls met earlier counters and forced revisions before data; planted controls were rejected by every qualified seat; the miss is reported under the frozen rule with no post-verdict change.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:5`; no non-author verifier on record.
- [~] End-to-end domain task logged — LOG round 60; chain audit → freeze → blind support → frozen measure (missed). No non-author verifier.
- [~] Instructions executable without oral context — support seats worked from packets only (`.ufo/waves/round-60/support/`). No non-author verifier.
- [~] No cross-domain bleed — ConnectSiblingsA3 found no sibling owner (`.ufo/waves/round-60/w1-a3/ConnectSiblingsA3.md`). No non-author verifier.

- discernment: **improved (author-side)** — three pre-data controls met earlier counters (CtlNarrowA3, CtlKeyedLabelA3, MutEvidenceA3) and a fourth seat found an evasion (RescoreConfineA3); each forced a revision before data; planted controls were rejected by every qualified seat; the miss is reported under the frozen rule with no post-verdict change.

Real rejects this round: 14 NOT-SUPPORTED verdicts on real ids (e.g. SupportD60 P05 on S612: "entry claim 'tälsäm boxes were strung as a necklace' appears nowhere in the API record"; SupportN60 P04 on S649: unreachable, live 429 and Wayback refused); every qualified seat rejected its two planted blocks (e.g. SupportT60 P02, an invented "Jayavarman VII of Angkor" clause). Pre-freeze: 16 audit seats rejected wording on 15 base lines (rewritten before the freeze) and flagged 7 teaches cells (S601, S608, S614, S624, S636, S640, S641) kept by the append-only registry and disclosed before data.

## Round shape and seats

Shape: default two v1 waves plus one residual call. Wave 1 (build + pre-data control) 40 seats: 15 critic, 12 reviewer, 7 mutation-tester, 3 executor, 1 scribe, 1 scout, 1 connector. Residual call 6 seats (4 critic, 2 reviewer). Wave 2 (support + falsify) 35 seats: 29 reviewer, 5 scout, 1 critic. Round total 81. Planner seat: the L1 (canonical §3 seat); the planning data-walk rode ScoutPlacementA3. Dead/refused seats: CtlKeyedLaneA3 refused (`cyber_policy`, hold, replaced by a differently designed CtlLaneReaderA3); MutEvidenceA3's revision-8 re-score turn refused (`cyber_policy`, hold; its first report stands; L1 re-scored its fixtures). SupportU60 and SupportX60 self-reported tool-rule breaches (`multi_tool_use.parallel`) and are voided by the counter. No other seat died.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1. Seats reported none, except RescoreMechA3 and MutEvidenceA3, which materialised `pypdf==5.4.0` through `uv run --with` into their sandbox caches (`uv` 0.13.0, existing); no pacman transaction.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists untracked fleet-root files (`live_s228.html`, `nama.html`, `s395.txt`, `tf_bavelas.html`, `wb2.html`, `bm.json`, `write`), all dated 2026-10-21/22 with no kotodama or amulet content: not written by this round's seats, left untouched.
- Open L0 questions: none new (freshness stays paused by the round-11 question).
