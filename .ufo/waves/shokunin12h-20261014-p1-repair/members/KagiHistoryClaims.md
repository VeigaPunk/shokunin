# KagiHistoryClaims — advisory inventory

Seat: history claims only. Not a native judge verdict, lane round report, receipt, or admission. No lane file, gate file, LOG, corpus note, SCORECARD, or sibling report was edited. No stage, commit, or push.

Measured revision: `fecee8743e52eb8fb5fbb40782934cb619a1a96e` (`git rev-parse HEAD`), matching `baselines.json` kagi.head. `git status --porcelain` shows only untracked `plans/` (parent WWKD; not this seat). Starting citation-gate receipt, not re-run here: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kagi-before.json` argv `bash corpus/claim-ledger.sh citations`, exit 0, `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)`.

Axes touched by this inventory: freshness (deleted vs historical cites), operability (current how-to counts), calibration (hash and placeholder overclaims), adjacency (lane-root description vs script-derived resolution). No scalar.

## Method

Read-only. Host paths were existence-tested only (`test -e`); no secret, session, oauth, token, or `op.env` content was opened. In-repo sha256/line counts were computed for lane files already named by the notes. Gate scripts were not executed.

## Cluster table

| id | class | classification | why |
|---|---|---|---|
| HC-01 | origin-tree / `--src` | superseded historical | re-measured empty; round-18 erratum still holds |
| HC-02 | PROVINCE surface list | superseded historical | round-18 caption already marks the list historical; bytes preserved |
| HC-03 | SKILL falsification round bullets | superseded historical | `SKILL.md:555-558` already says those numbers are history |
| HC-04 | in-repo pins that still match | live and current | not superseded; do not erratum them into history |
| HC-05 | frozen-wave script pin in `claim-ledger.md` | superseded historical | explicitly "at the frozen wave revision"; current stamp delegated to `stamps.tsv` |
| HC-06 | labeled dead cites (gate `labeled=13`) | superseded historical | marker is on the citing line; targets still absent or session-scoped |
| HC-07 | janitor host paths in SKILL/knowledge | unresolved live | PROVINCE caption does not reach these lines; files are absent |
| HC-08 | content-hash prefixes of missing files | unresolved live | asserted as source basis; scorecard says they are not asserted |
| HC-09 | SKILL current stamp/selftest counts | live | decision table and how-to comment, not under the history rule |
| HC-10 | lowercase `~/projects/shokunin` as current root | live | path absent; script no longer uses it; two notes still do |
| HC-11 | round-13 `<FILL ON STAMP>` | unresolved live | placeholder never filled; lesson is append-only |
| HC-12 | surviving `opencode.json` | out of this seat | file exists; line/symbol/hash drift belongs to LiveAnchors |

## HC-01 — origin-tree / `--src` (superseded historical)

`git grep -F -e origin-work/ -e ufo-fsd-alpha/ -e UFO_SRC -e ~/Projects/ufo -e /home/vgpnk/Projects/origin-work HEAD -- SKILL.md PROVINCE.md corpus` → no hits.

`origin-work` / `ufo-fsd` hits are the negative-sweep sentence itself (`LOG.md:725`, `SCORECARD.md:314`, `corpus/lessons/round-18.md:7`, `corpus/README.md:75`, `corpus/knowledge/substrate-deferral.md:3`). `--src` appears only as the class name (`corpus/lessons/round-18.md:9,66`, `corpus/README.md:75`).

Round-18 already recorded a/b/c = 0. Re-measurement agrees. No new erratum. Do not invent an origin-tree repair.

## HC-02 — PROVINCE surface list (superseded historical)

`PROVINCE.md:10-17` is the round-18 caption: surfaces below are HISTORICAL; unblock is reinstall, then every pin re-verifies in one run. The list at `:19-43` is preserved verbatim. That is the landed describe-don't-pin marking. Do not rewrite it.

Host re-measure of `corpus/drift-baseline.tsv` path column (15 rows): 14 absent, 1 present.

Present: `$HOME/.config/opencode/opencode.json` (see HC-12).

Absent: `$HOME/.local/bin/the-janitor`, `$HOME/.config/the-janitor/{client.py,opencode.json,config.json,op.env}`, `$HOME/.config/opencode/agents/janitor.md`, `$HOME/.config/opencode/tools/janitor_auth.ts`, `$HOME/.config/opencode/plugin/fnm-nudge.js`, `$HOME/.local/bin/tac-check`, `$HOME/.local/state/tac/daybreak-blue-access.json`, `$HOME/.local/state/the-janitor/tac-daybreak-blue.json`, `$HOME/.local/state/tac/handoff-status.json`, `$HOME/.agents/AGENTS.md`, `$HOME/.local/share/the-musketeer/chrome-profile/NativeMessagingHosts/com.1password.1password.json`.

`corpus/surface-census.tsv` path column: 34 absent, 1 present (same `opencode.json`). `/home/vgpnk/projects` is absent; `/home/vgpnk/Projects` exists.

## HC-03 — SKILL round bullets (superseded historical)

`SKILL.md:555-558` already states that each falsification bullet is the measurement at that round's revision and that current figures come from the gate verdict, not the narrative. Under that rule, these are history, not current pins:

- `:604-608` round-9 `DRIFT_PINS: CLEAN (files=15 symbols=19)` and the `deadbeef0b7e->2408b0c90b7e` falsifier
- `:627-628` round-11 `CLAIM_LEDGER: CLEAN (claims=11 stamped=28)` and `SELFTEST: PASS (39 cases)`
- `:649-650` round-14 `DOC_AUDIT: CLEAN (entries=17 row_linked=14 …)`

`:249-250` "18 rows as of round 14" is dated. Leave these bytes. No second marking inside the falsification section.

## HC-04 — pins that still match (live and current)

Do not describe these as superseded. A describe-don't-pin mark here would falsify a still-true pin.

- `corpus/drift-pins.sh`: 451 lines, sha256 prefix `c138d34c7f0dfe95` … suffix `0feb`. Matches `corpus/knowledge/drift-gate.md:3` and `corpus/stamps.tsv`.
- `corpus/transcript-scan.sh`: 282 lines, sha256 prefix `2d60981b198cef41` … suffix `3a23`. Matches `corpus/lessons/round-6-aggregator-audit.md:38` and the stamp row.
- Stamp set: 56 non-comment rows in `corpus/stamps.tsv`; 35 `R` rows in `corpus/claim-ledger.tsv`. Matches `PROVINCE.md:52` and `corpus/README.md:64-65`. Working-tree sha256 of `corpus/claim-ledger.sh` prefix `93c5827202b9cdec` matches its stamp row (1319 lines, 79301 bytes).

## HC-05 — frozen-wave script pin (superseded historical, already marked)

`corpus/knowledge/claim-ledger.md:4-5` pins `corpus/claim-ledger.sh` at 436 lines, sha256 `d63c60b0821b5388…`, and says that figure is the frozen wave revision and that the shipped revision is `corpus/stamps.tsv`. Current file does not start with `d63c60b0`. The marking is the right pattern. No new erratum for this sentence.

## HC-06 — labeled dead citations (superseded historical)
Before-receipt labeled lines, re-checked as still dead or session-scoped:

- `SKILL.md:293`, `SKILL.md:633` `local://` — session URI, labelled
- `corpus/knowledge/claim-ledger.md:24-25,122-123` `local://` / `artifact://` / `agent://` / `proc://` — labelled
- `corpus/lessons/round-11.md:45,47` `local://round-10/{connector,critic}.md` — labelled scratch
- `corpus/knowledge/claim-ledger.md:132`, `corpus/lessons/round-11.md:71`, `corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:21` `.ufo/reports/round-2/AGGREGATE.md`

