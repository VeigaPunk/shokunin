# kaidoku — round 88 (attempt 3)

Lane HEAD after the round: `a242fff3fe339ffae31d83960062609a784b97c4` (`git -C kaidoku-shokunin ls-remote
origin refs/heads/main` prints it). Base `0cf8e3243059e0bc510b90c880d13d191e78d732`.

## Work performed

Declared claims (two, both frozen before data; axes: coverage, depth):

- **R88-C1 — coverage, capability acquisition (Frontier → Core).** A packed UPX 5.2.0 little-endian ELF whose
  first `b_info`'s `sz_cpr` is zeroed (`upx -t` answers `b_info corrupted`; the round-87 magic repair refuses)
  is repaired from chain geometry (`12 + sz_cpr` contiguity, `sz_unc` bound, PackHeader `u_len` accounting),
  composing the round-87 anchor repair unchanged. Frozen predicate: `recovered 4 of 4` with
  `N1-refuse-plain`/`N2-corrupt-payload`/`N3-intact-idempotent` all true, the round-87 regression arm 8 of 8,
  exit 0.
- **R88-C2 — depth.** Craft rule block 28 (the refusal-signature decision table) lands: `blocks 28,
  resolved 28, unresolved []`, exit 0, where a block resolves only when every `corpus/knowledge/<name>.md`
  citation it carries exists at that revision and its range is inside the file.

Frozen container `.ufo/waves/round-88/claims.json` (freeze `70d6f7dec57a874e31bb53ee7f10056cffec656d`), plan
`plans/round-88-claims.md` (declaration `7fbe16d455d52e83d42fbfe176e30c7cbb17694b`).

- **Declaration and pre-freeze controls.** Four instruments, three base controls, census before, and a red
  freeze-gate fixture (a container naming an absent counter) at `7fbe16d4` / `d190c5b5`:
  `.ufo/waves/round-88/pre/c1-control-{identity,naive-global,r87-anchor}-at-base.json`,
  `pre/c2-depth-at-base.json`, `pre/c2-control-junk-blocks.json`, `pre/red-container.json`.
- **Instrument supersession, disclosed before data was scored.** `field-tamper-matrix-v2.py` replaces the v1
  matrix (v1 reported five zero-over-zero writes as `tolerated` and left five real messages
  `other-refusal`); predicates, counters, labels, kill rules and targets unchanged, re-taken before record
  `l1/scores/c2-matrix-at-declaration.json` (68 cells, 63 effective, 0 unclassified). Entry appended to
  `claims.json` `instrument_supersessions` at `01ffb937`.
- **One v1 wave `r88-w1`, 14 seats** (spec/dispatch/results under `.ufo/waves/round-88/`, evidence under
  `w1/`): executor 4, scout 2, scribe 2, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1;
  attack 5/14 = 36 %; the L1 held the planner seat (the validator rejects `planner`). Seven seats delivered
  a report (ExecGeomCross, ExecMutation, ExecR87Regress, ReviewerC1, ReviewerC2, CriticClaims, ConnectorR88).
  Seven settled with a partial transcript and no report: ExecMatrix, ScoutUpxSrc, ScoutHostClasses,
  ScribeEntry, ScribeSources, MutationR88, SentinelR88. The results file carries no per-seat error field, so
  each cause is `unknown`; their last text verbatim: "I'll start by reading the plan, claims container, and
  the instrument." (ExecMatrix), "…reading the plan, claims, and existing sources registry in parallel."
  (ScoutUpxSrc), "…orienting on the lane, the frozen plan, and the tools I need to inspect."
  (ScoutHostClasses), "…reading the required inputs in parallel." (ScribeEntry), empty (ScribeSources),
  "…reading the target instruments and setting up my scratch." (MutationR88), "Decisive: the tool reported
  the pinned source hash while executing a tampered `.pyc`. Now fuzzing for unhandled exceptions."
  (SentinelR88). None of the seven is treated as evidence.
