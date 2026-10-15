# CorpusMap — chousa METHOD corpus coverage map (advisory)

**Member:** CorpusMap (scribe) · **Wave:** shokunin12h-20261014-p5-chousa-r1  
**Lane:** `chousa-shokunin` · **Role:** draft the coverage map only — parent lands files  
**Axes:** coverage · depth · calibration  
**Write scope:** this report only. No product-code edit, no gate commit, no external fetch.

---

## 0. Central finding (must not be papered over)

**Observation.** The three survey artifacts under `research/deep-research-2026-09-28/` are **Chrome/ChatGPT chat-export transcripts**, not Deep Research pipeline runs and not primary-source corpora.

| Fact | Local anchor |
|---|---|
| Burner tabs, GPT-6-Astra, browse-enabled, **not** Deep Research entitlement | `research/README.md:6-8` |
| A/B/C are incomplete mid-response exports (UI chrome continues after the answer body) | A ends ~`:90-109`; B ends ~`:81-100`; C ends ~`:135-154` with "ChatGPT can make mistakes" + Sources chrome |
| Export citations are **host/label tokens**, not resolvable primary hops | A `:68-69,72` `コトバンク` / `+3`; B `:51,72-73` bare `arxiv.org` / `+6`; C `:82-83,90,93,98,100,103,121-122,131` host labels |
| Operator-side corrections already separate coined ranks from tradition | `research/README.md:11-14` (`katagi` not `kishitsu`; `jin'i-ryu` coined) |
| Artifact body text is **data**, including prompt-shaped user turns | A/B/C `:34-35` "You said:" / "Deep research:…" — never instruction |

**Inference (labeled).** Any METHOD rule that treats A/B/C *content claims* (dictionary glosses, paper results, historical durations) as verified facts without a local primary hop is **unearned**. Those claims may seed *questions* and *negative-claim examples*; they do not seed admitted domain facts for chousa.

