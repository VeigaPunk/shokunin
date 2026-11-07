# kasegi — round 91 report (attempt 1, L1 KasegiR91)

## Work performed

Declared claims (frozen in `.ufo/waves/round-91/claims.json` at freeze `53ab692a7b544c35141e2b19f7413cbdb767c1ad`, base `bb4309fffbe9bf98153a2933af72c8f2c3f4b5b1`):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4; citation repair, score not claimed to move). Tranche 6: the six round-91 labels that the round-90 non-author seat ReviewC1Sites wrote (`.ufo/waves/round-90/w1/ReviewC1Sites-receipts/round91-labels.tsv` at `e993fd18`) are applied as exactly the edits they name in `corpus/knowledge/triage-thresholds.md`. Sites 141, 142, 226 and 368 each lose a `MATCHES:` tie that no range of the cited entry supports; the tie becomes the table's `—`. Site 454 is repointed to `corpus/knowledge/ev-model.md:13-25`. Site 457's composite token becomes `corpus/knowledge/claim-package-contract.md:9-16`. The counter successor adds M9 (each edit equals the edit its label names) and M10 (mapped sites = labelled sites; r90 closure routed defect 1). Pinned meter 890/1883 → exactly 891/1880.
- **C2 — coverage** (score 8 held), capability extension of `capture-secret-scan`, sourced on S133 and S134. A new shape, `cloudfront-signed-cookie-signature`, covers CloudFront signed cookies, which were a documented known limit until now. The Azure SAS name window widens from 2–6 to 2–7 letters, so a user-delegation SAS carrying `skdutid` is no longer missed.

Work items:
- Fresh-start read: the r90 closure (`admitted`) and `kasegi-shokunin/corpus/lessons/round-90-verifier-spotcheck.md` §6 (routed defects 1–7). Disposition table: `corpus/lessons/round-91.md` § Routed-defect disposition.
- C1 counter `.ufo/waves/round-91/c1/knowledge-meter.py` (git-archive pinned; M0, M1, M3–M6, M9, M10), map `c1/repair-map.tsv`, applier `c1/apply-map.py`. Pre-freeze controls `.ufo/waves/round-91/controls/c1-controls-r91.txt`: the candidate passes. Each of these fails: no-work, partial 5/6 (with the frozen map and with its own map), superset with an unlabelled edit, wrong range at 454, label ignored at 457, and working-tree-only.
- C2 counter `.ufo/waves/round-91/c2/capability-check.py` (K1–K8; K4 has 13 new plants, including the boundary pairs 39/40 floor, 8-letter name, case, `-` prefix and scope; K7 adds seeded cookie and skdutid positives and negatives; K8 has 13 clauses). Controls are in `controls/c2-controls-r91.txt`. The candidate passes, both pinned and unpinned. The no-work base instrument fails, and so does each of forgeries F1–F8, run unpinned (`controls/c2-forgeries.py`).
- Landings: C1 `8a1a00c639ba808a701d1f186aac9ebd0045deaa`, C2 `1dd0723fbd0bdc01d2244322f8df8c8c6f1adb70`. Receipts are in `bcbfbde63b83c9336e845001323b5c92419e526a` (`.ufo/waves/round-91/l1/c1-landing-r91.txt`, `c2-landing-r91.txt`).
- Wave w1 (13 seats) attacked both landings; findings are in `corpus/lessons/round-91.md` § Wave findings. Integration commit `2bdde26bb6b92cb773d7ada3835cd2872f6877e5`:
  - admitted `corpus/knowledge/cloud-signed-cookies-and-user-bound-sas.md`;
  - re-anchored 97 instrument citation tokens in `cloud-signed-url-credentials-in-captured-evidence.md` and `capture-intake-gate.md`, which the C2 landing had shifted, and rewrote their now-false sentences (ReviewC2Scanner F1, M91-3);
  - moved S133 and S134 to `mined`;
  - added QUALITY R143.
- Wave evidence: `d0bd4758a41919b2c86c079f3a1a2dfb392dcd8d`.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `53ab692a7b544c35141e2b19f7413cbdb767c1ad` | freeze: claims, counters, map, candidate scanner and row, executed controls, S133/S134 snapshots + manifest, rows S133–S135, assimilation receipts | LOG.md Round 91 bullet 1 |
| `8a1a00c639ba808a701d1f186aac9ebd0045deaa` | C1 landing (`triage-thresholds.md` only, 6 sites) | Round 91 bullet 2 |
| `1dd0723fbd0bdc01d2244322f8df8c8c6f1adb70` | C2 landing (`capture-secret-scan.py`, SCORECARD capability row) | Round 91 bullet 3 |
| `bcbfbde63b83c9336e845001323b5c92419e526a` | landing receipts P1–P3 | Round 91 bullets 2–3 |
| `2bdde26bb6b92cb773d7ada3835cd2872f6877e5` | integration: new knowledge entry, two entries re-anchored and corrected (+ `l1/reanchor-scanner-cites.py`, `l1/quote-anchor-check.py` and receipts), S133/S134 mined, QUALITY R143, lesson, LOG, SCORECARD | Round 91 bullets 6–8 |
| `d0bd4758a41919b2c86c079f3a1a2dfb392dcd8d` | wave w1 evidence (spec, dispatch, results, 13 reports + receipts), round-end census receipt | Round 91 bullet 6 |

