# mado — round 76 report

**Lane:** mado-shokunin · **Round:** 76 (hyaku run 15, attempt 1) · **Lane base:**
`c3e0bc5f10b72964d54d18dc9b0706dc308dd1bf` · **Lane HEAD at filing:**
`2308e12ab19949cd86832c5ba4bcb29855a9a4f5` (`ls-remote origin refs/heads/master` agrees).

**Declared claims (2).**

1. **C1 · calibration** — a successor counter certifies the landing harness's **contract outcome
   field** (`verdict=`), not only its M-Z kill decision (`mz=`): sixteen frozen fixture cases, four
   named mutations of the harness's `outcome_green` rule killed 4/4 where the held mz-only rule
   kills 0/4.
2. **C2 · operability** — the guard census counts an **interprocedural cancellation** (a callee
   that deletes the guard key from the mapping it receives) and a **dynamic-key `del`**, scoring
   59/59 against the held classifier's 55/59 while the population verdict stays 20/13/13/0.

**Round shape.** ONE v1 wave, 13 seats (`w1-spec.json`, validated under
`scripts/hyaku/ufo-wave-policy.json`, band 8–16; `spawn=13 resume=0 total=13`). Role mix: scout 2,
executor 3, scribe 2, reviewer 2, critic 1, mutation-tester 1, connector 1, sentinel 1. Attack
seats 4/13 = 30.8 % (≥25 % required); connector seats 1 (≤2). Residual call: none. **Round total:
13 seats.** Dead seats: none (`w1-results.json`, 13/13 settled with substantive final output).
The L1 held the planner seat (the validator rejects `planner` as a swarm role); no planner was
dispatched. The wave was dispatched through the inline handoff (`w1.ready` →
`w1.ready.dispatched`), not by a self-issued `task` call.

## Work performed

- **C1 instrument.** `quality/counters/c1-r76-outcome-field.py` runs sixteen real `bash` fixture
  lanes through the actual harness pipeline and scores **both** `mz=` and `verdict=` per case,
  then applies four named mutations of the harness's single `outcome_green` return line
  (`outcome-summary-only`, `outcome-killed-only`, `outcome-killed-any`, `outcome-killed-or`) and
  scores each against the frozen label set. Receipt:
  `measurement-c1-r76-final.txt` → `cases=16 correct=16 mutants=4 killed=4 base_killed=0
  verdict=TARGET_MET`, rc 0, at `3588a527`.
- **C1 successor harness.** `quality/counters/c1-r76-landing-controls.py` adds two mechanical
  fixes to the frozen round-75 generation: the witness grammar reads **16+ hex** (an over-long
  echo is a parsed mismatch, making prefix-vs-equality observable) and the per-run challenge is
  drawn by **rejection sampling until it contains an `a-f` letter** (deterministic uppercase
  oracle, closing round-75 M75-4). The contract row is unchanged in shape; the named
  `outcome_green(...)` rule is the single mutation anchor.
- **C2 instrument.** `quality/counters/c2-r76-shapes.py` adds D3 (a live `del m[KEY]` in a local
  function that receives the mapping, under the dominance test) and D4 (`del env[k]` where `k` is
  bound exactly once, earlier, to the guard key or a module constant), carries the forty-seven
  round-75 cases byte-identically (hash-checked) and appends twelve. Receipt:
  `measurement-c2-r76-final.txt` → `population=20 readers=13 guarded=13 unguarded=0 controls=59/59
  base_controls=55/59 verdict=TARGET_MET`, rc 0, at `3588a527`.
- **Negative result (lands with C1).** The round-75 plan's first item — kill the echo-dropping
  outcome mutation — is impossible through `verdict=`: the field is green only when `killed == 2`,
  and the M-Z kill already requires the echo, so that mutation changes no reachable published
  field. Recorded in `corpus/knowledge/outcome-field-r76.md` §2 and lesson M76-2; the claim moved
  to the four observable outcome-rule mutations, with `always-red` as the shape that separates a
  rule ignoring the green conjunct.
- **Corpus.** Two knowledge entries (`outcome-field-r76.md`, `interprocedural-del-r76.md`), the
  lesson with six mined mistakes and two repair passes, QUALITY 128–131, two index rows and a
  frontier bullet, rows S455/S456 with S450/S453/S454 `used-by` extended, PROVINCE refinement.
