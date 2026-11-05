# kake round 92 — report (author-side; admission belongs to the non-author closure)

Lane: `kake-shokunin`. Round 92, **attempt 2** (attempt 1 landed the lane work and ended without a
report — `.ufo/watchdog.log:2603`, `lane-dead-no-report kake round=92`). Base
`e143faff1b86aad172dd87696da900c70347b8b2`; freeze `a5640ca02c20f94a0fa03af41b977b46ae99808e`
(`.ufo/waves/round-92/freeze.md`); carrier `2a4447c1a4696cbfb40b17014e47fc6af716c06d`. Lane head at
filing: `027faf79bba2600c0852f1ec2b51774c868cf321` (`git ls-remote origin refs/heads/master` prints it).

The round declared two claims, each on a distinct axis and causally separable:

- **C1 — calibration** (lowest owned non-retired axis, score 2 HOLD): the four routed round-91
  instrument defects **K91-1, K91-2, K91-4 and K91-5** close on committed bytes. Item A ← K91-1
  (a receipt with no execution was admitted), item B ← K91-2 (no registry row for the round's
  counter), item C ← K91-5 (a replay counted checks without asserting their labels), and the
  `battery`/`differential` conjuncts ← K91-4 (membership instead of exact open sets and reason
  strings). Counter `.ufo/waves/round-92/c92_defects.py`.
- **C2 — freshness** (score 10 HOLD, **capability acquisition** on open frontier ground): a
  heuristic freshness decision instrument `scripts/heuristic_freshness.py` implements
  `.ufo/waves/round-92/c2-contract.md` (13 clauses, RFC 9111 §4.2.2, opened this round). Counter
  `.ufo/waves/round-92/c92_heuristic.py`.

## Work performed

- **Freeze, counters, contract and pre-freeze controls (L1).** Two frozen counters, the 13-clause
  contract, five forgery subjects (`frozen/neg-*.py`), the population pin
  (`frozen/c2-population.sha256`) and the self-pin (`frozen/c1-self.sha256`) committed at
  `a5640ca0`. Do-nothing controls read `open=3 closed=0 battery=hit differential=fail self=hit
  met=false` (C1) and `candidate=absent … met=false` (C2), both exit 1 (`controls/base-c1.txt`,
  `controls/base-c2.txt`). Two positive controls prove `met=true` is reachable on conforming bytes
  and that the battery discriminates (`controls/ctl-c1-known-good.txt`,
  `controls/ctl-c2-positive.txt`, which also carries the sandbox differential: the oracle-import
  forgery answers correctly **without** the audit-hook sandbox and is refused **with** it). Four
  control defects were found and fixed before the freeze commit (`corpus/lessons/round-92.md`
  §Mistakes 1–4); no counter, case, predicate or label was changed after it.
- **C1 item A — mutation runner (ExecMutation).** `integration/mutate-tip.py` (stdlib only, N=30,
  K=20, S=10) plus `integration/mutation-tip.txt` and `mutation-tip.log`; the receipt digest equals
  the gate blob `d7bca38ec146…` and the log records a `base` and an `M01` run that differ
  (`w1/ExecMutation.md`).
- **C1 item B — registry row (ScribeRegistry).** `SKILL.md:1663` registers `c92_defects.py` with its
  `--revision` command, exit codes, `--selftest` (12/12) and its `met` predicate; `SKILL.md:1667`
  carries the "how to verify" line for both counters (`w1/ScribeRegistry.md`).
- **C1 item C — replay with label assertions (L1).** `controls/run_controls.sh` replays under
  `ONLY=c1` and asserts each of the nine declared labels; the counter's `C_labels` conjunct reads
  them from the replay (`controls/after-c1-carrier.txt` JSON line).
- **C1 battery and differential (L1).** The five-fixture battery builds each fixture from the
  measured revision and reads its **exact** open set and declared reason substring (FA stale
  receipt, FB canned runner, FC constant labels, …), and the frozen round-91 counter is run on the
  same canned-runner fixture it accepts — that is the `differential` conjunct.
- **C2 instrument (ExecHeuristic + L1 integration).** `scripts/heuristic_freshness.py` (22 985
  bytes, sha256 `7bfe82da8e1a…`, stdlib only, `--selftest`), committed at `2a4447c1`
  (`w1/ExecHeuristic.md`).
