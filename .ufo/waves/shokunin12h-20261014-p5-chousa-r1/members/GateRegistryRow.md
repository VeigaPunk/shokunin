# GateRegistryRow — `tools/research-gate.sh` SKILL registry row (r1 draft)

**Seat:** `GateRegistryRow` / runtime id `GateRegistryRow-2` (scribe)  
**Item:** `chousa/GateRegistryRow`  
**Wave:** `shokunin12h-20261014-p5-chousa-r1`  
**Advisory status:** Data only. Not a judge verdict, admission, SCORECARD score, or landed SKILL edit. Parent cuts the row into `chousa-shokunin/SKILL.md` §Gates when `tools/research-gate.sh` lands.  
**Lane bounds:** leaf member; no subagent dispatch; no product-code edit; no commit/push; local read-only (no external fetches).  
**Axes:** coverage · depth · calibration  
**Schema authority:** `PROTOCOL.md` §Gate standard (`PROTOCOL.md:359-402`) — registry = eight fields: name, `gate|probe`, entry command, verdict map, self-test command and spelling, pinned-value path, write scope, owner.  
**Measured-at:** `2026-10-15T00:54:17Z` (UTC)  
**Lane HEAD at draft:** `chousa-shokunin` `02a615a93a3cfa7583bc165700522709cd47089e` (seed / mint). Working-tree gate: **absent** — no `tools/` directory; parent-land candidate from `ResearchGateDesign` + fixtures/ids peers.

---

## 0. Axes (godspeed)

| Axis | What this draft optimizes |
|---|---|
| **coverage** | All eight PROTOCOL registry fields filled; live + selftest exit maps declared; method-contract check classes and FindingIds seed vocabulary named as the pin surface; peer-authority order stated (script > design seats when they diverge). |
| **depth** | Verdict map grounded in mint SKILL + wave contract + fleet gate precedent (kagi claim-ledger / mori census / PROTOCOL three-class outer interface); write scope and two-evidences obligations spelled for a *record* gate (not a host-census gate). |
| **calibration** | Classification is **`gate`** (can fail) not probe; **no fake green** — script and fixtures do not exist at measure time, so no selftest tally is claimed; pin path is a *pointer plan*, not restated expected matrices; D-137/D-139/D-101 failure modes pre-named so parent does not land a partial row. |

---

## 1. Behavior delivered

Draft of the single SKILL gate-registry row for `tools/research-gate.sh`, grounded in local authority only:

| Source | What it supplied | Class |
|---|---|---|
| `PROTOCOL.md:359-402` §Gate standard | Eight-field schema; `0=clean` / `1=failed`; other codes mapped to `clean\|failed\|could-not-evaluate`; self-test = exit **and** stable finding-id; flag spelling lane-owned; two evidences; read-only over non-owned surfaces | **observation** (protocol text) |
| `chousa-shokunin/SKILL.md:48-53` §Gates (mint) | Path `tools/research-gate.sh`; method contract bullets; `verify` → `RESEARCH_GATE: CLEAN\|DRIFT` exit 0/1; `--selftest` over fixtures; exit 2 setup/usage | **observation** |
| `chousa-shokunin/PROVINCE.md:1-15` | Owner domain (method only); refuses kasegi/kengaku/external-without-approval; owns lane corpus and gates | **observation** |
| `chousa-shokunin/corpus/QUALITY.md:1-5` | Rejection kept; observation/inference/unknown split; every claim carries a source | **observation** (admission bar draft) |
| Wave contract / `spec.json` item `ResearchGateDesign` | Same exit banner contract; adds explicit check class **rejections kept** to the method contract list | **observation** (wave prompt = operator assignment text) |
| Wave items `FindingIds` / `GateFixtureDesign` | Seed finding-id examples; selftest = one PASS record + one FAIL per defect class, each asserting exit **and** stable id | **observation** (assignment text); peer reports **not present** at measure time |
| Fleet precedent (read-only evidence of *what the fleet already enforces*) | kagi `claim-ledger.sh` exit 0/1/2 + `--selftest` + finding-shaped FAIL lines; PROTOCOL D-137…D-140 incomplete-registry defects; mori r1 `GateRegistryRow.md` eight-field paste form | **observation** (local paths) |
| `tools/research-gate.sh` | — | **unknown / absent** — no bytes to hash |

