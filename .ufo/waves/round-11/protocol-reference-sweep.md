# Round-11 protocol-compaction reference sweep

Read-only scan of the six child repositories, the six named root documents, and `.ufo/reports/` (including all nested corpus/lesson/knowledge files and text scripts). No repository files were changed; no builds or tests were run.

## Evidence and scope

- Executed `functions.grep` searches for literal `PROTOCOL\.md`, `MANIFEST\.json`, and `rounds\[[^]]+\]` across the target roots, with `gitignore=false`; re-executed a non-`.git` text-file scan to count and group exact file:line matches.
- Literal `PROTOCOL.md`: **161 matching lines / 59 files**. Four lines are substring false positives for the unrelated external `SPEEDRUN-PROTOCOL.md` (Kake `SKILL.md:114,240`, `corpus/knowledge/speedrun-pipeline.md:3`, `corpus/lessons/round-5.md:7`). Thus the exact Shokunin protocol references are **157 lines / 56 files**. The table below includes all 161 search hits and labels the four false positives.
- Literal `MANIFEST.json`: **74 matching lines / 30 files**. All file:line groups are listed below.
- Indexed `rounds[...]`: **28 occurrences / 26 matching lines** in scope. The kagi child-repo subtree has **12**, not 13, exact `rounds[1]` occurrences on 12 lines (full locations below). This disagrees with the existing 13-count assertion in root `LOG.md:25` and `.ufo/reports/round-10/protocol.md:64`.
- `MISSION.md` and `AXES.md` returned no literal `PROTOCOL.md`/`MANIFEST.json` hits in the scoped searches.
- The requested path `.ufo/reports/round-2/AGGREGATE.md` is absent in the current tree (the directory scan reported the path missing). `.ufo/reports/AGGREGATE.md` exists and itself refers to the old `round-2` path at lines 555–556; the round-10 protocol report also says the top-level canonical path does not exist at lines 177–178. Treat these as conflicting/stale path claims, not as active section anchors.

## Reference table — `PROTOCOL.md` search hits

Line numbers in the first column are the referencing files' lines; any `PROTOCOL.md:NNN` in the third column is a line citation into the protocol and is especially fragile. Grouped lines enumerate every exact search hit in that file. Kinds: **bare** = filename/name only; **section** = named section/step/table; **line** = protocol line-number citation; **quote** = quoted or phrase-level wording.

