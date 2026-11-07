# kasegi — round 90 report (attempt 1, L1 KasegiR90)

## Work performed

Declared claims (frozen in `.ufo/waves/round-90/claims.json` at freeze `33f43db99c06e89bb9fb78c538313e9450da649f`, base `6088c3eb0c29040415c69e7b5fb91e110480ab26`):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4; internal-citation repoint, score not claimed to move). Tranche 5: 34 citing sites in `corpus/knowledge/triage-thresholds.md` that the round-89 non-author seat ReviewC1Labels labelled WRONG with a supported range are repointed per site. 4 sites are excluded because their label reason says the row content is stale (`c1/excluded.tsv`). The successor counter pins every reading to the measured revision (r89 closure routed defect 1). Meter 812/1827 → exactly 843/1829.
- **C2 — coverage** (score 8 held), capability acquisition `capture-intake-gate`, sourced on S131. Before it opens the snapshot file, `corpus/instruments/capture-source.py` now scans the capture with `capture-secret-scan`. On a hit it exits 3, writes nothing, keeps any existing file and prints the shape and line but never the value. It fails closed and honours the digest-bound allowlist. This implements `considerthese/2026-10-24.md:49-52` after four routings.

Work items:
- Fresh-start read: r89 closure (`admitted`) and `kasegi-shokunin/corpus/lessons/round-89-verifier-spotcheck.md` §6 (routed defects 1–6). The disposition table is in `corpus/lessons/round-90.md` § Routed-defect disposition.
- C1 counter `.ufo/waves/round-90/c1/knowledge-meter.py` (git-archive pinned; M0 base limb added per r89 C1-F1; per-site M3; M9 label binding), map `c1/repair-map.tsv`, applier `c1/apply-map.py`. Pre-freeze controls `.ufo/waves/round-90/controls/c1-controls-r90.txt`: the candidate passes; no-work, shift+1, superset, unlabelled and working-tree-only all fail. Environment receipt: the r89 meter reads `b9fcf005` as 815 live / 814 clean clone; the r90 meter reads 812 / 812.
- C2 counter `.ufo/waves/round-90/c2/capability-check.py` (G0–G6, P; shapes derived from the scanner at REV; loopback HTTP inputs; seeded plants). Controls `controls/c2-controls-r90.txt`: the candidate passes. The no-work base instrument fails, and so does each forgery: F1 blanket, F2 AWS-only, F3 write-then-check, F4 allowlist ignored, F5 fail-open, F6 leaky.
- Landings: C1 `4a7e676895d3fc74e18c853457c9b465ade2ddf5`, C2 `643ddb4379536e7a5ff7cdfe5c5befe9afbf63f2`; receipts `779062a3676cc6b10bf855f18ff897baf0cc6fd5` (`.ufo/waves/round-90/l1/c1-landing-r90.txt`, `c2-landing-r90.txt`).
- Wave w1 (12 seats) attacked both landings; findings are in `corpus/lessons/round-90.md` § Wave findings. Integration `124e5b49db2591ec39813c8d1a63be06912463db`: knowledge entry admitted, glosses on sites 158/439 repaired (M90-3), S131 mined, QUALITY R142. Wave evidence `e993fd181e320f1f21e06b05e16c68b0f07cff76`.
- **Correction filed** (r89 routed defect 1): the round-89 tip reading "814/1827 at `b9fcf005`" cannot be re-derived. Pinned to the revision it reads **812/1827** (`controls/c1-controls-r90.txt`; SCORECARD round-90 section).

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `33f43db99c06e89bb9fb78c538313e9450da649f` | freeze: claims, counters, map, exclusions, candidate, executed controls, S131 snapshot + manifest, S131 queued / S132 rejected rows, assimilation receipts | LOG.md Round 90 bullet 1 |
| `4a7e676895d3fc74e18c853457c9b465ade2ddf5` | C1 landing (`triage-thresholds.md` only, 34 sites) | Round 90 bullet 2 |
| `643ddb4379536e7a5ff7cdfe5c5befe9afbf63f2` | C2 landing (`capture-source.py`, instruments README, SCORECARD capability row) | Round 90 bullet 3 |
| `779062a3676cc6b10bf855f18ff897baf0cc6fd5` | landing receipts P1–P3 | Round 90 bullets 2–3 |
| `124e5b49db2591ec39813c8d1a63be06912463db` | integration: `corpus/knowledge/capture-intake-gate.md`, 158/439 gloss repair, S131 mined, QUALITY R142, lesson, LOG, SCORECARD | Round 90 bullets 6–8 |
| `e993fd181e320f1f21e06b05e16c68b0f07cff76` | wave w1 evidence (spec, dispatch, results, 12 reports + receipts), round-end census receipt | Round 90 bullet 6 |

