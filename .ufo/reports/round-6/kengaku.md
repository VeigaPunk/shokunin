# kengaku-shokunin — round-6 report

Commit: `d5f1cad` (`round-6`) in `kengaku-shokunin/`.

## Gap selected

Corpus README's two executable open gaps: *"n≥2 on flip-capable tasks"* (8
v2→r5 flips unclassified) and *"27 test-timeout: solvable-but-slow vs
algorithmically wrong"*. Both closed this round against the live local
endpoint. Third gap (planning-horizon coverage) remains open — no local
multi-step harness exists.

## What landed

| Artifact | Content |
|---|---|
| `corpus/knowledge/bench-arena-round6-stability.md` | n=3 probe of 8 flip tasks + 3 controls: 5/8 scaffold-determined, 2/8 noise, 06 strategy-bound; status≠sha rule; canary refresh |
| `corpus/knowledge/bench-arena-task27-timeout-anatomy.md` | faulthandler-instrumented post-mortem: `_active` hidden contract → thread-exception deadlock; r5 sol also semantically broken; r6 gen fails on hallucinated `Condition(condition=…)` kwarg |
| `SKILL.md` | +4 parsing rules: scaffold-vs-noise n≥2 rule, strategy-bound truncation (doubled cap), rc=124 crash-deadlock signature + faulthandler method, status-stability ≠ sha-stability |
| `corpus/knowledge/bench-arena-round5-battery.md` | Corrected 27's "slow not wrong" reading → hidden-contract deadlock over a semantically broken sol |
| `corpus/README.md` | +2 index rows; 2 gaps marked CLOSED with pointers; 1 new gap opened (scaffold-delta mechanism) |
| `LOG.md` | round-6 entry with evidence trail |

## Executed evals — headline numbers

**Stability probe** (33 runs: 11 tasks × n=3, temp 0.2, max_tokens 4096,
direct `POST 127.0.0.1:34113/v1/chat/completions`, graded by `grade.sh`):

- **5/8 flips scaffold-determined** (03, 08, 12, 13, 31 — unanimous ×3) —
  opencode-vs-API decides them, not sampling.
- **2/8 true sampling noise** (09, 20) — both wide-shallow SQL tasks.
- **06 strategy-bound**: `finish=length` at 4096 *and* at 8192 (65.5 s) —
  exponential regex expansion; compact-mode reps (45 tok) emit wrong regex.
  Bimodal failure family; no token budget fixes it.
- Controls: 01 PASS ×3 identical sha; 33 FAIL ×3 identical sha; 13
  FAIL ×3 identical-wrong sha (new deterministic-FAIL case).

**Task-27 anatomy** (faulthandler-instrumented test, 4 sols exercised):

- Reference PASSes whole test in **0.23 s** — nothing about it is slow.
- r5 sol: 6 reader threads die on `rw._active` `AttributeError` (private
  attr absent from prompt.md — hidden contract); main hangs on `Barrier(7)`
  → the rc=124 "timeout" is a **thread-exception deadlock**.
- `_active` alias patch: unblocks phase 1 → reveals `RuntimeError: release
  unlocked lock` + writer-preference violation. r5's sol was broken
  *underneath* the hang.
- r6 fresh gen: instant `TypeError: Condition(condition=…)` — third failure
  family, API hallucination.

## Calibration delta

Predicted ≥5/8 noisy flips; observed 2/8. Direction right (stability
classifiable, controls held), magnitude wrong — scaffold dominance
underestimated at temp 0.2. New prior recorded in knowledge entry.

## Open frontier

New gap: **scaffold-delta mechanism** — 5 unanimous flips show which harness
won but not why; needs a scaffold-variant ablation (system-prompt on/off ×
tool surface) to isolate the causal surface. Remaining: planning-horizon
coverage (no local multi-step harness).
