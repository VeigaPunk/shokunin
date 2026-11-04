# mado round 75 — report

author: mado L1 (hyaku run 15, attempt 1) · lane `mado-shokunin` · round 75
date: 2026-11-04 (America/Sao_Paulo)
base: `b149d2ece1a6d75f5738aa8bf4a9493f1a9c7da6`
frozen declaration and instruments: `def73656c94f0e88bd671cfb4a65124338261722`
lane tip at report time: `f1827f9d5f3fe29eb2bb7e1b8701cadd436f3069` (pushed; `ls-remote` shows it)
report commits (fleet repo): this file, and nothing else this round
shape: ONE v1 wave, 13 seats, band 8–16, attack share 4/13 = 30.8 %; no residual call; round
total 13 seats; no dead seats

## Work performed

The round declared **two claims**, each on a distinct axis with its own falsifiable before→after,
both frozen before any candidate data in `.ufo/waves/round-75/claims-declaration-r75.md`:

- **C1 — calibration (capability):** the landing harness credits the M-Z kill and greens the
  outcome only on the run's own echo of its per-run challenge. Closes the round-74 rule's declared
  limit ("not wired into the frozen round-72 harness").
- **C2 — operability:** the guard census counts a key-carrying mapping bound to any simple name
  and handed as `env=`, and treats a literal-key `del env[KEY]` between the guard construction and
  the launch as a cancellation — both on S453/S454 ground opened this round.

Work items, each with its evidence pointer:

- **Freeze and controls.** `claims-declaration-r75.md`; controls
  `controls/c1-harness-cases-r75.json` (11 cases, sha256 `f1e851a9…`) and
  `controls/c2-cases-r75.json` (47 cases, sha256 `d99502ba…`); pre-freeze do-nothing baseline
  `control-baseline-r75.txt` (held 6/11 and 41/47) — commit `def73656`.
- **C1 instruments.** `quality/counters/c1-r75-landing-controls.py` (successor generation: pinned
  r72 load, per-run `secrets.token_hex(8)`, witness-gated credit/outcome, redacting child-env
  evidence) and `quality/counters/c1-r75-harness-witness.py` (the counting command over eleven
  real `bash` fixture lanes); the standing instrument `quality/landing-counters.sh` gains the
  nonce-gated echo — commit `def73656`, repaired at `b545bea9`, `f75afbf6`, `4527fcae`,
  `a3c88663`.
- **C2 instrument.** `quality/counters/c2-r75-shapes.py` (the round-74 classifier plus the two
  deltas; 36 carried cases hash-checked) — commit `def73656`, repaired at `e3e29bb4`, `f75afbf6`.
- **Measurements.** `measurement-c1-r75-final.txt` at `a3c88663` (`cases=11 correct=11
  base_correct=6 verdict=TARGET_MET`, rc 0) and `measurement-c2-r75-final.txt` at `4527fcae`
  (`population=20 readers=13 guarded=13 unguarded=0 controls=47/47 base_controls=41/47
  verdict=TARGET_MET`, rc 0); earlier receipts at `def73656`, `e3e29bb4`, `f75afbf6` are kept
  beside them, append-only — commits `dd237a55`, `466e1307`, `1557198f`.
- **Wave.** `.ufo/waves/round-75/w1-spec.json`, `w1-dispatch.json` (13 spawn, 0 resume),
  `w1.ready`/`w1.ready.dispatched`, `w1-results.json` (13/13 settled), 13 seat reports and their
  receipts under `w1/` — commits `dd237a55`, `f1827f9d`. Roles: executor 3, scribe 2, scout 2,
  reviewer 2, critic 1, mutation-tester 1, connector 1, sentinel 1; the L1 held the planner seat
  (mapping recorded: planner → L1, with the data-walk riding `R75ScoutChain`/`R75Conn` items).
- **Corpus.** Two knowledge entries (`harness-witness-credit-r75.md`,
  `guard-carrier-copy-del-r75.md`), rows S453/S454, lesson with seven mined mistakes, four QUALITY
  criteria (124–127), index rows and frontier bullet — commit `745eca38`.
