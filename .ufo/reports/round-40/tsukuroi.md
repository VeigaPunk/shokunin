# tsukuroi — round 40 report (hyaku run 8, attempt 1)

L1: `TsukuroiR40`. Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, base
`53b294a274656be6479aadf2ec2fee890ded77ce`, final lane hash `0e5805a1f149bd2ed9fe0db2e0a832afb034a835` (branch `master`, pushed; `git ls-remote
origin refs/heads/master` prints it). Round shape: **one v2 wave of 65 seats** (policy
`scripts/hyaku/ufo-wave-policy-v2.json`, band 64–128), no residual call; round total 65. Earlier attempts: none (the
watchdog log holds no `lane-dead-no-report tsukuroi round=40` line); the lane was clean at start
(`jj-lane.sh state`: `ahead=0 behind=0 tracked=0 untracked=0`).

## Work performed

Declared claims (`SCORECARD.md` "Round 40 — declaration", commit `758a4b08`; counters frozen at `a447b67b`):
- **C1 — operability**: the census `--selftest` gains varied mount-table cases so nine literal-keyed and guard mutants
  of the round-39 STORAGE cross-check fail it (routed R39-FIXTURE-MONOCULTURE).
- **C2 — depth (sourced, S219–S225)**: `corpus/knowledge/pacman-exec-environment-r40.md`, what a libalpm hook command
  or install scriptlet finds when it starts (EX1–EX8, pacman 54d9411 as built by Arch 7.1.0.r9.g54d9411-3), measured
  by a counter that reads the rule cell (routed R39-CONTENT-UNREAD).

Work items:
- Protocol load: MISSION.md, AXES.md, CORPUS.md (SOURCES contract), the run-8 goal file, the round-39 lesson and
  verifier spot-check (`corpus/lessons/round-39-verifier-spotcheck.md` §6, seven routed defects), QUALITY 64–87,
  `considerthese/2026-10-25.md`.
- Sources opened this round: pacman `meson_options.txt`, `util.c`, `trans.c`, `hook.c`, `alpm-hooks.5.asciidoc` at
  54d9411 and the Arch `PKGBUILD` at tag `7.1.0.r9.g54d9411-3`, snapshotted with digests in
  `.ufo/waves/round-40/frozen/src/SHA256SUMS`; a read-only host capture `.ufo/waves/round-40/frozen/hostcap/`
  (MANIFEST sha256 `57888c10…`: libalpm strings `/usr/bin/bash` at index 1277, 14 of 69 effective hooks carry
  `NeedsTargets`).
- Freeze commit `a447b67b`: `tools/score-selftest-literals-r40.py` (sha256 `8b06de18…`), `tools/check-exec-environment-r40.py`
  (sha256 `d4a2bb94…`), the snapshots, the capture and their two `SKILL.md` registry rows (QUALITY 70).
- Pre-data controls, scored with the frozen counters before any seat (`.ufo/waves/round-40/controls/controls.jsonl`,
  script `run_controls.py`): C2 do-nothing, X-empty, X-false by negation, X-false by values, own-work only, held rows,
  quote-as-rule writer and duplicated block all FAIL; C1 do-nothing (survivors 9), one-literal fixtures (survivors 9),
  self-reading selftest and arm-rewritten all FAIL; both candidates PASS. Recorded limit: the self-reading control
  failed its own baseline (`baseline_pass 0`), so it did not isolate the selfref guard (lesson R40-CONTROL-OWN-BASELINE).
- C1 implementation `c707e356`: five selftest cases in `run_selftest` (device, mountpoint, options, subvolume, position,
  fstype case, unlistable root with btrfs mounted); `probe_storage_arm` byte-identical to the base
  (`w1/C1CritControl.md` §1, arm sha256 `71e6007e…` at base and tip).
- C2 implementation `bf238050`: the entry and registry rows S219–S225.
- Wave `w1` (65 seats) attacked and verified both claims, re-opened every new source, drafted the routed corrections,
  the SKILL/README sections, the lineage table, the Gate rows and the mistakes sweep (reports
  `.ufo/waves/round-40/w1/*.md`).
- Integration `aad01138`: EX4/EX5/EX7/EX8 corrections appended to the entry plus a `## QUALITY check` (QUALITY 14);
  S226 (alpm-hooks.5 CAVEATS) and S208/S209 used-by additions; SKILL sections "Storage arm selftest literal variation —
  round 40", "Hook and scriptlet execution environment — round 40", "Counter lineage — rounds 35-40"; README coverage
  row and frontier notice; QUALITY 88; the round-40 lesson; the round-39 corrections (LOG erratum for future-dated
  headings, SCORECARD gates-row disclosure and receipt-provenance scoping).
- Outcome `e3bc9340`: SCORECARD measured outcome, axes table (self-assessment 27 checks, 0 mismatches,
  `after/self-assessment-final.jsonl`), capabilities, planned row; LOG entry; packaging-patch note on the entry.
- Final receipts `d84e2aab`: sources census END exit 0, C2 at `e3bc934` PASS.

## Landed changes

