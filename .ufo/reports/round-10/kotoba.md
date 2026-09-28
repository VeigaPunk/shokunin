# kotoba — round 10 report

Lane: `kotoba` (child repo `kotoba-shokunin/`, axes depth + consistency).
Landed commits, all pushed to `origin/master`:
`abef8aa` (round-10 move), `32e0d79` (lesson hash pin), `d49dfa5` (salt
correction from an L2 falsification). The aggregator lane also pushed
`778310d` (its r6 audit of this repo) into the same branch during the round.
Pre-round HEAD was `8e22a41`.

## Axis move — depth (planned at round 9)

Recorded ceiling at round 9: *"checklist execution is still lane-attested (no
external verifier)"*; the harness claim set existed only as hand-run recipes.

Landed: **`verifiers/verify_harness_claims.py` + `verifiers/baseline.json`** — a
committed drift detector over the two skill routers. `27/27 checks pass`, exit 0
on the live host (≈3 s); exit 1 on a perturbed baseline naming the perturbed
checks; exit 2 with an unreadable environment; exit 3 with no baseline;
`--self-test` → `0 failure(s) over 10 assertions`; fixture overrides
(`--omp-bin/--omp-db/--omp-sessions/--oc-log/--oc-bin/--baseline/--cwd`) so it is
testable without touching the operator's skill tree.

What it pins, per claim family:

| check family | values today |
|---|---|
| `omp.elf.template_*` | 273 B, sha256 `c1f03c8e248eb40e…`, recovered by byte anchor |
| `omp.db.*`, `omp.offered.*`, `omp.names.*` | 17 rows; 17 offered; 2 dangling dirs; 0 name≠folder; 0 missing |
| `omp.cache.*` | `keys_reproduced` 17/17, `verified_skills` 17, `misses` 0 |
| `omp.catalogue.*` | newest captured `<skills>` block 2026-09-28T21:47:06.212Z, **17/17 lines byte-equal to the cache**, 0 stale |
| `omp.descriptions.*` | over-cliff 17/17, unmodelled forms 0 (excluded, never guessed) |
| `oc.log.*` | `init_count_max` 18 == 17 root names + builtin; `<available_skills>` 0; `<skills>` 0; monotone |
| `oc.dup.*`, `oc.permission.*` | 3 roots both-sided (existing/duplicate split); 471/471 skill-permission lines allow |

Measured before → after, with the counting form:

| metric | before | after | evidence |
|---|---|---|---|
| harness claims executed by a committed artifact | 0 | 11 of 22 registry rows (see below) | `python3 verifiers/verify_harness_claims.py` |
| hand-run recipe blocks in the round-9 corpus file | 6 | 0 (each replaced by a check or a catalogue/grep the script runs) | `grep -n 'verify_harness_claims' corpus/knowledge/harness-router-models-round9.md` → 2 annotations on the 2 blocks |
| checks that can fail | — | 27, each with a perturbing proof (perturbed baseline / fixture worlds) | exit-1 run names the checks |
| planted-fault detection | — | 9/10 (the 10th is an equivalent mutation: `>-` trailing whitespace is discarded by the loader, so the key is identical) | `/tmp/round10/mutation-report.md` (scratch; summary in the artifact) |
| depth score | 8 | 9 | `SCORECARD.md` row, command inline |

Denominator: an L2 distiller built a deduplicated registry of the fleet's
harness claims — **22 rows, 21 machine-checkable in principle, 3 superseded**
(`/tmp/round10/claim-registry.md`; scratch). The verifier executes 11 of them
line-for-line: HC-01 render-path consequences, HC-02 truncator (via
`--self-test`), HC-03 keys, HC-04 cache coverage, HC-06 invalidation, HC-07 offer
gate, HC-09 discovery scope, HC-11 opencode gate counters, HC-13 duplicates,
HC-14/HC-15 counters. Five more were re-measured this round by lanes (freeze
ladder, loss metrics, activation counts, opencode name-mismatch source read, the
round-9 scope audit). One (HC-17: body-only edits change neither offer nor
render) still has **no runtime matcher measurement** and stays labelled
guidance — named in `corpus/knowledge/harness-verifier-round10.md` § Open gaps.

## The mechanism got a better authority, and a round-9 claim died

omp ships as a Bun single-file executable with **readable embedded JS**. Read
from the binary, the mechanism is no longer inferred:

```js
A8n: sha256(K7s ‖ 0x00 ‖ e.name ‖ 0x00 ‖ e.description)   // cache key
H7s: previewSkillDescription (ws-collapse; ≤100 verbatim; t[:99]; first
     [.!?] sentence if ≥40 chars and no ellipsis; else last-space + …)
ldl: accept iff one line, ≤160 chars, ≤12 words
nV.render = cache.get(key) ?? previewSkillDescription(...)
```

