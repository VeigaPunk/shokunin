# kasegi — round 42 (attempt 3)

Lane `kasegi-shokunin`. Round shape: **two v1 waves declared; wave 1 ran, wave 2 handed off but not taken.**

- Wave 1 `kasegi-r42-build` — **64 seats**, dispatch `.ufo/waves/round-42/wave1-dispatch.json`, results
  `.ufo/waves/round-42/kasegi-r42-build-results.json` (64 results, 0 dead). Role mix: executor 19, scout 11,
  critic 8, reviewer 8, scribe 7, mutation-tester 5, connector 2, sentinel 2, simplifier 1, revenger 1 —
  attack roles 21/64 = **32.8 %**.
- Wave 2 `kasegi-r42-falsify` — **36 seats** rendered and validator-validated under policy v1
  (`.ufo/waves/round-42/wave2-spec.json`, `.ufo/waves/round-42/wave2-dispatch.json`, `counts.spawn=36`,
  attack roles 31/36), handoff written at `.ufo/waves/round-42/kasegi-r42-falsify.ready` (l1 `KasegiR42a3`).
  The orchestrator's dispatcher did not take it inside this round's window: no `.ready.dispatched` marker,
  no `wave2-results.json`, no seat spawned. **Round total = 64 seats** (band 64–128, ceiling 256); the
  falsification that did run is the instrument's own thirteen graded selftest mutants plus the seven replay
  limbs at Y (below).
- Judged head **J = `4c40ef21cced6ebed592e5622996ab41996e2da9`**; verification ref
  **Y = `b2c49ea5e7bc214e91c2b0bede5d4eaed4968572`** (J + the receipt only). Lane tip and remote
  `master` = **`b2c49ea5e7bc214e91c2b0bede5d4eaed4968572`**.

## Work performed

Declared claims (frozen `.ufo/waves/round-42/claims.json`, commit `0566bd66`, clarified by errata 1–4):

- **C1 — depth:verifiability (4, held).** `corpus/instruments/r42-closure.sh` runs export-mode only and
  prints `closed=13/13 exit=0` at Y with a graded selftest of thirteen `verdict=pass` lines
  (`selftest cases=13 failures=0`); base and round-41-head exports red; plain run refused exit 2; a distinct
  ref-not-found red; every J1–J7 replay limb rejecting its committed defeat artifact.
- **C2 — coverage (8, held).** F25 admitted 24 → 25 (CVE Record Format) with README frontier row and
  PROVINCE amendment; registry S064 `mined` plus two screened rejects; the knowledge entry with its
  provenance trio; harness `entries=28 pass=28` incl `PASS F25`; binding `records=56 bound=56`; audit
  `expected=61`; census exit 0; measure 45/45.

Work items (evidence pointer in parentheses):

- Read the round prompt in full and loaded `skill://shokunin`, PROTOCOL/MISSION/AXES/CORPUS/LEARNING,
  `skill://swarm`, the lane SKILL/PROVINCE/SCORECARD and `corpus/lessons/round-41-verifier-spotcheck.md`.
- **Inherited state resolved.** Attempts 1–2 landed wave 1 (64 seats, 0 dead), the instrument, the C2
  material and an uncommitted wave-2 handoff (its `.ready` was poisoned — pointed at a spec without
  `taskCall` — and had been removed at `de09313`). The inherited instrument scored `closed=10/13`,
  `selftest cases=13 failures=3`; four implementation defects made the frozen after-state unreachable. All
  four were repaired **inside the frozen predicate** and recorded as erratum 4
  (`.ufo/waves/round-42/claims-erratum-4.md`); no target, counter, kill rule or score moved.
  - **E-R1 J1 replay substrate.** `replay_j1`/`strip_evidence_copy` mutated the first correction line whose
    evidence changed, whatever its round; `check_j1` grades only `Correction (round 42)` lines, so the strip
    landed on a round-39 line and J1 accepted its own mutant. Repair: `graded_lines()` selects round-42
    claim-bearing lines and the strip must remove every evidence id
    (`corpus/instruments/r42-closure.sh:1228-1243`, `1741-1756`).
  - **E-R2 J1 `union` literal.** The payload printed `union=0` unconditionally; it is now the count of graded
    records a cross-record union would have covered (`r42-closure.sh:507-568`).
  - **E-R3 J4 `dyn` absence.** The receipt is declared `dyn unpinned`; its legitimate absence at J counted as
    an escaping declaration. A `dyn` declaration is now valid while absent, still rejected if absolute,
    `..`-bearing or resolving outside the export root (`r42-closure.sh:640-676`).
  - **E-R4/E-R5 J10 grading and J8/J10 self-reference.** `line_ok` was `verdict == pass`, and J8/J10 graded
    payloads computed after the selftest returned, so `payload-match` was structurally 0. `run_selftest`
    now iterates to a fixed point planting J10 and J8 payloads before grading; `line_ok` means a graded
    `selftest case=J<n> …` line was emitted; J8's canonical mode grades a synthetic all-pass graded block
    while a committed receipt is still graded from its own bytes (`r42-closure.sh:1548-1560`,
    `2052-2085`).
