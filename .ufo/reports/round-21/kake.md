# Kake — round 21 (hyaku attempt 1)

## Work performed

Declared claims, following the SCORECARD planned row on the tied-lowest owned axes:

1. **C1 freshness:** make historical publishing provenance discoverable: complete provenance trios in the first eight lines **4/21 → 21/21**. This is metadata coverage, not live-property re-verification.
2. **C2 operability:** make historical decision records inspectable and runnable through a local structural gate: exact Gate headings in the fixed baseline lesson population **1/15 → 15/15**; the new round-21 lesson brings the current total to **16/16**.

- Added seventeen pure four-line knowledge prefixes and fourteen EOF lesson-gate reconstructions. Original corpus bytes survive; unknown historical decisions remain unknown. Evidence: `kake-shokunin/corpus/lessons/round-21.md`, `.ufo/waves/round-21/initial.json`, and the byte-preservation audit.
- Added `scripts/corpus-contract.mjs`, registered in `SKILL.md`'s appended gate table, plus revision-bound counting, digest-first frozen replay and pointer-mapping evidence tools. S019 scopes this to local corpus structure, not platform semantics.
- Carried the round-20 outside review forward without editing its protected file; retained its citation/confinement bounds and clarified named-function/static-scanner limits in QUALITY. Evidence: `corpus/lessons/round-20-verifier-spotcheck.md`, round-21 lesson and `w1/Round20Debt.md`.
- Rejected a concrete draft claiming nonexistent `corpus/CORPUS.md` registration; corrected the new metadata references to S019. Rejected retrospective admission of the already-disproved orphan-impossibility premise. Evidence: `w1/MetadataSafety.md`, `w1/GateTruth.md`, round-7 reconstructed Gate and round-21 integration rulings.
- Dispatched **one validated 64-seat build wave**, using unchanged validator taskCall. Role mix: **36 scribe, 3 executor, 6 scout, 3 connector, 8 reviewer, 5 critic, 3 sentinel**. L1 holds the canonical planner seat; validator excludes planner as a swarm role. All 64 reports are inside the lane. Evidence: `.ufo/waves/round-21/{wave1-spec,wave1-validation,wave1-dispatch-result}.json` and `w1/swarm-registry.json`.
- **Operator wrap-up superseded the planned falsification wave:** no wave 2, new seat or worker was dispatched after that directive. Total dispatched: **64**. Author-side reviews are not independent closure verification.
- Mandatory fleet misroot sweep found four owned reports (Knowledge08, Lesson09, Lesson14, Population): copied byte-exact into the lane, `cmp` exit 0 for each, then removed only their fleet copies. Other-lane/orchestrator files were untouched. Evidence: `.ufo/waves/round-21/misroot-sweep.json`; mistake recorded in the lesson.
- Publishing/deploys/submissions remain operator-owned. No domain source tree was edited or pushed; no domain-facing action was taken. Cross-domain boundaries: protocol owns the shared contract, kagi owns credentials, tabi owns browser operation. This round owns only kake's corpus maintenance.

Stale-lane: respawn-per-round driver; this assignment opens no other kake mission. No next round was started.
Tool installs/updates: **none**, including all seats; pacman pause respected.
Inherited lane working tree at start: clean. The protected round-20 verifier lesson was read and left unchanged. Lane status was clean again after the final push and before this report was written.

## Landed changes

**Pushed lane HEAD: `c2d8da86d05f14e9d4c449a51911091bda7fc33b`.**

| Commit | Landed work | LOG linkage |
|---|---|---|
| `df6196b022a7fe9ac9a88af1293dc377a8197652` | Metadata prefixes, retrospective Gates, structural gate and registry, S019, QUALITY/README updates, frozen baseline and author-wave artifacts | `LOG.md:670–701`, round-21 entry |
| `c2d8da86d05f14e9d4c449a51911091bda7fc33b` | Full measurement receipts, SCORECARD verdicts, lesson correction register, recovered four misroot reports and final sentinel report; anchor-helper stdout-flush repair | `LOG.md:703–731`, same-round measured closure |

Both lane commits carry `kake-shokunin <kake@shokunin.local>`. Push succeeded to the lane's existing remote before this report was written. No report or fleet commit swept another lane's work.

## Before → after measurements

Baseline: **`5009ecaa1cce10b895617a585ddd3f7c7c923a84`**.
Measured source revision: **`df6196b022a7fe9ac9a88af1293dc377a8197652`**.
The final evidence commit appends bookkeeping and fixes the audit helper's output flush; it does not change the measured corpus gate or claim populations.

```sh
node .ufo/waves/round-21/measure.mjs --revision 5009ecaa1cce10b895617a585ddd3f7c7c923a84
node .ufo/waves/round-21/measure.mjs --revision df6196b022a7fe9ac9a88af1293dc377a8197652
```

| Claim | Before | After | Verdict |
|---|---|---|---|
| C1, complete exact-lowercase provenance trios | 4/21 | 21/21 | **improved, bounded; freshness HOLD 10** |
| C2, fixed fifteen baseline lane lessons | 1/15 | 15/15 | **improved, bounded; operability HOLD 10** |
| New round-21 lesson, separately named | absent | Gate present; full current total 16/16 | not substituted into the legacy denominator |

