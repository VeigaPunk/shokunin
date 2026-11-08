# souji round 85 — report

Lane: `souji-shokunin` (repo `/home/vgpnk/Projects/shokunin/souji-shokunin`), round 85, attempt 1 (`SoujiR85`).
Lane base `705fa1385c4ccec23811cfa57104046ec6587258` (r84 closed `admitted`). Round shape: one v1 wave of 12 seats
under `scripts/hyaku/ufo-wave-policy.json` (band 8-16).

## Work performed

Declared claims (2, causally separable — S85Connector §1: no shared file, population, counter, command or receipt):

1. **C1 — calibration 7 (the lane's lowest owned non-retired axis): the false-row population binds the pointer
   counter's ledger-class enum guard.** The r84 population bound five clauses and left the class-enum guard with no
   row; the r85 population adds NF-S (an unknown ledger class on item I85T) and kills the guard-dropping mutant
   (0/1 → 1/1), with the five r84 clauses still bound and both pristine arms green.
2. **C2 — operability 8: record-agreement K4 re-derives tracked bytes instead of trusting `git status`.** K4 answered
   "no uncommitted round work" from `git status --porcelain` alone, so an index stat-cache forgery read clean; it now
   re-hashes every status-clean stage-0 tracked regular file and symlink against the index object id through the
   receipt writer's own `_truth_refusal` (three frozen forgeries missed → three refused).

Work items, each with a pointer:

- Frozen instruments committed before any after-data (P `5bd5a0ce`): `census/round-85/c1-items.tsv` (3 items, sha256
  `d9a2ad8c…5114`), `c1-ledger.tsv`, `c1-pointer-counter.py` (`91b4ffde…7304`; r84 rules byte-for-byte, one added
  POPS pin), `c1-false-row-harness.py` (`d49aeb32…53a2`, fixture rev R8), `c1-clause-battery.py`, `c1-false-rows.tsv`
  (47 rows, `1468236c…8d42`), `c1-mutants.json` (six mutants, `bb788c0e…2e2d`), `c2-k4-counter.py` (7 rows, hermetic
  synthetic repository), the base-tool control `controls/c2-K-a-base-tool.py` (`ec5b809d…32c`) and both before
  receipts.
- Preregistration frozen ALONE in F `43c630eb` (`git show --name-only` = `census/round-85/preregistration.txt`).
- C1 after arm: `census/round-85/records/c1-after.txt` — `ARM pristine pop=r85 rows=47 mismatches=0 errors=0`,
  six `MUTANT-PAIR … killed=yes`, `SUMMARY mutants=6 sets=r85 pristine_r85=ok killed_r85=6`, EXIT 0. Before arm
  (same counter, battery, mutants; r84 44-row population): `killed_r84=5`, `m11-class-enum killed=no`, EXIT 0
  (`census/round-85/controls/c1-before-r84-population.txt`, re-stamped on the filed harness after S85Reviewer LOW-1).
  r83 regression: `ARM pristine pop=r83 rows=36 mismatches=0`, `killed_r83=0`, EXIT 0
  (`census/round-85/records/c1-regress-r83.txt`).
- C2 repair in `tools/souji-record-agreement.py`: `truth_refusal` (runs the receipt writer's `_truth_refusal` from the
  writer's source beside the tool's REAL path, in a `-I -B` subprocess; fails closed on a missing writer, a
  subprocess failure or the writer's own refusal) and one `K4 . stat-cache-concealed` row; K4's own status read is
  now pinned to the writer's config set (S85Sentinel F1/F2, A6). Filed tool `0ade0751…8fb7` (first landing
  `ed1ada73…d382`, superseded by the same round's repair).
- C2 after arm: `census/round-85/records/c2-after.txt` — `SUMMARY rows=7 mismatches=0 errors=0`, KF1/KF2/KF3
  `k4=1 named=yes`, honest rows unchanged, EXIT 0. Before: base blob `ec5b809d` `mismatches=3`, the three forgeries
  `k4=0 match=no`, EXIT 1 (`census/round-85/controls/c2-before-base-tool.txt`).
- C2 regression on the real lane: `python3 -B tools/souji-record-agreement.py --root . --rev 43c630eb` runs (exit 1
  from pre-existing K3/K4 findings only, no `stat-cache-concealed` row on committed bytes); the pre-existing K3
  mismatch (`corpus/README.md:1017 3 refused != receipt 0 refused`) is present at the base commit too and is named
  below as inherited.
- A1 finding (not a claim; the round's first reading was withdrawn by its own wave): the census-in-tree branch and
  the last-component basename check are REACHABLE and UNBOUND, not shadowed. Their single-edit mutants survive both
  pinned populations (`killed_r84=0 killed_r85=0`, both pristine arms green,
  `census/round-85/records/a1-c7-shadow.txt`), but that is evidence about the population: S85Scribe drove each
  branch through the counter's own `--forge` path and showed it refusing a row the populations do not carry, and one
  added row (NF-W, a census-rooted token landing in `census/round-84/w1/`) kills the census-in-tree mutant in a
  48-row probe population. The own-tree belt is the bound one (dropped → 7/7 rows red). r84's routed "ground it or
  delete it" therefore answers "ground it"; NF-W and the 48-row population are routed to r86 and nothing was
  deleted. The seat corrected itself once (its first basename mutant crashed with `IndentationError` — a crash, not
  a kill, Q133); the corrected run is `…/S85Scribe/receipts/f4-clause-bindings.txt`.
- Sources: S337 (PIT/pitest.org, admitted `docs` B `mined`); S315/S316/S317/S335 re-opened for the C2/C1 ground. The
  C1 claim is the round's sourced claim (S337: a suite is judged by the mutants it kills). Registry `259 → 260`;
  census `souji ok` EXIT 0 both ends (`census/round-85/records/sources-census-{before,after}.txt`).
- Docs landed: `corpus/knowledge/own-tree-pointer-binding.md` r85 section (shadowed vs unbound + the probe),
  `corpus/knowledge/filter-filemode-witness.md` r85 section (K4 and its rows), `corpus/QUALITY.md` Q156/Q157 under
  `## Round 85 criteria`, `corpus/README.md` r85 frontier block, `plans/round-85.md` A0-A4,
  `corpus/lessons/round-85.md`, `SCORECARD.md` r85 rows + two capability rows + planned r86.
- r84 spot-check defects answered: D1 — `.ufo/waves/round-85/claims.json` frozen (the gate's `claims-missing` setup
  refusal no longer fires); D2 — the battery prints `mismatches` and `errors` separately per mutant and no kill this
  round came from an error. The r84 routed r85 C1 list: the census-token row built and its premise falsified (A1);
  unknown-class row built (the claim); token-on-line row not built (it would make the pristine arm red by
  construction); NF-L3 carried. C2 list carried (A2/A3 explain why two of them cannot be rows yet).
- Wave: 12 seats — executor×3, scribe, scout×2, connector, reviewer, critic, mutation-tester×2, sentinel; attack
  5/12 = 42 %; one connector. **12/12 settled with substantive output, 0 dead** (`w1-results.json`). Seat verdicts:
  S85ExecC1 re-derived both C1 arms and every pin; S85ExecK4 broke the K4 repair in five directions and routed the
  gitlink concealment; S85ExecEvade attacked the population and found the census-in-tree clause deciding (the round's
  own sentence withdrawn) plus four unbound shapes; S85Scribe withdrew its own first F4 probe (a crash read as a
  kill) and supplied the reachability/reachability-reversal evidence; S85ScoutShapes censused the lane's real
  `census/round-*` shapes; S85ScoutSources opened S338-S340 (one rejected); S85Connector proved separability and
  mapped the prior art the repair should follow; S85Reviewer re-derived both claims and passed chronology; S85Critic
  ran eight neutral attacks and showed a weaker counter still scores 6/6; S85MutCounter found five unbound guards and
  one dead clause; S85MutK4 killed three repair clauses and exposed the C2 counter's honest-row crash; S85Sentinel
  found the two HIGH escapes the repair now closes. The falsification ledger (14 rows over 2 claims and all six
  attack seats) is `.ufo/waves/round-85/claim-falsification.tsv`; seat reports and receipts are committed under
  `.ufo/waves/round-85/w1/` (`aa2b9ccf`).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| instruments, populations, mutants, controls, before receipts | r85 C1/C2 bullets | `5bd5a0ce` |
| preregistration (F, alone) | r85 "Frozen claims" line | `43c630eb` |
| wave-1 spec, dispatch (12 seats), validator output | r85 wave bullet | `1ed32fe4` |
| C2 repair, after receipts, shadow probe, sources, knowledge, QUALITY, SCORECARD, LOG | r85 C2/Sources/Docs bullets | `5d3dd78d` |
| A1 withdrawn (reachable/unbound), basename correction, C2 counter fix filed | r85 correction bullet | `13b34b28`, `1d4b515b` |
| C2 repair closing the Sentinel's two HIGH escapes (realpath + `-I`, pinned status config) | r85 C2 bullet | `ec7c5732` |
| wave evidence: claims.json, results, 12 seat reports, ledger (14 rows) | r85 wave bullet | `aa2b9ccf` |
| re-stamped C1 before receipt + r83 regression (S85Reviewer LOW-1) | r85 C1 bullet | `1ff0eb58` |
| wave evidence: claims.json, ledger, 12 seat reports and receipts | r85 wave bullet | (this round's wave commit) |

## Before → after measurements

**C1 (calibration).** Counting command (both ends; re-derived by S85ExecC1 and S85Reviewer):

```
python3 -B census/round-85/c1-clause-battery.py --counter census/round-85/c1-pointer-counter.py \
  --work <empty dir outside /tmp> --only r85 --expect-killed 6        # after
  … --only r84 --expect-killed 5                                      # before
```

| end | observed | receipt | measured commit |
|---|---|---|---|
| before | pristine `rows=44 mismatches=0`, `m11-class-enum killed=no`, `killed_r84=5`, EXIT 0 | `census/round-85/controls/c1-before-r84-population.txt` | `1ff0eb58` (re-stamped on the filed harness) |
| after | pristine `rows=47 mismatches=0 errors=0`, six `killed=yes`, `killed_r85=6`, EXIT 0 | `census/round-85/records/c1-after.txt` | `5d3dd78d` |

Shadow probe (A1, a finding not a claim): `--mutants census/round-85/probes/c7-shadow.json --only r84,r85
--expect-killed 0` → `killed_r84=0 killed_r85=0`, both pristine arms green
(`census/round-85/records/a1-c7-shadow.txt`) — read together with S85Scribe's reachability probe, which shows the
clause refusing a row the populations lack: unbound, not dead.

**C2 (operability).** Counting command:

```
python3 -B census/round-85/c2-k4-counter.py --tool tools/souji-record-agreement.py --work <empty dir>
```

| end | observed | receipt | measured commit |
|---|---|---|---|
| before | base blob `ec5b809d…`: `rows=7 mismatches=3 errors=0`, KF1/KF2/KF3 `k4=0 match=no`, EXIT 1 | `census/round-85/controls/c2-before-base-tool.txt` | `5d3dd78d` |
| after | filed tool `0ade0751…`: `rows=7 mismatches=0 errors=0`, three forged rows `k4=1 named=yes`, EXIT 0 | `census/round-85/records/c2-after.txt` | `ec7c5732` |

No owned axis score changed (calibration 7, coverage 8, operability 8 — the lane has no reproducible 0–10 mapping);
both rows carry the verdict, the counting command and the measured commit instead. Waves' qualifications and the
narrowed sentences are in `plans/round-85.md` A1-A4.

## Sources & frontier

`SOURCES.md` rows before → after: `259 → 260`
(`grep -cE '^\| *S[0-9]{3,}' corpus/SOURCES.md`; before/after census `souji ok`, EXIT 0,
`census/round-85/records/sources-census-before.txt`, `…-after.txt`). Rows added by tier: one `docs` tier B
(S337). Rows touched old→new: none — S315, S316, S317 and S335 were re-opened this round for the C2/C1 ground and
their `status`/`recheck`/`used-by` cells are unchanged (recorded in the lesson's `## Gate`). Frontier rows advanced:
the r84 frontier block closed on the population instrument (the class-enum guard bound; the census-in-tree branch
measured shadowed) and the "clean `git status`" frontier moved one tool further (record-agreement K4). One candidate
was screened and none was rejected this round (no second external candidate was opened; the round re-opened four
existing rows instead). `Assimilation: none` (no shokuknow theme taken; `considerthese/` does not exist in this
lane).

## Trend verdicts

- **expansion: unchanged** — one new registry row (S337) and two knowledge sections on ground the coverage map
  already holds; `PROVINCE.md` unchanged and no `## Frontier` row promoted to Core. The round's gain is instrument
  power and one tool path, not breadth.
- **quality: improved** — the population that certifies the pointer counter now kills the class-enum mutant it left
  green (`killed_r84=5 → killed_r85=6`, both pristine arms green), and the lane's audit tool no longer certifies a
  tree it has not measured (three stat-cache forgeries missed → refused, honest rows unchanged). Two clauses of the
  C2 repair are unrowed and one class (gitlink/flag sweep) escapes — stated as limits (A2/A3), not claimed.
- **discernment: improved** — the wave falsified the round's own framing before filing, and the round withdrew
  rather than defended it: the census-in-tree clause r84 called "unbound" was first re-read as shadowed and the wave
  showed it is reachable and unbound (A1, S85Scribe F1), the basename clause was first read as bound on a mutant that
  crashed rather than killed and the wave reversed that too (F4 second run), the C1 target was retargeted before F
  (A0.3), the C2 counter was caught dying on an over-refusal (A0.4/M2 from S85MutK4's mutant), five more counter
  guards were measured unbound (A4, S85MutCounter), a gitlink concealment escapes K4 (A2, S85ExecK4) and two
  receipts named instrument bytes a reader could not obtain (A5, F2 — fixed and re-filed). Q156/Q157 were added so
  the next round tests reachability and status-trust before naming a clause.

## SHONEN

- [~] Box 1 — decision tables, error patterns and checklists exist with cited sources: `SKILL.md` classify/removal
  tables and error-pattern list, `corpus/QUALITY.md` Q156/Q157, citations S337 and `census/round-85/records/*`.
  Verifier pending (operator/non-author); pointer resolvable.
- [~] Box 2 — an end-to-end domain task executed and logged: the census-in-token refusal measured, the class-enum
  guard bound and the K4 repair landed with before/after receipts; `LOG.md` r85 entry, `SCORECARD.md` r85 rows.
- [~] Box 3 — instructions executable without oral context: `preregistration.txt`, `plans/round-85.md`,
  `corpus/lessons/round-85.md` and the counters are runnable as written; re-derived by S85ExecC1 and S85Reviewer.
- [~] Box 4 — no cross-domain bleed, `PROVINCE.md` accurate: `git diff 705fa138 -- PROVINCE.md` empty; the round
  stayed inside hygiene-instrument ground and the flag-sweep gap is routed inside the lane (A2).

Stale-lane: respawn-per-round driver; no other mission of this lane is open (the round's only open item is the
wave's own settle, and the report lands after it).

## Conformance and sweep lines

- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): no souji/round-85 file at the fleet
  root. Two untracked artifacts are other owners': `.ufo/reports/round-100/mado.md` (mado's lane) and
  `corpus/lessons/round-64-verifier-spotcheck.md` (a kagi round-64 spot-check written at the fleet root) — named,
  not touched. `.scratch/*` is orchestrator state, never a misroot.
- **Pre-file gate:** `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 85` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=6 findings=0`, **exit 0**.
- **Inherited state:** the pre-existing K3 disagreement (`corpus/README.md:1017 3 refused != receipt 0 refused`) is
  present at the base commit and is routed to r86 as a record-agreement row.
- **Tool installs: none** — no pacman (paused host-wide), no uv/npx/binary fetch, no sysctl, sudo or kernel change.
- **Scratch:** the L1's `/fast/scratch/hyaku/souji-r85/l1` tree was removed after the last measurement; seat trees
  are the seats' own to remove.
