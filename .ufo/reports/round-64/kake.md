# Kake — round 64 (attempt 2)

## Work performed

Declared claims (unchanged from inherited freeze): **C1 calibration** — repaired semantics-binding counter verifies S432 resolution; **C2 operability** — quote-tool gate rejects the canned stub; **C3 freshness** — standing offline §paths gate evaluates again. C1 works the lowest owned non-retired axis (2). **Honest stop: C1 unprovable; C2 and C3 measured met.** Scores hold calibration 2, operability 10, freshness 10; no numeric increase.

- Reused frozen build `4c8295fa5e3b628f1fdf3840299ae415c01849fb` and receipt commit `cc8add1fa740b920ea5179a71152680ab220c70c`, contract `.ufo/waves/round-64/contract.md`. No frozen instruments, predicates or receipts were rewritten or discarded.
- Integrated the inherited validated v2 w1 after **Main WAVE-DONE: all 65 seats settled**. Evidence `.ufo/waves/round-64/w1-spec.json`, `w1-dispatch.json`, `w1.ready.dispatched`, `w1-results.json`, and 62 scoped reports; committed `8b1ddae586c3b187dc41998dd3e2b0a83e537ec9`. No duplicate dispatch; inherited ready owner remains KakeR64, successor KakeR64a2.
- Wave shape: one v2 wave, 65 total; scout 10, executor 15, reviewer 16, critic 6, mutation-tester 5, connector 2, sentinel 1, simplifier 1, revenger 1, scribe 8. Attack roles 27/65 (41.5%); L1 holds planner under validator exception. No residual/replacements. Three no-report seats counted dead/no-credit: CriticExploratory, MutC2Counter, ScribeMistakeClass. Handoff has no id/status/last-error fields: cause unknown; MutC2Counter partial text mentions an eval deadline, not a finished matrix.
- Applied C1's frozen kill rule: authentic source pins plus token-only/contradictory prose still green (`w1/ReviewerC1Prose.md`), as does a hidden criterion (`w1/MutC1Prose.md` Q3x). No calibration credit; frozen counter retained. `w1/RevengerC63Defect.md` corroborates provenance survivors.
- Appended source-quote, census attribution, chronology and seven-cell delta corrections; grounded QUALITY criteria and SKILL limitation; bounded classifier capability row in SCORECARD. Evidence `corpus/lessons/round-64.md` §Attempt-2 evidence corrections / §Wave settlement; `LOG.md:2269-2278`.
- Cross-domain boundary: concrete tools are lane-owned; generic verification method belongs to chousa/tameshi, browser effects to tabi, publication to operator (`w1/ConnSiblingOverlap.md`). No domain source tree modified or pushed.

## Landed changes

All paths below are lane-relative. Every item is tied to `LOG.md` Round 64, lines 2269–2278.

| Commit | Changes |
|---|---|
| `4c8295fa5e3b628f1fdf3840299ae415c01849fb` | Inherited frozen C1/C2 counters, fixtures, contract, controls; seven sidecar line-cell repair; initial lesson/QUALITY/SKILL rows; source re-open receipt |
| `cc8add1fa740b920ea5179a71152680ab220c70c` | Inherited T0 after receipts for C1/C2/C3/census |
| `8b1ddae586c3b187dc41998dd3e2b0a83e537ec9` | Settled wave evidence and reopened live body; append-only lesson/QUALITY/SKILL limitations; LOG and SCORECARD verdicts/capability row |
| `9e798798c884961d9f17f13320d11db7ee9e4282` | Integrated measurement receipt `controls/after-final.txt` and LOG measurement pointer |

Final lane hash **`9e798798c884961d9f17f13320d11db7ee9e4282`**, landed via jj-lane.sh. Required `git -C /home/vgpnk/Projects/shokunin/kake-shokunin ls-remote origin refs/heads/master` printed that hash. Final receipt-only commit does not claim a fresh full-tree measurement; integrated measurements name `8b1ddae5` explicitly.

## Before → after measurements

Base `1a48131577ba82c967650561be34e8dba909432a`; initial measured T0 `4c8295fa5e3b628f1fdf3840299ae415c01849fb`; integrated measured revision `8b1ddae586c3b187dc41998dd3e2b0a83e537ec9`. Receipts under `.ufo/waves/round-64/controls/`.

| Claim | Counting command | Before → after and verdict |
|---|---|---|
| C1 calibration | `python3 -B .ufo/waves/round-64/c64_calibration.py --root . --revision <commit>` | base lesson_gate=0 unresolved=1 met=false exit 1 → T0/integrated lesson_gate=1 unresolved=0 met=true exit 0, pins=1 recipe_rederive=1 located=6150-6154. Four declared controls met=false exit 1. Counter selftest 26/26. **Unprovable**: wave marker-only greens fire the frozen kill rule; measured green is not admission. `base-c1.txt`, `after-c1.txt`, `after-final.txt`; `w1/ReviewerC1Prose.md`, `w1/MutC1Prose.md`. |
| C2 operability | `python3 -B .ufo/waves/round-64/c64_quote_tool.py --root . --revision <commit>` | Same canned stub: c63 met=true exit 0 → c64 tool_sha=mismatch met=false exit 1. Real T0/integrated tool_sha=ok selftest=4/4 frozen_cases=ok rederive=agree met=true exit 0; counter selftest 11/11. **Measured met**, bounded to frozen tool sha/four cases. Base real tool already exists and already greens; the frozen claim is the stub differential, not tool introduction. `stub-c63-defect.txt`, `stub-c64.txt`, `after-c2.txt`, `after-final.txt`; `w1/ReviewerC2ShaPin.md`. |
| C3 freshness | `node scripts/freshness-sweep.mjs --offline` in archive of measured revision | Base exit 2 `paths sidecar binding invalid: SKILL.md:364` → T0/integrated `VERDICT: OK (exit 0, partial: offline)`, drift 0. **Measured met**, with separate frozen permitted-diff proof: exactly seven line cells changed; hashes and 30-entry roster unchanged (`w1/ScoutSidecarDiff.md`). `sweep-before.txt`, `sweep-after.txt`, `after-final.txt`. |

