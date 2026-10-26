# kama round 46 report

author: kama L1 (agent `KamaR46`)
date: 2026-10-26
attempt: 1 (watchdog: `2026-10-26T16:39:29-03:00 launch kama round=46 pgid=368305 driver=hyaku-inline attempt=1`; no `lane-dead-no-report kama round=46` line, so nothing was inherited; the lane was clean at launch: `jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`)
base: `0163fea2dab3f282ebd70c71da9ab5de4cedf733` (round-45 verifier spot-check; lane remote tip at launch)
lane tip: `e8fa87ef19ec5eb28f5fd9701a0a42da45bd688d` (`git ls-remote origin refs/heads/master` prints it)
measured commit: `4340cf2f68ebbfb618086e16825c2e7effd7fa58`. Re-measured at `4991ecc2` and `42ea1204`, with the same claim values.
Stale-lane: progressing. The driver respawns the lane each round, and no other mission of this lane is open.

**Round shape:** one v2 wave, `kama-r46-w1`, with 65 seats. It validated under policy v2 with exit 0 (`.ufo/waves/round-46/w1/dispatch.json`: `spawn 65`).
- Role mix: executor 16, critic 17, scribe 11, reviewer 7, scout 5, mutation-tester 3, connector 3, sentinel 1, revenger 1, simplifier 1.
- m_flash roles: 47/65. Attack roles (reviewer, critic, mutation-tester): 27/65.
- Ready file written 16:55:50 -03; WAVE-DONE received.
- `python3 tools/seat-yield.py .ufo/waves/round-46/w1 --expect-reports 65` → `seats=65 status=unknown:65 reports=65 missing=0`, exit 0. The results JSON carries no status field, so the status shows as `unknown`.
- Dead seats: 0. Residual call: none. **Round total: 65 seats.**
- Planner seat: held by the L1, because the validator rejects `planner`. The planning data-walk rode on scouts U1DiffCtx/U1DiffModels and connector N2Couple.

## Work performed

The round declared two claims and froze them before any data at `5790944350ae41bfe2ce50934bba59e086e747f4` (`.ufo/waves/round-46/preregistration.json`):
- **C1, freshness 8→8, sourced on S486 and S487.** The 91 on-release llama.cpp registry rows are re-verified at release b11906 (`4d71b42f`), 17 commits past b11889. Every reworded, drifted or removed verdict must carry a machine witness, and b11906 is registered as a source. Counter: `tools/round46-release-recheck-audit.py`.
- **C2, calibration 7→7, capability acquisition `append-only-audit`.** This is considerthese/2026-10-26.md proposal 1. The lane's append-only self-description is set against its git history. The tool must match an independent recomputation on a random fixture and on the lane's own history, and must be entered in the capability table. Counter: `tools/round46-append-audit-check.py`. Calibration, depth and adjacency are tied as the lowest axes at 7.

Work items:

- **Protocol load:** `skill://godspeed`, `skill://shokunin`, the round prompt, fleet `AXES.md` and `MISSION.md`. From the lane: SCORECARD head and §Planned (round 46), `SHONEN.md`, the round-45 report, `corpus/lessons/round-45-verifier-spotcheck.md` and `considerthese/2026-10-26.md`.
- **Freeze `57909443`:** both counters, preregistration, controls and start census.
  - Controls (all `met=False`, `.ufo/waves/round-46/controls/*.out`):
    - C1 carry-forward of the b11889 ledger: `valid=71 unverified=20`.
    - C1 mass `holds-reworded` with boilerplate witnesses: `valid=6`.
    - C2 tool that replays events fixed at build time: `fixture=0`.
    - C2 event finder without restoration: `fixture=0 lane=0`.
  - Freeze-time check (round-45 D2, KQ64): `.ufo/waves/round-46/freeze/prereg-time-check.out` → `RESULT pass`, `exit=0`.
