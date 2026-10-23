# kotodama — round 62 report (hyaku phase 4, attempt 1, L1 KotodamaR62)

Lane base `d42ffb89`; lane tip `2ce9d4d1544763ecbc89bdd2bca88dfd11d18473` (pushed; `jj-lane.sh state`: local = remote, ahead 0). Instruments revision 0 `f0173481`; revision 1 `e6a61e82`; freeze `9143fc44`; O landed `e605603c`; D landed `a2c5caa5` (measured revision); receipt `25b44b8a`; records `2ce9d4d1`.

## Work performed

Declared claims (`reports/round-62/claims.json`, frozen at `9143fc44`):

- **D — depth (sourced claim, S693):** repair in place the four footwear-entry lines the round-61 closure routed (`corpus/lessons/round-61-verifier-spotcheck.md` §7 item 1): line 63 (S692 closed list), 74 (S665 caption), 75 (S666 dropped hedge), 93 (S687 tier C as sole support → new tier-B row S693). Predicate `ACCEPT-D-62: every leg above prints PASS.` (16 legs). **Author verdict: PASS.**
- **O — operability (capability acquisition):** `tools/reopen-row.py`, a bounded row re-opener with archived-copy fallback and a body-versus-caption verdict (the S671 transient and S665 caption classes of round 61). Predicate `ACCEPT-O-62: every leg above prints PASS.` (9 legs, offline random fixture only). **Author verdict: PASS.**

Anti-loop: rounds 58-61 failed on new or rebuilt sourced entries judged by a no-slack live LOCATE or a blind SUPPORT leg. This round opened no new entry, ran no support leg as a predicate, gave D's only live leg (one new row) a bounded treatment frozen before data (three passes 60 s apart over three attempts per URL, a same-page capture in each row) with its own paired control (`reports/round-62/locate-control.py`), and judged O on an offline fixture.

Work items:

- Repair first (round-61 spot-check §7, items 1-5): dispositions in `corpus/lessons/round-62.md` `## Spot-check intake`; item 1 is claim D; item 2 recorded as an appended note (S655/S658/S681 `news` → `docs`, no cell edited again); item 3 by a SCORECARD correction row and the LOG round-62 entry (R61-M1..M7); item 4 by O's ORDER leg (argument order including repeated ids); item 5 by QUALITY criterion 16 plus D's paired LOCATE control. Landed `2ce9d4d1`.
- Instruments revision 0 (`f0173481`): `accept-d.py`, `accept-o.py`, claims, separability manifest, census start, dry run.
- Pre-data control wave (wave 1, 37 seats): twelve controls met revision 0, each forcing a revision-1 change before any data (`e6a61e82`): CtlDMarkOnly (hidden comments/parentheticals, full PASS), CtlDJunkTokens (token salad), CtlDRegistryEdits (S688 URL reuse, full PASS; `| S650b |`), CtlDCaptureShapes and CtlDFabricated fxB (different-page/bare/future captures), CtlDOffTopicRow (Hermes spaceplane, full PASS), MutCounterD (CR on line 1), CtlOOrderErr (de-duplication, full PASS), CtlODefault and CtlONoRetry caseC (schedule), CtlOUnbounded c5/c10/c11, ExecReopenTool's live S665 run (thumbnail caption). L1 re-score: `reports/round-62/telemetry/controls-rescore.txt` (24 receipts: every listed fixture FAIL under revision 1; honest positives PASS). Errata: three O guards came from source inspection, not executed controls (lesson `## Errata`, ResidCriticFreeze).
- Build: ExecReopenTool wrote the tool (selftest 32/32), landed `e605603c`; the scribes drafted lines 63/75 (ScribeHedgeOpen), 74 (ScribeHeelCaption) and talaria candidates (ScribeTalariaMW, ScribeTalariaRef); the L1 registered S693 from Dictionary.com (live-readable), landed `a2c5caa5`.
- Measurement: `reports/round-62/telemetry/final-measures.txt`, the first and sole authoritative runs at `a2c5caa5`.
- Residual falsify call (8 seats, `.ufo/waves/round-62/resid/`): both counters reproduced (ResidRerunD, ResidRerunO ×2), the four lines SUPPORTED by one-line reviewers, freeze integrity held (ResidCriticFreeze), and the tool review found a HIGH redirect SSRF (ResidToolSecurity) outside the predicate, routed to round 63.
- Records: QUALITY criterion 16, lesson with Gate, mistakes R62-M1..M5, routed defects; SCORECARD capability row and round-62 section; LOG entry. Landed `2ce9d4d1`.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `f0173481` | instruments revision 0, claims, manifest, census start, dry run | round 62 entry |
| `e6a61e82` | revision 1 (before data), LOCATE paired control and receipt, re-score receipts, wave-1 spec, registry, 37 reports | round 62 entry, "Pre-data controls" |
| `9143fc44` | freeze: claims and manifest at revision 1, revision-1 dry run | round 62 entry, "Pre-data controls" |
| `e605603c` | claim O: `tools/reopen-row.py` | round 62 entry, "Claims" |
| `a2c5caa5` | claim D: footwear lines 63/74/75/93, S693, S687 used-by → `—` | round 62 entry, "Claims" |
| `25b44b8a` | final measures | round 62 entry, "Claims" |
| `2ce9d4d1` | lesson, QUALITY 16, SCORECARD, LOG, census end, residual reports | round 62 entry, "Records" |

## Before → after measurements

