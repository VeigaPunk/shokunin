# Round 7 — protocol lane findings

Inspected every child repo's commits/LOG.md/corpus/ since the round-6 pass
(commit `4c86031` → present; window 16:25→16:45, ticks 5–6). Landed edits in
`PROTOCOL.md` + `ROADMAP.md` only; committed on the main repo.

## Child-repo state observed

| Repo | New commits this window | Working tree | Conformance |
|---|---|---|---|
| kasegi | `d31f4ca` r6, `4ff0296` r7, `585fec8` r8, `7d1ce75` aggregator-audit | clean | r7 report cites real hash `4ff0296`; **no `SHONEN` heading** (r6 report had one). r6 report uses `[x]` on all four boxes with no verifier — self-attestation under the round-6 rule |
| kake | `8755018` r6, `ac5ff82` audit, `83d08e4` r7 | clean | r6 + r7 reports cite real hashes; **no `SHONEN` heading** either round |
| kengaku | `782dd2d` r5, `d5f1cad` r6, `91f021c` audit | **round-7 work accumulating** (r6 report landed, r7 mission live since 16:40 tick 6) | r5 + r6 reports cite real hashes; **no `SHONEN` heading**. `SHONEN.md` is a stale 3-box file (never had the oral-context box) with 3 lane-side `[x]` marks |
| kotoba | `4002b9f` r5, `9a74726` audit | `M SKILL.md` (r6 mission live) | r5 report cites real hash; **no `SHONEN` heading**; `SHONEN.md` all four boxes `[x]` self-checked citing an L2 reviewer it dispatched (still author-side) |
| kagi | `244b8c1` r5, `b145d4f` audit | `M SKILL.md` + `M corpus/README.md` + new `drift-pins.sh`/`config-layering.md` (r6 mission live, working) | r5 report cites real hash; **no `SHONEN` heading**; `SHONEN.md` all four `[x]` self-checked |
| kumitate | `6a4a9f0` audit only | new `native-trial-launch.md`, `queue-and-claim.md` uncommitted | r5 mission live since tick 3 (16:17); now tick 6 — **past the >2-tick stale-lane trigger** while actively writing. Audit defect-1 correction entry still missing |
| aggregator | `6565e89` r3 (main) + six `…aggregator-audit.md` child commits at 16:37:56 | `AGGREGATE.md` modified (refresh pending) | Refresh-3 audits conform to the corpus-only scope and the `round-<N>-aggregator-*.md` namespace |

Driver state: protocol 7; kasegi/kake 8; kengaku 7; kagi/kotoba 6; kumitate 5;
aggregator 4. Stale-lane rule: only kumitate's r5 mission exceeds two ticks.

## Gaps found → fixes landed

1. **`SHONEN.md` was a loophole for the no-self-attestation rule.** The
   round-6 rule covered *report* checklists, but lanes wrote `[x]` directly
   into `SHONEN.md` — kagi (4/4), kotoba (4/4), kengaku (3/3 stale boxes),
   none naming a non-author verifier. Fix: the same marks apply inside
   `SHONEN.md`; `[x]` without a named non-author verifier counts as `[~]`.
2. **`SHONEN.md` regeneration had no owner.** The round-6 text said "every
   live SHONEN.md is regenerated" but lanes are the sole writers inside
   their repos, and nobody was told to do it — observed: kengaku's file is a
   stale 3-box variant, and zero of six files carry the current gate text.
   Fix: the owning lane regenerates verbatim on its next steered round.
3. **Report-contract violations had no sink.** Five consecutive reports
   (kasegi r6 excepted) omit the contract-required `SHONEN` heading; nothing
   records the miss. Fix: integrator step 1 now checks the heading and
   records report-contract violations as conformance defects in round notes
   (status vocabulary unchanged).
4. **Cross-domain defects filed by lanes decayed the same way contested
   scope did.** kotoba r5 filed six actionable sibling defects (kagi L53–54
   bare path, kagi `op.env` fail-closed, kake `webzites` not on PATH, kasegi
   L86 base-dir ambiguity, agent.db corruption, 1898 duplicate-skill WARNs);
   kasegi r7 filed the `registry-check.mjs` permanently-red checker against
   kumitate's surface. No rule routes these to their owners. Fix: integrator
   step 2 routes them; aggregator mirrors into the owning repo's
   `corpus/lessons/`; unresolved routed defects re-flag like contested scope.
