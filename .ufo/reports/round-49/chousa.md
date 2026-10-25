# chousa — round 49

## Work performed

Declared claims, frozen at lane commit `fe740e7838b338d17fec9338c909557e6e7fed7d` (`corpus/evidence/round49/claims.md`) after their do-nothing controls were scored:
**R49-C1 operability** (the lowest scored axis, 3/10; a capability acquisition): `tools/assimilate-rows.py`, the addendum-section-10 package adopter.
**R49-C2 depth** (sourced; the assimilation theme): the theme "a citation index's data is a derived artefact" adopted by document as two lane entries.

- C1 tool landed at `65940928cc9332b386bcbca92571451cc4374cbe`. W1 `ReviewToolCode` found defects, fixed at `4ce61fc59e30b9215514841fe658e96cc998d138`: tab headings, calendar-invalid dates and non-UTF-8 input. The do-nothing copy control fails every leg (`corpus/evidence/round49/controls/c1-before.txt`).
- C2 adoption landed at `1254ab262b2fbc199923345d389f85d0debbef6e`, then was narrowed after W2 at `763b33704643da8d921ada641f11aa139adbcb64`:
  - Two entries were added: `corpus/knowledge/aggregator-vs-source-r36.md` and `corpus/knowledge/citation-count-semantics-r37.md`.
  - Eight rows were added: `corpus/SOURCES.md` S096–S103.
  - There are 31 located quotes (`corpus/evidence/round49/spans.tsv`). The two OLE `.doc` captures are read as the UTF-16LE text of their raw files.
  - The staged NCPSSD homepage row was refused.
  - The Gate is in `chousa-shokunin/corpus/lessons/round-49.md` under `## Gate`. It carries the admit and refuse table, five register re-check verdicts and the renumber map.
- Disclosed post-freeze change: `build-spans.py` now clips raw-form span context at a carriage return, and one S100 quote was replaced (`corpus/evidence/round49/claims-erratum.md`). Before the change, `CAPTURE_BOUND` was 21/28. W2 `CritErratum` reproduced the 21/28 as a text-mode read artefact on spans that were already exact slices, and ruled that **C2 stands**. It also corrected a false clause in the erratum.
- Counter limits found by W1, recorded but not repaired because the counters are frozen:
  - A replay of the tool's outputs passes `c1-count.py` (`CritForgeC1`).
  - A hollow quote passes the structural C2 legs (`CritForgeC2`).

  QUALITY 72 and `quote-substance-check.py` were added in response; this round's manifest passes it with `FAILURES=0`.
- Round-48 routed defects:
  - The a05 propagations are corrected in the round-49 lesson (`a05-check.py` exit 1 → 0).
  - The P2 false-negative class is documented as a QUALITY 69 note.
  - QUALITY 69's pointer to a nonexistent Mistake 4 is fixed.
  - The inherited QUALITY 69 line was verified true (W1 `ExecQualityWindows`) and landed.
  - The three R40/R41 JSON leftovers were reverted. Their pre-revert diffs are in `.ufo/waves/round-49/inherited/`.

## Landed changes

| commit | change | LOG |
|---|---|---|
| `fe740e78` | Frozen claims, counters, controls, span builder, inherited diffs | `LOG.md` Round 49 |
| `65940928` | `tools/assimilate-rows.py` | same |
| `1254ab26` | Two entries, S096–S103, lesson, QUALITY 69 note / 71 / 72, two SKILL Gates rows, checks, erratum | same |
| `4ce61fc5` | Tool fixes from W1; SKILL row text | same |
| `87e93353` | First after-measurement | same |
| `763b3370` | W2 narrowing, LOG/SCORECARD entries, wave evidence | same |
| `5275c892273242b5be989336f5d44ce8cbf671f9` | Final after-measurement and wave evidence (lane tip; `git ls-remote origin refs/heads/master` prints this hash) | same |

## Before → after measurements

All measured at lane tip `5275c892` (`corpus/evidence/round49/measure-after.txt`; tracked tree equals the commit).

