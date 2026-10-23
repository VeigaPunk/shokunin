# chousa — round 32 (attempt 2)

Base `7a7259f0` (gate SHA-256 `0bc318b3…1258`). Lane HEAD `aa472066` (pushed; final gate SHA-256
`f4731885ac0f83076210be364fd443a4378ac88c3b3ef94b5bf1c9e380f003f0`). Round shape: default two v1
waves — wave 1 = pre-data controls + builds (39 seats), wave 2 = falsify (33 seats); no residual
call; round total 72. Every run below names the gate it used (routed R6).

## Work performed

Declared claims (frozen in `corpus/evidence/round32/claims.md`; design v1 `4111607c` from attempt 1,
design v2 `3d586d3a` after the control wave and before any candidate receipt):

- **C1 operability** (lowest scored axis; surface: the `verify-all --json` manifest append) — the
  probe and the append are one `flock -x` critical section on the manifest's own open file.
- **C2 coverage** (surface: the exempt arm of `verify-chain`) — hops marked `unresolved`,
  `blocked-no-fetch` or `labelled-dead` are read with the resolved-hop rules; a resolvable one
  drifts with `CHAIN_EXEMPT_RESOLVABLE`.

Work items:

- Inherited state: attempt 1's landed commit `4111607c` (design v1, counters, L1 receipts) was
  re-verified — counters re-run on the base gate (C1 5/24, C2 84/120, matching v1's disclosed
  values); its uncommitted files (`gen-wa-spec.py`, `wa-spec.json`, `wa-dispatch.json`,
  `wa-run.err`, `wa/swarm-registry.json`) were deleted unread-as-evidence; its seats' tasks were
  not re-sent.
- Pre-data control wave (inside wave 1) broke both v1 counters: a probe-only lock met C1 v1 at
  24/24 (`.ufo/waves/round-32/w1/CtlC1PartialLockB/b-s3247102{1,2}.json`, gate `034f786b`); duplicate
  findings, missing DRIFT verdict, case-insensitive and whitespace-collapsing readers met C2 v1 at
  120/120 (`w1/MutC2CounterB/frozen-*`, `w1/CtlC2NoisyB`, `w1/CtlC2WeakReaderB`). Design v2
  `3d586d3a`: C1 counter delays every manifest write 300 ms under strace; C2 counter counts findings,
  checks the record verdict, refuses a fixture inside the gate's lane root, adds case-only and
  whitespace-only negatives (TOTAL 132). All controls re-scored under v2 and committed before the
  first candidate receipt (`f43dd5a3`, `a065845a`; Chronology32: first candidate receipt 18 s after
  the last control commit). Best v2 non-oracle controls: C1 12/24, C2 126/132.
- Candidate built by ExecC1Build / ExecC2Build / ExecR2Selftest31, integrated by the L1
  (`0f96bc1c`, gate `10f2fe12`); selftest 228 → 241, base case lines byte-identical
  (sha256 `a8873064…`).
- Falsify wave: C1 contract breaks outside the counter (symlink retarget, SentinelC1After;
  unreadable-under-lock glue, CriticC1Contract) repaired at `53cf649c` (gate `f4731885`; before/after
  `.ufo/waves/round-32/measure/post-falsify/c1-fix-probe.out`). **C2 §9 counterexample**
  (CriticAxis32): a control that never opens a cited source, ranking source files by mtime/inode,
  scores 132/132 on two seeds (`w2/CriticAxis32/control-metadata-s3232002{1,2}.json`), because the
  counter writes the resolvable sources first. Counter not amended; C2 reported not verified.
- Round-31 routed defects R1–R6 repaired (`corpus/evidence/round32/r31-repairs.md`): R1 named
  correction appended to `corpus/lessons/round-31.md`; R2 round-31 counters v3
  (`corpus/evidence/round31/c{1,2}-count-v3.py`, 132/132 on gate `0bc318b3`, 120/132 on the two
  mutants v2 let through) plus seven selftest cases (MutSelftestR2: all six mutants killed); R3
  battery on gate `0bc318b3` (`w1/ExecNoHarmBase32/`); R4 `SKILL.md` historical tally, README
  disposition revision, gate comment (now `220-228`); R5 `bfc0b02b` = the committed round-31 oracle
  script `.ufo/waves/round-31/controls/MutOracleC1/v2/oracle-c1.sh`; R6 this report. Carried, not
  fixed: nested `"line"`/`"sha256"` keys read as the record's own.
