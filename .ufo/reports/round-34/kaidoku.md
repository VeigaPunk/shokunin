# kaidoku — round 34 (run-6 re-dispatch, attempt 1)

**Status: `rejected-honest-stop`.** One new claim, frozen before its data, met its six frozen clauses and then stopped: an unregistered structure-blind class reached the green target without decoding a record. No capability, no score, no credit. The previous attempt of round 34 (report `27322359`, inherited through `f432c8e3`) stays intact and is not rewritten; this report supersedes it as the round's record and cites it where it stands.

Lane tip at filing: `39f433b2a2973ced6285ea81a919afcab437c524` (this report cites no later lane commit). Base `ec3125ad3d130d92f888a4128dfaa2982f36fff7`; freeze `c79bbe7b0959132b9873ff3431cf5eb313b58b33`; stop `cd75b92e583735729546b0ea3b250f2df6d0652a`; docs `66b84027`; stop bindings `5a0435ff`.

## Work performed

Declared claims: **one** — R34-C2, a capability acquisition declared on axis **depth**, "a pre-freeze structure-blind shortcut-replay gate built to make QUALITY 67 executable". R34-C1 (the inherited version-needs depth claim) remains **stopped and untouched**: five frozen artifacts byte-identical from `54a87a51`, zero execution or scoring hits, 183/183 child execs python3 (`.ufo/waves/round-34/r34b/w1/RevR34C1Untouched.md`).

