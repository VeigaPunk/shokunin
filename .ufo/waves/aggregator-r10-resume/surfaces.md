# Aggregator round 10 (resume) — lane surfaces reconnaissance

**Seat:** R10Surface (scout). **Write scope:** this file only. **Mode:** read-only over the fleet.
**Stamps.** `CUTOFF 2026-10-15T04:55:22Z` = `2026-10-15T01:55:22-03:00` (`date -u +%FT%TZ`, epoch `1792040122`).
Fleet-root HEAD at cutoff `f2df270` (`git log -1` → `f2df270 2026-10-15T01:55:17-03:00 w21 spec: …`); HEAD when this
seat opened its first measurement `99efc52` (`2026-10-15T01:52:09-03:00 ops: exclude the three Devin-owned lanes
(18 remain)`); inherited baseline `.ufo/waves/aggregator-r10/before.json` `measured_commit`
`b598ce0e1d4fa8851d3e238ee6afde42bd57f787`, gate `sha256 68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8`.

**Discipline.** Metadata, IDs, counts, pathnames and rule/pointer names only. No corpus bytes, no credential
material, no finding snippets, no session material. Every figure below is a pasted command result; where a
command cannot decide, the cell says `not-evaluable` instead of guessing.

---

## 1. Physical lane surfaces (19)

Set identity — `find . -maxdepth 1 -type d -regextype posix-extended -regex '\./[a-z0-9][a-z0-9-]*-shokunin' -printf '%f\n' | sort`
→ **19 names**; root-level symlinks → 0 (`find . -maxdepth 1 -type l` empty). Root `.gitignore` carries a
`*-shokunin/` rule, so these 19 are untracked in the fleet tree and each contributes its **own** git revision.

