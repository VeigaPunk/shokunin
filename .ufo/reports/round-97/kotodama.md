# kotodama — round 97 report (hyaku run 15, attempt 1)

Lane: kotodama (linguistic-cultural worldbuilding). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Lane HEAD at landing: `fc5ba047df8a3baf7159a3d7cdfa1b72fc14768e` (branch `main`). `git ls-remote origin refs/heads/main` → `fc5ba047df8a3baf7159a3d7cdfa1b72fc14768e`.
Base `1ffc5a83d2c70e3bc581594efbcf32c562ba2569`. Freeze `24eac1e91688d8aa0696a07eff17beeacd407763` (before any seat ran). Round commit `fc5ba047`.

## Work performed

Declared claims (`reports/round-97/claims.json`, 2 claims, distinct axes, causally separable):

- **Claim O — operability** (successor grader move v8 → v9). It closes the seven CriticO96 classes that still survive v8. They were measured before the freeze: `reports/round-97/controls/critic96-on-v8.txt`, `CRITIC-O96 survivors=7`. Target: battery97 `survivors=0 unnamed=0 refused=31`, selftest ≥154, mutation97 killed == total ≥118 with 0 survived and 0 broken-pattern, REG identical. Both drivers are sha-bound to a pin and to their first-measurement receipt, which closes round-96 routed defect 2.
- **Claim C — coverage** (sourced frontier → core entry on verbal duelling and ritual insult). At base no topic line or heading owns the surface, measured by the frozen content sweep leg C8. Target: the entry plus ≥3 new tier A|B rows opened 2026-11-05, all cited and captured, census and index rc 0, C8 owners 0.
- Lowest-axis note: freshness is the historically lowest non-retired axis. It stays paused by the L0 round-11 and round-89 questions (no ANSWER). This round moves no freshness claim, so the lowest-axis obligation is neither met nor waived.

Work items (wave `w1`, 12 seats, one v1 wave). The spec is `.ufo/waves/round-97/w1-spec.json`, the dispatch is `w1-dispatch.json` and the results are `w1-results.json`. Each seat's report is `.ufo/waves/round-97/w1/<Seat>.md` and its stage is `.ufo/waves/round-97/w1/stage/<Seat>/`.

