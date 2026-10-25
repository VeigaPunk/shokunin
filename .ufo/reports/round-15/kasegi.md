# kasegi — round 15 report

Lane: kasegi (depth + coverage, bounty/security research). Repo:
`~/projects/shokunin/kasegi-shokunin`. Round: 15/1024. Axis-move: **depth**
(forced into a source-loss re-anchor). Lane commit `eb5b590`.

## The event that redefined the round

`~/Projects/bounties` — the lane's PROVINCE root and the anchor of every
`~/Projects/bounties/...` citation in `SKILL.md` and all 22 `corpus/knowledge/`
entries — **was removed from the filesystem at 2026-09-28T23:51:31Z**, ~36 s
after the watchdog launched this round (20:50:55-03:00) and 19 min after round
14 last verified the tree alive (telemetry appends 23:32:22Z / 23:32:32Z).

The round's **first command** was a domain-tree snapshot (r14 lesson 4: read the
append-only log at round start). It returned `cd: no such file or directory`, so
the inherited r15 plan ("lift the EV constants into `## Triage economics`") was
replaced before a single edit. Had the round gone straight to editing, it would
have published fresh citations to files that no longer exist anywhere.

Detection (all re-runnable, all recorded verbatim in
`corpus/knowledge/source-tree-loss-2026-09-28.md` §1): `ls -d` → no such file;
full-depth `find /home/vgpnk` for `bounties` / `cantina-pendle` /
`bounty-fleet` / `missions.jsonl` → empty (one swallowed EACCES stderr line
re-run and recorded: a mode-000 unrelated dir); `/scratch` depth ≤ 4 → empty;
`~/.local/share/Trash/{files,info}` never initialized; `/proc/mounts` → no
separate volume. A critic L2 re-derived the absence independently (both casings,
the 40-entry `~/Projects` listing, full-root name sweep, rename-window sweep,
`docker inspect` on all 31 containers, 72 deleted-but-open fds) and killed the
"house-tidy swarm" hypothesis (`~/.ufo/house-tidy-round0-plan.md` exists with
this scope listed read-only, zero execution artifacts). **Actor UNDETERMINED**;
the single honest blind spot is that btrfs subvolume enumeration returns
`Operation not permitted` for this user and `/.snapshots` is root-only. **Data
PRESUMED-LOST locally.** Sentinel timeline bounds the event to 23:32Z–23:51:31Z
with concurrent activity at `origin-work/ufo-fsd-alpha` 20:53:17,
`origin-work/tmp` 20:53:56, `origin-work/open-bug-bounties/.git` 20:57:10, and an
attached `ufo_sighting` tmux (4 windows, created 15:24:42) hosting a separate
live agent session — panes captured read-only, never sent keys.

## What survives (measured, not assumed)

| root | state | round-15 disposition |
|---|---|---|
| `~/Projects/the-bounty-hunter` | frozen 2026-09-05 code mirror: HEAD `1cfbd86` (A=C 12:35:36-03:00) over `37c3668` (v0.1.0, 09:06:07-03:00), tag `v0.1.0`, clean worktree, 34 files / 8 dirs, remote `VeigaPunk/the-bounty-hunter`. `.git` crtime 09:01:51, reflog holds only the two commits (no clone/fetch), 0 packs / 48 loose objects, `fsck` clean ⇒ the local repo is the **origin** of that remote. 9 of 10 sampled `ops/*.mjs` are byte-identical to `37c3668`. `bounty-map/programs/` **does not exist** (0 records) | **censused** at file granularity (per-file `wc -l` + sha256 + provenance verdict for 11 files) |
| `~/Projects/origin-work/open-bug-bounties` | 26 claim-package dirs + 3 files, **0** `status.json` (pre-dates the six-file contract), `submission-review/claims` 21 entries, 43 `.ufo-missions`, 5 `data/*.json` inventories, git HEAD `1307b8b`. The mirror's `ops/check-freshness.mjs:14` defaults its board to exactly this path — the two survivors are wired together by the ops code | **inventory only** → round-16 coverage move |
| `~/Projects/bounties` | absent | 18/18 surfaces corpus-attested as-of 2026-09-28T23:32Z; **0/18 present** |

