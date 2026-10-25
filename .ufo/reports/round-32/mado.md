# mado — round 32 report (hyaku inline campaign, attempt 1)

Lane tip (measured, pushed): `d9ed38166cc3be8ef4c52b41d66ad94010feb047` on `master`
(`jj-lane.sh state`: `local=d9ed3816 remote=d9ed3816 ahead=0 behind=0`). Round-32 commits, in
order: `f5910876` data + wave-1 evidence · `48f9fe09` scratch-tree removal · `a551f71c`
published axis table + claims + LOG · `d9ed3816` seat-report refresh. Registration frozen
before any data: `.ufo/waves/round-32/registration.md` (in `f5910876`).

## Work performed

Two declared claims, causally separable, each on a distinct axis (the round contract prefers
two; a third was not added because the item-10 assimilation rides inside the frontier step):

- **C1 — coverage** (the lane's owned axis): the **Hyprland IPC two-socket contract** theme
  moves from frontier to core — three admitted knowledge entries plus five `corpus/SOURCES.md`
  registry rows, every source re-opened by the lane itself on 2026-10-24.
- **C2 — calibration** (the lane's **lowest-scoring non-retired axis**, resolved-active
  39/40 = 0.9750 at the r31 tip): the lane's *published* axis table is stale against the
  counters it names; a new gate re-derives the published fractions and fails when they differ.

Work items (evidence pointers):

- Registration frozen before any data seat ran — `.ufo/waves/round-32/registration.md`
  (claim predicates, frozen counters, kill rules, do-nothing controls).
- **Item-10 assimilation, sources re-opened by the L1** (fetched bytes kept under
  `.ufo/waves/round-32/fetch/`): `S186.bin` 6,539 B sha256 `535bc4c385a06162…`,
  `S187.bin` 268,731 B, `S188.bin` 12,879 B sha256 `c830ce0717f92776…`, `S189.bin` 6,479 B
  sha256 `eea605dfe5ce09e1…`, `S196.bin` 297,863 B sha256 `f9b51362f2440e02…`. Every byte
  length and digest matches the package's published anchor; the package's **line** anchors did
  not (see `## Mistakes`).
- Three entries admitted: `corpus/knowledge/ipc-contract-r25.md` (S186, S187, S189),
  `corpus/knowledge/dispatcher-semantics-r25.md` (S188),
  `corpus/knowledge/dispatcher-surface-and-request-grammar-r26.md` (S186, S188, S196) —
  each opening with the provenance trio and a `## Gate` block carrying the lane's own access
  date and a ≤25-word located quote.
- Five registry rows appended — `corpus/SOURCES.md:198-202` (S186, S187, S188, S189, S196) —
  normalized to the census 11-column schema (`recheck` = `90d`, `opened` = `2026-10-24`,
  `used-by` = exactly the citing entries, `status` = `mined`, no literal or escaped `|` in any
  cell). **No row was appended that no admitted entry cites**; nothing was bulk-imported.
- Id-collision check **before the first append** — `.ufo/waves/round-32/assimilation/`:
  `reg-ids` 185, `staged-ids` 132, `collisions` **0** (the staged set starts at S186). Guard
  proven able to fail: on the indented fixture `  | S002 | …` the 0–3-space extractor finds
  `S002` while a column-zero-only extractor finds nothing
  (`fixture-indented.md`, `fixture-ids`, `fixture-ids-col0`).
- Validate-before-append on a scratch mirror of the lane (`assimilation/validate/`) —
  census `validate --file` on the mirrored registry, run before the first append; the
  lane-level census after the round exits 0 (pasted under `## Sources & frontier`).
- Quarantine hand-check — `.ufo/waves/round-32/assimilation/quarantine-slice` (13 rows:
  6 payload-absent + 7 never-checked) with a per-row verdict in
  `.ufo/waves/round-32/w1/reports/ExecQuarantineSlice.md`: 5 PRESENT/adoptable, 1 ABSENT as
  quoted (S224, rotating `updated_at`), 7 UNVERIFIABLE prose cells (`unreachable` is not
  fabrication). **No quarantined row was appended**; the register was read, never edited.
- **C2 instrument** — `quality/check-axis-scores.py` (255 L, selftest `17/17`), which takes the
  lane's *last* published axis table and re-derives each axis it can re-derive at the revision
  under test, using that axis's own committed instrument.
- `considerthese/2026-10-23.md` mined for exactly **one** still-unimplemented proposal
  (proposal 3, "cross-check one landed tool against a public pin") — grounded by re-opening the
  pins it points at; it lands as the round's Gate block and the lane's `S###.bin` fetch
  convention, not as a claim. The operator-authored file was **not edited**.
- Frontier step — `corpus/lessons/round-32.md` (## Gate with 3 admits, 1 reject with reason
  and flip, the quarantine verdicts; ## Mistakes with four rows), the source census before and
  after, and the C1 sourced claim (S186/S187/S188/S189/S196).
- Round shape (below), the lane hygiene repair, and the honest stop on C1 (below).

## Landed changes

| Commit | Change | LOG.md tie |
|---|---|---|
| `f5910876486943d967e6994e21ccddb9aee4f249` | the three admitted entries, the five registry rows, the three coverage-map rows, `corpus/lessons/round-32.md`, `quality/check-axis-scores.py`, the whole wave-1 evidence set (`registration.md`, `w1-spec.json`, `w1-taskcall.json`, `dispatch-w1.sh`, 32 seat reports, fetch bytes, assimilation receipts) | §Round 32, work bullet 1–3 |
| `48f9fe094ac1a41cd36d1d36eaff644963aa009f` | removal of a seat's 187 MB scratch clone trees from the committed wave set (the bytes stay in history at `f5910876`) | §Round 32, honest notes |
| `a551f71c8fae2559a6c9b35310ebab327fadef25` | the re-derived axis table, the round-32 claims table, the capability row, the planned row and the LOG entry | §Round 32, work bullet 4–5 |
| `d9ed38166cc3be8ef4c52b41d66ad94010feb047` | refresh of the four seat artifacts that finished after the data commit | §Round 32, honest notes |

Lane commits carry the lane identity `mado-shokunin <mado@shokunin.local>`; every commit was
made through `scripts/hyaku/jj-lane.sh` and the `landed <hash>` line is the only citable
output. The report itself is committed on the fleet repo through
`scripts/hyaku/fleet-commit.sh --as mado`.

## Before → after measurements

**C1 — coverage (the Hyprland IPC two-socket theme).** Frozen counter (registration §C1),
run over committed bytes:

```sh
cd /home/vgpnk/Projects/shokunin/mado-shokunin
A=corpus/knowledge/ipc-contract-r25.md; B=corpus/knowledge/dispatcher-semantics-r25.md
C=corpus/knowledge/dispatcher-surface-and-request-grammar-r26.md
e=0; for f in "$A" "$B" "$C"; do [ -f "$f" ] && e=$((e+1)); done
r=$(grep -cE '^\|[[:space:]]*S(186|187|188|189|196)[[:space:]]*\|' corpus/SOURCES.md)
c=$(grep -cE '^source:.*S(186|187|188|189|196)' "$A" "$B" "$C" | awk -F: '{s+=$2} END{print s+0}')
echo "entries=$e rows=$r cited_entries=$c"
```

- Before (base `256222890d935212874a09751ff9b7869943c2d7`): `entries=0 rows=0
  cited_entries=0` — reproduced by the wave's own control seat
  (`.ufo/waves/round-32/w1/reports/ExecThemeHoldCheck.md`).
- After (tip `d9ed38166cc3be8ef4c52b41d66ad94010feb047`): `entries=3 rows=5
  **cited_entries=7**`.
- The registered target was `entries=3 rows=5 cited_entries=3`. The counter prints **7**, and
  the wave's critic proved the counter unsound in both directions:
  `.ufo/waves/round-32/w1/reports/CriticC1Predicate.md` (verdict: **CLAIM DEAD — predicate
  dead, not necessarily the data**) built a junk tree — three 13-byte stub files, each one
  `source: S<n>` line, plus five stub rows whose `used-by` names a file that does not exist —
  and the **verbatim frozen counter printed `entries=3 rows=5 cited_entries=3`, TARGET MET**;
  it also built a realistic tree (two `source:` lines on one entry) that the counter *falsely*
  rejected with `cited_entries=4`. The critic's report landed at **20:08:00**, the data commit
  at **20:05:38** — 2 min 22 s later.
- **Verdict: C1 is an HONEST STOP — not met under its registered counter.** The landed
  artifacts are real (three entries with located quotes, five census-valid rows, index map
  46/46), but the registered counter cannot distinguish them from junk, so the claim is not
  reported as verified. The target was **not** narrowed after landing and the counter was **not**
  re-frozen; the minimal sound repair (count *entries that cite at least one of the five ids*,
  and require each id to be registered and each `used-by` path to exist) is routed to round 33
  as a **recommendation**, not as this claim's rule.
- Do-nothing controls (seat `ExecThemeHoldCheck.md`): rows-only → `entries=0 rows=5
  cited_entries=0`; entries-only → `entries=3 rows=0 cited_entries=3`. Neither half alone
  reaches the triple — the counter's *shape* is not the problem, its *soundness* is.

**C2 — calibration (the published axis table must not be stale).**

```sh
python3 -I quality/check-axis-scores.py --rev <rev> --repo .
```

- Before (base `256222890d935212874a09751ff9b7869943c2d7`): `MADO_AXIS_ROW: axis=navigation
  published=43/43 derived=43/43 verdict=MATCH` · `axis=calibration published=39/40
  derived=41/41 verdict=STALE` · `axis=operability published=9/9 derived=12/12 verdict=STALE`
  · `MADO_AXIS: checked=3 mismatched=2`, exit 1.
- After (tip `d9ed38166cc3be8ef4c52b41d66ad94010feb047`): all three rows `MATCH` ·
  `MADO_AXIS: checked=3 mismatched=0`, exit 0.
- The pre-fix tip (`48f9fe09`) measured `mismatched=3` (navigation had moved to 46/46 while the
  publication still said 43/43) — that is the honest reading of the base→tip movement.
- Instrument soundness: `python3 -I quality/check-axis-scores.py --selftest` →
  `MADO_AXIS_SELFTEST: 17/17 assertions passed` (exit 0), including "a missing publication is
  not a pass" and "a missing instrument is not a pass"; the perturbation control (published
  `41/41` → `40/41`) is caught by the same rule. Independent attack: the wave's
  `CriticC2Predicate.md` (verdict **CLAIM SURVIVES**, twice — on the comparison rule and on the
  NOT-PUBLISHED rule) with one disclosed nuance: the round-31 table was *honestly* a
  base-state record; the lane nevertheless **consumes the last table as its current
  self-assessment**, which is what the gate enforces.
- **Verdict: C2 target met (mismatched 2 → 0, exit 1 → 0).**

Supporting counters at the tip: `quality/check-index.py --rev <tip> --repo .` →
`indexed=46/46 missing=0 dangling=0 duplicates=0 coverage=10.0000/10`;
`quality/check-index-rows.py --rev <tip> --repo .` → `rows=46 errors=0 warns=3` (the three
warns are the pre-existing r12/r24 glob conventions); `.ufo/waves/round-31/c2/count.py <tip>` →
`active=41 resolved_active=41 fraction=1.0000`; `quality/check-index.py --selftest` →
`12/12 assertions passed`.

## Sources & frontier

Census command (both ends pasted, exit 0):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- **before** (round start): exit 0 — `mado ok /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md`, 185 rows, seven `W04` duplicate-url warnings (all pre-existing).
- **after** (round end): exit 0 — same lane result, **190 rows**, the same seven `W04` warnings.
- Rows added: **5**, all tier **A** — S186, S187, S188, S189, S196 (three `docs`, one `docs`
  version-matched page, one `code` at the host's own v0.56.2 commit). Each carries the lane's
  own access date `2026-10-24` and a ≤25-word located quote in the lesson's Gate block.
- Rows touched old→new: **none** (S001–S185 byte-unchanged). Frontier rows advanced: **none**.
- Sourced claim: **C1** — its entries cite S186, S187, S188, S189, S196, all `mined` rows
  opened and re-grounded this round.
- Frozen manual census (CORPUS.md §Census) re-run by the wave's executor seat:
  `.ufo/waves/round-32/w1/reports/ExecCensusManual.md`.
- **Assimilation: adopted.** One theme (the Hyprland IPC two-socket contract), 3 admitted
  entries, 5 rows, 1 rejected candidate (`two-literature-drift-r26.md` — PROVINCE scope:
  documentation localization is not a desktop/compositor-craft surface, and two of its rows are
  tier-C community; flip recorded in the lesson's Gate block). The source repo
  `/home/vgpnk/Projects/shokuknow` was read only; nothing was written, committed, fetched or
  pushed there, and no campaign tool was run there.
- Mistake mined: `corpus/lessons/round-32.md` §Mistakes — 4 rows: two `scope` (a seat wrote
  outside its declared scope into `corpus/README.md` and `LOG.md`; the wave's write scope was
  stated in prose only), one `reference-drift` (the package's line anchors are wrong while its
  byte/digest anchors are right), one `number-drift` (the published axis table stale against
  the counters it names). Each fix names the command that fails before it and passes after.

## Trend verdicts

- **expansion — improved.** Three admitted `knowledge/` entries on ground the coverage map did
  not hold (the lane held no IPC-contract or dispatcher-semantics row; its only socket mentions
  were incidental), each citing a `mined` registry row opened this round; the coverage map grew
  43 → 46 rows over 46 notes (`indexed=46/46`).
- **quality — improved.** A real self-assessment defect was found and repaired by
  re-derivation (published 39/40 & 9/9 against derived 41/41 & 12/12), the staged package's
  wrong line anchors were re-derived rather than copied, and no admitted entry failed its
  re-check. The round's own unsound counter is disclosed rather than hidden.
- **discernment — unchanged.** The wave's critic disagreed with the lane's frozen C1 predicate
  and the disagreement was learned (lesson row + routed round-33 repair), so it was not left
  unlearned; but no grounded `QUALITY.md` criterion was added this round — the counter was
  killed **after** the data landed, and the round-31 counter's published fractions are cited by
  C2's axis line, so the criterion is deferred rather than added blind. The outside spot-check
  of this round's own admits and rejects (3 admits, 1 reject) remains the closure's duty.

## Round shape, wave evidence, seats

**Shape: one v1 wave, 32 seats, band 32–64, policy
`scripts/hyaku/ufo-wave-policy.json` (validator `ufo-swarm-wave.mjs plan` → exit 0,
`counts.spawn=32`, `dispatch.calls=1`).** No wave 2: the v1 second wave requires wave 1 to
yield ≥32 distinct attack items, and the wave's 13 attack seats produced their findings after
the data was committed, so a falsification wave could not gate this round's landing. No
residual task call was made.

- Spec `.ufo/waves/round-32/w1-spec.json`; rendered `taskCall` (32 tasks, each led by
  `/skill:godspeed`) `.ufo/waves/round-32/w1-taskcall.json`; dispatcher
  `.ufo/waves/round-32/dispatch-w1.sh`; seat reports `.ufo/waves/round-32/w1/reports/` (32).
- Seat-role mix (32): scout 7, reviewer 6, executor 5, scribe 4, critic 4, connector 2,
  revenger 1, sentinel 1, mutation-tester 1, simplifier 1 — **13 of 32 (40.6%) attack roles**
  (reviewer 6 + critic 4 + revenger 1 + mutation-tester 1 + sentinel 1), above the 25% floor.
  §3's floor roles are all covered (connector ×2, executor ×5, scribe ×4, scout ×7, reviewer
  ×6, critic ×4). `planner` is a frozen-topology seat the validator rejects: the L1 holds the
  canonical planner seat and the bounded planning data-walk rode the scout/connector items.
- **Dispatched: 32. Returned with a report: 32. Dead seats: 0** (24 exit codes recorded as 0;
  the dispatcher script was cut by the harness's 600 s background-task timeout before the last
  eight seats wrote their exit codes — every seat nevertheless produced its report file).
- **Host mapping, stated plainly:** this seat has no `task`/AgentSwarm tool, so the validated
  `taskCall` was dispatched as **one batched launch of 32 concurrent `omp -p` seat processes**
  carrying each seat's composed task text unchanged (`.ufo/waves/round-32/dispatch-w1.sh`). The
  route per seat is the operator's own `task.agentModelOverrides` table in
  `~/.omp/agent/config.yml` (read-only here) — the taxonomy role decides the route; no provider
  or model literal is written into the lane repo. Seats were bound to absolute lane paths and
  the fleet-root-relative-path trap was closed by the wave context.
- **Scope violation, recorded not hidden:** two seats wrote outside their declared scope (the
  lane's `corpus/README.md` and `LOG.md`). Both files were restored from the branch tip
  (`git show master:<path> > <path>` — no `git checkout`, no `git add`) and re-applied under the
  L1 alone; the restored bytes and the L1's own appends are the diff. A stray `LOG.md.lock`
  was removed. A seat's 187 MB scratch clone trees were committed in `f5910876` and removed in
  `48f9fe09` (the bytes remain in history).
- Misroot sweep before this report: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  — the untracked/modified fleet-root entries are `.ufo/state/*` driver files, `.ufo/watchdog.log`
  and other lanes' artifacts (`live.html`, `bm.json`, `.omp/mcp.json`); **no mado round-32 file
  landed at the fleet root**, and nothing of another lane's was touched.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources →
  unchanged this round; the three admitted entries add cited decision material to the corpus,
  not to SKILL.md. Evidence: `corpus/knowledge/ipc-contract-r25.md` §1–§3,
  `corpus/knowledge/dispatcher-semantics-r25.md` §1–§3, `corpus/knowledge/dispatcher-surface-and-request-grammar-r26.md` §1–§3. Asserted by the author; no named non-author verifier for this box yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md → this round's end-to-end task is the assimilation itself (fetch → re-ground → transform → validate → append → census → re-derive), executed and logged in `LOG.md` §Round 32 and `corpus/lessons/round-32.md`. Evidence: `.ufo/waves/round-32/assimilation/`, the census receipts, and the five `landed` commits. No named non-author verifier.
- [~] Instructions executable by an agent without oral context → the wave context carried
  absolute paths, the write scope, the pacman guard and the planner mapping; 32 seats executed
  it without oral context. Evidence: `.ufo/waves/round-32/w1-spec.json` and the 32 reports in
  `.ufo/waves/round-32/w1/reports/`. Asserted by the author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → one candidate was **refused** on
  PROVINCE grounds (`two-literature-drift-r26.md`, documentation localization), and the
  connector seat's read-only sibling scan is at
  `.ufo/waves/round-32/w1/reports/ConnectorSiblingOverlap.md`. Asserted by the author; the
  outside verdict is the closure's duty.

## Extras

- **Stale-lane:** none — respawn-per-round driver; this report and its commits are the only
  artifacts of round 32, and no round 33 was started.
- **L0 questions:** none appended this round — no operator decision blocked the round. Two
  items are operator-visible in the report rather than as questions: the paused pacman guard
  (respected) and the item-10 "wave-4 quarantine-first" pattern, which this lane did **not**
  take (it adopted from its own package after hand-checking, because its package's quarantine
  slice was hand-checked row by row this round).
- **Tool installs:** none. No tool was installed or upgraded by the L1 or by any seat; the
  `/home/vgpnk/.omp/agent/RULES.md` policy and the paused-pacman guard were carried in the wave
  context and neither was needed.
- **Honest notes.**
  1. **C1 is an honest stop.** Its registered counter prints `cited_entries=7`, not the
     registered `3`, and the wave's critic proved the counter admits junk trees and rejects
     realistic ones. The claim is reported **not met**; the predicate was not re-frozen and the
     target was not narrowed after the data landed.
  2. The round ran **~35 minutes over** its 170-minute budget: the wave's 32 seats ran
     concurrently while the L1 re-opened five sources, wrote three entries, built and hardened
     the C2 gate, and repaired two seat scope violations.
  3. `quality/check-axis-scores.py` was written and then **edited mid-flight** (9132 B → 9448 B)
     to parse the publication's wrapped prose; the critic observed that edit in the working
     tree. The committed bytes are the ones measured above.
  4. The lane's `corpus/QUALITY.md` was deliberately **not** touched this round: adding a
     criterion would have moved the round-31 counter's `active=41`, which C2's published axis
     line cites. The criterion the counter's own kill warrants is therefore a round-33 task.
