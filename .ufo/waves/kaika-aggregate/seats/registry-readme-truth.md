# Seat: registry / README truth — round 12

Status: **complete for the assigned checks; no README/MANIFEST/conf/report/gate was modified.**
Scope: worktree README roster + Files statements vs `MANIFEST.json` roster, `shokunin.conf`
LANES, and the 21 physical `<id>-shokunin` local dirs. All 21 lane repos were read with git
read-only commands only.

Provisional-status declaration (parent direction): the source-row census parser fix for
indented Markdown rows is in progress elsewhere. **No census/source-row total is asserted
here.** The numbers below are MANIFEST/git/config set arithmetic at a fixed revision, not
lane source censuses, and final census totals still wait for the parent's `FINAL LANES READY`.

## 0. Revision and paths (exact)

Audited file (current worktree README, committed and clean):

```
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
git rev-parse HEAD
  -> ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2        (branch kaika/aggregate)
git status --porcelain README.md MANIFEST.json shokunin.conf ROADMAP.md
  -> (empty)  ; porcelain_exit=0
sha256sum README.md MANIFEST.json shokunin.conf ROADMAP.md
  -> a84a0f7b2727920499e6f05a3e0d480e3225d5b2b0b2b10ad4668bf25b3abb0e  README.md
  -> de481567aaa629a16e955be3777e1d39e36f9dcb3d6e3062890d471d029a7b08  MANIFEST.json
  -> a42e8406082ebb9a4248d91df06cb331c365b94e3ce877a6d8652363baebc5ee  shokunin.conf
  -> 71eca52a006e03389cc970dc247ef90589fecf8a5584a857bb9e0171b81d47a4  ROADMAP.md
```

`README.md` is 125 lines. Claims audited at: L12–15 (fleet-root/registration sentence),
L46 (lifecycle repo sentence), L88–91 (roster preamble), L93–110 (16-row table),
L112–114 (2026-10-16 mori/chousa note), L117–125 (Files block; L122 is the round count).

Second surface, **not mine and not committed** — see §7: the main checkout
`/home/vgpnk/Projects/shokunin` is on `master` at `dcf3b64` (merge of kaika/protocol,
kaika/contract, kaika/census, kaika/driver) with `README.md` dirty (`git diff --stat` =
`1 file changed, 65 insertions(+), 44 deletions(-)`), i.e. somebody already drafted the
corrected wording there. It is working-tree state, not a commit; I read it for comparison
only. Main `MANIFEST.json` at that revision has `roster=13 rounds=312` vs the worktree's
`314` (worktree is +2 ledger entries; HEAD commit `ee8ba85` is *not* an ancestor of `dcf3b64`).

## 1. Populations (each measured, exact)

| Surface | Count | Exact set |
|---|---|---|
| Physical dirs `/home/vgpnk/Projects/shokunin/*-shokunin` | **21** | audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi |
| `MANIFEST.json` `.roster` rows | **13** | kasegi, kengaku, kake, kumitate, kotoba, kagi, kama, audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku |
| `ROADMAP.md` roster table (L7–19) | **13** | same ids as the manifest roster (names given as `<id>-shokunin`) |
| `shokunin.conf` LANES entries | **20** | 2 fleet lanes (`protocol`, `aggregator`) + 18 child lanes: kaidoku, kasegi, kengaku, kake, kumitate, kotoba, kagi, kama, lore, revenger, tameshi, mado, tsukuroi, tabi, mori, chousa, kotodama, souji |
| `.ufo/state/*.round` lanes | **21** | aggregator, audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, mado, mori, protocol, revenger, tabi, tameshi, tsukuroi |
| README roster table rows | **16** | the 13 manifest ids + mori, chousa, kotodama |

Commands used (outputs abbreviated):

