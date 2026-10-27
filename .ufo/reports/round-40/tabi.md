# tabi — round 40 report

## Work performed

Declared claim: **C1 — coverage capability**, a nonce-bound Playwright Firefox loopback TCP measurement that records actual sample spans and fails closed on unavailable observation surfaces. It is the sole round-40 claim; the stagnation nudge waived the lowest-axis obligation (adjacency 8) because all owned axes were at/above saturation 8 and no capability entered during rounds 37–39. Frozen claim and control chain: `.ufo/waves/round-40/claims.json`; baseline `a1b1e939048885d2793759b7f49b10c5c820d70d`; final pre-data claim freeze `07e99cf1e2f67c5679aa5ba1ccb19a8f59b228e4`.

- Reopened S145 (`proc_pid_net(5)`) from `https://man7.org/linux/man-pages/man5/proc_pid_net.5.html`, HTTP 200, 17,119 B; retained HTML, sha256, anchor and quote in `.ufo/waves/round-40/sources/`. `S145-open-recount.txt` corrects the extended quote's 12-word count; the registry's exact quote is 11 words.
- Froze C1 before data with a do-nothing round-39 receipt refusal, then found and fixed an unavailable-surface false green before dispatch. The initial freeze `cb35339d81b425f486f9cb34a08111996be61b8a` and intermediate revisions are preserved and explicitly superseded; the final counter, live measurement wrapper, driver mode, nonce controls and frozen digests are at `07e99cf` (`claims.json`, `c1-sample-span-v3.mjs`, `measure-c1-round40.mjs`, `playwright-firefox-egress-round39.mjs`).
- A parser-only synthetic positive exposed that structural receipt scoring could pass without a browser. Before any seat data, changed the official counting command to launch the driver, create a fresh nonce, refuse existing output paths, verify receipt/run nonce binding, and score the produced receipt. The 7-case wrapper/nonce selftest is `.ufo/waves/round-40/controls/c1-measure-selftest-v2.json`; synthetic receipts are selftest-only and are not claim evidence.
- Validated one policy-v2 wave: `.ufo/waves/round-40/w1-plan.json` records 64 seats, one task call, no resumes, and attack share 19/64. Final spec/dispatch/registry and ready handoff are pinned at `250a38056438dc62a8ddcfbdfcdc065bfab9a048`; the orchestrator reported WAVE-DONE for all 64 seats. `.ufo/waves/round-40/w1-results.json` has 64 nonempty final outputs; seat reports/evidence are under `.ufo/waves/round-40/w1/`.
- Ran the frozen C1 command once against the live loopback fixture; output and receipt are committed in `corpus/evidence/round40/playwright-egress/`. The measured bytes satisfy the literal counter, but the claim is **not admitted** because W1 CritControlReach F4-full shows the same wrapper can be made to return predicate=true via a `NODE_OPTIONS=--require` driver replacement with no Firefox launch. Details and the stress/no-observation/tree findings are in the Gate and Mistakes below.
- Hand-checked the full 38-row staged quarantine slice; verdict per staged ID and source-row disambiguation are in `corpus/lessons/round-40.md` and the corresponding `ScoutQuarantine*` reports. Package adoption remains closed; no package row or knowledge entry was appended.
- Mistakes from rounds 37–39 were read first (`.ufo/reports/round-37/tabi.md`, `round-38/tabi.md`, `round-39/tabi.md`, and `corpus/lessons/round-39-verifier-spotcheck.md`). C1 closes the sample-span proxy defect only; wrapper provenance, process-tree refresh, and sampling blind spots remain open. The final no-op finding is reported, not amended after data.
- Accidentally sent one `agent://all` coordination message before Main replied; the tool reported 140 recipients. Switched to direct `agent://Main` messaging, made no cross-lane writes, and recorded the process mistake in `LOG.md` and the lesson.

## Landed changes

All lane changes are tied to the round-40 entries in `LOG.md`; commits were made only through `jj-lane.sh --as tabi`.

