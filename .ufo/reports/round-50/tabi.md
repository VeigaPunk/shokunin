# tabi — round 50 report (Windows host)

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tabi-shokunin`
(branch `master`). Baseline `a9b47d6a1ea2a2f649c0177dac90dd5e992b9274`; freeze
`2febf9b23cfd6d2b7f9ce6de145c5edf1b4a1c46`; amendment 1 `2604c1d984dcc1d0daba87ba29d75393ed44fa87`;
amendment 2 `5c7019944eee9c6bae56f076765685bb8ba1865f`; C2+C3 data
`196367606e51417f27165ceec5c4fb0db3734a62`; C1 data `1ea714f5a39452bb39d61404b7d87e2a27fc4d6a`;
C1 correction 1 `bceb21140583e1a4126c681b1ca2e691b6485a15` (**cited measured revision for C1**);
green receipt `f3364aaa9ad7612f7fe154bbcbfead1612de3527`; integration `ed701bf7e7483dbb2cfcc2639d6e425ea487680e`;
selfassessment receipts `ea11da958a9b8279203cda760a73b8129ac1a082`. Axes at start: adjacency 8
(lowest), others 9; saturation 8 / window 3; the r49 capability row restarted the window (round 50 =
position 1), nudge inactive — the lowest-axis obligation applies (C1 works adjacency).

## Work performed

- **C1 (adjacency, lowest owned axis)** — the r46→r49 regression-gate re-bind, one generation on:
  round-open red control measured with the inherited v9 meter at the baseline (exit 1, **24
  findings** — 11 lanes' heads advanced, kasegi/kengaku/mado provinces changed bytes, kotoba's
  browser-ground line set restructured; receipt `.ufo/waves/round-50/controls/c1-meter-v9-red-at-round-open.json`,
  taken before any lane write). audit-r50 + delta-r50 regenerated at ONE fresh snapshot; kotoba's
  three BG-hit lines moved one line down with text byte-verbatim (a non-BG chousa row inserted
  between audio and game-dev-2d), dispositions carried by exact whole-line quote match, **0 new
  adjudications**; one tsukuroi head race routed through the frozen correction flow (raced receipt
  committed); meter v10 (const/comment/schema retarget of v9, selftest 16/16, committed 62-line
  diff) GREEN at the correction revision.
- **C2 (coverage — capability extension, the r49 planned residual, sourced: S153 re-opened
  byte-identical this round)** — the r3 journey model over the webview2 surface: `scripts/webview2-cdp-loopback-round50.mjs
  --journey` (frozen at amendment 2, sha `2152d292…`) drives a 3-page loopback HTTP fixture A → B → C
  over the pages' OWN anchor clicks with `Page.getNavigationHistory` at C and a real
  `Page.navigateToHistoryEntry` back hop to the B entry; per-step URL/title/PNG pins; the
  invocation-bound nonce rides a `#nonce` marker on every fixture page; Edg/156.0.4314.58 identity;
  keyed teardown sweep 0; evidence `corpus/evidence/round50/webview2-journey/` (receipt + 4 PNGs);
  counter `webview2-receipt-r50.mjs` green 0 findings on the committed bytes; the r49 counter refuses
  the r50 receipt with 4 findings. Two committed red receipts carried the pre-data amendments: the
  page-target race (`controls/c2-first-live-run-red-target-race.json`) and the history-model
  misprediction (`controls/c2-journey-history-model-red.json` + `controls/c2-model-red-pngs/`) — the
  MEASURED surface truth (the initial data: page occupies history slot 0) is now the committed model
  and a lesson Mistake.
- **C3 (operability — the r49-closure D3 carry-in, adopted exactly as the closure suggested)** — a
  versioned counter (`webview2-receipt-r50.mjs`) grades a missing pinned runtime as the DECLARED
  could-not-evaluate class `runtime-pin-host-drift` under `couldNotEvaluate` (never a finding);
  folder-present-without-exe stays the hard `runtime-msedgewebview2-absent` finding; new
  receipt-internal `runtime-identity-mismatch` check; 13-case hand-declared fixture selftest 13/13 at
  the data revision, with the d3-asis case pinning the REAL removed runtime (passing on this host,
  where the folder is absent) and deterministic with-exe/without-exe probes covering both runtime
  branches on any host; the counter's own draft defect carried by a committed red/green pair.
- **Carry-in D1/D2 (corrections of record, append-only)** — the SCORECARD erratum block re-measures
  the D1 drift from committed bytes (line-based `grep -c` is **0 at baseline / 1 at tip** — the
  residual sentence is line-wrapped across lines 84-85; the revision-stable join+squeeze form reads
  **1 at baseline / 2 at tip**) and names D2's true position (S160 sits **between S158 and S159**,
  not "after S159"; the substantive requirement WAS met). This round's own registry insertion was
  positioned after the S160 row with its position named explicitly.
