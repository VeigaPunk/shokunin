# kengaku — round 96 report (hyaku run 15, attempt 2; L1 KengakuR96 → KengakuR96a2)

Lane `kengaku-shokunin`, branch `master`. BASE `45740a616028015b5dfcf9900753e3bb5e6fe689` (round 95
closed). Final lane hash **`f6033dadc7ae8694c0b2156a020d671284dff6b2`**
(`git ls-remote origin refs/heads/master` → `f6033dadc7ae8694c0b2156a020d671284dff6b2`).
Inherited state: `.ufo/watchdog.log` has `2026-11-05T23:31:12-03:00 lane-dead-no-report kengaku round=96`. Attempt 1
(KengakuR96) landed P0 → F → C → the receipts at T (`599c1fa1`) and dispatched wave w1, then died. Attempt 2 reused
every committed byte and every untracked w1 seat output after re-reading each against its receipts. Nothing was
discarded. The orchestrator session also crashed, and 7 of the 13 w1 seats died with it.

## Work performed

Two claims, frozen at F `be3ff962` in `plans/round-96-claims.md`:
- **R96-C1 — coverage** (the lowest non-retired axis, held at its L0 cap 7): a fourteenth located offline replay of a
  pinned Terminal-Bench 2.0 grader, `multi-source-data-merger` @ `2fd12b88`.
- **R96-C2 — calibration** (held at ceiling 10): fourteen standing C1 counters (round 79 gate, rounds 83–95). All are
  recorded as met, but six are red at BASE. The target was 6 red → 0 red under a frozen battery predicate.

Work items:
- Protocol load and claim choice (attempt 1). The round-95 spot-check's 7 routed defects each have a disposition in
  `corpus/lessons/round-96.md`, table "Round-95 spot-check routed defects".
- P0 `ff6765a6`: 17 mechanism predictions (`.ufo/waves/round-96/L1/predictions-mechanism.txt`), the capture
  `corpus/evidence/round96/graders/multi-source-data-merger/`, census start, and the standing-counter BASE receipts
  `.ufo/waves/round-96/L1/base/`.
- P1 `cea469bd` and P1b `e8a80c0e`: the instruments.
  - `plans/round96_merger_probe.py`: bwrap `--unshare-all --clearenv`, no `/etc`. The agent venv is python 3.11 /
    pandas 2.2.3 / pyarrow 17.0.0; the grader venv is python 3.13 / pandas 2.3.3 / pyarrow 22.0.0. It runs 17 cases × 4 legs.
  - `plans/round96_c1_replay.py`: legs L1–L9; L7 is keyed to the member set.
  - `plans/round96_standing_battery.py`: STANDING / BITES / GROWS.
  - In the dry run, 17 of 17 predictions held (`L1/dryrun/probe-dryrun-1.txt`).
- P2 `a3b57321`: controls, tabulated in `.ufo/waves/round-96/L1/controls/README.md`.
  - C1: do-nothing fails, positive passes, forged receipt fails, wrong cwd gives rc 2.
  - C2: positive passes, `c1-only` do-nothing fails (red 7), the `delete-l7` and `repin-abs` forgeries fail,
    `c2-only` separability passes.
- F `be3ff962`: 11-row `frozen-instruments` table and 7-row `candidate-bytes` table.
- C `09717e49` is the measured tip T. It holds:
  - the official receipt `corpus/evidence/round96/merger-probe.txt` (17/17);
  - the ledger flip;
  - the `mteb-retrieve` subject re-pin and the seven C2 counter repairs;
  - the SKILL class cells;
  - SOURCES rows S310–S316.
- Receipts at T: C1 `7b7a17d3` (`L1/c1-tip.txt` pass) and C2 `599c1fa1` (`L1/c2-tip.txt` fail, `GROWS 6/5`).
- Wave w1, dispatched by attempt 1 (13 seats): 6 seats delivered reports, 7 were lost. Residual call r1 (4 seats)
  re-ran the critic, the C2 reviewer, the C1 mutation-tester and the connector.
- Revert `3f300cbd` (attempt 2). Under the lane's Q78, the C2 repair bytes were reverted after T because non-author
  seats found two harms:
  - the re-pinned r87 counter failed at r87's own measured tip;
  - the r93/r94/r95 freeze-integrity gates went PASS → FAIL.
