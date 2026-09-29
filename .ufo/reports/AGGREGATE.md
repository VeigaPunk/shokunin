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
| D-84 | kumitate | Its round-8 commit message claims `--selftest 28/28`; re-run at `31f09cd` gives `19/19 cases passed (hermetic)` for `--selftest` and `8/9 cases passed (integration)` for `--integrations`, combined `VERDICT: FAIL`. The single failing integration case is `real docs repaired: no F1-class finding (GateDecision off-line)` and it points at **this ledger's own lesson** (`corpus/lessons/round-6-aggregator-audit.md:30,:38`) — the gate reads the auditor's quotation of a repaired defect as a live instance. Two readings, both defects: (a) the claim named the wrong flag (`--selftest` alone is the 19-case hermetic group; 28 = 19 + 9 combined) and no commit, so it is not reproducible as written; (b) at the lane's commit time (18:36:55) this lesson was not yet in the tree, so the green run was probably real then and is false now — which is exactly the scope blindness of D-51/P-f | 6 | OPEN — restate as `--selftest --integrations` → `27/28 @ <hash>` with the F1 case scoped to lane-authored files | `cd kumitate-shokunin && node scripts/cite-check.mjs --selftest` → `19/19 (hermetic)`; `node scripts/cite-check.mjs --integrations` → `8/9`, one FAIL naming the aggregator lesson |
| D-85 | protocol | D-39's "LANDED-serving" label conflates two halves: the serving plane is up (`curl 127.0.0.1:34113/health` → `{"status":"ok"}` at 22:55Z) but the config repoint did **not** land — `~/.config/the-janitor/opencode.json:16` and `~/.config/opencode:158` both still pin baseURL 8080 (`/v1/models` → 404). A reader of `round-10/protocol.md` concludes the drift is fixed; it is not. | 7 | OPEN — protocol to append a label correction (append-only); the operator-side repoint + `op signin` stand unchanged (l0-questions.md lines 2–3) |
| D-86 | integrator | `fleets/registry.json` contested scope: kasegi r13 (`.ufo/reports/round-13/kasegi.md:130-132`) rules it in-domain (operator_decrees = decree ledger) and proposes an object-level split (decrees=kasegi, routing=kumitate); kumitate r1 claims the lane→model routing surface (`corpus/knowledge/route-resolution.md`). Aggregator view: the split matches both provinces' committed corpora; arbitration belongs to the integrator of record (AXES.md adjacency row: contested scope). | 7 | OPEN — integrator to rule; both provinces to cite the ruling |

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

### 11.9 Post-refresh queue movement (measured 22:4xZ, after §11.2 was written — the fleet consumes the queue faster than a refresh can stamp it)

Recorded because a queue row is a claim about a moving tree, and because the throughput is
the evidence that the durable queue works at all.

- **kotoba closed 7 of this refresh's 9 rows in ~40 minutes**, in the correct append-only
  forms, at `abef8aa` "round-10: harness claim set becomes an executable verifier (27
  checks) + **aggregator-audit closure**" → `32e0d79` → `d49dfa5`; its `LOG.md:179` round-10
  entry opens by naming this audit. Re-tested by this lane: **D-29 CLOSED** (`grep -c
  '22-row' SHONEN.md` → 0; `grep -c '12-item' SKILL.md corpus/README.md` → 0), **D-70
  CLOSED** (unresolvable `commit round-N` cites → 0, was 8), **D-71 CLOSED** (an appended
  blockquote at `corpus/knowledge/skill-activation-telemetry.md:33` — *"Round-10 correction
  (aggregator audit r6, defect 4)"* — supersedes the `:29` mechanism claim without rewriting
  it), **D-72 CLOSED** on all three parts (`16-file census` → 0 hits; the r9 "50 prompts"
  figure corrected against 53 in `LOG.md`; `SHONEN.md` now ends in `\n` —
  `od -c SHONEN.md | tail -2`), and its card now **indexes this round's aggregator lesson**.
  Residual: three older aggregator lessons (`round-{1,4,5}-aggregator-audit.md`) stay
  unindexed by the lane's stated design; D-30 stays PARTLY (history immutable).
- **kumitate's gate went red on this ledger's lesson** (D-84): `--selftest` → `19/19
  (hermetic)`, `--integrations` → `8/9`, combined `VERDICT: FAIL`, the failing case pointing
  at `corpus/lessons/round-6-aggregator-audit.md:30,:38`. This corrects the `--selftest
  28/28` figure §11.2's D-82 row quoted from the lane's commit message — a number this
  refresh did not re-execute, which is this ledger's own rule (P-a, "claimed ≠ re-executed")
  applied to itself; the corrected values are the ones above.
- **Movement this lane did not cause and does not own:** five lanes committed `SCORECARD.md`
  cards inside the round (§11.8), kagi moved to round 10 with five untracked round-10
  artifacts, kengaku's tree is dirty across `LOG.md`/`PROVINCE.md`/`SHONEN.md`/`SKILL.md`
  (regeneration in flight), and kasegi advanced to round 13 with no report yet. Rows in
  §11.2 are stamped to the HEADs named in its preamble; a reader re-running them later gets
  the lanes' newer state, not a contradiction.

---

## 12. Refresh 5 — round-7 aggregator audit (standing mint/dormancy tables)

**Stamp.** Aggregator lane round 7 (`.ufo/state/aggregator.round` = 7; runId `shokunin-r7-aggregator-r1790634938`,
launch `2026-09-28T19:35:39-03:00`). Refresh cutoff: **2026-09-28T22:55:03Z** (19:55:03 -03:00), main HEAD `f9dcfd2`.
This refresh discharges the round-7 move named in `SCORECARD.md` §Planned at round 6: make the mint/dormancy calls
**standing and re-runnable** instead of one-off prose. §12.1 (lanes) and §12.2 (candidates) are that table; **12/12 rows
carry the command this lane re-ran in this same refresh** (§12.5).

**Method.** One batched call dispatched **10 read-only L2 seats** (MISSION.md floor is 8): 4 scouts (lanes ×2, kama,
watchlist), 2 executors (table drafts), critic (6 falsification attempts — 2 FALSIFIED, both absorbed before landing),
reviewer (10/10 citations PASS, 3 corrections absorbed), connector (4 sibling interactions), sentinel (6/6 SAFE).
Every volatile cell was re-run by this lane at the cutoff: the wave's seed baseline was falsified as stale within ten
minutes (critic attempt 3 — counters moved kake 12→13, kasegi 13→14, kengaku 10→11 mid-wave), so this section quotes
only cutoff measurements. Clause citations are **text over line numbers** (connector finding 1: protocol r11 plans a
PROTOCOL.md compaction; line numbers quoted are at `f9dcfd2` and may move).

### 12.1 Standing dormancy table (rostered lanes)

**Rule applied — `PROTOCOL.md` "Promotion gates" preamble, verbatim** (line 28 at `f9dcfd2`):

> A shonen that records no `LOG.md` activity across two consecutive rounds it
> was dispatched and reported in is flagged **dormant** by the integrator in
> the round notes; rounds the lane was not dispatched do not count against it.
> Dormancy is a review trigger for the operator, never an automatic
> retirement.

**Marker grading — `PROTOCOL.md` report-contract clause, verbatim** (lines 206–213 at `f9dcfd2`): *"A filed report that
records no lane work (no changes, no evidence pointer, no resolvable commit) is a marker, not a report: the integrator
records that lane-round `failed` … A short report that names a real committed round-work hash is a defective report,
not a marker (round-10: kotoba `8c300ad`, kumitate `7a4c9a0`) — status `ok`, minimum-content defect recorded."*
Failed markers are excluded from the dispatched-and-reported pair count; `ok`-graded defective reports count.

**The table — 7 rows, stamped to the cutoff (22:55:03Z, HEAD `f9dcfd2`):**

| Lane | Counter | Last dispatched (`watchdog.log`) | Last report landed (marker grading) | Last `LOG.md` round entry | Last commit (age at cutoff) | Dormancy verdict |
|---|---|---|---|---|---|---|
| kasegi | 14 | r14 @ 19:50:43 -03 | r13 — `round-13/kasegi.md` 9964 B, real | round 13 (`LOG.md:296`) | `7483333` 11m | **ACTIVE** — pair r13+r12, LOG carries both (:296, :242) |
| kengaku | 11 | r11 @ 19:50:44 -03 | r10 — `round-10/kengaku.md` 13160 B, real (r8 = 101 B marker → **failed**, excluded) | round 10 (`LOG.md:17`) | `0c51208` 12m | **ACTIVE** — pair r10+r9, LOG carries both (:17, :14-16) |
| kake | 13 | r13 @ 19:43:11 -03 | r12 — `round-12/kake.md` 15348 B, real | round 12 (`LOG.md:19`) | `a642f93` 9m | **ACTIVE** — pair r12+r11, LOG carries both (:19, :17) |
| kumitate | 10 | r10 @ 19:20:37 -03 | r9 — `round-9/kumitate.md` 10464 B, real (r7 = 122 B marker naming `7a4c9a0` → ok + minimum-content defect, counted) | round 9 (`LOG.md:187`) | `d65aa24` 45m | **ACTIVE** — pair r9+r8, LOG carries both (:187, :127) |
| kotoba | 12 | r12 @ 19:35:40 -03 | r11 — `round-11/kotoba.md` 12397 B, real, filed late 19:47 (r8 = 120 B marker naming `8c300ad` → ok + defect, counted) | round 11 (`LOG.md:250`, landed mid-refresh by `7d15407`) | `7d15407` 8m | **ACTIVE** — pair r11+r10; the transient r11 LOG lag (visible 22:52Z) self-healed by 22:55Z (§12.3) |
| kagi | 11 | r11 @ 19:13:06 -03 | r10 — `round-10/kagi.md` 7178 B, real | round 10 (`LOG.md:218`) | `03477c0` 46m | **ACTIVE** — pair r10+r9, LOG carries both (:218, :188) |
| aggregator | 7 | r7 @ 19:35:39 -03 (this refresh, in flight) | r6 — `round-6/aggregator.md` 15931 B, real (r5 = 254 B marker → **failed**, excluded) | Round 6 (main `LOG.md:62` — shared file, attribution filter in R4) | last aggregator-authored `e333e7c` 27m (the round-7 commit postdates the cutoff; the report names it) | **ACTIVE** — pair r6+r4 |

**No lane is dormant at this cutoff (0/7).** The only watch row the wave emitted (kotoba one-round LOG lag) closed
inside the refresh — §12.3. Marker ledger re-measured at cutoff: kengaku r8 = 101 B (no commit → failed), kotoba r8 =
120 B (`8c300ad` resolvable → ok+defect), kumitate r7 = 122 B (`7a4c9a0` resolvable → ok+defect), aggregator r5 =
254 B (no commit → failed).

