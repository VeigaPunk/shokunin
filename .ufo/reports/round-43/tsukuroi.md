# tsukuroi — round 43 report (hyaku run 9, attempt 1)

L1: `TsukuroiR43`. Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`. Base
`6951ead90566b2d74f7c45b4efca29246badad64` (the `jj-lane.sh state` local at round start); final lane hash
`5f8b3c58bbf46128c0d924149bf795bc8199c66b` (`git ls-remote origin refs/heads/master` prints it). Wave evidence:
`.ufo/waves/round-43/` in the lane (called `W/` below). Stale-lane: respawn-per-round driver; no other mission of this
lane is open. No earlier attempt of this round exists (`.ufo/watchdog.log` has no `lane-dead-no-report tsukuroi round=43`
line); nothing was inherited.

## Work performed

Declared claims (two, frozen at `fe35700183188f7d712e2932cabde1944efca052` before any seat; `SCORECARD.md`
"Round 43 — declaration"):

- **C1, operability.** `tools/boot-chain-audit.sh` runs under `set -uo pipefail`. Its `boot_inputs_newer` read
  `find … | grep -q .`, so a missing start point or an unreadable directory made it print "no input newer", and the
  BOOTED-OBSERVED gate passed (a fail-open). The fix decides on find's output.
- **C2, depth (sourced: S240 opened this round).** `corpus/knowledge/btrfs-scrub-record-r43.md` has three rows: SR1 (the
  scrub record's write discipline), SR3 (what resume writes; when recording failures print) and SR6 (an unprivileged
  status never reads `running`). They rest on S237, S240 and S241, and wave-2 reads judged them.

Work items:

- Protocol load: skill://shokunin, MISSION, AXES, CORPUS, LEARNING, skill://swarm. Lane files: SCORECARD (round-42
  planned row), the round-42 spot-check (`corpus/lessons/round-42-verifier-spotcheck.md`), considerthese 2026-10-26 and
  QUALITY 79-91.
- Freeze `fe357001`. It holds the declaration, the frozen counters `tools/score-bootinputs-r43.py` (sha256 `886f92c8…e10f`)
  and `tools/check-scrub-record-r43.py` (`b4602c56…9854`), the pinned sources `W/frozen/src/` (ioctl.c, SHA256SUMS,
  FETCH.txt) and `W/frozen/hostcap/`, and the pre-data control batteries. The controls are `W/controls/battery-summary-c1.jsonl`
  and `-c2.jsonl`. Each reads `should_fail_accepted 0, control_accepted 1`.
- Before receipts at the base: `W/before/c1-before.jsonl` (FAIL, correct 8) and `W/before/c2-before.jsonl` (FAIL, rows 0).
- Implementation `717b716a`: the `inputs_newer_than` helper with three `R43-C1` selftest cases; the C2 draft entry; rows
  S240 and S241; the S237 used-by change; and the supersession pointer at `corpus/knowledge/btrfs-scrub-record-r42.md:4`.
- Wave 1 (44 seats) built and attacked the work. Integration `9b974f2a`:
  - Nine C2 narrowings. Each was checked against its source line, and the check is recorded in the
    `corpus/lessons/round-43.md` "Entry gate (C2)" table (QUALITY 91).
  - One wave-1 claim was rejected ("device id never emitted"; `scrub.c:782-792` shows it is emitted).
  - A fourth selftest case kills a surviving mutant (49 cases).
  - SKILL sections "Boot-input freshness under pipefail — round 43" and "Scrub record re-grounded — round 43".
  - The round43 registry table, with the two new counters.
  - PROVINCE and README notes.
- Registry fix `8acf0b02`: the REGISTRY-ROW-AMBIGUOUS finding of `check-registry-coverage.py` is fixed. It now passes
  68/68 (`W/w2/RegistryFinal.md`).
- Wave 2 (34 seats, six counted C2 reads; dispatch `64646d6e`). Integration `5647d4ff`:
  - The SR3 skip condition was narrowed after `W/w2/C2CritSR3.md` bound `partly`. The new text was checked against
    `scrub.c:1430-1437`.
  - SKILL and lesson reference fixes.
- Residual call: two reviewers, dispatch `d950df34`, records at `c3954913`. The counted residual `W/residual/C2ResSR3.md`
  binds `ROW SR3 VERDICT: holds` on the narrowed row. `W/residual/ResFixCheck.md` found one more mislabel, which is fixed.
  QUALITY 92 (R43-CAP-HEADER-DUP) was added.
- Outcome `a87249c7`: the measured outcome, the axes table and the capabilities table, which has one header row
  (QUALITY 92 count prints 1). Also the LOG entry and the after receipts. Self-assessment receipt `5f8b3c58` (27 checks,
  0 mismatches).
- Frontier step: the census was run at start and end; one SOURCES row (S240) was opened and cited by C2; six mistakes
  were mined (`corpus/lessons/round-43.md` `## Mistakes`); considerthese "Cross-note correction propagation map" was
  mined (`W/w1/ConsiderMap.md`, closed by pointers).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` printed nothing at the end. No lane-43 file
  was found at the fleet root. Scratch `/fast/scratch/hyaku/tsukuroi-r43` was removed after landing.

## Landed changes

Every commit was landed by `jj-lane.sh`, which printed `landed <hash>` after remote verification. LOG entry:
`LOG.md` "Round 43 — hyaku run 9".

| Commit | Change |
|---|---|
| `fe35700183188f7d712e2932cabde1944efca052` | declaration, frozen C1/C2 counters, control batteries + receipts, pinned ioctl.c and host capture |
| `717b716a8943151ace8657e0ca23d7d9b8434f26` | C1 fix in `tools/boot-chain-audit.sh`; C2 draft entry; S237 used-by, S240, S241; r42 entry pointer; before receipts |
| `7d0ed1c2d62961cbde8a4d6be120b2573ebbd8f9` | C1 after receipt at `717b716`; w1 spec, generator and validated dispatch |
| `9b974f2a5fdd151760ac166bc91dc75749697b2f` | w1 integration: entry narrowings, 4th selftest case, SKILL sections + registry table, PROVINCE/README notes, lesson draft, w1 reports |
| `8acf0b022586a0f3164c77659fb96ba5f90949b6` | registry row names one tool |
| `64646d6e5749e0b5b6e458aa0753d39c47404e6b` | w2 spec and validated dispatch |
| `5647d4ff94f5882f99c02d20ec703d0191aea2d9` | w2 integration: SR3 narrowing, SKILL/lesson fixes, w2 reports and results |
| `d950df341f98e87b8510f7b1bcbb1790b008af12` | residual-call dispatch |
| `c3954913f6b376b4f9ff3d596f1eaefc6846e937` | residual records, QUALITY 92, lesson fix |
| `a87249c742852b63dffe537eefaf3a1db8edd9e4` | measured outcome, axes and capabilities tables, LOG entry, after receipts, sources census |
| `5f8b3c58bbf46128c0d924149bf795bc8199c66b` | self-assessment receipt (lane tip) |

## Before → after measurements

**C1 (operability).** Counter `python3 tools/score-bootinputs-r43.py --revision <REV> --scratch <DIR>`. Predicate:
`cases == 16 and correct == 16 and identity_ok == 1 and live_agree == 1 and selftest_pass == 1 and selftest_r43 >= 2`.

| Revision | Result | Receipt |
|---|---|---|
| base `6951ead9` | **FAIL**: correct 8 of 16 (the eight masked cases read 0), selftest_r43 0, selftest PASS total=45 | `W/before/c1-before.jsonl` |
| `717b716a` | **PASS**: correct 16, selftest_r43 3, selftest 48 | `W/after/c1-after-717b716.jsonl` |
| measured `c3954913` | **PASS**: correct 16, identity_ok 1, live_agree 1, selftest PASS total=49, selftest_r43 4 | `W/after/c1-after-c395491.jsonl` |

Kill rules did not fire (`W/w2/C1FinalKillRule.md`):
- Only `inputs_newer_than`, `boot_inputs_newer` and `run_selftest` changed.
- The round-42 C1 counter PASSes, and the census selftest gives 132/132.

**C2 (depth).** Counter `python3 tools/check-scrub-record-r43.py --revision <REV>`. Predicate:
`rows == 3 and quotes_ok == 3 and props_ok == 3 and host_ok == 3 and sources_ok == 1 and verdicts_ok == 3 and
novelty_base_hits == 0 and pointer_ok == 1`.

| Revision | Result | Receipt |
|---|---|---|
| base `6951ead9` | **FAIL**: rows 0 | `W/before/c2-before.jsonl` |
| measured `c3954913` | **PASS**: every conjunct is met | `W/after/c2-after-c395491.jsonl` |

Bound verdicts at the measured revision:
- SR1: holds / holds.
- SR3: holds / partly, then the residual `C2ResSR3` reads holds.
- SR6: holds / holds.

`transcripts_bound` is 7 of 7 when the counter reads the host session dir (`W/after/c2-after-c395491-direct.json`).

Kill rules did not fire. I audited all six counted outputs: none carries a second or contradictory verdict line.

Recorded counter limits (not claimed):
- C1: the namespace's mount-table, uid_map, script-path and cwd channels are open (K7 PASS). The counter does not
  exercise the empty-btime branch or every start point in every draw.
- C2: the binding accepts a padded or blank-line-prefixed verdict line. It also accepts a JSON `verdict` field that
  contradicts `verdict_line`.

## Sources & frontier

| Item | Value |
|---|---|
| Command | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` |
| Start | `tsukuroi ok`, exit 0, 40 W04, 239 rows (`W/before/sources-census-start.txt`) |
| End | `tsukuroi ok`, exit 0, 40 W04, 241 rows (`W/after/sources-census-final.txt`; row count from `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`) |
| Rows added by tier | A: 2 (S240 `code`, Linux v7.2.11 `fs/btrfs/ioctl.c`; S241 `own-work`, the round-43 host capture) |
| Rows touched old→new | S237 `used-by`: `…btrfs-scrub-record-r42.md` → `…r42.md, …btrfs-scrub-record-r43.md` (logged in the lesson Gate) |
| Frontier rows advanced | none moved Frontier → Core. The scrub-record line is re-grounded from source and gains the kernel-side privilege fact (SR6). |
| Sourced claim | C2 rests on S240, which was opened this round. The Gate records the URL, the access date and a located quote (`ioctl.c:3132-3133`). |

