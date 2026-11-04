# mori round 89 — report (L1 MoriR89, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/mori-shokunin` (mori — fleet & host observability;
detection and report only). Entering revision `30a29797012281b9fd0c748b38b929ac67f8c754`;
final lane tip `ab48dbec724e5ee55e85df9f1d690fcf5fceff65` (pushed; `git ls-remote origin
refs/heads/master` prints it). Measured revision for both after-values:
`7715bb56dce6b75ce281ef1a78be4eeb34a9e245` (no instrument byte changed between it and the tip:
`git diff --stat 7715bb56 ab48dbec -- .ufo/waves/round-89/count-c1.py
.ufo/waves/round-89/count-c2.py .ufo/waves/round-87/count-c2.py .ufo/waves/round-88
.ufo/waves/round-89/noharm-c1.py .ufo/waves/round-89/heldout-c1.py` is empty).

Round 88 was closed `rejected-harmed` (`corpus/lessons/round-88-verifier-spotcheck.md`). This
round declares **two claims on distinct axes**, both carrying that closure's routed defects:

- **C1 — operability.** The r87 receipt gate (`.ufo/waves/round-87/count-c2.py`) binds the
  **executed script**: path identity by `normpath`/repo-relative `realpath`, and the entering
  token rule minus the positions that provably do not execute the bound path (POSIX comment,
  redirection target, `echo`/`printf`/`:` operand, CPython `-W`/`-X` value, after `-c`/`-m`,
  after the script operand); quoted command strings are searched recursively. Frozen predicate
  P-C1: `C1=met equiv=accepted comment=refused selfprint=refused real=met arms=26`, rc 0.
- **C2 — calibration.** The twelve r88 mutation survivors are armed and each kill is
  **attributed to its declared arm** (`killed ⟺ (rc≠0 ∨ fail>0) ∧ FAIL <declared arm>`; an
  unlabelled red run is `unattributed`, never killed). Frozen predicate P-C2:
  `C2=met mutants=12 killed=12 survivors=0 unattributed=0 unanchored=0 arms=28,26`, rc 0.

Contract `.ufo/waves/round-89/contract.md`, frozen at `d4438695` before any after-value, with
do-nothing and skip-work controls committed first (`evidence/controls-r89.txt`).

## Work performed

**C1 (operability) — the executed-script binding, landed through a disclosed repair sequence.**

- Frozen instruments and controls: `count-c1.py`, `count-c2.py`, `controls-r89.sh`,
  `evidence/controls-r89.txt` — commit `d4438695`. The do-nothing control at entering reads
  `C1=unmet equiv=refused comment=accepted selfprint=accepted real=met arms=23` rc 1 and
  `C2=unmet mutants=7 killed=0 survivors=7 unattributed=0 unanchored=5 arms=25,17` rc 1.
- First landing `760428ab` (path identity + script position, gate selftest 23 → 26 arms, the r88
  caller pin `SUBJECT_ARMS`/`TARGET` migrated, registry row 23 appended to `SKILL.md`). The
  frozen predicate read met, but the wave's reviewer `Mo89R01C1` measured **13 valid equivalents
  newly refused** and six counterfeits still bound (`w1/Mo89R01C1.md:51-100`);
  `noharm-c1.py` read `harm=13 open=6` rc 1 (`evidence/noharm-760428ab.txt`).
- Repair 1 `9f4d20b9` (invocation-aware parser: quote-aware `;`/`&&`/`||`/`|` split, POSIX
  comment rule, wrapper unwrapping, `-W`/`-X` values, `sh -c` recursion, `uv run`) took the
  34-case battery to `harm=0 open=0 gained=3` rc 0.
- The residual seats then showed repair 1 was tuned to that battery: the reviewer
  `Mo89R03Repair` built 59 new cases (every expectation proved by a witness run) and measured
  `harm=11`; the critic `Mo89C02Critic` graded three non-executing-branch counterfeits `met`
  end-to-end; the mutation-tester `Mo89M02Mut` measured 29 of 41 binding mutants surviving both
  detectors (`r/Mo89R03Repair.md` §2, `r/Mo89C02Critic.md` §(b), `r/Mo89M02Mut.md`).
