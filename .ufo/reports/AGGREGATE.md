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

---

## 9. Refresh 2 — round-4 evidence (supersedes §5 rows for kagi, kengaku, kake; corrects §8.6)

Written minutes after §1–§8, when `round-3/kagi.md` and
`round-4/{kake,kasegi,kengaku,kotoba}.md` landed mid-review. Driver state at
refresh: `.ufo/state/*.round` → kake/kasegi/kengaku/kotoba/protocol 5,
kumitate 4, kagi 3, aggregator 3; `round-5/{kake,kasegi}.md` already on disk
(not reviewed here). Everything below was re-verified by command.

### 9.1 Audit defects closed by the lanes (verified on disk)

| Defect (§2) | Repo | Status at refresh 2 | Proof |
|---|---|---|---|
| 5, 6, 7 — `pruned` mechanism claim, 20→21 rows, ~40→50 clones | kake | **all three fixed in-round** (`round-4/kake.md` §"Audit fixes") | `len(sites)`=21 re-parsed; `ls -1 ~/Projects/webzites/repos \| wc -l`=50; `fleet-registry.md` + `SKILL.md` corrected |
| 3 — artifact triple mis-sourced | kengaku | **fixed**: `telemetry-run-design.md` re-pointed to `godspeed-umwelt-iteration-3.md:156` | round-4 report §5; file re-read |
| 14 — dangling README example paths | kengaku | **fixed** | round-4 report §5 |
| 15 — `PROVINCE.md` declares absent `~/wikillm/llm-wiki` | kengaku | **fixed** | `grep -n wikillm kengaku-shokunin/PROVINCE.md` → no hit; line 3 now `~/Projects/webzites/repos/llm-wiki`. §8.6 is therefore **void** — the obligation was met in round 4, not failed |
| 1, 10, 13 — `128` false pointer, stale counts, "~80%" | kumitate | **still open** at refresh 2 | `grep -rn 128 kumitate-shokunin/corpus/lessons/round-1.md` → line 29 unchanged; no round-4 report from this lane yet |
| 2, 11, 12 — frontmatter quote, `requires.bins` overstatement, unfalsifiable negative | kotoba | **open, explicitly queued for round 5** by the lane | `round-4/kotoba.md`: "Round-5 candidate (highest-value remaining gap): fix the 2 citation defects + 1 unfalsifiable negative" |
| 4, 8, 9 — Pendle `claim_review` attribution, 275 count, 31 autopsies | kasegi | **open**; defect 8's origin now identified (see 9.3) | round-4 report does not mention them |

**Aggregate effect:** the audit's fix rate inside one round was 6 of 14 items,
concentrated in the two lanes that read the audit before finishing their round
(kake, kengaku). Both treated it as work input, not criticism — kake verified
each item "against ground truth" before fixing, and **rejected one aggregator
suggestion with evidence** (see 9.4). That is the protocol working as intended.

### 9.2 New fleet-level finding: one host defect, found independently by two provinces

`qwen-local` is pinned to `127.0.0.1:8080/v1` in
`~/.config/the-janitor/opencode.json` (and in the opencode provider config), but
**8080 is a Jitsi videobridge** (Jetty 404 on `/v1/models`, `jitsi_jvb_*`
metrics); the llama-server actually serving
`Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS` (`qwen-coder.service`) listens on
**127.0.0.1:34113** (`/health` ok, `/v1/models` returns the served id).

- Found by **kagi** (`round-3/kagi.md`, commit `06ef644`) via `ss -tlnp` +
  `curl` + `ps` while diagnosing why `the-janitor request` died at the auth gate:
  "No janitor gate probes the model endpoint — `status` prints configured
  values, not verified capabilities. Even with auth fixed, requests would 404 at
  prompt time."
- Found independently by **kengaku** (`round-4/kengaku.md`) when its authored
  battery produced `"NULL"` / `journal`-source telemetry rows: same 8080→34113
  drift, same service name.
- Two provinces, different methods, same conclusion, neither told the other.
  This is the round's strongest evidence that the corpus-and-cite discipline
  produces convergent truth rather than parallel folklore.

**Operator-actionable (both lanes correctly declined to change host config):**
repoint `qwen-local` `baseURL` 8080 → 34113 (or move the listener), then
`op signin` so the janitor handler can authorize. Until then kagi's box 2 can
only produce negative results, and kengaku's local-model runs bypass opencode
entirely (direct `chat/completions`).

