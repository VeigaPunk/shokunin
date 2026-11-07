# souji — round 78 report (L1 SoujiR78, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Base `a8558d410e9855a9d990d6542a24a9a3a365ab6c` (r77 admitted). Preregistration `census/round-78/preregistration.txt` (frozen at F `007404ea363461a76ff23afcf6173b3281532dd3`).

## Work performed

Declared claims (two, causally separable; S78Connector: SEPARABLE):

- **C1 — operability (sourced on S323 and S324, both opened this round):** the pre-report gate refuses non-regular git discovery sources (HEAD, commondir, packed-refs, the system/global/XDG/repository/worktree config files and every file their includes name) before its first git call, and bounds check 1 with a 45 s timeout. Frozen 17-row counter: mismatches 12 → 0, hangs 12 → 0.
- **C2 — calibration (the lowest owned axis, 7):** the 22 evidence pointers LOG.md makes that the lane's pointer check reports MISSING at the base resolve to verified classes under a location-bound successor counter. Resolved 0 → 22 against a 19-of-22 no-capture mechanical ceiling; 12 LOG forgeries and 7 r77 forgeries refused; pointer check missing 22 → 19.

Work items:

- Protocol load and inherited debts: r77 spot-check routed defects 1–5 read first (`corpus/lessons/round-77-verifier-spotcheck.md`). Defect 1 → S321 anchor and scope cells swept (`corpus/SOURCES.md:280`) and an append-only `## Correction` closes `corpus/lessons/round-77.md`. Defect 2 → C2's instrument. Defect 3 → C1. Defect 4 → `census/round-78/probes/domain-trial.sh` (EPOCHREALTIME wall time, W-blob amendment line). Defect 5 → carried (lesson `## Routed to round 79` (d)).
- Pre-freeze feasibility in scratch (Q70): base gate 12 HANG rows, a draft candidate 17/17; one draft defect found and fixed before W (lesson M2).
- P `a0dcfa8d7da794e821b22a421584ac2a03c611c0`: C1 counter + population (`census/round-78/c1-gitsrc-counter.py`, `c1-population.tsv`); C2 successor counter with pinned populations, location-bound MOVED/QUARANTINED, source-bound TOKEN and `--forge` (`census/round-78/c2-pointer-counter.py`), LOG.md population, forgery sets `c2-forge-r77.tsv` (7) and `c2-forge-r78.tsv` (12), legacy-forge harness, mechanical-ledger generator, G6 collision probe; every control receipt at the base; prefreeze forgery battery (`records/c2-prefreeze-r77-forge.txt` 7/7 refused, 35/35; `records/c2-prefreeze-r78-forge.txt` 12/12); S323/S324 captures; census-before.
- F `007404ea…`: preregistration; freeze-check `--substance --chronology` `SUMMARY claims=2 findings=0` (`census/round-78/records/freeze-check-at-F.txt`).
- W `ed22dc9cb7a6b61a7d0bd150db4a95191b1333aa`: C1 candidate gate (blob sha256 `b746bd9d…4eef`).
- K `d90740fec1862556ed504aafcd21e89d5dece0f0`: 240 host-local wave files LOG.md cites captured at their own paths (L10, L14, L20); byte-exact (S78ExecC2: disk-only 0, committed-only 0).
- L `a0f3b91fe59129802c48f7e4db750960ddeaa408` (defective: duplicate L19 row, L21 lost; receipt `census/round-78/records/attempts/c2-at-L-duplicate-row.txt` resolved=21) → L2 `87d456179668738ca59e607c3176de056e6a9991` repaired (lesson M1).
- A `319109b0ddc836c6cf3364fdde3ab99796f21f32`: after-arms (C1, its four regressions, C2, the r77-population regression, pointer check).
- I `bbd199da07dc6ce40ac428cdfd2321a6630442f4`: S323/S324 rows, Q140/Q141, `corpus/knowledge/git-discovery-sources.md`, README frontier r78, SKILL gate rows r78, SCORECARD r78 rows and capability rows, LOG.md `## Round 78` with the append-only per-item pointer corrections, lesson draft.
- Wave w1 (12 seats, 0 dead). Repair R `3221566c4e71b077bf322c0457ffdb218209674f` (gate scan: NUL-delimited records, `--type=path`, canonical seen-set and 64-file bound, `RECEIPT-GITSOURCE-SCAN`, timed gitfile/commondir reads, loose-ref check). Receipts R2 `6a49837d9e5a980bdf3507656b0b349bbc68e0a8`: frozen C1 17/17 at R, r77 16/16, r76 30/30, r36 21/21, r27 4/4, `repair-probes.txt` 10/10 (run 1 kept, 8/9).
- I2 `723295a4706da97d35ae0bfebb580c4b4dd380bb`: wave mirror (`census/round-78/records/wave-w1/`), lesson Gate corrections, `## Wave`, `## Mistakes (wave)`, `## Routed to round 79`. Census-after `e691025957c7befb66a69b2fae237e71f9c2a9ce`.
- Domain trial (C1 conjunct): the R gate over the lane itself at the report tip through the committed trial script (see the end of this report).

