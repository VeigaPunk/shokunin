# kaika W1 — STATE dossier: `mado` (desktop & compositor craft)

- Author: W1StateMado (revenger seat; read-only; leaf member, no dispatch).
- Measured: 2026-10-19, window ending 21:14:06Z (`date -u`).
- Repo: `/home/vgpnk/Projects/shokunin/mado-shokunin` @ `e1d81d48026b6b9c9e9614c3b6390240200110db`.
- Commands run from the lane root unless another path is shown.
- Web: not used. A STATE dossier needs only local evidence; `web_search` was available.
- Writes: this file only.
- Gate runs: the lane gate ran in its two verdict modes, `--no-live` and the default live mode. Its header says it is read-only and writes no file: "no file is written; scratch lives under /tmp/w5-mado-m52-* and only --selftest makes it" (`tools/mado-verify.sh:23-24`).
- Not run: `--selftest` and `--regression`, because both write /tmp scratch.
- Prompt injection: none seen. `.ufo/prompts/mado-round-1.md` (fleet root) and `~/Projects/gkeep/install.sh` were read as data only.

## 0. Headline

1. **The lane's own gate now reports DIVERGED.**
   - File plane: `counts: pass=28 fail=1 unknown=0 skip=8 note=4`.
   - Live: `counts: pass=51 fail=1 unknown=0 skip=0 note=8`.
   - The single FAIL in both is `hypr.root.include_graph — 18 source lines (expected 17)`.
   - On 2026-10-15 the file plane read `MADO_VERIFY: CLEAN (29 pass, 4 notes …)` (`.ufo/evidence/fleet-round-1/file-plane.txt`; `SCORECARD.md:122`).
2. **The cause has a full provenance chain.** The operator project `~/Projects/gkeep` ran its installer on 2026-10-17. It changed two files:
   - It appended `source = ~/.config/hypr/gkeep.conf` to `hyprland.conf` (`install.sh:21-36`).
   - It inserted a `custom/gkeep` waybar module and css snippet (`install.sh:60-82`).
   - Both backups carry the stamp `.bak.1792267376` = 2026-10-17T20:02:56Z (`date -u -d @1792267376`).
   - Each backup is byte-equal to the lane's recorded pin: hypr `4f52854a3c143dcf`, waybar `07f7d663106b72e4`.
3. **The gate catches the hypr drift with only one row and misses the rest.**
   - `sources_resolve` and `local.inventory` iterate pinned lists only (`tools/mado-verify.sh:2229-2238`, `:2249-2256`). The new 13th local conf passes unseen ("12/12 active local confs").
   - The count-mismatch branch does not name the added line (`:2211-2212`).
   - The waybar module set is not pinned. A module was added and no row moved.
4. **Ledger state:**
   - Last admitted round = 11 (2026-10-14, `bb08dd5`). The fleet `MANIFEST.json` maximum for mado is also 11, but the ledger has no round-1 entry.
   - "Fleet round 1" (2026-10-15) is LIVE, blocked and unadmitted (+0). Its report sits in the lane `.ufo/`, not at the fleet path its prompt required.
   - Recommended next round: **N = 12** (§1.2).
5. **The lowest non-retired axis cannot be determined from the committed SCORECARD.**
   - Only two sub-axes carry scores, and both read 10.0000 today. Four axes are unscored, the capabilities table is empty, and no saturation line is declared.
   - Measured contract rubrics point to two weak axes:
     - Calibration: 0 of 5 `QUALITY.md` criteria cite a lesson.
     - Freshness: 3 of 22 knowledge entries carry the `source:`/`verified-at:`/`recheck:` triple, and the gate reports DIVERGED.
6. **Mistakes mined: 14 classes** (§4).
   - The lane `QUALITY.md` captures none of them beyond the generic "measured anchor" rule. It has 5 criteria, is still headed "probation draft", and cites no lesson.
   - Closeout findings F1–F4 are still owed.
   - The `…a5171` hash corruption has grown from 34 occurrences in 13 files to 52 in 17.
7. **The fleet ledger inflates mado's verdicts.** 28 of 45 MANIFEST "improved" verdicts for mado rounds 2–11 sit on axes the lane's own SCORECARD never claimed (§2.2).

## 1. Identity

### 1.1 Facts

| Field | Value | Evidence |
|---|---|---|
| Domain | desktop & compositor craft — Hyprland/waybar/walker config plane + display behavior on this host | `PROVINCE.md:3-4` |
| Owned surfaces | `~/.config/hypr/`, waybar, walker, alacritty/foot/kitty/ghostty configs, themes/wallpapers as declared files, hypridle/hyprlock; omarchy skill = read-only docs; all config trees READ-ONLY | `PROVINCE.md:6-12`; 9/9 declared paths exist (existence loop, Appendix A) |
| Refuses | secrets (→ kagi), model endpoints (→ kama), model quality (→ kengaku); never mutates running compositor | `PROVINCE.md:14-16` |
| Rank | shonen. Roster: 0 of 13 rows are mado (withheld by design until the operator adds one) | `SKILL.md:3` "Rank: shonen (probation)"; MANIFEST roster count (Appendix A); mint note "roster row withheld" (MANIFEST rounds[], mado mint entry) |
| Promotion checklist | 4× `[~]`; the historical 4× `[x]` (commit `c03c249`) was superseded at `7cd7f33` | `SHONEN.md:5-12`; `SCORECARD.md:39-42` |
| Driver lane axes | `coverage + operability` | fleet `shokunin.conf:56` |
| Branch / HEAD | `master...origin/master`, clean; HEAD `e1d81d4` (2026-10-17 00:29:06 −03:00, "mado: ignore interactive session logs") | `git status --porcelain=v1 -b`; `git log -1 --format='%H %ci' e1d81d4` |
| Commits / identity | 18 commits — `git rev-list --count HEAD`; 1 author identity `mado-shokunin <mado@shokunin.local>` — `git log --format='%an <%ae>' \| sort -u \| wc -l` | — |
| Last admitted round | **11** (2026-10-14, `bb08dd5`, "THE ARC CLOSES") | `LOG.md:302-438`; `SCORECARD.md:26-30`; `corpus/knowledge/closeout-r11.md` |
| Fleet ledger | mado entries: round 0 (mint) and rounds 2–11 (train); max 11; **round 1 absent** | python over `MANIFEST.json` (Appendix A); `MANIFEST.json:2253,2259` (round 11) |
| After round 11 | fleet round 1 (2026-10-15): **LIVE, blocked, unadmitted, +0 verified rounds**; conformance scaffold 2026-10-16 (`c1b548a`, not a round) | `SCORECARD.md:92-198`; `LOG.md:440-652`; lane `.ufo/reports/round-1/mado.md:3` "BLOCKED before native specialist dispatch. Not a completed or admitted round." |
| Driver state | `.ufo/state/mado.round` = `1`. Watchdog: launch 2026-10-15T01:45:42, `lane-dead-no-report` at 01:50:57, relaunched | fleet `.ufo/state/mado.round`; fleet `.ufo/watchdog.log` (3 mado lines — `grep -c mado .ufo/watchdog.log`) |
| Open L0 question | "Ratify the relaunched round namespace, bounded score rubrics and native craft dispatch shape …" — unanswered | fleet `.ufo/l0-questions.md:37`; only 1 mado line — `grep -c mado .ufo/l0-questions.md` |

