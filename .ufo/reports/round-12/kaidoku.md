# kaidoku — round 12 (steered; = arc3-loop1-round12, finished as frozen)

**Lane:** kaidoku-shokunin · **worktree** `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin` (branch `kaika/round`, base `de77d75`)
**Lane HEAD at report time:** `2a0d6c1` (records) — work `4072ebb`, fix `6a35398`; claims measured at `6a35398`, re-checked at `2a0d6c1`.
**Steer:** kaika steer table row `kaidoku | 12 | arc3-loop1-round12 halted with frozen claims | finish exactly as frozen`. Collision check at start: no `.ufo/reports/round-12/kaidoku.md` in the fleet root or the ledger worktree; lane `LOG.md` had no round-12 entry.
**Push:** none. The standing operator rule "No push" (orchestrator binding §6.6) overrides MISSION.md's commit-then-push; all three lane commits are committed only.

`R12` below = `.ufo/waves/arc3-loop1-round12` in the lane worktree.

## Work performed

Declared claims (frozen, `R12/claims-frozen.md:11-63`), three, causally separable:

- **C1 — coverage (owned):** close one corpus Unknown — `inspect_go_binary` as the fourth `ev_` Evidence-ID verb family.
- **C2 — depth (owned):** queue-drain rule #17 in `SKILL.md`.
- **C3 — operability (fleet):** citation-drift instrument grades the ungraded `recheck:` lines of the r7/r10/r11 `ev_` entries.

Campaign items (SOURCES, expansion, QUALITY rows) had no free slot: the frozen claims fill the 1–3 cap (§6.4 "a declared open round keeps its declared claims first"). The round's mistakes are still mined into a lesson (records, not a claim).

Work items:

- **L2 swarm — one batched `task` call, 10 members** (planner `R12Planner`, connector `R12Connector`, executors `R12ExecC1`/`R12ExecC2`/`R12ExecC3`, scribe `R12Scribe`, scout `R12Scout`, reviewer `R12Reviewer`, critic `R12Critic`, mutation-tester `R12Mutation`); every prompt led with `/skill:godspeed` + the verbatim `directive.md` bytes; no model passed; writers had disjoint file sets; no L2 committed. Two follow-up messages each to `R12ExecC3`/`R12Mutation` (resumes, no godspeed re-carry). Outputs: `R12/integration/` (c1, c2, c3, mutation, records-draft.md).
- **C1 entry landed:** `corpus/knowledge/2026-10-19-arc3-r12-go-evidence-id-domain.md` (from seat CR-4 per verdict VZ-1, `R12/claims/verdicts/VZ-1.md:26-30`), headers `source:` / `verified-at: 2026-10-19` / `recheck:` (expected id stated), no DRAFT header, OBSERVATION/INFERENCE/UNKNOWN labels; token on the Evidence-model row `corpus/README.md:41`. Evidence: fresh live rerun of `/usr/bin/docker` (sha256 `70f68a77…f45c9`) reproduced the stored same-path id `ev_87621921fc54a38ee60f85c9f81a47508dcdebd1c6f70569ec78da3a3a055dcd` twice, copies path-distinct (`R12/integration/c1/live-*.json`, `live-recompute.txt`); retained reconciliation `records=27 matched=27` over seven seat bundles (`R12/integration/c1/reconcile-all-go-ids.{mjs,txt}`); QUALITY check 15/15 criteria, 0/6 weak signals (`R12/integration/c1/quality-check.md`).
- **C2 rule landed:** `SKILL.md:293-314` — evidence-id field sensitivity is projection-local; isolate the field set, diff the residual projection when the mutation does not reproduce the alternate id. Cites only r7/r10/r11 corpus ranges (r11 narrowed `:19-23`→`:19` per critic: line 23 carries a stale "pending" clause). SHONEN box-1 count correction appended at `SHONEN.md:14`.
- **C3 rows landed:** three `exact` rows in `.ufo/gates/citation-drift/pointer-table.json:536-559`, pin `expected.json:12` = `7994eec7…`. **Deviation from VZ-1's pick, on measurement:** PL-4's substring needles killed 17/24 breaking mutants (`R12/integration/mutation/table1-rerun.md`); full-line pins killed all but false-alarmed on harmless rewording (mutation-tester + reviewer); landed form = order-free delimited-token lookaheads: 20/20 breaking text mutants (+6 positional) killed, 0/12 harmless false alarms (`R12/integration/mutation/lookahead-regex-check.{py,txt}`); seeds 3/3 caught, control clean (`R12/integration/c3/seeded-run-lookahead.txt`); selftest 13/13.
- **Harm caught before records:** `4072ebb` inserted a README lessons-index row and an inline SHONEN line, shifting pinned lines → strict probe `failed findings=5` (`R12/integration/probe-at-4072ebb.txt`); fix `6a35398` → `clean findings=0`.
- **Census measured on the right tree:** `c1-census-v10.py` defaults `--root` to the lane *main* checkout (`c1-census-v10.py:629`); figures here come from `git archive <rev>` trees with `--root` (PASS at `de77d75`, `6a35398`, `2a0d6c1`); correction appended in `R12/integration/measurements-6a35398.txt`.
- **Custody:** no pre-pair existed (live legs unpaired in r11 and r12); two post-only receipts `R12/receipts/config-post-only{,-2}.txt` bracket an operator-side `~/.bashrc` content change at 21:46:35Z, after the last live leg (21:33Z). No zero-drift claim. Selftest 28/28.
- **Lesson:** `corpus/lessons/round-12.md` — ten mistake classes with `## Gate`.

