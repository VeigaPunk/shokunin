# R8MemberRecensus — round-32 unjudged fleet wave

Member seat: `R8MemberRecensus`  
Family: **R8** — transcript / ledger / seat coverage  
Lane: `kumitate-shokunin` @ dispatch HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`  
Origin tree: `/home/vgpnk/Projects/ufo-fsd-alpha` @ `964f443ee53df0ce06bd689af01f0dea031b01f9`  
Deletion pin: `5725fa7d3`  
Note: `corpus/knowledge/native-transcript-ledger-seats.md`  
This report is **data**, not a verdict. Parent owns the registry row and stanza.

## Axes (named)

- **coverage** — live R8 membership vs registry/note section honesty  
- **operability** — claims gate re-derives the row without error  
- **calibration** — declared count matches measured live set; no phantom/deleted members

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row R8 + `## Planned` round-32 pre-registration |
| `kumitate-shokunin/corpus/README.md` | map row → `knowledge/native-transcript-ledger-seats.md` |
| `kumitate-shokunin/corpus/knowledge/native-transcript-ledger-seats.md` | R8 section-form note (4 `##` members) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-claims gate (live-anchor semantics) |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_transcript.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_ledger.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_seat_coverage.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_dispatch_topology.rs` | live member |

No note/registry edits by this seat (parent-owned). Report path only.

## Exact commands + observed output

### Origin HEAD + layer universe

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ ls /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/*.rs | wc -l
88

$ ls /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/*.rs | wc -l
4
```

Layer check: **R_members live = 88 + 4 = 92** (matches dispatch/planned drift vs frozen stanza 98).

### R8 live membership (direct presence + line counts)

```
$ for f in native_transcript.rs native_ledger.rs native_seat_coverage.rs native_dispatch_topology.rs; do
    test -f crates/ufo-core-runtime/src/$f && wc -l crates/ufo-core-runtime/src/$f
  done
# (cwd origin)
986 crates/ufo-core-runtime/src/native_transcript.rs
343 crates/ufo-core-runtime/src/native_ledger.rs
291 crates/ufo-core-runtime/src/native_seat_coverage.rs
434 crates/ufo-core-runtime/src/native_dispatch_topology.rs
```

All four basenames resolve under `crates/ufo-core-runtime/src/`. **Zero** resolve under `crates/ufo-cli/src/`.

### `LC_ALL=C` boundary probe (declared ∩ live)

Both sides sorted with `LC_ALL=C sort` (locale trap per `## Limits`).

```
$ printf '%s\n' native_dispatch_topology.rs native_ledger.rs native_seat_coverage.rs native_transcript.rs \
    | LC_ALL=C sort > /tmp/r8_dec.txt
$ ls crates/ufo-core-runtime/src/*.rs | xargs -n1 basename | LC_ALL=C sort > /tmp/r8_live_all.txt

$ comm -12 /tmp/r8_dec.txt /tmp/r8_live_all.txt
native_dispatch_topology.rs
native_ledger.rs
native_seat_coverage.rs
native_transcript.rs

$ comm -23 /tmp/r8_dec.txt /tmp/r8_live_all.txt
# (empty)
```

`comm -23` empty ⇒ **no phantom declared members**. Intersection size **4**.

### Deletions since `5725fa7d3` (runtime + CLI)

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --name-status 5725fa7d3..HEAD \
    -- crates/ufo-core-runtime/src crates/ufo-cli/src | grep '^D'
D	crates/ufo-cli/src/admission.rs
D	crates/ufo-core-runtime/src/native_epoch.rs
D	crates/ufo-core-runtime/src/native_epoch_tests.rs
D	crates/ufo-core-runtime/src/native_launch_tests.rs
D	crates/ufo-core-runtime/src/replay_falsification_probes.rs
D	crates/ufo-core-runtime/src/rfc3339.rs
```

R8-name filter on the same diff range:

```
$ … | grep -E 'native_(transcript|ledger|seat_coverage|dispatch_topology)'
M	crates/ufo-core-runtime/src/native_dispatch_topology.rs
M	crates/ufo-core-runtime/src/native_ledger.rs
M	crates/ufo-core-runtime/src/native_seat_coverage.rs
M	crates/ufo-core-runtime/src/native_transcript.rs
```

**No `D` rows for any R8 basename.** All four R8 files are modified in place, not deleted. Deleted-since-pin files are **NOT** R8 members (R11/other-family remainder; owner: those family seats / parent integration).

### Registry row (SCORECARD) vs note headings

Registry cell (SCORECARD in-scope surface registry):

```
| R8 | transcript / ledger / seat coverage | 4 files (`native_transcript.rs`, `native_ledger.rs`, `native_seat_coverage.rs`, `native_dispatch_topology.rs`) | yes — native-transcript-ledger-seats (r7) |
```

Note `## ` headings:

```
11:## `native_transcript.rs` (939 L) — …
68:## `native_ledger.rs` (350 L) — …
112:## `native_seat_coverage.rs` (317 L) — …
143:## `native_dispatch_topology.rs` (465 L) — …
```

### Claims gate (operability check)

```
$ node scripts/claims-check.mjs --row R8 --src /home/vgpnk/Projects/ufo-fsd-alpha --strict
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 4
ROW R8   form=section   notes=1 sections=4 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=4 adv=0)
```

JSON section inventory (same run, `--json`): four sections, each `live: true`, `symbolHit: true`, `inFamily: true`, `file` under `crates/ufo-core-runtime/src/…`.

## Derived live member list

**Exact R8 members (current origin tree):**

1. `crates/ufo-core-runtime/src/native_transcript.rs` (986 L)  
2. `crates/ufo-core-runtime/src/native_ledger.rs` (343 L)  
3. `crates/ufo-core-runtime/src/native_seat_coverage.rs` (291 L)  
4. `crates/ufo-core-runtime/src/native_dispatch_topology.rs` (434 L)

**Declared count the registry row must carry: `4`**  
(form: `4 files (…)` — measured set equals the existing cell; no membership cell rewrite required for R8).

Sorted basenames: `native_dispatch_topology.rs`, `native_ledger.rs`, `native_seat_coverage.rs`, `native_transcript.rs`.

## Sections added / removed

| Action | Section | Reason |
|---|---|---|
| **none added** | — | All four live members already have one `## \`<member>.rs\`` section |
| **none removed** | — | No section names a file absent from the live tree; no R8 deletion since `5725fa7d3` |

Section honesty status: **complete at 4/4** under claims-check live-any-anchor + symbol rules.

### Heading line-count drift (informational; not a membership change)

Note headings still print historical sizes; live `wc -l` differs:

| Member | Note heading L | Live L |
|---|---:|---:|
| `native_transcript.rs` | 939 | 986 |
| `native_ledger.rs` | 350 | 343 |
| `native_seat_coverage.rs` | 317 | 291 |
| `native_dispatch_topology.rs` | 465 | 434 |

Some bare `:N-M` cites in the note body fall past EOF on the shrunken files (e.g. ledger `:331-349`, seat_coverage `:182-317`, topology `:410-465`). Claims-check still `MATCH`es because **at least one** own-file anchor per section is live (`ownAnchors.some(…)`). Parent may refresh stale line cites when integrating; **not** a section add/remove event and **not** a declared-count change.

## Unresolved blockers

**None for R8 membership.**  
- Live set = registry declared set = note section set = **4**.  
- Gate: `CLAIMS: MATCH … sections=4 adv=0`.  
- No deleted-member phantom sections to strip.  
- No new member lacking a section.

## Cross-domain findings (owner named; not absorbed)

| Finding | Owner |
|---|---|
| Layer `R_members` live **92** (88+4) vs frozen stanza **98**; six runtime/CLI deletes since `5725fa7d3` listed above | Parent stanza + **R11** / other-R family seats (those basenames are not R8) |
| `admission.rs` deleted from CLI | R11 / CLI remainder seat |
| `native_epoch.rs`, `native_epoch_tests.rs`, `native_launch_tests.rs`, `replay_falsification_probes.rs`, `rfc3339.rs` deleted | Respective R* remainder owners (not R8) |
| Note heading L counts + some range cites stale vs live files | Parent note integration (optional cite refresh); membership unaffected |

## Summary for parent

- **Member list:** `native_transcript.rs`, `native_ledger.rs`, `native_seat_coverage.rs`, `native_dispatch_topology.rs` (all under `crates/ufo-core-runtime/src/`).  
- **Declared count:** **4**.  
- **Sections added:** 0.  
- **Sections removed:** 0.  
- **Removals recorded:** n/a (no deleted R8 members).  
- **Claims:** MATCH, 4 in-family live sections, adv=0.  
- R8 does **not** drive the planned 98→92 layer shrink; hold the row at 4 and leave layer arithmetic to parent after other family seats land.
