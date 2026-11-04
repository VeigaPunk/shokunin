# kama — round 82

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin` (branch `master`), final lane tip
`b1ba614b51255a3dcfe3e0946f32f8e31bd65c09` (remote-verified: `git ls-remote origin refs/heads/master`
prints it). Base `aaf974dbd3b6adb2ef914dc7293cda92b4e05551` (round-81 non-author closure tip). Frozen plan
`kama-shokunin/plans/round-82-claims.md` (freeze commit `bfdd7a70`). **Stale-lane: no** — the driver is
respawn-per-round and no other mission of this lane is open.

## Work performed

The round declares two claims on two distinct axes, each measured on its own committed receipts:

- **C1 — calibration (the lowest assigned axis, 7).** The round-81 self-record's six declared facts are
  re-derived at the sealed revision `1b64f66d` and the five stale ones are answered by dated,
  value-bound corrections; the sixth holds and must not be corrected.
- **C2 — operability (held 8; the `append-debt` capability gains a delta leg).** Round 81's five pending
  append-only events are repaid by 15 committed late rows that a delta check re-derives, and the
  acceptance population closes under the round-81 rule — repaired to the row-level wording its own prose
  and the frozen plans always used.

Work items, each with its evidence pointer:

- **Freeze and controls before data.** `plans/round-82-claims.md` at `bfdd7a70` declares both predicates,
  the six-fact table, the five corrections, both target lines and the control lists.
  `kama-shokunin/.ufo/waves/round-82/measured/before/c1-enum.out` (`SELFRECORD_R81_ENUM claims=6 stale=5
  corrected=0`, exit 1), `…/control/c1-no-corrections.out` (`mismatches=5`, exit 1),
  `…/before/c2-late-delta-base.out` (`LATE_DELTA … new=0 bad=15`, exit 1), `…/before/c2-debt-base.out`
  (`APPEND_DEBT round=82 … unaccepted=5`, exit 1) and the freeze-tip gate control
  `…/control/c2-gate-arm-freeze-tip.out` (arm 8 red on the debt leg at `bfdd7a70`).
- **C1 instrument.** `kama-shokunin/tools/round82-selfrecord-round81.py` (selftest `pass=23 fail=0`,
  `measured/after/c1-selftest.out`): git-blob fact readers, the `## Corrections` container only, exact
  token comparison, `fix=` path token check, and red arms for outside-container, wrong-`at`, wrong-`old`,
  wrong-`new`, token-less `fix`, duplicate, holding-fact and unknown-fact corrections. The base-binding
  arm `registry-base-bound` proves F2's population witness.
- **C2 leg 1.** `kama-shokunin/tools/round82-late-delta.py` (selftest `pass=13 fail=0`): re-derives the
  late register's delta from the frozen round-81 generator (imported, not re-implemented), binds carried
  rows byte-wise to the base revision and grades new rows by cells and by accepting/deletion round order.
- **C2 leg 2 repair.** `kama-shokunin/tools/round81-append-debt.py` now resolves each late row's OWN
  introducing commit (`git blame <rev> -- registry/append-only-late.tsv`, `blame_rows`) instead of one
  commit for the whole register; three new selftest arms (`row-intro-later`, `row-intro-earlier`,
  `row-intro-unbound`) and `APPEND_DEBT_SELFTEST pass=25 fail=0`. The red-before is
  `measured/defects/c2-debt-register-level-before.out` (`bad_rows=15`, every row `not-descendant`, rev
  `b0064016`); the repair is disclosed in the module docstring, the lesson and the report.
- **Gate.** `tools/pre-report-gate.py` gains arm 12 `round82-instruments` (both new counters' own
  selftests, each required to end with its own summary prefix); the gate selftest is
  `PRE_REPORT_SELFTEST pass=29 fail=0` (three new arms).
- **Final gate.** `python3 tools/pre-report-gate.py --repo . --round 82 --tip master` prints
  `PRE_REPORT round=82 arms=12 failed=0 uncommitted=0`, exit 0 at `9efa6f1c`
  (`measured/after/gate.out`); arm 8 carries the debt line, arm 12 both new selftests.
