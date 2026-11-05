# kotodama — round 90 (hyaku run 15, attempt 1)

lane: kotodama-shokunin · round: 90 · campaign: hyaku · date: 2026-11-04/05 (−03:00)
base: `6b0b86e45ae902331aca75863db380f2991458c4` · freeze: `d0b6f2a7f9cc36272682749a9b047b739406f0c8`
claim-C lands: `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761` · corrected lands: `210c0dd08a1bc8aa6dd32d2ec9e38cb0f2ccfbc4`
lane tip at report: `6394ad434e6995a5e5395652f01e7eeff560860c` — `git ls-remote origin refs/heads/main` prints the same hash.

## Work performed

Declared claims (frozen before data, `reports/round-90/claims.json`):

- **O / operability — capability acquisition.** `tools/check-advance-evidence.py`, a landing-evidence grader that refuses the thirteen counterfeit classes the round-89 wave demonstrated, with a 67-check selftest and a committed 43/43 mutation receipt, both landed before the first dispatch.
- **C / coverage — sourced claim.** One new linguistics entry, `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, over seven sources opened this round (S942–S948 admitted; S949–S951 registered as rejections with their flip conditions).

Freshness is the lane's historically lowest axis and is **paused** by the open L0 questions `kotodama | round-11` and `kotodama | round-89` (round-89 spot-check §6.1 forbids a further freshness move until ruled). Coverage is therefore the axis this round works directly, on ground the coverage map did not hold.

Work items, each with its evidence pointer:

- **Freeze and controls, before any data** — `d0b6f2a7` (claims, counter, grader, mutants), `9fb2c58f` (at-freeze control receipts and counter revisions 2–5), `ebd81b1b` (revision 6, the ENTRY-verdict keying defect a wave seat reported). `reports/round-90/counter-revisions.md` records every revision with its reason and sha256; no leg, threshold, predicate or constant changed.
- **Inherited attempt resolved** — an earlier attempt of this round committed `d0b6f2a7 … 945e6a3e` and died on provider failure. Reused after re-verification: the grader, the counter, the mutant generator, the at-freeze and stub receipts, the 43/43 mutation receipt, eight seat reports under `.ufo/waves/round-90/w1/`, and the frozen claims. Discarded: its seven captures, which carried no manifest (replaced by L1 re-fetches with a manifest under `reports/round-90/evidence/`), and its four seats that delivered nothing. Named as R90-M4 in the lesson.
- **Claim C landing** — the entry, registry rows S942–S948 admitted (six A, one B; all `mined`, `opened 2026-11-04`, `used-by` the entry) and S949 rejected, lesson gate lines with one located quote per id, eight committed captures plus `manifest.json` (sha256, http_status, local fetch instant), `corpus/README.md` row and count moves. Lands `7f3a7aa6`; entry 19,930 B there.
- **Source-conduct check** — every source opened by ordinary HTTP (`curl -sS -L`), no browser, no challenge, no login. The seed list was wrong in three places and opening the pages caught it: WALS chapter 74 is Situational Possibility (the Prohibitive is chapter 71), `glossary.sil.org/term/vocative` is 404 while `/term/vocative-case` answers, and the SIL glossary carries no prayer, invocation, supplication, petition, vow, votive, blessing or curse term at all (nine-term 404 sweep, lesson R90-M9).
- **Rejections registered** — the three tier-C Wikipedia seeds are rows with reasons and flips, S949–S951, each with a gate line quoting a span that occurs in its committed capture (S949's first draft quoted a span the capture splits across markup; corrected at `e0795be6`).
- **Post-wave correction** — the reviewer's six content defects (D1–D6) fixed at `e0795be6` and the entry's WALS 72 definitions corrected at `3f56892f`; the entry is 20,400 B at the corrected lands.
- **Measurement** — `reports/round-90/final/lands-O.txt` `MEASURE90-O: PASS legs=6/6`, `final/lands-C.txt` `MEASURE90-C: PASS legs=4/4`, `final/separability.txt` `SEPARABILITY: PASS` (each claim graded only by its own overlay: other claim's paths absent O 6/6, C 4/4), plus re-measurements at `e0795be6`, `210c0dd0` and the final tip `6394ad43` (`lands-O-final.txt`, `lands-C-final.txt`), all 6/6 and 4/4.
- **Frontier step** — `corpus/SOURCES.md` census exit 0 at start (`census-start.txt`) and end (`census-end.txt`); seven rows opened and admitted, three rejected; lesson `## Gate` carries URL, access date and quote for every new row; `## Mistakes` carries R90-M1 … R90-M9.
- **Scope and sweep** — no write outside `kotodama-shokunin/` and this report; the fleet-root sweep shows `.scratch/run15-state.json` (orchestrator), `.ufo/reports/round-86/kama.md` (kama lane) and `mo.tip` (0 bytes, 23:58, naming neither this lane nor this round) — none is a kotodama misroot, none touched.

