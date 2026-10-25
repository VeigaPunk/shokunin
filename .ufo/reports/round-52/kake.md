# Round 52 — kake (operability, freshness)

author: L1Kake52 (lane worker) · lane: kake-shokunin · round 52
base: `93d7fdbd45b0e5698927e7f9cb3dafca24ace416`
measured revision: `a4a890cf1381a194891689dcbba0bf524350926b`; tip `a1d83ecf2012f92fd470c5aaacebf2225207b8e9`
pushed: `git ls-remote origin refs/heads/master` = `a1d83ecf` (ahead 0)
contract: `.ufo/waves/round-52/contract.json`, frozen before any data

## Claims

**C1 (operability, capability deepening)** — `met: registry_rows == 2 AND selftest_receipts == 2
AND vacuity_mutant_families_killed >= 10 AND real_data_reruns_pass == 2 of 2`.

- SKILL.md now carries two gate registry rows (`wave-evidence-ledger`, `quote-truth-counter`),
  each with kind, entry command, verdict map, self-test, pinned values, write scope and owner.
- Both counters have a `--selftest` mode with committed receipts: ledger **19/19**, quote-truth
  **18/18** (sandbox git fixtures, removed on exit).
- The vacuity ladder **rejects 13 of 18 mutant families** (exit 1) that the round-51 counter
  **accepts** (exit 0) on the same fixtures; the `pass` fixture agrees (both exit 0).
- Real round-51 data re-runs at full marks: ledger **3/3**, quote-truth **8/8**.
- C1's vacuity floor, C2's C8 mirror read (`show(root, rev, MIRROR)` + pinned sha256) and C6's
  receipt fields (`httpStatus`/`bytes`/`fetchedAt`) are implemented and each has a fixture.

**C2 (freshness, sourced learning + drift reconciliation)** — `met: admitted_entries_citing_mined_rows
== 3 AND registry_rows_delta == +3 AND census_validate_exit == 0 AND sweep_drift_legs_before == 3
AND sweep_drift_legs_after == 1`.

- Three entries on per-engine crawl hygiene beyond Google, on rows opened this round:
  `yahoo-japan-rel-nofollow-semantics.md` (S374), `baidu-friendly-crawl-guidance.md` (S329),
  `baidu-mobile-matching-error-causes.md` (S312).
- Registry 145 → **148** rows; census validate exit 0, no E-codes.
- Live sweep: 3 drift legs before → **1** after (`plazir-gate-anomaly`, operator-owned, disclosed).

## Measured (receipts under `.ufo/waves/round-52/control/`)

| Instrument | Command | Result | Receipt |
|---|---|---|---|
| registry | `c52_gate_registry.py --root . --revision a4a890c` | rows 2, receipts 2, met, exit 0 | `c1-registry.txt` |
| ledger | `c52_wave_ledger.py --root . --revision a4a890c` | 3/3 met, exit 0 | `c1-ledger-real.txt` |
| ledger control | `… --revision 007d66e4` (pre-wave) | 0/3, exit 1 | `c1-ledger-control-absent.txt` |
| ledger at contract base | `… --revision 93d7fdb` | 3/3 (r51 evidence present; not a control) | `c1-ledger-at-contract-base.txt` |
| ledger selftest | `c52_wave_ledger.py --selftest` | 19/19, exit 0 | `c1-ledger-selftest.txt` |
| mutation ladder | `c52_mutation_ladder.py` | 13/18 caught, control green, exit 0 | `c1-mutation-ladder.txt` / `.json` |
| quote-truth | `c52_quote_truth.py --root . --revision a4a890c` | 8/8 met, exit 0 | `c2-quote-real.txt` |
| quote-truth control | `… --revision 93d7fdb` | 0/8, exit 1 | `c2-quote-base.txt` |
| quote-truth selftest | `c52_quote_truth.py --selftest` | 18/18, exit 0 | `c2-quote-selftest.txt` |
| sweep | `node scripts/freshness-sweep.mjs` | exit 1, one leg (`plazir-gate-anomaly`) | `sweep-after.txt` (before: `drift-before.txt`) |
| sweep selftest | `node scripts/freshness-sweep.mjs --selftest` | 36/36, exit 0 | `sweep-selftest.txt` |
| census | `sources-census.sh validate --root … kake` | exit 0, 148 rows | `census-after.txt` |

