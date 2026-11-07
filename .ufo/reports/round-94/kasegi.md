# kasegi — round 94 (attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (branch `master`).
Base `dff5a0a01e8aafe6be81f4ee61567745c3c4c485`; lane tip at filing `64bb47d39e3340cd90b80a1f74ec18f0a723b5e4`.
Driver digest: `.ufo/state/inline-dispatcher.log` `2026-11-07T13:06:07 spawned kasegi 94 w1 13`; WAVE-DONE received
(all 13 seats settled).
**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

## Work performed

The round declares **two claims** (frozen in `.ufo/waves/round-94/claims.json`, freeze `96b5033f`):

- **C1 — `depth:verifiability` (the lane's lowest non-retired axis, score 4).** Citation-anchor tranche 9: the 19
  token-level repoints the round-94 non-author label set names, in `corpus/knowledge/triage-thresholds.md` and
  `corpus/knowledge/considerthese-proposals-ledger.md`, applied under a successor counter that walks every labelled
  file (including one outside `corpus/knowledge`), binds lane-root tokens embedded anywhere in a written value
  (including a `cell-repair` replacement) and prints the measured revision. Ten label rows that ask for a prose
  reword are frozen as `EXCLUDED` with a reason each. Measured knowledge meter 1008/1999 → 1009/2000.
- **C2 — `coverage` (score 8 held; capability extension `capture-secret-scan`).** Three GitLab edge classes from
  GitLab's own machine-readable rules file (S140): the personal-access-token optional custom instance prefix
  (`acme-glpat-…`), the runner authentication token (`glrt-`/`glrtr-`, optional `t1_`/`t2_`/`t3_`) and the deploy
  token (`gldt-`); the round-93 `glrt-` known limit is retired; every planted path and basename is relocated at run
  time; a previous-landing regression limb (K9) is added.

Work items (each with its evidence pointer):

- **Freeze** `96b5033f` — claims, the C1 counter/map/labels, the C2 counter/candidate scanner/candidate row,
  the executed controls (C1 12/12, C2 10/10), the S140 capture + manifest, and the S140/S141 SOURCES rows:
  `.ufo/waves/round-94/`, `.ufo/waves/round-94/controls/`, `corpus/source-snapshots/round-94/`,
  `corpus/SOURCES.md:152`/`:335-336`.
- **C1 landing** `d51220ae` — 19 map rows applied to 18 lines of two knowledge files
  (`git diff-tree --no-commit-id --name-only -r d51220ae` = exactly those two paths); counter run
  `.ufo/waves/round-94/l1/c1-landing-r94.txt` (M0–M10 pass, `after_rev=d51220ae…`).
- **C2 landing** `99646086` — the landed scanner (`sha256 22ba32d1…beaf`) and the capability row
  (`sha256 4f10e273…eed8`, byte-equal to the frozen candidate row); counter run at three seeds
  `.ufo/waves/round-94/l1/c2-landing-r94.txt` (K1–K9 pass, `scanned=2224 hits=0 unused_allow=0`).
- **Wave w1** — one v1 wave of **13 seats** (dispatch `.ufo/waves/round-94/w1-dispatch.json`, ready
  `.ufo/waves/round-94/w1.ready`, results `.ufo/waves/round-94/w1-results.json`): 3 critics, 2 reviewers,
  2 mutation-testers, 1 sentinel (attack share 8/13 = 61.5 %), 1 connector, 1 scout, 2 executors, 1 scribe;
  **no dead seat**, no residual call, round total 13. Seat reports and receipts in `.ufo/waves/round-94/w1/`.
- **Harm repair** `b3548106` — the C2 landing grew the scanner 458 → 491 lines and mis-pointed 65 of 102
  full-path citations across five entries (CriticHarm's named harm). Every `capture-secret-scan.py:N[-M]` token
  re-anchored from the base→tip content map: 68 tokens + 1 hand-disposition row; the seat's 35-pair drift table
  reconciles 35/35; `anchorcheck.py` 0 bad on all five. Receipt `.ufo/waves/round-94/l1/reanchor-r94.txt`,
  map tool `.ufo/waves/round-94/l1/reanchor-r94.py`.
- **Integration** `b3548106` — `corpus/lessons/round-94.md` (Gate S140/S141, Mistakes M94-1..4, wave findings),
  `LOG.md` round-94 entry, `SCORECARD.md` round-94 section + planned 95, `corpus/QUALITY.md` R146/R147,
  S140 `queued` → `mined` (+ used-by), S141 landed as `rejected`.
- **R145 repair** — the round-93 routed defect 6 (no committed enumerator for R145's 39-row claim) is closed by
  `.ufo/waves/round-94/controls/r145-enumerate-r94.py` + `.txt` (`R145-ENUMERATE pass parse_a=32 parse_b=44`) and
  QUALITY R147 supersedes R145's count only.
- **Evidence redaction** `86fb7e6f` — the wave-evidence commit `5a43f2bc` carried 18 scanner-shaped fixture lines
  across 14 seat receipts; 159 matched values replaced by shape markers, per-line digests in
  `.ufo/waves/round-94/l1/redaction-r94.txt`; the tip scans `hits=0 allowed=24 unused_allow=0 rc=0`.
- **Misroot sweep** — `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only other lanes'
  `.scratch/*` (orchestrator-owned), `f.txt` and `trail-ids.txt` (predate the wave, content names no
  kasegi/94 path); no seat wrote outside the lane. Scratch removed (`/fast/scratch/hyaku/kasegi-r94`, 5.6 GB).

## Landed changes

Every change below is tied to a `LOG.md` bullet in the round-94 entry (or the appended round-94 correction) and to
the commit that carries it.

| Commit | What it carries | LOG tie |
|---|---|---|
| `96b5033f` | freeze: claims, C1 counter/map/labels, C2 counter/candidate scanner/row, executed controls, S140 capture + manifest, SOURCES rows S140/S141 | round-94 bullet 1 (Read first … freeze) |
| `d51220ae` | C1 landing: `corpus/knowledge/triage-thresholds.md`, `considerthese-proposals-ledger.md` | bullet 2 (C1 landing) |
| `99646086` | C2 landing: `corpus/instruments/capture-secret-scan.py`, `SCORECARD.md` capability row | bullet 3 (C2 landing) |
| `5a43f2bc` | wave w1 evidence: spec, dispatch, ready, results, 13 seat reports/receipts, landing receipts, re-anchor receipts, end census | bullet 4 (Wave w1) |
| `b3548106` | integration: lesson, LOG, SCORECARD round 94 + planned 95, QUALITY R146/R147, S140 mined, S141 rejected, five re-anchored entries | bullets 5 (Integration) and the `Sources`/`Mistakes` bullets |
| `86fb7e6f` | wave-evidence redaction (159 fixture values, 14 receipts) | round-94 correction (appended) |
| `64bb47d3` | LOG correction (the redaction record) | round-94 correction |

## Before → after measurements

Each claim with its counting command and the commit it was measured against; the verdicts are the frozen kill
rules' verdicts, not a re-reading.

### C1 — `depth:verifiability` → **NOT VERIFIED on P4** (P1–P3 substance verified)

Command (frozen):

```
python3 -B .ufo/waves/round-94/c1/knowledge-meter.py --lane <lane> \
  --base-rev dff5a0a01e8aafe6be81f4ee61567745c3c4c485 --after-rev d51220aeb4a538b7b211bb2629e83210669cd56d \
  --map .ufo/waves/round-94/c1/repair-map.tsv --labels-rev 96b5033f4dfa8d6605c13e0c9aad458be3cd7df3 \
  --base-target 1008/1999 --target 1009/2000 \
  --map-sha256 11de45a74337b945b5179645e18e0f710a2f9ec54935450806a0e4bda7a78847
```

- **Before:** 1008/1999 at `dff5a0a` (base); 19 repoints unapplied; the M3 union crashed on a labelled
  non-knowledge file and M5 ignored a lane-root token inside a cell replacement.
- **After:** 1009/2000 at `d51220ae`; M0, M1, M3–M6, M9 (`rows=19`), M10 (`labelled=29 want=19 mapped=19
  kinds=excluded=10,range=19`) pass; `after_rev=d51220ae…`; P3 names exactly the two knowledge files; the ten
  `EXCLUDED` rows are unmapped and byte-unchanged. Evidence: `.ufo/waves/round-94/l1/c1-landing-r94.txt`.
- **Verdict: NOT VERIFIED.** P1, P2 and P3 stand (re-derived by CriticClaimsC1, ExecC1Indep, MutC1Counter,
  ReviewC1Labels), but **P4 does not reproduce**: the frozen before-fixture in the controls driver clones the
  mutable live lane instead of pinning `dff5a0a`, so after the tranche landed the
  `m5-cell-repair-before-r93` reception flips to `rc=1 want=0`, and the receipt's `candidate=e7adac6…` is a scratch
  commit that is not an object in the repo. Under the frozen kill rule (`P4 not reproducing: C1 NOT VERIFIED`),
  C1 is not verified. The critic's one-line pin restores `C1-CONTROLS-RESULT pass controls=12`; the fix is routed
  to round 95. `.ufo/waves/round-94/w1/CriticClaimsC1.md`.
- **Qualifiers (not re-scores):** ReviewC1Labels: 18/19 landed rows CORRECT, 1 PARTIAL (row 151, routed), 0 WRONG;
  9/10 exclusions right (row 396 is token-fixable in substance); two round-95 labels written. MutC1Counter: 17/17
  mutants killed, 0 survivors, seven invisible to the frozen suite (routed coverage gaps).

### C2 — `coverage` (score 8 held; capability extension) → **NOT VERIFIED on P4 as written** (P1–P3 verified)

Command (frozen):

```
python3 -B .ufo/waves/round-94/c2/capability-check.py --lane <lane> --rev 996460861d4130ddb2da6b7554e905d3e47504a3 \
  --work <scratch> --instrument-sha256 22ba32d145f90f7759caf16d3ee524eb1779153d3f2a33611675a93a4667beaf \
  --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6 [--seed N]
```

- **Before:** no GitLab custom instance prefix, no runner-auth or deploy shape; plants keyed on path shape
  (round-93 M93-4); no previous-landing limb.
- **After:** the three shapes at `99646086` (S140 lines 4/114/255), the `glrt-` limit retired, plants relocated,
  K9 added; K1–K9 pass at seeds 4242, 1 and 9191 (`scanned=2224 hits=0 allowed=24 unused_allow=0`); P2 the landed
  scanner and gate equal the pins; P3 the landing changes exactly the scanner + the SCORECARD row (row
  byte-equal to the frozen candidate). Evidence: `.ufo/waves/round-94/l1/c2-landing-r94.txt`.
- **Verdict: NOT VERIFIED on P4 as written.** P4 names a tenth control, `the S140-allowlist-removed control`, that
  does not exist in the frozen driver (the redaction made such a control vacuous) and is absent from the receipt,
  whose tenth control is `tampered-instrument`. Two independent seats (CriticClaimsC2, ReviewC2Scanner) read the
  same mismatch; both re-derived P1–P3 as standing. The frozen claim is **not** re-worded; the correction is
  recorded here and in `SCORECARD.md` and queued for the next freeze. `.ufo/waves/round-94/w1/CriticClaimsC2.md`.
- **Qualifiers (not re-scores):** MutC2Counter: 6/7 forgeries killed, one SURVIVOR (a scanner that drops the
  unplanted `session-cookie` gate shape) routed; SentinelShapes: 52 encoding and 32 boundary fixtures as stated,
  three defects (two S140 vendor classes neither detected nor named; an allowlist gap for a prefixed token in an
  escaped context; two provenance/limit sentences) and four qualifiers routed; ReviewC2Scanner: eight qualifiers.
- **Tip reading (integration):** the C2 counter passes at the final tip `86fb7e6f` as well (K1–K9, `scanned=2476
  hits=0 unused_allow=0`), after the evidence redaction.

### Cross-cutting measurements

- **C1 meter at the integration tip** (`b3548106`): 1007/1998 (down 2 from the C1 landing). The re-anchor replaced
  the drifted token strings `:120-128`/`:1-151` with `:120-121`/`:1-152`, two values that already exist elsewhere,
  so the distinct-token count falls by two while 65 mis-pointed citations become correct. Disclosed, not claimed.
- **Density:** `python3 corpus/instruments/density.py SKILL.md --label r94` = **273.2**, unchanged
  (`git diff --stat dff5a0a <tip> -- SKILL.md` empty).

## Sources & frontier

Census command (both runs, rc 0):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

- **Before:** 139 rows, rc 0, six inherited W04 duplicate-URL warnings
  (`.ufo/waves/round-94/controls/census-start-r94.txt`, run over a scratch export of the base corpus).
- **After:** 141 rows, rc 0, the same six W04 warnings (`.ufo/waves/round-94/l1/census-end-r94.txt`).
- **Rows added by tier:** tier A — S140 (GitLab's own `rules/mit/gitlab/gitlab.toml` at commit 59ada1f4; the
  source of the three shapes, admitted, captured, `queued` → `mined`, used-by
  `corpus/instruments/capture-secret-scan.py`); tier B — S141 (the same repository's `github.toml`; opened,
  rejected: its `ghr_` 76 rule is a round-95 lead and GitLab is not the vendor of GitHub tokens).
- **Rows touched old→new:** S140 `queued` → `mined`, used-by `—` → the instrument (freeze → integration); S141 added
  `rejected` (no later change). No other row's status, recheck or used-by cell changed.
- **Frontier rows advanced:** none. The round extends an owned capability and the citation-verifiability
  instrument; `PROVINCE.md`/`corpus/README.md` frontier rows are untouched.
- **Redaction:** the S140 capture is the fetched text with the 82 `examples`/`negativeExamples` element lines
  replaced by one fixed marker (line numbering preserved; `.ufo/waves/round-94/controls/redaction-r94.txt`); the
  intake gate refused the unredacted bytes (`.ufo/waves/round-94/controls/capture-intake-r94.txt`), and
  `source-recheck.py` re-derives the three regex anchors (rc 0). Two freeze commits were refused by GitHub push
  protection (GH013) for the ruleset's published example values; both were unpushed local commits abandoned by the
  lane, and no remote history was rewritten (L0 line `kasegi | round-94`).
- **Assimilation:** none adopted (`merge/kasegi` ids collide with the lane registry by construction; adoption waits
  for a later round). **considerthese:** not mined this round — the two claims were frozen before the proposal list
  could be screened without widening them; routed to round 95.

## Trend verdicts

- **expansion: improved** — registry 139 → 141 (S140 admitted/mined; S141 rejected) and `capture-secret-scan`
  extended with three first-party-sourced shapes (S140 lines 4/114/255). Basis: registry + capability, not a new
  `knowledge/` entry; `PROVINCE.md` and the coverage map are unchanged, so this is the registry-and-repertoire
  form of the trend.
- **quality: improved (with one disclosed harm, repaired in-round)** — the scanner's known-limits text now names
  the remaining GitLab families; the 65 mis-pointed citations across five entries were repaired to 0 bad
  (`anchorcheck.py`), with the one row inside the rewritten block hand-dispositioned; R146 (structural redaction)
  and R147 (R145's count superseded with a committed enumerator) enter. The C2 landing *created* a citation harm
  that the integration repaired; it is disclosed, not hidden, and the entries end correct.
- **discernment: improved** — the wave's independent seats falsified two of the round's own predicate readings
  (C1 P4's reproduction; C2 P4's misnamed control), named the citation harm with numbers, and each finding was
  recorded as a lesson row (M94-1..4) and, where a rule was missing, a criterion (R146/R147). No disagreement was
  left unlearned.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `corpus/lessons/round-47-verifier-spotcheck.md` (non-author; boxes 1, 3 and 4 checkable from outside).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `corpus/practice/curl-h1-1913733/report.md`
  (round 85) and `corpus/practice/curl-ibb-h1-1997312/report.md` (round 86), both logged in LOG.md.
- [~] Instructions executable by an agent without oral context — pointer: `corpus/lessons/round-47-verifier-spotcheck.md`
  (declared-root recheck observations).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` (scope unchanged; live-target
  testing remains refused).

## Round shape, dispatch and tooling

- One v1 wave (`kasegi-r94-w1`, policy `scripts/hyaku/ufo-wave-policy.json`, band 8–16), **13 seats**, spawn 13 /
  resume 0 / total 13; 0 dead seats; no residual `task` call; round total 13. Roles: 3 critics, 2 reviewers,
  2 mutation-testers, 1 sentinel, 1 connector, 1 scout, 2 executors, 1 scribe. The planner seat is the L1's
  (the validator rejects `planner`); no seat spawned a sub-swarm.
- **Tool installs / upgrades:** none this round (lane and seats used present tools only).
- **Open L0:** `kasegi | round-94` (the GH013 blocked-commit handling and the source-policy question); the
  round-93 push-protection question remains open. The round routed around both.
- **Corrections:** the seat brief's "18 redacted line numbers" is wrong — the artifact has **82** redacted lines
  across 24 rules (ScoutGitLabRules, three ways); the report uses 82.