| Referencing file:line(s) | Kind | What it needs from `PROTOCOL.md` |
|---|---|---|
| `kagi-shokunin/LOG.md:145` | section + quote | Preserve `Evidence standard` and the “pins verifiable for only 2 of 13 files” incident wording/findability. |
| `kagi-shokunin/SCORECARD.md:19–20` | line + rule reference + quote | `:19` cites `PROTOCOL.md:292–298` for the pin count and quotes “pins verifiable for only 2 of 13 files”; `:20` depends on the rule that unverified lane `[x]` marks count as `[~]`. |
| `kagi-shokunin/SKILL.md:187` | section + quote | Preserve `Evidence standard` and the “fingerprint printer with no stored baseline” counterexample. |
| `kagi-shokunin/corpus/knowledge/drift-gate.md:5,14` | section + line + quote | `:5` names `Evidence standard` and cites `L292–298`; `:14` quotes “a pin only counts if its expected values are persisted inside the repo.” |
| `kagi-shokunin/corpus/lessons/round-1-aggregator-seed.md:89,99,101` | bare + section/rule | `:89` append-only `LOG.md` corrections; `:99` `Invariants`/contested-scope rule; `:101` dormancy threshold. |
| `kagi-shokunin/corpus/lessons/round-5-aggregator-audit.md:51` | bare + rule | Author-only `[x]` marks are not verified; preserve the promotion-mark semantics. |
| `kagi-shokunin/corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:5` | section/step + quote | Preserve integrator step 2 routing and aggregator mirroring of routed sibling defects into aggregator-owned `corpus/lessons/` files. |
| `kagi-shokunin/corpus/lessons/round-9.md:7` | section + quote | Preserve `Evidence standard`, committed-pin requirement, and the baseline-free fingerprint-printer example. |
| `kagi-shokunin/corpus/lessons/round-6-aggregator-audit.md:9,43,84,98,120,134,139,143,199` | bare + line + section/quote | `:9` is a snapshot note. Line cites: `:43` `453–454` (pin claim); `:84` `469–476` (canonical seed); `:98` `43–47` (non-author verifier); `:120,:199` `466` (scorecard evidence); `:134` `486–490` (contested-scope rule); `:139` `535–548` and `:143` `537–538` (lane/main-repo identity). Several are already stale against current text; remap to semantic anchors, not new raw numbers. |
| `kake-shokunin/SKILL.md:114,240`; `kake-shokunin/corpus/knowledge/speedrun-pipeline.md:3`; `kake-shokunin/corpus/lessons/round-5.md:7` | false-positive bare | These are references to the external `SPEEDRUN-PROTOCOL.md`, not this repo’s `PROTOCOL.md`; no Shokunin anchor is required. |
| `kake-shokunin/corpus/lessons/round-1-aggregator-audit.md:11,75` | bare + rule | `:11` relies on report-path/naming requirements; `:75` on the contested-scope invariant. |
| `kake-shokunin/corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:5` | section/step + quote | Preserve integrator step 2 route/mirror duty. |
| `kake-shokunin/corpus/lessons/round-5-aggregator-audit.md:24` | quote | Preserve the exact evidence rule: “A status command printing configured values is not evidence of capability.” |
| `kake-shokunin/corpus/lessons/round-6-aggregator-audit.md:8–9,98,107,134` | bare + line + file-contract rule | `:8–9` snapshot/version note; `:98,:134` cite `502–503` for lane identity; `:107` relies on the scorecard contract row. Keep the claim semantics, not those obsolete line positions. |
| `kasegi-shokunin/corpus/lessons/round-1-aggregator-audit.md:9,70` | bare + rule | Append-only correction discipline and contested-scope arbitration. |
| `kasegi-shokunin/corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:5` | section/step + quote | Preserve integrator step 2 route/mirror duty. |
| `kasegi-shokunin/corpus/lessons/round-6-aggregator-audit.md:10–11,93` | bare + line | `:10–11` snapshot note; `:93` cites `PROTOCOL.md:394` for `/tmp` evidence rejection. Current line 394 is the aggregator commit rule, so this line citation is already stale; retain the closure-time evidence rule under `Evidence standard`. |
| `kengaku-shokunin/SKILL.md:408` | bare + rule | The closure-resolvable evidence rule rejects ephemeral `/tmp` workdirs as durable evidence. |
| `kengaku-shokunin/LOG.md:14–15` | bare + rule | References protocol-lane work and aggregator-owned correction/commit policy; filename mention has no numeric anchor. |
| `kengaku-shokunin/SCORECARD.md:56,60` | bare + file-contract/scorecard rule | Preserve protocol-governed score evidence and aggregator-owned corpus-file ownership. |
| `kengaku-shokunin/corpus/README.md:43,47` | bare + section + rule | `:43` aggregator commits its own lesson; `:47` explicitly names `Evidence standard` and rejects `/tmp` closure pointers. |
| `kengaku-shokunin/corpus/knowledge/bench-arena-round7-noise-n25.md:89` | quote + invariant | Preserve “corpus corrections are new entries” append-only rule. |
| `kengaku-shokunin/corpus/lessons/round-1-aggregator-audit.md:60` | quote/rule | Promotion gate includes the `PROVINCE.md` reality check; keep the actual gate wording. |
| `kengaku-shokunin/corpus/lessons/round-8.md:14` | section + quote | Preserve `Evidence standard` and the rule that `/tmp` pointers are not evidence at closure. |
| `kengaku-shokunin/corpus/lessons/round-9.md:55` | file-contract + quote | Preserve the file-contract canonical seed and verbatim-diff constraint (“no other prose, added boxes, or removed boxes”). |
| `kengaku-shokunin/corpus/lessons/round-6-aggregator-audit.md:155` | section + quoted label | Preserve the four-box `canonical SHONEN.md seed` block and exact box count. |
| `kengaku-shokunin/corpus/evidence/round9-fleet/sibling-overlap.md:16–17,27` | line | Cites `247–273,300–309` (evidence/report/closure duties) and `226–245` (integrator/aggregator assignment); remap to named sections/steps. |
| `kotoba-shokunin/LOG.md:23,94` | bare + rule | File-contract table and round-6 promotion-mark rule; preserve semantics and non-author verification. |
| `kotoba-shokunin/SCORECARD.md:5` | bare + Fleet-2 convention | Preserve the `Fleet-2 conventions` axis-score evidence rule. |
| `kotoba-shokunin/corpus/knowledge/dispatch-prompt-audit-round7.md:62` | line | Cites `PROTOCOL.md:101–102` for report-path acceptance; current lines are prompt-fidelity text, so the old citation is stale. Preserve the actual report path contract and step labels. |
| `kotoba-shokunin/corpus/lessons/round-5-aggregator-audit.md:16` | quote | Preserve “a subagent the lane dispatched is still the lane.” |
| `kotoba-shokunin/corpus/lessons/round-6-aggregator-audit.md:11–12,46,89,128` | bare + line | `:11–12` snapshot; `:46` explicitly extracts `PROTOCOL.md` seed lines `439–446`; `:89,:128` cite `502–503` for lane identity. Re-anchor the seed/identity clauses semantically. |
| `kotoba-shokunin/corpus/lessons/round-10.md:90,133` | quote + rule | `:90` relies on “commits are cited by hash” (not subject/tag); `:133` relies on `/tmp` not being durable evidence. |
| `kumitate-shokunin/scripts/cite-check.mjs:108` | bare | Protocol filename is one member of a checked-document allowlist; requires the file name to remain, no section anchor. |
| `kumitate-shokunin/corpus/lessons/round-5-aggregator-mirror-out-of-province-membrane-seal.md:5,24` | section/step + rule | `:5` integrator step 2 routing; `:24` lane write-scope boundary (own child repo + report) and integrator disposition. |
| `kumitate-shokunin/corpus/lessons/round-6-aggregator-audit.md:8` | bare | Snapshot/version note; the file name is the reference. |
| `.ufo/reports/AGGREGATE.md:10,50,128,130,154,182,194,201,203,231,252,275,282,377,477,520,552,555` | bare + section + quote/rule | Includes report/file requirements, `Promotion gates`, schema and step-3 mint threshold, `Evidence standard`, and canonical-ledger location. `:203` explicitly names “Promotion gates”; `:477` names `Evidence standard`; `:520–522` quotes the mint bar but omits “unplaceable” from the current protocol wording; `:555` points at the canonical ledger path. |
| `.ufo/reports/round-1/protocol.md:3,5,47,66,74` | bare + write-scope | Historical protocol file/edit references; `:47` requires integrator ownership of `MANIFEST.json`/`PROTOCOL.md`/`ROADMAP.md`; `:66` seed drift. |
| `.ufo/reports/round-3/protocol.md:5,66`; `.ufo/reports/round-4/protocol.md:4,66`; `.ufo/reports/round-5/protocol.md:4,114`; `.ufo/reports/round-6/protocol.md:4,136`; `.ufo/reports/round-7/protocol.md:5,116`; `.ufo/reports/round-8/protocol.md:5,117` | bare | Historical “edited/not touched `PROTOCOL.md`” inventory references; they require the file identity, not a heading or stable line. |
| `.ufo/reports/round-3/kotoba.md:22,34` | file-contract + quote/rule | File-contract/meta-domain carve-out and non-author review; preserve “never self-attestation” meaning. |
| `.ufo/reports/round-3/aggregator.md:4,11,96` | bare + section/rule | Aggregator write-scope exception, contract set, and independent assessment requirement. |
| `.ufo/reports/round-4/aggregator.md:4,14,55,88,154,169` | bare + rule/quote | Current protocol/contract-set references; `:88` names proposals; `:154` quotes mint bar; `:169` relies on the round-6 protocol rule and CORPUS write boundary. |
| `.ufo/reports/round-7/kotoba.md:90,97` | line + rule | `:90` cites `101–102` for `report_of()` filename acceptance; `:97` notes protocol/prompt/generator divergence. Re-anchor report naming and step numbering. |
| `.ufo/reports/round-9/protocol.md:5,46,98,169,172` | bare + section + quote | `:46` names `Integrator of record`; `:98–103` is a report-contract quote labelled verbatim from protocol; `:171` preserves the prompt-conflict phrase “never MANIFEST.json.” |
| `.ufo/reports/round-9/kagi.md:6` | section + quote | `Evidence standard` plus the baseline-free printer / 2-of-13 pin incident. |
| `.ufo/reports/round-9/kengaku.md:5,113,170` | bare + seed + quote | Aggregator-owned commit rule; canonical seed; promotion-gate quote “a subagent the lane dispatched is still the lane.” |
| `.ufo/reports/round-10/protocol.md:9,34,37,170,172,178,237,238,313,336,411,422,425,433,446` | bare + section/step + quote | `:34` `Integrator of record`; `:37` file-contract row; `:178` fallback queue/ledger clause; `:313–316` verbatim report contract; `:336–340` prompt’s closure-step requirements; `:411` step-4 evidence semantics; `:422` closure/freeze semantics; `:446` compaction acceptance. `:170–172,:237–238` are line-count/incident references, not protocol headings. |
| `.ufo/reports/round-10/kotoba.md:163` | section/step | Depends on step-4 closure semantics alongside `MANIFEST.json`; preserve the step label and entry/closure behavior. |
| `ROADMAP.md:24,40,68,115` | bare + rule | Protocol improvement/minting, author-attested marks, and the tracked `.ufo/state`/watchdog historical contradiction. Preserve operative write-scope and mint rules; do not drop the historical context without retaining the resolution. |
| `CORPUS.md:50` | bare + append-only rule | Aggregator correction discipline is explicitly compared with protocol’s `LOG.md` append-only rule. |
| `SCORECARD.md:18,38,41,42,47,53,71` | bare + section/step | Protocol-soundness/compaction plan, file-contract `SCORECARD.md` row, `Fleet-2 conventions` precedence, step-4 closure semantics and marker clause. |
| `LOG.md:8,20,46,55,57` | section + step + bare | `:8` `Invariants`; `:46–49` explicitly `Round-robin rounds`, `Integrator of record`, `Invariants`, `Fleet-2 conventions`; `:55–57` compaction limit and preserve-every-obligation test. |

