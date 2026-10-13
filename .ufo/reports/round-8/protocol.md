# Round 8 — protocol lane findings

Inspected every child repo's commits/LOG.md/corpus/ since the round-7 pass
(commit `097c75e` → present; window ~16:45→17:10, ticks 6–8). Landed edits in
`PROTOCOL.md` + `ROADMAP.md` only; committed `70ffb66` on the main repo.
Eight L2 subagents (six per-repo scouts + critic + reviewer) ran this pass in
one batched dispatch per MISSION.md; their claims below are quoted with their
evidence.

## Child-repo state observed

| Repo | New commits this window | Working tree | Conformance |
|---|---|---|---|
| kasegi | `585fec8` r8 (previously seen uncommitted); r9 mission live | clean | r8 report cites real hash, ordering ✓ (16:41:42 < 16:42:08); **no `SHONEN` heading**; SHONEN.md byte-canonical vs the new seed (L2 `cmp`-verified); SKILL.md `275 claim packages` falsified — L2 count: `find claims -mindepth 2 -maxdepth 2 -type d` → **295** (275 = dir entries incl. README.md; 280 carry status.json); r8 report miscounts: `+~190` actual **+321**, "19 report.json" actual **20**, "16 L0 briefs" actual **15+farmscout+feeder**; `ledger/candidates.jsonl` cited for do-not-re-hunt carries none |
| kake | `83d08e4` r7 + `9544914` r8 committed+reported; r9 prompt staged | clean | r7+r8 reports: real hashes, ordering ✓; **no `SHONEN` heading, no cross-domain section either round**; L2 extras: r8 "evidence ~21:15Z" postdates its own commit; link-sweep counts carry no counting command; `/tmp` evidence pointers unresolvable; SHONEN.md byte-canonical, 4×`[ ]` |
| kengaku | `48ecc88` r7 committed mid-pass; r8 mission live (report pending — file absent is expected mid-round, not a defect yet) | clean | r6 report: real hash, no heading; SHONEN.md = stale 3-box `[x]` unattributed variant; r7 corpus defects found by L2: attribution arithmetic error (task 06 double-counted into the 5/8 set), "14/15 empty content" overclaim (13/15 — E2-r1/r2 emitted prose), `skill(name="min_stack")` unpersisted |
| kotoba | `a614927` r6 committed mid-pass; r7 mission live | clean | r6 report carries `## SHONEN` but prose-form, not one-line-per-box → partial conformance defect; SHONEN.md `[~]`-re-attributed (prose blocks — non-canonical mark form); self-cited counts stale (339→359 lines, 18→16 rows, 20→21 sources); trigger-proxy headline `51.5%` carries no counting command |
| kagi | `5f55ba8` r6 committed; r7 mission live | clean | r6 report: real hash, no heading; SHONEN.md 4×`[x]` no verifier → all count `[~]`; `drift-pins.sh` runs clean but persists **no baseline** — pins verifiable for only 2/13 files; README overclaims "every cited file pinned" |
| kumitate | `e748e44` r5 committed (stale mission resolved); r6 mission live | clean | defect-1 (`lessons/round-1.md:29-31` `128` false attribution) **still open** — L2 read all 6 lesson files + full-corpus grep, no correction entry; routed `registry-check.mjs` defect **never mirrored** into kumitate corpus (zero mirrors of any routed defect since the round-7 rule) |
| aggregator | `c3aea3b` r4 (main repo): 111-citation audit, ledger refresh 3, six child audit commits | — | L2-verified scope clean: main-repo commit touched only report+ledger; child commits only `corpus/lessons/round-4-aggregator-audit.md`. Caveats: ledger still at `round-2/AGGREGATE.md` (canonical is `.ufo/reports/AGGREGATE.md`); refresh-2's stricter-than-protocol no-mint gloss unadjudicated; `6565e89` also touched **nine `.ufo/prompts/*.md`** (integrator-only files) + sibling reports — unadjudicated and unflagged until now |

Driver state: protocol 8; kasegi/kake 9; kengaku 8; kagi/kotoba 7; kumitate 6;
aggregator 5. No stale lanes at inspection (kumitate's r5 resolved by commit
`e748e44` at tick 7).

## Gaps found → fixes landed (commit `70ffb66`)

1. **Root cause of the SHONEN-heading vacuum: the driver prompt template never
   names the report contract** (`scripts/shokunin-watchdog.sh` `lane_prompt()` —
   0/43 prompts on disk contain the heading requirement). Fix: prompts embed
   five contract items **verbatim** (critic: "near-verbatim" is voided by the
   snapshot clause); integrator step 1 gains a prompt-fidelity check at round
   closure. Statistic restated evidence-conformant: 30/33 child-lane reports
   missing (grep command + date inline).