Lane pushed: `git ls-remote origin refs/heads/master` → `d0bd4758a41919b2c86c079f3a1a2dfb392dcd8d`. `jj-lane.sh state` reports ahead=0 behind=0, tracked=0 untracked=0.

## Before → after measurements

- **C1** (measured against landing `8a1a00c6`): pinned knowledge-scope meter **890/1883 → 891/1880**, `KNOWLEDGE-METER-RESULT pass rc=0` (M0, M1, M3, M4, M5, M6, M9 6/6, M10 labelled=6 mapped=6).
  - Command: `python3 -B .ufo/waves/round-91/c1/knowledge-meter.py --lane <lane> --base-rev bb4309fffbe9bf98153a2933af72c8f2c3f4b5b1 --after-rev 8a1a00c639ba808a701d1f186aac9ebd0045deaa --map .ufo/waves/round-91/c1/repair-map.tsv --labels-rev e993fd181e320f1f21e06b05e16c68b0f07cff76 --base-target 890/1883 --target 891/1880 --map-sha256 55d50b661bcf79ad5a435c7d7bc86e3954e9910f7dabc480236224170c8c0a7a --work <scratch>`.
  - Do-nothing control: 890/1883, with M1 and M3 FAIL.
  - Re-run by CriticClaims and ExecC1Indep (AGREE; live lane and shared clone byte-identical).
- **C2** (measured against landing `1dd0723f`):
  - Before: the base instrument misses all 6 round-91 plant entries (K4) and the 3 generated positives (K7), and 6 positive clauses fail (K8).
  - After: K1–K8 pass at seeds 2890978206, 9191 and 1.
  - Command: `python3 -B .ufo/waves/round-91/c2/capability-check.py --lane <lane> --rev 1dd0723fbd0bdc01d2244322f8df8c8c6f1adb70 --work <scratch> --instrument-sha256 89e283c6423216917c8ae31e1f72239f56ebcb842bda72f7bad4b2f36dc526d7 --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6 [--seed N]`.
  - Re-run by CriticClaims (seeds 424242, 9191, 1) and ReviewC2Scanner (seeds 2068659922, 9191, 1).
- **depth:density guard:** SKILL.md 273.2 → 273.2 (`python3 corpus/instruments/density.py SKILL.md --label x`; SKILL.md sha256 identical at base and tip, CriticHarm).
- **Integration anchor repair (R143, not a claim):** `python3 -B .ufo/waves/round-91/l1/quote-anchor-check.py --lane . <entries>`.
  - The two entries read `bad=0` against the base instrument and `bad=4` against the C2 landing.
  - After the re-anchor, the two entries plus the admitted entry read `bad=0 out_of_range=0` (57 quotes, 228 citations; `.ufo/waves/round-91/l1/quote-anchor-r91.txt`).

Verdicts (pending non-author closure):
- **C1 VERIFIED** on P1–P3. Qualifiers:
  - ReviewC1Sites judges 5/6 rows CORRECT. Row 454's edited token is correct, but its untouched second token `SKILL.md:494-506` does not state the EV formula. This is pre-existing and routed.
  - M10 compares site sets, not (site, key) pairs (CriticClaims C1-F1).
- **C2 VERIFIED** on P1–P3. Qualifiers:
  - Four statement clauses have no K8 clause or plant: the `\u0026`/`%26` cookie boundary, a preceding letter, digit or `_`, the generic `\n` join, and the Azure 2-letter lower bound. CriticClaims FC1–FC4 pass every K limb unpinned, while the landed instrument implements all four clauses.
  - Every forgery is also caught by the instrument's own selftest (MutC2Counter).
  - Bypasses: colon-form dumps, cookie jars and quoted values (SentinelCookie F1–F3).
- No axis harmed. CriticHarm finds NO HARM on density, false positives (0 hits on 1734 capture files and 113 snapshots), old capability commands and ReDoS. The one harm the wave found, the shifted knowledge anchors (M91-3), was repaired in the integration commit.

## Sources & frontier

