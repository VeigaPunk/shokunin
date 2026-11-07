# kagi — round 52 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. BASE `1d984adaa4a5c66ea9f24cb95bf79ffbca16c32b` (round-51 spot-check tip). Predeclaration `52ebb412561d9601ad8658c30d1cfa0087af64d4` → candidate `a2cb69b7b54f3af611f89ed71adc03dab0675f94` → receipts/lane tip `282849f7ef236549f06e551dc294f7cfee4fc01d` (`git ls-remote origin refs/heads/master` ⇒ `282849f7ef236549f06e551dc294f7cfee4fc01d`). One attempt (`.ufo/watchdog.log`: `launch kagi round=52 … attempt=1`, no earlier attempt and nothing inherited).

## Work performed

Declared claims (frozen in `plans/round-52.md` at `52ebb412`):

- **C1 — operability (capability acquisition):** the lane executes five OpenBao KV v2 version-lifecycle mechanics documented by S110, 0 → 5.
- **C2 — calibration:** the lane's committed statements about OpenBao rewrap agree with the pinned binary (round-51 closure D1), 2 → 0.

Work items:

- Protocol load: `skill://godspeed`, the round prompt, round-51 spot-check `corpus/lessons/round-51-verifier-spotcheck.md` (defects D1–D3 routed into this round), SCORECARD §Saturation (all axes at 9; capabilities entered in rounds 49 and 51, so the nudge does not fire).
- Source opened: S110 `https://openbao.org/docs/secrets/kv/kv-v2/` (HTTP 200, 83532 B, sha256 `6cfd72ec…7e02b1587`), capture `.ufo/waves/round-52/capture/S110.body`; re-fetched with the declared profile byte-identical; four quotes located `count=1` (`corpus/lessons/round-52.md` §Gate).
- Pre-freeze controls: `plans/round-52-controls.sh`, 20 controls, run 2 `CONTROLS: match=20 mismatch=0` (`.ufo/waves/round-52/controls/controls-prefreeze.txt`); run 1 kept (`controls-prefreeze-run1.txt`, 16/19: the C2 counter took a backticked `<!--` for a comment opener, fixed before the freeze, M52-3). Committed in predeclaration `52ebb412` before any candidate scoring.
- C1 trial `corpus/openbao-kv-versions-trial.sh` (candidate = reference fixture outside comment lines; `.ufo/waves/round-52/final/kill-rules.txt`), entry `corpus/knowledge/openbao-kv-v2-version-lifecycle.md`, registry row S110 + fetch row, coverage-map row, capability row `SCORECARD.md:716`. The trial closes round-51 routed S-1/S-2/S-3/M51-3 (no secret on argv, no server log, port held by our pid, refusal = non-zero exit AND server text).
- C1 execution evidence (answers R52CriticC1): `.ufo/waves/round-52/final/c1-execution-evidence.txt` — 31 `bao` calls, every mechanic's subcommand present, 0 token-shaped argv elements.
- C2 corrections: one `Correction (round 52, D1)` line appended to `corpus/knowledge/vault-openbao-token-lease-lifecycle.md` and to `corpus/lessons/round-51.md`; SCORECARD erratum E52-1 for the round-51 depth row (same over-read in words the C2 pattern cannot see; declared in the plan before the freeze).
- Gate defect found while landing (M52-2): the declared-axis gate `corpus/claims-declared.sh` read the frozen plan's backticked `<!--` as a comment and reported both round-52 claims MISMATCH; fixed (code-span masking, selftest case 13), red witness `.ufo/waves/round-52/final/gate-m52-2.txt` (BASE gate + case 13 ⇒ `FAIL (passed=12/13)`, amended ⇒ `PASS (13 cases)`).
- Ledger population migrations with journal `.ufo/waves/round-52/expectation-migrations.json` (R13-01, R24-06, R21-02, R31-02, R33-02, R34-03, R14-01, R12-03, R22-03, R24-05, R24-15; `EXPECT_JOURNAL: CLEAN (changed=11 journaled=11)`); four of them (stamp population) were found only by the full verify of the candidate (M52-5).
- Wave `kagi-r52-build` (12 seats) — findings integrated into the entry's Bounds, lesson §Mistakes M52-4 and §Routed; reports `.ufo/waves/round-52/build/`.
- QUALITY criteria QM66 (doc-vs-binary sentences need a probe on the same input) and QM67 (comment-skipping readers mask code spans), `corpus/QUALITY.md` tail.

