# Protocol surfaces — admission criteria vs closure enforcement

Scope: PROTOCOL.md, PROTOCOL-APPENDIX.md, templates/round-prompt.md, AXES.md, LEARNING.md, scripts/shokunin-watchdog.sh, scripts/hyaku/inline.sh, scripts/hyaku/closure-prompt.md, scripts/hyaku/append-closure.py, scripts/hyaku/lane-addendum.md §9.

## 1. Stated admission criteria (verbatim substance, with lines)

### 1.1 Claim-verification rule
- `templates/round-prompt.md:37-40`: "**Admission:** every claim verifies — measured, or exploratory with a named non-author `unprovable-but-better` judgment — and **no axis is harmed**; a trade anywhere is not an improvement. Report all verdicts and let the operator rule."
- `templates/round-prompt.md:14-17`: 1–3 declared claims, each one axis-move on a distinct axis, each falsifiable before→after; at least one on the **lowest-scoring non-retired axis** unless the stagnation nudge waives it.
- `templates/round-prompt.md:18-21`: claims must be **causally separable** — verifiable without the others having landed; two claims on one axis = one claim; measure each with a counting command run before and after.
- `AXES.md:34-38`: "A round is admitted only if every claim verifies **and no axis is harmed** — a trade anywhere is not an improvement: report every verdict and let the operator rule."
- `PROTOCOL.md:436`: "`SCORECARD.md` axis scores: every score is a claim: it carries the counting command that produced it and the commit it was measured against, so a reader can re-derive it."
- `scripts/hyaku/closure-prompt.md:86-89`: "`admitted` only if every claim verifies and no axis is harmed... Conformance defects... stay in notes and never bar admission; 'could not re-open' grades `unprovable`, never `harmed`."

### 1.2 Axis-verdict rule
- `AXES.md:34-36`: every claim verifies **and** no axis harmed is the admission conjunction; grade each axis.
- `scripts/hyaku/closure-prompt.md:38-39`: "Grade each axis `improved | harmed | unchanged | unprovable-but-better | unprovable`."
- `scripts/hyaku/closure-prompt.md:30-33`: closure re-derives before→after "against `{{HEAD}}` with a plain measurement you run yourself... check no owned axis was harmed (`git diff {{BASE}} {{HEAD}} -- SCORECARD.md`)."
- `AXES.md:43-55`: exploratory claim verifies only as `unprovable-but-better` **with a named non-author reviewer on record**; without it lands `unprovable` and honest-stop applies.

### 1.3 Do-nothing rule
- `scripts/hyaku/lane-addendum.md:416-420` ("Claim sizing", §9, binding addendum): "A target must be one a do-nothing control cannot reach... Before freezing, build the cheapest control that skips the claimed work, score it with the frozen counter, and commit that receipt: if it meets the target, the counter or target is wrong — fix it before data."
- `scripts/hyaku/lane-addendum.md:421-424`: "The claim is judged on the counter, kill rule and predicate declared before data. A rule changed after any seat has scored is not the claim's rule... Freeze one predicate that is the same sentence in the plan, the same condition in the counter's code and the same label in the receipt."
- `scripts/hyaku/lane-addendum.md:408-413`: declare each after-state as one concrete value the closure can re-derive with one command over committed bytes; use no universal clauses unless the counting command enumerates the full set; never narrow a target after landing.

### 1.4 Non-author-review rule
- `templates/round-prompt.md:118-119`: "`[x]` only with a named non-author verifier, `[~]` with a resolvable evidence pointer."
- `PROTOCOL.md:63-68`: promotion boxes "checked by a reviewer who did not author the round's changes — a fresh lane or integrator review, never self-attestation; a subagent the lane dispatched is still the lane."
- `LEARNING.md:40-48`: "Discernment is checked from outside... a non-author — a fresh reviewer or the operator — spot-checks... **at least one admit and one reject**... A subagent the lane dispatched is still the lane. An exploratory round claim... is admitted only through this gate: a named non-author reviewer judging the change better, with reasons on record — never through self-attestation."
- `scripts/hyaku/closure-prompt.md:40-43`: non-author closure spot-checks ≥1 admit and ≥1 reject, re-opens each source, runs the census.

### 1.5 Trend rules
- `templates/round-prompt.md:116-117`: "**Trend verdicts** — one verdict each for `expansion`, `quality`, and `discernment` (`improved`, `harmed`, `unchanged`, `unprovable-but-better`), with evidence; no scalar."
- `LEARNING.md:31-38`: `expansion: improved` with `quality: harmed` is a trade — "reported as a trade, never admitted."
- `templates/round-prompt.md:127-129`: "The watchdog... does not check trend verdicts or the full claim-admission criteria. Driver completion is not admission; independent non-author verification remains required."