- **Bookkeeping.** `quality/tool-ledger.md` 133 → 136 rows (three new instruments); three SKILL
  registry rows; SCORECARD round section, repair section and axis line; LOG entry.
- **Wave.** `w1/` carries the thirteen seat reports and their receipts; `w1-results.json` records
  every settle. Per-seat disclosures below.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze v1: declaration, both frozen control sets, pre-freeze control, three instruments | round 76 bullets 1–3 | `755b339f1f6ec18f45b494d40515aecdbe9ceb73` |
| Freeze v2: label set v3 with its evidence derivation, the named `outcome_green` rule, the observable mutant class | round 76 bullet 2 | `cb713254ee9926e036e594312fdc61b57825526b` |
| Corpus: entries, lesson, QUALITY 128–131, README rows/frontier, SOURCES rows, ledger, SKILL registry, SCORECARD, LOG, PROVINCE, fetch receipts | round 76 bullets 1–5 | `81ca5d1b9173a198331209dfb00a6e92a15fd569` |
| Matched control for the frozen set, `used-by` extensions, M76-5 | round 76 bullet 4 | `c9e366f1111489ce4bd238bdad2fc24377aaa44a` |
| C2 repair: D3 parameter binding (R76RevC2 P2 / R76Mutant `d3-anyarg`) | round 76 repair bullet 1 | `5dade9b3043ca1aab16523ffeb4a177ae9cd9f89` |
| Harm watch, census end, C2 final measurement, measured-revision statements | round 76 bullet 5 | `e160d18e5b1c90d1bd052b30c15b33634e01e92f` |
| Wave-found repairs F1/F3/F4/F6 | round 76 repair bullets 2–6 | `6806b4dc8b46fb07e8759983f323267f6b32b763` |
| C1 final measurement at the corrected instrument | round 76 bullet 1 | `0e69154100a9c0ed2f0d4f9a3e591376bc8a7181` |
| Carried C1 limits (last-row parse, grammar survivor, self-consistency) | round 76 repair bullet 7 | `fb89b1d5e92cf3a1bbb06f0706cf0affc1f3b06d` |
| Second repair pass: C1 `--base-rev` binding, C2 allowlisted env, scope-local cancellations | round 76 second repair pass | `3588a527eba555a94e497097b0467efc04274c6d` |
| Wave evidence: 13 seat reports, results.json, final measurements | round 76 wave bullets | `587b2989be082080a23a3a565151f5a419b6e11e` |
| Final harm watch and census | round 76 bullet 5 | `2308e12ab19949cd86832c5ba4bcb29855a9a4f5` |

Every change above is committed and pushed inside the lane repo; the lane tip is on
`origin/master` (`ls-remote` printed `2308e12a…`).

## Before → after measurements

All numbers below are **re-executed** this round unless marked *evidence-verified*; a number with
neither label is a defect (QUALITY 131).

**C1 — calibration** (measured at `3588a527`, its instrument's last change; earlier receipts at
`cb713254` and `6806b4dc` show identical counts):

```sh
python3 -I quality/counters/c1-r76-outcome-field.py --repo . --rev 3588a527eba555a94e497097b0467efc04274c6d \
  --base-rev c3e0bc5f10b72964d54d18dc9b0706dc308dd1bf \
  --controls .ufo/waves/round-76/controls/c1-outcome-cases-r76.json \
  --scratch-root <scratch>
```

| | before (held mz-only rule) | after (successor counter) |
|---|---|---|
| outcome-rule mutants killed | 0/4 (`control-baseline-r76-matched.txt`) | 4/4 (scores 15/16, 15/16, 15/16, 14/16) |
| case score | not scoreable (no `verdict=` parse) | 16/16 |
| control receipt | `control-baseline-r76-matched.txt` | `measurement-c1-r76-final.txt` |
| contract | — | `cases=16 correct=16 mutants=4 killed=4 base_killed=0 verdict=TARGET_MET`, rc 0 |

**C2 — operability** (measured at `3588a527`; identical counts at `755b339f`, `cb713254`,
`5dade9b3`):

```sh
python3 -I quality/counters/c2-r76-shapes.py --repo . --rev 3588a527eba555a94e497097b0467efc04274c6d \
  --base-rev c3e0bc5f10b72964d54d18dc9b0706dc308dd1bf \
  --controls .ufo/waves/round-76/controls/c2-cases-r76.json \
  --scratch-root <scratch>
```

