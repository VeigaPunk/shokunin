# Candidate falsification — protocol lane

## Must-fix

1. **The candidate contradicts its own orphan-order for kake r13.** `PROTOCOL.md:102-104` says the integrator sweeps only if the successor also terminates without landing. The candidate's r13 entry says kake r13 was “UNTRACKED … -> landed by this pass”, while `watchdog.log:185` shows kake r14 launched and was live at the 20:55 cutoff; `.ufo/reports/round-13/kake.md` is still `M` (observed `git status --short`). That sweep would freeze the live r14 in-place edit into the r13 record. Replacement text:
   > `kake r13 remains unlanded while kake r14 is live; do not sweep it in this pass. Record the attribution/durability debt and require the r14 successor to land an appended erratum or its own correction report.`

2. **The filed-report rule is not enforceable against the observed kake r14 edit.** `PROTOCOL.md:105-106` permits a correcting report or appended erratum, but the candidate notes an in-place edit as “substantively the right correction” (MANIFEST r14 notes). The actual diff is `git diff .ufo/reports/round-13/kake.md` (`+3/-1`, labelled “r14 erratum”). Replacement text:
   > `A filed report MUST NOT be edited in place, whether labelled or silent. A correction lands only in the correcting round's report or as an appended erratum in a new commit naming the superseded text; the r14 in-place edit is a form defect and MUST NOT be swept into the r13 report.`

3. **The candidate has no delivery mechanism for the new standard.** `scripts/shokunin-watchdog.sh:52-60` embeds mission/axes/L2/commit/L0 text, but none of the five child-lane contract items or `Gate standard`; `grep -n 'Prompt embeds contract' PROTOCOL.md` points to the existing M7 fact that prompts carry 1/5. A rule reached only by a lane voluntarily rereading `PROTOCOL.md` is aspiration, not an enforceable next-round standard. Replacement text:
   > `Delivery: the integrator MUST include the Gate-standard registry row, gate command, self-test invocation, verdict map, and pinned-value path in each dispatched child prompt (or record the exact missing items as a routed template defect); closure MUST not grade a gate as conformant until that prompt delivery is present.`

4. **Kotoba r12 is marked `ok` despite evidence the protocol calls non-completion evidence.** `MANIFEST` r12 says report untracked at completion and contains literal `LANE_HASH` (`grep -n LANE_HASH .ufo/reports/round-12/kotoba.md` → line 224); `PROTOCOL.md:90-101,192-200,235-236` says landed means committed, completion evidence satisfies the report contract, and missing heading/dead/orphaned hash/report-before-commit are defects. The candidate may choose status-neutral treatment for real work, but it must state why an unlanded placeholder report is not a completion-marker failure and make the rule match the r11 DRAFT treatment. Replacement text:
   > `An untracked report at completion is not landed completion evidence. If it contains a real resolvable round-work hash, record status ok only after the lane/respawn lands it; until then record in-flight (or failed where the marker rule applies) and carry the durability debt. A literal placeholder such as LANE_HASH is not a cited hash.`

5. **Sibling-only progress remains under-specified.** The new pin at `PROTOCOL.md:135-141` says sibling-authored files are not subject activity and to grade on own signals, but the r13 kotoba entry still says `in-flight`/progressing on `683d147/7163c81/ed5c261`, all aggregator-authored (verified `git -C kotoba-shokunin log`: those commits show `aggregator-shokunin`). Replacement text:
   > `Sibling-authored files alone MUST NOT satisfy progressing. If no subject-authored commit or subject-owned file evidence exists, record the lane as lacking a progressing signal; do not call it progressing, and do not call it silent/failed unless the stale-lane rule's silence threshold is met.`

The round-11 approach critique's MF-1 (explicit keying/frozen adjudication), MF-2 (self-test plus freeze-run), and MF-3 (capability rather than literal `--selftest`) were absorbed: the candidate adds row identity, frozen checker artifacts, and flexible self-test spelling. W-2 was **not** absorbed: the live-successor durability race is contradicted by the kake r13 sweep claim. W-3's ≤20-line Pareto warning was not absorbed (see Length cost).

## Contradictions

- **Red gate vs marker/step 1:** `PROTOCOL.md:157-162` says a marker is failed and real committed work is ok; `PROTOCOL.md:370-371` says a red gate is status-neutral unless rules prescribe failed. These are compatible only if the text explicitly says gate redness never converts a real report to failed, while a marker independently does. Add:
  > `Gate redness is never the marker predicate: step 1 determines marker-versus-real-report first; only a marker invokes failed, while a red gate remains a routed conformance defect.`
