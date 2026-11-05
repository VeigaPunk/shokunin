# tameshi — round 87 (hyaku run 15, attempt 1)

Lane: `tameshi-shokunin` (verification-fixture craft). L1: `TameshiR87`.
Base `4a079f6ab57ab2f47b9e502a35eca75ec180cda7` (round-86 tip). Freeze `1d5102a1`.
Lane HEAD at this report: `d91971194f6e1d12cdcbed3e22bb4ed8857109bd`
(`git ls-remote origin refs/heads/master` prints the same hash; `jj-lane.sh state`: `ahead=0 tracked=0 untracked=0`).
Lesson: `corpus/lessons/round-87.md`. Ledger entry: `LOG.md` "Round 87 (2026-11-05)".

## Work performed

Declared claims (frozen at `1d5102a1` before any after-state data; `plans/round-87.plan.md`):

- **R87-C1 — operability, capability acquisition.** Successor certification counter for
  `tools/design-blob-audit.py` (`.ufo/evidence/round-87/measure.py`). Target: real instrument
  `C1_R87 … passed=8/8`, every frozen control below 8/8. **Verdict: killed.**
- **R87-C2 — calibration (lowest scored axis: calibration 8 of depth 10 / calibration 8 / freshness 9).**
  Census v2 (`tools/capability-census-v2.py`) refuses overreach: tree, symlink, uncited and
  path-with-line pins. Target: overreach population `bound=0`, real population `30/30`.
  **Verdict: killed** (by a real-population overreach the rule forbids; see below).

Work items with evidence:

- Pre-freeze instruments committed at `a3b4f75d`: `measure.py`, the seven controls
  (`.ufo/evidence/round-87/controls/`, sha256 in `pre-freeze/sha256s.txt`), census v2 and its manifest.
  Pre-freeze scores: real `8/8`; `ctl-att3b-label-worktree` 0/8, `ctl-cn1-oracle-worktree` 1/8,
  `ctl-fingerprint` 0/8, `ctl-sequence` 0/8, `ctl-pinned-hash` 0/8, `ctl-always-accept` 0/8,
  `ctl-r85-forgery` 0/8 (`.ufo/evidence/round-87/pre-freeze/c1/`).
- Census v2 selftest 15/15 (`pre-freeze/c2/census-v2-selftest.txt`); the mutants M1 and M2 showed the
  arms can fail (`mistakes/M1-red-selftest.txt`, `M2-red-selftest.txt`, each 13/15).
- Overreach manifest committed at `38c83698` (v2-schema copy of the r86 relabel rows; only the schema field changed).
  v1 on those bytes `CAP_CENSUS: rows=30 bound=30 unbound=0 mismatches=0` exit 0
  (`pre-freeze/c2/v1-overreach-before.txt`); v2 `CAP_CENSUS_V2: rows=30 bound=0 unbound=30 mismatches=0` exit 1
  (`pre-freeze/c2/v2-overreach.txt`).
- Freeze `1d5102a1` (`plans/round-87.plan.md`): predicates, controls, kill rules, sourced claims, routed r86 defects.
- Frontier: `S289` (git-cat-file) and `S299` (Python shutil) re-opened 2026-11-05 for R87-C1; located quotes
  in `corpus/lessons/round-87.md` `## Gate` (snapshots `.ufo/evidence/round-87/sources/`).