- Repair 2 `7715bb56` is **subtract-only** (entering rule minus provably non-executing
  positions), with `heldout-c1.py` (78 cases from the two residual seats) landed beside it.
  `heldout-c1.py`: entering `harm=0 newopen=0 open=36 gained=0`; `760428ab` `harm=24 newopen=1
  open=9`; `9f4d20b9` `harm=12 newopen=1 open=25`; landed `7715bb56` `harm=0 newopen=0 open=30
  gained=2` (`evidence/heldout-revs.txt`). `noharm-c1.py` at the same revision:
  `harm=0 open=0 gained=3` (`evidence/after-r89-final.txt`).
- The knowledge entry, criterion and lesson were corrected for repair 2 at integration
  (`corpus/knowledge/execution-binding-r89.md` “Round-89 repair 2”,
  `corpus/QUALITY.md` 186–189, `corpus/lessons/round-89.md` `## Mistakes (repair 2)`), commit
  `ab48dbec`.

**C2 (calibration) — twelve attributed arms.**

- Seats `Mo89E01ArmsC1` (three arms in `.ufo/waves/round-88/count-c1.py`: `arms_last_tally`,
  `green_mixed_fail`, `own_ok_red`) and `Mo89E02ArmsC2` (nine arms in `count-c2.py`:
  `target_full`, `met_line_derived`, `clean_wrong_split`, `receipt_name_bound`,
  `clone_top_bound`, `own_ok_red`, `verdict_last_wins`, `absent_without_supersedes`,
  `vacuous_body_fabricated`), with `own_ok_of`/`met_line`/`clone_root_ok` extracted, the dead
  `want_met` deleted and the `FX … ok` wording — landed `7ce712d4` from the seats' candidates
  (`w1/candidates/`, diffs in `w1/Mo89E02ArmsC2-r88-c2.diff`).
- Independent per-mutant measurements: `w1/Mo89E01ArmsC1-mutants-transcript.txt`,
  `w1/Mo89E02ArmsC2.md`, and `r/Mo89M02Mut.md` (subject B, one mutation at a time, restore
  verified by sha256).

**Routed defects from the r88 spot-check (all five addressed).**

1. Newness overstatement → append-only corrections in
   `corpus/knowledge/receipt-counterfeit-r88.md` and `corpus/README.md` (commit `c89e5b6e`), plus
   a lesson row (`newness-counted-by-helper-not-by-refusal`).
2. Genuine `./path` refusal and the comment/self-print evasions → C1, with the equivalence
   battery as a standing floor (`noharm-c1.py`, `heldout-c1.py`).
3. Kill attribution and the checksum canary → C2's frozen kill rule plus the counter's
   `canary_unattributed` arm; the critic's canary still reaches the target line and is disclosed
   below, not waived.
4. The twelve survivors, label-substring arms, the misleading `FX clean … refused` and the dead
   assignment → C2; the r89 C1 counter's own `FX … accepted|refused` polarity is disclosed and
   carried (frozen instrument).
5. Post-data detector drift (r88 E4) and the F3 host-path replay → kept visible; F3 carried as
   round-90 planned work.

**Frontier step.** Four sources admitted and one rejected, one knowledge entry, one mistake per
row in the lesson, one `considerthese` proposal landed (suggestion 2, carry-over ledger).

