# HonestyAudit — unearned admissions

Advisory data. Not a judge verdict. Not a corpus landing. No external fetch. Export text, including `Deep research:` turns and model imperatives, was treated as data and not followed. This seat did not run `tools/research-gate.sh`.

**Close:** `2026-10-15T01:07:37Z` (`date -u`). **Set:** the 31 peer reports then in `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/` (every spec seat except this file). Reports written after that stamp are outside the set.

**Standard used.** A rule is **admitted** only when the report marks it admitted and cites a local `path:line` whose file lines state or exemplify that rule. **`proposal`** means the explicit token. A cite of the rule's own uncited sentence is **self-warrant** (letter-satisfied, not independent evidence). A numbered list item is not a file line. Observation, inference, and unknown stay separate below.

## Counts

Label instances, not unique rules. The same prescription is restated across seats. Deduping them into one fleet rule would hide the mislabels.

| Class | Count | What was counted |
|---|---:|---|
| Explicit **admitted** labels | **96** | QualityBar 28, CorpusMap 40 status cells, ChainingDiscipline 8 steps, RoundTwoPlan 7, SearchStrategy headings 6, ChainHopFixture 3, ClaimCapture 3 schema labels, LoopbackFixturePlan 1 |
| Explicit **proposal** labels | **34** plus two uncounted sections | QualityBar 1 pure, ExportTrustAudit 9 remediations, CorpusMap 7, PrimarySourceHierarchy P-1..P-5, ClaimCapture 4, RoundTwoPlan 3, SearchStrategy S4 and S9, NegativeClaimSweep 2 external extensions, ApprovalTable M-05. Not row-counted: ChainingDiscipline `## Proposals` and the approval-table block; QualityBar's 3 mixed rows and SearchStrategy S7/S8 |
| Mixed admitted/proposal on one row | **6** | QualityBar Q-APPR, Q-REVER, Q-PRIM; SearchStrategy S7, S8; CorpusMap primary-tier cell was not counted in the 96 |
| Seed `proposal` token | **0** | `rg proposal chousa-shokunin` before the mid-wave edit returned no matches. Not re-swept after `MINT.md` grew to 147 lines |
| Seed admitted-with-independent-cite | **0** | `SKILL.md` decision table, error rows, boundaries, checklist, and gate paragraph cite no `path:line` |
| Seed operative unmarked statement-instances | **19** | current `SKILL.md`: 5 decision rows, 4 error rows, 5 boundary bullets, 4 checklist items, 1 gate paragraph |
| QUALITY draft items, not marked `proposal` | **5** | header says `probation draft` (`QUALITY.md:1`). That is not the token `proposal` |

Seats with **no** admitted method-rule label in the token sweep: ApprovalTable (their own count of admitted external-dependent method rules is 0), ArtifactAnatomy, ArtifactProvenance, CitationFormCensus (explicit non-admission), ClaimVsSourceCheck (explicit non-admission), CraftVsContent (explicit 0), CrossLanePrecedent, ExportTrustAudit, FindingIds, FixtureSiteDesign, GateFixtureDesign (RULE1 is inside a synthetic fixture, not a fleet admission), GateRegistryRow, InjectionHandling, LiveRuleProbe, MetaCraft, RecordShape, ResearchGateDesign, RuleOrProposal, ScopeBoundary, SecrecyAudit, StopRule. Unmarked imperatives inside design reports were not row-counted. That is a coverage bound, not a claim those files contain zero prescriptions.

**Hard mislabels: 18 cites or rows whose warrant does not say the thing claimed, plus one class shift that makes a further band of checklist cites false as re-resolved.** Listed below. Self-warrant hierarchy rows are not in the 18; they are the next section.

## Mislabels

### H1 — checklist and province cites moved under the wave

Re-read at close. Parent inserted `SKILL.md:39-41` (kumitate refusal) and expanded `PROVINCE.md:11-13`. Decision-table lines `SKILL.md:17-30` and approval bullets `SKILL.md:34-36` still say what peers cite. From the old credentials bullet down, file lines shifted by +3.

