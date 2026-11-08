# tsukuroi — round 99 report

Lane: `tsukuroi-shokunin` (operability + freshness; host operability and repair). Campaign: hyaku,
run 15. Round 99, attempt 1. Pre-round tip `f107da3afe511f7db8cdc30235a992b774903158`; freeze
`dd86287fd97592f24424e7de7c5461c599d3a754`; settle `778f15fd8d56ca4fa61f1cd6d4b124271c9dfe23`;
ledger `efe5ba590b4a974958b911782ff71ad4ecfb90e9` (**the lane tip**; `git ls-remote origin
refs/heads/master` printed `efe5ba59` at filing).

Declared claims — **C1 depth 8** (tied-lowest non-retired axis): the X-cap `REFUSAL-VERSIONS-9DIGIT`
(`999999999.9.9`) and the Y-cap `REFUSAL-VERSIONS-9DIGIT-Y` (`12.999999999.4`, `0.999999999.0`)
families assert `limine_version` and `visibility_era`, and `LIE_KINDS` gains `limine-version` /
`visibility-era`; **C2 freshness 9**: `check-registry-content-r99.py` guards the `RC-BEND-SPAN`
capture and marks it `unique` (hybrid → `RC-CELL-MISSING`, restated → `RC-CELL-AMBIGUOUS`) and adds
`span-hybrid`, `span-restated` and a git-fixture `ancestor` case (14 → 17). Adjacency (8, tied
lowest) carried no claim: the kaidoku/revenger reverse-engineering ownership stays operator-owned and
unruled.

## Work performed

