# chousa — round 46 report (hyaku run 6, in-session L1)

Lane: `/home/vgpnk/Projects/shokunin/chousa-shokunin` · lane branch `master`
Base: `6e2630a6343948b3fe5bf299901207a0619ad949` · freeze:
`c2f0e9d100c0d46633a6277b2fd51d2ac99678eb` · landing:
`c294484f736dca099b8cce6e978c31dad51095dd` · receipt commit (lane tip):
`72a0f2bcd2d635259866efd567eb00541f5a5aab`

Declared claims (frozen in `corpus/evidence/round46/claims.md` before any seat
scored, with their do-nothing controls): **C1 operability** (the lane's lowest
non-retired axis, 3/10) — inference grounding becomes an executable check, a
capability acquisition; **C2 calibration** — the gate registry covers the
executable verifiers outside the frozen name pattern; **C3 depth** — the
evidence-pool versioning theme adopted from the shokuknow package as two
knowledge entries. Routed from the round-45 closure as D7 and D8.

## Work performed

- **C1 — `tools/inference-ground.py` + `corpus/evidence/round46/c1-count.py`.**
  The tool screens a knowledge entry's `#### Inference` section: every bullet
  must cite an `S###` source and carry a grounding token (backticked/quoted
  phrase, or a figure) that appears verbatim in a span of a source it cites, or
  is the designator of a cited document. Six declared fixtures
  (`corpus/fixtures/inference-ground-r46/`, three positive, three junk) plus a
  CANARY leg (renamed copies) and byte pins. Evidence: `c1-count.py` →
  `POSITIVE_PASS=3/3 JUNK_KILLED=3/3 CANARY=pass C1=PASS` exit 0 in
  `corpus/evidence/round46/measure-after.txt:9-15`; forges in
  `controls/c1-controls.txt` (always-exit-0 `0/3`, citation-only `1/3`,
  name-oracle `CANARY=fail`).
- **C2 — registry extension.** `corpus/evidence/round46/c2-count.py` enumerates
  entry points from three legs (every file under `tools/`, the round-45 counter
  pattern, and every existing `*.py`/`*.sh` a SCORECARD or claims cell names) and
  requires each inside a `## Gates` row. Five rows added to `SKILL.md` covering
  thirteen historical instruments, the round-46 tool, its three counters and the
  span builder. Evidence: `measure-after.txt` → `REGISTERED=73/73
  UNREGISTERED=0 C2=PASS`; ten forges refused in `controls/c2-controls.txt`
  (prose paste, six-cell, no-`exit`, after-heading, fenced, `.pyc` suffix,
  comment-abutting, multi-line comment) with one positive control.
- **C3 — two entries, five rows, eleven spans.** `corpus/knowledge/
  evidence-pool-versioning-r39.md` and `…-r39-amendment-2026-10-23.md`, rows
  S085–S089 in `corpus/SOURCES.md:95-99` (bound by document: staged S120–S122,
  S127, S128 → lane S085–S089), eleven quotes with ±80 chars of context in
  `corpus/evidence/round46/spans/`, rebuildable by `build-spans.py --check`
  (`SPANS_ROWS=11 STALE=0`). Evidence: `measure-after.txt` → both modes
  `ENTRIES=2/2 CITES_BOUND=5/5 QUOTE_ROWS=11/11 QUOTES_IN_SPAN=11/11
  QUOTES_IN_ENTRY=11/11 CAPTURE_BOUND=11/11 SPAN_IDS=5/5 SPAN_CONTEXT=11/11
  REF_ID_UNBOUND=0 REF_BOUND=2/2 C3=PASS`; the `--lane-only` forge in
  `controls/c3-controls.txt` passes lane-only and is refused by the default mode
  at `CAPTURE_BOUND=0/11`.
- **Frontier / curation.** Five sources opened this round from the on-disk
  campaign captures (no fetch): S085 FEVER dataset page, S086 FEVER ACL paper,
  S087 the Zenodo record, S088 the AVeriTeC dataset page, S089 the AVeriMaTeC
  arXiv HTML. The lesson's `## Gate` records each URL, the access date
  `2026-10-25` and a ≤25-word located quote (`corpus/lessons/round-46.md:231-315`).
  Quarantine: the adopted S086 URL is slice row `chousa round4 S116`
  (`payload-absent`); hand-checked — all three register quotes are present in the
  capture once the PDF column interleave is removed — verdict **present**, row
  adoptable (`.ufo/waves/round-46/w1/ScoutQuarantineOverlap.md`).