That AGGREGATE path is still absent (`test -e` false). `.ufo/reports/AGGREGATE.md` exists. `.ufo/reports/round-2/` exists and contains `kagi.md`, `kaidoku.md`, `kama.md` only. The citing lines already say relocated / labelled. Gate class: unresolved but labelled, so CLEAN. Do not delete the cites. Do not retarget them to the later AGGREGATE file inside the original lessons.

Sibling cites sampled from notes all exist: `kama-shokunin/corpus/knowledge/cross-lane-scope.md`, `kotoba-shokunin/corpus/knowledge/alwayson-checklist-round7.md`, `kotoba-shokunin/corpus/knowledge/fleet-skill-audit-round5.md`, `kake-shokunin/SKILL.md`, `kake-shokunin/corpus/knowledge/mirror-pitfalls.md`, `kake-shokunin/corpus/lessons/round-1-aggregator-audit.md`. Not citation-to-deleted. `.ufo/reports/round-10/protocol.md` exists.

## HC-07 — host paths outside the PROVINCE caption (unresolved live)

The citation gate does not check host paths (`corpus/claim-ledger.sh:442-450` `cite_class` returns non-zero outside corpus, shorthand, `.ufo`, sibling, and root-doc shapes; `corpus/knowledge/claim-ledger.md:116-120`). CLEAN does not cover this class.

