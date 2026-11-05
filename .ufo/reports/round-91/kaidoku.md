# kaidoku — round 91

Lane `kaidoku-shokunin`. Round 91, attempt 1, resumed twice by the orchestrator (the first attempt landed the claims and wrote the wave ready file, then parked when the driver was drained; the wave was dispatched at 07:41:53 from that ready file and this session integrated it). Base `2135f6e1d3f69a259b32cc5167c52ccb1a261c24`; declaration `deb2765a55fef0e4e81500a027dfe59951b69e87`; final instrument revision `e3ff8f01dbce8600ce3dcd368edcc4c49a4d4658`; measured revision `6d98f52b6e53a6fde52a78fb9c37df5ff5a865de`; lane tip `ee44eeb545e81f322bfcd1ec315f3df3b8008f6a`.

Declared claims, frozen before scoring (`plans/round-91-claims.md`, `.ufo/waves/round-91/claims.json`):

- **R91-C1 — coverage (capability acquisition).** The packed-ELF last-block `b_info.sz_cpr` stop-boundary class enters Core as a *measured refusal*: a packed UPX 5.2.0 `--best` LE ELF whose last block before the chain stop carries `sz_cpr` moved by ±7 is refused with rc 2 and no output unless `upx -t` on the input is green, in which case the input is returned byte-identical.
- **R91-C2 — depth.** `SKILL.md`'s `## Queue-drain craft` gains rule block 31, a decision table routing the three measured base failure classes of that tamper to the guard that answers each, shape-floored from block 31 by a new counter.

## Work performed

