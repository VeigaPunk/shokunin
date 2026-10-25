# kaika W1 — ART dossier: `kotodama` (linguistic-cultural worldbuilding)

- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` — HEAD `c42d675` (`git -C kotodama-shokunin rev-parse --short HEAD`), clean tree: `0` — `git -C kotodama-shokunin status --porcelain | wc -l`. Read-only; nothing in the repo was touched.
- Date: 2026-10-19. Author seat: W1ArtKotodama (scout). Every web row below was opened in this session.
- Tools: `web_search` available and used. Access failures are recorded, not hidden: Annual Reviews (HTTP 403), SSRN (403), Royal Society Open Science (403), De Gruyter (captcha), mapsofmyths.com (401), Princeton Index of Medieval Art (timeout ×2), Edition.fi (Anubis proof-of-work wall; only the page's metadata loaded).
- Local reads were limited to the ART shape (`corpus/README.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `SKILL.md` headings, `corpus/knowledge/` filenames), plus targeted `grep` sweeps of entry header and source lines. The sweeps ground the negative claims below; every count was run from the lane root.
- Prompt-injection report: none found. Two fetched pages carried untrusted non-target content, and neither contained directives aimed at the agent: `folgertkarsdorp.nl/momfer/` now serves a Dutch online-casino page (lapsed or hijacked domain), and Edition.fi serves an anti-scraper wall. I followed nothing from either.

## 0. Counts

| measure | value | command / basis |
|---|---|---|
| SOURCES rows drafted | 30 (A 23 / B 2 / C 5) | `grep -cE '^\| S[0-9]{3} ' kaika-w1-kotodama-art.md`; tiers: contract awk command on this file |
| row status | mined 8 / queued 14 / watch 5 / rejected 3 | column 7 of the §3 table |
| candidate knowledge entries | 6 (5 new files + 1 append-only amendment) | §4 |
| mistakes / hazards mined | 6 | §7 |
| lane defects found (ART-scope files) | 6 | §8 |

## 1. Uncovered ground

### 1.1 What the lane already holds (focus-relevant)

- Partitions: linguistics 25 / myth-symbol 26 / culture-material 26 / synthesis 29 / verification 24 / civilizations 94, total 224. Command: `ls corpus/knowledge/*/*.md | wc -l` → `224`. The vector is from the README footer, checked with `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (README:560-562).
- Conlang side: `conlang-methodology.md`, `phonetics-phonology.md`, `morphological-typology.md`, `syntax-typology.md`, `historical-linguistics.md`, `semantic-fields-lexicon-building.md`, `kinship-terminology.md`, `naming-systems.md`, `writing-systems.md`, and `synthesis/conlang-blueprint-template.md`.
- Folklore side: `myth-symbol/motif-index-usage.md` (TMI chapters, ATU grid, five-check palette audit), `myth-folktale-genres.md` (Bascom tiers; da Silva & Tehrani calibration), and `verification/myth-consistency-gate.md`.
- Costume and era: `dress-through-eras.md`, `costume-semiotics.md`, `garment-lexicon-crosslinguistic.md`, `sumptuary-law-rank-display.md`, `textile-technology.md`, `ritual-garments.md`, `era-periodization-models.md`, `calendar-festival-systems.md`, `timekeeping-instruments.md`, and `verification/costume-era-consistency-gate.md`.
- Symbols: the five-register method `symbolism-synthesis-method.md`, plus the color, animal, plant, mineral, number, direction, and celestial register files.
- `SKILL.md` headings are dominated by process: label typing, claim-uncertainty typing, slot-label routing, derivation replay, family-clean projection, register craft, gates and probes. No heading names an external-source discipline beyond "Using the evidence" (SKILL.md:558).

### 1.2 The frontier as recorded

- No `## Frontier` heading in the corpus index: `grep -cE '^## Frontier' corpus/README.md` → `0`. The nearest section is `## Known gaps (frontier)` (`1` match). It holds `12` bullets, all process residuals (rounds 5–7 rechecks, gate pins, header conformance, D2/D3 drills) and no domain topic: `sed -n '/^## Known gaps (frontier)/,/^Total knowledge entries/p' corpus/README.md | grep -c '^- '` → `12`.
- `PROVINCE.md` has no Core/Frontier/Adjacent headings: `grep -cE '^#+ .*(Core|Frontier|Adjacent)' PROVINCE.md` → `0`. It has Domain/Owns/Refuses bold labels and an "Adjacent contract" paragraph.
- Consequence: wave 2 has no lane-authored domain-frontier list to fill. The candidate entries in §4 name their gaps from negative sweeps and the partition rows.

### 1.3 Negative sweeps: sources the corpus never cites (from the lane root)

| source family | files | command |
|---|---|---|
| Grambank | 0 | `grep -rlE Grambank corpus/knowledge \| wc -l` |
| Kinbank | 0 | `grep -rlE Kinbank corpus/knowledge \| wc -l` |
| DatSemShift / Database of Semantic Shifts | 0 | `grep -rlE 'DatSemShift\|Database of Semantic Shifts' corpus/knowledge \| wc -l` |
| CALS | 0 | `grep -rlE '\bCALS\b\|cals\.info\|Conlang Atlas' corpus/knowledge \| wc -l` |
| Lexurgy | 0 | `grep -rlE '[Ll]exurgy' corpus/knowledge \| wc -l` |
| Index Diachronica | 0 | `grep -rlE 'Index Diachronica' corpus/knowledge \| wc -l` |
| MOMFER | 0 | `grep -rlE MOMFER corpus/knowledge \| wc -l` |
| ISEBEL | 0 | `grep -rlE ISEBEL corpus/knowledge \| wc -l` |
| PeriodO | 0 | `grep -rlE PeriodO corpus/knowledge \| wc -l` |
| Seshat / Cliopatria | 0 / 0 | `grep -rlE Seshat corpus/knowledge \| wc -l`; `grep -rlE Cliopatria corpus/knowledge \| wc -l` |
| ICOM costume vocabulary (word-bounded; see §7 M1) | 0 | `grep -rnE '\bICOM\b' corpus/knowledge \| wc -l` |
| Getty AAT | 0 | `grep -rlE 'Art (&\|and) Architecture Thesaurus' corpus/knowledge \| wc -l` |
| Lexis of Cloth and Clothing | 0 | `grep -rlE 'Lexis of Cloth' corpus/knowledge \| wc -l` |
| Iconclass | 0 | `grep -rlE Iconclass corpus/knowledge \| wc -l` |
| Index of Medieval Art | 0 | `grep -rlE 'Index of Medieval Art\|Index of Christian Art' corpus/knowledge \| wc -l` |
| ATU 2024 edition (in the motif entry) | 0 lines | `grep -c '2024' corpus/knowledge/myth-symbol/motif-index-usage.md` |
| "controlled vocabulary" (any) | 0 | `grep -rliE 'controlled vocabular' corpus/knowledge \| wc -l` |

