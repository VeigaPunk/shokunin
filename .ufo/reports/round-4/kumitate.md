# kumitate-shokunin — round 4 report

## Axis walked

Gap selection: corpus README + round-3 lessons both named
`crates/ufo-core-runtime` ("loop-driver/native-admission internals") the
biggest unmapped surface — and the only judged path in the dispatch table.
Round 4 maps it. Two read-only scouts fanned over the crate's own family
boundary (`loop_driver*` / `native*`); I read the crosscut wiring myself
(`lib.rs`, `ufo-cli`, `native.rs::judge_handoff`, `native_contract.rs`,
`state.rs`).

## Landed (commit `round-4` = e0f5ca7)

- `SKILL.md` — new "Core-runtime map" section: contract-hash fuse
  (`NATIVE_CONTRACT_FILES` 66-entry ordered registry,
  `MAX_CONTRACT_FILE_BYTES` 256 KiB, `MIN_CONTRACT_HEADROOM_BYTES` 8 KiB),
  handoff decode posture (deny_unknown_fields, profile = version, named
  regular file ≤16 MiB), judge order, verdict vocabulary, loop stops,
  resume posture. `ufo` CLI section updated: `membrane-seal` command added;
  exit codes corrected; `self-iter` → `run_dry_until_halt` clarified
  (dry = fixture substrate, not a smoke path).
- `corpus/knowledge/native-judge-pipeline.md` — CLI intake, handoff schema
  (21 required + 8 optional fields, three profiles), full judge order,
  refusal vocabulary per module, verdict fields, contract-hash mechanism,
  classifier.
- `corpus/knowledge/loop-driver.md` — entry points, five-stage round
  pipeline, `LoopOutcome`/`BrakeTelemetry`/`stop_evaluation` vocabulary,
  `LoopState` checkpoint inventory, module table, traps.
- `corpus/lessons/round-4.md` — method + traps.
- `corpus/README.md` — coverage map + gaps rewritten (added the previously
  unlisted `swarm-wave-lifecycle.md` entry).
- `LOG.md` — round-4 entry with evidence.

## Corrections to prior SKILL.md claims

1. `classify_failure` → actual Rust symbol is `classify_failure_fields`
   (`native_text.rs:161`); `FAILURE_RULES` first-match order; advance
   authority is `FailureClass::permits_advance` (`execution_profile.rs:447`).
2. Exit code 2 covers EVERY typed local refusal (kinds
   `invalid|json|validation|io` via `fail_local` `main.rs:906`), not only
   "usage rejection"; untyped failures are exit 1 (`ufo: <err>`).

## Key facts now captured

- Verdict-bearing outcomes (admit OR reject) emit
  `.ufo/rounds/<runId>/r<NN>-digest.json`; a refused handoff is an `Err`,
  never an `Unsound` verdict — `RoundValidity::Sound` is the only native
  construction (`native.rs:398`).
- `mission_goal` derives only from plan `acceptance_criteria`; any
  unmeasurable criterion dominates to `unverified` (`native.rs:626`).
- Mid-round contract drift is caught by hash: launcher freezes the contract
  hash, collector re-reads `ufo status`.
- Critical-seat `lane_timeout` invalidates the round — D1a retry is a
  substrate action, not a judge patch (`native_telemetry.rs:~870`).
- Checkpoints are protocol-fingerprinted (`ufo.fsd.v4`) — bumps refuse all
  old checkpoints deliberately.
- Editing `native.rs` is a contract act: 8 KiB headroom fuse; overflow goes
  to `lib.rs`/registry siblings.

## Remaining gaps (in scope order)

native-trial launch sequence (wall handoff/pane binding); the-tick ops
beyond `path_ping`; fleet-dispatcher front half (claim/dispatch, whip);
`native_seats`/`native_admission_text` helper detail, `lease`/`live`/
`lane_overlay`/`cost_ledger` internals, `l3_swarm`.

## Evidence

Sources read: `native.rs`, `native_schema.rs`, `native_header.rs`,
`native_contract.rs`, `state.rs`, `loop_driver.rs`,
`ufo-cli/src/main.rs`, `lib.rs`, `conformance/fixtures/native-handoff/
handoff.json`; scout maps over the remaining `loop_driver_*` and `native_*`
modules (agent transcripts `LoopDriverMap`, `NativeAdmissionMap`).
Commit verified: `git log` = e0f5ca7, tree clean.
