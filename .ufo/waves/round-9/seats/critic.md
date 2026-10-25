# Critic seat — round 9 corpus-review plan

**Stamp.** Main HEAD `62fdfbe` (`git log -1 --format='%h %cI'` → `62fdfbe 2026-09-28T21:46:25-03:00`). Child cells were pinned to the revisions shown below; HEADs moved during the wave, so moving-worktree bytes are not treated as landed evidence. This is author-side evidence for the aggregator lane: `PROTOCOL.md:34-38` says a subagent dispatched by a lane is still that lane.

## Falsification attempts

### A1 — axis selection / plan switch: **REPAIRED-BY-AMENDMENT**

**Claim attacked:** corpus review is the justified next axis, despite the round-8 plan queuing cross-lane quality.

**Deciding evidence:** `grep -n 'corpus review\|### Planned\|Owed from round 8\|### Retired' SCORECARD.md` observed: line 207 says corpus review `8 → 8` with rule-10 verdicts owed; lines 226-231 still queue round 9 as **cross-lane quality**, while lines 232-233 separately say the corpus verdicts are owed; lines 240-242 say cross-lane quality has residuals and corpus review owes a verdict re-emission. Round-8 `grep -n '## Next\|Falsified if a provisional\|Owed from round 8' .ufo/reports/round-8/aggregator.md` observed `## Next` at 246 and the explicit cross-lane move at 252-253.

The tie-break is defensible only as “the sole 8-axis with an unpaid aggregator-owned rule-10 duty; cross-lane SHONEN marks are lane-owned.” It is not recorded in the committed SCORECARD plan, and the gate deliverable could make the choice self-serving. **Amendment:** “Round 9 supersedes SCORECARD.md:226-231 because rule 10 is the only stale aggregator-owned obligation; retain the cross-lane landed-HEAD reruns as required inputs, and record this reason in the round-9 report and move log.”

### A2 — self-written gate / V-metric circularity: **REPAIRED-BY-AMENDMENT**

**Claim attacked:** “verdicts re-derivable by a committed gate” measures corpus quality rather than merely proving the lane’s own tool works.

**Deciding evidence:** `awk 'NR>=357 && NR<=370 {printf "%d\\t%s\\n",NR,$0}' PROTOCOL.md` observed `357-361` requiring isolated self-test with independent committed finding-id, `362-366` stating “Self-test green is capability, not a measurement,” requiring a committed input snapshot/expected verdict for mutable fleet artifacts and a cited revision, and `367-370` requiring registry rows in each lane’s `SKILL.md`.

A gate over mutable child corpora plus a same-lane expected output is circular unless the frozen input snapshot and expected verdict are committed independently of the live rerun. **Amendment:** V counts only when the gate has (1) declared exit map, (2) isolated fixture self-test asserting exit and finding-id, (3) committed frozen corpus snapshot plus expected verdict, and (4) a live run naming the exact landed revision; self-test-only green is explicitly zero measurement credit. The round’s own verdict remains author-side and must not be called non-author.

### A3 — kake/kagi landed HEAD versus lane worktree: **REPAIRED-BY-AMENDMENT**

**Claim attacked:** provisional box-3 verdicts can simply be firmed/broken at “the lane’s landed HEAD” while the lane is live and dirty.

**Deciding evidence (fresh drift check):** `git -C <repo> log -1 ...; git -C <repo> status --porcelain | wc -l` observed kake `a209441`, dirty `0`; kagi first observed `4391b3b`, dirty `21`, then moved to clean lane commit `4b8c018`. The earlier `4391b3b` was explicitly an aggregator-identity commit; its dirty corpus bytes were not part of that revision. `PROTOCOL.md:362-366` says a verdict names its revision and a moving worktree is not comparable to a cited commit.

Thus a pinned landed-HEAD verdict can be firm only for the committed tree; it cannot silently grade kagi’s prior worktree or any later worktree. **Amendment:** stamp every cell with the exact `rev-parse --short HEAD` used; report worktree-only deltas as `provisional`; if decisive text is absent at HEAD, use a third outcome `stays-provisional` rather than forcing firm/broken. The L1 amendment requiring immediate HEAD/status re-check repairs the moving-target defect.

### A4 — registry impossibility for main-repo aggregator gate: **REPAIRED-BY-AMENDMENT**

**Claim attacked:** a `corpus-gate.mjs` can conform to §Gate standard when registry rows must live in `SKILL.md`, but main repo has no `SKILL.md`.

