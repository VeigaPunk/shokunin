# PROTOCOL.md — duplicated-rule + contradiction audit (round-11, protocol lane support)

Subject: `/home/vgpnk/projects/shokunin/PROTOCOL.md`, 583 lines (`wc -l`), main HEAD `6deaeaa`
(working tree; `git log -1` at read time = `8ec7a568` "kengaku: round-9 report").
Read-only audit. All line numbers = current file.

Persistence check on the round-10 list: the **number** survived, the **list** did not.
- `.ufo/reports/round-10/protocol.md:237` D-48: "`PROTOCOL.md` 583 lines with ~29 inline incident
  references; 17 duplicated rule pairs named by the round-10 simplifier audit".
- `.ufo/reports/round-10/protocol.md:383-384`: "`SimplifyProto` (13 defects, 17 duplicated rule
  pairs, compaction target)".
- `.ufo/reports/round-10/protocol.md:446-447`: "compact `PROTOCOL.md` 583 → ≤450 lines, 17
  duplicated rule pairs collapsed".
- `SCORECARD.md:47-51`: "collapse the 17 duplicated rule pairs the round-10 simplifier audit named
  … and resolve the remaining contradictions it listed (`round open indefinitely` vs `missing
  report never holds a round open`; three ledger-path statements)".
No file in the repo enumerates the 17 pairs. The count below is re-derived from the current text.

---

## Count

**30 duplicate clusters** (one obligation each, 2–6 instances) covering **96 instance locations**.
Counting rule used: a cluster = one obligation with ≥2 locations that **state** it; a bare
cross-reference ("per the embed clause above", "see above", "same discipline as `LOG.md`") is not
counted as an instance, but a location that asserts the obligation in its own words is.

Collapsing the 30 clusters into the audit's coarser "rule pair" families reproduces **exactly 17**
(see §Reconciliation) — the round-10 count is consistent with mine at family granularity.

---

## Duplicate clusters

### D1 · mint bar (2 unplaceable demand instances or operator directive)
- `15-17` «"minted when a domain demand is proven: two documented *unplaceable* demand instances … or an explicit operator directive — the bar closure step 3 applies, stated once here."»
- `293-296` «"Mints a new shonen only if evidence shows an unserved domain — minimum evidence per **Lifecycle**: two documented *unplaceable* demand instances or an explicit operator directive."»
- **Canonical:** `15-17` (self-declared "stated once here").
- **Merge from `293-296`:** the ROADMAP-drift rule ("where a restatement drifts, this file wins and the drift is a round-notes defect") and the mint *action*; replace its bar restatement with a pointer to Lifecycle. (`CORPUS.md`/`ROADMAP.md` restatements are outside this file.)

### D2 · shokunin promotion minimum bar (triple)
- `20-23` «"its skill file carries real decision tables, error patterns, checklists, and cited sources — not generic advice; its `LOG.md` shows completed rounds; and a reviewer can execute the written instructions without oral hand-holding"»
- `50-57` «"`SKILL.md` contains at least one decision table, one error-pattern list, and one checklist, each citing a resolvable source …"» (4 bullets)
- `481-484` «"- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources"» (echoed again as the `SHONEN.md` file-contract row at `470`)
- **Canonical:** `48-57` for the prose bar; `481-484` is its declared rendering (`48-49`: "rendered box-for-box by the `SHONEN.md` seed below; the two change only in the same edit").
- **Merge from `20-23`:** "— not generic advice" (also Invariants `491-492`) and "its `LOG.md` shows completed rounds" (plural) vs box 2's "at least one end-to-end domain task"; fold into `50-57` and keep Lifecycle as a one-line pointer. Note the seed cannot absorb detail: it is byte-diffed against six child repos (`470`).

### D3 · `[x]` requires a named non-author verifier; unverified `[x]` degrades to `[~]` (4 locations)
- `39-47` «"Every `SHONEN.md` box checked by a reviewer who did not author the round's changes … Any `[x]` in `SHONEN.md` carrying no named non-author verifier is author attestation and counts as `[~]` for the gate."»
- `151-155` «"`[~]` means asserted-by-author, not skipped."»
- `486-487` «"Marks: `[~]` asserted by the lane itself (evidence pointer required), `[x]` only with a named non-author verifier per **Promotion gates**."»
- `544-546` «"kotoba's `3b029b8` committed under the operator's personal identity blurs the author/non-author line the `[x]` verifier rule depends on"»
- **Canonical:** `39-47`.
- **Merge:** `486-487` carries no unique content (pure restatement + pointer) — delete or reduce to the pointer; `151-155`'s promotion-review disqualification consequence is already only at `155-159`.