## Landed changes

| change | commit | LOG.md entry |
|---|---|---|
| C1 entry + README:41 token; C2 rule #17 + SHONEN correction; C3 rows + `expected.json` pin; integration evidence; post-only receipts; lesson | `4072ebb` | `LOG.md:1685-1714` (round-12 entry, bullets C1/C2/C3) |
| Fix: README lessons row removed, SHONEN correction moved to EOF; lesson row #9 | `6a35398` | same entry, "Harm caught and fixed" bullet |
| Records: SCORECARD round section (`SCORECARD.md:2029-2122`) incl. `Planned:` r13 + saturation note; LOG entry; lesson row #10; census SCOPE re-key `1759-2027`→`1759-2122` (`c1-census-v10.py:276`); measurements; retained mutation check | `2a0d6c1` | same entry (records this entry) |

All three commits by `kaidoku-shokunin <kaidoku@shokunin.local>`, pathspec-limited; credential sweep printed nothing each time; toplevel verified as the lane worktree before each commit.

## Before → after measurements

| claim | counting command | before (`de77d75`) | after (`6a35398`; same at `2a0d6c1`) |
|---|---|---|---|
| C1 coverage | command A (`SCORECARD.md:88-124`, `REV=<commit>`) | knowledge_files 90, mapped 90, missing [], dangling [] | **91, 91, [], []** |
| C2 depth | command A | rule_blocks 16, citation_resolved_rules 16 | **17, 17** |
| C3 operability | `git show <rev>:.ufo/gates/citation-drift/pointer-table.json \| python3 -c "import json,sys;t=json.load(sys.stdin);print(sum(1 for e in t['entries'] if e.get('file','').endswith('-evidence-id-domain.md') and e.get('must_match','').startswith('^recheck:')))"` | 0 (entries 57, sha `1b3ab955…`) | **3** (entries 60, sha `7994eec7…`) |

Instruments (harm check, all at `6a35398`; recorded in `R12/integration/measurements-6a35398.txt`): citation-drift strict `clean findings=0` at `de77d75` and `6a35398` (`failed findings=5` at `4072ebb`, fixed); census PASS 0/0/0/0 (archive tree, `--root`); citation-drift selftest 13/13; custody selftest 28/28; PROVINCE 162 lines. Calibration/freshness/adjacency: no claim, unchanged.

