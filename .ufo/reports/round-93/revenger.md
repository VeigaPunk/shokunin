# revenger — round 93 (hyaku run 15, attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Lane tip cited: `28b5f99b90c1da91ac85d2e6d6aa6ec49efa42e6` (= `git ls-remote origin refs/heads/main`). Landing commit: `0723ebd0687291685fa231b9808bbb20b5e49c13`. Base: `281a5bad66e844190a570cb35d257c6974749993`. Freeze: `02050cb2a6758e3bd9cec696ff0e42df6f23511a`.

## Work performed

**Declared claims (2; two distinct axes; both frozen at `02050cb` before any seat scored):**

- **C1 — coverage (knowledge-map ground K, the lowest non-retired axis, 9/15 = 6.0).** Row C08 (browser/Electron runtime evidence) moves `uncovered` → `held`, backed by one admitted entry derived from the lane's saved round-77 CDP record. Frozen predicate: `C1_VERDICT=pass` from `reports/round-93/c1_k_admit_counter2.py --rev <rev>`. Target: `K_HELD_BACKED` 10/15.
- **C2 — calibration (the lane's counting instruments).** Successor counters `c1_k_admit_counter2.py` and `c2_legend_counter2.py` plus the frozen nine-class forgery battery `forge_battery.py` (classes F1–F9, the routed r92 critic and mutation findings). Frozen predicate: `BATTERY_VERDICT=pass` from `forge_battery.py --stage full`; red-before `--stage v1-only` must show `V1_REACH_C2=5/5`.
- Shape: no third claim. The frontier step (curation, mined mistake, sourced claim) rides inside C1/C2 as §2b.

Work items, with evidence pointers:

- Load order and protocol: `skill://shokunin`, `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/{PROTOCOL,CORPUS,LEARNING}.md`, `MISSION.md`, `AXES.md`, lane `SCORECARD.md` (round-92 section), `corpus/QUALITY.md`, `corpus/README.md`, `corpus/lessons/round-92*.md`, `corpus/SOURCES.md` census (round start: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` exit 0, 21 W01 + 12 W04, 0 E).
- Round-start verification of the C08 record: `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json` → `ORACLE OK (17/17 checks)`, exit 0 (`reports/round-93/controls/oracle-opening.log`); record sha256 `b045a4ee…` and fixture shas `46e51761…`, `fb079fa2…` match the pins (same log, wave `ScoutRecord/digests.txt`).
- Freeze: `reports/round-93/claims.md`, `freeze-base.txt`, `c1_k_admit_counter2.py`, `c2_legend_counter2.py`, `forge_battery.py`, `controls/` (do-nothing receipts `c1v2-do-nothing.log` [fails], `c2v2-do-nothing.log` [fails]; selftests `selftest-c1v2.log`, `selftest-c2v2.log` [pass]; red-before `battery-v1-only.log` [`V1_REACH_C2=5/5`]; `battery-full.log` [`V2_KILLS=9/9`, `POS_C1V2=pass`, `POS_C2V2=pass`, `DO_NOTHING_C2=fail`, `R92_RECEIPTS=4/4`]). Committed at `02050cb`.
- Wave: one v1 wave `revenger-r93-w1`, 13 seats, validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatched by the orchestrator inline (`.ufo/waves/round-93/w1.ready` → `w1.ready.dispatched`; `WAVE-DONE` received from Main; `w1-results.json`, 13 seats settled, no dead seat). Spec `w1-spec.json`, validator output `w1-plan.out`, dispatch `w1-dispatch.json`, registry `w1/swarm-registry.json` (committed, `.ufo/waves/round-93/`).
- Seat outputs (wave dir `.ufo/waves/round-93/w1/`):
  - `ScoutRecord` — oracle re-run, digests, S495 and S496 rows, S496 quote receipt (`quote-receipts/S496.receipt.json`, body sha `ba8018bb…`, quote located at span 3408–3526), `opens.json`.
  - `ScoutS136` — S497 `supersedes S136 —` row; addendum fetched at pinned `dotnet/runtime` commit `b22bfee2…` (body sha `1e6e225a…`); receipt `quote-receipts/S497.receipt.json`. The brief's `github.com/dotnet/ecma-335` URL returns 404; recorded in lesson M2.
  - `ScribeEntry` — entry draft (`entry-draft.md`, READY) for the C08 entry.
  - `ExecOracle` — independent re-derivation of LEDGER facts; `derivations.txt`, `ledger-check.tsv`.
  - `ExecBattery` — integrity of the three instruments (sha equal to freeze blobs), reproduction of all four verdict logs, one-constant mutant that flips the record leg (`canfail.log`).
  - `ExecCensus` — census mid-round (exit 0), no-harm diff (empty), assimilation collision count 155/155 (`collisions.txt`), L0 inventory (7 open `revenger |` lines, none appended).
  - `ReviewerGate`, `ReviewerBlind`, `CriticR93` — Q-gate votes (`vote.json` each, artifact-bound). `ReviewerBlind` derived facts from fixture and record bytes before reading the entry.
  - `ReviewerErrata` — entry revision patch for the round-92 entry (`entry-r92-revision.patch`, `git apply --check` clean), relabel correction, S136 row text, gate re-run log.
  - `CriticR93` — 12 ranked findings against both v2 counters (`CriticR93/findings.md`, receipts under `receipts/`), attempts A0–A29 and R1–R9 (real-tools bypasses).
  - `MutationR93` — 21 mutants of the two v2 counters: 20 killed, 1 equivalent (`C2_NO_NEW`), 0 survived (`mutants.md`, `results.json`).
  - `ConnectorOverlap` — sibling overlap (tabi, kaidoku, kotoba, kumitate, kengaku; read-only; contested-open rows named, not absorbed) and considerthese proposal 2 measured (`measurement.tsv`: r89–r92 8/8 claims contested or not verified).
  - `SentinelScope` — write-scope audit. It found two defects, both fixed before landing: a gitignored `reports/round-93/__pycache__/` written by a counter import without `-B`, and a 275 MiB seat scratch dir (`/fast/scratch/hyaku/revenger-r93/CriticR93`) left after yield. Both removed by the L1.
- Landing (`0723ebd0`): the C08 entry `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` (admitted; 17 oracle checks re-run; lint 0/0/0/0; embedded `checked_blocks=2 problems=0`); `corpus/SOURCES.md` S495–S497; `corpus/README.md` C08 → `held`; the round-92 entry's next revision (errata patch, see Landed changes); `reports/round-93/` receipts, `opens.json`, `quote-receipts/`, `votes/`; `.ufo/waves/round-93/` wave evidence; `SKILL.md` gate-registry rows for the two v2 counters and the battery.
- Entry corrections during the round (three digest moves, all re-bound): (a) an underived count sentence and a "(15 words)" parenthetical removed (critic Q11); (b) the `verified-at:` byte-identity clause scoped to `corpus/live corpus/fixtures` because the registry changed at landing (critic Q15; `git diff --quiet 02050cb… -- corpus/live corpus/fixtures` exit 0, verified). Final candidate digest `1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647`; all three votes bind it (`reports/round-93/votes/*.json`, `digest_ok=True`, `artifact_ok=True`).
- Landing-tree measurements: `c1-after.log` (`C1_VERDICT=pass`, `C1_K_HELD_BACKED=10/15`), `c2-after.log` (`C2_VERDICT=pass`), `battery-after-full.log` (`V2_KILLS=9/9`, `BATTERY_VERDICT=pass`); all with `--rev 0723ebd0`.
- Census round end, after a landing defect: S497's used-by cell carried a stray dash (`— corpus/lessons/round-93.md`), E11 exit 1. Fixed (`corpus/SOURCES.md`, used-by is mutable). Round end now `reports/round-93/census-round-end.log`: exit 0, 0 E, 21 W01 + 13 W04 (lesson M5).
- Assimilation: none. `merge/revenger/` package still 155/155 id collisions (`ExecCensus/collisions.txt`); L0 `revenger | round-91` unanswered; wave-4 quarantine was done in round 92 (26 rows). Nothing adopted.
- Operator-side and cross-lane notes: a relayed message from a `ReviewerV4` seat about round-94 bookkeeping reached this L1's channel; it is not this lane's round and nothing was acted on.

## Landed changes

| change | file(s) | LOG / SCORECARD entry | commit |
|---|---|---|---|
| Freeze of claims, successor counters, battery, controls and receipts | `reports/round-93/{claims.md,freeze-base.txt,c1_k_admit_counter2.py,c2_legend_counter2.py,forge_battery.py,controls/*}` | pre-data freeze (no LOG line) | `02050cb2a6758e3bd9cec696ff0e42df6f23511a` |
| C08 knowledge entry (admitted) | `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` | LOG.md "Round 93" → C1 | `0723ebd0687291685fa231b9808bbb20b5e49c13` (landing); digest `1304008c…` |
| Round-92 entry next revision (recheck pointer, labelled beyond-quote statements) | `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` (`git apply` of `.ufo/waves/round-93/w1/ReviewerErrata/entry-r92-revision.patch`) | LOG.md "Round 93" → Corrections | `0723ebd0…` |
| SOURCES S495, S496, S497 | `corpus/SOURCES.md` | LOG.md "Round 93" → Evidence; SCORECARD round-93 Sources | `0723ebd0…` (rows); `28b5f99b…` (S497 used-by cell fix) |
| C08 row → held | `corpus/README.md` | SCORECARD round-93 C1 | `0723ebd0…` |
| Gate-registry rows for the two v2 counters and the battery | `SKILL.md` | SCORECARD round-93 (instruments) | `0723ebd0…` |
| Round lesson (Gate, Mistakes M1–M5, corrections, census) | `corpus/lessons/round-93.md` | LOG.md "Round 93" | `0723ebd0…`; M5 and census fix `28b5f99b…` |
| Wave evidence, votes, receipts, logs | `.ufo/waves/round-93/**`, `reports/round-93/{votes,quote-receipts,opens.json}` | LOG.md "Round 93" → Wave | `0723ebd0…` |
| Adjudication: SCORECARD round-93 section, LOG entry, post-landing measurements | `SCORECARD.md`, `LOG.md`, `reports/round-93/{c1-after.log,c2-after.log,battery-after-full.log,census-round-end.log}` | this report | `28b5f99b90c1da91ac85d2e6d6aa6ec49efa42e6` |

Tool installs: none (no tool installed by this L1 or any seat; no pacman, sudo, sysctl or system configuration touched — sentinel check 4).

## Before → after measurements

| claim | before → after | counting command | measured commit(s) | verdict |
|---|---|---|---|---|
| C1 — K (coverage) | `K_HELD_BACKED` **9/15 (6.0) → 10/15 (6.7)** | `PYTHONUTF8=1 python3 -B reports/round-93/c1_k_admit_counter2.py --rev 0723ebd0687291685fa231b9808bbb20b5e49c13` → `C1_VERDICT=pass`, exit 0. Base: `… --rev 281a5bad…` → `C1_C08_HELD=fail`, verdict fail (`controls/c1v2-do-nothing.log`) | base `281a5bad`; landing `0723ebd0`; re-run on adjudication `28b5f99b` (tree unchanged in `corpus/knowledge`, `reports/round-93`) | **met on the frozen counter; contested** (critic findings 1–7, 10–11: reachable forgeries outside the frozen nine; the landed entry is not among them) |
| C2 — calibration (reach of the counters) | nine routed classes: **v1 reach 5/5 → v2 kills 9/9** (v1 red, `controls/battery-v1-only.log`); the r92 receipts `4/4` resolve | `PYTHONUTF8=1 python3 -B reports/round-93/forge_battery.py --stage full` → `BATTERY_VERDICT=pass`, exit 0; `--stage v1-only` → `V1_REACH_C2=5/5` | counters at `02050cb`; battery against base trees; run at `0723ebd0` (`battery-after-full.log`) | **met on the frozen predicate; contested** — the critic built further passing attacks (findings 1–12). No 0–10 score claimed |
| Mutation support (no claim) | 21 mutants of the v2 counters: 20 killed, 1 equivalent | `MutationR93/mutants.md` | base-tree builds | recorded |

Axes not moved, no harm: PROVINCE.md and corpus/QUALITY.md unchanged (`git diff --stat 281a5bad..0723ebd0 -- PROVINCE.md corpus/QUALITY.md` → empty). Holds at base (`reports/round-73/measure.py`, `f_probe4.py`, `mg_probe.py`, `ag_probe2.py` over the freeze archive): `K_HELD_BACKED=9/15`, `F4_COVERAGE=11/11`, `M_RECORDED=3/3`, `A1V2_RECORDED=5/5`; not re-run at landing.

## Sources & frontier

- SOURCES before → after (counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; malformed `awk -F'|' … NF!=13`; tier and status histograms by the CORPUS census commands): rows **494 → 497**; malformed 0 → 0; duplicate ids 0 → 0; tiers A=445 → 448, B=21 → 21, C=28 → 28; status mined=458 → 461, queued=16 → 16, rejected=20 → 20. Measured at `02050cb` and `0723ebd0` (`git show <rev>:corpus/SOURCES.md`).
- Rows added by tier: **A = 3** (S495 own-work record, tier A for the fixture-scoped record; S496 docs, tier A for the protocol's self-description; S497 docs, tier A for the addendum's own scope). None tier B or C.
- Rows touched old → new: none in place (append-only). S497's used-by at landing was set to this round's lesson; the stray-dash cell fix in `28b5f99b` is a cell correction of a row added this round. No status or recheck changed on any existing row.
- Census: round start `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` exit 0 (21 W01 + 12 W04, 0 E); round end exit 0 (21 W01 + 13 W04, 0 E; `reports/round-93/census-round-end.log`).
- Frontier rows advanced: C08 `uncovered` → `held`. Sourced claim: C1 rests on S495 and S496 (§2b.4), both opened 2026-11-05; the quote receipts are in `reports/round-93/quote-receipts/`.
- Assimilation: none (`merge/revenger/` 155/155 id collisions; L0 `revenger | round-91` unanswered).
- considerthese: `considerthese/2026-11-05.md` proposal 2 mined (`.ufo/waves/round-93/w1/ConnectorOverlap/considerthese-note.md`): measured r89–r92, 8/8 contested or not verified; recorded as the round-94 baseline, not adopted as a QUALITY criterion.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the coverage map did not hold (C08: `uncovered` → `held`), each `source:` citing a `mined` row (S495, S496). Evidence: `corpus/README.md` C08 row; `c1-after.log` `C1_K_HELD_BACKED=10/15`.
- **quality: improved.** The round-92 entry's recheck pointer and two beyond-quote statements were corrected (next revision, patch applied, round-92 votes not re-bound, correction logged); the new entry's Q11 and Q15 defects were found by the gate and fixed before admission. No admitted entry fails its re-check (lint and embedded gates re-run on the final bytes: `checked_blocks=2 problems=0`).
- **discernment: unchanged.** The gate caught defects (two counts, one scope sentence, a stale vote binding) and the frozen counters are still reachable by attacks outside the frozen nine (critic findings 1–12). There is no outside non-author spot-check of this round's gate decisions yet; the integrator's spot-check is pending. Neither a harm nor an improvement is claimed.

## SHONEN

The round-93 SHONEN assessment of the lane's shokunin (no box is marked `[x]`: no named non-author verifier exists for this round):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md gate-registry rows for the two v2 counters and the battery added this round (`git show 0723ebd0:SKILL.md`); the prior lane attestation stands (r64 bytes); no non-author confirmation of the current bytes.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-77 record re-run and identity-checked (oracle 17/17, `reports/round-93/controls/oracle-opening.log`); LOG.md "Round 93" entry at `28b5f99b`.
- [~] Instructions executable by an agent without oral context — `reports/round-93/claims.md` predicates and commands; `corpus/lessons/round-93.md` `## Gate`; no outside verifier has executed them yet.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-unchanged (empty diff); the contested rows (tabi `adjacency.tsv:5`, kaidoku README 36–37) are reported in `.ufo/waves/round-93/w1/ConnectorOverlap/overlap.tsv`, not absorbed; the C08 entry is fixture-scoped.

## Stale-lane

No mission of this lane is open beyond this round; the lane was dispatched once for round 93 (`watchdog.log` launch 11:05:13; the round's wave completed in ~1 h). No `lane-dead-no-report` line for round 93. Progressing throughout (commits authored by the lane at 02050cb, 0723ebd0, 28b5f99b; wave seat activity in the lane tree).

## Round shape, seats and dead seats

- One v1 wave, `revenger-r93-w1`, **13 seats** (band 8–16): scout ×2 (`ScoutRecord`, `ScoutS136`), scribe ×1 (`ScribeEntry`), executor ×3 (`ExecOracle`, `ExecBattery`, `ExecCensus`), reviewer ×3 (`ReviewerGate`, `ReviewerBlind`, `ReviewerErrata`), critic ×1 (`CriticR93`), mutation-tester ×1 (`MutationR93`), connector ×1 (`ConnectorOverlap`), sentinel ×1 (`SentinelScope`).
- Attack share: reviewer ×3 + critic + mutation-tester = 5/13 = 38.5 % (≥25 %). Connector seats: 1 (≤2).
- Residual call: none. Planner: held by the L1 (the validator rejects the role); no planner seat dispatched.
- Round total: 13 seats. Dead seats: none (`w1-results.json`: 13 settled, each with its output). Seat routes: as the run-15 map at spawn; not separately measured.
- Re-bindings: `ReviewerBlind` and `ReviewerGate` and `CriticR93` each re-bound their vote to a later entry digest (three moves, `corpus/lessons/round-93.md` M1). This is not a new seat.

## Open L0 questions

- `revenger | round-91` (assimilation id-collision guard, mass drift 155/155) — still open; routed around (assimilation none).
- No new L0 question appended this round.

## Misroot sweep and inherited state

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root (adjudication time): `M .scratch/run15-state.json` (orchestrator-owned run state; not touched by this lane), `?? .ufo/closure-kaidoku-r92.json` (kaidoku closure artifact; names kaidoku's round-92 closure), `?? cases_A.json` (member `llm-inference-batching-scheduler`; not this lane). None names revenger round 93 as its writer; none moved, copied or deleted. No misroot.
- Lane leftovers: none. `git status --porcelain` in the lane was empty at landing and adjudication except the stray `__pycache__`, removed before landing.

## Scratch

Seat scratch under `/fast/scratch/hyaku/revenger-r93/` was removed by the L1 after landing (`CriticR93` 275 MiB removed earlier; `ExecBattery`/`ExecOracle` and the L1's own `l1/` removed at the end of this round). Disk guard status was not consulted again after the wave.

## Honesty notes

- Both claims are **contested** on the critic's evidence. The frozen predicates are met; the frozen counters are not sound against every attack. The round does not claim a verified admission of the claims as "clean". The operator rules.
- The C08 entry's admission rests on three votes and on the frozen counter; the critic's Q01 and Q11 dispute were resolved by correcting the text, not by relabelling the votes.
- The round-92 votes remain lane-internal (LEARNING.md); the admission of the round-92 entry rests on the integrator's spot-check, as its record states.
