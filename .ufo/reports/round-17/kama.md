# kama — round 17 report (hyaku phase 2, steered, attempt 1)

Lane repo `kama-shokunin` (jj-colocated; commits only through `scripts/hyaku/jj-lane.sh`).
Start `cff9e62f05aa7cfb9059444f62eb787100719713` (clean; no `lane-dead-no-report kama
round=17` line, nothing inherited). Landed: build `54a29268e2083caa2b1e0d54ee1e7d90961302f3`
(measured commit), falsify evidence + corrections `5e9ae6e93dce529a48229647e482f18a291463cd`
(lane tip, pushed: `jj-lane.sh state` → `local=remote=5e9ae6e… ahead=0 behind=0`).

## Work performed

Declared claims (2): **C1 calibration** (lowest assigned axis, 7) — the verdict-matrix
gate `tests/probe-verdicts/check.py` claimed gradings no detector could fail; repaired and
backed by a fault-control detector. **C2 operability** (sourced; hardening of capability
`live-llamacpp-lifecycle`, no new row) — live receipt v2 checks that fail on the
misbehaviour they name. Separation criterion: `corpus/lessons/round-17.md` §Declared
claims (C1 touches only check.py and its detectors; C2 only the live tool, its gate and
controls; `tools/kama-probe.sh` byte-identical `36b64978…` throughout).

- C1: check.py grades `served_model` (from each row's own `/v1/models` body, probe
  `served_ids()` precedence) and the `GET /v1/models` route; malformed and non-UTF-8 probe
  output is a recorded row failure (`54a2926:tests/probe-verdicts/check.py`); detector
  `tests/probe-verdicts/fault-controls.py` (F0 identity control + F1–F8); counting
  `.ufo/waves/round-17/c1/mutants.py --grid`. Matrix bytes unchanged (`bf9068d8…`, 9
  files, 72 rows; falsify `MatrixBytes.md`).
- C2: `tools/kama-llamacpp-live.py` receipt `kama-llamacpp-live/v2` (exact `/health`
  body — S042; `teardown_graceful` — S043/S047, S044; ownership-gated port closure;
  `loading_envelope_graded` over every stored 503 body; receipt on internal fault);
  `tests/llamacpp-live/check-receipt.py` v1+v2 (v1 unchanged; selftest 26 v1 + 13 v2
  mutations); `tests/llamacpp-live/controls.py` K0–K8 + gate-flip arm.
- Frontier step: SOURCES S042–S047 opened this round (lesson §Gate); mined mistake M1
  (S041 in-place edit) with fail-capable `tools/sources-append-only.py` + KQ22; KQ20/KQ21
  from the gate-overclaim class (M2).
- Routed defects (round-16 spot-check 1–6) and jj risks: lesson §Routed defects /
  §Routed jj-migration risks — provenance v2 (`.ufo/waves/round-17/dispatch-provenance.py`,
  policy block + one canonicalization, spawned 0 → 79 demo
  `.ufo/waves/round-17/provenance-0to79-demo.txt`); strict verdict counter (round-16
  falsify corrected to 34/40/0 + 5 nonconformant); OPTIONS corrections appended in five
  files; round-13 live gate exit 4 for worktree-ahead-of-HEAD (jj R1; selftest 13/13);
  `.gitignore` `.ufo/state/` + `__pycache__/` (`registry/history/.lock` was already
  ignored); `AGENTS.md` jj VCS rule. Not changed, with reason: round-16 `measure.py`
  parity (pinned counting command, latent hazard), `tools/kama-probe.sh:422` comment
  (would move the probe pin).
- Planner seat: held by L1 (validator rejects `planner`); the bounded planning data-walk
  rode `RevengerPlannerWalk` (build wave).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| check.py grading, fault-controls.py, mutants.py, runs/ | §round 17 — graded fields and fail-capable live checks | `54a29268` |
| live tool v2, receipt gate v1+v2, controls.py, live receipts | same | `54a29268` |
| sources-append-only.py, round-13 exit 4, count-verdicts.py, dispatch-provenance.py | same | `54a29268` |
| SOURCES S042–S046, QUALITY KQ20–KQ22, knowledge §Round 17, SKILL/README/PROVINCE/SHONEN appends, .gitignore, AGENTS.md | same | `54a29268` |
| falsify wave evidence (spec, dispatch, validation, provenance, 73 reports, summary) | §round 17 — falsify wave and corrections | `5e9ae6e9` |
| S047 supersedes S043; SKILL/knowledge/AGENTS corrections; lesson §Falsify wave; SCORECARD falsify verdicts | same | `5e9ae6e9` |

## Before → after measurements

Measured against lane commit `54a29268e2083caa2b1e0d54ee1e7d90961302f3`; raw outputs
`.ufo/waves/round-17/runs/`, `.ufo/waves/round-17/live/`; every number re-ran identically in
falsify `/tmp` clones.

- **C1** — `python3 tests/probe-verdicts/fault-controls.py --check <check.py> --json`:
  frozen check.py (`b853576e…`) 3 of 8 faults accepted (F5 served_model, F6 route, F8
  malformed) → current 0 of 8. `python3 .ufo/waves/round-17/c1/mutants.py --grid --out …`:
  full detector 7/8 → 10/10 killed; round-16 pair detector 1/8 → 1/10 (only reject-all) —
  the pair cannot see field-deleting mutants on either gate. Bounded by falsify:
  non-author mutants H1–H3, H5–H7 survive both detectors (lesson §Falsify wave).
