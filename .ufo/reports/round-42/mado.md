# mado — round 42 report (hyaku run 7, attempt 1) — honest stop

**round 42 attempt 1: wave 1 planned (36 seats) but not dispatched — run ended.** The orchestrator wrapped run 7 up (dispatcher spawn cap 0) after the `w1.ready` handoff sat untaken; no seat ran and no data landed. Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`a62f2e0c3a5d1737bcf93ac45ae98a1b195e1341`** (`git ls-remote origin refs/heads/master` prints it). Round shape as planned: two v1 waves (`w1` 36 seats build + first falsifiers, `w2` ~36 seats falsify); actually run: **0 seats**, no residual call, round total **0**, dead seats 0 (none spawned). Planner seat: held by the L1 (`MadoR42`). Open L0 questions: none. Tool installs: none. The round's claims are **unverified and unadmitted**; a later attempt re-dispatches round 42 from the freeze below.

## Work performed

Declared claims (frozen before any data, `.ufo/waves/round-42/registration.md`): **C1 operability (capability acquisition)** — `tools/mado-geometry.py`, a read-only join of `windowrule = size W H, match:class RX` lines and one `hyprctl clients -j` dump (AGREE / DIFFER / TILED / BADSIZE per matched client); **C2 coverage (sourced, assimilation of the gkeep-geometry theme of `merge/mado/`)** — `corpus/knowledge/hyprland-gkeep-geometry-r42.md`. Lowest-axis rule: every published axis ties at its maximum at base (`receipts/axis-base.txt`: navigation 59/59, calibration 63/63, operability 12/12, `MADO_AXIS checked=3 mismatched=0`).
- Round start: deleted the two untracked round-41 seat scratch files routed by `corpus/lessons/round-41-verifier-spotcheck.md` §6.1 (`.ufo/waves/round-41/w2/ExecDiffFuzzV2/scratch/s-grow`, `s-size`); lane tracked tree clean at the end (`jj-lane.sh state` ahead=0).
- Pre-wave source fetches (C2 pins) and host receipts: `.ufo/waves/round-42/fetch/` (seven Hyprland v0.56.2 files at `efb50993780079460b0cbed1363e2166a2de1d9f`, `host-gkeep.conf` sha256 `3726e488…`, `host-clients-r42.json`, `gkeep-ui-excerpt.py`), hashes in `receipts/fetch-sha256.txt`.
- Facts read from those pins by the L1 (not yet entries or rows): the rule match engine is `re2::RE2::FullMatch` with a `negative:` prefix (`fetch/Hyprland-RegexMatchEngine.cpp:10-16`); `static_.size` is an expression consumed in the floating branch (`fetch/Hyprland-DefaultFloatingAlgorithm.cpp:55-66`); `hyprctl clients -j` reports `w->size(GEOMETRIC_GOAL)`, the animation goal (`fetch/Hyprland-HyprCtl.cpp:394-395,412-413`). The host's gkeep rules declare float, center and `size 420 500` for `^(org.omarchy.gkeep)$`; `hyprctl clients -j` shows 4 clients and no gkeep window.
- Frozen predicates and controls: C1 counter `quality/counters/c1-r42-geometry.py` (37 fixtures + clauses a, b, b2, b3, g, run in a bubblewrap sandbox under `RLIMIT_NPROC = 1`), reference `.ufo/waves/round-42/c1/ctl-ref-tool.py.txt` (selftest 73/73, scores 37/37 TARGET_MET), controls `ctl/run-c1-controls.py`; C2 counter `quality/counters/c2-r42-gkeep-entry.py` (clauses a–i: the round-41 v2 counter plus word-bounded quotes, a computed `<receipt>:<line>` locator per cited id, three own-work census lines recomputed from pinned host receipts), controls `ctl/run-c2-controls.py`.
- Defects the controls found and closed before the freeze (each a mistake of this round, fixed with the control that shows it can fail): a stdin-echo control hung the first C1 controls run for 30 minutes (3-timeout breaker added to the counter); three equivalent mutants (M03 loop bound, M20 a dead `#` contract clause — the sentence and the code were deleted, M38 empty regex already refused) are excluded **by name** in the runner and receipt; one missed mutant (M26, strict UTF-8 decode) is now killed by an invalid-byte-in-JSON-string input; C2 control P first failed (quotes under 3 words, a held-id entry line without a locator, mutant F6 editing a directory component the counter does not read) and every mutant "failed" for that reason until P was fixed.
- Wave 1 (`make-w1-spec.py` → `w1-spec.json` → `w1-dispatch.json`, accepted by the policy-v1 validator: 36 seats — executor 13, scribe 7, scout 3, connector 3, reviewer 3, critic 3, mutation-tester 2, simplifier 1, sentinel 1; 69% m_flash-routed roles, 25% attack roles) was written and handed off with a `w1.ready`; it was never spawned. The uncommitted `w1.ready` was removed so a later attempt's dispatcher cannot pick up this stale handoff.