### Falsification findings the frozen instrument does not cure

Both waves attacked the frozen predicate; the claims are frozen, so none of these was repaired inside the round, and every one stands as a bound on what O and C prove.

| attack (seat) | claim/leg | verdict | what it means here |
|---|---|---|---|
| an 11-line stub printing the tally line and the 13 case names passes SELFTEST + REFUSALS + STUB (`CriticClaims`) | O | weakened | only TOOL and MUTATION carry discrimination against a non-implementing tool |
| the committed stub receipt records the stub *passing* SELFTEST and failing REFUSALS and MUTATION (`ReviewerDiscipline` MINOR-2, `CriticClaims` F4–F6) | O | broken as stated | the frozen `after_target` sentence says the stub fails SELFTEST; the bytes say otherwise (reported, not edited) |
| 21 new single-point mutants of the grader: 7 killed, 14 survive the selftest (`MutationTester`) | O | weakened | "one negative per sub-check" holds for the checks the selftest exercises, not for every entry-mode sub-check (table/topic floors, NEWIDS status, gate-quote selection, capture confinement, sha256 skip, http-status widening, fetched-date, registry indentation, duplicate leniency) |
| `MATERIALIZE` and `INDEX` pass at the base revision for both claims (`CriticClaims` F3, F9) | O, C | not discriminators | only the claim-specific legs carry the verdict |
| a 10-line tool passes SELFTEST and REFUSALS (`CriticClaims` F4) | O | self-attested | the selftest is a fixture battery inside the tool it certifies |
| title-chrome gate quotes, a co-fabricated capture, a shadow duplicate id and a 66 KB hollow entry all pass C 6/6 (`ReviewerChrome`, `CriticClaims` F5–F6) | C | broken as discriminators | the six C legs prove structure and gate binding, never content; the landed bytes were scanned clean for all five classes |
| graded-file capture paths and repeated-sentence inflation (`ReviewerChrome` c/d) | C | refused | the instrument works where it is written to |
| `C.surface` prose is false at base as written; the operative unmoved-command holds (`CriticClaims` F7) | C | broken as written | recorded as R90-M8, re-measured in the lesson; the frozen text is not edited |
| `O.before` cites `reports/round-89/mutation-score.txt`, absent at base and at HEAD (`CriticClaims` F11) | O | citation defect | the actual receipt is `.ufo/waves/round-89/w1/MutationCounter.md` |

The critic's smallest safe corrections (fail on duplicate lands ids, fail on a qualifying row whose URL already exists at base, apply the self-quote test in entry mode) are routed to round 91: the tool is sha256-pinned by the frozen O predicate, so editing it now would fail O by construction.

## Landed changes

Each change is tied to the `LOG.md` round-90 entry (`LOG.md`, "## Round 90") and to the commit that carries it.

| change | commit |
|---|---|
| claims, frozen counter, grader `tools/check-advance-evidence.py`, mutant generator and at-freeze controls | `d0b6f2a7` |
| at-freeze control receipts, counter revisions 2–5 | `9fb2c58f` |
| inherited v1 wave spec, validated dispatch, ready handoff (12 seats) | `c0c628d8` |
| counter revision 6 (ENTRY verdict keying), frozen bytes unchanged | `ebd81b1b` |
| in-flight preservation of the dead attempt (not a landing) | `945e6a3e` |
| claim-C landing: entry, S942–S948, lesson, README moves, evidence + manifest, separability harness, census end | `7f3a7aa6` |
| w2 spec, validated dispatch, ready handoff (11 seats), separability overlay set fix | `fe59fc35` |
| lesson base-surface correction and R90-M7/M8/M9, counter receipts at lands, separability receipt | `19187112` |
| `LOG.md` round-90 entry, `SCORECARD.md` round-90 rows and the grader capability row | `195aff9c` |
| entry definitions corrected to the chapter's own words (WALS 72 minimal/maximal) | `3f56892f` |
| reviewer D1–D6 content fixes, S949 quote fix, census end refresh | `e0795be6` |
| rejection rows S950 and S951 with gate lines and captures | `210c0dd0` |
| settled w2 evidence: eleven seat reports, stage receipts, `w2-results.json`, tip receipts | `26e30795` |
| final counter receipts at the tip, registry counts corrected to 875 in LOG and SCORECARD | `6394ad43` |

