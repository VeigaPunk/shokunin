# kumitate — round 14

Lane `/home/vgpnk/projects/shokunin/kumitate-shokunin`. Axis move: **operability**
(8 — the lower of this lane's two owned axes). Report path
`.ufo/reports/round-14/kumitate.md`; round identity **round 14**; `SHONEN.md`
unchanged (still a shonen repo: promotion needs the checklist's four boxes and
none is claimed here).

## Decision

Round 13's `## Planned` pre-registered three candidate moves and named option 2 —
"move the member probe into a gate so a `yes` cell is re-derived from the notes" —
as the operability one. That is the move that ran, because operability is the
lowest axis (8 < 9) and because option 2 closes the hole both the round-12 and
round-13 critics measured: `scripts/proxy-check.mjs` reads the registry's fourth
cell as a string (`:263`) and never opens the note, so a renamed member section
still read `PROXY: MATCH … coverage=9` exit 0 in round 13.

Two deviations from the forecast, both measured, both recorded:

1. It landed as a **separate artifact**, not a mode inside `proxy-check.mjs`. The
   frozen `A` term is a **file count** (`find … | wc -l`,
   `scripts/proxy-check.mjs:281`), so a mode in an existing file moves no term —
   the plan's `A=4 → 5` for that placement is refuted by the definition it was
   written against. A separate artifact also keeps the proxy's self-only
   arithmetic free of origin-tree I/O.
2. `C` moved 9 → 10 (the forecast said "C unchanged"). The gate needs an
   execution path, and `surface-probe --checklists` runs it.

## The artifact

`scripts/claims-check.mjs` — contract `kumitate-claims-v1`, 791 L, zero deps
(node: builtins only), read-only, exit 0/1/2/64, 12 finding kinds, 35-case
hermetic suite, sha256 `d0f95fa051687a8235678d4b212351c04d562abece394ae7727aa9bf763cb188`.
For each covered row it re-derives: the note(s) the cell names, one member
section per file (a `## ` heading whose first backticked token is path-like), a
live own-file anchor, a verbatim symbol, and the declared member count when the
cell names one. Contract, arms, anchor semantics and limits:
`corpus/knowledge/member-claims-gate.md`.

## SHONEN

`SHONEN.md` is unchanged this round; the promotion checklist is not claimed.

## Before → after (frozen proxies, same commands both sides)

| term | before | after |
|---|---|---|
| A (`find . -path ./.git -prune -o -type f \( -name '*.mjs' -o … \) -print \| wc -l`) | 4 | **5** |
| C (`grep -c '^\s*- \[' SKILL.md`) | 9 | **10** |
| `f_O = (A+C)/(A+C+3)` | 13/16 = 0.8125 ⇒ **8** | 15/18 = 0.8333 ⇒ **8** |
| C1 / C2 (`grep -c` + `find … \| wc -l`) | 18/19, 45/45 ⇒ coverage 9 | 18/19, **47/47** ⇒ coverage **9** |

The integer holds at 8 by arithmetic, not by accident: `x/(x+3) ≥ 0.9` needs
`A+C ≥ 27`, i.e. 12 more honest items. The move is recorded as `f_O`
0.8125 → 0.8333 and the axis is walked, not inflated.

## Evidence (all re-run by L1 before publication)

- `node scripts/claims-check.mjs` → `CLAIMS: MATCH (rows=19 yes=18 notes=26
  sections=90 adv=16)` exit 0, 0.13 s. 9 section-form rows / 90 member sections
  (S6 5, S7 9, S8 60, R3 2, R4 3, R6 2, R8 3, R9 4, R10 2); advisories exactly
  9 × `ROW_NO_SECTIONS` + 4 × `MEMBER_COUNT_SUSPECT` + 3 × `SECTION_FILE_NOT_MEMBER`.
- `--selftest` → `CLAIMS_SELFTEST: 35/35 pass` / `VERDICT: PASS` exit 0;
  `--row S8` MATCH sections=60; `--row Z9` → usage exit 64; `--src`,
  `--scorecard`, `--self` absent → fail-closed exit 2; `--json` totals == text.
- **Drop-one arms on a lane copy**: renamed S8 member heading →
  `SECTION_FILE_UNRESOLVED row=S8` `CLAIMS: DRIFT` exit 1; deleted S8 section →
  `MEMBER_COUNT_DRIFT row=S8 declared 60 members, found 59 distinct sections`
  exit 1; on the same copies `node scripts/proxy-check.mjs` (claims-check moved
  out to hold the frozen A=4) → `PROXY: MATCH (A=4 C=9 operability=8; C1=18/19
  C2=45/45 coverage=9; pins=4 match)` exit 0. The compensating check is the gate,
  not the proxy.
- `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=5 C=10 operability=8;
  C1=18/19 C2=47/47 coverage=9; pins=5 match)` exit 0; `--selftest` →
  `PROXY_SELFTEST: 55/55 pass` exit 0.
- `node scripts/surface-probe.mjs --checklists` → `CHECKLIST: 10/10 pass` exit 0.
- `node scripts/cite-check.mjs` → `CITE_CHECK: DRIFT (files=49 tokens=4557
  errors=14 warnings=75)`: **zero errors in this lane's own prose**; all 14 sit in
  the two third-party aggregator artifacts.
- Independent re-derivation: the round's census lane rebuilt all 19 rows with its
  own probe — 0 differences (heading order, resolved file, anchor-candidate
  counts, symbol verdicts, family membership) and the same two drop-one outcomes,
  plus fidelity runs recording which narrower readings would have produced false
  findings (`--anchor qualified` → 17 false `SECTION_NO_ANCHOR`; naive
  tokenizer → 3 false `SECTION_NO_SYMBOL`).

## Falsifications that changed the artifact or the record

1. **A ghost note passed.** The first landed revision raised `NOTE_MISSING` only
   for the explicit `knowledge/<stem>.md` form, so `yes — ghost-note-that-does-not-exist`,
   a bare `yes` with no em dash and a nested-path spelling all read `MATCH` exit
   0. Found by the executor-review lane, reproduced by the critic, fixed (a part
   asserts a note when it is the token, token + `: …`, or a path; the aggregate
   finding is guarded). All three spellings now `DRIFT` exit 1.
2. **`--row Z9` was exit 2** (fail-closed) where the dispatched contract said
   usage 64 — caught by two lanes, reclassified.
3. **The drop-one harness matched the note's own documentation** of the round-13
   control and reported a false green; the arm now mutates a line-anchored heading
   and proves the byte delta before running the tool.
4. **17 false anchor misses** under a backtick/extension-limited scanner (the
   runtime notes and the S8 `.timer` section write plain parenthesised refs).
5. **`\|` in a members cell** shifts the row and drops S7 from the covered set;
   the splitter is escape-aware by rule.
6. **One added line to `proxy-check.mjs`** shifted 28 cited line numbers and made
   three corpus mentions of its previous sha256 read as `PIN_MISMATCH`; cites were
   re-pointed arithmetically and superseded hashes described instead of pinned.
7. **The proxy suite's literals were coupled to the fixture file count** (adding a
   fifth pin moved fixture `A` 4 → 5): 20 expected strings, 4 constants and the
   one `AXES_DRIFT`-on-removal case were re-derived, not fudged.