(`\|` above is table escaping; type a bare `|` when pasting.)

Already held, so these become `mined` rows:
- WALS: `13` — `grep -rlE 'WALS|wals\.info' corpus/knowledge | wc -l`
- Thompson Motif-Index: `9` — `grep -rl Motif-Index corpus/knowledge | wc -l`
- Glottolog: `3` — `grep -rl Glottolog corpus/knowledge | wc -l`
- PHOIBLE: `2` — `grep -rl PHOIBLE corpus/knowledge | wc -l`
- D-PLACE: `2` — `grep -rlE 'D-PLACE' corpus/knowledge | wc -l`
- Rosenfelder/LCK: `2` — `grep -rlE Rosenfelder corpus/knowledge | wc -l`
- Berezkin: `1` — `grep -rl Berezkin corpus/knowledge | wc -l`
- Tehrani: `1` — `grep -rl Tehrani corpus/knowledge | wc -l`

### 1.4 The backlog a registry can serve

- `corpus/SOURCES.md` absent: `test -e corpus/SOURCES.md && echo present || echo absent` → `absent`.
- `(to-verify)` markers: `799` occurrences — `grep -ro '(to-verify)' corpus/knowledge | wc -l` — in `156` of 224 files (`grep -rl '(to-verify)' corpus/knowledge | wc -l`).
  - By partition (`for d in linguistics myth-symbol culture-material synthesis verification civilizations; do printf '%s ' $d; grep -ro '(to-verify)' corpus/knowledge/$d | wc -l; done`): linguistics 67, myth-symbol 42, culture-material 117, synthesis 100, verification 89, civilizations 384.
- Entries whose external shelf was written offline: `25` — `grep -rliE 'not consulted|no network' corpus/knowledge | wc -l`. Example: `cartography-and-mapmaking.md` says its external shelf is "**not consulted this round** (no network at seat time)" (line 18).
- Dataset versions unpinned: `0` WALS release strings (`grep -rnoE 'v20[0-9]{2}\.[0-9]+' corpus/knowledge | wc -l` → `0`) against `55` WALS lines (`grep -rnE 'WALS' corpus/knowledge | wc -l`). The lane's own profile already requires version identity: "One source ID denotes one consulted edition/version/witness, not an entire author's output." (`verification/citation-format-and-source-registry.md:75`). Only `1` Glottolog line carries a version number (`grep -rnE 'Glottolog [0-9]' corpus/knowledge | wc -l` → `1`, `civilizations/moche.md:39`, "Glottolog 5.3").
- ATU edition currency: `21` lines cite Uther 2004 (`grep -rnE 'Uther \(?2004' corpus/knowledge | wc -l`). There are `19` distinct ATU numbers (`grep -rhoE 'ATU [0-9]+[A-Z]?\*?' corpus/knowledge | sort -u | wc -l`) in `6` files (`grep -rlE 'ATU [0-9]+' corpus/knowledge | wc -l`). A 2024 revised edition exists (S016), and none of these lines names it.

### 1.5 Taste to preserve

- The corpus already refuses pop symbol dictionaries. `33` files mention "symbol dictionar…" (`grep -rliE 'symbol dictionar' corpus/knowledge | wc -l`), and sampled mentions are rejections, e.g. "Jungian symbol dictionaries", "pan-cultural symbol dictionaries", "A timeless, universally decoded symbol dictionary" (`grep -rhoiE '.{0,40}symbol dictionar.{0,30}' corpus/knowledge | head -6`).
- So the research brief's "symbol dictionaries" maps to iconographic *indexes* (Iconclass, AAT's boundary) rather than meaning dictionaries (S027, S029, §6 R1).

## 2. Current art (2025–2026) the corpus does not hold

| item | what is new | row | corpus |
|---|---|---|---|
| Glottolog 5.3 | about page titled "Glottolog 5.3" (release year not shown on the opened page); data curated in a public GitHub repo with releases | S001 | only 1 versioned line (moche.md:39) |
| WALS Online dataset v2020.6 | citation now names a Zenodo dataset DOI (10.5281/zenodo.23010827) distinct from the 2013 work | S002 | 0 release strings |
| D-PLACE 2026 edition | citation: Chira, Hrnčíř, Forkel, Greenhill, Gray (eds.) 2026, served at dplace2.clld.org | S007 | cited without edition (kinship-terminology.md:40) |
| Grambank v1.0 | site cites "The Grambank Consortium (eds.) 2024"; CC-BY-4.0 CLDF | S004 | 0 |
| DatSemShift 3.0 | 10,642 shifts / 52,241 realisations / 2,439 languages (home page, 2026-10-19) | S006 | 0 |
| CALS live census | 1323 conlangs, 127 natlangs, 145 features, "97.9% of all features are from WALS" | S009 | 0 |
| ConlangCrafter (2025) | LLM multi-hop conlang pipeline with diversity and consistency evaluation | S012 | 0 |
| ATU Revised and Supplemented Edition (Nov 2024) | FFC 284–286 reissued 2024; the FFC catalogue lists the 2004 Parts I–III as Open Access at Edition.fi | S016 | 0 |
| Berezkin–Duvakin catalogue | digital database state stated as of 24.12.2025; entries cross-reference TMI numbers and ATU types | S017 | 1 file (celestial only) |
| ISEBEL expanded | now five regions (adds Flanders and Iceland via Sagnagrunnur) | S019 | 0 |
| Automated motif indexing (2026) | first computational motif indexing; 0.85 F1 fine-tuned Llama3 on El-Shamy's Arabian Nights index | S020 | 0 |
| LLM narrative homogeneity (2026) | LLM stories converge; temperature and negative prompting do not fix it | S021 | 0 (the only 2 "language model" hits are non-LLM senses: swahili-coast.md:31, calibration-registry.md:110) |
| Cliopatria (2025) | open GeoJSON of 1600+ polities, 3400 BCE–2024 CE, linked to Seshat | S023 | 0 |
| Iconclass Consortium (2024) | the free browser depends on user-community support; consortium membership open from 1 July 2024 (home page) | S027 | 0 |

