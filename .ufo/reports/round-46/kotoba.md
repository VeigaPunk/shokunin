# kotoba — round 46 (kaika steered round)

Lane commits (branch `kaika/round`, worktree `.tower/worktrees/kaika/kotoba-shokunin`): **`f2f9ee1`** (landing) and **`04192c2`** (landing pin, after-battery). Base `78ee57e`, the merge of the r46 WIP `36ab0d3`. Steer: `.ufo/waves/kaika/steer.md` → kotoba 46, "land r46 if its claims verify on re-measurement, else close it honestly". Collision check: no fleet-root `.ufo/reports/round-46/kotoba.md` existed and no lane LOG entry closed round 46. Precedence: the standing operator rule "No push" and PROTOCOL.md § Invariants (operator-gated artifacts are committed, not pushed) override MISSION.md § Round end's commit-then-push, so nothing was pushed. The integrator commits this report.

## Work performed

Declared claims: the three claims pre-registered in `.ufo/round-46/claims.json`. They stay first under §6.4, which fills the 1–3 cap.
- **C1 — depth (owned, lowest owned axis):** close the scope-file cwd seam.
- **C2 — operability (advisory):** close or bound the live-JSON shadow channels and raw duplicate JSON members.
- **C3 — calibration (advisory):** bound scoped-out reason/evidence/probe-target drift, and reconcile the records.

Campaign items are file-contract conformance work and were not claimed (no score credit).

- Re-measured every claim at the committed bytes: comparator `ccf41c23…` @ `36ab0d3`/`78ee57e`, then landing `778b367e…` @ `f2f9ee1`. The frozen comparator `055d3b9` (`1101213a…`) was the before. Evidence: `.ufo/round-46/evidence/w2/c1/summary.json` (sha256 `8e4b9856…`), `.ufo/round-46/evidence/w2/c2/summary.json` (`ae14fdf0…`), and `.ufo/round-46/evidence/w2/l1-matrix/snapshot2/results.json` (`779c38d5…`, at `ccf41c23`) and `snapshot3/results.json` (`bbe11ad0…`, at landing).
- Found and worked around a measurement race. The scoped-out probe recomputes `$HOME/.omp/agent/sessions`, and about 100 live agents grow that directory every few seconds. Paired runs therefore hit `false blocker` on both comparators (`.ufo/round-46/evidence/w2/l1-matrix/race-fresh2/results.json`; reviewer HIGH-3). All arms were re-measured on a frozen `cp -a` snapshot of the carrier (listing digest `4d715d65…`, recorded at lane `LOG.md:2304`). The snapshot was deleted after measurement because it contained session transcripts. A re-run needs a fresh snapshot, and the recipe is in `corpus/knowledge/harness-independent-round41-census.md` § Round 46 landing.
- Repaired a harm before landing. The reviewer's MED-3 reproduced: a duplicate-member fragment in prose ahead of a valid payload was frozen exit 0 but exit 2 at `ccf41c23`, a new false red. `extract_json` now selects the payload with a plain decode and re-decodes only the selected payload with the unique-member hook (`verifiers/compare_harness_independent.py:233`). Two regression arms were added, and the floors moved in step 328→330 (registry, both tables, docstring). Repro: `.ufo/round-46/evidence/w2/l1-matrix/med3/`.
- Built a canonical-layout measurement harness, `.ufo/round-46/evidence/w2/gates/meas-tree.sh` + `battery.sh`. It makes a shared clone under `/tmp` whose parent symlinks the fleet root, because `../` citations do not resolve from the tower worktree. Before battery: `gates/before-78ee57e/`. After battery: `gates/after-f2f9ee1/`.
- Conformance:
  - `corpus/QUALITY.md`: Q01–Q18, each citing a lesson row.
  - `corpus/lessons/round-46.md`: § Mistakes M1–M19 and § Gate.
  - `corpus/SOURCES.md`: per contract v1.
  - `SHONEN.md`: canonical form.
  - `PROVINCE.md`: § Core (line 8), § Frontier (line 16), § Adjacent (line 23).
  - `corpus/README.md`: § Frontier (line 64) plus 3 index rows.
  - `README.md`: the `**Domain:** >` leak is fixed.
  - `SKILL.md`: one portability-floor paragraph (§ Frontmatter craft) and one Sources pointer.