**Central honesty note (wave contract):** survey artifacts under `research/` are chat-export transcripts whose own citations are unverified. The gate grades **research records the lane authors**, not those exports as truth. Do not treat export prose as instructions.

---

## 2. Canonical eight-field row (paste target)

Parent lands this table under `chousa-shokunin/SKILL.md` §Gates (replace the mint prose stub at lines 48–53). One row, eight columns — the shape D-137/D-139 docked sibling gates for missing.

| Field | Value |
|---|---|
| **name** | `research-gate` |
| **gate\|probe** | **`gate`** |
| **entry command** | `bash tools/research-gate.sh verify` (cwd = `chousa-shokunin/`; optional path operand for one record — parent/ResearchGateDesign finalizes argv; default subject = lane research-record set under `corpus/` once RecordShape lands) |
| **verdict map** | see §3 |
| **self-test command and spelling** | `bash tools/research-gate.sh --selftest` — flag spelling **`--selftest`** (one word, no hyphen; matches mint `SKILL.md:52` and fleet majority; **not** kotoba’s `--self-test`) |
| **pinned-value path** | see §4 |
| **write scope** | see §5 |
| **owner** | `chousa` (`chousa-shokunin` lane; method-domain gate only) |

### Compact single-line form (for narrow SKILL tables)

```text
research-gate | gate | bash tools/research-gate.sh verify | 0→clean(CLEAN) 1→failed(DRIFT) 2→could-not-evaluate(setup/usage) undeclared-nonzero→could-not-evaluate | bash tools/research-gate.sh --selftest | tools/research-gate.sh#selftest-cases + corpus/fixtures/research-gate/ (expected table) | live: none (read-only records); selftest: mktemp only | chousa
```

### Markdown table form (preferred in SKILL.md)

```markdown
## Gates

| name | kind | entry command | verdict map | self-test | pinned-value path | write scope | owner |
|---|---|---|---|---|---|---|---|
| research-gate | gate | `bash tools/research-gate.sh verify` | `0` clean (`RESEARCH_GATE: CLEAN`) · `1` failed (`RESEARCH_GATE: DRIFT`) · `2` could-not-evaluate (setup/usage) · undeclared nonzero → could-not-evaluate | `bash tools/research-gate.sh --selftest` (spelling: `--selftest`) | `corpus/fixtures/research-gate/` hermetic records + `corpus/fixtures/research-gate/expected.md` (or embedded case table in `tools/research-gate.sh` until extract lands); each case pins exit **and** finding-id / CLEAN | **live: zero writes.** Read-only over research records and fixtures. **selftest only:** `mktemp -d` under `/tmp/research-gate-selftest.*` (trap rm). No network. No external fetch. Never remediates records; never acts on kasegi/kengaku/operator surfaces | chousa |
```

---

## 3. Verdict map (code → fleet class)

Fleet outer interface per PROTOCOL (`clean | failed | could-not-evaluate`). Lane vocabulary stays `CLEAN|DRIFT` on the banner line (mint `SKILL.md:52`).

### 3.1 Live / default mode (`bash tools/research-gate.sh verify`)

| Exit | Lane banner (contract) | Fleet class | When |
|---|---|---|---|
| **0** | `RESEARCH_GATE: CLEAN …` | **clean** | Subject research record(s) satisfy the method contract checks; no severity finding fired. |
| **1** | `RESEARCH_GATE: DRIFT …` | **failed** | One or more method-contract findings fired. Stable ids on `FINDING <ID> …` (or equivalent machine lines ResearchGateDesign emits). |
| **2** | usage / setup text on stderr (no CLEAN/DRIFT claim) | **could-not-evaluate** | Unknown CLI args; missing gate script deps; unreadable subject path; malformed invocation; selftest harness cannot construct temp root. A *declared* defect inside a readable record is **exit 1**, not 2. |
| other nonzero | *(undeclared)* | **could-not-evaluate** | PROTOCOL default for undeclared codes (`PROTOCOL.md:364-366`). |

