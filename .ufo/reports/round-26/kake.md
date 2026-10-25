# Kake round 26 — source freshness re-verification

## Work performed

**Declared claim C1 — freshness:** re-verify the 32 previously opened external SOURCES rows (S001–S034 excluding own-work S014/S019; S035 excluded), recheck the knowledge statements relying on them, and append corrections for adjudicated STALE statements. Contract: lane `.ufo/waves/round-26/contract.json` and `contract-amendment.json`. **C1 verifies author-side: 0/32 → 32/32 decided.** Independent closure remains required. The legacy freshness score stays 10→10; the receipt delta, not a scalar increment, measures this maintenance move.

- Resumed the already-held kake=26 attempt1 claim; never dispatched, failed, advanced or started another round. Reconstructed KakeR25's progress from its dead-session transcript, seat transcripts/reports, committed candidate and current lane state (`.ufo/waves/round-26/resume-evidence.json`). The predecessor's terminal `landed e28312b14b076584fedd696fae2a684e460bd11e` output is retained in that transcript.
- **W2 had not spawned before death:** the predecessor transcript ends with its pending dispatch-loop eval and session exit; no W2-named seat transcripts or returned Spawned result existed. Thus its validated 64-seat payload spent no seats. Reused that payload unchanged, obtained/released a fresh wave slot, and dispatched W2 successfully on the first replacement attempt (`w2-dispatch-attempts.json`, `w2-spawn-result.json`, `w2-assignments.json`). No dead seat was replaced.
- Reused the pushed source bytes, population, receipts and W1 reports only with fresh checks: W2's 32 receipt reviewers checked their anchors/quotes; RefetchCompare re-fetched the 34 row/index slots and reproduced all effective texts; CensusRerun recomputed all 35 retained payload hashes. Original W1 reports/drafts remain historical evidence, not canonical final judgments. Re-ran base/candidate measurements and both selftests in throwaway clones (`verification/`).
- Re-fetched population: 34 row/index slots, **33 distinct URLs** (S028/S033 share one), plus S008's documented timeout retry = 35 initial/retry attempts. Initial fetches were 15:09–15:10 UTC and the retry 15:11 UTC. W2 live refetches were additional document-only reads. No account, browser, website-property probe, publication or credential operation was undertaken.
- Falsification changed the statement adjudication: 37 additional row-statement units reviewed; S001's v3.0.1 attribution and two S024 scope statements corrected; four earlier STALE tags reclassified as precision notes without deleting corpus bytes. Final ledger **313 units, 7 STALE corrections, 4 reclassified tags, 6 UNVERIFIABLE units** (`statements.json`, corpus EOF adjudication blocks). S021's fragment wording is already corrected in r23, not a rejected finding. The separate SKILL-tail review has 11 units (7 HOLD, 4 already corrected), outside the counter's 313.
- Corrected S024/S025's stale `used-by` cells to include the actual knowledge citer; logged old→new in the round lesson (W2 UncoveredLessonCites). Historical lessons were not rewritten.
- Fixed the counter's missing per-row output, integrity-checked every fetch of each row, tightened document-group twin handling, and checked duplicate/out-of-population ledger pairs and unaccounted correction tags. Counter fixtures increased 14→24; extractor fixtures 73→74 (`measure.py`, `text_selftest.py`). All six previously surviving counter mutants and six new-rule mutants were killed; the HTML-sniff survivor was also killed (`verification/counter-mutation-replay.json`, `extractor-sniff-mutant.json`).
- Preserved receipts as originally written; corrected their stale derived offsets/locator prose in `receipt-locator-errata.json`. The counter verifies quote presence, **not prose coordinates**. W1 derived-view hashes/offsets may describe the pre-amendment extractor; retained raw bytes/manifests, current views and errata are authoritative.

### Swarm and conformance

| Wave | Inherited/new | Seats | Role mix | Reports / dead |
|---|---|---:|---|---|
| W1 build | Inherited, spawned by KakeR25 on try 6 after five job-cap refusals | 64 | 32 scout, 26 reviewer, 2 executor, 2 critic, 1 connector, 1 scribe | 64 / 0 |
| W2 falsify | New replacement dispatch of inherited validated payload | 64 | 36 reviewer, 23 critic, 2 mutation-tester, 2 scout, 1 scribe | 64 / 0 |

