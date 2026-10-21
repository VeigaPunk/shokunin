# tameshi — round23

## Work performed

**Declared C1 (calibration, tied lowest owned axis): required-command receipt binding.** The frozen unit is ten public-CLI rejection predicates. They move from tool-absent 0/10 to discriminated 10/10. Numeric calibration stays 8 (delta 0). There is no second-axis claim, no promotion and no producer authentication. The contract, ruler and before receipt landed in `15ae6029625dccef2c5e6015ca7b73e027cde70a` before dispatch (`.ufo/evidence/round-23/contract.json`, SCORECARD.md:1027).

Paths below are lane-relative under `tameshi-shokunin/` unless they are fleet paths.

**Authorship.** The round was authored by TameshiR23 up to `336565fc`. TameshiR23 died at 2026-10-21T14:57:01Z. Its last assistant turn, on the `openai-codex/gpt-6.1-sol` fallback, reads: `Codex error event: This content was flagged for possible cybersecurity risk ... (code=cyber_policy)`. The orchestrator reassigned the remainder to **CloseTameshi22**, the non-author closure of r22, under the same held claim (tameshi23, attempt1, base 28cae179). Nothing refused was rephrased or rerouted. This agent is the r23 author of record, so a different agent must close r23.

**TameshiR23 work (verified before reuse):**
- Added `tools/command-binding.py`. It binds a digest-pinned bundle's requirements to receipts by exact name, argv, cwd, revision, typed exit and stdout tokens.
- Added the frozen ruler `.ufo/evidence/round-23/measure.py`, plus 19 supplemental fixtures (`extra-cases.json`).
- Added a ten-anchor guard sweep (`mutations-A.json`, 10/10 killed).
- Ran a 43-command baseline registry replay with full streams (`replay/`, `replay-command-A.json`).
- Ran a source-read substitution: the output-only check accepts it, while the gate rejects it 1/ARGV_MISMATCH. The correct command is clean 0.
- Added source row S083, the knowledge entry `corpus/knowledge/required-command-binding.md`, QUALITY46 and the SKILL.md registry rows.
- Made 15 traced source re-anchors.

I verified these by hash and output before reuse:
- `reader-freeze2.json`: all 10 path digests match the `336565f` blobs.
- `registry-C.json`: 46/46 active, 4 superseded, exit 0.
- `answering-models1.json`: 64/64 rows match the last assistant metadata in the child transcripts.
- `task-call2.json` equals the validator's `taskCall`. Its 64 names equal the dispatched job list and the w2 registry, and no task carries a model parameter.
- The uncommitted `spec2.json` edit is the validated, dispatched version; it is committed as such.

**Wave-2 terminal outcomes (`.ufo/waves/round-23/original-outcomes2.json`).** I collected the task-result callbacks delivered to the author's session (async-result and `wait` results) and made no re-dispatch, resume or replacement.
- 30 seats completed.
- 34 seats are dead. None has a callback; each child transcript ends with `Request was aborted` and no session_exit, when the parent ended. The dead include all 20 reviewers.
- Replay16's partial final text is kept as `w2/Replay16.partial.md`, and the seat stays failed.
- Seat outputs were persisted byte-exact under `w2/*.md`, indexed in `w2-persisted-outputs.json`.
- Deviations from instructions are recorded:
  - Replay40–43 wrote reports despite the no-write rule; their final outputs are kept beside the reports as `*.output.md`.
  - CorpusClaim ran out-of-slice read-only commands.

**Seat accounting with the lane's own r22 gate.** `tools/wave-accounting.py` on `.ufo/evidence/round-23/accounting/{bundle,expected}.json` returns exit 0, `[]`, totals 128/93/35. Replay16 is the only failed-with-report seat (`accounting/receipt.json`).