Round-18 lesson `:56-62` says all round 9–17 evidence quotes stay verbatim and historical. That sentence is in the lesson, not on the citing lines. A reader of the knowledge source-basis lines still sees a current file identity. Coverage is therefore unresolved, and the claims stay live until an append-only erratum names them. Do not rewrite the source lines.

Representative live cites of absent paths, with no historical marker on the line:

- `corpus/knowledge/handler-on-disk-state.md:3-6` — `~/.local/bin/the-janitor` and `client.py` as source basis
- `corpus/knowledge/handler-trust-boundary.md:3-7` — same, plus `janitor.md`, `janitor_auth.ts`, `fnm-nudge.js`
- `corpus/knowledge/janitor-env-contract.md:3-4` — dated 2026-09-28 read, but the path is still the entry's source
- `SKILL.md:28,33,39-40` — decision table requires `~/.config/the-janitor/op.env`, `tac-register` output path, and `$MUSKETEER_CHROME_PROFILE/NativeMessagingHosts/` as current surfaces
- `corpus/knowledge/substrate-deferral.md:4-7` — correctly says absent; this file is the exception, not the cluster

`SKILL.md:567` already says script line numbers date to the 2026-09-28 read. That does not mark the decision-table paths historical.

## HC-08 — content-hash prefixes of missing files (unresolved live)

Baseline prefixes (first 12 hex, no full hash reprinted) match the note prefixes for the two public files, and both files are absent:

- handler pin prefix `2408b0c90b7e` matches `2408b0c9…57edd` at `handler-on-disk-state.md:3`, `handler-trust-boundary.md:3`, `janitor-env-contract.md:3-4`, `drift-gate.md:19,27`
- `client.py` prefix `8179b241c6f1` matches `8179b241…ce51` at `handler-trust-boundary.md:5-6` and `drift-gate.md:19`

`drift-gate.md:19` is a historical audit sentence ("hashes happened to be quoted in prose"). `drift-gate.md:27` repeats the truncated handler prefix inside a current-tense schema example. The preserved full pin lives in `drift-baseline.tsv`. The notes still assert the prefix.

`corpus/knowledge/config-layering.md:58` asserts `sha256 \`af8873ca…\`` for `~/.config/the-janitor/config.json` (mode 600). The baseline row for that path has sha `-` (withheld). The file is absent, so the prefix is not re-derivable. This is a private-file hash prefix the lane's own hash policy refuses to store in the baseline, still sitting in a living knowledge entry. Do not expand the prefix. Do not copy it into any new pin.

`SCORECARD.md:323` says describe-don't-pin is satisfied and that no content hash of a missing file is asserted anywhere, the handler sha living only in `drift-baseline.tsv`. That sentence is false against HC-08. SCORECARD is parent/RecordPrep territory. This seat does not edit it. Named debt below.

## HC-09 — SKILL current counts (live)

Not under `:555-558`.

- `SKILL.md:46` decision table: `verify` "(54 stamps + 32 claims + claim ids)". Measured stamp rows 56, claim rows 35. `PROVINCE.md:52` and `corpus/README.md:64-65` already say 56 and 35.
- `SKILL.md:241` how-to comment: `--selftest # 94 scratch cases`. Persisted pin `R11-09` expects `SELFTEST: PASS (97 cases)`. `PROVINCE.md:52` says 97. The 94 figure is the round-14 count, written as the current comment. This seat did not run the selftest.

These are superseded-revision counts presented as the current executable layer. Operability harm is a reader who treats 54/32/94 as the pass line.

## HC-10 — lowercase fleet root (live)

`test -e /home/vgpnk/projects` → absent. `test -e /home/vgpnk/Projects/shokunin` → present.

`corpus/scope-gate.sh:91` resolves `LANE_ROOT` from `SCRIPT_DIR/../..`, overridable by `ADJ_LANE_ROOT` / `--lane-root`. It does not open `~/projects/shokunin`. `LOG.md:710-711` records that the lowercase default was removed at `8a6ec16`.

Still stated as the current resolver, with no historical marker:

- `corpus/knowledge/adjacency-scope.md:92` — `lane:` "resolves under `~/projects/shokunin/<lane>-shokunin/`"
- `corpus/README.md:25` — index points conformance at `~/projects/shokunin/CORPUS.md`