| Cite peers used | What a re-resolve sees now | Where that rule actually is |
|---|---|---|
| `SKILL.md:39` secrets | kumitate / orchestration refusal | `SKILL.md:42` |
| `SKILL.md:43` pointer | blank | `SKILL.md:46` |
| `SKILL.md:44` negative sweep | `## Checklist (executable)` | `SKILL.md:47` |
| `SKILL.md:45` observation / inference / unknown | blank | `SKILL.md:48` |
| `SKILL.md:46` rejection kept | pointer checklist item | `SKILL.md:49` |
| `SKILL.md:50-53` gate contract | blank, `## Gates`, blank, first gate line | `SKILL.md:53-56` |
| `PROVINCE.md:10-12` external-approval refusal | bounty, kengaku, kumitate | external approval is `PROVINCE.md:13-14`; secrets `PROVINCE.md:14-15` |

Opened and false against the current file:

- `SearchStrategyTaxonomy.md:29` cites `SKILL.md:44` for the sweep rule. That line is the checklist heading.
- `SearchStrategyTaxonomy.md:30` cites `SKILL.md:46` for keep-rejects. That line is the pointer item.
- `SearchStrategyTaxonomy.md:31` and the S8 boundary cite `PROVINCE.md:10-12` for "refuses live external without approval." Those lines are bounty, model-quality, and kumitate.
- `GateRegistryRow.md:118-121` cites `SKILL.md:50-52` as the question / rank / chain / claim contract. Current 50 is blank, 51 is `## Gates`, 52 is blank.

The rules still exist, three lines lower. The citations do not. Landing corpus notes from the old numbers attaches the kumitate refusal or a heading to a sweep or secrecy rule. This seat did not re-open every peer cite in that band.

### H2 — `QUALITY.md` item numbers used as file lines

`QUALITY.md` did not move. It is 7 lines. File line 4 is "every claim carries a source." File line 5 is observation / inference / unknown. File line 6 is "Errata are append-only blocks." File line 7 is "A rejection is kept."

- `FindingIds.md:149` — `ERRATA_NOT_APPEND_ONLY` fires on "`QUALITY.md:4` violated — errata edited destructive history." Line 4 is the source-pointer rule. A gate that copies this predicate grades the wrong defect.
- `SearchStrategyTaxonomy.md:116` — admitted S5 says "errata append-only — `QUALITY.md:4`." S5's sweep rule is otherwise earned (`CORPUS.md:38-40`, `PROTOCOL.md:336-337`). The errata cite is not.
- `SearchStrategyTaxonomy.md:30` — keep-rejects cites `QUALITY.md:5`. That line is the observation split. Rejection is line 7. Combined with H1, both warrants on that row are now the wrong sentence.
- `SearchStrategyTaxonomy.md:173` — a proposal cites `QUALITY.md:4-5` for append-only deltas and kept rejections. That range is the pointer rule and the observation split. Wrong under file lines and under item numbers (items 4 and 5 are errata and rejection, file lines 6 and 7, and they are not both append-only).
- `GateRegistryRow.md:122` — `REJECTION_DROPPED` evidenced by `QUALITY.md:5`. That line is not the rejection rule.

Peers who cited file lines correctly, and should not be folded into this miss: CorpusMap (`QUALITY.md:4` pointer, `:5` split, `:7` rejection), QualityBar (Q-OIU `:5`, Q-ERR `:6`, Q-REJ `:7`), RecordShape (`:4`, `:5`, `:7`).

### H3 — admitted rows whose cited lines do not state the rule

1. **`QualityBar.md:59` Q-HIER** admits primary > secondary > aggregator > unsourced and adds `research/README.md:6-8` as "operator already demotes A/B/C genre." Those lines are the CDP 9222 / no-entitlement / `9/8/10` note. They do not state the four tiers. `SKILL.md:18` and `:28` do, and those lines did not move. The README attachment is unearned. The hierarchy itself is self-warrant, not independent evidence (see below).

2. **`QualityBar.md:73` Q-AXES** is admitted as a method cue from `A:54`, `README:13-14`, `C:67`, `B:57` only. No fleet gate states "do not collapse export axes into one research-record score." README:13-14 restates A's four axes as "usable." That is operator endorsement of export content, not a measured method rule. Should be `proposal` or an observation of the export.

3. **`QualityBar.md:75` Q-DELTA** admits a preference for localized deltas, and in the same cell says the ACE numbers at `B:77-79` are export-unverified and any numeric threshold is `proposal`. The preference and the numbers are one paragraph. The paragraph's "direct experimental evidence" is the unverified case study. Admitting the preference and refusing the numbers splits one warrant.

