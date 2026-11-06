# kengaku — round 95 report (hyaku run 15, attempt 1; L1 KengakuR95)

Lane `kengaku-shokunin`, branch `master`. BASE `4524072dfae9c5e8210592b7c1da26959aa29dae` (round 94
closed). Final lane hash **`c8598439a32295bcbe114c6b9ccb3dc1d23151e3`**
(`git ls-remote origin refs/heads/master` → `c8598439a32295bcbe114c6b9ccb3dc1d23151e3`).
Inherited state: clean tree, no `lane-dead-no-report kengaku round=95` line in the watchdog log; nothing inherited.

## Work performed

Two claims, frozen at F `d9cd18a7` in `plans/round-95-claims.md`:
**R95-C1 — coverage** (the lowest non-retired axis, held at its L0 cap 7): a thirteenth located
offline replay of a pinned Terminal-Bench 2.0 grader, `fix-code-vulnerability`. **R95-C2 —
calibration** (held at ceiling 10): the number of known false freeze-integrity gates that pass the
lane's counter, 14 → 0. The 14 are the false gates the round-94 wave built. The claim is declared
in-sample.

- Protocol load and claim choice. I read the round-94 spot-check
  (`corpus/lessons/round-94-verifier-spotcheck.md`). Each of its 7 routed defects has a disposition in
  `corpus/lessons/round-95.md`, table "Round-94 spot-check routed defects".
- P0 `2457f0254efcef452591fc1ac691dc7670b1aded`: 15 mechanism predictions were filed before any probe
  run (`.ufo/waves/round-95/L1/predictions-mechanism.txt`). The same commit holds the capture
  `corpus/evidence/round95/graders/fix-code-vulnerability/` (7 files, HTTP 200,
  `.ufo/waves/round-95/L1/capture-fetch.txt`) and the C2 population `plans/round95-false-gates.tsv`
  (14 rows with sha256). It also holds the 14 BEFORE receipts, `controls/before-r94-counter-<id>.txt`:
  each shows the frozen round-94 counter printing `PREDICATE R94-C2 pass`, rc 0, at BASE.
- P1 `16dcfed7ef4c9e2ac7d28568d855905a8457b20d` holds the instruments:
  - `plans/round95_vuln_probe.py`: rebuilds `/app/bottle.py` from upstream bottle @ `0207a34f` with the
    Dockerfile's two sed deletions, runs `solve.sh` unmodified, and runs 15 cases × 7 legs in bwrap.
  - `plans/round95_c1_replay.py`: L6 now compares the stamps and L7 checks the legacy fields.
  - `plans/round95_c2_counter.py`: 20 CLI fixtures; W3 drives the battery red with three probe
    mutations; PREDICATE line must agree with rc; ten CLI mutants.
  - `plans/round95_false_gate_census.py`: the C2 counting command.
  - Dry-run receipts are in `.ufo/waves/round-95/L1/dryrun/`. 15 of 15 predictions held.
- P2 `7783e9cbc83c207a3eb09224de68050c383f68f0`: the controls, tabulated in
  `.ufo/waves/round-95/L1/controls/README.md`.
  - C1 receipt-side controls on a P1 clone with a draft table. The honest state passes all 9 legs, rc 0.
    Each forgery is rc 1 at its intended leg: probe swap (L8), foreign LANE_TIP (L3), dropped cases
    (L5+L6), forged stamp (L6), legacy fields omitted (L7), ledger-only (L1), member swap (L7).
    Sandbox outage gives rc 2.
  - C2 do-nothing: the census scoring the round-94 counter gives `passing=14`, rc 1.
- F `d9cd18a7519a58a1fa6d1cb9768e3873c31cd545`: the frozen claims with an 11-row `frozen-instruments` table.
- C `afe9c229e37aecc0b52b78b0e5c7dd80cf0cf239` is the measured tip T for both counters. It holds:
  - the official receipt `corpus/evidence/round95/vuln-probe.txt` (15/15 `ok=True`);
  - the ledger flip, with legacy-gate fields;
  - the SKILL decision-table class cells, set to the ledger;
  - SOURCES rows S303–S309 (`corpus/SOURCES.md:319-325`).
