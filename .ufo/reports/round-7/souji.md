# souji — round 7 (small receipts + quarantine exercise)

Lane HEAD at report time: `1cf5fa8` (souji-shokunin identity). Single
batched dispatch: 24 seats on **zai-coding-plan/glm-5.3-flash**; 24/24.

## Round verdict: REJECTED as a round — 2/3 claims verified

C1 (calibration) and K1 (coverage) verify; O1 (quarantine exercise) is
NOT-MET and is reported as such. Nothing was manufactured to pass.

## Work performed

**C1 — blind-pair receipts on small live artifacts (verified).** Six
author/blind pairs audited lore's `.scratch` (218KB), lore's worktree
registrations, and four souji self-hygiene shards. Every pair agreed; the
receipts denied every candidate:

- lore `.scratch`: NOT-SAFE on three independent gates — untracked-dirty,
  a live reference in lore's own LOG.md, mtime 0.75d < the 1-day floor.
- lore worktrees: **the parent's r6 column misread was caught** — the "3"
  was unpushed commits, not registrations; actual registrations 0 (the 19
  were pruned r3). S02 refused to manufacture a candidate from the
  misread.
- souji self-hygiene: every tracked path fails the unpushed-touching gate
  (the lane's 11 bookkeeping commits touch tools/, tests/, census/);
  untracked residue is today's in-flight round work.

**Discovery (the round's real finding).** The lane's own remote does not
exist: `github.com/VeigaPunk/shokunin-repo-hygiene` → 404 (creation is
operator-owned; never pushed). With zero remote-tracking refs, every
pushed receipt inside the lane repo is unverifiable — the discipline
correctly refuses the lane certifying its own files removable. Verified
parent-side: `git ls-remote origin` → Repository not found.

**O1 — quarantine exercise (NOT-MET).** With every in-scope candidate
denied, the flow had no authorized target: the only receipt-authorized
removals in the fleet are the 96 approval rows (operator sign-off
pending since r3) and lanes that push (external). The quarantine flow
stays UNEXERCISED — now with a definitive reason, recorded in
`corpus/lessons/round-7.md`.

**K1 — fleet delta census (verified).** `tools/souji-census.sh` re-run
(`census/round-7/fleet-census.tsv`); deltas vs r6 classified as live-deltas;
no new dead worktree registrations; kotodama hands-off stands (40.4G+).

## Landed changes

- `census/round-7/` (24 fragments + fleet census); `corpus/lessons/round-7.md`;
  LOG entry — commit `1cf5fa8`.

## Before → after measurements

- C1: before — blind-pair practice existed for files, not for live small
  artifacts → after: 6/6 pairs agree; 3 distinct gate classes exercised
  (dirty-touching, live-reference, mtime-age) + the misread catch.
- O1: unexercised → still unexercised, now with an evidenced reason
  (NOT-MET; honest stop).
- K1: delta census reproducible via the r6 tool; deltas = live-only.

## SHONEN

- [~] SKILL.md decision tables — the receipts' gates got their realest workout yet.
- [~] End-to-end domain task — the lane proved a negative space: nothing in scope is removable.
- [~] Executable without oral context — 24 zero-context seats.
- [~] No cross-domain bleed — operator-gated items and lane pushes named as the remaining gates; nothing absorbed.
