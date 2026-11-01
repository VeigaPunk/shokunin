# tsukuroi — round 60 report (Windows host, 2026-11-01)

Base `5dd83fa3` → head `b8b24076` (pushed to origin master; commits, all lane identity: `e1e10178`
carry-in, `41c18296` declaration, `bef165c4` work, `6d65fc0f` work addendum, `dd994b92` measured outcome,
`7fa72945` receipts, `b8b24076` receipts fixup — an appended correction to the final append-receipts
receipt's header, whose prose base sha carried a `…91ea7` typo for the true base `…91ea6`; the measurement
itself ran with the correct base and no value changes). Report written by the round author; the non-author
closure judge re-derives everything from committed bytes.

## Work performed

- **FRESH-START ruling (prompt §7; r50/r51/r52)** — the three rejected closures re-spot-checked from
  committed bytes at THIS base, plumbing reads only (receipt `.ufo/waves/round-60/before/freshstart-spotcheck.txt`):
  r50 `.ufo/waves/round-50/after/c1-final.json` → FAIL, verdicts_ok 0, marks_ok 0, seats_ok 18; r51
  `.ufo/waves/round-51/before/c2-cheats-at-amend1.json` → 0 bytes; r52 `.ufo/waves/round-52/after/c1-final.json`
  → FAIL, verdicts_ok 1, marks_ok 0, seats_ok 16 — identical to the r58/r59 re-derivations. Ruled out for
  cause: (a) the counted-cohort depth resume (gated on the absent wave-dispatch surface, L0 round-53,
  `.ufo/l0-questions.md:229`); (b) the S266 `type= interact` falsification probe (L0 round-57,
  `.ufo/l0-questions.md:247`, unanswered); (c) re-claiming any admitted r53–r59 move; (d) a bare re-run of
  an existing instrument as THE freshness move (the three planes' cadence pass is due 2026-11-30, not
  today; no drift has fired); (e) the `considerthese/` set (re-mined: seven notes, latest 2026-10-26,
  unchanged; all aggregator/wave-class or Linux-host-class here). Declared instead: three claims a
  do-nothing control cannot reach (each target absent at base, receipts `.ufo/waves/round-60/before/c1-c2-c3-at-base.txt`).
- **Carry-in 1 (routed, not claimed) — R59-GATE-FAIL-RECEIPT-UNLANDED discharged at `e1e10178`**: the
  intermediate registry-coverage FAIL (95/95/1 at `2913b75d`) regenerated from the committed gate at the
  base (identical counts: registered 95, rows_total 95, findings 1 REGISTRY-ROW-MISSING
  `tools/recheck-eventlog-r59.sh`) and committed raw under its honest name
  `.ufo/waves/round-59/after/registry-coverage-FAIL-at-2913b75d.regenerated-r60.json` + regeneration note
  naming the routing rule (gate red state in a repair story commits its raw receipt same-round, named
  FAIL + revision + original-or-regeneration; byte-equality to the scratch-deleted r59 original not
  claimed). PASS 96/96/0 re-run at `c4aa0f5c` and at the base.
- **Carry-in 2 (routed, not claimed) — byte-stable writers**: every record append this round written in
  binary mode against the target file's own line-ending convention; proven on committed bytes by C3's
  instrument (below). The tameshi r63 additivity-receipt convention is the fleet precedent (credited; no
  gate ownership moved — ADJ-07 method debt named in the tool docstring and registry row).
- **Carry-in 3 (routed) — whole-SKILL non-author SHONEN verification (owed since r55)**: operator's call;
  the L0 question `tsukuroi | round-60` appended to `.ufo/l0-questions.md` (byte-stable append); box marks
  untouched; routed around, never treated as answered. Standing L0s (round-53, round-57, round-1
  kaidoku/revenger) unchanged and routed around.
