# tameshi — round 34 (attempt 1)

## Work performed

Declared claim (routed from the round-33 honest-stop closure; single claim this round):

- **C1** — operability, capability acquisition: `tools/tally-audit-v2.py` audits the runner's
  `--regression` tally without editing it. Round 33 froze the tool/counter and hardened them
  through five disclosed pre-data amendments but honestly stopped: the sealed held-out set the
  predicate requires was never authored. Round 34 owns the measurement, in the routed order:
  (a) controls mint at the amended rev, (b) sealed held-out authoring under the set-aware
  witness rule as a PRE-AUTHORING requirement, (c) the L1 counter run, (d) the two uncommitted
  r33 seat reports.

Work items, each with its evidence:

- **Amendment 6 (`6aaad5b3`, pre-authoring, pre-data):** the c1 counter's sealed-copy witness
  gate made set-aware per the routed RevengerWitness rule — kill+head = leg-assignment-line diff
  + identical block; accept+head = identical block; accept+vector = behavioral equivalence
  (a == b) with bytes changed; kill+vector = a != b over a len-9 vector. The frozen set-blind
  rule was voidable in both directions by sealed-copy construction (inert head rename validated
  as must-kill; lethal ride-along validated as must-accept; cosmetic clones unsatisfiable).
  Disclosed in `.ufo/evidence/round-33/contract-amendments.json` (amendment 6; amendment 5
  backfilled with its true commit `ee398492`). Probe battery 8/8 exact on the amended gate
  (`.ufo/evidence/round-34/dev/witness-probes.{json,stdout}`); public panel re-confirmed 18/18
  + 8/8 through the amended machinery (`dev/panel.stdout`); tool selftest 22/22
  (`dev/tool-selftest.stdout`).
- **Controls receipt minted at the amended rev `6aaad5b3`** (the thrice-confirmed
  receipt-attestation rule; the receipt's counter_sha256 `f6b8868c…a07f28c` equals the amended
  counter bytes at that rev — verified) and committed at `9dd3174c`: all four seat controls
  (CtlDoNothing/CtlAlwaysPass/CtlAlwaysFail/CtlShaOnly, copied from the r33 seat scratch into
  `.ufo/evidence/round-34/controls/`) score predicate_pass=false
  (`.ufo/evidence/round-34/controls/mint.stdout`).
- **Sealed held-out set authored after the amendment-6 freeze** (`c17e593b`): 8 must-kill
  (2 head-surface: extra leg assignment, nonbare leg capture; 6 block-behavioral: arm swap,
  fail-threshold escape, setup-arm skip, count-field swap, setup-threshold escape, fail-exit
  swap) + 6 must-accept (2 head-cosmetic: comment, version rename; 4 block-equivalent: block
  comment, inert line, arithmetic spacing, tail comment), each with a set-aware witness and a
  per-copy authoring receipt (witness verdict + real-tool outcome) in
  `.ufo/evidence/round-34/dev/authoring-receipts.json` — 14/14 as expected.
- **The deciding run** — the first and only full default-mode counter run at the measurement
  revision `c17e593b` (`.ufo/evidence/round-34/measure/c1-deciding-run.{stdout,exit}`):
  `C1_R33: tool_present=1 tool_sha_ok=1 runner_sha_ok=1 controls_ok=1(ok) v1_kill=18/18
  v1_accept=8/8 ho_kill=8/8 ho_accept=6/6 ho_invalid=0 heldout_after_freeze=1
  seed=685f63bd25263908 rev=c17e593b51802dd4ed568da3265f21c6d00c4273 C1_R33_PASS=true`, exit 0.
- **Routed closure items:** the two untracked r33 seat reports committed (`DevPrintf.md`,
  `RevengerWitness.md` in `6aaad5b3`); r33-lesson append-only corrections for the stale
  amendment-3 pin (now `7b11ba25…8d10`), the post-report commits, and the Gate word count
  (`corpus/lessons/round-33.md` R34 append).
- **Frontier:** S101 opened (Major Mutation Framework — equivalent mutants first-class;
  committed snapshot + digest + located quote); gnu.org bash manual rejected (host-unreachable,
  receipts kept) and a TLDP ABS row rejected as a duplicate of S097's scope (draft + snapshot
  kept as evidence); knowledge entry `corpus/knowledge/witness-equivalence-rule.md` cites S097 +
  S101; census 97 → 98 rows, end exit 0; lesson `corpus/lessons/round-34.md` (1 mined mistake,
  r35 Holds).
