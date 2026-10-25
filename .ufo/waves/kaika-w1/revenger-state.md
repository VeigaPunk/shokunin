# STATE dossier — lane `revenger` (kaika W1, 2026-10-19)

Scribe: W1StateRevenger · read-only sweep; sole write is this artifact.
Repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (roster name `shokunin-binary-forensics`).

## 1. Identity

- Domain: "Reverse engineering of shipped artifacts under the evidence-ledger discipline — byte-oracle fixtures, Evidence IDs, forged-claim rejection controls" (README.md:5-7).
- Rank: **shonen** — fleet `MANIFEST.json:98` `"rank": "shonen"`, minted 2026-10-11 (`MANIFEST.json:100`). `SHONEN.md` present with 4 boxes: 0 checked, 3 partial `[~]`, 1 unchecked (SKILL.md absent) — `SHONEN.md:5-16`.
- Git: branch `main`, HEAD `8bbcb4e` "revenger: ignore interactive session logs"; clean — `git status --porcelain | wc -l` → `0`; `git log --oneline -5` → top `8bbcb4e`, then `b63858d` "protocol conformance: adopt SCORECARD.md contract fields (2026-10-16 operator amendment rollout)".
- Last lane round: **60** — `grep -nE '^## Round [0-9]+' LOG.md | awk -F'[ :]' '{print $4}' | sort -n | uniq | tail -1` → `60`. Round 60 (devin) admitted coverage improved via adjudicator `reports/round-59/r59d-adjudicator.md` (author round renumbered 60 because r59 slot held the falsified malformed-UTF-16 round). Evidence: `reports/round-59/{r59-author,r59-devin-verifier,r59d-adjudicator}.md`.
- Current open round: **fleet round-1** (separate numbering, "not a renumbering of imported r1–r60", LOG.md:723-725) — **BLOCKED / unadmitted**: "Status: BLOCKED / unadmitted. Verified completed rounds added: 0." (lane `.ufo/reports/round-1/revenger.md:3`).
- Next round number: **61** (lane numbering) after fleet round-1 closes; immediate next action per SCORECARD interactive-continuation `planned:`: operator establishes global role bindings, then "a fresh interactive L1 continuation revalidates the same 32-scope spec and dispatches its complete canonical payload once" (SCORECARD.md:108-110).

## 2. Fleet-ledger verification (assignment hint)

- Fleet `MANIFEST.json` `rounds[]`: 294 entries — `jq -r '.rounds | length' MANIFEST.json` → `294`. Lane distribution — `jq -r '.rounds[].lane' MANIFEST.json | sort | uniq -c`: audio 4, chousa 9, game-dev-2d 4, game-dev-3d 4, kaidoku 14, kotodama 5, mado 10, null 214, tabi 10, tameshi 10, tsukuroi 10. **Zero `revenger` entries.**
- Total `revenger` mentions in MANIFEST: 4 — `grep -c 'revenger' MANIFEST.json` → `4`: roster id/name (`:95-96`) + two kaidoku round notes citing revenger evidence (`:2782`, `:2810`). No rounds entry under any key (also checked `binary-forensics`: only the roster `repo` field `:99`).
- Fleet `.ufo/reports/round-1/` holds 10 lane reports (kaidoku, kama, kasegi, kengaku-shokunin, kotoba, kumitate, mori, protocol, souji, web-properties-publishing) — **no `revenger.md`**; the lane's handoff report sits unpicked at lane `.ufo/reports/round-1/revenger.md`.
- Reading: the fleet ledger lags the lane by design for the blocked fleet round-1 (PROTOCOL.md:237 — integrator appends `rounds[]` entries; admission blocked → none yet), but imported historical r1–r60 were also never integrated. Fleet-recorded revenger rounds: **0**; lane-own LOG rounds: **60 + 1 blocked fleet round**.

## 3. Axes

Active mission axes: coverage + calibration (SCORECARD.md:3). Historical depth is retired as a scoring axis: "retired: historical depth scoring, wrong-fit for this dispatch's coverage+calibration assignment, not saturation" (SCORECARD.md:65-66).

| axis | score | evidence / command | last change |
|---|---|---|---|
| calibration — selected saved-ledger runnability | 2.5 → 5.0 | C command (SCORECARD.md:33-46) rerun live: `CALIBRATION 2 / 4 score= 5.0`; `REPLAY 8 / 10` | fleet round-1 |
| coverage — selected-family record presence | 5.0 → 5.0 | F command (SCORECARD.md:49-61): `COVERAGE 4 / 8 score= 5.0 families= ['native-static', 'javascript', 'archives', 'evm']` | fleet round-1 init; unchanged |
| depth (historical, retired) | unmeasured | imported table SCORECARD.md:127-133 | r52/r47/r42 reviewer-verify receipts |

