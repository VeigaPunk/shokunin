# R4MemberRecensus — runtime support (R4)

Lane: `kumitate-shokunin` @ `175de6ba`. Origin: `ufo-fsd-alpha` @ `964f443e`.
Wave: `shokunin12h-20261014-p2-kumitate` round-32 re-census. **Unjudged** — no verdict.

Family: **R4 — runtime support**. Note: `corpus/knowledge/runtime-support.md`.
Registry cell (SCORECARD / `corpus/README.md` map): `yes — runtime-support`; members cell currently `6 files (\`lane_overlay*\`, \`lease*\`, \`live*\`)`.

Parent owns the registry row and the `kumitate-proxy-v1` stanza. This report is data only.

---

## 1. Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | R4 row; `### coverage:runtime-layer`; `## Planned` round-32 |
| `kumitate-shokunin/corpus/README.md` | map row → `knowledge/runtime-support.md` |
| `kumitate-shokunin/corpus/knowledge/runtime-support.md` | R4 note (3 member `##` sections + `## Traps`) |
| `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` | (named in contract; not re-derived here) |
| `kumitate-shokunin/scripts/claims-check.mjs` | section/anchor/MEMBER_COUNT rules; `--row R4` run |
| `kumitate-shokunin/scripts/proxy-check.mjs` | frozen derivation reference only |
| Origin `crates/ufo-core-runtime/src/{lane_overlay,lease,live}*.rs` (6) | live membership + anchors |
| Origin git `5725fa7d3..HEAD` delete log for R4 globs | deletion filter |

Not edited: note, registry, stanza, origin tree. Output path only this file.

---

## 2. Exact commands + observed output

### 2.1 Live R4 membership (authoritative enumeration)

```
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/{lane_overlay,lease,live}*.rs \
    | xargs -n1 basename | LC_ALL=C sort
lane_overlay.rs
lane_overlay_tests.rs
lease.rs
lease_tests.rs
live.rs
live_tests.rs

$ ls -1 …/{lane_overlay,lease,live}*.rs | wc -l
6
```

Line counts at origin HEAD `964f443e`:

```
$ wc -l crates/ufo-core-runtime/src/{lane_overlay,lease,live}*.rs
  306  lane_overlay.rs
  343  lane_overlay_tests.rs
  618  lease.rs
  648  lease_tests.rs
  441  live.rs
  530  live_tests.rs
```

`#[test]` heads (`grep -c '^[[:space:]]*#\[test\]'`):

| file | tests |
|---|---|
| `lane_overlay_tests.rs` | 16 |
| `lease_tests.rs` | 18 |
| `live_tests.rs` | 27 |
| production trio | 0 each |

### 2.2 Deletion filter since `5725fa7d3`

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha log --diff-filter=D --name-only --pretty=format: \
    5725fa7d3..HEAD -- \
    'crates/ufo-core-runtime/src/lane_overlay*' \
    'crates/ufo-core-runtime/src/lease*' \
    'crates/ufo-core-runtime/src/live*' \
  | sed '/^$/d' | LC_ALL=C sort -u
(empty)
```

Tree listing at `5725fa7d3` and at `HEAD` for the same globs is **identical** (six paths). **No R4 member was deleted.** Nothing to remove from the note on deletion grounds.

### 2.3 Layer context (dispatch pins; not re-scored here)

```
$ ls -1 …/crates/ufo-core-runtime/src/*.rs | wc -l   → 88
$ ls -1 …/crates/ufo-cli/src/*.rs | wc -l            → 4
⇒ R_members live = 92 (stanza still claims 98 — parent re-pins)
```

R4 contributes **6 / 92** of the live runtime+CLI universe under the cell's glob family. CLI has **zero** R4-pattern files.

### 2.4 Note section inventory vs live (locale-safe)

```
$ grep -E '^## `' corpus/knowledge/runtime-support.md \
    | sed -E 's/^## `([^`]+)`.*/\1/' | xargs -n1 basename | LC_ALL=C sort
lane_overlay.rs
lease.rs
live.rs

$ comm -3 <(live list LC_ALL=C sort) <(note headings LC_ALL=C sort)
lane_overlay_tests.rs
lease_tests.rs
live_tests.rs
```

Only the three `*_tests.rs` members appear on the live-only side. Note-only side empty. `## Traps` is non-member (no path-like first backtick) — correctly ignored by `claims-check`.

### 2.5 Claims gate (measured, not a verdict)