- Integration `0fb7d589`:
  - the lesson (Gate, M1–M8, W-1…W-22);
  - Q79 and Q80 (`corpus/QUALITY.md`, end of file);
  - the SCORECARD round-96 section and the LOG entry (both at end of file);
  - SKILL registry rows `round96-c1-replay` and `round96-standing-battery` (`SKILL.md:701-702`);
  - the w1 and r1 evidence, the landing receipts and the misroot record.
- End receipts `f6033dad`: `.ufo/waves/round-96/L1a2/end-receipts.txt` and `census-end.txt`.
- Planner seat: held by the L1 (the validator rejects `planner`). No planning data-walk was delegated.

## Landed changes

| commit (landed, remote-verified) | change | LOG entry |
|---|---|---|
| `ff6765a662425d65ead297bc0c9fd86f5577be5f` | P0 predictions, capture, census start, BASE receipts | `LOG.md` "Round 96" (order line) |
| `cea469bd8c007b7ff60a22a82df72068f03559eb` | P1 instruments, dry runs | same |
| `e8a80c0e23f8a2b365756b4e971b4210afa3f829` | P1b battery grow leg | same |
| `a3b5732104cb4e36cdefa4a070fc453f88bfaecd` | P2 controls, candidate repair bytes | same |
| `be3ff962c3558ece7843119c1df26fa2cdbd313a` | F frozen claims | same |
| `09717e49ff46fad5b255619d671aaaae52dfc180` | C: receipt, ledger flip, subject re-pin, counter repairs, SKILL cells, S310–S316 | R96-C1 / R96-C2 / Sources bullets |
| `7b7a17d3faea4443aaee341f5fffcf7db8e52c03` | C1 receipt at T, M3 receipts, w1 spec and dispatch | R96-C1, Waves |
| `599c1fa122f35fffde940f4ecabfc0184d704f29` | C2 receipt at T, ledger counts, r91 grow diagnostic | R96-C2 |
| `3f300cbd86546f7938193e3c8188c0f4c4ad2af0` | revert of the seven counters and the `mteb-retrieve` subject cell to BASE bytes | R96-C2 ("Bytes reverted") |
| `0fb7d5894ca88b03191bbecc47dbadb88bd81302` | integration: lesson, Q79/Q80, SCORECARD, LOG, SKILL rows, w1+r1 evidence, landing receipts, misroot | Mistakes, Waves |
| `f6033dadc7ae8694c0b2156a020d671284dff6b2` | end receipts at the landing tip, census end | Sources |

## Before → after measurements

**R96-C1 (coverage).** Counting command:
`python3 plans/round96_c1_replay.py --lane . --rev REV --work DIR --env-venv E --grader-venv G`
- Before:
  - BASE `45740a61`: ledger executed 39 of 88, `file-artifact` 30/76, `serialization-schema` 6/10.
  - Do-nothing (`L1/controls/c1-do-nothing.txt`): all legs fail, rc 1.
  - ExecC1Rerun at BASE and at F: rc 1.
- After, at T `09717e49` (`L1/c1-tip.txt`): `LEGS L1=pass … L9=pass`,
  `TARGET executed_rows=40 member=multi-source-data-merger cells=file-artifact:31,serialization-schema:7 set_contains_base=1 located=1 executed=1 cases=17 legs=68 mismatches=0 defects=0`,
  `PREDICATE R96-C1 pass`, rc 0.
- The same result holds at `3f300cbd` (`L1a2/c1-landing.txt`) and at the landing tip `0fb7d589`
  (`L1a2/end-receipts.txt`).
- Self-verdict: **met.** Non-author evidence:
  - ExecC1Rerun and ReviewerC1 reproduced the result with fresh venvs.
  - Real pytest 8.4.1 gives the same reward as the harness on 17/17 cases.
  - ExecImage ran solve.sh in the real image; the outputs are byte-identical to the venv run.
  - CriticClaimsR rules **verifies-narrowed**. C1 is separable from the C2 bytes (`r1/CriticClaims/c1-noc2.txt`).
    The finding set is incomplete: over-report, a wrong name winner and partial `values` also pass `P,P,P,1`.