**Fresh-wave adjudication (`.ufo/waves/round-23/fresh-adjudication.json`).** It supersedes, without editing, the author's unexecuted `fresh-adjudication-draft.json`. Three overclaims were accepted and corrected append-only (lesson `## Fresh falsification wave…` Errata A–D, QUALITY47, a SKILL.md:2033 correction and a knowledge-entry erratum):
- **CorpusClaim/CwdDeclared:** the replay instrument copies receipt argv, cwd and revision from what it executes, so that population tests only exit and stdout. Argv discrimination rests on the source-read pair and the synthetic cases.
- **CwdDeclared/RevisionDeclared/RunnerIsolation:** the replay is not an isolated clone. It is 41 revision-pinned rows plus 2 live-dependent rows (`pin-disposition-read`, `verify-round15`). The clone symlinks live siblings.
- **MistakeRule/TrustedRequirements:** the gate sees only bundle-declared requirements. Requirement freezing is done by replay.py's evidence-local pre-execution check.

A broken Mistakes pointer was also corrected: `route-mix-before.json:34/64` should point to line 3, `zai=34/64`. `route-mix-final.json` line 3 shows `zai=25/64`.

**Eight repairs are routed, not claimed:**
- an argv swap-name case and a name-insensitive mutant
- a negative-exit mutant
- bundle_sha256 pins in the two frozen registry rows
- carrying the runner's held/cleanup/external fields into the replay projection
- hashing the clone's copy of the runner
- realpath for the fleet root
- bounded streams
- preexisting loose stdout tokens

Making these changes would alter `tools/registry.json`, which is an input of 58 ledger entries, or the replay and fixtures after the falsify wave closed. No fresh falsifier is available: the job cap refuses spawns and dead seats are never replaced.

**No-harm maintenance.**
- The corrections drifted the strict monitor to 59/62, restraint 6, at `332dc89` (`monitor-intermediate-D.json`). This is a harmed intermediate and is retained.
- Three actual traced L1-author source reads (`.ufo/evidence/round-23/reanchor-final.py`, `source-traces-final/`, `source-refresh-final-{receipts,entries}.json`) were appended to the unchanged 264-entry ledger prefix, giving 267 entries. The prefix bytes are unchanged (`source-prefix-preservation-final.json`).
- These reads are not blind or independent cold-read, recipe execution or command coverage.

### Dispatch, routing and inherited scope

- **BUILD wave1 (TameshiR23):** one validated 64-seat wave: reviewer19, connector17, critic12, simplifier5, revenger4, executor3, scout2, scribe1, sentinel1.
  - Before dispatch, two refusals were recorded and fixed: a route-concentration refusal (34/64 ZAI), rebalanced to 25/64, and an invalid registry path (`record1-refused.json`).
  - Result: 63 completed, 1 dead. SourceScope (scribe) died on a Haiku 429: `rate_limit_error`.
