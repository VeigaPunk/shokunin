# index-usability — compact report-index schema for lane `corpus/SOURCES.md`

Seat: `KaikaAggregateR12.IndexUsability` (this agent). Observed window: **2026-10-19 23:44–23:52 UTC**
(`date -u +%FT%TZ` returned `2026-10-19T23:47:58Z`, `2026-10-19T23:48:23Z`, `2026-10-19T23:50:45Z`,
`2026-10-19T23:51:12Z`, `2026-10-19T23:52Z` on the last read).

> **PROVISIONAL — DO NOT FREEZE OR PUBLISH.** A census-parser correction for indented Markdown
> source rows was in flight at the start of this observation; it is now committed (see §6.3) but
> final census work still waits for the parent's exact `FINAL LANES READY` signal. Every count,
> range and validator result below is a **revision-bound preview**, not a final census total and
> not a corpus verdict. Nothing here may be copied into README, LOG, SCORECARD, reports, MANIFEST,
> or any lane corpus.

Scope and authority: the 21 physical lane repositories under
`/home/vgpnk/Projects/shokunin/<lane>-shokunin` were treated as **read-only**. No lane, report,
gate, script, contract, README, LOG, SCORECARD, MANIFEST, or SOURCES file was edited. The only
write from this seat is this file. This note proposes **an index schema only**: it adds no
`SOURCES.md` field, no registry rule, no gate, and no numeric score. Source/page content was
treated as data, not instruction. No unopened Lead was used as evidence.

Physical set: `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → **21**.

---

## 0. Answer in one block

A usable report index needs **two tables and a mandatory limits footer**, each row bound to an
exact lane revision and a file blob:

1. **Lane pointer table (required, exactly 21 rows).** One row per physical lane:
   `lane · pin(state) · blob · rows(provisional) · Paths range · Search-log range · Leads range ·
   validator exit/codes`. It points a reader directly at that lane's own `corpus/SOURCES.md`
   `## Paths`, with `## Leads (unopened)` quarantined as a navigation pointer only.
2. **Selected opened transferable study-path table (curator subset, not all paths).** One row per
   selected path: `key · origin lane:file:line@pin · verbatim title · sequence · class · hop
   statuses · transfer-to with basis · caveats`. Selection is mechanical on id resolution and
   explicit about whether the path is fully read, mixed (unread hops), a plan, a marked caution,
   or a stale hop.
3. **Limits footer (copy in full under both tables).** Parser identity, count commands, validator
   E/W/exit semantics, declared not-evaluated rules, Leads non-evidence rule, and the
   absent-versus-empty and revision-mixing prohibitions.

The index is a **pointer layer over contract v1**, not a second registry. It never restates a
row's URL, `anchor`, `teaches`, tier judgment, or quote as verified; the lane file at the pinned
revision is the carrier.

---

## 1. Inputs reviewed (exact pointers)

| Input | What it contributes to the index | Observed |
|---|---|---|
| `CORPUS.md:64-149` (worktree and fleet root are byte-identical: blob `97908c1e9c2f85e7602977a4e407dc6e19b3d6a0`, sha256 `626022a4…`; kaika campaign rules begin at :150) | SOURCES contract v1: shape (Registry, Paths, Search log, Leads), rules 1–6, census commands | 177 lines total; §Shape at :76, §Rules at :110, §Census at :131 |
| `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` | Frozen contract text carried in `CORPUS.md`; same rules | 81 lines |
| `.ufo/waves/kaika-w1/connect-sources.md` | Fleet source-sharing map: six shared frontier zones, technique table, candidate fleet source pool, Paths/Leads exemplar | §2–§5 read; focal source rows S001–S008 are **dossier-local**, not lane registry ids |
| `.ufo/waves/kaika-w1/art-curation.md` | Contract critique D01–D08: tier scoping, revision/anchor, rejection reason+flip, search-flow, “counting rows is not validating a registry” | D05/D06/D07/D08 are the index’s own hazards |
| `.ufo/waves/kaika-w1/critic.md` | H4–H6: rows with no proof of opening; counting command returns 0 on a no-space row; Goodhart and tier inflation; verifier independence | H4/H5/H6 and H7 read |
| `.ufo/waves/kaika-w1/freshness.md` | `recheck:` reality: zero calendar deadlines fleet-wide; external URLs nearly absent outside kotodama; dead-root inventory | headline and per-lane table read |
| `.ufo/waves/kaika-w3/*-review.md` | Per-lane SOURCES audit precedent: validate exits, E-codes, row re-opens, count reproduction | e.g. chousa `:46-48`, kengaku `:55-60`, lore `:69-74`, mado `:64-69`, revenger `:43-48`, souji `:71-76`, kaidoku `:35-41` |
| `.ufo/waves/kaika-aggregate/seats/planner.md` | Revision discipline: one OID per lane, same OID for gate/SOURCES/count; changing-head trap; final matrix shape | §“Pinning semantics”, §“Changing-head trap”, checklist 3–8 |
| `.ufo/waves/kaika-aggregate/seats/source-count-reconciliation.md` | Independent count reconciliation, W/E semantics, validator latent weaknesses, post-integration rerun list | §2–§8 read |
| `.ufo/waves/kaika-aggregate/seats/audit-*.md` | Per-lane structural audits and study-path extraction; concrete stale-hop and pointer-drift findings | mado §SOURCES finding 2, tabi §5, kotoba §7/§11, kagi §8, audio/game-dev-2d/kumitate absence notes |

