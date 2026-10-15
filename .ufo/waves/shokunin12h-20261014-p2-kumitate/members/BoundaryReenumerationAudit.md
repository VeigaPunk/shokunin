# BoundaryReenumerationAudit — advisory (unjudged)

Independent re-enumeration of both layer universes. Data, not a verdict. This seat did not edit notes, the registry, or the stanza.

Origin: `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`). Lane: `kumitate-shokunin` @ dispatch `175de6ba2e9e904010411b19cab27e0af9aad3d4`.

## Axes

- **coverage** — live file set vs family reports vs what `familyPatterns()` actually admits
- **operability** — every count below is a command that was run
- **calibration** — a lane-list disagreement is not the same fact as a gate-pattern over-admit

## Files inspected

- `kumitate-shokunin/SCORECARD.md` registry rows 119-142 and the round-32 Planned stanza (1364-1409)
- `kumitate-shokunin/scripts/proxy-check.mjs` `LAYER_PATTERNS` (317-319), `layerOf` (554-559), `layerTerms` (581-595)
- `kumitate-shokunin/scripts/claims-check.mjs` `familyPatterns` / `inFamily` (255-272), distinct-section count (401-405)
- Origin `scripts/` and the two crate `src` dirs by `find` (read-only)
- Family reports S1 through S8 and R1 through R11 under this wave's `members/`
- `DeletionBoundaryArithmetic.md` family-size table, used only as a cross-check

## Commands + observed output

### Pin and membership stability

```text
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --name-only --diff-filter=AD -- \
    scripts crates/ufo-core-runtime/src crates/ufo-cli/src | wc -l
0

$ git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --name-only -- \
    scripts crates/ufo-core-runtime/src crates/ufo-cli/src
scripts/fleet-dispatcher.test.mjs
```

File set equals HEAD. One S8 member is content-dirty in the worktree. That is not a membership move and is not the halt condition in Planned. Other origin dirt (`README.md`, `config/ufo.json`, two `bundled/*.json`) is outside both layer universes.

### Layer walk (this seat's command, not a family lane's)

Frozen filters, copied from `LAYER_PATTERNS`: top-level `scripts/*.mjs`, every regular file recursively under a `scripts/` subdirectory (any extension), top-level `*.rs` in the two `src` dirs. Symlinks: 0. Nested non-regular: 0.

```text
$ find scripts -maxdepth 1 -type f -name '*.mjs' | wc -l
73
$ find scripts -mindepth 2 -type f | wc -l
18
$ find scripts -mindepth 2 -maxdepth 2 -type f | wc -l
14
$ find crates/ufo-core-runtime/src -maxdepth 1 -type f -name '*.rs' | wc -l
88
$ find crates/ufo-cli/src -maxdepth 1 -type f -name '*.rs' | wc -l
4
```

**S_members = 73 + 18 = 91. R_members = 88 + 4 = 92.** Matches the dispatch measurement and the before-proxy JSON (`S_members` 91, `R_members` 92). The depth-1 trap is still live: `maxdepth 2` reads 14 and drops the four depth-2 members `charter-scribe/prompts/kimi-update.prompt.txt`, `charter-scribe/systemd/charter-scribe.service`, `charter-scribe/systemd/charter-scribe.timer`, `lean-cargo/bin/cargo-shim.sh`.

### Disjoint partition this seat derived

Named families by the cell's non-widening tokens (explicit basenames, `probe-*.mjs`, `loop_driver*.rs`, `execution_profile*`, `cost_ledger*`, `lane_overlay*`, `lease*`, `live*`, `distill*`, `l3_swarm*`, `local_ship*`, `bounded_fs*`, and the three directory patterns). Remainder = layer walk minus that named set. Bash shim excluded (see counterexample).

