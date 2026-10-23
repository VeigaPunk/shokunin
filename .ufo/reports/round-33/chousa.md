# chousa — round 33 report

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, base `2b9cc73a`, final lane tip
`1b6312e5fb411f489d80db550a241db26401a1ce` (helper: `landed 1b6312e5…`, `ahead=0 behind=0`).
Attempt 1; `.ufo/watchdog.log` has only this round's launch line, so no earlier work was inherited.

## Work performed

Declared claim (one): **C1 operability** (lowest scored axis: operability is the only scored axis,
`SCORECARD.md:7`). Surface: the claim-record field reader in `verify-claims` (`json_str`/`json_has_key`
and their callers). The rule: claim fields come from the record's top-level JSON object only,
nested members change nothing, repeated top-level read fields make the record invalid, and string
content is never structure. This was carried as round-31 D-C and round-32 D4.

- Design v1 `3b528b9a` (08:23Z): counter `corpus/evidence/round33/c1-count.py` (144 records). L1
  base 60/144; python oracle 144/144 (`.ufo/waves/round-33/controls/L1-design/`).
- Wave 1 (32 seats): pre-data controls, candidate build, repairs and sources. CriticAxisFit33 found
  that the duplicate class covered only 3 of 7 keys and that any exit was accepted. Design v2
  `e3e24ec8` (08:35Z) has 156 records, six duplicated keys, and requires exit 1 with a DRIFT line.
  The L1 re-scored all 34 control gates under v2 before any candidate: best non-oracle 142/156,
  do-nothing 60/156 (`controls/L1-v2-rescore/summary.txt`, committed `96be7925`).
