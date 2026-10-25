# Tsukuroi — round 14: repair-first source-scope corrections

## Work performed

**Declared claim C1 — depth:** repair the two source-inconsistent propositions rejected in round13, through named corrections **R14-VALUE-DOMAIN** and **R14-COMMENT-ATTRIBUTION**, with a resolved-correction count **0→2**, exact reopened source quotes, preserved historical text and a demonstrated red-before check. Depth and adjacency were tied lowest at8; this works depth. Ordinal depth stays8→8(0), not an invented point-per-record gain. One claim only; no new capability, expanded surface or exploratory claim.

- Read the independent `corpus/lessons/round-13-verifier-spotcheck.md` first. Its MD:97 and S042 findings motivated the two named corrections; rounds12 and13 remain rejected, and their verifier files are unchanged. Evidence: lane `LOG.md` named round14 correction entries; `corpus/lessons/round-14.md` §Mistakes.
- Reopened `systemd.exec(5)` §ProtectSystem= and exact #8047/comment6071740243. The option is documented as taking a boolean argument or `full`/`strict`; non-exhaustive mechanism examples do not enlarge that domain. The comment asserts VM execution, calls Codex Medium a second opinion with independence not guaranteed, and does not establish its own generation method. Account fields are not maintainer acceptance. Its maintainer sentence concerns **#6634**; #8047 itself waits for the reporter. Evidence: `corpus/knowledge/source-scope-correction-r14.md` and `.json`; `.ufo/waves/round-14/repair/{l1-source-review,QuoteReview-source,ClaimSeparation-source}.json`.
- Repaired the two additional routed metadata defects through named **R14-S041-METADATA** and **R14-GATE-CONTRACT** errata: S041 is actually mined, and the old JSON's oversized `gate_contract` is not executable enforcement. Original keys remain historical under an additive supersession object; active references route to the new correction without discarding valid r13 teaching. Evidence: `root-dac-correction-r13.json` key `r14_supersession`, new pair §R14-S041-METADATA/§R14-GATE-CONTRACT, and LOG's supporting-errata entry.
- Mined the recurring **claim exceeds its exact source object** class into QUALITY19; QUALITY20 supersedes only criterion18's blanket bot attribution, preserving its fixture-identity rule. The same checker fails actual prior defects and restored-defect fixtures. Evidence: `corpus/QUALITY.md` criteria19/20, lesson §Mistakes/§Gate — completed author-side integration, `verification.json`.
- Dispatched one validator-approved, unchanged32-seat task batch: executor4, scout8, reviewer6, critic4, connector4, sentinel2, scribe2, revenger1, mutation-tester1. L1 holds the canonical planner seat; DataWalk is bounded revenger reconnaissance, not a forbidden planner-role bypass. All32 reports and source-retention handoffs finished before final verification. Evidence: `.ufo/waves/round-14/repair/{spec,dispatch,swarm-registry,task-result,record-result}.json` and `integration-verification.json` seat-report count32/32. No model parameter, routing mutation or second dispatch.
- Removed an uncommitted host-IP echo from an API403 message and reduced the duplicate full-body snapshot to digest/short quotes. The single retained full comment is explicitly untrusted data; none of its restore or post-output instructions were executed. Evidence: LOG §round14 pre-commit evidence hygiene, `EvidenceSentinel.md`, source snapshots and recorded safety patterns.

Mission's operability/freshness assignment is initial, not an exclusive axis fence (`MISSION.md` §The axes framework); the current SCORECARD owns all six and binds the lowest-axis obligation. This repair remains existing host/rollback-net work. Reusable verification methods remain tameshi-adjacent; fleet VM execution/correlation is not verified or absorbed from mori, and no desktop scope is absorbed from mado. `SiblingConnector.md` is author-side advice, not an ownership ruling or new adjacency gain.

Entry worktree was clean; inherited lane-authored leftovers: none. The current baseline `8606bad4cbc6451ac2890c9f8e2548a36c386db6` includes the outside round13 closure; it is not confused with the earlier lane delivery hash. No verifier or operator-owned file was edited.

**Stale-lane:** respawn-per-round; this progressing round14 session is the only open tsukuroi mission in the bounded round12–14 dispatch digest. Retained digest: round12 complete `2026-10-20T01:04:01-03:00`; round13 complete `2026-10-20T02:11:46-03:00`; current launch `2026-10-20T02:55:31-03:00 launch tsukuroi round=14 pgid=1551465 driver=hyaku-inline attempt=1`. No earlier round14 dead-no-report line was found in that sweep. This report is filed after all lane work is committed and pushed.

Tools installed/updated by L1 or any seat: **none**. Pre-existing tools sufficed. No privileged probe, snapper query, daemon activation, package transaction, boot, Btrfs operation or host remediation was performed. The mkinitcpio42 `/sysroot` versus `/new_root` hook blocker remains intact. No new L0 question was appended.

## Landed changes