1. **Freeze (L1).** Counter `reports/round-97/predispatch.py`. Do-nothing control `predispatch-base.txt` → `PREDISPATCH-97: FAIL legs=4/13`. Sha-only forgery control `controls/forgery-sha-only.txt` (v8 plus one comment line) → O0 PASS, O1 FAIL 147/147 < 154, FAIL 5/13. Sweep falsifiability control `sweep-control.txt` → round-96 replay owners=2, round-97 base owners=0, rc 0. Two counter revisions happened before the freeze, both recorded in the lesson: the C1 table rows now reset per table, and C8 was narrowed to topic and headings after a table-cell hit in `trickster.md:25`. Freeze commit `24eac1e9`.
2. **ExecBattery97.** Built battery97 (battery96 plus CR1, US1, OGH1, IS1, NUL1, CM1, CMW2). Its control over v8 was taken before any v9 bytes existed: `BATTERY-SHA256 79efb67c…`, `TOOL-SHA256 f29ab013…`, `BATTERY-SUMMARY survivors=7 unnamed=0 refused=24` (`reports/round-97/controls/battery97-control-v8.txt`). Pin: `controls/battery97.sha256`.
3. **ExecGraderV9.** Wrote v9 (`1021dc9d…`) with the new diagnostics `VERDICT-CTRL` (C0 controls, naming the codepoint), `VERDICT-SEPARATOR` (Zs) and `HEADING-COMBINING` (on TOPIC). Results: selftest 155/155, battery97 0/0/31, REG 34/34 (`stage/ExecGraderV9/`). One self-repair before V9-READY: a U+0020 regression on REG A5c was found and fixed. The round-96 cosmetic defect 6 is fixed (v7 → v8 labels, blank line removed). Its own counter run: PASS 13/13 (`counter.txt`).
4. **MutationTester97 (attack).** Wrote `mutants97.py` (111 carried plus 10 new). It pinned the driver, then took its first measurement on v9: `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern` (`reports/round-97/controls/mutation97-first.txt`, first line `DRIVER-SHA256 f9c623fd…` = pin). Red-before on v8: 111/121, 10 broken-pattern (`stage/MutationTester97/red-before-v8.txt`). No grader repair was needed.
5. **CriticO97 (attack).** Fresh classes against v9: `CRITIC-O97 survivors=8 unnamed=0 refused=17`. On v8 the same fixtures give survivors=19 refused=6. The CriticO96 replay over v9 gives survivors=0 refused=19. These survivors are routed to round 98: ENC1 U+20DD, DEL1 U+007F and non-ASCII heading numbering (`stage/CriticO97/attacks.md`). Deviation: the seat attacked once `V9-READY` existed, because ExecGraderV9/DONE came after its 90-minute loop. The bytes it attacked (`1021dc9d…`) are the landed v9 bytes.
6. **ReviewerO97 (attack, non-author).** Ran the frozen counter: PASS 13/13 (O3 121/121). It also checked the pin and receipt table and their mtime order. Its shadowed-branch equivalence check, run on each of the 3 new branches, found every one non-shadowed. battery96 over v9 shows 24/24 refused, and the cosmetic edits are neutral (`stage/ReviewerO97/review.md`). **Claim O: PASS.**
7. **ScoutSurface97.** Content sweep: 59 body hits in 32 files, 0 topic or heading owners. It also wrote the adjacency boundaries, the skeleton and the partition counts (`stage/ScoutSurface97/surface.md`).
8. **ScoutSources97.** Ran 8+ queries. It admitted 8 candidates (7 tier A, 1 tier B) and turned away 2 (no unique quote) plus 7 wall rejects, with every attempt recorded (`stage/ScoutSources97/candidates.{md,json}`).
9. **ConnectorOverlap97.** Checked the sibling PROVINCE and SKILL files and the in-lane owners. Nothing is contested (`stage/ConnectorOverlap97/overlap.md`).
10. **ExecRegistry97.** The only registry writer. It re-verified the 8 candidates and appended S985–S992 plus S993 (Thrênoi, frontier). The append is append-only (added=9 removed=0) and census rc 0. Evidence and manifest are under `reports/round-97/evidence/`.
11. **ScribeEntry97.** Drafted `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`, the README index row and section (268 → 269), and one S993 sentence in the lament entry.
12. **ReviewerC97 (attack, non-author).** C1–C8 PASS. Support table: 12 supported, 2 weak, 2 unsupported, 1 contradicted. The contradicted sentence was the funerary S993 sentence. It also found a manifest-name defect and an absent quoted word (`stage/ReviewerC97/review.md`).
13. **CriticC97 (attack).** Claim C survives the predicate. It raised defect F1–F4: the quote, a design claim contradicted by S985, a misstated neighbour slot set, and copied boundary prose (294 shared 8-grams with the oath entry) (`stage/CriticC97/critic.md`).
14. **L1 integration repairs** (after the seats, before landing; counter bytes untouched):
    - Entry: lines 68, 95, 97 and 135, the §8 table cells (marked *(design)*), the S985 grounding line, §4 rewritten from S985's ashik and haló passages, §6 slot sentence, §1 and §12 boundary prose, and the micro-example (new invented people). After the rewrite 35 8-grams are shared with the oath entry.
    - Funerary sentence rewritten from the S993 passages, and the S993 teaches cell corrected.
    - Manifest file names repointed by sha256.
    - Quote recount: 40 fragments, all count 1.
    - QUALITY criterion 39 added. Lesson, LOG and SCORECARD written.

Round shape and seat mix:

- One v1 wave: 12 spawn seats, 0 resume, 0 residual calls. Round total 12 seats.
- Roles: executor 3, mutation-tester 1, critic 2, reviewer 2, scout 2, connector 1, scribe 1.
- Attack seats 5/12 = 42%.
- Dead seats: none (all 12 settled; WAVE-DONE received).
- Planner: the canonical L2 planner seat is held by the L1. The planning data-walk rode ScoutSurface97 and ConnectorOverlap97.

Routed round-96 defects (`corpus/lessons/round-96-verifier-spotcheck.md` §5): all 7 are handled, as listed in `corpus/lessons/round-97.md`:

1. Content sweep: C8 plus criterion 39.
2. Mutation pin: O3 receipt binding.
3. CriticO96 on v8: measured, now claim O.
4. Thrênoi: S993 written.
5. R27 rule: one row per opened URL, stated.
6. Cosmetic: fixed.
7. Dead reviewer: ReviewerC97 delivered a verdict.

## Landed changes