- **Integration** (`a14f0a42`, `1a72fdef`, `bd74e8bc`, `5cd1b164`): repair `tools/round-88/upx-chain-repair.py`
  (11-case selftest, composes the round-87 module by path), counter `tools/round-88/upx-chain-battery.py`
  (4-case selftest, three controls, round-87 regression arm), matrix v2 (13-case selftest), depth counter
  `tools/round-88/depth-blocks.py` (7-case selftest); knowledge entry
  `corpus/knowledge/2026-11-04-r88-binfo-chain-geometry.md`; SKILL decision-table row + craft block 28;
  PROVINCE `## Round-88 additions to Core`; `corpus/README.md` coverage row and frontier note; QUALITY rows
  154-160; `corpus/lessons/round-88.md` (M88-1..M88-10).
- **Independent re-derivations inside the wave.** ExecGeomCross derived 252/249/201/226 from scratch
  (445,684 offsets scanned) and reproduced the committed repair on 4 of 4 carriers; ExecR87Regress ran the
  frozen round-87 counter with the new repair (8 of 8, 139.87 s, `--no-rea` 0 of 4); ExecMutation's 13-row
  single-edit table found two surviving guards (R01 derived-bound, R02 sentinel-reach) not killed by any
  selftest case; ReviewerC1 reproduced the predicate (196.9 s) and scored eight cheaper rules, one of which
  (packer-as-oracle, R7) reaches 4 of 4; ReviewerC2 reproduced the matrix v2 receipt cell-for-cell and probed
  the depth counter's floor; CriticClaims falsified both claims' *instruments* (see verdicts); ConnectorR88
  separated `sz_unc` (not recoverable) from `sz_cpr` (recoverable) under one refusal string.
- **Final-tip re-measurement (this attempt).** Both frozen counters re-run on `5cd1b164` with all four
  `claims.json` pins re-hashed byte-equal: C1 `recovered 4 of 4`, controls true, regression 8 of 8, exit 0
  (133.4 s, `l1/scores/c1-at-5cd1b164.json`); C2 `blocks 28, resolved 28, unresolved []`, exit 0
  (`l1/scores/c2-at-5cd1b164.json`).
- **Inherited state, resolved.** Attempt 1's L1 (`KaidokuR88`) kept running after the driver declared the
  round dead at 20:36 and landed the wave-integration commit `5cd1b164` under the lane identity through
  `jj-lane.sh`; this attempt verified that commit's content, stood the stale L1 down by message (it confirmed
  no further writes, commits or spawns), and did not rewrite it. Attempt 2 (`KaidokuR88a2`) built an 11-seat
  second-wave spec at 20:42 and wrote its `.ready` at 20:43, then died; run-15's round shape is ONE v1 wave of
  8-16 seats and `r88-w1`'s 14 seats already met it, so the wave was **not dispatched** and its unused
  `r88-w2.ready`, spec, dispatch and generator were reverted (not committed). Untouched inherited untracked
  files, named not edited: `.ufo/waves/round-{85,86,87}/r*-w1.ready{,.dispatched}`.

## Landed changes

| commit | carries | LOG.md entry |
|---|---|---|
| `7fbe16d4` | plan, four instruments, three base controls, census before, wave spec/dispatch | `## 2026-11-04 — round 88` (declared claims) |
| `70d6f7de` | `claims.json` freeze | same entry (freeze) |
| `d190c5b5` | red freeze-gate fixture | same entry (prefreeze gate) |
| `6d235a4c` | matrix v2 + 68-cell receipt + prefreeze receipt | same entry (supersession) |
| `01ffb937` | `instrument_supersessions` append | same entry (supersession) |
| `a14f0a42` | repair, counter, depth counter, entry, S309/S310, craft block 28, Core row, README, QUALITY 154-155, lesson | same entry (integrated work, sources) |
| `1a72fdef` | measured receipts, SCORECARD capability row and round section, LOG entry | same entry (measured) |
| `bd74e8bc` | entry/plan wording, M88-4..M88-6, QUALITY 156, `sz_unc`-vs-`sz_cpr` receipt | same entry (mistakes) |
| `5cd1b164` | wave results and evidence, M88-7..M88-10, QUALITY 157-160, PROVINCE receipt pointer | same entry (wave attacks) |
| `a242fff3` | final-tip measurement of both counters, SCORECARD wave/attack record, LOG bullet | same entry (wave attacks and final-tip measurement) |

Lane tip `a242fff3fe339ffae31d83960062609a784b97c4` is on `origin/main` (`ls-remote` output above).

## Before → after measurements

**R88-C1 (coverage).** Recovered 0 of 4 → 4 of 4.