### 1.2 Next round number: recommend **12**

| Candidate N | Collision / problem |
|---|---|
| 1 (resume fleet r1) | `corpus/lessons/round-1.md` already holds the fleet-r1 lesson (2026-10-15). Probation round 1 lives at `LOG.md:5-63`. The continuation's blockers belong to a dispatch frame that kaika does not use: routing aliases and the receipt binding (`.ufo/blocked/*.json`). The lane report does say "Do not advance to round 2" (`.ufo/reports/round-1/mado.md:105`), so the parent must rule on this explicitly. |
| 2 | Probation round 2 already exists: `LOG.md:64-158`, `plans/round-2.plan.md`, and a MANIFEST round-2 entry. |
| **12** | Free. 0 lane files match round-12 — `ls plans corpus/lessons \| grep -c round-12`. 0 tracked mentions — `git grep -n 'round-12\|round 12' HEAD -- '*.md' \| wc -l`. 0 mado reports at fleet `.ufo/reports/round-12/` — `ls … \| grep -c mado`. It continues the MANIFEST lane namespace (max 11). |

Disposition for W2 (append-only): add a LOG entry that closes fleet round 1 as *superseded, unadmitted*. Its navigation candidate `7cd7f33` is already on master and re-measures 22/22 at HEAD (§2.1). Its routing and receipt blockers applied only to that dispatch frame. The parent, as judge-of-record, ratifies; L0 `:37` is still open.

## 2. Axes

### 2.1 Scored sub-axes — the only numeric rows (`SCORECARD.md:44-47`)

| Axis / sub-axis | Recorded | Re-measured 2026-10-19 |
|---|---|---|
| coverage / admitted-note reachability | 3.6364 at `bb08dd5` → 10.0000 at `7cd7f33` (candidate, `SCORECARD.md:163-179`) | **10.0000**: `indexed=22/22 missing=0 dangling=0 duplicates=0` at `e1d81d4`, via the SCORECARD counter body with rev = HEAD (`SCORECARD.md:69-90`) |
| operability / hermetic suite pass fraction | 10.0000 = `MADO_SELFTEST: 268/268` (2026-10-15; `SCORECARD.md:47,121`) | Not re-run (writes /tmp). The gate bytes are unchanged: `93e43f8fe8b9bdd4…bc00095`, 3,231 L / 150,103 B — `sha256sum tools/mado-verify.sh; wc -lc tools/mado-verify.sh`. Last gate commit is `de22dfd` — `git log -1 -- tools/mado-verify.sh`. |

The other four axes (depth, freshness, calibration, adjacency) have no score, command or commit. That is an AXES contract defect (`AXES.md:75-83`; D7).

### 2.2 Lane move log vs fleet ledger verdicts

The lane axis column comes from `awk -F'|' '/^\| [0-9]+ \|/{…print $2,$3}' SCORECARD.md`. The fleet column lists the MANIFEST verdict keys equal to `improved` (python, Appendix A).

| Round | Lane SCORECARD axis-moves | MANIFEST "improved" | Manifest-only | Lane-only |
|---|---|---|---|---|
| 2 | depth | depth, operability, calibration | 2 | 0 |
| 3 | depth, coverage | depth, operability, freshness, calibration | 3 | 1 (coverage) |
| 4 | calibration, depth, freshness | depth, operability, freshness, calibration | 1 | 0 |
| 5 | calibration, operability | depth, operability, freshness, calibration, adjacency | 3 | 0 |
| 6 | operability | all six | 5 | 0 |
| 7 | operability, coverage | depth, operability, freshness, calibration, coverage | 3 | 0 |
| 8 | operability, freshness | depth, operability, freshness, calibration, coverage | 3 | 0 |
| 9 | coverage, operability | depth, operability, freshness, calibration, coverage | 3 | 0 |
| 10 | calibration, operability | depth, operability, freshness, calibration, coverage | 3 | 0 |
| 11 | calibration, freshness | depth, operability, calibration | 2 | 1 (freshness) |

Totals:
- 45 MANIFEST "improved" verdicts, of which 28 are manifest-only.
- 19 lane axis-moves, of which 2 are lane-only.

`AXES.md:27-36` makes a round 1–3 claims, each on a named axis. A ledger "improved" verdict with no claim behind it is not a measured verdict. Mistake M14; fleet-level fix for D3 or the parent.

### 2.3 Contract fields

- **Capabilities: 0 rows** (`SCORECARD.md:202-206`, "— none yet —").
  - The record shows at least five capabilities that have actually run:
    - the verdict gate (round 5, `SCORECARD.md:20`)
    - `--selftest` (round 5)
    - `--regression` (round 7, `SCORECARD.md:22`)
    - `--snapshot` / `--snapshot-diff` (round 8, `SCORECARD.md:23`)
    - the omarchy drift arm and theme arms (rounds 8–9, `SCORECARD.md:23-24`)
  - `AXES.md:62-64` admits rows only "through a round that demonstrates the capability running". Running them inside the round is a cheap, honest calibration move.
- **Saturation:** undeclared (`SCORECARD.md:208-210`).
- **Planned:** empty (`SCORECARD.md:212-214`). The last planned prose was the operator routing unblock and resuming r1 (`SCORECARD.md:143-148`); kaika supersedes it.
- **Retired:** none (`SCORECARD.md:216-218`).

### 2.4 Lowest non-retired axis

As committed, it is **indeterminate**:
- The two scored sub-axes are tied at 10.0000, and both are saturated on finite denominators. The SCORECARD itself warns about this (`SCORECARD.md:52-53`).
- Four axes are unscored.
- No saturation line or stagnation window is recorded, so the nudge (`AXES.md:66-73`) cannot be invoked.

Candidate bounded rubrics, measured today. W2 pre-registers the chosen rubrics, baselines, commands and commit in SCORECARD before working.

