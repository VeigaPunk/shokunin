# kaidoku — round 77

Lane `kaidoku-shokunin`, round 77, attempt 1. Base `188562d43e3cc58b217ad7aa763fb296c5b8a0b7`; declaration
`819cf30e2fc35d91a69df1b2a42a025741c7d0ef`; freeze `6767a879c6a3f386a9c3fc9d332c794f2d9ea914`; filing revision
`88e73357c26c468f4c28d5f29fd5004358b695eb`; final lane tip `97280cadb87386e7968c3f90e8503f14d41695ea`.

**Declared claims.** Two, on two distinct axes, both capability acquisitions, frozen before data
(`plans/round-77-claims.md`, `.ufo/waves/round-77/claims.json`):

- **R77-C1 — calibration: evidence-cell verdict binding.** The round-76 non-author spot-check (routed defect 5)
  found that its own atom admitted a false verdict written beside a resolving pointer: three cells said
  `c1-at-landing.json (D24 true, mismatch_count 0)` while that receipt records `exit 1`, `mismatch_count 1`,
  `D24_capability_rows false`. R77-C1 lands an instrument that parses each annotation with a closed grammar and
  re-derives it from the JSON receipt the cell names.
- **R77-C2 — operability: the prefile gate keeps a receipt.** Routed defects 3 and 4: the round-76 filing
  asserted `prefile-check.sh` passed with no retained output, and its `gate-at-tip.txt` carried no wrapper exit.
  R77-C2 lands a receipt that binds argv, revision, exit, verdict line, stdout digest and the child's key set.

Lowest-axis obligation: coverage/depth/calibration are tied at 10.0 behind different proxies; **calibration** is
named lowest and R77-C1 works it. No nudge waiver is claimed (capability rows entered in rounds 73–76, inside
the 10-round window).

## Work performed

- **Declaration and freeze.** Both instruments, `plans/round-77-claims.md`, the 15- and 13-case selftests, the
  do-nothing controls, the census-start and three source snapshots landed **before any claim data** at
  `819cf30e`; the claims file with both predicates byte-identical to the instruments' `PREDICATE` constants and
  the two base receipts landed at `6767a879`. The round-29 gate audits the freeze **CLEAN**, findings `[]`, three
  instrument paths (`.ufo/waves/round-77/l1/scores/gate-at-freeze.json`, `exit 0`).
- **R77-C1 instrument** `tools/round-77/verdict-bind.py` (`819cf30e`, sha256 `45280392…`): frozen scope = the
  SCORECARD `## Capabilities` rows with first-working round ≥ 73 plus the PROVINCE `- **Core — ` bullets; eight
  grammar forms (`field literal`, unique atom shorthand, `field N of M` with the `*_ok`→`*_total` pairing,
  `N mismatches`, `N survivors`, `N|word atoms`, `pristine N`, `validate defect-free`); type-strict comparison
  (S289: `true` never satisfies an integer field); unparsable clauses and absent receipt fields are **unbound**,
  never passes. Selftest 15 cases, 0 failures (`pre/selftest-c1.json`).
- **R77-C2 instrument** `tools/round-77/prefile-receipt.py` (`819cf30e`, sha256 `174eedb5…`): runs
  `tools/round-29/prefile-check.sh` with a list argv under exactly HOME/LANG/PATH/TMPDIR inside the work root,
  writes `{argv, rev, exit, prefile_line, stdout, stdout_sha256, passed, env_keys}`, and `--check-receipt`
  re-derives every clause from those bytes (a failing gate is a valid receipt). `--battery` scores six arms.
  Selftest 13 cases, 0 failures (`pre/selftest-c2.json`).
- **Controls, frozen before data and re-taken after the wave.** `tools/round-77/gen-controls.py` derives
  `no-binding` (`parse_clause` → None) and `all-false` (`bind` → mismatch) controls from the pinned instrument
  bytes; `pre/controls-c1.json` records `no-binding` `bound_clauses 0` / `mismatch_count 0` and `all-false`
  `mismatch_count 24`, neither meeting the target and both diverging from pristine. Round 76's own audit at base
  is the pointer-only control: `mismatch_count 0`, `D24` true, false annotation standing
  (`pre/controls-c1.json` `pointer-only`). `pre/controls/c2-gate-alone.json`: the gate alone prints
  `prefile: PASS` at exit 0 and retains nothing. `pre/controls/c2-forged-arms.json`: `--validate-battery` refuses
  a forged `arms_ok` (two defects).