`26e30795` was committed under the lane identity by the orchestrator side between my own commits and confined to `.ufo/waves/round-90/w2/**` plus the two tip receipts; its content is the wave evidence I intended to land. The same concurrent writer also edited this report's early draft (tip line, a duplicate `e0795be6` row, a two-wave sentence); this file is the L1's corrected text.

## Before → after measurements

Frozen counter, unchanged after data: `reports/round-90/measure90.py` (sha256 `6e1ea6a5…`, revision 6; the freeze pinned revision 1 and `reports/round-90/counter-revisions.md` records 2–6 with reasons, none touching a leg, threshold or constant).

| claim | before | after | counting command | measured at |
|---|---|---|---|---|
| O / operability | `tools/check-advance-evidence.py` absent at base (`git cat-file -e` fails); the round-89 predicate accepted five counterfeit landings its own wave built and scored 10/41 mutants (`.ufo/waves/round-89/w1/MutationCounter.md`) | tool present at the freeze pin (sha256 `121888f0…`), `SELFTEST PASS 67/67`, all 13 refusal cases ok, `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern`, stub control recorded (`SELFTEST PASS 67/67` fake, REFUSALS 0/13, `0/43 killed`, 43 broken-pattern) — `MEASURE90-O: PASS legs=6/6` | `python3 -B reports/round-90/measure90.py --root <clone> --freeze d0b6f2a7f9cc36272682749a9b047b739406f0c8 --lands <lands> --claim O --work <existing-dir>` | `7f3a7aa6` (`final/lands-O.txt`) and `6394ad43` (`final/lands-O-final.txt`) |
| C / coverage | no dedicated entry; linguistics partition 34 files; registry 865 rows; 0 new ids | entry 20,400 B, 10 `##` headings, one 5-row × 4-column table; linguistics 35 files, knowledge 262; registry 875 rows with S942–S948 mined and cited and S949–S951 rejected; `CORPUS-INDEX: OK files=262 rows=262 findings=0`; zero base rows changed — `MEASURE90-C: PASS legs=4/4` | same command with `--claim C` | `7f3a7aa6` (`final/lands-C.txt`) and `6394ad43` (`final/lands-C-final.txt`) |

Separability at `7f3a7aa6` (`reports/round-90/final/separability.txt`): overlay O `PASS legs=6/6` with the six C paths absent, overlay C `PASS legs=4/4` with the four O paths absent; the shared paths are the frozen config, the counter and the instrument only.

## Sources & frontier

Counting command (both ends, exit 0):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

| quantity | before (`6b0b86e4`) | after (`210c0dd0`) |
|---|---|---|
| rows | 865 | 875 |
| tiers | A=511 B=329 C=25 | A=517 B=330 C=28 |
| status | mined=762 queued=58 rejected=45 | mined=769 queued=58 rejected=48 |
| changed old rows | — | 0 (cell-wise compare of all 11 columns) |
| removed old rows | — | 0 |
| census rc | 0 (`census-start.txt`) | 0 (`census-end.txt`) |

Rows added by tier: seven admitted (six A — S942 WALS ch. 72, S943 WALS ch. 73, S944 WALS ch. 71, S946 AIO IGI3 646, S947 Blidstein PLOS One, S948 Galofaro & Kubas OASIcs; one B — S945 SIL glossary `vocative-case`) and three rejected C (S949 *Votive offering*, S950 *Curse tablet*, S951 *Sacred language*, each with reason and flip). Rows touched old→new: none — no `status`, `recheck` or `used-by` cell of a pre-existing row changed, because freshness is paused and nothing was re-verified this round. Frontier rows advanced: none; `corpus/README.md` gains one index row and the partition/total arithmetic only.

Assimilation: none — the lane has no `considerthese/` directory, and the shokuknow package adoption stays closed under the wave-4 quarantine-first rule.

## Trend verdicts