| Family | Live | Rule |
|---|---:|---|
| S1 | 1 | `fleet-dispatcher.mjs` |
| S2 | 7 | 2 top-level + 5 under `collect-omp-native-handoff-lib/` (`refusal-line.mjs` absent) |
| S3 | 2 | `ufo-swarm-wave.mjs`, `ufo-swarm-collect.mjs` |
| S4 | **5** | `ufo-sighting.mjs` + 4 under `ufo-sighting-lib/` |
| S5 | 2 | `omp-global-config.mjs`, `ufo-mission-result.mjs` |
| S6 | 5 | the five watcher basenames |
| S7 | 6 | 5 `probe-*.mjs` + `fake-omp.mjs` (`atomic-write.mjs` and both `probe-*.test.mjs` absent) |
| S8 | 63 | 91 - 28 |
| sum S | **91** | |
| R1-R10 | 8+12+5+6+4+4+5+4+1+2 = **51** | unchanged; none of the six deletions match these patterns |
| R11 | **41** | 37 runtime remainder (88 - 51) + 4 CLI |
| sum R | **92** | |

`DeletionBoundaryArithmetic.md` prints the same sizes (S4 = 5, sum 91; R11 = 41, sum 92). That cross-check agrees with this walk. It is not the authority.

### comm -3 against family reports (both sides LC_ALL=C sort)

Reported script union = each seat's published member list (S8 taken from the fenced block under "Exact live S8 member list (63)", not from prose around it). Reported runtime union = R1-R10 published lists + R11's fenced 41.

```text
reported script lines 92 unique 92
$ LC_ALL=C uniq -d repS
(empty — no path listed by two family reports)
$ LC_ALL=C comm -3 layer-S.txt repS.txt
	scripts/ufo-sighting

reported runtime lines 92 unique 92
$ LC_ALL=C uniq -d repR
(empty)
$ LC_ALL=C comm -3 layer-R.txt repR.txt
(empty)
```

A leading tab is only-in-the-report. No layer file is missing from the reported union. No reported path is claimed by two families. The single disagreement is `scripts/ufo-sighting`, present only in `S4MemberRecensus.md`.

S8's 63-line fence versus this seat's remainder: `LC_ALL=C comm -3` empty. R11's 41-line fence versus this seat's remainder: empty.

Arithmetic if the parent sums the declared counts the seats asked for:

```text
script if S4=6: 1+7+2+6+2+5+6+63 = 92
script if S4=5: 1+7+2+5+2+5+6+63 = 91
runtime:        8+12+5+6+4+4+5+4+1+2+41 = 92
```

92 is not `S_members` 91. 91 and 92 match the walk.

## Counterexample 1 — S4 counts a file the denominator cannot see

`S4MemberRecensus.md` declares **6** and tells the parent to backtick `scripts/ufo-sighting` so `familyPatterns` will see the bash shim.

The shim is a real file. It is not a layer member.

```text
$ find scripts -maxdepth 1 -type f ! -name '*.mjs' | LC_ALL=C sort
scripts/dev-verify.sh
scripts/gates.sh
scripts/nc5-origin-sync.sh
scripts/nc5-seat-watch.sh
scripts/probe-token-plan-models.verdict.json
scripts/self-iter.sh
scripts/smoke.sh
scripts/ufo-night-watchdog-lib.sh
scripts/ufo-night-watchdog.sh
scripts/ufo-sighting
```

`LAYER_PATTERNS.S` is `^scripts/[^/]+\.mjs$` and `^scripts/[^/]+/.+`. Both reject `scripts/ufo-sighting` (observed: `[False, False]`). `S_members` will stay 91 if the parent does not edit `proxy-check.mjs`. Editing that filter is a derivation change, which this round's halt text forbids.

`layerTerms` increments `S_sections` for every section with `inFamily === true` (`proxy-check.mjs:595`). It does not check that the file is in the layer walk. A path-backticked shim plus the section S4 already added (`SECTION_FILE_NOT_MEMBER` on `scripts/ufo-sighting`) becomes an in-family section the denominator does not count.

That one section is enough to fake the planned step: `floor(10 * 63/91) = 6`, `floor(10 * 64/91) = 7`.

Leaving the section in place and declaring 5 is also wrong. `MEMBER_COUNT_DRIFT` compares distinct sections, and distinct includes out-of-family sections (`claims-check.mjs:401-405`). Declared 5 with the shim section still present drifts.

S4's pasted verdict line `CLAIMS: MATCH (... sections=6 adv=0)` cannot be emitted by `renderVerdict` (`claims-check.mjs:534-535`) together with `warnings=2`. The ROW line `adv=2` and the two warn lines are the observations consistent with the source. Do not treat `adv=0` as gate output.

