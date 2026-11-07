# kasegi — round 92 report (attempt 1, L1 KasegiR92)

## Work performed

Declared claims (frozen in `.ufo/waves/round-92/claims.json` at freeze `9e4f0d6830dcc9a30c6f524c48d074ec8979f040`, base `0628fd247914555838a42c02ba5d4ac08b7e095d`):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4; citation repair, score not claimed to move). Tranche 7 applies the 30 (site, key) labels that the round-91 non-author seat ReviewC1Labels wrote (`.ufo/waves/round-91/w1/ReviewC1Labels-receipts/round92-labels.tsv` at `d0bd4758`):
  - 25 pairs get exactly the edit their label names: 10 range repoints, 7 CORRECT qualifications, 2 dash cells (369/370), 2 token drops (58/144), 2 named repoints (150/152) and 2 whole-cell repairs (155/249). The files are `corpus/knowledge/triage-thresholds.md` and `root-loss-2026-10-12.md:68`.
  - 3 no-edit pairs and 2 EXCLUDED errata pairs (437, 438) stay unchanged. For 437 and 438, the label's repoint would make the quoted superseded text false.
  - The counter successor binds the map on (site, key) pairs, which closes r91 closure routed defect 2.
  - Pinned meter target: 947/1947 → 960/1944.
- **C2 — coverage** (score 8 held), capability extension of `capture-secret-scan`, sourced on S136 and S137. It adds the new shape `github-token`, which matches two forms:
  - GitHub's prefixed tokens `ghp_`/`gho_`/`ghu_`/`ghs_`/`ghr_` followed by exactly 36 base62 characters;
  - the stateless installation form `ghs_<APPID>_<JWT>`.
  This closes round-91 lead A, where all 8 bare-prefix fixtures were missed. Fine-grained `github_pat_` tokens remain a named known limit.

Work items:
- **Fresh-start read.** I read the r91 closure (`admitted`) and `kasegi-shokunin/corpus/lessons/round-91-verifier-spotcheck.md` §6 (routed defects 1–8). The disposition table is in `corpus/lessons/round-92.md` § Routed-defect disposition.
- **C1 counter.** `.ufo/waves/round-92/c1/knowledge-meter.py` is git-archive pinned (limbs M0, M1, M3–M6, M9, M10 on pairs; the docstring defines the kinds and EXCLUDED). The map is `c1/repair-map.tsv` and the applier is `c1/apply-map.py`.
  - Pre-freeze controls are in `.ufo/waves/round-92/controls/c1-controls-r92.txt`. The candidate passes. Each of these 10 controls fails: no-work, partial 24/25 (frozen map), partial own map, skip-qualify-59, excluded-437 applied, no-edit pair qualified, named-cell 155 token-only, drop-token 58 as a dash cell, wrong key column at 86, and working-tree-only.
- **C2 counter.** `.ufo/waves/round-92/c2/capability-check.py` (K1–K8):
  - K4 adds 12 round-92 plants: 6 positives and 6 boundary/negative plants, plus 4 more negatives (S031–S034).
  - K7 adds seeded GitHub positives and negatives. K8 maps 29 clauses.
  - Controls are in `controls/c2-controls-r92.txt`. The candidate passes both pinned and unpinned. The no-work base instrument fails, and so does each of forgeries F1–F10 (`controls/c2-forgeries.py`) on a behavioural limb, run unpinned.
- **Landings and receipts.**
  - C1 landing: `cb1ef2b9856df79c530f3ff1374fa9691ff56233`.
  - C2 landing: `58c0c115342877ee556cae19928d69839b0b29f0`.
  - Receipts are in `ee830069af1255043aeb39f1d324e6b3e5d69dbd` (`.ufo/waves/round-92/l1/c1-landing-r92.txt`, `c2-landing-r92.txt`).