- **Tool `4a2a4d55`:** `tools/append-only-audit.py`, with a 10-case selftest (`AOA_SELFTEST pass=10 fail=0`). It landed after the freeze and before the wave, so seats could attack it.
- **Wave spec `96d32918`:** `build_spec.py`, `spec.json`, `dispatch.json` and the C1 fragment checker `.ufo/waves/round-46/tools/check-fragment.py`.
- **C1 ledger `7d057345`:** `registry/release-recheck-b11906.tsv`, 91 rows: 6 `unchanged-file`, 81 `holds`, 4 `holds-reworded`, 0 drifted, 0 removed.
  - 70 rows were carried mechanically: their file is byte-identical between the releases and the counter re-derives them from bytes.
  - S479 was carried with its blob re-derived (one comment line moved).
  - 20 rows were read. Each was built by an executor (X1R01–X1R10) and re-judged independently by a critic (K1R01–K1R10). 19/20 verdicts were equal.
  - S121 is filed as `holds-reworded` on its full anchored range, following critic K1R07 over the builder (lesson §Gate).
  - Also landed: rows S486 (b11906 binary and tag identity) and S487 (three b11906 live receipts, 11/11 checks each). Seat X1Replica replicated the receipts on its own install.
  - SOURCES §Round-46 release re-verification.
  - Evidence under `.ufo/waves/round-46/c1/`: release JSON, ls-remote, commit list, diffstat, live install and model-fetch records.
- **Integration `4340cf2f`:**
  - Wave output (65 reports under `.ufo/waves/round-46/w1/out/`).
  - SCORECARD: the capability row, a canonical capability list as of round 46, §Round 46 with "What `met=True` does not show", and a head re-anchor (banner round 46, latest closure round 45, spot-check count 32, depth and coverage hashes).
  - PROVINCE instrument clause.
  - SKILL.md §Round-46 instrument registry (gate `registered 38 unregistered 0 defective 0`).
  - Lesson `corpus/lessons/round-46.md`, KQ66–KQ68, README frontier disposition, LOG §Round 46.
- **Fixes `4991ecc2` and `42ea1204`:** three harms that the measured commit introduced and the tip regression run caught. All are corrected and recorded as lesson Mistakes rows:
  - The round-43 registry counter read `spot=1`.
  - The `digest-ledger` unknown count rose 2→5 and the `hexrun-census` unknown count rose 21→26. Five digest rows and five hexrun rows with evidence are appended (`.ufo/waves/round-46/hexrun-evidence/`).
  - The measured-results block had been inserted inside the head pointer sentence, a repeat of round-43 D1.
  - Final receipts are in `e8fa87ef`.
- **Routed round-45 closure items:**
  - D1 (claim-outcome reader) was deferred by the preregistration. Instead, the hand-read KQ65 sample is committed as wave evidence for a later reader: 411 lines labelled by S8Sample1–3 and 142 independent lines by R8Sample. Where they label the same line they agree 8/8 (`.ufo/waves/round-46/measured/sample-agree.out`). No reader was written.
  - D2 is closed by the freeze check above.
  - D3: the model re-fetch URL and sha256 are recorded in `.ufo/waves/round-46/c1/live/model-fetch.txt`, and a proposed `--model-url` patch with a passing selftest is in `.ufo/waves/round-46/w1/out/X9D3/`.
- **Tooling:** llama.cpp b11906, the official Linux x64 release binary. Channel: GitHub release asset `llama-b11906-bin-ubuntu-x64.tar.gz`, sha256 `064ade62…eef3`, equal to the release digest. Installed into `/home/vgpnk/.local/opt/llama-b11906` by seat X1Live for the live run. No pacman. No other installs (seat reports state none).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → empty (`.ufo/waves/round-46/measured/misroot-sweep.out`). Scratch `/fast/scratch/hyaku/kama-r46` was removed.

## Landed changes

Every hash below is a `landed` line from `jj-lane.sh`, and each maps to `LOG.md` §Round 46.