Per-file provenance (L1 reads + 3 scouts + revenger, all sha256-pinned; full
table in the corpus entry §4.1): `ops/ev-report.mjs` (92 ln, `ba5485ed6a5d`)
resolves **all 14** spans the corpus recorded from the live tree at 0 offset;
`ops/rank.mjs` (249 ln) matches at `DEFAULTS :55-59` and still hard-pins
`adjusted_ev === 514` at `:136`; `bounty-map/schema.json` matches at
`ev_inputs :32-52`; `ops/park-disposition.mjs` matches at `:18-21`, `:53-78`.
**Diverged**: `ops/fleet-dispatch.mjs` 330 ln vs the lost 427 — 3-term score at
`:97` vs 5 terms at `:110`, no `priority.json`/`review-verdicts` reader
anywhere, `adjusted_ev` telemetry at `:152`/`:155`/`:156` vs `:200`/`:204`,
different model strings, no `GRID`; `ops/shared.mjs` 41 ln — **no
`gitMutationBlocker`**; `ops/claim-check.mjs` 83 ln / **19** `err(` sites vs
233 / 48, with the whole `status.json` gate family absent. Fourth marker:
`lessons/round-4-aggregator-audit.md:28` records 14 `ops/*.mjs`; the mirror has
13. No second copy of any ops file exists on disk, so the live revisions survive
**only as corpus quotations** — which is exactly what a corpus is for.

Vocabulary discipline adopted: a 0-offset anchor match proves
**anchor-compatibility, not identity** (the lost bytes are gone), so
"REVISION-IDENTICAL" was corrected to ANCHOR-COMPATIBLE in the record; and every
lost-tree anchor is now written `` `[lost-tree] path:line` `` so the token cannot
resolve against the mirror by accident.

## Measured (both instruments, same script each side)

| instrument | before r15 | after r15 |
|---|---|---|
| `density.py` file mean over `SKILL.md` | 142.5 | **152.9** |
| `density.py` path-citation instances | 376 | **623** |
| block `## Triage economics` | 93.3 | **131.4** |
| block `## Ops integrity layer` | 61.1 | **111.5** |
| block `## VDP disclosure packages` | 81.8 | **117.4** |
| block `## Retirement lane` | 62.5 | **93.0** |
| `resolve.py` SKILL.md resolvability | 47/289 = 16.26 % | **222/486 = 45.68 %** |
| `resolve.py` corpus resolvability | 129/971 = 13.29 % | **396/1297 = 30.53 %** |
| `resolve.py` lane total | 156/1107 = 14.09 % | **410/1437 = 28.53 %** |
| `anchorcheck.py` over `SKILL.md` | n/a | 194 in-range mirror cite instances, **0 past-EOF** |

