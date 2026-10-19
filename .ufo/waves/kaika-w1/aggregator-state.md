# kaiKA W1 — fleet-root `aggregator` lane: STATE dossier

**Scope.** Read-only STATE probe of the `aggregator` lane: the fleet-root
(`/home/vgpnk/Projects/shokunin`) cross-lane quality / mint-and-dormancy /
corpus-review lane. No web research was assigned for STATE; no fix was applied.
All measurements are 2026-10-19 around 17:0x -03 on branch `master`, working
tree clean, HEAD `31baf5c` — except axis and conformance-history evidence, which
must be read at `12f2da5` because HEAD no longer contains the aggregator
SCORECARD section (§8, defect A1).

**Ground-truth caveat, read first.** At HEAD the root `SCORECARD.md` and
`LOG.md` are not the fleet files. `SCORECARD.md` line 1 is
`# kotoba-shokunin — Scorecard`; `grep -c '^## Aggregator lane' SCORECARD.md`
→ **0**, while the same command on `git show 12f2da5:SCORECARD.md` → **1**
(E6). The last good aggregator section is `12f2da5:SCORECARD.md:199-438`
(240 lines). Commit `31baf5c` ("fleet backlog commit", author
`kotodama-shokunin`, 2026-10-19T17:03:23-03:00) replaced both files
(560 SCORECARD lines / 2,201 LOG lines changed; E6). Every aggregator round
that reads the HEAD card today reads the wrong document.

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| Lane / rank | `aggregator`; main-repo L1 lane, **not** a rostered shonen (no rank row in `MANIFEST.json`) | `MISSION.md:22`; `jq '.roster\|length'` → 13, no `aggregator` |
| Domain / assigned axes | cross-lane quality, mint/dormancy calls, corpus review | `MISSION.md:22`; `shokunin.conf:21` |
| Repo / cwd | fleet root itself; **no** `aggregator-shokunin` repo exists | `ls -d ~/Projects/aggregator-shokunin` → No such file |
| Branch / HEAD | `master` / `31baf5cb0704`; tree clean (0 porcelain lines) | E1 |
| Lane git identity | `aggregator-shokunin`; **last authored commit `b159992` at 2026-09-29T01:24:49-03:00** | E19 |
| Later aggregator work | committed by `ci`: `e5efe29` (2026-10-14, r11 final re-run), `79752af` (2026-10-15, corpus-gate discovery) | E19 |
| Lane counter | `.ufo/state/aggregator.round` = **10**, mtime 2026-10-15T01:50:57-03:00 | E2 |
| Lane output marker | `.ufo/state/aggregator.out` = `Working...` (two lines); mission pid `2685182` is **dead** | E2 |
| Last completed report | `.ufo/reports/round-11/aggregator.md` (14,359 B, mtime 2026-10-14 18:50) | E4 |
| Last report at the counter path | `.ufo/reports/round-10/aggregator.md` = **187 B marker**, not a report | E4 |
| Last aggregator LOG entry | 2026-10-15 "round 10 aggregator relaunch" (`12f2da5:LOG.md:723`) | E7 |
| Fleet MANIFEST closure | last aggregator-bearing row is fleet round **12, `in-flight`**, closed 2026-09-29T01:27:10-03:00; 28 such rows total, none newer | E5 |
| Next round number | **12** recommended, not 11 | §1.1 |

### 1.1 Round-number conflict (a real collision, not a bookkeeping nicety)

Four numbers disagree:

- state counter: **10** (2026-10-15 relaunch deliberately reused 10; LOG says
  "Steered round is **10**, notwithstanding later-numbered historical entries");
- existing report path: **11** (`round-11/aggregator.md`, 14,359 B, completed
  cross-lane-quality move);
- fleet ledger: last aggregator row **12 `in-flight`** (2026-09-29), never closed;
- prompt files exist through `aggregator-round-12.md`.

The relaunch's own contract is to write `.ufo/reports/round-10/aggregator.md`;
that path currently holds a 187-byte marker, so a real round-10 report would be
a repair. But the watchdog's next increment (11) would target the path holding
the historical r11 report — the exact marker-overwrite class D-153 and
`cross-lane-gate` exist to catch. **Do not advance to 11 blindly.** Complete
round 10 at its own path, then reconcile the counter to 12 and record why 11 is
skipped; alternatively declare a new namespace as the other lanes did, but
record it in the ledger. No fix is applied here.

---

## 2. Axes

Scores are the last recorded values in `12f2da5:SCORECARD.md` (aggregator
section); evaluator: report `.ufo/reports/round-11/aggregator.md` plus its
"final training-round re-run" section.

| Axis | Score | Evidence pointer | Last change |
|---|---:|---|---|
| corpus review | **9** | gate `corpus-gate-v1` self-test 12/12; six corpora re-emitted `not conformant` at named revisions; kama's first verdict also not conformant (3/5 lessons lack commit/report pointer) | round 9, re-run round 11 |
| cross-lane quality | **9** | `cross-lane-gate-v1`: 46 presented reports graded; 5 marker-overwrite, 2 verdict-without-revision, 110 cited-commit-missing; self-test 6/6 | round 11 final training re-run |
| mint/dormancy calls | **9** | lifecycle census `type=="mint"` finds 1 (then); kama probation without roster promotion; 8/8 dormancy rows with per-repo LOG grammar; **0/8 dormant** | round 11 |