## Line-number citations that should be replaced with named anchors

The explicit `PROTOCOL.md` line citations in the table are snapshot pointers and will move under compaction. Several already point at unrelated current text, demonstrating that raw numbers are not durable:

- `101–102` is cited for `report_of()` path acceptance, while current `PROTOCOL.md:101–102` is prompt-fidelity text.
- `292–298` is cited for the pin evidence standard, while current `:293–302` is mint/entry-shape content.
- `394` is cited for rejecting `/tmp`, while current `:394` is aggregator commit-scope text.
- `453–454` is cited for the pin count, while current `:453–454` is the commits-by-hash rule.
- `466` is cited for the SCORECARD evidence obligation, while current `:466` is the file-contract table header (the SCORECARD row is now `:473`).
- `486–490` is cited for contested scope, while current `:486–490` is the seed mark rule plus the start of `Invariants`; contested-scope wording is at current `:493–499`.
- `502–503` is cited for lane identity, while current `:502–503` is append-only LOG text; the identity rule is at current `:542–549`.

For the new compact text, cite the preserved heading/phrase plus a revision where needed. Do not attempt to keep these old line numbers valid by padding or placing prose at legacy positions.

## Must-survive anchors

### Heading/label anchors

Preserve these exact protocol heading names where present and retain the named paragraph/block labels that external references use:

- `## Lifecycle` — mint threshold is referenced as `Lifecycle` in `.ufo/reports/AGGREGATE.md:520–522`.
- `## Promotion gates` — cited by Kagi promotion audits, Kengaku lessons, and `.ufo/reports/AGGREGATE.md:203`.
- `## Round-robin rounds` — main `LOG.md:46` names this section for marker/lands-by-lane behavior.
- `## Evidence standard` — cited repeatedly across Kagi, Kake, and Kengaku corpus/evidence files.
- `## File contract per shokunin repo` — used as “file-contract table”/“SCORECARD row” and for the canonical SHONEN seed.
- `## Invariants` — cited by root `LOG.md:8` and child contested-scope/append-only references.
- `## Fleet-2 conventions (adopted)` — cited as `Fleet-2 conventions` for score evidence and MISSION/PROTOCOL precedence.
- `**Integrator of record.**` — not an H2 heading, but explicitly referenced as `§Integrator of record`; keep this exact label.
- `The canonical `SHONEN.md` seed` — not an H2 heading; preserve the label and seed as a verbatim block.

Keep numbered integrator steps discoverable as `step 1` through `step 4`, especially step 2 (route/mirror), step 3 (mint threshold), and step 4 (append/closure entry semantics). `§Conformance record`, `§Routing lines`, `§Template correction`, `§Closure`, and `§Dispatch digest` cited in the root log/scorecard are headings in `.ufo/reports/round-10/protocol.md`, not headings in `PROTOCOL.md`; they must not be mistaken for required protocol headings.

