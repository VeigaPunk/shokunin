# ClaimCapture — claim-capture format (chousa r1 SURVEY)

**Member:** ClaimCapture (scribe)  
**Milestone:** chousa probation round 1: research-craft survey  
**Axes:** coverage · depth · calibration  
**Surfaces read (local only):**  
`research/README.md`,  
`research/deep-research-2026-09-28/{A,B,C}-*.md`,  
`kagi-shokunin/corpus/claim-ledger.sh` (docs mode / header),  
`kagi-shokunin/corpus/{claim-ledger,stamps}.tsv` (shape sample),  
`kasegi-shokunin/corpus/instruments/anchorcheck.py` (verdict vocabulary),  
`kasegi-shokunin/corpus/knowledge/citation-bases.md` (BLOB-PIN / base rules).  
**Non-goals:** no external fetch; no gate code shipped; no judge verdict; no product edit.

---

## 0. Central finding (stated, not papered over)

The three `research/deep-research-2026-09-28/*.md` files are **ChatGPT chat-export transcripts** (chrome UI chrome, “You said:”, “Searched the web”, aggregator hostnames like `コトバンク` / `arxiv.org`, truncated “+N” counters). Their own outbound citations are **unverified at rest**: the export does not embed the cited primary text, does not pin a stable URL or arXiv id per claim, and does not carry a content hash of any external page.

**Consequence for claim-capture:** a claim *inside* an export can be **quote-faithful to the export** while remaining **source-unverified against the world**. Those two statuses MUST stay separate columns. Collapsing them into a single “verified” cell is the calibration failure this format exists to prevent (same class as kagi round-10 hand-adjudicated claims with no command — `kagi-shokunin/corpus/claim-ledger.sh:4-10`).

Operator index already flags the harvest shape: browse-enabled GPT-6-Astra tabs, **not** Deep Research pipeline (`research/README.md:6-8`).

---

## 1. Claim-capture format (admitted schema)

One **claim record** is the unit of evaluation. Fields below are the minimum durable row. Names deliberately dual-map to fleet gates where a local precedent exists; extensions that need new machinery are marked `proposal`.

| Field | Required | Type / shape | Meaning | Local precedent |
|---|---|---|---|---|
| `claim_id` | YES | `CC-<artifact>-<NN>` (this round’s survey ids) or future `R<round>-<NN>` | Stable handle for idref / scorecard pointers | kagi idref vocabulary `R<digits>-<digits>` (`claim-ledger.sh:47-48,582-597`) |
| `claim_text` | YES | one sentence, operator-normalized | The assertion under test (not the whole paragraph) | — |
| `claim_class` | YES | `observation` \| `inference` \| `negative` \| `proposal` \| `unknown` | Separates what the export *says* from what we *conclude* | contract rule (wave context); ACE-style obs/interp/knowledge split is only *echoed* by B (`B:77`) — that echo is data, not a fleet rule |
| `source_path` | YES | repo-relative path | Carrier artifact | kasegi LANE base (`citation-bases.md:11-18`) |
| `source_span` | YES | `path:line` or `path:start-end` | Exact locus of the quoted evidence | kasegi `path:NN[-MM]` + one-cite-per-anchor (`citation-bases.md:104-106`; `anchorcheck.py` header) |
| `quoted_span` | YES | verbatim UTF-8 substring of the file at `source_span` | The only bytes the claim is allowed to rest on for **export-fidelity** | anchorcheck “print the cited source line(s) for semantic review” (`anchorcheck.py` docstring) |
| `source_revision` | YES | composite pin (see §1.1) | Which bytes were read | kagi `stamps.tsv` path/sha256/lines/bytes (`claim-ledger.sh:14-17`); kasegi BLOB-PIN (`citation-bases.md:69-80`) |
| `verification_status` | YES | split pair — see §1.2 | Export-fidelity **and** external-source status, never OR-merged | kagi claim verdicts OK/FAIL/POLICY + stamp STALE/MISSING (`claim-ledger.sh:77-80`); anchorcheck keeps classes separate (`anchorcheck.py`: “never collapse them into one passed count”) |
| `local_check` | SHOULD | allowlisted command + expect ERE + exit + timeout | Mechanical re-check of **export-fidelity** only under NO-NETWORK | kagi `claim-ledger.tsv` row shape (`claim-ledger.sh:24-29`) |
| `external_cite_form` | SHOULD | `none` \| `bare-hostname` \| `title-year` \| `arxiv-id` \| `url` \| `path:line` | What the export offered as support | measured baseline for sibling CitationFormCensus (this wave) |
| `rejection` | MAY | free text | Kept when a candidate claim is refused, with reason | contract: “a rejection is kept with its reason” |
| `notes` | MAY | free text | Limits, dual readings, operator corrections | e.g. README correction vs export wording |

