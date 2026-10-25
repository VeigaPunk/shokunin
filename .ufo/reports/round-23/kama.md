# kama — round 23 report

## Work performed

Declared claim (one): **C1 calibration 7 → 7 (narrow)**, the lowest assigned
non-retired axis (calibration 7, operability 8). Sourced on S089–S101. On the
graded rows of `tests/report-audit/repo-state-grid.py`, repository-local git
state in the audited lane and fleet no longer crashes
`tools/report-landing-audit.py` into exit 1, flips its verdict, hangs it, or
runs a repository-configured program. This is narrow D4 movement, not
untrusted-repository safety; KQ32 stays in force.

Coordinator history: the first L1 (CloseKama22) ran both waves and landed
three commits; it died with the host session (SIGHUP 13:10:51 -03) while
running the mutant population over its uncommitted falsify-wave integration.
KamaR23-2 (this replacement) reconstructed state from the lane, wave
receipts and the dead transcript, re-verified the inheritance, finished the
integration and landed it.

- Inherited, re-verified, landed: uncommitted auditor/grid/mutant edits (git
  timeout F30, filter-only promisor F27, shallow fleet F28, broken branch
  F29, contract kind for F17/F21/F23/F24, controls C09–C12, mutants M26–M31,
  kill only on grid exit 1) — `e876b953e9da28d2dffd29c923052bc626148c27`.
- Inherited, rewritten to the measured state, landed: SKILL.md round-23
  registry section, KQ34 (replaced by ConnQualityRules' stricter draft),
  README frontier disposition, knowledge §Round-23 (traceback count 8 → 9;
  sources corrected) — `0df800e896f6bce285a81e794ad4ae1d1e6c3a71`.
- Discarded: nothing. Not reused: the falsify drafts for SCORECARD/LOG (new
  blocks written from final measurements).
- New by the replacement: info/grafts content check ignoring blank and `#`
  lines (S101; control C13; mutant M32) after re-running CritRefusalScope's
  probe on the inherited tree showed comment-only/empty grafts still refused
  (`.ufo/waves/round-23/final/refusal-results.json`); grid timeout now kills
  the auditor's whole session (56 orphaned FIFO-blocked git processes from
  this round were killed); mutant runner lists contract-row failures.
- Frontier step: SOURCES 88 → 101; S095 rejected and superseded; mistakes
  M4–M7 mined (`corpus/lessons/round-23.md`).
- Misroot sweep: ScribeLogEntry's two files moved byte-exact from the fleet
  root into `.ufo/waves/round-23/falsify/` (`cmp` equal, fleet copies
  removed; lesson M5).

## Landed changes

Each change is tied to `LOG.md` §round 23 — repository-local git state in
the report landing audit.

- `e0f04346fea0690228f3d3be539559316da4f703` — neutralize repository-local git state; fault grid and isolation mutants (CloseKama22).
- `34b23761bd20596b3a9f4c2857ed2ff5fcea85f5` — NUL-delimited log records, catch-all refusal, promisor/sha256/top-level refusals; grid F22–F26 and mutants (CloseKama22).
- `245a37f69628c2c6bb29bbf17897d8fb5946c857` — sources S089–S095, round-23 lesson (CloseKama22).
- `e876b953e9da28d2dffd29c923052bc626148c27` — falsify-wave integration and grafts/session-kill/contract-attribution fixes (KamaR23-2).
- `0df800e896f6bce285a81e794ad4ae1d1e6c3a71` — SOURCES S096–S101, lesson append, KQ34, SKILL, README, knowledge, SCORECARD, LOG, wave evidence (KamaR23-2).

Lane tip after landing: `0df800e896f6bce285a81e794ad4ae1d1e6c3a71` (ahead 0).

## Before → after measurements

Measured in a clean clone of `e876b953e9da28d2dffd29c923052bc626148c27`
(git 2.56.0, Python 3.14.8); frozen arm = `4fe9339f8fc3a4a4a479d9c938a850da12f1124d:tools/report-landing-audit.py`.

| C1 component | Before → after | Counting command |
|---|---|---|
| Fault rows met | 0/26 → 26/26 | `python3 tests/report-audit/repo-state-grid.py --arm both --json` (exit 1, frozen red by design) |
| Tracebacks / executed programs / timeouts | 9/3/2 → 0/0/0 | same |
| Contract rows | 1/4 → 4/4 | same |
| Controls | 13/13 → 13/13 | same |
| Isolation mutants | 22/24 killed (`245a37f6`, any nonzero exit counted) → 30/31 killed on grid exit 1, each with failed rows listed; survivor M20 (defensive-only, reported) | `python3 tests/report-audit/isolation-mutants.py --json` |
| Selftest (no harm) | 50/50 → 50/50 | `python3 tools/report-landing-audit.py --selftest` |
| Historical ledger (no harm) | rounds 10–21 and 10–22, with and without errata: current = frozen byte-for-byte (exit 0/1; 13 reports, 54 required, 9 raw defects, 9 corrected) | recipe `nh-history-parity` (`.ufo/waves/round-23/recipe.json`) exit 0 |
| Over-refusal probe (11 complete repos) | inherited tree 2 refusals (empty/comment grafts) → 0 | `.ufo/waves/round-23/final/refusal-probe.py` |

Evidence: `.ufo/waves/round-23/final/` (grid, mutants, selftest, ledger,
parity, citation, install-io, source-witness outputs).

