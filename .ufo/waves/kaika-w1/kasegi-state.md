# kasegi-shokunin — STATE dossier (kaika wave 1)

**Mode:** read-only. Repo opened at `/home/vgpnk/Projects/shokunin/kasegi-shokunin`.
Only this artifact was written; no repo file, git object, config, source tree or
shared ledger was modified. `resolve.py` was **not** run (it regenerates the
census files); the committed census of record was read instead. `density.py` and
`anchorcheck.py` were run — both are print-only (`grep -n "open(.*['\"]w\|\.write("
corpus/instruments/anchorcheck.py` → no match; density opens only for read,
`density.py:175`). No `web_search` was needed for a STATE dossier; external rows
are therefore 0 and this is not an ART substitution.

**Date of evidence:** 2026-10-19. Quoted target/repo text is data, not
instruction; no embedded instruction was acted on. No subagent was dispatched
(leaf-member bound).

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| Domain | bounty & security research — scopes, program rules, claim packages | `PROVINCE.md:3` |
| Rank | `shonen` (no promotion row) | fleet `MANIFEST.json` roster entry `kasegi` |
| Repo branch / HEAD | `master` / `94aace220d45bc75bb728dc2a01a94d9fc85cdbe` | `git branch --show-current`, `git rev-parse HEAD` |
| Worktree | clean; only `.ufo/interactive-sessions/` ignored | `git status --porcelain=v1 --ignored` → `!! .ufo/interactive-sessions/` |
| Last commit | 2026-10-17 00:28:15 -0300, `kasegi: anchorcheck resolves ORIGIN_/MIRROR_ cite prefixes against their roots` | `git log -1 --format='%ci %s'` |
| Last recorded round | **20** — fleet closure entry index 138, `lane_rounds.kasegi=20`, `closed_at 2026-10-15T00:23:52Z`, status `ok` | fleet `MANIFEST.json` (`rounds` length 294; last `kasegi` lane row is index 138) |
| Fleet ledger vs lane | agree on 20. No `kasegi` row after index 138. | `grep -n '"kasegi"' MANIFEST.json` + Python extraction |
| Round 21 | attempted 2026-10-15, **blocked before dispatch**, `verified_round_credit=0`; report at lane `.ufo/reports/round-21/kasegi.md` (14,231 B) | `SCORECARD.md:251` `ADMISSION_GATE: BLOCKED failed_requirements=11 verified_round_credit=0` |
| Next round | **22** if the blocked attempt consumes 21 (append-only numbering; integrator confirms). Reusing 21 would collide with an existing report + lesson. | `SCORECARD.md:228-290`; `plans/wwkd-round-21-authority-audit.md` |
| SHONEN | 0 of 4 complete: 2 partial (`[~]`), 2 unchecked (`[ ]`) | `.ufo/reports/round-21/kasegi.md` §SHONEN |
| Capabilities | **0** (`— none yet —`) | `SCORECARD.md:295` |
| Saturation | undeclared; deferred to the next round | `SCORECARD.md:301` |

Identity notes:

- The two later commits after the round-21 report are **not rounds**:
  `24cfce5` (2026-10-16 SCORECARD contract scaffolds, “no axis claims”, +17 lines
  in `LOG.md`/`SCORECARD.md`) and `94aace2` (2026-10-17, +4/−2 in `anchorcheck.py`
  and `.gitignore`). The round-21 report's `INHERITED-ANCHORCHECK-EDIT` debt was
  therefore integrated after the report, but neither commit carries a round
  verdict; do not count them as a round 21 completion.
- The lane's own WWKD says “Round 20 is the highest documented lane round”
  (`plans/wwkd-round-21-authority-audit.md:5`) and the old launch counter 17 is
  not a verified-round count. The fleet ledger agrees at 20.
