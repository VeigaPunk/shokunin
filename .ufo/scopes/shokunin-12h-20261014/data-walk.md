# Shokunin 12-hour program — preflight data walk

Observed start: 2026-10-14T23:13:34Z. Hard deadline: 2026-10-15T11:13:34Z. Final integration-only hour starts 2026-10-15T10:13:34Z. State: **dispatch blocked**, not saturation, budget exhaustion, or a failed craft round.

## Authorities and write membrane

Loaded `skill://ufo`, `skill://swarm`, the OMP shokunin binding, the canonical shokunin skill and protocol bundle, UFO `run-logic.md` invariants and WWKD stance, and the runtime repository contract. One L1 owns this program; swarm reports are advisory and are not native judge input. No pushes. External substrates and UFO source are read-only; invoking the requested runtime commands and opening its wall does not authorize source repair. Secret and session surfaces remain shape-only.

## Direct observations

- UFO checkout resolves at `/home/vgpnk/Projects/ufo-fsd-alpha`; `scripts/` and `config/` exist. Current runtime HEAD measured by `git rev-parse HEAD`: `964f443ee53df0ce06bd689af01f0dea031b01f9`.
- Initial fleet HEAD measured by `git rev-parse HEAD`: `98a386ed3061637f718cc98e6584f739bccdbfc0`. Initial `git status --short`: no staged or tracked modifications, 21 untracked entries belonging to prior work. They are outside this program's commit pathspec.
- `bash scripts/ufo-sighting open` succeeded: status attached, hatch open, tmux `ufo_sighting:1`, missionCount 0. It created no program L1 or L2 mission.
- Global OMP config declares `m_sol: openai-codex/gpt-6.1-sol:max`, `m_composer: xai-oauth/grok-composer-2.5-fast`, and `m_grok: xai-oauth/grok-4.7:xhigh`. Alias resolution is configuration evidence, not an authenticated completion probe.
- Current seat bindings: executor/connector/reviewer/revenger/sentinel -> `m_mid`; scout/scribe/mutation-tester/simplifier/distiller/labrat -> `m_fast`; critic/planner/main -> `m_strong`. None of those bindings implements the operator's composer-content/grok-audit split. No global route or per-dispatch model override was changed.
- `node scripts/sync-global-routing.mjs --check` exits 1: bundled `crates/ufo-core-runtime/bundled/omp-seat-routing.json` drifts from the global table.
- `cargo run -p ufo-cli -- routing-health` succeeds, with rows 0, routes {}, malformedRows 0. This is an empty historical ledger, **not provider readiness**.
- `node scripts/sync-ufo-contracts.mjs --check` exits 1: 18 missing generated targets, six dependency-closure omissions, sighting-surface digest drift, and 74 route-equivalence mismatches. Full observed output is retained separately.
- Actual `bash scripts/self-iter.sh --task 'UFO-FSD smoke' --rounds 2 --concurrency 6` exits 2: `BLOCKED: phase-0 UFO-FSD contract gate failed`, `allContractsReady: false`. It supplied no successful smoke, native handoff, or kumitate verdict.
- Live `config/ufo.json` has swarm wave band 16–32, member cap 100, nightcall L1 alias `m_strong`, defaultIterateRounds 1024. The prompt's eight-round default is not the live value; the program must impose its own finite phase/deadline bounds without changing runtime config.
- `bash -n shokunin.conf` exits 2 at line 58: the quoted `LANES` value closes after revenger, leaving tameshi/mado/tsukuroi/tabi as invalid shell text. This fleet-local prerequisite is repairable without changing any roster member or launching the watchdog.
- `MANIFEST.json` currently has 135 round entries and 13 roster rows. The four newer local lanes are recorded in mint/probation entries, not roster rows; that is not authority to promote them.
- Canonical mint templates exist at `/home/vgpnk/Projects/kimi-shokunin/templates/mint/`; the skill-relative `skills/shokunin/templates/` path is absent. Tameshi's repository is the operator-approved seed shape, not a reason to copy its asserted promotion marks.
- Secondary definition inventory is readable and lists 18 filenames across fast/mid/strong buckets. No credential values or session payloads were read.
- Existing research surfaces: `research/deep-research-2026-09-28/A-shokunin-tradition.md`, `B-multiagent-knowledge.md`, and `C-rank-taxonomy.md`. No external fetch was made.

## Re-census evidence to inherit, not blindly overwrite

Kumitate `SCORECARD.md` rounds 18–31 distinguish stale defaults from genuine upstream membership drift. Preserve the `$UFO_SRC` -> first existing new/old checkout -> fail-closed derivation; describe superseded content hashes rather than pinning them as current; carry DRIFT only with named debt. Kake's current scorecard already records round-18 historical migration annotations and three correct remaining red-gate debts. The Phase 1 wave must inventory current state, not assume every requested repair is still missing.

## Consequence

No worker dispatch, craft-round admission, mint, lane identity commit, native judged round, or mission-completion receipt has occurred. The fallback wave remains blocked by the requested seat split even if the native Phase 0 failure selects fallback. Do not call the present state convergence.