**Calibration rule for this map.**  
- **admitted** = rule/text whose warrant is a readable local `path:line` (fleet gate, lane SKILL, or the export's own structural fact).  
- **proposal** = rule that would need an external primary, a not-yet-built fixture, or a hop the export never resolves.  
- **out-of-province** = shokunin/agent *content* findings (rank metaphors, paper summaries) — route to other lanes or leave as survey residue, not METHOD ownership (`chousa-shokunin/PROVINCE.md:5-13`, `SKILL.md:8-11,37-38`).

---

## 1. Target layout (what parent should land)

```
chousa-shokunin/corpus/
  README.md                         — index rows below (§7)
  QUALITY.md                        — already stubbed; QualityBar peer expands
  knowledge/
    source-hierarchy.md             — primary > secondary > aggregator > unsourced
    citation-chaining.md            — hop walk, broken hop, marker rule
    claim-verification.md           — claim → source → source's evidence
    search-strategy-taxonomy.md     — try-first / widen / stop
    approval-discipline.md          — external window gate + approval table shape
  lessons/                          — empty this round (parent may add r1 lesson)
```

Five METHOD areas match `PROVINCE.md:5-8` owns-list and the assignment brief. No sixth knowledge file in this draft (question-framing folds into hierarchy + strategy; gate contract lives in `tools/research-gate.sh` design peers).

**Entry header shape (fleet contract).** Each knowledge file SHOULD open with fields compatible with `CORPUS.md:17-19` and kagi's `Reverify:` tooth (`kagi-shokunin/corpus/claim-ledger.sh:53-58,825-826`):

```
# <title>
source: <local paths this entry is built from>
verified-at: 2026-10-14 (local read-only survey; no external hop)
recheck: <command or "by-hand: …">
Reverify: by-hand: interactive-only — <≥24 char reason>   # until claim-ledger rows exist
```

Until chousa has its own stamps/claim-ledger, `Reverify: by-hand: interactive-only — …` is the honest form (kagi vocabulary at `claim-ledger.sh:59-60`); inventing fake `R*-*` ids would violate the idref rule (`claim-ledger.sh:47-51`).

---

## 2. `knowledge/source-hierarchy.md` — hierarchy

### 2.1 Purpose
Decision table: **primary > secondary > aggregator > unsourced**. Rank every cited object before a claim is admitted.

### 2.2 Contract anchors (admitted)

| Line payload the entry will carry | Status | Source |
|---|---|---|
| Intent row: Rank sources → primary > secondary > aggregator > unsourced claim; never treat aggregator as primary | admitted | `chousa-shokunin/SKILL.md:18` |
| Error: aggregator quoted as primary → hierarchy violation; re-derive from primary | admitted | `chousa-shokunin/SKILL.md:28` |
| Owns hierarchy tiers by name | admitted | `chousa-shokunin/PROVINCE.md:5-6` |
| QUALITY: every claim carries measured anchor (path:line / command / evidence id) | admitted | `chousa-shokunin/corpus/QUALITY.md:4` |
| Observation / inference / unknown stay separate | admitted | `QUALITY.md:5`; `SKILL.md:45`; B export names the same failure mode as literature *claim* (not verified): `research/.../B-multiagent-knowledge.md:77` |

### 2.3 Tier table (local examples only)

| Tier | Definition (METHOD) | Local positive example | Local negative / broken example | Status |
|---|---|---|---|
| **primary** | Artifact whose bytes *are* the fact under claim (source text, gate source, measured command output) | `kagi-shokunin/corpus/claim-ledger.sh:31-46` (citation rule text is the gate's own primary); `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-61` (verdict vocabulary is instrument primary) | Export A claims "Daijisen / Nihon Kokugo Daijiten / Kanjipedia" (`A:67`) but the only local hop is bare `コトバンク` (`A:68-69`) — **no primary present locally** | admitted definition; primary *dictionary* examples remain **proposal** until external window |
| **secondary** | Analysis that cites a primary and can be checked against it | `research/README.md:10-14` operator corrections over the exports (secondary on A/C structure) | A `:80-88` workshop narratives cited only via host tokens (`adachi-hanga.com` `A:83`) — secondary *shape* without local primary | admitted shape; content unverifiable locally |
| **aggregator** | Index / summary / UI citation chip that collapses many sources | Chat export "Sources / Web search" chrome (`A:107-109`, `B:98-100`, `C:152-154`); bare `arxiv.org` + `+N` (`B:71-73`); `コトバンク` + `+N` (`A:68-69`, `C:82-83`) | Using `+6` as if six papers were read | admitted: aggregator *form* observed in artifacts |
| **unsourced** | Assertion with no pointer | A `:52` "strongest historical model…" before any cite; B `:55` literature-support claim before Sources line | — | admitted as defect class |

### 2.4 Rules the entry should state

1. **admitted** — Rank is about *epistemic role in the record*, not prestige of the domain (`SKILL.md:18`).  
2. **admitted** — An aggregator hop never upgrades a claim; it only names where to walk next (`SKILL.md:28`).  
3. **admitted** — Export body claims that name external dictionaries/papers without a resolvable local primary are recorded as **unverified-local**, not admitted facts (central finding §0).  
4. **proposal** — Formal mapping of "practitioner interview / museum report / dictionary entry / peer-reviewed paper" into the four tiers needs external primaries or a loopback fixture; mark any such sub-taxonomy `proposal` until round-2 loopback.

### 2.5 Explicit rejections (keep with reason)

| Rejected move | Reason | Anchor |
|---|---|---|
| Treat A/B/C dictionary gloss tables as primary Japanese lexicography | Export is aggregator of unknown browse results; no local dictionary bytes | A `:60-72`, C `:73-85` |
| Treat B paper table (`B:63-69`) as verified literature | Bare titles + `arxiv.org` host; no arXiv ids, no PDFs | B `:71-73` |
| Collapse skill / teaching authority / permission into one hierarchy ladder | C itself warns against collapse — content finding, not METHOD ownership | C `:53,65-67` — **out-of-province content**; METHOD only keeps the *meta-rule* "don't collapse independent axes" as analogy **proposal** |

### 2.6 Source-line inventory (minimum set the file must cite)

```
chousa-shokunin/SKILL.md:17-21,27-30
chousa-shokunin/PROVINCE.md:5-8
chousa-shokunin/corpus/QUALITY.md:3-7
research/README.md:6-14
research/deep-research-2026-09-28/A-shokunin-tradition.md:56,60-72,83-84
research/deep-research-2026-09-28/B-multiagent-knowledge.md:59,63-73,77
research/deep-research-2026-09-28/C-rank-taxonomy.md:65-67,81-85
kagi-shokunin/corpus/claim-ledger.sh:31-46
kasegi-shokunin/corpus/knowledge/citation-bases.md:1-18
```

---

## 3. `knowledge/citation-chaining.md` — chaining

### 3.1 Purpose
How a citation **chain** is walked hop-by-hop; what a **broken hop** looks like; how dead pointers stay labelled rather than silent.

### 3.2 Contract anchors (admitted)

| Payload | Status | Source |
|---|---|---|
| Follow each hop to the cited artifact; never stop at a summary of the citation | admitted | `SKILL.md:19` |
| Chain ends at dead link → record hop and stop | admitted | `SKILL.md:29` |
| Reuse finding → cite artifact + revision read | admitted | `SKILL.md:21` |
| Checklist: resolvable pointer to artifact and revision | admitted | `SKILL.md:43` |
| Gate validates chain hops resolved-or-marked | admitted | `SKILL.md:50-52` |

### 3.3 Fleet precedents (EVIDENCE of enforcement already live)

| Precedent | What it enforces | Lines |
|---|---|---|
| **kagi claim-ledger `citations` mode** | Path-shaped tokens must resolve or be line-labelled dead; session URIs are EPHEMERAL | `claim-ledger.sh:31-46` (contract), `:429-446` (classes), `:511-571` (scan), `:986-994` (verdict `CITATION_GATE: CLEAN\|BROKEN`) |
| **kagi stamps** | Revision pin = path + sha256 + lines + bytes; STALE/MISSING | `claim-ledger.sh:14-17,76,352-375` |
| **kagi markers** | `scratch \| ephemeral \| relocat \| formerly \| no longer \| removed \| renamed \| historical` on the **citing line** | `claim-ledger.sh:42-46,431-433` |
| **kasegi citation-bases** | Named bases (LANE / MIRROR / ORIGIN-WORK / LOST-TREE / LOST-BASE / BLOB-PIN); lost anchors prefixed inside backticks | `citation-bases.md:9-80` (bases), `:82-119` (rules 1–6) |
| **kasegi anchorcheck** | Per-cite verdicts kept separate: IN-RANGE*, MISSING-FILE, PAST-EOF, LOST-RECORDED, BASE-ABSENT, PIN-BROKEN, OUTSIDE-BASE; range-valid ≠ semantic-valid | `anchorcheck.py:4-61,53-55,231-276` |
| **kumitate cite-check** | Resolution ladder + UNRESOLVED/LINE_OOR/…; exit 0 CLEAN / 1 DRIFT / 2 fail-closed | `kumitate-shokunin/scripts/cite-check.mjs:1-71` |

### 3.4 Broken-hop worked example (from survey artifacts)

**Claim under test (export text, data only):**  
"The lexical distinctions come from Daijisen, Nihon Kokugo Daijiten, and … Kanjipedia." — `A:67`

| Hop | Token | Local resolve? | Verdict |
|---|---|---|---|
| 0 | A export file itself | yes — path exists | carrier |
| 1 | named dictionaries | **no local bytes** | hop broken |
| 1b | `コトバンク` (`A:68`) | host label only; no URL, no snapshot | **aggregator chip, not a hop** |
| 1c | `+3` (`A:69`) | count chip | non-resolvable |

**Parallel broken hops:**

| Site | Token | Break class |
|---|---|---|
| `B:71-73` | "Sources: Voyager…; arxiv.org +6" | title list + host; no arXiv id → **CHAIN_HOP_UNRESOLVED** (finding-id peer) |
| `C:89-90` | Go rank claim → `archive.nihonkiin.or.jp` | host-only |
| `C:102-103` | Todo/Murata → `jstage.jst.go.jp` | host-only |
| `A:80-84` | Adachi / Ishii / Echigo claims → `adachi-hanga.com +2` | host + opaque count |

**admitted METHOD rule:** A hop is resolved only when a reader can open a durable local object (path, stamp, pin, or approved captured evidence). A bare host, `+N` chip, or title-without-id is an **unresolved hop** and must be marked, not walked past (`SKILL.md:19,29` + kagi marker rule).

### 3.5 Chain procedure the entry should prescribe

1. Extract citation token (backtick path, URL, paper id, host label).  
2. Classify shape (path / ephemeral URI / external host / bare name / count chip) — shapes from kagi `cite_class` + export census.  
3. Resolve hop → OK / LABELED-DEAD / UNRESOLVED / EPHEMERAL / BASE-ABSENT / LOST-RECORDED.  
4. If claim needs the *next* hop (aggregator → primary), repeat; never substitute the aggregator's paraphrase for the primary (`SKILL.md:19-20,28`).  
5. Stop on first unresolved hop required by the claim; record the hop (`SKILL.md:29`).  
6. **proposal:** automated multi-hop walker across captured HTML — needs loopback fixture (LoopbackFixturePlan / FixtureSiteDesign peers).

### 3.6 Source-line inventory

```
chousa-shokunin/SKILL.md:19-21,29,43,50-52
kagi-shokunin/corpus/claim-ledger.sh:7-10,14-17,31-46,76-78,429-446,511-571,986-994
kasegi-shokunin/corpus/knowledge/citation-bases.md:1-18,82-119
kasegi-shokunin/corpus/instruments/anchorcheck.py:4-61,53-55,231-276
kumitate-shokunin/scripts/cite-check.mjs:1-71
research/deep-research-2026-09-28/A-shokunin-tradition.md:67-69,83-84
research/deep-research-2026-09-28/B-multiagent-knowledge.md:71-73
research/deep-research-2026-09-28/C-rank-taxonomy.md:81-83,89-103,120-122
```

---

## 4. `knowledge/claim-verification.md` — verification

### 4.1 Purpose
**claim → source → the source's own evidence**. Status vocabulary: verified / contradicted / unresolved (and fleet extensions).

### 4.2 Contract anchors (admitted)

| Payload | Status | Source |
|---|---|---|
| Verify path: claim → source → source's own evidence; never accept restatement as source | admitted | `SKILL.md:20` |
| Source cited but not read → unsupported; unresolved | admitted | `SKILL.md:27` |
| Two sources disagree → report both; do not average | admitted | `SKILL.md:30` |
| Negative claim carries search sweep | admitted | `SKILL.md:44`; fleet rule `CORPUS.md:38-40` |
| Rejection kept with reason | admitted | `SKILL.md:46`; `QUALITY.md:7` |
| Falsifiable or marked opinion | admitted | `QUALITY.md:3`; `CORPUS.md:25` |
| Count carries its command | admitted | `CORPUS.md:33-37` |
| Quote names its location | admitted | `CORPUS.md:41-44` |

### 4.3 Verification status table (admitted + fleet extensions)

| Status | Meaning | Local warrant |
|---|---|---|
| **verified** | Claim text supported by opened primary bytes at cited revision | kagi claim row: exit match + last-line ERE (`claim-ledger.sh:24-30`); anchorcheck IN-RANGE* then **manual semantic** check (`anchorcheck.py:53-55`) |
| **contradicted** | Opened source denies the claim | (no A/B/C local example — **proposal** until loopback disagree-fixture) |
| **unresolved** | Required hop missing, unread, or out of window | A/B/C external cites; `SKILL.md:27` |
| **unverified-local** | Export asserts external primary; this host cannot open it (this round's default for A/B/C content) | §0 |
| **STALE / MISSING** | Revision pin drifted or absent | `claim-ledger.sh:76,352-375` |
| **LOST-RECORDED / BASE-ABSENT** | Historical base deliberately non-openable or tree gone | `anchorcheck.py:17-19,30-31,73-74` |
| **LABELED** | Dead pointer acknowledged on citing line | `claim-ledger.sh:42-46,566-568` |

### 4.4 Five load-bearing survey claims → local checkability (map feeds ClaimVsSourceCheck)

| # | Claim (paraphrase) | Site | Local check result |
|---|---|---|---|
| 1 | `jin'i-ryū` not attested artisan rank | A `:47,64`; C `:53,109`; README `:12-13` | **structural agreement across local exports + operator note** — still not primary-lexicon verified; status **unverified-local** for the linguistic fact, **verified** for "exports + README assert this" |
| 2 | 職人気質 read *katagi* not *kishitsu* | A `:47,71`; README `:11-12` | same as #1 |
| 3 | ACE brevity-bias case: 18282→122 tokens, acc 66.7→57.1 | B `:79` | **unverified-local** — no paper bytes |
| 4 | No traditional four-rank ladder matching mint→…→mint-siblings | C `:65` | negative claim; local sweep possible only over these three files — **proposal** for full sweep protocol (NegativeClaimSweep peer) |
| 5 | Apprenticeship durations 5–9 years (Adachi/Ishii/Yoita) | A `:80-86` | **unverified-local** — host-only cites |

### 4.5 Observation / inference / unknown discipline

Carry B's failure-mode *label* as METHOD requirement even though the paper citation is unresolved:

- **observation** = what the opened bytes say (`B:77` names the risk of losing this distinction).  
- **inference** = what we conclude beyond the bytes.  
- **unknown** = hop not opened / out of approval window.

**admitted** from lane QUALITY + SKILL; B line is illustrative residue only.

### 4.6 Source-line inventory

```
chousa-shokunin/SKILL.md:20,27,30,43-46
chousa-shokunin/corpus/QUALITY.md:3-7
CORPUS.md:33-51
kagi-shokunin/corpus/claim-ledger.sh:24-30,76-81,766-772
kasegi-shokunin/corpus/instruments/anchorcheck.py:53-55
research/deep-research-2026-09-28/A-shokunin-tradition.md:47,64,71,80-86
research/deep-research-2026-09-28/B-multiagent-knowledge.md:57-59,77-79
research/deep-research-2026-09-28/C-rank-taxonomy.md:53,65,109
research/README.md:11-14
```

---

## 5. `knowledge/search-strategy-taxonomy.md` — strategy taxonomy

### 5.1 Purpose
Ordered strategies: what to try first, how to widen, when to stop — grounded in fleet practice where it exists.

### 5.2 Observed strategies in the survey exports (descriptive, not endorsed)

| Export behavior | Site | METHOD reading |
|---|---|---|
| Declare multi-part question up front | A/B/C `:35` | **admitted** good form — matches `SKILL.md:17` "question framing first" |
| "Searched the web" with opaque result set | A `:42`; B `:42`; C `:42,55` | **admitted defect example** — no query log, no hit list retained |
| Site-scoped queries shown as chrome | C `:44-46` (`site.nihonkiin.or.jp…`, `site.kodokanjudoinstitute.org…`) | shows *intent* to prefer institutional hosts; **queries themselves not replayable** without network |
| Quoted-string probes for negative claims | C `:57-59` (`"自己立法" "自律"`, `"jin'i-ryu"`) | negative-claim sweep *shape*; results not retained |
| Stop mid-answer (A/B truncated) | A `:88-90`; B `:79-81` | **incompleteness** → stop-rule input (StopRule peer); not a valid stop |

### 5.3 Taxonomy the entry should carry

| ID | Strategy | Try when | Widen by | Stop when | Status | Local warrant |
|---|---|---|---|---|---|---|
| S0 | **Frame the question** | always first | split multi-part questions into numbered claims | question is single falsifiable unit or explicit multi-claim list | **admitted** | `SKILL.md:17`; A/B/C `:35` as positive form |
| S1 | **Local primary first** | any claim about fleet/lane state | sibling lanes, stamps, instruments | local primary opened or proven absent (sweep recorded) | **admitted** | this round's NO EXTERNAL FETCHES contract; kagi/kasegi gates |
| S2 | **Path-resolve census** | citations present in a doc | kagi citations mode / anchorcheck / cite-check | CLEAN or each broken hop listed | **admitted** | `claim-ledger.sh:986-994`; `anchorcheck.py:63`; `cite-check.mjs:69-70` |
| S3 | **Negative-claim sweep** | "no X", "not attested", "absent" | broaden patterns, second tool, second tree | sweep commands recorded with zero/non-zero hits | **admitted** shape | `SKILL.md:44`; `CORPUS.md:38-40`; C `:57-59` as *shape* only |
| S4 | **Aggregator → primary walk** | only aggregator in hand | follow each chip to durable object | primary opened or hop marked unresolved | **admitted** | `SKILL.md:19,28`; broken hops §3.4 |
| S5 | **Disagreement retain** | two sources conflict | do not average; capture both spans | both retained with pointers | **admitted** | `SKILL.md:30` |
| S6 | **Loopback multi-source** | need agree/disagree/silent without external net | fixture site with ≥3 sources | claim-capture table filled | **proposal** (round 2) | contract deliverable; no fixture bytes yet |
| S7 | **External approved fetch** | operator approval row = granted | only targets in approval table; capture evidence to local store | scope limit hit or evidence captured | **proposal** until approval table granted | `SKILL.md:34-36`; `PROVINCE.md:11-12` |
| S8 | **Stop / yield incomplete** | diminishing returns or hard boundary | — | unknowns listed; no silent fill | **admitted** incomplete-export lesson | A/B truncation; README `:7-8` non-DR note |

### 5.4 Falsification conditions (for proposals)

| Strategy | Falsified if |
|---|---|
| S6 loopback | Fixture sources do not actually disagree/silent on the seeded question (harness can check) |
| S7 external | Fetch occurs with approval state ≠ granted, or evidence not captured locally |
| S3 sweep | Absence claimed without command, or command not re-runnable |

### 5.5 Source-line inventory

```
chousa-shokunin/SKILL.md:17-21,30,34-36,44
chousa-shokunin/PROVINCE.md:5-12
CORPUS.md:38-40
research/README.md:6-8
research/deep-research-2026-09-28/A-shokunin-tradition.md:35,42,88-90
research/deep-research-2026-09-28/B-multiagent-knowledge.md:35,42,79-81
research/deep-research-2026-09-28/C-rank-taxonomy.md:35,42-48,55-61
kagi-shokunin/corpus/claim-ledger.sh:986-994
kasegi-shokunin/corpus/instruments/anchorcheck.py:53-56,63
kumitate-shokunin/scripts/cite-check.mjs:69-76
```

---

## 6. `knowledge/approval-discipline.md` — approval discipline

### 6.1 Purpose
External live-target research is **forbidden** until an operator approval table says otherwise. The table is a chousa deliverable, not a permission slip written by the agent.

### 6.2 Contract anchors (admitted)

| Payload | Status | Source |
|---|---|---|
| Refuses external live-target research without operator approval | admitted | `SKILL.md:34-36`; `PROVINCE.md:11-12`; SKILL frontmatter anti-trigger `:3` |
| Window without approval table is **loopback-only** | admitted | `SKILL.md:34-35` |
| Approval table is itself a chousa deliverable | admitted | `SKILL.md:35-36` |
| Secrets/session shape-only; no secret values | admitted | `SKILL.md:39`; `PROVINCE.md:12-13`; `CORPUS.md:48-51` |
| Refuses kasegi bounty scope / kengaku model-quality | admitted | `SKILL.md:37-38`; `PROVINCE.md:10-11` |

### 6.3 Approval table schema (draft columns — all rows `pending` until operator acts)

Parent/ApprovalTable peer owns the filled table; this entry owns the **discipline**.

| Column | Meaning | Admitted from |
|---|---|---|
| `target` | Exact host/path/paper id allowed | contract "scope limit" |
| `why` | Which unresolved hop / claim needs it | §3 broken hops |
| `scope_limit` | max pages / max bytes / no-login / no-paywall-bypass | hard boundary |
| `evidence_to_capture` | what must land locally (HTML snapshot path, PDF hash, quote span) | chaining + verification |
| `approval_state` | `pending` \| `granted` \| `denied` \| `expired` | only operator flips from pending |
| `granted_by` / `granted_at` | empty while pending | — |
| `capture_path` | local path once captured | revision pin candidate |

**Seed pending rows the discipline entry should list (not fetch):**

| target (proposed) | why | scope_limit | evidence_to_capture | state |
|---|---|---|---|---|
| Kotobank / Daijisen entries for 職人気質, 見習い, 職人 | resolve A `:67-72`, C `:81-85` hops | single entry pages; no account | saved HTML + sha256 + quoted gloss span | pending |
| arXiv abs pages for Voyager/ACE/… named in B `:63-69` | resolve B `:71-73` | abs + pdf only for named titles; no crawl | arXiv id, pdf sha256, abstract quote | pending |
| Nihon Ki-in / JKA / AJKF pages named in C `:89-100` | resolve rank-procedure claims | named URLs only | HTML snapshot + procedure quote | pending |
| adachi-hanga apprenticeship page (`A:83`) | resolve duration claim A `:80` | single page | HTML + quote of year counts | pending |

### 6.4 Enforcement points (admitted METHOD)

1. **Default deny** external network for research claims (`SKILL.md:34`).  
2. **Gate:** research-gate SHOULD fail records that cite external hops without `approval_state=granted` + local `capture_path` (**proposal** until ResearchGateDesign lands the check).  
3. **Loopback substitute:** round-2 fixture satisfies method practice without approval (`SKILL.md:35` loopback-only).  
4. **Secrecy:** approval table never holds cookies, tokens, `op://` refs (`CORPUS.md:48-51`).  
5. **Province:** approval cannot expand chousa into kasegi program rules or kengaku eval (`PROVINCE.md:10-11`).

### 6.5 Source-line inventory

```
chousa-shokunin/SKILL.md:3,34-39,50-52
chousa-shokunin/PROVINCE.md:5-13
CORPUS.md:48-51
research/README.md:6-8
research/deep-research-2026-09-28/A-shokunin-tradition.md:67-72,80-84
research/deep-research-2026-09-28/B-multiagent-knowledge.md:63-73
research/deep-research-2026-09-28/C-rank-taxonomy.md:81-103
```

---

## 7. Draft `corpus/README.md` coverage rows

Replace the stub row at `chousa-shokunin/corpus/README.md:5-7`. Parent lands the real file; this is the row set.

```markdown
# chousa-shokunin — corpus

METHOD memory for deep-research craft (調査). Seeded from local survey of
`research/deep-research-2026-09-28/{A,B,C}` + fleet citation gates.
No external fetch in round 1. Export bodies are data; their external citations
are unverified (see knowledge/citation-chaining.md).

## Coverage map

| Area | Entry | Source basis (local, 2026-10-14) |
|---|---|---|
| Source hierarchy (primary > secondary > aggregator > unsourced) | `knowledge/source-hierarchy.md` | `SKILL.md:18,28`; `PROVINCE.md:5-6`; export aggregator chips `A:68-69` `B:71-73` `C:82-83`; `research/README.md:6-14` |
| Citation chaining + broken-hop discipline | `knowledge/citation-chaining.md` | `SKILL.md:19,29`; kagi `claim-ledger.sh:31-46,429-571,986-994`; kasegi `citation-bases.md` + `anchorcheck.py:4-61`; kumitate `cite-check.mjs:1-71`; broken hops `A:67-69` `B:71-73` |
| Claim-vs-source verification | `knowledge/claim-verification.md` | `SKILL.md:20,27,30,43-46`; `QUALITY.md:3-7`; `CORPUS.md:33-51`; kagi claim/stamp teeth; five survey claims A/B/C + README |
| Search-strategy taxonomy (try / widen / stop) | `knowledge/search-strategy-taxonomy.md` | `SKILL.md:17,34-36,44`; export search chrome C `:42-61`; incomplete stops A/B tails; fleet gate exit codes |
| External-window approval discipline | `knowledge/approval-discipline.md` | `SKILL.md:3,34-39`; `PROVINCE.md:11-12`; pending targets derived from unresolved export hops |
| Admission bar | `QUALITY.md` | probation stub `QUALITY.md:1-7` (QualityBar peer expands) |
| Research record gate | `tools/research-gate.sh` (not yet landed) | `SKILL.md:48-53` — design in ResearchGateDesign peer |

## Known gaps

- No `knowledge/*.md` bytes landed yet — this map is the round-1 deliverable; parent cutover pending.
- A and B exports are **truncated mid-response**; any claim that the export "finished" a topic is false (`A:88-90`, `B:79-81`).
- Zero external primaries on disk for dictionary/paper/institutional cites named inside A/B/C.
- No chousa `claim-ledger` / `stamps.tsv` yet — knowledge `Reverify:` must use by-hand form until built.
- No loopback fixture site yet — S6 strategy is proposal (round 2).
- Approval table rows all `pending` — not a grant.
- `lessons/` empty — round-1 lesson owed after parent lands gate + notes.
- kumitate cite-check is cross-lane precedent only; chousa does not absorb kumitate src-tree semantics.

## Frontier (next honest moves)

1. Land the five knowledge files from this map with path:line cites only.
2. Land `tools/research-gate.sh` + hermetic fixtures (peers).
3. Round-2 loopback agree/disagree/silent exercise before any external grant.
4. Operator review of approval table; still no fetch until `granted`.
```

---

## 8. Cross-cutting calibration notes

### 8.1 What chousa owns vs routes away

| Material | Route |
|---|---|
| METHOD rules (hierarchy, chain, verify, strategy, approval) | **chousa knowledge/** |
| Shokunin rank metaphors, jin'i-ryu coinage, kyū/dan content | **out-of-province** content residue; do not mint as chousa domain facts (`PROVINCE.md:10-11`; CraftVsContent peer) |
| Bounty programs / claim packages | **kasegi** |
| Model quality / eval | **kengaku** |
| Secret custody | **kagi** (shape-only here) |
| Fleet citation *mechanics* | cite as **precedent**, don't fork bounty-specific bases into chousa |

### 8.2 Counts (reproducible)

| Count | Command basis (run 2026-10-14 in survey) |
|---|---|
| 3 survey artifacts + 1 README | `research/deep-research-2026-09-28/*.md` (3) + `research/README.md` |
| A 109 / B 100 / C 154 / README 17 lines | `wc -l` on those paths |
| sha256 A `9033857d…0b85` B `6d8dbddd…2006` C `e48fe70f…321b` README `5199b23b…3e86` | `sha256sum` on those paths |
| 5 planned knowledge entries | this map §1 |
| 0 knowledge files present pre-map | `chousa-shokunin/corpus/knowledge/` only `.gitkeep` |

### 8.3 Admitted vs proposal tally (this map only)

| Class | Count | Notes |
|---|---|---|
| Admitted METHOD rules/rows grounded in SKILL/PROVINCE/QUALITY/CORPUS/fleet gates/export *structure* | **≥28** distinct rule rows across §§2–6 | not double-counting repeated anchors |
| Proposal (external primary, loopback, gate check not yet coded) | **≥8** | S6/S7, dictionary/paper tiers, contradicted status example, research-gate approval tooth |
| Out-of-province content (not METHOD) | rank/paper *findings* in A/B/C bodies | must not appear as admitted chousa facts |

### 8.4 Conflicts to surface for the judge (verbatim tensions)

1. **Export claims "primary-ish sources" (user prompt A `:35`) while README says not Deep Research (`README:7-8`) and hops don't resolve** — METHOD must prefer README+resolve facts over export self-description.  
2. **B distinguishes "published findings" vs "proposed engineering rules" (`B:59`) but still cites via bare arxiv.org** — good *label*, broken *chain*.  
3. **Fleet already enforces citation resolve (kagi/kasegi/kumitate) while chousa corpus is empty** — round-1 success is the map + later cutover, not claiming enforcement chousa does not yet run.  
4. **Anchorcheck: range-valid ≠ semantic-valid (`anchorcheck.py:53-55`)** — chousa verification entry must keep this split or it will rubber-stamp line hits.

---

## 9. Out of scope (this member)

- Writing the five `knowledge/*.md` files into the lane repo (parent).  
- Implementing `tools/research-gate.sh` (ResearchGateDesign).  
- Filling ApprovalTable grants (operator).  
- Running external fetches or CDP live research.  
- Judging other members or claiming a wave verdict.  
- Absorbing kasegi bounty bases or kengaku eval notes into chousa METHOD.

---

## 10. Hand-off

**Behavior delivered:** advisory coverage map for five METHOD knowledge areas + README row set + source-line inventories + admitted/proposal/out-of-province calibration.  
**Gates touched:** none executed (read-only).  
**Artifact path:** `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/CorpusMap.md`  
**Parent should:** land `corpus/README.md` rows §7 and five `knowledge/*.md` using §§2–6 inventories; stamp revisions when claim-ledger exists; keep export trust finding in round report.

— CorpusMap · end report