**Wave.** One v1 wave of **12 seats** (`w1-spec.json`/`w1-dispatch.json`, validator rc 0, band
8–16): executors 3, scribes 2, reviewers 2, scout, critic, mutation-tester, connector, sentinel
(attack share 4/12) — plus a **4-seat residual** call (`r-dispatch.json`: reviewer, critic,
mutation-tester, scribe) after three w1 attack seats died on `402 Insufficient account funds`
(`Mo89C01Critic`, `Mo89M01Mut`, `Mo89Se01Boundary`). Round total **16 seats**. The L1 holds the
canonical planner seat (planner is not a swarm role). Both result handoffs lost per-seat final
text to an orchestrator kernel restart; the seat reports are the evidence, and the handoffs are
committed as `w1-results.json` / `r-results.json`.

## Landed changes

| Commit | Content | LOG entry |
|---|---|---|
| `d4438695` | frozen contract, both counters, controls script and controls receipt | Round 89 — freeze |
| `760428ab` | C1 first landing: r87 gate binding, 26 arms, r88 caller pin, SKILL registry row 23 | Round 89 — C1 |
| `7ce712d4` | C2: twelve attributed arms, helper extraction, dead assignment, FX wording | Round 89 — C2 |
| `9f4d20b9` | C1 repair 1 (invocation-aware parser) | Round 89 — repair sequence |
| `c89e5b6e` | knowledge `execution-binding-r89.md`, S607–S611, QUALITY 186–188, lesson, r88 corrections of record, SKILL limits, first after receipt and no-harm receipt | Round 89 — corpus |
| `bb50c332` | w1 wave evidence (spec, dispatch, results, nine seat reports, candidates) | Round 89 — wave |
| `fbd3091e` | residual attack evidence (four seat reports + evidence, `r-results.json`) | Round 89 — residual |
| `7715bb56` | C1 repair 2 (subtract-only rule) and `heldout-c1.py` | Round 89 — repair 2 |
| `ab48dbec` | repair-2 errata (knowledge, lesson, QUALITY 189), SCORECARD round-89 section and round-90 plan, LOG entry, final receipts, end census | Round 89 — record |

`LOG.md` carries one appended `## Round 89 — 2026-11-04 (L1 MoriR89, attempt 1)` entry naming
each claim, the repair sequence, the receipts, the wave, the disclosed attack findings and the
verdicts; `SCORECARD.md` carries the round-89 section with the before→after table, the
demonstrated-instrument row and `## Planned (round 90)`.

## Before → after measurements

| Claim | Axis | Counting command | Before (entering `30a29797`) | After (measured at `7715bb56`) |
|---|---|---|---|---|
| C1 | operability | `python3 -I .ufo/waves/round-89/count-c1.py <rev>` | `C1=unmet equiv=refused comment=accepted selfprint=accepted real=met arms=23` rc 1 | `C1=met equiv=accepted comment=refused selfprint=refused real=met arms=26` rc 0 |
| C1 no-harm floor (disclosed, not the predicate) | operability | `python3 -I .ufo/waves/round-89/noharm-c1.py <rev>`; `python3 -I .ufo/waves/round-89/heldout-c1.py <rev>` | `NOHARM harm=0 open=11 gained=0 cases=34`; `HELDOUT harm=0 newopen=0 open=36 gained=0 cases=78` | `NOHARM harm=0 open=0 gained=3`; `HELDOUT harm=0 newopen=0 open=30 gained=2` |
| C2 | calibration | `python3 -I .ufo/waves/round-89/count-c2.py <rev>` | `C2=unmet mutants=7 killed=0 survivors=7 unattributed=0 unanchored=5 arms=25,17` rc 1 | `C2=met mutants=12 killed=12 survivors=0 unattributed=0 unanchored=0 arms=28,26` rc 0 |

Receipt: `.ufo/waves/round-89/evidence/after-r89-final.txt` (`# replay: clone`, four instruments,
`# rev: 7715bb56`). The earlier `evidence/after-r89.txt` binds the superseded repair-1 revision
`9f4d20b9` and stays byte-unchanged. Instrument selftests at the tip
(`evidence/selftests-r89.txt`): r87 gate 26/0, r88 c1 28/0, r88 c2 26/0, r89 c1 15/0, r89 c2
17/0, all rc 0.