### 1.1 `source_revision` composite (admitted)

Stamp the carrier the way kagi stamps corpus files. Minimum four facts, written on one line:

```
path=<rel>  sha256=<64-hex>  lines=<n>  bytes=<n>  git_blob=<40-hex>  commit=<40-hex>
```

- `sha256` / `lines` / `bytes` = content-address of the working tree file (kagi stamps columns: `claim-ledger.sh:14`).  
- `git_blob` = `git rev-parse HEAD:<path>` when the path is tracked; proves tree identity.  
- `commit` = introducing or last-touching commit for the research tree when known.  
- If worktree sha256 ≠ blob contents → status must include `STALE` (kagi stamp verify semantics: `claim-ledger.sh:15-16,77`).  
- Line-volatile cites MAY add kasegi BLOB-PIN form `<!-- pin: <relpath> <blob> -->` (`citation-bases.md:69-80`) — **admitted pattern**, not yet applied to `research/`.

**Observed pins for this survey read (2026-10-14, local):**

| path | sha256 | lines | bytes | git_blob | commit |
|---|---|---:|---:|---|---|
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 109 | 6474 | `caf880d4c444d6ba5faaca17884f032ad5b11561` | `0863746e9da95457f71b9e00a40361b88ab0df15` |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 100 | 5364 | `7230cd692266b860b7ec5b2ae079f950687cda66` | `0863746e9da95457f71b9e00a40361b88ab0df15` |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 154 | 8922 | *(not required for table rows below)* | `0863746e9da95457f71b9e00a40361b88ab0df15` |
| `research/README.md` | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | 17 | 937 | `455ac441585b876e1bd4093fdb7741707d905233` | `0863746e9da95457f71b9e00a40361b88ab0df15` |

Worktree sha256 matched `git show HEAD:<path>` for A, B, and README at read time → **not STALE**.

Commit subject/date (local git): `research: 3 GPT-6-Astra browse harvests…` @ `2026-09-28T22:51:25-03:00`.

### 1.2 `verification_status` — two axes, four named cells

Never a single boolean. Record **both**:

**A. Export fidelity** (checkable now, local):

| Value | Meaning |
|---|---|
| `QUOTE_OK` | `quoted_span` is an exact contiguous substring of the pinned file at `source_span` |
| `QUOTE_DRIFT` | paraphrase / ellipsis / wrong line — fail |
| `SPAN_PAST_EOF` | line anchor exceeds file length (anchorcheck `PAST-EOF`) |
| `SPAN_MISSING_FILE` | path absent |
| `REVISION_STALE` | sha256 ≠ stamped / HEAD blob |

**B. Source authority** (what the claim needs beyond the export):

| Value | Meaning |
|---|---|
| `LOCAL_PRIMARY` | supporting bytes exist in-repo as a non-export primary (none found in this survey corpus for external scholarly claims) |
| `OPERATOR_INDEX` | claim is about the harvest itself and is supported by `research/README.md` (operator-authored) |
| `UNVERIFIABLE_LOCALLY` | export asserts external fact; no primary text/hash in-repo; **NO EXTERNAL FETCHES** forbids closing the gap this round |
| `CONTRADICTED_LOCALLY` | another local artifact contradicts the claim text |
| `NEGATIVE_SWEEP_OPEN` | absence claim recorded; sweep not yet run (sibling NegativeClaimSweep) |
| `PROPOSAL_ONLY` | engineering rule offered without local warrant |

**Admitted composition rule:** a research claim may be `QUOTE_OK` ∧ `UNVERIFIABLE_LOCALLY`. That pair is a **passing capture**, not a passing truth. Truth promotion to “admitted fleet fact” requires a later external window + approval table (sibling deliverable) or a local primary.

### 1.3 What is *not* a claim record