- L2 swarm: 10 seats in one batched call (planner, connector, executor ×3, sources executor, scribe, scout, reviewer, critic). The first send was refused at the session's 100-job cap and was re-sent whole after the orchestrator's capacity note.
  - Provider exhaustion: `R46ExecC1-2`, `R46ExecC2-2` and `R46ExecC3Gates-2` died with `resource_exhausted` ("Devin … Reached free model rate limit"). Per the orchestrator's route note, C1 and C2 were re-dispatched fresh as `R46ExecC1b` and `R46ExecC2b`. The C3 re-dispatch, `R46ExecC3b`, died on "Codex is at capacity", so the L1 ran C3 and the battery itself.
  - Seat reports: `.ufo/round-46/scouts/w2-reviewer.md`, `w2-critic.md`, `w2-connector.md`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| C1/C2/C3 re-measurement evidence (`.ufo/round-46/evidence/w2/{c1,c2,critic,l1-matrix,gates,sources}`, 1.4 MB) | lane `LOG.md:2300` (Round 46 landing) | `f2f9ee1` |
| `extract_json` selected-payload duplicate check (MED-3 repair) + 2 self-test arms; floors 328→330 in `verifiers/check_assertion_floors.py`, `verifiers/floors-registry.json` | `LOG.md:2300` (C2 bullet) | `f2f9ee1` |
| `verifiers/corpus-baseline.json` re-record 55→58 / 38→40 / 27→29 (`notes.round46_landing`) | `LOG.md:2300` (last bullet) | `f2f9ee1` |
| SCORECARD: round-46 segments prepended to rows depth `:28`, operability `:31`, calibration `:33` (the calibration segment corrects "uncommitted candidate"); planned `:98`/`:100`; move log `:227-229`; saturation `:283` | `LOG.md:2300` | `f2f9ee1` |
| Census entry: appended § Round 46 landing (record reconciliation, dead-recheck correction) | `LOG.md:2300` (C3 bullet) | `f2f9ee1` |
| `corpus/QUALITY.md`, `corpus/lessons/round-46.md`, `corpus/SOURCES.md`, `corpus/README.md`, `SHONEN.md`, `PROVINCE.md`, `README.md`, `SKILL.md` | `LOG.md:2300` (conformance bullet) | `f2f9ee1` |
| Landing pin, after-battery evidence, SKILL `S002` cited by literal id | `LOG.md:2312` | `04192c2` |

## Before → after measurements

All before/after values below were measured on `78ee57e` (comparator `ccf41c23`) → `f2f9ee1` (comparator `778b367e`), against the frozen `055d3b9` comparator `1101213a`.

- **C1 depth — verdict `improved`, score 9 → 9 (held; band 9.5 needs non-author re-verification).**
  - Counting command: `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py`.
  - Planted-CWD relative `--scope-file`:
    - Frozen: exit 0. The receipt attests `3d8500ed…`, but the planted superset that was actually enforced is `886b1393…`.
    - `ccf41c23`: exit 2 `laundering`. `778b367e`: exit 2.
  - Absolute planted control: exit 0, and the receipt digest equals the enforced file.
  - Honest join: exit 0, 24/24 protocol, 20/24 strict, 4 adjudicated, 4 scoped out.
  - Self-test 0/328 at `ccf41c23`; 330 at landing. Floors 9/9 exact.
  - Critic held-out probe P1 (symlinked relative `--cwd`): **survives**.