I did **not** run the corpus gate (`.ufo/waves/round-9/corpus-gate.mjs`) and make no gate verdict.
I read its declared implemented/not-evaluated sets (`corpus-gate.mjs:62-123`): implemented are
r2, r4, r7, r8-literal, r10, SHONEN **form**; `RULES NOT EVALUATED` at `:88-115` covers r1, r3,
r5, r6, r9, box-3 verifier independence and SHONEN truth; `OUT OF SCOPE BY CONSTRUCTION` at
`:116-123`. A gate pass or a clean SOURCES census is **not** whole-corpus semantic conformance.

---

## 2. What the index inherits from contract v1 (never re-defines)

These are contract facts, not index proposals:

- `## Paths` is an ordered study sequence with a stated “why this order”; it is not a link list.
- `## Leads (unopened)` is quarantined: “a lead is not evidence and never a row”.
- A registry row is a claim, written after opening the source; only `status`, `recheck`, and
  `used-by` change in place; a correction is a new row whose `teaches` opens `supersedes S0NN —`.
- A count carries its command; there is **no row quota**.
- The lane's research method stays chousa's; admission stays in `QUALITY.md`; `SOURCES.md`
  duplicates neither.
- Census is run from the lane root with the contract's own commands (`CORPUS.md:131-148`).

The index adds only **derived pointer columns** (line ranges, blob identity, validator exit,
selection class). It never turns a count into a quality/truth claim and never edits a registry.

---

## 3. Failure modes the index must not reproduce (audit-grounded)

| # | Failure mode | Evidence observed in this round's notes | Index rule |
|---|---|---|---|
| F1 | **Revision mixing.** A HEAD observed earlier is paired with bytes read later. | The planner names the changing-head trap; in this very capture window `kumitate` advanced `6336d71→0acb775`, `kaidoku` advanced `5ac7860→3b5fea8`, then both **landed** in their main checkouts (`767adaf`, `a5683a9`) with identical SOURCES blobs. `game-dev-3d` had 35 rows at reviewed `3f53896ff` and 36 at HEAD after `cab506b`. | Every row carries full OID + SOURCES blob; recapture on any move; never mix gate/SOURCES/count revisions. |
| F2 | **Absence rendered as “0 rows”.** | At 23:47Z `game-dev-2d`, `kaidoku`, `kumitate`, `audio` main checkouts returned validator `missing`/exit 2; by 23:52Z kaidoku and kumitate had landed, so only audio and game-dev-2d remain. Their files exist on the unlanded `kaika/round` branch. | Three distinct states: `landed`, `branch-only` (pin the branch + blob, mark pending), `absent` (no file at either). Never print `0` for absent. |
| F3 | **Count copied without its command.** | kagi's search log cites a grep that returns 0 (`audit-kagi.md` §8); kengaku LOG says 25 rows while HEAD is 26 (`audit-kengaku.md`); kotoba's search log cites a quota the contract does not set (`kaika-w3/kotoba-critic.md`). | `rows` cell is derived by the contract command at the pin; the lane's own number is not copied. |
| F4 | **Stale hop inside a path.** | mado's U2 path ends `→ S029 → S030` while S030 is `rejected` and the path text does not mark it (`audit-mado.md` §SOURCES finding 2); tabi's audit notes S028 should be read after S004; game-dev-3d's audit notes S036 supersedes S011's scope. | Table B carries per-hop statuses and classes; `stale-hop` paths are excluded until the lane appends a correction. |
| F5 | **Structural pass read as semantic truth.** | kasegi-critic: “Structural census cannot prove a source was opened or a quote semantically supports a claim”; kake-critic: the census “cannot establish that every external source was opened”. | Limits footer states this explicitly under both tables. |
| F6 | **Leads leakage.** | Contract: ART dossier rows are leads, not rows; connect-sources §5 pool rows are dossier-local ids, not lane registry ids. | Leads appear only as a section range; no lead title, URL, or count enters either table. |
| F7 | **Pointer drift.** | `audit-kotoba.md` §7: fleet `CORPUS.md` changed at `fa78388` after the lane HEAD, shifting cited line numbers 17→24. | The index cites `lane/corpus/SOURCES.md:line@pin` + blob, never a `CORPUS.md` line as the carrier. |
| F8 | **Validator holes read as coverage.** | Peer reconciliation: `symbolic()` accepts any word (`every round` passes as a cadence); the `supersedes` E04 exemption is not integrity-checked; E08 depends on `TZ`; `validate` reads the working tree, not a git blob; lane labels differ between roster and dir modes. | Limits footer names each; the index pins the script blob and the `--today` date. |