**Lowest non-retired axis.** All three are tied at 9; there is no lower axis.
Selection is by *unpaid duty*, which the round-10 relaunch already used: corpus
review carries 0/21 conformant verdicts, 0/21 `corpus/SOURCES.md` registries,
and 596/683 knowledge entries missing the required `source:` field (§6). Round
10's selected move — replace the fixed six-lane corpus list with physical
discovery — did land in `79752af` (`corpus-gate.mjs` +116 lines; live discovery
now selects 21 lanes), but its report never landed and the counter did not
advance. That move is **not** available as a new claim; its evidence is already
committed.

**Saturation line.** None declared in the aggregator section (only `grep -ci
saturat` → 2, both the phrase "not saturated"). This is a contract gap: every
lane is required to record a saturation line and stagnation window
(`AXES.md` §SCORECARD.md contract). Proposal: declare **9.5** for the three
axes — band 9 is "machine-checked/externally audited", band 10 is "repeated
non-author verification in the opposite direction"; both existing gates are
re-runnable by a non-author but their verdicts have not been re-run in the
opposite direction across rounds. Do not retire any axis: no saturation evidence,
and mint/dormancy still lacks a positive dormancy case.

**Capabilities.** The aggregator section contains **0 capability rows** — the
root `Capabilities` table at `12f2da5:SCORECARD.md:118` sits above the
aggregator header (line 199) and belongs to the protocol lane. The instruments
`corpus-gate-v1` and `cross-lane-gate-v1` were demonstrated in rounds 9/11 but
were never entered as capability rows. This is why the sources census (§10) has
no table to enter yet: the table must first be restored under the aggregator
section.

**Planned claims.** The section's only `### Planned` item is "round 12 —
cross-lane quality (lowest at 8)", already superseded by the round-11 final
re-run that landed 8→9. The round-10 relaunch section adds the discovery move,
which landed at `79752af` without a report. There is therefore **no current,
unconsumed planned claim**. A new round must write its claims before starting.

---

## 3. Per-repo conformance verdict practice

### 3.1 Contract

`CORPUS.md:60`: "**Each round's review emits a verdict per repo** — `conformant`
or `not conformant`, naming the failed rule and the command that shows it."
Combined with `PROTOCOL.md:311` ("reviews every child repo's `corpus/` each
round") and the gate standard (`PROTOCOL.md:360`), the practice is:

1. run the committed `corpus-gate-v1` over discovered physical lanes;
2. for each lane emit `# verdict <repo> <clean|failed> findings=N rules=...`
   at a **named revision** (and `dirty=N`);
3. route failures into the append-only ledger queue (`.ufo/reports/AGGREGATE.md`,
   `D-` rows), not into silent rewrites;
4. mirror only aggregator-owned lessons into the child corpus, committed by the
   aggregator at creation time (`PROTOCOL.md:311`).

### 3.2 Instrument

`node .ufo/waves/round-9/corpus-gate.mjs` (`corpus-gate-v1`; tracked; the round-10
discovery change landed in `79752af`).

- Verdict map: `0 clean`, `1 failed`, `2 could-not-evaluate`, `3 frozen drift`;
  precedence `2 > 3 > 1 > 0`.
- Self-test: **12/12 PASS** (run today, exit 0; fixtures in `os.tmpdir()`,
  live tree untouched; E8).
- Frozen snapshots: `--snapshot <repo> <commit>` via `git archive`; expected
  JSON pins self-test cases and frozen digests.
- Implemented checks: `r2` lesson cites round/evidence; `r4` count without a
  backticked command; `r7` index row names an absent path; `r8` credential
  material on literal text (occurrence unit, `op://` included, classification
  `could-not-evaluate`); `r10` missing aggregator lesson; `shonen` canonical form.
- Declared **not evaluated** (with reasons, not faked): `r1` source-token
  semantics, `r3` falsifiability, `r5` negative-claim sweep, `r6` quote location,
  `r9` append-only/authorship, and box-3 non-author provenance. This is the
  honest ceiling of "mechanical conformance".

### 3.3 Current verdicts (live worktrees, 2026-10-19)

`node .ufo/waves/round-9/corpus-gate.mjs --all` → exit **1**; discovery selected
**21** physical lanes; **21/21 failed**, **1,374 findings** total (E8). No
`conformant` verdict exists in this run; the ledger's historical rows (rounds
9/11) likewise record 0/6 and 0/7 conformant.

| Lane | Findings | Lane | Findings | Lane | Findings |
|---|---:|---|---:|---|---:|
| audio | 19 | kaidoku | 88 | revenger | 2 |
| chousa | 64 | kake | 47 | souji | 13 |
| game-dev-2d | 28 | kama | 16 | tabi | 163 |
| game-dev-3d | 42 | kasegi | 55 | tameshi | 79 |
| kagi | 63 | kengaku | 70 | tsukuroi | 93 |
| kotoba | 94 | kotodama | 197 | | |
| kumitate | 107 | lore | 15 | | |
| mado | 80 | mori | 39 | | |

Three lanes are graded **provisional** because their live worktree differs from
the cited revision (`dirty=1`; E8/E15):
`game-dev-3d` (`?? reports/round-107/`), `kama` (`?? .ufo/round-10/`), `lore`
(`?? .scratch/`). A provisional result must never be recorded as a frozen
verdict.

### 3.4 Practice gaps

- **Registry home gone.** `PROTOCOL.md:360` makes the aggregator's registry home
  "inside its own section" of root `SCORECARD.md`; that section is absent at
  HEAD (§8 A1). The gate's own header already records the older gap ("the
  aggregator lane HAS NO SKILL.md … routed defect, D-120 class"). Gate Delivery
  cannot be graded conformant until the section is restored.
- **Revision discipline.** The gate names revisions and dirty counts; the ledger
  sometimes cited worktree results. Round 11 explicitly refused to call kama's
  first verdict frozen until the tree was committed — that is the correct
  practice and must survive.
