# kake round 91 — report (author-side; admission belongs to the non-author closure)

Lane: `kake-shokunin`. Round 91, attempt 1. Base `5b20af16661040f383e9e84f85b838619857cb14`.
Freeze `f4fff130a52ae6de49af5de7d568d2ee320ebfb0` (`.ufo/waves/round-91/freeze.md`).
Lane head at filing: `5c46767019051ee042bc15febb2665f801ba4abd`.

## Work performed

The round declared two claims, each on a distinct axis and causally separable:

- **C1 — calibration** (lowest owned non-retired axis, 2 HOLD): the three routed round-90
  instrument defects close — R90-A (defect-queue shape: the round-90 counter admitted a stale
  receipted revision, a case-variant token and a receipt with no execution), R90-B (the tip
  conformance gate was never re-mutated after its hardening) and R90-C (`run_controls.sh` stopped
  replaying after the round-90 relocation). Counter `.ufo/waves/round-91/c91_defects.py`.
- **C2 — operability, capability acquisition**: a stored-response reuse decision instrument
  (`scripts/stored_reuse.py`) under `.ufo/waves/round-91/c2-contract.md` (21 clauses), scored by
  `.ufo/waves/round-91/c91_reuse.py` against 45 clause-tagged hand cases, a seeded generated
  population and five frozen forgery subjects.

Work items, each with its evidence:

- **Freeze and controls (L1).** Two frozen counters, the contract, five forgery subjects, the
  population pins and the pre-freeze control harness were committed at `f4fff130`. Do-nothing
  controls read `open=3 closed=0 met=false` (C1, `controls/base-c1.txt`) and
  `candidate=absent … met=false` (C2, `controls/base-c2.txt`); a junk fixture stayed `open=3`
  (`controls/ctl-c1.txt`); the five forgery subjects were each refused and a reachability control
  built from a frozen byte-copy of the counter's reference read `met=true`
  (`controls/ctl-c2.txt`); the harness reads `controls ok 18/18`. Four control defects were caught
  and fixed before the freeze (`corpus/lessons/round-91.md` §Mistakes 1–4).
- **C1 item A — the successor counter is shown able to say no.** The counter self-invokes a
  battery over four fixture repositories built from the measured revision: a stale-digest receipt
  leaves item B open, a case-variant token leaves item B open, a script that prints
  `controls ok 9/9` and exits 3 leaves item C open, and the constructed positive leaves no item
  open (`controls/freeze-state-c1.txt`, `controls/after-c1-carrier.txt`).
- **C1 item B — R90-B closed by a real mutation score (ExecMutationTip).** 34 single-point mutants
  of the tip gate `scripts/cache_key_conformance.py` (sha256 `d7bca38e…`) scored with the frozen
  round-90 counter: 20 killed, 14 survived, control `met=true`. Receipt
  `.ufo/waves/round-91/integration/mutation-tip.txt`; survivors named in `w1/ExecMutationTip.md`
  (sandbox branches `os.system`, `gc.get_objects`, `_posixsubprocess`, import/open audit; the
  generated-tally conjuncts; two hand-case deletions).
- **C1 item C — R90-C closed by a replay (L1 + ExecReplayC).** `run_controls.sh` re-pointed at
  `.ufo/waves/round-90/inherited/baseclean.out`, taking its root from `${LANE:-…}`, asserting each
  control and printing `controls ok K/K`: `ONLY=c1` replays `controls ok 9/9` at the tip
  (`controls/replay-tip.txt`, `w1/ExecReplayC.md`).
- **C2 tool (ExecReuseTool).** `scripts/stored_reuse.py` (433 lines, stdlib only, `--selftest`
  45/45), scored `met=true` by the frozen counter (`w1/ExecReuseTool.md`,
  `controls/after-c2-carrier.txt`).
- **C2 review (ReviewReuse).** 53 cases computed from the contract alone: 0 disagreements, exact
  output protocol, clause 3 uncovered by the frozen battery, four declared ambiguities, two
  counter leniencies (`w1/ReviewReuse.md`).
- **C2 mutation (MutReuse).** 17/17 required tool mutants killed; 5 surviving clause variants
  named; 9/10 counter mutants survived, four of which admit a subject the frozen counter refuses
  (`w1/MutReuse.md`).
- **C2 real-data trial (ExecReuseTrial).** 18 recorded surfaces from
  `.ufo/waves/round-61/capture/` and the r81/r82 captures converted under a declared adapter
  convention and decided offline: 4 `not-storable`, 4 `heuristic-undecided`, 10 `reuse` at capture
  time flipping to `revalidate` at +30 d; 36/36 agreement with the counter's reference; `met=true`
  at seeds 1, 2 and 3 (`w1/ExecReuseTrial.md`).
- **Knowledge and registry (ScribeKnowledge).** `corpus/knowledge/stored-response-reuse.md`,
  registry row S469 (tier A, spec, mined, recheck 180d), coverage-map row, frontier line and
  `PROVINCE.md` §Round 91; 20 located quotes verified as raw substrings at their line numbers;
  census `kake ok`, exit 0 (`w1/ScribeKnowledge.md`). Honest limit: the row rests on the retained
  RFC 9111 body re-hashed this round, not on a fresh fetch — the ScoutSources seat died before its
  GET.
- **Attack seats.** ReviewC1 falsified the frozen C1 counter four ways; CriticClaims measured C1 as
  not a calibration measurement, confirmed C2's separation and reached C2's `met=true` by
  importing the counter's reference through an absolute path (`w1/ReviewC1.md`,
  `w1/CriticClaims.md`).