- **Wave w1** (13 seats) attacked both landings. Findings are in `corpus/lessons/round-92.md` § Wave findings.
- **Integration commit** `2bb252492448c839ec77e6697303ebcc873cd627`:
  - admitted `corpus/knowledge/github-prefixed-tokens-in-captured-evidence.md`;
  - ran R143/R144 re-anchoring over all four entries that cite the scanner by line. The tool changed 78 tokens; 8 hand dispositions and 3 sentence corrections were also needed (`l1/reanchor-r92.txt`). The quote check goes from 2 bad at base to 0 (`l1/quote-anchor-r92.txt`);
  - moved S136 and S137 to `mined`;
  - added QUALITY R144.
- **Wave evidence:** `7ba6623edd8da9ac2dd4dc6fb0de7c754a490545`.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `9e4f0d6830dcc9a30c6f524c48d074ec8979f040` | freeze: claims, counters, map, candidate scanner and row, executed controls, S136–S138 snapshots + manifest, rows S136–S138, assimilation receipts | LOG.md Round 92 bullet 1 |
| `cb1ef2b9856df79c530f3ff1374fa9691ff56233` | C1 landing (`triage-thresholds.md`, `root-loss-2026-10-12.md`; 25 sites) | Round 92 bullet 2 |
| `58c0c115342877ee556cae19928d69839b0b29f0` | C2 landing (`capture-secret-scan.py`, SCORECARD capability row) | Round 92 bullet 3 |
| `ee830069af1255043aeb39f1d324e6b3e5d69dbd` | landing receipts P1–P3 | Round 92 bullets 2–3 |
| `2bb252492448c839ec77e6697303ebcc873cd627` | integration: new knowledge entry; four entries re-anchored and corrected (+ `l1/reanchor-scanner-cites.py`, receipts); S136/S137 mined; QUALITY R144; lesson, LOG, SCORECARD; round-end census receipt | Round 92 bullets 6–8 |
| `7ba6623edd8da9ac2dd4dc6fb0de7c754a490545` | wave w1 evidence (spec, dispatch, results, 13 reports + receipts) | Round 92 bullet 6 |

Lane pushed: `git ls-remote origin refs/heads/master` → `7ba6623edd8da9ac2dd4dc6fb0de7c754a490545`. `jj-lane.sh state` reports ahead=0 behind=0, tracked=0 untracked=0.

## Before → after measurements

- **C1** (measured against landing `cb1ef2b9`): pinned knowledge-scope meter **947/1947 → 960/1944**, `KNOWLEDGE-METER-RESULT pass rc=0`.
  - Limbs: M0, M1, M3, M4, M5, M6, M9 rows=25, M10 labelled=30 want=25 mapped=25.
  - M10 kind tally: dash-cell 2, drop-token 2, excluded 2, named 2, named-cell 2, no-edit 3, qualify 7, range 10.
  - P3: two paths.
  - Command: `python3 -B .ufo/waves/round-92/c1/knowledge-meter.py --lane <lane> --base-rev 0628fd247914555838a42c02ba5d4ac08b7e095d --after-rev cb1ef2b9856df79c530f3ff1374fa9691ff56233 --map .ufo/waves/round-92/c1/repair-map.tsv --labels-rev d0bd4758a41919b2c86c079f3a1a2dfb392dcd8d --base-target 947/1947 --target 960/1944 --map-sha256 6d87cafaec99961a15c00967d30c2bb164ed480d8b3fbaeadccd55b048d9b772 --work <scratch>`.
  - Do-nothing control: 947/1947, with M1 and M3 FAIL.
  - Re-run by ExecC1Indep (AGREE, including an independent byte check) and CriticClaims (STANDS).
- **C2** (measured against landing `58c0c115`):
  - Before: the base instrument misses all 6 round-92 plant entries (K4) and the 3 generated GitHub positives (K7), and 6 positive clauses fail (K8).
  - After: K1–K8 pass at seeds 989818075, 9191 and 1. K3 reads `scanned=1882 hits=0`, so the new shape adds no false positive on the lane tree.
  - Command: `python3 -B .ufo/waves/round-92/c2/capability-check.py --lane <lane> --rev 58c0c115342877ee556cae19928d69839b0b29f0 --work <scratch> --instrument-sha256 04666f676c09cc3d32e41d506c8198936ac04aff33b207813aab39304baf3a9e --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6 [--seed N]`.
  - Re-run by CriticClaims (seeds 9191, 1, 271828, 314159: STANDS) and ReviewC2Scanner (seed 1545880357).