Dated, so superseded historical rather than a current how-to: `corpus/knowledge/surface-census.md:245-248` ("Reproduction (2026-09-28)"), `corpus/lessons/round-1-aggregator-audit.md:3`, `corpus/lessons/round-1-aggregator-seed.md:10,15,77`, `corpus/lessons/round-4-aggregator-audit.md:58`. Leave those lesson bytes.

Same stale string, outside this seat's write scope (gate data, not notes): `corpus/adjacency.tsv:19` comment and `corpus/claim-ledger.tsv` `R11-08` note field. The `R11-08` expect regex does not include the path. No implementation defect found. Do not edit those files from this seat.

## HC-11 — unfilled round-13 stamp (unresolved live)

`corpus/lessons/round-13.md:9-10` still says the shipped script is sha256 `<FILL ON STAMP>` / `<LINES>` lines, and that `stamps.tsv` was re-pinned to 33 artifacts.

Introducing commit `4b8c0183bd57ec5d0033fd07f650e116d7e9f600` (2026-09-28 21:50:42 -0300, "round-13"). Blob of `corpus/claim-ledger.sh` at that commit: git blob `606d166e1c92d6395a3217120a7443bb6461f820`, sha256 prefix `5b385cde` … suffix `a72f`, 1052 lines, 62941 bytes. That blob is not the current file (current stamp prefix `93c5827202b9cdec`, 1319 lines). The placeholder was never replaced. Append-only forbids rewriting the lesson. The historical blob must be described, not pinned as HEAD.

## HC-12 — boundary to LiveAnchors

`$HOME/.config/opencode/opencode.json` exists. Its line, symbol, and hash claims are not citation-to-deleted. This seat did not read the file. Owner: KagiLiveAnchors.

Contested surfaces that are absent (musketeer profile, `~/.agents/AGENTS.md`) stay the round-18 moot-until-return debt. Owners remain kake (lease) and kotoba (checklist reading). No new adjudication.

## Proposed delta — unapplied

Parent may append the following as a new lesson. Do not insert it into round-18, and do not edit the cited lines. This seat did not write it into the lane repo.

```markdown
# round-19 history erratum — citation-to-deleted and superseded revisions

2026-10-14. Advisory inventory at kagi HEAD `fecee8743e52eb8fb5fbb40782934cb619a1a96e`. Append-only. Original LOG, SKILL, PROVINCE, and corpus bytes are unchanged. This entry describes; it does not re-pin.

## Already marked (do not rewrite)

- PROVINCE.md:10-17 already marks the surface list historical.
- SKILL.md:555-558 already marks falsification round bullets as history, including the round-9 `symbols=19` falsifier, the round-11 `claims=11 stamped=28` / `39 cases` repro, and the round-14 `entries=17` docs repro.
- claim-ledger.md:4-5 already delegates the current `claim-ledger.sh` revision to `corpus/stamps.tsv`. The `d63c60b0821b5388…` / 436-line figure is the frozen wave revision only.
- Labeled dead cites stay labeled: `local://` session URIs, and `.ufo/reports/round-2/AGGREGATE.md` (still absent; `.ufo/reports/AGGREGATE.md` is a different file and is not a retarget).
- Origin-tree / `$UFO_SRC` / `ufo-fsd-alpha/` path citations: re-measured 0. Round-18's vacuous result still holds.

## Describe, don't pin

- SKILL.md:46 "54 stamps + 32 claims" is the pre-round-18 count. At this revision the data files hold 56 stamp rows and 35 claim rows (`PROVINCE.md:52`). The decision-table cell is not a current pin.
- SKILL.md:241 "94 scratch cases" is the round-14 count. The persisted pin is `R11-09` (`97 cases`). The comment is not a current pin.
- Host source-basis lines that name `~/.local/bin/the-janitor`, `client.py`, `janitor.md`, `janitor_auth.ts`, `fnm-nudge.js`, `tac-check`, `~/.config/the-janitor/`, `~/.local/state/the-janitor/`, `~/.local/state/tac/`, and the musketeer profile describe the 2026-09-28 substrate. Those paths were absent at this re-measure (14/15 drift-baseline paths; 34/35 census paths). The truncated public prefixes `2408b0c9…57edd` and `8179b241…ce51` match the preserved baseline prefixes and are not re-derivable here. They are not current identity.
- `corpus/knowledge/config-layering.md:58` prefix `af8873ca…` is a private-file hash prefix. The baseline withholds that hash (`sha=-`). Do not expand it, do not copy it into a pin, and do not treat it as re-derivable.
- `corpus/knowledge/adjacency-scope.md:92` and `corpus/README.md:25` name `~/projects/shokunin`. That directory is absent. `corpus/scope-gate.sh:91` resolves the lane root from the script directory (`SCRIPT_DIR/../..`), which is the repair landed at `8a6ec16`. The lowercase string is a deleted path, not the resolver.
- `corpus/lessons/round-13.md:9` `<FILL ON STAMP>` / `<LINES>` was never filled. The round-13 blob of `corpus/claim-ledger.sh` (commit `4b8c0183bd57ec5d0033fd07f650e116d7e9f600`, git blob `606d166e1c92d6395a3217120a7443bb6461f820`) is 1052 lines / 62941 bytes, sha256 prefix `5b385cde` suffix `a72f`. That blob is not HEAD. Current identity is the `stamps.tsv` row only.

