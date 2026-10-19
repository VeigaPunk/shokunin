# kaika W1: protocol drift map (canonical kimi-shokunin, fleet root, host bindings)

Probe: W1Drift, revenger seat, 2026-10-19. Read-only. Uses only local evidence: git history, file bytes, driver logs and runtime paths. `web_search` was not used because nothing in this assignment needed it. This file is for the D5 canonical-sync writer, the parent (tower L1) and the operator.

## Measured revisions

| tree | path | branch @ HEAD | commit date (-0300) | remote |
|---|---|---|---|---|
| canonical | `~/Projects/kimi-shokunin` | main @ `bc7d690` | 2026-10-13 16:57 | live `origin/main` = **`b3ca98f`**, which is 3 commits ahead (`git -C ~/Projects/kimi-shokunin ls-remote origin`) |
| D5 worktree | `~/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon` | kaika/canon-sync @ `bc7d690` | n/a | clean (`git status --short` empty) |
| fleet root | `~/Projects/shokunin` | master @ `31baf5c` | 2026-10-19 17:03 | `## master...origin/master` |
| OMP/Devin binding | `~/.agents/skills/shokunin` → symlink → `~/Projects/ompskills/.omp/skills/shokunin` | main @ `0bddb85` | 2026-10-13 12:05 | **ahead 1**, unpushed |
| Kimi binding | `~/.kimi-code/skills/shokunin` → symlink → `~/Projects/myskills/shokunin` | main @ `fd9ed8c` | 2026-10-16 22:47 | in sync |

The assignment named `~/.agents/skills/shokunin/SKILL.md` as "the host binding". That path is itself a symlink into ompskills (`find ~/.agents/skills/shokunin -maxdepth 0 -printf '%l'`). A second, separate binding also exists: the Kimi mirror in myskills. Both are mapped below.

---

## 0. Findings in brief

1. **Three entry points load three different protocols** (§2):
   - Fleet rounds run the amended protocol.
   - OMP/Devin `/skill:shokunin` loads the canonical pre-amendment (one-axis) protocol. The binding also says canonical wins on process.
   - Kimi `/skill:shokunin` loads a fleet mirror that is missing `LEARNING.md`.
2. **The fleet's six protocol files are canonical `812f1da` plus exactly two fleet-first changes.** The fleet re-vendored those bytes in `e867f78` (6/6 byte-identical). The two changes are:
   - **`79752af`**, Registry home (2026-10-15). Admission is not on record (D02).
   - **`84bade0`**, operator amendment 2026-10-16: multi-claim rounds, capabilities table, stagnation nudge, exploratory claims (D01).

   Nothing flows the other way: the canonical tree has no protocol text the fleet lacks. `CORPUS.md` is byte-identical in both.
3. **Craft-hours is fully gone.** Both adds were reverted byte-clean, and the sweep finds 0 live remnants in all four trees (V3). Nothing in this checklist brings it back. Never cherry-pick `ee1e5d6` or `7e81867`.
4. **P0 blocker (outside the protocol files).** Fleet HEAD `31baf5c` committed kotoba-shokunin's `b7470d7` (round 36) files over the fleet-root `LOG.md` and `SCORECARD.md`; the blobs are byte-identical (D18):
   - It deleted 845 and 395 lines respectively.
   - It removed the protocol lane's registry-home section, which is the structure D02 defines.
   - Every kaika fleet worktree is branched from that commit.
5. **The fleet's `scripts/shokunin-watchdog.sh` is a stale fork** (D04): a dead launcher path, hardcoded lanes and models, and a report check that only tests file existence. The driver that actually ran on 2026-10-15 was the canonical one. That driver renders the *fleet's* `templates/round-prompt.md` (D03).
6. **The canonical renderer breaks on `/` and silently corrupts on `&` in axes strings** (D05, reproduced). The fleet's config workaround is eroding (the souji row brings `/` back), and the canonical example config triggers the bug itself.
7. **The canonical schema contradicts the canonical protocol** (`supersedes.entry`). The fleet ledger has also outgrown the schema's vocabulary: `train`, `craft`, and lane status `closed` (D11).
8. **"Upstream" is circular** (D16). kimi-shokunin calls the fleet its upstream, and the fleet calls kimi-shokunin its upstream. Only the operator can rule on this.

---

## 1. Lineage (git dates, -0300)

| when | tree | commit | what |
|---|---|---|---|
| 2026-09-28 | fleet | `58bc367`…`e275d4a` | protocol rounds 1–12 authored in the fleet |
| 2026-09-29 00:19 | fleet | `17c1fad` | last change to the fleet's v4 watchdog base |
| 2026-09-29 19:48 | canonical | `459b02b` | kimi-shokunin 0.1.0, the Kimi port (config-driven driver, template renderer, mint kit) |
| 2026-10-13 12:05:28 | canonical, ompskills, fleet | `812f1da`, `0bddb85`, `e0b4d9b` | `LEARNING.md` added; host binding created; fleet root initialised. All three share the same second. |
| 2026-10-13 16:47 | fleet | `e867f78` | protocol re-vendored from canonical: 6/6 files equal `812f1da` |
| 2026-10-13 16:55–16:58 | both | `ee1e5d6`→`bc7d690`; `7e81867`→`820eb26` | Craft-hours added and reverted in both trees |
| 2026-10-15 01:46 | fleet | `7d02e96` | canonical driver started on the fleet; template staged; axes sanitised |
| 2026-10-15 09:00 | fleet | `79752af` | Registry home, committed inside "fleet state: checkpoint WIP…" |
| 2026-10-15 09:02 | fleet | `b2f2efa` | Registry-home evidence files committed |
| 2026-10-16 15:55 | fleet + myskills | `84bade0` + `318912d` | operator amendment; Kimi mirror synced from the fleet |
| 2026-10-16 22:39–22:47 | fleet + myskills | `0b1ac3b` + `8eb0c91`, `fd9ed8c` | SCORECARD rollout; nudge pointer fix; mirror description |
| 2026-10-17 15:43 / 2026-10-19 09:05 | canonical (remote only) | `cbd6fc5` (merge `dc5b8e2`) / `b3ca98f` | README Devin-wiki link; `considerthese/2026-10-19.md` reflection |
| 2026-10-18 23:58 | fleet | `e20f4fa` | souji sweep removes `.ufo/waves/round-14/registry-home-rerun/*` |
| 2026-10-19 17:03 | fleet | `31baf5c` | backlog commit carries the LOG/SCORECARD overwrite |