- **Carry-in L0** — `tabi | round-44` L2-floor stays open, routed around (fifth round; L1-inline; no
  wave-settled clause in any predicate).
- **Fresh-start ruling honored** (section 7): the last three REJECTED closures (r42, r43, r47) were
  re-read before declaring; refused classes ruled out — no nonce-relabeled/synthetic-receipt counters
  (the r50 counter pins committed-byte digests, requires the nonce echo on the data: page AND the
  fixture pages, identity equal to the runtime folder's version tail, sweep 0, and ships 13
  hand-declared refusal fixtures with exact-match findings); no wave/seat claims; no
  reasoned-not-measured after-states (every after-state is an instrument output at a named revision;
  both design corrections were forced by live red receipts, not reasoning); each claim's red is the
  do-nothing state and its green requires the round's work.

## Landed changes (all tied to LOG.md's round-50 entry)

| Commit | Change |
|---|---|
| `2febf9b2` | freeze: claims.json (3 claims, frozen predicates + kill rules, freshStartNote, frozenDigests), meter v10, runner r50, counter r50 + 16 fixture files, round-open controls (meter red 24; the r49-counter D3 reds: selftest 0/8 today + both committed r49 receipts exit-1-with-only-that-finding), census START exit 0 |
| `2604c1d9` | amendment 1: the runner's page-target poll (first live run red receipt committed; runner digest re-pinned; fixtures re-authored; counter selftest 13/13 re-run) |
| `5c701994` | amendment 2: the journey history model corrected to the measured surface truth (model-red receipt + 4 PNGs committed; runner/counter/fixtures/claims re-pinned; selftests re-run) |
| `19636760` | C2+C3 data: the journey evidence tree (receipt + 4 PNGs), counter-green receipt, r49-counter cross-refusal receipt, data-time selftest 13/13, runner stdout receipt |
| `1ea714f5` | C1 data: audit-r50 (16 rows = 10 unchanged + 6 sibling-absent) + delta-r50 (12 lane + 16 line rows) at one fresh snapshot |
| `bceb2114` | C1 correction 1 (tsukuroi head race; raced receipt committed) |
| `f3364aa` | C1 GREEN receipt (meter v10 exit 0 / predicate true / 0 findings at `bceb2114`) |
| `ed701bf7` | integration: SCORECARD round-50 block + erratum (D1/D2/D4) + capabilities row, lesson `corpus/lessons/round-50.md` (Gate + 6 Mistakes + census stamps), LOG entry, knowledge note `corpus/knowledge/webview2-journey-round-50.md` (notes 65 → 66), corpus/README note row + round-50 section, PROVINCE round-50 line, census END exit 0, check-sources clean rows=160, duplicate-row catch record, staged S153 re-open bytes |
| `ea11da95` | selfassessment receipts (one EPERM-crashed run kept and named + the completed re-run: verdict=failed mismatches=1 — the standing m3 stale-index class) + lesson dated appendix |

## Before → after measurements

- **C1**: `node .ufo/waves/round-49/counters/c1-adjacency-host-v9.mjs --rev a9b47d6a… --repo <lane>
  --fleet <fleet> --json` → exit 1, predicate=false, **findingCount 24** (control, round open) →
  `node .ufo/waves/round-50/counters/c1-adjacency-host-v10.mjs --rev bceb2114… --repo <lane> --fleet
  <fleet> --json` → exit 0, predicate=true, **findingCount 0**, counts {roster:16, mapRows:16,
  auditRows:16, deltaLanes:12} — measured at `bceb2114` (receipt committed at `f3364aa`). Selftest
  16/16; `grep -cE '^\|…S…\|' corpus/SOURCES.md` 160 → 160 (see Sources & frontier).
- **C2**: `git ls-tree -r --name-only <REV> -- corpus/evidence/round50 | wc -l` → **0 at baseline →
  5 at `19636760`**; counter on the committed bytes → exit 0, predicate true, **0 findings**,
  couldNotEvaluate [] (measured at `19636760`); cross-refusal: the r49 counter → exit 1 with **4
  findings**; `--path-selftest` 6/6.
- **C3**: `node .ufo/waves/round-49/counters/webview2-receipt-r49.mjs --selftest
  .ufo/waves/round-49/counters/webview2-receipt-r49-fixtures` → exit 1, **0/8**, every case polluted
  with `runtime-msedgewebview2-absent` (control at the freeze) → `node
  .ufo/waves/round-50/counters/webview2-receipt-r50.mjs --selftest
  .ufo/waves/round-50/counters/webview2-receipt-r50-fixtures` → exit 0, **13/13** (measured at the
  data revision, receipt committed at `19636760`); draft-counter red/green pair committed
  (`controls/c3-counter-selftest-draft-counter-red.json` 10/13 → `measure/c3-counter-selftest-at-freeze.json` 13/13).