- **Wave `r87-w1`:** one validated v1 wave, 10 seats, `.ufo/waves/round-87/w1-spec.json`,
  `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`, results `.ufo/waves/round-87/r87-w1-results.json`
  (WAVE-DONE received: "all 10 seats settled"). Seat reports in `.ufo/waves/round-87/w1/`:
  - `T87E1.md` (executor, counterfeit hunt): `cf-c` and `cf-d` reach `passed=8/8` → **kill candidates**;
    `cf-a` (correct git-backed) also 8/8, not a kill; `cf-b` and `cf-e` 7/8. Verdict `killed`.
  - `T87E2.md` (executor, determinism and arm liveness): five identical verdicts; eight single-deviation
    near misses each 7/8. Verdict `arms-live`.
  - `T87E3.md` (executor, overreach hunt): an uncited pin binds through post-table prose (`selftest-text pin`).
    Verdict `overreach-bound`. Reproduced by the L1 (below).
  - `T87SC1.md` (scout, pin inventory): all 12 historical pins are cited regular blobs. Verdict `inventory-clean`.
  - `T87CN1.md` (connector, read-only sibling scan, 17 files): patterns and two adjacency overlaps, reported only.
  - `T87S1-gate-quotes.md` (scribe): all Gate quotes verbatim, word counts and lines verified.
  - `T87R1.md` (reviewer): `no-kill-found`; weak findings M1 (seven of eight cases satisfiable without committed bytes),
    C1 (citation is directory-prefix and whole-word, not exact as the plan sentence says), C4 (post-table prose
    absorbed into the last row, graded `note`; this was the kill, see M7).
  - `T87C1.md` (critic): `C1-killed` (`cf-oid`: object-id equality reaches 8/8 with a wrong `carried` on a
    well-formed wrong sha); `C2-survives` on its own reading (the `live` branch binds by id: 18/30 relabel).
  - `T87M1.md` (mutation-tester): census v2, 13 of 20 mutants killed by selftest, 7 survive (C03, C05, C12, C17,
    C18, C19, C20); counter, 2 of 9 killed, 7 survive (K01, K02, K04, K06, K07, K08, K09). No control reached
    `passed=8/8` under any mutant. Verdict `survivors`.
  - `T87SN1.md` (sentinel): PATH shim receives zero counter and census argv; GIT_* poisoning leaves verdicts
    unchanged; non-empty `--work` refused exit 2; absolute manifest refused. Verdict `robust`.
