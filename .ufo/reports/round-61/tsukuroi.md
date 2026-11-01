# tsukuroi-shokunin — round 61 report (2026-11-01, Windows host)

Base `6b26c338` → head `52d9ba1a` (pushed origin master). Commits (helper-printed, all ancestors of
master): `136bfb00` declaration, `abb2a161` work, `541cdaea` measured outcome, `52d9ba1a` receipts.

## Work performed

- **C1 (depth, lowest tied 8, SOURCED): the Windows driver query plane.** Landed
  `corpus/knowledge/windows-driver-query-plane-r61.md` (rows DQ1-DQ5, S276 opened live 2026-11-01
  before the declaration text, disclosed ordering): the CSV inventory (one quoted 4-column header; the
  trailing-space `"Kernel "` Driver Type cell; empty Link Date cells as normal values), the
  host-measured 15-column `/V` column set (Start Mode/State/Status/Accept-Stop/Accept-Pause the triage
  columns — S276 documents no columns), S276's two documented restrictions MEASURED as refusal
  messages (`/FO LIST /NH` → `/NH option is valid only for "TABLE" and "CSV" format.` rc 1; `/V /SI` →
  `The verbose option is invalid for signed drivers.` rc 1), the invalid-format refusal rc 1 (S276
  documents no return-value table and no message text — the S274/S275 absence class), the `/SI`
  plain-text table (159 rows at capture), and the MSYS boundary on a SECOND command (bare `/FO`
  mangled to `'C:/Program Files/Git/FO'` recorded in the receipt's own `command=` line; `//FO` and the
  on-invocation `MSYS_NO_PATHCONV=1` both pass — the r60 RG5 class generalized, per-host not
  per-command). Evidence: probes dq1-dq5c via receipt-run (`.ufo/waves/round-61/driver-probes/`),
  SOURCES row S276 (line 285, directly after S275), knowledge-header gate 77/0/77
  (`.ufo/waves/round-61/after/knowledge-header-77-0-at-abb2a161.json`).
- **C2 (operability, 9 saturated): the registry read plane's recheck duty made executable.** Landed
  `tools/recheck-registry-r61.sh` — 10 live rows over RG1-RG5's invariant signatures (R1/R2/R2b/R3/
  R4/R4b/R4c/R5a/R5b/R5c), the r60 C2 `--due YYYY-MM-DD` convention verbatim (shape + calendar-range
  gate rc 2 before any probe, no receipt on refusal), rollup `RECHECK_REGISTRY: PASS (10 rows, M
  match, 0 drift)`; the round61 superseding registry table (97 round-60 rows byte-identical + 1 new,
  contiguous); registry-coverage gate 98/98/0. First run FAILED 1 drift — the R4 type-extraction
  regex `REG_[A-Z]+` truncated at the underscore (authoring-time artifact, not host drift) — FAIL
  receipt kept under its honest name and the fixed run cited (R61-ARM-FIRST-RUN, the r59 rule).
  Evidence: `.ufo/waves/round-61/receipts/` (due pass, no-due shape pass, FIRST-RUN-FAIL),
  `.ufo/waves/round-61/after/registry-coverage-98-98-0-at-abb2a161.json`.
- **C3 (coverage, 9 saturated): the coverage map catches up to the Windows-host transition.** Landed
  `corpus/README.md` `## Rounds 53-61 — the Windows host transition` — 9 map rows (the eight r53-r60
  notes with their VERIFIED row-ids and source-id headers + the r61 note), the map duty the r60 axes
  table explicitly deferred to a coverage round. Map governance on held ground: PROVINCE.md
  blob-identical to base (`23198d74…` both revisions), no frontier claim. Evidence: counting command
  below; each map row cross-checked against its note's own ids.
- **Carry-ins addressed first (status-neutral, none claimed):** the bde06613 gate-receipt rule
  re-applied (the discharged r59 FAIL receipt verified PRESENT at the base via cat-file; no r61 gate
  red state occurred — the C2 first-run FAIL is a probe-instrument first run, receipted regardless);
  byte-stable appends via the r60 C3 instrument (final five-file measurement old-only 0/0 raw+norm on
  ALL files, `--require-raw` exit 0 — the r55-r59 CRLF-rewrite class avoided, not normalized away);
  four standing L0s routed around, never treated as answered (`round-53` wave-dispatch line 229,
  round-1 kaidoku/revenger scope, `round-57` S266 line 247, `round-60` whole-SKILL SHONEN line 253).
