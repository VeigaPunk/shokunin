# kasegi — round 75 (attempt 2) report

Lane: `kasegi-shokunin`, branch `master`. Lane tip at report time: `373bf4e7f9f9a6b59008e8f39a5a7aecd17c4b84` (`git ls-remote origin refs/heads/master`, same hash). Landing commits: `7d692165445ca1c252e7771c6cb2f4970bc9a17a` (C1, C2, wave evidence, lesson, scorecard, log) and `373bf4e7f9f9a6b59008e8f39a5a7aecd17c4b84` (misroot recovery, lesson M75-5).

## Work performed

**Declared claims (2, both frozen at `748dfb6`, base `f9cc05b5`).**
- **C1 — depth:verifiability** (lowest non-retired axis, score 4; nominal per QUALITY R58, the scored `resolve.py` census is not read by this gate). Counter amendment of `corpus/instruments/recheck-cwd-census.py`: a `restoration_only` bucket for files whose only recheck-ish header is `restoration-recheck:`, a RESULT gate that requires it zero, and selftest case 6.
- **C2 — coverage** (score 8, held; the denominator is operator-owned). Frontier admission F53 on S110, the NDSS Symposium 2023 paper "FUZZILLI: Fuzzing for JavaScript JIT Compiler Vulnerabilities".

