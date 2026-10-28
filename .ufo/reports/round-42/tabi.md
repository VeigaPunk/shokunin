# Round 42 — tabi

**Disposition: not admitted — honest stop (4th consecutive). Both frozen claims were
refused under their pre-declared kill rules; the round's repairs and evidence are
landed, measured, and the refusal paths are routed to round 43.**

## Work performed

Declared claims (frozen before any seat data at `9b6de3a19de11abdb80e82a1310abc64a40215bb`,
baseline `34e177959d1b7ce04afb85a001420e02631ce79e`, `.ufo/waves/round-42/claims.json`):
**C1 coverage capability** — admission attempt of the frozen round-41 Playwright Firefox
loopback TCP chain on committed bytes with a settled attack wave (stagnation nudge
active: all axes ≥ saturation 8, no capability entered rounds 39–41, so the
lowest-axis obligation was waived and C1 was the frontier move); **C2 calibration** —
closure of the round-41 verifier's routed defects D1–D4, measured by a frozen checker.
Fresh-start round: the r39–r41 reports and the round-41 verifier spot-check were read
before declaring; both claims were sized so a do-nothing control cannot reach them
(C2's baseline red control is committed; C1's baseline tree count is 0).

- froze C1/C2 predicates, kill rules and counting commands pre-data; baseline red
  control `controls/c2-baseline-red.json` (exit 1, 7 findings at the baseline rev);
  sentence identity across claims.json / checker header / checker code audited by
  `w1/CritPredicateSentence` — `tabi-shokunin/.ufo/waves/round-42/claims.json`.
- landed the D1/D2/D3 repairs at the freeze commit: r41 receipt+witness committed as
  explicit files (sha256s equal the committed r41 measure record), S148
  `supersedes S146` with a verbatim quote + S146 flipped rejected, baseline control
  populated with its counting command and the 0 — commit `9b6de3a19de11abdb80e82a1310abc64a40215bb`.
