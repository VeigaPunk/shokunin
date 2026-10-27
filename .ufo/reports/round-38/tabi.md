# tabi — round 38 report

## Work performed

Declared claims: **C1 calibration**, correcting/measuring the six round-37 verifier defects; **C2 coverage capability**, adding a Playwright Firefox/Juggler loopback evidence operation. C1 is **not met**; C2 is **unprovable/not admitted** because the runtime-evidence attack found that the receipt's egress/survivor telemetry is not sufficiently bound to the launched session. No claim is represented as admitted.

- Read the frozen round-38 claims at `.ufo/waves/round-38/claims.json` (freeze commit `a8e7d50c04254bb19f9de08b31ca2aa811fbe7fc`) and round-37 outside spot-check `corpus/lessons/round-37-verifier-spotcheck.md` (lane path; routed defects 1–6).
- Landed candidate counters and driver at `98239d0396ff32c3feb14638b3214fe688e8b122`; frozen claims at `a8e7d50c04254bb19f9de08b31ca2aa811fbe7fc`. The frozen calibration counter has defects of its own, identified by w1 and not amended after scoring.
- Ran the Playwright driver `node scripts/playwright-firefox-loopback-round38.mjs --out corpus/evidence/round-38/playwright-firefox/receipt.json --runs 2`: two first-shot hashes matched (`3e0c070a75f041986f63792a036addf08f0915b79713fd655499c601ec56378c`); the driver reported 0 non-loopback observations and 0 survivors. W1 attacks show those summary values are not conclusive session-bound egress evidence: PID discovery uses a global executable grep, sampling is every 400 ms and can miss brief connections, and a missing/empty PID set is not refused (reports `w1/Reviewer06.md`, `w1/Critic18.md`, `w1/Critic20.md`, `w1/Critic21.md`, `w1/Critic24.md`, `w1/Critic26.md`, `w1/MutationTester29.md`). Thus this is a demonstration, not an admitted capability.
- Opened S144 this round: https://playwright.dev/docs/browsers, §Firefox (accessed 2026-10-27; located quote: “Playwright doesn't work with the branded version of Firefox since it relies on patches.”). Registry row and sourced knowledge note: `corpus/SOURCES.md` S144; `corpus/knowledge/playwright-firefox-loopback-round-38.md`; index `corpus/README.md`.
- Dispatched one v2 falsification wave: **64 seats**, role mix 15 reviewers, 12 critics, 10 mutation-testers, 10 executors, 10 scribes, 4 scouts, 3 connectors. All 64 returned nonempty output; no dead seats (`.ufo/waves/round-38/w1-results.json`). The L1 held the planner seat; connectors carried the bounded overlap/planning scan. No second wave or residual call: the 64-seat v2 wave met the round band and the findings falsified the frozen claims; wave evidence is committed at `a6616d5f45f5312053c6d56ed2a95e32344f4948`.
- Re-derived quarantine slice with the specified `awk -F'|' …` extraction against the read-only absent-defect register: **38 rows**. This round did not hand-check every payload/source, so adoption remains closed and the quarantine-first requirement is recorded as a conformance defect; no package rows were appended. No `considerthese/` directory exists (directory check this round).
- The round-end census passed, but the assimilation quarantine's 38 rows were not individually adjudicated. Round-end census receipt is `.ufo/waves/round-38/measure/census-end.txt`.

## Landed changes

- `98239d0396ff32c3feb14638b3214fe688e8b122` — round-38 candidate counters and Playwright Firefox driver; LOG round-38 opening record.
- `a8e7d50c04254bb19f9de08b31ca2aa811fbe7fc` — frozen two-claim record and counter digests; LOG round-38 opening record.
- `3bc0b108708c46c800f9050a1caa25bfe3bf5e5a` — S144, sourced knowledge note and receipt, lesson, SCORECARD correction/capability candidate and LOG entries.
- `3624aae098024b17ced84588c29ca027f8dcbab0` — README index row for the new note.
- `a6616d5f45f5312053c6d56ed2a95e32344f4948` — validated 64-seat wave spec/dispatch/results and seat evidence.
- `7b23b08fbc017c7ad1b44e3638d231eabf332c9e` — preserved round-37 w1 seat results needed to re-derive the 34-seat figure.
- `0930a6b0c83df9a4e78927531180ea29a4ba0335` — round-37 commit/tally correction ledger, lesson M2 classification, census receipt.
- `d95558989b188dcb9a74cf9078eec63d68d40642` — round-38 census and numstat receipts.
- `2946fea53284adae34251c4418358b710469f5dc` — corrected SCORECARD disposition; C1 still fails at this tip.
- Final lane tip at filing: `2946fea53284adae34251c4418358b710469f5dc`; `jj-lane.sh state` and `git ls-remote origin refs/heads/master` both showed this exact hash, ahead=0.