Round total **128 seats**; all dispatched seats have reports, so dead-seat list is empty. The L1 holds the planner seat. W2's captured role aliases were reviewer m_mim, critic m_auto, mutation-tester m_sol, scout m_flash, scribe m_haiku (spawn receipt); no model parameters or routing changes were supplied. One ordinary residual executor dispatch returned `Background job limit reached (100)` and spawned nothing; L1 performed that integration instead.

**Inherited role-floor conformance defect:** W1 has two executor seats, below the prompt's three-executor minimum. This requirement is **not met**; no padding or retrospective role relabelling is claimed. The measured C1 result does not erase the defect or confer round admission.

### Recovery, scope and residual limitations

- Inherited/re-verified: pushed e28312b implementation and fetched data; W1's 64 reports; initial before/candidate captures; W2 spec/dispatch/registry. Discarded as final authority: the assumption that W2 spawned, four overclassified STALE judgments, and pre-extractor-change locator values. All original evidence remains available.
- W1 RowS012's fleet-root report was moved byte-exact by the predecessor (`misroot-RowS012.txt`). Replacement's complete fleet-root status sweep found no own misroot; other lanes' reports/waves, driver state and watchdog edits were left untouched.
- Bounds were not perfectly followed: W2 S004/S011/S018/S020/S030/S032 disclosed transient `/tmp` scratch; S006/S007/CounterCritic disclosed `/dev/shm` scratch. Seats report their scratch deleted. KakeR25's `/tmp/kake-r26-m.json` was an L1 file, not a seat file; its hash is recorded and it was deleted. Replacement initially used `/tmp` clones, then moved subsequent scratch to `/fast/scratch/hyaku/kake-r26/` following the parent directive. All replacement-owned round scratch in both locations was removed before landing. Lesson Mistakes records the deviations; no claim of perfect write-bound compliance is made.
- Locator offsets remain human-reviewed; citing-set completeness is manually checked rather than guaranteed by the counter. Living-doc HOLD is dated, not perpetual; immutable RFC byte equality cannot by itself prove absence of external errata/supersession. RFC 9557 observations are second-hand seat notes, not a newly admitted source row. No claim depends on newly mining RFC 9557.
- Round-24 C1/C2 remain separate unadmitted debt; no stopped probe/counter was retried, rephrased or rerouted. W2 S034/S033 disclosed reading historical digest cross-references in the r24 lesson; this is disclosed, not described as a fresh r24 investigation. No tools installed or updated.

## Landed changes

Every item is tied to `LOG.md` **Round 26 — source recheck**, **Round-26 resume and falsify-wave integration**, and **Round-26 measured outcome**:

- `e28312b14b076584fedd696fae2a684e460bd11e` — inherited initial source recheck, raw evidence, W1, receipts and initial corpus corrections (predecessor helper terminal landed line).
- `b44daedc9658d86374f1c3e3cdfc3a6951d0bdf6` — helper output `landed b44daedc9658d86374f1c3e3cdfc3a6951d0bdf6`; falsify-driven corpus adjudication, additional citing-file reviews, counter/extractor fixture strengthening, QUALITY/SKILL lessons and verification evidence. **Measured implementation revision.**
- `a2be0dc53845a4963f9af447d7c7c6644bfde6b3` — helper output `landed a2be0dc53845a4963f9af447d7c7c6644bfde6b3`; all 64 W2 reports and assignment/outcome receipts, measured SCORECARD/LOG/lesson, S024/S025 routing repair and final coverage-map note. **Final lane tip.**

Final helper state: local=remote=`a2be0dc53845a4963f9af447d7c7c6644bfde6b3`, ahead=0, behind=0, tracked=0, untracked=0. No external/domain-source repository was modified or pushed.

## Before → after measurements

Counting command, run using the final counter in a throwaway clone:

```sh
python3 -B .ufo/waves/round-26/measure.py --root . --revision <commit>
```

| Revision | Decided / expected | Row result | Statement ledger | Exit |
|---|---:|---|---|---:|
| Baseline `97404de4ff73d6c8a4f87385cf5fdf36dca7f006` | 0/32 | `receipts_absent` | No round-26 ledger at base | 1 (expected) |
| First candidate `e28312b14b076584fedd696fae2a684e460bd11e` | 32/32 | HOLD32, UNVERIFIABLE0, findings0 | 276 / 8 corrections (pre-W2) | 0 |
| Landed implementation `b44daedc9658d86374f1c3e3cdfc3a6951d0bdf6` | 32/32 | HOLD32, STALE0, UNVERIFIABLE0, findings0; 32 row records | 313 / 7 corrections; 4 reclassified tags accounted | 0 |