- **C2 operability — verdict `improved-bounded`, 8.5 → 8.5 (held).**
  - Counting command: `HOME=<snapshot> PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/l1-matrix/r46_l1_matrix.py`. Re-run after landing: same exits.
  - Registered arms, frozen → landing:

    | Arm | Frozen | Landing |
    |---|---:|---:|
    | live mode shadow | 0 | 2 |
    | summary shadow | 0 | 2 |
    | non-string verdict | 0 | 2 |
    | same-id mode duplicate | 0 | 2 |
    | raw duplicate `results` (seat C2b) | 0 | 2 |
    | raw duplicate `re_derived` (seat C2b) | 0 | 2 |
    | nested duplicate member | 0 | 2 |

  - MED-3 prose arm: frozen 0 → `ccf41c23` 2 (harm) → landing 0. A duplicate inside the selected payload is still exit 2.
  - Surviving same-class doors, all pre-existing:
    - Mirror opt-out (positive mode, independent value 3→1002, all four mirror maps removed): exit 0 on both comparators (R2; reviewer HIGH-1).
    - A row with no `verdict` reads PASS (MED-1).
    - `NaN` and case-variant shadow keys pass (critic P2/P3).
  - Under the lane's own Q01 this is not "closed".
- **C3 calibration — verdict `improved` as registered, class `improved-bounded`, 8.5 → 8.5 (held).**
  - Counting command: same matrix.
  - Arms, frozen → landing:

    | Arm | Frozen | Landing | Class |
    |---|---:|---:|---|
    | reason + evidence drift | 0 | 2 | `scope reason drift`, `scope evidence drift` |
    | committed reason, redirected target | 0 | 2 | `scope probe target drift` |
    | probe-copy shadow | 0 | 2 | `scope probe channel split` |
    | fabricated observable (pre-existing reject) | 2 | 2 | — |
    | honest control | 0 | 0 | 24/24 |

  - Record reconciliation, counted with `grep -n 'committed at `36ab0d3`' SCORECARD.md corpus/knowledge/harness-independent-round41-census.md`: 0 → 2 appended corrections. The original "uncommitted candidate" wording stays as history (append-only).
  - Surviving shapes: record-level `kind` drift exits 0 on both comparators (critic P5). Committed scope-outs stay payload-selectable when the probe matches (reviewer HIGH-2, r39 design).
- **No axis harmed (gate battery, `battery.sh` @ `78ee57e` → `f2f9ee1`):**

  | Gate | `78ee57e` | `f2f9ee1` |
  |---|---|---|
  | checklist | 9/10 (`LOG.md:2111`) | 9/10 (same failure) |
  | corpus integrity | 9/9 | 9/9 |
  | corpus independent | exit 0 | exit 0 |
  | surfaces | 5/7 (stdout `8432070a…`) | 5/7, byte-identical |
  | pins | 1/3 (stdout `16e71a19…`) | 1/3, byte-identical |
  | floors | 9/9 at `…/328/150` | 9/9 at `…/330/150` |

- **Admission (self-assessed; the operator rules):** C1 verifies. C2 and C3 verify their registered arms, but each has surviving same-class doors. By lane precedent (r45) and Q01, that is `improved-bounded`, not a full verify. No axis was harmed at landing. Scores did not move.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `.ufo/round-46/scouts/B2.md` (lane-run inventory)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/cold-run-round11.md`
- `[~]` Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (only non-author run; B1/B2 fixed r13, not re-run)
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` § Adjacent, `.ufo/round-46/scouts/w2-connector.md`

`SHONEN.md` was regenerated in canonical form (50 → 12 lines). The scout's audit confirmed the seed matches the template byte-for-byte and that each box has exactly one evidence line.

## Sources & frontier

