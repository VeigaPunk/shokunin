# kumitate — round 13 of ≤1024 (fleet-2)

**Lane:** kumitate-shokunin · **cwd** `/home/vgpnk/projects/shokunin/kumitate-shokunin`
**Axes:** operability + coverage (orchestration/tooling).
**Round move:** one axis-move, **coverage**. **Score 8 → 9** on the frozen proxy
(`A=4 C=9 operability=8` unchanged).
**Repo commit:** `round-13` (lane), pushed to `github.com/VeigaPunk/kumitate-shokunin`.

## Axis-move and measurement

Frozen proxy (`SCORECARD.md` → `### coverage`): `coverage = floor(10 × C1/C1_total
× C2/C2_total)`; C1 = registry rows matching `/^\| (S|R)\d+ \|/` whose note cell
starts `yes`; C2 = `corpus/README.md` rows naming a corpus note over corpus note
files. The family standard is round 12's, unchanged: **every** member of a family
named at internals level — a `## ` section headed by that member's own path with
≥1 anchor in that member's own file and ≥1 symbol verbatim in it.

| Term | Before (r12 close) | After (r13) | Command |
|---|---|---|---|
| C1_total | 18 | **19** (the partition adds one registry row) | `node scripts/proxy-check.mjs` (counts the rows) |
| C1 | 16/18 (S7 `no` at 9 of 69 named; R11 `no`) | **18/19** (S7 = 9-member cluster `yes`, new S8 = 60-member remainder `yes`; R11 stays `no`) | `node scripts/proxy-check.mjs` → `C1=16/18` → `C1=18/19` |
| C2 | 43/43 | **45/45** (`knowledge/remaining-scripts-census.md` + `lessons/round-13.md`, each with a README row) | `grep -c '^\| `\(knowledge\|lessons\)/' corpus/README.md` → 45; `find corpus/knowledge corpus/lessons -name '*.md' \| wc -l` → 45 |
| coverage ⇒ score | `floor(10 × 0.888)` = 8 | `floor(10 × 18/19)` = **9** | `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=4 C=9 operability=8; C1=18/19 C2=45/45 coverage=9; pins=4 match)`, exit 0 |
| residue (diagnostic) | 150/211 ≈ 0.711 | **195/211 ≈ 0.924** (the census names 45 basenames no earlier note carried) | walk of `corpus/**.md` + `SKILL.md`, basename containment over 212 files / 211 unique basenames |

`17/19` ⇒ `floor(8.947)` = **8** — i.e. the S7 half alone (the partition without
the census) would have scored nothing, which is why the round did both moves.

A and C are untouched: `find … \| wc -l` → 4 runnable artifacts, `grep -c '^\s*-
\[' SKILL.md` → 9 executed checklist items.

## The pre-registered plan, executed — with one measurement-forced substitution

Round 12's `## Planned` offered (1) partition `S7` into `S7a`/`S7b` (17/19 = 0.894
⇒ still 8) or (2) name the 60-member remainder. The round did **both**, and the
substitution is not cosmetic:

- **`S7a`/`S7b` are invisible to the proxy.** `RE_REGISTRY_ROW =
  /^\| (S|R)\d+ \|/` (`scripts/proxy-check.mjs:139-143`, counted `:255-265`) only
  sees `\d+` rows. A copy with `| S7a |` reports `PROXY: DRIFT … C1_TOTAL_DRIFT
  term=C1_total declared=19 computed=18` exit 1. So the split had to be **two
  top-level rows**: `S7` = the 9-member route-probe cluster, `S8` = the 60-member
  remainder.
- **The plan's arithmetic was re-derived, not assumed:** `S7` alone → 8, `S7`+`S8`
  → 9, and the un-partitioned `17/18` route is now unreachable by construction.

## What landed

- **`corpus/knowledge/remaining-scripts-census.md`** (new, 854 L) — registry
  family **S8, 60 of 60 members** named at internals level, one `## ` section per
  member. Contents: the partition statement and the id-grammar reason for it; a
  60-row `| member | L | class |` census (29 suites + 23 tools + 3 shims + 4
  assets + 1 doc, **54,874 L** by `wc -l`) with its re-derivation commands; the
  S1–S6/S7 boundary arithmetic (114 script-layer files = 45 + 9 + 60); the five
  top-level `.sh` scripts the frozen universe cannot reach; the
  `scripts/ufo-l0-monitor.test.mjs` trailing-newline caveat (1,345 vs 1,346); and
  the two-arm member-completeness probe printed with its real output.
