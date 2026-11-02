# tabi — round 55 report (2026-11-02, Windows host)

Lane head at round end: `545b251d` (work commit; receipts commit follows). Baseline
`793d947e`. Freeze `db6f4225`. C2 data `c1e64885` (+ addendum `81b2fdbd`) + the D54-1
landing rides the same commit. C1 data `103bf06f`. Correction 1 `216b1cf2` (the frozen
correction flow, cycle 1 of 2; the raced correction-0 receipt kept). Axes at round start:
adjacency 8, coverage 9, depth 9, operability 9, freshness 9, calibration 9; saturation 8 /
window 3; the r54 capability row keeps the window RESTARTED (round 55 = position 1) — the
nudge is inactive, the lowest-axis obligation applies. Claims: 2 (C1 adjacency, C2 coverage).
Both verified; no axis harmed (self-derived; the non-author closure re-derives everything).

**Fresh-start ruling honored** (the rendered contract §7 lists r42/r43/r47 as the last
three REJECTED closures; rounds 48–54 were subsequently admitted, so the discipline is
applied as a bar, not a standing verdict). What was ruled out, and why:

- **r42-class (counter greens nonce-relabeled/synthetic receipts)** — ruled out: the r55
  counter pins committed-byte digests (driver/hostsrc re-hashed at scoring time), requires
  the invocation-bound nonce on the data: page, fixture pages, all typed values, the echo
  page AND the server log, and ships 103 hand-declared fixtures (3 green incl. one
  declared-cne green + 100 refusals incl. seven new round-55 control-domain cases) with an
  exact-match expected-findings manifest and the declared could-not-evaluate rule per case.
- **r43-class (in-model do-nothing seats)** — not applicable: no wave/seat claim is
  declared; the L2-floor L0 stays open and routed around (L1-inline round, disclosed in
  claims.json per the standing PROVINCE.md line).
- **r47-class (reasoned-not-measured after-states)** — ruled out: no after-state number is
  asserted from arithmetic. C1's after is the v15 meter's own exit-0 run at the data
  revision; C2's after is a live receipt produced by the frozen runner after the freeze and
  scored by the frozen counter over committed bytes.
- **Shared r42/r43/r47 defect (do-nothing-reachable evidence)** — both claims carry the
  do-nothing-control test: C1's red control IS the do-nothing state (6 findings at round
  open, receipt taken before any lane write; green requires the re-bind work), and C2's
  baseline evidence tree is EMPTY (`git ls-tree -r --name-only 793d947e… -- corpus/evidence/round55 | wc -l` → 0).

## Work performed

