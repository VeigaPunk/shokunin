# kengaku — round 88 (hyaku run 15, attempt 1)

Lane `kengaku-shokunin`, branch `master`. Base `801b903af6412cb424209a60b3a52e56c3532866` (round-87 spot-check tip).
Claims freeze `0220c2f9f356bf032bd58b4ed39e32f6e26fa440` (`plans/round-88-claims.md`, `plans/round88-cases.json`, before any instrument).
Instruments `1f267d4b6f60f1137ebf8b905d318bd2d9894e99`. Measured tip `7fcc680b86599eedd63e862a061848298428b3cc` (receipt `LANE_TIP da16ec39`, `WORKTREE clean`).
Lane HEAD at filing `79d403776f9ea82857ba4df8e3e1f2675c6b8f2f`; `git ls-remote origin refs/heads/master` returns the same hash. No plan, evidence or SOURCES byte changed between `7fcc680b` and HEAD (`git diff --stat 7fcc680b 79d40377 -- plans corpus/evidence corpus/SOURCES.md` empty).

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Round-87 items: V1 (zero-seat wave) discharged by this round's dispatch of 12 seats; V2 and V4 routed to the Q66 instrument (landed, attacked, findings routed to round 89); V3 by the dated pointer in `corpus/lessons/round-88.md` Gate; V5 by the explicit axis line in the SCORECARD round-88 table; V6 by this line.

Tool installs or upgrades: none.

## Work performed

**R88-C1 — coverage (held at its L0 cap 7): a sixth located offline replay of the captured `fix-git` grader.** Met as frozen at `7fcc680b`. The counter `plans/round88_c1_replay.py` (legs L1–L8) and probe `plans/round88_fixgit_probe.py` run the captured grader unmodified inside bubblewrap over eight frozen cases (sixteen legs), all observed equal to predicted. The attack wave shows the counter cannot establish that a receipt came from the grader rather than a forged probe (finding 1 below); the pass is a measurement of the committed receipt, not an authenticated one. Axis verdict: coverage moved by a count (one member of an existing class; Critic F2); score held at 7.
- Source: `corpus/evidence/round52/graders/fix-git/tests/test_outputs.py` (sha256 `a8a6f51e…43f3`) re-fetched 2026-11-05, HTTP 200, 1194 B, `cmp` silent (`corpus/lessons/round-88.md` Gate; ScribeR88 `source-check.md`).
- Receipt: `corpus/evidence/round88/fix-git-probe.txt` (`PREDICATE R88-PROBE pass`, `cases=8 legs=16 mismatches=0`).
- Ledger: `plans/grader-population-ledger.json` row `fix-git` executed, round 88, classes `crypto-credential`, `file-artifact`.

**R88-C2 — capability acquisition (no axis score): the Q66 executable half.** Met as frozen at `7fcc680b`, not sound. `plans/round88_claim_figures.py` extracts 56 before-figure records from the eight frozen claims files (rounds 80–87), re-runs each claim's counter at its own BASE, and reports the one known mispredict (`MISMATCH KNOWN R87-C1 kv:defects claimed==7 measured 3`). The attack wave found four ways the predicate passes with the failure it names (findings 2–5 below); these are routed to round 89, not repaired, because the frozen kill rules make any post-commit-A edit void the claim.
- Predicate evidence: `RECORDS claims=17 files=8 records=56 checked=56 matched=55 mismatches=1 prose=0`, `DEFECTS n=0`, `PREDICATE R88-C2 pass`.
- Selftest (`--selftest`): five `SELFTEST … pass` lines and `PREDICATE R88-C2-SELFTEST pass`; the frozen text says four (Reviewer B finding 1; frozen text reported, not repaired).

