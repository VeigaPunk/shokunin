# kengaku — round 13

**Axes:** novelty + calibration (LLM evaluation/research).  
**Selected axis:** novelty, the current floor.

## Data walk

- `MISSION.md` assigns this lane novelty + calibration; `AXES.md` requires one measured axis-move and a before→after scorecard record.
- The current `SCORECARD.md` post-round-11 table scores novelty **6** and calibration **8**. The next axis-move is novelty.
- The child worktree already contains user-owned round-12 edits (`SKILL.md`, `grader.py`, and untracked round-12 evidence). Round-12’s own mutation artifact reports the promoted analyzer selftest and full replay failed; those files will remain untouched and will not be cited as verified round-13 evidence.
- The committed round-11 JSONL has 64 `meta` records, eight `A-CKPT710-ack` records per pid, raw response captures, and truth trajectories. Its `-ack` label is not the request intent: `run_r11.py:76-80` asks `Reply 'ok'` at turns **2–6 and 9** (384 true ack-only responses), but the initial state at turn 1 and post-checkpoint spillover state at turn 8 are both requested full-state outputs and still logged under `-ack`. The ack raw field is truncated to 80 characters (`probe_plan_r11.md:32-35,59-60`). Round 11 reports a simple `startswith('ok')` count and warns it is a lower bound on full-state emission (`analysis_r11.md:30`; `probe_plan_r11.md:137-144`).
- Concrete boundary case: pid 203 turn 8 is a requested spillover full-state response, not an ack-only response. Its JSON matches truth after operation 8 (`ADD nails 3`), but it must be excluded from the ack-only denominator and can serve as a negative control. This catches a flaw in the initial turn-set hypothesis before any measurement.
- The r11 input is committed local evidence; this move needs no endpoint traffic. The main and child `origin` remotes resolve to the authorized VeigaPunk repositories; both branches had zero local-only commits at inspection.

## WWKD plan — request-intent-aware ack-state audit

**Question:** among turns whose prompt actually asks only `Reply 'ok'`, how often does the model emit a complete, exactly correct state snapshot instead—and what can the 80-character capture safely establish?

1. **Skeleton:** implement a stdlib-only analyzer over committed `round11-power/results-r11.jsonl`; join `A-CKPT710-ack` records to `meta.truth` by `(pid,turn)`. Use the code/plan schedule to separate true ack-only turns `{2,3,4,5,6,9}` from state-request turns `{1,8}`. Do not infer intent from the `-ack` suffix.
2. **Overfit one real instance:** pid 203, turn 8 is a state-request negative control and must not enter the ack-only numerator or denominator. Hand-check one true ack turn against the same pid's truth.
3. **Measure:** on the 64×6 = **384** true ack-only responses, report explicit `ok/no-state`, `complete exact state`, `complete wrong state`, and `unresolved raw` categories. A complete state means a parseable JSON object fully contained in the stored 80-character raw field and equal to `meta.truth[turn-1]`; a truncated/unparseable raw field is unresolved, not a model error. Report turns 1 and 8 separately as schedule-label controls. Recompute exact equality from raw JSON and truth, never trust stored `ok` fields. Any relation to later checkpoints is descriptive only.
4. **Price and boundary:** scout public prior art for exact request-intent-aware state-fidelity scoring on acknowledgement-only turns; connector checks sibling ownership. Route reusable prompt-craft implications to kotoba rather than absorbing them.
5. **Verification gate:** deterministic selftest covers plain `ok`, exact JSON, wrong/partial JSON, truncated raw, and the turn-8 exclusion. On committed r11 bytes, assert unique `(pid,turn)` join keys, 64 meta rows, 384 ack-only records (exactly six per pid), and category totals = 384. Increase the novelty score only if the in-repo instrument measures a distinct construct and the prior-art review supports the scoped wording.

**Out of scope:** changing round-12 user files; new model requests; changing the benchmark prompt or task generator; interpreting capture truncation as model failure; causal, cross-model, or universal claims; changing other axes.
