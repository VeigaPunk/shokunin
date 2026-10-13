# kumitate round-8 closeout — operability axis-move

**Axis.** operability (owned pair: operability + coverage, per `MISSION.md`
fleet-2). Lowest axis at round open: operability **0** (A=0 runnable artifacts,
C=0 executable checklist items). Coverage was 5.
**Move.** Land the repo's first runnable artifact — `scripts/cite-check.mjs`,
a read-only, zero-dependency citation re-verifier — repair every citation it
falsifies, and make the corpus index complete.
**Repo `HEAD` at open:** `7a4c9a0`. **Source tree:** `ee907f1cf` (ufo-fsd-alpha).

## Gate (raw)

```
$ node scripts/cite-check.mjs
CITE_CHECK: CLEAN (files=33 tokens=2026 errors=0 warnings=48)     # exit 0

$ node scripts/cite-check.mjs --selftest
28/28 cases passed
VERDICT: PASS                                                     # exit 0

$ node scripts/cite-check.mjs --src /nonexistent ; echo $?
cite-check: fail-closed — --src /nonexistent is missing              # exit 2
$ node scripts/cite-check.mjs --self <empty-dir> ; echo $?
cite-check: fail-closed — empty scan set under <empty-dir>           # exit 2
$ node scripts/cite-check.mjs --bogus ; echo $?
cite-check: unknown argument: --bogus                                # exit 64 (usage)

$ node scripts/cite-check.mjs --json | head -c 200
{"schema":"kumitate-cite-check-v1","src":"/home/vgpnk/Projects/origin-work/ufo-fsd-alpha",…
```

Pins: 28 collected / 28 ok / 0 mismatch / 0 unknown. Orphan refs 0. Index 8124
src files + 39 self + 267 fleet, with `node_modules/ .git/ target/ .ufo/`
pruned (the `.ufo/` prune alone keeps 18 cited basenames unique — measured in
`/tmp/kumitate-r8/ambiguity.md` §5.2).

## Before → after (same tool, same flags, same roots)

Measured in-repo by stashing the round's doc repairs (`git stash push -- SKILL.md corpus/ LOG.md`),
running the final tool, restoring. Raw JSON: `/tmp/kumitate-r8/before-real.json`
vs `/tmp/kumitate-r8/run4.json`.

| Metric | Before (HEAD `7a4c9a0` docs) | After |
|---|---|---|
| errors | **22** (18 `SYMBOL_OFF_LINE`, 3 `UNRESOLVED`, 1 `LINE_OOR`) | **0** |
| warnings | 46 (42 suffix-resolved, 1 runtime-hint, 1 ambig, 2 symbol-miss) | 48 (46 suffix-resolved, 1 runtime-hint, 1 ambig) |
| orphan refs | 260 | 0 |
| rev pins unknown | 0 | 0 |
| tokens resolved | 1661 OK | 1738 OK |

Warnings are non-blocking by design: a suffix/basename resolution is a real hit
with an under-specified citation, and the runtime/host-config classes cannot be
verified from the source tree at all.

## Drift repaired (each verified at the source line before and after)

`GateDecision` `gate.rs:11`→`:15` in three docs (SKILL, `loop-driver`,
`native-judge-pipeline`); `permits_advance` `:447`→`:448` ×2 (round 6 fixed
three sites — these two survived); `publish_guarded` `:127`→`:124` ×2;
`ldd_dry_round_{dispatch,judge}_phase` `:117`/`:457`→`:112`/`:428`;
`LoopStateView` `:331`→`:327`; `HonestyBrake` `:97`→`BoundaryStop` enum
`:319-322`; `validate_header` `:247`→`:243`; `clamp_honest_baseline_vector`
`:22`→`:21`; `native_seats.rs:218-233`→`:218-230` (overshoot past a 230-line
file); `judge.rs:410`→`loop_driver_judge.rs:410`;
`run_root_alias_mutation_hook` `:482`→`:445`; four survivor-mutant line refs →
their name lines (`:6504/:630/:7038/:7070`); `local_ship_tests.rs:25/:42`→
`:31/:50`; CLI exit map `main.rs:1848-1860`→`1841-1860`;
`GODSPEED_EVIDENCE_MARKER`→`EVIDENCE_MARKER` (the real const, `godspeed.rs:10`);
`validate_native_` (line-wrapped token) → `validate_native_measurement`;
`LOCAL_COLLAPSE` → `LOCAL_COLLAPSE_SENTINEL` (`live.rs:45`, use `:254`);
`scripts/ufo-sighting/` is a 224-line FILE ×2; `config/ufo.json (:1348-1355)`
and `:7043/:7073` given their real owners; `omp_role_chains.rs` → generator
pointers (`build.rs:117`, `execution_profile.rs:572`).

