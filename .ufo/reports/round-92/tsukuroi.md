# tsukuroi — round 92 (lane report)

Lane: `tsukuroi-shokunin` (host operability and repair). Round 92, attempt 1. Lane HEAD at filing:
`7793773a3837a46762cd6415da055ba4d20a1e29` (branch `master`, `ls-remote` re-derived below). Round shape: one v1 wave, 13 seats
(4 executor, 2 critic, 2 reviewer, 2 mutation-tester, 1 scout, 1 scribe, 1 connector; 6 attack seats =
46% >= 25%; 1 connector; no residual call; 0 dead seats  (per `w1-results.json`)). Frontier step: `corpus/SOURCES.md`
376 → 381 rows.

## Work performed

Declared claims (2, distinct axes, causally separable; frozen in `SCORECARD.md` "Round 92 — declaration",
`.ufo/plans/round-92.md` and `.ufo/waves/round-92/claims.json`):

- **C1 (operability 9, assurance arm)** — the `limine-pins` battery's oracle channel is closed: every gate
  runs as a private copy under `bwrap --unshare-all --clearenv` + `python3 -I`, and five channel controls
  (sibling, `sys.path`, absolute lane path, parent `/proc`, caller environment) certify each read channel.
- **C2 (depth 8, tied lowest non-retired axis)** — the gate's global-section visibility rule is
  version-selected: `--limine-version X.Y.Z` picks the pre-12.9.5 rule or the v12.9.5+ `create_menu_tree`
  rule (no first-line-is-entry exception), refuses anything outside `X.Y.Z` with rc 64, and is certified by
  seven era families plus `--usage-check`.

Work items, each with its evidence pointer:

- **Freeze** (`da99b2f4`): declaration, instruments, five channel controls, four one-clause C2 bends,
  pinned v12.9.4/v12.9.5/v12.9.6 sources, instrument manifest (28 lines after A8) —
  `git -C tsukuroi-shokunin show da99b2f4 --stat`.
- **Two control repairs before scoring** (`495a9f6c` A1, `429fd1a3` A2): the generated controls never
  called `find_oracle()` (dead in both legs: `0/82`), and `K4-syspath` matched a wildcard name and crashed
  (984 error rows). Both are kept as receipts
  (`.ufo/waves/round-92/after/c1-controls/before-clone-dead-controls/`, `.../before-clone/K4-syspath.json`)
  and became QUALITY 133/134 and lesson M3/M4.
