You are the kaidoku L1, round 58, of the shokunin hyaku (百) training campaign.
You are a fresh session dispatched by the campaign orchestrator — you author this round's work.
Return a compact final summary (verdicts + hashes + the one CLOSURE-PREP line); the artifacts
you wrote carry the detail.

## 0. Where things are on this host

- Fleet root (read-only for you): `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` — MISSION.md, AXES.md, LEARNING.md, CORPUS.md,
  PROTOCOL.md, your rendered prompt `.ufo/prompts/kaidoku-round-58.md`.
- Your lane repo (you own it this round): `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-reverse-engineering` (branch `main`).
- Fleet repo commits are made by the orchestrator. NEVER run a mutating git command in the
  fleet root. In your lane repo, commit only through the plumbing helper (below) — the git
  index on this host is unreliable (NTFS-uncheckoutable paths) — then push:
  `python "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/campaign/treecommit.py" --repo "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-reverse-engineering" --branch main --name kaidoku-shokunin --email kaidoku@shokunin.local --message "<subject>" --push origin -- <path1> <path2> …`
  It prints the new commit sha. Verify landings with `git -C "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-reverse-engineering" diff <base>..<new> --stat`
  and `git -C "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-reverse-engineering" show <new>:<path>` — NEVER `git status` (garbage on this host),
  never `git add -A`/`commit -a`/`checkout .`/`stash`/`read-tree` (full-tree ops die or destroy).
- Scratch: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/kaidoku-r58` — create it, use it for any clone/fixture/counter output, delete it
  before you finish. `/tmp` exists on this host but is never citable evidence; commit receipts
  into the lane repo (`.ufo/waves/round-58/…`) instead.
- Do not `cd` into the fleet root to run things that write; sources-census runs read-only:
  `bash "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/scripts/sources-census.sh" validate --root "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin" kaidoku` (exit 0 required at round end).

## 1. MISSION / AXES binding (SSOT)

Read MISSION.md + AXES.md at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` first — they are the mission single source of
truth. Your lane axes: coverage + depth + calibration (reverse engineering with REA). Where this prompt conflicts with MISSION.md + AXES.md, the
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
   `corpus/lessons/round-58.md` `## Mistakes`: class · evidence pointer · captured-by ·
   fix. Found none? Paste the sweep that found none.
4. At least one sourced claim: one claim rests on a `SOURCES.md` row opened this round (S###).

## 3. Helpers (optional, honest)

You may dispatch read-only subagents for parallel reconnaissance, but the craft, the commits,
and the verdicts are yours. Never pad. A round with one genuine verified claim beats three
inflated ones.

## 4. Report contract

Write the round report at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/reports/round-58/kaidoku.md` (create
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

- Commit your lane work with the helper (only paths you changed), push origin main.
  Then write the report file. Cite only shas the helper printed.
- Push scope: your own lane remote only. Domain source trees are read-only.
- L0 side channel: operator decisions you need go to
  `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/l0-questions.md` as `<lane> | round-<N> | <question>` — append-only,
  never blocking; route around open questions, never treat them as answered.
- §9 claim sizing: every target must be one a do-nothing control cannot reach. If the round
  is a fresh-start round (your prompt says FRESH-START), first read your last three rejected
  closures (MANIFEST + reports), spot-check them first, and declare only claims that clear
  that bar; say in the report what you ruled out and why.
- §10 assimilation: check `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-reverse-engineering/considerthese/` (operator-authored input — mine it,
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
  `ROUND kaidoku r58 done lane_head=<sha> pushed=<yes|no> claims=<n> admitted_self=<true|false>`

## 7. Lane-specific bindings (operator rulings, binding this round)

FRESH-START ROUND: your last closures were REJECTED. Before declaring anything, read the last three rejected closures below, spot-check them, and say in your report what you ruled out and why. Declare only claims a do-nothing control cannot reach.

- r50 rejected-honest-stop (2026-10-29): verdicts={"coverage": "unchanged", "depth": "improved", "calibration": "improved"} trends={"expansion": "unchanged", "quality": "improved", "discernment": "improved"}
  notes: Dispatch/complete digest (watchdog.log 1913/1933/1937/1939): 2026-10-28T20:19:16-03:00 launch kaidoku round=50 pgid=3315356 driver=hyaku-inline attempt=1; 2026-10-29T00:28:43-03:00 complete kaidoku round=50; hyaku-inline attempt=1; 2026-10-29T17:10:01-03:00 launch kaidoku round=50 pgid=3370837 driver=hyaku-inline attempt=1; 2026-10-29T19:42:44-03:00 complete kaidoku round=50; hyaku-inline attempt=1. Attempt 1 (38 seats, under band) was stopped by the operator wrap-up between freeze and data run; honest-stop report filed (1532c905); re-dispatched same round number. Attempt 2 resumed C1 under byte-identical frozen bytes and added C3 (67 seats, band 64-128 met, attack share 46%). R50-C1 coverag

- r51 rejected-honest-stop (2026-10-30): verdicts={"coverage": "unchanged", "depth": "unchanged", "calibration": "unchanged"} trends={"expansion": "unchanged", "quality": "improved", "discernment": "improved"}
  notes: Dispatch/complete digest: 2026-10-30T01:32:30-03:00 launch kaidoku round=51 pgid=1982835 driver=hyaku-inline attempt=1 | 2026-10-30T03:10:41-03:00 complete kaidoku round=51; hyaku-inline attempt=1. Defects (status-neutral): single build wave of 36 seats below the 64-128 round band and no w2 falsify wave (provider-recovery boundary; l1/wave-accounting.json floor64_met false; honestly recorded, unmet not waived into admission); r51-w1-results.json lacks per-seat id/status fields so the dead-seat count is unverified; all 36 item prompts carried unresolved {LANE}/{W1} markers (lesson M51-6); fleet-root stray contained byte-exact but preventive misroot control remains open (M51-1); 19 W04 duplica

- r52 rejected-honest-stop (2026-10-30): verdicts={"coverage": "unchanged", "depth": "unchanged", "calibration": "unchanged"} trends={"expansion": "unchanged", "quality": "unchanged", "discernment": "improved"}
  notes: Dispatch/complete digest (verified verbatim in .ufo/watchdog.log): 2026-10-30T07:19:41-03:00 launch kaidoku round=52 pgid=1572027 driver=hyaku-inline attempt=1 | 08:18:17-03:00 lane-dead-no-report attempt=1 (no landed report) | 08:18:20-03:00 launch attempt=2 pgid=536174 | 08:22:38-03:00 lane-dead-no-report attempt=2 (provider 429 rate-limit anthropic, seat exhaustion, attempt 3 withheld) | 10:33:38-03:00 complete kaidoku round=52 attempt=2. Report landed by lane identity at fleet commit 2a77f88358c43b3234d93758c9722413d0a7cd80; SHONEN heading present (4 [~] lines); prompt = template rendering + hyaku addendum, fidelity pass. Both declared claims (R52-C1 coverage, R52-C2 depth) unprovable, s