## Landed changes

Every change below is tied to LOG.md `## Round 78` (`LOG.md:3027-3036`) and to the commit that carries it.

| change | commit |
|---|---|
| instruments, populations, forgery sets, controls, captures, census-before | `a0dcfa8d7da794e821b22a421584ac2a03c611c0` |
| preregistration | `007404ea363461a76ff23afcf6173b3281532dd3` |
| C1 candidate gate | `ed22dc9cb7a6b61a7d0bd150db4a95191b1333aa` |
| C2 captures (240 files) | `d90740fec1862556ed504aafcd21e89d5dece0f0` |
| C2 ledger (defective) and repair | `a0f3b91fe59129802c48f7e4db750960ddeaa408`, `87d456179668738ca59e607c3176de056e6a9991` |
| after-arms | `319109b0ddc836c6cf3364fdde3ab99796f21f32` |
| corpus, SKILL, SCORECARD, LOG, QUALITY, README, lesson draft | `bbd199da07dc6ce40ac428cdfd2321a6630442f4` |
| wave repair of the gate | `3221566c4e71b077bf322c0457ffdb218209674f` |
| repair receipts, S321 scope sweep, SOURCES provenance, knowledge corrections | `6a49837d9e5a980bdf3507656b0b349bbc68e0a8` |
| wave mirror, lesson Wave/Mistakes/Routed | `723295a4706da97d35ae0bfebb580c4b4dd380bb` |
| census-after | `e691025957c7befb66a69b2fae237e71f9c2a9ce` |
| domain-trial receipt | final lane hash below |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-78/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=17 mismatches=12 errors=0 hangs=12`, EXIT=1; K-b 14, K-c 10, K-d 11, all EXIT=1 | `census/round-78/records/c1-after.txt`: `SUMMARY rows=17 mismatches=0 errors=0 hangs=0`, EXIT=0; r77 16/16, r76 30/30, r36 21/21, r27 4/4; identical at the repair | `python3 -B census/round-78/c1-gitsrc-counter.py --gate-dir DIR --work WORK` | `ed22dc9cb7a6b61a7d0bd150db4a95191b1333aa` (gate blob `b746bd9d…4eef`); repair `3221566c` |
| C2 | `census/round-78/controls/c2-K-a-no-ledger.txt`: `SUMMARY items=22 resolved=0 unresolved=22`, EXIT=1; mechanical 19, r77 counter accepts 7, shifted population EXIT=2 | `census/round-78/records/c2-after.txt`: `SUMMARY items=22 resolved=22 unresolved=0 refused=0 mismatched=0 errors=0`, `FORGE-SUMMARY forged=12 matched=12 accepted=0`, EXIT=0; pointer check missing 22 → 19 | `python3 -B census/round-78/c2-pointer-counter.py --root LANE --rev REV --fleet-root FLEET --population census/round-78/c2-population.tsv --ledger census/round-78/c2-pointer-ledger.tsv --forge census/round-78/c2-forge-r78.tsv` | `87d456179668738ca59e607c3176de056e6a9991` (after-arm commit `319109b0`) |

**C1** — counting command `python3 -B census/round-78/c1-gitsrc-counter.py --gate-dir DIR --work WORK` (DIR = gate + writer from the measured revision); measured against W `ed22dc9cb7a6b61a7d0bd150db4a95191b1333aa` (gate blob `b746bd9d…4eef`).

- Before (`census/round-78/controls/c1-K-a-do-nothing.txt`, base gate `5d08f547…df55a`): `SUMMARY rows=17 mismatches=12 errors=0 hangs=12`, EXIT=1.
- After (`census/round-78/records/c1-after.txt`): `SUMMARY rows=17 mismatches=0 errors=0 hangs=0`, EXIT=0.
- Controls red: K-b refuse-any-include 14, K-c config-only 10, K-d timeout-only 11 (all EXIT=1).
- Regressions: r77 16/16, r76 30/30, r36 21/21, r27 4/4 (`census/round-78/records/c1-regress-*.txt`); identical at the repair R (`census/round-78/records/wave-repair/`).
- Qualifications (S78CriticClaims, S78MutGate): bounding every git call with no pre-check also reaches hangs=0 (mismatches 11 on the class token only), so what separates the candidate is the refusal ordering and class; K-d's hangs come from check 4's 300 s bound; the counter has no duration predicate (mutant m13 survives; pinned by probe arm a6); its killpg misses `timeout`'s own group.

**C2** — counting command `python3 -B census/round-78/c2-pointer-counter.py --root LANE --rev REV --fleet-root FLEET --population census/round-78/c2-population.tsv --ledger census/round-78/c2-pointer-ledger.tsv --forge census/round-78/c2-forge-r78.tsv`; measured against L2 `87d456179668738ca59e607c3176de056e6a9991` (receipt committed in A `319109b0`).

- Before (`census/round-78/controls/c2-K-a-no-ledger.txt`, base): `SUMMARY items=22 resolved=0 unresolved=22 …`, EXIT=1.
- After (`census/round-78/records/c2-after.txt`): `SUMMARY items=22 resolved=22 unresolved=0 refused=0 mismatched=0 errors=0`, `FORGE-SUMMARY forged=12 matched=12 accepted=0`, EXIT=0.
- Controls: K-b mechanical ledger 19 of 22 (L10 L14 L20 refused), K-c frozen r77 counter accepts 7 of 7 forgeries, K-d shifted population EXIT=2, K-e G6 copy refused by r78 only.
- Regression: r77 population 35/35, forgeries 7/7 refused (`census/round-78/records/c2-regress-r77.txt`). Pointer check over LOG.md missing 22 → 19 (`records/c2-pointer-check-before.txt`, `records/c2-pointer-check-after.txt`).
- Qualifications (S78CriticClaims, S78MutCounter): the claimed delta over the mechanical control is the three captures (at the after revision the generator reaches 22 because the captures exist); 9 of 22 items are byte-verified; four counter mutants survive every frozen artifact and five false single rows pass (routed r79). The append-only LOG.md correction named as claimed work landed at I, after the after-arm; no counted number depends on it.

No owned axis score changed (calibration 7, coverage 8, operability 8).

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Before: `census/round-78/records/census-before.txt`, `souji ok`, EXIT=0.
  - After: `census/round-78/records/census-after.txt`, `souji ok`, EXIT=0.
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 245 → 247.
  - Added: tier A ×2. S323 git config.adoc "Includes" at v2.56.0 (docs, `mined`) and S324 git setup.c get_common_dir_noenv at v2.56.0 (code, `mined`), both cited by `corpus/knowledge/git-discovery-sources.md` and QUALITY Q140; C1 rests on them (sourced claim).
  - Rejected (lesson Gate): gitrepository-layout(5) as the open-behaviour source (S124 already holds the semantics); `Documentation/config/include.adoc` (HTTP 404).
  - Rows touched old→new: S321 anchor cell "(the fstat type read follows at line 1169)" → "(the fstat at line 1169 … feeds only the size and stat data, never a file-type test …)"; S321 scope cell "add_patterns() open and type check" → "add_patterns() open and the fstat size read that follows it". Status, recheck and used-by unchanged.
  - Non-L1 re-open: S78ScoutSources re-fetched both captures sha256-identical and admitted both; its corrections were applied (knowledge entry; S324 quote length 12 tokens; SOURCES `Round-78 provenance` line declaring the S042/S300 overlaps).
- **Frontier advanced.** README "Frontier (r78 git discovery sources and LOG.md pointer resolution)". It stays frontier.
- **Mistakes mined:** seven (`corpus/lessons/round-78.md` `## Mistakes` M1–M4, `## Mistakes (wave)` M5–M7), each with captured-by and a fix shown able to fail or caught by a computed verdict.
- **Assimilation: none.** `considerthese/` is absent in this lane; no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved** — two mined tier-A rows on ground the lane did not hold (which files git opens at discovery and while reading a config), a new knowledge entry `corpus/knowledge/git-discovery-sources.md`, QUALITY Q140/Q141, two capability rows each backed by a receipt.
- **quality: improved** — the wave's seven gate routes outside the frozen rows were repaired with probes that can fail (run 1 at 8/9 kept), frozen counters stay at 0 at the repair; the r77 correction-sweep defect is closed in both cells and the lesson; the S78ScoutSources corrections were applied before filing.
- **discernment: improved** — S78CriticDiscern agrees 19/19 with the ledger classes and with the Gate's admit and reject; the lane recorded its own instrument and process errors (M1–M7) and accepted the critics' "operability reachable by bounding alone" and "C2 delta is the captures" findings as qualifications rather than contesting them.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r78 pre-report gate git-discovery-source counter (C1)" and "r78 location-bound pointer resolution counter (C2 …)" (`bbd199da`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 78` — the LOG pointer census captured 240 host-local files at their cited paths (`d90740fe`) and the gate ran over the lane at the tip (`census/round-78/records/c1-domain-trial.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: seven seats re-ran the prereg commands as written and reproduced every predicate (`census/round-78/records/wave-w1/seats/S78ExecC1.md`, `S78ExecC2.md`, `S78Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling gates and logs were documented, not edited (`census/round-78/records/wave-w1/seats/S78Connector.md`); the fleet misroot sweep found no file of this round.