Exact captures: `.ufo/waves/round-26/verification/measure-before-final-counter.json`, `measure-candidate-reverify.json`, `measure-final.json`. The final tip adds evidence/documentation and allowed SOURCES cells, not counter logic.

Exercised gates: counter `--selftest` **24/24 exit0**; extractor **74/74 exit0**; retained pre-fix extractor **22 failures, exit1**, followed by green-after; counter mutation replay **12/12 killed**; extractor HTML-sniff mutant killed by the new attributed-opening-tag case; corpus contract **0 findings, exit0**; offline freshness sweep **exit0**. Files under `verification/` hold commands/stdout/stderr. An initial scratch-layout failure in the red-before harness was repaired before the retained valid red witness. The earlier scratch extractor-run records label their baseline C revision, with working-tree fixture changes described in `note`; they are fixture-run evidence, not an assertion that those changes already existed in C.

## Sources & frontier

Maintained counting/conformance command before and after:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Both outputs and exits:

```text
kake W04 S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake ok /home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit=0
```

Original tab-separated outputs: `census-before.txt`, `verification/census-final.json`. Registry counts (`verification/registry-counts.json`, `registry-final-counts.json`): **35→35 rows**, tiers A33/B0/C2 unchanged; statuses mined31/queued2/rejected2 unchanged; malformed0. Added by tier **A0/B0/C0**. W04 is inherited, not a new failure.

Rows opened/re-fetched: 32 external rows in `population.json`, each grounded by its receipt quote/anchor. No new source row, no status/recheck change. Cells changed: **S024 and S025 used-by**, each `corpus/lessons/round-22.md` → `corpus/knowledge/static-canonical-preflight.md, corpus/lessons/round-22.md`; logged in lesson **Source registry routing correction**. Initial assertions of unchanged cells describe the pre-W2 candidate, not the final state.

Sourced C1 examples: S003 source-folder quote/Actions attribution, S001 versus S002 version attribution, and S024 base[href] scope, all named in appended knowledge blocks. Mistakes include overclassified STALEs, used-by routing gaps, missing row output, surviving mutants, extractor-derived locator drift and scratch-scope deviations. Fail-capable witnesses are explicitly distinguished from prose-only errata in the lesson. Frontier ground unchanged; this round maintains held publishing-platform/canonical knowledge, not a new capability or live-site conformance.

## Trend verdicts

- **expansion: unchanged** — no newly admitted knowledge entry on uncovered ground and no capability acquisition; SOURCES rows 35→35, coverage map explicitly calls this quality maintenance.
- **quality: improved** — nine prior knowledge entries re-verified; false attributions/scope claims are marked with appended fixes, and four invalid STALE diagnoses are explicitly reclassified. Original knowledge-file bytes remain prefixes (`verification/no-harm-final.json`). No axis harm observed within this bounded documentary maintenance claim; source limitations remain disclosed.
- **discernment: unchanged, pending independent closure** — the author-side falsifiers caused grounded QUALITY criteria and real rejected/reclassified admissions, but the lane's own seats are not the required non-author spot-check. No outside admission/rejection agreement is fabricated.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources — `SKILL.md` Source recheck section and gate registry; `corpus/QUALITY.md` Recheck adjudication. Author-side evidence, no new non-author verifier.
- [~] End-to-end domain maintenance task executed and logged — 32-source recheck and appended corrections, `LOG.md` Round-26 measured outcome and `verification/measure-final.json`; no website was evaluated or published.
- [~] Instructions executable without oral context — gate registry plus 24-case/74-case selftests and captured CLI runs. Independent instruction-execution verification remains pending.
- [~] No cross-domain bleed — `PROVINCE.md` publishing-platform/source-grounded audit ownership; browser, credential, publication and adjacent runtime work not absorbed. Author-side assessment only.

Stale-lane: this replacement progressed through pushed implementation/evidence commits; no other kake mission is open. Round27 was not started. Open L0: the already-routed round-24 policy-stop disposition remains unresolved; no new L0 question filed. Full round admission is left to the non-author closure, including the disclosed inherited executor-floor defect.
