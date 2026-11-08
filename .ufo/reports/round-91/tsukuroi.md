# tsukuroi round 91 — limine-pins visibility repair and unverified-image plane

L1: TsukuroiR91a2 (attempt 2). Prior attempt TsukuroiR91 (attempt 1)
died without a report (`lane-dead-no-report tsukuroi round=91`
2026-11-08T00:55:20-03:00); its committed work is inherited and reused
(see **Inherited state** below). Lane tip at writing:
`9df223fd85cd2201ecb6015d87c1262f3c0d47c7` (remote `refs/heads/master`
matches), via the `jj-lane.sh` helper only.

## Work performed

Declares the round's claims (narrowed by `.ufo/plans/round-91.md`,
binding the falsification ledger):

1. **C1 (measured, operability 9, narrowed)** — the `limine-pins` gate
   reads `hash_mismatch_panic`/`measured_boot` only from the global
   section (config.c 642-650) and reports `unverified_image_lines` for
   efi chainload entries whose image line is not a pin URI. Frozen
   battery `tools/limine-pin-battery-r91.py` reads 82/82 met ×3
   canonical and in a `git clone --shared` at the landed tip
   (`.ufo/waves/round-91/after/measured/c1-receipt-{canonical,clone}.txt`,
   `git log 6d12e07f`, `ls-remote` match). F2 oracle-import
   discrimination and freeze-manifest battery binding are **not
   established** (narrowed, not claimed); F3-unsorted is an equivalent
   mutant, not a battery blind spot. Supporting detail:
   F2-oracle-replay (`w1/CriticClaims/gates/F2-oracle-replay.py`)
   reads 80/82; F3-unsorted reads 82/82 because the gate appends in
   `sorted(image_lines)` order (check-limine-pins.py:187), making the
   deleted `unverified.sort()` (:193) redundant — `u1_ok` (battery:1683)
   requires `got_sorted == sorted(got_sorted)`, so the battery does see
   unsorted answers. The 13-line freeze manifest omits the battery.
   K2 was a broken control at freeze (duplicate
   `--tpm-present`, 984/984 `error:`), repaired in `6d12e07f` and
   re-measured 2/82 unmet ×3 canonical + clone
   (`runs-{canonical,clone}/K2-landed-adapter-fixed.*`); N10 duplicated
   N01 (byte-identical `7e158cd2…`), rewritten as a distinct whole-file
   LAST-wins bend and re-measured 78/82 unmet ×3 both layouts
   (`runs-{canonical,clone}/N10-panic-first-anywhere-fixed.*`).
2. **C2 (exploratory, depth 8, narrowed)** — knowledge entry
   `corpus/knowledge/limine-unverified-image-r91.md` + `.json`
   (S374-S376, uri.c/chainload.c/config.c tag `8ad14430…`): silent
   no-shape fail (uri.c 46-75), unhashed-but-shaped SB bypass
   (chainload.c 423-427), first-`PATH` precedence (chainload.c
   415-418), hash-mismatch prompt bypassing `panic()` (uri.c 307-314);
   host line 72 is a live instance. Upstream v12.9.5/12.9.6 invert the
   V1 first-line exception (`w1/ScoutDrift.md`); pin correct for host
   limine 12.9.4-1 only. ReviewSource CONFIRMED all clauses on a pinned
   clone; two precision notes folded into the entry (attempt-1
   uncommitted diff, D3 repair: the entry previously overstated the
   `#`-missing case as a resolve failure).

Work items (each with evidence pointer):

- **Freeze** (`d3b0987`): battery 82 families, 12 controls ×3 both
  layouts, sources pinned byte-identical
  (`.ufo/waves/round-91/before/{freeze-manifest.sha256,src/,host/receipt.txt}`,
  `before/new-ground-sweep.txt` rc=1 prior-state sweep).
- **Candidate** (`45ae6518`): V1 scoping, U1 field, S1 sanitize
  (`sanitize()` on both top-level values), dead-block removal;
  S374-S376 rows; C2 entry.
- **Measurements** (`d6f674f8`): 82/82 ×3 canonical and clone
  (`after/measured/`, receipt lines `families_passed 82/82 verdict met`
  ×6); control summaries
  (`before/controls/summary-{canonical,clone}.txt`)
  show K1 2/82 (0 errors), K2 0/82 with 984 errors and N10 81/82 —
  both PRE-repair rows kept as evidence with a post-wave repair note
  appended; the corrected `*-fixed.*` receipts carry K2 2/82 unmet and
  N10 78/82 unmet ×3 in each layout.