---

## 4. Proposed schema

### 4.1 Table A — lane pointer rows (required: exactly 21, one per physical lane)

Header (seven columns; the file is always `corpus/SOURCES.md`, so it is named in the header, not
repeated in every cell):

```text
| lane | pin (state) | blob | rows | Paths | Search log | Leads | validator |
```

- `lane` — physical repo basename (`kagi-shokunin`, …). Do not use roster ids (`kagi`) in this
  column; the validator's own lane label is invocation-dependent (roster vs dir mode).
- `pin (state)` — `<40-hex OID> (landed)` when the file exists at the lane default-branch HEAD;
  `<40-hex OID> (branch-only <branch>)` when it exists only on a lane worktree branch; `absent`
  when it exists at neither. For `branch-only`, the table must also carry the main-HEAD OID at
  which the file is absent. `landed` means “exists at this OID”, not “reviewed”.
- `blob` — `git -C <lane> rev-parse <pin>:corpus/SOURCES.md` (40-hex git blob id). This is the
  content identity; a reader can verify bytes without trusting a moving ref.
- `rows` — integer from the contract census command at the pin, suffixed `p` (provisional) until
  the parent's `FINAL LANES READY` and the canonical parser are fixed. Never present without the
  command in the footer.
- `Paths`, `Search log`, `Leads` — inclusive line ranges of the named `##` section at the pin
  (heading line through the line before the next `##` heading; `EOF` allowed). `Leads` is a
  navigation pointer only.
- `validator` — `<rc>/<codes>` from
  `bash scripts/sources-census.sh validate --today <YYYY-MM-DD> <lane-dir>` at the pinned script
  blob; codes are `E##×n` and `W##×n` (warnings do not change status) or `missing` for exit 2.
  For a `branch-only` lane, say which directory was validated (worktree file vs main checkout);
  the main checkout that lacks the file validates `missing`/exit 2, not clean.

Example (observed row, provisional): `audio-shokunin` · `343cd978… (branch-only kaika/round)` ·
`db1a3e64…` · `15p` · `26-34` · `35-41` · `42-51` · `1/E09×1,W01×1,W04×2`.

### 4.2 Table B — selected opened transferable study paths (curator subset)

Header:

```text
| key | origin | title | sequence | class | hops | transfer-to (basis) | caveats |
```

- `key` — index-local stable key (`P-01`…). Never a registry id.
- `origin` — `<lane>:corpus/SOURCES.md:<line>@<12-hex pin>` where `<line>` is the first line of the
  `## Paths` bullet; the section range and blob are in Table A. If the bullet wraps, the anchor is
  still its first line.
