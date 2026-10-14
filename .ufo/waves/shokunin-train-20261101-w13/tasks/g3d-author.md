# r82 AUTHOR (g3d) — evalcat residual fold + parser-hazard pinned cells

Read SHARED.md + r81 author/adjudicator + r80-critic reports first.

ARM A — evalcat residual fold (xconnector X7, small bounded).
r80-critic's six-category fold landed 4/6 in r81 (catalogue 8->14).
Fold the uncovered two + representative witnesses (~6 classes total):
- `update_tag` (tag != eval — the PUREST discriminating witness;
  adjudicator-noted)
- one custom-setter class (e.g. a property setter that tags internally)
- `libraries.load` or `libraries.write` (data-layer)
- `instance_empty`/`instance_collection` (relations)
- `batch_remove` (destructive batch)
- `evaluated_get` on a stale ID (name-vs-behavior edge)
All bare rows inside arm_evalcat before `closed`, under the closed-set
falsifier (violations=0 must hold). Same _ec_* machinery as r81.
Prediction (measured-inert priors): all held=stale, edge=1-or-absent,
handler deltas 0. If ANY flushes a watched handler -> the falsifier
fires; report it, that's the design.

ARM B — parser-hazard pinned cells (xconnector X6, pin-level).
The r81 contract covers distinct-key attribution + marker presence +
physical last-wins + drop-not-misattribute on the glued line. Now pin
the RESIDUAL hazards as explicit battery cases (through the tracked
parse_arms at bpy_battery.py:211-220):
- forged `violations=0` row injected mid-stream -> parser must NOT let
  it mask a real violation (pin: does the battery detect the forgery —
  measure and pin whichever behavior exists, honestly)
- dup_flush forged logical-last (same key, later forged value wins —
  pin the physical last-wins behavior as the CONTRACT, documented)
- binjunk non-UTF-8 bytes -> capture/decode behavior pinned (likely
  UnicodeDecodeError class — pin as known-failure-mode cell, or the
  guarded decode if implemented)
- detach-child EOF-hold cell (bounded): detached descendant delays
  capture EOF — pin harness behavior under the battery timeout
Hazard pins are CONTRACT pins: they document measured parser behavior,
not safety claims. Wording: "the demonstrated hazard resolves as X" —
never "the parser is safe".

Prior 118 ARM rows byte-identical; falsifier liveness re-verified.
Report -> reports/round-82/r82-author.md.