- **Scope.** `corpus-gate` grades corpus rules, not `SKILL.md`/`PROVINCE.md`
  claims. The aggregator's cross-lane quality gate grades report durability, not
  report truth. Neither instrument substitutes for the other.
- **Zero conformant is the signal, not a failure of the gate.** All 21 lanes
  failing is consistent with the ledger's directional claim; the census is a
  baseline, not evidence of the aggregator's inability to grade.

---

## 4. Dormancy flags

### 4.1 The aggregator itself is dormant in practice

| Signal | Evidence |
|---|---|
| Counter frozen at 10 | `.ufo/state/aggregator.round` = 10, mtime 2026-10-15T01:50:57-03:00 (E2) |
| Output never replaced | `.out` = `Working...`; pid `2685182` not alive (E2) |
| Watchdog failed twice | `lane-round-failed aggregator round=10 :: marker/contentless report; NOT advancing` at 2026-10-15T01:45:42 and 01:50:57; each followed by a relaunch; no `complete aggregator round=10` line (E3) |
| Last report | round-11 report (2026-10-14); the counter-10 path holds a 187 B marker (E4) |
| Last authored commit | `b159992`, 2026-09-29; later work authored `ci` (E19) |
| Fleet ledger | last aggregator row fleet round 12 `in-flight`, 2026-09-29; no newer row (E5) |
| Driver | watchdog last tick 2026-10-15T01:58:27; no later ticks (E3) |

This is a **failed-round loop**, not a clean stop: the driver could not advance
because the report at the counter path was a marker, and the lane has not filed
a real round-10 report. The lane is dormant for four days (2026-10-15 →
2026-10-19).

### 4.2 The fleet dormancy rule has never had a positive case

Rule (`PROTOCOL.md:55`): "Two consecutive dispatched-and-reported rounds with no
`LOG.md` activity flag a shonen dormant". Historical round-11 table:
**0/8 dormant under reading A** (both pair rounds silent required); **1/8
(kengaku) under reading B** (latest pair round silent suffices). No operator
ruling exists between the readings, so a dormancy call today would be
unadjudicable. Additional unresolved inputs:

- **Marker exclusion** decides kengaku: excluding its 274 B r12 marker yields
  pair r13+r11 (only B fires); counting it yields r13+r12 (both readings fire).
- **Province loss is invisible** to the predicate: kasegi's province root
  `~/Projects/bounties` vanished, yet its LOG cadence keeps it `ACTIVE`.
- **Probation precedence** is undefined: a probation lane (kama) that goes
  silent is neither clearly dormant nor a failed probation.
- **LOG grammar is per-repo**: five lanes use date bullets, kotoba title-case
  headings, kama lowercase headings; a single matcher is 0/6 correct.
- **State counters are unusable as a current dispatch signal**: they are frozen
  at 2026-10-15 while fleet reports exist through round 104 and local reports
  through round ~307. E.g. `audio` counter 1 / last fleet report 76; `lore` 1 /
  102; `kumitate` 18 / 32; `kotodama` empty / 48; `aggregator` 10 / 11 (E10).

### 4.3 Fleet report-path compliance

Six physical lanes have **zero** reports at the contract path
`.ufo/reports/round-<N>/<lane>.md`: `chousa`, `mado`, `revenger`, `tabi`,
`tameshi`, `tsukuroi` (E10). Some have lane-local `reports/` or `.ufo/` round
dirs, but the protocol's "dispatched-and-reported" evidence is the fleet path
(`PROTOCOL.md` report contract). A dormancy sweep that scans only the fleet path
would miscount them; one that scans only lane-local paths would violate the
contract. **No lane is called dormant in this dossier** — the evidence base is
stale and the two readings disagree.

**Historical claims to preserve.** Round 11's 8-row table is the last complete
sweep: kasegi/kake/kumitate/kagi ACTIVE, kengaku/kotoba ACTIVE-watch, kama
ACTIVE-insufficient-history, aggregator ACTIVE (r9+r8 pair). Do not upgrade
those rows into a current claim without a new sweep.

---

## 5. Mint calls

| Metric | Value | Command / evidence |
|---|---:|---|
| Physical lanes | **21** | `find . -maxdepth 1 -type d -name '*-shokunin' \| wc -l` |
| Roster ids | **13** | `jq '.roster\|length' MANIFEST.json` |
| Lifecycle mint rows (`type=="mint"`) | **10** | `jq '[.rounds[]\|select(.type=="mint")]\|length'` (E11) |
| Roster additions since r11 | **+7**: kama, audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku | roster minted dates: kama 2026-09-29; five 2026-10-11; kaidoku 2026-10-13 (E11) |
| Unrostered physical lanes | **8**: chousa, kotodama, mado, mori, souji, tabi, tameshi, tsukuroi | `comm` set difference (E11) |

**The ledger and the roster are not the same population.** Ten typed mint rows
exist:

- kama (11.5, probation) and kaidoku are **rostered**;
- eight are **not rostered** (notes say "Probation >=3 verified rounds; roster
  row withheld"): chousa, kotodama, mado, mori, souji, tabi, tameshi, tsukuroi;
- five rostered lanes have **no `type=="mint"` row** at all: audio,
  game-dev-2d, game-dev-3d, lore, revenger (roster says minted 2026-10-11).

The round-11 census (`sum(type=="mint")` → 1) was correct at its cutoff; it is
now **10**, and no aggregator round has adjudicated any of the nine later mints,
the seven roster additions, or kama's roster promotion (roster row dated
2026-09-29 while r11 said promotion was withheld for two more verified rounds).
The `minted` array is still vestigial (0 truthy), which is why the unit-predicate
lesson matters (`M7`, self-defect 27).