Work items, each with its evidence pointer:
- Attempt-1 inheritance: the attempt-1 L1 died at 06:53 -03 (`.ufo/watchdog.log`, `lane-dead-no-report kasegi round=75`) after freezing the claims (commit `748dfb6`), committing the controls (`c880047`) and dispatching wave `w1` (`.ufo/waves/round-75/w1.ready.dispatched`, 06:49:44). Attempt 2 reused those outputs only after re-measuring them on the landed bytes. The attempt-1 scratch-derived amendment in `SentinelCounter` was discarded (not landed); the executor's `ExecC1Amend.patch` was landed.
- Wave `w1` settled (`.ufo/waves/round-75/w1-results.json`, 12 seats, dead 0; Main's WAVE-DONE rerouted to this attempt, message `15c21a58f63ca308`). Seat reports in `.ufo/waves/round-75/w1/`.
- C1 landing: `patch -p1` of `.ufo/waves/round-75/w1/ExecC1Amend.patch` into `corpus/instruments/recheck-cwd-census.py` (sha256 `e666ae11fd9d50ecea107b8835090eed0dc798e8e8a233324b9fbd59ab52a21a`, the value `MutAuditC1` measured on its battery). Registry row `SKILL.md:982`; instrument row `corpus/instruments/README.md:354`.
- C1 measurements on the landed bytes: `.ufo/waves/round-75/controls/c1-after-r75.txt`.
- C2 landing: `corpus/source-snapshots/round-75/S110.txt` (sha256 `0780beaefb5c0d973c76d4376a0c151345910890fa9a913b68461d71747e51ef`, 1869 lines, fetched 2026-11-05T09:51:07Z, HTTP 200), `corpus/source-snapshots/round-75/manifest.json` (24 quotes), `corpus/knowledge/fuzzilli-ndss2023-jit-fuzzing-paper.md` (25 double-quoted strings of at least 12 characters, all located: 24 in the S110 manifest, 1 in the S109 round-74 manifest), registry row `corpus/SOURCES.md:122`, F53 admission `corpus/README.md` `## Round-75 admission` block and `PROVINCE.md:223`, `corpus/instruments/knowledge-expected.txt:40`.
- C2 is sourced: S110 was opened this round (fetched 2026-11-05T09:51:07Z); the entry's header names `source: S110`.
- Frozen-claim verdict reviews: `ReviewC1`, `ReviewC2`, `CriticClaims`, `MutAuditC1`, `SentinelCounter` (attack seats, `.ufo/waves/round-75/w1/*.md`). Their findings are routed in the lesson (`corpus/lessons/round-75.md` § Mistakes and § Routed defects); no frozen predicate was reworded after scoring.
- Assimilation check: the id-collision guard, `.ufo/waves/round-75/assimilation/{reg-ids,staged-ids,collisions}` (reg 109, staged 94, collisions 79). Nothing adopted; L0 question filed (`.ufo/l0-questions.md`, line 328).
- Non-claim work: `ExecReplay` re-derived 20 committed base values from base receipts, all agree (`.ufo/waves/round-75/w1/ExecReplay-agree.txt`).
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, run after landing commit `7d69216`): `cited-lines.txt` (the NDSS paper's first lines, written by a round-75 seat at the fleet root) copied byte-exact into the lane root (`cmp` exit 0) and committed in `373bf4e7`; the fleet copy deleted. Other untracked fleet files `run_check_probe.py` and `run_check_probe2.py` name another lane's round (kengaku r90) and were not touched. Recorded as `M75-5` in the lesson.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| C1 counter amendment (`restoration_only`, RESULT gate, selftest 6) | `LOG.md` § Round 75, "C1 landing" | `7d692165` |
| SKILL.md gate-registry row; `corpus/instruments/README.md` row | § Round 75, "C1 landing" | `7d692165` |
| S110 registry row (109 → 110) and round-75 note bullet | § Round 75, "C2 landing" | `7d692165` |
| S110 capture and manifest (`corpus/source-snapshots/round-75/`) | § Round 75, "C2 landing" | `7d692165` |
| knowledge entry `fuzzilli-ndss2023-jit-fuzzing-paper.md`; knowledge-expected 90 → 91 | § Round 75, "C2 landing" | `7d692165` |
| F53 admission block (`corpus/README.md`), PROVINCE r75 line | § Round 75, "C2 landing" | `7d692165` |
| QUALITY R121–R123 | § Round 75, "Mistake mining" | `7d692165` |
| lesson `corpus/lessons/round-75.md` (M75-1..M75-4) and wave evidence `.ufo/waves/round-75/` | § Round 75 | `7d692165` |
| SCORECARD round-75 section and move log | `SCORECARD.md` § Round 75 | `7d692165` |
| misroot recovery `cited-lines.txt`; lesson M75-5 | § Round 75, "Mistake mining" (M75-5 added in the lesson) | `373bf4e7` |
| L0 question (assimilation collision; WAVE-DONE routing) | `.ufo/l0-questions.md` line 328 | fleet commit of this report |

## Before → after measurements

Measured against base `f9cc05b5`; landed bytes at `7d692165`, with the `373bf4e7` change (lesson and a copied excerpt) not affecting any counter.

**C1 — `depth:verifiability`, score 4 → 4 (held, nominal R58).**
- Counting command: `python3 corpus/instruments/recheck-cwd-census.py --selftest` (`TMPDIR` scratch).
  - Before: `selftest cases=5 failures=0`, exit 0. After: `selftest cases=6 failures=0`, exit 0.
- Counting command: `cd /tmp && python3 <lane>/corpus/instruments/recheck-cwd-census.py --root <lane> --lane <lane>`.
  - Before (base, `c1-donothing-r75.txt`): `RECHECK-CWD entries=90 noprefix=0 exit2_foreign=0 exit0_foreign=68 exit1_foreign=22 exit_other=0 norecheck=0`, conformant, exit 0.
  - After C1 alone (measured by `ExecC1Amend` and `ReviewC1` on the candidate, and the same bytes in `7d692165` before C2 entry): `entries=90 … restoration_only=0`, conformant, exit 0.
  - After C2 (landed tree, `c1-after-r75.txt`): `entries=91 noprefix=0 exit2_foreign=0 exit0_foreign=69 exit1_foreign=22 exit_other=0 norecheck=0 restoration_only=0`, conformant, exit 0. The +1 is the C2 entry; the declared drift.
- Parity (A4): base counter vs landed counter on the same tree: one differing line, the inserted `restoration_only=0`.
- Kill rule (A3): `MutAuditC1` battery on the same sha256 (`e666ae11…`): M-P1 (restoration into norecheck) exit 1, M-P2 (RESULT drops the conjunct) exit 1, M-P5 (restoration value through `run_foreign`) exit 1; unamended base survives (`cases=5`). M-P4 (marker-absent conjunct removed) survives; routed (R75-2).
- Exec surface: `grep -c 'bash", "-c'` = 1 before and after (`run_foreign`).

**C2 — `coverage`, score 8 → 8 (held; denominator operator-owned).**
- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 109 → 110.
- `git diff f9cc05b5 -- corpus/SOURCES.md | grep -c '^-[^-]'`: 0 removed lines.
- `ls corpus/knowledge/*.md | wc -l`: 90 → 91; `knowledge-expected` 92 → 93 lines, 91 rows, `LC_ALL=C sort -c` exit 0, set-equal to the directory.
- `python3 corpus/instruments/capture-binding-check.py`: `records=88 bound=88` → `records=89 bound=89 unbound=0`, exit 0 (`c2-after-binding-r75.txt`).
- `source-recheck.py --manifest corpus/source-snapshots/round-75/manifest.json --source S110` from `/tmp`: exit 0 (`c2-after-srcrecheck-r75.txt`); max quote 12 words over 24 quotes.
- `python3 corpus/instruments/frontier-recheck-count.py`: `rows=52 admitted=52 → 53`; `FRONTIER-PASS F53 ids=S110`; `entries=55 pass=55 → 56 pass=56`, exit 0 (`c2-after-frontier-r75.txt`).
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`: exit 0 before and after; six inherited W04 warnings unchanged.
- Lead line: `corpus/SOURCES.md:176` (the NDSS lead, base line 175) sha256 `124b3a00…adb5a1`, byte-identical to base.

## Sources & frontier

- **SOURCES.md rows, before → after:** registry 109 → 110 (`grep -cE` above). Rows added by tier: tier A, 1 (S110, paper, `corpus/SOURCES.md:122`). Rows touched old → new: none (the NDSS lead bullet is kept byte-identical and retired in the round-75 note bullet at `corpus/SOURCES.md:272`).
- **Frontier rows advanced:** F52 → F53 (`corpus/README.md` § Round-75 admission; `PROVINCE.md:223`). Knowledge entries 90 → 91. Coverage map: one new row in the § Round-75 admission table.
- **Census (round start and round end):** start `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → `kasegi ok`, exit 0; end → `kasegi ok`, exit 0. Conformance: exit 0 at round end, no warning beyond the six inherited W04.
- **Considerthese:** nothing still unimplemented to mine (ConnectorSweep §2 dispositions for `considerthese/2026-10-26.md`; P4's externalise plank is operator-owned).
- **Assimilation: none** — `merge/kasegi/SOURCES.append.md` stages 94 ids against a registry with 79 collisions; nothing adopted; L0 question filed.
- **Source frontier step:** S110 was opened this round; the one sourced claim (C2) cites it. The OSV overview page remains a lead (not opened).

## Trend verdicts

- **expansion: improved** — one new admitted frontier F53 (the NDSS paper's design, comparison design and evaluation scope) on ground the coverage map did not hold (`corpus/README.md` § Round-75 admission; `corpus/knowledge/fuzzilli-ndss2023-jit-fuzzing-paper.md`).
- **quality: improved** — C1 makes restoration-recheck-only files visible: the base counter counted them as `norecheck` and passed the real tree (`c1-donothing-r75.txt`); the landed counter reports them in `restoration_only` and its RESULT gate requires zero (`c1-after-r75.txt`). C2's 24 manifest quotes are located at their anchors and every quote is at most 12 words. The predicate gaps the attack seats found (M75-2, M75-3) are routed, not hidden.
- **discernment: unchanged** — the attack seats found letter gaps in both frozen predicates (`CriticClaims` F1, F6, F7, F11; `ReviewC1` T2, T6; `MutAuditC1` M-P4), and the lane's self-assessment at freeze did not anticipate them. Nothing was reworded after scoring; the gaps are routed to round 76 (R75-1 to R75-5).

## SHONEN

`grep -c '^## SHONEN'` on this report = 1.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md:982` (this round's gate row for the census counter); prior author-assertion pointer `corpus/lessons/round-47-verifier-spotcheck.md`. Outside promotion verification remains required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md. Untouched this round (no domain task; round 74's documentation-only trial stays the last one, `LOG.md` § Round 74).
- [~] Instructions executable by an agent without oral context. Evidence: `corpus/lessons/round-75.md` § Counting commands (census, source-recheck, capture-binding, frontier and census validate all run from a foreign cwd on the landed bytes).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md:223` (the r75 Frontier amendment and its scope limit); scope unchanged.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. Attempt 2 used `patch`, `pdftotext`, `curl` and `python3` already present; no `pacman`, no `uv`, no `npm`, no host sysctl change.

## Round shape, waves and seats

- Shape: **one v1 wave of 12 seats** (`.ufo/waves/round-75/w1-spec.json`, `w1-dispatch.json`), inside the run-15 band 8–16. No residual call; no wave 2.
- Role mix: executor×3 (`ExecC1Amend`, `ExecC2Capture`, `ExecReplay`), scout×1 (`ScoutSurface`), scribe×2 (`ScribeEntry`, `ScribeLesson`), connector×1 (`ConnectorSweep`), reviewer×2 (`ReviewC1`, `ReviewC2`), critic×1 (`CriticClaims`), mutation-tester×1 (`MutAuditC1`), sentinel×1 (`SentinelCounter`). Attack seats 5/12 (42 %, ≥25 %). Connector seats 1 (≤2). The §3 L2 floor is met inside the wave (planner = this L1).
- Dead seats: 0 (`w1-results.json`, `note: None` for all 12).
- Round total: 12 seats.
- Seat run notes: `ExecC1Amend` and `ScribeEntry` removed their scratch dirs; `CriticClaims` wrote one report at the fleet root by a relative path, copied byte-exact to the lane and removed (recorded as M75-5).
- Attempt 1's dispatch named `l1: KasegiR75`; Main rerouted WAVE-DONE to `KasegiR75a2` (`.ufo/l0-questions.md` line 328 records the routing gap).

## Open questions (L0)

- `.ufo/l0-questions.md` line 328: assimilation of `merge/kasegi/` (79 id collisions; decide renumber-by-document or re-stage) and the ready-file `l1` routing.

## Commands run by the integrator (for the closure verifier)

```sh
cd /home/vgpnk/Projects/shokunin/kasegi-shokunin
TMPDIR=/fast/scratch/hyaku/kasegi-r75/L1/tmp python3 corpus/instruments/recheck-cwd-census.py --selftest      # cases=6 failures=0
cd /tmp && python3 /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/instruments/recheck-cwd-census.py --root /home/vgpnk/Projects/shokunin/kasegi-shokunin --lane /home/vgpnk/Projects/shokunin/kasegi-shokunin   # conformant exit 0
cd /tmp && python3 /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/instruments/source-recheck.py --manifest /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/source-snapshots/round-75/manifest.json --source S110   # exit 0
cd /home/vgpnk/Projects/shokunin/kasegi-shokunin && python3 corpus/instruments/capture-binding-check.py && python3 corpus/instruments/frontier-recheck-count.py   # records=89 bound=89; FRONTIER-PASS F53; entries=56 pass=56 exit=0
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi   # kasegi ok, exit 0
```

Receipts: `.ufo/waves/round-75/controls/{c1-donothing-r75,c1-redbefore-restoration-r75,c1-after-r75,c2-base-counters-r75,c2-after-binding-r75,c2-after-srcrecheck-r75,c2-after-frontier-r75,c2-after-census-r75}.txt`; wave evidence `.ufo/waves/round-75/w1/`.