```
ls -1d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l
  -> 21
jq -r '.roster|length' MANIFEST.json                      -> 13
jq -r '[.roster[].id]|join(" ")' MANIFEST.json            -> kasegi kengaku kake kumitate kotoba kagi kama audio game-dev-2d game-dev-3d lore revenger kaidoku
python3 (regex over shokunin.conf LANES pipe rows):
  lanes_total=20 child=18 fleet=['protocol','aggregator']
ls -1 .ufo/state/ | sed 's/\.\(mission\|out\|round\)$//' | sort -u
  -> aggregator audio chousa game-dev-2d game-dev-3d kagi kaidoku kake kama kasegi
     kengaku kotoba kumitate lore mado mori protocol revenger tabi tameshi tsukuroi   (21)
grep -c -E '^\| \[[a-z0-9-]+\]\(https://github' README.md -> 16
```

## 2. Exact mismatch: operator-controlled roster vs local repositories

**Child-lane set difference, both directions (exact):**

```
physical(21) − conf-child(18) = audio, game-dev-2d, game-dev-3d        (3)
conf-child(18) − physical(21) = ∅                                      (0 missing)
```

**Why the three are absent — deliberate, cited, and still dispatched:**

- `git show 99efc52 --format='%h %cI%n%B' -- shokunin.conf` →
  `99efc52 2026-10-15T01:52:09-03:00` / `ops: exclude the three Devin-owned lanes
  (18 remain); add the wall lane-watch view`; the diff removes exactly
  `audio|audio-shokunin|…`, `game-dev-2d|game-dev-2d-shokunin|…`,
  `game-dev-3d|game-dev-3d-shokunin|…`.
- Six minutes earlier `7d02e96` (2026-10-15T01:46:20, "start the 21-lane fleet driver")
  had generated `audio-round-1.md`, `game-dev-2d-round-1.md`, `game-dev-3d-round-1.md`
  among 21 first-round prompts.
- They are still being dispatched by the wave orchestrator, not the local watchdog:
  `git log --diff-filter=A -- .ufo/prompts/audio-round-101.md .ufo/prompts/game-dev-2d-round-105.md .ufo/prompts/game-dev-3d-round-108.md`
  → all three added by `5b471e4 2026-10-19T18:23:55-03:00 kaika: W1 research dossiers (52),
  frozen SOURCES contract v1, steer table, W2 prompts (operator directive 2026-10-19)`
  (`git merge-base --is-ancestor 5b471e4 HEAD` → exit 0, i.e. ancestor of `ee8ba85`).
  Each of those prompts states verbatim: *"this lane is absent from shokunin.conf LANES"*.
- `.ufo/state/*.round` counters for the three lanes are still at the initial `1`
  (`audio=1 game-dev-2d=1 game-dev-3d=1`), while the eight furthest-advanced lanes read
  10–18: `kumitate=18 kasegi=17 kagi=16 kake=16 kotoba=16 protocol=14 kengaku=13
  aggregator=10`.
- `.ufo/watchdog.log` (tracked) ends at `2026-10-15T01:58:27-03:00 tick=2` (last 12 lines
  checked with `tail -12`) → the tracked log records no local tick after 2026-10-15; this
  is log evidence only (no process probe, §7), and it means conf LANES is a
  *configuration* surface, not evidence of live dispatch.
- `.ufo/state` (worktree and main checkout agree) also **lacks `kotodama` and `souji`**
  even though conf declares them; so state ≠ conf and state ≠ physical. Neither is a roster.

**Conf repo column is consistent with the filesystem:** every LANES row's repo field is
exactly `<id>-shokunin` and every one resolves to an existing dir
(`conf repo col != <id>-shokunin: []`). The mismatch is membership, not paths.

**Conclusion (exact):** 18 of 21 physical lane repos are in the operator conf; the other 3
are excluded by an explicit 2026-10-15 operator commit and remain live only through
wave-generated prompts. 0 conf-declared lanes are missing locally. Manifest roster (13) is a
strict subset of both conf (18) and physical (21): 8 physical repos have MANIFEST `mint`
entries but no roster row (see §3).

## 3. README roster table vs MANIFEST — exact classification of all 16 links

All 16 README links were checked against each lane's actual `origin` (normalized by
stripping a trailing `.git`): **16/16 match** — no dead or wrong repository URL.