**Score impact.** Mint/dormancy stays **9**, not 10: the lifecycle census can
now observe positives, but (a) the ledger has no positive dormancy case, (b) the
roster/mint populations contradict each other, and (c) no round has recorded the
promotion evidence for kama or the seven additions. A band-10 claim would need
repeated non-author verification of a reconciled lifecycle, not a higher count.

**Candidate table status.** The round-11 candidate calls (kessho below bar,
umihotaru below bar, kagemusha below bar, axis-framework stewardship below bar,
filesystem custody WATCH) are **stale** — nine mints and the roster changes
happened after them. Re-test before repeating any call; do not copy them into a
new report as current.

---

## 6. Corpus census

### 6.1 The aggregator's own ledger (its "corpus")

| Metric | Value | Command |
|---|---:|---|
| canonical ledger | `.ufo/reports/AGGREGATE.md` | `test -f` |
| size / lines | 244,780 B / 2,132 lines | `wc -lc` |
| top-level refresh sections | 15 `## ` | `grep -c '^## '` |
| routed rows | 165 `D-` rows; max **D-155** | `grep -cE '^\| D-[0-9]+'`; sort tail |
| last refresh | §15 (round-11 audit), 2026-09-29 | `grep -n '^## 15'` |
| L0 side channel | 51 lines, unclassified since round 11 (last classification was 15 open / 3 superseded / 1 answered-by-event on 20 lines) | `wc -l .ufo/l0-questions.md` |

No new `D-` row has been filed since round 11 despite the defects in §8 (root
file replacement, state counters, six missing fleet reports, corpus metadata
regression). The ledger is stale by four days and one fleet widening (6 → 21
lanes).

### 6.2 Fleet corpora it reviews

Scoped to the 21 lane repos (not `.tower` copies or other host repos):

