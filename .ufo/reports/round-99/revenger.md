# revenger — round 99 (hyaku run 15, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
- Lane head pushed: `3c707c8af83020f9a9bd5491efe70be3d5456230`. `git ls-remote origin refs/heads/main` prints the same hash.
- Landing commit (measured): `250dd8f3c9dffee4112e2316ba9e778b813e8df9`.
- Claims freeze: `7e6edd4db649f99c425daa46a91edbbd18a6e27c`.
- Amendment A: `61e27feb4e8099af7f9bf41fbf69e223354f691e`. Amendment B, the single candidate amendment: `9ddd38ac8baef67d689ac36fa233aaaef35b1703`. Both were recorded before the v8 freeze and before any landing-tree scoring.
- v8 freeze: `01266760d9918b868f7cd8a25dd5cf6e1052d193`.

## Work performed

**Declared claims: two, on the axes coverage and calibration (`reports/round-99/claims.md`).**
- **C1 — coverage, K 13/15 → 14/15.** Row C14 (host readiness for REA routes) moves `partial → held` through the new v8 counter, run as `--profile c14r99`. The entry is the round-98 candidate `corpus/knowledge/round-98-rea-host-readiness.md`, with the r98 closure's routed defects fixed. Verdict: **met on the frozen counter**. Admission is pending the non-author closure.
- **C2 — calibration.** Frozen v7 accepts 9/12 of the round-98 fresh holdout vectors (c02: V01, V02, E01, E02, E03; c14: R01, V02, O01, L01). Target: v8 accepts 0/12, with both builder controls `control-ok`, the stub self-test ok and twelve per-vector lines, all in one run. Verdict: **met, contested.** This is a development-set result.
- **Frontier step (§2b):**
  - Sourced claim: C1 rests on S506, re-opened this round at its pinned revision and byte-identical, and on S507, re-hashed this round and re-produced live.
  - Mistakes M16–M20 mined.
  - Census taken before and after.
  - considerthese proposal 4 mined.
  - Assimilation: none.

**Wave and dispatch.** One v1 wave of 12 seats:

| Item | Value |
|---|---|
| Seats by role | executor ×3 (ExecCounterV8, ExecHarness8, ExecControlsR99), scout ×1 (ScoutReopenR99), scribe ×1 (ScribeLessonR99), connector ×1 (ConnectorR99), reviewer ×3 (ReviewerClaimsR99, VoterGateR99, VoterBlindR99), critic ×1 (CriticR99), mutation-tester ×1 (MutationR99), sentinel ×1 (SentinelR99) |
| Attack share | 5/12 |
| Connector seats | 1 |
| Planner | held by the L1 (the validator rejects `planner`) |
| Residual call | none |
| Round total | 12 |
| Spec | `.ufo/waves/round-99/w1-spec.json` |
| Plan | `plan` rc 0 |
| Run | `run` rc 0 (`w1-dispatch.json`) |
| Handoff | `w1.ready`, marked `.dispatched` |
| Completion | `WAVE-DONE w1` received |
| Results | `.ufo/waves/round-99/w1-results.json`, 12 seats |
| Dead seats | none |

Seat names carry a round suffix (VoterGateR99 and so on). That avoided the r98 cross-round name collision (M18). VoterGateR99 and VoterBlindR99 were parked when the re-vote message reached them; both revived and re-voted.

**Work items and evidence pointers.**

*L1, before the freeze:*
- Fixed the candidate's Q11 defect: the paths are now counted, not the lines (`reports/round-99/controls/q11-paths-old-vs-new.log`: the old command prints 1, the new one prints 3).
- Fixed the Q16 defect: 12.1.4 is credited to the doctor record (`q16-version-attribution.log`).
- Lint rc 0 (`lint-candidate-freeze.log`).
- Re-fetched S506 at its pinned revision. It is byte-identical to the committed body (`reports/round-99/quote-receipts/S506-reopen-r99.txt`).
- Ran the C2 do-nothing control on frozen v7: 9/12 accepted, both controls ok (`controls/c2-do-nothing-v7-holdout98-{c02,c14}.log`).
- Round-start census (`controls/census-round-start.log`).

