# kotodama — round 85

## Work performed

Declared claims: **D — depth**, a sourced metallurgy-register entry; **O —
operability / capability acquisition**, an explicit-root, duplicate-sensitive
corpus-index auditor. Base `0d181583b18ae94e80a251ca5ab5f3055b16c74c`; immutable freeze `ed816e71a97dde9b65f9265276b77c7583274671`.
Freshness remains paused by kotodama round-11's open L0 question beginning
“drift-recheck threshold calibration”; no stagnation waiver is asserted.

- **D: structural predicate verifies, source/body review completed.**
  `corpus/knowledge/culture-material/metallurgy-metal-register.md` lands at
  `5abe107204f1a98c754d49289e6a3c75ee3dfa44`: 27,848 bytes, ten sections, six decision rows, twenty
  single-id body anchors across four new sources, zero unknown ids and zero
  cited-line findings. Counter: `reports/round-85/lands-d.txt` PASS 8/8.
  Actual entry sha256 matches ReviewerEntry's reviewed snapshot byte-for-byte
  (`reports/round-85/noharm.json`). Source review independently located 20/20
  entry quotes and 5/5 row quotes in live and same-page archive bodies;
  `.ufo/waves/round-85/w1/stage/ReviewerEntry/review.md`.
- **O: after-predicate verifies; frozen before-premise partly falsified.**
  `tools/check-corpus-index.py` lands at `228e3a4c27ac2ea8e373de02a315cb5d94222d9b`: 23 isolated CLI
  checks, real 258-file index reconciled from 253 effective rows to 258,
  zero findings, frozen counter PASS 10/10 (`reports/round-85/lands-o.txt`).
  The earlier checker already existed **and already selected the last valid
  footer** after round-75 repair `012e8d3c`. The frozen first-footer statement
  is false and stays preserved. Genuine additions: explicit root,
  duplicate-row failure and malformed-final-footer refusal. Last-footer
  selection is a retained regression guard, not new acquisition. Evidence:
  `.ufo/waves/round-85/w1/stage/CriticClaims/critic.md` F3 and
  `ExecIndexReading/index-reading.json` in the same stage root.
- **Real domain task:** twelve translated-label semantic records across two
  fictional eras, four source/design bridges, NON-CANON prepared lore handoff:
  `reports/round-85/metallurgy-craft.json`. ReviewerEntry caught absent
  promised sense/clock fields; repaired records keep unknown native forms null
  and E1/E2 intervals explicitly fictional. Reproducible red/green:
  `reports/round-85/craft-ledger-red-green.json`, incomplete 12 → 0,
  exit 1 → 0. This grounds QUALITY criterion 32.
- **Record corrections:** all R84-C1–C9 (including carried R83-D2/D3)
  superseded in `reports/round-85/errata.md`, lesson and SCORECARD corrections;
  no old report, lesson, frozen declaration or receipt rewritten. In
  particular round-84 quality is unchanged and author-side dispositions are
  not discernment evidence.
- **Bounded preservation:** zero pre-existing knowledge files changed, zero
  old registry rows changed, PROVINCE byte-identical, all five historical
  footer blocks retained (`reports/round-85/noharm.json`). Combined index
  259 files / 259 rows / zero findings, registry 0 missing / 79 registered /
  0 dead, cited records 0 empty / 0 scratch, census exit 0 at data revision
  `76ff07078c4a13d2f9ddad0b9aaf72fd62db71ba` (`reports/round-85/final-checks.json`).

**Round shape:** ONE v1 wave, 12 seats, no residual call: 2 scout, 3 executor,
3 scribe, 1 connector, 1 reviewer, 1 critic, 1 mutation-tester. Attack roles
3/12 = 25%; one connector; planner held by L1. Parent WAVE-DONE received for
all twelve before this report. Spec/dispatch/results under
`.ufo/waves/round-85/`. Five substantive deliveries: ExecIndexAuditor,
ExecIndexReading, ReviewerEntry, CriticClaims, MutationTester. Seven settled
empty outputs: ScoutGapMetal, ScoutSourcesMetal, ExecControls, ScribeEntryMetal,
ScribeRows, ScribeErrata, ConnectorOverlap. **No replacements.** Results omit
status, answering-model and last-error metadata for those seats; their cause
of failure is unknown, not attributed to a provider. L1 completed their reachable
slices. Host routing read during the round: reviewer/critic/executor/
mutation-tester/sentinel → m_zfl; scout/scribe/connector → m_flash.
That is configured routing, not proof of any individual answering model.

**Admission qualification:** both unchanged after-predicates are green, but
this is **not an assertion of full round admission**. The O before-premise
is partly false. Counter authority, selftest and timing defects below remain
conformance defects; independent closure decides admission.