- **Wave w1** (13 seats, one v1 wave, `w1/results.json`): ExecReplicate
  82/82 ×3 both layouts + rc=2 on `--runs 0/-1`; ExecLints registry
  PASS; MutGate 30/38 killed; MutBattery 4/31 detected; CriticForgers
  base.py 82/82 (docstring sufficient), 23/27 killed;
  CriticClaims items 1-12 (narrowing source); ReviewSource CONFIRMED;
  ReviewGate S1 FIXED, S2 routed; ScoutURI/Chainload/Drift CONFIRMED;
  ConnectorOverlap 0 conflicts, D1-D3 C2 header/prose findings INCLUDE
  a live falsifier of the *committed* C2 header claim: `w1/ConnectorOverlap.md`
  demonstrates `uri.c:106 return true` contradicts the round-90-r90
  text repaired in the uncommitted C2 diff — the repaired text and the
  `source:`/`recheck:`/`verified-at:` headers (fixed at `6d181609`)
  are what land, never the falsified bytes; ScribeLesson mined
  R91-JUDGE-ORACLE-IMPORTABLE (a future-round battery-hardening item,
  does not falsify the C2 entry content).
- **Frontier step** (§2b): SOURCES 373 → 376 rows (S374-S376 mined;
  census start 53 lines → end 56, exit 0, see below); lesson
  `corpus/lessons/round-91.md` carries `## Mistakes` (S1-S4, one mine
  per seat finding class) and `## Gate`; sourced claim: C1 rests on
  S352 (config.c 642-650) re-opened this round, C2 on S374-S376.

## Landed changes

Every change below is committed and pushed via `jj-lane.sh` (cited
`landed <hash>` lines only):

| Change | Commit | LOG/SCORECARD row |
|---|---|---|
| Freeze, battery r91, candidate draft, controls | `d3b0987d68364ccf8b781a755cbcd9563f939468` | Round-91 declaration |
| C1 measured 82/82 ×3 canonical+clone, controls both layouts | `d6f674f8176f45ba01de9261bfabaa7e951bcef8` | Round-91 measured outcome (pre-wave) |
| V1/U1 gate fixes + registry rows + C2 knowledge entry | `45ae65181a928e3b0bdffe79afa859c6c38f03a0` | Wave w1 ReviewGate S1/S2 |
| SCORECARD measured outcome | `3d645e2cec6115d9100c22ae3e62d772f4b1faf1` | Round-91 pre-wave outcome |
| Lesson + wave receipts | `2d7e09e101996cc1ac5836c6d635f3f608453ac5` | Lesson Gate/Mistakes |
| Narrowing amendment + final measured outcome + LOG + README r91 frontier + knowledge headers | `6d181609045d539d27c566c19e1a797202405c26` | narrowing doc (original path, later moved), SCORECARD final, LOG r91 |
| Amendment at tracked path (`.ufo/plans/round-91.md`) | `1708726195a56882a648fbe455b436ecb896c5e5` | narrowing (same bytes) |
| K2/N10 control fixes as wave evidence | `6d12e07f53fecd90d38c9c088c0afe4f8d1cb079` | before/controls evidence |
| Narrowing path fix (tsv/prose → `.ufo/plans/round-91.md`) | `20f65353449169e578573a31f55fd186d812ea6c` | claim-falsification.tsv, SCORECARD, LOG, README |
| Post-wave control-fix corrections (LOG/SCORECARD/README) | `8a4826e9338a773eafb18ff89d37b53b1e707742` | final outcomes |
| Lesson M1 + canonical+clone fixed receipts | `03b773e56660380ad469490afcf001639c195a84` | lesson Mistakes M1, runs-*/\*-fixed.* |
| N10 clone receipt + summaries + lesson sync | `71fc1b6695e5d6cb04ebef8bf43a5a9d0b402cd0` | runs-clone/N10-*-fixed.*, summary notes |
| Narrowing amendment correction (F3 equivalent mutant; K2/N10 receipts) | `9df223fd85cd2201ecb6015d87c1262f3c0d47c7` | `.ufo/plans/round-91.md` |

## Before → after measurements

- **C1:** counting command `python3 tools/limine-pin-battery-r91.py
  --gate tools/check-limine-pins.py --runs 3` (canonical) + same over a
  `git clone --shared` at the landed tip. Before (K1 r90 gate): 2/82
  unmet ×3 both layouts (`before/controls/summary-{canonical,clone}.txt`
  `K1-landed-gate 2 2 2`). After: 82/82 met ×3 both layouts at
  `6d12e07f` (`after/measured/c1-receipt-{canonical,clone}.txt`);
  `git ls-remote origin refs/heads/master` =
  `9df223fd85cd2201ecb6015d87c1262f3c0d47c7` at report time. Kill rule unmet if any run
  < 82/82; void if battery/manifest differ from the freeze manifest
  *as declared* — disclosed NOT binding (manifest omits the battery;
  narrowed claim excludes it).