Opened but not registered (row cap of 30; available as swaps):
- Arčon, Robnik-Šikonja, Tratnik 2025, LLM motif detection on Cinderella variants — https://arxiv.org/abs/2510.18561
- Tsutsumi & Jinnai 2025, YokaiEval: 809 multiple-choice questions; Japanese-trained models beat English-centric ones — https://arxiv.org/abs/2506.03619
- Pulotu, about page — https://pulotu.com/about (its counts disagree with each other; see §7 M5)
- Hagedorn & Darányi 2022, aft corpus: 1518 ATU-annotated tales over 182 types, built from Ashliman — https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.78
- Costume Core introduction — http://www.ardenkirkland.com/costumecore/introduction
- KCI Digital Archives — https://www.kci.or.jp/en/archives/
- FIT Fashion History Timeline — https://fashionhistory.fitnyc.edu/about-timeline/
- FFC complete catalogue — https://www.folklorefellows.fi/ffc-catalogue/
- NWO ISEBEL project page — https://www.nwo.nl/en/projects/463-17-003

## 3. SOURCES.md rows (draft for `corpus/SOURCES.md`)

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Glottolog 5.3, About — https://glottolog.org/about.html | docs | A | languoid catalogue and genealogy (Hammarström classification merged with dialect-level data); data curated in a public GitHub repo with numbered releases; AES endangerment is derived from ELCat, UNESCO Atlas and Ethnologue — cite the version used | mined | 2026-10-19 | on-release | linguistics/naming-systems.md; civilizations/zapotec-mixtec.md; civilizations/moche.md |
| S002 | WALS Online, CLDF dataset — https://github.com/cldf-datasets/wals | dataset | A | cite the work (Dryer and Haspelmath eds. 2013) plus the DOI of the release used; wals.info now cites dataset v2020.6 (Zenodo 10.5281/zenodo.23010827); CC-BY-4.0 StructureDataset | mined | 2026-10-19 | on-release | linguistics/conlang-methodology.md and 12 more (§1.3) |
| S003 | PHOIBLE 2.0, dev repository — https://github.com/phoible/dev | dataset | A | more than 3000 phonological inventories for more than 2100 ISO 639-3 codes; one row per languoid-phoneme pair; use the latest release, not master; cite the inventory source (e.g. UPSID) inside PHOIBLE | mined | 2026-10-19 | on-release | linguistics/conlang-methodology.md; verification/phonology-sanity-gate.md |
| S004 | Grambank v1.0 — https://github.com/grambank/grambank | dataset | A | global structural-feature dataset in Glottobank, CC-BY-4.0 CLDF; cite Skirgård et al. (Science Advances) plus the release DOI; the web edition cites The Grambank Consortium (eds.) 2024 | queued | 2026-10-19 | on-release | — |
| S005 | Passmore et al. 2023, Kinbank, PLOS ONE 18(5) e0283218 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218 | paper | A | 210,903 kinterms from 1,229 languages in CLDF; worked null result: no coevolution of cross-cousin marriage and bifurcate-merging terms in Bantu | queued | 2026-10-19 | 180d | — |
| S006 | DatSemShift 3.0, Database of Semantic Shifts — https://datsemshift.ru/ | dataset | A | a shift is a meaning pair linked by derivation, attested as polysemy or as change over time, plus lexical-motivation patterns; 10,642 shifts, 52,241 realisations, 2,439 languages on 2026-10-19 | queued | 2026-10-19 | 180d | — |
| S007 | D-PLACE (2026 edition) — https://d-place.org/ | dataset | A | cross-cultural codings (Ethnographic Atlas and others) now cited as a 2026 edition (Chira, Hrnčíř, Forkel, Greenhill, Gray eds.) served at dplace2.clld.org; quote frequencies with the edition and sample | mined | 2026-10-19 | on-release | linguistics/kinship-terminology.md; civilizations/mesoamerica-primary-sources.md |
| S008 | Rosenfelder, The Language Construction Kit — https://zompist.com/kit.html | docs | B | naturalistic conlang order (sounds, lexicon, grammar, script, translation); working backwards from a text breeds incoherence; sequels ALC, Lexipedia, Syntax Construction Kit — practitioner method, not linguistic evidence | mined | 2026-10-19 | 365d | linguistics/conlang-methodology.md; linguistics/semantic-fields-lexicon-building.md |
| S009 | CALS, Conlang Atlas of Language Structures, statistics — https://cals.info/statistics/ | community | C | 1323 conlangs and 127 natlangs on 145 features, 97.9% of them taken from WALS; a census of conlanger choices, never evidence of natural-language typology | watch | 2026-10-19 | 90d | — |
| S010 | Lexurgy sound change applier — https://github.com/def-gthill/lexurgy | tool | A | GPL-3.0 Kotlin tool (CLI and web app) applying ordered regular rules to a word list; a deterministic replay engine for a conlang's sound history | queued | 2026-10-19 | on-release | — |
| S011 | Searchable Index Diachronica v10.2 — https://chridd.nfshost.com/diachronica/ | community | C | crowd-compiled attested sound changes searchable by segment; its maintainer did not write the Index and holds none of its sources, so trace every change to the cited source before use | queued | 2026-10-19 | 365d | — |
| S012 | Alper, Yanuka, Giryes, Beguš 2025, ConlangCrafter (arXiv 2508.06094) — https://arxiv.org/abs/2508.06094 | paper | A | LLM conlang pipeline staged phonology, morphology, syntax, lexicon, translation; randomness injected for diversity and self-refinement for consistency; evaluation on consistency and typological diversity | watch | 2026-10-19 | 90d | — |
| S013 | Thompson, Motif-Index of Folk-Literature (rev. 1955–58), digital edition — https://www.ruthenia.ru/folklore/thompson/indexleft.htm | spec | A | the 23 lettered chapters (A–Z without I, O, Y) online; an individually maintained digitization that asks readers to report errors, so check load-bearing IDs against print | mined | 2026-10-19 | 365d | myth-symbol/motif-index-usage.md; myth-symbol/myth-folktale-genres.md; +7 (grep -rl Motif-Index corpus/knowledge) |
| S014 | Karsdorp, van der Meulen, Meder, van den Bosch 2015, MOMFER, Folklore 126(1) 37–52 — https://www.theomeder.nl/momfer.pdf | paper | A | the TMI's measured defects: 45,000+ motifs, chapters A–K hold 78%, 72 motifs indexed twice, male/female motif skew 4178 vs 3318, India over-represented and Arab world thin; WordNet-expanded semantic search | queued | 2026-10-19 | 365d | — |
| S015 | Mellmann 2020, Thompson's Motif-Index as CSV (OSF 10.17605/OSF.IO/XEB67) — https://github.com/KatjaMellmann/TMI_as_CSV | dataset | B | CC-BY-4.0 CSV of the 1955–58 TMI built as a relational reference table, not a search tool; the basis for an executable motif-ID existence check | queued | 2026-10-19 | 365d | — |
| S016 | Uther, The Types of International Folktales, Revised and Supplemented Edition 2024 (FFC 284–286) — https://www.folklorefellows.fi/ffc-284-286-2024-edition/ | spec | A | 2024 is the third iteration and fifth revision since 1910; a type is international when identified among three or more cultural or national groups; its accompanying indices include the Thompson motifs referenced in type descriptions | watch | 2026-10-19 | on-release | — |
| S017 | Berezkin and Duvakin, World mythology and folklore: thematic classification and areal distribution of motifs — https://www.ruthenia.ru/folklore/berezkin/eng.html | dataset | A | defined motifs with areal indices beyond Europe, cross-referenced to TMI numbers and ATU types; inclusion in the digital database stated as of 24.12.2025 | mined | 2026-10-19 | 180d | myth-symbol/celestial-symbolism-calendars.md |
| S018 | da Silva and Tehrani 2016, Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales (PMID 26909191) — https://pubmed.ncbi.nlm.nih.gov/26909191/ | paper | A | phylogenetic, not spatial, signal in ATU magic-tale distributions; The Smith and the Devil inferred to the Bronze Age, a model-dependent inference rather than a dated text | mined | 2026-10-19 | 365d | myth-symbol/myth-folktale-genres.md |
| S019 | ISEBEL search engine — https://search.isebel.eu/ | dataset | A | belief-legend archive harvesting five regions (Netherlands, Flanders, Denmark, North-East Germany, Iceland) from the Folktale Database of the Low Countries, the Danish Folktale Database, WossiDiA and Sagnagrunnur | queued | 2026-10-19 | 180d | — |
| S020 | Alyami and Finlayson 2026, Automated Motif Indexing on the Arabian Nights (arXiv 2603.19283) — https://arxiv.org/abs/2603.19283 | paper | A | annotated 2,670 expressions of 200 El-Shamy motifs over 58,450 sentences; compared retrieval, embeddings and LLM prompting; best is fine-tuned Llama3 at 0.85 F1 | watch | 2026-10-19 | 90d | — |
| S021 | DK and Hatzel 2026, Do Large Language Models Always Tell The Same Stories? (arXiv 2606.17350) — https://arxiv.org/abs/2606.17350 | paper | A | LLM stories are more similar to each other than human stories across 10 models; negative prompting and temperature scaling fail to remove the homogeneity | watch | 2026-10-19 | 90d | — |
| S022 | PeriodO technical overview — https://perio.do/technical-overview/ | spec | A | a period needs a name, temporal bounds, a region and a citable source; start and stop are intervals with a verbatim label (authoritative) plus structured years; an authority (shared source) is not a periodization | queued | 2026-10-19 | 365d | — |
| S023 | Bennett et al. 2025, Cliopatria, Scientific Data 12:247 — https://www.nature.com/articles/s41597-025-04516-9 | paper | A | open GeoJSON of 1600+ polities from 3400 BCE to 2024 CE linked to Seshat; with rare exceptions polities need at least 5000 km2 and 50 years to be included; border uncertainty and disputes are not encoded | queued | 2026-10-19 | on-release | — |
| S024 | ICOM Costume Committee, Vocabulary of Basic Terms for Cataloguing Costume — https://terminology.collectionstrust.org.uk/ICOM-costume/vbt_ie.htm | spec | A | generic-first garment naming (basic term, then type, then variant), lists grouped by layer and body area, function recorded separately; its authors scope it to dress within the orbit of European style | queued | 2026-10-19 | 365d | — |
| S025 | Getty Art and Architecture Thesaurus, About the AAT — https://www.getty.edu/research/tools/vocabularies/aat/about.html | spec | A | 74,460 concepts (503,230 terms) under ODC-By; a Costume hierarchy within Furnishings and Equipment; term-level current/historical dates and Deprecated, Avoid-Use, Pejorative flags; no iconographic subjects or proper names | queued | 2026-10-19 | 180d | — |
| S026 | Lexis of Cloth and Clothing in Britain c.700–1450, research outline — http://lexisproject.arts.manchester.ac.uk/research/ | dataset | A | searchable medieval dress lexis across Old and Middle English, Welsh, Old Irish, Anglo-Norman, Medieval Latin and Anglo-Norse with date-range search; companion Encyclopedia of Medieval Dress and Textiles (Brill 2012) | queued | 2026-10-19 | 365d | — |
| S027 | Iconclass, top-level divisions — https://iconclass.org/en/_ | spec | A | ten divisions 0–9 for image subjects, two tied to one tradition (7 Bible, 9 Classical Mythology and Ancient History); Van de Waal's art-subject classification printed 1973–1985; consortium membership open since July 2024 | queued | 2026-10-19 | 180d | — |
| S028 | The Folklore Database — https://www.folkloredatabase.com/ | community | C | rejected: login-gated third-party aggregation of the Berezkin–Duvakin catalogue, ATU and Thompson that reserves text-and-data-mining and AI-use rights; use the primary catalogues (S013, S017) instead | rejected | 2026-10-19 | — | — |
| S029 | ARAS, Archive for Research in Archetypal Symbolism — https://aras.org/ | community | C | rejected: member-gated image archive framed as Jungian archetypal symbolism; universal-meaning readings fail QUALITY.md calibration (criterion 2); at most an image-finding lead | rejected | 2026-10-19 | — | — |
| S030 | Vulgarlang conlang generator v14.4.2 — https://www.vulgarlang.com/ | tool | C | rejected: paywalled one-click generator (200-word demo); its output is an unprovenanced design artifact and cannot support any knowledge claim (QUALITY.md criterion 1) | rejected | 2026-10-19 | — | — |