- **FALSIFY wave2 (TameshiR23 dispatch):** one validated 64-seat wave: reviewer20, connector17, critic12, simplifier4, revenger3, executor3, scout2, mutation-tester1, sentinel1, scribe1.
  - Result: 30 completed, 34 dead (aborted at the parent's death).
  - Before the abort, some seats logged other provider errors: connector 429 `You've reached your weekly usage limit for your plan`, and simplifier 403 `You have run out of credits or need a Grok subscription`.
- **Round total:** 128 unique seats, 93 completed / 35 dead, no replacements. The L1 holds the canonical planner seat. Evidence: `.ufo/waves/round-23/{spec1,spec2,task-call1,task-call2,validation*,record*,dispatch*,assignments*,original-outcomes1,original-outcomes2}.json`.
- **Closure rules for this coordinator:** it dispatched no seat (job cap; Main's no-re-dispatch rule), so no third wave or residual task call was run.
- **Untouched:** no sibling gates, product surfaces, MANIFEST, claims, driver state, routing settings or fleet scripts were edited.
- **Installs:** none by this coordinator. The author recorded one: dulwich 1.2.17 via `uv run --no-project --with dulwich` (uv 0.13.0), ephemeral official package cache. Its stated reason was a Replay30 Git-blob read (`fresh-adjudication-draft.json`). Pacman and host services were untouched.
- **L0:** no new question. The inherited `tameshi | round-18 | R17-INCIDENT routing` remains open.

**Stale-lane:** respawn-per-round driver. No other mission of this lane is open, and no next round was started.

**Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): the only untracked seat file is `.ufo/waves/round-27/build/ScribeLesson.md`. It was written by KagiR26.ScribeLesson-17 (kagi), so it is not this lane's and was left untouched. The other entries are driver-owned `.ufo/state/*`/watchdog runtime.

## Landed changes

Delivered lane tip: **`6a1821a8897eea6e7d9669292160ec9593669409`**. Helper state: local=remote, ahead0/behind0, tracked0/untracked0. Git HEAD is detached, as expected for jj.

| Change | Landed commit | LOG entry |
|---|---|---|
| Frozen C1 declaration, ruler, before receipt, audit wave | `15ae6029625dccef2c5e6015ca7b73e027cde70a` | LOG.md:1544 |
| Gate, fixtures, replay instrument, wave1 evidence | `496d212bc46789cdf8cafab72978bdb7f4182963` | LOG.md:1544 |
| Executed replay, binding falsifiers, S083, knowledge, QUALITY46, registry rows | `8f66b5d992ffcef296d037fe4aad6c057b6422c2` | LOG.md:1544 |
| Fifteen traced source re-anchors, wave2 spec | `336565fc2e70e034307ef267aaa2018572c200d3` | LOG.md:1567 |
| Wave2 outcomes and persisted findings, adjudication, errata, QUALITY47, inherited receipts | `332dc8900a4a8c55953b1726e1d5ca3f04186bd0` | LOG.md:1567, LOG.md:1589 |
| Three traced source re-anchors, intermediate-D monitor | `549ede24aa9b2a6746d3973cf55dc4ceb07a5413` | LOG.md:1589 |
| Final receipts, seat accounting, SCORECARD/LOG verdict | `6a1821a8897eea6e7d9669292160ec9593669409` | LOG.md:1589 |

## Before → after measurements

### C1 calibration — improved; numeric 8→8, delta 0

Counting command, the unchanged frozen instrument run from a private clone of the named revision:

```sh
python3 .ufo/evidence/round-23/measure.py --repo "$CLONE_AT_REV"
```

| Observation | Revision | Result | Receipt |
|---|---|---|---|
| Before | `28cae179e4dc2c1fa7f032a79cdddf0b5d862d76` | tool absent, 0/10, exit 1 (absence of the capability, not ten executed failures) | `.ufo/evidence/round-23/before.json` |
| Final | `549ede24aa9b2a6746d3973cf55dc4ceb07a5413` | 10/10, exit 0. Eight cases exit 1 and two (bool-exit, tampered) exit 2; gate SHA `d533dc1e…` | `.ufo/evidence/round-23/final-verification.json` `claim-final` |

The gate bytes are identical at 496d212, 336565f and 549ede2 (d533dc1e). The ten-anchor guard sweep `mutations-A.json` (10/10, pristine/restored 0) was therefore not re-run. The ten predicates cover nine mechanisms: unknown-command overlaps missing membership.

Same final revision, same receipt file:
- `python3 tools/command-binding.py --selftest` → 38/38, exit 0.
- `--bundle replay/bundle.json --expected replay/expected.json --json` → 0/[].
- Source-read pair → 1/ARGV_MISMATCH; correct command → 0.

The replay verdict tests only exit and stdout (Erratum A), on 41 pinned plus 2 live-dependent rows (Erratum B).

**No-harm**, using commands from the lane root:

```sh
python3 .ufo/evidence/round-21/coldread/measure.py --repo /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev REV --explain
python3 tools/registry-check.py --root /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev REV --json
```

| Point | Revision | Monitor (sections, restraint, depth, overrides) | Registry |
|---|---|---|---|
| Base | 28cae179 | 62/62, 8, 8, false | 43/43 (`registry-baseline.json`) |
| Harmed | 496d212 | 48/62, 6 | — |
| Harmed | 8f66b5d | 47/62 | — |
| Restored | 336565f | 62/62, 8, 8 | 46/46 (`monitor-current-C.json`, `registry-C.json`) |
| Harmed | 332dc89 | 59/62, 6 | — |
| Final | 549ede2 | 62/62, 8, 8, false (strict) | 46/46 active + 4 superseded, exit 0 (`final-verification.json`) |

All harmed intermediates are kept. After landing, I also re-ran the strict monitor at tip `6a1821a`: 62/62, restraint 8, depth 8. That commit adds only evidence and SCORECARD/LOG text. No other axis is claimed or inflated.

## Sources & frontier

**Sources:** 80→81 rows.
- Tiers: A 71→72, B 7→7, C 2→2.
- Statuses: mined 51→52, queued 23→23, rejected 6→6.
- Malformed rows: 0→0.
- One added row, S083 (own-work, tier A, scoped to the lane's persisted required-command declarations). No existing row's status, recheck, used-by or immutable field changed.
- No frontier row advanced: this is same-ground calibration.
- CorpusClaim's suggestion to remove the stale `Next unused id: S083` line was rejected, because those lines are append-only under the round-18 QUALITY35 rule.

Counting command (author receipt at 336565f: `.ufo/evidence/round-23/source-invariants.json`; final at 549ede2: `final-verification.json` `monitor-final` `sources`):

```sh
git show "$REV:corpus/SOURCES.md" | python3 -c 'import sys,re,collections,json; r=[[c.strip() for c in x.split("|")[1:-1]] for x in sys.stdin.read().splitlines() if re.match(r"^\|\s*S[0-9]{3,}\s*\|",x)]; print(json.dumps({"rows":len(r),"tiers":dict(collections.Counter(x[3] for x in r)),"statuses":dict(collections.Counter(x[7] for x in r)),"malformed":sum(len(x)!=11 for x in r)},sort_keys=True))'
```

The source quote, open date and bounded lookup are recorded in the r23 lesson `## Gate`. The mined mistake (lesson `## Mistakes` row 1) is source-read or count credit substituting for a required command. Its fix is QUALITY46, and it is shown able to fail: the same receipt is clean 0 with the correct argv and 1/ARGV_MISMATCH with the source-read argv. The appended row for the replay-metadata overclaim is explicitly not counted as failure-backed.

Census command, executed at both endpoints:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

Start, exit 0 (`.ufo/evidence/round-23/census-start.json`); end, exit 0, stderr empty (`final-verification.json` `census-final`). Both runs print the same output:

```text
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi	W04	S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi	W04	S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi	W04	S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi	W04	S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

The W04 notices are pre-existing repeated URLs across scopes. Census success is conformance, not claim admission.

## Trend verdicts

- **Expansion: unchanged.** This is a same-ground calibration repair. A capability row was added (`required-command-receipt-binding`, SCORECARD.md:1045), but no uncovered coverage-map ground is claimed.
- **Quality: improved.** A real source-read substitution that output-only checking accepts is now rejected 1/ARGV_MISMATCH, while the correct command is clean. Fresh falsifiers exposed three overclaims, which were corrected append-only with QUALITY47. Strict source credit is restored to 62/62, and 46/46 registered outcomes hold at the measured revision.
- **Discernment: unchanged.** The admit/reject decisions and the falsifier agreement come from our own seats, which are not an outside spot-check. A non-author closure must sample them.

## SHONEN

- [~] Real sourced decision tables/error patterns/checklists — lane assertion `SHONEN.md:5-6`; SKILL.md registry rows plus the SKILL.md:2033 correction; S083, QUALITY46/47. No independent promotion verifier.
- [~] End-to-end domain task executed and logged — frozen 43-command replay, source-read substitution red, final battery 46/46; LOG.md:1589, `final-verification.json`. No independent promotion verifier.
- [~] Instructions executable without oral context — strict input-keyed monitor 62/62 at 549ede2 with the 267-entry ledger. These are author byte reads, not independent or blind cold-read or required-command execution (`SHONEN.md:9-10`). No promotion credit.
- [~] No cross-domain bleed — PROVINCE.md unchanged. Only this lane's gate, corpus and evidence were edited; the kagi misroot was left untouched (`SHONEN.md:11-12`). No independent promotion verifier.