`K7s` is the whole 273-byte bunfs prompt `compress-description-<hash>.md` — the
routing-hint sentence **plus** `Skill: {{name}}` / `Description: {{description}}`
(placeholders hashed verbatim). Round 9 recorded only the 226-byte first line,
which reproduces **0/17** keys: the recorded recipe could not have detected
drift. Corrected in `corpus/knowledge/harness-router-models-round9.md`,
`SKILL.md` § Sources/§ Frontmatter craft and the new artifact.

Three lanes reproduced the corrected rule independently: the critic (verdict
"fails as documented, holds as mechanism"; the bare sentence → 0/17), a scout
(17/17, template bytes + sha256 identical; 39 SKILL.md files scanned; the freeze
census over 4107 catalogues shows signatures 3→5→11→17 with zero unexplained
lines), and an executor's own implementation (`omp_verify.py`: 17/17, and
`--baseline <repo>/verifiers/baseline.json` → 13 OK / 4 SKIP / exit 0, i.e. it
reproduced the landed repo's `omp.*` values from the host rather than re-reading
them). That executor also falsified a *live* `SKILL.md` sentence — the cache key
was described there as `sha256(prompt + name + ws-collapsed description)` — fixed
in `d49dfa5` (uniform ws-collapse reproduces 11/17 and invents staleness).

## Freshness re-measure inside the move

- db 17 rows, description lengths 44–98 (`sqlite3 -readonly`); main file 12288 B,
  `-wal` 0, `-shm` 3 — mtime remains a lower bound.
- Newest catalogue 2026-09-28T21:47:06.212Z, 17/17 cache; 4116 real `<skills>`
  blocks over 5924 session files (the raw literal count 8194 is contaminated by
  captured transcript text — documented so nobody quotes it).
- opencode: init histogram 15×1 16×141 17×34 18×14 (monotone in time), permission
  lines 471/471 allow via `permissions["*"]`, duplicates 1918 warns with 3 roots
  both-sided, `~/.claude/plugins/cache` and `~/.config/opencode/skill` absent.
- omp binary sha256 `55016ef5…`; `session_init` 4142 (round-9 range
  ~4032–4116); compression warns 10925.
- **Drift found in our own corpus:** round-9's template quote and its offer-gate
  root list (`~/.agents/skills` missing — 15 of 17 names live there; without it
  only 12/17 keys are discoverable). Both corrected with the evidence.

## Aggregator audit r6 — 9 defects, 9 closed (independent non-author review)

`778310d` landed `corpus/lessons/round-6-aggregator-audit.md` (audited HEAD
`8e22a41`, verdict **not conformant**) while this round was running. Its findings
were taken as ground truth rather than re-run, and every kotoba-owned defect was
closed inside this repo — ledger with per-item verification in
`corpus/lessons/round-10.md` § Closure ledger:

counts re-measured (`20 data rows`; `13/9/9/8` checklist boxes; dispatch
checklist 12 items in the artifact / 9 boxes in `SKILL.md`) → `SHONEN.md`
regenerated with a trailing newline · 8 dead `commit round-N` pointers → real
hashes (`1d93182`, `397b29c`, `4002b9f`, `a614927`, `3b029b8`) · 4 unindexed
files → indexed (`comm` diff now returns only the self-referential `README.md`) ·
`skill-activation-telemetry.md` "compression is a model call" → appended, named
correction · CLAUDE.md census 16 → 18 · source-length range re-based to 163–818
with its command · `SCORECARD.md` rewritten so every row carries
`score — command @ tree`, owned/advisory labels, a fractional rubric, and an
axis-name reconciliation (`consistency` declared a calibration sub-axis).

Routed back out: the aggregator's own round-5 minor-4 withdrawal (source char
counts reproduce exactly under ws-collapse — confirmed here), the `8c300ad`
non-lane git identity class (kumitate `7a4c9a0`, kagi `ea77bf0`), and the
`AXES.md`↔`MISSION.md` axis-set mismatch (raised on the L0 channel).

## L2 lanes — 14 in two batched `task` calls (floor 8)

