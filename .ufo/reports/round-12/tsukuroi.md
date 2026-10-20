# Tsukuroi — round 12 (2026-10-20)

## Work performed

Declared claims: **C1 — operability / capability acquisition:** make the census observe root-directory metadata independently of package ownership, retaining evidence through package-probe failures. **C2 — depth:** add an independently usable, sourced ordinary-mkdir indicator matrix distinguishing DAC/search, mount/namespace, credentials and collision. Depth 8 was tied lowest with adjacency 8, so C2 meets the lowest-axis duty. Neither claim asserts a repaired host or proven historical Btrfs cause.

- Implemented root mode/uid/gid and owner-bit observations in the packages line, preserving six plane names/order and the rollup. Missing/non-directory metadata fails closed; absent owner bits are **report-only**, not automatic degradation. Evidence: `tools/tsukuroi-census.sh`, lane `.ufo/waves/round-12/resumed/{after,selftest-after,live-after}.json`, LOG.md:428 and :475.
- Found the missing policy distinction: `/usr/lib/tmpfiles.d/root.conf` contains `z / 555 - - -`, shipped by systemd. Unowned by pacman does not mean policy-free. Rejected the proposed permanent 0555 DEGRADED rule and superseded conditional mode-repair advice. Evidence: SOURCES S039/S040; `resumed/ClaimCriticR.md`; appended errata in `corpus/knowledge/snapper-eacces-mechanism.md`.
- Corrected the matrix's fixture ownership, effective-versus-bounding capability claims, ProtectSystem=full scope, ENOENT handling and operation-order overreach. Four indicator families and ten documented scenarios are not four independent causes or ten executed host experiments. Evidence: `corpus/knowledge/root-dac-decision-r12.{md,json}`, `resumed/{MatrixR,MatrixCriticR,C2ReviewR}.md`.
- Converted the prior outside QUALITY-check disagreement into criteria #14–16 and mined policy/proxy/ordering/path-root/date mistakes. Gate quotes, rejections and mutable source transitions are recorded in `corpus/lessons/round-12.md`; all 16 applicable criteria are evaluated in the new note. Evidence: `resumed/admission-criterion-red-green.json`, `mode-policy-mutant.json`.
- Synchronized SKILL/registry, PROVINCE, README, SCORECARD and SHONEN without transferring sibling scope. No host repair, service action, package operation, boot or restore was performed. Tools installed/updated: **none**. Evidence: LOG.md round-12 entries and the bounded seat reports.

Paths abbreviated `resumed/` in this report mean lane-repo `.ufo/waves/round-12/resumed/`.

**Inheritance:** the previous headless attempt ended mid-wave; `resumed/dispatch-history.json` commits its launch/death digest. Reused the uncommitted QUALITY/SOURCES, matrix and lesson drafts plus first-wave observations after targeted rechecking. Discarded automatic mode-health grading, unknown-policy-origin, root-owned-temp-fixture, bounding-set-as-live-effective-set and universal errno-order premises. Removed duplicate resumed aliases and sanitized raw journal excerpts into dated aggregate findings. Two seat reports were misrooted in the fleet; copied byte-exact into this lane (SHA-256 prefixes `5093cc57` and `7acaf6dd`), then Main removed the fleet copies. The mistake and absolute-path correction are in the lesson. No outside/aggregator lesson was edited; the latest outside record was `round-1-verifier-spotcheck.md`, not a nonexistent round-11 spot-check.

**Wave evidence:** inherited validated 32-seat batch plus one new validated **32-seat** task call, unchanged validator taskCall, no model parameter. Each batch: 3 executor, 8 scout, 4 connector, 6 reviewer, 3 critic, 3 scribe, 2 revenger, 1 sentinel, 1 mutation-tester, 1 simplifier. L1 holds the canonical planner seat; revenger-routed Planner/PlannerR perform bounded data-walks. Registry/spec/dispatch are under `.ufo/waves/round-12/` and `resumed/`. Seats are author-side, not independent non-authors. Role routing was left to session configuration; provider identity was not independently audited.

## Landed changes

**Pushed lane HEAD: `670126f5161b824d9dabdfacd085d27ff0afa3e3`.** The lane push completed before this report was written.

