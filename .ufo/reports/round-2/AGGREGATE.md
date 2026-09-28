# AGGREGATE — fleet quality review + mint/no-mint assessment

**Author:** aggregator L1 (`m_qwen`), main-repo lane.
**Refreshed:** 2026-09-28 at driver round 3 (`.ufo/state/aggregator.round` = 3;
`watchdog.log` v2/v3 steers each lane every 450 s, cap 1024).
**Evidence window:** every artifact on disk at refresh time — rounds 0–4:
`.ufo/reports/round-1/{kasegi,kengaku-shokunin,kotoba,kumitate,protocol,web-properties-publishing}.md`,
`round-2/kagi.md`, `round-3/{kake,kasegi,kengaku,kotoba,kumitate,protocol}.md`,
`round-4/protocol.md`; all six child repos' `corpus/`, `LOG.md`, `SKILL.md`,
`PROVINCE.md`, `SHONEN.md`; `MANIFEST.json`, `PROTOCOL.md` (post-`68294b4`),
`CORPUS.md`, `.ufo/waves/round-1.json`.
**Method:** independent re-execution. Aggregator ran the cited commands itself
(`find`, `wc`, `grep`, JSON parses, `git cat-file`) and dispatched five
read-only L2 `reviewer` lanes (one per child corpus; `reviewer` → `m_composer`
per the fleet map in `.ufo/prompts/aggregator-L1.md`) whose payloads are
mirrored into each repo's `corpus/lessons/round-1-aggregator-audit.md`.
No claim below rests on a lane's self-report alone.

---

## 1. Per-lane quality review

| Lane | Reports | Child commits | SKILL lines | Corpus files | LOG entries | Verdict |
|---|---|---|---|---|---|---|
| protocol | r1, r3, r4 | main `eac90ae`, `68294b4`, +r4 | — | — | — | **strong** — every gap it names is evidenced by a live artifact |
| kasegi | r1, r3 | `5a0188f`,`49f5945`,`e73b2b5`,`d6b71c0`,`0bde2e0` | 240 | 14 | rounds 0–4 | **strong, 3 citation defects** |
| kengaku | r1 (`kengaku-shokunin.md`), r3 | `90a5ce8`,`24ff62e`,`a4c056e` | 239 | 14 | rounds 0–3 | **strong content, non-conforming surfaces** |
| kake | r1 (`web-properties-publishing.md`), r3 | `cd5b381`,`ddf40e2` | 163 | 8 | rounds 0–3 | **strong, numeric drift + report-before-commit** |
| kumitate | r1, r3 | `45b4ed3`,`0ac95e1`,`efe19da` | 283 | 10 | rounds 0–3 | **strong technical core, 1 false pointer** |
| kotoba | r1, r3 | `1d93182`,`229b687` | 229 | 8 | rounds 0–3 | **good, 2 citation defects; self-attested promotion** |
| kagi | r2 | `9b3e49f`, + aggregator `9987054` | 105 | 9 | rounds 0–2 | **strong; cleanest citation record on the roster** |
| aggregator | this file + `round-3/aggregator.md` | child corpus lessons ×6, `CORPUS.md` | — | — | — | see §6 for its own defect |

### What is genuinely strong (verified, not reported)

- **kasegi** re-verified: 1088 program records; 486-row verdict ledger with
  430/50/6 leave/continue/drop; partition 438+19+26+3 = 486; wrap-report
  0 GO / 5 GO-WITH-FIX / 2 NO-GO; 12-row operator queue; `ev-report.mjs` exit 2
  on a missing program; schema `additionalProperties:false` + `p_in_scope`
  [0,1]; `evidence-manifest/v1`; four `claim_review.hard_gates`; Pendle pin
  `f24265966bb53f75d834ad705decde8e479d3a33`. Round 3 read all three `ops/`
  scripts and produced gate semantics nobody had written down (global
  duplicate-submission scan across `claims/*/*/status.json`; reviewer role must
  be literally `kx-reviewer`; three-way `head_sha256` binding) — that is
  domain knowledge with teeth.
- **kasegi refuted its own hypothesis**: round-1 report predicted the Cantina
  $100 fee gate "likely generalizes"; round 3 sampled five sibling ingestions
  and recorded that only `cantina-dydx` repeats the pattern, so the fee gate is
  Pendle-specific so far. Hypothesis → test → refutation → corpus entry is
  exactly the loop `PROTOCOL.md` asks for.
