# W1 Freshness census — `corpus/knowledge/` headers across all lane repos

Seat: W1Freshness · date 2026-10-19 · read-only; one-off parsing ran as heredoc Python
in `/tmp` (nothing written to any repo). Counting commands are given per figure.

**Headline: zero overdue rechecks fleet-wide — because no entry carries a calendar
deadline at all.** Every `recheck:`/`Recheck when:` line is a re-run command, an
event trigger ("before using X", "when Y changes"), or prose. The four
`2026-10-17` dates inside kotodama recheck lines are incidental re-inspection
mentions, not due dates (verified by reading all four lines:
`kotodama-shokunin/corpus/knowledge/civilizations/japan-medieval-sengoku.md:24`,
`korea-three-kingdoms-goryeo.md:23`, `ottoman.md:7`, `thrace-dacia.md`,
`culture-material/material-culture-inference-method.md:17` — each reads
"Before exact use…" / "remains open after the 2026-10-17 triage").

## Method

- Entry = every regular file under `<lane>/corpus/knowledge/` except `.gitkeep`
  (three excluded: `chousa`, plus `.manifest.d/*.sha256` receipts counted as files
  — see notes). Command: `find <lane>/corpus/knowledge -type f ! -name .gitkeep | wc -l`
- Header detection: line-anchored, case-insensitive `source:` / `original-source:` /
  `sources:` (list form), `verified-at:` / `verified at`, `recheck:` / `re-check:` /
  `recheck when:`; fenced code blocks and table cells that merely *name* the trio
  (e.g. kaidoku's `2026-10-15-metadata-trio.md`) are excluded.
- Resolvability: `~` and `/` paths checked on the live host; relative tokens tried
  against lane root, entry dir, `corpus/`, `corpus/knowledge/`; bare names searched
  recursively under `corpus/`. `/tmp`, `_npx`, `/proc` classed transient;
  `* {} () |` classed glob. URLs counted present (not fetched).
- Verified-at ranges: first ISO date in each `verified-at:` value.

## Per-lane table

| lane | entries | `source:` | `sources:`-list | `verified-at:` | `recheck:` | full trio | overdue | dead-ptr files | no-resolvable-src |
|---|---|---|---|---|---|---|---|---|---|
| audio-shokunin | 14 | 9 | 0 | 9 | 9 | 9 | 0 | 3 | 1 |
| chousa-shokunin | 24 | 24 | 0 | 24 | 14 | 14 | 0 | 0 | 9 |
| game-dev-2d-shokunin | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| game-dev-3d-shokunin | 45 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| kagi-shokunin | 21 | 7 | 1 | 0 | 0 | 0 | 0 | 6 | 7 |
| kaidoku-shokunin | 90 | 88 | 10 | 87 | 18 | 17 | 0 | 43 | 30 |
| kake-shokunin | 18 | 7 | 4 | 0 | 0 | 0 | 0 | 6 | 5 |
| kama-shokunin | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| kasegi-shokunin | 25 | 17 | 0 | 0 | 0 | 0 | 0 | 12 | 15 |
| kengaku-shokunin | 27 | 11 | 0 | 0 | 0 | 0 | 0 | 9 | 8 |
| kotoba-shokunin | 35 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| kotodama-shokunin | 224 | 156 | 224 | 224 | 224 | 224 | 0 | 0 | 178 |
| kumitate-shokunin | 38 | 1 | 10 | 0 | 0 | 0 | 0 | 0* | 10 |
| lore-shokunin | 25 | 12 | 0 | 12 | 11 | 11 | 0 | 2 | 1 |
| mado-shokunin | 22 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 3 |
| mori-shokunin | 14 | 7 | 0 | 7 | 5 | 5 | 0 | 2 | 1 |
| revenger-shokunin | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| souji-shokunin | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tabi-shokunin | 26 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| tameshi-shokunin | 19 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| tsukuroi-shokunin | 26 | 19 | 0 | 14 | 14 | 14 | 0 | 0 | 17 |
| **fleet** | **707** | **367** | **251** | **469** | **311** | **311** | **0** | **86** | **288** |

Count commands (reproducible):
- entries: `find <lane>/corpus/knowledge -type f ! -name .gitkeep | wc -l`
- `source:`: `grep -rlE '^\s*[-*> ]*(original-)?[sS]ource\s*:' <lane>/corpus/knowledge | wc -l`
- `sources:` list form: `grep -rlE '^\s*[-*> ]*sources\s*:' <lane>/corpus/knowledge | wc -l`
- `verified-at:`: `grep -rlE '^\s*[-*> ]*[vV]erified[- ]at\s*:' <lane>/corpus/knowledge | wc -l`
- `recheck:`: `grep -rlE '^\s*[-*> ]*([rR]e-?[cC]heck|[rR]echeck when)\s*:' <lane>/corpus/knowledge | wc -l`

\* kumitate's dead pointers live inside `- sources:` bibliography lists, which the
resolver pass skipped (it resolves only `source:`/`original-source:` field values).
Manual check: 10 of the 10 `sources:`-list entries reference
`scripts/ufo-*.mjs`, `config/ufo.json`, `crates/ufo-core-runtime/src/*.rs`, and
`src/native*.rs` relative to a stated root `~/Projects/origin-work/ufo-fsd-alpha`.
That root is **absent**; the same files all exist at `~/Projects/ufo-fsd-alpha`
(verified: `config/ufo.json`, `scripts/ufo-swarm-wave.mjs`,
`crates/ufo-core-runtime/src/gate.rs` all present). The root moved; every such
entry's stated anchor prefix is stale. Same class of issue as kumitate's
`~/Projects/ufo-*` prose roots elsewhere in the entries.

### Notes on the zero rows and entry counts

- `game-dev-3d`: only 3 of 45 files are lane-authored prose entries
  (`engines.md`, `rea.md`, `seed.md`); the other 42 are a vendored snapshot
  (`unreal-mcp/upstream/*`, LICENSE, hooks, `gate/run_gate.sh`) plus 12
  `.manifest.d/*.sha256` receipts — none of which are knowledge entries carrying
  headers. The trio being 0 on a vendored snapshot is correct, not a defect.
- Zero-header lanes by design or by drift: `game-dev-2d`, `revenger`, `kama`,
  `souji` (a `.tsv` ledger), `tameshi` (19/19 lack the trio), `kumitate` (37/38),
  `kotoba` (32/35), `tabi` (24/26), `mado` (18/22), `game-dev-3d` — these lanes
  carry provenance inline (`[L1-F<n>]` receipts, `path:line` table columns,
  `[tok]` tokens) instead of the header trio.
- `kaidoku` plural `sources:` = 10 files carry a `- sources:` bullet list in
  addition to `source:` lines.

## Overdue list — EMPTY

No `recheck:`/`Recheck when:` value anywhere is a bare `YYYY-MM-DD` or an `Nd`
cadence. Deadline-gated scan (date adjacent to by/due/before/until/deadline/
refresh, or `\d+d` cadence added to `verified-at`) returned zero rows:
`grep -rhoE '^\s*[-*> ]*(re-?check|recheck when)\s*:.*' */corpus/knowledge | grep -E '20[0-9]{2}-[0-9]{2}-[0-9]{2}'` → 7 hits, all incidental.

Recheck-kind distribution (first `recheck:` line per entry, `res==0` excluded):
- command: chousa 14, audio 7, kaidoku 16, mori 5, tsukuroi 4, tabi 2,
  mado 3, kotoba 1, lore 1, kotodama 10 = **63**
- event ("when/before/if/next"): kotodama 184, lore 9 = **193**
- prose (trigger described, no keyword): kotodama 26, tsukuroi 10,
  audio 2, kaidoku 2, kotoba 1, lore 1 = **42**
- date-mention (date inside command/prose, not a deadline): kotodama 4

Closest thing to staleness anywhere: `kaidoku` entries whose recheck commands
were last exercised 2026-10-19 (same-day, fresh); `kaidoku` `verified-at` floor
is 2026-09-21 (`corpus/knowledge/2026-09-21-*.md` family, oldest verified date
fleet-wide).

## Source-kind mix (of entries carrying `source:`)

Multiple kinds may co-occur per entry.

| lane | url | repo/abs path | command | prose/biblio only |
|---|---|---|---|---|
| audio | 0 | 8 | 1 | 1 |
| chousa | 0 | 14 | 1 | 9 |
| kagi | 0 | 7 | 0 | 0 |
| kaidoku | 0 | 74 | ~50 | ~10 (command-covered values still counted path/prose where mixed) |
| kake | 0 | 7 | 0 | ~2 |
| kasegi | 0 | 15 | ~2 | ~2 |
| kengaku | 0 | 11 | 1 | ~3 |
| kotoba | 0 | 2 | 1 | 0 |
| kotodama | 10 | 56 | 8 | 178 (book/journal citations — the `- sources:` ledgers) |
| kumitate | 0 | 10+ (inside `sources:` lists) | 0 | — |
| lore | 0 | 10 | 0 | 1 |
| mado | 0 | 3 | 1 | 2 |
| mori | 0 | 7 | 5 | 0 |
| tabi | 0 | 1 | 1 | 1 |
| tameshi | 0 | 1 | 0 | 0 |
| tsukuroi | 0 | 2 | 4 | 17 |

URLs appear only in kotodama (DOIs, BMCR review links, Dartmouth teaching pages
inside the `- sources:` bibliographies — e.g.
`civilizations/aegean-minoan-mycenaean.md:4-17`). Every other lane's sources are
host paths, repo paths, or commands — the fleet's knowledge is almost entirely
own-probe-derived, which is on-essence, but means "where to learn more" is
unserved today outside kotodama. The SOURCES.md draft contract fills exactly
this gap.

## Dead / unresolvable pointers (by file)

Roots verified absent on host (each is a root, not a typo): `~/Projects/webzites`
(kake, kengaku), `~/Projects/bounties` + `~/Projects/the-bounty-hunter` (kasegi),
`~/Projects/origin-work` (kumitate — real root now `~/Projects/ufo-fsd-alpha`),
`~/.bailian` + `~/bench-arena` + `~/archive/bench-arena` (kengaku),
`~/.local/bin/the-janitor` + `~/.local/bin/tac-check` (kagi),
`~/.config/opencode/skills/ufo/` (kotoba). Several lanes already document the
loss in-corpus (`kasegi/root-loss-2026-10-12.md`,
`kasegi/source-tree-loss-2026-09-28.md`, kengaku entries naming "the absent
root") — the pointers are honest tombstones, not silent rot.

| lane | file | dead pointers (all in `source:`/`original-source:` lines) |
|---|---|---|
| kagi | cdp-bridge-1password.md | `~/.local/bin/the-janitor` |
| kagi | credential-isolation.md | `~/.config/the-janitor/opencode.json`, `~/.local/bin/the-janitor` |
| kagi | janitor-command-surface.md, janitor-env-contract.md, op-env-refs.md | `~/.local/bin/the-janitor` |
| kagi | tac-evidence-integrity.md | `~/.local/bin/tac-check` |
| kake | drift-detection.md | `scripts/kimi-surface.mjs` |
| kake | fire-journal-codes.md | `~/Projects/webzites/scripts/kimi-surface.mjs` |
| kake | fleet-registry.md | `~/Projects/webzites/fleet/fleet.config.json` |
| kake | free-read-verbs.md | `~/Projects/webzites/src/{cli,fleet,probe,reconcile}.mjs` (4 paths) |
| kake | mirror-pitfalls.md | `fleet/kimi-surface-ops.md` |
| kake | ops-automation.md | `~/.config/systemd/user/webzites-{keeper,probe}.{service,timer}` (4 units) |
| kake | origin-repos.md | `repos-r8.md`, `~/Projects/webzites/reports/keepers/repos-r1.md` |
| kake | publish-channels.md | `~/Projects/webzites/fleet/kimi-surface-ops.md` |
| kake | speedrun-pipeline.md | `~/Projects/webzites/docs/SPEEDRUN-PROTOCOL.md` |
| kasegi | claim-gates.md | `~/Projects/bounties/ops/claim-check.mjs` |
| kasegi | claim-package-contract.md | `~/Projects/bounties/fleets/mission-template.md` |
| kasegi | ev-model.md | `~/Projects/the-bounty-hunter/ops/ev-report.mjs` |
| kasegi | evidence-dir.md | `~/Projects/bounties/evidence/` |
| kasegi | intake-and-finalize.md | `~/Projects/bounties/ops/import-board.mjs` |
| kasegi | mission-control.md | `~/Projects/bounties/ops/fleet-dispatch.mjs` |
| kasegi | mission-ledger.md | `missions.json`, `~/Projects/bounties/ledger/` |
| kasegi | operator-queue.md | `docs/claim-ready-index.md` (inside absent root) |
| kasegi | policy-access-playbook.md | `~/Projects/the-bounty-hunter/fleets/mission-template.md` |
| kasegi | program-quirks.md | `claims/cantina-pendle/ingestion-20260915/` |
| kasegi | retirement-autopsies.md | `docs/autopsies/`, `~/Projects/the-bounty-hunter/ops/park-disposition.mjs` |
| kasegi | terminal-classes.md | `docs/continuation-notes.md` |
| kengaku | bailian-cli-telemetry.md | `~/.bailian/telemetry.jsonl`, `~/.bailian` |
| kengaku | bench-arena-round11-power.md | `results-r11.json` |
| kengaku | bench-arena-round12-ladder.md | `results-r12.json` |
| kengaku | benchmark-selection.md | `~/Projects/webzites/repos/llm-wiki/wiki/…/benchmark-shortlist-for-godspeed-research.md` |
| kengaku | godspeed-eval-findings.md | `~/Projects/webzites/repos/llm-wiki/wiki/…/godspeed-umwelt-iteration-2.md` |
| kengaku | ledger-route-telemetry.md | `~/Projects/bounties/ledger/telemetry.jsonl` |
| kengaku | local-bench-arena.md | `~/bench-arena/`, `~/archive/bench-arena/` |
| kengaku | local-model-index.md | `index.md`, `~/.bailian/skills/bailian-docs-llm-wiki/models/`, `~/.bailian/wiki-sync-state.json` |
| kengaku | telemetry-run-design.md | `~/Projects/webzites/repos/llm-wiki/wiki/…/godspeed-umwelt-iteration-3-alpha-shittycodex.md` |
| kotoba | anatomy-and-compression.md | `~/.config/opencode/skills/ufo/SKILL.md` |
| kotoba | harness-independent-round41-census.md | `.ufo/round-41/drafts/v10/*` (6 paths — drafts dir absent; surviving artifact lives at `.ufo/round-45/evidence/H01/channel-census.json`) |
| lore | r102-push-synthesis-r95-r102.md | `-debt.json` (truncated name), `V74-debt-2.md` |
| lore | r94-cross-myth-design-comparison.md | `R26.md` |
| mori | lane-silence-r2.md | `PROTOCOL.md` (cited at some root; absent where anchored) |
| mori | observability-census-r1.md | `mori-shokunin/tools/mori-census.sh` (exists at `tools/mori-census.sh` — prefix duplicated) |
| tabi | arc-synthesis.md | `r9-aud-b9.md` |
| audio | 2026-10-13-sox-ffmpeg-packet-residue.md | `r62-adjudicator.md`, `r62-verifier.md` |
| audio | 2026-10-14-sox-extension-suffix.md | `formats_i.c`, `runs/census.json`, `runs/sweep-author-probes.json`, `sounder.c`, `src/formats.c`, `tx16w.c` (SoX source tree — external artifact, unpacked copy not retained) |
| audio | 2026-10-14-sox-posttable-fallback.md | `smp.c`, `src/formats.c`, `tx16w.c` (same class) |
| kaidoku | 43 files | mostly target-internal members (`dist/application/Doctor.js`, `app.asar`, `DirectAnalysis.js`, `EvidenceInputResolver.js` — inside installed apps, never lane paths) plus evaporated host state: `/var/lib/systemd/coredump/core.waybar…zst`, `~/.cache/uv/archive-v0/…/cli-64.exe`, `/var/lib/pacman/sync/*.db` (exists — glob), `dist/browser/CdpEndpoint.js`, `03-rea-doctor.md`, `11-asar-surface.md`, `12-evidence-bundle.md` (sibling-name drift), `claims/cantina-pendle/` family |
| kumitate | 10 files (`sources:` lists, resolved manually) | all pointers resolve under `~/Projects/ufo-fsd-alpha/` but the entries name `~/Projects/origin-work/ufo-fsd-alpha` — stale root prefix, files themselves intact |

Transient-by-design (correctly declared, not defects): `kaidoku` `/tmp/*.json`
probe envelopes (parsed then deleted per entry text), `_npx` cache paths.

## Entries with `source:` but no resolvable pointer (288 total)

Breakdown by class: kotodama 178 are bibliography-only (books/journals — resolvable
by library lookup, intentionally so); chousa 9 and tsukuroi 17 describe self-audits
and receipts in prose; kumitate 10 under stale root; kasegi 15 + kengaku 8 + kake 5
+ kagi 7 under absent roots; audio 1, lore 1, mado 3, mori 1, tabi 1, tameshi 1,
kotoba 1, kaidoku 30 (command-only provenance — executable, no stored artifact).

## `verified-at:` ranges (lanes carrying the field)

| lane | entries w/ verified-at | oldest | newest |
|---|---|---|---|
| kaidoku | 87 | 2026-09-21 | 2026-10-19 |
| kotodama | 224 | 2026-10-17 | 2026-10-19 |
| chousa | 24 | 2026-10-15 | 2026-10-19 |
| tsukuroi | 14 | 2026-10-14 | 2026-10-15 |
| lore | 12 | 2026-10-17 | 2026-10-18 |
| audio | 9 | 2026-10-13 | 2026-10-14 |
| mori | 7 | 2026-10-15 | 2026-10-15 |
| mado | 3 | 2026-10-14 | 2026-10-14 |
| kotoba | 2 | 2026-10-15 | 2026-10-19 |
| tabi | 2 | 2026-10-14 | 2026-10-14 |

All other lanes: zero entries carry the field.

## Findings for wave 2

1. **Header conformance is bimodal.** kotodama (224/224 trio), chousa, tsukuroi,
   audio carry the full trio; 10 lanes carry zero `verified-at:`/`recheck:` on any
   entry. A fleet `QUALITY.md`-level rule "every knowledge entry opens with
   `source:`/`verified-at:`/`recheck:`" would flag ~430 entries across
   game-dev-2d/3d, kagi, kake, kama, kasegi, kengaku, kotoba, kumitate, lore,
   mado, mori, revenger, souji, tabi, tameshi.
2. **No calendar-based freshness machinery exists.** Overdue = 0 because due
   dates do not exist; rechecks are commands and event triggers. If the fleet
   wants staleness detection it must invent the `Nd` cadence convention (the
   SOURCES.md draft already has `recheck: 90d` — extend it to knowledge).
3. **Root-loss is a live hazard, already half-documented.** Five dead external
   roots (webzites, bounties, the-bounty-hunter, `.bailian`, bench-arena) +
   one moved root (`origin-work/ufo-fsd-alpha` → `ufo-fsd-alpha`) + two
   uninstalled tools (`the-janitor`, `tac-check`) + a cleaned drafts dir
   (kotoba round-41 v10). kasegi/kengaku keep honest tombstones; other lanes
   (kumitate, mori, audio, lore, tabi) carry quiet drift. A "dead-pointer sweep"
   is a cheap falsifiable round claim for several lanes.
4. **External learning sources are absent outside kotodama.** Only 10 entries
   fleet-wide cite a URL. SOURCES.md per lane is the right instrument; the
   corpus today proves almost nothing came from the outside.
5. **`game-dev-3d`'s vendored `unreal-mcp/` snapshot (42 files) sits inside
   `corpus/knowledge/`** and inflates its entry count; consider whether receipts
   (`.manifest.d`) and upstream checkouts belong under knowledge or a sibling
   `corpus/vendor/` / `corpus/evidence/` dir.
