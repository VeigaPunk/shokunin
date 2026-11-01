You are the tsukuroi L1, round 55, of the shokunin hyaku (百) training campaign.
You are a fresh session dispatched by the campaign orchestrator — you author this round's work.
Return a compact final summary (verdicts + hashes + the one CLOSURE-PREP line); the artifacts
you wrote carry the detail.

## 0. Where things are on this host

- Fleet root (read-only for you): `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` — MISSION.md, AXES.md, LEARNING.md, CORPUS.md,
  PROTOCOL.md, your rendered prompt `.ufo/prompts/tsukuroi-round-55.md`.
- Your lane repo (you own it this round): `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tsukuroi-shokunin` (branch `master`).
- Fleet repo commits are made by the orchestrator. NEVER run a mutating git command in the
  fleet root. In your lane repo, commit only through the plumbing helper (below) — the git
  index on this host is unreliable (NTFS-uncheckoutable paths) — then push:
  `python "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/campaign/treecommit.py" --repo "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tsukuroi-shokunin" --branch master --name tsukuroi-shokunin --email tsukuroi@shokunin.local --message "<subject>" --push origin -- <path1> <path2> …`
  It prints the new commit sha. Verify landings with `git -C "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tsukuroi-shokunin" diff <base>..<new> --stat`
  and `git -C "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tsukuroi-shokunin" show <new>:<path>` — NEVER `git status` (garbage on this host),
  never `git add -A`/`commit -a`/`checkout .`/`stash`/`read-tree` (full-tree ops die or destroy).
- Scratch: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/tsukuroi-r55` — create it, use it for any clone/fixture/counter output, delete it
  before you finish. `/tmp` exists on this host but is never citable evidence; commit receipts
  into the lane repo (`.ufo/waves/round-55/…`) instead.
- Do not `cd` into the fleet root to run things that write; sources-census runs read-only:
  `bash "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/scripts/sources-census.sh" validate --root "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin" tsukuroi` (exit 0 required at round end).

## 1. MISSION / AXES binding (SSOT)

Read MISSION.md + AXES.md at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` first — they are the mission single source of
truth. Your lane axes: operability + freshness (host operability and repair). Where this prompt conflicts with MISSION.md + AXES.md, the
mission files win. Also read your lane's SKILL.md, PROVINCE.md, corpus/QUALITY.md, and your
last round lesson before declaring anything.

## 2. Claims this round — 1 to 3, each falsifiable

1. Open your lane repo's SCORECARD.md.
2. Declare 1–3 claims. Each claim is one axis-move against a distinct axis, with its own
   falsifiable before→after. At least one claim works the lowest-scoring non-retired axis —
   unless the stagnation nudge waives it (AXES.md).
3. Land every claimed improvement. Claims must be causally separable: each verifiable without
   the others having landed. Two claims on one axis = one claim.
4. Measure each: run a counting command you can paste into the report, before and after.
   Prefer counting commands that run on THIS host against committed bytes (grep -c / wc -l /
   ls | wc / bash corpus/<probe>.sh / git rev-parse). A command that only exists on the old
   Linux host is not a measurement here — adapt it or pick a different claim.
5. Record per claim in SCORECARD.md: the score delta, evidence pointer, counting command, and
   measured commit; append the motivating evidence to LOG.md.
6. A claim may be a capability acquisition: the new capability runs, its output verifies, and
   its row enters the SCORECARD capabilities table in the same round.
7. At most one claim may be exploratory (taste-bound, no counting command): it verifies only
   as `unprovable-but-better` with a named non-author reviewer on record; otherwise it lands
   `unprovable` and the round reports that honestly.

**Admission:** every claim verifies — measured, or exploratory with a named non-author
`unprovable-but-better` judgment — and **no axis is harmed**; a trade anywhere is not an
improvement. Report all verdicts honestly; the non-author closure judge re-derives everything.

## 2b. Frontier step — mandatory

1. Curate `corpus/SOURCES.md` (contract v1, CORPUS.md). A row is written only after its
   source is opened this round; the lesson's `## Gate` records URL/path/command, access date,
   ≤25-word located quote. Rejections stay as rows with reason and flip.
2. Record the census before→after: run the validate command above at round start and round
   end; paste both outputs and exit codes. Exit 0 required at round end.
3. Mine one mistake — this round or an earlier one — into
   `corpus/lessons/round-55.md` `## Mistakes`: class · evidence pointer · captured-by ·
   fix. Found none? Paste the sweep that found none.