- **Wave `r77-w1`** — one v1 wave, 12 seats, validated under `ufo-wave-policy.json` (band 8–16; dispatch payload
  `.ufo/waves/round-77/r77-w1-dispatch.json`, `counts {spawn 12, resume 0, total 12}`; ready marker and the
  orchestrator's dispatched map retained). Roles: 3 executor, 2 reviewer, 1 scout, 1 connector, 1 critic,
  1 mutation-tester, 1 sentinel, 1 scribe, 1 revenger — attack roles 6/12 = 50 %, one connector; the L1 holds the
  planner seat (a frozen-topology seat is never a swarm role). **10 seats returned evidence** under
  `.ufo/waves/round-77/w1/`; **2 died with zero-byte output and no evidence dir** (`ExecC2Receipt`, `ReviewerC1`);
  `r77-w1-results.json` carries `note: null` for both, so their last error text is not retained — recorded as a
  defect of the round, not papered over. No replacement seats, no residual call.
- **What the wave changed.** `ExecControls` (F1) found the first control generator appended each override *after*
  the module's `__main__` guard, so both controls ran the unmutated instrument: repaired at `63dc9c6f` (override
  before the guard, generator refuses an override that lands after it, per-control `diverges` field), disclosed as
  an `instrument_supersessions` entry at `2ae8da54`, and the controls re-taken. `ScribeSources` cross-checked the
  three source quotes (it confirmed the RFC line: the text file carries 16 form feeds, so `str.splitlines()` would
  count 303 while `grep -n` reports 298). `ScoutSurfaces` independently reproduced the scope arithmetic
  (`rows 39 / in_scope 9 / bound 21` at the freeze; `41 / 11 / 25` at HEAD) and named two blind spots.
  `ExecC1Grammar` scored 20/20 attack fixtures with no false pass. `ReviewerC2` reproduced `arms_ok 4` and named a
  prose imprecision (five receipts, not three) and a trust gap. `MutationTester` reports 10 mutants, 8 killed by
  declared cases, **2 survivors** (below). `ConnectorCross` found sibling precedents (`mado`'s
  `.ufo/waves/round-17/label-check.py` binds an outcome token; it has no grammar extraction or typed equality) and
  absorbed nothing. `CriticClaims` died mid-work; its two suspicions were re-checked by the L1 and are recorded as
  limits (below).
- **Record corrections** (routed defects 1 and 2, carried unclaimed): the three false citations now name
  `c1-at-tip.json` and restate the landing value as 1 by construction (R76-C1 before→after cell, the
  `capability-row binding` capability row, the PROVINCE round-76 evidence line); the round-76 report's
  revision-prose correction is appended to `LOG.md` (round-77 entry), the filed report stays byte-identical.
- **Frontier step.** `corpus/SOURCES.md` 194 → 197 rows; three sources opened this round (two admits, one reject);
  the lesson's `## Gate` records every URL, access date, snapshot digest and located quote; one mistake mined
  (record-vs-receipt) plus two found in-round (fixture for the wrong reason; a control that cannot fail); the
  round's claims rest on S289 and S290.
- **Assimilation: none.** No `merge/kaidoku/` theme fits this routed-defect round inside the 1–3 claim cap, and
  this lane holds no `considerthese/` directory.

## Landed changes

Every change below is a lane commit between the base and the tip (`git log 188562d4..97280cad`, 17 commits); the
round-77 `LOG.md` entry (appended at `1d84253a`) is the narrative index for them.

| change | commit |
|---|---|
| declaration: the two instruments, the frozen plan, both selftests, the controls, census-start, three source snapshots | `819cf30e` |
| freeze: `claims.json` with both predicates and instrument pins, the two base receipts | `6767a879` |
| record corrections (three cells), S289–S291 rows, two knowledge entries, the lesson, three SKILL registry rows | `fd0b95bd` |
| round section, two capability rows, coverage-map row and frontier note, freeze-ledger row | `41543a54` |
| gate receipts as JSON carrying `exit` (freeze CLEAN; record CLEAN, 52 of 52 disclosures) | `440ee041` |
| wave-1 spec, dispatch payload, generator | `509c1051` |
| control generator repaired (wave F1) and controls re-taken | `63dc9c6f` |
| `gen-controls` supersession entry appended to the frozen claims container | `2ae8da54` |
| before-prose erratum ("three" → five receipts) and the third mined mistake | `11f0b19e` |
| wave evidence (12 seat records, results handoff, ready markers), SKILL registry pipe fix, QUALITY row 135, S289 anchor | `88e73357` |
| filing receipt (`prefile: PASS` at `88e73357`, exit 0) | `ff561504` |
| measured records, two C2 controls, the LOG entry, the measured pair at `ff561504` | `1d84253a` |
| the two C2 do-nothing controls re-created | `37f5d069` |
| tip gate (CLEAN, 52 of 52) and prefile receipt (PASS) at `37f5d069` | `88582548` |
| the measured records name the tip receipts | `6ff00080` |
| the tip measurement pair at `6ff00080` | `9dc94ad9` |
| the end census (exit 0, 197 rows, 23 W04) | `97280cad` |

