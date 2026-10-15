# R10Evidence — aggregator round-10 resume evidence matrix

**Seat.** UFO-FSD scribe. Writes only this file. Advisory: no verdict, admission, promotion,
axis score, integration, commit, push or shipping authority is asserted here.

**Execution boundary (attested).** No gate, regression, selftest, frozen replay, build, lint,
test, formatter, judge, network call or alternate runtime was invoked by this seat. Inherited
failing gates were **not** re-run. Only read-only reads and read-only counting commands. The
final round report is **not** written here; that is the parent's duty (append after commit).

**Confidentiality.** Metadata, IDs, rule names, pathnames and counts only. No corpus prose, no
finding text, no credential value or reference, no session material.

**Ordering.** Sections 1–4 are the report contract's required sections **in order**
(`templates/round-prompt.md` §4; `.ufo/prompts/aggregator-round-10.md` §4). Sections 5–9 are
supporting evidence required by this seat's assignment.

---

## 0. Observation base (provenance pin)

| # | Fact | Value | Pointer |
|---|---|---|---|
| 0.1 | Fleet root / host | `/home/vgpnk/Projects/shokunin` | cwd |
| 0.2 | Main HEAD at observation | `f2df270cfd18083922243685b874d7e77844514c` | `git rev-parse HEAD` |
| 0.3 | HEAD movement during this session | `b598ce0` → `99efc52` → `f2df270` | `git log --oneline -4` |
| 0.4 | Historical baseline artifact | inherited, `.ufo/waves/aggregator-r10/before.json` sha256 `afecb2fda4e1f78e01b5e3863480c75de4588228cc781278148eb8b7753f57ae` | `sha256sum` |
| 0.5 | Baseline measured commit | `b598ce0e1d4fa8851d3e238ee6afde42bd57f787` | `before.json:2` |
| 0.6 | Baseline gate digest | sha256 `68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8` | `before.json` `gate_sha256` |
| 0.7 | Baseline coverage | 6 represented / 19 direct local lanes, 13 omitted, gate exit 1 | `before.json` |
| 0.8 | Resume metadata recount | reviewed 6, available 19, omitted 13, gate_exit 1 (a recount of 0.4, **not** a new run) | `.ufo/waves/aggregator-r10-resume/before.json` |
| 0.9 | Selector source at observation | `.ufo/waves/round-9/corpus-gate.mjs`: baseline digest `68939d0c…` (= 0.6) **changed mid-observation to** sha256 `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3` (976 lines, worktree-modified, diff 102 insertions / 14 deletions, **uncommitted**) | `sha256sum`; `git diff --stat` |
| 0.10 | Frozen expectations (inherited, unmodified) | 8 frozen revision keys, 12 selftest cases; sha256 `9af28e2e00f8f80256856765a0c692457bdc3f26b893981e96bc000672f2043a`, 17277 B | `.ufo/waves/round-9/corpus-gate.expected.json`; digest also pinned by a sibling artifact (§6) |
| 0.11 | Aggregator axes (authority) | cross-lane quality **9**, corpus review **9**, mint/dormancy calls **9** | `SCORECARD.md:301-305` |
| 0.12 | Report path (historical marker present) | `.ufo/reports/round-10/aggregator.md` 187 B, md5 `75eaefe096ac72d22598809416888cfd`, introduced `f5d8507` | §7 |
| 0.13 | Root `SHONEN.md` | absent (`ls SHONEN.md` → No such file or directory) | §4.4 |
| 0.14 | Steered round identity | round 10 (`CONTEXT.md`; `.ufo/state/aggregator.round` = `10`) | `MISSION.md` §Round end; `PROTOCOL.md:85-89` |
| 0.15 | Operator custody update (appended concurrently) | `audio`, `game-dev-2d`, `game-dev-3d` are Devin-owned, removed from the driver, hold unrelated in-flight work (465 / 77 / 3 dirty paths), and are **read-only** to this wave; they stay physical discovery members but are not configured-fleet members | `.ufo/waves/aggregator-r10-resume/CONTEXT.md:28-30`; `LOG.md:701-708` |

---

## 1. Work performed

Status legend: **landed** = present on disk now; **inherited** = prior wave's artifact, adopted as
evidence only; **parent** = not this wave's to perform.