- **depth:density guard:** SKILL.md 273.2 → 273.2. The SKILL.md sha256 is identical at base and tip (CriticHarm).
- **Integration anchor repair (R143/R144, not a claim):** `python3 -B .ufo/waves/round-91/l1/quote-anchor-check.py --lane . <entries>`.
  - The four citing entries read `bad=2` against the base instrument, both from round 88 (M92-2), and `bad=6` against the C2 landing.
  - After the re-anchor, those four entries plus the admitted entry read `bad=0 out_of_range=0` (85 quotes, 338 citations).

Verdicts (pending non-author closure):
- **C1 VERIFIED** on P1–P3. Qualifiers:
  - ReviewC1Sites judges 16 of the 25 landed rows CORRECT, 7 partial and 2 WRONG. In the WRONG rows (58 and 144), the label's "keep `SKILL.md:117`" leaves a tie that does not state the rule. The tie was already there; it is routed to a round-93 label (`SKILL.md:191`).
  - P1 is scope-bound to `corpus/knowledge`, so P3 alone catches an out-of-scope edit (CriticClaims variant B).
  - MutC1Counter: 22 of 29 mutants survive the scripted controls. Measured proposed controls kill 15 of them; the other 7 are shown entailed.
- **C2 VERIFIED** on P1–P3. Qualifiers:
  - Forged instruments pass K1–K8 when the sha256 pins are omitted: 7 of 8 at every seed tried, including a path-keyed lookup table and a harness-gated detector (MutC2Counter). The behavioural limbs also miss the `_`/digit boundary, tail-alphabet, JWT-floor and app-id bounds (CriticClaims D-1; 10 MutC2Scanner survivors). Only the pins reject them; this is routed as counter defects D1–D5.
  - Bypasses (SentinelGitHub P1): escape sequences whose last byte is a letter or digit (`\t`, `\u0020`, `%20`, `%3A`, …) hide a token. A one-line boundary patch has been measured.
  - The landed shape also hits GitHub's own documentation example tokens (ScoutSources, SentinelGitHub §3).
- No axis harmed. CriticHarm finds NO HARM on density, false positives, ReDoS (linear), old capabilities (round-91 counter K1–K8 unpinned; intake gate) and C1 class movement.

## Sources & frontier

