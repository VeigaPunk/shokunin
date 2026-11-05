# revenger — round 98 (hyaku run 15, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
- Lane head pushed: `5498390e2faf92e2bbb4fa5d35dbe50b070dbb94`. `git ls-remote origin refs/heads/main` prints the same hash.
- Landing commit (measured): `f5dc6f8e1e509b53558676d5c4be423806a38b48`.
- Claims freeze: `9d49002a3804de48d365b7d32849ada06745d64f`.
- Amendments A, B and C, each recorded before scoring: `cf8a9d4`, `0146c0a`, `1b76b4d`.
- v7 freeze: `5d9b08706aab3d310b2fa3bf9552b1e333102cb1`.
- mutate7 freeze: `af91e9d264b8a8aa2ab526b210459eae0361a55c`.

## Work performed

**Declared claims: two, on the axes coverage and calibration (`reports/round-98/claims.md`).**
- **C1 — coverage, K 13/15 → 14/15.** Row C14 (host readiness for REA routes) moves `partial → held` through a new v7 admission counter, `--profile c14`. The candidate entry is `corpus/knowledge/round-98-rea-host-readiness.md`. Verdict: **NOT VERIFIED**, an honest miss.
- **C2 — calibration.** Frozen v6 accepts 5/5 of the r97 routed holdout forgeries (FR02, FR08, FR09, FR10, FR12). The target is v7 `c02` 0/5, with both positives, the stub self-test and the row-set leg printed in one run. Verdict: **met, contested** (development set).
- **Frontier step (§2b):** a sourced claim (C1 rests on S506 and S507, both opened this round), mistakes M11–M15 mined, a census before and after, and one considerthese proposal mined. Assimilation: none.

**Wave and dispatch.** One v1 wave of 12 seats:

| Item | Value |
|---|---|
| Seats by role | executor ×3 (ExecCounterV7, ExecHarness7, ExecControls), scout ×1, scribe ×1, connector ×1, reviewer ×3 (ReviewerClaims, ReviewerGate, ReviewerBlind), critic ×1, mutation-tester ×1, sentinel ×1 |
| Attack share | 5/12 |
| Connector seats | 1 |
| Planner | held by the L1 (the validator rejects `planner`) |
| Residual call | none |
| Round total | 12 |
| Spec | `.ufo/waves/round-98/w1-spec.json` |
| Plan | `plan` rc 0 |
| Run | `run` rc 0 (`w1-dispatch.json`) |
| Handoff | `w1.ready` (dispatched) |
| Completion | `WAVE-DONE w1` received |
| Results | `.ufo/waves/round-98/w1-results.json` (12 seats) |
| Dead seats | none |

Seat-name collision: my first re-vote messages reached the *round-93* seats `ReviewerGate` and `ReviewerBlind`. Both declined and wrote nothing. The real r98 instances were `ReviewerGate-6` and `ReviewerBlind-5`, and the re-votes went to them.

**Work items and evidence pointers.**

*Domain trial (L1), 2026-11-05 on this host.* I ran three things, saved at `corpus/live/runs/round-98/` (S507):
- `rea doctor` (rea 6.7.0): exit 1, `healthy: false`, 11 healthy and 13 failing scope checks;
- the host probe transcript;
- `rea inspect-artifact corpus/fixtures/archive-r2/fixture.zip`: exit 0, Evidence `ev_0ef6c8cd…`. The members match the round-2 `truth.json`, so the ZIP route works even though doctor's overall verdict is unhealthy.

I also fetched the REA connection-and-recovery reference at `12f6e09` (S506): 16650 bytes, sha256 `ce2d122b…` (`reports/round-98/quote-receipts/`).

*Candidate entry.* The route-by-route readiness table, with each route's probe class: `corpus/knowledge/round-98-rea-host-readiness.md`.

*Pre-freeze controls* (`reports/round-98/controls/`):
- `c1-base-rowstatus.log`: 13 held, C14 partial.
- `c2-do-nothing-v6-holdout.log`: v6 accepted 5.
- The round-start census.

