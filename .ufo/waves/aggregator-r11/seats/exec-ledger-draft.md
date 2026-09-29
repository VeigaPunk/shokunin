# exec-ledger-draft — AGGREGATE.md §15 (refresh 8) + SCORECARD `### Round 11` + LOG.md entry

**Seat:** `LedgerExec` (L2, aggregator lane wave `aggregator-r11`). **Composer's stamp:** `2026-09-29T03:26:04Z`, main HEAD
`8afbc8f` (`date -u +%Y-%m-%dT%H:%M:%SZ; git rev-parse --short HEAD`). All static text below is final-quality prose in the
ledger's established voice; every cell that lands from a live seat is a `<TBD: … >` placeholder carrying the exact
command that fills it. **This file is a draft skeleton — it is not the ledger.** Counts measured at composition are
labelled *composition reading* and every one of them is expected to drift inside the wave (§14.1 / P-s).

**Two brief-vs-measurement corrections, stated before the draft consumes them (never silently adopted):**

1. The brief says *"MISSION.md table = 8 lanes"*. Measured at `8afbc8f`:
   `grep -cE '^\| (protocol|aggregator|kasegi|kengaku|kake|kumitate|kotoba|kagi|kama) \|' MISSION.md` → **9**, and the
   file's own heading reads *"## Fleet shape (9 L1 lanes)"*. The fleet is **9 L1 lanes = 2 main-repo (protocol, aggregator)
   + 7 child repos (kasegi, kengaku, kake, kumitate, kotoba, kagi, kama)**. "8" matches no measured set on any surface;
   the draft uses the measured set and the §15.1 table carries **8 rows** (7 child lanes + the aggregator self-row) by the
   §12.1 precedent (which excluded `protocol`, whose row belongs to the protocol lane's own section).
2. The brief says the routed row is *"D-150 territory"* and *"max existing key is D-149"*. Measured:
   `python3 -c "import re;t=open('.ufo/reports/AGGREGATE.md').read();r=re.findall(r'^\| (D-\d+)',t,re.M);print(len(r),len(set(r)),max(r,key=lambda x:int(x[2:])))"`
   → **160 rows, 146 distinct, max `D-150`**. `D-150` is already occupied (§14.18's connector row, `AGGREGATE.md:1909`).
   The mint-bookkeeping row is proposed as **`D-151`**; keys are the L1's to assign, so the text below is key-less.

---

## §15 — the draft, to be appended to `.ufo/reports/AGGREGATE.md` verbatim (placeholders resolved)

### 15. Refresh 8 — round-11 aggregator audit (the mint that left no ledger record)

**Stamp.** Aggregator lane round 11 (`.ufo/state/aggregator.round` = `11`; `cat .ufo/state/aggregator.round`). Refresh
cutoff: **`<CUTOFF>`** (`<TBD: date -u +%Y-%m-%dT%H:%M:%SZ>`), main HEAD **`<TBD: git rev-parse --short HEAD>`**. This
refresh discharges the move named in `SCORECARD.md` §Planned: mint/dormancy calls, held at 8 for two refreshes, worked as
**post-mint accounting** — the ledger's first case of a mint executed that the ledger never recorded (§15.3).

**Round-10 note (why refresh 8 lands on round 11).** Round 10 produced no refresh: its report is a 187-byte marker
(`wc -c .ufo/reports/round-10/aggregator.md` → 187) reading *"Fleet wrap: lane completed by operator directive before its
report landed."* Per the marker clause that lane-round is graded **failed** and excluded from the dormancy pair count;
the refresh counter advanced while the round counter did not. §12 is round 7 / refresh 5, §13 round 8 / refresh 6, §14
round 9 / refresh 7 — **the round−refresh offset is 2 through §14 and the round-10 marker makes §15 = round 11 / refresh 8.**
A reader who assumes the offset holds will look for a §15 at round 10 and find a marker.

**Method.** `<TBD: seat count — 12 L2 seats visible in this wave's roster at composition>` read-only L2 seats in one
batched `task` call (`MISSION.md` floor 8): scouts (sweep window, standing tables, mint event, dormancy re-key, L0, corpus
currency), executors (this ledger draft, queue distillation), plus critic, reviewer, sentinel, revenger, connector.
Every volatile cell was re-run by this lane at the cutoff. Clause citations are **text over line numbers** — at the
`<CUTOFF>` revision the anchors resolve as:
`grep -n 'never an automatic retirement' PROTOCOL.md` → **39**; `grep -n 'is a marker, not a report' PROTOCOL.md` → **150**;
`grep -n 'canonical for rank and roster' PROTOCOL.md` → **409**; `grep -n '^## Gate standard' PROTOCOL.md` → **324**
(line numbers at main `8afbc8f`, the composition revision; `PROTOCOL.md` was compacted at `17c1fad`, so §12.1's
*"line 28 at `f9dcfd2`"* no longer resolves — the dormancy text now sits in the `## Lifecycle` tail, not under
`## Promotion gates`).

### 15.1 Standing dormancy table (rostered lanes) — re-keyed to the 9-lane fleet

**Rule applied — `PROTOCOL.md` `## Lifecycle` tail, verbatim** (`PROTOCOL.md:37-39` at `8afbc8f`; the §12.1
"Promotion-gates preamble" citation moved):

> Two consecutive dispatched-and-reported rounds with no `LOG.md` activity flag a shonen **dormant**
> by the integrator in the round notes; undispatched rounds do not count against it. Dormancy is a
> review trigger for the operator, never an automatic retirement.

**Marker grading — `PROTOCOL.md` report-contract clause, verbatim** (`PROTOCOL.md:150-155` at `8afbc8f`): *"A filed
report recording no lane work — no changes, no evidence pointer, no resolvable commit — is a marker, not a report: the
integrator records that lane-round `failed` … A short report naming a real committed round-work hash is a *defective*
report, not a marker: status `ok`, minimum-content defect recorded. A marker naming nothing checkable is `failed`
whatever the lane actually did."* Failed markers are excluded from the dispatched-and-reported pair count; `ok`-graded
defective reports count.

**The table — 8 rows, stamped to the cutoff (`<CUTOFF>`, HEAD `<HEAD>`):** the 7 child lanes + the aggregator self-row.
**Row-set change vs §12.1: `kama` is added** (minted, §15.2/§15.3) — the fleet grew and the table's row set was never
re-derived (self-defect 28). `protocol` stays out by the §12.1 precedent (its row is the protocol lane's).

| Lane | Counter | Last dispatched (`watchdog.log`) | Last report landed (marker grading) | Last `LOG.md` round entry (R5 scan — bullets for 5 child lanes, headings for kotoba/kama/main) | Last commit (age at cutoff) | Dormancy verdict |
|---|---|---|---|---|---|---|
| kasegi | `<TBD: cat .ufo/state/kasegi.round>` | `<TBD: grep -n 'launch kasegi round=' .ufo/watchdog.log \| tail -1>` | `<TBD: ls -la .ufo/reports/round-<N>/kasegi.md + wc -c>` | `<TBD: R5 scan — kasegi entries are bullets ("- <date> — round N:"); a heading-pattern scan returns EMPTY here>` | `<TBD: git -C kasegi-shokunin log -1 --format='%h %ar' --author=$(git -C kasegi-shokunin config user.email)>` | `<TBD: pair derivation>` |
| kengaku | `<TBD: cat .ufo/state/kengaku.round>` | `<TBD: grep -n 'launch kengaku round=' .ufo/watchdog.log \| tail -1>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` |
| kake | `<TBD: cat .ufo/state/kake.round>` | `<TBD: grep -n 'launch kake round=' .ufo/watchdog.log \| tail -1>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` |
| kumitate | `<TBD: cat .ufo/state/kumitate.round>` | `<TBD: grep -n 'launch kumitate round=' .ufo/watchdog.log \| tail -1>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` |
| kotoba | `<TBD: cat .ufo/state/kotoba.round>` | `<TBD: grep -n 'launch kotoba round=' .ufo/watchdog.log \| tail -1>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` |
| kagi | `<TBD: cat .ufo/state/kagi.round>` | `<TBD: grep -n 'launch kagi round=' .ufo/watchdog.log \| tail -1>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` | `<TBD: …>` |
| **kama** (new row) | **2** — `cat .ufo/state/kama.round` | **r2 @ 00:19:34 -03** — `grep -n 'launch kama round=' .ufo/watchdog.log \| tail -1` (r1 launched 22:44:08 -03, completed+respawned 00:19:33 -03) | **r1 — `.ufo/reports/round-1/kama.md` 10,144 B, real** (`wc -c .ufo/reports/round-1/kama.md`; names a committed hash `c6199a2`) → **`ok`** | **round 1** — `grep -niE '^#{2,3} *round [0-9]+' kama-shokunin/LOG.md` → `kama-shokunin/LOG.md:7` (**case-insensitive is load-bearing**: kama's heading is lowercase `## round 1`, so the §12.1 heading pattern returns nothing — verified at composition) | `c6199a2` — `git -C kama-shokunin rev-parse --short HEAD`; **`<TBD: %ar>`** | **ACTIVE — not yet dormancy-eligible:** 1 dispatched-and-reported pair (r1), r2 live ⇒ the two-consecutive-round precondition is not yet met, so this row **cannot** be graded dormant for two more rounds whatever happens. This is the row the rule's positive test case will have to be sought in. |
| aggregator | **11** — `cat .ufo/state/aggregator.round` | **r11 @ `<TBD: grep -n 'launch aggregator round=' .ufo/watchdog.log \| tail -1>` (this refresh, in flight)** | **r10 — `.ufo/reports/round-10/aggregator.md` 187 B, marker, names nothing checkable → `failed`, excluded.** Last `ok` report: r9 18,604 B, real (`wc -c .ufo/reports/round-9/aggregator.md`) | **Round 9** (`LOG.md:324`, main — shared file; attribution filter `^#{2,3} Round [0-9]+ — aggregator` in R5; there is **no** round-10 aggregator LOG entry) | `<TBD: git log -1 --format='%h %ar' --author=<aggregator identity> >` | **ACTIVE** — pair = r9 (ok) + r8 (ok); r10's marker is excluded, not a strike |

**LOG-scan method — the §12.1 heading pattern is correct for 2 of 8 rows, and a wrong matcher fails silently.** The
published `^#{2,3} Round [0-9]+` pattern resolves only for `kotoba` (`kotoba-shokunin/LOG.md:780`) and the main-repo
`LOG.md` (the aggregator row, filtered `— aggregator`). Measured at the composition revision: the other five child LOGs
carry **bullet** entries (`- <date> — round N: …`, e.g. `kasegi-shokunin/LOG.md:684`) and `kama`'s heading is
**lowercase** (`## round 1` at `kama-shokunin/LOG.md:7`) — so the heading pattern returns **empty for six of the eight
rows**. That is §12.1 self-defect 9 reproduced by copying its prose: the R5 block below uses a case-insensitive token
scan and requires a tail-read, and this note is the reason. **Two live cells the scan surfaces, for the scouts to
adjudicate (not this seat's ruling, and not publishable as read):** (i) **`kagi` — its newest LOG token moved from
`round 15` (`kagi-shokunin/LOG.md:645/648`) at `03:26:04Z` to `round 16` (`:593`) at `03:29:52Z` while
`.ufo/state/kagi.round` stayed **17**: a real LOG lag whose depth is not stable inside four minutes — exactly the cell
that must be tail-read, never tail-scanned, before it is graded**; (ii) **`kengaku` — the token scan's tail lands on a
prose line** (`LOG.md:18` holds both `round-8` and `round-11`), the false-tail risk that correction 3's numeric bound
does not remove.

**Everything moved between two readings 3m48s apart** (`2026-09-29T03:26:04Z` → `03:29:52Z`) — P-s in one line, and
the reason this table's cells are stamped rather than asserted. Child HEADs at the second reading: kasegi `b021dc9`
(dirty 29), kengaku `e171cdf` (5), kake `ab87a48` (4), kumitate `f9f8e4d` (4), kotoba `d85982d` (0), kagi `8a6ec16` (0),
kama `c6199a2` (1); counters kasegi 18, kengaku 14, kake 17, kumitate 17, kotoba 17, kagi 17, kama 2 — every child HEAD
in §14.1's table has moved again. Command: R0 + R5.

**No lane is dormant at this cutoff (0/8)** — `<TBD: confirm after the kama row lands; the verdict count changes from §12/§13/§14's 0/7 to 0/8>`. The
dormancy rule still has **no positive test case** (eight refreshes) — and the kama row is now the fleet's youngest lane,
so the earliest a positive case can exist is kama r3.

**Per-row marker ledger re-measured (`<TBD: the scouts' grading)`:** `<TBD: kengaku r8 = 101 B no-commit failed; kotoba r8 = 120 B naming 8c300ad → ok+defect; kumitate r7 = 122 B naming 7a4c9a0 → ok+defect; aggregator r5 = 254 B failed; aggregator r10 = 187 B failed — five row-hit markers, unchanged in grading, plus any new marker the sweep window turns up>`.

### 15.2 Standing mint/watchlist table (candidates) — **kama GRADUATED**

**Mint bar — `PROTOCOL.md` `## Lifecycle` → shonen bullet, verbatim** (`PROTOCOL.md:12-13` at `8afbc8f`): *"two documented
**unplaceable** demand instances (work no existing province could absorb) or an explicit operator directive."*

**Graduation note (the §12.2 kama row retires; it is not re-tested).** The row that stood for three refreshes as
*"Bar met — mint-eligible … **blocked-external** — operator decision pending"* was **falsified by event**:
`git log --oneline -1 17c1fad` → `fleet relaunch: all L1 lanes -> @m_swe; repo moved to ~/Projects/shokunin; kama row;
pending protocol+scorecard edits`, `2026-09-29T00:19:02-03:00` — i.e. the operator ruled **by minting**, on the
*operator-directive* limb, not by editing the L0 file. `kama-shokunin/MINT.md` (3,891 B): *"Minted by: L0 integrator
session (operator directive, 2026-09-28), on aggregator evidence."* The candidate column is therefore **struck**; kama's
row moves to §15.1 as a lane, and the mint, not the demand, becomes the accounting object (§15.3).

**The table — 4 remaining candidates + space for new sweep candidates:**

| Candidate | Surface | Demand instances (dated pointers, verified at cutoff) | Owning-province test | Bar verdict (dated) | Status | Re-run |
|---|---|---|---|---|---|---|
| ~~**kama**~~ | ~~local model serving & endpoint health~~ | **GRADUATED 2026-09-29** — operator directive, `17c1fad`; 2 unplaceable instances (kagi r3 `06ef644`, kengaku r4 `a1af83c`) were the evidence, and they still resolve | mooting (the surface now has an owner: `kama-shokunin/`) | **MINTED** — not a candidate | **retired from this table; now a §15.1 lane row.** Its "blocked-external" label is dead; **never re-list kama as a mint candidate** (the §12/§14 "not re-flagged" rule, upgraded one step) | — |
| kessho | CI/verification harnesses | `<TBD: sweep rounds 10–<cutoff> for builder instances>` — §14.9's reading was 0 unplaceable (the round-11–13 refusals are refused *commands/scope*, not refused verification work) | `<TBD: owning-province test on the new instances>` | **Below bar** (§14.9 re-derivation: 5 lanes / 15 tracked harnesses) | `<TBD: new instance? kumitate round-gate.mjs + kotoba verifiers both landed since; re-test the D-82 condition>` | `<TBD: git -C <repo> ls-files \| grep -E '(^|/)(scripts\|verifiers)/.*\.(mjs\|sh\|py\|js)$\|corpus/(drift-pins\|claim-ledger\|transcript-scan\|surface-census)\.sh$' \| wc -l per lane>` |
| umihotaru | fleet/pane wall ops | `<TBD: §12.5-U sweep over the window>` | owned (`scripts/shokunin-watchdog.sh`), not a domain | **Below bar** (re-tested 2026-09-28) | `<TBD: new instance?>` | `<TBD: §15.7-U>` |
| kagemusha | substrate adapters & mirrors | `<TBD: §12.5-G sweep over the window>` | distributed across three served provinces; no refusal | **Below bar** (re-tested 2026-09-28) | `<TBD: new instance?>` | `<TBD: §15.7-G>` |
| axis-framework-stewardship | SCORECARD templates, per-axis proxies, rollout order | `<TBD: sweep; §12.2 found 1 incidental mention>` | not a domain — protocol + aggregator work; routed, not refused | **Below bar** (refresh-4 ruling stands) | `<TBD:>` | `<TBD: §15.7-A>` |
| `<TBD: new candidate, if the sweep turns one up — name / surface / instances / province test / bar / status / re-test>` | | | | | | |

**M-row movement this refresh (`<TBD: final tallies>`):** **M2 "mints executed" 0 → 1** — and the 0 published through
nine refreshes was **false-in-fact** (§15.3, self-defect 27). **M4 "candidates with a dated bar test"**: kama's row retires,
so the denominator drops 5 → 4 while the dated-test count stays 4, changing the fraction from 5/5 to 4/4 for a
non-substantive reason — record which, do not let the fraction move silently. **The table now has 0 bar-met candidates
for the first time in nine refreshes**; the standing duty reduces to keeping the four below-bar verdicts dated and
re-running their sweeps.

**kama live-drift probes (`<TBD: re-run at cutoff; §12.2's values were 34113 → 200, 8080 → 404, both configs pinning 8080; kama r1's census is the successor evidence>)`** — the drift the mint was built on persists; the mint gave the
surface an owner, **not** a fix (kama r1 L0 lines, §15.6). Filed as the lane's work, not a residual here.

### 15.3 Mint event bookkeeping — a mint executed with no ledger record (proposed row `D-151`)

**The finding, one line:** the fleet minted a 7th child lane (`kama`, operator directive, main `17c1fad`
`2026-09-29T00:19:02-03:00`) and **no canonical ledger surface recorded it** — the two files `PROTOCOL.md` names as
roster truth still say 6, and `MANIFEST.json`'s `rounds[]` carries no `minted` record for it.

**Measured divergence across every surface that should carry it** (composition reading, `8afbc8f`):

| Surface | Command | kama present | Count |
|---|---|---|---|
| `MANIFEST.json` `.roster[]` | `python3 -c "import json;print([r['id'] for r in json.load(open('MANIFEST.json'))['roster']])"` | **no** | **6** |
| `ROADMAP.md` §Roster table (the declared mirror) | `sed -n '5,12p' ROADMAP.md` | **no** (kama appears only as a **candidate** at `ROADMAP.md:80`: *"Integrator decision pending: mint or record a rejection"*) | **6** rows |
| `MANIFEST.json` `rounds[].minted` | `python3 -c "import json;m=json.load(open('MANIFEST.json'));print(len(m['rounds']),sum(1 for r in m['rounds'] if r.get('minted')))"` | **no** | **48 rounds / 0 non-empty `minted`** |
| `MISSION.md` §Fleet shape | `grep -c 'kama' MISSION.md`; heading *"Fleet shape (9 L1 lanes)"* | **yes** (landed at `17c1fad` — `git show 17c1fad:MISSION.md \| grep -c kama` → 1) | **9** lanes |
| `.ufo/watchdog.log` | `grep -n 'kama' .ufo/watchdog.log` | **yes** | launch r1 `22:44:08 -03`, complete+respawn `00:19:33 -03`, launch r2 `00:19:34 -03` |
| `.ufo/state/` | `cat .ufo/state/kama.round`; `git ls-files .ufo/state/ \| grep kama` | **yes** | `kama.round` = 2, both state files tracked (18 state files tracked) |
| `kama-shokunin/` | `git -C kama-shokunin log --oneline \| wc -l`; `rev-parse --short HEAD` | **yes** | 2 commits (`9cee9fc` seed, `c6199a2` round-1), HEAD `c6199a2`, 23 files `+3164/−27` |
| `.ufo/reports/` | `ls -la .ufo/reports/round-1/kama.md` | **yes** | r1 report 10,144 B, names `c6199a2` |
| `AGGREGATE.md` §12.1 / §12.2 | `grep -n '\*\*kama\*\*' .ufo/reports/AGGREGATE.md` | **no lane row**; as a **candidate** row, `blocked-external` | 7 lane rows / 5 candidate rows |

**Three defects fall out, in severity order.**

1. **The split is canonical-side.** `PROTOCOL.md:409-413` verbatim: *"`MANIFEST.json` is canonical for rank and roster;
   `ROADMAP.md` mirrors it. Only integrator roles write main-repo files … the protocol lane holds the
   `PROTOCOL.md`/`ROADMAP.md`/report writes plus, as integrator-of-record, `MANIFEST.json` `rounds` appends; edits
   *outside* `rounds` stay operator-side."* The operator directive landed the row in `MISSION.md` — the one roster
   surface that is **not** declared canonical — and left the canonical file and its mirror at 6. Every consumer that
   reads roster truth (`MANIFEST.json`, `ROADMAP.md`) is blind to a live lane that has a repo, a watchdog counter, a
   report and a LOG entry.
2. **No `minted` record, and no `type: "mint"` entry.** `PROTOCOL.md:204` fixes the round-entry shape
   `{round, date, type, lanes, promotions, minted: [id...], notes}`; `PROTOCOL.md:208-210` requires that *"a `type: "mint"`
   entry … carries no `lanes` map, is excluded from lane-status tallies, and names its mint evidence pointer, the
   probation note, and whether the roster/`ROADMAP.md` rows landed or are pending."* Measured: 48 entries, **0** with a
   non-empty `minted`, and no `type: "mint"` entry at all. So the fleet's own closure instrument cannot report the mint
   it executed.
3. **The standing metric was measuring the ledger, not the fleet.** §12.2 and §14.9 published *"M2 / mints executed: 0"*
   for nine refreshes, resting on the same `rounds[]` scan that defect 2 invalidates. The measurement was correct about
   the file and wrong about the fleet — a metric-validity defect (self-defect 27), not a staleness one.

**The two legitimate readings, which the operator must disambiguate** (this is what the routed row asks):

- **Operator-directive reading:** the directive *is* the mint; `MINT.md` dates it, `MISSION.md` carries the row, the
  probation clause is skipped, and the roster row is **owed now**. Fix = operator adds the `MANIFEST.json` roster row +
  `ROADMAP.md` table row; protocol appends the `rounds[].minted` + `type: "mint"` entry.
- **Sibling-mint reading:** `PROTOCOL.md:34-36` — *"self-iterates through at least three verified rounds building
  `corpus/` + `PROVINCE.md` before roster rows exist; (d) only after those rounds land does the operator add the
  `MANIFEST.json` roster row and `ROADMAP.md` table row — probation state is recorded in `rounds[].notes` meanwhile, not
  as a roster row."* kama is at **round 1 of ≥3** and `MINT.md` §Probation invokes exactly this clause, so the roster row
  is **correctly pending** and only `rounds[].notes` is owed now.

Both readings are evidenced; they disagree about whether the canonical roster is stale or correct. **The ledger does not
rule — but it does record that the surfaces currently contradict each other, which no reading permits.**

**Proposed routed-row text (key assigned by the L1; text is final):**

> **Owner:** operator (roster/rank edit — outside `rounds`, hence operator-side per `PROTOCOL.md:409-413`) **+** protocol
> (the `rounds[]` append — integrator-of-record scope). **Sev 3.** A mint executed with no ledger record: `kama` was
> minted by operator directive at main `17c1fad` (`2026-09-29T00:19:02-03:00`), its lane repo exists (HEAD `c6199a2`,
> MINT.md 3,891 B), the watchdog has launched it twice (r1 `22:44:08 -03` completed+r2 `00:19:34 -03` live) and r1
> reported 10,144 B — yet `MANIFEST.json` `roster` still lists **6** ids, `ROADMAP.md` §Roster still lists **6** rows
> (kama appears only as a *candidate* at `:80`), and **0 of 48** `rounds[]` entries carry a non-empty `minted` or a
> `type: "mint"` entry. `MISSION.md` — not a declared roster surface — is the only file carrying the new lane (9 lanes).
> Rule on the limb: **operator-directive** (roster row owed now: add the `MANIFEST.json` row + `ROADMAP.md` mirror row,
> and append the `rounds[].minted`/`type:"mint"` entry) **or** **sibling-mint probation** (roster row owed at kama r3;
> record `rounds[].notes` now). Either ruling closes it; the contradiction does not close itself.
> **Evidence:** §15.3 table; `grep -n 'canonical for rank and roster' PROTOCOL.md` → 409; `git show 17c1fad:MISSION.md | grep -c kama` → 1; the section 15.3 commands above.

**Adjacent, same bookkeeping gap (kama's own r1 L0 line, already filed lane-side).** `.gitignore:1-6` lists the six child
repos and **omits `kama-shokunin/`**: `git check-ignore -v kama-shokunin` → no match (exit 1), `git status --short | grep -i kama` → `?? kama-shokunin/`. A main-repo `git add -A` would stage the nested lane repo as an embedded gitlink —
the same accident class the protocol lane filed for `.ufo/state`. Gauged at composition: `?? .ufo/prompts/kama-round-2.md`
(untracked dispatch prompt, the D-146 class) and ` M .ufo/state/kama.{mission,round}` (tracked, modified — the files the
r1 L0 line called untracked have since been tracked). Proposed as its own row (§15.9).

### 15.4 Queue movement this refresh

`<TBD: seats/queue-distill.md figures>` — the L1's independent count rules; the L2's proposed text is not authoritative.

- **Keys (composition reading, `8afbc8f`):** `python3 -c "import re;t=open('.ufo/reports/AGGREGATE.md').read();r=re.findall(r'^\| (D-\d+)',t,re.M);print('rows',len(r),'distinct',len(set(r)),'max',max(r,key=lambda x:int(x[2:])),'next','D-%d'%(max(int(x[2:]) for x in r)+1))"`
  → **160 rows, 146 distinct, max `D-150`, next free `D-151`**. **The brief's "max D-149 / D-150 territory" is stale:**
  `D-150` was consumed by §14.18's connector row. **New rows this refresh therefore continue from `D-151`**, and this
  seat's proposed rows are key-less (§15.9).
- **Folds and contradictions:** `<TBD: re-verify D-39⊇D-85, D-51⊇D-84 still hold; D-59 / D-68 / D-75(a) still open>`.
- **Open rows by owner, before this refresh's additions:** `<TBD: per-owner tally re-run>`.
- **Rows whose subject this refresh closes, not adds:** the §12.2 kama candidate row (graduated — §15.2); D-40
  ("kama mint-or-reject") — its decision has been *executed*; record the execution, do not close it silently, and do not
  re-open it as a mint question (§15.3 rules the bookkeeping, not the mint).
- **Round-10 marker: a documented not-dispatch, not a queue row.** `.ufo/reports/round-10/aggregator.md` is a 187 B
  fleet-wrap marker. It is `failed` for this lane (marker clause) and is excluded from §15.1's pair count; whether the
  driver's fleet-wrap path may close a lane-round on an operator directive without work is the protocol lane's question
  (the kumitate-r10 L0 line asked the same of `report_of()`).

### 15.5 Aggregator self-defects filed at refresh 8 (numbering continues §14.12, which ended at 26)

| # | Defect | Evidence |
|---|---|---|
| 27 | **The standing M2 metric measured the ledger, not the fleet.** §12.2 and §14.9 published *"mints executed: 0"* for nine refreshes off a `rounds[]` scan; a mint had been executed by operator directive and the scan could not see it because the record was never written. Correct about the file, false about the fleet | §15.3 defects 2–3; `python3 -c "import json;m=json.load(open('MANIFEST.json'));print(sum(1 for r in m['rounds'] if r.get('minted')))"` → 0 |
| 28 | **§12.1's dormancy row set was never re-derived when the fleet grew.** 7 rows for a 9-lane fleet (`kama` absent) through refreshes 5–7, including this lane's own §14.9 re-run, which re-ran every row's command and never asked whether the row set was complete | §15.1 8-row table; §12.1/§14.9 7-row tables |
| 29 | **§12.2's kama cell was republished as `blocked-external` ~3h after the mint falsified it.** The mint landed `2026-09-29T00:19:02-03:00`; §14's re-run (≈`01:1xZ`) re-executed the *byte-identity* command (which passed, because the operator answered by minting, not by editing) and reported the row *"unchanged, not re-flagged"*. A table that re-runs commands but not state can certify a dead cell — the standing-table method's own falsifier | §14.9 vs §15.2/§15.3; `git log --oneline -1 17c1fad` |

**Recurrence, recorded but not numbered:** self-defect 9's class — a LOG matcher that fails silently — **recurred in this
refresh's own draft** (a heading-only pattern copied from §12.1's prose, which returns empty for six of eight row
targets) and was caught before publication, not after. It stays self-defect **9**, not a new number: the fix is the
§15.1 method note and the R5 matcher, and a queue whose numbers grow while its classes persist is the metric-validity
defect 27 in another costume.

**Fix landed in-round for 28:** §15.1 carries the re-derived 8-row set and every future refresh states the fleet's lane
count next to the table's row count, so a row-set gap fails loudly instead of passing as a re-run. **27 and 29 are method
defects** and route as proposals, not rows: (P-w) a standing metric declares what it measures — the ledger or the fleet —
and is re-derived from the fleet surface at least once per refresh; (P-x) a standing table's re-run reports row-set
changes as first-class movement, not only cell changes.

### 15.6 L0 surfacing (MISSION.md: the aggregator surfaces entries each round)

`<TBD: seats/l0-forensics.md — classify by content, never by line number>` — at composition the file is **19 lines**,
sha256 `f857348e07903ccca56e60591905d4f1ecf565700ac34bf11bf4cde428d88d50` (`wc -l .ufo/l0-questions.md; sha256sum .ufo/l0-questions.md`).

**Two movements already measured this refresh, which change classifications §14.13 published:**

- **The kama mint-decision line (protocol r10, line 2) moves `blocked-external` → `answered by event`.** Its own text
  asked *"Mint kama, or record a rejection?"* and the operator answered **mint** by directive (`17c1fad`). The line's
  bytes did not change — the operator answered by executing, not by writing — which is exactly why §14's byte-identity
  test certified a dead cell (§15.5 defect 29). **The byte-identity test is retired for this line and replaced (§15.7
  kama block).** The *repoint* demand behind it is **not** answered: it is now kama's own province work, and kama r1
  filed it as its own lines.
- **Four lines appeared since §14.13's 11-line census** (`git log --oneline -3 -- .ufo/l0-questions.md` →
  `17c1fad`, `cd2d343`, `b5fff81`): **kama r1 ×3** (the live repoint + its larger-blast-radius addendum + the
  `.gitignore` hygiene gap), **kake r15/r16 ×2** (bounties-vanished corroboration and the escalating prune regime),
  **kasegi r16 ×1** (a second in-round source loss). `<TBD: the L0Scout's content-classified table for all 19 lines,
  lane × opening words × classification>`.

**Operator answers to date: 0** (`<TBD: re-confirm by the forensics method>`). New classifications expected:
**`answered by event`** (kama mint decision — new class), **`superseded`** (kasegi r12, per §14.13), **`open,
operator-only`** (the repoint family, the driver/template debt, the AXES vocabulary split, the gate-promotion item), and
the aggregator r9 CORPUS.md amendment set (`<TBD: unchanged?>`).

**One new line the aggregator owes at this cutoff:** `<TBD: whether §15.3's ruling request is filed on the L0 channel
as well as routed as a ledger row — a mint-bookkeeping ruling is an operator decision with two file owners, so the
protocol lane's r10 pattern (route + surface) applies>`.

### 15.7 Re-run commands (host-verified at this refresh's stamps; `grep` here is pi-uu-grep 0.2.0)

```sh
# R0 revision stamps — main + the 7 child lanes (the fleet's measured shape: 9 L1 lanes = 2 main-repo
#     (protocol, aggregator) + 7 child repos. "8 lanes" matches no measured set; this loop is the measured one.)
date -u +%Y-%m-%dT%H:%M:%SZ; git rev-parse --short HEAD
for d in kasegi kengaku kake kumitate kotoba kagi kama; do
  printf '%-9s %s dirty=%s\n' $d "$(git -C $d-shokunin rev-parse --short HEAD)" \
    "$(git -C $d-shokunin status --porcelain | wc -l)"; done

# R1 the gate: self-test (capability) then the repos (measurement) — §Gate standard's two evidences.
#     kama is a 7th tree: run it and record whether the gate handles a probation lane at all.
node .ufo/waves/round-9/corpus-gate.mjs --registry     # verdict map + checks + declared not-evaluated
node .ufo/waves/round-9/corpus-gate.mjs --selftest     # -> "# selftest tally 12/12 PASS", exit 0
node .ufo/waves/round-9/corpus-gate.mjs --all; echo "exit=$?"   # per-repo "# summary … rev=<hash>"
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kama-shokunin c6199a2   # frozen run over kama's round-1 revision

# R2 rule-8 occurrences with unit + revision + authorship (§14.4) — python3 scanner in .ufo/waves/round-9/l1-baseline.md §1
#     kama now scans too: a minted lane's corpus enters the rule-8 census for the first time.
# R3 SHONEN canonical form (§14.7) — checker in l1-baseline.md §2; kama's SHONEN.md joins the census (7 files, was 6)
# R4 queue keys (§14.10 / §15.4)
python3 -c "import re,collections;t=open('.ufo/reports/AGGREGATE.md').read();\
r=re.findall(r'^\| (D-\d+)',t,re.M);print('rows',len(r),'distinct',len(set(r)),'max',max(r,key=lambda x:int(x[2:])))"
# R5 the dormancy scan, 8 rows (§15.1) — per lane: counter, last dispatch, newest LOG token, last non-aggregator commit age.
#    The child LOG entry forms DIFFER: bullets ("- <date> — round N: …") for kasegi/kengaku/kake/kumitate/kagi,
#    headings for kotoba, LOWERCASE headings for kama. A heading-only pattern (^#{2,3} Round [0-9]+) returns
#    EMPTY for six of the eight rows — the §12.1 self-defect-9 trap, reintroduced by a copy of the prose pattern.
#    NOTE: keep awk OUT of a double-quoted "$( )" — '$NF' there is expanded by the shell and the filter dies silently.
for d in kasegi kengaku kake kumitate kotoba kagi kama; do
  tok=$(grep -noiE 'round[- ]([0-9]+)' $d-shokunin/LOG.md | awk -F'[: ]' '$NF<=99' | tail -1)
  printf '%-9s counter=%-3s launched=%-4s newestLOGtoken=%-14s commit=%s\n' $d "$(cat .ufo/state/$d.round)" \
    "$(grep -n "launch $d round=" .ufo/watchdog.log | tail -1 | cut -d: -f1)" "$tok" \
    "$(git -C $d-shokunin log -1 --format='%h %ar')"
done
#    aggregator row: the main LOG.md is shared with the protocol lane — filter the attribution (this is the whole filter):
grep -nE '^#{2,3} Round [0-9]+ — aggregator' LOG.md | tail -1
#    CONFIRM every token by reading the entry, never by tailing the scan: kengaku's scan tail lands on a prose line
#    (kengaku-shokunin/LOG.md:18 carries both round-8 and round-11) — the matcher is a candidate, not a grade:
grep -n 'round' kengaku-shokunin/LOG.md | tail -3
```

**R6 — kama graduation (REPLACES §14's R7 byte-identity check).** §14's R7 was
`git show e333e7c:.ufo/l0-questions.md | md5sum; md5sum .ufo/l0-questions.md` — a byte-identity test asserting the kama
L0 line was *unanswered*. The mint falsified the premise: the line's bytes are still identical **and the decision was
made**. The replacement asserts the event, the record gap, and the untouched file, in that order:

```sh
# R6 (a) the mint exists on its surfaces
git log --oneline -1 17c1fad                                    # -> fleet relaunch … kama row, 2026-09-29T00:19:02-03:00
git show 17c1fad:MISSION.md | grep -c kama                      # -> >=1  (the row landed in MISSION.md, not MANIFEST)
git -C kama-shokunin log --oneline | wc -l                      # -> 2     (9cee9fc seed, c6199a2 round-1)
git -C kama-shokunin rev-parse --short HEAD                     # -> c6199a2
grep -n 'kama' .ufo/watchdog.log                                # -> r1 launch 22:44:08 -03, complete+respawn 00:19:33 -03, r2 launch 00:19:34 -03
wc -c .ufo/reports/round-1/kama.md                              # -> 10144 (real report, names c6199a2)
# R6 (b) the canonical ledger did NOT record it — the divergence §15.3 measures
python3 -c "import json;m=json.load(open('MANIFEST.json'));print('roster',len(m['roster']),'rounds',len(m['rounds']),'minted',sum(1 for r in m['rounds'] if r.get('minted')))"
                                                                # -> roster 6 rounds 48 minted 0
sed -n '5,12p' ROADMAP.md                                       # -> 6 rows; kama only as a candidate at :80
git check-ignore -v kama-shokunin || echo NOT-IGNORED           # -> NOT-IGNORED (.gitignore:1-6 omit it)
# R6 (c) the L0 line was never edited — the operator answered by executing
wc -l .ufo/l0-questions.md; sha256sum .ufo/l0-questions.md
awk -F'|' '$1 ~ /kama/ {print NR": "$2}' .ufo/l0-questions.md   # -> the r1 lines (the repoint demand, still open, now kama's)
```

**R7 — the kama row is retired from the mint table; assert the retirement, never re-list it.** The check must be
**scoped to §15**: §12.2 (`AGGREGATE.md:928`) and §13's mint table (`:1285`) carry kama candidate rows, and both are
append-only (§12/§13 stay unrevised) — a global grep would report them as failures. Scope and assert:

```sh
awk '/^### 15\.1/{f=1} f' .ufo/reports/AGGREGATE.md | grep -c '^| \*\*kama\*\*'                                  # -> 1  (the §15.1 lane row)
awk '/^### 15\.2/{f=1} /^### 15\.3/{f=0} f' .ufo/reports/AGGREGATE.md | grep -c '^| ~~\*\*kama~~'               # -> 1  (struck + graduated)
awk '/^### 15\.2/{f=1} /^### 15\.3/{f=0} f' .ufo/reports/AGGREGATE.md | grep -c '^| \*\*kama\*\*'                # -> 0  (no unstruck candidate row)
```

### 15.8 Residual gaps kept honest, and proposals routed

- **The fleet has 9 L1 lanes and two different roster truths.** `MISSION.md` says 9; `MANIFEST.json` — the file
  `PROTOCOL.md` calls canonical — says 6. Until §15.3's ruling lands, **any count that reads the roster is wrong on one
  of the two files**, including this ledger's own M-rows. Named, not smoothed.
- **The dormancy rule still has no positive test case** (0/8 in eight refreshes). Its correctness is unproven in the
  only direction that matters, and kama — the fleet's youngest lane — makes the earliest possible positive case kama r3.
- **The mint table now has 0 bar-met candidates.** The axis's live content for the next refresh is *negative* calls and
  bookkeeping, not promotion; the M2 metric that was supposed to track promotions measured the wrong file (§15.5 defect 27).
- **`kama`'s drift is unfixed.** The mint gave the surface an owner; the 8080/34113 repoint, the janitor's zero-failover
  `qwen-local`-only provider set, and the declared-context (32768) vs served-context (16384) drift are all still live
  (kama r1 L0 lines) — a delegated duty, not a fleet residual.
- **Proposals routed to protocol/integrator (this lane cannot land main-repo files):** **P-w** a standing metric declares
  whether it measures the ledger or the fleet, and the fleet surface is re-derived at least once per refresh (§15.5
  defect 27); **P-x** a standing table's re-run reports **row-set** changes as first-class movement, not only cell
  changes (§15.5 defect 28); **P-y** `rounds[]` gains a `type: "mint"` entry for operator-directive mints as well as
  lane-initiated ones — `PROTOCOL.md:208-210` currently scopes the entry to *"a lane-initiated sibling mint"* and an
  operator mint under an existing heading is exactly the case that fell through.

### 15.9 Routed-defect rows added at refresh 8 (keys below are **proposals with their basis** — the L1 assigns; `D-150` is
already taken by §14.18's connector row, so the measured next-free is `D-151`, not the brief's "D-149/D-150 territory", §15.4)

| Key | Owner | Sev | Defect | Evidence / command |
|---|---|---|---|---|
| `D-151` `<TBD: L1 assigns>` | operator (roster) + protocol (rounds) | 3 | **The mint with no ledger record** — text in §15.3 (final prose, reproduced there) | §15.3 table; R6 block |
| `D-152` | operator | 3 | `.gitignore:1-6` lists the six child repos and omits `kama-shokunin/` ⇒ the nested lane repo shows `??` in the main tree and any main-repo `git add -A` stages it as an embedded gitlink (the `.ufo/state` accident class) | `git check-ignore -v kama-shokunin` → exit 1; `git status --short \| grep -i kama` → `?? kama-shokunin/`; kama r1 L0 line |
| `D-153` `<TBD: or fold into P-w>` | protocol | 4 | The M2 standing metric measured the ledger, not the fleet, and published `mints executed: 0` across nine refreshes while a mint was executed | §15.5 defect 27; §15.3 |
| `D-154` `<TBD: or fold into D-146>` | integrator | 4 | `?? .ufo/prompts/kama-round-2.md` — an untracked dispatch prompt for the newest lane (the non-durable-dispatch class), and `.ufo/state/kama.{mission,round}` are tracked-but-modified at the composition stamp | `git status --short`; `git ls-files .ufo/state/ \| wc -l` → 18 |
| `<TBD: sweep-window rows>` | `<TBD>` | | `<TBD: seats/sweep-window.md rows, marker census, stale-rounds rows>` | `<TBD>` |
| `<TBD: L0 rows, if any are owed by lanes other than kama>` | | | | |

---

## SCORECARD.md — draft `### Round 11 (refresh 8)` section (appends to `.ufo/reports/…`; placeholders resolved)

Placement: after `### Round 9 (refresh 7) — corpus-review axis-move` and before the `### Planned` block, matching the
existing section order. **Also required: the `### Round 10` gap must be acknowledged in one line**, since §12/§13/§14
sections correspond to rounds 7/8/9 and a reader will look for round 10 — it produced a marker, not a section.

### Round 11 (refresh 8) — mint/dormancy axis-move: the mint the ledger never recorded

Measured at the refresh cutoff **`<CUTOFF>`** (main HEAD `<HEAD>`); the mint event it audits is stamped
**2026-09-29T00:19:02-03:00** (`17c1fad`). This section ships in the round-11 commit, so it cannot cite its own hash —
the report does. **Axis choice:** all three axes stood at 8/9 with the lowest pair tied; **mint/dormancy** was taken
because the operator minted `kama` outside the ledger's own record and the standing tables still described the pre-mint
fleet — an unpaid obligation with a named counter-party, where cross-lane quality's residual was already *resolved* in
§14.6. **Round 10 recap (one line):** `.ufo/reports/round-10/aggregator.md` is a 187 B fleet-wrap marker — `failed`,
excluded from the dormancy pair count, no section owed.

| Axis | Score (before r11) | Score (after r11) | Evidence pointer | Last change |
|---|---|---|---|---|
| mint/dormancy calls | **8** | **9** | Before: the fleet had minted a 7th lane and no canonical ledger surface recorded it — `MANIFEST.json` roster 6, `ROADMAP.md` 6, **0 of 48** `rounds[]` entries with a `minted`; §12.1 carried 7 rows for a 9-lane fleet; §12.2 still carried kama as a bar-met *candidate* labelled `blocked-external` (dead for ~3h); "mints executed: 0" published for nine refreshes off a scan that could not see the mint. After: §15.3's five-surface divergence table with commands, the mint routed to its two correct owners (operator roster / protocol rounds) at §15.3, §15.1 re-keyed to **8 rows** incl. kama with the row-set change declared, §15.2's kama **graduated + struck with a never-re-list rule**, three self-defects (27 metric validity, 28 row set, 29 dead cell certified by a passing command), and R6 replacing the retired byte-identity check with an event check | round 11 |
| cross-lane quality | **8** | **8** (untouched) | not the round's axis; its box-3 residual stands as §14.6 left it (1 broken, 2 provisional-with-cause, 1 could-not-evaluate, 2 firm) but `SHONEN.md` form conformance is 0/6 on `[x]` verifier-ids and is now 0/7 once kama's file joins the census | round 9 |
| corpus review | **9** | **9** (untouched; one cell added) | not the round's axis; the gate, its r4 FP classes and the unregistrable-registry gap (D-127/P-v) stand. New this round: kama's corpus enters the rule-8 census and the gate's `--all` run for the first time (`--snapshot kama-shokunin c6199a2`), which is a measurement, not a move | round 9 |

Metrics (before → after, with counting commands):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M2′ | mints executed, measured **on the fleet surface** (M2's original cell measured the ledger — §15.5 defect 27) | **0** *(ledger-reported; false-in-fact)* | **1** — `kama`, operator directive `17c1fad` | `git log --oneline -1 17c1fad`; `git show 17c1fad:MISSION.md \| grep -c kama` → ≥1 |
| M7 | roster surfaces carrying the newest lane, of 3 (MISSION / MANIFEST / ROADMAP) | **1 / 3** | **1 / 3** — routed `D-151`; **the metric is the round's headline defect, and it does not move until the operator rules** | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['roster']))"` → 6; `sed -n '5,12p' ROADMAP.md` → 6 rows |
| M8 | `rounds[]` entries carrying a mint record | **0 / 48** | **0 / 48** — unchanged; the ledger instrument cannot report the executed mint | `python3 -c "import json;m=json.load(open('MANIFEST.json'));print(sum(1 for r in m['rounds'] if r.get('minted')))"` |
| M9 | dormancy rows vs the fleet's lane count | **7 rows / 9 lanes** (gap 2, undetected for 3 refreshes) | **8 rows / 9 lanes** (7 child + aggregator; `protocol` excluded by §12.1 precedent) — gap named, `<TBD: close or justify>` | `AGGREGATE.md` §15.1; `cat .ufo/state/*.round \| wc -l` → 9 |
| M10 | candidates in the standing mint table, and bar-met among them | 5 / 1 (kama) | **4 / 0** — kama graduated; first refresh in nine with no bar-met candidate | `AGGREGATE.md` §15.2 |

### Planned — amendment to the committed `### Planned` block (the round-11 axis departs from it; §14
self-defect 26 was *not* amending §Planned before switching, so this draft amends it in the same edit)

- **round 12 — corpus review (continuing at 9).** Unchanged residual set: the gate's registry home (D-127/P-v), the r4
  heuristic's three declared FP classes (D-141), per-rule movement at each lane's next landed revision, plus
  `--snapshot kama-shokunin` added to the frozen set.
- **Owed and not to be aged:** D-151's ruling (operator + protocol), the §12.2 kama cell's death recorded in the queue
  (D-40's decision has been *executed*), D-133 re-test at kagi's next landed revision, and §14's D-129 (the round-8
  section still reads as published).
- **Standing duty (every refresh), amended:** re-run §15.1/§15.2 **and re-derive their row sets against the fleet's live
  lane count** (self-defect 28's fix); re-run the gate's frozen snapshots incl. kama; **never** re-list kama as a mint
  candidate (§15.7 R7); re-run the reviewer seat against this lane's own newest cells (P-q).

### Retired

- none (unchanged). The splits declined at rounds 7–9 stay declined. **New reason to keep "mint/dormancy calls" unsplit:**
  the axis's two directions diverged in one round — the *mint* half is now operator-gated bookkeeping (`D-151`), the
  *dormancy* half is lane-measurable and still has no positive test case; that is the split's argument, and this round
  is the first evidence either way, so defer the decision one more refresh rather than split on one sample.

### Move log (row to append)

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 10 | — | (marker: fleet wrap; no work) | — | `.ufo/reports/round-10/aggregator.md` 187 B, `failed` |
| 11 | mint/dormancy calls | 8 — a mint executed with no ledger record (roster 6/6 across MANIFEST + ROADMAP, 0/48 `minted`), dormancy at 7 rows for a 9-lane fleet, kama still a bar-met candidate labelled `blocked-external`, M2 measuring the ledger | 9 — §15.3 five-surface divergence table + routed `D-151` with its two owners, §15.1 re-keyed to 8 rows, §15.2 kama graduated + struck with a never-re-list rule, self-defects 27–29, R6 replacing the retired byte-identity check | `.ufo/reports/AGGREGATE.md` §15 (M7–M10); `.ufo/waves/aggregator-r11/`; `17c1fad`; `kama-shokunin` `c6199a2` |

---

## LOG.md — draft entry (main repo, `/home/vgpnk/Projects/shokunin/LOG.md`; appends after `## Round 9 — aggregator lane …` at `LOG.md:324`)

Heading form must match this lane's existing entries exactly (`^#{2,3} Round [0-9]+ — aggregator`) — it is the only
attribution the shared file supports (§12.1 correction 2; the whole filter is the R5 line
`grep -nE '^#{2,3} Round [0-9]+ — aggregator' LOG.md | tail -1`, verified → `LOG.md:324` at composition):

```markdown
## Round 11 — aggregator lane — mint/dormancy axis-move: the mint the ledger never recorded

**Move.** All three axes stood at 8/9 with the lowest pair tied; this round took **mint/dormancy** because the operator
had minted a 7th child lane (`kama`, directive, main `17c1fad` `2026-09-29T00:19:02-03:00`) and **no canonical ledger
surface recorded it**. §15 audits post-mint accounting instead of promotion calls. **Round 10 recap:** the lane's round-10
report is a 187 B fleet-wrap marker — `failed`, excluded from the dormancy pair count, no refresh emitted, which is why
refresh 8 lands on round 11.

**What landed (verifiable artifacts).**
- **§15.3 — a five-surface divergence table, every cell commanded.** `MANIFEST.json` `roster` = **6** (`python3 -c …`),
  `ROADMAP.md` §Roster = **6** rows with kama only as a *candidate* at `:80`, **0 of 48** `rounds[]` entries carry a
  non-empty `minted` (`python3 -c "…sum(1 for r in m['rounds'] if r.get('minted'))"` → 0). Against that: `MISSION.md`
  carries the row (9 lanes, landed at `17c1fad`), the watchdog launched kama twice (r1 `22:44:08 -03` completed, r2
  `00:19:34 -03`), `kama-shokunin` has 2 commits (HEAD `c6199a2`) and `MINT.md` 3,891 B, and `.ufo/reports/round-1/kama.md`
  is a real 10,144 B report. **The operator directive landed the row in the one roster surface `PROTOCOL.md` does not call
  canonical.**
- **The mint is routed to its two correct owners** (`PROTOCOL.md:409-413` verbatim): the roster/rank edit is
  **operator-side** (*"edits outside `rounds` stay operator-side"*); the `rounds[].minted` + `type: "mint"` append is the
  **protocol lane's** (integrator-of-record). Proposed row **`D-151`** — key-less here; `D-150` is already taken by
  §14.18's connector row, so the brief's "D-149/D-150 territory" is stale.
- **§15.1 re-keyed to 8 rows** (7 child lanes + the aggregator self-row; `protocol` excluded by §12.1 precedent) — kama
  added, its row ACTIVE and **not yet dormancy-eligible** (1 reported pair, r2 live). Dormancy **0/8**, still no positive
  test case in eight refreshes; kama r3 is the earliest it can exist.
- **§15.2 — kama GRADUATED and struck**; the table's only bar-met row retires, leaving **4 candidates / 0 bar-met** for
  the first time in nine refreshes, with a **never-re-list rule** for the minted lane.
- **R6 replaces §14's R7 byte-identity check.** That test asserted the kama L0 line was unanswered; the operator answered
  **by minting, not by writing**, so the bytes stayed identical and the passing command certified a dead cell. R6 asserts
  the event, the record gap, and the untouched file, in that order.
- **Self-defects 27–29.** 27: the M2 standing metric measured the ledger, not the fleet — *"mints executed: 0"* for nine
  refreshes while a mint was executed. 28: §12.1's row set was 7 for a 9-lane fleet and was never re-derived, including by
  §14's own re-run. 29: §14.9 republished the kama cell as `blocked-external` ~3h after the mint falsified it — a table
  that re-runs commands but not state can certify a dead cell.

**Evidence.** Main repo: ledger §15 + this entry + `SCORECARD.md` §Round 11 + `.ufo/waves/aggregator-r11/` (seat files,
this draft among them) + the round-11 dispatch prompt, in the commit named in `.ufo/reports/round-11/aggregator.md`.
Mint event: main `17c1fad`; `kama-shokunin` `9cee9fc` (seed) + `c6199a2` (round-1); `.ufo/reports/round-1/kama.md`
10,144 B. **GitHub push scope: nothing pushed by L2s; this lane pushes only the main-repo report path per MISSION.md.**

**Falsifiable next iteration (round 12).** corpus review, continuing at 9: resolve the gate's registry home (D-127/P-v)
or record the reasoned rejection; close the r4 heuristic's three declared FP classes (D-141); re-run the gate at each
lane's next landed revision and report per-rule movement, **with `--snapshot kama-shokunin c6199a2` added**.
**Falsified if:** (a) any refresh publishes a roster count without naming which of `MANIFEST.json` / `MISSION.md` it read
(the split is the finding, §15.3); (b) §15.2 lists kama as a candidate again; (c) a standing metric is published without
declaring whether it measures the ledger or the fleet (P-w); (d) a dormancy table's row count is published without the
fleet's live lane count beside it (P-x fix, self-defect 28).
```

---

## Composers' checklist (for the L1 before this draft becomes §15)

- [ ] Replace `<CUTOFF>`, `<HEAD>`, seat count, and every `<TBD: …>` with the seat outputs; re-run R0/R4/R5 at the
      cutoff and stamp them.
- [ ] **Re-check the two brief corrections above before publishing** — MISSION.md is 9 lanes (not 8) and `D-150` is taken
      (next free `D-151`); if either measurement moved, re-derive rather than inherit.
- [ ] Confirm the kama §15.2 row is both **struck** and **graduated**, and that §15.1 carries it as a lane row — R7 asserts it.
- [ ] Decide whether `D-153`/`D-154` stay rows or fold into the P-w proposal and D-146 (flagged inline).
- [ ] Amend `SCORECARD.md` §Planned in the same commit as the new `### Round 11` section (self-defect 26's rule).
- [ ] Keep LOG.md's entry heading form byte-compatible with the lane's existing four entries, so R5's attribution filter
      still resolves it.
- [ ] **Do not re-derive the dormancy LOG cells with a heading-only pattern.** R5's matcher is case-insensitive and
      token-based for a measured reason (five child lanes use bullets, kama is lowercase); confirm each token with a
      tail-read, and never publish a LOG cell whose scan returned empty as if it were a measurement (self-defect 9).