- **Bookkeeping and repairs.** `SKILL.md` three new gate rows plus the corrected/reclassed
  `mado-r74-witness-rule` row; `quality/tool-ledger.md` 130 → 133 rows; the gate's TMPDIR scratch
  repair with `PIN_MADO` re-cut; receipts under `.ufo/waves/round-75/receipts/` — commits
  `b545bea9`, `f75afbf6`, `4527fcae`, `a3c88663`, `87b85c9f`.
- **Records and harm watch.** `SCORECARD.md` round section, `LOG.md` round-75 entry,
  `PROVINCE.md` refinement, `receipts/harm-watch-r75.txt` — commits `f0cf818d`, `87b85c9f`.
- **Tools installed or upgraded: none** (no pacman transaction; the host-wide pause was honoured).

**Seat outcomes (from `w1-results.json`; no seat died, none was replaced).**
`R75ScoutChain` (JSON finding file), `R75ScoutSources` (three-fetch digest/quote report),
`R75ExecC1` (independent counter run + real-lane harness + selftest receipts), `R75ExecC2`
(independent run, hand-check of the eleven appended cases, carried-set comparison),
`R75ExecGate` (gate tallies, r74 selftest tallies, the TMPDIR red-before), `R75ScribeEntries` and
`R75ScribeLesson` (drafts, integrated by the L1), `R75RevC1` (`C1: survives with defects` — two
P2s), `R75RevC2` (`C2: survives with defects` — two P1s, both repaired at `e3e29bb4` and
re-probed), `R75Critic` (framing critique; outcome-scoring gap, duplicate mode, probabilistic
uppercase oracle), `R75Mutant` (C1: M1/M4 killed, M2/M3 survive; C2: 4/4 killed), `R75Conn`
(twelve cross-links, one `considerthese/` proposal, orphan and contradiction list), `R75Sentinel`
(no P1; the nonce disclosure, loader path, unpinned base generation, root scratch; the carried
gate scratch defect). Findings are integrated as named below; nothing is backfilled.

**Pre-freeze disclosure.** A three-case plumbing run of the C1 candidate (`right`,
`stale-witness`, `crash`) ran before the declaration was written, to validate the fixture
pipeline; no case, label, predicate, target or counter was re-cut afterwards. Disclosed in the
declaration and mined at `corpus/lessons/round-75.md` M75-2's neighbourhood.

## Landed changes

Every change below is tied to its `LOG.md` round-75 entry (one of the three bullets) and to the
lane commit that carries it.

| Change | Evidence | Commit |
|---|---|---|
| Freeze: declaration, two control sets, baseline receipt, three instruments, instrument echo | `claims-declaration-r75.md`, `controls/`, `control-baseline-r75.txt` | `def73656` |
| Measurement receipts and the wave plan/dispatch/registry | `measurement-c{1,2}-r75.txt`, `w1-spec.json`, `w1-dispatch.json` | `dd237a55` |
| Gate scratch repair (TMPDIR/`MADO_SELFTEST_SCRATCH`), `PIN_MADO` re-cut, challenge redaction, C2 base label, `SKILL.md` rows, ledger rows, gate receipts | `tools/mado-verify.sh`, `quality/counters/c1-r75-landing-controls.py`, `c2-r75-shapes.py`, `SKILL.md`, `quality/tool-ledger.md`, `receipts/` | `b545bea9` |
| Final measurements at the repair commit | `measurement-c{1,2}-r75-repair.txt`, `receipts/harness-real-r75.txt` | `79a4ff7b` |
| C2 `env=`-only usage; dead-branch deletes do not cancel | `quality/counters/c2-r75-shapes.py` | `e3e29bb4` |
| Private loader directory, `O_NOFOLLOW` write, pinned held generation, `/` refusal | `quality/counters/c1-r75-landing-controls.py`, `c2-r75-shapes.py` | `f75afbf6` |
| Loader creates the validated scratch root before its private dir | `quality/counters/c1-r75-landing-controls.py` | `4527fcae` |
| Absent-candidate contract (`correct=absent`, rc 1) | `quality/counters/c1-r75-harness-witness.py`, `receipts/absent-candidate-r75.txt` | `a3c88663` |
| Corpus: two entries, S453/S454, lesson, QUALITY 124–127, README index/frontier, census and fetch receipts | `corpus/` | `745eca38` |
| SCORECARD round section, LOG entry, PROVINCE refinement | `SCORECARD.md`, `LOG.md`, `PROVINCE.md` | `f0cf818d` |
| Harm-watch receipt; wave evidence (13 seat reports, results) | `receipts/harm-watch-r75.txt`, `w1-results.json`, `w1/` | `87b85c9f`, `f1827f9d` |