- Counting command: `python3 -I -B tools/round-88/upx-chain-battery.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --repair-cmd tools/round-88/upx-chain-repair.py --upx /usr/bin/upx --pkg /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --work <scratch> --json-out .ufo/waves/round-88/l1/scores/c1-at-5cd1b164.json`.
- Measured against `5cd1b1641f462f29fe0bc170b87ba69f1ba45ba1` (the round's final tip); the same value was
  measured at the integration revision `a14f0a42` (`l1/scores/c1-at-a14f0a42.json`) and at `bd74e8bc`
  (`l1/scores/c1-at-bd74e8bc.json`).
- Before (at the declaration): the unchanged round-87 repair `recovered 0 of 4` with all three controls true,
  exit 1 (`pre/c1-control-r87-anchor-at-base.json`); do-nothing `identity` 0 of 4; cheap rule `naive-global`
  0 of 4.
- After: `recovered 4 of 4 controls_ok={'N1-refuse-plain': True, 'N2-corrupt-payload': True,
  'N3-intact-idempotent': True} met=True exit=0`; regression arm `recovered 8 of 8`, controls true, rc 0.
  Per carrier (jq/xxd/libz/dinit) every arm is true: `field_only`, `identity`, `rea_recover`, `repair_rc0`,
  `test_ok`; REA procedure counts 167/99/184/1268 on the restored bytes.
- **Verdict: met under the frozen predicate.** Weakened, disclosed, routed: the label is not
  mechanism-unique — a packer-as-oracle repair (`w1/ReviewerC1/report.md` §2 R7) and a window-restricted copy
  of the counter's own `packed` sibling (`w1/CriticClaims/receipts/cheat-c1-sibling-v2.json`) both score
  4 of 4 with every control true (M88-4, M88-8). The scan cost is quadratic in the candidate count and was
  measured, not asserted: 800 candidates/25,760 bytes → 1.02 s, 3,200/102,560 → 14.22 s,
  12,800/409,760 → 221.85 s (`l1/scores/c1-candidate-scan-scaling.json`; M88-10).

**R88-C2 (depth).** `blocks 27, resolved 27` → `blocks 28, resolved 28, unresolved []`.

- Counting command: `python3 tools/round-88/depth-blocks.py --root . --rev 5cd1b1641f462f29fe0bc170b87ba69f1ba45ba1 --json-out .ufo/waves/round-88/l1/scores/c2-at-5cd1b164.json`.
- Measured against `5cd1b1641f462f29fe0bc170b87ba69f1ba45ba1`; the same value was measured at `a14f0a42`
  (`l1/scores/c2-at-a14f0a42.json`).
- Before: base `0cf8e324` gives `blocks 27, resolved 27, met_target true` (`pre/c2-depth-at-base.json`); the
  junk-block control gives `blocks 29, resolved 27`, exit 1 (`pre/c2-control-junk-blocks.json`).
- After: `{"blocks": 28, "met_target": true, "resolved": 28, "unresolved": []}`, exit 0. Matrix evidence for
  the block's content: 68 cells, 63 effective, 0 unclassified, 10 labels
  (`l1/scores/c2-matrix-at-declaration.json`).
- **Verdict: met under the frozen predicate; falsified as a *discriminating* measure.** `met_target` is
  `not unresolved`, so the counter exits 0 at base with 27 blocks and a one-line citation-only block scores
  28/28 (M88-7); the landed block also cites the C1 knowledge entry, absent at base, so the landed artifact
  is not causally separable, although ReviewerC2 measured a base-citing block at 28/28 at base bytes (M88-9).
  The depth content is bound by the frozen block text and the review, not by the instrument.

**No axis harmed.** Calibration, freshness and the coverage/depth score numbers are unchanged; the round
edited no score row (SCORECARD round-88 section).

## Sources & frontier

Census command, run at round start and at round end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`

- Before: exit 0, **213 rows** (recorded at the declaration, `7fbe16d4`; `git show 0cf8e324:corpus/SOURCES.md`
  counts 213 data rows).
- After: exit 0, **215 rows** (this attempt, 28 W04 duplicate-URL warnings, no E03/E04 finding).
- Rows added by tier: tier **A +2** — S309 (`src/packhead.h` at `v5.2.0`) and S310 (`src/packer.cpp` at
  `v5.2.0`), both HTTP 200 with recorded sha256 and a located quote in the lesson's `## Gate`.
- Rows touched old→new: S309 `absent → mined`, S310 `absent → mined`, both `used-by
  corpus/knowledge/2026-11-04-r88-binfo-chain-geometry.md`; `p_unix.cpp` re-opened and its round-87
  rejection kept (no row, flip not met); `src/headers.h` opened and rejected (HTTP 404, no row).
- Frontier rows advanced: PROVINCE `Frontier` class "anti-UPX stub whose magic or entry is altered" gains the
  zeroed-`sz_cpr` corruption class in Core (`PROVINCE.md` `## Round-88 additions to Core`, receipt pointer
  corrected to the measured `c1-at-a14f0a42.json` at `bd74e8bc`); `corpus/README.md` coverage row for
  `packed-ELF b_info chain geometry` plus the round-88 frontier note.
- Sourced claim: R88-C1's entry cites S309 and S310, both opened this round (§2b item 4).
- **Assimilation: none** — `merge/kaidoku/` was not consumed this round (two-claim budget); no package entry
  was opened. No `considerthese/` directory exists in this lane.
- Mistake mined: `corpus/lessons/round-88.md` `## Mistakes` carries M88-1..M88-10 with class, evidence
  pointer, captured-by and fix; M88-1..M88-3 were mined from the instruments' own pre-freeze runs, M88-4..M88-10
  from the wave's attacks, each fix shown able to fail or explicitly routed because the instrument is frozen.

## Trend verdicts

- **expansion — improved.** A corruption class moves from Frontier to Core with a measured capability row
  (`SCORECARD.md` capabilities, `packed-ELF b_info chain geometry`), two tier-A sources are mined, and the
  Core row is backed by a re-run at the final tip. Surface: PROVINCE `## Round-88 additions to Core`.
- **quality — improved.** Four attack seats plus a critic found ten defects; six corrections landed this round
  (QUALITY rows 156-160, the PROVINCE receipt pointer, the plan's stale vocabulary sentence, the entry's
  sentinel wording) and the four that need an instrument change are routed with their red controls named.
- **discernment — improved.** The round's own instruments are now known not to force their labels: a
  mechanism-blind repair scores C1's target and a content-free block scores C2's target, both measured and
  committed (`w1/CriticClaims/receipts/`). The round reports both claims met **and** both measures
  non-discriminating, rather than either alone.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — craft block 28 (17-row refusal table) plus the round-88 decision-table row, `SKILL.md` at `a14f0a42`; depth counter resolves 28 of 28 blocks at `a242fff3`.
[~] At least one end-to-end domain task executed and logged in LOG.md — pack → zero `sz_cpr` → repair → `upx -t`/`upx -d` to the carrier pin → REA inventory 167/99/184/1268; `l1/scores/c1-at-5cd1b164.json`, LOG `## 2026-11-04 — round 88`.
[~] Instructions executable by an agent without oral context — seven wave seats reproduced the predicates and the 4-case/11-case/13-case/7-case selftests pass from the committed plan and tools alone (`.ufo/waves/round-88/w1/`).
[~] No cross-domain bleed (PROVINCE.md still accurate) — ConnectorR88's cross-lane scan found no sibling lane holding this ground (`w1/ConnectorR88/links.md`); PROVINCE's Core row now cites the measured receipt.

## Notes

- **Stale-lane:** respawn-per-round driver; round 88 is this lane's only open mission (campaign target round
  100; `next/` advanced to 89 by the driver, not by this report).
- **Tool installs/upgrades: none** this round (host pins unchanged: `upx 5.2.0` at `/usr/bin/upx`, REA
  `rea-agents` 6.5.0 from the existing npx cache, both sha256-pinned in `claims.json`).
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): no kaidoku file landed at the
  fleet root. Present and untouched: `?? after` (24 bytes, 2026-11-03, another lane's), `M
  .ufo/reports/round-84/kama.md` and `M .scratch/run15-state.json` (not this lane's).
- **Scratch:** every seat and the L1 worked under `/fast/scratch/hyaku/kaidoku-r88/<seat>/`; the L1 tree is
  removed after landing. No `/tmp` path is cited as evidence.
- **Open L0 questions: none filed this round.**
