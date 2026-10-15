# S5MemberRecensus — round-32 script-layer re-census (advisory)

**Seat:** S5MemberRecensus (leaf). **Family:** S5 — routing & result helpers.
**Lane:** kumitate-shokunin @ dispatch HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`.
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`.
**Not a verdict.** Parent owns registry row, stanza, re-pin, gates, commit.

## Axes this move touches

- `coverage:script-layer` honesty term: S5 was topic-form (`sections=0`,
  `ROW_NO_SECTIONS`); after this note edit it is section-form with
  **2 in-family member sections** (gate-verified).
- Operability / calibration: notes now carry live anchors against the
  restructured origin tree (627 / 2966 L), not the frozen 735 / 3691 L cell.

## Files inspected

| path | role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row S5; round-32 `## Planned` |
| `kumitate-shokunin/corpus/README.md` | coverage-map stems for the three notes |
| `kumitate-shokunin/corpus/knowledge/route-resolution.md` | S5 note (edited) |
| `kumitate-shokunin/corpus/knowledge/failure-telemetry.md` | S5 note (edited) |
| `kumitate-shokunin/corpus/knowledge/singleton-and-queue-ownership.md` | S5 note (edited) |
| `kumitate-shokunin/scripts/claims-check.mjs` | section-form rules (read) |
| `ufo-fsd-alpha/scripts/omp-global-config.mjs` | live member |
| `ufo-fsd-alpha/scripts/ufo-mission-result.mjs` | live member |

## Live membership (origin tree) — command + observed output

**Command (exact):**

```bash
ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
git -C "$ORIGIN" rev-parse HEAD
# → 964f443ee53df0ce06bd689af01f0dea031b01f9

ls -la "$ORIGIN/scripts/omp-global-config.mjs" "$ORIGIN/scripts/ufo-mission-result.mjs"
wc -l "$ORIGIN/scripts/omp-global-config.mjs" "$ORIGIN/scripts/ufo-mission-result.mjs"
sha256sum "$ORIGIN/scripts/omp-global-config.mjs" "$ORIGIN/scripts/ufo-mission-result.mjs"

# presence-only pair walk (registry-declared basenames only; no family widen)
for f in omp-global-config.mjs ufo-mission-result.mjs; do
  p="$ORIGIN/scripts/$f"
  if [ -f "$p" ]; then printf 'PRESENT scripts/%s %sL\n' "$f" "$(wc -l < "$p")"
  else printf 'ABSENT scripts/%s\n' "$f"; fi
done
```

**Observed:**

```
PRESENT scripts/omp-global-config.mjs 627L
PRESENT scripts/ufo-mission-result.mjs 2966L
sha256 omp-global-config.mjs  71668acae663eaf1b2692960cec436b80db4d68735ad00614549459ab4325ae3
sha256 ufo-mission-result.mjs bf23cf3ee51702a74bc492049a0f613d79d838a1cec55579508da1c214755551
```

No other `*omp-global*` / `*mission-result*` basenames under `scripts/`.
Related but **out of family** (not invented into S5): `ufo-mission-activity.mjs`,
`ufo-mission-lifecycle.mjs`, `ufo-mission-observation.mjs` (+ tests).

### Exact member list (derived)

1. `scripts/omp-global-config.mjs` (627 L)
2. `scripts/ufo-mission-result.mjs` (2966 L)

**Declared count the registry row must carry:** **2** (same two basenames;
line counts in the cell are stale — 735/3691 → 627/2966). Parent owns the
cell rewrite. Suggested cell shape (data only, not applied here):

`2 members: \`omp-global-config.mjs\` (627 L) + \`ufo-mission-result.mjs\` (2966 L)`

or keep the `A + B` form with updated sizes. Adding the explicit `2 members`
prefix enables the gate's `MEMBER_COUNT_DRIFT` integer arm; without it the
row still section-matches on distinct path-form headings.

## Registry row S5 (read-only compare)

```
| S5 | routing & result helpers | `omp-global-config.mjs` (735 L) + `ufo-mission-result.mjs` (3691 L) | yes — route-resolution · failure-telemetry · singleton-and-queue-ownership |
```

| claim | live |
|---|---|
| both basenames present | **yes** |
| line counts 735 / 3691 | **no** — 627 / 2966 |
| note stems resolve | **yes** — 3 notes under `corpus/knowledge/` |
| covered `yes` | kept; parent decides cell text |

## Family notes — sections added / removed

### Before (gate)

```
node scripts/claims-check.mjs --row S5 --src /home/vgpnk/Projects/ufo-fsd-alpha
→ ROWS: 1  YES: 1  NOTES: 3  SECTIONS: 0
→ form=topic  adv=1  ROW_NO_SECTIONS
→ CLAIMS: MATCH (… sections=0 adv=1) exit 0
```