Round shape: ONE v1 wave of **12 seats** (policy `ufo-wave-policy.json`, band 8–16; validator `counts: spawn=12 total=12`), no residual call, **round total 12**. Role mix: scout 1, connector 1, executor 3, scribe 1, reviewer 2, critic 2, mutation-tester 1, sentinel 1; attack seats (reviewer/critic/mutation-tester) 5/12 = 42 %. The §3 planner seat is held by the L1 (the validator rejects `planner`). Dead seats: **0** (all 12 settled with output, `build-results.json`; seven ended with `SEAT-STATUS: complete` or `"status":"complete"`, the other five yielded JSON summaries with their reports written). Seats dispatched by the orchestrator from `build.ready`; WAVE-DONE received before this report.

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `52ebb412561d9601ad8658c30d1cfa0087af64d4` | predeclaration: plan, counters c1/c2, controls (20 MATCH, run 1 kept), S110 capture, census start, BASE readings | `LOG.md` `## Round 52` bullet 1 |
| `a2cb69b7b54f3af611f89ed71adc03dab0675f94` | candidate: trial, entry, S110 + fetch row, README row, two D1 corrections, gate fix + case 13, manifest rows `52 C1/C2`, SCORECARD capability row/readings/post-move/E52-1, QM66/QM67, lesson, seven ledger migrations + journal, restamp, wave evidence | `LOG.md` `## Round 52` bullets 4–6 |
| `282849f7ef236549f06e551dc294f7cfee4fc01d` | receipts: revision readings, kill rules, harm counters, full verify of candidate and tip, citations, census end, four stamp-population migrations (M52-5), final wave reports | `LOG.md` `## Round 52` bullet 6 (M52-5 sentence) |

## Before → after measurements

| Claim | Counting command | Before (BASE `1d984ada`) | After (candidate `a2cb69b7`) | Target | Receipts |
|---|---|---|---|---|---|
| C1 | `bash plans/round-52-c1.sh <rev>` | `C1_OPENBAO_KV: value=0 absent=1 pins=1` | `value=5 discriminating=5 pins=1 setup_ok=1 nosecret=1 noargv=1(real=31,real2=31) src=1(S110)`, every T `real=HOLDS/HOLDS` and `shimvec` = EXPECT_VEC | 5 | `.ufo/waves/round-52/final/c1-base.txt`, `c1-candidate-rev.txt` |
| C2 | `bash plans/round-52-c2.sh <rev>` | `value=2 assertions=2 … uncorrected=[corpus/knowledge/vault-openbao-token-lease-lifecycle.md:292 corpus/lessons/round-51.md:22]` | `value=0 assertions=2 guard=1 probe=1 obs_helper=sys/wrapping/wrap obs_kv=secret/data/<path> uncorrected=[]` | 0 | `final/c2-base.txt`, `c2-candidate-rev.txt`; tip tree `final/tip-counters.txt` |

