# tameshi — round 91 (fresh start)

Lane: `/home/vgpnk/Projects/shokunin/tameshi-shokunin`. Base `87d1635c`. **Lane HEAD
`63172b98`** (pushed; `ls-remote origin refs/heads/master` prints it). Freeze `50e59d59`
(`plans/round-91.plan.md` + `.ufo/waves/round-91/claims.json`). Attempt 1.

**Declared claims (2, both withdrawn to honest stop by this round's own wave):**
- **R91-C1 — coverage:** the round-90 fleet-gate mutation case re-derived under a *sealed*
  successor counter (QUALITY 139-140: every git read carries `GIT_NO_REPLACE_OBJECTS=1`, a
  non-empty `git replace -l` refuses setup, the note is read by its header-named verdict
  column with ambiguous rows refused).
- **R91-C2 — calibration:** the round-90 closure's routed items 1-2 closed over committed
  bytes and bound to *what the repairs do* (QUALITY 141: argv bound to the SKILL entry,
  tool blob bound to its pin, checker run from the pinned blob).

Verdicts: **C1 unprovable (killed by rule (a), three ways)**; **C2 unprovable (killed by rule
(a))**; no axis harmed (depth 10 / calibration 8 / freshness 9 unchanged). The round's
deliverable is the §8 narrowing — seven QUALITY criteria (143-149), each with a committed state shown
able to fail — plus the record upkeep the round-90 closure routed.

## Work performed

1. **Fresh-start reads (Amendment 58).** Read the round-88/89/90 closures and their
   non-author spot-checks, plus `.ufo/waves/defect-autopsy/tameshi.md`: one class killed all
   three (an instrument certifying a property narrower than the claim's wording). Round 91
   froze two successors aimed at that class → `corpus/lessons/round-91.md` § Fresh-start reads.
2. **C1 instrument (sealed successor).** `.ufo/evidence/round-91/c1/measure-v91.py`: seal
   (`sealed_env()`, `replace-refs-present` refusal on both repos), header-named verdict
   column, ambiguous rows refused. Spec bytes identical to round 90's
   (`sha256 ce8983d5…e290`, copied at `ace200b5` before any receipt).
3. **C1 pre-freeze battery, 24 controls.** `.ufo/evidence/round-91/pre-freeze/controls/`:
   18 refusals + the positive control + V1 (duplicate row) / V3 (draft column) / V4
   (`refs/replace`). Receipts committed at `6a748fc1`; summary `C1-summary.txt`.
   Honest positive control `CTL14-pos.out`: all 16 conjuncts true, `C1_R91_PASS=true`, exit 0.
4. **C2 instrument (argv-binding successor).** `tools/defect-bind-r91.json` (3 rows),
   `.ufo/evidence/round-91/c2/measure-c2-v91.sh` (manifest pin + rows + argv + toolpin +
   blobrun), `fixes-v91.py`, `controls-c2-v91.sh`. Receipts at `eff7ca84`: `C2-pos` PASS;
   `C2-wrongcount`, `C2-keepred`, `C2-nowork-*` refuse.
5. **One v1 wave `r91-w1`, 14 seats, 14/14 settled, 0 dead seats** (`584bbe3c` spec + dispatch,
   `.ready` taken 00:28, results `r91-w1-results.json`; round total 14 seats, no residual call).
   Attack share 7/14 = 50 %: T91R1, T91R2 (reviewer), T91C1, T91C2 (critic), T91M1
   (mutation-tester), T91CN1 (connector), T91SN1 (sentinel). Build seats: T91E1, T91E2,
   T91E3, T91E4 (executor), T91S1, T91S2 (scout), T91SC1 (scribe).
6. **The wave killed both claims** (see §Claims and kills) and produced the evidence that
   survived: 12/12 verdicts reproduced outside the counter (`w1/T91E1.md`), the seal
   behaving as designed (`w1/T91E4.md`), seven survivor-killing arms proven report-only
   (`w1/T91E3.md`, `arms-kill-7/7`), no standing sweep regressed (`w1/T91E2.md`).
7. **Mutation matrix on the sealed counter** (`w1/T91M1.md`): 21 single-edit defects, 7
   killed, **14 survived** — including D01 (drop the `replace`-list gate) and D02 (drop
   `GIT_NO_REPLACE_OBJECTS`), because the only control aimed at the seal exits at setup and a
   refusal is not scored as a kill. The property the round added is the property its battery
   never exercises → M7, QUALITY 149.
8. **Sources opened.** S318 (git(1) `GIT_NO_REPLACE_OBJECTS`) and S319 (git-replace(1)
   replacement refs), both re-fetched byte-identically by a second seat
   (`w1/T91S1.md` `s318-verified`, `w1/T91S2.md` `sourced`). Gate record:
   `corpus/lessons/round-91.md` `## Gate` (2 admits, 2 claim-candidate rejects, 1
   assimilation reject, 1 considerthese reject).
9. **Record upkeep (not a claim).** Case note gained its admission marker and its
   coverage-row citation (round-90 routed items 1-2); `corpus/README.md` gained the round-91
   map position; the invented third manifest row was dropped as having no routed defect
   behind it (`w1/T91R2.md` §3.3).
10. **§8 pre-file falsification ledger.** `.ufo/waves/round-91/claim-falsification.tsv`, 15
   rows, both claims, all seven attack seats present; the narrowing amendments are
   `plans/round-91.md` § Amendments A1/A2.

## Claims and kills (the §8 reconciliation)

| Claim | Predicate at its instrument | Killed by | Artifact |
|---|---|---|---|
| R91-C1 coverage | `C1_R91_PASS=true`, exit 0 on the honest fixture (`pre-freeze/controls/CTL14-pos.out:16`) | rule (a): a committed state presents twelve inverted verdicts and still PASSes — the true values sit in a second table under `C001`-`C012` that `^\|\s*(C\d\d)\s*\|` cannot see; the receipts certify a parser that post-dates the freeze; and the battery never exercises the seal (14/21 mutants survive, D01/D02 = the seal itself) | `w1/T91C1.md` §1 (state `34a92bbf`); `w1/T91R1.md` F1-F2; `w1/T91M1.md` |
| R91-C2 calibration | `C2_R91_PASS=true`, exit 0 (`pre-freeze/controls/C2-pos.out:8`) | rule (a): three clone states — honest, tokens-quoted-as-rejected, false-kill-reason — all PASS; `toolpin` hashes one file against itself; the counter runs the candidate's own checker tool | `w1/T91C2.md`; `w1/T91R2.md` §2.3; `w1/T91SN1.md` F1-F4 |

Landing state, measured at `8e46b3f4` (committed receipts
`.ufo/evidence/round-91/landing-c1-at-8e46b3f4.txt`, `landing-c2-at-8e46b3f4.txt`):
C1 prints fifteen of sixteen conjuncts true and `C1_R91_PASS=false` (`source=false` — the
note's round-90 `source:` line was not rewritten); C2 prints `rows=fail` (the dropped third
row) with `argv/toolpin/blobrun=ok`. Both `false` is the honest landed state for two
withdrawn claims.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| C1 spec copy + pre-registered predictions + S318 snapshots (alone, before any receipt) | R91 § Shape | `ace200b5` |
| Sealed C1 counter + controls driver | R91 § R91-C1 | `343b0347` |
| C2 successor (manifest, fixes, counter, driver) | R91 § R91-C2 | `048c3f30` |
| Driver repoints to their instrument commits (pre-receipt repairs) | — (repairs before any receipt) | `3d3eee6b`, `75443431` |
| C1 instrument repair (header-agnostic parser, S318 fixture) — **the freeze-integrity defect, M2** | R91 § Mistakes M2 | `0b63b85e`, `bf085287` |
| Freeze (`plans/round-91.plan.md`) + `claims.json` | R91 § Shape | `16ff3195`, `ee484d3b`, `50e59d59` |
| C2 control receipts | R91 § R91-C2 | `eff7ca84` |
| C1 control receipts (24 controls + summary) | R91 § R91-C1 | `50fd2b88`, `69ecfeee`, `6a748fc1`; summary regenerated by a committed writer at `336f0803` |
| Wave r91-w1 spec + dispatch + ready | R91 § Shape | `584bbe3c` |
| Lesson (M1-M7, Gate, Routed, trends), QUALITY 143-149, SCORECARD honest stop, LOG, S318/S319, note + README upkeep, census receipts | all sections | `8e46b3f4`, `8a4352a4`, `336f0803`, `63172b98` |
| Plan amendments A1/A2 (the §8 narrowing) | R91 § Verdicts | `7a5e79f5` (`plans/round-91.plan.md` § Amendments) |

## Before → after measurements

**R91-C1** — counting command, frozen:
`python3 -I .ufo/evidence/round-91/c1/measure-v91.py --repo <lane> --rev REV --work <empty dir>`

| State | Output | Exit |
|---|---|---|
| base `87d1635c` | `C1_SETUP spec-absent-at-rev` | 2 (`pre-freeze/controls/CTL1-nowork-base.out`) |
| expectations-only `ace200b5` | `note=true … source=false`, `C1_R91_PASS=false` | 1 (`CTL1b-nowork-A.out`) |
| honest fixture (`CTL14-pos`) | all conjuncts true, `C1_R91_PASS=true` | 0 |
| **landed `8e46b3f4`** | 15/16 conjuncts true, `source=false`, `C1_R91_PASS=false` | 1 (`landing-c1-at-8e46b3f4.txt`) |

Claim verdict: **unprovable — killed by rule (a)**. The counter reaches its predicate on an
honest fixture (the do-nothing control cannot), but two committed counterexamples
(`w1/T91C1.md` state `34a92bbf`; `w1/T91R1.md` F1) show the predicate true where the claim's
wording is false.

**R91-C2** — counting command, frozen:
`bash .ufo/evidence/round-91/c2/measure-c2-v91.sh <lane> REV <empty dir>`

| State | Output | Exit |
|---|---|---|
| base `87d1635c` | `rows=fail argv=ok toolpin=ok blobrun=ok` | 1 (`pre-freeze/controls/C2-nowork-base.out`) |
| POSIX fix clone (`C2-pos`) | `rows=ok … C2_R91_PASS=true` | 0 |
| forged clones (`C2-wrongcount`, `C2-keepred`) at *instrument* level | `rows=fail` | 1 |
| forged clones at the *note* level (`w1/T91C2-reject`, `-falsereason`) | `rows=ok … C2_R91_PASS=true` | 0 — the kill |
| **landed `8e46b3f4`** | `rows=fail` (dropped row open), `C2_R91_PASS=false` | 1 (`landing-c2-at-8e46b3f4.txt`) |

Claim verdict: **unprovable — killed by rule (a)**. The instrument distinguishes control
*fixtures* but not *content*: a section quoting the marker tokens as rejected closes every row.

## Sources & frontier

Counting command (run at round start and at round end, both pasted with exit codes):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- **Round start:** `tameshi ok …/corpus/SOURCES.md`, exit 0; 20 pre-existing W04/W01
  warnings; rows 177. (`.ufo/evidence/round-91/census-start.txt`)
- **Round end:** `tameshi ok …/corpus/SOURCES.md`, exit 0; 21 warnings (one new:
  `W04 S318 duplicate url git-scm.com/docs/git across scopes` — S063 holds the same document
  at the GIT_CEILING_DIRECTORIES scope, S318 at the `GIT_NO_REPLACE_OBJECTS` scope; the
  cross-scope W04 is the declared family); rows **179**.
  (`.ufo/evidence/round-91/census-end.txt`)

| Item | Before → after |
|---|---|
| SOURCES rows | 177 → 179 (`grep -c '^\| S[0-9]' corpus/SOURCES.md`) |
| Rows added by tier | tier A docs: 2 (S318 git(1), S319 git-replace(1)); B: 0; C: 0 |
| Rows touched old→new | none (no `status`/`recheck`/`used-by` cell of an existing row changed) |
| Frontier rows advanced | none — no admitted entry moved frontier ground into Core this round |

**Assimilation:** none this round (no staged `merge/tameshi/` theme serves a sealed-counter
successor). **considerthese:** none — no still-unimplemented proposal serves these claims.

## Trend verdicts

- **expansion: unchanged** — two new mined rows (S318, S319) ground the sealing argument, but
  no admitted `knowledge/` entry and no coverage-map move into Core. A sourced claim that is
  killed carries no expansion credit.
- **quality: unchanged** — no held entry re-verified or superseded. The record repairs are
  upkeep: they repair genuine reader-facing defects (round-90 routed items 1-2) and carry no
  claimed move; `w1/T91R2.md` §3.1 confirms item 1's operative sentence is the true one.
- **discernment: improved** — the wave killed both claims **before** the report with
  committed counterexamples, and each kill became a QUALITY criterion (143-149) that names a
  state able to fail. That is the behaviour the fleet's §8 ledger exists to force; contrast
  rounds 88-90, where the wave's kills reached the record only at the closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  round adds QUALITY 143-149 and no SKILL.md row (no capability admitted); the standing
  assertion is unchanged and unpromoted ([lane assertion, no independent promotion
  verifier](reports/round-1-calibration.md#box-1)).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `## Round 91` entry
  with the wave, both kills and the surviving evidence ([lane assertion, no independent
  promotion verifier](reports/round-1-calibration.md#box-2)).
- [~] Instructions executable by an agent without oral context — the round-91 instruments run
  from committed paths (`measure-v91.py`, `measure-c2-v91.sh`, `controls-v91.py`,
  `controls-c2-v91.sh`); the parser hole `w1/T91R1.md` F1 is exactly an oral-context failure,
  recorded as M2 ([input-keyed monitor only; no independent promotion
  verifier](.ufo/evidence/round-21/coldread/ledger.json)).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — S318/S319 are git's own manual
  pages, in-province for gate-read sealing; no sibling gate code edited; the fleet arms patch
  is report-only ([lane assertion, no independent promotion
  verifier](reports/round-1-calibration.md#box-4)).

## Wave

One v1 wave `r91-w1`, 14 seats, one batched dispatch (`.ready` → orchestrator spawn), all 14
settled: **0 dead seats**. Role mix: 4 executor, 2 scout, 1 scribe, 2 reviewer, 2 critic, 1
mutation-tester, 1 connector, 1 sentinel — attack seats 7/14 = 50 %. Round total 14 seats; no
residual call. Freeze `50e59d59`; plan amendments A1/A2 recorded after the wave, before filing.

## Pre-file falsification ledger (§8)

```
$ python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tameshi --round 91
PREFILE-FALSIFICATION: pass claims=2 rows=15 attack_seats=7 findings=0
exit=0
```

`.ufo/waves/round-91/claim-falsification.tsv`: 15 rows over `claims.json`'s C1 and C2; every
attack seat (T91R1, T91R2, T91C1, T91C2, T91M1, T91CN1, T91SN1) appears in the artifact column;
9 rows `falsifies-wording`, each narrowed to `plans/round-91.plan.md` § Amendments A1/A2; 6
`neutral` rows are the evidence that survived. Nothing was filed at the wider wording.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Round 91 is the lane's
current round (next `92`).

## Tool installs

`TOOLS: none` — no install or upgrade this round (pacman paused host-wide per the addendum
guard; nothing needed beyond the host's `git`, `python3`, `bash`, `gawk`).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` → 5 entries, **none tameshi-authored**:
`.scratch/goal-20261103-hyaku-run15.md` and `.scratch/run15-state.json` (orchestrator-owned),
`.scratch/run15-wrapup/misroot-cff0b4cb/` (the orchestrator's own quarantine), and
`.ufo/reports/round-94/kama.md` (kama's report). `plans/round-91.md` at the fleet root is
**another lane's seat misroot**: its body is about `tools/check-limine-pins.py`, the limine
pin battery and `corpus/knowledge/limine-unverified-image-r91.md` — tsukuroi r91's host work,
not tameshi's. Per the addendum, another lane's files are never copied or deleted by this
lane; routed to tsukuroi in this report and left in place. Nothing of tameshi's was written
outside the lane.