Working-tree correction: two stale `prefile-rev-binding-*.json` receipts from an earlier wrong-revision attempt
were deleted before the tip receipts landed (they measured the receipt commit instead of the filing revision);
they never reached a commit.

## Before → after measurements

**R77-C1.** Counting command (as printed in the plan, executable with the two variables bound):

```sh
python3 -I -B tools/round-77/verdict-bind.py --root . --rev $REV --json-out $OUT
```

- before, at base `188562d4` (`pre/c1-at-base.json`): `exit 1`, `mismatch_count 4`, `bound_clauses 21`,
  `in_scope_rows 9` — the four defects are `D24 true` vs `false` and `mismatch_count 0` vs `1` in the
  `capability-row binding` row and in `PROVINCE.md` line 585.
- after, at `ff561504` (`l1/scores/c1-at-record.json`) and at `6ff00080` (`l1/scores/c1-at-tip.json`): `exit 0`,
  `mismatch_count 0`, `bound_clauses 25`, `in_scope_rows 11`, `groups 24`, `unbound_clauses 2`,
  `validate {defects []}`.
- do-nothing controls: `no-binding` scores `bound_clauses 0` (fails the ≥ 18 floor); `all-false` scores
  `mismatch_count 24`; the pointer-only control (round 76's audit at base) scores `mismatch_count 0` with the
  false annotation standing. None reaches the target.

**R77-C2.** Counting command:

```sh
python3 -I -B tools/round-77/prefile-receipt.py --root . --rev $REV --work $WORK --battery --json-out $OUT
```

- before, at base `188562d4` (`pre/c2-at-base.json`): `exit 1`, `arms_ok 4` of 6 — `record-receipt` absent, and
  the `gate-exits` arm names five round-76 gate receipts without `exit`.
- after, at `ff561504` (`l1/scores/c2-at-record.json`) and at `6ff00080` (`l1/scores/c2-at-tip.json`): `exit 0`,
  `arms_ok 6`, `arms_total 6`, `validate {defects []}`.
- filing receipt `l1/scores/prefile-at-filing.json`: `rev 88e73357`, `exit 0`, `prefile: PASS`, four-key child
  environment, stdout digest; `--check-receipt --expect-rev 88e73357` accepts it
  (`prefile-rev-binding-at-filing.json`, exit 0) and the same check at another revision refuses it
  (`prefile-rev-binding-stale.json`, exit 1, naming the revision).
- do-nothing controls: the gate alone retains nothing (`pre/controls/c2-gate-alone.json`), and a forged `arms_ok`
  is refused (`pre/controls/c2-forged-arms.json`, `--validate-battery` exit 1).

## Sources & frontier

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

- **before:** exit 0, 194 rows, 23 W04 warnings (`.ufo/waves/round-77/l1/census-start.txt`).
- **after:** exit 0, 197 rows, 23 W04 warnings (`.ufo/waves/round-77/l1/census-end.txt`).
- **rows added by tier:** tier A mined ×2 — S289 (RFC 8259 §3 Values, `grep -n` line 298, 14-word contiguous
  quote, snapshot 28 360 B, sha256 `61a5378f4255c720…`), S290 (GNU Bash Reference Manual §3.7.5 Exit Status,
  line 4435, 10-word quote, 1 040 954 B, sha256 `78d0eefbe60cfe73…`); tier C rejected ×1 — S291 (`ast.literal_eval`,
  line 2760, 13-word quote, 362 493 B, sha256 `8cacd731a2e0af73…`; reason: the annotation grammar is not a Python
  literal grammar and `literal_eval` would accept Python-only spellings the records never use; flip: the grammar
  becomes a Python literal grammar; consumer search `grep -c 'literal_eval' tools/round-77/verdict-bind.py` → 0).
- **rows touched old→new:** none — no existing row's `status`, `recheck` or `used-by` changed.
- **frontier rows advanced:** the coverage map gains
  `| Instrument and record layer, round 77 | 2026-11-04-r77-verdict-binding, 2026-11-04-r77-prefile-receipt | held … |`
  and the Frontier section gains the round-77 note (Core for `tools/round-77/{verdict-bind,prefile-receipt}.py`,
  moving no carrier ground; the frontier list is unchanged).

## Trend verdicts

- **expansion: unchanged.** The two new knowledge entries deepen the already-mapped instrument/record ground
  (`corpus/README.md` row "Instrument and record layer, round 77"), the frontier note says it "moves no carrier
  ground", and no new source kind or carrier class entered Core.
- **quality: improved.** A record check that could not see its own defect class is superseded: the pointer that
  resolved but carried a false verdict now fails at base (4 defects) and passes only after the record is
  corrected; the filing gate's verdict is retained with its exit, revision and digest and is re-derivable from the
  receipt bytes. Both instruments carry red fixtures and legitimate look-alikes, and the round's own F1 defect (a
  control that could not fail) was caught by a seat and repaired with a divergence assertion before the record.
