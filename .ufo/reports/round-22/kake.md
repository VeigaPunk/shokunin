# kake — round 22 report (recovery attempt 2)

## Work performed

Declared claim (1 of 1–3): **C1, operability, capability acquisition: offline static canonical publishing preflight.** It is a read-only, network-free validator for local static HTML. A frozen 32-case matrix measures it. Operability and freshness are both at the saturation line, so they tie for lowest owned axis. C1 is also the move that SCORECARD's stagnation nudge planned (round 21 added no capability). Claim contract frozen before dispatch: `kake-shokunin/.ufo/waves/round-22/contract.json`.

- Recovery coordinator KakeR22Recovery, operator-authorized. Attempt 1 ended without a report (`.ufo/watchdog.log:546`, `lane-dead-no-report kake round=22`). Claim base `7c61c8c` preserved. Attempt-1 commits `c0fd6d5` (integration) and `26b27af` (checkpoint, wave-2 reports) were already pushed. Reuse and discard are recorded in `kake-shokunin/corpus/lessons/round-22.md` §Recovery attempt 2.
- Attempt 1 (reused): validator `scripts/canonical_audit.py`, matrix/cases/fixtures, counter `measure.py`, `replay.py`, S020–S027, knowledge entry `corpus/knowledge/static-canonical-preflight.md`, and QUALITY round-22 criteria for the round-21 spot-check routed notes 1–4 (`corpus/QUALITY.md:75-94`). Re-verified unchanged since `c0fd6d5`: cases.json, fixtures, matrix.py and contract.json (`residual/CritAdmission.md` Attack 2).
- Wave-2 integration: 43 of 64 seat reports existed and were read. Defects fixed in landed `b539cc1`:
  - empty-authority `///path`/`//`/base `///` false clean (`w2/Attack05.md`);
  - usage errors printed no stdout JSON, and a repeated `--manifest` let the last path win (`w2/BoundaryCLIErrors.md`);
  - manifest symlink scope (`w2/BoundarySymlinks.md`);
  - the counter repeated the matrix's declared numerator, and an unmeasurable baseline exited 0 (`w2/FalsifyCounting.md`);
  - replay compared aggregates only; dead-seat wording (`w2/FalsifyAdmissions.md`).
- Residual review (8 seats, one ordinary task call). Fixed after they returned:
  - `alias/../manifest.json` audited a different file (`residual/CritScope.md` P2);
  - a self-consistent stub matrix passed the counter (`residual/ResRevCounter.md` P2);
  - help synopsis (`ResRevCliUsage.md` P3);
  - fd ownership on an interrupted close (`ResRevManifestFd.md` P3).
  - No counterexample: `ResRevNetPath.md` (40+ spellings), `CritAdmission.md` (all six admission attacks hold), `CritScope.md` (both scope decisions kept). Per-case replay was shown able to fail (`ResRevReplayRepin.md`).
