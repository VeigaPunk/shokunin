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

---

## 11. Refresh 4 — round-6 aggregator audit (canonical path; supersedes §9.1, §10.1, §10.2, §10.4, §10.5, §10.6)

**Stamp.** Aggregator lane, steered round 6 (`.ufo/state/aggregator.round` = 6; runId
`shokunin-r6-aggregator-r1790629072`; prompt `.ufo/prompts/aggregator-round-6.md`).
Written 2026-09-28 21:57Z→22:3xZ (local 18:5x -03). Main-repo HEAD at the
after-measurement: `8ec7a56`. Anchor revisions of the two integrator files a live
protocol lane was editing during this round: `PROTOCOL.md` `sha256 9e700d691307…`
(576 lines at 21:44Z; it grew 387 → 576 mid-round, and the protocol lane's own
round-10 report says 583), `ROADMAP.md` `sha256 d9a6ad856cf7…`. Line numbers in
those two files are soft; quoted clause text is the durable pointer.

**Relocation — protocol duty discharged.** `git mv .ufo/reports/round-2/AGGREGATE.md
.ufo/reports/AGGREGATE.md`, per PROTOCOL.md: *"canonically `.ufo/reports/AGGREGATE.md`
(the `round-2/AGGREGATE.md` snapshot is relocated there by its next refresh; no other
path counts)"*. Before-state `ls .ufo/reports/AGGREGATE.md` → *No such file or
directory*, re-checked 21:43Z by the reviewer L2 and 21:57Z by this lane. §1–§10 move
as unchanged bytes (`wc -l` → 557 pre-append). §10.6's ruling that relocation is
"integrator action" is **superseded** by the round-9 clause quoted above; this refresh
is the first at the canonical path, so the protocol lane's round-10 fallback queue
(`.ufo/reports/round-10/protocol.md` §Routing lines, 49 rows) now has a durable home
and is reconciled in §11.2 rather than duplicated.

**Method.** 11 read-only L2 subagents in one batched dispatch (MISSION.md floor is 8):
six per-repo `scout`s, plus `critic`, `reviewer`, `sentinel`, `connector`, `planner`.
Route buckets conform to the MISSION.md map (`planner`/`connector` → `m_lunamax`;
`scout` → `m_flash`; `reviewer`/`critic`/`sentinel` → `m_zfl`); no
`m_composer`/`m_antigravity`. **100 citations re-executed** against the live surfaces —
kasegi 18, kengaku 13, kake 18, kumitate 15, kotoba 18, kagi 18. Counting rule:
`awk '/^## Re-executed citations/{f=1;next} /^## /{f=0} f' <lesson> | grep -c '^|'`
minus the 2 header rows; kasegi's section is a bullet list → `grep -c '^- '` → 18.
Every L2 was read-only in both repos; only the aggregator wrote files, and each file
was committed at creation time (§11.7 self-defect 1 records the one that was not).
The `reviewer` L2 independently re-executed all six lesson drafts before this lane
committed them: 4 `clean`, 2 `needs-fix` (kengaku index counts window-stale,
kumitate rule-9 row overtaken by a lane commit) — both fixed by the appended
`## Post-audit re-measurement` sections in `1bd17ec` / `31f09cd`.

### 11.1 Round-6 corpus verdicts (CORPUS.md rule 10) and lesson commits

| Repo | Audited HEAD | Verdict (failed rules) | Majors / defects | Lesson commits (`aggregator-shokunin <aggregator@shokunin.local>`) |
|---|---|---|---|---|
| kasegi | `fb9ac8e` (r11; r12 child work uncommitted at audit) | **not conformant** — 4, 5, 7, 9 (contested), 1/6 | 7 / 11 | `d341b48` |
| kengaku | `f147a27` (r7; r8–r9 uncommitted) | **not conformant** — 7, 9, 4 | 5 / 12 | `3175e69`, re-measure `1bd17ec` |
| kake | `dd4eabf` (r10) | **not conformant** — 4, 1 | 5 / 11 | `ab8c9e2` |
| kumitate | `7a4c9a0` (r7; r8 in flight) | **not conformant** — 7, 6, 4, 1, 2, 9 | 6 / 12 | `0ac2272`, re-measure `31f09cd` |
| kotoba | `8e22a41` (r9, clean tree) | **not conformant** — 4, 1/2/6, 7, 3 | 5 / 9 | `778310d` |
| kagi | `e64e81b` (r9, clean tree) | **not conformant** — 4 only | 6 / 10 | `ad694a2` |

Totals: **34 majors, 65 defects, 69 routed rows written into the six lessons.**
Commands: majors `awk '/^## Defects/{f=1;next} /^## /{f=0} f' <lesson> | grep -cE
'^[0-9]+\. \*\*(MAJOR|major)'` (kengaku uses a `**Major**` subhead →
`awk '/^\*\*Major\*\*/{f=1;next} /^\*\*Minor\*\*/{f=0} f' <lesson> | grep -cE '^[0-9]+\.'` → 5);
routed rows `awk '/^## Routed-defect rows/{f=1;next} /^## /{f=0} f' <lesson> | grep -c '|'`
summed over the six → 11+15+12+10+10+11 = 69. All six lessons committed and pushed
(`git -C <repo> rev-list --count origin/master..HEAD` → 0 for all six at 21:56Z).

**No repo is conformant.** The dominant failed rule is **4 (a count carries its
command)** — 5 of 6 repos — and in three of them the falsified count sits inside a
`SCORECARD.md` score cell (kagi four numbers, kumitate three, kotoba two): the
fleet-2 axis artifact is inheriting the corpus's oldest defect class. Second is
**7 (an index row is a claim)** — 4 of 6 repos, all in the files→rows direction
(aggregator-owned lessons and new lane lessons unindexed).

