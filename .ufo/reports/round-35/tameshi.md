# tameshi — round 35 report (hyaku run-5, fresh claim after stale-claim reset)

**Lane:** tameshi-shokunin · **Round:** 35 · **Base:** `51d3f08073be65d3475cf0286042fc0dbe4c4a7d` · **Tip (report write):** `5df962b32fec2c341df9757245a51a14176eb905` · **Measured content:** `34fa5b0cfe909f3cde644676ead723256281dd05` (C1 deciding, C2 re-run) and `d16f9b5a` (first C2 after)

**Lineage.** Eight `lane-dead-no-report tameshi round=35` lines (watchdog.log:977,989,1006,1019,1042,1061,1074 + the 2026-10-23 16:09/17:33 launches) — every earlier attempt of this round died with the orchestrator session (OOM/SIGSEGV freezes) **after** landing lane commits but **before** the report. This attempt inherits, re-verifies and folds; it re-ran every counter and the census gate at write time (2026-10-24, receipts in `/tmp/r35-*` this session, committed receipts in `.ufo/evidence/round-35/`). Reused (re-verified): the A1–A8 apparatus, both counters, the panel/sealed sets, wave specs/registries/reports, census receipts. Discarded: nothing — no inherited artifact failed re-verification.

## Work performed

Declared claims (2, distinct axes, causally separable — separate counters, no shared run):