- Preserved the red pre-repair transcript as
  `.ufo/waves/round-42/final-gates/all-gates.pre-repair.txt` (J1 `replay=…=accepted`, J4 `escape=1`,
  J8/J10 `payload-match=0`, `selftest cases=13 failures=4`) — the reds stay citable.
- Regenerated the declared-block pins at the integration head (469 rows, 0 missing, the suite pinned by
  sha256; `.ufo/waves/round-42/declared-blocks.txt:1-469`).
- Minted the receipt at J and committed it as Y; re-ran run, selftest, plain-run refusal and
  unresolvable-ref red at Y (`/fast/scratch/hyaku/kasegi-r42/verify-Y.txt`, transcript quoted below and in
  the receipt itself).
- Mined this round's mistakes into `corpus/lessons/round-42.md` §Mistakes — **M42-3** replay-substrate,
  **M42-4** self-referential payload-match, **M42-5** wrong-absence on a `dyn` declaration — each with class,
  evidence pointer, the criterion that should have caught it, the fix, and a demonstrated failing case.
- Rendered, validated and handed off wave 2 (36 seats, `wave2-dispatch.json` through
  `ufo-swarm-wave.mjs run --spec` under `scripts/hyaku/ufo-wave-policy.json`); the dispatch carries the
  erratum-4 note so seats attack the current bytes rather than the pre-repair reds. Not taken by the
  dispatcher in-window (state above).

## Landed changes

Tied to `LOG.md` §Round 42 (`LOG.md:1754` onward) and the commit carrying each change:

| Change | Commit |
|---|---|
| Frozen claims, controls, wave-1 spec/dispatch; errata 1–3 | `0566bd66`, `27e18d2`, `8be06a9`, `514ff62` |
| Wave-1 build integration: instrument, J6/J7 repairs, F25/S064 knowledge+registry+manifest, SKILL.md registry repair, scribe/SCORECARD/LOG/SHONEN/QUALITY appends | `857cac4` |
| S064/S065/S066 registry, province and SCORECARD append corrections | `29061f6` |
| r42-closure suite, J1/J4 closures, settled wave-1 evidence, receipt at the integration head | `f66b8e0`, `0a7ca53`, `d238e36` |
| 13/13 suite candidate and wave-2 handoff (poisoned ready later removed) | `9d971cf`, `de09313` |
| Erratum 4, four instrument repairs, measured r42 rows, M42-3..5, declared pins | `49259a01` |
| Receipt at `49259a01` (intermediate green pair) | `697c6b9b` |
| Wave-2 spec/dispatch/registry/ready + Y0 verification transcript | `694a88e6` |
| **Judged head J** — receipt dropped, final mint from this tree | **`4c40ef21`** |
| **Receipt Y** — teed run+selftest transcript at J | **`b2c49ea5`** |

## Before → after measurements

Commands run from the lane root; the suite in export mode with private `--work` under
`/fast/scratch/hyaku/kasegi-r42/`. Every value below was re-derived at the commit named.

**C1 — depth:verifiability (4 held → 4 held, verified at Y `b2c49ea5`).**