- Domain ground truth remains absent: `~/Projects/bounties` (lost 2026-09-28),
  `~/Projects/the-bounty-hunter` and the whole `~/Projects/origin-work` tree
  (lost on/around 2026-10-12). Verified this session:
  `test -e ~/Projects/bounties` → fail; `test -e ~/Projects/the-bounty-hunter` →
  fail; `test -e ~/Projects/origin-work` → fail; `test -d ~/Projects/ufo-fsd-alpha`
  → pass at `964f443e`. Re-scoping `PROVINCE.md` is still an operator decision
  (open L0 row, `.ufo/l0-questions.md` kasegi round-15).

---

## 2. Axes

The lane scores only the axes it owns (depth split into density + verifiability,
plus coverage). Other axes are fleet-owned and reported, not scored here.

| Axis | Score | Evidence pointer (re-runnable) | Last change |
|---|---:|---|---|
| depth:density | **9** | `python3 corpus/instruments/density.py SKILL.md --label w1-state` → mean **154.0**, **645** path-citation instances, **18** blocks. BAR_R15 = **142.5**. **11 of 18 blocks are below the bar**; median block density **129.2**; range 13.3–462.5. | r15 (held r19/r21) |
| depth:verifiability | **4** | Committed census of record (`corpus/instruments/citation-survival.md`, r18 definition): SKILL **32/506 = 6.32 %**; corpus **118/1153 = 10.23 %**; lane **134/1480 = 9.05 %**. `python3 corpus/instruments/anchorcheck.py SKILL.md` → `7 in-range, 0 bad; 7 distinct; LOST-RECORDED=306; PIN-BROKEN=0; ORIGIN=0; OUTSIDE-BASE=0; BASE-ABSENT=0`. | r19 (held r21) |
| coverage | **7** | r15 denominator: 18/18 corpus-attested, **0/18 present**; the two r15 “surviving roots” are now **0/2 present**. | r15 (held r21) |

- **Lowest non-retired axis: `depth:verifiability` = 4.** Planned next move is
  already named in `SCORECARD.md:167-174`: audit recorded severity/decree claims
  for support in the surviving lane corpus; “Do not replace primary sources with
  circular corpus citations to raise the resolution fraction.”
- **Saturation line + stagnation window N are not declared** (`SCORECARD.md:301`),
  so the stagnation nudge cannot fire and no axis is retired.
- **Capabilities: 0.** No capability has a demonstrated running round; the r21
  report explicitly refuses to count a rendered plan or a resolver fixture as
  capability evidence.
- Score honesty check: the density **score is 9** while 11/18 blocks are below the
  lane's own bar. That is not a contradiction in the lane's terms — the axis
  score records the best measured state and the bar rule is per-repaired-block —
  but it is why the file mean must not be read as “all blocks healthy”.
- The round-20 move-log row records `freshness` verdicts “measured at HEAD (see
  lesson) … no scalar” (`SCORECARD.md:186`); that is a fleet-wave move, not a
  fourth lane-owned axis.

### SKILL.md — bloat vs density (explicit verdict)

**Dense by its own proxy, not healthy by its own conjunctive rule.** On
2026-10-19: 81,063 B / 1,012 lines, mean density **154.0** (`density.py`), just
above `BAR_R15 = 142.5`. But **11/18 blocks are below 142.5**, the median block
is **129.2**, and the file's defined resolvability is **32/506 = 6.32 %** —
far under the ≥60 % conjunctive gate that the lane itself adopted from r16
(`SCORECARD.md:55-58`). The second-highest-density block is
`## Cited paths` at **313.9** — 7,222 B / 37 lines, entirely `[lost-tree]`
paths that cannot be opened. The mean is carried by that block, `## Policy
access playbook` (462.5) and two other table-shaped blocks; the thin majority
(13.3–131.4) is where the actionable craft sits.

Size context: `wc -c */SKILL.md | sort -n` over 18 lane repos puts kasegi at
**81,063 B, rank 13 of 18**, above the fleet median (**45,705.5 B**,
`(40280+51131)/2`) but far below the 144,943 B maximum. The 81 KB is therefore
not an outlier, but it is ~1.8× the fleet median.