**Clean everywhere, verified not assumed — rule 8 (no credential material).** The
`sentinel` L2 ran 15 sweep classes over both repos and all seven git histories:
70 `op://` hits are prose/schematic placeholders or the sweep pattern quoted in a
prior lesson; 16 cookie/bearer hits are identifier-format docs (kumitate) or
declared-fake localhost fixtures (kagi); `sk-`/`ghp_`/`github_pat_`/`xox*`/`AKIA`/
JWT/`BEGIN … PRIVATE KEY` bodies → **0**; pickaxe history (`git log -S`/`-G`) across
all seven repos → no token body ever added or removed; the untracked working-tree
files (`kengaku corpus/evidence/`, `kake scripts/`, kagi's drift TSVs, now tracked)
→ 0. kagi's committed `drift-baseline.tsv`/`drift-symbols.tsv` carry sha256 pins and
paths only: the 10 live `op.env` key names tested `grep -qF` against both TSVs →
`keys scanned: 10 / appearing literally: 0`. Rule 9 held in five repos; kumitate
breached it and committed the breach (§11.2 D-50).

### 11.2 Routed-defect queue — the durable rows (reconciled against the round-10 fallback queue)

Reconciliation rule: the protocol lane's round-10 report was the queue of record while
this ledger was absent (its own words: *"the aggregator's canonical ledger is still
absent … this section is the queue of record"*). Its `D-nn` ids are **adopted as the
ledger's keys** — no parallel numbering. Every row was re-tested on disk this round;
new rows continue the series from `D-50`. Full defect text for `D-01…D-49` stays in
`.ufo/reports/round-10/protocol.md` §Routing lines; per-repo detail with re-executed
commands is in the six committed lessons (§11.1). Statuses are as of 21:57Z, main HEAD
`8ec7a56`, child HEADs kasegi `fb9ac8e`, kengaku `1bd17ec`, kake `dd4eabf`,
kumitate `31f09cd`, kotoba `8e22a41`, kagi `ad694a2`.

**A. Status changed since round 10 (re-tested, not inherited)**

| # | Owner | Defect | Status @ r6 | Proof |
|---|---|---|---|---|
| D-01 | kasegi | "275 claim packages/dirs" family | **PARTLY** — a proper appended correction landed (`LOG.md:282-286`, r12: 275→274 dirs / 295 packages, 19→20, BLOCKED 16→15, bh 21→22); `SKILL.md:163` still prints `status.json 275` vs live **280** — P-b (sweep every mention) unsatisfied in a mutable file | `sed -n '163p' kasegi-shokunin/SKILL.md`; `ls -d claims/*/*/status.json \| wc -l` → 280 |
| D-02 | kasegi | receipt overclaim | **PARTLY** — correction entry landed; `submitted-registry.md:17-19` reproduces (1 receipt, mozilla only) | `find claims -name receipt.md \| wc -l` → 1 |
| D-03 | kasegi | histogram sums 282 ≠ 280 | **PARTLY** — `SKILL.md:459` + `submitted-registry.md:195` reproduce 248/15/15/2 = 280; `lessons/round-9.md:33` still sums 282 (append-only → correction entry owed, D-53) | lesson `d341b48` defects 1, 7 |
| D-04 | kasegi | "19 claim-* missions", "16 L0 briefs" | **PARTLY** — `README.md:23` corrected to 20; **four sites still say 19** (`ufo-archive-2026.md:11`, `SKILL.md:385`, `lessons/round-8.md:10`, `README.md:49`) and `ufo-archive-2026.md:36` still says 16 (live: 15 per-program + farmscout + feeder + `dispatch.log` = 18 entries) | `ls -d fleets/ufo-archive-2026/missions/claim-*/ \| wc -l` → 20; `ls fleets/ufo-archive-2026/inquiries/bounty-fleet-2026-09-06/ \| wc -l` → 18 |
| D-10 | kagi | drift-gate baselines untracked | **CLOSED** at `e64e81b` — `drift-baseline.tsv` (15 rows) + `drift-symbols.tsv` (19 pins) + `knowledge/drift-gate.md` committed; gate re-run: `DRIFT_PINS: CLEAN (files=15 symbols=19)` exit 0, `--selftest` `PASS (13 cases)`, and a falsified baseline copy → `DRIFT …/opencode.json sha deadbeef0000->a318e719a04b`, `DRIFT (files_ok=14 files_bad=1)` exit 1. Residual: round-10 helpers untracked (`corpus/state-shape.tsv`, `surface-census.sh`, `surface-census.tsv`, `knowledge/surface-census.md`, `lessons/round-10.md`) | `git -C kagi-shokunin ls-files corpus/drift-baseline.tsv corpus/drift-symbols.tsv \| wc -l` → 2; `git -C kagi-shokunin status --porcelain` |
| D-11 | kagi | `SHONEN.md` regeneration | **CLOSED** at `e64e81b` — seed-identical modulo `<name>`, box char, one indented evidence line per box (reviewer L2 `diff` exit 0; re-checked by this lane: 4 boxes, 0 bare `[~]`). The marks still fail the promotion gate → **D-63** | `grep -c '^- \[' kagi-shokunin/SHONEN.md` → 4 |
| D-21 | kumitate | README missing 5 knowledge + 5 lesson rows | **CLOSED** at `2075363` — 31 index rows ↔ 32 tracked corpus files; the single unindexed file is this round's aggregator lesson (owner-indexed next round) | `git show HEAD:corpus/README.md \| grep -coE '^\| .(knowledge\|lessons)/'` → 31 |
| D-28 | kotoba | `SHONEN.md` regeneration | **CLOSED** at `e997d45`/`8e22a41` — 4 `[~]` boxes + one indented evidence line each; sole byte deviation is the missing trailing newline (D-72). The falsified counts *inside* box 1's evidence line stay open (D-29) | `cmp` vs seed regenerated from PROTOCOL.md's canonical block |
| D-30 | kotoba | lane commit identity | **PARTLY** — repo-local `kotoba-shokunin <kotoba@shokunin.local>` configured + logged; `e997d45`/`8e22a41` canonical; `3b029b8` (operator) and `8c300ad` (`shokunin@local`) are immutable history | `git -C kotoba-shokunin config --local user.email` |
| D-32 | kotoba | duplicate-skill-warning disposition untracked | **CLOSED** — `corpus/knowledge/opencode-offer-trace-round8.md` tracked at `8e22a41`; its counts reproduce (1918 `duplicate skill name` lines, 190 `init count=`) | `git -C kotoba-shokunin ls-files corpus/knowledge/opencode-offer-trace-round8.md \| wc -l` → 1 |
| D-33 | aggregator | canonical ledger absent; no refresh since r4; zero durable queue rows | **CLOSED this refresh** — `git mv` to `.ufo/reports/AGGREGATE.md`, §11.2 populated, `.ufo/reports/round-6/aggregator.md` filed | `test -f .ufo/reports/AGGREGATE.md && echo 1` → 1 |
| D-44 | kake | `probe-delta.mjs` hardcoded `/home/kake/...` | **CLOSED** at `dd4eabf` — default path built from `process.env.HOME` (`scripts/probe-delta.mjs:33`) | `grep -rn '/home/kake' kake-shokunin/ \| wc -l` → 0 |
| D-45 | kake | axis-move recorded unmeasured ("(pending)") | **CLOSED** at `dd4eabf` — move log carries measured values, all re-executed by the scout L2 (6 delta events / 0 phantom over 76 rows; exits 0/2/64; probe 12 ok / 5 violated / 1 error). Residual: no counting command or measured-against commit per row → **D-58** | `node scripts/probe-delta.mjs --history ~/Projects/webzites/state/probe-history.jsonl --json` |
| D-47 | aggregator | six round-6 lessons uncommitted at creation | **CLOSED for the six lessons** — committed 21:52–21:56Z under `aggregator-shokunin`, pathspec-limited, pushed (all six `rev-list --count origin/master..HEAD` → 0). Too late for kumitate, which swept one into `a6f9456` → **D-50**. Re-classified: the three kagi `corpus/` helpers named in the r10 row are the *lane's* round-10 work, not aggregator files | `git -C <repo> log --oneline -1 -- corpus/lessons/round-6-aggregator-audit.md` |
| D-31/D-36/D-37 | kumitate, kake, kagi, kasegi | three contested surfaces | **RULED at r10** (session-store split; CDP lease = operator-side arbitration with a documented split; `fleets/registry.json` split decrees/routing). The rulings owe a `PROVINCE.md` record in each repo → **D-76** | `.ufo/reports/round-10/protocol.md` §Contested-scope rulings |
| D-41 | aggregator | round-3 commit `6565e89` touched `CORPUS.md` + nine prompts | **ADJUDICATED at r10** — historical conformance defect, no rewrite, scope text now explicit. Accepted by this lane; recorded in §11.7 | `.ufo/reports/round-10/protocol.md` §Contested-scope rulings, item 4 |
| D-39 | operator | `qwen-local` 8080→34113 repoint, `op signin` | Not re-tested (no audited surface needed it); r10 recorded LANDED-serving with the `op signin` half unverifiable. Unchanged | `.ufo/reports/round-10/protocol.md` §Routing lines D-39 |

**B. Re-flagged OPEN — unchanged after re-test (row text in the r10 report; proof re-run this round)**

| # | Owner | Defect (short) | R | Re-test @ r6 |
|---|---|---|---|---|
| D-05 | kasegi | r8 report cites `ledger/candidates.jsonl` for do-not-re-hunt; file carries none; no errata | 8 | OPEN — no errata entry in `LOG.md` (`grep -c candidates.jsonl kasegi-shokunin/LOG.md` → citation only) |
| D-06 | kasegi/external | `claim-index.mjs` ignores `claim-hold/*`; 3 packages queued regardless | 10 | documentation LANDED (`knowledge/operator-queue.md`); external fix owner unchanged |
| D-07 | kasegi/operator | queue row 4 = byte-identical duplicate of the 2026-09-06 anthropic VDP; `claim-check.mjs` returns OK | 9,10 | OPEN as data; do-not-file documentation landed |
| D-08 | kagi | bare `handoff-status.json` cites in `SKILL.md` (4 mentions, 0 absolute paths) | 5,7,8,9 | OPEN — 5th refresh: `grep -c 'local/state/tac/handoff-status.json' kagi-shokunin/SKILL.md` → 0 |
| D-09 | kagi | `SKILL.md:28` `op.env` prerequisite row lacks the fail-closed stop note | 5,7,8,9 | OPEN — `grep -n missing kagi-shokunin/SKILL.md` → drift-gate and usage lines only |
| D-12 | kengaku | round-8 defects closed **by history rewrite**; r7 report cites orphaned `85b22e3` | 9 | OPEN — `git -C kengaku-shokunin merge-base --is-ancestor 85b22e3 HEAD` → exit 1; `fsck --lost-found` → dangling |
| D-13 | kengaku | `LOG.md:9` round-5 entry rewritten in place; no appended correction | 9 | OPEN — `git -C kengaku-shokunin diff 85b22e3 f147a27 -- LOG.md` → one unannotated `-`/`+` pair |
| D-14 | kengaku | noise-n25 discordance denominator | 9 | OPEN, **wording corrected**: the falsified on-disk token is `0/12 PASSes` at `:23-24` (the file's own `:13` table fixes PASS/25 = 17); the `0/25` discordance figure is consistent |
| D-15 | kengaku | `SHONEN.md` stale 3-box variant | 8,9 | OPEN — the **only** non-conforming seed left fleet-wide: `grep -c '^- \[' kengaku-shokunin/SHONEN.md` → 3, all three bare `[x]` with inline prose |
| D-16 | kengaku | `corpus/lessons/round-6.md` missing although r6 corpus work landed (`d5f1cad`) | 9 | OPEN — `ls kengaku-shokunin/corpus/lessons` → no lane `round-6.md` |
| D-17 | kumitate | defect-1: `lessons/round-1.md:29-32` "installed ufo skill says the swarm cap is 128 lanes" | 4,7,8,9 | OPEN — **5th refresh**; `grep -rn '128' ~/.config/opencode/skills/ufo/` → no matches (exit 1); `128` exists only as kimi parity in `scripts/ufo-swarm-wave.mjs:13,:203`; `git grep -n '128' HEAD -- corpus/lessons/round-1.md` → `:30`, `:32` unchanged at `a6f9456` |
| D-18 | kumitate | `ops/registry-check.mjs` permanently red (7 `@role` errors); no mirror anywhere | 7,8,9 | OPEN — `grep -rn 'registry-check' kumitate-shokunin --include='*.md' \| wc -l` → 1, and that hit is this round's aggregator lesson |
| D-19 | kumitate | 6 committed notes + `lessons/round-6.md` cite `local://kumitate-r6-*` maps | 9 | OPEN — `read local://kumitate-r6-dispatch-ingress.md` → *Local file not found* |
| D-20 | kumitate | commits cited by subject/tag, not hash | 9 | PARTIAL at r10 → **re-test:** `2075363`'s message says "5 lesson rows re-pinned from 'commit round-N' to real shas"; corpus-wide sweep still needed at close |
| D-22 | external | membrane-seal launcher argv unparseable (`run-omp-native-trial.mjs:1931` vs `main.rs:95`) | 6,7,8,9 | OPEN — owner outside all provinces; kumitate carries the report |
| D-23 | external | judge `is_format_char` Cf-only vs producer Cf∪Mn∪Zs — real interop break | 6,7,8,9 | OPEN — same ownership |
| D-24 | kake | future-dated evidence label `~21:15Z` vs commit `9544914` @19:49:59Z | 8,9 | OPEN at `dd4eabf`; a **second** instance found → D-67 |
| D-25 | kake | "44 same-origin links, 0 real non-200" self-contradicted, no counting command | 8,9 | OPEN — `LOG.md:12`, `lessons/round-8.md:32`; the 74→75 sitemap errata did land |
| D-26 | kake | keeper-timer claim false at read time | 9 | OPEN — re-executed twice this round (scout + this lane): `systemctl --user is-enabled webzites-keeper.timer` → `disabled`, `is-active` → `inactive`, `journalctl --user -u webzites-keeper.service -n 3` → `-- No entries --`; the sentence is byte-identical at `18537e9` (r5) and `dd4eabf` → false at write time, not drifted |
| D-27 | kake | `/tmp` evidence pointers cited from committed files | 8,9 | OPEN and **escalated**: the round-10 axis artifact itself cites `/tmp/kake-r10/*` from committed `SCORECARD.md:24`, `LOG.md:15`, `lessons/round-10.md:4` and the r10 report → D-57 |
| D-29 | kotoba | falsified self-counts "22-row" / "12-item" | 9 | OPEN — re-counted: 22 table lines → **20 data rows** (`grep '^\|' \| tail -n +3 \| wc -l`); the dispatch checklist renders **9** `- [ ]` boxes while the corpus artifact lists 12 numbered items; standing at `SHONEN.md:6`, `SKILL.md:552`, `corpus/README.md:21` |
| D-35 | operator/scripts | `lane_prompt()` carries 1 of 5 child-lane contract items | 8,9 | OPEN — unchanged at `609ecb6` (no diff); the route-map half of the old claim is **fixed** (`m_lunamax`/`m_flash`/`m_zfl` = the MISSION bucket) |
| D-40 | protocol/operator | kama mint-or-reject unruled since round 2 | 2,8,10 | OPEN — L0 question filed by the protocol lane at r10 (`.ufo/l0-questions.md`, 3 entries at 21:57Z); §11.6 re-tests the bar and re-flags |
| D-42 | kengaku | flip/delta taxonomy sweep partially landed via a history rewrite | 9 | OPEN — 4 survivor spots (`corpus/README.md:22`, `lessons/round-5.md:8`, `SKILL.md:168,311`) |
| D-43 | operator | `.ufo` versioning split (state/log tracked-but-churning) | 6,8 | PARTIALLY LANDED — prompts now committed by the integrator, but 1 untracked again → D-79; state/log untracking still operator-side |
| D-46 | kumitate | `loop-driver.md:7,44-45` claims one `wait()` per subagent; `prompt.rs:1144-1164` drains all handles in one pass | 10 | OPEN at `a6f9456` |
| D-48 | protocol (self) | `PROTOCOL.md` 576–583 lines, ~29 inline incident refs, 17 duplicated rule pairs | 10 | OPEN — the lane's own round-11 planned move |
| D-49 | protocol (self) | stale-lane actuator wording corrected in `43342dd`, not amended | 10 | CLOSED-by-correction (accepted form; no orphaned cite) |

**C. New rows filed by this refresh (r6)**

| # | Owner | Defect | R | Status / required form | Proof |
|---|---|---|---|---|---|
| D-50 | kumitate | A lane committed in-place edits to **two aggregator-owned** lessons (`2075363`: `round-4-aggregator-audit.md` `execution_profile.rs:447`→`:448`; `round-5-aggregator-audit.md` `c5abaac` re-based) and swept a third, uncommitted one into `a6f9456` (72 lines of `round-6-aggregator-audit.md`) | 6 | **LANDED-as-violation.** Owner adjudication: both edits are factually correct and are **ratified** (`grep -n 'fn permits_advance' …/execution_profile.rs` → `:448`); the form breaks "no lane edits another lane's or the aggregator's corpus files" and "a lane never commits an aggregator-owned file". Required lane form: report the finding, let the owner correct its own file | `git -C kumitate-shokunin show --stat 2075363 -- corpus/lessons/round-4-aggregator-audit.md corpus/lessons/round-5-aggregator-audit.md`; `git -C kumitate-shokunin show --stat a6f9456` |
| D-51 | kumitate | Its own citation gate goes red on aggregator-owned lessons: `node scripts/cite-check.mjs` → `VERDICT: FAIL`, `CITE_CHECK: DRIFT (files=34 tokens=2148 errors=2 warnings=50)`, and **both** ERROR rows are inside `corpus/lessons/round-6-aggregator-audit.md` (`:23 LINE_OOR native_contract.rs:10896` — the parser joined two cells of one table row; `:36 UNRESOLVED corpus/lessons/round-9.md` — a quoted defect path resolved against the origin `src` root). Origin tree unchanged, so this is not source drift | 6 | OPEN — scope the glob to lane-authored files or exclude `corpus/lessons/round-*-aggregator-*.md`; the auditor-side half (do not put two files' line numbers in one table row) is adopted by this lane → §11.5 P-f | `cd kumitate-shokunin && node scripts/cite-check.mjs \| grep ERROR`; `git -C ~/Projects/origin-work/ufo-fsd-alpha rev-parse --short HEAD` → `ee907f1cf` |
| D-52 | kumitate | `corpus/knowledge/failure-telemetry.md:18` cites Rust `classify_failure`; the real symbol is `classify_failure_fields` (`native_text.rs:161`) and `SKILL.md:408` already says so — one repo, two answers | 4 | OPEN at `a6f9456` | `git grep -n 'classify_failure' HEAD -- corpus/knowledge/failure-telemetry.md` |
| D-53 | kasegi | stale falsified counts in append-only lessons: `lessons/round-5.md:16` "21 reports, every verdict BLOCKED" (live 22; 20 BLOCKED / 2 READY) and `lessons/round-9.md:33` histogram summing 282 | 9 | OPEN — appended correction entries (never a rewrite) | `ls ~/Projects/bounties/.ufo-mission-report-bh*.md \| wc -l` → 22 |
| D-54 | kasegi | `SKILL.md:323` names `claims/cantina-pendle/ingestion-20260915/` as the verification base for a six-file contract table whose `status.json` row asserts a `claim_review` block with `hard_gates` + subchecks — that package has **no** `claim_review` key (only a prose mention inside `resume_condition`); the block exists on `claims/bugcrowd-seek/honest-zero/status.json` | 1, 4 | OPEN — **5th refresh**; re-point the base or restate the row | `python3 -c "import json;print('claim_review' in json.load(open('claims/cantina-pendle/ingestion-20260915/status.json')))"` → `False` |
| D-55 | kasegi | `corpus/README.md` coverage map has no row for `knowledge/program-quirks.md` (19 rows / 20 files); the `README.md:30` lessons range also implies a non-existent `lessons/round-2.md` | 4 | OPEN | `comm -13 <(grep -oP 'knowledge/[a-z0-9-]+\.md' corpus/README.md \| sort -u) <(ls corpus/knowledge/*.md \| sed 's\|^corpus/\|\|' \| sort)` |
| D-56 | kasegi | `corpus/knowledge/evidence-dir.md:78` negative ("Zero claims dirs reference it") still carries no sweep inside the lane's own file — the command exists only in the aggregator's lesson | 4 | OPEN | `grep -rl 'george' claims/ \| wc -l` → 0 |
| D-57 | kasegi + kake | Axis-artifact evidence is session-scoped: kasegi `SCORECARD.md`'s depth pointer is `/tmp/kasegi-r12/reviewer.md`; kake's round-10 operability move is evidenced by `/tmp/kake-r10/*` cited from committed `SCORECARD.md:24`, `LOG.md:15`, `lessons/round-10.md:4` and the r10 report | 6 | OPEN — the closure rule forbids tmpfs pointers; append durable pointers (kake's two round-10 evidence reports already live in `~/Projects/webzites/reports/`) and label `/tmp` paths as session provenance | `grep -n '/tmp/' kasegi-shokunin/SCORECARD.md kake-shokunin/SCORECARD.md` |
| D-58 | fleet (6) | `SCORECARD.md` rows without `<counting command> @ <commit>`: 2 of 6 carry **no** commit hash at all, the rest carry 2–7 | 6 | OPEN — PROTOCOL's file-contract row already requires both; add it to the closure checklist (§11.5 P-h) | `for d in kasegi kengaku kake kumitate kotoba kagi; do grep -coE '\b[0-9a-f]{7,40}\b' $d-shokunin/SCORECARD.md; done` → kasegi 0, kengaku 7, kake 0, kumitate 4, kotoba 3, kagi 2 |
| D-59 | kumitate | `SCORECARD.md` calibrates against sibling numbers it did not re-derive: "kake (operability 6)" — kake's committed card says **8**; "kagi … `DRIFT_SELFTEST: PASS (11 cases)`" — kagi's says **13** | 6 | OPEN — a borrowed number carries its own re-run against the sibling's committed artifact | `grep -n operability kake-shokunin/SCORECARD.md; grep -n -i selftest kagi-shokunin/SCORECARD.md` |
| D-60 | kengaku | lessons index 6 rows vs 8 files at `f147a27` (both aggregator lessons unindexed); 10 rows vs 11 files on the live tree | 6 | PARTLY — the lane indexed its own r8/r9 lessons mid-round; the remaining orphan is this round's aggregator lesson | lesson `1bd17ec` §Post-audit re-measurement |
| D-61 | kengaku | round-8 work uncommitted, unlogged, unreported: `.ufo/reports/round-8/kengaku.md` is a 101-byte marker claiming "work pushed" while `?? corpus/evidence/` persists and `LOG.md` has no round-8/9 entry | 6 | OPEN — "landed means committed"; the marker claim is falsified by the repo's own status | `git -C kengaku-shokunin status --porcelain`; `grep -n 'round 8\|round 9' kengaku-shokunin/LOG.md` → 0 hits |
| D-62 | protocol | A **committed main-repo artifact** cites an orphaned hash: `.ufo/reports/round-8/protocol.md:16,120` and `round-9/protocol.md:35` name kengaku `48ecc88`, which is dangling (`merge-base --is-ancestor` exit 1; `fsck --lost-found` → dangling commit) | 6 | OPEN — the hash-ancestry rule needs a retroactive row for the integrator's own reports, not only lane reports | `git -C kengaku-shokunin fsck --lost-found \| grep 48ecc88` |
| D-63 | fleet | `[x]` verifier ids do not resolve: kagi marked all four boxes `[x]` naming `KagiR9Reviewer` (boxes 2 and 4 name no id at all); a whole-tree grep finds the string **only** on the line that names it. Per PROTOCOL a dispatched subagent *is* the lane, so all four count `[~]` | 6 | OPEN — propose the mechanical addition: `[x] <verifier-id>` requires the id to resolve to a committed report, transcript path, or ledger row (§11.5 P-j) | `grep -rn KagiR9Reviewer /home/vgpnk/projects/shokunin */ 2>/dev/null` → 1 hit, `kagi-shokunin/SHONEN.md:6` |
| D-64 | kagi | `corpus/lessons/round-9.md:175` + `LOG.md:215`: "the delivered/committed **445**-line revision is green" — the committed blob is **451** lines and no 445-line blob ever existed; `LOG.md:147` in the same repo says 451 | 6 | OPEN — appended correction (both files) | `wc -l kagi-shokunin/corpus/drift-pins.sh` → 451; `git -C kagi-shokunin log --all --oneline -- corpus/drift-pins.sh` → `e64e81b`, `5f55ba8` (30 lines) |
| D-65 | kagi | `SCORECARD.md:16` depth cell carries four falsified counts: 16-row decision table (15 at the measured commit `ea77bf0`, 16 at HEAD), 15-item checklist (13/14), 25 anti-pattern bullets (21/24), "`Source basis:` on every knowledge entry" (6/14 literal; 14/14 by substance) | 6 | OPEN — `SCORECARD.md` is mutable lane-owned: correct the cell in place **with the counting commands inline** + a `LOG.md` entry | lesson `ad694a2` citation row 18 |
| D-66 | kagi | hash-policy sentence says "6 private **0600** files" are pinned by mode+lines only; the baseline holds **7** mode-600 rows (the 7th, the musketeer `NativeMessagingHosts` manifest, *is* hashed). No secret material — but a reader can mis-infer that no 0600 file is hashed | 6 | OPEN — restate as a named-path list, not a mode class | `awk -F'\t' '$2=="600"' kagi-shokunin/corpus/drift-baseline.tsv \| wc -l` → 7 |
| D-67 | kake | **Second** future-dated evidence label: `~20:20Z` in `corpus/knowledge/sitemap-orphan-audit.md:3,62` + `lessons/round-7.md:4`, shipped in `83d08e4` at **19:39:21Z**; `/tmp/orphan-check.mjs` mtime 19:35Z bounds the real run | 6 | OPEN — appended entries with the real UTC run times | `git -C kake-shokunin log -1 --format='%ad' 83d08e4` |
| D-68 | kake | `corpus/knowledge/ops-automation.md:25` prints the identity `total - ok = violated+errors` with no command and no validity window; it is false on **11 of 76** history rows (rows 09-20T23:47:43→09-21T01:33) | 5 | OPEN — routed r5 as a minor, acknowledged in `lessons/round-10.md`, uncorrected at `dd4eabf` | per-row sum over `~/Projects/webzites/state/probe-history.jsonl` |
| D-69 | kake | `corpus/knowledge/ghp-subpath-spotcheck.md:3` names no artifact at all for its 2 352-path round-6 baseline; and the round-10 report cites no commit hash (subject only) | 6 | OPEN | `grep -n 'baseline audit' kake-shokunin/corpus/knowledge/ghp-subpath-spotcheck.md` |
| D-70 | kotoba | 8 unresolvable `commit round-N` citations (`corpus/lessons/round-{1,4,5,6,7}.md:3`, `corpus/README.md:23,24,25`); **3 sites newly added in r9** | 4 | OPEN — appended correction listing the real hashes (r1 `1d93182`, r3 `229b687`, r4 `397b29c`, r5 `4002b9f`, r6 `a614927`, r7 `3b029b8`) | `git -C kotoba-shokunin rev-parse --verify round-5` → `fatal: Needed a single revision` |
| D-71 | kotoba | inherited mechanism claim falsified and still unnamed: `corpus/knowledge/skill-activation-telemetry.md:29-30` "compression is a *model call* (rewrites, not truncates)" vs the lane's own round-7 cache-or-truncate proof; only the render-size half was annotated | 5 | OPEN — appended correction pointing at `knowledge/render-mechanism-round7.md` | `grep -n 'model call' kotoba-shokunin/corpus/knowledge/skill-activation-telemetry.md` |
| D-72 | kotoba | minors: `SHONEN.md` lacks a trailing newline; `corpus/README.md` CLAUDE.md row says "16-file census" vs live **18**; the r9 report says the prompt population "grew to 50" vs **53**; `lessons/round-{1,3,4}.md` unindexed | 6 | OPEN | `find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*' \| wc -l` → 18; `ls .ufo/prompts/*-round-*.md \| wc -l` → 53 |
| D-73 | protocol | The lane-identity invariant's parenthetical "kagi/kake/kumitate/kengaku already do" is **false for all four**: kagi/kumitate/kengaku have zero lane-identity commits and no local config; kake has exactly one (`83d08e4`) under `kake-shokunin <kake-shokunin@local>` — right name, non-conforming email. Only **kotoba** conforms, the repo the sentence names as the violator | 6 | OPEN — correct the sentence; the round-10 measurement beside it (0 of 60 reports lane-committed) is accurate | `for d in kasegi kengaku kake kumitate kotoba kagi; do git -C $d-shokunin log --format='%an <%ae>' \| sort \| uniq -c; git -C $d-shokunin config --local user.email; done` |
| D-74 | protocol | Prompt-fidelity counts are HEAD-stamped and already stale in three successive values (36/40 → 45/41 & 0/46 → 0/58). At main HEAD `8ec7a56`: **45 of 50** child reports missing the `SHONEN` heading, **0 of 62** prompts carry the rule; the `58` denominator fails its own mtime reconstruction (54 prompt files existed at 17:51:04) | 6 | OPEN — stamp such counts with the commit they were measured at | `ls .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l` → 50; `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l` → 45 |
| D-75 | protocol | Three statements are now history-only and must be re-stamped: (a) "Rounds 2–10 closed with zero closure artifacts (`rounds` stuck at `[0,1,1.5]`)" — 15 entries at `640a4c5` covering rounds 0–11; (b) the drift-pin clause's "round-8 audit found kagi's pins verifiable for only 2 of 13 files" — closed by D-10; (c) the `SHONEN.md` file-contract row's "kagi 4 bare `[x]`, kotoba per-box prose blocks" — both regenerated, only kengaku's 3-box stands | 6 | OPEN | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"` → 15 |
| D-76 | fleet | The r10 contested-scope rulings owe a `PROVINCE.md` record in kumitate (`agent.db`), kake + kagi (CDP lease halves), kasegi + kumitate (`registry.json` split). kagi's `PROVINCE.md` is modified in its live round-10 tree — verify at close | 10 | OPEN — re-flagged; the integrator cannot edit child files | `git -C kagi-shokunin status --porcelain -- PROVINCE.md` → ` M` at 21:57Z |
| D-77 | protocol + aggregator | One root `SCORECARD.md` path serves two main-repo lanes; the protocol lane's version states the aggregator's axes "are not scored here", and both lanes respawn independently | 6 | OPEN — ruling owed: per-lane sections with an ownership line (this refresh's choice: appended without touching a protocol byte) or per-lane filenames (§11.5 P-i) | `head -7 SCORECARD.md` |
| D-78 | operator/protocol | `MISSION.md` assigns `novelty` (kengaku) and `consistency` (kotoba); neither is among AXES.md's six axes (`grep -n novelty AXES.md` → exit 1). kotoba already scores `consistency` 5→7; kengaku's r9 evidence file calls itself "(novelty axis)". A score for an undefined axis is not re-derivable by a non-author | 6 | OPEN — both files are operator-side; the protocol lane names the correction, the operator rules. L0 line appended this round | `grep -n 'novelty\|consistency' AXES.md MISSION.md` |
| D-79 | operator | `.ufo/prompts/` untracked again: 1 file at 21:57Z after `640a4c5` committed 8 (`6deaeaa` then committed the round-9 kumitate prompt) — the driver keeps generating between integrator commits | 10 | OPEN | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` → 1 |
| D-80 | aggregator | **Withdrawn charge:** round-5 kotoba minor 4 ("source char counts false at write time: claimed 820/681/660/578/436 vs observed 836/702/672/599/444") does **not** reproduce — whitespace-collapsed `description:` lengths reproduce the lane's values exactly. The offset was the auditor's raw-YAML boundary artifact | 6 | CLOSED by withdrawal; recorded in lesson `778310d` so the lane can stop carrying it | kotoba lesson §Re-executed citations, correction note |
| D-81 | aggregator | The round-5 kagi ref-shape falsification sweep returned 0 lines then and **1** now (`corpus/transcript-scan.sh:242` — a synthetic two-segment marker in the gate's scratch-CDB `--selftest` seed; non-material, no vault identifiers) | 6 | OPEN — append-only annotation owed in `kagi-shokunin/corpus/lessons/round-5-aggregator-audit.md` | sentinel sweep S1/S4 + kagi lesson defect 9 |
| D-82 | fleet (watch) | Three lanes independently built the same artifact class in one round: kumitate `scripts/cite-check.mjs` (citation re-verifier, `--selftest` 28/28), kagi `corpus/drift-pins.sh` (drift gate, 13-case selftest), kake `scripts/probe-delta.mjs` (delta detector, exits 0/2/64). Each was absorbed by its province → **no mint**, but this is the third verification-tooling demand instance and kessho's written trigger ("a lane reports verification work no province can own") is close to being met | 6 | WATCH — mint trigger not met; re-test when a fourth lane builds one or a lane refuses the work | the three committed artifacts + §11.6 |
| D-83 | kagi + protocol | A lane's main-repo commit swept this lane's **staged** ledger rename: `git log --oneline -1 -- .ufo/reports/AGGREGATE.md` → `ade32e4` "round-10 kagi report: coverage axis-move", which also carries the `round-2/AGGREGATE.md` deletion. PROTOCOL.md requires a lane's main-repo commit to be pathspec-limited to its own report (`git commit -- .ufo/reports/round-<N>/<id>.md`), never `commit -a`/`add -A`; a bare `git commit` consumes whatever is staged in the shared index. Outcome benign (the relocation this refresh owed landed), attribution wrong, hazard structural: eight lanes share one index | 6 | OPEN — protocol to tighten the clause (a lane main-repo commit carrying a non-report path is a conformance defect even when the index was dirty on arrival); aggregator-side fix adopted: leave nothing staged between commands, `git commit -- <paths>` immediately after writing |

### 11.3 §10.1 round-4 verdicts superseded (movement in both directions)

| Repo | Refresh 3 (r4) | Refresh 4 (r6) | What moved |
|---|---|---|---|
| kengaku | conformant | **not conformant** | Degraded: rule 9 (`LOG.md:9` rewritten in place by the r7 amendment), rule 7 (index 6 rows / 8 files), rule 4 (`0/12 PASSes` on a 25-draw probe whose own table says 17). Its r4 strength (21/21 citations) still holds — 13/13 sampled this round |
| kumitate | conformant (r4 delta) | **not conformant** | Degraded: rule 6 (`gate.rs:11` in three files, actual `:15` — landed fixed at `2075363`), rule 4 (charter-scribe 5→6, script layer 41→42, 68/105/211 commandless), rule 2 (`local://` pointers unreadable), rule 9 (D-50) |
| kagi | conformant | **not conformant** | One rule-4 count (445 vs 451) + four falsified SCORECARD counts. Its r9 axis-move is nonetheless the strongest independently reproduced artifact in the fleet this round (drift gate: clean run, 13-case selftest, proven detection on a falsified baseline) |
| kasegi | not conformant (2 majors) | **not conformant (7)** | Grew: the r12 in-place number repairs fixed SKILL/README values but left 4 "19" sites, 2 stale lesson counts, the Pendle attribution (5th refresh), the missing index row and the unswept negative. The in-place repair *form* is contested under rule 9 — see §11.5 P-l |
| kake | not conformant at that commit (fixed r5) | **not conformant (5)** | Grew: keeper-timer claim (5 rounds), a second future-dated label, the `total-ok` identity false on 11/76 rows, `/tmp` evidence promoted into a committed axis artifact, a sourceless 2 352-path baseline |
| kotoba | not conformant (3 majors) | **not conformant (5)** | Two of the three r4 majors were repaired at `4002b9f`; the r9 additions are the two falsified self-counts (now inside a committed `SHONEN.md` evidence line), 3 new unresolvable `commit round-N` cites, and the uncorrected mechanism claim. One r5 charge against it is **withdrawn** (D-80) |

### 11.4 §10.4 promotion inputs superseded (non-author review; `SHONEN.md` files untouched — outside aggregator write scope)

Box order: (1) decision tables/error patterns/checklists/cited sources; (2) ≥1 logged end-to-end domain task; (3) executable without oral context; (4) no cross-domain bleed.

| Repo | 1 | 2 | 3 | 4 | Ruling at refresh 4 |
|---|---|---|---|---|---|
| kagi | `[~]` 18/18 sampled citations reproduce, but one falsified count ships in the same commit (D-64) and four in its SCORECARD (D-65) | `[x]` r9 drift gate is an executed end-to-end task with a **proven negative** (falsified baseline → DRIFT, exit 1) | `[~]` a lane-dispatched reviewer reproduced ~15 probes — a subagent is still the lane | `[x]` CDP lease reported, not absorbed (r3/r7/r9/r10) | **Closest to ready.** Blocked on box 3 and on D-63 (its four `[x]` name a verifier id that resolves nowhere) |
| kake | `[~]` parity arithmetic reproduces exactly (93 locs → 19/74); 5 majors open | `[x]` probe→correction→handoff cycle under the operator-gated reading | `[~]` | `[x]` | Not ready — D-26 uncorrected for 5 rounds is a calibration failure, not a coverage gap |
| kengaku | `[x]` 13/13 sampled citations reproduce | `[x]` r4 eval slice + r5 33-task battery | `[ ]` **the box does not exist in its `SHONEN.md`** (3-box file, D-15) | `[x]` | Not ready — stale seed + the append-only violation (D-13) + rounds 8–9 unlanded (D-61) |
| kasegi | `[~]` most numbers reproduce exactly (1088/486/592/703/584/903/198/3361); 7 majors open | `[ ]` still no executed or handed-off claim task | `[~]` | `[x]` | Not ready |
| kumitate | `[~]` mechanisms verified at symbol level; `128` (D-17) and `classify_failure` (D-52) contradictions uncorrected | `[~]→[x]` **first candidate this round**: `scripts/cite-check.mjs` is a runnable artifact with `--selftest` 28/28 and a real repair (22 citation errors → 0 claimed; the tool now reports 2, both from this ledger's own lesson, D-51) | `[~]` | `[x]` two ufo-fsd-alpha findings reported, not absorbed | Not ready until D-17/D-52 land, but box 2 is met for the first time — refresh 3 recorded it `[ ]` (read-only archaeology) |
| kotoba | `[~]` the falsified counts sit inside its own `SHONEN.md` evidence line | `[x]` r5 fleet audit + r7 dispatch-prompt audit, both re-verified this round | `[~]` a blank-context L2 ran the checklist — still the lane | `[x]` cross-domain prompt/agent defects reported, not fixed | Not ready — D-29 |

Fleet-wide gate observation: **no repo has a single `[x]` on box 3 from a named non-author verifier.** Every box-3 claim in the fleet rests on a lane-dispatched subagent, which PROTOCOL.md counts as the lane. Refresh 3's "promotion-ready pending box-3" rulings for kengaku/kagi/kake therefore stand, and the only way to close box 3 is a cross-lane or integrator execution walkthrough — which is exactly what this refresh did for six repos' *corpora* but not for their *instructions*. Proposed as the round-7 aggregator move candidate (§11.8).

### 11.5 Fleet patterns → protocol/CORPUS proposals (integrator lands; aggregator cannot)

- **P-f — a verifier tool must scope to lane-authored files.** D-51: kumitate's gate reports `errors=2` and both rows are inside an aggregator lesson (a markdown table row joined two files' line numbers; a quoted defect path resolved against the origin `src` root). Generalizes: any lane that gates on "every corpus citation resolves" goes red the moment an auditor quotes a defect into the same tree. Fix both sides — lanes exclude `corpus/lessons/round-*-aggregator-*.md` (or gate lane-authored paths only); auditors do not put two files' line numbers in one table row (adopted here: this ledger's proof cells name one file per command).
- **P-g — an uncommitted or merely *staged* aggregator-owned file is a hazard, not a neutral state.** PROTOCOL.md already forbids a lane committing one; the enforcement that actually works is the owner committing at creation, and in a shared index even `git mv` is unsafe. This round produced both failure modes: six lessons left uncommitted until one was swept by a lane commit (D-50, `a6f9456` at 18:40:18 vs the owner's commit at 21:52Z), and a staged ledger rename consumed by another lane's bare `git commit` (D-83, `ade32e4`). Proposed clause: the aggregator's refresh states each artifact's **commit latency** and names any lane commit that touched an aggregator path; a lane that finds an untracked or staged `round-*-aggregator-*` / ledger change records it and leaves it; a lane main-repo commit carrying any non-report path is a conformance defect.
- **P-h — axis scores inherit the count rule, and need a check, not just a rule.** PROTOCOL.md's `SCORECARD.md` row already requires "the counting command that produced it and the commit it was measured against"; 2 of 6 committed cards carry no commit hash at all (D-58) and three carry falsified numbers (D-59, D-65, D-29). Proposed: add to the integrator's closure checklist *"a score row without `<command> @ <commit>` is an opinion, recorded as a conformance defect"* — the same treatment the `SHONEN` heading gets.
- **P-i — one root `SCORECARD.md` for two main-repo lanes is a collision** (D-77). The protocol lane's card says the aggregator's axes "are not scored here"; both lanes respawn independently against the same path. This refresh appends an aggregator section without altering a protocol byte, which works only while lanes append. Ruling owed: per-lane sections with an ownership line each, or per-lane filenames (`SCORECARD-<lane>.md`) with the file-contract row updated.
- **P-j — `[x] <verifier-id>` must resolve** (D-63). kagi's four `[x]` name `KagiR9Reviewer`, which exists nowhere but the line naming it. Proposed mechanical addition to the `SHONEN.md` contract: the id resolves to a committed report, transcript path, or ledger row, else the mark counts `[~]`.
- **P-k — HEAD-stamped counts.** Three successive values of the same prompt-fidelity measurement now sit in PROTOCOL.md (D-74). Proposed: any fleet count in an integrator file carries `@ <commit>` so a reader can tell a stale number from a false one.
- **P-l — in-place number repairs in mutable files vs rule 9.** kasegi's r12 fixed falsified counts by editing `SKILL.md` + 5 corpus entries in place, each marked "round-12 correction/addition" (`corpus/README.md:82`). CORPUS.md rule 9 says corrections are new entries; PROTOCOL.md's sweep-every-mention rule says a corrected fact left standing in a sibling file is still a defect; the append-only clause covers `LOG.md` and `lessons/`. Proposed clarification: **`knowledge/` entries are mutable-with-an-inline-correction-mark; `lessons/` and `LOG.md` are append-only.** Without it, lanes that obey the sweep rule look like they broke rule 9 (kasegi) and lanes that obey rule 9 look like they skipped the sweep (kengaku D-13).
- **P-m — a marker report must not advance a lane counter.** Already landed by the protocol lane at r10; recorded here because this lane's own round-5 file is one of the four markers graded (`.ufo/reports/round-5/aggregator.md`, 254 B) and because the aggregator round counter therefore skipped a refresh generation (D-33).

### 11.6 Mint / dormancy calls (aggregator axis)

**Mint — no mint this round; one ruling still owed.**

- **kama** (local model serving & endpoint health): refresh 3 ruled it meets the written bar (two documented demand instances — kagi r3, kengaku r4; no province owns the surface; both discoverers declined the fix as operator-owned). Re-tested: `MANIFEST.json` `minted` is `[]` in all 15 `rounds` entries (`python3 -c "import json;print([r.get('minted') for r in json.load(open('MANIFEST.json'))['rounds']])"`), and the protocol lane filed the L0 question at r10 (`.ufo/l0-questions.md`, entry 2 of 3 at 21:57Z, recommending mint). **Aggregator position unchanged: mint-eligible.** The operator-side fix (qwen-local 8080→34113 + `op signin`) is independent of the decision; r10 records the repoint as landed-serving, the `op signin` half unverifiable.
- **kessho** (CI/verification harnesses): below the bar, but the gap narrowed — D-82 is the third independent verification-tooling instance in one round, all three absorbed by their provinces. Trigger restated: a lane reports verification work no province can own, or refuses it.
- **umihotaru / kagemusha**: unchanged, no new instance.
- **New candidate surfaced this round, ruled below the bar:** *axis-framework stewardship* (SCORECARD templates, per-axis proxies, rollout order — the `planner` L2's output). It is protocol+aggregator work, not a domain: the template proposal routes to the protocol lane (§11.5 P-h/P-i) and the per-repo cards are lane work. No mint.

**Dormancy — no lane dormant.** Rule: no `LOG.md` activity across two consecutive rounds the lane was dispatched *and* reported in. Evidence: `grep -oE 'round[- ](0\|[1-9][0-9]?)' <repo>/LOG.md | sort -u -V` → kasegi …round-12, kagi …round-9, kake …round-10, kotoba …round-9, kengaku …round-7 committed (r8/r9 in flight, D-61), kumitate …round-8 in flight; `git -C <repo> log -1 --format='%ar'` → all six committed within the last two hours. The only dormancy-adjacent subject is **this lane**: round 5 filed a 254-byte marker and no refresh (§11.7 self-defect 2). Recorded here rather than in the round notes because the integrator flags dormancy and the aggregator's own absence is the aggregator's to file.

### 11.7 Aggregator self-defects (filed against this lane)

1. **Lesson files left uncommitted in live lanes' trees** — root cause of D-50. kumitate's `a6f9456` swept 72 lines of `round-6-aggregator-audit.md` into a lane commit at 18:40:18, ~3 h before its owner committed. Same class as the round-9 finding ("aggregator mirrors sat uncommitted in kake/kumitate/kagi; kasegi swept one into `c80c2a1`"). Practice fixed this round (commit at creation, pathspec-limited, `-c user.name=aggregator-shokunin -c user.email=aggregator@shokunin.local`); proposed check P-g.
2. **Two-round refresh gap.** Refresh 3 was written at aggregator round 4; round 5 produced a marker and no refresh, so 41 lane reports accumulated (`ls .ufo/reports/round-{5,6,7,8,9,10,11,12}/*.md | wc -l` → 41 at 21:57Z) with the durable queue empty on disk (`grep -c routed .ufo/reports/round-2/AGGREGATE.md` → 0). PROTOCOL.md's consequence clause describes exactly this: "a round filed without the ledger duty keeps the routed-defect queue empty by construction". Discharged by §11.2.
3. **A round-5 charge against kotoba was wrong** — withdrawn (D-80). Filed here because a false auditor claim costs the audited lane a repair cycle it does not owe.
4. **A round-5 sweep result against kagi is stale** — 0 lines then, 1 now, non-material (D-81); the annotation is owed in the round-5 lesson, append-only.
5. **Ledger left at the non-canonical path for two refreshes** — §10.6 called relocation "integrator action"; the round-9 clause assigns it to the aggregator's next refresh. Discharged.
6. **This lane had no main-repo `LOG.md`/`SCORECARD.md` before round 6** — both were created by the protocol lane at r10 (`640a4c5`), which also had to state that the aggregator's axes were unscored. The aggregator's first entries are this round's; the collision it created is D-77.
7. **Round-3 write-scope violation adjudicated at r10** (`6565e89` touched `CORPUS.md` + nine prompts): accepted as a historical conformance defect, no rewrite. Its content was ratified; the scope rule is now explicit and this round's main-repo writes are limited to the ledger, this lane's report, and the two root files PROTOCOL.md now assigns to main-repo lanes.
8. **A staged rename left in the shared main-repo index.** `git mv` of the ledger staged the
   relocation and the kagi lane's bare `git commit` consumed it (`ade32e4`, D-83). Same hazard
   class as self-defect 1, different mechanism: where eight lanes commit concurrently into one
   index, *staged* is as exposed as *untracked*. Practice fixed this round — write, then
   `git commit -- <paths>` in one step, leaving nothing staged between commands.

### 11.8 Fleet-2 axis-framework census (measured twice — the fleet moved mid-round)

| Metric | Command | 18:02 -03 (main HEAD `0a30b44`) | 21:57Z (main HEAD `8ec7a56`) |
|---|---|---|---|
| child repos with a **committed** `SCORECARD.md` | `for d in kasegi kengaku kake kumitate kotoba kagi; do git -C $d-shokunin ls-files SCORECARD.md \| wc -l; done` | **0 / 6** | **6 / 6** |
| …of which carry ≥1 commit hash | `grep -coE '\b[0-9a-f]{7,40}\b' <repo>/SCORECARD.md` | n/a (none committed) | 4 / 6 (kasegi 0, kake 0) |
| committed round-6 aggregator lessons | `git -C <repo> ls-files corpus/lessons/round-6-aggregator-audit.md \| wc -l` | 0 / 6 | **6 / 6** |
| canonical ledger present | `test -f .ufo/reports/AGGREGATE.md && echo 1 \|\| echo 0` | 0 | **1** |
| durable routed-defect rows in the ledger | `grep -cE '^\| D-' .ufo/reports/AGGREGATE.md` (count the `D-` keyed rows of §11.2) | **0** | **79** distinct keys `D-01…D-83` = 45 carried from the r10 queue (D-34/D-38 dropped as closed-at-r10; D-36/D-37 folded into the D-31 rulings row) + 34 new |
| lane reports in the sweep window | `ls .ufo/reports/round-{5,6,7,8,9,10,11,12}/*.md \| wc -l` | 33 | 41 — all swept (six scouts per lane + this lane read `round-9/protocol.md` and `round-10/protocol.md` §Routing/§Rulings) |
| conforming `SHONEN.md` seeds | reviewer L2 `diff` vs the regenerated canonical seed | 3 pristine (kasegi, kake, kumitate) + kagi conforming-with-marks | 3 pristine + kagi + kotoba conforming in form; **kengaku non-conforming (3 boxes)** |
| lane-identity commits | `git -C <repo> log --format='%an <%ae>' \| sort \| uniq -c` | 0 / 6 repos canonical | 1 / 6 (kotoba) + kake's single name-conforming/email-variant commit |

The 0/6 → 6/6 `SCORECARD.md` landing is **lane work, not this lane's axis-move**: five lanes created and committed their cards inside this round's window (kake `dd4eabf`, kotoba `e997d45`, kagi `e64e81b`, kumitate `2075363`, kasegi and kengaku during their live rounds). It is recorded because a census that hides sibling motion is unfalsifiable, and because the honest before→after for *this* lane's move is the ledger/queue/lesson column set.

**Round-7 aggregator move candidate** (lowest axis after this refresh: mint/dormancy calls at 6 — see `SCORECARD.md` §Planned): a standing, re-runnable mint/dormancy assessment table in this ledger — one row per rostered lane (last dispatched round, last reported round, last `LOG.md` round token, last commit age, verdict + command) and one per watchlist candidate (demand instances with pointers, owning-province test, bar verdict), re-tested each refresh, with the operator-gated kama half recorded as **blocked-external** against its L0 pointer instead of silently re-flagged. Queued behind it, and the highest-value cross-lane-quality move available: a **box-3 execution walkthrough** — one non-author agent per repo runs `SKILL.md`/`corpus/` with no oral context and records where it stalls, the only measurement that can turn the fleet-wide `[~]` on box 3 into an `[x]` (§11.4). Falsifiable target: 6/6 repos with a named non-author box-3 verdict, committed in the repo.
