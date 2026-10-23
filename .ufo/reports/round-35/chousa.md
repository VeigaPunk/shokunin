# chousa — round 35 report

Lane: chousa (deep-research method). Round 35, attempt 1. Lane repo
`/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`.
Base `08be4c9e3a4ebe55d915ce4761c81854286c23ae` (gate `a6307edf…2995b`).
Landed lane tip **`b6f2c0db8de4047e6518f4232da2fd3c3954cf00`** (pushed; `ahead=0`, no untracked lane files).

## Work performed

Two claims, distinct axes, each with a counter, a frozen predicate and a kill rule declared in
`corpus/evidence/round35/claims.md` (`0e167649`) before any after-data; the post-data §Erratum is
append-only.

1. **C1 — operability** (lowest scored axis, 3/10): `research-gate.sh` resolves, verifies and pins
   ONE absolute grep binary at startup and refuses an unverifiable pin with a named exit-2 refusal,
   instead of resolving bare `grep` through `PATH` at each matcher call.
2. **C2 — calibration**: the lane's receipts can separate an output-equivalent keyed engine from the
   landed dead-zone routing (a mechanism/routing witness), where output counters cannot.

Work items (each with its evidence pointer):

- **Freeze** (`0e167649`): design v1 with P1/P2, kill rules, the two limits stated before data, two
  counters (`c1-count.py`, `c2-count.py`), the witness tool (`tools/mechanism-witness.py`), and five
  pre-data control receipts in `.ufo/waves/round-35/controls/`.
- **C1 before-state measured**: `GREP_PIN_MATCH=0/9` on the base gate
  (`controls/c1-base-s3501.json`), with the PATH-shim and `BASH_ENV`-function tripwires firing
  (852 / 867 bytes) at *identical output* — the substitution is invisible in output — and the
  no-grep-`PATH` run exiting 2 (`S3`).
- **C1 cheapest control**: a hardcoded `/usr/bin/grep` wrapper without provenance, override or echo
  scores 3/9 (`controls/c1-hardcoded-s3501.json`), so the counter is not met by the obvious fix.
- **C2 before-state**: `WITNESS_SEPARATED=0/2 battery=absent`
  (`controls/c2-before-s3501.json`); the base tree holds no witness tool.
- **C2 cheapest controls**: an always-pass witness separates 0/2; an always-fail witness fails the
  landed gate (`controls/c2-stub-pass-s3501.json`, `controls/c2-stub-fail-s3501.json`).
- **Landing** (`e87c5d7e`, gate `1f2fb4f5…c617`): `grep_pin_init` + direct-path `grep()` wrapper,
  refusal `research-gate: GREP_PROVENANCE refused: <reason> (candidate=<path>)` before any record
  read, `RESEARCH_GATE_GREP` override (absolute, GNU-reporting), opt-in
  `CHOUSA_GREP_PIN_ECHO=1` → `GATE_GREP: path=… source=default|override version="…"`; R1 `slen`
  reads its own parameter; R2 case-range comments 252-253 / 254-256.