Counter exits: **1 → 0**. Full argv/stdout/stderr/revision receipts: `.ufo/waves/round-21/{measure-before,measure-after}.json`. The baseline lesson allowlist excludes all aggregator/verifier/operator artifacts and includes round-19-recensus. The original planned shell pipeline was replaced because it leaked the protected verifier file and hid denominator growth.

Exercised checks:

- `node scripts/corpus-contract.mjs --selftest`: **7/7, exit 0** (`corpus-selftest.json`).
- `node scripts/corpus-contract.mjs --json`: **exit 0**, 21 knowledge entries, 16 lane lessons, zero findings/errors (`corpus-after.json`). The structural matcher is more permissive than the exact-lowercase independent counter; both agree on complete-trio counts. Neither verifies date/source truth.
- `node .ufo/waves/round-21/replay-proof.mjs`: **PASS**, 36 pinned inputs, two stable expected-red runs, zero failures; **exit 0** (`replay.json`). Frozen inputs stayed unchanged; missing-metadata findings cover 17 files, missing-Gate findings cover 14.
- Gate digest: `ca6f685e0b826a40894990b4f536d272ba3e948444e7ab74fb41602bbdf0ed29`, persisted with measured revision in `gate-digest.json`.
- Existing paths gate: `node scripts/freshness-sweep.mjs --offline --section=paths --json` remains **exit 1**, three drift targets/four old locations, **newMissing 0**, missSet **55**. No pin was weakened or expanded (`paths-after.json`). Offline/skipped publishing checks are not passes; no current web readiness is claimed.
- Broad anchor census: **zero prior-byte violations**, seventeen prefixes and fourteen EOF additions. It reports 3,294 references, 2,051 moved references and **78 baseline-inapplicable diagnostics**, entirely in author wave reports (73 pointers into new suffix lines, five into the new round-21 lesson). **Exit 1 is retained**, not reported as an all-reference pass. The round lesson supplies the per-file +4 correction register for existing knowledge pointers. The initial large JSON was truncated by immediate process.exit; exitCode fixed flushing, and both receipts remain (`anchors.json`, `anchors-fixed.json`).

Limits: the structural gate skips symlink/nonregular entries and role-excluded names, permits an empty corpus, and does not prove metadata honesty or exhaustive write confinement. The separate fixed-population counter supplies this round's inventory evidence. These limits are recorded in SCORECARD and `w1/Confinement.md`, not hidden behind green selftests.

## Sources & frontier

Validation command, run at start and after integration:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Before output and exit:

```text
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit 0
```

After output and exit: identical, **exit 0**. Receipts: `.ufo/waves/round-21/census-before.txt`, `census-after.json`.

Rows **18→19**; tiers **A16→17, C2→2**; statuses **mined14→15, queued2→2, rejected2→2**. Exact pasteable table-count commands and outputs are in `source-rows-before.json` and `source-rows-after.json`; the former binds to baseline 5009ecaa, the latter to the integrated table.

- Added **S019**, tier-A scoped own-work corpus audit. Canonical input opened this round: kimi-shokunin `skills/shokunin/protocol/CORPUS.md`, commit `e737d2ea97f6b0198503e077676c3f2ea07974a9`, access 2026-10-20. Short located quotes, file URI and input digest appear in the round lesson's Gate/integration rulings. The local gate source was read and exercised this round.
- S019 supports metadata/Gate discoverability only; each historical entry retains its own domain evidence and date. No platform mechanism is inferred from a format source.
- Existing rows touched old→new: **none** for status, recheck or used-by. S019 is newly added, not a promotion of an old source tier.
- Frontier ground advanced: **none**; no new domain knowledge entry or capabilities-table credit. Rejections and mistakes are recorded in `corpus/lessons/round-21.md`, including draft false-path attribution, broadened path debt repaired without repinning, misrooting and helper output loss.

## Trend verdicts

- **expansion: unchanged** — the same twenty-one domain entries; no new coverage-map ground or capability row admitted. The new audit source is maintenance, not domain expansion.
- **quality: improved** — bounded to recoverable provenance, explicit historical decision records and runnable rejection of missing fields/Gates. Pure-byte preservation, frozen red-before demonstration and the preserved known-red paths verdict support this; not live-property freshness.
- **discernment: unchanged** — the round's reviews are author-side. A separately orchestrator-dispatched non-author must sample an admit and reject and adjudicate admission. Prior round-20 independent agreement is carried forward, not reused as round-21 outside verification.

New L0 questions: none. Inherited operator restore-or-retire decisions remain open. Orchestrator actions: independently close/spot-check round 21; retain the operator wrap-up exception for skipped wave 2; decide future domain restoration/publishing separately. This report does not self-admit the round.

## SHONEN

- [~] Real decision tables, error patterns, checklists and cited sources: `SKILL.md`, `corpus/QUALITY.md`, S019 and the corpus gate registry. Author assertion only.
- [~] End-to-end local corpus repair prepared, verified and handed off: `LOG.md:670–731`, frozen replay and this pushed report; no domain publish claimed.
- [~] Instructions executable without oral context on the exercised local surface: revision-bound counter, gate selftest and frozen replay receipts; missing external substrate remains explicit debt.
- [~] No cross-domain bleed on this round's scope: `PROVINCE.md`, source boundaries above and untouched domain source trees. No non-author promotion check is claimed.