C3's raw exit-0 discriminator has a known bypass: selectively deleting seven stale entries greens the sweep (`w1/CriticClaims.md`). That fixture violates the contract's pre-existing permitted-diff condition, so is not an admitted repair; no predicate was changed after data. Remote §armed checks remain skipped and §history suspended, complete=false. This is not live publishing readiness.

No blanket no-harm assertion: c60 gate-status replay reports one mismatch, c56 selftally live row red (`w1/ExecC63Regression.md`). Causation is unproven; this remains an unresolved standing-gate defect. Corpus/source preservation audits pass within their scoped diff (`w1/ExecAppendOnly.md`, `w1/ReviewerNoHarmCorpus.md`). Other carried defects: missing ledger-mut fixture builder; one-sided outside-verdict binding; C2 unhashable-id helper gap unreachable behind frozen tool sha. Frozen instruments are not patched post-score.

## Sources & frontier

SOURCES **171 → 171**: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, independently reproduced at base and T0 in `w1/ScoutCensusState.md` / `w1/ExecCensusCommands.md`. Tier totals A=148 B=6 C=17; status mined=141 queued=8 rejected=22. Added by tier A/B/C: 0/0/0. Registry row/cell touches: none, so old→new none. Frontier rows advanced: none. Capability re-entry is held-ground tool operability, not new frontier knowledge.

Sourced claim C1 cites **S432**, reopened 2026-10-30 at https://fetch.spec.whatwg.org/ (200, 1,854,393 bytes, sha256 `63b0a018753c330adf1e40417524eb70ea02d4d3e123bcb39b6770f23bad911b`, identical retained raw body). `sources/receipts.json`, `sources/S432.live.html`; Gate records URL/date/location. Original short quote was normalized, not verbatim; appended correction retains apostrophe/backticks and distinguishes field purpose from the row's exact-value rule (`corpus/lessons/round-64.md:136-146`, `w1/ScoutS432Reopen.md`). No new row was written.

Assimilation: none. Considerthese proposal 5 rejected as duplicating the existing historical-gate registry/c60 counter, with flip condition recorded in Gate; no operator input edited. Source package remains read-only/staged. Mistakes and demonstrated fix: sidecar binding exit 2 → seven-line repair exit 0; marker-only/provenance survivors honestly retained as unresolved, not claimed repaired.

Census command both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`

Before output (`controls/census-before.txt`):
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
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
census-before-exit=0
```
After output (`controls/census-after.txt`; integrated replay in `controls/after-final.txt` agrees):
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
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
census-after-exit=0
```
Both exit 0; 16 W04 warnings unchanged. Validation output does not print 171; that count belongs to the separate row-count command above.

## Trend verdicts

- **expansion — improved, bounded:** standalone retained-span classifier capability row re-enters SCORECARD after real tool selftest and stub-proof differential. No new knowledge/frontier coverage.
- **quality — improved, bounded:** §paths evaluation restored and C2 stub denied; stronger pins/recipe chain genuine. C1 semantic sufficiency is explicitly unprovable; no complete corpus-clean claim.
- **discernment — unchanged pending outside round-64 review:** lane-owned wave exposed its own false greens and produced grounded criteria, but dispatched seats are not outside verification. Round-63 outside agreement is not round-64 agreement.

Stale-lane: respawn-per-round mission; inherited work progressed and is now landed; no other kake mission is open. Three no-report seats receive no independent credit. Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only tracked operator `.scratch/goal-20261029-hyaku-run12.md` and shared L0 modifications, no untracked misroots; neither touched. No tools installed/upgraded; no pacman transactions. Open L0: round-59 calibration-ownership question remains unanswered; no ruling inferred. Handoff status/last-error defect remains orchestrator-owned.

Self-evaluation: accuracy 4 (frozen counter limitations disclosed); completeness 4 (three absent seat reports and unresolved standing-gate red retained); clarity 4 (full census retained for contract); actionability 4 (exact future controls named); conciseness 3 (required audit evidence is long). Overall 3.8/5. Highest improvement: next freeze must reject token-prose/outside-verdict controls and ship replayable ledger-mut construction. User agreement expected on honest-stop disclosure, not on admitting C1.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged; no promotion claim (`SHONEN.md:5`).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — unchanged; this round is bounded instrument maintenance (`SHONEN.md:6`).
- [ ] Instructions executable by an agent without oral context — unchanged; no non-author promotion verification (`SHONEN.md:7`).
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — unchanged; boundary scan is lane-side, not promotion authority (`SHONEN.md:8`, `w1/ConnSiblingOverlap.md`).