- `title` — the lane's own title, quoted verbatim, not paraphrased.
- `sequence` — `S### → …` exactly as written at the pin.
- `class` — one of:
  - `fully-read` — every hop `mined` (audit vocabulary: “fully-read chains”);
  - `mixed` — at least one `queued` hop, all ids resolve (a reading plan with unread hops);
  - `plan` — all/only `queued` (not citable as evidence; follow the lane's own “queued, not mined” marker);
  - `caution` — the path text explicitly marks a `rejected` hop as the lesson;
  - `method` — the lane's own method/re-anchor/own-work sequence (transferable as method, not domain evidence);
  - `stale-hop` — a `rejected` hop the path text does **not** mark (observed: mado U2 → S030). **Excluded** from selected rows; list only in a separate “excluded” note.
- `hops` — compact `mined n / queued n / rejected n` for the referenced ids, read from the same
  file at the pin. This is a row-status tally, **not** a source count and not a quality measure.
- `transfer-to (basis)` — candidate lanes with a basis pointer: `[W1 connect-sources §3]`,
  `[W1 connect-sources §2a]`, or `[lane-text]`. If the target is only curator judgment, write
  `[curator — parent adjudicates]`. Transferability is a selection rationale, never evidence that
  the receiving lane has adopted or verified the path.
- `caveats` — observed limits at the pin (e.g. “one unread hop”, “lane audit says read S028 after
  S004”, “branch-only, not landed”, “text marks rejected hop as caution”). Do not repair the path
  here.

**Selection predicate (mechanical, run at the pin):**

1. The bullet is under `## Paths` and is a study sequence, not a correction/errata bullet and not
   a search-log note.
2. Every `S###` in the bullet resolves to a Registry row in the **same** file at the **same** pin
   (`comm -13` must print nothing).
3. The class is `fully-read`, `mixed`, `caution`, or `method`; `plan` is listed only with that
   class, and `stale-hop` is excluded.
4. No lead, ART-dossier id, or unregistered title appears in the row.
5. The row is a pointer: it does not restate `teaches`, `anchor`, tier, or quote as verified.

### 4.3 Mandatory limits footer (copy under both tables)

1. **Parser identity.** The validator is `scripts/sources-census.sh`, cited by **git blob** and
   mode: `census` (default), `validate`, `overdue`, `shared`, `selftest`. Exit map: 0 clean or
   warnings · 1 E/overdue findings (or census missing) · 2 usage/env/missing registry · 3 selftest
   failure. `missing` (exit 2) must never be rendered as clean or as “0 rows”.
2. **Count command.** `rows` comes from `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
   corpus/SOURCES.md` at the pin (contract v1); tier/status histograms, malformed NF≠13, duplicate
   ids, enum violations and `used-by` path existence use the contract's own commands. Counts are
   **provisional** until `FINAL LANES READY` and the canonical parser are both settled. A count
   is not a quota, a quality measure, or a validation of any row.
3. **Validator mechanics.** `validate` codes E01–E12 (malformed, id, duplicate id/URL+scope, kind,
   tier, status, opened date, recheck, community-at-A, missing `used-by`, row outside Registry) and
   warnings W01–W04 (tier-C mined with used-by, thin rejected row, mined with no used-by, same URL
   across scopes). Warnings do not change status. `overdue` judges only ISO dates and `NNd`
   cadences; symbolic cadences are reported, never judged overdue. `shared` matches normalized
   URLs only. `validate` reads the **working-tree** file: confirm
   `git status --porcelain -- corpus/SOURCES.md` is empty, or validate a `git show` copy.
4. **Declared not-evaluated.** r1 (is the token a source), r3 (falsifiability), r5 (negative-claim
   sweep), r6 (quote location), r9 (append-only/ownership history), box-3 verifier independence,
   and SHONEN claim truth are **not evaluated** by the corpus gate; a snapshot has no history, so
   append-only is not checkable there. Neither `validate` nor the corpus gate verifies that a row
   was opened in the round that wrote it, that a quote grounds `teaches`, that a tier is honest
   for its scope, that an `anchor` is exact, that a `supersedes` target exists, that Leads stayed
   out of the registry, or that a Path's ordering is good. Path id resolution and Leads/evidence
   separation are index-author checks (§5), not validator outputs.
5. **Unopened Leads.** Leads are not evidence and are never counted as sources. Table A carries a
   line range only; Table B never contains a lead title, URL, or id. If a lane's path prose says
   “as a lead only”, the index preserves that marker and does not promote the item.
6. **No semantic promotion.** A validator `ok`, a gate pass, or a clean structural census does not
   establish whole-corpus semantic conformance.

### 4.4 Rendering rules

- One physical lane per row; 21 rows, sorted by basename. Missing row = coverage failure, not a
  clean lane.
- Full 40-hex OIDs and blob ids are the record; shortened hex in a rendered table is display only.
- A lane that moves between observation and publication is **re-captured** (OID, blob, ranges,
  rows, validator) or the row is marked stale. Never pair a pre-move gate/validator result with a
  post-move file read.
- `branch-only` rows are explicitly pending. They are not published as landed and their counts
  are not added to a “landed” subtotal without the label.
- No score column, no rank, no “quality” field. The index reports pointers and classes only.

---

## 5. Author checks (exact commands, tested on this corpus)

Run from `/home/vgpnk/Projects/shokunin` with absolute lane paths.

```sh
# 1. physical set
ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l        # observed: 21
# 2. pin + content identity (landed path)
git -C <lane> rev-parse HEAD                                   # 40-hex
git -C <lane> rev-parse HEAD:corpus/SOURCES.md                 # 40-hex blob; fatal if absent
git -C <lane> cat-file -e HEAD:corpus/SOURCES.md; echo $?      # observed: 0 landed, 128 absent
# 3. branch-only fallback (only when step 2 exits 128)
git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/<lane> rev-parse HEAD
git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/<lane> rev-parse HEAD:corpus/SOURCES.md
# 4. section ranges at the pin
git -C <lane> show <pin>:corpus/SOURCES.md | grep -nE '^ {0,3}## '
# 5. provisional rows (contract v1 command)
git -C <lane> show <pin>:corpus/SOURCES.md \
  | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
# 6. path-id resolution (tested; dangling set must be empty)
git -C <lane> show <pin>:corpus/SOURCES.md > /tmp/s.md
awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' \
  /tmp/s.md | sort -u > /tmp/ids
awk '/^## Paths/{f=1;next}/^## /{f=0}f' /tmp/s.md | grep -oE 'S[0-9]{3,}' | sort -u > /tmp/pids
comm -13 /tmp/ids /tmp/pids                                    # must print nothing
# 7. validator at a pinned script blob (canonical copy from the fleet root)
git -C /home/vgpnk/Projects/shokunin rev-parse HEAD:scripts/sources-census.sh
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today <date> <lane-dir>; echo $?
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census   --today <date> <lane-dir>
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh overdue  --today <date> <lane-dir>
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh shared   --today <date> <dir> [<dir>...]
# 8. working-tree equality for the validator (validate reads the file, not the blob)
git -C <lane> status --porcelain -- corpus/SOURCES.md | wc -l    # observed: 0 for all 21 at capture
```

Observed on the selected paths at their pins: tabi `protocol-choice` and `flake-receipts`,
tameshi, chousa, souji, kagi, audio, kumitate, kotoba and mado paths all had
`dangling: []`; example tabi: `refs=20 ids=28` through the two commands above (all 20 distinct
referenced ids resolve). The check is mechanical id **resolution**, not ordering quality.

---

## 6. Provisional baseline at capture (2026-10-19T23:52Z)

### 6.1 Pins (full OIDs; blobs are `corpus/SOURCES.md`)

`state` is the state observed at the final capture. `kaidoku` and `kumitate` **landed during the
observation window**; their blobs were identical before and after landing, so their rows,
ranges and validator results are unchanged. Only `audio` and `game-dev-2d` remain branch-only.

```text
audio-shokunin        branch-only  pin 343cd978ef376fc6e0c3d53a8740b931f7d031df (kaika/round)
                                    blob db1a3e6406d8ce491dce614fde6b362c008c9d0d
                                    absent at main defbe128649268bfca75757cb3978be802696592
chousa-shokunin       landed       pin d730ae4c33989ad9c8535764d4cae77b4db869f6
                                    blob 8429343f1b750a9fd4bc7a470373d99ae57d1ad3
game-dev-2d-shokunin  branch-only  pin ff32e252b9301d5d25f863accedddddeda1ca569 (kaika/round)
                                    blob ef111e28a5e0068b390acf1e1d573966734527c0
                                    absent at main e89905162b3a630a599607279681b30572010724
game-dev-3d-shokunin  landed       pin 3118be0b18dd7351b1faf6ce99d26a34370793ec
                                    blob 07a5816947c98a6c39b4ace520aa15654c74c795
kagi-shokunin         landed       pin 1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2
                                    blob 36e166f08fefd6053c1effde41ec6174cb0f5820
kaidoku-shokunin      landed*      pin 767adafb97e2eef6980e2ad873d357e16721c467
                                    blob a411c18c74c0690c1073e08f241c53779750263d
kake-shokunin         landed       pin 7e17c663b8713daac27774d49d87c4d44ea30747
                                    blob bb7ed1649256a0ccfd5f8bdc71f1b9c003b9ee09
kama-shokunin         landed       pin 03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9
                                    blob 7de1360655eadada356fe110813c6e1338142551
kasegi-shokunin       landed       pin 13a51920068c48c0c5b3c8c81d5af0df6d4ea337
                                    blob 01fcdbb6b833482ac15e8211624832f52b8abb9e
kengaku-shokunin      landed       pin a42bb40c1767e1ac24394fadda7301ae5409e7ae
                                    blob 74070565c0932a39737fc7d24250c5a716802e40
kotoba-shokunin       landed       pin c61a973b2e02e1ded169703ddcb06466f4edd8bd
                                    blob a048aef0997e68881c9740e878d2fe01402bb04b
kotodama-shokunin     landed       pin 4ad26836552462d28a946ca3b067cab0b5ce3532
                                    blob 34e27f6a1878b0de2bf69785ef2c4b391a1fdb01
kumitate-shokunin     landed*      pin a5683a96cae2fcdcf313e4a3b47dea340d6451a9
                                    blob 6e92b79bdfe022648574c271c4a9a9768238912b
lore-shokunin         landed       pin 6e804e2e5bff0edcc260c995a058dd724b0c98c0
                                    blob a547b1b60314cb7aacdebad9fb7852509c8e59d3
mado-shokunin         landed       pin e3e6a8e6ca493e250fb357343816a88e844c4c63
                                    blob 56f8f49c9913455e89bdf91434130f0d4637b887
mori-shokunin         landed       pin bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a
                                    blob 9065f76f35d7185b4fc5b2ba10c9a05a5cd1186f
revenger-shokunin     landed       pin cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97
                                    blob 2fcf0d901c71116ea951eb012be67125c2980948
souji-shokunin        landed       pin 31984f473ce4bdab61a99b16cca194b28108cb81
                                    blob a67b6f573f1fbb52198c028f0d7e77f5fa3b7f35
tabi-shokunin         landed       pin 9bc89bfe78b1c455501b2c7a0d9bd061ea539c21
                                    blob 89a69384adeff8ccda3b41e4938abc40425492b9
tameshi-shokunin      landed       pin a21e9104723e7a46b794b03b8fdcdd1455696f7e
                                    blob b1cff984384860ad7b3d301aef493ba0386c3a68
tsukuroi-shokunin     landed       pin d8ec15d5e6c1d93370f5a85b929745e26577f4d8
                                    blob 194059c471e25702edb6b39c58abd91a79f3d8b5
```

`*` = landed during the observation window (main-checkout HEAD advanced to the listed OID; the
SOURCES blob equals the earlier branch blob).

### 6.2 Table A preview (provisional; 12-hex display only)

| lane | pin (state) | blob | rows | Paths | Search log | Leads | validator |
|---|---|---|---:|---|---|---|---|
| audio-shokunin | `343cd978ef37` (branch-only) | `db1a3e6406d8` | 15p | 26-34 | 35-41 | 42-51 | `rc1` E09×1, W01×1, W04×2 (worktree file) |
| chousa-shokunin | `d730ae4c3398` (landed) | `8429343f1b75` | 18p | 30-45 | 46-71 | 72-83 | `rc0` |
| game-dev-2d-shokunin | `ff32e252b930` (branch-only) | `ef111e28a5e0` | 31p | 39-45 | 46-52 | 53-56 | `rc0` (worktree file); main `missing` rc2 |
| game-dev-3d-shokunin | `3118be0b18dd` (landed) | `07a5816947c9` | 36p | 46-53 | 54-65 | 66-70 | `rc0` |
| kagi-shokunin | `1e9e67ff3f8f` (landed) | `36e166f08fef` | 16p | 24-29 | 30-33 | 34-43 | `rc0` |
| kaidoku-shokunin | `767adafb97e2` (landed*) | `a411c18c74c0` | 22p | 30-39 | 40-43 | 44-50 | `rc0` |
| kake-shokunin | `7e17c663b871` (landed) | `bb7ed1649256` | 18p | 28-34 | 35-44 | 45-65 | `rc0` |
| kama-shokunin | `03b5f0e8b9ec` (landed) | `7de1360655ea` | 30p | 44-50 | 51-56 | 57-60 | `rc0` |
| kasegi-shokunin | `13a51920068c` (landed) | `01fcdbb6b833` | 27p | 35-40 | 41-49 | 50-54 | `rc0` |
| kengaku-shokunin | `a42bb40c1767` (landed) | `74070565c093` | 26p | 50-57 | 58-65 | 66-70 | `rc0` |
| kotoba-shokunin | `c61a973b2e02` (landed) | `a048aef0997e` | 11p | 26-40 | 41-67 | 68-87 | `rc0` |
| kotodama-shokunin | `4ad268365524` (landed) | `34e27f6a1878` | 47p | 78-111 | 112-119 | 120-169 | `rc0` |
| kumitate-shokunin | `a5683a96cae2` (landed*) | `6e92b79bdfe0` | 20p | 35-55 | 56-94 | 95-118 | `rc0` |
| lore-shokunin | `6e804e2e5bff` (landed) | `a547b1b60314` | 32p | 42-51 | 52-63 | 64-78 | `rc0` W01×1, W04×2 |
| mado-shokunin | `e3e6a8e6ca49` (landed) | `56f8f49c9913` | 39p | 52-60 | 61-93 | 94-120 | `rc0` W04×1 |
| mori-shokunin | `bf7cdc4783d0` (landed) | `9065f76f35d7` | 34p | 42-47 | 48-53 | 54-56 | `rc0` |
| revenger-shokunin | `cf02419276e5` (landed) | `2fcf0d901c71` | 15p | 31-37 | 38-43 | 44-49 | `rc0` |
| souji-shokunin | `31984f473ce4` (landed) | `a67b6f573f1f` | 33p | 43-48 | 49-55 | 56-68 | `rc0` |
| tabi-shokunin | `9bc89bfe78b1` (landed) | `89a69384adef` | 28p | 44-50 | 51-58 | 59-63 | `rc0` |
| tameshi-shokunin | `a21e9104723e` (landed) | `b1cff9843848` | 44p | 57-62 | 63-100 | 101-122 | `rc0` |
| tsukuroi-shokunin | `d8ec15d5e6c1` (landed) | `194059c471e2` | 34p | 42-47 | 48-55 | 56-73 | `rc0` |

Preview totals (provisional, all 21 source files): `FLEET rows 576 | tier.A 500 | tier.B 33 |
tier.C 43 | status.queued 220 | status.mined 307 | status.rejected 49 | tier.invalid 0 |
status.invalid 0 | missing 0`. Arithmetic holds: 500+33+43 = 576 and 220+307+49 = 576.
Landed-only subtotal = 488p; branch-only subtotal = 88p. These are **not** final totals.

### 6.3 Parser and validator identity

| Artifact | Identity | Observed |
|---|---|---|
| Canonical (fixed) `scripts/sources-census.sh` | fleet root `master` HEAD `b38d358ef302d893d4c2c6fe9e1dd6c524275cfb` (merge of `kaika/sources-hardening`); file blob `55c886d1f67e41a84db2ac5a97fac591d1f14fe8`; sha256 prefix `a621fe0ec8a946430e4956353717c97a` | `selftest` rc 0, 93 `killed`, 0 `SURVIVED`, final line `selftest ok`; commit `ff701da145201de549e52b2a8bbcaf490329c44c` (“sources census: parse supported Markdown indentation in every mode”) |
| Pre-fix parser | blob `b5dcc152212a38d2e3ee122fc46081453840cdcf`; sha256 `aed9ed65e42eaa5d372c380509e05f6fabbb39ec15cc75f06010898474ae8d1b`; present in `fleet-census` @ `ae7bf19` and in this worktree (`fleet-aggregate` @ `ee8ba85` tree) | `selftest` rc 0, 56 `killed`, `selftest ok` |
| Parity at capture | fixed vs pre-fix `validate` on all 21 source files | **identical stdout and exit codes** on every lane; 0 indented `##`/`|` lines exist in any of the 21 files (`grep -cE '^ +(##|\|)'` → 0 everywhere), so the fix is currently behaviour-neutral for this corpus |
| Indented-row fixture | the fix’s own selftest exercises indentation widths 0,1,2,3 for valid rows, invalid tier/used-by, row-outside-Registry, and the shared map | 93-check selftest; this is the fix’s declared coverage, not independently re-derived by this seat |

Skew warning: this worktree (`fleet-aggregate`, branch `kaika/aggregate`) still carries the
**pre-fix** copy at `scripts/sources-census.sh`; the fleet root carries the fixed copy. An author
who runs the worktree copy is not running the canonical bytes; pin the blob.

### 6.4 Validator observations (canonical fixed parser, `--today 2026-10-19`)

- 20 lanes `rc0`; warnings only: lore `W01 S027 tierC mined used-by=corpus/knowledge/r103-canon-status-and-supersession.md` and `W04 S017 arxiv.org/html/2603.05890`, `W04 S032 www.iso.org/standard/70908.html`; mado `W04 S030 wiki.hypr.land/Configuring/Basics/Window-Rules`.
- 1 lane `rc1`: **audio** (branch-only file):
  `E09 S011 recheck=—`; `W01 S007 tierC mined`; `W04 S014` (FFmpeg af_loudnorm source URL);
  `W04 S015` (ITU-R BS.1770-5 PDF URL). Failed rule: **E09**, invalid `recheck` cell.
- Main checkouts of branch-only lanes: `validate` returns `missing` with **exit 2** (observed for
  audio and game-dev-2d at the final capture; kaidoku and kumitate returned this earlier and now
  validate `ok` after landing). Exit 2 must not be read as clean.
- `overdue --today 2026-10-19` over all 21 source files → **0 overdue lines**.
- `shared --today 2026-10-19` over all 21 source files → **2 URLs**, rc 0:
  `godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd` (game-dev-2d + game-dev-3d)
  and `kubernetes.io/docs/concepts/workloads/pods/probes` (kama + mori). The peer reconciliation’s
  17-file run saw only the second; the difference is the file set (branch-only files included
  here), not a contradiction.
- Working-tree equality: `git status --porcelain -- corpus/SOURCES.md` → 0 lines for every one of
  the 21 source files at capture (17 main checkouts + 4 worktree files before landing; 19 + 2
  after landing).

### 6.5 Concrete count-drift evidence

`game-dev-3d-shokunin`: `git show 3f53896ff:corpus/SOURCES.md | grep -cE '^\|…S…\|'` → **35**;
`git show HEAD:corpus/SOURCES.md | …` → **36**; the delta landed in `cab506b`
(“round-108: post-review fixes”). A count copied from the w3 review would be stale by one at HEAD.
This is exactly why Table A carries a pin and a blob.

---

## 7. Candidate selected paths (provisional; parent adjudicates)

All rows below were id-resolved at the stated pin; none uses a Lead. `hops` is a row-status tally,
not a source count. Transfer targets are candidate only; `[W1]` = `connect-sources.md` basis.

| key | origin | title (verbatim) | sequence | class | hops | transfer-to (basis) | caveats |
|---|---|---|---|---|---|---|---|
| P-01 | tabi `:47` @ `9bc89bfe78b1` | `protocol-choice` | S002 → S005 → S006 → S012 → S011 → S008 → S009 | fully-read | mined 7 | kake, kaidoku, kagi (W1 §2a browser/CDP; §3 WebDriver BiDi row) | transport choice is per evidenced feature; ordering not independently judged |
| P-02 | tabi `:48` @ `9bc89bfe78b1` | `flake-receipts` | S013 → S014 → S017 → S015 → S016 → S018 → S019 | fully-read | mined 7 | tameshi, tsukuroi (curator) | generic retry-evidence method; receiving lanes not verified to adopt |
| P-03 | tameshi `:59` @ `a21e9104723e` | `Mutation verdict semantics and validity` | S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007 | mixed | mined 4, queued 4 | kumitate, kagi, chousa (W1 §3 mutation-testing row) | four unread hops at the pin |
| P-04 | chousa `:36` @ `d730ae4c3398` | `Following a citation chain` | S003 → S005 → S006 → S007 → S010 | mixed | mined 4, queued 1 | all 21 lanes (W1 §3 chousa row) | S010 unread; ordering is chousa's own |
| P-05 | souji `:45` @ `31984f473ce4` | `F1 git-native housekeeping` | S002 → S001 → S009 → S003 → S004 → S010 → S011 | mixed | mined 6, queued 1 | all lanes' worktree/object hygiene (W1 §2a item 5) | S011 unread; git-version-sensitive |
| P-06 | kagi `:28` @ `1e9e67ff3f8f` | `Vault and OpenBao authentication/lifecycle` | S012 → S013 → S014 → S015 → S016 | fully-read | mined 5 | tabi, kama, kumitate (W1 §3 kagi row) | credential-adjacent reading; no vault read by this seat |
| P-07 | audio `:28` @ `343cd978ef37` (branch-only) | `Game loudness` | S001 → S002 → S003 → S004 → S006 → S005 → S007 | fully-read | mined 7 | game-dev-2d, tameshi (W1 §3 EBU R128 row) | **not landed**; pending parent signal |
| P-08 | kumitate `:43` @ `a5683a96cae2` | `OMP delegation contract` | S001 → S002 → S003 → S004 | fully-read | mined 4 | lanes dispatching OMP L2s (lane-text: task boundary bounds every spawn) | broad target set is curator judgment; path is kumitate-specific |
| B-01 (caution) | kotoba `:28` @ `c61a973b2e02` | `Authoring a SKILL.md that loads everywhere` | S001 → S008 → S003 → S002 → S011 | caution | mined 4, rejected 1 (S011) | kotoba, kumitate (W1 §2a item 4) | text explicitly says “the rejected tutorial last”; rejected row is taste evidence, not support |
| X-01 (excluded) | mado `:55` @ `e3e6a8e6ca49` | `Configuration-language era (U2)` | S021 → … → S029 → S030 | stale-hop | mined 9, rejected 1 (S030) | — (excluded) | path text does not mark S030 as rejected; `audit-mado.md` §SOURCES finding 2; exclude until a lane-side append-only correction |

Also observed but not selected here: `tabi` `accessible-selectors` is marked “queued, not mined”
(class `plan`); `lore` `:50` is a **correction** bullet, not a study sequence; `mado` U4/U6 is
explicitly queued and is not cited as evidence by its own audit. These demonstrate why the
selection predicate needs the `plan` and correction-bullet exclusions.

---

## 8. Open items routed to the parent (not rules, not edits)

1. **Landing state.** At final capture, audio (`343cd978…` branch) and game-dev-2d
   (`ff32e252…` branch) have registries only on `kaika/round`; their main checkouts still return
   `cat-file` exit 128 and validator `missing`/exit 2. Final Table A must either land these or
   publish them explicitly as `branch-only` pending rows after `FINAL LANES READY`.
2. **Audio E09 before any clean claim.** The branch file’s `S011 recheck=—` fails E09. A landed
   copy would make the lane’s validator status `rc1`, not clean; fix is lane-side (append-only
   correction), not an index rule.
3. **Canonical validator identity.** The fleet root now carries the fixed parser (blob
   `55c886d1…`); this worktree still carries the pre-fix blob (`b5dcc152…`). The final index must
   cite the blob it ran and re-run after integration.
4. **Stale/caution path annotations.** mado (rejected S030 unflagged in U2), tabi (S028 read-order
   note), game-dev-3d (S036 vs S011 scope) are lane-side observations from the audit seats; the
   index records them as caveats and does not repair the lane text.
5. **Roster labels.** `shokunin.conf` roster mode and physical-dir mode label lanes differently
   and add protocol/aggregator `missing` rows; Table A keys the 21 physical basenames.
6. **Pointer drift.** `CORPUS.md` line numbers are not stable carriers (`audit-kotoba.md` §7);
   Table A uses lane-relative `corpus/SOURCES.md` + line at pin + blob.

---

## 9. Limits of this note

- Read-only observation; no lane, report, gate, script, contract, or config was modified. No
  corpus gate was run; no SOURCES URL was fetched or re-opened by this seat; no quote, `teaches`,
  tier, `anchor`, or `used-by` semantics were verified. The row-status tallies and validator
  outputs are structural only.
- No unopened Lead was used as evidence. Leads were read only as section ranges for Table A.
- Totals are **provisional**: they describe the 21 source files at the pins in §6.1 and are
  sensitive to the parent’s parser/integration state; they must be re-read after
  `FINAL LANES READY`. They are not published as final and must not be copied into any report.
- Concurrent-writer observation: lane worktrees and main checkouts moved during the window
  (`kumitate` `6336d71→0acb775→d933e15→a5683a9`; `kaidoku` `5ac7860→3b5fea8→767adaf`), so a row
  captured before the last read is only as good as its pin; re-capture on any move.
- The schema is a recommendation for the parent’s report/index surface. It adds no registry rule,
  no admission method, no gate, and no score; its selection table is curator judgment and the
  parent retains adjudication.
