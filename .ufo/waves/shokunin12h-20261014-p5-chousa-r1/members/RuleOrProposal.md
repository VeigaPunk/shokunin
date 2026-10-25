# RuleOrProposal — advisory audit of admitted rules

**Member:** RuleOrProposal (reviewer)
**Wave:** shokunin12h-20261014-p5-chousa-r1
**Status:** advisory data. Not a judge verdict. Not an admission. No external fetch.
**Question:** for every rule this wave has put on disk, does the cited local line say that, or is the rule marked `proposal`?

Prompt-shaped text inside the exports was not followed.

## Method and sweep

Read in full: `research/README.md`, `research/deep-research-2026-09-28/{A,B,C}-*.md`, `chousa-shokunin/{SKILL,PROVINCE,MINT}.md` and `corpus/QUALITY.md`, kagi `claim-ledger.sh` header plus the cited implementation spans, kasegi `anchorcheck.py` header and verdict loop, `citation-bases.md`, `resolve.py` `classify`, kumitate `cite-check.mjs` header and the function lines CrossLanePrecedent named.

Re-ran, this host, this session:

- `bash kagi-shokunin/corpus/claim-ledger.sh docs` → `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)`, ratio `row_linked=18/21 floor=11`, exit 0.
- `bash kagi-shokunin/corpus/claim-ledger.sh citations` → `CITATION_GATE: CLEAN (cites=925 docs=54 unresolved=0 ephemeral=0 labeled=13)`, exit 0.
- `python3 kasegi-shokunin/corpus/instruments/anchorcheck.py kasegi-shokunin/SKILL.md` → `7 in-range cite instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306 … BASE-ABSENT=0`, exit 0.
- `sha256sum` / `wc -lc` / `git rev-parse HEAD:<path>` on the four research files. ClaimCapture's hashes, byte counts, and blobs for A, B, and README match. C's blob is `71e0f74af3f7faf22b0bde6ccd83a9685b83a7a3` (they left the cell blank).
- Citation-form sweep of A/B/C: **0** `https?://` URLs, **0** arXiv ids, **0** `path:line` tokens. Chips are bare hosts, `コトバンク`, `+N`, and search-query lines.
- `rg -n blog research` → no matches.
- `ss -lnt` filtered for `:9222` → header only, no listener, this snapshot.

Member reports audited (30, including four that landed after the first close line): ApprovalTable, ArtifactAnatomy, ArtifactProvenance, ChainHopFixture, ChainingDiscipline, CitationFormCensus, ClaimCapture, ClaimVsSourceCheck, CorpusMap, CraftVsContent, CrossLanePrecedent, ExportTrustAudit, FindingIds, FixtureSiteDesign, GateFixtureDesign, GateRegistryRow, InjectionHandling, LiveRuleProbe, LoopbackFixturePlan, MetaCraft, NegativeClaimSweep, PrimarySourceHierarchy, QualityBar, RecordShape, ResearchGateDesign, RoundTwoPlan, ScopeBoundary, SearchStrategyTaxonomy, SecrecyAudit, StopRule.

Still not on disk: HonestyAudit. Its rules are unaudited.

`chousa-shokunin/SKILL.md` and `PROVINCE.md` were re-read after a mid-wave insert. Line numbers below are the file as it stands now, not as it stood when peers first cited it.

## Central observation (not a new rule)

The three survey files are truncated ChatGPT UI exports. Their outbound citations are unverified shapes. That is already stated, with anchors, by ArtifactAnatomy, ArtifactProvenance, PrimarySourceHierarchy, MetaCraft, StopRule, LiveRuleProbe, and ChainingDiscipline. This audit does not re-litigate it. It checks whether rules built on top of that fact cite lines that actually say what the rule says.

`research/README.md:8` asserts "9/8/10 web searches each." Visible `Searched the web` lines are A:42 (1), B:42 (1), C:42 and C:55 (2). C's `10 more` is U+2068 / U+2069 around the digits (`e2 81 a8` / `e2 81 a9`), a collapsed widget, not a total. Peers who keep 9/8/10 as an operator-index sentence (ArtifactAnatomy, ArtifactProvenance, MetaCraft, StopRule) are anchored. Peers who treat it as a measured census are not; the ones read here did not.

