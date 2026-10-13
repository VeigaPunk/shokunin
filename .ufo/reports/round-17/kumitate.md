# Kumitate — round 17

## Axis move

**Axis:** `coverage:runtime-layer`, the tied lowest axis at round start.

- Before: `C1r=11/11`, `R_sections=60`, `R_members=98` ⇒ `floor(10 × 60/98)` = **6**.
- After: R1 gained eight member sections and R8 gained its missing `native_dispatch_topology.rs` section, so `R_sections=69` ⇒ `floor(10 × 69/98)` = **7**.
- Held: `coverage:script-layer` **6**, operability **8**, retired aggregate coverage **10**.

The threshold for 7 was 69. R1 alone would have reached 68/98 and still scored 6, so R1 0→8 and R8 3→4 were landed atomically. Lane commit `c860887` (`round-17`) is pushed to `VeigaPunk/kumitate-shokunin`.

## Delivered

- `corpus/knowledge/native-judge-pipeline.md`: one gate-recognized section for each of R1's eight declared files, each with a live own-file anchor and a verbatim source symbol.
- `corpus/knowledge/native-transcript-ledger-seats.md`: internals-level `native_dispatch_topology.rs` section covering FIFO task/result binding, exact dispatch matching, spawn evidence, wave-token reuse refusal, Main's three-call shape, `probe_parent`→labrat, and nested-dispatch refusal.
- `SCORECARD.md`: claim block, axis row, move log, limits, retired-successor table, and round-18 plan updated. Current runtime numerator is 69/98; current script numerator remains 74/114.
- `corpus/lessons/round-17.md`, `corpus/README.md`, `SKILL.md`, and the gate companion notes updated to the measured state.
- `scripts/round-gate.mjs`: uncounted portability repair. Its stale lowercase absolute main-repo default failed after the checkout moved to `~/Projects`; the default now derives the lane repo's parent. Explicit flag/environment precedence is unchanged.

No domain source tree was modified. The origin checkout was read-only evidence.

## Verification

Observed before the lane commit:

- `node scripts/claims-check.mjs --row R1 --row R8 --strict` → `CLAIMS: MATCH (rows=2 yes=2 notes=2 sections=12 adv=0)`.
- Independent census → R1 occurrences=8/distinct=8; R8 occurrences=4/distinct=4.
- `node scripts/claims-check.mjs` → `MATCH`, 19 rows, 146 raw sections, 14 advisories. Reconciliation: 74 script + 69 runtime in-family sections + R9's 3 out-of-family sections = 146.
- `node scripts/proxy-check.mjs` → `MATCH`; `S=74/114 coverage:script-layer=6`, `R=69/98 coverage:runtime-layer=7`, five pins match.
- Live surface smoke → `SURFACE_PROBE: CLEAN` with 12/12 checks and one non-gating origin warning.
- Executable checklist → 10/10 pass.
- Hermetic suites → cite-check 20/20, surface-probe 38/38, round-gate 57/57, proxy-check 71/71, claims-check 35/35.
- `node --check scripts/round-gate.mjs` and `git diff --check` → exit 0.
- Live citation scan → 14 errors, all in two sibling-authored aggregator artifacts already recorded as third-party residue; zero errors in lane-authored prose.

## Falsification and limits

The critic reproduced a real disagreement between the score proxy and claims gate: the proxy sums section occurrences, while the claims gate deduplicates files only for its declared-count finding. A duplicate-one/drop-one R8 fixture retained four occurrences and a warning-only `MATCH` while covering three distinct members. Therefore the pre-registered “zero errors” halt was rejected. The landed evidence uses strict advisory-free row checks plus explicit occurrence=distinct equality.

The durable distinct-numerator fix and mutation case remain queued for an operability round. They were not hidden inside this coverage move.

Other uncounted repairs:

- Removed backtick semantics from R1's obsolete native wildcard explanation; otherwise `familyPatterns()` widened the eight-member family to every native-prefixed Rust file.
- Corrected R8's contract ordinals: seat coverage 55th, ledger 56th, dispatch topology 57th, transcript 60th.
- Corrected the agent-XOR citation to the seat-coverage validator rather than the unrelated duplicate-launch-record arm.
- Removed three new lane-local citation failures: one runtime receipt leaf misclassified as a source citation and two superseded content hashes represented as current pins.

## L2 concurrency

One batched dispatch launched nine L2 lanes: planner, four R1 executors, R8 scout, critic, mutation-tester, and connector.

- Planner independently confirmed the 69 threshold, R1-alone failure at 68, and runtime as a valid tied-floor choice.
- Executors split the eight R1 files and produced source-backed member sections.
- R8 scout strict-checked the fourth section on a scratch copy and found the pre-existing ordinal mismatch.
- Mutation lane confirmed partial-R1 drift, R8 warning clearance, inert prose-first headings, and dead-anchor rejection.
- Critic found the occurrence/distinct hole described above.
- Connector found no literal target-basename overlap across six sibling corpus trees and no ownership conflict. Adjacent runtime wording in Kagi/Kama did not claim these Rust internals.

## Fallback relay

Effective configuration observation: `modelRoles.m_swe` resolves to `devin/swe-2:max`; `retry.fallbackChains.m_swe` is `null`. Daybreak is separately mapped as `m_daybreak`, not exposed as an m_swe fallback chain. No genuine m_swe capacity failure occurred, so no fallback advance was observed or forced.

## SHONEN status

- Real decision tables, error patterns, executable checks, and source citations remain present.
- End-to-end round task executed and logged.
- Instructions remain runnable without oral context.
- Province boundary held: orchestration/tooling only; sibling overlap was reported, not absorbed.

Promotion remains an integrator decision; this round does not self-promote.

## Next move

`coverage:script-layer` is now uniquely lowest at 6. Round 18 is pre-registered to complete S2's eight-member native trial/collector family: 74→82/114, score 6→7. Four collector-library members have no existing corpus/SKILL basename hit, so the move requires fresh source analysis rather than prose reformatting. Distinct-numerator hardening, the cite-check fence defect, and other operability items remain queued because operability is not the floor.