- Failure-capable fix evidence: `.ufo/waves/round-22/postfix/defect-probe-{before,after}.json` (2/8 met on `c0fd6d5` → 8/8) and `counter-probe-{before,after}.json` (3/3 counter-examples accepted by the `c0fd6d5` runner → 3/3 rejected). Selftest is 62/62 (`postfix/selftest-after.json`); the `c0fd6d5` selftest was 56/56 and had none of the new cases.
- Planner seat: held by the L1 (validator rejects `planner`). No planning data-walk rode a seat this attempt.
- Stale-lane: respawn-per-round driver; this assignment opens no other kake mission. No next round was started.
- Tool installs/updates: none (L1 and residual seats reported none). pacman pause respected.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` found no kake-authored fleet-root file. `-.rej` (charter-scribe content) and `.ufo/state/*` belong to others and were untouched. A seat-created `kake-shokunin/scripts/__pycache__/` was removed and never committed.

Waves and seats (round total 136 of ≤200):

| Wave | Seats | Roles | Dead |
|---|---|---|---|
| w1 build (attempt 1) | 64 validated/dispatched | 35 scout, 8 reviewer, 6 critic, 4 connector, 4 scribe, 3 executor, 2 simplifier, 1 sentinel, 1 revenger | 4 scribes (RegistryDraft, Knowledge, LessonDraft, TrendDraft): `anthropic/claude-haiku-5-5` 429 rate_limit_error, retry-after-ms=8182000 (`w1-deaths.json`) |
| w2 falsify (attempt 1) | 64 validated/dispatched | 28 reviewer, 24 scout, 4 critic, 4 mutation-tester, 4 connector | 21 seats, no report; attempt-1 coordinator died mid-wave (SIGHUP/provider quota per watchdog), last error text unrecoverable: 9 reviewer, 8 scout, 4 connector (names in lesson §Reuse and discard) |
| residual (attempt 2) | 8 (ordinary task call, ≤8 rule; 72 left was too few for a genuine new 64-item wave) | 6 reviewer, 2 critic | 0 |

## Landed changes

| Commit (landed) | Content | LOG entry |
|---|---|---|
| `c0fd6d53906a42dadfb997ddda2c8162f1adb78a` (attempt 1) | validator, frozen matrix, counter, replay, S020–S027, knowledge entry, QUALITY, SKILL row | `LOG.md` §Round 22 — static canonical publishing preflight |
| `26b27af3be44fec9de221f716b3cf3d2861ab146` (attempt-1 checkpoint) | w2 reports and registry | same; recovery entry |
| `b539cc17c25e5f42fe8803e2aa42b4574c4b44c6` | wave-2/residual fixes (validator, counter digest pins + row-derived numerator + baseline exit 2, per-case replay, validator re-pin), postfix probes, residual reports, S028/S029, QUALITY "derived counts and resolver neighbours", knowledge/SKILL boundaries, lesson recovery section | `LOG.md` §Round 22 — recovery attempt 2 |
| `adc04dae88ec06ff507515f6bbb1619b08ccddf7` | `measure-after-v2.json`, `final-suite.txt`, SCORECARD capability row + round-22 section, LOG entry, lesson measurement | same |

Lane tip after landing: `adc04dae88ec06ff507515f6bbb1619b08ccddf7` (`jj-lane.sh state`: ahead=0 behind=0).

## Before → after measurements

C1, measured against `b539cc17c25e5f42fe8803e2aa42b4574c4b44c6` with baseline `7c61c8cc791bde36dd5e3688bdfea2678d90146c`:

```
python3 .ufo/waves/round-22/measure.py --root . --revision 7c61c8cc791bde36dd5e3688bdfea2678d90146c --cases-root .
→ exit 0; accepted 0 / total 32; available false; instrumentValidated true   (measure-before-v2.json, 2 identical runs)
python3 .ufo/waves/round-22/measure.py --root . --revision b539cc17c25e5f42fe8803e2aa42b4574c4b44c6
→ exit 0; accepted 32 / total 32; acceptedDerivedFromRows true              (measure-after-v2.json, 2 identical runs)
```

- Both runs used the same runner (sha256 `fa916ada…`). The matrix and cases digests are pinned inside the counter.
- `python3 .ufo/waves/round-22/replay.py --root .` → `frozen_replay_match`, 69 inputs verified, 32 cases compared, 0 per-case mismatches (`postfix/replay-after.json`).
- `frozen/expected.json` re-pins only the validator digest (`35433e50…` → `5de32200…`); the oracle is unchanged.
- No owned-axis harm on the exercised checks (`final-suite.txt`):
  - `node scripts/corpus-contract.mjs --json` exits 0.
  - `TZ=UTC node scripts/freshness-sweep.mjs --section=paths` exits 1 with the carried red: 3 targets, missSet 55, no new miss.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.
  - Before: `kake ok …/corpus/SOURCES.md`, exit 0 (`.ufo/waves/round-22/census-before.txt`).
  - After: `kake ok …/corpus/SOURCES.md`, exit 0 (`.ufo/waves/round-22/census-after.txt`).
- Rows: 19 → 29 over the round.
  - Attempt 1 added S020–S027, all tier A, opened 2026-10-20.
  - Recovery added S028 (RFC 9110 §4.2.1–4.2.2) and S029 (RFC 3986 §3), tier A, opened 2026-10-21. Gate receipts with ≤25-word quotes are in `corpus/lessons/round-22.md` §Sources opened in recovery. Independent re-open matched both digests (`residual/ResRevSources.md`).
- Rows touched old→new: none (no status/recheck/used-by change to an existing row). Rejects: WHATWG URL slash-skipping was considered and not opened as a row (the policy rejects both readings).
- Frontier advanced: canonical signals, from frontier to an owned capability. New study path: "Empty-authority network-path rejection".
- Sourced claim: C1's knowledge entry cites S020, S021, S026, S027, S028 and S029, all opened this round.
- Mined mistakes (`corpus/lessons/round-22.md` §Recovery mistakes), each with a fail-capable fix:
  - frozen-population blind spot (defect probe 2/8 → 8/8);
  - count-only oracle (counter probe 0/3 → 3/3 rejected);
  - dead-seat credit wording;
  - lexical path normalisation.
- Attempt-1 mistakes: retrospective chronology; signal-is-not-selection.
- The 8 w2 source re-open seats died. S020–S027 were not re-opened by an independent seat this round. ResRevSources spot-checked S020/S027 against their recorded quotes only.

## Trend verdicts

- **expansion: improved.** New owned ground (canonical signals, a new knowledge entry) and a capability row that demonstrably runs (`SCORECARD.md` Capabilities, round 22).
- **quality: improved.** Eleven falsifier-found defects were fixed with before/after probes. The counter now derives its numerator from per-case rows and pins its instrument. Replay compares per case. Bounded to the exercised populations.
- **discernment: improved (author-side, pending the non-author spot-check).** Four new mined mistakes have fail-capable fixes; two QUALITY criteria come from them. Two scope decisions were kept after a critic tried to break them. The last fixes were not re-reviewed by a seat; this is disclosed.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — not promoted; no non-author verifier this round (round-22 SKILL row at `kake-shokunin/SKILL.md:411` is author work).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched; fixtures and an archived static snapshot are not an end-to-end publishing task.
- [ ] Instructions executable by an agent without oral context — untouched.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — untouched this attempt.

Open L0 questions: none added. Open defects for the closure: the last fixes (`..` path split, help synopsis, fd ownership, counter digest pin and executed floor) are probe-verified only. w2's 21 dead items were not replaced, so source re-opens S020–S027 and the boundary items they covered remain unattacked.