Commands behind this table:
- `git -C ~/Projects/kimi-shokunin log --format='%h %ad %s' --date=iso b3ca98f`
- `git -C ~/Projects/shokunin log --format='%h %ad %s' --date=iso -- PROTOCOL.md PROTOCOL-APPENDIX.md MISSION.md AXES.md CORPUS.md LEARNING.md templates scripts`
- Vendoring equality, run for each file `f`: `diff <(git -C ~/Projects/shokunin show e867f78:$f) <(git -C ~/Projects/kimi-shokunin show 812f1da:skills/shokunin/protocol/$f)` → SAME ×6. The same diff of `820eb26` against `bc7d690` → SAME ×6.
- Revert cleanliness: `git -C ~/Projects/kimi-shokunin diff --stat 812f1da bc7d690` → empty, and `git -C ~/Projects/shokunin diff --stat 7e81867~1 820eb26` → empty.

---

## 2. Entry-point matrix: what each consumer actually loads

| consumer | resolves to | protocol state | 1–3 claims? | `LEARNING.md`? | evidence |
|---|---|---|---|---|---|
| Fleet lane round dispatched by the driver | Canonical driver run with the fleet conf. It renders `$SHOKUNIN_ROOT/templates/round-prompt.md` (canonical watchdog:35), and the lane reads the fleet's `MISSION.md` + `AXES.md`. | amended (fleet) | yes | yes | fleet LOG entry in `7d02e96` (see note below) |
| OMP/Devin `/skill:shokunin` | `~/.agents/skills/shokunin` → ompskills binding; its `protocol/` → `kimi-shokunin/skills/shokunin/protocol` | **pre-amendment** | **no** (one-axis) | yes | `readlink`; ompskills SKILL.md:31 |
| Kimi `/skill:shokunin` | `~/.kimi-code/skills/shokunin` → `myskills/shokunin`, whose `protocol/` holds copies of 5 fleet files | amended | yes | **no**: file absent, 6 dangling references | `cmp` ×5 SAME; `grep -c 'LEARNING.md' …/protocol/*.md` → 2+2+0+1+1 |
| kimi-shokunin plugin installs from GitHub | canonical | pre-amendment | no | yes | not installed locally: `~/.kimi-code/plugins/installed.json` has no shokunin entry |

Notes on the evidence:
- The `7d02e96` LOG entry says: "`SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin bash <canonical>/scripts/shokunin-watchdog.sh`".
- ompskills SKILL.md:31 says: "On process, gates, verdicts and the learning path the canonical files win".
- This session resolved `skill://godspeed` to `~/.agents/skills/godspeed/SKILL.md`. So OMP skill lookup goes through `~/.agents/skills`.

---

## 3. Divergence register

Every row gives: files · nature (amendment / regression / host-specific / canonical defect) · newer side · sync direction · operator approval.

### D01: operator amendment 2026-10-16 (multi-claim rounds, capabilities, stagnation nudge, exploratory claims)
- **Files and hunks:**
  - `PROTOCOL.md`: the prompt-embed clause (fleet :93–97) and Fleet-2 conventions (fleet :484–492).
  - `MISSION.md`: "The axes framework" (:38–48).
  - `AXES.md`: "Working the axes", new "Capabilities" section, new "The stagnation nudge" section, and the SCORECARD contract table (rows axes/capabilities/planned/saturation).
  - `LEARNING.md`: expansion observable, exploratory gate, closing paragraph.
  - `PROTOCOL-APPENDIX.md`: rows "Multi-claim rounds" and "Exploratory claims" (fleet :49–50).
- **Nature:** amendment. The appendix source column says "operator amendment 2026-10-16". `84bade0`'s message calls it an operator amendment.
- **Newer side:** fleet, `84bade0` 2026-10-16 15:55. Canonical last touched these files on 2026-10-13 (`812f1da`/`bc7d690`) or 2026-09-29 (`459b02b`: MISSION, APPENDIX).
- **Direction:** fleet → canonical.
- **Approval:** none for the text, which is already operator-ratified. Commit locally only: the standing rule is no push, and pushing to `VeigaPunk/kimi-shokunin` belongs to the operator (MISSION.md §Push scope).
- **Mechanics (dry-checked with `git apply --check`, no writes):**
  - `git -C ~/Projects/shokunin show 84bade0 --format= -- <file>`, piped to `git -C "$K" apply --directory=skills/shokunin/protocol`, applies **clean** for PROTOCOL.md, MISSION.md, AXES.md and LEARNING.md.
  - The APPENDIX hunk **fails on its own**: its trailing context is the Registry-home row from D02. Either apply D02 first, or hand-insert the two rows directly after the "Lane write scope" row.
- **It is live fleet-wide:** 21/21 lane `SCORECARD.md` files carry Capabilities and Saturation headings. Command: `for d in ~/Projects/shokunin/*-shokunin; do grep -qiE '^#+ .*capabilit' $d/SCORECARD.md && grep -qiE '^#+ .*saturation' $d/SCORECARD.md && echo ok; done | wc -l` → 21.

### D02: Registry home (where main-repo lanes register their gates)
- **Files:** `PROTOCOL.md` Gate standard, the **Registry** and **Delivery** bullets (fleet :383–386, :403–406); `PROTOCOL-APPENDIX.md` row "Registry home" (fleet :51).
- **Nature:** amendment, fleet-first, made by the protocol lane's round-14 relaunch. **Admission is not on record.**
- **Newer side:** fleet, `79752af` 2026-10-15 09:00, committed inside a "checkpoint WIP" commit.
- **Direction:** fleet → canonical only after admission. Until then, hold it back.
- **Approval:** **YES.** Either the operator ratifies it, or the protocol lane closes round 14 properly first.
- **Why it counts as unadmitted:**
  - The main-repo LOG entry (`12f2da5:LOG.md:782–783`) promises: "The following verification entry records actual CLI runs and after-count". No such entry exists before end of file. The next sections (:790–:828) are operator directives and the amendment rollout.
  - `.ufo/reports/round-14/protocol.md` is still the 340-byte marker from 2026-09-28 (`ef36757`). It has 0 SHONEN headings and 0 registry-home mentions (`wc -c`; `grep -c`).
  - No ledger row mentions it: `jq '.rounds[]|select(tostring|test("registry home";"i"))' MANIFEST.json` → 0.
  - The appendix row's evidence pointer `.ufo/waves/round-14/registry-home-rerun/before.json` is **dead at HEAD**. souji's `e20f4fa` emptied the directory. The 12 files are recoverable at `b2f2efa`.
  - The home this clause defines (`## Gate registry — protocol lane registry home`, at `12f2da5:SCORECARD.md:147`, split at `## Aggregator lane` :199) **does not exist at HEAD** (D18).