- **SOURCES rows:** 0 → 11. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` on `f2f9ee1`.
  - By tier: A=10 (8 external spec/docs, 2 own-work), C=1.
  - Status: mined=4 (S001, S002, S003, S008 → `SKILL.md`), queued=6, rejected=1 (S011, the agentman tutorial: it contradicts the client guide S002; the flip is recorded).
  - Census result: malformed 0, duplicate ids none, enum/tier-inflation none, mined used-by missing none.
- **Rows touched old→new:** S001, S002, S003 and S008 went `queued`→`mined` with used-by `—`→`SKILL.md`; the change is logged in the lesson's § Gate.
- **Pre-landing corrections:** S010 originally claimed "--json exit 0" and is corrected to exit 1. S011's recheck went from `none` to `180d`.
- **L1 re-open:** the lane L1, not a non-author, re-opened S003, S006 and S007; all 3 quotes are present.
- **Timestamp defect:** the fetch log labels local time with `Z`; this is disclosed in the lesson.
- **Frontier:** `PROVINCE.md` § Frontier and `corpus/README.md` § Frontier went from 0 to 6 areas. No frontier ground moved into core this round.

## Mistakes

- **Classes mined:** 19 (`corpus/lessons/round-46.md` § Mistakes). Most come from STATE §4, re-verified by the scribe seat.
- **New at landing:**
  - M17: a fix silently narrows accepted input (false red).
  - M18: a seat reports a run result it did not observe.
  - M19: measuring against a carrier that live agents write.
- **Criteria added:** Q01–Q18 in the new `corpus/QUALITY.md`, each grounded in a lesson row. Q18 comes from M17.

## Trend verdicts

- **Expansion: `unchanged`.** No `knowledge/` entry was admitted, because the claim cap was full. Registry rows are not expansion (contract rule 4).
- **Quality: `unchanged`.** The census entry was re-verified at landing and its dead `recheck:` was marked by an appended correction. It was not re-derived, so it is no longer left stale but it is not stronger either.
- **Discernment: `unchanged`, pending.** A bar now exists (Q01–Q18), but no non-author spot-check has run. If the orchestrator's spot-check of ≥1 admit (S003) and ≥1 reject (S011) agrees, this becomes `improved`.

## L0 questions

- kotoba | round-46 | Does AXES.md's "lowest non-retired axis" range over advisory axes? Under the all-axes reading, freshness and adjacency (8.0) are the lowest, not depth (9); C1 met only the owned-only reading the lane declared at SCORECARD § Saturation. r47's C1 is freshness, so it meets both readings.
- kotoba | round-46 | Can a lane amend an append-only LOG citation that later goes dead (`LOG.md:2111` → never-committed runner)? The checklist gate stays red on it forever. Options: a gate erratum ledger, or accepting it as permanent.

## Integrator notes

- **Fleet-root strays.** Through the broken-`cd` hazard, the reviewer seat `W2RoundKotoba.R46Reviewer-2` wrote 28 files into the fleet root: `ind_mode.json`, `live_*.json` (9), `err.*.txt` (9), `out.*.json` (9). They were reported to Main and the lane did not touch them; at L1 check time they appeared to be already cleaned. The `live_*.json` count is 9 by the seat's own list.
- **Root ledger clobber.** The fleet-root `LOG.md`/`SCORECARD.md` still hold kotoba bytes. W2RoundProtocol attributes them to kotoba commit `b7470d7`, not `c8e233d`.
- **Report location.** Lane reports for rounds 20–45 live only in the lane repo. Bare `.ufo/reports/round-45/kotoba.md` pointers resolve against the fleet root and read dead; the lesson now uses host-absolute paths.
- **Evidence bloat** (M15/Q11) carried: `.ufo/round-46/` stays 52 MB / 8050+ tracked files. This round added 1.4 MB. Pruning was not done (never delete knowledge without an operator ruling).
- **Harness.** The tower worktree location breaks `../` citations; measure in a canonical-layout clone (`meas-tree.sh`). The broken `cd` alias (`__fnmcd` missing) also aborted one of the L1's own subshell commands; this is noted for kumitate/mori (adjacent).
