# Round 43 — tabi

**Disposition: not admitted — honest stop (5th consecutive). Both frozen claims were refused by
their pre-declared kill rules after a fully settled 64-seat attack wave; every refusal is a
committed, re-derivable demonstration, and the round's instruments, repairs, sourced entry and
controls are landed and measured.**

## Work performed

Declared claims (frozen before any seat data at freeze `7ca6f018280b08dcc6a519e11ecc2c1ccbfc62bc`,
baseline `ab592825cd195599822ca227f7768914df208201`,
`.ufo/waves/round-43/claims.json`): **C1 coverage capability** — admission attempt of the round-43
signature-authenticated Playwright Firefox loopback TCP chain (per-invocation Ed25519 run key never
persisted, signed measure record, self-keyed witness, counter challenge-response; sourced via
**S150**, opened this round); **C2 calibration** — round-42 routed-defect checker hardened
(blob-type gate via **S151**, pinned measure blob id `8ff64d691f5c09569a50f2a5a038bb23774c3d35`,
V0-probe refusal, freeze-binds-controls rule). The stagnation nudge was active (no capability
entered rounds 39–42, window 3), so C1 was the required frontier/capability move; adjacency stays
lowest (8). Fresh-start reading done first: r39–r42 reports and the r40/r41/r42 non-author
verifier spot-checks.

- froze both predicates, kill rules, counting commands, the C1 residual model and all 8 controls
  (each bound by sha256 + verbatim quote line — r42 closure conformance defect 1 closed at the
  freeze layer) — commit `7ca6f018`.
- built and pinned the round-43 instruments: `scripts/measure-c1-round43.mjs`,
  `scripts/playwright-firefox-egress-round43.mjs` (r41 chain + `nonLoopbackRemotes` recording),
  `counters/c1-signature-bound-v5.mjs` (strict argv, wrapper-signature/witness-attestation/
  challenge verification), `counters/check-routed-defects-round43.mjs` (rules r1–r6),
  fixture generators `v0-fabrication.mjs` + `tree-vs-blob.mjs` — digests in claims.json
  (`frozenDigests`, re-derived 8/8 by `w1/ExecDigestPins`).
- all pre-data controls red/committed (`.ufo/waves/round-43/controls/`): baseline tree count 0;
  battery 7/7 (five r41 vectors + new `--import` vector); r42-receipt replay refused; synthetic
  pair refused; tampered record refused; C2 baseline red (`r5-claims-absent`, `r6-probe-absent`);
  V0 fabrication refused by v2 via the measure-blob pin **while the r42 checker bytes still green
  it** (`ExecC2V0Probe` reproduced: v2 exit 1 + pin finding, r42 exit 0); tree fixture named
  `r1a-not-a-blob` where r42 named no type violation.
- opened S150 (node:crypto docs, HTTP 200, 681,625 B, sha256 `4b7024df…c50c42af`, flat-byte quote
  `createPrivateKey, createPublicKey, generateKeyPair, sign, verify,`) and S151 (git-cat-file,
  79,360 B, sha256 `624464ef…5165048d7`, quote `Instead of the content, show the object type
  identified by`); registry 149 → 151 — commits `7ca6f018`, `db5b2940`.
- ran the live measurement: first attempt was refused by the round's own counter (46 real
  `*-egress` findings — one non-loopback owned socket, run-1 samples 111–133, gone by run 2;
  bytes archived at `.ufo/waves/round-43/measure/failed-run-1/`); the driver/counter were
  hardened BEFORE the freeze to record remotes (disclosed in LOG/SCORECARD; no predicate
  loosened); second run clean: exit 0, v5 predicate true, spans 18,588/25,649 ms, egress 0,
  nonce `d2c85f6e…`, measure record sha256 `c67a1096…97b258` — receipts committed as explicit
  files at `ba433c94` (the directory commit had silently skipped both >1 MiB receipts — the r41
  D1 class, caught by `git ls-tree` at the freeze before any citation).
