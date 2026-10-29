# kengaku — round 52 report (hyaku run 11, attempt 4)

Lane: `kengaku-shokunin` · L1 `KengakuR52a4` · 2026-10-28 · campaign target round 100 · lane branch `master`, final lane hash `7a76a4bbfe6cc2a2f8dc9999f671a7645c6f2c2e` (`git ls-remote origin refs/heads/master` prints it).
Stale-lane: respawn-per-round driver; no other mission of this lane is open (attempts 1–3 ended `lane-dead-no-report`; attempt 3 hit its request budget mid-round).

## Work performed

**Declared claims (frozen at `1315234`, `plans/round-52-claims.md`, base tip `30801b47`; amendments A1–A6 each dated before the scored after-run):**

1. **R52-C1 — novelty 8→9.** A whole-benchmark grader-vacuity triage for Terminal-Bench 2.0 (89 tasks, pin `2fd12b88aafdd04a52c298e3940bcb189f9766d6`, 184 capture files): `python3 plans/round52_c1_grader_audit.py --lane .`
2. **R52-C2 — operability 8→9.** Every advertised verdict instrument has a registry row in `SKILL.md`'s *Gate/probe registry*: `python3 plans/round52_c2_registry.py --lane .`

Lowest non-retired axis is coverage 7, capped by open L0 questions `kengaku | round-25`, `round-33`, `round-51`; not claimed (routed around, never treated as answered). Stagnation nudge not invoked. No exploratory claim.

Round shape: **two v1 waves, 35 + 33 = 68 seats, 0 dead** (`w1-results.json`, `w2-results.json`: 35/35 and 33/33 seats returned final output). Role mix (both waves): executor 20, reviewer 12, scribe 11, scout 8, critic 6, connector 4, revenger 3, mutation-tester 3, sentinel 1; attack seats (reviewer/critic/mutation-tester/sentinel) 22/68 = 32 %. No residual `task` call. The canonical §3 planner seat is the L1 (the validator rejects `planner`); the bounded planning walk rode scout/connector/revenger items in wave 1. Seats named by `task.agentModelOverrides`; I passed no `model`. Attempt 3 froze, ran wave 1 and built wave 2; this attempt reused what it re-verified and discarded what it did not (below).