Lane pushed: `git ls-remote origin refs/heads/master` → `e993fd181e320f1f21e06b05e16c68b0f07cff76`; `jj-lane.sh state` ahead=0 behind=0, tracked=0 untracked=0.

## Before → after measurements

- **C1** (measured against landing `4a7e6768`): pinned knowledge-scope meter **812/1827 → 843/1829**, `KNOWLEDGE-METER-RESULT pass rc=0` (M0, M1, M3, M4, M5, M6, M9 34/34). Command: `python3 -B .ufo/waves/round-90/c1/knowledge-meter.py --lane <lane> --base-rev 6088c3eb0c29040415c69e7b5fb91e110480ab26 --after-rev 4a7e676895d3fc74e18c853457c9b465ade2ddf5 --map .ufo/waves/round-90/c1/repair-map.tsv --labels-rev 02b6d88f1c059e2f881fd07c73834f502b4f212d --base-target 812/1827 --target 843/1829 --map-sha256 7c420856c3347d362bfc419030aa474cbc253975f3026bc13355b654055fb8b3 --work <scratch>`. Do-nothing control: 812/1827, M1+M3 FAIL. Re-run by CriticClaims and ExecC1Indep (live lane and shared clone byte-identical).
- **C2** (measured against landing `643ddb43`): before, the base instrument writes all 11 plants, destroys an existing file and has no allowlist (G1/G2/G4/G5 FAIL). After, G0–G6 and P pass at the runtime seed and at seeds 9090 and 1. Command: `python3 -B .ufo/waves/round-90/c2/capability-check.py --lane <lane> --rev 643ddb4379536e7a5ff7cdfe5c5befe9afbf63f2 --base-rev 6088c3eb0c29040415c69e7b5fb91e110480ab26 --work <scratch> --instrument-sha256 0630d32b98d40bd07c4716b0062babfaa1a8cee6b8bb4103c582b71d41d53dbf [--seed N]`. Re-run by CriticClaims at seeds 9090, 1 and 1132209826.
- **depth:density guard:** SKILL.md 273.2 → 273.2 (`python3 corpus/instruments/density.py SKILL.md --label x`; SKILL.md untouched).

Verdicts (pending non-author closure): C1 **VERIFIED** on P1–P3, with this qualifier: ReviewC1Sites found 2 of 34 sites (158 and 439) carrying a stale gloss that the new range refutes. The glosses were repaired at integration; the tokens are unchanged. C2 **VERIFIED** on P1–P3, with these qualifiers: the counter leaves the `line=` field, whole-bytes scanning, `--kind text` refusal and "imported" unbound, and a missing `--allow` file loads as empty. The landed bytes were probed directly on each. No axis harmed (CriticHarm: density, callers, SOURCES all NO HARM; F1 = M90-3, repaired).

## Sources & frontier