## Landed changes

All entries below tie to `LOG.md` **Round 85**, numbered items indicated.
Lane final tip **`798ed60e6752287cd03750672b35833273d7f6eb`** is pushed; pre-report `git ls-remote origin
refs/heads/main` printed that exact full hash.

| change | LOG item | landed commit |
|---|---|---|
| Frozen D/O declaration and structural counter, census start | opening, 5–6 | `ed816e71a97dde9b65f9265276b77c7583274671` |
| Pre-data base/freeze red controls and validated wave payload | opening, 5 | `bd520d85819a1ea6550061292263fc5bd6541396` |
| Index auditor, five omitted rows, two live headings, gate registry | 1 | `228e3a4c27ac2ea8e373de02a315cb5d94222d9b` |
| Metallurgy entry, S919–S923, worked ledger/red-green, QUALITY 32, L1 source reads and errata | 2–4 | `5abe107204f1a98c754d49289e6a3c75ee3dfa44` |
| Settled wave evidence, measured receipts, separability, final index row/footer, SCORECARD, LOG and lesson | 4–6 | `76ff07078c4a13d2f9ddad0b9aaf72fd62db71ba` |
| Final census/no-harm/misroot receipts and four current SHONEN evidence lines | 7 | `150f6be771f254b1eb919e59f0306b7ab985db34` |
| Close-evidence LOG tie | 7 | `798ed60e6752287cd03750672b35833273d7f6eb` |

No inherited uncommitted lane work was found at opening (helper state:
tracked=0, untracked=0). Non-author round-84 spot-check preserved unchanged.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`;
no attributed own round misroot found. Orchestrator `.scratch/` files left
untouched. Unassigned root `after` contains only `== SCORECARD diff base-`;
it names no lane/round and was left untouched (`reports/round-85/misroot-sweep.json`).

## Before → after measurements

The counter runs over committed blobs at `--lands`; its exact sha256 is
`f4611703c3b031a36fb8c3f2342be0659ee1d6840084022079e62d76195e2871`.
For each command below, supply an existing explicit directory for `--work`.

```sh
python3 -B reports/round-85/measure85.py --root . --claim D --lands 5abe107204f1a98c754d49289e6a3c75ee3dfa44 --freeze ed816e71a97dde9b65f9265276b77c7583274671 --work <existing-dir>
# ACCEPT-D-85: PASS legs=8/8; exit 0
python3 -B reports/round-85/measure85.py --root . --claim O --lands 228e3a4c27ac2ea8e373de02a315cb5d94222d9b --freeze ed816e71a97dde9b65f9265276b77c7583274671 --work <existing-dir>
# ACCEPT-O-85: PASS legs=10/10; exit 0
```

| claim | before at base / freeze | after at own lands |
|---|---|---|
| D | 258 knowledge files, 842 rows, entry absent, zero metallurgy/smelt/smith/foundry/alloy basename owners; counter FAIL 0/8 at base, 1/8 at freeze | 259th knowledge file, 847 rows, 27,848 B / 10 sections / 6 decisions / 20 anchors / 4 ids; PASS 8/8 |
| O | existing r28 sweep already last-footer/supplement aware; successor tool absent; base effective rows 253/258, five missing, two header drifts, total/footer/vector drifts (ten findings); counter FAIL 0/3 at base, 1/3 at freeze | tool present, 23 selftest checks; actual repaired 258-file tree clean; fresh nonce green/missing/duplicate/stale-final-footer/error controls pass; PASS 10/10 |

Before commands and outputs: `reports/round-85/baseline.json`,
`control-d-base.txt`, `control-d-freeze.txt`, `control-o-base.txt`,
`control-o-freeze.txt`; these were committed **after freeze but before dispatch**,
not inside the freeze. A do-nothing landing fails data predicates rather than
passing through a refusal. The combined tree later gives
`CORPUS-INDEX: OK files=259 rows=259 findings=0` (final-checks.json).

Separability: `python3 -B tools/check-claim-separability.py
reports/round-85/separability.json --root . --timeout 120 --budget 300 --jobs 1`
→ zero findings, two counterfactual base+one-claim acceptance runs, zero skipped,
exit 0 (`reports/round-85/separability.txt`). This ran **after dispatch**;
wrong nested argv first returned input exit 2 and is retained as
`separability-input-red.txt`. No late check is called pre-dispatch evidence.

**Counter/attack limits:** CriticClaims F1 demonstrates a selective inadequate
index stub can pass the O counter (out-of-protocol synthetic scratch-commit
experiment, explicitly not compliant committed acceptance). F2 shows missing
freeze-ancestry/LEGCOUNT guards and variable O denominator. The counter has no
conformant isolated selftest. Those are retained defects, not silently repaired
after scoring. MutationTester's separate transport-overlay tests killed seven
of eight mutants with clean/restored controls; wrong-source identity survived
D's structural URL/quote shape check. Actual source identities, body quotes,
implementation and selftest cases were separately read. These experiments do
not replace the actual committed-land measurements above. Counter unchanged
through the round; no target narrowed after data.

## Sources & frontier

Rows **842 → 847**, knowledge files **258 → 259**. New rows by tier:
**B 4 mined** (S919 Metallurgy, S920 Iron, S921 Bronze, S922 Alloys),
**C 1 rejected** (S923 Bronze Age's universal racial-stage/diffusion model).
Opened 2026-11-04. Literal existing-row old→new changes: **none**; status,
recheck and used-by cells of all 842 old rows are byte-identical. New rows'
URLs, locators, ≤25-word quotes and access dates are in the lesson Gate;
L1 receipts and independent reviewer live/archive records are committed.

Re-derive the row counts on immutable revisions:

```sh
python3 -c 'import re,subprocess; revs=["0d181583b18ae94e80a251ca5ab5f3055b16c74c","76ff07078c4a13d2f9ddad0b9aaf72fd62db71ba"]; [print(r,len(re.findall(r"^ {0,3}\|\s*S\d{3,}\s*\|",subprocess.check_output(["git","show",r+":corpus/SOURCES.md"],text=True),re.M))) for r in revs]'
# 0d181583b18ae94e80a251ca5ab5f3055b16c74c 842
# 76ff07078c4a13d2f9ddad0b9aaf72fd62db71ba 847
```

Census command (both runs):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`.
Full start output, exit 0:

```text
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	W01	S907 tierC mined used-by=corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md

exit=0
```

Full end output, exit 0:

```text
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	W01	S907 tierC mined used-by=corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
```

No new E-code; W01/W04 warnings are inherited. The new ore-to-metal naming-chain
surface moves into the corpus with one-way partial-owner links; no pre-existing
queued source row was advanced. Bounded source search log and study path added.
Mistakes R85-M1–M6 in the lesson include the false before-premise, incomplete
worked ledger and counter/timing defects. The field-completeness repair is
shown able to fail by the twelve-record red fixture and grounds QUALITY 32.

**Assimilation: none.** Staged `merge/kotodama/MERGE-REPORT.md` menu opened
read-only; no staged package adopted, no staged ids copied, no historical
quarantine verdict overridden. `considerthese/` absent. The L1's bounded
sibling-PROVINCE regex sweep found no metallurgy/smelting owner; canon and
world-bible acceptance stay lore's, general research method stays chousa's.
No engineering procedure, global archaeology or native etymology is acquired.

## Trend verdicts

- **expansion: improved.** New admitted source-scoped entry and demonstrated
  capability, indexed after landing. Evidence: D/O lands, four mined source
  rows, actual 259/259 combined index and SCORECARD capability row.
- **quality: unchanged.** No existing knowledge entry re-verified, deepened or
  superseded. New entries, instruments and record repairs do not fire this
  observable (LEARNING.md and QUALITY 20). Round-84's contrary statement is
  corrected in this round's errata.
- **discernment: improved.** The actual worked-ledger omission becomes
  grounded QUALITY criterion 32, with same-command red→green evidence and
  explicit null/fictional-clock semantics. Disposition counts and lane-dispatched
  reviewer agreement are not presented as an outside spot-check.

## SHONEN

- [~] Real decision tables, error patterns, checklists and cited sources:
  `SKILL.md` corresponding named headings and Gates and probes;
  `reports/round-85/final-checks.json`. Author assertion, no promotion verifier.
- [~] End-to-end domain task executed/logged: LOG round-85 items 2–3,
  `reports/round-85/metallurgy-craft.json`, `craft-ledger-red-green.json`.
- [~] Executable without oral context: explicit-root CLI, 23 isolated
  subprocess checks, frozen-land commands in `lands-o.txt` / `lands-d.txt`;
  known counter conformance gaps remain named.
- [~] No cross-domain bleed: `PROVINCE.md` unchanged, prior knowledge unchanged,
  `reports/round-85/noharm.json`; NON-CANON lore handoff and scope limits.

No `[x]`, promotion, canon acceptance or outside spot-check is self-granted.
Stale-lane: this is the sole respawn-per-round kotodama mission; progressing
through the listed own commits, no other mission of this lane is known open.
Open L0: round-11 freshness pause remains unresolved; no new question added.
Tool installs/upgrades: none; pacman pause respected. One critic seat reports
prohibited scratch Git mutations; its boundary violation is retained explicitly.
Own round scratch removed after all seats settled and lane work landed.
