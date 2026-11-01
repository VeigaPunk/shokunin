# tabi — round 47 (Windows host)

Dispatch digest: `2026-11-01T00:40:23-07:00 launch tabi round=47 base=b95b546949e7 (zcode run14)`
(`.ufo/watchdog.log`); no `complete` line at write time. Mission open ~69 min at write time
(> two driver ticks) — **progressing**: five lane-authored commits landed and pushed under the
lane repo this round (`80325bd8` → `d76eb5bb` → `524910a9` → `c2711c47` → `dce01d28`), the report
itself being the last act. Baseline `b95b546949e71f34bfaa1e63de44aff4b4d29371`; lane head at
report time `dce01d280cacfe586c7ec69135d43e7a95faebe6` (pushed, `git ls-remote origin
refs/heads/master` equal).

**Headline: C1 (adjacency) VERIFIED under its frozen predicate. C2 (operability) REFUSED under its
own pre-declared kill rule — the routed repair is landed and live-verifies, but the frozen
after-state was mis-authored from reasoning instead of a pre-data measured prediction. Round
admission: FALSE — reported honestly; the claim was not re-declared post-data. No axis is harmed.**

## Work performed

- **C1 — adjacency (lowest owned axis, 8): the r46-planned regression-gate re-run became real.**
  At round open the committed r46 ledger generation measured RED against the advanced fleet: ten
  sibling heads advanced since the r46 snapshot, three provinces changed bytes — meter exit 1,
  **17 findings** (receipt `.ufo/waves/round-47/controls/c1-meter-red-at-round-open.json`, taken
  before any lane write). audit-r47 (16 rows: 10 unchanged + 6 sibling-absent) and delta-r47
  (12 lanes, 16 line rows) regenerated at ONE fresh snapshot; binfor's two genuinely new
  browser-ground lines (`PROVINCE.md:30` rea-cdp-browser over the host's own Chrome/Edge; `:33`
  list-browser-targets/inspect-web-page over a loopback CDP endpoint) adjudicated
  **contested-open** — the same family as the sre `:53` row, fleet L0 `b6b3b5e4…` :65 still open;
  every other disposition carried from r46 by exact whole-line quote match. Meter v7 (pure core
  byte-identical to v6; committed retarget diff `.ufo/waves/round-47/controls/v6-v7-retarget.diff`;
  selftest 16/16) at correction-1 `524910a9`: **exit 0, predicate true, 0 findings**. One head race
  (sre + tsukuroi) caught between data commit and meter run and resolved under the frozen
  data-correction flow — a correction, not a refusal.
- **C2 — operability: the r46-routed `minimalEnv` PATH repair (sourced S157).** Red at round open:
  the committed pre-repair gate exits 2 `could_not_evaluate` (`git_failed`, `status=spawn`) —
  `.ufo/waves/round-47/controls/c2-gate-red-at-round-open.json`. Repair landed at `c2711c47`
  (PATH split/join on `path.delimiter`, keep `isAbsolute`; the only functional delta vs the freeze
  blob): the gate **evaluates** — exit 1, verdict=failed, rows=16, verified=5, findings 6 ×
  sibling_unresolved (exactly the absent siblings, 1:1 with the audit-r47 sibling-absent rows) +
  4 × ruling_unresolved + 3 × quote_too_long — and the self-test is clean on this host
  (`ADJACENCY_SELFTEST verdict=clean cases=57 reasons=18 could_not_evaluate=6`). The frozen
  predicate demanded verified=10 with exactly-6 findings; **the kill rule fired and the claim is
  refused**. The two honest finding classes the refusal surfaced — the fleet-venue split (the gate
  requires one directory to be both fleet repo and sibling parent; this host splits them) and the
  legacy 25-word quote cap vs the meter-era whole-line quotes — are recorded with cause in
  SCORECARD (r48 planned), not smoothed.
- **r46 carry-in (all four items, `corpus/lessons/round-46-verifier-spotcheck.md` §7):**
  V1 closed as SOURCES row **S156** (`teaches` opens `supersedes S155 —`; staged blob re-measured
  **104,255 B** — `git cat-file -s 859d441fa1f5b5f70e1ec6ca636e91edf1ae481b` → 104255 — sha
  unchanged; the superseded "104,251 B" named, never rewritten in place). V2 closed as
  `corpus/knowledge/chrome-cdp-teardown-round-46-corrected.md` (trio-first per the
  r21-corrected precedent; body verbatim, suffix-identity asserted; original keeps an append-only
  supersession paragraph; README round-47 section + correction index). V3 superseded by a fresh
  receipt-derived disclosure: `.ufo/waves/round-47/measure/selfassessment-precommit.txt` reads
  `verdict=failed rev=c2711c47… mismatches=1 could_not_evaluate=171 superseded=24` (the 1 is the
  pre-commit `m3-unlanded-paths` artifact; the r46 receipt reads `mismatches=1
  could_not_evaluate=175 superseded=23` — the same single m3 class at both revisions); every
  number in the round-47 disclosure is quoted from a receipt's own summary line. L2-floor L0
  (tabi | round-44) stays open and routed around; no wave clause in any predicate; L1-inline.