- **Wave-reported vectors fixed on the final bytes** (gate
  `a47688518e509edbf43b433a5e16e1cf2481233f3acedb5824ba341f7f0c38ad`, committed `770a69d6`): the
  wrapper no longer dispatches through the `command` keyword (a `BASH_ENV` `command()` function
  received every pinned call in three seats' probes); the `--version` probe cuts its line in bash
  instead of `head` (a forged `head` pinned a non-GNU stub in two seats' probes) and is bounded by
  an absolute `timeout(1)`; the dead `command -v grep` fallback is gone (it resolved the gate's own
  `grep()`; four seats confirmed); `readonly -f grep` / `readonly GREP_BIN` now refuse with the named
  error instead of aborting as a bare rc 1.
- **Measured after, on the final bytes**: C1 `GREP_PIN_MATCH=9/9` on seeds 3529 and 3539
  (`final/c1-s{3529,3539}.json`); C2 `WITNESS_SEPARATED=2/2 OUTPUT_EQUIV=2/2 LANDED_WITNESS=pass` on
  the same seeds (`final/c2-s{3529,3539}.json`); selftest `PASS (256 cases, 0 skipped)`; R1 probe
  `offsets=1 first=5`.
- **Frontier step**: S067 (exec(3), PATH search) and S068 (bash(1), `BASH_ENV`) opened from the
  installed man pages this round and filed with located quotes (lesson `## Gate`); three knowledge
  entries; QUALITY 45–49; the mined mistake is the `local a=$1 b=${#a}` dynamic-scope read that
  shipped in round 34 with a probe that fails on the old bytes.
- **Repairs**: R1 probe `repairs/slen-probe.sh` (base `offsets=0` / landed `offsets=1`); R2 all 14
  gate case-number comments verified against a selftest run (wave seat RevCaseRanges); R3 round-34
  wave debris reconciled — 26 tracked `w2a2/*.md`, the three `ExecC2Oracle` texts tracked since
  `6a3cc32`, the "3 untracked" note was already false in the commit that recorded it (wave seat
  ScoutDebris); R4 runbook rows + metadata headers (all three entries now pass the metadata screen's
  required fields).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| frozen design v1 + counters + witness tool + pre-data controls | LOG.md §Round 35 (opening) | `0e167649` |
| wave spec, validated plan/taskCall, registry, generator | LOG.md §Round 35 | `2b2e0171` |
| gate: grep pin (landed form) + R1 `slen` + R2 case ranges; C1/C2 after receipts, R1 probe | LOG.md §Round 35 | `e87c5d7e` |
| three knowledge entries, QUALITY 45–49, S067/S068, README front/rows, SKILL rows + section, SCORECARD, lesson, wave evidence | LOG.md §Round 35 | `beb04ea1` |
| erratum 7, witness trace-size/survivor corrections, late wave seat evidence | LOG.md §Round 35 | `770a69d6` |
| erratum 8 (late survivors) | LOG.md §Round 35 | `7d21a333` |
| late wave seat evidence, `tools/__pycache__` ignored, `MutCounterC1` | LOG.md §Round 35 | `234c95d4`, `b6f2c0db` (tip) |
| this report | — | fleet repo, `fleet-commit.sh`; lane tip at landing `b6f2c0db` |

## Before → after measurements

| Claim | Counting command (lane root) | Before | After | Commit measured |
|---|---|---|---|---|
| C1 | `python3 corpus/evidence/round35/c1-count.py --gate tools/research-gate.sh --seed N --receipt F` | `GREP_PIN_MATCH=0/9` (gate `a6307edf`, `controls/c1-base-s3501.json`) | `9/9` on seeds 3529 and 3539 (`final/c1-s3529.json`, `final/c1-s3539.json`) | `770a69d6` (gate `a4768851…`) |
| C2 | `python3 corpus/evidence/round35/c2-count.py --seed N --receipt F` | `WITNESS_SEPARATED=0/2 battery=absent` (`controls/c2-before-s3501.json`) | `WITNESS_SEPARATED=2/2 OUTPUT_EQUIV=2/2 LANDED_WITNESS=pass` on seeds 3529 and 3539 (`final/c2-s3529.json`, `final/c2-s3539.json`) | `770a69d6` |
| R1 (repair) | `bash .ufo/waves/round-35/repairs/slen-probe.sh tools/research-gate.sh` | base gate `offsets=0`, exit 1 | landed `offsets=1 first=5`, exit 0 | `770a69d6` |
| R2 (repair) | `bash tools/research-gate.sh --selftest` labels | round-34 comments said `252-254` / `255-257` | `252-253` / `254-256`, confirmed by the run's own `ok-case` names (case 255 `claims-deadzone-line`, 256 `claims-deadzone-edge`); all 14 case-number comments correct | `770a69d6` |
| R3 (repair) | `git ls-files .ufo/waves/round-34/w2a2/*.md \| wc -l` | report said "23 of 33"; spot-check said 3 untracked | 26 tracked; `ExecC2Oracle/{boundary-diff,diff-fuzz,pcre-boundary}.txt` tracked since `6a3cc32` | `770a69d6` |

Verdicts and the narrowing (all named in SCORECARD and claims.md §Erratum):

- **C1: met under P1; reading narrowed.** The counter proves path + version resolution, refusal
  shape and output equality. It does **not** measure per-call engine identity: a gate that opens the
  record then refuses (`147ded03…`), correct-output engines replacing `tok_span_offsets_direct`
  (`fd6d5a8e…` bash-glob, `9040dcba…` awk), a `BASH_ENV` `command()` swap, and an S1/S2 attack that
  knows the tripwire path (`3a7cbefc…`, `51ffec6a…`) all score 9/9 (wave seats MutPinRefusals,
  MutGrepPinEngines, MutGrepShimEnv, RevScenarioS1S2, CritGrepProvenance, CritClaimSizing,
  ExecPinModeVerify — six independent confirmations). The read-ordering claim therefore rests on the
  wave's strace evidence (0 opens of the claims fixture under every refusal vs 2 in both positive
  controls), not on the counter. Paired invocation overhead of the pin: +1.59 ms (CritGrepClaimScope).
  Two further survivors arrived after the landing and are in claims.md §Erratum 8: a one-line mutant
  that validates the override and then assigns `GREP_BIN=/usr/bin/grep` scores 9/9 while misreporting
  `source=override` (S7/S9 override with the same path as the default pin), and `--pin`'s capture
  body inherits `CHOUSA_GREP_PIN_ECHO=1`, so a baseline pinned with the echo on makes `--drift`
  report `GATE_DRIFT: -LINE` against an unchanged gate (ExecPinModePinDrift). A further survivor
  (ExecC1Control): the counter reads the `GATE_GREP:` echo as a **string**, so a gate that prints a
  hardcoded version literal with zero `--version` calls, or that validates an override and then
  swaps `GREP_BIN` to a byte copy after the echo, scores 9/9 while the substitute serves the matches —
  and `S6`'s stub prints its banner to stderr, which the gate discards, so the non-GNU branch is
  never exercised. Verified against the final gate.
- **C2: met under P2 as a ROUTING witness.** It proves the routed matcher function was entered, not
  that its body ran: a one-record shortcut (8 stamps for 8 records — the landed gate itself emits 9),
  a length-keyed engine (6/31 scanned seeds), a real chunk call with a discarded result, a
  body-replaced matcher (`3e5648b8…`), a column-0 decoy definition and static marker forgery all pass
  (wave seats MutC2KeyedBattery, MutWitnessBypass1/2, MutWitnessThreshold, RevWitnessCode). The axis
  caveat is recorded (CritC2AxisFit): P2 measures receipt strength, not the lane's self-assessment
  accuracy.
- **R1's probe is a demonstration, not a counter** (ExecSlenProbe): a hardcoded `slen=32766` or a
  deleted confirmation line also prints `offsets=1`. The defect itself was fail-closed — only the
  length mattered, and a wrong `slen` loses matches, never invents offsets. r36: a real R1 counter.

## Sources & frontier

Census (frozen command, exit codes as run):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
round start:  chousa W04 S051 duplicate url … ; chousa W04 S053 duplicate url … ; chousa ok …  exit 0  (66 rows)
round end:    same two W04 lines + chousa ok …                                                exit 0  (68 rows)
```

Rows **66 → 68**; both new rows tier A, mined, both opened this round from installed man pages:

- S067 exec(3) — quoted at decompressed `/usr/share/man/man3/exec.3.gz:107-110` ("The file is sought
  in the colon-separated list of directory pathnames specified in the PATH environment variable.",
  17 words, accessed 2026-10-23, file SHA-256 `2f1badd3…b1523`, man-pages 6.19-1). `execvp.3.gz` is
  a `.so man3/exec.3` stub. The page does **not** state component order — the row says so and the
  order claim rests on the S1 measurement.
- S068 bash(1) — quoted at decompressed `/usr/share/man/man1/bash.1.gz:391-395` ("When bash is
  started non-interactively, to run a shell script, for example, it looks for the variable BASH_ENV
  in the environment", 21 words, bash 5.3.20, file SHA-256 `b68beb3e…bdffe`). Narrowed after wave
  seat ExecCensus found the exported-function clause unanchored; the row now cites `BASH_ENV` only.

Rows touched old→new: S067, S068 new; no existing row's status/recheck/used-by changed this round.
Used-by: `corpus/knowledge/grep-pin-r35.md` (both). Frontier rows advanced: **none** — the round's
surfaces come from the round-34 lesson and the spot-check, not from `corpus/README.md` §Frontier
(wave seat ScoutFrontier); one stale frontier sentence (the "about 28000–32767" dead-zone claim) was
corrected in `corpus/README.md` and the knowledge table gained the three r35 entries.

## Trend verdicts

- **expansion — improved.** A new measured surface (tool provenance at 68 grep call sites) and a new
  instrument (output-vs-routing witness) with the release of a survivor table; three knowledge
  entries on ground the corpus did not cover; two source rows. It closes no README frontier row,
  which is stated rather than implied.
- **quality — improved.** A real contract hole (PATH-resolved matcher) closed and hardened against
  five of the six vectors the wave reported; the latent `slen` defect repaired with a
  before/after demonstration; all 14 case-range comments now match a selftest run; S067/S068 paged
  with located quotes; the no-harm observables hold (selftest 256 with the dead-zone cases 254–256,
  prior counters exercised in the wave).
- **discernment — improved.** The round falsified its own instruments before the closure could: six
  independent seats reproduced the engine-swap class on C1 and four on C2, the tripwire path was
  shown predictable, the witness's parser and marker shown forgeable, and C1's `--seed` shown
  decorative. Every one is recorded as a narrowing in the SCORECARD row and claims.md §Erratum — not
  argued away — and the capability rows are scoped to what the receipts prove ("path + version", not
  engine identity; "routing", not computation). One dead seat by provider refusal.

## Round shape and wave

- **One v2 wave, 65 spawn seats** (0 resume) under
  `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128, `maxLanes` 256), validated by
  `ufo-swarm-wave.mjs run` (schema `ufo-swarm-wave-dispatch-v1`, `counts.spawn=65`); spec
  `.ufo/waves/round-35/w2-spec.json`, plan `.ufo/waves/round-35/w2-plan.json`, taskCall
  `.ufo/waves/round-35/w2-taskcall.json`, registry `.ufo/waves/round-35/w2/swarm-registry.json`
  (`2b2e0171`). Dispatched by the orchestrator as exactly ONE batched task call; no seat dispatched
  from this session.
