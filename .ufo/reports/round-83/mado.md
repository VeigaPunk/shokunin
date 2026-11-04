# mado round 83 — second-surface allocation and tray state

## Work performed

Declared claims: **C1 coverage**, allocation-map resolution for a second declared layer surface; **C2 operability**, executable tray item-count and host-registered rows. **Honest stop, not round admission.** Final finite counters are green, but the frozen C1 target missed its mutation population and independent attacks expose stronger causal/producer-status claims the fixtures do not certify.

- Generalized `tools/mado-barfoot.py` allocation resolution before exclusive-pass ordering. Six new surface cases cover top/bottom/left placement, explicit zones, zero allocation and two namespaces; five additional cases exercise prior gaps. Evidence: `quality/counters/c1-r83-surface-band.py`, `.ufo/waves/round-83/controls/c1-cases-r83.json`.
- Added two executable runbook rows, a boolean-property matcher, 31 case bindings and 27 matcher mutations. Retained carried cases except a disclosed fixture-PID supersession. Evidence: `SKILL.md:231`, `quality/counters/c2-r83-runbook.py`, round83 C2 controls.
- Opened systemd busctl and Waybar SNI-host sources; added S484/S485 and a bounded knowledge entry. Evidence: `corpus/lessons/round-83.md` Gate, `corpus/knowledge/bar-footprint-surface-band-r83.md`, round83 `fetch/`.
- Integrated settled attacks rather than declaring the green counters sufficient. Evidence: `.ufo/waves/round-83/w1-results.json` and seven seat reports under `w1/`.
- Corrected forward the C1 mutation constant, C2 diagnostic verdict (`MUTANTS_SKIPPED` rather than a full target claim), and two session identifiers in a new negative fixture. These amendments do not retroactively admit the frozen claims. Evidence: `measurement-c1-r83-freeze.txt`, `final-c1-r83.txt`, `final-c2-r83.txt`.

## Landed changes

Lane final **bc48e8035cf93019937d955031a6deeac4bb59ab**; `git -C mado-shokunin ls-remote origin refs/heads/master` printed that exact hash before this report. All work maps to `LOG.md` Round83 and `SCORECARD.md` Round83.

| Commit | Landed work / LOG linkage |
|---|---|
| 4e48d8e75da2703a391c1ded0675633dfb599f55 | First instrument/control declaration; LOG instruments bullet |
| 4208c24ae741d10df15afffcd6612d7ee686171e | Preserve carried assign branch and declare supersession fields; LOG red-measurement repair history |
| aeeb5e54fb231758ea77ba930cefcd2ce34e1c9f | Add mismatch-reader cases and repair mutation anchors; same LOG history |
| dbc09269fe547ab13541e722dd7d2ba33015f348 | Consolidated band resolution and final pre-wave instruments; frozen receipt revision |
| 5ceb187f9494e22a9cf23ccc34c3f5ef90d9eafa | Settled attack integration, bounded entry, QUALITY137, lesson, source registry, scorecard and successor bookkeeping/diagnostic corrections |
| bc48e8035cf93019937d955031a6deeac4bb59ab | Final measurement/census/index/ledger/axis/gate receipts |

**Wave:** ONE validated v1 wave, 10 seats: scout1, connector1, executor3, scribe1, reviewer1, critic1, mutation-tester1, sentinel1. L1 holds planner seat (validator excludes planner). Attack share 4/10. No residual calls. Main delivered WAVE-DONE before this report; actual handoff is `w1-results.json`. Seven nonempty outputs; scout, connector and entry scribe settled empty (3 evidence gaps, no provider error text supplied). No replacement seats. L1 authored the bounded entry; no outside non-author approval is claimed. The empty connector means sibling-overlap review was not delivered, so scope is kept at the existing layer/tray province boundary.

**Attack integration:** ReviewerC1's non-bar live-box substitution, extra positive-band override and explicit-zone override survive 58/58. MutationTester confirms precedence and finds boolean-padding/later-array-element gaps. ExecC2Live demonstrates that a producer emitting plausible text then failing can yield a matching count through the pipeline. These are retained as counter/interpretation limits, not concealed or renamed passes. Critic's diagnostic-target defect is repaired forward. Privacy sentinel found local account/path disclosure, not credentials; required absolute machine handoff paths remain. Historical commits are not rewritten.

## Before → after measurements

Measurements below are **re-executed this round**, not relayed. All final receipts measured content commit **5ceb187f9494e22a9cf23ccc34c3f5ef90d9eafa**; final commit adds receipts only.

### C1 coverage

Command (lane cwd; replace DIR with private `/fast/scratch/hyaku/mado-r83/...`):

```sh
python3 -I quality/counters/c1-r83-surface-band.py --repo . --rev 5ceb187f9494e22a9cf23ccc34c3f5ef90d9eafa --base-rev 67dd2b667b72f7f72309340d488b355d543841a5 --controls .ufo/waves/round-83/controls/c1-cases-r83.json --carried .ufo/waves/round-82/controls/c1-cases-r82.json --scratch-root DIR
```