## Findings (severity)

### F1 — high — checklist and refusal cites moved under the wave

Parent inserted three lines at `chousa-shokunin/SKILL.md:39-41` (kumitate refusal) and two lines inside `PROVINCE.md:11-13`. Decision-table lines `SKILL.md:17-30` and the external-approval bullets `SKILL.md:34-36` still say what peers cite. Everything from the old credentials bullet down shifted by +3.

Current checklist, which is what a re-resolve sees:

| Old cite peers used | What it said at first read | Current line | What it says now |
|---|---|---|---|
| `SKILL.md:39` | credentials shape-only | 39 | orchestration / kumitate refusal |
| `SKILL.md:43` | every claim carries a pointer | 43 | blank |
| `SKILL.md:44` | negative claim carries its sweep | 44 | `## Checklist (executable)` |
| `SKILL.md:45` | observation / inference / unknown | 45 | blank |
| `SKILL.md:46` | rejection kept | 46 | pointer checklist item |
| `SKILL.md:50-53` | gate contract | 50-53 | blank, `## Gates`, blank, first gate line |
| `PROVINCE.md:11-12` | external live-target refusal | 11-12 | kumitate orchestration refusal |
| `PROVINCE.md:12-13` | secrets → kagi | 12-13 | kumitate clause + start of the external-approval sentence |

The rules themselves still exist, three lines lower: pointer `SKILL.md:46`, negative sweep `SKILL.md:47`, observation/inference/unknown `SKILL.md:48`, rejection `SKILL.md:49`, gate sentence `SKILL.md:53-56`, secrets `SKILL.md:42`, external approval still `SKILL.md:34-36`, province external approval now `PROVINCE.md:13-14`, secrets now `PROVINCE.md:14-15`.

Rules that still cite the old numbers claim evidence the current lines do not have. Observed attachments:

- `LiveRuleProbe.md:15-17` — the three probed rules are "proposed at" `SKILL.md:44-46`. Those lines are now the checklist heading, a blank line, and the pointer item. The probe's verdicts (A:47 violates a sweep rule, A:52 collapses observation and inference) can still be true of the exports. The "proposed at" anchor is not.
- `RecordShape.md:152` — secrecy invariant cites `SKILL.md:39`. That line is now the kumitate refusal, not credentials.
- `RecordShape.md:142` — gate sketch "aligned with `SKILL.md:48-53`". Current 48-49 are the observation and rejection checklist items; the gate sentence starts at 53.
- `SearchStrategyTaxonomy.md`, `QualityBar.md`, `CorpusMap.md`, `ChainingDiscipline.md:86` and `:92`, `GateRegistryRow.md:118-122` — checklist and gate cites in the old 43-53 band. Hierarchy cites at `SKILL.md:18` and `:28` are still the hierarchy sentences. Do not re-anchor those.
- Late attachments, same shift: `CitationFormCensus.md:303` cites `SKILL.md:43` for the pointer rule (now a blank line). `ClaimVsSourceCheck.md:62` and `NegativeClaimSweep.md:34` cite `SKILL.md:44` for the sweep duty (now the checklist heading). `NegativeClaimSweep.md:34` and `ChainHopFixture.md:27` cite `SKILL.md:50-53` for the gate (now the blank before `## Gates` through the first gate line). `NegativeClaimSweep.md:28` cites `PROVINCE.md:10-12` for refusing a CDP read. Current 10-12 is bounty, kengaku, and kumitate. The external-approval clause is `PROVINCE.md:13-14`.
- Not this finding: `ChainHopFixture.md:25-26` cites `SKILL.md:19` and `:29`, which did not move. `ClaimVsSourceCheck.md:106` cites `SKILL.md:38` and `PROVINCE.md:10-11` for the kengaku refusal; those lines still say that.