| # | Work item | Owner seat | Artifact | Status | Evidence pointer |
|---|---|---|---|---|---|
| 1.1 | Canonical contract read (MISSION/AXES/PROTOCOL/CORPUS/SCORECARD + canonical skill) | R10Evidence | this file §0 | landed | `CONTEXT.md:3-26`; `PROTOCOL.md:327-405,406-431` |
| 1.2 | Baseline provenance pinned from recorded artifacts; no old live gate re-run | R10Evidence | §0.4–0.10 | landed | `sha256sum` of 0.4, 0.9 |
| 1.3 | Discovery-universe count (read-only) | R10Evidence | §3.2.1 | landed | `node -e` readdir count → 19 |
| 1.4 | SHONEN box/mark census, 19 child repos (read-only) | R10Evidence | §4.3 | landed | `grep -c`/`python3` count over `*-shokunin/SHONEN.md` |
| 1.5 | L0 open-question census (read-only) | R10Evidence | §5.1 | landed | `.ufo/l0-questions.md` pinned md5 in §5.1 |
| 1.6 | Historical marker byte pin + provenance | R10Evidence | §7 | landed | `md5sum`, `git log -1 f5d8507` |
| 1.7 | Round/role routing conflict census (read-only) | R10Evidence | §5.3, §5.4 | landed | `shokunin.conf` grep; `MANIFEST.json`; `~/.omp/agent/config.yml:318-332` |
| 1.8 | Existing `corpus-gate.mjs` default-selection fix | R10Selection (executor) | `.ufo/waves/round-9/corpus-gate.mjs` (now sha256 `e7d49942…`, 976 `wc -l` lines [seat reports 977], diff 102+/14−) | **present, uncommitted at observation** (§0.9) | source facts only: discovery registry row `:168`, `discoverLanes` `:239`, own-git guard `:552`, coverage diagnostics `:933`/`:939`, r7 under-coverage note `:428` |
| 1.9 | Selection seat change record | R10Selection | `.ufo/waves/aggregator-r10-resume/selection.md` (5864 B, sha256 `7a81e775…`) | landed (advisory record; self-declares "no build… or gate run") | §6 |
| 1.10 | `selection-regression.mjs` standalone CLI tests | R10Regression (executor) | **not present** in the wave dir at observation | **not landed** | `ls .ufo/waves/aggregator-r10-resume/` |
| 1.11 | `measure-corpus.mjs` redacted collector | R10Census (executor) | `.ufo/waves/aggregator-r10-resume/measure-corpus.mjs` (21424 B, sha256 `fefbf2ff…`) | landed (collector script; **not executed by this seat**) | §6 |
| 1.12 | Advisory planning evidence | R10Plan (planner) | `.ufo/waves/aggregator-r10-resume/plan.md` (16586 B, sha256 `6d119a43…`) | landed (advisory, may still grow) | §6 |
| 1.13 | Adversarial falsifier evidence | R10Critic (critic) | `.ufo/waves/aggregator-r10-resume/critic.md` (18548 B, sha256 `5d51a430…`) | landed (advisory, may still grow) | §6 |
| 1.14 | Reviewer seat `R10Review` output | R10Review (reviewer) | not present in wave dir at observation; seat not in live roster | **not landed / unobserved** | roster + `ls` |
| 1.15 | Lane-surface reconnaissance | R10Surface (scout) | `.ufo/waves/aggregator-r10-resume/surfaces.md` (20172 B, sha256 `35b86024…`; cutoff `CUTOFF 2026-10-15T04:55:22Z`) | landed (advisory) | §6 |
| 1.16 | Historical preservation pins | sibling seat (writer unconfirmed at observation) | `.ufo/waves/aggregator-r10-resume/preservation-pins.json` (sha256 `5463a068…`) | landed (metadata only; states "not verification results") | §6 |
| 1.17 | Prior-round plans and falsifiers | inherited seats | `.ufo/waves/aggregator-r10/seats/{plan,critic,scout,scribe}.md` | inherited | §6 |
| 1.18 | Final report section appended after commit | Main | `.ufo/reports/round-10/aggregator.md` | **parent** | §7 |

**Dispatch consistency check (factual, no ruling).** `.ufo/waves/aggregator-r10-resume/dispatch.json`
declares `dispatched: 9` with roles planner 1, connector 1, executor 3, scribe 1, scout 1,
reviewer 1, critic 1. Six non-scribe seat artifacts exist at the final observation (plan, critic,
surfaces, selection, measure-corpus, preservation-pins) plus this file; the regression harness and
the reviewer seat's artifact are absent, and the reviewer seat is not in the live roster. This is a
coverage observation, not a wave-validity claim.

---

## 2. Landed changes

| # | Change | Path | Commit | LOG entry | Status |
|---|---|---|---|---|---|
| 2.1 | Default-selection replacement in `corpus-gate.mjs` | `.ufo/waves/round-9/corpus-gate.mjs` | **none** — worktree-modified, uncommitted at observation (`M`, 102+/14−) | required: none yet | **not landed** by the landed-means-committed rule (`PROTOCOL.md:116-124`); needs its round-10 commit hash + a `LOG.md` entry |
| 2.2 | Lane-appended L0 questions (not this wave) | `.ufo/l0-questions.md` | uncommitted at observation (`M`; appended during the session, 25 → 43 newline-lines) | n/a | observed, authored by lanes |
| 2.3 | `w21 spec` commit (not this wave) | repo-wide | `f2df270` | n/a | observed HEAD movement |
| 2.4 | Parent motivation / planned-move records | `LOG.md:723-743`; `SCORECARD.md:398-417` | uncommitted at observation | self-describing | observed, authored by Main |
| 2.5 | Other lanes' concurrent edits (not this wave) | `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `LOG.md`, `SCORECARD.md` | uncommitted at observation | n/a | `git status --short` — **not ours to sweep** |
| 2.6 | Per-repo verdict lessons, AGGREGATE refresh, LOG/SCORECARD append, report append, commit, push | aggregator-owned corpus files; `.ufo/reports/round-10/aggregator.md` | **to be created by parent** | required | **parent duty — not done, not claimed** |

Every row above is "not landed" unless a commit hash appears. No placeholder in this file is
presented as a completed change. Row 2.1 is the one implementation edit that exists; it carries
no commit hash yet and therefore has no "Landed changes" entry the report contract can cite.

---

## 3. Before → after measurements

### 3.1 Required measurements (parent-executed; **not executed by this seat**)