- **Frontier step (L1).** `corpus/lessons/round-91.md` (§Gate, §Registry, §Mistakes 1–4,
  §Wave review, §Routed); census before/after; `merge/kake` id collision re-run (8 collisions,
  `.ufo/waves/round-91/assimilation/`); the 12-row quarantine slice re-derived and unchanged
  (`.ufo/waves/round-91/assimilation/README.md`).
- **Dead seats, named.** `ScoutGround`, `ExecReuseStubs` and `ConnectorScope` wrote no report and
  `ScoutSources` wrote a helper script and no `.md`; no seat was replaced. The L1 ran a bounded
  overlap scan in their place: `scripts/cache_control_effective.py` (r86) parses response
  Cache-Control with an HTTP-date reader, `scripts/cache_current_age.py` (r87) owns the age
  arithmetic, `vary_match.py` (r88) and `cache_key.py` (r89) own matching and keys — the new tool
  composes their ground but re-implements the directive grammar instead of delegating to r86
  (routed).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: counters, contract, forgery population, pins, control harness, re-pointed `run_controls.sh` | round-91 | `f4fff130` |
| `scripts/stored_reuse.py`, `corpus/knowledge/stored-response-reuse.md`, S469, README/PROVINCE/SKILL updates, wave evidence, mutation and replay receipts | round-91 | `cdc6c1dfa91b6c8d10db2c10254d4b31181bd6f3` |
| SCORECARD/LOG round-91 sections, lesson, final receipts | round-91 | `5c46767019051ee042bc15febb2665f801ba4abd` |

## Before → after measurements

**C1 (calibration).** Counting command:
`python3 -B .ufo/waves/round-91/c91_defects.py --root . --revision <REV> --work <scratch>`

- before, at `5b20af16`: `C1v91 … items=3 open=3 closed=0 met=false`, exit 1
  (`controls/base-c1.txt`).
- after, at `cdc6c1dfa91b6c8d10db2c10254d4b31181bd6f3`: `C1v91 … items=3 open=0 closed=3 met=true`, exit 0
  (`controls/after-c1-carrier.txt`).
- intermediate, at the freeze `f4fff130`: `open=1 closed=2`, only B open
  (`controls/freeze-state-c1.txt`) — A and C are closed by committed bytes before any wave data,
  which is the honest reading of what each item measures.

**C2 (operability).** Counting command:
`python3 -B .ufo/waves/round-91/c91_reuse.py --root . --revision <REV> --work <scratch>`

- before, at `5b20af16`: `C2v91 … candidate=absent hand=0/45 generated=0/120 forgeries_refused=0/5
  met=false`, exit 1 (`controls/base-c2.txt`).
- after, at `cdc6c1dfa91b6c8d10db2c10254d4b31181bd6f3`: `C2v91 … hand=45/45 generated=120/120 forgeries_refused=5/5 anti_table=ok
  population=ok met=true`, exit 0 (`controls/after-c2-carrier.txt`).

## Sources & frontier

`SOURCES.md` rows 205 → 206, tier A 180 → 181: **S469** (RFC 9111 §5.2.1 request directives,
§4.2.1 first-match freshness lifetime, §4.2.4 serving stale), status `mined`, `used-by`
`corpus/knowledge/stored-response-reuse.md`, recheck 180d. Rows touched: none. Rows added by tier:
1 × A. Frontier rows advanced: the coverage map gains the stored-response reuse row and
`corpus/README.md` gains the round-91 frontier line.

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kake` → exit 0 at round start (`assimilation/census-before.txt`,
29 × W04) and exit 0 at round end (`controls/census-after.txt`, 30 × W04, S469 is a third scope on
the RFC 9111 URL). Rows 205 → 206 by
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

Assimilation: none — the `merge/kake` package still collides on the same eight ids (S312, S329,
S367, S372, S373, S374, S390, S409; `.ufo/waves/round-91/assimilation/collisions`), and the
12-row quarantine slice is unchanged since round 86.

## Trend verdicts

- **expansion: improved.** One knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/stored-response-reuse.md`), one new registry row opened this round (S469) and
  a new instrument surface (`scripts/stored_reuse.py`) that composes r87–r90 instead of repeating
  them; knowledge `.md` 78 → 79 and the registry 205 → 206.
- **quality: improved.** The round's own attack seats falsified both frozen counters and every
  finding is routed with a receipt rather than left standing; the tip gate finally has a mutation
  score (34/20/14, R90-B); the control harness was corrected four times before the freeze and four
  more after the wave (`w1/ExecReplayC.md` F1–F3, F5); ReviewReuse found no contract disagreement
  in 53 independent cases. No file was deleted and no filed row was rewritten.
- **discernment: improved.** Four control defects were caught by the round's own pre-freeze
  controls (Mistakes 1–4) and four counter forgeries by the wave (ReviewC1 a2/c/e2/f,
  CriticClaims); the round reports both claims as measured on frozen predicates and *not admitted*,
  because the counters that measure them are forgeable in classes the round could not fix after
  data. The outside spot-check still owns admission.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. The round was worked by one L1
(`KakeR91`) in one v1 wave plus L1 integration.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `corpus/knowledge/shonen-ledger.json` box 1; this round appends `stored_reuse` and
  `c91 reuse capability` registry rows to `SKILL.md`.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — box 2 stays `[ ]` on the
  round-47 receipt gap recorded in the ledger; the round-91 LOG entry adds an end-to-end trial
  (`w1/ExecReuseTrial.md`) but does not close the historical gap.
- [~] Instructions executable by an agent without oral context — pointer: box 3; the new tool's
  docstring and the knowledge entry's checklist carry the runnable commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: box 4; `PROVINCE.md` gains
  §Round 91 with the stated boundary and no sibling-lane path was added.

## Tooling

No tool installed or upgraded; no pacman transaction; network limited to the two RFC GETs named in
the wave items.