| change | file(s) | LOG entry | commit |
|---|---|---|---|
| freeze of claims O and C, counter, do-nothing, forgery and sweep controls, CriticO96-on-v8 receipt, census-start | `reports/round-97/{claims.json,predispatch.py,predispatch-base.txt,sweep-control.py,sweep-control.txt}`, `reports/round-97/controls/{forgery-sha-only.txt,critic96-on-v8.txt}`, `.ufo/waves/round-97/census/census-start.txt` | round 97 | `24eac1e9` |
| claim O: grader v9 | `tools/check-advance-evidence.py` | round 97 | `fc5ba047` |
| claim O: drivers, pins, receipts | `reports/round-97/controls/{battery97.sha256,battery97-control-v8.txt,mutants97.sha256,mutation97-first.txt}`, `.ufo/waves/round-97/w1/stage/{ExecBattery97,MutationTester97}/` | round 97 | `fc5ba047` |
| claim C: entry | `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` | round 97 | `fc5ba047` |
| claim C: 8 registry rows S985–S992; frontier row S993; 0 removed | `corpus/SOURCES.md` | round 97 | `fc5ba047` |
| claim C: index row, count and section | `corpus/README.md` | round 97 | `fc5ba047` |
| frontier: S993 sentence in the lament entry | `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` | round 97 | `fc5ba047` |
| frontier: criterion 39 | `corpus/QUALITY.md` | round 97 | `fc5ba047` |
| lesson, scorecard, log | `corpus/lessons/round-97.md`, `SCORECARD.md`, `LOG.md` | round 97 | `fc5ba047` |
| evidence: captures and manifest, lands receipts (including the ENOSPC run), wave dir, census-end | `reports/round-97/**`, `.ufo/waves/round-97/**` | round 97 | `fc5ba047` |

## Before → after measurements

Counting command for all legs (frozen counter): `python3 -B reports/round-97/predispatch.py --root <lane> --work <scratch> --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569`.

| claim | leg | before (base `1ffc5a83`, control) | after (landed `fc5ba047`, tool v9 `1021dc9d…`) |
|---|---|---|---|
| O | O0 tool sha ≠ v8 | FAIL (sha = v8) | PASS |
| O | O1 selftest | FAIL 147/147 < 154 | PASS 155/155 |
| O | O2 battery97 | FAIL driver missing; over v8 measured survivors=7 refused=24 | PASS survivors=0 unnamed=0 refused=31, driver = pin = receipt |
| O | O3 mutation97 | FAIL driver missing; v8 red-before 111/121 + 10 broken | PASS 121/121 killed, driver = pin = first receipt |
| O | O4 REG | FAIL no output | PASS 34/34 byte-identical |
| C | C1 entry | FAIL absent | PASS 36739 B, 13 h2, table 7×6, 6/6 phrases, topic equal |
| C | C2 registry | FAIL 908 rows, highest S984, 0 qualifying | PASS 917 rows, highest S993, 8 qualifying |
| C | C3 append-only | PASS (guard) | PASS added=9 removed=0 |
| C | C4 census | PASS (guard) | PASS rc 0 |
| C | C5 index | PASS (guard, 268) | PASS 269/269/0 |
| C | C6 ids cited | FAIL | PASS 8/8 |
| C | C7 captures | FAIL | PASS 8/8 |
| C | C8 content sweep | PASS (guard, owners 0) | PASS owners 0 of 269 |

The landed tree measures `PREDISPATCH-97: PASS legs=13/13` rc 0 (`reports/round-97/predispatch-lands.txt`). The same 13/13 was run independently by ReviewerO97 and by ExecGraderV9. The first L1 lands run died in O3 on host ENOSPC: `/fast` was at 100% with 256 KiB free, filled by another tenant. That run is kept as `reports/round-97/predispatch-lands-enospc.txt`, and the re-run used `--work` on `/home`.

**Honest note on claim C.** The frozen predicate was met by the scribe's draft. Two seat reviews nevertheless found sentences contradicted by their cited sources, and copied boundary prose. The L1 repaired these before landing. The frozen legs measure presence, citation and ownership, not whether each sentence is supported (lesson R97-M2, R97-M4). The repaired text has not been re-reviewed by a non-author seat; the closure should sample it.

## Sources & frontier

