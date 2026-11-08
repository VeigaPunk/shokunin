# tsukuroi — round 93 report

Lane: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin` (branch `master`, jj-colocated).
Round: 93 (attempt 1). Freeze: `c633f49aa512e1c8a0e0464b7fb5d354c70096cf`.
Lane tip at filing: `42979f5a2eb16babb4de344c5b21205accae2171` (re-derived with `git ls-remote origin refs/heads/master`).
Round shape: one v1 wave, 14 seats (5 executor, 2 reviewer, 2 critic, 2 mutation-tester, 1 scout,
1 scribe, 1 connector; 7 attack seats = 50 %), no residual call. Dead seats: 0 (all 14 settled, `w1-results.json`).

## Work performed

Declared claims (1-3, frozen in `.ufo/waves/round-93/claims.json` and captured in
`.ufo/plans/round-93.md`; verdicts below are on amendments A1-A3's narrowed wording):

- **C1 — depth 8 (the tied lowest non-retired axis)** — the `limine-pins` battery carries four
  families the r92 roster lacked (`ERA-EXACT-125`, `ERA-B-FIRST-BODY`, `ERA-B-U1`,
  `REFUSAL-VERSIONS`); the landed gate reads 96/96 `met` ×3 canonical + ×3 clone; N01-N04 each read
  `unmet` ×3 both layouts with the named family in `failed_families` and 0 error rows.
- **C2 — operability 9 (assurance arm + capability acquisition)** — `--limine-version auto` probes the
  installed bootloader read-only, records `limine_version`/`limine_version_source`, selects the era
  from the probed value, and refuses on the certified failure shapes; `AUTO-ERA-A`, `AUTO-ERA-B`,
  `AUTO-PROBE-FAIL` `met` ×3 both layouts; N05/N06 `unmet` ×3 both; the live receipts show
  12.9.4/`probe`.

- **Freeze and instruments.** `tools/limine-pin-battery-r93.py` (96 families; the r92 ISOLATION
  launcher plus the V3 PATH exception), `tools/check-limine-pins.py` V3 (`probe_limine_version`,
  `auto`, `limine_version_source`, selftest 37 → 39 rows), `tools/make-r93-bends.py` (six one-clause
  bends), do-nothing controls (r92 gate `35c1088b…`, r92 battery `aef33925…`), a 14-line freeze
  manifest and a 13-line instrument-only manifest — all at `c633f49a`
  (`.ufo/waves/round-93/before/{freeze-manifest,instruments}.sha256`).
- **C1 measurements (L1).** Landed gate `96/96 met` ×3, 0 error rows (`after/c1-canonical.json`);
  N01 `95/96 unmet` failed `ERA-EXACT-125`, N02 `88/96 unmet` failed `ERA-B-FIRST-BODY` (+7
  collateral), N03 `95/96 unmet` failed `ERA-B-U1`, N04 `95/96 unmet` failed `REFUSAL-VERSIONS`,
  ×3 each, 0 error rows (`after/bend-N0*.json`, `after/bend-family-matrix.txt`).
- **C1 clone legs.** Seat ExecReplicate: `git clone --shared` at the freeze commit, instruments
  14/14 manifest-clean there; gate `96/96 met` ×3 and N01-N04 `unmet` with the named family
  (one run each, cross-check) — `w1/ExecReplicate.md`,
  `w1/ExecReplicate/compare-clone-vs-canonical.txt`. The claim's ×3-per-bend clone leg is supplied
  by the round's own clone run: `after/clone-gate.json` (3 runs, `96/96 met`) and
  `after/clone-bend-N0{1,2,3,4}.json` (3 runs each), all 0 error rows — amendment A3, CriticClaims F7.
- **C2 measurements.** Landed gate auto families 4/4 in every canonical run and in the clone (the
  clone gate ×3 above); N05 `95/96 unmet` failed `AUTO-ERA-B`, N06 `95/96 unmet` failed
  `AUTO-PROBE-FAIL`, ×3 canonical and ×3 clone (`after/bend-N05*.json`, `after/bend-N06*.json`,
  `w1/ExecAutoReplicate/{n05,n06}.json`).
- **C2 live.** Root/L1 receipt (read-only; `/boot` digest `cmp`-identical before/after):
  `--live --limine-version auto` → rc 1, `limine_version 12.9.4`, `limine_version_source probe`,
  `visibility_era pre-12.9.5`, `LP-MISMATCH line 30`, `LP-MISMATCH line 38` (`after/live-c2.json`,
  `after/live-boot-digest-*.txt`). Unprivileged seat ExecLive: same two fields with rc 2
  `CANNOT-EVALUATE` (`w1/ExecLive/live.stdout`), probe syscall-traced `O_RDONLY`-only, probe edge
  cases (absent, exit 1, garbage, stderr-only, 5.012 s timeout) all refused, and era selection
  identical to the explicit flag (`w1/ExecLive.md`).
- **Do-nothing legs.** r92 gate vs the r93 battery: `94/96 unmet`, failed
  `AUTO-ERA-A,AUTO-ERA-B`, 8 error rows; `AUTO-PROBE-FAIL` passes there (a blanket refuser
  satisfies a refusal family) — amendment A1, lesson M2. The r92 battery has none of the seven new
  names (`grep -c` = 0, `after/do-nothing-roster.txt`) and scores the landed gate `89/89 met`
  (`after/r92-battery-on-r93-gate.txt`, no regression); the battery's `constant-healthy` selftest
  gate reads `0/96` (`after/battery-selftest-noref.txt`).
- **Lane gates.** Gate selftest `PASS 39/39`; `--usage-check` `met` (11 cases); battery selftest
  without `--reference` `PASS 5/5` (`after/battery-selftest-noref.txt`) and the 18-leg reference run
  NOT completed in the wave timebox (ExecLints F3: the battery prints only after all legs, so a
  killed run proves nothing — routed); registry coverage at the freeze revision flagged the two new
  tools (`w1/ExecLints/registry-coverage.log`, the red leg), repaired in SKILL.md (two rows +
  R93-REG-1) and re-run at the landing commit `b02384c7`: PASS 147/147
  (`after/registry-coverage-tip.json`); knowledge headers 109/109 and refs 0 dangling at
  `b02384c7` (`after/knowledge-{header,refs}-tip.json`); line endings PASS (477 files); host census
  rollup DEGRADED, `systemd` moving to DEGRADED on 4 failed user units (host state, baseline rc 1
  reproduced, `w1/ExecLints/census-live.log`); sources census 385 rows exit 0.
- **Frontier step.** SOURCES 381 → 385 rows (S382-S385, tier A); knowledge entry
  `corpus/knowledge/limine-version-probe-r93.md`; anchor changes S377 (3.14 → 3.15.2) and S384
  (raw 2029 → 2035) logged old→new with QUALITY-127 sweep receipts; mistakes mined into
  `corpus/lessons/round-93.md` (M1 landing smoke, M2 calibration, M3 inherited landing, M4 curation).
- **Freeze-manifest scope (honest reading).** The 14-line freeze manifest pins 13 instruments/controls
  plus the declaration; the r92 manifest (A8) pinned 28 lines with no declaration, so the declaration
  line is this round's over-pin. At the freeze commit the manifest verifies 14/14
  (`w1/ExecReplicate/clone-identity.txt`); in the worktree its plan line changes only by the plan's own
  appended amendments A1-A3. The claim's void leg is therefore read against
  `before/instruments.sha256` (13 lines, instruments/controls only), which verifies clean at the
  landing tip; ExecBends, ReviewBattery, MutAuto, ReviewGate F3 and CriticClaims F6 measured the same
  split.
- **Round-92 spot-check routed defects (5).** Routed 1: the four commits the r92 table missed
  (`b5cb636a`, `98185b9b`, `1d1c7439`, `7793773a`) are named in Landed changes. Routed 2: registry
  coverage re-run at this round's tip and committed. Routed 3: S377's anchor corrected by a logged
  change plus the appended S385 (version-pinned URL). Routed 4: `claims.json` C2's frozen literal
  stays; the A7 §5 pointer is restated here. Routed 5: the pre-A3 usage receipts stay labelled and
  are not cited for any r92 number.
- **Wave w1 (14 seats, 7 attack = 50 %, 0 dead).** ExecReplicate (clone gate ×3 + bends ×1
  cross-check, `compare-clone-vs-canonical.txt`), ExecAutoReplicate (clone auto legs, N05/N06 ×3),
  ExecBends (independent canonical ×1 of six bends + both do-nothing legs, `compile.txt`, `diffs.txt`),
  ExecLints (gate selftest 39/39, census selftest 218/218, lane checkers: the freeze-revision registry
  red leg and the landing green, `census-live.log`), ExecLive (probe trace and edge cases), ScoutSource
  (source pins, S384 locator correction, S385 proposal), ScribeLesson (number check, criteria review,
  M1 evidence correction, 138 draft), ConnectorOverlap (20-repo sweep, 0 conflicts),
  ReviewGate (8 findings: probe grammar, UTF-8, manifest, N02), ReviewBattery (7 families by hand,
  F1-F8), CriticClaims (F1-F7: live parenthetical, parse clause, timeout certifier, manifest, the
  missing clone ×3 leg), CriticForgers (independent gate 96/96, f1-f6 forgery, f6 survivor + fixture
  leakage), MutEra (16 mutants: the four families are each the sole killer of their clause class;
  M13 10-digit cap survives — routed), MutAuto (12 mutants: 6 killed, 5 survivors, M12 timeout rows;
  gaps routed). Findings drove A1-A3, criterion 138 and the routed list.
- **Pre-file falsification ledger.** `python3 scripts/hyaku/prefile-falsification.py --lane tsukuroi
  --round 93` → `PREFILE-FALSIFICATION: pass claims=2 rows=15 attack_seats=7 findings=0`, exit 0
  (`.ufo/waves/round-93/claim-falsification.tsv`; all 7 attack seats read, 5 `falsifies-wording` rows
  each pointing at the plan amendments).

## Landed changes

| commit | what it carries |
|---|---|
| `c633f49a` | freeze: `tools/limine-pin-battery-r93.py` (`ddd7e955…`), `tools/check-limine-pins.py` V3 (`6b4c53d1…`), `tools/make-r93-bends.py` (`d0c3d3e7…`), the six bends, the two do-nothing controls, `claims.json`, `.ufo/plans/round-93.md`, SCORECARD "Round 93 — declaration", the 14-line freeze manifest |
| `b02384c7` | land: `corpus/SOURCES.md` S382-S385, `corpus/knowledge/limine-version-probe-r93.md`, `corpus/lessons/round-93.md`, `corpus/QUALITY.md` 136/137, `corpus/README.md` round-93 frontier, `SKILL.md` rows + R93-REG-1, `SCORECARD.md` outcome + capability `installed-version-probe`, `LOG.md` round-93, plan A1-A3, `after/` canonical+clone receipts, wave spec/ready/dispatch |
| `9f66744e` | settle: `.ufo/waves/round-93/w1/` (14 seat receipts + `w1-results.json`), `claim-falsification.tsv`, tip receipts, plan A4, `corpus/QUALITY.md` 138, SKILL R93-REG-1 extension, the reworded S377/S384 corrections |
| `42979f5a` | tip receipts re-run at the settle tip (`registry-coverage-tip.json` PASS 147/147, `knowledge-{header,refs}-tip.json` 109/109 and 0 dangling, `line-endings-tip.txt` PASS 477, `q127-s377-landing.txt` rc 1 on both phrases) |

Round-92 report rows appended here for the r92 spot-check's routed defect 1 (reports are never
rewritten): `b5cb636a` (w1 settlement, results.json, ExecLints and ReviewSource reports), `98185b9b`
(A9 number corrections, K1 leg fixed and re-measured, results.json committed), `1d1c7439` (K1
do-nothing receipt from the fixed leg: 1/89, 352 error rows, ERA-DEFAULT the only pass), `7793773a`
(A8 manifest regenerated after the run-c1 fix, 28 lines, sha `8f48d358`). Each is tied to the r92
LOG entry's round-92 block.

## Before → after measurements

### C1 — depth 8 (the tied lowest non-retired axis)

Counting command: `python3 tools/limine-pin-battery-r93.py --gate tools/check-limine-pins.py --runs 3
--work <scratch> --json <out>` (instruments pinned by `before/instruments.sha256`; measured at the
freeze `c633f49a`, re-verified at the landing tip by the same manifest).

- Before: the r92 roster (89 families) has none of the four families (`grep -c` = 0,
  `after/do-nothing-roster.txt`), and the r92 battery scores the landed gate `89/89 met` without
  sampling the target (`after/r92-battery-on-r93-gate.txt`).
- After: landed gate `96/96 met` ×3 canonical (`after/c1-canonical.json`) and ×3 in a
  `git clone --shared` (`after/clone-gate.json`); N01-N04 `unmet` ×3 canonical (`after/bend-N0*.json`)
  and ×3 clone (`after/clone-bend-N0*.json`), each with its named family and 0 error rows
  (`after/bend-family-matrix.txt`).
- Verdict: **met** on A2's narrowed wording (C1-1 N02's label, C1-2 the tenth refusal member,
  C1-3 empty-or-whitespace-only stdout).

### C2 — operability 9 (assurance arm; capability `installed-version-probe`)

Counting command: the same battery invocation with the `count-runs.py` family filter, plus
`python3 tools/check-limine-pins.py --live --limine-version auto`.

- Before: the r92 gate rejects `auto` with rc 64, so `AUTO-ERA-A`/`AUTO-ERA-B` fail on it
  (`after/c2-donothing-r92-gate.json`: `94/96 unmet`, 8 error rows); `AUTO-PROBE-FAIL` passes there
  by refusal shape (A1).
- After: the three auto families 4/4 in every canonical run and in the clone; N05/N06 `unmet` ×3
  both layouts with the named family and 0 error rows; the live receipts print `limine_version
  12.9.4`, `limine_version_source probe` (root rc 1, lines 30/38; unprivileged rc 2, same fields).
- Verdict: **met** on A2/A3's narrowed wording (C2-1 mechanism certifier, C2-2 certified failure
  shapes, C2-3 the privileged live parenthetical, C2-4 the parse clause, C2-5 the timeout certifier).

## Sources & frontier

- **SOURCES before → after.** `381 → 385` rows; counting commands
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
  and `grep -c '^| S[0-9]' corpus/SOURCES.md`: at round start **381 rows, exit 0**; at round end
  **385 rows, exit 0** (`after/census-after.txt` carries the validate warnings/ok lines; the count is
  the grep's, re-runnable at the tip).
- **Rows added by tier.** Tier A: S382 (Limine v12.9.5 `common/lib/config.c`), S383 (v12.9.5
  ChangeLog), S384 (v12.9.5 `host/limine.c`), S385 (version-pinned Python 3.15 docs page, the appended
  supersession of S377's locator). Tier B/C: none.
- **Rows touched old→new.** S377 anchor `Python 3.14 docs` → `Python 3.15.2 docs`; S384 anchor
  "print at raw 2029, `--version-only` raw 2022-2026" → "print at raw 2035, `--version-only` print at
  raw 2031"; both logged in `corpus/lessons/round-93.md` §Gate with the QUALITY-127 sweep receipt
  `after/q127-s377-pre.txt` (prints the old S377 cell at the freeze revision) and its landing leg.
  No status/`recheck`/`used-by` change.
- **Frontier rows advanced.** The round-92 frontier's "12.9.5-exact boundary", "first body line after
  the cut", "era-B U1" and "`N04-accept-any`'s family-level survival" are closed by families whose
  bends name them; the r92 gate's fixed-era default is answered by V3. Still open: the r92 launcher
  residuals (A6), the probe's grammar leniency (suffix/extra components; ReviewGate F1,
  CriticClaims §5), the AUTO fake's source leakage (CriticForgers §3), the N02 bend's corrected shape
  (ReviewBattery F1), the ESP-containment family (CriticForgers A1), and the r89 frontier (blanks
  before CR-LF, ESP containment, empty labels).
- **Assimilation: none** — the `merge/tsukuroi/` package's 70 entries target surfaces this lane already
  holds at a later round (hook order r38-r40, initramfs v42, pacnew, snapper, btrfs repair/space) and
  none touches the Limine/gate surface this round changes; nothing was adopted, per the contract's
  no-penalty line. `considerthese/2026-10-26.md`: every proposal is already adopted (QUALITY 103, 108,
  110, 112, 115; r90 lesson Gate); none mined this round.
- **PREFILE-FALSIFICATION:** pass claims=2 rows=15 attack_seats=7 findings=0 (exit 0)

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the lane did not hold (the v12.9.5
  tag's own cut, the release note that dates it, and the `limine --version` print site) whose
  `source:` cites three `mined` rows opened this round (S382-S384), plus S385; SOURCES 381 → 385.
- **quality — improved.** The battery gains seven families each tied to a one-clause bend; the r92
  survivor `N04-accept-any` is killed at family level; the gate's probe is implemented with a refusal
  path and a source field; the registry gains the two new tools plus R93-REG-1; two anchor cells are
  corrected with sweep receipts; the r92 battery still scores the new gate `89/89` (no regression).
- **discernment — improved.** The wave's attack seats falsified five predicate wordings (A2/A3) and
  the round narrowed rather than filed them; the do-nothing legs are honest (A1), and the attack
  artifacts are the ledger's adversaries, not a re-reading of the receipts.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointers:
  `SKILL.md` registry rows `limine-pins` (R93-REG-1), `limine-pin-battery-r93`, `make-r93-bends`;
  `corpus/knowledge/limine-version-probe-r93.md`; non-author verification remains owed (the closure).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: the LOG round-93
  entry and the live run `after/live-c2.json` (root) with `w1/ExecLive.md` (unprivileged).
- [~] Instructions executable by an agent without oral context — pointers: the wave items in
  `.ufo/waves/round-93/w1-spec.json` were executed by 14 seats, and the battery's docstring +
  `--selftest` reproduce every family; QUALITY 128/136/137 carry the round's rules. The whole-SKILL
  no-oral-context retest remains unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round stays on the owned boot/Limine
  surface; ConnectorOverlap's 20-repo sweep found no contradiction and no absorbed sibling ground
  (`w1/ConnectorOverlap.md`). Contested kaidoku/revenger RE ownership stays unruled.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No pacman transaction, no `uv`/`npx`/cargo install; pacman stays paused per the addendum guard.