- **D** — `python3 -B reports/round-62/accept-d.py`. Before, at the freeze (`declaration-dry-run-rev1.txt`): `ACCEPT-D-62: FAIL` (SET, OPEN, HEDGE, CAPTION, SOLE, ROWS, LOCATE). After at `a2c5caa5` (`final-measures.txt`): all 16 legs PASS (`SET differ=[63, 74, 75, 93]`, `SOLE id=S693 tier=B`, `LOCATE located=1 cited=1 at=2026-10-23T12:05Z`), `ACCEPT-D-62: PASS`, exit 0. Reproduced by ResidRerunD (byte-identical except the timestamp).
- **O** — `python3 -B reports/round-62/accept-o.py`. Before at the freeze: `ACCEPT-O-62: FAIL` (no tool, nine legs). After at `a2c5caa5`: TOOL, INDEP, GEN (53/53), ORDER (repeats 5/5), BOUND (no unlisted request), EXIT (incl. default registry), PRIV, DEFAULT (9 requests, bursts [3, 3, 3], gaps 60/60 s, 150 s), ERR PASS; `ACCEPT-O-62: PASS`, exit 0. Reproduced twice by ResidRerunO.
- LOCATE paired control: `python3 -B reports/round-62/locate-control.py` → `LOCATE-CONTROL-62: PASS` (6 cases), and FAIL on a PASSES = 1 copy (`telemetry/locate-control.txt`).
- Separability: `python3 -B tools/check-claim-separability.py reports/round-62/separability-manifest.json` ran only in the dry runs (exit 2 at the absent O land, as declared); not re-run after landing — an unrun check, not a pass.

## Sources & frontier

- Rows: `git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'` → 618 at `d42ffb89`, 619 at `2ce9d4d1`. Added by tier: B 1 (S693, Dictionary.com `talaria`, mined, opened 2026-10-23, used-by the footwear entry, live URL plus a 2024-05-29 same-page capture).
- Rows touched old→new: S687 used-by `corpus/knowledge/culture-material/footwear-codes-terminology.md` → `—` (census W01 → W03); logged in the lesson.
- Census: start `exit=0` (`reports/round-62/telemetry/census-start.txt`); end `exit=0` (`census-end.txt`), also run on the landing tree before `a2c5caa5`.
- Frontier advanced: the footwear entry's routed lines repaired; the caption/label backlog (S673, S661, S663, S677, S161; ScoutCaptionRows) routed for the new tool.
- Mined mistakes: R62-M1..M5 (`corpus/lessons/round-62.md` `## Mistakes`).

## Trend verdicts

- **expansion: unchanged** — no new knowledge surface (236 files); one row added for a repair.
- **quality: improved (author-side)** — four routed overstatements repaired and judged SUPPORTED by one-line non-author reviewers; tier-C sole support removed; a runnable re-opener with archived fallback and caption verdict (ACCEPT-O-62 PASS). Disclosed against it: the tool's HIGH redirect SSRF, found after measurement and routed, not repaired.
- **discernment: improved (author-side)** — twelve pre-data controls met revision 0 and each was closed before data; the counters were never changed after the freeze (ResidRerunD); the provenance overstatement for three guards is recorded as an erratum.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:5`; untouched this round; no non-author verifier.
- [~] End-to-end domain task logged — `LOG.md` round 62: routed defect → sourced repair → frozen measure (PASS) → one-line review. No non-author verifier.
- [~] Instructions executable without oral context — residual seats worked from one line and one row each (`.ufo/waves/round-62/resid/`). No non-author verifier.
- [~] No cross-domain bleed — ConnectSiblings: nearest prior art `chousa-shokunin/tools/quote-reopen.py`, no sibling owner of footwear or talaria (`.ufo/waves/round-62/w1/ConnectSiblings.md`). No non-author verifier.

## Gate

The lesson's `## Gate` carries S693 with URL, access date and quote. Real rejects this round:

- Merriam-Webster `talaria`: live page `403` to an ordinary request (`curl … -w '%{http_code}'` → `403`; locator `NOT_LOCATED … HTTPError`, `ScribeTalariaMW.md:49`); a capture-only row under the observed Wayback 429s was refused.
- Cambridge Farnese Hermes cast: the quote does not name talaria; its capture failed the locator (`ScribeTalariaRef.md:41`).
- BBC "Why did men stop wearing high heels?" (S695 draft): not registered; line 74 repaired by caption attribution instead.
- Collins and Britannica `talaria`: `403`; not used.
- Pre-data: the twelve revision-0 counter designs met by controls (above) were rejected by revision 1.

## Round shape and seats

Shape: default v1, one wave plus residual. Wave 1 (controls + build) 37 seats (`.ufo/waves/round-62/w1-spec.json`): mutation-tester 16, executor 9, scribe 7, critic 2, reviewer 1, scout 1, connector 1. Wave 2 not dispatched: its genuine attack items were fewer than 32, so one residual `task` call of 8 seats (reviewer 7, critic 1). Round total 45. Planner seat: the L1 (validator rejects `planner`). Dead seats: none. Cancelled at the settle deadline: CtlDHonest and CtlONoRetry (~66 min; both had written their reports, which are kept). Refusals: none. The residual call carried a `solutionSpace` field per task, added by the L1 because the task tool requires it; wave 1 likewise (the validator's `context`/`task` text unchanged).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. No pacman transaction.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked fleet-root files; none names kotodama or round 62 (`0` at 12:09Z holds `NF=13 cells=11 double_quotes=0`; `xc.xml` at 11:03Z is a Perseus rate-limit page) — not attributable, left untouched.
- Open L0 questions: none new (freshness stays paused by the round-11 question).