### D4 · jin'i-ryu bar
- `24-26` «"promoted when it can iterate on itself: given a round's telemetry it proposes and lands its own improvements (falsifiable deltas in `LOG.md`)"»
- `60-64` «"At least one logged round in which the shokunin — given the round's telemetry — proposed and landed a falsifiable improvement to its own `SKILL.md`/`PROVINCE.md`."»
- **Canonical:** `60-64` (has verifier/evidence framing).
- **Merge from `24-26`:** only its tail, "with the main repo aggregating only promotion/mint decisions" → belongs to D5.

### D5 · main repo aggregates only promotion/mint decisions
- `25-26` «"with the main repo aggregating only promotion/mint decisions."»
- `63-64` «"the main repo aggregates only the promotion decision."»
- `297-299` «"each lane's own `LOG.md` entry remains lane work, not integrator work — lanes write inside their own repos"»
- **Canonical:** `63-64`.
- **Merge:** `25-26` uniquely says **mint**; `297-299` adds the lane-owns-its-`LOG.md` clause (keep with step 4).

### D6 · prompt snapshot clause + mandatory protocol re-read
- `79-82` «"Round prompts are snapshots: where a prompt — or any earlier round's instructions — conflicts with the current `PROTOCOL.md` or `CORPUS.md`, the repo files win. A lane re-reads the protocol at the start of every steered round; a long-lived mission does not grandfather superseded rules."»
- `220-223` «"where a generated driver prompt conflicts (e.g. "never MANIFEST.json"), this file wins per the snapshot clause"»
- `246-248` «"so the duty reaches the lane solely through this file's re-read"»
- **Canonical:** `79-82`.
- **Merge:** the concrete conflict example (`"never MANIFEST.json"`) and the integrator-role assignment from `220-223`.

### D7 · prompt embeds contract verbatim ↔ closure step 1 re-checks "the five contract items"
- `84-89` «"Round prompts embed the operative contract verbatim … Each *child-lane* prompt carries, as quoted protocol text: the report path and filename, the commit-before-report ordering, the `SHONEN` heading requirement, the commit-hash citation rule, and the lane's write scope."»
- `267-269` «"checks the round's dispatched `.ufo/prompts/*.md` carried the five contract items verbatim per the embed clause above"»
- **Canonical:** `84-97` (the item lists).
- **Merge from `267-269`:** the **L2 route-map ↔ `MISSION.md` bucket** check (only stated there) — it is a sixth item not in the embed list, so either add it to `84-97` or keep the step-1 line without the "five … per the embed clause" restatement.

### D8 · `scripts/` is operator-side; the lane names corrections, never edits
- `104-107` «"the integrator's report must also carry the exact corrected `lane_prompt()` text required, since `scripts/` is edited by the operator-side maintainer, not a lane."»
- `232-239` «"it never edits a prompt or the script … `scripts/` and `.ufo/state/` remain operator-side — the protocol lane names required template corrections in its report but never edits the script."»
- `506-509` «"`MISSION.md`, `AXES.md`, and `scripts/` are operator-side integrator files: the protocol lane names the corrections they need in its round notes and does not edit them."»
- `526-527` «"untracking them is operator-side work named in the round notes."»
- **Canonical:** `506-509`.
- **Merge:** `104-107`'s "exact corrected `lane_prompt()` text" duty is **not** in `506-509` → must be added there (it is the only enforceable form of "names the corrections"); `232-239`'s "expand by exactly three" enumeration.

### D9 · rounds are per-lane counters, not a fleet clock (4 locations)
- `109-114` «"Rounds are per-lane counters, not a fleet-global clock … the integrator closes round `<N>` per lane, not per fleet."»
- `228-229` «"the entry shape had no semantics for a per-lane-counter driver"»
- `253-257` «"Under the respawn driver lanes hold different counters at the same instant (one lane's round 9 was dispatched 17:57, an hour after another lane's round 9 closed at 16:47) … fleet-wide completion is never observable"»
- `303` «"Semantics under a per-lane-counter driver:"»
- **Canonical:** `109-114`.
- **Merge from `253-257`:** the closure consequence ("Closure is therefore per lane-round") and its measurement.

