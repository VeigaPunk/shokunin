# kasegi — round 23 report (attempt 2)

Lane: `kasegi-shokunin`. Pushed lane hash: **`f6966d4dd25b29687d1d1f831417e9b8d1900760`** (helper `landed`; measured bytes — the lane tip
later advanced to `5842ef72a545477d6f9729d7a986d62c7c370486` only by amended seat reports).
Base `922a4dde90b60b465e2b8b241d1fe363f1f27e98`; lane tip at attempt start
`1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` (inherited checkpoint `8bf9807`,
"policy-paused, unadmitted, no task resumption"). Frozen claims unchanged from
`.ufo/waves/round-23/claims.json`.
Stale-lane: no — respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims (2, frozen before data):
**C1 `depth:verifiability`** (lowest axis, score 4) — make `MIRROR-EQUIVALENT`
sound: bounty-prefixed and relative mirror fallbacks must not credit parent
traversal or symlink escapes outside the selected mirror, and sibling-root prefix
confusion must be rejected, preserving valid confined and missing-file controls.
**C2 `coverage`** (score 7) — admit F06 FIRST multi-party CVD, F07 the *current*
CNA operational rules and F08 CRA manufacturer reporting duties, 0/3 → 3/3, with
located quotes and executable local rechecks.

- **C1 fix.** `corpus/instruments/resolve.py`: new `bounty_suffix()` (exact-root
  equality or `/`-delimited descendant, so `~/Projects/bounties-x` is an ordinary
  other root) plus `under_mirror(realpath)` on both the bounty and relative mirror
  fallbacks (`resolve.py:194-260`). The literal bounty hit and the lane-relative
  `INTERNAL` branch are named carve-outs, not silently changed.
- **C1 counter.** New `corpus/instruments/mirror-containment-fixtures.json` (24
  cases: 12 escape, 12 control) replayed by new
  `corpus/instruments/mirror-containment-check.py` on real copied CLI bytes — one
  isolated `HOME`/`KASEGI_MIRROR`/lane tree per case, reading the CLI's own
  `citation-survival.tsv` and asserting both `class` and `resolved_path`.
  Receipts: `.ufo/waves/round-23/c1-fixed.json`, `c1-baseline.json`, control bytes
  `c1-baseline-resolver.py`.
- **C1 no-harm guard.** Frozen `git archive 922a4dd` export through both detectors:
  identical summaries (`distinct=1589 resolves=11 mirror=0 internal=197 gone=1381
  skill=39/513 corpus=192/1262 all=208/1589`) and `changed=0 added=0 dropped=0`.
  `mirror=0` because no mirror candidate exists on this host — published as
  vacuity; the matrix, not this diff, is the evidence.
- **C2 landed.** `corpus/source-snapshots/round-23/manifest.json` (four sources, 33
  quote assertions), snapshots `S018.txt`/`S029.txt`/`S030.txt`/`S031.txt` (new:
  normalized `pdftotext` capture of CNA Rules 4.2.6, 49154 B), the three entries,
  and `corpus/README.md` § Frontier F06–F08 `queued → admitted` (`README.md:200-202`)
  plus appended Coverage-map rows.
- **C2 correction found by the wave and landed.** F07's "current CNA rules" was
  **already superseded on the date it was opened**: v4.2.6 was approved 2026-10-14,
  effective 2026-10-20, replacing v4.2.0, and §4.2.11 changed **SHOULD → MUST**.
  New row **S031** + snapshot + 10 assertions; the entry was rewritten with
  rule-number locations only (no page claims), 4.2.0/4.1.0 kept as history.
  Confirmed by `falsify/CnaVersionDate.md` and `falsify/Q2TierSupport.md`; the
  inherited `build/CnaFix.md` had found it on 2026-10-20 and no corpus file
  disclosed it (lesson M13).
- **Wave-attacked repairs landed.** Fixture-name confinement in the checker (a
  doctored matrix had unlinked a host file), `resolved_path` assertion,
  process-group timeout, per-case containment, bounded stored output, checker sha +
  UTC stamp in the receipt; two cases added because mutation seats proved the
  earlier matrix could not see lane-first ordering or a mirror-root prefix sibling
  (`falsify/MutateRelConfine.md`); the bare-glob escape case replaced by the
  discriminating hop form (`falsify/AbsFormProbe.md` F1); every `recheck:` line made
  cwd-independent (`falsify/RecheckAsWritten.md`); `source-recheck.py` now applies a
  declared normalization (`normalized=markup-whitespace`), implementing
  `considerthese/2026-10-24.md` proposal 1; `corpus/QUALITY.md` gains **Q8** and
  **R10**.
- **Frontier counter made field-exact** after `falsify/DenomCount.md` proved the
  `grep` form column-agnostic.