### Phrases/clauses whose wording is quoted or used as a durable search key

Keep these exact phrases, or make the compaction map each one explicitly to a verbatim surviving home:

- “A status command printing configured values is not evidence of capability.” — `Evidence standard`; Kake `round-5-aggregator-audit.md:24` quotes it.
- “a pin only counts if its expected values are persisted inside the repo” — `Evidence standard`; Kagi `drift-gate.md:14` and `round-9.md:8–9` quote it.
- “a fingerprint printer with no stored baseline cannot detect drift” and “pins verifiable for only 2 of 13 files” — cited by Kagi LOG/SCORECARD/lessons and round-9 report as the incident phrase.
- “a subagent the lane dispatched is still the lane” — current promotion rule at `PROTOCOL.md:40–41`; Kotoba/Kengaku quote it.
- “Commits are cited by hash, never by subject or tag” — current evidence rule at `:453–454`; Kotoba `round-10.md:90` depends on it.
- “the counting command that produced it and the commit it was measured against” — SCORECARD file-contract row; Kagi `round-6-aggregator-audit.md:120` quotes it.
- “silence is not a ruling and must never default to whichever lane wrote first” — contested-scope invariant; Kagi/Kake audit citations rely on this exact ruling.
- Lane identity strings `<lane>-shokunin` / `<lane>@shokunin.local`, plus the rule that an unconfigured lane sets `git config user.name/email` and records it in `LOG.md`; cited by Kagi/Kake/Kotoba identity audits.
- The report contract: report lands last, after child-repo work is committed; it cites that commit’s hash; that hash remains an ancestor of `HEAD`; never amend a cited commit; report is committed by the lane. Round-9 and round-10 reports label this text verbatim from the protocol.
- The canonical SHONEN seed’s four boxes, only `<name>` substitution, exact mark form (`[x] <verifier>` / `[~]` with pointer), and “no other prose, added boxes, or removed boxes.”
- Mint threshold: **two documented *unplaceable* demand instances or an explicit operator directive** (current `Lifecycle`/step-3 wording). `.ufo/reports/AGGREGATE.md:520–522` quotes a shortened form that omits “unplaceable”; preserve/correct to the protocol’s exact threshold, not that omission.
- Closure-time evidence durability: `/tmp`, `/dev/shm`, session-scoped artifacts are not evidence at closure; child references cite this as the durable-evidence rule.
- Integrator step-2 routing and aggregator ledger/fallback rule; closure steps 1–4; step-4 partial-entry/status/`closed_at` semantics; and the marker-vs-defective-report distinction referenced from root `LOG.md` and round-10 reports.
- Main-repo write-scope / operator-side distinction, including the `.ufo/state`/`watchdog.log` historical “stay untracked” contradiction and the current no-lane-commit rule; Roadmap `:115` depends on this context.

