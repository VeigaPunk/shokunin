# kengaku — round 66 (hyaku run 15, attempt 1), 2026-11-03

Lane-root base, stated once: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`. Wave paths below are relative to it (`.ufo/waves/round-66/w1/...`). Lane tip at filing: `e02c2d9095b928df0f192ef0f30229857d63deea` (`git ls-remote origin refs/heads/master` prints the same hash). Freeze `9a07df6a`; receipt of record first run `2c1ef88a`; landing `e02c2d90`; fleet L0 question `74ddb468`.

## Work performed

**Declared claims (2).**
- **R66-C1 — coverage** (lowest owned axis, L0-capped at 7; capability acquisition `offline-torch-tensor-parallel-grader-probe`). Execute the pinned TB2 `torch-tensor-parallelism` grader offline against five frozen cases. **Verdict: admitted on the amended counter** (predicate met; capability enters; coverage held at 7).
- **R66-C2 — operability** (held at ceiling 10 if admitted; round-65 SecurityScan M-1, a fabricated receipt accepted by the R65 checker). Add a `--strict` mode to the R65 receipt checker. **Verdict: not admitted, kill rule (b)**: the frozen clause needs the receipt's `PROBE` sha, and the committed R65 receipt has no `PROBE` line. Operability held at 10; no change.

Frontier step (inside the claim cap, not a claim): sourced claim (C1 rests on S183, opened live this round); two registry defects repaired (S236, S237); the round-65 spot-check's routed items worked; one considerthese item selected (not implemented); Assimilation: none.

**Work items with evidence.**
1. Protocol load: `skill://shokunin`, kimi `protocol/` files, lane SKILL/PROVINCE/SCORECARD/QUALITY/README, round-65 lesson and spot-check (`corpus/lessons/round-65-verifier-spotcheck.md`). Source census start: exit 0, 227 rows at `f0587e53` (`corpus/evidence/round66/census-start.txt`).
2. Sources opened live 2026-11-03, captured under `corpus/evidence/round66/sources/`: S183 torch grader (sha `4ae4285e…`, `cmp`-identical; `test_outputs.py` 211 lines); S233 SQLite amalgamation zip (HTTP 200, 2990966 bytes, sha `0a9c8e34…`, listing `sqlite-amalgamation-3540100.unzip-l.txt`); S234 kv-store grader (sha `115de2e9…`, `cmp`-identical). Re-checked independently by the SourceReview seat (all pass).
3. Pre-freeze controls: the five-case probe run (`corpus/evidence/round66/tensor/prefreeze-run2.txt`; K1 13/13 P; K2 do-nothing exists F + 12 F; K3 stub exists P + 12 F; K4 column ws2/ws4 F; K5 row ws2/ws4 F; all `frozen=match`). Superseded later, retained (see item 9).
4. Freeze `9a07df6a`: `plans/round-66-claims.md`, `plans/round66_c1_tensor_probe.py`, the five cases (`corpus/evidence/round66/tensor/cases/{k1-ref,k3-stub,k4-col-nogather,k5-row-noreduce}/parallel_linear.py`; K2 is an empty `/app`), the red fixture `corpus/evidence/round66/red/fabricated-r65.txt` with its red-before checker output `corpus/evidence/round66/red/red-before-r65-checker.txt` (`PREDICATE R65-C1 pass`, rc 0), the wave spec and dispatch.
5. Wave `.ufo/waves/round-66/w1`: validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16; 13 spawn seats); ready file `.ufo/waves/round-66/w1.ready`; WAVE-DONE received for all 13 seats (`.ufo/waves/round-66/w1/w1-results.json`, 13/13 with output). Seat reports: `.ufo/waves/round-66/w1/<Seat>.md`.
6. Seat findings that changed the round (each recorded in the lesson's Mistakes rows and in claims Amendment A1):
   - FreezeReview F1: a receipt with no `CASE` lines passed the C1 counter (the frozen sentence binds every `case_sha`/`junit_sha`). F7: an unknown case name raised `KeyError`. F5: the junit directory was shared, so the post-freeze run overwrote the control's bytes.
   - SecurityScan M-1 to M-6: fabricated receipt accepted (no CASE, no junit); grader not re-hashed; malformed lines crash; the sandbox shared the host network (outbound connect succeeded) and PID namespace (a host process could be signalled); junit overwrite.
   - ReceiptGateBuild / ReceiptMutate: the strict proposal relaxed the frozen PROBE clause into a header binding; blacklist evasion (d1) and a false positive on free text (d2).
   - ProbeMutate: all live mutants killed (M1-control, M2, M3, M4, M5b, M5c, M6); M5 literal was a no-op; survivors none. DeterminismProbe: vectors identical across three runs; FRAGMENT and junit bytes are run-local (not invariant).
   - ClaimFalsifier: A1 coordinated rewrite accepted (limit); A4 cheating K1 passes the grader (limit: API-surface oracle); A5 hand-built receipt with copied bytes accepted (limit: not proof of execution).
7. **Amendment A1** (dated, `plans/round-66-claims.md`, landed `e02c2d90`): the counter enforces the frozen sentence as written (CASE presence; junit bytes beside the receipt, per receipt; VECTOR agrees with the junit it names; grader re-hashed on check; unknown and malformed lines named), and the sandbox adds `--unshare-net --unshare-pid`. The vector table, cases and kill rules are unchanged. Red→green on the amended counter: a receipt with its k1 junit forged to `<failure>` (junit sha rewritten to match) → `CHECK defect: k1-ref VECTOR disagrees with the outcomes its junit bytes record`, rc 1 (previously rc 0); selftest refuses no-CASE and malformed receipts (`SELFTEST` all True).
8. C1 receipts under A1: receipt of record `corpus/evidence/round66/tensor/receipt.txt` and control `corpus/evidence/round66/tensor/control-a1.txt` (both `PREDICATE R66-C1 pass`, rc 0). Junit bytes in `receipt.junit/` and `control-a1.junit/`.
9. Superseded records (kept, not re-judged): `corpus/evidence/round66/tensor/prefreeze-run1.txt` (first run, pre-fix sha `2a6aaacc…`; refused) and `prefreeze-run2.txt` (probe sha `c5ef1b54…`; refused under A1 — its junit directory `tensor/junit/` was retired and its bytes remain in commits `9a07df6a` and `2c1ef88a`). The claims doc's earlier sentences "removed unscored" and "junit receipt-local, cannot overwrite" were false and are corrected in Amendment A1.4 and A1.6.
10. R66-C2 proposal (`.ufo/waves/round-66/w1/ReceiptGateBuild/proposed/round65_c1_sqlite_probe.py`, `round65-strict.diff`): strict refuses the fabricated fixture (exit 1, named defects) and default output is byte-identical on both fixtures. It is **not** landed in `plans/`. Its pass on the committed R65 receipt uses a header/version binding, because the committed receipt has no `PROBE` line (`grep -c '^PROBE' corpus/evidence/round65/sqlite-gcov-probe.txt` → 0). That is not the frozen clause (kill rule b). Decision requested: L0 `kengaku | round-66` (`74ddb468`).
11. Frontier: `plans/round66_registry_check.py` (quote and meta counter; selftest 13/13; red: the superseded S233 and S234 rows and the S233 composite quote refused, rc 1; green: S236/S237 and the verbatim quotes pass, rc 0). Registry rows S236 (supersedes S233) and S237 (supersedes S234), both opening `teaches` with `supersedes S0NN —` (census E04 otherwise). S183 `used-by` gains the knowledge entry. Knowledge entry `corpus/knowledge/tb2-torch-tensor-parallel-offline.md`. Lesson `corpus/lessons/round-66.md` (Gate, Mistakes rows 1–13, landing verdicts). QUALITY Q49; README block.
12. considerthese: `considerthese/2026-10-26.md` item 2 ("One standing TB2 admission counter with a built-in filler control") is selected and recorded in the lesson; not implemented (`grep -rn tb2_grader_admit plans corpus SCORECARD.md` → 0 hits). Assimilation: none (merge/kengaku id drift, `kengaku | round-54`, adoption blocked).
13. Routed defects of round 65 (`corpus/lessons/round-65-verifier-spotcheck.md` §6): items 1, 2, 3 (S236/S237 supersession), 4 (this report states the lane-root base), 7 (census output committed under `corpus/evidence/round66/`), 8 (M-1 — open, see C2), 9 (partly), 10 (open). Items 5 and 6 (dated pointer and census-before corrections) are **open**: not landed in this round's commits and routed to round 67 with their evidence pointers.

## Landed changes

| commit | what | LOG / record |
|---|---|---|
| `9a07df6a` | freeze: claims doc, probe (pre-amendment), cases, pre-freeze control, source captures, red fixture, wave spec and dispatch | `LOG.md` Round 66 |
| `2c1ef88a` | receipt of record (first run; superseded by the A1 re-issue in `e02c2d90`) | `LOG.md` Round 66 |
| `e02c2d90` | landing: Amendment A1 (claims doc) and amended counter `plans/round66_c1_tensor_probe.py`; `plans/round66_registry_check.py`; receipts `tensor/receipt.txt`, `tensor/control-a1.txt` and their junit dirs; `corpus/knowledge/tb2-torch-tensor-parallel-offline.md`; `corpus/lessons/round-66.md`; `corpus/SOURCES.md` (S236, S237; S183 `used-by`); `corpus/QUALITY.md` Q49; `corpus/README.md` block; `SCORECARD.md` Round 66 section (incl. capability entry, planned round 67); `LOG.md` Round 66; census `corpus/evidence/round66/census-start.txt` and `census-end.txt`; wave evidence `.ufo/waves/round-66/w1/` | `LOG.md` Round 66 |
| `74ddb468` | fleet root `.ufo/l0-questions.md`: `kengaku | round-66` (R66-C2 PROBE-binding decision) | fleet L0 queue |

No change to a frozen case, the frozen vector table or a kill rule. The round-65 checker (`plans/round65_c1_sqlite_probe.py`) is unchanged.

## Before → after measurements

**R66-C1 (coverage, L0-capped at 7).** Measured against `e02c2d90`.
- Before: `grep -c torch-tensor-parallelism corpus/evidence/round52/graders/executed17.lst` → `0`; `corpus/evidence/round62/class-survey.txt`: `CLASS process-environment count=3 ... executed 0`.
- After: `python3 plans/round66_c1_tensor_probe.py --check-receipt corpus/evidence/round66/tensor/receipt.txt; echo $?` → `CHECK ok cases=5`, `PREDICATE R66-C1 pass`, exit 0. Control: `--check-receipt corpus/evidence/round66/tensor/control-a1.txt` → exit 0.
- Measured by the L1 at the landed tip: receipt and control exit 0 (commands above).
- Score: coverage 7 (held; L0 cap `kengaku | round-25/33/51` not lifted). Capability row enters the SCORECARD block (first working round 66).

**R66-C2 (operability, held at ceiling 10 if admitted).** Measured against `e02c2d90`.
- Before: `python3 plans/round65_c1_sqlite_probe.py --check-receipt corpus/evidence/round66/red/fabricated-r65.txt; echo $?` → `PREDICATE R65-C1 pass`, exit 0 (`corpus/evidence/round66/red/red-before-r65-checker.txt`).
- After (proposal, not landed): `--strict` on the fabricated fixture → exit 1 with named defects; `--strict` on the committed R65 receipt → exit 0 only via the header binding; the frozen `PROBE` clause cannot be met (`grep -c '^PROBE' corpus/evidence/round65/sqlite-gcov-probe.txt` → `0`).
- Default predicate, re-run at `e02c2d90`: `python3 plans/round65_c1_sqlite_probe.py --check-receipt corpus/evidence/round65/sqlite-gcov-probe.txt` → `PREDICATE R65-C1 pass`, exit 0; the fabricated fixture still → `PREDICATE R65-C1 pass` (M-1 open).
- Score: operability 10 (held; no admission, no change).

**Counter red→green (amended C1 counter, `e02c2d90`).** Forged-junit receipt → rc 1 `k1-ref VECTOR disagrees with the outcomes its junit bytes record` (was rc 0); no-CASE receipt → refused by name (selftest); unknown case → named (selftest fixtures).

**Frontier counter (`plans/round66_registry_check.py`).** `--selftest` → 13/13 True, rc 0. `meta` on the superseded S233/S234 rows → rc 1 (red); `meta` on S236/S237 → rc 0 (green); `quote` on the lesson's three QUOTE lines → rc 0.

## Sources & frontier

- **SOURCES.md before → after.** Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Before: `227` (at `f0587e53`: `git show f0587e53:corpus/SOURCES.md | grep -cE …` → `227`). After: `229`.
- **Rows added by tier.** S236 (tier A, code), S237 (tier A, code). Both `mined`, opened 2026-11-03, recheck `180d`, used-by `corpus/lessons/round-66.md`, each with a located quote in the lesson's `## Gate` (`QUOTE` form, grep-F-able in `corpus/evidence/round66/sources/`).
- **Rows touched old→new.** S183 `used-by`: `corpus/knowledge/tb2-grader-vacuity-triage.md` → `corpus/knowledge/tb2-grader-vacuity-triage.md, corpus/knowledge/tb2-torch-tensor-parallel-offline.md`. S183 `status`: `mined` → `mined` (the claims doc's "queued → mined" premise is false for the committed row; logged, not edited — claims Amendment A1.8). S233 and S234 are superseded by new rows; their own fields are unchanged.
- **Census.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0 at start (`corpus/evidence/round66/census-start.txt`) and at the landing tip (`corpus/evidence/round66/census-end.txt`; warnings only, `grep -c 'E0\|E1'` → 0). Re-run by the L1 at the landed tip: exit 0.
- **Frontier rows advanced.** S183 (sourced claim for R66-C1, re-opened live); the knowledge entry is the first `process-environment` member on this lane's frontier.
- **Mistakes mined.** `corpus/lessons/round-66.md` `## Mistakes`, rows 1–13 plus two mined at landing (sandbox scope; survivor in the selftest). Rows closed: 1, 2 (fixed, shown red→green), 9, 10, 11, 12, 13, and the sandbox and selftest items. Open: row 3 (strict not admitted; M-1 open) and rows 4–7 (dated corrections not landed; routed to round 67). Row 8 (false S183 premise) reported, not edited.
- **considerthese.** One item selected (2026-10-26 item 2), not implemented; recorded in the lesson.
- **Assimilation: none** — the merge/kengaku package's id drift is open (`kengaku | round-54`); this round adopts nothing.
- **Discernment sample for the non-author closure.** Admit: S236, S237. Reject: S234 `teaches` (meta-text), S233 quote (not verbatim). Verdict pending the closure (`corpus/lessons/round-66.md` `## Landing verdicts`).

## Trend verdicts

- **expansion: improved.** A knowledge entry on a previously unexecuted class member (`process-environment`, first member, `corpus/knowledge/tb2-torch-tensor-parallel-offline.md`); the grader executed offline (receipt of record, `PREDICATE R66-C1 pass`).
- **quality: improved.** Two registry defects repaired by superseding rows that pass the new counter (S236, S237); the C1 counter now enforces its own frozen sentence (Q49), shown red→green. Not `harmed`: the open C2 item is a miss, not a regression (the R65 default predicate is unchanged).
- **discernment: unchanged.** The round-65 spot-check's two form disagreements are repaired and mined; the round's own gate decisions await the non-author closure. Not self-attested.

## SHONEN

Four boxes, `SHONEN.md`. No `[x]`: no non-author verifier has written a box this round.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` (not edited this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 66 (offline grader run; receipt `corpus/evidence/round66/tensor/receipt.txt`).
- [~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/tb2-torch-tensor-parallel-offline.md` (`recheck:` command, `plans/round66_c1_tensor_probe.py`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `.ufo/waves/round-66/w1/SiblingOverlap.md` (no sibling-owned ground; PROVINCE.md not edited).

## Round shape, seats, and conformance

- **Shape.** One v1 wave, 13 seats (`.ufo/waves/round-66/w1/w1-spec.json`; validator `w1-validate.stderr`; band 8–16). Seat roles: scout 1 (TensorRecon), executor 2 (ReceiptGateBuild, QuoteGateBuild), mutation-tester 2 (ProbeMutate, ReceiptMutate), reviewer 2 (FreezeReview, SourceReview), critic 1 (ClaimFalsifier), sentinel 1 (SecurityScan), scribe 2 (KnowledgeDraft, LessonDraft), connector 1 (SiblingOverlap), revenger 1 (DeterminismProbe).
- **Attack share.** Reviewer 2 + critic 1 + mutation-tester 2 = 5/13 = 38% (≥25%). Connector 1 (≤2). Residual call: none.
- **Dead seats.** None; 13/13 settled with output.
- **§3 L2 floor — conformance defect.** The floor asks for 3 executors; the wave carries 2 (the third was not dispatched). The DeterminismProbe revenger and the two mutation-testers ran probes, which partly covers the gap. Recorded as a minimum-content defect of this round, not a marker.
- **Planner.** The L1 holds the §3 planner seat (`planner` is frozen-topology, not a swarm role).
- **Routing.** Routes per the run-15 map; the seats did not record their answering model. No claim depends on a seat's answering model.
- **Mid-wave counter amendment.** The counter changed after the attack seats had measured it (Amendment A1). The receipt of record and control were re-issued under the amended bytes; the attack reports measured the earlier bytes and are cited as such.
- **§3 misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file from this round at the fleet root (only orchestrator-owned `.scratch/` entries, not touched).
- **Scratch.** Seat and L1 scratch under `/fast/scratch/hyaku/kengaku-r66` (removed at the end of the round). The torch venv is at `~/.local/share/kengaku-r66/venv-torch` (outside the reaper's scope; recreate command in `plans/round66_c1_tensor_probe.py` `setup_error`).
- **Stale-lane.** Not stale: the wave settled within the round; no mission was open longer than two driver ticks.

## Tool installs (tool, version, channel, reason)

- `torch` 2.15.0+cpu — `uv pip install --index-url https://download.pytorch.org/whl/cpu` (official PyTorch CPU index), into `~/.local/share/kengaku-r66/venv-torch`. Reason: the process-environment class needs a gloo-capable torch; this host had none.
- `transformers` 5.22.1 and `pytest` 9.2.0 — `uv pip install` from PyPI, same venv. Reason: pytest runs the grader; transformers is not used by the torch grader (installed for the pipeline member, unmeasured).
- `uv` 0.13.0, `bubblewrap` 0.13.1, `gcc`/`gcov` 16.2.1 — existing; not changed.
- pacman: not used (paused host-wide).
- `RULES.md` was read before the first install.

## Open items and L0

- L0 open: `kengaku | round-25/33/51` (coverage cap), `kengaku | round-56`, `kengaku | round-63` (amended K2 detector), `kengaku | round-54` (merge/kengaku id drift), and new `kengaku | round-66` (`74ddb468`: the PROBE binding for the R65 strict gate).
- Carried to round 67: C2's successor (a PROBE-binding predicate frozen before data; the `fabrication-declaration` scan limited to field lines); round-65 mistake rows 5–7 dated corrections; the considerthese item 2 as a frontier candidate; the process-environment class's other two members (`install-windows-3.11` needs qemu, absent on this host; `torch-pipeline-parallelism` unmeasured).
- Limits named, not hidden: the grader is the oracle and sees the API surface, not sharded execution (ClaimFalsifier A4); the receipt check is not proof of execution (A5); the junit bytes are run-local.

## Pre-report gate

- `git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master` → `e02c2d9095b928df0f192ef0f30229857d63deea refs/heads/master` (equals the lane tip, `jj-lane.sh state` → `local=… remote=… ahead=0 behind=0`).
- `grep -c '^## SHONEN'` on this report → `1`.