**R96-C2 (calibration).** Counting command:
`python3 plans/round96_standing_battery.py --lane . --rev REV --work DIR`
- Before, at P0 `ff6765a6` (`L1/dryrun/battery-base.txt`): `STANDING total=14 green=8 red=6`, `PREDICATE R96-C2 fail`.
- After, at T (`L1/c2-tip.txt`): `STANDING total=14 green=14 red=0`, `BITES checked=12 bitten=12`,
  `GROWS checked=6 tolerant=5`, `PREDICATE R96-C2 fail`, rc 1.
- Self-verdict: **not met.** The frozen predicate fails at T. The kill-rule byte-scope clause is also triggered: the
  `mteb-retrieve` subject cell was landed outside the candidate-bytes table (M5).
- Two non-author runs of the same bytes at T pass 6/6 (`r1/CriticClaims/battery-t.txt`,
  `r1/ReviewerC2/battery-T-at-T.txt`). The predicate is nondeterministic (M2, Q80). The frozen official receipt
  stands and is not re-scored.
- **Harm (non-author):**
  - The repair byte-replaced frozen instruments of closed rounds, so gate v2 at T reports r93/r94/r95 broken
    (`w1/ExecHarm.md` §3). They passed at BASE.
  - The re-pinned r87 counter failed at its own tip `10de494d`.
  - The revert `3f300cbd` restores the bytes and r87 (`L1a2/r87-landing.txt`: pass at T and at `10de494d`). The
    freeze-integrity gates stay `broken:touched-after-freeze=2`, because the history touch is permanent
    (`L1a2/freeze-landing.txt`, rc 1 ×3).
- At the landing tip: `STANDING total=14 green=7 red=7`, `PREDICATE R96-C2 fail` (`L1a2/battery-landing.txt`). These
  are BASE's six reds plus r95, whose L7 pins 39 and turns red when C1 lands; this is growth drift, the `c1-only`
  control state.
- The critic and reviewer both count the premise as 1 genuine mismatch plus 5 cases of growth drift (M6).

**Harm check (other gates).** At BASE, T and the landing tip (`w1/ExecHarm.md` §1, `L1a2/end-receipts.txt`), each of
these is PASS → PASS:
- `grader.py`;
- `PREDICATE R68-A3 pass`;
- `PREDICATE R68-C1 pass`;
- `PREDICATE R91-F1 pass`;
- anchor line `live=0 cells=0`.

The round-79 gate is `DEFECTS n=1` at BASE and at the landing tip (unchanged). Novelty 8, depth 10, operability 10,
freshness 10 and adjacency 9 are held.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
  - Round start: `kengaku ok` (`.ufo/waves/round-96/L1/census-start.txt`).
  - Round end: `kengaku ok`, `rc=0` (`.ufo/waves/round-96/L1a2/census-end.txt`; only W04 cross-scope warnings, as
    before).
  - Row count: `grep -c '^| \?S[0-9]\+ ' corpus/SOURCES.md` 301 → 308.
- Rows added (`corpus/SOURCES.md:326-332`):
  - tier A, admitted / mined: S310 grader, S311 solve.sh, S312 Dockerfile, S313 test.sh, S314 instruction;
  - tier A, rejected: S315 task.toml, with a flip that the non-author ExecImage seat exercised (image pulled, outputs
    byte-identical);
  - tier B, rejected: S316 README.
- ScoutSources re-opened all seven rows live: 7/7 HTTP 200, sha256 = row, quote on its line, word counts equal; upstream
  `main` is identical to the pin.