- `cb35339d81b425f486f9cb34a08111996be61b8a` — initial C1 sample-span freeze, round-start census/source bytes, no-op control and LOG entry (superseded before dispatch).
- `1db426e487e8c68ff8768da1f35a4be398a821e3`, `c2b89814232b921619e6f6b45822dfeeaa9832f0`, `c1304773787f3f0cb7b3a0a7cb0a37db56be8155` — scorecard declaration, unclaimed residual boundary, and reopened S145 source evidence.
- `ade9923dda9bc4bb3ae7e14704664ee951645873`, `af86ec4e72fdba447e2e1bf3fde29eefba00ccc1`, `c451a3c401741e5cc34239e0df63d113d86267e5`, `046f63a3214ff41d56bc949aa4d1010a23046ba3`, `8a387c0ca0428cedf6399d097f1fd24321764123`, `bf6a7cfaad046c923eeb686eda6dd8b3305c06a1`, `07e99cf1e2f67c5679aa5ba1ccb19a8f59b228e4`, `250a38056438dc62a8ddcfbdfcdc065bfab9a048` — validated wave payload and successive **pre-data** control/freeze/dispatch corrections. Final operative claim/counter freeze is `07e99cf`; final v2 spec/dispatch is `250a380`.
- `c0256902708bb6b9f466f35181a7872b75777c56`, `18bac4e9443d9d439b14d929b9ab0bb034427ef5`, `df9f1b65f68d5133251df58f100d5aebba3f77a1`, `c925d9230c3f7908152fad7bc0f0dd1cdd9af45f`, `f8e89d7ca14235f5d2146999b190c00122c011fb` — append-only dispatch-reference/process/census/claim bookkeeping corrections; the start exit-code file is labelled as a later transcription, not a contemporaneous receipt.
- `22883df61d8deb55e03a1afebc81f7290c3a3cfc` — live measurement receipt and wrapper output, wave results/reports, lesson, S145 used-by old→new, full census-end receipt, and committed-receipt binding counter.
- `93fdd032d0531737a788c3c67d3427d1a7720aa8` — scorecard C1 disposition and `corpus/evidence/round40/measurement-binding.json`.
- `26cfde0382e4512f8e357690526a21c594991d86` — LOG measurement-binding record. Final lane tip at filing is `26cfde0382e4512f8e357690526a21c594991d86`; `jj-lane.sh state` and `git ls-remote origin refs/heads/master` both showed this hash, `ahead=0 behind=0`.
- Fleet L0 append: `.ufo/l0-questions.md` C1/F4 future-freeze question, committed via `fleet-commit.sh --as tabi` at `58cffd1f42723048bcfe48eb0bc2f346caa9b77f`.

## Before → after measurements

| Claim | Before | After / measured revision | Counting command | Verdict |
|---|---|---|---|---|
| C1 coverage capability | At baseline `a1b1e939048885d2793759b7f49b10c5c820d70d`, the committed round-39 receipt had no r40 schema/nonce and actual sample spans of 799 ms / 701 ms. C1 v3 replay control with a fresh nonce: exit 1, findings `schema`, `run-nonce-mismatch`, `run1-sample-span`, `run2-sample-span` (`.ufo/waves/round-40/controls/c1-round39-replay-v3.json`). | At measured revision `22883df61d8deb55e03a1afebc81f7290c3a3cfc`, the frozen command exited 0: wrapper/driver/counter all exit 0; `predicate=true`; fresh nonce matched; two live runs span 1204 ms / 1202 ms, 13 samples each, recorded ss/proc rows 9/9 and 10/10, zero recorded nonLoopback, zero survivors, closed ports, Firefox 157.0, identical first-shot hashes. Binding manifest re-derives `c1_live_runs` 0→1; `check-measurement-binding --at 26cfde0382e4512f8e357690526a21c594991d86 --reproduce` returned `verdict=clean`, `claims=1`, `bound=1`, `findings=[]`. | `node scripts/measure-c1-round40.mjs --out corpus/evidence/round40/playwright-egress/receipt.json --scratch /fast/scratch/hyaku/tabi-r40/TabiR40a2/measure` | **Unprovable / not admitted.** A no-op environment-preload control (CritControlReach F4-full) intercepts the wrapper's driver spawn, supplies the nonce-bound synthetic receipt and exits 0 in 0.06 s with no browser. The frozen target is reachable without the claimed operation, so no coverage score or capability row is granted; coverage held 9→9. |

The actual measured receipt supports the **bounded run facts above**, not an egress-isolation or “no socket existed” claim. It records positive socket-row counts in this capture; the counter nevertheless permits zero-observation receipts because `ticks:1` is a completion sentinel and `ss.lines` / `proc.inodes` are not predicate terms. No counter, predicate, or claim was amended after W1 data.

## Sources & frontier

- Required census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  - Before: exit 0, `tabi ok`, 20 pre-existing W04 duplicate-URL warnings, no E findings; stdout `.ufo/waves/round-40/measure/census-start.txt`. The exit-0 file was transcribed after the freeze; the command's exit 0 was observed at the original run and is reported honestly.
  - After: exit 0, same 20 W04 warnings, `tabi ok`; `.ufo/waves/round-40/measure/census-end.txt` and `census-end-exit.txt`.
