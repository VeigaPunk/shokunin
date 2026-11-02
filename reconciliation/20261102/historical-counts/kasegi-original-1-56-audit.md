# Kasegi original rounds 1–56: documentary completed-attempt reconciliation

Audit date: 2026-11-02. Read-only historical reconciliation, **not fresh replay certification**, admission, promotion, or new training credit. No repository program, instrument, gate, target probe, provider call, publication, or live-lane edit was performed. Only pinned Git object reads and local audit-artifact creation were used.

## Result and counting boundary

- **39 directly supported substantive completed-and-independently-reviewed round labels:** **1, 4, 5, 20, 22–56**. This includes honest rejections and harmed/rejected work; it is not a success count.
- **3 additional older labels have substantive work plus an independently pinned whole-tree corpus disposition:** **11, 14, 19**. Under the older corpus-review regime these support a **42-label documentary count**, but the surviving review is not a complete per-round claim adjudication. Keep this narrower scope attached to the number.
- **11 further labels contain real work and/or detailed author-side review reports but lack a securely attributable independent terminal per-round pointer in this inspection:** **3, 6, 7, 8, 9, 10, 12, 13, 15, 17, 18**. These are custody gaps, not fabricated-work verdicts. They could bring the supported original-label total to **53**, but cannot presently be silently included in the strict count.
- **3 labels excluded:** **2** (no original work/report/lesson/round commit found), **16** (explicit closeout marker, in-flight work deferred), **21** (blocked before required dispatch, no outside review, explicit zero verified-round credit).

Thus the conservative documentary range is **39–53 original round labels**, with **42** supported if the three explicitly bounded historic whole-tree dispositions satisfy the user's historical-regime criterion. **53 is an unresolved ceiling, not a certified count.** Modern rejections must not be subtracted merely because they are not admissions. Conversely, a closeout marker or undelivered dispatch is not a substantive reviewed attempt.

This is one count per original label, not an assumption that one label equals one invocation. Retry/restart evidence exists (notably 23, 34, 40, 42, 46, 48); no extra count was assigned to subsidiary attempts without their own separately bound substantive work and terminal independent disposition. Consequently 53 is a ceiling for the original **label inventory**, not a mathematical upper bound on recoverable distinct attempts. R17 also has a later reused-label continuation; it is explicitly not an extra verified round.

## Immutable custody and navigation

All lane paths below are relative to:
`/workspace/scratch/e2fdad13233f/shokunin-training/lanes/kasegi`

Pinned original lane tip: **`eae1d614542e8d30d77e9f4e8b9dea6a11aad138`**.
Seed ancestor: **`aeddcd2ec1244befef8b13667e511f817639154d`**.

All fleet paths below are relative to:
`/workspace/scratch/e2fdad13233f/shokunin-training/reconciled/shokunin`

Pinned fleet snapshot: **`ec723da5373b02351ca61d2b3f4f482529332f5e`**. Only original 1–56 artifacts and relevant older aggregator/audit records were inspected; cloud57 onward were not adjudicated here.

Machine-readable artifacts:
- `audit/kasegi-historical-round-inventory.json`: 56 rows, classification, original-ancestry work commits with **full hashes**, frozen claim paths, report/lesson/review paths, Git blob IDs and last-touch commits.
- `audit/kasegi-historical-navigation.json`: exact source repository/revision/path/blob/last-commit for every exported document.
- `audit/kasegi-historical-navigation/`: pinned readable document copies. The odd directory names `lane-` and `fleet-` are navigation prefixes, not repository names.

Every work commit in the inventory was obtained from `git log <original-tip>` (therefore reachable from the pinned original tip); existence does not itself prove that the work passed review. Review source identity is documentary: explicit non-author reviewer declarations and provenance in committed artifacts, not a new authentication of historical humans or provider identities.

## Older rounds: actual work, review custody, disposition

`F<n>` denotes fleet `.ufo/reports/round-<n>/kasegi.md`; `L<n>` denotes lane `corpus/lessons/round-<n>.md` where present. Full work hashes and all blob pins are in the inventory, avoiding reliance on abbreviated hashes in old prose.