## Not a repair

Do not re-pin drift baselines, breadth counts, or stamp expectations to the empty host. Do not delete historical quotes. A green citation-gate run does not cover host paths.
```

Proposed unapplied captions, if a later lane commit is allowed to touch mutable files. Not applied here.

SKILL.md, insert after the title block, do not alter the decision table:

```markdown
**Round-19 erratum (2026-10-14):** decision-table parentheticals "54 stamps + 32 claims" and "--selftest 94 cases" are superseded counts. Current data-file counts are the PROVINCE gate registry (56 stamps, 35 claims, 97 selftest cases). Host paths named as current surfaces are the absent janitor substrate; see `corpus/lessons/round-19-history-erratum.md`. Falsification round bullets below remain historical by the rule at the Falsification heading.
```

`corpus/knowledge/adjacency-scope.md`, append, do not edit `:92`:

```markdown
## Erratum (2026-10-14) — basis root

The `~/projects/shokunin/<lane>-shokunin/` string in the basis-column row is a deleted checkout path. `lane:` resolution is the script-derived fleet root (`corpus/scope-gate.sh` `LANE_ROOT`, `SCRIPT_DIR/../..`), not that string. Measured: `/home/vgpnk/projects` absent; `/home/vgpnk/Projects/shokunin` present.
```

## Named debt (retained)

| debt | state | unblock | owner |
|---|---|---|---|
| KAGI-HC-SUBSTRATE | live, already named in `SCORECARD.md:331-343` and `corpus/lessons/round-18.md:71-73` | reinstall the-janitor and its config/state tree; do not re-pin baselines to the empty host | operator; kagi records, does not absorb |
| KAGI-HC-SKILL-COUNTS | live in `SKILL.md:46` and `:241` | apply the caption above, or leave the erratum lesson as the only marker and accept the decision table as stale until a lane commit | parent, on a later kagi commit; not this seat |
| KAGI-HC-HASH-ASSERT | live in the four knowledge source lines and `config-layering.md:58`; scorecard sentence at `SCORECARD.md:323` is false | append the erratum; do not expand `af8873ca…`; correct the scorecard sentence in the round-19 record, not by rewriting round-18 | parent / RecordPrep for the scorecard sentence; notes stay append-only |
| KAGI-HC-LOWERCASE-ROOT | live in `adjacency-scope.md:92` and `README.md:25`; same string in `adjacency.tsv:19` and `R11-08` note | append the note erratum; comment-only gate text is untouched because this seat does not edit gate files; no resolver defect found | notes: parent; comment text: GateRepair only if that seat already has the file open for a real defect — do not open it for this comment |
| KAGI-HC-FILL-STAMP | live placeholder at `corpus/lessons/round-13.md:9` | append the historical blob description; do not rewrite the lesson; do not stamp `5b385cde…` as current | parent, append-only |
| KAGI-HC-OPENCODE-LIVE | one census/baseline path present | measure line/symbol/hash drift there; absence debt does not cover it | KagiLiveAnchors |
| KAGI-HC-CONTESTED-ABSENT | musketeer profile and `~/.agents/AGENTS.md` absent | restore substrate, then re-open the existing kake lease and kotoba checklist readings; no new ruling | kake, kotoba, integrator |

## What this seat did not do

No gate implementation change. No persisted expectation edit. No LOG/corpus rewrite. No re-pin. Citation gate was not re-run; the before receipt is the captured verdict. Sibling member reports were not read or overwritten.
