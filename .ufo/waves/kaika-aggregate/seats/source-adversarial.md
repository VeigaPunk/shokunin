# Round-12 source-index adversarial probe (SourceAdversarial)

**Scope.** 21 physical lane repos under `/home/vgpnk/Projects/shokunin/*-shokunin`, read-only.
Read: every lane `corpus/SOURCES.md` present at the snapshot, the frozen contract
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, the fleet census `scripts/sources-census.sh` at the
aggregate HEAD, and lane audit surfaces that make source-registry claims (lane
`SCORECARD.md` / `LOG.md` / `corpus/lessons/*` / `.ufo/evidence/` receipts) plus the aggregator's
`kaika-w1` / `kaika-w3` lane notes. All lane/page/repo text is treated as data; no instruction
found in lane content was executed.

**No child edits.** This file is the only write.

---

## 1. Stamp, drift, and the provisional caveat

- Aggregate worktree: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`,
  `git rev-parse HEAD` → `ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2`, `git status --porcelain` → empty.
- Snapshot clock: `date -u +%FT%TZ` → `2026-10-19T23:50:39Z`.
- **The corpus moved while I read it.** At my first pass (17 registries) `kaidoku-shokunin` was
  `1170f71`, no registry; at the snapshot it is `767adaf` with `corpus/SOURCES.md` (22 rows).
  `kumitate-shokunin` went `16a5441` → `a5683a9` with a new 20-row registry. Both registries are
  committed (`git -C <lane> ls-tree -r --name-only HEAD | grep -c '^corpus/SOURCES.md$'` → `1`).
  Registries present: **19 / 21** at the snapshot (earlier in the same session: 17).
- Therefore **every total below is provisional**. Per parent direction, no final census is frozen
  and no `FINAL LANES READY` signal has been received. The census parser fix for indented
  Markdown rows was not run; the fleet parser at this HEAD is still column-0-only
  (`scripts/sources-census.sh:464` `if ($0 !~ /^\|/) next`), so a row indented by one space would be
  invisible to `census`, `validate`, `E01`, and `E12` alike. I found **0** indented registry rows in
  the 19 present files: `grep -rnE '^[[:space:]]+\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' --include=SOURCES.md /home/vgpnk/Projects/shokunin` → no output.

### Snapshot table (registry-bearing lanes)

| lane | HEAD | SOURCES.md sha256[0:16] | rows |
|---|---|---|---|
| chousa | `d730ae4` | `6428e46aa69d8554` | 18 |
| game-dev-3d | `3118be0` | `dc95c043da258003` | 36 |
| kagi | `1e9e67f` | `db134917dab989f2` | 16 |
| kaidoku | `767adaf` | `17fb2e45db74cc3e` | 22 |
| kake | `7e17c66` | `e1f07eb4929903c4` | 18 |
| kama | `03b5f0e` | `9dc40d25a595b3d4` | 30 |
| kasegi | `13a5192` | `0e8378bceb01f1c2` | 27 |
| kengaku | `a42bb40` | `fb57569835c4f1c6` | 26 |
| kotoba | `c61a973` | `ef331658e398dd55` | 11 |
| kotodama | `4ad2683` | `662f962687717fa9` | 47 |
| kumitate | `a5683a9` | `203b34e6c39705d3` | 20 |
| lore | `6e804e2` | `9fc435e8095f8f86` | 32 |
| mado | `e3e6a8e` | `9b175fa9925a7b72` | 39 |
| mori | `bf7cdc4` | `efe349d580266b84` | 34 |
| revenger | `cf02419` | `c1573b2fbc284493` | 15 |
| souji | `31984f4` | `1b7cc681084e9e5e` | 33 |
| tabi | `9bc89bf` | `000053ccfc4e61f2` | 28 |
| tameshi | `a21e910` | `6b34e8991f56d78d` | 44 |
| tsukuroi | `d8ec15d` | `3e06c2ebb36f5fea` | 34 |

Missing at snapshot: `audio-shokunin` (`defbe128`), `game-dev-2d-shokunin` (`e8990516`).
The fleet root's own `protocol` / `aggregator` lanes also have no `corpus/SOURCES.md`.

---

## 2. Commands run, with observed output and exit codes

```sh
# 1. section shape, per lane
python3: regex '^## ' over each corpus/SOURCES.md
→ all 19 have exactly # SOURCES / ## Registry / ## Paths / ## Search log / ## Leads (unopened);
  tameshi adds ## Id allocation. 4/4 required sections present in 19/19.