### 1.6 Report/conformance (marker vs real report)
- `PROTOCOL.md:230-239` (integrator step 1): verify each cited commit exists and is ancestor of HEAD, no uncommitted round work, `SHONEN` heading present, prompt carried the full contract. "A report violating the report contract... is a conformance defect in the round notes — it does not change the lane's status unless the round's rules already prescribe `failed`."
- `PROTOCOL.md:190-206`: contentless marker → `failed`; short report naming real committed hash → `ok` + defect.
- `scripts/hyaku/closure-prompt.md:20-29`: step-1 concretizes step 1; marker → `failed`; defects named, status-neutral.

## 2. Closure enforcement (what actually runs)

### 2.1 `scripts/shokunin-watchdog.sh` — driver only
- `report_of()` `scripts/shokunin-watchdog.sh:187-207`: file exists at the contract path, changed vs pre-launch byte digest, contains a `SHONEN` heading (regex), `wc -c >= MIN_REPORT_BYTES` (400). No claim, axis, trend, or counting-command check.
- `sources_gate()` `scripts/shokunin-watchdog.sh:367-385`: `sources-census.sh validate` exit 0 passes, exit 1 blocks advancement, exit 2 warns. This is the sole mechanical gate in `advance()`.
- `report_sources_conformance()` `scripts/shokunin-watchdog.sh:349-362`: checks the Sources & frontier heading; called with `|| true` — never blocks.
- Net: watchdog certifies "a real report with a SHONEN heading landed", nothing about admission.

### 2.2 `scripts/hyaku/inline.sh` — mechanical only
- `verify` `scripts/hyaku/inline.sh:153-178`: `report_of` must pass or exit 1; if the report is uncommitted it is swept into a commit (attribution defect noted); if the lane has `ahead != 0` it fast-forward pushes; uncommitted lane changes only produce a `WARN`, never a failure. No re-derivation.
- `closure` `scripts/hyaku/inline.sh:189-199`: renders the closure prompt substituting `BASE`, `HEAD`, and the watchdog digest; commits it; prints its path. Writes no verdict — the verdict is the fresh closure agent's.
- `fail` `scripts/hyaku/inline.sh:180-188`: logs `lane-dead-no-report`, retries the same round until `MAX_ATTEMPTS=3`, then blocks.
- `advance` `scripts/hyaku/inline.sh:203-218`: records the closure outcome, increments `next`, purges scratch, blocks after 3 consecutive `rejected*`. A missing closure row logs `CLOSURE-DEBT` but does not stop the advance.
- `closure_count` `scripts/hyaku/inline.sh:104-112` + `append-closure.py:37-64`: the MANIFEST append validates JSON shape (status vocabulary, trend vocabulary, report exists, duplicate refusal, `closure-correction` needs `supersedes`). It does not check whether any claim verifies, any axis is harmed, trends agree with the spot-check, or a do-nothing control exists.

### 2.3 `scripts/hyaku/closure-prompt.md` — the real admission check
- The non-author closure agent (fresh `task`, never by the lane) performs all substantive checks: step-1 conformance, per-claim re-derivation with a plain measurement run by the judge, per-axis grading, gate-evidence verification (never executing a sibling gate), discernment spot-check, then writes the spot-check file and the MANIFEST entry.
- Conformance defects are explicitly status-neutral; only marker-vs-report, or claims-that-do-not-verify / harmed axes, drive `admitted=false` (`rejected-honest-stop`, `rejected-harmed`, `failed-marker`).

## 3. Which admission criterion is not checkable by the lane before it files?

The lane cannot self-check **the claim-verification / no-axis-harmed conjunction as the non-author closure will apply it**, specifically the semantic match between each claim's *stated wording* and the frozen predicate/counter that is supposed to prove it. The lane can run its frozen counter and see green — but green certifies only the *narrower* property the instrument encodes, not the wider sentence the claim states in the report. Whether the closure's plain re-measurement, the do-nothing/forgery controls, and the wave's own adversarial artifacts (reviewer/critic/mutation-tester seats) agree that the wording is true is decided by the non-author judge after the freeze, after the wave commits, and after the report is filed. No mechanical step in `verify`/`closure`/`append-closure.py` compares stated wording to frozen predicate; the comparison lives entirely inside the closure agent's reading of the report, the counter code, and the wave artifacts.

[INFERENCE] This is the one joint that produces the fleet's dominant rejection class: instrument-green-but-unprovable-wording, where the lane's own wave already holds a committed counterexample to the wording — in lane custody before filing — yet nothing forces the L1 to reconcile wave artifacts against wording before writing the report.

