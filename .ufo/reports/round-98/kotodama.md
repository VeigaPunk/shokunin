# kotodama — round 98 report (hyaku run 15, attempt 2)

Lane: kotodama (linguistic-cultural worldbuilding). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Lane HEAD at landing: `7ff35e6ce6a8027fd04ba4a6bccce179b7286ca3` (branch `main`). `git ls-remote origin refs/heads/main` → `7ff35e6ce6a8027fd04ba4a6bccce179b7286ca3`.
Base `bcf664aa089ddbd1fac85772ed22a38d1b454d23`. Freeze `db88f107606aae90efe01344551c7e1ea71cd419`, made by attempt 1 before any seat ran. Round commit `7ff35e6c`.
Attempt 1 (L1 `KotodamaR98`) ended mid-work (`.ufo/watchdog.log`: `lane-dead-no-report kotodama round=98`, 23:31:14). This attempt (L1 `KotodamaR98a2`) inherited its outputs, re-verified them, and landed the round.

## Work performed

Declared claims (`reports/round-98/claims.json`; 2 claims on distinct axes; causally separable; frozen by attempt 1 and not changed):

- **Claim O — operability** (successor grader move v9 → v10). It closes the five CriticO97 forgeries that pass v9 without a named refusal: DEL1 (U+007F), ENC1 (U+20DD), ROMAN1, SUP1 and FWPER1. Before the freeze these measured `CRITIC-O97 survivors=8` (`reports/round-98/controls/critic97-on-v9.txt`) and battery98 over v9 `survivors=5 refused=31` (`controls/battery98-control-v9.txt`). Target: legs O0–O5.
- **Claim C — coverage** (sourced frontier → core entry on toasts and drinking-speech formulae). At base no topic line or heading owns this surface (C8 owners=0). Target: legs C1–C9.
- **Lowest-axis note:** freshness is the lowest non-retired axis. It stays paused by the open L0 round-11 and round-89 questions. No claim this round moves freshness, so the obligation is neither met nor waived.

Work items. Wave dirs are `.ufo/waves/round-98/w1/` and `w2/`. Each seat's report is `<wave>/<Seat>.md` and its stage is `<wave>/stage/<Seat>/`.