| lane dir | HEAD (short) | dirty paths | corpus files | knowledge/*.md | lessons/*.md | corpus/README.md | corpus/QUALITY.md | corpus/lessons/ | SHONEN.md | max `round-N-aggregator-*` |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| audio-shokunin | d9aa6f9 | 467 | 123941 | 14 | 0 | **absent** | **absent** | **absent** | yes | none |
| chousa-shokunin | 34774a1 | 2 | 4 | 0 | 0 | yes | yes | empty (`.gitkeep`) | yes | none |
| game-dev-2d-shokunin | 884a4c4 | 79 | 692385 | 2 | 66 | yes | **absent** | yes | yes | none |
| game-dev-3d-shokunin | db64943 | 4 | 89751 | 3 | 90 | yes | **absent** | yes | yes | none |
| kagi-shokunin | 15ea78c | 3 | 63 | 21 | 26 | yes | **absent** | yes | yes | 9 |
| kaidoku-shokunin | 6645585 | 1 | 80 | 72 | 4 | yes | yes | yes | yes | none |
| kake-shokunin | 20d1311 | 1 | 41 | 17 | 21 | yes | **absent** | yes | yes | 9 |
| kama-shokunin | c390918 | 2 | 16 | 8 | 7 | yes | **absent** | yes | yes | none |
| kasegi-shokunin | 4b2e302 | 2 | 55 | 25 | 22 | yes | **absent** | yes | yes | 9 |
| kengaku-shokunin | 3f31e54 | 3 | 184 | 23 | 19 | yes | **absent** | yes | yes | 9 |
| kotoba-shokunin | 581e293 | 1 | 48 | 29 | 18 | yes | **absent** | yes | yes | 9 |
| kumitate-shokunin | 6b982ab | 3 | 75 | 38 | 36 | yes | **absent** | yes | yes | 9 |
| lore-shokunin | 5eb9451 | 5 | 1532 | 6 | 0 | yes | **absent** | **absent** | yes | none |
| mado-shokunin | bb08dd5 | 3 | 25 | 22 | 1 | yes | yes | yes | yes | none |
| mori-shokunin | 0715198 | 2 | 8 | 1 | 0 | yes | yes | empty (`.gitkeep`) | yes | none |
| revenger-shokunin | 286033c | 2 | 457 | 2 | 1 | **absent** | **absent** | yes | yes | none |
| tabi-shokunin | c24eaea | 1 | 1830 | 23 | 10 | yes | yes | yes | yes | none |
| tameshi-shokunin | 284ab0f | 2 | 22 | 19 | 1 | yes | yes | yes | yes | none |
| tsukuroi-shokunin | 0ecf3ff | 3 | 27 | 24 | 0 | yes | yes | empty (empty) | yes | none |

Commands: `git -C <dir> rev-parse --short HEAD`; `git -C <dir> status --porcelain | wc -l`;
`find <dir>/corpus -type f | wc -l`; `ls <dir>/corpus/knowledge/*.md | wc -l`; `ls <dir>/corpus/lessons/*.md | wc -l`;
`test -f <dir>/corpus/{README,QUALITY}.md`; `test -d <dir>/corpus/lessons`;
`ls <dir>/corpus/lessons/ | grep -oE '^round-[0-9]+-aggregator'`.
Caveats: file counts are **live-worktree** counts taken at the cutoff, not revision counts; `dirty` was re-read
twice (01:53 → 01:55) and moved for three lanes (audio 466→467, game-dev-2d 78→79, kumitate 2→3) — the table keeps
the later pass. Three lanes are custody-restricted (§7) and were read only.

---

## 2. Inherited nineteen-dir list vs current `shokunin.conf` (text only)

Read as text; nothing was sourced. Commands: the §1 `find`; `diff shokunin.conf shokunin.conf.full-roster-20261015`;
`grep -cE '\|[a-z0-9-]+-shokunin\|' shokunin.conf`; `git show 7d02e96:shokunin.conf | grep -cE '…'`.

| Set | Count | Members vs the 19 physical dirs |
|---|---:|---|
| inherited `before.json.direct_child_lanes` (b598ce0) | 19 | sorted list is **identical** to the current 19 physical dirs |
| current `shokunin.conf` `LANES`, child lines | 16 | 19 physical − {`audio`, `game-dev-2d`, `game-dev-3d`} |
| current `shokunin.conf` `LANES`, root lines | 2 | `protocol|.`, `aggregator|.` → configured fleet = **18** |
| configured-but-missing child dirs | **0** | every conf-configured child repo directory exists |
| physical-but-unconfigured child dirs | **3** | `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` |

Revision evidence for the delta: `git show 7d02e96:shokunin.conf` has **19** child lane lines, including `audio|`,
`game-dev-2d|`, `game-dev-3d|`; HEAD-previous commit `99efc52` subject reads *"ops: exclude the three Devin-owned
lanes (18 remain); add the wall lane-watch view"*; `LOG.md:701-708` states the same three were removed from
`LANES` and their lane processes killed. No code or config was consulted beyond these bytes.

**Boundary (recorded as a boundary, not as a mint/dormancy or code-filter result).** 19 physical ≠ 18 configured.
Operator custody update (`CONTEXT.md` §Operator custody update, appending `LOG.md:701-708`): the three excluded repos
are Devin-owned and hold unrelated in-flight work; they stay physical corpus-discovery members and read-only for this
wave; only the other 16 children receive mirrored lessons. The selection surface must therefore cover all **19**
physical corpora while collector metadata must **not** equate the local discovery set with the configured fleet.

**Filename discrepancy (metadata only).** `shokunin.conf` and `shokunin.conf.full-roster-20261015` are
**byte-identical** (`diff` → no output; both 3859 B; same mtime second `01:50:47`; both tracked; both last changed
by `99efc52`). The `full-roster` name therefore does not currently hold a pre-exclusion 21-lane roster. Recorded as a
boundary question; no lifecycle decision is made here.

---

## 3. Missing QUALITY / index / lesson structures (by metadata)

| Missing structure | Count | Lanes |
|---|---:|---|
| `corpus/README.md` (index) absent while `corpus/` exists | 2 | `audio-shokunin` (123 941 corpus files), `revenger-shokunin` (457) |
| `corpus/QUALITY.md` absent (`CORPUS.md` layout item) | **12** | audio, game-dev-2d, game-dev-3d, kagi, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, revenger |
| `corpus/lessons/` directory absent | 2 | `audio-shokunin`, `lore-shokunin` |
| `corpus/lessons/` present with **zero** `*.md` | 3 | `chousa-shokunin` (`.gitkeep`), `mori-shokunin` (`.gitkeep`), `tsukuroi-shokunin` (empty dir) |
| lanes carrying a `round-9-aggregator-*` lesson | 6 | kagi, kake, kasegi, kengaku, kotoba, kumitate |
| lanes carrying a **`round-10-aggregator-*`** lesson | **0 / 19** | — |

The last row is the gate-side fact: `ls <lane>/corpus/lessons/round-10-aggregator-*.md | wc -l` → 0 for all 19, so the
committed `corpus-gate` r10 check at `--round 10` would fire per lane at this revision. Whether the parent's per-repo
lesson duty satisfies it is the parent's call; this seat records presence only.

Index-row accuracy (`r7` phantom rows) and count-claim conformance (`r4`) are **not-evaluated** here: they need the
index and entry text, and this file carries no corpus content.

---

## 4. Mint census — `MANIFEST.json` `type == "mint"`

Commands: `python3 -c "import json;m=json.load(open('MANIFEST.json'));…"` (census forms below), roster/round counts
from the same object. Result: `roster 13`, `rounds 142`.

`by_type`: `train 53 | closure-correction 50 | closure 15 | mint 8 | retroactive-closure 7 | ops 3 | work 2 |
train+audit 2 | scaffold 1 | train+audit+unlock 1`.

`type == "mint"` → **8 rows**:

| round | date | `minted[]` |
|---|---|---|
| 11.5 | 2026-09-28 | `[]` (probation-shaped: roster row withheld; lane named in `notes` = kama) |
| 0 | 2026-10-13 | `["kaidoku"]` |
| 0 | 2026-10-14 | `["tameshi"]` |
| 0 | 2026-10-14 | `["mado"]` |
| 0 | 2026-10-14 | `["tsukuroi"]` |
| 0 | 2026-10-14 | `["tabi"]` |
| 0 | 2026-10-14 | `["mori"]` |
| 0 | 2026-10-14 | `["chousa"]` |

Distinct minted lane ids across `type=="mint"` rows (array or probation note): kama, kaidoku, tameshi, mado,
tsukuroi, tabi, mori, chousa = **8**. Roster (13 rows, all `rank: shonen`): kasegi, kengaku, kake, kumitate, kotoba,
kagi, kama, audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku — i.e. six of the eight minted ids
(chousa, mori, tameshi, mado, tsukuroi, tabi) have **no** roster row, and five rostered ids
(audio, game-dev-2d, game-dev-3d, lore, revenger) appear in **no** `type=="mint"` row reachable by this census.

**Instrument note.** `sum(1 for x in rounds if x.get('minted'))` → **8** at this revision: seven `mint` rows plus one
`ops` row (2026-10-14) whose `minted` array also names mori and chousa. The round-11 ledger's finding that the field
is empty in every revision (§r11 `mint-table` §1.5) does **not** hold at the current revision; whether it held when
written is **not-evaluable** here (only the current revision was measured — no history walk was performed).

**Historical reconciliation (literal, no inference).** `SCORECARD.md:278` records the round-11 census as *"the first
mint is counted by `type=="mint"` (1, kama)"*. The current revision yields 8, and 6 of the 7 newer rows are dated the
same calendar day (`2026-10-14`) as that record, so the delta **cannot be ordered by date alone** ⇒ the *timeline*
is not-evaluable; only the current count (8) is asserted. No mint, promotion or roster decision is made here.

---

## 5. Newest dispatched-and-reported pairs per repo `LOG.md` grammar

Rule pointer (`PROTOCOL.md:55`, lifecycle): two consecutive **dispatched-and-reported** rounds with no `LOG.md`
activity flag a shonen **dormant** *as a review trigger* by the integrator; undispatched rounds do not count.
Inherited operationalisation (`.ufo/waves/aggregator-r11/seats/dormancy-table.md` §1): failed markers are excluded
from the pair, `ok`-graded defective reports count, and the pair is the two most recent rounds that were **both**
dispatched and reported. **Corpus omissions are not dormancy evidence** under any reading (§7).

### 5.1 Per-repo LOG grammar (matched form differs per repo — the mandated heading form is not universal)

Matchers, anchored at line start: bullet `^- [0-9]{4}-[0-9]{2}-[0-9]{2} . round ([0-9]+)`; heading
`^#{2,3} [Rr]ound ([0-9]+)`. (The `r11` §5 census already found the case-sensitive heading form host-broken for most
lanes; the counts below reproduce that finding at this revision.)

| lane | form that matches | entries | max round | round on last matching line |
|---|---|---:|---:|---:|
| audio | heading | 279 | 77 | 77 |
| chousa | bullet | 1 | 0 | 0 |
| game-dev-2d | heading | 126 | 78 | 78 |
| game-dev-3d | heading | 87 | 87 | 87 |
| kagi | bullet | 20 | 18 | 18 |
| kaidoku | bullet | 14 | 14 | 14 |
| kake | bullet | 18 | 18 | 18 |
| kama | **mixed** | 1 bullet + 3 heading | 0 / 3 | 0 / 3 |
| kasegi | bullet | 18 | 19 | 19 |
| kengaku | bullet | 20 | 15 | 15 |
| kotoba | **mixed** | 8 bullet + 12 heading | 9 / 18 | 9 / 16 |
| kumitate | **mixed** | 33 bullet + 1 heading | 31 / 32 | 18 / 32 |
| lore | heading | 349 | 85 | 85 |
| mado | bullet | 13 | 11 | 11 |
| mori | **mixed** | 1 bullet + 1 heading | 0 / 1 | 0 / 1 |
| revenger | heading | 119 | 60 | 60 |
| tabi | bullet | 12 | 11 | 11 |
| tameshi | bullet | 12 | 11 | 11 |
| tsukuroi | bullet | 12 | 11 | 11 |

Two grammar traps reproduced: **mixed-form** repos (kama, kotoba, kumitate, mori) need both matchers, and kumitate's
max bullet round (31) differs from the round on its last bullet line (18) — its `LOG.md` is not in round order, so
"last line" and "max round" are different cells.

### 5.2 Dispatched-and-reported input per lane

Commands: `.ufo/state/<lane>.round`; `grep -E ' <lane> round=' .ufo/watchdog.log | tail -1`;
`ls .ufo/reports/round-*/<lane>.md` (sorted); `wc -c`; the §5.1 matchers over `<lane>-shokunin/LOG.md`.

| lane | counter | latest launch (round @ ts, −03:00) | reports in tree | newest report round (bytes) | newest pair | pair rounds present in `LOG.md`? | literal evidence |
|---|---:|---|---:|---|---|---|---|
| audio | 1 | r1 @ 01:45:42 | 13 | r76 (2946 B) | [75, 76] | yes, yes | no silence |
| chousa | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 dispatched-and-reported rounds) |
| game-dev-2d | 1 | r1 @ 01:45:42 | 15 | r77 (668 B) | [76, 77] | yes, yes | no silence |
| game-dev-3d | 1 | r1 @ 01:45:42 | 13 | r85 (736 B) | [84, 85] | yes, yes | no silence |
| kagi | 16 | r16 @ 01:50:57 | 17 | r19 (3164 B) | [17, 19] | yes, **no** | newest pair round r19 absent from `LOG.md` |
| kaidoku | 1 | r1 @ 01:50:57 | 4 | r4 (3080 B) | [3, 4] | yes, **no** | newest pair round r4 absent |
| kake | 16 | r16 @ 01:50:57 | 16 | r19 (3211 B) | [17, 19] | yes, **no** | newest pair round r19 absent |
| kama | 1 | r1 @ 01:50:57 | 3 | r4 (3074 B) | [2, 4] | yes, **no** | newest pair round r4 absent |
| kasegi | 17 | r17 @ 01:50:57 | 18 | r20 (3131 B) | [18, 20] | yes, **no** | newest pair round r20 absent |
| kengaku | 13 | r13 @ 01:50:57 | 13 | r16 (2979 B) | [14, 16] | yes, **no** | newest pair round r16 absent |
| kotoba | 16 | r16 @ 01:50:57 | 17 | r19 (3166 B) | [17, 19] | yes, **no** | newest pair round r19 absent (heading max 18, bullet max 9) |
| kumitate | 18 | r18 @ 01:50:57 | 17 | r32 (2256 B) | [17, 32] | yes, yes | no silence |
| lore | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |
| mado | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |
| mori | 2 | r2 @ 01:50:57 | **1** | r1 (2189 B) | [1] | yes | **not-evaluable** (1 round ⇒ no pair) |
| revenger | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |
| tabi | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |
| tameshi | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |
| tsukuroi | 1 | r1 @ 01:50:57 | **0** | — | — | — | **not-evaluable** (0 rounds) |

**Dormancy verdict: none asserted.** No lane is called dormant, active-by-merit or retired here — the literal
evidence is only *"pair round present/absent in `LOG.md`"* plus the insufficiency counts above. Two further
ambiguities are recorded rather than resolved:

1. **Report-round space ≠ counter space.** Seven lanes' newest report round is far above their dispatched counter
   (audio 76 vs 1; game-dev-2d 77 vs 1; game-dev-3d 85 vs 1; kumitate 32 vs 18; kasegi 20 vs 17; kagi 19 vs 16;
   kotoba 19 vs 16) and five lanes carry report rounds ≥ 73 while the driver counter stands at 1. Root
   `.ufo/reports/` spans 43 round directories from older programs, so *which* report round belongs to the lane's
   current round cannot be decided from metadata ⇒ the pair input itself is ambiguous for those lanes.
2. **Counter round absent from `LOG.md`** for three lanes (chousa counter 1 vs LOG bullet round 0; kengaku counter
   13 vs bullet max 15; mori counter 2 vs LOG rounds 0/1) — another place where round numbers are not tree-wide
   comparable.
3. **No pair report falls in the sub-400 B marker class** (`wc -c`: the smallest pair report is game-dev-2d r77 at
   668 B; the newest pair reports run 668–3211 B). Hex-token counts / in-repo-resolvable counts for the newest pair
   report, from `grep -oE '\b[0-9a-f]{7,40}\b'` followed by `git -C <repo> cat-file -t <token>`: audio r76 6/3,
   game-dev-2d r77 3/3, game-dev-3d r85 3/3, kagi r19 2/1, kaidoku r4 0/0, kake r19 2/1, kama r4 2/1,
   kasegi r20 2/1, kengaku r16 2/1, kotoba r19 2/1, kumitate r32 2/1, mori r1 2/1 — i.e. whether "a resolvable
   commit" is satisfied (and therefore whether a report grades `ok+defect` or a failed marker, which changes the
   pair) is a ruling on the same boundary `r11` §3/§4 left open, not a measurement. Left as-is; no lane is called
   dormant or active on the strength of it.

### 5.3 Driver's own launch-tick grading (literal log counts, not this seat's verdict)

Over `.ufo/watchdog.log` lines ≥ 340: **16 `lane-round-failed`** (aggregator 2, kagi 2, kama 2, kasegi 2, kengaku 2,
kotoba 2, protocol 2, kaidoku 1, kake 1 — each reading `marker/contentless report; NOT advancing`),
**7 `lane-dead-no-report`** (chousa, lore, mado, revenger, tabi, tameshi, tsukuroi), **3 `complete`** (kumitate ×2,
mori ×1). 16 + 7 + 3 = 26 events across the 18 configured lanes.

---

## 6. Latest-launch staleness — “> two ticks (900 s)” standing duty

**Result: none.** At `CUTOFF 2026-10-15T04:55:22Z` no lane's latest launch is older than 900 s.

Launch-wave digest (`awk 'NR>=307' .ufo/watchdog.log | grep -E 'launch .* round=' | awk '{print $1}' | sort | uniq -c`):
`5 @ 2026-10-15T01:44:22-03:00 | 6 @ 01:45:00 | 21 @ 01:45:42 | 18 @ 01:50:57` (the 21-lane stamp predates the
Devin-lane exclusion; the 18-lane stamp is the current configured fleet + 2 root lanes).

Latest launch **per lane** (last launch line wins): the 18 configured lanes and both root lanes → `01:50:57-03:00`
= **age 265 s**; `audio`, `game-dev-2d`, `game-dev-3d` → `01:45:42-03:00` = **age 582 s** (they were not relaunched
after exclusion). Oldest age in the fleet = 582 s < 900 s, so the >900 s condition has **no member**; if a threshold
report is wanted anyway it is `0 / 21`.

Supporting progress evidence (metadata, not a dormancy claim):
`newest-file mtime age` 0–379 s (kake 379 s max; tabi 0 s) and `last non-aggregator commit age` 13 451–118 235 s
(`git -C <repo> log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%at'`).
Launch pids for the 18 configured lanes are **alive** in `/proc` (all executing the fleet watchdog script); the
excluded lanes' launch pids (`2651133`, `2651120`, `2651667`) are **dead**, matching `LOG.md:701-708` ("lane
processes were killed"). Two of the three excluded lanes nevertheless show sub-10 s write activity inside their
trees (`audio` 8 s, `game-dev-2d` 9 s, `game-dev-3d` 2 s) from the Devin-owned work this wave must not touch ⇒
classified **progressing-weak (external writer, not fleet-authored)**, recorded as evidence only.
Parent note confirmed: no child lessons exist yet, so no parent-authored mtime contamination reaches the child repos
at this cutoff.