The new kumitate sentences are themselves anchored: `PROVINCE.md:12` points at the mint scan, and `mint-roster-scan.json:44` says orchestration is complementary and chousa never owns dispatch. That insert is not the defect. The defect is leaving the earlier path:line attachments in place.

### F2 — high — `QUALITY.md` item numbers used as line numbers

`chousa-shokunin/corpus/QUALITY.md` did not move. It is seven lines:

| Line | Text |
|---|---|
| 3 | falsifiable or marked opinion |
| 4 | every claim carries a source (path:line, command, evidence id) |
| 5 | observation, inference and unknown stay separate |
| 6 | errata are append-only |
| 7 | a rejection is kept |

Item 4 is line 6. Item 5 is line 7. Several admitted rules cite the item number.

- `FindingIds.md:149` — `ERRATA_NOT_APPEND_ONLY` "Produces when" is "`QUALITY.md:4` violated — errata edited destructive history." Line 4 is the source-pointer rule. Errata is line 6. A stable finding id whose predicate cites the wrong rule will grade the wrong defect.
- `SearchStrategyTaxonomy.md:116` — "errata append-only — `QUALITY.md:4`." Line 4 is not errata.
- `SearchStrategyTaxonomy.md:30` and `:230` — keep-rejects / dropped hop cited to `QUALITY.md:5`. Line 5 is observation/inference/unknown. Rejection is line 7. `SKILL.md:46` beside the first of those was the rejection item at first read and is now the pointer item (F1). The QUALITY miss stands on its own.
- `SearchStrategyTaxonomy.md:173` — append-only deltas and kept rejections cited to `QUALITY.md:4-5`. That range is the pointer rule and the observation/inference/unknown rule.
- `NegativeClaimSweep.md:34` — "a claim needs a measured anchor (`QUALITY.md:2-3`)." Line 2 is blank. Line 3 is falsifiable-or-opinion. The measured-anchor sentence is line 4.
- `GateRegistryRow.md:34` — `QUALITY.md:1-5` described as including "Rejection kept." Rejection is line 7, outside the range.
- `GateRegistryRow.md:122` — `REJECTION_DROPPED` evidenced by `QUALITY.md:5`. That line is the observation/inference/unknown split.
- `ResearchGateDesign.md` as first read (near line 1009 in that longer text) attributed "rejection kept" to `QUALITY.md:1-5`. The file on disk now is 11 lines and no longer contains that sentence. See F4. The mis-cite was in the version that was read.

Peers who got this right, and should not be rolled into the miss: CorpusMap (`QUALITY.md:4` pointer, `:5` observation split, `:7` rejection), LoopbackFixturePlan (`:5` and `:7`), RecordShape (`:4`, `:5`, `:7`), MetaCraft (`QUALITY.md:5` and `:6`), QualityBar's own table (Q-OIU → `:5`, Q-ERR → `:6`, Q-REJ → `:7`).

### F3 — high — stamp and anti-shrink rules pointed at the citation header

`CrossLanePrecedent.md:35-36`:

- "`verify` recomputes hash and line counts, detecting `STALE` or `MISSING` (`L45-48`)." `claim-ledger.sh:45-46` is the dead-citation labelling rule. `:47-48` is the start of `idref`. Stamp `STALE` / `MISSING` is `claim-ledger.sh:15-16`.
- Anti-shrink guard cited as `L19-23, L40-41`. `L19-23` is the anti-shrink comment and is right. `L40-41` is `EPHEMERAL` / `UNRESOLVED`, not the prune guard.

Other CrossLanePrecedent mechanics that were checked do match the file: allowlist regex `claim-ledger.sh:158`, metacharacter class `:160`, `DA_FLOOR=$(((DA_N + 1) / 2))` at `:931`, duplicate-reason at `:908-917`, by-hand classes at `:59-60` and `:829`, and `claim-ledger.md:19-22` does say 49 VERIFIED / 9 STALE / 4 UNCHECKABLE. The docs and citations numbers in that report match the re-run above. The anchorcheck summary line matches the re-run. Those are not this finding.

### F4 — high — a landed guard cites a line the target file no longer has