- **Gate hardening** (`689623fd` A3, from the wave's ReviewGate F1-F5): bounded the version digits before
  `int()` (a 5000-digit component traced back instead of rc 64), pinned leading-zero acceptance,
  moved the `bwrap` guard before `--selftest`, normalised a string `tpm`, fixed the CLI description —
  `git show 689623fd -- tools/check-limine-pins.py tools/limine-pin-battery-r92.py`.
- **Instruments**: `tools/check-limine-pins.py` (V2 `--limine-version`, era-selected `in_global`,
  `limine_version`/`visibility_era`, 37-case `--selftest`) and `tools/limine-pin-battery-r92.py`
  (89 families, ISOLATION launcher, `--isolation-check`, `--usage-check`, `--selftest`).
- **Pinned sources**: `.ufo/waves/round-92/before/src/` (`SHA256SUMS`, `cmp-pins.txt`, `URLS.txt`;
  v12.9.5 and v12.9.6 `config.c` are byte-identical, `a940acae…`; v12.9.4 `config.c` equals the r91 pin,
  `aafc9c41…`).
- **Corpus**: `corpus/knowledge/limine-r92-oracle-isolation.md` (OI1-OI4, EV1-EV5, S377-S381),
  `corpus/SOURCES.md` +5 rows, `corpus/QUALITY.md` 132-135, `corpus/lessons/round-92.md` (M1-M5),
  `corpus/README.md` round-92 Frontier, `SCORECARD.md` capability `battery-oracle-isolation` + measured
  outcome, `SKILL.md` registry row `limine-pin-battery-r92` + correction R92-REG-1.
- **Wave w1** (13 seats, dispatched 02:06, settled with `w1-results.json`: 13 seats, 13 outputs, 0 dead):
  receipts in `.ufo/waves/round-92/w1/`, seat reports as `w1/<Seat>.md` (`ReviewSource`'s is
  `w1/ReviewSource/review.md`, its only report path); the wave's own falsifications drove amendments A3-A9.
- **Registry and lane gates** (`ec728e4a`, from the wave's ExecLints F1-F4): the r92 battery had no
  operative row at the freeze (F1), the row appended at A1 had 6 cells and broke the table for two commits
  (F2), the `limine-pins` row still described the r87 gate (F3) and the battery row pinned the freeze digest
  (F4). Rows replaced with the current interface; `check-registry-coverage.py` PASS 145/145 at `ec728e4a`.
  F5 (the gate's V2 text cites v12.9.6 raw lines without naming S379/S380) is documentation-only and is
  routed, not edited now: a docstring edit would change the instrument sha every receipt is bound to.
- **Credential incident** (M5): a seat's environment-channel probe wrote live 1Password token lines into
  a receipt; redacted (7 values across 2 files, sha256-prefixed markers, rescan 0), the unpushed
  secret-bearing commit was squashed away (never pushed), the content re-landed as `689623fd`; GH013 text,
  the L0 lines (`tsukuroi | round-92` twice: incident, resolution) and QUALITY 135 are the record.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: declaration, instruments, controls, pinned sources, corpus rows, registry/frontier | round-92 entry | `da99b2f4` |
| A1 control repair (`BATT = find_oracle`), QUALITY 132/133, registry rows | round-92 entry | `495a9f6c` |
| A2 K4 frozen-name resolution, QUALITY 134, claims.json, manifest | round-92 entry | `429fd1a3` |
| A3 gate hardening (ReviewGate F1-F5), regenerated C2 bends and manifest | round-92 entry | `689623fd` |
| A4/A7 narrowings + instrument ledger, QUALITY 135, registry row fix | round-92 entry | `e9fce481` |
| wave w1 evidence, final C1/C2 receipts, lesson, SCORECARD measured outcome | round-92 entry | `22b5bc10` |
| pre-file ledger, A8 manifest, registry rows, lesson M6, swept r91 plan | round-92 entry | `ec728e4a` |

## Before → after measurements

- **C1** (`python3 .ufo/waves/round-92/before/controls/run-controls.py --battery <battery> --gates
  <gates> --runs 3`): the same five control bytes read **82/82 `met` ×3** against the unchanged r91
  battery (`after/c1-controls/before-clone/` for K3/K5/K6/K7 — their sha256 are unchanged since A1 — and
  `before-clone-fixed/` for K4, which the A1 bytes crashed) and **0/89 `unmet` ×3 with 0 error rows**
  under the r92 battery in the canonical lane (`canonical-after-final/`) and in a `git clone --shared`
  (`after-clone-final/`); the landed gate reads **89/89 `met` ×3** in both layouts
  (`after/c2-gate-{canonical,clone}.txt`). Measured at `35c1088b…`/`aef33925…` (battery row of the A7
  instrument ledger); reading: met on the differential (A7 §1), not on the `0/89` alone.
- **C2** (`python3 tools/limine-pin-battery-r92.py --gate tools/check-limine-pins.py --runs 3`):
  **89/89 `met` ×3** canonical and clone; `--usage-check` **`met` 11/11** in both layouts; the one-clause
  bends `N01-era-flat-a` **87/89** (2 families fail), `N02-era-flat-b` **85/89** (4 fail, A9 correction),
  `N03-default-b` **88/89** (1 fail), each `unmet` ×3 in both layouts with 0 error rows
  (`after/c2-near-misses/{canonical-final,clone-final}/summary.tsv`; the `{canonical,clone}` dirs hold the
  A4-era crashed bends and are kept as A4 evidence, not cited as numbers); `N04-accept-any` **89/89** (named
  limit) and `unmet` under `--usage-check` (`after/usage-n04.txt`); refused versions print **no JSON** —
  rc 64, 0 bytes on stdout (`after/usage-stdout-check.txt`). The r91-gate do-nothing reads **1/89** with 352
  error rows (only `ERA-DEFAULT`, the flag-less family, passes: `after/c1-controls/k1-donothing.json`, A9).
  Narrowed predicate: A5.

## Sources & frontier

`SOURCES: 376 → 381 rows` (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`) and
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
→ **exit 0** before and after ((exit 0 and 381 rows after; the W04 duplicate-URL warnings are the same URLs in different scopes and W01 is the tier-C lead, both warnings, no error)). Added: 5 rows — S377 Python `-P`/`-I` docs (A), S378 bubblewrap
manual (A), S379 Limine v12.9.6 `config.c` (A), S380 Limine v12.9.6 ChangeLog (A), S381 issue #700 (C, a
community lead, never sole support). Rows touched old→new: none (all five are new; no `status`/`recheck`/
`used-by` change to an existing row). Frontier rows advanced: the r91 bullets "battery oracle-import
channel (ScribeLesson M1 / QUALITY 132 draft)" is landed and measured (QUALITY 132, capability
`battery-oracle-isolation`); "freeze manifest does not pin the battery" is repaired (the manifest now
lists both instruments, all five channel controls, the four bends and their generators); "selftest lacks
V1/U1 coverage" is repaired (37 cases). Assimilation: **none** — no `merge/tsukuroi/` theme fits this
round's surface (the staged entries are Limine entry semantics; this round's ground is the battery's
channel model and the version boundary), recorded here for the next round to take one.

## Trend verdicts

- expansion: **improved** — one admitted entry on coverage-map ground the lane did not hold (the oracle
  channel and the v12.9.5 boundary, S377-S381, all `mined`), plus one capability row
  (`battery-oracle-isolation`) that entered only after running end to end in both layouts.
- quality: **improved** — the gate crashed on a 5000-digit version and is hardened (F1-F5); the battery
  closes its oracle channel with one control per channel; 82 → 89 families; QUALITY 132-135 new; the r91
  routed defects 3-5 are closed; the era-A behaviour is unchanged (no-regression receipt 82/82).
- discernment: **improved** — four wave seats falsified the round's own wording (CriticClaims §1/§4/§5,
  MutGate M02/M13/M18, CriticForgers' crashed bends, ReviewGate's five defects) and every one became an
  amendment (A3-A7) or a named limit; the lane caught two dead controls and a wildcard control itself
  before any candidate score (M3/M4); the credential class is captured as QUALITY 135.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointers:
  `SKILL.md:38-50` (health-verdict table), `:90-141` (update-safety checklist), registry row
  `limine-pin-battery-r92` + R92-REG-1, `corpus/knowledge/limine-r92-oracle-isolation.md`; non-author
  verification of the promotion gate remains owed (the r91 closure so recorded).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: LOG round-92 entry;
  the live-read `--live` leg could not run this round (the conf is root-only; the r87 live receipt stands).
- [~] Instructions executable by an agent without oral context — pointers: `.ufo/plans/round-92.md`,
  `tools/limine-pin-battery-r92.py` docstring (ISOLATION + V2 + usage), the control generators.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: ConnectorOverlap reports 0 conflicts
  and names kumitate's orchestration-level seat isolation as adjacent, not absorbed.

## Stale-lane

Respawn-per-round driver; this lane-round was launched 2026-11-08 01:28 -03 and is the only mission of
this lane open. Age at filing: about 1 h 20 m; the lane is progressing (commits `da99b2f4`, `495a9f6c`,
`429fd1a3`, `689623fd`, `e9fce481`, `22b5bc10`), not silent.

## Pre-file falsification ledger

`PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=7 findings=0` (exit 0)

## Tool installs

None this round (no tool was installed or upgraded).
