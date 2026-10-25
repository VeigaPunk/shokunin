# chousa — round 43 report

lane: chousa · round: 43 (attempt 1) · host: Kimi, fresh L1 (`Kimi fresh L1`) ·
date: 2026-10-24 · lane repo: `/home/vgpnk/Projects/shokunin/chousa-shokunin`

**Round shape.** One v2 wave (policy `scripts/hyaku/ufo-wave-policy-v2.json`, band 64–128),
64 seats, 26 attack roles (40.6%). AgentSwarm is not exposed on this Kimi seat. The
validated `taskCall` was dispatched as one batch of `kimi --agent-file` processes. The
parent stayed up until those processes exited. Dead seats were not replaced.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

**Tool installs:** none. Pacman was not used.

## Work performed

**Declared claims (frozen in `corpus/evidence/round43/claims.md` before any seat scored;
measured at `737f40b6aa8f37ffe2269db370fd6d65a720d9a8`):**

- **C1 — operability** (lowest scored non-retired axis, 3/10): `tools/absent-split.py`
  enumerates the 15 rows the committed round-42 table labels `absent`, assigns each
  exactly one of {misquote, not-carried}, both classes are nonempty, and two runs match.
- **C2 — calibration:** every label in `corpus/evidence/round43/absent-split.tsv` agrees
  with an independent recompute of rule R43-SPLIT (NFKC, whitespace collapse, longest
  contiguous run, row maximum ≥ 1/2 → misquote, else not-carried). A one-row flip fails.
- **C3 — depth** (sourced on S078): `corpus/knowledge/search-log-method-r39.md` cites
  lane S078, that row's URL is the Europe PMC full-text opened from the committed
  capture, and the located quote is in that capture.

**Work items, each with an evidence pointer:**

- Rule R43-SPLIT frozen before scoring. Construction recompute reproduced the published
  ratios (S086 4/46 and 2/29; S093 79/120) and is disclosed in `claims.md`. The 1/2 bound
  was not retuned after seats scored.
- Split table: `corpus/evidence/round43/absent-split.tsv` — 9 `misquote`, 6 `not-carried`.
  Named examples land on the lesson's sides: S093, S094, S108, S116 are `misquote`;
  S086 and S114 are `not-carried`.
- Do-nothing controls fail: missing tool exits 1 (`controls/c1-control-before.txt`);
  `--flip S086` scores 14/15 and exits 1 (`controls/c2-control-before.txt`); missing
  entry exits 1 (`controls/c3-control-before.txt`).
- One theme adopted, one entry: search-log method, from the committed Europe PMC
  capture only. No fetch (L0 `8d77e6c1` still open).
- Rejected with reason and flip: `search-log-fields-r36.md` (staged S077 capture is a
  267-byte / 265-character Client Challenge; the Japanese capture does not contain
  参照日) and `search-tracking-record-r40.md` (the column sentence is not contiguous
  in the pdftotext capture). Gate: `corpus/lessons/round-43.md`.
- Collision handled by document. Lane S077 stays the pdftotext manual. Staged S077
  (PRISMA-S DOI) is not adopted. The Europe PMC URL (staged id S118) is lane S078, the
  next free lane id. Staged S078 is the Cochrane chapter and is not this row.
  `assimilation/collisions` contains only S077. The indented fixture `  | S118 |`
  collides; a column-zero pattern misses it (`assimilation/guard/`).
- Scratch census before the append: `validate --file` on the mirrored registry plus
  the S078 row, exit 0, no E03/E04 (`assimilation/validate-census.txt`).
- QUALITY 61, mined from `considerthese/2026-10-24.md` and not edited there: a
  validated spec is not a completed dispatch. Shown able to fail on the round-42
  registry of null agent ids.
- Append-only erratum in `corpus/lessons/round-42.md`: the S077 capture is 267 bytes
  and 265 Unicode characters. The r42 sentences were not rewritten.
- Inherited debt, deliberate: `PROVINCE.md` mode restored to 644 (content unchanged).
  Prior-wave registries, r41 `cells.json`, and untracked r40/r41 seat reports left
  untouched. Register not edited. Both routed by L0.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| split tool, counters, controls, table, S078 row, knowledge entry, lesson, QUALITY 61, erratum, SCORECARD, LOG, assimilation scratch | `LOG.md` Round 43 | `737f40b6aa8f37ffe2269db370fd6d65a720d9a8` |