### D10 · report lands last; must cite the commit hash; landed = committed
- `116-127` «"A lane report **lands last** — written only after the lane's child-repo work is committed, and it must cite the commit hash. Landed means committed: changes that exist only in a working tree do not count for the round."»
- `272-274` «"a report that violates the report contract (missing heading, dead or orphaned hash, report filed before its commit)"»
- `453-454` «"**Commits are cited by hash, never by subject or tag**"»
- `87-88` (embed item: "the commit-before-report ordering … the commit-hash citation rule")
- **Canonical:** `116-127`.
- **Merge from `453-454`:** the tag failmode (`git rev-parse round-4` fails) — a distinct failure class, keep as its own bullet but stop restating the ordering there.

### D11 · report/commit attribution carries the lane identity
- `128-134` «"Landed also means landed *by the lane*: the commit that adds `.ufo/reports/round-<N>/<id>.md` carries the lane identity … (round-10 measurement: 21 reports were added by `6565e89`, 21 by `609ecb6`, 4 by `0a30b44` — 46 of 60 swept …)"»
- `542-553` «"Lane authorship is auditable: each child repo is configured at mint so round commits carry the lane identity … a main-repo lane commits with `git -c user.name=<lane>-shokunin …`"»
- `554-556` «"Round-10 measurement: 0 of 60 reports were added by a lane-identity commit — 33 by the operator's identity and 26 by `shokunin <shokunin@local>`"»
- **Canonical:** `542-553` (child + main-repo rule with the `-c` recipe).
- **Merge:** `128-138` uniquely carries "a swept report is still landed — history is never rewritten to fix attribution" and the counter-advance timestamp. **Both measurements are stale and uncommanded** — see §Contradictions (c3).

### D12 · the driver's completion signal is the report path's existence
- `143-146` «"the report file's existence is also the round-completion signal"»
- `163-165` «"`report_of()` is the driver's completion signal and the mission stays live until the stale-lane rule below fires"»
- `200-203` «"The driver's completion signal is that path's existence (`report_of()` in `scripts/shokunin-watchdog.sh`)"»
- **Canonical:** `200-203` (names the function and the script).
- **Merge:** `163-165`'s "mission stays live until the stale-lane rule fires" (link), and delete `143-146`'s duplicate framing (contradiction (a)).

### D13 · missing report / contentless marker → integrator records `failed`
- `161-169` «"A lane whose mission has terminated or been respawned without filing its round report is recorded `failed` by the integrator … `failed` covers every lane-round that was prompted or dispatched and has no report by closure"»
- `205-218` «"a contentless **completion marker** closes a lane-round with no work behind it … the integrator records that lane-round `failed`, keeps the marker file as a conformance defect"»
- `319-322` «"**Completion evidence** is a `.ufo/reports/round-N/<lane>.md` that satisfies the report contract; a completion marker is not a report (see above) and makes the lane-round `failed`."»
- **Canonical:** `161-169` for the rule; `200-218` for the marker taxonomy.
- **Merge:** `319-322` carries no unique content (cross-ref + restatement) — reduce to the pointer.

### D14 · the driver's `failed`/respawn path is unreachable while its daemon is up
- `185-188` «"recording `failed` is a ledger act, not a kill: the driver's respawn path is unreachable while its daemon is up (step 4), so nothing in this section terminates live work."»
- `329-331` «"so the driver's `live` test can never fail while its daemon is up and its `lane-dead-no-report` retry path is unreachable (0 occurrences in 135 log lines)."»
- **Canonical:** `329-331` (carries the probe evidence).
- **Merge:** `185-188`'s conclusion "recording `failed` is a ledger act, not a kill" (unique framing, keep once).

### D15 · report path and filename `.ufo/reports/round-<N>/<id>.md` (5 locations)
- `140-142` «"Every dispatched lane writes a report at `.ufo/reports/round-<N>/<id>.md` in the main repo … A report under any other name does not satisfy the contract."»
- `87-88` (embed item "the report path and filename")
- `320-321` «"**Completion evidence** is a `.ufo/reports/round-N/<lane>.md` …"»
- `386-387` «"files its own round report at `.ufo/reports/round-<N>/aggregator.md`"»
- `513-514` «"their lane report at `.ufo/reports/round-<N>/<id>.md`"»
- **Canonical:** `140-142`.
- **Merge:** `142-143`'s "under any other name does not satisfy the contract" is canonical there; `386-387` must keep the `aggregator.md` special case.

### D16 · `SHONEN` heading requirement and its consequence (4 locations)
- `151-159` «"a `SHONEN.md` checklist assessment for that lane's shokunin, under a `SHONEN` heading … a report missing the `SHONEN` heading is a conformance defect AND is disqualified as evidence in that lane's promotion review"»
- `99-103` «"41 missing a `SHONEN`-led heading (`grep -rLE …` → 41 of 45 …)"»
- `267-268` «"checks each report for the contract-required `SHONEN` heading"»
- `88` (embed item)
- **Canonical:** `151-159`.
- **Merge:** nothing new in `267-268`; keep `99-103` as the measurement (dated).

