# souji — round 96 (attempt 1)

Stale-lane: no (respawn-per-round driver; no other mission of this lane is open).
Lane: souji-shokunin · base `689d1c9570a5df2344e16a5916c49e24b46823ab` · instruments P1 `0656de3f` · controls P2 `4dd8a103` · freeze F `c1209623` · lane HEAD and pushed `2bbbab6d8c150e92523553d357764a5c185c42fb` (ls-remote = HEAD).
Verdict: **C1 harmed (trade, not admitted); C2 verified on a narrowed reading.** Operator ruling requested on C1 (see Open L0).

## Work performed

Declared claims (2 of the 1–3 cap; each one axis-move, causally separable):
- **C1 — calibration 7 (the lowest owned non-retired axis).** Claim: the r96 search's SystemExit leg clears a
  top-level-caught SystemExit so the Q172 declared-shape table reads `mismatched=0` (r95 hook: 2 on the same twelve
  scripts). Target axis: calibration. **Measured result: a gain on that table and a harm on two terminating shapes the
  r95 hook scored correctly → harmed (trade).**
- **C2 — operability 8.** Claim: the r96 forgery probe stops waiting on pipe EOF after the process-group kill, so the
  T1 pipe-holder arm refuses with exit 2 + `C2-FORGERY-FATAL:` within its timeout (r95 probe: `hung`), counted by
  the twenty-arm counter. Target axis: operability. **Measured: verified on the narrowed reading (A7).**
- Frontier step (inside the cap): corpus/SOURCES.md contract v1 — S368 (setsid(2), opened and quote-verified this
  round) admitted; S369–S371 supersede the over-claimed teaches of S365–S367; lesson `corpus/lessons/round-96.md`
  (Gate, Mistakes); knowledge entries `crash-channels-beyond-excepthook.md` (r96 section rewritten) and
  `deadline-owned-reaping.md` (new this round, two false limit clauses withdrawn).

Work items (evidence pointers):
- Protocol and mission load: MISSION.md, AXES.md, CORPUS.md §SOURCES, SCORECARD `### Planned (r96)`, the r95
  non-author spot-check §7 (`corpus/lessons/round-95-verifier-spotcheck.md`). Evidence: `plans/round-96.md` A0.0.
- Instruments landed at P1 `0656de3f`: `census/round-96/c1-survivor-search.py` (sha256 33c4bf63…), `declared-shapes.py`
  (aa804f4d…), `shapes/` (12 named shapes of 42 files), `c1-targets.json` (320ea2ec…), `c2-forgery-probe.py`
  (9f989da8…), `c2-setup-arms.py` (05c05ab1…, twenty arms), `c2-forgery-controls.py` (403f7d23…),
  `c1-control-r95-rule.py` (8f92c965…), `c1-forgery-controls.py` (2e58b239…). Commit: `git log 0656de3f -1`.
- Controls at P2 `4dd8a103`: `census/round-96/controls/{c1-control-r95-rule,c1-forgery-controls,c2-control-r95-probe,c2-forgery-controls}.txt`
  and `prefreeze-feasibility-note.txt`.
- Freeze F `c1209623`: `census/round-96/preregistration.txt` (only file in F).
- Wave w1 (13 seats; validated under `scripts/hyaku/ufo-wave-policy.json`, one batched dispatch): spec
  `.ufo/waves/round-96/w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json` (13/13 settled, WAVE-DONE
  from the orchestrator), claims `.ufo/waves/round-96/claims.json`, ledger `claim-falsification.tsv` (14 rows; gate
  pass below). Seat reports in `.ufo/waves/round-96/w1/R96*.md`.
- Integration (L1): reproduced the module-level `finally` and re-raise shapes under the frozen r95 and r96 hooks
  (`plans/round-96.md` A1: r95 70, r96 1; L1 scratch only, not committed). Opened setsid(2) (sha256 52cbc190…, 17-word
  quote occurrence 1). Narrowings A1–A11 recorded in `plans/round-96.md`.