- **L1 reproduction of the C2 kill** (not taken on the seat's word): in a scratch `git clone --shared` at `1d5102a1`
  with the probe manifest committed in the clone, `selftest-text pin` binds on the pin
  `tools/selfstate-freshness.json@d10a9c66d618` (`CAP2_ROW … bound=yes reason=pin:…`; census `bound=30`, exit 0).
  Causal control: the same manifest after removing only the path from the post-table prose line → `pin-not-cited`,
  census `bound=29`. Files: `.ufo/evidence/round-87/kill-c2/probe-prose-absorbed.txt`,
  `control-prose-path-removed.txt`, `overreach-probe.json`, `sha256s.txt`.
- **C1 kill, L1 check:** `cf-c`/`cf-d` source and outputs are in `T87E1.md`; the reproduction command is in that file.
  The frozen counter stayed untouched.
- Standing sweeps at `ccd6ac26` (`.ufo/evidence/round-87/landing/`): selfstate `rows=26 match=24 stale=2 unexpected=0`
  (the two stale rows are declared frozen snapshots, `expect=stale`); census v1 real `30/30`; census v2 real `30/30`;
  census v2 selftest `15/15`; C1 counter real `8/8` at the landing revision; `receipt-bytes-bind` `unbound=0`;
  `registry-figure-bind` all match; coldread precheck `floor_credited=47 cand_credited=47 lost=0`.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Pre-freeze: `measure.py`, seven controls, census v2 + manifest, receipts, pre-freeze scores (no claim data) | Round 87 (pre-freeze instruments) | `a3b4f75d4172880f37c19f9040920952bc56b217` |
| v2-schema overreach manifest (rows identical to r86) | Round 87 | `38c83698` |
| Freeze: `plans/round-87.plan.md` | Round 87 (freeze) | `1d5102a1788667f45c3163c6251ae520d5e62654` |
| Records: `corpus/SOURCES.md` used-by (S289, S299), round-86 correction note, round-87 note; `corpus/QUALITY.md` criteria 132–133; lesson Gate and first Mistakes; mistake red evidence | Round 87 (Frontier) | `ccd6ac2624f339856d90bb8b34f791eac7aa6753` |
| Landing: lesson verdicts, Mistakes M6–M9, routing and trends; `SCORECARD.md` round-87 block; `LOG.md` round-87 entry; wave evidence `.ufo/waves/round-87/`; kill evidence `.ufo/evidence/round-87/kill-c2/`; landing receipts | Round 87 (landing) | `d91971194f6e1d12cdcbed3e22bb4ed8857109bd` (lane HEAD) |

No existing tool was modified. The round-85 counter, the round-86 counter, census v1 and their verdicts are untouched.
No capability row was entered (C1 not verified).

## Before → after measurements

| Claim | Before | After | Verdict | Counting command | Measured commit |
|---|---|---|---|---|---|
| R87-C1 counter | r86 counter on its counterfeits: `att3b` 8/8, `cn1` 8/8 (r86 kill) | r87 counter, real `passed=8/8`; controls 0/8, 1/8, 0/8, 0/8, 0/8, 0/8, 0/8; counterfeits `cf-c` 8/8, `cf-d` 8/8, `cf-oid` 8/8 | **killed** | `python3 -I .ufo/evidence/round-87/measure.py --repo . --rev 1d5102a1 --work <EMPTY_DIR>` | `a3b4f75d` (controls), `1d5102a1` (freeze), `ccd6ac26` (landing run, `8/8`) |
| R87-C2 census | v1 on overreach bytes: `rows=30 bound=30 unbound=0`, exit 0 | v2 on overreach bytes: `rows=30 bound=0 unbound=30`, exit 1 (predicate b met); v2 real `rows=30 bound=30 unbound=0`, exit 0 (predicate a met); kill probe (uncited prose-absorbed pin): `bound=30` exit 0; causal control `bound=29` | **killed** | `python3 -I -X utf8 tools/capability-census-v2.py --repo . --rev REV --manifest <m> --selfstate tools/selfstate-freshness.json` | `38c83698` (overreach), `ccd6ac26` (real), probe on a clone of `1d5102a1` |

## Sources & frontier

- Census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`):
  before exit 0 (`.ufo/evidence/round-87/census-before.txt`); after the records commit, exit 0 (`census-mid-after-lesson.txt`);
  final exit 0 (`census-final.txt`). Warnings W01/W04 retained, none erased.
- Rows: **171 → 171** (no row added; none removed). Rows added by tier: none.
- Rows touched old → new:
  - `S289` `used-by`: `…corpus/lessons/round-85.md` → `…corpus/lessons/round-85.md, corpus/lessons/round-87.md`. Status `mined` → `mined`, recheck `180d` → `180d`.
  - `S299` `used-by`: `corpus/lessons/round-68.md` → `corpus/lessons/round-68.md, corpus/lessons/round-87.md`. Status `mined` → `mined`, recheck `365d` → `365d`.
  - Round-86 note: appended correction (the S305 fetch instant is `Thu, 05 Nov 2026 00:45:18 GMT` per its header; the row is unchanged).
- Frontier rows advanced: none. Frontier F1–F11 unchanged.
- Sourced claim: R87-C1 cites `S289` and `S299`, both re-opened this round (§2b.4 met).
- Assimilation: **none.** `merge/tameshi/MERGE-REPORT.md` (103 staged rows, 86 knowledge entries) covers mutation-score semantics, flaky verdicts and PBT generators; none serves either claim. Nothing appended; the quarantine-first duty was not triggered.
- considerthese: `considerthese/2026-10-28.md` ideas 1, 2, 3 and 5 are already implemented by committed tools; idea 4 (assimilation backlog) is out of claim scope, so none was taken.
- Calibration side finding (not claimed): `LOG.md` has 16 quoted counter lines with no backing receipt (old append-only rounds); `corpus/lessons/round-86.md` has 2 (`resolved=0/2`, `rows=len(rows)`). Named as open debt, not moved.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | No `knowledge/` entry, no capability row, no frontier move; rows 171 → 171 (census exit 0). |
| quality | unchanged | No admitted entry changed; both successor instruments killed by their own rules; criteria 132–133 added as rules. |
| discernment | unchanged | The gate froze two claims whose kill classes the wave then found (M6, M7): the same pattern as round 86 (kill by the wave, not the freeze gate). A reviewer finding was graded `note` and was the kill (M7). No claim was admitted wrongly. The operator may rule `harmed` on the M7 grading miss. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; no SKILL.md section added this round (`git diff --stat` on SKILL.md is empty). Pointer: `SHONEN.md:5-6`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round ran the frozen counter and census v2 end-to-end on committed bytes and killed both claims; pointers `LOG.md` "Round 87 (2026-11-05)", `.ufo/evidence/round-87/landing/`. Lane assertion; no independent promotion verifier.
- [~] Instructions executable by an agent without oral context — both instruments run from committed CLIs; census v2 selftest 15/15 (`.ufo/evidence/round-87/landing/cap-census-v2-selftest.txt`); lane assertion, no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — connector scan read-only; overlaps reported, nothing absorbed (`.ufo/waves/round-87/w1/T87CN1.md`). Lane assertion, no independent promotion verifier.

## Round extras

- **Round shape:** one validated v1 wave under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
  (band 8–16). Spawn 10, residual calls 0, replacements 0. The L1 holds the planner seat (the validator refuses `planner`).
- **Seat mix:** executor 3 (T87E1, T87E2, T87E3), scout 1 (T87SC1), connector 1 (T87CN1), scribe 1 (T87S1),
  reviewer 1 (T87R1), critic 1 (T87C1), mutation-tester 1 (T87M1), sentinel 1 (T87SN1). Total round seats 10.
- **Attack share (counting rule, stated once):** attack roles are reviewer, critic and mutation-tester
  (labrat is a frozen-topology seat, not a swarm role): **3 of 10 = 30 %**. The sentinel is counted as robustness, not attack.
- **Routes:** assigned by the orchestrator from the run-15 map; the L1 did not observe the answering model per seat, so none is claimed.
- **Dead seats:** none. All ten seats settled with a final output, and each has a deliverable file in the wave dir.
- **Duplicate-session / replacement:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open; next round is 88.
- **Tool installs:** none. pacman remained paused and was not used.
- **Open L0 questions:** none appended to `.ufo/l0-questions.md`.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): ` M .scratch/run15-state.json`
  (orchestrator-owned, not touched) and `?? tools/mori-source-digest.py` (named for the mori lane, not tameshi; left in place).
  No tameshi seat file landed at the fleet root.
- **Routed round-86 defects:** (1) before-state inputs committed (`a3b4f75d`, `38c83698`) — addressed. (2) final-tip figures without receipt — open (see Sources & frontier). (3) S305 fetch instant — corrected in an appended note. (4) attack-share counting rule — stated once above. (5) QUALITY criteria for M3/M4 — addressed as criteria 132–133. (6) retained instruments unregistered — open (the new counter and census v2 are also unregistered). (7) successor C1/C2 — ran; both killed; successors routed to round 88 (lesson `## Routed to round 88`).
- **Residual debts, named:** PATH is pinned in the counter and census but the r86 `GIT_*`/receipt race/parent-alias, conversion, malformed kind/source-id and caller revision-authority debts stay open. The census `live` branch trusts the self-state id (critic C2e). The docstring of census v2 does not match its code (M8). Seven census and seven counter mutants survive (M9).
- **Pre-report gate:** `git ls-remote origin refs/heads/master` → `d91971194f6e1d12cdcbed3e22bb4ed8857109bd` (matches lane HEAD).