### D17 · aggregator-owned files: lanes never commit them; aggregator commits at creation, pathspec-limited (4 locations)
- `390-394` «"Every file it creates inside a child repo is **committed by the aggregator itself at creation time**, pathspec-limited to its own files … and a lane never commits an aggregator-owned file."»
- `193-198` «"Uncommitted **aggregator-owned** files (`corpus/lessons/round-*-aggregator-*`) are not the lane's to commit: the lane records them in its report and leaves them for the aggregator to resolve"»
- `264-266` «"uncommitted aggregator-owned files are reported, not lane debt"»
- `560-562` «"no lane edits another lane's or the aggregator's corpus files; `round-<N>-aggregator-*.md` are aggregator-owned."»
- **Canonical:** `390-394`.
- **Merge:** `193-198`'s respawn-handoff duty (unique) and `560-562`'s edit-vs-commit distinction (edits, not just commits).

### D18 · aggregator ledger canonical path / queue-of-record (6 locations) — contradiction (b)
- `395-402` «"maintains one rolling audit ledger — canonically `.ufo/reports/AGGREGATE.md` … While the canonical ledger does not exist, the integrator's round notes are the queue of record"»
- `284-287` «"keeps an **open routed-defects row** in its `AGGREGATE.md` ledger"» (basename only, no path)
- `290-292` «"The ledger row — not round notes alone — is the durable queue … while the aggregator is absent the integrator's report itself is the fallback record."»
- `90-92` «"the aggregator prompt … embeds *its* operative set verbatim: report path, the ledger path and refresh duty …"» (the path is never given)
- `403-408` «"The ledger is append-only in the same sense as `LOG.md` … An aggregator round report is incomplete unless the ledger was refreshed or the report names why no row changed"»
- `498` «"and an open row in the aggregator ledger"»
- **Canonical:** `395-398` (the only place that states the path).
- **Merge:** nothing should be deleted blindly — collapse to one path statement at `395-398` and make `284-287`, `498`, `90-92` pointers to it. Full verdict in §Contradictions (b).

### D19 · append-only: corrections are appended, never in-place (7 locations)
- `124-127` «"Corrections land as new commits, never by amending a cited one — and append-only files (`LOG.md`) take an appended correction entry pointing at the superseded text, never an in-place rewrite"»
- `342` «"never an in-place edit, same discipline as `LOG.md`"»
- `375-382` «"**`rounds` is append-only after closure.** Corrections are appended entries carrying `type: "closure-correction"` and `supersedes: {round, type, date}` …"»
- `403-404` «"The ledger is append-only in the same sense as `LOG.md` — refresh sections supersede earlier rows explicitly rather than rewriting them."»
- `450-452` «"**A falsified claim in an append-only file gets a named correction entry in the lane's next round** — appended, never rewritten"»
- `502-503` «"`LOG.md` is append-only: entries are never rewritten or deleted; corrections land as new entries."»
- `560-562` «"Corpus corrections are new entries, never in-place rewrites"»
- **Canonical:** `502-503` for the invariant; each artifact's application keeps only its artifact-specific mechanic.
- **Merge:** the per-artifact specifics (`supersedes:{round,type,date}`, the `LOG.md` appended-correction-entry form, the ledger refresh-section form) must each be stated exactly once; today the generic clause is repeated 4× and the `LOG.md` referent is invoked 3×.

### D20 · `in-flight` rows → closure-correction entries; last row for a lane wins
- `339-346` «"Every `in-flight` row is resolved by the next protocol round, which appends `{"round": N, "type": "closure-correction", …}` — never an in-place edit, same discipline as `LOG.md`. `rounds[].round` is therefore not unique: consumers read the array in order and the last row for a lane wins."»
- `375-382` «"Corrections are appended entries carrying `type: "closure-correction"` and `supersedes: {round, type, date}` … Consumers read the array in order; the last row for a lane wins."»
- **Canonical:** `375-382`.
- **Merge from `339-346`:** "A lane dispatched for its Nth round *after* round `N` closed rides the next closure-correction for `N` — never dropped, never folded into `N+1`" (unique; keep with the `in-flight` bullet).

