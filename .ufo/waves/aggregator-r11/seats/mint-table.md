# Mint / watchlist candidate table — aggregator refresh 8 (round 11)

**Seat:** MintScout (L2, aggregator lane). **Scope:** read-only. Only this file written.
**All measurements taken at:** `2026-09-29T03:26–03:30Z` (`date -u` → `Tue 29 Sep 2026 03:27:17 AM UTC`).
**Repo root for every command:** `/home/vgpnk/Projects/shokunin` (main repo).
**D-key queue:** max existing key is now **D-150** (`grep -rhoE 'D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -t- -k2 -n | tail -3` → `D-149 D-150 D-150`; D-150 = `cc6d9d4`). Rows below are **proposed text, no keys** — L1 assigns.

> **CORRECTION BANNER.** This table was first drafted on the brief's premise that the kama mint left **no** ledger record (census `if x.get('minted')` → 0). That is **false**: `MANIFEST.json` `rounds[36]` is a `type: "mint"` probation entry (`2d19a64`). The `0` is a **falsy-empty-list** artifact. §1.1/§1.2/§1.5 and the §2 kama row are corrected; the mint is **ledger-recorded**, and the real defect is the census **instrument**. Credit: `agent://L0Scout`, independently re-derived here.

---

## 1. KAMA GRADUATION — evidence block

### 1.1 Verdict — **minted-in-probation, LEDGER-RECORDED** *(corrected; see §1.5)*

**The mint IS recorded.** `MANIFEST.json` `rounds[36]` carries a `type: "mint"` entry:

```bash
python3 -c "import json;d=json.load(open('MANIFEST.json'));print([e for e in d['rounds'] if e.get('type')=='mint'])"
# [{'round': 11.5, 'date': '2026-09-28', 'type': 'mint', 'minted': [], 'notes': 'sibling-mint allowance landed in
#  PROTOCOL.md Lifecycle; kama-shokunin minted in probation (local model serving & endpoint health — aggregator
#  mint-eligible r4/r6/r7, demand instances: kagi r3 + kengaku r4 endpoint-drift 8080->34113). Roster row withheld
#  until >=3 verified self-iteration rounds per the new clause; lane wired into watchdog (m_flash, axes
#  operability+freshness).'}]
git show 2d19a64 --stat      # integrator@shokunin.local 2026-09-28T22:44:21-03:00: MANIFEST.json + PROTOCOL.md (+15)
git show 2d19a64 -- PROTOCOL.md | grep -n -A12 'sibling mint'   # lands the "Sibling mint (lane-initiated)" clause
```

So `minted: []` and the 6-id roster are the **designed probation shape**, not a missing record: PROTOCOL.md's new clause says the roster row is withheld until the sibling self-iterates ≥3 verified rounds, and "probation state is recorded in `rounds[].notes` meanwhile, not as a roster row." kama holds 1 completed round (r1) + 1 live (r2) ⇒ **withholding is correct as of this refresh**. The two commits are complementary, not contradictory: `2d19a64` (22:44:21) = ledger record + protocol clause; `17c1fad` (00:19:02) = MISSION.md kama row + relaunch.

> **Correction to this round's brief.** The brief's instrument — reproduced verbatim below — reports `0` because `x.get('minted')` returns `[]`, which is **falsy**:
> `sum(1 for x in r if x.get('minted'))` → **0 (buggy)** · `sum(1 for x in r if 'minted' in x)` → **35** · `sum(1 for x in r if x.get('type')=='mint')` → **1 ← correct**. The mint was never unrecorded; the census was blind to it. See §1.5, which also names the prior-refresh cells this contaminated.

