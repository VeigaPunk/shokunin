# kake — round 93 report (attempt 1, resumed after three L1 deaths)

Lane: kake (operability + freshness; calibration sub-axis). Repo: `/home/vgpnk/Projects/shokunin/kake-shokunin`, branch `master`.
Freeze: `bb8012fee38c0e497cdaf36337072737bca0b3cd`. Base: `10ecbd1ade91d0721e87a9942a66a2b61d5ce8d5`.
Lane tip cited by this report: `75effe7bbc1b77fbfcf80c09119c0680d9e224c9` (`git ls-remote origin refs/heads/master` = the same hash, checked after the lane commit).
Round shape: ONE v1 wave `w1` of 13 seats (band 8–16), no wave 2, no residual call. Round total: 13 seats.

## Work performed

Declared claims (2, distinct axes; frozen before any seat scored, see `.ufo/waves/round-93/freeze.md`):

- **C1 — calibration (lowest owned non-retired axis, HOLD 2): the lane's machine-checkable self-assessment matches the repo state it describes.** Counter `.ufo/waves/round-93/c93_selfassess.py`, predicate `.ufo/waves/round-93/c1-predicate.md`. Target: mismatches 0 across classes E1–E5.
- **C2 — freshness (HOLD 10), capability acquisition: a conditional request evaluation instrument (contract v1).** Counter `.ufo/waves/round-93/c93_conditional.py`, contract `.ufo/waves/round-93/c2-contract.md`, candidate `scripts/conditional_eval.py`.

No exploratory claim was declared.

Work items (each with its evidence pointer):

- Load and freeze: contract, predicate and counters committed at `bb8012fe` (`.ufo/waves/round-93/freeze.md`); pre-freeze controls `controls/base-c1.txt` (mismatches=20, exit 1), `controls/ctl-c1-selftest.txt`, `controls/base-c2.txt` (candidate absent, exit 1), `controls/ctl-c2-fixtures.txt`.
- Wave `w1` dispatched from `w1-dispatch.json` at 2026-11-04T22:26:45 (`w1.ready.dispatched`). Seat roles: reviewer 2 (ReviewC1, ReviewC2), critic 1 (CriticClaims), mutation-tester 1 (MutConditional), sentinel 1 (SentinelScope), executor 2 (ExecC1Fixes, ExecC2Tool), scribe 3 (ScribeC1Prose, ScribeEntry, ScribeSources), scout 2 (ScoutGround, ScoutContract), connector 1 (ConnectorScope). Attack seats 5/13 = 38 % (≥25 %). The L1 held the planner seat (validator refuses `planner`).
- C1 repairs (E3 and E5): `w1/ExecC1Fixes.md` — E3 metadata trio on `corpus/knowledge/meta-robots-directives.md`; six SKILL.md citations re-pointed or moved into `[r93-absence …]` spans (`repairs.diff`, `worktree-replica.txt`).
- C1 repairs (E1, E2, E4): `w1/ScribeC1Prose.md` — Gate heading, QUALITY criterion pointers, Mistakes-table contiguity in `corpus/QUALITY.md` and `corpus/lessons/round-{29,33,54,85,92}.md` (committed in `d838e744`).
- C2 candidate: `w1/ExecC2Tool.md` — `scripts/conditional_eval.py`, sha256 `d3bac7de…`, stdlib only, selftest 90/90 (`receipts/selftest.txt`); found and fixed two of its own defects (D1 quoted-comma tags, D3 non-UTF-8 stdin) before the final bytes.
- C2 knowledge entry and registry: `w1/ScribeEntry/ScribeEntry.md`, `w1/ScribeSources.md` (source-seat re-verification of the two RFC bodies, `cmp` identical), `corpus/knowledge/conditional-request-evaluation.md`, `corpus/SOURCES.md` rows S471–S476 (commit `4f5846fe`). The rows were appended only after a mirror gate: `sources-census.sh validate --file <mirror>` exit 0 (`w1/ScribeSources/quotes.json`, `all_ok=true`).
- Sidecar re-pin: `corpus/knowledge/freshness-sidecar.json`, three line-bound entries re-derived by `lineSha256` match (200→203, 128→131, 649→651), commit `4f5846fe`, per the handoff in `w1/ScribeC1Prose/sidecar-repin-for-L1.json`.
- Adversarial falsification of the instruments:
  - `w1/ReviewC1.md` and `w1/ReviewC1/Attack.md` — C1 counter met=true reachable by six fixture routes (F1 shadow `subprocess.py` via `sys.path[0]`, F2 canned wrapper, F3 cardinality-only pins, F4 silenceable `## Mistakes`, F5/F6 E3/E5 resolution), two live-capable at base.
  - `w1/ReviewC2.md` — candidate 162/162 agree on a contract-only battery written before the candidate existed; the frozen positive control `frozen/pos-good.py` scores 160/162 on that battery (R93-8).
  - `w1/recovered-partial/MutConditional/` — 40 mutants of the frozen reference: 31 killed, 9 survived (R93-7).
  - `w1/ScoutContract.md` — 18 contract ambiguities, 2 material refusal divergences from RFC text (R93-9, R93-10).
  - `w1/ConnectorScope.md` — no sibling-lane overlap for the seven C2 terms; adjacent empirical fragment in `tabi-shokunin` (81 raw hits), named, not absorbed.
  - `w1/recovered-partial/SentinelScope/escapes.txt` — partial probes; two escape probes returned information (R93-14).