| Change | Lane commit |
|---|---|
| Freeze: both counters, preregistration, controls, start census | `5790944350ae41bfe2ce50934bba59e086e747f4` |
| `tools/append-only-audit.py`, prereg-time-check receipt | `4a2a4d55d09dfacf83dc62d1b3fddae5f6d2a050` |
| Wave spec, dispatch, fragment checker | `96d329186e777080c03ac89fdd2366714d504dc3` |
| C1 ledger, S486/S487, SOURCES §Round-46, c1 evidence | `7d0573455c2a19fffcb439fbca8180797699cc9c` |
| Wave integration, capability row, SKILL registry, SCORECARD §Round 46, lesson, KQ66–68, README, LOG (measured commit) | `4340cf2f68ebbfb618086e16825c2e7effd7fa58` |
| Measured results, digest/hexrun ledger rows, calibration-row fix, end census | `4991ecc28efa1378f394d267dd67ab0a11c1b976` |
| Pointer-sentence repair, lesson row | `42ea1204aef3aaa847f64112cbec1dc6eafb1ff9` |
| Final tip receipts, misroot sweep | `e8fa87ef19ec5eb28f5fd9701a0a42da45bd688d` |

## Before → after measurements

- **C1 freshness 8→8: met.**
  - Command: `python3 tools/round46-release-recheck-audit.py --repo <fresh clone> --tip <commit> --upstream <llama.cpp clone>`.
  - Base `0163fea2`: `unverified=91 section=0 newrow=0 met=False`, exit 1 (`.ufo/waves/round-46/controls/base.c1.out`).
  - Measured `4340cf2f`: `pop=91 rows=91 valid=91 unverified=0 unchanged=6 holds=81 reworded=4 drifted=0 removed=0 flags_missing=0 section=1 newrow=1 met=True`, exit 0 (`.ufo/waves/round-46/measured/c1-after.out`). The same result holds at `4991ecc2` (`c1-fix.out`) and `42ea1204` (`c1-final.out`).
  - What this does not show:
    - Holds is a text-equality check. A two-second relocation script greens all 91 rows (K1Cheat); the preregistration names relocation as the verification itself.
    - The witnesses of the three `server.cpp` reworded rows could be auto-picked.
    - Critics showed range choices the counter accepts for weaker verdicts.
    - V1Code found defects F1–F4 in the checker and counter.
  - These are listed in SCORECARD §Round 46 and routed to round 47.
- **C2 calibration 7→7 (capability): met on the frozen counter.**
  - Command: `python3 tools/round46-append-audit-check.py --repo <fresh clone> --tip <commit> --scratch <dir>`.
  - Base: `selftest=0 fixture=0 lane=0 table=0 met=False`, exit 1 (`controls/base.c2.out`).
  - Measured `4340cf2f`: `selftest=1 fixture=1 lane=1 table=1 lane_events=5 lane_unrestored=0 lane_partial=2 met=True`, exit 0 (`measured/c2-after.out`). The same result holds at `4991ecc2` and `42ea1204`.
  - What this does not show:
    - The counter's "independent" recomputation uses the same definition as the tool. Both drop deleted lines that begin with `--` (K2Hist): on the lane the counts are low by 4 and 2 with no status change, and a 21-line fixture deletion reads as 0 events.
    - X2Fixture found 7 fixtures where the tool and the counter agree and are both wrong.
    - K2Cheat built three non-capabilities that reach `met=True`.
    - Mutant survivors: M2Ctr 12/32, M2Tool 10/39.
    - K2Design: three of the five files are not declared append-only anywhere in the lane.
  - I disclose this; I do not prettify it. The tool stays on the frozen definition, and a v2 with an amendment is planned.
- **Tip regressions** at `42ea1204` (`.ufo/waves/round-46/measured/*-final.out`):
  - round-41 head `mismatches=0 met=True`
  - round-42 self-description `mismatches=0 maxN=46 met=True`
  - round-43 registry `mismatches=0 met=True`
  - gate `registered 38 unregistered 0 defective 0`
  - capability census `listed 10 observed 10 … met True`
  - `digest-ledger` `unknown=0`, exit 0 (base: unknown 2)
  - `hexrun-census` `unknown=21`, exit 1. This equals the base value, which was already red. No new unknowns.
  - pointer check `met=True` (`pointer-final.out`)