1. **Freeze (attempt-1 L1, re-verified).** Counter `reports/round-98/predispatch.py`. Do-nothing control `predispatch-base.txt` → `PREDISPATCH-98: FAIL legs=5/15`. Forgery and positive controls are in `controls/forgery-summary.txt`: F-O-SHA fails O1/O2/O5, F-C-JUNK fails C3/C7, F-C-DUP fails C7, P-C-BOUND passes C7, P-C-REOPEN passes C9. battery98, its pin and its v9 receipt are all in freeze commit `db88f107` (round-97 routed defect 2). ReviewerO98b confirmed this with `git log` per path.
2. **ExecGraderV10 (w1).** Wrote grader v10 (`d35b13c9…`) with new checks `VERDICT-CTRL` (Cc incl. DEL), `VERDICT-COMBINE` (M*) and a non-ASCII numbering strip in heading tokens. Selftest 161/161, battery98 0/0/36/0/3/0 (`w1/ExecGraderV10.md`).
3. **MutationTester98b (w2, attack).** Took over the unpinned draft `mutants98.py` left by the dead seat: 128 mutants, every pattern re-verified against v10, no edits needed. Pinned it before measuring (`controls/mutants98.sha256`, `dd88caec…`). First measurement: `MUTATION-SCORE: 128/128 killed, 0 survived, 0 broken-pattern` (`controls/mutation98-first.txt`). Red-before over v9: 117/128 with 11 broken patterns (`w2/stage/MutationTester98b/red-before-v9.txt`).
4. **CriticO98b (w2, attack).** Tried 25 fresh classes: `CRITIC-O98 survivors=24 unnamed=0 refused=1` on v10, and the same 24 on v9, so none is a v10 regression. It also found one **over-refusal regression**: an h2 heading with an Mc mark is CLEAN on v9 and refused on v10 (`w2/stage/CriticO98b/attacks.md`).
5. **ReviewerO98b (w2, attack, non-author).** Ran the frozen counter: `PREDISPATCH-98: PASS legs=15/15`, rc 0. It checked the pin, receipt and commit-order table, ran shadowed-branch probes on the 7 new branches, and confirmed that battery97 over v10 still gives 0/0/31. Findings: F1 (medium, `HEADING-NUMBER` refuses a bare non-ASCII-numeral heading that cannot anchor), F2 (dead branch), F3 (unpinned load-bearing branch), F4 (medium, Mc heading over-refusal), F5 (generic TOPIC name). **Verdict: claim O PASS, first failing leg none.** (`w2/ReviewerO98b.md`)
6. **ScoutSurface98 / ConnectorOverlap98 (w1).** Content sweep found 0 owners. No sibling lane claims the surface. Nine in-lane boundaries are assigned (`w1/stage/ConnectorOverlap98/overlap.md`).
7. **ScoutSources98 (w1).** Opened 26 candidates: 11 admitted (tier A 6, B 5), 15 rejected, each with HTTP status and a flip condition (`w1/stage/ScoutSources98/candidates.md`).
8. **ExecRegistry98 (w1).** Sole registry writer. Appended S994–S1004 and S1005, which supersedes S992 (round-97 routed defect 1). Census rc 0. Wrote the manifest in `reports/round-98/evidence/manifest.json`.
9. **ScribeEntry98 (w1).** Wrote the entry `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` (13 h2, decision procedure, error patterns, checklist) and the README index row.
10. **ReviewerC98 (w1, attack, non-author).** C1–C9 PASS. Re-opened 11/11 sources by plain curl (HTTP 200, count 1, `stage/ReviewerC98/reopen.json`). In a 28-sentence support sweep, 27 sentences were supported and one was contradicted (line 142, S999).
11. **CriticC98 (w1, attack).** Claim C survives. It found F1, an "Oceanic" word in S994's teaches cell that no capture grounds, and F2, a one-word misquote of S996.
12. **ReviewerOath98 (w1).** Sentence-support sweep of the round-96 oath entry (round-97 routed defect 5): of 22 sentences, 11 supported, 3 weak, 5 unsupported, 3 contradicted (`stage/ReviewerOath98/support.md`).
13. **ExecGateCaps98 (w1).** Wrote a new tool, `tools/check-gate-captures.py` (selftest 13/13), for round-97 routed defect 3. On the round-97 lesson it fails with 9 findings. On this round's lesson it passes with 0 findings in 13 rows (`reports/round-98/gate-captures-lands.txt`).
14. **L1 integration repairs**, made after the seats and before landing; no counter bytes were touched:
    - Entry line 142 rewritten on two S999 quotes, each count 1.
    - The "so much as" quote fixed.
    - §8 table preamble now marks unquoted cells as design, and the §13 ledger preamble is corrected.
    - S1006 supersedes S994 (the teaches-cell fix).
    - 8 oath-entry sentence repairs, each new quote count 1 in its round-96 capture (`grep -c -F`).
    - QUALITY criterion 40 added.
    - README sentence corrected (tiers and the two supersedes).
    - Lesson, LOG and SCORECARD written.
    The 8 oath repairs and S1006 were drafted by attempt 1 and re-verified here.

Round shape and seat mix:

- One v1 wave `w1` of 13 seats (validated, `w1-spec.json`/`w1-dispatch.json`) plus one residual call `w2` of 3 seats (`w2-dispatch.json`). Round total: 16 seats.
- w1 roles: executor 3, mutation-tester 1, critic 2, reviewer 3, scout 2, connector 1, scribe 1.
- w2 roles: mutation-tester 1, critic 1, reviewer 1.
- Attack seats: 7 of 13 in w1 (54%), 3 of 3 in w2.
- **Dead seats: 3.** MutationTester98, CriticO98 and ReviewerO98 (w1) died with the crashed orchestrator session. They left no report, `w1-results.json` shows output null, and they are counted as no evidence. The w2 seats replaced them. No w2 seat died.
- WAVE-DONE was received for both waves.
- Planner: the L1 holds the canonical planner seat. The planning data-walk rode ScoutSurface98 and ConnectorOverlap98.

## Landed changes

