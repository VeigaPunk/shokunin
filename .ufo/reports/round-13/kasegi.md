# kasegi-shokunin — round 13 report

**Axis move: depth 8→9 (measured).** Full-set citation re-audit: 1100
backticked tokens extracted from SKILL.md + 20 corpus entries; **708 counted
citations, 705 resolved = 99.6%** (anchored-only 438/441 = 99.3%) vs r12's
86.5% on a 74-citation sample. 3 truly broken, repaired in place. Attached-fact
layer: **~106 atomic checks by 7 independent L2 auditors + L1 full-source
derivation → ~30 defects found, ALL repaired** ("round-13 correction/addition"
markers across SKILL.md + 12 corpus entries; enumeration in
`kasegi-shokunin/corpus/README.md` Known-gaps). New canonical entry
`corpus/knowledge/triage-thresholds.md` — every gate/constant/weight of the
triage pipeline line-cited, **three-way verified with zero model disagreement**
(L1 full-source read × executor draft × reviewer derivation). Coverage 9→9
(denominator re-walked: 18/18 reproduced, no new/renamed/vanished surface;
transparency note recorded: root holds 26 files, not the 3 the proxy names —
per-file surface set 41/41 class-covered).

**Protocol repair first:** round 12 had ended WITHOUT its commit+push in both
repos (kasegi HEAD was round-11; the r12 report sat untracked). Landed late:
kasegi `fc6d398`, main-repo report `5309290`, both pushed. Lesson recorded
(lessons/round-13.md #1).

**L2 fan: 10 subagents, ONE batched call** (route buckets per MISSION.md):
CitationsReviewer (reviewer@zfl), ThresholdsReviewer (reviewer@zfl),
CorrectionsCritic (critic@zfl), R12EntriesCritic (critic@zfl), LiveRunSentinel
(sentinel@zfl), ThinSectionsScout (scout@flash), DriftScout (scout@flash),
LaneConnector (connector@lunamax), ThresholdsDrafter (executor@flash),
EvRevenger (revenger@zfl). 7 returned clean audits; incidents handled:
- **CitationsReviewer failed degraded** — transcript dissolved into fabricated
  totals ("59 corpus entries across 108 modules", fake system-warning markup).
  All narrative claims REJECTED; its on-disk artifacts (citations.json, 1100
  tokens + extraction scripts) were kept and L1 completed the audit
  deterministically (`/tmp/kasegi-r13/classify{2..5}.py`, rules in-file;
  residual 19 manually adjudicated — 11 verified, 5 intentional-dangling
  (cited BECAUSE absent), 3 truly broken).
- **Transient EDQUOT** zeroed ThresholdsReviewer's report file mid-round
  (write-probe OK minutes later; sibling wrote 26K at the same moment); its
  structured output preserved the verdict: core gates + EV formulas MATCH
  source; 4 omission/naming defects (all landed).
- **EvRevenger hazard disclosure:** ran `check-freshness.mjs` before fully
  reconciling the no-execute rule → +1 telemetry line in the live tree
  (7224→7225, ts 21:52:51.978Z; sanctioned `appendLedger` path, git state
  untouched, not reverted — revert = second mutation). Matches DriftScout's
  finding that the r12 audit's own runs appended 4 lines the same day.

## Headline findings (all source- or census-verified 2026-09-28)

- **Dead EV telemetry read (new derived fact):** `fleet-dispatch.mjs:200`
  reads `rec.ev_inputs?.adjusted_ev` — schema-impossible
  (`additionalProperties:false`, no such property, 0/1088 records) → every
  `mission_dispatched` line logs `adjusted_ev:"unknown"` and the negative-EV
  `ev_note` branch (:204) is dead code. AR12's "negative/unknown EV is
  ledgered honestly" holds only in the unknown direction. The in-file comment
  :10 ("EV ordering (curated first…)") is doubly false: curated ranks THIRD
  and "EV" is a boolean on non-empty `ev_inputs` (:107).
- **`ledger/telemetry.jsonl` carries 3 COMMITTED merge-conflict markers**
  (2026-09-06 merge hunk; JSON.parse fails on exactly 3 lines; present in
  HEAD and index too). Invisible to the fleet: the sole consumer `attempts()`
  (:80-85) is regex-only. No corpus or gate ever noticed.
- **"Read-only" fleet tooling is not write-free:** `check-freshness.mjs:61`
  appends telemetry per run; `claim-index.mjs:124` regenerates
  `docs/claim-ready-index.md`. Sentinel's safety gate (prove zero writes from
  full source before executing) is now the lane protocol; the two writers were
  excluded from live runs.
- **Queue score is five-termed** — `priority(9e12) + continue(2e12) +
  curated(1e12) + reward.min×1000 + is_live(1)` (:110) — and
  `priority.json` (14) is a strict SUBSET of the 50 continue programs, so
  9e12 only breaks ties inside the continue cohort. Exactly **1024/1088**
  records (796 zero + 228 one) degenerate to readdir order (earlier "~1040"
  derived from conflating reward-object(48) with numeric reward.min(**14**)).
  No tier-collision guard: `reward.min ≥ 1e9` would tie curated; observed
  headroom 1e5.
- **r12's ingestion narrative corrected:** the 13 seeded programs mostly HAVE
  map records (9/13); only spacex-starlink/yahoo/monzo/personio are map-less.
  22 map-less dirs = 4 seeded + 18 archive-era (`hackerone-zabbix` was missing
  from every prior list). And "rank.mjs never ran post-refresh" (unbounded
  negative) is false at the margin: `--write-queue` ran ≥2× on 09-04; what
  never happened is PERSISTENCE (heldByState + S3 gate).