### D21 · integrator-of-record scope = appending `MANIFEST.json` `rounds`
- `232-234` «"appending `MANIFEST.json` `rounds` entries"»
- `297-299` «"Appends one entry to `MANIFEST.json`'s `rounds` array (integrator-of-record scope …)"»
- `511-512` «"as integrator-of-record, `MANIFEST.json` `rounds` appends; `MANIFEST.json` edits *outside* `rounds` (roster, rank, minting) remain operator-side integrator work."»
- **Canonical:** `297-299`.
- **Merge:** `511-512`'s outside-`rounds` boundary; `504-505` ("`MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it") is a **different** obligation — keep.

### D22 · `.ufo/prompts/*.md` must be committed to be durable
- `234-235` «"committing already-generated `.ufo/prompts/*.md` so dispatch evidence is durable"»
- `316-317` «"The committed `.ufo/prompts/<lane>-round-N.md` corroborates mission *content* and must be committed to be durable"»
- `517-521` «"as are that round's generated `.ufo/prompts/*.md` — an untracked prompt is non-durable dispatch evidence (round-10: 8 of 58 prompt files untracked …)"»
- **Canonical:** `517-521`.
- **Merge:** `316-317`'s "corroborates mission *content*" qualifier (vs the log line proving *dispatch*) is unique.

### D23 · lane write scope; only integrator roles write main-repo files; pathspec-limited commits
- `513-527` «"Lanes write only inside their own child repo and their lane report … Only integrator roles write main-repo files …"»
- `388-390` «"It is the sole exception to lane write-scope: it may create or repair `corpus/` inside any child repo — nothing else: no main-repo files outside its own report and ledger."»
- `537-541` «"A lane's main-repo commit is pathspec-limited to its own report file (`git commit -- .ufo/reports/round-<N>/<id>.md`) — never `commit -a` / `add -A`"»
- `89-93` (prompt embed items: "the lane's write scope", "the corpus-only write scope")
- **Canonical:** `513-527`.
- **Merge:** `537-541`'s exact commit recipe and the `commit -a`/`add -A` rationale (unique; only place with the command).

### D24 · `.ufo/state/` + `.ufo/watchdog.log` are runtime, no lane commit may include them
- `522-527` «"`.ufo/state/` and `.ufo/watchdog.log` are driver runtime that churns every tick … so no lane commit may include them — pathspec-limited commits are the enforcement; untracking them is operator-side work named in the round notes."»
- `238-239` «"`scripts/` and `.ufo/state/` remain operator-side"»
- **Canonical:** `522-527`.
- **Merge:** nothing unique in `238-239`; reduce to a pointer.

### D25 · evidence standard: resolvable pointer; numeric claim carries its counting command
- `412-415` «"Everywhere the protocol says *evidence*, it means a resolvable pointer …"»
- `425-429` «"A numeric claim carries its counting command, an absence claim its search sweep, and a quote its location …"»
- `470-473` «"Verification is mechanical …"» / «"Every score is a claim: it carries the counting command that produced it and the commit it was measured against"»
- `569-572` «"An axis-move inherits the evidence standard: before and after numbers each carry the counting command and the commit they were measured against"»
- **Canonical:** `412-415` (+`425-429` as detail).
- **Merge:** `568-572`'s "a score no reader can re-derive is an opinion, not a measurement" (unique phrasing, keep once); `473` is the third restatement of the same score rule → with `569-572` it is the clearest true duplicate pair in this cluster.

### D26 · main-repo lanes keep `SCORECARD.md` (and `LOG.md`) at the main-repo root
- `515-517` «"the two main-repo lanes (`protocol`, `aggregator`) additionally keep `SCORECARD.md` and `LOG.md` at the main-repo root"»
- `473` «"Main-repo lanes keep theirs at the main-repo root"»
- `567-569` «"measured in `SCORECARD.md` (per child repo; the two main-repo lanes keep theirs at the main-repo root)"»
- **Canonical:** `515-517` (complete: both files + the reason).
- **Merge:** nothing unique in `473`/`567-569` beyond what is at `515-517`; keep the axis-move duty from `567-574` but drop the path restatement.

### D27 · SSOT precedence: `MISSION.md` vs `PROTOCOL.md`
- `575-576` «"`MISSION.md` is the mission SSOT: fleet shape, model map, concurrency floor, push rule, L0 side channel. Watchdog prompts bind to it."»
- `577-582` «"Precedence between the two SSOTs: `MISSION.md` owns fleet shape, the model map, the concurrency floor, the push rule, and the L0 channel; `PROTOCOL.md` owns process, evidence, and gates …"»
- `93-94` «"the L2 minimum — a number this file does not own: `MISSION.md` §L2 concurrency is its source"»
- **Canonical:** `577-582`.
- **Merge:** `575-576`'s "Watchdog prompts bind to it" (unique) and `93-94`'s ownership assertion of the L2 number into the precedence bullet; the duplicated ownership list may then be stated once.

