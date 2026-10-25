# Round 12 SOURCES — curated lane reading index

**Scope:** this is a pointer layer over the 21 physical local child repositories, pinned to the exact commits listed below. `MANIFEST.json` remains the operator-controlled 13-entry roster; the 21 physical local repositories are a distinct population, not 21 registered roster rows. No child `corpus/SOURCES.md`, knowledge entry, lesson, or scorecard was changed by this aggregator.

This index records where each lane's `## Paths`, `## Search log`, and `## Leads (unopened)` live, plus selected reading paths and a few explicit rejection/flip examples. It does **not** restate source claims as verified facts, append any `S###` row, establish a second research method, or count source rows as knowledge expansion. Unopened Leads remain navigation pointers only, never evidence. The 32-seat dispatch/evidence map is `.ufo/waves/kaika-aggregate/dispatch.md`; the gate result matrix is `.ufo/waves/kaika-aggregate/r12-gate-final.md`.

## Census and validator at the final pins

The corrected `scripts/sources-census.sh` was read from this worktree at fleet commit `54a20d39c533dcfd41473582e12ed380cf3d932b`, blob `3f314620b2395eeb70d8405410132027dfe608e4`. It parses 0–3 leading Markdown spaces, omits `repo=.` main-repo lanes from default discovery, and retains the SOURCES-contract E/W distinction. The exact archive/root construction, full commands, per-lane stdout, script identity, and limits are recorded in `.ufo/waves/kaika-aggregate/sources-census-final.md`.

The four modes ran on the 21 refreshed full-commit tree snapshots, with `--today 2026-10-20`:

| Mode | Exit | Observed result |
|---|---:|---|
| `census` | 0 | **576 rows**; tiers **A=500, B=33, C=43, invalid=0**; statuses **mined=307, queued=220, rejected=49, invalid=0**; missing registries **0**. Rows = tier sum = status sum = 576. |
| `validate` | 0 | 21 `ok` lane rows; **0 E-code errors**, **7 W-code warnings**, 0 missing. Exact warning rows are listed below; warnings were not hidden or promoted to errors. |
| `shared` | 0 | 2 normalized URLs occur in more than one lane: gdUnit4 command docs; Kubernetes pod probes. Exact lane pairs are below. |
| `overdue` | 0 | 0 overdue rows; 557 cadence rows. Symbolic cadences are reported, not judged overdue. Histogram: 30d=2, 90d=100, 180d=88, 365d=72, 730d=10, `every round`=1, `frozen`=2, `on-change`=5, `on-commit`=2, `on-gate-change`=1, `on-release`=274. |

Validation warnings (all are W-codes, not E-code failures):

```text
audio-shokunin W01 S007 tierC mined used-by=corpus/knowledge/2026-10-19-game-loudness-whole-mix-protocol.md, corpus/lessons/round-101.md
audio-shokunin W04 S014 duplicate url raw.githubusercontent.com/FFmpeg/FFmpeg/n9.0.1/libavfilter/af_loudnorm.c across scopes
audio-shokunin W04 S015 duplicate url www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf across scopes
lore-shokunin W04 S017 duplicate url arxiv.org/html/2603.05890 across scopes
lore-shokunin W01 S027 tierC mined used-by=corpus/knowledge/r103-canon-status-and-supersession.md
lore-shokunin W04 S032 duplicate url www.iso.org/standard/70908.html across scopes
mado-shokunin W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
```

Shared normalized URLs:

```text
godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd — game-dev-2d-shokunin, game-dev-3d-shokunin
kubernetes.io/docs/concepts/workloads/pods/probes — kama-shokunin, mori-shokunin
```

## Lane registry pins and local study paths

Each `HEAD` is the final full commit read from the original lane repository; `blob` is `git rev-parse <HEAD>:corpus/SOURCES.md`. Section ranges are inclusive and refer to that same blob. `validate` is the corrected-script result at the matching full-tree snapshot. `mined/queued/rejected` are registry statuses only, not a semantic quality grade.