**Work items, with evidence pointers**
- Freeze: `plans/round-88-claims.md`, `plans/round88-cases.json` at `0220c2f9`.
- Instruments: `plans/round88_fixgit_probe.py`, `plans/round88_c1_replay.py`, `plans/round88_claim_figures.py` at `1f267d4b`.
- Frontier: S277 row in `corpus/SOURCES.md` and `corpus/lessons/round-88.md` at `da16ec39`.
- Controls (`.ufo/waves/round-88/L1/`): `base-runs.txt` (do-nothing at BASE for both; C2 instrument absent at BASE, `git cat-file -e` rc 128), `tip-runs.txt`, `controls.txt` (ledger-only → `DEFECT L1-receipt` rc 1; forged `LANE_TIP` orphan → `DEFECT L3-tip` rc 1), `separation.txt` (C2 unchanged by a C1 receipt removal; `PREDICATE R88-C2 pass`).
- Quarantine adjudication: `.ufo/waves/round-88/assimilation/quarantine-slice.txt` and `corpus/lessons/round-88.md` (S091 unverifiable, HTTP 403; S105 refused, quote absent from the cited capture).
- Wave 1: `.ufo/waves/round-88/w1-spec.json`, `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`; seat evidence under `.ufo/waves/round-88/w1/<seat>/` (committed at `79d40377`).
- Lesson: `corpus/lessons/round-88.md`. Q66 status corrected: `corpus/QUALITY.md` (Q66). SKILL class cells: `SKILL.md:74,77`. Index rows: `corpus/README.md:943,986`.

## Landed changes

| commit | what | tie |
|---|---|---|
| `0220c2f9` | freeze: claims R88-C1/C2, fix-git case table | LOG round 88 |
| `1f267d4b` | instruments: fix-git probe, C1 counter, Q66 counter | LOG round 88 |
| `da16ec39` | S277 row, round-88 lesson skeleton | LOG round 88 |
| `7fcc680b` | measured tip: receipt, ledger row executed, SKILL class cells, README index, Q66 executable half | LOG round 88 (measured tip) |
| `0f6ea1de` | L1 transcripts (base, tip, controls, separation) and LOG round-88 entry | LOG round 88 |
| `d9cb2b40` | wave-1 spec, dispatch, ready handoff, assimilation slice dir and scopes | LOG round 88 (wave) |
| `79d40377` | wave-1 evidence (12 seats), lesson wave dispositions and quarantine verdicts, Q66 status corrected, README row corrected, SCORECARD round-88 and LOG correction | LOG round 88 correction; SCORECARD round 88 |

Fleet report commit: see the `fleet-commit.sh` line in the closure output of this session.

## Before → after measurements

| claim | BASE `801b903a` | measured tip `7fcc680b` | counting command |
|---|---|---|---|
| R88-C1 | `TARGET executed_rows=31 member=fix-git located=0 executed=0 cases=0 legs=0 mismatches=0 defects=3`, `PREDICATE R88-C1 fail`, rc 1 | `TARGET executed_rows=32 member=fix-git located=1 executed=1 cases=8 legs=16 mismatches=0 defects=0`, `PREDICATE R88-C1 pass`, rc 0 | `python3 plans/round88_c1_replay.py --lane . --rev <REV> --work DIR` (`.ufo/waves/round-88/L1/base-runs.txt`, `tip-runs.txt`; ScoutR88 `counter-base.txt`, `counter-tip.txt`) |
| R88-C1 ledger | executed 31; `crypto-credential` 2 of 12; `file-artifact` 23 of 76 | executed 32; `crypto-credential` 3 of 12; `file-artifact` 24 of 76 | `python3 -c` over `plans/grader-population-ledger.json` (ExecCensusR88 `census.md`; ScoutR88 §2) |
| R88-C2 | instrument absent (`git cat-file -e 801b903a:plans/round88_claim_figures.py` rc 128) | `RECORDS claims=17 files=8 records=56 checked=56 matched=55 mismatches=1 prose=0`, `DEFECTS n=0`, `PREDICATE R88-C2 pass`, rc 0 | `python3 plans/round88_claim_figures.py --lane . --rev <REV> --work DIR` (`tip-runs.txt`) |
| R88-C2 selftest | — | five `SELFTEST … pass`, `PREDICATE R88-C2-SELFTEST pass`, rc 0 | `… --selftest` (`base-runs.txt`) |