**Banner contract (stable compare; parent should keep this prefix even if trailing counters grow):**

```text
RESEARCH_GATE: CLEAN|DRIFT
```

Recommended counter tail (non-normative until script lands; mirrors kagi/mori rollups):

```text
RESEARCH_GATE: CLEAN|DRIFT (findings=N drift=M records=R)
```

### 3.2 Selftest mode (`--selftest`) — separate rollup

| Exit | Banner (recommended) | Meaning |
|---|---|---|
| **0** | `RESEARCH_GATE_SELFTEST: PASS (N cases, N passed, 0 failed)` | Every hermetic case matched want-exit **and** want finding-id / CLEAN; fixtures byte-unchanged. |
| **1** | `RESEARCH_GATE_SELFTEST: FAIL (…)` | Capability red — **not** a live fleet DRIFT measurement over production records. |
| **2** | usage | Bad invocation outside the selftest path. |

Selftest is **capability evidence** (PROTOCOL “Two evidences”, `PROTOCOL.md:374-377`), not the live grade. A green selftest does not imply live CLEAN on authored corpus records; a red selftest does not by itself mean a research claim is false.

### 3.3 Method-contract check classes (what exit 1 may name)

From mint SKILL + wave `ResearchGateDesign` prompt (union; **script wins** if a landed implementation narrows/expands):

| Check class | Seed finding-id (FindingIds prompt examples) | Contract source |
|---|---|---|
| Question declared | `NO_QUESTION` | `SKILL.md:50-51`; decision table row “Research a question” |
| Sources ranked | `UNRANKED_SOURCE` | `SKILL.md:51`; hierarchy row |
| Chain hops resolved-or-marked | `CHAIN_HOP_UNRESOLVED` | `SKILL.md:51`; chaining row |
| Claims pointed | `CLAIM_UNPOINTED` | `SKILL.md:51-52`; checklist “resolvable pointer” |
| Rejections kept | `REJECTION_DROPPED` | wave ResearchGateDesign prompt; `QUALITY.md:5`; checklist “rejected source kept” |

**Additional ids** (proposal until FindingIds / script emit them): negatives without sweep, observation/inference collapse, secret-shaped values in a record, external-live fetch without approval-table row. Mark any such id `proposal` in SCORECARD until a local fixture asserts it.

### 3.4 Why `gate` not `probe`

PROTOCOL (`PROTOCOL.md:361-363`): a tool that cannot fail is a **probe**.

| Test | Result |
|---|---|
| Can the tool return a non-clean verdict on purpose? | **Yes** — exit 1 `DRIFT` (mint contract) |
| Selftest asserts exit **and** finding-id? | **Required** by wave GateFixtureDesign + PROTOCOL self-test clause |
| Expected values intended in-repo? | **Yes** — fixtures + expected table (see §4) |
| Read-only over non-owned surfaces? | **Yes** — live zero-write; no network; no sibling-lane mutation |
| Would “probe” fit? | **No** — a pure probe cannot fail closed on method drift |

→ register as **`gate`**.

Until the script + selftest + pin path exist in-repo, closure must **not** grade the gate conformant (`PROTOCOL.md:401-402`). Classification of the *intended* instrument is still `gate`; classification of the *present tree* is **gate-shaped mint stub / unlanded**.

---

## 4. Pinned-value path

PROTOCOL: expected values are **persisted inside the owning repo**, independent of recomputation; the registry **points**, it does not restate the matrix (`PROTOCOL.md:354-356`, `369-373`, `382-384`).

### 4.1 What exists now (measured)

