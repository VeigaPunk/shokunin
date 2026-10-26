# mori — round 50 report (attempt 2, L1 MoriR50a2)

Lane `mori-shokunin`, branch `master`. Entering tip `7197160b`; freeze `950e99be` (attempt 1); orchestrator salvage
`9b8562a3`; data `487941b9`; integration `bae8656e`; final lane tip `756d5b1a5679b131203663cbbbd2c4d96f7143ee`
(receipts commit; `git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (frozen by attempt 1 at `950e99be`, `.ufo/waves/round-50/contract.md`; run unchanged per §10 "frozen and
resumed rounds"): **C1 — calibration** (the self-assessment: `SCORECARD.md` `## Axes` Last change/Evidence cells and
`SHONEN.md` tally pins agree with the fleet `MANIFEST.json` and the instruments); **C2 — depth** (FR1: the memcg OOM
report block and `memory.stat`, entry `corpus/knowledge/oom-memcg-stat-r50.md`). Both work a lowest-scoring axis
(depth, freshness, calibration tied at 5). No exploratory claim.

- Re-verified attempt-1 state before reuse: frozen bytes `sha256sum -c .ufo/waves/round-50/evidence/freeze-sha256.txt`
  all OK; both counters at the salvage `9b8562a3` (C1 `mismatches=6`, C2 unmet); selftest receipts re-run in a
  `git archive` — identical but for the header line; live sources re-fetched 2026-10-26T09:26 and sha256-equal to the
  copies (`.ufo/waves/round-50/assimilation/a2/live-sha-L1.txt`).
- C1 data: four Axes rows + correction paragraph (`SCORECARD.md:10-14,21-29`), SHONEN pins `(114/114)`, `(17/17)`
  (`SHONEN.md:7`) — landed `487941b9`.
- C2 data: rows S489–S491 appended after a scratch mirror census (`assimilation/a2/mirror-validate.txt`, rc 0, 22 W04)
  — landed `487941b9`.
- Wave `a2w1`: 64 seats (policy v2, validated rc 0) attacked the landed data and drafted the frontier step; 64/64
  reports in `.ufo/waves/round-50/a2w1/`, results `a2w1-results.json`.
- Integration: six entry overclaims corrected (lesson M4), S490/S491 anchors widened, SHONEN pointers fixed, SCORECARD
  correction wording made exact; lesson `corpus/lessons/round-50.md`; QUALITY 134–136; README/SKILL Round50; LOG
  round 50 — landed `bae8656e`.
- considerthese `2026-10-26.md` suggestion 3: rounds 47–49 frozen counters re-executed at their scored revisions —
  all AGREE (one transient r47 divergence, `conform.py` setup error under load, reproduced on rerun)
  (`a2w1/Mo50bExecReexecR4{7,8,9}.md`; lesson Gate; QUALITY 136).
- Routed defect 4: lane `.scratch/` ignored residue deleted (`evidence/a2-scratch-deletion.txt`).
- Planner seat: held by the L1 (the validator rejects `planner`).

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `487941b9395e89678af0053cc443cdb49cdee6e3` | C1 Axes cells + SHONEN pins; C2 rows S489–S491; assimilation scratch `a2/` | Round 50 C1/C2 bullets |
| `4548a34dc8b4072abaa4335c1f54a9efcfcc314a` | wave a2w1 spec/dispatch, receipts `a2-c{1,2}-at-data.txt` | Round 50 header |
| `bae8656ea74a8ea3a4f2cf784e15cbeb91d9ad7d` | wave integration (entry, rows, SHONEN, SCORECARD, lesson, QUALITY 134–136, README, SKILL, LOG), 64 reports, scratch-deletion receipt | Round 50 (`LOG.md:2732-2763`) |
| `756d5b1a5679b131203663cbbbd2c4d96f7143ee` | receipts at `bae8656e` (`a2-c{1,2}-at-landed.txt`, `census-end.txt`, `a2-pin-check-at-landed.txt`: `PIN_CHECK=met tally_pins=35 … mismatches=0`, exit 0 — no operability harm, the two new SKILL gate rows match) | Round 50 C1/C2 bullets |

Inherited from attempt 1 (committed by the orchestrator salvage `9b8562a3`, not authored by this L1): the entry draft,
`w1/` reports (5), `w1-*` spec/dispatch, `w1.ready{,.dispatched}`, selftest receipts, and the late round-49 report
`Mo49ExecCounterTiming.md`. Reused after re-verification: entry draft, receipts, source copies, the five w1 reports.
Discarded: nothing; 35 attempt-1 seats left no report (outcome unknown).

## Before → after measurements

- **C1** — `python3 .ufo/waves/round-50/count-c1.py R`. Before (`7197160b`): `C1=unmet items=8 axes=6 pins=2 boxes=4
  mismatches=6 errors=0 hidden=0 manifest=a94551c5bc8d … failed=mismatch` (`evidence/control-c1-do-nothing.txt`).
  After (`bae8656e`): `C1=met items=8 axes=6 pins=2 boxes=4 mismatches=0 errors=0 hidden=0 manifest=a94551c5bc8d`
  exit 0 (`evidence/a2-c1-at-landed.txt`; also met at `487941b9`, `a2-c1-at-data.txt`). Controls (before data): all
  seven non-witness controls unmet. Selftest `C1_SELFTEST pass=34 fail=0`.
