# Critic — diff-review of the round-11 `PROTOCOL.md` compaction

Lane: protocol (integrator-of-record) · Round 11 · 2026-09-28 ~19:52 -03:00
Role: critic (semantic layer above the 93-predicate machine census, which passes 93/93 and is not re-run here).

## 0. Basis

| Item | Identity (re-executed) |
|---|---|
| Original | `git -C ~/projects/shokunin show HEAD:PROTOCOL.md` → 583 lines, `md5sum` → `a89395757757044f2923c41a3a4ab74c` |
| Candidate | `/tmp/shokunin-r11/protocol-100.md` as of **mtime 19:49:31 -03:00, 444 lines, md5 `256d90bf18d5164fa1141fbd6c063a18`**; pinned copy at `/tmp/shokunin-r11/critic-snapshot-protocol-100.md` |
| Volatility | The candidate was under active edit during this review: an earlier 445-line revision (read ~19:47) carried a different local-first bullet ("Domain source repos that lanes study … (operator rule, 2026-09-28)"). All quotes below are from the pinned 444-line snapshot; its md5 was stable through 19:52. **Land against the same md5 or re-diff.** |
| Supporting audits | `obligations.md` (91 O-rows, 583-line tiling), `protocol-dupes.md` (30 clusters, 96 instances, contradictions (a)/(b)/(c1–c3)), `appendix-draft.md` (40 extracted incident facts) |
| Seed check | SHONEN seed block extracted from both files and diffed: **byte-identical** (`diff` → empty; seed md5 `df5878d39bceab00903213dfc0fd8e13`) — agrees with the machine census. |

Method: every O-01…O-91 row was located in the candidate and compared sentence-by-sentence against the original; every appendix pointer was re-resolved against the table; every new/changed factual figure was re-executed against the repo (read-only).

---

## 1. Semantic drift walk — 91 obligations

**Headline: 0 of 91 obligations lost their normative force; every MUST/NEVER/ONLY/definition has a surviving home in the candidate.** Drift found is confined to (i) four factual/pointer defects in the new appendix, (ii) six minor incident-detail losses, (iii) two wording spots. Per-obligation census (candidate line numbers from the pinned snapshot):

