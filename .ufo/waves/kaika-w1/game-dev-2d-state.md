# game-dev-2d — STATE dossier (kaika W1, 2026-10-19)

Lane: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin` (leaf, read-only wave).
Method: static inspection only. The battery was **not executed** — this wave's single
permitted write is this artifact, and battery runs write scratch under `corpus/live/`.
Every "after"/verdict below is quoted from the lane's own committed records, not
re-measured; values from `SCORECARD.md`/`LOG.md` are recorded observations, not
session observations. No web source was needed for a STATE dossier, so `SOURCES.md`
rows = 0 here (wave 2's ART dossiers carry the external rows). No embedded
instructions were found in the read material; repo content was treated as data.

## 0. Bottom line

The lane is substantively real — 104 recorded rounds, 585 executable CASES in 51
families, one demonstrated capability, and r104 shows `improved` on all three owned
axes — but its **learning path is broken at curation**: `corpus/knowledge/` holds two
files (497 words) and none has been touched since r59, while 45 later rounds pushed
falsifiable mechanism facts into `lessons/`, reports, and `LOG.md` only. The formal contract
surfaces (`SKILL.md`, `corpus/QUALITY.md`, `## Gate`, scorecard scores, frontier)
are absent or scaffolded, so a reader cannot derive expertise from the repo alone —
contrary to the depth axis's own definition (AXES.md: "A reader can act on SKILL.md
alone").

## 1. Identity

| item | value | evidence / command |
|---|---|---|
| domain | 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness, on Godot 4.7.2 | `PROVINCE.md:3` (18-word quote) |
| rank | `shonen` (roster), `SHONEN.md` present, **0/4 boxes checked** | `grep -c '^\- \[ \]' SHONEN.md` → 4; `MANIFEST.json` roster `rank: shonen` |
| branch / HEAD | `main`, `e89905162b3a630a599607279681b30572010724` ("round-104 record (work 5f924226)", 2026-10-19 00:04:32 -0300) | `git branch --show-current`; `git log -1 --format='%H %ad %s' --date=iso` |
| working tree | clean; 0 untracked/modified | `git status --porcelain \| wc -l` → 0 |
| last round | **104** — "ROUND 104 (2026-10-19): res_uid lattice + gate tab-PASS tightening + evasion probe + companion adoptions" | `LOG.md:1311`; `SCORECARD.md` §"Round 104 verdict"; work `5f924226` |
| next round | **105** | 104 + 1; r104 routed work explicitly targets r105 (`reports/round-104/r104-adjudicator.md:42,68`) |
| fleet ledger | max lane round **104 confirmed**; closure records `admitted: true` for 101–104 only | MANIFEST `rounds[]` scan: 9 records mention the lane — train 61–64, closure 101–104 + mint record |
| remote | `https://github.com/VeigaPunk/shokunin-godot-2d.git` | `git remote -v` |

**Ledger gaps (verified, not inferred).** MANIFEST has **no closure record for rounds
65–100** for this lane, although `LOG.md`/`SCORECARD.md` record verdicts for most of
them. Record-shape gaps inside the lane:

- 85 distinct `## Round N` headers in `LOG.md` for 104 rounds:
  `grep -oiE '^## (round|ROUND) [0-9]+' LOG.md | grep -oE '[0-9]+' | sort -n | uniq | wc -l` → 85.
  Rounds 79–88 are recorded as lowercase `## round N`/`- ROUND N` blocks; 89–104 as
  `- ROUND N` bullets.
- Round **83 has no report directory and no closure anywhere**; rounds **82 and 84
  each have one scout report only** (`reports/round-82/r82-scout.md`,
  `reports/round-84/r84-scout.md`). The r84/r85 scouts describe 82/83 as "in flight";
  their surfaces were later re-landed as r87 (input) and r91 (navigation), but the
  disposition of 82–84 is never recorded. Command:
  `python3 - <<'PY'` over `reports/round-*` → missing dirs 1–59 (older flat reports)
  and 83; SCORECARD has no §Round for 82–84.
