# souji round 84 — report

Lane: `souji-shokunin` (repo `/home/vgpnk/Projects/shokunin/souji-shokunin`), round 84, attempt 1 (`SoujiR84`).
Lane base `54709d0db92d9dcd95504a34173c1f6a3fd88ec1` (r83 closed `admitted`). Round shape: one v1 wave of 12 seats
under `scripts/hyaku/ufo-wave-policy.json` (band 8-16).

## Work performed

Declared claims (2, causally separable — S84Connector §1: no shared file, counter, population, command or receipt):

1. **C1 — calibration 7 (the lane's lowest owned non-retired axis): the false-row population binds five pointer-counter clauses.**
   The lane's population is its self-assessment instrument; the r83 36-row population certified five clauses it did
   not discriminate. The r84 44-row population carries one false row per claimed clause (the five named) and true
   rows for the shapes it names, and a clause-kill battery measures the difference; the population is not minimal
   and does not certify the counter's whole rule (A8/A10).
2. **C2 — operability 8: the vault CLI's signal path freezes the descendant tree before terminating it.**
   The r83 walk TERMed descendants after a single map read, so a CLI that trapped the signal and forked a `setsid`'d
   child escaped both the map and the group kill.

Work items, each with a pointer:

- Frozen instruments committed before any after-data (P `bd2bbb12`): `census/round-84/c1-false-rows.tsv` (44 rows,
  sha256 `4795f009…f6f`), `c1-false-row-harness.py` (R7 fixture + two pinned populations),
  `c1-mutants.json` (five single-edit mutants), `c1-clause-battery.py`, `c1-pointer-counter.py` (the r83 bytes,
  `052c4f3f…`), `c2-population.tsv` (22 rows, `31422477…ec58`), `c2-late-fork-counter.py` (the `latefork` stub), the
  do-nothing control `controls/c2-K-a-r83-tool.sh` (`72a405f2…`), and both before receipts.
- Preregistration frozen alone in F `35d87842` (`git show --name-only` = `census/round-84/preregistration.txt`).
- C1 after arm on the filed bytes: `census/round-84/records/c1-after.txt` — `ARM pristine pop=r84 rows=44
  mismatches=0 errors=0`, five `MUTANT-PAIR … killed=yes`, `SUMMARY mutants=5 sets=r84 pristine_r84=ok killed_r84=5
  killed_total=5`, EXIT 0. Per-mutant killing rows: m6↔NF-L, m7↔NF-L2, m8↔TF9+TF10, m9↔TF8+TF9+TF10+NF-P
  (`census/round-84/records/c1-m9-rows.txt`: `refused_true=3 accepted=1`), m10↔NF-M.
- C1 before arm (do-nothing: the same counter, battery and mutants on the r83 36-row population):
  `census/round-84/controls/c1-before-r83-population.txt` — pristine `36/0`, five `killed=no`, `killed_r83=0`, EXIT 0.
- C2 repair in `tools/souji-vault-verify.sh` (`cli_kill_tree` only): SIGSTOP every descendant discovered by a
  fork-free `/proc` pass before any trappable signal, a second map pass for the read→STOP window, then a SIGKILL
  sweep with the starttime re-checked; every stat read is whole-file with the last-`)` strip (closes r83 spot-check
  D5 on the re-check path). Filed tool sha256 `030fa10d…ef41d` (`1f49b3a7`).
- C2 after arm: `census/round-84/records/c2-after.txt` — `rows=22 mismatches=0 errors=0 orphans=0`, l1 0.7 s / l2
  0.6 s, 0 survivors, EXIT 0. Before: `census/round-84/controls/c2-before-r83-tool.txt` — `mismatches=2 orphans=2`,
  one surviving `setsid sleep 600` per late row, EXIT 1.
- C2 regressions on the filed bytes: `records/c2-regress-selftest.txt` (57 checks, 0 failed), `c2-regress-r17.txt`
  (`total=37 failed=0 skipped=0`), `c2-regress-probe-d.txt` (`arms=4 failed=0`).
- C2 clause mutants of the filed bytes: `records/c2-mutants-on-filed.txt` — STOP→TERM killed (1 mismatch), no-KILL
  sweep killed (2), single-pass survives (22/22), first-line re-check survives (22/22). The last two are the
  unrowed belts A1/A2.
- Sources: S334 (`signal(7)`, admitted), S335 (own-work clause-kill receipts, admitted), S336 (arXiv 1808.04849,
  rejected as the wrong paper). Registry `256 → 259`; census before `souji ok` EXIT 0 (88 lines), after `souji ok`
  EXIT 0 (`census/round-84/records/sources-census-before.txt`, `…-after.txt`).
- Docs landed: `corpus/knowledge/own-tree-pointer-binding.md` r84 section, `corpus/knowledge/gate-signal-handling.md`
  r84 section, `corpus/QUALITY.md` Q154/Q155 under a new `## Round 84 criteria`, `corpus/README.md` r84 frontier
  block, `plans/round-84.md` A0-A6, `corpus/lessons/round-84.md`, `SCORECARD.md` r84 rows + capability rows +
  planned r85.
- r83 spot-check defects answered: D1 (SOURCES `252 → 256`, corrected in LOG), D2 (`## Round 23 criteria` restored
  in P), D3 (`b0a5b662…` superseded-by `72a405f2…`, corrected in LOG), D4 (seat-delivery sentence corrected in
  LOG), D5 (whole-file re-check in every stat read; unrowed — A2), D6 (wave seat reports force-added with the
  round).
- Sentinel clause coverage: `S84Sentinel.md` F1/F2 dropped each MOVED-refusal clause of the counter and scored it on
  both populations — the **census-in-census** clause and the **last-component** clause are unbound by both, and a
  census-in-census-dropping mutant resolves a wrong file while both populations stay green (A10). The round's
  sentence is narrowed to the five clauses it certifies and the gap is routed.
- Sentinel kill scope on C2: F6 (a CLI whose comm holds a newline) is **fixed in the filed bytes** (`030fa10d`,
  `survivors=0`) and still open in `a33038e9`/`a810acaf`; F7 (the abort path's group kill can signal a process that
  joined the CLI's group) and F9 (TMPDIR inside the vault → no trap) are pre-existing since r81/r83 and routed.
- Critic: a 40-row subset kills the same 5/5 (A8); at F the lane tool still held the r83 bytes, so the claim's
  subject is the repair commit's bytes (A9).
- Wave: 12 seats, roles executor×3, scribe, scout×2, connector, reviewer, critic, mutation-tester×2, sentinel;
  attack 5/12 = 42 %; one connector; **12/12 seats settled with substantive output, 0 dead**
  (`w1-results.json`). Seat verdicts and the falsification ledger (12 rows over 2 claims and every attack seat) are
  in `.ufo/waves/round-84/claim-falsification.tsv`; every seat report and the receipts they cite are committed in
  the wave-evidence commit `a8e88b9c` (r83 D6). S84Critic's report file stayed a skeleton; its findings are in its
  final output (`agent://S84Critic`) and are recorded in the ledger (A8/A9). No seat was replaced or re-dispatched.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| instruments, populations, mutant set, controls, before receipts; QUALITY heading restore | r84 C1/C2 bullets | `bd2bbb12` |
| preregistration (F, alone) | r84 "Frozen round" line | `35d87842` |
| `tools/souji-vault-verify.sh` freeze-before-signal repair + its receipts, regressions and filed-byte mutants | r84 C2 bullet | `1f49b3a7` |
| knowledge sections, QUALITY Q154/Q155, S334-S336, lesson, plans A0-A6, SCORECARD rows | r84 Sources/amendments bullets | `4557fc71` |
| README frontier block, LOG entry, A10/lesson-M7 narrowing | r84 docs bullets | `56a95d62` |
| wave evidence: spec, dispatch, ready, registry, results, ledger, 12 seat reports and receipts (r83 D6) | r84 wave bullet | `a8e88b9c` |

## Before → after measurements

**C1 (calibration).** Counting command (both ends run by the L1 and re-derived by S84ExecC1 and S84Reviewer):

```
python3 -B census/round-84/c1-clause-battery.py --counter census/round-84/c1-pointer-counter.py \
  --work <empty dir outside /tmp> --only r84 --expect-killed 5        # after
  … --only r83                                                        # before
```

| end | observed | receipt | measured commit |
|---|---|---|---|
| before | pristine `rows=36 mismatches=0`, five mutants `killed=no`, `killed_r83=0`, EXIT 0 | `census/round-84/controls/c1-before-r83-population.txt` | `bd2bbb12` |
| after | pristine `rows=44 mismatches=0 errors=0`, `killed_r84=5`, EXIT 0 | `census/round-84/records/c1-after.txt` | `1f49b3a7` |

The claim certifies **five named clauses**; it does not certify the counter's whole rule — the sentinel's per-clause
battery (A10) shows the census-in-census and last-component clauses unbound by both populations, and the round says
so in its knowledge section, Q154, lesson M7 and routed list rather than in a wider sentence.

**C2 (operability).** Counting command:

```
python3 -B census/round-84/c2-late-fork-counter.py --tool <candidate> --work <empty dir outside /tmp>
```

| end | observed | receipt | measured commit |
|---|---|---|---|
| before | r83 tool `72a405f2…`: `rows=22 mismatches=2 errors=0 orphans=2` (l1, l2; 1 survivor each), EXIT 1 | `census/round-84/controls/c2-before-r83-tool.txt` | `bd2bbb12` |
| after | filed tool `030fa10d…`: `rows=22 mismatches=0 errors=0 orphans=0`, EXIT 0 | `census/round-84/records/c2-after.txt` | `1f49b3a7` |

No owned axis score changed (calibration 7, coverage 8, operability 8 — the lane has no reproducible 0–10 mapping);
both rows carry the verdict, the counting command and the measured commit instead.

## Sources & frontier

`SOURCES.md` rows before → after: `256 → 259` (counting command
`grep -cE '^\| *S[0-9]{3,}' corpus/SOURCES.md`; pins in the census files). Census command and exits:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
before: 88 lines, last line `souji ok …/corpus/SOURCES.md`, EXIT 0   (census/round-84/records/sources-census-before.txt)
after:  88 lines, last line `souji ok …/corpus/SOURCES.md`, EXIT 0   (census/round-84/records/sources-census-after.txt)
```

- Rows added by tier: **A** 2 (S334 `docs` signal(7); S335 `own-work` clause-kill receipts), **B** 1 (S336
  `paper`, rejected), C 0.
- Rows touched old→new: none — no existing row's cells were rewritten (append-only).
- Frontier rows advanced: two new `### Frontier (r84 …)` bullets in `corpus/README.md` (the false-row population;
  the frozen CLI tree), each with its knowledge pointer, receipts and limits.
- `Assimilation: none` — no shokuknow theme taken; `considerthese/` does not exist in this lane.
- Gate: S334 opened (sha256 + decompressed lines 406-407, quote "SIGSTOP ... cannot be caught, blocked, or
  ignored."), S335 opened (its own SUMMARY line), S336 rejected (the fetched abstract is a healthcare data-science
  paper, quote in the Gate) — all three in `corpus/lessons/round-84.md` `## Gate`.

## Trend verdicts

- **expansion: unchanged** — the registry gains three rows (one rejected) and the knowledge base two sections on
  ground the coverage map already holds; no new kind of surface entered, `PROVINCE.md` unchanged, and the round's
  gain is instrument power and one tool path, not breadth.
- **quality: improved** — measured: the population that certifies the pointer counter now kills five clause-blind
  mutants it previously passed (0/5 → 5/5, both pristine arms green), and the vault tool's signal path leaves no
  survivor on the two late-fork rows that the r83 bytes left one each, inside the same 5 s settle, with selftest
  57/0, r17 37/0/0 and probe D 4/0 on the filed bytes. Two clauses of the repair are unrowed and are stated as such
  (A1/A2) rather than claimed.
- **discernment: improved** — the wave falsified parts of the round's own wording before filing (A1 the second map
  pass, A2 the whole-file re-check, A5 the substrate of two seats' findings, A7 NF-Q's missing kill, A8 the
  non-minimal population, A9 the claim's subject at F, A10 the two unbound clauses), the pre-file ledger carries
  twelve rows over two claims and every attack seat, and the round's do-nothing arms (36-row population, r83 tool
  bytes) are committed receipts rather than assertions. The sentinel's census-in-census finding is the round's most
  valuable result — a wrong-file resolution that both populations certified green — and it is filed as a narrowing,
  not smoothed over. Two seats scored a mid-write reference and their survivor counts do not reproduce on the filed
  bytes; that is recorded too.

## SHONEN

- `[~]` SKILL.md decision tables/error patterns/checklists/cited sources — pointers: SKILL.md gate registry rows,
  `corpus/SOURCES.md` S334/S335, `corpus/lessons/round-84.md` `## Gate`.
- `[~]` At least one end-to-end domain task logged in LOG.md — pointer: LOG.md r84 entry (population battery + vault
  signal path on this round's own receipts).
- `[~]` Instructions executable by an agent without oral context — pointer: the two frozen counting commands in
  `census/round-84/preregistration.txt`, re-run by S84ExecC1 and S84Reviewer.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — pointer: `git diff 54709d0d..HEAD -- PROVINCE.md`
  empty; S84Connector §2 (sibling overlap reported, nothing absorbed).

Stale-lane: respawn-per-round driver (hyaku-inline); no other mission of this lane is open. Tool installs: none (no
pacman, uv, npx, binary fetch, sysctl or sudo — the pacman pause was respected).