```
$ node scripts/claims-check.mjs --row R4 --src /home/vgpnk/Projects/ufo-fsd-alpha
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 3
ROW R4   form=section   notes=1 sections=3 adv=1
CLAIMS  warn  MEMBER_COUNT_SUSPECT     row=R4  declared 6, found 3 distinct sections
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=3 adv=1)
```

Matches SCORECARD's in-family sum fragment `R4 3`. The cell already declares **6 files**; the honesty gap is **missing test-companion sections**, not a wrong declared integer.

### 2.6 Existing production-section own-file anchor spot-check

Re-derived against origin bytes (gate rule: range endpoints non-empty):

| section | own-file anchors | status |
|---|---|---|
| `lane_overlay.rs` | `:98-177`, `:180-196`, `:50-95` LIVE; `:198-241` **DEAD_EMPTY** (start line blank after drift) | ≥1 live → section still passes; repair recommended |
| `lease.rs` | `:379-490`, `:516-560` LIVE | ok |
| `live.rs` | bare `:29`, `:38`, `:42`, `:45` LIVE; bare `:236-242` LIVE but now points at `impl PrivateTempFile` (prose still says `LiveDispatchResult`); bare `:441-445` **DEAD OOB** (file is 441 L) | ≥1 live → passes; prose/anchor drift |

Heading line-count claims are stale: note says 262 / 842 / 484 L; live is **306 / 618 / 441** L. Parent/scribe may refresh headings when landing the three new sections.

---

## 3. Derived member list (exact)

**Live R4 members (declared count the row must carry: `6`):**

1. `lane_overlay.rs`
2. `lane_overlay_tests.rs`
3. `lease.rs`
4. `lease_tests.rs`
5. `live.rs`
6. `live_tests.rs`

**Pattern remains** `` `lane_overlay*`, `lease*`, `live*` `` — still exact for the live set; no glob widening/narrowing required.

**Registry cell text (suggestion for parent; parent owns the edit):** keep

`6 files (\`lane_overlay*\`, \`lease*\`, \`live*\`)`

or expand to the explicit six basenames. Integer **must stay 6**. Do **not** drop to 3 to match today's sections — that would freeze the honesty hole.

---

## 4. Sections added / removed

### Removed

**None.** No deleted R4 files since `5725fa7d3`; no phantom member headings in the note.

### Added (required for honest `yes` at 6/6 — parent integrates into `runtime-support.md`)

Three new `## \`<member>.rs\`` sections. Drafts below use **own-file anchors that resolve live** at `964f443e` and **backticked symbols verbatim** in those files. Place them after the matching production section (or after `live.rs` before `## Traps`).

#### Draft — `lane_overlay_tests.rs`

```markdown
## `lane_overlay_tests.rs` (343 L) — overlay loader + global-home pin suite

Companion pin file for `lane_overlay.rs` (`grep -c '^[[:space:]]*#\[test\]'` → **16**).

- Canonical omitted-field policy: `omitted_overlay_routes_follow_canonical_local_policy` (`lane_overlay_tests.rs:5`) asserts distiller → `hvm/qwen-hvm` cap 1 and others → `local/fixture-primary` cap 8 via `load_overlays_from_dir`.
- Refusal pins: `overlay_refuses_unimplemented_route` (:29), `overlay_refuses_zero_parallel_cap_and_empty_role` (:40), `overlay_refuses_excessive_directory_entries` (:59), `overlay_refuses_excessive_lane_count` (:79) — all expect `load_overlays_from_dir(…).is_err()`.
- Roster const pin: `default_routes_pin_roster_fixture_consts` (:217) binds `default_route_for_role` to the live fixture/Qwen route consts.
- Inheritance: `whitespace_only_overlay_route_inherits_role_default` (:236).
- Global layer order: `global_candidates_resolve_in_documented_precedence_order` (:256).
```

#### Draft — `lease_tests.rs`

```markdown
## `lease_tests.rs` (648 L) — writer-lease fencing pin suite

Companion pin file for `lease.rs` (`grep -c '^[[:space:]]*#\[test\]'` → **18**). Helpers: `dead_pid` / `plant_lease` above the first `#[test]`.

- Live second holder: `lease_second_live_holder_is_refused` (`lease_tests.rs:27`) matches `LeaseError::HeldBy` at epoch 1.
- Epoch fence + same-epoch foreign holder: `lease_stale_epoch_write_is_rejected` (:46) — `guarded_write` → `GuardedWriteError::Lease(LeaseError::StaleEpoch { current: 2 })`, then foreign holder → `HeldBy`.
- Capability / takeover: `guarded_write_refuses_a_foreign_process_capability` (:91), `lease_takeover_after_holder_death` (:130), `lease_foreign_namespace_holder_is_refused_even_when_pid_is_dead` (:147).
- Single-winner: `lease_concurrent_takeover_never_double_wins_an_epoch` (:171).
- Malformed store: `lease_malformed_file_is_a_typed_error` (:219) — present-but-bad is evidence, never overwritten.
```

#### Draft — `live_tests.rs`

```markdown
## `live_tests.rs` (530 L) — live Qwen dispatch / authorization pin suite

