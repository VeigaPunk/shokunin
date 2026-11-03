# kake — round 74

## Work performed

The round declared two claims, frozen in `.ufo/waves/round-74/contract.md` at
`b35dd4d7d6a0a633d7c950bf641d3f948e680448` (base controls and retained sources committed before any
seat ran), with Amendment 1 (terms only, after the wave-1 attack seats and before any after-state) at
`312b531a1e319cb0cc14d9d2eac4ff1414d6ca75`:

- **C1 calibration** (lowest owned axis, score 2, HOLD) — seven of the eight counters the frozen
  contracts of rounds 69–73 name had no `SKILL.md` gate-registry table row at base (only
  `c73_tmp_v3.py` was registered, and `c72_tmp_v2.py` was an unregistered routed debt). Land the
  seven rows plus the round's own counter row, with a counter that re-derives the gap from committed
  bytes and a selftest that kills the witness-cell, dump-row, prose-only, dead-path, missing-file and
  fenced-row readings.
- **C2 freshness** (score 10, HOLD) — `corpus/knowledge/freshness-sidecar.json` carried 148
  `kind=absent` notes, 144 of whose tokens resolve on this host (they were written on the Windows
  host, dated 2026-10-31). The standing sweep never probes a note's token for the note's own sake, so
  the contradiction was invisible. Land an `os.stat` three-way re-observation (present / absent on
  ENOENT·ENOTDIR / unevaluable on any other `OSError`), flip the 144 contradicted notes to dated
  `restored` observations with the prior note preserved under `history`, keep the 4 genuinely absent
  entries (3 tokens) `absent`, and land the counter and tool as the new capability. Sourced on S441
  and S442 (opened this round).

Work items, each with evidence:

- Freeze commit `b35dd4d7` (lane, via `jj-lane.sh`): contract, the three claim controls
  (`controls/base-c1-registry.txt`, `base-c2-sidecar.txt`, `base-c2-sweep.txt`) and the retained
  Python-doc sources (`.ufo/waves/round-74/sources/python-os-{path,stat}.{html,txt}`, byte-identical
  to ScoutSources' independent 2026-11-03 fetches).
- Amendment commit `312b531a`: A1–A7 (registration cells, one counter per row with the entry-command
  basename bound, `own_row` section bound, label honesty, append-after-935 placement, reproduction
  fields, unevaluable severity) and B1–B5 (severity, extended restored-note vocabulary, base-byte
  binding, zero-drift pass, field-name mapping), each closing a measured attack finding.
- Wave `w1` (one v1 wave, 14 seats, band 8–16; scout 2, executor 4, scribe 2, reviewer 2, critic 1,
  mutation-tester 1, connector 1, sentinel 1; attack share 4/14 = 28.6 %; the L1 held the planner
  seat): spec `w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json` — 14/14 settled,
  none dead. Dispatched through the inline handoff (`w1.ready` written 20:13, taken by the
  orchestrator; seats filled in tranches).
- Instrument deliverables integrated: `.ufo/waves/round-74/c74_registry_gap.py` (selftest 8/8; the
  delivered 5/5 was extended with f6 fenced-row, f7 witness-cell and f8 dump-row fixtures),
  `.ufo/waves/round-74/c74_sidecar_reobserve.py` (selftest 8/8; the delivered counter's verdict did
  not gate on its annotation findings — fixed and g8 added), `scripts/sidecar_reobserve.py` (selftest
  10/10; extended vocabulary, `ensure_ascii=False`, atomic replace, reader-mirroring validation,
  `--root` required with `--write`).
- Landing evidence: `SKILL.md` `### Round 74 gate registry additions` (32 appended lines, 0
  deletions), `corpus/knowledge/sidecar-reobservation.md`, one `corpus/README.md` coverage row, the
  `corpus/SOURCES.md` S441/S442 rows, the 144-entry sidecar rewrite, `SCORECARD.md` round-74 section
  and capability row, `LOG.md` round-74 entry, `corpus/lessons/round-74.md`.

## Landed changes

All tied to the LOG.md round-74 entry. Lane commits (pushed; `git ls-remote origin refs/heads/master`
shows the final hash): freeze `b35dd4d7`, amendment `312b531a`, round work `30c35842`, measured
claims/lesson `a0500653`, receipts `c9fd9643`.

- `SKILL.md` — the round-74 gate-registry section: seven population rows plus `c74_registry_gap.py`'s
  own row, with `gate (live …)` only for exit-0 counters and `instrument (historical …)` for the
  measured non-green ones; successor mentions spelled `.ufo/waves/round-73/c73_tmp_v3.py`. C1.
- `corpus/knowledge/freshness-sidecar.json` — 144 `absent` → `restored` flips with the prior
  observation under `history`; `line`/`lineSha256` unchanged (0 position changes); 4 absent entries
  remain. C2.
- `corpus/knowledge/sidecar-reobservation.md` — the new entry (provenance trio, S441/S442, the
  three-way probe, the procedure, the census, the limits). C2.
- `corpus/README.md` — one coverage row; it supersedes the old sidecar row's "30 entries" count.
- `corpus/SOURCES.md` — S441 and S442 appended after S440 (178 → 180 rows).
- `scripts/sidecar_reobserve.py` — the re-observation capability (check/write/selftest).
- `.ufo/waves/round-74/` — contract, amendment, controls (3 claim controls, 4 supplementary base-harm
  receipts with `controls/PROVENANCE.md`, 11 after receipts), sources, spec/dispatch/results, the two
  counters, and all 14 seat reports with their held-out fixtures.
- `SCORECARD.md` — the round-74 measured-claims section, the capability row and the move log; 37
  appended lines, 0 deletions.
- `LOG.md` — the round-74 entry (10 appended lines, 0 deletions).
- `corpus/lessons/round-74.md` — four mined mistakes, the Gate (5 admits / 5 rejects), the sourced
  claim and the routed limits.

Inherited state resolved: none — the lane was clean at `ced2878a` (`git status --porcelain` empty at
round open). The four `base-harm-*.txt` receipts are the L1's own post-freeze supplementary readings,
disclosed in `controls/PROVENANCE.md` and lesson M4; the three claim controls remain the frozen set.

## Before → after measurements

- **C1 (calibration)** — counting command
  `python3 -B .ufo/waves/round-74/c74_registry_gap.py --root . --revision <rev>`
  (receipts `controls/base-c1-registry.txt`, `controls/after-c1-registry.txt`,
  `controls/after-c1-registry-final.txt`):
  - Before, base `ced2878a`: `unregistered=7 own_row=false met=false`, exit 1.
  - After, landed tip `30c35842`: `unregistered=0 own_row=true met=true`, exit 0; re-measured at `a0500653` and at the
    final tip `c9fd9643`: same line, exit 0. The do-nothing control is the base receipt: no row added
    leaves `unregistered=7`.
- **C2 (freshness)** — counting command
  `python3 -B .ufo/waves/round-74/c74_sidecar_reobserve.py --root . --revision <rev>`
  (receipts `controls/base-c2-sidecar.txt`, `controls/after-c2-sidecar.txt`,
  `controls/after-c2-sidecar-final.txt`):
  - Before, base `ced2878a`: `entries=174 absent=148 restored=26 absent_present=144 contradictions=144
    met=false`, exit 1; the standing sweep at base exits 1 with one unannotated miss and never names
    the 144 contradictions (`controls/base-c2-sweep.txt` — the blindness control).
  - After, landed tip `30c35842`: `absent=4 restored=170 absent_present=0 contradictions=0
    annotation_findings=0 met=true`, exit 0; re-measured at `a0500653` and at the final tip `c9fd9643`: same line, exit 0. The
    sweep's `--selftest` stays `36/36` and `--offline` stays exit 1 with the same single `~/projects`
    drift and no `Error:` line (`controls/after-harm-sweep-selftest.txt`,
    `controls/after-harm-sweep-offline.txt`).
- **Harm at `a0500653`** (claim counters and the sweep re-checked at the final tip `c9fd9643` with the same lines): c66 exit 0 (`members=28 evaluated=28 mismatches=3
  structural=0 agreement=25 scores_held=3/3 met=True`), c70 exit 0 (`pointers=373 dangling=17
  annotated=17 unannotated=0 append_only=true met=true`), c72 exit 0 (`findings=[] met=True`),
  c73_wave_pointers `met=true`, c73_tmp_v3 `selftest=41/41 findings=[] met=True`; the three new
  instrument files carry 0 `/tmp` literals. Receipts `controls/after-harm-*.txt`.

## Sources & frontier

- Census: before — `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kake` exit 0 (`ok`, 178 rows; the 16 W04 duplicate-URL warnings are
  pre-existing and allowed). After — same command, exit 0, `ok`, 180 rows
  (`controls/after-census.txt`).
- Rows before→after: 178 → 180. Rows added by tier: two tier-A `docs` rows — S441
  (`docs.python.org/3/library/os.path.html#os.path.exists`) and S442
  (`docs.python.org/3/library/os.html#os.stat`), both opened 2026-11-03 and retained under
  `.ufo/waves/round-74/sources/`. Rows touched old→new: none (no status, recheck or used-by cell of an
  existing row changed; the diff is 2 additions, 0 deletions). Frontier rows advanced: none (the two
  rows back the round's freshness instrument and its knowledge entry; no new coverage-map ground
  beyond the sidecar ground the lane already held).
- The lesson's `## Gate` records both URLs, the 2026-11-03 access dates, located ≤25-word quotes
  (S441: "may return False if permission is not granted to execute os.stat() on the requested file,
  even if the path physically exists"; S442: "All functions in this module raise OSError (or
  subclasses thereof) in the case of invalid or inaccessible file names and paths"), and 5 admits /
  5 rejects with reasons.
- Assimilation: none. The round's claims are lane-instrument repairs; no `merge/kake/` source was
  opened and no `considerthese/` proposal was implemented (the latest file's open proposals remain
  candidates for a later round).

## Trend verdicts

- **expansion: unchanged** — one new knowledge entry (`sidecar-reobservation.md`) on ground the lane
  already holds (the local-path freshness sidecar), two curated rows, no frontier-map move. Evidence:
  the SOURCES diff (2 additions, 0 deletions) and the absence of a new coverage area.
- **quality: improved** — two instruments added or repaired with able-to-fail evidence: C1's counter
  is red at base and green at the tip over the same eight counters (7/8 → 0/8 unregistered), with
  eight selftest fixtures; C2's counter goes 144 → 0 contradictions with history preserved, and the
  standing sweep is unchanged (36/36, exit 1 same drift), so no gate was weakened to go green. The
  attack seats measured the delivered counters' two verdict gaps and both were closed before the
  after-state (A2, M2).
- **discernment: improved locally** — four mistakes mined with evidence, the Gate records 5 admits
  and 5 substantive rejects (including rejecting the "any cell" registration test and the "clean"
  freshness reading), and the contract's amendment was written only after the attack seats' measured
  findings and before any after-state. The independent non-author spot-check is owed to the hyaku
  closure, as recorded in the lesson.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the round-74
  gate-registry section (eight rows, honest Kind labels, entry/self-test commands) plus S441/S442;
  `w1/ReviewerC1.md` and `w1/ConnOverlap.md` re-derived the row grammar and the placement.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-74 LOG entry with
  the two frozen claims measured end-to-end; receipts under `.ufo/waves/round-74/controls/` measured
  at `30c35842`/`a0500653`.
- [~] Instructions executable by an agent without oral context — the registry rows' command cells,
  `scripts/sidecar_reobserve.py`'s `--check`/`--write` CLI and the contract's amendment re-derive every
  step; the wave's 14 seats ran from committed bytes alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched; the round's only web
  reads were two public Python-doc GETs; `w1/ConnOverlap.md` found no sibling overlap requiring
  arbitration.

## Stale-lane

kake's own mission: this round, landed and reported; no other mission of this lane is open
(respawn-per-round driver). Age under two driver ticks.

## Tooling

No tool installed or upgraded by the L1 or any seat this round (pacman untouched, per the host-wide
pause). The wave's seats recorded the host toolchain they used (git, node, Python 3) and no installs.

## Round shape

One v1 wave `w1` of 14 seats (band 8–16), no residual call, round total 14. Roles: scout 2, executor
4, scribe 2, reviewer 2, critic 1, mutation-tester 1, connector 1, sentinel 1; dead seats: none
(14/14 settled in `w1-results.json`). Lane commits: freeze `b35dd4d7`, amendment `312b531a`, round
work `30c35842`, measured claims/lesson `a0500653`, receipts `c9fd9643` (pushed; ls-remote
shows the final hash). Report commit follows via `fleet-commit.sh`.
