# mado — round 44 report (hyaku run 9, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`8ac15c412051874836e0db36b1178723ade6c340`** (`git ls-remote origin refs/heads/master` prints it). Base `6a1a90528fe533cadee506a9fa3e9d13d15cc41f` (round-43 tip + its closure). Round shape: **two v1 waves** — `w1` 38 seats (build + first falsifiers) and `w2` 33 seats (falsify the landed data); round total **71**; no residual call; dead seats **0** (every seat wrote its report; `w1-results.json` 38/38, `w2-results.json` 33/33). Role mix: w1 executor 12, scribe 8, critic 5, scout 3, connector 3, reviewer 3, mutation-tester 2, sentinel 1, simplifier 1 (m_flash roles 27/38, attack 10/38); w2 executor 10, critic 7, reviewer 7, mutation-tester 3, connector 2, sentinel 1, scout 1, scribe 1, simplifier 1 (m_flash 20/33, attack 17/33). Planner seat: held by the L1 (`MadoR44`); the planning data-walk rode `w1/ScoutStagedResidue`. Open L0 questions: none. No earlier attempt of round 44 (no `lane-dead-no-report mado round=44` line).

## Work performed

Declared claims (`.ufo/waves/round-44/registration.md`, freeze `e2289516a9a857f55cda7be635933e89b931c3da`; both **re-registered before any data** as v2 in `registration-v2.md`, freeze `03fa5c618b089064a657b3d79d3d4272ae4b6894`):
- **C1 — operability (contract extension of the round-43 capability): `tools/mado-geometry.py` names maximized/fullscreen clients** (FULLSCREEN/MAXIMIZED from the dump's `fullscreen` integer, summary fields only when present, top verdict NOT_COMPARED exit 5), judged by `PRED-C1-r44-v2`.
- **C2 — coverage (sourced; assimilation of the gkeep residue of `merge/mado/`): `corpus/knowledge/hyprland-gkeep-size-request-r44.md`** — the report size, sendWindowSize, xdg configure and serial, onAck, the protocol's hint/binding states, GTK 4.24.1's configured-size handling, gkeep's declarations — judged by `PRED-C2-r44-v2`.

Lowest-axis rule: every published axis ties at its maximum at base (`receipts/axis-base.txt`: navigation 60/60, calibration 68/68, operability 12/12), so each is a lowest axis; the claims' after-states are their counters' lines (w1/CritClaimSizing F6/F9 recorded). All paths below are under `mado-shokunin/.ufo/waves/round-44/`.

- Protocol load; round-43 closure D1-D7 routed into the lesson (Mistakes M44-1..7, errata E1-E4; D3 fixed in SKILL.md; D2 supersession deferred with reason; D7 tip axis receipt committed `receipts/axis-tip.txt`).
- Pins fetched 2026-10-26 (`receipts/fetch-sha256.txt`): `fetch/` Hyprland Window.cpp + XDGShell.cpp at efb5099, xdg-shell.xml 1.49, gdktoplevel-wayland.c 4.24.1, gkeep ui.py 133b867; `fetch-c1/` FullscreenController.hpp, FullscreenHandler.cpp, HyprCtl.cpp.
- v1 freeze with controls (`receipts/ctl-c1.txt` 0 of 15 met; `ctl-c2.txt` 0 of 3). w1 broke both v1 predicates before data: sandbox-gated and padded-selftest cheats met C1 (`w1/CritC1Cheat.md`), 9/9 forgeries met C2 (`w1/CritC2Cheat.md`), a re-pointed r12 and a quote-only entry met C2 (`w1/CritClaimSizing.md` F1), hidden census-prefix lines (`w1/RevC2Counter.md` F2); `w1/CritFsPremise.md` showed the "false report" premise wrong and an all-state dump exiting 0.
- v2 freeze: C1 adds NOT_COMPARED, b5 state-blind teeth, e environment invariance (`receipts/ctl-c1-v2.txt`: `CTL_C1v2 VERDICT: PASS (controls scoring TARGET_MET: 0 of 20; reference met: 1)`; X1 sandbox gate caught by e only, X2 padded selftest by b5 only); C2 adds T1-T4, exact census exemption, surface clause j (`receipts/ctl-c2-v2.txt`: `CTL_C2v2 VERDICT: PASS (wrong=0 of 11; positive admitted=1)`).
- Independent implementations from contract text met both C1 versions (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`, `w2/ExecIndepV2.md` 26/26); `w2/LabNotCompared.md`: 20031 random cases, 0 divergences tool vs model.
- w2 re-ran every counting command and agreed (`w2/RerunC1Data.md`, `w2/RerunC2Data.md`, `w2/RerunControlsV2.md`, `w2/RerunCensus.md`), separability both ways (`w2/ExecSeparability.md`), no harm (`w2/ExecHarmTip.md`); its content attacks drove correction commit `74c606a1c7fd52a6bb85bb1c786529c926040c73` (`w2/CritEntryHyprland.md` F1-F5, `w2/CritEntryClient.md` F1-F6, `w2/CritSkillLicence.md` F1-F4).
- considerthese `2026-10-25.md` proposal 1 (domain-vs-meta ratio) → `quality/ratio-domain-meta.py` + QUALITY 82 (`DOMAIN_META: domain=12 meta=5 window=34-43 default=1`).

## Landed changes

| Commit | Change | LOG.md Round 44 bullet |
|---|---|---|
| `e2289516a9a857f55cda7be635933e89b931c3da` | v1 freeze: registration, counters, reference, controls, pins, before receipts, id guard | 2 |
| `ae996fcf5e50d2d882dcf543a4ab2df5604dada2` | w1 spec/dispatch (38 seats) | 3 |
| `03fa5c618b089064a657b3d79d3d4272ae4b6894` | v2 freeze before data: both v2 counters, v2 reference, v2 controls, L1 draft (positive control) | 4 |
| `e46789213830597348fe96a351ae004d10587385` | **data**: tool, entry, rows S298-S301 + S164 used-by, lesson, README row + Frontier, SKILL/PROVINCE rows, QUALITY 82-84, ratio tool, SCORECARD/LOG Round 44, live receipt | 5 |
| `290cddea92a18e2202456db89cb2bb60d9aaacff` | after-data receipts, w1 evidence (38 reports), w2 spec/dispatch | 5 |
| `74c606a1c7fd52a6bb85bb1c786529c926040c73` | w2 corrections (entry, SKILL, lesson post-data corrections) | 5 |
| `8ac15c412051874836e0db36b1178723ade6c340` | w2 evidence (33 reports, results), tip receipts, handoff markers | 5 |

Inherited state: none (tree clean at start).

## Before → after measurements

- **C1** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r44-geometry-states-v2.py --repo . --rev <rev> --work <scratch>`: base `6a1a905` `fixtures=11/26 tool=present verdict=TARGET_MISSED`, clauses `a:1 b:0 b4:0 b5:0 e:1 g:1 r:1`, exit 1 (`receipts/c1-v2-before-base.txt`) → data `e467892` `fixtures=26/26 tool=present verdict=TARGET_MET`, all clauses 1, exit 0 (`receipts/c1-after-data.txt`) → tip `74c606a` same (`receipts/c1-after-tip.txt`). Self-verdict **TARGET_MET**. The superseded v1 counter misses at data (19/26: NOT_COMPARED changed the model; `receipts/c1-v1-after-data.txt`). Open predicate defects (w2, no re-registration after data): `w2/CritC1V2Cheat.md` cheat-h (state logic enabled only when cwd is the counter's work dir) reaches MET; `w2/MutC1V2.md`: 25 mutants, 1 survivor (M01, key drift inside the b5 hook, admits the X2 control); `w2/MutTool.md` survivors as listed there.
- **C2** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c2-r44-gkeep-size-request-v2.py --repo . --rev <rev>`: base `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-v2-before-base.txt`) → data `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-after-data.txt`) → tip `74c606a` same (`receipts/c2-after-tip.txt`). Self-verdict **TARGET_MET**. Open predicate defects: clause j has no range-width bound — whole-file locator ranges satisfy it (`w2/ExecDoNothingV2.md` O1, `w2/CritC2V2Forgery.md`: 7 forgeries admitted); `w2/MutC2V2.md` 18 survivors classed missing control; the claim-to-quote binding stays the non-author reading (declared).
- Harm watch: `python3 -I quality/check-axis-scores.py --rev 74c606a… --repo .` → `MADO_AXIS: checked=3 mismatched=0` (navigation 61/61, calibration 71/71, operability 12/12; `receipts/axis-tip.txt`; data commit `receipts/axis-data.txt` also 0 mismatches — no two-phase red window this round); round-43 counter on the landed tool 37/37 (clause r); `w2/ExecHarmTip.md` all fifteen base gates same exit status. No axis harmed.

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: round start (`receipts/census-before.txt`) W04 ×7 (S030, S042, S045, S097, S119, S120, S121) + W01 S277, `mado ok`, exit 0 → round end (`receipts/census-after.txt`) identical set, `mado ok`, exit 0.

- Rows 234 → **238** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by tier: **A ×4** — S298 (code, Hyprland XDGShell.cpp @ efb5099), S299 (spec, xdg-shell.xml @ wayland-protocols 1.49), S300 (code, GTK gdktoplevel-wayland.c @ 4.24.1), S301 (code, gkeep ui.py @ 133b867), all `mined`, opened 2026-10-26; Gate lines (access date, sha256, ≤25-word located quotes) in `corpus/lessons/round-44.md` `## Gate`.
- Rows touched old→new: S164 `used-by` `corpus/knowledge/rule-attribution-r24.md` → `…, corpus/knowledge/hyprland-gkeep-size-request-r44.md` (logged in the lesson). `w2/RevRows.md`: all cells verified, one LOW anchor-label note.
- Frontier advanced: `corpus/README.md` "Round-44 gkeep size-request route" (the round-43 route's open "client's acknowledgement path" item); knowledge entries 60 → 61.
- Sourced claim: C2 rests on S298-S301, opened this round (plus held S164, re-pinned).
- **Assimilation: theme gkeep residue (`merge/mado/`).** Id guard: `reg-ids` 234, `staged-ids` 147, **collisions 42** (S203..S297); proof fires on an indented scratch `  | S311 |` row, column-zero pattern does not (`assimilation/id-guard.md`); renumber map by document (`assimilation/renumber-map.tsv`: staged S311 → held S164, byte-identical tag/commit copies per `w1/CritAssimilation.md`; S312 → new S301). Quarantine slice 13 rows (`assimilation/quarantine-slice`): none cited by the residue; 7 prose rows unverifiable, none adopted (`w1/ScoutQuarantine.md`). ADMIT `gkeep-client-size-request-r12.md` (three of its sentences corrected in the entry); REFUSE r13, r14, r15, r9 with reasons and flips.
- Mistakes mined: M44-1..9 in `corpus/lessons/round-44.md` `## Mistakes` (M44-8: four rounds of C2 counters pinned only new ids' receipts — fix T1 shown able to fail by control FORGED-PIN; M44-9: the v1 premise wording). QUALITY 82-84.
- considerthese: `considerthese/2026-10-25.md` proposal 1 → QUALITY 82 + `quality/ratio-domain-meta.py`.

## Trend verdicts

- **expansion: improved** — one knowledge entry on ground absent at base (`receipts/c2-ground-base.txt`: `git grep` exit 1), rows 234 → 238, a Frontier route advanced, one capability row (state-aware join, SCORECARD Round 44).
- **quality: improved** — both instruments tightened before data after w1 broke them (v2 controls receipts), w2's content findings on the entry and SKILL corrected in `74c606a`, the round-43 closure's D3/D7 fixed and D1/D4/D5 errata appended; limits: the open v2 predicate defects above and D2 (registry supersession) deferred.
- **discernment: improved** — the lane withdrew its own premise wording on critic evidence, refused four staged files with flips and corrected three predecessor sentences it admitted, and records each v2 residual instead of claiming it closed; `w2/ConnCalibration.md` counts 4 content mismatches (LOG mistake range, a cited path the seat found absent — `assimilation/renumber-map.tsv` is tracked since `e2289516`, so that one is the seat's error — w1 paths cited before they landed, a QUALITY check path absent at the data commit), recorded for the next round. Outside confirmation is the non-author closure's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — FULLSCREEN/MAXIMIZED/NOT_COMPARED licence rows, exit map and corrected D3 note (`SKILL.md:280-293`, commit `74c606a`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged — live read-only host run of the landed tool `receipts/live-geometry-host-r44.txt` (`NO_MATCHING_CLIENT`, exit 3); LOG.md Round 44; no non-author verifier.
- [~] Instructions executable by an agent without oral context — three seats built passing tools from the contract text alone (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`, `w2/ExecIndepV2.md`); dispatched seats are not outside-lane verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE tool-row note; sibling scans `w1/ConnSiblingOverlap.md`, `w2/ConnSiblingDup.md`; no non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none by the L1; seats report none needed (python3 stdlib, curl, git, bwrap already present).

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only orchestrator/driver files and another lane's report (`.ufo/reports/round-48/tameshi.md`) — none written by this round's seats; nothing moved or deleted.