- **C2 independent review (ReviewC2).** 97 cases computed from the contract alone: 93/97
  agreement, **0 tool defects**, all four disagreements resolving to three contract ambiguities
  named before running (`w1/ReviewC2.md`, `w1/ReviewC2/agreement.txt`).
- **C2 stubs (ExecStubs).** 14 held-out subjects scored: both contract-faithful subjects admitted,
  seven clause-violating subjects refused, **five admitted** (clauses 2, 3, 4, 6, 8 uncovered);
  F6 shows the counter's own reference accepting `max-age="5"`, which clause 4 refuses
  (`w1/ExecStubs.md`).
- **C2 mutation (MutHeuristic).** 13 of 24 single-clause tool mutants survive the frozen counter
  and 9 hand-built clause-violating subjects read `met=true`; the sandbox, the forgery battery and
  the population pins hold (4 of 16 counter mutants are killed by a frozen subject)
  (`w1/MutHeuristic/Mutations.md`).
- **C1 attack (ReviewC1).** The frozen C1 counter is falsified three ways, each reaching `met=true`
  in a fixture clone: a runner that mutates nothing and prints canned per-target verdicts, a
  control harness that echoes the nine frozen labels, and a counter blob edited with its self-pin
  rewritten in the same commit — classes 3, 5c, 6 (`w1/ReviewC1/Attack.md`).
- **C1 attack (CriticClaims).** Three more constructions: F1 a receipt whose log and runner execute
  a *different* gate than the digest names (`333230ce`), F2 a registry row naming a counter that
  refuses every revision (`605a0026`), F3 a harness whose labels are constants; it also confirmed
  C1/C2 separability in both directions and re-measured the do-nothing control at the freeze
  (`w1/CriticClaims/C1.md`).
- **Real domain work (ExecTrial).** The instrument decided all 18 recorded surfaces (12 round-61,
  3 round-81, 3 round-82 captures) from their recorded headers, with the headers each decision
  rests on tabulated: 18/18 exit 0, 18/18 agreeing with a pre-run hand derivation from the contract
  (`w1/ExecTrial/trial.txt`). No live property was fetched and no cache was observed.
- **Entry and frontier drafting (ScribeEntry, ScribeRegistry, ScoutGround).** The knowledge entry
  `corpus/knowledge/heuristic-freshness.md` (480 lines), the README frontier section and row
  (`corpus/README.md:136`, `:736-753`), the S470 draft, and the insertion-point / `heuristic-undecided`
  seam map for `scripts/stored_reuse.py` (`w1/ScribeEntry.md`, `w1/ScoutGround.md`).
- **Source opening (ScoutSources).** Live GET `https://www.rfc-editor.org/rfc/rfc9111.txt` → 200,
  84 477 B, sha256 `aeb52adb3279d5f23dae34f68af11bd5cef0a0aff7ffcd014c9ca93c5302cf3e`, byte-identical
  to the retained body; four errata checked, none names §4.2.x (`w1/ScoutSources/Sources.md`).
- **Sibling-overlap scan (ConnectorScope).** No sibling lane holds RFC 9111 §4.2.2 ground and S470
  is not a within-scope duplicate (`w1/ConnectorScope.md`).