- **Inherited, re-verified and reused:** frozen claims + counters (`1315234`…`bfbcb07`), 35 wave-1 reports, the wave-2 spec/dispatch (revalidated under policy v1 after A5; `87301ba`). Evidence: `git log` `1315234 07ea208 19bc16c 28c0018 bfbcb07`.
- **Inherited and discarded:** attempt 3's `w2.ready` (named `KengakuR52a3` as L1, never dispatched; I rewrote it with my id after re-validation) and the untracked `.ufo/waves/round-52/w1/C1ExecFetchGraders/artifacts/graders/` duplicate, which held the GH013-flagged upstream bytes (`W2SentinelScope` F1). A second flagged copy under `w2/W2CritRoundHonesty/receipts/` was also deleted before committing. Census of the final tree: `grep -rlE 'hf_[A-Za-z0-9]{30,}'` → no hits.
- **Operator exclusion (`bfbcb07`, committed before this attempt):** GitHub push protection GH013 flagged a fake Hugging Face token in `sanitize-git-repo/tests/test_outputs.py:12`; the capture is withheld (`corpus/evidence/round52/graders/EXCLUDED.md`). Consequence: the literal C1 counter reads 183/184 and 88/89.
- **Amendment A5 (additive report; `87301ba`, `plans/round-52-claims.md`):** the counter adds `A5 EXCLUDED/CAPTURES/TASKS` lines and `PREDICATE R52-C1-A5`, leaves the literal predicate and exit code untouched, and the claims file says the literal verdict decides the kill rule. `W2CritA1Amendment` ruled A5 *honest-additive with one demonstrated gap* (a swap of two files passes A5: no set-equality check on absent paths) and A1 *a fitted rule as implemented*.
- **Amendment A6 (`4343829`):** after `W2RevRowsA`/`W2MutC2` showed `parse_rows` dropped any row with an escaped pipe (the pre-round `gate-flip-check` row was a false MISSING, and wave 1 appended a stale duplicate beside it), the C2 counter now splits on unescaped pipes and fails on duplicate row names (stricter only). Not adopted, carried: the span-scoped negation fix for `SELFTEST-UNBACKED` (a naive narrowing flags the landed `order-check` cell) and the unfrozen mutation controls K5/K7.
- **C2 work:** wave 1 drafted 28 rows (6 scribes); wave 2 re-measured them. `W2ScribeRowsCheck` and `W2RevRowsA/B` found 7 false cells (`round46-c3` `defects=0` really 6; `round46-c1` 35 controls really 34; `round51-routing` "no `2` path" really `--bogus` exits 2 and its scope claim; `routed-findings` `mismatched=1` really 43/12; `round46-c3` scope; `round35-hardening` undated live count; a stale duplicate `gate-flip-check` row with `ok=19/19`, really 27/27). All repaired in `SKILL.md` (30 rows incl. `round52-c1`/`round52-c2`).
- **C1 work:** 183 captures committed byte-exact with `SHA256SUMS` (184 lines); 16 confirmation receipts over 8 never-read tasks (readers `W2ExecConfirmA/B/C`, `W2RevConfirmations`); 30 labels (`labels.json`, agree 30/30 — the classifier's own rules, not blind agreement); `prior-art.md` (14 fetched URLs, per-finding verdicts for 5 tasks); knowledge entry `corpus/knowledge/tb2-grader-vacuity-triage.md`.
- **Controls (eight, all fail their counter on the named leg):** `.ufo/waves/round-52/claims/c1-control-{nothing,name-only,blind-class,drop-capture}.txt`, `c2-control-{nothing,empty-cells,drop-row,false-selftest}.txt`, produced by `.ufo/waves/round-52/controls.py` on a scratch copy. Disclosure: the C1 controls fail on the real tree for the extra reason that the literal predicate already fails (183/184); `c1-control-drop-capture` expects `present=182`, not the frozen `present=183 mismatched=1`, because the tree already holds 183.
- **Wave-2 attacks that landed (not fixed this round, recorded):** `W2CritC1Reach` — five routes to `PREDICATE R52-C1 pass` without reading a grader (population JSON shrunk, forged stub with re-pinned digest, `confirmed:"false"`, example URLs as prior art); `W2MutC1` — 0 of 16 mutants killed by a frozen control's named leg; `W2RevEntryLesson`/`W2ExecEntryDraft` — the per-test split misclassifies both tests that motivated A1 (`P3`, `P2`), AST counts 47 `P1` against the counter's 33, one false `P1`; `W2MutC2` — survivors M4/M5 (decoy table, entry-missing) outside the frozen controls; `W2ConnectIndexBoth` — the corpus index lacked rows for new files (rows added for the artefacts that landed; per-file seat receipts are not indexed). All in `corpus/lessons/round-52.md` and `corpus/QUALITY.md` Q42.
- **Round-51 closure routed defects (`corpus/lessons/round-51-verifier-spotcheck.md`):** D1 (no registry row for `round51_surfaces.py`/`round51_routing.py`) closed by the C2 rows; D2 (63 vs 64 seats) closed by the append-only `LOG.md` erratum (`28c0018`); D3 (C2 gate survivors) and D4 (`prose` reading is not truth) named in the lesson and carried, not fixed — fixing them was no claim of this round and the round's counters read different artefacts; Q42 states the requirement.
- **Assimilation:** none (no `merge/kengaku/` theme or `considerthese/` proposal taken; the frozen claims predate it). **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file written by a round-52 seat at the fleet root; an untracked `lane3/` (a full clone of this lane at a round-50 commit, created 14:59, before round-52 launched) is not a round-52 seat's and was left untouched; one >1 MiB seat fetch (`w2/W2ScoutPriorArtFresh/receipts/fetch/tb2-paper-full.html`) stayed untracked (helper skips files over 1 MiB).
- **Tool installs:** none.
- **L0:** attempt 3 filed `kengaku | round-52` (GH013 exclusion; `.ufo/l0-questions.md:203`); open, routed around. The A5 question (does a digest-pinned absence count?) is left to the closure.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| frozen claims, counters, population, wave-1 spec | round-52 entry | `1315234` (attempt 3) |
| A1 per-test classification + disclosure receipt | round-52 entry | `07ea208` (attempt 3) |
| A2 counter corrections; 183 pinned captures | round-52 entry | `19bc16c` (attempt 3) |
| wave-1 evidence, C2 rows, round-51 erratum, wave-2 dispatch | "Round-51 erratum (round 52)" + round-52 entry | `28c0018` (attempt 3) |
| GH013 exclusion (`EXCLUDED.md`) | round-52 entry | `bfbcb07` (operator decision) |
| Amendment A5 (counter + claims), wave-2 spec revalidated | round-52 entry | `87301bacca90c03fa915716fbe6d7023762c5ab3` |
| wave-2 results/reports, corrected registry rows + A6 counter, confirmations/labels/prior-art, knowledge entry `tb2-grader-vacuity-triage.md`, `SOURCES.md` S179–S193, lesson `round-52.md`, QUALITY Q42, corpus README rows | round-52 entry | `434382945c289a3fbf9e2a2ffd97c5964918a5e7` |
| SCORECARD round-52 section, LOG round-52 entry, after/control receipts | round-52 entry | `7a76a4bbfe6cc2a2f8dc9999f671a7645c6f2c2e` (lane tip) |

## Before → after measurements

Measured against `434382945c289a3fbf9e2a2ffd97c5964918a5e7` in a clean shared clone (`git status --porcelain` → 0 lines); receipts `.ufo/waves/round-52/claims/c1-after.txt`, `c2-after.txt`, selftests `c1-selftest.txt`, `c2-selftest.txt`.

**R52-C1 — not admitted (literal predicate fails; novelty stays 8).**
`python3 plans/round52_c1_grader_audit.py --lane .`

| | before (`c1-before.txt`, base tip `30801b47`) | after (`c1-after.txt`, exit 1) |
|---|---|---|
| TASKS | total 89, records 89, classified 0 | total 89, records 89, classified **88** (target 89) |
| CAPTURES | expected 184, present 0 | expected 184, present **183** (target 184), mismatched 0 |
| CLASS | V0=89 | V1=2 V4=0 V2=53 V3=31 V0=3; TESTCLASS presence_only_tests=33 in 27 tasks |
| CANDIDATES / CONFIRMED | 0 / 0 | 29 / **8** (target ≥2) |
| PRIOR-ART | ok=False urls=0 | ok=True urls=**14** (target ≥3) |
| PREDICATE | `R52-C1 fail` | `R52-C1 fail`; additive `R52-C1-A5` **pass** |

Selftest `cases=6 failures=0` (exit 0). By the frozen kill rule legs 1 and 2 fail by one file, the operator's GH013 exclusion; under the A5 reading every leg holds and the score rule's prior-art leg would price 4 of the 5 priced confirmed tasks phenomenon-new at weakness level (`caffe-cifar-10` unclear; three more confirmed tasks are unpriced). I do **not** claim that reading: wave 2 showed the instrument misclassifies its own motivating tests and is forgeable. The operator rules on A5.

**R52-C2 — met on its (A6-stricter) counter; operability 8→9.**
`python3 plans/round52_c2_registry.py --lane .`

| | before (`c2-before.txt`) | after (`c2-after.txt`, exit 0) |
|---|---|---|
| ADVERTISED / REGISTERED | 72 / 44 | 74 / 74 (rows=76; `round52_c1`/`round52_c2` now cited) |
| MISSING | 28 | **0** |
| INCOMPLETE / ENTRY-MISSING | 0 / 0 | 0 / 0 |
| SELFTEST-UNBACKED | 1 (`order-check`; later shown a parser false positive, A3) | 0 |
| DUPLICATE (A6) | not a leg | 0 |
| PREDICATE | `R52-C2 fail` | `R52-C2 pass` |

Selftest `cases=3 failures=0`. The counter proves a row exists, is complete and names a real entry script; row *truth* was reviewed by `W2ScribeRowsCheck`/`W2RevRowsA/B` (seats of this lane, not independent), 7 false cells repaired; Q42 records that the counter cannot see a false cell.

## Sources & frontier

Census command (round start, this attempt, before any edit): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → 15 pre-existing `W04` duplicate-url warnings, `ok`, **exit 0**, 171 rows. Round end (after the final lane commit): same command → 15 `W04`, `ok`, **exit 0**, 186 rows; `census`: tier A 158 / B 23 / C 5, mined 167 / queued 8 / rejected 11 (before: A 147 / B 22 / C 2, mined 155 / queued 8 / rejected 8).

- Counting command: `grep -c '^| S[0-9]' corpus/SOURCES.md` → 171 at base tip `30801b4`, 186 at the lane tip.
- Rows added: 15 — tier A 11 (S179–S185, S187–S190), tier B 1 (S186, third-party review), tier C 3 (S191–S193, rejected with flip conditions). Rows touched old→new: none (S115 re-opened with identical bytes, no second row; S020 left `queued`). Frontier rows advanced: none.
- Sourced claim: C1's knowledge entry `corpus/knowledge/tb2-grader-vacuity-triage.md` cites S179–S190 (each row opened 2026-10-28 by `W2ScribeSourcesRows` with a located ≤25-word quote; the lesson's `## Gate` carries URL, date, quote, location). Gate records admits (S184, S187, S190) and rejects (S191, S193) for the non-author spot-check.
- Mined mistake: `corpus/lessons/round-52.md` `## Mistakes` — ten rows (class · evidence · captured-by · fix), including `counter-reachable-without-the-work` (captured-by none; fix not landed, Q42 states the requirement) and `false-registry-cell`.
- Assimilation: none. `considerthese/`: no proposal taken this round.