## Before → after measurements

- **C1 calibration** — `node .ufo/waves/round-38/counters/c1-routed-defects.mjs --rev <REV> --repo <lane> --json`. At baseline `a8e7d50c04254bb19f9de08b31ca2aa811fbe7fc`, exit 1 / predicate false; recomputed round-37 reports 34 total, 23 ok / 11 finding. At final lane tip `2946fea53284adae34251c4418358b710469f5dc`, exit 1 / predicate false. D1 re-derives 34 seats; D2 re-derives 23/11; D5 receipt matches 144 rows, A128/B7/C9, mined120/queued15/rejected9. Remaining failures: D4 red-control receipt absent; D6 counter cannot find the nested numstat file because its `git ls-tree --name-only` is non-recursive. D3 correction/hash ledger is present by the final tip. **Verdict: not met.**
- **C2 coverage capability** — `node scripts/playwright-firefox-loopback-round38.mjs --out <receipt> --runs 2`. Before: no Playwright Firefox/Juggler operation or entry. Demonstration: two runs, first-shot SHA equal, reported egress 0 and survivors 0. W1 independently found the measurement does not bind a nonempty set of launched Firefox PIDs and 400-ms sampling can miss connections; its own binary/version claim is also not bound (Critic23). The counter/receipt gate required by the claim was not completed. **Verdict: unprovable / not admitted**; no capability row is accepted as verified for stagnation-window purposes.

Counting command for the C1 census population: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` (exit 0). The detailed output and parsed counts are in `.ufo/waves/round-38/measure/census-end.txt`.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.

- Before: exit 0, 143 rows; A127/B7/C9; mined119/queued15/rejected9; 20 pre-existing W04 duplicate-URL warnings (round-start transcript).
- After: exit 0, 144 rows; A128/B7/C9; mined120/queued15/rejected9; same 20 W04 warnings (`.ufo/waves/round-38/measure/census-end.txt`).
- Rows added: 1, tier A (S144). Rows touched: none. Frontier rows advanced: S144, opened this round and cited by the new knowledge note.
- Assimilation: none; full 38-row quarantine slice not hand-checked, so no adoption. No `considerthese/` directory.
- Mistake mined: round-37 self-assessment overclaim, plus the round-37 M3 surface-mismatch; M3's red control remains unlanded and is explicitly unresolved in `corpus/lessons/round-38.md`.

## Trend verdicts

- **expansion: unchanged** — S144 and a knowledge note were added, but the capability predicate is not admitted and no verified capability row enters the repertoire.
- **quality: unchanged** — C1 does not meet its frozen target; the failures are reported rather than hidden, and no evidence shows an admitted knowledge claim became false or stale.
- **discernment: unchanged** — no qualifying independent non-author admit/reject spot-check was completed; dispatched wave seats do not count as outside verification.

## SHONEN

- [~] Decision tables, error patterns, checklists and citations — `SKILL.md:697` and §Evidence ladder/Runbook; not independently re-verified this round.
- [~] End-to-end domain task — new Playwright Firefox loopback run in `corpus/evidence/round-38/playwright-firefox/receipt.json`; bounded to the fixture, with the evidence limitations above.
- [~] Executable without oral context — `scripts/playwright-firefox-loopback-round38.mjs`; run executed, but the instrumentation attack findings remain.
- [~] No cross-domain bleed — `PROVINCE.md:3-19`; this round stayed on browser/WebDriver operation and did not absorb sibling ground.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Round shape, tools, open questions, and misroot sweep

- One v2 wave: 64 seats; roles: 15 reviewer, 12 critic, 10 mutation-tester, 10 executor, 10 scribe, 4 scout, 3 connector; all 64 outputs nonempty; dead seats 0; no residual call. L1 held planner seat.
- Playwright 1.64.0 was already installed globally through npm; Firefox 157.0 (Playwright build v1555) installed through the official Playwright CLI browser channel because this round's capability probe required it. WebKit 27.2 downloaded via the same official CLI for feasibility probing but could not run: missing ICU74, libflite and libjxl libraries. No pacman transaction; pacman remains paused. No uv/npm package installation or system package update was performed in this round.
- L0 questions: none.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only `.scratch/closure-mado-r50.json`, `kotoba-shokukin/`, and this report; no tabi seat artifacts at fleet root. Other lanes' paths were untouched.