Verdict: **historical annotation, not filler, is the bloat.** 313 loss markers
plus a 1,847 B status preamble duplicate `PROVINCE.md`/`SCORECARD.md`
(measured: `sed -n '8,35p' SKILL.md | wc -c` → 1,847). Deleting the dead
appendix would *lower* the density mean — the proxy's perverse incentive — so
the correct test is the conjunctive bar, under which the file currently fails;
any cut must be an explicit docs-consolidation claim, not a density claim.

---

## 3. Corpus

Counts (all commands run from the lane root):

| Item | Count | Command |
|---|---:|---|
| `corpus/knowledge/*.md` | **25** | `ls corpus/knowledge/*.md \| wc -l` |
| `corpus/lessons/*.md` | **24** | `ls corpus/lessons/*.md \| wc -l` |
| instruments / census files | **7** | `find corpus/instruments -type f \| wc -l` |
| `corpus/QUALITY.md` | **0 (absent)** | `test -f corpus/QUALITY.md` → fails |
| coverage-map data rows | **25** | `awk '/^## Coverage map/{f=1;next}/^## /{f=0} f&&/^\| /{n++} END{print n-2}' corpus/README.md` |
| `## Frontier` rows | **0** | `grep -c '^## Frontier' corpus/README.md` |
| lessons with `## Gate` | **3 of 24** | `grep -l '^## Gate' corpus/lessons/*.md \| wc -l` |
| knowledge with exact `source:` | **0 of 25** | `grep -l '^source:' corpus/knowledge/*.md \| wc -l` |
| knowledge with prose `Source:` | **17 of 25** | `grep -l '^Source:' corpus/knowledge/*.md \| wc -l` |
| knowledge with `verified-at:` | **0 of 25** | `grep -rl '^verified-at:' corpus/knowledge/*.md \| wc -l` |
| any corpus file with `recheck:` | **0** | `grep -rl '^recheck:' corpus --include='*.md' \| wc -l` |
| lesson files for rounds 16/18/19 | **0** | `ls corpus/lessons/` (has 17, 20, 21; no 16/18/19; no round-2) |
| `[lost-tree]` + `[lost-base]` markers in SKILL | **313** (110 + 203) | `grep -oE '\[lost-(tree\|base)\]' SKILL.md \| wc -l` |
| SKILL size | **81,063 B / 1,012 lines** | `wc -c SKILL.md`; `wc -l SKILL.md` |

**Coverage map.** The map has **25 data rows** but references only **24 of 25**
knowledge files; `corpus/knowledge/citation-bases.md` is missing from the map and
appears only in the Known-gaps prose (`corpus/README.md:58`). Its
`| Lessons | lessons/round-1.md … lessons/round-15.md |` row is stale: 24 lesson
files exist including `round-17-mirror-relocation.md`, `round-20-recensus.md` and
`round-21-routing-blocked.md` (`corpus/README.md:36`). An index row is a claim —
these rows understate the corpus.

**Frontier.** There is no `## Frontier` section in `corpus/README.md`
(`grep -c '^## Frontier'` → 0), and `PROVINCE.md` has **no H2 sections at all**
(`grep -c '^## ' PROVINCE.md` → 0): no `Core`, `Frontier`, `Adjacent`. The fleet
contract requires `README.md` “coverage map, known gaps, frontier”
(`CORPUS.md:11`) and a province “Core / Frontier / Adjacent” structure
(`LEARNING.md:66-70`). The lane's own “Known gaps” section lists no prospective
frontier topics.

**Freshness.** 0 of 49 corpus entries carry `recheck:`, so no entry can be
assessed as overdue and none has a declared cadence; 0 carry `verified-at:`. The
oldest prose as-of stamps cluster on 2026-09-28 and 2026-10-13/14; the two
primary roots have been absent since 2026-10-12. Semantic freshness is therefore
**unbounded**, not green.