| # | Counting command | Before | After |
|---|---|---|---|
| 1 | `bash corpus/instruments/r42-closure.sh` (plain) | exit 127 at base — instrument absent (`c1-controls/do-nothing.txt`) | `plain exit=2` (refused, export mode only) |
| 2 | `bash corpus/instruments/r42-closure.sh --export-ref <Y>` | base `5053a7f4…` → `closed=5/13 exit=1`; r41 head `1f746461…` → `closed=4/13 exit=1` | **`closed=13/13 exit=0`** |
| 3 | `bash corpus/instruments/r42-closure.sh --selftest --export-ref <Y>` | r41 suite at base `selftest cases=12 failures=8` | **`selftest cases=13 failures=0`** with 13 `positive=pass … verdict=pass` lines |
| 4 | `… --export-ref 5053a7f46de35784cff4b56756906e9014a38276` | — | `closed=5/13 exit=1` |
| 5 | `… --export-ref 1f7464612ac4c44e39886b82e812610d3c039b13` | — | `closed=4/13 exit=1` |
| 6 | `… --export-ref deadbeef…` | — | `ERROR ref-not-found ref=deadbeef… closed=0 exit=1` (exit 1) |

The seven replay limbs at Y, from the same run:
`J1 …replay=RevC1Counters.md=rejected` · `J2 …RevC1Counters.defeats.txt=rejected` ·
`J3 …MutSkillTablePipes.md=3/3` · `J4 …CritDeclarationCoverage.md=2/2` ·
`J5 …MutScratchTiming.md=outside=detected,inside=detected` · `J6 …MutBindingExistence.md=rejected` ·
`J7 …MutFrontierParser.md=rejected`. J8 at Y: `receipt=.ufo/waves/round-42/final-gates/all-gates.txt,
source=committed,…,payload-match=12/12,forged=6/6 closed=1`.

Receipt (committed at Y, `.ufo/waves/round-42/final-gates/all-gates.txt`, 33 lines):
`export-ref=4c40ef21…`, `suite-sha256=fca5ae62…`, `time-basis=ref-commit`,
`run-utc=2026-10-28T15:12:46Z`, `closed=13/13 exit=0`, `selftest cases=13 failures=0`.

**C2 — coverage (8 held → 8 held, verified at Y).**

| # | Counting command | Before (`c2-controls/before.txt`) | After |
|---|---|---|---|
| 1 | `grep -cE '^\| F[0-9]+ \|' corpus/README.md` | 24 | **25** (F25 admitted) |
| 2 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 63 | **66** (S064 mined; S065/S066 rejected — erratum 1) |
| 3 | `awk -F'\|' '/^\|[[:space:]]*S064[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); if(s=="mined") n++} END{print n+0}' corpus/SOURCES.md` | 0 | **1** |
| 4 | `grep -rlE '^source: S064' corpus/knowledge \| wc -l` | 0 | **1** |
| 5 | `ls corpus/knowledge/*.md \| wc -l` | 60 | **61** |
| 6 | `python3 corpus/instruments/frontier-recheck-count.py` | `entries=27 pass=27` | **`entries=28 pass=28 exit=0`** incl `PASS F25` |
| 7 | `python3 corpus/instruments/capture-binding-check.py` | `records=55 bound=55` | **`records=56 bound=56 unbound=0`** |
| 8 | `python3 corpus/instruments/recheck-audit.py --quiet` | `expected=60` | **`expected=61 missing=0 unexpected=0 exit=0`** |
| 9 | `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` | exit 0 (`W04 S028`, `W04 S029`) | **exit 0** (same two standing warnings, `ok`) |
| 10 | `awk -F'\|' '/^\| F[0-9]+ \|/{tot++;s=$4;gsub(/[ \t]/,"",s);if(s=="admitted")adm++} END{printf "%d/%d = %.3f\n",20+adm,20+tot,(20+adm)/(20+tot)}' corpus/README.md` | 44/44 = 1.000 | **45/45 = 1.000** |

Do-nothing control: `c1-controls/do-nothing.txt` (r42 instrument absent at base; r41 suite
`closed=8/12 exit=1`, `selftest cases=12 failures=8`) and `c2-controls/before.txt` reach none of the after
values — every delta atom (24→25, 63→66, 60→61, 27→28, 55→56, 60→61) needs the round's work; the 1.000
measure is a no-harm guard, not an expansion gate.

## Sources & frontier

Census command, run at round start and at round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

- **before** (`.ufo/waves/round-42/census-before.txt`):
  `kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes` /
  `kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes` /
  `kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md` / **exit=0**.