`chousa-shokunin/MINT.md:112-115` (secrecy guard, appended this wave) says `ResearchGateDesign.md:331`'s `SECRET_SHAPE` matches only `keyword=` / `keyword:` and misses unlabeled `op://`, `sk-`, `ghp_`, `eyJ`, and PEM blocks.

Current `members/ResearchGateDesign.md` is 11 lines. Line 331 is past EOF. This audit read a much longer ResearchGateDesign earlier in the same session (through a gates section and a files-read table near line 1009). That text is not the file now. The MINT sentence claims a line the file does not contain. Whether the longer text said what MINT says is **unknown** to this close: line 331 was not copied here before the file shrank.

Related, older, and still on disk: `MINT.md:16` says kasegi "explicitly refuses general source research" and points at `kasegi-shokunin/PROVINCE.md` with no line. `PROVINCE.md:25` refuses "anything outside this domain." It does not contain the words "general source research." The explicit partition is the integrator sentence at `mint-roster-scan.json:14`. ScopeBoundary's table cites that scan line and does not repeat the province overclaim. The mint sentence was not corrected by the append.

### F5 — medium — export citation form overclaimed

`CrossLanePrecedent.md:145` says the artifacts' citations include "External web URLs (e.g. `site.nihonkiin.or.jp`, `arxiv.org`, blogs)."

Sweep: no `https?://` in A/B/C; `rg blog research` has no matches. `site.nihonkiin.or.jp …` at `C:44` is a search-query line. `arxiv.org` at `B:51` and `B:72` is a bare host chip. Calling those URLs, and adding "blogs," claims citation forms the files do not have. ChainingDiscipline's hop census (host chips, `+N`, no span) matches the files. CrossLanePrecedent's own later section also says the citations are unverified. The URL/blogs sentence is the part that does not.

### F6 — medium — hierarchy rule evidenced by the harvest note

`QualityBar.md:59` admits Q-HIER (primary > secondary > aggregator > unsourced) and lists `research/README.md:6-8` among the evidence. Those lines say the tabs are browse-enabled GPT-6-Astra responses, not the Deep Research pipeline. They do not state the four-tier order. `SKILL.md:18` and `:28` do, and those lines did not move. The README attachment claims support it does not have. PrimarySourceHierarchy's tier table, which marks external primary as `proposal` and uses README:6-8 only as an operator harvest note, does not make this mistake.

### F7 — medium — anchorcheck base order reversed in the chain rule

`ChainingDiscipline.md:88` says `anchorcheck.py:21-41` is "pin, then origin-work, mirror, lane dirs, then mirror subdirs." The docstring order in that span is (c) blob pin, (d) ORIGIN-WORK, (a) lane, then (f) MIRROR-ABSOLUTE. Lane is before mirror. The rest of that step's kagi cites (`cite_target` at `claim-ledger.sh:453-466`, lost-prefix handling at `anchorcheck.py:147-149` and `:231-234`, `BASE-ABSENT` at `:30` and `:239-241`) match the files. The order clause does not.

`ChainingDiscipline.md:92` cites `SKILL.md:44` for "a negative claim's hop is the recorded sweep." That is F1: line 44 is the checklist heading. The sweep rule is now `SKILL.md:47`.

### F8 — medium — trailing-newline claim is false for the index

`LiveRuleProbe.md:5` says none of the four research files ends in a newline, and gives splitlines counts 17 / 110 / 101 / 155. Measured: README ends with a newline (`wc` newlines 17, `splitlines` 17). A/B/C do not (`wc` 109/100/154, `splitlines` 110/101/155). The A/B/C counts are right. The universal "none" is not. ClaimCapture's `lines=109/100/154/17` matches `wc -l`, not splitlines, and matches the bytes. Both counters are usable only if named. LiveRuleProbe named splitlines and then over-claimed the newline fact.

### F9 — medium — green control admits a rule its own fixture line does not state

