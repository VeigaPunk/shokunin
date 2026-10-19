# kaika W1: prior fleet research absorption check

Probe: `W1PriorResearch` (revenger seat). Read-only. Date: 2026-10-19.
Scope: `research/` (README, `deep-research-2026-09-28/`, `round-18-kimi-model-routing/`) and the
two lane `considerthese/` dirs (`kotoba-shokunin`, `chousa-shokunin`).

**Tooling note.** This probe was not assigned web research, so none was done. Every verdict rests
on local files, git history, and read-only host metadata (`stat`, `ss`). Two kinds of file were
deliberately not opened because they hold credentials: `~/.kimi-code/config.toml` and the shim
unit files. For those, only metadata was read. The evidence is prose plus git history, so no LSP
server applies. Text grep is the instrument, and it is labelled as such where it carries a negative
claim.

**HEADs read:** fleet root `master` `31baf5c`; kotoba `master` `78ee57e`; chousa `master` `ab19cff`;
kengaku `master` `99cf615`; kimi-shokunin `bc7d690`.

## 0. Verdict legend

| verdict | meaning |
|---|---|
| ABSORBED | landed in a lane or fleet file or commit (pointer given) |
| CONVERGENT | the fleet already held it before the research landed (dated pointer). No absorption trail is needed. |
| REJECTED | dispositioned with a reason on record (pointer) |
| PARTIAL | measured or recorded, but the remedy or follow-through did not land |
| ORPHANED | no lane or fleet record acts on it. **★ = worth reviving** (§7). |
| MOOT / LAPSED | the premise no longer holds (evidence given) |
| REFUTED | contradicted by evidence |

## 1. Headline (confidence: high unless marked)

1. **The deep-research harvest (2026-09-28) had exactly one absorption path.**
   - It became the demand instance that minted chousa: `chousa-shokunin/MINT.md:8-13`; the
     MANIFEST `rounds[]` round-0 note; `.ufo/scopes/shokunin-12h-20261014/operator-demand.md:21`.
   - Chousa's round-1 audit wave (32 member reports) turned it into method specimens plus 10 kept
     rejections: `chousa-shokunin/corpus/knowledge/archived-export-intake.md:101-110`.
   - The fleet root never logged the harvest. `LOG/SCORECARD/ROADMAP/CORPUS/LEARNING/MISSION` contain
     0 references to it.
   - The README's own "corrections for our scheme" were never applied by the fleet and never
     corrected in the index.
2. **Round-18 routing research was well absorbed for missions M1–M6, then went stale.**
   - Kengaku absorbed M1–M6 as a digest, then built a 9-probe calibration battery that re-verified
     6 of the 13 carried items (R-01, R-02, R-03, R-07, R-10, R-13), plus a seat-level check on a
     seventh (R-08).
   - That digest landed at 11:09 on 2026-10-15, 23 minutes before M7–M10 began landing. It also
     predates the 2026-10-16 operator overrides. Kengaku's corpus therefore still states 3
     superseded facts.
   - One security finding never reached any lane: live keys sit in world-readable shim unit files.
     Fast mode was enabled on 2026-10-16 without the conditional-go evidence the research required.
3. **Both `considerthese` reflections were written against the GitHub remote while the standing
   no-push rule kept local work unpushed.**
   - At reflection time, kotoba had 36 commits (16 round landings) and chousa had 6 that were not
     on the remote.
   - Most of the "open" items had already been fixed or pre-registered locally hours earlier.
   - The one live defect kotoba caught is still at HEAD: a YAML scalar leaked into the README
     `**Domain:**` line. It also affects chousa and kotodama, and neither reflection caught those.
   - No contract mentions `considerthese`: not the fleet root, not the upstream, not any lane.

## 2. How the prior research flowed (reconstructed contract + evidence chain)

| Prior artifact | Landed | Fleet trail | Lane absorption |
|---|---|---|---|
| `research/README.md` + exports A/B/C | `0863746` 2026-09-28 22:51:25, the only commit touching these paths | 0 refs in fleet `LOG/SCORECARD/ROADMAP/CORPUS/LEARNING/MISSION` | chousa mint demand (2026-10-14); r1 wave `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/` (32 reports); MINT guards `MINT.md:32-147` (integration, provenance, scope, secrecy, chaining); intake record `corpus/knowledge/archived-export-intake.md` (CL-01..CL-09, RJ-01..RJ-10); fixtures `corpus/fixtures/archives-r9/`; 114 chousa files reference the exports |
| `research/round-18-kimi-model-routing/` (681 files, 10 subtrees) | 23 commits 2026-10-15 08:39→11:59, plus `542204b` 2026-10-17 00:29 (APPLY note + toml OPERATOR OVERRIDES) | fleet report `.ufo/reports/round-18/kengaku.md`. MANIFEST has no `rounds[]` row for this work: its round-18 rows are kasegi, kake, chousa, kotodama. | kengaku digest `f9d54f1` (2026-10-15 11:09, M1–M6 only); kengaku r19/r20 probe battery `plans/probe-battery-r19.md` → `corpus/knowledge/probe-battery-r19.md` (P1–P9) |
| `kotoba-shokunin/considerthese/2026-10-19.md` | remote `4f7c789` 08:01 (git author João Pedro Veiga; text signs "kotoba-shokunin (Grok Bot)"), merged locally `78ee57e` 17:09 | none | none: 0 references outside the file itself |
| `chousa-shokunin/considerthese/2026-10-19.md` | remote `efd9ba0` 09:06, merged locally `ab19cff` 17:05 | none | none |

**Reflection blind spot (the mechanism behind §5/§6).**