- **expansion: improved.** One admitted `knowledge/` entry on ground the coverage map did not hold, citing seven `mined` rows opened this round (six A, one B), with a README index row and a new partition count; the base surface was carried only as sub-sections (`carthage.md:1`, `sacred-topography-pilgrimage.md:1` and `:74`, `religion-language-co-evolution.md:1` and `:64`, `tibet.md:92`, `direction-symbolism.md:129`), so the entry adds a topic rather than a copy.
- **quality: improved, with a recorded limit.** The round's instrument is a real improvement over the round-89 predicate that a wave passed with five counterfeits at 10/41 — it holds 67 self-checks, 13 named refusals and a 43/43 committed mutation pass — and the reviewer's six content defects were fixed rather than argued. The limit is measured, not hidden: 14 of 21 independent entry-mode mutants survive, so the improvement is in the checks the selftest exercises, not in every entry-mode sub-check.
- **discernment: unchanged (pending the non-author spot-check).** Four disagreements became lesson rows with fixes (R90-M3 counter keying, R90-M7 separability set bug, R90-M8 base-surface wording, R90-M9 inherited 404 claim re-measured) and four more are recorded as honest limits (the falsification table above). A dispatched seat is still the lane, so no verdict above `unchanged` is claimed until an outside spot-check samples this round's seven admits and three rejections.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — asserted: no `[x]` this round. `SKILL.md` unchanged; the round's craft lives in the entry's design procedure and its eight failure checks, and the new gate is registered in `SCORECARD.md` capabilities, not in `SKILL.md`.
[~] At least one end-to-end domain task executed and logged in LOG.md — asserted: the entry's procedure §6 was exercised against the seven admitted sources (mood decision, prohibitive strategy, address system, vow formula with receipt, votive object inventory, archaism list, litany ordering principle, failure cases); `LOG.md` "## Round 90".
[~] Instructions executable by an agent without oral context — asserted: `python3 -B tools/check-advance-evidence.py --selftest --work <dir>` and the counter commands recorded in `reports/round-90/claims.json` run without lane-specific context; `reports/round-90/final/lands-{O,C}*` record the runs.
[~] No cross-domain bleed (PROVINCE.md still accurate) — asserted: the entry is a design surface, hands the register to lore through `synthesis/worldbible-integration-contract.md` and leaves canon, research method and rights to their owners; `PROVINCE.md` unchanged this round.

## Round shape

Two v1 waves for this round, 23 seats in total, no residual call; the L1 holds the canonical planner seat (the validator rejects `planner` as a swarm role) and a bounded planning data-walk rode the scout item.