Probe re-run (ExecBaseR88 `replay.txt`, independent scratch tree at `7fcc680b`): the observation block reproduces `corpus/evidence/round88/fix-git-probe.txt`; all pins verify.

## Sources & frontier

- `SOURCES: S277 admitted; rows 268 → 269.`
- Counting command: `sh scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` exit 0 after (269 rows); `validate --file` on a full `git archive 801b903a` tree exit 0 before (268 rows), and on the tip tree exit 0 after.
- Rows added by tier: A 1 (S277). Tier totals A 238 → 239, B 24, C 6. Status mined 243 → 244; rejected 17; queued 8. Rows touched old → new: none (S277 appended; the register check for W04 unchanged at 30).
- Frontier rows advanced: S277 (mined, used by `corpus/lessons/round-88.md`).
- Quarantine (shokuknow `absent-defect-register.md`, kengaku rows S091 and S105): S091 unverifiable (HTTP 403 at fetch, not fabrication); S105 refused (the quoted `指定されたページまたはファイルは存在しません` is absent from the cited capture, both Wayback forms). Nothing adopted.
- Considerthese: none taken this round. Proposal 1 of `considerthese/2026-10-26.md` (routed-findings burn-down) is still unimplemented and is the named round-89 candidate.
- Assimilation: none — `merge/kengaku/` remains blocked by L0 `kengaku | round-54`.

## Trend verdicts

- **expansion: improved.** One more executed member (`fix-git`, located offline replay, 31 → 32 executed), the `crypto-credential` class moved 2 → 3 of 12 (its previous executed member is round 80), and one admitted source row. Caveat: the coverage movement is a count, not a new surface (Critic F2).
- **quality: unchanged.** No existing figure or claim changed. The one documented mispredict (R87-C1 `defects=7` vs measured 3) is reported on the record and not repaired. The new Q66 instrument is weaker than its own predicate (findings 2–5), so it does not raise the lane's quality bar yet; QUALITY.md Q66 now says so.
- **discernment: improved.** The attack wave (one reviewer per frozen predicate, a critic, a mutation battery, a sentinel and an executor per control prediction) found holes that the frozen controls had missed: a forged probe passes C1, a doctored claimed value passes C2, a deleted before-figure passes C2, and the selftest is not in the predicate path. Caveat: the instruments themselves still discriminate less than their predicates say; the improvement is in what the lane now knows about its gates, and the fixes are routed.

## Wave 1

Shape: one v1 wave, 12 seats (band 8–16), attack share 6 of 12 (three reviewers, critic, mutation-tester, sentinel), one connector, one scout, one scribe, three executors. Dispatch `.ufo/waves/round-88/w1-dispatch.json` at 2026-11-05T02:37; all twelve seats delivered; no dead seat. The dispatcher recorded `SentinelR88-2` and `ConnectorR88-2` as spawn names; outputs sit under `SentinelR88/` and `ConnectorR88/`.