*Seat work:*
- **ReviewerClaims.** Seven findings (F1–F7), adopted as Amendment A before the v7 freeze (`.ufo/waves/round-98/w1/ReviewerClaims.md`). They scope `C1_USEDBY_GROUNDED`, fix the FR10 mechanism, add a second positive, and make the real-tree c02 control diagnostic only.
- **ExecCounterV7.** Built `reports/round-98/c1_k_admit_counter7.py` (sha256 `59c9930a…`) with 28 legs and `SELFTEST_C1V7=OK legs=55`. Red-before receipts are in `controls/v7-dev/`, one refusing new leg per vector. Its C1_LINT run found the candidate had no `## §Q-map`, which led to Amendment B.
- **ExecHarness7.** Built `reports/round-98/forge_reach7.py` and `forgeries7/`. Red-before on v6: `C2_ACCEPTED=5/5`, `C2_VERDICT=not-met` (`controls/v7-dev/harness-v6.log`). Before the freeze, the L1 made two integration fixes to it: the `--profile` argument index, and the same approved round-96 record supplement into the honest fixture that v7's fixture uses. Both fixes are in the frozen bytes at `5d9b087`.
- **ExecControls.** Wrote `controls/make_c1_controls.sh` and the S505 correction mirror check (`s505-*`), plus `skip-work-table-r98.md`.
- **ScoutReopen.** Re-fetched S506 byte-identical and found every derivation row MATCH. Live `rea doctor` and `inspect-artifact` are byte-identical to the committed record (zero drift). The `merge/revenger` package is still present, with 155/155 id collisions, unchanged from r97 (`.ufo/waves/round-98/w1/ScoutReopen.md`).
- **ReviewerGate / ReviewerBlind / CriticR98.** They voted on three digests (`1ea9260c…` → `73f1d7e0…` → `6d27c129…`). Superseded votes are kept in `.ufo/waves/round-98/w1/superseded-votes-digest-*`. On the final digest, Gate and Blind have 0 FAIL. CriticR98 FAILs **Q11** ("three installation paths" is not derived; the rows print 1 and 1) and **Q16** (`ghidra-version 12.1.4` is credited to the probe transcript, but only the doctor record prints it).
- **CriticR98 holdout.** 12 new forgery classes (`.ufo/waves/round-98/w1/CriticR98/fresh/`).
- **MutationR98.** Built `reports/round-98/mutants/mutate7.py`. Its v6 reproduction matches r97's tree kill of 107/140. It found that the recorded r97 self-test figure of 137/140 includes crash-artifact kills; the honest figure is 127/140.
- **ConnectorOverlap.** Adjacency with kaidoku's doctor-taxonomy entries, with no contradiction.
- **SentinelScope.** No credential material, both rows have 11 columns, census exit 0, no misroot.
- **ScribeLesson.** Drafted the lesson, which the L1 integrated as `corpus/lessons/round-98.md`.

*L1 integration:* v7 frozen, C2 scored, C1 controls and diagnostic run, holdout run on v7, mutation run, landing written, round-end diagnostics run.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `9d49002` | claims freeze: candidate entry (candidate), S506/S507, record, receipts, do-nothing controls | Round 98 |
| `cf8a9d4` | Amendment A, wave spec and dispatch | Round 98 |
| `0146c0a` | Amendment B: §Q-map added to the candidate (lint rc 0), new digest; superseded votes kept | Round 98 |
| `1b76b4d` | Amendment C: critic Q11/Q16 fixes and Q06 correction, new digest `6d27c129…`; superseded votes kept | Round 98 |
| `5d9b087` | **v7 freeze**: counter, harness (with the L1 integration fixes), forgeries7, controls, v7-dev receipts | Round 98 |
| `af91e9d` | mutate7 freeze | Round 98 |
| `f5dc6f8` | **landing**: `corpus/lessons/round-98.md`, `SCORECARD.md`, `LOG.md`, `SKILL.md` (three probe blocks), votes, controls (`c2-v7-frozen.log`, `c1-v7/`, `mutate7-*`, `selftest-v7-frozen.log`), wave evidence | Round 98 |
| `5498390` | adjudication: landing-tree c02 and v6 diagnostics, round-end census | — |

Not flipped: `corpus/README.md` (C14 stays `partial`) and the entry's `admission-status` (stays `candidate`). `git diff --stat 34c56f9 f5dc6f8 -- PROVINCE.md corpus/QUALITY.md corpus/README.md` is empty.

## Before → after measurements