**Pushed lane HEAD before report creation:** `932e32d6d2d360e18fa7fe4cdd397215fd166e4b`. The commit-and-push command completed successfully and final `git status --short` produced no lines. Lane commits carry `tsukuroi-shokunin <tsukuroi@shokunin.local>`.

| Commit | Changes | Matching LOG entry |
|---|---|---|
| `9dd82bceda4cf45c1e1e59e17c996ac898a5ecb7` | Named MD/JSON corrections, S044/S045, append-only notices and active routing, QUALITY19/20, bounded checker and registered interface, complete32-seat wave/source evidence | round14 named correction R14-VALUE-DOMAIN; R14-COMMENT-ATTRIBUTION; supporting errata R14-S041-METADATA/R14-GATE-CONTRACT; C1/depth and recurring-class prevention; pre-commit evidence hygiene; joined checker integration |
| `932e32d6d2d360e18fa7fe4cdd397215fd166e4b` | Exact measured outputs, history/source/table/safety aggregates and reproducible counting logic; final lesson/SCORECARD/LOG assessment | round14 immutable measurement and source agreement |

The second commit changes evidence and round bookkeeping only; checker bytes and its five measured input files remain those of the implementation commit. No lane work follows this report. Fresh independent closure is required; these lane-dispatched seats do not supply outside admission.

## Before → after measurements

### C1/depth — source-grounded repair, ordinal8→8(0)

Commands actually executed from the lane root:

```sh
python tools/check-source-scope-correction.py --revision 8606bad4cbc6451ac2890c9f8e2548a36c386db6
python tools/check-source-scope-correction.py --revision 9dd82bceda4cf45c1e1e59e17c996ac898a5ecb7
python tools/check-source-scope-correction.py --selftest
```

| Input | Resolved correction count | Exit | Observed result |
|---|---:|---:|---|
| Baseline `8606bad4cbc6451ac2890c9f8e2548a36c386db6` |0|1|7 findings, including **VALUE_DOMAIN_OVERCLAIM** and **COMMENT_ATTRIBUTION_OVERCLAIM** at preserved active loci, not merely missing successor files |
| Implementation `9dd82bceda4cf45c1e1e59e17c996ac898a5ecb7` |2|0|`status=PASS`, findings0 |
| Isolated selftest | — |0|`CHECK_SOURCE_SCOPE_CORRECTION_SELFTEST: PASS (15 cases, 15 passed, 0 failed)` |

Same evaluator SHA256 for both revision runs: `0771619dde7cc69fdb37538ad786f293b629f4062167a44a2d9cf4702ec6d428`. The counter evaluates resolved correction predicates and notice/history relations, not just JSON-object presence. Restored-domain and restored-attribution fixtures assert failed exit, exact expected finding-ID sets and count1. Missing notices require count0; moved notices and removed historical phrases fail. Invalid CLI separately returned exit2/E-CLI. Exact commands/stdout/stderr: `.ufo/waves/round-14/repair/verification.json`.

**Source agreement is separate from gate conformance:** the correction quotes are11 and16 words, match their reopened source locations, and all five supplemental body quotes match the canonical retained body and declared counts. The source's definition supports only the documented option domain; illustrative mechanism scope is labelled lane inference. The exact comment supports the observed account/body distinctions, not confirmed VM execution, generation method, host causality or maintainer acceptance. Evidence: `l1-source-review.json` and `integration-verification.json` source-agreement records.

Python aggregation over `git show <revision>:<path>` observed:0 removed/replaced historical lines across the ten changed historical text files; original r13 JSON object exactly preserved after removing its additive supersession key; all43 existing source rows unchanged; census, old checker, both outside verifier lessons and SHONEN bytes unchanged. The mention sweep has24 classified historical/supersession/rejection hits, no unmarked active copy of the two defects. Table blocks are consistent. Recorded credential-material, IPv4 and raw-journal-prefix scans have0 hits on their declared scope; this is not a full privacy audit. Evidence: `integration-verification.json`; equivalent frozen aggregation reproducers are in `count-commands.json`.

One capture error is retained: the first safety enumeration asked the implementation commit for `verification.json`, which was written afterward, and git correctly returned128. Only that enumeration's input scope was fixed; neither checker nor census was rerun. Static pre-execution integration also fixed a counter set-operation bug and a noun/verb self-description matcher, with a dedicated fifteenth fixture. No failed gate output was suppressed or rerolled.

| Axis | Author-side verdict | Boundary |
|---|---|---|
| depth | **improved** | Two source-grounded named corrections, red0→green2; ordinal8 unchanged |
| coverage | unchanged | Same rollback-net surface; no new held ground |
| operability | unchanged | Census bytes unchanged; no new demonstrated host capability |
| freshness | unchanged | Dated source reopens support this repair, not a broad live-state gain |
| calibration | unchanged | No score inflation, independent approval or promotion claimed |
| adjacency | unchanged | No ownership transfer or newly accepted handoff |