- Rows touched old → new: none.
- Frontier row advanced: ledger member `multi-source-data-merger` unexecuted → executed (round 96).
- Sourced claim: R96-C1 rests on S310–S314 (opened 2026-11-05; `corpus/lessons/round-96.md` `## Gate`).
- Mistakes mined: `corpus/lessons/round-96.md` `## Mistakes`, M1–M8. Each new criterion is shown able to fail:
  - M1 (byte-replacing a closed round's frozen instruments) → Q79; the gate runs at the landing tip exit 1;
  - M2 (nondeterministic frozen predicate) → Q80; the two committed battery receipts at T disagree.
- Assimilation: none (`merge/kengaku/` held by L0 `kengaku | round-54`). considerthese: none taken (latest file
  `considerthese/2026-11-05.md`).

## Trend verdicts

- **expansion: improved.** The ledger frontier moved 39 → 40 of 88, with two class-cell moves (`L1/ledger-count.txt`).
  Five tier-A rows were added on a member the corpus did not hold. There is new member knowledge: the grader's conflict
  report is checked at one value point (6 wrong-pass states).
- **quality: unchanged.** No admitted `knowledge/` entry was superseded or re-verified.
- **discernment: improved.**
  - S315 and S316 were rejected with flips, and S315's flip was exercised by a non-author seat.
  - Q79 and Q80 are grounded in M1 and M2.
  - The critic's narrowing of C1 and the C2 harm are recorded beside the self-verdicts.
  - The C2 repair was reverted under Q78 rather than kept.
- **Calibration axis (claimed): harmed.** C2 was not met, and its repair leaves a permanent freeze-integrity break on
  r93/r94/r95. Standing reds went 6 → 7 at the landing tip (growth drift from C1). The score line was not edited; the
  closure rules.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:701-702` (registry rows `round96-c1-replay`, `round96-standing-battery` with the nondeterminism warning); class cells `SKILL.md:74,84`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 96" entry (multi-source-data-merger replay, receipt `corpus/evidence/round96/merger-probe.txt`)
- [~] Instructions executable by an agent without oral context — `plans/round-96-claims.md` (each predicate one command; venv staging recipe; controls `.ufo/waves/round-96/L1/controls/README.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-96/r1/ConnectorOverlap.md` CO-1 (no sibling replays TB2 graders; five sibling PROVINCE lines assign LLM eval here)

## Round shape, seats, extras

- Shape: ONE v1 wave `w1` (13 seats, validator-dispatched by attempt 1) plus ONE residual call `r1` (4 seats, an ordinary
  task payload `r1-dispatch.json`). Round total: 17 seats.
- w1 role mix: 4 executor, 2 reviewer, 1 critic, 2 mutation-tester, 1 scout, 1 connector, 1 scribe, 1 sentinel. Attack
  share (reviewer, critic, mutation-tester) is 5/13 = 38 %.
- w1 seats:
  - **Delivered (6):** ExecC1Rerun, ReviewerC1, ExecHarm, ExecImage, ScoutSources, SentinelProbe.
  - **Dead (7)**, lost when the orchestrator session crashed (`w1-results.json` note "orchestrator kernel restarted
    mid-wave"; no report): ExecC2Rerun, ReviewerC2, CriticClaims, MutTesterC1, MutTesterC2, ConnectorOverlap, ScribeLesson.
    Their partial files stay in `w1/` and are not counted.
- r1: CriticClaimsR (critic), ReviewerC2R (reviewer), MutTesterC1R (mutation-tester), ConnectorOverlapR (connector). All
  4 delivered (`r1-results.json`). Attack share 3/4.
- Lost items not re-run: ExecC2Rerun (covered by the two r1 battery runs), MutTesterC2, ScribeLesson (the L1 drafted the
  lesson).
- Every seat prompt led with `/skill:godspeed` plus the verbatim directive bytes.
- Misroot sweep (`.ufo/waves/round-96/L1a2/misroot-sweep.txt`):
  - Fleet-root `.pytest_cache` (23:15, its nodeids name the round-96 grader; ConnectorOverlapR CO-5) was copied to
    `L1a2/misroot/pytest_cache` and checked identical with `diff -r`. The fleet copy was removed. The copy is self-ignored,
    so the sha256 list is recorded in the sweep file.
  - `w4lines.txt` (16:57, before launch) and `.scratch/*` were left untouched. Recorded as lesson M7.
- Open L0 questions: none new. The existing kengaku L0s (rounds 54, 90–92) were routed around.
- Tool installs:
  - L1: none (scratch uv venvs only).
  - ExecImage: `docker pull alexgshaw/multi-source-data-merger:20251031` (official tag, digest `sha256:8b327820…e666e`),
    removed afterwards with `docker rmi`.
  - ReviewerC1, ExecC1Rerun, SentinelProbe, CriticClaimsR: none installed (pre-existing uv, bwrap, pytest; scratch venvs only).
  - No pacman, no sysctl changes.
- Scratch: `/fast/scratch/hyaku/kengaku-r96` removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