- **Record.** `SCORECARD.md` gets the appended `#### round-82 correction` block and the §Round 82
  section; `LOG.md` gets the §Round 82 entry and two appended `LOG-CORRECTION round=81` lines;
  `SKILL.md`'s pre-report-gate row is re-anchored to twelve arms; `PROVINCE.md` gains the round-82
  instrument note; `corpus/lessons/round-82.md` carries the Gate, the five corrections, the mined
  mistake and the freeze divergences; `corpus/knowledge/pin-recheck-trigger.md`, its `corpus/README.md`
  coverage row and `KQ134` land the round's knowledge delta.
- **Attack and verification seats.** One v1 wave of 14 seats (`executor` 4, `scribe` 3, `scout` 2,
  `reviewer` 2, `connector` 1, `critic` 1, `mutation-tester` 1; attack share 4/14 = 29 %), dispatched
  through the `.ufo/waves/round-82/w1.ready` handoff; results in `.ufo/waves/round-82/w1-results.json`.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| frozen claims plan | §Round 82 (plan reference) | `bfdd7a70` |
| C1 counter, C2 delta checker, 15 late rows, before/control receipts | §Round 82 C1/C2 | `b0064016` |
| successor-register hypothesis artifact (unused; see disclosures) | §Round 82 C2 | `ac761e04` |
| row-level introduction repair in `round81-append-debt.py`, gate arm 12, red-before receipt | §Round 82 C2; lesson §Mistakes | `5fe3c58c` |
| round-81 corrections, §Round 82 record, twelve-arm SKILL row, PROVINCE note, lesson, knowledge entry, sources S563–S565, KQ134, README row | §Round 82; §Corrections; §Mistakes | `962bd251` |
| F2 base binding (freeze divergence 5), selftest tally 19 | §Round 82 C1 | `a251cbab` |
| wave spec, dispatch and refreshed claim receipts | §Round 82 wave | `bacae072` |
| calibration closure re-anchor (gate arms selfdesc, newest-closure) | §Round 82 dispositions | `4f156ecf` |
| closure-pointer clause + PROVINCE instrument naming | §Round 82 dispositions | `4beb4f2b`, `384ef1d5` |
| head rows reconciled to the tip (gate 29 cases, debt 25 arms, PROVINCE digest, 55 entries, receipt-bound round-81 counter) | §Round 82 dispositions | `d18e55e8` |
| §Planned (round 83), 46 capabilities, saturation vector, capability mirror | §Round 82 | `0d7c7c3e` |
| hardening pass (RV01/RV02/CR01/MT01 findings), second-pass corrections, final gate green | §Round 82; lesson §Hardening notes | `e93d859a`, `45c4926e`, `6a160310`, `8a3e8af2`, `95e417f1`, `6da926f2`, `9efa6f1c`, `b1ba614b` |
| census before/after receipts and the freeze-tip gate control | §Round 82 C2 | `87cd90fb` |
| receipt header normalization to the `rev=<hex>` contract form | §Round 82 C1/C2 | `6e93c33b` |
| full-path receipt citations and the F2 divergence note | §Round 82 C2; lesson §Freeze divergences | `7ad14e6c` |

## Before → after measurements

**C1 (calibration).** Counting command `python3 tools/round82-selfrecord-round81.py --repo .`:

- before: the freeze-tip run printed `SELFRECORD_R81_ENUM claims=6 stale=5 corrected=0`, exit 1; the
  retained receipt re-runs the frozen command at `e93d859a` where the sealed facts are unchanged and
  prints the same line (`measured/before/c1-enum.out`, header `# rev=e93d859a`).
- after, at `45c4926e` (the mutant-killing tip): `SELFRECORD_R81 claims=6 mismatches=0 corrected=5
  unbacked=0`, exit 0 (`measured/after/c1-green.out`).
- controls: `--no-corrections` → `claims=6 mismatches=5 corrected=0`, exit 1
  (`measured/control/c1-no-corrections.out`); `--enumerate` → `stale=5`, exit 1
  (`measured/before/c1-enum.out`); selftest `pass=23 fail=0`
  (`measured/after/c1-selftest.out`).