| Round | Actual work/custody | Independent disposition and count treatment |
|---|---|---|
| 1 | Two original work commits; grounded skill and five knowledge entries; F1/L1 | `corpus/lessons/round-1-aggregator-audit.md`: non-author aggregator plus independent reviewer, cited commands re-executed, **conformant/pass with concerns**. Count. |
| 2 | No F2, L2, or original round-2 work commit found; original LOG jumps 1→3 | Aggregator-r6 explicitly calls README's implied round-2 lesson nonexistent. Exclude; do not fill the number gap. |
| 3 | Claim gate inventory, VDP corpus and sibling-package sampling; F3/L3; `e73b2b54d8261c34a23ac950255a428113028494` | Aggregator-r3 says report/full corpus read but directs next delta audit; no isolated terminal r3 review bound here. Custody gap. |
| 4 | Ledger/evidence-store censuses; F4/L4; two original commits | `round-4-aggregator-audit.md`: explicitly audits r4 delta, 18 numeric claims reproduce, **NOT CONFORMANT** on two major formal failures. Count reviewed failure. |
| 5 | Mission-control plane census and dispatcher study; F5/L5 | `round-5-aggregator-audit.md`: explicitly pins r5 delta; independent reviewer plus L1 adjudication; **NOT conformant**, two false-at-write-time majors plus carried defect. Count reviewed failure. |
| 6 | Retirement/autopsy classifier study; F6/L6; `d31f4ca9a1b1dc435f6fa820caef120e272683b7` | The similarly named **aggregator round-6** audit actually pins lane r11 with dirty r12 work. Do not mislabel it as a terminal lane-r6 review. Gap. |
| 7 | Ops tail and wrapper study; F7/L7; `4ff0296c164e6954d4c98ac7541f885d94950b02` | Later aggregate coverage is not an isolated terminal r7 disposition. Gap. |
| 8 | Archived fleet snapshot study; F8/L8; `585fec817ea448560a755c8684cf08283bd608c5` | **Aggregator round-8** cold run is later lane-r13/r14-era evidence, not lane-r8 closure. Gap. |
| 9 | Submitted registry/receipt study; F9/L9; `c80c2a177794bd2f553f9638b89b2cb5ba372562` | F9 names reviewer confirmations and recovered critic output; raw independent custody not established here. **Aggregator round-9** audits later r14/r15-era state. Gap. |
| 10 | Operator queue audit; F10/L10; `04f9527aa33bb569433080fc7c7aa6ef97577be6` | Work preserved, independent terminal round pointer unresolved. Gap. |
| 11 | Intake surface/map/registry study; F11/L11; `fb9ac8e894071480e31f6ed37782d911131de3ce` | Aggregator-r6 report and lane `round-6-aggregator-audit.md` pin this HEAD, independently re-execute claims, **NOT CONFORMANT**. Bounded whole-tree review support, not every r11 claim replay. |
| 12 | Runtime layer, Git state, target checkouts and citation repairs; late commit `fc6d398d5cacfcedc19a6bbaa0cc9bc475c5f735` | F12 reports 74-citation independent L2 audit (64 OK/9 defects); surrounding aggregate review included worktree r12 content before commit. Exact final independent review custody remains unresolved. |
| 13 | Full citation audit and fact repairs; `7483333d90e93dac09b64b76c928f5e46af384d5`; F13/L13 | F13 explicitly rejects degraded/fabricated reviewer narration and retains artifacts cautiously. Aggregator box-3 cold run pins r13 HEAD but dirty r14 content and remains provisional. Do not use that provisional mixed-state review as clean r13 closure. |
| 14 | Thin-cohort repair and sampling; `b7180b0303755212ea4b60e52152aa8bf010c5b0`; F14/L14 | `round-9-aggregator-corpus-verdict.md` explicitly measures landed archive at this revision and emits failed CORPUS rule table. Bounded whole-tree disposition support; promotion/box-3 remains provisional/could-not-evaluate. |
| 15 | Root-loss re-anchor and instrument work; `eb5b5902a4f20373eaebe0671b26a4296dcdb584`, annotation `0f2dca09b3eedcd1da090a23c8aa38ea64b1d3d6`; F15/L15 | Detailed 15-seat author report, self-rejections and root-loss evidence. Aggregator report mentions re-emission at 0f2dca0, but surviving lane verdict body remains pinned b7180b0 and marks r15 provisional. Do not count same review twice absent exact final counterpart. Gap. |
| 16 | F16 is explicitly **closeout (marker)**: operator stops long run, in-flight work left for next round | Exclude. No completed substantive independent review established. |
| 17 | F17 and original LOG describe confined ORIGIN checker and ten returned L2 reviews; later LOG continuation reuses r17 | Original work is folded into later ancestry rather than a clean original-r17 subject commit. Later `d43e63c8872c4029c7edb9067d8f272642e7885a` is after r20 and is explicitly inherited durability, not another verified round. Original round review custody gap; no duplicate credit. |
| 18 | Broad anchor triage, resolver repairs and corpus rewrite; `ed44a923e465c3cf509898a26a6c6fe082df6851`, 33-file commit; F18 describes nine independent read-only seats | Raw reviews cited under historical `/tmp/kasegi-r18/`; independent terminal artifact not established here. Gap, not no-work. |
| 19 | Real second-root-loss recensus commit `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`; no F19 | Fleet `.ufo/waves/aggregator-r11/seats/corpus-verdicts.log` pins exact revision with dirty=0 and 55 findings; aggregator-r11 report adopts failed corpus verdict. Bounded whole-tree support despite missing report. |
| 20 | `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` plus three audit/erratum commits; F20 and `round-20-recensus.md` | Five independent Kasegi audit seats in fleet `shokunin12h-20261014-p1-audit/members/`; GateRerun independently agrees on anchor/density and falsifies final-census wording; RecordConformance names broken foreign-history/path bindings; lane appends audit errata. Count completed measured/reviewed recensus, **not clean success or promotion**. |
| 21 | Blocked routing authority audit, inherited resolver evidence and errata; lane lesson/report | `round-21-routing-blocked.md`: required wave never dispatched, outside spotcheck not performed; gate exit1/11 failed requirements/zero verified-round credit. Exclude. |