### D28 · open routed-defect row until the owning lane's correction lands
- `282-287` «"routes cross-domain defects … The aggregator mirrors each routed defect into the owning repo's `corpus/lessons/` … and keeps an **open routed-defects row** in its `AGGREGATE.md` ledger until … correction lands"»
- `450-452` «"it stays on the routed-defect queue until it lands"»
- `498` «"and an open row in the aggregator ledger"»
- **Canonical:** `282-287`.
- **Merge:** `450-452`'s naming of *where* the correction entry goes ("in the lane's next round") — unique.

### D29 · orphan prompt (no dispatch line) = attempted dispatch → `failed`
- `315-319` «"a prompt with no dispatch line is an attempted dispatch and records `failed`"»
- `165-169` «"`failed` covers every lane-round that was prompted or dispatched and has no report by closure, including a prompt left behind by a launch that failed (`lane_prompt()` runs before `ufo-sighting launch` …)"»
- **Canonical:** `315-319` (owns the dispatch-evidence definition).
- **Merge:** `167-169`'s "0 observed as of round 10, structural" measurement.

### D30 · operator-owned domain actions vs ordinary bookkeeping
- `530-537` «"**domain-facing actions are operator-owned** … Repo bookkeeping — committing and `git push`ing the round's commits — is ordinary lane work, not publishing, when the driver instructs it. Exception: operator-gated artifacts …"»
- `417-423` «"Where the domain's terminal action is operator-owned (vault approval, publish click, claim submission), executed means *prepared + verified + handed off*"»
- **Canonical:** `530-537` for the push/hold rule; `417-423` for the "what executed means" rule.
- **Merge:** neither is wholly redundant — but the identical list "(vault approval, publish click, claim submission)" appears in both; state it once and point.

---

## Contradictions

### (a) "keeps its round open indefinitely" vs "a missing report never holds a round open in the integrator's ledger" — **VERDICT: genuine contradiction in scope; `143-146` is the wrong instance**
- `143-146`: «"For the current respawn driver the report file's existence is also the round-completion signal: a lane that finishes all other work but files no report **keeps its round open indefinitely** (covered by the stale-lane rule below)."»
- `161-164`: «"A lane whose mission has terminated or been respawned without filing its round report is recorded `failed` by the integrator; **a missing report never holds a round open in the integrator's ledger** — though it does hold the *driver* open, since `report_of()` is the driver's completion signal and the mission stays live until the stale-lane rule below fires."»
- Third instance, same duty: `251-253`: «"A round is **completed** when every dispatched lane has either reported or been recorded failed by the integrator — a failed lane counts; **a missing report does not**."»
- Unqualified "indefinitely" also collides with the two-tick bound at `170-173` ("A mission still open more than two driver ticks after its steer is a stale-lane review trigger … the integrator may record it `failed`") and with `187-188` ("the driver's respawn path is unreachable while its daemon is up (step 4), so nothing in this section terminates live work").
- **Canonical:** `161-164` (ledger-level, and it explicitly splits ledger vs driver). **Rewrite `143-146`** to "keeps the driver-side mission open (the integrator's ledger still records `failed` — below)" and drop "indefinitely"; keep `251-253` as the definition of round completion. Note the residual empirical truth at `185-188` + `.ufo/reports/round-10/protocol.md:284-285` ("a genuinely dead lane currently hangs until an operator runs `omp down`") — the *driver* hold is indefinite in practice, which is exactly why the scope must be stated in both places.

