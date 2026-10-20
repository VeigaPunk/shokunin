# mado — round 17 report (hyaku phase 2, attempt 1)

Lane HEAD (pushed): `6046ab72b18dd0e68c3116cb2c0134ba6f687beb`. Baseline `27cd06f`
(admitted round-16 closure). Pre-registration `0175f13`. Admission is **not**
asserted here; independent non-author closure and operator disposition remain
required. This round does not readmit round 15.

## Work performed

Declared claims (SCORECARD.md § "Round 17 — declared claims (2026-10-20)",
corrections § "Round-17 pre-measurement corrections"):
**C1 calibration** (lowest scored axis at declaration), **C2 coverage** (new
declared rubric V over PROVINCE surfaces P1-P6; it became the lowest row once
declared, and both lowest rows were worked), **C3 operability — capability
acquisition** (post-hoc transcript tripwire). No exploratory claim.

- R16-V1 routed: append-only erratum `corpus/lessons/round-16.md` § "Erratum
  (round 17, append-only) — R16-V1"; recut tamper control
  `.ufo/waves/round-17/evidence/frozen-tampered-recut.json` (tampered exit 2
  `snapshot_tampered`, control exit 0 `frozen_match`, gate `226220ae…`).
- QUALITY 23 (receipt-label precision) `corpus/QUALITY.md:111`, cited to
  `lessons/round-17.md#mistakes M1`; runnable check
  `.ufo/waves/round-17/label-check.py` + `label-claims.json` (red R16-V1 line,
  want-side and wrong-revision mutants, greens) → `evidence/label-check-final.txt`
  `EXPECT_SUMMARY: 7/7`, exit 0, R16-V1 line MISMATCH.
- Rubric-V instrument committed before any note landed (`f52f43f`, tightened
  `ab0bc9b`, hardened after wave 2 in `f71ccbe`; stricter only; baseline 2/6 under all).
- Two sourced documentary routes: `corpus/knowledge/idle-lock-route-r17.md`
  (`surface: P6`, hypridle v0.1.8 / hyprlock v0.9.6) and
  `corpus/knowledge/terminal-route-r17.md` (`surface: P4`, `scope:` one
  Alacritty-only route via xdg-terminal-exec v0.14.3, Alacritty v0.17.0);
  SOURCES S056-S071; README index rows and Frontier bullet.
- `tools/mado-tripwire.py` (written by L1 after seat TripwireCore died),
  suites `tripwire/{core,compound,hardening,w2-regressions}`; real-transcript
  receipts `evidence/tripwire-r13..r17.txt`, `tripwire-anchor-r15.txt`,
  `tripwire-vs-oracles.json`, `tripwire-pacmanlog-join.txt`; SKILL registry
  rows, limit paragraph and usage subsection.
- Wave 1 (build): 70 seats. Wave 2 (falsify): 78 seats, one attack item each;
  corrections integrated at `f71ccbe` (`lessons/round-17.md` § "Wave-2 corrections").
- Planner seat: held by L1 (validator rejects `planner`); planning data-walks
  rode RevPreRegistration, RubricBaselineScout and CalibrationBaselineScout.

Stale-lane: respawn-per-round driver; no other mado mission is open; no
round 18 work was started. Inherited state: clean tree at dispatch; the
non-author `round-16-verifier-spotcheck.md` and the operator's
`considerthese/2026-10-20.md` (a reflection, not an operator teaching) were
read and left unedited; no `corpus/lessons/operator-*.md` exists. Tool
installs: none (L1 and all reporting seats).

## Landed changes

All on the mado remote (`git -C mado-shokunin log 27cd06f..6046ab7`, all
`mado-shokunin <mado@shokunin.local>`); LOG.md § "2026-10-20 — round 17:
receipt labels, P4/P6 sourced routes, transcript tripwire".

| Commit | Change |
|---|---|
| `0175f13` | pre-registration + census start |
| `f52f43f`, `ab0bc9b` | rubric-V instrument bound, then tightened (before integration) |
| `a9998d1` | C2: P4/P6 notes, SOURCES S056-S070, README rows |
| `fc6f960`, `245fd11` | wave-1 evidence receipts; label-check mutant fixture |
| `3722ba4` | C1: QUALITY 23, round-16 erratum, label check, lesson round-17 |
| `3e9848a` | SCORECARD pre-measurement corrections |
| `988b858` | C3: tripwire tool, suites, real-transcript receipts, SKILL rows, lesson M2 |
| `f71ccbe` | wave-2 corrections: tripwire fixes + 26-case regression suite, S066 digest / S059 / S061 / S062 / S070 anchors, S071, note scope/anchors, label-check and measure hardening, both waves' reports |
| `6046ab7` | results tables, capability row, harm watch, final receipts, LOG |

## Before → after measurements

| Claim | Counting command | Before @ `27cd06f` | After @ `f71ccbe` (= content of `6046ab7`) |
|---|---|---|---|
| C1 | `git show REV:corpus/QUALITY.md \| grep -cE '^[0-9]+\. .*lessons/'` over `grep -cE '^[0-9]+\. '` (also `python3 .ufo/waves/round-17/measure.py REV`) | 14/22 = 6.3636 | 15/23 = 6.5217; semantic block counter 17/22 → 18/23 |
| C2 | `python3 .ufo/waves/round-17/measure.py REV` (sha256 at `f71ccbe` in `evidence/measure-final.json` run) | 2/6 = 3.3333 (P1, P2) | 4/6 = 6.6667 (P1, P2, P4, P6) |
| C3 | `python3 -I tools/mado-tripwire.py --selftest .ufo/waves/round-17/tripwire/<suite>`; `--scan …/MadoR15/MadoR15.LibinputEvents.jsonl` | absent (`git show 27cd06f:tools/mado-tripwire.py` fails) | present, sha256 `7a98720e…`; 9/9, 16/16, 33/33, 26/26 exit 0; anchor exit 1, line 54 `call_38165` `sudo` + `pacman:-S` (8 findings / 7 calls) |

