# kumitate — round 90 (attempt 1)

Lane `kumitate-shokunin` (orchestration & tooling; axes operability + coverage). Hyaku run 15, Linux host.
Lane commits: freeze `b67fa9639ca6537b92021ea938f769ff1ed6c883`; integration at measured revision M
`82c9c7efb9d9567341c209ad888012646590e99f`; close `bf24587c3e5a17f426b3b6c6dbea777eac054544` (final, pushed).
Stale-lane: none (respawn-per-round driver; no other mission of this lane is open).
Round shape: one v1 wave `kumitate-r90-w1`, 12 seats, band 8–16 under `ufo-wave-policy.json`; the L1 holds the planner seat.
Seat roles: executor 3, scribe 2, scout 1, connector 1, sentinel 1, reviewer 1, critic 2, mutation-tester 1. Attack share 4/12 (33 %: reviewer, two critics, mutation-tester). Dead seats: none (12/12 COMPLETE, `.ufo/waves/round-90/w1-results.json`). Residual call: none. Round total: 12 seats.
Tool installs: none (node, git, curl, sha256sum, bwrap already present; no pacman, no sysctl change).

## Work performed

**Declared claims: 1.** **C1 — operability (lowest non-retired axis; integer 9), capability acquisition `receipt-bind` v4.**
Verdict: **C1 UNMET — rejected-honest-stop.** The frozen kill rule fired on two seat constructions at 47/47, so no capability row enters the table. Operability stays 9; every coverage row stays 10. No axis is harmed.

Evidence, in order:
- Fresh-start reads before declaration: the non-author spot-checks of rounds 87, 88 and 89 (`corpus/lessons/round-{87,88,89}-verifier-spotcheck.md`) and the operator Amendment 27 (`.scratch/goal-20261103-hyaku-run15.md`). Round 89's pre-registration bound this round to a scorer that satisfies Q82.
- Plan frozen before data at `b67fa963`: `.ufo/waves/round-90/plan.md` (claim, 47 arms, kill rule, harm rules, limits); blind probe `.ufo/waves/round-90/probe/probe90-c1.mjs` (sha256 `70622333…f2b694`); 18 pre-data controls `.ufo/waves/round-90/controls/table.txt` (driver `run-controls90.mjs`).
- Wave dispatched via the inline handoff (`w1.ready`, `w1.ready.dispatched`; WAVE-DONE received; `w1-results.json`).
- Instrument v4 built by the executor (`.ufo/waves/round-90/K90ExecInst/`): `receipt-bind-v4.mjs` sha256 `35f4f25e6130dd827747ceff8ced80682d96c6c04d9516f2a463ce58cc7c1fce`; 76 selftest arms; diff in `diff-v3-v4.diff`. Integrated byte-identically into `scripts/receipt-bind.mjs` at `82c9c7ef` (`cmp` checked).
- Attack seat: reviewer `K90Reviewer.md` — whole-text strip of the six code points scores **47/47** and rewrites a mid-token instrument name (`cmd=scripts/legit\u200B.mjs` binds CLEAN to `scripts/legit.mjs`).
- Attack seat: critic A `K90CriticA.md` — context-gated tolerances (`TMPDIR` ancestor of `--dir`; `--dir` containing `/kumitate-r90/`) score **47/47** on two runs each. The probe header's Q82 claim (no round token in any candidate-visible path) is false for the mandated scratch root. Mistake M3.
- Mutation seat `K90Mutation/mutants.txt` — ten boundary-removal mutants of v3, all UNMET (`held` 34–39/47); one probe gap named (O_NOFOLLOW, declared out of scope).
- Harm seat `K90CriticB.md` — v3 vs the v4 stand-in on 131 committed receipt directories and 643 individually bound receipts: AGREE 131/131 and 643/643, **0 flipped verdicts**; a constructed mid-value U+200B and a trailing NBSP do not change verdict.
- Q82 audit seat `K90ExecAudit/` — `audit-clean.txt`: `Q82_AUDIT: CLEAN labels=47 scanned=130 hits=0` (exit 0); `audit-keyed-negative.txt`: `LEAK hits=161` (exit 1). The audit checks names only, not the scratch-root token (M3).
- Sentinel `K90Sentinel.md` on base v3: reproduced weaknesses routed (see Routed defects below); none claimed as fixed.
- Sources seat `K90ScribeSources/` — S260, S261, S262 with captured bytes and sha256; quotes ≤25 words; admitted to the registry (see Sources & frontier).
- Connector `K90Connector/overlap.md` — no sibling owns the claim; the claim is kumitate-owned (`PROVINCE.md:15`); "Q82" is a fleet-wide label collision, so cite it lane-qualified.
- Scout `K90Scout/` — touchpoints of `pin.receipt-bind` (`SCORECARD.md:338` only sha-carrying consumer); round-89 gate defects; the literal `68` is not in the instrument source (measured by receipt).
- Close battery `.ufo/waves/round-90/close/` (runner `K90ExecClose/run-close90.mjs`, 13 cases, run at the clean committed M): see Before → after.
- Frontier step: knowledge entry `corpus/knowledge/receipt-invisible-prefix-fields.md` (sourced on S258, S260, S261); Q83 admitted to `corpus/QUALITY.md`; lesson `corpus/lessons/round-90.md` with `## Gate` and `## Mistakes`.

