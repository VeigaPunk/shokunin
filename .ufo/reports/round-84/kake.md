# kake — round 84 (attempt 1)

## Work performed

Declared **C1 calibration** (lowest owned axis, score 2): close round-83 routed
D1–D4. Declared **C2 freshness** (score 10): acquire policy-header value semantics.
**Honest stop: C2 unprovable**, despite a green frozen counting command. No
capability credit and no post-score narrowing to syntactic equivalence.

- Frozen contract/counters/controls landed `f358022f7e1b2f3846be8ceacbe3a7ef22edf4be`;
  base `fe42ad11eb1084ad2ea68d12c5bbb2922a089868`. Contract:
  `.ufo/waves/round-84/contract.md`.
- C1 repairs: real RFC headings, full-span 66-word correction, one settled
  connector (`ConnectorSibling`), committed start census. Evidence:
  `corpus/lessons/round-84.md:36-47`; `controls/after-c1.txt`.
- C1 instrument defect: frozen v1 omitted D3/D4 prose checks; ReviewC1 also
  demonstrates split D1 lines, non-string output and loose receipt tokens.
  Separate diagnostic v2 repairs only the two prose checks (10/10 selftest),
  without replacing the frozen counter. See `w1/ReviewC1.md` and
  `controls/after-c1-v2.txt`. Actual prose conjuncts are present.
- C2 tool runs offline over retained captures and synthetic pairs. The real
  pair has zero policy changes; controls have three and one. **Semantic
  rejection:** the frozen Referrer-Policy list reorder can change the last
  recognized policy. Evidence `w1/ReviewC2.md`, lesson Integration verdict,
  knowledge-entry appended warning. The frozen expectations are unchanged.
- New field-specific equivalence QUALITY criterion has that failing witness;
  `corpus/QUALITY.md:1703-1710`. Do not use the experimental tool to waive
  policy drift or authorize publishing.
- Wave shape: one validated v1 wave, 13 seats: scout 2, executor 3, scribe 3,
  reviewer 2, critic 1, mutation-tester 1, connector 1. All 13 settled with
  nonempty outputs; attack 4/13 = 30.8%; no replacement, residual call or
  dead seat. L1 held planner; ScoutRecon carried bounded data-walk.
  WAVE-DONE received before report. Evidence: `w1-spec.json`,
  `w1-dispatch.json`, `w1-results.json`, `w1-accounting.json`.
- Mutation evidence: five mutants killed by combined detection, one guarded
  equivalent; frozen selftests alone kill 3/6 and leave two substantive
  integration gaps (`w1/MutC.md`). Canned output/input-dependence and imported
  table enforcement remain disclosed; no green test overrides those findings.

All wave-relative paths above are under `.ufo/waves/round-84/`.

## Landed changes

Each row is logged at `LOG.md` §Round 84 (lines 2770 onward).

| Change | Landed commit |
|---|---|
| Contract, counters, synthetic pairs, base/junk/selftest/start census | `f358022f7e1b2f3846be8ceacbe3a7ef22edf4be` |
| Validated spec/dispatch/ready evidence | `87cbfd99b677a330c14a68a33f10548f15e6e10c` |
| Tool, knowledge, S457, lesson, QUALITY, wave evidence, v2 diagnostic | `b05c390135302c44415b021fd0c0723b3f58d45e` |
| Pinned measurements, SCORECARD and LOG | `c5d89c086ad1f427e40090688fa85ac2aba5dfcf` |

Final lane hash `c5d89c086ad1f427e40090688fa85ac2aba5dfcf` was printed by
`git -C /home/vgpnk/Projects/shokunin/kake-shokunin ls-remote origin refs/heads/master`.
No inherited uncommitted lane files were present at round open.

## Before → after measurements

Measured carrier `b05c390135302c44415b021fd0c0723b3f58d45e`.