**Deciding evidence:** `ls SKILL.md` observed “No such file or directory”; `awk 'NR>=367 && NR<=370 {…}' PROTOCOL.md` observed “rows live in each lane’s `SKILL.md`.” The protocol lane’s precedent is `git log -1 --format='%h %an %s' -- .ufo/waves/round-12/closure-check.py` → `cab25dd protocol-shokunin round-12: third closure pass … wave artifacts committed: closure-check.py`; `git ls-files .ufo/waves/round-12/closure-check.py` confirmed it is durable. `.ufo/reports/round-12/protocol.md` registry sweep found 13 mentions and line 170 says closure grades no gate conformant until a row exists in lane `SKILL.md`, while no such main-repo file exists.

This is a protocol defect of D-120 class, not a reason to abandon the gate’s measurable portions. **Amendment:** build the gate with all executable §Gate evidence, route a D-row for the missing main-repo registry home, and mark the gate `non-conformant/unregistrable` until the integrator amends the registry clause or supplies a main-repo lane registry file. Do not count the gate as conformant merely because its self-test passes.

### A5 — write scope and wave-path durability: **SURVIVES**

**Claim attacked:** `.ufo/waves/round-9/**` is outside aggregator scope or a gate script there is junk.

**Deciding evidence:** `awk 'NR>=424 && NR<=439 {…}' PROTOCOL.md` observed lines 424-433 limiting ordinary lane writes, then lines 434-435 explicitly state “`.ufo/reports/` and `.ufo/waves/` are the round’s written evidence, committed with the round’s integration commit.” `git ls-files .ufo/waves/round-12/closure-check.py` observed the committed protocol gate precedent. `git ls-files .ufo/waves/round-12 .ufo/waves/round-11 .ufo/waves/round-8 | wc -l` observed `127` tracked wave artifacts.

Therefore this seat’s evidence file and a round-scoped gate artifact are in the wave evidence scope. The gate should still name its durable wave path and not pretend that evidence placement creates a permanent lane registry; the registry defect remains A4.

### A6 — 6/6 metric with missing province root / could-not-evaluate: **SURVIVES, with amendment**

**Claim attacked:** a vanished `~/Projects/bounties` root makes a kasegi verdict unevaluable, so “6/6 verdicts” inflates coverage.

**Deciding evidence:** `ls -d ~/Projects/bounties 2>&1; echo "exit=$?"` observed “No such file or directory” and exit 2. At landed kasegi `b7180b0`, `git -C kasegi-shokunin grep -c 'Projects/bounties' b7180b0 -- corpus/` observed 27 files and 45 matching lines; a sample `~/Projects/bounties/ops/claim-check.mjs` resolved `exists: False`. `CORPUS.md:55` says each review emits `conformant` or `not conformant` per repo.

The missing root is an observable failed citation/sweep, so kasegi can receive a real `not conformant` verdict naming rule and command; §Gate’s `could-not-evaluate` class is not a third CORPUS rule-10 verdict. **Amendment:** count 6/6 only when each cell is literal `conformant` or `not conformant`; a gate-level `could-not-evaluate` is separately reported and does not count as coverage.

### A7 — literal rule-8 conflict: **REPAIRED-BY-AMENDMENT**

**Claim attacked:** inherited “rule 8 clean” judgments are safe, and the plan’s 6/6 metric is fully specified.

**Deciding evidence:** `git -C <repo> grep -c 'op://' <HEAD> -- corpus/`-style landed scans (with the HEADs observed in this wave) produced line-count totals 2/1/2/1/3 for kasegi/kengaku/kake/kumitate/kotoba. Kagi drifted: the old `4391b3b` scan produced 53 matching lines while the later `4b8c018` scan was not comparable to it; the authoritative L1 sweep reported 55 at `4391b3b` and later content changed. The discrepancy itself proves the revision must be stamped. The L1’s literal-text instruction requires classifying every hit without printing refs; no secret value was printed.

`CORPUS.md:43-46` literally bans vault ref paths, while round-6’s inherited “schematic placeholders are clean” interpretation is not the text. **Amendment:** every rule-8 cell must list file/line/class (`real-vault-path` → FAIL; schematic placeholder → `FAIL-literal / PASS-intent`) at the pinned landed revision, and route the rule-text ambiguity to operator/integrator. Never count a legacy “clean” ruling without this literal sweep.

## Headline

The corpus move is defensible as debt-first only after recording why it supersedes the committed cross-lane plan; the gate and rule-8 metrics otherwise risk circular/self-authored or inherited measurements, while landed-HEAD pinning and a strict `conformant/not conformant` coverage rule make the move falsifiable.

## Amendments required

1. Record the axis-switch reason and retain cross-lane landed-HEAD reruns as inputs.
2. Define V as frozen-snapshot + exact-revision re-derivability, not self-test green.
3. Permit `stays-provisional` when decisive text is worktree-only.
4. Route main-repo registry absence as D-120-class protocol debt; do not call the gate conformant yet.
5. Count 6/6 only for literal CORPUS rule-10 verdicts; `could-not-evaluate` is not coverage.
6. Grade rule 8 literally at each pinned HEAD and route the text/intent conflict.
