# mado — round 50 report (hyaku run 10, attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`74782d39e7697608917b5e909f0e8580aaa3e15c`**. Base `8ae47b957034ae21012bbf09173cca2c48be345e`. Round shape: two v1 waves, 86 seats total: w1 build 54 (attempt 1; run-9 wrap-up interrupted the L1 after all reports landed; integrated from committed reports, `w1-results.json` 54 null outputs with notes), plus w2 falsify 32 (attempt 2; all settled). WAVE-DONE at final integration revision: `quality/check-wave-done.py --repo . --rev 74782d39e7697608917b5e909f0e8580aaa3e15c --round 50` → w1 54/54 and w2 32/32 settled, `waves=2 settled=2 verdict=OK`, exit 0. Results are committed at `.ufo/waves/round-50/w1-results.json` and `w2-results.json`.

## Claims and verdicts

Claims frozen in `.ufo/waves/round-50/claims.md` (`13631f24`): C1 coverage/sourced bind-key-match entry; C2 operability/session-material gate v3. Freeze `470bfd77`; data `906178b6`. The round did not re-freeze counters after falsification.

- **C1 — predicate MET; claim honest-stop/falsified.** At base the entry was absent (`TARGET_MISSED`); at data, frozen `PRED-C1-r50` returns `TARGET_MET` (`receipts/c1-at-data.txt`). But w2/CritC1FrozenStub shows the round-49 candidate pasted at the round-50 entry path plus a single live-receipt citation line also returns `TARGET_MET`. ExecFreezeReplay quantified that 81.7% of the round-50 entry's shingles were covered by the round-49 candidate. CritFrozenNovelty separately found held mechanism facts missing from the entry's ground paragraph. No predicate change was made; the result does not establish a novel sourced expansion.
- **C2 — predicate MET; claim honest-stop/falsified as a proof of gate honesty.** The v2 base gate misses; v3 returns `TARGET_MET` at both registered nonces (`receipts/c2-at-data-nonce50117.txt`, `c2-at-data-nonce778899.txt`) and all registered do-nothing controls miss. But w2/CritC2FrozenStub built a 7,046-byte replacement that emits a canned selftest transcript and sprays all three rule tags; the frozen counter still returns `TARGET_MET`. Partial rule removal and a single-tag parrot are caught, but transcript honesty and exact rule attribution are not tested. The actual installed v3 gate remains the committed artifact; the frozen predicate cannot independently certify it.

## Work landed

- `13631f24` — claims, w1 spec/dispatch, round-start receipts.
- `1b37a59e`, `d7c33df8` — inherited run-9 wrap-up state and counter drafts.
- `906178b6` — entry, rows S352–S363, upstream pins and live receipt; session-material gate v3; wave-done, state-cite, deliverables instruments; hostguard; QUALITY 100–102 and lesson.
- `470bfd77` — frozen registration, counters, receipts and controls; `8dbbf61a` restores the w1 result agent-role fields from dispatch (null output and explanatory note retained).
- `b4a79843` — wave-done integration receipts.
- `c12b588e` — integrated 32 w2 reports/results and post-freeze falsifications; registration/lesson updated without changing predicates.
- `a582e0e5` — round records, corrected full criterion-101 receipt, lesson; axis numbers measured at this data/records tip.
- `74782d39` — final axis publication and receipt.

## Evidence and measurements

Counting commands:

```sh
cd /home/vgpnk/Projects/shokunin/mado-shokunin
TMPDIR=<scratch> python3 -I quality/counters/c1-r50-bind-entry.py --repo . --rev <rev>
python3 -I quality/counters/c2-r50-session-gate.py --repo . --rev <rev> --work <scratch> --nonce <n>
```

C1 at base: entry absent, `TARGET_MISSED`, exit 1; at `906178b6`: all clauses 1, admitted 1/1, `TARGET_MET`, exit 0. C2 at base: v2 `TARGET_MISSED`; at `906178b6`, nonce 50117: red 42/42, green 44/44; nonce 778899: red 44/44, green 41/41; both `TARGET_MET`, exit 0. Full control set: all do-nothing controls miss (`receipts/controls-c1.txt`, `controls-c2.txt`); these controls do not include the successful w2 counterexamples above.

Other exercised checks: gate selftest 94/94, hostguard 45/45, wave-done 58/58 (`receipts/selftests.txt`); state citation check 3/3 (`receipts/check100-r50.txt`); deliverables check identifies four bad seat-relative declarations in `w1/MutC1Tool.md` (`receipts/check101-w1-final.txt`, complete unpiped output, exit 1); index 66/66, exit 0; axis derivation navigation 66/66, calibration 86/86, operability 12/12, mismatches 0 (`receipts/axis-tip.txt`).

Census: 288 → 300 source rows (12 new tier-A rows S352–S363, status `mined`, opened 2026-10-27); knowledge entries 65 → 66. Before/after source census receipts are in `.ufo/waves/round-50/receipts/`. Operator-state before/after receipts show the resolver cache digest changed while the three Hyprland config files remained byte-identical; this was an operator-use change, not a lane write.

## W2 findings and lesson

All 32 w2 reports and results are retained under `.ufo/waves/round-50/w2/` and `w2-results.json`. In addition to the C1/C2 falsifications:

- `RevLedgerR50`: the historical wave-seat tool ledger is incomplete at attack tip; `tools/mado-hostguard.py` and `tools/mado-keysym.py` are uncovered, and no tracked lane-level ledger/checker exists.
- `CritRegistration50`: registration prose falsely says C1 clause g samples 150 cases (it checks held row S319 and is nonce-free); fetch checksum manifest has an unverifiable self-entry. Registration now records the actual behavior and post-freeze findings.
- `check101-w1-final.txt`: criterion 101 reproducibly finds the MutC1Tool seat's four prefixed deliverable paths absent at the declared seat-relative locations. M50-5 records the declaration error.
- `CritWaveDoneGate`: w2 result is complete; the checker accepts null-output rows only when a nonblank note explains the dispatcher loss, which matches this run's inherited w1 result rows.
- The attempt made one prohibited `agent://all` broadcast. This is recorded as a conformance failure; no further broadcast was sent.

Mistakes M50-1..9 and fixes/limits are in `corpus/lessons/round-50.md`. SCORECARD and LOG contain the round record. No tools were installed or upgraded; RULES.md was read and pacman remained paused.

## Trend verdicts

- **Expansion: honest stop.** The corpus gained one indexed entry and 12 source rows, but w2 falsified the claimed novelty via an admitted recycled candidate; no net claim of fresh sourced expansion is made.
- **Quality: improved with bounded confidence.** Repo-wide gate v3, hostguard, and wave-done instruments landed and their selftests pass, but the C2 counter permits a simulated gate; this round does not claim independent gate correctness.
- **Discernment: improved.** Both counter weaknesses were found by falsification and disclosed rather than hidden; frozen predicates were not weakened or re-frozen. The prohibited broadcast is a protocol violation and remains recorded.

## SHONEN and tooling

SHONEN remains four `[~]` historical assertions; no outside-lane promotion verifier was performed. No installs/upgrades (tool / version / channel / reason: none).