Topic headings only (`## Mechanism…`, `## Entry failure classes…`,
`## acquireSingletonLock`, …) — none path-form, so zero gated member sections.

### After (gate)

```
node scripts/claims-check.mjs --row S5 --src /home/vgpnk/Projects/ufo-fsd-alpha --strict
→ ROWS: 1  YES: 1  NOTES: 3  SECTIONS: 2
→ form=section  adv=0
→ CLAIMS: MATCH (rows=1 yes=1 notes=3 sections=2 adv=0) exit 0
```

JSON sections (abridged):

| note | heading | file | anchors live | inFamily |
|---|---|---|---|---|
| `route-resolution.md` | `scripts/omp-global-config.mjs` | `scripts/omp-global-config.mjs` | 14 / true | true |
| `failure-telemetry.md` | `scripts/ufo-mission-result.mjs` | `scripts/ufo-mission-result.mjs` | 22 / true | true |

### Sections **added**

| note | heading |
|---|---|
| `corpus/knowledge/route-resolution.md` | `## \`scripts/omp-global-config.mjs\`` |
| `corpus/knowledge/failure-telemetry.md` | `## \`scripts/ufo-mission-result.mjs\`` |

Each carries ≥1 own-file pathish anchor and ≥1 backticked symbol verbatim in
that member (gate `symbolHit: true`, `live: true`).

### Sections **removed**

**None.** Neither declared member is absent from the live tree; there was no
path-form phantom `## \`scripts/<gone>\`` to delete.

### Non-section repairs (recorded)

| note | change |
|---|---|
| `singleton-and-queue-ownership.md` | **No** second path-form `##` (avoids occurrence double-count). Dead prose anchor `~L1716` → live `scripts/ufo-mission-result.mjs:1308`. Topic headings retained. |
| `failure-telemetry.md` | Dropped in-member claims for `CAPACITY_FAILURES`, `ROUTING_HEALTH_OUTCOMES`, `DEADLINE_CLASS_BY_ROLE`, `SEAT_CLASS_BY_ROLE` — first two live under S2 `collect-omp-native-handoff-lib/base.mjs`; last two **rg-empty** in `ufo-mission-result.mjs`. |
| both size notes | Documented 735→627 and 3691→2966 for parent cell update. |

## Files changed (this seat)

1. `kumitate-shokunin/corpus/knowledge/route-resolution.md` — added S5 member section + live anchors.
2. `kumitate-shokunin/corpus/knowledge/failure-telemetry.md` — added S5 member section + live anchors; relocated capacity/routing-health attribution.
3. `kumitate-shokunin/corpus/knowledge/singleton-and-queue-ownership.md` — anchor repair; no path-form section (by design).
4. This advisory: `.ufo/waves/shokunin12h-20261014-p2-kumitate/members/S5MemberRecensus.md`.

**Not edited (parent-owned):** `SCORECARD.md` registry row S5, `kumitate-proxy-v1` stanza, pins, `corpus/README.md` map row.

## Contribution to layer arithmetic (for parent)

- Pre: S5 `S_sections` contribution **0** (topic-form).
- Post: S5 contribution **2** in-family sections (gate `sections=2`, both
  `inFamily: true`).
- Parent still must re-sum full-layer `S_sections` / `S_members` after all
  family seats land; this seat does not claim the layer score.

## Cross-domain findings (owner ≠ this seat)

| finding | owner |
|---|---|
| `CAPACITY_FAILURES` / `ROUTING_HEALTH_OUTCOMES` live in `scripts/collect-omp-native-handoff-lib/base.mjs`, not S5 | **S2** native-trial / handoff family |
| `DEADLINE_CLASS_BY_ROLE` / `SEAT_CLASS_BY_ROLE` deleted from `ufo-mission-result.mjs` | origin tree / whoever owned the shrink; do not re-home into S5 without a live symbol |
| Registry line counts 735/3691 stale vs 627/2966 | parent (registry cell) |
| Layer `S_members` 114→91 (tree-wide) | parent / full re-census — S5 pair unchanged in membership |

## Unresolved blockers

**None for S5.** Both members exist; both notes now carry honest path-form
sections; `--strict` claims gate MATCH on `--row S5`.

## Limits

- Did not re-run full-repo `claims-check` / `proxy-check` (parent gate wave).
- Did not edit registry or stanza.
- Did not widen S5 to mission-activity/lifecycle/observation helpers.
- Live global alias table block in `route-resolution.md` remains the
  2026-09-28 observation (not re-probed this seat — config is operator host
  state, shape-only).