- Leak sweep before filing: two orphaned `fixture-pipe-holder.py` grandchildren from this wave's arm runs were still
  alive (reparented to init): PID 2085368 (sentinel arms, 27 min old) and PID 2254969 (L1 after-arm run). Both command
  lines were checked to lie under `/fast/scratch/hyaku/souji-r96/` and both were SIGKILLed; `ps` then showed zero.
  Reaping by process group is not sufficient for these (A4); see Open L0 on the reaping authority (PROVINCE F5 HOLD).
- After receipts on committed bytes: `census/round-96/records/c1-after.txt` (`SEARCH-SUMMARY … errored=7 killed=2
  survived=1`, check line `check=pass`, EXIT 0); `shapes-after.txt` (`SHAPES-SUMMARY shapes=12 mismatched=0`, EXIT 0);
  `c2-after.txt` (`ARMS-SUMMARY arms=20 conform=20`, EXIT 0, first run; the probe and counter bytes are unchanged since P1 `0656de3f`).

Seat evidence used in the verdicts (all in `.ufo/waves/round-96/w1/`):
- C1 falsifications: `R96ScoutSources.md` §3 (module-level finally), `R96ReviewerC1.md` Q1 (re-raise, q1e),
  `R96Sentinel.md` F-1 (excepthook/thread block, E10) and F-2 (fallback fd 2, E5/E9), `R96ReviewerShapes.md` §3 (the
  "r94-rule mismatched=6" label).