- L1 receipts at T and the wave spec/dispatch: `ea19299d8dacb6d024c429c53982fb5a73d50035`
  (`.ufo/waves/round-95/L1/c1-tip.txt`, `c2-tip.txt`, `c2-tip-do-nothing-r94-counter.txt`,
  `legacy-r79-gate.txt`, `lane-gates-end.txt`).
- Integration after WAVE-DONE: `1c00331c3c39bc1af308d625771cabe0cc06889b`. It holds:
  - the lesson `corpus/lessons/round-95.md` (Gate, M1–M3, W-1…W-16);
  - Q77 and Q78 (`corpus/QUALITY.md:1395-1396`);
  - the SCORECARD round-95 section (`SCORECARD.md:4402`) and the capability-row update;
  - SKILL registry rows (`SKILL.md:699-700`) and the LOG entry (`LOG.md:3607`);
  - the `mteb-retrieve` subject revert (lesson M2) and the w1 evidence.
- End receipts at the landing tip: `c8598439a32295bcbe114c6b9ccb3dc1d23151e3` (`.ufo/waves/round-95/L1/end-receipts.txt`,
  `census-end.txt`, `misroot-sweep.txt`).
- Conformance items (no claim slot):
  - Round-94 routed defect 5: the legacy round-79 ledger gate went from 14 defects (BASE) to 0 (T) to
    1 (landing tip, see harm check).
  - Round-94 W-10: `--work` inside the lane is now refused by every round-95 instrument.
  - Round-94 SP-2: the probe sets `LANG=C.UTF-8`.
- Planner seat: held by the L1 (the validator rejects `planner`). No planning data-walk was delegated.

## Landed changes

| commit (landed, remote-verified) | change | LOG entry |
|---|---|---|
| `2457f0254efcef452591fc1ac691dc7670b1aded` | P0 predictions, capture, C2 population and BEFORE receipts, census start | `LOG.md:3607` (order line) |
| `16dcfed7ef4c9e2ac7d28568d855905a8457b20d` | P1 instruments and dry-run receipts | `LOG.md:3607` |
| `7783e9cbc83c207a3eb09224de68050c383f68f0` | P2 controls (C1 receipt-side, C2 do-nothing and designated legs) | `LOG.md:3607` |
| `d9cd18a7519a58a1fa6d1cb9768e3873c31cd545` | F `plans/round-95-claims.md` | `LOG.md:3607` |
| `afe9c229e37aecc0b52b78b0e5c7dd80cf0cf239` | C: receipt, ledger flip and legacy fields, SKILL class cells, SOURCES S303–S309 | `LOG.md:3607` R95-C1 / Conformance / Sources bullets |
| `ea19299d8dacb6d024c429c53982fb5a73d50035` | receipts at T, w1 spec and validator dispatch | `LOG.md:3607` R95-C1 / R95-C2 / Wave bullets |
| `1c00331c3c39bc1af308d625771cabe0cc06889b` | integration: lesson, Q77/Q78, SCORECARD, SKILL rows, LOG, `mteb-retrieve` revert, w1 evidence (12 seat dirs, results, one env receipt redacted) | `LOG.md:3607` Mistakes / Wave bullets |
| `c8598439a32295bcbe114c6b9ccb3dc1d23151e3` | end receipts at the landing tip, census end, misroot sweep | `LOG.md:3607` Sources bullet |

## Before → after measurements

**R95-C1 (coverage).** Counting command:
`python3 plans/round95_c1_replay.py --lane . --rev afe9c229e37aecc0b52b78b0e5c7dd80cf0cf239 --work DIR`
- Before, at BASE `4524072d` (`controls/c1-base.txt`): `LEGS L1..L9=fail`, `TARGET executed_rows=38 … executed=0 …`,
  `PREDICATE R95-C1 fail`, rc 1.
- After, at T `afe9c229` (`c1-tip.txt`): `LEGS L1=pass … L9=pass`,
  `TARGET executed_rows=39 member=fix-code-vulnerability located=1 executed=1 cases=15 legs=105 mismatches=0 defects=0`,
  `PREDICATE R95-C1 pass`, rc 0. The landing tip gives the same result (`end-receipts.txt`).
- Ledger moves:
  - executed: 38 → 39 of 88;
  - `file-artifact`: 29 → 30 of 76;
  - `serialization-schema`: 5 → 6 of 10;
  - the member set is BASE ∪ {fix-code-vulnerability}.
