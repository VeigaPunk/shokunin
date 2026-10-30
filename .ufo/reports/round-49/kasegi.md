# kasegi round 49 — citation-base grounding (C1) and the CVE Services publication surface (C2)

## Work performed

The round declared **two** claims (1–3 permitted), each on a distinct axis, each frozen before any seat ran
(`.ufo/waves/round-49/claims.json`, base `9b1662a2fa0e7c7b0ad6c4d45cb7786f27bdd03b`, freeze commit
`1954022d91c2063d0ce25bb5551778bc0b3e70f3`):

- **C1 — depth:verifiability (the lane's lowest non-retired axis, score 4):** close the class of citations
  that name a file which exists on disk but cannot be opened from the lane, and record every repair. The
  frozen counter is `corpus/instruments/citation-ground-check.py` (sha256 `988a5370…`, unchanged since the
  freeze); the declared before-value is `unresolved-class=68`.
- **C2 — coverage (8):** admit one new frontier surface — **F30, the CVE Services publication API** — backed
  by a tier-A first-party capture, a knowledge entry whose own `recheck:` line re-verifies its own declared
  source, and a registry row. The frozen counter is `corpus/instruments/frontier-recheck-count.py`; the
  declared before-value is `FRONTIER-CENSUS rows=29 admitted=29 closed=29 problem-rows=0 registry=77`.

No exploratory claim, no capability claim, no third claim. **The round's falsification arm was released
undispatched — see the wave disposition below; the claims verify on their frozen predicates and the round
files as an honest stop with its independent verification duty outstanding.**

Work items, each with an evidence pointer:

- Declared and froze the two claims, built the counter, and wrote the do-nothing control **before** any
  seat ran: `.ufo/waves/round-49/claims.json` (sha256 `c299aeaf…`), `.ufo/waves/round-49/freeze.txt`,
  `.ufo/waves/round-49/controls/do-nothing.txt` — the base tree reads `unresolved-class=68`,
  `class-lane-bare=57`, `class-fleet-relative=11`, `class-total=147`, `class-protected-blocked=79`,
  `ledger-rows=0`, exit 1.
- The frozen counter was replayed at the base export by the lane's own freeze gate:
  `python3 corpus/instruments/freeze-check.py --claims .ufo/waves/round-49/claims.json --tool-root
  /home/vgpnk/Projects/shokunin/kasegi-shokunin --base /fast/scratch/hyaku/kasegi-r49/base --work
  /fast/scratch/hyaku/kasegi-r49/freeze --timeout 900` → `claim C1 base_read=unresolved-class=68 verdict=ok`,
  `claim C2 base_read=FRONTIER-CENSUS rows=29 admitted=29 closed=29 problem-rows=0 registry=77 verdict=ok`,
  `freeze-check claims=2 base_ok=2 exit=0` (`.ufo/waves/round-49/freeze.txt`).
- Enumerated the class with the frozen counter itself and repaired it: 68 distinct citations at 109 sites
  (`.ufo/waves/round-49/apply-repairs.py`; dry run `rows=68 sites_changed=109 problems=0`), each repair
  recorded in `corpus/instruments/citation-ground-ledger.md` — 68 rows, each with its old token, its new
  token, its base class, every occurrence site (re-derived after the round's own later appends) and a
  referent note.
- Repaired the vocabulary the class exposed: `corpus/knowledge/citation-bases.md` gains a **FLEET** base
  entry (the fleet repo had no base at all, so fleet-root-relative cites had no base to be read against)
  and a round-49 amendment to rule 6 stating what a base repair is and is not (a path-prefix repair that
  keeps every line anchor and every sentence is not the rewrite rule 6 forbids).
- Opened and captured the C2 source as the L1 (rule 1: a row is written only after its source is opened in
  the round that writes the row): `corpus/source-snapshots/round-49/S078.txt` — the CVE Services API
  OpenAPI document (OpenAPI 3.0.2, `info.version` 2.8.8.1, first-party in the CVE Program's own
  repository), sha256 `1403e607cf2c5be529b9d34bad5f1ebe6b72c7673fb1de2fda79431bf1684472`, 282553 bytes,
  8374 lines — with the manifest `corpus/source-snapshots/round-49/manifest.json` (8 assertions Q1–Q8,
  each exactly-once at its pinned anchor).
- Landed the admission: `corpus/knowledge/cve-services-publication-api.md` (ground F30, source S078, the
  provenance trio, a scope-and-decision-rule paragraph, an eight-row question/ground table whose every
  quote is located, and an overlap-and-novelty section against F25 and F07), the registry row **S078**, the
  coverage-map row and the Frontier F30 row in `corpus/README.md`, and the PROVINCE.md frontier amendment.
- Closed the two routed defects the round-48 non-author closure left open, as curation outside the two
  claims: **M48-4** (the frozen battery's positive control was the pre-freeze draft) — a new **non-frozen**
  fixture file `corpus/instruments/shonen-shipped-fixtures.json` whose positive control is the shipped
  `SHONEN.md` bytes (sha256 `b1352168…`) and whose cases cover the unchecked-box-with-evidence shape, with
  the runner `corpus/instruments/shonen-shipped-fixture-check.py` (`selftest cases=5 failures=0`, exit 0);
  the frozen `fixtures.json` was **not** amended. **M48-6** (a NUL byte in an evidence pointer raised an
  uncaught `ValueError` → exit 1, a verdict-map violation) — `corpus/instruments/shonen-form.py` now maps
  `ValueError` to its registered exit 2 with the named finding `SF-UNREADABLE`; the round-48 self-test still
  reads `selftest cases=17 failures=0`, and the amendment is disclosed in the SKILL.md registry block, in
  `corpus/lessons/round-49.md` and here.
- Closed the round-48 closure's curation defect 4 (a source that was opened and then refused must land as a
  rejected row with its reason and its flip): **S079** (Bugcrowd researcher submission, status `rejected`,
  reason and flip recorded, `used-by` `—`).
- Added the round-49 QUALITY criteria R60–R64, each grounded in this round's lesson and in the closure's
  routed defects (`corpus/QUALITY.md`).
- Mined the round's mistakes into `corpus/lessons/round-49.md` § Mistakes: a stale instrument census quoted
  as current (the committed census described a 50-file corpus and a 9.05 % lane rate where the live
  instrument on the same tree read 22.81 %), the counter's own two defects caught by its self-test before the
  freeze, a past verdict read as a standing ban, the vocabulary's missing FLEET base, and the lane's own new
  text reintroducing the class it had just closed.
- **Wave disposition (honest stop):** the round built and validated its falsification arm — the 64-seat
  wave-1 spec (`.ufo/waves/round-49/wave1-spec.json`, policy v2, band 64–128, validator exit 0, 64 spawn
  seats, 31 of them attack roles: reviewer 14, critic 5, mutation-tester 12) and its rendered dispatch
  (`wave1-dispatch.json`) — and handed it over through `.ufo/waves/round-49/wave1.ready` (13:02). The
  operator's wrap-up ruling released the wave **UN-DISPATCHED**: no seat spawned, no seat report exists, no
  `wave1-results.json` was written and no WAVE-DONE message arrived. **No seat count, no role mix, no dead
  seat and no falsification credit is claimed for a wave that never ran**, and no WAVE-DONE is fabricated.
  The two claims therefore verify on their frozen predicates, re-derivable by the commands below; the
  round's independent non-author verification duty remains outstanding and is reported as such.

## Landed changes

All paths are lane-relative; every item is logged under `LOG.md` **Round 49** (`LOG.md`, the `## Round 49`
entry and the `## Round 49 — wave disposition and close` entry).

| Lane commit | Changes | Carried by |
|---|---|---|
| `1954022d91c2063d0ce25bb5551778bc0b3e70f3` | the frozen counter `corpus/instruments/citation-ground-check.py`, the regenerated base census `corpus/instruments/citation-survival.{md,tsv}`, `.ufo/waves/round-49/claims.json`, `.ufo/waves/round-49/freeze.txt`, `.ufo/waves/round-49/controls/do-nothing.txt` | this attempt (`KasegiR49`) |
| `a71cd11817c552cdc5c999cf48cc63bd64c6fb34` | the 64-seat wave spec, the rendered dispatch and the base class census (`.ufo/waves/round-49/controls/class-before.json`) | this attempt |
| `6d1aad3d59db7cccc64e48acde646e475e530da1` | the ledger's first landing, `corpus/knowledge/cve-services-publication-api.md`, `corpus/README.md` (the F30 rows), `corpus/SOURCES.md` (S078 + the round-49 search-log bullet), `corpus/QUALITY.md` (R60–R64), `corpus/lessons/round-49.md`, `PROVINCE.md`, `SCORECARD.md`, `LOG.md`, `SKILL.md` (the two registry rows), the M48-4/M48-6 closure artifacts, the regenerated census | this attempt |
| `7bfafc50220c0bfe6fed7ba0251dd19d5a528c71` | `corpus/instruments/citation-ground-ledger.md` (the re-derived sites), the S078 capture and manifest, the 21 repaired corpus files (the lessons and knowledge entries whose citations were re-grounded), the wave's ready file and wave directory | this attempt |
| `a693fce03505f1253f4c5f05af5500cc0a3ff0f8` | the wave disposition in `corpus/lessons/round-49.md`, `LOG.md` and `SCORECARD.md` | this attempt |

**Final pushed lane tip:** `a693fce03505f1253f4c5f05af5500cc0a3ff0f8` — `jj-lane.sh state` printed
`branch=master local=a693fce0… remote=a693fce0… ahead=0 behind=0 head=detached tracked=0 untracked=0`, and
the pre-report gate `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master`
prints that exact hash. The fleet-side report commit is recorded in the "Operational disposition" section.

## Before → after measurements

### C1 — depth:verifiability

**Counting command (the frozen counter, unchanged since the freeze):**
`python3 corpus/instruments/citation-ground-check.py --root TREE --fleet-root /home/vgpnk/Projects/shokunin --ledger TREE/corpus/instruments/citation-ground-ledger.md`

| | before (base `9b1662a`) | after (measured `a693fce`) |
|---|---|---|
| `unresolved-class` | **68** | **0** |
| `class-lane-bare` / `class-fleet-relative` | 57 / 11 | 0 / 0 |
| `ledger-rows` / `rows-resolving` / `findings` | 0 / 0 / 68 | 68 / 68 / 0 |
| exit code | 1 | 0 |
| `class-protected-blocked` (named debt, never repaired) | 79 | 79 |
| self-test | — | `selftest cases=10 failures=0` (exit 0) |

**The axis's own metric moved** (`corpus/instruments/resolve.py`, the committed citation-survival census,
same instrument and same scope at both ends; the base census was regenerated at the freeze commit and the
after census at the measured tip):

| | before (base `9b1662a`) | after (measured `a693fce`) |
|---|---|---|
| lane total (SKILL.md + corpus) | **1071/4696 = 22.81 %** | **1115/4758 = 23.43 %** |
| corpus alone | 1038/4307 = 24.10 % | 1090/4372 = 24.93 % |
| SKILL.md alone | 130/694 = 18.73 % | 132/701 = 18.83 % |

Of the 68 repaired rows, 49 merge into a distinct citation the corpus already carried in the opened form and
19 are fresh, which is why the numerator rises by 44 rather than by 68 (the round's own new files add
INTERNAL citations too). The isolated effect of the repair alone was also measured on two scratch exports of
the same measured commit — the tree as landed and the same tree with the repair reversed at the ledger's
sites — with `resolve.py` run over each.

**The score is held at 4, and the reason is named.** `score-gap.py` prints `gap: 22 of 68 rechecks still
gated on a lost base; score 5 needs 0 gated unsupported claims`, and `recheck-audit.py --root . --quiet`
prints `executes=46 gated=22 broken=0` — unchanged since round 46, because those 22 gated recheck lines fail
closed on the lost domain bases, which only the operator can restore. This claim therefore moves the metric
the axis counter reads (citation survival) and does not move the score-5 bar: the score is held, not
re-scored.

### C2 — coverage

**Counting command (the frozen counter):**
`python3 corpus/instruments/frontier-recheck-count.py --root TREE`

| | before (base `9b1662a`) | after (measured `a693fce`) |
|---|---|---|
| frontier census | `FRONTIER-CENSUS rows=29 admitted=29 closed=29 problem-rows=0 registry=77` | `FRONTIER-CENSUS rows=30 admitted=30 closed=30 problem-rows=0 registry=79` |
| entries | `entries=32 pass=32 exit=0` | `entries=33 pass=33 exit=0` |
| capture binding | — | `source-recheck.py --manifest corpus/source-snapshots/round-49/manifest.json --source S078` → 8/8 `OK`, exit 0; `capture-binding-check.py --root .` → `MANIFEST round-49 records=1 url_bound=1 fetched=1 archival=0`, `records=64 bound=64 unbound=0`, exit 0 |

**One disclosed difference from the frozen expectation:** the frozen `expect_after` line read
`FRONTIER-CENSUS rows=30 admitted=30 closed=30 problem-rows=0 registry=78`, and the measured line reads
`registry=79`. The cause is the rejected curation row **S079** (the round-48 closure's routed defect 4),
which was added after the freeze and is outside the claim: the claim's own predicate — one more admitted
frontier row, no problem row, the new entry's own recheck passing — holds unchanged, and the registry count
is one higher because the round also recorded the source it opened and refused. The frozen predicate was not
amended to match the measurement.

The coverage **score** is held at 8 for a reason the report states rather than hides: the coverage score's
denominator is the lost domain root's 18-surface set (0 present, 18 corpus-attested, operator-owned
re-scope), not the frontier count. A new frontier row is the lane's frontier measure, not a coverage-score
move — the same pattern as rounds 38–46.

### Non-target guards

- `SKILL.md` was edited only by the two required registry rows (the protocol's registry home is SKILL.md);
  the density instrument reports mean **267.1** over 37 blocks (round 48: 270.1 over 36) — a proxy
  movement, disclosed, and the score stays 9.
- `recheck-audit.py --root . --quiet` → `lines=68 total=68 pass=68 fail-closed=22 parse_fail=0 cwd_fail=0
  paths_fail=0` and `expect=present expected=68 missing=0 unexpected=0` (the expected-entry list was
  extended with the new entry, so the entry census closes clean).
- `anchorcheck.py SKILL.md` → `in-range=16 bad=0 lost-recorded=306 origin=0 outside-base=0 base-absent=0
  exit=0` (unchanged shape; no anchor was moved by this round).
- The frozen counter's bytes are unchanged since the freeze: sha256 `988a5370…` at `1954022d` and at the
  measured tip.

## Sources & frontier

- **Registry rows 77 → 79.** Rows added by tier: **A = 1** (S078, kind `spec`, tier A, status `mined`,
  opened 2026-10-30, recheck `90d`, used-by `corpus/knowledge/cve-services-publication-api.md`), **C = 1**
  (S079, kind `docs`, tier C, status `rejected`, opened 2026-10-30, recheck `180d`, used-by `—`). Rows
  touched old→new: **none** — no pre-existing row's `status`, `recheck` or `used-by` cell changed this
  round. Rows rejected this round: **one** (S079, the Bugcrowd researcher-submission surface, with its
  reason and its flip condition). Counting command:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 77 → 79.
- **Census before → after**, command
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  — **exit 0 at both ends**; the four W04 duplicate-URL warnings (S028, S029, S072, S076) are pre-existing
  and unchanged, and the two new rows add no warning. Before (round start): the same four warnings, then
  `kasegi ok …/corpus/SOURCES.md`, `EXIT=0`. After (round end): the same four warnings, then `kasegi ok
  …/corpus/SOURCES.md`, `CENSUS_EXIT=0` (receipt `/fast/scratch/hyaku/kasegi-r49/census-end.txt`).
- **Frontier rows advanced: 29 → 30** (F30, the CVE Services publication API). Counting command:
  `grep -cE '^\| F[0-9]+ \|' corpus/README.md` → 29 → 30, and the frozen frontier counter reads
  `FRONTIER-CENSUS rows=30 admitted=30 closed=30 problem-rows=0 registry=79`.
- **Sourced claim:** C2's evidence rests on the row **S078**, opened this round; the round's Gate block
  records the URL, the access date, the capture path and the located quote (17 words by `wc -w`,
  `S078.txt:125`), plus the seven further anchors the entry cites.
- **Search log:** one bounded-study bullet appended for this round (question, where searched, date, counts,
  stop rationale).
- **Assimilation: none.** The staged package `/home/vgpnk/Projects/shokuknow/merge/kasegi/` was **not**
  adopted: the read-only id-collision screen shows mass id drift between the package's older registry
  baseline and this lane's registry, so no staged row is appendable without wholesale renumbering, and the
  package holds no citation-base or CVE Services ground. **No staged row was appended and the campaign repo
  stayed read-only.**
- **considerthese:** not mined this round; the lane's `considerthese/` proposals ledger was not edited (the
  round's claims are the two frozen ones, and the ledger's open proposal — the end-to-end domain task —
  stays open as SHONEN box 2).

## Trend verdicts

- **expansion: improved** — one new admitted `knowledge/` entry on coverage-map ground the lane did not
  hold (the CVE Program's write path), cited to a `mined` `corpus/SOURCES.md` row (S078) opened this round,
  with its own capture, its own recheck line (8/8 located quotes) and a frontier row that advances 29 → 30.
  No capability row is claimed.
- **quality: unchanged** — no corpus entry was re-verified, deepened or superseded, and no admitted entry
  failed its re-check (`recheck-audit.py` prints `broken=0`). The round's own quality work (the M48-4 and
  M48-6 closures, the R60–R64 criteria, the vocabulary's FLEET base, the regenerated census) sits outside
  LEARNING.md's quality observable, and the density proxy moved down (270.1 → 267.1) — disclosed, not
  hidden.
- **discernment: improved** — the round-48 non-author closure's routed defects (M48-4, M48-6, the curation
  defect on the opened-then-refused source, the rule-6 tension and the vocabulary gap) each became a
  lesson-backed criterion (R60–R64) or a landed fix, and the round's own gate decisions (admit S078 and
  F30; refuse the Bugcrowd lead as a rejected row; refuse the staged package) are written down with reasons
  and flip conditions. The **first** limb of LEARNING.md's discernment test — an outside spot-check of
  **this** round's admits and rejects — is **not** met: the wave that would have carried it was released
  undispatched, so no outside verification exists for this round and the verdict rests on the second limb
  only. That is why the round files as an honest stop rather than an admitted round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author assertion;
  no named non-author verifier this round (`SKILL.md`; the two registry rows added this round).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched: no end-to-end bounty
  task ran this round; the work is source capture, citation repair and instrumentation (`LOG.md` Round 49;
  the considerthese ledger's end-to-end-domain-task proposal stays open).
- [~] Instructions executable by an agent without oral context — author assertion; the two new instruments
  are runnable and their self-tests are committed (`selftest cases=10 failures=0` for the citation-ground
  gate, `selftest cases=5 failures=0` for the shipped-fixture runner), and the ledger's shape is documented
  in `corpus/instruments/citation-reground-ledger.md`; no promotion claimed.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` gained one appended frontier
  amendment (F30, the CVE Services publication surface) and no other change; the lane still refuses live
  target testing.

## Operational disposition

Stale-lane: respawn-per-round driver; this mission progressed through the cited commits and no other kasegi
round was started by this L1. **No closure is claimed**: the round's independent non-author verification
duty is outstanding and the wave that would have carried the round's own falsification arm was released
undispatched. **Tools installed/updated: none** — the operator tooling directive at
`/home/vgpnk/.omp/agent/RULES.md` was read, and the host-wide pacman pause was respected (no pacman
transaction, no host service restart; the round needed no new tool, so no install route was required). No
target was contacted, no domain source tree was written, and the campaign repo
`/home/vgpnk/Projects/shokuknow` stayed read-only. Misroot sweep:
`git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only the unrelated `rerun-daemons.log`
(written by an invalid-args run; it names no lane and no round) — nothing of this lane's seats landed at the
fleet root, so no misroot copy was made. Scratch discipline: every scratch tree of this round lives under
`/fast/scratch/hyaku/kasegi-r49/`, and no committed artifact cites a `/tmp` path as evidence.

**Open L0 question (appended this round):** `kasegi | round-49 |` in `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`
— 79 class members sit in `round-*-verifier-spotcheck.md` and `round-*-aggregator-*.md` lessons the lane
may not edit; who re-grounds them (the aggregator that owns those files, or the operator)? The round routed
around it and reported it; the lane does not block on it.
## Post-filing correction — final lane tip (appended after the filed bytes)

The "Final pushed lane tip" line in **Landed changes** names `a693fce03505f1253f4c5f05af5500cc0a3ff0f8`, which
was the lane tip when this report was written and which remains an ancestor of the branch tip — it is
superseded only as the *tip*. One further lane commit landed after the report was filed, carrying the
round-end receipts only (no claim work, no counter byte, no score): `b329b7b453b3e6e821070cdff7d1cf25191fc237`
— `.ufo/waves/round-49/controls/census-end.txt` (source census, `CENSUS_EXIT=0`), `c1-final.txt`
(`unresolved-class=0 ledger-rows=68 rows-resolving=68 findings=0`), `c2-final.txt`
(`FRONTIER-CENSUS rows=30 admitted=30 closed=30 problem-rows=0 registry=79`) and `resolve-after.log`.
`jj-lane.sh state` prints `branch=master local=b329b7b4… remote=b329b7b4… ahead=0 behind=0 tracked=0
untracked=0`, and `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master`
prints that exact hash. The fleet-repo commit that carries this report and the L0 line is
`bdd65436eefb0e6713b583f6563adad327ed6121` (plus this correction's own commit). Every claim, measurement and
verdict above is unchanged; only the tip pointer moves.
## Erratum 1 — the isolated-repair measurement was never taken (appended after the filed bytes)

**Withdrawn text.** The C1 section in **Before → after measurements** reads: "The isolated effect of the repair
alone was also measured on two scratch exports of the same measured commit — the tree as landed and the same
tree with the repair reversed at the ledger's sites — with `resolve.py` run over each." That sentence is
**withdrawn**: the measurement was never taken. The two scratch exports were deleted while their census runs
were still in flight; the landed-tree run then failed with `FileNotFoundError`
(`/fast/scratch/hyaku/r49-after-tree.log`, exit 1) and the reversed-tree run produced no census output at all
(both scratch trees are gone). The claim was therefore written against a measurement that did not exist.

**What the round does report.** The whole-tree difference between two runs of the same instrument over the
same scope at two commits — the base commit's regenerated census (lane total 1071/4696 = 22.81 %) and the
measured tip's census (1115/4758 = 23.43 %) — plus the counter-derived arithmetic of the repair's own
contribution (49 of the 68 repaired tokens merge into a distinct citation the corpus already carried in the
opened form; 19 are fresh). The **isolated effect of the repair alone was not measured this round** and no
claim rests on it: C1's predicate is the frozen counter's `unresolved-class=68 → 0` with `ledger-rows=68`,
`rows-resolving=68`, `findings=0`, re-derivable by one command over committed bytes.

**Lane tip after this erratum.** One further lane commit carries the mined correction only (no claim work, no
counter byte, no score): `de94a3924b4cc14a7dafb08dc174cf93441e07ce` — the new § Mistakes row in
`corpus/lessons/round-49.md` and the append-only correction entry in `LOG.md`. `jj-lane.sh state` prints
`branch=master local=de94a392… remote=de94a392… ahead=0 behind=0 tracked=0 untracked=0`, and
`git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master` prints that hash. The
previous tip `b329b7b4…` (the round-end receipts commit) remains its ancestor; the earlier filed tip
`a693fce0…` and the report's first fleet commit `bdd65436…` remain on record unchanged. Every claim,
measurement, verdict and trend line in this report stands as filed, except the withdrawn sentence.