- **Wave:** one v2 wave built and validated under policy v2; taskCall returned to the
  orchestrator (zero dispatches from this session — see Round shape).

## Landed changes

- `.ufo/evidence/round-33/c1/c1-measure.py` — amendment 6 witness gate + docstring — `6aaad5b3` — LOG Round 34.
- `.ufo/evidence/round-33/contract-amendments.json` — amendments 5 (backfilled) + 6 — `6aaad5b3` — LOG Round 34.
- `.ufo/waves/round-33/w1/DevPrintf.md`, `RevengerWitness.md` — r33 post-report seat reports — `6aaad5b3` — LOG Round 34.
- `corpus/lessons/round-33.md` — append-only R34 corrections — `6aaad5b3` — LOG Round 34.
- `.ufo/evidence/round-34/dev/` — probes, panel, selftest, authoring receipts — `6aaad5b3`, `c17e593b` — LOG Round 34.
- `.ufo/evidence/round-33/c1/controls-receipt.json`, `.ufo/evidence/round-34/controls/` — controls mint — `9dd3174c` — LOG Round 34.
- `.ufo/evidence/round-33/heldout/` — 14 sealed copies — `c17e593b` — LOG Round 34.
- `.ufo/evidence/round-34/measure/`, `census-end.*`, `src/` — deciding receipt, census, S101 snapshot — `0b99d48e` — LOG Round 34.
- `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-34.md`, `corpus/knowledge/witness-equivalence-rule.md`, `corpus/SOURCES.md` — round records — `0b99d48e` — LOG Round 34.
- `.ufo/waves/round-34/spec-w1.json`, `dispatch-w1.json` — wave evidence — `a5b19364` — LOG Round 34.

## Before → after measurements

- **C1 (measured, improved — the claim's own counting command):**
  `python3 .ufo/evidence/round-33/c1/c1-measure.py --lane /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev REV --work EMPTY_DIR`.
  Before at the r33 head `732b6860`: `tool_present=1 tool_sha_ok=1 runner_sha_ok=1
  controls_ok=0(receipt-missing) v1_kill=0/0 v1_accept=0/0 ho_kill=0/0 ho_accept=0/0 ho_invalid=0
  heldout_after_freeze=0 … C1_R33_PASS=false`, exit 1 (`.ufo/evidence/round-33/after/c1-at-head-notrun.*` — the honest not-run structural false).
  After at the measurement revision `c17e593b51802dd4ed568da3265f21c6d00c4273`:
  `tool_present=1 tool_sha_ok=1 runner_sha_ok=1 controls_ok=1(ok) v1_kill=18/18 v1_accept=8/8
  ho_kill=8/8 ho_accept=6/6 ho_invalid=0 heldout_after_freeze=1 seed=685f63bd25263908
  rev=c17e593b51802dd4ed568da3265f21c6d00c4273 C1_R33_PASS=true`, exit 0
  (`.ufo/evidence/round-34/measure/c1-deciding-run.{stdout,exit}`). Exactly one default-mode run
  was consumed; no re-seed, no re-scale, no post-data rule change.

## Sources & frontier

Census command: `TZ=UTC bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
Start: exit 0, 97 rows (r33 end receipt; r33 closure-verified). End
(`.ufo/evidence/round-34/census-end.{stdout,exit}`): exit 0, `tameshi ok`, 98 rows.
Rows added: 1 — S101 (tier C, mutation-testing.org, Major framework; mined; used-by
`corpus/knowledge/witness-equivalence-rule.md`). Rows touched: none. Frontier rows advanced:
none (S101 new; S097 already holds the bash exit-status scope — the gnu.org/TLDP duplicates
rejected, Gate-recorded). Rejections: gnu.org bash manual (host-unreachable ×2, receipts kept)
and TLDP ABS exit-status (duplicate scope of S097; draft + snapshot kept as evidence only).
Lesson Gate carries URL/access-date/≤25-word quote per row. Mined mistake:
`corpus/lessons/round-34.md` `## Mistakes` ×1 (authoring prediction asserted, not executed —
caught by the per-copy authoring harness; the fix shown able to fail by the caught receipt).
The round's sourced-claim conjunct rests on S101 (opened this round; the knowledge entry the
claim lands cites it, alongside S097).

## Trend verdicts