- **Lowest non-retired axis: calibration and coverage tied at 5.0** — "The two proxies tie after this move; that is not saturation" (SCORECARD.md:18-19). Calibration was lowest before the fleet round-1 move (2.5).
- Live verifier ground truth (this session): 8/10 pass; `verify_icon_languages.py --self-test` exit 1 → `AssertionError: r47: artifact`; `verify_multi_icon_states.py --self-test` exit 1 → `AssertionError: r42: artifact`. Exactly the two named failing ledgers (SCORECARD.md:21-22).
- Saturation line: **not declared** — "to be declared by the lane on its next round per `AXES.md` §The stagnation nudge" (SCORECARD.md Saturation section).
- Capabilities: **0** — table reads "— none yet —"; rows enter only through a round demonstrating the capability running (SCORECARD.md Capabilities).
- Planned claims: (a) original planned — "isolate the existing `verify_icon_languages.py` artifact-path failure with unchanged saved inputs" (SCORECARD.md:59-61); (b) superseding interactive-continuation planned — keep fleet round-1 open; operator route bindings first; no language-ledger advance this session (SCORECARD.md:108-112).
- Halted: calibration's historical r59 malformed-name validity/refusal criterion — "remains **halted and falsified**" (SCORECARD.md:67-68; LOG.md:707-721); adjudicator: "Calibration axis remains HALTED pending newly declared criterion or operator ruling" (reports/round-59/r59d-adjudicator.md:27-28).

## 4. Corpus

| item | count | command |
|---|---|---|
| knowledge entries | 2 | `find corpus/knowledge -name '*.md' -not -name '.gitkeep' \| wc -l` → `2` |
| lessons | **2** (hint said 3 — off by one; likely counted `.gitkeep`) | `find corpus/lessons -name '*.md' -not -name '.gitkeep' \| wc -l` → `2`; repo-wide sweep for other lesson files → none |
| QUALITY.md criteria | 0 — file absent | `ls corpus/QUALITY.md` → not found |
| coverage-map rows | 0 — `corpus/README.md` absent | glob `corpus/README.md` → none |
| `## Frontier` rows | 0 — same absent file | — |
| verify scripts | 10 | `ls corpus/verify_*.py \| wc -l` → `10` |
| live run records | 344 files, 4.2M | `find corpus/live/runs -type f \| wc -l`; `du -sh corpus/live/runs` |
| fixtures | 46 dirs, 404K | `ls corpus/fixtures \| wc -l`; `du -sh corpus/fixtures` |

- Knowledge entries: `seed.md` (REA toolset census, verification discipline, calibration strategy, investigation map) and `2026-10-12-rea-readiness-checklist.md` (host-readiness decision table).
- **Metadata: 0/2 entries carry `source:` / `verified-at:` / `recheck:`** — `grep -c 'source:' corpus/knowledge/*.md` → `0`, `0` (same for `verified-at:`, `recheck:`). No overdue rechecks possible (none dated); 100% missing required fields. Caveat: both entries predate the current contract; still a defect under the wave contract.
- Lessons: `round-1.md` (fleet round-1 gate decisions: replay admitted as round evidence only; nine-role batch ≠ completed round; receipt hashes ≠ producer origin; no knowledge admission under absent bar; no outside spot-check) and `2026-10-12-r1-provider-gap.md` (native `provider_unavailable`: Ghidra `not_configured`, Hopper `executable_missing`, IDA `not_configured`).
- PROVINCE.md: owns/refuses/sources present; write scope tightened to this repository only (PROVINCE.md:25-32).

## 5. Mistakes mined (16 classes; **0 captured by a formal criterion** — QUALITY.md and SKILL.md are absent, so the discipline lives only in LOG rules, lessons, and verifier self-tests)