**Disclosed, not waived.** (a) 30 of the 78 held-out counterfeits are still bound — the
provenance classes a syntax rule cannot decide (non-executing branches, function shadowing,
`PATH`/`python3` substitution, `sitecustomize`, blob overwrite, heredoc data, `uv run -m`,
`bash -n`); a binding is a statement about the recorded command text, and the receipt's replay is
the only execution evidence. (b) The frozen r89 C1 counter cannot tell the rule from a lookup of
its own six strings (critic `forge-a1`/`forge-b` reach its target); the floor is the paired
`noharm-c1`/`heldout-c1` batteries, not `count-c1` alone. (c) C2's counter cannot tell a real arm
from a canary that reds every arm on any edit (`forge-c1`, `forge-c2b` reach the target line); the
claim is verified on the committed subject bytes by the landed diff plus three independent
per-mutant measurements. (d) The skip-work control's `count-c1.py` leg was confounded by arms
appended after its own `own_arms_pinned` (`w1/Mo89R02C2.md` §4 F1); the control is frozen and
only its `count-c2.py` leg is cited. (e) The repair sequence ran after the first after-value;
each revision is receipted and named, and no frozen predicate, counter, population or kill rule
moved.

## Sources & frontier

Census (the frozen command in `CORPUS.md` §SOURCES.md; receipts
`evidence/census-start.txt`, `evidence/census-end.txt`):

```
scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori   # start rc 0, end rc 0
scripts/sources-census.sh census   --root /home/vgpnk/Projects/shokunin mori
```

| Census | Before (round start) | After (round end) |
|---|---:|---:|
| rows | 379 | 384 |
| tier A / B / C | 340 / 19 / 20 | 344 / 19 / 21 |
| status mined / queued / rejected | 322 / 24 / 33 | 326 / 24 / 34 |

Rows added: **S607** (Python 3.14 `shlex` — tokenizer scope), **S609** (Python 3.14
`os.path.normpath`), **S610** (Python 3.14 command line — which argument CPython executes),
**S611** (POSIX.1-2024 §2.3 token recognition — the comment rule), all tier A; **S608** rejected
(tier C) — `shlex` as proof of shell execution. Rows touched old→new: **none** (no `status`,
`recheck` or `used-by` cell of an existing row changed; the lesson's `## Gate` records every new
row's URL, 2026-11-04 access date and ≤25-word located quote). Sourced claim: C1's rule rests on
S611 (comment rule) and S610 (`-c`/`-m` data), cited by
`corpus/knowledge/execution-binding-r89.md`. Frontier rows advanced: **none closed** — the round
works the lane's own gate integrity; FR9 (durable fixture evidence) is exercised by the two
batteries and their receipts but not closed, and the provenance classes in (a) above are the
frontier ground the syntax rule cannot reach. Assimilation: none (no `merge/mori/` theme taken).
`considerthese/2026-10-26.md` suggestion 2 (follow unfixed flags forward) landed as the
carry-over ledger in `corpus/lessons/round-89.md`.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`execution-binding-r89.md`: what a recorded `# cmd:` executes, what each source licenses, and
  the measured limits), sourced by four newly admitted rows, plus a demonstrated instrument row
  (the paired no-harm/held-out floor) in `SCORECARD.md`.