| | before (held round-75 classifier) | after (successor census) |
|---|---|---|
| frozen control cases | 55/59 (misses exactly the four new positives) | 59/59 |
| population | 20 files / 13 readers / 13 guarded / 0 unguarded | same |
| contract | — | `population=20 readers=13 guarded=13 unguarded=0 controls=59/59 base_controls=55/59 verdict=TARGET_MET`, rc 0 |

**No-harm watch** (`receipts/harm-watch-r76.txt`, re-executed at `587b2989`; the tip commit adds
only that receipt and the census):

| Check | Result |
|---|---|
| `bash tools/mado-verify.sh --selftest` | `MADO_SELFTEST: 460/460 assertions passed` |
| `quality/check-index.py` | 95/95, missing 0, dangling 0, duplicates 0 |
| `quality/check-tool-ledger.py` | 136/136 rows, uncovered 0, dangling 0, bad_pointer 0 |
| `quality/check-axis-scores.py` | checked 3, mismatched 0 |
| `sources-census.sh validate --root … mado` | exit 0, 49 lines |
| seven frozen instruments (`mado-verify.sh`, `landing-counters.sh`, `check-tool-ledger.py`, `check-axis-scores.py`, `c1-r75-*` ×2, `c2-r75-shapes.py`) | identical blob ids base → tip |

## Sources & frontier