- **C2** — `python3 tests/llamacpp-live/controls.py --tool ABS --gate ABS --json`: frozen
  tool+gate 6 accepted-bad (+1 inconclusive) → current 0 (each of K1–K6, K8 fails its
  targeted check; K7 rejected on setup error); three real b11755 runs 11/11, gate `VALID`
  with model, server, probe, tool pins (+3 and +20 falsify reruns). Trade risk: 1 of 60
  real runs under 32x `stress-ng` load failed `loading_envelope_graded` on a healthy
  server (falsify `LiveUnderLoad.md`); six v2 checks have no retained bad control.
- No-harm: round-16 `measure.py` PASS (55/17 → 72/0) in a `/tmp` clone with the new
  check.py; `test-snapshot.sh` 30/0; v1 receipts `VALID` with four pins; probe and matrix
  bytes unchanged.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kama` — round start exit 0 (`W04 S031`; 
`.ufo/waves/round-17/sources-before-validate.txt`), round end exit 0 (`W04 S031`, `W04
S043` shared server.cpp URL, disclosed; `.ufo/waves/round-17/sources-final-validate.txt`).
Rows 41 → 47: tier A 38 → 44 (S042 code, S043 code, S044 docs, S045 docs, S046 own-work,
S047 code), B 0, C 3; mined 31 → 37, queued 5, rejected 5. Rows touched old→new: none
(S047 supersedes S043 by a new row; `tools/sources-append-only.py --from cff9e62 --to
54a2926` and `--from 54a2926 --to 5e9ae6e` exit 0). Frontier advanced: "live grading of
a loading server by the receipt" now held (`corpus/README.md` §Round-17); no new
coverage-map ground. Mined mistake: M1 (S041), guard shown failing on `b8e485c→ccc4bb3`.
Sourced claim: C2 on S042/S043/S044 (S047 after correction).

## Trend verdicts

- **expansion: unchanged** — one existing knowledge entry deepened; no uncovered ground; no
  new capability row.
- **quality: improved** — the round-16 entry's v1 limits superseded by graded checks backed
  by sources and controls; a stale source reading (S043) superseded by a stronger row
  (S047) within the round; OPTIONS overstatements corrected by appended text; no admitted
  entry failed re-check.
- **discernment: unchanged** — no non-author admit/reject sample yet; every seat is
  lane-dispatched. KQ20–KQ22 added with lessons (not counted as discernment until an
  outside check agrees).

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources → `SKILL.md`
  §Round-17 (gate rows + falsify corrections); no non-author verifier.
- [~] End-to-end domain task logged → `SHONEN.md` box 2 round-17 pointer:
  `.ufo/waves/round-17/live/receipt-{1,2,3}.json` (v2, 11/11, four-pin `VALID`) and
  `tests/llamacpp-live/controls.py`; lane-owned control, not consumer reconciliation.
- [~] Instructions executable without oral context → `SKILL.md` §Round-17 rows (corrected
  by falsify `SkillRound17Rows.md`); independent execution review still open.
- [~] No cross-domain bleed → `PROVINCE.md` round-17 note; handoffs advised to kagi,
  tameshi, kumitate, kaidoku, operator (lesson §Falsify wave).

## Waves and seats

| Wave | Seats | Role mix | Terminal | Dead |
|---|---:|---|---|---|
| build | 82 | scout 19, executor 15, reviewer 14, scribe 10, connector 8, critic 6, revenger 4, sentinel 2, simplifier 2, mutation-tester 2 | 82 completed | 0 |
| falsify | 80 | reviewer 34, scout 8, critic 7, executor 6, connector 6, scribe 6, revenger 5, mutation-tester 4, sentinel 2, simplifier 2 | 71 completed, 9 failed (429 rate limit ×8, no final message ×1) | 7 without report: C1AdmissionCritic, C2AdmissionCritic, C2SourcedClaim, ControlsSafety, MistakesFailCapable, SeparabilityNoHarm (m_opus 429), TrendVerdicts |

Round total 162 ≤ 200. Both waves validated under policy v2 (`build/validation.json`,
`falsify/validation.json`: policy sha256 `70418a0f…`, version v2, band 64–100) and
dispatched as one task call each with the validator's `taskCall` unchanged (0 `model`
keys). Build: one refused call (job cap, 82 refused) then capacity-gated retries; falsify:
capacity-gated, no refused call. Routing changed mid-round by orchestrator notes (role
decides route); build seats ran on the routes of 15:15Z, falsify seats on those of 18:35Z.

## Mistakes and incidents

Lesson §Mistakes M1–M8: M1 S041 append-only violation (mined); M2 gate-overclaim class; M3
round-16 summary miscount; M4 async spawned count; M5 L1 wave-context premises unchecked;
M6 seat misroots/bound slips (cleaned; L1 misroot sweep `git -C … status --porcelain`
found no kama file at the fleet root at report time); M7 L1 measurement invocation; M8 L1
cited S043 past what its lines prove (S047).

## Tool installs

None by L1 or by any seat report this round (pacman pause respected). Observed on the host,
unattributed to kama: `uv tool` ruff 0.17.1 and vulture 2.16 (13:14 -03). Round-16 install
disclosure (routed defect 5): the operator-owned footprint includes the retained archive
`~/.local/opt/llama-b11755-bin-ubuntu-x64.tar.gz` (22,240,468 bytes, sha256
`753bfa7327a75b477d4d14cde71e0e46a40acc3a1408c5504530b78c33a6e226`, equal to the upstream
b11755 asset); no `/usr/bin/llama-server` exists, so the `~/.local/bin` link shadows nothing
(shell-local PATH check). Install untouched.

## Open L0 questions

- `kama | round-16 | Ratify or reject the lane-owned live llama.cpp fixture …` (still open).
- `kama | round-17 | …` appended this round: include the retained archive in round-16 (b).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