- **Census.**
  - Start (`.ufo/waves/round-92/controls/census-start-r92.txt`): `kasegi ok`, rc 0, 6 inherited W04, registry 135 rows.
  - End (`.ufo/waves/round-92/l1/census-end-r92.txt`): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` gave `kasegi ok`, rc 0, the same 6 W04, registry **138** rows.
  - Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Rows added by tier:** tier A +2, tier B +1.
  - **S136** (GitHub Docs, About authentication to GitHub), opened 2026-11-07. Quote at S136.txt:158: "GitHub issues tokens that begin with a prefix to indicate the token's type."
  - **S137** (GitHub Blog, Behind GitHub's new authentication token formats), opened 2026-11-07. Quote at S137.txt:167: "A 32 bit checksum in the last 6 digits of each token".
  - S136 and S137 went from `queued` (freeze) to `mined` (integration). Used-by changed from `—` to `corpus/instruments/capture-secret-scan.py, corpus/knowledge/github-prefixed-tokens-in-captured-evidence.md`.
  - **S138** (W3C HAR draft, tier B) was opened and rejected. Its quote at S138.txt:30-31 reads "never published … has been abandoned". The capture is committed, so the rejected row's anchors resolve (r91 routed defect 5). ScoutSources AGREES clause by clause, and the flip is unmet.
- **Sourced claim:** C2 rests on S136 and S137. Both the instrument docstring and the admitted entry cite S136 lines 158–167 and S137 lines 156–174.
- **Frontier:** a new edge class for the capture scanner: bare provider-prefixed tokens with no key name. ScoutSources opened two round-93 leads, both measured as misses by the landed scanner:
  - fine-grained `github_pat_` (22 + `_` + 59), from GitHub's REST API description;
  - GitLab `glpat-` + 20.
- **Mistakes mined** (see `corpus/lessons/round-92.md` § Mistakes):
  - M92-1: registry kind enum drift. The census caught it before the freeze; receipt `l1/m92-1-kind-enum.txt`.
  - M92-2: the round-91 re-anchor covered fewer entries than cite the instrument, so two quotes have been stale since round 88. Fixed by QUALITY R144.
  - M92-3: diff-mapped anchors widen over new text, and a bare continuation token was misattributed. The quote checker accepts both, so they were fixed by hand; ReviewC2Scanner's list caught two remaining off-by-one ranges.
- **considerthese:** no new proposal mined. The latest file's open items were taken in rounds 87–90.
- **Assimilation: none.** Collisions are 94/94 (`.ufo/waves/round-92/assimilation/collisions`; the staged file predates S031–S138). Reg-ids 138, staged 94. The quarantine slice has 7 rows, which were not hand-checked; nothing was appended.

## Trend verdicts

- **expansion: improved.** Two tier-A first-party sources were mined and one was rejected with a committed capture; the registry went 135 → 138. One new knowledge entry was admitted. `capture-secret-scan` gains a provider-prefix class: the base instrument misses all 6 new plant entries (K4/K6), and 21 realistic encodings are detected (SentinelGitHub).
- **quality: improved.**
  - 25 non-author-labelled citation pairs now carry the edits their labels name, and the meter reads 947/1947 → 960/1944. M10 now binds (site, key) pairs, which closes r91 routed defect 2.
  - Two quotes that had been stale since round 88 were repaired, and 75+ shifted instrument citations were re-anchored (bad 2 → 0). R144 was added.
  - Qualifier: 2 of the 25 rows still carry a wrong surviving tie (routed).
- **discernment: unprovable-but-better.** Non-author seats agreed with the S138 rejection (ScoutSources), the two EXCLUDED errata pairs and the three no-edit pairs (ReviewC1Sites), and the EXCLUDED freeze timing (CriticClaims). The outside closure spot-check is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md` (line 94); SKILL.md unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `kasegi-shokunin/corpus/practice/curl-h1-1913733/report.md` (LOG Round 85), `corpus/practice/curl-ibb-h1-1997312/report.md` (LOG Round 86).
- [~] Instructions executable by an agent without oral context — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE.md unchanged (`git diff --stat 0628fd24 7ba6623e -- PROVINCE.md` empty); live-target testing still refused.

## Round shape and other

- **Shape:** ONE v1 wave of **13 seats** (policy `ufo-wave-policy.json`, band 8–16), dispatched through the inline handoff (`w1.ready`, l1 KasegiR92; WAVE-DONE received).
  - Roles: reviewer 3, mutation-tester 3, critic 2, executor 1, sentinel 1, scout 1, connector 1, scribe 1.
  - Attack seats: 8/13 (62 %).
  - No residual call; round total 13. Dead seats: 0 (`w1-results.json`: 13/13 settled, each wrote its report).
  - The L1 holds the planner seat; the round-93 label data-walk rode ReviewC1Labels.
- **Hygiene:**
  - Every new wave file, the admitted entry and the lesson were scanned with the landed scanner (`--files`): scanned=99, hits=0 (`.ufo/waves/round-92/l1/wave-scan-r92.txt`).
  - A literal grep for GitHub token shapes over the same files is empty.
  - Committed fixtures build token values at run time, so no contiguous token literal is committed.
  - Every seat reports its scratch deleted. `/fast/scratch/hyaku/kasegi-r92` was removed after landing.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/` (orchestrator-owned) and the pre-existing untracked `f.txt` and `trail-ids.txt` (not kasegi's, already noted by the r91 closure). No kasegi misroot was found.
- **Inherited state:** none. The lane was clean at start, and there is no `lane-dead-no-report kasegi round=92`.
- **Open L0 questions:** unchanged (`kasegi | round-77`, `kasegi | round-89`); none added.
- **Tool installs:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
