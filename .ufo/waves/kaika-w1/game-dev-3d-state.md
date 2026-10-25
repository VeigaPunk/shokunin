# game-dev-3d — STATE dossier (kaika W1, read-only)

Lane repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin` · wave: kaika W1 research
· date: 2026-10-19 · shape: **STATE** (lane-internal; no web research performed or needed,
`web_search` was available and unused by design).

**Read-only discipline.** No repo edit, commit, checkout, install, or subagent dispatch. The
only write is this artifact. All measurements below are reads (`read`, `git` read commands,
`grep`, `du`, `sha256sum`, one Python JSON count). No battery, gate, or fixture was re-run;
nothing here upgrades a lane claim to execution evidence — every lane claim is reported at the
strength its record gives it.

## 0. Evidence frame

- HEAD `7c4e5897d900ef8af0a826fa8c786e7cf32ea08f` — `git log -1 --format='%H %ci %s'` →
  `2026-10-19 00:33:08 -0300`, subject `r107-aborted: stray shards from the cancelled side-round
  swarm (wrong-cwd spawn; relocated, unvalidated, content not admitted)`.
- Branch `main`; `origin` → `https://github.com/VeigaPunk/shokunin-3d-engines.git`;
  `git rev-list --count origin/main..HEAD` → **0**; `git rev-parse origin/main` →
  `7c4e589…` (same commit). Work is pushed.
- Tracked diff: `git diff --stat` and `git diff --cached --stat` both **empty**.
- Untracked: `git status --porcelain=v1` → **1 entry**, `?? reports/round-107/`;
  `git status --porcelain --untracked-files=all | wc -l` → **79** files, `du -sh
  reports/round-107` → **988K**. This is the "1 uncommitted change" named in the assignment:
  **`reports/round-107/` — report it, never touch it.**
- Tracked files: `git ls-files | wc -l` → **23,448**.

## 1. Identity

| field | value | evidence |
|---|---|---|
| lane id | `game-dev-3d` | fleet `MANIFEST.json` roster entry |
| repo directory | `game-dev-3d-shokunin` | this checkout |
| repo name (fleet) | `shokunin-3d-engines` | `MANIFEST.json` roster `repo` |
| rank | **shonen** (probation; never promoted) | `MANIFEST.json` roster `rank`; `SHONEN.md` present |
| minted | `2026-10-11` (fleet) vs `2026-10-13` (lane) — **conflict** | `MANIFEST.json` `minted`; `corpus/README.md:3-4` "minted 2026-10-13" |
| domain | 3D game production verified by executable headless fixtures; Godot / three.js / Unity / Unreal; REA static inspection as supporting evidence | `PROVINCE.md:1-12`; `SKILL.md` frontmatter |
| owned axes | depth, coverage, calibration | `SCORECARD.md:3` |
| last **admitted** round | **106** (interrupted round, closed on verified subset) | `SCORECARD.md:337`; LOG bullet `ROUND 106` (LOG.md:1494+); commits `4755b0e` (work) + `3ea02ff` (report-last) |
| round 107 | **aborted, not admitted**: only `reports/round-107-aborted-swarm/r107-planner.md` (10 lines) is committed; 79 shard files untracked; no LOG or SCORECARD entry | `git show --stat HEAD`; `git status`; `grep -c '107' LOG.md` → 5 mentions, none a round entry |
| next round number | **107** (r107 never entered the ledger; `.ufo/state/game-dev-3d.round` = `1`, a fleet-side counter reset — unusable) | `cat .ufo/state/game-dev-3d.round` → `1` |
| SHONEN boxes | **1 checked / 3 unchecked** (`[x]`→1, `[ ]`→3) | `grep -c '^\- \[x\]' SHONEN.md`; `grep -c '^\- \[ \]' SHONEN.md` |

**Fleet ledger check (assignment hint "max recorded round 73").** Confirmed against the fleet
file and contradicted by the lane: `python3 -c "…[r for r in MANIFEST['rounds'] if
r['lane']=='game-dev-3d']"` → **[70, 71, 72, 73]** (4 entries). The lane's own records run to
106. `.ufo/reports/` carries lane reports for rounds 70–79 and 83–85 (13 files:
`grep -rl 'game-dev-3d' .ufo/reports/*/*.md | wc -l`), so the fleet's own artifacts exceed its
ledger. The hint is the fleet ledger's truth, not the lane's: **lane N = 106 admitted, 107
aborted; fleet N = 73 recorded.**