- Self-verdict: **met on its frozen predicate**. The non-author critic rules "verifies-narrowed". The
  replay covers the six `test_outputs.py` functions on a `/app/bottle.py` that is byte-identical to the
  prebuilt image's. It does not cover the TB2 reward:
  - In the image, the repository's own suite scores C11 (half fix) and C15 (package shadow) as reward 0.
  - Two reward-1 states need no fix at all: `rm /app/bottle.py`, because a site-packages oracle remains,
    and `git checkout -- bottle.py`, because `.git` keeps the oracle.
  - Both are routed to round 96.

**R95-C2 (calibration).** Counting command:
`python3 plans/round95_false_gate_census.py --lane . --rev afe9c229e37aecc0b52b78b0e5c7dd80cf0cf239 --work DIR`
- Before, at BASE: the frozen round-94 counter passes 14 of 14 false gates (`controls/before-r94-counter-*.txt`).
  The do-nothing census at T gives `FALSEGATES total=14 passing=14 designated_red=0 honest=pass`, rc 1
  (`c2-tip-do-nothing-r94-counter.txt`).
- After, at T (`c2-tip.txt`): `FALSEGATES total=14 passing=0 designated_red=14 honest=pass`, `PREDICATE R95-C2 pass`, rc 0.
  Honest gate v2 is unchanged (sha256 `8574b4d5…`). Its legs:
  - W1 pass;
  - `W2 pass fixtures=20 ok=20`;
  - `W3 pass probes=3`;
  - `W4 pass freeze=d9cd18a7519a summary=(11, 11, 0)`;
  - `W5 pass mutants=10 killed=10`.
- Self-verdict: **met on its frozen predicate, in-sample as declared at F**. The non-author critic rules
  "verifies-narrowed: in-sample regression count, not calibration of unseen gates". Evidence against a
  broader reading:
  - At least 8 held-out false gates pass the counter 5/5.
  - A behaviour-preserving rename turns the counter red.
  - 14 of 20 counter mutants survive.
  - The operator/closure rules on this.

**Harm check (not claims).** Measured at the landing tip `c8598439`, also at T where noted
(`end-receipts.txt`, `lane-gates-end.txt`):
- Unchanged and green:
  - `grader.py` `VERDICT: PASS`;
  - `plans/round68_capability_table.py` `PREDICATE R68-A3 pass`;
  - `plans/round91_f1_counter.py` `PREDICATE R91-F1 pass`;
  - `plans/anchor_line_check.py` `live=0 cells=0`;
  - `plans/state_check.py` (ExecLegacyHarm: 318 match, 0 mismatch, at BASE and T).
- Harm found and reverted: the C commit's `mteb-retrieve` subject repair turned `plans/round87_c1_replay.py`
  from PASS to FAIL at T (ExecLegacyHarm H1, lesson M2). It was reverted in `1c00331c`. At the landing tip
  the round-87 counter passes again (`PREDICATE R87-C1 pass`, rc 0). The round-79 gate now reports
  `DEFECTS n=1` (SUBJECT-MISMATCH `mteb-retrieve`): two lane gates disagree about one cell, and this is
  routed to round 96.
- Disclosed: `plans/round94_c1_replay.py --rev T` goes red because its L7 pins `executed_rows=38`. Rounds
  90–93 counters are already red at BASE for the same reason.
- Other axes held: novelty 8, depth 10, operability 10, freshness 10, adjacency 9.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
  - Round start: `kengaku ok`, exit 0, 294 rows (`.ufo/waves/round-95/L1/census-start.txt`).
  - Round end: `kengaku ok`, exit 0, 301 rows (`census-end.txt`; only the pre-existing W04 duplicate-url warnings).
  - Row count: `grep -c '^| \?S[0-9]\+ ' corpus/SOURCES.md` 294 → 301.
- Rows added by tier, tier A ×7 (`corpus/SOURCES.md:319-325`):
  - **admitted / mined**: S303 grader, S304 solve.sh, S305 Dockerfile oracle-removal lines, S306 upstream
    bottle.py @ `0207a34f`, S307 instruction.
  - **rejected** with flips: S308 test.sh, S309 task.toml.
  - Quotes and word counts were computed by the script that wrote the rows. The anchor gate gave `live=0`
    before the commit.
  - The wave's ScoutSources re-opened all 7 live: HTTP 200, sha256 = row = capture.