Held tool **52/58 → candidate 58/58**, carried47/47, selftest136/136, actual mutant kills39/39, successor TARGET_MET exit0 (`receipts/final-c1-r83.txt`). Frozen dbc09269 counter declared38 mutants, observed39 kills and correctly printed TARGET_MISSED exit1 (`measurement-c1-r83-freeze.txt`). This mismatch was corrected after scoring, so the **frozen claim remains missed**. Independent causal survivors additionally prevent stronger certification. No numeric expertise score awarded.

### C2 operability

```sh
python3 -I quality/counters/c2-r83-runbook.py --repo . --rev 5ceb187f9494e22a9cf23ccc34c3f5ef90d9eafa --controls .ufo/waves/round-83/controls/c2-runbook-cases-r83.json --carried .ufo/waves/round-82/controls/c2-runbook-cases-r82.json --scratch-root DIR
```

**29→31 rows**, executed31 matched31, shape26/26, anchors31/31, rows31/31, mutants27 killed27, tree=bound, TARGET_MET exit0 (`receipts/final-c2-r83.txt`). Held r82 instrument stops with `the runbook section carries 0 command rows, frozen target expects 29`, exit2 (`control-c2-r82-at-r83.txt`). That section-refusal control cannot by itself prove semantic improvement. Finite predicate met; **producer-success interpretation unprovable**, because the count pipeline masks failures. No full operability admission claimed.

**Harm watch, re-executed:** index102/102; ledger152/152 uncovered0; axis checked3 mismatched0; hermetic gate460/460. Each exit0, at content revision above: `receipts/final-{index,ledger,axis,gate}-r83.txt`. Tool hash is SHA-256 `8b17706014e6708a11413f0bd6c3398ca4e1b95b40b9c2d51f80f5064c677207`, not a Git blob id. No desktop state changed.

## Sources & frontier

Registry **418→420**, two tier-A mined rows, no existing status/recheck/used-by edits. Counting command over each committed revision:

```sh
 git show REV:corpus/SOURCES.md | python3 -c 'import sys,re; print(sum(bool(re.match(r"^ {0,3}\|\s*S[0-9]{3,}\s*\|",s)) for s in sys.stdin))'
```

Base67dd2b6 prints418; content5ceb187f prints420. New S484 busctl formatting and S485 Waybar host registration were opened before registration. Gate quotes/access date/locators are in `corpus/lessons/round-83.md`; C2 cites S484 and held S482. New entry indexes bounded observations and explicitly refuses causal admission. Frontier exploration advanced; no core-completion claim.

Census command at start/end: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` — initial invocation exit0; final exit0. Unfiltered durable receipts: `census-start-r83.txt` (base registry/corpus reconstructed; non-corpus used-by dependencies linked to lane tree) and `final-census-r83.txt` (literal root command). The first reconstruction omitted those dependencies and exited1; it was not called a conformant start receipt. Warning set includes W04 scoped duplicate URLs and W01 S277, not only W04.

Assimilation: none. `considerthese/2026-11-04.md` proposal7 used for explicit re-executed versus evidence-verified labelling. Round82 D1 receipt pointer corrected append-only; D2 7ok/7defect, D3 warning set, D4/D5 set_size/configure span distinction, D6 actual wave results, D7/D8 revision/hash units, D9 three refusals among eight new cases, D10 row-specific Gate quotes are recorded in the lesson. S481's immutable loose anchor remains routed, not silently rewritten. Prior report facts here are evidence-verified from the outside spot-check, not re-executed.

## Trend verdicts

- **expansion: unchanged** for admission — explored new finite surface ground, but extra-surface source causality is not certified; no capability admitted from C1.
- **quality: improved** in bounded evidence handling: mutation-count defect is red-before/green-after, QUALITY137 grounded; frozen failures and successful semantic cheats remain disclosed. This is not a claim that stronger predicates passed.
- **discernment: unchanged** — lane attacks rejected overstrong interpretations, but outside-lane admit/reject spot-check remains pending.

## SHONEN

- [~] Real tables/patterns/checklists: `SKILL.md:231`, bounded surface-band entry; no promotion verifier.
- [~] End-to-end model/runbook execution: LOG Round83 and `final-c1-r83.txt` / `final-c2-r83.txt`; not full desktop behavior.
- [~] Executable instructions: declaration commands and seven nonempty seat outputs; three empty seats disclosed.
- [~] Province boundary retained: read-only layer/tray work; PROVINCE owns these surfaces; sibling scan seat empty, no outside approval.

Stale-lane: only this round open, progressing via landed commits; no separate mission opened. Misroot sweep: `receipts/misroot-r83.txt`; orchestrator `.scratch` and unattributed `after` left untouched. Existing operator questions (host recovery/pacman and historical session-material history) remain operator-owned; no new L0 request. Tools installed: none. Scratch cleaned after landing.

Self-evaluation: accuracy3 (stronger causal predicates unresolved), completeness3 (three empty seats and frozen honest-stop), clarity4 (separate frozen/successor verdicts), actionability4 (exact receipts/commands), conciseness3 (amendment history retained). Mean3.4; no self-rating substitutes for closure. Highest-impact improvement: a pre-scoring mutation-population assertion and an extra-surface disagreement case before the next freeze.
