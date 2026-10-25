# S8MemberRecensus — round-32 script-layer family S8

Advisory only. Not a verdict. Parent integrates registry row + stanza.

## Files inspected

- `kumitate-shokunin/SCORECARD.md` (registry row S8; `## Planned` round-32)
- `kumitate-shokunin/corpus/README.md` (map row → `knowledge/remaining-scripts-census.md`)
- `kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md` (family note; edited)
- `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` (layer term shape)
- Origin tree `/home/vgpnk/Projects/ufo-fsd-alpha` at `964f443ee53df0ce06bd689af01f0dea031b01f9`

## Exact commands + observed output

### Layer walk (S_members)

```bash
SRC=/home/vgpnk/Projects/ufo-fsd-alpha
ls -1 "$SRC"/scripts/*.mjs | wc -l
# 73
find "$SRC/scripts" -mindepth 2 -type f | wc -l
# 18
{
  ls -1 "$SRC"/scripts/*.mjs
  find "$SRC/scripts" -mindepth 2 -type f
} | sed "s|^$SRC/||" | LC_ALL=C sort -u | wc -l
# 91
git -C "$SRC" rev-parse HEAD
# 964f443ee53df0ce06bd689af01f0dea031b01f9
```

### Live S1–S7 intersection (for S8 subtraction)

Historical family shapes filtered to files that still exist. Live S1–S7 count **28**:

```
scripts/collect-omp-native-handoff-lib/base.mjs
scripts/collect-omp-native-handoff-lib/events.mjs
scripts/collect-omp-native-handoff-lib/evidence.mjs
scripts/collect-omp-native-handoff-lib/policy.mjs
scripts/collect-omp-native-handoff-lib/screening.mjs
scripts/collect-omp-native-handoff.mjs
scripts/fake-omp.mjs
scripts/fleet-dispatcher.mjs
scripts/omp-global-config.mjs
scripts/probe-redact.mjs
scripts/probe-token-plan-kimi.mjs
scripts/probe-token-plan-models.mjs
scripts/probe-token-plan-shared.mjs
scripts/probe-ufo-route-health.mjs
scripts/run-omp-native-trial.mjs
scripts/the-tick-ping.mjs
scripts/ufo-ground-handler.mjs
scripts/ufo-l0-monitor.mjs
scripts/ufo-l0-watch.mjs
scripts/ufo-mission-result.mjs
scripts/ufo-sighting-lib/argv.mjs
scripts/ufo-sighting-lib/base.mjs
scripts/ufo-sighting-lib/observe.mjs
scripts/ufo-sighting-lib/surface.mjs
scripts/ufo-sighting.mjs
scripts/ufo-stale-watchdog.mjs
scripts/ufo-swarm-collect.mjs
scripts/ufo-swarm-wave.mjs
```

S7 historical companions **gone** from tree (owned by S7 re-census, not S8):
`scripts/atomic-write.mjs`, `scripts/probe-redact.test.mjs`,
`scripts/probe-ufo-route-health.test.mjs`.

### S8 derivation

```bash
comm -23 /tmp/s8-all-scripts.txt <(LC_ALL=C sort /tmp/s8-s1s7-live.txt) > /tmp/s8-members-live.txt
wc -l < /tmp/s8-members-live.txt
# 63
wc -l $(cat /tmp/s8-members-live.txt | sed "s|^|$SRC/|") | tail -1
# 36827 total
```

`LC_ALL=C sort` on both `comm` sides.

### Registry / note before edit

- Registry row S8 (SCORECARD): **60 members** claimed; note
  `knowledge/remaining-scripts-census.md`.
- Note heading set: **60** `## \`scripts/…\`` sections.
- `comm -3` note vs live (both `LC_ALL=C sort`):
  - **note-only (15 phantoms):** see removals below
  - **live-only (18 new):** see additions below
  - **common:** 45

## Exact live S8 member list (63)