| README link | manifest roster row? | physical dir? | remote (actual) |
|---|---|---|---|
| kasegi-shokunin | **yes** | yes | kasegi-shokunin |
| kengaku-shokunin | **yes** | yes | kengaku-shokunin |
| kake-shokunin | **yes** | yes | kake-shokunin |
| kumitate-shokunin | **yes** | yes | kumitate-shokunin |
| kotoba-shokunin | **yes** | yes | kotoba-shokunin |
| kagi-shokunin | **yes** | yes | kagi-shokunin |
| kama-shokunin | **yes** | yes | kama-shokunin |
| kaidoku-shokunin | **yes** | yes | shokunin-reverse-engineering |
| revenger-shokunin | **yes** | yes | shokunin-binary-forensics |
| audio-shokunin | **yes** | yes | shokunin-game-audio |
| game-dev-2d-shokunin | **yes** | yes | shokunin-godot-2d |
| game-dev-3d-shokunin | **yes** | yes | shokunin-3d-engines |
| lore-shokunin | **yes** | yes | shokunin-world-bible |
| mori-shokunin | **no** | yes | mori-shokunin |
| chousa-shokunin | **no** | yes | chousa-shokunin |
| kotodama-shokunin | **no** | yes | kotodama-shokunin |

- **Canonical rows:** 13 of 16 (the table's first 13). **Nonrostered rows:** 3
  (mori, chousa, kotodama). README gives all 16 the rank `shonen`; the 3 nonrostered ones
  have no rank field in `.roster` (their manifest records are ledger entries — mint and round
  rows — not roster rows).
- **Physical lanes with no README row (5):** `mado`, `souji`, `tabi`, `tameshi`, `tsukuroi`.
- **Minted but not rostered (8):** exact command
  `jq -r '[.rounds[]|select(.type=="mint")|.minted[]] as $m | ([.roster[].id]) as $r | $m-$r | .[]' MANIFEST.json`
  → `tameshi mado tsukuroi tabi mori chousa kotodama souji`. (Reverse difference is 12:
  the 2026-09 seeds have no per-lane mint entry; the one shared mint entry `round=11.5`
  carries `minted=[]`.)

So the README's L88 claim *"Every minted shokunin registers a row here"* is false for 5 of
those 8, and its L88 claim *"`MANIFEST.json` is canonical; `ROADMAP.md` mirrors it"* is
contradicted by its own table for 3 rows. Intent is documented, not accidental:
`9ee7059` (2026-10-14T09:51:17) says *"roster rows withheld pending probation"* for
tameshi/mado/tsukuroi/tabi; `7bf2b1a` (2026-10-18, souji) records *"conf lane + MANIFEST
mint entry"* with no roster row; mori/chousa rows were added by `3883dd8`
(2026-10-16), kotodama's by `bc889c5` (2026-10-17) — all three without a MANIFEST roster
row, and none of those commits added one (`.roster|length` = 13 at each of `3883dd8`,
`bc889c5`, and HEAD).

**Related naming errors in the same block:**

- L14 and L46 say a minted shokunin gets its own `shokunin-<domain>` repo; L90–91 asserts a
  calendar rule: *"2026-09 remotes keep that shape … 2026-10 remotes use
  `shokunin-<domain>`"*. Measured remote shapes: **14 `<id>-shokunin` / 7
  `shokunin-<domain>`**. The calendar rule fails for 7 lanes whose manifest mint date is
  2026-10 and whose remote is `<id>-shokunin`: tameshi, mado, tsukuroi, tabi, mori, chousa
  (mint 2026-10-14) and kotodama (mint 2026-10-17). Among 2026-10 mints it holds only for
  the 2026-10-11
  (audio, game-dev-2d, game-dev-3d, lore, revenger), 2026-10-13 (kaidoku) and 2026-10-18
  (souji) mints.
- `MANIFEST.json` `.roster[].repo` holds the **remote** name, not the canonical lane name:
  six rows carry `shokunin-*` (`shokunin-game-audio`, `shokunin-godot-2d`,
  `shokunin-3d-engines`, `shokunin-world-bible`, `shokunin-binary-forensics`,
  `shokunin-reverse-engineering`). Any wording of the form "canonical names are
  `<id>-shokunin`" must say it describes the local checkout/lane id; `.repo` is the remote.

## 4. Files statement vs actual tree

Listed in README L119–125: `PROTOCOL.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md`,
`MISSION.md`, `PROTOCOL-APPENDIX.md`, `MANIFEST.json`, `ROADMAP.md`, `shokunin.conf`,
`scripts/`, `.ufo/` (+ `.ufo` `waves/`, `reports/`, `prompts/`, `l0-questions.md`).
**Every listed path exists** (`ls -1` at HEAD). Tracked root entries **not** mentioned:
`README.md`, `LOG.md`, `SCORECARD.md`, `research/`, `templates/`, `.gitignore`; plus
`.ufo/state/`, `.ufo/gates/`, `.ufo/scopes/`, `.ufo/round-44/`, `.ufo/history-pin.json`,
`.ufo/lane-watch.sh`, `.ufo/watchdog.log`. `scripts/` is not just "the round driver" at
HEAD: it contains `shokunin-watchdog.sh`, `sources-census.sh`, and `fixtures/`.
So L117–125 reads as a file inventory but is a partial one; either label it "selected" or
complete it.

**Protocol authority / vendoring (the substantive Files defect).** README L119–121 says the
six protocol files are *"canonical protocol, vendored from kimi-shokunin (upstream)"* —
canonical and vendored are competing authorities in one sentence, and no upstream revision
is pinned anywhere in the repo. Exact check:
`grep -rn -iE "bc7d690|kimi-shokunin|re-vendored" PROTOCOL.md AXES.md LEARNING.md CORPUS.md MISSION.md PROTOCOL-APPENDIX.md`
→ no match, exit 1 (the `pin` occurrences inside `PROTOCOL.md` are the history/drift pins,
L214–215, L322–325, L370–372, not an upstream pin). Measured:

```
upstream = /home/vgpnk/Projects/kimi-shokunin  (git HEAD bc7d690 2026-10-13T16:57:15-03:00)
for f in PROTOCOL AXES LEARNING CORPUS MISSION PROTOCOL-APPENDIX; do
  diff upstream/skills/shokunin/protocol/$f.md  worktree/$f.md | wc -l; done
  -> PROTOCOL.md 55 | AXES.md 67 | LEARNING.md 37 | CORPUS.md 118 | MISSION.md 13 | PROTOCOL-APPENDIX.md 8
git -C upstream diff --stat 812f1da bc7d690 -- skills/shokunin/protocol/
  -> (empty: upstream protocol bundle unchanged between 812f1da and bc7d690)
```

- Upstream HEAD `bc7d690` is a revert of the `§Craft-hours` commit `ee1e5d6`; neither the
  fleet copies nor upstream contain `craft-hours`/`HOURS.md`, so the fleet copies descend
  from the upstream pre-`ee1e5d6` bundle (last upstream change `812f1da`, 2026-10-13T12:05:28,
  same timestamp as fleet-root init `e0b4d9b`).
- All six fleet copies differ from that upstream bundle (by 8–118 diff lines), and the
  fleet's own `PROTOCOL.md` L9–16 declares the rules substrate-neutral with host notes in
  the appendix. `MANIFEST.json.protocol` = `PROTOCOL.md`, `.repo` = `shokunin`.
- The vendoring event is committed as `e867f78` (2026-10-13T16:47:03, "protocol re-vendored
  from kimi-shokunin"), i.e. vendoring happened **before** upstream's add/revert pair and
  no pin records which upstream revision was taken.

Verdict: the fleet-root copies *are* the authority of record here; "vendored" describes
lineage only, and without a pin it cannot identify a baseline. §5 gives replacement text.

## 5. Safe wording (exact, paste-ready)

**(a) Files — protocol authority (replaces L119–121):**

> `PROTOCOL.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md`, and `MISSION.md` are the fleet-root
> contracts; `PROTOCOL.md` and `PROTOCOL-APPENDIX.md` are a required pair (the appendix is
> the fleet's incident digest, not a second protocol). The fleet-root copies are the
> authority of record for this repository. They descend from the upstream
> [kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) protocol bundle, re-vendored at
> `e867f78` (2026-10-13) and adapted here since; no upstream revision pin is recorded, so
> any upstream mirror is reference-only.

(The "required pair" wording is supported by `PROTOCOL.md:210`: *"REQUIRED sibling
`PROTOCOL-APPENDIX.md`"*.)

**(b) Files — round count (replaces L122 parenthetical):**

> `MANIFEST.json` — canonical operator-controlled roster + append-only round ledger (count
> entries at the revision you cite; do not restate a fixed total).

If a number is wanted at all it must be revision-bound, e.g. *"314 ledger entries at
`ee8ba85` (`jq '.rounds|length'`)"* — and even that is a point-in-time observation.

**(c) Roster preamble (replaces L88–91):**

> `MANIFEST.json` is the canonical **operator-controlled roster**; `ROADMAP.md` mirrors its
> roster set. A physical `<id>-shokunin` checkout or a `shokunin.conf` LANES row does not by
> itself confer roster membership. Local lane checkouts and canonical lane ids use
> `<id>-shokunin`; GitHub remotes use either `<id>-shokunin` or `shokunin-<domain>`. The
> table marks each linked repository as rostered or link-only; unlinked local lanes are
> listed below it.

**(d) Intro registration sentence (replaces L13–15):**

> Roster membership lives in `MANIFEST.json` and is reflected below; each specialist lives
> in its own repository. A repository link that is not a manifest row is a link, not a
> registered mint.

**(e) Lifecycle probation sentence (replaces L46 clause):**

> … its own `shokunin-*` repository at mint, and — after probation, on an operator roster
> edit — a row in `MANIFEST.json` (rows are withheld until then).

**(f) Table: add a status column** (`rostered — shonen` for the 13, `link only — not in
MANIFEST` for mori/chousa/kotodama) and a line naming the five unlinked local lanes
(`mado`, `souji`, `tabi`, `tameshi`, `tsukuroi`). If the 3 link-only rows should instead be
registered, the fix is in `MANIFEST.json`, not the README.

## 6. Findings by severity

**HIGH**

1. README L93–110 presents 16 rows under "Roster" with rank `shonen`; only 13 are manifest
   rows. mori/chousa/kotodama are nonrostered (evidence §1, §3). Any reader treating the
   table as the registry overcounts the roster by 3.
2. README L88 claims *"Every minted shokunin registers a row here"*; 5 minted lanes have no
   row (mado, souji, tabi, tameshi, tsukuroi; evidence: §3 jq output + `9ee7059` /
   `7bf2b1a` messages). The claim and the withholding practice cannot both stand.
3. README L119–121 calls the protocol bundle "canonical … vendored from upstream" with no
   pin; the copies differ from upstream in all six files and the fleet root is the only
   source that binds them (`MANIFEST.protocol`, `PROTOCOL.md:210`). A reader cannot tell
   which copy governs (§4).

**MEDIUM**

4. README L122 hardcodes "79 rounds". 79 was exact only at `e867f78` (`git show
   e867f78:MANIFEST.json | jq '.rounds|length'` → 79); it was already stale at the README's
   own last edit `bc889c5` (→ 179) and is 314 at HEAD, with max `.round` 108 and 81 distinct
   round values. No reading of "round" yields 79 today.
5. README L14/L46/L90–91's `<id>-shokunin` vs `shokunin-<domain>` calendar rule fails for
   7/21 lanes (all 2026-10-14 and 2026-10-17 mints), and L14's "roster row →
   `shokunin-<domain>` link" pattern is false for 10/16 existing links (§3).

**LOW**

6. Files block is a partial inventory presented as a list: `LOG.md`, `SCORECARD.md`,
   `research/`, `templates/` and `.ufo/{state,gates,scopes,round-44,history-pin.json,
   lane-watch.sh,watchdog.log}` are unmentioned; `scripts/` also holds `sources-census.sh`
   and `fixtures/` (§4).
7. The 2026-10-16 mori/chousa aside (L112–114) documents the two repos as "created and
   pushed after their 10-round in-session craft runs — rounds 2–11 admitted on both lanes".
   Ledger check (`jq` over `.rounds`): chousa has 9 lane-scoped `craft` entries (rounds
   15–23) plus one `closure` (round 24), with `lane_rounds.chousa` values
   `[1…14, 24]` (no 15–23 there); mori's `lane_rounds.mori` values are `[1…12]`, and its
   only lane-scoped entry is round 12, `type=closure`, `lane_round: 12`,
   `lane_rounds: {mori: 12}`, with `capabilities_added` — not `type=craft`. So "10-round"
   and "rounds 2–11 admitted" are not reproducible from the ledger fields as written for
   either lane (chousa's craft rows are numbered 15–23; mori has one closure row at lane
   round 12); keep the sentence revision-bound or drop the counts (it is also stale
   relative to round 12's mori closure).

**INFO / adjacent (not this seat's write scope)**

8. `ROADMAP.md:90` still lists `kama` under "Candidate domains (watchlist)" with "mint
   decision pending" while `ROADMAP.md:13` lists kama as a rostered shonen and
   `MANIFEST.roster` contains it. The README's "ROADMAP mirrors it" claim therefore also
   papers over a contradiction inside ROADMAP; the ROADMAP round-10 narrative is likewise
   superseded.
9. Main-checkout `README.md` (dirty, §0) already carries corrected wording close to §5(a)
   and §5(b), including "shokunin.conf — driver routing, not roster authority" and
   "repository link only — not in MANIFEST". Two defects remain in that draft:
   (i) it cites *"the report's inventory command and result are recorded in
   `.ufo/reports/round-12/aggregator.md`"* — **that file has never existed** (`ls` absent in
   main and in the fleet-aggregate/fleet-ledger/fleet-protocol worktrees;
   `git log --all -- .ufo/reports/round-12/aggregator.md` → empty; round-12 dir holds only
   lane reports); and
   (ii) its "13 entries … 21 physical directories" numbers need a revision-bound citation
   since both counts are set arithmetic, not prose facts.
10. Workspace artifact unrelated to this audit: `/home/vgpnk/Projects/shokunin/bash: `
    exists as a directory (name literally `bash: `), does not end in `-shokunin`, and does
    not affect the 21-lane count.

## 7. Verification gaps / limits (declared)

- **No network check.** The README's "(private)/(public)" remote-visibility parenthetical
  was not verified (no `gh`, no API call); only local `origin` URLs were compared.
- **Main checkout draft is someone else's uncommitted work.** I read it; I did not stage,
  edit, or rely on it as evidence for the worktree audit. Whether it becomes the integrated
  text is the parent's call.
- **Driver liveness inferred, not probed.** Evidence is the `.ufo/watchdog.log` tail
  (`tick=2` at 2026-10-15T01:58:27) plus prompt commits; no process/`systemctl`/`proc`
  inspection was run, and `.ufo/state` is tracked/rewritten state (stale by construction per
  ROADMAP's operator-debt item).
- **No gate, build, test, or lint was run** (contract forbids them here); the round-9 corpus
  gate's r2/r4/r7/r8-literal/r10/SHONEN-form checks are not evidence about any README claim.
- **Census totals deliberately withheld.** No source-row count is claimed; the indented-row
  parser fix is in progress elsewhere, so all lane source figures remain provisional until
  the parent's `FINAL LANES READY`.
- **Round-ledger numbers are point-in-time**: 314/313/108/81/100/214 at `ee8ba85` only; the
  worktree and main differ (312 on `dcf3b64`).
- **No repo was mutated:** all 21 lane repos were read with `git remote get-url` /
  `git rev-parse` / `git log`; the only file written by this seat is this note.
