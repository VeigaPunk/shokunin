# souji — round 1 (dry-run census)

Lane HEAD at report time: `ab7f2f7` (work commits `652b6f8` + `ab7f2f7`, both
souji-shokunin identity). Dispatch: batch 1 of 64 on opencode-go never
spawned and was user-interrupted; batch 2 of 64 on **opencode-go-6**
(completed 788s). Two batches for one round is a deviation from "exactly
ONE batched AgentSwarm" caused by the lane failure + interruption, recorded
here for the closure notes.

## Work performed

Claims: **C1 coverage** — dry-run census classifying every mint demand
instance; **C2 calibration** — zero false-SAFE in the admitted table under
non-author spot-check. Both verified; no axis harmed.

- 64/64 seat fragments landed (`souji-shokunin/census/round-1/seat-01..64.json`), 246 evidence rows (`census.tsv`, `census-summary.json`).
- Parent re-derivation loop: all 109 b2f2efa files have introducing commits that are ancestors of `origin/master` → 0 NOTPUSHED (`git show --name-only --format='' b2f2efa` + per-file `git log --diff-filter=A` + `git merge-base --is-ancestor <sha> origin/master`).
- 24 worktrees re-derived: 19 lore + 2 gd2d detached (r80-baseline, r81-frozen) are dir-absent with unique commits = 0 → metadata-prune candidates; 3 gd2d named-branch registrations (wt-r98/99/100) each hold 1 unpushed commit → NOT-SAFE.
- kotodama set NOT-SAFE: 37 unpushed commits, 17 dirty paths, `.scratch` grew 553M (11:45) → 1.9G (12:35) under live round-22 writes; 715 live references (blind seat S60).
- Critic seat S63 attacked 6/6 author SAFEs and overturned all: 5 launch-*.json stale receipts were falsified by self-polluted reference sweeps (hits only in the census's own fragments — defect D3); seat-21's SAFE(pushed) on /tmp/r87-C5 conflicted with its own unreachable evidence.
- Blind spot seats S54–S61 re-derived 21 targets independently (all NOT-SAFE); their disagreement with the final SAFE(pushed) rows traces to defect D1, not missed evidence.

## Landed changes

- `census/round-1/` fragments + `census.tsv` + `census-summary.json` — LOG.md round-1 entry — commit `652b6f8`.
- `SCORECARD.md` (coverage 7 / calibration 5 with counting commands) — commit `ab7f2f7`.
- `corpus/lessons/round-1.md` — gate record + defects D1–D3 (D1: fleet default branch is `origin/master`, resolve it, never hardcode `origin/main`; D2: unreachable→NOT-SAFE misfires on worktree metadata, absent dir is the prune condition; D3: sweeps must exclude `souji-shokunin/census/**`).
- `LOG.md` append-only entry for round 1 (above).

## Before → after measurements

- C1 coverage: before 4 known evidence instances → after 246 rows covering 109/109 b2f2efa files + 24/24 worktrees + 18 lane recon rows + kotodama set + 6 fleet dirs. Counting: `python3 -c "import csv;print(sum(1 for _ in csv.DictReader(open('census/round-1/census.tsv'),delimiter='\t')))"` → 246, measured against `652b6f8`.
- C2 calibration: before — no measurement existed → after — author first-pass SAFE precision 0/6, non-author catch 6/6 (critic) + parent re-derivation; final table 0 false-SAFE among 132 unique SAFE proposals (109 pushed + 21 metadata-prune + 2 root strays). Counting: `census-summary.json` keys `author_stage` and `final_verdicts`, measured against `652b6f8`.
- Cross-domain observation (reported, not absorbed): game-dev-2d-shokunin branches wt-r98/99/100 carry 1 unpushed commit each — those 3 worktree registrations stay NOT-SAFE until that lane pushes; routed to game-dev-2d/operator.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists with cited sources — `souji-shokunin/SKILL.md` (seed level, exercised this round).
- [~] End-to-end domain task executed and logged — the round-1 census, `LOG.md` round-1 entry.
- [~] Instructions executable by an agent without oral context — 64 zero-context seats ran the census from the template alone.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; game-dev-2d observation routed, kotodama left untouched.