- **C2** — `python3 .ufo/waves/round-50/count-c2.py R`. Before (`7197160b`): `C2=unmet … failed=entry_absent,pins`
  (`evidence/control-c2-donothing-git.txt`). After (`bae8656e`): `C2=met claims=22 located=22 quote_missing=0
  bad_rows=0 sources=3 source_rows=ok pins=ok provenance=ok` exit 0 (`evidence/a2-c2-at-landed.txt`). Staged-entry
  controls unmet. Selftest `C2_SELFTEST pass=31 fail=0`.
- Named limits (frozen counters; wave findings, lesson `## Wave a2w1 — integrated findings`): C1 verdict-word
  substring, second `## Axes`, Score column unread, `admitted`-filter arm vacuous; C2 substring location, prose
  unread, entailment unchecked (six overclaims met the counter — M4).

## Sources & frontier

- Census command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0, 21 W04
  (`evidence/census-start.txt`); end rc 0, 22 W04 (`evidence/census-end.txt`; the new W04 is S491, same URL as S003/S476
  at a different scope).
- Rows: `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md` 261 → 264; added by tier: A 3 (S489 docs, S490 code, S491
  code), all `mined`, opened 2026-10-26, Gate quotes in `corpus/lessons/round-50.md`. Rows touched old→new: S490 anchor
  and teaches, S491 anchor (in-round rows only, logged in the Gate). Frontier advanced: FR1 (memcg report block).
- Sourced claim: C2 rests on S489–S491. Mistakes mined: M1–M4 (lesson `## Mistakes`).
- Assimilation: theme FR1 from `merge/mori/` — admit 1 rewritten entry (staged S533 → S489 by document), reject
  S534/S539 own-work rows and the r46 tmpfs hypothesis (flips in Gate). Collision check: 261 registry ids, 136 staged,
  18 collisions S471–S488 (none adopted), guard proof `assimilation/guard-proof/`, renumber map S533→S489; quarantine
  slice S244/S262/S268 — round-48 verdicts stand, none cited.
- considerthese: `considerthese/2026-10-26.md` suggestion 3 (lesson Gate, QUALITY 136).

## Trend verdicts

- **expansion: improved** — one entry on FR1 ground the lane did not hold (sweep `evidence/sweep-memcg-stat.txt`: 0
  hits for `memory.stat`, `Memory cgroup stats`, `failcnt`), three mined tier-A rows.
- **quality: improved** — the self-assessment now matches the fleet record and the instruments (C1 `mismatches=6` →
  0), and three prior closures' evidence-verified counters were re-executed and agree.
- **discernment: unprovable-but-better** — the wave's six entailment overclaims were caught and corrected, Gate keeps
  admit/reject with flips; no non-author has judged it yet (the closure owns that).

## SHONEN

[~] SKILL.md decision tables, error patterns, checklists with sources — `SKILL.md:1018-1067` (Round50, memcg OOM block decision row); `corpus/QUALITY.md:1176-1250`
[~] an end-to-end domain task executed and logged — `LOG.md:2732-2763` (Round 50); `.ufo/waves/round-50/evidence/a2-c2-at-landed.txt`
[~] instructions executable without oral context — `python3 tools/mori-pin-check.py --selftest` (114/114); `python3 tools/mori-unlanded-check.py --selftest` (17/17); receipts `.ufo/waves/round-50/evidence/selftests/`
[~] no cross-domain bleed — `corpus/knowledge/oom-memcg-stat-r50.md` Boundaries (limit configuration is tsukuroi's); `a2w1/Mo50bConnSiblings.md` (tsukuroi holds the same `oom_kill.c` bytes at another scope: adjoins)

## Extras and defects

- Round shape: attempt 1 dispatched one v1 wave `w1` of 40 seats (5 reports; 35 outcomes unknown — no results file);
  attempt 2 dispatched one v2 wave `a2w1` of 64 seats (executor 17, reviewer 15, critic 9, scribe 8, connector 4,
  mutation-tester 3, scout 3, sentinel 2, simplifier 2, revenger 1; m_flash roles 39/64, attack 27/64). Attempt-2
  total 64; 104 dispatched across both attempts, above the 100 ceiling. Dead seats in a2w1: 0 (64/64 reports; the
  results file records no per-seat status). No residual call. The contract's "two v1 waves" shape was not run (data
  landed first, one wave attacked it).
- Round-49 routed defects: 1 author date — checked below; 2 receipts committed; 3 correction entry (lesson, LOG); 4
  `.scratch` ignored entries 166 → 0, 25G → 29M (225 tracked files kept), round-40 conform dirs 0; producers
  (`tools/mori-pin-check.py:884-887`, `round-40/conform.py:69`) routed to round 51; 5 round-49 seats were late, not
  dead; 6 `variants` = runs − `real`; 7 K4 closed for SHONEN only, handle rule not met; 8 D-g wording corrected.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no mori-authored untracked file at the
  fleet root (only `.ufo/state/` driver files, untouched). Seat scratch dirs: all removed.
- Stale-lane: respawn-per-round driver; no other mori mission open. Tool installs: none (L1 and seats). Open L0
  questions: none.
- Author date check (round-49 D-a): lane tip `756d5b1a` committed `2026-10-26T10:54:21-03:00`; this report was
  written after it and is filed by one `fleet-commit.sh` call; check `git -C /home/vgpnk/Projects/shokunin log -1
  --format=%aI -- .ufo/reports/round-50/mori.md` ≥ that time.