- **quality — improved.** Two false claims were corrected append-only (r88's “three new
  conditions”; repair 1's “executes” framing), four QUALITY criteria were added from measured
  failures (186–189), and the landed rule reads `harm=0 newopen=0` on 78 cases it did not author
  where the entering rule read `open=36` and repair 1 read `harm=12`.
- **discernment — improved.** The r88 outside spot-check's routed defects are discharged or
  explicitly carried; its disagreement became a named correction and a criterion, and the
  round's own residual attack seats (not the author) changed the landing twice — the second time
  against a battery the author did not write. No fresh non-author spot-check of this round exists
  yet; the closure supplies it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry row 23 (r89 counters, verdict map, pins, limits paragraph) and the r89 limits note; no named non-author verifier for this round yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 89` (both claims, the repair sequence, the receipts); the task is the gate repair measured through the gate's own public path (`count-c1.py` → `grade_population` → real seven-receipt population).
- [~] Instructions executable by an agent without oral context — `python3 -I .ufo/waves/round-89/count-c1.py <rev>`, `count-c2.py <rev>`, `noharm-c1.py <rev>`, `heldout-c1.py <rev>`, each with its own usage line and `--scratch`; selftests 15/17/—/— and the gate 26 (`evidence/selftests-r89.txt`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the work is the lane's own receipt-gate accounting; `PROVINCE.md` untouched; the held-out counterfeits are reported as limits, and no host, credential or orchestration surface was read or claimed.

## Extras

- **Stale-lane:** respawn-per-round driver; this round's mission ran under `hyaku-inline`
  (launch `2026-11-04T17:53:21-03:00`); no other mori mission is open. The mission exceeded two
  driver ticks and is **progressing** (lane-authored commits `760428ab`…`ab48dbec`).
- **Dead seats:** `Mo89C01Critic`, `Mo89M01Mut`, `Mo89Se01Boundary` — `402 Insufficient account
  funds` (opencode-go), no report; replaced by a residual call under new names, never re-spawned
  under the old ones.
- **Inherited state:** the previous attempt of this same round left no uncommitted lane work at
  start; the residual wave's `r-results.json`, `r/` and three receipts were inherited uncommitted
  and are committed byte-exact at `fbd3091e`/`ab48dbec`.
- **Tool installs:** none by the L1. Seat `Mo89R04Corpus` downloaded BusyBox 1.35.0 x86_64-musl
  from `busybox.net/downloads/binaries/` into scratch only (sha256 `6e123e7f…311348`; no checksum
  file published beside it), used once for a shell-comparison probe and deleted with its scratch
  tree — recorded here per the tooling directive.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no
  mori-round-89 seat file at the fleet root; nothing to move.
- **Open L0 questions:** none added this round; the mori r65/r73 instrument ruling and the r61
  assimilation questions remain open and untouched.

## Erratum (appended after the filed bytes; supersedes two statements above)

1. **Final lane tip.** The header's “final lane tip `ab48dbec724e5ee55e85df9f1d690fcf5fceff65`”
   is superseded: the lane tip is `192c7e0bdae6cbf84052d30a87862ccadf6ffe09`
   (`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` reads
   `ahead=0 behind=0`). `192c7e0b` appends three corrections of record and touches no instrument
   byte: `SKILL.md` gains the repair-2 limits paragraph superseding the two round-89 paragraphs
   that described repair 1; `corpus/README.md` gains the Round-89 frontier correction naming the
   subtract-only rule and the held-out numbers; `corpus/lessons/round-89.md` gains the D2 ledger
   correction (`9f4d20b9` → repair 2 `7715bb56`), the S608 flip-text correction (`shlex` is a
   tokenizer, not an execution model; the immutable cell stays, the correction lives in the
   lesson) and the docs.python.org digest-drift note. Both after-values and every receipt are
   unchanged, and `git diff --stat 7715bb56 192c7e0b -- <the six instrument paths>` is empty.
2. **A second L1 ran this round.** `MoriR89-2` was spawned with the same ready-file label and
   authored repair 1, repair 2, `noharm-c1.py`/`heldout-c1.py`, the residual `r` wave and the
   corpus commits that this report integrates; it stopped when it saw this report and the lane
   tip, and reverted its remaining uncommitted edits (lane tree clean, `tracked=0 untracked=0`).
   Its stale-at-`ab48dbec` list is what `192c7e0b` corrects. Two L1s on one lane-round is an
   orchestration defect for the closure to record, not a lane claim; no work of its is left
   unlanded and no seat was re-spawned under a dead name.