| Axis | Candidate rubric (lane's own claims as denominator) | Baseline today |
|---|---|---|
| calibration | `QUALITY.md` criteria citing the lesson that produced them (`LEARNING.md:55-57`) | 0/5 → **0.0000** |
| freshness (a) | knowledge entries opening with `source:`/`verified-at:`/`recheck:` (`CORPUS.md:17-18`) | 3/22 → **1.3636** |
| freshness (b) | gate file-plane rows not FAIL/UNKNOWN | 28/29 → 9.6552 |
| coverage | admitted-note navigation (existing) | 22/22 → 10.0000 (saturated) |
| operability | hermetic suite pass fraction (existing) | 268/268 → 10.0000 (recorded; saturated) |
| depth, adjacency | none in the record — W2 defines or declares them unscored with a reason | — |

Counting commands:
- calibration: `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md` → 0; `grep -cE '^[0-9]+\. ' corpus/QUALITY.md` → 5.
- freshness (a): `for f in corpus/knowledge/*.md; do head -n 15 "$f" | grep -q '^source:' && head -n 15 "$f" | grep -q '^verified-at:' && head -n 15 "$f" | grep -q '^recheck:' && echo "$f"; done | wc -l` → 3; `ls corpus/knowledge/*.md | wc -l` → 22.
- freshness (b): `bash tools/mado-verify.sh --no-live | awk '$3=="PASS"' | wc -l` → 28; `… | awk '$3=="FAIL"||$3=="UNKNOWN"' | wc -l` → 1.
- coverage: SCORECARD counter (`SCORECARD.md:69-90`) with `REV=$(git rev-parse HEAD)`.

**Recommendation.** Treat freshness as the lowest axis in observed reality:
- the lane's own instrument reads DIVERGED;
- a present-tense SKILL claim is contradicted (§3.4);
- no entry has been verified since 2026-10-14.

Calibration is the lowest under the contract rubric. The proposed round (§6) works both, so it meets the lowest-axis obligation under either choice.

## 3. Corpus

### 3.1 Counts (each `<n> — <command>`)

- Knowledge entries:
  - 22 — `ls corpus/knowledge/*.md | wc -l`
  - 7,863 L — `cat corpus/knowledge/*.md | wc -l`
  - 522,853 B — `cat corpus/knowledge/*.md | wc -c`
- Lessons:
  - 2 — `ls corpus/lessons` → `round-1.md` (fleet r1, 2026-10-15) and `round-10.md` (training round 10, landed in round 11).
  - Both carry `## Gate` (`round-1.md:9`, `round-10.md:125`).
  - Reject rows in `round-1.md`: 4 — `grep -c '| Reject |' corpus/lessons/round-1.md`.
- `QUALITY.md` criteria: 5 — `grep -cE '^[0-9]+\. ' corpus/QUALITY.md`. Lesson-citing: 0 — `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md`. Header "Admission bar (probation draft)" (`corpus/QUALITY.md:1`).
- Coverage-map rows: 22 — `grep -cE '^\| \`knowledge/' corpus/README.md`.
- Province routes: 7 — awk over `## Province routes` minus the header row.
- `## Frontier` bullets: 5 — `awk '/^## Frontier/{f=1;next} /^## /{f=0} f && /^- /' corpus/README.md | wc -l`.
- `PROVINCE.md` Core/Frontier/Adjacent headings: 0 — `grep -ciE '^(#+ |\*\*)(core|frontier|adjacent)' PROVINCE.md`.
- Gap ledger: 12 named unknowns (`corpus/knowledge/arc-synthesis.md:336-341`).

### 3.2 Coverage map and frontier (what is held)

Coverage-map rows (`corpus/README.md:12-33`), one per note:
- MADO-1/2/3 surveys
- hyprctl live layer
- keybind/rule semantics
- waybar/walker semantics
- e2e health report r3
- executor test
- idle/lock
- province self-audit
- walker-deep, walker-live-surface, walker-deep-r9
- gate-mutation-proof, gate-mutation-sweep-r8
- omarchy drift watch
- remaining-planes census
- theme/wallpaper
- snapshot-diff receipt
- arc synthesis
- gate standing-use
- closeout-r11

`## Frontier` (`corpus/README.md:66-84`):
1. Rendered UI, waybar module text, walker socket protocol, dispatcher behavior, per-window rule effects.
2. Idle/lock transitions and daemon stop-cause.
3. Unlanded theme/walker live rows and mutation/branch coverage.
4. Dated errata and record debt (closeout F1–F5; walker r9 §8).
5. Outside-lane promotion verification.

The gap ledger (`arc-synthesis.md:290-307`) gives the reason for each unknown. Rows relevant to §6:
- "window-rule effects / exec-once results | no rule-read verb in Hyprland 0.56" (`:300`).
- "waybar module text | no IPC/query verb in waybar 0.15.0" (`:301`).

### 3.3 Metadata triple and rechecks

- Entries opening with all three fields: 3/22.
  - They are `arc-synthesis.md:3,7,9`, `closeout-r11.md:3,12,15` and `gate-standing-use.md:3,9,11`.
  - Command: `grep -nE '^(source|verified-at|recheck):' corpus/knowledge/*.md`.
- The other 19 carry none of the three fields anywhere — same grep. They use prose "Probe window:" or "Measured 2026-10-14" openings instead.
- `verified-at` values: all three are 2026-10-14.
- `recheck` values are commands (`sha256sum tools/mado-verify.sh`, the battery, `--regression | tail -1`), not dates. **Overdue by date: 0**, because no dated recheck exists that could be overdue.
- Real staleness is measured against live instead (§3.4).
- Caution for W2: do **not** prepend headers to the 19 legacy notes.
  - That would move every quoted note sha. Examples: `arc-synthesis.md` §1.1 per-note sha prefixes, and closeout freeze pins.
  - The notes declare "earlier text is never edited" (e.g. `walker-deep.md:615-617`).
  - Record the debt instead. New entries open with the triple.

### 3.4 Freshness against live (2026-10-19)

- **Gate:** file plane DIVERGED (28/1/0/8/4); live DIVERGED (51 pass / 1 fail / 0 unknown / 8 note). Full outputs are in Appendix B.
- **hypr root, now:** 32 L / 1,329 B / sha `ce7483f35ab5…`, mtime 2026-10-17 17:02:56 −03:00 (`wc -l`, `stat`). The recorded pin is 29 L / 1,273 B / `4f52854a3c14…`.
  - 18 `source` lines — `grep -c '^[[:space:]]*source' ~/.config/hypr/hyprland.conf`.
  - The last include is `~/.config/hypr/gkeep.conf` at `:32`, after `ai-usage.conf` at `:29`.
  - `diff` against `hyprland.conf.bak.1792267376` shows only lines 30–32 added.
  - `gkeep.conf` is 264 B with three `windowrule =` lines. Inspected shape-only — `awk '{print NR": "$1" "$2}'`.
- **Stale present-tense claim in SKILL.md (the playbook, not a dated note).**
  - `SKILL.md:40-41`: "`hyprland.conf` is a pure orchestrator: 17 `source` statements, zero settings of its own (29 lines …)".
  - `:46` names `ai-usage.conf (:29)` as the last include. Live says 18 sources, 32 lines, last = `gkeep.conf`.
  - Other stale quotes:
    - 8 notes quote the old pin `4f52854a` — `grep -l '4f52854a' corpus/knowledge/*.md | wc -l`. SKILL.md does too, 2× (`:297` worked example dated 2026-10-14; `:422`).
    - 6 notes quote "17 source" — `grep -lE '17 \`?source' corpus/knowledge/*.md | wc -l`.
  - The notes are dated history (`corpus/README.md:5-8`), not false. SKILL.md:40-46 is present tense.
- **Waybar plane drift** (gate PASS, because its waybar rows are semantic, not byte-pinned):
  - `config.jsonc`, recorded at round 3 (`config-health-report-r3.md:189`): 249 L / 6,068 B `07f7d663106b72e4`. Now: 260 L / 6,354 B `a408a33df48a39dc`.
    - Top-level module entries went 17 → 18, measured by a JSONC parse of `modules-left/center/right` (python, Appendix A).
    - The delta is exactly `custom/gkeep` inserted at the front of `modules-right`.
    - Note: MADO-R3-1 counts "19 modules" under its own convention (2+8+9). W2 must re-derive that count under the note's convention, not this one.
  - `style.css`: 136 L / 1,887 B `8316c08ceaa7e3f0` → 155 L / 2,256 B `8f335ca01da53d32`, mtime 2026-10-17 20:32:18 −03:00.
    - An intermediate `style.css.pre-ai-readability` exists: 2,118 B, `c9215e9ee3053e19`.
    - [INFERENCE] There were two edits: the gkeep snippet at 17:02, then an "ai-readability" restyle at 20:32.
  - Backups: both `config.jsonc.bak.1792203278` (2026-10-17T02:14:38Z) and `.bak.1792267376` equal `07f7d663…`. The first event's write is `[UNK]`: it was either a no-op or reverted before the gkeep install.
- **Recovered since the closeout:** waybar process, layer and tray rows PASS (pid 1724, `DP-1 level 2 … 3440x26`). The closeout's live caveat (waybar core-dump, `SCORECARD.md:30`) no longer holds.
- **Still open:** hypridle absent (`live.consumer.hypridle` NOTE; F1, S1, operator-owned) — open since 2026-10-14.
- **Pins held:** Hyprland 0.56.2 `efb5099…`, waybar v0.15.0, walker 2.17.0, omarchy 3.8.3 / tag v3.8.4 / HEAD `8fcc9d60`, skill leaf `becd149e4d1c…`; omarchy command surface 282. All PASS or HELD in the live run.
- **Backups:** `hypr.backups` NOTE now counts 2: `autostart.conf.bak.1791942509` (2026-10-14T01:48:29Z, the known "65 B dead backup") and the new `hyprland.conf.bak.1792267376`.

### 3.5 Drift provenance (adjacency: report, never absorb)

- `~/Projects/gkeep`:
  - Operator project. HEAD `133b867` (2026-10-18), "Add a Copy button that puts the note on the clipboard." No fleet lane owns it: `grep -c gkeep MANIFEST.json` → 0.
  - It ships `BarWidget.qml`. No Quickshell is installed: `command -v quickshell qs` → no. On this host the QML widget is declared-only.
- `install.sh:21-36`:
  - copies `share/hypr/gkeep.conf` → `~/.config/hypr/gkeep.conf`;
  - writes `hyprland.conf.bak.<epoch>`;
  - appends `# gkeep local notes` / `source = ~/.config/hypr/gkeep.conf`.
- `install.sh:60-82`:
  - inserts a `custom/gkeep` block before `custom/ai-usage` in the waybar config (`on-click` capture, `on-click-right` list);
  - appends `share/waybar/gkeep.css` to `style.css`;
  - backs up both files.
- `install.sh:88-90` runs `hyprctl reload` and `configerrors`. Today `live.hypr.configerrors` reads empty (PASS).
- For mado this is an operator-applied change to owned surfaces. Its job is measure, re-anchor and recommend. It must not edit gkeep or any config.

## 4. Mistakes mined (14 classes)

Sweeps used in this section:
- `grep -ciE 'negative|sweep|absence|hash|sha|derive|scratch|/tmp' corpus/QUALITY.md` → 0.
- SKILL standing rules (`SKILL.md:27-36`) hold only the anchor, O/I/U-separation, shape-only and append-only rules.
- "re-derive" appears 10 times in SKILL.md — `grep -ciE 'clock|re-deriv' SKILL.md` — but only in round-append narrative (`:502-1460`), never as a standing rule.

| # | Class | Evidence | Already captured? | Proposed criterion (cite the lesson) |
|---|---|---|---|---|
| M1 | Prose-copied hash tail propagates: `…a5171` instead of `…1a625171` | closeout F1 (`closeout-r11.md:196-198`); SC-B (`lessons/round-10.md:188-193`). Count 52 in 17 files — `git grep -c 'a5171' HEAD -- '*.md' \| awk -F: '{s+=$NF;n++} END{print s,n}'` (was 34/13 at `f7bfc9f`, `lessons/round-10.md:88`). No erratum in `arc-synthesis.md` (no errata heading — `grep -nEi '^#+ .*errat' corpus/knowledge/arc-synthesis.md` → none). | No (QUALITY sweep 0; SKILL narrative only) | "A pinned value (sha, size, count) is published with its re-derivation command at a named commit. A truncated tail must be a true suffix. Corrections carry both values." (`lessons/round-10.md:82-97`, "A citation that cannot be re-derived is a clock, not a value.") |
| M2 | Pre-commit artifact cited by a window sha | F5: `SKILL.md:1314` cites AUD-M9 `7ad8eccd…`; landed blob `866272ee…`. Corrected append-only at `SKILL.md:1500-1505`. | Lesson only (`lessons/round-10.md:98-107`) | "Cite committed artifacts by `git show <commit>:<path> \| sha256sum`. A window sha is tagged as such and re-bound at commit." |
| M3 | Planned name cited as landed path | F4: `gate-standing-use.md:13` still cites `ten-round-synthesis.md` (`grep -n ten-round-synthesis …` → `:13`); the plan's `arc-closeout.md` never landed (AUD-M11 F1, `LOG.md:310-312`). | Fleet `CORPUS.md:45` covers index rows only; lane: no | "A path enters a note only after it exists at a commit. A predicted name is labelled planned and is never a recheck target." |
| M4 | Record debt deferred for rounds | README 8/22 unrowed from round 3 to 11 (`lessons/round-10.md:108-118`). Lessons 0 for ten rounds. SCORECARD rows 4–9 stubs. ⟨PENDING⟩ still in drafts: 22/19/19/13 — `grep -c PENDING plans/*.md`. | Fleet `LEARNING.md:63-64` (lesson per round); lane: no | "A round's index row, lesson (`## Gate`) and scorecard row land in that round's commit. A deferral is a named rejection, never a carry." |
| M5 | Planned gate clauses shipped as notes; covering mutant owed | `reports/r7-aud-m7.md:34-35` (C3/C4 "NOT LANDED as gate rows"); `reports/r9-aud-m9.md:40` (C1b NOT LANDED); `gate-standing-use.md:205-211` (theme mutant owed) | Yes, as gate maintenance rules (`gate-standing-use.md:203-226`), but not in QUALITY | Reference the maintenance rules from QUALITY: "a chartered clause that did not land is a finding with its command" |
| M6 | Auditing a moving tree; verdict tied to harness stdout | `reports/r8-aud-m8.md:36` (selftest "FAILED — 88 passed, 1 failed" on mid-edit copies); `reports/r8-ver-m8.md:100-110` (`MADO_REGRESSION: FAIL (out of band: restore-not-ok)` from a 4,096-byte stdout truncation; cause `[U]`) | Fleet `PROTOCOL.md:378-379` (verdict names its revision); lesson (`lessons/round-10.md:98-107`) | "Audit verdicts bind to a commit or frozen-copy sha. A mid-edit FAIL is labelled in-flight, never a defect." |
| M7 | Count transcription errors | `313→315` (`LOG.md:138-141`); R3-2 §0 `6×→7×` (`LOG.md:253-256`); mako `50→119 B` (`LOG.md:97-100`); F3 `2,837` vs `2,887 L` still at `walker-deep-r9.md:296` | Partly: QUALITY #2 "measured anchor"; fleet `CORPUS.md:33-37` "A count carries its command" | Adopt the fleet rule verbatim: `<n> — <command> <date>` |
| M8 | Unswept negative capability claim | "no rule-read verb in Hyprland 0.56" (`arc-synthesis.md:300`; `config-health-report-r3.md:449`) vs `hyprctl --help` line 51: `getprop ... → Gets a window property` (and line 58 `workspacerules`) — `hyprctl --help \| grep -nE 'getprop\|workspacerules'`. `getprop` mentions in corpus + SKILL: 0 — `grep -rc getprop corpus SKILL.md \| awk -F: '{s+=$2} END{print s}'`. [INFERENCE] `getprop` reads effective per-window properties, i.e. rule effects without rule attribution. Docs and a measurement must confirm this. | Fleet `CORPUS.md:38-40` "A negative claim carries its sweep"; lane: no | "An absence claim about a tool cites that tool's own `--help`/man sweep at the pinned version (command + matching lines)." |
| M9 | Promotion `[x]` without established independence | `[x]` 4/4 at `c03c249` (VER-M3/VER-M4B). Regressed to `[~]`×4 at `7cd7f33`: "outside-lane verifier independence is not established by the inherited record" (`SHONEN.md:6`). | Fleet `PROTOCOL.md:63-68`; `LEARNING.md:43`; lane: no | "Every `[x]` and spot-check records the verifier's dispatching lane. Lane-dispatched seats are `[~]`." |
| M10 | Published counting block not exercised literally | Hardcoded `REV` wrapper (`LOG.md:609-640`; `SCORECARD.md:181-198`) | Erratum only | "A published counting block is run verbatim (`bash -s` on the fenced bytes, sha recorded) for each recorded result." |
| M11 | Scratch receipts as evidence pointers | 79 unique `/tmp` paths in 51 distinct dirs are cited; 0 of the dirs exist today (existence loop, Appendix A). `SCORECARD.md:19` already marks one "(ephemeral)". | Lesson (`lessons/round-10.md:74-78` "scratch does not survive"); cadence row (`gate-standing-use.md:201`) | "Evidence that must outlive the round is a committed path or quoted lines plus sha. A /tmp path is provenance only." |
| M12 | Report filed off-contract; ledger gaps | Prompt: "Write the round report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-1/mado.md` on the fleet repo" (fleet `.ufo/prompts/mado-round-1.md` §4). Fleet copy count: 0 — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-1 \| grep -c mado`. Lane copy: `.ufo/reports/round-1/mado.md`. | No | SKILL round-closure checklist item (process, not QUALITY) |
| M13 | Drift instrument set-blindness | Today's run: include count FAIL without a named delta (`tools/mado-verify.sh:2211-2212`); presence-only over pinned lists (`:2229-2238`, `:2249-2256`); unpinned waybar module set (`custom/gkeep` added, 0 rows moved) | Not in the residual ledger as a blind spot (`gate-standing-use.md:251-297` read at headings only — [UNK] whether it is named there) | SKILL/gate rule: "census rows compare sets (missing and extra) and name the delta" |
| M14 | Ledger verdicts not tied to claims | 28 of 45 fleet "improved" verdicts are manifest-only; r3 coverage and r11 freshness are lane-only (§2.2) | Fleet `AXES.md:27-36` | Fleet-level (D3/parent): MANIFEST verdicts equal the round report's claim verdicts; unclaimed axes are `unchanged` |

Rounds with no gate disagreement: no arc round was rejected or harmed, so no harmed verdicts exist anywhere in the record. Fleet round 1 is the one honest stop: blocked, +0 (`.ufo/reports/round-1/mado.md:87-93`).

Gate agreement on record:
- Round 10: AUD-M10 and VER-M10 agree on both admits and rejects (`lessons/round-10.md:163-171`).
- Round 1 (fleet): the outside spot-check was "**not supplied**" (`lessons/round-1.md:19-22`). No `QUALITY.md` criterion was ever added because of "No criterion is added to `QUALITY.md` without an outside-disagreement lesson behind it" (`:21-22`).
- `LEARNING.md:32` also counts "a disagreement becomes a lesson that adds a grounded criterion". The method lessons in `lessons/round-10.md` ground M1, M2, M6 and M11 today.

## 5. Contract defects (19) — report only; nothing touched

| # | Defect | Evidence (command → value) | Rule |
|---|---|---|---|
| D1 | SKILL frontmatter `description` lacks quoted triggers, an anti-trigger and a sibling-arbitration note | `SKILL.md:3` "Domain specialist — desktop & compositor craft. Rank: shonen (probation)." Quoted triggers: 0 — `sed -n '2,3p' SKILL.md \| grep -c '"'` | `PROTOCOL.md:414` |
| D2 | No gate registry row at the registry home (`SKILL.md`) for `tools/mado-verify.sh` | `grep -ci registry SKILL.md` → 0 | `PROTOCOL.md:383-388,405-406` "closure grades no gate conformant until its registry row exists" |
| D3 | PROVINCE lacks Core/Frontier/Adjacent | → 0 (§3.1) | `LEARNING.md:68-70` |
| D4 | 19/22 knowledge entries do not open with `source:`/`verified-at:`/`recheck:` | → 3/22 (§2.4) | `CORPUS.md:17-18`; `LEARNING.md:61-62` |
| D5 | QUALITY: 5 criteria, 0 cite a lesson, still "probation draft" | §3.1 | `LEARNING.md:54-58` |
| D6 | Lessons: 2 files for 11 admitted rounds plus 1 blocked. `round-1.md` holds fleet r1 (2026-10-15), not probation r1 (2026-10-14): a namespace collision | `ls corpus/lessons` | `CORPUS.md:14,18` |
| D7 | SCORECARD: 4/6 axes unscored; capabilities 0; saturation undeclared; planned empty | `SCORECARD.md:44-47,200-218` | `AXES.md:75-83` |
| D8 | Fleet-r1 report absent from the fleet path the prompt required | M12 | fleet `.ufo/prompts/mado-round-1.md` §4 |
| D9 | MANIFEST lacks mado probation round 1 (`65a2254`, "admitted 3x ADMIT"). Same gap for tameshi, tsukuroi and tabi (minted the same hour) | python (Appendix A): mado rounds 0, 2–11 | append-only ledger completeness |
| D10 | MANIFEST verdicts diverge from lane claims (28/45 manifest-only) | §2.2 | `AXES.md:27-36` |
| D11 | Fleet root carries no mado record outside MANIFEST and config; L0 `:37` unanswered | `grep -c mado LOG.md SCORECARD.md ROADMAP.md` (fleet root) → 0/0/0 | operator/integrator duty |
| D12 | Open errata owed since 2026-10-14. **F1** 52/17 (M1). **F2** `snapshot-diff-receipt-r9.md:33` still `…db62` (`grep -n 'db62'`). **F3** `walker-deep-r9.md:296` still "2,837 L". **F4** `gate-standing-use.md:13`. walker-deep errata "_None yet" (`walker-deep.md:615-617`), sha `0982ba066c72575a` unchanged since `eead56b` (`git log -- corpus/knowledge/walker-deep.md`). AGENTS gate pointer: 0 — `grep -c mado-verify AGENTS.md`. F5 is closed (`SKILL.md:1500-1505`). | listed | `closeout-r11.md:195-205`; `QUALITY.md:7` |
| D13 | Dead evidence pointers: 51 distinct /tmp dirs cited, 0 exist | M11 | `PROTOCOL.md:330` (resolvable pointer) |
| D14 | Stale present-tense SKILL claim (17 sources / 29 L / ai-usage last) | §3.4 | `AXES.md:14` (freshness) |
| D15 | Gate blind spots: set-blind census, undiagnosed count delta, unpinned waybar module set | M13 | `PROTOCOL.md:362-364` (a gate compares against persisted expected values) |
| D16 | Bloat (detail below) | — | `PROTOCOL.md:439-440` "never generic agent advice" / elegance |
| D17 | Rank/probation stated three ways. `SKILL.md:3` "shonen (probation)". `SCORECARD.md:28` "Probation 4/4 `[x]` since round 5" (arc-end statement, unqualified in place). `SHONEN.md` 4×`[~]`. `SCORECARD.md:39-42` qualifies it further down. | listed | calibration (`AXES.md:15`) |
| D18 | [INFERENCE] SHONEN evidence lines carry prose beyond a pointer | Seed text matches modulo marks: `grep -vE '^  ' SHONEN.md \| sed -E 's/^- \[[ x~]\]/- [ ]/' \| diff - <seed>` → SEED-MATCH; 4 evidence lines. The canonical form allows "one indented evidence line per box … no other prose" (`PROTOCOL.md:417`). | `PROTOCOL.md:417` |
| D19 | Stale provenance: `gate-standing-use.md:228` names harness sha `cf41efaa…` as "today"; the current file is `75ed934dc86360f5…` (mtime 2026-10-14 18:00 −03, after the note's 20:44–20:56Z window). Provenance only, not gated. | `sha256sum …/tameshi-shokunin/tools/mutate-and-run.sh` | freshness |

D16 bloat detail:
- `SKILL.md`: 116,306 B / 1,580 L — `wc -c SKILL.md; wc -l SKILL.md`. The core playbook (`L1-450`) is 42,410 B — `awk 'NR<451' SKILL.md | wc -c`. Eight round-append sections (`L451-1580`) are 73,896 B = **63.5%** — `awk 'NR>=451' SKILL.md | wc -c`. These appends are chronology, not distilled craft.
- README coverage rows up to 2,025 chars; 4 rows exceed 1,500 — `awk 'length>1500' corpus/README.md | wc -l`.
- SCORECARD has a 2,395-char row.
- `plans/`: 380,747 B in 18 files; `reports/`: 114,677 B in 9 files — `du -sb plans reports`.
- The gate is 150,103 B.

Other checks:
- **Uncommitted changes:** none — `git status --porcelain=v1 -b` shows the header only.
- **Ignored local artifact:** `.ufo/interactive-sessions/`, 2,641,017 B — `du -sb .ufo/interactive-sessions`. These are native session logs, ignored by `.gitignore:1`. Never touch them.
- **Append-only history:** held.
  - Every deletion in `LOG.md` and `corpus/knowledge/` history is a 1-line EOF-newline re-add of identical text. Examples: `7cd7f33` LOG `-`/`+` of the same line; `e1e1bb7` and `eead56b` "\ No newline at end of file".
  - Commands: `git log --numstat -- LOG.md corpus/knowledge`; `git show <c> -- <f> | grep -E '^-|No newline'`.

## 6. Proposed round 12 (1–3 claims, distinct axes, ≥1 on the lowest)

Fences for every claim:
- Config trees and the running compositor stay read-only. Allowed: hyprctl read verbs only, plus `getprop`.
- Never `setprop`, `dispatch`, `keyword` or `reload`. No mutating `omarchy` verb. Never `git status` on the omarchy checkout.
- Never execute lock, idle or toggle scripts.
- Session material stays shape-only: no window titles. Select windows by class or address.
- Do not edit `~/Projects/gkeep` or any config. Do not prepend headers to legacy notes.

### C1 — freshness: re-anchor the 2026-10-17 drift append-only (the lowest axis in observed reality)

- **Claim:** Every present-tense anchor that the gkeep install falsified is re-verified, recorded with both values and provenance, and re-anchored by the lane's own protocol. The re-anchor protocol: "Changing the baseline … requires an appended erratum naming old→new values, the reason, and the re-measure command" (`omarchy-drift-watch.md:284-287`). The pins rule: "Pins are never edited to match reality." (`gate-standing-use.md:222`).
- **Counting command:** `bash tools/mado-verify.sh --no-live | awk '$3=="FAIL"||$3=="UNKNOWN"' | wc -l`.
  - Before: **1** at `e1d81d4`, 2026-10-19 (`hypr.root.include_graph`).
  - After target: **0**, measured at the round commit.
- **Deliverables:**
  - New `corpus/knowledge/config-drift-r12.md`. It opens with `source:`/`verified-at:`/`recheck:` and carries:
    - hypr: 17→18 sources; 29→32 L; `4f52854a…`→`ce7483f3…`; last include `ai-usage.conf`→`gkeep.conf`;
    - local confs 12→13;
    - waybar: `07f7d663…`→`a408a33d…`, `custom/gkeep`;
    - style: `8316c08c…`→`8f335ca0…`;
    - the backup and epoch provenance;
    - `install.sh` line anchors;
    - a getoption spot-check that the precedence claims still hold. gkeep adds only `windowrule` lines.
  - A `SKILL.md` erratum append correcting `:40-46`.
  - A gate re-anchor for `EXPECT` (`:2190-2207`), the selftest fixture (`:244-260`) and `LOCAL` (`:2249`), carrying the appended erratum.
- **Harm watch — operability:**
  - The edit lies outside the excised marker pairs (`gate-standing-use.md:233-243`), so `--regression` reads SETUP until the printed `REGRESSION_RECUT` re-sweep runs. After the re-sweep, update `PIN_MADO` (`:1290`) and `TABLE_MADO` (`:1293`) from the *measured* table.
  - `--selftest` must stay N/N, and `--regression` must end at PASS.
  - Run the harness read-only.
  - **Worktree pitfall:** `MADO_R7_FLEET=$(dirname "$(dirname "$(dirname "$MADO_R7_SELF")")")` (`:1295`). Run from `.tower/worktrees/kaika/mado-shokunin/`, it would resolve the harness to `…/kaika/tameshi-shokunin/…`, possibly a sibling W2 worktree mid-edit. Set `MADO_VERIFY_HARNESS=/home/vgpnk/Projects/shokunin/tameshi-shokunin/tools/mutate-and-run.sh` explicitly (`:1505`). Current harness sha is `75ed934dc86360f5…`.
  - /tmp headroom is fine: 5% of inodes used — `df -i /tmp`.
- **Fallback C1′ (no gate edit):** keep the gate red as a true alarm, with the drift dispositioned as "re-anchor owed".
  - Counting command: present-tense SKILL claims contradicted by live and lacking an appended erratum.
  - Before: 1 (`SKILL.md:40-46`). After: 0. Verify with `grep -n 'Errata (round 12)' SKILL.md` or the lane's chosen marker.
- **Optional within the same axis** (two claims on one axis count as one): close F2, F3 and F4 with appended errata. Each is a single-line correction carrying both values.

### C2 — coverage: window-rule effects move from gap to measured ground

- **Claim:** The read-only verb `hyprctl getprop` (0.56.2 `--help` line 51) is measured on at least one window class that has rules. The best candidate is Alacritty opacity, which also re-tests F2 (`config-health-report-r3.md` F2; `keybind-rule-semantics.md` §4.6).
  - The result lands as `corpus/knowledge/window-rule-effects-getprop.md`, opening with the triple.
  - The negative claim at `arc-synthesis.md:300` and `config-health-report-r3.md:449` gets an appended correction in the round's records.
- **Counting command:** `grep -rc getprop corpus SKILL.md | awk -F: '{s+=$2} END{print s}'`.
  - Before: **0**. After: ≥1, from the new entry.
  - Coverage-map rows go 22 → 23, and the SCORECARD navigation counter must print `23/23 … exit 0`, so coverage is not harmed.
  - Frontier bullet 1 (`corpus/README.md:70-72`) is updated in place in the index.
- **Bound and reject path:**
  - If `getprop` returns values without rule attribution, admit a bounded "effect-read, not match-read" entry.
  - If it cannot read rule-applied values at all, reject the candidate with that reason and keep the rejection in `## Gate`.
  - [INFERENCE] semantics: confirm with docs (ART) and with measurement before admission.
- **Sources:** `hyprctl --help`; Hyprland wiki hyprctl and window-rules pages (ART dossier, if assigned); Hyprland 0.56 changelog. These are `SOURCES.md` rows with `used-by` = the new entry.

### C3 — calibration: ground `QUALITY.md` in the mined mistakes (the lowest axis under the contract rubric)

- **Claim:** `QUALITY.md` gains criteria from M1, M2, M7, M8 and M11 (§4). Each new row cites the lesson that produced it: `lessons/round-10.md` method lessons and the new `lessons/round-12.md` `## Mistakes`. A **non-author** spot-check records agree or disagree on ≥1 admit and ≥1 reject (`LEARNING.md:39-43`).
- **Counting command:** `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md`.
  - Before: **0** (of 5 criteria — `grep -cE '^[0-9]+\. ' corpus/QUALITY.md`). After: ≥4.
  - Supersessions are new rows that name the row they replace (`LEARNING.md:57-58`).
- **Harm watch:** "harmed when … a criterion is added with no lesson behind it" (`LEARNING.md:32`). Every new row needs a resolvable lesson anchor.
- **Alternative C3′:** SCORECARD contract completeness.
  - Six of six axes scored with command and commit (now 2/6).
  - Capabilities 0 → k, each run in-round: selftest, `--regression`, snapshot pair, live verdict.
  - Saturation line and stagnation window declared.
  - Count: `grep -cE '^\| (coverage|operability|freshness|calibration|depth|adjacency)' SCORECARD.md` on the round's score table.

### What `SOURCES.md` (D1) and the new entries serve

- **C2** needs the most new sources: tier-A docs and tool rows.
- **C1** cites `code`/`own-work` rows: `install.sh`, the gate, `omarchy-drift-watch.md`.
- **C3** cites `own-work` lesson rows.
- Seeds are in §7. W2 must re-open every row in its own round.
- Candidate knowledge entries:
  1. `config-drift-r12.md` (C1).
  2. `window-rule-effects-getprop.md` (C2).
  3. Conditional, on ART sources: `hyprland-config-era-r12.md`, covering the hyprlang → Lua configuration transition and window-rule syntax eras. SKILL already flags the "current wiki lua-era, host 0.56.2 still parses hyprlang" caveat (`LOG.md:95-96`). This entry fills frontier/coverage-map ground, and its `[INF-docs]` class must stay labelled.

### Lesson seeds for `lessons/round-12.md`

- `## Mistakes`: M1–M14 with pointers. Mark M12 and M14 as fleet-level.
- `## Gate`, candidate rejects:
  - prepending headers to legacy notes (sha cascade, §3.3);
  - treating gate PASS on waybar as "plane unchanged" (M13);
  - treating the gkeep project as mado-owned (adjacency).

### MANIFEST closure note (parent)

Record all six axes. Claimed axes take their measured verdict; every other axis is `unchanged`. This avoids repeating M14.

## 7. Local source seeds (opened this session; tier A; W2 must re-open in its round)

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|hyprctl --help (Hyprland 0.56.2 efb5099) — local tool output|tool|A|full read-verb list incl. getprop (line 51) and workspacerules (line 58); grounds rule-effect reads and refutes the no-rule-read-verb claim|queued|2026-10-19|on-release|—|
|S002|tools/mado-verify.sh @ 93e43f8f — lane gate source|own-work|A|exit map, encoded invariants, EXPECT and LOCAL pinned lists, harness path resolution, re-cut procedure|mined|2026-10-19|on-change|corpus/knowledge/gate-standing-use.md|
|S003|~/Projects/gkeep/install.sh @ 133b867 — operator project installer|code|A|exact provenance of the 2026-10-17 hypr include and waybar module and css drift with epoch-stamped backups|queued|2026-10-19|on-change|—|
|S004|corpus/knowledge/omarchy-drift-watch.md lines 284-287 — lane re-anchor protocol|own-work|A|how a baseline moves: appended erratum with old and new values, reason and re-measure command|mined|2026-10-19|90d|corpus/knowledge/omarchy-drift-watch.md|
|S005|corpus/lessons/round-10.md lines 63-123 — method lessons|own-work|A|re-derivable documents survive; citations as clocks; commit binds; gaps bill readers|mined|2026-10-19|90d|corpus/lessons/round-10.md|
|S006|corpus/knowledge/arc-synthesis.md lines 290-341 — gap ledger and classification|own-work|A|the 12 named unknowns and why each stays unknown; frontier source for depth and coverage moves|mined|2026-10-19|90d|corpus/knowledge/arc-synthesis.md|
|S007|PROTOCOL.md lines 360-408 — fleet gate standard|spec|A|verdict map, self-test, two evidences, registry row at SKILL.md as condition of conformance|queued|2026-10-19|on-change|—|

Row counts:
- Rows: 7 — `grep -cE '^\|S[0-9]{3}\|' <this file>`. These use the compact `|S` form here; W2 uses the contract's `| S` form.
- Tier A: 7; B: 0; C: 0.

## Leads (unopened)

- Hyprland wiki: hyprctl usage page; window rules page; config-language (Lua) migration notes.
- Hyprland GitHub releases 0.53–0.56 changelogs: hyprctl `getprop` introduction and semantics; window-rule syntax eras.
- `waybar(5)` / Waybar wiki: custom module `exec`/`signal` semantics; any IPC added after 0.15.0.
- Walker 2.x and elephant upstream docs: socket protocol, reload semantics.
- omarchy manual: hooks `*.d` directories (MADO-3 §7 drift).

## Appendix A — commands run (read-only) and key outputs

- `git -C <lane> status --porcelain=v1 -b` → `## master...origin/master` only. `git log --oneline -n 40` → 18 commits.
- `python3` over fleet `MANIFEST.json`:
  - roster mado rows: 0 of 13;
  - mado-lane rounds: 0 (mint), 2, 3, …, 11;
  - per-round improved keys (§2.2).
- SCORECARD counter body at HEAD → `revision=e1d81d4… indexed=22/22 missing=0 dangling=0 duplicates=0 coverage=10.0000/10`.
- `bash tools/mado-verify.sh --no-live` → `counts: pass=28 fail=1 unknown=0 skip=8 note=4` / `MADO_VERIFY: DIVERGED (1 fail, 0 unknown, 28 pass) — first fail: hypr.root.include_graph (18 source lines (expected 17))`, exit 1. Boundary `fd6b8c320ac6…` PASS (was `bb2639d9a980…` on 2026-10-15).
- `bash tools/mado-verify.sh` → `counts: pass=51 fail=1 unknown=0 skip=0 note=8` / `MADO_VERIFY: DIVERGED (1 fail, 0 unknown, 51 pass)`, exit 1.
- `grep -n '^[[:space:]]*source' ~/.config/hypr/hyprland.conf` → 18 lines (`:4-13,16-20,23,29,32`).
- `diff` against `hyprland.conf.bak.1792267376` → `29a30,32` only. `sha256sum` of the backup → `4f52854a3c143dcf`.
- JSONC parse of the waybar config and its backups → top-level modules 15 (`.bak.1791314470`) → 17 (`.bak.1792203278`, `.bak.1792267376`, both `07f7d663…`) → 18 (live, `+custom/gkeep`).
- `for d in <PROVINCE paths>; do [ -e "$d" ] …` → 9/9 exist.
- `/tmp` pointer sweep:
  - unique paths: 79 — `grep -ohE '/tmp/[A-Za-z0-9._/-]+' -r corpus SCORECARD.md SKILL.md LOG.md | sort -u | wc -l`;
  - distinct top dirs: 51 — same with `[A-Za-z0-9._-]+`;
  - existing now: 0 — existence loop.
- `command -v quickshell qs noctalia-shell dms` → none; `grim`, `hyprpicker` present.
- `df -i /tmp` → 5% inodes used.

## Appendix B — live gate rows today (abridged; FAIL and NOTE rows verbatim)

```text
hypr      hypr.root.include_graph         FAIL    18 source lines (expected 17)
hypr      hypr.root.sources_resolve       PASS    17/17 targets exist
hypr      hypr.local.inventory            PASS    12/12 active local confs
hypr      hypr.file.sha_pin               NOTE    hyprland.conf sha256 ce7483f35ab5… drifted from round-1 pin 4f52854a3c14…; re-verify anchors
hypr      hypr.backups                    NOTE    2 backup file(s) under ~/.config/hypr (S3 litter class)
hypr-live live.consumer.hypridle          NOTE    hypridle absent — declared 150s/152s idle chain has no consumer (F1, S1; operator-owned)
hypr-live live.waybar.process             PASS    waybar pid 1724
waybar    waybar.config.parse             PASS    JSONC parses (260 L, 6354 B)
omarchy   omarchy.git.head                PASS    HELD: 8fcc9d60 (P3 pin)
theme     theme.parts.declared_only       NOTE    declared-only, consumer absent: foot.ini(foot) kitty.conf(kitty) ghostty.conf(ghostty) helix.toml(helix) vscode.json(code) keyboard.rgb(asusctl)
gate      boundary.readonly               PASS    config plane byte-identical before/after (combined sha fd6b8c320ac6…)
counts: pass=51 fail=1 unknown=0 skip=0 note=8
MADO_VERIFY: DIVERGED (1 fail, 0 unknown, 51 pass) — first fail: hypr.root.include_graph (18 source lines (expected 17))
```