## Trend verdicts

- **expansion: improved.** 89-task population surface covered by a committed instrument (184 pinned file identities, 183 bytes), one new knowledge entry, 15 registry rows, 28 previously undiscoverable gates now have registry rows. Evidence: `c1-after.txt`, `c2-after.txt`, `corpus/knowledge/tb2-grader-vacuity-triage.md`. Caveat: the C1 verdict itself is *not admitted*.
- **quality: improved, with a recorded gap.** 7 false registry cells and a stale duplicate repaired; 4 counter defects fixed before the after-run (A2, A3, A6); Q42 added. Gap: the C1 counter is forgeable and its per-test class is leaky (wave-2 receipts), and the C2 counter cannot see a false cell.
- **discernment: improved.** Wave 2 attacked the lane's own amendment (A1 judged "fitted rule as implemented", A5 "honest-additive with one gap") and the round reports the literal C1 fail instead of claiming the A5 reading; the ten mistake rows name what no gate caught. No outside spot-check yet — the closure's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry now 74 rows (`round52-c2` rows at lines 635–636)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 52" entry; 89-grader population executed end to end in `c1-after.txt`
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/tb2-grader-vacuity-triage.md` "Re-run" section and `corpus/lessons/round-52.md`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; the round stays inside LLM/benchmark evaluation; `W2ConnectSiblings2` found no sibling lane owning TB2 grader audits