LOG.md entry: "Round 40 — hyaku run 8 (stamp: the commit that lands this entry)" (`LOG.md`, commit `e3bc9340`), plus
the erratum "Round 40 — erratum: heading stamps later than their commits" (commit `aad01138`).

| Commit | What |
|---|---|
| `a447b67b2502bae1e96fda341ae5ad32243ae524` | freeze: two counters, pinned sources, host capture, registry rows, start census receipt |
| `758a4b08c6ea259a033f071fc864b544511fb172` | declaration and pre-data controls |
| `c707e356c2911646f7304d706eb77d118e510610` | C1: census selftest varies mount-table literals |
| `bf2380503b8e4a5d33162026854b0b7b66d18b86` | C2: entry EX1–EX8, S219–S225 |
| `f951f288483c1af0cef4afd458488b84cf7a2165` | before/after receipts, assimilation checks, wave generator |
| `aad01138d544878a64ff97927708c94a79432a3a` | integration of the wave findings (see Work performed) |
| `e3bc9340ae015c286cfc7c79eca61747c31d7b0b` | measured outcome, self-assessment table, LOG entry |
| `d84e2aab555557606b2cf5a999929be45f1d4f44` | final self-assessment, sources census and C2 receipts |
| `6c20e44bded93777592230449e2b921c3e40a62a` | wave results file (`w1-results.json`, 65 seats) and the three late seat reports |
| `0e5805a1f149bd2ed9fe0db2e0a832afb034a835` | wave generator as dispatched (65 items) |

## Before → after measurements

| Claim | Counting command | Before (base `53b294a2`) | After | Measured against | Verdict |
|---|---|---|---|---|---|
| C1 operability | `python3 tools/score-selftest-literals-r40.py --revision <REV> --scratch <DIR>`; predicate `baseline_pass == 1 and neutral_pass == 3 and mutants_applied == 9 and survivors == 0 and selfref == 5` | survivors 9, FAIL exit 1 (`.ufo/waves/round-40/before/c1-before.jsonl`) | survivors 0, baseline PASS 124/124, neutral 3/3, applied 9/9, selfref 5, PASS exit 0 | `c707e356` (`after/c1-after-c707e35.jsonl`) and `aad01138` (`after/c1-final-aad0113.jsonl`) | **verified under the frozen predicate**; counter sufficiency falsified by a self-reading prologue (`declare -f`, `${0}`, `${BASH_ARGV0}`) that passes with no fixture (`w1/C1CritControl.md`); held-out H5/H6/H9 survive but key on properties every kernel btrfs line has (`w1/C1HeldOutMutants.md`) |
| C2 depth | `python3 tools/check-exec-environment-r40.py --revision <REV>`; predicate `rules_verified == 8 and duplicate_rows == 0 and duplicate_headings == 0 and source_ok == 1 and counts_ok == 2 and novelty_base_hits == 0` | entry absent, rules 0, FAIL exit 1 (`before/c2-before.jsonl`) | rules 8, source_ok 1, counts_ok 2, novelty 0, PASS exit 0 | `bf238050` (`after/c2-after-bf23805.jsonl`), `aad01138` (`after/c2-final-aad0113.jsonl`), `e3bc9340` (`after/c2-final-e3bc934.jsonl`) | **predicate met; the counter's content check is falsified** — a token-list writer and non-negated false rules pass it (`w1/C2CritControl.md`, `w1/C2CritXFalse.md`). Content per row: EX1, EX2, EX3, EX6 hold; EX4, EX5, EX7, EX8 partly, corrected append-only (EX5's "/tmp is a tmpfs" host sentence was false and is withdrawn); 0 rows `fails`, so the kill rule did not fire |

No-harm: seven lane gates exit 0 at `aad01138` (`after/gate-*-aad0113.jsonl`); round-39 C2 counter exit 0
(`after/r39-c2-aad0113.jsonl`); round-39 C1 counter PASS at the dispatch tip (`w1/C1ExecR39Counters.md`; census bytes
unchanged since); additions only across the round (`w1/RevNoHarmAxes.md`); self-assessment 27/0 at `e3bc9340`
(`after/self-assessment-final.jsonl`). Causal separability: `w1/CritSeparability.md`.

## Sources & frontier

- Rows: 218 → 226 — `grep -cE '^ {0,3}\| *S[0-9]{3,} *\|' corpus/SOURCES.md`; malformed rows 0
  (`awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}'`).
- Census: start `tsukuroi ok`, exit 0 (`.ufo/waves/round-40/before/sources-census-start.txt`); end `tsukuroi ok`,
  exit 0 (`.ufo/waves/round-40/after/sources-census-final.txt`), W04 advisories only.
- Rows added by tier: tier A 8 (S219 meson_options.txt, S220 Arch PKGBUILD, S221 util.c exec environment, S222 trans.c
  scriptlet staging, S223 hook.c hook inputs, S224 alpm-hooks.5 NeedsTargets/Depends/Target, S225 own-work host
  capture, S226 alpm-hooks.5 CAVEATS); B 0; C 0. All `mined`, opened 2026-10-26; Gate quotes in
  `corpus/lessons/round-40.md` `## Gate`.