## Landed changes

| change | file(s) | LOG.md entry | commit |
|---|---|---|---|
| receipt-bind v4 (field lines after a leading run of U+FEFF/U+200B..U+200E/U+00A0; contract `kumitate-receipt-bind-v4`; selftest 68 → 76) | `scripts/receipt-bind.mjs` | round 90 (one-line record + section) | `82c9c7ef` |
| round-90 frozen plan, blind probe, controls, driver, Q82 audit, wave evidence | `.ufo/waves/round-90/**` | round 90 section | `b67fa963` (plan/probe/controls), `82c9c7ef`, `bf24587c` |
| QUALITY Q83 (prefix class with positive and negative twins) | `corpus/QUALITY.md` | round 90 | `82c9c7ef` |
| knowledge `receipt-invisible-prefix-fields.md` (new) | `corpus/knowledge/` | round 90 | `82c9c7ef` |
| K89-V6 named correction (recheck `64/64` → measured `68/68` at v3, `76/76` at v4; append-only) | `corpus/knowledge/receipt-lane-membership-and-link-binding.md` | round 90 | `82c9c7ef` |
| SOURCES rows S260 (mined), S261 (mined), S262 (queued) | `corpus/SOURCES.md` | round 90 | `82c9c7ef` |
| captures for S260–S262 (sha256 recorded; `source-capture` CLEAN captures=89) | `.ufo/pins/source-captures.json` | — (gate artifact) | `82c9c7ef` |
| lesson `round-90.md` (Gate, Mistakes M1–M5) | `corpus/lessons/round-90.md` | round 90 | `82c9c7ef` |
| SKILL.md gate row and checklist item → v4, 76 cases, 47 arms | `SKILL.md` | round 90 | `82c9c7ef` |
| SCORECARD: `pin.receipt-bind` → `35f4f25e…`; `A_wave` 1210 → 1253; `C2`/`C2_total` 227 → 230; move-log rows 89 (gate repair) and 90; `## Planned` pointer; round-90 declaration | `SCORECARD.md` | round 89 gate line and round 90 record | `82c9c7ef`, `bf24587c` |
| round-89 gate repair (`SCORECARD_ROW_MISSING`, `LOG_ENTRY_MISSING`, `SCORECARD_PLAN_MISSING`) | `SCORECARD.md`, `LOG.md` | round 89 gate line | `82c9c7ef` |
| README coverage-map rows for the two new corpus notes; `readme-map.json` pins (228 → 230 covered; one restore from `b67fa963` after a truncating edit was caught and reverted) | `corpus/README.md`, `.ufo/pins/readme-map.json` | — (gate artifact) | `82c9c7ef` |
| round-89 K89-V5 repair: per-item checklist receipt (`close/checklist-items.txt`, 46 items) | `.ufo/waves/round-90/close/` | round 90 disposition | `bf24587c` |
| round-89 K89-V8 repair: every gate receipt cited with its verdict (this report, LOG, SCORECARD) | — | round 90 disposition | `bf24587c` |
| origin pin `kumitate-pin` recreated at `31c465f1` (official local clone; the pin directory had been removed) | `/fast/scratch/hyaku/kumitate-pin/src` (not lane-tracked) | — | — |
| spotcheck adoption of round-89 verifier spotcheck (`spotcheck-adopt --adopt`, `wrote=both`) | `corpus/README.md`, `.ufo/pins/readme-map.json` | — | `82c9c7ef` |