- C2 falsifications: `R96Sentinel.md` F-4 (E6a–E6d: the counter's killpg does not reach the setsid grandchild),
  `R96Scribe/reapcheck.out` (B: one survivor after the counter-style kill; C: two after the probe exits),
  `R96ReviewerC2.md` Q1a (unbounded output → 27.3 GB RSS, SIGTERM at 36 s, no FATAL).
- Undermining, not falsification: `R96Critic.md` (2) (basename cheat reaches 20/20); `R96MutC2.md` survivors M3/M5.
- Census (neutral): `R96ExecCensus.md` — full population r96 and r95 identical: `killed=139 survived=76 errored=53`,
  zero differing verdicts, survivor sets identical (268 scored ids).
- Connector (neutral): `R96Connector.md` — no sibling owns the surface; SOURCES rule 2 PASS.

Commands (counting commands, paste-ready):
```
python3 -B census/round-96/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness census/round-93/c1-false-row-harness.py --population census/round-93/c1-false-rows.tsv --lane . --fleet-root /home/vgpnk/Projects/shokunin --work <empty> --jobs 5 --ids census/round-96/c1-targets.json
python3 -B census/round-96/declared-shapes.py --search census/round-96/c1-survivor-search.py --scripts census/round-96/shapes --work <empty>
python3 -B census/round-96/c2-setup-arms.py --probe census/round-96/c2-forgery-probe.py --fixture-pass tests/fixtures/r93-k4-flagfail.py --fixture-fail tests/fixtures/r92-k4-flagfail.py --tool tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty>
```

Prefile gate (addendum §8): `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 96` →
`PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=8 findings=0`, exit 0.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| P1 instruments, shapes, S365–S367 rows and captures, crash-channels entry, plan A0 | `LOG.md` r96 | `0656de3f` |
| P2 controls and feasibility note | `LOG.md` r96 | `4dd8a103` |
| F preregistration | `LOG.md` r96 | `c1209623` |
| Narrowings A1–A11, S368 + S369–S371 rows, reaping and crash-channel corrections, lesson, SCORECARD r96 rows, LOG, after receipts | `LOG.md` r96 (Narrowed before filing; Sources) | `2bbbab6d` |
| Wave evidence (spec, dispatch, results, claims, ledger, seat reports) | `LOG.md` r96 (Wave) | on disk under `.ufo/waves/round-96/` (git-ignored; not committed) |

Note: `.ufo/waves/` is git-ignored in this lane; the wave evidence is on disk and cited by path, not committed.

## Before → after measurements

| claim | axis | before (command, commit) | after (command, commit) | verdict |
|---|---|---|---|---|
| C1 declared-shape table (`mismatched`) | calibration 7 | r95 hook: `python3 -B census/round-96/declared-shapes.py --search census/round-95/c1-survivor-search.py --scripts census/round-96/shapes --work <empty>` → `SHAPES-SUMMARY shapes=12 mismatched=2` (t1/t4 70); commit `4dd8a103` (P2 control) | r96 hook: `… --search census/round-96/c1-survivor-search.py …` → `SHAPES-SUMMARY shapes=12 mismatched=0` (`records/shapes-after.txt`); instrument commit `0656de3f`, receipts `2bbbab6d` | gain on t1/t4 |
| C1 terminating module-level shapes (reproduced by the L1; not in the table) | calibration 7 | r95 hook: `fshape_modfin.py` 70, `fshape_reraise.py` 70 (errored, correct) | r96 hook: 1, 1 (declared, wrong); plain rc 1 for both | **harm** |
| C1 ten-target search | calibration 7 | frozen r95 search: `errored=7 killed=2 survived=1` (`controls/c1-control-r95-rule.txt`, P2) | r96 search: `errored=7 killed=2 survived=1`, check line `check=pass`, EXIT 0 (`records/c1-after.txt`) | unchanged |
| C2 T1 arm | operability 8 | r95 probe: `ARM T1 exit=hung`, `ARMS-SUMMARY arms=20 conform=19` (`controls/c2-control-r95-probe.txt`, EXIT 1) | r96 probe: `ARM T1 exit=2 … conform=yes`, `ARMS-SUMMARY arms=20 conform=20`, EXIT 0 (`records/c2-after.txt`, first run on committed bytes) | +1 arm, verified (narrowed) |
| C2 first-run anomaly | operability | `ARM S12 exit=-15` in the first after run, the first r95 control run and the first MutC2 baseline (A8) | reruns conform (rerun 2: 20/20; control rerun 2: 19) | disclosed, not repaired |

## Sources & frontier

- SOURCES census (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`): EXIT 0 at round end
  (only the expected W04 cross-scope duplicate-URL warnings, 94 lines).
- Rows before → after: `git show 689d1c95:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 286;
  `grep -cE … corpus/SOURCES.md` → 293. `git diff --numstat 689d1c95 -- corpus/SOURCES.md` → `7 0` (additions only).
- Rows added by tier: tier A 7 (S365, S366, S367 from P1, carried by the r95 captures and re-verified live by the scout
  this round; S368 setsid(2) new; S369–S371 superseding rows). Tier B 0, tier C 0.
- Rows touched old→new: none (no existing cell changed; CORPUS rule 2).
- Frontier rows advanced: the process-group claim in `deadline-owned-reaping.md` is now sourced (S368), where previously
  its only source (S367) did not carry it; the EH/fd teaches of S365/S366 are corrected to what their quotes carry
  (S369/S370). The r96 scout's `write(2)` EAGAIN candidate was screened and not rowed (flip condition in the lesson).
- Knowledge entries: `deadline-owned-reaping.md` (new, sourced S367/S368), `crash-channels-beyond-excepthook.md` (r96
  section rewritten as a trade verdict).

## Trend verdicts

- **expansion: improved.** New knowledge entry `deadline-owned-reaping.md` on the uncovered reaping ground, citing the
  mined row S368 (tier A, the process-group fact); registry 286 → 293.
- **quality: improved.** C2 operability: the T1 arm moves from `hung` to exit 2 + FATAL (19 → 20 conforming arms, after
  receipts on committed bytes). Two false limit clauses and the "cannot block" and "momentarily" wording withdrawn.
- **discernment: harmed.** C1 calibration: the EH clear that fixes the top-level-caught shapes also turns two terminating
  module-level shapes from errored to declared (reproduced in both directions by the L1). Not admitted; the score stays 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Decision tables/Error patterns/Checklists/Gate registry; corpus/SOURCES.md S100-S103 and S368-S371; corpus/lessons/round-96.md Gate
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md (Round 96 entry: C1 and C2 instrument runs on committed bytes, `records/c1-after.txt`, `records/c2-after.txt`)
- [~] Instructions executable by an agent without oral context — census/round-96/run-receipt.sh; census/round-96/records/c1-after.txt; census/round-96/records/c2-after.txt
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-96/w1/R96Connector.md` §1 (no sibling owns the surface); PROVINCE.md reaping HOLD referenced in plans/round-96.md A4

No box is `[x]`: no named non-author verifier has checked the round's promotion-relevant claims beyond the wave's own
seats, and the C1 verdict is a harm.

## Round shape and wave

- One v1 wave, 13 seats, `w1` (band 8–16): executor 3, reviewer 3, critic 1, mutation-tester 2, sentinel 1, connector 1,
  scout 1, scribe 1. The L1 holds the canonical planner seat (the validator rejects `planner`). Attack seats (reviewer,
  critic, mutation-tester, sentinel, connector): 8/13.
- Residual calls: none. Round total: 13 seats.
- Dead seats: none. All 13 settled with output; each `R96*.md` report exists. The S12 `exit=-15` anomaly is a probe
  arm, not a seat death (A8).
- Labrat: the validator refuses `labrat` as a swarm role; the prereg's labrat task ran as a reviewer (`R96ReviewerShapes`).
- Spec header: the prereg's ROUND SHAPE line said 12 seats while its role list sums to 13; the claims file and the spec
  carry 13 (`plans/round-96.md` A0.2).
- Tool installs: none (no pacman, uv, npx, binary fetch, sysctl or sudo). Recorded per `~/.omp/agent/RULES.md`.

## Mistakes

- **M1 — a clear scoped by frame name.** Class: a gate whose table omitted the shape that breaks it. Evidence: plans/round-96.md A1.
  Captured-by: none. Fix: r97 RERAISE-aware rule plus the two shapes in the table; shown able to fail (r96 prints 1 where r95 prints 70).
- **M2 — "cannot block" and "momentarily" written from intent.** Evidence: R96Sentinel F-1, F-2 (E10 stack, E5/E9). Captured-by: none before the wave. Fix: A2/A3.
- **M3 — a kill sentence written without measuring the kill's reach.** Evidence: R96Sentinel F-4 (E6c); R96Scribe reapcheck B/C. Captured-by: none. Fix: A4; shown able to fail (reapcheck B).
- **M4 — a counted quantity a cheap edit reaches.** Evidence: R96Critic (2). Captured-by: the critic seat. Fix: A7.
- **M5 — a receipt's number attributed to the wrong instrument.** Evidence: R96ReviewerShapes §3. Captured-by: the reviewer seat. Fix: A9.
- Misroots: none. Fleet-root sweep (`git status --porcelain`, `.ufo/` newer than the r95 close) shows only the
  orchestrator's `.scratch/` and driver logs, which are excluded; no seat file landed at the fleet root.

## Open L0 questions

Appended to `.ufo/l0-questions.md` (see the commit for this report):
1. `souji | round-96 | C1 verdict: the r96 EH clear is a trade (t1/t4 70→0; module-level finally and re-raise 70→1). Admit as harmed-not-admitted (current) or require the r97 fix before any calibration claim on the EH leg?`
2. `souji | round-96 | Reaping authority: may the lane kill its own arm grandchildren by identity (per-arm absolute fixture path) at act time? PROVINCE F5 holds reaping; the L1 killed two own-run orphans by PID this round (2085368, 2254969).`
3. `souji | round-96 | Host signal: S12 arms received an unattributed SIGTERM in three first runs (after arms, r95 control, MutC2 baseline). Is a host-wide signal sweep running during seat batches?`

Stale-lane: no (respawn-per-round driver; no other mission of this lane is open).