| claim | before | after | command | verdict |
|---|---|---|---|---|
| C1 operability | `TOOL=absent C1=FAIL` exit 1. Copy control: `SETS_PASS=0/3`, GUARD and PIPE FAIL | `SETS_PASS=3/3`, GUARD PASS, PIPE PASS, `C1=PASS` exit 0. Copy control still `C1=FAIL` exit 1 | `python3 corpus/evidence/round49/c1-count.py` | **Improved narrowly.** Conformance on fixed inputs; the replay limit is named. |
| C2 depth | `ENTRIES=0/2 BOUND=0/9 C2=FAIL` exit 1. Staged-copy control: `REF_ID_UNBOUND=11 C2=FAIL` | `BOUND=8/9 REFUSED=1 QUOTE_ROWS=31 CAPTURE_BOUND=31/31 ANCHOR_BOUND=8/8 INFERENCE_GROUNDED=2/2 QUARANTINE_VERDICTS=5/5 C2=PASS` exit 0 (also `--lane-only`) | `python3 corpus/evidence/round49/c2-count.py` | **Improved**, subject to the closure's ruling on the disclosed change. |

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Round start:** exit 0, `ok`, five pre-existing W04 warnings (S051, S053, S073, S074, S075).
- **Round end:** exit 0, `ok`, the same five W04 warnings (`measure-after.txt`).
- **Rows:** 95 → 103 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- **Tiers:** A 89→92, B 1→6, C 5→5.
- **Statuses:** mined 71→79, queued 19, rejected 5.
- **Added by tier:** A S096–S098; B S099–S103.
- **Rows touched old→new:** none.
- **Frontier:** the coverage map gains two entries on ground the lane did not hold: index derivation, link lag, the resolution ladder and CNKI counter rules.

**Assimilation:** theme "derived index data" from `merge/chousa/`.
- Section-10 collision check: 14 collisions (S082–S095). The guard was proven on an indented-row fixture.
- Renumber by document: staged S087/S088/S089/S092/S100–S103 → lane S096–S103.
- One admit-later and one reject, plus the NCPSSD refusal.

**considerthese:** `considerthese/2026-10-25.md:55-56` "Report a capture-age line" was mined into QUALITY 71 (`capture-age-check.py`; it fails on the round-48 report).

**Freshness:** the newest capture the lane may read is 2026-10-24 23:26 -03; this round's captures are from 2026-10-23. Sourced claim: C2 rests on S096–S103, all opened this round.

**Mined mistakes:** four, in the lesson's `## Mistakes`: the a05 charity propagation, the hollow-quote counter, the replay-passes counter, and the dangling criterion pointer.

## Trend verdicts

- **expansion — improved.** Two entries on new coverage ground; eight rows on documents not previously held (W1 `CritTheme`, `ConnSiblings`). The aggregator conclusion itself was already held and earns no credit.
- **quality — improved.** The adopted entries passed W2 claim-by-claim attacks and were narrowed on six overclaims each (`w2/CritEntryAgg.md`, `CritEntryCCS.md`). The a05 correction and QUALITY 71/72 checks were each shown able to fail.
- **discernment — unchanged pending closure.** The lane-side admit and refuse decisions are recorded. All seats were dispatched by this lane, so none is a non-author. The closure should re-open S100 (UTF-16LE) and the refused NCPSSD row.

## SHONEN

- [~] Decision tables, error patterns, cited sources — `chousa-shokunin/SKILL.md` Gates rows `assimilate-rows` and `chousa round-49 counters and checks`; `corpus/QUALITY.md` 71–72.
- [~] End-to-end task executed and logged — `LOG.md` Round 49; `corpus/evidence/round49/measure-after.txt`.
- [~] Instructions executable without oral context — `tools/assimilate-rows.py` docstring; `corpus/evidence/round49/c1-count.py`.
- [~] Province fit — `PROVINCE.md`; `.ufo/waves/round-49/w1/ReviewProvince.md`, `ConnSiblings.md` (no overlap).

## Round shape, stale lane, tooling, L0

**Shape:** two v1 waves via the inline handoff, 40 + 35 = 75 seats; no residual call.
- **W1 (40):** scribe 17, executor 9, reviewer 4, critic 4, mutation-tester 2, connector 2, scout 2.
- **W2 (35):** executor 16, scribe 5, critic 4, mutation-tester 3, reviewer 3, connector 2, simplifier 1, scout 1.
- The L1 held the planner seat; the W2 `ScoutPlanned` item carried the data-walk.

**Conformance defect:** this report was filed before WAVE-DONE arrived for either wave, because the run reached its budget stop.
- At filing, W1 had 39/40 reports (`ScoutInherited` outstanding) and W2 had 27/35 (MutA05, MutSubstance, ReviewQuality, ExecReplayC1, ScribeScorecard, ScribeTrends, ScribeShonen and ScoutPlanned outstanding).
- These seats were live, not dead; their late reports remain uncommitted wave evidence.

**Incident:** host `/tmp` filled to 0 bytes mid-round. My one partial archive extraction there was removed; L1 and W2 scratch moved to `/dev/shm`.

**Misroot sweep:** `git status --porcelain` on the fleet root shows only `.ufo/waves/round-30/wave1/ScribeLesson.md`. It is another lane's round-30 seat report, so I did not touch it.

**Stale-lane:** launched 16:50 -03; progressing with lane commits throughout.

**Tool installs:** none. **L0:** `8d77e6c1` is still open; no new question was appended.
