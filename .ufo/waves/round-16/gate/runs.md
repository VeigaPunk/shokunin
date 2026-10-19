# root-ledgers gate — round-16 runs (protocol lane)

Gate: `.ufo/gates/root-ledgers.py`, sha256
`90867e3158e57549eac590619100f40639a02cc28966acd0680994a5c5ec7557` (landing bytes; superseded
working digests this round: `b151c9dc…` as left by the first seat, `9d924c16…` after the fence
hardening). Pinned values:
`.ufo/gates/root-ledgers/expected.json`. All runs from the fleet-protocol worktree root
(working tree = restored ledgers before the round-16 commit). Exit map: 0 clean · 1 failed ·
2 could-not-evaluate · 64 usage.

Authoring note: the gate L2 (`R16Gate`) stopped on a provider rate limit with a duplicated
`GATE_DIR` assignment that pointed the data dir at `.ufo/gates/` (every mode exited 2,
`pinned_values_unreadable`; `mutate.sh` reported `mutants killed 0/7`, exit 1). L1 replaced it with
the single correct definition (`.ufo/gates/root-ledgers/`); the runs below follow that fix. The
broken state is itself a demonstration that both `--selftest` and `mutate.sh` fail closed.

Re-dispatch note: the seat was re-dispatched fresh (`R16GateRedo`) per the orchestrator route
note; it died at start on a second provider capacity limit (`turn_rate_limit_exceeded`) and changed
nothing. L1 then landed its one bounded hardening directly: headings and rows inside fenced code
blocks (``` / ~~~, CommonMark-style) no longer count (`mask_fences`), with fixture
`fenced-aggregator` and mutant `fence-tracking-disable`. The table reflects the hardened gate; the
frozen replays did not change (the real ledgers carry 0 fence lines at either pinned revision).

Critic response (`R16Critic`, findings 2 and 6): a duplicated registry heading now reads
`protocol_registry_duplicated` (fixture `registry-duplicated`, mutant `duplicate-check-disable`), and
live mode names what it measured — worktree path, `HEAD`, and how many root ledgers are dirty —
instead of `revision: null`.

| command | exit | stdout (abridged only where marked) |
|---|---|---|
| `python3 .ufo/gates/root-ledgers.py --json` | 0 | `{"exit": 0, "findings": [], "revision": "worktree /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-protocol @31baf5c dirty_ledgers=2", "verdict": "clean"}` (pre-commit run) |
| `python3 .ufo/gates/root-ledgers.py --rev 31baf5c` | 1 | `scorecard_header_lost` (line 1 `# kotoba-shokunin — Scorecard`), `log_header_lost` (line 1 `# kotoba-shokunin — Iteration Log`), `protocol_registry_lost`, `aggregator_section_lost`; `VERDICT failed` |
| `python3 .ufo/gates/root-ledgers.py --rev 12f2da5` | 0 | `VERDICT clean` |
| `python3 .ufo/gates/root-ledgers.py --frozen` | 0 | `frozen pre-incident (12f2da5): ok` · `frozen kotoba-clobber (31baf5c): ok` · `VERDICT clean` |
| `python3 .ufo/gates/root-ledgers.py --selftest` | 0 | 9 fixtures ok (aggregator-lost, clean, closure-row-lost, fenced-aggregator, kotoba-clobber, missing-log, registry-below-aggregator, registry-duplicated, registry-lost); `selftest 9/9` |
| `sh .ufo/waves/round-16/gate/mutate.sh` | 0 | 9 mutants (scorecard-header-flip, log-header-flip, registry-check-disable, aggregator-check-disable, ordering-flip, row-prefix-swap, header-pin-echo, fence-tracking-disable, duplicate-check-disable) each `killed (exit 1)`; `mutants killed 9/9` |
| frozen tamper: temp copy of `.ufo/gates`, `frozen[0].sha256["LOG.md"]` set to 64 zeros, `--root . --frozen` | 2 | `snapshot_tampered LOG.md -- frozen pre-incident: 12f2da5:LOG.md sha256 df559cd0… != pinned 0000…`; `VERDICT could-not-evaluate` |
| `python3 .ufo/gates/root-ledgers.py --root /nonexistent` | 2 | `missing_input SCORECARD.md`, `missing_input LOG.md`; `VERDICT could-not-evaluate` |
| `python3 .ufo/gates/root-ledgers.py --bogus` | 64 | argparse usage on stderr |

Residuals (not detected by design; named, not hidden): a ledger whose header and section
headings are fleet bytes while its body is foreign; LOG.md append-only is not checked here (a
prefix check vs a pinned revision would be the next move). The gate reads the working tree it
runs on; `--rev` names the revision.