- **FRESH-START r50/r51/r52 re-spot-checked at the base** (receipt
  `.ufo/waves/round-61/before/freshstart-spotcheck.txt`, plumbing reads): r50 FAIL 0/0/18, r51
  evidence 0 bytes, r52 FAIL 1/0/16 — identical to the r58/r59/r60 derivations. Ruled out for cause,
  none reachable by a do-nothing control: (a) the counted-cohort depth resume (L0 round-53); (b) the
  S266 interact probe (L0 round-57); (c) re-claiming any admitted r53-r60 move; (d) a bare instrument
  re-run as THE freshness move (cadence due 2026-11-30, no drift fired — the r60 receipts' own `due=`
  anchors); (e) the considerthese set (re-mined: seven notes, latest 2026-10-26, unchanged,
  aggregator/wave-class or Linux-host-class).
- **Assimilation:** `considerthese/` mined, nothing adopted this round. Assimilation: none — shokuknow
  unreachable.

## Landed changes (each tied to a LOG.md entry and its commit)

| Commit | Changes |
|---|---|
| `136bfb00` | SCORECARD "Round 61 — declaration" (claims C1/C2/C3 with before→after, falsifiers, verdict conditions); before-receipts `.ufo/waves/round-61/before/` (census-start exit 0 42 W04 0 E-code; freshstart-spotcheck; c1-c2-c3 at-base plumbing reads) |
| `abb2a161` | the C1 note + SOURCES S276 + probes dq1-dq5c; `tools/recheck-registry-r61.sh` + run receipts (FIRST-RUN-FAIL kept, due pass, no-due shape); SKILL round61 superseding registry table (98 rows) + SKILL round-61 section; README `## Rounds 53-61` map section |
| `541cdaea` | SCORECARD "Round 61 — measured outcome" + axes restate (ordinals unchanged); LOG round-61 entry; `corpus/lessons/round-61.md` (Gate S276, explicit 0 rejections, 3 mistakes, sweep); battery receipt + both gate JSON receipts at the work revision |
| `52d9ba1a` | the final five-file append-receipt measurement (base→outcome; `--require-raw` exit 0); both gates re-run at the final tree (98/98/0, 77/0/77); census END receipt exit 0 (42 W04, 0 E-code); the pre-existing adjacency-gate host limit named in the commit message |

## Before → after measurements (counting command; measured at `abb2a161`, receipts
`.ufo/waves/round-61/after/c1-c2-c3-counts-at-work.txt`)

- **C1 depth:** before at `6b26c338` — `git cat-file -e 6b26c338:corpus/knowledge/windows-driver-query-plane-r61.md`
  rc 128; `git grep -c -i driverquery 6b26c338 -- corpus SKILL.md PROVINCE.md tools` → 0 files (rc 1);
  SOURCES rows 275. after — `grep -c "^| DQ" corpus/knowledge/windows-driver-query-plane-r61.md` → **5**;
  `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **276** (S276 at
  line 285 after S275 at 284; 0 duplicate ids; Gate quote `wc -w` = 14); knowledge-header PASS 77/0/77.
- **C2 operability:** before — `git cat-file -e 6b26c338:tools/recheck-registry-r61.sh` rc 128;
  `git grep -c RECHECK_REGISTRY 6b26c338 -- tools SKILL.md` → 0 (rc 1). after —
  `bash tools/recheck-registry-r61.sh --receipt <r1> --due 2026-11-30` → rc 0 `RECHECK_REGISTRY: PASS
  (10 rows, 10 match, 0 drift)`; `grep -c '^due=' <r1>` → **1**; no-flag run rc 0 10/10/0 with `^due=`
  → **0**; malformed `--due` (`2026-13-45`, `30d`, `2026-11-3X`) refused rc **2** writing no receipt;
  `bash -n` rc 0; registry-coverage **98/98/0**.
- **C3 coverage:** before — `git grep -c 'knowledge/windows-' 6b26c338 -- corpus/README.md` → 0 files
  (rc 1). after — `grep -c 'knowledge/windows-' corpus/README.md` → **9**; PROVINCE.md blob-identical
  to base (`git rev-parse <rev>:PROVINCE.md` → `23198d74…` at both).

## Sources & frontier

SOURCES.md rows before→after: **275 → 276** (counting command
`grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; at base the same
plumbing read → 275). S276 (driverquery, Microsoft Learn Windows Commands, tier A docs, opened live
2026-11-01, quote 14 words by `wc -w`, recheck 180d, used-by the r61 note) inserted at its id position
directly after S275 — the insert is a pure single-line insertion (old-only 0/0, new_only 1, the final
append-receipt receipt). Rejections this round: **0 — stated explicitly** (no source opened and
rejected; no lead carried from r60). Census: exit 0 at round start (42 W04, 0 E-code) and at round end
(42 W04, 0 E-code; receipts `.ufo/waves/round-61/before/sources-census-start.txt` and
`.ufo/waves/round-61/after/sources-census-end.txt`). Mistake mining: `corpus/lessons/round-61.md`
`## Mistakes` — R61-ARM-FIRST-RUN, R61-SOURCES-ROW-DELIMITER, R61-SPAWN-VAR-POSITION, each with class ·
evidence · captured-by · fix, plus the no-further-mistakes sweep. Frontier: unchanged — C3 is map
governance on held ground; PROVINCE.md untouched (blob-identical).