# 2. contract census (fleet script) — PROVISIONAL
bash .tower/worktrees/kaika/fleet-aggregate/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin
→ FLEET rows 530 | tier.A 459 tier.B 30 tier.C 41 tier.invalid 0
  status.queued 201 status.mined 283 status.rejected 46 status.invalid 0 | FLEET missing 4
→ EXIT=1 (missing registries)

# 3. contract validate — PROVISIONAL
bash .../scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin --today 2026-10-19
→ protocol missing; aggregator missing; audio missing+unlisted; game-dev-2d missing+unlisted;
  game-dev-3d unlisted; lore W04 S017; lore W01 S027; lore W04 S032; mado W04 S030
→ EXIT=2 (usage/env/missing registry)

# 4. row well-formedness, 19 lanes
python3: split on '|', strip
→ 530/530 rows have NF=11 cells (contract's NF=13); 0 malformed; 0 duplicate ids per lane;
  0 enum violations; 0 tier-A community rows.

# 5. row -> used-by citation (the check no gate implements)
for each mined row, each used-by path: does the target file contain the row id?
→ mined rows 283; mined used-by cells 402; cells whose target carries the id 319;
  cells that do NOT 83 (20.6%), spread over 61 distinct target files in 4 lanes:
  kotodama 30, lore 27, tameshi 25, mori 1.

# 6. mined-row decomposition by knowledge uptake
→ 228 rows have ≥1 corpus/knowledge/ used-by carrying the id;
  23 rows have knowledge used-by but no cell carries the id (kotodama 8, lore 8, tameshi 7);
  32 rows have no corpus/knowledge/ used-by at all:
     kaidoku 21 (all → corpus/lessons/round-13.md), kotoba 4 (→ SKILL.md),
     mado 3 (→ corpus/lessons/round-12.md), kumitate 1, mori 1, souji 1, tabi 1 (lessons).

# 7. reverse direction: ids cited by corpus/knowledge/*.md but row still 'queued'
→ game-dev-3d S003; souji S024, S025. All other lanes: 0.

# 8. lead/row contradiction test
python3: normalized URL sets of Registry vs Leads, per lane
→ intersection empty in 19/19 lanes. No URL is simultaneously a row and an "unopened" lead.

# 9. blocked/partial-open disclosure scan (anchor+scope+teaches)
→ 13 regex hits; 3 are false positives on inspection (chousa S001: "manifest unreadable" is a
  gate test name; kake S014: "404-411" is a line range; game-dev-3d S023: "404" sits inside a
  commit hash). The 10 genuine disclosures: 3 mined at tier A (kotodama S032 body 403, S035 JSTOR
  paywalled, S036 argument unread), 5 queued (kasegi S024, lore S021/S023/S032, tameshi S020),
  2 rejected (kotodama S030, tabi S026). All 10 narrow their scope in the same row; none claims
  to have read text it did not.

# 10. recheck cadence reachability
→ 245/530 rows (46.2%) carry a symbolic cadence (`on-release`, `on-commit`, `on-change`, …);
  the census `overdue` mode reports these but never judges them overdue.

# 11. anchor locator sanity (manual review of the 13 anchor-token heuristic hits)
→ no bare-homepage anchor found. Every heuristic "bare" anchor I opened carries a section, a
  line range, a commit, or an edition. The heuristic was wrong, not the rows.
```

---

## 3. Findings

Severity is about *misreading risk by a fleet aggregator*, not about lane honesty. Several lanes
self-disclose the very gap; that is recorded under counterexamples.

### F1 — HIGH — `mined` is asserted one-directionally: 83/402 mined used-by cells do not contain the row id

- **Exploit path.** An aggregator (or the round-12 census) counts `status.mined` as "this source
  was mined into admitted knowledge". It reads 283 fleet-wide. For 83 pointer cells in 4 lanes the
  cited file cannot be shown to know the row exists; the row→entry link lives only in the
  `used-by` cell. Example: `kotodama-shokunin/corpus/SOURCES.md:31` (S002, WALS/C-LDF) lists eleven
  knowledge files; none contains `S002`; they cite "WALS" by name (13/3/10/18/23/2/3/6/13/1/5
  occurrences, checked per file). `lore-shokunin/corpus/SOURCES.md:13` (S005, Spence 1913) lists
  eight fixture notes; each says "Spence" but none says `S005`. `tameshi-shokunin/corpus/SOURCES.md:42`
  (S031) lists 12 knowledge/lesson files; none contains `S031`.
- **Why the gate cannot see it.** `scripts/sources-census.sh:417` checks only
  `[ ! -e "$dir/$path" ]`; the E01–E12 / W01–W04 inventory (header, lines 23–33) contains no
  content check on the target. The frozen contract's own census snippet has the same gap.
- **Impact.** The registry's strongest-looking status (`mined`) is not verifiable in the
  direction that matters for rule 4 ("expansion counts admitted `knowledge/` entries whose
  `source:` cites a `mined` row"). A fleet "mined" total overstates knowledge uptake by up to the
  83 cells / 24 rows affected.
- **Smallest remediation.** Promote tameshi's B2 check to a fleet `E13`: for every mined row, at
  least one used-by target must contain the row id or its source basename; keep B1 (id only) as
  the warning. tameshi already wrote the script
  (`.ufo/evidence/kaika-round-1/sources-census-v2.sh`, `B1`/`B2`).

### F2 — HIGH — `mined` used-by is not restricted to knowledge entries or lessons

- **Evidence.** `kotoba-shokunin/corpus/SOURCES.md:14,15,16,21` — four tier-A `mined` rows whose
  `used-by` is `SKILL.md`. That is neither a knowledge entry nor a lesson under the frozen
  contract's definition. `kotoba-shokunin/corpus/lessons/round-46.md:59` records the in-place
  change literally: "S001, S002, S003, S008 `queued`→`mined`, used-by `—`→`SKILL.md`". The same
  lane's admission bar Q12 (`corpus/QUALITY.md:23`) requires a knowledge entry's `source:` to name
  an `S###` row; **0 of 34** kotoba knowledge files cite any `S###` id. So the 4 `mined` rows have
  zero knowledge-entry uptake, and the row's own admission criterion is met by no entry.
  `lore-shokunin/corpus/SOURCES.md:13,14` list 11 `corpus/fixtures/**` paths as `mined` used-by
  (fixtures, not knowledge/lessons), e.g. `r94-paired-crossing/inspiration-note.md`.
- **Exploit path.** A "mined rows" or "expansion" reading treats a skill paragraph or a fixture
  note as admitted knowledge. Under rule 4 neither can ever count.
- **Impact.** 4 + 11 cells (7 rows: kotoba 4, lore S004/S005/S006) are category errors that the gate's path-existence check
  accepts. Combined with F1, 32/283 mined rows have no knowledge-entry back-reference at all —
  e.g. `kaidoku` is 21/22 rows `mined` solely via one lesson (`corpus/lessons/round-13.md`), and
  0 of its 91 knowledge files cite any id.
- **Smallest remediation.** Census rule: every used-by path must match
  `^corpus/(knowledge|lessons)/`; a non-matching path is E-level, not silent.
- **Counterexample (done right).** `kengaku` (5 new entries, 19 distinct ids, every cited row's
  `used-by` names the entry and every cell carries the id: 0 non-id cells);
  `kotodama-shokunin/corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18,20`
  names S031–S042 with an inline URL each and 12 rows list the entry back.

### F3 — MEDIUM-HIGH — a recorded receipt prints 25 failures under a "must print nothing" header and the lane still claims CLEAN

- **Evidence.** `tameshi-shokunin/.ufo/evidence/kaika-round-1/sources-census-final.txt:12`:
  `== H4: mined rows whose used-by file does not contain the row id (must print nothing)`,
  followed by **25** `no-id-cite:` lines (lines 13–37). The same lane's SCORECARD capability row
  (`tameshi-shokunin/SCORECARD.md:240`) cites the *v2* script →
  `SOURCES_CENSUS: CLEAN (contract v1 + H4 id-or-path)`. In v2 the strict id check is demoted to
  `== B1 strict id-cite (informational)` while B2 (id **or** source basename) gates the verdict.
  The aggregator note already caught part of this (`kaika-w3/tameshi-review.md:44`: "count=25
  (informational)").
- **Exploit path.** A reader takes the verdict token `CLEAN` as the receipt's conclusion while the
  receipt body contains 25 findings labelled "must print nothing"; the demotion is only visible in
  the script, not the recorded output.
- **Impact.** This is the cleanest single instance of "structural cleanliness presented as semantic
  conformance": the check that would falsify the mined claim is present, fails 25 times, and the
  headline stays green. It also shows why F1's fix must be an error, not a warning.
- **Smallest remediation.** Make B2's basename branch the only informational one; make id-cite an
  error for rows whose source is not `own-work`/`code`; re-emit the receipt with the verdict line
  derived from both checks.

### F4 — MEDIUM — rejected rows can read as positive recommendations; the W02 check is a length test

- **Evidence.** `mado-shokunin/corpus/SOURCES.md:41` (S030, tier **A**, status `rejected`):
  `teaches` = "Provides a current Lua example to contrast with the v0.54 hyprlang form." — a
  benefit, no `REJECTED:` reason, no `flip:`. Contract shape requires
  `REJECTED: <reason>; flip: <what would change the verdict>`.
- **Why the gate cannot see it.** `scripts/sources-census.sh:518` fires W02 only when
  `length(teaches)<8`; a 77-character positive sentence passes. The row is also counted in the
  tier-A histogram (459 fleet-wide) and in `W04` for a duplicate URL.
- **Exploit path.** A tier-A row with a positive `teaches` is exactly what a cross-lane source pool
  would surface; the `status` column is easy to drop when aggregating.
- **Impact.** One row at this snapshot, but the class is unchecked fleet-wide; the same
  length-only rule is what lets F1/F2 pass.
- **Smallest remediation.** W02 → `teaches !~ /^(REJECTED|supersedes S[0-9]{3})/` and reject
  rows missing `flip:`.

### F5 — MEDIUM — tier A does not distinguish "read the body" from "read the publisher's record"; supersession leaves the A rows in place

- **Evidence.** `kotodama-shokunin/corpus/SOURCES.md:63,67,68` — S034/S038/S039 are tier **A**,
  `mined`, anchored to "Crossref publisher abstract" / "as described by its publisher". The
  aggregator already filed this (`kaika-w3/kotodama-review.md:144`, D1 medium tier inflation) and
  the lane appended S044/S045/S046 (`SOURCES.md:73–75`) as tier **B**, `queued`, `supersedes …`.
  Result: the identical publisher text is in the registry twice, once A/mined and once B/queued;
  the A rows remain counted by every histogram. Also `SOURCES.md:61,64,65` — S032/S035/S036 are
  A/mined with `HTTP 403` / "JSTOR full text paywalled" / "its argument is unread". Their `scope`
  cells do narrow the claim to bibliographic identity, so the row is not lying; the histogram and
  the tier letter are what overstate.
- **Exploit path.** A fleet count of A-tier mined rows (459 A, 283 mined) is read as primary-text
  coverage; for 3 rows in this lane the primary text was never read and the tier-A anchor is a
  bibliographic record.
- **Impact.** Bounded to 3 mined rows + 1 queued supersession here, but the vocabulary has no field
  for it, so any cross-lane "A-tier mined" number inherits the ambiguity.
- **Smallest remediation.** Add `anchor-kind` (body | record | metadata) or require superseded rows
  to carry `superseded-by S0NN` in `scope`; do not rely on the appended B row alone.

### F6 — MEDIUM — status lag makes real knowledge use invisible; and one lane's used-by is incomplete

- **Evidence (understatement, not overstatement).** `souji-shokunin/corpus/SOURCES.md:32,33`
  (S024/S025) are `queued` with `used-by —`, yet
  `souji-shokunin/corpus/knowledge/quarantine-same-filesystem-rename.md:1,15-20` quotes both rows
  with section anchors and verbatim text. `game-dev-3d-shokunin/corpus/SOURCES.md:11` (S003) is
  `queued` while `corpus/knowledge/godot-headless-not-render.md:26` cites `(S003)`.
  `kake` has 14 knowledge→mined-row citations that the row's `used-by` does not name
  (e.g. `ghp-subpath-spotcheck.md` cites S001/S005; rows name only `ghp-served-set.md` /
  `ghp-custom-domain.md`).
- **Exploit path.** A rule-4 expansion count driven from `status=mined` misses entries that cite
  `queued` rows (3 here) and entries whose row's `used-by` is incomplete (14 here). The index
  therefore *understates* uptake in some lanes and overstates it in others; the two errors do not
  cancel in a direction an aggregator can assume.
- **Smallest remediation.** One command: knowledge-entry scan for `S###` → compare to the registry
  both ways, emit `E14 stale-queued` and `E15 used-by-incomplete`.

### F7 — MEDIUM — fabricated contract requirements used as stop rationale (rule 5)

- **Evidence.** `kotoba-shokunin/corpus/SOURCES.md` §Search log: "Stop rationale: the contract asks
  8–14 honest rows" and "contract requires at least one rejected row". The frozen contract says the
  opposite: `SOURCES-CONTRACT-v1.md:58` — "There is no row quota; a short registry of opened,
  honestly tiered rows beats a long one." The contract defines `rejected` as a kept status but sets
  no minimum. The aggregator critic already named this (`kaika-w3/kotoba-critic.md:48`).
- **Exploit path.** A reviewer trusting the search log concludes the registry size was
  contract-mandated, so a thin registry reads as compliant rather than as the lane's choice.
- **Impact.** Rationale-level overstatement; it does not change row content, but it is the kind of
  false authority that survives into reports.
- **Smallest remediation.** Append an erratum naming line 58; census cannot catch this, a reviewer
  must.

### F8 — LOW-MEDIUM — 46% of recheck cadences can never fire; "census clean" says nothing about freshness

- **Evidence.** 245/530 rows carry symbolic cadences. The census `overdue` mode emits
  `cadence` rows but never judges them overdue (script header, `overdue` block).
- **Exploit path.** A registry with 100% symbolic cadences is permanently "not overdue". mori
  (25/34), souji (24/33 at the earlier snapshot), kama (23/30), mado (23/39) are the densest.
- **Impact.** Freshness claims cannot be derived from the gate; the contract permits symbolic
  cadence, so this is a limit of the instrument, not a lane violation.
- **Smallest remediation.** Require a concrete `NNd` or ISO date on every row whose source is not
  `own-work`; keep symbolic only for `own-work`/`on-commit`.

### F9 — LOW — fleet coverage of the source index is 19/21 lanes and the gate is red

- **Evidence.** `FLEET missing 4` (protocol, aggregator, audio, game-dev-2d); validate exit 2;
  `audio`, `game-dev-2d`, `game-dev-3d` are `unlisted` in the conf-derived lane set though three
  have `*.round` state. `kaidoku`/`kumitate` landed registries mid-session.
- **Exploit path.** "All 21 lanes keep a source index" would be false at this snapshot; a fleet
  ledger built from the census must carry `missing 4` and the `unlisted` set.
- **Smallest remediation.** Root-level routing note naming the 4 absent registries as owned work,
  not a clean baseline.

---

## 4. Where the index does **not** overstate (counterexamples, same snapshot)

1. **Leads are kept out of the registry.** 19/19 lanes carry a `## Leads (unopened)` section
   (1–40 bullets); the normalized URL intersection between Registry and Leads is empty in every
   lane. kotodama's Leads header says "A lead is not evidence and never a row" and keeps 40
   bullets out; mado/tsukuroi/tameshi carry the same line.
2. **Blocked opens are disclosed, not laundered.** `kasegi-shokunin/corpus/SOURCES.md:30` (CRA,
   tier A, `queued`) says "Article 14 not reached in this round's reader — re-open before mining"
   and its `teaches` tells the reader to mine only after reading. `lore` S021/S023/S032 name the
   bot challenge/Wayback path; `kotodama` S032/S035/S036 name the 403/paywall.
3. **Rule-1 gate records are substantive where they exist.** `kotodama-shokunin/corpus/lessons/round-49.md`
   `## Gate` has 47 URL lines covering S001–S047, each with access date, verbatim ≤25-word quote and
   location; 47 found by `grep -cE 'https?://'` over the section. `kotoba`'s round-46 Gate records
   fetch timestamps + SHA-256 and **self-reports** a timestamp-label defect ("18:40 values are local
   time (UTC−3) labelled `Z`"). `kengaku`'s five entries carry ids both ways (19 distinct ids).
4. **Lore's own audit records the C3 weakness rather than hiding it**:
   `lore-shokunin/SCORECARD.md:708` says the post-landing critic "says this breaks as a capability
   claim (registry bookkeeping, not a new reader ability)" and records the fleet census exiting 1
   (E04 S017, W01 S027). `kaika-w3/lore-critic.md:21` documents that `measure.sh` is fail-open
   (`bash .ufo/waves/round-103/measure.sh no-such-revision` → `0/0`, exit 0).
5. **Tooling records are not sold as expansion.** 26 `own-work` rows exist (21 A/mined); they are
   the lane's own re-runnable gates/receipts, which the contract admits at tier A. tameshi's 12
   mined rows include 7 tool records (its harness + six sibling-lane gates, `SOURCES.md` S031–S037)
   yet its SCORECARD explicitly holds expansion unchanged: `tameshi-shokunin/SCORECARD.md:116`
   "expansion | unchanged | Corrections, not new knowledge on previously uncovered ground."
   revenger's tool-presence census is registered (S001) but its coverage map marks the affected
   rows `partial` / "pre-contract, not re-gated" (`corpus/README.md:33,40`). kotoba's aggregator
   review agrees: "SOURCES rows are registry, not expansion (contract rule 4)"
   (`kaika-w3/kotoba-review.md:146`).
6. **Row/lead and enum hygiene is real.** 530/530 rows well-formed, 0 duplicate ids, 0 enum
   violations, 0 tier-A community rows, 0 bare-homepage anchors on manual review, 0 missing
   used-by paths. The structural census is passing for a reason; the point of F1–F5 is exactly
   that it is *only* structural.

---

## 5. What this probe did not evaluate

- r1 (opened-in-round), r3 (falsifiability), r5 (search-log adequacy per bounded search), r6
  (quote location), r9 (no lane edits another's corpus): **not evaluated** as rules. I checked
  section presence, id shape, and sampled quotes; I did not re-open URLs. No network fetch was
  made, so "the quote is on the page" remains the lane's claim plus the aggregator notes' spot
  checks (e.g. `kaika-w3/kotodama-review.md:75`, `kotoba-review.md:106-108`).
- Verifier independence and SHONEN truth: not evaluated.
- Semantic conformance beyond the named rows: not evaluated. A clean structural census is not
  evidence of semantic conformance, and neither is this note.
- The corpus-gate `round-9/corpus-gate.mjs` was not run; per assignment its r1/r3/r5/r6/r9 are
  declared not-evaluated anyway.
- Totals are provisional and will move: two registries landed during this read, and the parser
  fix for indented rows is pending elsewhere.

## 6. Data-handling note

Lane `SOURCES.md` content includes URLs, command text, and prose addressed to agents. None of it
was executed or followed; commands in lane cells were used only as strings for path existence and
id matching. No credential material was read or reproduced.