- Lesson `corpus/lessons/round-93.md`: `## Gate` (admits and rejects; the L1's first Gate block carries three quoted line spans that do not contain their quote and one quote over 25 words — the source-seat block beside it carries the corrected spans, both kept, routed), `## Mistakes` rows 1–7, `## Wave review and Routed` (R93-1…R93-15).
- SCORECARD and LOG: `SCORECARD.md` capabilities row (Conditional request evaluation), move-log rows for 93, round-93 claims section; `LOG.md` round-93 entry.

Attempt history: `.ufo/watchdog.log` shows `lane-dead-no-report kake round=93` for attempts 1–3 (2026-11-05 00:52–00:53 and 02:18–02:19) and a relaunch at 10:33. The earlier attempts' uncommitted or unlanded outputs were inherited: the w1 wave files (reused after re-verification by re-running both counters at the current tip); the ScribeC1Prose late output (committed `d838e744`, subject says "not a landed round"; it left the freshness sweep at exit 2 — mistake 7); the ScribeSources row draft (appended only after the mirror gate). Discarded: nothing.

## Landed changes

| Commit | Change | LOG / evidence |
|---|---|---|
| `191ef8dd` | wave-1 spec (13 seats) and validated dispatch payload | LOG round 93; `w1-spec.json`, `w1-dispatch.json` |
| `bb8012fe` | freeze: two counters, C2 contract, fixture population, pre-freeze controls | LOG round 93; `freeze.md` |
| `5272c727` | preservation of in-flight wave outputs at the run-15 wrap-up (not a landed round) | `w1/…` |
| `d838e744` | ScribeC1Prose E1/E2/E4 repairs and sidecar spec (not a landed round; sweep exit 2 until `4f5846fe`) | `w1/ScribeC1Prose/`, mistake 7 |
| `4f5846fe` | registry rows S471–S476 (mirror-gated), knowledge entry, freshness-sidecar re-pin | LOG round 93 (frontier step); `corpus/SOURCES.md`; `corpus/knowledge/freshness-sidecar.json` |
| `75effe7b` | round-93 lesson `## Mistakes` 5–7 and `## Wave review and Routed`; SCORECARD verdicts and planned round; LOG entry; recovered partial receipts | `corpus/lessons/round-93.md`; `SCORECARD.md`; `LOG.md`; `w1/recovered-partial/` |

Scope guard: no change to `scripts/` at the fleet root, `templates/`, `.ufo/state/`, `.ufo/watchdog.log`, `MANIFEST.json`, or any sibling repo. No lane commit touched `considerthese/` (operator-authored, read only).

## Before → after measurements

**C1 — calibration (HOLD 2).** Counter: `python3 -B .ufo/waves/round-93/c93_selfassess.py --root . --revision <REV>`.

- Base `10ecbd1a` (do-nothing control, re-run this session): `C1v93 revision=10ecbd1a… lessons=87 entries=80 rows=255 criteria=39 mismatches=20 E1=1 E2=8 E3=1 E4=4 E5=6 pins=ok met=false`, exit 1.
- Measured at `75effe7b`: `C1v93 revision=75effe7b… lessons=88 entries=81 rows=255 criteria=39 mismatches=0 E1=0 E2=0 E3=0 E4=0 E5=0 pins=ok met=true`, exit 0.
- Score: stays 2 (HOLD). The counter's `met=true` is the frozen predicate's verdict. It is not a calibration proof: ReviewC1 falsified the instrument (R93-1…R93-6). Non-author spot-check owed; L0 question filed for the operator's ruling.

**C2 — freshness (HOLD 10), capability.** Counter: `python3 -B .ufo/waves/round-93/c93_conditional.py --root . --revision <REV> --work <scratch>`.

- Base control at the freeze revision `bb8012fe` (`controls/base-c2.txt`): `candidate=absent hand=0/44 generated=0/120 forgeries_refused=0/6 positive=refused … met=false`, exit 1.
- Measured at `75effe7b`: `C2v93 revision=75effe7b… candidate=present hand=44/44 generated=120/120 forgeries_refused=6/6 positive=admitted anti_table=ok population=ok seed=93 met=true`, exit 0.
- Tool selftest: `python3 -B scripts/conditional_eval.py --selftest` → `selftest 90/90`, exit 0.
- Score: stays 10 (HOLD). Capability row entered (SCORECARD Capabilities, first-working round 93). The frozen population misses 9/40 reference mutants and two legal input classes (R93-7, R93-8), so the frozen counter is weaker than its `met` suggests; not repaired after scoring.

No other axis was re-scored. No axis was observed harmed in the exercised checks.

Freshness sweep (protocol gate, not a claim): `node scripts/freshness-sweep.mjs --offline --section=paths` exit 2 at `d838e744` (`paths sidecar binding invalid: corpus/lessons/round-29.md:200`), exit 1 at `4f5846fe` and `75effe7b` with one unannotated miss (`~/projects` at `corpus/lessons/round-90.md:82`), the baseline miss the seat measured on master. Status-neutral conformance item.

## Sources & frontier

- **`corpus/SOURCES.md` rows before → after.** `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: base `10ecbd1a` 207, `75effe7b` 213.
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`: exit 0 before (`.ufo/waves/round-93/assimilation/census-before.txt`) and exit 0 at `75effe7b`; W04 advisories 31 → 37 (the six new rows re-scope `rfc9110.txt` and `rfc9111.txt`, already held).
- **Rows added by tier.** A = 6 (S471–S476; kind `spec`; RFC 9110 §13.2.2, §13.1.1–§13.1.4, §8.8.3.2; RFC 9111 §4.3.2; each opened 2026-11-05T01:26:51Z, HTTP 200, `cmp`-identical to the L1's bodies). Status `mined`; used-by `corpus/knowledge/conditional-request-evaluation.md`.
- **Rows touched old → new.** None. `status`, `recheck` and `used-by` of existing rows unchanged.
- **Rejections (kept as rows-with-reason in the lesson Gate, not appended):** the RFC-Editor errata pages (ground nothing about these clauses); a secondary precedence explainer (tier inflation); "the RFC fixes 304 body content" (proposition rejected).
- **Frontier rows advanced.** Conditional request evaluation (RFC 9110 §13) moves from open ground to bounded held ground for supplied values only (`corpus/README.md` §Round-93 frontier step). Still open: revalidation exchange (RFC 9111 §4.3.4), 304 header set (RFC 9110 §15.4.5), `If-Range`/`Range`, HTTP-date parsing, validator generation, live CDN/browser observation.
- **Sourced claim.** C2 rests on S471–S476 (the knowledge entry cites them in its `source:` line).
- **Mistake mined.** Lesson `## Mistakes` rows 5–7 (scratch mirror construction, E11 false failure from absent non-corpus targets, the sweep-at-`d838e744` regression). Captured-by and fix recorded per row; row 7 has `captured-by: none` and names the fix.
- **Assimilation:** none. `merge/kake/SOURCES.append.md` collides with the registry on eight ids (`.ufo/waves/round-93/assimilation/collisions`; 129 staged ids from S287). No package row appended. The collision guard, the required proof, and the quarantine slice were not run this round; they are owed to a round that adopts from the package.
- **considerthese:** one proposal allowed; none taken. `considerthese/2026-11-05.md` proposal 3 (held-out vs frozen divergence column) is named as the successor to R93-7/R93-8.

SOURCES: rows 207 → 213 (see above); census exit 0 before and after.

## Trend verdicts

- **expansion: improved.** New primary-source ground on the freshness/conditional-request surface (six A-tier rows, one knowledge entry, one held capability). Evidence: `corpus/SOURCES.md` S471–S476; `corpus/knowledge/conditional-request-evaluation.md`; SCORECARD Capabilities row; `corpus/README.md` §Round-93 frontier step.
- **quality: improved.** C1 self-assessment mismatches 20 → 0 at `75effe7b` (E1–E5 each 0); the new entry carries the source/verified-at/recheck trio; the sidecar re-pin restores the freshness sweep's line bindings. Limits: the C1 counter is falsified as an instrument (R93-1…R93-6), so the quality gain is the measured repo state, not a verified counter.
- **discernment: unchanged.** No non-author spot-check of this round's gate decisions exists (owed to closure per LEARNING.md). The instrument that admitted C1 is falsified; the C2 frozen population misses nine reference mutants and two legal classes; the lesson's own Gate carries a span defect the source-seat block corrects. The round records these disagreements, and none is a self-attested verdict.

## SHONEN

Per-box assessment for `SHONEN.md` (not edited; the canonical seed is preserved):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/knowledge/shonen-ledger.json` row `box 1`; re-measured this round at `75effe7b`: SKILL.md E5 rows 0 mismatches (`c93_selfassess.py` E5=0), SKILL.md change limited to absence annotations (`w1/ExecC1Fixes/repairs.diff`).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched this round (`corpus/knowledge/shonen-ledger.json` row `box 2`, status `gap`).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/shonen-ledger.json` row `box 3`; the new `scripts/conditional_eval.py --selftest` is a runnable check (`receipts/selftest.txt`, 90/90).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/knowledge/shonen-ledger.json` row `box 4`; ConnectorScope found no sibling-lane overlap for the C2 terms (`w1/ConnectorScope.md`).

## Round-shape, seats and dead seats

- Round shape: one v1 wave `w1`, 13 seats (band 8–16), attack seats 5/13 (reviewer 2, critic 1, mutation-tester 1, sentinel 1). The freeze text said 12 seats; the dispatch file has 13 (count drift, no predicate changed). No residual task call. No wave 2 (the wave's own attacks supplied the falsification).
- **WAVE-DONE not received.** No `w1-results.json` exists, and this resumed L1 received no `WAVE-DONE` message; `wait` reports nothing pending. No w1 seat is live (`proc://`). Settlement is therefore evidenced by artifacts, not by the orchestrator's results file. The L0 question for the operator is appended to `.ufo/l0-questions.md` (`kake | round-93 | Two rulings and one handoff gap.`).
- Seats with a filed report in `w1/` (9): ScoutContract, ExecC2Tool, ExecC1Fixes, ScribeC1Prose, ScribeEntry, ScribeSources, ReviewC2, ReviewC1, ConnectorScope.
- Seats with no filed report (4), reported as unsettled, not as passes: ScoutGround (empty directory), CriticClaims (partial receipts), MutConditional (partial receipts; copied to `w1/recovered-partial/MutConditional/`), SentinelScope (partial receipts; copied to `w1/recovered-partial/SentinelScope/`). Last error text: unavailable — no results file. Their `agent://<id>` outputs returned blank or a preamble, and `agent://SentinelScope` returned another round's output (round 75), so no final text was used as evidence.
- Role-mix claim check: `agent://` outputs of ReviewC1 and ReviewC2 were read; their filed files were read in full.

## Pre-report checks

- `grep -c '^## SHONEN' .ufo/reports/round-93/kake.md` must print 1 (checked before commit).
- Lane gate: `git -C /home/vgpnk/Projects/shokunin/kake-shokunin ls-remote origin refs/heads/master` = `75effe7bbc1b77fbfcf80c09119c0680d9e224c9`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows ` M .scratch/run15-state.json` and `?? .ufo/closure-kaidoku-r92.json`. Neither carries kake round-93 content; both left untouched. No kake-round-93 file was found at the fleet root; the sweep copied nothing and deleted nothing.
- Scratch: `/fast/scratch/hyaku/kake-r93` removed after landing; every receipt cited is in the lane's wave dir.
- Tool installs: none. No pacman, no uv, no npm, no cargo.
- Host sysctls: no seat of this round's receipts records a sysctl change. [INFERENCE: the 2026-11-05 host incident concerns other lanes' seats.]
- Stale-lane: the respawn driver relaunched this round after three L1 deaths; this attempt was launched at 10:33 (`watchdog.log`). No other mission of this lane is open. Progressing: the lane commits listed above; silent seats are the four named above.
- Stale-lane line: mission respawned; progressing.

## Open L0 questions

- `kake | round-93 | Two rulings and one handoff gap.` — (1) settle `w1` (`results.json`) or accept the artifact-based settlement; (2) rule whether C1 (met on the frozen predicate; instrument falsified by ReviewC1) admits, is recorded `unprovable`, or waits for a successor counter.
- Routed to the successor (not questions): R93-1…R93-15 in `corpus/lessons/round-93.md` §Wave review and Routed.

## Mistakes

See `corpus/lessons/round-93.md` `## Mistakes` rows 1–7 (rows 1–4 found before the freeze; rows 5–7 found in this attempt). Row 7 is the sweep regression introduced by the lane's own late commit `d838e744`, fixed at `4f5846fe`.