## Before → after measurements

| Claim | Counting command (frozen) | Before (held leg) | After (measured commit) |
|---|---|---|---|
| C1 calibration | `python3 -I quality/counters/c1-r75-harness-witness.py --repo . --rev <REV> --base-rev b149d2ece1a6d75f5738aa8bf4a9493f1a9c7da6 --controls .ufo/waves/round-75/controls/c1-harness-cases-r75.json --scratch-root DIR` | held round-72 harness on the eleven fixture modes: `base_correct=6/11` (`control-baseline-r75.txt`) | `MADO_R75_HARNESS_WITNESS: cases=11 correct=11 base_correct=6 verdict=TARGET_MET rev=a3c886634a4eaa9fa39cd6865c5e8b052c83c2cb`, rc 0; bounded 10.0000 (held 5.4545) |
| C2 operability | `python3 -I quality/counters/c2-r75-shapes.py --repo . --rev <REV> --base-rev b149d2ece1a6d75f5738aa8bf4a9493f1a9c7da6 --controls .ufo/waves/round-75/controls/c2-cases-r75.json --scratch-root DIR` | held round-74 classifier: `base_controls=41/47` (`control-baseline-r75.txt`) | `MADO_R75_GUARD_SHAPES: population=20 readers=13 guarded=13 unguarded=0 controls=47/47 base_controls=41/47 verdict=TARGET_MET rev=4527fcae6a8619e890172ca0a616ae8a3e20fd87`, rc 0; bounded 10.0000 (held 8.7234) |