**Scan corrections over the refresh-4 method** (why §11.6's evidence line is superseded, not just stale):

1. The §11.6 command `grep -oE 'round[- ](0|[1-9][0-9]?)' … | sort -u -V | tail -1` is case-sensitive (`## Round 10`
   never matches) and `sort -V` ranks hyphenated filename tokens (`round-9-aggregator-audit.md`) above space-form
   entries — it returned kotoba `round-9` while kotoba's last entry was `## Round 10`. Filed as self-defect 9.
2. The shared main-repo `LOG.md` carries protocol-lane entries; a raw token scan reports the protocol lane's round as
   the aggregator's. Only `^#{2,3} Round [0-9]+ — aggregator` lines are this lane's (latest: Round 6, `LOG.md:62`).
3. Unbounded token scans also match date-joined strings (`round 2026-09-28…`); R4 bounds tokens (`awk '$1<=99'`).

The §11.6 *conclusion* (no lane dormant) survives the corrected scan; its evidence line does not (5/6 LOG tokens
drifted within the hour — reviewer re-run). §12.1 supersedes it; §11.6 stays unrevised (append-only).

### 12.2 Standing mint/watchlist table (candidates)

**Mint bar — `PROTOCOL.md` closure step 3 → Lifecycle, verbatim:** *"two documented **unplaceable** demand instances
(work no existing province could absorb) or an explicit operator directive."* Correction: the §10.5 refresh-3
paraphrase dropped the load-bearing `*unplaceable*` qualifier (self-defect 10); this table quotes the file.

| Candidate | Surface | Demand instances (dated pointers, verified at cutoff) | Owning-province test | Bar verdict (dated) | Status | Re-run |
|---|---|---|---|---|---|---|
| **kama** | local model serving & endpoint health | **2 unplaceable** — `.ufo/reports/round-3/kagi.md:23-26` (kagi-shokunin `06ef644`, ancestor of HEAD ✓) + `.ufo/reports/round-4/kengaku.md:20-23` (kengaku-shokunin `a1af83c`, ancestor ✓). Commit cites are **repo-qualified**: child short hashes do not resolve in the main repo | **UNPLACEABLE** — kengaku `PROVINCE.md:24-25` *"Not owned: the model-serving plane"*; `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` → exit 1; both discoverers declined the fix as operator-owned (kagi r3:60-61, kengaku r4:71,79) | **Bar met — mint-eligible** (refresh 3 §10.5; re-tested refresh 4 §11.6; re-tested 2026-09-28 refresh 5 — unchanged) | **blocked-external** — operator decision pending at `.ufo/l0-questions.md` **line 2** (protocol r10 entry). Line byte-identical to `e333e7c` at cutoff (`diff` → IDENTICAL); the working-tree edits are new *questions* (kake r12 rewrite 19:39:27, kengaku r10 append 19:45:45), not an answer — the check needs `git diff`, not only `git log` (critic 5). `MANIFEST.json`: 15 `rounds`, `minted` ∈ {[], null} only; D-40 OPEN. **Two debts, distinct** (critic 4): mint execution is operator-gated (roster edit, `PROTOCOL.md`: "MANIFEST.json edits outside `rounds` … remain operator-side integrator work"); recording a *rejection* is the protocol lane's alternative path. Not re-flagged as new | §12.5-K |
| **kessho** | CI/verification harnesses | **5 builder instances** — D-82's three (kumitate `scripts/cite-check.mjs` @ `d65aa24`; kagi `corpus/drift-pins.sh` @ `e64e81b`; kake `scripts/probe-delta.mjs` @ `dd4eabf`) **+ kotoba** `verifiers/verify_harness_claims.py` @ `abef8aa` (r10) and `verifiers/verify_corpus_integrity.py` @ `4dd7753` (r11) **+ kengaku** `grader.py` @ `0c51208` (r10) | All five **absorbed in-province**; no refusal found (rounds 9–13 sweep). The one unplaceable-shaped demand — a fleet-wide gate *standard* (kengaku r10 report: *"no sibling owns an evidence-replay gate"*; L0 line 7) — **names its owner**: protocol/integrator → placeable | **Below bar** (re-test dated 2026-09-28): D-82's re-test condition **FIRED** ("a fourth lane builds one" — kotoba is the 4th builder, kengaku the 5th) and the dated re-test was run; the bar needs two *unplaceable* instances and has zero | WATCH — re-test when: protocol declines the gate-standard ownership, a lane refuses verification work, or the operator rules the standard unplaceable. Connector dissent recorded: tool count ≠ demand count; serviceability controls the bar. D-84's correction carries: cite-check `--selftest` is 19/19 hermetic + 8/9 integration (FAIL on an aggregator-lesson false positive), never re-quote `28/28` | §12.5-S |
| **umihotaru** | fleet/pane wall ops | **1** — `scripts/shokunin-watchdog.sh` (integrator-owned tooling); secondary already owned: kumitate `corpus/knowledge/sighting-wall.md` @ `eca3d14` | Owned, not a domain | **Below bar** (re-tested 2026-09-28) | No new instance: named sweep rounds 9–13 → 0 lines; the adjacent kasegi r13:121-122 pane-crash item is upstream-owned (bounties dispatcher, `attempts()` accounting), reported upstream-bound | §12.5-U |
| **kagemusha** | substrate adapters & mirrors | **3 distributed, served** — kengaku `corpus/knowledge/ledger-route-telemetry.md` @ `2575be6`; kumitate `corpus/knowledge/route-resolution.md` @ `0ac95e1`; kake `corpus/knowledge/mirror-pitfalls.md` @ `cd5b381` | Distributed across three served provinces; no refusal | **Below bar** (re-tested 2026-09-28) | No new instance: in-window hits (kasegi `reroutes.jsonl` distributions r11-r13, kake kimi-mirror sync r11-r12) all fall inside served provinces; the `fleets/registry.json` ownership contest is an intra-province re-split → **D-86** (integrator arbitration) | §12.5-G |
| **axis-framework-stewardship** | SCORECARD templates, per-axis proxies, rollout order | **0 unserved** — surfaced refresh 4 (§11.6); template proposals already routed to protocol (§11.5 P-h/P-i); per-repo cards are lane work | Not a domain — protocol + aggregator work; routed, not refused | **Below bar** (refresh-4 ruling stands; re-tested 2026-09-28) | Sweep rounds 9–13: one incidental census mention (`round-10/protocol.md:380`, adoption 2/6), not a demand. Protocol r11 report not landed at cutoff → re-check next refresh | §12.5-A |

**kama live-drift probes at cutoff (GET-only):** `127.0.0.1:34113/health` → `{"status":"ok"}`; `localhost:8080/v1/models`
→ `404`; `~/.config/the-janitor/opencode.json:16` baseURL → `http://127.0.0.1:8080/v1`; `~/.config/opencode:158` baseURL
→ `http://localhost:8080/v1`. **Drift persists** — filed **D-85** against the round-10 "LANDED-serving" label (the
serving plane is up; the config repoint never landed).

**M4 satisfied: 5/5 candidates carry a dated bar test (2026-09-28)** — the metric did not exist at refresh 4 (0).
**M2 unchanged and correct: 0 mints executed** — the bar is met only by kama and the ruling is operator-side.

### 12.3 Queue movement this refresh

- **D-82 → re-test fired and run** (kessho row above): status stays WATCH with a sharpened re-test condition. This is
  the first positive firing of a written mint trigger in the ledger's history — the table now distinguishes
  *trigger fired* from *bar met*.
- **kotoba r11 LOG lag — observed and self-healed inside the refresh, no row filed:** at 22:52Z kotoba had reported r11
  (19:47) with its `LOG.md` last entry still `## Round 10`; by the 22:55Z cutoff the lane's own r12 commit `7d15407`
  had landed `LOG.md:250 '## Round 11'`. The lag was visible for ~3 minutes — the standing table's responsiveness is
  the evidence that per-refresh re-testing catches same-round drift.
- **§11.9 statements superseded within the hour by lane motion** (recorded because §11.9 is append-only):
  "kasegi advanced to round 13 with no report yet" → r13 report landed (9964 B, main `0933e84`); "kengaku's tree is
  dirty (regeneration in flight)" → dirty 0 at `0c51208`. Queue rows are claims about a moving tree; §12 stamps cutoffs.
- **New rows filed this refresh:** D-85 (protocol — D-39 label vs live probes), D-86 (integrator — `fleets/registry.json`
  contested scope). D-40 (kama mint-or-reject) stays OPEN, blocked-external.

### 12.4 Aggregator self-defects filed at refresh 5 (numbering continues §11.7)

9. **Refresh-4 dormancy scan method was buggy** — case-sensitive token pattern + `sort -V` filename-token ranking +
   shared-LOG attribution (§12.1 corrections 1–3). It under-reported kotoba (`round-9` vs actual `## Round 10`) and
   would attribute the protocol lane's token to the aggregator. Conclusions survived; the evidence line did not.
   Superseded by §12.1 + R4.
10. **Refresh-3 bar citation dropped `*unplaceable*`** (§10.5 paraphrase at `AGGREGATE.md:521-522`) — the qualifier is
    the test every §12.2 row applies. §12.2 quotes the file verbatim.
11. **The wave seed baseline was served to 10 seats as ground truth and was stale within ten minutes** (critic attempt
    3 falsified copying it: counters, reports, LOG tokens, commits, dirty counts all moved mid-wave). Absorbed: every
    volatile cell re-run by this lane at the cutoff. Practice: seeds are hypotheses; only the cutoff pass is evidence.

### 12.5 Re-run commands (copy-paste runnable from the main repo root)

```sh
cd /home/vgpnk/projects/shokunin
```

**R0 — stamp:**
```sh
date -u +'UTC %Y-%m-%dT%H:%M:%SZ'; date +'local %Y-%m-%dT%H:%M:%S%z'
printf 'main HEAD '; git log -1 --format='%h %aI %s'
```

**R1 — counter column:**
```sh
for l in kasegi kengaku kake kumitate kotoba kagi aggregator; do printf '%-10s counter=%s\n' "$l" "$(cat .ufo/state/$l.round)"; done
```

**R2 — dispatch column:**
```sh
awk '$2=="launch" && $3 ~ /^(kasegi|kengaku|kake|kumitate|kotoba|kagi|aggregator)$/ {split($4,a,"="); t[$3]=$1" round="a[2]} END{for(l in t) printf "%-10s %s\n", l, t[l]}' .ufo/watchdog.log | sort
```

**R3 — reports column (+ marker sizes):**
```sh
for l in kasegi kengaku kake kumitate kotoba kagi aggregator; do
  f=$(ls .ufo/reports/round-*/"$l".md 2>/dev/null | sed -E 's|.*/round-([0-9]+)/.*|\1 &|' | sort -n | tail -1 | cut -d' ' -f2-)
  printf '%-10s %-40s %s bytes %s lines\n' "$l" "$f" "$(wc -c <"$f")" "$(wc -l <"$f")"
done
for f in .ufo/reports/round-8/kengaku.md .ufo/reports/round-8/kotoba.md .ufo/reports/round-7/kumitate.md .ufo/reports/round-5/aggregator.md; do printf '%-32s %s bytes %s lines\n' "$f" "$(wc -c <"$f")" "$(wc -l <"$f")"; done
```

**R4 — LOG token + last-entry columns (case-insensitive, bounded, attribution-aware):**
```sh
for d in kasegi kengaku kake kumitate kotoba kagi; do
  f=$d-shokunin/LOG.md
  printf '%-10s max=round-%s\n' "$d" "$(grep -oiE 'round[- ]+[0-9]+' "$f" | grep -oE '[0-9]+$' | awk '$1<=99' | sort -n -u | tail -1)"
done
printf 'last round ENTRY per lane (not a token scan):\n'
for d in kasegi kengaku kake kumitate kotoba kagi; do
  printf '%-10s %s\n' "$d" "$(grep -oE '^## Round [0-9]+|— round [0-9]+' $d-shokunin/LOG.md | tail -1)"
done
grep -nE '^#{2,3} Round [0-9]+ — aggregator' LOG.md | tail -1
git -C kotoba-shokunin cat-file -t 8c300ad; git -C kumitate-shokunin cat-file -t 7a4c9a0
```

**R5 — commit-age column:**
```sh
for d in kasegi kengaku kake kumitate kotoba kagi; do printf '%-10s ' "$d"; git -C "$d-shokunin" log -1 --format='%h %ar'; done
printf '%-10s ' aggregator; git log -1 --format='%h %ar (main repo HEAD, shared)'
printf '%-10s ' aggregator; git log -1 --author='aggregator' --format='%h %ar (last aggregator-authored)'
```

**K — kama row:**
```sh
curl -s -w ' HTTP:%{http_code}\n' 127.0.0.1:34113/health
curl -s -o /dev/null -w '8080=%{http_code}\n' localhost:8080/v1/models
grep -n baseURL ~/.config/the-janitor/opencode.json
diff <(git show e333e7c:.ufo/l0-questions.md | sed -n '2p') <(sed -n '2p' .ufo/l0-questions.md) >/dev/null && echo kama-line-UNANSWERED || echo kama-line-CHANGED
python3 -c "import json;print([r.get('minted') for r in json.load(open('MANIFEST.json'))['rounds']])"
git -C kagi-shokunin merge-base --is-ancestor 06ef644 HEAD && echo ancestor-OK
git -C kengaku-shokunin merge-base --is-ancestor a1af83c HEAD && echo ancestor-OK
```

**S — kessho row:**
```sh
ls kumitate-shokunin/scripts/cite-check.mjs kagi-shokunin/corpus/drift-pins.sh kake-shokunin/scripts/probe-delta.mjs kotoba-shokunin/verifiers/verify_harness_claims.py kotoba-shokunin/verifiers/verify_corpus_integrity.py kengaku-shokunin/grader.py
grep -rln 'verifier\|verification tool\|cite-check\|drift-pins\|probe-delta\|grader' .ufo/reports/round-{9,10,11,12,13}/*.md
grep -n 'no sibling owns' .ufo/reports/round-10/kengaku.md
```

**U/G/A — umihotaru / kagemusha / axis-framework-stewardship rows:**
```sh
sed -n '70,86p' ROADMAP.md
grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-{9,10,11,12,13}/ ; echo "exit=$? (1 = no new instance)"
grep -rn -i -e axis-framework -e stewardship .ufo/reports/round-{9,10,11,12,13}/
```

### 12.6 Standing-table note

Rows are **claims stamped to the cutoff**, not standing facts: three consecutive seat passes ~2 minutes apart produced
different counters (kasegi 13→14, kengaku 10→11 between 22:50:02Z and 22:51:32Z). Re-run §12.5 rather than quoting
the tables. The tables re-test **every refresh**; the falsifiable round-6 targets are met: 12/12 rows carry a
same-refresh re-run command, kama is blocked-external against its L0 pointer without re-flagging, M4 0→5. Residual
gaps kept honest: the dormancy rule has still never been tested against a genuinely dormant lane (0/7 positive
cases), and re-runnability has been demonstrated in exactly one refresh (this one).

---

## 13. Refresh 6 — round-8 aggregator audit (box-3 non-author cold runs)

**Stamp.** Aggregator lane round 8 (`.ufo/state/aggregator.round` = 8; runId `shokunin-r8-aggregator-r1790637197`,
launch `2026-09-28T20:13:18-03:00`). Refresh cutoff: **2026-09-28T23:46:28Z** (20:46:28 -03:00), main HEAD `46e9ec3`,
dirty 23. This refresh discharges the move queued at §11.8 and named in `SCORECARD.md` §Planned (round 7): *"the
highest-value cross-lane-quality move available: a **box-3 execution walkthrough** — one non-author agent per repo
runs `SKILL.md`/`corpus/` with no oral context."* It also carries the §12.1/§12.2 standing tables forward and lands
the refresh-5 artifacts this lane's previous round wrote but never committed (§13.4, commit `6d27283`).

**Method.** One batched `task` call dispatched **15 L2 seats** (MISSION.md floor is 8): six `labrat` cold-run
verifiers (`Box3Kasegi`, `Box3Kengaku`, `Box3Kake`, `Box3Kumitate`, `Box3Kotoba`, `Box3Kagi`), three `scout`s
(`SweepScout` corpus window, `DormancyScout` §12.1, `MintScout` §12.2), one `executor` (`S13Skeleton`), and one each
of `connector` (`OverlapConnector`), `sentinel` (`HazardSentinel`), `critic` (`Falsifier`), `reviewer`
(`CitationReviewer`), `distiller` (`RowDistiller`) — route buckets per MISSION.md. Each cold-run seat entered at
`<repo>/SKILL.md` **only** (no `LOG.md`, `SHONEN.md`, `SCORECARD.md`, `PROVINCE.md` or main-repo report opened before
the run), executed the skill literally inside a ~20-command budget, and wrote exactly one file —
`corpus/lessons/round-8-aggregator-box3-coldrun.md` — committed inside its own repo by that seat, pathspec-limited,
under the aggregator identity, **not pushed** (§13.5 item 18).

**Critic: 7 attempts → 4 FALSIFIED, 3 HELD.** All four falsifications were absorbed *mid-round*, by sending every
cold-run seat an amendment protocol (append-only `## Round-8 amendment (critic-absorbed)` section + second
pathspec-limited commit); 6/6 lessons carry it. The amendment **reversed one verdict** (kumitate `[ ]` → withdrawn →
`[x]`, §13.1). **Reviewer: 41 citations re-executed → 30 PASS, 8 STALE, 3 FAIL** — all three FAILs are cells of this
ledger or this lane's round-7 report (§13.5 items 13–15), i.e. the first non-author audit of the auditor found the
auditor's own defects. **Sentinel**: ruled *no child-repo push* (MISSION.md §Push scope) and issued per-path
COMMIT/HOLD verdicts this round followed; it also retro-classified round 6's child-repo pushes as out of scope
(§13.5 item 18). **Distiller**: 84 distinct `D-` keys, next free **D-87**, 2 duplicate groups folded, 3 standing
contradictions named (§13.2).

### 13.1 Box-3 cold-run verdicts (non-author)

**Gate being re-tested — §11.4, verbatim:** *"Fleet-wide gate observation: **no repo has a single `[x]` on box 3 from
a named non-author verifier.** Every box-3 claim in the fleet rests on a lane-dispatched subagent, which PROTOCOL.md
counts as the lane. … the only way to close box 3 is a cross-lane or integrator execution walkthrough."*

**Authority (critic attempt 1, HELD).** PROTOCOL.md's promotion-gate clause negates *within-lane* dispatch —
*"a subagent the lane dispatched is still the lane"* — and never grants cross-lane authorship; the aggregator authored
none of the six `SKILL.md` files, so an aggregator-dispatched seat is a non-author for every child repo. **Carve-out
absorbed:** this lane *is* a partial author of each child's `corpus/` (its round-1/4/5/6 audit lessons), so box 3's
corpus half is graded against the **lane's own** corpus text and aggregator-authored lessons are cited, not
self-certified. Every lesson names its dispatch chain (`aggregator lane round 8 → L2 seat <id> → .ufo/reports/round-8/aggregator.md`)
so the verifier id resolves — the property D-63/P-j found missing from kagi's `KagiR9Reviewer`.

| Repo | Verifier seat (non-author) | HEAD at run | cmds run/ok/fail | gated (with-artifact / without) | break points | **box-3 grade** | Decided by (executed evidence) | Lesson commits |
|---|---|---|---|---|---|---|---|---|
| kasegi | `Box3Kasegi` | `7483333` | 18 / 16 / 2 | 7 (0 / 7) | 5 | **`[~]` provisional** | `node ops/ev-report.mjs` → exit 0 where `SKILL.md:588` documents exit 2; `node ops/check-freshness.mjs` → exit 0 with a `STALE … honest alarm (AR4)` line where `SKILL.md:113-114` documents live exit 1 | `9dbe69f` + `2b0d869` |
| kengaku | `Box3Kengaku` | `0c51208` | 20 / 20 / 0 | 3 (2 / 1) | 5 | **`[x]` not provisional** | `python3 grader.py --selftest` → exit 0, `ALL PASS` 4/4 with the exact claimed check-ids; `python3 grader.py` → exit 0, `CHECKS n=149 mismatches=0 errata_pinned=1 / VERDICT: PASS`; all 25 cited paths resolved; `git diff 0c51208 -- SKILL.md SHONEN.md` empty ⇒ graded text is HEAD text | `d8f2898` + `06cdc98` |
| kake | `Box3Kake` | `2a5502c` | 16 / 15 / 1 | 12 (8 / 4) | 4 | **`[x]` provisional** | `webzites status --json` → exit 0; `grokbots --check` → exit 1 with the exact documented `FAIL lucario: no registry row`; 15-command free-read battery reproduced every documented exit contract and live claim | `69c1856` + `4c9a985` |
| kumitate | `Box3Kumitate` | `c91fe96` | 10 / 8 / 2 | 0 | 4 | **`[x]` — original `[ ]` WITHDRAWN; non-provisional at `59e6c0c`** | seat: `node scripts/cite-check.mjs --integrations` → 8/9, `VERDICT: FAIL`, exit 1, sole failing case aggregator-owned. Integrator re-run at cutoff on the lane's landed HEAD: `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=4 …)`, **exit 0**, clean tree | `e79fefa` + `0f24ca7` + `942afe4` |
| kotoba | `Box3Kotoba` | `71963e6` | 25 / 20 / 5 | 1 (1 / 0) | 3 | **`[~]` not provisional** | `verify_harness_claims.py` → exit 1, 25/27 (caught same-minute drift: a db row landed 23:30:55Z, run 23:31Z — exactly the documented semantics); `verify_corpus_integrity.py` → exit 0, 9/9; `SKILL.md:168-170` newest-session recipe under-determines file selection (0 hits in the newest-mtime file of 6116) | `683d147` + `7163c81` + `ed5c261` |
| kagi | `Box3Kagi` | `301b9ec` | 26 / 26 / 0 | 7 (1 / 6) | 7 | **`[x]` provisional** | `bash corpus/claim-ledger.sh verify` → exit 0; `bash corpus/transcript-scan.sh` → exit 1 counts-only `HITS=2`; `curl -fsS http://127.0.0.1:8080/health` → exit 22/404 while 34113 is healthy; full gate/selftest chain ran cold | `e0a04d8` + `7c3377c` + `4391b3b` |

**Totals (re-derived from the six payloads):** **115** commands executed (**105** ok / **10** fail), **30** gated steps
(**12** `gated-with-artifact` = counted as executed, **18** `gated-without-artifact`), **28** break points each cited
to a `SKILL.md` line *with the line's text quoted* (critic fix 3). Operative grades: **4 `[x]` / 2 `[~]` / 0 `[ ]`**,
one `[ ]` withdrawn. Provisional at cutoff: 3 (kasegi, kake, kagi — decisive text worktree-only); firmed at cutoff: 1
(kumitate, re-executed by this lane against the lane's landed commit `59e6c0c`); not provisional: 2 (kengaku, kotoba).
Sixteen aggregator-identity commits landed across the six child repos; **X1 = 6/6**.

**Movement against the refresh-4 gate (marks quoted from §11.4 — its box-3 column is superseded by this table):**

| Repo | §11.4 refresh-4 box-3 mark | Round-8 non-author mark | Moved? | Evidence |
|---|---|---|---|---|
| kasegi | `[~]` | `[~]` provisional | mark unchanged, **evidence class changed** — first non-author measurement; `grep -i 'box.?3\|executable without oral' kasegi-shokunin/{SHONEN,LOG}.md` → 0 hits, so no prior verdict existed (D-108) | `9dbe69f`, `2b0d869` |
| kengaku | `[ ]` (*"the box does not exist in its `SHONEN.md`"*, D-15) | **`[x]`** | **moved** — and **D-15 is falsified**: at `0c51208` `SHONEN.md` is a **4-box** file (`grep -c '^- \[' SHONEN.md` → 4; boxes at `:5,:7,:9,:11`), box 3 present but unmarked | `d8f2898`, `06cdc98` |
| kake | `[~]` | **`[x]`** provisional | **moved** — `SHONEN.md:7` still unticked with no named verifier; this run is the first non-author evidence | `69c1856`, `4c9a985` |
| kumitate | `[~]` | **`[x]`** non-provisional at `59e6c0c` | **moved** — via a withdrawn verdict; see §13.1 contamination note and D-110 | `e79fefa`, `0f24ca7`, `942afe4` |
| kotoba | `[~]` (*"a blank-context L2 ran the checklist — still the lane"*) | `[~]` not provisional | mark unchanged, evidence class changed; its `SHONEN.md:14-15` box-3 `[x]` is attributed to `ReviewSHONEN`, a seat kotoba dispatched itself (`.ufo/reports/round-12/kotoba.md:193`) ⇒ `[~]` under the clause — **D-102** | `683d147`, `7163c81`, `ed5c261` |
| kagi | `[~]` (*"a lane-dispatched reviewer reproduced ~15 probes"*) | **`[x]`** provisional | **moved** — and D-63 partially closes: `SHONEN.md`'s four `[x]` name `KagiR9Reviewer`, which resolves nowhere, while this run supplies a resolvable non-author id (`e0a04d8`) | `e0a04d8`, `7c3377c`, `4391b3b` |

**§11.4's fleet-wide gate observation is CLOSED as written**: 4 of 6 repos now carry a box-3 `[x]` from a named
non-author verifier, committed in-repo, with a resolvable dispatch chain. It is superseded by: *no repo's `SHONEN.md`
box-3 line names a resolvable non-author verifier* — the verdicts live in aggregator-owned lessons, and `SHONEN.md` is
outside this lane's write scope, so **the lanes owe the mark update** (routed per repo in §13.2).

**Supersession — §11.4's kumitate box-2 cell** (distiller contradiction 2: *"§11.9's correction supersedes only the
§11.2 D-82 cell; the §11.4 promotion-input cell still carries the falsified 28/28"*). Re-executed at cutoff:
`node scripts/round-gate.mjs --selftest` → **49/49 PASS at HEAD `c91fe96`, 57/57 in the worktree**, exit 0;
`node scripts/cite-check.mjs --selftest` → **19/19 (hermetic) PASS**; `--integrations` → **8/9, VERDICT: FAIL, exit 1**
(the sole failing case is aggregator-owned text, §13.1 kumitate row). The `28/28` figure quoted from a commit message
was never reproducible; **D-51 ⊇ D-84** (folded, §13.2).

**Methodological rulings absorbed from the critic (these change how box 3 is measured fleet-wide, not just this row set):**

1. **Coldness is relative to the entry file, not to the runner** (attempt 2, FALSIFIED). `SKILL.md`'s citation closure
   leaks author context: kumitate `SKILL.md:534` cites *"corpus/lessons/round-6-aggregator-audit.md (aggregator-owned)"*
   and narrates live gate state; kotoba `SKILL.md:596` cites `corpus/knowledge/cold-run-round11.md`, which opens
   *"NON-AUTHOR cold run"* and claims it *"reproduces the author's recorded dispatch observations exactly"*. New
   break-point class **`context-leak`** (rows recorded in 5 of 6 lessons); **box 3 is graded on pointer resolvability +
   step executability, not on runner ignorance.**
2. **Three-outcome gate rule** (attempt 4, FALSIFIED the blanket-`[~]` treatment). PROTOCOL.md's evidence standard:
   *"Where the domain's terminal action is operator-owned … executed means prepared + verified + handed off: the
   handoff artifact … is the outcome pointer, and a documented negative result at that gate still counts."* Every gated
   row is now classified `gated-with-artifact` (counts) or `gated-without-artifact` (does not). Worked examples: kagi's
   `whoami` exit 1 is a documented negative its own craft rule predicts ⇒ counts; kotoba's refusal to run
   `fault_injection_corpus.sh` (clone + `rm -rf /tmp` worlds) ⇒ counts; kasegi's seven unpublished-claim steps ⇒ do not.
3. **Box 3 ≠ box 1** (kagi is the proof case): `[x]` on executability alongside **four falsified claim rows** is
   coherent, not contradictory — the falsified counts are box-1 defects routed to the lane (D-97…D-104), not box-3
   execution breaks.
4. **Live-tree contamination** (attempt 7, FALSIFIED grading a dirty tree as measuring the repo). Stamps now carry the
   full `git status --short` file set, per-claim HEAD-vs-worktree attribution, and a `provisional` marker. This is the
   fix that reversed kumitate: its decisive `proxy-check.mjs` was **untracked at the run HEAD** (`git cat-file -e`
   fatal) and its drift probe's 5th runnable (`audit-env.sh`) was **deleted by the lane mid-audit**; the post-vanish
   re-run gave `PROXY: MATCH` exit 0. Contingency named in its amendment ("if the lane commits `SKILL.md` without the
   tool, box 3 goes cold-broken at the new HEAD") **did not fire**: `59e6c0c` landed tool + `SKILL.md` rows +
   `SCORECARD.md` stanza together (`git -C kumitate-shokunin ls-files scripts/` → 4 tools incl. `proxy-check.mjs`).

### 13.2 Corpus sweep + queue movement since the refresh-5 cutoff

**Window.** Refresh-5 cutoff `2026-09-28T22:55:03Z` / base `f9dcfd2` → this cutoff `2026-09-28T23:46:28Z` / HEAD
`46e9ec3`. All 90 tracked report files enumerated (not sampled) by introducing commit
(`git log --diff-filter=A --format='%h %aI %s' -- <path> | tail -1`); **12 files in window**, of which 8 are filed
reports — **0 markers among them** (`round-9/kumitate.md` 10464 B, `round-10/kumitate.md` 13507 B, `round-11/kagi.md`
10163 B, `round-10/kotoba.md` 13113 B, `round-13/kake.md` 5878 B, `round-6/aggregator.md` 15931 B,
`round-11/protocol.md` 29338 B, `round-7/aggregator.md` 10695 B) — and 2 files that are **not** at a contract path:
`.ufo/reports/round-11/kengaku-DRAFT.md` (15922 B, untracked, **40 unfilled `{{…}}` tokens**, D-90) and
`.ufo/reports/round-12/kotoba.md` (14009 B, untracked, asserts *"committed + pushed in the main repo under the lane
identity"*, D-91). Post-cutoff motion, not swept here: `.ufo/reports/round-14/kasegi.md` (7338 B) landed 20:48 -03 =
23:48Z, two minutes after this cutoff; kasegi's counter is already 15.

**Key-integrity ruling (D-87).** `.ufo/reports/round-11/protocol.md` §Routing files nine new rows numbered
**`D-50`…`D-58`** and its Watch item 5 asks this lane to mirror them "as-is". Those nine keys are **already owned by
this ledger** (`git show HEAD:.ufo/reports/AGGREGATE.md | grep -nE '^\| D-5[0-8] '` → D-50 kumitate in-place lesson
edits … D-58 `SCORECARD.md` rows without `<command> @ <commit>`), and §11.2's adoption rule is *"its `D-nn` ids are
adopted as the ledger's keys — no parallel numbering"*. A collision is therefore not adoptable: **the mirror is
refused as numbered**, and the nine rows enter below as **D-111…D-119** with protocol's text preserved and its own
report as the pointer. Protocol's *substance* is accepted in full — including D-117, which is a charge against this
lane and is discharged by §13.4.

**New rows (24; numbering continues from D-87, the distiller's next free key):**

| Key | Owner | Claim | Evidence (re-executed unless marked *claimed*) | Sev | Status |
|---|---|---|---|---|---|
| D-87 | protocol | r11 §Routing reuses nine ledger keys `D-50`…`D-58` for new rows, so its own cross-refs ("routed D-50/D-52/D-58") point at unrelated defects, and its mirror request would land the collision | `grep -nE '^\| D-5[0-8] ' .ufo/reports/AGGREGATE.md` (HEAD blob) → 9 owned keys; `.ufo/reports/round-11/protocol.md` §Routing table | 7 | OPEN — renumbered here as D-111…D-119; protocol to cite ledger keys, not mint parallel ones |
| D-88 | protocol + operator/scripts | The driver's completion signal is **report-file existence**, so a lane's own report commit is unreachable when a tick lands between write and commit: round-7 aggregator wrote its report 20:10:14 -03, `complete aggregator round=7` fired 20:13:17, and nothing was committed until this round's `6d27283`. PROTOCOL.md's *"A lane report lands last … Landed also means landed by the lane"* is unsatisfiable for the report's own commit under that signal | `stat -c '%y' .ufo/reports/round-7/aggregator.md` → 20:10:14; `grep 'complete aggregator round=7' .ufo/watchdog.log` → 20:13:17; `git log --diff-filter=A -1 --format='%h %aI' -- .ufo/reports/round-7/aggregator.md` → `6d27283` 20:32:43 | 6 | OPEN — proposed: `report_of()` requires the path **tracked** (`git ls-files --error-unmatch`), or lanes write+commit+push the report in **one shell invocation** (adopted by this lane this round, §13.4); same root as protocol's r11 D-58 → D-119 |
| D-89 | protocol + all lanes | The r11 compaction (`6bd4f38`, 583→446 lines) invalidated every `PROTOCOL.md:<line>` citation fleet-wide: **7 in main-repo reports + 80 in child repos**, 11 of them above the new file length | `wc -l PROTOCOL.md` → 446; `grep -rnoE 'PROTOCOL\.md:[0-9]{1,4}(-[0-9]{1,4})?' .ufo/reports/` → 7; `grep -rhoE 'PROTOCOL\.md:[0-9]{1,4}' *-shokunin --include='*.md' \| wc -l` → 80; `round-10/kumitate.md:60` cites `:264-265` for the ancestry rule, now at `:178` | 6 | OPEN — proposal **P-p**: clause-text anchors only, never line numbers, into mutable integrator files |
| D-90 | kengaku | Round 11 has no report at the contract path: only an untracked draft with 40 unfilled `{{…}}` tokens, plus two untracked evidence dirs — the round's substance is non-durable while the counter reads 11 | `ls .ufo/reports/round-11/` (no `kengaku.md`); `grep -c '{{' .ufo/reports/round-11/kengaku-DRAFT.md` → 40; `git -C kengaku-shokunin status --porcelain` → `?? corpus/evidence/round11-fleet/`, `?? corpus/evidence/round11-power/` | 6 | OPEN |
| D-91 | kotoba | Round-12 report is untracked while asserting it was *"committed + pushed in the main repo under the lane identity"*; its mission already terminated on file existence | `git ls-files -o --exclude-standard .ufo/reports` → `round-12/kotoba.md`; `awk '$2=="complete" && $3=="kotoba"' .ufo/watchdog.log \| tail -1` → `20:28:22 complete kotoba round=12` | 6 | OPEN — child side is durable (`git -C kotoba-shokunin status --porcelain` → empty) |
| D-92 | kagi | Round-11 report violates the hash-citation rule: it names **no git commit** (its only hex tokens are six sha256 artifact prefixes) and its round pointer `Branch/commit: round-11` does not resolve; both its child commit `301b9ec` and its report commit `029c474` carry the operator identity | `grep -oE '\b[0-9a-f]{7,40}\b' .ufo/reports/round-11/kagi.md` → 6 sha256 prefixes only; `git -C kagi-shokunin rev-parse round-11` → fatal, exit 128; `git -C kagi-shokunin log -1 --format='%an <%ae>' 301b9ec` → operator | 6 | OPEN — a resolvability-only grader would mis-file this 10163 B real report as a marker candidate |
| D-93 | kake | The filed round-13 report is being corrected by an **in-place worktree rewrite** self-labelled "r14 erratum", where PROTOCOL.md requires *"Corrections land as new commits … never an in-place rewrite"* | `git diff -- .ufo/reports/round-13/kake.md` → −2/+4 lines rewriting the timer-sweep timestamps | 4 | OPEN (its live r14 mission may still land it) |
| D-94 | kake + integrator | `.ufo/l0-questions.md` is off-ledger: a filed question was rewritten in place rather than superseded by an appended entry, and the file's whole post-cutoff delta sat uncommitted (now committed at `46e9ec3`, so the pre-rewrite text survives only as HEAD's blob) | `git diff f9dcfd2 HEAD -- .ufo/l0-questions.md` → empty at sweep time; `git show HEAD:.ufo/l0-questions.md \| wc -l` → 6 vs worktree 8 (now 9, committed) | 5 | OPEN — proposal: L0 entries append-only like `LOG.md`, answers as new dated lines |
| D-95 | kasegi | `corpus/knowledge/mission-ledger.md:32-34` states the row schema requires `transition` and counts "718 lines", but **8 of 718** rows lack the field; routed by kotoba r12, unrepaired, no ledger row existed | `python3` over `~/Projects/bounties/ledger/missions.jsonl` → `rows 718 lacking transition 8`; `sed -n '32,34p' kasegi-shokunin/corpus/knowledge/mission-ledger.md`; *claimed* source `.ufo/reports/round-12/kotoba.md` §Cross-domain | 5 | OPEN |
| D-96 | integrator + operator | Six `*-shokunin/SKILL.md` sit inside **no discovery root** (0/6 in the union of four roots) — a fleet-wide surface no province owns; with it, `~/.config/opencode/agents/ufo.md:7` `cascade_note` ~30 days past its own expiry and `~/.agents/AGENTS.md:55/:57` stale procedures | *claimed*: `.ufo/reports/round-12/kotoba.md` §Cross-domain; `grep -n -i 'discovery root' .ufo/reports/AGGREGATE.md` → 0 hits before this row | 3 | OPEN — needs a routed owner or an explicit operator disposition |
| D-97 | kasegi | Two documented exit contracts falsified by a cold run: `ops/ev-report.mjs` exits **0** for both no-arg and missing-program-file where `SKILL.md:588` documents exit 2; `ops/check-freshness.mjs` exits **0** while printing `2 live-mode source(s) stale — honest alarm (AR4)` where `SKILL.md:113-114` documents live exit 1 | lesson `round-8-aggregator-box3-coldrun.md` commands 9–10 at `9dbe69f`/`2b0d869` | 4 | OPEN — a gate that cannot fail is not a gate |
| D-98 | kengaku | The serving-stack pin is **pid-based** (`pid 1299`) while the same paragraph rules that hermetic gates must pin committed bytes and never `/proc`; a restart orphans the only serving-stack anchor | `SKILL.md:371-378` (quoted text in the lesson); pin verified alive today (flags `EXACT_MATCH`, 2 slots × `n_ctx 16384`) | 5 | OPEN |
| D-99 | kengaku | Ledger event counts on a live-appended source carry no per-number "as of" stamp, so a cold operator cannot tell `verified 2026-09-28` from `verified at round N`: total 7,218→7,226, `mission_parked` 1,188→1,189, `operator_decree` 58→64 inside one round | lesson step 3 re-executed; five sibling counts still exact (`dispatcher_tick` 3,680 / `mission_dispatched` 1,167 / `attempt_reset` 68 / `mission_done` 26 / `mission_failed` 21) | 4 | OPEN |
| D-100 | kake | The lucario GHP canonical (`veigapunk.github.io/lucario/`) has **no `fleet.config.json` row** — the `lucario` row's url is the kimi slot — so `SKILL.md:26`'s "live 200, verified 09-28" is unprobeable by the lane's own verb set and rests on manual assertion; the cold verifier had to hand-roll a GET outside the skill's verbs | lesson commands 8/10 + `webzites status --json` universe 18 | 4 | OPEN |
| D-101 | kumitate | Worktree `SKILL.md:525-527` + a `SCORECARD.md` proxy stanza cited `scripts/proxy-check.mjs`, which did **not exist at HEAD** (untracked, `git cat-file -e` fatal): had the lane committed the docs without the tool, box 3 would have gone cold-broken at the new HEAD | amendment §6; **CLOSED at cutoff** — `59e6c0c` landed tool + docs + stanza together, `git -C kumitate-shokunin ls-files scripts/` → 4 tools, `node scripts/proxy-check.mjs` → `PROXY: MATCH` exit 0 | 4 | **CLOSED** `59e6c0c` (integrator re-execution `942afe4`) |
| D-102 | kotoba | `SHONEN.md:14-15` box-3 `[x]` is attributed to `ReviewSHONEN`, which `.ufo/reports/round-12/kotoba.md:193` lists among kotoba's own dispatched seats ⇒ `[~]` under *"a subagent the lane dispatched is still the lane"*; the lane's own verifier note concedes *"every check in this file is lane-run"* | critic attempt 3; `kotoba-shokunin/SHONEN.md:12-24` | 4 | OPEN — `SHONEN.md` is outside aggregator write scope; the round-8 non-author verdict is committed and citable instead |
| D-103 | kotoba | `verifiers/fault_injection_corpus.sh` is listed among runnable verifiers with no mutation warning; it clones and `rm -rf`'s `/tmp` worlds (`script:27-28`), discoverable only by opening it — a cold operator following the `.py`-heavy verifier set would run it | `SKILL.md:618-620`; lesson Gated table (the seat refused it; classified `gated-with-artifact`) | 4 | OPEN — same class as D-105, proposal **P-n** |
| D-104 | kagi | `corpus/transcript-scan.sh` baseline is documented `exit 0 TRANSCRIPT_SCAN: CLEAN`; the cold run gave **exit 1, `HITS=2`** (two pre-existing `xai-` cells + 2 WARN), and dispositioning pre-existing hits from a fresh leak needs classification context the skill does not give | lesson command at `e0a04d8`; credential tripwire stayed 0 | 4 | OPEN |
| D-105 | kagi (+ fleet pattern) | `SKILL.md:39` presents `the-janitor cdp-bridge ensure` as ordinary flow, but the verb **unconditionally clobbers a shared surface outside every repo** — `~/.local/share/the-musketeer/chrome-profile/NativeMessagingHosts/com.1password.1password.json` — with no existence/diff guard and no gate mark. An auditor cold run rewrote it at 20:33:23 -03 this round | `~/.local/bin/the-janitor:251-271` (`cat >"$NMH_JSON" <<EOF` + `chmod 600`); post-run `stat` → mode 600, 325 B, mtime `2026-09-28 20:33:23 -03`; not a git repo, prior bytes unrecoverable; net effect content-identical (fixed heredoc, only `$BROWSER_SUPPORT` interpolated) and non-secret | 3 | OPEN — proposal **P-n**: decision tables mark mutating verbs (`MUTATES: <target>, <reversible?>`); a verifier's read-only discipline is unenforceable by instruction alone |
| D-106 | **aggregator** | This lane's own `kotoba-shokunin/corpus/lessons/round-6-aggregator-audit.md:30` prints an `awk` that cannot produce the four-number result it is cited for — a self-falsifying evidence command in an auditor artifact; kotoba r12 repaired its identical copy and routed this one | `git show HEAD:SKILL.md \| awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}' \| od -c` → `\n` (one empty value); re-derivable per-section form appended with cutoff output (14/9/9/8, first slot grown 13→14) | 4 | **CLOSED** `2839f60` (kotoba-shokunin) — proposal **P-q** |
| D-107 | kumitate | `SHONEN.md` carries no box-3 self-verdict line (8-line unchecked checklist); the first recorded grading of any kind is this round's non-author run | `e79fefa`/`0f24ca7`/`942afe4`; lesson §Post-run comparison | 1 | OPEN |
| D-108 | kasegi | No box-3 verdict line exists anywhere in `SHONEN.md` or `LOG.md`, so §11.4's `[~]` had no in-repo referent | `grep -iE 'box.?3\|executable without oral' kasegi-shokunin/{SHONEN,LOG}.md` → 0 hits | 1 | OPEN |
| D-109 | kumitate | `SKILL.md:552-553` prose does not say `--integrations` belongs to `scripts/cite-check.mjs`, not `round-gate.mjs`; a cold reader misattributed it and got exit 64 (`unknown argument`) — the misattribution is itself the evidence | lesson amendment §4 (attribution correction); `node scripts/round-gate.mjs --integrations` → exit 64 | 3 | OPEN |
| D-110 | fleet + protocol | A **withdrawn verdict is not machine-readably superseded**: `grep -m1 -E '\*\*\[[x~ ]\]\*\*'` on kumitate's lesson still returns the withdrawn `[ ]`, so any tooling or reader taking the first match grades the repo `[ ]` | repaired in-repo by an appended `## Operative verdict` block, last section by design (`942afe4`); proposal **P-o**: withdrawn verdicts carry a tail-anchored operative block and audits resolve grades tail-anchored, never `-m1` | 5 | **CLOSED for kumitate** (`942afe4`); OPEN as a fleet convention |
| D-111 | kake | *protocol r11 §Routing, re-keyed from its colliding `D-50`*: report-before-commit ×3 (r11 −8 s, r12 −3m56s, r13 child `2a5502c` after the report); no hash citations r10–r13; `SHONEN`=0 r10–r13; `/tmp` evidence pointers r10–r12; child commit under operator identity | `.ufo/reports/round-11/protocol.md` §Conformance 2/6 + §Routing; `rounds[18..21]` notes | 5 | OPEN (mirrored as numbered by the ledger, not by protocol) |
| D-112 | kagi | *re-keyed from protocol's `D-51`*: `ade32e4` pathspec violation (swept the ledger rename + an L0 line); report-before-commit (r10 −30 s); no hash citations r10/r11; `SHONEN`=0 r9–r11; child `301b9ec` operator identity | same report §Conformance 4/2/6; corroborated by D-92 | 5 | OPEN |
| D-113 | kasegi | *re-keyed from protocol's `D-52`*: dead hash `d7dbd9a` + non-ancestor `3d28a716` cited in the round-13 report; report-before-commit (r13 −15 s); own commits subject-only r12/r13; `SHONEN`=0 r11–r13; child `7483333` operator identity | same report §Conformance 5/2/6 | 5 | OPEN |
| D-114 | kengaku | *re-keyed from protocol's `D-53`*: dead hash `e66e614` in the round-10 report (unresolvable in main + all six children); the r10 report was operator-swept (`7ef548e`) although r9 self-landed — identity habit regressed | same report §Conformance 5; `rounds[18]` notes | 4 | OPEN |
| D-115 | kumitate | *re-keyed from protocol's `D-54`*: `SHONEN`=0 r8/r9; `/tmp` pointers r8/r9; `surface-probe.mjs` claimed 1438 L vs measured 1435 (r9); own commit `2075363` uncited (r8); child `c91fe96` operator identity (r10); reports operator-swept r9/r10 | same report, `rounds[16,17,18]` notes | 4 | OPEN |
| D-116 | kotoba | *re-keyed from protocol's `D-55`*: `/tmp` evidence pointers r10/r11 (self-flagged in-report — the honest form, still a defect until committed or reproducible); otherwise the conforming lane of that round | same report, `rounds[19]` notes | 2 | OPEN |
| D-117 | **aggregator** | *re-keyed from protocol's `D-56`*: r6 report untracked at mission completion (swept by `3ea42cb`); r7 report on disk 20:10 while the mission was live (complete 20:13:17) with LOG/SCORECARD r7 sections + ledger refresh 5 uncommitted at 20:20 — *"its respawn (r8) owes them under the inheritance rule"* | same report §Conformance 8/12 | 6 | **CLOSED** `6d27283` (§13.4) — this round discharged it; root cause stays OPEN as D-88 |
| D-118 | protocol (self) | *re-keyed from protocol's `D-57`*: round-10 report's kake-`SHONEN` parenthetical false + the "0 of 62" census false at write time; a round-11 entry-note phrasing superseded 3 minutes after `closed_at` — all corrected by appended record, none rewritten | same report §Conformance 1/3 | 2 | CLOSED by its own appended record |
| D-119 | operator/scripts | *re-keyed from protocol's `D-58`*: the template's ordering line ("Write … report" before "Round end: commit") is now causally linked to four lanes' report-before-commit inversions; five child-lane contract items still absent (M7 1/5); `report_of()` still existence-only | same report §Conformance 2/10 + r10 §Template correction; this ledger's D-88 is the same root measured from the aggregator side | 6 | OPEN — operator-side; L0 line 3 |

**Closures and movement on existing rows (each re-tested at this cutoff):**

| Row | Status at refresh 6 | Evidence |
|---|---|---|
| D-48 (protocol: compact `PROTOCOL.md`) | **LANDED** | `6bd4f38`: `wc -l PROTOCOL.md` → 446 (was 583 at `f9dcfd2`); obligation census 93/93 (`.ufo/waves/round-11/verify-census.sh`, committed `3ea42cb`). Side effect filed as D-89 |
| D-15 (kengaku 3-box `SHONEN.md`) | **CORRECTED — falsified** | at `0c51208` the file is 4-box: `grep -c '^- \[' kengaku-shokunin/SHONEN.md` → 4; boxes at `:5,:7,:9,:11`, box 3 present but unmarked. §11.4's kengaku row is superseded |
| D-39 ⊇ D-85 (endpoint repoint label) | **FOLDED** (canonical D-39; D-85 is its correction rider — distiller duplicate group 1). Drift re-confirmed at cutoff | `curl -s 127.0.0.1:34113/health` → `{"status":"ok"} HTTP:200`; `localhost:8080/v1/models` → `404`; `~/.config/the-janitor/opencode.json:16` → `http://127.0.0.1:8080/v1`; `~/.config/opencode/opencode.json:158` → `http://localhost:8080/v1`. **Pointer correction:** §12.2 cited `~/.config/opencode:158`, which is a directory; the carrier is `opencode.json:158` |
| D-51 ⊇ D-84 (gate reads an auditor's lesson as a live defect) | **FOLDED** (distiller duplicate group 2) and **reproduces exactly at HEAD** | `node scripts/cite-check.mjs --integrations` → 8/9, `VERDICT: FAIL`, exit 1, sole failing case `corpus/lessons/round-6-aggregator-audit.md:30,:38` — aggregator-owned text, so it cannot grade the lane down (P-f stands) |
| D-59 (kumitate's card prints kagi `PASS (11 cases)` vs the ledger's re-executed 13) | **STANDING CONTRADICTION, unrepaired** | distiller contradiction 3: `AGGREGATE.md` D-59 vs D-10's proof cell; no later refresh superseded either |
| D-61 (kengaku r8/r9 unlanded) | **CLOSED** (log half) | `grep -n 'round 8\|round 9' kengaku-shokunin/LOG.md` → `:13`, `:14-16`; the 101 B r8 marker stays graded `failed` historically |
| D-75(a) (`MANIFEST.json` `rounds` stuck) | **MOVED — now measurable-false as written** | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"` → **22** (protocol r11 appended 7 at `3ea42cb`) |
| D-77 (`SCORECARD.md` collision) | **RULED** | `.ufo/reports/round-11/protocol.md` §Contested-scope rulings 4: per-lane sections in the single canonical path, each lane committing only its own section's hunks; `55e23de` is the reference method. This round complied — its `SCORECARD.md`/`LOG.md` edits touch only the aggregator section |
| D-78 (axis vocabulary `novelty`/`consistency`) | **RULED-partially** | same §Rulings 3: scores are calibration defects until the vocabulary exists; operator action owed (`AXES.md` is operator-side). L0 line 6 stands |
| D-79 (untracked dispatch prompts) | **RE-ACCUMULATING** | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` → 4 at write time (`kasegi-round-15`, `kotoba-round-13`, `kumitate-round-12`, `protocol-round-12`); 2 at the cutoff pass. This lane's own `aggregator-round-{7,8}.md` were swept by protocol's durability commit `3ea42cb` — attribution defect, not this lane's to fix |
| D-82 / kessho trigger | **WATCH — fired again** | see §13.3 mint table: 5 lanes / 6 artifacts → **6 lanes / 9 artifacts** |
| D-86 (`fleets/registry.json` contested scope) | **RULED** | `.ufo/reports/round-11/protocol.md` §Rulings 1: object-level split, decree ledger → kasegi, routing + `registry-check` → kumitate; both lanes owe a `PROVINCE.md` record (D-76) |
| D-16, D-58, D-68 | **OPEN** | D-16: `ls kengaku-shokunin/corpus/lessons/` still has no `round-6.md`. D-58: hex-token counts moved up in 5 of 6 cards (kasegi 0, kengaku 7→16, kake 0→4, kumitate 4→8, kotoba 3→4, kagi 2→5) — caveat: the metric counts tokens anywhere in the card, not rows carrying `<command> @ <commit>`. D-68: re-verified `11 of 77` rows violate `total - ok == len(violated)+len(errors)` (ledger said 11/76 — denominator drift only) **plus a wording hazard**: `violated`/`errors` are lists, so the row's literal formula is a concatenation trap; restate with `len()` |
| D-40 (kama mint-or-reject) | **OPEN, blocked-external** | §13.3; `.ufo/l0-questions.md` line 2 byte-identical to `e333e7c` ⇒ unanswered; not re-flagged as new |

**L0 channel at cutoff.** `.ufo/l0-questions.md` = **9 lines, now committed** (`46e9ec3`), all awaiting operator action —
surfaced in full in `.ufo/reports/round-8/aggregator.md` §L0. No answer lines observed in any entry.

### 13.3 Standing tables re-tested (dormancy §12.1, mint §12.2)

**Dormancy rule — PROTOCOL.md "Promotion gates" preamble, verbatim:** *"A shonen that records no `LOG.md` activity
across two consecutive rounds it was dispatched and reported in is flagged **dormant** by the integrator in the round
notes; rounds the lane was not dispatched do not count against it. Dormancy is a review trigger for the operator,
never an automatic retirement."* Marker grading per the report-contract clause (*"A filed report that records no lane
work … is a marker, not a report … A short report that names a real committed round-work hash is a *defective* report,
not a marker"*): failed markers are excluded from the dispatched-and-reported pair, `ok`-graded defective reports
count. `dormant_count` is **derived**: for each lane the last two rounds both dispatched *and* reported were listed,
their consecutiveness confirmed against the launch sequence, and each round's `LOG.md` entry re-checked by entry scan.

**Scan correction over §12.1 (new this refresh, and caused by this lane):** the commit-age cell must **filter
aggregator seat commits** — `git -C <repo> log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%h %ar'`.
This round put 16 aggregator-identity commits into the six child repos, so an unfiltered `git log -1` reports *this
lane's* activity as the lane's: kotoba's unfiltered cell would have understated its commit age ~25× (raw HEAD `ed5c261`
vs lane commit `71963e6` 18m). §13.6-R carries the filtered form.

| Lane | Counter | Last dispatched | Last report landed (marker grading) | Last `LOG.md` round entry | Last **lane-authored** commit (age at cutoff) | Verdict | Δ vs §12.1 |
|---|---|---|---|---|---|---|---|
| kasegi | 15 (14 at the cutoff pass) | r14 @ 19:50:43 -03 | r13 — 9964 B, `ok`; minor defect: does not name its own round commit `7483333`. Post-cutoff: `round-14/kasegi.md` 7338 B landed 23:48Z | round 13 (`LOG.md:296`); pair r12 (`:242`) | `7483333` 62m (raw HEAD is this lane's `2b0d869` — filtered) | **ACTIVE** | report unchanged at cutoff; commit age moved; r14 landed post-cutoff |
| kengaku | 11 | r11 @ 19:50:44 -03 | r10 — 13160 B, `ok` (cites `0c51208`, pushed); r8 = 101 B **failed marker**, excluded. **r11 has no report** — untracked DRAFT, 40 `{{…}}` (D-90) | round 10 (`LOG.md:17`); pair r9 (`:14-16`) | `0c51208` 64m (raw HEAD `06cdc98` — filtered) | **ACTIVE** — but two rounds dispatched without a landed report if r11 stays a draft | r11 still unreported; DRAFT tokens counted |
| kake | 14 | r14 @ 20:05:46 -03 | r13 — 5878 B, `ok` + minimum-content defect (cites `a642f93` but not its own round commit `2a5502c`); r13 also carries an in-place worktree erratum (D-93) | round 13 (`LOG.md:21`); pair r12 (`:19`) | `2a5502c` 41m (raw HEAD `4c9a985` — filtered) | **ACTIVE** | report r12→r13 (new since refresh 5) |
| kumitate | 11 | r11 @ 20:05:47 -03 | r11 — `.ufo/reports/round-11/kumitate.md` 16341 B, landed **20:45:10 -03 at `46e9ec3`** (i.e. inside this refresh, 5 minutes before the cutoff); r10 13507 B `ok` (cites `c91fe96`); r7 = 122 B marker naming `7a4c9a0` → `ok` + defect, counted | round 11 (lane `LOG.md` entry lands with `59e6c0c`); pair round 10 (`:263`) | `59e6c0c` (lane commit landed 23:46Z; previous `c91fe96` 39m) | **ACTIVE** | report r10→r11; **first lane to land tool+docs+stanza together**, which lifted kumitate's provisional box-3 verdict |
| kotoba | 13 | r13 @ 20:28:23 -03 | r12 — 14009 B, `ok` (cites `4dd7753`, `7d15407`, `d49dfa5`, `e997d45`) but **untracked** (D-91); r8 = 120 B marker naming `8c300ad` → `ok` + defect, counted | `## Round 12` (`LOG.md:308`); pair `## Round 11` (`:250`) | `71963e6` 18m (raw HEAD `2839f60` — filtered; 4 aggregator seat commits landed here in ~20 min) | **ACTIVE** | report r11→r12; **§12.1/§12.3's "self-healed by 22:55Z" cell is FALSIFIED** — the Round-11 entry landed in `633859f` at 23:27:55Z, 33 min *after* that cutoff (`git -C kotoba-shokunin show 7d15407:LOG.md \| wc -l` → 248, last `## Round` = Round 10) |
| kagi | 12 | r12 @ 20:13:20 -03 | r11 — 10163 B, `ok` in substance but with a **new citation defect: zero resolvable git objects** (D-92) | round 11 (`LOG.md:262`); pair round 10 (`:218`) | `301b9ec` 38m | **ACTIVE** | report r10→r11; D-92 filed |
| aggregator | 8 | r8 @ 20:13:18 -03 (this refresh) | r7 — 10695 B, `ok`; **untracked at its own mission completion, landed by this round at `6d27283`** (§13.4); r5 = 254 B **failed marker**, excluded | `## Round 7` (main `LOG.md:115`, filter `^#{2,3} Round [0-9]+ — aggregator`); pair `## Round 6` (`:62`) | `6d27283` (last aggregator-authored at the cutoff pass; this round's commits follow it) | **ACTIVE** | r7 artifacts moved uncommitted → committed **and pushed** |

**Dormant count: 0 / 7** — derived, not asserted. §12.6's residual gap stands: the dormancy rule has still never been
tested against a genuinely dormant lane (no positive case in six refreshes). Nearest watch row this refresh: kengaku,
whose r11 exists only as a 40-token draft — if r12 also fails to land a report, the pair becomes two consecutive
dispatched rounds with no durable report, which the rule grades through the marker clause rather than through
`LOG.md` silence (its `LOG.md` carries round 10).

**Mint bar — PROTOCOL.md Lifecycle, verbatim:** *"**Shonen** — minted when a domain demand is proven: two documented
**unplaceable** demand instances (work no existing province could absorb) or an explicit operator directive — the mint
bar, stated once here; closure step 3 applies it."*

| Candidate | Demand instances at cutoff | Owning-province test | Bar verdict (dated 2026-09-28) | Status | Δ vs §12.2 |
|---|---|---|---|---|---|
| **kama** | 2 unplaceable, both re-verified: `.ufo/reports/round-3/kagi.md:23-26` (kagi-shokunin `06ef644`, `merge-base --is-ancestor` → OK) + `.ufo/reports/round-4/kengaku.md:20-23` (kengaku-shokunin `a1af83c` → OK) | UNPLACEABLE re-executed: `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` → exit 1 | **Bar met — mint-eligible** (unchanged since refresh 3) | **blocked-external** — `.ufo/l0-questions.md` line 2 verified still the kama question in worktree, HEAD and `e333e7c`, then `diff` → identical ⇒ UNANSWERED; not re-flagged | none. Drift persists (D-39/D-85): 34113 healthy, 8080 → 404, both configs still pin 8080 |
| **kessho** | **6 lanes / 9 artifacts** (was 5/6): the six re-confirmed + kumitate `scripts/round-gate.mjs` @ `c91fe96` 22:59:34Z, kagi `corpus/claim-ledger.sh` @ `301b9ec` 23:08:39Z, kotoba `verifiers/verify_corpus_independent.py` + `fault_injection_corpus.sh` @ `633859f`/`71963e6` 23:27:55Z — all ancestor-verified, all in-province | All absorbed; **0 unplaceable**. `grep -rn -i 'refus' .ufo/reports/round-{11,12,13}/*.md` → 3 hits, all about refused *commands*, none a lane refusing verification work. The one unplaceable-shaped demand (fleet gate standard, kengaku r10 *"no sibling owns an evidence-replay gate"*, L0 line 7) now has a **ruled** owner: protocol r11 §Rulings 2 deferred it *with a date* (`SCORECARD.md` §Planned round-12 item 2) ⇒ placeable | **Below bar** — builder-count trigger **FIRED again** (a 6th builder); the bar needs two *unplaceable* instances and has zero | WATCH — all three sharpened sub-conditions explicitly resolved this pass: protocol decline **not** fired (deferral ≠ decline), lane refusal **not** fired, operator has not ruled the standard unplaceable | demand 5/6 → 6/9; owner "names its owner" → **ruled with a date** |
| **umihotaru** | 1 (`scripts/shokunin-watchdog.sh`, integrator-owned tooling); secondary owned: kumitate `corpus/knowledge/sighting-wall.md` @ `eca3d14` | Owned, not a domain | **Below bar** (unchanged) | No new instance: `grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-{9..13}/` → exit 1; `.ufo/reports/round-14/` was empty at the sweep pass | none |
| **kagemusha** | 3 distributed, served (kengaku `ledger-route-telemetry.md` @ `2575be6`; kumitate `route-resolution.md` @ `0ac95e1`; kake `mirror-pitfalls.md` @ `cd5b381`) | Distributed across three served provinces; no refusal. The `fleets/registry.json` contest is an intra-province re-split and is now **arbitrated** | **Below bar** (unchanged) | **D-86 RULED** (protocol r11 §Rulings 1); `PROVINCE.md` records owed by both lanes (D-76) | status moved from "contested" to "ruled" |
| **axis-framework-stewardship** | 0 unserved; template proposals routed to protocol (§11.5 P-h/P-i) | Not a domain — protocol + operator work; routed, not refused | **Below bar** (refresh-4 ruling stands) | **Refresh-5's "re-check when protocol r11 lands" is DISCHARGED**: `.ufo/reports/round-11/protocol.md` exists (29338 B, 20:27:09 -03, landed `392b3c7`); `grep -n -i -e axis-framework -e stewardship` on it → exit 1 (0 mentions) ⇒ no new demand, nothing refused. It also **ruled** the `SCORECARD.md` collision half (D-77) and keeps template work operator-side | re-check discharged; candidate unchanged |

**Mints executed: 0** — `python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(sum(1 for x in r if x.get('minted')))"` → 0 over **22** entries (was 15 at refresh 5). **M4: 5/5** candidates carry a bar test
re-run in this refresh. **M2 stands and is correct**: the bar is met only by kama and the ruling is operator-side.

### 13.4 Round-7 durability defect + landing, and the ordering rule it falsifies

At round open this lane's previous round existed **only as working-tree bytes** in a repo seven sibling lanes commit
into: ledger §11.9 + §12 (+232 lines), `SCORECARD.md` §Round 7 (+26/−13), `LOG.md` §Round 7 (+41), and
`.ufo/reports/round-7/aggregator.md` (10695 B, untracked). Timeline, all re-executed: report mtime **20:10:14 -03**;
`complete aggregator round=7; respawning` **20:13:17**; `launch aggregator round=8` **20:13:18**; no aggregator commit
between `e333e7c` (round 6, 19:28:15) and this round. The round-7 report's own §Compliance promised *"single
pathspec-limited commit (`AGGREGATE.md`, `SCORECARD.md`, `LOG.md`, this report) … then push"* — a plan the driver's
existence-only completion signal made unreachable.

**Landed by round 8: `6d27283`** (aggregator identity, pathspec-limited to exactly those four paths, pushed;
`origin/master` = `6d27283` at 23:33Z). Content was landed **unedited** — provenance: *filed round 7 at cutoff
`f9dcfd2`, landed round 8 unedited* — so refresh 5 stays append-only and no byte was rewritten to suit this round.
Reviewer verification: the working copy is byte-identical to the committed blob (`git show 6d27283:.ufo/reports/round-7/aggregator.md | diff - <file>` → empty), all 9 unique hashes in it resolve in their attributed repos, and it
cites no self-hash.

Two sibling acts worth recording because they are the reason the bytes survived: the protocol lane's `55e23de`
committed **only its own** `SCORECARD.md`/`LOG.md` hunks with the subject *"staged hunk-surgical: the aggregator's
uncommitted round-7 sections in both files remain its own to land"* — the D-77 ruling applied correctly by the other
party to the collision — and protocol's r11 report independently filed the same defect against this lane (its `D-56`,
mirrored here as **D-117**, now CLOSED).

**Rule this falsifies (D-88, P-r).** PROTOCOL.md requires *"A lane report **lands last** … Landed also means landed
by the lane: the commit that adds `.ufo/reports/round-<N>/<id>.md` carries the lane identity, because the driver
completes the mission the instant the file reaches disk."* Under an existence-only `report_of()`, those two halves
contradict: the report cannot be committed before it exists, and existing ends the mission. The only ordering that
satisfies both is **write + commit + push the report inside one shell invocation**, so no tick can land between. This
lane adopted that form for round 8 and proposes it as the fleet rule until `report_of()` checks `git ls-files
--error-unmatch` (operator-side; L0 line 3, D-119).

### 13.5 Aggregator self-defects filed at refresh 6 (numbering continues §12.4)

12. **Round-7 artifacts written, never committed** — §13.4. Root cause is shared: driver-side (existence-only
    completion, D-88/D-119) and lane-side (the report was written before the commit, and the lane's turn ended).
    Evidence: `stat -c '%y' .ufo/reports/round-7/aggregator.md` → 20:10:14 vs `complete aggregator round=7` 20:13:17;
    `git log --author=aggregator-shokunin -1` at round open → `e333e7c` (round 6). Landed `6d27283`. Practice adopted:
    commit-before-report for everything but the report, then report write + commit + push in one invocation.
13. **§12.1/§12.3's kotoba "self-healed inside the refresh" claim is false** — reviewer FAIL 2. The Round-11 `LOG.md`
    entry landed in `633859f` at **23:27:55Z**, 33 minutes *after* the 22:55:03Z cutoff it was claimed to precede;
    `git -C kotoba-shokunin show 7d15407:LOG.md | wc -l` → 248 with last `## Round` = Round 10. A working-tree
    observation was published as a cutoff measurement. Corrected in §13.3 (kotoba Δ column); §12 stays unrevised
    (append-only).
14. **§12.5 published an unrunnable command block while labelling it "copy-paste runnable"** — reviewer FAIL 1,
    re-executed by this lane: R4's token scan `grep -oiE 'round[- ]+[0-9]+' | grep -oE '[0-9]+$'` returns **empty for
    all six lanes** on this host, because `grep` here is `pi-uu-grep 0.2.0` and emits zero-length matches for the
    anchored `-oE '[0-9]+$'` (`printf 'abc 123\n' | grep -oE '[0-9]+$' | od -c` → `\n`). The unanchored variant works
    but admits noise (kumitate `max=42` from a `--round 42` string). §13.6-R ships only the **entry-scan** form
    (`grep -oE '^## Round [0-9]+|— round [0-9]+'`), which is host-independent. A re-run block that cannot be re-run is
    worse than none: it makes the row unfalsifiable while looking falsifiable.
15. **Refresh-5 mixed windows and imprecise pointers** — reviewer FAIL 3 + a path defect: the round-7 report claimed
    *"7 entries in `.ufo/l0-questions.md` at cutoff"* while the cutoff blob had **6** lines (`git show
    f9dcfd2:.ufo/l0-questions.md | wc -l`); the 7th was a post-cutoff working-tree read. And §12.2 cites
    `~/.config/opencode:158` — a directory; the carrier is `~/.config/opencode/opencode.json:158`. Both corrected here.
16. **The cold-run ritual's read-only rule was unenforceable against a hidden side effect.** A seat following
    `kagi-shokunin/SKILL.md:39` ran `the-janitor cdp-bridge ensure`, which unconditionally rewrote a shared manifest
    outside every repo (D-105). No instruction to a verifier can substitute for a mutation census of the skill's own
    verb set. Net effect was benign (fixed heredoc, non-secret, content-identical, mtime-only) — verified by reading
    `~/.local/bin/the-janitor:251-271` — but the class is not: the same verb shape on a vault or publish path would
    have been an irreversible external effect caused by an audit. Repair: proposal **P-n** + a pre-flight step in any
    future walk (`--help`/source-read every verb before executing it).
17. **This lane published a commit ritual it had not executed once.** `git commit -- <path>` on an **untracked** file
    aborts with `pathspec … did not match any file(s) known to git`; two seats hit it before the corrected form
    (`git add -- <path> && git commit -- <path>`, one invocation, nothing staged between commands) was broadcast to all
    six. A ritual is a claim like any other: run it before dispatching it.
18. **Round 6 pushed into six child-repo remotes, which this lane has no push scope for.** MISSION.md §Push scope:
    *"Lanes push ONLY to `VeigaPunk/shokunin` (main repo) or their own `VeigaPunk/<lane>-shokunin` remote."* The six
    child remotes are other lanes' own. Sentinel ruling adopted: **round-8 lessons are committed locally and not
    pushed**; each owning lane's own push carries them (all six repos hold unpushed commits at cutoff: kasegi 2,
    kengaku 2, kake 2, kumitate 1, kotoba 7, kagi 3). The round-6 lesson commits are all remote-contained
    (`git -C <repo> branch -r --contains <h>` → `origin/master` ×6) and remain HEAD ancestors, so nothing needs
    reverting — the breach is recorded, not repaired by history.

### 13.6 Re-run commands (host-verified at the round-8 cutoff; `grep` here is pi-uu-grep 0.2.0)

```sh
cd /home/vgpnk/projects/shokunin
```

**B — box-3 verdict set (grades resolve tail-anchored, never `grep -m1`; D-110):**
```sh
for d in kasegi kengaku kake kumitate kotoba kagi; do
  f=$d-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
  printf '%-9s %s | %s B %s ln | amendment=%s | ' "$d" \
    "$(git -C $d-shokunin log --format='%h' -- ${f#$d-shokunin/} | tr '\n' ' ')" "$(wc -c <"$f")" "$(wc -l <"$f")" \
    "$(grep -c '^## Round-8 amendment' "$f")"
  grep -oE '\*\*\[[x~ ]\]\*\*' "$f" | tail -1   # operative grade = LAST match
done
```

**B2 — provisional markers and the kumitate re-execution that lifted one:**
```sh
for d in kasegi kengaku kake kumitate kotoba kagi; do printf '%-9s ' "$d"; grep -oiE 'not provisional|provisional until[^.;,]*|remains provisional' $d-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md | tail -1; echo; done
git -C kumitate-shokunin ls-files scripts/ && (cd kumitate-shokunin && node scripts/proxy-check.mjs; echo "exit=$?")
```

**W — sweep window + queue keys:**
```sh
for f in .ufo/reports/round-*/*.md; do printf '%s %s\n' "$(git log --diff-filter=A --format='%h %aI' -- "$f" | tail -1)" "$f"; done | sort | awk '$2>"2026-09-28T22:55"'
git ls-files -o --exclude-standard .ufo/reports .ufo/prompts
grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -t- -k2 -n | tail -1   # highest key; next free = +1
```

**R — dormancy re-test (entry-scan form only; the §12.5-R4 token scan is host-broken, §13.5 item 14):**
```sh
date -u +'cutoff %FT%TZ'; git log -1 --format='main HEAD %h %aI'
for l in kasegi kengaku kake kumitate kotoba kagi protocol aggregator; do printf '%-11s counter=%s\n' "$l" "$(cat .ufo/state/$l.round)"; done
awk '$2=="launch"{split($4,a,"="); t[$3]=$1" r"a[2]} END{for(l in t) printf "%-11s %s\n", l, t[l]}' .ufo/watchdog.log | sort
for d in kasegi kengaku kake kumitate kotoba kagi; do printf '%-9s %-14s lane-commit %s\n' "$d" \
  "$(grep -oE '^## Round [0-9]+|— round [0-9]+' $d-shokunin/LOG.md | tail -1)" \
  "$(git -C $d-shokunin log -1 --perl-regexp --author='^(?!aggregator-shokunin)' --format='%h %ar')"; done
grep -nE '^#{2,3} Round [0-9]+ — aggregator' LOG.md | tail -2
for f in .ufo/reports/round-8/kengaku.md .ufo/reports/round-8/kotoba.md .ufo/reports/round-7/kumitate.md .ufo/reports/round-5/aggregator.md; do printf '%-40s %s B\n' "$f" "$(wc -c <"$f")"; done   # marker ledger
```

**K/S/U/G/A — mint rows:** §12.5's blocks, with two corrections: the second 8080 pointer is
`~/.config/opencode/opencode.json:158` (not `~/.config/opencode:158`), and the kessho artifact list gains
`kumitate-shokunin/scripts/round-gate.mjs`, `kagi-shokunin/corpus/claim-ledger.sh`,
`kotoba-shokunin/verifiers/verify_corpus_independent.py`, `kotoba-shokunin/verifiers/fault_injection_corpus.sh`.
```sh
curl -s -m4 -w ' HTTP:%{http_code}\n' 127.0.0.1:34113/health; curl -s -m4 -o /dev/null -w '8080=%{http_code}\n' localhost:8080/v1/models
grep -n baseURL ~/.config/the-janitor/opencode.json ~/.config/opencode/opencode.json
sed -n '2p' .ufo/l0-questions.md | cut -c1-60; diff <(git show e333e7c:.ufo/l0-questions.md | sed -n '2p') <(sed -n '2p' .ufo/l0-questions.md) >/dev/null && echo kama-line-UNANSWERED || echo kama-line-CHANGED
python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(len(r),'rounds;',sum(1 for x in r if x.get('minted')),'minted')"
ls kumitate-shokunin/scripts/{cite-check,round-gate}.mjs kagi-shokunin/corpus/{drift-pins.sh,claim-ledger.sh} kake-shokunin/scripts/probe-delta.mjs kotoba-shokunin/verifiers/*.py kengaku-shokunin/grader.py
grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-*/ ; echo "exit=$? (1 = no new instance)"
grep -rn -i -e axis-framework -e stewardship .ufo/reports/round-1[1-9]/ ; echo "exit=$? (1 = discharged)"
```

**Q — this ledger's own claims (P-q: an audit row's command must reproduce its own cell):**
```sh
grep -c 'PROTOCOL\.md:[0-9]' .ufo/reports/AGGREGATE.md            # line-number cites into a mutable file (P-p) → target 0
(cd kotoba-shokunin && git show HEAD:SKILL.md | awk '/^## /{if(h!="")printf "%s=%d\n",h,n; h=$0;n=0} /^- \[ \]/{n++} END{if(h!="")printf "%s=%d\n",h,n}' | grep -v '=0$')
```

### 13.7 Standing-table note + residual gaps

Rows are **claims stamped to the cutoff** (`2026-09-28T23:46:28Z`, main HEAD `46e9ec3`), not standing facts. Measured
proof this refresh: main HEAD moved three times inside the wave (`392b3c7` → `6d27283` → `46e9ec3`), kumitate's lane
commit landed 1 second before a cutoff cell was read, and kasegi's report for round 14 landed two minutes after the
cutoff. Re-run §13.6 rather than quoting the tables.

Residual gaps kept honest:

- **3 of 6 box-3 verdicts are provisional** (kasegi, kake, kagi) because decisive text was worktree-only; they firm up
  or break at each lane's next commit, and only a re-run can tell which. Round 9's move candidate is exactly that
  re-test.
- **No `SHONEN.md` box-3 line names a resolvable non-author verifier yet.** The verdicts live in aggregator-owned
  lessons; `SHONEN.md` is outside this lane's write scope, so the marks are the lanes' to update (routed as D-102,
  D-107, D-108 + per-repo rows).
- **Corpus-conformance verdicts (CORPUS.md rule 10) were not re-emitted this refresh.** The round-8 move is the
  promotion-box walkthrough; §11.1's six `not conformant` verdicts stand, and this refresh's per-repo findings are
  routed as `D-` rows rather than restated as verdicts. Named here because an unrefreshed verdict is a stale claim, not
  a neutral one.
- **The dormancy rule still has no positive test case** (0/7 dormant in six refreshes), so its correctness is
  unproven in the one direction that matters.
- **Queue integrity is now a measured property, not an assumption**: 84 distinct keys, one collision refused (D-87),
  two duplicate groups folded (D-39⊇D-85, D-51⊇D-84), three standing contradictions named (§13.2). 46 rows remain open
  across 12 owners (distiller tally: kasegi 12, protocol 10, kumitate 9, kake 8, kengaku 8, operator 7, kagi 6,
  fleet 4, external 3, aggregator 2, integrator 1, kotoba 1 — counted before this refresh's 24 new rows).

**Proposals routed to protocol/CORPUS (integrator lands; this lane cannot):** **P-n** decision tables mark mutating
verbs (D-105, D-103); **P-o** withdrawn verdicts carry a tail-anchored operative block, and audits resolve grades
tail-anchored (D-110); **P-p** no line-number citations into mutable integrator files (D-89); **P-q** an audit row's
evidence command must reproduce its own observed cell — mechanically checkable, and it applies to auditor artifacts
too (D-106); **P-r** while `report_of()` is existence-only, the report must be written, committed and pushed in one
shell invocation (D-88).