| Physical lane | Final HEAD | SOURCES blob | Rows; tiers A/B/C | Statuses mined/queued/rejected | `## Paths` | `## Search log` | `## Leads` | Validate |
|---|---|---|---|---|---:|---:|---:|---|
| audio-shokunin | `0462a5440f23f45707ba681e2a011940e3c923dd` | `48d5b87b07cab290672f71195bb70687a8665776` | 15; 11/2/2 | 14/0/1 | 26–34 | 35–41 | 42–51 | rc0; W01×1,W04×2 |
| chousa-shokunin | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `8429343f1b750a9fd4bc7a470373d99ae57d1ad3` | 18; 14/1/3 | 8/7/3 | 30–45 | 46–71 | 72–83 | rc0; no W |
| game-dev-2d-shokunin | `bce53b83a21ea43ddc2bf050bfe78cb4f2b68550` | `6eb0f26c5e3f61567527a45d4b7c95ae52815dd6` | 31; 30/1/0 | 10/19/2 | 39–45 | 46–52 | 53–57 | rc0; no W |
| game-dev-3d-shokunin | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `07a5816947c98a6c39b4ace520aa15654c74c795` | 36; 33/2/1 | 6/28/2 | 46–53 | 54–65 | 66–70 | rc0; no W |
| kagi-shokunin | `c2cab35bc92e57e39e5489bac3386db078345b3f` | `36e166f08fefd6053c1effde41ec6174cb0f5820` | 16; 14/0/2 | 14/1/1 | 24–29 | 30–33 | 34–43 | rc0; no W |
| kaidoku-shokunin | `767adafb97e2eef6980e2ad873d357e16721c467` | `a411c18c74c0690c1073e08f241c53779750263d` | 22; 20/1/1 | 21/0/1 | 30–39 | 40–43 | 44–50 | rc0; no W |
| kake-shokunin | `5009ecaa1cce10b895617a585ddd3f7c7c923a84` | `bb7ed1649256a0ccfd5f8bdc71f1b9c003b9ee09` | 18; 16/0/2 | 14/2/2 | 28–34 | 35–44 | 45–65 | rc0; no W |
| kama-shokunin | `2f7303c242319c1dc96c6bcf7702ac18b3ca1aad` | `7de1360655eadada356fe110813c6e1338142551` | 30; 27/0/3 | 17/8/5 | 44–50 | 51–56 | 57–60 | rc0; no W |
| kasegi-shokunin | `922a4dde90b60b465e2b8b241d1fe363f1f27e98` | `01fcdbb6b833482ac15e8211624832f52b8abb9e` | 27; 25/0/2 | 15/10/2 | 35–40 | 41–49 | 50–54 | rc0; no W |
| kengaku-shokunin | `6180e4fb92e90c0b172e9788e2c765d097f2e142` | `74070565c0932a39737fc7d24250c5a716802e40` | 26; 24/0/2 | 18/5/3 | 50–57 | 58–65 | 66–70 | rc0; no W |
| kotoba-shokunin | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `a048aef0997e68881c9740e878d2fe01402bb04b` | 11; 10/0/1 | 4/6/1 | 26–40 | 41–67 | 68–87 | rc0; no W |
| kotodama-shokunin | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `34e27f6a1878b0de2bf69785ef2c4b391a1fdb01` | 47; 34/6/7 | 20/22/5 | 78–111 | 112–119 | 120–169 | rc0; no W |
| kumitate-shokunin | `1770305fae20826b39905a8251ddeca6b4957ac4` | `6e92b79bdfe022648574c271c4a9a9768238912b` | 20; 19/1/0 | 9/9/2 | 35–55 | 56–94 | 95–118 | rc0; no W |
| lore-shokunin | `01306d51252f837909af5252c398ee4e31259f9b` | `a547b1b60314cb7aacdebad9fb7852509c8e59d3` | 32; 24/3/5 | 12/17/3 | 42–51 | 52–63 | 64–78 | rc0; W01×1,W04×2 |
| mado-shokunin | `7dcb785b7b943d03703181b218d7860a7b43007b` | `56f8f49c9913455e89bdf91434130f0d4637b887` | 39; 35/1/3 | 27/9/3 | 52–60 | 61–93 | 94–120 | rc0; W04×1 |
| mori-shokunin | `6531ac6029e200a6392bb76673b6a17d3c895c96` | `9065f76f35d7185b4fc5b2ba10c9a05a5cd1186f` | 34; 31/2/1 | 12/21/1 | 42–47 | 48–53 | 54–56 | rc0; no W |
| revenger-shokunin | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `2fcf0d901c71116ea951eb012be67125c2980948` | 15; 14/0/1 | 12/1/2 | 31–37 | 38–43 | 44–49 | rc0; no W |
| souji-shokunin | `31984f473ce4bdab61a99b16cca194b28108cb81` | `a67b6f573f1fbb52198c028f0d7e77f5fa3b7f35` | 33; 29/3/1 | 16/15/2 | 43–48 | 49–55 | 56–68 | rc0; no W |
| tabi-shokunin | `f032f2dccc8a99632eea52edafa8220284b5c919` | `89a69384adeff8ccda3b41e4938abc40425492b9` | 28; 22/4/2 | 20/6/2 | 44–50 | 51–58 | 59–63 | rc0; no W |
| tameshi-shokunin | `18ad5d050ef4bcd830fe513825baed878f025024` | `b1cff984384860ad7b3d301aef493ba0386c3a68` | 44; 37/5/2 | 12/29/3 | 57–62 | 63–100 | 101–122 | rc0; no W |
| tsukuroi-shokunin | `b76b5c377eaee3e3d8d47fdddde977828d05dbd5` | `194059c471e25702edb6b39c58abd91a79f3d8b5` | 34; 31/1/2 | 26/5/3 | 42–47 | 48–55 | 56–73 | rc0; no W |