| # | Claim | Before | After | Counting command | Measured commit |
|---|---|---|---|---|---|
| 3.1.1 | Default `--all` represented lanes | 6 of 19 (`before.json`) | **NOT MEASURED** | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json` | before `b598ce0e…`; after = parent's |
| 3.1.2 | Omitted direct local lanes | 13 (`before.json.omitted`) | **NOT MEASURED** | collector exact-set compare (plan §"Exact commands") | as above |
| 3.1.3 | Gate process exit | 1 | **NOT MEASURED** | same invocation, `status` retained separately from collector exit | as above |
| 3.1.4 | Frozen replay / selftest agreement | 8 frozen keys, 12 cases (stored expectations, no pass observed by this seat) | **NOT MEASURED** | existing `--selftest` / frozen replay | parent |
| 3.1.5 | Broad corpus-review score | 9 (`SCORECARD.md:303-305`) | **HOLD 9 expected; parent decides** | — | — |
| 3.1.6 | Cross-lane quality / mint-dormancy | 9 / 9 | **unchanged by this move (expectation)** | — | — |

The "after" column is deliberately empty: this seat did not execute any gate or test, and the
implementation it would grade appeared uncommitted only after the baseline pin (§0.9). No after
value, exit code, MATCH verdict or score increase is claimed anywhere in this file.

### 3.2 Measurements this seat did execute (read-only counting commands, not gates/tests)

| # | Measurement | Result | Command shape |
|---|---|---|---|
| 3.2.1 | Direct physical child dirs matching `/^[a-z0-9][a-z0-9-]*-shokunin$/` under MAIN_ROOT | **19** | `node -e 'readdirSync(".",{withFileTypes:true}).filter(e=>e.isDirectory()&&RE.test(e.name))'` |
| 3.2.2 | Matching symlinks at depth 1 | **0** | `find . -maxdepth 1 -type l -regextype posix-extended -regex …` |
| 3.2.3 | SHONEN.md files among the 19 | **19 / 19 present** | `ls *-shokunin/SHONEN.md` |
| 3.2.4 | Canonical boxes across the 19 | **76** (19 × 4; no added/removed box) | `grep -c '^- \['` |
| 3.2.5 | `MANIFEST.json` | rounds **142**, roster rows **13**, entries by type: mint **8**, closure **15**, other **119** | `node -e` JSON count |
| 3.2.6 | Selector digest, two observations | baseline `68939d0c…` (round-9 source) → current `e7d49942…` (976 lines, uncommitted) | `sha256sum` twice |

---

## 4. SHONEN

### 4.1 The four canonical boxes (verbatim, `PROTOCOL.md:425-428`)

| Box | Text |
|---|---|
| B1 | `[ ]` SKILL.md contains real decision tables, error patterns, checklists, cited sources |
| B2 | `[ ]` At least one end-to-end domain task executed and logged in LOG.md |
| B3 | `[ ]` Instructions executable by an agent without oral context |
| B4 | `[ ]` No cross-domain bleed (PROVINCE.md still accurate) |

Seed header is `# <name> — Promotion checklist` with `<name>` the only substitution
(`PROTOCOL.md:419-428`). No root `SHONEN.md` exists at MAIN_ROOT (§0.13), so the four boxes
attach to **child** repos; the aggregator's round-10 report carries the four-box assessment as
prose only and grants nothing.

### 4.2 Marks (spec, `PROTOCOL.md:430-431` + `63-73`)

| Mark | Meaning | Gate effect |
|---|---|---|
| `[ ]` | untouched / unmet | — |
| `[~]` | asserted by the lane itself; must carry a resolvable evidence pointer | assertion only |
| `[x]` | requires a **named non-author verifier** on the mark line (`[x] <verifier-id>`) | any `[x]` with no named non-author verifier **counts as `[~]`** |

Additional mechanical rules: marks are confined to the box character plus one indented evidence
line per box; no added/removed boxes; byte-identical seed modulo `<name>` (`PROTOCOL.md:413`).

### 4.3 Mark census (read-only, current tree; MD5 per file)

| Lane | boxes | `[x]` | `[~]` | `[ ]` | `[x]` lines with no inline verifier token (→ `[~]`) | SHONEN.md md5 |
|---|---|---|---|---|---|---|
| audio | 4 | 0 | 1 | 3 | 0 | `8a952425a2cefbf6a00dcf504764c906` |
| chousa | 4 | 0 | 0 | 4 | 0 | `e1f01c34ef562f639681867efd4a47f5` |
| game-dev-2d | 4 | 0 | 0 | 4 | 0 | `b04b935703bbaee9173dd8c2f81d7100` |
| game-dev-3d | 4 | 1 | 0 | 3 | 0 | `339a470cb9ced1441213a7399e619a79` |
| kagi | 4 | 4 | 0 | 0 | **4** | `f733f3a7d28035b0dd608850c3dc889c` |
| kaidoku | 4 | 4 | 0 | 0 | **4** | `26cb5c5b1bf898dc6369a67fe8c95595` |
| kake | 4 | 0 | 0 | 4 | 0 | `084794b025e93e038478e42d53d3f53c` |
| kama | 4 | 0 | 4 | 0 | 0 | `dfb3509f63573b682a7cbc704dae84b7` |
| kasegi | 4 | 0 | 0 | 4 | 0 | `e07f6a278aa7e27d4134507863b5cfc0` |
| kengaku | 4 | 0 | 4 | 0 | 0 | `878b5a76ff8ae386c92235bed7dc64e6` |
| kotoba | 4 | 0 | 4 | 0 | 0 | `8cb12fa47ffbe5334f137600d21b35ec` |
| kumitate | 4 | 0 | 0 | 4 | 0 | `531ce597e5be89bc71fb0fb6389ac2c5` |
| lore | 4 | 0 | 2 | 2 | 0 | `294f3e4963bdd926bc1c2045b2759da6` |
| mado | 4 | 0 | 4 | 0 | 0 | `8f6cab7fca09eb2a70cffc139f9436e7` |
| mori | 4 | 0 | 0 | 4 | 0 | `bdb0815284e210c60c4abb9946a4f36e` |
| revenger | 4 | 4 | 0 | 0 | 0 | `8c1cc47ed0ef029b9c4eb21aa1315354` |
| tabi | 4 | 4 | 0 | 0 | 0 | `fbbaf7c7a0937ae3cc157a6443ca3c6a` |
| tameshi | 4 | 0 | 3 | 1 | 0 | `24fbc4f6e8761ffb8af6e6cb7ccf6e33` |
| tsukuroi | 4 | 0 | 4 | 0 | 0 | `9cf1d450685ae0ed0d15dee1b54e8fd5` |
| **total** | **76** | **17** | **26** | **33** | **8** | — |

Corollaries: 17 `[x]` marks exist; **8** of them (kagi ×4, kaidoku ×4) carry no inline verifier
token and therefore read as `[~]` for the gate. 9 `[x]` marks carry an inline verifier token and
are form-valid. Whether any box claim is *true* is prose and is not machine-checkable from the
graded tree.