## Trend verdicts

- **expansion: unchanged** — no new province ground: the driver-query plane instruments the lane's own
  driver/firmware Core surface on the Windows host class; PROVINCE.md and corpus/README.md's domain
  ground unchanged (the README delta is the map rows for EXISTING entries); no capabilities-table row
  entered (the round acquired no new capability class — the recheck arm extends the existing r59
  pattern to one more plane); SOURCES +1 on already-held province ground.
- **quality: improved** — a new sourced plane landed under 0-finding gates (header 77/0/77, registry
  98/98/0 at both work and final revisions; census exit 0 both passes); the registry plane's recheck
  duty moved from prose to an executable arm whose receipts self-carry the due anchor; the final
  five-file append-receipt measurement proves every record append byte-pure (`--require-raw` exit 0);
  S276's two documented restrictions are now measured against the host, not just read; no admitted
  entry failed its re-check (both r60 recheck arms and the new arm pass live).
- **discernment: improved** — three self-caught defects, all BEFORE an outcome cited them and all
  receipted: the arm's first-run FAIL kept under its honest name (R61-ARM-FIRST-RUN), the 14-cell
  SOURCES row caught at the awk NF check with no committed byte ever malformed
  (R61-SOURCES-ROW-DELIMITER), the wrong-var spawn caught at the receipt rc line and disclosed rather
  than silently dropped (R61-SPAWN-VAR-POSITION); the FRESH-START ruling (d) again held (no drift has
  fired; the cadence pass stays due 2026-11-30); the pre-existing adjacency-gate host limit is named
  rather than smoothed (below).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — Author-side
  evidence: this round ADDS the DQ1-DQ5 row-index table (`corpus/knowledge/windows-driver-query-plane-r61.md`,
  `grep -c "^| DQ"` = 5) and the round61 superseding registry table (`grep -c '^| ' ` over the table =
  100 lines, 98 data rows, gate 98/98/0); the standing whole-SKILL non-author verification remains
  parked on L0 `tsukuroi | round-60` (fleet `.ufo/l0-questions.md:253`), so the box stays `[~]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — Author-side evidence:
  `corpus/knowledge/host-health-report-r3.md` (historical) and this round's full
  declare→source→probe→instrument→gate→measure cycle logged in LOG.md round-61 with committed
  receipts; the box's original end-to-end claim is unchanged and unverified by a non-author — stays
  `[~]`.
- [~] Instructions executable by an agent without oral context — Author-side evidence: this round's
  own work is a live demonstration (declaration → probes → arm → gates ran from committed bytes
  alone); `corpus/knowledge/executor-test-sufficiency.md` and the SKILL no-oral-context checklist
  unchanged; the whole-SKILL retest remains unexecuted (L0 `round-60`) — stays `[~]`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — Author-side evidence: PROVINCE.md
  blob-identical to base this round (`23198d74…` both revisions); the driver-query plane named inside
  the existing Core driver/firmware surface (state/health reading, not shipped-artifact internals —
  kaidoku/revenger untouched); contested ownership still unruled (carried) — stays `[~]`.

## Named limits (reported, not smoothed)

`tools/check-adjacency-table-r51.py` reads FAIL at the base AND at the final tree with identical
detail (`ancestry_ok` 0, all 10 pinned sibling blobs "unreadable" on this host) — the r49/50/51 anchor
green runs are Linux-host pins; this is a pre-existing host-class surface absence (the r53
host-transition pattern), not a round delta: PROVINCE/adjacency files are byte-untouched and the gate
is not in this round's declared gate set. Receipts: the FAIL JSONs were re-derived at both revisions
during this round's verification (transcribed here; not committed as round receipts since no repair
story attaches — the bde06613 rule is about gate reds in a repair story). `check-self-assessment.py`
still cannot evaluate on this host (K13, named limit). The L2 floor (≥8 subagents, one batched
AgentSwarm call) has no dispatch surface on this host (standing L0 `round-53`) — routed around, not
waived by the lane. The DQ rows' own executable recheck arm is deliberately NOT landed (the r59
planned-item pattern: an arm joins the discipline when its plane's drift fires or its note's duty
matures; the DQ note carries the 30d cadence and C2's arm already covers the registry plane).
