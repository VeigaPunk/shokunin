# kumitate-shokunin — round 5

Commit: `e748e44` (`round-5`) in `kumitate-shokunin/`.

## What landed

The two longest-standing named gaps — both survived from round 3's gap
list — are now mapped:

1. **Native-trial launch sequence** (`corpus/knowledge/native-trial-launch.md` +
   SKILL.md "Launch sequence" section): the full `main()` spine of
   `run-omp-native-trial.mjs` as an ordered gate stack — input freeze →
   path/rerun/predecessor guards → idempotency decision → membrane-seal +
   resume-anchor gates → session + contract-mirror checks → wall handoff →
   deferred assignment authoring → O_EXCL pre-dispatch anchor →
   full-policy re-resolve drift gate → phase-0 domain probes → epoch
   receipt → attested omp spawn → session pairing → collector → Rust
   judge → verdict.json XOR rejection.txt → tick marker + pane retirement.
   Includes the complete post-validation refusal vocabulary, the rollback
   asymmetry (only the snapshot rolls back), and the traps
   (`manifest.json` post-dates the session; `.omp/config.yml` carries no
   routing; `telemetry` is dead; `autoRegisterInvokedNativeTrial` is a
   boolean).

2. **Fleet-dispatcher front half** (`corpus/knowledge/queue-and-claim.md` +
   SKILL.md summary): `pending-work.json` schema and lock discipline,
   `validateQueueTask` field map, `claimNextTask` pipeline, the four
   never-conflate counters (attempts / resumeAttempts / launchMisses /
   watchdog attempt N/3), state vocabulary (`blocked` non-terminal,
   `failed` never written, `launching` = claim lock not process), the
   `repend` door the watchdog uses, and ledger kind census.

## Latent defect surfaced (cross-domain, reported — not owned)

`sealBoundaryViaRuntime` (run-omp-native-trial.mjs:1931) shells
`ufo membrane-seal write --root … --run …` but `Command::MembraneSeal`
(crates/ufo-cli/src/main.rs:95-111) is a flat flag struct — no `write`
subcommand or positional exists in the clap surface. Clap 4.6.6 exits at
`Cli::parse` with "unexpected argument 'write'", so **every real
`authority_boundary` seal write fails `membrane_seal_write_failed`**: the
verdict stays durable, no seal lands, and the next fresh dispatch refuses
`membrane_seal_standing` until an operator signs or removes. Verified with
a minimal clap 4.6 repro (unexpected argument 'write' found).

Why it survived since the H13 cutover (d76ddcc0e): stub symmetry — the
JS tests pin the `write` argv against a fake runtime
(tests/run-omp-native-trial.test.js:3939, :4104) while the Rust contract
test omits `write` from its argv (cli_contract.rs:1514). No test runs the
real binary against the launcher's argv shape. Candidate fixes: drop the
`write` token from the launcher argv, or add a `MembraneSealAction::Write`
subcommand in ufo-cli.

Also documented (already known upstream, now in-playbook): the wall
handoff does not exit the outer launcher process — main() continues
in-process and the O_EXCL dispatch snapshot arbitrates the double-launch
race (tests pin it as "a source defect under its own report",
run-omp-native-trial.test.js:4404).

## Method

Two read-only scouts on disjoint slices (launcher spine ~15min; dispatcher
front ~8min); parent spot-verified every risky claim against source,
including building a minimal clap binary to disprove a scout's charitable
"consumed as a subcommand token" gloss. Round-4 lesson held: split along
the file's own family boundary, verify rather than restate.

## Evidence

Origin repo `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`:
`scripts/run-omp-native-trial.mjs` :194-4693; `scripts/fleet-dispatcher.mjs`
L96, L114-150, L5310-5701, L5743-5924, L8937, L12086-12513, L12798,
L13187; `crates/ufo-cli/src/main.rs` :95-111, :232, :287-308;
`crates/ufo-core-runtime/src/loop_driver_publish.rs` :26-173;
`crates/ufo-cli/tests/cli_contract.rs` :1507-1530;
`tests/run-omp-native-trial.test.js` :3869-4258, :4404; clap 4.6.6
(Cargo.lock) + /tmp/clap-probe repro.

## Remaining gaps (README updated)

- `ufo-core-runtime` support families: `native_seats`,
  `native_admission_text`, `lane_overlay`, `lease`, `live`,
  `cost_ledger` internals, `l3_swarm`.
- the-tick ground-handler ops beyond `path_ping`.
- fleet-dispatcher settle/reconcile tail (recordDispatchResult verbs,
  auto-reap, manifest reconcile).
- `ufo-sighting-lib` internals beyond the native-trial chain.