| # | class | evidence pointer | captured? | proposed criterion |
|---|---|---|---|---|
| 1 | r1 native `provider_unavailable` — honest stop, claim unmet, coverage not admitted | LOG.md:26-30; lesson `2026-10-12-r1-provider-gap.md` | no | readiness claims qualify only with an actual session Evidence ID; setup is not a pass |
| 2 | r7 comparison-tool 0/1 explicit-relationship detection; not admitted, kept as telemetry | LOG.md:97-100 | no | a tool-comparison claim scores the tool's explicit output; manual difference is separately labeled, never substituted |
| 3 | r15 duplicate-ZIP `Artifact path collision: same.txt` — not admitted; halted | LOG.md:189-192 | LOG rule only | halt progression on a failed route until a new route or changed input is explicitly claimed |
| 4 | r17 Wakaru `capability_unavailable` — not admitted; halt | LOG.md:211-214 | no | caller-supplied-provider absence is recorded, never retried identically |
| 5 | r25 stale jump operand confound — declared "valid jump destination" was invalid after byte shift; not admitted | LOG.md:247-253 (r25 result) | no | after any byte-shifting edit, re-derive all absolute operands/jump targets before declaring the fixture premise |
| 6 | r51 declared 160-byte directory wrong; failed input retained, corrected input re-declared | LOG.md:614-617 | no | (shared with 7) fixture construction constants must be byte-verified against the derived fixture before the producer call |
| 7 | r52 directory entry-count fields wrong; same retain-and-redeclare pattern | LOG.md:631-634 | no | same as 6 |
| 8 | r58 verifier implementation exited 1 — substituted saved `entry_locations` for byte-derived paths; rejected, repair lane dispatched | LOG.md:703-705 | no | a verifier derives expected values from bytes; never substitutes saved fields for byte-derived ones |
| 9 | **r59 invalid-surrogate refusal prediction FALSIFIED** — REA accepted unpaired surrogate name `A=\ude00B!` (raw `41003d0000de42002100`); calibration harmed relative to declared expectation; halted pending operator ruling | LOG.md:713-721; `reports/round-59/r59d-adjudicator.md` | no | a predicted refusal is a falsifiable hypothesis: pre-register strict-decoder ground truth, classify either way, never pre-classify parser malformed-input behavior |
| 10 | r59-devin author said 7/7 dirs; verifier found 8/8 — correction adopted | `r59d-adjudicator.md:24-25` | no | non-author byte counts supersede author prose counts |
| 11 | r18 ledger typo (wrong seed ID, referred to `rot13(input)` line 4) — caught by reviewer pre-commit | LOG.md:224 | no | ledger seed IDs are checked against request JSON before commit |
| 12 | r30 boundary-checklist mislabel (556 is name child-directory pointer, not data-entry pointer) — corrected with attribution | LOG.md r30 result | no | byte-offset role labels cite the decoded structure, not memory |
| 13 | r35 saved JSON reformatted → byte SHA differs from receipt raw-output SHA — provenance caveat recorded | LOG.md r35 result | no | saved records are byte-preserved or re-bound to the receipt explicitly |
| 14 | r36 second refusal's stated interval cause not independently reproduced — refusal not used for a calibration claim | LOG.md r36 result | no | a refusal cause is claimed only when independently reproduced |
| 15 | `evidence_id` path-sensitivity discovery: `ev = f(content, path, params)` — same bytes elsewhere minted `ev_50038b96…`; later adjudicated cross-lane (kaidoku removed the false universal "evidence ids are f(content, path, params)" from summary sites, MANIFEST.json:2782) | `r59d-adjudicator.md:26`; MANIFEST.json:2782 | no | candidate knowledge entry (see §7) |
| 16 | fleet round-1 routing `MISSING_BINDING` ×5 — reviewer/critic/sentinel require `@m_grok` (observed `@m_mid`/`@m_strong`), scribe requires `@m_composer` (observed `@m_fast`), connector requires `@m_antigravity`+`@m_zfl` fallback (observed `@m_mid`); assessment exit 2; admission blocked | lane `.ufo/reports/round-1/revenger.md` routing table; LOG.md:739-758 | lesson `round-1.md` gate 2 | operator-owned; reported, not absorbed (adjacency discipline) |

Gate disagreements: (a) predecessor's nine-role batch + validated 32-scope plan + local acceptance **not** counted as a completed round (lesson `round-1.md` gate candidate 2, rejected); (b) "no new `knowledge/` entry admitted. `corpus/QUALITY.md` is absent; do not invent a quality bar" (lesson `round-1.md`); (c) r26 operator pause superseded only for the dispatched r27 (LOG.md:258-262).

## 6. Contract defects