- **Role mix**: 22 executor, 11 reviewer, 10 mutation-tester, 8 scout, 6 critic, 6 scribe,
  2 connector — attack 27/65 = **41.5 %**. No planner seat anywhere (the L1 holds the §3 planner
  seat; the planning data-walk rode scout/connector items).
- **Returned**: 46 of 65 seat reports are on disk at the landing commit (some seats were still
  writing at the cutoff); the reports that returned cover both claims, the repairs, the sources and
  the round shape. **Dead seats: 1** — `CritWitnessBlind`, provider `cyber_policy` refusal, no
  output, not retried, not rerouted; its slice (witness blind spots) is covered by MutWitnessBypass1/
  2, MutWitnessThreshold, RevWitnessCode and MutC2KeyedBattery.
- **Conformance finding** (CritRoundShape): 28 of 65 item texts name paths lane-relative while the
  shared context binds all 65 to the absolute lane root; seats were told artifacts live under the
  absolute `{WD}` and every report trailer is lane-relative. Recorded as a spec-writing defect for
  round 36 (every item gets an absolute prefix), not hidden.
- Residual call: none.

## Declared behaviour changes and limits

- A pin that cannot be verified now exits 2 **before any record is read**; previously any `grep` on
  `PATH` ran. A host whose GNU grep is not at `/usr/bin/grep` or `/bin/grep` now needs
  `RESEARCH_GATE_GREP` (the old `command -v grep` fallback was dead code — it resolved the gate's own
  wrapper — so such hosts already failed; the message now names the fix).