- **C1 (depth, lowest tied at 8, SOURCED)** — `corpus/knowledge/windows-registry-read-plane-r60.md`, rows
  RG1-RG5 (evidence: the note + receipts `.ufo/waves/round-60/registry-probes/rg1…rg5c` via receipt-run +
  SOURCES row S275): the registry READ contract of `reg.exe query` — named-value three-column entry shape;
  the single-message absence class (missing key AND missing value both rc 1 + `ERROR: The system was
  unable to find the specified registry key or value.`; S275 documents 0 Success / 1 Failure with no
  message text — the message is host-measured, the S274 boundary class); bounded `/s` recursion; the type
  vocabulary (5 types observed on the Schedule service key vs S275's documented six; REG_QWORD exists on
  the host AND `/t REG_QWORD` is ACCEPTED, rc 0 — the documentation is the stale side, the r59 J3 class);
  the MSYS/bash boundary (bare `/v` fails `Invalid syntax.` rc 1 at the conversion boundary; forward-slash
  key paths refuse `Invalid key name.` rc 1; `MSYS_NO_PATHCONV=1` on the receipt-run invocation is the
  probe convention). Read-only: `reg add/delete/copy/save/restore/load/unload` operator-owned, never
  invoked; no credential-bearing hive read.
- **C2 (operability)** — both recheck arms became SELF-DESCRIBING for the cadence pass (the r59 planned
  item; the R59-DECLARED-COMMAND-RECEIPT-SIDE proper fix): `tools/recheck-services-r56.sh` and
  `tools/recheck-eventlog-r59.sh` accept an optional `--due YYYY-MM-DD` (shape + calendar-range validated
  at the argument gate, rc 2 refusal BEFORE any probe and with no receipt written); with the flag the
  receipt header carries exactly one `due=<value>` line before `---`; without it the receipt shape is
  byte-identical to the landed conventions. Live passes receipted `.ufo/waves/round-60/receipts/`
  (services 22/22/0, eventlog 11/11/0, both `due=2026-11-30`; a no-flag shape run beside them).
- **C3 (calibration)** — `tools/append-receipt.py` (evidence: the tool + selftest `APPEND_RECEIPT_SELFTEST:
  PASS (5 cases)` rc 0 + registry row 97/97 + receipts
  `.ufo/waves/round-60/after/append-receipts-final-four-files.txt`): the byte-stable append verifier —
  old_only/new_only line-membership counts raw AND CR-normalized (empty lines dropped on both sides),
  `prefix_ok`, `eol_rewrite_disclosed`, exit 0/1/2, `--require-raw`; applied to this round's own record
  appends: all four record files measure old-only 0/0, `--require-raw` exit 0 — the r55-r59 CRLF-rewrite
  class avoided, not normalized away.
- **2b frontier** — SOURCES row S275 opened this round (live fetch; C1 rests on it); mistake mining into
  `corpus/lessons/round-60.md` `## Mistakes` (three rows, each with class · evidence · captured-by · fix);
  census start and end receipts (below).

## Landed changes (all tied to the LOG.md round-60 entry and its commit hashes)

| Change | Commit | LOG entry |
|---|---|---|
| r59 gate-failure receipt + regeneration note | `e1e10178` | round-60 carry-in entry |
| L0 question appended (fleet `.ufo/l0-questions.md`, not a lane commit) | — (fleet-root append) | round-60 carry-in entry |
| SCORECARD declaration + before-receipts (freshstart, c1-c2-c3-at-base, census-start) | `41c18296` | round-60 entry |
| C1 note + probe receipts + S275 row + C2 arm edits + C2 pass receipts + C3 tool + registry table + SKILL round-60 section | `bef165c4` | round-60 entry |
| C1 row-index decision table (the declared-grep repair) | `6d65fc0f` | round-60 entry |
| Measured outcome + axes restated + lesson round-60 + after-battery/gate receipts | `dd994b92` | round-60 entry |
| Final append-receipts + final-tree gate receipts + census-end receipt | `7fa72945` | round-60 entry |

Protected surfaces byte-identical to base (verified by blob sha): `corpus/README.md`, `PROVINCE.md`,
`SHONEN.md`, `corpus/QUALITY.md`, `AGENTS.md`. Capabilities table untouched (no row entered — the round's
instruments are registered in the gate/probe registry, not the repertoire table).

## Before → after measurements (counting command + measured commit)