## 2. Axes

`SCORECARD.md` keeps the mint table (lines 6–10) and appends per-round verdict tables from
r72 onward. The table is **unscored** and stale; the verdict stream is current.

| axis | recorded score | last-change in table | latest recorded verdict | evidence pointer |
|---|---|---|---|---|
| depth | `unscored` | **r71** | r106: **improved** | `SCORECARD.md:8`, `:342` |
| coverage | `unscored` | **r68** | r106: **improved (bounded)** | `SCORECARD.md:9`, `:341` |
| calibration | `unscored` | **r61** | r106: **improved (bounded)** | `SCORECARD.md:10`, `:343` |

- **No numeric score was ever assigned.** The mint line says: "Scores remain unassigned without
  a quality rubric; a row count is a measurement, not a score or verdict." (`SCORECARD.md:2-4`).
  The `AXES.md` SCORECARD contract requires "score 0–10 + evidence pointer … or
  `unprovable-but-better` + named non-author reviewer" (`AXES.md` table, §SCORECARD.md contract).
  This lane satisfies neither branch: **0 of 3 axis rows carry a contract-conforming state**.
- **Lowest non-retired axis: formally undefined** (no scores exist, so "lowest" cannot be
  computed). For the proposed round I treat **calibration** as the de facto lowest: it is the
  only axis whose *measurement infrastructure is absent* (`corpus/QUALITY.md` missing, no
  scores, no saturation line, no capabilities rows), while depth and coverage have live,
  growing evidence streams. A round claiming calibration is therefore safe against either
  reading of the obligation; a round claiming only depth/coverage would be indefensible until
  scores land.
- **Saturation line: not declared.** The placeholder reads "The lane's saturation line and
  stagnation window N are to be declared by the lane on its next round per `AXES.md` §The
  stagnation nudge; not asserted by this conformance change." (`SCORECARD.md:283-285`). 20+
  rounds have landed since; still absent.
- **Capabilities: 0 rows.** `SCORECARD.md:277` reads `| — none yet — |`. Under `AXES.md`, rows
  enter only through a round demonstrating the capability running; rounds 101–106 demonstrate
  runnable capabilities (a fail-closed close-out gate PASS; the pinned-env full battery
  PASS), so "none yet" is stale rather than true.