Verdicts (verbatim from each seat's output):

| seat | verdict | content |
|---|---|---|
| ScoutR88 | — | member recon; ledger counts confirmed |
| ScribeR88 | `SEAT ScribeR88 VERDICT FINDINGS findings=1` | source re-open and gate check; one cosmetic finding (fixed by the lesson rewrite) |
| ExecBaseR88 | — | BASE and tip counter reruns, probe re-run, pins; one first-pass quoting defect in its own harness, corrected in-file |
| ExecCtrlR88 | — | ledger-only and forged-LANE_TIP reproduced; two own-controls predicted wrong (B: doctored `defects=9` passes C2; C: deleted before-figure passes C2) |
| ExecCensusR88 | — | census rc 0 with `--root`; `--file` rc 1 on partial trees (E11 path artifact, documented) |
| ReviewerR88a | — | C1 counter: 2 MINOR (L3 accepts any ancestor; `stage()` edge case) |
| ReviewerR88b | — | C2 claims and engine: 5 findings (frozen "four" text wrong; predicate homes differ; extraction recall; over-capture) |
| ReviewerR88c | `SPOTCHECK admit=agree q66=agree` | non-author spot-check of the S277 admit and the Q66 claim |
| CriticR88 | `SEAT CriticR88 VERDICT FINDINGS findings=15` | six MAJOR (F1–F6), eight lower |
| MutTesterR88 | — | C1: 13 mutants, 9 killed, 4 survived (3 redundant with L6, 1 output-only). Q66: 10 mutants, 6 killed, 4 survived (2 output-only, 2 undetected) |
| SentinelR88 | `FINDINGS 8` (2 High, 4 Medium, 2 Low) | forged-probe path (High), C2 has no freeze anchor (High), constants inside the file under test (Medium) |
| ConnectorR88 | — | sibling overlap: replay of `fix-git` and the L6 re-run are fleet-first; receipt-ancestor leg has DUPLICATE relatives in kama and tameshi; re-derivation of frozen figures has no sibling equivalent |

Full findings with dispositions are in `corpus/lessons/round-88.md` ("Wave 1" and "Routed to round 89").

Findings that bear on what this round's green can mean:

1. **C1 accepts a forged probe** (Sentinel F1 High; Critic F1 MAJOR). L6 re-runs the probe from the measured tree and compares it with the receipt; a probe whose grader call is replaced by an echo passes. No frozen element pins the probe bytes.
2. **C2 passes a changed claimed value** (ExecCtrlR88 control B; Critic F4; MutTester O1). The KNOWN check compares `(claim, key)` only.
3. **C2 passes a deleted before-figure** (ExecCtrlR88 control C; Critic F5; Sentinel F3). Records are printed, not gated; `F6-norecords` fires only for a zero-record claim whose counter passes.
4. **C2 extraction net is convention-dependent** (MutTester O4; Reviewer B finding 3). R83-C2's before-state yields zero records; dropping the backward-direction selftest passes the predicate.
5. **C2 has no freeze anchor and an unimplemented kill rule** (Critic F5–F6; Sentinel F3); the selftest is named in the predicate but not invoked by `run_check` (MutTester O2).

None of these was repaired in-round. Repairing them is a post-commit-A edit, and the frozen kill rules name any such edit as making the claim unmet. Each is routed to round 89 (`corpus/lessons/round-88.md`, "Routed to round 89").

## Honest limits

- The tip receipt and the tip counters are real measurements on committed bytes; they are not authenticated as grader output (finding 1).
- R88-C2 "met as frozen" means its frozen predicate passes at the tip with the one documented KNOWN mispredict; it does not mean the Q66 check is sound (findings 2–5).
- The frozen R88-C2 text says four selftest lines and the instrument prints five (Reviewer B finding 1); reported, not repaired.
- The counter's `executed_rows` figure is printed but no leg reads it (MutTester O6).

## Mistakes

1. **Figure-not-measured** (routed R87-V2/V4): the round-87 claim text carried `defects=7` at BASE; the counter measures 3. The check added this round does not yet catch the class soundly (findings 2–5); the Q66 text is corrected.
2. **Overclaim in the first draft.** The lesson and Q66 initially described the Q66 check as complete. The attack wave showed otherwise; both are corrected in `79d40377`.
3. **Census before-measurement was late.** The first before-census was not run before the S277 append; it was run afterwards from a full base tree (exit 0, 268 rows, 30 W04) and recorded in the lesson.
4. **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows ` M .scratch/run15-state.json`. This is the driver's state file, not written by this seat; it is left untouched. No other fleet-root change.
5. **Instrument-side bugs found during development** (regex group order, span direction, digit keys, binary archive decode) were fixed before the instrument was committed.

## Push and verification

- Fleet repo: report committed with `fleet-commit.sh` (line in the closure output).
- Lane remote: `git ls-remote origin refs/heads/master` = `79d403776f9ea82857ba4df8e3e1f2675c6b8f2f` = lane HEAD.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:74,77` (class cells updated this round; not promoted).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-88 entry and correction; ScribeR88 and ReviewerR88c are non-author checks of the admit, not of the whole task.
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-88.md`, `plans/round-88-claims.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:151`.