- **Residual debt named**: F01–F05's rechecks exit 2 `not-listed` (no capture for
  S001–S015), reproduced in `falsify/Q7ControlsClaim.md` and recorded in the lesson.
- **Detector liveness findings left as debt, disclosed**: `falsify/BraceGlobProbe.md`
  (first-match brace/glob suppression; empty brace alternative never resolves) —
  pre-existing on both byte sets, outside the frozen predicate, not repaired.

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `953c2788` | C1 fix + matrix checker + fixtures + receipts; C2 manifest, F06–F08 entries, Frontier admission; SCORECARD r23 section; lesson attempt-2 section; wave-2 spec/registry | LOG "round 23: detector soundness + F06–F08 admission (attempt 2)" |
| `2712c992` | post-attack repairs: checker hardening, 23-case matrix, F07→S031, recheck `cd` prefixes, README coverage/provenance, S030/S031/S029 assertions, lessons M12–M18 | LOG (same entry, "after the falsify wave") |
| `4d9231e7` | log the post-attack repairs and final measurements | LOG |
| `12edac47` | seal: ordering/prefix pins, declared recheck normalization, Q8/R10, final receipts | LOG "- Final seal" |
| `bf9ce024` | rescue: 24-case matrix (root-name continuation), docstring truth fixes, supplementary Gate rows for S018/S031, corrected census | LOG "- Rescue pass" |
| `f6966d4d` | receipts carry each case's `method`/`domain`, so the baseline→landed routing change (`literal/bounty` → `literal/other`) is visible in the artifact | LOG "- Final seal" addendum |
| `8acb255d` | failing Q7/Q8 control exits recorded beside the clean runs | — |

## Before → after measurements

| Claim | Before | After | Counting command | Measured against |
|---|---|---|---|---|
| C1 | escape **0/12 GONE**; controls 12/12; matrix **12/24**, exit 1 | escape **12/12 GONE**; controls 12/12; matrix **24/24**, exit 0 | `python3 corpus/instruments/mirror-containment-check.py --resolver .ufo/waves/round-23/c1-baseline-resolver.py --json …c1-baseline.json`, then the same without `--resolver` (`--json …c1-fixed.json`); both print `matrix_sha256=d05b1e0c…b809` (`cases=24 escape=12 controls=12`) | before: `922a4dd` resolver bytes (`d6a3c3f1…f903`); after: `f6966d4` tree (`690153ad…ea2d`) |
| C1 guard | — | `changed=0 added=0 dropped=0`; `mirror=0` (vacuous, disclosed) | export `git archive 922a4dd`, run both resolvers, diff `citation→class` | before: `922a4dd`; after: landed bytes |
| C2 | F06–F08 admitted **0/3**; frontier **5/8**; rechecks exit 2 (manifest absent) | **3/3** admitted; frontier **8/8**; four rechecks exit 0, three failing controls exit 1/2/1 | `awk -F'|' '$2 ~ /^ *F0[6-8] / && $4 ~ /^ *admitted *$/ {n++} END{print n+0}' corpus/README.md` → 0 → **3**; F01–F08 variant → 5 → **8**; the four `recheck:` lines run from `/tmp` → exit 0 (`S018` 7 OK, `S029` 10 OK, `S030` 11 OK, `S031` 11 OK) | before: `922a4dd`; after: `8acb255d` |

The do-nothing control is the `922a4dd` resolver on the same 24-case matrix: 0/12
on the escape target, so the counter cannot be met by skipping the fix (§8 control
receipt committed). The escape set grew from 6 to 12 during the round because the
falsify wave found unpinned spellings; every added case discriminates on the same
receipts (baseline FAIL / fixed PASS), reproduced independently by
`falsify/MutateRelConfine.md`, `falsify/MutateBountyConfine.md`,
`falsify/MutateBoundary.md`, `falsify/AbsFormProbe.md` and `falsify/BraceGlobProbe.md`.

## Sources & frontier

SOURCES rows **27 → 31**: added S028 (rejected duplicate proposal), S029 (CRA
reporting clocks), S030 (CNA 4.2.0), **S031** (CNA 4.2.6, current). Tiers A=29,
C=2; status mined 19, queued 9, rejected 3; 19 rows carry `used-by`. Counting
command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (27 on
`git show 922a4dd:corpus/SOURCES.md`, 31 now) plus a cell census of
tier/status/used-by. Rows touched old→new (logged in `corpus/lessons/round-23.md`
§ Gate): S018 `status queued→mined`, `used-by —→multiparty-vulnerability-coordination.md`;
S029/S030/S031 are new rows whose `teaches` cell opens `supersedes S0xx —`; S022 and
S024 stay byte-identical and `queued`. Frontier rows advanced: **F06, F07, F08**
(`5/8 → 8/8` admitted, entries linked).