1. **`SKILL.md` absent** — `glob revenger-shokunin/**/SKILL.md` → none. Required at mint (PROTOCOL.md:42); SHONEN box 1 unchecked: "`SKILL.md` is absent" (SHONEN.md:6); SCORECARD named debt; README.md:10-12 documents seed-form absence. **Confirmed defect, not just hint.**
2. **`AGENTS.md` absent** — PROTOCOL.md:42-43 mint list includes it; SCORECARD named debt.
3. **`corpus/QUALITY.md` absent** — README.md:13-14 promises "QUALITY.md (the admission bar)"; lesson round-1.md blocks knowledge admission on it; SCORECARD named debt. Highest-leverage defect: it gates all corpus admission.
4. **`corpus/README.md` absent** — coverage map + `## Frontier` missing; SCORECARD named debt.
5. **Knowledge metadata missing** — 2/2 entries lack `source:`/`verified-at:`/`recheck:` (commands §4).
6. **Fleet-ledger divergence** — MANIFEST `rounds[]`: 0 revenger entries vs lane LOG 60 rounds + blocked fleet round-1; fleet `.ufo/reports/round-1/` lacks `revenger.md` (handoff unpicked in lane `.ufo/`). Open L0 touching this lane: tsukuroi round-1 asks to "arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed" (fleet `.ufo/l0-questions.md:42`).
7. **Hint discrepancy** — lessons 3 (hint) vs 2 (measured, command §4).
8. **Bloat (by design, append-only — noted, not actionable without protocol-gated compaction)** — `stat -c '%s'`: LOG.md 195,343 B / 764 lines; SCORECARD.md 26,965 B / 156 lines; corpus/live/runs 4.2M / 344 files; `.ufo` 2.3M / 15 files. Bulk is per-round wave-spec rosters (8-worker tables) — historical identity.
9. **Dead pointers: none found** among checked targets — `~/.agents/skills/reverse-engineer-anything/SKILL.md` present; `~/Projects/gamez/research` present; `corpus/live/runs/promotion-review-r5.md` + `review-r1-r3.md` present. Historical `.shokunin/revenger/**` paths in LOG are recorded identity, not live pointers (PROVINCE.md:31).
10. **Stray artifacts: none** beyond by-design run records; `.gitignore` (27 B) covers only `.ufo/interactive-sessions/`.
11. **Uncommitted changes: 0** — `git status --porcelain | wc -l` → `0`.

## 7. Proposed round (for wave 2; ≥1 claim on the lowest non-retired axis — calibration/coverage tied 5.0)

- **Claim 1 (calibration):** isolate `verify_icon_languages.py`'s artifact-path failure with unchanged saved inputs (ROOT-reads / HIST-identity split, the proven named-ledger pattern). Falsifiable: before `python3 -B corpus/verify_icon_languages.py --self-test` exit 1 `AssertionError: r47: artifact` → after exit 0 `PASS: 3/3 group-language states…`; counting command = SCORECARD C command → `CALIBRATION 3 / 4 score= 7.5`. Guardrails: 9/9 input SHA unchanged, forgery rejections retained. This is SCORECARD's own planned move; sequencing gated on fleet round-1 closure.
- **Claim 2 (calibration):** same repair for `verify_multi_icon_states.py` (before exit 1 `AssertionError: r42: artifact`) → `CALIBRATION 4 / 4 score= 10.0`. Serves SOURCES.md: the ROOT/HIST repair pattern becomes a knowledge entry citing the lane's own round-1 lesson + verifier source (own-work, tier-A).
- **Claim 3 (coverage or contract restoration):** either add one missing saved-record family (managed or android) via provider-neutral fixture + producer call → `COVERAGE 5 / 8 score= 6.25` (heavier; needs REA CLI run; r15/r17 halts do not block a distinct family), **or** — recommended first — the named-debt restoration: reconstruct `corpus/QUALITY.md` + `corpus/README.md` (+ `SKILL.md`, `AGENTS.md`) as a separately declared sourced move with an outside admit/reject spot-check. This unblocks knowledge admission, the gate registry, and wave-2's SOURCES.md landing.
- Candidate knowledge entries: (a) "REA `inspect-pe-resources` preserves unpaired UTF-16 surrogates in resource names (JSON `\ude00` escape) rather than refusing; strict UTF-16 decoders reject the same bytes" — source: r59 saved Evidence `ev_8ab30e10…` + Unicode §3.9 (surrogate code units are not scalar values); fills the halted r59 criterion's ground truth. (b) "`evidence_id` is path-sensitive: `ev = f(content, path, params)`" — source: `r59d-adjudicator.md:26` + kaidoku adjudication (MANIFEST.json:2782). (c) "Saved receipt hashes bind stdout consistency, not producer origin" — source: lesson `round-1.md` + r35 provenance caveat.

## 8. Verification commands used this session (all read-only)

`git log --oneline -5`; `git status --porcelain | wc -l`; `git branch --show-current`; `jq -r '.rounds | length'`; `jq -r '.rounds[].lane' | sort | uniq -c`; `grep -c 'revenger' MANIFEST.json`; `grep -nE '^## Round [0-9]+' LOG.md`; verifier self-test loop (10 scripts); SCORECARD C command; `stat`/`du`/`find`/`ls` counts; metadata `grep -c`; pointer-target `ls` checks. No repo file was modified; no git mutation; no producer call.