## Selected lane Paths — navigation examples, not transfer claims

These exact path titles/sequences are copied as pointers from the lane `## Paths` at the pin in the table. Row IDs are lane-local. The hop status counts refer only to the registry status labels at that pin and do not validate the underlying source claims.

| Lane origin | Path | Sequence | Hop status note |
|---|---|---|---|
| `audio-shokunin` §Paths line 29 | Godot asset path | `S009 → S010 → S011 → S008 → S013` | 4 mined, 1 rejected; the path explicitly marks S011 as a rejected tutorial used to explain the conflict, not as support. |
| `game-dev-2d-shokunin` §Paths line 41 | Tilemap physics attribution | `S004 → S003 → S005 → S002 → S027 → S029 → S030` | 5 mined, 2 queued; a mixed reading route ending in the lane's own measurements. |
| `tameshi-shokunin` §Paths line 59 | Mutation verdict semantics and validity | `S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007` | 4 mined, 4 queued; the queued tail is frontier reading, not completed support. |
| `kagi-shokunin` §Paths line 26 | Machine credential custody boundaries | `S001 → S004 → S002 → S003 → S006 → S007` | 6 mined; rows point to the lane's knowledge entry. |
| `kasegi-shokunin` §Paths line 37 | CVSS severity and CWE prioritization | `S002 → S001 → S013 → S014 → S015` | 5 mined; the lane audit reports the path feeds two named knowledge entries. |
| `revenger-shokunin` §Paths line 35 | `decoding a resource name field` | `S009 → S010 → S011 → S013` | 4 mined; the terminal record is byte-identified by the lane's registry. |
| `kotoba-shokunin` §Paths line 28 | Authoring a SKILL.md that loads everywhere | `S001 → S008 → S003 → S002 → S011` | 4 mined, 1 rejected; the final rejected hop is explicitly the caution lesson. |

Excluded from the selected reading set: **game-dev-3d** §Paths line 48, `S012 → S011 → S035` has S036 superseding S011 without the path being updated; **mado** U2 §Paths line 55 ends at rejected S030 without marking it as caution; **lore**'s In-world-time path remains a study sequence after its related knowledge entry was rejected at re-grade and moved to the rejected archive. These are preserved as staleness/rejection evidence, not silently “fixed” by this index.

## Transferable paths from the four opened W1 ART dossiers

The W1 references below were read as local research artifacts; their `S###` identifiers are **dossier-local**, never lane registry IDs. These routes are candidates for a lane's own curation only after that lane opens the cited sources and applies its own `QUALITY.md`. No claim that any lane adopted them is made.

