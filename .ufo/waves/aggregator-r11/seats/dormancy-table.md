# Dormancy table — 8-lane fleet (7 lanes + aggregator self-row)

**Seat:** DormancyScout (scout, L2). **Output file:** `.ufo/waves/aggregator-r11/seats/dormancy-table.md` (this file only; no other fleet state touched, nothing committed).

**Stamps.** All cells measured **2026-09-29T03:26:00Z – 2026-09-29T03:30:11Z**; commit-age column stamped to a single instant **τ = 2026-09-29T03:28:48Z** (`date -u +%s` immediately before the age loop). Main HEAD at measurement: `8afbc8f` (`git log -1 --format='main HEAD %h %aI %an'` → `8afbc8f 2026-09-29T00:19:15-03:00 Joao Pedro Veiga`). Correction/verification pass (kama ledger row, D-key max) re-stamped `date -u +'MEASURED_AT %Y-%m-%dT%H:%M:%SZ'` → `2026-09-29T03:32:20Z`; per-repo LOG-matcher verification pass (peer-seat correction) re-stamped → `2026-09-29T03:35:36Z` / `2026-09-29T03:35:55Z`.

**Row identity = roster + self.** 8 rows: the 6 `MANIFEST.json` roster ids + kama + aggregator. Roster re-read: `python3 -c "import json;m=json.load(open('MANIFEST.json'));print([r['id'] for r in m['roster']])"` → `['kasegi','kengaku','kake','kumitate','kotoba','kagi']`, **len 6** — kama is not rostered, but **the mint *is* ledger-recorded** and the missing roster row is *by declaration*, not a gap:

- `python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];[print(json.dumps(x)) for x in r if x.get('type')=='mint']"` → `rounds[36]` = `{"round": 11.5, "date": "2026-09-28", "type": "mint", "minted": [], "notes": "sibling-mint allowance landed in PROTOCOL.md Lifecycle; kama-shokunin minted in probation (local model serving & endpoint health — aggregator mint-eligible r4/r6/r7, demand instances: kagi r3 + kengaku r4 endpoint-drift 8080->34113). Roster row withheld until >=3 verified self-iteration rounds per the new clause; lane wired into watchdog (m_flash, axes operability+freshness)."}`, landed by `git log -1 --format='%h %aI %an %s' 2d19a64` → `2d19a64 2026-09-28T22:44:21-03:00 integrator sibling-mint allowance + kama probation entry`.
- `PROTOCOL.md:28-36` (sibling-mint clause, verbatim): *"the sibling self-iterates through at least three verified rounds building `corpus/` + `PROVINCE.md` before roster rows exist; (d) only after those rounds land does the operator add the `MANIFEST.json` roster row and `ROADMAP.md` table row — probation state is recorded in `rounds[].notes` meanwhile, not as a roster row."*

⇒ **kama is scored in this table as probation-minted / roster-row-pending.** *(Correction credited to peer seat `L0Scout`, verified here against the file — my first pass read `minted` truthiness as "no mint record"; see §5 defect 5.)* Mint ownership stays with the L1/MintScout seat.

---

## 1. Rule as applied (verbatim, not paraphrased)

`sed -n '30,45p' PROTOCOL.md` at `8afbc8f`, "Promotion gates" preamble:

> Two consecutive dispatched-and-reported rounds with no `LOG.md` activity flag a shonen **dormant** by the integrator in the round notes; undispatched rounds do not count against it. Dormancy is a review trigger for the operator, never an automatic retirement.

`sed -n '145,160p' PROTOCOL.md` (report-contract clause):

> A filed report recording no lane work — no changes, no evidence pointer, no resolvable commit — is a marker, not a report: the integrator records that lane-round `failed`, keeps the marker file as a conformance defect, and names the counter advancement in the round notes. A short report naming a real committed round-work hash is a *defective* report, not a marker: status `ok`, minimum-content defect recorded.

Operationalisation inherited from §12.1 / §13.3 (unchanged): **failed markers are excluded** from the dispatched-and-reported pair; `ok`-graded defective reports count; the pair is the two most recent rounds that were **both** dispatched **and** reported in, adjacency checked against the restricted sequence (precedent: §12.1 aggregator row pairs **r6 + r4**, skipping the r5 failed marker). Log-activity tested by **entry scan**, not by the §12.5-R4 token scan (host-broken — §13.5 item 14).

---

## 2. The table (8 rows)

`<lane>` = the row's lane id. Every cell carries its own command; ages are at τ.