*Seat work:*
- **ReviewerClaimsR99** sent F1–F4 (`.ufo/waves/round-99/w1/ReviewerClaimsR99.md`). F1 was a blocker: v7/v8 `c14` check S505's `used-by`, and that cell named an entry which never cites S505, so C1 could not be reached. This led to Amendment A: S505's `used-by` was grounded by citation to `corpus/lessons/round-97.md`. A scratch run showed v7 `c02` still passes, so C02 is not harmed (`controls/amendA-s505-scratch.log`).
- **VoterGateR99** voted Q16 FAIL on digest `36cc6ac2…`, because one output cell was not the command's stdout. **CriticR99** found the same class, plus the S507 "exit 1" cell and four smaller derivation gaps. **ScoutReopenR99** independently found the same class in its §3 and G1.
  - All of this went into Amendment B. The cell rule was made verbatim, and the derivation table was regenerated with 29 rows. The S507 `teaches` cell was fixed.
  - A new `controls/deriv_check.py` re-runs every derivation row. It reports 7 mismatches on the claims-freeze entry and 0 on the amended one (`controls/amendB-deriv-check.log`).
  - The new digest is `246d09a8…`. The superseded votes are kept in `.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/`.
- **Votes on `246d09a8…`** (`reports/round-99/votes/`), 0 FAIL in total:
  - VoterGateR99: 10 PASS, 7 n/a, 0 FAIL;
  - VoterBlindR99: 11 PASS, 6 n/a, 0 FAIL;
  - CriticR99: 12 PASS, 5 n/a, 0 FAIL.
- **ExecCounterV8** built `reports/round-99/c1_k_admit_counter8.py` (sha256 `620dfca9…`). It adds the `c14r99` profile and nine new named legs (C1_VOTES_GLOB, C1_NA_REASON, C1_RECHECK_CMD, C1_HEX_CLAUSES, C1_COVMAP_ROW, C1_ROW_IDS, C1_DECISION_KEYS, C1_OWNWORK_ROUND, C1_FETCHLOG_DATE). Self-test: `SELFTEST_C1V8=OK legs=98`. Red-before receipts are in `.ufo/waves/round-99/w1/ExecCounterV8/`.
- **ExecHarness8** built `reports/round-99/forge_reach8.py` (sha256 `0a393136…`). The builder and the parity patch are pinned by hash, and the harness fails closed. On v7 it reproduced the per-vector 9/12 result.
- **ExecControlsR99** wrote `controls/make_c1_controls_r99.sh` and `controls/skip-work-table-r99.md`.
- **MutationR99** built `reports/round-99/mutants/mutate8.py` and `mutants-r99.json`, which it pre-registered.
  - It reconciled r98 routed defect 5: mutate7 matched `=pass`, but the counter prints `=OK`. mutate8 fixes that, and a forced-FAIL copy still exits 3.
  - On v8: `MUTANT_KILL_V8=154/309` (tree) and `MUTANT_SELFTEST_V8=285/309`. `d-host` is killed by the self-test only.
- **ScoutReopenR99** re-ran every derivation row, re-fetched S506, and re-ran `rea doctor` (rc 1) and `rea inspect-artifact` (rc 0) live. Both live outputs are byte-identical to the r98 record. It also measured the assimilation collisions at 155/155.
- **ConnectorR99:** sibling-overlap scan, with no contradiction. It forwarded reusable leg rules to ExecCounterV8.
- **SentinelR99:** 0 credential-shaped secrets, no misroot, census rc 0.
- **ScribeLessonR99** drafted the lesson, which the L1 integrated as `corpus/lessons/round-99.md`.