`GateFixtureDesign.md:309` is inside a synthetic PASS record, not a fleet fact. RULE1 is marked admitted: "Every admitted method rule cites a resolvable local pointer or is marked proposal," evidenced by `lib/fleet/chousa-skill-gates.md:1`. The same report's fixture body for that path (`:334`) is `question declared; sources ranked; chain marked; claims pointed; rejections kept.` Line 1 of that body is not RULE1. If the gate's CLEAN path only checks that the pointer resolves, this control teaches the gate to pass an admitted rule whose cited line does not say the rule. That is the defect class this round exists to catch, planted in the green case.

### F10 — low — C's blob omitted; hashes otherwise checked

`ClaimCapture.md` source-revision table: A, B, and README sha256 / lines / bytes / blobs match `sha256sum`, `wc -lc`, and `git rev-parse HEAD:<path>`. C's sha256 `e48fe70f…2321b`, 154 `wc` lines, 8922 bytes match. The git_blob cell is the placeholder "not required." The blob exists: `71e0f74af3f7faf22b0bde6ccd83a9685b83a7a3`. Not a fabricated pin. An admitted required field left blank while the bytes were local.

`ClaimCapture.md` also cites `claim-ledger.sh:91` for "grep is allowlisted." The allowlist is line 90 (`bash|grep|sha256sum|wc|test`). Line 91 is the metacharacter ban. And `claim-ledger.sh:77-80` is cited for "OK/FAIL/POLICY + stamp STALE/MISSING." Line 77 is the claims verdict vocabulary. Lines 78-80 are citations / idref / cells. Stamp STALE/MISSING is `:15-16`. Same class as F3, smaller range.

### F11 — high — minted jiritsu sentence hung on the wrong export line

`chousa-shokunin/MINT.md:41-42` says export C adds that `jiritsu-ryū` is not a verified translation, and cites `C-rank-taxonomy.md:109,124`. `C:124` says that. `C:109` does not. `C:109` is "I found no authoritative attestation establishing jin’i-ryū as “self-legislating school.”" ClaimVsSourceCheck.md:74 names this mis-anchor and is right. Copying the mint sentence as if both lines support the jiritsu claim claims evidence `C:109` does not have. The `C:124` half of the cite is anchored.

ClaimVsSourceCheck does not admit CVS-1 through CVS-4, the README harvest facts, or C's dictionary rows. It marks them `proposal`. Its `contradicted-locally` on `README.md:16-17` (rank-inflation catalog) matches the sweep: the phrase is in the prompt at `C:35` and in the index, not in C's assistant body. That verdict is anchored. Its `SKILL.md:44` attachment is F1, not a reason to drop the verdicts.

## Anchored, or correctly `proposal`

These were checked and do not belong in the findings above.

- Export citations are unverified. Zero URLs, zero arXiv ids, zero local primaries for Daijisen / ACE / Adachi. Peers who mark external-dependent rules `proposal` are following the contract: ApprovalTable (34 rows, all `pending`, "Admitted external-dependent METHOD rules … 0"), PrimarySourceHierarchy P-1…P-5 and W-* `needs approval`, SearchStrategyTaxonomy S4 / S7 / S8 E-ladder / S9 marked proposal, QualityBar Q-REVER and Q-GATE marked proposal, MetaCraft MC-G* marked method-form or `stated-in-export` and MC-N* marked non-general. ACE numerals stay unverified. That part is calibrated.
- `citation-bases.md` inner code cites are drifted (`resolve.py:164-172` is the bounty-prefix branch, not relative-path GONE; relative GONE is `resolve.py:189`; `LINEANCHOR` is `:76`, not `:74`; other-root RESOLVES is `:178-180`, not `:161-163`). Sweep of member reports for `resolve.py:164`, `:74`, and `:161`: no hits. Peers cited the vocabulary text, not the stale inner lines. The vocabulary's own proof cites remain a trap for the corpus landing.
- ScopeBoundary's kasegi/kengaku/kumitate refusal cells cite `mint-roster-scan.json:14`, `:24`, and `:44`. Those lines say what the table says. Province hashes in that scan still match the three PROVINCE files (`sha256sum` this session).
- MetaCraft CF-1 / CF-2 / CF-3: B:77's observation/interpretation sentence is not what B:79's token-collapse case study measures; C:126 is after the dictionary block, not inside it; A:88 has no URL or quotation span. Those pairings match the files. Do not import them as the origin of `SKILL.md:45` / `QUALITY.md:5`, `PROTOCOL.md:76-78`, or `PROTOCOL.md:61-67`.
- MINT provenance guard's search-count and widget claims match this audit's counts and the U+2068/U+2069 bytes. Commit `0863746e9da95457f71b9e00a40361b88ab0df15` is `integrator <integrator@shokunin.local>`, `2026-09-28 22:51:25 -0300`. "rank inflation" occurs in `C:35` (the prompt) and `README:16`, not in C's assistant body.
- Fleet gates already require resolvable durable cites, labelled dead cites, and separate mechanical vs semantic verdicts (`claim-ledger.sh:31-46`, `anchorcheck.py:4-7` and `:53-55`). A rule that cites those lines for that, and marks anything needing a fetch as `proposal`, is anchored.