## 4. Pre-file self-check coverage

| Criterion | Lane can self-check? |
|---|---|
| Marker vs report (SHONEN heading, size, cited hashes ancestor, no uncommitted work, pushed) | yes — all mechanical, mirrors closure step 1 |
| SHONEN `[x]` needs named non-author verifier | partial — lane can verify presence of a name, but the lane itself stays `[~]` by rule; closure/promotion reviewer confers `[x]` |
| Trend verdicts present, in-vocabulary, with evidence | yes for presence/vocabulary; partial for correctness (closure spot-checks discernment) |
| Sources census exit-0 | yes — `sources-census.sh validate` is runnable pre-file (watchdog also runs it) |
| Every claim verifies + no axis harmed (semantic: wording = predicate, counter re-derivable from committed bytes) | partial — counter-green is self-checkable; the semantic wording-vs-predicate match and the non-author's judgment are not |
| Do-nothing / forgery controls committed before freeze with observed ids | yes — lane can and must run this per §9; failure to do so is the most common filing defect |
| Gate evidence (self-test tally, frozen-run verdict, revision) | yes — lane owns its gates; closure verifies committed evidence, never re-executes |

## Gate attachment point

### Attachment
A pre-file self-closure gate belongs **inside the lane round itself, between wave-settlement (WAVE-DONE) and report filing**, invoked by the L1 through the existing jj helper — not in `inline.sh verify` (report already filed) and not in the watchdog (driver completion is not admission by design). Concretely: a new committed lane-side script at `{{LANE_CWD}}/tools/pre-file-gate.sh` (lane-owned, registered in the lane's `SCORECARD.md`/registry where gates are listed), run as:

```
{{LANE_CWD}}/tools/pre-file-gate.sh --round {{ROUND}} --base {{BASE}} --head <lane branch tip>
```

and required to pass with exit 0 before the L1 may write `.ufo/reports/round-{{ROUND}}/{{LANE}}.md`, mirroring the existing pre-report guard at `scripts/hyaku/lane-addendum.md:377-382` (`ls-remote` must print the final lane hash; `grep -c '^## SHONEN' <report>` must print 1). The closure prompt then asks for the gate's receipt: `pre-file-gate PASS <lane> r{{ROUND}} <head-hash> <counter-hashes> <wave-results-hash>`.

### Smallest such gate (catches the `yes`/`partial` rows that matter)
For each declared claim (1–3), the gate fails closed unless all hold:
1. **Wording = predicate.** The claim sentence is transcribed verbatim into a `claims.json` manifest; the frozen counter's kill condition (code line or registry selector), the before→after counting command, and the target are asserted byte-equal to that sentence's operative clause (no universal term — "all/every/no harm" — unless the command enumerates the full set). A predicate narrower than the sentence fails.
2. **Wave artifacts reconciled against wording.** Every wave seat finding (reviewer/critic/mutation-tester/labrat) under `{{LANE_CWD}}/.ufo/waves/round-{{ROUND}}/*-results.json` is dispositioned `agree`/`defect`/`reject` with a pointer; any `agree` counterexample whose target matches the claim's wording **blocks filing** — the claim must be narrowed (with the narrowing recorded as an honest stop) or withdrawn before the report is written. This forces the L1 to reconcile adversarial artifacts it already holds in custody against stated wording, before filing.
3. **Do-nothing/forgery receipt committed.** The cheapest no-work control and the named false-green controls were scored pre-freeze with observed rc/finding ids, committed in the lane tree, and do not meet the target. [INFERENCE] Missing receipt is a filing defect, not a post-hoc replay.
4. **Lane-side step-1 mirror.** Report skeleton passes the mechanical checks closure will apply: SHONEN heading + one line per box, every cited commit `merge-base --is-ancestor` of the branch tip, `jj-lane.sh state` shows `ahead=0`, `git status --porcelain` empty for round work, census exit 0.
5. **Evidence pins.** Both before and after numbers carry their counting command and measured commit; the gate re-runs each counting command against `{{HEAD}}` and compares to the reported value.

Print `GATE PASS`/`GATE FAIL <reason>` with exit 0/1; mirror the `0=clean / 1=failed` verdict convention of PROTOCOL §Gate standard. On FAIL the lane narrows or withdraws the claim and never files the original wording.

### Table (criterion → prompt line → closure enforcement → lane self-check)

| Criterion | Stated in prompt (line) | Enforced at closure (file:line) | Lane can self-check |
|---|---|---|---|
| Every claim verifies + no axis harmed (admission) | `templates/round-prompt.md:37-40`; `AXES.md:34-38` | `scripts/hyaku/closure-prompt.md:30-39,86-89` (judge re-derives, grades axes, sets `admitted`) | partial — counter-green yes; semantic wording-vs-predicate match no |
| 1–3 claims, distinct axes, causally separable, lowest non-retired axis | `templates/round-prompt.md:14-21`; `AXES.md:27-33` | `scripts/hyaku/closure-prompt.md:30-39` (judge checks) | yes — inspectable pre-file |
| Falsifiable before→after with counting command + measured commit | `templates/round-prompt.md:20-23`; `AXES.md:27-29`; `PROTOCOL.md:436` | `scripts/hyaku/closure-prompt.md:30-33` (judge re-derives with plain measurement) | yes — re-runnable pre-file |
| No universal clauses unless fully enumerated; never narrow after landing | `scripts/hyaku/lane-addendum.md:408-415` (§9) | `scripts/hyaku/closure-prompt.md:86-89` (via `admitted=false`) | yes — inspectable pre-file |
| Do-nothing control cannot reach target; controls committed before freeze | `scripts/hyaku/lane-addendum.md:416-420` (§9) | `scripts/hyaku/closure-prompt.md:30-37` (judge verifies gate evidence; missing pre-freeze receipt fails claim) | yes — executable pre-file; commonly skipped [INFERENCE] |
| Predicate frozen before data; same sentence/code/label | `scripts/hyaku/lane-addendum.md:421-424` (§9) | `scripts/hyaku/closure-prompt.md:30-37` (judge checks freeze) | yes — inspectable pre-file |
| Axis verdicts: improved/harmed/unchanged/unprovable-but-better | `templates/round-prompt.md:37-40`; `AXES.md:43-55` | `scripts/hyaku/closure-prompt.md:38-39,80-85` (judge grades; entry `verdicts`) | partial — lane grades provisionally; closure decides [INFERENCE] |
| Exploratory claim needs named non-author reviewer | `templates/round-prompt.md:31-35`; `AXES.md:47-50` | `scripts/hyaku/closure-prompt.md:36-37` (judge is the named reviewer) | no — reviewer is the closure judge by construction |
| Trend verdicts (expansion/quality/discernment) | `templates/round-prompt.md:116-117`; `LEARNING.md:31-38` | `scripts/hyaku/closure-prompt.md:40-48,80-85` (judge grades with spot-check evidence) | partial — presence/vocabulary yes; correctness no |
| Non-author spot-check: ≥1 admit + ≥1 reject, agree/disagree with reason | `LEARNING.md:42-48`; `templates/round-prompt.md:127-129` | `scripts/hyaku/closure-prompt.md:40-48` (judge performs) | no — must be non-author |
| SHONEN `[x]` needs named non-author verifier | `templates/round-prompt.md:118-119`; `PROTOCOL.md:63-68` | `scripts/hyaku/closure-prompt.md:20-21`; promotion gate (`PROTOCOL.md:63-75`) | no — confers `[x]`; lane asserts `[~]` |
| Marker vs real report | `PROTOCOL.md:190-206`; `templates/round-prompt.md:121-125` | `scripts/hyaku/closure-prompt.md:20-29` + `scripts/shokunin-watchdog.sh:183-207` (`report_of`) | yes — same regex/size checks pre-file |
| Cited commit exists + ancestor of HEAD; pushed; no uncommitted work | `PROTOCOL.md:117-122,230-232` | `scripts/hyaku/closure-prompt.md:20-28`; mechanically in `scripts/hyaku/inline.sh:153-178` (`verify`) | yes — pre-report guard already exists (`scripts/hyaku/lane-addendum.md:377-382`) |
| Prompt carried full round contract verbatim | `PROTOCOL.md:93-104` | `scripts/hyaku/closure-prompt.md:26-27` | yes — diff prompt vs template pre-file |
| Sources census exit 0 | `templates/round-prompt.md:54-62` | `scripts/shokunin-watchdog.sh:367-385` (`sources_gate`); `scripts/hyaku/closure-prompt.md:43` | yes — runnable pre-file |
| Gate evidence verified, never executed by judge | `PROTOCOL.md:412-417` | `scripts/hyaku/closure-prompt.md:34-36` | yes — lane runs its own gates/counters pre-file |
| MANIFEST entry shape + vocabulary + duplicate refusal | `PROTOCOL.md:252-325` | `scripts/hyaku/append-closure.py:37-64` (`validate`) | yes — `append-closure.py --dry-run` on the staged entry pre-file |