Opened-source quotes behind the rows (≤25 words each):
- S008 (zompist.com/kit.html, opening section): "Working backwards (e.g. creating a text and then devising a grammar to match) will lead to an inconsistent if not incoherent work."
- S009 (cals.info/statistics, "Quick numbers"): "97.9% of all features are from WALS".
- S011 (diachronica page, "Some notes about sources"): "I (chridd) did not write the Index Diachronica itself."
- S016 (FFC 2024 edition page, opening summary): "The ATU catalog is constituted of international types, practically defined as identified among three or more cultural or national groups."
- S022 (§Authorities): "Belonging to the same authority does not imply any semantic relationship between periods, other than sharing a source."
- S024 (Introduction, Anne Buck): "They apply to fashionable and unfashionable dress within the orbit of European style."
- S028 (home page footer): "expressly reserves all rights in relation to text and data mining, automated extraction, scraping, machine learning".

Paste-ready counting on the table (contract commands):
- rows: `grep -cE '^\| S[0-9]{3} ' kaika-w1-kotodama-art.md`
- tiers: `grep -E '^\| S[0-9]{3} ' kaika-w1-kotodama-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`

### Leads (unopened)

- Schreyer 2021, "Constructed Languages", *Annual Review of Anthropology* 50:327–344, doi 10.1146/annurev-anthro-101819-110152 — 403 at Annual Reviews and SSRN.
- ConlangCrafter's ACL 2026 acceptance: reported only by search snippets, not verified on an opened page.
- Grambank paper counts (195 features, 2,467 varieties): search snippets only. Open Skirgård et al. 2023, *Science Advances* 9(16) eadg6175 before quoting them.
- Kinbank v1.2 (57 added languages): ANU portal snippet only.
- CALS archived on GitHub 2025-09-03 and moved to Codeberg: search snippet only.
- Uther 2024 Introduction and Part I–III contents PDFs linked from the FFC page: needed before asserting any 2004→2024 renumbering.
- Edition.fi OA PDFs of ATU 2004, books 763/765/769 — blocked by Anubis.
- El-Shamy 2006, *A Motif Index of The Thousand and One Nights* (the S020 index).
- Ikeda 1971 (FFC 209) and Ting 1978 (FFC 223): regional indices listed on the FFC catalogue.
- Heda Jason 2000, *Motif, Type and Genre* (FFC 273), a manual for compiling indices — directly relevant to the lane's in-world index practice (motif-index-usage.md:72).
- MOMFER parsed TMI and code — github.com/fbkarsdorp/tmi (cited in S014, note 7).
- Declerck, Kostová, Schäfer 2017, DH2017 linked-data ATU/TMI abstract.
- Multilingual Folk Tale Database (MFTD).
- Princeton Index of Medieval Art — timed out ×2.
- Getty Iconography Authority (IA), named on the AAT page.
- Warburg Iconographic Database.
- Seshat databank proper (seshat-db.com); ChronOntology; Pleiades; Trismegistos People; Europeana Fashion; Met Open Access API.
- Encyclopaedia of Medieval Dress and Textiles (Brill 2012).
- Kümmel 2007, *Konsonantenwandel*; Blevins 2004, *Evolutionary Phonology*; SegBo; LAPSyD; AUTOTYP; Lexibank/CLICS current release.
- Thuillard, Le Quellec, d'Huy, Berezkin 2018 (world myth motifs; contested macro-phylogeny).

