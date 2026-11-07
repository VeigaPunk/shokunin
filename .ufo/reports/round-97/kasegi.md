# kasegi — round 97 (attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (branch `master`).
Base `b06af5e07efbd961a8449f7de6b57eeea62c6bd3`; freeze
`daf7fc6a627d615178c27594110e956e592e4cd9`; C1 landing
`75a471809cba265c8981ece1c0ed29c7895d9308`; C2 landing
`a9a53608dce6aea07d298bb9d5133532078eb1dd`; integration `369758f3`; wave
evidence `b4bb939a`; final lane tip `a7416b18723d4d6e7143205ed53ca5eaf1eb3cbe`
(`git ls-remote origin refs/heads/master` prints the same hash).

## Work performed

Two declared claims:

- **C1 — depth:verifiability (lowest non-retired axis, score 4 held):** tranche 12
  qualifies 33 bare lane-instrument basenames to their tracked
  `corpus/instruments/` paths in sixteen `corpus/knowledge/*.md` files (nine
  distinct tokens: `resolve.py`, `anchorcheck.py`, `capture-source.py`,
  `source-recheck.py`, `density.py`, `capture-secret-scan.py`,
  `claim-package-check.py`, `r35-defect-closure.sh`, `r36-closure.sh`). The
  round-97 counter adds the `qualify-lane` label kind (value must be tracked,
  non-`.ufo`, INTERNAL; key must be a bare basename; edit is exactly
  `key` -> `label`). Meter 1040/2041 -> 1043/2035: nine bare GONE tokens leave
  the scope (-9 denominator), three qualified paths are new (+3 numerator, +3
  denominator) and six qualified paths already existed (numerator unchanged);
  net +3/-6.
- **C2 — coverage (score 8 held), capability extension `capture-secret-scan`:**
  the ten remaining GitLab families the round-96 known-limits list named
  (runner registration `GR1348941`+20, `feed_token=`+20, `gloas-`+64,
  `glft-`+20, plain `glagent-` 50, `glimt-` 20-25 lower-case,
  `glsoat-`+20, the `gitlab+deploy-token-<N>:<token>@` URL form, `glffct-`+20,
  `glrct-`+20; S140 lines 101/160/174/190/213/229/278/341/392/412). Selftest
  128 -> 148. The landing also repairs the round-96 spot-check's routed K2
  defect: 181 credential-shaped fixture literals across 43 wave receipts are
  redacted structurally.

Work items (evidence pointers):

- C1 counter, labels, map, generator, harness and its executed receipt:
  `.ufo/waves/round-97/c1/`, `.ufo/waves/round-97/controls/`.
- C1 pre-freeze candidate receipt `.ufo/waves/round-97/l1/c1-candidate-r97.txt`
  (1040/2041 -> 1043/2035 at the scratch candidate `f410e91f`); landing receipt
  `.ufo/waves/round-97/l1/c1-landing-r97.txt` (pass at `75a47180`, plus the
  `--measure-rev` cross-check 1043/2035); post-landing control re-run
  `.ufo/waves/round-97/l1/c1-controls-postlanding-r97.txt` (14/14,
  `ATTRIBUTION pass fixtures=13`); P3 path-set receipt
  `.ufo/waves/round-97/l1/c1-p3-r97.txt` (16 files, SKILL.md untouched, 30/30
  lines).
- C2 capability gate, candidate scanner, pre-freeze K1-K6 pass
  `.ufo/waves/round-97/l1/c2-candidate-r97.txt` (candidate `659e320f`, seed
  4242) and landing pass `.ufo/waves/round-97/l1/c2-landing-r97.txt` (landing
  `a9a53608`, seed 20261107).
- Redaction: `.ufo/waves/round-97/l1/redaction-r97.txt` (43 files, 181 values,
  before/after digests) and the tool `.ufo/waves/round-97/l1/redact-r97.py`;
  the wave-evidence redaction is `.ufo/waves/round-97/l1/redaction-r97-w1.txt`
  (30 values in the receipts + 30 in the `ExecC2Probe` report).
- Sources: S146 capture `corpus/source-snapshots/round-97/S146.txt` + manifest;
  S147 reject sweep `.ufo/waves/round-97/l1/s147-reject-r97.txt`; S140 re-open
  receipt `.ufo/waves/round-97/l1/s140-live-fetch-r97.txt` and
  `.ufo/waves/round-97/l1/s140-capture-lines-r97.txt`.