**Blast radius of the r18 correction.** `corpus/knowledge/citation-bases.md` is
the one written vocabulary for bases; it is the one knowledge entry missing from
the coverage map (above) and carries no `source:/verified-at:/recheck:` header.

---

## 4. Mistakes mined

“Captured?” = does a `QUALITY.md` criterion or `SKILL.md` rule already cover the
class? No `corpus/QUALITY.md` exists, so **every row's QUALITY answer is “no
criterion”**; the “captured by” column names the closest surviving rule when one
exists. Absence sweep for the round-level classes:
`grep -ci 'transcription\|self-ingest\|frozen filesystem\|marker report\|report-before-commit\|outside spot-check' SKILL.md`
→ 0; same sweep over the corpus:
`grep -rci 'transcription\|self-ingest\|frozen filesystem\|marker report\|report-before-commit\|outside spot-check' --include='*.md' corpus | awk -F: '{s+=$2} END{print s+0}'`
→ 1 (`transcription` in a lesson). So round-process failure classes are
essentially uncaptured.

| # | Class | Evidence pointer | Captured by | Proposed criterion (if none) |
|---|---|---|---|---|
| M1 | Completion-evidence failure: 273 B marker filed as a round closeout | fleet MANIFEST round-16 row: `kasegi r16 -> failed … 273 B, hex tokens 0, SHONEN 0 … marker`; introducing commit `17c1fad` | Fleet `PROTOCOL` marker rule; no lane rule | A round artifact is evidence only if it names its work commit and a before→after measurement; a marker is not a round |
| M2 | Dead hash citation + attribution/report-before-commit | MANIFEST r13 note: `d7dbd9a UNRESOLVABLE in every local object database`; report committed 15 s before its own child commit | No lane rule | Every cited hash must pass `git cat-file -e <hash>` at filing; report commit must be an ancestor or a named successor |
| M3 | Gate disagreement resolved with evidence (critic falsification rejected) | `corpus/README.md` last Known-gaps bullet: “One critic falsification REJECTED with evidence” (`fleets/claimer-mission.md:29`) | Citation-bases rule 1/6 (anchor bases) | A rejection must name the exact location and its sweep; rejecting on absence requires the search command |
| M4 | Density bar deliberately not cleared (honest negative, no reflow gaming) | `SCORECARD.md` r15 row: four repairs `131.4 / 111.5 / 117.4 / 93.0`, `BAR_R15` not cleared | Yes — `instruments/README.md` bar rule + form-sensitivity (93.3 prose vs 150.0 table) | — |
| M5 | External shock mid-round: primary tree deleted while the round ran | `corpus/knowledge/source-tree-loss-2026-09-28.md`; LOG r15 | Partly — base vocabulary + PROVINCE annotations | A round's first command is an existence check of every base it plans to cite |
| M6 | Numerator transcription error: `480/1506` published; r18 labrat re-derived `451/1506` | `SCORECARD.md:88-96`; LOG r17/r18 | No QUALITY criterion | Census numbers are copied from the committed TSV, never retyped; re-derive once before publication |
| M7 | Instrument blind spots: resolver ingested its own generated census; stripped leading dots; broadened matcher found 82 hidden bad anchors | LOG r18 (`old token cleanup stripped leading dots`); `instruments/README.md` known limits | Yes — r18 corrections + documented limits | Keep a mutation fixture per instrument; a `bad=0` is only meaningful under the named matcher |
| M8 | Re-anchored four receipt citations to git-untracked files; no durable blob pin claimed | LOG r18 (“The source tree is mutable and all four receipt-store files are git-untracked”) | Yes — citation-bases rule 2 (BLOB-PIN) | Untracked-but-read bytes are current-byte evidence only; record SHA-256 and the absence of a pin |
| M9 | Second root loss: 202 bad anchors; scores held, `BASE-ABSENT` class invented | `SCORECARD.md:121-149`; `corpus/knowledge/root-loss-2026-10-12.md` | Yes — derived roots + `BASE-ABSENT` + `[lost-base]` | — |
| M10 | Stale current-tense claims: 22 live lines still call absent roots “live” | `corpus/lessons/round-20-recensus.md:39-43`; spot-check `submitted-registry.md:9`, `:27` | Partly — citation-bases rules 1/3 cover anchors, not prose “LIVE” assertions | Any sentence asserting a tree is live carries an as-of date and the `test -d` result; absent → `[lost-base]` |
| M11 | Self-description drift: stale rates/dead pointers/`$UFO_SRC`/unreproducible 50-deletion claim | `corpus/lessons/round-20-recensus.md:22-48` | No QUALITY criterion | Self-description is a claim: rates cite the census file, `$` variables cite a reader, deletions cite a command |
| M12 | Blocked round: 32 scopes authored and rendered, **0 dispatched**; no receipt fabricated | `SCORECARD.md:228-290`; `.ufo/rounds/round-21/admission-gate.json` exit 1 | No lane rule (external routing contract); report records it | A rendered wave is not execution; blocked rounds report zero credit and their unblock action |
| M13 | Prior frozen assertion falsified: `32/506` replay → `33/506` live-FS, `31/506` Git-export | `SCORECARD.md:259-270`; `.ufo/rounds/round-21/frozen-*-guard.json` | No QUALITY criterion | “Frozen” must name both byte inputs and the filesystem definition; replays publish all divergent definitions |
| M14 | Ledger holes: no round-2 record; no lesson for rounds 16, 18, 19 | `corpus/README.md` Known gaps (“no round-2 record and LOG.md jumps round 1→round 3”); `ls corpus/lessons` | Append-only discipline prevents rewriting; no rule requires a lesson per round | A round without a lesson is recorded as a named omission in the next lesson |
| M15 | Fleet conformance defects: SHONEN heading absent in reports r10–r14 and r17; operator-identity commits; report-before-commit | fleet MANIFEST notes for r12/r13/r14/r17 | No lane rule | Report template check before filing: SHONEN section, work commit, hash resolution |
| M16 | Contract omission: QUALITY bar never minted; provenance fields never written; Gate sections mostly absent | `CORPUS.md:12,17`; `LEARNING.md:54-60`; counts in §3 | No — this is the missing gate itself | Create `QUALITY.md` thin, each criterion citing the lesson that produced it; add the three headers + `## Gate` |