- opened S149 this round by the L1 (git-ls-tree docs; HTTP 200, 38,955 B, sha256
  `2c298383476164238c6e25ba804412a335c405ab9540650bb603778e2f4f8b64`; verbatim
  13-word quote) and landed the sourced note
  `corpus/knowledge/committed-bytes-verification-round-42.md` + README coverage row
  (the round's sourced claim) — commit `9b6de3a`.
- ran the C1 pre-data controls: battery all-pass (5 vectors exit 2, clean exit 0),
  r39/r40/r41 receipt replays refused under fresh nonces
  (`.ufo/waves/round-42/controls/c1-*-r42*`), then the live measurement: exit 0,
  predicate true, findings empty, two real Firefox runs spanning 16,356/17,790 ms
  (`corpus/evidence/round42/playwright-egress/`, `measure/c1-measure.json`) —
  commit `236c4f49f6cf8be7fd2efc71c7e89b7465b47a27`.
- validated and dispatched one policy-v2 wave (64 seats; dispatch JSON carries
  `taskCall`, verified by `w1/ExecWaveAudit` — the r41 ready-pointed-at-spec defect
  did not recur); the inline dispatcher stalled ~18 min and the orchestrator consumed
  the ready manually (kama r61 precedent); WAVE-DONE received; **64/64 seats settled,
  0 dead, 64/64 nonempty reports with VERDICT lines (21 ok / 43 finding)** —
  commits `236c4f4`, `435b64c90406e46a0e3573a36744110420f862f4`.
- **C1 refused by its kill rule**: `w1/CritC1Reach` reached counter exit 0 / predicate
  true three ways with zero browser runs (r41 bytes relabeled, r42 bytes relabeled,
  hand-written receipt naming pid 1 as firefox); `w1/CritC1Witness` and
  `w1/RevWitnessProbe` greened a 4-scalar nonce patch and fully synthetic
  receipt+witness pairs; `w1/MutC1Counter` added the unpinned `--pins` hole. The
  in-process nonce binds only the live wrapper invocation. No capability row.
- **C2 refused as worded**: the four repairs are closed and seat-verified
  (`w1/RevReceiptBytes`, `w1/ExecQuoteVerify`, `w1/ExecBaselineCount`, 38/38 fresh
  quarantine verdicts), the checker survived all seven mutation attacks
  (`w1/MutC2*` — every clause load-bearing), the adversarial CLI battery
  (`w1/SentC2Checker`) and the synthetic selftest (`w1/ExecSelftestSynthetic`,
  32/34 finding ids, positive control green); but `w1/CritPredicateSentence`/
  `w1/RevC2Freeze` demonstrated the counter accepts tree objects where the frozen
  sentence says "committed blob", and `w1/CritC2Ledger` (V0) demonstrated a
  self-consistent fabrication greens all rules — the kill rule's fabrication limb.
  Checker exit 0 at `435b64c` is recorded as instrument pass, not admission.
- completed D4: fixed the slice extraction (trailing-backtick S171 bug; red/green in
  `w1/MutSliceExtraction`, independent re-derivation `w1/ScoutRegisterDrift`) and
  re-adjudicated all 38 staged rows via 19 scout seats — verdicts misbound 25 /
  absent 6 / partial 4 / present 2 / unreachable 1, per-row evidence files, TSV at
  `corpus/../.ufo/waves/round-42/quarantine/re-adjudication.tsv`; `w1/RevQuarCross`
  independently reproduced 7/8 sampled letters (the S135 divergence became QUALITY
  criterion 105). Package adoption stays closed; assimilation: none.
- recorded the standing-gate conflict: `scripts/check-c2-knowledge-round41.mjs` exits
  1 because its frozen pins describe the pre-D2 state the r41 closure routed as a
  defect — left unamended per no-post-data-amendment; `check-sources.mjs` clean
  (0 findings).
- no tool installs; no pacman transactions (pause honored); no sibling/fleet writes;
  `w1/ExecScratchGuard` found zero out-of-bounds seat writes.

## Landed changes

Every change is tied to the round-42 LOG.md entries (pre-dispatch entry + integration
entry) and landed through `jj-lane.sh --as tabi`:

- `9b6de3a19de11abdb80e82a1310abc64a40215bb` — claims freeze; routed-defects checker;
  D1 (r41 receipt+witness committed); D2 (S148 supersedes S146, S146 rejected);
  D3 (baseline control populated); S149 opened + committed-bytes note + README row;
  baseline red control; slice-ids + derivation; census-start receipt.
- `236c4f49f6cf8be7fd2efc71c7e89b7465b47a27` — C1 live measurement + battery/replay
  controls; C1/C2 pre-data controls; wave spec/gen/run-output/dispatch/registry/ready;
  LOG pre-dispatch entry.
- `0081bfdb93b6bd1bf2853bb128996f1a976b7218` — SCORECARD declared-claims section;
  TSV builder.
- `435b64c90406e46a0e3573a36744110420f862f4` — 64/64 wave results + seat reports;
  quarantine TSV; round-42 lesson (`## Gate` + `## Mistakes`); QUALITY criteria
  104–105; S146 teaches → REJECTED form; S148/S149 used-by; census-end receipt; LOG
  integration entry.
- `db91779b2d9d5a820a271a70683d099f9c0a1522` — SCORECARD executed disposition + final
  checker receipt.
- `227956616c5413f280cc43cdcf0e6bc8f30da8b6` — C1 receipt+witness committed at the
  measured state (closing the untracked-recurrence `w1/RevReceiptBytes` routed);
  late forgery-evidence files; orchestrator dispatch marker.
- `15b75a7337089ed42208555a71ed89a966b21932` — final tip: >1MiB RevWitnessProbe
  evidence files; wave-created self-symlink debris removed. **Lane HEAD = origin/master
  = `15b75a7337089ed42208555a71ed89a966b21932`, ahead 0, working tree clean.**

## Before → after measurements

- **C1 / coverage capability** — counting command
  `node scripts/measure-c1-round41.mjs --out corpus/evidence/round42/playwright-egress/receipt.json --scratch /fast/scratch/hyaku/tabi-r42/L1-measure/run`.
  Before at `34e177959d1b7ce04afb85a001420e02631ce79e`:
  `git ls-tree -r --name-only 34e177959d1b7ce04afb85a001420e02631ce79e -- corpus/evidence/round42 | wc -l` → 0
  (`controls/c1-baseline-tree-count.txt`); committed-r41-receipt replay refused, exit 1.
  After at the live run (2026-10-28) and committed at `227956616c5413f280cc43cdcf0e6bc8f30da8b6`:
  exit 0, driver 0, counter 0, predicate true, findings empty, spans 16,356/17,790 ms.
  **Verdict: not admitted — the kill rule fired** (four seats demonstrated the frozen
  counter's do-nothing reach over committed bytes; evidence pointers in the Work
  section). Coverage held 9 → 9; no capability row entered.
- **C2 / calibration** — counting command
  `node .ufo/waves/round-42/counters/check-routed-defects-round42.mjs --rev <REV> --repo /home/vgpnk/Projects/shokunin/tabi-shokunin --json`.
  Before at baseline: exit 1, 7 findings (`controls/c2-baseline-red.json`). After at
  `435b64c90406e46a0e3573a36744110420f862f4`: exit 0, predicate true, findings []
  (`controls/c2-final-r42.json`), with all 38 TSV evidence paths verified committed
  blobs. **Verdict: not met as worded** — the counter does not enforce the sentence's
  "committed blob" term (accepts trees) and cannot refuse a self-consistent
  fabrication; exit 0 is an instrument pass, not claim admission. Calibration held
  9 → 9. (Prose note: this report's Work section and claims.json name 5 baseline
  finding classes; the committed control lists 7 finding rows — the control file is
  authoritative, `w1/ExecSelftestSynthetic` flagged the discrepancy.)

## Sources & frontier

Required census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:

- Before (2026-10-28, pre-edit): **exit 0**, `tabi ok`, 20 W04 duplicate-URL warnings,
  no E findings — `.ufo/waves/round-42/measure/census-start.{out,err,exit}`.
- After (post-registry edits): **exit 0**, `tabi ok`, 21 W04 warnings (S148 shares
  S146's URL — expected) — `.ufo/waves/round-42/measure/census-end.{out,err,exit}`.

Row count command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`:
147 (r41 end) → **149**. Histogram (`w1/ExecCensus`): tiers A133/B7/C9 (was
A131/B7/C9); status mined 124 / queued 15 / rejected 10 (was mined 123 / rejected 9).

- Rows added by tier: **S148** (tier A, mined — supersedes S146; Node.js CLI docs,
  same URL as S146; quote `A space-separated list of command-line options.`, verbatim,
  byte-located at 243279 of the committed staged copy; opened 2026-10-28) and **S149**
  (tier A, mined — git-ls-tree manual; quote `Lists the contents of a given tree
  object, like what "/bin/ls -a" does`, 13 words, NAME/DESCRIPTION; opened 2026-10-28
  by the L1, opened copy + sha256 committed at `9b6de3a`).
- Rows touched old→new: **S146** status `mined` → `rejected`; used-by
  `corpus/knowledge/environment-injection-measurement-integrity-round-41.md` →
  `corpus/lessons/round-42.md`; teaches rewritten to the REJECTED form required by the
  lane's `check-sources.mjs` gate (old spliced quote preserved in git history and this
  round's lesson, which logs every transition). **S148/S149** used-by gained
  `corpus/lessons/round-42.md`. No other row changed.
- Frontier rows advanced: the committed-bytes instrument class moves from unnamed to
  held (`corpus/knowledge/committed-bytes-verification-round-42.md`, sourced by S149);
  the loopback-TCP capability remains frontier (C1 refused).
- **Assimilation: none** — the wave-4 quarantine-first re-adjudication is complete
  (38/38 fresh verdicts; misbound 25 / absent 6 / partial 4 / present 2 / unreachable
  1), and the fresh data keeps package adoption closed. No `merge/tabi/` row or entry
  appended. `considerthese/` absent (no such directory in this lane).
- Errors 0; warnings are the pre-existing W04 duplicate-URL family plus the one new
  S148/S146 share.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | New admitted note on uncovered ground (`committed-bytes-verification-round-42.md`, citing mined S149 opened this round); knowledge notes 58 → 59 (`ls corpus/knowledge/*.md | wc -l`); S148 correction row. No fabricated or bar-failing admission. |
| quality | improved | r41 routed defects D1–D4 closed with committed red→green proofs (baseline red control 7 findings → 0 at the final rev); S146 superseded by S148 (verbatim quote); D3 control populated; no admitted entry failed a re-check; QUALITY criteria 104–105 added from observed failures (`corpus/lessons/round-42.md`). |
| discernment | unchanged | The 38-row re-adjudication and `RevQuarCross`'s 7/8 independent reproduction are lane-internal (dispatched seats remain the lane); the outside non-author admit/reject spot-check is the closure's duty and is pending at filing. The S135 classification disagreement is captured as criterion 105, not smoothed. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Approval table, §Evidence ladder, §Runbook; unchanged this round; no new non-author verifier (closure pending).
- [~] At least one end-to-end domain task executed and logged in LOG.md — two real Playwright Firefox loopback runs with committed nonce-bound receipts (`corpus/evidence/round42/playwright-egress/receipt.json`, LOG round-42 integration entry); author-run, claim admission refused on instrument grounds.
- [~] Instructions executable by an agent without oral context — `scripts/measure-c1-round41.mjs` usage-contract red cases executed from the committed header alone (`w1/ExecC1ColdRunbook`: cases 1/2/4 exact; case 3 routed); no fresh independent cold-read promotion verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; `w1/ConnSiblingProc` refreshed the kama/souji overlap (nothing new to absorb); process/socket findings were routed, not absorbed.

## Stale-lane, wave shape, tooling, open questions, misroot, cleanup

- Stale-lane: respawn-per-round driver; this round is tabi round 42 (hyaku run 11,
  block target 51); no other mission of this lane is open.
- Wave shape: one policy-v2 wave `w1`, 64 seats (band 64–128 respected), one dispatch
  through the ready handoff, no residual call, round total 64. Role mix: scout 20,
  mutation-tester 9, executor 9, reviewer 8, critic 6, scribe 5, connector 4, sentinel
  1, simplifier 1, revenger 1; attack share 23/64 (35.9% ≥ 25%); L1 held the canonical
  planner seat; three connector seats plus `CritAdmissionPolicy` carried the bounded
  planning/overlap work. Dead seats: 0. Evidence: `.ufo/waves/round-42/w1-results.json`
  (status/note entries), `w1-parse-summary.json`, `w1/<Seat>/report.md`.
- Tool installs/updates: none. Playwright 1.64.0 / Firefox 157.0 already present; the
  pacman pause was honored (no pacman invocation by the L1 or any seat report).
- Open L0 questions (pre-existing, none assumed answered): `tabi | round-39` swarm-band
  template reconciliation; `tabi | round-39` shokuknow seat-artifact disposition;
  `tabi | round-40` F4 future-freeze guidance (partially executed this round — the
  wrapper scrub/binding held; the counter-scoring layer is the new routed surface).
  New question filed this round: the frozen-instrument vs routed-defect conflict
  (`check-c2-knowledge-round41.mjs` pins the pre-D2 state the round-41 closure ordered
  fixed) — recorded in `corpus/lessons/round-42.md` Mistakes 6 alongside the unanswered
  r27 quarantine/frozen-claim question.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator/other-lane paths (`.scratch/*`, `EXEC-MARKER`, `o.bin`, `oldrep*.out` —
  health-check output, no tabi/round-42 attribution); untouched. No tabi seat wrote at
  the fleet root (`w1/ExecScratchGuard` concurs).
- Cleanup: `/fast/scratch/hyaku/tabi-r42/L1-measure` and `L1-controls` removed after
  evidence landed in the lane; seat scratch dirs were seat-owned (trap/finally) —
  `w1/ExecScratchGuard` observed mid-wave trees only. Two wave-created self-symlinks
  (`corpus/knowledge/knowledge`, `corpus/lessons/lessons`) were removed and noted.