**Marks move between observations (lane-authored).** Two reads in this session differ: tameshi
went from 4 `[x]` / 0 `[~]` to 0 `[x]` / 3 `[~]` / 1 `[ ]` (md5 `dfc81c8c…` → `24fbc4f6…`), and
kama/kengaku/tabi/kotoba moved off `[x]` relative to the inherited census. The table above is a
point-in-time census with per-file md5s; every mark total is a snapshot, not a stable property.

**Drift vs the inherited census** (`.ufo/waves/aggregator-r10/seats/scribe.md` §3b): that census
recorded 6 lanes with bare `[x]` (kagi, kaidoku, kama, kengaku, tabi, tameshi) and kama 4 `[x]`.
The current tree shows kama/kengaku/tabi/tameshi reverted to `[~]` and only kagi/kaidoku bare.
The inherited per-lane counts are therefore **historical**, superseded by the md5-pinned table
above; marks are lane-authored and move between observations.

### 4.4 Independence ruling — no author-dispatched reviewer qualifies

| # | Rule | Source |
|---|---|---|
| 4.4.1 | A promotion box needs a reviewer who did **not** author the round's changes; a subagent the lane dispatched **is still the lane**; self-attestation is not verification | `PROTOCOL.md:63-68` |
| 4.4.2 | Only a non-author `<id>` may write `[x]`; an `[x]` with no named non-author verifier is author attestation and counts as `[~]` | `PROTOCOL.md:63-73` |
| 4.4.3 | Live precedent: kotoba's round-13 note reverts its round-11/12 `[x]` marks to `[~]` because they rested on lane-dispatched subagents (`ReviewSHONEN`, `ColdRunRecord`); the only non-author evidence on record is another lane's (aggregator r8) cold run | `kotoba-shokunin/SHONEN.md` |
| 4.4.4 | Caveat class: kaidoku's box 2/3 were self-checked at r1 before later audits (flagged) — audit-after-self-check does not retroactively supply the verifier | `kaidoku-shokunin/SHONEN.md` |
| 4.4.5 | This wave's seats are author-dispatched by the aggregator L1: **R10Evidence, R10Critic, R10Plan, R10Surface, R10Overlap, R10Regression, R10Selection, R10Census (and an unobserved R10Review) are all the aggregator lane**. None may write `[x]` for, or serve as the named non-author verifier of, any box in this round | `dispatch.json`; `CONTEXT.md` |
| 4.4.6 | Machine check cannot see independence: the gate's `shonen` check reads a verifier token, not the authorship graph; `box-3` and `shonen-semantics` are declared **not evaluated** | `.ufo/waves/round-9/corpus-gate.mjs` declared exclusions (inherited) |

Consequence for the parent's appended report: use `[~]` only for author-supported assertions and
`[ ]` for unmet/unexercised boxes. No `[x]` may be issued in round 10 by any seat of this wave.

---

## 5. Cross-domain evidence (report contract item)

### 5.1 Open L0 question census — by stable lane / round / opening words

Source: `.ufo/l0-questions.md` (append-only; **moving target** — observed growing during this
session: 25 lines [inherited scribe census] → 34 → 36 → 39 → 41 → **43 newline-lines** at the
final pin). Pin at census: md5 `073f8e061417de9a90214cc2f5e6a7c2`, **39 question lines**,
**33 distinct lane|round groups**, relaunch divider at line 23. Cited by lane/round/opening words,
never line number; the Main-appended custody question carries the stable key `current43`. Seven
entries were appended *during* this observation window (`mado r1`, `kasegi r17`, second `kake r16`,
`kotoba r16`, `kama r1` freshness addendum, `tsukuroi r1`, `aggregator r10`) and the file kept
growing after each pin; counts are a point-in-time observation, not a stable property. The census
below is the complete set at the pinned digest.

Full census (39 lines):

