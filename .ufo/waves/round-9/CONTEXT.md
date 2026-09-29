# Round-9 aggregator wave — shared seat context (read this first)

Author: aggregator L1, round 9 (fleet-2), repo `/home/vgpnk/projects/shokunin`.
Written 2026-09-28T21:2x-03 at main HEAD `91d0178`. This file is seat input, committed as wave evidence.

## Goal — one axis-move: corpus review

All three aggregator axes (cross-lane quality, mint/dormancy calls, corpus review) are tied at **8** in
`SCORECARD.md` §Aggregator lane, so "lowest-scoring" is decided by debt, not by the number: CORPUS.md rule 10
(each round's review emits a verdict per repo) was **not** satisfied at refresh 6 — ledger §13.7 names it as owed,
and §11.1's six `not conformant` verdicts are now three refreshes stale, measured at HEADs that no longer exist.

The move: (a) re-emit **6/6** per-repo conformance verdicts at each repo's **landed** HEAD with re-executed
commands; (b) make those verdicts re-derivable by a committed gate conforming to `PROTOCOL.md` §Gate standard
(new at protocol round 12, commit `dddb4ec`); (c) discharge the round-8 residual by firming or breaking the three
provisional box-3 verdicts (kasegi, kake, kagi) at the lanes' landed HEADs — those verdicts are inputs to (a).

## Ground truth measured by the L1 (re-measure your own cells; these are for orientation)

Main repo `/home/vgpnk/projects/shokunin`:

| Artifact | State |
|---|---|
| `git log -1` | `91d0178` 2026-09-28T21:16:56-03:00 |
| `.ufo/reports/AGGREGATE.md` | 1498 lines; §11 refresh 4 (round 6), §12 refresh 5 (round 7), §13 refresh 6 (round 8) |
| `SCORECARD.md` | aggregator section starts at `## Aggregator lane`; round-8 metrics X1–X8; §Planned names the round-9 move |
| `LOG.md` | 276 lines; last entry `## Round 8 — aggregator lane …` |
| `.ufo/reports/round-8/aggregator.md` | this lane's round-8 report (15-seat wave digest, §SHONEN, §Next) |
| `PROTOCOL.md` | 514 lines; §Evidence standard L299, **§Gate standard L339**, §File contract L374, §Invariants L400, §Fleet-2 L453 |
| `CORPUS.md` | 57 lines; rules unnumbered (numbering below is the ledger's) |
| `MANIFEST.json` | `rounds` array, 30 entries; last two are protocol r12 closure corrections (`closed_at` 20:55 and 21:20 -03) |
| `.ufo/l0-questions.md` | 11 lines, 0 answer markers, clean vs HEAD (committed by protocol at `df1b2c6`) |
| round-8 refresh cutoff | **2026-09-28T23:46:28Z** = 20:46:28 -03 → the sweep window is everything after it |

Child repos (subdirectories of the main repo):

| Repo | HEAD | Tree | Note |
|---|---|---|---|
| `kasegi-shokunin` | `b7180b0` | clean, 0 unpushed | lane r14 landed; r15 **live** |
| `kengaku-shokunin` | `f09ff1f` | clean, 0 unpushed | lane r11 landed; r11 mission still live per state file |
| `kake-shokunin` | `4c9a985` | **dirty 5**, 2 unpushed | HEAD is an aggregator-identity commit; lane r13/r14 work uncommitted; r14 live |
| `kumitate-shokunin` | `e0e5de1` | clean, 0 unpushed | lane r12 landed (`round-gate.mjs --close` CLEAN); r12 live |
| `kotoba-shokunin` | `3ea0e08` | clean, 0 unpushed | lane r13 landed (`verifiers/verify_surfaces.py`); r14 live |
| `kagi-shokunin` | `4391b3b` | **dirty 20**, 3 unpushed | HEAD is an aggregator-identity commit; lane r13 live |

Fleet event: `~/Projects/bounties` is **GONE** from the filesystem (`ls -d ~/Projects/bounties` → No such file or
directory; kasegi r15 filed it to `.ufo/l0-questions.md`). It was kasegi's `PROVINCE.md` root and the anchor of
~376 `SKILL.md` path citations. `PROTOCOL.md` §File contract requires a lane that finds a surface moved or absent
to correct `PROVINCE.md` to the real path and log the correction.

Live missions right now — never edit their files: kasegi r15, kumitate r12, kagi r13, kotoba r14, protocol r12,
kake r14, kengaku r11.

## CORPUS.md rule numbering (canonical for this round)

`CORPUS.md` does not number its bullets; the ledger's verdicts cite numbers (§11.1 "not conformant — 4, 5, 7, 9").
This table is the mapping a non-author needs; the gap itself is a routed defect (a verdict citing "rule 4" against
an unnumbered contract file is not re-derivable).

| # | Rule | `CORPUS.md` line |
|---|---|---|
| 1 | `knowledge/` entries cite a source: file path, command output, or URL | 18 |
| 2 | `lessons/` entries cite the round and the evidence (LOG.md round, commit, report) | 19 |
| 3 | A corpus entry is falsifiable or marked opinion; no unverifiable claims | 20 |
| 4 | A count carries its command — `<number> — <command> <date>` | 28 |
| 5 | A negative claim carries its sweep (the search command that produced the absence) | 33 |
| 6 | A quote names its location (frontmatter vs body, script vs installed skill) | 36 |
| 7 | An index row is a claim — write the row when the file exists, not before | 40 |
| 8 | No credential material, ever — secret values, tokens, cookies, `op://…` refs | 43 |
| 9 | Corrections are new entries, never rewrites; no lane edits another's corpus files | 47 |
| 10 | Each round's review emits a verdict per repo — `conformant` / `not conformant`, naming the failed rule and the command that shows it | 55 |

(Unnumbered lane-duty bullet at `CORPUS.md` L21: "The aggregator reviews every corpus each round and files gaps
as lessons." Aggregator-owned lesson naming: `corpus/lessons/round-<N>-aggregator-*.md`.)

## PROTOCOL.md §Gate standard (protocol r12, `dddb4ec`) — the clauses a gate must satisfy

- **Verdict**: `0` = `clean`, `1` = `failed` fleet-wide; every other code the gate exits is declared in its
  registry entry and mapped onto `clean | failed | could-not-evaluate`; an undeclared nonzero code reads as
  `could-not-evaluate`. The gate's inner vocabulary stays lane-owned.
- **Self-test**: a self-invocation mode over isolated fixtures (temp trees, no network, no live-tree write)
  asserting **both** the exit code and a stable expected finding-id, with expected values committed in the owning
  repo and independent of the recomputation. Flag spelling is the lane's; the registry records it. A helper-only or
  model-only self-check does not satisfy the clause.
- **Two evidences**: self-test green is capability, not measurement. A gate whose verdict depends on a mutable
  fleet artifact also ships a run over a **committed input snapshot** with its committed expected verdict. A
  verdict names the revision it was measured against.
- **Registry**: schema is §Gate standard's; **rows live in each lane's `SKILL.md`** — name, `gate|probe`, entry
  command, verdict map, self-test command + spelling, pinned-value path, write scope, owner. The aggregator ledger
  stays the routed-defect queue, not a second inventory; a fleet index is pointers to lane rows, never copied
  expected values. (Note: the two main-repo lanes have **no** `SKILL.md` — same class of gap as ledger D-120.)
- **Scope**: read-only over surfaces it does not own; never acts on an external surface; a verdict is lane-local
  evidence and never defines host runtime stop conditions.
- **Closure consequence**: a red gate is a conformance defect recorded in the round notes and routed to its owner,
  status-neutral. The integrator verifies a gate's committed evidence; it does not execute a sibling's gate.

## Seat contract (hard rules)

1. **Write scope = your own evidence file only**, at the path your task names under
   `/home/vgpnk/projects/shokunin/.ufo/waves/round-9/`. NEVER write inside a child repo; never touch
   `AGGREGATE.md`, `SCORECARD.md`, `LOG.md`, `MANIFEST.json`, `CORPUS.md`, `PROTOCOL.md`, `.ufo/reports/**`,
   `.ufo/state/**`, `.ufo/l0-questions.md`, `.ufo/watchdog.log`. The L1 mirrors lessons into child repos and
   lands every commit after the wave settles.
2. **No state-mutating git**: no `commit`, `add`, `push`, `checkout`, `stash`, `reset`, `clean`, `mv`, `rm`.
   Read-only only: `log`, `show`, `cat-file`, `ls-files`, `status`, `diff`, `rev-list`, `rev-parse`, `blame`,
   `archive` (extract into a temp dir under `/tmp`).
3. **No mutating host verbs**: no installers, no skill/CLI verbs that write shared manifests, no network or vault
   writes, no systemd toggles, no publishing. A decisive check that would need one → record it as
   `gated-without-artifact` with the would-be command and the gate that blocks it (ledger §13.1's three-outcome
   rule: `gated-with-artifact` counts as executed, `gated-without-artifact` does not).
4. **Evidence standard** (`PROTOCOL.md` §Evidence standard): every number carries the command you ran *in this
   session* plus its observed output; every absence claim carries the sweep that produced it; every quote names
   file and line. Anything not observed is labelled `[INFERENCE]`. A command printing configured values is not
   evidence of capability. Commits are cited by hash, never by subject or tag.
5. **Host caveat**: `grep` on this host is pi-uu-grep 0.2.0 — `-oE '[0-9]+$'` emits zero-length matches and some
   `-o` forms misbehave. Prefer `awk` / `python3` for extraction, and verify that a counting command reproduces
   its own observed value before publishing it (ledger proposal P-q).
6. **Dirty-tree rule** (round-8 critic ruling, absorbed): grading a dirty worktree measures the lane's in-flight
   edit, not the repo. For `kake-shokunin` and `kagi-shokunin` report **both** the verdict at the landed HEAD
   (`git show <HEAD>:<path>`, or `git archive <HEAD> | tar -x -C /tmp/…`) and what the worktree-only bytes would
   change, marking decisive worktree-only text `provisional`.
7. **Authorship**: a subagent the lane dispatched is still the lane (`PROTOCOL.md` §Promotion gates). Your verdict
   on this lane's own artifacts is therefore *not* non-author; say so where it matters.
8. **Output**: write your evidence file first — markdown, tables, every command with its exit code and observed
   value, plus a measurement stamp (wall time + main HEAD + child HEAD your cells refer to) — then return the
   terse JSON payload. The file is the durable evidence and will be committed. Do not run builds, linters,
   formatters, or test suites outside your own scope.