| wave spec, plan, dispatch, settle table, 48 seat reports | `LOG.md` Round 43 (wave named in the report; the evidence commit is this hash) | `a0ecc586b1c686a035388c5ed522cacfe55e372f` |

`jj-lane.sh` printed `landed 737f40b6aa8f37ffe2269db370fd6d65a720d9a8` and
`landed a0ecc586b1c686a035388c5ed522cacfe55e372f` after remote verification.
No raw git or jj mutation. No sibling repo, fleet script, prompt, or MANIFEST edit.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 operability | `python3 corpus/evidence/round43/c1-count.py` | missing tool exits 1 (`controls/c1-control-before.txt`) | `ABSENT_ENUMERATED=15/15`, `CLASSED=15/15`, `BOTH_NONEMPTY=1/1`, `REPRODUCIBLE=1/1`, `MUTANT_DETECTED=1/1`, `C1=PASS`, exit 0 | `737f40b6aa8f37ffe2269db370fd6d65a720d9a8` |
| C2 calibration | `python3 corpus/evidence/round43/c2-count.py` | `--flip S086` → `SPLIT_AGREES=14/15`, exit 1 | `SPLIT_AGREES=15/15`, `VOCAB_OK=15/15`, `C2=PASS`, exit 0 | `737f40b6aa8f37ffe2269db370fd6d65a720d9a8` |
| C3 depth | `python3 corpus/evidence/round43/c3-count.py` | missing entry exits 1 (`controls/c3-control-before.txt`) | `ENTRY_CITES=1/1`, `QUOTE_LOCATED=1/1`, `URL_MATCH=1/1`, `C3=PASS`, exit 0 | `737f40b6aa8f37ffe2269db370fd6d65a720d9a8` |

The round-1 operability scale is unchanged: **3 → 3**. `tools/research-gate.sh` was not
edited. A landed executor re-ran `--selftest` and recorded `PASS (275 cases, 0 skipped)`
(`.ufo/waves/round-43/w1/ExecNoHarmGate.md`).

Landed reviewers re-ran the three counters on the committed bytes and agreed
(`ReviewC1Rerun.md`, `ReviewC2Rerun.md`, `ReviewC3Rerun.md`). `MutFlipS086.md` and
`CritDoNothing.md` confirmed the controls still fail. No seat retuned the 1/2 bound.

## Sources & frontier

- SOURCES rows before → after: **77 → 78** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Rows added by tier: **tier A +1** (S078, Europe PMC full-text XML of Bramer et al. 2018,
  opened from the committed capture, sha256 `833b13e3e80212522d016a8db9c6edeacb8965148d2334722a7a73c415d7136d`).
  Tier B +0, tier C +0.
- Rows touched old → new: S078 is new (`mined`, recheck `365d`, used-by
  `corpus/knowledge/search-log-method-r39.md`). No other row's status, recheck, or
  used-by changed. Staged recheck prose was stripped to `365d` and recorded in the Gate.
- Frontier: one search-log method fact the lane did not hold. The three-literatures
  entry was refused. No coverage-map rewrite.