Gate agreements/disagreements worth preserving:

- r15 critic and labrat independently derived the compounding-ratchet argument
  (re-deriving the bar from the current mean); both were adopted
  (`SCORECARD.md:44-58`).
- r20 independent audit **agreed** with all three instruments' counters and then
  found 22 dead-path lines the author had missed (`round-20-recensus.md:39`).
- r21's admission gate blocked 10 role bindings + 1 missing fallback and refused
  to manufacture a receipt (`invalid_id`, exit 1) — an honest stop, not a failure
  of craft.

---

## 5. Contract defects

Lane-local (owner: kasegi):

| # | Defect | Evidence (command / location) |
|---|---|---|
| D1 | `corpus/QUALITY.md` missing — the learning path's quality gate is skipped | `test -f corpus/QUALITY.md` fails; required by `CORPUS.md:12`, `LEARNING.md:13`; 10/18 lane repos have one, kasegi is 1 of 8 without |
| D2 | Knowledge entries do not open with `source:`, `verified-at:`, `recheck:` | 0/25 exact `source:`; 0/25 `verified-at:`; 0/49 `recheck:`; 8/25 lack even a prose `Source:` (list: `citation-bases`, `intake-surface`, `repo-git-state`, `root-loss-2026-10-12`, `source-tree-loss-2026-09-28`, `submitted-registry`, `target-checkouts`, `ufo-workspaces`) |
| D3 | Lessons lack `## Gate` | 3/24 have it; required by `CORPUS.md:18`, `LEARNING.md:60` |
| D4 | No `## Frontier` in `corpus/README.md` | `grep -c '^## Frontier' corpus/README.md` → 0; `LEARNING.md:59` |
| D5 | `PROVINCE.md` has no Core/Frontier/Adjacent structure | `grep -c '^## ' PROVINCE.md` → 0; `LEARNING.md:68-70` |
| D6 | Coverage-map defects: `citation-bases.md` has no map row; Lessons row stale (`round-1 … round-15`) | `corpus/README.md:36` (Lessons row); `citation-bases.md` appears only at `README.md:58`; 24 lesson files incl. 17/20/21 |
| D7 | Saturation line + stagnation window N undeclared | `SCORECARD.md:301` |
| D8 | Capabilities table empty (0 rows) | `SCORECARD.md:291-297` |
| D9 | Stale rate in r19 row vs census of record | `SCORECARD.md:134` says lane `132/1469 = 8.99 %`; census says `134/1480 = 9.05 %`; also `corpus 116/1142` vs `118/1153` |
| D10 | 22 live dead-path lines still unmarked (r20 audit class) | `round-20-recensus.md:39`; explicit false-current claims verified: `submitted-registry.md:9` (“live sibling tree”), `:27` (“verified live”); the wider audit class includes `citation-bases.md:72`, `triage-thresholds.md:12`, `intake-and-finalize.md`, `ops-invariants.md`, `operator-queue.md`, `SCORECARD.md:174` |
| D11 | `$UFO_SRC` documented as a consumer but read by no instrument | `round-20-recensus.md:22`; `grep -n 'UFO_SRC' corpus/instruments/*.py` → no reader |
| D12 | Missing lesson files for rounds 16, 18, 19 (and the round-2 hole) | `ls corpus/lessons/` |
| D13 | SKILL bloat/density mismatch | 81,063 B / 1,012 lines; 11/18 blocks < 142.5; mean 154.0; median 129.2; 6.32 % resolvability; 313 loss markers; all-lost `## Cited paths` block is 7,222 B / 37 lines with density **313.9** |
| D14 | Shared report path missing for rounds 19 and 21 | `ls .ufo/reports/round-19/kasegi.md` and `round-21/kasegi.md` at the fleet root fail; round-21 report exists only at `kasegi-shokunin/.ufo/reports/round-21/kasegi.md` (14,231 B); fleet `round-21/` contains only `kotodama.md` |
| D15 | Max line length 1,187 chars in SKILL | `awk '{if(length($0)>max){max=length($0);ln=NR}} END{print max,ln}' SKILL.md` → `1187 695` |