```
scripts/charter-scribe/config.json
scripts/charter-scribe/prompts/kimi-update.prompt.txt
scripts/charter-scribe/sync.mjs
scripts/charter-scribe/systemd/charter-scribe.service
scripts/charter-scribe/systemd/charter-scribe.timer
scripts/check-hand-authored-sets.mjs
scripts/check-hand-authored-sets.test.mjs
scripts/check-routing-free-config.mjs
scripts/check-routing-free-config.test.mjs
scripts/fleet-dispatcher.test.mjs
scripts/fleet-ledger-read.mjs
scripts/fleet-ledger-read.test.mjs
scripts/fleet-ledger-rotate.mjs
scripts/fleet-ledger-rotate.test.mjs
scripts/fleet-selfheal-verify.mjs
scripts/gates-plan.mjs
scripts/land-fleet-run.mjs
scripts/lean-cargo/README.md
scripts/lean-cargo/bin/cargo-shim.sh
scripts/lean-cargo/install-shim.sh
scripts/lean-cargo/measure.sh
scripts/local-helper.mjs
scripts/omp-native-shutdown.mjs
scripts/omp-role-work.mjs
scripts/omp-wave-context.mjs
scripts/prepare-ephemeral-fleet.mjs
scripts/prepare-ephemeral-fleet.test.mjs
scripts/prepare-ephemeral-l1.mjs
scripts/primeagent-recovery-assess.mjs
scripts/primeagent-refinement-ledger.mjs
scripts/project-devin-subagents.mjs
scripts/render-seat-tables.mjs
scripts/render-seat-tables.test.mjs
scripts/sync-global-routing.mjs
scripts/sync-ufo-contracts.mjs
scripts/the-tick-config.mjs
scripts/ufo-credential-screen.mjs
scripts/ufo-drills.mjs
scripts/ufo-godspeed-inject.test.mjs
scripts/ufo-l0-monitor-hook.test.mjs
scripts/ufo-l0-monitor.test.mjs
scripts/ufo-l0-watch.test.mjs
scripts/ufo-mission-activity.mjs
scripts/ufo-mission-activity.test.mjs
scripts/ufo-mission-lifecycle.mjs
scripts/ufo-mission-observation.mjs
scripts/ufo-mission-observation.test.mjs
scripts/ufo-native-names.mjs
scripts/ufo-night-watchdog.test.mjs
scripts/ufo-refinement-context.mjs
scripts/ufo-refinement-context.test.mjs
scripts/ufo-route-preflight.mjs
scripts/ufo-route-preflight.test.mjs
scripts/ufo-stale-watchdog.test.mjs
scripts/ufo-state-census.mjs
scripts/ufo-state-census.test.mjs
scripts/ufo-state-retention.mjs
scripts/ufo-state-retention.test.mjs
scripts/ufo-statusline-hook.test.mjs
scripts/ufo-swarm-collect.test.mjs
scripts/ufo-swarm-wave.test.mjs
scripts/ufo-watchdog-repend.mjs
scripts/ufo-watchdog-repend.test.mjs
```

Class shape: **23 suites + 32 tools + 3 shims + 4 assets + 1 doc = 63**;
54 top-level `scripts/*.mjs` + 9 under `charter-scribe/`/`lean-cargo/`.
`wc -l` total **36827**.

## Sections removed (15)

Recorded in note `## Limits` (round-32 bullet). Files absent from live tree:

1. `scripts/charter-scribe/sync.test.mjs`
2. `scripts/local-helper.test.mjs`
3. `scripts/omp-global-config.test.mjs`
4. `scripts/omp-role-work.test.mjs`
5. `scripts/prepare-ephemeral-l1.test.mjs`
6. `scripts/primeagent-refinement-ledger.test.mjs`
7. `scripts/project-devin-subagents.test.mjs`
8. `scripts/run-omp-native-trial.test.mjs`
9. `scripts/sync-global-routing.test.mjs`
10. `scripts/ufo-drills.test.mjs`
11. `scripts/ufo-ground-handler.test.mjs`
12. `scripts/ufo-mission-lifecycle.test.mjs`
13. `scripts/ufo-mission-result.test.mjs`
14. `scripts/ufo-statusline-gate.test.mjs`
15. `scripts/ufo-statusline-hook-machinery.test.mjs`

## Sections added (18)

Each with ≥1 own-file live anchor and ≥1 backticked symbol verbatim in the member:

1. `scripts/check-hand-authored-sets.mjs` — `DECLARED_PRE_HOOKS` `:35`, `enumerateSets` `:82`
2. `scripts/check-hand-authored-sets.test.mjs` — `DECLARED_PRE_HOOKS` `:14`, `checkHandAuthoredSets`
3. `scripts/check-routing-free-config.mjs` — `ROUTING_KEYS` `:20`, `checkRoutingFreeConfig` `:87`
4. `scripts/check-routing-free-config.test.mjs` — `checkRoutingFreeConfig` `:12`, `scanText`
5. `scripts/land-fleet-run.mjs` — `LandingError` `:32`, `landFleetRun` `:50`
6. `scripts/omp-wave-context.mjs` — `WaveContextError`, `WAVE_CONTEXT_MARKER` `:59`
7. `scripts/prepare-ephemeral-fleet.mjs` — `readFleetPolicy` `:84`, `composeEphemeralFleet`
8. `scripts/prepare-ephemeral-fleet.test.mjs` — `composeEphemeralFleet`, `landFleetRun`
9. `scripts/render-seat-tables.mjs` — `TARGETS` `:26`, `seatsDigest` `:38`
10. `scripts/render-seat-tables.test.mjs` — `renderSeatTables`, `seatsDigest`
11. `scripts/ufo-godspeed-inject.test.mjs` — `loadHandler` `:33`, `DIRECTIVE` `:52`
12. `scripts/ufo-night-watchdog.test.mjs` — `hasTmux` `:90`
13. `scripts/ufo-refinement-context.mjs` — `REFINEMENT_CONTEXT_SCHEMA` `:24`, `buildRefinementContext` `:47`
14. `scripts/ufo-refinement-context.test.mjs` — `buildRefinementContext`, `REFINEMENT_BEGIN`
15. `scripts/ufo-route-preflight.mjs` — `ROUTE_PREFLIGHT_SCHEMA` `:32`, `routeFamilies` `:54`
16. `scripts/ufo-route-preflight.test.mjs` — `routeFamilies`, `probeFamilies`
17. `scripts/ufo-state-census.mjs` — `CENSUS_SCHEMA` `:22`, `censusState` `:28`
18. `scripts/ufo-state-census.test.mjs` — `censusState`, `sparse`

Retained 45 prior sections kept; each still had ≥1 live own-file anchor against
current file lengths (many secondary anchors are stale after upstream shrinks;
gate needs only one live own-file anchor).

Post-edit: `comm -3` of note headings vs live members → **empty**; heading count **63**.

## Declared count the S8 registry row must carry

**63**

(Parent owns editing the SCORECARD registry cell and the `kumitate-proxy-v1`
stanza. This member did not touch either.)

## Note edits performed

Path: `kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md`

- Title/membership/composition prose: 60 → **63**; measurement recipe pointed at
  live origin path + HEAD; census table rebuilt from live `wc -l`.
- Removed 15 phantom `##` sections; added 18 new `##` sections.
- `## Limits`: recorded removals + additions + declared-count **63**.
- Did **not** edit `corpus/README.md` map row wording (still says “60 of 60”);
  parent may refresh map prose when integrating.

## Unresolved blockers

None for S8 note honesty against the live member set.

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| S7 live membership is **6**, not 9 (`atomic-write.mjs` + two `probe-*.test.mjs` gone). S8 subtraction used live S7 only. | S7MemberRecensus / parent |
| S2 lib is **5** files (was 6; `refusal-line.mjs` gone per Planned). | S2MemberRecensus |
| S4 `ufo-sighting-lib/` is **4** files (was 26). | S4MemberRecensus |
| Layer `S_members=91` vs frozen stanza `114` — DRIFT is correct; parent re-pins. | parent / StanzaDerivation |
| Five top-level `.sh` still outside frozen universe (unchanged definitional limit). | parent (registry policy) |
| `corpus/README.md` S8 map blurb still says “60 of 60”. | parent (map prose) |

## Arithmetic check (informational)

`91 (S_members) = 28 (S1–S7 live) + 63 (S8)` ✓