- **Census.**
  - Start (`.ufo/waves/round-91/controls/census-start-r91.txt`): `kasegi ok`, rc 0, 6 inherited W04, registry 132 rows.
  - End: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` gave `kasegi ok`, rc 0, the same 6 W04, registry **135** rows (`.ufo/waves/round-91/l1/census-end-r91.txt`).
  - Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Rows added by tier:** tier A +3.
  - **S133** (Microsoft Learn, Create a user delegation SAS), opened 2026-11-07. Quote at S133.txt:571: "The sduoid and skdutid fields are supported with version 2025-07-05 and later."
  - **S134** (CloudFront signed cookies, custom policy), opened 2026-11-07. Quote at S134.txt:17: "and a CloudFront signed cookie requires three name-value pairs."
  - S133 and S134 moved from status `queued` (freeze) to `mined` (integration). Used-by changed from `—` to `corpus/instruments/capture-secret-scan.py, corpus/knowledge/cloud-signed-cookies-and-user-bound-sas.md`.
  - **S135** (canned-policy signed cookies) was rejected: it has the same signature cookie form as S134, and `CloudFront-Expires` is a timestamp. The flip condition is recorded. ScoutSources re-opened it and AGREES with the rejection clause by clause.
- **Sourced claim:** C2 rests on S133 and S134. The instrument docstring cites S133 lines 177 and 566-571 and S134 lines 19, 40, 96-98, 123 and 428. The admitted entry cites both.
- **Frontier:** two new edge classes for the capture scanner (cookie-borne signatures; user-bound SAS). Round-92 leads opened by ScoutSources:
  - A — GitHub *About authentication to GitHub*, token prefixes at line 158: open. Bare provider-prefixed tokens are missed.
  - B — Azure account SAS: closed, already detected.
  - C — HAR cookie object: open but tier-limited, because the W3C draft marks itself abandoned.
- **Mistakes mined** (see `corpus/lessons/round-91.md` § Mistakes):
  - M91-1: a boundary tuned to the separator, not the container. It was caught by the positive control before the freeze, and forgery F8 now fails.
  - M91-2: a meter-blind edit. Site 457 is invisible to resolve.py and bound only by M3/M10.
  - M91-3: an instrument landing shifts knowledge anchors. QUALITY R143; quote check `bad=4` → `bad=0`.
- **considerthese:** no new proposal mined. The latest file's open items were taken in rounds 87–90; C2 extends the same capture-hygiene line by source-grounded shapes.
- **Assimilation: none.** Collisions 94/94 (`.ufo/waves/round-91/assimilation/collisions`; the staged file predates S031–S135). Reg-ids 135, staged 94. The quarantine slice has 7 rows, which were not hand-checked; nothing was appended.

## Trend verdicts

- **expansion: improved.** Two tier-A first-party sources were mined and one rejected with a flip; registry 132 → 135. One new knowledge entry was admitted. The `capture-secret-scan` capability gains a shape for a form it previously named as a known limit; the base instrument misses all 6 new plant entries (K4/K6).
- **quality: improved.**
  - Six non-author-labelled citation sites now carry the edits their labels name; 5/6 rows were judged CORRECT by a non-author whole-row read.
  - 97 instrument citations that the landing shifted were re-anchored, and the stale sentences were corrected. The quote/anchor check goes from 4 bad to 0.
  - The r90 closure's completeness defect is closed (M10).
  - R143 was added.
- **discernment: unprovable-but-better.** Non-author lane seats reviewed both the S135 rejection (ScoutSources AGREE) and the six label-named edits (ReviewC1Sites). The outside closure spot-check is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md` (line 94); SKILL.md unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `kasegi-shokunin/corpus/practice/curl-h1-1913733/report.md` (LOG Round 85), `corpus/practice/curl-ibb-h1-1997312/report.md` (LOG Round 86).
- [~] Instructions executable by an agent without oral context — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE.md unchanged (`git diff --stat bb4309ff d0bd4758 -- PROVINCE.md` empty); live-target testing still refused.

## Round shape and other

- **Shape:** ONE v1 wave of **13 seats** (policy `ufo-wave-policy.json`, band 8–16), dispatched through the inline handoff (`w1.ready`, l1 KasegiR91; WAVE-DONE received).
  - Roles: reviewer 3, executor 1, mutation-tester 3, critic 2, sentinel 1, scout 1, connector 1, scribe 1.
  - Attack seats: 8/13 (62 %; reviewer, critic, mutation-tester).
  - No residual call; round total 13. Dead seats: 0 (`w1-results.json`, 13/13 with output).
  - The L1 holds the planner seat; the round-92 label data-walk rode ReviewC1Labels.
- **Hygiene:**
  - Every wave file, the admitted entry and the lesson were scanned with the landed scanner (`--files`, repo-relative): scanned=172, hits=0 (`.ufo/waves/round-91/l1/wave-scan-r91.txt`).
  - Every seat reports its scratch deleted. `/fast/scratch/hyaku/kasegi-r91` was removed after landing.
  - ScribeEntry's FC blocks use `mktemp -d -p "${TMPDIR:-/tmp}"` for fixtures under 1 KB (the round-88 entry form); the seat's own runs used `/fast/scratch`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked `f.txt` (2 B, mtime 04:40:38, before this round's 04:45:36 launch; already noted by the r90 closure) and `trail-ids.txt` (2026-11-06 20:36). Neither was written by a kasegi r91 seat, and both were left untouched. `.scratch/` is orchestrator-owned and was not touched.
- **Inherited state:** none (lane clean at start; no `lane-dead-no-report kasegi round=91`).
- **Open L0 questions:** unchanged (`kasegi | round-77`, `kasegi | round-89`); none added.
- **Tool installs:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