## 4. Candidate knowledge entries

Every candidate must clear `corpus/QUALITY.md` criteria 1–5: provenance, calibration, coupling, usability, canon hygiene. Each card states how.

### C1 — `myth-symbol/iconography-index-usage.md` (new row under `## myth-symbol/`)

- **Claim (falsifiable).** Iconclass's top level has exactly ten divisions, 0–9, and two of them are bound to single traditions ("7 · Bible", "9 · Classical Mythology and Ancient History"). An Iconclass palette over a fictional culture's symbols is therefore an etic, Western-art grid whose bins are uneven by construction.
  - Rule: tag symbols with `cf.` plus the nearest notation, never mint notations, ship the palette, and never read bin counts as the culture's emphasis.
  - Falsifier: re-opening https://iconclass.org/en/_ shows a different number of top-level divisions or different labels.
- **Source and location.** iconclass.org/en/_ (top-level list); iconclass.org/help/about, General introduction: "Henri van de Waal began to develop ideas for a universal classification for the subject matter of works of art" (19 words).
- **Boundary.** S025 says the AAT "contains no iconographic subjects", so AAT is the object and material vocabulary, not the subject index.
- **Gap filled.** Narrative has an external grid (`motif-index-usage.md`); the five symbol registers in `symbolism-synthesis-method.md` have none. Sweep: `grep -rlE Iconclass corpus/knowledge | wc -l` → `0`. By contrast, `66` files mention "iconograph…" (`grep -rliE 'iconograph' corpus/knowledge | wc -l`) without any notation system.
- **Couples.** `symbolism-synthesis-method.md`, `motif-index-usage.md` (shares its `cf.` notation and never-mint rule, §7), `color-symbolism.md`, `animal-symbolism.md`, `plant-symbolism.md`, `mineral-stone-symbolism.md`, `verification/real-world-inspiration-boundaries.md`.
- **Recheck.** Re-open iconclass.org/en/_ (expect 10) and iconclass.org/help/about; consortium status 180d.
- **QUALITY.**
  1. Two opened primary pages.
  2. Calibration: Iconclass's "universal" ambition is contradicted by its own division design. Label it mainstream as a museum indexing standard, not as a source of symbol meaning.
  3. Coupling: listed above.
  4. Usability: a tagging procedure plus palette table.
  5. Canon hygiene: reference only, handed to lore.

### C2 — `culture-material/period-assertion-records.md` (new row under `## culture-material/`)

- **Claim (falsifiable).** An era label enters a handoff only as a *period assertion* with four parts: a name, temporal bounds, a spatial association, and a citable source.
  - Start and stop are intervals. Their verbatim textual label is authoritative over any structured year.
  - Periods that merely share a source (an authority) do not thereby form a periodization.
  - Falsifier: PeriodO's overview lists different admission conditions, or treats structured years as authoritative.