Assimilation: none. `merge/tsukuroi/` was evaluated read-only (`W/w1/AsmGate.md`):
- `initramfs-hook-api-r25.md` is refused this round. Its flip conditions are recorded.
- `ext4-journal-guarantee-r32.md` is rejected as out of province.

The quarantine slice (12 rows) and the collision check are in `W/w1/AsmGate/`.

considerthese: mined "Cross-note correction propagation map" (`considerthese/2026-10-26.md`) into the lesson. The four
unpointed dependents and the PROVINCE overreach it found are now pointed or corrected.

## Trend verdicts

These are author-side verdicts. Non-author closure is pending.

- **expansion: unchanged.** The r43 entry deepens the scrub-record Frontier line (held since round 26). It enters no new
  coverage-map ground (`corpus/README.md` "Round-43 coverage note"). No capability row is new; the boot-chain-audit row
  is updated.
- **quality: improved.**
  - The round-42 entry's withdrawn SC1/SC3 text and its host-errno-only running-state note are superseded by stronger
    rows. Those rows are verified by counted reads at pinned source lines (C2 PASS), and the old entry's header points
    to them.
  - A fail-open in the lane's own boot-chain audit is fixed, with red-before evidence.
  - S237 and S240 were re-fetched byte-identical.
  - No admitted entry failed its re-check.
  - The PROVINCE overreach was marked.
