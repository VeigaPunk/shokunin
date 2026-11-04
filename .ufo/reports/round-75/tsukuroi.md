# tsukuroi — round 75 report (hyaku run 15, lane round 75)

Lane: `tsukuroi-shokunin` · declaration `1e2bb29c` · base `a21302a4` · measured revision
`bd0acc44` · lane tip/remote `bd0acc444cd6c82823602ed7a49bd1ef11360d2d` · one v1 wave, 12 seats.

**Declared claims.** C1 on **depth** (the lowest non-retired axis, tied at 8 with adjacency): a new
sourced entry states the systemd v262 job-transaction plane this lane never held. C2 on **freshness**
(9): the four round-74 closure routed defects close in committed bytes. Both were frozen, with
controls and frozen instruments, in `SCORECARD.md` section *Round 75 — declaration* at `1e2bb29c`
before any seat or note existed.

## Work performed

- **C1 — the job-transaction plane (depth).** `corpus/knowledge/systemd-job-transaction-plane-r75.md`
  lands six rule rows JT1-JT6 with pinned v262 snapshots: merge algebra with the immediate-collapse
  qualification (JT1), the state-dependent redundancy predicate (JT2), `JOB_TRY_RESTART`'s exclusion
  from any transaction (JT3), the complete thirteen-member `JobResult` outcome set (JT4), the ten
  labelled `transaction_activate` stages (JT5), and the five per-class pull-in flags with restart
  propagated as a collapsed try-restart inside `PROPAGATE_STOP` plus the separate graceful-stop branch
  that may enqueue a direct restart (JT6). Counting command `python3 tools/count-jt-rows-r75.py
  --revision <REV>` reads `JT_ROWS=6 JT_VERIFIED=6 JT_SOURCES=3 JT_SNAPSHOTS=3 JT_MALFORMED=0 met=1`
  rc 0 at `bd0acc44`; at the base it reads `JT_MAP absent` rc 128
  (`.ufo/waves/round-75/after/measure-final.txt`).
- **C1 sources.** S314 (`src/core/transaction.c`), S315 (`src/core/job.c`), S316 (`src/core/job.h`) at
  tag v262, plus S317, the measured refusal of the `systemctl(1)` manual (mined 3 / rejected 1).
  Evidence: `corpus/SOURCES.md:325-328` (rows S314-S317); Gate table in `corpus/lessons/round-75.md`.
- **C1 reviewer falsification, in-round.** R1Reviewer held JT1, JT2, JT3 and JT5, refused JT4 and JT6
  as drafted and supplied the corrected sentences that landed (`.ufo/waves/round-75/w1/R1Reviewer.md`).
  S1Scout independently re-fetched all three snapshots by a second route (per-file HTTP and the
  codeload tarball, byte-identical) and found the same content gaps plus the `UNIT_REFRESHING`
  omission, now an appended note erratum. K1Critic's D2 found JT5's compressed enumeration; the
  note's second erratum enumerates the ten labels and names the upstream "Eights step" typo.
- **C1 not verified as declared.** The frozen sentence's "propagating restart only as try-restart" is
  over-broad: `transaction.c:1220-1247` and the helper at `:999-1027` may enqueue a direct
  `JOB_RESTART`. Erratum `R75-DECL-PROPAGATE-SCOPE` in `SCORECARD.md`; no predicate was widened and no
  depth uplift is claimed (QUALITY 106).
- **C2 — the four r74 routed repairs (freshness).** `corpus/lessons/round-74.md` now names
  `R74-DEATH-RECEIPT-MISSING` (SC3Index 429/`RESOURCE_EXHAUSTED`, no receipt committed) and
  `R74-REPORT-WORDING` (the accurate "no review-accepted drafts" plus the 27552-byte
  `w1/SC3Index/report.md`); `.ufo/waves/round-74/w1/E3HostProbe/receipt-g-landing.txt` carries
  `R74-SWEEP-RESIDUE` quoting both the fabricated and the real OID; `SCORECARD.md` carries
  `## Round 75 — axes table restated` with six axis rows, each with a real counting command,
  superseding the round-65 table (`ROUTED_STALE=0 ROUTED_OK=4/4` rc 0 at `bd0acc44` vs
  `ROUTED_STALE=4 ROUTED_OK=0/4` rc 1 at base).