Supporting measurements at the landing tip (`receipts/harm-watch-r75.txt`, commit `f0cf818d`):
index `93/93`; ledger `133/133 uncovered=0`; axis table `3/3 MATCH` (navigation 93/93,
calibration resolved-active 86/86, operability selftest 12/12); gate `MADO_SELFTEST: 460/460`;
census exit 0. No owned axis is harmed; the four scorecard harm-watch rows are unchanged (the
gate's count unchanged at its amended bytes, its pin moved).

## Sources & frontier

Registry 389 → 391 rows (`census-start-r75.txt`, `census-end-r75.txt`).

- Round-start census (base revision mirror: `git archive b149d2e` + the fleet `shokunin.conf` in
  scratch, so the used-by paths resolve): `scripts/sources-census.sh validate --root
  <scratch>/fleet-base mado` → exit 0, 45 warning lines.
- Round-end census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
  → exit 0, 47 lines (the 45 + the two new W04 duplicate-URL warnings).
- Rows added by tier: A 2 (S453, S454), B 0, C 0. Rows touched old→new: none in place; S446 is
  re-opened as a reject with its quote count corrected 23 → 21 in the lesson (round-74 D3), never
  edited in the registry. Both new rows are different-scope repetitions of held documents
  (`simple_stmts.rst` ← S440/S447/S451; `builtins/stdtypes.rst` ← S446), so neither carries
  `supersedes`; both are `mined`, `used-by corpus/knowledge/guard-carrier-copy-del-r75.md`,
  recheck 180d.
- Gate block (`corpus/lessons/round-75.md`): both URLs, the 2026-11-04 access date, three
  byte-identical fetches each (`fetch/simple_stmts.rst.{1,2,3}` sha256
  `d4320642…`, 41,375 B; `fetch/builtins_stdtypes.rst.{1,2,3}` sha256 `5a6951b7…`, 248,201 B),
  located quotes of 13 and 21 words at `:468-469` and `:5350-5352`, and the re-opened reject
  (S446). The three-fetch set was re-derived by the L1 independently of the sources scout.
- Frontier rows advanced: the two round-74 frontier surfaces (witness wiring; carrier grammar)
  moved into core; `corpus/README.md` gains the round-75 bullet and two index rows (index
  91 → 93).
- **Assimilation: none** — the round's claims are instrument work; nothing from
  `/home/vgpnk/Projects/shokuknow/merge/mado/` was adopted. The connector's `considerthese/` read
  is carried to round 76's planned item 4.
- **Sourced claim:** C2 rests on S453/S454, both opened this round with the Gate block above.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries on ground the round-74 frontier named
  (harness wiring; the copy/delete carrier shapes), each `source:`-bound (S453/S454 and own-work
  receipts); two new tier-A rows opened with three byte-identical fetches each; the index grows
  91 → 93 with zero removals.
- **quality: improved.** Ten wave-found defects repaired at named commits without touching a
  frozen predicate, label, control set or target; four QUALITY criteria land with red-before
  states; the gate's scratch repair carries a red-before receipt and is re-measured 460/460; both
  claims re-measured at their final instrument commits.
- **discernment: improved.** The round's own do-nothing controls (6/11 and 41/47) were re-derived
  independently by the critic and both reviewers; the wave found ten defects the L1's selftests
  did not (including two that would have shipped a false accept and a dead-branch regression), and
  each is either repaired with a flip receipt or carried as a named limit. The non-author closure
  spot-check of the gate decisions remains the external step.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  maintained; this round adds three gate rows and corrects one (commit `b545bea9`), and the
  entries cite S453/S454 and the receipts. No new non-author promotion clearance.
- [~] At least one end-to-end domain task executed and logged in LOG.md — round 75's two claims
  ran end to end (harness pipeline on eleven fixture lanes; census over the twenty-file
  population), logged in the round-75 entry (commit `f0cf818d`). Promotion-grade outside
  verification is still missing.
- [~] Instructions executable by an agent without oral context — the entries, the lesson, the
  declarations and the counters' docstrings are self-contained and pointer-complete; dispatched
  seats are still the lane's own, so this stays author-asserted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md gains an append-only
  round-75 refinement (commit `f0cf818d`); no sibling-owned surface was written.

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open. This round's mission
started 2026-11-04T02:59:55-03:00 and is progressing (lane commits this round; working tree clean
except the wave evidence committed at `f1827f9d`).

## Conformance notes and disclosures

- The frozen declaration's planning line says "ONE v1 wave of 12 seats"; thirteen seats were
  dispatched and settled (round-74 D4 repeated). The frozen file is not rewritten and the dispatch
  is the operative record (`w1-dispatch.json` `spawn=13`); recorded as lesson M75-7.
- The frozen C2 measurement receipt (`measurement-c2-r75.txt`) carries the stale evidence label
  "(the held round-73 rule must miss the target)" where the base leg is `c2-r74-shapes.py`; the
  instrument's message is corrected at `b545bea9`, the frozen receipt keeps its bytes, and the
  final receipt records the corrected message.
- The declaration's no-harm line listed `tools/mado-verify.sh` as byte-identical while the same
  declaration amended it (D5); the report and SCORECARD declare the amendment and the `PIN_MADO`
  re-cut instead (lesson M75-1).
- The C1 counter scores the M-Z decision only; the outcome clause is implemented and inspected but
  not certified by the frozen denominator (critic finding; carried as a named limit and planned
  item 1).
- L0 questions: none filed this round; the open r57–r60, L2-floor, host-recovery pacman-pause and
  r37/r38 session-material questions remain operator-owned and no work depended on them.