External (not lane-owned; carried verbatim, not fixed):

| # | Blocker | Evidence |
|---|---|---|
| X1 | Routing bindings: 10 role bindings + missing `@m_antigravity → @m_zfl` fallback; wave dispatch blocked | `.ufo/rounds/round-21/admission-gate.json`, `routing-observation.json` |
| X2 | Receipt binding absent; canonical mint refused (`invalid_id`) | `.ufo/rounds/round-21/receipt-mint-attempt.json`, `receipt-preflight.json` |
| X3 | Canonical-upstream drift observed **during this session**: `/home/vgpnk/Projects/kimi-shokunin` listed (LICENSE, skills, templates) and seconds later `stat`/`cat` returned “No such file or directory”, repeatedly; no canonical template content is claimed | this session's `ls`/`find`/`cat` sequence; same prune regime documented in `.ufo/l0-questions.md` kasegi/kake rows |

Conflict reported verbatim (not reconciled): `PROVINCE.md` says both surviving
roots are ABSENT, while `corpus/knowledge/submitted-registry.md:9` calls
`~/Projects/origin-work/open-bug-bounties/` “the live sibling tree”. The second
statement is false at this date and is D10 debt, not a second truth.

**Uncommitted / stray:** none. `git status --porcelain` → empty;
`git status --porcelain --ignored` → only `!! .ufo/interactive-sessions/`
(ignored by `.gitignore:1`) and `__pycache__/` (`:2`). Both `plans/*.md` are
tracked (`git ls-files plans` → 2 files). No stray untracked artifact found;
nothing was touched, staged, committed or cleaned.