| Pin surface | Path / locus | Status at `2026-10-15T00:54:17Z` |
|---|---|---|
| Gate script | `chousa-shokunin/tools/research-gate.sh` | **Absent** (`tools/` directory does not exist) |
| Fixture tree | `corpus/fixtures/research-gate/` | **Absent** |
| Expected table | `corpus/fixtures/research-gate/expected.md` (or `.tsv`) | **Absent** |
| SKILL registry row (8 fields) | `SKILL.md` §Gates | **Prose stub only** (`SKILL.md:48-53`) — D-137-class if left as-is after land |
| Frozen live snapshot run | under `corpus/` or `.ufo/waves/*/frozen` | **Absent** — second PROTOCOL evidence still owed after land if live subjects are mutable authored records |
| Peer design reports | `members/ResearchGateDesign.md`, `GateFixtureDesign.md`, `FindingIds.md` | **Absent** at this seat’s measure time (members dir empty except this file when written) |

### 4.2 Registry pin pointer (what the row should name)

**Primary (honest for r1 land — land in the same commit as the gate):**

1. `tools/research-gate.sh` — if cases are embedded, the embedded hermetic table **is** the committed expected values (mori pattern).
2. **Preferred durable extract:** `corpus/fixtures/research-gate/expected.md` (or `.tsv`) — rows `case_id → exit → CLEAN|DRIFT → finding_id_or_CLEAN`, so SCORECARD/LOG can cite a path that is not “the whole script”.
3. Fixture records themselves: `corpus/fixtures/research-gate/pass-minimal.md` plus one fail fixture per defect class (GateFixtureDesign contract).

**Do not** pin expected values only inside wave member markdown under `.ufo/waves/…` — those are advisory and outside the lane repo; PROTOCOL requires pins **in the owning repo**.

### 4.3 Minimum selftest matrix the pin must keep stable

Authority: wave `GateFixtureDesign` + `FindingIds` seed list + method contract. Exact case labels are parent/ResearchGateDesign’s once the script exists; registry requires **at least**:

| # | case intent | want exit | want id / verdict |
|---:|---|---:|---|
| 1 | minimal complete research record | 0 | `CLEAN` (no FINDING lines) |
| 2 | missing question | 1 | `NO_QUESTION` + `DRIFT` |
| 3 | source present but unranked | 1 | `UNRANKED_SOURCE` + `DRIFT` |
| 4 | chain hop neither resolved nor marked | 1 | `CHAIN_HOP_UNRESOLVED` + `DRIFT` |
| 5 | claim without resolvable pointer | 1 | `CLAIM_UNPOINTED` + `DRIFT` |
| 6 | rejection omitted / dropped | 1 | `REJECTION_DROPPED` + `DRIFT` |
| 7 | CLI unknown arg | 2 | usage (no CLEAN/DRIFT claim) |

Each case must assert **exit code and** stable finding-id (or CLEAN), per `PROTOCOL.md:369-373`. A helper-only or model-only self-check does **not** satisfy the clause.

### 4.4 Two evidences (post-land debt — state, do not fake)

| Evidence | Role | r1 status |
|---|---|---|
| Hermetic `--selftest` | **Capability** | Owed at land; this seat does not claim a tally |
| Frozen run over committed input snapshot + expected verdict | **Measurement** when subjects are mutable authored records | Owed if live `verify` grades non-fixture corpus records; snapshot inputs need digests (`PROTOCOL.md:378-381`) |

Selftest green alone must not be written into SCORECARD as proof that production research records are clean.

---

## 5. Write scope

| Mode | Allowed writes | Forbidden |
|---|---|---|
| **live** (`verify`) | **None.** Creates zero files. Reads research records + in-repo fixtures only. | Any write under fleet root, lane repos, host state; network; external URL fetch; subprocesses that mutate |
| **`--selftest`** | Only `$work` from `mktemp -d /tmp/research-gate-selftest.XXXXXX` (or equivalent); removed on exit (trap). Copy fixtures into `$work` for isolation. | Mutation of tracked fixture bytes; any path outside `$work`; network |
| **remediation** | **None always.** Gate reports DRIFT; it does not “fix” a research record in place | Silent rewrite of claims, auto-rank sources, drop rejections |
| **secrets** | Shape-only detection if implemented; never print secret values (`PROVINCE.md` / SKILL boundaries) | Credential/session content capture |
| **cross-domain** | Report-only if a record wanders into bounty or model-eval claims | Absorbing kasegi/kengaku work; acting on operator approval surfaces |