| Half | Measurement | Result |
|---|---|---|
| ledger record | `python3 -c "import json;d=json.load(open('MANIFEST.json'));print([e for e in d['rounds'] if e.get('type')=='mint'])"` | **`rounds[36]` = `{round:11.5, type:"mint", minted:[], notes:"…kama-shokunin minted in probation…"}`** committed `2d19a64` (integrator@shokunin.local) |
| PROTOCOL clause | `git show 2d19a64 -- PROTOCOL.md \| grep -n -A12 'sibling mint'` | **"Sibling mint (lane-initiated)"** landed: step (d) — roster row added only after ≥3 verified self-iteration rounds; probation recorded in `rounds[].notes` meanwhile |
| directive / roster-of-record | `git show 17c1fad -- MISSION.md \| grep -n kama` | `36:+| kama \| `kama-shokunin/` \| `@m_swe` \| operability + freshness (local model serving/endpoints) \|` → **kama row landed** |
| lane repo exists | `ls -la kama-shokunin/` + `git -C kama-shokunin log --format='%h %aI %s'` | repo present (MINT.md 3891 B, PROVINCE/SKILL/LOG/SCORECARD/SHONEN/corpus/registry/tools); **2 commits**: `9cee9fc 2026-09-28T22:42:49-03:00 seed: kama shonen`, `c6199a2 2026-09-28T23:15:05-03:00 round-1: operability axis …` (HEAD `c6199a2`) |
| MANIFEST roster | `python3 -c "import json;m=json.load(open('MANIFEST.json'));print([r['id'] for r in m['roster']])"` | `['kasegi', 'kengaku', 'kake', 'kumitate', 'kotoba', 'kagi']` → **6 ids, kama absent — designed probation withholding** (PROTOCOL step (d)) |
| MANIFEST mint census | `python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(sum(1 for x in r if x.get('type')=='mint'))"` | **1** — the `rounds[36]` probation mint. (The brief's `if x.get('minted')` prints **0**: empty list is falsy. `'minted' in x` → 35.) |
| dispatch | `grep -n -i kama .ufo/watchdog.log` | `22:44:08-03:00 launch kama round=1 runId=shokunin-r1-kama-r1790646247`; `00:19:33-03:00 complete kama round=1; respawning`; `00:19:34-03:00 launch kama round=2 runId=shokunin-r2-kama-r1790651973` |
| state | `cat .ufo/state/kama.mission .ufo/state/kama.round` | `shokunin-r2-kama-r1790651973` / `2` — round 2 dispatched, not-yet-reported |
| report | `wc -l .ufo/reports/round-1/kama.md` | **145 lines**, cites `c6199a2` in `VeigaPunk/kama-shokunin` — marker grading = **ok + defect** (report exists, names a resolvable commit) |
| MINT.md | `head -30 kama-shokunin/MINT.md` | mint cause recorded: kagi r3 + kengaku r4 independent discoveries of endpoint drift; "model serving — **no province owns it**" |

### 1.2 What the correction changes for the standing tables

- **kama is not a missing record — it is a probation lane.** Its row is sourced from **two real places**: `MANIFEST.json` `rounds[36]` (`type: "mint"`, probation) and `MISSION.md:19`. Key it as `probation-minted`, not `minted-unrecorded`.
- **Dormancy table (§12.1) still re-keys to 7 lane rows** (kama added), but kama's row is a **probation** row: PROTOCOL step (d) withholds the roster entry until ≥3 verified self-iteration rounds, so dormancy/promotion grading for kama does **not** read the `roster` list — it reads `rounds[36].notes` + the lane's own rounds.
- **Mint table (§12.2): strike kama's candidate row**, replace with `status: probation-minted (rounds[36], 2d19a64)`; the graduation condition is **3 verified self-iteration rounds** (kama holds 1 completed + 1 live ⇒ 2 to go).
- **A ledger-record defect DOES exist, but it is the instrument, not the record:** every standing mint census in this ledger uses `if x.get('minted')`, which is falsy for `[]`. See §1.5. The fix is a one-token change to the re-run command (`x.get('type')=='mint'`), plus correcting `SCORECARD.md` M2.

### 1.3 Live medal-defect found on the way (kama's own r1 L0 line, still open)

```bash
cd /home/vgpnk/Projects/shokunin
cat -n .gitignore                      # lines 1-6: kasegi/kengaku/kake/kumitate/kotoba/kagi-shokunin; NO kama-shokunin/
git check-ignore -v kama-shokunin      # (exit 1) → not ignored
git check-ignore -v kumitate-shokunin  # .gitignore:4:kumitate-shokunin/  (exit 0)
git status --short                     # ?? kama-shokunin/   ?? .ufo/prompts/kama-round-2.md
```
Confirmed live at `03:27Z`: the nested lane repo shows as `??` in the main tree, so any `git add -A` stages it as an embedded gitlink. **The other half of kama's r1 hygiene line has been resolved** — `.ufo/state/kama.mission`/`kama.round` are now **tracked** (`git ls-files .ufo/state | wc -l` → 18; `git status --short .ufo/state` → 18× ` M`, no `??`) after `17c1fad`. So the hygiene line is half-landed, half-live.

### 1.4 kama LOG-token matcher defect (cross-ref for the dormancy seat)

`grep -cE '^#{2,3} Round [0-9]+' kama-shokunin/LOG.md` → **0** (exit 1). kama's LOG uses **lowercase** `## round 1 — operability axis (measured via freshness)`. The fleet token scan is case-sensitive per the inherited rule, so kama's genuine LOG activity scores 0 tokens. **Classify kama by report/commit evidence, not by the token scan**; recommend the L1 extend the matcher to `[Rr]ound` or normalize kama's heading.

### 1.5 SELF-DEFECT — the falsy-empty-list census filter (contaminated prior cells)

**Defect:** the standing mint census `sum(1 for x in r if x.get('minted'))` tests **truthiness**, and every `rounds[]` entry carries `minted: []` (empty by schema — the mint *events* are `type: "mint"` rows, whose own `minted` list is also empty). The filter returns 0 no matter how many mints exist. Correct forms: `x.get('type')=='mint'` → **1** · `'minted' in x` → **35** · truthiness → **0**.

```bash
cd /home/vgpnk/Projects/shokunin
python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print('truthy',sum(1 for x in r if x.get('minted')),'| key',sum(1 for x in r if 'minted' in x),'| mint',sum(1 for x in r if x.get('type')=='mint'))"
# truthy 0 | key 35 | mint 1
```

**The field has never held a value in this ledger's lifetime** — across **all 12 historical revisions** of `MANIFEST.json`, the truthy count is 0 (12/12), so `minted` is **vestigial** and truthiness is the wrong predicate:

```bash
cd /home/vgpnk/Projects/shokunin
git log --format=%h -- MANIFEST.json | while read c; do git show $c:MANIFEST.json | python3 -c "import sys,json;print(sum(1 for e in json.load(sys.stdin)['rounds'] if e.get('minted')))"; done | sort | uniq -c
#      12 0
```

**Cells this contaminated (exact lines, re-derived; final text edit is L1's):**
- `SCORECARD.md:178` — M2 row: `| M2 | mints executed | 0 | 0 — correct: the bar is met only by kama and the ruling is operator-side | python3 -c "import json;print([r.g…` (the cell and its embedded re-run command both use the falsy predicate; the "15 × `[]`" reading is the schema, not absence).
- `SCORECARD.md:208` — aggregator-history cell: "mints executed 0 over 22 rounds entries".
- `AGGREGATE.md:940` — "**M2 unchanged and correct: 0 mints executed** — the bar is met only by kama and the ruling is operator-side." (refresh-5 §).
- Correct reading of all three: **1 mint event recorded** (`rounds[36]`, probation); the `rounds[].minted` lists are empty **by schema** across every revision, never by absence of mints.
- Schema note: exactly one `type: "mint"` entry exists and **no** entry in any revision carries a non-empty `minted` list ⇒ either set `rounds[36].minted = ["kama"]` or drop the field and standardize on `type` — and fix the census command, or every future refresh re-reports 0.

**Provenance:** this seat initially reproduced the brief's falsy filter and reported "mint executed but UNRECORDED". L0Scout (`agent://L0Scout`) surfaced `rounds[36]`; this seat re-derived it independently from `MANIFEST.json` + `2d19a64` (stat + PROTOCOL diff) before correcting. The error was the instrument; the corrected finding is *"the ledger's mint census is blind to `type:'mint'` probation rows"*, **not** *"the mint went unrecorded."*

---

## 2. Candidate table (re-run, refresh 8)

Counting rules per the round contract (marker grading; LOG `^#{2,3} Round [0-9]+`; commit-age excludes aggregator-authored seat commits; dormancy = no LOG activity across two consecutive dispatched-and-reported rounds).

| Candidate | Surface | Demand instances | Owning-province test | Bar verdict (2026-09-29T03:27Z) | Status | Re-run command |
|---|---|---|---|---|---|---|
| **kama** *(GRADUATED to probation — leaves the candidate watchlist)* | local model serving & endpoint health | 2 unplaceable: `.ufo/reports/round-3/kagi.md:23-26` + `.ufo/reports/round-4/kengaku.md:20-23` (both re-verified at refresh 5, repo-qualified short hashes) | `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` → exit 1; `kengaku/PROVINCE.md:24-25` "Not owned: the model-serving plane" | **Bar met — MINTED (probation)** | **probation-minted, ledger-recorded**: `MANIFEST.json` `rounds[36]` = `{round:11.5, type:"mint", notes:"…kama-shokunin minted in probation…"}` @ `2d19a64`; PROTOCOL "Sibling mint (lane-initiated)" clause landed same commit; roster row **withheld by design** until ≥3 verified self-iteration rounds (kama: 1 done + 1 live ⇒ 2 to go) | `python3 -c "import json;d=json.load(open('MANIFEST.json'));print([e for e in d['rounds'] if e.get('type')=='mint'])"` |
| **kessho** | CI/verification harnesses | **re-derived (my matcher, stated):** `git -C <lane>-shokunin ls-files \| grep -iE 'verif\|check\|gate\|drift\|claim-ledger\|selftest\|grader'` → raw **6 lanes / 209 files @ 03:28:26Z** (kasegi 3, kengaku 5, kake 2, kumitate 7, kotoba **180** (fixture-inflated), kagi 11, kama 1). Refined (exclude `/(fixtures\|knowledge\|lessons)/`): **5 lanes / 29** (kasegi 1, kengaku 5, kumitate 4, kotoba 11, kagi 8; kake 0 — its harness files are `corpus/knowledge/*.md`). **Volatile:** kagi's refined count moved 7→8 inside this refresh window (kagi r17 live; the new file is `corpus/scope-gate.sh`) — quote both with their stamps. **New builder instances r14–r18:** kagi r14 (`corpus/claim-ledger.sh` sixth mode `docs`, report :39 `DOC_AUDIT: BROKEN …` exit 1); kagi r15 (`corpus/checklist-run.sh` + `checklist.tsv`, `CHECKLIST_SELFTEST: PASS (34 cases)`); kotoba r14 (`verifiers/fixtures/surfaces/*` + 4 inventory fixtures, report :32). **0 refusals** (`grep -rn -iE 'refus\|declin' .ufo/reports/round-1[4-8]/` → all hits concern refused *commands*, none a lane refusing verification work) | Every instance absorbed in-province; the one unplaceable-shaped demand (fleet gate *standard*, kengaku r10 "no sibling owns an evidence-replay gate", L0 line 7) **names its owner**: protocol/integrator — D-82 ruled/deferred with a date (protocol r11) | **Below bar** — 0 unplaceable demand. Re-derived counts **differ from §13.3's "6 lanes / 9 artifacts"**; my raw matcher inflates on kotoba fixtures, so quote the refined count as the comparable figure | unchanged; trigger fired again (builder instances #4+) but all in-province | `for l in kasegi kengaku kake kumitate kotoba kagi kama; do echo -n "$l: "; git -C $l-shokunin ls-files 2>/dev/null \| grep -iE 'verif\|check\|gate\|drift\|claim-ledger\|selftest\|grader' \| grep -vcE '/(fixtures\|knowledge\|lessons)/'; done` |
| **umihotaru** | fleet/pane wall ops | **1** — `scripts/shokunin-watchdog.sh` (integrator-owned tooling); secondary owned: kumitate `corpus/knowledge/sighting-wall.md` @ `eca3d14` | Owned, not a domain | **Below bar** | **No new instance**: full-repo sweep `grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/` → **16 matches in 3 files** (`AGGREGATE.md` = its own tables; `round-6/protocol.md`; `round-7/aggregator.md`). Restricted to round dirs, `grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-*/` → **2 files only (round-6, round-7)**, **zero** in `round-8..18` ⇒ nothing new since the refresh-7 cutoff | `grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-*/; grep -rln -i 'umihotaru\|kagemusha' .ufo/reports/round-*/` |
| **kagemusha** | substrate adapters & mirrors | **3 distributed, served** — kengaku `corpus/knowledge/ledger-route-telemetry.md` @ `2575be6`; kumitate `corpus/knowledge/route-resolution.md` @ `0ac95e1`; kake `corpus/knowledge/mirror-pitfalls.md` @ `cd5b381` | Distributed across three served provinces; no refusal | **Below bar** | **D-86 RULED** (protocol r11 §Rulings 1) — `fleets/registry.json` re-split is intra-province, not a mint demand. No new instance in `round-14..18` | same command as umihotaru (shared matcher) |
| **axis-framework-stewardship** | SCORECARD templates, per-axis proxies, rollout order | **0 unserved** — surfaced refresh 4 (§11.6); template proposals routed to protocol (§11.5 P-h/P-i); per-repo cards are lane work | Not a domain — protocol + operator work; routed, not refused | **Below bar** (refresh-4 ruling stands) | **Re-check DISCHARGED**: `grep -rn -i -e axis-framework -e stewardship .ufo/reports/round-1[1-9]/` → **exit 1** (0 mentions, r11–r19). Protocol r11 report `392b3c7` carries 0 mentions | `grep -rn -i -e axis-framework -e stewardship .ufo/reports/round-1[1-9]/; echo "exit=$? (1 = discharged)"` |

**Mints executed recount (corrected instrument):** `python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(sum(1 for x in r if x.get('type')=='mint'))"` → **1** (the `rounds[36]` kama probation mint, `2d19a64`). The brief's `if x.get('minted')` variant → **0** — an artifact of empty-list falsiness, not a missing record (§1.5). So **1 mint executed / 1 recorded**, and the prior refreshes' "0 mints executed" is a stale reading produced by the falsy filter.

---

## 3. NEW CANDIDATE ASSESSMENTS (refresh-8 sweep)

Sweep surfaces: `.ufo/reports/round-14/` … `round-18/` (+ `scratch/` under r15), `kama-shokunin/**`, and `.ufo/l0-questions.md` lines added at `17c1fad`.

**L0 delta measured:** `wc -l .ufo/l0-questions.md` → **19** (HEAD and `17c1fad` identical); `git show e333e7c:.ufo/l0-questions.md | wc -l` → **6** ⇒ **13 lines added at `17c1fad`** (one pre-existing line, `5` = kake r12, was also rewritten). Lane distribution now: kasegi 3, kama 3, kake 3, protocol 2, kumitate 2, aggregator 2, kotoba 1, kengaku 1, kagi 1.

### 3.1 NEW — filesystem-drift / vanished-roots forensics  → **above bar (mint-eligible, unplaceable); recommend L0 routing**

- **Surface:** `~/Projects` root attrition and its *attribution* — who owns filesystem deletion/prune forensics for paths the fleet cites.
- **Demand instances (≥6, across 3 lanes, all dated 2026-09-28/29):**
  1. kasegi r15 (`.ufo/reports/round-15/kasegi.md:9-46`, L0 line 1): `~/Projects/bounties` — the lane's PROVINCE root and anchor of ~376 SKILL.md citations — **gone**; `~/Projects` dir mtime `2026-09-28T20:51:31-03:00`; 18/18 corpus-attested surfaces absent, 0/18 present; actor UNDETERMINED.
  2. kasegi r16 (L0 line): SECOND in-round loss — `~/Projects/origin-work/open-bug-bounties/.ufo-missions/groknight` lost **8 mission dirs / 681 files / 41 dirs / 14 MB** at `2026-09-28T22:45:06-03:00`; not recoverable.
  3. kake r15 (`.ufo/reports/round-15/kake.md:25-31`, L0 line): `~/Projects/ufofsdbeta` + `ufofsdbeta-kimi-review` — **verified PRESENT at kake r1** — absent now; `ephemeral/wz1` emptied; same-window corroboration.
  4. kake r16 (`.ufo/reports/round-16/kake.md:137-144`, L0 line): Revenger bounds a **live, escalating prune regime** — five instants W1 ≤23:51:31Z, W2 00:42:39Z, W3 01:45:06Z, W4 `.ufo-missions` 262→2 dirs ≤02:05:07Z, W5 groknight re-touched 02:19:20Z; actor UNDETERMINED; the "fleet GC" hypothesis **not confirmed** (dispatcher-daemon.out / fleet-ledger.jsonl carry no unlink records).
  5. kotoba r14 (`.ufo/reports/round-14/kotoba.md:113`): `~/Projects/bounties` remains GONE — third-lane independent confirmation.
  6. kake r15 report :42 — sentinel guard 47/47 byte-identical while the roots drifted (proves the guard does not cover this surface).
- **Owning-province test:** `grep -il 'filesystem\|retention\|forensic\|attrition' *-shokunin/PROVINCE.md` → **only `kasegi-shokunin/PROVINCE.md:6`**, and that line is a *statement of fact* ("`~/Projects/bounties` was removed from the filesystem at …"), **not a claim of ownership**. No lane's PROVINCE.md claims filesystem retention/GC/deletion forensics. The plausible mechanism is operator-side (`~/Projects/origin-work/ufo-fsd-alpha/.ufo/` retention/GC), which is **outside the fleet roster** — hence unplaceable.
- **Bar verdict:** **ABOVE the bar on demand + ownership** (≥6 instances, 3 lanes, no province owns, escalating and continuing) — the strongest new candidate of this refresh and textually the same shape as kama's pre-mint state (two independent discoverers, no owner). **Missing half vs kama:** no lane has *refused* it as out-of-province, and the "domain vs operator incident" question is operator-side. ⇒ **blocked-external pending an L0 ruling**, held as a watchlist row.
- **Proposed L0 text (no key):** `aggregator | round-11 | ~/Projects root attrition (5 lanes cite paths there): kasegi r15/r16 lost bounties + groknight −681f, kake r15/r16 corroborate an escalating prune regime (W1–W5), kotoba r14 confirms; actor UNDETERMINED, mechanism unconfirmed (ufo-fsd-alpha retention/GC plausible). No lane's PROVINCE.md owns filesystem/retention/deletion forensics (grep → only kasegi PROVINCE.md:6, a fact statement). Mint a forensic/retention province, or rule it an operator incident? If a province, name the write scope — the surface is outside every lane repo.`
- **Proposed D-row text (no key):** `routed | operator | new mint candidate: filesystem-drift/vanished-roots forensics (unplaceable, ≥6 instances, kasegi/kake/kotoba) — bar met, blocked-external on the operator domain-vs-incident ruling`.
- **Re-run command:** `grep -rn -iE 'vanished|GONE from the filesystem|attrition|prune regime|~/Projects.*(absent|gone|removed)' .ufo/reports/round-1[4-8]/*.md .ufo/reports/round-1/kama.md; grep -il 'filesystem\|retention\|forensic\|attrition' *-shokunin/PROVINCE.md`

### 3.2 NEW — fleet-hygiene / meta-file governance  → **below bar (owner exists: operator/integrator); recommend a hygiene D-row**

- **Surface:** main-repo meta-files — `.gitignore` lane coverage, `.ufo/state` / `.ufo/prompts` tracking policy, driver/template text.
- **Demand instances (≥5, across 3 lanes):**
  1. kama r1 L0 line 3: `.gitignore` omits `kama-shokunin/` → **verified live at 03:27Z** (§1.3: `git check-ignore -v kama-shokunin` exit 1; `git status --short` → `?? kama-shokunin/`).
  2. protocol r10 (`.ufo/reports/round-10/protocol.md:146-147`): ".ufo/state (16 files) + watchdog.log are tracked although PROTOCOL.md said untracked, so every round starts with a dirty tree." (At 03:27Z verified: 18 tracked, 18× ` M` — still churning.)
  3. protocol r10 L0 line 2: driver/template debt — `lane_prompt()` emits 1 of 5 child-lane contract items; `report_of()` completes a mission on file existence (a 101-byte marker advanced kengaku 8→9).
  4. protocol r10 :154 / :194 / :216: `corpus/lessons/round-6-aggregator-audit.md` untracked in **all six** child repos; kagi drift-gate baselines untracked at round-9.
  5. kake r14 (`.ufo/reports/round-14/kake.md:111`): kake's report **untracked in the main repo** at r14 open.
- **Owning-province test:** `PROTOCOL.md:410` — "`MISSION.md`, `AXES.md`, `CORPUS.md`, and `scripts/` are operator-side integrator files"; `PROTOCOL.md:84` "the corrected `lane_prompt()` text [is] required, since `scripts/` is operator-side"; `PROTOCOL.md:419` "untracking them is operator-side". ⇒ **the owner EXISTS and is named (operator/integrator), it is simply slow** — this is a *placeable* surface, so it fails the unplaceable-demand test.
- **Bar verdict:** **BELOW bar — no mint.** Correctly a hygiene backlog, not a province. Note the asymmetry: one of kama's two hygiene complaints (state-file tracking) has since landed (§1.3), the other (`.gitignore`) is still live — so the *surface* is real and recurring but owned.
- **Proposed D-row text (no key):** `routed | operator | fleet-hygiene backlog (owned, not mintable): (a) append kama-shokunin/ to .gitignore (kama r1, verified live 2026-09-29T03:27Z); (b) .ufo/state tracked-but-churning vs PROTOCOL "untracked" (protocol r10); (c) lane_prompt() 1-of-5 contract items + report_of() file-existence closure (protocol r10).`
- **Re-run command:** `cat -n .gitignore; git check-ignore -v kama-shokunin; git status --short; grep -n -i 'operator-side' PROTOCOL.md`

### 3.3 Other sweep results (evaluated, no row warranted)

- **"no lane owns / no province / unowned" phrase scan r14–r18:** only 3 hits, all low-signal — `round-14/kake.md:119` ("unowned watchdog/sibling churn" — describes kake's own env, not a demand), `round-16/kagi.md:162` (a link-resolution scope note), `round-17/kasegi.md:39` ("no province re-point, network, credential, or target work" — a boundary statement). **No new unplaceable demand.**
- **kama repo phrase scan:** all `unowned`/`no province` hits are kama's own province claims (`corpus/knowledge/consumer-registry.md:38,68-71`, `MINT.md:22,45`) — i.e. inside the now-minted kama domain, not a new candidate.
- **`round-18/` is empty** (round in progress) — no evidence to grade.
- **kasegi r16 report (`.ufo/reports/round-16/kasegi.md`, 273 B) is a marker**: "# kasegi round-16 closeout (marker) … In-flight repo work survives in the child repo's working tree; next round resumes there." It names no commit hash. Its marker grading / dormancy consequence belongs to the dormancy + grade seats; flagged here because it sits inside my kessho/FS-drift sweeps. Cross-ref: `wc -c .ufo/reports/round-16/kasegi.md` → 273.

---

## 4. Hand-offs for the L1 assembler

1. **Key kama as probation, not as a candidate or a missing record.** Re-key §12.1 to 7 lane rows; kama's row sources `MANIFEST.json` `rounds[36]` (`type:"mint"`) + `MISSION.md:19`. Replace §12.2's kama candidate row with `status: probation-minted — graduation condition = ≥3 verified self-iteration rounds (2 to go)`.
2. **Fix the mint census instrument (`SCORECARD.md` M2 + `AGGREGATE.md` re-run lines).** Replace `if x.get('minted')` with `if x.get('type')=='mint'`; correct M2 from "0 mints executed" to **1**. Decide the vestigial-`minted`-field question (populate `rounds[36].minted=["kama"]` or drop the field). See §1.5.
3. **Route two new candidate rows:** filesystem-drift forensics (**above bar, blocked-external**, proposed L0 + D text §3.1) and fleet-hygiene (**below bar**, proposed D text §3.2). No keys assigned (max existing D-150, `cc6d9d4`; keys are L1's).
4. **Note the kama LOG-token matcher defect** (§1.4) for the dormancy seat — grade kama on report/commit evidence, not the case-sensitive token scan.