Not landed (routed): K89-V7 (S255 quote-location drift) — not repaired this round; carried.

## Before → after measurements

Every number below is a counting command or a verdict line; the commit it was measured against is named.

**C1 (receipt-bind v4; operability):**
- Before, do-nothing control = committed v3 at base `7218699c`:
  `node .ufo/waves/round-90/probe/probe90-c1.mjs --lane . --work <scratch> --rev 7218699cfbdec702ba42f35ceac0a8e52d1bd564 --tool <v3 at base>` → `C90_C1: UNMET held=39/47` exit 1; failing arms are exactly `dup-feff dup-zwsp dup-zwnj dup-zwj dup-lrm dup-nbsp single-zwsp single-nbsp` (`.ufo/waves/round-90/controls/ctl-base-v3-at-rev.txt`, measured at `b67fa963`).
- After, integrated v4 on the lane at M `82c9c7ef`:
  `node .ufo/waves/round-90/probe/probe90-c1.mjs --lane . --work <scratch> --rev 82c9c7ef… ` → `C90_C1: HELD held=47/47` exit 0 (run 1 and run 2; `close/probe1.txt`, `close/probe2.txt`; `RUN_CLOSE: PROBE_DETERMINISM SAME`).
- Lane selftest: `node scripts/receipt-bind.mjs --selftest --work <scratch>` → `RECEIPT_BIND_SELFTEST: PASS held=76/76` (`close/selftest.txt`); base v3 selftest `held=68/68`.
- Kill rule (frozen, decisive): reviewer `cand-1-global-strip` → `C90_C1: HELD held=47/47` exit 0 (`K90Reviewer.md`); critic `d-tmpdir-gated-prefix` and `e-round-path-gated-prefix` → `HELD held=47/47` exit 0 on two runs each (`K90CriticA.md`). Verdict **UNMET**.
- Bind over committed receipts: `node scripts/receipt-bind.mjs --dir close --rev 82c9c7ef… --lane .` → `RECEIPT_BIND: CLEAN matched=12 mismatched=0 unchecked=0 external=1` (12 of 12 others counted, `close/bind.txt`).
- Harm, base v3 vs v4 stand-in over committed receipts: 131/131 directories and 643/643 receipts AGREE, 0 flips (`K90CriticB.md`).
- Operability and coverage proxies at M: `node scripts/proxy-check.mjs --strict` → `PROXY: MATCH (A=36 C=46 operability=9; C1=19/19 C2=230/230 coverage=10; S=88/88 coverage:script-layer=10; R=92/92 coverage:runtime-layer=10; K=55/55 coverage:kimi-layer=10; O=1/1 O_members=65 O_findings=0 O_bound=35 coverage:omp=10; pins=6 match; source=snapshot)` exit 0 (`close/proxy.txt`). Before: operability 9, coverage rows 10.