- **Planned claims: stale, two generations.** `SCORECARD.md:12` still says "planned: r72
  (devin, ADMIT) — pdd strict-Euclidean waypoint-pop…"; `SCORECARD.md:13-18` carries the r73-ish
  next-move list ("planned: depth — rendering/GPU behavior, navigation mesh baking,
  multiplayer/replication, orthographic boundary precision …"). The real current queue is
  `reports/round-106/next-iteration-carry.md` ("r107–r139"), which is a report, not the
  SCORECARD `planned` field.
- **Saturation/unprobed ground the lane itself names** (`SCORECARD.md:13-18`): rendering/GPU,
  navmesh baking, multiplayer/replication, orthographic precision beyond one near=1 and one
  far=10 sample, general slope sliding and friction, untouched initial grounded flag/general
  jump controller, further solver regimes; Unity/Unreal executables, production-project launch,
  broad PackedScene, GUI/viewport, export templates, non-Linux platforms; no same-step slope
  contact telemetry or floor-angle sweep.

## 3. Corpus

All counts are reads of the current tree.

| measure | count | command |
|---|---|---|
| knowledge markdown files | **26** | `find corpus/knowledge -name '*.md' \| wc -l` |
| knowledge entry/provenance docs (flat 3 + `unreal-mcp` README/PROVENANCE/adaptation) | **6** | listed by `ls corpus/knowledge; ls corpus/knowledge/unreal-mcp` |
| entry docs opening with `source:` | **0 of 6** | `grep -c '^source:'` per file → 0 each |
| with `verified-at:` | **0 of 6** | `grep -c '^verified-at:'` → 0 each |
| with `recheck:` | **0 of 6** | `grep -c '^recheck:'` → 0 each |
| executability cards | **13** | `find corpus/knowledge/unreal-mcp/executability -name '*.md' \| wc -l` |
| pinned upstream files | **12** | `find corpus/knowledge/unreal-mcp/upstream -type f \| wc -l` |
| lesson markdown files | **92** | `find corpus/lessons -name '*.md' \| wc -l` |
| lessons named `round-<N>.md` (contract form) | **0** | `find corpus/lessons -name 'round-*.md' \| wc -l` |
| lessons named `r<N>-<slug>.md` | **92** | `find corpus/lessons -name 'r*-*.md' \| wc -l` |
| lessons carrying a `## Gate` section | **0** | `grep -lE '^## Gate' corpus/lessons/*.md \| wc -l` |
| lessons containing capital-`Gate` at all | **0** | `grep -rc 'Gate' corpus/lessons/*.md \| grep -v ':0' \| wc -l` |
| lessons containing lowercase "gate" anywhere | 21 | `grep -rli 'gate' corpus/lessons/*.md \| wc -l` |
| `corpus/QUALITY.md` | **missing** | `ls corpus/QUALITY.md` → rc 2 |
| `corpus/SOURCES.md` | **missing** | `ls corpus/SOURCES.md` → rc 2 |
| coverage-map rows in `corpus/README.md` | **0** | `grep -c 'Frontier' corpus/README.md` → 0; only `## Correction note` is level-2 |
| `## Frontier` rows in `corpus/README.md` | **0** | same |
| `PROVINCE.md` Core/Frontier/Adjacent sections | **0** | `grep -ciE 'core\|frontier\|adjacent' PROVINCE.md` → 0 |
| tracked fixture files | **147** | `git ls-files corpus/fixtures \| wc -l` |
| registered battery CASES | **350** | `grep -cE '^\s+\("' corpus/fixtures/run_battery.py` → 350 |
| battery receipt rows | **350** (291 ordinary / 59 negative controls), verdict PASS, `seeds_unchanged=true` | Python read of `reports/round-105/n24/runs/node24-full-rerun-20261018T204240Z.verdicts.json`: `len(results)`=350, `Counter(kind)`=291/59 |
| `run_battery.py` identity | sha256 `f456bd00a1f7cc6f68d0dd64ff0994d354a7568ef5f34d0cb044209dab1ef69f`; git blob `dd2d9b74448afddb88dcf2da56008302eba8060d` | `sha256sum`; `git hash-object` |
| artifact/predecessor/knowledge/lessons/fixtures sizes | 100K / 160K / 592K / 972K / 34M | `du -sh corpus/{artifacts,predecessor,knowledge,lessons,fixtures}` |
| `corpus/live` | **1.7G** (gitignored; `corpus/live/runs` = 1.7G) | `du -sh corpus/live corpus/live/*` |
| `reports/` | **456M** | `du -sh reports` |
| `reports/round-104` | **410M**, **21,950 tracked files** (physics subtree 15,495) | `du -sh reports/round-104/*`; `git ls-files reports/round-104 \| wc -l`; `git ls-files reports/round-104/physics \| wc -l` |
| `LOG.md` | 278K, 1,500 lines | `wc -lc LOG.md` |
| `SCORECARD.md` | 52K, 345 lines, 30 round-verdict blocks | `wc -lc SCORECARD.md`; `grep -cE '^## Round [0-9]+ verdict' SCORECARD.md` |
| unique external URLs in `corpus/knowledge/*.md` + `SKILL.md` + `PROVINCE.md` | **2** (EpicGames repo, prymeagnt-games-engine-mechanics) | `grep -rhoE 'https?://[^ )|]+' … \| sort -u \| wc -l` |

**Freshness assessment.** "Overdue `recheck:` before 2026-10-19" is not assessable: no
knowledge doc carries a `recheck` field (0/6). Missing-field census is therefore **6/6 missing
all three fields**, not an overdue subset. The newest provenance work is inline and dated
(`corpus/knowledge/engines.md` correction note 2026-10-18; `stat -c %y` → 2026-10-18 22:24).

**Coverage map and frontier live outside the contract location.** Five frontier docs exist
(`reports/frontier/`: `fa-bpy-evalcat.md`, `fb-physserver.md`, `unknowns-map.md`,
`bpy-boundary.md`, `navagent-dissection.md`; 96K) but `corpus/README.md` has no `## Frontier`
and `PROVINCE.md` has no Core/Frontier/Adjacent structure. The knowledge is real; the index the
contract requires is absent.

**Count drift inside the corpus.** `corpus/fixtures/README.md:5` says "later rounds extend the
battery to 235 registered cases (189 ordinary and 46 negative controls)" — stale by 115 rows.
The runner has 350 CASES (`grep -cE '^\s+\("'`), and the r105 pinned-env receipt has 350 rows
(291 ordinary / 59 negative). The stale count is in a fixture **doc**, which the r103 ruling
classified as repairable (fixture code is pinned; docs are not).

## 4. Mistakes

Mistake classes mined from LOG, SCORECARD, reports, and commits. "QUALITY captures?" is
uniformly **no**: `corpus/QUALITY.md` does not exist (`ls` rc 2), so no criterion exists in the
lane's corpus. "SKILL captures?" is a measured keyword sweep over `SKILL.md` (count per term).
A `0` means the term never appears; a low count is quoted with its actual context.

| # | class | evidence pointer | QUALITY | SKILL sweep | proposed criterion (none exists today) |
|---|---|---|---|---|---|
| M1 | **verifier REJECT left unadjudicated and unrecorded** — r90 verifier returned a round REJECT (bimodal cell + third crash class); repair landed (`6420dc7`) but no adjudicator; SCORECARD commit says skip | `reports/round-90/r90-verifier.md` table row "Round verdict \| **REJECT**"; `reports/round-90/r90-repair.md`; commit `cbc52eb` message "r90/r91 skipped (no adjudicator yet)" | no | `bimodal`=0, `teardown`=0 | A rejected round re-enters only through a recorded adjudication naming the verifier's counterexample and the repair receipt. |
| M2 | **dead-seat salvage admitted without verifier** — r91 author seat records a dead dispatched author and rewrote the fixture; commit lands 235 rows; no verifier/adjudicator, no LOG/SCORECARD entry | `reports/round-91/r91-author.md` "Seat completion note … dispatched author died"; only 2 files in `reports/round-91/`; commit `b6ba234` | no | `dead-seat`=0 | Salvage work carries a non-author replay before it is admitted; otherwise it lands `unverified`. |
| M3 | **sampling inside a physics callback** — r92 verifier FAILED pre-fold; timing delta leaked 0.016667 vs 0.166667 when a callback batched into the same iteration | `SCORECARD.md:213` ("verifier FAILED pre-fold … re-anchored timing to iteration boundary + settled ticks") | no | `iteration`=1 (only "Next-iteration hooks"), `scheduler`=0, `timing`=0 | Fixtures sample engine state at the iteration boundary with N settled ticks, never inside a physics callback. |
| M4 | **contention flake** — r94 cannon accumulator cells flip ~1% under load via the engine's 16.67 ms wall-bail | `SCORECARD.md:233` (r94 calibration row: "accumulator cells flip ~1% under contention") | no | `contention`=0 | Any wall-clock-bounded engine cell gets a load envelope and is excluded from exact-signature pins or pinned with tolerance. |
| M5 | **teardown partial-line race** — r95 SHM `d`-count moved across four independent seats at teardown; M-surface never moved | `SCORECARD.md:241` (r95 calibration row: "SHM `d`-count race … teardown partial-line prints") | no | `teardown`=0 | Child output read at teardown must be drained deterministically or enveloped; partial-line output never pins a value class. |
| M6 | **load-dependent engine API null** — r99 `clsloop` `ClassDB.instantiate` returned null under load (`made=360/beq=0` vs pin) | LOG `ROUND 99` bullet ("clsloop ClassDB.instantiate null under load") | no | `load` not a swept term; `contention`=0 | A ClassDB/reflection cell states its load class; cells that flip under load are not pinned as constants. |
| M7 | **gate false-pass classes** — r102's first gate landing accepted 11 attack classes (symlinks, extra card, substring labels, CRLF manifests, unread shards, shadowed tools) | LOG `ROUND 102` ("11 false-pass classes on the first landing … 11/11 attacks now DETECTED") | no | `green-gate-overread` present (1 named pattern) | Partial: the pattern warns against overreading green; add "no gate lands without an adversary suite" as a rule, since it exists only in the lesson/LOG. |
| M8 | **verdict raced a stale intermediate** — r103 attack verdicts ran against a 249-line intermediate while the final gate was 347 lines; ruling: pin the target hash | LOG `ROUND 103` LAWS ("falsification verdicts must name the target's hash") | no | `stale`=0 | Every falsification/verification verdict records the target's sha256; a verdict without it is void. |
| M9 | **protected-vs-repairable fixture ambiguity** — r103 edited a fixture README while the template marked `corpus/fixtures/**` protected; ruled a template defect | LOG `ROUND 103` "CONFORMANCE DEFECT (recorded, ruled accepted)" | no | `protected`=0 | Round templates distinguish fixture CODE (pinned) from fixture DOCS (repairable) explicitly. |
| M10 | **documented override not implemented** — r104 found a documented `REPO` override that the script did not implement | LOG `ROUND 104` LAWS ("A documented override that the code does not implement is a defect class") | no | `override`=0; `command-does-not-reproduce-its-printed-rc` is adjacent | A documented override is grepped for in the script before the doc cites it. |
| M11 | **concurrent writer corrupts a running battery** — r105's first pinned-env full run failed `seeds_unchanged=false` because another seat wrote a fixture mid-run; second sighting | LOG `ROUND 105` LAWS ("mid-run seed change means a concurrent WRITER"); SCORECARD r105 depth row | no | `concurrent`=0, `write-isolation`=0 | Batteries run against a write-isolated snapshot; a concurrent-write FAIL is infrastructure, not a row failure. |
| M12 | **provider exhaustion mid-round** — r106 lost xai credits at 47/128 then Cursor Pro rate limits; closed as interrupted on the verified subset | `SCORECARD.md:337-343`; LOG `ROUND 106` | no | `provider`=0, `rate limit`=0 | Interrupted rounds close on a verified subset with the exhaustion named and the remainder routed; retry-inflated agent counts never read as seats. |
| M13 | **wrong-cwd swarm spawn** — r107 side-round swarm spawned in the wrong cwd; shards were relocated, unvalidated, and not admitted; 79 untracked files remain | HEAD commit `7c4e589`; `git status --untracked-files=all` → 79 | no | `wrong-cwd`=0; `implicit-cwd command` is adjacent (quoted-command class, not spawn cwd) | A swarm's first acceptance check is its resolved cwd; a spawn outside the lane root is a process defect, not a seat. |
| M14 | **known corpus-conformance gap never repaired** — r104 recorded there is no `corpus/QUALITY.md` and no lessons index; still true at HEAD | `reports/round-104/lessons-carry.md:81` ("There is **no `corpus/lessons/README*` and no `corpus/QUALITY.md`**") | n/a (the bar is the missing file) | `QUALITY`=0 occurrences in SKILL.md | The admission bar is a required artifact; a recorded absence is scheduled, not carried indefinitely. |
| M15 | **count written into prose, unapplied** — fixtures README still says 235 cases vs 350 measured | `corpus/fixtures/README.md:5`; runner count command above | no | `count-written-into-prose` present (1 named pattern) | Captured as a rule, not applied: fixture docs get the same count sweep as prose. |

**Count: 15 mistake classes.** Two (M7, M15) are partially captured by SKILL patterns; M10 is
adjacent to a pattern; the rest have **no** rule in `SKILL.md` and none anywhere in
`QUALITY.md` (absent). The pattern registry is also Unreal/gate-weighted: of 8 named patterns,
7 concern pointer/count/cwd/temp-dir/gate/string/rc discipline, none concerns the physics
battery, scheduler sampling, contention, teardown, or provider death — the classes this lane
actually hit most.

**Honest-stop / rejection record quality.** Rejections exist and are detailed where reports
exist (r90 REJECT; r92 pre-fold FAIL; r94/r95 findings; r98 clobber disclosure; r102 attacks),
but the *ledger* does not carry them: no LOG or SCORECARD entry for r90/r91; r99/r100 have
adjudicators but no SCORECARD verdict block.

## 5. Contract defects

Ordered by blast radius. "Owner" is my recommendation, not an assignment.

| # | defect | evidence (command/quote/location) | owner |
|---|---|---|---|
| D1 | `corpus/QUALITY.md` absent — the admission bar, and the file every future knowledge entry must clear | `ls corpus/QUALITY.md` → rc 2; known since `reports/round-104/lessons-carry.md:81` | lane + wave-2 writer |
| D2 | `corpus/SOURCES.md` absent — the new curated source registry | `ls corpus/SOURCES.md` → rc 2 | wave 2 |
| D3 | no knowledge entry opens with `source:` / `verified-at:` / `recheck:` (0/6 docs) | per-file `grep -c` → 0/0/0 | lane |
| D4 | no lesson carries `## Gate` (0/92), and the naming convention `round-<N>.md` is unmet (0/92; all are `r<N>-<slug>.md`) | `grep -lE '^## Gate' corpus/lessons/*.md \| wc -l` → 0; `find -name 'round-*.md'` → 0 | lane |
| D5 | `corpus/README.md` has no coverage map and no `## Frontier`; frontier content lives in `reports/frontier/` | `grep -c Frontier corpus/README.md` → 0 | lane |
| D6 | `PROVINCE.md` has no Core/Frontier/Adjacent structure, and its write scope points at a nonexistent root: "Only writes `.shokunin/game-dev-3d/**` and its own reports." (`PROVINCE.md:46`); sources line `PROVINCE.md:25` is the same dead root | `ls -d .shokunin` → rc 2; `grep -ciE 'core\|frontier\|adjacent' PROVINCE.md` → 0 | lane |
| D7 | `README.md` advertises a missing file: "`QUALITY.md` (the admission bar)" (`README.md:16`) | `grep -n QUALITY README.md`; file absent | lane |
| D8 | SCORECARD axes are `unscored`, table `last change` frozen at r71/r68/r61 while verdicts continue to r106; `planned:` frozen at r72 | `SCORECARD.md:8-12` | lane |
| D9 | saturation line/`N` never declared; capabilities table still `— none yet —` after runnable capability rounds | `SCORECARD.md:275-285` | lane |
| D10 | SCORECARD verdict ledger incomplete/malformed: 30 blocks vs rounds 72–106 (missing 90, 91, 99, 100; r92 only an inline row with columns `r92 \| improved \| improved \| improved \| text` instead of lane/subject/verdict/commit; 87 block precedes 85/86; rounds 81/82 dated **2026-11-01**, in the future) | `grep -cE '^## Round [0-9]+ verdict'` → 30; `sed -n '213p'`; `grep -n '2026-11-01'` → lines 109,119 | lane |
| D11 | LOG has no round 90 or round 91 entry and no r107 abort entry; last entry is ROUND 106 | `grep -nE 'ROUND 9[01]'` → none; `wc -l LOG.md` → 1500 | lane |
| D12 | fleet ledger drift: `MANIFEST.rounds` has 4 lane entries [70–73] vs 106 admitted; `.ufo/state/game-dev-3d.round` = `1`; `.ufo/reports` has 13 lane reports (70–79, 83–85) | Python count; `cat .ufo/state/…`; `grep -rl` | operator/fleet |
| D13 | dead `.shokunin/game-dev-3d` root in **306 tracked files** — 231 `reports/`, 72 `corpus/`, 1 each SCORECARD/PROVINCE/LOG; **live** instances: 3 in SCORECARD axis commands, 2 in PROVINCE, 4 fixture files in runnable header comments (7 lines) | `git grep -l '\.shokunin/game-dev-3d' \| wc -l` → 306; `git grep -l … \| cut -d/ -f1 \| sort \| uniq -c`; `git grep -n … -- corpus/fixtures` → 7 lines | lane (r106 sweep remainder) |
| D14 | bloat: `reports/round-104` = 410M / 21,950 tracked files (physics 15,495); `reports` total 456M; `corpus/live` 1.7G ignored; `corpus/fixtures/three/node_modules` 23M ignored; fixtures 34M | `du -sh`; `git ls-files … \| wc -l` | lane + operator (history) |
| D15 | untracked round material: `reports/round-107/` 79 files / 988K, explicitly unvalidated and unadmitted by the HEAD commit; duplicated by the committed `reports/round-107-aborted-swarm/` | `git status --porcelain --untracked-files=all \| wc -l` → 79; `du -sh reports/round-107` → 988K; `git show --stat HEAD` | operator (do not touch from this wave) |
| D16 | fixture doc count drift: "235 registered cases (189 ordinary and 46 negative controls)" vs 350 (291/59) | `corpus/fixtures/README.md:5`; runner count 350; receipt Counter 291/59 | lane |
| D17 | identity date conflict: fleet `minted` 2026-10-11 vs lane "minted 2026-10-13" | `MANIFEST.json`; `corpus/README.md:3-4` | operator/fleet |

**State facts that are not defects but shape the dossier:** rank is still `shonen` with one of
four promotion boxes checked (`SHONEN.md`); the lane is a *leaf* member with no subagent
dispatch in this wave; work tree is otherwise clean and pushed.

## 6. Proposed round — 3 claims

**Design note.** Every claim is measurable with a command that exists today; no claim depends on
another landing; the calibration claim is the lowest-axis claim under the only defensible
reading (no scores → calibration has no measurement infrastructure at all). Claims 1–2 serve
`SOURCES.md` and the new knowledge entries directly; claim 3 produces the first entry admitted
through the new bar. All three are `improved` candidates with `harmed` checked per axis.

### Claim 1 — calibration: restore the self-assessment and admission layer

*Target axis:* calibration (de facto lowest). *Claim:* the lane lands `corpus/QUALITY.md`
(≥8 criteria, each citing a lesson and carrying a recheck command), replaces the three
`unscored` axis rows with contract-conforming states (score + evidence pointer, or
`unprovable-but-better` + named non-author reviewer), declares the saturation line and
stagnation window `N`, adds ≥2 capability rows with demonstrated commands, and records the
five missing verdict blocks (90, 91, 99, 100, and r92 as a block) **from existing reports,
without re-running anything**.

*Before → after (commands):*
- `test -f corpus/QUALITY.md; echo $?` → **2 → 0**
- `grep -cE '^\| Q[0-9]+' corpus/QUALITY.md` → **0 (file absent) → ≥8**
- `grep -cE '^\| (depth|coverage|calibration) \| unscored \|' SCORECARD.md` → **3 → 0**
- `grep -cE '^## Round [0-9]+ verdict' SCORECARD.md` → **30 → 35**
- `grep -c '^Saturation line:' SCORECARD.md` → **0 → 1**
- `sed -n '/^## Capabilities/,/^## Saturation/p' SCORECARD.md \| grep -cE '^\| [a-z0-9-]+ \|'` (capabilities rows) → **0 → ≥2**

*Falsifiers:* any axis row left `unscored`; a criterion with no lesson pointer; a capability
row without a round demonstration; a verdict block whose content does not match its source
report (r90 must record **REJECT**, not an admit, unless an adjudicator lands).

### Claim 2 — coverage: the "where to learn more" registry and entry provenance

*Target axis:* coverage. *Claim:* `corpus/SOURCES.md` lands with ≥15 tiered rows (contract
table: id/source/kind/tier/teaches/status/opened/recheck/used-by), the six entry docs gain
`source:`/`verified-at:`/`recheck:` openings, `corpus/README.md` gains a coverage map and a
`## Frontier` section fed from `reports/frontier/`, and `PROVINCE.md` gains Core/Frontier/
Adjacent headings with the write scope corrected to this repo.

*Before → after (commands):*
- `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md` → **0 (file absent) → ≥15**;
  tiers via `… \| awk -F'|' '{gsub(/ /,"",$5); print $5}' \| sort \| uniq -c`
- `grep -lE '^source:' corpus/knowledge/*.md \| wc -l` → **0 → 3** (flat entries); the
  `unreal-mcp` provenance docs → **3 more**
- `grep -cE '^## (Coverage map|Frontier)' corpus/README.md` → **0 → 2**
- `grep -cE '^## (Core|Frontier|Adjacent)' PROVINCE.md` → **0 → 3**

*Falsifiers:* a row listing a source not opened (leads go under `## Leads (unopened)`, never
as rows); a `teaches` line not grounded in what was read; any `|` inside a cell.

### Claim 3 — depth: the 45° floor-angle boundary, sampled adjacently

*Target axis:* depth (the lane's own unprobed list names "general slope sliding and friction"
and "no same-step slope contact telemetry or floor-angle boundary sweep"). *Claim:* on Godot
4.7.2 headless, an adjacent 44.9°/45.1° pair at `floor_max_angle=45` discriminates on-floor
from wall-contact with same-step contact telemetry and a measured slide distance, on
GodotPhysics3D and Jolt; two new CASES rows, prior 350 rows byte-identical, `run_battery.py`
unchanged.

*Before → after (commands):*
- `grep -cE '^\s+\("[^"]+", "slope3d_angle\.gd"' corpus/fixtures/run_battery.py` → **2 (floor,
  steep at 30°/60°) → 4**
- `grep -cE '^\s+\("' corpus/fixtures/run_battery.py` → **350 → 352**
- receipt: 352 rows, verdict PASS, `seeds_unchanged=true`, prior-row comparison 0 mismatches

*Falsifier:* 44.9° must read `on_floor=true` and a nonzero downhill displacement; 45.1° must
read `on_floor=false`/`on_wall=true`; if both sides read the same, the claim is false and the
round reports the boundary as unmeasured. The fixture change targets `slope3d_angle.gd`
(fixture **code**, so the round carries a non-author replay per row F of `SKILL.md`).

**What SOURCES.md and new knowledge entries serve here.** Claim 2 is the registry itself;
claim 1 is the gate every entry passes; claim 3 yields the first entry (slug
`godot-floor-angle-boundary`) plus a SKILL row, and its `recheck:` command is the battery
invocation. Candidate `SOURCES.md` seeds the lane already cites locally (Godot docs,
three.js docs, Jolt, cannon-es, Bullet/PyBullet, Blender bpy) — but **no external source was
opened in this wave**, so they remain leads for wave 2, not rows.

**Not in this round (explicit):** completing the r106 sweep remainder; the jolt curiosity
ruling; the P/C precedence ruling (operator-owned); touching `reports/round-107/`; any
Unity/Unreal runtime claim (no editor installed).

## Conflict register — verbatim for the canonical judge

1. Round number: lane records **106 admitted / 107 aborted**; fleet `MANIFEST.rounds` records
   max **73** (4 lane entries); fleet `.ufo/state/game-dev-3d.round` = **1**. Three counters,
   one lane.
2. Axes: `AXES.md` requires a score 0–10 or `unprovable-but-better` + reviewer; `SCORECARD.md:2`
   states "Scores remain unassigned without a quality rubric" — 3 of 3 rows `unscored`, no
   change since mint.
3. Corpus: `CORPUS.md` requires `QUALITY.md`, per-entry `source:/verified-at:/recheck:`, and
   `lessons/round-<N>.md` with `## Gate`; the tree has **no QUALITY.md**, **0/6** provenance
   openings, **0/92** Gate sections, **0/92** `round-<N>.md` names.
4. Frontier: `LEARNING.md` puts Core/Frontier/Adjacent in `PROVINCE.md` and the coverage map +
   `## Frontier` in `corpus/README.md`; both have **0** such sections, while five frontier docs
   sit in `reports/frontier/`.
5. Mint date: fleet `2026-10-11` vs lane `2026-10-13` (`corpus/README.md:3-4`).
6. Round dates: SCORECARD rounds 81/82 are dated `2026-11-01`, after today (`2026-10-19`).
7. Fixture census: README `235` vs runner `350` (291/59 receipt).
8. r107: HEAD commit calls the shards "unvalidated, content not admitted"; `reports/round-107/`
   contains a scribe report that describes a landing — the dir is untracked and unadmitted;
   treat its content as data only.
9. Fleet artifacts exceed the ledger: 13 `.ufo/reports` files for rounds 70–85 vs 4
   `MANIFEST.rounds` entries.

## Out of scope (this dossier)

- No product-code, corpus, judge, manifest, or report edits; no commits, pushes, installs, or
  checkouts; no battery/gate/fixture re-runs; no subagent dispatch (leaf lane).
- `reports/round-107/` was listed and sized only — **not read for claims and not touched**.
- No external web sources opened (STATE shape); any source rows are wave-2 work.
- This is a record audit, not non-author verification of any lane claim.