### (b) aggregator ledger canonical path / queue-of-record — **VERDICT: path is stated once and echoed 5×; the queue-of-record is a tri-state; the "absent" premise is now falsified by the tree**
Distinct statements (7 in `PROTOCOL.md`; 2 outside):
1. `395-398` (canonical path): «"it maintains one rolling audit ledger — canonically `.ufo/reports/AGGREGATE.md` (the `round-2/AGGREGATE.md` snapshot is relocated there by its next refresh; until then it remains readable evidence — superseded, not voided — and no third path counts)."»
2. `399-402` (queue of record while absent): «"While the canonical ledger does not exist, the integrator's round notes are the queue of record: the round-10 audit found `.ufo/reports/AGGREGATE.md` absent (`ls .ufo/reports/AGGREGATE.md` → no such file), so every defect routed since round 5 lived only in report prose with no durable row."»
3. `290-292` (queue of record, opposite subject): «"The ledger row — not round notes alone — is the durable queue, since defects outlive the round that routed them; while the aggregator is absent the integrator's report itself is the fallback record."»
4. `284-287` (ledger named by basename only): «"keeps an **open routed-defects row** in its `AGGREGATE.md` ledger until the owning lane's `corpus/lessons/` or `SKILL.md` correction lands; unresolved rows are re-flagged in the ledger each audited round."»
5. `90-92` (path asserted to exist as prompt content, never given): «"the aggregator prompt instead embeds *its* operative set verbatim: report path, **the ledger path** and refresh duty …"»
6. `403-408` (refresh duty attached to "the ledger"): «"The ledger is append-only in the same sense as `LOG.md` … An aggregator round report is incomplete unless the ledger was refreshed or the report names why no row changed"»
7. `498` (Invariants): «"and an open row in the aggregator ledger"»
8. Outside the file — the ledger artifact itself, `.ufo/reports/AGGREGATE.md:555-557`: «"Ledger canonical location per round-6 PROTOCOL.md is `.ufo/reports/AGGREGATE.md`; this file lives at `.ufo/reports/round-2/AGGREGATE.md`. Relocation is a main-repo structural change = integrator action; refresh 3 appends in place."»
9. Outside the file — the dispatch prompts define a *different* path shape: `.ufo/prompts/aggregator-round-4.md:3` «"and round-3/AGGREGATE.md if present"»; `.ufo/prompts/aggregator-round-5.md:3` «"and round-4/AGGREGATE.md if present"»; `.ufo/prompts/aggregator-L1.md:9` «"Write .ufo/reports/round-1/AGGREGATE.md"». (kotoba round-7 report: «"three-way definition divergence PROTOCOL.md vs spawn prompt vs generator"» — `.ufo/reports/round-7/kotoba.md:93-97`.)
**Now-false premise (re-executed):** the canonical ledger **exists** in the current tree and the round-2 snapshot does not:
- `ls -la .ufo/reports/AGGREGATE.md` → `-rw-r--r-- 1 vgpnk vgpnk 43541 Sep 28 16:41 .ufo/reports/AGGREGATE.md`
- `ls -la .ufo/reports/round-2/AGGREGATE.md` → `No such file or directory`
- `git status --short .ufo/reports/` → `R  .ufo/reports/round-2/AGGREGATE.md -> .ufo/reports/AGGREGATE.md` (staged rename, **not committed**: `git log --all --oneline -- .ufo/reports/AGGREGATE.md` prints nothing)
- content is still the round-3 refresh: `.ufo/reports/AGGREGATE.md:4` «"**Refreshed:** 2026-09-28 at driver round 3"»
So `399-402`'s "does not exist / `ls` → no such file" and `396-398`'s "until then it remains readable evidence" are both stale; and with the ledger present, `290-292` ("the ledger row … is the durable queue") and `399-402` ("the round notes are the queue of record") now assert *different* queues of record without a precedence rule.
**Canonical:** `395-398` for the path; exactly one queue-of-record sentence, subordinate to ledger-existence (recommend: "the ledger is the queue of record; while it is absent or unrefreshed, the integrator's round notes are the queue of record and `notes` carries the pointer"). Count for the compaction move: **7 in-file statements + 2 out-of-file path definitions** (SCORECARD.md:50-51 called this "three ledger-path statements" — the path itself is stated in 1 place, echoed in 5, and contradicted by 2 prompt-side path shapes).

