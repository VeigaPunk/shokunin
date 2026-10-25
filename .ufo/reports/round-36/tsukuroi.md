# tsukuroi — round 36 report (attempt 1, 2026-10-24)

Lane HEAD at filing: `4b2d263685f7f363f3bcf0529e22ac65954b6052` (pushed; `jj-lane.sh state` clean).
Round shape: two v1 waves under `ufo-wave-policy.json` (band 32–64), each dispatched as exactly
ONE task call. Wave 1 = 32 seats (9 executor, 7 scribe, 3 scout, 3 critic, 3 reviewer, 2
mutation-tester, 2 connector, 1 revenger, 1 sentinel, 1 simplifier; §3 floor met; planner seat
held by the L1 per the orchestrator ruling). Wave 2 = 32-seat payload, 31 spawned (reviewer 9,
mutation-tester 8, executor 6, critic 4, scribe 3, sentinel 1, connector 1; 21/32 attack roles).
Round total 63 seats. Dead seats: W2ScribeRegistry (spawn-dropped, no error text), W2CritKill
(provider `cyber_policy` at 13s, error text recorded). No residual call.

## Work performed

Declared claims: **C1 (operability)** — the five live tools routed by the round-35 spot-check
(`check-revision-binding.py`, `check-report-receipts.py`, `score-census-handoff-r32.py`,
`mutants-btrfs-space-r30.py`, `run-receipt.py`) build every child environment from a fixed
dict, counted by the frozen probe `tools/probe-child-env-allowlist-r36.py` VERSION 7; **C2
(depth, exploratory — lowest-axis duty, depth tied adjacency at 8)** —
`corpus/knowledge/journalctl-v262-field-filter-r36.md`, the systemd 262 rejection of
`journalctl -F`/`-N` combined with limiting options, sourced on S198/S199 opened this round.

- C1 change design, review and landing: wave-1 `ExecC1Design` diff + `ReviewC1Design`
  corrections (LC_ALL, ceiling wording) + `SimplifierProbe` (`__import__('re')` rewrite) —
  landed at `c052bb7d`; AST-verified zero ambient reads on spawn paths (W2RevToolA).
- Counter `probe-child-env-allowlist-r36.py` VERSION 7 (freeze `1e926801`, sha256
  `a2a5acac…`): ExecProbeR36 draft + L1 integration (run-layout/underscore normalisation,
  five-target set with the livefive named parity limit, untraced channel) — evidence
  `.ufo/waves/round-36/l1/`.
- C2 note + S198/S199 rows + census validation — `c052bb7d`; matrix 54 cells
  (`.ufo/waves/round-36/w1/ScribeC2Draft/matrix-mini.json`), quote re-opens W2QuoteNews/
  W2RevSources AGREE.
- Routed repairs: round-35 tarball committed as evidence (`6d76fb20`); NoUpgrade supersession
  appends ×4 (`c052bb7d`, W2RevNoUpgrade verified verbatim); mori freshness re-read
  (`ScoutMori`, tip `13f3db7e`); gate baselines (`ExecGateBaselines`).
- Wave-2 falsification integrated: before battery 18/20 pairs leaking all-five (W2ReBefore);
  after-mutants m1–m6 ALL KILLED on exercised builders with ordinary-run leak checks; the
  QUALITY-82 live view at the change commit 0/5 tools leaking (W2LiveOracle); review-driven
  repairs XDG_RUNTIME_DIR (harm: systemd plane BLOCKED→running, W2RevToolB F2) and
  `env=dict(env)` visibility (W2RevToolA H1) landed `4b2d2636`.

## Landed changes (LOG.md entries ↔ commits)

Declaration `6d76fb20` (SCORECARD+LOG+tarball); wave-1 evidence `189d8a08`; freeze `1e926801`
(probe + claim/r33claim base receipts); change `c052bb7d` (five tools, note, S198/S199, four
appends, registry table, lesson, README row); wave-2 evidence `8d5fa7fe`; outcome `d39da87a`
(measured outcome + full wave-1/wave-2 evidence snapshot + lesson + registry repair);
verdict-final + repairs `4b2d2636`. Every entry has a matching LOG.md section; commit identity
`tsukuroi-shokunin <tsukuroi@shokunin.local>` via `scripts/hyaku/jj-lane.sh` only.

## Before → after measurements

- C1 before (W2ReBefore, receipt-backed): `python3 tools/probe-child-env-allowlist-r36.py
  --revision 6d76fb20 --set livefive` → **18/20 pairs leaking, all five targets > 0**,
  `harness_errors []` (measured at `d39da87a`-era receipts under seat dir, committed `d39da87a`).