- **discernment: improved.** The round's population is an outside document (the round-76 spot-check's routed set),
  the wave re-derived both counters independently (scout arithmetic, reviewer re-runs, 20/20 grammar attacks,
  10-mutant battery), and the wave's findings changed the record rather than decorating it: the control generator
  was repaired, the before-prose erratum was written, two mutation survivors and two grammar limits were routed
  instead of being called clean.

## Routed to round 78 (unclaimed work this round)

1. **Mutation survivors (2 of 10).** `c1-rev-show-to-worktree` (no selftest case exercises `show()`, so reading
   the working tree instead of the `--rev` blob is undetected) and `c2-nonint-exit-accepted` (the selftest refuses
   a missing `exit`, not a string/bool one). Closing them needs new selftest cases, and the frozen predicates name
   the case counts (15 and 13); the fix cannot land inside this freeze.
2. **Grammar near-misses are no-claims.** `(D24: true)` scores as prose and `(mismatch 0)` as an unknown field
   (unbound, counted but not a defect), so a re-punctuated false annotation makes no claim and escapes the binder.
   Next round: reject near-miss field names or require a minimal bound share per cell.
3. **C2 arm limits.** `record-receipt` checks the filing receipt's internal consistency (the revision binding is
   imposed by the kill rule and demonstrated in `prefile-rev-binding-*`), and `gate-exits` accepts any integer
   `exit` key rather than a full gate receipt.
4. **Two dead seats.** `ExecC2Receipt` and `ReviewerC1` returned zero bytes with no evidence and no retained error
   text; their slices (the C2 forgery battery, the C1 independent re-derivation) were partly covered by
   `ReviewerC2`, `ExecC1Grammar` and the L1's own runs, but not by an independent seat.

## SHONEN

`SHONEN.md` carries four boxes; none is `[x]` (no named non-author verifier has closed one this round).

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — three registry rows
  for the round's instruments (`SKILL.md`, "instrument-registry"), the eight-form grammar table in
  `corpus/knowledge/2026-11-04-r77-verdict-binding.md`, and S289/S290 cited in both entries.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — the two counters run end to end at
  base, filing and tip, with receipts named in the round-77 `LOG.md` entry and the record section.
- `[~]` Instructions executable by an agent without oral context — `plans/round-77-claims.md` prints both counting
  commands with their variables, and every command in this report was executed as printed with the variables
  bound.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — the round adds only the lane's own record layer;
  `ConnectorCross` names `mado`'s `label-check.py` as a sibling rule and absorbs nothing, and the PROVINCE
  additions name only `tools/round-77/*` and the round-29 gate.

## Stale-lane

Not stale: respawn-per-round driver, this round filed under its own number; no other mission of this lane is open.

## Tooling

No tool install or upgrade ran this round; no pacman transaction (host-wide pause respected).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/*` (orchestrator-owned run state),
`.ufo/l0-questions.md` (modified by another session), `.ufo/reports/round-79/mado.md` (another lane) and an empty
untracked `after/` directory. No file names kaidoku or round 77 outside the lane and this report; no seat wrote
into the fleet root.
