# tameshi round 97 — the committed battery is re-derivable (calibration) and the guard edits are measured (operability)

Lane `tameshi` (verification-fixture craft), round 97, attempt 1. Base
`07e50d6d0142b21e8443b5417b8edc4d1dd76455`; records revision `2a57b42f9497d17340967624acd61bbbbaeb5e26`;
lane tip after this round
`29734beb095984038d66bb5dd4d149d81378de31` (branch `master`, `ahead=0 behind=0`, `ls-remote` agrees). Report filed by `fleet-commit.sh --as tameshi`.

**Declared claims (2).** R97-C1 targets **calibration** (the lane's lowest non-retired axis, 8):
the round-96 50-state battery verdict is a function of committed bytes — a committed reader
re-grades the 50 committed receipts against the committed driver's own expectations and prints
`BATTERY states=50 matched=50 mismatched=0 missing=0`, closing spot-check D-a (the report cited a
`C1-summary.txt` that was never committed). R97-C2 targets **operability**: a guard-inertia matrix
applies ten declared exact-string edits to the round-96 checker and prints
`GUARD_INERTIA rows=10 killed=8 limits=2 survived=0 unmet=0`, closing spot-check D-b (the
"are the guards inert?" probe had no committed measurement). Both claims were frozen before any
scored record: `plans/round-97.plan.md` and `.ufo/waves/round-97/claims.json` at `e72a0c8b`, then
amended pre-data by A1–A14 from the round's own wave (`plans/round-97.plan.md` §Amendments), each
row citing the artifact that falsified the sentence. No predicate, counter or target moved after
data; the records run postdates every amendment.

## Work performed

- **Protocol load.** `skill://shokunin`, `kimi-shokunin/skills/shokunin/SKILL.md`, `protocol/`
  PROTOCOL, MISSION.md, AXES.md, CORPUS.md, LEARNING.md, `skill://swarm`, `skill://godspeed`; lane
  SKILL.md, PROVINCE.md, SCORECARD.md, corpus/QUALITY.md, corpus/README.md `## Frontier`, the
  round-96 lesson and the round-96 non-author spot-check (D-a/D-b/D-c, inert risk note).
- **C1 instrument.** `.ufo/evidence/round-97/c1/battery-bind.py`: reads the 50 receipts as blobs at
  `--rev`, imports the committed driver blob as the oracle (`states()` + `EXPECT_EXTRA`), pins the
  driver with `--driver-sha`, refuses a non-64-hex or mismatched pin (`driver-sha-invalid` /
  `driver-sha-mismatch`, exit 2), reads nothing from the working tree, and prints the battery line.
  Selftest `BATTERY_SELFTEST: 7/7 pass`.
- **C2 instrument.** `.ufo/evidence/round-97/c2/guard-inertia.py` + `guard-inertia.json`: ten
  pre-registered rows (8 killed, 2 measured limits) over the round-96 checker, each one exact-string
  edit (uniqueness and no-op refused), pristine and mutant run against the same four-file fixture
  store; `--checker-sha` and `--manifest-sha` pins; refusals `edit-no-op`, `edit-ambiguous`,
  `state-unbuildable`, `limit-mechanism-missing`, `manifest-sha-mismatch`, `manifest-empty`
  (exit 2). Selftest `GUARD_INERTIA_SELFTEST: 7/7 pass`.
- **Pre-freeze controls (18/18)** — `.ufo/evidence/round-97/controls97.py` at
  `.ufo/evidence/round-97/pre-freeze/`: the two no-work controls (base grep rc 1; `cat-file -e`
  rc 128), both positives, both selftests, the four C1 forgeries (de-index committed, `counter_sha=`
  edit, `exit=` edit, `C1_R96_PASS` payload edit), the `--driver-sha` mismatch and the empty/short pin refusals (A4's own receipts), the C2 flipped
  expectation (`survived`, rc 1), the no-op anchor (rc 2), the substituted manifest under the pinned
  digest (rc 2) and the empty manifest (rc 2). `CONTROLS97 states=18 matched=18 mismatched=0`.
- **A1–A14 pre-data amendments.** From the round's own wave: A3 the `mutant=D<nn>` digest exemption
  (E3 E2e, R1 cases 06/28), A4 a non-64-hex `--driver-sha` (R1 F2), A5 the `__pass` scope (R1 F5),
  A6 `cat-file -e` rc 128 (R1 F6), A7 committed-vs-index deletion (R1 F4), A8 the plan sync (R1 F3),
  A9 the C2 Before clause (R2 F1, L1 §5/§9: `R96L1.md` exists, "partly refuted"), A10/A11 the C2
  command and the two setup refusals (R2 F3/F5, E2 F2), A12 the manifest digest pin (C1 §1/§2: a
  substituted manifest printed the exact line), A13 the non-guard-manifest limit (C1 §2), A14 the
  no-work control rc assertions (C1 §1/§3). Two of these are tool repairs, the rest narrow the
  sentences to what the instrument enforces.
- **Records run.** At `2a57b42f` both hypotheses were run three times each:
  `.ufo/evidence/round-97/landing/c1-positive-{1,2,3}.out` are byte-identical
  (`54c6f667…`), `.ufo/evidence/round-97/landing/c2-positive-{1,2,3}.out` are byte-identical
  (`254536aa…`); the earlier `.ufo/evidence/round-97/repeat/` set is byte-identical too.
- **Frontier step (§2b).** S159 (Wikipedia, mutation testing) re-opened this round with a located
  quote at line 762 ("Equivalent mutants detection is one of the biggest obstacles to practical
  usage of mutation testing.", 14 words, snapshot `00082805…`-class bytes under
  `.ufo/evidence/round-97/sources/s159.html`, sha256 `4b5a8374…`); S006 (shmutant README) re-opened
  with its non-unique-literal refusal quote (lines 490-491, snapshot `s006.html` sha256
  `55bb7196…`); both ground C2's `limit`/`edit-ambiguous` design and the lesson cites them.
  A draft row for the Stryker "Equivalent mutants" page was appended as S324 and **withdrawn before
  the freeze** — the URL already has S160, and the census flagged the duplicate (W04); the ground
  was re-opened from S159 instead. S009's UCL page returned a Cloudflare challenge page on two
  fetches (5 474 B), so it was not re-opened and its status is unchanged. Four mistakes are mined in the lesson's `## Mistakes` (M1 re-staged de-indexed receipt; M2
  evaluation-order truncation; M3 duplicate-URL row; M4 the three C1 body-edit forgeries built
  on top of each other, so the exit/payload paths were never reached — found by R97S1 and R97R1
  and repaired as A15).
- **Wave `w1`, one v1 wave, 12 seats** (`.ufo/waves/round-97/w1-spec.json`, dispatch
  `.ufo/waves/round-97/w1-dispatch.json`, `counts.total=12`): executor 3 (R97E1-E3), scribe 1
  (R97SC1), scout 1 (R97S1), reviewer 2 (R97R1/R97R2), critic 1 (R97C1), mutation-tester 1 (R97M1),
  sentinel 1 (R97SN1), connector 1 (R97CN1), revenger 1 (R97L1). Attack share 4/12 = 33 % by the
  addendum §6 named set (reviewer×2, critic, mutation-tester), 7/12 = 58 % including sentinel,
  connector and revenger. All twelve seats delivered a report and receipts; no seat died and none
  was replaced. R97E1 reproduced C1 (50/50, the five refusals, and a same-class body swap that the
  declared provenance limit covers); R97E2 reproduced C2 (all ten rows, both limits re-measured,
  exact-anchor counts); R97E3 probed the oracle boundary and found the `mutant=D<nn>` digest
  exemption (FW-C1-1 → A3); R97R1 falsified six C1 clauses (A3-A8) and confirmed the rest; R97R2
  held all nine C2 wording clauses and falsified the Before clause (A9); R97C1 found the unpinned
  manifest (A12/A13) and the shadowed control rc (A14); R97M1 mutated the two instruments (11/12 =
  91.7 % killed); R97SN1 ran the hostile-environment pass (pins and manifest refusals fire; the
  hand-written-receipt family stays the declared limit); R97CN1 found no duplicate implementation;
  R97L1 reproduced six guards independently and compared them with C2; R97S1 mapped every clause
  to its enforcing line and independently found the shadowed receipts (A15); R97SC1 verified the
  record fragments, found the same fixture defect and eight record mismatches (word counts, HTTP
  dates, anchor cells, QUALITY 175's rc), all corrected at `4460bba`. The L1 holds the planner seat (§3 mapping); no planner was
  dispatched.
- **Pre-file falsification ledger.** `.ufo/waves/round-97/claim-falsification.tsv` — 18 rows,
  both claims, all seven attack seats present (reviewer×2, critic, mutation-tester, sentinel,
  connector, revenger); the `falsifies-wording` rows point at A3-A9/A12/A13 and the two
  `falsifies-number` rows at A14/A15. Gate:
  `PREFILE-FALSIFICATION: pass claims=2 rows=18 attack_seats=7 findings=0`, exit 0.
- **Wave accounting.** The orchestrator settled the wave at 12:06 local and wrote
  `.ufo/waves/round-97/w1-results.json` (12 rows). Its `output` fields are null: the
  orchestrator kernel restarted mid-wave and the seat outputs were not retained; the seat
  reports and receipts in `.ufo/waves/round-97/w1/` are the record, and every claim in this
  report is read from them. No seat died and none was replaced.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → 11 entries, all
  `.scratch/` orchestrator state, another lane's report (round-68 kagi, round-90 tabi) or this
  report; no lane-authored file was written into the fleet root by this round (nothing copied,
  nothing deleted).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Instruments (C1 binder, C2 matrix + manifest), census before | Round 97 §Shape | `917d7109c9c4e43dd8fd69e59b147181e2e94d85` |
| Pre-freeze controls (14/14), frozen plan, lesson Gate + M1-M3, S159/S006 re-opens | Round 97 §Shape | `997ce0c4e4139b7c435d8a91ccefd7ce13a3dfa6` |
| Claims freeze C1/C2 (wording, shas, kill rules) | Round 97 §Shape | `e72a0c8bde44920554dc81c88c0dbb8dde491977` |
| A1 wording (missing vs mismatched) + QUALITY 175-176 + wave registry | Round 97 §R97-C1 | `136e98a84731d33779fe273061b79e388c6c9037` |
| A2 disclosure (base-rev reachability) | Round 97 §R97-C1 | `43acfe8125b3586e10fbf8da2b5c5bbe5fff885d` |
| Wave w1 spec (12 seats) + dispatch | Round 97 §Shape | `f5ace66a2a3705d833f388a9c44904e258946eea` |
| Repeated controls byte-identical 3/3 | Round 97 §R97-C1 | `605c9c58466dcc6d23e35a22f57469bfc553f89e` |
| A3-A11 pre-data amendments + re-pinned instruments + refreshed controls 14/14 | Round 97 §R97-C2 | `6f0805226b5c4a9e5826a1feae8a9093605dece0` |
| A12-A14 (C2 manifest pin, empty refusal, control rc assertions) | Round 97 §R97-C2 | `406119cdc83f1104b395bcf9334288c2d4f0ad0a` |
| Pre-freeze controls 16/16 (records base) | Round 97 §R97-C1/§R97-C2 | `35db02e9c6b2257e5243d39d2bbe0b346f2292e6` (superseded) |
| Records positives at `35db02e9` (3/3 byte-identical each) | Round 97 §R97-C1/§R97-C2 | `2170db7641d9ab01f141bdd59e74bdd259b8dc3f` (superseded) |
| A15/M4 control-fixture repair: each C1 forgery from pristine bytes; exit and payload paths reached; controls 16/16 at that commit, 18/18 after A4's receipts (new records base) | Round 97 §R97-C1 | `2a57b42f9497d17340967624acd61bbbbaeb5e26` |
| Records positives re-run at `2a57b42f` (3/3 byte-identical each) | Round 97 §R97-C1/§R97-C2 | `21eca3c13e18a1fc12cb22ec346bbf95a070f94f` |
| Wave seat reports and receipts (9 of 12 at that commit) | Round 97 §Shape | `ef427ff0059c0043a58607b18e1fab8f4f70ff05` |
| SC1 record fixes (Gate counts/dates, anchors, QUALITY 175 rc, A4 receipts); controls 18/18 | Round 97 §R97-C1 | `4460bbad8b3f74d1cbadf040bc629580ee566b36` |
| Remaining wave evidence (S1, SC1, SN1) and receipts | Round 97 §Shape | `1074ab523b75ee362c31ef8837f80afe3d45fcdb` |
| Falsification ledger (18 rows) + settled `w1-results.json` | Round 97 §Shape | `8152e9244a626cc9c6075f9559c8be385ce86032` |
| Census after + `w1.ready.dispatched` marker (final lane tip) | Round 97 §Shape | `29734beb095984038d66bb5dd4d149d81378de31` |


## Before → after measurements

### R97-C1 (calibration) — verified under the amended wording (A1-A8)

Counting command (at the records revision):

    python3 -I .ufo/evidence/round-97/c1/battery-bind.py --lane . --rev 2a57b42f9497d17340967624acd61bbbbaeb5e26 --driver-sha 88bcca8651f6a60568c0b74346796b5ce3407a9b2c8ac70ca7f229102d3c0ff5

Before: at base `07e50d6d` no committed tool prints a `BATTERY states=` line
(`git grep -c 'BATTERY states='` → no output, rc 1,
`.ufo/evidence/round-97/pre-freeze/c1-nowork-bind-absent.out`), the base does not carry the reader
(`git cat-file -e 07e50d6d:.ufo/evidence/round-97/c1/battery-bind.py` rc 128), and the
`C1-summary.txt` the round-96 report cites is absent at `8ed9c526`
(`c1-nowork-summary-absent.out`, rc 128). Disclosure (A2): the same reader run from the worktree
against the base data prints the predicate, so the after-state is a committed reader over old data.

After: `BATTERY states=50 matched=50 mismatched=0 missing=0`, rc 0
(`.ufo/evidence/round-97/landing/c1-positive-1.out`, byte-identical in runs 2 and 3). Refusals:
`c1-forge-worktree-only.out` (`matched=49 missing=1`, rc 1), `c1-forge-counter-sha.out`
(`mismatched=1`, rc 1), `c1-forge-exit.out` (`mismatched=1`, rc 1), `c1-forge-payload.out`
(`mismatched=1`, rc 1), `c1-forge-driver-sha.out` (`BATTERY_SETUP driver-sha-mismatch`, rc 2);
selftest `BATTERY_SELFTEST: 7/7 pass` (`c1-selftest.out`). Declared limits (unchanged): the oracle
is the committed driver; a hand-written receipt with the right payload is accepted; a
`mutant=D<nn>` receipt is exempt from the digest check by construction.

Measured commit: `2a57b42f9497d17340967624acd61bbbbaeb5e26`. The do-nothing control (base tree,
no tool) does not produce the line.

### R97-C2 (operability) — verified under the amended wording (A9-A14)

Counting command (at the records revision):

    python3 -I .ufo/evidence/round-97/c2/guard-inertia.py --lane . --rev 2a57b42f9497d17340967624acd61bbbbaeb5e26 --checker-sha 02a5482a573193c37bd9ebfa9303e84284561f50326043967834c9fdbf0d1c80 --manifest-sha 9de0b7e9649e0e267d05489a9d14b4075424e16ae80a8a6b27ae34870fe094da

Before: at base `07e50d6d` no committed tool prints a `GUARD_INERTIA` line
(`git grep -c 'GUARD_INERTIA'` → no output, rc 1, `c2-nowork-absent.out`); round 96's R96M1 matrix
covers the counter, not the checker's guards; the round-96 revenger probe left a late seat report
(`R96L1.md`, "partly refuted") but no committed runnable matrix (A9).

After: `GUARD_INERTIA rows=10 killed=8 limits=2 survived=0 unmet=0`, rc 0
(`.ufo/evidence/round-97/landing/c2-positive-1.out`, byte-identical in runs 2 and 3). The two
`limit` rows are measured identical pairs (`verify-quiet`: both exit 2 with the token;
`git-absolute`: both exit 0 under the pinned PATH). Refusals: `c2-forge-flipped-expect.out`
(`survived=1`, rc 1), `c2-forge-noop.out` (`GUARD_SETUP edit-no-op`, rc 2),
`c2-forge-manifest-subst.out` (`manifest-sha-mismatch`, rc 2), `c2-forge-manifest-empty.out`
(`manifest-empty`, rc 2); selftest `GUARD_INERTIA_SELFTEST: 7/7 pass` (`c2-selftest.out`).
Declared limits: a four-file fixture store, one edit per guard (no two-edit combinations), and the
manifest's row choice is a human declaration that the digest pin fixes but does not validate.

Measured commit: `2a57b42f9497d17340967624acd61bbbbaeb5e26`. The do-nothing control (base tree, no
tool) does not produce the line.

## Sources & frontier

`SOURCES.md` rows before → after, counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`:

- before: exit 0, rows 183 (A 165 · B 14 · C 4), status mined 149 · queued 23 · rejected 11
  (`.ufo/waves/round-97/census-before.txt`);
- after: exit 0, rows 183 (A 165 · B 14 · C 4), status mined 149 · queued 23 · rejected 11,
  unchanged (`.ufo/waves/round-97/census-after.txt`).

Rows added by tier: **none** — the only candidate (the Stryker "Equivalent mutants" page) was
withdrawn as a within-scope duplicate of S160 (census W04), and the ground was re-opened from
S159. Rows re-opened: S159 (located quote, line 762, snapshot sha256 `4b5a8374…`) and S006 (located
quote, lines 490-491, snapshot sha256 `55bb7196…`). Rows touched old → new: S159 `used-by` gains
`corpus/lessons/round-97.md`; S006 `used-by` gains the same. Rows refused / not opened: S009's UCL
page was a Cloudflare challenge page on two fetches (no quote located; status unchanged). Rows
unchanged: S160 (the duplicate case is recorded in the lesson, not appended). Frontier rows
advanced: **none** — F1-F11 in `corpus/README.md` are unchanged; this round's ground is the lane's
own instruments. Assimilation: **none** from `/home/vgpnk/Projects/shokuknow` this round (no
`merge/tameshi/` theme fits a reader/guard matrix, and `considerthese/` has no unimplemented
proposal bearing on it; the latest files were read).

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | unchanged | no new admitted knowledge entry on uncovered ground; rows 183 → 183; S159/S006 re-opened, one duplicate candidate withdrawn; frontier unchanged |
| quality | improved | QUALITY 175-176 appended, each with an `Able to fail:` receipt (the five C1 forgeries; the two measured `limit` rows and the two C2 refusals); two new instruments replace an uncommitted summary and an absent probe |
| discernment | improved | the round's own wave falsified twelve atomic assertions pre-data (R97R1 F1-F6, R97E3 FW-C1-1, R97C1 §1/§2, R97L1 §9, R97R2 F1); every one became an amendment A3-A14 with its artifact cited; no finding was smoothed, and the six the instrument refused (the digest exemption, the manifest substitution, the dead-seat provenance) are now declared limits or refusals |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  [lane assertion; round-97 evidence: `plans/round-97.plan.md`, `.ufo/evidence/round-97/*`, QUALITY 175-176; no independent promotion verifier](reports/round-1-calibration.md#box-1)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  [lane assertion; `## Round 97` LOG entry; no independent promotion verifier](reports/round-1-calibration.md#box-2)
- [~] Instructions executable by an agent without oral context
  [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  [lane assertion; the round touches the lane's own checker/reader only; connector sweep reported no duplicate implementation; no independent promotion verifier](reports/round-1-calibration.md#box-4)

**Stale-lane:** respawn-per-round driver; this is the lane's only open mission and no other mission
is open. **Tool installs:** none this round (no package was installed or upgraded; pacman untouched).
**Host note:** the wave was host-deferred (load1 157-158 against LOAD_MAX 144) by leaked
`kama-r94/SC02BudgetSweep/harness/stub.py` burners; the orchestrator reaped 16 of them and the wave
spawned at 11:22:21 local.