- **Frozen before data.** `plans/round-91-claims.md` and `.ufo/waves/round-91/claims.json` pin the predicates, labels, kill rules, counter paths, carrier and packer pins and instrument sha256 values at `deb2765a`. Pre-declaration scratch probes are kept as exploratory evidence (`pre/probes/probe-t7.py`, `probe-cls.py` and outputs), not as receipts.
- **The defect the claim repairs, measured at base.** At `2135f6e1d` the unchanged round-90 repair answers `rc 0` on all eight last-block cells: two write bytes outside the tampered window (the sentinel word at jq 10094-10097 and libz 60124-60127), six return a file `upx -t` still rejects, none is refused — `pre/c1-base-round90-repair.json`, `refused 0 of 8; unsafe 2; intact 4 of 4`, exit 1.
- **Candidate capability.** `tools/round-91/upx-stop-boundary-repair.py` changes one branch of the round-90 repair: when no successor decides the walk it runs `upx -t` on its input, returns identity on green and refuses with rc 2 and no output file on red. Composes the round-87/88/89/90 modules by absolute path.
- **C1 measured at the final revision.** `tools/round-91/stop-boundary-battery.py` → `refused 8 of 8; unsafe 0; intact 4 of 4`, exit 0 (`l1/scores/c1-at-6d98f52b.json` at the measured revision; identical label at `e3ff8f01` and `04ba98f9`); the per-cell records show rc 2 with no output file on every tampered cell and byte-identical output on all four intact carriers.
- **Regression arm at the same revision.** The round-90 battery with the new repair → `P1 6 of 6; P2 4 of 4; P3 4 of 4`, exit 0, all eight controls true (`l1/scores/c1-regression-at-e3ff8f01.json`, also met at `04ba98f9` and `deb2765a`): the interior, block-0 and magic classes keep their repairs.
- **Cheap rules measured by an independent seat.** Wave seat `ExecCandidate` built variants in a scratch clone at the declaration commit and scored them with the frozen counter: blanket refusal `refused 8 of 8; intact 0 of 4`; geometry as specified `refused 8 of 8; intact 3 of 4`; geometry-pure `refused 3 of 8; intact 3 of 4`. None reaches the label (`w1/ExecCandidate/c1-variant-*.json`), and the seat reproduced both frozen arms cell for cell.
- **C2 depth.** Block 31 added to `SKILL.md` (`stop-boundary-refusal-table v1`): three routed rows, each citing a `QUALITY.md` row and a knowledge document present at base (QUALITY 159). `tools/round-91/depth-blocks-v3.py` adds a decision-table clause for blocks at or after `--shape-from 31`; `--prose-proof` kills the prose fixture the shape-blind predecessor accepts (`l1/scores/c2-prose-at-e3ff8f01.json`, `control_killed true`).
- **Sources.** S313 (`src/p_unix.cpp`, UPX v5.2.0) re-opened this round; the decoder's only per-block arithmetic bound read at line 496. Entry `corpus/knowledge/2026-11-05-r91-stop-boundary-refusal.md`. Wave seat `ScoutSource` independently re-fetched the file (HTTP 200, 24181 B, same sha256), resolved the tag to commit `034b6d0d…`, proved the tag URL and commit URL byte-identical, and recorded `master` drift for the row's recheck field.
- **Adversarial review, in wave.** `ReviewerRepair` (no HIGH; MED-1 refusal-class rc mapping fixed), `ReviewerFalsify` (falsified the impossibility premise — see below), `SentinelWrite` (no HIGH; MED-1 cost recorded as QUALITY 183; MED-2 write-ordering fixed), `MutCounter` (mutant table; three survivors reported as a named limit), `CriticClaims` (falsification report; findings folded in below), `ConnectorOverlap` (no sibling lane claims the class).
- **Two instrument supersessions, both found by the wave and disclosed in the container.** (1) ReviewerRepair MED-1: the round-90 module's own `Refused` escaped to rc 1; now both refusal classes are qualified (`b0zero` repro rc 1 → rc 2). (2) SentinelWrite MED-2: `--info` was written after `--out`, so a refused info path answered rc 2 with the output on disk; now both targets are validated before the first write (repro rc 2 with no output). The frozen label was met before and after each; both are recorded in `claims.json` `instrument_supersessions` with their reasons and reproductions.
- **Calibration diagnostic (not a claim).** `tools/round-91/record-cells.py` re-derives the round-89/90 claim rows from committed bytes: `mismatches 5` at base (`pre/c3-at-base.json`) → `mismatches 1` at the final revision (`l1/scores/c3-at-e3ff8f01.json`), the remainder being R89-C1's receipts, which carry no revision field at all (a historical defect that cannot be repaired without rewriting a receipt). D-5's placeholder and directory pointer are pinned in place; R89-C2's after-receipt is pinned.
- **Round-90 routed defects.** D-1, D-3, D-5 answered by the LOG correction entry and the pinned rows; D-4 by the registry rows for the three round-90 tools and the four round-91 instruments; D-2 and D-6 by this report's shape and tables.
- **Registry and criteria.** `corpus/QUALITY.md` gains rows 178-183; PROVINCE gains a round-91 Core section (refusal only; the repair stays Frontier); corpus README gains a coverage row, an index row, a lesson row and a frontier note.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `plans/round-91-claims.md`, `.ufo/waves/round-91/claims.json`, `tools/round-91/` (four instruments), `SKILL.md` block 31 + registry rows, `pre/` receipts | `## 2026-11-05 — round 91` (declared claims) | `deb2765a55fef0e4e81500a027dfe59951b69e87` |
| knowledge entry, lesson, QUALITY 178-181, README rows, PROVINCE section, LOG round-91 + correction entries, SCORECARD round-91 + correction row, wave spec/dispatch/ready | `## 2026-11-05 — round 91` and `## 2026-11-05 — round 91 correction of the round-90 record` | `f7f5153b393c8057639aafb3a85f0cd9a9be61a5` |
| regression receipt at declaration | `## 2026-11-05 — round 91` (regression arm) | `fe1913d90a3774020bab129f4c8cc5bc10daa523` |
| MED-1 refusal-class fix (supersession 1), entry corrections, D-5/R89 pins, QUALITY 178-182 | `## 2026-11-05 — round 91` (wave findings) | `04ba98f900b3874c191dbcbec731fddd04b02278` |
| MED-2 write-ordering fix (supersession 2), QUALITY 183, container supersession record | `## 2026-11-05 — round 91` (wave findings) | `e3ff8f01dbce8600ce3dcd368edcc4c49a4d4658` |
| final receipts, wave seat evidence (`r91-w1-results.json`), census receipts, lesson wave section | `## 2026-11-05 — round 91` (wave findings) | `86bcdad988dfcbc4bac6ea02b935411108cc9e3e`, `6d98f52b6e53a6fde52a78fb9c37df5ff5a865de`, `ee44eeb545e81f322bfcd1ec315f3df3b8008f6a` |