- **Wave 1** (`kotodama-r90-v1`, the earlier attempt's dispatch: spec `spec-v1.json`, `w1-dispatch.json`, ready `w1.ready`, results `w1-results.json`): 12 seats — 2 scribe, 4 executor, 1 scout, 1 connector, 2 reviewer, 1 critic, 1 mutation-tester; attack 4/12. Eight seats delivered reports; four (`ScribeEntry`, `ScribeLesson`, `ConnectorSiblings`, `MutationTester`) delivered nothing and stay dead, with `ScribeEntry`'s seven captures reused as the seed for the L1 re-fetch. Results carry no per-seat status or id (the dispatcher's known gap); delivery is evidenced by the eight committed reports.
- **Wave 2** (`kotodama-r90-v2`, this attempt: spec `spec-v2.json` validated against `ufo-wave-policy.json` (band 8–16), `w2-dispatch.json`, ready `w2.ready` with `l1: KotodamaR90`): 11 seats — 3 executor (`ExecVerifyQuotes`, `ExecCounterAtLands`, `ExecIndexCheck`), 2 reviewer (`ReviewerEntry`, `ReviewerChrome`), 1 critic (`CriticClaims`), 1 mutation-tester (`MutationTester`), 1 sentinel (`Sentinel`), 1 scout (`ScoutFrontier`), 1 connector (`ConnectorSiblings`), 1 scribe (`ScribeReceipts`); attack 5/11. All eleven delivered; results `w2-results.json`.

**Wave-2 handoff note:** the dispatcher wrote `w2-results.json` and all eleven seat reports, but no `WAVE-DONE` message reached this L1. The settled results file plus eleven committed seat reports are treated as the handoff, and the report is filed after them, not before.

What the wave established, and what it broke:

- **The frozen claims reproduce from outside.** `ExecCounterAtLands` re-ran both claims from a clean clone (`MEASURE90-O: PASS legs=6/6`, `MEASURE90-C: PASS legs=4/4`); `ExecVerifyQuotes` re-fetched the eight URLs and matched seven captures byte-for-byte or on content-line diff (S947/S948 differ in two per-request token lines only; the S949 quote was the one real mismatch and was corrected); `ExecIndexCheck` reproduced `CORPUS-INDEX: OK files=262 rows=262 findings=0`, census `rc=0` with no warning naming S942–S951, and all five census clauses clean for the new rows.
- **Six content defects in the entry, one in the lesson** (`ReviewerEntry` D1–D6, fixed at `e0795be6`): the WALS 72 design-consequence cell called the maximal system "marked" and claimed most languages grammaticalise a minimal imperative, contradicted by the same cell's counts (minimal-only 20 of 375, "neither" 201); "chapters 72 and 73 explicitly set non-inflectional wish expressions aside" was false for 72; "eleven words" for an eight-word translation; the prohibitive tricolon dropped the 55 class; an uncited breach inventory and two argument-structure glosses read as source-backed (now marked as design reading); the lesson miscounted six `mined` rows for seven. No graded leg could catch any of these — the counter counts structure and gate binding, not the truth of the prose.
- **The entry-mode grader has real holes; the landed bytes are clean of them.** `ReviewerChrome` built five sandbox counterfeits on top of the landed revision: title-chrome gate quotes, a capture fabricated with its quote, a graded-file capture path, a repeated-sentence entry and a shadow duplicate registry id. The first, second and fifth pass the frozen counter; the third and fourth are refused. Its scans of the landed bytes for all five classes came back clean, and a 66 KB hollow entry also passes 6/6.
- **Adjacency** (`ConnectorSiblings`): lore already records a fictional Moon-Basin Vow with two contradictory accounts of its site; that is event ownership, not grammatical-design ownership. The new entry stays a design surface, resolves no canon, and hands the register off through the integration contract. No contest, no absorption.
- **Conduct** (`Sentinel`): no credential shape or `op://` in the round's new files; every manifest capture is a tracked lane file with a matching hash; every round-90 commit carries the lane identity and no seat commit exists; 8/8 captures HTTP 200 with no challenge, login or paywall wall (S948's `captcha` string is the site's feedback widget). Two reds are recorded rather than repaired: `tools/check-cited-records.py` exits 1 because eleven round-90 receipts echo `/fast/scratch` `--work` roots in recorded command lines (the base was already red with three inherited `/tmp` echoes, and no capture is outside the lane), and the `/tmp` trees the sentinel attributed to an L1 are not this attempt's writes and are left untouched.
- **Frontier** (`ScoutFrontier`): ranked next surfaces for the linguistics partition, each with the grep that shows the lane does not hold it; recorded in its report.

## Open items, routed

1. **L0 (open, unanswered).** `kotodama | round-11` (freshness drift threshold) and `kotodama | round-89` (does live re-verification sit inside that pause) still gate any freshness claim. This round moved coverage instead and did not block on an answer.
2. **Frozen-text defects, disclosed not repaired.** `O.after_target` misdescribes the stub receipt's failure mode (it fails REFUSALS and MUTATION, not SELFTEST), and `O.before` cites `reports/round-89/mutation-score.txt`, which does not exist (the receipt is `.ufo/waves/round-89/w1/MutationCounter.md`). The frozen file is not edited; the O verdict does not depend on either sentence.
3. **Grader coverage gap.** Entry mode refuses neither a title/chrome quote nor a co-fabricated capture, does not check duplicate lands ids, and does not apply the self-quote test; fourteen of twenty-one independent mutants survive it. Routed to round 91 as a new counter revision with the critic's three comparisons plus the surviving sub-checks.
4. **Registry.** `tools/check-gate-registry.py` reports `0 missing / 86 registered` and lists 26 tools without a row; `tools/check-advance-evidence.py` is not yet in the `SKILL.md` gate table, and the SCORECARD capability row is its register entry for now.
5. **Inherited debts** (unchanged, not closed here): numeric/lowest-axis mapping (R86-C1), formal L2-planner conflict (L0 `kotodama | round-86`), the full cited-record red from the non-author r84 spot-check, and the r88 counterfeit controls' `KOTODAMA_ROOT` requirement (R88-V3).

## Stale-lane

Respawn-per-round driver; this lane holds no other open mission. Round work is committed and pushed at `6394ad43`, and this report is the last artefact to land.

## Tool installs

None this round. pacman stayed paused; no `uv tool`, `npx` or binary install was needed (curl, git, python3 and coreutils only).