- **C1 (adjacency — lowest owned axis): the regression-gate re-bind + the v15 meter
  generation bump.** Round-open red control: the committed v14 meter generation at the
  baseline measured RED — exit 1, 6 findings (4 lane-screen-head-mismatch: kengaku, mori,
  shokunin-binary-forensics, tameshi; PLUS lane-screen-sha-mismatch and
  lane-screen-lines-mismatch both on kengaku — its second consecutive byte change; ZERO
  audit findings), receipt `controls/c1-meter-v14-red-at-round-open.json` taken before any
  lane write. The v15 meter (frozen digest `2fbcf068…`) differs from v14 only in header
  comments (incl. the Round 55 delta paragraph quoting the red control's numbers and naming
  the fix), the ledger rebind to the r55 names, the schema strings (v15 in all four places
  — `controls/c1-token-check-r55.txt`), the usage strings and the sentence/header token —
  and FIXES a v14 comment-only name-leftover (v14's header said "tabi round 53"; found by
  this round's diff review; v14 bytes never edited). Pure core byte-identical to v14
  (committed diff `controls/v14-v15-meter.diff`). Ledgers re-bound at ONE fresh snapshot:
  audit-r55 carries the r54 statuses verbatim; delta-r55 re-binds all 12 lane rows (11
  provinces byte-identical at their new heads; kengaku RE-SCREENED at its new head
  `a6cd337d…` — 892 lines, was 847, ZERO browser-ground hits, 0 new adjudications), 16
  line rows carried by exact whole-line quote match. GREEN at `216b1cf2` at correction 1 —
  exit 0, predicate true, 0 findings, counts {roster:16, mapRows:16, auditRows:16,
  deltaLanes:12}; one correction cycle consumed (correction 0 raced tameshi's mid-round
  commit; raced receipt kept `measure/c1-meter-raced-at-correction0.json`). Selftest 16/16
  (`measure/c1-meter-v15-selftest.json`). Receipt named by OUTCOME
  `measure/c1-meter-green-at-correction1.json`.
- **C2 (coverage — capability acquisition `webview2-keyevent-control-keys-windows`,
  first-working 55; the r54 planned residual): the key-domain control keys, each with a
  page-side DOM witness.** The r55 runner carries the r52 plain trace, r53 Shift chords and
  r54 chord-domain leg unchanged and adds the control-domain leg: End (VK 35) re-anchors
  the caret with the NEGATIVE EDIT WITNESS (value read back unchanged — a movement key
  edits nothing), Backspace (VK 8) deletes exactly the nonce's last character (residue
  re-derived by the counter from the receipt's own nonce) with the removed character
  re-typed to an exact restore, Tab (VK 9) moves focus field → field2 witnessed by
  `document.activeElement`, and ONE Enter keyDown (VK 13, text `\r`) from the TABBED-TO
  field drives the implicit submission — the same `/echo?field=&mixed=` query, witnessed
  SERVER-SIDE (fixture served log) and CLIENT-SIDE (echo page renders both). S153
  re-opened byte-identical a SEVENTH time (the dispatchKeyEvent contract); S083 re-opened
  with the located ground EXTENDED to §4.10.22.2 Implicit submission (the default-button
  contract the Enter leg rides). The pre-freeze smoke run CAUGHT the caret-placement
  defect (a mouse click into a non-empty field places the caret at the click point;
  Backspace then deleted a middle character) and the End anchor landed BEFORE the freeze —
  red control committed at the citing round
  (`controls/c2-smoke-caret-midtext-red.json`, criterion-108 discipline). Live run: nonce
  `tabi-r55-5a70384367c4b44b`, fresh compile spawned FIRST TRY (compile bytes inside the
  receipt), Edg/156.0.4314.58, keylog window +4, `journey.form.pageKeylog` 69 entries
  re-derived END TO END by the counter from the receipt's own nonce, teardown 0. Counter
  green: exit 0, 0 findings, couldNotEvaluate []. Cross-refusals symmetric: r54 counter on
  the r55 receipt → exit 1, 6 findings; r55 counter on the committed r54 receipt → exit 1,
  7 findings (incl. control-domain-missing + keylog-length — the frozen expectation,
  derived from the counter's check flow and corrected once BEFORE the freeze). Selftest
  103/103 at the frozen bytes; `--path-selftest` 6/6. Evidence tree 0 → 7.
- **D54-1 (r54-closure carry-in, routed): the three cited counter receipts LANDED** at the
  exact cited paths under `.ufo/waves/round-54/measure/` — re-measured THIS round on the
  committed r54 receipt + committed PNG bytes with the committed r54 counters: green exit 0
  (0 findings, cne []); `c2-r53counter-refuses-r54.json` exit 1 with EXACTLY the cited 5
  findings; `c2-r54counter-refuses-r53.json` exit 1 with EXACTLY the cited 7 findings incl.
  chord-domain-missing + keylog-missing. Provenance note
  `measure/d54-1-landing-note-r55.txt` discloses these are r55 re-measures (the r54
  originals LOST at scratch cleanup). The cited-receipt landing rule NAMED and landed as
  **QUALITY.md criterion 109** citing the lesson.
- **D54-2 (routed): S161's anchor cell corrected of record** — §5.3 → §3.5.1, verified
  against the staged bytes (`data-level="3.5.1" id="interface-keyboardevent"` present; no
  §5.3 heading exists in them); old→new logged in the lesson; no frozen byte edited.
- **D54-3 (the L2-floor L0 standing): referred to only**, never treated as answered.
- **Freeze-chain disclosure (this round's own defect, caught and fixed same-round):** the
  freeze needed four commits — two EMPTY path-carrier commits (`774610da`, `a766984c`) and
  a claims-only probe (`7b82763d`) — because CRLF line endings in the commit path list
  (python text-mode stdout on this host) defeated treecommit's isfile resolution. Caught
  by the post-commit diff-tree landing check, root-caused, fixed (LF paths), the full
  frozen set landed at `db6f4225` with every digest matching claims.json's pins. The class
  is mined in the lesson and covered by criterion 109's landing-check rule.

## Landed changes (every change tied to a LOG.md entry and its commit)

| Commit | Content |
|---|---|
| `774610da` (pushed) | freeze attempt — EMPTY path list (the CRLF defect, disclosed) |
| `a766984c` (pushed) | second empty carrier (disclosed) |
| `7b82763d` (pushed with the carrier) | claims.json only (the probe) |
| `db6f4225` (pushed) | the FULL freeze: claims.json + meter v15 + runner r55 + counter r55 + 103 fixtures + round-open controls (v14 red control, v14 selftest, token check, v14→v15 diff, the smoke caret-defect red control) + freeze receipts (counter selftest 103/103, path-selftest 6/6, v15 selftest 16/16, census start) |
| `c1e64885` (pushed) | C2 data: live control-domain receipt + 5 per-step PNGs + counter green + both cross-refusals; PLUS the D54-1 landing (the three r54 receipts at the cited paths + the provenance note) |
| `81b2fdbd` (pushed) | C2 addendum: the back leg's per-step PNG pin (`receipt-journey-b-back.png`) |
| `103bf06f` (pushed) | C1 data: audit-r55 + delta-r55 bound at one fresh snapshot + the snapshot receipt |
| `216b1cf2` (pushed) | C1 correction 1: delta-r55 re-bound (tameshi raced correction 0); the raced receipt kept |
| `545b251d` (pushed) | work: SOURCES (S083 re-open + S153 seventh re-open + S161 anchor fix), knowledge note 71, round-55 lesson, QUALITY criterion 109, SCORECARD round-55 block, LOG, PROVINCE round-55 line |
| receipts commit (after this report) | census-end + check-sources + c3-gate receipts |

## Before → after measurements (counting command + measured commit, per claim)

- **C1 (adjacency):**
  - Before: `node .ufo/waves/round-54/counters/c1-adjacency-host-v14.mjs --rev 793d947e… --repo <lane> --fleet <fleet> --json` → exit 1, **6 findings**, at `793d947e` (the round-open control).
  - After: `node .ufo/waves/round-55/counters/c1-adjacency-host-v15.mjs --rev 216b1cf2… --repo <lane> --fleet <fleet> --json` → exit 0, predicate true, **0 findings**, counts {roster:16, mapRows:16, auditRows:16, deltaLanes:12}, measured at `216b1cf2`; selftest 16/16 at the frozen bytes. One correction cycle consumed (frozen allowance: two).
- **C2 (coverage):**
  - Before: `git ls-tree -r --name-only 793d947e… -- corpus/evidence/round55 | wc -l` → **0**.
  - After: `git ls-tree -r --name-only 81b2fdbd… -- corpus/evidence/round55 | wc -l` → **7** (receipt + 6 per-step PNGs), measured at `81b2fdbd`. Counter green: `node .ufo/waves/round-55/counters/webview2-receipt-r55.mjs corpus/evidence/round55/webview2-control-keys/receipt.json --shot … --png-a … --png-b … --png-c … --png-form … --png-echo … --driver scripts/webview2-cdp-loopback-round55.mjs --hostsrc scripts/webview2-host-round48.cs` → exit 0, predicate true, **0 findings**, couldNotEvaluate []; selftest 103/103 at the frozen bytes; `--path-selftest` 6/6.

## Sources & frontier

- SOURCES.md rows before→after: `grep -c '^| S' corpus/SOURCES.md` → **161 before, 161 after** (the S162 duplicate-URL draft was DROPPED before landing — check-sources E04 caught it while authoring, and the registry contract routed the ground to an S083 RE-OPEN with an extended located ground instead of a duplicate row). Census: start exit 0, `tabi ok`, 22 pre-existing W04 (`measure/census-start.txt`); end exit 0, same W04 set, registry 161 rows (`measure/census-end.txt`). Gate: `node scripts/check-sources.mjs` → `SOURCES_GATE verdict=clean rows=161 findings=0` (`measure/check-sources-at-work.txt`).
- Sourced claim: C2 rests on **S083 re-opened this round** (fresh fetch 466,321 B, sha256 `dc7c3088…`, staged `.ufo/waves/round-55/sources/html-form-control-infrastructure.html`; the located ground extended to §4.10.22.2 Implicit submission; the ≤25-word located quote greps verbatim 1 hit in the raw bytes: `hitting the "enter" key while a text control is <a id=implicit-submission:focused`) and **S153 re-opened byte-identical a SEVENTH time** (sha256 `f60f0c02…` == the registered anchor; the dispatchKeyEvent modifiers ground; used-by extended in place, old→new logged). S161 re-verified from the staged bytes for the D54-2 anchor correction. Knowledge notes 70 → **71** (the control-keys note). Lesson `corpus/lessons/round-55.md` carries the Gate (both opens with command/date/quote), the Corrections of record (D54-1/D54-2/D54-3 + the fresh-start ruling), paste-able Measurements, and four mined Mistakes (caret-placement class; CRLF commit-path class; the v14 comment name-leftover; the frozen-expectation-walk correction).

## Trend verdicts

- **expansion: improved** — the measured surface grew again: the webview2 key-event model now covers the control-key domain (End caret-anchor with the negative edit witness, Backspace edit with exact restore, Tab focus traversal with the page's own activeElement witness, Enter keyboard-submit with the implicit-submission default-button ground), four trace plans in one fill, the complete page keylog re-derived by the counter (0 → 7 evidence files); the capability row `webview2-keyevent-control-keys-windows` enters the table; S083's located ground extended to a new section; seven new refusal cases in the counter's exact-findings manifest; notes 70 → 71.
- **quality: improved** — the regression gate absorbed the second consecutive kengaku byte change AND a mid-round tameshi commit race at one correction cycle (the frozen flow working as designed; the raced receipt kept and named by outcome); the v15 bump is isolated to comments/ledger names/schema strings/usage/token with the pure core byte-identical (diff reviewed BEFORE any run — the review caught the v14 comment name-leftover); the pre-freeze smoke run caught the caret defect and the fix landed BEFORE the freeze with the red control committed at the citing round; 103 exact-findings fixtures; the CRLF empty-commit class caught by the landing check, named, fixed in-round (criterion 109).
- **discernment: improved** — every after-state is an instrument output at a named revision (`216b1cf2` for the green, `c1e64885`/`81b2fdbd` for the receipt); the carry-ins were corrected of record with measured oracles (the three D54-1 receipts re-measured on committed bytes at the exact cited paths with provenance disclosed and the originals named LOST; the D54-2 anchor verified against the staged bytes); the duplicate-URL draft was dropped the moment the gate flagged it rather than argued around; the frozen cross-refusal expectation was corrected pre-data by walking the counter's check flow; the lane did not self-check its SHONEN boxes (the operator-owned gate routed around per the standing routing).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` §Approval table / §Evidence ladder / §Runbook (unchanged this round; prior `[x]` was named lane-dispatched, not non-author — the operator owns the gate).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: this round's live control-domain journey in `LOG.md` Round 55 (+ the r54 lineage in `corpus/knowledge/webview2-*`).
- [~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/executor-test-sufficiency.md` verdict SUFFICIENT (standing); the r55 runner's own usage/header is self-contained.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` (the round-55 line added; refusal routes revenger/kaidoku/kake/kagi unchanged).

No self-`[x]`: the boxes remain `[~]` with resolvable pointers; `[x]` stays the operator's call (the standing routing from the r54 spotcheck note).

## Assimilation

`considerthese/` does not exist in the lane repo (checked 2026-11-02). Shokuknow register not reachable from this host. Assimilation: none — shokuknow unreachable.