| claim | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| C1 coverage K | **13/15 → 13/15** | `PYTHONUTF8=1 python3 -B reports/round-98/c1_k_admit_counter7.py --profile c14 --tree <tree>`. Diagnostic landing-like tree (C14 held, entry admitted, S505 queued): `C1_K_HELD_BACKED=14/15`, `C1_VOTES=fail` (`vote CriticR98 decision Q11='FAIL'`), `C1_VOTE_NOTES=fail` (ReviewerGate's PASS notes are under 6 tokens; ReviewerBlind's Q17 note is n/a-style), `C1_VERDICT=fail`, rc 1 (`reports/round-98/controls/c1-v7/diag-landing.log`). Do-nothing tree: 13/15, fail (`do-nothing.log`). Junk-row tree: 14/15, fail (`junk-row.log`) | `9d49002` → `5d9b087` | **NOT VERIFIED.** Kill rule: a vote FAIL. No flip |
| C2 calibration | v6 **5/5 → v7 0/5** | `PYTHONUTF8=1 python3 -B reports/round-98/forge_reach7.py --counter reports/round-98/c1_k_admit_counter7.py --profile c02 --work <scratch>` (git clone at `5d9b087`) → `C2_ACCEPTED=0/5`, `C2_POSITIVE=pass`, `C2_POSITIVE2=pass`, `C2_STUB_SELFTEST=ok`, `C2_ROWSET_FR06=C1_ADMITTED_UNION,C1_ROWSET,C1_VERDICT`, `C2_ROWSET_FR07=` the same, `C2_VERDICT=met`, rc 0 (`controls/c2-v7-frozen.log`). Before: `controls/v7-dev/harness-v6.log` (5/5, not-met); `controls/c2-do-nothing-v6-holdout.log` (accepted=5; the builder's COUNTER line was pointed at v6, see Amendment A5) | `5d9b087` | **met on the frozen predicate; contested.** This is a development-set result |
| C2 fresh holdout (reported, not the target) | c02: v6 **5/6** → v7 **5/6** accepted. c14: v7 **4/6** accepted (R01 suffix row, V02 FAIL under an extra key, O01 foreign-round pointer, L01 fetch-log date) | `build_fresh98.py --counter <v7> --profile c02\|c14 --work <scratch> --lane <lane>` (`.ufo/waves/round-98/w1/L1-holdout-v7/holdout98-v7-c14.log`, `holdout98-v7-c02-parity.log`, `holdout98-v6-c02-parity.log`). The unpatched c02 run shows `control-BROKEN` (missing round-96 records), so its 0/6 is not a discrimination result. The parity patch is `parity-patch.diff` | `5d9b087` | v7 does not generalize to the new classes |
| C02 no-harm (A1) | C02 held | v7 `--profile c02` and v6 on a clone of `f5dc6f8`: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=13/15` (`controls/measured-at-landing/c02-landing-f5dc6f8.log`, `v6-landing-f5dc6f8.log`) | `f5dc6f8` | no harm |
| self-test | — | `c1_k_admit_counter7.py --self-test` → `SELFTEST_C1V7=OK legs=55`, rc 0 (`controls/selftest-v7-frozen.log`) | `5d9b087` | pass |
| mutation (reported) | v7 tree kill c02 **173/249**, c14 **127/249** | `mutate7.py --counter reports/round-98/c1_k_admit_counter7.py --out <scratch> --kill-tree <archive 9d49002> --selftest --jobs 8 --label V7 --profile <p>` (`controls/mutate7-v7-{c02,c14}.out`) | `af91e9d` | The harness exited 3, which means the self-test baseline failed, so there is no self-test detector number. `d-host` survives. The denominator differs from r97's |

## Sources & frontier

- **Census, before** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`, base `34c56f9`): exit 0, 21 × W01, 13 × W04, 0 E-codes (`reports/round-98/controls/census-round-start.log`).
- **Census, after** (same command, lane at `f5dc6f8`): exit 0, 0 E-codes (`reports/round-98/controls/census-round-end.log`).
- **Rows:** 505 → 507 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Two rows added, both tier A:
  - S506: docs, REA connection-and-recovery reference at `12f6e09`, `mined`, opened 2026-11-05. Located quote: "Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra." (body bytes 7126–7202).
  - S507: own-work, saved round-98 record, `mined`, opened 2026-11-05. Located quote: bytes 1–41 of `rea-doctor-r98.txt`.
  - Both rows' `used-by` names the candidate entry.
- **Rows touched old → new:** none. The planned S505 correction (`mined → queued`, used-by → `—`) was **withheld**: ScribeLesson measured that it breaks C02's `C1_SOURCES` supersedes chain (S504 → S505). It is routed to r99 as a citation fix (lesson, Gate).
- **Frontier rows advanced:** none. C14 stays `partial`.
- **Sourced claim (§2b.4):** C1 rests on S506 and S507, opened this round (ScoutReopen re-opened both byte-identical).
- **Mistakes mined** (`corpus/lessons/round-98.md ## Mistakes`), with the evidence that each can fail:

| Mistake | Captured-by | Fix | Shown able to fail |
|---|---|---|---|
| M11 S505 used-by drift | none | v7 `C1_USEDBY_GROUNDED` (data fix routed) | `controls/v7-dev/usedby-base34.log`, exit 1 |
| M12 admission before closure (r97) | none | the r98 candidate stayed `candidate` | `git log` timestamps in the lesson |
| M13 r97 holdout accepted by v6 | — | v7 legs | `c2-do-nothing-v6-holdout.log` |
| M14 candidate without §Q-map; L1 did not run `corpus/lint_entry.py` before the freeze | the lint | Amendment B; lint before freeze | `controls/v7-dev/self-test-first-run.log`, exit 1 |
| M15 derivation-hygiene misses across two amendments | the critic vote | routed, not fixed this round | `c1-v7/diag-landing.log` |