## R22–56: terminal independent review evidence inspected

For **each** row the independent source is lane
`corpus/lessons/round-N-verifier-spotcheck.md` at the pinned lane tip. F<N> supplies work/report counterpart; frozen claims and corresponding full-hash work commits are individually inventoried in JSON. These are substantive review bodies with counters, adversarial decisions, source checks or measured misses, not heading-only confirmations.

| Round | Terminal review substance / outcome |
|---|---|
| 22 | C1 wrong-axis nonmove; C2 five frontier entries and source registry verified; **rejected-honest-stop**. |
| 23 | Detector soundness improved and F06–F08 verified; independent admit/reject source sampling; attempt-label mismatch noted, no extra attempt counted. |
| 24 | Frontier rechecks and F09 verified; statutory false generalizations independently rejected; both owned axes improved. |
| 25 | Executable recheck move and F10 verified; sourced vendor-crosswalk rejection reproduced; both axes improved. |
| 26 | Expected-list/gate conformance plus F11 verified; frozen tally/receipt caveats routed. |
| 27 | **Substantive honest stop:** pre-freeze C1 fixtures built AND executed; incorrect MISSING-FILE premise falsified as BASE-ABSENT (M27-1); before receipts independently reproduced. No specialist wave/no implemented after-state, but not a mere plan. **rejected-honest-stop**, count attempt. |
| 28 | Anchor gate soundness and F12 verified; source snapshot binding and two staged-package rejections checked. |
| 29 | Selftest completeness/hermeticity and F13 verified; counters independently re-run; form defects status-neutral. |
| 30 | Three claims verified; missing initial LOG and stale prose routed, not absence of work. |
| 31 | Thirteen load-bearing limbs and F15 verified; 3 weak rows/2 tamper probes disclosed. |
| 32 | **rejected-honest-stop** with 25 committed capture/control files and 3650 insertions; independent before/after shows no implemented claim; captures and fake-control receipts checked. No dispatched seats does not erase substantive measured work. |
| 33 | Capture-binding and F16 verified; ledger counts and source admission independently checked. |
| 34 | Nine-defect closure suite and F17 verified; two frozen-rule survivors killed; attempts1/2 consolidated, not double-counted. |
| 35 | **rejected-honest-stop**: both frozen kill rules fire at judged revision; missing capture and registry rows landed after completion and cannot retroactively change verdict. |
| 36 | Nine routed closure-order defects and F19 verified; later wave-evidence-only commit distinguished from judged head. |
| 37 | Routed-defect suite and F20 verified; final-head receipt omission and province defect routed. |
| 38 | C1 **NOT VERIFIED**, frozen `closed=7/8 exit1`; C2 F21 verified. Independently completed adverse adjudication; not all-claims success. |
| 39 | C1 **NOT VERIFIED**, `7/8 exit1`, selftest failure; C2 F22 verified with three recorded source refusals. Completed adverse adjudication. |
| 40 | C1 kill rule fires; C2 verified; explicit **rejected-honest-stop**. |
| 41 | C1 10/12 and six selftest failures; C2 counters met but genuine sibling-owned RFC9116 overlap independently confirmed; both claims **NOT VERIFIED**, no harm. |
| 42 | Attempt3, extensive independent export-mode falsification; claims verified, final addendum says **admitted:true stands** with RD42-1..9 routed. Earlier attempts not separate credit. |
| 43 | C1 19/19 and C2 verified; unbacked composite summary distinguished from established limb evidence. |
| 44 | Eight routed fixes and frontier move verified; frozen-counter defect named rather than concealed. |
| 45 | Frozen claims individually re-derived from artifacts plus committed gate evidence; owned axes improved, no harm; source admits/rejects independently checked. |
| 46 | Final §9 reconciliation supersedes earlier admission: **rejected-harmed**, expansion/quality trade under canonical clause. Claims' measurements stand; completed reviewed attempt remains. Operator ruling required only for subsequent admission, not to make existing rejection terminal. |
| 47 | Refused harmful limb and unmet frontier target; **rejected-honest-stop** independently confirmed. |
| 48 | Restored checklist form predicate verified; nominal/nonmoving owned-axis measure disclosed; final closure **admitted**, no promotion. |
| 49 | Citation-ground class 68→0 and F30 verified; report's unmeasured claim corrected; rejects/owned-axis holds documented. |
| 50 | Census-freshness capability and replacement C2/F31 verified; EPSS duplicate refused; **admitted** with two routed defects. |
| 51 | Three claims and carry-in corrections independently verified; negative mirror-identity decision checked; **admitted**. |
| 52 | Quote-audit capability, corrections and F33 independently verified; self-catch and final green state checked; **admitted**. |
| 53 | Equality-limb repair and F34 verified; nominal score label retained; **admitted**. |
| 54 | Figure-audit capability and F35 verified; two numerical-prose defects status-neutral; **admitted**. |
| 55 | Ledger9→17 and F36 verified; DF-3 census self-reference defect found/routed without erasing genuine work; **admitted**. |
| 56 | Ledger17→27, F37 and routed DF-3 correction verified; final review commit is original pinned tip; **admitted**. |

## Remaining custody work — no automatic reruns

1. For the eleven gap labels, recover *already existing* independent reports or contemporaneous integrator disposition with exact tested revision and scope. Author summaries of reviews are leads, not newly authenticated independent artifacts.
2. Decide whether historic whole-tree adjudications for 11/14/19 satisfy the intended completed-attempt rule; retain their scope limitation if counted. Do not retroactively require modern waves/seat minima in the original 2026-09 regime.
3. Recover the exact r15 final re-emitted verdict rather than treating an aggregator summary and the r14-pinned lesson as two independent closures.
4. Bind original r17 implementation/review separately from its later reused-label continuation. R21 explicitly prevents credit inflation from that inherited work.
5. If retry attempts are to receive separate credit, reconstruct each attempt's substantive bytes and terminal independent disposition. Launch counts, multiple report updates, and `attempt2` directory names alone are insufficient.
6. Source roots and historical `/tmp` reviewer artifacts are not reconstructed here. Lost domain sources mean this audit cannot certify old technical claims by live replay; documentary rejection and source-loss findings remain valid historical outcomes.

No root-ledger absence was treated as automatic failure, no admission was changed, and no lane/fleet counters or completion labels were edited.