- Rows touched old → new: none.
- Frontier rows advanced: ledger member `fix-code-vulnerability` unexecuted → executed (round 95).
- Sourced claim: R95-C1 rests on S303–S306 (opened 2026-11-05; Gate block in `corpus/lessons/round-95.md` `## Gate`).
- Mistake mined: `corpus/lessons/round-95.md` `## Mistakes`, M1–M3. Each criterion is shown able to fail:
  - M1 (wrong cwd, recurring) → Q77;
  - M2 (a ledger repair broke a pinning counter) → Q78;
  - M3 (in-sample read as calibration) → routed.
- Assimilation: none (`merge/kengaku/` held by L0 `kengaku | round-54`). considerthese: none taken (latest file
  2026-11-05; its residual is not implemented).

## Trend verdicts

- **expansion: improved.** The population frontier moved 38 → 39 of 88, with two class-cell moves. Five tier-A
  rows were admitted on a member the corpus did not hold (S303–S307). There is new member knowledge: the
  `_hval` gap, the package shadow, and two reward-1 holes in the image (site-packages and `.git` oracle copies).
- **quality: unchanged.** No admitted `knowledge/` entry was superseded or re-verified. The legacy ledger
  repair is conformance, and it is partly reverted.
- **discernment: improved.**
  - S308 and S309 were rejected with flips. S309's flip was exercised by a non-author seat; the lesson's
    `## Gate` row records the result and the updated rejection reason (the registry row itself is unchanged).
  - Q77 and Q78 are new criteria grounded in mistakes M1 and M2.
  - The critic's narrowing of both claims is recorded beside the self-verdicts, not overwritten.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:699-700` (new `round95-false-gate-census` and `round95-c2-counter` registry rows); decision-table class cells set to the ledger (`SKILL.md:71-84`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:3607` (fix-code-vulnerability replay, receipt `corpus/evidence/round95/vuln-probe.txt`)
- [~] Instructions executable by an agent without oral context — `plans/round-95-claims.md` (each predicate is one command; controls `.ufo/waves/round-95/L1/controls/README.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-95/w1/ConnectorOverlap.md` (no sibling replays TB2 graders; kaidoku's forgery controls are a complement)

## Round shape, seats, extras

- Shape: ONE v1 wave `w1` (policy `scripts/hyaku/ufo-wave-policy.json`, band 8–16), 12 seats. No residual call. Round total: 12.
- Role mix: 3 executor, 1 scout, 1 connector, 1 scribe, 2 reviewer, 1 critic, 2 mutation-tester, 1 sentinel.
  Attack share (reviewer, critic, mutation-tester) is 5/12 = 42 %. One connector.
- Dead seats: none. All 12 reported (`.ufo/waves/round-95/w1-results.json`). Each seat prompt led with `/skill:godspeed`
  plus the verbatim `directive.md` bytes.
- Credential material: SentinelProbe's `receipts/outside-env-values.txt` held the host's full environment with live
  credential values. Before the wave commit I replaced every value with its length (names kept). No credential bytes
  were committed or pushed. The underlying exposure is that the probe sandbox inherits the host environment (SP1,
  routed to round 96 with a verified `--clearenv` fix).
- Misroot sweep (`.ufo/waves/round-95/L1/misroot-sweep.txt`): `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows `.scratch/*` (orchestrator-owned) and `w4lines.txt`. `w4lines.txt` was created 16:57 -03, before this round's
  launch, and has no kengaku content, so it was left untouched. No misroot.
- Open L0 questions: none new this round. The existing kengaku L0s (rounds 54, 90–92) were routed around.
- Tool installs:
  - L1: none.
  - ReviewerC1, ExecC1Rerun: pytest 8.4.1 via `uv pip`, into scratch venvs only (Python 3.14.8 and uv-managed 3.11.17).
  - CriticClaims: `docker pull alexgshaw/fix-code-vulnerability:20251031` (official Docker Hub tag, digest
    `sha256:cac32525…c5c0`, ~695 MB). The image is still in the local daemon; `docker rmi` reclaims it.
  - No pacman, no sysctl changes.
- Scratch: `/fast/scratch/hyaku/kengaku-r95` removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
