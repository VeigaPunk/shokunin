# Schema provenance and legacy ledger debt — Round 12 seat note

**Seat.** `KaikaAggregateR12.SchemaProvenance` (reviewer), dispatched in
`.ufo/waves/kaika-aggregate/dispatch.md` as "closure schema provenance and legacy
reconciliation debt". This is a read-only scratch note; it is not the round report, not a
gate, and not a census. The parent is sole coordinator/integrator/adjudicator and owns the
report, ledger refresh, and any commit.

**Observed.** 2026-10-19 ~20:45–21:00 -03. Fleet root HEAD
`b38d358ef302d893d4c2c6fe9e1dd6c524275cfb`; aggregate worktree HEAD
`ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2` (an ancestor of `b38d358`, verified exit 0).
`?? .ufo/waves/kaika-aggregate/` in the aggregate worktree is the wave directory containing
this and the sibling seat notes (untracked until the parent commits it); ` M README.md` in
the fleet root is the parent's working-tree edit, not this seat's. No child lane repo was
read in a mode that writes, and none was modified.

**Status.** No `FINAL LANES READY` signal has been received. Every count here is bound to
the exact revision named beside it and is provisional for final-census/report purposes.

## 1. Authority and planned Round 12 write paths

| Rule | Exact source | What it binds here |
|---|---|---|
| Report path and name | `PROTOCOL.md:146-148` | `.ufo/reports/round-12/aggregator.md` (the only valid name for this lane's round-12 report) |
| Minimum report content | `PROTOCOL.md:152-169` | work performed + evidence pointers; child-repo changes tied to `LOG.md`; cross-domain evidence; **Sources & frontier** section; `SHONEN` heading with one line per box |
| Report lands last | `PROTOCOL.md:117-119`, `PROTOCOL.md:135-137` | report is written after the round work is committed and must cite that commit's hash; corrections are new commits/errata, never rewrites of filed bytes |
| Aggregator scope | `PROTOCOL.md:326-341` | report covers per-repo corpus verdicts and cross-lane learnings; the rolling ledger is `.ufo/reports/AGGREGATE.md`; "no main-repo files outside its own report and ledger"; report incomplete unless the ledger was refreshed or the report names why no row changed |
| Aggregator exception | `PROTOCOL.md:329-333` | may create/repair `corpus/` inside a child repo only, committed by the aggregator at creation, pathspec-limited; **this round's seat contract makes all child repos read-only**, so the exception is not exercised |
| Root ledgers | `PROTOCOL.md:468-478` | the two main-repo lanes keep root `SCORECARD.md`/`LOG.md`; those are fleet files, not lane scratch; pathspec-limited commits only, never `commit -a`/`add -A` |
| Append-only rounds | `PROTOCOL.md:314-320` | corrections are appended `closure-correction` entries with `supersedes` (and `entry` when the triple is ambiguous); never in-place edits, never prepends |
| History pin | `PROTOCOL.md:322-325` | `.ufo/history-pin.json` pins `sha256(rounds[0:k])` and its anchor commit |

**Contract tension to state, not silently resolve.** `PROTOCOL.md:330` says the aggregator
has "no main-repo files outside its own report and ledger", while `PROTOCOL.md:468-470` says
both main-repo lanes "also keep `SCORECARD.md` and `LOG.md` at the main-repo root". For this
round the seat contract plus the parent's sole-integrator role resolve the practical path:
seats write neither root ledger; the parent owns them. The report must not cite the
aggregator corpus exception as authority for a root-ledger write, and if it records the
tension it should cite both lines rather than assert one silently.

**Planned Round 12 allowed paths** (from `.ufo/waves/kaika-aggregate/dispatch.md` plus this
seat's contract):

- Each seat owns exactly one note: `.ufo/waves/kaika-aggregate/seats/<seat>.md` (this file for
  `SchemaProvenance`). Untracked until the parent commits the wave.
- Parent-owned integration paths: `.ufo/reports/round-12/aggregator.md`,
  `.ufo/reports/AGGREGATE.md`, `.ufo/waves/kaika-aggregate/**`, and whatever the parent's
  integrator role commits. The parent decides `SCORECARD.md`/`LOG.md`/`MANIFEST.json`/
  `PROTOCOL*.md`/`ROADMAP.md` writes; **seats do not write them**.
- Read-only: all 21 original lane repos at `/home/vgpnk/Projects/shokunin/<id>-shokunin`
  (retired `.tower/worktrees/kaika/<lane>-shokunin` paths are not substitutes), domain source
  trees, and every remote. No project builds, tests, lint, or formatting were run by this
  seat (a read-only `check-jsonschema` manifest validation was run; §10.4).
- A seat note is not evidence until committed. The report must cite the commit that adds the
  seat files, or it must say the notes were working-tree artifacts at write time; a pointer to
  an untracked path does not resolve at closure (`PROTOCOL.md:343-358`, Evidence standard).

## 2. Revision pins for every artifact used below

| Artifact | Revision / path | Blob | SHA-256 | Note |
|---|---|---|---|---|
| Fleet root HEAD | `b38d358ef302d893d4c2c6fe9e1dd6c524275cfb` | — | — | merge `kaika/sources-hardening` into `kaika/ledger`, 2026-10-19 20:46:21 -03 |
| Aggregate worktree HEAD | `ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2` | — | — | ancestor of `b38d358` (exit 0) |
| `MANIFEST.json` @ `b38d358` = `ee8ba85` | fleet HEAD / aggregate worktree HEAD | `e6403816a074ccc8022684ff180e08797e3d030c` | `de481567aaa629a16e955be3777e1d39e36f9dcb3d6e3062890d471d029a7b08` | **314** `rounds[]`; working tree clean for this path |
| `MANIFEST.json` @ `dcf3b64` | pre-merge fleet revision | `7ac0c5f1090a1f8388dd0bd04234eb36a95bc610` | `bf475275fabe90cf92f2251e06b4a96959a9fcbc481b9d589103e749fc4bf61a` | **312** `rounds[]`; revision at which the parent's quoted `206/312` reproduces |
| `.ufo/history-pin.json` @ HEAD | both HEADs | `03b9be29bf122324cd824a82377e4429b3ea299d` | `b161cd4106c928472c1eca8395262beb7624e23349743fcd2880e2b416e7f81b` | `k=48`, pinned digest `ce97497e…d67f0a8e`, anchor `ae19fca` |
| `PROTOCOL.md` @ HEAD | both HEADs | `74bdc54d306fb96183c59155f056c3b982b32ffa` | `886e459b2aa79b8198912ad54bd57fbb025cc424d78684a02fb3d4c832d4411a` | same bytes in both worktrees |
| `.ufo/waves/round-15/closure-check.py` @ HEAD | both HEADs | `2e5c0afede78f50f94249b4043d6379b8fd54112` | `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` | 2060 lines; the canonical closure runtime (r15 successor) |
| `.ufo/waves/round-9/corpus-gate.mjs` @ HEAD | both HEADs | `c5e8f29f4fb9f2c28b3acab3e701dd85248098d3` | `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3` | `corpus-gate-v1` |
| `.ufo/reports/AGGREGATE.md` @ HEAD | both HEADs | `dbd2d42fa2abeac873d6819e3004278031bb4c78` | `94ab5f6b03cb493a7e50ccd4fef92fd1e199d1a59ea68110d0cd08937ad84523` | 2132 lines; 165 `D-` rows; max `D-155`; last section §15 |
| `scripts/sources-census.sh` @ fleet HEAD | `b38d358` | `55c886d1f67e41a84db2ac5a97fac591d1f14fe8` | `a621fe0ec8a946430e4956353717c97a2029b9fa85b9a8721cf4f363e1beead7` | corrected indented-row parser (`ff701da`) |
| `scripts/sources-census.sh` @ aggregate worktree HEAD | `ee8ba85` | `b5dcc152212a38d2e3ee122fc46081453840cdcf` | `aed9ed65e42eaa5d372c380509e05f6fabbb39ec15cc75f06010898474ae8d1b` | **stale** relative to fleet HEAD; do not use for final census from this worktree |
| Committed canonical schema | `/home/vgpnk/Projects/kimi-shokunin/templates/MANIFEST.schema.json` @ `bc7d69064a543bc9f5d3aeaccd2d59a0652d5747` | `5eae1063ffef73c7ceddfa26f013334a2463278a` | `6bd93af2c9dc59606b7c1ce310a3e4bfbf38bbf5093a51a7b97a0f2b105e43d8` | clean checkout; **no** `supersedes.entry`, no `trends`/`lane`/`lane_round` |
| Amended schema | `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon/templates/MANIFEST.schema.json` @ worktree HEAD `b3ca98f93859d54519425b5a594ed70b62361a33` | `5eae1063ffef73c7ceddfa26f013334a2463278a` at HEAD | `d6fc5f0a39122471cd1576910975d9649f7e2150582de723c29eac21d57c995c` working tree | **dirty**: ` M templates/MANIFEST.schema.json`, `+33/−2`; adds `entry`, `trends`, `lane`, `lane_round` |

Commands for the pins are in §10. The working-tree schema is the only byte set among these
that supports `supersedes.entry`; it is **uncommitted** and exists only in that worktree.

## 3. The parent update: statement, reproduction, and attribution

Parent-provided statement (normalized spacing from this seat's assignment; content unchanged):

> "canonical runtime validates all new closure shapes and all 45 `supersedes.entry` records;
> only 206/312 whole historical ledger records match current schema, 106 retain legacy
> vocabulary; preserve originals and report debt"

Verification status, kept separate so the report does not launder parent claims as its own
measurements:

| Parent claim | This seat's status | Evidence |
|---|---|---|
| `206/312` match current schema | **Reproduced exactly**, but only at `dcf3b64:MANIFEST.json` (312 records) and only against the **amended, uncommitted** schema bytes (`d6fc5f0a…`). At current fleet HEAD `b38d358` (314 records) the same check yields **208/314** | `check-jsonschema 0.38.2` exit 1; failing-entry count 106 at both revisions; §10 |
| `106` retain legacy vocabulary | **Reproduced**, same 106-entry set at 312 and 314; the two appended records (array indices `312` = kotodama round 49, `313` = mori round 12) validate | validator output: 106 unique failing paths; §5 |
| 45 `supersedes.entry` records | **Counted 45**; all 45 resolve to an existing array index whose `round` and `type` agree, and all target dates agree; targets are 26 `closure` + 19 `closure-correction`, 0 legacy-typed | §10.8 |
| canonical runtime validates all new closure shapes | **Code-inspected, not re-executed** (this seat ran no gate/test). The runtime's shape rules and supersedes rule are at `closure-check.py:526-701`; its type handling is at `:98-106`, `:577-589`; exit precedence at `:1428` | §6 |
| preserve originals and report debt | **Aligned and verified**: the history pin reproduces (`k=48`, digest match, anchor `ae19fca` is an ancestor); `rounds` is append-only (`PROTOCOL.md:314-320`) | §6/§10 |

The parent did not name the manifest revision behind `206/312`. The report must name it,
because the current committed ledger has moved: `dcf3b64` = 312/206/106 and fleet HEAD
`b38d358` = 314/208/106. Both are correct at their own revision; a bare "206/312" is already
stale at HEAD.

## 4. Schema identity is the load-bearing variable

Two byte identities are in play, and they give different answers:

1. **Committed canonical schema** — `kimi-shokunin` @ `bc7d690`, blob `5eae1063`, clean.
   `supersedes` has `additionalProperties: false` with only `round`/`type`/`date`; `entry`
   is forbidden. There is no `trends`, `lane`, or `lane_round` property (the round entry has
   no top-level `additionalProperties: false`, so those keys are merely undescribed).
   Whole-manifest result: **163/314 valid, 151 invalid** — the 106 legacy records **plus**
   all 45 `supersedes.entry` records.
2. **Amended working-tree schema** — `kimi-shokunin-canon` HEAD `b3ca98f`, dirty
   `+33/−2`, sha256 `d6fc5f0a…`. Adds `entry` (integer ≥0), `trends` (three required keys),
   `lane`, `lane_round`. Result: **208/314 valid, 106 invalid**.

The delta between the two counts is exactly the 45 `supersedes.entry` records. They are
**protocol-valid** (`PROTOCOL.md:314-320` explicitly authorizes `entry`) and are not legacy
vocabulary; they are a schema-lag class. The report must not merge them into "106 legacy".

**Wording rule.** `206/312` or `208/314` is meaningless without the schema bytes. Say
"against the amended schema working-tree bytes sha256 `d6fc5f0a…` (uncommitted in
`kimi-shokunin-canon` @ `b3ca98f`, +33/−2 vs committed blob `5eae1063`)", not "current
schema" or "canonical schema" unqualified. If the amendment is committed before the report
lands, cite that commit; until then, call it an uncommitted amendment and cite the committed
schema's 163/314 as the canonical-conformance figure.

Also do not alter the enums to make the debt disappear. `type` remains
`scaffold|work|ops|closure|closure-correction|retroactive-closure|mint` and lane status
remains `ok|failed|not-dispatched|in-flight` in both schema byte sets; `train`, `craft`,
`train+audit`, `train+audit+unlock`, and `closed` are fleet-era vocabulary, not canon.
Adding them to the canonical enum is an operator/schema decision in the canonical repo, not
an aggregator repair, and would still not make the historical records retroactively valid.

## 5. The 106-record debt at fleet HEAD, exactly partitioned

Source: `MANIFEST.json` blob `e6403816`, sha256 `de4815…`, 314 `rounds[]`, fleet HEAD
`b38d358`. Validator: `check-jsonschema 0.38.2` against the amended schema, exit 1.

| # | Class | Entries | Schema rule failed | Values |
|---|---:|---|---|---|
| 1 | `type` outside enum | 75 | `$.rounds[i].type.enum` | `train` 63; `craft` 9; `train+audit` 2; `train+audit+unlock` 1 |
| 2 | Lane status outside enum | 24 | `$.rounds[i].lanes.*.enum` | `closed` 24, entries 142–165 |
| 3 | Missing required `date` and `type` | 5 | `$.rounds[i].required` | entries 272, 277, 279, 291, 293 (kotodama loop rows; rounds 43,44,46,47,48) |
| 4 | `not-dispatched` without `closed_at` | 1 | `allOf` → `closed_at` required | entry 1 (round 1, `type:"work"`, kagi `not-dispatched`) |
| 5 | `round: null` | 1 | `$.rounds[i].round.type:number` | entry 138 (multi-lane snapshot closure) |

The classes are **disjoint**: 75 + 24 + 5 + 1 + 1 = 106 (the validator's 111 error rows are
106 entries; only the five class-3 entries carry two errors each). Exact failing-entry set at
both 312 and 314:

```
1, 75-90, 95-134, 138, 142-175, 264, 267, 271, 272, 276-279, 282, 285, 287, 288, 291, 293
```

(Ranges inclusive; `95-134` means every integer index in that span, not a stride.)

Key boundaries:

- **Only 1 of the 106 lies inside the pinned prefix**: entry 1 (`closed_at` debt) is in
  `rounds[0:48]`, whose canonical-JSON digest is pinned. It cannot be rewritten without
  producing `history_pin_mismatch`; the pin was verified to reproduce and anchor (§6).
- **105 of the 106 lie after the pinned prefix**; they are still not rewritable, because
  `rounds` is append-only after closure and index citations (including the 45
  `supersedes.entry` values) depend on positional stability.
- **"New-dated" is not "new closure shape".** Nine of the 75 enum failures are `craft`
  entries dated **2026-10-19** (chousa rounds 15–23, indices 264, 267, 271, 276, 278, 282,
  285, 287, 288). A sentence such as "all new entries validate" or "the new ledger is
  schema-clean" is false at HEAD even though the appended closure rows 294–313 validate.
- **Corrections do not clear type debt.** An appended `closure-correction` supersedes lane
  *rows*, not the superseded entry's `type`, `round`, or missing `date`. The 106 remain
  visible in the array forever under the current mechanism. Report them as debt; do not
  claim a correction made them conform.

Semantic debt is separate and larger: W1's manifest audit
(`.ufo/waves/kaika-w1/manifest.md` §3) records round-namespace collision, `closed`/`ok`
interchange, ambiguous supersedes, 10 unresolved `in-flight` rows, untyped `verdicts`,
zero rows for `revenger`, and unresolved kama probation. Schema conformance does not clear
any of these. If the report says "ledger health", it must say which lens it means:
structural schema, runtime row/supersedes, or semantics.

## 6. What the canonical runtime actually validates (and does not)

Runtime identity: `.ufo/waves/round-15/closure-check.py`, blob `2e5c0afe`, sha256
`0ac440f7…`, 2060 lines. The protocol registry row (`SCORECARD.md:194`) declares entry
command `python3 .ufo/waves/round-15/closure-check.py --repo . --json --no-citations` and
the exit map `0 clean / 1 failed / 2 could-not-evaluate / 3 no-baseline`.

What its ledger walk validates (`:526-701`): lane ids in the universe, `lanes` is a map,
statuses in `ok|failed|not-dispatched|in-flight`, `lane_rounds` integer values,
`closed_at` on not-dispatched/in-flight rows, `supersedes` on every closure-correction,
`supersedes` resolves to exactly one earlier row (unique triple, or explicit `entry` index
whose `round`/`type` agree), and `lane_rounds` keys in the lane universe. Closure types are
`closure|closure-correction|retroactive-closure`; `mint|scaffold|work|ops` are recognized
non-closure types; **any other type is `unknown_entry_type`** (`:577-589`).

It does **not** validate `trends`, `lane`, `lane_round`, `date` format/requiredness, or the
`type` enum as schema rules; unknown types become CNE findings, not schema errors. At HEAD
the 75 `train`/`craft`/`train+audit*` records **plus the five type-absent kotodama rows**
would therefore be reported `unknown_entry_type` (80 entries, CNE). Exit precedence is
`debt ? 1 : (cne ? 2 : 0)` (`:1428`), so a full-ledger run with any debt exits 1 and still
carries CNE rows. **A run cannot be called "clean" from the new-closure result alone.**

What the runtime's supersedes result means: all 57 `closure-correction` entries resolve —
45 by `supersedes.entry` and 12 by a unique `(round,type,date)` triple among **earlier**
entries. The 45 targets are 26 `closure` + 19 `closure-correction`; none is legacy-typed.
That is the precise sense in which "all 45 `supersedes.entry` records" validate. It is not a
schema claim: under the committed schema all 45 would be rejected for the unexpected
`entry` property.

## 7. Copy-ready report wording

Use these as shapes, filling exact values at write time. Do not paste a value whose revision
moved.

### 7.1 Provenance header

> Measurements are pinned to fleet commit `<full-oid>` (`git -C /home/vgpnk/Projects/shokunin
> rev-parse HEAD`, exit 0), `MANIFEST.json` blob `<blob>` (sha256 `<sha>`, `<N>` `rounds[]`),
> `PROTOCOL.md` blob `<blob>`, `.ufo/history-pin.json` blob `<blob>`, closure runtime blob
> `<blob>`, corpus gate blob `<blob>`, and the census parser blob `<blob>`. Child-lane
> observations are pinned per lane in §Pins: each row names the original repo path and the
> exact OID used for both the gate snapshot and the SOURCES read. This report ships in its
> own commit and cannot cite its own hash.

### 7.2 Parent evidence

> Parent-reported, not re-executed by this lane: `<verbatim statement>`. Independently
> reproduced: the 106-record legacy set and the 45 `supersedes.entry` resolutions, by
> `<command>` (observed `<output>`, exit `<code>`). Code-inspected only: the canonical
> runtime's closure/supersedes rules (`closure-check.py:526-701`); no gate run was made.
> Open: `FINAL LANES READY`; all census totals below are provisional.

Never write "verified" for a parent probe this lane did not run. The parent's corrected-parser
probe (`93 killed, 0 survivors; shellcheck 0`) stays parent evidence until re-run.

### 7.3 Lane revision pins

> Pins were captured after `FINAL LANES READY` with `git -C <original-lane-root> rev-parse
> HEAD`; only full OIDs are recorded, never branch names, tags, abbreviated hashes, or retired
> worktree paths. Each gate run used `--snapshot <original-lane-root> <same-OID> --round 12
> --json` and was accepted only with `mode=snapshot`, `revision=<same-OID>`, `dirty=0`. The
> SOURCES read used `git show <same-OID>:corpus/SOURCES.md`. A live-tree result is not a
> frozen verdict.

Provisional heads at this observation (do not publish as final):
`audio 343cd978e` (writer worktree pending W3), `game-dev-2d` still finishing,
`kumitate 0acb775` (targeted fix pending final review), `kaidoku 5ac7860` (two citation
errata owed). The physical pin set is the 21 original lane directories:
`audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba,
kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi` — each
`/home/vgpnk/Projects/shokunin/<id>-shokunin`. If a head moves before the report lands,
recapture the OID and re-run both the gate and the SOURCES read; mark the prior row
stale/superseded rather than mixing revisions. If a `--snapshot` is CNE (the gate's
`spawnSync` buffer case reported by the audio seat), record the snapshot CNE separately and
never substitute it with a live-tree pass.

### 7.4 Legacy ledger debt

> Schema conformance is reported against two byte identities, because they differ. Committed
> canonical schema: `kimi-shokunin` @ `<oid>`, blob `<blob>`, sha256 `<sha>` — `<A>/<N>`
> records validate. Amended schema: working-tree bytes sha256 `<sha>` (uncommitted in
> `kimi-shokunin-canon` @ `<oid>`, `+33/−2` vs committed `<blob>`) — `<B>/<N>` validate.
> The delta is exactly the `<K>` `supersedes.entry` records the committed schema rejects but
> `PROTOCOL.md:314-320` authorizes; they are protocol-valid, not legacy vocabulary.
> Under the amended bytes the `<L>` non-conforming records partition as: `<n1>` type-enum
> (`train`×`…`, `craft`×`…`, …), `<n2>` lane-status `closed` (entries `<range>`), `<n3>`
> missing `date`+`type` (entries `<list>`), `<n4>` missing `closed_at` (entry `<i>`), `<n5>`
> `round:null` (entry `<i>`); the classes are disjoint. These are preserved originals:
> `rounds` is append-only (`PROTOCOL.md:314-320`) and `.ufo/history-pin.json` (`k=<k>`,
> sha256 `<sha>`) reproduces and anchors at `<commit>`; `<p>` debt record(s) lie inside the
> pinned prefix. This is structural only and does not clear the semantic ledger defects
> recorded in W1 `manifest.md` §3.

### 7.5 Gate and census claims

> `corpus-gate-v1` (`node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> <OID> --round
> 12 --json`) mechanically implements r2, r4, r7, r8-literal, r10, and SHONEN **form**. It
> declares r1, r3, r5, r6, r9, box-3 verifier independence, and SHONEN **truth** not
> evaluated (gate header `:88-108`, registry `not_evaluated` `:177-186`). A pass is a
> rule-level result for the graded committed tree, not whole-corpus semantic conformance.

> Census is provisional: parser `<blob>/<sha>` (corrected indentation), captured at
> `<OIDs>`. `FINAL LANES READY` has not been received; these totals are a pre-signal baseline
> and are superseded by the post-signal run. The aggregate worktree's own
> `scripts/sources-census.sh` is stale (`aed9ed65…`) relative to fleet HEAD
> (`a621fe0e…`); the final run must name which bytes it used.

### 7.6 SHONEN and Sources & frontier for the aggregator

The main repo has no `SHONEN.md`; the round-11 precedent is report-local author assessments
under a `SHONEN` heading, all `[~]` with pointers because no independent non-author verifier
exists (`reports/round-11/aggregator.md:171-187`). Do not invent `[x]` marks.

> `SOURCES: unchanged — main-repo lanes hold no corpus/` (`PROTOCOL.md:156-160`).

### 7.7 Ledger refresh

If the report adds schema-debt findings to `.ufo/reports/AGGREGATE.md`, append a new refresh
section (next would be §16) and continue the queue at **D-156** (max observed `D-155`; no
schema-debt row exists for the 106/45 classes). Own the row to protocol/integrator/operator,
not to the aggregator; do not renumber or mint parallel keys. If the ledger is not refreshed,
the report must say why no row changed (`PROTOCOL.md:340-341`).

## 8. Forbidden phrasings (do not ship)

- "The ledger conforms" / "schema-clean ledger" / "all records validate" — 106 records do
  not, at HEAD, under either schema byte set.
- "206/312 records conform" without the revision and schema-byte identity — stale at HEAD
  (208/314) and ambiguous about `supersedes.entry`.
- "Current schema" or "canonical schema" for the uncommitted `d6fc5f0a…` bytes.
- "All new entries validate" — nine `craft` entries dated 2026-10-19 do not.
- "The 45 entry records were legacy violations" — they are protocol-valid; the committed
  schema lags the protocol.
- "The runtime passes/validates the ledger" without the exact command, exit code, and
  `debt/contradictions/cne/nonclosure` counts; 80 `unknown_entry_type` CNE are expected
  (75 named legacy types + 5 type-absent rows).
- "Corrections fixed the old records" — corrections supersede lane rows; they do not change
  a record's `type`/`round`/missing fields, and filed bytes are never rewritten.
- "The gate/census proves the whole corpus is conformant" — the gate declares the semantic
  and history rules not evaluated; census counts rows, not source truth.
- Any final census total before `FINAL LANES READY`.
- Any edit to the canonical enum, the history pin, `rounds` originals, the root ledgers,
  `MANIFEST.json`, `PROTOCOL*.md`, scripts, or gates by a seat.

## 9. Limits and residual risk

- **No project gate, test, census, build, lint, or formatting run was made by this seat.** The
  runtime and corpus-gate claims above are code/registry inspection plus the parent's
  statement; the 45 supersedes resolutions and all schema counts were computed read-only. A
  generic `check-jsonschema` validation of the manifest was run (it is not a project gate and
  creates no artifact); its outputs are in §10.4.
- **Validator identity.** `check-jsonschema 0.38.2` was available at
  `/home/vgpnk/.local/bin/check-jsonschema`; Python `jsonschema` is absent
  (`ModuleNotFoundError`), and Node `require('ajv')` fails. The authoritative counts are the
  `check-jsonschema` runs; a stdlib walk was used as a cross-check and reproduced them
  exactly. `format: date`/`date-time` assertions may be annotation-only in some validator
  configurations; the only `closed_at` failure here is a `null`, which fails required-type
  regardless.
- **HEAD motion.** The fleet root moved from `dcf3b64` (312) to `b38d358` (314) during this
  observation. Any report sentence that quotes 206/312 must either pin `dcf3b64` explicitly
  or restate the current 208/314. The two appended rows are valid closures and do not change
  the 106.
- **Wave completeness.** 28 seat notes existed at observation against 32 planned seats; the
  report must check the full set and not treat missing notes as clean.
- **Schema commit risk.** The amended schema is uncommitted in a separate worktree; if that
  worktree is cleaned or the edit is lost, the 208 figure loses its byte identity. The
  committed canonical schema remains the only durable schema artifact today.
- **Retired worktrees.** This note uses original lane paths and named commits only; no retired
  `.tower/worktrees/kaika/<lane>-shokunin` path is evidence.

## 10. Exact commands, observed outputs, exit codes

All commands run read-only from the paths shown. `jq` is jaq 3.1.1; Python 3.14.7;
git 2.55.0; check-jsonschema 0.38.2. Abbreviated outputs are marked.

### 10.1 Revisions and ancestry

```sh
$ git -C /home/vgpnk/Projects/shokunin rev-parse HEAD
b38d358ef302d893d4c2c6fe9e1dd6c524275cfb          # exit 0
$ git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate rev-parse HEAD
ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2          # exit 0
$ git -C /home/vgpnk/Projects/shokunin merge-base --is-ancestor \
    ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2 HEAD ; echo $?
0
$ git -C /home/vgpnk/Projects/shokunin status --short
 M README.md                                       # exit 0 (parent edit, not this seat)
$ git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate status --short
?? .ufo/waves/kaika-aggregate/                     # exit 0 (wave seat notes, untracked)
```

### 10.2 Artifact pins

Shell paths used below (absolute; set once):

```sh
FR=/home/vgpnk/Projects/shokunin
WT=/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
KANON=/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon
SCHEMA_WT=$KANON/templates/MANIFEST.schema.json
SCHEMA_CANON=/home/vgpnk/Projects/kimi-shokunin/templates/MANIFEST.schema.json
```

```sh
$ git -C "$FR" rev-parse HEAD:MANIFEST.json \
    HEAD:.ufo/history-pin.json HEAD:PROTOCOL.md \
    HEAD:.ufo/waves/round-15/closure-check.py \
    HEAD:.ufo/waves/round-9/corpus-gate.mjs HEAD:scripts/sources-census.sh
e6403816a074ccc8022684ff180e08797e3d030c
03b9be29bf122324cd824a82377e4429b3ea299d
74bdc54d306fb96183c59155f056c3b982b32ffa
2e5c0afede78f50f94249b4043d6379b8fd54112
c5e8f29f4fb9f2c28b3acab3e701dd85248098d3
55c886d1f67e41a84db2ac5a97fac591d1f14fe8      # exit 0
$ git -C "$FR" show HEAD:MANIFEST.json | sha256sum
de481567aaa629a16e955be3777e1d39e36f9dcb3d6e3062890d471d029a7b08  -   # exit 0
$ jq '.rounds|length' "$FR/MANIFEST.json"
314                                               # exit 0
$ git -C "$WT" show dcf3b64:MANIFEST.json | sha256sum
bf475275fabe90cf92f2251e06b4a96959a9fcbc481b9d589103e749fc4bf61a  -   # exit 0
$ git -C "$WT" rev-parse dcf3b64:MANIFEST.json
7ac0c5f1090a1f8388dd0bd04234eb36a95bc610        # exit 0
$ jq '[.rounds[]|select((.supersedes|type)=="object" and
      (.supersedes|has("entry")))]|length' "$FR/MANIFEST.json"
45                                                # exit 0
$ sha256sum "$WT/.ufo/waves/round-15/closure-check.py" \
    "$WT/.ufo/waves/round-9/corpus-gate.mjs" "$WT/.ufo/reports/AGGREGATE.md"
0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c  .../closure-check.py
e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3  .../corpus-gate.mjs
94ab5f6b03cb493a7e50ccd4fef92fd1e199d1a59ea68110d0cd08937ad84523  .../AGGREGATE.md
                                                  # exit 0 (operand paths abbreviated here)
$ grep -cE '^\| D-' "$WT/.ufo/reports/AGGREGATE.md"
165
$ grep -oE '^\| D-[0-9]+' "$WT/.ufo/reports/AGGREGATE.md" \
    | sed 's/[^0-9]//g' | sort -n | tail -1
155                                               # exit 0
```

### 10.3 Schema identity

```sh
$ sha256sum "$SCHEMA_CANON"
6bd93af2c9dc59606b7c1ce310a3e4bfbf38bbf5093a51a7b97a0f2b105e43d8  $SCHEMA_CANON
$ git -C /home/vgpnk/Projects/kimi-shokunin rev-parse HEAD:templates/MANIFEST.schema.json
5eae1063ffef73c7ceddfa26f013334a2463278a        # exit 0
$ git -C /home/vgpnk/Projects/kimi-shokunin status --short -- templates/MANIFEST.schema.json
                                                  # empty, exit 0 (clean)
$ sha256sum "$SCHEMA_WT"
d6fc5f0a39122471cd1576910975d9649f7e2150582de723c29eac21d57c995c  $SCHEMA_WT
$ git -C "$KANON" status --short -- templates/MANIFEST.schema.json
 M templates/MANIFEST.schema.json                 # exit 0 (dirty)
$ git -C "$KANON" rev-parse HEAD
b3ca98f93859d54519425b5a594ed70b62361a33        # exit 0
$ git -C "$KANON" diff --stat -- templates/MANIFEST.schema.json
 templates/MANIFEST.schema.json | 35 +++++++++++++++++++++++++++++++++--
 1 file changed, 33 insertions(+), 2 deletions(-)   # exit 0
```

### 10.4 Authoritative schema counts

`check-jsonschema` exit 1 means "invalid" (expected here). `pipe-exit` is the
`check-jsonschema` status under `set -o pipefail` (the final `jq` would otherwise mask it).
Failing entries are unique `$.rounds[i]` paths in the JSON output.

```sh
$ command -v check-jsonschema
/home/vgpnk/.local/bin/check-jsonschema          # exit 0
$ python3 -c "import jsonschema" 2>&1 | tail -1
ModuleNotFoundError: No module named 'jsonschema' # python exit 1
$ node -e "require('ajv')" 2>&1 | grep -m1 "Cannot find module"
Error: Cannot find module 'ajv'                   # node exit 1
```

```sh
$ set -o pipefail
$ MAN="$FR/MANIFEST.json"
$ check-jsonschema --output-format json --schemafile "$SCHEMA_WT" "$MAN" \
    | jq -r '[.errors[]|.path|capture("\\$\\.rounds\\[(?<i>[0-9]+)\\]").i|tonumber]|unique|length'
106          # total 314 → 208 valid; amended schema
$ echo "pipe-exit=$?"
pipe-exit=1
$ check-jsonschema --output-format json --schemafile "$SCHEMA_CANON" "$MAN" \
    | jq -r '[.errors[]|.path|capture("\\$\\.rounds\\[(?<i>[0-9]+)\\]").i|tonumber]|unique|length'
151          # total 314 → 163 valid; committed schema
$ echo "pipe-exit=$?"
pipe-exit=1
$ check-jsonschema --output-format json --schemafile "$SCHEMA_WT" \
    <(git -C "$WT" show dcf3b64:MANIFEST.json) \
    | jq -r '[.errors[]|.path|capture("\\$\\.rounds\\[(?<i>[0-9]+)\\]").i|tonumber]|unique|length'
106          # total 312 → 206 valid; the parent's quoted ratio
$ echo "pipe-exit=$?"
pipe-exit=1
```

Error distribution (same three runs):

```
amended @314:  train 63 · closed 24 · craft 9 · date 5 · type 5 ·
               train+audit 2 · closed_at 1 · train+audit+unlock 1 · round:null 1
committed @314: the same 106 plus 45 × "Additional properties are not allowed
               ('entry' was unexpected)"
amended @312:  identical to amended @314 (106 unique failing entries)
```

The same five constraint classes were cross-checked with an in-session stdlib walk
(`json`/`re`/`datetime`, Python 3.14.7); the authoritative values are the
`check-jsonschema` runs above. The walk reproduced 208/106, 163/151, and 106/206 and the
disjoint class counts (75/24/5/1/1).

### 10.5 History pin reproduction

```sh
$ jq -r '.k, .sha256, .manifest_commit' "$WT/.ufo/history-pin.json"
48
ce97497ed699a8f0939be062d042cf4d6e3e7531116fbe4681593991d67f0a8e
ae19fca
$ echo $?
0
$ python3 - <<'PY'   # cwd: $WT
import json, hashlib, subprocess
repo = '/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate'
rounds = json.load(open(repo + '/MANIFEST.json'))['rounds']
canon = lambda o: hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
pin = json.load(open(repo + '/.ufo/history-pin.json'))
print('k', pin['k'])
print('want', pin['sha256'])
print('current', canon(rounds[:pin['k']]))
anchor = json.loads(subprocess.check_output(['git', '-C', repo, 'show', pin['manifest_commit'] + ':MANIFEST.json']))['rounds'][:pin['k']]
print('anchor', canon(anchor))
print('ancestor', subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', pin['manifest_commit'], 'HEAD']).returncode)
PY
k 48
want ce97497ed699a8f0939be062d042cf4d6e3e7531116fbe4681593991d67f0a8e
current ce97497ed699a8f0939be062d042cf4d6e3e7531116fbe4681593991d67f0a8e
anchor ce97497ed699a8f0939be062d042cf4d6e3e7531116fbe4681593991d67f0a8e
ancestor 0
```

### 10.6 Runtime and gate coverage (code inspection only)

```sh
$ cd "$WT"
$ grep -n "ADJUDICATED_TYPES = \|NONCLOSURE_TYPES = " \
    .ufo/waves/round-15/closure-check.py
98:ADJUDICATED_TYPES = ("closure", "closure-correction", "retroactive-closure")
102:NONCLOSURE_TYPES = ("mint", "scaffold", "work", "ops")
$ grep -n "trends" .ufo/waves/round-15/closure-check.py ; echo $?
1                    # no trends handling
$ grep -n "exit_code = EXIT_DEBT" .ufo/waves/round-15/closure-check.py
1428:    exit_code = EXIT_DEBT if debt else (EXIT_ERROR if cne else EXIT_OK)
$ wc -l .ufo/waves/round-15/closure-check.py
2060                 # exit 0
$ sed -n '88,108p' .ufo/waves/round-9/corpus-gate.mjs
# (output: the "RULES NOT EVALUATED, with the reason" comment block; summarized)
# declares r1,r3,r5,r6,r9 + box-3 independence not evaluated
```

### 10.7 Planned paths and wave state

```sh
$ cd "$WT"
$ test -e .ufo/reports/round-12/aggregator.md ; echo $?
1                    # report path free at observation
$ ls .ufo/waves/kaika-aggregate/seats/ | wc -l
28                   # exit 0; dispatch plans 32 seats
```

### 10.8 Supersedes resolution (45 `entry` + 12 triple)

```sh
$ python3 - <<'PY'   # cwd: $WT
import json, collections
R = json.load(open('MANIFEST.json'))['rounds']
entry = [(i, e['supersedes']['entry']) for i, e in enumerate(R)
         if isinstance(e.get('supersedes'), dict) and 'entry' in e['supersedes']]
ok = 0
targets = collections.Counter()
for i, j in entry:
    su, tgt = R[i]['supersedes'], R[j]
    if tgt.get('round') == su.get('round') and tgt.get('type') == su.get('type') and tgt.get('date') == su.get('date'):
        ok += 1
        targets[tgt.get('type')] += 1
print('supersedes.entry records', len(entry))
print('resolved (entry index + round/type/date match)', ok)
print('target types', dict(targets))
cc = [i for i, e in enumerate(R) if e.get('type') == 'closure-correction']
by_entry = sum(1 for i in cc if isinstance(R[i].get('supersedes'), dict) and 'entry' in R[i]['supersedes'])
by_triple = 0
bad = []
for i in cc:
    su = R[i].get('supersedes') or {}
    if 'entry' in su: continue
    want = (su.get('round'), su.get('type'), su.get('date'))
    matches = [j for j in range(i) if (R[j].get('round'), R[j].get('type'), R[j].get('date')) == want]
    if len(matches) == 1: by_triple += 1
    else: bad.append((i, len(matches)))
print('closure-corrections', len(cc), 'by entry', by_entry, 'by unique earlier triple', by_triple, 'unresolved', bad)
PY
supersedes.entry records 45
resolved (entry index + round/type/date match) 45
target types {'closure-correction': 19, 'closure': 26}
closure-corrections 57 by entry 45 by unique earlier triple 12 unresolved []
```