| O | Home (cand. ≈L) | Verdict | Note |
|---|---|---|---|
| O-01 | 11–14 | OK | "the bar closure step 3 applies, stated once here" → "the mint bar, stated once here; closure step 3 applies it" — same bar, same single-statement rule |
| O-02 | 15–17 | OK | skill-file clause moved to gates L43–45, incl. "— real craft, not generic advice" (orig. "not generic advice"); "LOG.md shows completed rounds" kept at L16 |
| O-03 | 18–19 | OK | D4/D5 merge applied; "given the round's telemetry" preserved in the gate (L52–53) |
| O-04 | 21–24 | OK | dormancy verbatim incl. "never an automatic retirement" |
| O-05 | 31–32 | OK | "Every gate names its verifier and its evidence" kept |
| O-06 | 33–38 | OK | non-author rule, `[x]`→`[~]` degradation kept (L39) |
| O-07 | 39–47 | OK | 4-box minimum bar kept; "at least one decision table, one error-pattern list, and one checklist, each citing a resolvable source" |
| O-08 | 49 | OK | delete/rank-update/record kept |
| O-09 | 51–53 | OK | falsifiable improvement + falsification condition kept; duplicate "main repo aggregates only the promotion decision" dropped per D5 (mint-inclusive form kept at L22) |
| O-10 | 57–59 | OK | round-robin + "never as an implicit no-op" |
| O-11 | 61–64 | OK | monotonic rounds, skipped-round, duplicates-allowed tail kept |
| O-12 | 67–70 | OK | snapshot clause + re-read duty |
| O-13 | 71–80 | OK* | item sets intact; "(currently 8 subagents in one batched call)" dropped — deliberate: the number is MISSION-owned, dropping it prevents exactly the staleness class the dupes audit's (c3) documents. *Not a drift. |
| O-14 | 81–82 | OK | "the integrator's report must also carry the exact corrected `lane_prompt()` text required, since `scripts/` is operator-side" |
| O-15 | 85–88 | OK | per-lane counters |
| O-16 | 89–96 | OK | lands-last, HEAD-cite, ancestry check `git merge-base --is-ancestor`, no-amend, LOG correction-entry form — all kept; r9 incident → appendix |
| O-17 | 97–98 | OK | "the commit that adds … carries the lane identity, because the driver completes the mission the instant the file reaches disk" |
| O-18 | 99–101 | OK | swept-report clause + "history is never rewritten to fix attribution" |
| O-19 | 103–108 | OK (improved) | contradiction (a) fix applied: orig. "keeps its round open indefinitely (covered by the stale-lane rule below)" → "keeps the *driver's* mission open until the stale-lane rule below fires, while a missing report never holds a round open in the *integrator's ledger* — there the lane-round is recorded `failed` at closure". Scope now split exactly as dupes (a) prescribed |
| O-20 | 109–113 | OK | 4-item minimum content |
| O-21 | 114–118 | OK | "(reports are filed once; the assessment, not the report, is re-filed)" → "(reports are filed once; the assessment is not)" — same meaning; "Consequence, not just a label:" → "Consequence:" (rhetoric dropped, force intact) |
| O-22 | 120–122 | OK | failed-on-no-report + "prompted or dispatched" + orphan prompt |
| O-23 | 123–130 | OK | two-tick trigger + actuator + launch-timestamp age |
| O-24 | 131–133 | OK | progressing/silent + `find -newermt` probe kept verbatim |
| O-25 | 134–139 | OK | "records `failed` only for silent missions", "ledger act, not a kill", respawn-path-unreachable "(step 4)"; commit-sparsity figures → appendix |
| O-26 | 140–142 | OK | inherited-work resolution |
| O-27 | 142–144 | OK | aggregator-owned files left for the aggregator; r9 incident → appendix |
| O-28 | 145–147 | OK* | "so a contentless **completion marker** closes a lane-round" → "**can** close" — slight modal softening, but accurate (the binding consequences live in O-29/O-31, which survive). *Benign. |
| O-29 | 148–150 | OK | marker → `failed` + defect kept + counter advancement named |
| O-30 | 151–152 | OK | defective-ok classification kept; figures → appendix |
| O-31 | 152–153 | OK | + improved generalization: "real work sitting unattributed in child repos does not rescue it" (the r5 incident's lesson, kept as a rule) |
| O-32 | 154 | OK | "This does not relax step 1" |
| O-33 | 156–158 | OK | integrator-of-record + "never MANIFEST.json" example + snapshot-wins |
| O-34 | 158–163 | OK | three expansions enumerated; scripts/.ufo/state operator-side "(§Invariants)"; "Everything else stays …" folded into "Its main-repo writes are …" — same scope |
| O-35 | 164–166 | OK | closure artifact + "the only guaranteed delivery channel" |
| O-36 | 170–171 | OK | round-completed definition ("a failed lane counts; a missing report does not") |
| O-37 | 172–175 | OK | per-lane-round closure + unresolved rows |
| O-38 | 177–185 | OK | all five step-1 checks incl. L2 route-map↔MISSION bucket; r9 route-map incident → appendix |
| O-39 | 186–196 | OK | routing incl. self-defects; open ledger row until correction lands; first-audited-round sweep duty; "The ledger row — not round notes alone — is the durable queue". Original's "; while the aggregator is absent the integrator's report itself is the fallback record" dropped — see D18 note in §2 (consequence preserved via routing-line duty + round-notes fallback; round notes live inside the integrator's report) |
| O-40 | 198–200 | OK | mint bar pointer to Lifecycle; ROADMAP-drift defect rule kept |
| O-41 | 201–207 | OK | entry shape + 4 statuses + optional keys |
| O-42 | 208–213 | OK | partial entries; `closed_at` required on `not-dispatched` |
| O-43 | 214–222 | OK* | dispatch/completion/termination evidence intact; "rounds 1–3 … 8 real lane-rounds" → "the earliest rounds … real lane-rounds (§Appendix, "Dispatch evidence")" — figures pinned to the appendix row, which carries "8 real lane-rounds". *OK. |
| O-44 | 223–228 | OK | probe-independence rule; probe incident → appendix row "Liveness probes" (all figures preserved: kasegi r12/kagi r9/kake r10, 18:27:55-58, 0/135, `omp down`) |
| O-45 | 228–231 | OK | committed-digest rule full ("that digest — not the live log — is the pointer that resolves at closure") |
| O-46 | 232–238 | OK* | in-flight debt, closure-correction append, rides-next-correction, never-dropped/never-folded — plus NEW re-confirmation clause; wording tension flagged as F8 |
| O-47 | 239–241 | DEFECT (F1) | rule kept; pointer "(§Appendix, "Contradicted rows")" resolves to nothing — see §4 |
| O-48 | 242–246 | OK | lane_rounds map required on not-dispatched; `ok` derivability; notes pointers |
| O-49 | 248–253 | OK | retroactive typing incl. fleet-2/`609ecb6` clause |
| O-50 | 254–257 | OK | append-only rounds + `supersedes` + index-citation rationale; r10 citation count → appendix (figure defect F2) |
| O-51 | 258 | OK | consumers read in order; last row wins |
| O-52 | 260–267 | OK | aggregator scope, commit-at-creation, subject form, lane-never-commits |
| O-53 | 268–270 | OK | canonical `.ufo/reports/AGGREGATE.md` + "no third path counts" + relocation clause |
| O-54 | 271–272 | OK (improved) | "While the canonical ledger does not exist" → "is **absent or unrefreshed**" — correct generalization; stale `ls → no such file` premise removed from body, kept dated in appendix row |
| O-55 | 273–276 | OK | append-only ledger + refresh-or-reason rule + empty-queue-by-construction |
| O-56 | 279–281 | OK | evidence definition |
| O-57 | 283–287 | OK | end-to-end task + operator-gated "prepared + verified + handed off" (D30 applied: list stated once at §Invariants, pointed to) |
| O-58 | 289–292 | OK | counting command / sweep / quote location / probe |
| O-59 | 294–296 | OK | closure-time resolution; incidents → appendix |
| O-60 | 297–299 | OK | future-dating defect; incident → appendix |
| O-61–63 | 301–308 | OK | re-execution / corrections sweep / named correction entry — all kept |
| O-64 | 309 | OK | hash-never-tag + `git rev-parse round-4` failmode (now in the bullet itself) |
| O-65 | 311–318 | OK* | full rule kept; only the inline example "(e.g. `kagi-shokunin/corpus/drift-pins.sh`)" dropped — F6c, minor |
| O-66 | 321 | OK | SKILL.md frontmatter rule |
| O-67 | 322 | OK | PROVINCE surfaces |
| O-68 | 323 | OK | LOG.md contract row |
| O-69 | 324 | OK | SHONEN mechanical verification + seed byte-identity + mark confinement |
| O-70 | 326 | OK | corpus row + aggregator review duty |
| O-71 | 327 | OK | SCORECARD re-derivability |
| O-72 | 340 | OK | marks line kept verbatim (D3's "delete or reduce to the pointer" not taken — harmless, it carries the pointer) |
| O-73 | 345–346 | OK | cited-and-verifiable |
| O-74 | 347–352 | OK | contested scope, arbitration, re-flag, silence-never-defaults |
| O-75–76 | 353–354 | OK | evidence-driven + LOG append-only |
| O-77 | 355–357 | OK | MANIFEST canonical; integrator-only main-repo writes |
| O-78 | 357–359 | OK | operator-side files; names-but-never-edits |
| O-79 | 359–361 | OK | rounds-appends scope + outside-rounds boundary |
| O-80 | 361–364 | OK | lane write scope + main-repo-lane SCORECARD/LOG home |
| O-81 | 365–367 | OK | reports/waves/prompts committed; untracked-prompt defect; round-10 measurement → appendix "Prompts committed" |
| O-82 | 367–370 | OK | runtime paths excluded from lane commits; untracking operator-side |
| O-83 | 371–372 | OK | meta-domain patterns |
| O-84 | 373–387 | OK + NEW (F7) | local-first core kept; NEW push-scope/read-only text — audited in §3(a) |
| O-85 | 388–391 | OK | lane-identity at mint; kotoba incident → appendix "Lane identity"; the stale live-tree claim "(kagi/kake/kumitate/kengaku already do)" dropped — staleness removed, incident preserved |
| O-86 | 389–390 | OK | `-c user.name/user.email` recipe kept |
| O-87 | 392–395 | OK | corpus evidence inheritance + edit-direction rule |
| O-88 | 398–403 | OK | axis-move + counting commands + file-contract precedence |
| O-89 | 404 | OK | MISSION SSOT + "Watchdog prompts bind to it" (D27's unique content kept) |
| O-90 | 405–409 | OK | precedence merged into one bullet (D27 applied): ownership list stated once, conflict example kept, "neither file is edited by a lane" |
| O-91 | 410 | OK | L0 side channel — file-final line survived (obligations §D predicted its loss; it did not happen) |

**Walk result: 91/91 obligations survive with meaning intact; verdicts OK except where flagged (F1 pointer; F8 wording).**

---

## 2. Dropped nuance — 30 dupe clusters vs candidate

| Cluster | Merge rec (dupes audit) | Candidate | Unique content of non-canonical instances | Verdict |
|---|---|---|---|---|
| D1 mint bar | replace step-3 restatement with pointer; keep ROADMAP-drift rule | applied (L198–200; L14 pointer) | mint action + ROADMAP rule kept | OK |
| D2 promotion bar | fold 20–23 into 50–57; Lifecycle → one-line pointer | applied | "not generic advice" → gates "— real craft, not generic advice"; "completed rounds" plural kept at L16 (original plural-vs-at-least-one tension **retained unchanged**, not resolved — same as HEAD) | OK |
| D3 verifier marks | reduce L486–487 to pointer | kept verbatim with pointer (harmless restatement) | `[~]`-asserted/`[x]`-verifier semantics intact; promotion-review disqualification kept at L117 | OK |
| D4 jin'i-ryu bar | keep 60–64; move 24–26's tail | applied | "main repo aggregating only promotion/mint decisions" kept at L22 | OK |
| D5 aggregation scope | canonical 63–64; keep 297–299's lane-LOG clause | applied | "(each lane's own `LOG.md` entry remains lane work, not integrator work)" kept in step 4 (L202) | OK |
| D6 snapshot clause | merge example + role assignment | applied | both kept (L68, L157) | OK |
| D7 embed ↔ step-1 check | add route-map to embed list OR drop "five … per the embed clause" phrasing | neither taken — original phrasing kept (L179–182); route-map check kept | no loss; "five contract items" still defined by the embed clause | OK (rec optional) |
| D8 scripts operator-side | move "exact corrected `lane_prompt()` text" toward canonical; keep three-expansion enum | duty kept once at L81–82 (original home), enum kept at L159–161 | both duties present exactly once | OK |
| D9 per-lane counters | merge closure consequence + measurement | applied | "Closure is therefore per lane-round" kept (L173); 17:57/16:47 measurement → appendix (log line numbers converted to timestamps per (c2) fix) | OK |
| D10 lands-last/citation | keep tag failmode as own bullet, stop restating ordering | applied | "`git rev-parse round-4` fails wherever the tag doesn't exist" kept in the bullet itself (L309) | OK |
| D11 lane identity | merge swept-still-landed + counter-advance; measurements stale → dated appendix | applied | swept rule kept (L99–101); measurement → appendix — **but the appendix row is defective, see F3** | DRIFTED (F3) |
| D12 completion signal | fix contradiction (a); delete duplicate framing | applied (see O-19) | driver-vs-ledger split preserved once | OK |
| D13 missing-report/marker | reduce 319–322 to pointer | kept with "(see above)" pointer (harmless) | rule + pointer | OK |
| D14 respawn unreachable | keep "ledger act, not a kill" once + probe evidence | applied | both kept in respective homes | OK |
| D15 report path | keep aggregator.md special case | applied | `.ufo/reports/round-<N>/aggregator.md` kept (L261) | OK |
| D16 SHONEN heading | keep measurement dated | applied | 41/45 + command + `0a30b44` pin in appendix row | OK |
| D17 aggregator-owned files | keep respawn-handoff + edit-vs-commit | applied | both kept (L142–144, L392–395, L186–187) | OK |
| D18 ledger path / queue-of-record | one path statement; make 284-287/498/90-92 pointers; one queue-of-record sentence subordinate to ledger-existence | applied | path once (L268–269); step-2 pointer "(canonical path and fallback queue: the aggregator-lane paragraph below)"; Invariants "open row in the aggregator ledger" (basename, no path — acceptable pointer); embed item "the ledger path and refresh duty" kept. Original's aggregator-**lane**-absent fallback sentence ("while the aggregator is absent the integrator's report itself is the fallback record") dropped; covered operationally by routing-line duty + round-notes fallback + first-audited-round sweep | OK (note: lane-absent fallback now implicit) |
| D19 append-only | per-artifact specifics exactly once | applied | `supersedes:{round,type,date}` once (L255–256); LOG correction-entry form once (L95–96); ledger refresh-section form once (L273); "same discipline as `LOG.md`" duplicate dropped | OK |
| D20 in-flight → correction | merge rides-next-correction | applied | kept (L236–237) | OK |
| D21 integrator scope | keep outside-rounds boundary; keep canonical-rank row separate | applied | all three kept (L159–161, L201, L359–361, L355) | OK |
| D22 prompt durability | keep "corroborates mission *content*" qualifier | applied | kept (L218) | OK |
| D23 write scope | keep exact recipe + `commit -a` rationale | applied | kept verbatim (L384–387) | OK |
| D24 runtime paths | reduce 238–239 to pointer | applied ("(§Invariants)") | kept | OK |
| D25 evidence standard | keep "opinion, not a measurement" once | kept both restatements (L327, L400–402) — harmless, no drift | semantics identical | OK |
| D26 SCORECARD home | drop path restatement from table+Fleet-2, keep complete invariant | applied | complete form kept at L362–364 | OK |
| D27 SSOT precedence | merge into one bullet; keep watchdog-bind + L2 ownership | applied (L404–409) | all unique content kept | OK |
| D28 routed-defect row | keep "in the lane's next round" | applied | kept (L307) | OK |
| D29 orphan prompt | merge 0-observed measurement | applied | "(dispatch evidence and orphan prompts: step 4)" + appendix row "Failed covers orphan prompts" (0 observed, structural) | OK |
| D30 operator-owned actions | state the list once and point | applied | "(§Invariants, local-first)" pointer; handoff semantics intact | OK |

**Cluster result: 29 applied or harmlessly unapplied; the one substantive casualty is not a rule but the appendix's Lane-identity figures (F3).**

### Appendix completeness vs appendix-draft (40 extracted facts)

21 table rows carry the draft's facts except:

- **LOST (F5a):** "rounds 2–9: no lane was instantiated as integrator, so no `rounds` entry could be written without inventing statuses" (appendix-draft "Integrator and rounds" §; was original L224–228, elided in candidate with only "(§Appendix, "Closure entries")").
- **LOST (F5b):** "rounds 2–8 produced no closure artifact at all and rounds 5–9 produced report prose instead of `rounds` entries" (appendix-draft; was original L248–249).
- **WEAKENED (F6a):** Closure-entries-9 row drops the kengaku/kotoba/kagi `in-flight`-before-dispatch instances (original L352–354; r10 conformance item 2 has them).
- **WEAKENED (F6b):** "three still do" (round-9 rows still contradicted at r10-write time, original L227–228) dropped from the row.
- **WEAKENED (F6c):** drift-pins example script path dropped entirely (original L456).
- **WEAKENED (F6d):** canonical-form row drops the contrast "untouched mint seeds (kasegi, kake, kumitate) already conform" (appendix-draft has it).
- **WEAKENED (F6e):** Append-only-`rounds` row drops the three example citations (`LOG.md:4`, `corpus/README.md:6`, `corpus/lessons/round-1.md:3`, original L378–380).
- **WEAKENED (F6f):** No-closure-channel row drops the file cite `protocol-round-9.md:3` (original L246).

All F6 items are incident-narrative trim, not normative loss; F5 is a conscious-triage question the integrator should answer explicitly.

---

## 3. New-text audit (the three additions)

### (a) Operator read-only-repos rule (§Invariants local-first, L373–376)

Candidate: «"Push scope is owned by `MISSION.md` §Push scope — hard rule (operator commit `235b414`, 2026-09-28): lanes push only to the main repo and their own `<lane>-shokunin` remote; domain source trees are read-only and upstream-bound work is carried in the round report."»

Verification (all re-executed):
- `MISSION.md` heading `## Push scope — hard rule` **exists**; `git show 235b414 -- MISSION.md` shows that exact section added (+9 lines): "Lanes push ONLY to `VeigaPunk/shokunin` … never commit there, never push to their remotes. Work that belongs upstream is documented in the lane report; the operator owns those pushes." → **the §pointer resolves and the content matches.**
- Date: commit `235b414` → 19:25:03 2026-09-28 ✓.
- No contradiction with the local-first bullet's own clauses (bookkeeping-is-ordinary-work, operator-gated hold, pathspec-limited report commit), with O-90 precedence (MISSION owns the push rule — the candidate *cites* rather than re-owns it, which is the correct direction), or with the aggregator's corpus-commit-at-creation rule (child-lane pushes carry the aggregator's commits; the lane never *commits* them).
- **Nit (F7, non-blocking):** the commit's author is `shokunin <shokunin@local>` — the identity the file itself calls "a third identity that is neither operator nor lane". "(operator commit `235b414`)" is true as "the commit landing the operator's rule" but reads as an authorship claim in a file that polices commit attribution. Suggest "operator rule, landed in `235b414`".

Verdict: **OK** (one wording nit).

### (b) In-flight still-live re-confirmation clause (step 4, L237–238)

Candidate: «"An `in-flight` row whose mission is still live at the next pass is re-confirmed by a closure-correction carrying `in-flight` plus the launch pointer, and stays debt until the mission terminates."»

- Internally consistent with O-47 ("no `in-flight` unless its mission was live at `closed_at`" — the re-confirmation's `closed_at` is the re-confirming pass) and with O-48 (pointer in `notes`).
- **Wording defect (F8):** the bullet's headline still reads «"Every `in-flight` row is resolved by the next protocol round, which appends … `lanes: {<id>: <terminal status>}`"». For a still-live mission the next round's correction carries `in-flight`, not a terminal status, and the row "stays debt" — so "every … is resolved by the next protocol round" is false in exactly the case the new clause creates. One-word fix: "Every `in-flight` row is **answered** by the next protocol round — resolved (`<terminal status>`) or re-confirmed (`in-flight` + launch pointer)."
- No conflict with MISSION.md (silent on `rounds`).

Verdict: **OK semantically, WEAKENED wording (F8)** — fix the headline verb, don't drop the clause (it closes a real gap the original left: the original had no prescribed handling for a still-live mission at the next pass and its "resolved … `<terminal status>`" wording would have forced fabricating a termination).

### (c) Conditional ledger fallback "absent or unrefreshed" (L271–272)

- The original's premise ("While the canonical ledger does not exist … the round-10 audit found `.ufo/reports/AGGREGATE.md` absent") is **now false on disk**: `ls -la .ufo/reports/AGGREGATE.md` → exists (100,054 B, mtime 19:34; header still "Refreshed: 2026-09-28 at driver round 3" ⇒ stale/unrefreshed; `git status --short .ufo/reports/` → ` M .ufo/reports/AGGREGATE.md`, uncommitted).
- The candidate's two-state condition is therefore not just safe but **required** — the original form would have been falsified the moment the ledger file appeared. This is exactly dupes (b)'s recommended rewrite ("absent or unrefreshed, the integrator's round notes are the queue of record").
- Consistent with step 2 ("The ledger row — not round notes alone — is the durable queue") and with the appendix "Ledger" row, which remains a correctly *dated* incident ("round-10 audit found … absent"), satisfying the appendix preamble's "pinned to their measurement round" rule.

Verdict: **OK (improvement).**

---

## 4. Cross-reference integrity

### Appendix pointers — `(§Appendix, "X")` census (15 instances, 14 distinct names)

| Pointer | Instances | Row with `Rule = X`? |
|---|---|---|
| "Prompt embeds contract" | 1 | ✓ (row 1–10) |
| "Lands last" | 1 | ✓ (rows 9, 10) |
| "Stale-lane actuator" | 1 | ✓ (rows 10×2) |
| "Marker vs report" | 1 | ✓ (rows 10, 5) |
| "No closure channel" | 1 | ✓ (row 2–10) |
| "Closure entries" | 1 | ✓ (rows 10, 9, 1) |
| "Dispatch evidence" | 1 | ✓ (row 1–3) |
| "Liveness probes" | 1 | ✓ (row 10) |
| **"Contradicted rows"** | 1 | **✗ NO SUCH ROW — F1** |
| "Append-only `rounds`" | 1 | ✓ (row 10) |
| "Ledger" | 1 | ✓ (row 10) |
| "Tracked runtime" | 1 | ✓ (row 10) |
| "Lane identity" | 1 | ✓ (row 9) |
| "Evidence standard" | 2 | ✓ (row 9,4) |
| "Canonical form" | 1 | ✓ (row 8) |

**13/14 names resolve; 1 broken.** The contradicting-rows incidents live under rows titled "Closure entries | 9" and "Closure entries | 1". Fix either side (add a `Contradicted rows` row, or re-point to "Closure entries").

### Section / structural references

- `(§Invariants, local-first)` (Evidence standard, L284) ✓; `(§Invariants)` (integrator, L162) ✓; bold `**Lifecycle**`/`**Promotion gates**` ✓.
- `MISSION.md §Push scope — hard rule` ✓ (heading exists, added by `235b414`); `MISSION.md §L2 concurrency` ✓ (heading `## L2 concurrency — required`).
- Step numbers: "closure step 3 applies it" (L14) ✓; "(step 4)" ×2 (L139, L175) ✓; "(dispatch evidence and orphan prompts: step 4)" (L121) ✓; "(see above)" ×2 ✓; "per the embed clause above" (L181) ✓; "the aggregator-lane paragraph below" (L191) ✓ — paragraph exists below; "per the gate below" (L15, L18) ✓.
- Row pointers into r10: D-12, D-13, D-30, D-33, D-41, D-48, D-49, M5, M6, M7, §Closure, §Conformance 1–9 (10 items exist), §Integrator, §Stale-lane, §Dispatch digest, §Evidence, §Template correction — all present in `.ufo/reports/round-10/protocol.md` (re-grepped).
- Appendix row figures re-executed where new: `launch kagi round=1` = 15:50:56 ✓ (watchdog.log:3); steer onward 15:52:38 ✓ (watchdog.log:17, `steer aggregator -> round 3`); `9a2e9fb`/`025b2e3`/`8ec7a56` exist with lane identities at 18:37:14/18:47:47/18:57:35 → "18:37–18:57" ✓; `43342dd` ✓; `640a4c5` 18:37:02 ✓; r10's "8/58 → 0/62" M5 ✓.
- "8 of 58 prompt files untracked at `0a30b44`": pin not present in r10's table (it pins only the after-column "0 at `8e32ae0`"), but arithmetically consistent with the tree: prompts tracked at HEAD = 63, added `0a30b44..HEAD` = 13 ⇒ 50 tracked at `0a30b44`, and 50 + 8 = 58 ✓. Pin plausible; recommend the row carry its counting command or rest on "r10 M5".

---

## 5. Findings table

| # | Where | Evidence | Verdict | Severity |
|---|---|---|---|---|
| F1 | O-47 → appendix, L241 vs table | `(§Appendix, "Contradicted rows")` — no row with that Rule exists (incidents sit under "Closure entries" rows) | **LOST** (pointer dead) | must fix |
| F2 | Appendix "Append-only `rounds`" row | "→ 12 at round 11" — re-executed `grep -rn 'rounds\[' *-shokunin \| wc -l` → **13** (19:50); also violates the appendix preamble ("figures verbatim from the round record, pinned to their measurement round, never live values" — round 11 has no record) | **DRIFTED** | must fix |
| F3 | Appendix "Lands last | 10", lane-identity sentence | "0 of 60 reports added under a lane identity at `8e32ae0` … first lane-identity report commits landed 18:37–18:57 (`9a2e9fb`, …)" — `git merge-base --is-ancestor 9a2e9fb 8e32ae0` → exit 0 and `git show --stat 9a2e9fb` adds `.ufo/reports/round-8/kumitate.md`, so 0-lane-identity at `8e32ae0` is false by the row's own second half; cited source r10:131 itself says "0 of **62**" with 33+26=59 unaccounted | **DRIFTED** (chimera of two stale figures under one pin) | must fix |
| F4 | Appendix "Protocol self-defect" row | candidate "~30 inline incident references" vs r10:237 verbatim "~29 inline incident references" | **DRIFTED** (one token) | must fix |
| F5a | Integrator section | "no lane was instantiated as integrator (rounds 2–9)" cause dropped; in appendix-draft but not in candidate body/table | **LOST** (narrative) | recommended |
| F5b | Integrator section | "rounds 2–8 produced no closure artifact at all and rounds 5–9 produced report prose instead of `rounds` entries" dropped | **LOST** (narrative) | recommended |
| F6a–f | Appendix rows (see §2 list) | six incident-detail drops, each quoted there | **WEAKENED** (minor, non-normative) | optional |
| F7 | §Invariants L374 | "(operator commit `235b414`)" — author is `shokunin <shokunin@local>`, not the operator identity | OK with nit | recommended wording |
| F8 | Step 4 L232–238 | "Every `in-flight` row is resolved by the next protocol round … `{<id>: <terminal status>}`" vs the new re-confirmation exception ("stays debt until the mission terminates") | **WEAKENED** (self-inconsistency the new clause introduces) | must-fix wording (one word) |
| F9 | O-28 L146 | "closes" → "can close" | OK (accurate; binding rules intact) | none |
| F10 | Fleet-2 L402 | "while `corpus/`, `LOG.md`, or `SHONEN.md` drift **are** a conformance defect" (orig. "is") | OK (grammar slip only) | cosmetic |
| F11 | O-21 L117 | parenthetical rephrase | OK (same meaning) | none |
| F12 | O-13 L76–77 | "(currently 8 subagents in one batched call)" dropped | OK (deliberate anti-staleness; MISSION owns the number) | none |
| F13 | SHONEN seed | extracted + diffed both files | OK (byte-identical) | none |

---

## 6. Overall verdict

**MUST FIX FIRST — then safe to land.** The compaction is semantically faithful: 91/91 obligations survive with their force intact, all 30 dupe-cluster merges preserved the unique content (with two acceptable judgment calls: the lane-absent ledger fallback made implicit, and the L2 current-value parenthetical delegated to MISSION), both known contradictions (a)/(b) are fixed as prescribed, and the seed block is byte-identical. What predicates cannot see and I found: **four small factual defects, all in the new appendix + one wording defect the new clause introduced:**

1. **F1** — add an appendix row `| Contradicted rows | 9, 1 | round-9 entry: kake `in-flight` vs report committed 17:44:34 (`4c81066`), kumitate `ok` with no derivable report, kengaku/kotoba/kagi `in-flight` before dispatch, counters that never reached 9; round-1 kagi `not-dispatched` vs `launch kagi round=1` (15:50:56) | r10 §Conformance 2–3 |` (or re-point L241 to "Closure entries").
2. **F2** — fix the Append-only-`rounds` row: delete "→ 12 at round 11" or re-pin it with command+output (re-executes to 13 now).
3. **F3** — rewrite the Lane-identity sentence so it does not assert "0 of 60 … at `8e32ae0`"; e.g.: "before 18:37, 0 report-adds carried a lane identity (r10 census: 33 operator, 26 `shokunin@local`, 3 unaccounted — r10:131's '0 of 62 at `8e32ae0`' predates `9a2e9fb`, 18:37:14); first lane-identity report commits landed 18:37–18:57 (`9a2e9fb`, `025b2e3`, `8ec7a56`)".
4. **F4** — "~30 inline incident references" → "~29" (verbatim from r10:237).
5. **F8** (wording) — "Every `in-flight` row is **answered** by the next protocol round — resolved (`<terminal status>`) or re-confirmed (`in-flight` + launch pointer)."

All five are one-line edits. F5a/F5b and the F6 series are the integrator's triage call; nothing normative depends on them.