## Before → after measurements

**R91-C1 (coverage).** Counting command, run at the named revision:

```sh
python3 -I -B tools/round-91/stop-boundary-battery.py --root . \
  --repair-cmd tools/round-91/upx-stop-boundary-repair.py --work <scratch> \
  --rev 6d98f52b6e53a6fde52a78fb9c37df5ff5a865de \
  --expect "refused 8 of 8; unsafe 0; intact 4 of 4" --json-out <receipt>
```

| arm | before (`2135f6e1d`, round-90 repair) | after (`6d98f52b`, round-91 repair) |
|---|---|---|
| refused | 0 of 8 | 8 of 8 |
| unsafe (bytes outside the window) | 2 | 0 |
| silent (rc 0, broken file unchanged) | 6 | 0 |
| intact identity | 4 of 4 | 4 of 4 |
| regression `P1/P2/P3` | `P1 6 of 6` at round 90 | `P1 6 of 6; P2 4 of 4; P3 4 of 4`, all controls true |

**R91-C2 (depth).**

```sh
python3 -I -B tools/round-91/depth-blocks-v3.py --root . --rev 6d98f52b6e53a6fde52a78fb9c37df5ff5a865de \
  --expect-blocks 31 --expect "blocks 31, resolved 31, required-shaped 1/1" --json-out <receipt>
```

Before (`2135f6e1d`): `blocks 30, resolved 30, required-shaped 0/0`, met false (`pre/c2-depth-at-base.json`). After (`6d98f52b`): `blocks 31, resolved 31, required-shaped 1/1`, met true (`l1/scores/c2-at-6d98f52b.json`). The shape-blind predecessor accepts the prose fixture that v3 refuses (`control_killed true`).

**Calibration diagnostic (not claimed).** `record-cells.py --rounds 89 90`: `mismatches 5` at base → `mismatches 1` at `6d98f52b` (R89-C1 A3 only; its receipts carry no revision field).

## Sources & frontier

Census command, run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

| | rows | tier A | tier B | tier C | mined | rejected | exit |
|---|---|---|---|---|---|---|---|
| before (round start) | 221 | 201 | 11 | 9 | 197 | 24 | 0 |
| after (round end) | 221 | 201 | 11 | 9 | 197 | 24 | 0 |

Receipts: `.ufo/waves/round-91/l1/census-before.txt`, `census-after.txt`, `census-after-counts.txt`. The end run reports 7 W04 duplicate-URL warnings (S276, S298, S299, S300, S303, S311, S316) and `ok`; none is new or touched this round.

- Rows added by tier this round: **none**. The round re-grounded an existing row rather than opening a new one; no source was read that the registry lacked.
- Rows touched old → new: S313 `used-by` `corpus/knowledge/2026-11-04-r90-interior-block-szcpr.md` → `corpus/knowledge/2026-11-04-r90-interior-block-szcpr.md, corpus/knowledge/2026-11-05-r91-stop-boundary-refusal.md`; `status` `mined` → `mined`; `recheck` `on-release` → `on-release`; `opened` unchanged (2026-11-04), the 2026-11-05 re-open recorded in the lesson's Gate. Logged in `corpus/lessons/round-91.md` `## Gate`.
- Frontier rows advanced: PROVINCE "the last block before a chain stop" moves from *Frontier, under-determined* to *Core as a measured refusal*; the **repair** of that class, the self-resuming suffix, the `libz` `u_len` gap, `p_filesize`/`p_blocksize`/adler repairs, 32-bit carriers and `--lzma` output stay Frontier.
- Assimilation: none — this lane has no `merge/kaidoku/` package and no `considerthese/` directory.
- Sourced claim: R91-C1's knowledge entry rests on S313, re-opened 2026-11-05 (HTTP 200, 24181 B, sha256 `bf83c413…642e`, line 496 quoted in the lesson's Gate; independently re-fetched by seat `ScoutSource`).

## Trend verdicts