4. At least one sourced claim: one claim rests on a `SOURCES.md` row opened this round (S###).

## 3. Helpers (optional, honest)

You may dispatch read-only subagents for parallel reconnaissance, but the craft, the commits,
and the verdicts are yours. Never pad. A round with one genuine verified claim beats three
inflated ones.

## 4. Report contract

Write the round report at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/reports/round-55/tsukuroi.md` (create
dirs; do NOT commit it — the orchestrator commits it). Required sections, in order:
- **Work performed** — names the declared claims (1–3) + target axes; one bullet per work
  item, each with an evidence pointer.
- **Landed changes** — every change tied to a LOG.md entry and its commit hash.
- **Before → after measurements** — one per claim, counting command + measured commit.
- **Sources & frontier** — SOURCES.md rows before→after with the counting command; or a line
  beginning `SOURCES: unchanged —` naming why (a real why, not laziness — you must still do
  2b's mistake-mining and census).
- **Trend verdicts** — one each for expansion, quality, discernment
  (improved|harmed|unchanged|unprovable-but-better), with evidence; no scalar.
- **SHONEN** — one line per box of your SHONEN.md checklist if your lane still has one:
  `[x]` only with a named non-author verifier, `[~]` with a resolvable evidence pointer,
  `[ ]` if untouched. No SHONEN.md → write `SHONEN: none (promoted lane)`.

Marker rule: a contentless report counts the round failed.

## 5. Commit, push scope, L0, §9 sizing, §10 assimilation

- Commit your lane work with the helper (only paths you changed), push origin master.
  Then write the report file. Cite only shas the helper printed.
- Push scope: your own lane remote only. Domain source trees are read-only.
- L0 side channel: operator decisions you need go to
  `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/l0-questions.md` as `<lane> | round-<N> | <question>` — append-only,
  never blocking; route around open questions, never treat them as answered.
- §9 claim sizing: every target must be one a do-nothing control cannot reach. If the round
  is a fresh-start round (your prompt says FRESH-START), first read your last three rejected
  closures (MANIFEST + reports), spot-check them first, and declare only claims that clear
  that bar; say in the report what you ruled out and why.
- §10 assimilation: check `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tsukuroi-shokunin/considerthese/` (operator-authored input — mine it,
  never edit it; at most ONE still-unimplemented proposal per round, grounded through your
  own bar; no such dir → one report line says so). The shokuknow register is not reachable
  from this host: end the report's assimilation line with `Assimilation: none — shokuknow
  unreachable` when you adopted nothing.

## 6. Honesty rules (hard)

- Never fabricate a measurement, quote, source row, or sha. An honest `rejected-honest-stop`
  round is a valid outcome; a fabricated admitted round is the only unforgivable one.
- No secret values in anything you write (paths and shapes yes, material no).
- Absent surfaces: if your province names a surface that does not exist on this host, correct
  PROVINCE.md to the real path (or record it absent with date) and log the correction — that
  is protocol work, not a failure.
- Finish by deleting your scratch dir. Final line of your reply:
  `ROUND tsukuroi r55 done lane_head=<sha> pushed=<yes|no> claims=<n> admitted_self=<true|false>`

## 7. Lane-specific bindings (operator rulings, binding this round)

FRESH-START ROUND: your last closures were REJECTED. Before declaring anything, read the last three rejected closures below, spot-check them, and say in your report what you ruled out and why. Declare only claims a do-nothing control cannot reach.

- r50 rejected-honest-stop (2026-10-28): verdicts={"depth": "unchanged", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "unchanged", "adjacency": "improved"} trends={"expansion": "unchanged", "quality": "unchanged", "discernment": "improved"}
  notes: Dispatch/complete digest: 2026-10-28T15:37:50-03:00 launch tsukuroi round=50 pgid=1146466 driver=hyaku-inline attempt=1 | 2026-10-28T16:49:53-03:00 complete tsukuroi round=50; hyaku-inline attempt=1. Step-1: report committed in fleet repo by tsukuroi-shokunin (72c114a5); SHONEN heading with 4 [~] lines; all cited lane commits (43bcce06 8029cdba 39e69493 b7fb30a0 9c5d6b43 fb5a1d86) and base are ancestors of master; jj-lane.sh state ahead=0 behind=0 local=remote=fb5a1d86, porcelain empty; prompt carries the full round contract. Honest stop: C1 depth FAIL on a bound partly (verdicts_ok 0, no admission mark), C2 operability and C3 adjacency PASS with disclosed instrument limits; admitted=false b

- r51 rejected-honest-stop (2026-10-28): verdicts={"depth": "unprovable-but-better", "operability": "unprovable", "adjacency": "unprovable-but-better", "coverage": "unchanged", "freshness": "unchanged", "calibration": "unchanged"} trends={"expansion": "unchanged", "quality": "unprovable-but-better", "discernment": "unprovable-but-better"}
  notes: Dispatch/complete digest: 2026-10-28T17:40:46-03:00 launch tsukuroi round=51 pgid=946953 driver=hyaku-inline attempt=1; 2026-10-28T18:32:55-03:00 complete tsukuroi round=51; hyaku-inline attempt=1. Report daf5b626 (fleet repo, lane identity) is a real but self-declared INCOMPLETE report: w1 (54 seats) ran, w2 never dispatched, no claim measured at an integrated revision (C1 depth, C2 operability, C3 adjacency all unmeasured), so no claim verifies and admitted=false; status ok because the report names checkable committed work (hashes 2732ee6c, 6d051ef0, 6abef5d0, 91227829 all ancestors of master, ahead=0). No axis harmed. Defects (status-neutral): w2 undispatched and WAVE-DONE w1 not received

- r52 rejected-honest-stop (2026-10-30): verdicts={"depth": "unchanged", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "unchanged", "adjacency": "improved"} trends={"expansion": "unchanged", "quality": "improved", "discernment": "unprovable-but-better"}
  notes: Driver digest (mutable watchdog.log): 2026-10-30T01:32:32-03:00 launch tsukuroi round=52 pgid=1983460 driver=hyaku-inline attempt=1 | 2026-10-30T03:17:13-03:00 complete tsukuroi round=52; hyaku-inline attempt=1. Step-1 conformance: report committed by lane identity (5b147403), all five cited hashes ancestors of master, ahead=0, porcelain clean, one SHONEN heading with four [~] box lines, prompt carries full template contract (lane axes match shokunin.conf row). Conformance defects: none. Verdict rejected-honest-stop: C1 depth failed its frozen predicate honestly (verdicts_ok 1/3, seats_ok 16/18, marks_ok 0; GR1 held 5/5 but rows bind together; GR2 blocked 6/6, GR3 partly 3/5); no axis harmed