## Other

- **Round shape:** one v1 wave `w1` of 12 seats, validated under `ufo-wave-policy.json` (band 8–16; `schema ufo-swarm-wave-dispatch-v1`, spawn 12) and dispatched via the inline handoff (`census/round-78/records/wave-w1/w1.ready.dispatched`). WAVE-DONE received. No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats 5 of 12 (42 %). The L1 holds the §3 planner seat.
- **Dead seats:** 0; all 12 wrote report files.
- **Seat incident:** S78ExecC1 ran `git restore` on the lane gate file, erasing the L1's uncommitted repair (lesson M7); caught by a digest check, receipts discarded, repair re-applied and committed before any receipt. The L1 also reaped three blocked git processes a seat's parallel counter runs leaked.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only orchestrator `.scratch/*` and the pre-existing `?? trail-ids.txt`; nothing of this round.
- **Routed to r79:** lesson `## Routed to round 79` (a)–(d) and SCORECARD "r79 (planned)".
- **Open L0 questions:** none new.
- **Tool installs:** none. No pacman transaction, no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r78/` removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.

Domain trial (C1 conjunct): `census/round-78/records/c1-domain-trial.txt` (landed `4632b99f5e887e969e7f6ad942fd16bfe1010dcf`, trial run at `a500ee69`) — `check-gitsource=PASS check-tip=PASS check-report=PASS check-shonen=PASS check-clean=PASS check-prereg=PASS`, `EXIT=0`, `wall_seconds=41.508582`; gate blob `5f5cb865…a853` = the repair R, and the receipt itself prints `amendment=b746bd9d…4eef -> 5f5cb865…a853` over the W blob; trial script sha256 `946e944d…1e5a` equal to its blob at master. It graded the first `report_lines=112` lines of this report (`head -n 112 | sha256sum` = `765e575f…e349`); the lines from this paragraph on were appended afterwards. A first trial (`census/round-78/records/attempts/c1-domain-trial-run1.txt`, landed `62b35a33`) graded an earlier revision of this report, before the measurements table the lane's report-contract checker requires was added (`tools/souji-report-contract.py`: 7/7 PASS after); the L1's `git mv` of that receipt touched only the git index and is lesson M8 (`a500ee69`).

Final lane hash: 4632b99f5e887e969e7f6ad942fd16bfe1010dcf