## Limits (recorded, not hidden)

Topic-form rows (S1–S5, R1, R2, R5, R7) stay prose: only note existence and
`NOTE_FOREIGN` are checkable there, and the critic's cheapest surviving fake is
exactly that (reduce S1's note to one token → `MATCH` exit 0). Cross-row
repointing shows as a warning spike (`sections=145 adv=76`, still `MATCH`). The
gate checks shape — live anchors, verbatim symbols — never sentence truth. The
mutation lane's 9/10 "survivors" were re-read as harness misses rather than
coverage claims, and the suite's arm coverage was strengthened with three cases
(unknown-row usage, symbol threshold, liveness boundary). Full list:
`SCORECARD.md` `## Limits`.

## Close

`node scripts/round-gate.mjs --close` → `ROUND_GATE: CLEAN (round=14 lane=kumitate
checks=13 errors=0 warnings=0)` exit 0 (lane HEAD `dffbf0e` + the close-evidence
commit, pushed; this report committed+pushed as `5fa216c`). `--round 14` →
`CHECKLIST: 10/10 pass` and `--tracked` → `CLEAN (checked=12)`.

Mid-close correction, recorded rather than smoothed: the aggregator lane committed
`corpus/lessons/round-9-aggregator-corpus-verdict.md` (`93b0567`, a third-party
artifact it owns) into this checkout after the round commit and without a
`corpus/README.md` row, so `C2_TOTAL` moved 47 → 48 and the stanza drifted
(`C2_TOTAL_DRIFT declared=47 computed=48`). The repair follows the rounds 8/9/11
precedent for this exact seam — a README row for the third-party note, `C2` 48/48,
coverage unchanged at 9 — instead of rewriting the tool's claim; the sibling's
commit rode this lane's push (`dffbf0e..93b0567`).

## Cross-domain (reported, not absorbed)

Origin HEAD moved `4f34e7dab` → `f65ee4b3d` with 35 dirty paths at the round
reading; no registry target has a 2026-09-28 mtime (correctly scoped max
2026-09-27 20:10, `proposal.rs`) — a sentinel lane's "target mtimes today" alarm
came from `.ufo/`, `clean-ephemeral/` and `clean-siblings/` paths and is recorded
as mis-scoped. Sibling lanes carry analogous gates (kagi `claim-ledger.sh cells`,
kotoba `verify_*`, kake `probe-delta.mjs`); no sibling uses a member-enumeration
convention, so the family standard stays lane-local.

## Next (pre-registered in `SCORECARD.md`)

Round 15: coverage — **R11** (42 runtime `.rs` + 5 CLI `.rs`, 0 of 47 named) ⇒
C1 19/19 ⇒ 10 = saturation, so the same round must declare the split
(`coverage:script-layer` vs `coverage:runtime-layer`) rather than slip it in; the
alternative single move is a paragraph-level arm in `claims-check` (operability,
`A+C` 15 → 16, still ⇒ 8).