| change | file(s) | LOG entry | commit |
|---|---|---|---|
| freeze: claims, counter, do-nothing and forgery controls, battery98 + pin + v9 receipt, critic97-on-v9, census-start | `reports/round-98/{claims.json,predispatch.py,predispatch-base.txt}`, `reports/round-98/controls/*`, `.ufo/waves/round-98/census/census-start.txt` | round 98 | `db88f107` |
| claim O: grader v10 | `tools/check-advance-evidence.py` | round 98 | `7ff35e6c` |
| claim O: mutation driver, pin, first receipt | `.ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py`, `reports/round-98/controls/{mutants98.sha256,mutation98-first.txt}` | round 98 | `7ff35e6c` |
| claim C: entry | `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` | round 98 | `7ff35e6c` |
| claim C: registry S994–S1006 (S1006 supersedes S994, S1005 supersedes S992; S992 in place status/used-by only) | `corpus/SOURCES.md` | round 98 | `7ff35e6c` |
| claim C: index row, count and section | `corpus/README.md` | round 98 | `7ff35e6c` |
| routed r97-1: S992 citations re-pointed to S1005 | `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` | round 98 | `7ff35e6c` |
| frontier: oath entry repairs (8 lines) | `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` | round 98 | `7ff35e6c` |
| frontier: gate-capture checker; criterion 40 | `tools/check-gate-captures.py`, `corpus/QUALITY.md` | round 98 | `7ff35e6c` |
| lesson, scorecard, log | `corpus/lessons/round-98.md`, `SCORECARD.md`, `LOG.md` | round 98 | `7ff35e6c` |
| evidence: captures, manifest, lands receipts, waves w1/w2, census-end | `reports/round-98/**`, `.ufo/waves/round-98/**` | round 98 | `7ff35e6c` |

## Before → after measurements

Counting command for all legs (frozen counter): `python3 -B reports/round-98/predispatch.py --root <lane> --work <scratch> --base-rev bcf664aa089ddbd1fac85772ed22a38d1b454d23`. Before = base `bcf664aa` (`predispatch-base.txt`). After = landed tree `7ff35e6c` (`reports/round-98/predispatch-lands.txt`, `PREDISPATCH-98: PASS legs=15/15`, rc 0). ReviewerO98b reproduced 15/15 independently.

| claim | leg | before | after |
|---|---|---|---|
| O | O0 sha ≠ v9 | FAIL | PASS `d35b13c9…` |
| O | O1 selftest ≥160 | FAIL 155/155 | PASS 161/161 |
| O | O2 battery98 | FAIL 5/0/31/0/3/0 | PASS 0/0/36/0/3/0, driver = pin = receipt |
| O | O3 mutation98 | FAIL driver missing (v9 red-before 117/128, 11 broken) | PASS 128/128, driver = pin = first receipt |
| O | O4 REG | PASS 34/34 (guard) | PASS 34/34 |
| O | O5 critic97 replay | FAIL survivors=8 | PASS survivors=3 (benign controls rc 0), the 5 named forgeries refused |
| C | C1 entry | FAIL absent | PASS 47760 B, 13 h2, table 7×5, 6/6 phrases, topic equal |
| C | C2 registry | FAIL 917 rows, S993, 0 qualifying | PASS 930 rows, S1006, 11 qualifying |
| C | C3 append-only | PASS (guard) | PASS added=14 removed=1 in-place=1 illegal=0 |
| C | C4 census | PASS (guard) | PASS rc 0 |
| C | C5 index | PASS 269 (guard) | PASS 270/270/0 |
| C | C6 cited | FAIL | PASS 11/11 |
| C | C7 captures | FAIL | PASS 11/11, 17 verified |
| C | C8 sweep | PASS owners 0 (guard) | PASS owners 0 of 270 |
| C | C9 non-author re-open | FAIL | PASS 10 ids |

**Harm findings on claim O** (non-author; outside the frozen predicate; reported, not prettified):

- ReviewerO98b F4 / CriticO98b: v10 widens the heading combining check from Mn/Me to all M. As a result, a valid h2 heading with a Devanagari visarga (Mc), which is CLEAN on v9, is now `FAIL TOPIC`.
- ReviewerO98b F1: the `HEADING-NUMBER` loop refuses a bare non-ASCII-numeral heading (`## Ⅳ.`) and protects nothing.
- Measured lane exposure: 0 of 3010 h2 headings in `corpus/knowledge` carry Mc, and 0 are numeral-only.
- These are still two new false-refusal surfaces. The grader was not changed after the mutation first measurement, because the pin binds those bytes. The fix is routed to round 99.
- Claim O meets its frozen predicate. Whether the "no axis harmed" admission holds is the closure's ruling.

**Honest note on claim C.** The scribe's draft met the frozen predicate, but the seat reviews found one contradicted sentence, one misquote and one ungrounded teaches word. The L1 repaired these before landing (lesson R98-M2, R98-M3). After the repair the entry has not been re-reviewed by a non-author seat, so the closure should sample line 142 and §8.

## Sources & frontier