- Mistakes mined into `corpus/lessons/round-32.md` `## Mistakes` (six rows), QUALITY 33–35 with
  shown-able-to-fail checks (`corpus/evidence/round32/q33-check.py`: FAIL on the round-31 lesson at
  `4111607c`, PASS after the correction).
- L1 errors caught in-round and corrected: four L1 "control" receipts were base reruns (the seat had
  restored its gates) — `controls/L1-design-v2/CORRECTION.md` (ReceiptCensus32); S060/S061 first
  texts over-read their sources (ReopenS060/S061) — corrected; 11 stale self-description sentences
  (ScoutSelfDesc32) — fixed in `SKILL.md`, `corpus/README.md`, `SCORECARD.md`.
- Planner seat: held by the L1 (validator rejects `planner`); the planning data-walk rode
  CriticAxisFit32b, CriticSeparability32b and ReviewerCounters32b.

## Landed changes

| Commit | Content | LOG.md |
|---|---|---|
| `4111607c` (attempt 1) | design v1, v1 counters, L1 do-nothing and oracle receipts | Round 32 entry |
| `3d586d3a` | design v2, v2 counters, L1 v2 receipts, wave-1 spec/dispatch | Round 32 entry |
| `f43dd5a3`, `a065845a` | wave-1 control, oracle and build evidence; v2 control re-scores | Round 32 entry |
| `0f96bc1c` | candidate gate (C1, C2, R2 cases, R4c); R1/R4 corrections; S060–S061; knowledge entries; r31 counters v3; repair record | Round 32 entry |
| `5d8a1707` | candidate measurement; QUALITY 33–35; lesson draft | Round 32 entry |
| `53cf649c` | post-falsify C1 repairs (gate `f4731885`); source-row and self-description corrections; Q33 check; receipt relabel; C2 counterexample recorded | Round 32 entry |
| `aa472066` | final measurement and no-harm battery; falsify evidence; SCORECARD, LOG, lesson | Round 32 entry |

Each hash is the jj-lane helper's `landed` line after remote verification.

## Before → after measurements

| Claim | Counting command (lane root) | Before | After | Verdict |
|---|---|---|---|---|
| C1 | `python3 corpus/evidence/round32/c1-count-v2.py --seed N --receipt F` | `APPEND_SERIALIZED=0/24`, gate `0bc318b3` (`controls/L1-design-v2/c1-base-s3201.json`) | `24/24` on gate `f4731885` at `53cf649c`, seeds 32101, 32102 (`measure/final/c1-s3210{1,2}.json`); committed receipts on landed gates: `10f2fe12` ×18, `f4731885` ×3, none below 24 | **met** (P1 v2) |
| C2 | `python3 corpus/evidence/round32/c2-count-v2.py --seed N --receipt F` | `EXEMPT_AUDIT_MATCH=0/132`, gate `0bc318b3` (record checks fail; raw hop matches 96/132, R1–R3 0/36) | `132/132` on gate `f4731885`, seeds 32111, 32112 (`measure/final/c2-s3211{1,2}.json`); `10f2fe12` ×36, all 132 | **not verified** — a no-reader metadata-order control also prints 132/132 (§9) |

Separability (v2, SepAudit32): C2 counter on the C1-only gate `3144a46f` 0/132; C1 counter on the
C2-only gate `2a21aa43` 0/24. No-harm on gate `f4731885` (`measure/final/battery.out`): selftest
PASS 241; claims-r2 17/17 CLEAN; chain-r3 17/22 CLEAN; chain-r3-broken 1/2 DRIFT; round-1 observable
3/3; round-31 counters v2 120/120, v3 132/132. No corpus chain record changes verdict
(NoHarmCorpus32, gate `10f2fe12`). Disclosed behaviour changes: flock-less host and
unreadable-under-lock manifest refused with exit 2. Operability score 3 → 3 (delta 0), C1
observable beside it.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.
Round start (06:47Z): two W04 lines (S051, S053, pre-existing), `chousa ok`, exit 0. Round end
(08:01Z, lane `aa472066`): the same two W04 lines, `chousa ok`, exit 0.