- **Landed report vs completion evidence:** `PROTOCOL.md:90-101` makes landed=committed; `:235-236` calls a contract-satisfying path completion evidence. The candidate's untracked kotoba `ok` entry violates that conjunction unless the replacement above is adopted.
- **Orphan order vs aggregator duty:** `PROTOCOL.md:205-212` gives the aggregator routed-defect/commit duties, while `:102-104` makes successor landing precede integrator sweep. The candidate must state that aggregator-owned corpus files are excluded and that neither aggregator nor integrator may pre-empt a live successor's report; otherwise the duties conflict.
- **Five writes vs invariant:** `PROTOCOL.md:166-177` adds L0 and wave artifacts to integrator writes, while `:418-423` says lanes write only own child repo/report and calls `.ufo/waves` integration evidence. Add an explicit exception:
  > `The protocol lane, as integrator-of-record, is the sole exception for MANIFEST rounds, L0 durability, and the current round's .ufo/waves closure artifacts; ordinary lanes remain confined to their child repo and report.`
- **Kake r14:** the observed labelled in-place edit is neither a new correcting report nor appended erratum; it must be recorded as a defect, not blessed as substantively right.

## Length cost

`wc -l -c PROTOCOL.md` observed `514 47874`; `git show HEAD:PROTOCOL.md | wc -l -c` observed `446 39718`: **+68 lines, +8156 bytes**. `awk 'NR<475' ... | grep -o 'round-[0-9][0-9.]*' | wc -l` → `4`; appendix (`NR>=475`) → `18`; the body round-reference budget stayed 4. The move is not Pareto on protocol soundness: the gate-integrity gain is real, but the candidate spends 68 lines while leaving delivery and durability contradictions. Smallest deletion set: remove the 36-line `## Gate standard` body section and retain only a ≤20-line registry-class rule plus the already committed checker/frozen artifacts; this addresses W-3 without deleting the absorbed row-identity/orphan/L0 pins.

## Falsified

- **Census passed:** `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md` observed `93/93 obligations found; 0 MISSING` (all I1–I13 and V1–V5 PASS).
- **r7 aggregator `ok`:** watchdog lines 171/189 show launch/complete; `6d27283` exists in main repo and `git log` shows aggregator identity at 20:32:43. Defensible, but the report was landed after completion (record defect).
- **r8 aggregator `in-flight`:** watchdog line 190 shows launch and no complete by the candidate cutoff; status is defensible. `supersedes` target r8 retroactive-closure exists in MANIFEST.
- **r11 protocol/kumitate `ok`, kengaku `in-flight`:** watchdog lines 195, 204, 181 support complete/launch facts. `kengaku-DRAFT.md` is 15922 bytes, wrong filename, and absent from tracked report path; `grep` for placeholders was attempted but the file moved during concurrent work, so that specific observation is not stable. The in-flight status is defensible on primary path evidence.
- **r12 kotoba `ok`:** watchdog line 197 supports completion and the report is 14009 bytes with `SHONEN` (grep found heading), but it is untracked and line 224 is literal `LANE_HASH`; this is not clean `ok` evidence under the landed/report-contract clauses. `4dd7753`, `abef8aa`, `d49dfa5` resolve in `kotoba-shokunin` history, but the placeholder remains a failed citation.
- **r13 kotoba `in-flight`:** watchdog line 198 shows launch/no complete at cutoff, but its “progressing” basis is sibling commits `683d147/7163c81/ed5c261` (all `aggregator-shokunin` in `kotoba-shokunin`); under the new pin this must not be called progressing.
- **r14 kasegi `ok`:** watchdog lines 202–203 support termination. `grep -c '^#{1,6} *SHONEN' .ufo/reports/round-14/kasegi.md` → `0`; commit `50b2179` exists, is operator-authored, and the report cites live ancestor hashes in kasegi repo but dead `4028846` (not found there). Real 7338-byte report plus real work makes `ok` defensible as a defective report, not a marker; SHONEN/dead-pointer/operator identity are defects.
- `supersedes` checking (Python over `MANIFEST.json`) was attempted but the first script had `NameError: name 'v' is not defined`; the six visible targets are the expected r7/r8 retroactive, r11 correction, r12/r13 closure entries. Re-run the corrected check before landing. Entry-keyed reproduction observed `71 ok / 3 failed / 14 not-dispatched / 2 in-flight` over 90 rows; lane-round-keyed dedup incorrectly collapsed to 48 rows (`28/2/17/1`), confirming the row-identity pin. Every visible r14 `not-dispatched` lane has a `lane_rounds` value in the candidate JSON.

## Gaps

- The watchdog advanced after the candidate cutoff: line 208 completes kagi r12 and line 209 launches r13, while the entries claim closed_at 20:55. The frozen checker must use its frozen cutoff, not the live log.
- Child-repo ancestry was checked by recent-log inspection, not a complete per-entry `merge-base --is-ancestor` loop; the cited main-repo hashes absent from main but present in child repos are not interchangeable.
- The candidate's new gate section is not yet committed, and no evidence was read that each lane has the mandated SKILL.md registry row; the standard is therefore not currently enforceable end-to-end.