4. **`QualityBar.md:81` Q-RANK** admits "rank labels are not self-certified; permissions stay separate from vocabulary" on `C:53,65-67,85,126` plus `SKILL.md:38`. `SKILL.md:38` is still the kengaku refusal. It does not state that criterion. The rest is export content.

5. **`QualityBar.md:71` Q-EXP**, the clause "operator corrections outrank the export's casual wording." `README:6-8` and `:11-14` do not say the index outranks the export. Chrome-versus-paper is locally observable (`A:1-33`, footer `ChatGPT can make mistakes` at `A:90` / `B:81` / `C:135`). The authority ranking is not.

6. **`QualityBar.md:82` Q-ONE** admits "comma-stacked `file:1,2,3` anchors that break resolvers are defects," citing `citation-bases.md:104-106`. Those lines say comma lists defeat `resolve.py:74` and classify `GONE`. Re-opened: `resolve.py:74` is `EXTS = re.compile(...)`. The line-anchor regex is `LINEANCHOR` at `resolve.py:76`. Imported `is_pathlike("file.md:83,104,118")` is `False`; `LINEANCHOR` does not match; `strip_anchor` returns the token unchanged. The token is not extracted, so it is not `GONE`. Separately, `claim-ledger.sh:1115` fixtures `` `corpus/ok.txt:1,2,3` `` and `:1226` expects `CITATION_GATE: CLEAN` for that form. One "fleet" rule papers over a broken hop and a second instrument that accepts the form.

7. **`SearchStrategyTaxonomy.md:53` S1** admits "local inventory before remote." The evidence table cites resolver base order: `claim-ledger.sh:434-450` (citation classes for tokens already in a doc), `anchorcheck.py:21-48` (pin, origin, lane, mirror), `kumitate-shokunin/LOG.md:128-133` and `SKILL.md:664-667` (cite-check re-resolves path/line/symbol/pin). Those lines are not a research procedure of enumerating corpus, then `CORPUS.md`, then instruments, then dumps, before any remote search.

8. **`SearchStrategyTaxonomy.md:79`** says `IN-RANGE` "may be read as evidence," citing `anchorcheck.py:9-12`. The same file says range-valid is not semantic support (`anchorcheck.py:53-56`). QualityBar Q-MECH cites that split correctly. S2's core "resolve before trust" is still supported by `claim-ledger.sh:41-46`. The IN-RANGE row is not.

9. **`SearchStrategyTaxonomy.md:184`** admits "label hop; seed new chain" on `citation-bases.md:97-100`. Those lines forbid silently rewriting `~/Projects/bounties/...` to the mirror. They do not state the positive procedure.

10. **`CorpusMap.md:82`** admits README:10-14 as **secondary**, defined in the same row as "analysis that cites a primary and can be checked against it." README:10-14 names the export file and states corrections. It does not cite a dictionary or paper primary. The row's own definition is not met.

11. **`CorpusMap.md:130`** admits "Gate validates chain hops resolved-or-marked" on `SKILL.md:50-52`. Those lines are now blank / `## Gates` / blank (H1). Even against the pre-insert file, that cite was the contract sentence, not an observed run. At close the script exists (`chousa-shokunin/tools/research-gate.sh`, header `:8-9` says `RESEARCH_GATE: CLEAN|DRIFT`, exit 0/1/2). This seat did not run it. Existence is not a measured validation.

12. **`CorpusMap.md:276` S1** is marked admitted with the warrant "this round's NO EXTERNAL FETCHES contract; kagi/kasegi gates." No `path:line`.

13. **`CorpusMap.md:277` S2** includes `anchorcheck.py:63` as warrant for a path-resolve census. Line 63 is `Usage: python3 anchorcheck.py <file.md>`. The summary format is `:58-61`. `claim-ledger.sh:986-994` does support `CITATION_GATE: CLEAN|BROKEN`. `cite-check.mjs:69-70` is the exit contract (`CLEAN` / `DRIFT` / fail-closed), not "each broken hop listed." The row is not wholly unearned. The anchorcheck line is.

14. **`CorpusMap.md:283` S8** admits a stop rule on "A/B truncation; README `:7-8` non-DR note." Truncation is an incompleteness example. README:7-8 is the entitlement note, not a stopping rule.