- **FRESH-START (§7):** r41/r42/r43 rejected closures re-spot-checked in committed bytes at HEAD
  (r41 receipt blobs `7b2ece05`/`5930d20f`; r42 counter `5c45c4d5` + selftest receipt `ec0c238e`
  verdict=clean 18/18 + signing note `72e6b85f`; r43 D3 crash receipt `54ea155a`). Ruled out
  (full list in `.ufo/waves/round-47/claims.json` `freshStartNote`): re-running r46 receipts
  (do-nothing reachable); the meter re-run alone with a stationary fleet (do-nothing reachable —
  frozen pre-data with the replacement declared; the round-open meter measured 17 findings, so the
  work was real); the V1/V2/V3 corrections as axis claims (routed protocol work, not moves);
  S152–S155 90d rechecks (due 2027-01-29, not due); a third claim (job-object surface absent in
  Node; two red+green claims plus three routed corrections is the honest size); Firefox/BiDi/
  wave-settled claims (absent surface; open L0); widening the gate repair beyond minimalEnv (a
  semantic change smuggled into a routed fix).
- **Frontier observation (reported, not absorbed):** the host scratch area holds recent
  `kaidoku-r53…r55` and `revenger-r74…r78` working dirs while both lane dirs are absent from the
  sibling parent — the audit-r47 `sibling-absent` rows' "successor ground" note stands; belongs to
  the operator/integrator.
- Scratch `scratch/tabi-r47` used for the meter build/authoring aids and deleted at round close
  (verified absent); this round launched no browser and the round-close sweep found 0 token-bearing
  browser processes.

## Landed changes (each tied to its LOG.md entry — `## Round 47 — 2026-11-01`; commits cited by hash, all helper-printed, all pushed)

| Commit | Change |
|---|---|
| `80325bd8e977a2730cb7b2bbd16ae26d4b022648` | freeze: claims.json (2 claims, predicates, kill rules, 6 frozen digests, fresh-start note, carry-in routing), meter v7 + selftest receipt + retarget diff, the two round-open red controls, census-START receipt (exit 0) |
| `d76eb5bbf84276d0f0d568d6918e1e571555a441` | C1 data: `corpus/adjacency-host-audit-r47.tsv` + `corpus/adjacency-host-delta-r47.tsv` at one snapshot. **Disclosure (lesson Mistake 2):** this commit's message names the C2 repair while its gate blob is still pre-repair (the edit landed later); corrected by the next commit, disclosed in LOG + lesson + here |
| `524910a98abe7d21ed81bfffb1366d43eea0e8a5` | C1 correction 1 under the frozen flow: both ledgers re-bound to a fresh snapshot after the sre/tsukuroi head race — the cited measured revision for C1 |
| `c2711c47fb12c88c401268fbcdd5a41ed9adddae` | C2 repair: `scripts/check-adjacency.mjs` `minimalEnv` host-portable PATH filter (import + block only) |
| `dce01d280cacfe586c7ec69135d43e7a95faebe6` | integration: SCORECARD round-47 block, SOURCES S156+S157 (155 → 157), corrected teardown note + original supersession append (notes 63 → 64), README round-47 section + correction index, lesson `corpus/lessons/round-47.md` (Gate + 3 Mistakes), LOG entry, and receipts (green/red meter, gate green + selftest, committed-bytes, selfassessment, check-sources, census-end, S157 staged copy) |

## Before → after measurements