- **discernment: improved (provisional on the outside check).**
  - The gate rejected a false wave-1 claim with source evidence (scrub.c:782-792; confirmed by `W/w2/C2CritRejectF1.md`).
  - It narrowed nine sentences on checked lines.
  - The one counted `partly` became a narrowed, re-read row.
  - The R43-CAP-HEADER-DUP mistake, which no criterion captured, became QUALITY 92 citing its lesson row.
  - The non-author spot-check of one admit and one reject is still owed. Candidates are in the lesson.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources.
  - Round 43 adds the boot-input pipefail signature table and the scrub-record re-grounded observation → reading →
    action table (`SKILL.md` "Boot-input freshness under pipefail — round 43", "Scrub record re-grounded — round 43").
  - Wave-2 `W/w2/SkillReview.md` reviewed them; that seat is the lane, not a non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md.
  - `LOG.md` "Round 43 — hyaku run 9": a defect in the lane's boot-chain audit was found, fixed, shown red-before and
    re-measured.
  - Non-author replay is pending.
- [~] Instructions executable by an agent without oral context.
  - The round-43 sections carry paste-ready read-only commands; `W/w1/C1ExecHandRepro.md` reproduced the fail-open from
    the text.
  - A whole-SKILL retest was not executed.
- [~] No cross-domain bleed (PROVINCE.md still accurate).
  - `W/w1/ConnSiblings.md` found no contested scope. No live sibling pin moved.
  - The round-42 PROVINCE overreach is corrected by an appended note.