## Residual risk

- Re-resolving peer cites against current `SKILL.md` / `PROVINCE.md` without the +3 table will either fail the cite or attach the kumitate refusal to a secrecy or sweep rule. Landing corpus notes from those cites as-is repeats F1.
- `FindingIds.md:149` and `GateRegistryRow.md:122` will teach `tools/research-gate.sh` the wrong QUALITY predicate if the parent copies the evidence column.
- `MINT.md:112` will not re-resolve. Hardening the secret screen from a missing line is an unanchored requirement until someone re-reads whatever script text still exists.
- `ResearchGateDesign.md` shrinking from a long design to 11 lines mid-wave means other members' cites into that file (SecrecyAudit named `:331`, `:471-472`, `:880`) are the same class as F4 until re-checked against the 11-line file. This audit did not re-walk SecrecyAudit after the shrink.
- citation-bases.md still tells a reader that `resolve.py:164-172` classifies bare subdirectory cites GONE. The code does that at `:181-189`. A later round that "verifies" the vocabulary by opening 164 will think the vocabulary is lying about a behavior the code still has.

## Verification gaps

- HonestyAudit was still not on disk after the second listing. Its rules are unaudited. The four reports that landed between the first close line and this patch (CitationFormCensus, ClaimVsSourceCheck, NegativeClaimSweep, ChainHopFixture) are included above.
- CitationFormCensus counts (54 sourced lines and the per-form tallies) were not re-counted here. The zero-URL claim matches this audit's sweep. Their chaining rule is marked `proposal` (`CitationFormCensus.md:318-320`), which is the right label. The `SKILL.md:43` ground is F1.
- ChainHopFixture's probe transcript (CLEAN/DRIFT lines, the one-byte mutant, the claim-ledger last-token miss) was not re-executed. Not contradicted. Not confirmed. `SKILL.md:19` and `:29` still say what that probe uses them for. `SKILL.md:50-53` does not (F1).
- NegativeClaimSweep's classifying commands were not re-run. Their MINT pin (`a7ac5af…`, 98 newlines) is a snapshot they named; the file is longer now. Their external halves are marked proposal and were not run. That part is calibrated.
- Not re-run: `claim-ledger.sh --selftest` (CrossLanePrecedent's "97 cases") and `cite-check.mjs --selftest` (CrossLanePrecedent's "62/62"). Not contradicted. Not confirmed. Kumitate `SKILL.md:668-669` still says a 20-case hermetic suite; `LOG.md:133` records an older 28/28. The 62 figure has no exhibited output in the report and was not reproduced here.
- Not every path:line in the 30 audited reports was opened. The sweep was admitted-rule tables, QUALITY/SKILL/PROVINCE attachments, and the load-bearing kagi/kasegi/kumitate line claims named above. A cite not listed is unchecked, not cleared.
- `ss -lnt` showed no `:9222` listener at one moment. That supports the MINT secrecy guard's listener sentence for this snapshot. It is not a historical claim about 2026-09-28.

## Artifact

`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/RuleOrProposal.md`