- Row count command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: baseline 145 → final 145. Tier histogram command/output is in `corpus/lessons/round-40.md` §Census: A129/B7/C9; mined121/queued15/rejected9.
- Added rows by tier: none. Old rows touched: S145 `used-by` changed from `corpus/knowledge/playwright-firefox-session-bound-tcp-round-39.md` to that path plus `corpus/lessons/round-40.md`; no `status` or `recheck` changed. Registry diff was 1 insertion/1 deletion for S145 only; no package rows were appended. Frontier rows advanced: none; S145 was reopened solely to ground C1.
- Quarantine-first: all 38 staged rows were hand-checked, with precise per-row classifications and seat evidence in `corpus/lessons/round-40.md` §Gate. No `merge/tabi/` package content was adopted; assimilation = **none**. No `considerthese/` directory exists.
- S145 scope and quote: Linux `proc_pid_net(5)` DESCRIPTION `/proc/net/tcp`, `rem_address` field; the extended source quote is 12 words, exact registry wording is 11. `corpus/lessons/round-40.md` records the correction and the S145 `used-by` transition. Quarantine staged S145 is a different SameSite draft row and was rejected as absent; the identities are kept separate.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, source row, or admitted capability entered; the existing S145 source was reopened and S145 `used-by` now cites the lesson. Evidence: SOURCES census 145→145; `SCORECARD.md` Round 40 disposition.
- **quality: unchanged** — no corpus knowledge entry was reverified/deepened or superseded this round; the measured tool run and its limitations are documented, but C1 remains unadmitted due the demonstrated wrapper false-green. Evidence: `corpus/lessons/round-40.md` Gate/Mistakes and CritControlReach F4-full.
- **discernment: unchanged** — no qualifying outside non-author admit/reject spot-check occurred; all wave seats were dispatched by this lane. Evidence: lesson Gate explicitly marks the outside spot-check pending.

## SHONEN

- [~] Decision tables, error patterns, checklists and cited sources — `SKILL.md` §Approval table, §Evidence ladder and §Runbook; author assessment only this round.
- [~] End-to-end domain task executed and logged — loopback Firefox run receipt `corpus/evidence/round40/playwright-egress/receipt.json`, LOG round-40 integration entry; author-run, and claim admission is not asserted.
- [~] Instructions executable without oral context — `scripts/measure-c1-round40.mjs` and the SKILL runbook; no independent cold-read promotion verifier this round.
- [~] No cross-domain bleed; PROVINCE remains accurate — `PROVINCE.md:3-19`, `w1/ConnSiblingOverlap/report.md`; adjacent process/socket mechanisms were reported, not absorbed.

## Stale-lane

Respawn-per-round driver; attempt 2 launched `2026-10-27T15:11:46-03:00`; progressing (lane-authored commits after launch); no other tabi mission is open.

## Wave shape, tooling, open questions, misroot and cleanup

- One v2 wave `w1`, 64 seats, one batched dispatch, no residual call; 64/64 result entries have nonempty final output, no empty/dead result observed. Role mix: 38 scout, 8 reviewer, 7 critic, 4 mutation-tester, 3 executor, 3 connector, 1 scribe. Attacks 19/64; L1 held the canonical planner seat. Evidence: `.ufo/waves/round-40/w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`, `w1-results.json`.
- Tool installs/updates: none. Playwright 1.64.0 and Firefox 157.0 were already present; pacman was not used.
- Open L0: new line `tabi | round-40 | W1 CritControlReach F4-full...` in `.ufo/l0-questions.md` asks for next-freeze guidance; two unanswered round-39 lines remain: run-10 swarm-band/template reconciliation and the read-only shokuknow seat artifact disposition. No answer was assumed.
- Cross-domain boundary: `ConnSiblingOverlap` found the closest mechanism overlap in kama’s `/proc/net` listener-ownership join and souji’s process-residue listing; their owned surfaces differ from Tabi’s Playwright client-connection observations. Mado’s “C1 round 40” is an unrelated label collision. Nothing was absorbed into another province.
- Required fleet-root misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed `.ufo/reports/round-58/chousa.md`, `.scratch/closure-mado-r50.json`, `.scratch/source-routing-queue.md`, `.ufo/waves/round-75/`, and `o.bin`. A read-only grep of `o.bin` for `tabi|round-40|TabiR40a2` found no match; all observed paths belong to other lanes/orchestrator and were untouched. No Tabi seat misroot was found.
- Cleanup: `/fast/scratch/hyaku/tabi-r40/` was removed after all seat evidence landed in the lane. Domain sources remained read-only.