- **C2:** exploratory, no counting command. Verdict: `unprovable`
  pending the hyaku closure's named non-author judgment; entry rows
  re-derivable from `.ufo/waves/round-91/after/src-c2/` pins and
  `before/host/receipt.txt` line 72.

## Sources & frontier

Census command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--root /home/vgpnk/Projects/shokunin tsukuroi` — start: 53
`^tsukuroi` lines (`before/census-start.txt`), end: 56 lines incl.
`tsukuroi ok …/corpus/SOURCES.md` — exit 0 both. Rows 373 → 376
(`grep -c '^| S[0-9]' corpus/SOURCES.md` → 376 at tip), all tier A,
all `mined`, added by tier A=3, none touched old→new except the
used-by append for the new entry; frontier rows advanced: S374-S376.
Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status
--porcelain`, no pathspec): only `.scratch/*` and
`.ufo/reports/round-99/mado.md` (another lane's) — no fleet-root
misroot by this lane's seats; nothing to copy or delete.
Assimilation: none (no `merge/tsukuroi/` adoption this round;
considerthese: no still-unimplemented proposal mined — ConnectorOverlap
finds none fitting this claim set; say-so per §10).

## Trend verdicts

- **expansion:** unchanged — 3 new S-rows + 1 knowledge entry on
  genuinely new ground (URI resolution / unhashed image lines); no
  coverage score change.
- **quality:** improved — V1 visibility and U1 reporting are now
  measured by the battery (82/82 ×3 both layouts) and ReviewGate S1
  (JSON sanitize) is fixed; K2/N10 control defects repaired and
  re-measured; F2 oracle-import and freeze-manifest binding disclosed
  and narrowed, not claimed; F3 shown equivalent.
- **discernment:** unchanged — the lane downgraded its wording to
  `.ufo/plans/round-91.md` where the wave falsified it; the closure's
  independent judgment on C2 is still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SHONEN.md boxed with author-side pointers (SKILL.md:38-50 decision table, :90-141 checklist, ledger SKILL.md:5930 battery row) at tip `9df223fd`; non-author verification owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md round-91 entry at tip `9df223fd` (V1/U1 repair measured end-to-end, wave findings + repairs logged); non-author replay owed.
- [~] Instructions executable by an agent without oral context — battery docstring alone sufficed for a docstring-only re-implementation (CriticForgers base.py 82/82); whole-SKILL no-oral-context retest remains unexecuted at tip `9df223fd`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md:44-52 ADJ-01..07 + round-19 anchors unchanged; ConnectorOverlap 0 sibling conflicts at tip `9df223fd`.

## Round shape

One v1 wave of 13 seats (attack share 4/13 = 31% ≥ 25%; connector 1 ≤ 2):
ExecReplicate, ExecLints, ReviewGate, ReviewSource, MutGate, MutBattery,
CriticClaims, CriticForgers, ScoutURI, ScoutChainload, ScoutDrift,
ConnectorOverlap, ScribeLesson — seat mix per
`.ufo/waves/round-91/w1-spec.json`; 0 dead seats; WAVE-DONE received
before this report (`w1-results.json` committed at `2d7e09e1`).
Post-wave repairs (K2/N10 controls, C2 entry header + falsified
sentence) landed as wave evidence, not a second wave.

## Inherited state

Attempt 1 (`TsukuroiR91`): froze at `d3b0987`, landed candidate and
measurements, wrote SCORECARD pre-wave outcome and lesson, dispatched
w1 (13 seats, `w1.ready` + `w1.ready.dispatched` + `w1-results.json`
present), died before the report. Reused as verified above: freeze,
battery bytes (`sha256sum` of `tools/limine-pin-battery-r91.py` =
`655ee8f3…` matching the freeze header), control summaries, measured
receipts (6 × `82/82 met`), all 13 seat reports (committed at
`6d181609`), lesson S1-S4. Discarded: the attempt-1 *committed* C2
header/prose (falsified by ConnectorOverlap's uri.c:106 finding);
the D3-repaired entry text and C2 source headers in the working tree
are what landed. R90-R1..R5 routed items: R90-R1 repaired (V1), R90-R2
(R4/R6/R7/R9/R10 certified), R90-R3 roster gaps and R90-R4 remain
open (routed, see lesson).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. This
mission began 2026-11-08 (attempt 2, `TsukuroiR91a2`); activity since
launch observed continuously (lane commits above, pre-report gates
re-run); it is progressing, not silent.

## Tool installs

None. No tool was installed or upgraded this round; pacing and
routing came from the host table and the addendum.