Admission notes (for the closure; verdicts are the operator's):

- C1 kill rules hold at `a2cb69b7` (`final/kill-rules.txt`: instruments unchanged since `52ebb412`; trial = reference outside `#` lines; 0 committed `r52-` nonces; bao pin unchanged). **Disclosed weakness (M52-4):** R52CriticC1 showed the frozen counter checks printed verdicts, not execution — F2 (shim fingerprinting by junk calls), F5b (run-dir creation order) and F6 (T1 real, T2–T5 printed) each score 5, and control K1-F8 is vacuous. C1's admission therefore rests on the frozen counter **and** the kill rule **and** the execution receipt `final/c1-execution-evidence.txt`, as round 51's did; the hardening is routed, not claimed.
- C2 known ceilings (declared or found): the pattern is lexical (SCORECARD round-51 depth row handled by E52-1, uncounted); R52ReviewerC2 F1 (same-basename pointer), R52CriticC2 A17/A24/A26 (symlinks into excluded names) — the candidate has 0 symlinks (`git ls-tree -r a2cb69b7 | awk '$1=="120000"' | wc -l` ⇒ 0) and both corrections sit in the files they correct; R52CriticC2 A2/A13 (prose denial) is the declared prose ceiling.
- Harm check: full `claim-ledger.sh verify` FAIL/POLICY ids are the BASE set at the tip tree — BASE (`build/R52ExecHarm-verify-base.txt`): FAIL R11-08, R25-02, R36-01; POLICY R29-01, R29-02, R38-03; tip (`final/verify-tip.txt`): the same six ids. The candidate verify (`final/verify-candidate.txt`) additionally read FAIL R12-03/R22-03/R24-05/R24-15 (stamp population 124 → 125), migrated in `282849f7` (M52-5). Citations: BASE unresolved 4 (non-owned spot-check cites); candidate 5 = the same 4 + `round-52.md:56` → `census-end.txt`, which lands in `282849f7` (`final/citations-candidate.txt`). Round-48 counter `value=0` at the candidate with K07 `CLEAN (claims=31)` and K10 `PASS (13 cases)` (`final/harm-counters.txt`). The round-51 C2 counter reads `SETUP reason=g1-gate-changed` by design (it pins the BASE gate sha256); its two populations read directly are 0 (gate CLEAN, round-48 V=0).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.
  - Round start: `kagi ok …/kagi-shokunin/corpus/SOURCES.md`, rc 0 (`.ufo/waves/round-52/controls/census-start.txt`).
  - Round end: `kagi ok …/kagi-shokunin/corpus/SOURCES.md`, rc 0, 19 W04 warnings as at start (`.ufo/waves/round-52/final/census-end.txt`; re-run after the last lane commit: `kagi ok`, rc 0).
- Registry rows: `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md` ⇒ 109 → 110. Added by tier: A 1 (S110), B 0, C 0. Rows touched old→new: none. Lane census `bash corpus/sources-census.sh` ⇒ `CLEAN (rows=110 A=106 … entries_sourced=16 … captures=110 …)`.
- Rejected this round (with flip conditions in the lesson Gate): the KV v2 API page, the `kv undelete`/`kv destroy`/`kv metadata` command pages; the rewrap API page is not re-registered (its single `creation_path` occurrence is the C2 evidence).
- Frontier advanced: KV v2 version operations move from one documented Vault parameter (S024) to an executed OpenBao trial; the round-51 rewrap note is corrected against the binary.
- Sourced claim: C1 rests on S110, opened 2026-11-07 (entry `source:` line, trial header line 3).
- Mined mistakes: `corpus/lessons/round-52.md` §Mistakes M52-1 (doc-over-read, the D1 class; fix shown able to fail by `c2-base.txt` value 2 and K2-F1/F2/F3), M52-2 (codespan-comment in the declared-axis gate; red witness `gate-m52-2.txt`), M52-3, M52-4 (printed-protocol, routed, not counted), M52-5 (population coupling; the full verify read FAIL).
- Assimilation: none — `grep -rilE 'openbao|undelete|max_versions|rewrap' /home/vgpnk/Projects/shokuknow/merge/kagi | wc -l` ⇒ 0 (lesson §Assimilation; R52ConnectorSiblings agrees).
- considerthese: newest `considerthese/2026-10-26.md`, no proposal taken (none fits; lesson §considerthese).

## Trend verdicts

- **expansion: improved.** New executed ground: `git grep -il undelete 1d984ada -- corpus` empty → trial + entry + S110 at `a2cb69b7`; capability row "OpenBao KV v2 version-lifecycle trial" (first-working round 52); C1 0 → 5.
- **quality: improved.** The declared-axis gate no longer drops headings after a backticked `<!--` (shown able to fail, `gate-m52-2.txt`); the new trial carries the round-51 secret-handling fixes (R52SentinelSecrets: argv, logs, stdout clean; N1–N6 none); ledger FAIL/POLICY ids unchanged BASE → tip. Disclosed against it: the C1 counter's printed-protocol hole (M52-4) and four trial defects (R52ReviewerTrial D1–D4), all routed.
- **discernment: improved.** The round-51 over-read is withdrawn by truth-bound corrections (C2 2 → 0) and a criterion (QM66); source decisions carry reasons and flips (admit S110; reject four adjacent pages); the lesson records the counter weaknesses the wave found rather than claiming them fixed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SKILL.md` §Vault-ops decision table / §Failure table (unchanged this round); no non-author verifier named this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence `LOG.md` `## Round 52` (the KV v2 trial run end to end, `final/c1-execution-evidence.txt`); seat R52ExecTrial ran the committed trial three times and the counter twice without lane context (`build/R52ExecTrial.md`), a seat of this lane, so not a non-author verifier.
- [~] Instructions executable by an agent without oral context — evidence `corpus/knowledge/openbao-kv-v2-version-lifecycle.md` §Measured (one command), `build/R52ExecTrial.md` value=5 reproduced from committed bytes.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `build/R52ConnectorSiblings.md` (no sibling lane owns KV v2 or rewrap ground); `PROVINCE.md` unchanged.

## Other

- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked `trail-ids.txt` (1 byte `,`, mtime 2026-11-06 20:36, before this round's launch at 22:30, no kagi/r52 content — not this lane's) and `.scratch/…` (orchestrator-owned); no misroot from this round's seats, nothing moved.
- Inherited state: none (clean tree at BASE, `jj-lane.sh state` `tracked=0 untracked=0`).
- Scratch: several seats left their dirs under `/fast/scratch/hyaku/kagi-r52/` (a §7 defect of theirs, named here); the L1 removes `kagi-r52` after filing.
- Tool installs: none (L1 and, per their reports, all seats).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none added this round.