- `corpus/SOURCES.md` rows went from 908 to 917 (`grep -c -E '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; base via `git show 1ffc5a83…:corpus/SOURCES.md`). Highest id S984 → S993. Removed lines: 0.
- Rows added by tier: A 8 (S985, S986, S987, S989, S990, S991, S992, S993); B 1 (S988); C 0. Status `mined`, opened `2026-11-05`, recheck `180d`. Each row's located quote is recorded in the `## Gate` of `corpus/lessons/round-97.md`.
- Rows touched old→new: none among base rows. S993, the Thrênoi row, moves from round-95 reject to round-96 nomination to round-97 `mined`, used-by the lament entry.
- Rejected: Bevan *Naqāʾiḍ* (no unique quote), Labov chapter (preview repeated, author copy 403), and seven 403 or login-shell walls. Every reject carries a flip condition.
- Census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` rc 0 at start (`.ufo/waves/round-97/census/census-start.txt`) and at end (`census-end.txt`), with no warning on S985–S993.
- Frontier rows advanced: the verbal duelling and ritual insult surface, indexed under `## linguistics/ (42)`. The Thrênoi professional-mourner facet is now in the lament entry.
- Sourced claim: claim C cites S985–S992, all opened 2026-11-05 by plain curl with HTTP 200.
- Mined mistake: R97-M1 (an ownership premise built from file names). The fix is leg C8 plus criterion 39, shown able to fail (round-96 replay owners=2). R97-M2 through R97-M5 are in the lesson.
- Assimilation: none. `considerthese/` does not exist in this lane, and shokuknow `merge/kotodama/` was not adopted this round.

## Trend verdicts

- **expansion: improved.** A surface with no topic or heading owner at base now has an entry (36739 B) and eight tier A/B rows, with census rc 0. Evidence: counter legs C1–C8 and `census-end.txt`.
- **quality: unchanged.** No admitted entry was re-verified or superseded as a claim. One sourced sentence was added to the lament entry. Grader v9 is operability, not knowledge quality.
- **discernment: improved.** Criterion 39 is grounded and able to fail. Two candidates were turned away with reasons and flip conditions. Seat-caught contradictions were repaired, and the R27 registry rule is stated. This is the author's verdict; the closure should check it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. The new entry carries a design procedure, error patterns, a genre table and eight cited sources (`corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`). SKILL.md itself did not change.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Scouting, sourcing, registry, entry, review and repair are logged in `LOG.md` (round 97). Pointer: `.ufo/waves/round-97/w1/`.
- [~] Instructions executable by an agent without oral context. The frozen counter `reports/round-97/predispatch.py` passes 13/13 on the landed tree, and the grader selftest passes 155/155. Pointer: `reports/round-97/predispatch-lands.txt`.
- [~] No cross-domain bleed (PROVINCE.md still accurate). ConnectorOverlap97 found no sibling claim. Copied boundary prose was removed (8-gram overlap with the oath entry went from 294 to 35), and orality, politeness and binding-speech each share 0. Pointer: `stage/ConnectorOverlap97/overlap.md`, `stage/CriticC97/critic.md`.

No box is `[x]`: no non-author verifier has promoted a box, and promotion is operator-owned.

## Stale-lane

Open missions for this lane: none beyond round 97 (respawn-per-round driver). Progressing: this round (landed). Silent: none.

## Tool installs

None. RULES.md was read (operator, 2026-10-19). There was no pacman transaction (paused host-wide), and no seat reported an install.

## Routing and holds

- Host disk: `/fast` reached 100% during the round (another tenant). The L1's first lands run died on ENOSPC and was re-run with scratch on `/home`. `$HYAKU_SCRATCH/kotodama-r97` was removed after landing, along with the `/home` scratch. No L0 line was added; the round-96 disk-pressure question remains open.
- Host sysctls: unchanged by this lane.
- L0 open: freshness pause (round-11, round-89); ideophones overlap (round-92); disk pressure (round-96).

## Landing

Lane commits were made with `jj-lane.sh commit … --as kotodama` and landed `24eac1e91688d8aa0696a07eff17beeacd407763` (freeze) and `fc5ba047df8a3baf7159a3d7cdfa1b72fc14768e` (round). `ls-remote origin refs/heads/main` prints `fc5ba047df8a3baf7159a3d7cdfa1b72fc14768e`. This report was committed by `fleet-commit.sh --as kotodama`.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time shows `.scratch/*` (orchestrator), `.ufo/reports/round-100/revenger.md` and `w4lines.txt`, none of them this lane's. No round-97 seat file was at the fleet root, so nothing was copied or deleted.