## Round shape, seats, routing, incidents

- **Shape:** two v1 waves under `ufo-wave-policy.json`, plus one residual call.
  - w1: 44 seats — 12 executor, 9 critic, 6 reviewer, 6 scribe, 3 mutation-tester, 3 scout, 3 connector, 2 sentinel.
  - w2: 34 seats — 11 reviewer, 10 critic, 6 executor, 2 scout, 2 connector, 1 mutation-tester, 1 sentinel, 1 simplifier.
  - Residual: 2 reviewer seats in one ordinary call, counted in the round total. Its dispatch was hand-built in the w2
    schema because the wave band does not apply to a residual call.
  - Round total: 80 seats. Dead seats: 0. Every seat settled with a report.
  - m_flash roles were 29/44 and 18/34 of the seats; attack roles were 18/44 and 22/34.
- **Routing:** the run-8 map from `~/.omp/agent/config.yml`. No model was passed.
- **Planner seat:** held by the L1 (orchestrator ruling 2026-10-19).
- **Spawn:** every wave was spawned inline by the orchestrator from my `.ready` files. WAVE-DONE was received for w1, w2
  and the residual call.
- **Incidents:**
  - `W/w1/SentMisroot.md` F1/F2: seat imports left `tools/__pycache__` in the lane (ignored), and I left pre-wave strays
    in the shared scratch root. Both were removed. Mistake R43-L1-SCRATCH-STRAY.
  - `W/w2/SentScopeFinal.md` reports lane `.git` index/object writes during w2 (unattributed; no ref, jj or tracked
    change) and two fleet-root files `p.out`/`p.err`, which a chousa round-52 seat wrote. I did not touch them, and they
    were gone at my final sweep.
- **Adjacency handoffs (report-only; the owners decide):** `W/w2/AdjFinal.md`.
  - tameshi `corpus/knowledge/service-optin-protocol.md:153` (also `:249`, and `fleet-kill-rate-ledger.md:71`) cites
    census `915-970` for the round-5 hardening block. At the tip that block starts at census `:2425` (56 lines); the pin
    has been dead since round 6+. It is not a round-42 or round-43 shift.
  - mori `PROVINCE.md:287` cites census `:376,1100-1115`. Its referents are `PRESSURE_FILE` at `:455`, the arm
    `:1103-1118` (content at `c8efaa3f:1097-1112`, +6 by round 42) and the pressure read at `:1200-1207`.
  - Frozen chousa r36 records pin `boot-chain-audit.sh:1174-1191`; that content is now at `1183-1200`. No action.
  - No sibling pins a line of `btrfs-scrub-record-r42.md`.
- **Tool installs:** none, by me or by any seat that reported.
- **L0 questions:** none opened.