Per-axis self-verdicts (pending non-author verification): C1 coverage **improved**; C2 depth **improved**; C3 operability **improved**; no axis harmed at `6a35398` (the `4072ebb` probe harm was repaired before records).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — command A 17/17 at `6a35398`; correction `SHONEN.md:14`; no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round's live `inspect-go-binary` recheck `R12/integration/c1/live-*.json` (`LOG.md:1695-1699`); no non-author verifier.
- [~] Instructions executable by an agent without oral context — the entry's `recheck:` (`corpus/knowledge/2026-10-19-arc3-r12-go-evidence-id-domain.md:7`) was re-executed by an L2 from text alone; no non-author verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched (162 lines; census G21 14 rows clean); no non-author verifier.

## Sources & frontier

- `corpus/SOURCES.md`: absent → absent (`ls corpus/SOURCES.md` → no such file at `2a0d6c1`). Rows 0 → 0; no tier rows added or touched. Not claimed: the frozen claims fill the cap. Planned for r13 (`SCORECARD.md` `Planned:` line) with first leads from the connector scan: Ghidra GP-6528 / `GoRttiMapper.java` (Go 1.26 gate), RARE (arXiv 2607.12507), Decompile-Diverge (arXiv 2609.05370), V8-snapshot surface (Trail of Bits / CVE-2025-55305) — leads only, none opened this round.
- Frontier rows advanced: none (PROVINCE untouched). Corpus Unknowns: `inspect_go_binary` `ev_` domain closed; path-free `search_bytes` candidate remains open (VZ-1:32-34).

## Mistakes

Classes mined: 10 (`corpus/lessons/round-12.md` `## Mistakes`): 3-seed measurement overstating substring needles; over-tight full-line pins; live legs without custody pre-pair (r11, r12); seat computation cited without a retained script; stale status inside a cited range; dispatch counting (`CN-1`); digest without named serializer; frozen set vs active stagnation nudge; line-shifting insert into a pinned file (self-inflicted, fixed); census default root = main checkout. Criteria added to `corpus/QUALITY.md`: **0** (cap; #3 and #5 queued for r13 in `Planned:`).

## Trend verdicts

- **Expansion:** improved — corpus 90 → 91, fourth `ev_` family (command A at `6a35398`).
- **Quality:** improved — new entry passes 15/15 QUALITY criteria with a retained 27/27 receipt; C3 needles measured by mutation (17/24 → 20/20+6, 0/12 FA) instead of 3 seeds.
- **Discernment:** improved — the round refuted its own recommended candidate (PL-4) on measurement and caught two of its own instrument errors (pointer shift, census root) before records; evidence `corpus/lessons/round-12.md` #1, #2, #9, #10.

## L0 questions

- kaidoku | round-12 | The stagnation nudge (AXES.md:66-73) has applied since arc3 r10 (all owned proxies 10.0, no capability since arc2-r8); r12's frozen non-capability claims were finished as frozen per the steer. Confirm r13 should be the planned capability/frontier move (ARM64X via Ghidra + `corpus/SOURCES.md`), or rule otherwise.

## Integrator notes

- `c1-census-v10.py:629` hard-codes `--root /home/vgpnk/Projects/shokunin/kaidoku-shokunin`; any worktree run without `--root` grades the main checkout. Gate-owner fix needed (lane-owned instrument; not changed this round beyond the SCOPE re-key).
- `~/.bashrc` (custody path) changed content at 2026-10-19T21:46:35Z, after this lane's last live leg — `[INFERENCE]` the orchestrator's `cd`-alias repair; operator-owned, untouched by the lane.
- Fleet-root stray commits `c095ea1..b21278d` ("r12 base/after/after2/traced", author `r12 <r12@test>`) are not kaidoku's (no kaidoku L2 touched those files); the kaidoku mutation-tester used throwaway repos under `/var/tmp`.
- `CN-1` seat of the frozen 48 never reported (47/48).
- The lane's main checkout is not updated by this round (worktree branch `kaika/round` only).
- Stale-lane list: no kaidoku mission open longer than two driver ticks; this session progressed (three lane commits).
- Cross-domain evidence: none encountered.