15. **`RoundTwoPlan.md:350`** admits "Exports are not Deep Research primaries" on `research/README.md:6-8`, including burner Chrome CDP 9222, fired by L0, no Deep Research entitlement, and `9/8/10` web searches. Sweep of `research/`: those strings occur only in the README. The three exports contain `GPT-6 Astra` and `Searched the web` (A:42 once, B:42 once, C:42 and C:55). They do not contain the counts or the entitlement sentence. `ChainingDiscipline.md:143` records the same gap. Admitting the index sentence admits unreceipted session facts. The label "admitted (local)" discloses the base and still treats the note as settled.

16. **`LoopbackFixturePlan.md:128`** admits "report both; do not average" on `SKILL.md:29-30`. Line 29 is the dead-link row. Line 30 is the disagree row. Line 31 is blank. The disagree rule is on 30 only.

17. **`MINT.md:16-17`** says kasegi "explicitly refuses general source research" and cites `kasegi-shokunin/PROVINCE.md` with no line. That file's refusal, read this session, is "anything outside this domain" (`PROVINCE.md:25`). A grep of `kasegi-shokunin` for `general source research` returned no matches. The integrator sentence is `mint-roster-scan.json:13-14`. The scan's own authority line (`:4`) says these are integrator fit decisions, not consultations. The 17-row count and all 17 province sha256 pins matched current bytes at that read (`scanned_lanes` 17, `pin_mismatch` none). The count is earned. The verb "explicitly refuses," attached to the province file, is not. `MINT.md:22-23` uses the same verb for kengaku. `kengaku-shokunin/PROVINCE.md:6` refuses anything outside its domain; `:20` owns public literature for eval. It does not say it refuses general source research.

18. **`research/README.md:12-13`** states `jin'i-ryu` "is NOT an attested artisan rank" and "it's our coined term." `A:47` says "I haven't found evidence." `A:64` says "I could not substantiate this spelling" in "the Japanese or English sources searched." A contains no query list (`Searched the web` once, `A:42`). C:109 is a different claim (translation of "self-legislating school"), and its visible queries are two groups plus `10 more` undisclosed (`C:48`, `C:61`). A closed negative was admitted from a failed search in a truncated export. That is the round's central finding, one level up.

### Not counted as hard mislabels