- **C1 depth** — before at `5dd83fa3`: `git cat-file -e 5dd83fa3:corpus/knowledge/windows-registry-read-plane-r60.md`
  → rc 128; `git grep -c -i "reg query" 5dd83fa3 -- corpus SKILL.md PROVINCE.md tools` → 0 files (rc 1;
  likewise `REG_SZ`, `CurrentVersion`); SOURCES rows **274**. After at `6d65fc0f`:
  `grep -c "^| RG" corpus/knowledge/windows-registry-read-plane-r60.md` → **5**; SOURCES rows → **275**
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`), malformed **0**, S275 inside Registry after
  S274; knowledge-header gate **76/0/76**. (The declared grep's first work-tree run at `bef165c4` read
  **0** — rows were `##` headings; repaired by the `6d65fc0f` addendum, FAIL state re-derived from
  committed bytes at `.ufo/waves/round-60/after/c1-declared-grep-first-run-FAIL-at-bef165c4.txt`, nothing
  substituted.) Measured commit: `6d65fc0f`.
- **C2 operability** — before at `5dd83fa3`: `git grep -c 'due=' 5dd83fa3 -- tools/recheck-eventlog-r59.sh
  tools/recheck-services-r56.sh` → 0 (rc 1); `--due` in tools/ → 0; r59 pass receipt `grep -c '^due='` → 0.
  After at `6d65fc0f`: `bash tools/recheck-services-r56.sh --receipt <r1> --due 2026-11-30` → rc 0
  `RECHECK_SERVICES: PASS (22 rows, 22 match, 0 drift)`, `grep -c '^due=' <r1>` → **1**
  (`due=2026-11-30`); `bash tools/recheck-eventlog-r59.sh --receipt <r2> --due 2026-11-30` → rc 0
  `RECHECK_EVENTLOG: PASS (11 rows, 11 match, 0 drift)`, `^due=` → **1**; no-flag run → rc 0 with `^due=`
  **0** (shape preserved); malformed values (`2026-13-45`, `30d`, `2026-11-3X`) → rc **2**, no receipt
  written; `bash -n` rc 0 both. Measured commit: `6d65fc0f` (receipts from the `bef165c4`-tree runs).
- **C3 calibration** — before at `5dd83fa3`: `git cat-file -e 5dd83fa3:tools/append-receipt.py` → rc 128;
  `append-receipt` mentions 0; `round60 superseding` heading 0. After at `dd994b92`:
  `python tools/append-receipt.py --selftest` → `APPEND_RECEIPT_SELFTEST: PASS (5 cases, 5 passed, 0
  failed)` rc 0; registry-coverage gate → **97 tools / 97 rows / 0 findings** PASS;
  `python tools/append-receipt.py --repo . --base 5dd83fa3… --tip dd994b92… --file LOG.md --file
  SCORECARD.md --file SKILL.md --file corpus/SOURCES.md` → old_only raw **0** norm **0** on all four
  (LOG/SCORECARD/SKILL prefix true; SOURCES insert after S274, prefix false by position, old-only 0),
  `--require-raw` exit **0**. Measured commit: `dd994b92` (receipt landed `7fa72945`, receipt-after-subject,
  the tameshi r63 precedent; the receipt header's base-sha typo corrected by the appended correction in
  `b8b24076`). Gates re-run at the final tree: registry 97/97/0, headers 76/0/76, SCORECARD uniqueness
  ok rc 0.

## Sources & frontier

- SOURCES rows before→after: **274 → 275** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md`); malformed 0 (`awk -F'|' '/^…/ && NF!=13'` → 0), duplicate ids none, enum check
  clean; S275 inserted at its id position inside `## Registry` (line 284, after S274) — a pure single-line
  insert (old bytes byte-identical, removal round-trip verified). New row S275: Microsoft Learn `reg query`
  (Windows Commands), opened live 2026-11-01, tier A docs, quote 21 words by `wc -w`, used-by the C1 note.
  Rejections: **0 — stated explicitly** (no source opened and rejected; no lead reopened). Gate record:
  `corpus/lessons/round-60.md` `## Gate`.