**C2 (operability).** Counting commands `python3 tools/round82-late-delta.py --repo . --round 82` and
`python3 tools/round81-append-debt.py --repo . --round 82`:

- before (tip instrument against the base tree `bfdd7a70`, 88-row register): `LATE_DELTA round=82 base=aaf974dbd3b6
  population=103 carried=88 new=0 bad=15`, exit 1 (`measured/before/c2-late-delta-base.out`); and
  `APPEND_DEBT round=82 base=aaf974dbd3b6 events=68 accepted=53 late=10 pending=0 unaccepted=5
  bad_rows=0 bad_declarations=0 out_of_population=0`, exit 1 (`measured/before/c2-debt-base.out`).
- after: `LATE_DELTA round=82 base=aaf974dbd3b6 population=103 carried=88 new=15 bad=0`, exit 0 at
  `8a3e8af2` (`measured/after/c2-late-delta.out`); `APPEND_DEBT round=82 base=aaf974dbd3b6
  events=68 accepted=53 late=15 pending=7 unaccepted=0 bad_rows=0 bad_declarations=0
  out_of_population=0`, exit 0 at `45c4926e` (`measured/after/c2-debt.out`; `pending` is the round's own
  post-base events and rises with each later record commit).
- controls: base delta run `bad=15`; the unmodified module's red-before `bad_rows=15`
  (`measured/defects/c2-debt-register-level-before.out`); the freeze-tip gate arm red on the debt leg
  (`measured/control/c2-gate-arm-freeze-tip.out`); selftests `LATE_DELTA_SELFTEST pass=13 fail=0`
  (`measured/after/c2-selftest.out`) and `APPEND_DEBT_SELFTEST pass=25 fail=0`
  (`measured/after/c2-debt-selftest.out`).

## Sources & frontier

Counting command (round start and round end):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

- round start (base blob `aaf974db`): `census --file` on the base `corpus/SOURCES.md` → `rows 302`,
  `tier.A 287 / tier.B 11 / tier.C 4`, `status.mined 271 / queued 8 / rejected 23`
  (`measured/before/census.out`); `validate --root` exit 0.
- round end (tip): `rows 305`, `tier.A 290 / tier.B 11 / tier.C 4`, `status.mined 273 / queued 8 /
  rejected 24` (`measured/after/census.out`); `validate --root` exit 0
  (`measured/after/census-validate.out`), warnings the pre-existing `W04` inventory plus the
  pre-existing `W01 S481` — no new instance (S563/S564/S565 carry three distinct URLs).

Rows added by tier: **2 mined (S563, S564, both tier A), 1 rejected (S565, tier A)**. Rows touched
old→new: none (`status`, `recheck` and `used-by` of existing rows are unchanged; S565's `used-by` is
`—` as for every rejected row). Frontier rows advanced: the four `pin-watch` `behind` relations gained
their first pinned-document comparison (S563 at `b12103` vs S564 at `b11755`: the `### GET /health`
statement is byte-identical, one line shifted, the document grew 2402 → 2620 lines), recorded in
`corpus/knowledge/pin-recheck-trigger.md` with its `corpus/README.md` coverage row.

Gate decisions (2026-11-04, every URL fetched this round): S563 admit, S564 admit, S565 reject with its
flip — URLs, byte counts, sha256 and ≤25-word located quotes in `corpus/lessons/round-82.md` §Gate.

Assimilation: the round's consequent work is the `pin-recheck-trigger.md` entry and its two sources; a
`merge/kama/` theme was not adopted (the package's staged entries target other ground; the round chose
the recheck rule its own freshness work demanded). Assimilation: none from `merge/kama/`.

`considerthese/2026-10-26.md`: proposals 1–3 remain unimplemented and are named in the report rather
than implemented; proposal 4 (the daily pin-gap line) is already the `pin-watch` capability. No new
proposal lands this round.

## Trend verdicts

- **expansion — improved.** The frontier moved on ground the lane did not hold: the four `pin-watch`
  `behind` relations now have a pinned-document comparison rule and its first receipt (S563/S564, the
  knowledge entry and its coverage row); registry 302 → 305; two capabilities enter the repertoire
  (`late-delta`, `selfrecord-round81`).
