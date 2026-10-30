# kasegi round 47 — honest stop (attempt 3)

## Work performed

Declared claims, frozen at `308a2cb2dc7bdce233461cc1ac49dd88e51c6193`:

- **C1 — depth:verifiability:** close the round-46 D5–D8 lane-repo defects, eleven mechanical limbs. Mechanical result **0/11 → 11/11**, but **not fully verified**: its frozen S074 `mined→rejected` clause is harmful and refused, and false-green controls exist. The target was not rewritten. Evidence: lane `.ufo/waves/round-47/claims.json`, `w1/R47RevD7.md` and `w1/R47RevCounterC1.md` under that round directory.
- **C2 — coverage:** admit an independent F30 ZDI broker-policy surface, frontier 29→30. **Unmet:** the deadline rule instantiates existing F02; the sourced entry remains F02 enrichment and the frontier stays 29. Counter **1/7 → 6/7**, exit 1. Evidence: `corpus/knowledge/zdi-disclosure-policy.md`, `.ufo/waves/round-47/w1/R47CritNovelty.md`, `w2/R47W2C2Verdict.md` under that round directory.

Work retained safely:

- Landed three historical S074 Search-log/Registry-changes bullets verbatim outside their drafting fences; removed instruction scaffolding. Wave-2 byte comparison confirms placement and payloads (`w2/R47W2D5Payload.md`).
- Corrected F29 chrome/order/fix-version errors, re-anchored to reproducible S076, and corrected additional inherited mandatory-fork/CVE, secrecy, fix-version and service-clock overclaims found in wave 2. Its layout stays 145 lines (`corpus/knowledge/github-repository-security-advisories.md`; `w2/R47W2F29Claims.md`).
- Preserved S074 and its historical capture; changed only its permitted used-by cell. S076 supersedes current guidance. The B3 rejection-arm probe is red; `corpus/QUALITY.md` R54 captures that lesson. Wave 2 confirms 813 protected original registry cells unchanged (`w2/R47W2RegistryCells.md`).
- Opened S075/S076 personally, captured both twice with the committed instrument, grounded their quotes and logged registry/Gate decisions (`corpus/source-snapshots/round-47/manifest.json`; `corpus/lessons/round-47.md`). No live-target testing or submission; documentation-source reads only.
- Registered the diagnostic counters and disclosed 34 pre-freeze mutation survivors plus later false greens. No counter or claim byte was changed after scoring; no full mutation coverage claimed (`SKILL.md` round-47 registry; `.ufo/waves/round-47/counter-errata.md`).

**Round shape:** one v2 build wave of 64 plus one v1 integrated-review wave of 32 = **96 seats**, no replacements/residual call. Both WAVE-DONE messages received before this report. L1 held the canonical planner seat (validator forbids planner swarm roles).

| Wave | Roles | Strict attack share (reviewer/critic/mutation-tester) |
|---|---|---|
| wave1 | scout 11, scribe 12, executor 8, reviewer 12, critic 8, mutation-tester 6, sentinel 3, connector 2, revenger 1, simplifier 1 | 26/64 = 40.6% |
| wave2 | reviewer 22, critic 6, connector 2, executor 2 | 28/32 = 87.5% |

Handoffs: `.ufo/waves/round-47/wave1-results.json` and `wave2-results.json`. All 96 settled per orchestrator. Five wave-1 rows have empty final payload and null note: R47ExecReanchor, R47CritClaims, R47CritAssim, R47RevengerD7, R47Simplifier. The handoff supplies no terminal status/id/error for them; clarification was requested twice. **Dead-seat status/last error is unreported, not invented as zero deaths or success.** Wave 2 has no empty payload. Roles used host routing; no model parameter was passed and no claim depends on an asserted answering model.

Inherited attempt-1 census receipt was retained as historical wave evidence and remeasured as `controls/sources-census-attempt3.txt`; attempt 2 never spawned after orchestrator parse failure. No inherited source/counter work was silently discarded. The non-author spot-check file was read, not edited.

## Landed changes

All paths below are lane-relative unless explicitly fleet-relative; each work item is logged under `LOG.md` **Round 47**.