| lane (agent class) | model bucket | deliverable |
|---|---|---|
| scout ×2 | `m_flash` | omp cache/key evidence (17/17, template hex, 39 files); opencode evidence (all round-9 numbers reproduced, `drifted=[]`) |
| executor ×2 | `m_flash` | independent `omp_verify.py` (17/17, interop 13 OK/4 SKIP vs the landed baseline); independent `opencode_verify.py` (5 checks, drift/exit-code proofs on synthetic hosts) |
| planner-class critic | `m_zfl` | key-rule falsification: holds as mechanism, fails as documented (0/17 vs 17/17); ufo precedence primed; CJK/`: `/non-ASCII all reproduce |
| reviewer | `m_zfl` | checkable-claim classification of `SKILL.md` (denominator work) |
| connector | `m_lunamax` | cross-axis sweep: no sibling verifier of this class; kagi/kengaku scripts are different artifact classes |
| sentinel ×2 | `m_zfl` | round-9 fact re-measure + catalogue census (4116 blocks, 17/17 newest, contamination warning); falsification lane on the verifier |
| distiller | `m_zfl` | 22-row deduplicated claim registry (21 machine-checkable, 3 superseded) |
| labrat | `m_zfl` | 8 synthetic SKILL.md fixtures + the 8 guard cases that became the parser's unmodelled-scalar exclusion |
| mutation-tester | `m_zfl` | 10 planted faults, 9 detected, 1 equivalent mutation named |
| simplifier | `m_zfl` | check-set redundancy audit |

## SHONEN

- [~] `SKILL.md` contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` (591 lines, ≤600 bound) — anatomy/decision tables, four checklists (13/9/9/8 boxes), 20-data-row anti-pattern table, Sources incl. `verifiers/`; counts re-measured at round 10 (aggregator r6 defect 1).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` round 10 — the verifier build + audit closure; round-5 fleet audit, round-7 dispatch audit of 53 prompt files (`ls .ufo/prompts/*-round-*.md | wc -l` → 53, aggregator r6 defect 7).
- [~] Instructions executable by an agent without oral context — pointer: round-7 blank-context reviewer (13 verdicts, zero questions); round 10 makes the harness half *executable* (`verifiers/verify_harness_claims.py`, 27 checks, 4 exit codes) rather than prose.
- [~] No cross-domain bleed (`PROVINCE.md` accurate) — pointer: aggregator audit adopted and its kotoba-owned defects closed here; its routed items and the sibling/agent-def/dispatch-prompt defects reported, not fixed; `PROVINCE.md` unchanged.

Verifier note: every check this round, including the five L2 verification lanes,
was lane-run — therefore `[~]`; one lane (the aggregator's r6 audit) was
non-author but audited the *previous* commit (`8e22a41`), not this round's work.

## Cross-domain evidence (routed, not absorbed)

- **Sibling lanes:** connector sweep — kagi's `corpus/*.sh` gates host telemetry
  (transcript/drift-pin/surface-census) and kengaku's scripts are benchmark
  runners; neither recomputes a skill-harness claim, so no duplication, no
  handover owed. Kengaku `LOG.md:11` cites `<available_skills>` plus prompt-size
  estimates but no counter this verifier computes.
- **Main repo (protocol lane):** its closure actuator is prose + one-off
  `python3 -c` snippets rather than a committed script; the artifact class is
  adjacent, not duplicated (`MANIFEST.json` + `PROTOCOL.md` step 4). Its round-10
  items (prompt-template fidelity 1/5, `report_of()` completing on file
  existence) remain operator-side; kotoba confirms the SHONEN-heading item from
  the child side (41/45 child reports lack it).
- **Operator surfaces:** `~/.agents/skills/{sekhmet,xbrd}` are dangling symlinks
  into a vanished port (`Projects/origin-work/ufo-fsd-alpha/ports/xbgst-codex/`),
  recorded as a baseline count; the shadowed `~/.config/opencode/skills/ufo`
  description hashes to a key absent from the cache, so root order is
  load-bearing (a flip would orphan ufo's row).
- **Fleet pattern:** git-identity breach class `8c300ad` (`shokunin
  <shokunin@local>`, historical/immutable) also present as kumitate `7a4c9a0`,
  kagi `ea77bf0` — reported for the aggregator/protocol ledger.

## Conformance / process notes

- Mission `shokunin-r10-kotoba-*` opened 2026-09-28T18:35 and this report lands
  well past two 450 s driver ticks; the lane worked continuously (14 L2 lanes,
  ~2 h wall including 20-minute lane tails), so no stale-lane action is
  requested — but the round is long, and the L2 lanes' tail (5 lanes >18 min) is
  the cost driver, not idling.
- Evidence pointers in this report are either committed artifacts or commands;
  the `/tmp/round10/` scratch (fixture, mutation, registry, independent
  verifiers) is summarised and explicitly not cited as closure evidence.
- Repo writes by other lanes this round: the aggregator committed `778310d` into
  `kotoba-shokunin` (its own audit artifact). No collision; it was integrated and
  indexed rather than reverted.
- `python3 -m py_compile` artifacts were removed before committing
  (`verifiers/__pycache__` deleted, not committed).