Verdict (author): C1 **verified on the graded population**, calibration
7 → 7. Not admitted by me; a non-author closure decides. Harm disclosure
under the no-trade rule: operability is **traded** on two declared states —
a complete blobless partial clone (T01) and a paired promisor pack without
promisor config (F23) now refuse with exit 2 where frozen gave a verdict —
and git ≥ 2.45 is required. Any reading wider than the graded rows is
falsified by the open near variants listed in the lesson (RowF12, RowF21,
RowF22, RowF23, RowF26, RowC04, ExecSecondLanded, ExecAmbiguityFixture,
RevengeGitfile, CritTradeoffHarm H2, SentinelDoSW2 memory/`--errata`).

## Sources & frontier

Round start (base `4fe9339f`, extracted to a temp dir):
`scripts/sources-census.sh validate <base>/kama-shokunin` → `ok`, exit 0;
census rows 88, tier A 83 / B 2 / C 3, mined 72 / queued 8 / rejected 8.

Round end:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama   # W04 duplicate-URL warnings omitted
kama	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
exit 0
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama
kama	rows	101
kama	tier.A	96
kama	tier.B	2
kama	tier.C	3
kama	status.mined	84
kama	status.queued	8
kama	status.rejected	9
exit 0
```

- Rows 88 → 101: 13 added, all tier A (S089–S095 by CloseKama22; S096–S101
  by KamaR23-2; 12 docs, 1 code).
- Touched old → new: S095 status mined → rejected (teaches asserted an
  undocumented subprocess mechanism; SrcS095). Superseding rows: S096 →
  S095, S099 → S092 (anchor section), S100 → S091 (scope, `gpg.program`).
- Sourced claim: C1's knowledge entry cites S093/S096–S098; the grafts check
  cites S101; lesson §Gate carries URL, access date 2026-10-21 and quote for
  every new row.
- Append-only guard: `python3 tools/sources-append-only.py --from 4fe9339f8fc3a4a4a479d9c938a850da12f1124d --to `0df800e896f6bce285a81e794ad4ae1d1e6c3a71`` → `no append-only violations`, exit 0.
- Frontier: D4 partially advanced (graded rows only); everything else
  unchanged (`corpus/README.md` §Frontier disposition — round 23).
- Mistake mined: M4 fleet contamination by a seat fixture, M5 misroot, M6
  over-refusal of inert grafts, M7 harness FIFO leak; each with a fix shown
  able to fail (M29/C10, M32/C13).

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry or capability row; one
  entry deepened, 13 source rows.
- **quality: improved** — KQ34; three defective source rows corrected by
  superseding rows; mutant kills now require grid exit 1 and list their rows.
- **discernment: improved** — falsify findings became graded rows, contract
  reclassification, corrected counts (8 → 9 tracebacks) and a rejected row;
  over-refusal found and removed (M6).

## SHONEN

- [~] Real decision tables/error patterns/checklists/citations — author assertion; `SKILL.md` §Round23 registry rows.
- [~] End-to-end domain task executed/logged — unchanged; `LOG.md` earlier rounds.
- [~] Instructions executable without oral context — recorded commands in SCORECARD/LOG §round 23.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; no fleet/sibling edits beyond the removed markers (lesson M4) and the swept misroot (M5).

## Swarm, limits and operational disclosure

- Planner seat: held by the L1 (validator rejects `planner`); the bounded
  planning data-walk rode connector `ConnPlanningWalk` (build wave).
- Wave 1 build: 68 seats (scout 15, reviewer 14, executor 10, scribe 10,
  critic 5, connector 5, revenger 3, sentinel 2, mutation-tester 2,
  simplifier 2); dispatched 15:07Z, one call. Dead: 1 — RevClaimScope
  (reviewer): "Devin stream error resource_exhausted: Reached free model rate
  limit… reset … at 17:06 UTC".
- Wave 2 falsify: 73 seats (scout 24, reviewer 17, critic 8, executor 6,
  mutation-tester 4, connector 4, scribe 4, sentinel 2, revenger 2,
  simplifier 2); first attempt refused "Background job limit reached (100)",
  same payload spawned 15:46Z. Dead: 4, aborted by the host kill with no
  output — RowC01Clean, RowF07LogFollow, RowF09SignatureProgram ("Request
  was aborted" 16:10:50Z), CritOpenHonesty (last entry a tool result
  15:52Z, no final output).
- Round total 141 of 200 seats; no post-crash wave (59 remain, below the
  64 band, and falsification already ran). No dead seat replaced; their
  items were not re-issued.
- Fleet incident: four zero-byte `.promisor` markers written into the fleet
  repo by falsify seat RowF06LazyFetch's probe; removed by CloseKama22,
  absent at handoff (lesson M4;
  `.ufo/waves/round-23/falsify/fleet-contamination/promisor-markers.txt`).
- Tool installs: none.
- L0 questions: none opened.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Final report audit

From the lane directory, executed on this report's final draft before the fleet commit:

```sh
python3 tools/report-landing-audit.py --rounds 10-22 --report 23=<this report> --fleet-repo /home/vgpnk/Projects/shokunin --json
```

Observed exit 0, stderr empty; round 23: 5 round commits, 5 required, 0 defects, 0 post-report. Summary:

```json
{
 "by_kind": {
  "landed-ambiguous": 0,
  "landed-omitted": 8,
  "landed-section-missing": 0,
  "landed-unresolved": 0,
  "unresolved-full-hash": 1
 },
 "corrected": 9,
 "defects": 9,
 "errata_invalid": 0,
 "errata_rows": 9,
 "errata_unmatched": 0,
 "post_report_commits": 5,
 "reports": 14,
 "required_commits": 59,
 "rounds": [
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23
 ],
 "status": "clean",
 "uncorrected": 0
}
```