| Commit | Changes and matching log |
|---|---|
| `70fede2a7a890cb50a72db2d4230ee541183bf7b` | Census implementation/selftest expectations; matrix and source registry; QUALITY/lesson; appended snapper corrections; SKILL/PROVINCE/README/SHONEN synchronization; inherited and resumed wave evidence. LOG.md:428, “round 12, resumed host-metadata and diagnostic-depth work”. |
| `670126f5161b824d9dabdfacd085d27ff0afa3e3` | Immutable-revision captures, source-resolving counters, fresh ordinary-mkdir controls, killed policy mutant, SCORECARD capability/claim rows and final lesson measurements. LOG.md:475, “round 12 post-integration measurement pin”. |

Census measured SHA-256: `d17d32a35946c71c1fc195e36178aa383f4a04d7172cc579b6e9e25fa537f27e`. The final three-line parent edit only aligned test regexes with the emitted root_euid field; earlier moving-review digests are not the measured revision.

## Before → after measurements

Baseline: `b76b5c377eaee3e3d8d47fdddde977828d05dbd5`. After: implementation commit `70fede2a7a890cb50a72db2d4230ee541183bf7b`; evidence and ordinal-score bookkeeping then landed at pushed HEAD above.

### C1 — operability / root-metadata-observer: improved, author-verified

Command: `bash tools/tsukuroi-census.sh`, then count packages-line sequences matching:

```text
root_status=ok root_mode=[0-7]{4} root_uid=\d+ root_gid=\d+ root_euid=\d+ root_owner_write=(?:present|absent) root_owner_search=(?:present|absent)
```

Exact combined reproducer: `resumed/count-commands.json` field `C1_command`; actual captures: `before.json` and `live-after.json`. This counter was applied to the recorded runs, not a second live rerun.

- Records **0 → 1**; presence predicate exits **1 → 0**. Census exits **1 → 1**: existing host findings remain DEGRADED, not suppressed.
- After root observation: `root_mode=0555 root_uid=0 root_gid=0 root_euid=1000 root_owner_write=absent root_owner_search=present root_src=default root_dir=/`.
- `bash tools/tsukuroi-census.sh --selftest` ran once after integration: **97 cases, 97 passed, 0 failed**, exit **0**. All **80** legacy case labels remain; **17** focused registrations were added. Two named skips: non-root-owned fixture requiring CAP_CHOWN, and EACCES/000-parent fixture with cleanup/root-bypass limitations. Skips are not passes.
- A sole automatic-DEGRADED assignment in an isolated policy mutant failed the same suite: **93 passed / 4 failed**, exit **1**, including stable finding `0555 owner-write absent is report-only (R12-C1)`. Shipping source was never mutated. Failure labels were on stderr; a capture assertion was corrected from retained output without rerunning the mutant. Evidence: `mode-policy-mutant.json`.
- Ordinal score **9 → 9 (delta 0)**; the demonstrated capability enters SCORECARD. No unsupported count-to-score conversion is claimed.

### C2 — depth: improved, author-verified

The source-resolving counting script is persisted in `resumed/count-commands.json` as `C2_script`. Reproduce for either revision:

```sh
python -c "$(jq -r .C2_script .ufo/waves/round-12/resumed/count-commands.json)" <revision>
```

It requires six nonempty branch fields and every source_id to resolve to a mined SOURCES row linked to the matrix. Observed outputs: baseline **0**, exit **0**; measured revision **4**, exit **0**. Ten scenarios are documented; all criteria **1–16** are explicitly evaluated. Source reopening and static reasoning, not field count alone, support the claim (`SourcesR.md`, `MatrixCriticR.md`).

Fresh isolated uid-1000-owned ordinary-mkdir controls: parent 0555/new target → **errno 13**; same parent/existing target → **errno 17**; caller-owned 0755/new target → **success** (`mkdir-controls.json`). Read-only-mount and effective-root-capability cases were **not experimentally run**. The matrix does not infer historical target state, unit-private mount state, live CapEff or a Btrfs ioctl cause from these controls.

Ordinal score **8 → 8 (delta 0)**: diagnostic depth improves without inventing a numeric scale. Other axes remain unchanged: coverage 9, freshness 9, calibration 9, adjacency 8. No measured code regression or scope harm was found; final admission remains for the independent closure session.

## Sources & frontier

