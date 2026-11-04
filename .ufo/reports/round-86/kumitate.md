# kumitate — round 86

Lane `/home/vgpnk/Projects/shokunin/kumitate-shokunin`. Lane tip at filing: `fc0316e7f3bb84b08ead7944891d83d80cd67d9e`
(pushed; `git ls-remote origin refs/heads/master` prints it). Pre-round base `232350995d3001e606609aaf22ba1b58168d3655`;
freeze `e7228850690c6bd48400140964cbaf18667fbc06`; measured revision M `19b4e440e83ea9d618708003f36c3a799eb13e08`;
disposition `ee0ffa9f7a5c4ec51663b25a366f9b3d241146a3`. One v1 wave, 12 seats, settled before this report
(`.ufo/waves/round-86/w1-results.json`).

## Work performed

**Declared claim (one).** C1 — **operability**, the lane's lowest non-retired axis (integer 9, terminal
under `f_O`): a **capability acquisition**, `counter-receipt` v3, whose answer binds *both* halves of a
counter-transcript verdict to the bytes it read — the transcript half already did, the source half now
carries a digest of the same source buffer it parsed. The lane's other five rows are saturated coverage
sub-axes at 10 and a second operability claim would be one claim under `AXES.md`, so the round declares
one claim and spends the remaining seats on the pre-registered measurement amendment and the routed
defects. Round-85 pre-registration candidates (5), (6) and (7) are the claim's content.

- **C1 predicate frozen before any candidate data** — plan, 24-arm probe and four scored controls at
  `e7228850`: `.ufo/waves/round-86/plan.md`, `.ufo/waves/round-86/probe/probe86-c1.mjs`,
  `.ufo/waves/round-86/controls/`. Target `C86_C1: HELD held=24/24` exit 0; kill rule: any arm red, or any
  control reaching 24/24.
- **Pre-data controls scored, then committed** — v2 base `14/24`, constant printer `0/24`, label-keyed
  no-reader `0/24`, nonce-only replay `0/24`, each exit 1 with `rev=`/`cmd=`/`exit=` headers
  (`.ufo/waves/round-86/controls/{base,stub,noreader,replay}.txt`).
- **Probe coherence disclosed, not claimed** — an L1 scratch reference (v2 + the digest line) read
  `HELD held=24/24` before the freeze; it is not the claim's evidence and is not committed (`plan.md` §C1).
- **v3 instrument integrated** — `scripts/counter-receipt.mjs` sha256
  `e95313700aaf8430c51e0f8abdb991ab168519eecf9803cce3fac51154f31069`: `SOURCE:` gains
  `sha256=<source bytes>`, everything else byte-identical in behaviour; its own suite grew to 63 cases
  (`.ufo/waves/round-86/close/selftest.txt`).
- **Independent driver, built from the contract only** — `.ufo/waves/round-86/build/K86ExecDriver/driver86-c1.mjs`
  (54 arms, 10 generated fixtures) reads `K86_EXEC_DRIVER: HELD held=54/54` against the integrated bytes
  (`build/K86ExecDriver/`).
- **Supplemental same-path control** — `.ufo/waves/round-86/probe/same-path.mjs` (one path overwritten three
  times): base/stub/no-reader/replay each `0/3`, base distinct and canned controls not
  (`controls/cv-*.txt`); committed `d12847c5` **before** integration and disclosed as a late supplement, with
  the frozen probe left untouched.
- **Pre-registered `A` re-baseline measured before candidate data** — `.ufo/waves/round-86/open/a-rebaseline.txt`:
  tracked runnable files 980 at base, **35** outside `.ufo/`, `A_wave` 945; `f_O` = 9 under both denominators.
  `scripts/proxy-check.mjs` now derives `A` excluding `.ufo/` and prints the non-scoring `A_wave`; a selftest
  arm proves a wave-shaped `.mjs` moves `A_wave` and not `A`.
- **R85-V12 repaired in the gate, not by hand** — `scripts/readme-map.mjs` (contract `kumitate-readme-map-v3`)
  counts rows only inside `## Coverage map`; a row elsewhere is `outside-map` and the verdict carries
  `outside_map=<n>`; the 28 rows that sat under `## Known gaps`/`## Frontier` were moved into the table.
  `README_MAP: CLEAN files=219 rows=219 covered=219`, selftest 18/18 (`close/map.txt`, `close/map-selftest.txt`).
- **R85-V1…V15 answered** — named corrections appended to `SCORECARD.md` §“Round 86 — named corrections to
  round 85” and `LOG.md` (proxy MATCH was false: committed receipts read A_DRIFT 975/980; counts
  908/913/975/980; shipped-only 35; candidate-vs-integrated digest; attack set 4/13; report commit
  `b67837ee`; sub-item commits `6e3e4749`/`602f1835`); the section arm, the source rows and the corpus
  entry close the rest; `K86Scout` re-derived each one against committed bytes
  (`.ufo/waves/round-86/w1/K86Scout.md`, `build/K86Scout/receipts-2026-11-04.txt`).