| Lane | Remote state the reflection read | Local-only commits at reflection time | Round landings among them |
|---|---|---|---|
| kotoba | merge-base `c8b53ac` (remote tip `74fc0f1`) | **36** | **16** (rounds 21–36) |
| chousa | merge-base `38f217e` (remote tip `d556a0e`) | **6** (round-12 pre-registration + dispatch deviations) | 0 landed; the fixes it asked for were pre-registered at `ba8ce4e` 07:32 |

The reflections confirm the remote-only view in their own text. Kotoba says it reviewed "via the
GitHub API at `master` HEAD `74fc0f1`" (`kotoba considerthese:3-4`) and concluded "No craft round
moved." (`:11`). Chousa says "4 commits … nothing since." (`chousa considerthese:3`).

The `origin/master` reflog then shows "fetch origin: fast-forward" followed by "update by push" at
17:08:38/17:09:39 (kotoba) and 17:05:17/17:05:48 (chousa). Those times are earlier than this
campaign's session start, 20:36Z. [INFERENCE: an operator-side sync, not a kaika action.]

**Contract invariants these flows touch** (last-known-good → divergence):
- "**An index row is a claim.**" (`CORPUS.md:45`). `research/README.md:10-17` asserts more than its
  sources carry, and no erratum exists (D-19).
- "**Corrections are new entries, never rewrites.**" (`CORPUS.md:52`). The kengaku digest has no
  superseding entry for M7–M10 or the 2026-10-16 overrides (R-19).
- "Operator teaching outranks every other source." (`LEARNING.md:47`), with a landing slot of
  `corpus/lessons/operator-<date>-<slug>.md`. There are 0 such files fleet-wide. `considerthese`
  fits neither slot: it is operator-identity commits of bot proposals that call themselves
  "proposals only — not acted on" (`kotoba considerthese:56`).

## 3. Disposition ledger: deep research (README + A/B/C exports)

Export lines are cited as `A:`, `B:`, `C:` for `research/deep-research-2026-09-28/{A-shokunin-tradition,B-multiagent-knowledge,C-rank-taxonomy}.md`.
`members/` = `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/`; intake =
`chousa-shokunin/corpus/knowledge/archived-export-intake.md`.

