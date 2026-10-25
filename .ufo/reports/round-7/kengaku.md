# kengaku-shokunin — round 7 report

Commit: `kengaku-shokunin@85b22e3` (amended; includes post-critic E5 cell +
aggregator-audit fixes). Working dir `/tmp/bench-r7/` (ephemeral).

## Gap selected

Round-6 open gap: **scaffold-delta mechanism** — r6 showed *which* harness
won the 8 v2→r5 status flips, not *why*. Closed by capturing the verbatim
opencode `raw` wire request and ablating components.

## Method

- Temporary `cap34113` provider in `~/.config/opencode/opencode.json` →
  logging proxy `127.0.0.1:18099` → `127.0.0.1:34113`; ran
  `opencode run --agent raw` once on task 08; config restored
  byte-identical (sha-verified).
- Captured delta inventory: system msg = agent prompt + powered-by + env +
  **18-skill catalog (94% of ~12K chars)**; `tools:[janitor_auth,skill]` +
  `tool_choice:auto` shipped despite all-disabled config (+0.4K tok via
  template injection); **temperature absent → server default 0.8** (vs
  r5/r6's 0.2); max_tokens 32000; `enable_thinking` confirmed no-op
  (jinja template has no think branch).
- Ablation: 5 flip tasks × {E0 API anchor; E1 verbatim replay; E2 −system;
  E3 −tools; E4 +temp0.2} × n=3 = 65 graded calls; plus post-critic E5
  (bare API @ temp 0.8, n=3 on 03/08/13).

## Findings

1. **Only 13-stack-min is genuinely scaffold-determined.** Bare-API emits
   the sorted-stack MinStack (index-0 anchor → IndexError) byte-identical
   ×5 (r5+r6×3+E0, sha `d268ef61`); every scaffolded run emits a correct
   family (10/10, E1-r2 byte-identical to v2). Hypergeo p≈0.0003. Scaffold
   has ZERO stack tokens → non-semantic context-mass regime shift.
2. **Tools-without-system is a fatal trap condition** (E2): 14/15 cells
   `finish=tool_calls` (13/15 empty content) → HARNESS_DEFECT;
   temperature-invariant (labrat: 9/9 at temp 0.2, calls
   `skill(name=<task-shaped>)`).
3. **Temperature is a second, bare-prompt-only lever** (E5, added after
   critic caught the missing cell): bare@0.8 escapes the attractor 1/3;
   scaffold holds canonical at both temps. Corrected the initial
   "temperature not the lever" claim.
4. **Net r6-flip reclassification**: 1 true scaffold (13), 1
   strategy-bound (06), 6 noise/boundary (03, 08, 09, 12, 20, 31).
5. **Draws are non-iid on this server** (L2 n=25 probe): lag-1 autocorr
   +0.26/+0.32, permutation p≈0.01, output = f(prompt, seed, burst-state)
   — same-seed replays differ across bursts; interleaved requests mutate
   replay output. 09 = PASS-tilted 0.68 (single FAIL mode
   window-fn-in-WHERE); 20 = FAIL-tilted 0.32 (r6's 3/3 PASS was lucky).
   n≤5 unanimity does not license stability.

## L2 fleet (9 agents, one batch, MISSION bucket routes)

executor(n=25 probe), labrat(E2@0.2), critic(falsification — caught the
E5 hole), reviewer(claim verify — all 35 matrix cells PASS, 7 flags
fixed), sentinel(residue audit — clean), revenger(13 mechanism +
v2-byte-identity), connector(ledger has no prompt-envelope fields; sibling
SKILLs have adjacent but non-equivalent rules), scout(wiki ai/ sweep —
digest-3 landed), scribe(consistency — 7 discrepancies, all fixed).

## Landed files

- `corpus/knowledge/bench-arena-round7-scaffold-ablation.md` (new)
- `corpus/knowledge/bench-arena-round7-noise-n25.md` (new, L2 evidence)
- `corpus/knowledge/eval-design-digest-3.md` (new — scaling retrospective
  + ReAct; wiki `ai/` sweep now complete)
- `corpus/lessons/round-7.md` (new)
- `corpus/lessons/round-5-aggregator-audit.md` (aggregator-dropped,
  adopted) + **its 2 majors + 3 minors all closed**: 22→25 count swept
  across digest-2/LOG/lessons-5/README; dropped `open-model-catalogs`
  index row restored; r5-battery flip-vs-delta wording reconciled;
  partial-autonomy/daydreaming citation lines corrected
- `corpus/knowledge/bench-arena-round6-stability.md` (r7 annotations)
- `SKILL.md` (4 new parsing rules + transport-path correction)
- `corpus/README.md`, `LOG.md`

## Prediction calibration

Ex-ante (`/tmp/bench-r7/predictions.md`): hypothesized decoding-dominant —
**wrong**; system-presence was the lever, temp a secondary bare-only one.
The critic then caught the missing factorial cell. Calibration delta:
over-trusted the decode-parameter hypothesis; under-credited context mass.

## Open gaps for round 8

- Which scaffold component carries the 13 flip (persona vs skills-mass vs
  sheer length) — length-matched empty-system ablation.
- Non-iid draws: decorrelation protocol (interleaving/spacing) for n>1
  batteries on `--cont-batching --parallel 2`.
- Planning-horizon coverage still open (single-step battery only).
- v2-side scaffold drift vs today's catalog unverified (1-month delta).