## Sources & frontier

Histogram aggregation selected registry lines matching `^\|\s*S\d{3,}\s*\|`, split the eleven cells, and counted tier column3/status column7 (zero-based). The executed Python aggregation is retained through its exact data/scope and equivalent replay form:

```sh
python -c "$(jq -r .registry_script .ufo/waves/round-14/repair/count-commands.json)" \
  8606bad4cbc6451ac2890c9f8e2548a36c386db6 \
  9dd82bceda4cf45c1e1e59e17c996ac898a5ecb7
```

| Measure | Before | After |
|---|---|---|
| rows |43|45|
| tiers |A36/B1/C6|A37/B1/C7|
| statuses |mined31/queued5/rejected7|mined32/queued5/rejected8|
| malformed |0|0|

Added tiers **A1/B0/C1**: S044 docs/A/mined, used-by the new correction; S045 community/C/rejected, superseding S042's teaching, also used-by the correction's source-curation record. Existing `status`/`recheck`/`used-by` changes: **none**. S001–S043 immutable fields and rows remain preserved; S041 remains mined. Source rows are curation, not expansion credit. Frontier ground advanced: **none**; historical issuer, operation, credentials and private namespace remain unknown, and boot-hook safety is unchanged.

Source URLs opened on2026-10-20:

- S044: https://man.archlinux.org/man/systemd.exec.5 — SANDBOXING > ProtectSystem=, footer systemd262.1: **“Takes a boolean argument or the special values "full" or "strict".”** (11 words).
- S045: https://api.github.com/repos/omacom/omarchy/issues/comments/6071740243 — body opening sentence: **“I tried this on a stock Omarchy worker VM and could not reproduce the central claim”** (16 words). L1 initially opened the exact API object; later unauthenticated requests were403 rate-limited. Authenticated read-only `gh api` and the canonical HTML comment independently supplied retained account/body witnesses; no token material or GitHub write is recorded. The first-person experiment remains unverified by this lane.

Required census command, executed at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi
```

Start — **exit0**:

```text
tsukuroi	W04	S038 duplicate url man.archlinux.org/man/access.2 across scopes
tsukuroi	W04	S041 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S042 duplicate url github.com/omacom/omarchy/issues/8047 across scopes
tsukuroi	W04	S043 duplicate url github.com/omacom/omarchy/issues/6629 across scopes
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
```

End — **exit0**, stderr empty:

```text
tsukuroi	W04	S038 duplicate url man.archlinux.org/man/access.2 across scopes
tsukuroi	W04	S041 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S042 duplicate url github.com/omacom/omarchy/issues/8047 across scopes
tsukuroi	W04	S043 duplicate url github.com/omacom/omarchy/issues/6629 across scopes
tsukuroi	W04	S044 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
```

W04s are disclosed scope-separated URL reuse, not a warning-free pass. Source records, quote locations, bounded searches, rejected propositions/flips and the four mined mistakes are in `corpus/lessons/round-14.md` §Gate/§Mistakes, `start.json` and `integration-verification.json`.

## Trend verdicts

- **expansion: unchanged** — repairs existing rollback-net knowledge; no uncovered coverage-map ground or new capability admitted. Row growth alone is not expansion.
- **quality: improved** — weaker source-inconsistent propositions are explicitly superseded by located, source-faithful corrections; stale metadata and overstated gate specification are marked and corrected. The bounded green counter is not treated as source truth.
- **discernment: improved** — the prior outside disagreement becomes grounded QUALITY19/20, named mistakes and corrections with actual red-before and restored-defect evidence. This is disagreement-learning, **not** a claim that a fresh outside reviewer has agreed with the new admission/rejection choices.

All verdicts are author-side, pending fresh independent hyaku closure. **Orchestrator action:** obtain a non-author admit/reject source spot-check before advancing this lane. Rounds12/13 remain rejected; this report does not waive the operator's third-consecutive-rejection block. No new L0 question or operator host-remediation request is opened by this source repair.

## SHONEN

- [~] Real decision tables, error patterns, checklists and citations: `SKILL.md` health table/update-safety checklist plus round14 correction routing and registered bounded checker; new knowledge pair and lesson Gate. Author-side only.
- [~] End-to-end domain work executed and logged: historical `corpus/knowledge/host-health-report-r3.md` and LOG round3; this round's source-repair trigger→correction→red/green→pushed-evidence outcome is in LOG round14 and `verification.json`. No new live-host task is claimed.
- [~] Instructions executable without oral context: gate CLI and isolated15-case selftest are demonstrated; whole-SKILL no-oral-context execution remains unverified (`corpus/knowledge/executor-test-sufficiency.md`, unchanged SHONEN box3).
- [~] No cross-domain bleed: `PROVINCE.md` round14 routing keeps OS diagnosis here; `SiblingConnector.md` records bounded sibling surfaces. No sibling method, remote VM verification or recipient acceptance is acquired.