- Candidate `eb179ec3` (ExecC1Build's `claim_scan`, gate `52f07c74`) scored 156/156 on seeds 3351
  and 3352 (`measure/candidate/`).
- Wave 2 (34 seats) falsified the landed gate. P1 held on every landed-gate run (ReceiptCensus33:
  every committed v2 receipt on `52f07c74`, `94a7be5a`, `165acd5f` and `43a1af35` is 156/156, none
  lower). **§9 counterexample, found after data:** CriticControls33 inferred, and the L1 built,
  a gate that masks the counter's six fixed confuser strings, strips nested containers with a
  regex and counts repeats. It scores **156/156 on seeds 3391 and 3392**
  (`.ufo/waves/round-33/w2/L1ShortcutMask/`, committed `4c076a0f`). The pre-data control meant to
  catch this kind of label-keyed shortcut, CtlC1Shortcut, ended on a safety-filter hold.
- Post-falsify repairs (fail-closed clauses the counter never generates): bare non-JSON tokens,
  FF/VT whitespace, invalid escapes, an escaped NUL in read fields, marker_default rows with
  repeated keys, three-repeat id display, and quadratic cost on long members (64 KiB unread member
  4.7 s → 0.11 s). Commits `0cad05eb` and `1b6312e5`. The final gate `43a1af35` was built in a
  scratch copy and installed after wave 2 settled.
- Repairs D1–D5 from `corpus/lessons/round-32-verifier-spotcheck.md`:
  - **D1:** exempt-hop counter v3 `corpus/evidence/round32/c2-count-v3.py`. The round-32
    metadata-order control now scores 87–98/132 instead of 132/132. Controls were scored before
    the landed gate; the landed gate scores 132/132.
  - **D2:** `corpus/evidence/round33/d2-census.py` counts 21 receipts (not 18, not 20). The
    correction is appended to `SCORECARD.md`.
  - **D3:** the battery now prints a revision header (`w1/ExecNoHarmBase33/battery.sh`).
  - **D4:** fixed by C1.
  - **D5:** wave contexts forbid name-based signals, and the check
    `corpus/evidence/round33/no-name-signals.sh` exits 1 on the round-32 run (`RerunC1b.md:31`).
- Planner seat: the L1 held the canonical §3 planner seat (the validator rejects `planner`). The
  planning data walks rode scouts ScoutDocs33, ScoutJsonReaders33 and ScoutSourcesFrontier33.

## Landed changes

| Commit | Change | LOG |
|---|---|---|
| `3b528b9a`, `e3e24ec8` | design v1, v2 + L1 base/oracle receipts | LOG Round 33 |
| `96be7925` | wave-1 controls + L1 v2 re-score (before data) | LOG Round 33 |
| `eb179ec3` | C1 candidate gate `52f07c74` + selftest 242–248 | LOG Round 33 |
| `7f6aeb70` | candidate measurement, battery, D1 counter v3 | LOG Round 33 |
| `0fb300b5` | gate docs `94a7be5a`; S062, S063; knowledge `claim-record-fields-r33.md`; QUALITY 36–39; SKILL; README | LOG Round 33 |
| `4c076a0f` | shortcut counterexample evidence; S062 anchor fix | LOG Round 33 |
| `0cad05eb` | post-falsify repairs, gate `165acd5f`, selftest 249–250 | LOG Round 33 |
| `1b6312e5` | final gate `43a1af35`, selftest 251; SCORECARD, LOG, lesson, QUALITY 40–41 | LOG Round 33 |

## Before → after measurements

- **C1:** `python3 corpus/evidence/round33/c1-count-v2.py --seed N --receipt F` (lane root).
  - Before: `TOPLEVEL_FIELD_MATCH=60/156` on base `f4731885`
    (`controls/L1-design-v2/c1v2-base-s3311.json`).
  - After: `156/156` on final gate `43a1af35` at `1b6312e5`, seeds 3701 and 3702
    (`measure/final/c1v2-s370{1,2}.json`), and on every other committed landed-gate run.
  - **Verdict: P1 v2 met, but the counter does not verify clause 3.** The fixture-literal
    shortcut also scores 156/156, so this is not a clean verification under §9.
  - Non-counter evidence on the reader: differential fuzz against an independent python reference
    agrees on 1950/1950 records on the final gate (`measure/final/fz-9021{2,3,4}.json`); base
    agrees on 313/750 (FuzzDiff33).
- **No harm** on `43a1af35`, from `measure/final/battery.out`. Its header records `gate_sha256`;
  `lane_revision=0cad05eb` is the tip at run time, and the gate was committed in `1b6312e5`.
  - Selftest PASS 251; the first 241 case lines are identical to base.
  - claims-r2 17/17 CLEAN; chain-r3 17/22; broken 1/2 DRIFT; observable 3/3.
  - Round-31 counters v3 132/132; round-32 C2 v2 132/132; D1 v3 132/132 ×2.
- Operability score: 3 → 3 (the C1 observable sits beside it).

## Sources & frontier

- Rows 61 → 63 (`grep -c '^| S0' corpus/SOURCES.md`). Two tier-A rows added:
  - S062 RFC 8259. Its anchor was corrected in-round (316–333 → 316–335) after ReopenS062.
  - S063 Python `json` docs, `queued → mined`.
- Both rows were re-opened by the L1 (`measure/reopen-L1.txt`) and by ReopenS062/ReopenS063. No
  existing row was touched.
- Census:
  - Start: `chousa ok`, exit 0, two W04 warnings (`measure/census-start.txt`).
  - End: `chousa ok`, exit 0, the same two W04 warnings (`measure/census-end.txt`).
- Frontier: the round-31 nested-key carry moved to held ground (`corpus/README.md` Round 33).
- Mined mistakes (`corpus/lessons/round-33.md` `## Mistakes`):
  - fixed literal fixture content let a shortcut meet the counter (QUALITY 40);
  - the v1 counter covered 3 of 7 keys;
  - the L1 edited the gate in place while seats scored it (QUALITY 41; the `b808e9b5` 0/156
    receipt is a non-revision);
  - a tally had no counting command.
- Sourced claim: C1's knowledge entry cites S062 and S063.

## Trend verdicts

- **expansion: improved.** New knowledge entry `claim-record-fields-r33.md` (S062, S063) and a new
  capability row. The counter caveat on that row is stated.
- **quality: improved.**
  - D1: the exempt-hop capability is now verified by a counter whose metadata carries no truth.
  - D2: tally corrected with its counting command.
  - D3: battery header.
  - Five fail-open classes closed; selftest 241 → 251; QUALITY 36–41, each shown able to fail.
- **discernment: improved.** The pre-data critic broke v1 before data. The post-data shortcut was
  built, scored and reported rather than left as inference. S062 was over-read and corrected
  in-round. Real rejects are in the lesson `## Gate`. Limit: the label-keyed control was lost to a
  safety hold, so C1's own counter is weaker than claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry rows 77–88 (selftest 251, round-33 counters row), claims-mode paragraph; CalibrationSkill33 found 1 stale range (`SKILL.md:83`, metadata 137–154), not fixed this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 33; `measure/final/battery.out`
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh --selftest` → PASS (251 cases)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round

Round shape: two v1 waves. Wave 1 had 32 seats (12 mutation-tester, 7 executor, 4 scribe,
4 scout, 2 critic, 1 connector, 1 sentinel, 1 reviewer). Wave 2 had 34 seats (15 executor,
8 reviewer, 5 mutation-tester, 3 scout, 2 critic, 1 sentinel). Round total 66; no residual call.
Holds (`cyber_policy`, not retried): CtlC1Shortcut, MutC1Counter. Dead seats: none.

Misroot: SentinelParser33's report was written at the fleet root. It was moved byte-exact into the
lane and the fleet copy was deleted.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none. Open L0 questions: none new; the fetch-scope question is still open.