- Rows touched old→new: S208 used-by `…pacman-hook-order-r38.md, …pacman-transaction-order-r39.md, …boot-writers-r19.md`
  → + `corpus/knowledge/pacman-exec-environment-r40.md`; S209 used-by `corpus/knowledge/pacman-hook-order-r38.md` → +
  `corpus/knowledge/pacman-exec-environment-r40.md`.
- Sourced claim: C2 rests on S219–S225 opened this round.
- Frontier: no Frontier area moves; the entry deepens held update-safety Core (`corpus/README.md` "Round 40 — the libalpm
  execution environment…", frontier notice). Open limits: EX1–EX3/EX5 have no host instance while pacman is paused.
- Mistake mined: five rows in `corpus/lessons/round-40.md` `## Mistakes` (R40-HOSTCELL-UNANCHORED, R40-ANSWER-KEY,
  R40-CONTROL-OWN-BASELINE, R40-HEADING-TIMES, R40-TMP-MISROOT); QUALITY 88 added.
- Assimilation: theme "pacman hook timing" (`merge/tsukuroi/`, `pacman-hook-timing-r25.md`, sha256 `e18c146e…`),
  continued: four residual propositions admitted by re-grounding (NeedsTargets stdin → EX6; `.pacnew` trigger name → EX8;
  cwd `/` → EX1; interpreter → EX4, with correction) and one inference rejected ("every path inside them must be
  absolute"); no staged row, id or text adopted. Collision check: registry ids 225 (before S226), staged ids 147,
  collisions 26 (S200–S225; `.ufo/waves/round-40/assimilation/collisions`); every colliding id names a different
  document, so a future adoption is document-keyed from S227. Guard proof: indented `  | S219 |` caught by the
  0–3-space pattern (1), missed by column-zero (0). Renumber map: none (nothing adopted). Quarantine slice: 12 rows,
  unchanged; none intersects the documents cited this round.
- considerthese: proposal "Probe lineage table" (`considerthese/2026-10-25.md`) mined as `SKILL.md` "Counter lineage —
  rounds 35-40" and a lesson paragraph.

## Trend verdicts

- **expansion: unchanged.** The admitted entry deepens held update-safety ground, not uncovered coverage-map ground
  (`corpus/README.md` round-40 section; `w1/C2ScoutNovelty.md`: EX2 and the AbortOnFail half of EX7 were already held).
- **quality: improved.** C1's selftest now refuses nine literal/guard mutants that passed it at the base (receipts
  above); the round-39 deferred propositions are grounded at source and one staged false inference is refused; the
  round-39 records carry their routed corrections. The entry's own EX5 host defect was caught and withdrawn in-round.
- **discernment: unchanged.** The Gate records admits and a reject with reasons and the round mined its own mistakes
  into QUALITY 88, but both new counters were shown to credit an answer-key writer, and the outside spot-check is
  pending (`w1/CritTrend.md`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round 40 adds the symptom →
  EX row → command table (`SKILL.md` "Hook and scriptlet execution environment — round 40"); non-author verification
  pending.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 40 — hyaku run 8" (host
  capture → source rules → counter → wave verdicts); non-author replay pending.
- [~] Instructions executable by an agent without oral context — the round-40 SKILL tables carry paste-ready read-only
  commands; the whole-SKILL no-oral-context retest remains unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/ConnSiblings.md` and `w1/C2ScoutNovelty.md` found no
  sibling lane covering an EX proposition; self-asserted, no non-author check.

## Round shape, seats, routing

- One v2 wave `w1`: 65 seats — executor 12, critic 12, scribe 8, sentinel 2, revenger 3, simplifier 2 (m_flash roles
  39, 60 %), reviewer 14, mutation-tester 4, scout 5, connector 3. Attack roles (reviewer + critic + mutation-tester)
  30 (46 %). Spec `.ufo/waves/round-40/w1-spec.json` (generator `make-w1-spec.py`), validated payload
  `w1-dispatch.json`, results `w1-results.json`. Planner seat: held by the L1 (validator rejects `planner`); the
  planning data-walk rode connector ConnFrontier and scout AsmPackageScan.
- Dead seats: 0. All 65 seats settled with output (`w1-results.json`, orchestrator WAVE-DONE) and 65 reports are in `w1/`; the last, C1ExecEnvMatrix, landed at 05:17 local after a ten-cell determinism matrix (all PASS). Late reports C1HeldOutGuards (six guard mutants all killed; the `$devn` mutant confirmed equivalent) and C1SentScratch (counter writes only under `--scratch`; two low defects: empty `first_fails`, scratch kept after Ctrl-C) were read after integration and change no verdict.
- Routing: run-8 role map from `~/.omp/agent/config.yml` (never passed `model`); no claim depends on a seat's model.
- Tool installs: none by the L1; no seat reports an install.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none filed this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file from this lane's
  seats (only driver `.ufo/state/` files); `/tmp` lane archives from seat runs of `check-self-assessment.py` were
  transient and are recorded as R40-TMP-MISROOT.