- C1 after: per-tool pristine readings leaking 0 at `c052bb7` for check-report-receipts,
  mutants-btrfs-space, run-receipt (W2MutTool2/4/5); live-oracle 0/5 (W2LiveOracle); repaired
  score-census-handoff unit reading (probe `--only` at `4b2d2636`). **The declared full-battery
  after-value was falsified: W2RevToolA/W2MutTool3/W2RevCounter show the frozen counter reads
  `leaking 1` at `c052bb7` (source-channel parameter rule) — repaired at `4b2d2636`, but the
  full-battery invocation also crashes on target 1 (probe bug S1) and a do-nothing variant
  reads 0 (vacuity S3). C1 verdict: NOT VERIFIED** (honest stop; before>0 is receipted, the
  after target is unreachable by the frozen counter as shipped).
- C2 prior state: `grep -rl "cannot be combined with options that limit the journal"
  corpus/knowledge/ SKILL.md` → nothing at base (pasted in note); after: the note + 54-cell
  matrix (verdict: exploratory, correction-needed per W2RevC2/W2CritC2Depth — 15 terms, `-n`
  -F-vs-N distinction, action-override classification; corrections recorded for the closure).

## Sources & frontier

`scripts/sources-census.sh validate --root … tsukuroi`: start exit 0, 197 rows (02:26:45Z);
end exit 0, **199 rows**, 31 W04 advisories (unchanged class). Rows added by tier: **S198**
(docs, tier A, journalctl(1) at 262, semantics only) and **S199** (docs, tier A, systemd NEWS
pinned at tag v262, supersedes S024 for the note). Rows touched old→new: none (S024 left
queued and unchanged per the S196/S006 pinned-copy precedent; the change is logged in the
lesson). Frontier rows advanced: S024 remains queued for a future non-note purpose. Sourced
claim: C2 rests on S198/S199 opened this round (quote contract verified by W2QuoteNews).

## Trend verdicts

- **expansion: unchanged** — C2 adds mechanism ground on an owned journal surface (depth per
  W2CritC2Depth's ruling), no new surface; S198/S199 are tier A on owned ground.
- **quality: improved** — five tools' child builders are fixed dicts (AST-verified); the
  NoUpgrade supersession sweep landed verbatim (W2RevNoUpgrade); the XDG_RUNTIME_DIR live-harm
  was caught by a falsify seat and repaired with the plane back to `running`; census/gates:
  registry coverage PASS 53/53 at `4b2d2636`, census exit 0. Held back from stronger: the C2
  note's corrections are not yet applied, and the counter's own defects (S1/S3/S4) are new
  debt.
- **discernment: improved** — the lane applied its own kill rule against its claim (C1
  reported not verified on a counter-reading), all six after-mutants killed on exercised
  builders, the sensitivity GAP re-stated honestly (live-mode instrument), and every wave-2
  review finding is dispositioned in SCORECARD/LOG. Against: freeze documentary defect
  (R36-DOC-FREEZE) and the a-posteriori r33claim pick (S5), both mined.

## SHONEN

- [~] SKILL.md decision tables/sources — round36 registry table live (53/53 coverage PASS at
  `4b2d2636`); NoUpgrade correction blocks appended. Evidence: `SKILL.md` registry section.
- [~] End-to-end domain task — host census live run exercised via the livefive handoff mode
  (W2ExecCensusSelftest); prior e2e receipts stand. Evidence: `W2ExecCensusSelftest.md`.
- [~] Executable without oral context — the five fixed-dict builders and the probe are
  self-contained; no-oral-context retest of the whole SKILL remains unexecuted.
- [~] No cross-domain bleed — W2ConnAfter: no collision; mori S014/S160 neighborhood sentence
  landed in SOURCES.md; contested RE ownership untouched.

## Report extras

- **Stale-lane**: respawn-per-round driver; no other mission open.
- **Tool installs**: none by the L1; seats reported none.
- **Open L0 questions**: none appended this round (none required).
- **Inherited at filing**: W2ReAfter (full after battery) was still settling; its per-tool
  components are superseded by the receipts named above. The next round owes: probe VERSION 8
  (S1 clone-branch bug, S3 vacuity gate, S4 `os.get_exec_path` in OS_AMBIENT, parameter-aware
  source rule), the C2 note corrections (W2RevC2's five blocking items), and — per the
  orchestrator steer effective next dispatch — one v2 wave of 64 seats under
  `ufo-wave-policy-v2.json`.
- **Installs/updates**: none.
