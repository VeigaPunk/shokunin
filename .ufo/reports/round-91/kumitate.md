# kumitate — round 91 (attempt 1)

Lane `kumitate-shokunin` (orchestration & tooling; axes operability + coverage). Hyaku run 15, Linux host, fresh start (Amendment 35).
Lane commits: freeze `2b1b8bf3d274db8e608035bffb27bd3b3d4009d4`; wave spec + dispatch `2df92d8db51e17209658d946854b645560f0391b`; integration at measured revision M `77ebfe3794214fe06d8047f8698ffe0252f64461`; close receipts `74423664048843f85d98f34465c7a3d043d198b9`; final (post-report round-gate receipt) `1325caf47a25567afd076a49a232564485e4171e`.
Stale-lane: none (respawn-per-round driver; no other mission of this lane is open).
Round shape: one v1 wave `kumitate-r91-w1`, 12 seats, band 8–16 under `ufo-wave-policy.json`; the L1 holds the planner seat (the validator refuses `planner`).
Seat roles: executor 2, scribe 2, scout 1, connector 1, sentinel 1, reviewer 2, critic 2, mutation-tester 1. Attack share 5/12 (42 %: two reviewers, two critics, mutation-tester); connectors 1. Dead seats: none (12 results with substantive output, no DEAD/FAILED/TIMEOUT marker, `.ufo/waves/round-91/w1-results.json`). Residual call: none. Round total: 12 seats. WAVE-DONE received before this report.
Tool installs: none (node 24.21.0, prlimit, mkfifo, curl, git already present; no pacman, no sysctl change).

## Work performed

**Declared claims: 1.** **C1 — operability (lowest non-retired axis; integer 9, terminal under `f_O`), capability acquisition `receipt-bind` v5 (bounded external reads), sourced on S263/S264/S265.**
Verdict: **C1 UNMET — rejected-honest-stop.** Kill clause (d) of the frozen plan fired: three seat-built tools reach `C91_C1: HELD held=56/56` and each has a committed reproduction of a wrong verdict on an input of a declared class. No capability row. Operability stays 9; every coverage row stays 10; no axis harmed.