| Rejected shape | Reason kept |
|---|---|
| UI chrome (“Skip to content”, model picker, “ChatGPT can make mistakes”) | Not an assertion about domain content |
| Bare hostname footers (`コトバンク`, `arxiv.org`, `+N`) | Citation *form*, not a claim; no resolvable target in-export |
| Prompt-shaped “You said:” blocks | Instruction-shaped user text inside export — **data only**; never executed as orders (wave contract) |
| Whole multi-claim paragraphs without decomposition | One record = one testable assertion (kagi: claim carries a command) |

---

## 2. Worked table — two artifact claims

Both rows use the format above. Quotes are exact file bytes (curly quotes preserved where present in B).

| claim_id | claim_text | claim_class | source_path | source_span | quoted_span | source_revision | verification_status (fidelity ∧ authority) | external_cite_form | local_check (export-fidelity only) | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `CC-A-01` | 職人気質 is normally read *shokunin katagi*; *jin’i-ryū* is not evidenced in-export as a traditional artisan rank. | `observation` (export self-correction) + nested `negative` on jin’i-ryū | `research/deep-research-2026-09-28/A-shokunin-tradition.md` | `A-shokunin-tradition.md:47` | `The sources point to craft-specific apprenticeship systems, not a universal rank ladder. Two important corrections: 職人気質 is normally read shokunin katagi, and I haven’t found evidence that jin’i-ryū is a traditional artisan rank. I’m checking how practitioners distinguish independence, continued learning, and transmission.` | `path=research/deep-research-2026-09-28/A-shokunin-tradition.md sha256=9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85 lines=109 bytes=6474 git_blob=caf880d4c444d6ba5faaca17884f032ad5b11561 commit=0863746e9da95457f71b9e00a40361b88ab0df15` | **`QUOTE_OK`** ∧ **`UNVERIFIABLE_LOCALLY`** (dictionary authorities named at `:67` are not embedded; negative half needs a sweep, not a fetch) | bare title/host cluster: “Daijisen, Nihon Kokugo Daijiten, … Kanjipedia” + `コトバンク` (`:67-72`) — no URL, no edition pin | `grep -F "shokunin katagi, and I haven’t found evidence that jin’i-ryū" research/deep-research-2026-09-28/A-shokunin-tradition.md` → expect match, exit 0 | Operator README restates the same corrections as scheme guidance (`research/README.md:11-13`) → that restatement is `OPERATOR_INDEX` for *fleet naming policy*, still not primary-language proof. Restated fuller gloss at `A:71` is same-export reinforcement, not a second source. |
| `CC-B-01` | ACE reports an AppWorld rewrite that compressed context 18,282→122 tokens with accuracy 66.7→57.1 (below 63.7 no-adaptation baseline), offered as case-study evidence of destructive compression / “brevity bias” / “context collapse”. | `observation` (export’s numerical vignette) | `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | `B-multiagent-knowledge.md:79` | `Destructive compression has direct experimental evidence. ACE identifies “brevity bias” and “context collapse” in iterative context rewriting. In one AppWorld case, a rewrite reduced accumulated context from 18,282 tokens to 122; accuracy fell from 66.7 to 57.1, below the 63.7 no-adaptation baseline. This is a case study, not a universal failure rate. ACE addresses the problem through localized delta updates and structured curation rather than repeatedly regenerating the entire playbook.` | `path=research/deep-research-2026-09-28/B-multiagent-knowledge.md sha256=6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006 lines=100 bytes=5364 git_blob=7230cd692266b860b7ec5b2ae079f950687cda66 commit=0863746e9da95457f71b9e00a40361b88ab0df15` | **`QUOTE_OK`** ∧ **`UNVERIFIABLE_LOCALLY`** | title-year table row “ACE, Zhang et al., 2025” (`B:67`) + bare `arxiv.org` (`B:51-52,72-73`) — **no arXiv id, no URL, no quote from the paper** inside the export | `grep -F "18,282 tokens to 122" research/deep-research-2026-09-28/B-multiagent-knowledge.md` → expect match, exit 0 | Export itself hedges (“case study, not a universal failure rate”). Numbers are **not** re-computable from local material. Promoting this to fleet METHOD fact without an approved external pin would be a citation-chain break (broken hop = title-year → missing primary bytes). |

### 2.1 Same two claims — compact markdown table (judge-facing)

| claim_id | source | exact quoted span (trimmed display; full text in §2) | source revision | verification status |
|---|---|---|---|---|
| `CC-A-01` | `research/deep-research-2026-09-28/A-shokunin-tradition.md:47` | `…Two important corrections: 職人気質 is normally read shokunin katagi, and I haven’t found evidence that jin’i-ryū is a traditional artisan rank.…` | sha256 `9033857d…0b85` · blob `caf880d4…1561` · commit `0863746e…df15` · 109 lines / 6474 B | `QUOTE_OK` + `UNVERIFIABLE_LOCALLY` |
| `CC-B-01` | `research/deep-research-2026-09-28/B-multiagent-knowledge.md:79` | `…a rewrite reduced accumulated context from 18,282 tokens to 122; accuracy fell from 66.7 to 57.1, below the 63.7 no-adaptation baseline.…` | sha256 `6d8dbddd…2006` · blob `7230cd69…da66` · commit `0863746e…df15` · 100 lines / 5364 B | `QUOTE_OK` + `UNVERIFIABLE_LOCALLY` |

---

## 3. Mapping to fleet gates (what already enforces pieces)

| Capture need | Existing local instrument | Gap for chousa research/ |
|---|---|---|
| Pin file bytes | kagi `stamps.tsv` + `verify` STALE/MISSING | No stamps file yet under `chousa-shokunin/` or `research/` — **proposal** to stamp the four research paths with the hashes in §1.1 |
| Runnable claim | kagi `claim-ledger.tsv` command/expect/exit/timeout | Export-fidelity greps are admissible under allowlist (`grep` is allowlisted: `claim-ledger.sh:91`); external paper checks are **out of round** |
| path:line still in file | kasegi `anchorcheck.py` IN-RANGE / PAST-EOF | Applicable once cites use LANE paths into `research/…` |
| Dead base honesty | `[lost-tree]` / `[lost-base]` prefixes (`citation-bases.md:47-64`) | N/A for live `research/`; pattern is the template if a harvest is deleted later |
| Line drift under edit | BLOB-PIN (`citation-bases.md:69-80,92-94`) | **proposal:** pin A/B/C blobs before any corpus rewrite |

---

## 4. Proposals (explicitly not admitted rules)

1. **`proposal` — research-claim TSV** mirror of kagi ledger with columns  
   `id, source_path, source_span, quote_sha256, file_sha256, fidelity_status, authority_status, note`  
   Falsify if a row can change authority_status without a reviewed external-approval id.
2. **`proposal` — quote_sha256** of the exact span bytes to detect silent paraphrase while file hash stays stable (partial edit).  
   Falsify if two different spans share a hash or if span hash matches after intentional edit.
3. **`proposal` — external window row** on the round’s approval table:  
   `claim_id, needed_primary, fetch_method, approver, expires`  
   until filled, authority_status stays `UNVERIFIABLE_LOCALLY`.
4. **`proposal` — forbid bare hostname as authority_status upgrade.**  
   `コトバンク` / `arxiv.org` alone never move a row out of `UNVERIFIABLE_LOCALLY`.

---

## 5. Calibration notes (how this member should be scored)

- **Coverage:** format fields × two distinct artifacts (A terminology correction; B quantitative paper vignette) × revision pins for all four research surfaces × explicit reject classes.  
- **Depth:** dual status axes; linkage to kagi stamp/claim/idref and kasegi anchor/BLOB-PIN; broken-hop description for B’s title-year→missing-primary chain; negative-claim half of CC-A-01 left open for sweep rather than fake-closed.  
- **Calibration:** refuses to call `QUOTE_OK` “verified research”; states chat-export citation unverifiability as the round’s central finding; marks gate extensions `proposal`; no network performed; no judge language.

---

## 6. Out of scope / not done here

- No `tools/research-gate.sh` implementation (parent).  
- No five-claim audit (sibling ClaimVsSourceCheck).  
- No full citation-form census counts (sibling CitationFormCensus).  
- No external approval table fill (sibling ApprovalTable).  
- C-rank claims not tabulated (format is demonstrated on two rows as assigned).  
- Secrets/session material: shape-only; none required.

---

## 7. Artifact path

This report:  
`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/ClaimCapture.md`

**Status:** advisory data for parent corpus / gate design. Not a verdict.