| id | Finding / suggestion (source) | Verdict | Evidence pointer | Note |
|---|---|---|---|---|
| D-01 | 職人気質 is read *katagi*, not *kishitsu* (README:11-12; A:47,71) | MOOT + REJECTED as lane content | 0 fleet files outside `research/` and `.ufo/waves` use "kishitsu". Chousa routed the lexical row "unowned" (`members/CraftVsContent.md:100`; `MINT.md:52-53` "Lexical and workshop rows stay unowned"). The dictionary hop was never walked (`members/ClaimVsSourceCheck.md:48` "unverifiable-locally"). | nothing to correct; not worth reviving |
| D-02 | "`jin'i-ryu` is NOT an attested artisan rank — it's our coined term and should be labeled so." (README:12-13) | **ORPHANED ★** at fleet level; REJECTED at chousa scope | Fleet docs carry the token 5 times (`PROTOCOL.md` 3, `README.md` 2) and kimi upstream 8 times. There are 0 "coined"/"coinage" labels in either. Chousa refused to copy the gloss (RJ-02, intake:102) and refused "Do not amend `PROTOCOL.md:21`" (`MINT.md:92`). That is a lane-scope refusal, not a fleet decision. | The negative is unproven: A only says "I could not substantiate this spelling as an established artisan rank…" (A:64), and sweeps A-09/C-08 are still `pending`. The label needs no lexicographic claim, because the token is the fleet's own (`58bc367`, 2026-09-28 15:29). |
| D-03 | Four usable axes: competence / independence / improvement / transmission (README:13-14; A:54) | REJECTED (lane) | RJ-01, RJ-02 (intake:101-102); `MINT.md:77-92` "Do not add a second axis taxonomy". Fleet keeps six axes (`AXES.md:7-16`). | no fleet-level record of the decision |
| D-04 | "Track five axes separately: task competence, retention, evidence fidelity, cross-domain transfer, and operating cost." (B:57) | REJECTED as taxonomy (RJ-01); underlying measures **ORPHANED** | grep sweep: 0 hits for retention or operating-cost measures in fleet protocol docs and in every lane `SCORECARD.md`/`SKILL.md` (cmd §11) | relevant to kaika: heavy parallelization means cost; SKILL rewrites mean retention. If revived, do it as a check inside existing axes, not as a new axis. |
| D-05 | "make knowledge changes—not agent self-assessments—the unit of evaluation" (B:57) | CONVERGENT | self-attestation ban `eac90ae` 2026-09-28 15:37; non-author gate `097c75e` 16:43; both before the 22:51 landing. Claims are measured before→after (`AXES.md:27-30`). | none |
| D-06 | ACE "brevity bias" / "context collapse"; remedy: localized delta updates (B:79, hedged "This is a case study, not a universal failure rate.") | numerals REJECTED; remedy **ORPHANED ★** | Numerals routed to kengaku as unverified (RJ-03, intake:103). Chousa's Q-DELTA (`members/QualityBar.md:75`) was not admitted: chousa `corpus/QUALITY.md` is 7 lines with 0 delta/rewrite hits, and `members/HonestyAudit.md:70` objects to the split warrant. Kengaku: 0 hits. | Both reflections propose SKILL.md compaction (kotoba trim; chousa distillation), which is the operation ACE warns about (§7 #7, #10) |
| D-07 | Paper lineage: Voyager, Generative Agents, Reflexion, Dynamic Cheatsheet, ACE, Memento-Skills, LEGOMem (B:63-71) | REJECTED as a verified map (RJ-04, intake:104); **ORPHANED ★** as a reading list | ApprovalTable B-01..B-10 all `pending` (`members/ApprovalTable.md:110-119`). Routed to kengaku (`members/CraftVsContent.md:121`), which has 0 hits. The export has zero `http`, zero doi, zero arXiv id (`members/ClaimVsSourceCheck.md:98`). | leads in §10 |
| D-08 | Weight-space MoE ≠ memory-owning agents; neural results "do not directly validate rules for splitting Markdown corpora" (B:75) | REJECTED as content; kept as method form | MC-G07 transfer ban (`members/MetaCraft.md:80`); content → kengaku (`CraftVsContent.md:122`) | low value |
| D-09 | Prompt Q2: when to split a domain vs expand (B:35) | never answered (CL-05, intake:87); CONVERGENT | protocol mint bar "two documented *unplaceable* demand instances" was in place by `640a4c5` (2026-09-28 18:37), before the harvest | none |
| D-10 | Prompt Q3: credit assignment; "team success does not establish which specialist actually improved" (B:47, progress chrome) | never answered; CONVERGENT in part | per-lane rounds, per-axis verdicts, non-author verification (`PROTOCOL.md:61-68`) | not examined further |
| D-11 | Rank renames Initiate→Grounded→Maintainer→Agentwright / Minarai→Shokunin→licensed→Oyakata (C:69) | REJECTED (lane); not adopted (fleet) | RJ-05 (intake:105); `MINT.md:86-89` lists the English rename among 47 non-general rows | not worth reviving: renaming erodes the essence, and D-02 covers honesty |
| D-12 | Keep certification and permissions separate from rank names; rank conferred by procedure, not self-description (C:53,65-67,92-100) | CONVERGENT | sibling mint as a permission separate from rank: `2d19a64` 2026-09-28 22:44, 7 min before the harvest commit; non-author gate `PROTOCOL.md:61-68` | none |
| D-13 | "Safe self-iteration usually means changing implementation within externally maintained constraints" (C:126) | REJECTED (lane: unlabeled opinion) / CONVERGENT (fleet) | RJ-05; `members/MetaCraft.md:48` CF-2. Fleet jin'i-ryu gate = a landed falsifiable improvement to the lane's own SKILL/PROVINCE (`PROTOCOL.md:76-78`). | none |
| D-14 | Use kyū/dan only with published examinations (C:89-105) | MOOT | fleet trends are verdicts, never scalars (`LEARNING.md:25-26`) | none |
| D-15 | Kendō shōgō, Go promotion vs authorization, shu-ha-ri, menkyo kaiden (C:97-100,128-133) | not adopted; unowned | ApprovalTable C-02..C-06 `pending` | not worth reviving |
| D-16 | nenki-ake ≠ ichininmae ≠ independent practice (A:76-78) | method form kept (MC-G03, `members/MetaCraft.md:76`); content unowned (`CraftVsContent.md:105`); CONVERGENT | probation of ≥3 verified rounds before a roster row (`PROTOCOL.md:47-50`) | none |
| D-17 | Graduated responsibility through entrusted work (A:88) | REJECTED | RJ-09 (intake:109); already covered by `PROTOCOL.md:61-67` | none |
| D-18 | Apprenticeship durations of 7/5/9/5 years (A:80-86) | unverified; unowned | `CraftVsContent.md:106`; ApprovalTable A-04..A-06 `pending` | not worth reviving |
| D-19 | README provenance claims: burner Chrome, CDP 9222, "fired by L0", no Deep Research entitlement, "9/8/10 web searches" (README:6-8) | REJECTED as fact; the index itself **ORPHANED ★** | RJ-06 (intake:106) and `MINT.md:55-64` (visible search labels are 1/1/2); `members/StopRule.md:142` R6 "INDEX_OVERRUN"; M-01/M-02 refused (`MINT.md:105-108`). `research/README.md` was never amended: `0863746` is its only commit. | owner: fleet integrator (append-only erratum) |
| D-20 | Unanswered asks: A Q3 teach-vs-hoard, A Q4 public evidence of mastery, C's rank-inflation catalog | never answered (CL-05; `MINT.md:49-51` "Do not invent them") | Rank inflation is not the observed failure: 13 of 13 MANIFEST roster rows are `shonen` (cmd §11). | [INFERENCE] Teach-vs-hoard maps onto kaika D1 `SOURCES.md ## Paths`; public evidence of mastery maps onto the README front door (K-L2). |
| D-21 | ApprovalTable M-05: extend fleet citation gates with an EXTERNAL base class | PARTIAL | Chousa's gate recognizes URL pointers. It fails them closed with `EXTERNAL_WITHOUT_APPROVAL` unless the record's Meta declares an external window and an Approval row is `approved`/`granted` (`chousa-shokunin/tools/research-gate.sh:568`, `:645-647`, `:822-838`). kagi/kasegi gates were not re-checked here. | ★ prior art for D4 `sources-census.sh` |
| D-22 | The ApprovalTable as a work queue (A-01..M-05) | **ORPHANED** | 34 rows, 34 `pending` (cmd §11). Chousa rounds since have stated "Zero network" (chousa `LOG.md` round-23 boundaries line). | Chousa owns the instrument: "The approval table is itself a chousa deliverable." (`chousa-shokunin/SKILL.md:45-46`). Leads in §10. |

Confidence: high for the git/grep facts. D-10 is not deep-checked.

## 4. Disposition ledger: round-18 kimi model routing

`R18/` = `research/round-18-kimi-model-routing/`; report = `R18/routing/kengaku-round18-report.md`
(§6 lists 13 carried-open items); digest = `kengaku-shokunin/corpus/knowledge/kimi-model-routing-round18.md`;
battery = `kengaku-shokunin/corpus/knowledge/probe-battery-r19.md`; toml = `R18/routing/kimi-secondary-models-round18.toml`.