- **Assimilation: none.** `merge/revenger/` is still present, and all 155/155 staged ids collide with the registry, unchanged from r97 (`.ufo/waves/round-98/w1/ScoutReopen.md` §E). The L0 lines from round 91 and round 97 are still open; nothing was adopted.
- **considerthese:** proposal 5 of `considerthese/2026-11-05.md` (adoption tracking for successor instruments) was mined into the lesson's `## considerthese` as a registry-completeness check. It was not implemented as a claim.

## Trend verdicts

- **expansion: unchanged.** No entry was admitted. The C14 candidate and two mined rows (S506/S507) were added as pending ground. K is 13/15 before and after.
- **quality: unchanged.** No admitted entry was superseded or re-verified. The candidate's defects were caught before admission.
- **discernment: improved, contested.** Two pieces of evidence:
  - The lane's gate refused the lane's own candidate on real defects. The lint caught the missing §Q-map, and the critic caught Q11/Q16; the critic's findings were re-derived by ScribeLesson.
  - v7 refuses the five routed forgeries by named legs.

  Against that, the fresh holdout shows no generalization (c02 5/6 under both v6 and v7; c14 4/6). The C2 gain is a development-set gain.

No axis was harmed. C02 is still held on the landing tree under v6 and v7 `c02`. PROVINCE, QUALITY and README are byte-unchanged.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — three round-98 probe blocks were added (`SKILL.md:622–638`) and run (`reports/round-98/controls/c2-v7-frozen.log`). No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `rea doctor` plus `rea inspect-artifact` on the archive-r2 fixture on this host (`corpus/live/runs/round-98/`; LOG.md round-98 entry). ScoutReopen reproduced both byte-identical. ScoutReopen is a lane seat, not a non-author verifier.
- [~] Instructions executable by an agent without oral context — the counter, harness and mutation commands ran from committed bytes on a clean clone (`controls/c2-v7-frozen.log`, `controls/selftest-v7-frozen.log`). No outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md is byte-unchanged. The connector found adjacency with kaidoku and no contested scope (`.ufo/waves/round-98/w1/ConnectorOverlap.md`).

## Stale-lane

No. This round progressed (8 lane commits, wave writes, measurements). No other mission of this lane is open.

## Tool installs

None. The L1 and the seats used python3 stdlib, curl, git, the lane's scripts and the installed `rea` 6.7.0 (read-only `doctor` and `inspect-artifact`; no `rea setup`). There were no pacman, uv, npx or cargo installs, and no host sysctl was touched.

## Misroot and inherited-state sweep

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time shows:
  - `.scratch/run15-kernel.py` and `.scratch/run15-state.json`: orchestrator-owned, not touched;
  - `.ufo/l0-questions.md`: other lanes' uncommitted lines, not committed by me;
  - `w4lines.txt`: names no lane or round, and predates this round (see the r97 report).

  None of these was written by this round's seats. SentinelScope's sweep agrees.
- Inherited state: there was no earlier attempt of r98, and the lane was clean at round start (`jj-lane.sh state`: ahead=0, untracked=0).
- Round-97 spot-check items (§6):

| Item | Status |
|---|---|
| 6.1 S505 | the leg landed; the data fix was withheld (harm to C02) and routed |
| 6.2 single-run C2 outputs | done (`forge_reach7` prints all of them) |
| 6.3 stale label | done (`SELFTEST_C1V7`) |
| 6.4 stub on full trees | done (`C2_STUB_SELFTEST` on built trees) |
| 6.5 admitted before closure | honoured (no flip) |
| 6.6 FR02/08/09/10/12 | done as v7 legs |
| 6.6 FR06/07 row-set leg | done (`C1_ROWSET`) |
| 6.6 M9 byte-exact quote leg | done (`C1_QUOTE_BYTES`) |
| 6.6 `d-host` | open |
| 6.6 M4 index-or-reject | open |
| 6.6 M7 SCORECARD line | open |
| 6.7 L0 | still open |

- No `corpus/lessons/operator-*.md` teaching is present.
- Scratch `/fast/scratch/hyaku/revenger-r98/` was removed after landing.

## Open items and routed work (r99)

- C14 candidate:
  - derive "three installation paths" with a command that prints 3 (Q11);
  - attribute `ghidra-version 12.1.4` to the doctor record (Q16);
  - have every voter write PASS notes of at least 6 tokens (`C1_VOTE_NOTES`);
  - re-vote, then flip through v7 `c14`.
- S505: ground it by citation, through a C02 entry revision that cites S505.
- v8 legs for the r98 holdout survivors: c02 V01, V02, E01, E02, E03 and c14 R01, V02, O01, L01.
- The mutate7 self-test baseline exit 3, and `d-host`.
- M4 `claude-red-re-bridge.md` index-or-reject.
- L0: the assimilation id collision (open).