**Census before → after.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin mado`.

| | exit | lines | receipt |
|---|---|---|---|
| round start | 0 | 47 | `census-start-r76.txt` |
| round end | 0 | 49 (47 + two W04 duplicate-URL warnings) | `census-end-r76.txt` |

**Registry:** 391 → 393 rows. Rows added: S455 (CPython v3.14.8 `expressions.rst` § Calls —
"argument is placed in the slot, filling it (even if the expression is None, it fills the slot)",
18 words, three byte-identical fetches, sha `e19de4fe…`) and S456 (CPython v3.14.8
`simple_stmts.rst` § The del statement — "Trying to delete an unbound name raises a NameError
exception", 10 words, sha `d4320642…`), both tier A, `status=mined`, `used-by
corpus/knowledge/interprocedural-del-r76.md`. Rows touched old → new (CORPUS rule 2):
S450 `replay-witness-credit-r74.md` → `replay-witness-credit-r74.md,
harness-witness-credit-r75.md, outcome-field-r76.md`; S453 and S454
`guard-carrier-copy-del-r75.md` → `guard-carrier-copy-del-r75.md,
interprocedural-del-r76.md`. S446 re-opened and kept rejected (flip condition unchanged).

**Frontier rows advanced.** The round-75 frontier bullet named "score the outcome field" and
"two next carrier shapes"; round 76 lands the first as a bounded certificate plus a negative
result (the echo term is not observable through `verdict=`) and the second as D3/D4, and adds the
readme frontier bullet `outcome-field-r76.md` / `interprocedural-del-r76.md`. Index 93 → 95 rows,
complete.

**Assimilation: none.** No `merge/mado/` package was adopted this round (the round's claims rest
on its own instruments and the two new sourced rows). considerthese mined: proposal 5 of
`considerthese/2026-10-28.md` ("separate relayed from re-measured in every number") lands as
QUALITY 131 and is applied throughout this report.

## Wave disclosures (per seat)

All thirteen seats settled; none died. A seat whose output was empty would be an evidence gap,
never backfilled (QUALITY 115); none was empty.

| Seat | Role | What it returned and what was done |
|---|---|---|
| `R76ScoutChain` | scout | Anchored anatomy of both C1 files (challenge draw, grammar, named rule, mutant anchors, the six overridden globals) and the C2 D3/D4 line spans; also ran the counters. No repair requested. |
| `R76ScoutPopulation` | scout | Re-derived 20/13/13/0 without the gate, confirmed 47 carried + 12 appended, and found three latent channels: non-first-parameter cancellation, a pre-taken copy launched after the callee deletion, and cross-scope bare-name collision. Fixed the first (D3 parameter binding) and third (scope-local call cancellations); the copy channel stays a declared limit. Also flagged `callee-del-param-rebound` as unreachable (M76-7 style, frozen not re-cut). |
| `R76ExecC1` | executor | Reproduced C1 at `cb713254` (16/16, 4/4), drove the real harness, both selftests (19/19, 23/23), and re-derived three labels from evidence lines only. Report kept at `w1/R76ExecC1/report.md` (its write-directory rule took precedence over the top-level report name). |
| `R76ExecC2` | executor | Reproduced C2 at `cb713254` (59/59 vs 55/59), hand-checked all twelve new labels (12/12), and executed four cases as runnable fixtures, observing the key absent at launch. |
| `R76ExecGate` | executor | Gate 460/460, index 93/93 at base and freeze, ledger 133 rows at base and 3 uncovered at freeze, axis 3/3, census exit 0, eight frozen instruments identical. Its ledger finding was the pre-integration gap; the rows landed at `81ca5d1b` and the final receipt is `136/136, uncovered=0`. |
| `R76ScribeEntries` | scribe | Drafted both entries and independently flagged the control-receipt/mutant-name mismatch (fixed as M76-5). |
| `R76ScribeLesson` | scribe | Drafted the lesson skeleton and three QUALITY proposals; the integrated lesson carries six mistakes and four criteria. |
| `R76RevC1` | reviewer | Two P2 findings: `--base-rev` resolved but unbound (repaired: held generation must exist at base, rc 2 receipt `repair-r76-c1-base-absent.txt`), and the frozen kill-rule wording "below fifteen" (repaired as F1). Also confirmed the echo-dropping rule still certifies (the declared negative result) and the last-row parse weakness (now a declared limit). |
| `R76RevC2` | reviewer | P2: D3 accepted a delete from any parameter while cancelling the first argument (repaired at `5dade9b3`, receipt `repair-r76-c2-d3.txt`). |
| `R76Critic` | critic | Six framing findings: F1 kill-rule wording (repaired), F2 the control is a port (disclosed in the receipt), F3 receipts without command/rc (provenance appended), F4 a stale knowledge-entry citation (repaired), F5 no pre-freeze held run on v3 (closed by the matched control), F6 the C2 control-note miscount (frozen file, corrected in the successor note and entry), F7 the revision split (stated per claim). |
| `R76Mutant` | mutation-tester | Five own mutations: three killed (`constant`, `forward`, `d4-twobind`), two survivors (`grammar16` narrowing, `d3-anyarg` broadening) carried as named gaps in the entry and lesson. |
| `R76Conn` | connector | Old → new source-cell crosswalk (adopted for S450/S453/S454), sibling sweep (no positive D3/D4 implementation; closest C1 method in kaidoku, compatible receipt limits in kake/chousa), and the control-receipt/mutant-set contradiction that became M76-5. |
| `R76Sentinel` | sentinel | Two P2s: C2 inherited the caller environment into git children (repaired to an allowlist) and the evidence prototypes write into unvalidated scratch roots (carried as a prototype limit). Confirmed the challenge redaction and the fixture git-root checks. |

## Trend verdicts

- **expansion: improved.** Two admitted entries on new ground (the contract outcome field and its
  observability bound; interprocedural and dynamic-key deletions), each `source:`-bound to a
  `mined` row (S450/S455; S453/S454/S455/S456), the index grows 93 → 95 with zero removals, and
  two tier-A rows were opened with three byte-identical fetches each.
- **quality: improved.** Six wave-found defects repaired at named commits without touching a
  frozen predicate, label, control set or target (F1/F3/F4/F6, D3 parameter binding, C1
  `--base-rev` binding, C2 child env and scope-local cancellations), each with a flip receipt or
  a carried-limit statement; four QUALITY criteria (128–131) land from the lessons; both claims
  are re-measured at their final instrument commits; the gate, index, ledger and axis checks are
  green at the landing tip.
- **discernment: improved.** The round's own wave produced the P2s that the L1's selftests missed
  (unbound `--base-rev`, D3 parameter identity, inherited child env, cross-scope cancellation,
  the stale kill-rule wording), each repaired or carried by name; the negative result replaces a
  claim the round could not honestly certify, and the survivors (`grammar16`, `d3-anyarg`) are
  written down rather than absorbed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry now 76 rows with three new gate rows; four historical `[~]` boxes unchanged (no outside-lane promotion evidence this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md — round-76 LOG entry records both claims end to end; no outside-lane verifier in this round.
- [~] Instructions executable by an agent without oral context — the frozen declaration, both counters' selftests and the wave seats' independent reproduction (R76ExecC1/R76ExecC2) are in-repo; dispatched seats do not count as outside-lane promotion evidence.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md append-only this round; no sibling surface written; outside-lane approval still absent.

## Stale-lane

Respawn-per-round driver; this lane has no other mission open.

## Tool installs

None this round (no tool installed, upgraded or removed; no pacman transaction).