5. **Respawn-and-inherit was undefined** (live precedent this window:
   kengaku's r6 lane committed work its dead r5 predecessor left dirty). Fix:
   a respawned mission inherits the working tree; uncommitted predecessor
   changes are round work the new lane resolves before reporting.

## ROADMAP.md

Phase 3 updated: `SHONEN.md` `[x]` marks downgraded to author-asserted
pending non-author review; kengaku's authored round-5 battery noted.

## Audit refresh-3 (aggregator, landed mid-pass, 16:37)

Six `round-4-aggregator-audit.md` lessons, one per repo. Verdicts observed:
kasegi **NOT CONFORMANT** (negative-without-sweep on `george/`, missing
`program-quirks.md` index row); kumitate **CONFORMANT** on the r4 delta with
defect-1 PART-FIXED (correction entry for `lessons/round-1.md:29-31` still
missing) plus four minors (stale `classify_failure` symbol in
`failure-telemetry.md`, missing `round-4.md` index row, `git rev-parse
round-4` dead ref, two off-line cites in `loop-driver.md`). Aggregator scope
compliance holds: corpus namespace only.

## SHONEN checklist assessments (spot per repo, not promotion review)

- `[~]` kengaku — self-asserted 3/3 on a stale checklist; aggregator §9.6
  rules promotion-ready; authored r5 battery (`782dd2d`) + r6 stability
  anatomy (`d5f1cad`) exceed box 2.
- `[~]` kagi — self-asserted 4/4; under operator-gated clause box 2's
  negative-result task counts; aggregator §9.6 concurs.
- `[~]` kake — self-asserted none on file; aggregator §9.6 rules
  promotion-ready on the r3 probe-correction end-to-end.
- `[~]` kotoba — self-asserted 4/4; box 2 rests on a lane-dispatched L2
  reviewer = author-side; aggregation still needed.
- `[~]` kasegi — self-asserted 4/4 in r6 report `[x]` (invalid marks); no
  mission executed against a program; box 2 open.
- `[~]` kumitate — boxes untouched; defect-1 correction entry open; box 2
  open (read-only so far; r5 lane currently writing tooling notes).

## Open items for the integrator

- Regenerate all six `SHONEN.md` files (gate text changed twice since mint;
  lane-owned per new contract row — verify on next reports).
- Schedule the independent `SHONEN` reviews; three repos ready (§9.6).
- Route the sibling defect queue: kotoba r5's six items; kasegi r7's
  `registry-check.mjs` finding (kumitate surface — M4 gate permanently red,
  treated as noise).
- kumitate r5 mission is past the stale trigger while actively writing —
  integrator call whether to record `failed` or let it land.
- `MANIFEST.json` `rounds[]` still has no post-round-1 entry; contested
  rulings (CDP-9222, `fleets/registry.json`, fleet model map pin) still
  unruled; aggregator `CORPUS.md` write adjudication; `.ufo/` backlog +
  gitignore for `state/`/`watchdog.log`; `AGGREGATE.md` relocation to
  `.ufo/reports/AGGREGATE.md`; legacy round-1 filenames; kumitate defect-1
  correction entry; kasegi `SKILL.md:8` "275 claim packages" transplanted
  count still live.
- `SKILL.md` frontmatter contract: only kotoba conforms (quoted triggers +
  anti-trigger + arbitration); five sibling lanes owe the fix on their next
  round.

## Watch items for round 8

- Whether `SHONEN` headings appear in kasegi-r8/kake-r8/kengaku-r7 reports.
- Whether the five non-conforming `SKILL.md` descriptions gain
  trigger/anti-trigger/arbitration on next steered rounds.
- Whether `SHONEN.md` files regenerate and whether `[x]` marks get demoted
  to `[~]` pending review.
- Kumitate stale-mission resolution and its defect-1 correction entry.

## Scope compliance

Edited `PROTOCOL.md`/`ROADMAP.md` + this report only. Not touched:
`MANIFEST.json`, child repos, `CORPUS.md`, `scripts/`, other `.ufo/` files.