Final verification at the measured tip: `control/final-verify.txt` (all seven instruments, same
numbers, tip `a1d83ec`).

## Routed defects from round-51 closure

| Defect | Handling |
|---|---|
| r51-1 counters unregistered | two SKILL.md registry rows + selftest modes + `baselines.json` (script sha256 + nine input blobs + receipt digests) |
| r51-2 C8 read the wrong referent | C8 now reads mirror bytes, pins their sha256, requires the mirror blob at its add-commit to carry the same bytes, strict ancestry, and append-only equality |
| r51-3 C1 vacuity floor | spawn/grant/payload bound, `seats` roster mirror, report bytes hashed and de-duplicated, dead-seat classification, all-zero timing rejected |
| r51-4 junk controls not replayable | replaced by `c52_mutation_ladder.py`, which builds the fixtures from committed evidence and runs both counters on them |
| r51-5 measured commit descriptive | this report and SCORECARD name the measured revision hash and its receipts |
| r51-6 "frontier line 23 narrowed" | corrected in PROVINCE § Round-52 (bytes identical; the block is the reading) |
| r51-7 live drift hidden | live verdict and per-leg reconciliation recorded in SCORECARD and the lesson |
| r51-8 staged ids unpinned | the three staged rows are committed with their entries and retained bodies; ids resolved against the registry at the measured revision |
| r51-9 untracked leftovers | committed as historical wave evidence in `73c22a3` (17 files from rounds 46/48) |

## No-harm (round-51 routed defect 7)

The live sweep still exits 1, on one leg: `plazir-gate-anomaly` — `~/Projects/plazir-15-site` has
no source sitemap (`source skipped(no-source-file)`) and its live sitemap carries 7 locs against a
pin of 8. That is an operator-owned absence: it is disclosed and **not** re-pinned. The other two
legs were reconciled from observed state and recorded in `freshness-pins.json`: `pq2Reconciled`
(remote `e6bd071…` → `24991e4…`, 0 unpushed) and `sitemapReconciled` (listing 200/7810 B; source
tree pruned 2026-10-12). The sweep's sitemap verdict gained a pure `LISTED-STEADY` branch so a
published listing is a pinned steady state, not a mislabelled `PRE-PUSH` (+1 selftest case).

## SHONEN

- [~] SKILL.md tables and S-id cites are current for this round's ground (three rows, three entries) but the file's older sections still carry their own drift.
- [ ] End-to-end task: not run this round — the wave-1 dispatch was refused at the background-job cap and no seat evidence exists.
- [~] Executable without oral context: every instrument runs from its committed command; the counters are registered and selftestable, but the round's own claims were measured by the L1.
- [~] PROVINCE accuracy: the round-52 block is accurate and the round-51 wording is corrected; the wider document is not re-audited.

`SHONEN.md` itself is untouched (all `[ ]`) — this section is a reading, not a promotion.

## Mistakes

1. The 46-seat wave never ran (dispatch refused, spawned nothing); no seat output is claimed.
2. The first ledger rewrite silently turned absent evidence into a pass (0/3 `met=True` at the
   pre-wave revision); the control caught it and absent evidence is a miss again.
3. The first ladder family set was too weak (7/18 because five mutants were already killed by the
   old counter); six families aimed at real gaps took it to 13/18.
4. The pre-append mirror needed a base snapshot to satisfy census `E11`; the mirror tree now
   carries the used-by targets at the base revision.
5. The ledger's coverage floor first required `settled == spawn`, which would reject any wave with
   a classified dead seat; it is now `settled + dead == spawn`.

## Wave accounting

| item | value |
|---|---|
| declared batch | 46 seats (`w1-dispatch.json`) |
| spawned / settled / dead | 0 / 0 / 0 |
| seat reports | none |
| instruments built | `c52_wave_ledger.py`, `c52_mutation_ladder.py`, `c52_quote_truth.py`, `c52_gate_registry.py` |
| lane commits | `73c22a3` evidence · `5422ff3` append+registry · `3a50ae4` C7 fix · `1ae8de5` baselines+receipts · `a4a890c` receipts+drift+scorecard · `a1d83ec` final verification |