1. **C1 — capability acquisition `tools/tally-audit-v3.py`** (depth: audit-surface detail; operability: runnable artifact). Audits the runner's regression tally across all four `(root,auto,KEEP)` triples, compares FULL stdout + exit, scans a comment-blinded code view, witnesses the runner's real auto root.
2. **C2 — self-assessment conformance, six declared mismatch classes** (calibration, the lane's lowest owned axis). m1 knowledge-header trio · m2 README index · m3 stranded seat file · m4 frozen-contract tool pin · m5 round-34 authoring adjudication · m6 standing sources-registry row count.

- Apparatus A1–A8 (all pre-data; contract `.ufo/evidence/round-35/contract.json`): four-config whole-stdout oracle; quote-aware `code_view`; real auto-root witness `/tmp/tameshi-r4-2-regression.…` (A4 — real shape is `tameshi-r4-2-regression.XXXXXX`); last-match depth-0 block locator (A7); leg-occurrence head rule; filesystem-safety execute gate; counter `TOOL_SHA256` re-pin (A6/A8). Evidence: commits `7267738`…`34fa5b0`, lesson `corpus/lessons/round-35.md` §"The change".
- Waves (dispatched by attempts 1–3 of this same round; this seat holds no dispatch tool per the accepted host mapping — the orchestrator dispatches prepared waves): **w1** one v2 wave, 64 seats, policy v2 (`spec-w1.json`, validator `spawn=64`), 6 reports survived the attempt-1 OOM → `.ufo/waves/round-35/w1/`; **w2** one v1 wave, 58 seats, policy v1 (`spec-w2.json`, validator exit 0), 54 reports committed at `5829676`, 4 outputs routed into A7/A8 instead of reports; **residual** 6-seat falsification wave, 5 reports in `.ufo/waves/round-35/residual/` (2 reviewers, 1 critic, 1 sentinel, 1 scout, 1 C2 reviewer). **Round total 128 spawn slots / 70 distinct items** (w1 64, w2 58, intersection 58, w2-only [] — the item-name sets verify the respawn). Dead seats: w1's 58 unreported seats (attempt-1 OOM, respawned as w2) and the residual sentinel (no report; respawned by the closure as `ResidualSentinelClosure`, not in-tree) — orchestrator losses, not seat refusals.
- C2 record repairs: knowledge header trios (×2 entries), README index rows, stranded round-34 seat file copied byte-exact into the lane (`cmp` equal) + fleet copy deleted, round-33 pin reconciliation record, round-34 authoring adjudication block, standing sources-registry row count replaced by a re-derivable command. Evidence: `git show d16f9b5a --stat`, lesson `## Mistakes` 1–2.
- Frontier: S102 opened (POSIX.1-2024 §2.3 Token Recognition), committed snapshot, Gate record in the lesson. Census gate run at round start and round end. Misroot sweep at the fleet root (§Sources & frontier).
- L1 re-verification at write time (this attempt): C1 before re-run, C1 deciding re-run at `34fa5b0`, tool selftest re-run, C2 base and tip re-runs, census start/end, cold-read monitor at base and tip, S102 snapshot hash, command D at tip — all agree with the frozen committed receipts (§Before → after).

## Landed changes

Every change ties to the LOG.md round-35 entry (`LOG.md` §"Round 35 — 2026-10-23 (TameshiR35, attempt 3)"):

- `d16f9b5` — `tools/tally-audit-v3.py` + frozen C1/C2 counters + C2 record repairs + S102 row/snapshot.
- `43aea03` — v2 wave evidence (64 seats, 53% attack, policy v2 exit 0) + C2 after receipt + inherited r34 seat report.
- `7267738`…`f9df589`, `23bd903`, `7da6e07`, `691bb51` — pre-data amendments A4–A7, A5/A6 counter re-pins, before/control receipts, sealed set + manifest.
- `1fc6cb7` — w2 spec + dispatch + validator receipts (58 seats, policy v1) + registry.
- `5829676` — A8 counter re-pin + 54 w2 seat reports.
- `34fa5b0` — A8 receipts re-run from final counter bytes (before exit 1; v2 control `0/6` kill `0/3` accept at `5829676d`; public-panel rehearsal).
- `5df962b` — **this fold:** LOG.md round-35 entry, SCORECARD.md round-35 section, `corpus/lessons/round-35.md` (Gate, 5 Mistakes, Holds), end receipts `.ufo/evidence/round-35/after/`, closure pin re-check `.ufo/evidence/round-35/closure/pins.stdout`, residual wave reports. Helper output: `landed 5df962b32fec2c341df9757245a51a14176eb905`.

## Before → after measurements

Counting commands re-executed at write time (2026-10-24); committed receipts agree.

**C1** — counter `python3 .ufo/evidence/round-35/c1/c1-measure.py --lane LANE --rev REV --work EMPTY_DIR --sealed .ufo/evidence/round-35/c1/sealed`:

- Before (base `51d3f08`): `C1_R35: mode=before tool_present=0 runner_sha_ok=1 rev=51d3f08073be65d3475cf0286042fc0dbe4c4a7d C1_R35_PASS=false`, exit 1 (committed `before/c1-at-base.stdout`; re-run `/tmp/r35-c1-before.out` identical, exit 1).
- Do-nothing control (v2 on the same 9-copy panel): `pub_kill=0/6 pub_accept=0/3 … PASS=false`, exit 1 (committed `control/c1-v2-control.stdout`) — cannot reach the target.
- After (tip `34fa5b0`): `mode=deciding … pub_kill=6/6 pub_accept=3/3 pub_slots=9 pub_distinct=9 ho_kill=4/4 ho_accept=3/3 ho_invalid=0 ho_distinct=7 sealed_after_freeze=1 … C1_R35_PASS=true`, exit 0 (committed `after/c1-at-34fa5b0….stdout`; **re-run this session: identical line, exit 0**, 133.8 s). Tool selftest re-run: `TALLY_AUDIT_V3_SELFTEST: 33/33 pass`, exit 0. Measured commit: `34fa5b0cfe909f3cde644676ead723256281dd05`.
- Disclosed predicate defects (routed, not patched): counter PASS weaker than the declared 6/3/9 target (`c1-measure.py:517`; receipt meets the stronger target); `code_view` clause not universal after ANSI-C `$'…'` quotes. Both filed by residual seat `ResidualCriticPredicate` (MAJOR ×2), recorded in SCORECARD + lesson Holds.

**C2** — counter `python3 .ufo/evidence/round-35/c2/c2-measure.py --lane LANE --rev REV --fleet FLEET`:

- Before (base `51d3f08`): committed `before/c2-at-base.stdout` `m1=8 m2=3 m3=1 m4=1 m5=1 m6=1 total=15 … C2_R35_PASS=false`, exit 1. Write-time re-run: `total=14`, exit 1, `PASS=false` — m1/m2/m4/m5/m6 fire identically; m3 reads 0 only because the round's own committed repair already removed the stranded fleet file (frozen receipt captured m3=1 while it existed). Before-state confirmed.
- After (tip `34fa5b0`): `m1=0 m2=0 m3=0 m4=0 m5=0 m6=0 total=0 … C2_R35_PASS=true`, exit 0 (committed `after/c2-at-final.stdout`; re-run this session identical, exit 0). First after at `d16f9b5a` (`after/c2-at-d16f9b5a.stdout`); hand re-derivation of all six classes in `residual/ResidualReviewC2.md` (all agree). Measured commit: `34fa5b0cfe909f3cde644676ead723256281dd05`.

**Numeric axes** (guardrails, measured): depth `9 → 9` — command D at tip prints `recorded_cases=9 depth_score=9` (re-run this session); the runner is byte-identical `a7d3f2dd…` at base and tip. Calibration `8 → 6` — cold-read monitor re-run: `calibration_restraint_score: 8, sections_covered 64/64` at `51d3f08` and `6, 60/64` at `34fa5b0`; four SKILL headings cite inputs this round's record repairs rewrote, so the frozen ledger withholds their credit by its input-drift rule (the exception is recorded in the lesson Holds; refresh routed to round 36). The stale `8` carried from rounds 29–34 is superseded by the measured `6`.

## Sources & frontier

Census command (both ends): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi` — **start exit 0, end exit 0**, final line `tameshi ok …/corpus/SOURCES.md` both runs.

- Rows **98 → 99**: `git show 51d3f08:corpus/SOURCES.md | grep -c '^| S[0-9][0-9][0-9] |'` → 98; tip and working tree → 99 (re-run this session). One row added, no rows touched or removed; tier delta A +1 (A38→A39, B 5, C 2 unchanged); frontier: S102 **mined** this round.
- **S102** — POSIX.1-2024 Shell Command Language §2.3 Token Recognition (spec, tier A): the normative `#`-comment rule grounding `code_view`'s comment-blanking. Opened 2026-10-23 UTC; 357,953 bytes; snapshot `.ufo/evidence/round-35/src/s102-posix-chap02.html`, sha256 re-verified `0889867a53fe12508a71e8739ec23ecdddc95e6f67697c98e26acc8ff0ec1acd`; located quote (≤25 words) in the lesson `## Gate`. C1 is the round's sourced claim (contract `sourced_by`: S102 + S097; S102 opened this round).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — fleet-root untracked files (`bm.json live.html live_s228.html nama.html s395.txt tf_bavelas.html unblob.log wb2.html write AGENTS.md`) inspected; **none names tameshi/round-35** (grep -il, exit 1) — nothing copied, nothing deleted; they belong to other lanes/operator. The one round-relevant misroot (r34 `ReviewDevReceipts.md`) was already repaired in-round (C2 m3, byte-exact `cmp`). `.ufo/state/*` and `watchdog.log` untouched.
- **Mined mistakes** (`corpus/lessons/round-35.md` `## Mistakes`, 5 rows): lane-relative path resolved from fleet root (captured-by C2 m3); inverted evidence pointer on later correction (captured-by C2 m5); pre-data amendment that silently no-opped in the counter (`7267738` line 165, caught by the control's `div=-` column); U+001E record-separator parser loss (caught by the counter's own pristine comparison); census-invariance prose contradicted by its own receipts (98→99, caught by closure re-read — disclosed as a seventh undeclared class, LOG corrected, C2 predicate unchanged).

## Trend verdicts

- **expansion: improved** — new mined tier-A source (S102) cited by the new capability and the lesson; the tally-audit-v3 capability enters the SCORECARD capabilities table (row admitted this round); audit surface widened from 2 to 4 runner configs + full-stdout tuple + comment-blind scans. Evidence: `corpus/SOURCES.md` S102 row; SCORECARD capabilities row; contract surface clauses (1)–(4).
- **quality: improved** — the runner audit now kills the two structural classes the r34 wave converged on (unswept `(0,0)`/`(1,1)` configs — the r34 seat-found `auto==0&&KEEP==0` accept swap is killed; comment text seizing the head/brace/`esac` locators is killed), measured 16/16 on behavior ground truth with a v2 do-nothing control at 0/6. Evidence: deciding receipt at `34fa5b0`; `control/c1-v2-control.stdout`.
- **discernment: improved** — C2 is a calibration move measured by its own counter: 15 self-assessment mismatches across six classes → 0, each repair located and hand-re-derived; five mistakes mined with captured-by criteria. Evidence: `before/c2-at-base.stdout` (15, exit 1) vs `after/c2-at-final.stdout` (0, exit 0); lesson `## Mistakes`.

No axis harmed: every other axis row in the SCORECARD round-35 section carries `unchanged` with a named bound; depth's numeric scalar is unchanged by design (9 recorded legs, runner byte-identical).

## Holds routed to round 36 (from the lesson, not this round's debt to close)

Head-side masks outside the block oracle (ANSI-C quotes / nested `$(…)` / backslash-newline hide executed assignments — needs a real shell lexer); stderr outside the compared tuple; removed-`workdir` side effect invisible to the tuple; tail region of `run_regression` uninspected; preamble seeding / helper-scope / name-assembled masks / per-index parsing recall classes; counter PASS cardinality asserts (frozen pre-data next round); cold-read refresh for the four drifted SKILL headings.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-1`); unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-2`); the round-35 LOG entry is the new logged task.
- [~] Instructions executable by an agent without oral context — lane assertion, input-keyed monitor only (`.ufo/evidence/round-21/coldread/ledger.json`); monitor re-run this session (60/64 sections at tip, input-drift rule; refresh routed to r36).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-4`); misroot sweep clean; siblings read-only.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none this session (no installs or upgrades by this attempt).
**Open L0 questions:** none appended; operator-owned `~/.omp/agent/mcp.json` left untouched per the brief.
**Round shape:** two waves + one residual wave inside the 1–3 claim cap (128 spawn slots / 70 distinct items); role mix per wave recorded above; dead seats named above. Admission remains the separate non-author closure duty.