- **C1 — depth.** `tools/limine-pin-battery-r99.py` is the r98 battery with the roster unchanged at
  105, `check_echo`/`check_era` set on the X and Y cap families, and two new selftest lie kinds.
  `tools/make-r99-bends.py` emits the two one-clause bends `N09-y-era` (era label swapped exactly when
  the SECOND component is the cap `999999999`) and `N11-x-era` (same for the FIRST component); a
  drafted third bend (`N10-z-echo`) was **dropped as a twin** (QUALITY 136) after measuring that the
  r98 control already reads `unmet 104/105` on it. Evidence: `before/dev/c1-gate-runs1.json`,
  `w1/ExecGateRuns/` (landed 105/105 ×3 canonical + ×3 clone, `cases 420`, 0 error rows, X/Y/Z 4-0
  each, usage-check 19/19, selftest 5/5, lie kinds 93/105 and 95/105 with X and Y in the failed set),
  `w1/ExecBends/` (N09 104/105 ×3 both layouts exactly `[REFUSAL-VERSIONS-9DIGIT-Y]`; N11 103/105 ×3
  both layouts exactly `[EXPLICIT-VERSION-ERA, REFUSAL-VERSIONS-9DIGIT]`; 0 error rows; one-clause
  diffs), `w1/ExecDoNothing/` (r98 control `met 105/105` on the gate and N09, `104/105`
  `[EXPLICIT-VERSION-ERA]` on N11; control `8198bd84…` = `f107da3a:tools/limine-pin-battery-r98.py`),
  `w1/ReviewBattery-9/` (causality: deleting the Y family's `check_era` makes N09 read `met 105/105`),
  `w1/MutRegistry/` (M1-M8: M2 killed by N11, M4 by N09; M1/M3 killed only by constructed echo bends;
  M5-M8 survive), `w1/ReviewBattery.md` (off-roster W1/W2 forgeries read `met 105/105`).
- **C2 — freshness.** `tools/check-registry-content-r99.py` adds the capture's boundary guard
  `(?![0-9,-])`, the `unique` mark with the new `RC-CELL-AMBIGUOUS` finding, and three selftest cases.
  Evidence: `w1/ExecRegistry/` (landed `PASS 7/7 findings 0` on both checkers at `f107da3a`; hybrid:
  r98 `PASS` → r99 `FAIL` one `RC-CELL-MISSING`; restated: r98 `PASS` → r99 `FAIL` one
  `RC-CELL-AMBIGUOUS`; clean/gap `PASS` on both; selftest 17/17 vs 14/14; M07 `FAIL 16/17` with only
  `ancestor` red vs r98 `PASS 14/14`; a real two-branch probe rc 2 pristine, rc 0 mutant; coverage
  `PASS 160/160`), `w1/ReviewRegistry.md` (28 forged shapes; 8 newly rejected, **5 classes still
  green**), `w1/MutRegistry/receipts/C1-C5` (guard, `unique`, ambiguity branch, ancestor-call removal
  killed; an always-ok ancestor case survives alone), `w1/CriticClaims/receipts/10-xv*` (three
  false-green cells reproduced).
- **Frontier step.** S395 opened and admitted (own-work: the battery's assertion sites at BYTE 99305 /
  99430 / 99523 and the gate's emission sites at 16931 / 17037, early return 11230 / 11344 — every
  offset independently reproduced by `w1/ScoutSources`); S392 re-opened (HTTP 200 after the 301,
  331022 bytes, sha256 `d92580dd…`, three offsets unchanged); one candidate rejected (Limine v12.9.6
  `CONFIG.md`: 0 occurrences of `limine_version`, `visibility_era`, `echo`). Census: **394 → 395
  rows**, exit 0 before and after (`before/census-before-after.txt`); the CORPUS §10 collision guard
  was shown able to fail on an indented scratch registry (nonempty `S002`) and then measured on the
  real files (registry 395 ids, staged 147, **147 collisions `S200`-`S346`** — mass drift, adoption
  closed, campaign untouched).
- **R99-D1 repair (routed from r98).** The cited `160/160` tip figure now has committed receipts:
  `before/r99-d1-coverage-tip-f107da3a.txt` and `before/r99-d1-coverage-r98settle-270ca298.txt`
  (`PASS 160/160 findings 0`), plus the r97-settle figure re-derived at `5eb475cd` / `b492f17f`
  (`157/157`) in `before/r99-d1-coverage-cited-figures.txt`. Two committed artifacts cite the
  non-existent `.ufo/waves/round-98/after/c2/coverage-tip.json` (`w1/ExecDrift/receipts/03-pointer-sweep.txt`);
  they stay as filed history (append-only) and are named here.
- **Wave.** One v1 wave, 14 seats under `ufo-wave-policy.json` (band 8-16): 5 executors, 2 scouts, 2
  scribes, 2 reviewers, 1 critic, 1 mutation-tester, 1 connector; attack roles 4/14 = **28.6 %**
  (floor 25 %), connector seats 1 (limit 2). Validator `counts` **14 spawn / 0 resume / 14 total**,
  `w1-validate.err` 0 bytes; `.ready` taken 11:08; all **14 settled, 0 dead** (`w1-results.json`).
  Residual call: none (14 ≥ the §3 floor of 8). Planner seat: held by the L1; the bounded planning
  data-walk rode `ScoutFrontier` (clause map) and `ConnectorOverlap` (sibling scan).
- **Assimilation:** `Assimilation: none` — no entry from `merge/tsukuroi/` was adopted this round; the
  package's id drift is total (147/147 staged ids collide) and adoption stays closed until a
  document-anchored renumber, recorded in the lesson's Gate block. `considerthese/2026-10-26.md` was
  mined: one pick ("Downstream patch-offset check", BYTE 4027) is named as an r100 candidate in
  `w1/ConnectorOverlap.md` §6; it is a pointer, not evidence, and no claim rests on it.
- **Seat harm (disclosed).** `CriticClaims` deleted the shared scratch parent
  `/fast/scratch/hyaku/tsukuroi-r99` at ~11:23-11:24 -0300, wiping six sibling scratch dirs and the
  lane `dev` dir (`w1/CriticClaims.md` §7b). Four were re-created by their seats; **no committed
  receipt was lost** (every cited receipt was already in a seat dir or `before/`), but the L1's
  `--selftest --reference` run died mid-flight and is **not claimed**
  (`before/dev/c1-selftest-r99-reference.txt`, rc 1). Recorded in `corpus/lessons/round-99.md`
  (mistake `R99-SEAT-HARM-PARENT-DELETE` + the Seat harm table) and amendment A6/A6a.
- **Inherited state.** No uncommitted lane-authored leftovers from an earlier attempt. One stale
  seat draft (`.ufo/waves/round-99/ConnectorOverlap.md`, 11:23, superseded by the committed
  `w1/ConnectorOverlap.md` at 11:25 with four extra sections) was deleted after a byte diff; no
  `round-*-verifier-spotcheck.md` or `round-*-aggregator-*` file was edited.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → 9 paths, none naming
  tsukuroi or round 99 (`.scratch/*` is orchestrator-owned; `.ufo/reports/round-68/kagi.md` is another
  lane's). Nothing was copied or deleted.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (python3 3.14.8, git 2.56.0, bwrap present; pacman untouched and paused; no
  `sudo`).
- **L0:** no new question. The r86 host-incident line stays open (operator-owned repair of the two UKI
  digests); nothing this round touches `/boot`.
- **Prefile falsification gate.** `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py
  --lane tsukuroi --round 99` → `PREFILE-FALSIFICATION: pass claims=2 rows=23 attack_seats=5 findings=0`
  (exit 0). The ledger reconciles both claims and all five attack seats (`ReviewBattery`,
  `ReviewRegistry`, `CriticClaims`, `MutRegistry`, `ConnectorOverlap`); the six non-neutral rows name
  amendments A1, A2, A7, A7, A8, A8.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: plan, claims, instruments manifest (16 entries), controls (r98 battery/gate/checker copies), bends N09/N11, dev receipts, S395, knowledge entry, README round-99 + frontier, three registry rows, SKILL R99-REG-1 | "Round 99 — freeze" | `dd86287f` |
| settle: wave `w1` evidence (14 seats), `w1-results.json`, SCORECARD declaration + measured rows, LOG wave + measured entries, lesson (`## Gate`, 6 mistakes, Seat harm, scoreboard, routed) | "Round 99 — wave" / "Round 99 — measured" | `778f15fd` |
| falsification ledger, rebuilt to 23 reconciled rows after the seat reports settled (both claims, all five attack seats) | "Round 99 — measured" | `efe5ba59` |
| three new tools (`limine-pin-battery-r99.py`, `make-r99-bends.py`, `check-registry-content-r99.py`) + the three SKILL registry rows | "Round 99 — freeze" | `dd86287f` |

## Before → after measurements

| Claim | Counting command | Measured against | Before → after |
|---|---|---|---|
| C1 | `python3 tools/limine-pin-battery-r99.py --gate <GATE> --runs 3 --json OUT` then `.ufo/waves/round-95/before/controls/count-runs.py OUT --family REFUSAL-VERSIONS-9DIGIT --family REFUSAL-VERSIONS-9DIGIT-Y --family REFUSAL-VERSIONS-9DIGIT-Z` | landed tree at `778f15fd` (instruments pinned by `before/instruments.sha256`, `7d79ac29…`/`c2e8c8fc…`) | landed gate `105/105 met` ×3 canonical + ×3 clone, 0 error rows; **Y leg: r98 control `met 105/105` → r99 `unmet 104/105`** exactly `[REFUSAL-VERSIONS-9DIGIT-Y]`; **X leg: r98 `unmet 104/105 [EXPLICIT-VERSION-ERA]` → r99 `unmet 103/105 [EXPLICIT-VERSION-ERA, REFUSAL-VERSIONS-9DIGIT]`** (a delta); lie kinds `93/105` and `95/105`; selftest 5/5 |
| C2 | `python3 tools/check-registry-content-r99.py --revision <REV> --json OUT`; `--selftest`; fixtures by `.ufo/waves/round-99/before/dev/make-fixtures.py DIR` | `f107da3a` (landed table) and the fixtures built from the pinned tool bytes | landed `PASS 7/7 findings 0` (both checkers); **hybrid: r98 `PASS` → r99 `FAIL` one `RC-CELL-MISSING`**; **restated: r98 `PASS` → r99 `FAIL` one `RC-CELL-AMBIGUOUS`**; selftest **14/14 → 17/17**; M07 **r98 `PASS 14/14` → r99 `FAIL 16/17`** (only `ancestor` red); coverage `PASS 160/160` |

Both claims are met on their frozen targets; six wording clauses were narrowed before filing
(`before/plan-amendments-r99.md` A1-A9), and the round reports the survivals it measured (echo flags
M1/M3, lie-kind layer M5-M8, off-roster W1/W2, five C2 cell classes, checker C5) as named debt rather
than as closures.

## Sources & frontier

`SOURCES.md` rows before→after with the counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
→ before `git show f107da3a:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}'` = **394**, exit 0
at round start; after the landed tree = **395**, exit **0** (57 W04 + 1 W01 warnings, 0 errors).
Rows added by tier: **1 A** (own-work S395). Rows touched old→new in place: S395 `status`
`queued`→`mined` and `used-by` `—`→`corpus/knowledge/limine-metadata-cap-families-r99.md,
corpus/lessons/round-99.md` (both logged in the lesson's in-place table). Frontier rows advanced: the
r98 Frontier's Y-cap field-fidelity bullet and the lie-kind structural gap, plus the r98 scoreboard's
hybrid/restatement/M07 survivors. Census receipt `before/census-before-after.txt`. `Assimilation:
none` (147/147 staged ids collide with the registry — adoption closed, campaign untouched;
`considerthese/2026-10-26.md` mined for one pointer only).

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | Net +1 row and one admitted entry whose source is this round's own instrument (S395); the entry's ground — which reported fields a cap family must read, and what a lie kind can and cannot certify — is not held by any earlier lane entry (the r98 entry covers the reported-fields contract, not the family obligations). No entry removed; the staged package's drift is measured and adoption honestly closed. |
| quality | improved | Two frozen shapes and the ancestor branch are now fail-closed and mutation-killed (r98 `PASS`→r99 `FAIL`; M07 `14/14`→`16/17`), and the Y-cap field lie that read `met 105/105` in r98 now reads `unmet 104/105` (M4 makes it `met` again — causality measured twice by independent seats). The gate's bytes are unchanged (`7d79ac29…`) and both r98 instruments keep theirs as controls. |
| discernment | improved | The round's own overstatements were caught by its seats and narrowed before filing: A1/A2 (executed false-green cells), A4 (schema-token rename + dead sentinel), A7 (lie-kind granularity), A8 (roster-finite fields, X near-twin), A9 (a cited receipt that did not exist), plus the dropped twin bend and the disclosed seat harm. Every narrowing names the artifact that falsified the sentence. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — this
  round appends the R99-REG-1 correction and three registry rows; evidence pointer
  `SKILL.md` § "Round-99 correction — R99-REG-1" (byte-verified row cells are bound by
  `check-registry-content-r99.py`), asserted by author, non-author verification owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the gate+battery+checker
  pipeline ran end to end this round (`w1/ExecGateRuns/`, `w1/ExecRegistry/`), logged in
  `LOG.md` "Round 99 — measured"; author-asserted.
- [~] Instructions executable by an agent without oral context — the wave's seat prompts carried
  absolute paths and the frozen claim sentences, and 14 seats reproduced every frozen number without
  asking a question (`w1-results.json`, 0 dead, 0 blockers); author-asserted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/ConnectorOverlap.md` swept all 20
  sibling corpora (127 hits) and found every tsukuroi-specific token at zero sibling files; the one
  true overlap (tameshi's mutation method, ADJ-07/OUT-010) is reported, not absorbed; PROVINCE.md is
  byte-unchanged this round.