- Rows 59 → 61 (`grep -c '^| S0' corpus/SOURCES.md`): added tier A ×2 — S060 Python `fcntl` docs
  (https://docs.python.org/3/library/fcntl.html), S061 RFC 9110 (https://www.rfc-editor.org/rfc/rfc9110.txt);
  both on registered hosts, opened by scribe seats and re-opened by the L1 (same body SHA-256, quotes
  found once). Both `mined`, used by `corpus/knowledge/manifest-append-lock-r32.md` and
  `exempt-hop-audit-r32.md`. Located quotes and access dates in `corpus/lessons/round-32.md` `## Gate`.
- Rows touched old→new: none of S001–S059. S060/S061 texts corrected in-round before filing
  (scope/teaches over-read; logged in the lesson).
- Frontier advanced: "concurrent appenders to one manifest" (open since round 24) → held;
  "exemption is record-declared and unverifiable" (round 3) → audited for three statuses, measure
  not verified (`corpus/README.md` Round32 disposition).
- Sourced claim: C1's knowledge entry cites S060 (opened this round).
- L0 fetch-scope question (`8d77e6c1`) still open; only registered hosts were opened.

## Trend verdicts

- **expansion: improved** — two knowledge entries on ground the coverage map did not hold, each
  citing a row opened this round (S060, S061); capability row "serialized manifest appends"
  backed by passing counter receipts.
- **quality: improved** — all six round-31 routed defects repaired with re-checked evidence
  (ReviewRepairs32: holds, two wording defects fixed); QUALITY 33–35 each with a check shown able to
  fail; round-31 counters v3 kill the two mutants v2 missed.
- **discernment: improved** — the pre-data control wave forced design v2 before data on both
  claims; the falsify wave's catches (C2 metadata shortcut, two source over-reads, four mislabeled
  receipts, two C1 contract breaks) are recorded, not hidden, and C2 is reported as not verified
  instead of re-scaled. Limit: the C2 counter flaw reached data.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates table round-32 counters row; `corpus/knowledge/manifest-append-lock-r32.md` (S060)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 32; `.ufo/waves/round-32/measure/final/battery.out`
- [~] Instructions executable by an agent without oral context — `python3 corpus/evidence/round32/c1-count-v2.py`; `bash tools/research-gate.sh --selftest` (PASS 241)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; ConnectorPost32 (no sibling consumer affected)

## Seats

Wave 1 (39; validated v1): 15 critic, 4 mutation-tester, 6 executor, 6 scribe, 4 scout, 1 connector,
1 reviewer, 1 sentinel, 1 revenger; 15 control seats messaged once for the v2 re-score, 14 answered
(not new seats). Wave 2 (33; validated v1): 10 reviewer, 7 critic, 6 mutation-tester, 3 executor, 4 scout,
2 sentinel, 1 connector. Round total 72. Dead seats: none. Holds (safety-filter refusal, item ended,
not retried): CtlC1ShortcutB (`code=cyber_policy`, no output), CriticPredicateGaps32b (same),
CtlC1JitterB's v2 re-score wake turn (same; its v1 receipts stand). Cancelled at settle deadline:
none. Disclosed collateral: RerunC1b's `pkill -x sleep` killed three sibling `sleep` processes.
Misroot sweep: `git status --porcelain` at the fleet root shows no untracked file naming this lane.
Several seats scored the lane working tree while it held the uncommitted intermediate gate
`d13a76e3` (C1 ×2, C2 ×2, all at target); those receipts are not counted as landed-gate evidence.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none. Open L0 questions: fetch-scope `8d77e6c1` (unchanged).