---

## 7. Unknown surfaces scoped (no inference, no lifecycle decision)

- **Corpus completeness is unknown** for 12 lanes (no `corpus/QUALITY.md`), for 2 lanes whose `corpus/` has no index
  (`audio` 123 941 files, `revenger` 457 files — the largest unknowns), and for 5 lanes with no lessons content
  (audio, lore by absent dir; chousa, mori, tsukuroi by empty dir).
- **Dormancy is essentially unmeasured**: 7 of 19 lanes have zero reports in `.ufo/reports/`, one has one report,
  and for the remaining 11 the pair rounds are not comparable to their counters (§5.2).
- **Not established here:** full `CORPUS.md` conformance; configured-but-missing dirs beyond a name-level check;
  atomic live-tree snapshots; index-row (`r7`) and count-claim (`r4`) accuracy; whether the `full-roster` file
  should have retained the excluded lanes (§2).
- **Custody boundary is load-bearing for the round's other surfaces.** 19 physical corpora ⊃ 18 configured lanes;
  `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` are Devin-owned, read-only for this wave, and
  must not receive mirrored lessons, commits or pushes; collector metadata must keep "local discovery set" distinct
  from "configured fleet" (`CONTEXT.md` §Operator custody update; `LOG.md:701-708`).
- **No mint, promotion, dormancy or retirement decision is made in this file**, and no positive dormancy case was
  manufactured from corpus omissions or from the 582 s launch window.