## `MANIFEST.json` reference table

All 74 literal `MANIFEST.json` hit lines, grouped by file. **Bare** means only the filename is mentioned; **index/schema** means the reference depends on `rounds` structure, indexed location, append/correction semantics, or step-4 closure rules.

| Referencing file:line(s) | Kind / dependency |
|---|---|
| `kagi-shokunin/LOG.md:4` | index: `rounds[1].lanes.kagi` historical status. |
| `kagi-shokunin/corpus/README.md:5,24,26` | bare + index: round-1 deferral/status and corpus index evidence. |
| `kagi-shokunin/corpus/lessons/round-1-aggregator-audit.md:13` | index: round-1 citation conformance. |
| `kagi-shokunin/corpus/lessons/round-1-aggregator-seed.md:10,17` | index/schema: `rounds[1]` plus the earlier fractional ops row. |
| `kagi-shokunin/corpus/lessons/round-1.md:3,36` | index + bare: round-1 deferral and requirement to cite MANIFEST, including non-successes. |
| `kagi-shokunin/corpus/lessons/round-4-aggregator-audit.md:35,63` | index: valid `lanes.kagi` citation vs the obsolete `.deferred` key. |
| `kotoba-shokunin/corpus/knowledge/agents-md-and-dispatch-surfaces.md:45` | bare filename in a scope fence. |
| `kotoba-shokunin/corpus/knowledge/alwayson-checklist-round7.md:62` | bare search/producer inventory. |
| `kumitate-shokunin/scripts/cite-check.mjs:108` | bare filename in checked-doc allowlist. |
| `.ufo/reports/AGGREGATE.md:10,152,154,182,262,273` | bare + historical rounds schema/index/status; reference includes the obsolete `rounds[1].deferred` defect. |
| `.ufo/reports/round-1/kotoba.md:35`; `.ufo/reports/round-1/kengaku-shokunin.md:38` | bare “not touched” inventory references. |
| `.ufo/reports/round-1/protocol.md:17,24,43,44,46,47,75` | rank canonicality, rounds schema, write-scope, and historical not-touched references. |
| `.ufo/reports/round-3/protocol.md:67`; `.ufo/reports/round-3/kengaku.md:39`; `.ufo/reports/round-4/protocol.md:67` | bare not-touched inventory references. |
| `.ufo/reports/round-3/aggregator.md:12,78` | contract-set read and obsolete round-1 indexed-key defect. |
| `.ufo/reports/round-4/aggregator.md:15,55` | contract-set read / not-touched inventory. |
| `.ufo/reports/round-2/kagi.md:43` | bare indexed manifest item in round-2 evidence inventory. |
| `.ufo/reports/round-5/protocol.md:49,115` | rounds-entry absence claim and not-touched inventory. |
| `.ufo/reports/round-6/protocol.md:115,137`; `.ufo/reports/round-7/protocol.md:94,117`; `.ufo/reports/round-8/protocol.md:99,118` | rounds schema/state plus not-touched inventory. |
| `.ufo/reports/round-7/kotoba.md:84` | bare producer/scope search. |
| `.ufo/reports/round-9/protocol.md:6,16,19,169,171` | integrator rounds append/write authority, historical array contents, and snapshot-clause resolution of “never MANIFEST.json.” |
| `.ufo/reports/round-10/protocol.md:9,25,63,218,337,378,396,422,426,434,438` | rounds closure/index, step-4 workflow, manifest consumer search, prompt instructions, freeze/closure, and edit-scope references. |
| `.ufo/reports/round-10/kotoba.md:163` | step-4 closure artifact paired with PROTOCOL. |
| `ROADMAP.md:14,27` | canonical rank source and per-round closure entry requirement. |
| `SCORECARD.md:17,26,40,70` | closure metrics, `rounds[]` shape/identifiability, and cited round-10 evidence. |
| `LOG.md:6,14,41,46,52` | rounds as evidence store, historical contents, append-only entry count, evidence ranges, JSON/status validation. |