- **Freeze before data.** Instruments, configs, eight synthetic `MREC` fixtures, `expected.json` and 26 pins landed at `c79bbe7b`; freeze order confirmed on four evidence classes agreeing to the millisecond — instrument births ≤ 07:11:41Z, commit object 07:13:11.435Z, receipts 07:13:21.916Z–07:13:52.481Z, and the base-absence reproduced from a `git archive` of `ec3125ad` (`.ufo/waves/round-34/r34b/w1/RevFreezeOrder.md`).
- **Before receipt:** `GATE_COUNTER_UNEVALUABLE finding=gate_absent`, exit 2 at the base (`.ufo/waves/round-34/r34b/before/c2-at-base.txt`).
- **Production receipt:** `GATE_COUNTER_OK finding=shortcut_gate_discriminates selftest_failures=0 mutants_killed=3 red=REPLAY_GATE_REFUSED green=REPLAY_GATE_CLEAN green_positive_matched=8 clauses_failed=-`, exit 0 (`.ufo/waves/round-34/r34b/after/c2-at-instruments.{txt,json}`), reproduced field-for-field from a fresh clone by two seats (`w1/ExecRecountC2.md`, `w1/ExecSeatSelftests.md`).
- **Five pre-data controls, all miss:** do-nothing (`gate_absent`, exit 2), always-clean gate (4/6 clauses), junk clean stub (5/6), no-positive-check gate (4/6), vacuous-floor gate (5/6); failing clause named per control (`.ufo/waves/round-34/r34b/controls/`, audited in `w1/RevControls.md`, mutated in `w1/MutCounterClauses.md`: 5/5 clause mutants survive the control corpus, 5/5 are killed by isolation probes — a coverage gap, not a false pass).
- **Decisive counterexample, bound:** content-multiset memorisation `w1/CtlMultiset-files/nameset.py` (sha256 `2e8feaea92ee…`) scores `matched 8 / target 8`, exit 0 at four seeds with exact argv, cwd, UTC and fixture digests in `nameset-green-receipt.json`; a payload-signature memoriser authored after the stop (`payload_keyed.py`) scores 8/8 plain **and 8/8 with every name byte zeroed**, where the pinned structural reader scores 0/8 (`payload-keyed-receipt.json`). Independent seats reproduce with their own readers: `w2/ACounterexample1.md` (own table 8/8 at three seeds; a zero-knowledge variant reading the counter's inherited-cwd `expected.json` also 8/8), `w1/ExecRedReproduce.md`, `w1/CritCounterLimits.md`, `w1/CritClaimWidth.md` CE-1, `w1/ScribeKnowledgeEntry.md` F1, `w1/MutShortcutClasses.md` (five variants at 8/8: value/offset, record signature, digest replay, label replay, fixed-slice memo).
- **Why that stops the claim.** Registering any of those flips the same gate to `REFUSED` within two seeds, so the refusal mechanism works and the **registered set** was unfaithful to the class it names; §9's rule (a target a control that skips the claimed work can reach is not an improvement; r29-C1 precedent) applies. `.ufo/waves/round-34/r34b/claim-stop.json`; addendum binding the receipts, the corrected wording and a sixth defect at `claim-stop-addendum.json`.
- **Record defects (six), disclosed not repaired in frozen bytes:** F1 declarative pins in a container the lane's own freeze gate rejects (`instruments_missing`, exit 3) — repaired by the enforced container `instruments.json` (`freeze-integrity: CLEAN pins=26 freeze=b917ea64ebbe rev=66b84027…`), which is documentary only: nothing pins the container and it is worktree-blind (`w2/APinsEnforced.md`); F2 predicate identity false in three sentences, not two (`predicate-reconciliation.json`; `w2/AStaticBlindness.md` D2); F3 a class drop to the three-class floor still prints CLEAN; F4 a shortcut relabelled `structural` prints CLEAN even on the red config, and gate mutant M3 survives its own selftest (`w1/MutGateBranches.md` M3, `w1/RevengerGateFailModes.md` D1); F5 a gate that runs no reader satisfies all six clauses and `met_target` is never cross-checked with `matched` (`w1/CritCounterLimits.md` probes D/E); F6 the deterministic public-seed transform publishes each permuted copy's digest and names the copy `opaque-<sha256(copy)[:20]>`, so an identity replay reaches 8/8 (`w1/MutFixtures.md`, `w1/MutShortcutClasses.md`).
- **Repair evidence, not a claim:** `w1/CtlMultiset-files/mini-counter-fresh.py` (fresh generated content per run; seat-demonstrated 8/8 structural, 0/8 for nine classes) is itself defeated by an argv seed leak (`/proc/<ppid>/cmdline` replay, `w2/ACounterexample1.md`, 8/8 seeded, 0/8 unseeded) — so the repair needs its own control before any future claim.
- **Sibling overlap:** substantive and uncited before this round — kake's `lookup_control_check.py` (2026-10-22) is the earlier instrument in this family, with tsukuroi, mado, chousa, kama and mori adjacent; cited, not absorbed; the "generic gate" wording is flagged as tameshi-provenance and the class roster as kama's frontier (`w1/ScoutSiblings.md`).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only operator files (`.omp/mcp.json`, `.scratch/goal-20261025-hyaku-12h.md`, `.ufo/state/*.report-baseline`). No seat wrote into the fleet root; nothing to copy back or delete.
- **Considerthese:** `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/considerthese/` does not exist — no proposal was mined.
- **Assimilation:** `none`. The id-collision guard was still run and proven: registry 105 ids, staged 132, collisions 0; an indented scratch fixture collides (1 collision with the 0–3-space pattern, 0 with a column-zero pattern), so the guard is live (`.ufo/waves/round-34/r34b/assimilation/`). No append: this is a resumed round whose claim was frozen before 2026-10-24, so shokuknow material waits for round 35.

## Wave 2 — falsification of the stop (32 seats)

Every wave-2 seat attacked the stop, its evidence, the six record defects or the proposed repair. What survived, what changed, and what the round owed:

- **The stop survived every reproduction.** `w2/ACounterexample2.md` reproduced the payload class 8/8 under the pinned transform and 8/8 with every name byte erased (pinned structural reader 0/8 on the erased bytes); `w2/ACounterexample1.md` reproduced the multiset class with its own table and added a zero-knowledge variant that reads the counter's inherited-cwd `expected.json` (8/8, 0/8 when cwd is `/tmp`) — a channel the stop record does not list; `w2/AStopJustified.md`, `w2/AStopHarm.md` and `w2/ARecordDefects.md` all reproduce the frozen verdict and the counterexample.
- **The stop's basis is a supra-rule stop, and is now stated as such.** All six frozen clauses were true, so the frozen `kill_rule`'s own trigger did not fire; the stop rests on round-contract §9 (`templates/round-prompt.md` §9: "a target must be one a do-nothing control cannot reach") and the r29-C1 precedent (`w2/AStopHarm.md` R1). That distinction was implicit in the first filing; it is explicit here.
- **QUALITY 67's operative step was not executed, only its terminal clause.** The criterion asks for the replay *before* the freeze; the seven frozen classes were pinned at `c79bbe7b`, but the class that decided the round was authored 07:19Z and landed 07:22:55Z, ten minutes after the freeze, and no pre-freeze scoring receipt exists. Registering it on scratch bytes returns `REFUSED`, so the route would have worked (`w2/AQuality67Route.md`).
- **Class precision corrected.** The multiset class decodes no header field, no record entry and no `name_off` (`w2/AStaticBlindness.md` D1: it buffers the whole file, so "reads no header" was too strong; blindness is content-contingent and its failure direction is refusal). The payload class is name-blind and record-aware, not traversal-free: a count-only key reaches 6/8, so its scalar columns are load-bearing (`w2/ACounterexample2.md`).
- **The proposed repair is defeatable on both of its readings.** `w2/ARepairFresh.md`: a positional reader that never reads `names_off` scores 8/8 on 14/14 seeds because the fresh generator writes the pool in record order (and 0/8 on the frozen permuted counter — the "fresh" surface is strictly weaker); an argv seed leak (`/proc/<ppid>/cmdline`) replays the generator (8/8 on explicit seeds, 0/8 with `os.urandom`). `w2/ARepairLoadBearing.md`: fixed content, fixed payload and replayed fixtures each let a memoriser back in; fixed names alone do not. So QUALITY 69's fresh-content route is necessary but not sufficient, and is corrected accordingly.
- **The stop record was tightened under attack.** `w2/AStopCompleteness.md` (P1-1..P1-5) found no receipt for the decisive run, an unorderable `l1_rerun_utc`, a pin receipt that did not exist, and four of five classes with report-only provenance. `claim-stop-addendum.json` now binds two class sources with exact argv/UTC/seeds, the enforced 26-pin receipt, the F6 identity-leak defect and corrected wording; four classes remain report-only and are named as such. `w2/AMutStopRecord.md` adds the honest limit: the record is un-pinned, 0 of 5 mutants are caught by the lane's own instruments, and a dropped defect would be undetectable.
- **Pins and predicate, after repair.** `w2/APinsEnforced.md`: the enforced container verifies CLEAN 26/26 at two revisions, but the clean window starts at the container's own landing (`b917ea64`), the container is not self-verifying (a forged 27th pin still reads CLEAN), and it is worktree-blind. `w2/ARecordDefects.md`: F1, F3 and F4 still true; F5 resolved by `b917ea64`; the count-only repair for F3 is insufficient (count is not identity).
- **Source audit.** `w2/ASourceS106.md` re-fetched the tag, commit and `external.h` URLs live: all byte-identical to the capture, every anchor exact, three `\f` bytes in the file (so a `splitlines()` reader is +3), census `ok` on a HEAD fixture. Two corrections folded in: the row now names the tracked capture `.ufo/waves/round-34/prep/R34ElfReader-files/readelf.c-binutils-2_47`, and the line list now includes `:14121`. Stated limits: E11 is existence-only, and the census never reads quotes.
- **Docs corrections accepted against interest.** `w2/ADocsOverclaim.md` enumerated 34 overclaiming sentences in the unlanded wave-1 scribe drafts; none of those blocks landed (the committed docs were written after the stop). Its four residual flags on landed text were fixed: "makes QUALITY 67 executable" → "built to make … executable", "eight readers" → nine reader files, and the empty `corpus/knowledge/2026-10-25-r34-pre-freeze-shortcut-replay-gate.md` a seat left behind was deleted.

- **Closure-style read, recorded against interest.** `w2/ASealVerdict.md` returns `ok+conformance-defect` — the stop is substantively correct and reproducible, but three record defects remain: the counting command's gate path is production-legal and unpinned (a mock gate plus `--rev 0000…` yields `GATE_COUNTER_OK`, so the receipt proves its own shape, not that the pinned gate ran); the F3 repair as worded is count-only and a count-preserving swap defeats it (QUALITY 70 already asks for count+names+digests); and F1's `repair_landed` overstates a post-data documentary audit. All three are recorded in the addendum as Y1-Y3; none touches frozen bytes. Sibling precedent for the routing: chousa r33 stopped on a fixture-literal mask, took the criterion-before-build route and was admitted the next round (`w2/ASiblingStop.md`).
- **Containment, measured.** `w2/ASentinelNewArtifacts.md`: both counters make no network calls and spawn only `/usr/bin/python3` (9 execve, all python), `-I` blocks a sibling-import trap, child env is rebuilt, writes stay in a temp dir with zero leftovers. But a scored reader is unsandboxed: it inherits the caller's cwd, can write the lane, and its grandchild survives the counter's exit; and the fresh-seed repair is replayable through its own receipt (`--seed` accepted and printed; a digest-keyed memoriser scores 8/8 with the known seed, 0/8 with `os.urandom`). Stated as a limit of the instruments, not repaired in frozen bytes.

## Landed changes

| commit | what | record |
|---|---|---|
| `c79bbe7b` | R34-C2 freeze: gate, counter, red/green configs, eight fixtures, eight readers, `claims.json`, 26 pins | `LOG.md` entry; lesson `## Claim R34-C2` |
| `b917ea64` | before/production/control receipts, enforced pin container, predicate reconciliation, wave-1 spec/payload/seat-map | lesson M34-5, M34-6, M34-11 |
| `cd75b92e` | stop record + the decisive counterexample source | lesson `## Claim verdict`; SCORECARD section |
| `66b84027` | SCORECARD section, LOG entry, lesson M34-5..M34-12, QUALITY 68-74, SKILL instrument registry, S106 row, knowledge entry, README rows | this report's Sources & frontier |
| `5a0435ff` | stop addendum, nameset and payload receipts, enforced pin receipt, end census, QUALITY corrections | lesson M34-12, M34-13 wording fixes |
| `417a8211` | S105 and QUALITY 73 restored after two anchor-replacement mistakes, tracked S106 capture, the repair's own defeats, wave-2 reports | lesson M34-12, M34-13; QUALITY 74 |
| `b62b4767` | SCORECARD criteria count corrected and the final census receipt confirmed identical to the landed one | this report |
| `1675a8d8` | addendum extended under attack: `predicate_status` "satisfied as written (registered scope)", the producer's recorded dissent, limits X1-X5 and the corrected repair route; LOG blindness wording fixed; last wave reports | `w2/AStopJustified.md`, `w2/ACounterexample2.md` |
| `2eafca42` | addendum: post-filing seal findings Y1-Y3, the closure-style disposition, the chousa r33 precedent; late wave-2 reports | `w2/ASealVerdict.md`, `w2/ASiblingStop.md` |
| `39f433b2` | Y4/Y5 recorded (the forward-dated rerun field is superseded by the receipt; the capability-table wording is clarified) | `w2/AStopFields.md` |
| fleet report commit | this file | cites `39f433b2` |

Wave evidence: `.ufo/waves/round-34/r34b/` (specs, payloads, seat maps, prompts, w1, w2, receipts, controls, assimilation, census start/end).

## Before → after measurements

**R34-C2 (the only claim).** Counting command, frozen before data:

```
python3 -I -B tools/round-34/c2-shortcut-gate-counter.py --root <LANE> --rev <REV> --json-out <RECEIPT>
```

| | at base `ec3125ad` | at freeze `c79bbe7b` |
|---|---|---|
| verdict line | `GATE_COUNTER_UNEVALUABLE finding=gate_absent` | `GATE_COUNTER_OK finding=shortcut_gate_discriminates selftest_failures=0 mutants_killed=3 red=REPLAY_GATE_REFUSED green=REPLAY_GATE_CLEAN green_positive_matched=8 clauses_failed=-` |
| exit | 2 | 0 |
| six clauses | none evaluable | all true |

**Verdict: falsified measure / honest stop.** The six clauses are true; the claim is not admitted, because the same target is met by a control that skips the claimed work:

```
python3 -I -B tools/round-34/mini-fix/mini-counter.py --root . \
  --control-reader .ufo/waves/round-34/r34b/w1/CtlMultiset-files/nameset.py --seed <S>
→ matched 8 / target 8 / met_target true, exit 0  (seeds kaidoku-r34-mini-v1, alt-1, alt-2, alt-3)
```

Owned axis scores are **unchanged**: coverage 10, depth 10, calibration 10, delta 0. No capability row entered.

## Sources & frontier

Census command (run at round start and round end):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

| | rows | A / B / C | mined / rejected / malformed | exit |
|---|---|---|---|---|
| start (`census-start.txt`) | 105 | 99 / 5 / 1 | 101 / 4 / 0 | 0 (8 × W04 duplicate-url warnings) |
| end (`census-end.txt`) | 106 | 100 / 5 / 1 | 102 / 4 / 0 | 0 (9 × W04) |

Rows added: **S106** (tier A, mined) — binutils `readelf.c` at tag `binutils-2_47`, commit `6ce87bbc`, capture sha256 `7e81eedf19b2b93663bb3f598f74b54c107bd699f551667eb1b3d0e33eddeeff`; the `SHT_GNU_verneed` decode: `sh_info` count (`:14058`), `endbuf` bound (`:14056`, `:14067-14068`), field order (`:14072-14076`, `:14102-14106`), dynamic-string resolution (`:467-470`), ten warn-only failure paths including the located quote `warn (_("Missing Version Needs information\n"))` at `:14149`. Opened 2026-10-25 via sourceware `blob_plain` after `raw.githubusercontent.com` 404'd every binutils-gdb path; three fetches byte-identical; release tag tree equals commit tree. Rows touched old→new: none of the 105 existing rows changed status, recheck or used-by (S105 was overwritten by a bad anchor and restored verbatim — M34-12; the swap is visible in `66b84027` and repaired before this filing).

Frontier rows advanced: **none**. PROVINCE is unchanged; the gate's home is SKILL.md's registry only, because Core needs an end-to-end REA probe with an `evidence_id` and subject sha256 (`w1/ConnectorFrontier.md`). Adjacency: the family is held by kake, tsukuroi, mado, chousa, kama, mori, tameshi and kotoba; cited, not absorbed.

**Sourced-claim requirement: not met, and disclosed.** The round's one claim stopped, and S106 was opened *after* the freeze (the frozen claims file already names it — a forward reference, `w2/ACensusNow.md` F). So S106 is curation with no claim credit, and no claim rests on it. Prior-art candidates from the bounded search (Chakraborty, Kapoor & Narayanan, WEIZZ, Adebayo, Segura; Geirhos and tmp.0ut rejected) are recorded as **leads**, not rows: no admitted entry cites them.

## Trend verdicts

- **expansion: unchanged.** One knowledge entry documenting an instrument and its stop; no new domain surface, PROVINCE unchanged, no frontier bullet moved.
- **quality: improved.** Six instrument defects found and routed to QUALITY 68-74 rather than patched in frozen bytes; the enforced 26-pin container; the receipts that three seats needed; the S105 row restored; the C1 entry's `sh_link` wording corrected by an appended pointer without rewriting the entry. The capability itself was denied, so no quality credit is claimed for it.
- **discernment: improved.** The round stopped on its own counterexample instead of banking a registry-relative CLEAN, and the stop record was then tightened under attack (addendum binding two class sources, exact argv/UTC/seeds, the F6 identity leak, corrected wording). Residual discernment debt: the stop record still cites four met-target classes with report-only provenance (`w2/AStopCompleteness.md` P1-4).

## SHONEN

- [~] SKILL.md real decision tables, error patterns, checklists, cited sources — the round-34 instrument registry landed with the three-verdict table, the exit-code map and S106; verifier: `w1/ScribeSkillRegistry.md` (lane seat, not an outside verifier) plus `w2/ADocsOverclaim.md` corrections. Not `[x]`: no non-author outside verifier.
- [~] At least one end-to-end domain task logged — instrument only this round; the last end-to-end domain run is the historical libjq smoke. Pointer: `LOG.md` round-33 entry; not re-run.
- [~] Instructions executable by an agent without oral context — the gate, counters, configs and receipts are runnable and were reproduced by four independent seats (`w1/ExecRecountC2.md`, `w1/ExecSeatSelftests.md`, `w1/RevengerGateFailModes.md`, `w2/ARerunAll.md` if settled). No outside verifier.
- [~] No cross-domain bleed — PROVINCE unchanged and no closure claim; the semantic duplication with kake's lookup checker and the "generic gate" wording are flagged rather than absorbed (`w1/ScoutSiblings.md`, `w1/ConnectorFrontier.md`). Outside judgment pending.

## Round shape, seats and tooling

Two validated v1 waves, each dispatched as exactly one task call:

| wave | items | roles | returned | dead / cancelled | validation |
|---|---|---|---|---|---|
| w1 build + first falsifiers | 34 | executor 7, reviewer 6, scribe 5, mutation-tester 4, critic 4, scout 3, sentinel 2, revenger 2, connector 1 | 34 | 0 | `ufo-swarm-wave.mjs plan`, exit 0, band 32-64 |
| w2 falsify the stop | 32 | reviewer 10, executor 6, critic 5, scribe 5, mutation-tester 2, sentinel 1, connector 1, revenger 1 | 23 landed with a report on disk at filing (9 still running; no dead or refused seat) | 0 | `plan --emit-tasks`, exit 0, band 32-64 |

Round total: **67 seats** (34 + 32 + the L1 holding the canonical planner seat; the validator rejects a `planner` role, so the planner duty is the L1's own, per the 2026-10-19 orchestrator ruling). Every seat carried `/skill:godspeed` and the verbatim directive as the first bytes of the prompt it was told to read first; prompt files and seat maps are committed under `.ufo/waves/round-34/r34b/{w1,w2}/prompts/` and `w1-seat-map.json`/`w2-seat-map.json`. Routing was the host role map; no model was passed. Tool installs: **none** (host `python3` 3.14.8 sufficed).

`Stale-lane:` respawn-per-round driver; this is the lane's only open mission; round 35 is not started.

## Open questions routed

None blocked the round. One operator-facing note, not a question: the run-6 queue re-dispatched round 34 although its attempt-1 report had landed (`27322359`) and its claim had stopped with Main's approval; this attempt therefore ran a *second* claim in the same round number, which the frozen-claims rule permits only because R34-C1 was left untouched. A closure for round 34 now has two claim verdicts to read.