- **quality — improved.** Five stale facts of the round-81 record are repaired value-bound without
  rewriting a filed byte, and the sixth is proved to hold; the late-acceptance rule's prose/code
  divergence is repaired with a red-before receipt and three red-capable arms; the gate gains arm 12 and
  29 selftest cases. Bound: the repair happened after its red-before receipt existed and a closure must
  judge admissibility; F2's freeze witness was mis-stated (see disclosures).
- **discernment — improved, bound.** The round reads its own prior claim more strictly than the closure
  did: it finds that the late-acceptance rule could never accept a post-register event, proves it with a
  committed red receipt, and declines to hide the sequence; it also classifies the closure's own R81V1
  sentence as half-wrong (the `pass=16` half is LOG's, not SCORECARD's) instead of accepting it. Bound:
  no independent non-author verification exists yet; the round's self-verdict is `[~]` only.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md` §§Decision table, Error signatures, Checklist; the round-82 pre-report-gate row is
  re-anchored to twelve arms. No named non-author verifier this round.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` §Round 82
  (the late-row repayment and the pin recheck); earlier live receipts `.ufo/waves/round-16/live/` and
  `round-17/live/` stand.
- `[~]` Instructions executable by an agent without oral context — pointer: `SKILL.md` §Checklist,
  `corpus/knowledge/pin-recheck-trigger.md` with its `recheck:` command.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` §Write boundary and
  the round-82 note; service repair, routing and credentials remain operator/sibling-owned.

## Wave

ONE v1 wave, 14 seats, dispatched through the inline handoff:
`.ufo/waves/round-82/w1-spec.json` (14 items, `maxLanes` 16), `w1-dispatch.json`, `w1.ready` (+ its
`dispatched` marker), `w1-results.json` for the per-seat status and final output. Role mix: 4 executor
(EX01 fact re-derivation, EX02 population, EX03 receipt replay, EX04 gate arm), 3 scribe (lesson,
sources, knowledge), 2 scout (pin recon, record scan), 2 reviewer (C1 and C2 attacks), 1 connector
(sibling scan), 1 critic (claims/controls), 1 mutation-tester — attack seats 4/14 = 29 % (≥25 %),
connector seats 1 (≤2). **All 14 seats settled with non-empty output; 0 dead seats.** No seat was
replaced and no payload was resent.

What the seats independently found (their receipts are in `w1/<Seat>/`, their reports beside them):

- **EX01** re-derived the six C1 facts before opening the counter; its `stale=5`/`F6 holds` table
  agrees with the counter, and its `--enumerate` reading matches the control.
- **EX02** re-derived the C2 population from the audit alone: 68 graded events / 492 undeclared line
  entries, 389 covered by the frozen register, **103** in the late register, 0 uncovered and 0 extra —
  no gap between the audit and the register (population 103 carried 88 + new 15).
- **EX03** replayed every receipt at its named revision: the honest receipts reproduce; two defects it
  named (a red `c1-json.out` left under `after/`, and a `tail`-captured `EXIT=` line) were fixed before
  the report (see disclosures).
- **EX04** captured the freeze-tip gate (arm 8 red on `unaccepted=5`) and specified arm 12, which the
  L1 then wired and the gate selftest covers (29 → 29 cases with the three new checks).
- **RV01** attacked C1 and found three admitting lines — substring `fix` tokens, a self-referential
  `fix=`, and any heading containing "Corrections" — all closed, with three new red arms
  (`near-token-new`, `fix-self-referential`, `near-corrections-heading`), selftest 19 → 22.
