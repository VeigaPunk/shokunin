## Method

Axis: gate-integrity. I copied the pristine `MANIFEST.json` bytes to `.ufo/waves/round-12/mutants/pristine.json` and recorded `sha256sum MANIFEST.json` as `bf1ba57e6950b6f805c09c3e4f81ecd5354f9f8422947244e440b0ef6d4c98f1`. Before each mutant I also ran `sha256sum MANIFEST.json .ufo/waves/round-12/closure-check.py`; the gate-script hashes observed were `d10dcd005a525864db5e018222ec396f2f9a43b7c63fe6e155a4564636ba795f` for mutants 1–4 and `4f53fcc0fbf6751d974100285a7bec82fe718caabcea5fc683a0b64b460a6720` for mutants 5–7. This records ExecChecker's concurrent edits rather than hiding them.

For each mutant I changed only `MANIFEST.json`, ran `python3 .ufo/waves/round-12/closure-check.py --no-citations`, recorded its first stdout line and exit code, copied `mutants/pristine.json` back, then verified the original manifest hash. Every restore observed `bf1ba57e6950b6f805c09c3e4f81ecd5354f9f8422947244e440b0ef6d4c98f1`; `git diff --stat MANIFEST.json` was empty because the candidate manifest is untracked relative to HEAD in this worktree (the byte/hash check is the stronger invariant here). Baseline after the script fix was `closure-check: debt debt=2 contradictions=0 unrowed_terminated=0 pending_round=2`, exit 1.

## Mutants

1. **m1 | failed→ok in legacy-adjacent correction.** Exact edit: `jq '(.rounds[3].lanes.aggregator) = "ok"' MANIFEST.json` (round-1 correction's aggregator). Command: `python3 .ufo/waves/round-12/closure-check.py --no-citations`. Observed: `closure-check: debt debt=2 contradictions=0 unrowed_terminated=0 pending_round=2`, exit 1. **Survived**: the changed row is not an independent debt driver in the current live evidence; a status-only check cannot prove this flip. A row/evidence consistency assertion for failed corrections (report absence/dispatch evidence) would catch it.

2. **m2 | delete `lane_rounds.protocol` from round-14 not-dispatched row.** Exact edit: `jq '(.rounds[27].lane_rounds) |= del(.protocol)'`. Command as above. Observed: `closure-check: debt debt=3 contradictions=1 unrowed_terminated=0 pending_round=2`, exit 1. **Killed**: the detector surfaced a contradiction/debt for the malformed not-dispatched row.

3. **m3 | change an ok lane to one with no derivable report.** Exact edit: `jq '(.rounds[27].lanes.kasegi) = "protocol"'`. Command as above. Observed: Python traceback ending `KeyError: 'protocol'`, exit 1. **Inconclusive**, not counted as a clean kill: the detector rejects the malformed lane by crashing in `_lane_round_keying_tally`, rather than emitting a gate finding. A schema/allowed-lane validation should report a structured debt/error instead of raising `KeyError`.

4. **m4 | naive re-keying trap.** Exact edit: `jq '(.rounds[24].lane_rounds.kengaku) = 9'` on the round-11 correction. Command as above. Observed: `closure-check: debt debt=2 contradictions=0 unrowed_terminated=0 pending_round=2`, exit 1. **Survived**: the authoritative entry-keyed ledger deliberately ignores `lane_rounds` for row identity, so this annotation change is invisible to the live gate. A dedicated invariant should reject a `lane_rounds` value that differs from the row's adjudicated lane-round or explicitly emit a warning/debt for identity drift.

5. **m5 | turn one new in-flight row into ok.** Exact edit: `jq '(.rounds[25].lanes.protocol) = "ok"'`. Command as above. Observed: `closure-check: debt debt=3 contradictions=1 unrowed_terminated=0 pending_round=2`, exit 1. **Killed**: evidence contradicts the premature terminal status.

6. **m6 | remove `supersedes` from a closure-correction.** Exact edit: `jq 'del(.rounds[25].supersedes)'`. Command as above. Observed: `closure-check: debt debt=3 contradictions=1 unrowed_terminated=0 pending_round=2`, exit 1. **Killed**: the correction's missing supersession creates a ledger/evidence contradiction.

7. **m7 | append duplicate contradictory status for the same lane-round.** Exact edit: append a `closure-correction` for `protocol r12` with `lanes.protocol="ok"`, `lane_rounds.protocol=12`, and the same closure timestamp. Command as above. Observed: `closure-check: debt debt=3 contradictions=1 unrowed_terminated=0 pending_round=2`, exit 1. **Killed**: duplicate last-wins status conflicts with live evidence and raises contradiction debt.

## Verdict

The gate detected 4 of 5 determinate mutants (m2, m5, m6, m7): mutation score **4/5 determinate = 80%**; m1 and m4 survived, and m3 was inconclusive because it crashed. This is meaningful detection evidence beyond the fixture self-test: malformed closure records and premature/duplicate adjudications change the live verdict. It also exposes two real gaps: `lane_rounds` identity drift is not checked, and invalid lane IDs crash instead of producing a structured gate result.

On the restored tree, command `python3 .ufo/waves/round-12/closure-check.py --selftest` printed `closure-check: ok selftest passed=10/10 failed=0` and `selftest: 10/10 passed`, exit 0. Command `python3 .ufo/waves/round-12/closure-check.py --frozen pre` printed `closure-check: debt debt=5 contradictions=0 unrowed_terminated=2 pending_round=7` and `baseline: match expected exit=1 analyzed exit=1`, exit 1. Command `python3 .ufo/waves/round-12/closure-check.py --frozen post` printed `closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=1` and `baseline: match expected exit=0 analyzed exit=0`, exit 0. Final manifest hash again matched `bf1ba57e6950b6f805c09c3e4f81ecd5354f9f8422947244e440b0ef6d4c98f1`.

## Gaps

- Add explicit allowed-lane/schema validation so m3 becomes a deterministic structured finding, not a `KeyError` traceback.
- Add a `lane_rounds` identity-drift check so m4 is killed while preserving the documented “never re-keys” semantics.
- m1 survived because changing a legacy-adjacent status did not alter current debt; a targeted correction/evidence consistency check is needed if such historical statuses are intended to be integrity-protected.
