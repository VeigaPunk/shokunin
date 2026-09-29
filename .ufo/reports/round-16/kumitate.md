# kumitate — round 16

Lane `/home/vgpnk/projects/shokunin/kumitate-shokunin`. Axis move: **coverage**
— the round-15 pre-registration, executed as written. Round identity **round 16**;
report path `.ufo/reports/round-16/kumitate.md`.

## Decision

Round 15 retired `coverage` at its terminal value (19/19 × 50/50 ⇒ 10) and
pre-registered exactly one move for round 16: give the two successors their first
measurement, with the terms fixed *before* the measuring round. This round
implemented those terms as machine-derived quantities of the frozen proxy, so the
"before" is the unstructured state (declared, unscored) and the "after" is a
re-derivation by a tool any non-author can run:

- `coverage:script-layer = floor(10 × C1s/C1s_total × S_sections/S_members)`
- `coverage:runtime-layer = floor(10 × C1r/C1r_total × R_sections/R_members)`

where `C1s`/`C1r` are the layer's registry `yes` rows over its rows
(`scripts/proxy-check.mjs`'s own registry parse) and the section terms count only
members of the row's **declared** family (`sections[].inFamily === true`).

Measured, same tools both sides:

```
before  PROXY: MATCH (A=5 C=10 operability=8; C1=19/19 C2=50/50 coverage=10; pins=5 match)
after   PROXY: MATCH (A=5 C=10 operability=8; C1=19/19 C2=52/52 coverage=10;
        S=74/114 coverage:script-layer=6; R=60/98 coverage:runtime-layer=6; pins=5 match)
```

The successors read **6** and **6** against the retired parent's terminal **10**
— a drop of four points on each half, entirely from the honesty term the old
aggregate never measured. That is the shape kasegi's own lane states as its split
test (`kasegi-shokunin/SCORECARD.md:69-78`, cited as that lane's rule, not as
fleet policy — an independent connector pass checked the fleet SSOT and found no
such rule there). Operability was not touched: `A=5`, `C=10` (the round adds no
runnable file and no `- [` line; a checklist row would have been an operability
term in a coverage round), so `f_O = 15/18 ⇒ 8` and the lane's live axes are now
`operability 8`, `coverage:script-layer 6`, `coverage:runtime-layer 6`.

## The artifact

- `scripts/proxy-check.mjs` (1174 → **1560 L**): six new integer terms
  (`S_members S_sections R_members R_sections coverage_script coverage_runtime`),
  `--src DIR`, `SRC_NOT_A_DIR` fail-closed, `AXIS_ROWS` extended to four mapped
  rows, and a hermetic suite grown 55 → **71 cases**.
- `scripts/claims-check.mjs` (819 → **863 L**): an additive, exported
  `probeSections()` (one derivation, shared with `runCheck`) + a `main()` guard so
  the proxy can import it **in process** — never a subprocess, and no second walk
  of the origin tree. CLI stdout is byte-identical to the pre-edit capture; the
  suite is still 35/35.
- `SCORECARD.md`: two `### coverage:script-layer` / `### coverage:runtime-layer`
  definition sections with the frozen derivations, the stanza 11 → **17 keys**,
  two new `## Axes` rows, move-log rows, seven new `## Limits` entries, the
  round-17 pre-registration.
- New notes: `corpus/knowledge/layer-axes.md` (370 L, the contract a reusing lane
  reads), `corpus/lessons/round-16.md` (326 L) + their `corpus/README.md` rows
  (`C2` 50/50 → **52/52**).
- `SKILL.md` proxy vocabulary and `corpus/knowledge/executable-scorecard.md`
  (grammar, term table, fail-closed arms, the amended invariant, round-16 inputs).

Members, from the origin tree: `S_members=114` = `scripts/*.mjs` (72) + **all**
files under `scripts/*/` (42, recursive — a depth-1 count reads 38; the four extra
live in `charter-scribe/{prompts,systemd}/` and `lean-cargo/bin/`);
`R_members=98` = `crates/ufo-core-runtime/src/*.rs` (93) + `crates/ufo-cli/src/*.rs`
(5). Sections, from `node scripts/claims-check.mjs --json`: S 74 of 74 in-family
(S6 5 + S7 9 + S8 60), R **60** of 63 raw in-family (the 3 excluded are R9's
out-of-family sections `loop_driver_tests.rs`, `local_ship_tests.rs`,
`distill_tests.rs`, members of R2/R6/R7; `S_sections + R_sections = 134` of the
gate's 137).

## What the round found unplanned

1. **The numerator had to be member-only.** The frozen text says "the fraction of
   that layer's *declared* members whose member section the claims gate
   verifies"; the all-sections reading is 63/98 = 0.643, the member-only reading
   60/98 = 0.612. An independent critic lane found the 3 out-of-family sections;
   L1 reproduced it. The forecast's *number* was refuted; its integer was not
   (both read 6).
2. **The pre-registered fallback is refuted by measurement, not taste.**
   `C1_layer` is 1.0 on both layers while `V_layer` is 0.649/0.612 — the terms are
   not re-expressions of each other, and rounds 13–14 show them moving apart
   (`C1 18/19` beside `sections=90`). The file-level-residue alternative
   (`F_layer`) is therefore not needed, and with it the origin-walk it would have
   required for a *different* reason (see 3).
3. **The proxy stops being self-only, and the price is paid in the open.** The
   four legacy terms still never read the origin tree; the two layer terms read it
   once, in process, through the imported `probeSections()`, with
   `SRC_NOT_A_DIR` fail-closed (exit 2). Recorded consequence: the `Proxy
   recompute` checklist item now needs the origin tree, exactly as `cite-check`,
   `claims-check` and `surface-probe` already do. Recorded, not hidden, in
   `## Limits` and in the artifact's own header/`USAGE`.
4. **The successor pair cannot be landed blind.** The round-15 lesson's
   arithmetic would have sectionized `R1` alone: under the member-only numerator
   that is 68/98 ⇒ 6. The round-17 plan was recomputed before pre-registration
   (`R1`'s 8 + `R8`'s `native_dispatch_topology.rs` ⇒ 69/98 ⇒ 7).
5. **Two gate blind spots, measured.** (a) `cite-check` does **not** line-check
   lane-local script citations (`scripts/<tool>.mjs:<N>` resolves as class
   `self-doc`, rung `self`, kind `OK`): after `proxy-check.mjs` grew ~400 lines, a
   plain run reported zero findings naming it, so the 44 doc pins this round
   re-anchored were verified by symbol lookup, not by the gate — and 18 of the 44
   the auto line-map produced were wrong (a shifted endpoint is only valid where a
   block *moved* rather than was *replaced*), e.g. `RE_REGISTRY_ROW` 140-144 → 219,
   the `A` count 281 → 426, `DEFAULT_SELF` 170 → 174. (b) `cite-check`'s span
   scanner loses backtick alignment after a ``` fence (`findSpans()`
   `scripts/cite-check.mjs:338-350` pairs backticks over raw text and drops spans
   inside `findFences()`'s ranges `:324-336`; the fence line's three backticks
   shift that pairing by one for the rest of the document). Reproduced in a
   `git archive HEAD` copy, one construct per file: prose token with no fence →
   `UNRESOLVED`; prose token after a ``` fence → no finding at all; after a `~~~`
   fence → `UNRESOLVED`; fence content → untokenized for both markers (by
   design). A sibling lane measured the scale in one draft: 13 of 229 inline
   citations tokenized with ``` fences, 230 of 230 with `~~~`.
6. **Round 15 was never committed** — its process ended first, and its report
   claimed a `round-15` commit that did not exist. Recovery: the two artifacts not
   yet interleaved with round-16's edits (the `R11` census note and the round-15
   lesson) are the `round-15` commit `db61be0`; round 15's scorecard/log/skill
   text lands inside the `round-16` commit, and both statements are in the commit
   bodies. Precedent anchor for this move: `637d181` (round-14 close evidence).

## Verification

Wave 1 — **12 L2 subagents in one batched dispatch**, routed per the fleet map
(planner/connector `@m_lunamax`; executor/scout `@m_flash`;
reviewer/critic/labrat/mutation-tester/distiller `@m_zfl`), one writer per file:
`ExecClaimsExport`, `ExecProxyLayers`, `ExecScorecard`, `ExecAxisNote`,
`ExecLesson`, `ExecCorpusDocs`, `ExecSkill`, `ScoutLayerBoundary`, `CriticTerms`,
`ConnectorSiblings`, `DistillerHeads`, `PlannerR17`. Wave 2 — 3 more:
`ReviewLayerTerms`, `LabratLayerArms`, `MutateLayerTerms`.

Independent work that could falsify, and partly did:

- **Boundary** (`ScoutLayerBoundary`): rebuilt 114/98 from the tree with
  `LC_ALL=C`-collated lists; union 212 files / 211 unique basenames (one duplicate
  basename, `base.mjs`, inside the script layer), intersection empty; reconciled
  the recursive 42 against the depth-1 38 and named the four nested files.
- **Terms** (`CriticTerms`): six ranked attacks with measurements — the
  member-only numerator (landed), `C1_layer`-on-`V_layer` double penalty (recorded
  in `## Limits`, inactive today), the recursive denominator definition (recorded),
  floor placement and product monotonicity (refuted as an attack), the retired
  row's terminal 10 (recorded, not a work target), and the origin dependency
  (recorded with its failure mode).
- **Dedupe** (`DistillerHeads`): the successors are defined once in `SCORECARD.md`
  and restated by reference elsewhere; no duplicate member section across the 137
  gated sections; the prose-vs-machine vocabulary gap was closed with one mapping
  sentence in each definition section.
- **Cross-lane** (`ConnectorSiblings`): no sibling defines a layer/member-section
  term; kasegi's split test is a local rule (cited as such); kagi's
  "documentation-coverage score" adjacency note is reported, not absorbed; no
  contested scope in either new corpus artifact.
- **Plan** (`PlannerR17`): recommended and then corrected the round-17 move from
  the tree (`R1` 8 + `R8` 1 ⇒ 69/98 ⇒ 7; `R1` alone ⇒ 6; script `S2` ⇒ 82/114 ⇒ 7
  with four members needing new research; the operability arm cannot pay).
- **Mutation** (`MutateLayerTerms`): **7 of 9 mutants killed**; the two survivors
  (no fixture asserts `SRC_NOT_A_DIR` precedence; no fixture asserts an unresolved
  heading earns no layer credit) are named gaps, queued in `## Limits`.
- **Review/arms** (`ReviewLayerTerms`, `LabratLayerArms`): wave-2, dispatched
  against the landed tools — independent replay of all six terms from the tree,
  doctored-copy falsification, the round-14 replay, and 9 doctored stanza/axes/src
  arms. Anything the round cites as verified is either in the logs above or in
  these two transcripts (`history://ReviewLayerTerms`, `history://LabratLayerArms`).

Integration by L1 (the round's own tool work, not L2): re-pin `pin.proxy-check`
and `pin.claims-check` from live `sha256sum` after the last tool edit; re-anchor
44 doc pins and hand-correct 18 of them; add three `## Limits` bullets from the
wave-2 findings; recover the missing `round-15` commit.

Close evidence (lane HEAD after the `round-16` commit, pushed; report
committed+pushed in the main repo):

```
$ node scripts/round-gate.mjs --close
ROUND_GATE: CLEAN (round=16 lane=kumitate checks=13 errors=0 warnings=0)   # exit 0
$ node scripts/proxy-check.mjs
PROXY: MATCH (A=5 C=10 operability=8; C1=19/19 C2=52/52 coverage=10;
  S=74/114 coverage:script-layer=6; R=60/98 coverage:runtime-layer=6; pins=5 match)   # exit 0
$ node scripts/claims-check.mjs
CLAIMS: MATCH (rows=19 yes=19 notes=27 sections=137 adv=16)   # exit 0
$ node scripts/surface-probe.mjs --checklists
CHECKLIST: 10/10 pass   CHECKLIST_SKIPPED: 0   VERDICT: PASS
$ node scripts/surface-probe.mjs
SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)
$ for f in cite-check surface-probe round-gate proxy-check claims-check; do node scripts/$f.mjs --selftest; done
20/20 · 38/38 · ROUND_GATE_SELFTEST: 57/57 · PROXY_SELFTEST: 71/71 · CLAIMS_SELFTEST: 35/35
$ node scripts/cite-check.mjs
CITE_CHECK: DRIFT (files=54 tokens=4861 errors=14 warnings=76)   # all 14 in the two third-party
                                                                 # aggregator artifacts; 0 naming either edited tool
$ node scripts/proxy-check.mjs --src /nonexistent
PROXY: FAIL-CLOSED (SRC_NOT_A_DIR) --src /nonexistent is absent   # exit 2
```

Freshness: origin tree `93798be12` (round-15 log) → **`5725fa7d3`** during this
round; the sibling lanes' notes on the two new artifacts are read-only surfaces —
nothing outside this repo was written or pushed, and no upstream push is implied.

## SHONEN

`SHONEN.md` unchanged — still a shonen repo. None of its four boxes is claimed;
the honest state is "two successor axes with a first, machine-derived
measurement, one retired parent, operability still the ceiling, and three queued
repairs (the two mutation survivors, the `cite-check` fence defect) that no axis
integer reflects yet".

## L0 side channel

Nothing filed. The one candidate — "may a lane amend its own tool's stated
invariant (self-only → origin-reading layer terms) inside a coverage round?" — is
answered by the round-15 pre-registration itself, which named the origin read and
required it to be *priced, not assumed*; the price is in `## Limits`, the
fail-closed arm, and the checklist dependency. If the operator disagrees, the
rollback is one line of `## Planned` plus `SRC_NOT_A_DIR` → optional, and the
recorded evidence still stands.