- **kengaku** re-verified: `~/wikillm/llm-wiki` genuinely absent; all five wiki
  pages exist; 125 agents / 21 experiments; RMSE 135,367 → 117,791 (~13%);
  K2 0/3 vs 3/3; T2 gradient 7→9→13→17→19; MCP-Atlas 36/220/1,000;
  SWE-Bench Verified retirement 2026-02-23; 180 families / 413 models /
  2026-09-11; 402 files / 342 markdown. Round 3 then found two real telemetry
  corpora the round-1 search had surfaced and discarded — `~/bench-arena/`
  (33-task two-model battery, PASS 21/33 vs 19/33, near-disjoint win sets,
  FAIL median latency 60.9 ms < PASS 79.5 ms) and
  `~/Projects/bounties/ledger/telemetry.jsonl` (7,218 lines; `dispatcher_tick`
  3,680; `attempt_reset` 68 vs `mission_done` 26) — and wrote the root cause of
  its own miss ("pattern-matched filenames to 'irrelevant harness' without
  reading them"). Self-diagnosed search failure is the highest-value lesson
  landed anywhere this round.
- **kake** re-verified: `webzites-fleet-v1` @ 2026-09-26; `probe.mjs:55`
  `html.includes(expect.marker)`; `CNAME` = ds4cc.com; `render.yaml`
  `ds4cc-marketplace-app` + `APP_ORIGIN=https://app.ds4cc.com`; plazir
  `rel=canonical` → `https://ds4cc.com/speedrun/`; `ufofsdbeta` has no
  `.github/` but has `dist/`; `ufofsdbeta-kimi-review` is not a git repo;
  `kimi-surface.mjs` header bans automated publish; 14 rows with
  `updatePath: kimi-websites-surface`. Round 3 then ran the playbook's own
  probes and **corrected the registry from live state**: 12 OK / 6 failing, and
  the `lucario` row is wrong (`fleet.config.json` says live/maintained;
  `lucario.kimi.page` is a never-published 404, canonical is the GHP site).
  Live probe beating a stale config is the domain's core move, demonstrated.
- **kumitate** re-verified: `ENTRY_FAILURE_CLASSES` = 7 (L37–40);
  `CAPACITY_FAILURES` = 3 (L109); swarm knobs 100/64/16/100;
  `globalRunnerCeiling` 1056, `maxConcurrentL1` 32, `windowPaneCeiling` 16;
  `PROPOSAL_WAVE_CEILING` 16, `CONCURRENCY_CEILING` 32; `acquireSingletonLock`
  L1716; `classifyFailure` L734; `MIN_HOIST_SAVINGS` 512; `stale_dispatch_pair`
  documented L50 / thrown L451,L459; `fleet-dispatcher.mjs` 14,769 lines.
  Round 3 mapped `maybeEnqueueIterationSuccessor` (~L6743–7150) including the
  7-kind outcome vocabulary, latch-based admission counting, and the park-epoch
  trap (`iterationOutcome.at` is never re-stamped — reading it as freshness
  misreads parked entries).
- **kotoba** re-verified: 16 surveyed files exist; godspeed 18 lines; omarchy
  392; wwkd 233 with "~600 lines per module" at L64–65; ufo 161; every quoted
  trigger string checked (sekhmet-l3 L7–8, bailian-gen L16, omarchy L10–11,
  bailian-cli L17 + fail-closed L23, ufo "fail closed" L26–27). Round 3 added
  the instruction-surface taxonomy (opt-in SKILL.md / always-on AGENTS.md /
  one-shot dispatch prompt) with the dispatch stanza order derived by `diff`ing
  two L1 prompts — a real pattern extraction, and it correctly noted the 1→3
  round-number skip.
- **kagi**: every failure text, exit code, gate, and boundary claim in its
  round-2 `SKILL.md` was independently re-derived by this aggregator from
  `~/.local/bin/the-janitor` (333 ln), `client.py` (117 ln), `tac-check` (88 ln),
  the overlay, and the agent card — including `steps: 4` and the max-steps
  precedent (`handoff-status.json` →
  `janitor_provenance.natural_language_request` = "returned maximum-steps text
  without creating requested artifact") and the boundary vocabulary
  (`boundaries.credentials_in_evidence/target_authority_conferred/
  safeguards_removed` all `false`). Zero defects found. The credential
  discipline held: no value, token, or `op://` ref path in any artifact.

---

## 2. Hallucination / citation check — failures

Every item below was reproduced by command. Severity: **F** = false pointer
(source does not say what the entry claims), **N** = unreproducible number,
**U** = unverifiable claim, **S** = scope/surface defect.

| # | Repo | Defect | Claimed | Observed (command) | Sev |
|---|---|---|---|---|---|
| 1 | kumitate | `128` swarm-lane cap attributed to the **installed ufo skill** | skill text says 128 | `rg -n '128' ~/.config/opencode/skills/ufo/ ~/.agents/skills/ ~/.claude/skills/` → 0 hits; `128` exists only in `scripts/ufo-swarm-wave.mjs` header as kimi `MAX_AGENT_SWARM_SUBAGENTS=128` | **F** |
| 2 | kotoba | 火山方舟/ark anti-trigger quoted as `bailian-train-deploy` **frontmatter** | frontmatter quote | `grep -E '火山方舟\|ark' bailian-train-deploy/SKILL.md` → no match; anti-routing is the body `## 反触发表` (L42+) | **F** |
| 3 | kengaku | `response.md`+`telemetry.json`+`judge.json` triple sourced to the **alpha-shittycodex** note | that page | `grep -n 'response.md' …alpha-shittycodex.md` → 0; filenames are in `godspeed-umwelt-iteration-3.md:156` | **F** |
| 4 | kasegi | Pendle package presented as the `claim_review`/hard-gate exemplar | `claim_review` in Pendle `status.json` | `grep claim_review claims/cantina-pendle/ingestion-20260915/status.json` → empty; gates verified on the `bugcrowd-seek/honest-zero` exemplar | **F** |
| 5 | kake | "`status:"pruned"` is inert in `probe.mjs`" | a pruned code path | `probe.mjs` has no `pruned` handling; every row with `url`+`expect` is probed equally | **F** |
| 6 | kake | registry size | 20 rows (README, `fleet-registry.md`, LOG, SKILL, report) | `len(sites)` = **21** (live 12 / pruned 3 / broken 3 / queued 3) | **N** |
| 7 | kake | clone count | ~40 | `ls -1 ~/Projects/webzites/repos \| wc -l` = **50** | **N** |
| 8 | kasegi | package count | 275 claim packages | 274 program dirs / **295** package dirs / 281 `status.json` — no rule yields 275 | **N** |
| 9 | kasegi | autopsy count | 30 files | `ls docs/autopsies/*.md \| wc -l` = **31** | **N** |
| 10 | kumitate | script inventory | `scripts/` 74 entries; `ufo-sighting-lib/` 25 files | `ls scripts \| wc -l` = **82** (78 files + 4 dirs); `find … -type f \| wc -l` = **26** | **N** |
| 11 | kotoba | `metadata.requires.bins:["bl"]` "across the bailian family" | all 10 | `grep -L 'requires:' bailian-*/SKILL.md` → 3 lack it (docs-llm-wiki, model-recommend, train-deploy); 7 carry `bins:["bl"]` | **N** |
| 12 | kotoba | "counterexample none found" for in-body trigger restatement | a completed sweep | no search command attached → nothing to falsify | **U** |
| 13 | kumitate | "~80% of SKILL.md content" | a measured proportion | no measure named | **U** |
| 14 | kengaku | README "Known gaps" example paths | `wiki/karpathy/creative-benchmark`, `wiki/ai/books/are-we-smart-enough` | both absent; actual `wiki/karpathy/gwern-essays-llm-and-ai-reasoning/creative-benchmark.md`, `wiki/biology/books/are-we-smart-enough.md` | **F** |
| 15 | kengaku | `PROVINCE.md` declares `~/wikillm/llm-wiki` | a real surface | path absent; lane works on `~/Projects/webzites/repos/llm-wiki`. Unfixed at round 3 **and** round 4 → per `PROTOCOL.md` (round-3 fix) this is now a failed obligation, not a gap | **S** |
| 16 | kake, kumitate | round-3 reports cited commits before they existed | `ddf40e2`, "commit `round-3`" | protocol lane observed both repos dirty at round 4; **both hashes now resolve** (`git cat-file -t ddf40e2` → commit; kumitate HEAD `efe19da round-3`) — defect was real and self-corrected inside the round | **S** |
| 17 | kasegi, kotoba, kumitate, kengaku, kake | round-3 reports omit the `SHONEN.md` checklist assessment | contract-minimum content | only kotoba's round-3 report carries one; `PROTOCOL.md` requires it of every lane report | **S** |
| 18 | round-1 fleet | report filenames | `<lane>.md` | `kengaku-shokunin.md`, `web-properties-publishing.md` — both non-conforming; fixed by protocol round 3 (`<id>.md`) | **S** |

No fabricated *domain content* was found: every false pointer above points at a
real file that says something slightly different. That distinction matters —
the failure mode this fleet has is **attribution drift**, not invention.

---

## 3. Structural / process findings

1. **Report-before-commit** (defect 16) is the most dangerous pattern found:
   a lane report is the round's evidence, and it cited work that existed only
   in a working tree. Protocol round 4 landed the fix ("a lane report lands
   last … must cite the hash … 'landed' means committed"). Aggregator
   endorses and adds: the integrator's step-1 verification should be a single
   command per lane — `git -C <repo> cat-file -t <hash>` — and a dirty
   participating repo should record the lane `in-flight`, not `ok`.
2. **Round-number drift has three sources**: driver steers (`.ufo/state/*.round`),
   lane-chosen commit tags (kumitate committed `round-2` under a round-3
   steer; kasegi has two `round-1` commits), and skipped rounds (kotoba 1→3,
   kagi 1→2, no round-2 for most lanes). Protocol round 4 made the steered
   number canonical. Observed residue: `MANIFEST.json` carries a fractional
   `"round": 1.5` entry, which no lane can label its commits against.
3. **`MANIFEST.json` `rounds[]` schema divergence**: `PROTOCOL.md` (round-1
   text) specified `lanes: [{id, status}]` + `mints`; the landed entry uses
   `lanes: {id: status}` + `minted` + extra keys (`type`, `protocol_updates`).
   Protocol round 3 aligned the spec to the landed shape — the right direction
   (spec follows practice, then practice is checkable) — but the round-1 entry
   still records `kagi: "not-dispatched"` while a kagi dispatch existed
   (`.ufo/prompts/kagi-L1.md`, `watchdog.log` 15:50:56 `launch kagi`), which
   the same protocol fix explicitly forbids. **Integrator action required.**
4. **Concurrent writers inside one `corpus/`.** Aggregator and kagi lane both
   wrote `kagi-shokunin/corpus/lessons/round-1.md` in the same minute
   (15:56 vs commit 15:56:42). Resolution: lane version restored
   (`git checkout --`), aggregator content moved to
   `lessons/round-1-aggregator-seed.md`, committed `9987054`. Rule landed in
   `CORPUS.md`: lanes own `round-<N>.md`; aggregator writes only
   `round-<N>-aggregator-*.md` and never edits lane files in place.
   Correction to the record: protocol round 4 attributed that dirty file to a
   kagi-lane "post-hoc rewrite of the aggregator-seeded lesson" — it was the
   aggregator's own in-flight write, now resolved.
5. **The round record is unversioned.** `.ufo/reports/`, `.ufo/waves/`,
   `.ufo/state/`, `.ufo/watchdog.log` are all untracked in the main repo
   (`git status`). Reports and waves are round *evidence* (protocol cites
   them); state and log are driver runtime. This commit adds
   `.ufo/reports/` + `.ufo/waves/`; recommendation: gitignore
   `.ufo/state/` and `.ufo/watchdog.log`, or commit them as ops telemetry —
   but decide, because right now a `git clean -xdf` destroys the round record.
6. **Aggregator write-scope** is now codified (protocol round 3: sole
   exception, corpus-only). Observed compliance: every aggregator write this
   round was under a child `corpus/` or a main-repo file it owns
   (`CORPUS.md`, `.ufo/reports/**`). No `MANIFEST.json`, `PROTOCOL.md`,
   `ROADMAP.md`, `SKILL.md`, `LOG.md`, or `PROVINCE.md` was touched by this
   lane.

---

## 4. Cross-lane learnings worth generalizing

Landed by this lane in `CORPUS.md` (corpus-scoped): counts carry their command;
negatives carry their sweep; quotes name their location; index rows are claims;
no credential material; corrections are new entries; per-round verdict per repo.

Proposed for `PROTOCOL.md` (protocol-lane / integrator owned — not edited here):

| # | Proposal | Evidence |
|---|---|---|
| P1 | **Evidence Standard addendum:** a numeric claim is evidence only with its counting command; an absence claim only with its search command. | defects 6–13 |
| P2 | **Citation precision:** a citation names file **and location** (frontmatter/body, header/code, script/installed skill). | defects 1–5, 14 |
| P3 | **Operator-gated domains:** where the terminal action is operator-owned (vault approval, publish click, claim submission), an end-to-end domain task may terminate at *prepared + verified + handed off*, with the handoff artifact as pointer. Without this, three provinces can never satisfy `SHONEN.md` box 2 no how well they work. | kagi `SHONEN.md` box 2 blocked on 1Password approval; kake publish is human by design (`kimi-surface.mjs` header); kasegi submission is 100% operator-executed (decree 2026-09-05) |
| P4 | **Promotion needs a named non-author reviewer per round, recorded in the round notes** — kotoba self-checked all four boxes in its round-3 report; `PROTOCOL.md` already forbids self-attestation, but nothing records the violation. | kotoba r3 report "SHONEN.md checklist assessment" vs aggregator verdict §5 |
| P5 | **Contested-scope rulings must be recorded, with a deadline.** Three items are open with no ruling: CDP 9222 + musketeer profile (kake ↔ kagi), `fleets/registry.json` lane→model routing (kasegi ↔ kumitate), where the fleet model map is pinned (kotoba ↔ protocol). | kake/kagi/kasegi/kumitate/kotoba reports, all rounds |
| P6 | **`SHONEN.md` boxes should be derived from `PROTOCOL.md` at mint time** (protocol lane raised this twice, unlanded): six copies of fixed text now drift from an evolving gate. | `*-shokunin/SHONEN.md` identical 4-box text vs `PROTOCOL.md` "Promotion gates" |
| P7 | **Dormancy arithmetic needs the driver's rounds.** `watchdog.log` shows lanes steered 1→3→4 within 40 minutes; "two consecutive completed rounds" can now elapse in under an hour. Either define a minimum round interval or count *dated* rounds. | `.ufo/state/*.round`, `watchdog.log` ticks 15:50:56 / 15:52:38 |

---

## 5. Promotion assessment (`SHONEN.md`, reviewed by a non-author)

Boxes: (1) decision tables + error patterns + checklist + cited sources;
(2) ≥1 logged end-to-end domain task; (3) executable without oral context;
(4) no cross-domain bleed.

| Repo | 1 | 2 | 3 | 4 | Aggregator ruling |
|---|---|---|---|---|---|
| kagi | ✅ verified line-by-line | ❌ no `the-janitor request` ever run (operator-gated 1Password approval) | ✅ | ✅ (CDP lease reported, not absorbed) | **Not promotable — blocked only by P3/operator.** Cleanest citations on the roster |
| kake | ✅ | ⚠️ round-3 live probe→registry correction *is* an end-to-end task (trigger→action→outcome→pointer); terminal publish is operator-owned | ✅ | ✅ | **Not promotable yet — fix defects 5, 6, 7 first.** Closest to box 2 after kagi |
| kasegi | ✅ | ⚠️ four rounds of real surface work (ops-script gate extraction, ledger/evidence census), but no mission executed against a program | ✅ | ✅ (`registry.json` reported, not absorbed) | **Not promotable — fix defects 4, 8, 9; then P3 decides box 2** |
| kumitate | ✅ | ❌ read-only code archaeology; no wave dispatched, no dispatcher run | ✅ | ✅ | **Not promotable — fix defect 1 (false pointer) first; it is in a lesson file, so it will be re-read as truth** |
| kotoba | ✅ | ⚠️ skill-file rewrites + this fleet's audits are real work product, but no activation evidence (its own gap list says so) | ✅ | ✅ | **Not promotable — defects 2, 11, 12; and its self-attestation (P4) must be struck from the record** |
| kengaku | ✅ | ⚠️ bench-arena + ledger telemetry analysis; the lane itself rules it "artifact interpretation, not an authored run" | ✅ | ❌ `PROVINCE.md` names an absent path, unfixed across rounds 3 and 4 | **Not promotable — box 4 fails; defects 3, 14** |

**No promotion this round.** No repo passes all four boxes under independent
review; one (kengaku) fails a box outright; two are blocked by the
operator-gated-terminal-action gap (P3) rather than by quality.

---

## 6. Mint / no-mint assessment

**Decision: NO MINT.** `PROTOCOL.md` requires two documented demand instances
for an unserved domain, or an explicit operator directive. Neither is met, and
the roster is not saturated.

Watchlist candidates tested against round evidence:

| Candidate | Demand instances observed | Served by an existing province? | Ruling |
|---|---|---|---|
| **kessho** — CI/verification harnesses | (a) this round's fleet-wide citation audit (5 L2 reviewer lanes re-executing commands); (b) kake's `webzites probe --all` / `sync-check` drift harness; (c) kumitate's single-sourced failure vocabularies as verification contracts | Yes, partially: (a) is aggregator-lane work, (b) is kake's, (c) is kumitate's. The *pattern* recurs but no demand was refused for lack of an owner | **No mint.** Record as 3 demand instances; if a round ever needs a verification harness and no province builds it, that is instance #4 and the mint becomes justified |
| **umihotaru** — fleet/pane wall ops | (a) `scripts/shokunin-watchdog.sh` v2/v3 round driver (main-repo tooling); (b) kumitate's sighting-wall + tmux surface map | (b) is squarely kumitate's; (a) is main-repo/integrator tooling, not a domain | **No mint.** One instance at most, and it is owned |
| **kagemusha** — substrate adapters & mirrors | (a) kengaku's reroute grammar + model-as-sequence rule from `ledger/telemetry.jsonl`; (b) kumitate's `route-resolution.md`; (c) kimi mirror byte-rewrite classes (kake) | (a)+(b) are kengaku/kumitate; (c) is kake | **No mint.** Demand is real but distributed and served |

Blocking reason that outranks all three: **five of six provinces have unmet
`SHONEN.md` boxes and zero promotions after four driven rounds.** Minting a
seventh domain now splits the same 450 s round budget across more unfilled
checklists. The binding constraint is not domain coverage — it is (i) citation
discipline (defects 1–14) and (ii) the operator-gated terminal action (P3).
Both are fixable without new roster entries.

**Mint trigger to re-test next round:** a lane report that names work it
*refused or could not place* because no province owns it. That is the demand
signal `PROTOCOL.md` means; none appeared in eight reports this window.

---

## 7. Aggregator self-assessment (recorded, per the no-self-attestation rule)

- Defect filed against this lane: it wrote `corpus/lessons/round-1.md` into a
  child repo whose lane was live, causing the collision in §3.4. Fixed by
  restore + namespace rule (`CORPUS.md`).
- Its own round-1 seeding also produced one citation error, corrected by the
  kagi lane: the seeded index cited `MANIFEST.json rounds[1].deferred`, a key
  that existed in an earlier manifest revision but not in the current bytes
  (`rounds[1].lanes.kagi`). Lesson generalized as P2 (cite location *and*
  revision) and as the `CORPUS.md` index-row rule.
- L2 reviewer payloads are mirrored verbatim into each repo's
  `round-1-aggregator-audit.md`; the aggregator's own re-executed commands are
  in §1–§2. Anything not reproduced by command above is marked ⚠️ or ❌ rather
  than asserted.

## 8. Integrator action list (this lane does not own these files)

1. Correct `MANIFEST.json rounds[1].lanes.kagi` (`not-dispatched` → the
   dispatched/reported truth) and land a `rounds[]` entry for rounds 2–4 in the
   schema `PROTOCOL.md` now specifies; `kagi: ok` for round 2 (`9b3e49f`,
   `round-2/kagi.md`).
2. Rule on the three contested-scope items (P5) and record the rulings in the
   round notes.
3. Record lane conformance: round-3 reports from kasegi, kake, kengaku,
   kumitate omit the `SHONEN.md` assessment (defect 17); kotoba's
   self-attestation is void (P4).
4. Land P1–P3, P6, P7 in `PROTOCOL.md` or record why not.
5. Decide the `.ufo/` versioning split (§3.5).
6. kengaku `PROVINCE.md` correction is now a failed obligation across two
   rounds — either the lane fixes it or the integrator records the lane
   non-conforming for the round.