- **considerthese assimilation (L1).** `considerthese/2026-10-26.md` proposal 5 landed as
  `corpus/QUALITY.md` §Round 92 ("a cited counter reading names its revision and whether it is by
  design"), grounded by `.ufo/waves/round-92/considerthese/historical-gate-at-freeze.txt`
  (`c56_quote_truth.py` exit 1 at `a5640ca0` on `C8_mirror_bytes`, a pinned historical population).
- **Attempt-2 re-verification (L1).** Both frozen counters were re-run at the base and at the
  carrier: `open=3 … met=false` exit 1 / `open=0 closed=3 battery=exact differential=ok self=ok
  met=true` exit 0, and `candidate=absent … met=false` exit 1 / `hand=28/28 generated=120/120
  forgeries_refused=5/5 anti_table=ok population=ok met=true` exit 0 — receipt
  `controls/attempt2-reverify.txt`. No inherited artifact needed repair.

## Landed changes

Every change below is recorded in `LOG.md` §"Round 92" and carried by the commit named beside it.

| Change | Commit |
|---|---|
| Frozen C1/C2 claims, both counters, the 13-clause contract, the pre-freeze control harness, the forgery subjects and pins, the RFC 9111 §4.2.2 source body | `a5640ca02c20f94a0fa03af41b977b46ae99808e` |
| Wave-1 spec, validated dispatch payload, seat registry and the `.ready` handoff (14 seats) | `f0b2dc635e34cc1c593655d926af74f19bd21034` |
| Wave-1 evidence (13 seat reports + receipts, `w1-results.json`, the dispatch marker), `scripts/heuristic_freshness.py`, `corpus/knowledge/heuristic-freshness.md`, S470, the SKILL/README/QUALITY registrations and the mutation-runner artifacts | `2a4447c1a4696cbfb40b17014e47fc6af716c06d` |
| SCORECARD and LOG round-92 sections, `corpus/lessons/round-92.md` (Gate/Registry/Mistakes/Wave review/Routed) and the carrier receipts | `9f15115bc8f07c5ca88105530086924faf65247e` |
| Attempt-2 re-verification receipt (`controls/attempt2-reverify.txt`) and the close-order mistake 5 / "Attempt 2 — inherited state" note in the lesson | `027faf79bba2600c0852f1ec2b51774c868cf321` |

No file was deleted between base and carrier: `git diff --diff-filter=D --name-only e143faff
2a4447c1` prints nothing; `git diff --numstat` outside `.ufo/` is **1059 added / 0 removed**.

## Before → after measurements

| Claim | Counting command | Before (base `e143faff`) | After (carrier `2a4447c1`) | Verdict |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-92/c92_defects.py --root . --revision <REV> --work <scratch>` | `items=3 open=3 closed=0 battery=hit differential=fail self=hit met=false`, exit 1 (`controls/base-c1.txt`; re-measured by attempt 2 in `controls/attempt2-reverify.txt`) | `items=3 open=0 closed=3 battery=exact differential=ok self=ok met=true`, exit 0 (`controls/after-c1-carrier.txt`; re-measured by attempt 2) | **met on the frozen predicate, falsified as worded** — not admitted (R92-1…R92-3) |
| C2 | `python3 -B .ufo/waves/round-92/c92_heuristic.py --root . --revision <REV> --work <scratch>` | `candidate=absent hand=0/28 generated=0/120 forgeries_refused=0/5 anti_table=n/a population=n/a seed=92 met=false`, exit 1 (`controls/base-c2.txt`; re-measured) | `candidate=present hand=28/28 generated=120/120 forgeries_refused=5/5 anti_table=ok population=ok seed=92 met=true`, exit 0 (`controls/after-c2-carrier.txt`; re-measured) | **met on the frozen predicate**; contract conformance rests on the independent 93/97 review, not on the counter |

Both readings are verdicts about this round's work measured at the named revision; the base
readings are do-nothing controls, per `corpus/QUALITY.md` §Round 92.

Honest verdicts:

- **C1: not admitted.** The frozen predicate reads `met=true`, and the round's own attack seats
  reached `met=true` doing none of the claimed work (a canned-verdict runner, a constant-label
  harness, a rewritten self-pin, a runner executing a different gate, a row naming a refusing
  counter). The claim as worded ("the defects close") is falsified; the counter is not repaired
  after scoring (freeze kill rule) and the defects are routed as **R92-1** (bind item A's execution
  to the named gate and to a sample chosen after the receipt is read), **R92-2** (bind the
  harness's labels to runs through a nonce), **R92-3** (a row is text — either say "registered" or
  resolve and run the row's command).
- **C2: met as a capability acquisition.** The instrument runs, its output verifies against the
  contract on an independent 97-case review (93/97, 0 tool defects, four disagreements = three
  contract ambiguities), it decides 18/18 recorded surfaces, and its capability row is in
  `SCORECARD.md`. Its frozen counter under-proves conformance (13/24 tool mutants survive, 9
  clause-violating subjects admitted, the counter's reference accepts `max-age="5"`) — routed as
  **R92-4** and **R92-5**, not patched.
- **No axis score moved.** Both claims were sized to close defects / acquire a capability, not to
  raise a HOLD score; no axis is claimed improved past HOLD.

## Sources & frontier

Counting command (both ends), frozen in `CORPUS.md` §*SOURCES.md — where a shokunin learns*:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

- **Before:** exit **0** at the round open (receipt `.ufo/waves/round-92/assimilation/census-before.txt`),
  206 registry rows.
- **After:** exit **0** at round end, re-run by attempt 2 at 2026-11-04T22:03-03:00, 31 W04
  advisories (the count the `ok` line carries; S470 is a fourth scope on the same RFC text),
  207 registry rows. Row count command: `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`
  → 206 at `e143faff`, 207 at `027faf79`.
- **Rows added by tier:** tier **A 1** (S470, kind `spec`, status `mined`, recheck 180d, `used-by`
  `corpus/knowledge/heuristic-freshness.md`); tier B 0; tier C 0.
- **Rows touched old→new:** none. No status, `recheck` or `used-by` cell of an existing row was
  changed this round.
- **Frontier rows advanced:** one — "Heuristic freshness decision (may a heuristic expiration time
  be assigned to a stored response, and what lifetime it carries…)" enters the frontier ground map
  at `corpus/README.md:136` (round r92, entry + `scripts/heuristic_freshness.py`, S470), with the
  frontier narrative at `corpus/README.md:736-753`. Knowledge entries 79 → 80
  (`git ls-tree -r --name-only 027faf79 -- corpus/knowledge | grep -c '\.md$'` → 80).
- **Sourced claim:** C2 rests on S470, opened this round (`w1/ScoutSources/Sources.md`: GET 200,
  84 477 B, sha256 `aeb52adb…`, located quotes at §4.2.2 lines 688–693, 695–696, 697–701,
  707–709). The Gate block in `corpus/lessons/round-92.md` records four located admits and three
  rejects (the 86400 cap is not the RFC's; the cacheable status set defers to RFC 9110 §15.1; the
  errata page grounds nothing about §4.2.x).
- **Assimilation: none.** `merge/kake` still collides on eight ids with the lane registry
  (`assimilation/collisions`: S312 S329 S367 S372 S373 S374 S390 S409; registry 206 ids,
  staged 129 from S287). A nonempty collision file closes adoption in scratch only; nothing was
  renumbered or appended.
- **considerthese:** `considerthese/2026-10-26.md` proposal 5 landed as `corpus/QUALITY.md`
  §Round 92, grounded on a measured instance, not on the proposal's text.

## Trend verdicts

- **expansion: improved.** One new capability on ground the coverage map did not hold
  (`scripts/heuristic_freshness.py` + `corpus/knowledge/heuristic-freshness.md`), one registry row
  opened this round (S470, tier A), one frontier row advanced (`corpus/README.md:136`), and a
  composed surface that reads the lane's existing cache instruments instead of repeating them —
  knowledge `.md` 79 → 80, registry 206 → 207, plus the demonstrated repertoire row in
  `SCORECARD.md` §"Demonstrated repertoire — round 92".
- **quality: unchanged.** No existing surface was weakened or deleted (0 deletions; 1059 added
  lines outside `.ufo/`), and the round's attack seats falsified **both** frozen instruments —
  C1 forgeable in three construction classes and C2's population leaving five clauses unexercised —
  so no quality gain is claimed: the counters entered as tools with their predicates and their
  falsification on the record, and the seven findings are routed (R92-1…R92-5 plus R92-6/R92-7)
  rather than patched after data. The one quality asset added is `corpus/QUALITY.md` §Round 92
  (a cited reading must name its revision and whether it is by design).
- **discernment: improved.** The lane can now tell a `met=true` counter from a real closure: the
  round's own seats falsified its C1 claim by construction (`w1/ReviewC1/Attack.md` classes 3/5c/6,
  `w1/CriticClaims/C1.md` F1–F3), measured the C2 counter's coverage gap (`w1/ExecStubs.md`,
  `w1/MutHeuristic/Mutations.md`), and an independent 97-case review found 0 tool defects behind
  four apparent disagreements that were contract ambiguities (`w1/ReviewC2.md`). Four control
  defects were caught by the round's own pre-freeze controls (Mistakes 1–4), and attempt 2
  re-measured the inherited readings instead of trusting them (Mistake 5). The outside spot-check
  still owns admission.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Round worked by one L1 in one v1
wave (14 seats) plus L1 freeze/integration/measurement; attempt 2 re-verified and closed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `corpus/knowledge/shonen-ledger.json` row `box 1`; this round adds two registry rows
  (`SKILL.md:1663` `c92_defects.py`, `SKILL.md:1665` `heuristic_freshness.py`) and the verification
  line at `SKILL.md:1667`.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — the ledger row `box 2`
  records a gap (one named receipt, `.ufo/waves/round-47/verification/offline-sweep-r46-verdict-time.txt`,
  does not exist at the revision) and that receipt still does not exist at `027faf79`, so the box
  stays `[ ]`; the round's LOG section adds a logged end-to-end run (`w1/ExecTrial/trial.txt`,
  18/18 surfaces) but does not close the historical gap.
- [~] Instructions executable by an agent without oral context — pointer: box 3; the new counter's
  `--revision`/`--work` command and the instrument's stdin/stdout contract plus `--selftest` are in
  `SKILL.md:1663-1667` and `corpus/knowledge/heuristic-freshness.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: box 4; the round's new entry
  cites RFC 9111 §4.2.2 only, `ConnectorScope` found 0 sibling overlap, and no sibling-lane path
  was added to `corpus/knowledge/*.md`.

## Round mechanics

- **Shape:** one v1 wave under `.ufo/waves/round-92/w1-spec.json` (band 8–16, `maxLanes` 14,
  dispatch `w1-dispatch.json`, ready handoff `w1.ready` taken at 2026-11-04T21:30:21,
  `w1.ready.dispatched`).
- **Seat mix (14):** executor 4, scout 2, scribe 2, reviewer 2, connector 1, sentinel 1, critic 1,
  mutation-tester 1. Attack seats (reviewer, critic, mutation-tester) = **4/14 = 28.6 %**;
  connector seats 1 (≤2). The L1 holds the canonical planner seat; the bounded planning data-walk
  rode `ScoutGround` — the validator rejects `planner` as a swarm role (orchestrator ruling
  2026-10-19; the open L0 question `kake | round-86` still asks for the ruling).
- **Dead seats:** `SentinelQuote` settled with no file in `.ufo/waves/round-92/w1/SentinelQuote/`
  and no report; its quote/scope check was not performed and is routed as **R92-6**. It was not
  replaced. The other 13 seats returned reports or receipts.
- **Residual call:** none. **Round total: 14 seats.**
- **Inherited state:** attempt 1's work was committed (`a5640ca0`…`9f15115b`) with a clean tree, so
  nothing was discarded; every inherited reading was re-measured by attempt 2 before filing
  (`controls/attempt2-reverify.txt`). Attempt 2 added only that receipt, the lesson's mistake 5 and
  the "Attempt 2 — inherited state" note.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file this
  lane's seats wrote into the fleet root. Untracked fleet-root entries belong to other lanes or the
  orchestrator and were left untouched: `after` (24 B, mtime 2026-11-03 20:05, content
  `=== SCORECARD diff base-`), `.ufo/reports/round-36/kagi.md`, and the `.scratch/` run state
  (orchestrator-owned by rule, never a misroot).
- **Scratch:** all counter work ran under `/fast/scratch/hyaku/kake-r92/KakeR92a2/`, removed after
  the last measurement; no `/tmp` path is cited.
- **Open L0 questions (not answered, routed around):** `kake | round-86` (planner seat vs the
  validator's role set) and `kake | round-89` (three items: item A's in-line correction tag vs
  append-only SCORECARD tails; the C2 shortcut-guard freeze v2 ordering; the seven non-conforming
  stubs admitted by the round-89 C2 instrument). No new question was filed this round; nothing was
  blocked on them.

## Tooling

No tool installed or upgraded; no pacman transaction (the host-wide pause holds). Network was
limited to the one RFC 9111 GET and the four errata HEADs named in the wave items.
