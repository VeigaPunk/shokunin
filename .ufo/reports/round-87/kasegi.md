# kasegi — round 87 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. Base `cd1f568a6be2656b5f5dc479eb90ef99b91131b5`, freeze `afb13a88e6fbc8e2f8a0c11f9cfbfde77e907e69`, final lane hash `4d007eb1cbde0c3c4cc9d16464e316f0159bfbc5` (`git ls-remote origin refs/heads/master` prints it). L1: KasegiR87. Stale-lane: respawn-per-round driver; no other mission of this lane is open. Earlier attempts: none (`.ufo/watchdog.log` shows only the attempt-1 launch line for round 87; the lane was clean at start).

## Work performed

Declared claims (frozen in `.ufo/waves/round-87/claims.json` at `afb13a88`; every control was executed and committed before the freeze):

- **C1 — depth:verifiability** (lowest axis, score 4; an internal-citation repoint, so the score is not claimed to move). Knowledge-scope tranche 2: the frozen 83-key map `.ufo/waves/round-87/c1/repair-map.json` (S029 ×1, S040 ×1, S069 ×10, S100 ×1, S102 ×70) repoints bare snapshot citations whose basename is held by exactly one tracked file under `corpus/source-snapshots/`. Meter target 596/1720 → exactly 678/1719. Counter `.ufo/waves/round-87/c1/knowledge-meter.py` (r86 successor; M4 scoped to snapshots, new M7 keeps the r86 quoted manifest-field tokens untouched).
- **C2 — coverage, capability acquisition `capture-secret-scan`** (the round's sourced claim: S124, S125). The new instrument `corpus/instruments/capture-secret-scan.py` scans captures at a revision or a file list. It uses the claim-package gate's SECRET_PATTERNS plus AWS STS session-token and AWS key-id shapes, with a digest-bound allowlist. Counter `.ufo/waves/round-87/c2/capability-check.py` (limbs K1–K5). This answers r86 spot-check routed defect 1.

Work items:

- Protocol and history load: r86 spot-check routed defects 1–6 (`corpus/lessons/round-86-verifier-spotcheck.md` §6); r86 lesson; SCORECARD "Planned round 87". I did not take the planned C2 package re-freeze: the r86 package already passes its counter at the tip, so a do-nothing control would reach that target (prompt §9). Disposition is in `.ufo/waves/round-87/claims.json` `planned_row_disposition`.
- Sources opened and captured by the L1: S124 and S125 (`corpus/source-snapshots/round-87/`, two byte-identical fetches, `source-recheck.py` rc 0). Both were scanned before the freeze (`.ufo/waves/round-87/controls/capture-scan-r87.txt`).
- C1 pre-freeze controls (`.ufo/waves/round-87/controls/c1-controls-r87.txt`):
  - Do-nothing control: M1 596/1720, rc 1.
  - Negative controls, each rc 1: partial 636/1719; pad 679/1720; `.ufo` fixture copy (M4); ambiguous S041 key (M4 and M1); quoted-field key (M7); wrong map sha (M6).
  - Positive control: rc 0.
- C2 pre-freeze controls (`.ufo/waves/round-87/controls/c2-controls-r87.txt`):
  - Do-nothing control: K1–K5 all FAIL.
  - Negative controls, each rc 1: always-clean, gate-only, path-bound allowlist, corpus-wide scope, whole-tree scope, refusal disabled, empty allowlist, stale row, no SCORECARD row, wrong sha pin.
  - Positive control: rc 0.
  - The first two batteries hung (`c2-controls-r87-attempt{1,2}-timeout.txt`). The cause was a `git cat-file --batch` pipe deadlock in the first candidate past ~1,560 blobs (lesson M87-1). I fixed it before the freeze.
- C1 landing `d87b1b55`: counter pass, after 678/1719, M1–M7, rc 0; 13/13 pins (`.ufo/waves/round-87/l1/c1-landing-r87.txt`). Frozen P3 is false: the commit also carries 3 wave-scaffold files (M87-2).
- C2 landing `132e16c5`: K1–K5 pass (K2 `rc=1 sts_files=2` on r86 freeze `252df0c9`; K3 `hits=0 allowed=18 unused_allow=0`; K4 exact planted set and STS allowlist row refused rc 2); instrument and allowlist byte-equal to the frozen candidates (`.ufo/waves/round-87/l1/c2-landing-r87.txt`).
- Wave findings (all routed to r88; none re-scores a claim; `corpus/lessons/round-87.md` § Wave findings):
  - ExecC1Indep: independent re-derivation matches the map 83/83 (`.ufo/waves/round-87/w1/ExecC1Indep.md`).
  - ReviewC1Semantics: APPROVE, no key wrong.
  - CriticClaims: C1 NOT VERIFIED on P3, C2 VERIFIED, with qualifiers F2–F9.
  - CriticHarm: the only harm is P3; no gate verdict flips between base and landing.
  - ReviewC2Scanner: CHANGES-REQUESTED for r88 (scope misses `corpus/practice/*/evidence/`; HAR/percent-encoding/non-text gaps; `--files` untested by the counter).
  - MutC1Counter: 19/28 killed. MutC2Scanner: 14 killed, 5 survived. MutC2Counter: 12/19 killed.
  - ExecC2History: STS exposure ran from `a48fe8b9` (r85) to `e73c1f94`, both paths; clean from `b079a106` (`.ufo/waves/round-87/w1/ExecC2History.md`).
  - ScoutSources: live re-open finds every quote; erratum D-1; leads L1–L4 (GCS, Azure SAS, CloudFront, HackerOne `expiring_url`).
  - ConnectorOverlap: sibling scanners (kagi, mado, mori) catch provider token prefixes and URI basic auth that kasegi misses.
- Curation admitted outside the claims: `corpus/knowledge/presigned-url-credentials-in-captured-evidence.md` (ScribeEntry draft, reviewed by the L1).
- Dogfooding R138: before committing, I scanned all 117 new wave/lane files with `--files`: `hits=0` (`.ufo/waves/round-87/l1/capture-scan-wave-r87.txt`). I also ran a whole-tree diagnostic scan at the tip. It found no STS value anywhere; its hits are fixture literals and old seat fixtures (`.ufo/waves/round-87/l1/whole-tree-scan-r87.txt`).
- Swarm: one v1 wave `w1` of 12 seats, validated under `ufo-wave-policy.json` (spawn 12), dispatched by the inline handoff (`.ufo/waves/round-87/w1.ready`; WAVE-DONE received).
  - Roles: executor ×2 (ExecC1Indep, ExecC2History), reviewer ×2, mutation-tester ×3, critic ×2 (CriticClaims, CriticHarm), scout ×1, scribe ×1, connector ×1.
  - Attack seats: 7/12 = 58 %.
  - Dead seats: 0. All 12 seats have an output in `w1-results.json` and a report in `w1/`.
  - Residual call: none. Round total: 12.
  - Planner seat: held by the L1 (the validator rejects `planner`).

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `afb13a88e6fbc8e2f8a0c11f9cfbfde77e907e69` | freeze: claims, counters, map, candidates, controls and receipts, S124/S125 captures and manifest, rows queued | `LOG.md` Round 87 |
| `d87b1b55a51d78411438e962a9abbebdd17930cd` | C1 landing: map applied to 5 knowledge files (plus 3 wave-scaffold files swept in; M87-2) | `LOG.md` Round 87 |
| `132e16c588a2424c06b5ca15ea01fce1ee9a396d` | C2 landing: `capture-secret-scan.py`, `capture-secret-allow.tsv`, SCORECARD capability row | `LOG.md` Round 87 |
| `d7888107c5384496b55c2da97b6726b3faa4f28a` | knowledge entry; S124/S125 mined; QUALITY R138/R139; S122 rule-2 correction record; lesson; LOG; SCORECARD | `LOG.md` Round 87 |
| `4d007eb1cbde0c3c4cc9d16464e316f0159bfbc5` | wave evidence: results, 12 reports and receipts, landing.json, L1 receipts, assimilation scratch | `LOG.md` Round 87 |

## Before → after measurements

- **C1:**
  - Counting command: `python3 -B .ufo/waves/round-87/c1/knowledge-meter.py --lane <git clone --shared of d87b1b55 under /fast/scratch/hyaku/kasegi-r87/> --base-rev cd1f568a6be2656b5f5dc479eb90ef99b91131b5 --map .ufo/waves/round-87/c1/repair-map.json --target 678/1719 --map-sha256 7db928c77efe2f594c0fcbc26174b79db1f60f7a1d244055b679512c778f1eaa`.
  - Measured at `d87b1b55`: 596/1720 → 678/1719, M1–M7 pass, rc 0. Reproduced by ExecC1Indep.
  - P3 `git diff --name-only afb13a88 d87b1b55`: 3 paths outside `corpus/knowledge/`.
  - **Verdict: NOT VERIFIED (kill rule, P3 false).**
- **C2:**
  - Counting command: `python3 -B .ufo/waves/round-87/c2/capability-check.py --lane . --rev 132e16c588a2424c06b5ca15ea01fce1ee9a396d --work <scratch> --instrument-sha256 b2bf9d65e0a2bea99003ea7fdb3aec237449abb4ccd301f45b3ce496d161c6d1 --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6`.
  - Before (base `cd1f568a`): K1 FAIL (no instrument), rc 1.
  - After (`132e16c5`): `CAPABILITY-CHECK-RESULT pass rc=0`; re-run before filing, rc 0.
  - **Verdict: VERIFIED-pending-closure.**
- depth:density: `python3 corpus/instruments/density.py SKILL.md --label x` 273.2 → 273.2.

## Sources & frontier

- Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Result: 123 at base `cd1f568a`, 125 at `4d007eb1`.
- Rows added by tier: A ×2.
  - S124: AWS IAM, Create a signed AWS API request (SigV4), `S124.txt:83-85`, `:409`.
  - S125: AWS IAM, IAM identifiers / unique-ID prefixes, `S125.txt:303-332`.
- Rows touched old → new:
  - S124 and S125: `queued` → `mined`.
  - Their used-by: `—` → `corpus/instruments/capture-secret-scan.py, corpus/knowledge/presigned-url-credentials-in-captured-evidence.md`.
  - S122: named rule-2 correction record for its r86 in-place scope edit (`corpus/SOURCES.md` Registry changes).
- Rejected: the S3 SigV4 query-auth URL. It serves a meta-refresh shell, so there is nothing to capture. Flip condition: a direct-HTML URL.
- Frontier: four new leads for r88 (ScoutSources L1–L4). Census at round start: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` exit 0 (`.ufo/waves/round-87/controls/census-start-r87.txt`). Census at round end: exit 0 (`.ufo/waves/round-87/l1/census-end-r87.txt`). Both carry the same 6 inherited W04 warnings.
- Mined mistakes:
  - M87-1: pipe deadlock in the candidate instrument, caught by the forgery controls.
  - M87-2: unscoped landing path list. Fix QUALITY R139, shown able to fail in `.ufo/waves/round-87/l1/r139-check-r87.txt` (`outside=3 verdict=FAIL exit=1` on `d87b1b55`).
- Sourced claim: C2 (S124, S125).
- Assimilation: none. Collisions 94/94 (lane 125 ids, staged 94); guard proof nonempty (`.ufo/waves/round-87/assimilation/guard-proof.txt`).
- considerthese: `considerthese/2026-10-24.md:49-52` (upstream capture hygiene) fits, but is not implemented this round. It is routed to r88 as an intake gate in `capture-source.py`.

## Trend verdicts

- **expansion: improved.** Two tier-A AWS sources were mined. One admitted knowledge entry cites them. A new instrument class was added (credential screening of captures).
- **quality: unprovable-but-better.**
  - Gains: the r86 leak class is now detectable by a committed, mutation-attacked check. The 83 repointed citations all resolve, and ReviewC1Semantics approved them.
  - Against: C1's landing mixed scope (M87-2), and ReviewC2Scanner names real scope and detection gaps.
  - Non-author reviewers on record: ReviewC1Semantics, ReviewC2Scanner, CriticClaims.
- **discernment: improved.** C1 is reported NOT VERIFIED on its own P3 rather than reframed. A forgery control exposed a hidden deadlock before the freeze. The allowlist binds exact matched bytes, and every row was read in context by ReviewC2Scanner. One source was rejected on capture grounds.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/lessons/round-47-verifier-spotcheck.md` (unchanged).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/practice/curl-ibb-h1-1997312/report.md` (unchanged this round; round 87 adds the capture-screening operation, `LOG.md` Round 87).
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-47-verifier-spotcheck.md` (unchanged).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; documentation only, no live target contacted.

## Operator notes

- **Open L0:** `kasegi | round-86 | …` (an expired HackerOne STS token remains in the history of `252df0c9` and in the r85 receipt). The ExecC2History inventory now bounds it: commits `a48fe8b9`..`e73c1f94`, 2 paths. No new L0 question this round.
- **Tool installs:** none.
- **Inherited state:** none (the lane was clean at start).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator `.scratch/` entries and `trail-ids.txt`, which predates this round and belongs to no lane. No misroot.
- **Scratch:** `/fast/scratch/hyaku/kasegi-r87` removed.