- **C1 (adjacency) — VERIFIED; measured at `524910a98abe7d21ed81bfffb1366d43eea0e8a5`:**
  before: `node .ufo/waves/round-46/counters/c1-adjacency-host-v6.mjs --rev b95b5469… --repo <lane> --fleet <fleet>` → exit 1, findingCount **17**;
  after: `node .ufo/waves/round-47/counters/c1-adjacency-host-v7.mjs --rev 524910a9… --repo <lane> --fleet <fleet>` → exit 0, predicate true, findingCount **0**, counts {roster:16, mapRows:16, auditRows:16, deltaLanes:12}.
  Ledger histogram: `awk -F'\t' 'NR>1{n[$2]++} END{for(k in n) print k, n[k]}' corpus/adjacency-host-audit-r47.tsv` → `unchanged 10 / sibling-absent 6`.
  Instrument: `--selftest` → allPass=true 16/16; meter blob `168e1ecc…` equal freeze → measured (`measure/c1-committed-bytes-at-cited-rev.txt`).
- **C2 (operability) — claim REFUSED under the frozen kill rule; repair landed at `c2711c47fb12c88c401268fbcdd5a41ed9adddae`:**
  before: `node scripts/check-adjacency.mjs --repo <lane> --fleet <fleet> --json` → exit **2**, `git_failed (status=spawn)`;
  after (repaired): same command → exit **1**, verdict=failed, rows=16, verified=**5**, findings 6 × sibling_unresolved + 4 × ruling_unresolved + 3 × quote_too_long — the frozen exactly-6/verified-10 clause false, kill rule fired.
  Repair scope: `git diff 80325bd8..c2711c47 -- scripts/check-adjacency.mjs` = import + PATH block only. Self-test: `node scripts/check-adjacency.mjs --self-test` → exit 0, `verdict=clean cases=57 reasons=18 could_not_evaluate=6`.

## Sources & frontier

`SOURCES: 155 → 157` — counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (and `awk` malformed/duplicate/enum checks, all clean: `node scripts/check-sources.mjs` → exit 0, `verdict=clean rows=157 tiers=A:141,B:7,C:9 status=queued:15,mined:132,rejected:10 findings=0` at the integration tip). Rows added: **S156** (docs/A — correction: `teaches` opens `supersedes S155 —`, the 104,255 B count with its command, sha unchanged; mined), **S157** (docs/A — Node.js path API, opened this round by raw fetch + stage + 1-hit quote; mined; used-by the round-47 lesson). No rows touched in place; census START **and** END exit 0 (END carries 22 W04 warnings: the 21 pre-existing + S156's intentional URL re-use of S155 — disclosed in the lesson). Sourced claim: C2's evidence cites S157, opened this round. Knowledge notes 63 → 64 (the corrected entry; original keeps a supersession append). Stale-count mining per §2b: the r46 V1 number-drift, closed as S156.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | No new coverage-map ground: C1 re-binds held ledger ground (the two genuinely new browser-ground lines are binfor province hits, screened + adjudicated, not tabi corpus ground); S156 is a correction; S157 documents the repair's own primitives; notes 63 → 64 is the correction's own record. |
| quality | improved | The routed defect closed in committed bytes with live red (exit 2, spawn failure) and green (exit 1 evaluated; selftest clean 57/57) receipts; the C1 regression gate went red 17 → green 0 with the two new browser-ground lines adjudicated rather than smoothed; S155's drifted count corrected as S156 without editing the original row; no admitted entry failed a re-check. |
| discernment | improved | The lane's own frozen kill rule refused its own claim at data time (C2) and the refusal is recorded with its rationale instead of a post-data re-declaration; the head race ran through the frozen correction flow; every disclosure number this round is quoted from a receipt's own summary line. |

## SHONEN

- `[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources` — unchanged this round (`SKILL.md` untouched; prior pointer `SKILL.md` §Approval table, §Evidence ladder, §Runbook stands); asserted-by-author.
- `[~] At least one end-to-end domain task executed and logged in LOG.md` — this round's end-to-end task: the adjacency regression gate red→green cycle and the gate repair, logged in the LOG round-47 entry with committed receipts (`.ufo/waves/round-47/`); asserted-by-author.
- `[~] Instructions executable by an agent without oral context` — the round's instruments run from committed bytes alone (meter v7 usage line, gate CLI, authoring flow in the lesson); asserted-by-author.
- `[~] No cross-domain bleed (PROVINCE.md still accurate)` — `PROVINCE.md` untouched and accurate; binfor's CDP browser-ground lines adjudicated `contested-open` and reported, not absorbed; asserted-by-author.

(All four remain `[~]`: only a non-author may write `[x]` — left to the operator per the r46 closure note; the round's evidence looks fully checkable by a non-author.)

Assimilation: `considerthese/` does not exist in the lane repo (checked 2026-11-01). Assimilation: none — shokuknow unreachable.

L0: the tabi | round-44 line (L2 floor) remains open and was routed around — never treated as answered; no new L0 question this round.