- **Understanding.** `SKILL.md` checklist item "Observation, inference and
  unknown stay separate" is now runnable (the tool command is inline);
  `corpus/QUALITY.md` gains criterion **66**; `corpus/README.md` gains two
  coverage-map rows and the round-45 "not adopted" clause is superseded in place.
- **Mistakes mined.** `corpus/lessons/round-46.md` `## Mistakes` holds fourteen
  classes with evidence, captured-by and a fix shown able to fail (junk-leg
  `!=0`→`==1`; fixture pins; unsound registry numeral escape; fence/comment/
  suffix forges; span-path read oracle; misroot; anchor drift; fabricated staged
  quote; attribution drift; before-state label; entailed span leg; filename
  oracle; post-freeze instrument edits; co-occurrence legs).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: claims + three counters + controls (no claim work) | `LOG.md` "Round 46 — 2026-10-25", C1/C2/C3 bullets | `c2f0e9d1` |
| tool, entries, rows, spans, Gates rows, coverage map, SKILL | C1, C2, C3, frontier bullets | `d09fc8e7` |
| wave-2 corrections: registry designator leg, C2 fence/comment/boundary, span paths, context spans, entry narrowings, map + anchor fixes | instrument-revision bullet; lesson mistakes 1–14 | `3807537d` |
| fence-above-Inference crash fix, CANARY leg, S084 remainder arithmetic, instrument limits | lesson `### Named limits` | `e50b388a` |
| wave-2 finish: Zenodo role correction, entry pointers, Gates rows into the table, registry table glue, C2 eight-cell rule, C1 dedupe, C3 span-id/context legs, shipped forges, four-tree before receipt | lesson `## Wave-2 corrections and record errata` | `45ede9c2` |
| final measurement receipt over `45ede9c2` | — | `524ef466` |
| Gates verdict maps corrected against observed exit contracts | C2 bullet | `0e2d7b8f` |
| checklist wiring + QUALITY 66 | Understanding bullet | `29793159` |
| C2 receipt positive control labelled | C2 bullet | `158ab27c` |
| multi-line comment scan, refreshed receipts, lesson sentence | C2 bullet; lesson errata | `c294484f` |
| receipt over `c294484f` | — | `72a0f2bc` |

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 operability | `python3 corpus/evidence/round46/c1-count.py` | `TOOL=absent POSITIVE_PASS=0/3 JUNK_KILLED=0/3 C1=FAIL` exit 1 (`controls/c1-before.txt`, tree A = base `6e2630a6` + this round's counters and fixtures) | `POSITIVE_PASS=3/3 JUNK_KILLED=3/3 CANARY=pass C1=PASS` exit 0 | `c294484f` (`corpus/evidence/round46/measure-after.txt`) |
| C2 calibration | `python3 corpus/evidence/round46/c2-count.py --list` | `ENTRY_POINTS=71 (tools=7 counters=50 named=69) REGISTERED=55/71 UNREGISTERED=16` exit 1; pristine base archive `ENTRY_POINTS=68 (7/47/66) REGISTERED=55/68 UNREGISTERED=13` (`controls/c2-before.txt` trees A–D) | `ENTRY_POINTS=73 (tools=8 counters=50 named=71) GATES_ROWS=35 REGISTERED=73/73 UNREGISTERED=0 C2=PASS` exit 0 | `c294484f` |
| C3 depth | `python3 corpus/evidence/round46/c3-count.py` (and `--lane-only`) | `ENTRIES=0/2 CITES_BOUND=0/5 QUOTE_ROWS=0/11 C3=FAIL` exit 1 (`controls/c3-before.txt`) | both modes full, exit 0 (`CAPTURE_BOUND=11/11` default, `skipped` lane-only) | `c294484f` |

Verdicts: **C1 improved** (frozen predicate met at every revision; the D7
entailment class is **not** closed — see the trend section), **C2 improved**
(limit: mention-based, not dependence-based), **C3 improved**. No axis is
harmed. The round-1 operability scale (a narrow 3/3 archive observable) is
unchanged at 3.

## Report extras — round shape, waves, seats

**Shape: v1, two waves, 64 seats.** Wave 1 (build + first falsifiers) 32 seats —
reviewer 9, scribe 7, scout 5, executor 4, critic 3, mutation-tester 2,
connector 1, sentinel 1; 32/32 reports. Wave 2 (falsify) 32 seats — reviewer 20,
critic 4, mutation-tester 3, scout 3, sentinel 2; **31/32 reports**: seat
`CritC2Scope` produced no report and is recorded dead, not replaced (its subject
— C2's mention-vs-dependence scope — was independently hit by `RevC2TagCount`,
`RevRerunC2` and `CritC2Framing`). No residual task call was needed. Both waves
validated under `scripts/hyaku/ufo-wave-policy.json` (band 32–64) and were
dispatched as one batched `task` call each from the emitted `taskCall`
(`.ufo/waves/round-46/{w1,w2}-dispatch.json`). Planner = the L1 (validator
rejects `planner`); bounded planning data-walks rode the scout/connector seats.
Specs, dispatch payloads, registries and all 63 seat reports are committed under
`.ufo/waves/round-46/`.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

**Inherited state (named, not touched):** the three modified JSON paths
(`.ufo/waves/round-40/w1/swarm-registry.json`,
`.ufo/waves/round-41/w1/swarm-registry.json`,
`corpus/evidence/round41/receipts/cells/cells.json`) are unchanged, hashes
identical to the round-45 record (`RevInherited.md`).

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain`
shows no chousa/round-46 path at the fleet root (`RevMisroot.md`); one seat's
draft was misrooted and moved byte-exact into the lane before it could persist
(lesson mistake 6).

**Tool installs:** none. No pacman transaction was run.

**Open L0 questions:** none added this round. Still open and unanswered: the
fetch-scope question `8d77e6c1` (so this round made no external fetch), the
round-43 inherited-tree question, the round-44 round-shape question.

## Sources & frontier

Census command (both ends):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
— round start **exit 0** (84 rows, five W04), round end **exit 0** (89 rows, the
same five W04), rows `S001`–`S089` contiguous, malformed rows 0, duplicate ids 0.

- **Rows before → after: 84 → 89** (+5). By tier: A +5 (all five are primary for
  their scope); B/C unchanged.
- **Rows touched old→new:** S085 recheck `180d` (staged) → `365d` (curation, a
  build-stamped page, logged in the lesson); the five rows are new, status
  `mined`; no existing row's status or `used-by` was changed. The five staged ids
  (S120–S122, S127, S128) were NOT appended — the campaign's numbers collide with
  held lane ids S082–S084 on different documents, so the rows were re-bound by
  document and written from the captures.
- **Frontier rows advanced:** two coverage-map rows
  (`corpus/README.md:1065-1066`) on ground the map did not hold; the round-45
  "pool-versioning amendment is not adopted" clause is superseded in place.
- **Assimilation:** one theme, two entries, five rows, per §10; the campaign tree
  was read only and no campaign tool was run.

## Trend verdicts

- **expansion — improved.** Two admitted knowledge entries on ground the
  coverage map did not hold, each `source:` citing a `mined` row opened this
  round; coverage map +2 rows; five new tier-A sources; no sibling lane holds
  this ground (`ConnectSiblings`), and six lanes already practise capture-digest
  binding row-by-row, so the entries state a fleet habit rather than discovering
  one.
- **quality — improved.** Three counters pass over a `git archive` of the
  landing (`measure-after.txt`); each was attacked and hardened (fence-blind
  bullets, filename oracle, unsound registry escape, fence/comment/suffix rows,
  span-path oracle, multi-line comments), every fix shown able to fail in
  `controls/`; the two entries were narrowed sentence by sentence by two critic
  seats and the Zenodo identifier inversion was corrected; QUALITY 66 added.
- **discernment — unchanged pending the outside check.** A seat this lane
  dispatched is still the lane. Wave 2's attacks are the strongest internal
  signal (the D7 entailment residual, C2's mention-based set and the C3
  co-occurrence legs are named, not hidden), but the non-author spot-check that
  decides discernment is the closure's.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** — 9-row decision table, 8 error rows, the checklist now carries the inference-ground command, `GATES_ROWS=35`; `RevShonen` box 1 HOLDS (all knowledge citations resolve). Pointer: `.ufo/waves/round-46/w2/RevShonen.md`.
- [~] **At least one end-to-end domain task executed and logged** — r9 recipe re-run CLEAN on all three archives, but the r25 battery's third pointer (`drift-r12`) is 11/12 since round 32's deliberate capture change and the baseline was never re-pinned; inherited, reported, **not fixed** (out of round scope). Pointer: `.ufo/waves/round-46/w2/RevShonen.md` S1.
- [~] **Instructions executable by an agent without oral context** — the cited gate command passes (`PASS (275 cases, 0 skipped)`), and the round-46 checklist item is now runnable with its exact command; three of six checklist items still carry no command (named, pre-existing). Pointer: `SKILL.md:69-70`; `RevShonen.md` box 3.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — PROVINCE unchanged; 61/61 knowledge titles in province; the scope-refusal gate's selftest cases 86–91/112–119/124 still pass. Pointer: `RevShonen.md` box 4.