### Indexed `rounds[...]` constraints and exact sites

The re-executed literal scan found these **12** current `rounds[1]` occurrences inside `kagi-shokunin/`:

- `kagi-shokunin/LOG.md:4,15`
- `kagi-shokunin/corpus/README.md:6,24,26`
- `kagi-shokunin/corpus/lessons/round-1-aggregator-audit.md:13`
- `kagi-shokunin/corpus/lessons/round-1-aggregator-seed.md:10–11`
- `kagi-shokunin/corpus/lessons/round-1.md:3`
- `kagi-shokunin/corpus/lessons/round-4-aggregator-audit.md:35,63–64`

`MANIFEST.json:14–16` shows `rounds[0]` is round 0 and `rounds[1]` is the round-1 `work` entry. Preserve array order and append corrections only; do not insert, reorder, or rewrite entries. The two historical `rounds[1].deferred` sites (`kagi-shokunin/LOG.md:15`, `round-4-aggregator-audit.md:63`) refer to a nonexistent/obsolete key and are themselves evidence of the old citation defect; the corrected `lanes.kagi` spelling appears at the companion lines. The round-1 closure-correction entry is appended later, so `rounds[1]` remains a stable pointer to the original entry, not the last-wins terminal status.

Other indexed occurrences in scope (28 total occurrences / 26 lines) are: `.ufo/reports/AGGREGATE.md:262,264,273,465` (two occurrences on `:465`); `.ufo/reports/round-3/aggregator.md:78,80`; `.ufo/reports/round-2/kagi.md:31` (two occurrences),`:43`; `.ufo/reports/round-10/protocol.md:63,64,417`; root `LOG.md:25,42,46` (`:46` is the range `rounds[4..14]`). Preserve append-only order and closure-correction semantics for those as well; the bracket citations are history pointers, not a license to mutate prior rows.

## Noteworthy stale/broken references

- The asserted 13 kagi `rounds[1]` citations is not reproduced: the current subtree has 12 literal matches. The list printed in `.ufo/reports/round-10/protocol.md:64–67` itself names 11 sites and omits `kagi-shokunin/LOG.md:15`; adding that omitted line yields 12, not 13. Reconcile the count in the next permitted edit rather than carrying forward 13.
- `.ufo/reports/AGGREGATE.md:555–556` calls `.ufo/reports/round-2/AGGREGATE.md` “this file,” but that path is absent in the current tree. `.ufo/reports/round-10/protocol.md:177–178` says the current `.ufo/reports/AGGREGATE.md` is absent; that file is present now. These are file-path/state discrepancies, not anchors that compaction can solve by renaming a heading.
- Round-10 report references `§Conformance record` / `§Routing lines` describe its own report sections. They do not require `Conformance record` or `Routing lines` headings in `PROTOCOL.md`.