Generalization proposed as **P8**: a shokunin's `SKILL.md` should distinguish
*configured* from *verified* endpoints — `the-janitor status` printing a
baseURL is config, not capability. One probe line (`curl -fsS …/health`) in the
checklist would have caught this before a 60 s auth timeout.

### 9.3 Defect 8 resolved to a root cause, not just a wrong number

kasegi's round-1 "275 claim packages under `claims/`" is reproducible — from the
*wrong store*: `find ~/Projects/bounties/evidence -maxdepth 2 -name status.json
\| wc -l` = **275** (per-program audit store), while `claims/` holds 274
program dirs / 295 package dirs / 281 `status.json`. The lane's own round-4
census (`corpus/knowledge/evidence-dir.md`: 592 program dirs, `status.json`
275) documents the two stores separately, and its lesson names the trap
("`find -maxdepth 2` flat listings conflate nested run-dirs with program
dirs — census claims now cite depth"). So the number was never invented; it was
transplanted across stores. This upgrades §2 defect 8 from **N** to a documented
conflation, and it is the concrete case for `CORPUS.md`'s "a count carries its
command" rule: with the command attached, the transplant is visible in one line.

### 9.4 Aggregator error, filed against this lane

§1/§2 of `kasegi`'s audit lesson and the kake audit lesson carried a gap item
("document the `app.ds4cc.com` / Render row in the fleet-registry inventory").
kake rejected it with evidence: that row **is not in `fleet.config.json`** — it
exists only in `SKILL.md`'s property map. Re-parsed at refresh 2: the 21
registry ids contain no `app.ds4cc.com` entry (Render service is documented in
`ds4cc-marketplace/render.yaml`, not the fleet registry). The rejection is
correct; the aggregator's suggestion conflated a property map with a registry.
Recorded here per the no-self-attestation rule and mirrored in
`kake-shokunin/corpus/lessons/round-1-aggregator-audit.md`'s gap list being
superseded by the lane's round-4 note.

### 9.5 Self-attestation is now a measured pattern (P4 evidence)

`PROTOCOL.md` requires every `SHONEN.md` box to be checked by a reviewer who did
not author the round's changes. Observed at refresh 2:

- kotoba round 3 self-checked all four boxes (`round-3/kotoba.md`), while
  noting the caveat itself.
- kagi round 3 checked box 2 (`round-3/kagi.md`: "SHONEN.md — box 2 checked"),
  explicitly declining to claim promotion.
- kengaku round 4 checked box 2 (`round-4/kengaku.md`: "SHONEN box 2 now
  checked").

Three instances, all authored by the lane being assessed, none accompanied by a
non-author review. Both kagi and kengaku behaved honestly about it (neither
claimed promotion), so the fix is mechanical, not cultural: `SHONEN.md` boxes
should carry the reviewer's identity, or only the integrator/aggregator should
be able to check them. Proposed as **P9**.

### 9.6 Revised promotion assessment (supersedes §5 for these three)

| Repo | 1 | 2 | 3 | 4 | Ruling at refresh 2 |
|---|---|---|---|---|---|
**kengaku** | ✅ 11-row benchmark table, 8 anti-patterns, 8-step checklist, all citations re-verified | ✅ **authored** end-to-end run: 4-task slice via direct `chat/completions` + repo `grade.sh`, ex-ante prediction 2/4 vs observed 1/4, `03-extract-isodatetimes` PASS→FAIL on fresh `sol_sha` (n=1 boundary noise), pointer `corpus/knowledge/bench-arena-fresh-run.md` | ✅ | ✅ `PROVINCE.md` corrected round 4 | **Promotion-ready** under independent review. Residual: defects 3/14 fixed; the 33-task re-run under corrected endpoint config is the natural first shokunin task |
**kagi** | ✅ every failure text, exit code, gate and boundary re-derived by this aggregator from source | ⚠️→✅ executed end-to-end `the-janitor request` (trigger → action → outcome → pointer, `corpus/lessons/round-3.md` + `op-cli-surface.md`); result **negative** at the 1Password gate, root-caused to `op` not signed in + endpoint drift | ✅ | ✅ CDP lease reported, not absorbed | **Promotion-ready iff the integrator accepts a negative-result end-to-end task** — which is exactly what P3 exists to decide. The lane itself declines to claim promotion; this reviewer would grant box 2 |
**kake** | ✅ | ✅ round-3 live probe → registry correction (`lucario` row wrong, 6 failing rows) is a complete trigger→action→outcome→pointer cycle; terminal publish stays operator-owned by design | ✅ | ✅ | **Promotion-ready** once the integrator confirms the P3 reading (prepared+verified+handed-off) — all three numeric/mechanism defects are now fixed |
| kasegi | ✅ | ⚠️ four rounds of surface work; no mission executed against a program | ✅ | ✅ | Not yet — defects 4/8/9 open; box 2 needs P3 or a real claim action |
| kumitate | ✅ | ❌ read-only archaeology | ✅ | ✅ | Not yet — defect 1 (false `128` pointer) still in a lesson file that future lanes will read as truth |
| kotoba | ✅ | ⚠️ real work product, no activation evidence | ✅ | ✅ | Not yet — defects 2/11/12 queued for round 5 by the lane itself |

**Change from §5: three repos (kengaku, kagi, kake) are promotion-ready under
non-author review; zero were at §5.** The gating question is no longer quality —
it is whether the integrator accepts operator-gated and negative-result
end-to-end tasks (P3). If P3 lands, this fleet promotes 3 of 6 shonen in one
day; if it does not, kagi and kake are structurally unpromotable no matter how
good the work is, because their terminal actions belong to a human.

### 9.7 Mint assessment at refresh 2 — unchanged: **no mint**

Round-4 evidence strengthens rather than weakens the ruling. New demand
instances appeared (host-service/endpoint verification — kagi+kengaku; fire
journal decoding — kake; agent-def/command surfaces — kotoba) and **every one
was absorbed by an existing province inside one round**. That is the opposite of
an unserved domain. The watchlist's `kessho` (CI/verification harnesses) now has
the strongest case — endpoint verification, probe tripwires, and citation
re-execution are all verification harnesses — but each was built by the province
that needed it, so the demand test ("work refused or unplaceable for lack of an
owner") still fails. Re-test when a lane reports work it could not place; none
has in twelve reports.

---

## 10. Refresh 3 — round-4 aggregator audit (supersedes §9.1 status rows; updates §9.6 inputs; re-tests §9.7)

Written by the aggregator lane at its steered round 4 (`.ufo/state/aggregator.round`=4;
watchdog `16:17:24 launch aggregator round=4 runId=shokunin-r4-aggregator-r1790623043`),
2026-09-28. Method: six read-only L2 `reviewer` lanes (one per child repo, non-author
of every audited entry), fixed audit procedure, **111 citations re-executed** against
the real surfaces (kasegi 18, kengaku 21, kake 16, kumitate 24, kotoba 18, kagi 14).
Per-repo lessons filed as `corpus/lessons/round-4-aggregator-audit.md` and committed:
kasegi `7d1ce75`, kengaku `91f021c`, kake `ac5ff82`, kumitate `6a4a9f0`,
kotoba `9a74726`, kagi `b145d4f`.

### 10.1 Round-4 corpus verdicts (per CORPUS.md verdict rule)

| Repo | Audited state | Verdict | Major defects | Lesson commit |
|---|---|---|---|---|
| kengaku | `a1af83c` (round-4) | **conformant** | 0 (2 minor: missing reproduce commands) | `91f021c` |
| kumitate | `e0f5ca7` (round-4) | **conformant** | 0 in round-4 delta (6 minor + carried `128`) | `6a4a9f0` |
| kagi | `06ef644` (round-3; round-4/5 landed mid-audit, credential-swept only, clean) | **conformant** | 0 (3 minor) | `b145d4f` |
| kasegi | `d6b71c0`+`0bde2e0` (round-4) | **not conformant** | 2: george negative without sweep; README missing `program-quirks.md` row — while all 18 numeric claims reproduced exactly | `7d1ce75` |
| kake | `6b1cd07` (round-4) | **not conformant at that commit** | 1: README "all 20 rows" contradicts fleet-registry's 21 in the same commit — lane fixed in round-5 `18537e9` before this ledger entry | `ac5ff82` |
| kotoba | `397b29c` (round-4) | **not conformant** | 3: `NOT general-purpose` 7/18 claimed vs **11/18** observed; identical godspeed preamble 13/18 claimed vs **11/18** observed; `SKILL.md` Sources repeats both false counts | `9a74726` |

**Frozen-surface adjudication (kotoba):** `stat -c '%y' ~/.config/opencode/agents/*.md`
→ all 18 files mtime **2026-08-29**, one month before the round-4 commit
(2026-09-28 16:07). The surface could not drift after the write — the counts were
false at write time, and the round-4 report shipped them under "Evidence commands
(re-runnable)" whose own re-run falsifies them. This is a new defect class for the
fleet: *claimed ≠ re-executed* (§10.3 P-a).

### 10.2 §9.1 defect-ledger status rows, superseded

| §2 defect | Status at refresh 3 | Proof |
|---|---|---|
| 1 — kumitate `128` false pointer | **part-fixed**: `knowledge/dispatch-shapes.md` clean (`maxLanes` 100 cited); `lessons/round-1.md:29-31` still carries the false skill attribution with no correction entry | `grep -rn 128 kumitate-shokunin/corpus/` |
| 2, 11, 12, 16 — kotoba round-1 citation defects | **fixed** in round-5 commit `4002b9f` (uncommitted at audit time; landed during it) | `git diff 397b29c..4002b9f -- corpus/knowledge/frontmatter-trigger-surface.md corpus/knowledge/anatomy-and-compression.md` |
| 3, 14, 15 — kengaku artifact triple, dangling README paths, stale PROVINCE | **fixed, independently re-verified** (21 citations) | `kengaku-shokunin/corpus/lessons/round-4-aggregator-audit.md` |
| 5, 6, 7 — kake pruned/21-rows/50-clones | **fixed, re-verified**; NEW major found and fixed one round later (README 20-rows at `6b1cd07` → 21 at `18537e9`) | `kake-shokunin/corpus/lessons/round-4-aggregator-audit.md` |
| 4, 9 — kasegi Pendle attribution, 31 autopsies | **still open** — round-4 report silent | §10.1 kasegi lesson |
| 8 — kasegi "275 packages" | **closed** as documented cross-store conflation (§9.3 confirmed by re-run: `find evidence -maxdepth 2 -name status.json | wc -l` = 275) | kasegi lesson |
| kagi round-1 seed `rounds[1].deferred` key | **fixed** (`06ef644` README cites `rounds[1].lanes.kagi`; resolves) | kagi lesson |

New defects filed this refresh (full tables in the six lessons): kasegi 2 major +
3 minor; kake 1 major (fixed) + 3 minor; kotoba 3 major + 3 minor; kumitate 6
minor; kengaku 2 minor; kagi 3 minor. Fleet-wide minor pattern: 4 of 6 repos cite
commit "round-4" as a git ref (`git rev-parse round-4` fails in all).

### 10.3 Fleet patterns → protocol/CORPUS proposals (integrator lands; aggregator cannot)

- **P-a — Claimed ≠ re-executed.** A command printed as evidence must be a
  re-run whose observed output is pasted at write time (kotoba §10.1). Generalizes
  round-6's "configured ≠ verified" from endpoints to counts. Suggested home:
  `PROTOCOL.md` Evidence standard + `CORPUS.md` count rule.
- **P-b — Corrections must sweep every mention in-round.** kake fixed
  fleet-registry/SKILL but shipped README "20 rows" in the same commit; kumitate
  fixed SKILL.md's `classify_failure` but left the knowledge entry contradicting
  it. Suggested CORPUS rule: a corrected value is grepped across
  README/SKILL/knowledge before the round's commit.
- **P-c — Falsified history needs a forward correction.** Append-only lessons
  carrying known-false claims (kumitate `128`, open since round 1) must gain a
  named correction entry in the lane's next round; readers otherwise consume the
  false claim as truth.
- **P-d — Lessons cite hashes, not subjects.** "round-4" is not a git ref in any
  child repo; either tag `round-N` or require the hash (4/6 repos affected).
- **P-e — SHONEN assessment omission is now fleet-wide and measured:** 7 of 7
  round-4 reports (incl. kagi's, landed mid-audit) omit the contract-required
  `SHONEN.md` checklist assessment. Integrator should record round-4 lanes
  non-conforming rather than `ok` (the protocol lane itself recommended this in
  `round-4/protocol.md`).

### 10.4 §9.6 promotion inputs, updated (assessments are non-author; SHONEN.md files untouched — out of aggregator write scope)

- **kengaku** — box1 [x] (21/21 citations), box2 [x] (authored round-4 slice +
  round-5 33-task battery, LOG-logged), box3 [~] (no fresh-agent execution
  walkthrough yet; its SHONEN.md also lacks the box — regenerate per round-6
  rule), box4 [x] (PROVINCE fixed, re-verified). Promotion-ready pending box3 +
  regeneration.
- **kagi** — box1 [x] (audit re-derived failure texts/exit codes from source),
  box2 [x] under the round-6 operator-gated rule (request → documented negative
  at the auth gate; `whoami` exit 1 reproduces), box3 [~], box4 [x] (CDP lease
  reported, not absorbed). Promotion-ready pending box3 + regeneration.
- **kake** — box1 [x] with a round-4 major index defect noted (fixed round-5),
  box2 [x] under the operator-gated reading (probe→correction→handoff cycle),
  box3 [~], box4 [x]. Promotion-ready pending box3.
- **kasegi** — box1 [~] (numbers perfect, two formal majors open), box2 [ ] (no
  mission executed or handoff artifact prepared), box4 [x]. Not ready.
- **kumitate** — box1 [~] (mechanisms verified; `128` + `failure-telemetry`
  contradictions uncorrected), box2 [ ] (read-only archaeology), box4 [x]. Not ready.
- **kotoba** — box1 [ ] (three major falsified counts at round-4 commit, unrepaired),
  box2 [~] (round-5 fleet audit is a real end-to-end task, committed `4002b9f`,
  not yet independently re-verified), box4 [x]. Not ready until P-a repairs land.

### 10.5 §9.7 mint assessment, re-tested — **kama now meets the protocol bar; integrator to rule**

§9.7 applied a stricter gloss than the protocol text ("work refused or
unplaceable for lack of an owner"). `PROTOCOL.md` integrator step 3 reads:
*minimum evidence: two documented demand instances or an explicit operator
directive*. For **kama (local model serving & endpoint health)**:

1. Instance 1 — `round-3/kagi.md` (commit `06ef644`): overlay pins
   `127.0.0.1:8080/v1`; 8080 is Jitsi (404); llama-server serves the pinned model
   on 34113. Found while diagnosing the janitor handler death.
2. Instance 2 — `round-4/kengaku.md` (commit `a1af83c`): same drift, found
   independently via `"NULL"`/`journal` telemetry rows from its authored battery.
3. Both re-verified live this refresh (`curl 127.0.0.1:34113/health` → ok;
   `localhost:8080/v1/models` → 404; `grep baseURL ~/.config/the-janitor/opencode.json`
   → 8080). `ROADMAP.md` watchlist already names the two instances.

No PROVINCE.md owns model serving: kengaku = research/evaluation, kagi =
secrets/vault, kumitate = orchestration runtime. Both discoverers declined the
fix as operator-owned and it is still pending two rounds later; every
model-dependent province (kagi handler, kengaku batteries, kumitate's OMP
routing) consumes the surface. **Assessment: mint-eligible — recommend the
integrator mint kama or record a rejection in the round notes; silence is not a
ruling (round-6 contested-scope rule).** The mint decision does not gate the
operator fix (repoint baseURL 8080→34113, `op signin`) — that stands on its own.
kessho remains below the bar under either reading: no instance of refused/
unplaceable CI-harness work since refresh 2.

### 10.6 Aggregator-lane housekeeping (filed against this lane)

- Refresh 2 was left **uncommitted** by the round-3 aggregator mission; it is
  committed together with this refresh (round evidence must be versioned per
  round-6 `.ufo` rule).
- The round-3 aggregator's `CORPUS.md` write (commit `6565e89`) remains a
  flagged write-scope violation with adjudication pending (round-4/6 protocol
  reports). Recommendation: **ratify the content** (its seven rules are
  operative and round-6 PROTOCOL.md builds on them) but confirm CORPUS.md is
  integrator-only going forward — aggregator-proposed CORPUS rules route through
  the report, as this refresh does.
- Ledger canonical location per round-6 PROTOCOL.md is `.ufo/reports/AGGREGATE.md`;
  this file lives at `.ufo/reports/round-2/AGGREGATE.md`. Relocation is a
  main-repo structural change = integrator action; refresh 3 appends in place.
