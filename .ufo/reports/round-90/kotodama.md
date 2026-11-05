# kotodama — round 90 (hyaku run 15, attempt 1)

lane: kotodama-shokunin · round: 90 · campaign: hyaku · date: 2026-11-04/05 (−03:00)
base: `6b0b86e45ae902331aca75863db380f2991458c4` · freeze: `d0b6f2a7f9cc36272682749a9b047b739406f0c8`
claim-C lands: `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761` · lane tip at report: `26e30795ce8513cb3cd888af676ad1ed3e31723a`

## Work performed

Declared claims (frozen before data, `reports/round-90/claims.json`):

- **O / operability — capability acquisition.** `tools/check-advance-evidence.py`, a landing-evidence grader that refuses the thirteen counterfeit classes the round-89 wave demonstrated, with a 67-check selftest carrying one negative per sub-check and a committed 43/43 mutation receipt.
- **C / coverage — sourced claim.** One new linguistics entry, `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, over seven sources opened this round (S942–S948; S949 retained as a rejection).

Freshness is the lane's historically lowest axis and is **paused** by the open L0 questions `kotodama | round-11` and `kotodama | round-89` (round-89 spot-check §6.1 forbids a further freshness move until ruled). Coverage is therefore the axis this round works directly, on ground the coverage map did not hold.

Work items, each with its evidence pointer:

- **Freeze and controls, before any data** — `d0b6f2a7` (claims, counter, grader, mutants), `9fb2c58f` (at-freeze control receipts and counter revisions 2–5), `ebd81b1b` (revision 6, the ENTRY-verdict keying defect a wave seat reported). `reports/round-90/counter-revisions.md` records every revision with the reason and the sha256; no leg, threshold, predicate or constant changed.
- **Inherited attempt resolved** — the earlier attempt of this round committed `d0b6f2a7 … 945e6a3e` and died on provider failure. Reused after re-verification: the grader, the counter, the mutant generator, the at-freeze and stub receipts, the mutation receipt (43/43), eight seat reports under `.ufo/waves/round-90/w1/`, and the frozen claims. Discarded: its wave roster (its seats produced no landing), and its seven captures, which had no manifest — replaced by L1 re-fetches with a manifest (`reports/round-90/evidence/`). Named as R90-M4 in the lesson.
- **Claim C landing** — entry 19,930 B with ten `##` sections and a five-row typology table; registry rows S942–S948 admitted (six A, one B; all `mined`, `opened 2026-11-04`, `used-by` the entry) and S949 rejected with its flip condition; lesson gate lines with one located quote per id; eight committed captures plus `manifest.json` (sha256, http_status, local fetch instant); `corpus/README.md` row and count moves. Lands `7f3a7aa6`.
- **Source-conduct check** — every source opened by ordinary HTTP (`curl -sS -L`), no browser, no challenge, no login. The seed list was wrong in three places and opening the pages caught it: WALS chapter 74 is Situational Possibility (the Prohibitive is chapter 71), `glossary.sil.org/term/vocative` is 404 while `/term/vocative-case` answers, and the SIL glossary has no prayer, invocation, supplication, petition, vow, votive, blessing or curse term at all (nine-term 404 sweep, lesson R90-M9).
- **Measurement** — `reports/round-90/final/lands-O.txt` `MEASURE90-O: PASS legs=6/6`, `final/lands-C.txt` `MEASURE90-C: PASS legs=4/4`, `final/separability.txt` `SEPARABILITY: PASS` with each claim graded only by its own overlay (other claim's paths absent O 6/6, C 4/4).
- **Frontier step** — `corpus/SOURCES.md` census exit 0 at start (`reports/round-90/census-start.txt`) and end (`census-end.txt`); seven rows opened and admitted, one rejected; lesson `## Gate` carries URL, access date and quote for every new row; `## Mistakes` carries R90-M1 … R90-M9.
- **Scope and sweep** — no write outside `kotodama-shokunin/` and this report; the fleet-root sweep shows `.scratch/run15-state.json` (orchestrator), `.ufo/reports/round-86/kama.md` (kama lane) and `mo.tip` (0 bytes, 23:58, names neither this lane nor this round) — none is a kotodama misroot, none touched.

### Falsification findings the frozen instrument does not cure

The inherited wave's critic (`CriticClaims`, committed) attacked the frozen predicate before the landing and its verdicts stand as bounds on O and C; the claims are frozen, so none of them can be repaired inside this round:

| attack | claim/leg | verdict | what it means here |
|---|---|---|---|
| an 11-line stub printing the tally line and the 13 case names passes SELFTEST + REFUSALS + STUB | O | weakened | only TOOL and MUTATION carry discrimination against a non-implementing tool |
| STUB leg is substring presence over a receipt whose stub source is not committed | O | broken as stated | the receipt records the stub *passing* SELFTEST and failing REFUSALS and MUTATION; the frozen `after_target` sentence says otherwise (reported, not edited) |
| an off-topic entry can satisfy TOPIC's word-overlap test | C | broken as a discriminator | the landed entry is on topic by construction and by the reviewer seat, not by the counter alone |
| NEWIDS does not exclude a junk or URL-colliding new row in entry mode | C | weakened | the seven landed rows are each URL-distinct from the base registry and each carries a located gate line and capture |
| `C.surface` prose is false at base as written; the operative unmoved-command holds | C | broken as written | recorded as R90-M8 and re-measured in the lesson; the frozen text is not edited |
| APPENDONLY catches a direct re-date but not a lesson-only re-verify | C | weakened | no row was re-dated or re-verified this round (0 changed cells) |

The smallest safe corrections the critic proposed (fail on duplicate lands ids, fail on a qualifying row whose URL already exists at base, apply the self-quote test in entry mode) are routed to round 91: the tool is sha256-pinned by the frozen O predicate, so changing it now would fail O by construction.


## Landed changes

Each change is tied to the `LOG.md` round-90 entry (`LOG.md`, "## Round 90") and to the commit that carries it.

| change | commit |
|---|---|
| claims, frozen counter, grader `tools/check-advance-evidence.py`, mutant generator and at-freeze controls | `d0b6f2a7` |
| at-freeze control receipts, counter revisions 2–5 | `9fb2c58f` |
| inherited v1 wave spec, validated dispatch, ready handoff | `c0c628d8` |
| counter revision 6 (ENTRY verdict keying), frozen bytes unchanged | `ebd81b1b` |
| in-flight preservation of the dead attempt (not a landing) | `945e6a3e` |
| entry, registry rows S942–S949, lesson, README moves, evidence + manifest, separability harness, census end | `7f3a7aa6` |
| entry correction after the reviewer's D1 defect (WALS 72 definitions) | `3f56892f` |
| reviewer D1–D6 content fixes, S949 quote fix, census end refresh | `e0795be6` |
| rejection rows S950 and S951 with gate lines and captures | `210c0dd0` |
| w2 spec, validated dispatch, ready handoff (11 seats), separability overlay set fix | `fe59fc35` |
| lesson base-surface correction and R90-M7/M8/M9, counter receipts at lands, separability receipt | `19187112` |
| `LOG.md` round-90 entry, `SCORECARD.md` round-90 rows and the grader capability row | `195aff9c` |
| six reviewer-found content defects fixed in the entry and the lesson (WALS 72 marked-class claim, chapter-72 exclusion, word count, prohibitive values, uncited breach inventory, S949 quote) and the census end receipt regenerated | `e0795be6` |
| settled wave-2 evidence: eleven seat reports with their stage, `w2-results.json`, the ready handoff and the tip measurement receipts | `26e30795` |

## Before → after measurements

Frozen counter, unchanged after data: `reports/round-90/measure90.py` (sha256 `6e1ea6a5…`, rev 6, `COUNTER AT LANDS … same=yes`).

| claim | before | after | counting command | measured at |
|---|---|---|---|---|
| O / operability | `tools/check-advance-evidence.py` absent at base (`git cat-file -e` fails); the round-89 predicate accepted five counterfeit landings its own wave built and scored 10/41 mutants | tool present at the freeze pin (sha256 `121888f0`), `SELFTEST PASS 67/67` with all 13 refusal cases ok, `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern`, stub control recorded (`SELFTEST PASS 67/67` fake, REFUSALS 0/13, `0/43 killed` with 43 broken-pattern) — `MEASURE90-O: PASS legs=6/6` | `python3 -B reports/round-90/measure90.py --root <clone> --freeze d0b6f2a7f9cc36272682749a9b047b739406f0c8 --lands 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 --claim O --work <existing-dir>` | `7f3a7aa6`, receipt `reports/round-90/final/lands-O.txt` |
| C / coverage | no dedicated entry; linguistics partition 34 files; registry 865 rows; 0 new ids | entry 19,930 B, 10 `##` headings, table 6×4; linguistics 35 files, knowledge 262; registry 873 rows with S942–S948 mined and cited (S949 rejected); index `CORPUS-INDEX: OK files=262 rows=262 findings=0`; zero base rows changed — `MEASURE90-C: PASS legs=4/4` | `python3 -B reports/round-90/measure90.py --root <clone> --freeze d0b6f2a7f9cc36272682749a9b047b739406f0c8 --lands 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 --claim C --work <existing-dir>` | `7f3a7aa6`, receipt `reports/round-90/final/lands-C.txt` |

Both claims were re-measured at the corrected tip `e0795be69fffc92a06e2c954bc9b36c68af77df4` (the commit that carries the reviewer's content fixes) with the same frozen counter: `MEASURE90-O: PASS legs=6/6` and `MEASURE90-C: PASS legs=4/4` (`reports/round-90/final/lands-O-tip.txt`, `lands-C-tip.txt`). The graded C object at that tip is the entry at 20,400 B; the structural legs (size, headings, table, topic overlap, new ids, gate, captures, index, appendonly) are unchanged. Both claims were re-measured a third time at the final lane tip `26e30795ce8513cb3cd888af676ad1ed3e31723a` (which only adds the settled wave-2 evidence and the tip receipts) with the same frozen command: `MEASURE90-O: PASS legs=6/6` (`MUTATION 43/43 killed, 0 survived, 0 broken-pattern`; STUB recorded) and `MEASURE90-C: PASS legs=4/4` (`CORPUS-INDEX: OK files=262 rows=262 findings=0`; APPENDONLY clean).

Separability, on the first lands (`reports/round-90/final/separability.txt`): overlay O `PASS legs=6/6` with the six C paths absent, overlay C `PASS legs=4/4` with the four O reward paths absent; shared paths are the frozen config, the counter and the instrument only.

## Sources & frontier

Counting command (both ends, exit 0):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

| quantity | before (`6b0b86e4`) | after (`19187112`) |
|---|---|---|
| rows | 865 | 875 |
| tiers | A=511 B=329 C=25 | A=517 B=330 C=28 |
| status | mined=762 queued=58 rejected=45 | mined=769 queued=58 rejected=48 |
| changed old rows | — | 0 (cell-wise compare of all 11 columns) |
| removed old rows | — | 0 |
| census rc | 0 (`census-start.txt`) | 0 (`census-end.txt`) |

Rows added by tier: seven admitted (six A — S942 WALS ch. 72, S943 WALS ch. 73, S944 WALS ch. 71, S946 AIO IGI3 646, S947 Blidstein PLOS One, S948 Galofaro & Kubas OASIcs; one B — S945 SIL glossary `vocative-case`), three rejected C (S949 Wikipedia *Votive offering*, S950 *Curse tablet*, S951 *Sacred language*, each with its flip condition). Rows touched old→new: none — no `status`, `recheck` or `used-by` cell of a pre-existing row changed, because freshness is paused and nothing was re-verified this round. Frontier rows advanced: none (no frontier promotion claimed; `corpus/README.md` gains one index row and the partition/total arithmetic only).

Assimilation: none — the lane has no `considerthese/` directory, and the shokuknow package adoption stays closed under the wave-4 quarantine-first rule.

## Trend verdicts

- **expansion: improved.** One admitted `knowledge/` entry on ground the coverage map did not hold, citing seven `mined` rows opened this round (six A, one B) with a README index row and a new partition count; eight-word shingle overlap with the nearest entries is not claimed here and is left to the non-author closure. The base surface was carried only as sub-sections (`carthage.md:1`, `sacred-topography-pilgrimage.md:1` and `:74`, `religion-language-co-evolution.md:1` and `:64`, `tibet.md:92`, `direction-symbolism.md:129`), so the entry adds a topic, not a copy.
- **quality: improved.** The round's own instrument is the improvement: a grader whose selftest holds one negative per sub-check (67 checks) and whose mutation pass is 43/43, against the round-89 predicate that a wave demonstrably passed with five counterfeits at 10/41. No admitted entry was found false; the one registry row whose `teaches` cell could overreach (S947, a distant-reading abstract) is scoped to the abstract's own findings in the row itself.
- **discernment: unchanged (pending the non-author spot-check).** The round turned three inherited or fresh disagreements into lesson rows with fixes (R90-M3 counter keying, R90-M7 separability set bug, R90-M8 base-surface wording) and one honest limit (R90-M6, a vacuous green from a tool pinned to another round). A dispatched seat is still the lane, so no verdict above `unchanged` is claimed until an outside spot-check samples this round's admits and its one rejection.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — asserted: no `[x]` this round. SKILL unchanged; the round's craft lives in the entry's design procedure and its eight failure checks, and the new gate is registered in `SCORECARD.md` capabilities, not in `SKILL.md`.
[~] At least one end-to-end domain task executed and logged in LOG.md — asserted: the entry's procedure §6 was executed against the seven opened sources (mood decision, prohibitive strategy, address system, vow formula with receipt, votive object inventory, archaism list, litany ordering principle, failure cases); LOG.md "## Round 90".
[~] Instructions executable by an agent without oral context — asserted: `python3 -B tools/check-advance-evidence.py --selftest --work <dir>` and the frozen counter commands in `reports/round-90/claims.json` run without lane-specific context; `reports/round-90/final/lands-{O,C}.txt` record the runs.
[~] No cross-domain bleed (PROVINCE.md still accurate) — asserted: the entry is a design surface, hands the register to lore as a handoff and leaves canon, research method and rights to their owners; PROVINCE.md unchanged this round.

## Round shape

Claim C landed and O's frozen legs were graded before the falsification wave. Wave 2 (`kotodama-r90-v2`, spec `.ufo/waves/round-90/spec-v2.json` validated against `ufo-wave-policy.json`, band 8–16, dispatch `.ufo/waves/round-90/w2-dispatch.json`, ready handoff `w2.ready`, l1 `KotodamaR90`):

The round ran two v1 waves in the run-15 band (8–16 seats each), 23 seats in total and no residual call. Wave 1 (`kotodama-r90-v1`, spec `.ufo/waves/round-90/spec-v1.json`, dispatch `w1-dispatch.json`, ready `w1.ready`, results `w1-results.json`): 12 seats — 2 scribe (`ScribeEntry`, `ScribeLesson`), 4 executor (`ExecIndepRefetch`, `ExecMirrorGate`, `ExecSeparability`, `ExecReadme`), 1 scout (`ScoutRecon`), 1 connector, 2 reviewer, 1 critic, 1 mutation-tester; attack 4/12. Wave 2: 11 seats — 3 executor (`ExecVerifyQuotes`, `ExecCounterAtLands`, `ExecIndexCheck`), 2 reviewer (`ReviewerEntry`, `ReviewerChrome`), 1 critic (`CriticClaims`), 1 mutation-tester (`MutationTester`), 1 sentinel (`Sentinel`), 1 scout (`ScoutFrontier`), 1 connector (`ConnectorSiblings`), 1 scribe (`ScribeReceipts`). Attack seats 5/11 (reviewers, critic, mutation-tester, sentinel). Two reviewers and one mutation-tester, no second connector. Results file `.ufo/waves/round-90/w2-results.json`; seat reports under `.ufo/waves/round-90/w2/`.

What the wave established, and what it broke:

- **The frozen claims reproduce from outside.** `ExecCounterAtLands` re-ran both claims from a clean clone (`MEASURE90-O: PASS legs=6/6`, `MEASURE90-C: PASS legs=4/4`); `ExecVerifyQuotes` re-fetched the eight URLs and matched seven captures byte-for-byte or on content-line diff (S947/S948 differ in two per-request token lines only); `ExecIndexCheck` reproduced `CORPUS-INDEX: OK files=262 rows=262 findings=0`, census `rc=0` with no warning naming S942–S949, and all five census clauses clean for the new rows.
- **Six content defects in the entry, one in the lesson** (`ReviewerEntry` D1–D6, all fixed at `e0795be6`): the WALS 72 design-consequence cell claimed the maximal system is "marked" and that most languages grammaticalise a minimal imperative — contradicted by the same cell's counts (minimal-only 20 of 375, "neither" 201); "chapters 72 and 73 explicitly set non-inflectional wish expressions aside" was false for 72; "eleven words" for an eight-word translation; the prohibitive tricolon dropped the 55 class; an uncited breach-inventory sentence and two argument-structure glosses read as source-backed (now marked as design reading); the lesson miscounted six `mined` rows for seven. The graded legs did not catch any of these — the counter counts structure and gate binding, not the truth of the prose.
- **The entry-mode grader has real holes, and the landed bytes are clean of them.** `ReviewerChrome` built five sandbox counterfeits on top of the landed revision: a title-chrome gate quote, a capture fabricated with its quote, a graded-file capture path, a repeated-sentence entry and a shadow duplicate registry id. The first, second and fifth pass the frozen counter (rc 0, `MEASURE90-C: PASS 4/4`); the third and fourth are refused. Its scans of the landed bytes for all five classes came back clean, and a 66 KB vacuous "hollow" entry also passes 6/6 — the six C legs prove structure, never content.
- **The selftest's entry-mode coverage is thin.** `MutationTester` reproduced the committed 43/43 and then wrote 21 new single-point mutants; 14 survive `SELFTEST PASS 67/67`, each proven behaviourally different from the clean bytes (table-shape and topic floors off by one, NEWIDS status/base-subtraction, gate-quote selection and URL-slash relaxation, capture confinement, traversal guard, sha256 skip, http-status widening, fetched-date check, registry indentation bounds, duplicate-row leniency). "One negative per sub-check" is therefore true of the commit-blocking checks the selftest exercises, not of the entry-mode sub-checks.
- **Non-discriminating legs** (`CriticClaims` F3–F11): `MATERIALIZE` and `INDEX` pass at base; `SELFTEST`/`REFUSALS` are self-attested (a 10-line tool passes both); `STUB` passes a receipt that records the stub passing SELFTEST; `MATERIALIZE`/`INDEX` are not C landing signals. Its F11 is a real citation defect in the frozen claims file: `O.before` cites `reports/round-89/mutation-score.txt`, which exists neither at base nor at HEAD — the actual round-89 receipt is `.ufo/waves/round-89/w1/MutationCounter.md`. The file is frozen and is not edited; the correct pointer is recorded here.
- **Adjacency** (`ConnectorSiblings`): lore already records a fictional Moon-Basin Vow with two contradictory accounts of its site; that is event ownership, not grammatical-design ownership. The new entry stays a design surface, resolves no canon, and hands the register off through `synthesis/worldbible-integration-contract.md`. No contest, no absorption.
- **Conduct** (`Sentinel`): no credential shape or `op://` in the round's new files; every manifest capture is a tracked lane file with a matching hash; 10/10 round-90 commits carry the lane identity and no seat commit exists; 8/8 captures HTTP 200 and no challenge/login/paywall wall (S948's `captcha` string is the site's feedback widget). Two reds are recorded rather than repaired: `tools/check-cited-records.py` exits 1 because eleven round-90 receipts echo `/fast/scratch` `--work` roots in recorded command lines (the base was already red with three inherited `/tmp` echoes; no capture is outside the lane), and the six `/tmp` trees the sentinel attributed to an L1 are not this attempt's writes and are left untouched.
- **Frontier** (`ScoutFrontier`): ranked next surfaces with the commands that show them unheld; recorded in its report.


Residual call: none. Planner seat: the L1 holds the canonical §3 planner seat (the validator rejects `planner` as a swarm role); a bounded planning data-walk rode the scout item. Formal L2-planner conflict remains open as L0 `kotodama | round-86`.

## Open items, routed

1. **L0 (open, unanswered).** `kotodama | round-11` (freshness drift threshold) and `kotodama | round-89` (does live re-verification sit inside that pause) still gate any freshness claim. This round moved coverage instead and did not block on an answer.
2. **Frozen-text defect, disclosed not repaired.** `claims.json` `O.after_target` says the stub receipt records the stub "failing SELFTEST and MUTATION"; the committed bytes record a fake `SELFTEST PASS 67/67` and failure at REFUSALS and MUTATION. The frozen file is not edited (R90-M3 area; the O verdict does not depend on the wording, since the MUTATION and REFUSALS legs carry the discrimination).
3. **Grader coverage gap.** Entry mode does not refuse a title/chrome quote or a co-fabricated capture; advance mode does. The attack seats and the non-author closure are the defence this round; a future round should move those refusals into entry mode.
4. **Registry.** `tools/check-gate-registry.py` reports `0 missing / 86 registered` and lists 26 tools without a row; `tools/check-advance-evidence.py` is not yet in the `SKILL.md` gate table, and the SCORECARD capability row is its register entry for now.
5. **Inherited debts** (unchanged, not closed here): numeric/lowest-axis mapping (R86-C1), formal L2-planner conflict, the full cited-record red from the non-author r84 spot-check, and the r88 counterfeit controls' `KOTODAMA_ROOT` requirement (R88-V3).

## Stale-lane

Respawn-per-round driver; this lane holds no other open mission. The full report lands after the lane commits and cites the pushed lane tip.

## Tool installs

None this round. pacman stayed paused; no `uv tool`, `npx` or binary install was needed (curl, git, python3 and coreutils only).