- validated and dispatched one policy-v2 wave (64 seats; dispatch JSON carried `taskCall`,
  verified by `w1/ExecWaveAudit` — the r41 defect class excluded); WAVE-DONE received; **64/64
  seats settled, 0 dead, 0 empty outputs; verdicts bound on seat-written files: 34 ok / 30
  finding** (`.ufo/waves/round-43/w1-results.json`, `w1-parse-summary.json`) — commits `b77e84a0`,
  `db5b2940`.
- **C1 refused by its kill rule**: four seats demonstrated in-model do-nothing reaches with zero
  browser runs — `w1/CritC1ReachSynth` (self-signed pair answers the counter's fresh challenge
  from the pair's own key, three variants incl. a second-process relay), `w1/CritC1ReachDirect`,
  `w1/CritC1Witness`, `w1/CritC1ReachReplay`; `w1/CritResidualModel` added the copied-counter
  reach. The challenge wall authenticates key-possession against the record's self-selected
  pubkey, not chain provenance. No capability row.
- **C2 refused as worded**: the r42 holes are closed and mutation-proven load-bearing
  (`MutC2Pin`/`MutC2Blob`/`MutC2Bind` ok; `CritC2Blob` adds commit/tag object refusals;
  `ExecC2FreezeRev` re-derived all six branches at the freeze, exit 0, with the baseline red
  control reproducing exactly) — but `w1/CritFreezeBindings` demonstrated two r5 false-greens
  (a freeze binding only 5 of its 8 named controls greens via the `binds.length < 5` floor; a
  19-char quote fragment greens via `includes`), `w1/CritFreezeAudit` found
  beforeState-to-bindings completeness unenforced, and `w1/CritPredC2` routed the r4/r5/r6
  sentence-code gaps. Exit 0 at the measured revision is an instrument pass, not admission.
- landed the round's sourced knowledge entry
  `corpus/knowledge/receipt-authenticity-signing-round-43.md` (S150+S151 cited; forgery→refusal
  decision table over the committed controls; declared residual model; limitations) + README
  coverage row; lesson `corpus/lessons/round-43.md` (Gate with both admits + located quotes;
  four Mistakes rows); QUALITY criteria 106–107 from the observed failures — commit `db5b2940`.
- final-tip gates: C2 counting command exit 0 / 0 findings at `db5b2940` in a clean clone
  (`controls/c2-final-r43.json`); census end exit 0 (`measure/census-end.*`); `check-sources`
  clean 151 rows; `check-selfassessment` paired runs at final tip and baseline are identical
  (verdict=failed, mismatches=1, could_not_evaluate=117 at BOTH — the single mismatch is
  pre-existing, no new red); freshness self-test clean 12; misroot sweep clean (`w1/ExecScratchGuard`: no tabi-owned misroot).

## Landed changes

Every change is tied to a LOG.md entry (pre-dispatch + integration) and landed through
`jj-lane.sh --as tabi`:

- `7ca6f018280b08dcc6a519e11ecc2c1ccbfc62bc` — freeze: claims.json (sentences byte-identical at
  three sites, control bindings), instruments, controls, S150/S151, census-start receipts, LOG
  pre-dispatch entry, SCORECARD declared-claims section.
- `ba433c94b14a0e0d5ecf2eba1be0a8ee3064491c` — C1 receipt+witness committed as explicit files
  (the >1 MiB directory-commit skip caught at the freeze).
- `b77e84a055dc8434838bdc305f1e83dd743b5715` — w1 spec (64 seats), validated dispatch
  (`taskCall`), ready handoff.
- `db5b2940782ee67571edb6cad9fe017647773299` — w1 results + parse summary + seat reports; sourced
  entry + README row; lesson; QUALITY 106–107; SCORECARD executed disposition; LOG integration
  entry; registry used-by updates; failed-run-1 evidence.
- `991b2842ac6c748f2abba019c636e91265f9fadc` — final-tip gate receipts (c2-final, census-end,
  selfassessment paired runs), dispatch marker, seat evidence files.
- `3bf87b608a10dfb1ce78bfad5c272c5a7658450d` — remaining >1 MiB seat evidence as explicit files.
  **Lane HEAD = origin/master = `3bf87b608a10dfb1ce78bfad5c272c5a7658450d`, ahead 0.**

## Before → after measurements

- **C1 / coverage capability** — counting command
  `node scripts/measure-c1-round43.mjs --out corpus/evidence/round43/playwright-egress/receipt.json --measure-out .ufo/waves/round-43/measure/c1-measure-r43.json --scratch /fast/scratch/hyaku/tabi-r43/L1-measure/run2`.
  Before at baseline `ab592825`:
  `git ls-tree -r --name-only ab592825cd195599822ca227f7768914df208201 -- corpus/evidence/round43 | wc -l` → 0
  (`controls/c1-baseline-tree-count.txt`). After at the live run (2026-10-29) committed at
  `ba433c94`: exit 0, v5 predicate true, spans 18,588/25,649 ms, egress 0. **Verdict: not
  admitted — the kill rule fired** (`CritC1ReachSynth`/`CritC1ReachDirect`/`CritC1Witness`/
  `CritC1ReachReplay` reach counter exit 0 / predicate true with zero browser runs using
  self-authored pairs that answer the fresh challenge). Coverage held 9 → 9; no capability row.
- **C2 / calibration** — counting command
  `node .ufo/waves/round-43/counters/check-routed-defects-round43.mjs --rev <REV> --repo /home/vgpnk/Projects/shokunin/tabi-shokunin --json`.
  Before at baseline: exit 1, findings `r5-claims-absent`, `r6-probe-absent`
  (`controls/c2-baseline-red-r43.json`; reproduced by `ExecC2FreezeRev` and re-derived at
  `db5b2940`). After at `db5b2940`: exit 0, findingCount 0 (`controls/c2-final-r43.json`).
  **Verdict: not met as worded — the kill rule fired** on the demonstrated r5 false-greens
  (forged-control-binding + quote-line limbs); exit 0 is an instrument pass, not admission.
  Calibration held 9 → 9.

## Sources & frontier

Required census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:

- Before (2026-10-29, pre-edit): **exit 0**, `tabi ok`, 21 W04 warnings —
  `.ufo/waves/round-43/measure/census-start.{out,err,exit}`.
- After (post-registry edits): **exit 0**, `tabi ok` — `.ufo/waves/round-43/measure/census-end.{out,err,exit}`.

Row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 149 → **151**
(tiers A133→A135; status mined 124→126, queued 15, rejected 10; `check-sources` clean, 0
findings; `ScoutRegister` verified no id collision).

- Rows added by tier: **S150** (tier A, mined — node:crypto docs; quote `createPrivateKey,
  createPublicKey, generateKeyPair, sign, verify,`, 7 words, API index line; opened 2026-10-29;
  staged copy `.ufo/waves/round-43/sources/crypto.html`, sha256 `4b7024df…c50c42af`; re-opened
  byte-identical by `RevS150`) and **S151** (tier A, mined — git-cat-file `-t` option; quote
  `Instead of the content, show the object type identified by`, 11 words; staged copy
  `git-cat-file.html`, sha256 `624464ef…48d7`; re-opened byte-identical by `RevS151`).
- Rows touched old→new: S150/S151 `used-by` gained
  `corpus/knowledge/receipt-authenticity-signing-round-43.md, corpus/lessons/round-43.md`. No
  other row changed.
- Frontier rows advanced: the receipt-authenticity instrument class moves from named (r42 routed
  fix) to held-with-declared-limits (the sourced entry); the loopback-TCP capability stays
  frontier (C1 refused — the r44 route now carries four falsifier classes of evidence).
- **Assimilation: none** — the r42 fresh re-adjudication (misbound 25 / absent 6 of 38) keeps
  package adoption closed; no `merge/tabi/` row or knowledge entry was appended from the package.
  `considerthese/` absent (no such directory in this lane).
- Errors 0; the 21 W04 duplicate-URL warnings are pre-existing.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | New admitted note `corpus/knowledge/receipt-authenticity-signing-round-43.md` on ground the coverage map did not hold, citing newly opened mined S150/S151; knowledge notes 59 → 60 (`ls corpus/knowledge/*.md \| wc -l`); registry 149 → 151; README coverage row. |
| quality | improved | The r42 routed defects closed in committed bytes with red→green proofs (V0 fabrication refused via the pinned blob id — the r42 checker bytes still green it; tree objects named `r1a-not-a-blob`; freeze binds every control by sha256+quote), each closure mutation-proven load-bearing; the wave then routed the NEXT defect classes with false-green demonstrations (QUALITY 106–107); no admitted entry failed a re-check. |
| discernment | unchanged | The 64-seat wave is lane-internal (dispatched seats remain the lane); the outside non-author admit/reject spot-check is the closure's duty, pending at filing. Both claim refusals under pre-declared kill rules are recorded, not smoothed. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round (frozen bytes; simplifier items route to r44); no new non-author verifier (closure pending).
- [~] At least one end-to-end domain task executed and logged in LOG.md — two real signature-authenticated Playwright Firefox loopback runs with committed signed receipts (`corpus/evidence/round43/playwright-egress/receipt.json`, measure record `.ufo/waves/round-43/measure/c1-measure-r43.json`, LOG round-43 integration entry); claim admission refused on the demonstrated counter reach.
- [~] Instructions executable by an agent without oral context — the frozen controls and fixtures were rebuilt byte-faithfully by seats from committed generators alone (`ExecC2V0Probe`, `ExecC2TreeFixture`, `ExecFixtureRepro`, `ExecC1Battery`); no fresh independent cold-read promotion verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; sibling findings routed, not absorbed (`w1/ScoutSibling`, `w1/ConnSiblingProc`, `w1/ConnAdjacency` 0 frozen-pin deltas).

## Stale-lane, wave shape, tooling, open questions, misroot, cleanup

- Stale-lane: respawn-per-round driver; this round is tabi round 43 (run-12 block, target 51);
  no other mission of this lane is open.
- Wave shape: ONE policy-v2 wave `w1`, 64 seats (band 64–128 respected), one dispatch through
  the ready handoff, WAVE-DONE received, no residual call, round total 64. Role mix: critic 16,
  executor 16, mutation-tester 8, reviewer 6, scout 5, scribe 5, connector 4, sentinel 2,
  simplifier 1, revenger 1; attack share 30/64 = 46.9% ≥ 25%. Dead seats: 0. Evidence:
  `.ufo/waves/round-43/w1-results.json`, `w1-parse-summary.json`, `w1/<Seat>/`. The L1 held the
  canonical planner seat; the planning/overlap work rode the four connector items.
- Tool installs/updates: none. Playwright 1.64.0 / Firefox (pinned sha256) already present; the
  pacman pause was honored (no pacman invocation by the L1 or any seat).
- Open L0 questions (pre-existing, none assumed answered): `tabi | round-39` band-template
  reconciliation; `tabi | round-39` shokuknow seat-artifact disposition; `tabi | round-40` F4
  guidance (superseded by the r41–r43 chain); `tabi | round-42` frozen-instrument vs
  routed-defect ruling (`check-c2-knowledge-round41.mjs` stays red, pre-existing, unchanged).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned paths (`.scratch/goal-20261029-hyaku-run12.md`, `.ufo/l0-questions.md`);
  untouched. `w1/ExecScratchGuard` concurs: no tabi-owned misroot.
- Cleanup: `/fast/scratch/hyaku/tabi-r43/*` L1 scratch roots removed after evidence landed in
  the lane; remaining per-seat roots removed at round end. Deliberately untracked in the lane:
  `w1/CritC2Blob/{annotated-tag-entry-fixture-repo,commit-gitlink-fixture-repo}/` — nested git
  fixture repos (committing them would create gitlinks); their receipts are committed and they
  are rebuildable from `w1/CritC2Blob/report.md`.