- Census start (base corpus, `controls/census-start-r90.txt`): `kasegi ok`, rc 0, 6 inherited W04, registry 130 rows. Census end: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` gave `kasegi ok`, rc 0, same 6 W04, registry **132** rows (`.ufo/waves/round-90/l1/census-end-r90.txt`). Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Rows added by tier: tier A +2. **S131** (GitHub push protection) opened 2026-11-07; quote at S131.txt:570 "push protection blocks pushes that contain secrets before they reach your repository". Status `queued` → `mined`; used-by `—` → `capture-source.py`, `capture-intake-gate.md`. **S132** (GitLab secret push protection) rejected: its skip conditions are the fail-open path the gate refuses by design. Flip condition recorded.
- Sourced claim: C2 on S131 (instrument docstring cites S131.txt:570; knowledge entry cites S131:570/610/612-613).
- Frontier: a new operation (refuse-before-write intake). Round-91 leads opened by ScoutSources: Microsoft *Create a user delegation SAS* (`skdutid`) and GitHub *Supported secret scanning patterns*.
- Mistake mined: M90-1 (meter reads the ambient tree; R142, shown able to fail), M90-2 (harness `file://` vs real HTTP), M90-3 (selection reads the label reason, not the row). See `corpus/lessons/round-90.md` § Mistakes.
- considerthese: `2026-10-24.md:49-52` intake gate implemented as C2.
- **Assimilation: none.** Collisions 94/94 (`.ufo/waves/round-90/assimilation/collisions`; the staged file predates S031–S132). Reg-ids 132, staged 94, quarantine slice 7 rows, not hand-checked.

## Trend verdicts

- **expansion: improved.** One new tier-A source mined and one rejected with a flip condition. A new capability row (`capture-intake-gate`) and a new knowledge entry; registry 130 → 132.
- **quality: improved.** Readings are now revision-pinned (R142), with an environment receipt showing the r89 meter disagree 815/814 and the r90 meter agree 812/812. 34 bare or wrong citations now resolve to non-author-labelled ranges, with 32/34 judged CORRECT and the 2 stale glosses repaired. The 814 → 812 correction is filed.
- **discernment: unprovable-but-better.** The S132 rejection and the 4 exclusions were reviewed by non-author seats (ReviewC1Sites agrees 4/4; ScoutSources confirms the S132 reason on the live page). The outside closure spot-check is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md` (line 94); SKILL.md unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `kasegi-shokunin/corpus/practice/curl-h1-1913733/report.md` (LOG Round 85), `corpus/practice/curl-ibb-h1-1997312/report.md` (LOG Round 86).
- [~] Instructions executable by an agent without oral context — evidence: `kasegi-shokunin/corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE.md unchanged (`git diff --stat 6088c3eb e993fd18 -- PROVINCE.md` empty); live-target testing still refused.

## Round shape and other

- Shape: ONE v1 wave of **12 seats** (policy `ufo-wave-policy.json`, band 8–16), dispatched through the inline handoff (`w1.ready`, l1 KasegiR90). Roles: reviewer 2, executor 1, mutation-tester 3, critic 2, sentinel 1, scout 1, connector 1, scribe 1. Attack seats: 7/12 (58 %; reviewer, critic, mutation-tester). No residual call; round total 12. Dead seats: 0 (`w1-results.json`, 12/12 with output). The planner seat is held by the L1.
- Hygiene: ReviewC2Gate's preamble names `mktemp -d /tmp/...` for scratch, against the scratch directive (it is a seat defect; no tree remains). `/fast/scratch/hyaku/kasegi-r90` was removed after landing. The wave-file credential scan found 0 hits in w1. The frozen candidate's selftest fake token (line 164) hits the `credential` shape; it is not a capture path, and the landed instrument carries the same fixture.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `trail-ids.txt` (mtime 2026-11-06 20:36, before this round, 1 byte). It is not written by a kasegi r90 seat and was left untouched.
- Inherited state: none (lane clean at start, no `lane-dead-no-report kasegi round=90`).
- Open L0 questions: unchanged (`kasegi | round-77`, `kasegi | round-89`); none added.
- Tool installs: none.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