| Claim | Counting command (lane root) | Before | After / verdict |
|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-84/c84_defect_queue.py --root . --revision <rev>` | frozen worktree receipt open=3 closed=1, exit 1; start census already fixed D4 state | carrier open=0 closed=4 met=true, exit 0; delivered repairs, qualified instrument |
| C2 | `python3 -B .ufo/waves/round-84/c84_policy_values.py --root . --revision <rev> --work /fast/scratch/hyaku/kake-r84/closure` | no tool, met=false, exit 1 | carrier declared=3 receipts_ok=1 real_changed=0 ctl_changed=3 ctl_mismatch=0 eq_changed=1 eq_mismatch=0 record_equal=1 determinism=1 selftest_ok=1 met=true, exit 0; **unprovable semantic claim** |

Exact stdout/exits: `controls/base-c84-defect-queue.txt`,
`controls/base-c84-policy-values.txt`, `controls/after-c1.txt`,
`controls/after-c2.txt`. Diagnostic v2 at freeze open=4 → carrier open=0;
`controls/base-c84-defect-queue-v2.txt` and `controls/after-c1-v2.txt`.
Frozen selftests 8/8 and 4/4; tool selftest 15/15. Scores unchanged.

## Sources & frontier

Registry **194 → 195 rows** (spacing-tolerant row count command:
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
Added tier A=1, B=0, C=0; **S457**, mined, fresh 2026-11-04 HTTPWG RFC 9111
HTML retrieval, 178573 bytes. Existing mutable cells unchanged. Row S457
cites only the new entry. S456 and S457 are explicitly two renderings of one
RFC, not independent corroboration. Source selection also avoids the frozen
D4 mutable-census coupling; counterfactual .txt append produces W04=23.
Evidence `w1/ScoutSources/row-anchor-check.txt`, lesson Gate/Risk.

Census command both times:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.

Before (exit 0):
```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	W04	S433 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S445 duplicate url html.spec.whatwg.org/multipage/links.html across scopes
kake	W04	S450 duplicate url html.spec.whatwg.org/multipage/semantics.html across scopes
kake	W04	S451 duplicate url www.rfc-editor.org/rfc/rfc3339.txt across scopes
kake	W04	S453 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S454 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S455 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
census_exit=0
```
After (exit 0):
```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	W04	S433 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S445 duplicate url html.spec.whatwg.org/multipage/links.html across scopes
kake	W04	S450 duplicate url html.spec.whatwg.org/multipage/semantics.html across scopes
kake	W04	S451 duplicate url www.rfc-editor.org/rfc/rfc3339.txt across scopes
kake	W04	S453 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S454 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S455 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
census_exit=0
```

Sources re-opened GET-only: rfc-editor RFC 9111 text and HTTPWG HTML;
receipts and located ≤25-word quotes retained under `w1/ScoutSources/`.
Gate admits bounded source facts, rejects unsupported universal reorder
semantics and oversized/mislocated anchors. The semantic frontier is **not**
advanced to core. No live property re-captured, no publish/deploy.

Assimilation: none. `considerthese/2026-10-26.md` read; no new proposal
implemented. Connector's sibling/package collision scan is retained in
`w1/ConnectorSibling.md`; source repo untouched.

## Trend verdicts

- **expansion: unchanged** — no admitted semantic capability; experimental
  entry explicitly warns of the counterexample.
- **quality: improved** — routed corrections and a marked semantic limitation,
  not an unmarked false claim; lesson and knowledge appended warnings.
- **discernment: improved (author-side, closure owed)** — rejection becomes a
  grounded QUALITY criterion with a failing witness; no outside admission is
  asserted for lane-dispatched reviewers.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
showed orchestrator `.scratch/` files and unrelated `after`; no identified
round-84 seat misroot, none removed. Stale-lane: only this round owned.
Open L0 questions unchanged; no new decision required to report honest stop.
No tools installed/upgraded; pacman untouched. Load-order deviation: swarm
binding/tool rules were read after dispatch; no claim of full procedural
conformance. Shared-checkout writers had disjoint ownership, not separate
worktrees; this too is a conformance deviation, not a concealed pass.

Self-evaluation: accuracy 3 (frozen semantic counterexample); completeness 4
(deliverables landed, admission deliberately withheld); clarity 4 (frozen
versus diagnostic instrument explicit); actionability 3 (experimental tool
must not approve publishing); conciseness 3 (large evidence record). Overall
3.4/5. Highest improvement: field-specific semantics before freezing a claim.

## SHONEN

- [~] Decision tables/error patterns/checklists — `SHONEN.md` box 1 and
  `corpus/knowledge/shonen-ledger.json`; no new non-author verification.
- [ ] End-to-end domain task — existing box-2 gap remains; no publication.
- [~] Executable instructions — `SHONEN.md` box 3, experimental-tool caveat
  above; no new promotion verification.
- [~] Domain boundary — `PROVINCE.md`; connector overlap report; no promotion.