## Landed changes

| Commit | Change | LOG |
|---|---|---|
| `809dc2caef09d9cbf15a496e55a1b208803a3561` | freeze: registration, counters c1/c2-r42, controls, reference, fetch receipts, before-receipts | Round 42 attempt 1 bullet 1 |
| `17b395658187cb408fa301bb22e6d7bf6ed9a93a` | w1 spec, dispatch and validator registry | bullet 1 |
| `a62f2e0c3a5d1737bcf93ac45ae98a1b195e1341` | LOG entry, census-after receipt (lane tip) | all bullets |

(The orchestrator's interrupted-run snapshot `8af026305bd93c1d6011c016b8a3b148832a4f07` carried only this round's uncommitted pre-freeze work.) Nothing in `tools/`, `corpus/knowledge/`, `PROVINCE.md`, `SKILL.md`, `corpus/SOURCES.md` or `corpus/lessons/` changed this round.

## Before → after measurements

Targets are not met; this is an honest stop, not a narrowed claim.
- **C1** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r42-geometry.py --repo . --rev <rev>`: before at base `62dd798bb08401a8697383552edcc36f109344fa`: `fixtures=0/37 tool=absent verdict=TARGET_MISSED`, exit 1 (`.ufo/waves/round-42/receipts/c1-before-base.txt`). After: tool absent at the tip — **not met** (target `37/37 TARGET_MET`). Controls: `receipts/ctl-c1.txt` — `CTL_C1 VERDICT: PASS`, 46 controls (absent base, 3 do-nothing, 5 cheats, 37 mutants), none reaches TARGET_MET; the reference does.
- **C2** `python3 -I quality/counters/c2-r42-gkeep-entry.py --repo . --rev <rev>`: before `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-before-base.txt`). After: entry absent at the tip — **not met** (target `admitted=1/1`). Controls: `receipts/ctl-c2.txt` — `CTL_C2: controls=74 correct=74/74` (genuine control P admitted under the real and pin-patched counter, 72 mutants/forgeries rejected, including the mid-word-quote and wrong-locator holes routed by the round-41 closure).
- Harm watch: no tracked domain file changed, so no harm run was needed; `receipts/axis-base.txt` re-derived at base; domain-versus-meta ratio of the last 30 commits not recomputed this round (criterion 60: this round made **no domain-facing change** and says so).

## Sources & frontier

Census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`): start `receipts/census-before.txt` exit **0** (`mado ok`, W04 ×7 + W01 S277), end `receipts/census-after.txt` exit **0**, identical. Registry rows 226 → 226 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); rows added 0; rows touched old→new: none; frontier rows advanced: none. No row was written because no source was opened for a row by a seat this round (the pre-wave fetches are receipts, not rows; S290–S299 stay reserved for the next attempt). Assimilation: **none this attempt** — the gkeep-geometry theme (11 staged files, ranked best by the round-41 scout) is planned for the next attempt; no id guard, quarantine slice, ADMIT or REFUSE was run. considerthese: `considerthese/2026-10-25.md` proposal 2 was chosen but not mined. The frontier step's mined mistake and sourced claim are therefore **not done** (conformance defect of this attempt): the mistakes of this round are recorded in LOG.md and above, to be lifted into `corpus/lessons/round-42.md` `## Mistakes` by the re-dispatched attempt.

## Trend verdicts

- **expansion: unchanged** — no knowledge entry, row or capability landed.
- **quality: unchanged** — no admitted entry was touched; the frozen instruments are stronger than round 41's (word-bounded quotes, computed locators, recomputed census lines, a timeout breaker) but unscored by any seat.
- **discernment: unchanged** — no gate decision was made; the round-41 spot-check's routed items 1–2 were acted on (leftovers deleted; C2 mid-word quote and wrong-locator holes closed in the counter), item 3 (S041 held-row citation, tool ergonomics) and item 4 (`PROVINCE.md:75-76` cite) remain open.

## SHONEN

- [~] SKILL.md real decision tables — historical (`SHONEN.md:5`); unchanged this round, no outside-lane verifier.
- [~] End-to-end domain task logged — the live read-only run of the reference on the host (`hyprctl clients -j | … --rules ~/.config/hypr/gkeep.conf` → `NO_MATCHING_CLIENT`, 4 clients, no gkeep window) is recorded in LOG.md Round 42; no non-author verifier.
- [~] Instructions executable without oral context — unchanged; dispatched seats were not run, so no new evidence.
- [~] No cross-domain bleed — PROVINCE.md untouched; the sibling-overlap scan (`ConnSiblingOverlap`) was planned and did not run.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` run before filing (it lists only the driver file `.ufo/state/mado.report-baseline`, left untouched, and this report); no seat of this lane wrote into the fleet root because none ran.