| Lane | counter | last dispatched (`watchdog.log`) | last report landed (marker grading) | last `LOG.md` round entry | last **lane-authored** commit (age at τ) | Dormancy verdict (pair used) |
|---|---|---|---|---|---|---|
| **kasegi** | 18<br>`cat .ufo/state/kasegi.round` | r18 launch @`2026-09-29T00:19:30-03:00`<br>`grep ' kasegi round=' .ufo/watchdog.log \| tail -1` (last `complete`: r17 @`00:19:30`, same command + `\| grep complete`) | r17 — `round-17/kasegi.md` **4708 B**, tracked, **ok + defect**<br>`ls -la .ufo/reports/round-*/kasegi.md \| sed -E 's#.*round-([0-9]+)/.*#\1#' \| sort -n \| tail -1` → 17; `wc -c`; `git ls-files` → tracked; zero in-repo resolvable commit (`grep -oE '\b[0-9a-f]{7,40}\b'` → only `1307b8b` = *external* `origin-work/open-bug-bounties` HEAD per its own line 24 — `git -C kasegi-shokunin cat-file -t 1307b8b` → fatal) | `— round 17` (`LOG.md:684`)<br>`grep -nE '^## Round [0-9]+\|— round [0-9]+' kasegi-shokunin/LOG.md \| tail -1`; **r16 absent** (`grep -cE '[Rr]ound 16\b'` → 0) | `0f2dca0` @`2026-09-28T22:10:19-03:00` **age 138 min**<br>`git -C kasegi-shokunin log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%h %aI'` | **ACTIVE** — pair **r17 + r15**; LOG carries both (r17 `:684`, r15 `:517`). r16 = 273 B failed marker, excluded |
| **kengaku** | 14<br>`cat .ufo/state/kengaku.round` | r14 launch @`2026-09-29T00:19:31-03:00`<br>same grep form | r13 — `round-13/kengaku.md` **4220 B**, tracked, **ok + defect** (WWKD *plan*, "Out of scope" declared; **zero** hex tokens ⇒ no resolvable commit; has evidence pointers ⇒ not a marker under the literal clause)<br>`ls -la .ufo/reports/round-*/kengaku.md \| sed -E 's#.*round-([0-9]+)/.*#\1#' \| sort -n \| tail -1` → 13; `grep -oE '\b[0-9a-f]{7,40}\b' .ufo/reports/round-13/kengaku.md` → empty | `— round 11` (`LOG.md:18`)<br>`grep -nE '^## Round [0-9]+\|— round [0-9]+' kengaku-shokunin/LOG.md \| tail -1`; **r13 absent** (`grep -cE '[Rr]ound 13\b' kengaku-shokunin/LOG.md` → **0**) | `f09ff1f` @`2026-09-28T21:15:23-03:00` **age 193 min** (fleet max)<br>same filtered `log -1` form | **ACTIVE — nearest miss (1 of 2 rounds)** — pair **r13 + r11**; LOG carries r11 only. See §4 ruling A/B: under reading B this row is the fleet's **first positive dormancy case** |
| **kake** | 17<br>`cat .ufo/state/kake.round` | r17 launch @`2026-09-29T00:19:31-03:00` | r16 — `round-16/kake.md` **12005 B**, tracked, **ok + defect** (no resolvable in-repo commit: `grep -c 'ab87a48' round-16/kake.md` → 0; its hex tokens `0de5eb9 9c28d29 bd02d10` all `cat-file -t` → fatal in every repo) | `— round 16` (`LOG.md:208`)<br>entry-scan `tail -1` | `ab87a48` @`2026-09-28T23:44:18-03:00` **age 44 min** | **ACTIVE** — pair **r16 + r15**; LOG carries both (`:208`, `:130`) |
| **kumitate** | 17<br>`cat .ufo/state/kumitate.round` | r17 launch @`2026-09-29T00:19:32-03:00` | r16 — `round-16/kumitate.md` **15354 B**, tracked, **ok** (cites `db61be0`, `git -C kumitate-shokunin cat-file -t db61be0` → commit) | `— round 16` (`LOG.md:746`) | `f9f8e4d` @`2026-09-28T23:37:47-03:00` **age 51 min** | **ACTIVE** — pair **r16 + r15**; LOG carries both (`:746`, `:667`). r7 = 122 B marker naming `7a4c9a0` → ok+defect, counted (not in this pair) |
| **kotoba** | 17<br>`cat .ufo/state/kotoba.round` | r17 launch @`2026-09-29T00:19:33-03:00` | r16 — `round-16/kotoba.md` **9700 B**, tracked, **ok** (cites `b25f37a` → commit) | `### Round 16` (`LOG.md:702`, addendum `:780`)<br>`grep -nE '^#{2,3} Round [0-9]+' kotoba-shokunin/LOG.md \| tail -1`; **r14 absent** (`grep -nE '[Rr]ound 14' kotoba-shokunin/LOG.md` → 4 hits, all *debt references* at `:491,:526,:563,:569` inside the Round-15 entry, no r14 entry) | `d85982d` @`2026-09-28T23:39:51-03:00` **age 48 min** | **ACTIVE — near miss (1 of 2 rounds)** — pair **r16 + r14**; LOG carries r16 only. r15 = 273 B failed marker, excluded |
| **kagi** | 17<br>`cat .ufo/state/kagi.round` | r17 launch @`2026-09-29T00:19:33-03:00` | r16 — `round-16/kagi.md` **15021 B**, tracked, **ok** (cites `587fda0` → commit) | `— round 16` (`LOG.md:593`) | `8a6ec16` @`2026-09-29T00:27:10-03:00` **age 1 min** (landed 8 min *after* its r17 launch line — lane live at τ) | **ACTIVE** — pair **r16 + r15**; LOG carries both (`:593`, `:502`) |
| **kama** | 2<br>`cat .ufo/state/kama.round` | r2 launch @`2026-09-29T00:19:34-03:00`<br>`grep ' kama round=' .ufo/watchdog.log \| tail -1` (last `complete`: r1 @`00:19:33`) | r1 — `round-1/kama.md` **10144 B**, tracked, **ok** (cites `c6199a2`; `git -C kama-shokunin cat-file -t c6199a2` → commit) | `## round 1` (`LOG.md:7`)<br>`grep -niE '^#{2,3} round [0-9]+' kama-shokunin/LOG.md \| tail -1` — **case-insensitive required**: the mandated case-sensitive matcher returns 0 (§5 defect 1) | `c6199a2` @`2026-09-28T23:15:05-03:00` **age 73 min** | **ACTIVE (insufficient history)** — **probation-minted / roster-row-pending** (`MANIFEST.json rounds[36]`, `type:"mint"`, `2d19a64`); dispatched-and-reported rounds = **{r1}** only (r2 dispatched, no report yet) ⇒ **no pair exists**; rule cannot fire. See §4.1 |
| **aggregator** (self) | 11<br>`cat .ufo/state/aggregator.round` | r11 launch @`2026-09-29T00:19:30-03:00`<br>`grep ' aggregator round=' .ufo/watchdog.log \| tail -1` (last `complete`: r10 @`00:19:29`) | r10 — `round-10/aggregator.md` **187 B**, tracked, **failed marker, excluded** (no changes, no evidence pointer, no commit)<br>`wc -c`; `git ls-files .ufo/reports/round-10/aggregator.md` → tracked | `## Round 9 — aggregator lane …` (`LOG.md:324`)<br>`grep -nE 'Round [0-9]+ — aggregator' LOG.md \| tail -1`; pair entry `## Round 8` (`LOG.md:213`) | **aggregator-authored** in main: `a2cac72` @`2026-09-28T22:35:27-03:00` **age 113 min**<br>`git log -1 --author='aggregator-shokunin' --format='%h %aI'` | **ACTIVE** — pair **r9 + r8**; LOG carries both (`:324`, `:213`). r10 failed marker excluded (the §12.1 r6+r4 precedent) |