**Pin typology (parent-verified, corrected mid-round).** `44a3c781…` is a
sha256 CONTENT pin that still matches (`sha256sum scripts/fleet-dispatcher.mjs`
= `44a3c781eacf…`) — not a git rev; `b18e0274d` is a valid commit 296 behind
HEAD with the dispatcher `git diff --stat` byte-empty across that range. Bare
`rev <hex>` wording was re-typed `sha256` at the two ambiguous sites
(`reconcile-and-cycle.md:3`, this repo's `LOG.md` r6 line), and cited pins are
now resolved self→src→fleet (a single-root check yields 6 false MISSING).

## Coverage half of the move

`SCORECARD.md` created (AXES contract: axes + scores + evidence pointers +
planned + retired, on frozen proxies). `corpus/README.md` coverage map
20/30 → **31/31** rows — the five round-7 notes plus five lesson files, with
five lesson rows re-pinned from unresolvable `commit round-N` to real shas
(`45b4ed3`/`efe19da`/`e0f5ca7`/`e748e44`/`eca3d14`), and `Known gaps` re-cut
(the round-7 defects are filed, not reproduced). `corpus/lessons/round-7.md`
written; the round-7 `LOG.md` entry backfilled.

Scores: operability **0 → 2** (`f_O=1/4`), coverage **5 → 7**
(`floor(10 × 0.778 × 1.0)`). Operability stays low on purpose: one artifact, no
CI/schedule, and the new Working-rules command is a bullet, not a GFM task
item, so the frozen C proxy does not credit it.

## L2 fleet (13 lanes, two batches, one batched call each)

Batch 1 (10): CiteSpec (planner — 252-line contract), SkillCiteCensus (599
citation rows), CorpusCiteCensus (4915 tokens / 923 line pins, 24/24
acceptance checks), AmbiguityMap (108 cited basenames; the `.ufo`-prune and
`RUNTIME_STATE_HINTS` hazards), CiteCheckImpl (executor — built and self-tested
the tool), RoundDrafts (scribe — scorecard/log/README drafts), CiteDriftFalsify
(critic), CitationAudit (reviewer — 28/30 pass, 6.7% drift, 3 new drift sites),
SiblingOverlap (connector — no sibling implements this; kagi `drift-pins.sh` is
the precedent), ToolScope (sentinel — 5 binding requirements, all adopted).
Batch 2 (5): ReadmeMapVerify + DocFixVerify (5 doc repairs re-verified OK),
ToolYagni, ToolMutant, ToolReaudit (phase-2 on the landed artifact).
Parent verified every repaired line against source; the two round-7 corpus
findings that survived earlier audits (`permits_advance :447`,
`native_seats.rs:218-233`) were caught only by the new tool.

## Falsifications worth keeping

- Critic (independently): the round's framing "citation drift is the biggest
  operability gap" is **FALSIFIED-AS-STATED** — 14/15 of its sampled citations
  were OK and the one drift was an *authoring* error, not drift-on-write; the
  more damaging missing artifact is an invocation surface. Round-8 answered
  that by landing the gate *plus* the SKILL.md working rule; the residual
  criticism (no CI/schedule mandate) is recorded in `SCORECARD.md` `Planned`.
- Reviewer audit: 30 sampled claims → 28 PASS / 2 FAIL (6.7%), both fixed.
- Sentinel re-audit of the artifact is in flight at close (phase-2 lane);
  the phase-1 requirements (R1 write/exec census, R2 no content echo, R3
  argv-array git only, R4 fail-closed exit 2, R5 exclusion reach) were adopted
  as binding before the build.

## Adjacency (reported, not absorbed)

`fleets/registry.json` lane→model routing is claimed in-domain by kasegi and
by this province's round-1 audit — unresolved, left to the integrator. The
`ufo-credential-screen.mjs` policy seam touches kagi's secret hygiene; the
`membrane-seal write` argv defect (round 5) still has no owning repo. None
absorbed here.

## Limits (honest)

The tool verifies *citations*, not claims: a well-cited wrong statement passes.
Suffix/`AMBIG` warnings remain (46/48), `PIN_UNTYPED` 20 pins read as bare hex
without a declared kind, and the corpus's interpretive prose is unchanged. The
tool is manual — nothing schedules it; `SCORECARD.md` round-9 makes that the
next move.