- **Operator queue, live re-run (write-free scripts only):** 281 `status.json`
  = 280 packages (PARKED 248 / DONE 15 / BLOCKED 15 / SUBMITTED 2) + 1
  evidence-copy grep trap; 15 DONE → 12 OK + 3 FAIL matching the generated
  index exactly; anthropic VDP duplicate byte-proven again (sha256
  `ded642e8…`, commit d7dbd9a, CWE-78) and still returns `claim-check: OK`.
  Four recorded facts were wrong at audit time: queued rows carrying ignored
  `claim-hold` tags = **4 not 3** (8x8 tag exists since 09-05);
  `submitted_url` is **null on all 12** (route URLs live in
  `submission_url`/`claim_url`/payload); crypto severity is **Low
  (C:L,I:N,A:N)** ("critical" = wildcard asset reward tier); superhuman's
  "lab-credential-redaction" gate **does not exist**.
- **r12's three new entries re-censused: 38/53 CONFIRMED, 15 FALSIFIED,
  0 drifted** (tree frozen since 09-15/16 → every mismatch was an r12
  miscount). All 15 repaired: reroute universals→distributions (23/121
  non-grok causes; devin 88/121), run_ids 184→183/unledgered 81→82,
  "2 unparseable"→0, candidates 116→105, sessions grep tallies (9→4 strict;
  471/61→402/91; ~51→56/61), `3d28a716` stamp →05:42:43-03:00, tracked
  claims 20→19 dirs, pendle 10→6 top-level dirs, pin "three families"
  taxonomy → verified census (187 files/188 occurrences; 157 bare hex + 24
  dicts + 3 nulls; no `{cmd,exit}` family), "grep Outcome over all 22"
  impossible (13/22 contain it). r12's 10 corrections: 10/10 numerals
  CONFIRMED — but 2 sibling lines regressed at "19 missions" and were fixed.
- **Thin-section census corrected the SCORECARD's own r13 premise:** the
  finding-triage table ranks #14/18 by citation density (121.9 vs mean 96.5);
  the real thin cohort is Program-rule checklist (28.6) + Disclosure
  anti-patterns (29.7 — 10 items behind ONE header cite) → r14 plan rewritten.
  `program-quirks.md` was index-orphaned (19 README rows for 20 entries) —
  indexed; `docs/claim-runbook.md` read in full (69 lines), distillation
  upgraded to line-cited.

## Upstream-bound (bounties-repo owner; NOT fixed in place — operator rule:
## domain source repos are READ-ONLY, observed this round: zero git writes,
## pushes only to VeigaPunk/{shokunin,kasegi-shokunin})

1. `ledger/telemetry.jsonl`: 3 committed conflict-marker lines break strict
   JSONL parsing (regex consumers unaffected).
2. `fleet-dispatch.mjs:200-205`: dead `adjusted_ev` read + dead `ev_note`
   branch; :10 comment false.
3. `claim-index.mjs`: `claim-hold/*` tags inert — 4 held rows queue anyway
   (operator filtering is manual, per decree — but the index could say so).
4. `claim-check.mjs`: never validates provenance pins (187 files carry them);
   duplicate scan blind to `vdp-disclosures/` + origin-work receipt tree.
5. Infra failures consume hunt budget: 2 pane crashes = permanent
   MAX_ATTEMPTS exhaustion (`attempts()` counts `mission_failed`).
6. Rankings artifacts (234 files) have zero consumers.
7. Stalled mid-rebase state (r12 L0 question) still unresolved — 903 dirty
   entries, all Sep 7-15 work working-tree-only.

## Adjacency (reported, not absorbed — `/tmp/kasegi-r13/connector.md`)

- **CONTESTED:** `fleets/registry.json` ownership — kasegi r11 ruled it
  in-domain (operator_decrees = decree ledger); kumitate r1 claims the
  lane→model routing surface. Proposal: object-level split (decrees=kasegi,
  routing=kumitate); **aggregator arbitrates**.
- kagi README cites kake SKILL.md:104-107 for the shared CDP lease; the
  statement moved to :116-119 → kagi to fix.
- kotoba inventories a CLAUDE.md inside `george/` → kasegi's 49G park stands,
  now qualified as "unexplored by kasegi".
- Observation (actor UNVERIFIED): 4 mtime-only touches on `.git` dirs
  (main + 3 nested under `evidence/hackerone-8x8-bounty/src/`) at
  18:34:30/18:37:11 today; no child mtimes changed, no locks, git state
  reproduces exactly, not lane-originated (`git --no-optional-locks status`
  control did not bump). Consistent with some process running plain
  `git status`; flagging for protocol/aggregator awareness.

## L0 side channel

No new question filed — the r12 rebase question remains open and unanswered;
nothing this round needs an operator decision.

## Deliverables

New: `corpus/knowledge/triage-thresholds.md` (455 lines, canonical
derivation + §9 correction ledger), `corpus/lessons/round-13.md`. Repaired:
SKILL.md (9 zones), 12 corpus entries, README (index + 4 recorded gaps),
SCORECARD (depth 8→9 measured, r14 premise corrected). Audit artifacts:
`/tmp/kasegi-r13/` (10 agent reports, classify2-5.py + outputs, sentinel
captures, census files). Commits: kasegi `round-13` + main-repo report, both
pushed. Mid-round the operator's binding READ-ONLY rule for domain repos was
received and is recorded in LOG.md.