- Fresh-start reads before declaration: `corpus/lessons/round-{88,89,90}-verifier-spotcheck.md` (all rejected-honest-stops of this capability). Common root named in `.ufo/waves/round-91/plan.md`: the claimed behaviour was wider than the scorer's arms.
- Freeze `2b1b8bf3`: `plan.md` (claimed classes, not-claimed classes, predicate, kill rule), probe `probe/probe91-c1.mjs` (sha256 `3bd88e8e…3f4c`; probe90's 47 arms + 9 new arms, every arm scored in two fixture contexts A/B — the round-90 M3 fix), 14 pre-data controls `controls/table.txt` (generator `controls/run-controls91.mjs`): do-nothing v4 `UNMET 52/56`, refuse-all 8/56, refuse-external 49/56, type-only 55/56, cap-only 53/56, cap-edge-minus1 55/56, refuse-empty 55/56, bounded-nonblock 54/56, dev-prefix 54/56, the three round-90 constructions grafted with the RD-2 fix 54/56, 47/56, 47/56 (the context-gated ones fail 8 arms each as `A=PASS B=FAIL`), absent 0/56, positive control `controls/ref-fd-fstat.mjs` `HELD 56/56`.
- Wave dispatched via the inline handoff (`w1.ready` → `w1.ready.dispatched`; `w1-results.json`).
- K91ExecInst: v5 candidate `K91ExecInst/receipt-bind-v5.mjs` (sha256 `33ee29eb…`), 56/56 twice, selftest 83/83.
- K91ReviewProc (hypothesis SUPPORTED): `/proc/self/pagemap` aborts with no verdict and `/proc/<pid>/smaps` binds 35 MiB on the positive control — `st_size` 0 is not a read bound (`K91ReviewProc/hypothesis.md`). K91Sentinel reproduced it with `/proc/kallsyms` (22489015 bytes CLEAN past the cap) and re-ran A4–A8: v4 A4 OOM / A5 hang / A6 CLEAN / A7 20 laundered; candidate all refused, A7 0/120, A8 0/150 hangs (`K91Sentinel/attacks.md`).
- L1 integration: v5 + a chunked read bound (refuse once > 16777216 bytes arrive) + selftest arm `external-pseudo-file-unbounded`; integrated sha256 `f39aab5c…6cc5e1`, selftest 84/84 (`scripts/receipt-bind.mjs` at `77ebfe37`).
- K91CriticA (decisive): `cand-extsh-gate`, `cand-capwindow`, `cand-dirhash` each 56/56 ×3; reproductions (FIFO without `.sh`: no verdict; 16781312-byte over-cap: CLEAN; non-empty directory: CLEAN) committed as git bundles `K91CriticA/repro/*.bundle` (heads `K91CriticA/repro-heads.txt`); L1 re-ran three reproductions and one 56/56 score: `close-l1/l1-rerun-criticA-repros.txt`.
- K91Reviewer: no in-class hole in probe or positive control; F1 (no external symlink-leaf arm), F2 (`--ctx` visible via `/proc/<ppid>/cmdline`, harmless: 2/56) routed. K91Mutation: 11 mutants, 7 killed, 5 survivors equivalent-on-suite (`K91Mutation/mutants.txt`). K91CriticB: v4 vs positive control AGREE 43/43 close dirs and 479/479 receipts — NO HARM (`K91CriticB/harm.md`).
- K91ExecCarry: round-90 gate repaired at the landed tree (`round-gate --round 90` CLEAN); round-90 spot-check uncovered → adopted (`spotcheck-adopt --adopt … wrote=both`); v4 reference list for the v5 bump. K91Scout recon (`K91Scout/recon.md`). K91Connector: no sibling owns the claim; adjacency — tabi `check-receipt-provenance.mjs:53` carries the RD-2 class (reported, not edited).
- Mistake fix shown able to fail: `close-l1/class-sampler.mjs` (≥ 6 randomized members per class): the three 56/56 constructions UNMET on both runs, v4 24/36, v5 and positive control `HELD 36/36` twice (`close-l1/class-sampler.txt`).
- Frontier: knowledge `corpus/knowledge/receipt-bounded-external-reads.md` (S263–S265); QUALITY Q84, Q85; lesson `corpus/lessons/round-91.md` (Gate, Mistakes M3/M6/M7/M8).

## Landed changes

| change | file(s) | LOG.md entry | commit |
|---|---|---|---|
| frozen plan, probe91, 14 controls + positive control, census-start | `.ufo/waves/round-91/{plan.md,probe,controls,open}` | round 91 section | `2b1b8bf3` |
| wave spec + validated dispatch | `.ufo/waves/round-91/w1-{spec,dispatch}.json` | round 91 section | `2df92d8d` |
| receipt-bind v5 (descriptor open `O_RDONLY\|O_NOFOLLOW\|O_NONBLOCK`, fstat type/size refusal, chunked read bound, receipt `O_NONBLOCK`; selftest 76 → 84) | `scripts/receipt-bind.mjs` | round 91 one-line record | `77ebfe37` |
| SKILL gate row + checklist item → v5 | `SKILL.md` | round 91 | `77ebfe37` |
| QUALITY Q84 (two contexts), Q85 (class sampling) | `corpus/QUALITY.md` | round 91 | `77ebfe37` |
| SOURCES S263, S264, S265 (mined) + captures | `corpus/SOURCES.md`, `.ufo/pins/source-captures.json`, `.ufo/waves/round-91/close-l1/sources/` | round 91 | `77ebfe37` |
| knowledge entry (new); S260 verbatim-quote and S255 line 70 → 75 corrections (append-only) | `corpus/knowledge/receipt-bounded-external-reads.md`, `receipt-invisible-prefix-fields.md`, `receipt-lane-membership-and-link-binding.md` | round 91 | `77ebfe37` |
| round-90 spot-check adoption; map rows for the two new notes | `corpus/README.md`, `.ufo/pins/readme-map.json` | round 91 | `77ebfe37` |
| SCORECARD: `pin.receipt-bind` → `f39aab5c…`, `A_wave` 1253 → 1319, `C2`/`C2_total` 230 → 233, move-log row 91, round-91 section, round-92 pre-registration, `## Planned` pointer | `SCORECARD.md` | round 91 | `77ebfe37`, `74423664` |
| lesson round 91 | `corpus/lessons/round-91.md` | round 91 | `77ebfe37`, `74423664` |
| wave evidence (12 seat dirs, results), close battery, close-l1 receipts | `.ufo/waves/round-91/**` | round 91 | `77ebfe37`, `74423664`, `1325caf47a25567afd076a49a232564485e4171e` |

## Before → after measurements

**C1** — counting command `node .ufo/waves/round-91/probe/probe91-c1.mjs --lane . --work <scratch> --alt /fast/scratch/hyaku --rev <REV> --tool <tool>`:
- Before (do-nothing, v4 at `0bff4bab`, measured at freeze `2b1b8bf3`): `C91_C1: UNMET held=52/56` exit 1, failing `ext-zero ext-null ext-fifo ext-overcap` (`controls/ctl-base-v4-at-rev.txt`).
- After (integrated v5 at M `77ebfe37`): `C91_C1: HELD held=56/56` exit 0 twice, `RUN_CLOSE: PROBE_DETERMINISM SAME` (`close/probe1.txt`, `close/probe2.txt`); selftest `PASS held=84/84` (`close/selftest.txt`).
- Kill rule: clause (d) fired — three constructions 56/56 with in-class reproductions (above). **UNMET.**
- Other gates at M (`close/`): `PROXY: MATCH --strict (A=36 C=46 operability=9; C2=233/233 coverage=10; … coverage:omp=10; pins=6 match)`; `SOURCES_CHECK: CLEAN rows=203`; `SOURCE_CAPTURE: CLEAN captures=92`; census `kumitate ok` exit 0; `COUNTER_PINS: CLEAN pins=45`; `README_MAP: CLEAN files=233 rows=233 covered=233`; bind `RECEIPT_BIND: CLEAN matched=12 … external=1`, 12 of 12 others. Reds, recorded as reds: `CHECKLIST: 43/46` (737 operator-owned `~/.omp/agent`; 756 host-bound; 739 cap-run red at load1 12.70 and `12/12 PASS` on a direct rerun, `close-l1/cap-run-direct.txt`); `round-gate --round 91` DRIFT `REPORT_MISSING` only (pre-report; post-report run in `close-l1/round-gate-r91-final.txt` at `1325caf47a25567afd076a49a232564485e4171e`); `plan-before-ready` FAIL `MAP_DRIFT` at the plan commit (spot-check adopted after the freeze — mistake M8).
- Axes: operability 9 → 9; coverage rows 10 → 10.

## Sources & frontier

- Census start (`open/census-start.txt`): `kumitate ok`, exit 0 (7 pinned W04). Census end: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` → `kumitate ok`, exit 0 (`close/census.txt`).
- Rows before → after: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **200 → 203** (base `0bff4bab` vs `77ebfe37`).
- Added by tier: A +3 (S263 fifo(7), S264 open(2), S265 Node.js v24 fs), status `mined`, used-by the new knowledge entry. Rows touched old→new: none (S260 and S255 corrections are append-only notes in their knowledge entries). Gate quotes, URLs, access date 2026-11-05 and sha256: `corpus/lessons/round-91.md` `### Sources opened this round`.
- Frontier rows advanced: none; the entry deepens the receipt-binding band already held.
- Sourced claim: C1 rests on S263–S265 (knowledge entry cites them).
- Mistake mined: M3 (round 90), M6 (round 90), M7 and M8 (this round), each with captured-by and a shown-able-to-fail receipt.
- Assimilation: none (one claim; package adoption not this round). considerthese: not mined this round.

## Trend verdicts

- **expansion — unchanged.** +3 source rows and one knowledge entry on a held band; no capability row.
- **quality — improved.** v5 closes RD-2 with red-before (v4 52/56; A4 OOM, A5 hang) and green-after (56/56 twice, 84/84 selftest, procfs read bound), NO HARM over 43 dirs / 479 receipts; Q84/Q85 admitted with shown-able-to-fail receipts; S260/S255 corrections landed. Tempered: instrument quality, not an admitted capability.
- **discernment — unchanged (pending non-author spot-check).** The frozen kill rule fired and was honored without narrowing; the lane's own plan missed the single-token class weakness (M7) and the adopt-before-freeze recurrence (M8).

## SHONEN

`SHONEN.md` has four boxes; none has a named non-author verifier this round.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:646` (gate row, v5) and `SKILL.md:763` (checklist item, v5).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 91" section (close battery at M `77ebfe37`, `.ufo/waves/round-91/close/`).
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-91/close/checklist-items.txt` (46 items); `close-runner/run-close91.mjs`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged (`git diff 0bff4bab -- PROVINCE.md` empty); connector ruling `w1/K91Connector.md` (no overlap on the claim).

## Routed defects and carried items

- Round 92: re-claim only under a class-sampling, two-context counter including procfs members; commit the three round-91 constructions as pre-data controls; adopt the round-91 spot-check BEFORE the freeze (M8).
- K91Reviewer F1/F2; CriticA `cand-shy-strip` (U+00AD); mutation survivors m02/m07/m10; RD-1, RD-5; tabi adjacency (`check-receipt-provenance.mjs:53`).
- Round-90 §6 items: 1 repaired (`close-l1/round-gate-r90.txt` CLEAN), 2 repaired (M3 two contexts, M4 mid-token arm), 3 and 4 repaired (append-only corrections), 5 re-run (K91Sentinel), 6 not repeated (this report states seat outcomes from results, not a status marker).

## Operator / host notes

- L0 questions: none appended.
- Host sysctls untouched. Seat nested `.git` dirs (K91CriticA/repro) converted to bundles before commit.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): untracked `.ufo/reports/round-45/kagi.md` and `w4lines.txt` belong to other lanes (no kumitate content); nothing moved.
- Origin pin `/fast/scratch/hyaku/kumitate-pin/src` recreated at `31c465f1` per `.ufo/pins/origin.json` for the proxy.

## Pre-report gate

- `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin ls-remote origin refs/heads/master` → `1325caf47a25567afd076a49a232564485e4171e`.
- `grep -c '^## SHONEN'` → 1, four `[~]` lines.