- Harm checks `.ufo/waves/round-97/l1/harm-r97.txt`: SKILL.md / PROVINCE.md /
  SHONEN.md / AGENTS.md / allowlist byte-identical base->tip; anchorcheck over
  106 knowledge files prints 1206 in-range / 8 bad, the same 8 bad as the base
  (105 files, 1206 / 8).
- Assimilation: none adopted; the id-collision check runs this round
  (`.ufo/waves/round-97/assimilation/`, 94/94 staged ids collide) and the
  indented-row guard is proven (`guard-receipt.txt`, verdict PASS).
- Push incident: the first two wave-evidence commits were refused by GitHub push
  protection (GH013) on the synthetic GitLab fixture bytes in
  `ExecC2Probe-receipts/fixture-bytes.txt` and then in `ExecC2Probe.md`; both
  unpushed blocked commits were abandoned (the round-94 precedent), `master`
  restored, the evidence redacted, and the wave evidence landed at `b4bb939a`.
  Recorded as M97-7.

## Landed changes

| change | commit | LOG entry |
|---|---|---|
| freeze: claims, counter, labels, map, generator, harness + receipt, gate, candidate scanner, receipts | `daf7fc6a` | Round 97 bullet |
| redaction of 181 fixture literals across 43 wave receipts | `b3c2aff9` | Round 97 bullet |
| C1 landing: 33 qualify-lane edits in 16 knowledge files | `75a47180` | Round 97 bullet |
| C2 landing: ten GitLab shapes, selftest 128 -> 148, SCORECARD row | `a9a53608` | Round 97 bullet |
| integration: entry, SOURCES 145 -> 147, QUALITY R153/R154, lesson, SCORECARD, LOG, assimilation receipts | `369758f3` | Round 97 bullet |
| wave evidence: spec, dispatch, ready, results (14/14), 14 seat reports and receipts (redacted) | `b4bb939a` | Round 97 bullet |
| integration addendum: wave counts, MutC1Counter finding, GH013 incident | `a7416b18` | Round 97 bullet |

Every change is tied to the Round 97 `LOG.md` entry (`LOG.md:3095-3115`).

## Before -> after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-97/c1/knowledge-meter.py --lane . --base-rev b06af5e0… --after-rev 75a47180… --map .ufo/waves/round-97/c1/repair-map.tsv --labels-rev daf7fc6a… --base-target 1040/2041 --target 1043/2035 --map-sha256 f4ed7387…` | 1040/2041 | 1043/2035 (M0-M10 pass) | `75a47180` |
| C2 | `python3 -B .ufo/waves/round-97/c2/capability-check.py --lane . --rev a9a53608… --work <scratch> --instrument-sha256 59909fc4… --gate-sha256 8b6f8493…` | selftest 128, 0 of the ten shapes, 56 clean-run hits in the wave receipts | selftest 148, K1-K6 pass (K2 `hits=0 allowed=27 unused_allow=0`) | `a9a53608` |

Do-nothing controls (committed in the freeze): C1 `after = base` prints
`M1 after=1040/2041` and `M3 bad_lines=33` (rc 1), and the round-96 counter
cannot express the `qualify-lane` rows (`M4/M5/M9/M10 FAIL`); C2's round-96
instrument at the same revision fails K1 (`cases=128`) and K4 (0 of ten).

## Sources & frontier