- **If ratified:** pin the evidence cell to `b2f2efa:.ufo/waves/round-14/registry-home-rerun/before.json` in both trees.
- **Note:** this move also deleted census rows G16/G26 and two anchors from `.ufo/waves/round-13/`. Per `b2f2efa:…/integration.md`, the fleet's preservation gate already encodes the amended text.

### D03: round-prompt template
- **File:** `templates/round-prompt.md`.
- **Nature:** amendment.
  - `84bade0` changed §2 (1–3 claims, admission, capability, exploratory), added the §3 Godspeed lead, and changed §4 so "Work performed" opens by naming the claims.
  - `0b1ac3b` fixed the stagnation-nudge pointer.
- **Newer side:** fleet, `0b1ac3b` 2026-10-16 22:39. Canonical is `459b02b` 2026-09-29. The fleet copy was byte-identical to canonical when it was staged: `diff <(git show 7d02e96:templates/round-prompt.md) …/kimi-shokunin/templates/round-prompt.md` → SAME.
- **Direction:** fleet → canonical.
- **Approval:**
  - Claims text: no.
  - **Godspeed path: YES.** The template now hardcodes `~/.agents/skills/godspeed/directive.md`. The canonical README promises the opposite (README.md:86–87: "no hardcoded hosts, models, or absolute paths").
  - Recommended: keep the lead (it is the operator's mandate), but carry the path as a config key the renderer substitutes, or word it host-neutrally ("the host's godspeed directive; see host binding").
- **Which copy is live:** the canonical driver reads `$SHOKUNIN_ROOT/templates/round-prompt.md` (canonical watchdog:35). The fleet copy is therefore the live template, and the canonical copy is only used when `SHOKUNIN_ROOT` is the plugin root.

### D04: fleet watchdog fork (regression)
- **Files:** fleet `scripts/shokunin-watchdog.sh` (v4 lineage) vs canonical `scripts/shokunin-watchdog.sh`.
- **Nature:** **regression**. The fleet keeps the pre-port driver:
  - hardcoded root (`SK=` :7);
  - **dead launcher** at :8: `UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting`. `ls` → "No such file or directory", and `~/Projects/origin-work` itself is absent;
  - a 9-lane list (:14), while the fleet conf has 20 lane rows (`grep -cE '^[a-z0-9-]+\|' shokunin.conf` → 20);
  - model aliases (`LANE_MODEL` `@m_swe` :26; route map `@m_lunamax/@m_flash/@m_zfl` :59);
  - `report_of()` only tests file existence (:45), so marker reports would advance rounds. Canonical :66–71 requires a SHONEN heading and at least 400 bytes.
  - It also contradicts the fleet's own MISSION.md:10: "nothing is hardcoded in `scripts/shokunin-watchdog.sh`".
- **Newer side:**
  - Design: canonical (`459b02b` 2026-09-29 19:48). It postdates the v4 base `17c1fad` (2026-09-29 00:19) and adds the content-checked `report_of`, config-driven LANES and the template renderer. [INFERENCE] It was ported from `17c1fad`; the canonical header says only "Kimi port of upstream scripts/shokunin-watchdog.sh".
  - Text: fleet (`84bade0` 2026-10-16 added the 1–3-claim and godspeed lines at :55 and :57; the fleet template already carries both).
- **Which driver actually ran:**
  - `.ufo/watchdog.log` has 50 canonical-format launches (`grep -cE 'launch [a-z0-9-]+ round=[0-9]+ pid=' .ufo/watchdog.log`), the last at 2026-10-15T01:50:57.
  - It has 93 v4-format launches (`grep -c 'runId=' .ufo/watchdog.log`), the last at 2026-09-28T23:15:05.
  - The `7d02e96` LOG entry records the canonical launch command.
- **Direction:** canonical → fleet. Retire the fleet copy, or replace it with a short wrapper that execs the canonical driver with `SHOKUNIN_CONF`. Also fix fleet README.md:123: "`shokunin.conf` + `scripts/` — the round driver".
- **Approval:** **YES.** PROTOCOL.md says `scripts/` is operator-side (fleet :112, canonical :111).

### D05: renderer bug on `/` and `&` (canonical defect; the fleet workaround is eroding)
- **Files:**
  - canonical `scripts/shokunin-watchdog.sh:76`: `-e "s/{{AXES}}/${LANE_AXES[$lane]:-}/g"`;
  - `templates/shokunin.conf.example:21`: the aggregator axes contain `mint/dormancy`;
  - fleet `shokunin.conf:76`: the souji row contains `stale/duplicate/preserved`.
- **Nature:** canonical defect, plus a regression of the fleet's own workaround.
- **Newer side:** the defect has been in canonical since `459b02b` (2026-09-29). Fleet workaround: `7d02e96` (2026-10-15). Fleet regression: the souji row in `7bf2b1a` (2026-10-18).
- **Reproduced** (`printf 'Your lane axes: {{AXES}}.\n' | sed -e "s/{{AXES}}/${axes}/g"`):
  - `/` → rc=1 ("invalid substitute flag"). `render_prompt` fails, so the lane gets `launch-fail`.
  - `&` → rc=0 but the output is `(a {{AXES}} b)`: silent corruption.
- **History:** the `7d02e96` LOG entry records kengaku's "`launch-fail kengaku round=13 :: prompt render failed`". The fleet sanitised every row on 2026-10-15. Souji (minted 2026-10-18) brought `/` back: `awk -F'|' '$1 ~ /^[a-z0-9-]+$/ && $3 ~ /[\/&]/ {print NR": "$1}' shokunin.conf` → `76: souji`. The shipped example breaks the shipped driver (same awk on the example → `21: aggregator`).
- **Direction:** fix canonical.
  - Escape AXES (and LANE) with the idiom mint-agent.sh already uses at :67: `sed -e 's/[\\&|/]/\\&/g'`.
  - Change the example row to "mint and dormancy calls", the fleet's wording.
  - Fleet: rely on the fix, or sanitise row 76.
- **Approval:** script change **YES**; example-conf edit no.

### D06: `scripts/mint-agent.sh` (canonical only)
- **(a) Probation checklist wording.** Lines :92–94 say "verified one-axis-move round" three times. Change to "verified craft round (1–3 claims)". This is amendment follow-through.
- **(b) Domain written into the axes column.** :84 writes `$DOMAIN` into the LANES axes column. The conf contract says otherwise (example :16–18: "keep them short — they are the lane's improvement contract, not a description"). Evidence: the fleet's mori and chousa rows (conf :63, :67, both stamped "minted … by mint-agent.sh") carry domain descriptions, and those render into "Your lane axes: …". Recommended: an optional `--axes` flag, with the domain kept as a comment line. This is a canonical defect.
- **Newer side:** canonical (`812f1da`, 2026-10-13).
- **Direction:** canonical-only fix; there is no fleet copy of this script.
- **Approval:** **YES**, because it is a script.

### D07: three skill bindings
- **Files:**
  - canonical `skills/shokunin/SKILL.md` (216 lines);
  - Kimi mirror `~/Projects/myskills/shokunin/SKILL.md` (228 lines) plus its `protocol/` (5 copies);
  - OMP/Devin binding `ompskills/.omp/skills/shokunin/SKILL.md` (74 lines), whose `protocol` is a symlink to canonical.
- **Nature:** the canonical lags the amendment; the Kimi mirror has **regressed** (it drops `LEARNING.md`, the learning-path essence); both bindings are host-specific.
- **Newer side:** Kimi mirror (`fd9ed8c` 2026-10-16 22:47) > canonical (`812f1da`) = ompskills (`0bddb85`). The last two were committed in the same second on 2026-10-13 12:05:28.
- **Details:**
  - Canonical one-axis sites: :3, :19, :54, :61, :66, and the admit rule at :73. Its Pointers list (:209–210) omits `LEARNING.md`.
  - The Kimi mirror carries the amended steps (diff hunks at :3 and :51–:90), but it removed the load-order item `5. LEARNING.md`. Its `protocol/` has no `LEARNING.md` although 6 references point at it. Its :19 still reads "ONE axis-move per round". This is the 1 residual hit in V2.
  - The OMP binding says "judge it on its axis" at :47, and calls the fleet's `MISSION.md` a "copy" at :36. The fleet copy is now ahead of canonical.
- **Direction:**
  1. Bring the mirror's amended hunks into canonical `SKILL.md` (they are fleet-derived). Keep the `LEARNING.md` load item, fix :19, and add `LEARNING.md` to Pointers.
  2. Retire the Kimi mirror: repoint `~/.kimi-code/skills/shokunin` to `kimi-shokunin/skills/shokunin`, where `protocol/` sits next to `SKILL.md`.
  3. The OMP binding then needs only the two wording fixes; the protocol arrives through its symlink.
- **Approval:** canonical `SKILL.md`, no. Kimi skill symlink and ompskills edits: **YES** (operator-owned host configuration and repos).

### D08: `commands/shokunin.md` (canonical only)
- **Lines:** :2 says "one-axis-move craft round"; :12 "Pick ONE axis"; :13 "Land exactly one improvement"; :14 states the single-axis admit rule. :7 lists the protocol files without `LEARNING.md`.
- **Nature:** amendment follow-through. **Approval:** no.
- **Newer side / direction:** canonical `459b02b` (2026-09-29) predates the amendment. There is no fleet equivalent; the host verbs live in the ompskills binding. Carry the amended wording into canonical.

### D09: `README.md` (canonical only)
- **Lines:** :8–13 "Every round is ONE axis-move"; :45 quick start; :65 "Contract in one line"; :28–29 file tree omits `LEARNING.md`; :83–87 Provenance calls `VeigaPunk/shokunin` "Upstream" (see D16).
- **Upstream state:** the upstream tip adds a wiki link at :17 (`cbd6fc5`). Seven `cursor/*readme*` branches and draft PR #1 exist (`git ls-remote origin`). `b3ca98f:considerthese/2026-10-19.md` §Top 3 lessons, item 1: "README direction is undecided."
- **Newer side / direction:** the wiki line is canonical-remote only (`cbd6fc5`, 2026-10-17). The fleet README already says "a round is 1–3 claims" (fleet README.md:55, `84bade0` 2026-10-16). Carry that wording fleet → canonical.
- **Approval:** minimal wording edits, no. Choosing the README direction, **YES**.

### D10: `kimi.plugin.json`
- **Lines:** :5 says "iterate one-axis-move craft rounds, Pareto/verdict-judge every round". This contradicts SKILL.md:24 ("never describe a shokunin round as "passing Pareto""). Version is `0.1.0` (:4).
- **Nature:** amendment follow-through, plus an internal contradiction in canonical.
- **Newer side / direction:** canonical `459b02b` (2026-09-29), with no fleet equivalent. Fix in canonical.
- **Approval:** description, no. Version bump or release, **YES**.

### D11: `templates/MANIFEST.schema.json` vs the fleet ledger
All counts are from `MANIFEST.json` as last committed at `12f2da5`; the worktree is clean.
**Newer side / direction:**
- The fleet protocol pinned `supersedes.entry` on 2026-09-28 (`df1b2c6`). The canonical port (`459b02b`, 2026-09-29) shipped that text (`git show 459b02b:skills/shokunin/protocol/PROTOCOL.md | grep -c 'MAY also carry'` → 1) together with a schema that forbids it. The contradiction is a day-one port defect. Fix: schema ← protocol, inside canonical.
- The ledger vocabulary kept evolving in the fleet from 2026-10-13. Whether it flows into the schema (fleet ledger → canonical schema) is the operator's call.

- **(a) `supersedes.entry` (canonical contradicts itself).** PROTOCOL.md (fleet :303, same text in canonical) says supersedes "MAY also carry `entry`". The schema at :117 sets `additionalProperties: false`, which forbids it.
  - Count: `jq '[.rounds[]|select((.supersedes|type)=="object" and (.supersedes|has("entry")))]|length'` → **44** fleet rows that are schema-invalid but protocol-valid.
  - Fix the schema by adding `entry` (integer ≥0). **Approval:** no, because it only aligns the schema with ratified text.
- **(b) Ledger vocabulary drift.**
  - `type` outside the 7-value enum: **80** rows (`jq '[.rounds[]|select((.type // "-") as $t|["scaffold","work","ops","closure","closure-correction","retroactive-closure","mint"]|index($t)|not)]|length'`). That is 75 non-enum values plus 5 rows with no type. The non-enum values are `train` 63, `craft` 9, `train+audit` 2, `train+audit+unlock` 1, dated 2026-10-13 to 2026-10-19.
  - Lane status `closed`: **24** (`jq '[.rounds[]|(.lanes // {})|to_entries[]|select(.value as $v|["ok","failed","not-dispatched","in-flight"]|index($v)|not)]|length'`), in `rounds[142..165]`, 2026-10-15/16.
  - The operator must choose: extend the enums and document `claims`/`verdicts` as the multi-claim fields, or treat all of these as defects and append corrections. **Approval: YES.**
- **(c) Fleet ledger defects (independent of the schema decision).**
  - 5 rows have no `type` and no `date`: `rounds[272,277,279,291,293]`, the kotodama r43/44/46/47/48 closures.
  - `rounds[138].round` is `null`. This is the row that crashed the closure gate, per the registry-home LOG entry.
  - `rounds[1]` has a not-dispatched lane but no `closed_at`.
  - Fix with appended closure-corrections; never rewrite rows. The integrator owns this.

### D12: `shokunin.conf.example` vs the fleet `shokunin.conf`
- **Nature:** host-specific. The fleet sets an absolute `SHOKUNIN_ROOT`, `SUBSTRATE_CMD='omp -p --cwd "%C" "@%P"'`, a Devin alternative as a comment, `FLEET_REMOTE=origin`, and 20 lanes.
- **Newer side:** fleet conf (`7bf2b1a`, 2026-10-18), copied from the canonical example (`459b02b`, 2026-09-29). `diff` of the first 41 lines differs only in: SHOKUNIN_ROOT, the sanitised aggregator axes, the removed example row, SUBSTRATE_CMD plus the Devin comment, and FLEET_REMOTE.
- **Direction:** keep fleet-local. The canonical side gets only the D05 example row. Optionally add OMP and Devin `SUBSTRATE_CMD` comment lines, copied from the host-binding table.
- **Approval:** no.

### D13: mint kit vs the amended SCORECARD contract
- **No `SCORECARD.md` seed.** The kit has none, but `AXES.md` §SCORECARD.md contract applies to every child repo and now has 5 fields, and 21/21 lanes carry Capabilities and Saturation. The `0b1ac3b` rollout had to retrofit every lane by hand.
  - A seed is optional. If added, these pins must change together: install.sh:35 ("must contain exactly 7 files"), and the "7-file" / "7 files" wording at SKILL.md:47, :119, :211 and README:31.
  - **Approval: YES**, because it changes the kit's shape.
- **Stale line pointer in `SHONEN.md`.** The comment at :1–5 says "lines 386-393", but the seed block is now at canonical PROTOCOL.md:419 (fleet :423). Replace the line numbers with the heading text. **Approval:** no.
- **Hook for D3:** a `templates/mint/corpus/SOURCES.md` seed. install.sh counts only top-level files, so it needs no install.sh change.
- **Newer side / direction:** the kit was last changed in `812f1da`/`bc7d690` (2026-10-13). The SCORECARD contract it lags is fleet `84bade0` (2026-10-16). Change canonical only; the fleet has no mint kit.

### D14: § cross-file references introduced by D01 (gate finding)
- **Where:** PROTOCOL.md:490 (`` `AXES.md` §Capabilities ``) and APPENDIX:49 (`§Capabilities, §The stagnation nudge`). The same style appears at LEARNING.md:81 and template :16/:23, outside the gate's scope.
- **Newer side / direction:** introduced by fleet `84bade0` (2026-10-16). Fix in both trees with identical bytes.
- **Gate result:** the fleet's preservation gate (`.ufo/waves/round-13/verify-protocol.sh`, two-file mode, V4) reports:
  - fleet: **failed=3** (census R6, caps, xref §Capabilities/§The);
  - canonical: **failed=2** (census R6, caps; xref unresolved=0).
- **Fix (both trees, same bytes):** write the two in-gate references without `§`, e.g. "`AXES.md`, section *Capabilities*". Alternatively, the protocol lane extends the gate's allowlist.
- caps (the 470-line budget) is **not** conformance authority. W1ProtocolLane confirmed this from `integration.md` at `b2f2efa`.
- **Approval:** no.

### D15: `lane_prompt()` named in PROTOCOL.md (both trees)
- **Where:** fleet :112/:258/:404, canonical :111/:257/:400.
- **Problem:** only the fleet v4 script defines `lane_prompt()` (`grep -c 'lane_prompt()'`: canonical driver 0, fleet driver 1). The canonical driver uses `render_prompt()` with the template. Once D04 retires v4, the protocol names a function that no driver has.
- **Newer side / direction:** the text is shared and comes from the fleet protocol rounds of 2026-09-28, before the canonical port. Fix in both trees with identical bytes.
- **Constraint:** census row G25 pins the text with the regex `the integrator names the exact .lane_prompt\(\)`.
  - Option 1: keep the token and append a gloss, e.g. "(canonical driver: `render_prompt()` over `templates/round-prompt.md`)".
  - Option 2: update G25 in the same commit.
- **Approval:** no; this is protocol-lane wording.

### D16: circular "upstream" (governance)
- **kimi-shokunin names the fleet as upstream:**
  - README.md:83: "Upstream shokunin lives at github.com/VeigaPunk/shokunin";
  - templates/mint/SHONEN.md:2: "(upstream main repo, master HEAD…)";
  - schema :5: "Derived from the upstream shokunin MANIFEST.json";
  - SKILL.md:174: "Restated faithfully from upstream `PROTOCOL.md`";
  - watchdog :2 and mint-agent :2: "Kimi port of upstream".
- **The fleet names kimi-shokunin as upstream:**
  - README.md:120–121: "canonical protocol, vendored from … kimi-shokunin (upstream)";
  - but README.md:12 also calls the fleet root "the canonical protocol".
- **ompskills SKILL.md:24–31** says the protocol lives in kimi-shokunin and canonical wins.
- **Newer side:** the kimi-shokunin strings date from `459b02b` (2026-09-29). The fleet README text is present at HEAD (README last touched by `bc889c5`, 2026-10-17). **Direction:** decided by the operator's ruling (Phase 0, step 2).
- **Approval: YES.**
- **Recommended:** kimi-shokunin is canonical. The fleet is the proving ground, under a duty to upstream any fleet-first amendment in the same session, with the vendored commit recorded in the ledger (D19). Reword the kimi-shokunin "upstream" strings to say the fleet is the protocol's origin and history.

### D17: fleet-only assets (host-specific, keep)
- **`templates/agents/`:** 13 `ufo-*` cards plus `ADAPTATION.md`, adapted to Kimi's subagent schema. The runtime copy at `~/.kimi-code/agents/ufo/` is byte-identical, 13/13 by `cmp`. Since `84bade0` the cards also carry the Godspeed posture line.
- **`.omp/agents/executor.md`:** a project-local leaf executor card for OMP.
- **`.devin/skills/{flashseat,glmseat}`:** Devin model-pin skills.
- **Newer side:** fleet-only. Cards: `04fd457` (2026-10-16), posture line `84bade0`. Executor card: `56d57d1` (2026-10-14). flashseat: `d41a9f5` (2026-10-14). glmseat: `ee2c793` (2026-10-17).
- **Direction:** none; keep all of these fleet-local. Do not upstream them in D5:
  - the cards derive from `ufo-fsd-alpha`, which is out of scope for this campaign;
  - the seat skills pin model aliases, which canonical text forbids.
- **Approval:** needed only if someone later proposes upstreaming them.

### D18: P0, fleet-root `LOG.md` and `SCORECARD.md` overwritten at HEAD
- **What happened:** `31baf5c` (2026-10-19 17:03, kotodama-shokunin identity) committed kotoba's files at the fleet root. They are byte-identical to kotoba-shokunin commit **`b7470d7`** (2026-10-19 07:36:02, "round 36"):
  - `git -C ~/Projects/shokunin rev-parse 31baf5c:SCORECARD.md 31baf5c:LOG.md` and `git -C ~/Projects/shokunin/kotoba-shokunin rev-parse b7470d7:SCORECARD.md b7470d7:LOG.md` both print `3fc970db…` / `99de619d…`.
  - This is not `c8e233d`: that kotoba commit (10:25:21, "round 37") replaced those blobs with `c2ce6947…` / `4a990b94…`. W2RoundProtocol raised the correction and I re-verified it. It matches the "mtime 07:35" in the `ab707d9` flag.
  - Headers: "# kotoba-shokunin — Iteration Log" / "— Scorecard" (`head -1`).
  - `git show --numstat 31baf5c -- LOG.md SCORECARD.md` → LOG.md +1356/−845, SCORECARD.md +165/−395.
- **Nature / newer side:** a fleet regression at `31baf5c` (2026-10-19 17:03). The last good state is `12f2da5`.
- **It was flagged earlier.** The kotoba r42 closure (ledger row from `ab707d9`) notes: "fleet-root LOG.md + SCORECARD.md are uncommitted-overwritten with kotoba-derived content".
- **Nothing unique is lost by restoring:**
  - `grep -vxFf kotoba-shokunin/LOG.md LOG.md | grep -cv '^\s*$'` → 0 lines are unique to the root copy.
  - The 7 root SCORECARD lines missing from kotoba's current file are kotoba's round-36 values. They remain recoverable from `b7470d7` in kotoba's own history.
  - The main-repo versions live at `12f2da5` (= `31baf5c~1`). That copy holds the registry section (:147), the aggregator section (:199), and the Capabilities/Saturation sections from `0b1ac3b`.
- **Blast radius:** the fleet worktrees `kaika/{contract,census,ledger,protocol}` all sit on `31baf5c` (`git worktree list`). Appending to root LOG/SCORECARD there would extend kotoba's copy.
- **Direction:** restore in a new commit; never rewrite history. **Approval: YES** (operator-flagged; these files belong to the protocol and aggregator lanes).

### D19: no ledger record of vendoring or ratification
- `protocol_updates` appears only in `rounds[1,3,13,25]`, all dated 2026-09-28 (`jq '.rounds|to_entries[]|select(.value|has("protocol_updates"))|.key'`).
- No row records the `e867f78` re-vendor, `79752af`, or `84bade0`.
- **Newer side / direction:** n/a. This is a missing fleet ledger record. Direction: fleet ledger only, written by the integrator.
- **Fix:** at sync time, the integrator appends an `ops` entry whose `protocol_updates` names the canonical sync commit.
- **Approval:** no; this is integrator duty.

### D20: upstream is ahead
- Live `origin/main` is `b3ca98f`. The local main and the D5 worktree are both at `bc7d690`.
- The 3 extra commits: `cbd6fc5` (README wiki link), merge `dc5b8e2`, and `b3ca98f` (adds `considerthese/2026-10-19.md`). None touches protocol, template or script text.
- **Newer side:** canonical remote (2026-10-17 and 2026-10-19). Local fleet and canonical checkouts are unaffected.
- **Their objects are already present locally:**
  - `git -C ~/Projects/kimi-shokunin rev-list --objects bc7d690..b3ca98f | wc -l` → 8;
  - `git -C ~/Projects/kimi-shokunin fsck --connectivity-only --no-dangling b3ca98f` → rc 0.
- **Direction:** fast-forward the D5 base to `b3ca98f` before writing. **Approval:** no for the local fast-forward; push stays with the operator.

---

## 4. Ordered sync checklist (for the canonical-sync writer and its owners)

`K` = the D5 worktree (`~/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon`). `F` = `~/Projects/shokunin`. Use `git -C` and absolute paths throughout: `cd` is wrapped and unreliable in this shell. Never cherry-pick `ee1e5d6` or `7e81867`, which would bring Craft-hours back.

### Phase 0: prerequisites (parent and operator, before D5 writes)
1. **[operator, P0, D18]** Restore root `LOG.md` and `SCORECARD.md` from `12f2da5` in a new commit, then refresh the `kaika/*` fleet worktrees. This step gates D02, D19 and every root LOG/SCORECARD write.
2. **[operator, D16]** Rule on the source of truth. Default: kimi-shokunin is canonical, and the fleet carries a same-session upstream duty.
3. **[operator, or protocol lane, D02]** Decide Registry home: ratify it, close round 14 (erratum on the r14 report, non-author verification, ledger row), or hold it.
4. **[operator, D03]** Decide how the godspeed-lead path is carried in the portable template.
5. **[operator, D11b]** Decide the ledger vocabulary: ratify `train`/`craft`/`closed` into the schema, or treat them as defects.
6. **[operator, D04–D06]** Approve or deny script changes; `scripts/` is operator-side.
7. **[parent, D20]** `git -C "$K" merge --ff-only b3ca98f`. The objects are local.
8. **[parent]** Wait for D3 (fleet contract: SOURCES.md, mistake mining, research step) to merge in the fleet, so D5 carries it in the same pass.

### Phase 1: D5 writer, canonical worktree, documents
These are the D5 core (protocol/, templates/, SKILL.md). Items marked † are outside the plan's D5 list; the parent may widen scope to include them.

9. Record the baselines from §5 (V1–V10).
10. **D01:** for each of PROTOCOL.md, MISSION.md, AXES.md and LEARNING.md, run `git -C $F show 84bade0 --format= -- <file> | git -C "$K" apply --directory=skills/shokunin/protocol -`. Then insert the APPENDIX rows "Multi-claim rounds" and "Exploratory claims" after "Lane write scope".
11. **D02, only if step 3 ratified it:** apply the `79752af` hunks, with the evidence cell pinned to `b2f2efa:`. Make the same pin edit in the fleet (step 24) so the bytes stay identical.
12. **D14** wording and **D15** gloss: identical bytes in both trees (mirrored in step 24).
13. **D3 deltas:** byte-copy the fleet's post-D3 `CORPUS.md`, `LEARNING.md`, the PROTOCOL.md file-contract row, and `templates/round-prompt.md`. Apply the godspeed handling decided in step 4.
14. **D07** canonical `SKILL.md`: the mirror's amended hunks, plus the `LEARNING.md` load item kept, :19 fixed, and Pointers updated.
15. † **D08** `commands/shokunin.md`; **D09** minimal `README.md` (3 one-axis sites plus the tree listing; leave the README direction to the operator); **D10** plugin description.
16. **D11a** schema: allow `supersedes.entry`. Apply step 5's vocabulary only if it was ratified.
17. **D13** mint kit: re-anchor the `SHONEN.md` comment; add the `corpus/SOURCES.md` seed (D3). Add `SCORECARD.md` only if approved, together with the install.sh 7→8 change and the "7-file" mentions.
18. **D05** example conf: aggregator axes become "mint and dormancy calls". Optionally add the OMP/Devin `SUBSTRATE_CMD` comments.
19. † **D16** "upstream" strings, worded per step 2.

### Phase 2: scripts (gated by step 6)
20. **D05:** escape AXES and LANE in `render_prompt` using the `dom_esc` idiom.
21. **D06:** mint-agent.sh probation wording, and keep the domain out of the axes column.

### Phase 3: parent/integrator, fleet
22. **D04:** retire the fleet `scripts/shokunin-watchdog.sh`, or turn it into a wrapper. Fix fleet README:123. Gated by step 6.
23. **D05:** sanitise fleet `shokunin.conf:76` (souji), unless step 20 landed.
24. Mirror steps 11 and 12 into the fleet so all six protocol files end byte-identical with canonical (V1). If D02 is held, the target is 4/6, with PROTOCOL.md and APPENDIX differing only by the Registry-home hunks.
25. **D19:** append an `ops` ledger entry whose `protocol_updates` lists `84bade0`, `79752af` (if ratified), the D3 commit, and the canonical commit. Record "vendored from kimi-shokunin @ <sha>" in the fleet README.
26. **D11c:** append corrections for the 5 typeless rows, `rounds[138]` and `rounds[1]`.

### Phase 4: operator (host configuration and pushes)
27. **D07:** repoint `~/.kimi-code/skills/shokunin` to `~/Projects/kimi-shokunin/skills/shokunin`, retiring the mirror. At minimum, add `LEARNING.md` to the mirror and fix its :19.
28. **D07:** ompskills binding wording (:36 "copy", :47 "on its axis"); push `0bddb85` together with this fix.
29. All pushes (kimi-shokunin, fleet). The standing rule is no push, so this needs the operator.

### Phase 5: verify
30. Re-run §5. Targets:
    - V1: 6/6 (or 4/6 with D02 documented as held);
    - V2: 0;
    - V3: 0;
    - V4: xref unresolved=0 in both trees, with census and caps unchanged;
    - V5: rc 0;
    - V6: OK;
    - V7: literal output;
    - V9: ≥1 in each of the 3 files;
    - V10: 0.

---

## 5. Verification battery (values measured 2026-10-19)

| id | command (`K`=canonical tree, `F`=fleet root) | now | target |
|---|---|---|---|
| V1 | `for f in PROTOCOL.md PROTOCOL-APPENDIX.md MISSION.md AXES.md CORPUS.md LEARNING.md; do cmp -s $K/skills/shokunin/protocol/$f $F/$f && echo same; done \| wc -l` | **1** (CORPUS.md) | 6, or 4 with D02 held |
| V2 | `RE='[Oo][Nn][Ee][ -]axis-move\|exactly one axis-move\|single next axis-move\|Pick ONE axis\|Land exactly one\|exactly one verifiable\|one verifiable improvement against\|lowest-scoring axis for the repo'; git -C $K grep -nIE "$RE" HEAD -- . \| grep -vE '1–3\|[Cc]laim is one axis-move' \| wc -l` | **23** at `bc7d690` (also 23 at `b3ca98f`); fleet 0; myskills 1; ompskills 0 (plus "on its axis" at :47, which the regex does not catch) | 0 |
| V3 | `git -C $K grep -nIiE 'craft.hours\|HOURS\.md\|10,000.hour\|craft_hours' HEAD -- . \| wc -l`; same grep on the fleet protocol files, templates and scripts, and on both bindings | **0** everywhere | stays 0 |
| V4 | `sh $F/.ufo/waves/round-13/verify-protocol.sh <tree>/PROTOCOL.md --appendix <tree>/PROTOCOL-APPENDIX.md` | canonical failed=2 (census R6, caps), xref 0; fleet failed=3 (+xref §Capabilities, §The) | xref unresolved=0 in both |
| V5 | `bash $K/install.sh` | rc 0, "mint kit: 7 files" | rc 0 |
| V6 | `bash -n $K/scripts/shokunin-watchdog.sh; bash -n $F/scripts/shokunin-watchdog.sh` | OK, OK | OK |
| V7 | `axes='a/b & c'; esc=$(printf '%s' "$axes" \| sed -e 's/[\\&\|/]/\\&/g'); printf '{{AXES}}\n' \| sed -e "s/{{AXES}}/$esc/g"` | the unescaped form fails: rc=1 for `/`, corrupted output for `&` | prints `a/b & c` |
| V8 | the D11 `jq` counts on `$F/MANIFEST.json` | type-outside-enum 80 · supersedes.entry 44 · status `closed` 24 · missing date 5 · round null 1 | per step 5 |
| V9 | `git -C $K grep -c LEARNING HEAD -- README.md commands/shokunin.md skills/shokunin/SKILL.md` | 1 file matches (SKILL.md:42 only) | each of the 3 files names it |
| V10 | `grep -c LEARNING.md ~/Projects/myskills/shokunin/protocol/*.md; test -e ~/Projects/myskills/shokunin/protocol/LEARNING.md` | 6 references, file absent | mirror retired, or file present |

---

## 6. Shared gaps (present in both trees, so not drift; land them in one pass with D3)
- **The report contract has no slot for trend verdicts.** `LEARNING.md`'s heading "The three trends — one verdict each, every round" (fleet :23) requires them, but `templates/round-prompt.md` §4 lists only Work / Landed / Before→after / SHONEN, in both trees.
- **Unsubstituted placeholder.** Template line 1 renders "Working dir: {{FLEET_ROOT}}/<{{LANE}}-repo>". The `<…-repo>` part is never filled in, although the driver knows each lane's working directory.
- **An open L0 item concerns `CORPUS.md` in both trees:** "aggregator | round-9 | CORPUS.md amendment set — four measured conflicts…". It is unresolved, and D3's `CORPUS.md` edit should not collide with it.

## 7. Fleet-local observations (outside the canonical sync)
- **Roster mismatch.** The README roster has 16 rows; the `MANIFEST.json` roster has 13. chousa, kotodama and mori are missing from MANIFEST (`jq -r '.roster[].id'` compared with the README table using `comm`). README.md:122 still says "79 rounds"; the ledger now has 294 entries.
- **Runtime files are tracked.** `.ufo/state/*` (64 tracked files: `git ls-files .ufo/state | wc -l`) and `.ufo/watchdog.log` are in git. The fleet's `.gitignore` does not ignore them.
- **MISSION.md disagrees with the conf.** MISSION.md's lane table lists 9 lanes and gives kama "operability + freshness"; the conf has 20 lanes and gives kama "operability + calibration". MISSION.md's route buckets also differ from the host table. All of these are still open L0 items, for example:
  - "kama | round-1 | Reconcile the relaunched counter and craft dispatch contract…"
  - "kagi | round-16 | Reconcile the relaunched counter and craft dispatch contract…"

  Neither is a sync item; the operator must rule on them.
- **myskills has uncommitted changes in the `godspeed/` directory** (`M SKILL.md`, `D filter.md`, `D velocity.md`). That directory is the godspeed skill, not shokunin; it was left untouched. Its `directive.md` matches `~/.agents/skills/godspeed/directive.md` byte for byte (`cmp`).

## 8. Method, coverage, disclosures
- **Coverage.** Every file in the assignment list was compared:
  - canonical: SKILL.md, protocol/×6, round-prompt, mint/* (11 files), schema, conf example, both scripts, the command file, README; plus `install.sh` and `kimi.plugin.json`;
  - fleet: the 6 protocol files, `templates/` (round-prompt + agents/), `scripts/`, `.omp/agents/`, `.devin/skills/`;
  - both host bindings.
- **Methods:** whole-file `diff -u`, per-file `git log` dates, `git apply --check` dry runs, the fleet's own preservation gate (it writes only to a `mktemp` directory), and `install.sh` (checks only).
- **Disclosures:**
  - A `git fetch --dry-run` contacted the kimi-shokunin origin. No refs, no `FETCH_HEAD` and no worktree changed. The `b3ca98f` objects are present locally, and I cannot tell whether this call or an earlier fetch put them there.
  - Scratch files (`/tmp/w1drift-*`: patches and roster lists) were created and then deleted.
  - One recursive grep ran from the wrong directory (the fleet root, because `cd` failed). It was read-only and I cancelled it.
  - The only write is this file. Repos, git state and host config were not changed.
- **L0 citations** use lane, round and opening words, never line numbers. This follows the fleet's obligation census, rows V8/V9 in `.ufo/waves/round-13/obligation-census-r13.tsv` (not this file's battery IDs).

## 9. Confidence
- **High:**
  - D01/D02 attribution (byte-level diffs plus the `git apply --check` results);
  - D04 "which driver ran" (log fingerprints plus the LOG launch line);
  - D05 (reproduced);
  - D11 counts;
  - D18 (numstat, headers, uniqueness check);
  - D20.
- **Medium (rests on absence of a record):** D02 "unadmitted". I searched the ledger, the r14 report, and the main-repo LOG through end of file at `12f2da5`. A verification could exist somewhere I did not search, such as a branch or the operator's notes.
- **Inference:** that the operator *wants* kimi-shokunin to stay canonical (D16 default). This follows the ompskills binding and the campaign plan's wording ("canonical upstream protocol … lags the fleet root"); nothing in the trees states it.