Companion pin file for `live.rs` (`grep -c '^[[:space:]]*#\[test\]'` → **27**).

- Enablement: `local_synthesis_ignores_unrelated_ambient_auth` (`live_tests.rs:7`) vs `local_synthesis_honors_explicit_dispatch_flag` (:17) — ambient `CURSOR_*` must not enable; `UFO_LIVE_DISPATCH=1` must.
- Timeouts: `live_dispatch_timeout_defaults_closed` (:25); `qwen_deadline_bounds_control_and_http_inside_outer_budget` (:36) pins inner deadlines inside the outer budget (default outer **330**).
- Fail-closed HOME: `qwen_distiller_refuses_to_guess_home` (:73) — unset `HOME` refuses rather than guessing a host path.
- Authorization matrix: `direct_transport_handler_authorizes_live_synthesis` (:353); refusals `local_collapse_marker_cannot_authorize_live_synthesis` (:382), `nonzero_exit_leftover_cannot_authorize_live_synthesis` (:394).
- Wire grammar: `route_and_sentinel_consts_match_wire_grammar` (:525) locks `QWEN_LIVE_ROUTE` / fixture routes / `LOCAL_COLLAPSE_SENTINEL`.
```

### Section delta summary

| action | member | reason |
|---|---|---|
| keep | `lane_overlay.rs`, `lease.rs`, `live.rs` | live; already sectioned |
| **add** | `lane_overlay_tests.rs`, `lease_tests.rs`, `live_tests.rs` | live members; zero note sections today |
| remove | — | no deletions |

After parent lands the three drafts (and only then): expected `claims-check --row R4` shape is `sections=6`, `adv=0` on the `MEMBER_COUNT_SUSPECT` arm (other advisories depend on optional dead-anchor cleanup). That moves this row's contribution to `R_sections` from **3 → 6** (**+3**), which the parent folds into the layer re-derive.

---

## 5. Declared count the row must carry

**`6`**

Evidence: live enumeration count 6; empty delete log since `5725fa7d3`; cell already says `6 files`; gate `MEMBER_COUNT_SUSPECT` is sections-behind-declaration, not declaration-behind-tree.

---

## 6. Unresolved blockers

- **None for membership.** The six files exist; drafts above have live anchors at `964f443e`.
- **Integration not performed here** (contract: parent owns note/row/stanza). Until the three sections land, `--row R4` continues to warn `MEMBER_COUNT_SUSPECT`.
- **Optional note hygiene** (not blockers, not counted as section add/remove): refresh production heading line counts; retarget `lane_overlay.rs:198-241`, `live.rs` bare `:236-242` / `:441-445`, and the `LiveDispatchResult` prose if the parent wants zero dead own-file anchors.

---

## 7. Cross-domain findings (owner)

| finding | owner |
|---|---|
| Live `R_members` 92 vs stanza 98; live `S_members` 91 vs 114 (dispatch-measured) | parent / full-layer recensus (other family members) |
| SCORECARD in-family sum still prices `R4` as **3** | parent after note sectionization |
| `membrane-seal write` argv defect | filed; stays out of province (not R4) |
| Origin line-drift inside existing R4 production sections | kumitate note owner (parent/scribe), origin unchanged |

No foreign-repo edit requested or made.

---

## 8. Calibration notes (axes named; no score claimed)

- **coverage:** R4 is the smallest honesty gap among glob families that already declare their full file count — +3 sections closes `MEMBER_COUNT_SUSPECT` without inventing members.
- **operability:** `claims-check.mjs --row R4` is the re-runnable probe used above; exit path observed green with one warn.
- **calibration:** note pin rev still says `ee907f1cf`; origin HEAD is `964f443e`. Membership set unchanged across that window; body anchors partially drifted.

---

## 9. One-line hand-off

**R4 live members = 6** (`lane_overlay.rs`, `lane_overlay_tests.rs`, `lease.rs`, `lease_tests.rs`, `live.rs`, `live_tests.rs`); **sections to add = 3** (the `*_tests.rs` trio); **sections to remove = 0**; **declared count = 6**; parent integrates note + row/stanza.