| Lane | Round | Opening words | Open-decision class |
|---|---|---|---|
| kasegi | 12 | "`~/Projects/bounties` is stalled mid-interactive-rebase" | git custody / rebase resolution + who resolves |
| protocol | 10 | "kama mint decision (pending since round 2/4)" | roster mint vs recorded rejection |
| protocol | 10 | "Operator-side driver/template debt: (1) `lane_prompt()` emits 1 of 5 child-lane contract items" | driver/template + `report_of()` completion semantics + tracked `.ufo/state` |
| kagi | 10 | "`cmd_refs` … redaction is a prefix match" | secret-redaction strictness (mechanism only; no values cited) |
| kake | 12 | "`webzites-keeper.timer` … loaded but DISABLED+inactive" | enable vs retire keeper-tick automation |
| aggregator | 6 | "Axis vocabulary split (ledger row D-78)" | MISSION vs AXES axis names undefined |
| kengaku | 10 | "Promote the gate convention (exit 0/1/2 + `--selftest` …)" | fleet-wide gate standard |
| kumitate | 10 | "Should the fleet adopt `round-gate.mjs` at the driver level?" | driver-level round gate |
| kumitate | 11 | "Fleet adoption of the machine-readable scorecard claim block?" | scorecard re-derivability block |
| kasegi | 15 | "`~/Projects/bounties` — the kasegi PROVINCE root … is GONE" | FS prune regime / province-root loss |
| kotoba | 13 | "Axis-accounting ratification, two items" | advisory-axis ratification + D-78 |
| aggregator | 9 | "`CORPUS.md` amendment set — four measured conflicts" | operator-side corpus text amendment |
| kama | 1 | "Local model endpoint drift is proven and still live" | endpoint port pins vs served port |
| kake | 15 | "corroboration on kasegi\|r15 vanished-root" | FS drift corroboration |
| kama | 1 | "Addendum to the repoint question (same decision, larger blast radius …)" | provider restriction + declared-vs-served context |
| kasegi | 16 | "SECOND in-round source loss on a surviving domain root" | unrecoverable mission-dir loss |
| kama | 1 | "Fleet hygiene gap (one line, your call as it is a main-repo meta-file)" | `.gitignore` omission; tracked/untracked state pair |
| kake | 16 | "corroboration update on the kasegi r15/r16 vanished-root items" | escalating prune regime W1–W5 |
| kake | 17 | "FS-cleanup/prune regime W6" | lowercase/uppercase namespace cleanup, informational |
| kama | 2 | "`tools/kama-probe.sh snapshot` … no scheduler exists" | systemd user timer creation |
| tabi | 5 | "Operator approval requested — filed: … `operator-approval-request.md`" | R1/R2/R3 answered-by-ID approval packet |
| kumitate | 17 | "The 2026-10-15 steer reuses round 17 although lane LOG.md already records round 32" | per-lane counter reconciliation |
| tameshi | 1 | "Relaunch numbering and routing reconciliation" | separate fleet-run namespace for counters |
| mori | 1 | "Which operator-selected remote URL should this lane use?" | **lane remote unset** |
| game-dev-3d | 1 | "Reconcile the relaunched round counter and craft-swarm contract?" | counter + planner-vs-validator |
| chousa | 1 | "Which operator-selected remote URL should chousa-shokunin use?" | **lane remote unset** |
| kama | 1 | "Reconcile the relaunched counter and craft dispatch contract before the next launch?" | counter + MISSION axis assignment vs prompt |
| game-dev-2d | 1 | "Ratify the relaunched score/round namespace and craft dispatch shape?" | namespace + numeric rubric missing |
| lore | 1 | "Reconcile the relaunched counter, numeric rubric and craft dispatch contract" | namespace + rubric + role buckets |
| tabi | 1 | "Reconcile the relaunched round namespace and craft dispatch wording" | namespace + dispatch contract |
| kengaku | 13 | "Reconcile the relaunched round namespace and craft-batch contract" | namespace + advisory-axis tie-break |
| kagi | 16 | "Reconcile the relaunched counter and craft dispatch contract" | namespace + route-bucket alignment |
| mado | 1 | "Ratify the relaunched round namespace, bounded score rubrics and native craft dispatch shape" | namespace + rubric |
| kasegi | 17 | "Reconcile the relaunched round namespace and craft dispatch contract" | namespace + host connector/critic buckets |
| kake | 16 | "Reconcile the relaunched round namespace and craft-dispatch wording" | namespace + host role table |
| kotoba | 16 | "Reconcile the relaunched round namespace and craft-batch contract before the next launch?" | namespace + craft-batch contract |
| kama | 1 | "2026-10-15 freshness addendum to the historical 'Local model endpoint drift …'" | freshness addendum to the endpoint-drift decision (same open decision as kama r1) |
| aggregator | 10 | "Corpus-review custody reconciliation: …" (stable key **`current43`**) | three Devin corpora reserved; discovery still represents all 19 physical children; metadata verdicts + durable handoff; lessons only for the other 16 |
| tsukuroi | 1 | "Ratify the explicitly steered fleet round-1 namespace after the historical lane-r11/training-r10 closeout, and arbitrate the kaidoku/revenger shipped-artifact overlap …" | namespace + cross-lane overlap arbitration (ADJ-06) |

Per-lane totals: kama **6**, kake **5**, kasegi **4**, aggregator **3**, kumitate **3**, protocol
**2**, kagi **2**, kengaku **2**, tabi **2**, kotoba **2**, mori **1**, chousa **1**, lore **1**,
mado **1**, tameshi **1**, tsukuroi **1**, game-dev-2d **1**, game-dev-3d **1**. (Sums to 39.)

Drift vs inherited census: the inherited scribe table recorded 18 question lines and omitted the
2026-10 relaunch entries beyond `tabi r5`; the current file has 39. The inherited census is
historical, not wrong at its pin.

### 5.2 mori / chousa remote questions (surfaced explicitly)

| # | Fact | Value | Pointer |
|---|---|---|---|
| 5.2.1 | mori r1 asks which operator-selected remote URL the lane should use | `git remote -v` in the lane returned no rows; `MINT.md` names no remote; `MANIFEST.json` has no mori roster row | `.ufo/l0-questions.md` (mori r1) |
| 5.2.2 | Verified: mori has **0** git remotes | `git -C mori-shokunin remote` → 0 rows | read-only command |
| 5.2.3 | Verified: mori is **absent** from the 13 manifest roster rows | `MANIFEST.json.roster` does not contain `mori` | JSON key scan |
| 5.2.4 | chousa r1 asks the same question for its own lane | no rows at baseline `34774a1777d4058ca8c2b4456ce2e6ccee9e24c5`; `shokunin.conf` names fleet origin but no chousa remote | `.ufo/l0-questions.md` (chousa r1) |
| 5.2.5 | Verified: chousa has **0** git remotes; chousa also absent from the roster | `git -C chousa-shokunin remote`; roster scan | read-only commands |
| 5.2.6 | Both lanes state they will commit locally, push only to the configured fleet origin, create no remote, and that the integrator owns committing the question | — | L0 entries |
| 5.2.7 | Effect on this move's scope | Neither lane's remote is inferred from sibling naming; no remote is created by any seat. The corpus move is unaffected; the decision stays with the operator | `CONTEXT.md` push-scope |

### 5.3 Round-namespace conflicts (surfaced explicitly)

Several lanes filed round-namespace reconciliation questions in the same watchdog window. Pattern:
a steered round number that is lower than the lane's own recorded history, with the prior filed
report preserved and a dated continuation appended.