- **Docs.** `SKILL.md` gains a five-symptom job-transaction diagnosis table of read-only checks;
  `PROVINCE.md` records the Core reading and the remaining Frontier; `corpus/README.md` indexes the
  note; both new tools carry operative registry rows in the round-71 table
  (`check-registry-coverage.py --revision bd0acc44` → 107 registered rows, 6 pre-existing missing
  rows for the r72-r74 tools, exit 0).
- **Frontier step.** `corpus/lessons/round-75.md` carries the Gate (four sources, located quotes,
  access date), the search log, six mined mistakes and the attack ledger. QUALITY 108 adopts the
  `considerthese/2026-10-26.md` "Cross-note correction propagation map" proposal and the lesson
  exercises it on three corrected propositions (`.ufo/waves/round-75/before/propagation-map.txt`).
- **Wave.** One v1 wave, twelve seats, roles scout 1 / executor 3 / scribe 3 / connector 1 /
  reviewer 2 / critic 1 / mutation-tester 1; strict attack 4/12 = 33 %; connector 1; the L1 held the
  planner seat; residual 0. `w1-results.json` reports twelve nonempty finals, **no dead seat**, and no
  seat replaced.

## Landed changes

Every line below is carried by the `LOG.md` entry `## Round 75 (2026-11-04) …` and by the commit that
holds it.

| Change | Commit |
|---|---|
| Declaration (two claims, controls, frozen instruments, three v262 snapshots) | `1e2bb29c` |
| Note `corpus/knowledge/systemd-job-transaction-plane-r75.md`; registry S314-S317; SKILL/PROVINCE/README appends; QUALITY 108; lesson; the four C2 repairs; wave spec/dispatch/seat reports | `c15fe829` |
| `LOG.md` round entry; note erratum (JT2 `UNIT_REFRESHING`); lesson gap row | `71ab09f4` |
| Wave results, `after/` receipts, JT5 label erratum, K1/S1 findings folded in | `e5f5ca9e` |
| Final measurement receipt `after/measure-final.txt` | `bd0acc44` |

## Before → after measurements

| Claim | Axis | Counting command | Before (base `a21302a4`) | After (`bd0acc44`) | Verdict |
|---|---|---|---|---|---|
| C1 | depth 8 | `python3 tools/count-jt-rows-r75.py --revision <REV>` | `JT_MAP absent`, exit 128 | `JT_ROWS=6 JT_VERIFIED=6 JT_SOURCES=3 JT_SNAPSHOTS=3 JT_MALFORMED=0 met=1`, exit 0 | **not verified as declared** — six true, reviewed rows and the mechanical target, but the frozen sentence's "only as try-restart" is over-broad (erratum `R75-DECL-PROPAGATE-SCOPE`); depth 8 → 8, no uplift |
| C2 | freshness 9 | `python3 tools/check-r74-routed-r75.py --revision <REV>` | `ROUTED_STALE=4 ROUTED_OK=0/4`, exit 1 | `ROUTED_STALE=0 ROUTED_OK=4/4`, exit 0 | **verified**; freshness 9 → 9, no uplift claimed |

Supporting counts at both revisions: registry rows 313 → 317; knowledge notes 92 → 93; lesson files
124 → 125. Receipts: `.ufo/waves/round-75/before/absence-controls.txt`,
`after/measure-final.txt`. Both instruments are unchanged from their frozen digests
(`5e87238c…` counter, `4b5c801c…` checker, both 13-case selftests), so each pair is same-instrument
evidence.

## Sources & frontier