Registry rows **34 committed baseline → 37 inherited at resumed start → 40 final**. Added over the baseline: **A +4, B +0, C +2**; the resumed attempt adds three A rows. Final histogram: **A35/B1/C4; mined30/queued5/rejected5**. Counting command (run against each revision's SOURCES bytes):

```sh
python -c 'import re; print(sum(bool(re.match(r"^\|\s*S\d{3,}\s*\|",l)) for l in open("corpus/SOURCES.md")))'
```

Counts and parser inputs are preserved in `resumed/{inheritance,after,count-commands}.json` and inherited `sources-before.json`.

Required validation command, run at resumed start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi
```

Start output, exit **0**:

```text
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
```

End output, exit **0** (`resumed/sources-after.json`):

```text
tsukuroi	W04	S038 duplicate url man.archlinux.org/man/access.2 across scopes
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
```

W04 is disclosed: S038 deliberately supersedes S034's overbroad access(2) teaching while preserving immutable history; it is not hidden as warning-free output.

- New rows: S035 mkdir docs/A; S036/S037 community/C rejections; S038 corrected access scope docs/A; S039 tmpfiles docs/A; S040 local packaged root policy own-work/A. The lesson Gate records URL/path, access date, located ≤25-word quote and decision for every new row.
- Mutable changes: S027/S028/S034 append the matrix to used-by; S035 queued→mined and used-by —→matrix; S039/S040 queued→mined and used-by —→matrix. S036/S037 remain rejected; recheck fields are unchanged. S038 was added mined. S038–S040 draft access dates were corrected by their author from copied campaign date to measured 2026-10-20 before landing; inherited opened dates were not rewritten.
- Frontier advanced: root metadata observation is now runnable; configured root-mode policy is located; #8047/#6629 leads were opened and rejected as host-cause support. Exact failing historical syscall/path, credentials, namespace and incident-time target state remain unknown. Mkinitcpio-v42 `/sysroot` hook compatibility remains an independent upgrade-safety blocker.
- Cross-domain evidence: reusable fixture craft remains tameshi's; fleet attribution remains mori's; no new recipient acknowledgement or ownership ruling is claimed. No L0 decision is required to finish this round; pre-existing contested RE ownership remains unchanged.

## Trend verdicts

All are author-assessed, pending independent hyaku closure; no scalar aggregate.

- **expansion: improved** — demonstrated `root-metadata-observer` repertoire entry, not a fabricated new coverage surface. SCORECARD capability row and measured live/selftest evidence.
- **quality: improved** — superseded policy-baseline, credential-proxy and errno-order shortcuts; source-supported matrix and 97/97 regression suite. No false 0755 policy or proven-host-cause claim remains in the admitted procedure.
- **discernment: improved** — prior outside admission disagreement became lesson-backed criteria #14–16; a known-policy false-positive design was rejected and its sole-delta mutant failed. A current-round independent admit/reject/source spot-check is still **owed**, not supplied by lane-dispatched reviewers.

**Stale-lane:** respawn-per-round; no other tsukuroi mission is open. Current launch `2026-10-20T00:41:10-03:00` was **1286 seconds** old at `2026-10-20T04:02:36Z` (timestamp subtraction), exceeding two 450-second ticks. It is **progressing**, not silent: lane-authored commits `70fede2`/`670126f` and the committed evidence were produced after launch. The predecessor ended with lane-dead-no-report; this report closes the inherited round, not a new round number.

## SHONEN

- [~] Decision tables, error patterns, checklists and citations — SKILL.md round-12 procedure/registry; `corpus/knowledge/root-dac-decision-r12.md`. Author evidence, no promotion verifier.
- [~] End-to-end domain task executed/logged — historical `host-health-report-r3.md`; current blind-spot trigger→read-only observation→verified evidence→operator handoff in LOG.md:428/:475 and this report. No host repair is claimed.
- [~] Instructions executable without oral context — matrix and selftest commands plus static `NoOralReviewR.md`; a fresh whole-SKILL no-oral-context execution remains unverified.
- [~] No cross-domain bleed — PROVINCE.md refinement and `OverlapHostR.md`/`OverlapMethodR.md`; census implementation stays here and reusable method authority is not absorbed.

Independent closure must sample at least one admit and one reject, reopen sources, and adjudicate the claims. No dispatched reviewer is presented as a non-author verifier.