SOURCES.md rows before -> after: 145 -> 147. Counting command:
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.
Rows added: S146 (docs, tier A, `mined` — GitLab Docs Deploy tokens, the default
`gitlab+deploy-token-{n}` username and its custom-username limit) and S147
(docs, tier B, `rejected` — the incoming-email page states no `glimt-` prefix or
length; absence sweep in the lesson's Gate).
Rows touched old -> new: S140 re-opened from its committed capture (status
`mined` unchanged; the L1's live `/-/raw/` fetch answered 403).
Frontier rows advanced: none (C2 extends an existing capability on held
ground; no new frontier area is claimed).
Census before -> after: `bash scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kasegi` — before: `kasegi ok` rc 0, 145 rows;
after: `kasegi ok` rc 0, 147 rows; the seven inherited W04 duplicate-URL
warnings (S028, S029, S072, S076, S080, S085, S143) unchanged.

## Trend verdicts

- **expansion: improved** — S146 admitted and mined; a new knowledge entry
  (`corpus/knowledge/gitlab-remaining-token-families.md`, ten shapes with
  per-line S140 quotes and the S146 username limit) on ground the coverage map
  did not hold; the `capture-secret-scan` capability row extended by ten shapes;
  S147 opened and rejected (taste evidence).
- **quality: improved** — ten published shapes with exact-length boundary
  negatives (selftest 148, K1-K6 at two seeds); the lane's own wave evidence
  repaired (181 + 60 credential-shaped literals redacted; allowlist audited to
  25/25 live; the landing scans `hits=0`); QUALITY R153/R154 added from seven
  mined mistakes.
- **discernment: improved** — seven mistakes mined (M97-1..M97-7), three caught
  by the gate's own limbs before the freeze and two by the push gate; S146
  admitted and S147 rejected with an absence sweep; the wave's non-author seats
  re-derived both claims and routed nine defects, all recorded. The non-author
  closure spot-check is pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/lessons/round-47-verifier-spotcheck.md:94` (non-author); SKILL.md byte-identical base->tip this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/practice/curl-h1-1913733/report.md` (round 85) and `corpus/practice/curl-ibb-h1-1997312/report.md` (round 86).
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-47-verifier-spotcheck.md` (Declared-root recheck observations); the new entry's `recheck:` command prints `RECHECK-OK`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-identical base->tip.

## Round shape

One v1 wave (`w1`) of 14 seats: 3 critics, 3 executors, 2 reviewers, 2
mutation-testers, 1 sentinel, 1 scout, 1 connector, 1 scribe (8/14 attack =
57%). Planner seat: the L1 holds it (orchestrator ruling 2026-10-19). Residual
call: none. Round total: 14 seats. All 14 settled, 0 dead
(`.ufo/waves/round-97/w1-results.json`: `seats: 14`, 14 results with non-empty
output).

## Wave findings

Both claims stand on their frozen predicates:

- **C1 STANDS on P1-P3.** CriticClaimsC1 re-derived every limb with its own
  census and map application; ExecC1Indep AGREE (independent meter
  1040/2041 -> 1043/2035, byte-exact map application at all sixteen files, 33
  rows on 30 lines); ReviewC1Sites 33 CORRECT / 0 PARTIAL / 0 WRONG;
  CriticHarm NO HARM; MutC1Counter C1 P2 STANDS (the 14 `CONTROL` lines are
  byte-identical to the frozen receipt) and reports 10 of 17 counter mutants
  surviving, 6 of the 10 named probes.
- **C2 STANDS on K1-K6.** CriticClaimsC2 at three seeds of its own plus an
  88-case boundary audit; ExecC2Probe 10/10 shapes with its own 30 positives and
  30 negatives; ExecC2Counter AGREE on all four items; ReviewC2Scanner APPROVE;
  SentinelShapes C2 STANDS; CriticHarm NO HARM; ScoutSources re-fetched the live
  rules file (HTTP 200, sha256 `14854f71…` = the manifest's raw digest) and
  confirmed all ten regexes byte-identical.

Routed defects (none re-scores a claim; recorded in
`corpus/lessons/round-97.md` § Wave findings): the C1 counter's M4 does not
require `target == "corpus/instruments/" + key` (a wrong-instrument label
passes; fixture `bfdfae1a`); five C2 shapes' right boundary is narrower than
S140 (SentinelShapes MUST-FIX 1, ReviewC2Scanner F2); the C2 gate's K3 plants
are not independent of its selftest, so ten literal-locked patterns pass
(MutC2Counter F01); four further S140 GitLab rules are undetected and unnamed
(ReviewC2Scanner F5); the S140 capture's line numbers are offset from upstream
(ScoutSources); `citation-survival.md` remains unregenerated; the claim-text
qualifiers (surface "12" vs sixteen, the -6 parenthetical, the P4 spec
mismatch); the pre-freeze candidate revs are scratch objects; and the C1
fixture set does not isolate six qualify-lane rules (MutC1Counter survivors).

## Stale-lane

Respawn-per-round driver; this lane has no other open mission. The round ran
from the base `b06af5e` to the landings above inside this dispatch; the wave
settled 14/14 and the lane worktree is clean and pushed. No mission is open
longer than two driver ticks.

## Tool installs

None. pacman transactions stayed paused; no `uv tool`/`npx`/binary install was
needed.

## Open L0 questions

None added this round.

## Erratum (appended after filing)

The round-97 wave evidence gained one late-written seat receipt
(`.ufo/waves/round-97/w1/ConnectorOverlap-receipts/sibling-gitgrep-single-defect.txt`,
984 lines, scan `hits=0`) after this report was filed; it is committed at
`73f8241ac734a794a6b2854f046dfb77cc82a8fc`, which supersedes `a7416b18` as the
lane tip. The cited landings (`daf7fc6a`, `b3c2aff9`, `75a47180`, `a9a53608`,
`369758f3`, `b4bb939a`) are unchanged ancestors of it, and
`git ls-remote origin refs/heads/master` prints `73f8241a`.
