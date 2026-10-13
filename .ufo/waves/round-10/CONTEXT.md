# Round-10 wave context (aggregator lane, refresh 8) — shared seat contract

Axis-move this round: **corpus review** — make the `CORPUS.md` rule-10 verdicts non-author
re-derivable end to end. Three parts, from `SCORECARD.md` §Planned (round 10):

- **A** give `corpus-gate.mjs` a legal registry home (`D-127` / proposal **P-v**) or record the
  reasoned rejection;
- **B** close the r4 heuristic's declared false-positive classes (round 9: 246 findings, three named
  classes incl. the rule-4/rule-9 collision `D-141`) until the count is defensible as violations;
- **C** re-run the gate at each lane's *next landed revision* and report movement per rule.

Falsifiers (do not trip them): the gate is called conformant while unregistrable; the r4 cell is
restated without its FP classes; a verdict that does not name its revision.

## Host facts (L1-measured, 2026-09-29T01:44:38Z = 2026-09-28T22:44:38-03:00)

Main repo `/home/vgpnk/projects/shokunin`, HEAD `a2cac72`, remote `origin` = `VeigaPunk/shokunin`.

| child repo | live HEAD | dirty files | round-9 pinned rev(s) (`frozen` keys) |
|---|---|---:|---|
| kasegi-shokunin | `b021dc9` | 1 | `b7180b0` |
| kengaku-shokunin | `e171cdf` | 4 | `f09ff1f` |
| kake-shokunin | `4214101` | 0 | `a209441`, `4c9a985` |
| kumitate-shokunin | `637d181` | 6 | `7a099b2` |
| kotoba-shokunin | `0f658ff` | 11 | `63ceba7` |
| kagi-shokunin | `2486643` | 6 | `4b8c018`, `4391b3b` |

Dirty counts move while the fleet runs: stamp every measurement with the revision **and** the dirty
count you observed (`P-s`: an audit cell's identity is the revision it measured).

The round-9 gate (read-only, do not edit it):

```
node .ufo/waves/round-9/corpus-gate.mjs --selftest            # 12/12 PASS, exit 0
node .ufo/waves/round-9/corpus-gate.mjs --all [--round 10] [--json]
node .ufo/waves/round-9/corpus-gate.mjs --snapshot <repo-dir> <commit>
node .ufo/waves/round-9/corpus-gate.mjs --registry
sha256 68939d0c70b6dc5ee9e2667b…  corpus-gate.mjs
sha256 9af28e2e00f8f80256856765…  corpus-gate.expected.json
```

Exit map `0 clean / 1 failed / 2 could-not-evaluate / 3 failed (frozen drift)`, precedence `2>3>1>0`.
Checks implemented: `r2 r4 r7 r8 r10 shonen`; declared **not-evaluated**: `r1 r3 r5 r6 r9 box-3
shonen-semantics` (reasons in the gate header lines 65–91).

L1 baseline, `--all` over the live trees at the stamp above:

| repo | rev | dirty | exit | findings | rules |
|---|---|---:|---:|---:|---|
| kasegi | `b021dc9` | 1 | 1 | 56 | r2,r4,r8,r10 |
| kengaku | `e171cdf` | 4 | 1 | 30 | r4,r8,r10,shonen |
| kake | `4214101` | 0 | 1 | 37 | r4,r8,r10 |
| kumitate | `637d181` | 6 | 1 | 46 | r2,r4,r8,r10 |
| kotoba | `0f658ff` | 11 | 1 | 83 | r4,r8,r10,shonen |
| kagi | `2486643` | 6 | 1 | 58 | r2,r4,r8,r10,shonen |

`--round 9` (round-9 selector, i.e. before the round-10 lessons exist) gives 304 findings:
r2 12, **r4 264**, r8 14, shonen 14. `--round 10` gives 310 (the six `r10` findings appear).

## Seat write scope — hard rule

Write **only** your own seat file under `.ufo/waves/round-10/` (`seats/<name>.md`, or the scratch /
lessons / mutants subdirs when your task names them). NEVER touch: `PROTOCOL.md`, `MISSION.md`,
`AXES.md`, `CORPUS.md`, `ROADMAP.md`, `MANIFEST.json`, `SCORECARD.md`, `LOG.md`, `scripts/`,
`.ufo/state/**`, `.ufo/prompts/**`, `.ufo/reports/**`, `.ufo/waves/round-{1,9,11,12,13}/**`, or any
file inside the six child repos. NEVER `git add`/`commit`/`push`/`checkout`/`restore`/`stash`/`clean`,
never mutate a child repo, never run a sibling gate that writes (read-only sibling gates are allowed
and are named in your task). The L1 owns every commit. `git archive`/`git show`/`git log`/`ls-files`
into `/tmp` is fine.

## Evidence discipline (your output is graded on this)

- Every number carries the command that produced it **and** the revision/tree it was measured
  against. Absence claims carry the sweep that produced the absence. Quotes carry `file:line`.
- Cross-repo pointers are qualified: `shokunin:<path>` for main-repo paths, `<repo>:<path>` for a
  child repo (`D-128` forward fix — 138 unqualified citations were this lane's own defect).
- No placeholders, no `TODO`, no `{{…}}`. If a measurement cannot be made, write
  `could-not-evaluate` and the reason.
- No credential material: no secret values, no live `op://` item paths (schematic form only, and
  say it is schematic).
- Say what you ran, not what should happen. A cell you did not execute is marked `not-run`.