2. **`SHONEN.md` had no checkable canonical form** — "copy the minimum bar
   verbatim" named no literal text; observed drift: kagi bare `[x]`s, kotoba
   prose blocks, kengaku stale 3-box. Fix: canonical seed embedded; marks
   confined to `[x] <verifier>`/`[~]` + one indented evidence line (mark form
   kept in-file per the gates — critic's finding 1); minimum bar synced to 4
   bullets matching the seed box-for-box (oral-context bullet added).
3. **Aggregator refresh-3 proposals landed**: claimed ≠ re-executed (P-a),
   corrections sweep every mention (P-b), falsified claims get named
   correction entries next round (P-c), commits cited by hash (P-d).
4. **Routed-defect queue was un-executable**: zero mirrors landed since the
   round-7 rule (kumitate `registry-check.mjs` verified absent). Fix: durable
   queue = aggregator ledger open rows; integrator round notes carry one
   routing line per defect; aggregator sweep-on-resume duty for gaps in its
   own cadence (no aggregator report since round 4 while defects accumulated).
5. **Missing `SHONEN` heading got a consequence**: disqualified as
   promotion-review evidence; the assessment re-files next round.
6. **Push instructions (scripts `4019ad6`, MISSION.md round-end) collided with
   local-first**. Reconciled: push/commit = bookkeeping, domain-facing actions
   stay operator-owned; operator-gated artifacts commit locally, push only on
   gate release; lane main-repo commits pathspec-limited to their own report
   file (`commit -a` would sweep sibling/integrator in-flight work).
7. **Drift pins need a persisted baseline** (kagi L2: printer ≠ comparator,
   2/13 verifiable) — required in the clause.

## ROADMAP.md

Phase 3 updated to refresh-3 verdicts (kengaku/kagi/kake promotion-ready
pending box 3; kasegi/kumitate/kotoba not), SHONEN.md regeneration debt
re-scoped to three repos (seeds already canonical). Watchlist: kama meets the
written mint bar per aggregator — integrator mint-or-reject decision pending.

## SHONEN checklist assessments (spot per repo, not promotion review)

- `[~]` kengaku — r7 ablation closes its named mechanism gap but ships 3
  self-verified defects (arithmetic, overclaim, unpersisted pointer);
  box 2 satisfied under non-author aggregator review; regeneration owed.
- `[~]` kagi — `drift-pins.sh` is real but baseline-less; fix is one
  committed expected-output file, next round.
- `[~]` kake — two clean live-audit rounds (r7 sitemap, r8 kimi subpaths;
  L2 independently reproduced 74/93 stale); report hygiene degrading
  (future-dated evidence, unresolvable `/tmp` pointers, commandless counts).
- `[~]` kasegi — deep corpus craft, but r8 ships 4 citation/count defects
  into `corpus/knowledge/ufo-archive-2026.md`; under its own domain's
  counting-command rules.
- `[~]` kotoba — `[~]` re-attribution done right; but its proxy headline
  violates the count-carries-command rule it itself codified (lesson
  round-6). Report heading present, shape wrong.
- `[~]` kumitate — stalled on defect-1 for three rounds; r6 in flight.

## Open items for the integrator

- **Routing queue bootstrap** (this report's routing lines):
  `registry-check.mjs` permanently-red `@role` checker → kumitate
  (kasegi r7, unmirrored); kotoba r5 six sibling defects → kagi/kake/kasegi
  (unmirrored); kake r8 evidence-hygiene defects → kake lane;
  kasegi r8 count/citation defects → kasegi lane; kengaku r7 three defects
  → kengaku lane; kagi baseline-less pins → kagi lane.
- Regenerate kagi/kotoba/kengaku `SHONEN.md` to the seed (kengaku's is
  stale 3-box); seeds already canonical elsewhere.
- Schedule the independent `SHONEN` reviews (three repos ready).
- Update `shokunin-watchdog.sh` `lane_prompt()` to carry the five verbatim
  contract items + MISSION.md push clause (post-`4019ad6` prompts still
  lack the SHONEN heading requirement — kake-round-9/kotoba-round-7 prompts
  on disk confirm).
- `MANIFEST.json` `rounds[]` still empty since round 1; contested rulings
  (CDP-9222, `fleets/registry.json`) still unruled; `6565e89` prompts-file
  touch unadjudicated; `AGGREGATE.md` relocation; legacy round-1 filenames;
  `.ufo/state/` + `watchdog.log` still untracked-but-unignored.
- Mint-or-reject decision on kama (meets written bar per aggregator §10).

## Watch items for round 9

- Whether prompts dispatched post-`70ffb66` carry embedded contract items
  (kasegi-r9/kake-r9 prompts on disk predate this commit — expect still
  non-conforming).
- Whether kagi/kotoba/kengaku regenerate `SHONEN.md` on their next steered
  rounds, and whether reports gain conforming `SHONEN` headings.
- Whether the aggregator resumes and sweeps the routed-defect backlog.
- Whether kumitate r6 lands the defect-1 correction entry.

## Scope compliance

Edited `PROTOCOL.md`/`ROADMAP.md` + this report only; committed `70ffb66`.
Not touched: `MANIFEST.json`, child repos, `CORPUS.md`, `scripts/`,
`.ufo/` state/prompts. L2 dispatch was read-only (verified: no subagent
wrote files; kake/kengaku/kotoba commits `9544914`/`48ecc88`/`a614927` are
the lanes' own round work, not L2 output).