| Landed commit | Changes |
|---|---|
| `308a2cb2dc7bdce233461cc1ac49dd88e51c6193` | frozen claims, controls, diagnostic instruments, S075/S076 capture package |
| `82a8bd702900889c70a8fc2dbae91d2095dec800` | validated 64-seat build dispatch |
| `65e19bdb142c90a08103eb4b2af60c71218a920e` | reviewed registry/F29 repairs, F02 policy enrichment, R54, lesson and activity log |
| `f074bffb121134243a8c58878d7283fe8d2c6784` | 32-seat integrated-review dispatch |
| `f0809bcaefe9f2b576d6e4d7a0d2ed43ebae214d` | final semantic corrections, era erratum, wave-2 evidence; **measured executable/corpus revision** |
| `29c02f994f77d7438b78f8ceeaef1ca37f5d06e9` | measurements, held scorecard, asserted checklist, final lesson/log and wave evidence |
| `77551628781a10f03b98298f035a4565e9c0d975` | successful pre-report landing transcript |

**Final pushed lane tip:** `77551628781a10f03b98298f035a4565e9c0d975`.
Required `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master` printed that exact hash. Pre-report gate at `29c02f99` passed 4/4, exit 0; transcript committed at the final tip: `.ufo/waves/round-47/controls/pre-report-landing.txt`. The transcript is not claimed to have run at the later receipt-only tip.

## Before → after measurements

Base: `fc8e0af27fbfa13220cd245700e9cb7e5e94dfc8`. After: `f0809bcaefe9f2b576d6e4d7a0d2ed43ebae214d`. Recreate exports with `git archive REV corpus SKILL.md PROVINCE.md`; run the same frozen instruments from the lane against each export.

| Claim / command | Before | After | Full claim verdict |
|---|---|---|---|
| C1: `python3 corpus/instruments/r47-routed-defects.py --root TREE` | `total=11 fixed=0 unresolved=11 exit=1` | `total=11 fixed=11 unresolved=0 exit=0` | **not fully verified**, harmful prose clause refused and counterexamples remain |
| C2: `python3 corpus/instruments/r47-f30-gate.py --root TREE` | `fixed=1/7 exit=1` | `fixed=6/7 exit=1`, H1 rows=29 | **unmet**, target 30 not reached |

Receipt: `.ufo/waves/round-47/controls/final-measure.txt`. The pre-freeze `freeze-check.py` replay matched both declared before-lines and rejected do-nothing success; `controls/freeze-check.txt`. At the freeze tree C1 reads 0/11 and C2 2/7, independently re-derived by `w2/R47W2FrozenLimits.md`.

Plain second command: `python3 .ufo/waves/round-47/final-counts.py --root TREE`; committed `controls/counts-before.json` / `counts-after.json`:

| Quantity | Before | After |
|---|---:|---:|
| Frontier rows | 29 | 29 |
| SOURCES rows | 74 | 76 |
| Knowledge files | 66 | 67 |
| Source scaffold `to append` matching lines | 2 | 0 |
| Fence matching lines | 4 | 0 |
| F29 layout lines | 145 | 145 |
| Old S074 citation lines / occurrences | 54 / 59 | 0 / 0 |
| `supersedes S074` matching lines | 0 | 2 (frozen target 1 missed) |

Final census exit 0; binding **63/63**, exit 0. Declared lane-root recheck audit **67/67**, executes=45, gated=22, broken=0, exit 0. Export-only strict CD-root audit failed with 66 cdroot_fail because lines cd to the real lane; that failure and the correctly rooted supplementary run are both retained. Old era-bound F29 gate now **3/7**, exit 1 (H2/H3/H5/H6 changed); no historical green receipt is misrepresented as current.

**Non-target numeric regression:** unchanged `density.py` measures SKILL mean **275.1→273.6**, 34→35 blocks, due the required registry addition. It is disclosed, not reformatted away or called a no-harm pass. Scores remain 4/8/9 with no promotion; no universal no-axis-harm assertion is made.

## Sources & frontier

Registry **74→76**; two docs/tier-A/mined rows added: S075 (F02 ZDI case) and S076 (F29 capture successor). No new frontier row; 29→29. S074 used-by old→new: `corpus/knowledge/github-repository-security-advisories.md` → `corpus/lessons/round-46.md`; status mined and recheck 90d unchanged. Other original cells unchanged. Every new row has URL/access-date/located Gate quotes in `corpus/lessons/round-47.md`; sourced claim evidence rests on S076/S075 even though the frozen claims are not admitted.