- Census start: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`,
  exit 0, five W04 warnings (S051, S053, S073, S074, S075).
- Census end: the same command, exit 0, the same five W04 warnings
  (`corpus/evidence/round43/receipts/census-end.txt`).
- Scratch validate before append: exit 0, no E03/E04.
- **Assimilation: yes** — one theme (search-log requirements). One entry admitted
  (`corpus/knowledge/search-log-method-r39.md`, filename is the package's label).
  Two rejects with flip, recorded in the lesson Gate. No bulk append. Campaign tree
  read-only.
- Located quote (12 words), access 2026-10-24, no fetch: "to register the steps taken
  and to make searches accountable and reproducible."

## Trend verdicts

- **expansion: improved** — one opened row (S078) on a source the lane did not hold,
  one lesson, and one new operation (the absent-class split). The measure is the new
  surface plus the row, not the row count.
- **quality: improved** — both split counters fail their do-nothing controls, and a
  landed reviewer re-ran them. QUALITY 61 records that a prepared spec is not a
  dispatch, shown able to fail on the round-42 null-id registry.
- **discernment: unchanged** — the admit/reject sample has no non-author spot-check.
  Seats this lane dispatched are still the lane. The sample is ready for the outside
  closure.

## SHONEN

- [~] Real decision tables / error patterns / checklists with cited sources —
  `corpus/evidence/round43/claims.md` (rule R43-SPLIT) and
  `corpus/knowledge/search-log-method-r39.md` (S078). No `[x]`: no non-author verifier.
- [~] An end-to-end domain task executed and logged —
  `corpus/evidence/round43/receipts/c1-after.txt` and `c3-after.txt`.
- [~] Instructions executable by an agent without oral context —
  `tools/absent-split.py` and `corpus/evidence/round43/claims.md`.
- [~] No cross-domain bleed; `PROVINCE.md` still accurate — content untouched; mode
  restored to 644. Campaign tree and sibling repos were read-only. No egress.

## Wave, seats and dead seats

- Shape: **one v2 wave**, spec `.ufo/waves/round-43/w1-spec.json`. Validator `plan` and
  `run` exit 0 (`w1-plan.json`, `w1-dispatch.json`, 64 tasks).
- Seat mix dispatched (64): reviewer 8, critic 8, mutation-tester 6, sentinel 2,
  revenger 2 = **26 attack (40.6%)**; executor 12, scout 10, scribe 8, connector 4,
  simplifier 4 = 38 build. The §3 floor was inside the dispatched wave. The planner
  seat is the L1. Scout and connector seats died without reports; their findings are
  absent, not passed.
- Grant, immediately before launch: `wave-slot.sh acquire chousa round-43-w1 64 3600`
  → `granted lane=chousa wave=round-43-w1 seats=64 live=32 pending=0 cap=256`.
  Released after settlement: `released lane=chousa wave=round-43-w1`.
- **Dispatch, as observed.** AgentSwarm is not a tool on this seat. The validator's
  `taskCall` (context + 64 tasks, unchanged) was launched as one batch of
  `kimi --agent-file` processes, one per task, each with a 480-second timeout.
  The first launcher script's `wait` ran in a pipeline subshell and printed `pids 0`
  before the processes were visible to that shell. The processes had started. A waiter
  parent stayed until they exited. That waiter was not a second wave and spawned no
  seats. Dead seats were not replaced.
- **Reports: 48. Dead: 16.** Settle table: `.ufo/waves/round-43/w1-settle.tsv`.
  Dead, no report file, not replaced: CritBoundHalf (critic; log ends mid-verdict,
  no report), SentNoEgress (sentinel; log claims a write that did not land),
  ScoutProvince, ScoutSiblingKengaku, ScoutSiblingKasegi, ScoutFrontier,
  ScoutCaptureForm, ScoutLaneS077, ScoutStagedS077, ScoutJapaneseHead,
  ScoutCochraneNotAdopted, ScoutRegisterStale (all 10 scouts; logs show tool-loop
  or "Write not available", no report), ConnSiblingScan, ConnQuoteReopen,
  ConnKumitate, ConnNoSecrets (all 4 connectors; same class). Last-error text is
  in the settle table. Nothing here counts a prepared spec as a dispatch.
- Round total: 64 seats in one validated wave. No residual call.

## Routed repairs from round 42

1. Absent-class split: landed as C1/C2. 9 misquote, 6 not-carried.
2. Wave completion: 48 reports from processes that ran. QUALITY 61. The round-42
   null-id registry is the shown-able-to-fail case, not this round's evidence.
3. Inherited working-tree debt: mode bit restored; the rest named and left, with an
   L0 asking the operator to commit or leave the r40/r41 seat reports.
4. Register staleness: L0 to the campaign owner. The register was not edited.
5. 265/267 nit: append-only erratum. Both numbers are true (267 bytes, 265 characters).
6. S077 collision: handled by document at adoption, as above. Lane S077 was not overwritten.

## Honesty and open questions

- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows driver
  runtime (`.ufo/state/*`, `.ufo/watchdog.log`) and untracked files (`bm.json`,
  `live.html`, `nama.html`, `live_s228.html`, `s395.txt`, and others) that do not name
  chousa round 43. Left untouched. No seat report landed at the fleet root.
- **Egress:** none. Every source opened this round is a committed capture or an
  already-registered installed file. The fetch-scope L0 `8d77e6c1` is still open.
- **Open L0 questions:** fetch-scope `8d77e6c1` (unchanged; this round did not fetch);
  register staleness (new, round 43); disposition of the inherited r40/r41 working-tree
  files (new, round 43). The r42 collision question is answered for this adoption by
  the item-10 by-document rule; the operator can still overrule that reading.
- **Known limits:** C1 grades that the command partitions the 15 rows. It does not
  grade label truth. C2 grades label agreement with the frozen rule, not live-web
  truth. C3 grades one located quote in one committed capture, not the three-literatures
  checklist. The 1/2 bound is the lane's construction.