- Census: `bash scripts/sources-census.sh validate --root <fleet-root> tsukuroi` — round start exit **0**
  (42 W04 duplicate-URL warnings, 0 E-code; `.ufo/waves/round-60/before/sources-census-start.txt`), round
  end exit **0** (42 W04, 0 E-code; `.ufo/waves/round-60/after/sources-census-end.txt`).
- Mistake mining: three mistakes captured in `corpus/lessons/round-60.md` `## Mistakes` —
  R60-C1-DECLARED-GREP (the declared grep read a shape the note lacked; caught by the before-citation
  battery; repaired by addendum `6d65fc0f`; FAIL receipted), R60-STRAY-RECEIPT (a refusal-gate test
  leaked a receipt to /tmp under the then shape-only gate; gate strengthened to calendar range, stray
  deleted same session, re-run refuses rc 2 with no receipt), R60-SELFTEST-SHAPE (the selftest first ran
  6 checks against the declared 5-case string; reshaped pre-landing, no committed byte carries the
  6-case form). Sweep that found no further mistakes is recorded in the lesson.

## Trend verdicts

- **expansion: unchanged** — `corpus/README.md` byte-identical to base (blob-sha verified); no
  capabilities-table row entered; S275 is a registry row; the new plane instruments an already-held
  province surface (the store behind the lane's own services/tasks planes, inside the host-transition
  record) — map-row addition stays deferred to a coverage round with its own claim.
- **quality: improved** — a new sourced plane landed under 0-finding gates (header 76/0/76, registry
  97/97/0, census exit 0 both passes); the two recheck arms' receipts became self-describing (the due
  anchor observable from the receipt); the record appends are byte-pure with the property now provable by
  a committed instrument (`--require-raw` exit 0); the routed gate-failure-receipt and CRLF classes are
  closed with named rules; the declared-grep shortfall was caught by the round's own battery and repaired
  with the FAIL receipted.
- **discernment: improved** (author-side; the deciding non-author judgment is closure's, per the r59
  precedent) — the round self-caught its own declared command reading 0 (receipted FAIL, repair by
  addendum), its own gate leaking a receipt off-repo (gate strengthened, stray deleted, refusal re-run
  clean), and reshaped its instrument pre-landing rather than land a mismatch; every FAIL state is
  re-derivable from committed bytes; the S275 admit carries its divergence (REG_QWORD) against the
  documented set; the carry-in regeneration honestly disclaims byte-equality to the deleted original.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author-side
  evidence: this round adds the registry READ plane's row-index decision table (note RG1-RG5) and the
  round-60 SKILL section; the standing author-side evidence (health-verdict decision table, update-safety
  checklist, error patterns, Sources section) is unchanged at `SHONEN.md`. Whole-SKILL non-author
  verification remains owed since r55 — routed to the operator this round via the new L0 question
  `tsukuroi | round-60`; no box self-marked.
- [~] At least one end-to-end domain task executed and logged in LOG.md — author-side evidence: LOG.md
  round-60 entry; the round's registry probes executed live through receipt-run with committed receipts
  (`.ufo/waves/round-60/registry-probes/`). Non-author replay remains owed.
- [~] Instructions executable by an agent without oral context — author-side evidence: the round-60
  declared counting commands were executed from the declaration text alone (battery receipts
  `.ufo/waves/round-60/after/`); the standing no-oral-context executor evidence is unchanged
  (`SHONEN.md` pointers). Whole-SKILL retest remains owed (same L0).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — author-side evidence: PROVINCE.md
  byte-identical to base (blob-sha verified); no sibling scope touched; the registry plane stays inside
  the lane's own host-operability province; the tameshi convention adoption is credited as method debt
  (ADJ-07), not ownership; contested kaidoku/revenger ownership remains unruled and unabsorbed.

Assimilation: `considerthese/` re-mined (seven notes, latest 2026-10-26, unchanged set; all
aggregator/wave-class or Linux-host-class on this host) — nothing adopted. Assimilation: none —
shokuknow unreachable.

L0: one new question appended this round (`tsukuroi | round-60`: the whole-SKILL SHONEN verification
ruling); standing questions `tsukuroi | round-53` and `tsukuroi | round-57` (and the round-1 kaidoku/
revenger scope) remain open and were routed around, never treated as answered.