**Smallest safe correction (parent):** S4 declared count **5**. Do not backtick `scripts/ufo-sighting` in a path-like form. Remove the member section whose heading is the shim path, and record the removal as outside the frozen universe, with the other nine top-level non-mjs files. Those ten belong to no scored family. That is the definition, not an orphan inside the 91.


## Counterexample 2 — lane lists are disjoint; the cells are not

`familyPatterns()` keeps every backtick with a slash, a star, or a known extension, anywhere in the members cell (`claims-check.mjs:256-258`). Applied to the live cells and the 91+92 walk:

| Row | Lane list | Gate admission | Over-admitting token |
|---|---:|---:|---|
| S8 | 63 | **91** | `*.mjs` |
| R1 | 8 | **23** | `native*.rs` |
| R11 | 41 | **92** | `crates/ufo-core-runtime/src/*.rs`, `crates/ufo-cli/src/*.rs` |
| S1-S7, R2-R10 | as table | same as lane list | none on this tree |

Gate multi-family hits: **84**. Every S1-S7 file (28) is also S8. Every runtime file is R11, and every `native*.rs` file (23) is also R1 — including R5's 4, R8's 4, R9's `native_tests.rs`, and R3's `native_profile.rs` (that file is in three families). Strict patterns (those four tokens removed) have **0** multi-hits and **95** orphans (54 S8 top-level mjs + 41 R11). The subtraction prose is not a pattern the gate can read.

`R1MemberRecensus.md` says the members cell has no backticked `native*.rs` glob and that no cell edit is required. That is false. `SCORECARD.md:127` backtick tokens, extracted from the live line, include `native*.rs` and `knowledge/runtime-remainder-census.md`. The round-17 Limits sentence that the shorthand is now non-pattern prose is stale: the explanation of the removal re-backticked the glob.

A lone `.rs` token in the R11 cell is also a pattern. It matches zero live files (basename equality, not a suffix). It is not the overlap source. The two directory globs are.

Today the notes do not section those cross-family files, so `S_sections` / `R_sections` are not yet double-counting. `SECTION_FILE_NOT_MEMBER` cannot fire for a foreign mjs inside the S8 note, a foreign `native*.rs` inside the R1 note, or any runtime file inside the R11 note. A later section, or a parent cell rewrite that keeps the backticks, counts the foreign file in the numerator.

**Smallest safe correction (parent), when rewriting the three cells:** replace each over-admitting backtick with tokens whose live match set equals the lane list.

- S8: drop the `*.mjs` backtick. Keep `charter-scribe/` and `lean-cargo/` (9 nested files, disjoint). Backtick the 54 top-level basenames. Dropping the glob without the basenames makes those 54 sections `SECTION_FILE_NOT_MEMBER` and drops them out of `S_sections`.
- R1: drop the backticks around `native*.rs` and around `knowledge/runtime-remainder-census.md`. The eight basenames already match. Do not trust the R1 report's "no cell edit" line.
- R11: drop the lone `.rs` token and both `crates/.../src/*.rs` globs. Backtick the 41 paths (or basenames: no runtime/CLI basename collision). Boundary prose `88 - 51 = 37` and CLI `4` is right; the backticks around the globs undo it.

Globs that are exact on this tree and need no split: `probe-*.mjs` (with `fake-omp.mjs`; `atomic-write.mjs` matches nothing live), `loop_driver*.rs`, `execution_profile*`, `cost_ledger*`, `lane_overlay*`, `lease*`, `live*`, `distill*`, `l3_swarm*`, `local_ship*`, `bounded_fs*`. `bounded_fs*` does not match `bounded_fixture.rs`.

## Heading hazard (not a current double-count)

Duplicate basename inside the script layer: `base.mjs` only.

- `scripts/collect-omp-native-handoff-lib/base.mjs` (S2)
- `scripts/ufo-sighting-lib/base.mjs` (S4)

A heading that is only `base.mjs` is `SECTION_FILE_AMBIGUOUS`. Both seats used full paths. Parent must keep the full path in those two headings. A basename backtick `base.mjs` in either cell would admit both files.

## Derived member list

Layer contribution, not the gate's widened admission:

- S1: `scripts/fleet-dispatcher.mjs`
- S2: `scripts/run-omp-native-trial.mjs`, `scripts/collect-omp-native-handoff.mjs`, and `scripts/collect-omp-native-handoff-lib/{base,events,evidence,policy,screening}.mjs`
- S3: `scripts/ufo-swarm-collect.mjs`, `scripts/ufo-swarm-wave.mjs`
- S4: `scripts/ufo-sighting.mjs`, `scripts/ufo-sighting-lib/{argv,base,observe,surface}.mjs`
- S5: `scripts/omp-global-config.mjs`, `scripts/ufo-mission-result.mjs`
- S6: `scripts/ufo-stale-watchdog.mjs`, `scripts/ufo-l0-monitor.mjs`, `scripts/ufo-l0-watch.mjs`, `scripts/the-tick-ping.mjs`, `scripts/ufo-ground-handler.mjs`
- S7: `scripts/fake-omp.mjs`, `scripts/probe-redact.mjs`, `scripts/probe-token-plan-kimi.mjs`, `scripts/probe-token-plan-models.mjs`, `scripts/probe-token-plan-shared.mjs`, `scripts/probe-ufo-route-health.mjs`
- S8: the 63 paths in `S8MemberRecensus.md` lines 96-158. `comm -3` against this walk was empty. Not re-copied here.
- R1-R10: the published lists (51 paths). Union with R11 matched the 92-file walk with an empty `comm -3`.
- R11: the 41 paths in `R11MemberRecensus.md` lines 117-162. `comm -3` empty.

Not members, do not subtract from the 91/92, do not add:

- Deleted outside the universe: `crates/ufo-cli/build.rs`, `crates/ufo-core-runtime/tests/godspeed_inject_full_prefix.rs`, `crates/ufo-core-runtime/tests/vector_anchors.rs`
- Added outside the universe: `scripts/nc5-origin-sync.sh`, `scripts/nc5-seat-watch.sh`, `scripts/ufo-night-watchdog-lib.sh`, `scripts/probe-token-plan-models.verdict.json`
- Historical exclusions still outside: `scripts/dev-verify.sh`, `scripts/gates.sh`, `scripts/self-iter.sh`, `scripts/smoke.sh`, `scripts/ufo-night-watchdog.sh`, plus `scripts/ufo-sighting`

## Sections added / removed by this seat

None. Read-only.

## Unresolved blockers

None for the enumeration. HEAD is still the pin; the layer name-set has not moved.

Residual, parent-owned, not a halt: family seats are editing notes while this report is written. The comparison above is to their published lists and to the tree, not to a note that may still be changing. If a note gains a section for a file another family owns, counterexample 2 says the current cells will count it.

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| S4 declared 6 and the path-backtick advice. Sum of seat counts would be 92 against `S_members` 91. One in-family shim section can floor 63/91 from 6 to 7. | Parent registry + sighting-wall section removal. Not S8. |
| `SCORECARD.md:127` still backticked `native*.rs`. R1 report says it does not. Limits text that says the shorthand is non-pattern prose is stale. | Parent R1 cell. R1 seat's "no cell edit" line is not safe to follow. |
| S8 `*.mjs` and R11 directory globs admit the other families. Lane lists themselves do not double-count. | Parent cell rewrite for S8 and R11. |
| `base.mjs` basename collision. Full-path headings already used. | Parent, if it rewrites those two headings to basenames. |
| R11 reports dead anchors on retained files. A dead anchor is CLAIMS drift but the section still counts in `R_sections` if `inFamily`. Membership is unaffected. | Parent note integrate / R11. Not this boundary. |
| S2 and S5 share `failure-telemetry.md`. S2 reported `SECTION_FILE_NOT_MEMBER` for S5's section. That warning does not add an `S_sections` credit (`inFamily` false). | Parent, optional: drop `failure-telemetry` from the S2 note cell. Not a double-counted member. |
| `scripts/fleet-dispatcher.test.mjs` bytes differ from HEAD. Set identity does not. | Whoever anchors that S8 section should read the worktree or `git show HEAD:`. |

## Impacted axes

- `coverage:script-layer` — the 6-to-7 step is one section wide (`64/91`). Crediting `scripts/ufo-sighting` is a false numerator, not a measured member.
- `coverage:runtime-layer` — lane union matches 92/92. No current double-count. The R1/R11 cells can create one if a foreign section is added or the widening backticks are kept while notes are rewritten.