- Provenance is self-reported: a binary that prints a GNU line and behaves differently is pinned.
  Round 35 adds no integrity pin (SHA-256 of the binary) — named, not claimed.
- The pin's own probe now uses an absolute `timeout(1)` when present (10 s) so a hung override
  cannot block the gate; when `timeout` is absent the probe runs unbounded (documented).
- C1 receipts carry `gate_sha256` but not `counter_sha256` (wave seat ExecC1Fresh1); C2 receipts bind
  the battery and both variant gates. Carried to r36.
- The witness's xtrace file is large (~310 MB per 9-record run, RevWitnessCode) and is written under
  its temp dir and deleted; the runbook row states the size.
- **Known defect in the landed bytes, routed to r36:** `CHOUSA_GREP_PIN_ECHO=1` is inherited by the
  `--pin` capture body (the capture's `env -u` list omits it), so a baseline pinned with the echo on
  embeds a `GATE_GREP:` line and `--drift` against an unchanged gate reports `GATE_DRIFT: -LINE`
  (`.ufo/waves/round-35/w2/ExecPinModePinDrift.md`; claims.md §Erratum 8a). The echo was meant to be
  receipt-only. Not fixed in-round: the fix changes the gate bytes again and the round is at its
  freeze; the defect is named here instead of hidden.

## Stale-lane / extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (no `pacman`, no `uv`/`npx` install by the L1 or by any seat that reported).
- L0 questions: none new. Standing: the fetch-scope question (man7.org unregistered host — S064's URL
  recorded but not fetched) and the rea MCP pin rewrite reported by kaidoku r19 (operator-owned file,
  untouched).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` run before this report;
  no seat-written file was found at the fleet root (the only round-35 writes outside the lane are
  this report and the seat reports under the lane).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — offsets
  `SKILL.md` Gates rows (round-35 counters row, `mechanism-witness` row) and Checklist item 6
  (pinned-binary re-check); no non-author verifier for this round yet.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` §Round 35; counter receipts
  `final/c1-s*.json`, `final/c2-s*.json`; selftest `PASS (256 cases, 0 skipped)`; lane assertion.
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh
  --selftest`; `python3 corpus/evidence/round35/{c1,c2}-count.py --seed N`;
  `python3 tools/mechanism-witness.py --gate tools/research-gate.sh --seed N`; lane assertion.
- [~] No cross-domain bleed (PROVINCE.md unchanged) — `PROVINCE.md` untouched this round; surfaces
  stay inside claim-vs-source verification machinery; lane assertion.