- **Self-warrant.** CorpusMap, QualityBar, RoundTwoPlan, ChainHopFixture, and ChainingDiscipline admit the four-tier hierarchy, question-before-search, hop-walking, and don't-average by citing `SKILL.md:17-21` and `:27-30`. Those lines still say that, and they cite nothing further. A fleet-root sweep for `primary > secondary` and `source hierarchy`, then a walk of `*-shokunin/**/*.md` that was not gitignore-skipped, found the four-tier string only in chousa's own `SKILL.md`, `PROVINCE.md`, and `MINT.md` (plus `shokunin.conf:70` and this wave's assignment). No artifact states those four tier names. `A:56` is a different priority list (practitioners, workshops, museums) and is unverified export prose. Treating `SKILL.md:18` as evidence that the hierarchy is grounded repeats the uncited sentence.
- **`ChainHopFixture.md:23-27`** says the three skill bullets are "admitted from the lane skill, not from the exports," and records that `research-gate.sh` was absent at its sweep. That absence was true at this seat's earlier `test -f` and is false at close. The disclosure keeps it from being a hidden existence claim. The `:50-53` cite is now the shifted band (H1).
- **GateFixtureDesign RULE1** at `:309` is a synthetic PASS record citing `lib/fleet/chousa-skill-gates.md:1`. Not a fleet admission. Not counted in the 96.
- **Q-FALS** cites `SKILL.md:43-46` as "checklist spirit." Those lines, then and now, do not say falsifiable. `CORPUS.md:25` and `QUALITY.md:3` do. Partial extra cite.
- **Q-OIU** cites `CORPUS.md:38-40`, which is the negative-sweep rule, not the observation split. `SKILL.md:45` was the split at first read and is blank now (H1). `QUALITY.md:5` still supports the split.
- **Q-SEC** cites `claim-ledger.sh:84-86` (the gate does not echo claim output). `CORPUS.md:48-51` and current `SKILL.md:42` support "no secret values." The claim-ledger lines do not.

## What can be admitted without bootstrapping the skill

These fleet lines were opened and do state the rule. Seats that cite them for that rule are not the mislabels above.

| Rule | Local warrant opened this session |
|---|---|
| A negative claim carries its sweep | `CORPUS.md:38-40`; `PROTOCOL.md:336-337` |
| A count carries its command | `CORPUS.md:33-37`; `PROTOCOL.md:336-337` |
| A quote names its location | `CORPUS.md:41-44` |
| Falsifiable or marked opinion | `CORPUS.md:25` |
| An index row is a claim | `CORPUS.md:45-47` |
| No credential material in a corpus | `CORPUS.md:48-51` |
| Corrections are new entries; `LOG.md` is append-only | `CORPUS.md:52-55`; `PROTOCOL.md:443` |
| Evidence means a resolvable pointer | `PROTOCOL.md:329-331` |
| Ephemeral / tmpfs pointers are not evidence | `PROTOCOL.md:340-342`; `claim-ledger.sh:39-46` |
| A dead citation must be labelled where cited | `claim-ledger.sh:42-46` |
| Revision stamp is path, sha256, lines, bytes | `claim-ledger.sh:14-18` |
| In-range is not semantic support | `anchorcheck.py:53-56` |
| Name survival is not content survival | `kasegi-shokunin/corpus/instruments/README.md:35-40` |
| Citations mode can return CLEAN with zero recognized cites | `claim-ledger.sh:993`; selftest `cite-unchecked` at `:1223` |
| Prose self-score is not a re-checkable claim | `claim-ledger.sh:4-10`; `claim-ledger.md:19-22` |

The four-tier source hierarchy, "never start from a search box," "do not average," and "walk each external hop to the artifact" are not in that table. Hop-walking is not what `claim-ledger.sh citations` or `anchorcheck.py` do. Both can return clean on the three exports because the chips are not path citations (`ChainingDiscipline.md:108-116` reports that run; this seat did not re-run it).

## Export citation census (why export-sourced admissions stay unearned)

Commanded over the four `research/` files this session: **0** `https?://` URLs, **0** backtick `path:line` tokens in A/B/C. Domain chips and `+N` remnants are not openable locators (`A:68-69` `コトバンク` `+3`, `A:83-84` `adachi-hanga.com` `+2`, `B:72-73` `arxiv.org` `+6`, `C:82-83` `コトバンク` `+5`, `C:121-122` `+4`). Each answer stops at `ChatGPT can make mistakes` (`A:90`, `B:81`, `C:135`) and the retained bytes then show UI chrome. Pins: A `9033857d…` 6474 bytes, 109 newlines; B `6d8dbddd…` 5364 bytes, 100 newlines; C `e48fe70f…` 8922 bytes, 154 newlines; README `5199b23b…` 937 bytes, 17 newlines. A/B/C have no trailing newline, so `wc -l` is one short of `splitlines()` (110 / 101 / 155). CorpusMap's `A:107-109` as "Sources / Web search" is the shifted chrome under splitlines numbering (107-109 are Outputs / Create file or site / Sources; Web search is the unterminated last line).

`B:59` says the model distinguishes published findings from proposed engineering rules. The proposed rules are not in the truncated file. There is nothing there to admit.

## Residual risk

- Re-resolving the close set against current `SKILL.md` / `PROVINCE.md` without the +3 table will either fail the cite or attach the kumitate sentence to a sweep, pointer, or secrecy rule. That is the landing defect.
- `tools/research-gate.sh` exists at close and its header matches the skill's verdict words. This seat did not run `verify` or `--selftest`. A CLEAN banner in a later log is not this audit.
- `MINT.md` is 147 lines at close. Lines 14-18 were re-read and still carry the explicit-refusal attribution. The appended guard was not audited line by line.
- ChainingDiscipline's `## Proposals` section and design-report imperatives outside the token sweep are not in the 34.
- RuleOrProposal closed before CitationFormCensus, ClaimVsSourceCheck, NegativeClaimSweep, ChainHopFixture, and this file were on disk. Their findings were not used as this seat's measurements. Overlap on Q-HIER's README cite, the QUALITY item-number miss, and the README closed negative is agreement after separate reads, not a shared verdict.