`SOURCES.md` rows **313 → 317** (`git show <REV>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]+ *\|'`).
Rows added by tier: **tier A 4** (three mined code snapshots, one rejected docs page), tier B 0,
tier C 0. Rows touched old→new: none — no pre-existing row's `status`, `recheck` or `used-by` changed
this round. Frontier rows advanced: the systemd Core reading moved from unit-fragment resolution to
job transactions; the Frontier list now names an observed transaction, a queued job, a live merge and
host-build line numbers as unmeasured.

Census (the frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
tsukuroi`): round start **exit 0** (`.ufo/waves/round-75/before/census-start.txt`, W04 duplicate-URL
warnings only), round end **exit 0** (`after/measure-final.txt`).

**Assimilation: none.** The `corpus-expansion-1` package `merge/tsukuroi/` was checked read-only and
114 of its 147 staged S-ids collide with the current registry
(`.ufo/waves/round-75/assimilation/{reg-ids,staged-ids,collisions}`); that is the mass-id-drift case
the contract routes to an L0 question instead of an append, and nothing was adopted. The L0 line is
`tsukuroi | round-75 | corpus-expansion-1 …` in `.ufo/l0-questions.md`.

## Trend verdicts

- **expansion: improved.** One new sourced entry on verified-new ground (held-ground sweep 0 lines at
  base, `before/held-ground.txt`), three mined tier-A snapshots plus one measured refusal, registry
  313 → 317 and notes 92 → 93, census exit 0.
- **quality: improved.** Two frozen instruments landed with 13-case hermetic selftests and no answer
  key; the in-wave attacks (R1Reviewer, S1Scout, K1Critic, R2Reviewer, M1Mutation) found four real
  defects before or at landing — the over-broad C1 clause, JT4's short enumerations, JT5's compressed
  labels and JT2's macro expansion — and each is corrected append-only with a named carrier, so no
  admitted artifact is left failing its own re-check. Named limits are recorded, not smoothed: the C1
  counter is polarity-blind (K1 D1/D2, E1Counter's scripted non-reader), and eleven R2Reviewer
  fixtures pass all four C2 items without a real repair.
- **discernment: improved.** The outside check of round 74 (four routed defects) is closed with
  committed bytes and a re-runnable checker; the round refused its own C1 claim rather than let a
  lexical PASS stand for truth; and QUALITY 108 makes the correction-propagation sweep a standing
  obligation, exercised here on three propositions and two carriers the round-74 record never named.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` round-75 diagnosis table (five symptoms, read-only checks, JT ids) plus the carried
  round-74 table; author-side only, no named non-author verifier for this box this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the wave's
  read-only host probe (`.ufo/waves/round-75/w1/E3HostProbe/01-surface.txt` … `05-failure-reads.txt`)
  and the `LOG.md` round-75 entry; the probe observed no transaction, which the note states.
- [~] Instructions executable by an agent without oral context — evidence: the note plus the SKILL
  table and the counter's own docstring were executed by twelve independent seats; the whole-SKILL
  no-oral-context retest is still the open round-60 L0 item.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` round-75 entry
  restates ADJ-04 (mori) and ADJ-06 (kaidoku/revenger) boundaries; C1Connector found no sibling
  overlap across 20 sibling repos (`w1/C1Connector.md`); no `[x]` is claimed without a named
  non-author verifier.

## Notes, holds and tooling

- **Stale-lane:** none — respawn-per-round driver; the next dispatch is round 76. No other mission of
  this lane is open.
- **Open L0:** `tsukuroi | round-75 | corpus-expansion-1 … id drift` (adoption paused, routed around).
- **Tool installs:** none this round. Pacman stayed paused; no package or service transaction ran.
- **Process defects disclosed:** a seat written binding file first (QUALITY 96) and no seat returned
  an empty final. R2Reviewer and K1Critic each ran their attack batteries against the frozen
  instruments without editing them; M1Mutation's survivor list (C1 4 of 7, C2 3 of 5) is carried as
  instrument-coverage debt in the lesson, not as a claim failure.