| id | Finding / suggestion | Verdict | Evidence pointer | Owner if open |
|---|---|---|---|---|
| R-01 | Token-plan keys 2/3 are quota-dead until 10-23 / 10-28 16:00Z; quarantine; re-entry only on a passing chat probe (report §6.1) | ABSORBED | digest; battery:147-150 (P1 1a–1f HIT) and :163-164 (resets re-derived to ±1 s) | kengaku: recheck due 2026-10-23T16:00Z / 2026-10-28T16:00Z (not yet due) |
| R-02 | Shim burst-flush; incremental flushing fix (report §6.2) | PARTIAL / MOOT | measured: battery:153 (P5b, span 0 ms). Fix not implemented. Both cascade lanes have been disabled since 2026-10-16 (toml:60-61). | operator. Related: kengaku r23 stream-surface WIP has been unadmitted since `a2ff634` (2026-10-16), "resume or discard next session". |
| R-03 | opencode-go WAF: a scripted UA gets 403 `1010` (report §6.3) | ABSORBED / VERIFIED | battery:156 (P7a: 200, no 403/1010) | none |
| R-04 | `kimi doctor` validates no model-level keys (report §6.4) | ABSORBED | digest (records that doctor's silence is not correctness evidence) | minor: kumitate `corpus/knowledge/kimi-modes-machinery.md:67` cites a doctor "valid" result without this caveat |
| R-05 | OMP-native route admission, the round-17 blocker (report §6.5) | ORPHANED (status unknown) | grep sweep in kumitate for `route admission|native route|admission path|round-17 blocker`: 0 | kumitate/operator: confirm or close |
| R-06 | Live API keys in commented `Environment=` lines of `glm-flash-shim.service` / `ds-flash-shim.service`, mode 0644 (`R18/census/ANALYSIS.md:43`) | **ORPHANED ★** | M7: "**Those commented lines were not touched**" (`R18/cascade-legorder/LEGORDER.md:55`). M9: "Commented key material (M1 vuln finding): preserved byte-for-byte." (`R18/glm-flash-legorder/LEGORDER.md:117`), and it lists the item as open (`:456-458`). `stat` today: both files 644, mtime 2026-10-15 11:26:20 / 11:27:18 (the M7/M9 edits). kagi: 0 hits. | kagi (documentation-only entry) + operator remediation. [INFERENCE: the key lines are still present. Nothing has modified the files since M7/M9 preserved them; content was not opened.] |
| R-07 | `managed:kimi-code` 401 with an empty OAuth store (report §6.7) | ABSORBED / re-verified | battery:476-477 (P8a/8b HIT, r20) | operator re-auth only |
| R-08 | Devin cold start is unbounded; warm on start (report §6.8) | PARTIAL | kengaku `corpus/evidence/probe-r19-devin-shim-seat.log:30-32` (shim warm, D7 precondition absent) and `:120` ("The r18 D7 cold-start timeout did NOT reproduce"); M10 limits: "Cold-start behaviour on a genuinely idle lane is untested" (`R18/devin-opus/ANALYSIS.md:234-235`) | low |
| R-09 | STRONG single-provider dependency; measure `grok-4.7` before promotion (report §6.9) | **ORPHANED ★** | toml:53 adds `openai-codex/gpt-6-luna-max` (also codex). The M10 cross-provider splice `devin/opus-5.5-high` has no lane dispatch receipt (grep sweep: `devin/opus|claude-opus-5-5` matches only OMP-alias rows such as `kama-shokunin/corpus/knowledge/alias-endpoint-normalization.md:27-28`). No `grok-4.7` battery row in kengaku. | kengaku + operator. [INFERENCE from toml OVERRIDES mirroring live on 2026-10-16; live config not opened.] |
| R-10 | M5 codex fast mode: no-go; conditional-go protocol (n≥10 interleaved A/B, applied-tier confirmation, shim `SHIM_SERVICE_TIER`) | **ORPHANED ★ + DIVERGED** | Operator enabled fast servicing on 2026-10-16 via `SHIM_SERVICE_TIER=priority` for all three codex pool entries: "applied-tier echo unconfirmed -- M5's conditional-go re-test still stands." (toml:54-59). Kengaku r20: echo `default` on all serviced, credits static (battery:472-473). No lane has run the protocol (grep sweep `conditional.go|SHIM_SERVICE_TIER`: kengaku has only the digest line). | kengaku |
| R-11 | M2 verify-later: 46 `video_in`/`audio_in` claims, `max_context_size`, DEF-5 cap divergence, `reasoning_key` rendering (report §6.11) | ORPHANED | no lane re-verifies these. kumitate counts capabilities but does not verify them (`kimi-config-plane.md:153-154`). | kengaku |
| R-12 | Stray listener on `127.0.0.1:8799` (report §6.12) | LAPSED | `ss -ltnH 'sport = :8799'` → 0 listeners today; mori never recorded it | nothing to revive |
| R-13 | glm cascade leg order vs the zai-primary policy (report §6.13) | ABSORBED / CLOSED | M9 `c9df79b` reordered to zai→devin; battery:151-152 (P4c/4d HIT) | stale record: toml:129,136,200 and `R18/routing/APPLY.md` item 6 still say "operator check"/"unverified". M9's patch text (§6a–6c) was never applied, including by `542204b`. Low priority: cascades are disabled. |
| R-14 | M7 ds cascade reorder (alibaba→hyper→opencode-go) and its quota warning (single key, no rotation; `LEGORDER.md:189-205`) | ABSORBED (as prediction input) / PARTIAL | `kengaku-shokunin/corpus/evidence/probe-r19-shim-ds-predictions.log:6`; follow-up patch text 7a–7d not applied (moot after the cascade was disabled) | [INFERENCE] the warning later materialized: fleet commit `34c1ad1` "token-plan key-1 quota exhausted (rotate to key 2)" |
| R-15 | M8: `ultra` rejected on the wire; splice `openai-codex/gpt-6.1-sol-max` | ABSORBED (by operator, host catalog) | used as a dispatch route: `souji-shokunin/LOG.md:300` "24 seats on openai-codex/gpt-6.1-sol-max"; also in kama's available-models telemetry | the R18 record (toml OVERRIDES) does not mention it. Low. |
| R-16 | M10: `/v1/models` on the shim is a static list, not authoritative; `devin/opus-5.5-high` STRONG splice | PARTIAL | used as a hypothesis source in kengaku's r19 devin seat (`probe-r19-devin-shim-seat.log:22-27`); splice not applied (see R-09) | low: OMP already routes Anthropic Opus via `m_opus` |
| R-17 | M2 `config-corrections.toml`: 56 blocks, 4 pool-relevant minimal edits, Section C global-effort removal | ORPHANED (application unknown) | no lane tracks the queue; live config not opened | kengaku/kumitate, as an evidence-only re-audit |
| R-18 | `APPLY.md` runbook / 13-entry table | SUPERSEDED | `APPLY.md:6-12` "Partly superseded (2026-10-16)"; operator hand edits recorded in toml:41-66 (9-entry pool, `default_model` opencode-go, cascades disabled) | none |
| R-19 | Kengaku digest freshness | **STALE ★** | digest landed `f9d54f1` 11:09, before M7 `54909b2` 11:32, M9 `c9df79b` 11:32, M8 `5eb7f74` 11:35, M10 `afb5573` 11:40, and `542204b` (10-17). The digest has 0 mentions of M7–M10/OVERRIDES. Stale statements: `:153` (default = cascade), `:175` "`SHIM_SERVICE_TIER` injection (filed idea, not implemented)", `:218` "the live config still holds the 17-entry pool". The digest and battery entries also lack the `source:`/`verified-at:`/`recheck:` opening lines required by `CORPUS.md:17` (0 of 3 in each). | kengaku |
| R-20 | Census D4–D6: `/models` is an incomplete oracle; narrow codex request shape | ABSORBED | kengaku P2 request bodies use the D6 shape (`probe-r19-P2-servicetier.log:26`); the devin seat applies D4 | none |

Confidence: high for the pointers. Medium for R-06, R-09, and R-14, which carry inferences.

## 5. Disposition ledger: `kotoba-shokunin/considerthese/2026-10-19.md`

| id | Item (location) | Verdict | Evidence |
|---|---|---|---|
| K-L1 | `.gitignore` replaced by `c8b53ac`; bytecode tracked (`:19-29`) | ABSORBED **before the reflection** | `4e92f36` (2026-10-18 11:22) untracked 2 `.pyc`; round 21 `2ca8d01` (2026-10-19 01:21) restored `__pycache__/` and `*.pyc`. Current `.gitignore` has 3 rules; tracked bytecode = 0. |
| K-L2 | README `**Domain:** >` (YAML folded-scalar marker); LOG entry misfiled (`:31-39`) | **ORPHANED ★, live at HEAD** | The README reached local only via merge `78ee57e` (17:09 today). The same defect class appears in chousa and kotodama: `**Domain:** "…` with no closing quote. That is 3 READMEs (cmd §11). The LOG bullet now sits at `LOG.md:2292`, under the heading "## 2026-10-19 — Round 46 B2 superseding report pin" (`:2286`). There are 16 unmerged cloud-agent README branches (kotoba 8, chousa 8, `origin/cursor/*`, 2026-10-17); none carries the leak. |
| K-L3 | Capabilities 0 rows, no saturation line, SKILL.md 601/600 (`:41-54`) | ABSORBED before the reflection | Saturation declared in round 21 (kotoba `SCORECARD.md` §Saturation, line 10.0, N=3). Capabilities: 2 rows (`dc4c0c0` r23 substrate-pin guard; `b0b0410` r29 assertion-floor guard). SKILL.md is 521 lines (`4b50d8d` r22 "line_budget cleared by content"). |
| K-P1 | Run the instruments rather than quote them (`:60-67`) | ABSORBED in-lane / structural for the channel | the r29 assertion-floor guard reruns all six self-tests (kotoba `SCORECARD.md` §Capabilities). The reflection bot still cannot execute anything. |
| K-P2 | Trigger-routing evals: `corpus/evals/trigger-intents.jsonl` + `verify_trigger_routing.py` (`:69-75`) | **ORPHANED ★** | `corpus/evals/` absent; kotoba `corpus/README.md:73` "Implicit-intent fidelity is still unmeasured" |
| K-P3 | Repo-hygiene gate for tracked `__pycache__`/`*.pyc`/interactive logs and `.gitignore` rule loss (`:77-82`) | **ORPHANED ★** (fixed by hand; no gate) | grep sweep over kotoba verifiers for `pycache|gitignore`: 0 hits. The class is live elsewhere: 5 tracked bytecode files in 4 lanes, and kaidoku tracks 4 interactive-session files (§7 #8). |
| K-P4 | Lint README as a governance surface (`:84-88`) | **ORPHANED ★** | see K-L2. The reflection notes that `governance.citation_resolves` covers LOG and SCORECARD only (`:84-85`). |
| K-P5 | Ready-made 601→600 trim (`:90-93`) | MOOT | SKILL.md is 521 lines (r22) |
| K-S | Side effect: `considerthese/` might be counted as unindexed (`:95-98`) | **REFUTED** | the verifiers enumerate `git ls-files corpus/` only: `verifiers/verify_corpus_integrity.py:547-552`, `verifiers/verify_corpus_independent.py:82-86` |

## 6. Disposition ledger: `chousa-shokunin/considerthese/2026-10-19.md`

| id | Item (location) | Verdict | Evidence |
|---|---|---|---|
| C-L1 | SKILL.md caught up with the gate (`38f217e`) (`:7`) | observation (accurate) | none |
| C-L2 | Conformance scaffolds; saturation line and window N undeclared; 0 capability rows (`:8`) | ABSORBED (pre-registered before the reflection) | the `ba8ce4e` pre-registration (07:32) planned the §Saturation declaration. `5691bf5` (09:12) landed "Saturation line: **8.0**", N=3, and the first capability rows (chousa `SCORECARD.md:469-495`, `:596+`). |
| C-L3 | README + Devin wiki link (`:9`) | observation; **missed defect** | chousa README `**Domain:** "Deep-research method …` has an unterminated quote (K-L2 class) |
| C-F | `A-r9.md:50` row C3 cites `A:76`, but the span is at `A:86` (`:11`) | ABSORBED (pre-registered before the reflection) | the `ba8ce4e` pre-registration: "calibration = close the A-r9 C3 finding". Fixed in `5691bf5`; LOG `:561`. `corpus/fixtures/archives-r9/A-r9.md` now cites `:86`. |
| C-P1 | Run `--selftest`/`--drift` independently (`:15`) | ABSORBED in-lane | every round's before-receipts, e.g. chousa `LOG.md` round-24 opening: "selftest `PASS (133 cases, 0 skipped)`; drift `none` vs the r12 baseline". An independent non-author run belongs to W3. |
| C-P2 | Track the hardening-r10 ledger (68 rows), the 27-item r11 queue, and A-r9 (`:16`) | ABSORBED in-lane | ledger addenda in r13–r15 (chousa `LOG.md:584`, `:606`, `:625`): 71 rows → by-design 38 · carried 21 · closed 10 · finding 0 · operator 3; queue 26→24. The reflection's "68" is a stale remote count. |
| C-P3 | Calibration nudges: saturation and capabilities (`:17`) | ABSORBED | see C-L2 |
| C-P4 | Watch SKILL.md size (~420 lines, mostly prose logs); distil back into decision tables (`:18`) | **ORPHANED ★** | SKILL.md is now 434 lines / 40,280 B, with 22 table rows and 6 headings. Lines 61–434 (374 lines) sit under the single `## Gates` heading. |

## 7. Orphans worth reviving: ranked, with owning lane

Each item gives a falsifiable before→after hook that wave 2 can adopt.

1. **`considerthese` intake contract.** Owner: the fleet protocol lane, via D3 (`LEARNING.md` +
   `templates/round-prompt.md`).
   - Each round's mistake-mining step reads `considerthese/` entries newer than the last round. It
     dispositions every proposal as absorbed / rejected-with-reason / deferred under the lesson's
     `## Mistakes`.
   - A reflection must name the HEAD it read and the local-vs-remote lag.
   - Hook: fleet-contract mentions of `considerthese`, 0 → ≥1
     (`git grep -c -i considerthese -- LEARNING.md templates/round-prompt.md PROTOCOL.md`).
   - Evidence: §2 blind spot. 4 of 9 kotoba items and 5 of 8 chousa items were already
     absorbed or pre-registered locally when written.
2. **README front-door YAML-scalar leak.** Owner: kotoba for the class (its domain is frontmatter
   fidelity; README lint as a governance surface). Each lane fixes its own README.
   - Hook: `grep -lE '^\*\*Domain:\*\* (>|")' *-shokunin/README.md | wc -l` 3 → 0.
   - Kotoba also appends a correction entry for the misfiled `LOG.md:2292` bullet (append-only).
   - Candidates: the 16 unmerged `origin/cursor/*` README branches.
3. **Shim unit credential exposure.** Owner: kagi, which owns "secrets & vault ops … credential
   hygiene evidence" (`kagi-shokunin/PROVINCE.md:3`). The entry is metadata-only and never opens the
   content.
   - Operator remediation: remove the commented key lines, `chmod 600`, and rotate both keys,
     because they have been world-readable since at least 2026-10-15.
   - Hook: `stat -c %a ~/.config/systemd/user/{glm,ds}-flash-shim.service` 644 → 600.
4. **Fast mode enabled without its evidence.** Owner: kengaku.
   - Run the M5 §7 conditional-go protocol through the shim (n≥10 interleaved
     `default`/`priority`, applied-tier confirmation), or file a revert recommendation.
   - Hook: lane files carrying an n≥10 A/B receipt, 0 → 1.
5. **Kengaku routing digest supersession.** Owner: kengaku (freshness).
   - Append a superseding entry covering M7–M10 and the 2026-10-16 overrides, and add the missing
     header fields.
   - Hook: digest entries with `source:`/`verified-at:`/`recheck:`, 0/2 → 2/2. Stale statements
     (`:153`, `:175`, `:218`) gain a superseding pointer, 0 → 3.
6. **Honest vocabulary.** Owner: the fleet protocol lane (D3) plus D5 canonical sync.
   - Label `jin'i-ryu` as the fleet's own coinage. Record at fleet level the fate of the README
     "corrections" (D-02, D-03, D-11).
   - Append an erratum to `research/README.md` pointing at chousa's RJ-02/RJ-06.
   - Hook: `git grep -c -i -E 'coined|coinage' PROTOCOL.md` 0 → ≥1; upstream likewise.
   - Do **not** assert the lexicographic negative (unproven, D-02).
7. **Agent-memory current art as sources.** Owner: kengaku `SOURCES.md` for the literature, with
   kotoba for a SKILL-compaction retention guard. The guard requires every line removed from SKILL.md
   to map to a corpus entry or a recorded rejection: the ACE "delta, not wholesale rewrite" lesson.
   - Needs a web window. Leads are in §10.
   - ApprovalTable rows B-01..B-10 become SOURCES rows only once opened.
8. **Fleet-wide tracked-artifact gate.** Owner: souji, whose province includes "Lane-repo hygiene
   surfaces, per-lane and only with a receipt" (`souji-shokunin/PROVINCE.md`).
   - Tracked bytecode today:
     - `audio-shokunin`: 2 files (`corpus/live/r94-reviewer/logs/pyc-prestate.pyc` and
       `corpus/live/r95-simplifier/measure_audio-folded.pyc`). These may be deliberate evidence; check.
     - `game-dev-2d-shokunin`: 1 file (`reports/round-104/mutations/__pycache__/…`).
     - `game-dev-3d-shokunin`: 1 file (`reports/round-104/physics/…/__pycache__/…`).
     - `souji-shokunin`: 1 file (`census/round-10/__pycache__/…`).
   - Kaidoku also tracks 4 `.ufo/interactive-sessions/` files.
   - Hook: tracked bytecode + interactive logs, 9 → 0 (or a receipt-backed keep list).
9. **Trigger-routing evals.** Owner: kotoba (coverage).
   - Hook: `corpus/evals/` absent → present, with a verifier that exits 0 and an "unmeasured" line
     that is superseded.
10. **Chousa SKILL.md distillation.** Owner: chousa, with the retention guard from #7.
    - Hook: lines under `## Gates`, 374 → fewer, with 0 gate facts lost. A table-row/fact census is
      taken before and after.
11. **R18 verify-later and the STRONG cross-provider gap.** Owner: kengaku, plus the operator.
    - Covers R-09, R-11, and R-17: an evidence-only re-audit of the 46 `video_in`/`audio_in` claims,
      DEF-5, and STRONG-pool provider diversity, without opening credential files.

**Not worth reviving (with reason):**
- katagi gloss: moot.
- Apprenticeship durations: unowned content.
- Rank renames: they would erode the essence.
- kyū/dan: moot.
- `:8799` listener: lapsed.
- opencode WAF: verified clean.
- `managed:kimi-code` 401: re-auth only.
- M8 sol-max: already applied by the operator.
- glm leg order: closed; only stale wording remains, and cascades are disabled.
- Burst-flush fix and devin warm-up: moot while cascades are disabled.

## 8. Mistakes mined (process level; each proposes a criterion)

| id | Mistake | Evidence | Proposed criterion / rule (owner) |
|---|---|---|---|
| X-1 | Reflections read a stale remote under a no-push rule | §2: 36/6 local-only commits; "No craft round moved." | A reflection states the HEAD it read and the lag versus local, or reads local (D3) |
| X-2 | An index overran its sources and was left standing for 3 weeks | `research/README.md:10-17`; StopRule R6; RJ-02, RJ-06 | `research/` harvests get an owner and an index-row-is-a-claim check (integrator; D3) |
| X-3 | A digest was frozen mid-round and never superseded | R-19 | A digest of a still-running parent round records "as of <commit>" plus a supersede trigger (kengaku `QUALITY.md`) |
| X-4 | A host change outran its evidence | R-10. Operator teaching outranks other sources (`LEARNING.md:47`); the miss is that no lane re-tested afterwards. | When the host changes a measured setting, the owning lane re-runs the named protocol within N rounds (kengaku) |
| X-5 | Template-generated public docs were not parsed | K-L2: 3 READMEs | README header fields come from the parsed frontmatter scalar, and a gate reads README (kotoba) |
| X-6 | A fix by hand with no gate; the class recurs in other lanes | K-L1/K-P3, §7 #8 | Hygiene fixes ship with a check (souji fleet-wide; each lane locally) |
| X-7 | A security finding had no owning lane | R-06: filed as "vuln" by M1, preserved by M7/M9, still 0644 four days later | Every `vuln`-class finding names an owning lane at filing time (protocol; kagi) |
| X-8 | A contract gap: the reflection channel has no slot | 0 `considerthese` mentions; 0 `operator-*` lessons | see §7 #1 |

## 9. Constraints for wave 2

- Do not copy `research/README.md:10-14` or the export glosses into any corpus as fact. Cite
  chousa's intake record instead (`MINT.md:37-44`; RJ-02).
- Chousa's gate fails URL pointers closed with `EXTERNAL_WITHOUT_APPROVAL` unless the record
  declares an external window and an approved Approval row (`research-gate.sh:645-647`,
  `:822-838`). If a chousa `SOURCES.md` or record carrying URLs is run through the gate, record the
  kaika operator directive as the approval. Otherwise the row is gate-red by design.
- Round-18 follow-ups must never open `~/.kimi-code/config.toml` or the shim unit files. Use metadata
  or count-only checks: "Cite the file path, the mode, and the mechanism" (`CORPUS.md:50-51`).
- Treat `considerthese` proposals as candidates to disposition, not as operator teachings. Their own
  text says "proposals only — not acted on" (`kotoba considerthese:56`). [INFERENCE; D3 should rule.]
- Kotoba and chousa HEADs now include the merged remote README/LOG hunks (`78ee57e`, `ab19cff`).
  Writers inherit those defects (K-L2).

## 10. Leads (unopened)

None of these were opened in this session. The identities are export-asserted only: the export
carries no id or URL (`members/ClaimVsSourceCheck.md:98`).

- Agent-memory literature (ApprovalTable B-01..B-07):
  - Voyager (Wang et al., 2023)
  - Generative Agents (Park et al., 2023)
  - Reflexion (Shinn et al., 2023)
  - Dynamic Cheatsheet (Suzgun et al., 2025)
  - ACE (Zhang et al., 2025). Claim to check: AppWorld 18,282→122 tokens; accuracy 66.7→57.1 vs a
    63.7 baseline.
  - Memento-Skills (Zhou et al., 2026). An existence check was flagged in `ApprovalTable.md:115`.
  - LEGOMem (Han et al., 2025)
- Japanese lexicon (A-01..A-03, C-01): Kotobank / Shōgakukan Digital Daijisen / Nihon Kokugo Daijiten
  entries for 職人気質, 見習い, 職人, 極み, 匠, 名匠, 親方, 師範, 守破離, 免許皆伝, 自律, 人為, 流, 自己立法.
- Rank institutions (C-02..C-06): Nihon Ki-in rank pages; Kodokan; Japan Karate Association; All
  Japan Kendo Federation shōgō; J-STAGE articles by Todo and Murata on grading history.
- Workshop accounts (A-04..A-07): adachi-hanga.com; the Taitō City interview with Ishii Torao; the
  Echigo Yoita forged-blade association; the Takenaka Carpentry Tools Museum report on Ogawa and
  Nishioka.

## 11. Counting commands (cwd = fleet root unless noted)

| value | command |
|---|---|
| 32 | `ls .ufo/waves/shokunin12h-20261014-p5-chousa-r1/members \| wc -l` |
| 34 rows / 34 pending | `grep -cE '^\| [A-Z]-[0-9]{2} ' .ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/ApprovalTable.md`; same rows piped to `grep -c '\| pending \|'` |
| 10 RJ / 9 CL | `grep -cE '^\| RJ-[0-9]+' chousa-shokunin/corpus/knowledge/archived-export-intake.md` (and `CL-`) |
| 114 | `git -C chousa-shokunin grep -il -E "deep-research\|research/README\|A-shokunin-tradition\|B-multiagent\|C-rank-taxonomy" \| wc -l` |
| 0 | `git grep -n -i -E 'research/\|deep-research\|kimi-model-routing\|considerthese' -- LOG.md SCORECARD.md ROADMAP.md CORPUS.md LEARNING.md MISSION.md \| wc -l` |
| 681 | `find research/round-18-kimi-model-routing -type f \| wc -l` |
| 24 | `git log --oneline -- research/round-18-kimi-model-routing \| wc -l` |
| 3+2 / 0 | `git grep -c -E "jin'i-ryu\|Jin'i-ryu" -- PROTOCOL.md README.md`; `git grep -i -c -E 'coined\|coinage' -- PROTOCOL.md README.md AXES.md LEARNING.md MISSION.md CORPUS.md PROTOCOL-APPENDIX.md templates \| wc -l` |
| 8 / 0 | `git -C ~/Projects/kimi-shokunin grep -c -E "jin'i-ryu\|Jin'i-ryu"` (summed); same repo `grep -i -l -E 'coined\|coinage' \| wc -l` |
| 0 | `git grep -i -l 'kishitsu' -- . ':!research' ':!.ufo/waves' \| wc -l` |
| 13× shonen | `python3 -c "import json;from collections import Counter;print(Counter(r.get('rank') for r in json.load(open('MANIFEST.json'))['roster']))"` |
| 36 / 16 | `git -C kotoba-shokunin rev-list --count --until='2026-10-19T08:01:25-03:00' c8b53ac..36ab0d3`; same range `log --format=%s \| grep -cE '^round [0-9]+: publish'` |
| 6 | `git -C chousa-shokunin rev-list --count --until='2026-10-19T09:06:17-03:00' 38f217e..098f5e6` |
| 3 | `grep -lE '^\*\*Domain:\*\* (>\|")' *-shokunin/README.md \| wc -l` |
| 8 + 8 | `git -C kotoba-shokunin branch -r \| grep -c origin/cursor/` (same for chousa); all fail `merge-base --is-ancestor <b> HEAD` |
| 5 files / 4 lanes; 4 | per lane: `git -C <lane> ls-files \| grep -cE '(^\|/)__pycache__/\|\.pyc$'`; `... \| grep -c 'interactive-sessions/'` |
| 0 | per lane `git -C <lane> grep -l -i considerthese` outside the two files; fleet root and upstream `git grep -c -i considerthese` |
| 0 | `find . -path ./.tower -prune -o -path '*/corpus/lessons/operator-*' -print \| wc -l` |
| 521 / 434 | `wc -l kotoba-shokunin/SKILL.md chousa-shokunin/SKILL.md` |
| 22 / 40280 | `grep -c '^\|' chousa-shokunin/SKILL.md`; `wc -c chousa-shokunin/SKILL.md` |
| 0 / 0+0 | `grep -cE 'M7\|M8\|M9\|M10\|OVERRIDES\|legorder\|opus' kengaku-shokunin/corpus/knowledge/kimi-model-routing-round18.md`; `grep -cE '^(source\|verified-at\|recheck):'` on that file and `probe-battery-r19.md` |
| 644 / 644 | `stat -c '%a %y %n' ~/.config/systemd/user/glm-flash-shim.service ~/.config/systemd/user/ds-flash-shim.service` (metadata only) |
| 0 | `ss -ltnH 'sport = :8799' \| wc -l` |
| 0 | negative sweeps (grep, not semantic): `git grep -l -i -E 'operating cost\|cost per (claim\|round\|admit)\|token spend\|tokens per (claim\|round)'` over lane `SCORECARD.md SKILL.md`; `git grep -n -i -E 'route admission\|native route\|admission path\|round-17 blocker'` in kumitate; `git grep -n -i -E 'pycache\|gitignore'` in `kotoba-shokunin/verifiers/*.py` |