**The frozen bar was NOT cleared, and that is published rather than gamed.**
`BAR_R15 = 142.5` (the pre-edit file mean, frozen as a declared constant) is
above all four repaired blocks in prose form. The labrat measured the *unchanged*
old Triage content at 100.0 as 76-col prose vs **150.0** as a single-line-row
table (the lane's own r14 record: 86.0 vs 973.3) — the bar is reachable by
reformatting alone, so clearing it is not evidence of knowledge. Bar rule
amended for r16: frozen constant + **conjunctive** ≥ 60 % resolvability gate,
because the mutation tester proved density rewards a fabricated `path:line`
exactly as much as a real one (8 killed / 4 survived, 4 blind spots recorded).
Ratchet quantified: 96.5 pristine → 102.5 r14 → 142.5 r15 → ~167.5 projected
r16, loading the most demand onto exactly the blocks a prior round left thin.

Instrument continuity was proven before use: an independent L2 reimplementation
reproduced pre-r13 `fc6d398` (mean 96.5 + all four recorded block values),
pre-r14 `7483333` (bar 102.5 + 28.6/29.7/62.5) and all 18 live BEFORE-r15
values. All three instruments are now **committed** at
`corpus/instruments/{density.py,resolve.py,anchorcheck.py,README.md}` with the
census of record `citation-survival.{md,tsv}` — previously `/tmp`-resident and
one sweep from being lost. Fixed-point caveat disclosed: these files cite each
other, so each recording pass moves the rate < 0.1 pp; the committed census is
authoritative and the chase stops there.

## What landed

- **New canonical entry** `corpus/knowledge/source-tree-loss-2026-09-28.md`
  (10 sections): detection commands, disappearance window, the 18 gone surfaces,
  both survivors, per-file provenance with sha256, the binding **anchor-base
  rule**, the resolvability census, the never-re-verifiable DATA-half list, the
  nine L2 corrections, the measurements.
- **`## Triage economics` re-anchored** (93.3 → 131.4): per-constant cites for
  the four formula terms, `isNum`/`fmt`, the 10-input print loop, all four exit
  branches, the strict `> 0` verdict; the `rank.mjs` run contract + a 7-row
  admission table; dual-base citing for `fleet-dispatch.mjs`. New derived
  arithmetic: default priors give `adjusted_ev = 0.0735 × reward.min − 1750`, so
  break-even needs `reward.min > 23 809.52`; the observed maximum was 10 000 →
  **−1015**, i.e. every default-basis program is negative-EV and the `:123` sort
  degenerates to `reward.min` desc — AR12 ("EV is ordering, not a gate") in
  arithmetic. Plus the `expected_reward` two-sources trap (`ops/rank.mjs:92`/`:104`
  vs `ops/ev-report.mjs:78`).
- **Runnable verification survived the loss**: an L2 smoke-ran a byte-identical
  copy of the mirror `ev-report.mjs` outside the mirror
  (`/tmp/kasegi-r15/ev-smoke`, copy sha256 == mirror sha256) and observed every
  branch — exit 2 / exit 2 / `WARNING` + all-UNKNOWN + exit 0 / `total_cost`
  finite with `adjusted_ev` UNKNOWN on a missing factor / string `"0.5"` rejected
  per key / exactly-0 → `false` / and the round-13 record reproducing
  0.1764 · 1764 · 1250 · **514** · true.
- **New invariant defect found and proved**: `TELEMETRY_EVENTS`
  (`ops/shared.mjs:13-22`, 8 names) is imported by **nothing** — `grep -rn` over
  the mirror returns only the declaration, and `appendLedger` (`:36-41`) never
  checks the event name — while the ops scripts append **17** distinct `event:`
  values, 4 of them whitelisted; 4 whitelisted names are appended by no ops
  script. A decorative whitelist, same defect class as the decorative bounty map.
- **New hazard documented**: never run the mirror's ops scripts in place — all
  11 derive their write root from `import.meta.url`, so a run would create and
  mutate `ledger/`, `fleets/run/`, `docs/autopsies/`, `evidence/`,
  `bounty-map/programs/` inside a read-only product repo (and ENOENT on the first
  `appendLedger`; the mirror has no `ledger/`) [INFERENCE — derived, never
  executed].
- **5 defects repaired**: the autopsy artifact is **seven** parts, not five
  (`ops/park-disposition.mjs:56-59` + `:61`,`:67`,`:72`) — `SKILL.md` said five
  while listing seven, and `retirement-autopsies.md:38` said "five fixed parts"
  while enumerating seven; `bounty-map/schema.json:32-51` → `:32-52`;
  `triage-thresholds.md`'s 32 `SKILL.md:NNN` cites (23 unique spans) **pinned to
  blob `fc6d398`** with 8/8 sampled spans verified — the durable fix for a whole
  defect class, and the hazard the lane had already named in
  `lessons/round-5-aggregator-mirror-ambiguous-citation-base.md`; 2 unsupported
  `ops/claim-index.mjs:4` cites marked `[lost-tree]`; 1 past-EOF corpus cite
  annotated (`submitted-registry.md:105`).
- `SKILL.md` preamble + `## Cited paths` header state the loss, the three anchor
  bases and the measured resolvability; `corpus/README.md` gained 2 coverage-map
  rows + 2 known-gaps entries; `SCORECARD.md` re-based.

## Scorecard

`depth` was **split** (AXES.md:20-24, recorded with reason) because its two
sub-metrics moved in opposite directions this round and one integer hid the
state that matters:

| axis | before | after | why |
|---|---|---|---|
| `depth:density` | 9 | **9** | 4 blocks repaired, mean 142.5 → 152.9, cites 376 → 623; bar not cleared → held, not raised |
| `depth:verifiability` | 2 (first measurement: 16.26 %) | **4** | SKILL 45.68 %, lane 28.53 %, 0 past-EOF anchors; **704 genuine citations point at files that no longer exist** (r13/r14: 705/708 = 99.6 % resolved — the proxy did not change, the filesystem did) |
| `coverage` | 9 | **7** | denominator moved: 0/18 surfaces present, 18/18 corpus-attested; of the 2 surviving roots, 1 censused and 1 inventory-only |

The split exposes a *worse* number rather than concealing it, which is the test
for whether a split is honest. No axis retired.

## L2 fleet (15 subagents, one batched dispatch, all read-only)

3 scouts (mirror `ev-report`+schema / `rank`+`fleet-dispatch` / gates+ops),
2 executors (triage draft / ops+vdp+retire drafts), critic (premise + mirror +
bar falsification), reviewer (154 corpus anchors re-derived: 15 CONFIRMED /
3 LINE-SHIFT / 11 CONTENT-MISMATCH / 125 NOT-IN-MIRROR), connector (cross-lane
blast radius + scope), labrat (instrument continuity + ratchet), revenger (mirror
git forensics), sentinel (disappearance forensics), simplifier (anti-gaming
audit + 8 detection checks), distiller (66 duplicate EV/triage statements,
22 CODE-half vs 14 DATA-half facts, canonical-home map), mutation-tester (12
mutations, 4 blind spots). L1 re-derived every integrated anchor itself
(`anchorcheck.py`: 194 in-range, 0 past-EOF) and **rejected two executor claims**
that failed that check (a `[corpus-attested]` stamp misplaced onto
mirror-verifiable DEFAULTS; a `:201-205` live-tree span no source records). An
L2 falsification is a claim, not a verdict.

## Adjacency + push scope (reported, not absorbed)

- 339 `Projects/bounties` references across all 8 lane repos + main (221
  path-shaped, 133 inside `corpus/knowledge/`): protocol 18, kake 25, kotoba 28,
  kumitate 29, kagi 38, kengaku 47, aggregator 75, kasegi 77. **No sibling lane
  and no main-repo doc had recorded the disappearance**; kasegi round 14 was the
  last report to observe the tree alive, and 4 lanes wrote files after 23:51Z
  without mentioning it. Every other lane's PROVINCE that names this root needs
  the same treatment.
- `the-bounty-hunter` is **mixed scope**, not exclusive whole-repo ownership:
  kasegi owns the bounty EV/claim/policy semantics (the hunter contract in
  `.omp/agents/the-bounty-hunter.md`, `ops/rank.mjs`, `ops/ev-report.mjs`,
  `bounty-map/schema.json`); kumitate owns orchestration/tooling
  (`fleet-dispatch`, `registry-check`, `validate`, `reroute-drill`, sighting
  scripts, lane→bucket routing); protocol/integrator arbitrates the repo-level
  split, consistent with the r10 `fleets/registry.json` ruling
  (`.ufo/reports/round-10/protocol.md:249-252`, `AGGREGATE.md:667`).
- Its remote `VeigaPunk/the-bounty-hunter` is **outside** the lane push
  allow-list (`MISSION.md:49-56`). This lane pushed nothing there, wrote zero
  bytes under `~/Projects/**` (attested independently by two L2s), reverted
  nothing and re-created nothing.
- Duplicate knowledge that will drift: kotoba
  `corpus/knowledge/fleet-program-intake.md:15-70` re-states the BANNED/PARKED/K3
  constants and the 26 h freshness threshold; kumitate
  `docs/fleet-orchestration-reference.md:186-242` re-derives `shared.mjs`
  telemetry events and `registry-check` gates. Both are now citing a *third*
  state (the lost tree) — integrator arbitration suggested, not requested by
  this lane.

## L0 side channel

Appended to `.ufo/l0-questions.md` (kasegi round-15 row): (1) operator reorg /
cleanup vs unintended deletion — the round-12 question had already flagged the
stalled rebase, 903 dirty entries and 49 G untracked `george/`; (2) is the data
recoverable (btrfs snapshot / remote / archive) or presumed lost; (3) should
`PROVINCE.md` re-point at the two surviving roots, and does `the-bounty-hunter`
belong to kasegi or kumitate. The lane made none of those calls itself.

## Round 16 plan

`depth:verifiability` (lowest axis at 4): anchor-base-pin the remaining **20**
`corpus/knowledge/*.md` entries the way `triage-thresholds.md` was pinned, then
re-run both instruments. Falsifiable target: lane resolvability 28.53 % → ≥ 40 %
with zero past-EOF anchors in `corpus/knowledge/`. Secondary: move the
`TELEMETRY_EVENTS` derivation to its canonical home `ops-invariants.md`
(distiller's map), repair `## Pipeline` (13.3, the last block below 100), and
census `~/Projects/origin-work/open-bug-bounties` for coverage.

Artifacts: `/tmp/kasegi-r15/*` (15 L2 reports + drafts + mutation report),
committed instruments + census in `corpus/instruments/`, lesson in
`corpus/lessons/round-15.md`, LOG entry at `LOG.md:517-683`.