*L1, after the v8 freeze* (clean clone at `01266760`; receipts in `reports/round-99/controls/post-freeze/`):
- C1 controls;
- the C2 run;
- the no-regression runs;
- the self-test;
- the fresh r99 holdout, run once;
- the landing flip, scored on the working tree and then on the landing archive;
- the C02 diagnostics;
- the round-end census.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `7e6edd4` | claims freeze: candidate Q11/Q16 fixes (digest `36cc6ac2`), S506/S507 re-open receipts, pre-freeze controls | Round 99 |
| `61e27fe` | Amendment A: S505 `used-by` grounded by citation; wave spec and dispatch | Round 99 |
| `9ddd38a` | Amendment B: verbatim derivation cells (29 rows), S507 `teaches` fix, `deriv_check.py`; digest `246d09a8`; superseded votes kept | Round 99 |
| `0126676` | **v8 freeze**: counter, forge_reach8, controls script, skip-work table, mutate8, votes, wave evidence | Round 99 |
| `250dd8f` | **landing**: C14 `held` (`corpus/README.md`), entry `admission-status: admitted`, `corpus/lessons/round-99.md`, `SCORECARD.md`, `LOG.md`, `SKILL.md` (four registry blocks), post-freeze receipts, round-end census | Round 99 |
| `3c707c8` | landing-archive measurements (`post-freeze/landing-archive-*.log`) | — |

## Before → after measurements