---

## 6. Proposed round 22

Constraints applied: 1–3 claims, distinct axes, ≥1 on the lowest non-retired
axis (`depth:verifiability` = 4); each claim falsifiable with a pasteable
command; no score or fraction moved by circular citation; no external live-target
work; no 32-member wave claimed (X1 blocks dispatch and is external).

**Setup (not a scored claim; prerequisites):**

1. Create `corpus/QUALITY.md` — thin is allowed (`LEARNING.md:56`), but every
   criterion cites the lesson that produced it. Ground candidates: M1 (round
   evidence), M6 (census transcription), M7 (instrument blind spots), M10 (live
   claim vs lost base), M12 (rendered wave ≠ execution), M13 (frozen means bytes
   + filesystem), M16 (provenance headers). Do **not** invent a bar first.
2. Record the outside non-author spot-check this round needs: ≥1 admit and ≥1
   reject, `agree`/`disagree` with reasons, in the round lesson
   (`LEARNING.md:39-49`). The r21 report recorded `OUTSIDE_SPOTCHECK:
   NOT_PERFORMED`; without it, admissions/exploratory verdicts do not clear
   discernment.

| Claim | Axis | Before → after (falsifiable) | Counting command | Expected verdict |
|---|---|---|---|---|
| **C1. Provenance and recheck closure** — every knowledge entry gets `source:`, `verified-at:`, `recheck:`; every lesson gets `## Gate`; each `recheck:` is a runnable command that fails closed on an absent base | depth:verifiability (4) | knowledge with all three fields **0/25 → 25/25**; lessons with Gate **3/24 → 24/24**; explicit false-current claims to the absent root **2 → 0** | `grep -l '^source:' corpus/knowledge/*.md \| wc -l`; `grep -l '^verified-at:' …`; `grep -l '^recheck:' …`; `grep -l '^## Gate' corpus/lessons/*.md \| wc -l`; `grep -rnE 'live sibling tree\|\(verified live\)' corpus/knowledge/*.md \| wc -l` | improved (auditability); resolver score **held at 4** — do not launder the fraction |
| **C2. Repair the thinnest actionable block** — likely `## Operator queue — live audit` (dens 97.2) or `## Pipeline` (13.3); target `dens ≥ 142.5` **and** ≥60 % of the block's path citations openable, per the conjunctive bar | depth:density (9) | target block summary row 97.2 → ≥142.5; file mean 154.0 → whatever follows (report, no self-inflation); `anchorcheck` bad stays 0 | `python3 corpus/instruments/density.py SKILL.md --label r22-before`; same with `--label r22-after`; parse the block row; `python3 corpus/instruments/anchorcheck.py SKILL.md`; every added cite passes `test -e` | improved at block level, score held at 9 if it moves nothing else; if 60 % cannot be met, report the block **blocked** and claim nothing |
| **C3. Declare and enter the frontier** — add `## Frontier` to `corpus/README.md` and `## Core / ## Frontier / ## Adjacent` to `PROVINCE.md`; admit **one** ART-sourced entry on uncovered ground with `source:`/`verified-at:`/`recheck:`, a coverage-map row and an `S###` row behind it | coverage (7) | frontier rows **0 → N** (N ≥ 1), each carrying an `S###`; PROVINCE H2 sections **0 → 3**; admitted frontier entry **0 → 1** | `grep -c '^## Frontier' corpus/README.md`; `grep -cE '^## (Core\|Frontier\|Adjacent)' PROVINCE.md`; `grep -cE '^\| F[0-9]{2} .*\| S[0-9]{3} ' corpus/README.md`; `test -f corpus/knowledge/<slug>.md` | improved expansion; coverage score moves only if a surface fraction moves, else held with the trend recorded |