Separability replayed by wave 2 (AttackSeparability): reverting each claim
commit moves only its own counter. Harm watch at `f71ccbe`: legacy hermetic
selftest 372/372 (gate sha `fba82a66…` unchanged), classifier selftest 52/52,
U-routes 7/7, navigation 32/32, census exit 0. Freshness not re-measured.

C3 second authority: `/var/log/pacman.log` (file read) joins all 4 mado-window
package transactions (lines 2410, 2422, 2423, 2429) to one issued `sudo pacman`
call each — 4/4 by call start time, 3/4 by record timestamp (one multi-call
provider-history record). Tripwire ⊇ every non-clean oracle row (oracle_only 0
in rounds 13-16). Honest limits: adversarial suite 4/26
(`evidence/tripwire-w2-adversarial.txt`); three real executed `pacman -Q` calls
hidden behind variable/helper spawns (`MadoR14.SourceSafety:152,155`,
`MadoR13.jsonl:470`).

## Sources & frontier

SOURCES rows 55 → 71 (`awk -F'|' '$2~/^ *S[0-9]{3} *$/' corpus/SOURCES.md`):
added tier A 13 (S056-S060, S063-S069, S071), tier C 3 (S061, S062, S070);
mined 43 → 56, rejected 4 → 7, queued 8 unchanged. Rows touched old→new: none
of the pre-round rows; same-round corrections (S066 digest nibble, S059 range,
S061/S062/S070 anchors) logged in `lessons/round-17.md` § Wave-2 corrections.
Census start (`evidence/census-start.txt`) and end (`evidence/census-end.txt`):

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
exit=0          (identical output at start 10:56 and end 12:09)
```

Frontier advanced: P6 idle/lock and one Alacritty-only P4 route moved onto
documentary sourced ground (README § Frontier); P3 Walker, P5 themes and all
behaviour remain open. Sourced claim: C2 rests on rows opened this round
(S056-S071). Mined mistakes: `lessons/round-17.md` § Mistakes M1-M5 (each fix
shown able to fail: label-check red line; instrument tightenings; tripwire
anchor exit 1), plus § Wave-2 corrections. Search log and Paths entries for
round 17 added to SOURCES.md.

## Trend verdicts

- **Expansion: improved (narrow).** Two new documentary routes on owned
  surfaces from 13 opened tier-A rows, and one new capability; rubric V 2/6 →
  4/6. Not behaviour coverage; P4 is Alacritty-only.
- **Quality: improved.** R16-V1 erratum + recut receipt; S066/S059/S061/S062/
  S070 and note anchors corrected under falsification; tripwire hardened with
  a 26-case regression suite; instrument made stricter. Freshness debt from
  the 09:15 non-lane `-Syu` is open, not addressed.
- **Discernment: unprovable-but-better pending outside check.** The routed
  outside defect became a criterion with a failing control, and the tripwire
  surfaced breaches the lane's own lessons had missed (r15 `sudo -n true`,
  r16 second `pacman -Q waybar`). These are author/lane-seat findings; no
  non-author agreement exists yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md gate registry rows `mado-tripwire`, `mado-label-check`, `mado-round17-measure` and the round-17 tripwire subsection; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — historical (round 3); round 17 ran no desktop task (host pause).
- [~] Instructions executable by an agent without oral context — `tools/mado-tripwire.py` usage in SKILL.md; lane-dispatched seats are not outside verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged; the mori `man-pages` install was reported, not absorbed (`evidence/tripwire-pacmanlog-join.txt`).

## Waves, seats, dead seats, misroots, L0

- Wave 1: 70 seats — scout 22, executor 11, reviewer 10, scribe 9, connector 8,
  revenger 4, critic 4, sentinel 2. Dead: 1 (`MadoR17.TripwireCore`, executor
  → m_swe: "Devin stream error resource_exhausted: Reached free model rate
  limit"; not respawned — L1 wrote the tool).
- Wave 2: 78 seats — reviewer 29, scout 25, critic 7, mutation-tester 4,
  connector 4, revenger 3, executor 2, sentinel 2, simplifier 2. Dead: 0.
- Round total 148 seats (≤200). No job-cap refusal.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows only driver state (`.ufo/state/*.report-baseline`, watchdog.log) and
  orchestrator files (`scripts/hyaku/jj-lane*.sh.new`); no mado seat file at
  the fleet root (wave-2 MisrootSweep agrees).
- Seat conduct (C3 over round 17's 149 transcripts): one `live_probe`
  (`ps -eo pid,etimes,cmd`, `MadoR17.RevSeparability.jsonl:152`, wave 1,
  before `ps` was named in a context); no package or host-mutation call in
  covered forms; 136 unparsed spawns, so `clean` would not have meant none ran.
- Host: pacman.log has 0 runs from round launch (10:51) to close
  (`evidence/pacmanlog-round-window.txt`); 13 earlier runs 07:45-09:39
  (including `pacman -Syu`, mkinitcpio 41.1→42.2) have no recorded actor.
- L0: no new question. The host-recovery decision stays on existing lines
  `.ufo/l0-questions.md` L54/L55 (R15-V1 operator-owned, current state `[UNK]`).
