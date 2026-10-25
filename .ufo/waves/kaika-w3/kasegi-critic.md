# kaika W3 critic — kasegi round 22

**Recommendation: ADMIT both claims, qualified as below.** I found no non-fixable trade, scope bleed, fabricated source quotation, or history loss. The strongest counterexamples are limits on what the measured changes prove; keep the numeric axis assessments held and record this outside spot-check in the lesson before finalizing the discernment trend.

## C1 — depth:verifiability / provenance disclosure

**Counterexample.** Provenance headers and runnable commands do not restore or verify the underlying lost-source chains. The accepted description is *disclosure*: most legacy records remain explicitly non-re-verifiable, not newly verified. The current resolver still marks the old material gone, so this is not a verifiability-score increase.

**Evidence.** Re-ran the `SCORECARD.md:336` header-presence loop against the 25 base knowledge paths and the same paths in the `c8b719d` archive: `source`, `verified-at`, and `recheck` each measured 0/25 → 25/25. Re-ran `SCORECARD.md:337`: 23 rechecks exit 1 and two exit 0. The 23 start with absent-base guards (`test -d`); `test -e` on `~/Projects/bounties`, `~/Projects/the-bounty-hunter`, and `~/Projects/origin-work` reports all three absent. Thus those failures are honest fail-closed results, not source re-verification.

Re-ran the line-339 prefix comparison: 25 files reported zero non-prefix lines; line 340's `grep -c 'r22 correction' … | awk …` returned 31; line 341's presence-wording sweep returned 8 on the base archive and 5 after. I inspected all five residual hits: `citation-bases.md:35` says “live repo while it stood”; the `root-loss`/`source-tree-loss` hits are dated historical observations; the `ufo-fsd-alpha` hits are explicitly relocated; `ufo-workspaces.md:287` is within a census labeled at lines 3–5 as verified 2026-09-28. None asserts an unsupported current state.

Re-ran `python3 corpus/instruments/resolve.py .` in scratch base/after archives: base `skill=32/506 corpus=140/1212 all=156/1539`; after `skill=39/513 corpus=187/1259 all=203/1586`; internal citations 146→193 and GONE 1383→1383. The 47-point all-total increase is INTERNAL, not restored source resolution. Re-ran `python3 corpus/instruments/anchorcheck.py SKILL.md` in both archives: identical 7 in-range, 0 bad, LOST-RECORDED=306, PIN-BROKEN=0.

**Impacted axis:** depth:verifiability only; no freshness or source-truth gain. **Smallest safe correction:** retain the claim only as provenance/status disclosure and keep the axis score held; do not describe the 23 failing rechecks as verification. This is already the stated scope and the score is held in `SCORECARD.md:327`.

**Verdict: ADMIT (qualified).** The append-only status and unchanged anchors are real improvements to auditability, but no lost claim is verified.

## C2 — coverage / frontier expansion; `sources-registry` capability

**Counterexample.** The new public-practice topics expand the knowledge frontier, but they do not restore the absent domain-root surfaces in the lane's existing coverage measure (`SCORECARD.md` measurement proxy; `AXES.md:12`). The map count 25→33 is not itself a coverage measure: the added rows include the pre-existing but unindexed `citation-bases.md` entry and the new `QUALITY.md`/`SOURCES.md` records, as well as the five new topic entries. The round correctly held the axis score and did not adopt the proposed denominator; do not retroactively credit the extra map rows as surface coverage.

**Evidence.** Re-ran `SCORECARD.md:343-346` from archive snapshots: admitted F01–F05 0→5; coverage-map rows 25→33; Province Core/Frontier/Adjacent headings 0→3; SOURCES rows 27. The five new knowledge files exist and their F01–F05 paths/source IDs match the registry. No denominator change was applied. The additions remain inside bounty/security research: the AI entry applies reproduction, impact, reachability, and independent review to claim evidence; it does not take over Kengaku's model/benchmark evaluation province.

Reopened sources for every admitted topic in the sample: FIRST CVSS guide/specification (S001–S002), CISA CVD guide PDF p. 6 (S003), HackerOne FAQ “How to Enable Safe Harbors” (S006), NCSC question 7 (S009), Anthropic “Open-source software” (S012), and MITRE methodology “Removal of CWE Mapping Normalization” (S013). The sampled quotes match their anchors. FIRST says “CVSS Base (CVSS-B) scores are designed to measure the severity of a vulnerability and should not be used alone to assess risk” (S001; entry quote `corpus/knowledge/cvss-v4-severity-and-vector.md:25`, anchor and URL `corpus/SOURCES.md:7`). The CISA timeline quote is recorded at `corpus/lessons/round-22.md:79` and occurs on PDF p. 6. These support bounded reporting rules, not broader authorization or guaranteed model performance.

I also reopened both rejected sources. CISA's page states “Gold Eagle lets organizations report, validate, and track AI-related vulnerabilities at scale” (S026; quote and location `corpus/lessons/round-22.md:102-103`, source URL `corpus/SOURCES.md:32`, *How Gold Eagle Works*); its linked PDF describes ingestion/validation/deduplication but supplies no checkable general procedure/results, so the C-tier rejection and flip-condition stand. HN S027 exposes only a title/link (`corpus/SOURCES.md:33`); the Medium destination returns HTTP 403. Its rejection is sound.

Re-ran the contract's seven census commands (`SOURCES-CONTRACT-v1.md:66-80`): 27 rows; malformed 0; tiers A=25/C=2; statuses mined=15/queued=10/rejected=2; duplicate IDs, enum/tier inflation, and missing mined `used-by` paths all empty. The supplied `sources-census.sh validate <snapshot>` also printed `ok`. Structural census cannot prove a source was opened or a quote semantically supports a claim; the gate quote records plus the reopened admit/reject sample address that gap. There is no row padding or tier inflation in the checked sample.

**Impacted axes:** coverage/expansion; no depth:density harm. **Smallest safe correction:** report the accepted move as five source-backed frontier topics (expansion improved), keep the existing coverage score/denominator unchanged, and do not use the 25→33 map-row count or new denominator proposal as surface coverage. This is a measurement-description correction, not a trade requiring rejection.

**Verdict: ADMIT (qualified).** Five new entries and the demonstrated registry capability are real; coverage-score movement is not established by the existing domain-root denominator.

## No-harm and outside spot-check

Re-ran `python3 corpus/instruments/density.py SKILL.md --label <base|r22>`: mean 154.0 on both snapshots; the 18 prior blocks retain their measured values and the new block is 155.6. Together with the identical anchorcheck above, no depth:density or anchor harm was observed. The sampled admits and rejects are supported; record this W3 agree/reasons result in `corpus/lessons/round-22.md` before closing the outside discernment check, which the report currently leaves pending.