Claim separability: C1 is verifiable without C2/C3 (its commands read corpus
headers); C2 is verifiable without C1 (density block row); C3 is verifiable
without C1/C2 (frontier row + file existence). The QUALITY bar is a setup
prerequisite for C3's admission, not a fourth claim.

**What SOURCES.md / new entries serve these claims**

- C1: SOURCES rows only where a lost-primary authority is replaced by a *live
  public primary* (e.g., platform policy pages); otherwise no S-row — the
  recheck line is a local command. C1 must not cite the lane's own corpus as a
  substitute for primary text.
- C2: no SOURCES dependency if the repair uses lane-internal instrument/knowledge
  paths; if the operator-queue gates are re-grounded in public platform docs, cite
  those S-rows and keep the lost-tree quotes as historical.
- C3: the ART dossier's top-ranked row(s) and its study `Path`; the new entry must
  clear the new `QUALITY.md` criteria and fill a named coverage-map gap.

**Honest-stop conditions**

- If C2 cannot reach 60 % resolvability without lost-path padding, the round
  reports the block as blocked, keeps the density score at 9, and files the
  reason as a lesson — no reflow-to-table.
- If no ART source clears the new QUALITY bar, C3 reports `unchanged` and keeps
  the frontier rows as queued (status `watch`/`queued`), not admitted.
- If the routing/receipt blockers (X1/X2) are still present, no wave or receipt
  is claimed; the round is still admissible as local craft if every claim
  verifies and no axis is harmed.

**Why not the other tempting moves**

- Raising the resolver fraction by replacing `[lost-*]` cites with lane-internal
  ones is citation laundering; the lane's own plan forbids it
  (`SCORECARD.md:167-174`).
- Deleting the all-lost `## Cited paths` appendix would cut ~7.2 KB and a
  density-313.9 block, i.e. it would *lower* the density mean; it is a
  docs-consolidation decision, not a density claim. Keep it as a pointer until a
  human rules, or evaluate the file under the conjunctive bar rather than the
  mean.
- A 32-seat authority audit is the r21 plan and remains blocked by X1; a
  single-author bounded audit is the executable subset and must not be described
  as a validated wave.

---

## 7. Out-of-scope items (reported, not absorbed)

- `~/Projects/ufo-fsd-alpha` (present, `964f443e`) is a UFO substrate, not a
  bounty surface; only its script paths are cited by this lane.
- Fleet routing/model bindings and receipt minting (X1/X2) belong to the
  integrator; this lane may not patch global config or synthesize a `task_` key.
- Canonical upstream `kimi-shokunin` is not the authority while the fleet root's
  `PROTOCOL.md`/`CORPUS.md`/`LEARNING.md`/`AXES.md` are present; its observed
  flapping (X3) is a host-drift signal for the operator, not a lane defect.
- No live target, program portal, credential, vault, or bounty endpoint was
  contacted. No security testing was performed.

---

## 8. Limits of this dossier

- No web sources; tiers A/B/C = 0/0/0 by design (STATE scope). Source rows and
  candidate entries belong to the ART dossier.
- The resolver census is read, not regenerated: running `resolve.py` writes
  `citation-survival.*`, which this wave forbids. Numbers are the committed
  census's, dated by its header (r18 definition, regenerated after round 20).
- The density/median figures are from the committed r15 instrument, whose
  known limits (form sensitivity, fabricated-cite reward, duplicate inflation)
  are documented in `corpus/instruments/README.md`; they are proxies, not proof.
- Fleet MANIFEST entries were read as JSON; the last `kasegi` lane row is index
  138 by enumeration, not by a `round` field (the closure row's `round` is
  `null`).
- `kimi-shokunin` path observations were intermittent within this session;
  treat X3 as “observed twice, not characterized”, not as a deletion finding.