- **`corpus/knowledge/route-probe-cluster.md`** (rewritten) — **S7, 9 of 9
  members**: title, `## Scope` and membership block state the partition;
  `## What each probe answers` is replaced by nine per-member `## ` sections
  (`probe-ufo-route-health.mjs`, `probe-token-plan-shared.mjs`, `-kimi.mjs`,
  `-models.mjs`, `probe-redact.mjs`, the two colocated suites, `atomic-write.mjs`,
  `fake-omp.mjs`); a probe section and rewritten limits; the round-12 topic
  sections, decision table and fenced citation ledger are untouched.
- **`SCORECARD.md`** — registry rows (S7 9-member `yes`, new S8 `yes`), 19
  families, the disjointness paragraph, C1/C1_total/C2/C2_total + re-pinned
  `pin.cite-check`, `## Axes` coverage 8 → 9 with a round-13 paragraph, three
  move-log rows, the round-12-plan review + round-14 plan, and four new limits.
- **`corpus/README.md`** — 2 rows (C2 43/43 → 45/45), the cluster row's
  parenthetical, and both gap bullets (script layer split; live-surface coverage
  now one uncovered family).
- **`corpus/lessons/round-13.md`** (new), **`SKILL.md`** (census pointer bullet,
  cluster bullet, the live `CITE_CHECK:` reading), **`LOG.md`** (round-13 entry),
  **`scripts/cite-check.mjs`** (defect repair — below).

## Evidence (round close)

```
$ node scripts/proxy-check.mjs
PROXY: MATCH (A=4 C=9 operability=8; C1=18/19 C2=45/45 coverage=9; pins=4 match)  # exit 0
$ node scripts/proxy-check.mjs --selftest
PROXY_SELFTEST: 55/55 pass   (10 fail-closed arms observed)   VERDICT: PASS       # exit 0
$ node scripts/cite-check.mjs
CITE_CHECK: DRIFT (files=47 tokens=4530 errors=14 warnings=75)                     # exit 1
$ node scripts/cite-check.mjs --selftest
20/20 cases passed (hermetic)   VERDICT: PASS                                      # exit 0
$ node scripts/surface-probe.mjs
SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)                    # exit 0
$ node scripts/surface-probe.mjs --checklists
CHECKLIST_SKIPPED: 0 · CHECKLIST: 9/9 pass   VERDICT: PASS                         # exit 0
$ node scripts/round-gate.mjs --selftest
ROUND_GATE_SELFTEST: 57/57 pass   VERDICT: PASS                                    # exit 0
$ grep -c '^\s*- \[' SKILL.md            → 9      (unchanged; A = 4 unchanged)
```

Citation gate: `errors=14`, **all** inside the two third-party aggregator
artifacts (`corpus/lessons/round-6-aggregator-audit.md` 2 × `LINE_OOR`;
`corpus/lessons/round-8-aggregator-box3-coldrun.md` 12). Per-file, the two new
notes are clean: `remaining-scripts-census.md` → `OK=605 FRAGMENT=69
REF_OWNER_AMBIG=0 errors=0`; `route-probe-cluster.md` → `OK=270 FRAGMENT=45
REF_OWNER_AMBIG=0 errors=0`.

Member probes (printed inside each note with their output):

```
S8 census  (60 members) → HEADINGS: 60  MEMBERS: 60  DUPLICATE: 0 / MEMBER_PROBE: 60/60 ok   exit 0
S7 cluster (9 members)  → HEADINGS:  9  MEMBERS:  9  DUPLICATE: 0 / MEMBER_PROBE:  9/9 ok    exit 0
drop-one control (rename one member heading):
  S8 → MEMBER_PROBE: 58/60 ok  exit 1      S7 → MEMBER_PROBE: 7/9 ok  exit 1
  and on the same tree: node scripts/proxy-check.mjs → PROXY: MATCH … coverage=9  exit 0
```

The last line is the round's honest boundary: the proxy cannot see note contents,
so `yes` cells rest on the probes + reviewers + gate, not on arithmetic.

## Claims falsified inside the round (calibration record)

1. **A member sheet inside the round mis-transcribed one member** (a g5 file,
   58 L, listed in g6 with `scripts/ufo-state-retention.mjs` 2,284 L missing; the
   group total proved it — 6,929 against the declared 9,155). Caught by the
   member probe (`DUPLICATE_HEADING` + `MISSING_HEADING`), fixed by its author,
   and the landed note verifies 60/60 against the origin-derived census.