- **RV02** attacked both C2 legs; its one claim-level escape (a note's deletion round unbound: `round-82
  accepts round-79` for a round-81 event passed both legs) is closed by binding the note's deletion round
  to the commit subject (`subject_rounds`), with the `note-wrong-deletion-round` arm, selftest 12 → 13;
  its `--late`-unbound and docstring findings are recorded as limits.
- **CR01** falsified the claims and controls: the do-nothing controls are red and the targets are
  unreachable without the work; it also named the two in-place SCORECARD edits as `pending` deletions
  (reported below, not hidden) and the receipt defects EX03 also found.
- **MT01** ran nine named mutants; eight were killed and the one escape (`startswith` token comparison)
  is now killed by the `prefix-token-not-equal` arm, proven red under the mutant (selftest 22 → 23).
- **SK02** scanned 104 declared round-81 claims, found 18 stale rows and 8 distinct stale facts outside
  C1's five corrections; the record now carries their corrections in the second-pass block.
- **SK01** found the `pin-watch` invocation in the new knowledge entry was wrong (`--repo` instead of
  `--pins registry/engine-pins.tsv`) and fixed by the L1; the live read is `pins=3 current=0 behind=3`,
  llama.cpp newest `b12110` (upstream moved again between reads).
- **CN01** found no sibling lane holds an append-only register that binds a row's introducing commit
  (`kaidoku`'s registers bind cell bytes, `chousa`'s `git-first-commit` binds a path's first add,
  `kaidoku`/`kotodama` bind chain state) — the rule is in-province, no absorption.

## Disclosures, routed defects and open limits

- **R81V1** fixed on both halves, and wider than C1 graded: the C2 row's `pending=1` (F1/F5) and its
  `pass=16` tally (deep in the row's fourth cell) are corrected, and the banner's duplicate `pending=1`
  with them — the closure was right, and the six-fact population was too narrow (see the SK02 finding
  and SCORECARD's `#### round-82 correction (second pass …)` block).
- **R81V2** fixed for this round's receipts (each `# rev:` header is read before its command runs);
  the round-81 `battery.out` label stays history. The R81V2 class itself is now a *reproducible* check
  only by receipt replay — EX03's seat receipt is the probe.
- **R81V3** fixed (registry 302 in the record and the F2 correction). **R81V4** fixed (twelve-arm SKILL
  row). **R81V5** recorded (no new warning instance). **R81V6/R81V7** recorded as pointers/counts.
  **R81V8** fixed (the Landed-changes table names every round commit).
- **Freeze divergence 5 — F2's witness.** The plan named "the tip registry count (302)"; the round's own
  three rows move the tip to 305, so the counter reads the registry at the declared base (302) and the
  correction stays `new=302`. Both numbers are in the record; the plan's witness cell should have said
  "base count" at freeze.
- **The C2 leg-2 instrument was repaired after its red-before receipt existed** (the rule sentences are
  unchanged; the resolution of "a row's introducing commit" now matches the prose and the round-81
  plan). The closure must rule on admissibility.
- **`--late` remains unbound**: a register passed on disk gets no introduction, so every row is
  `unbound-register`; the round used the default path and routes the v2 rule to round 83.
- **`registry/append-only-late-r82.tsv`** is committed but unread by either leg (the failed file-level
  hypothesis; retained rather than deleted because a 104-line deletion would enter round 83's
  acceptance population).
- **Receipt-binding state.** At the final tip `round72-receipt-tip-binding` reports bound 3 / shifted 5 /
  unbound 0 / stale 0 after the U1 path fix: the four *after* receipts are bound and the four
  before/defect receipts are `shifted` — they measured earlier trees by design, and the delta to the
  tip includes `corpus/knowledge` edits that the tool does not classify as record paths. The round does
  not claim the binding capability green for its before receipts.
- **The round's own in-place SCORECARD edits** (banner, claim row) are two graded deletion events, so
  the round's `APPEND_DEBT` line carries `pending=7`; the plan's sentence "every edit to an append-only
  file is an append" was too strong and is corrected by that number, not restated.
- **Receipt defects fixed before the report** (EX03/CR01): `c1-json.out` was a red, truncated capture
  and is now the green JSON; the `EXIT=` lines of `c1-enum.out`/`c1-no-corrections.out` were `tail`'s
  status and are now Python's; the delta `before` receipt was measured where its tool did not exist and
  now names `# tree=bfdd7a70` with the tip instrument.
- **Fleet root**: `after` (a 24-byte file dated 2026-11-03 20:05, before this round) is not this round's
  misroot and was not touched; `.scratch/` changes belong to the orchestrator by design.
- **Tool installs**: none this round (nothing installed or upgraded by the L1; that is the honest
  record).