- **Source and location.** https://perio.do/technical-overview/
  - §Linked Data: "To be included in the gazetteer, a period must give the period a name, impose some temporal bounds on the period" (21 words; the list continues with region and citable source).
  - §Temporal extent: "The skos:prefLabel of an interval should be considered the authoritative description."
  - §Authorities: the S022 quote in §3.
- **Calibration exemplar (S023, Methods).** Polities "occupy at least 5000 km2 and have a duration of at least 50 years". Also: "The dataset does not currently encode possible border uncertainty and territorial disputes." An era map's silences are inclusion thresholds; this couples to the cartography entry's "map's silences".
- **Gap filled.** `era-periodization-models.md` separates emic and etic periodization (§1) but has no record schema. `era-material-scoped-reconciliation.md` resolves design-local tags with no source or extent fields. Sweeps:
  - `grep -c 'assertion' corpus/knowledge/culture-material/era-periodization-models.md` → `0`
  - `grep -c 'assertion' corpus/knowledge/synthesis/era-material-scoped-reconciliation.md` → `0`
  - `grep -rlE PeriodO corpus/knowledge | wc -l` → `0`
- **Couples.** `era-periodization-models.md`, `synthesis/era-material-scoped-reconciliation.md`, `calendar-festival-systems.md`, `cartography-and-mapmaking.md`, `linguistics/naming-systems.md` (era names), `synthesis/era-language-staging.md`.
- **Recheck.** Re-open the three PeriodO sections (365d); Cliopatria on release.
- **QUALITY.**
  1. Two opened primary documents.
  2. Calibration: PeriodO warns that gYear values are "not, in general, convertible" to other calendars, so a non-Gregorian in-world calendar keeps its textual label authoritative.
  3. Coupling: listed above.
  4. Usability: a record template plus three decision rules.
  5. Canon hygiene: a resolution or assertion record is never a dating of canon.

### C3 — amendment §8 to `myth-symbol/motif-index-usage.md` (append-only; adds no index row)

Precedent for an amendment without a new row: README revision 1.9 records the round-28 §13 amendment as "a new section in an existing entry and adds no index row" (README:78-80).

- **Claim (falsifiable).** The ATU now exists as a Revised and Supplemented Edition (FFC 284–286, Jelgava 2024: Part I 651 pp., Part II 547 pp., Part III 340 pp.).
  - The entry's "cite this edition" instruction for Uther 2004 (`motif-index-usage.md:7`) is incomplete. Its own edition-drift rule (§3, line 71; §7, line 114) now has a third edition: every ATU number must name 2004 or 2024.
  - The 2024 definition of an international type ("identified among three or more cultural or national groups") gives the five-check audit (§5) a concrete in-world spread test.
  - Falsifier: the FFC page lacks the 2024 edition or the definition, or `grep -c '2024' corpus/knowledge/myth-symbol/motif-index-usage.md` is already >0 (it is `0`).
- **Sources and locations.**
  - S016, FFC 2024 page: "This is the third iteration of the index and its fifth revision since it was first published in 1910." (19 words)
  - S014, MOMFER p. 39, Accessibility section, a palette baseline: "with categories A – K containing seventy-eight per cent of all motifs in the index" (14 words).
  - S015, the CSV, enables an executable motif-ID existence check. Its first target set is `8` dotted IDs in the entry (`grep -rhoE '\b[A-HJ-NP-XZ][0-9]{1,4}(\.[0-9]+)+\b' corpus/knowledge/myth-symbol/motif-index-usage.md | sort -u | wc -l`).
- **Gap filled.** The entry's own recheck trigger: "re-check the index edition and re-run the §7 spot-check" (`motif-index-usage.md:17`).
- **Couples.** `myth-folktale-genres.md` (§3 type-age; its Europe-anchoring caveat at :64 stands), `trickster.md`, `hero-journey-variants.md`, `naming-systems.md`, `orality-formulaic-language.md`, `comparative-frameworks.md`. All cite Uther; 21 lines total (§1.4).
- **Recheck.** Re-open the FFC 2024 page; read the Part I contents PDF (a lead) before asserting any renumbering. Until then, the 19 cited numbers stay "ATU 2004".
- **QUALITY.**
  1. Publisher pages.
  2. Calibration: the amendment claims no number changed, because that is unknown until the contents are read.
  3. Coupling: listed above.
  4. Usability: a citation rule, a spread test, and an ID-existence check.
  5. Canon hygiene: as the parent entry.

### C4 — `linguistics/typology-database-selection.md` (new row under `## linguistics/`)

- **Claim (falsifiable).** Each conlang design question has one primary open dataset, and every figure taken from it cites the dataset release:

  | design question | primary dataset | row |
  |---|---|---|
  | phoneme-inventory plausibility | PHOIBLE 2.0 | S003 |
  | feature co-occurrence | WALS release / Grambank v1.0 | S002 / S004 |
  | language identity, family, sampling | Glottolog 5.3 | S001 |
  | kin-term systems | Kinbank | S005 |
  | semantic change paths | DatSemShift 3.0 (CLICS is already held for colexification) | S006 |
  | cultural correlates | D-PLACE 2026 | S007 |
  | conlang-population comparison only | CALS (C) | S009 |
  | diachrony replay | Lexurgy | S010 |
  | attested-change leads | Index Diachronica (C) | S011 |

  Falsifier: a maintainer's stated scope contradicts a row, or the corpus already holds such a table (it does not: Grambank, Kinbank, DatSemShift, CALS, Lexurgy and Index Diachronica are each `0` in §1.3).
- **Sources and locations.**
  - S003 README: "make use of the most recent release in your own analyses, rather than working from the tip of the master branch" (21 words).
  - S002 README: "the derived dataset using the DOI of the particular released version you were using" (14 words).
  - S009 statistics: "97.9% of all features are from WALS".
- **Defect it repairs.** `0` release strings against `55` WALS lines (§1.4), despite `citation-format-and-source-registry.md:75`.
- **Couples.**
  - `conlang-methodology.md` (whose source list at :4 has no question→dataset table), `phonetics-phonology.md`, `morphological-typology.md`, `syntax-typology.md`, `historical-linguistics.md`, `semantic-fields-lexicon-building.md`, `synthesis/symbol-lexicon-colexification.md`, `verification/phonology-sanity-gate.md`, `verification/citation-format-and-source-registry.md`.
  - `kinship-terminology.md`: it already says "Quote frequencies only from a sample you name" at :40. Kinbank's Bantu null result calibrates its "encodes weakly" framing.