| Surface | Value | Command |
|---|---:|---|
| `corpus/` dirs | 21 / 21 | `find . -maxdepth 2 -type d -name corpus` |
| `corpus/README.md` | 19 / 21 (audio, revenger absent) | E13 |
| `corpus/QUALITY.md` | **10 / 21** | `ls *-shokunin/corpus/QUALITY.md \| wc -l` |
| `corpus/SOURCES.md` | **0 / 21** | `ls *-shokunin/corpus/SOURCES.md 2>/dev/null \| wc -l` |
| knowledge files | **683** | Python lane-scoped scan (E12) |
| lesson files | **540** | same scan |
| `## Frontier` sections | **7 / 21** (chousa, kaidoku, kake, kama, mado, tabi, tsukuroi) | E13 |
| frontier bullet rows | 30 (chousa's section is prose, 0 bullets) | E13 |
| README table rows (coverage-map proxy) | 620 | E13 |
| `SKILL.md` | 18 / 21 (missing audio, game-dev-2d, revenger) | E14 |
| `PROVINCE.md` | 21 / 21 | E14 |

### 6.3 Required metadata is mostly absent

The corpus contract says each `knowledge/` entry opens with `source:`,
`verified-at:`, `recheck:` (`CORPUS.md` §Layout). Measured over the 683
lane-scoped knowledge files:

- **87 / 683** carry `source:` (596 missing);
- **81 / 683** carry `verified-at:` (602 missing);
- **87 / 683** carry `recheck:` (596 missing);
- **0** carry an explicit absolute overdue date; the 87 `recheck:` values are
  heterogeneous prose/commands/cadence (`recheck:` empty, `bash tools/...`,
  "§7.", etc.), so **overdue is not computable** — 0 overdue is "unmeasured",
  not "none".

Worst lanes: `kotodama` 224/224 missing all three; `kaidoku` 72/90 missing
source; `audio` 14/14; `game-dev-3d` 26/26; `kumitate` 38/38; `kasegi` 25/25;
`kengaku` 27/27; `tabi` 24/26. Best: `chousa` 24/24 compliant. This is the
strongest argument for the sources census: the fleet currently has a corpus
contract that most entries do not satisfy, and no instrument that measures it.

`QUALITY.md` exists in only 10 lanes and the formats are not comparable:
`chousa` / `mado` / `mori` / `tabi` / `tameshi` / `tsukuroi` / `kotodama` use
five numbered criteria; `kaidoku` uses a 15+ row table; `kama` uses a
`KQ1…KQ5` table. A fleet-wide "criteria count" is therefore not defined — a
census that compares lanes must first declare the unit. `kaidoku`'s bar is the
strongest observed (each criterion cites the lesson that produced it and names
supersession). This heterogeneity is a wave-2 D3 concern, not something the
aggregator can grade mechanically today.

---

## 7. Mistakes mined (rejected / harmed / honest stops / errata / disagreements)

The aggregator has no `QUALITY.md` and no `SKILL.md`; the fleet `CORPUS.md`
rules are the only applicable bar. Cumulative self-defects recorded through
round 11: **29** (`AGGREGATE.md` §14.12, §15.7).

| # | Class | Evidence pointer | Existing rule? | Proposed criterion if none |
|---|---|---|---|---|
| M1 | Predicate cannot turn positive (mint census keyed to empty `minted` array) | self-defects 27–28; §15.2; corrected query `type=="mint"` | `CORPUS.md:33` count-carries-command covers the *number*, not the predicate | **C-A** Every census predicate ships a fixture that can turn positive; a predicate with no positive fixture is `unprovable`, not zero |
| M2 | Unreproducible published metrics (115→99, 28→17, 30→uncountable, 41→unreproducible) | round-8 report, repaired in place at round 10 (D-129) | `CORPUS.md:33` count-carries-command — the repair was the rule working | — |
| M3 | Negative claim without a sweep ("rule 8 clean everywhere"; "no mint record") | self-defect 20; self-defect 28 | `CORPUS.md:38` negative-claim-carries-sweep | — (rule already covers; the failure was not applying it to the lane's own mirrors) |
| M4 | Evidence not committed (round-8 wave absent; transcripts session-scoped) | self-defect 21 | `PROTOCOL.md` report evidence standard; gate standard "two evidences" | **C-B** A finding cites only committed evidence; an uncommitted seat is not evidence |
| M5 | One grammar assumed for many repos (dormancy LOG matcher 0/6) | self-defect 29; dormancy table §5 | none | **C-C** A sweep names every member's grammar and tests the matcher on each before verdicts |
| M6 | Marker overwrote a real report (kotoba r15, 14,715 B→273 B; 5 live instances) | D-153; `cross-lane-gate-v1` 5 marker findings today | `PROTOCOL.md` marker clause; gate exists | **C-D** Promote report-byte durability to the protocol closure check, not just a lane gate |
| M7 | Axis switched away from `### Planned` without amending it | self-defect 26 | none | **C-E** Amend `### Planned` before switching; record the reason in the round report |
| M8 | Round-10 relaunch landed work (`79752af`) but filed no report; watchdog looped on the marker | E3/E4 | report contract; marker clause | **C-F** A relaunch that reuses a round number must also repair the counter-path report; otherwise the round is `failed` by construction |
| M9 | Root shared file replaced wholesale (aggregator section deleted; LOG lost) | §8 A1; `31baf5c` | none — `CORPUS.md:52` covers corrections in child corpora, not root shared files | **C-G** A shared SCORECARD/LOG section is append-only custody; whole-file replacement is a conformance defect and a gate must detect section loss |
| M10 | Lane identity drift: later aggregator work committed by `ci`, not `aggregator-shokunin` | `b159992` (Sep 29) vs `e5efe29`/`79752af` (`ci`) | `PROTOCOL.md:311` says aggregator commits its own files under its own subject | **C-H** A main-repo lane's report/ledger commit carries the lane identity; `ci` commits are integrations, not lane evidence |

**Honest stops and rejected moves to preserve.**

- Round 5 and round 10 each filed a marker (254 B / 187 B); both are **failed**,
  excluded from dispatched-and-reported pairs. Do not count them as rounds.
- Round 11's final training re-run explicitly says it "executed as one seat" and
  the ≥8-L2 wave was not re-dispatched; that is recorded, not hidden. The next
  round must dispatch the required batch or record a waiver.
- No axis has been retired. The corpus-verdict split proposals remain deferred.
  The round-10 relaunch's numeric corpus score remained 9 by declaration; do not
  retroactively claim a raise for the discovery move.
- Gate disagreements kept verbatim: kengaku r13's marker/ok conjunction is
  `could-not-evaluate` (a human ruling is needed); kasegi/kake cited external
  commits are unresolved (`cat-file` fails in-repo); kama's probation vs
  dormancy precedence is undefined; reading A vs B changes the fleet dormant
  count 0↔1. These are not failures to hide — they are the limits of the rule.

---

## 8. Contract defects (report paths; nothing touched)

| # | Sev | Defect | Evidence / command | Impact |
|---|---|---|---|---|
| A1 | **P0** | Root `SCORECARD.md` and `LOG.md` replaced by kotoba-lane content at `31baf5c`; aggregator section absent | `head -1 SCORECARD.md` → `# kotoba-shokunin — Scorecard`; `grep -c '^## Aggregator lane' SCORECARD.md` → 0; `git show 12f2da5:SCORECARD.md \| grep -c` → 1; `31baf5c` stat 560/2,201 lines | Every aggregator round contract (axes, planned, saturation, capabilities, registry home) has no valid file; report closure would fail |
| A2 | **P0** | Registry home for `corpus-gate-v1`/`cross-lane-gate-v1` is gone | `PROTOCOL.md:360`: aggregator registry home is inside its own section | Gate Delivery cannot be graded conformant; D-120 class widens |
| A3 | **P1** | Lane dormant / failed-round loop | §4.1; watchdog two `lane-round-failed` lines; dead pid 2685182 | No round advances; report path stuck |
| A4 | **P1** | `.ufo/state/*.round` stale vs reports (frozen 2026-10-15) | audio 1/76, lore 1/102, kumitate 18/32, kotodama empty/48, aggregator 10/11 (E10) | Any dormancy/round call from state is wrong |
| A5 | **P1** | Aggregator has 0 capability rows, no saturation line, no current planned claim | §2; `/tmp/agg-section.txt` (`grep -ci capabilit` → 1, only "no new capability") | Cannot satisfy `AXES.md` §Capabilities/§SCORECARD contract |
| A6 | **P1** | 2 of 9 aggregator reports are markers (r5 254 B, r10 187 B) | E4 | 22% of the lane's report history is not evidence |
| A7 | **P1** | Six lanes have 0 reports at the contract path | chousa, mado, revenger, tabi, tameshi, tsukuroi (E10) | Dormancy rule input is missing for 29% of physical lanes |
| A8 | **P1** | Corpus metadata non-compliance 87/683 | E12 | Corpus contract is unenforced; rule 1 is declared not-evaluated |
| A9 | **P2** | `corpus/QUALITY.md` only 10/21; `SOURCES.md` 0/21; `## Frontier` only 7/21 | E13 | Wave 2 D1/D3 has no uniform landing surface |
| A10 | **P2** | Mint/roster populations contradict (5 roster rows without mint rows; 8 mint rows unrostered) | §5; E11 | Mint census cannot be used as a lifecycle measure |
| A11 | **P2** | Fleet ledger's last aggregator row is r12 `in-flight` since 2026-09-29 | E5 | Closure debt sits unresolved for 20 days |
| A12 | **P2** | No `SKILL.md` / `PROVINCE.md` / `corpus/` / `SHONEN.md` for the aggregator; D-120 open | `ls` at root; `AGGREGATE.md:1468` | Main-repo lane cannot satisfy child-repo file contract as written |
| A13 | **P2** | Lane-authored identity stopped 2026-09-29; work since is `ci` | E19 | Custody/authorship evidence is weaker than the protocol expects |
| A14 | **P2** | L0 has 51 lines, unclassified since round 11; new aggregator r10 custody question appended | `wc -l`; tails (E9) | Operator decisions are invisible to the queue |
| A15 | **P3** | Bloat: `AGGREGATE.md` 244,780 B; 2,132 lines; `.tower` duplicates outside scope | `wc -lc` | Slower reviews; not a correctness defect |
| A16 | **P3** | `scripts/sources-census.sh` absent; `scripts/` has only `shokunin-watchdog.sh` | `ls scripts/` | D4 has no implementation yet |
| A17 | **P3** | Three lanes dirty/provisional | game-dev-3d `reports/round-107/`, kama `.ufo/round-10/`, lore `.scratch/` | Their verdicts cannot be frozen |
| A18 | **P3** | No current primary for OVERDUE recheck: `recheck:` is prose/cadence, not a date | E12 sample | Cannot honor the `recheck:` contract mechanically |

**Uncommitted changes:** root tree is clean (0 porcelain lines). The three child
lanes above have untracked dirs; they are reported, not touched.

---

## 9. Proposed round (1–3 claims, distinct axes)

All three axes tie at 9; each claim below is on a lowest non-retired axis.
Recommended order: **A first** (it restores the file every later claim must
write), then **B**, then **C**. The round must dispatch the required L2 batch
(≥8, one call) or record the waiver; the round-11 final re-run's one-seat shape
is not a precedent for a normal round.

### Claim A — calibration: restore record custody and make section loss detectable

- **Before:** `grep -c '^## Aggregator lane' SCORECARD.md` → **0**; the HEAD
  card is kotoba's; no gate detects a whole-file replacement of a shared
  section.
- **After:** section restored from `12f2da5` with a dated erratum (scores
  9/9/9, capabilities table incl. the two existing gates, saturation line,
  planned block), protocol-lane bytes byte-identical; `cross-lane-gate` gains a
  `shared-file-section-loss` check with a fixture that plants `31baf5c`'s
  replacement and fails naming the commit.
- **Counting command:** `grep -c '^## Aggregator lane' SCORECARD.md` 0→1;
  `node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --selftest` → N/N
  including the new fixture; `--all` → 1 finding naming `31baf5c`.
- **Falsifier:** section absent; protocol bytes changed; gate passes the
  replacement fixture; or the check cannot distinguish `12f2da5` from HEAD.

### Claim B — corpus review: land and demonstrate the fleet sources census

- **Before:** `corpus/SOURCES.md` → **0/21**; knowledge `source:` coverage
  **87/683**; no instrument aggregates or validates a source registry.
- **After:** D4 `scripts/sources-census.sh` (if D4 lands; otherwise the claim is
  blocked, not faked) runs over all 21 physical lanes, emits one fleet index and
  per-lane verdicts at named revisions, and passes a self-test covering:
  malformed row, reused `S###`, missing field, `|` in a cell, overdue explicit
  date, overdue cadence (opened+recheck), shared source across lanes (index, not
  failure), `used-by` dead pointer, `supersedes` missing target. Demonstrated on
  the 21 D1 registries; first capability row enters the restored aggregator
  table.
- **Counting command:** `ls *-shokunin/corpus/SOURCES.md | wc -l` 0→21;
  `bash scripts/sources-census.sh --selftest` → N/N; `--all` → exit 0 or 1 with
  per-lane rows; `grep -c '^| S[0-9]{3} ' **/corpus/SOURCES.md` sums the fleet.
- **Falsifier:** a planted malformed row / overdue date / shared source is not
  detected; the census writes outside tmp/report paths; a lane's rows are not
  the rows the lane opened; or the capability row is entered without a run.

### Claim C — mint/dormancy: reconcile the two populations and re-run dormancy

- **Before:** 10 typed mints, 13 roster ids, 21 physical lanes; 5 rostered with
  no mint row; 8 minted but unrostered; last dormancy sweep 2026-09-29; no
  current dormancy table.
- **After:** a 21-row lifecycle table (lane, roster?, typed mint?, probation
  rounds with evidence, last report at contract path, dormancy verdict under
  both readings) with every cell carrying its command; at least one named
  discrepancy resolved by an appended ledger row (never an in-place roster
  edit); kama's promotion evidence recorded or the roster row flagged.
- **Counting command:** `jq '[.rounds[]|select(.type=="mint")]|length'` 10;
  roster 13; physical 21; reconciliation rows 21/21; dormancy rows 21/21
  (0 or more dormant under each reading, named).
- **Falsifier:** any cell lacks a command; a status contradicts `MANIFEST.json`;
  a dormancy verdict lacks two dispatched-and-reported rounds; or a probation
  lane is promoted without three verified rounds.

**Score verdicts to record (do not pre-claim):** A `calibration` 9→9 (record
integrity restored; gate coverage grows) or 9.5 only if a non-author re-runs the
new fixture; B `corpus review` 9→9 (capability row; 0/21 conformant remains) or
9.5 only if the census closes a previously not-evaluated rule class and a
non-author re-runs it; C `mint/dormancy` 9→9 (no positive dormancy case). A
round is admitted only if every claim verifies and no axis is harmed.

---

## 10. How the fleet sources census becomes an aggregator capability

`local://kaika-plan.md:40` defines D4: "aggregates lane SOURCES.md into a fleet
index, flags malformed rows, overdue rechecks, sources shared across lanes;
self-test." Today the script does not exist (`scripts/` has one file, A16) and
no lane has `corpus/SOURCES.md` (0/21). The path from D4 to a capability row:

1. **Restore the home.** `PROTOCOL.md:360` puts the aggregator's gate registry
   inside its own root SCORECARD section; that section is missing (A1/A2).
   Claim A restores it. Do not create a third registry path.
2. **Shape it as a gate, not a report.** `PROTOCOL.md:360` defines a gate as
   "a committed, re-runnable verdict script a lane owns", with a declared exit
   map, a self-test over isolated fixtures asserting exit code **and** a stable
   finding id, committed expected values, a frozen snapshot, and a revision
   named in every verdict. Mirror `corpus-gate-v1`:
   - entry: `bash scripts/sources-census.sh --all` (discovery of the 21
     physical `*-shokunin` dirs, sorted, nonrecursive), `--repo <lane>`,
     `--snapshot <lane> <commit>` via `git archive`, `--selftest`;
   - verdict map `0 clean / 1 failed / 2 could-not-evaluate` (missing/unreadable
     registry, git failure, empty discovery) `/ 3 frozen drift`; precedence
     `2 > 3 > 1 > 0`;
   - findings `SRC-<lane>-<class>-<n>` in a deterministic order; classes from
     the SOURCES contract: malformed row, `S###` reuse, missing required field,
     `|` in a cell, invalid kind/tier/status, overdue explicit date, overdue
     cadence, `supersedes` target absent, `used-by` path unresolved; shared
     source is an **index row**, not a failure;
   - fleet index output is pointers only (never copied expected values), per the
     gate standard; no network, no live-target contact — URL liveness is
     declared `not-evaluated` (the census checks the registry, not the web).
3. **Demonstrate it in a round.** `AXES.md:57`: "Rows enter only through a round
   that demonstrates the capability running." The round report must carry the
   live invocation, the self-test tally, and the first-working round number.
   The row shape for the restored table:

   | Capability | What it can now do | Evidence pointer | First-working round |
   |---|---|---|---|
   | fleet sources census | aggregates all 21 lanes' `corpus/SOURCES.md` into one pointer index, emits per-lane source verdicts at named revisions, and fails closed on malformed rows / overdue rechecks / dead `used-by` pointers; shared sources are indexed for adjacency | `bash scripts/sources-census.sh --all` + `--selftest`; index path | the round that runs it |

4. **Attach the axis verdict.** The census is a **corpus-review capability**
   (it governs source registries, a corpus surface), not a new axis. Conservative
   verdict: corpus review 9→9; the capability row is the deliverable. If the
   round also proves the census closes a rule-1 class that the corpus gate
   declares not-evaluated, and a non-author re-runs it, record 9→9.5 with that
   evidence. Never claim 10: repeated opposite-direction non-author verification
   is the band-10 criterion.
5. **Feed the other duties.** The index makes shared sources visible to the
   adjacency practice, and a lane with zero valid sources becomes a
   dormancy/mint input (a lane whose sources are all rejected is not a living
   province). That does not authorize an automatic dormancy call — the rule
   still requires two dispatched-and-reported rounds.

**Why the aggregator owns it.** It is the only lane with the cross-repo corpus
write exception (`PROTOCOL.md:311`), it already owns the rule-10 per-repo verdict
practice and the canonical ledger, and its root section is the declared registry
home for main-repo gates. A child lane owning the fleet index would duplicate the
aggregator's review duty and violate the "one domain" boundary.

---

## 11. STATE checklist mapping

| Dossier item | Section |
|---|---|
| 1 Identity | §1 (incl. round conflict §1.1) |
| 2 Axes | §2 |
| 3 Corpus | §6 (plus §3 for verdict practice) |
| 4 Mistakes | §7 |
| 5 Contract defects | §8 |
| 6 Proposed round | §9 |
| Assignment add-ons: verdict practice / dormancy / census capability | §3, §4, §10 |

---

## 12. Evidence block

Commands were run read-only from the fleet root; gate stdout was captured in
`/tmp/kaika-census-gate.txt` and `/tmp/kaika-cross-gate.txt` (transient, outside
the repo). `12f2da5` is HEAD~1 and the last commit whose root SCORECARD carries
the aggregator section.

| ID | Command | Observed |
|---|---|---|
| E1 | `git branch --show-current; git rev-parse --short=12 HEAD; git status --porcelain \| wc -l` | `master`; `31baf5cb0704`; `0` |
| E2 | `cat .ufo/state/aggregator.{round,out,mission}; ps -p 2685182` | `10`; `Working...` ×2; `2685182`; `ps` header only (dead) |
| E3 | `grep ' aggregator ' .ufo/watchdog.log \| tail -6; tail -2 .ufo/watchdog.log` | two `lane-round-failed … marker/contentless report; NOT advancing` at 01:45:42/01:50:57; last `tick=2` 01:58:27 |
| E4 | `find .ufo/reports -path '*/round-*/aggregator.md' -printf '%p %s\n' \| sort -V` | 9 files; r5=254 B, r10=187 B, r11=14,359 B |
| E5 | `jq -r '.rounds[]\|select((.lanes//{})\|has("aggregator"))\|[.round,.type,.lanes.aggregator]\|@tsv' MANIFEST.json \| tail -3` | last: `12 closure-correction in-flight` |
| E6 | `head -1 SCORECARD.md; grep -c '^## Aggregator lane' SCORECARD.md; git show 12f2da5:SCORECARD.md \| grep -c '^## Aggregator lane'` | kotoba header; `0`; `1` |
| E7 | `git show 12f2da5:LOG.md \| grep -nE '^## .*aggregator\|round 1[01]' \| tail` | aggregator entries at 62/115/213/324/406/529; relaunch at 723 |
| E8 | `node .ufo/waves/round-9/corpus-gate.mjs --selftest; node … --all` | `12/12 PASS` exit 0; `--all` exit 1, 21 discovered, 1,374 findings, 21 failed |
| E9 | `wc -l .ufo/l0-questions.md; tail -2 .ufo/l0-questions.md` | 51 lines; aggregator round-10 custody question present |
| E10 | `for l in …; do printf '%s %s %s\n' "$l" "$(cat .ufo/state/$l.round)" "$(find .ufo/reports -path "*/round-*/$l.md" \| wc -l)"; done` | audio 1/13, chousa 1/0, lore 1/16, kotodama —/39, mado 1/0, revenger 1/0, tabi 1/0, tameshi 1/0, tsukuroi 1/0, aggregator 10/9 |
| E11 | `jq '.roster\|length'; jq '[.rounds[]\|select(.type=="mint")]\|length'; comm -23 <(…22 dirs…) <(jq -r '.roster[].id' …)` | 13; 10; 8 unrostered |
| E12 | Python lane-scoped scan of `*/corpus/knowledge/**/*.md` and `*/corpus/lessons/**/*.md` (first 40 lines for metadata) | 683 knowledge / 540 lessons; source 87, verified-at 81, recheck 87; missing 596/602/596; 87 cadence; 0 explicit overdue |
| E13 | Python: README `\|` rows; `## Frontier` section presence/bullets; `ls *-shokunin/corpus/QUALITY.md`; `ls *-shokunin/corpus/SOURCES.md` | 620 README rows; 7 frontier sections, 30 bullets; 10 QUALITY; 0 SOURCES |
| E14 | `for d in *-shokunin; do test -f $d/SKILL.md; test -f $d/PROVINCE.md; done` | SKILL 18/21; PROVINCE 21/21 |
| E15 | `git -C game-dev-3d-shokunin status --porcelain; … kama …; … lore …` | `?? reports/round-107/`; `?? .ufo/round-10/`; `?? .scratch/` |
| E16 | `wc -lc .ufo/reports/AGGREGATE.md; grep -c '^## ' …; grep -cE '^\| D-[0-9]+' …; sort max` | 2,132 lines / 244,780 B; 15 sections; 165 rows; `D-155` |
| E17 | `wc -c SCORECARD.md LOG.md` | 57.8 KB / 128.7 KB — wrong content, see A1 |
| E18 | `ls scripts/` | `shokunin-watchdog.sh` only |
| E19 | `git log -1 --author='aggregator-shokunin' --format='%h %aI %an %s'; git log -1 --format='%h %aI %an %s' e5efe29; … 79752af` | `b159992 2026-09-29 aggregator-shokunin`; both later commits author `ci` |
| E20 | `node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --selftest; … --all` | `6/6 PASS` exit 0; `--all` exit 1, 8 rounds / 8 failed, 123 findings (115 cited-commit-missing, 5 marker-overwrite, 3 verdict-without-revision) |
| E21 | `git show 12f2da5:SCORECARD.md \| awk 'NR>=199&&NR<=438' \| grep -nE '^\| (corpus review\|cross-lane quality\|mint/dormancy)'` | scores 9/9/9; Planned 176, Retired 194, Move log 208 in-section |
| E22 | `ls -d ~/Projects/aggregator-shokunin` | No such file or directory |

---

## 13. Limits and honest non-claims

- **HEAD is contaminated.** Axis scores and the last legal planned/retired
  blocks were read at `12f2da5`, not HEAD. This dossier does not claim the HEAD
  card is the lane's record; it claims the opposite, with commands.
- **Current corpus verdicts are live-worktree measurements**, not frozen
  verdicts; three lanes are dirty. Do not quote the 1,374 findings as a frozen
  baseline without naming the worktrees and revisions.
- **Overdue recheck is 0 only because it is not computable.** 87 metadata
  entries use `recheck:` for prose/commands/cadence; no absolute date was
  observed in the lane-scoped scan. A future census must define the cadence
  arithmetic and the `opened` basis before it can call anything overdue.
- **No lane is called dormant here.** The last complete sweep is 2026-09-29,
  the two readings disagree (0/8 vs 1/8), and the state counters are stale.
  The dossier reports the aggregator's own failed-round loop and the missing
  inputs; it does not manufacture a fleet verdict.
- **No web research was performed** (STATE assignment; no `web_search` calls).
  No fetched content was present, hence no prompt-injection attempt was observed.
- **No subagents** were dispatched (leaf-member bound). Gate runs are read-only
  over the repos; the only writes were the two transient `/tmp` captures and
  this artifact.
- **No fix was applied.** Every defect in §8 is routed for wave 2; the root
  SCORECARD/LOG restoration is integrator work, not a lane edit.
- **Counts are scoped to the 21 lane repos.** An unscoped `find .` over the
  fleet root also walks `.tower` worktrees and other copies (observed 179k
  knowledge-like paths); those are not fleet corpora and are excluded from the
  683/540 figures.
- **No source rows are offered.** This is a STATE dossier, not a lane
  `SOURCES.md`; the census design in §10 is the vehicle for those rows.