- **expansion: improved** — knowledge entry `corpus/knowledge/witness-equivalence-rule.md` on
  ground the coverage map did not hold (the set-aware witness rule + its voidability analysis);
  S101 admitted on uncovered registry ground; the sealed held-out set itself is new corpus
  ground (14 authored copies across 10 distinct fault/equivalence classes).
- **quality: improved** — the round's own gate caught the frozen witness rule as voidable in
  both directions BEFORE any data run (amendment 6, probe battery 8/8); the authoring harness
  caught a mis-authored witness (setup-threshold vector) pre-commit; the gnu.org/TLDP
  duplicate-source rows were rejected rather than rowed; the controls receipt was minted at the
  amended rev and attests it byte-exact.
- **discernment: improved** — C1's r33 honest stop is discharged by a measured true, not a
  retry; the kill rule consumed exactly once; every rejection (live pins, duplicates, the r33
  stale pin) kept as a lesson row; v3 residue classes explicitly NOT adopted post-data and
  routed to r35 under the freeze-before-data discipline.

## SHONEN

- [~] SKILL.md decision tables — lane assertion (cold-read ledger `.ufo/evidence/round-21/coldread/ledger.json`); this round's records drift sections ride in the r34 wave's cold-read seats (routed re-crediting).
- [~] End-to-end domain task — the C1 measurement end-to-end: freeze → controls → sealed set → deciding run, receipts committed (`round-34/measure/`).
- [~] Executable without oral context — lane assertion (round-21 input-keyed monitor); wave context bounds are fully path-absolute.
- [~] No cross-domain bleed — lane assertion; connector seat scans sibling overlap this wave.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Installs

None this round (python3/bash/bwrap/curl only; the rejected gnu.org fetches are network
receipts, not installs). Prior-round note stands: jsonschema 4.25.1 via uv (r33, mte repair).

## Round shape and seats

One v2 wave (alternative shape), policy v2 band 64-128, validated exit 0: 64 seats, attack 52/64
= 81% (≥25% met) — roles: mutation-tester 28, reviewer 21, executor 7, scout 3, critic 1,
sentinel 1, revenger 1, connector 1, scribe 1. Content: 14 per-copy sealed-set attacks, 6
counter-mutation seats, 8 review/critic/sentinel/revenger attack seats, 7 measurement-only v3
residue probes (ride to r35 Holds), 4 panel-seed replays, 13 cold-read/all-four re-crediting
seats (routed from the r33 closure), 5 frontier/quality/audit seats. The §3 L2 floor is met
inside the single wave (connector, executors, scribes, scouts, reviewers, critic, sentinel,
revenger, mutation-testers); the L1 holds the canonical planner seat (validator-frozen
topology — `planner` is not a swarm role); bounded planning data-walks rode inline on the L1.
Wave-slot acquire first: the spec was validated (`ufo-swarm-wave.mjs run`, DISPATCH_EXIT=0)
before the taskCall was returned. **Zero dispatches from this session** (orchestrator contract):
- wave id: `round-34-w1`; seats: 64; grant line: policy v2, band 64-128, attack 52/64 = 81%,
  validated exit 0, one batched `task` call carrying the taskCall unchanged;
  taskCall JSON path: `/home/vgpnk/Projects/shokunin/tameshi-shokunin/.ufo/waves/round-34/dispatch-w1.json`
  (schema `ufo-swarm-wave-dispatch-v1`, `taskCall = {context, tasks}`, counts spawn 64 / total 64).
Round total: 64 wave seats (0 dispatched by the L1; dispatched by the orchestrator), 0 residual
calls; the L1's inline measurement work is recorded above. (R33 routed tally fix: r33's report
under-counted its dev seats — the r34 counts above are from the validated dispatch json.)

## Dead seats / refusals

None at report time — the wave had not been dispatched by the L1 (orchestrator-owned dispatch);
any dead seats are reported by the orchestrator's relay and appended at closure.

## Open L0 questions

None new. (Standing: the mcp.json rea pin rewrite remains the operator's; the pacman pause
stands; the orchestrator owns the wave dispatch and its seat-relay accounting.)

## Tooling note

The orchestrator dispatches `round-34-w1` from the returned taskCall; seat relays return tagged
`[seat <name>]` and are folded into the round-34 lesson (findings) or this report at closure.
Post-data findings cannot amend the frozen rule (kumitate r42); proven defects route to r35
under the freeze-before-data discipline.