- **Recheck.** On release per dataset; pin census `grep -rnoE 'v20[0-9]{2}\.[0-9]+' corpus/knowledge | wc -l`.
- **QUALITY.**
  1. Maintainer-authored pages.
  2. Calibration: CALS is flagged non-typological; samples must be named and genealogically controlled (Glottolog families).
  3. Coupling: listed above.
  4. Usability: the decision table.
  5. Canon hygiene: no canon.

### C5 — `verification/generated-inventory-diversity-check.md` (new row under `## verification/`)

- **Claim (falsifiable).** A tale or myth inventory drafted by a language model cannot be presumed diverse. Measured LLM narratives are more similar to each other than human stories, and temperature scaling or negative prompting does not fix this.
  - The check: compute the inventory's motif-chapter palette (the `motif-index-usage.md` §5 audit) across independent drafts.
  - Compare against the TMI baseline, A–K = 78% (S014), declaring that baseline's own skews: male 4178 vs female 3318 motifs; India over-represented, Arab world thin.
  - Record which drafts converge.
  - Falsifier: the S021 abstract reports a mitigation that works. A no-convergence result passes the check and does not falsify the rule that diversity must be measured.
- **Sources and locations.**
  - S021 abstract: "LLM-generated narratives are consistently more similar to each other than human-written stories are." (13 words)
  - S012 abstract: "injecting randomness to encourage diversity and leveraging self-refinement feedback to encourage consistency" (diversity is engineered, then measured).
  - S020: automated motif tagging is feasible (0.85 F1, fine-tuned).
- **Gap filled.** The verification partition checks packets, records and gates, but not generated-content homogeneity. Sweep: `grep -rliE '\bLLMs?\b|language model' corpus/knowledge | wc -l` → `2`, both non-LLM senses.
- **Adjacency.** Prompt craft is kotoba's province (`PROVINCE.md:20`). This entry measures artifacts only; report prompting advice, don't absorb it.
- **Couples.** `motif-index-usage.md` §5, `myth-folktale-genres.md`, `verification/verification-independence-anti-circularity.md`, `verification/worked-example-verification.md`, `synthesis/worked-example-mini-culture.md`.
- **Recheck.** arXiv versions every 90d.
- **QUALITY.**
  1. Three papers plus MOMFER.
  2. Calibration: preprints; S021 measured r/WritingPrompts stories, not folk tales, so the transfer to tale inventories is an inference, flagged as such.
  3. Coupling: listed above.
  4. Usability: a procedure plus a record.
  5. Canon hygiene: no canon.

### C6 — `culture-material/costume-cataloguing-vocabularies.md` (new row under `## culture-material/`)

- **Claim (falsifiable).** A wardrobe lexicon is catalogued generic-first:
  1. A basic term by layer and body area: main garment, outerwear, protective, underwear, supporting/shaping, night/dressing.
  2. A type term.
  3. An optional variant or ephemeral term.

  Function goes in a separate field: the ICOM introduction says "the basic term for bathing or wedding dress alike is *Dress*". Every term carries date and status flags (current/historical, deprecated, avoid-use), and every vocabulary declares its scope bias.
  - Falsifier: the ICOM introduction lacks the generic-first principle or the European-orbit scope sentence, or the AAT page lacks the flags.
- **Sources and locations.**
  - S024 Introduction: "The principle followed is that a basic generic term should be the first catalogue name for each garment or accessory." (20 words); scope sentence quoted in §3.
  - S025: "Dates for the Terms" and "Other Flags" (Avoid Use / Deprecated / Pejorative).
  - S026: date-range search across seven medieval languages.
- **Scope calibration (opened, not registered).** KCI "systematically collects and preserves outstanding examples of western clothing through the centuries". FIT plans "coverage of non-western fashion as well" as future work. Open costume infrastructure skews Western, so non-Western dress must come from the culture-specific sources in `civilizations/`.
- **Gap filled.** `garment-lexicon-crosslinguistic.md` (how languages name garments) and `costume-semiotics.md` (sign systems) exist; nothing covers cataloguing vocabularies. Sweeps: `\bICOM\b` 0, AAT 0, Lexis 0, "controlled vocabular" 0 (§1.3).
- **Couples.** `garment-lexicon-crosslinguistic.md`, `dress-through-eras.md`, `costume-semiotics.md`, `sumptuary-law-rank-display.md`, `verification/costume-era-consistency-gate.md`, `synthesis/glossary-registry-format.md`, `synthesis/costume-language-coupling-table.md`. The last has 13 lines carrying `(to-verify)` — `grep -c '(to-verify)' corpus/knowledge/synthesis/costume-language-coupling-table.md` — the first discharge targets.
- **Recheck.** ICOM and AAT pages every 180d; Lexis search availability.
- **QUALITY.**
  1. Three primary standards.
  2. Calibration: every vocabulary's scope is stated, and none is treated as universal.
  3. Coupling: listed above.
  4. Usability: a three-tier naming template plus a flag set.
  5. Canon hygiene: no canon.

## 5. Paths

- **Folk-narrative indexing:** S013 → S014 → S015 → S016 → S017 → S020. Why this order:
  1. The index as published.
  2. Its measured defects.
  3. Its machine-readable form.
  4. The current type edition with its motif crosswalk.
  5. An areal catalogue reaching beyond Europe.
  6. Current-art automated indexing, read last because it presupposes all of the above.
- **Conlang typology:** S008 → S003 → S002 → S004 → S001 → S006 → S010 → S011 → S012. Why this order:
  1. Practitioner method.
  2. Phonology data.
  3. Structural features.
  4. Genealogy for sampling.
  5. Semantic change.
  6. A replay tool, then attested-change leads.
  7. The LLM pipeline, evaluated against everything earlier.
- **Era and costume records:** S022 → S023 → S024 → S025 → S026. Why this order:
  1. What a period record is.
  2. A worked polity dataset and its silences.
  3. Garment naming principles.
  4. A controlled vocabulary with dated and flagged terms.
  5. A period-specific multilingual lexis that exercises all of it.

## 6. Rejected candidates (with reasons)