2. **`wc -l` vs real lines on one member.** `scripts/ufo-l0-monitor.test.mjs` has
   no trailing newline: 1,345 by `wc -l`, 1,346 by `awk 'END{print NR}'`; the
   column keeps `wc -l` and the note states both readings — the table sums to the
   command it names.
3. **`scripts/cite-check.mjs` could die before printing a verdict.** A backticked
   `Object.prototype` member name (`toString`, `valueOf`, `constructor`,
   `hasOwnProperty`) in any doc walked the prototype chain of three token-keyed
   map literals (`ALIASES`, `SHORTHAND_PATHS`, `GENERATED_POINTERS`) and threw
   `TypeError [ERR_INVALID_ARG_TYPE] … Received function toString` out of
   `path.join` — the process died, so no `CLEAN`/`DRIFT` was printed. Found by an L2
   executor, **reproduced by L1 before the repair** (HEAD file + the new fixture:
   `node:path:1339` crash, exit 1, no verdict), fixed by making the maps
   null-prototype, covered by a hermetic case that kills the un-fixed file and
   passes after (`20/20 cases passed (hermetic)`). `pin.cite-check` re-pinned
   `8a6b5c9d…` → `a11ead17…`; A and C unchanged, so no proxy term moved.
4. **`REF_OWNER_AMBIG` can rebind a ref to the wrong file.** 17 short `:N` refs
   across the two new notes were ambiguous, and **three** of them
   (`scripts/ufo-swarm-wave.test.mjs:158/573/980`) had been rebound to the SUT
   `scripts/ufo-swarm-wave.mjs`, which also fits — the `test(...)` names live in
   the suite. All 17 were rewritten to cite the intended file explicitly; both
   notes now report zero ambiguity.
5. **The census note's `SCORECARD.md` line refs moved** when this round edited
   that file (S7 row `:103` → `:108`, the plan `:213` → prose, R11 `:114` →
   `:120`) — re-pointed after landing, before the commit.
6. **The frame's own claims were corrected against measurement** before landing:
   "six members already named by full path" → eleven (15 by basename), and the
   class histogram → 29 suites + 23 tools + 3 shims + 4 assets + 1 doc.

## Cross-domain (reported, never absorbed)

- **Origin tree** (read-only): HEAD moved `daa371583` → `4f34e7dab` with 35 dirty
  paths at the round-13 reading. None of the 69 census targets is among them, and
  the sentinel verified no target file carries a 2026-09-28 mtime (newest
  2026-09-27 20:17) and all 69 are git-tracked — so the 875 refs in the two notes
  are pinned to a revision the origin was not editing.
- **`scripts/lean-cargo/README.md:77` claims** `measure.sh` wipes `sccache` when
  `RESET_CACHE=1`; that token exists nowhere in `measure.sh`, and the wipe at
  `measure.sh:66` is unconditional. Owner: origin tooling lane. Found by an L2
  executor while documenting the member, reported, not edited.
- **The five unattributed top-level shell scripts** (`dev-verify.sh`, `gates.sh`,
  `self-iter.sh`, `smoke.sh`, `ufo-night-watchdog.sh`) sit outside the frozen
  counting universe (`scripts/*.mjs` + `scripts/*/`) and belong to no registry
  family; recorded as a definitional limit of this lane's proxy rather than
  absorbed into S8.
- **Sibling lanes** (connector): two Kake references to `charter-scribe` inside
  its site-probe context, generic `README.md`/`config.json` basename noise, and
  no sibling using family-member enumeration — the coverage convention stays
  lane-local. The shared `/home/vgpnk/projects/shokunin/corpus` tree does not
  exist, so the sweep covered the five sibling lane trees + their `SKILL.md`.

## L2 concurrency — 16 lanes, one batched dispatch