Other gates at M (`close/`, each quoted with its verdict):
- `SOURCE_CAPTURE: CLEAN captures=89 exemptions=111` (exit 0), `SOURCES_CHECK: CLEAN rows=200 tiers=A:168,B:22,C:10 status=queued:14,mined:158,rejected:28` (exit 0), `census: kumitate ok …corpus/SOURCES.md` (exit 0, 7 pinned W04), `COUNTER_PINS: CLEAN pins=45`, `README_MAP: CLEAN files=230 rows=230 covered=230`, `PLAN_BEFORE_READY_SUMMARY: pass=1 fail=0 na=0` at PLAN `b67fa963`.
- Checklist (`surface-probe --checklists`, per-item file `close/checklist-items.txt`): `CHECKLIST: 43/46 pass`, `VERDICT: FAIL`. The three reds, named with reasons: item 737 `OMP_CENSUS` (two UNLISTED entries under the operator-owned `~/.omp/agent`; L0 on record from round 89); item 756 OMP live comparison (host-bound by design); item 739 cap-run — passes `CAP_RUN_SELFTEST: 12/12` and `VERDICT: PASS` on a direct rerun but was red inside the battery at `load1=11.77`. Recorded as reds, not passes.
- `round-gate --round 90`: `ROUND_GATE: DRIFT` at the close snapshot only because this report and the round-90 SCORECARD/LOG records did not yet exist; re-run after this report lands (see Pre-report gate).

**Coverage / operability axes:** no change (9 and 10).

## Sources & frontier

- SOURCES rows before → after: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **197 → 200** (base `7218699c`: 197; now 200). Malformed rows 0; duplicate ids 0 (`sources-census.sh validate … kumitate` exit 0).
- Rows added by tier: **A +3** (S260, S261, S262). B 22 → 22; C 10 → 10. A 165 → 168.
- Status: mined 156 → 158 (+S260, +S261); queued 13 → 14 (+S262, cited by no entry, kept queued); rejected 28 → 28.
- Rows touched old→new: none (no existing cell changed).
- Captured: S260 `unicode-tr44.html` sha256 `d951c7cf…a1ab4`; S261 `unicode-proplist.txt` sha256 `f438f532…d955d6`; S262 `man7-realpath3.html` sha256 `dd2bfafe…d702` (`.ufo/pins/source-captures.json`, `source-capture` CLEAN captures=89).
- Located quotes (in `K90ScribeSources/gate.md`): S260 "U+200B … reclassified from Zs (space) to Cf (Format)…" (§2.3.1); S261 White_Space entries at PropList-18.0.0 line 15; S262 realpath(3) §DESCRIPTION.
- Frontier rows advanced: none. The knowledge entry (`receipt-invisible-prefix-fields.md`) deepens the receipt-binding band already held in `corpus/README.md`; it does not enter an uncovered band.
- Expansion credit: none claimed (the new entry is on a held band).
- Assimilation: none. `considerthese/` (dated files `2026-10-19`…) and `merge/kumitate/` were not mined this round: the claim was frozen before this item was in scope and §10 work waits for the lane's next round.

## Trend verdicts

- **expansion — unchanged.** +3 admitted SOURCES rows and one knowledge entry, all on the receipt-binding band already held; no frontier band entered; no capability row. Evidence: the SOURCES counts above; `corpus/README.md` coverage map.
- **quality — improved.** The instrument gained the invisible-prefix class with red-before (base v3 `39/47`, failing exactly the eight arms) and green-after (v4 `47/47` on two runs; selftest `76/76`); Q83 is admitted with a red-before/green-after command; the K89-V6 correction is appended. No admitted entry was found false. Tempered: the claim is UNMET, so the gain is instrument quality, not a capability.
- **discernment — unchanged.** The frozen kill rule did its job: two constructions reaching 47/47 were recorded and the claim was not narrowed. The probe's own Q82 header claim, however, was false for the mandated scratch root (M3), and the lane's first Q82 audit checked names only. Both are calibration gaps that the lane recorded, not corrected by fiat. The outside non-author spot-check of this round's gate decisions is **pending** (`corpus/lessons/round-90.md` `## Gate`: "to be recorded by the non-author verifier"); no `agree`/`disagree` is claimed here.