### (c) three further contradictions found in passing (not in the acceptance list; each needs a verdict at compaction)
- **(c1) embed clause vs the measurement.** `95-96`: «"The protocol prompt embeds its own duties: this file's re-read requirement, the integrator-of-record closure steps, and the L2 minimum."» vs `243-247`: «"the generated protocol prompts name none of steps 1–4 (`grep -c MANIFEST .ufo/prompts/protocol-round-10.md` → 0 …)"». Same shape for the aggregator at `90-93` vs the prompt files (item 9 above). **Verdict:** one sentence is normative ("embeds"), the other descriptive; state the duty as "must embed" and keep the measurement as a defect record.
- **(c2) log line numbers: declared non-durable, still cited.** `334-338`: «"`.ufo/watchdog.log` is mutable and the driver appends to it concurrently, so its line numbers drift: the round notes carry a committed digest (timestamp + text) … and that digest — not the live log — is the pointer that resolves at closure."» Yet the same file cites log **line numbers** at `177-178` (`.ufo/watchdog.log:117,126`), `255` (`.ufo/watchdog.log:88,130`), `356` (`.ufo/watchdog.log:3`). **Verdict:** keep the rule, convert the three citations to timestamp+text.
- **(c3) two uncommanded, now-false measurements** (violating the file's own numeric-claim rule at `425-426`).
  - `131-133`: «"21 reports were added by `6565e89`, 21 by `609ecb6`, 4 by `0a30b44` — 46 of 60 swept into three commits"»; re-executed: `git show --diff-filter=A --name-only --pretty=format: <hash> -- '.ufo/reports/round-*/*.md' \| grep -c 'ufo/reports/round-'` → **21 / 21 / 4** (agrees), but the denominator is now **64**, not 60 (`ls .ufo/reports/round-*/*.md \| wc -l` → 64).
  - `554-556`: «"0 of 60 reports were added by a lane-identity commit — 33 by the operator's identity and 26 by `shokunin <shokunin@local>`"»; re-executed by adding-commit author: `35 Joao Pedro Veiga <jpveigao10@gmail.com>`, `26 shokunin <shokunin@local>`, `1 protocol-shokunin <protocol@shokunin.local>`, `1 kumitate <kumitate@shokunin.local>`, `1 kengaku-shokunin <kengaku@shokunin.local>` → **64 total, 3 by lane identities, 35 by the operator**. So "0 of 60 … 33" is false on both counts today (the 26 holds).
  - `223-226` is the same class: «"Rounds 2–11 produced no closure artifact: `MANIFEST.json` `rounds` held `[0, 1, 1.5, 9]`"» while `jq '.rounds|length' MANIFEST.json` → **15** (round-10 report D-34: "LANDED this round (`640a4c5`, entries 4 → 15)").
  **Verdict:** these belong in the dated-incident appendix the SCORECARD compaction move already plans; each must carry its counting command or be dropped.

---

## Reconciliation with the audit's 17

Collapsing my 30 clusters into the round-10 audit's coarse families gives **exactly 17**:

| # | Family | Clusters |
|---|---|---|
| 1 | mint bar | D1 |
| 2 | shokunin promotion bar | D2 |
| 3 | verifier marks / non-author rule | D3 |
| 4 | jin'i-ryu bar | D4 |
| 5 | main repo aggregates only promotion/mint | D5 |
| 6 | prompt snapshot + re-read | D6 |
| 7 | embed items ↔ closure check | D7 |
| 8 | `scripts/` operator-side correction channel | D8 |
| 9 | per-lane counters | D9 |
| 10 | report lands last / commit citation | D10 |
| 11 | lane-identity commits | D11 |
| 12 | completion signal / report path | D12 + D15 |
| 13 | missing report / marker / stale-lane → `failed` | D13 + D14 + D29 |
| 14 | `SHONEN` heading | D16 |
| 15 | write scope / aggregator-owned files / runtime paths | D17 + D23 + D24 |
| 16 | ledger path, queue of record, append-only, closure-correction, MANIFEST scope, prompt durability | D18 + D19 + D20 + D21 + D22 + D28 |
| 17 | evidence standard / SSOT precedence / SCORECARD home / operator-owned actions | D25 + D26 + D27 + D30 |

## Single-instance obligations (no duplicate — do not delete at compaction)
`28-32` dormancy · `68-70` round-robin dispatch · `72-77` monotonic round numbers · `136-138` swept-report attribution · `157-159` assessment re-filed, not the report · `170-185` stale-lane trigger + progressing/silent test · `200-218` marker taxonomy · `262-276` step 1 checks · `300-302` round-entry shape · `304-310` partial entries / `closed_at` · `311-318` dispatch/completion/termination evidence · `324-333` liveness probes are not evidence · `347-357` evidence-contradicting rows · `358-366` `lane_rounds` map · `367-374` retroactive closure termination · `375-382` index-citation preservation (`rounds[1]` ×13) · `403-408` ledger refresh duty · `417-423` end-to-end task definition · `431-439` closure-time pointer resolution · `441-461` evidence-standard bullets (claimed≠re-executed, sweep, hash, drift pins) · `465-473` file-contract table · `475-487` `SHONEN.md` seed · `491-499` specialize/contested-scope · `500-503` evidence-driven rounds · `528-529` meta-domain · `534-536` operator-gated hold · `557-562` corpus evidence standard · `567-574` axis-move duty · `583` L0 channel.

## Artifacts
- This file: `/tmp/shokunin-r11/protocol-dupes.md` (read-only audit; no repo file touched).