- **after**: identical two `W04` warnings, `kasegi ok …/corpus/SOURCES.md`, **exit 0** (registry 67 lines, no
  new W/E code).

`SOURCES.md` rows **63 → 66**: one tier-1 row added and opened this round (**S064**, status `mined`) plus
**two screened rejections** (**S065** OSV schema, **S066** NVD API 2.0 schema, `rejected` with reason and
flip), closing D-r41-2. Rows touched old→new: S064 absent→`mined` (capture
`corpus/source-snapshots/round-42/S064.txt`, manifest record passing `capture-binding-check.py`); S065/S066
absent→`rejected`. No existing row cell changed. **Frontier advanced: F24→F25** (`corpus/README.md`), F25 =
CVE Record Format (`corpus/knowledge/cve-json-record-format.md`, ids S064), with the PROVINCE r42 amendment.
F24 (RFC 9116) stays parked on the open round-41 L0 scope question. `Assimilation: none` — the
`merge/kasegi/` package was audited (`.ufo/waves/round-42/wave1/ExecAssimilation.md`) and no theme fitted the
round's claims; `considerthese/` yielded no still-unimplemented proposal the claims could carry.

## Trend verdicts

- **expansion — improved.** F25 (24→25) adds a machine-readable vulnerability-record standard the lane did
  not hold; the registry gains the mined row with its capture (63→66). Measured, and unreachable by a
  do-nothing control.
- **quality — improved.** The C1 instrument moved from `closed=10/13`, `selftest failures=3` with a replay
  limb mutating text its check does not read, to `closed=13/13` with thirteen graded selftest cases at Y;
  the four defects it carried are recorded as mined mistakes with demonstrated failing cases, and the red
  pre-repair transcript is preserved rather than overwritten.
- **discernment — improved.** The round read the three inherited attempts, kept what verified, named and
  repaired what did not, and kept predicate and implementation in separate records (errata 4) instead of
  re-running the whole round or moving a target.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: the
  `r42-closure.sh` row sits in one contiguous, well-formed Gates-and-probes block and the D-r41-3
  split/duplicate rows are repaired; J3 `tables=18,rows=73,r42-rows=1,r40-rows=1,r40-split=0,bare=0,lead=0`;
  `density.py SKILL.md` mean 234.2 over 30 blocks (1134 lines, 782 path-citation instances);
  `anchorcheck.py` 16 in-range cite instances, 0 bad. No non-author check.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — evidence: no end-to-end hunt ran
  this round; the executed work is measurement and corpus curation (F25 lead screen, S064 capture with
  `source-recheck` and harness admission, the C1 suite run). Pointer `LOG.md:1754-1812`.
- `[~]` Instructions executable by an agent without oral context — evidence: every counter runs from
  committed bytes; base `closed=5/13 exit=1`, r41 head `closed=4/13 exit=1`, Y `closed=13/13 exit=0`,
  selftest `cases=13 failures=0`, plain run exit 2, ref-not-found red distinct; C2 counters green.
  Pointer: `.ufo/waves/round-42/final-gates/all-gates.txt` and the Y verification transcript quoted above.
  No non-author check.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — evidence: the only province move is the F25
  amendment for a vulnerability-record standard beside F18/F19/F20/F21/F23; the lead screen's no-overlap
  check and sibling scan are recorded in `.ufo/waves/round-42/wave1/ScoutC2Screen.md`; F24 stays parked on
  the open L0 question.

## Extras

- **Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no pacman transactions; no new binaries required).
- **L0 questions:** none newly filed; the open round-41 RFC 9116 scope question stays open and F24 parked.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` run state,
  another lane's `round-54/tameshi.md`, and three unrelated untracked files (`o.bin`, `oldrep1.out`,
  `oldrep2.out`) whose contents name no lane; no seat of this lane wrote into the fleet root.
- **Dead seats:** wave 1 — 0 of 64. Wave 2 — none spawned (see the round shape).
- **Wave-2 reservation:** the frozen C1 kill rule's wave-2 clause (“including any wave-2 attack receipt”)
  has no attack receipt this round because the dispatcher did not take the handoff; the falsification credit
  that ran is the thirteen graded selftest mutants and the seven replay limbs at Y, plus wave 1's 32.8 %
  attack share.