| W1 artifact + section | Route as written | Knowledge expansion vs capability | Boundary |
|---|---|---|---|
| `.ufo/waves/kaika-w1/art-learning.md` §Study paths, “Build a lane source/skill loop” | `S005 → S006 → S007 → S003 → S004 → S001/S019` | Reading path candidate for knowledge expansion | Does not establish a lane's admission bar or non-author review. |
| `art-learning.md` §Study paths, “Study memory retention without importing destructive forgetting” | `S018 → S015 → S016 → S014 → S017` | Reading path candidate for knowledge expansion | Recheck/supersede; not automatic deletion or rewriting. |
| `.ufo/waves/kaika-w1/art-mistakes.md` §Study paths, “LLM correction: limits → diagnosis → verifier → current benchmark” | `S001 → S002 → S004 → S003 → S011/S012 → S009 → S010` | Knowledge reading plus verification-practice candidate | Self-review is not an independent verifier; no benchmark result is asserted here. |
| `art-apprenticeship.md` §Study paths, “From activity to defensible practice claim” | Ericsson 1993 → Macnamara 2014 → Ericsson 2016 → Macnamara reply 2016 → Macnamara & Maitra 2019 | Literature reading candidate for knowledge expansion | Preserve disagreement; hours/repetition are not a promotion threshold. |
| `art-apprenticeship.md` §Study paths, “From apprenticeship to autonomous craft” | Lave & Wenger ch.1 → ch.4 → Collins et al. 1991 → Dreyfus 2004 → Kahneman & Klein 2009 | Literature reading candidate for knowledge expansion | Cross-domain analogy only; no universal rank schedule is established. |
| `.ufo/waves/kaika-w1/art-curation.md` §Proposed final SOURCES contract | Contract fields, scoped tiers, revision/anchor, rejection flip, search log | Capability/navigation reference, not knowledge expansion | The contract is already frozen at `SOURCES-CONTRACT-v1`; this index adds no rules and does not duplicate chousa's method. |
| `art-mistakes.md` §Audit rounds | Premortem → evidence review → closure check → next-audit recurrence → corpus-wide audit | Process/capability reference, not knowledge expansion | A planning sequence, not a verified finding or a universal research methodology. |

## Rejection/flip examples and open evidence gaps

| Lane / row | Recorded rejection and flip (summary from the row at the pinned HEAD) | Index treatment |
|---|---|---|
| audio S011 | Godot 4.4 tutorial conflicts with the same-version generated class reference and the host headless import; flip if the tutorial or engine source supports `compress/mode=0` for 4.4. | Kept as a rejected counterexample in the lane's Godot asset path, not as factual support. |
| game-dev-2d S015 / S031 | A pre-release snapshot or EOL 4.4 docs cannot ground current behavior; flips are build-scoped claims. | Kept rejected; no current-behavior claim borrowed. |
| kagi S008 | SOPS README lists formats/backends but does not teach lifecycle/rotation mechanics; flip if the upstream README restores that procedure. | A genuine retained rejection, not a missed source. |
| kotoba S011 | Tutorial claims conflict with the client contract; flip if the specification/client behavior changes. | Path deliberately ends with the rejected tutorial as a caution. |
| kasegi S026 / S027 | Gold Eagle lacks a checkable validation protocol/results for the general method; the HN item is a link without accessible article text/discussion. | Rejections retained with scoped flips; no claims sourced from them. |
| mado S030 | Duplicate/overlapping URL with S017; its path still includes the rejected row without a caution marker, and the exact distinct-anchor flip remains the lane's stated condition. | Excluded from the selected paths as a stale hop; no edit made. |
| lore S017 / S032 | Same URLs occur for distinct scopes; an append-only exception is recorded, while the census warns duplicate URL/scope without `supersedes`. | Reported as a warning/known tension, not waved away. |

W1 `art-curation.md` §Leads (unopened/access-limited) reports AJP-2.1 and TARCiS routes returning 403, current GRADE Book pages returning an empty shell, and the LOC WARC page returning 403. They remain **leads, not evidence**; the W1 ART dossiers and their own source rows were not re-opened in this aggregator round.

## Limits and authority

- A structurally valid row, a `mined` label, or an existing `used-by` path does not prove that the cited page was opened at the claimed revision or that it supports `teaches`. This aggregator did not fetch URLs or revalidate all anchors/quotes.
- The census validator checks row schema, enums, date/cadence syntax, duplicate rows/URLs, and `used-by` **path existence**; it does not prove that a target cites the row ID, validate `supersedes` targets, or judge a `## Paths` order. The path/hop table is a bounded pointer check, not a semantic source audit.
- Symbolic rechecks (including `every round` / `frozen`) are reported as cadences, not independently judged stale. `overdue=0` is not “all fresh.”
- The corpus gate does not structurally validate `SOURCES.md`. It implements r2/r4/r7/r8-literal/r10/SHONEN form only; r1/r3/r5/r6/r9, verifier independence, and SHONEN truth remain not-evaluated. R12 `r10` is missing on all 21 lanes because this assignment prohibits child-corpus writes; it is an aggregator-owned lesson-presence debt, not a child-authored defect.
- The index does not write or amend any lane registry, does not treat branch-only/unopened leads as evidence, does not claim lane expansion from row totals, and does not prescribe a universal research method.