- **R1 — a "universal symbol dictionary" entry** (Chevalier & Gheerbrant / Cirlot / ARAS-style meanings). It fails `corpus/QUALITY.md` criterion 2 (calibration). It also contradicts standing taste (33 files reject symbol dictionaries, §1.5). ARAS was opened and rejected as S029; Chevalier and Cirlot were not opened and get no rows. Replacement: C1 (an index, not a dictionary).
- **R2 — a CALS-based "naturalness statistics" entry.** CALS profiles 1323 self-reported conlangs on features that are 97.9% WALS's (S009). Its frequencies describe conlanger fashion; publishing them as typology launders hobby distributions. CALS stays a C/watch row only.
- **R3 — a deep-time myth-dating entry** (assigning "Bronze Age" to a fictional culture's tales from phylogenetic or areal-motif results). S018 infers one tale's age under model assumptions. `myth-folktale-genres.md:63` already flags such claims as contested. A generator built on it would turn a contested inference into a design rule.
- **R4 — a "ConlangCrafter as the lane method" entry.** The lane's method entry already stages the same layers (`conlang-methodology.md:3`). The paper evaluates consistency and diversity metrics, not naturalism. Pipeline and prompt engineering border kotoba's province. Kept as a watch row (S012).
- **R5 — sources rejected as rows:** S028 (rights reservation, login, third-party aggregation), S029 (Jungian universalism, membership), S030 (generator output, no provenance).
- **R6 — a dead or hijacked lead:** `https://www.folgertkarsdorp.nl/momfer/` now returns an unrelated online-casino page, so it is not even a rejected row. MOMFER is registered through its peer-reviewed paper (S014).

## 7. Mistakes and hazards mined (this session; each is a reusable taste rule)

- **M1 — substring false positives in negative sweeps.** A combined regex counted `10` "ICOM" hits that were all `ICOMOS`: `grep -rnoE 'ICOM[A-Z]*' corpus/knowledge | sed -E 's/^[^:]+:[0-9]+://' | sort | uniq -c` → `10 ICOMOS`. The word-bounded sweep returns `0` (`grep -rnE '\bICOM\b' corpus/knowledge | wc -l`). Rule: a negative claim's sweep uses word boundaries and prints what matched.
- **M2 — a URL that still answers is not the same source.** folgertkarsdorp.nl serves gambling content. Rule: a `recheck` re-opens the page and compares content against the row's `teaches` line, not just the HTTP status.
- **M3 — open access is not agent-fetchable.** Edition.fi (ATU OA PDFs) sits behind an Anubis proof-of-work wall; publishers returned 403 or a captcha. Rule: record the access failure and fall back to PubMed, arXiv or the repository record (done for S018 after the RSOS 403). The lane already practises named access failures (SCORECARD.md:463).
- **M4 — content negotiation returns a citation, not a page.** grambank.clld.org, wals.info, phoible.org and d-place.org returned `text/plain` citations only. Rule: ground `teaches` in the repository README or about page (done: S002, S003, S004).
- **M5 — sources disagree with themselves.**
  - The Pulotu about page says "137 Austronesian cultures and 63 variables" and, in its Variables section, "a total of 88 variables".
  - Cliopatria's README says "approximately 14K records"; the 2025 paper says "approximately 15 K records".
  - Rule: a count carries its location and date, never just the source name.
- **M6 — writing offline makes `(to-verify)` debt.** `25` entries say their shelf was "not consulted" or written with "no network" (§1.4), most recently `cartography-and-mapmaking.md` (round 48). Rule: a round that writes entries opens its shelf in the same round and registers it in SOURCES.md. This is the operator goal's "curation of sources" applied to the lane's own failure mode.

## 8. Lane defects found (ART-scope files only; STATE owns the full contract audit)

- **D1 — ATU edition currency.** `motif-index-usage.md:7` instructs "cite this edition" for Uther 2004; the 2024 Revised and Supplemented Edition is unmentioned (`grep -c '2024' corpus/knowledge/myth-symbol/motif-index-usage.md` → `0`). Repair: C3.
- **D2 — unpinned dataset versions.** `0` WALS release strings against `55` WALS lines, despite `citation-format-and-source-registry.md:75` (§1.4). Repair: C4 plus the SOURCES rows S001–S007.
- **D3 — no domain frontier.** `## Known gaps (frontier)` holds `12` process bullets and no `## Frontier` heading (§1.2).
- **D4 — `PROVINCE.md` lacks Core/Frontier/Adjacent headings.** `0` matches (§1.2).
- **D5 — README revision log.** `revision: 2.0` appears twice, and `revision: 1.9` is missing although the footer cites "Revision 1.9":
  - `grep -c '^revision: 2\.0' corpus/README.md` → `2`
  - `grep -c '^revision: 1\.9' corpus/README.md` → `0`
  - README:55 is a truncated duplicate of README:57. The revision-1.9 body (README:71) starts mid-sentence with no header line.
- **D6 — `corpus/SOURCES.md` absent** (§1.4). Also observed and left to STATE: `68` entries lack a `- source:` header line (`grep -rLE '^- source:' corpus/knowledge | wc -l`).

## 9. Hand-off notes for wave 2

1. **Land SOURCES.md from §3 (30 rows, 23 A).**
   - Re-open each row on the day of writing; the contract's `opened` field belongs to the row author.
   - Use the rows to discharge `(to-verify)` markers where a row's `teaches` covers the claim. Count before→after with `grep -ro '(to-verify)' corpus/knowledge | wc -l` (`799` now).
2. **Pick candidates that need no further fetching.**
   - C3 is an append-only amendment that repairs D1; it measures as `grep -c '2024' …motif-index-usage.md` 0 → ≥1.
   - C2 and C1 fill zero-coverage rows. Each counts as +1 index row, verified by `python3 -B reports/round-28/readme/sweep.py` (the lane's existing sweep).
3. **Axis note.**
   - SCORECARD records freshness as "historically the lowest non-retired axis" (SCORECARD.md:14-15), but freshness axis-moves are paused pending an operator ruling (e.g. SCORECARD.md:591, :945).
   - Unless the operator lifts the pause, frame registry and recheck work under coverage (new rows) and calibration (version pins, D2). Take the lowest-axis call from the STATE dossier.
4. **Keep the taste line.** Iconographic indexes yes, meaning dictionaries no. CALS and Index Diachronica are C leads only. LLM-generated inventories must pass a measured diversity check, not a prompt tweak.