## Sources & frontier

- SOURCES rows before→after: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  → **160 → 160 (unchanged)**. The round first drafted a new S161 row for the CDP protocol
  definition the journey claim rests on; the lane's own check-sources gate refused it
  `E04 duplicate_url` — the URL is already registered as **S153** (opened 2026-10-31) and this
  round's fresh fetch is BYTE-IDENTICAL to the registered anchor (sha256 `f60f0c02…` on both; master
  unchanged between the dates). The row was withdrawn pre-commit; **S153 re-opened** this round with
  the `getNavigationHistory` ("Returns navigation history for the current page.") and
  `navigateToHistoryEntry` ("Navigates current page to the given history entry.") descriptions
  located verbatim (1 hit each) in the opened bytes; staged copy at
  `.ufo/waves/round-50/sources/browser-protocol.json`. Catch record:
  `controls/sources-duplicate-row-catch.txt` (quotes the three gate runs that shaped the row,
  including two field-count refusals E01/E09). The frozen claims.json's "S161" provenance label is
  corrected of record in the SCORECARD erratum D4 — no measured predicate binds a registry count.
  Knowledge notes 65 → **66**; PROVINCE gained the round-50 runner line + the runtime-drift note.
- Census: START exit 0 / END exit 0 (22 pre-existing W04 duplicate-URL warnings, the same set
  disclosed r47/r48/r49; receipts `measure/census-start.txt` / `measure/census-end.txt`).
  check-sources at integration: verdict=clean rows=160 findings=0.
- Mistake mining: six Mistakes rows in `corpus/lessons/round-50.md`, each with its failing first
  read — the flag-less plain-mode live run; the runner's single-read page-target race (amendment 1);
  the history-model misprediction (amendment 2); the counter's wrong global distinctness rule (selftest
  first run 2/13); the fixture authoring path inconsistency (same selftest red); the duplicate S161
  registry row (gate E04, pre-commit). Plus the disclosed in-place overwrites (the first selftest
  run's receipt; the counter draft state re-measured via the committed named reproduction) and the
  EPERM selfassessment crash recurrence (receipt kept and named, never quoted as a verdict).

## Trend verdicts

- **expansion: improved** — the measured surface grew again: the webview2 page model now covers a
  multi-step journey with history-length and back-navigation evidence (0 → 5 evidence files; a live
  `navigateToHistoryEntry` hop recorded and counter-checked), the capability row
  `webview2-multi-step-journey-windows` enters the table (first-working 50), and a held source row's
  located ground extended to the two CDP history primitives (S153 re-opened, byte-identical).
- **quality: improved** — two pre-data instrument defects were caught by live red receipts and
  repaired under named amendments BEFORE any data committed; the D3 environmental pollution is closed
  in a versioned counter with the declared class, a hard-defect branch that still refuses, and a
  committed red/green selftest pair; the adjacency gate survived one live head race inside its frozen
  budget and reads green; no admitted entry failed a re-check.
- **discernment: improved** — every after-state is an instrument output at a named revision; the
  round refused its own first design twice and kept both red receipts instead of quietly re-running;
  the D1/D2 corrections quantify the drift from committed bytes rather than re-stating the r49
  numbers; the duplicate-row plan was refused by the lane's own gate pre-commit and is disclosed as
  a Mistake with the catch record; the declared could-not-evaluate class is bounded by a named rule
  (never a finding, only ever one code) that the fixture manifest asserts.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged
  this round (no SKILL.md edit declared); pointers resolvable (`corpus/lessons/round-49-verifier-spotcheck.md` §7
  holds the standing non-author note; boxes 1-4 all carried resolvable pointers through r49's closure).
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round's r50 journey
  (`corpus/evidence/round50/webview2-journey/`, LOG round-50 entry) extends the r3 journey precedent;
  logged.
- [~] Instructions executable by an agent without oral context — the r50 runner + counter +
  knowledge note are self-contained (`corpus/knowledge/webview2-journey-round-50.md` §1-§4); the
  executor-sufficiency note's own verdict (SUFFICIENT, lane-dispatched executor) stands until a
  non-author re-run (the closure's §7 note).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE updated this round (the journey
  surface + the runtime-drift standing condition); refusal routes unchanged
  (`PROVINCE.md` Refuses section; no cross-domain absorption: the CDP protocol definition is the
  lane's own execution surface ground, re-opened, not a sibling's finding).

SHONEN: no `[x]` written (promotion review is the operator's call; the r49 closure's §7 note lists
what a non-author re-run would close).

Assimilation: `considerthese/` does not exist in the lane repo (checked 2026-11-01). Shokuknow
register not reachable from this host. Assimilation: none — shokuknow unreachable.
