# kotoba — round 90 (attempt 1) report

Lane: kotoba (prompt & skill craft). Host: Linux, omp 18.15.0. Lane pushed tip (pre-report gate):
`10c9a3cdd0eaaf087d1e477d49dc3767465dd28f` (`git ls-remote origin refs/heads/master` = `state … local=… remote=… ahead=0`).
Round shape: one v1 wave `r90-w1`, 13 seats, band 8–16 (policy `ufo-wave-policy.json`), WAVE-DONE received, `r90-w1-results.json` lists all 13 seats with final output.

## Work performed

Declared claims (2, both frozen before any candidate score; `plans/round-90.md`, controls `plans/round-90-controls.md`):

- **C1 — depth** (owned lowest, score 9 held; claim type **capability acquisition**): a committed mutation-battery runner `verifiers/check_mutation_battery.py` over the two round-89 gates, two-sided per Q47 (declared kill-class mutants must flip a probe; generated equivalents must leave every probe identical). Verdict basis below.
- **C2 — freshness** (advisory; tied-lowest 8 under the all-axes reading; claim type **measured axis-move**): the host installed-skill census re-run on this host's live skills root `/home/vgpnk/.agents/skills` (the round-82/84 method), with the NAME-COLLISION ledger.

Work items, each with its evidence pointer:

- Protocol load and lane state: `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md`, `PROTOCOL.md`, lane `SCORECARD.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md` § Frontier, `considerthese/2026-10-26.md`, round-89 closure `corpus/lessons/round-89-verifier-spotcheck.md`. Base `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`; `jj-lane.sh state` clean at start.
- Base measurements re-run at the round base (not copied from round 89): `.ufo/waves/round-90/receipts/base-*.txt` (floors red `registry size drift` and `row vanish: freeze_gate`; integrity `unindexed 1`; D5 base receipt `closed 4 of 5, instance drift 4`; tip battery `2 of 6`; sibling census `province rows 20 matched 4`; SKILL.md 600 lines, 164 lines > 120 chars, longest 1491).
- Pre-data controls: `python3 -B verifiers/check_freeze_gate.py --plan plans/round-90-controls.md` → `freeze gate: 6 control(s) held — freeze may proceed`, exit 0 (`.ufo/waves/round-90/receipts/freeze-gate-r90.txt`); six shortcut worlds (C1: no instrument, r89 wave harness, stub; C2: Windows-root form, empty root, one-file root) each reach no predicate. Plan + controls committed `6af71591e7232a7eebbaff78e7db653a70c7218b`.
- Wave `r90-w1` (13 seats; roles and results in § Wave shape).
- Pre-score amendments from the wave's pre-landing findings, committed before the landing measurement: `plans/round-90-addendum-1.md` (`634f9f8739a9e6b243e3c3a157a9a72d7158e7ff`): A1 d5-m1a survivor → kill (its d5iii leg is active at the final bytes, `.ufo/waves/round-90/w1/ExecBattery/d5-m1a-evidence.txt`); minimum pins M ≥ 8, E ≥ 4; A2 wording bounds on the equivalence leg and the kill set; A3 the C2 comparison-empty bound; A4 SOURCES row fixes.
- Battery built and self-tested: `verifiers/check_mutation_battery.py` (ExecBattery; predicate sentence byte-equal to the plan line), manifest `verifiers/fixtures/mutation-battery/manifest.tsv` (14 kill, 6 equivalent, 0 survivor after A1), self-test `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 19 assertions`, exit 0. The satisfying self-test world needed five new real fixture kills (`fx-k5`…`fx-k9`) and the expected-line constants moved to `(8, 8, 6, 6, 1, 1)`, `(8, 9, 6, 6, 1, 1)`, `(8, 8, 5, 6, 1, 1)`; the predicate line itself did not change beyond the A1 pin.
- Carry-in repairs routed into the wave: floors half-bump (`verifiers/floors-registry.json` `instrument_total` 18 → 19; `freeze_gate` added to both guard tables and the F6 literal; ExecFloorsBump, `.ufo/waves/round-90/receipts/floors-selftest.txt` `0 failure(s) over 165 assertions`, `floors-live.txt` rc 0, `floors-regression.txt` reproduces the two base FAIL lines byte-for-byte, rc 2); unindexed round-89 spot-check row (ExecIndexRow).
- Host census: `python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills --fleet-root /home/vgpnk/Projects/shokunin` → `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, exit 0 (`.ufo/waves/round-90/receipts/c2-host-census.txt`, measured-rev `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`); NAME-COLLISION ledger `c2-name-collisions.txt`: count 0 over 83 surfaces.
- Attacks (wave seats; full files under `.ufo/waves/round-90/w1/`): ReviewerRepairs (floors and index repairs `sound`, `no_new_red: true`); ReviewerBattery F1 HIGH (the battery and manifest were untracked, so no committed revision could be measured; resolved by landing them); CriticClaims F1 (C2 census passes with zero identity comparisons; bounded by A3), F6/F7 (empty manifest; circular "equivalent" wording; answered by A1/A2), F15/F16 (SOURCES `teaches` wording and premature `mined`; fixed); MutTesterBattery (16 of 19 battery mutants killed; 5 of 5 equivalent rewrites survived; the three survivors are the battery's own G1 commit-check skip `mb-m2`, G1 clean-tree guard off `mb-m15`, and revision-copy restore not re-read `mb-m16`, routed to round 91); SentinelScope (no out-of-map writes, no misroot, `user.max_user_namespaces` unchanged at 122865).
- Knowledge and lesson: `corpus/knowledge/mutation-battery-round90.md` (provenance trio; counts corrected to 14/6/0; bounds), `corpus/knowledge/host-census-round90.md`, `corpus/lessons/round-90.md` (Gate, Mistakes, Considerthese, Seat record, Closure status), Q82 in `corpus/QUALITY.md`.
- Index: `corpus/README.md` rows for the three round-90 corpus files (see the late-found defect below).
- Landing receipts: `.ufo/waves/round-90/receipts/landing-*.txt` (battery, registry, tip battery, checklist, sibling census, SKILL.md size, D5 base receipt), `index-final.txt`.

**Late-found defect (routed, repaired in-round, disclosed):** the integrity gate read `unindexed 0` at landing, measured while the three new round-90 corpus files were still untracked. Once tracked, it reads `unindexed 3` (`corpus/knowledge/host-census-round90.md`, `corpus/knowledge/mutation-battery-round90.md`, `corpus/lessons/round-90.md`). Repaired by three index rows in `corpus/README.md` (commit `10c9a3c`); the landing-time `unindexed 0` reading is not cited as evidence for the landed tree. Q-class: an index row is a claim written when the file is tracked (CORPUS.md § index row).

## Landed changes

Each commit is a lane commit via `jj-lane.sh`, pushed to `origin/master`:

| Change | LOG.md entry | Commit |
|---|---|---|
| Plan and pre-data controls (frozen before any candidate score) | `LOG.md` § Round 90 — freeze entry | plan `6af71591e7232a7eebbaff78e7db653a70c7218b`; LOG freeze entry `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c` |
| Pre-score amendments A1–A4 | `plans/round-90-addendum-1.md` (SCORECARD Round 90 annotation) | `634f9f8739a9e6b243e3c3a157a9a72d7158e7ff` |
| Battery runner, manifest, registry row, floors half-bump, unindexed-row repair (ExecIndexRow), corpus material (landing) | `LOG.md` § Round 90 — landing and measurements | `1cb07ba90fccc17ffb9cc86f6e2ab95b6a9347e4` |
| Lesson seat record and closure status; SCORECARD annotations and capability row; LOG landing entry; wave evidence and landing receipts | `LOG.md` § Round 90 — landing and measurements; `SCORECARD.md` § Round 90 | `14912bfc6927c77a2613cb742e61ab668f17c2b8` |
| Index rows for the three round-90 corpus files | (index rows; no separate LOG entry) | `10c9a3cdd0eaaf087d1e477d49dc3767465dd28f` (lane tip) |

Files touched in the lane (by commit above): `verifiers/check_mutation_battery.py` (new), `verifiers/fixtures/mutation-battery/manifest.tsv` (new), `verifiers/fixtures/round-90/*.sh` (six controls, new), `verifiers/check_assertion_floors.py` and `verifiers/floors-registry.json` (floors half-bump), `SKILL.md` (battery registry row; intro lines joined; 600 lines), `corpus/SOURCES.md` (S260, S261 appended; S260 and S261 `queued` → `mined`, old→new logged in `corpus/lessons/round-90.md` § Sources), `corpus/QUALITY.md` (Q82 appended), `corpus/README.md` (index rows), `corpus/knowledge/mutation-battery-round90.md` and `corpus/knowledge/host-census-round90.md` (new), `corpus/lessons/round-90.md` (new), `SCORECARD.md` (round-90 annotations; capability row), `LOG.md` (freeze and landing entries), `plans/round-90.md`, `plans/round-90-controls.md`, `plans/round-90-addendum-1.md` (new), `.ufo/waves/round-90/**`.

## Before → after measurements

**C1 — depth (capability; mutation battery).** Predicate (frozen; `plans/round-90.md` § C1 as amended by A1–A2): `python3 -B verifiers/check_mutation_battery.py --rev <rev> --work <scratch>` prints `mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`, exit 0 iff K == M, M >= 8, E == E, E >= 4, S == S_declared and G1–G3 PASS.

- Before (base `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`): no instrument. `git grep -n 'mutation_battery' 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5 -- verifiers plans` → exit 1 (`.ufo/waves/round-90/receipts/before-c1-absence.txt`).
- After (landing `1cb07ba90fccc17ffb9cc86f6e2ab95b6a9347e4`): `mutation battery killed 14 of 14 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, exit 0; G1, G2 (20 mutant copies and 2 revision copies read back), G3 (1 SKILL.md line) PASS (`.ufo/waves/round-90/receipts/landing-battery.txt`).
- Self-test: `python3 -B verifiers/check_mutation_battery.py --self-test` → `0 failure(s) over 19 assertions`, exit 0 (run on the working tree that became `1cb07ba`, before the commit; the self-test reads only committed-form fixtures, and was not re-run at a later revision).
- Registry: `python3 -B verifiers/check_gate_registry.py --rev 1cb07ba90fccc17ffb9cc86f6e2ab95b6a9347e4` → `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, exit 0 (`landing-registry.txt`; base was 73 of 73 at `99ddd746`).

**C2 — freshness (measured; host installed-skill census on the live root).** Predicate (frozen; `plans/round-90.md` § C2): `python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills --fleet-root /home/vgpnk/Projects/shokunin` → `host skill surfaces measured N: identical I, drifted D, lane-absent A` with I + D + A == N == 83, exit 0; plus receipts.

- Before (base `0c20d8ab…`): no census receipt names this host's live root. `git grep -l 'home/vgpnk/\.agents/skills' 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5 -- .ufo/waves corpus verifiers receipts` → historical notes only (`.ufo/waves/round-90/receipts/before-c2-sweep.txt`); the stored round-84 receipts name the Windows roots.
- After (measured-rev `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`; the census reads the live root and does not depend on the lane revision): `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, exit 0 (`c2-host-census.txt`). NAME-COLLISION count 0 (`grep -c 'NAME-COLLISION' .ufo/waves/round-90/receipts/c2-name-collisions.txt` → 1, the count line only, with 0 pair rows).
- Comparison outcomes: none (zero identity comparisons; addendum A3). The claim re-verifies the method on the live surface; it does not produce identical or drifted findings on this host.

**Carry-in (not claims).** Floors: `python3 -B verifiers/check_assertion_floors.py` red at base (`registry size drift: instrument_total=18 but 19 entries`; `row vanish: freeze_gate`) → `PASS freeze_gate observed=30 floor=30`, rc 0 at landing (`floors-live.txt`). Integrity: `unindexed 1` at base → `unindexed 0` at the index-fixed tree, with the late-found three files now indexed (`index-final.txt`). Tip battery at `1cb07ba`: `guards 4 of 5; tip battery exit 0: 3 of 6`, rc 1 (`landing-tipbattery.txt`; base `2 of 6`).

**No-harm readings at landing (carried reds named, unchanged or improved):** sibling census `province rows 20 matched 4`, rc 1 (unchanged, `landing-siblingcensus.txt`); D5 base receipt `closed 4 of 5, instance drift 4`, rc 1 (unchanged, `landing-d5v3.txt`); checklist `governance.citation_resolves` red (carried; `landing-checklist.txt` lists the FAIL box); SKILL.md 600 lines, 92 672 B, 165 lines > 120 chars (164 at base; +1 registry row), longest 1491 (unchanged) (`landing-skillmd-size.txt`); census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok` (33 pre-existing W04 warnings, unchanged class).

## Sources & frontier

- **SOURCES rows, before → after:** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: **185 → 187** (receipt `.ufo/waves/round-90/receipts/census-before-rows.txt`; after at the lane tip).
- **Rows added by tier:** S260 (external, Stryker Mutator documentation, tier **A** scoped to the vocabulary and metric definitions, `docs`); S261 (own-work, the round-89 mutant matrix, tier **A** scoped). Tier counts added: A 2, B 0, C 0.
- **Rows touched old → new:** S260 `status` `queued` → `mined` (cited by `corpus/knowledge/mutation-battery-round90.md`); S261 `status` `queued` → `mined` (cited by the same entry); `recheck` and `used-by` set at creation (no in-place change to existing rows). Logged old→new in `corpus/lessons/round-90.md` § Sources.
- **Census:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0 at the round start (185 rows) and at the lane tip (187 rows).
- **Frontier rows advanced:** Frontier of `corpus/README.md` gains a mutation-testing surface (kill/survive/equivalent measurement over lane gates) in Core via the knowledge entry; the sourced claim (C1 rests on S260, opened this round) is admitted in the lesson Gate. The host census moves a frontier row from "not measured on this host" to "measured on the live root, comparison-empty".
- **Considerthese (`considerthese/2026-10-26.md`):** proposal 5 (evidence budget) mined as **Q82** (`corpus/QUALITY.md`); proposals 3 and 4 carried (noted in the lesson). Proposal 1 (SKILL.md byte ceiling) and 2 (move gate registry out of SKILL.md) not taken: unchanged, both still carried.
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kotoba/` not adopted: 55 id collisions stand (round-89 measure); L0 `kotoba | round-88` (renumber-or-retire) stays open. The absent-defect register slice (13 kotoba rows) was not verdict-landed this round; carried.

## Trend verdicts

- **expansion: improved.** One new-ground knowledge entry (`corpus/knowledge/mutation-battery-round90.md`, mutation testing of lane gates, sourced to S260 and S261; `source:` cites both `mined` rows); the census entry (`host-census-round90.md`) re-runs an existing method on new ground (this host's live root) with no new admitted claim beyond its receipts. Evidence: SOURCES 185 → 187; `corpus/README.md` index rows at `10c9a3c`.
- **quality: improved.** Two base reds cleared with a regression arm shown able to fail (floors half-bump: `floors-regression.txt`; index: `index-regression.txt`); an unverifiable survivor class (`d5-m1a`) corrected by addendum A1 before any scored reading; S260 wording cleared of two unsupported clauses (grep → 0); the knowledge entry's bounds stated (§ Bounds). Not improved: the battery's own G1/restore guards are untested (three survivors, round 91).
- **discernment: unchanged.** No non-author spot-check has run yet (the round-90 lesson's Gate is `pending` for the closure to sample one admit — S260 — and one reject — route (a), mutmut). Attack seats caught the defects above before landing, which is recorded as the wave's effect; no agreement or disagreement is recorded as a verdict here.

## SHONEN

Four boxes, checked against `SHONEN.md` (the lane's own assessment; no box is marked by this round's author):

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` § Gate registry gains the `check_mutation_battery.py` row (line 522) under the frozen registry form; `python3 -B verifiers/check_gate_registry.py --rev 1cb07ba90fccc17ffb9cc86f6e2ab95b6a9347e4` → `74 of 74`, `landing-registry.txt`.
[~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the battery measured at `1cb07ba` (`killed 14 of 14; equivalents survived 6 of 6; disclosed survivors 0 of 0`, `receipts/landing-battery.txt`) and the host census on the live root (`receipts/c2-host-census.txt`), both logged in `LOG.md` § Round 90 — landing and measurements.
[~] Instructions executable by an agent without oral context — evidence: the battery's `recheck:` in `corpus/knowledge/mutation-battery-round90.md` runs as written (`--self-test` → `0 failure(s) over 19 assertions`; `--rev <rev> --work <scratch>` at `1cb07ba`).
[~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` § Core was not updated this round, so its list of executable instruments is one round stale for the battery; the battery stays inside the lane's own gates (tameshi's generic mutation runner is a sibling surface, `ConnectorOverlap.md`, boundary stated).

## Wave shape and seats

- Wave `r90-w1`, policy v1 (band 8–16), 13 seats: scout 2 (ScoutMutSource, ScoutHostRoots), executor 4 (ExecFloorsBump, ExecIndexRow, ExecBattery, ExecHostCensus), reviewer 2 (ReviewerRepairs, ReviewerBattery), critic 1 (CriticClaims), mutation-tester 1 (MutTesterBattery), connector 1 (ConnectorOverlap), sentinel 1 (SentinelScope), scribe 1 (ScribeCorpus). Dispatch: `.ufo/waves/round-90/r90-w1-dispatch.json` (`counts spawn 13`); results `.ufo/waves/round-90/r90-w1-results.json`.
- Attack seats 5 of 13 (38 %, ≥ 25 %): ReviewerRepairs, ReviewerBattery, CriticClaims, MutTesterBattery, SentinelScope. Connector 1 (≤ 2).
- Planner: the L1 holds the §3 planner seat; the validator excludes `planner` (disclosed standing deviation).
- Dead seats: none. All 13 returned final output (`results` list). ReviewerRepairs' output (`.ufo/waves/round-90/w1/ReviewerRepairs/review.md`) landed after the first settlement window and before WAVE-DONE.
- Residual calls: none. Round total: 13 seats.
- Seat-written scratch: all seat scratch under `/fast/scratch/hyaku/kotoba-r90/` removed by the L1 after landing (`rm -rf`); the sentinel's second pass recorded the still-live dirs at its read time.

## Stale-lane

Stale-lane: no. Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No pacman transaction, no `sysctl` or `/proc/sys` write; `user.max_user_namespaces` unchanged at 122865 (SentinelScope, two passes).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time: `M .scratch/run15-state.json` (orchestrator-owned, untouched) and `?? .ufo/closure-kaidoku-r92.json` (another lane's closure, untouched). No file written by a kotoba seat sits at the fleet root; the round-90 grep of the fleet root matches only other lanes' closure prompts and the l0 file. No misroot to copy or delete.

## Open items for the closure and the next round

- Closure: admit or reject C1 and C2 under the claim rules; C1's capability row enters the table in this round (`SCORECARD.md`, row "mutation battery over the lane's own gates", first working round 90). C2's comparison-empty result is the closure's to rule on (is a re-verification without comparisons a freshness move?).
- Round 91 candidates (not declared here): the battery's own G1 commit-check, clean-tree and restore-verification arms (`mb-m2`, `mb-m15`, `mb-m16`); the `d5` base-receipt probe is path-dependent (Q79); the floors guard's child-cap drift (`verify_harness_independent.py --self-test` takes ~167 s against a 120 s cap, a host-load-dependent false red routed by ReviewerRepairs); an exit-ladder inconsistency in the freeze-gate probe world (ReviewerRepairs, counter defect routed, not repaired into frozen bytes).
- L0 questions: none appended this round. Open from earlier rounds and unchanged: `kotoba | round-88` (assimilation renumber-or-retire; C1 kill ruling), `kotoba | round-73` (gate-registry home), `kotoba | round-50` (sibling precedence).
- Stated budget (Q82): `du -sb .ufo/waves/round-90/` → **1 344 408 B** at the lane tip (round 89 measured 1 578 934 B; round 88 609 628 B). Budget stated for this round: 1 578 934 B (the round-89 measured size); round 90 is under it. No artifact was over budget.