Registry sentence (SKILL cell):

> **live: zero files (read-only records). selftest: `/tmp/research-gate-selftest.*` only (trap-cleaned). No network / no external fetch. Never remediates; never writes sibling lanes or main-repo protocol surfaces.**

Aligns with PROTOCOL scope (`PROTOCOL.md:388-392`): read-only over surfaces it does not own; never acts on an external surface.

---

## 6. Owner

| Field | Value |
|---|---|
| **owner** | `chousa` |
| **repo** | `chousa-shokunin` |
| **domain** | deep-research **method** (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification, approval-table craft (`PROVINCE.md:3-8`) |
| **not owner of** | bounty programs / claim packages → **kasegi**; model-quality / eval claims → **kengaku**; orchestration / driver completion → **kumitate** / operator; secret **content** custody → **kagi** (chousa may enforce shape-only refusal in records) |
| **gate ownership clause** | A red `research-gate` is a **conformance defect on chousa research records**, routed to chousa — status-neutral for fleet markers unless round rules say otherwise (`PROTOCOL.md:393-398`). Integrator verifies *committed evidence* (selftest tally, frozen-run, revision); it does not have to execute the sibling gate blind. |

---

## 7. Operability evidence (this seat)

Commands / facts at `2026-10-15T00:54:17Z` (read-only):

```text
$ git -C chousa-shokunin rev-parse HEAD
02a615a93a3cfa7583bc165700522709cd47089e

$ git -C chousa-shokunin ls-files
AGENTS.md
LOG.md
MINT.md
PROVINCE.md
SHONEN.md
SKILL.md
corpus/QUALITY.md
corpus/README.md
corpus/knowledge/.gitkeep
corpus/lessons/.gitkeep

$ test -e chousa-shokunin/tools; echo $?
1   # tools/ absent

$ sed -n '48,53p' chousa-shokunin/SKILL.md
## Gates
`tools/research-gate.sh` — validates a research record against the method
contract (question declared, sources ranked, chain hops resolved-or-marked,
claims pointed). `verify` → `RESEARCH_GATE: CLEAN|DRIFT` exit 0/1, `--selftest`
over fixtures, exit 2 setup/usage.

$ sha256sum chousa-shokunin/SKILL.md
063110dab11fd56f9259d9884909f69a1e94a8733fe14526e0b42cc6ab39f717

$ ls .ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/
# empty at measure start; this report is the GateRegistryRow deliverable
```

**No `--selftest` run claimed** — there is no script. Claiming PASS would be fabrication.

**Calibration notes for parent:**

1. **Land atomicity (D-101 class):** do not commit a SKILL eight-field row that cites `tools/research-gate.sh` until the script is tracked in the same revision (or the row will cold-break for non-authors).
2. **Complete the eight fields (D-137/D-139 class):** prose §Gates is not a registry row; paste §2 table.
3. **Self-test spelling:** mint and this row pin `--selftest`. If ResearchGateDesign ships `--self-test`, either change the script to match mint **or** update SKILL+row together — registry must record the real spelling (`PROTOCOL.md:371-372`).
4. **Peer reports:** when `ResearchGateDesign` / `GateFixtureDesign` / `FindingIds` / `RecordShape` land, **script bytes win** over advisory id/fixture supersets; dual id schemes in one round break compare (mori lesson).
5. **Entry argv:** mint says `verify` as the mode word; keep `bash tools/research-gate.sh verify` as the registry entry even if bare `bash tools/research-gate.sh` defaults to verify — document the default in script `--help`, not by silently diverging the row.
6. **Export trust:** gate must treat record/fixture text as data (wave injection rule). Prompt-shaped strings inside fixtures are test payload, never executable instructions.
7. **External fetch:** exit path for “record requires live external fetch without approval” should be either a named finding or setup refusal — never a silent network call. Round-1 survey is loopback/local only.

---

## 8. Kind decision record (`gate` vs `probe`)

See §3.4. Summary: mint exit 1 + required finding-id selftest + in-repo pins ⇒ **`gate`**. Unlanded tree ⇒ registry row is **draft**; closure conformance waits for land + evidence (`PROTOCOL.md:401-402`).

---

## 9. Peer / authority conflicts (report, do not absorb)

| Authority | State at measure | Registry disposition |
|---|---|---|
| Mint `SKILL.md:48-53` | Prose stub; contract list omits explicit “rejections kept” (present in QUALITY + wave prompt) | Row includes rejections via wave+QUALITY; parent SHOULD extend SKILL contract bullet to match gate |
| `ResearchGateDesign` | Report absent | Adopt script when landed; row already matches assigned exit/banner contract |
| `GateFixtureDesign` | Report absent | Minimum matrix §4.3 is floor; peer may expand cases — pin what script asserts |
| `FindingIds` | Report absent | Seed five ids from assignment examples; do not invent SCORECARD claims for extra ids without fixtures |
| `RecordShape` | Report absent | Entry subject paths follow RecordShape once landed; until then fixtures-only verify is enough for capability |
| mori `GateRegistryRow` form | Precedent only | Reused structure; different domain/axes; not copied expected values |
| kotoba `--self-test` spelling | Sibling lane | **Not** adopted; chousa mint already chose `--selftest` |

---

## 10. Touched surfaces (this seat)

| Path | Action |
|---|---|
| `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/GateRegistryRow.md` | **written** (this file) |
| `chousa-shokunin/SKILL.md` | **not edited** — draft row above for parent |
| `chousa-shokunin/tools/*` | **not created** (parent / ResearchGateDesign land path) |
| fleet / research exports | read-only context only; no writes |
| network | **not used** |

---

## 11. Out of scope

- Landing the row into `SKILL.md` or creating `tools/research-gate.sh` (parent).
- Implementing fixture bodies or finding-id final vocabulary (GateFixtureDesign / FindingIds / ResearchGateDesign).
- Running a fabricated selftest or claiming CLEAN/DRIFT on corpus records.
- Judging survey export truthfulness (central finding is their **unverified** citations — state it; gate does not launder them into primaries).
- Bounty scope, model eval, external live-target research, secret values.
- Subagent dispatch (leaf).
- SCORECARD/LOG edits, commits, pushes, judge verdicts.

---

## 12. Findings (for parent / integrator)

| ID | Severity | Finding |
|---|---|---|
| GRR-1 | blocker for land | `tools/research-gate.sh` **absent** at lane HEAD `02a615a` — registry row must not outrun the binary |
| GRR-2 | blocker for closure conformance | SKILL §Gates is **prose**, not an eight-field row — fails PROTOCOL registry clause until replaced |
| GRR-3 | process | Peer design members unset at measure time — parent reconciles script vs FindingIds/FixtureDesign; this row pins contract floor only |
| GRR-4 | calibration | No selftest tally is available; any SCORECARD cell claiming `RESEARCH_GATE_SELFTEST: PASS` before land is unearned |
| GRR-5 | design debt | Second evidence (frozen snapshot) still open after capability land if live verify grades mutable authored records |
| GRR-6 | contract hygiene | Mint SKILL method-contract list should gain explicit **rejections kept** to match QUALITY + wave ResearchGateDesign (else gate checks a rule SKILL forgets to name) |

---

## 13. Artifact paths

| Artifact | Path |
|---|---|
| This advisory report | `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/GateRegistryRow.md` |
| Paste target | `chousa-shokunin/SKILL.md` §Gates (parent) |
| Gate binary (owed) | `chousa-shokunin/tools/research-gate.sh` |
| Pin pointer (owed) | `chousa-shokunin/corpus/fixtures/research-gate/expected.md` (+ fixture records) |
| Schema | `PROTOCOL.md:359-402` |
| Lane HEAD measured | `02a615a93a3cfa7583bc165700522709cd47089e` |

---

**End of advisory report.** No judge verdict claimed. No remediation performed. No network used.