**Dormant count under the literal rule: 0 / 8.** Under alternate reading B: **1 / 8** (kengaku) — see §4.

### Marker ledger (re-measured, all of it)
`find .ufo/reports -name '*.md' -size -400c | sort` (all reports < 400 B):

| report | size | grade (command: `wc -c`)+commit resolution |
|---|---:|---|
| `round-10/aggregator.md` | 187 B | **failed** — no commit (`grep -oE '\b[0-9a-f]{7,40}\b'` → empty) |
| `round-12/kengaku.md` | 274 B | **failed** — no commit |
| `round-13/protocol.md` | 275 B | failed (protocol lane; out of this table's rows) |
| `round-14/protocol.md` | 340 B | failed (protocol lane) |
| `round-15/kotoba.md` | 273 B | **failed** — no commit |
| `round-16/kasegi.md` | 273 B | **failed** — no commit (fleet-wrap closeout text) |
| `round-5/aggregator.md` | 254 B | **failed** — no commit |
| `round-7/kumitate.md` | 122 B | ok + defect — names `7a4c9a0` (`cat-file -t` → commit) |
| `round-8/kengaku.md` | 101 B | **failed** — no commit |
| `round-8/kotoba.md` | 120 B | ok + defect — names `8c300ad` |

No report in the 400 B–4 kB band was classified as a marker: the only sub-4 kB non-marker is **kengaku r13 (4220 B, plan-only)** — see §4.

---

## 3. Non-re-derivable cells

*(the ticket asks me to name these, not to hide them)*

1. **kengaku r13 grade — `could-not-evaluate` on the marker/ok boundary.** Cause: the report-contract clause predicates "marker" on a **conjunction** ("no changes, **no** evidence pointer, **no** resolvable commit"). r13 satisfies two conjuncts (no changes landed; no resolvable commit) but not the third (it carries file/line evidence pointers and 4220 B of text). No command can decide the conjunction's weight; only a human ruling can. **Both possible grades and their consequences are stated in §4 so the row is usable either way.**
2. **kasegi / kake "no resolvable commit" — resolvable as a *negative*, not as a number.** `git -C <repo> cat-file -t <hash>` fails for every hex token in both reports. Whether an *external* repo HEAD (`1307b8b`, kasegi r17 line 24) counts as "a real committed round-work hash" is again a ruling, not a measurement.
3. **The 681-file loss is not re-derivable; its *cause-set* is.** `.ufo/l0-questions.md` line 16 (kasegi r16) asserts `open-bug-bounties/.ufo-missions/groknight` lost **681 files / 41 dirs / 14 MB** at `2026-09-28T22:45:06.815511919-03:00`, with a baseline (`root files 3494→2813`, `.ufo-missions 2863→2182f/303→262d`). At `2026-09-29T03:29:56Z–03:30:11Z` I re-measured read-only: `find … /groknight -type f | wc -l` → **2156 files / 256 dirs**, `.ufo-missions` → **2164 f / 259 d**, `git -C <that repo> ls-files | wc -l` → **30**, `ls -d …/groknight/{directus,flyio,ghost,hyatt,launchdarkly-mbb-og,payloadcms,sanity,storyblok}` → **8/8 absent**. The delta **681** is `could-not-evaluate`: pruning continued after the baseline (kake r16 lines 18/19 log W3→W4→W5 at `01:45:06Z`, `≤02:05:07Z`, `02:19:20Z`, and a **W6** instant at or before kake's r17 baseline `03:20:19Z` is appended at `.ufo/l0-questions.md:20`, uncommitted — `git diff --numstat .ufo/l0-questions.md` → `1 0`, measured `2026-09-29T03:37:39Z`), and the pre-loss tree is not attested by any unit-consistent command. **Unit mismatch is itself the finding** (the ledger's own P-u lesson): line 16's "root files 3494→2813" cannot be `find -maxdepth 1 -type f` (now **9**) — the unit is unstated, so the number is unreproducible.

All other cells in §2 reproduce from the commands printed in them.

---

## 4. Rulings requested of the L1

### 4.1 kama with n = 1 landed round — **cannot satisfy the dormant condition**
The rule is predicated on **two consecutive** rounds that were *both* dispatched *and* reported in. kama's dispatched-and-reported set is `{r1}` (r2 launched `00:19:34`, no report at τ), so the predicate has **0 qualifying pairs** and is vacuously false. Verdict **ACTIVE (insufficient history)** — not "active by merit". Two supporting facts:
- **Wraps counted correctly:** `grep -E ' kama round=' .ufo/watchdog.log` → **6** lines total — `launch r1` (22:44:08), **3 ×** `wrap kama round=1 complete; NOT respawning (fleet-wrap)` (23:39:57, 23:47:29, 23:55:00), `complete r1` (00:19:33), `launch r2` (00:19:34). `awk '{print $2}' | sort | uniq -c` → `1 complete / 2 launch / 3 wrap`. All three wraps carry **round=1** and the *same* `fleet-wrap` semantics: they are **re-emissions by the wrap tick, not three completions**. Distinct completed rounds = **1**. Counting wraps as completions would inflate kama to n=4 and manufacture a phantom pair → dormant-looking; that is the trap in this row.
- **kama is probation-minted / roster-row-pending, and the rule's subject is therefore unpinned.** `MANIFEST.json rounds[36]` (`type:"mint"`, landed `2d19a64`) records the mint *in probation*; the roster row is withheld by the `PROTOCOL.md:28-36` sibling-mint clause until **≥3 verified self-iteration rounds** land. So kama's rank is a *live declaration* ("minted in probation", `MANIFEST.json` `minting_rule`: *"a shonen is minted when a domain demand is proven"*), not an unrecorded field. Two consequences the L1 owns: (i) the pending gate for kama is the **≥3-round probation bar**, not dormancy — the two windows run on the same counter and `PROTOCOL.md` states **no precedence** between them (a probation lane that goes silent is neither "dormant" nor "failed the probation bar" by any written text → **gap**); (ii) dormancy still cannot fire here, because the ≥3-round clause *presupposes* multi-round history that kama does not yet have.

### 4.2 Vanished province root — **the rule is silent; the lane counts identically** (flagged as a gap)
The literal predicate has exactly two inputs: (i) dispatched-and-reported rounds, (ii) `LOG.md` activity. **Province existence, province health, citation resolvability and domain viability are not among them.** So a lane whose province root vanished counts **identically** — no special row, no leniency, no auto-retirement (the rule is already only a review trigger). Verified the trigger itself: `ls -d ~/Projects/bounties` → `ls: cannot access …: No such file or directory` (**exit 2**); `ls -d ~/Projects/open-bug-bounties` → also absent. kasegi r15/r16 are the L0 filings (`grep -nE '^(kasegi|kake) \| round-(15|16|17)' .ufo/l0-questions.md` → **10** (kasegi r15), **16** (kasegi r16)); kake corroborates at **14** (r15) and **19** (r16), and a further line **20** (kake r17, FS-prune regime **W6** — `~/projects`, the lowercase twin) was **appended mid-wave** and is **uncommitted** (`git show HEAD:.ufo/l0-questions.md | wc -l` → 19 vs `wc -l` worktree → 20; `git diff --numstat .ufo/l0-questions.md` → `1 0`), measured `2026-09-29T03:37:39Z`. *(Line numbers here are **claims about a moving append-only file**, not identities — the L0 channel's own keying is len+sha1, and my first pass cited the kake r16 line as 18 before the W6 append.)* §14.18 measured the blast radius across 4 other surfaces + 17 main-repo files (routed D-150).

**Gap (routed, not resolved here): the dormancy rule cannot express "province lost", and this fleet has now produced four distinct failure modes it cannot rank** — (1) province root deleted externally (kasegi), (2) surviving province root losing 681 files (line 16), (3) a lane that keeps its `LOG.md` cadence while its province is dead (kasegi: LOG entries for r15/r17 `after` the root vanished, so the rule reads it **ACTIVE**), (4) a lane that *stops* recording `LOG.md` while its repo is only 193 min stale (kengaku). Modes 3 and 4 are the same score under the literal rule and opposite verdicts under reading B. The smallest repair that would make the rule testable in the direction that matters: make the predicate **per-round** ("neither of the two latest qualifying rounds carries a `LOG.md` entry") and admit an **external-viability input** that the integrator cannot self-issue.

### 4.3 Reading A vs Reading B — the load-bearing ambiguity (kengaku, kotoba)
- **Reading A (verdict on this table, literal):** *"records no `LOG.md` activity across two consecutive rounds"* predicates absence over the **whole span** ⇒ dormancy needs **both** rounds silent. Activity is present in one round of each near-miss span (kengaku r11, kotoba r16) ⇒ **ACTIVE**; **0/8 dormant**.
- **Reading B (the one that matters):** dormancy fires when the **latest** qualifying round of the pair is silent. Outcome on identical data: **kengaku DORMANT** (r13: no LOG entry — `grep -cE '[Rr]ound 13\b' kengaku-shokunin/LOG.md` → **0** — plan-only report, no non-aggregator commit in 193 min), kotoba **ACTIVE** (r16 entry present, debt only for the *earlier* pair round). Result: **1/8 dormant — the first positive test case in eight refreshes**, which §12.6/§14.15 have repeatedly named as the missing evidence for the rule's correctness.

**The marker clause is what decides kengaku.** Without it, r12 (274 B, no commit) would enter the pair, the pair would be **r13 + r12**, and the span would be silent in *both* readings ⇒ **dormant**. With the clause applied as inherited, r12 is excluded and the pair is **r13 + r11**, and only reading B fires. So the marker-exclusion rule + reading choice — two rulings, neither previously stress-tested — are jointly the difference between 0/8 and 1/8.

My verdict column keeps Reading A (it is the closer literal reading). The L1 should rule; the data for either is in the row.

---

## 5. Measurement defects found in the ticket's own command set (all verified, not asserted)

1. **The mandated LOG matcher `^#{2,3} Round [0-9]+` (case-sensitive) is host-broken for 6 of 7 lanes.** `grep -cE '^#{2,3} Round [0-9]+' <lane>-shokunin/LOG.md` → kasegi **0**, kengaku **0**, kake **0**, kumitate **0**, kagi **0**, kama **0**, kotoba **9**. Six lanes write bullets (`- 2026-09-28 — round N:`) and kama writes a **lowercase** heading (`## round 1`) — both invisible to the mandated pattern (per §13.5 item 14 this form is already known broken; confirmed at τ). Classified by content, not line number, as the ticket instructs.

   **Per-repo matcher census (independently filed by peer seat `L0Scout`, reproduced here verbatim at `2026-09-29T03:35:36Z` — counts agree exactly):**

   ```sh
   for l in kasegi kengaku kake kumitate kagi kama kotoba; do printf '%-9s bullet=%s heading_ci=%s heading_cs=%s\n' "$l" \
     "$(grep -cE '^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+' $l-shokunin/LOG.md)" \
     "$(grep -ciE '^#{2,3} [Rr]ound [0-9]+' $l-shokunin/LOG.md)" \
     "$(grep -cE '^#{2,3} Round [0-9]+' $l-shokunin/LOG.md)"; done
   # kasegi bullet=16 heading_ci=0 heading_cs=0   kengaku 16/0/0   kake 16/0/0
   # kumitate 17/0/0   kagi 18/0/0   kama bullet=1 heading_ci=1 heading_cs=0   kotoba bullet=8 heading_ci=9 heading_cs=9
   ```

   ⇒ the correct matcher is **per-repo**: date-bullet form for kasegi/kengaku/kake/kumitate/kagi, case-insensitive heading form for kotoba (9) and kama (1). **No verdict row in this table rests on the heading-only scan** — proven by re-running the pair-presence test under the per-repo matcher (`2026-09-29T03:35:55Z`): kasegi r17=1/r15=1, kengaku r13=**0**/r11=1, kake r16=1/r15=1, kumitate r16=1/r15=1, kagi r16=1/r15=1 — identical to the union-scan result in §2. Absence cells re-confirmed: kasegi r16=0, kengaku r12=0, kengaku r13=0, kengaku r14=0, kotoba r14=0 (`heading_ci(Round 16)`=2, `heading_ci(Round 14)`=0; bullet form also 0).
2. **The established entry scan `grep -oE '^## Round [0-9]+|— round [0-9]+'` also has a hole, and for kotoba it flips the verdict.** kotoba appends `### Round 15`/`### Round 16` **correction entries**, which `^## Round` misses: the established form returns `## Round 15` while kotoba's newest entry is **Round 16** (`LOG.md:702`). Under the established form kotoba's last entry (r15) falls *outside* its pair {r16, r14} ⇒ the span reads silent ⇒ **false DORMANT**. The mandated `#{2,3}` form gets kotoba right and the other six wrong; neither form alone is sound. The sound union matcher used here: `grep -niE '^#{2,3} [Rr]ound [0-9]+|— [Rr]ound [0-9]+'`.
3. **The ticket's commit command `git log -1 --invert-grep --author='aggregator'` does not filter by author.** Verified: `git -C kasegi-shokunin log -1 --format='%h %aI %an' --invert-grep --author='aggregator'` → `b021dc9 … aggregator-shokunin` — it returns *the aggregator commit itself* (`--invert-grep` inverts the `--grep` message pattern only; it is not an author filter). Used instead, per the §13.3 correction: `git -C <repo> log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%h %aI'`. Without it, 4 of 7 lanes' commit cells would report **this lane's** activity as the lane's (kasegi's cell would have read `b021dc9`, 69 min, instead of `0f2dca0`, 138 min).
4. **Author identities differ per repo** (kasegi/kake/kumitate/kagi lane commits are authored `Joao Pedro Veiga`; kengaku/kotoba/kama are authored `<lane>-shokunin`). A filter keyed on a literal `lane` name rather than on the *aggregator* identity would silently drop all kengaku/kotoba/kama lane commits.
5. **The fleet's standing "mints executed: 0" metric mis-reads a probation mint as no mint — and my own first pass repeated it.** `sum(1 for x in r if x.get('minted'))` tests the truthiness of the `minted` **array**, which is empty for *every* entry including `rounds[36]` (the kama mint). Correct query: `sum(1 for x in r if x.get('type')=='mint')` → **1**. Same command-class as §14.9's M3 metric and the ledger's own P-u lesson (a count must name its unit); measured at `2026-09-29T03:32:20Z` → `rounds 48 | type==mint 1 | roster adds 0`. Corrected in C8, and the kama row/§4.1 were rewritten after peer seat `L0Scout` filed the same finding.
6. **Wave-brief key assumption corrected (not mine to fix, recorded because I measured it):** the standing queue's max key is **`D-150`** (`grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -t- -k2 -n | tail -1` → `| D-150`, matching §14.18's routed row), **not `D-149`** as the round brief states. No key is proposed by this seat.

---

## 6. Re-run block (copy-paste from the main repo root)

```sh
date -u +'cutoff %FT%TZ'; git log -1 --format='main HEAD %h %aI'
# C1 counters
for l in kasegi kengaku kake kumitate kotoba kagi kama aggregator; do printf '%-11s %s\n' $l "$(cat .ufo/state/$l.round)"; done
# C2 dispatch / completion (kama: 3 fleet-wrap re-emissions all carry round=1 — do not count as completions)
for l in kasegi kengaku kake kumitate kotoba kagi kama aggregator; do printf '%-11s ' $l; grep " $l round=" .ufo/watchdog.log | tail -1; done
grep -E ' kama round=' .ufo/watchdog.log | awk '{print $2}' | sort | uniq -c   # 1 complete / 2 launch / 3 wrap
# C3 newest report + grade
for l in kasegi kengaku kake kumitate kotoba kagi kama aggregator; do n=$(ls .ufo/reports/round-*/$l.md | sed -E 's#.*round-([0-9]+)/.*#\1#' | sort -n | tail -1); printf '%-11s r%-3s %6s B\n' $l $n "$(wc -c <.ufo/reports/round-$n/$l.md)"; done
find .ufo/reports -name '*.md' -size -400c | sort      # marker class, exhaustive
# C4 LOG round, content-classified — PER-REPO matcher (§5 defect 1: the mandated case-sensitive heading form is 0/6 lanes;
#    the union form below is sound but the per-repo form is the one to fold):
for l in kasegi kengaku kake kumitate kagi; do printf '%-9s bullet=%s last=[%s]\n' $l \
  "$(grep -cE '^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+' $l-shokunin/LOG.md)" \
  "$(grep -oE '^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+' $l-shokunin/LOG.md | tail -1)"; done
for l in kotoba kama; do printf '%-9s heading_ci=%s last=[%s]\n' $l \
  "$(grep -ciE '^#{2,3} [Rr]ound [0-9]+' $l-shokunin/LOG.md)" \
  "$(grep -oiE '^#{2,3} [Rr]ound [0-9]+' $l-shokunin/LOG.md | tail -1)"; done
for x in 'kasegi 17' 'kasegi 15' 'kengaku 13' 'kengaku 11' 'kake 16' 'kake 15' 'kumitate 16' 'kumitate 15' 'kagi 16' 'kagi 15'; do
  set -- $x; printf '%-9s round %-3s bullet=%s\n' $1 $2 "$(grep -cE "^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round $2(:| |\$)" $1-shokunin/LOG.md)"; done
grep -nE 'Round [0-9]+ — aggregator' LOG.md | tail -2       # aggregator pair (shared file; filter is load-bearing)
# C5 last lane-authored commit (NOT --invert-grep — see §5 defect 3)
for l in kasegi kengaku kake kumitate kotoba kagi kama; do printf '%-9s ' $l; git -C $l-shokunin log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%h %aI %an'; done
git log -1 --author='aggregator-shokunin' --format='%h %aI'   # aggregator self-row
# C6 pair-round LOG presence test (kengaku r13, kasegi r16, kotoba r14, kagi r17, kake r17, kumitate r17, kasegi r18)
for x in 'kengaku 13' 'kengaku 12' 'kengaku 14' 'kotoba 14' 'kasegi 16' 'kasegi 18' 'kagi 17' 'kake 17' 'kumitate 17'; do
  set -- $x; printf '%-9s round %-3s -> %s\n' $1 $2 "$(grep -cE "[Rr]ound $2\b" $1-shokunin/LOG.md)"; done
# C7 vanishing province (read-only)
ls -d ~/Projects/bounties ~/Projects/open-bug-bounties; echo "exit=$?"
R=~/Projects/origin-work/open-bug-bounties; find $R/.ufo-missions/groknight -type f | wc -l; git -C $R ls-files | wc -l
grep -nE '^(kasegi|kake) \| round-(15|16|17)' .ufo/l0-questions.md | cut -c1-90   # pin the filings by content; line numbers MOVE
git show HEAD:.ufo/l0-questions.md | wc -l; wc -l <.ufo/l0-questions.md; git diff --numstat .ufo/l0-questions.md
# C8 mint ledger (row-count precondition) — NB: test `type=='mint'`, NOT truthiness of `minted` (§5 defect 5)
python3 -c "import json;m=json.load(open('MANIFEST.json'));r=m['rounds'];print([x['id'] for x in m['roster']],len(m['roster']),'| rounds',len(r),'| type==mint',sum(1 for x in r if x.get('type')=='mint'),'| roster adds',sum(1 for x in r if x.get('minted')))"
python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];[print(json.dumps(x)) for x in r if x.get('type')=='mint']"
grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -t- -k2 -n | tail -1   # measured D-150 (NOT the D-149 the wave brief assumed)
```

**Raw evidence (unit-check for §3 item 3):**
```
MEASURED_AT 2026-09-29T03:29:56Z
root files now: 9            total files now: 2744
.ufo-missions dirs: 259      .ufo-missions files: 2164
groknight: drwxr-xr-x ... Sep 28 23:19 .../.ufo-missions/groknight
MEASURED_AT 2026-09-29T03:30:11Z
groknight files: 2156        groknight subdirs: 256        ls-files: 30
directus/flyio/ghost/hyatt/launchdarkly-mbb-og/payloadcms/sanity/storyblok -> 8/8 "No such file or directory"
```

---

## 7. Confidence and gaps

- **obs [certain]** — every cell in §2 and every figure in §3–§5 is a pasted command output from τ; sources: `.ufo/state/*.round`, `.ufo/watchdog.log` (313 lines), `.ufo/reports/round-*/`, `<lane>-shokunin/LOG.md`, `PROTOCOL.md:30-45,145-160`, `MANIFEST.json`, `.ufo/l0-questions.md` (lines 10/14/16/19/20 — a **moving** append-only file: 19 lines at HEAD, 20 in worktree, measured `2026-09-29T03:37:39Z`), live `ls`/`find` on `~/Projects`.
- **inf [moderate]** — Reading A as the intended reading of "across two consecutive rounds" (*unverified*: no operator/integrator ruling exists; §12.6/§14.15 record the rule has never fired, so no precedent settles it).
- **Matcher hardening (peer correction absorbed, `2026-09-29T03:35:36Z`/`03:35:55Z`).** Peer seat `L0Scout` filed the per-repo matcher; reproduced here and the table re-keyed to it. **No verdict changed**: pair-presence under the per-repo matcher is cell-for-cell identical to the union scan (kasegi r17/r15 = 1/1; kengaku r13/r11 = **0**/1; kake r16/r15 = 1/1; kumitate 1/1; kagi 1/1; kotoba Round 16 = 2 headings / Round 14 = 0; kama Round 1 = 1; aggregator Round 9/Round 8 = 1/1). `0 / 8` under reading A and `1 / 8` (kengaku) under reading B stand.
- **gap** — (a) the marker clause's conjunction is unpriced for a plan-only report (kengaku r13) — two grades, opposite fleet verdicts; (b) the feeding rule input "province viability" does not exist anywhere in `PROTOCOL.md`; (c) kengaku r14 is dispatched with no report at τ — if r14 also lands reportless, the pair becomes **r14 + r13** and *both* readings agree on **dormant**, making r14 a live watch item on a ~15-minute scale; (d) `PROTOCOL.md` states no precedence between the **≥3-round sibling-mint probation bar** and the **2-round dormancy window** for a probation lane like kama that goes silent (§4.1). *(The earlier gap "kama's rank is unrecorded" is **closed**: `MANIFEST.json rounds[36]` records the probation mint — §1, §5 defect 5.)*

**Lanes where a reported number could not be re-derived:** **kengaku** (r13 grade — conjunction, §3.1); **kasegi** and **kake** (whether the cited externals/no-commits satisfy "resolvable commit", §3.2); **the 681-file figure** (unit-unspecified baseline, §3.3). Nothing else in the table is estimated.