| Lane | Steered round | Lane history referenced | What is preserved | Pointer |
|---|---|---|---|---|
| kumitate | 17 | LOG records round 32; `.ufo/reports/round-17/kumitate.md` is a filed 76-line report | filed report; append dated continuation | L0 kumitate r17 |
| tameshi | 1 | completed training arc through round 11 at `284ab0f0…` | historical rounds unrewritten | L0 tameshi r1 |
| game-dev-3d | 1 | history through r87 at `db649433…`; inherited uncommitted r88 reports | r88 reports preserved | L0 game-dev-3d r1 |
| game-dev-2d | 1 | inherited r78 scorecard/log at `884a4c42…` | history preserved; axes were unscored | L0 game-dev-2d r1 |
| lore | 1 | inherited r85 at `5eb9451b…` | all three axes unmeasured | L0 lore r1 |
| tabi | 1 | completed training round 11 at `c24eaea1…` | historical records intact; fleet-round-1 label | L0 tabi r1 |
| kama | 1 | history through round 4 at `c390918f…`; `round-1/kama.md` already filed | filed bytes preserved + dated continuation | L0 kama r1 |
| kengaku | 13 | history through round 16 at `3f31e54c…`; round-13 plan already filed | both preserved | L0 kengaku r13 |
| kagi | 16 | lane records through round 19 at `15ea78c7…` | existing round-16 report gets only a dated append | L0 kagi r16 |
| kasegi | 17 | history through round 20 at `4b2e3023…`; round-17 report filed | historical report/LOG bytes intact | L0 kasegi r17 |
| kake | 16 | records through round 19 at `20d13115…`; round-16 report already filed | historical bytes intact | L0 kake r16 |
| mado | 1 | closed training arc through round 11 at `bb08dd57…` | SCORECARD had no numeric rows | L0 mado r1 |
| kotoba | 16 | lane records through round 19 at `581e2932…`; round-16 report already filed | historical bytes preserved; dated continuation; no counter mutation | L0 kotoba r16 |

Related axis-vocabulary conflict already on the queue: aggregator r6 (D-78) — `MISSION.md`
assigns `novelty`/`consistency` to kengaku/kotoba while `AXES.md` defines neither.