- **expansion — improved.** A knowledge entry on ground the coverage map did not hold (the last block before a chain stop), citing S313 re-opened this round; PROVINCE and the corpus frontier note move that class from Frontier to Core-as-refusal. Stated honestly: the registry did not grow (221 → 221) and the class is a refused boundary, not a new repair.
- **quality — improved, with measured limits.** Two counter arms the round-90 counter lacked (unsafe and silent writes) plus an intact control; a shape clause that kills a prose control the predecessor accepts; six QUALITY criteria added (178-183), three of them from this round's own defects; two instrument defects found by the wave were fixed and disclosed as supersessions. Named limits, all measured by the wave: (i) the frozen label admits two cheats — a carrier-reading repair and a hash-table repair both pass `refused 8 of 8; unsafe 0; intact 4 of 4` and the regression label (`w1/CriticClaims.md` ATTACK-2); (ii) the `refused` arm is "nonzero, no output", so an rc-1 exit passes where the description says rc 2 — every scored cell is rc 2 per cell (`l1/scores/c1-at-e3ff8f01.json`) but the label does not assert it; (iii) three counter mutants survive against the candidate (unsafe scoring removed, intact arm forced true, isolation listing moved), so the label's discrimination rests on `refused`/`intact` (`w1/MutCounter/mutant-M{1,2,3}-*.json`); (iv) the depth counter certifies a block's shape and its `corpus/knowledge/` citations, not its QUALITY-row citations or its routing, so a ghost criterion row still scores `met True` (`w1/CriticClaims.md` ATTACK-6/7); (v) block 31's third row mis-cites QUALITY 169 — disclosed, not repaired, because the C2 kill rule makes any post-declaration edit of block 31 a failure; (vi) the intact arm depends on `upx -t` on the input, and a label-less exit 0 is not a pass (a missing `--work` dir is `unevaluable`).
- **discernment — mixed, and reported as such.** Improved: the attack seats found six real defects in this round's own work (M91-5, M91-7, ReviewerRepair MED-1, SentinelWrite MED-1/MED-2, and the block-31 mis-citation); three were closed before landing and three are disclosed. Harmed at the level of justification and of measurement power: `ReviewerFalsify` showed the claim's premise "the class is not decidable" is false — `upx -t` is a decision procedure on all eight cells — so the refusal is policy, not necessity (M91-8, QUALITY 182); and `CriticClaims` showed the frozen label admits two cheats and an rc-1 exit, so the label measures "refused without output" rather than "typed rc-2 refusal by the intended mechanism". Both claims remain **met under their frozen predicates**; admission is the non-author verifier's, and the label amendments (rc assertion, cheat arms, QUALITY-row resolution) are routed to round 92 rather than applied to a frozen predicate.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — block 31 added with three routed rows citing base-present criteria, scored `required-shaped 1/1` by `tools/round-91/depth-blocks-v3.py` (`l1/scores/c2-at-6d98f52b.json`). Evidence pointer, not a named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the stop-boundary class measured end to end at `6d98f52b` (battery, regression arm, two independent seats) and logged in the round-91 LOG entry; closure admission is the non-author verifier's.
- [~] Instructions executable by an agent without oral context — both counters, their selftests, `--prose-proof` and the repair's `--selftest` run from the lane; seat `ExecSelftests` ran all eight commands in the lane and in a declaration clone with identical exits.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the new Core section is packed-ELF ground only; the sibling sweep (`w1/ConnectorOverlap.md`) finds no lane claiming the class and one shared-primitive adjacency (`record-cells`' `git cat-file -t == blob`, also used by tameshi's live round-87).

Stale-lane: respawn-per-round driver; no other mission of this lane is open. This is the lane's 91st steered round of the campaign to 100.

Tool installs: none by the L1 or any seat (no pacman, no `uv tool`, no binary installs). `upx` 5.2.0 (`/usr/bin/upx`, sha256 `cf2f6e7c…c969`) and REA 6.5.0 (`ad9a3fdbcad992c6`) were already present and are pinned in the container.

L0 questions: none this round. The one coordination question (whether the drained driver was holding the ready file) was answered by the orchestrator in-session.

Round shape: one v1 wave `r91-w1`, 12 spawn seats, handoff `.ufo/waves/round-91/r91-w1-results.json` (executor 3, reviewer 2, critic 1, mutation-tester 1, sentinel 1, scout 1, scribe 2, connector 1); attack 4/12 = 33 %; one connector; no planner (the L1 holds that seat); no residual call, no second wave. Dead seats: none — all twelve seats report; `CriticClaims` and `MutCounter` settled last.