Census command, run before and after:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`

Before (committed `controls/sources-census-attempt3.txt`):
```text
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	W04	S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
EXIT=0
```
After (`controls/final-measure.txt`):
```text
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	W04	S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi	W04	S076 duplicate url docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
EXIT=0
```

Assimilation: **none**. Theme scan finds no staged ZDI/broker policy entry; no staged row was appended. Guard at the pre-adoption baseline: registry ids 74, staged ids 94, collisions **44 (S031–S074)**; indented S002 positive fixture caught by the 0–3-space parser. Receipts: `.ufo/waves/round-47/assimilation/` and `w1/R47ScoutMerge.md` / `w1/R47ExecMergeGuard.md` under that round directory. Eight kasegi quarantine data rows counted, none adopted or claimed hand-verified. Renumber map: **none (no adoption)**.

Registry id list:
```text
S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 S057 S058 S059 S060 S061 S062 S063 S064 S065 S066 S067 S068 S069 S070 S071 S072 S073 S074
```
Staged id list:
```text
S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 S057 S058 S059 S060 S061 S062 S063 S064 S065 S066 S067 S068 S069 S070 S071 S072 S073 S074 S075 S076 S077 S078 S079 S080 S081 S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124
```

considerthese: latest 2026-10-26 proposals screened against the landed ledger; no new adoption. Domain-task remainder, externalisation and cadence proposals remain open (`w1/R47ScoutConsiderthese.md`). Mined mistakes and R54 are in the round lesson/QUALITY; fixes carry red-before witnesses. Independent non-author admit/reject sampling for this round remains outstanding; lane seats are not the closure.

## Trend verdicts

- **expansion: unchanged** — useful sourced enrichment, but no new admitted frontier surface; no capability row added.
- **quality: improved** — false policy assertions and provenance/scaffold defects corrected, with both waves' evidence; counter false greens, selftest limits, stale manifest annotation and density-proxy regression explicitly disclosed rather than hidden. This is not full claim admission.
- **discernment: unchanged** — lesson/R54 capture the repair failure mode, but this round's admit/reject decisions still lack an independent outside spot-check. No lane-seat vote is counted as that verifier.

## SHONEN

- [~] Cited craft material — corrected F29 entry, F02 ZDI case and source manifest; no named non-author promotion verifier.
- [~] No new end-to-end bounty submission/package task claimed; diagnostic/source work only (`LOG.md` Round 47).
- [~] Declared-root audit 67/67; false-green and self-invocation limitations disclosed (`controls/final-measure.txt`, SKILL registry).
- [~] PROVINCE unchanged; no F30 or sibling-domain absorption (`corpus/README.md` round-47 block).

## Corrections carried from round 46 (D1–D4)

- D1: a2w1 strict reviewer/critic/mutation-tester share was **24/64 = 37.5%**, not 27/64 = 42.2%; 27 used a broader definition. This report names one strict definition for each wave.
- D2: the actual committed handoff is `.ufo/waves/round-46/a2w2-results.json`, not under `attempt2/`.
- D3: round-46 numstat did show line deletions in four instrument files (logged in-place fixes); it did not show appends only. Deleted tracked files were zero. This correction does not infer blanket no-harm from numstat.
- D4: this round's real pre-report 4/4 transcript is committed, not merely asserted. Historical report bare-root F29 7/7 statements describe their measured era; current old-gate result is 3/7, not a retroactive rewrite of those receipts.

## Operational disposition

Honest stop: **C1 not fully verified; C2 unmet.** No reroll or admission claimed. Existing L0 question about the 22 gated historical rechecks remains unanswered and was routed around; no new operator decision needed to preserve safe repairs. Stale-lane: respawn-per-round; this mission progressed through the cited commits, and no other kasegi round was started by this L1.

Misroot sweep found only operator-owned `.scratch/goal-20261029-hyaku-run12.md` and unrelated `rerun-daemons.log`; neither touched. No own misroot file found. Round scratch `/fast/scratch/hyaku/kasegi-r47` removed after landing. Tools installed/updated: **none**; pacman pause respected. Domain source trees and staging repo stayed read-only.