Census, opening (registry untouched; attempt start), exact output:
```
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
census rc=0
```
Census, round end (same two warnings, now 31 rows), exact output:
```
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
census rc=0
```
Command both times: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.

**Assimilation: none.** No `merge/kasegi/` entry was adopted this round: the claims
were frozen before the 2026-10-24 directive landed, and the row budget went to
re-grounding F07 against the current rule set. `considerthese/` was mined: one
still-unimplemented proposal (`2026-10-24.md` proposal 1, "make the rechecker
normalize and pin, not just substring-match") landed as `QUALITY.md` **Q8** plus the
`normalized=markup-whitespace` path in `source-recheck.py`.

## Trend verdicts

- **expansion — improved.** Three frontier topics admitted (5/8 → 8/8), a fourth
  pinned source added (S031), and a capability acquisition (replayable matrix +
  pinned-quote recheck pair, exercised with before/after and failing controls).
  Evidence: `corpus/README.md:200-202`, `corpus/SOURCES.md` rows 34-37,
  `SCORECARD.md` § Capabilities.
- **quality — improved.** Ten instrument and record defects found by the wave were
  repaired before the seal, each with a reproduction (checker host-write, path-blind
  verdict, non-unique quote, superseded "current" source, column-agnostic counter,
  cwd-dependent rechecks, unpinned spellings). Evidence:
  `corpus/lessons/round-23.md` § Post-attack repairs and M12–M18.
- **discernment — improved.** The lane rejected its own first landing's F07 on a
  machine check instead of trusting the inherited draft, declined to widen the
  frozen predicate to cover the literal carve-out, and reverted an unpinned semantic
  change to bare-root bounty citations that no receipt would have certified.
  Evidence: `falsify/LiteralCarveout.md`, `falsify/InheritedReuse.md`, lesson M9/M17.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md`; `python3 corpus/instruments/density.py SKILL.md` (r15 record 152.9); untouched this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` round-23 entries plus lane commit `f6966d4d`.
- [~] Instructions executable by an agent without oral context — pointer: `mirror-containment-check.py --help`, the four cwd-independent `recheck:` headers, `c2-recheck-S0xx.txt` receipts.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` unchanged; `falsify/SiblingOverlap.md` found 0/60 phrase hits across five sibling corpora.

No box is `[x]`: no named non-author verifier has judged this round yet.

## Round shape, waves and seats

- **Shape: two v1 waves (default).** Wave 1 inherited from the same round's earlier
  attempt — `kasegi-r23-build`, **64 seats**, committed registry
  `.ufo/waves/round-23/build/swarm-registry.json`, 44 seat reports; role mix
  reviewer 19, scout 16, critic 8, scribe 6, connector 4, revenger 4, sentinel 4,
  executor 3. It satisfies the §3 L2 floor; the L1 holds the canonical planner seat,
  and the bounded planning walk rode `falsify/ClaimsIntegrity.md` and
  `falsify/InheritedReuse.md`.
- **Wave 2 (fresh): `kasegi-r23-falsify`, 36 seats** — critic 9, reviewer 7,
  executor 7, scout 4, mutation-tester 3, sentinel 2, revenger 2, connector 1,
  scribe 1; attack roles 19/36 = 53 %. Validated under
  `scripts/hyaku/ufo-wave-policy.json` (band 32–64): `plan`/`run` exit 0, registry
  `.ufo/waves/round-23/falsify/swarm-registry.json`, spec
  `.ufo/waves/round-23/falsify-spec.json`.
- **Refusals.** Dispatch attempt 1 refused at the host job limit —
  `Failed to start background task jobs: … Background job limit reached (100)` on all
  36 lanes, filed at `.ufo/waves/round-23/falsify/refusal-1.json`. The identical
  payload was resent once after the host freed capacity and was accepted. No wave was
  split, shrunk or padded.
- **Dead seats: none.** 36 of 36 wave-2 reports exist under
  `.ufo/waves/round-23/falsify/` (`LessonGateRows` landed last). Round total
  **64 + 36 = 100 seats**, inside the 32–128 band.
- **Routing.** Every seat routed through the host role map; no `model` passed.
  **Tool installs: none** — `curl`, poppler `pdftotext`, `python3` were already
  installed; the pacman pause was respected.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists
  33 entries; none kasegi-authored (`grep -i kasegi` on every untracked fleet-root
  file → 0 hits; `.ufo/waves/round-35/` belongs to mado's round). Nothing copied or
  deleted; no misroot mistake.
- **Open L0 questions: none.** F01–F05's capture debt needs fifteen public
  snapshots, not an operator decision.
