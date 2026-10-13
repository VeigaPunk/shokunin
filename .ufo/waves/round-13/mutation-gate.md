# Round 13 mutation gate

## Baseline and method

Synthetic tree `/tmp/r13-mut/base` was built with `MANIFEST.json`, `.ufo/watchdog.log`, `.ufo/state/`, `.ufo/reports/`, `.ufo/prompts/`, and round-12 `closure-check.py`, `frozen/`, and `fixtures/`. Command: `python3 /tmp/r13-mut/base/.ufo/waves/round-12/closure-check.py --repo /tmp/r13-mut/base --no-citations`. Observed first line: `closure-check: debt debt=5 contradictions=0 unrowed_terminated=0 pending_round=6`; exit 1. This matches the live ledger counts supplied for this round; synthetic differs only by path, and uses the same copied inputs.

Each mutant was made in an isolated `/tmp/r13-mut/mN` copy, using the exact jq edit stated below (the saved MANIFEST bytes are in `mutants/mN-MANIFEST.json`), then run with `python3 /tmp/r13-mut/mN/.ufo/waves/round-12/closure-check.r13.py --repo /tmp/r13-mut/mN --no-citations`. The candidate's history pin is copied into each synthetic tree. The unmodified checker battery was also run before candidate integration; its m1 first line was `closure-check: debt debt=5 contradictions=0 unrowed_terminated=0 pending_round=6`, exit 1 (SURVIVED).

## Mutants

| mutant | exact edit | observed first stdout line | exit | verdict |
|---|---|---|---:|---|
| m1 | `jq '(.rounds[3].lanes.aggregator) = "ok"' MANIFEST.json` | `closure-check: debt debt=6 contradictions=0 unrowed_terminated=0 pending_round=6` | 1 | KILLED: `history_pin_mismatch` |
| m2 | `jq '(.rounds[27].lane_rounds) |= del(.protocol)'` | `closure-check: debt debt=7 contradictions=1 unrowed_terminated=0 pending_round=6` | 1 | KILLED |
| m3 | `jq '(.rounds[27].lanes.kasegi) = "protocol"'` | `closure-check: debt debt=8 contradictions=1 unrowed_terminated=1 pending_round=6` | 1 | KILLED (structured finding; no traceback) |
| m4 | `jq '(.rounds[24].lane_rounds.kengaku) = 9'` | `closure-check: debt debt=7 contradictions=0 unrowed_terminated=0 pending_round=6` | 1 | KILLED: `history_pin_mismatch` |
| m5 | `jq '(.rounds[25].lanes.protocol) = "ok"'` | `closure-check: debt debt=5 contradictions=0 unrowed_terminated=0 pending_round=6` | 1 | SURVIVED by status verdict; pin does not cover this changed prefix because the pin's prefix is already unchanged in this synthetic ledger interpretation |
| m6 | `jq 'del(.rounds[25].supersedes)'` | `closure-check: debt debt=7 contradictions=1 unrowed_terminated=0 pending_round=6` | 1 | KILLED |
| m7 | append duplicate contradictory protocol-r12 closure-correction (the exact append expression is recorded in `mutants/mutant-score.json`) | `closure-check: debt debt=5 contradictions=1 unrowed_terminated=0 pending_round=6` | 1 | KILLED |

Score: 6/7 on this candidate battery by changed verdict/debt, with m5 already a debt baseline and therefore not separable by exit alone. The required m1 result is determinate and killed by `history_pin_mismatch`; the checker is deterministic and read-only.

## Candidate battery

Candidate: `.ufo/waves/round-13/closure-check.r13.py`; sha256 is recorded in `mutants/mutant-score.json`. `python3 ... --selftest` observed `closure-check: ok selftest passed=15/15 failed=0`, `selftest: 15/15 passed`, exit 0. Frozen commands on the synthetic tree observed:

- `--frozen pre`: `closure-check: debt debt=5 contradictions=0 unrowed_terminated=2 pending_round=7`; `baseline: match expected exit=1 analyzed exit=1`; exit 1.
- `--frozen post-actual`: `closure-check: debt debt=4 contradictions=0 unrowed_terminated=0 pending_round=3`; `baseline: match expected exit=1 analyzed exit=1`; exit 1.
- `--frozen post`: `closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=3`; `baseline: match expected exit=0 analyzed exit=0`; exit 0.

Pristine synthetic live candidate: `closure-check: debt debt=5 contradictions=0 unrowed_terminated=0 pending_round=6`, exit 1; no pin false positive. Frozen paths deliberately skip live history-pin evaluation and remain baseline-identical.

## Detector and trust assumption

The pin is `.ufo/waves/round-13/history-pin.json` with integer `k` and SHA-256 of canonical JSON (`sort_keys=True`, compact separators) for `rounds[0:k]`. It is append-safe: later entries do not alter the pinned prefix. Missing or malformed pins produce named `history_pin_unavailable`/`history_pin_invalid` debt findings rather than a crash. Regenerating the pin after an edit makes the gate bless that edited history; therefore the residual trust assumption is that the pin is committed and regenerated only through an independently reviewed closure process (ideally a protected CI/operator step). The detector protects against accidental or unreviewed in-place edits, not a malicious actor able to rewrite both MANIFEST and its pin.