- **Corpus curated and one mistake class gated** — S247/S248 admitted, S249 rejected, S246 re-opened
  (`corpus/SOURCES.md:201-203`); `corpus/knowledge/counter-receipt-source-binding.md`; Q79 in
  `corpus/QUALITY.md:1326-1340`; `corpus/lessons/round-86.md` with `## Gate` (2 admits, 1 reject, 1 re-open)
  and five `## Mistakes` rows.
- **Sibling scan** — `K86Connector` found the digest-binding surface uniquely this lane's and named souji's
  receipt digest and tameshi's context capture as sibling ground, not absorbed
  (`.ufo/waves/round-86/build/K86Connector/findings.json`).
- **Gates at M** — `PROXY: MATCH --strict` exit 0 (`A=35 A_wave=955 C=45 C2=219/219`, operability 9);
  `SOURCE_CAPTURE: CLEAN captures=76`; `SOURCE_DUPES: CLEAN groups=7 known=7`; `SOURCES_CHECK: CLEAN rows=187`;
  `plan-before-ready --round 86` exit 0 (`close/`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: plan, 24-arm probe, four scored controls, `A`-rebaseline receipt, round-85 spot-check adopted (row + pin) | `LOG.md` §Round 86 | `e7228850` |
| Supplemental same-path control + its four scored receipts | `LOG.md` §Round 86 | `d12847c5` |
| `counter-receipt` v3, `proxy-check` `A`/`A_wave`, `readme-map` v3, README relocation, SKILL rows/checklist, SOURCES S247–S249, knowledge entry, lesson, Q79, pins | `LOG.md` §Round 86 | `19b4e440` |
| Measured disposition, capability row, close receipts | `LOG.md` §Round 86 measured disposition | `ee0ffa9f` |
| Opened Node crypto capture bound by the S249 pin | `LOG.md` §Round 86 | `fc0316e7` |

## Before → after measurements

**C1 (operability, capability `counter-receipt` v3).** Counting command, run at the cited revision:

```
node .ufo/waves/round-86/probe/probe86-c1.mjs --lane /home/vgpnk/Projects/shokunin/kumitate-shokunin --work DIR
```

| state | command target | reading | commit |
|---|---|---|---|
| before (v2 bytes) | `controls/base/scripts/counter-receipt.mjs` | `C86_C1: UNMET held=14/24` exit 1 | `e7228850` |
| after | integrated `scripts/counter-receipt.mjs` | `C86_C1: HELD held=24/24` exit 0 | `19b4e440` |

Controls, same counter: constant `0/24`, label-keyed no-reader `0/24`, nonce replay `0/24` — none reaches
the target, so the frozen kill rule does not fire. Corroboration at the same M: tool selftest
`PASS held=63/63`; independent driver `HELD held=54/54`; same-path control `HELD held=3/3 distinct=true`.

**Non-claim measurement (pre-registered, no axis credit).** `A` re-baseline:

```
git ls-tree -r --name-only master | grep -E '\.(mjs|js|sh|py)$' | grep -v '^\.ufo/' | wc -l   # 35 at base
find . -path ./.git -prune -o -path ./.ufo -prune -o -type f \( -name '*.mjs' -o -name '*.js' -o -name '*.sh' -o -name '*.py' \) -print | wc -l
```

980 → 35 scored, `A_wave` 945 (base) → 955 (M, includes this round's probe/helper/candidates);
`f_O` = 9 before and after, so the operability integer is unchanged and the move is measurement accuracy,
not a score claim. `PROXY: MATCH --strict` exit 0 at M with the amended stanza.

**R85-V12 gate gap.** A fixture with one corpus row after `## Frontier` read `CLEAN` before the change and
`DRIFT … outside_map=1` after (`readme-map --selftest`, case 17); case 18 keeps an in-map tree clean.

## Sources & frontier

`SOURCES: 184 → 187 rows` — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
(184 at base `23235099`, 187 at `fc0316e7`). Tier histogram before A=157 B=17 C=10 → after A=158 B=19 C=10;
status before mined 147 / queued 13 / rejected 24 → after mined 149 / queued 13 / rejected 25
(`awk -F'|' …` census in `CORPUS.md`; counts recorded in `.ufo/waves/round-86/open/source-counts.json` and
the same walk re-run at close).

- Rows added by tier: **A** 1 (S249), **B** 2 (S247, S248).
- Rows touched old→new: **S247/S248/S249 appended only**; no existing `status`/`recheck`/`used-by` cell was
  edited — S247 and S248 open `supersedes S245`/`S246` per CORPUS rule 2, and the duplicate-URL pair
  (S245,S247) is pinned in `.ufo/pins/source-dupes.json` rather than hidden (`SOURCE_DUPES: CLEAN groups=7`).
- Frontier rows advanced: the counter-instrument band now has `corpus/knowledge/counter-receipt-source-binding.md`
  (frontier → held ground for the source half), and S247/S248 replace the two survey rows the round-85
  spot-check rejected as mis-transcribed/unreachable.
- Census, run at both ends: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kumitate` → exit **0** at open (`.ufo/waves/round-86/open/source-census.txt`,
  six pre-existing `W04` duplicate-URL warnings) and exit **0** at close (`close/census.txt`).
- `Assimilation: none` — the package at `/home/vgpnk/Projects/shokuknow/merge/kumitate` exists and is
  read-only, and no staged row is adopted this round (the round-85 spot-check's remaining work is the lane's
  own instrument, not staged material). The initial host probe misspelled the path (`shukuknow`) and its
  ENOENT is **not** absence evidence; that typo is a `## Mistakes` row and was corrected before the freeze.
  `considerthese/2026-10-26.md` was reopened: ideas 1/2/3/4/6 already map to Q75/Q76/Q68/Q69/Q72; idea 5 asks
  for non-author spot-check formatting, which this lane does not own.

## Trend verdicts

- **expansion — unchanged.** The one admitted entry deepens ground the coverage map already held
  (counter-transcript reconciliation/discrimination); no new frontier area is entered and no capability row
  is credited to expansion. Evidence: `corpus/README.md` coverage map; `SCORECARD.md` capabilities table.
- **quality — improved.** A weaker instrument is superseded by a stronger one on the same surface, proven on
  committed bytes (v2 14/24 → v3 24/24, controls unmoved; the r83 repair receipt still reads
  `DRIFT SOURCE_DECLARED`); two source rows are corrected rather than left standing (S247/S248), the orphan
  fragment in the v2 entry gets a named correction, and Q79 turns the round-85 attribution defect into a
  criterion. No admitted entry fails its re-check.
- **discernment — improved on the lane's own record.** The round rejected one candidate (S249) with its flip,
  re-adjudicated the standing S246 reject to an admission, and mined five mistakes, three of them with
  shown-able-to-fail receipts (map pin, candidate-vs-integrated digest, spec-text wave path). The non-author
  agree/disagree sample is the closure integrator's to record; this report does not self-attest it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` gate
  registry row `counter-receipt` (v3, `SKILL.md:607`), `readme-map` v3 (`:632`), checklist item
  `SKILL.md:761`; non-author verification pending.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the v3 acquisition and its
  measured disposition in `LOG.md` §Round 86, receipts `.ufo/waves/round-86/close/`.
- [~] Instructions executable by an agent without oral context — every claim, control and gate command in
  `plan.md`/`corpus/lessons/round-86.md` carries an absolute path and an expected verdict string.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round; the connector's
  sibling scan reported souji/tameshi ground without absorbing it.

## Round shape, seats and disclosures

ONE v1 wave, 12 seats under `ufo-wave-policy.json` (band 8–16): executor 4, scribe 1, scout 1, reviewer 1,
critic 1, mutation-tester 1, sentinel 1, connector 1, revenger 1 — attack seats 5/12 (≥25 %), connector 1,
no residual call, round total 12. The L1 held the canonical planner seat (the validator refuses `planner`).

- **Dead seat:** `K86Mutation` — `401 Invalid 'Authorization' header or token
  (type=authentication_error param=UNAUTHORIZED)` on `commandcode/deepseek/deepseek-v4.1-flash`; reported to
  the orchestrator, never replaced, no reroute requested.
- **Seats without artifacts:** reviewer, critic, sentinel and revenger settled while the orchestrator kernel
  restarted mid-wave; their output was not retained and no report/build file exists. Their items therefore
  produced **no** post-data adversary evidence, and this report does not claim any: falsification rests on the
  four frozen pre-data controls, the supplemental same-path control, the independent driver and the scout's
  revision-bound recon.
- **Conformance defect (disclosed, not repaired):** `ready-handoff --round 86 --wave w1` reads
  `DRIFT RELATIVE_WAVE_PATH ×4 (seat K86ExecProxy names a lane-relative .ufo/waves path)` on this round's own
  dispatch (`close/ready.txt`). It is a spec-text defect in the wave item; the seats still wrote inside the
  lane, and the taken `.ready`/dispatch are never rewritten. Round-87 candidate (6).
- **Frozen-text count correction:** the probe header says “twelve” arms generate at run time and the plan says
  “four arms” assert the source digest; measured, 21 of 24 arms vary per run and nine carry `--src`. Recorded
  in `corpus/lessons/round-86.md` `## Mistakes`; the 24-arm table and predicate are untouched.
- **Carried red:** `cite-check` DRIFT 2289 errors at M (2292 before this round's files; no new unresolved
  token — the round fixed three of its own and added none). `harm-matrix` was not re-run this round; the
  reds named above are the ones measured.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows one untracked fleet-root
  file, `after` (24 B, `== SCORECARD diff base-`), which names neither this lane nor round 86 — another
  lane's seat artifact, left untouched. No file of this round's seats was found at the fleet root.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. Launch
  `2026-11-04T17:00:42-03:00`, one kernel restart mid-wave, progressing throughout.
- **Tool installs:** none (no package, binary or upgrade installed this round).
- **Open operator question (L0):** routing — the assignment text says `m_mim` is on no role and `scout` is
  `@m_antigravity`, while `~/.omp/agent/config.yml` at dispatch routed `scout`/`scribe` to `@m_mim` and
  `connector` to `@m_antigravity`. The lane changed nothing and passed no `model`; the conflict is filed for
  the operator.