## Sources & frontier

- **Census validate** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`):
  - Start: exit **0** (93 W04, 1 W01 S481, 0 E), `.ufo/waves/round-46/census/start.out`.
  - End: exit **0** (93 W04, 1 W01 S481, 0 E), `.ufo/waves/round-46/census/end.out`.
- **Row count** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): **226 → 228**.
- **`census --file`:** tier B 7, C 4 (unchanged); mined 207→209, queued 8, rejected 11.
- **Rows added:** two tier A rows, both mined and opened 2026-10-26:
  - S486: llama.cpp b11906 binary and tag identity. Located quote: `target_commitish` "4d71b42fd87db24b8b7c808c151b713aa4459cfd".
  - S487: own-work b11906 live receipts. Quote: `{"status":"ok"}`.
  - The Gate is in `corpus/lessons/round-46.md`.
- **Rows touched old→new:** none (no status, recheck or used-by change).
- **Frontier advanced:** 91 rows were re-verified at b11906 against b11889. Still frontier:
  - b11907 and later
  - the S013 citation defect (re-pin proposed: ollama `98acec40`)
  - S022 and S002–S004, which hold today (U9Floating)
  - ten off-population llama.cpp rows (K1Pop)
- **Sourced claim:** C1 rests on S486 (counter `newrow=1`).
- **Mistake mined:** the lesson has eight Mistakes rows, each with a fix shown able to fail:
  - four seat-drafted rows (evidence durability, wave-stall blind spot, dead log pointer, undisclosed SCORECARD partials)
  - the spec-prose miscount (71/20 against the true 73/18)
  - the shared-definition blind spot in C2
  - the re-anchor that broke the round-43 reader
  - the pointer-sentence insertion, a repeat of round-43 D1
- **Assimilation:** none. **considerthese:** `considerthese/2026-10-26.md` proposal 1 → C2 (`tools/append-only-audit.py`).

## Trend verdicts

- **expansion: improved.** Capability `append-only-audit` entered the table with a demonstrated run (capability census `listed 10 observed 10`, `cap-final.out`). Read-only on sibling lanes, it finds the truncation class in 14/21 of them (seat N3Fleet, report never absorbed). This is pending closure. The wave's attacks (K2Design) argue that it is a history audit more than a calibration measure.
- **quality: improved.** 91 stale-prone rows were re-verified at a newer release with none failing. Three b11906 live runs passed, plus an independent replication. KQ66–KQ68 were added. `digest-ledger` unknown went 2 → 0. Three integration harms were caught and fixed within the round.
- **discernment: unchanged.** The act is still owed: the outside spot-check of the Gate. Under review: the S486/S487 admits, the S121 critic-over-builder admit and its matching reject of the single-line `holds`, the teardown-duration reject, and the carry-forward reject. Per KQ61, `improved` waits on the outside spot-check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round-46 instrument registry; gate `registered 38 unregistered 0 defective 0` (`.ufo/waves/round-46/measured/gate-final.out`). This is the author's assertion; there is no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → three b11906 live llama.cpp runs (`.ufo/waves/round-46/c1/live/receipt-1.json`…`-3.json`, `LOG.md` §Round 46), plus seat X1Replica's independent two-run replication. A seat is not a non-author mark.
- [~] Instructions executable by an agent without oral context → `tools/append-only-audit.py --selftest` `pass=10 fail=0` (`measured/aoa-selftest.out`). No independent execution review has been done.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` changed only in its instrument clause (`append-only-audit`). The sibling scan N1Overlap and the fleet scan N3Fleet are reported, not absorbed.

Open L0 questions (routed around, none filed this round): `kama | round-35` (MISSION.md axes pair), `kama | round-39` (validator band and planner), `kama | round-41..43` (parked worktree).