This round's own steered number is **round 10** while the card's latest sections are round 11
(`SCORECARD.md:289-305`) and `.ufo/state/aggregator.round` = 10. Same class: steered number ≠
latest recorded lane-round; resolved by `PROTOCOL.md:85-89` (externally steered number binds;
several entries may carry one steered round over a lane's own numbering).

### 5.4 Role-routing conflicts (surfaced explicitly)

| # | Declared | Observed | Class |
|---|---|---|---|
| 5.4.1 | MISSION requires a **planner** seat in one ≥8-member L2 batch | The generic UFO standalone-wave validator **excludes planner** (`unknown_role`) and declares a different band | Contract mismatch across lanes: tameshi r1, game-dev-3d r1, kama r1, game-dev-2d r1, lore r1, tabi r1, kengaku r13, kagi r16, kasegi r17, kake r16, mado r1 |
| 5.4.2 | `MISSION.md` §L2 maps role **classes** to route **buckets** (planner/connector heavy-reasoning; executor/scribe/scout fast-execution; reviewer/critic/sentinel/revenger/labrat/mutation-tester/simplifier/distiller economy w/ fallback) | Lanes report the live host tables' actual buckets differ from the MISSION prose (lore r1, kasegi r17, kake r16, tameshi r1, kagi r16) | Documented divergence; operator-owned table is authoritative |
| 5.4.3 | Host route authority pointer | `~/.omp/agent/config.yml:318-332` binds **14** taxonomy role ids to `@m_*` route aliases (role ids public in `PROTOCOL.md`/`MISSION.md`; alias strings deliberately not reproduced) | Route resolution is role-based, never model-pinned by a lane |
| 5.4.4 | `MISSION.md` §Fleet shape says each lane declaration carries `id`, `cwd`, **`route`**, `axes` | Shipped `shokunin.conf` `LANES` grammar is `id\|cwd\|axes` — **no route field**; the route table appears only as a commented-out shape example | Config-vs-mission grammar divergence; no route is set per lane |
| 5.4.5 | `MISSION.md` §Fleet shape lists the **nine** initial lanes | `shokunin.conf` declares **18** lanes (protocol + aggregator + 16 child) | MISSION text is stale relative to the shipped config |
| 5.4.6 | Generic-wave exclusion is why this batch is a native OMP task mapping | `.ufo/waves/aggregator-r10-resume/dispatch.json` sets `generic_ufo_wave: false` with the boundary stated; inherited `dispatch.json` states the same | No UFO mission created; no routing mutation |

### 5.5 Three divergent lane universes (scope boundary for this move)

| Universe | Count | Composition | Pointer |
|---|---|---|---|
| Physical direct child dirs matching the selection regex | **19** | audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, mado, mori, revenger, tabi, tameshi, tsukuroi | §3.2.1 |
| `shokunin.conf` lane declarations | **18** (16 child + 2 main-repo) | excludes **audio, game-dev-2d, game-dev-3d** ("the three Devin-owned lanes", `99efc52`) | `grep -cE '^[a-z0-9-]+\|'` |
| `MANIFEST.json` roster rows | **13** | kasegi, kengaku, kake, kumitate, kotoba, kagi, kama, audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku — excludes mori, chousa, mado, tabi, tameshi, tsukuroi | JSON roster scan |
| Selector default at baseline | **6** | kasegi, kengaku, kake, kumitate, kotoba, kagi | `.ufo/waves/round-9/corpus-gate.mjs:165-172` |

The selected fix enumerates the **first** universe only; the other three are not conformance
targets of this move and must remain named limits. Configured-but-absent paths and the three
Devin-owned lanes' non-declaration are separate operator decisions.

**Operator custody boundary (binding on this wave; `CONTEXT.md:28-30`, `LOG.md:701-708`).**

| # | Rule |
|---|---|
| 5.5.1 | `audio`, `game-dev-2d`, `game-dev-3d` are **Devin-owned** and were removed from `shokunin.conf` `LANES` (and the full-roster backup); their lane processes were killed and no process touches those repos. The fleet is **18 configured lanes = 16 child + 2 root**, while **19 physical child dirs** remain present. |
| 5.5.2 | The selector still includes all **19** physical corpora; the three Devin-owned repos stay **READ-ONLY**. Metadata-only verdicts stay in the fleet report; **no lesson, commit or push** in those three repos. |
| 5.5.3 | The collector must **not** equate the local directory set with the configured fleet: 19 local discovery members ≠ 18 configured lanes ≠ 13 manifest roster rows ≠ 6 baseline defaults. Coverage is claimed over the enumerated local set only. |
| 5.5.4 | Parent mirrors per-repo lessons only to the **other 16** child repos; the remaining child-corpus lesson duty proceeds under the canonical aggregator exception. |
| 5.5.5 | Record this discrepancy as a **boundary**, not as a mint/dormancy call and not as a discovery code filter: no exclusion rule may be added to the selector for these three names, and no lifecycle/roster inference follows from their presence or non-declaration. |
| 5.5.6 | This boundary is itself filed as an open L0 question: `aggregator \| round-10 \| Corpus-review custody reconciliation:` (stable key `current43`) — discovery still represents all **19** physical children while only **16** child lesson mirrors proceed; parent records metadata verdicts and the durable fleet handoff. |
| 5.5.7 | Parent-recorded motivation for this move: `LOG.md:723-743` (round-10 relaunch: 6/19, 13 omitted, one nine-seat native batch, custody respected) and `SCORECARD.md:398-417` ("### Round 10 (2026-10-15 relaunch) — selected move"; planned at `:409-414`; retired: none). |

---

## 6. Inherited vs this batch (lineage)

| Artifact | Batch | sha256 | Status |
|---|---|---|---|
| `.ufo/waves/aggregator-r10/before.json` | **inherited** (prior wave) | `afecb2fda4e1f78e01b5e3863480c75de4588228cc781278148eb8b7753f57ae` | historical authority for the before column |
| `.ufo/waves/aggregator-r10/dispatch.json` | **inherited** | — | historical dispatch metadata (roles CorpusPlan etc.) |
| `.ufo/waves/aggregator-r10/count-before.log` | **inherited** | — | 6 `# summary` lines + `# process-exit 1` |
| `.ufo/waves/aggregator-r10/before-summaries.log` | **inherited** | — | same 6 summaries, metadata only |
| `.ufo/waves/aggregator-r10/seats/plan.md` | **inherited** | `e55d23b5b3e8766ab40e9f971b63d18cc37622af0310a43486f1efb64ba82f49` | prior plan/falsifiers |
| `.ufo/waves/aggregator-r10/seats/critic.md` | **inherited** | `6ce3f3a0d62783068d19d14825fec8fbb1fad729788aee0a9d5fcebe4b0838e1` | prior counterexamples C1–C12 |
| `.ufo/waves/aggregator-r10/seats/scout.md` | **inherited** | `da3dfd1d46efede947414ed747cebc64d268f930ba678c96270397da8f115b99` | prior per-lane surface map |
| `.ufo/waves/aggregator-r10/seats/scribe.md` | **inherited** | `b102bf65e0b534c6dd20e776d82ad5c53e962b74b69bca06ad57f33e2277e245` | prior report-shape/SHONEN/L0 analysis |
| `.ufo/waves/aggregator-r10-resume/CONTEXT.md` | **this batch** | `5be9925297b2ee4ed500bd411c251b6a371df36ca25285945365f6113b66c52b` | canonical assignment + operator custody update (§5.5) |
| `.ufo/waves/aggregator-r10-resume/before.json` | **this batch** | `671514a0cb0c478e2ce3872324c59a5c93f4b29e7f81adade5bf2e9c9204f749` | metadata recount of the inherited run; `inherited_runtime_measurement` names its source |
| `.ufo/waves/aggregator-r10-resume/dispatch.json` | **this batch** | `76de24c48661c643b5fb12e1a724ee27a152f8e15d38b9c750600a8d8788d6cb` | 9 seats, `inherited_evidence` explicitly disclaimed |
| `.ufo/waves/aggregator-r10-resume/plan.md` | **this batch** (R10Plan) | `6d119a4361e024c6dbbb5d36c7a4195e8a551e7e7fbf24e4e4cf255e696b8147` (16586 B) | advisory |
| `.ufo/waves/aggregator-r10-resume/critic.md` | **this batch** (R10Critic) | `5d51a430b1d8fbd8e67014b8cb885c8fbc4076b2c42e0c35aa8eee0850ba60d8` (18548 B) | advisory falsifiers F1–F15 |
| `.ufo/waves/aggregator-r10-resume/surfaces.md` | **this batch** (R10Surface) | `35b86024b2ba36197803985bb5da9de7a65f84a4b3262e7eea3092acd6779225` (20172 B) | advisory lane-surface recon |
| `.ufo/waves/aggregator-r10-resume/preservation-pins.json` | **this batch** (sibling) | `5463a068998ee64979f9be9cc96bb794c99c95d6383e13876b6d9e0abc88d0d5` | historical preservation inputs, self-labelled "not verification results" |
| `.ufo/waves/aggregator-r10-resume/selection.md` | **this batch** (R10Selection) | `7a81e775e3368c1c819cf925b83a39bcd002108f548776dff79181c685953f29` (5864 B) | change record for the uncommitted selector edit |
| `.ufo/waves/aggregator-r10-resume/measure-corpus.mjs` | **this batch** (R10Census) | `fefbf2ff9f0aa29c25daa16696a269182c0491572aac6276ced42325bd7bbf9c` (21424 B) | redacted collector script (**not executed by this seat**) |
| `.ufo/waves/aggregator-r10-resume/evidence.md` | **this batch** (R10Evidence, this file) | `79d76d41…` (at the last hash sweep; file edited after) | this matrix |

Nothing in `.ufo/waves/aggregator-r10/` may be claimed as this batch's dispatch or output. The
resume `before.json` records that boundary itself.

---

## 7. Historical marker preservation (report path)

| # | Fact | Value |
|---|---|---|
| 7.1 | Path | `.ufo/reports/round-10/aggregator.md` |
| 7.2 | Size / digest | **187 bytes**, md5 `75eaefe096ac72d22598809416888cfd`, sha256 `ab5150b6087049d1dc12188b83af9ab2bbe505dcc026169aef6fa2dda2f471a1` |
| 7.3 | Introducing commit | `f5d8507` ("fleet-wrap: sentinel + aggregator r10 closeout; respawn-per-round halted at current round per lane") |
| 7.4 | Body (4 lines) | `# aggregator round-10 closeout (marker)` / Fleet wrap paragraph / "In-flight work survives in the main repo working tree." / "Not respawning." |
| 7.5 | Governing rule | filed report bytes are never rewritten; a correction lands as an appended erratum in a **new commit** naming the superseded text (`PROTOCOL.md:126-136`) |
| 7.6 | Append acceptance check (to run **after** the append, by parent) | `head -c 187 .ufo/reports/round-10/aggregator.md \| md5sum` still yields `75eaefe096ac72d22598809416888cfd` |
| 7.7 | Why the append is load-bearing | the marker alone grades `marker-overwrite` (187 B < the committed gate's 1024 B floor), so the path is a conformance defect until a real section lands; the appended section must itself carry `SHONEN` + ≥1 evidence pointer + landed-changes-with-`LOG.md`-entries + a checkable commit-hash citation (`PROTOCOL.md:145-151,178`) |
| 7.8 | Dated section requirement | append an explicitly dated current section; do not imply this wave's work or review happened at the marker's time |
| 7.9 | Stored preservation inputs (sibling artifact) | `.ufo/waves/aggregator-r10-resume/preservation-pins.json` pins baseline commit `b598ce0e…`, gate `68939d0c…`, `expected.json` `9af28e2e…` (17277 B) and the marker `ab5150b6…` (187 B); it self-labels these "historical preservation inputs, not verification results" — they are inputs, and the parent must still verify the post-append bytes (§7.6) |

---

## 8. Limits and non-claims

1. **No after-state exists.** The selector edit is present in the worktree (`e7d49942…`,
   uncommitted) but no regression harness or collector existed at observation (§0.9, §1.8–1.10),
   and no gate/test was run. Every "after" cell is empty by measurement, not by omission.
2. **No gate/test executed by this seat.** §3.2 rows are read-only counts; they are not gate
   verdicts and cannot substitute for the parent's isolated before/after CLI run, selftest, frozen
   replay or actual redacted census.
3. **Live, moving surfaces.** HEAD moved twice, `.ufo/l0-questions.md` grew 25→39 newline-lines,
   and lane `SHONEN.md` marks moved between observations. Every pin here is point-in-time.
4. **Coverage ≠ conformance.** Selecting 19 directories does not establish semantic CORPUS
   conformance; the gate declares r1, r3, r5, r6, r9, box-3 independence and shonen-semantics as
   **not evaluated** (inherited), and configured-but-absent paths are outside the claim.
5. **Snapshot limits.** A live-worktree census is not an atomic or frozen snapshot (baseline
   already carries one `dirty=1` lane).
6. **No promotion inference.** No `[x]`, no rank change, no mint/dormancy transition, no
   promotion follows from anything in this file.
7. **No verdict.** Broad score stays 9/9/9 per the inherited authority; only the canonical judge
   issues per-axis verdicts.
8. **Not written here.** The final report, per-repo verdict lessons, AGGREGATE refresh,
   LOG/SCORECARD appends, commit and push are the parent's duties and are unperformed.
9. **Custody limit.** Three of the 19 physical children (`audio`, `game-dev-2d`,
   `game-dev-3d`) are Devin-owned and out of this wave's write scope entirely: no lesson, commit
   or push there; the local-set tally is not evidence about configured fleet membership (§5.5).

---

## 9. Actionable pointers for the parent (in execution order)

1. **Before capture (already available):** `.ufo/waves/aggregator-r10/before.json` (6/19, 13
   omitted, exit 1, gate `68939d0c…`, commit `b598ce0e…`) — do not re-run the old live gate.
2. **Bind the measured source first:** the fix currently sits uncommitted in the worktree
   (`e7d49942…`, 976 lines). Commit it inside the round, then measure **that named revision**;
   a worktree run is not comparable to one over the cited commit (`PROTOCOL.md:359-402`).
3. **After capture (parent only):** run the fixed `.ufo/waves/round-9/corpus-gate.mjs --all
   --round 10` once on isolated trees + `node .ufo/waves/aggregator-r10-resume/measure-corpus.mjs`
   (when landed) capturing stdout to a wave path; compare **exact sorted label sets**, not counts.
4. **Regression:** `selection-regression.mjs` before/after replay (`--gate <source>`) plus existing
   `--selftest` and the 8 frozen keys / 12 cases in `.ufo/waves/round-9/corpus-gate.expected.json`
   (do **not** rebaseline them; digests stored in `preservation-pins.json`).
5. **Marker append:** append the dated section to `.ufo/reports/round-10/aggregator.md`; verify
   7.6 afterward; ensure §7.7 content contract is met.
6. **SHONEN section of that report:** four boxes from §4.1, marks per §4.2, no `[x]` (§4.4).
7. **Cross-domain naming:** carry §5.1–5.5 conflicts into the round notes / operator queue; the
   mori and chousa remote questions (§5.2) and the three-lane non-declaration (§5.5) are
   operator-side.
8. **Custody:** keep `audio`, `game-dev-2d`, `game-dev-3d` read-only; report their metadata
   verdicts in the fleet report only; mirror lessons to the other 16 child repos; never equate the
   19-member local set with the 18 configured lanes (§5.5).
9. **Records:** per-repo verdict lessons, append-only AGGREGATE refresh, LOG/SCORECARD appends,
   then commit-then-push (fleet remote only; no child push; child commits restricted to
   aggregator-owned corpus files).