- `SCORECARD.md` has verdict sections for 64–76, 78–81, 85–87, 89–95, 101–104
  (31 sections) and one-row ledger lines for 77, 78, 88, 90–95, 101–104. Rounds
  96–100 have LOG verdicts but no SCORECARD section:
  `grep -oE '^## Round [0-9]+' SCORECARD.md`.

## 2. Axes

Owned axes: **depth, coverage, calibration** (`SCORECARD.md:3`). All three are
**`unscored`**; the scorecard says "Scores remain unassigned without a quality
rubric; a row count is a measurement, not a score or verdict" (`SCORECARD.md:5`,
20 words). `AXES.md` §SCORECARD contract requires "Axis name → score 0–10 +
evidence pointer (measurable moves) **or** `unprovable-but-better` verdict + named
non-author reviewer"; `unscored` is neither. This is the exact question the lane
left in `.ufo/l0-questions.md:32` at its relaunch round-1 ("Please specify a
domain-grade numeric rubric if one is intended") — still unanswered at r104.

| axis | score | SCORECARD evidence pointer (last change) | r104 verdict | staleness |
|---|---|---|---|---|
| depth | unscored | `run_battery.py … --probe-timeout` → 74/74 PASS + `r49-fresh-after-reconnect-non-author.json` | improved | last change r49 → **55 rounds stale** |
| coverage | unscored | same command → named non-author 96/96 PASS, 85 ordinary+meta rows; `r61-crash-non-author.json`; r62 pipe-EOF lesson | improved | last change r61 → 43 rounds stale |
| calibration | unscored | same command → named non-author 81/81 PASS; `r56-pushframe-non-author.json` | improved | last change r56 → 48 rounds stale |

Commands: `sed -n '6,10p' SCORECARD.md`; row counts
`grep -cE '^\| depth \|' SCORECARD.md` = 32 (same for coverage/calibration) — the
32 r64–r104 verdict rows exist, but the axis score/evidence table was never updated
after r61.

**Lowest non-retired axis.** No numeric score exists, so the obligation cannot be
derived as written. Two defensible proxies, both pointing the same way:

1. stalest evidence pointer = **depth** (r49; 55 rounds);
2. the lane's own relaunch note selected **calibration** by an "explicit
   current-evidence-readiness rubric" (`.ufo/l0-questions.md:32`).

Recommendation for r105: either assign scores with re-derivable commands (calibration
move) or land the next claim on **depth** — the axis whose written evidence is oldest.

**Retired axes:** none. The `retired:` field holds a CASES row
(`r95b_order_celloff_y1000`, r101), not an axis (`SCORECARD.md:13`).

**Saturation:** declared at r101 (`SCORECARD.md:355`): an axis is saturated at round R
when R's verdict for it is `unchanged`; stagnation window **N = 5**; lane "not
saturated at r101". The file carries **two** `## Saturation` headings — line 351 is a
placeholder that says the declaration is owed, line 355 declares it:
`grep -n '^## Saturation' SCORECARD.md` → 351, 355. The placeholder is a
self-contradiction left in place.

**Capabilities:** 1 row — `headless production export` (r101), evidence
`corpus/lessons/r101-export-capability.md` + 12 rows PASS ×2. Count:
`grep -cE '^\| headless production export \|' SCORECARD.md` → 1.

**Planned claims:** the `planned:` field is **frozen at r64**:
`grep -c '^planned: r64' SCORECARD.md` → 1. It names r64's while-live gate as the
plan and r65's forged-rejection dual as "Next" — both long since landed. There is no
r105 plan in the scorecard; the only current carry list lives outside it, in
`reports/round-104/r104-adjudicator.md:42` (res_uid harness fix, `s02_deleted`
flakiness, `s01_createid` fixture repair) and the 3D side-round gate
(`reports/round-104/r104-connector.md:200`).

## 3. Corpus

| measure | value | command |
|---|---|---|
| knowledge entries | **2** | `ls corpus/knowledge/*.md \| wc -l` |
| knowledge words | **497** | `wc -w corpus/knowledge/*.md \| tail -1` |
| knowledge last commit | `587561c1` r59, 2026-10-13 10:46 | `git log -1 --format='%h %ad %s' --date=iso -- corpus/knowledge` |
| lessons files | **212** | `ls corpus/lessons \| wc -l` |
| lessons markdown | **75** | `ls corpus/lessons/*.md \| wc -l` |
| lessons JSON receipts | **137** | `ls corpus/lessons/*.json \| wc -l` |
| rounds with a lesson md | **69** of 104 | `ls corpus/lessons/*.md \| sed -E 's#.*/r([0-9]+)-.*#\1#' \| sort -n \| uniq \| wc -l` |
| rounds without a lesson md | **35** | rounds 57–60, 71–100, 102 (loop over 1..104) |
| lesson md carrying `## Gate` | **0 / 75** | `grep -l '^## Gate' corpus/lessons/*.md \| wc -l` |
| knowledge entries with `source:`/`verified-at:`/`recheck:` | **0 / 2** | `grep -cE '^(source\|verified-at\|recheck):' corpus/knowledge/*.md` → 0, 0 |
| fixtures | 110 files (93 `.gd`) | `ls corpus/fixtures \| wc -l`; `ls corpus/fixtures/*.gd \| wc -l` |
| CASES rows | **585** in **51** families | AST count: `python3 -c "import ast;t=ast.parse(open('corpus/fixtures/run_battery.py').read());print([len(n.value.elts) for n in ast.walk(t) if isinstance(n,ast.Assign) and any(getattr(x,'id',None)=='CASES' for x in n.targets) and isinstance(n.value,ast.List)])"` → `[585]` |
| battery size | 6,114 lines | `wc -l corpus/fixtures/run_battery.py` |
| reports round dirs | 44 (r60–r104 minus r83) | `ls -d reports/round-* \| wc -l` |
| reports tracked files / size | 1,496 files / 19M | `git ls-files reports \| wc -l`; `du -sh reports` |
| corpus/live tracked / size | **40,677 files / 1.6G** | `git ls-files corpus/live \| wc -l`; `du -sh corpus/live` |
| LOG / SCORECARD | 336,796 B / 1,324 lines; 49,593 B / 366 lines | `wc -c -l LOG.md SCORECARD.md` |

**Coverage map.** `corpus/README.md` is 24 lines and still describes the corpus as it
stood at **r19**: 22 bullets, the last knowledge row reading "r19-stream-attribution.md"
(`grep -c '^- ' corpus/README.md` → 22). It has **no `## Frontier` section**, and it
claims "29 inherited" fixtures where 110 files now exist. `PROVINCE.md` has **one**
heading (the title) and no Core / Frontier / Adjacent split:
`grep -c '^#' PROVINCE.md` → 1. The only frontier artifacts are unlinked reports
`reports/frontier/fa-pygame.md`, `reports/frontier/fb-lovephysics.md` (2026-10-14).

**Overdue `recheck:` / missing metadata.** Not computable as "before 2026-10-19"
because neither knowledge entry carries the fields at all (0/2). Both entries predate
the fleet contract (`CORPUS.md` §Layout; `LEARNING.md` §Files the path writes) and
the production-checklist still cites r2–r59 evidence only.

**Knowledge/lessons balance — lessons hold knowledge that never reached
`knowledge/`.** This is the dossier's strongest finding. Examples with locations:

- `corpus/lessons/r104-resource-loader-uid.md` §1–§8 is a mechanism table for
  `uid_cache.bin` layout, the lossy `uid://` text encoding, the collision survivor,
  `CacheMode` identity, `.import` remap refusals, malformed-sidecar behaviour, and
  cross-process persistence — e.g. the quoted claim "The runtime authority is the
  binary cache, not the `.uid` text" (`r104-resource-loader-uid.md:20`). None of it
  is in `corpus/knowledge/`.
- `LOG.md` carries **16** `LAWS:` blocks across r88–r103 (`grep -c 'LAWS:' LOG.md`
  → 16), each a falsifiable rule with a measurement: e.g. export filters are
  case-insensitive (`LOG.md:1278`), pack bytes are root-path dependent
  (`LOG.md:1243`), bounds gating on startup latency must pin the margin not the
  constant (`LOG.md:1277`), and a pinned source-sha is a point-in-time receipt
  (`LOG.md:1280`).
- 31 rounds (71–100, 102) produced no distilled lesson file at all; their only
  durable record is `reports/round-N/rN-*.md` plus the LOG verdict bullet. An agent
  reading `corpus/` therefore cannot see 30 rounds of physics/input/nav/animation
  lattices except through 7.3 MB of raw seat reports.

This is a direct calibration/coverage failure against `LEARNING.md`'s path
(curation → quality gate → understanding), and it is why two files can coexist with
585 pinned rows.

## 4. Mistakes mined (class → evidence → gate status → proposed criterion)

No `QUALITY.md` and no `SKILL.md` exist, so **no existing criterion captures any of
these**; the sweep is `find . -iname 'QUALITY*' -o -iname 'SKILL*' -not -path './.git/*'`
→ 0 results. `LOG.md`/reports are the only record.

| # | class | evidence pointer | captured? | proposed criterion (for `QUALITY.md`) |
|---|---|---|---|---|
| M1 | negative control contaminated by positive sidecars (r6 HOLD) | `LOG.md:57` | no | a negative-control scratch must begin and end empty, proven by the runner, not assumed |
| M2 | unresolved failure with no causal fix (r17 HOLD; r16 intermittent export retained) | `LOG.md:169` | no | an honest stop must leave a named hypothesis and the next probing command |
| M3 | verifier ran the pre-fix commit; runner diff uncommitted (r64 DISAGREE 2/5, r64 integration defect) | `SCORECARD.md:24` | no | verification binds committed bytes; the verified blob hash is recorded in the verdict |
| M4 | declared grid overstated resolution (r68 ~80× claim falsified as written) | `SCORECARD.md:64` | no | a measurement grid reports its resolution and edge uncertainty, not just its conclusion |
| M5 | hypothesis refuted at a wider scope (r70: fabrication window is runner plumbing, not engine-general) | `SCORECARD.md:81` | no | falsification is admissible as a depth move when it narrows scope and is recorded as such |
| M6 | pins falsified after landing (r79 P1 dispatch-order snapshot, P2 same-frame visibility; P3 new member) | `SCORECARD.md` §r79 depth row | no | a pin is a claim with a mechanism sentence; a "why" that is bookkeeping is labelled so |
| M7 | PASS-while-broken harness: hardcoded ENet ports let concurrent batteries cross-connect (r88 BLOCKER) | `LOG.md:1108` | no | no fixed global resources in fixtures; parallel-safety needs a bind-loser negative |
| M8 | dead flag / unmeasured claim (`--offy` no-op, r95; "Y-translation honestly unmeasured, not falsified") | `SCORECARD.md:280` | no | every claimed measurement must trace to an executed token; dead flags are retired rows |
| M9 | custody-broken-at-link, systemic r96–r99 (evidence no longer resolves at its cited path) | `LOG.md:1196`, `LOG.md:1206` | no | evidence is self-contained at its link target; rebase/link checks run at close |
| M10 | provider failure orphaned 4 fixtures + 7 design-superseded ones (r101) | `LOG.md:1255` | no | a seat failure may not leave registered-but-unowned artifacts; disposition before close |
| M11 | row state leaks across rows: shared scratch-project uid cache retired 7 rows pre-close (r104) | `LOG.md:1319` | no | row isolation is proven by a negative control (shuffled/reversed order), not by XDG alone |
| M12 | operator reboot precluded re-run after post-run retirement (r104) | `LOG.md:1324` | no | retirement after the last green run requires either a fresh run or an explicit disclosed gap |
| M13 | simplifier breached read-only scope and overlapped tracked edits (r53) | `LOG.md:520` | no | write scopes are declared and checked; a seat's report states files touched |
| M14 | broad `git add` swept 180 scratch files (r6 bookkeeping correction) | `LOG.md:60` | partly (`.gitignore` grew, but 40,677 live files remain tracked) | ignore rules are verified with `git ls-files`, not assumed |

Cross-cutting: M1/M7/M10/M11 are one shape — **the harness can print PASS while the
thing under test is broken or confounded**. The lane found this repeatedly and fixed
instances, but never distilled it into a criterion or checklist.

## 5. Contract defects

| # | defect | evidence |
|---|---|---|
| D1 | **`SKILL.md` absent** — promised by `README.md:9` and required by `LEARNING.md` step 3; not a seed-form lane any more (104 rounds, 1 capability) | `find . -iname 'SKILL*' -not -path './.git/*'` → 0 |
| D2 | **`corpus/QUALITY.md` absent** — required by `CORPUS.md` layout and `LEARNING.md`; r101/r102 routed a "QUALITY.md scribe note (file absent — census routed)" and it is still absent at r104 | `find . -iname 'QUALITY*'` → 0; `LOG.md:1287` |
| D3 | `corpus/README.md` stale by 85 rounds: 24 lines, 22 bullets, last row r19, no `## Frontier`, wrong fixture count | `wc -l corpus/README.md`; `grep -c '^- ' corpus/README.md`; `ls corpus/fixtures \| wc -l` |
| D4 | `PROVINCE.md` has no Core/Frontier/Adjacent structure and no frontier list | `grep -c '^#' PROVINCE.md` → 1 |
| D5 | Lesson shape violates `CORPUS.md`: `rN-slug.md`, not `round-N.md`; **0/75** carry the required `## Gate` (candidates, admitted, rejected, spot-check) | commands in §3 |
| D6 | Knowledge shape violates the contract: 0/2 entries have `source:`, `verified-at:`, `recheck:` | `grep -cE '^(source\|verified-at\|recheck):' corpus/knowledge/*.md` |
| D7 | Scorecard axes are all `unscored`, violating the 0–10-or-verdict field; axis evidence table frozen at r49–r61 | `SCORECARD.md:6-10`; `sed -n '6,10p'` |
| D8 | `planned:` frozen at r64 (40 rounds stale); duplicate `## Saturation` headings (placeholder + declaration) | `grep -c '^planned: r64'` → 1; `grep -n '^## Saturation'` → 351,355 |
| D9 | Fleet ledger missing closure records r65–r100 for this lane | MANIFEST scan (9 lane records: train 61–64, closure 101–104) |
| D10 | Round 83 has no record at all; 82/84 only scout reports; no disposition recorded | `reports/round-83` absent; `ls reports/round-82` → 1 file |
| D11 | Bloat: 40,677 tracked files / 1.6 G under `corpus/live/` despite the README calling live scratch "ignored and disposable"; `.git` 337 M, repo 2.0 G; one tracked bytecode cache `reports/round-104/mutations/__pycache__/mut05.cpython-314.pyc` | `git ls-files corpus/live \| wc -l`; `du -sh .git corpus/live`; `git ls-files \| grep -E '__pycache__\|\.pyc$'` |
| D12 | Stale checkout citations `.shokunin/game-dev-2d/…` in 72 LOG lines and 18 lesson files; r101/r102 repaired only SCORECARD/PROVINCE instances | `grep -c '\.shokunin/game-dev-2d' LOG.md` → 72; `grep -rl … corpus/lessons/*.md \| wc -l` → 18 |
| D13 | Identity: still `shonen` with 0/4 boxes after 104 admitted rounds and a capability; no promotion record (`promotions: []` on 101–104) | `SHONEN.md`; MANIFEST closure records |
| D14 | Uncommitted changes: **none** (clean) — recorded so wave 2 does not look for them | `git status --porcelain \| wc -l` → 0 |

Dead pointers: the README points at `SKILL.md` (absent); `corpus/README.md` indexes
only r1–r19; `SCORECARD.md:12` plans r64 work as future. Stray artifacts: tracked
scratch (§D11) and the tracked `.pyc`; `reports/` holds 44 round dirs, 1,496 files.

## 6. Proposed round (r105)

Constraints: 1–3 claims on **distinct** axes, each with a falsifiable before→after and
a counting command, ≥1 on the lowest non-retired axis; every claim must verify and no
axis may be harmed. The lane's own r104 routings give the depth claim for free.

**C1 — depth (presumptive lowest by stale evidence; closes r104's routed harness
defect).** Per-row scratch isolation for the `res_uid` family (per-row project dir or
fixture-side uid-cache reset), re-admitting the 7 rows retired at r104 plus the
`s01_createid` repair. Before: `grep -c '^PASS res_uid' <log>` = 23 landed rows and 7
retired (`LOG.md:1319`). After target: ≥30 res_uid rows green in two runs **in
shuffled/reversed order**, with a negative control showing that a deliberately shared
cache re-creates the Unrecognized-UID ERROR (proves the isolation is load-bearing).
Counting: `python corpus/fixtures/run_battery.py …` run twice, plus
`grep -c '^PASS res_uid' <log>`. Falsifier: the shuffled-order run drops any res_uid
row, or the shared-cache control passes.

**C2 — calibration (scorecard contract).** Replace `unscored` with either 0–10 scores
whose command a reader can rerun, or a named-non-author `unprovable-but-better` row per
`AXES.md`; replace the r64 `planned:` with r105/r106 claims; collapse the duplicate
`## Saturation`. Before→after: `grep -cE '^\| (depth|coverage|calibration) \| [0-9]'
SCORECARD.md` 0→3 (or 3 reviewer-backed verdict rows); `grep -c '^planned: r64'` 1→0;
`grep -c '^## Saturation'` 2→1. Falsifier: any score cannot be re-derived from its
cited command, or a reviewer refuses the exploratory wording.

**C3 — coverage (expansion through the corpus path).** Admit **≥8 knowledge entries**
distilled from r96–r104 with the three required fields, each citing its lesson/receipt;
refresh `corpus/README.md` coverage map + add `## Frontier`; add `## Gate` to every new
lesson. Before: entries 2, entries with fields 0, README bullets ending r19,
`## Gate` 0/75. After: `ls corpus/knowledge/*.md | wc -l` 2→≥10;
`grep -lE '^(source|verified-at|recheck):' corpus/knowledge/*.md | wc -l` 0→≥8;
`grep -c '## Frontier' corpus/README.md` 0→1. Falsifier: an entry cannot name the
exact file/section it came from, or its recheck command does not resolve.

**Candidate knowledge entries (4) this round should serve.**

1. `res-uid-authority` — runtime authority is `uid_cache.bin`, not the `.uid` text;
   source `corpus/lessons/r104-resource-loader-uid.md` §1, quote "The runtime
   authority is the binary cache, not the `.uid` text" (:20); fills the
   "resource/UID" coverage-map gap (currently absent).
2. `uid-text-lossy` — `uid://` round-trip is id→text→id, not text→id→text; source
   same lesson §3; recheck = rerun the s01_roundtrip row.
3. `export-pack-root-dependent` — pack bytes are scratch-root dependent, so pin
   size/magic/census, never cross-root shas; source `LOG.md:1243` + r101 pack law;
   recheck = export twice under two roots and compare sizes/hashes.
4. `startup-latency-margin-law` — bounds gating on spawn→first-output latency must
   pin the margin, not the constant; source `LOG.md:1277` with r102's 0.39 s→0.8 s
   drift and re-derived 1.25 s bound; recheck = timeout probe at two host loads.

**Out of scope for r105 (do not absorb).** The 3D re-vendoring side-round is a
scheduling gate owned by the 3D lane (`reports/round-104/r104-connector.md:200`); the
lane must record its disposition, not perform cross-repo edits. Publication/store,
engine/editor source, asset rights (art-east-asian-design), and harness-integrity
audits remain refused per `PROVINCE.md`.

## 7. Provenance and limits

- All lane facts read at `main@e8990516`, tree clean; file references are line numbers
  in that commit.
- Numbers are static measurements (files, words, AST row count). No battery run, no
  Godot invocation, no network. Recorded pass counts (74/74, 96/96, 81/81, 585 CASES)
  are quoted from the lane's committed scorecard/log and were **not** re-executed;
  their truth is the lane's recorded claim, not this dossier's observation.
- `corpus/live/` was measured with `du`/`git ls-files` only; no scratch was opened.
- The 3D side-round claim, the promotion question, and the numeric-rubric question are
  reported as operator/L0 decisions; this dossier does not decide them.