| claim | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| C1 coverage K | **13/15 → 14/15** | `PYTHONUTF8=1 python3 -B reports/round-99/c1_k_admit_counter8.py --profile c14r99 --tree <git archive 250dd8f3>` → `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0 (`post-freeze/landing-archive-c14r99.log`). Before: `controls/c1-base-rowstatus.log` (13 held, C14 partial at `3d054a98`). Controls (`make_c1_controls_r99.sh`, `post-freeze/c1-controls.out`): do-nothing `fail` (rc 1), junk-row `fail` (rc 1) | `7e6edd4` → `0126676` (v8) → `250dd8f` | **met on the frozen counter**; admission pending the non-author closure |
| C2 calibration | v7 **9/12 → v8 0/12** | `PYTHONUTF8=1 python3 -B reports/round-99/forge_reach8.py --counter reports/round-99/c1_k_admit_counter8.py --work <scratch>` (clone at `0126676`) → twelve `C2_VECTOR … refused` lines, each naming its leg; `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-ok`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`, rc 0 (`post-freeze/c2-v8-frozen.log`). Before: `controls/c2-do-nothing-v7-holdout98-{c02,c14}.log` | `0126676` | **met on the frozen predicate; contested** (development set) |
| C2 fresh r99 holdout (reported, not the target) | v7 12/12 → v8 **12/12** accepted | CriticR99 `build_fresh99.py --counter <v8> --profile c02\|c14` (`post-freeze/holdout99-v8-{c02,c14}.log`; v7 logs in `.ufo/waves/round-99/w1/CriticR99/fresh/`) | `0126676` | v8 does not generalize to the new classes |
| No regression (reported) | r98 dev set 0/5 kept | `forge_reach7.py --counter <v8> --profile c02` → `C2_ACCEPTED=0/5`, both positives pass (`post-freeze/noreg-forge7-v8-c02.log`). `--self-test` → `SELFTEST_C1V8=OK legs=98`, rc 0 | `0126676` | no harm |
| C02 no-harm (reported) | C02 row byte-identical | v8 `c02` on the landing archive fails `C1_ONLY_TARGET` (diff C14 only) **and** `C1_K_HELD_BACKED` (K 14 vs the profile's pinned 13) (`post-freeze/landing-archive-c02-diag.log`). The frozen diagnostic rule named only the first leg, so **the rule as written is not met** (M19). The landing tree with only the two C14 flip lines reverted passes both v8 and v7 `c02` (K 13/15, rc 0; `post-freeze/landing-c14unflipped-c02{,-v7}.log`) | `250dd8f` | C02 unharmed on its own legs; the diagnostic-rule miss is disclosed |

## Sources & frontier

- **Census, before** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`, base `3d054a98`): exit 0; 21 × W01, 13 × W04, 0 E-codes (`reports/round-99/controls/census-round-start.log`).
- **Census, after** (same command, landing tree): exit 0; 21 × W01, 0 E-codes (`reports/round-99/controls/census-round-end.log`).
- **Rows:** 507 → 507 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Rows added: none.
- **Rows touched old → new** (logged in `corpus/lessons/round-99.md` `## Gate`):
  - S505 `used-by`: `corpus/knowledge/round-96-native-analysis-sessions.md` → `corpus/lessons/round-97.md` (Amendment A; grounded by citation, status stays `mined`);
  - S507 `teaches` fragment: "(CLI 6.7.0, exit 1)" → "(CLI 6.7.0; its exit code 1 was observed in the L1 session and is not a line of the record)" (Amendment B).
- **Re-opened this round:**
  - S506 at its pinned revision: 2026-11-05T18:43:20-03:00, http 200, 16650 bytes, sha256 `ce2d122b…`, byte-identical, quote count 1. ReviewerClaimsR99 and ScoutReopenR99 re-fetched it independently and got identical bytes.
  - S507: the three records re-hashed equal. Live `rea doctor` and `rea inspect-artifact` outputs are byte-identical to them.
- **Frontier row advanced:** C14 `partial → held` (pending closure).
- **Sourced claim (§2b.4):** C1 rests on S506 and S507, both re-opened this round.
- **Mistakes mined** (`corpus/lessons/round-99.md` `## Mistakes`), each with evidence that it can fail:

| Mistake | Shown able to fail |
|---|---|
| M16 count by lines | `q11-paths-old-vs-new.log`: 1 vs 3 |
| M17 version attribution | `q16-version-attribution.log` |
| M18 cross-round seat-name collision | `ScribeLessonR99/m18-seat-name-collision.txt` |
| M19 no-harm rule copied without re-deriving it for a K move | `post-freeze/landing-c02-diag.log` vs `landing-c14unflipped-c02.log` |
| M20 hand-normalized output cells | `amendB-deriv-check.log`: 7 → 0 |

- **Assimilation: none.** `merge/revenger/` is present, and 155/155 of its staged ids collide with the 507-row registry (ScoutReopenR99, `collision-check-r99.log`). The L0 question is still open, and nothing was adopted.
- **considerthese:** proposal 4 of `considerthese/2026-11-05.md` (upstream drift watch) was mined into the lesson. The lane's own bar refuses it as a daily tracker. It is re-landed as a proposed producer-attribution census, with measurements: 15 live records name `rea 6.8.0`, while both doctor records say 6.7.0. It was not implemented as a claim.

## Trend verdicts

- **expansion: improved.** C14 is held on the frozen v8 counter, and the host-readiness entry is admitted pending the closure (K 13 → 14).
- **quality: improved.**
  - S505 `used-by` is grounded by citation: the r97/r98 routed defect is closed without harm to C02.
  - The S507 `teaches` cell no longer credits the record with an exit code it does not print.
  - The entry's 29 derivation rows are verbatim and machine-checked by `deriv_check.py` (0 mismatches).
- **discernment: improved, contested.**
  - v8 refuses all nine routed r98 survivors by named legs, with both controls ok.
  - The lane's gate refused its own candidate again on a real Q16 defect, found by three seats independently.
  - Against that: the fresh r99 holdout is accepted 12/12 by v8, so the C2 gain is a development-set gain.

No axis was harmed on its own legs. C02 is unharmed: its legs pass on the landing tree minus the C14 flip. The c02 diagnostic rule as frozen was not met by construction; this is disclosed above and recorded as M19. PROVINCE and QUALITY are byte-unchanged.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — four round-99 registry blocks were added (`SKILL.md:640–662`), and each entry command was run this round (`reports/round-99/controls/post-freeze/`, `amendB-deriv-check.log`). There is no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — ScoutReopenR99 re-ran `rea doctor` (rc 1) and `rea inspect-artifact` on `fixtures/archive-r2` (rc 0) live, byte-identical to `corpus/live/runs/round-98/` (`.ufo/waves/round-99/w1/ScoutReopenR99.md` §5; LOG.md round-99 entry). ScoutReopenR99 is a lane seat, not a non-author verifier.
- [~] Instructions executable by an agent without oral context — the counter, harness, controls script and `deriv_check.py` ran from committed bytes on a clean clone at `0126676` (`post-freeze/*.log`). There is no outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md is byte-unchanged. ConnectorR99 found no contested scope (`.ufo/waves/round-99/w1/ConnectorR99.md`).

## Stale-lane

No. This round progressed: 6 lane commits, wave writes and measurements. No other mission of this lane is open.

## Tool installs

None. The L1 and the seats used python3 stdlib, curl, git, the lane's scripts and the installed `rea` 6.7.0 (read-only `doctor` and `inspect-artifact`; no `rea setup`). There were no pacman, uv, npx or cargo installs, and no host sysctl was touched.

## Misroot and inherited-state sweep

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time shows:
  - `.scratch/run15-kernel.py` and `.scratch/run15-state.json`: orchestrator-owned, not touched;
  - `w4lines.txt`: predates this round (see the r97/r98 reports);
  - untracked `C1_pagliai.pdf` … `C13_norse_lsu.pdf` and `C10`/`C11`/`C3`/`C6` `.html` files: verbal-duel and flyting sources that name no revenger content. They belong to another lane, so they are not this round's misroots and were not touched.

  SentinelR99's sweep found no revenger/round-99 misroot.
- Inherited state: there was no earlier attempt of r99 (`watchdog.log` shows only `launch revenger round=99 … attempt=1`), and the lane was clean at round start (`jj-lane.sh state`: ahead=0, untracked=0).
- One L1 process slip: I ran `git mv -k` on two untracked vote files, which is a disallowed git command. With `-k` it skipped the untracked files and changed nothing. `git diff --cached --stat` was empty, and the files were then moved with plain `mv`. No index or jj state was affected.
- Round-98 spot-check items (§5):

| Item | Status |
|---|---|
| 1 Q11 paths | done (row counts paths; prints 3) |
| 2 Q16 attribution | done, then re-amended (Amendment B) after a fresh Q16 FAIL |
| 3 vote notes | done (0 FAIL; v8 `C1_VOTE_NOTES` passes on the landing tree) |
| 4 S505 grounding | done by citation (Amendment A), C02 unharmed |
| 5 mutate7 baseline exit 3 | reconciled (regex `=pass` vs `=OK`); `d-host` killed by the self-test only |
| 6 v8 legs for the r98 survivors | done (C2 0/12) |
| 7 M4, M7, L0 | M4 and L0 still open; M7 not addressed |

- No `corpus/lessons/operator-*.md` teaching is present.
- Scratch `/fast/scratch/hyaku/revenger-r99/` was removed after landing; `ls /fast/scratch/hyaku | grep -c revenger-r99` printed 0.

## Open items and routed work (r100)

- The fresh r99 holdout: 12 classes accepted by v8 (`.ufo/waves/round-99/w1/CriticR99/fresh/`). One of them, C14-N3 (an edited derivation count), is refused by `deriv_check.py` but by no counter leg.
- The entry's §Q-map Q13 rationale is stale against the new Q11/Q16 credits (VoterBlindR99 observation). No amendment remained this round.
- `d-host` survives the tree detector.
- M4: `claude-red-re-bridge.md` index-or-reject.
- The producer-attribution census (considerthese proposal 4).
- L0: the assimilation id collision (open).