## SHONEN

`SHONEN.md` has four boxes; none has a named non-author verifier this round.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:646` (gate registry row, v4) and `SKILL.md:763` (checklist item, v4).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 90 — measured disposition" (close battery at M `82c9c7ef`, receipts in `.ufo/waves/round-90/close/`).
- [~] Instructions executable by an agent without oral context — `SKILL.md` checklist items 718–763; `.ufo/waves/round-90/close/checklist-items.txt`; `K90ExecClose/run-close90.mjs` (13 cases).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round (`git diff 7218699c -- PROVINCE.md` empty); connector ruling `K90Connector.md` (kumitate-owned).

## Routed defects and carried items

- Routed to round 91 (counter versions, not edits to the frozen probe): **M3** (the candidate-visible `--work` root carries `kumitate-r90`; the probe's Q82 header is false) and **M4** (no mid-token or non-field invisible-code-point arm; the whole-text strip passes). Both are in `corpus/lessons/round-90.md` `## Mistakes`.
- Sentinel base-v3 weaknesses, not claimed here (`K90Sentinel.md`, routed RD-1..RD-6): A1 an absolute in-lane spelling launders the judged revision through an untracked worktree symlink (MED); A4 `cmd=node /dev/zero` unbounded memory, A5 FIFO unbounded time (MED); A6/A7/A8 bounded-read and TOCTOU rows (LOW); A9/A10 `GIT_REPLACE_REF_BASE` and `refs/replace/` redirect (LOW, RD-5 fix untested); A2/A3 external instruments are any readable file (design, DESIGN-1). Each must be re-run against any future candidate.
- K89-V7 (S255 quote-location drift): not repaired this round; carried.
- K89-V6: repaired (named correction, `82c9c7ef`).
- K89-V5 and K89-V8: repaired in this report and in `close/`.
- The probe-gap list from the mutation seat: O_NOFOLLOW single-descriptor read has no arm (declared out of scope; carried).

## Mistakes (mined; detail in `corpus/lessons/round-90.md`)

M1 fixture identity in candidate-visible paths (rounds 87–89; Q82 entered after the round-89 freeze); M2 invisible-prefix duplicates never armed (K89-V1; found by the sentinel after freeze); M3 probe header's no-round-token claim false for the mandated scratch root (not fixed; routed); M4 no mid-token or context invariance arm (not fixed; routed); M5 round 89 closed without its round-gate record lines (repaired). The fleet-root sweep found no misroot of this lane's (see below).

## Operator / host notes

- L0 questions appended this round: none. The round-89 OMP-census finding (operator-owned) remains on the L0 record.
- Host sysctl `user.max_user_namespaces` untouched (`122865`); no seat changed host state.
- Tool observation (not an install): `/usr/bin/xargs` (uutils 0.8.0) silently fails to execute scripts; the critic seat replaced it with a sequential runner. Recorded per the tooling directive; no tool was installed.
- Lane-side hygiene: one nested `.git` under the reviewer's fixture was archived to `K90Reviewer/step4/repo-with-blob-dotgit.tar` before commit (a nested repository cannot be committed as a path); the 8.9 MB connector grep output is committed gzip'd (`K90Connector/hits-E-blind-scorer.txt.gz`, 1.15 MB, committed as an explicit file).
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time): untracked `cited-lines.txt`, `run_check_probe.py`, `run_check_probe2.py` name other lanes (kengaku, a fuzzing paper); `.scratch/run15-state.json` and `.ufo/l0-questions.md` are modified by the orchestrator. None is this lane's and nothing was moved or edited.

## Pre-report gate

- Lane ls-remote (must equal the final lane hash): `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin ls-remote origin refs/heads/master` → `bf24587c3e5a17f426b3b6c6dbea777eac054544` (recorded at filing; `jj-lane.sh state` reports `local=remote=bf24587c…`, `ahead=0 behind=0`).
- `grep -c '^## SHONEN'` on this report → 1 (one heading, four `[~]` lines).