- `corpus/SOURCES.md` rows went from 917 to 930 (`grep -c -E '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; base via `git show bcf664aa:corpus/SOURCES.md`). Highest id went from S993 to S1006. One line was changed in place: S992.
- Rows added by tier: A 7 (S994, S996, S997, S998, S1000, S1003, S1006); B 6 (S995, S999, S1001, S1002, S1004, S1005); C 0. All were opened 2026-11-05 by plain curl with HTTP 200. The Gate table, with a `capture file` column and full sha256 values, is in `corpus/lessons/round-98.md`.
- Rows touched old→new:
  - S992: status `mined` → `queued`, used-by verbal entry → `—` (superseded by S1005, tier A → B).
  - S994 (added this round): status `mined` → `queued`, used-by entry → `—` (superseded by S1006).
- Rejected: 15 candidates, each with reason and flip (403/SSO walls, a timeout, JS shells, bot challenge, wrong chapters, a 404).
- Census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` gave rc 0 at start (`.ufo/waves/round-98/census/census-start.txt`) and rc 0 at end (`census-end.txt`). No warning on S994–S1006.
- Frontier rows advanced: the toast and drinking-speech surface is now indexed under `## linguistics/ (43)`. The oath entry has 8 sentence repairs.
- Sourced claim: claim C cites S995–S1004 and S1006, all opened this round.
- Mined mistake: R98-M1, a Gate hash that names no capture file. The fix is `tools/check-gate-captures.py`, which fails with 9 findings on round 97 and passes with 0 of 13 on round 98. R98-M2 through R98-M5 are in the lesson.
- Assimilation: none. `considerthese/` does not exist in this lane, and shokuknow `merge/kotodama/` was not adopted this round.

## Trend verdicts

- **expansion: improved.** A surface with no owner at base now has a 47760 B entry and 11 qualifying tier A/B rows, with census rc 0. Evidence: legs C1–C9 and `census-end.txt`.
- **quality: improved.** Eight contradicted or unsupported sentences in the round-96 oath entry were repaired. Each repair rests on a located quote that counts 1 in its committed capture (ReviewerOath98 `support.md`; lesson R98-M4). The S992 tier is corrected by supersede. This is the author's verdict and the repairs are not yet non-author re-reviewed.
- **discernment: unchanged.** The gate-capture checker is able to fail, and 15 rejects carry flip conditions. Against that, v10 introduced two over-refusals that non-author seats caught and the frozen battery did not. The net verdict is not better.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. The new entry has a decision procedure (§9), error patterns (§10), a checklist (§11) and 11 cited rows (`corpus/knowledge/linguistics/toast-drinking-speech-formulae.md`). SKILL.md itself did not change.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Scouting, sourcing, registry, entry, review and repair are logged in `LOG.md` (round 98). Pointer: `.ufo/waves/round-98/w1/`.
- [~] Instructions executable by an agent without oral context. The frozen counter passes 15/15 (`reports/round-98/predispatch-lands.txt`), and a non-author seat reproduced it.
- [~] No cross-domain bleed (PROVINCE.md still accurate). ConnectorOverlap98 found 0 sibling claims, and the lore and chousa boundaries are kept (`w1/stage/ConnectorOverlap98/overlap.md`).

No box is `[x]`: promotion is operator-owned.

## Stale-lane

Open missions for this lane: none beyond round 98 (respawn-per-round driver). Progressing: this round (landed). Silent: none.

## Tool installs

None. RULES.md was read (operator, 2026-10-19). There was no pacman transaction (paused host-wide), and no seat reported an install.

## Routing and holds

- Attempt 1's inherited outputs were reused after re-verification. The dead seats' drafts (`mutants98.py` pre-pin, `attacks_critic98.py`) were re-derived by the w2 seats; nothing was counted from the dead seats.
- Two scout capture duplicates (`w1/stage/ScoutSources98/captures/C1.txt`, `C11.html`) were discarded. Both are over 1 MiB and byte-identical by sha256 to the committed `reports/round-98/evidence/S994.txt` and `S998.html`.
- Host sysctls: unchanged by this lane.
- L0 open: freshness pause (round-11, round-89); ideophones overlap (round-92); disk pressure (round-96). No new L0 line.

## Landing

Lane commits were made with `jj-lane.sh commit … --as kotodama`:

- freeze: `db88f107606aae90efe01344551c7e1ea71cd419` (attempt 1)
- round: `landed 7ff35e6ce6a8027fd04ba4a6bccce179b7286ca3`

`ls-remote origin refs/heads/main` prints `7ff35e6ce6a8027fd04ba4a6bccce179b7286ca3`. This report was committed by `fleet-commit.sh --as kotodama`.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/*` (orchestrator) and `w4lines.txt`, which is not this lane's (it was present in round 97). No round-98 seat file was at the fleet root, so nothing was copied or deleted. `$HYAKU_SCRATCH/kotodama-r98` was removed.