planner/connector `@m_lunamax` · executor/scribe/scout `@m_flash` ·
critic/reviewer/sentinel/labrat `@m_zfl`. Landed: a design/acceptance matrix
(planner); an independent rebuild of the 60-member set from the origin
(`comm -3` against the working list **empty**, `wc -l` total 54,874, disjointness
vs S1–S6 proven) (scout); seven executor slices into `/tmp/kumitate-r13/parts/`
(six S8 groups balanced by `wc -l` + the S7 addendum, each with an anchor ledger
whose every line and symbol was re-read/re-grepped); the S8 non-member prose
frame + README/lesson/SKILL drafts (scribe); a 5/6-arm falsification with the
`S7a` invisibility, the 19-row stanza drift, the `AXES_DRIFT`, the `C2_DRIFT` and
the two blind-spot arms measured (critic); two reviewer passes (A: 290 rows /
289 OK / 1 truncated-ledger-text, 315 symbols 0 missing, 29/29 sections judged to
describe their own member; B: 314 rows / 0 wrong-line / 0 missing symbols, 30/30
sections); labrat: 69/69 parse, 804 symbols 0 missing, 10-member side-effect
audit; sentinel: both trees read-only, no same-day target mtime, zero
credential-shaped hits, no lane-owned listener/unit; connector: the cross-lane
sweep above. L1 re-verified every ledger with its own pass (428 anchors + 506
symbols), assembled both notes, repaired the 17 ambiguities and the one citation
error, ran both probes and all gates, and landed every edit.

Critic's landing objection (recorded, not hidden): `proxy-check.mjs` cannot read
notes, so the cheapest fake — flip two cells, update the stanza and the axes
integer — still passes all arithmetic. The round's answer is the two-arm member
probe plus the drop-one control showing it fires while the proxy does not; turning
it into a `--claims` mode of the proxy is **pre-registered for round 14**, not
slipped into this round.

## Residuals / limits (recorded, not hidden)

- **R11 is the only uncovered family** (42 runtime `.rs` + 5 CLI `.rs`, 0 of 47
  named). Landing it saturates C1 at 19/19 ⇒ coverage 10, which this scorecard
  will not claim while the file-level residue is 0.924 and the family standard is
  lane prose rather than a gate.
- **The probe is a documentation check, not a gate** — it reads the note, not the
  fleet; `cite-check --symbols` shows a symbol exists in the cited file, not that
  the sentence around it is faithful. That is what the reviewer lanes are for.
- **A census is not an operational contract.** None of the 69 members was
  executed beyond `node --check` / `bash -n` / `systemd-analyze verify`; they are
  fleet-mutating tooling.
- **The partition's boundary is a stated rule**: both helpers count as S7 members
  because the cluster's suites stage and import them; the narrower `probe-*` glob
  is 7 files / 2,651 L and is recorded alongside.
- Operability's gap is unchanged and out of this lane's reach (no CI/schedule leg
  it may own; the host's schedulers belong to other identities).

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited
      sources — decision table `SKILL.md:12`, 16 enforced anti-patterns `:448`,
      executable checklist `:514-537` (9 items, `CHECKLIST: 9/9 pass`), the
      watcher paragraph + the round-12/13 pointer bullets `:396-411`.
- [x] At least one end-to-end domain task executed and logged in LOG.md — two
      families (S7 9 members, S8 60 members) named at internals level from source,
      with 875 re-resolved refs, two reviewers adjudicating the ledgers, and the
      probes' output embedded in the notes; `LOG.md` round-13 entry.
- [x] Instructions executable by an agent without oral context —
      `node scripts/surface-probe.mjs --checklists` executes all nine items;
      each note carries the commands that reproduce its member-completeness claim.
- [x] No cross-domain bleed (PROVINCE.md still accurate) — origin drift, the
      `lean-cargo/README.md` claim defect and the sibling-lane boundary are
      reported with owners, never edited in place; `PROVINCE.md` unchanged.

## Next planned move (round 14)

**Coverage, 9 — pre-registered, one move only.** In preference order: (1) R11
coverage (the last family; lands at 19/19 ⇒ 10, i.e. saturation, so it must be
paired with a retirement/split decision recorded in the same round); (2) the
`--claims` mode that moves the member probe into `scripts/proxy-check.mjs`
(operability: A 4 → 5, `f_O = 14/17 = 0.823` ⇒ still 8 — it closes the loudest
hole two critics found and needs its own pin, cases and before/after row); (3) the
frozen `C` regex tightening (a definition change that moves no number today;
must be declared in the round whose *before* state is measured against it).

## L0 side channel

No new operator decision is required this round. Round-10's question (adopt
`round-gate.mjs` at the driver level) and round-11's (adopt the
`kumitate-proxy-v1` claim block fleet-wide) remain open in
`/home/vgpnk/projects/shokunin/.ufo/l0-questions.md` and are not re-filed.

**Report written by:** kumitate L1, round 13. **Cited lane commits:** the
`round-13` commit (below) and its close-evidence commit — both ancestors of lane
`HEAD`, which is what `round-gate` re-checks.