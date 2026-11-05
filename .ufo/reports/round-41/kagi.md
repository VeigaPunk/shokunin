# kagi round 41 — report (attempt 1)

Lane: kagi (secrets & vault ops). Owned axes: freshness + calibration. Lane repo `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`.
Revisions: predeclaration (frozen plan, counters, BASE controls) `5142b522fb905a237cb01aaa582b8e4543496bdd`; claim BASE `19025d97e5013bac2f45d6b9e61bfbafc84c3c8d`; positive control P0 (round-40 landed state) `6f1588cc0ebd5cbbd4e983fbd71c1e419d225ce0`; round-40 claim BASE `6cc8850dfc5757927699e5a53a876f47c8df21aa`.
**Lane hash (pushed, remote-verified): `209147c64610d76ec3a0b73ba9e499b227c84ec9`** (`git ls-remote origin refs/heads/master` → `209147c64610d7…`).

## Work performed

**Declared claims (2, both measured, neither exploratory):**

- **C1 — calibration: unjournaled loosening of ledger expectations is refused.** Frozen counter `plans/round-41-c1.sh`: BASE 0 → target 4. Axis: calibration (lowest-scoring axis class is shared by all six at 9; C1 is one of the two owned axes).
- **C2 — freshness: the `rendered-text-v1` whitespace declaration grounds on bound, current sources.** Frozen counter `plans/round-41-c2.sh`: BASE 1 → target 3. Axis: freshness.

Frozen predicates, kill rules and targets: `plans/round-41.md` (commit `5142b52`), not amended after data.

Work items, each with its pointer:

- Protocol load and claim choice: `plans/round-41.md` §Claims; SCORECARD round-41 pre-move table (`SCORECARD.md`, section `## Round 41 — pre-move`).
- Predeclaration controls, committed at `5142b52`: `.ufo/waves/round-41/controls/` (`c1-control-{no-gate,refuse-all,accept-all}.txt` → 0/0/0; `c2-control-decoy.txt` → 2; `c2-base-19025d9.txt` → 1).
- Wave `build` (one v1 wave, 11 seats), spec `.ufo/waves/round-41/build-spec.json`, validated under `scripts/hyaku/ufo-wave-policy.json` (`counts.total: 11`); dispatch `build-dispatch.json`; ready `build.ready`; orchestrator `WAVE-DONE build` received; per-seat reports `.ufo/waves/round-41/build/<seat>.md`. Results manifest `build-results.json` (11 seats, names only, no status field).
- C1 gate `corpus/expect-journal.sh` built by K41ExecJournal (sha256 `807501052598f05c162d780e4e327697a155d0369a0fd3ecf29a354489343756`; receipts `.ufo/waves/round-41/build/K41ExecJournal/`). Rules R1 `UNJOURNALED`, R2 `OLD_MISMATCH`/`COMMAND_MISMATCH`/`NEW_MISMATCH`, R3 `NOT_LITERAL`, R4 `WARN ORPHAN` (warning only), setup exit 2.
- C2 Sources paragraph of `corpus/rendered-text-v1.py` re-grounded on S095, S096, S097 by K41ExecDocs (sha256 `14f6ca6ab742296f45a699548c31e6d49892f6baef36ed419c283d1a0511b8c9`; `diff.txt`, `selftest.txt`, `unicodedata.txt`). Normalizer rule (step 5) unchanged.
- Registry: S097 admitted (tier A, docs; `str.isspace()` whitespace definition, opened 2026-11-05, body `.ufo/waves/round-41/capture/S097.body`); S098 rejected (tier A, spec; UTS #18 `\s` = White_Space excludes U+001C–U+001F, measured by K41LabRejectProbe, `probe.txt` verdict H0 holds: A−B = 4 code points, B−A = 0). Rows: `corpus/SOURCES.md` lines 104–105 (one row, S097, was first appended without its trailing pipe and fixed in the same commit; the census caught it as `SC_MALFORMED nf=12`). Fetch rows: `corpus/source-fetches.tsv` lines 140–141.
- Lesson `corpus/lessons/round-41.md` (Claims, Gate, Mistakes M41-1..M41-3, Frontier, Routed, considerthese). Log entry `LOG.md` (last bullet, round 41).
- Migration of the six round-40 debt expects (`R13-01`, `R21-02`, `R24-06`, `R31-02`, `R33-02`, `R34-03`) in `corpus/claim-ledger.tsv`, journaled in `.ufo/waves/round-41/expectation-migrations.json`. Measured values: heading count 54 → 56; `row-identity scorecard-rounds` count 56 sha256 `33f1893f1fabe500324920f586f82907449f1de4c4b2d56ac74c09c436d375bd`; census `rows=98 A=94 B=2 C=2 queued=1 mined=93 rejected=4 entries_sourced=14 legacy=21 captures=98 inrow=16 inrow_only=0 inrow_nonreproducing=12`.
- `SKILL.md` gate registry row for `corpus/expect-journal.sh` (SD7 finding fixed by row, not by prose). `SCORECARD.md` round-41 pre/post sections, the round-40 erratum (appended, not rewritten; names M40-3), and the post-move calibration row carrying the lane-status reds `R25-02`, `R29-01`, `R29-02` (SD5 finding).
- `corpus/stamps.tsv` reviewed re-pin (`claim-ledger.sh stamp` over the 122 stamped paths; `git diff` shows exactly seven changed rows: `corpus/claim-ledger.tsv`, `corpus/rendered-text-v1.py`, `corpus/source-fetches.tsv`, `corpus/SOURCES.md`, `LOG.md`, `SCORECARD.md`, `SKILL.md`; receipt `.ufo/waves/round-41/stamp-run.txt`).

**Incidents and how each was handled:**

- `plans/round-41-controls.sh` runs its C2 BASE line in the working tree, not a pinned revision (critic defect 1). Running it after landing overwrote `c2-base-19025d9.txt` with 3. Restored from `5142b52`; BASE re-measured from a clean `git archive 19025d9` extraction with the `5142b52` counter: C2 = 1, C1 = 0. The controls runner is **not** fixed this round (the frozen counter is untouched); routed to round 42.
- The first push of `209147c` was refused by the remote with `fatal error in commit_refs_rules` (helper classified it fatal, no retry). Commit contents were scanned for credential-shaped strings and structural anomalies (no gitlinks, no symlinks, no nested `.git`, no matches). A retry about 90 s later through `jj-lane.sh push` landed (`landed 209147c…`, remote confirmed). The first refusal is recorded as a transient remote error; no content cause was found.
- The C1 gate's `*.json` journal discovery fails closed (exit 2) when pointed at a wave directory, because `build-dispatch.json` and similar files are not journals. The landing check used a journal-only scratch directory. Routed to round 42.

**Seat roster and attack share (wave `build`):** 11 seats: executor 3 (K41ExecJournal, K41ExecDocs, K41LabRejectProbe), scout 1 (K41ScoutSources), scribe 2 (K41ScribeRegistry, K41ScribeLesson), connector 1 (K41ConnOverlap), reviewer 2 (K41ReviewJournal, K41ReviewDocs), critic 1 (K41CriticClaims), mutation-tester 1 (K41MutGates). Attack seats (reviewer, critic, mutation-tester) = 4 of 11 = 36 % (floor 25 %). Connector seats: 1. Planner: the L1 holds the canonical planner seat (validator rejects `planner`). The labrat role was not in the swarm role set and was remapped to `executor` for the S098 probe (spec `build-spec.json`, item K41LabRejectProbe). Dead seats: none (11 of 11 wrote a seat report; no seat ended without output). Residual call: none. Round total: 11 seats, one wave, band 8–16.

## Landed changes

| Change | LOG.md | Commit |
|---|---|---|
| Frozen plan, counters, BASE controls, BASE receipts (predeclaration) | round-41 line (predeclaration) | `5142b522fb905a237cb01aaa582b8e4543496bdd` |
| C1 gate `corpus/expect-journal.sh`; C2 Sources paragraph `corpus/rendered-text-v1.py`; S097/S098 rows and fetch rows; ledger migrations; SKILL gate row; SCORECARD round-41 sections and erratum; stamps; lesson; wave evidence; migration journal | round 41 entry | `209147c64610d76ec3a0b73ba9e499b227c84ec9` |

## Before → after measurements

Each counting command below was run at the stated tree and its output is pasted or pointed to.

| Claim | Before (BASE) | After (candidate / landing) | Counting command and receipt |
|---|---|---|---|
| C1 calibration | 0 — `bash plans/round-41-c1.sh` at clean `19025d9` archive: `0` (no gate file) | 4 — `EXPECT_JOURNAL=corpus/expect-journal.sh bash plans/round-41-c1.sh` → `4`, rc 0, at `209147c` | `plans/round-41-c1.sh` (frozen); receipts `.ufo/waves/round-41/controls/c1-control-*.txt`; `.ufo/waves/round-41/build/K41ExecJournal/c1-counter-readings.txt` |
| C1 controls | blanket-refuse 0, blanket-accept 0, no-gate 0 | unchanged, 0/0/0 | `bash plans/round-41-controls.sh` (receipts; see the incident above for the C2 BASE line) |
| C1 P0 acceptance | — | `expect-journal.sh --base-ledger <6cc8850 ledger> --ledger <6f1588c ledger> --journals <journal-only dir with round-40 migration>` → `EXPECT_JOURNAL: CLEAN (changed=6 journaled=6)`, rc 0 | scratch receipts; command recorded here |
| C1 landing check | — | `expect-journal.sh --base-ledger <5142b52 ledger> --ledger corpus/claim-ledger.tsv --journals <journal-only dir with round-41 migration>` → `EXPECT_JOURNAL: CLEAN (changed=6 journaled=6)`, rc 0 | same |
| C2 freshness | 1 — `bash plans/round-41-c2.sh` at clean `19025d9` archive (counter from `5142b52`): `1` (a 0, b 0, c 1) | 3 — `bash plans/round-41-c2.sh` → `3`, rc 0, at `209147c` | `plans/round-41-c2.sh` (frozen); `.ufo/waves/round-41/build/K41ExecDocs/c2-counter-readings.txt`; decoy control `c2-control-decoy.txt` → 2 |
| Registry (context) | 96 rows (`bash corpus/sources-census.sh` → `rows=96 … captures=96`, rc 0) | 98 rows (`bash corpus/sources-census.sh` → `rows=98 A=94 … captures=98`, rc 0; `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` → `kagi ok`, rc 0) | `.ufo/waves/round-41/census-lane-pre.txt`, `census-landing-pre-ledger.txt`, `census-validate-pre-ledger.txt` |
| Full ledger verify (context) | P0 `6f1588c`: `CLAIM_LEDGER: POLICY (claims=86 policy=3 stamped=122)` | `CLAIM_LEDGER: POLICY (claims=86 policy=3 stamped=122)`, rc 2; red set equal to P0 (see below) | `bash corpus/claim-ledger.sh verify` → `.ufo/waves/round-41/verify-landing-final.txt` |
| R36-01 (SD5-driven) | 3 at the first landing pass (round-41 calibration row omitted the lane-status reds) | 0 after the SCORECARD row fix — `bash plans/round-36-c1.sh` → `0`, rc 0 | `plans/round-36-c1.sh` |

Verify red set at the landing tree, compared with P0: FAIL `R11-08`, `R22-03`, `R24-15`, `R25-02`, `R36-03`; POLICY `R29-01`, `R29-02`, `R38-03`; the same five FAIL rows and three POLICY rows as P0 (`R22-03`/`R24-15` reason string differs: `verdict-not-final` at landing, `exit-mismatch` at P0; the same rows flip with clone environment, as the round-40 closure recorded). No STALE line after the stamp re-pin. No `R13-01`, `R21-02`, `R24-06`, `R31-02`, `R33-02` or `R34-03` line appears.

## Sources & frontier

- **SOURCES rows before → after (counting command `bash corpus/sources-census.sh`, rc 0 both):** `rows=96 A=92 B=2 C=2 queued=1 mined=92 rejected=3 … captures=96` → `rows=98 A=94 B=2 C=2 queued=1 mined=93 rejected=4 … captures=98`. Fleet validate `kagi ok`, rc 0.
- **Rows added by tier:** tier A, docs: S097 (mined, `str.isspace()` whitespace definition, Python 3.15.2 `stdtypes`, opened 2026-11-05); tier A, spec: S098 (rejected, UTS #18 `\s`, opened 2026-11-05, flip condition recorded).
- **Rows touched old → new:** no existing registry row edited in place (CORPUS.md SOURCES rule 2). Ledger expects (not registry rows): `R13-01` `^54$`→`^56$`; `R24-06` `count=54 sha256=52e7ba8d…`→`count=56 sha256=33f1893f…`; `R21-02`, `R31-02`, `R33-02`, `R34-03` census summary `rows=96 A=92 mined=92 rejected=3 captures=96`→`rows=98 A=94 mined=93 rejected=4 captures=98`.
- **Frontier rows advanced:** the rendered-text whitespace ground (S097 admitted; S098 rejected on fresh data); the expect-journal calibration ground (the gate, the migration journal). No frontier-to-core move; no new `corpus/knowledge/` entry.
- **Sourced claim (§2b.4):** C2 rests on S095 (re-opened, byte-identical to the round-40 capture; `cmp` exit 0) and S097 (opened this round). Scout receipts: `.ufo/waves/round-41/build/K41ScoutSources/`.
- **Mistake mined (§2b.3):** M41-1 counter accepted loosened expects (`corpus/lessons/round-41.md` §Mistakes; evidence `.ufo/waves/round-41/build/K41ReviewJournal/`); captured-by `none`; fix shown able to fail: the gate refuses F1–F4 with their frozen tokens and the counter reads 4 (blanket-refuse and blanket-accept read 0). M41-2 (normalizer Sources cited superseded or unidentified docs) fixed by C2. M41-3 (planner seat absent in round 40) is a conformance item: the L1 held the planner seat this round; no executable fix applies.
- **Assimilation:** none. `merge/kagi/` was not opened (quarantine-first is not this lane's obligation; see the lesson §Quarantine). considerthese: `considerthese/2026-10-26.md` proposals 1 and 3 remain unimplemented; not taken this round (no claim slot).
- **Frontier and capability:** the expect-journal gate is a new capability with its own selftest row in SKILL.md (`corpus/expect-journal.sh --selftest` → `EXPECT_JOURNAL_SELFTEST: PASS (cases=7)`, rc 0).

## Trend verdicts

- **expansion: unchanged.** Two rows added on already-held normalizer ground; no coverage or adjacency surface moved (`SCORECARD.md` coverage 9 → 9; the S098 rejection is a rejection, not an expansion).
- **quality: improved.** Freshness moved on its frozen counter (C2 1 → 3): the normalizer's declaration now cites current, non-superseded ids, carries one bound quote and binds a body by sha. Operability is unchanged as a score (the new gate has a selftest; nothing schedules it).
- **discernment: improved, with a disclosed caveat.** C1 moved 0 → 4 on its frozen counter with both blanket controls at 0. Caveat: the mutation runner prepared for the gate (`.ufo/waves/round-41/build/K41MutGates/run-mutants.sh`) matches only 4 of 11 C1 mutants on the delivered gate (its anchors were written against the seat's fixture gate). On the real gate: `MUTANTS C1: killed=0 survived=4 total=4` with 7 NOT-GENERATED (`.ufo/waves/round-41/mutants-landing.txt`). The `refuse_exit0` mutant rewrote an `exit 1` in the selftest, not the refusal path, so it is not evidence either way. The C1 discrimination claim therefore rests on the frozen counter and the blanket controls, not on the mutation battery. C2's mutants on the real paragraph: `MUTANTS C2: killed=4 survived=3 total=7` (`drop_S095`, `drop_S096`, `drop_S097` survive, as the seat predicted: term (a) needs one good id).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` gate registry (new row for `corpus/expect-journal.sh`, line 827) and existing decision tables; citation gate unchanged.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: round-41 LOG bullet (`LOG.md`, last entry): S095 re-open and S097 admit/S098 reject on live sources, with receipts `.ufo/waves/round-41/capture/`.
- [~] Instructions executable by an agent without oral context — evidence: `corpus/expect-journal.sh --selftest` (`EXPECT_JOURNAL_SELFTEST: PASS (cases=7)`) and `plans/round-41-c1.sh` / `plans/round-41-c2.sh` run from the committed tree.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: connector sweep `.ufo/waves/round-41/build/K41ConnOverlap.md` (no sibling owns the expect-journal or the rendered-text normalizer; the whitespace-class adjacencies are reported, not absorbed).

No `[x]` is written: no non-author verifier has closed this round yet.

## Routed to round 42

- Mutation runner: its anchors must be written against the delivered gate (`.ufo/waves/round-41/build/K41MutGates/run-mutants.sh`); rerun the 11 C1 mutants on the real file.
- Gate `*.json` journal discovery: exits 2 on a wave directory; restrict discovery to a named journal pattern in the frozen interface (a frozen-counter amendment).
- `plans/round-41-controls.sh`: the C2 BASE line must run from a `git archive` of `19025d9` (critic defect 1).
- Row deletion from the candidate ledger is outside the frozen classes (attack A6); a `MISSING_ROW` rule is round-42 instrument work.
- C3 counter defect (M40-9, M40-10, M40-17); gate-selftest scratch defaults `${TMPDIR:-/tmp}` in `corpus/anchor-pins.sh`, `corpus/claims-declared.sh`, `corpus/prefreeze-control.sh`, `corpus/self-description-sweep.sh`, `corpus/surface-census.sh`.
- Plan §C1 sentence "accepts F1–F4 by construction" overstates F4: the pre-change gate refuses the echo rebind by policy (`first-token:echo`), not by acceptance (reviewer finding 2). Corrected here by this text, not by a rewrite of the frozen plan.
- Round-40 report was amended in place (`.ufo/reports/round-40/kagi.md`); correction belongs in an appended erratum (not done here).

## Stale-lane

Stale-lane: no (respawn-per-round driver; no other mission of this lane is open).

## Tool installs

None. Every seat reported `Tool installs: none`. (`curl`, `python3`, `git`, `sha256sum`, `cmp`, `awk` were already present.) Operator rules read: `/home/vgpnk/.omp/agent/RULES.md`.

## Misroot sweep and open state

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` before filing: `M .scratch/run15-state.json` (orchestrator-owned, not touched), `?? .ufo/closure-kaidoku-r92.json` (another lane's closure, not touched). No round-41 seat wrote into the fleet root.
- L0 questions appended this round: none. Open decisions are routed above; none needs an operator ruling to close the round.
- Scratch `/fast/scratch/hyaku/kagi-r41` removed after the landing runs (§7.6).
