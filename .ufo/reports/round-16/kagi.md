# kagi — round 16 (adjacency 8 → 9)

Lane: kagi (secrets & vault ops). Repo: `/home/vgpnk/projects/shokunin/kagi-shokunin`
(commit `round-16`, pushed to `VeigaPunk/kagi-shokunin`).

Axis moved: **adjacency** — at the round-15 close operability, freshness and
calibration stood at 9 while **depth, coverage and adjacency were tied at 8**. The
lane rule is "pick the lowest-scoring axis"; adjacency was the only 8 with **no
mechanical support at all** — it lived in the `corpus/README.md` overlap table,
two `PROVINCE.md` refusals, and one `mode = -` census row. Depth's remaining
increment is refusal-bound (needs a resolved vault reference) and coverage's is an
ownership decision (breadth over *shared* dirs), so the tie broke on "which 8 can
this lane make falsifiable this round without vault contact".

## Before → after

| | before (`HEAD` `587fda0`) | after (round 16) |
|---|---|---|
| ownership | prose in 3 places; no gate read an owner, a claim or a basis | `corpus/adjacency.tsv`: 5 `# own` prefixes (27 of 35 census rows), 4 group rows covering the other 8 (owner / status / claim / basis / token) |
| a foreign surface | nothing fired | `FOREIGN` (uncovered shared row), `ORPHAN` (a group covering nothing), `OWN-UNLISTED` (an `# own` prefix that names no declared surface) |
| a stale owner citation | `corpus/README.md:76` cited `kake-shokunin/SKILL.md:104-107` for the musketeer lease; that slice matches `musketeer` **0 times** (`:161` is the claim) | `STALE-BASIS`, exit 1 — and the README was corrected in the same commit |
| the profile/manifest boundary | prose ("pins only the manifest, never the profile") | R7 claim↔mode biconditional: `presence-only` ⇔ census `mode = -`, either direction `OVERCLAIM` |
| a basis that escapes its root | unread (a `../../` path would have been `sed`-read) | `BASIS-ESCAPE`, exit 1 |
| the gate's own proof | n/a | `--selftest PASS (43 cases)`, `--falsify PASS (caught=9/9 failed=0)`, `--map` 35 rows |
| the number | no measurement | `ADJACENCY_SCOPE: CLEAN (census=35 owned=27 shared=8 groups=4 owners=4 unresolved=1 contested=1 escapes=0 inbound=0 foreign=0 orphans=0 stale_basis=0 basis_escape=0 own_unlisted=0)` exit 0, ~0.5 s |

## The pre-state (measured, three ways where it mattered)

- Ownership: `ls corpus/*scope*` ⇒ nothing; `grep -rl 'adjacency' corpus/*.sh` ⇒
  nothing; the three prose places named above.
- The stale citation: `sed -n '104,107p' kake-shokunin/SKILL.md | grep -c musketeer`
  ⇒ **0**; `sed -n '161p' … | grep -c musketeer` ⇒ 1. Independently reproduced by
  the reviewer, the connector and the sibling scout.
- The partition: 35 census rows, 4 `# scan` dirs; 8 rows outside every
  domain-owned path (4 `~/.config/opencode`, 3 in the musketeer profile, 1
  `~/.agents/AGENTS.md`); one `mode = -` row. Owned/shared = 27/8 by
  prefix-containment, recomputed independently by the data executor's own harness
  (`census_rows 35 owned 27 shared 8`, group coverage `4 / 1 / 2 / 1`,
  `orphan_rows []`, `uncovered_shared []`) — and that independently derived data
  file passes the landed gate with the same CLEAN line.

## What landed

`corpus/scope-gate.sh` (`verify` | `--map` | `--selftest` | `--falsify`; R1–R11;
env overrides `ADJ_DATA`/`ADJ_CENSUS`/`ADJ_HOME`/`ADJ_BASIS_ROOT`/`ADJ_LANE_ROOT`/
`REALPATH_BIN`) + `corpus/adjacency.tsv` + `corpus/knowledge/adjacency-scope.md`
(`Reverify: R16-01..06`; 7-column schema, the rule table with a failing input
each, verdict/exit table, **14 bounds**, 11 falsifiers) + `corpus/lessons/round-16.md`
+ six ledger rows `R16-01..06` + the README overlap table/coverage map
(now machine-checked) + `PROVINCE.md` (gate registered) + a SKILL.md
decision-table row + both round-16 scorecard sections + a round-15 corrigendum.

Rules fail closed on: `BAD-ROW` (schema, 8th column, fused line, duplicate
group/census row, duplicate directive, unknown directive, token with a URL
scheme), `FOREIGN`, `ORPHAN`, `UNKNOWN-OWNER` (the literal set, so a directive
cannot widen the vocabulary), `BAD-VALUE`, `OWNER-MISMATCH` (a `lane:` basis must
name the row's owner), `NOT-A-FILE`, `STALE-BASIS`, `BASIS-ESCAPE`,
`OVERCLAIM`, `FOREIGN-SCAN`, `ESCAPE`, `INBOUND`, `UNVERIFIED`, `ENUM-CLASH`,
`OWN-UNLISTED`. Declared and **exit-neutral**: `unresolved` (the arbiter is
named), `contested`, `ADJACENCY_ABSTAIN` (a `runtime` row legitimately absent),
`ADJACENCY_ASSET_ABSENT` (named, not silent — absence of an `asset` is the
census's `GONE` claim).

## Evidence (shipped revision)

```
bash corpus/scope-gate.sh
  ADJACENCY_ABSTAIN: rows=1
  ADJACENCY_SCOPE: CLEAN (census=35 owned=27 shared=8 groups=4 owners=4 unresolved=1
    contested=1 escapes=0 inbound=0 foreign=0 orphans=0 stale_basis=0
    basis_escape=0 own_unlisted=0)                                    exit 0, ~0.5 s
bash corpus/scope-gate.sh --selftest  ⇒ SCOPE_SELFTEST: PASS (43 cases)   exit 0
bash corpus/scope-gate.sh --falsify   ⇒ SCOPE_FALSIFY: PASS (caught=9/9 failed=0) exit 0
bash corpus/scope-gate.sh --map       ⇒ 35 SCOPE_MAP: lines (27 owned / 8 shared)
env PATH=/nonexistent /usr/bin/bash corpus/scope-gate.sh ⇒ SETUP line, exit 2
# siblings unchanged
DRIFT_PINS: CLEAN (files=15 symbols=20) · SURFACE_CENSUS: CLEAN (assets=20 runtime=15
scanned=4 ok=34 absent=2 skipped=0) · CHECKLIST_RUN: CLEAN (items=16 runnable=9
by_hand=7 failed=0) · CLAIM_LEDGER: CELL_AUDIT / DOC_AUDIT / CITATION_GATE green
```

`--falsify` runs nine mutations against **the shipped data + census** in `mktemp`
copies (the repo is never written): the stale kake basis, a foreign census row, a
drifted claim, a `# scan` over a shared dir, two prefix-creep variants, an `# own`
over an undeclared tree, `..` traversal in a basis, and a clean-looking `lane:`
citation whose lane root is a symlink out of the lane tree.

## Defects this round found in its own first implementations

Nine in the gate, plus three in the verification harness that was supposed to
catch them — the harness defects are the more instructive half:

1. `local rest="${cur#lane:}" lname="${rest%%/*}"` — bash word-expands the RHS
   before assigning under `set -u` ⇒ every `verify`/`--map` run died with **no
   verdict line** (scribe lane, exact repro).
2. `token_hits` defaulted an unanchored citation to line `1-1` ⇒ 3× `STALE-BASIS`
   on a correct data file (selftest).
3. Selftest fixtures were mutated rather than rebuilt ⇒ a symlink leaked into the
   next case; 11/29 false failures (selftest).
4. R9 compared an owned row against its *own* prefix and resolved the prefix
   through the same symlink ⇒ an anchored escape stayed CLEAN (reviewer).
5. A dangling symlink "resolved" (`readlink -f` canonicalizes a non-existent
   leaf) ⇒ CLEAN on a path whose target did not exist (selftest).
6. `--falsify` was defined and never wired into the parser/dispatch (scribe) —
   dead code at every revision that lane observed.
7. `--falsify` run 1: both data files end **without a trailing newline**, so
   three appended mutations merged into the last row and silently no-opped.
8. `--falsify` run 2: `mutate_case` counted successes but not failures, so the
   summary printed `PASS (caught=7/7)` **above** a `FALSIFY FAIL` line — the
   repo's own swallowed-verdict class, inside the verifier.
9. The EXIT trap referenced a function-local `R` ⇒ `R: unbound variable` after
   `falsify()` returned.

## The L2 wave (14 lanes, one batched dispatch)

planner, connector, 2 scouts, scribe, 2 executors, reviewer, critic, sentinel,
labrat, mutation-tester, simplifier, distiller — every route bucket used
(planner/connector @m_lunamax; executor/scribe/scout @m_flash;
reviewer/critic/sentinel/labrat/mutation-tester/simplifier/distiller @m_zfl).

| Lane | What it produced (with executed evidence) | Disposition |
|---|---|---|
| planner | R2 is classification, not a guard; absent rows need a runtime-only reading; a cited range matches ANY line | all three landed (`ASSET_ABSENT`, labels, documented range semantics) |
| connector | no sibling implements a host-path ownership map with a fail-closed foreign-claim gate; kake is the adjacent beneficiary; `README.md:76` resolves to text but not to the claim | adjacency evidence; nothing absorbed |
| scout (sibling) | the four landed bases resolve; the **pre-delta NMH basis matched a launcher line** (`(musketeer-chrome &)`) — the README:76 decay caught in the act; 4 fleet claimants for `~/.config/opencode`, no recorded owner | NMH row re-based with owner `kagi`; the launcher case became bound 6 |
| scout (host) | no ESCAPE/INBOUND can fire today; 0 symlinks in the declared set; **both data files lack a trailing newline**; `~/.local/bin/musketeer-chrome` (kake) and the profile's `SingletonSocket` are symlinks R9 cannot see | newline class landed in the entry + `--falsify`; the two symlink classes reported |
| exec (gate) | full draft + its own D1–D8 defect log | bootstrap SETUP guard landed from D4/F4 |
| exec (data) | independent partition derivation, identical everywhere; `# own $HOME/.local/bin` type variants CLEAN while claiming 116 foreign children | the numbers are why R10/R11 exist |
| scribe | entry + lesson drafts; found the unwired `--falsify`; found the `uniq -d` contradiction | drafts landed with corrections; both findings fixed |
| reviewer | all counts reproduced (35/27/8/4/4); D2 creep proved; double-counting advice | `R16-01` pins the partition, `R11-11` keeps the row count |
| critic | CE-A1 invented ownership ⇒ CLEAN; CE-C foreign symlink below an owned non-scan dir ⇒ CLEAN; the exact stale citation ⇒ `STALE-BASIS` | CE-C closed by R11; CE-A1 recorded as bound 1; the citation became falsify mutation 1 |
| sentinel | S1 `basis` traversal (private-byte oracle, `../../.config/the-janitor/op.env` reachable), S2 creep, S3 token echoed | S1 ⇒ `BASIS-ESCAPE`; S2 ⇒ R10/R11; S3 ⇒ token hygiene |
| labrat | safe prefix idiom, `realpath -m` fail-open, timings, `uniq -d` empty exits 0 | idiom landed; `-m` never used; `uniq -d` correction landed |
| mutation | 25 mutants / 14 killed at that revision, survivors listed with reasons | every survivor except the token-relevance bound is now caught |
| simplifier | no production rule should be deleted; literalize the status/claim sets; keep a separate gate | literalization landed; the `--scope`-merge proposal recorded as open |
| distiller | 13 reports, 19 unique moves, 4 explicit contradictions, 1 evidence-free claim | contradictions adjudicated one by one; the TODOs are gone |

## Corrigendum (measured, not inferred)

`corpus/lessons/round-15.md` attributed part of its first silent death to
"`uniq -d` exits 1 on an empty result". Measured in round 16 on this host (GNU
coreutils 9.x): `printf '' | sort | uniq -d` ⇒ exit **0**. The class is real — the
loop's final iteration status and `grep -v … | tail -1` under `pipefail` both kill
the script — but the attribution was wrong and would aim a future fix at the
wrong line. Corrected in place with a pointer; recorded in the round-16
calibration cell.

## Bounds (why 9, not 10)

State the ceilings in the same breath as the score:

- **Ownership truth is a governance fact.** The gate checks that a claim is
  declared, consistent and cited — never that it is *true*. An invented foreign
  census row plus an invented group row with a plausible owner and a
  token-matching basis still passes (critic CE-A1: `census=36 owned=27 shared=9`,
  CLEAN). Adjudication stays with the integrator.
- **`token` is a floor, not a relevance proof** (the launcher-line counterexample),
  and a citation written inside a `note` is checked by nobody.
- **The census is the universe**; a surface no row names is invisible, and
  enumeration is one level deep over 4 dirs.
- **`realpath` is the only link test**: hardlinks, bind mounts, and
  foreign→foreign links are out of scope; an unreadable middle component reads as
  absent.
- **Nothing schedules this gate** (operator scope, unchanged).
- **The summary line carries fields the broadcast contract did not** — the fields
  are pinned by `R16-01`, the prose is not the contract.

## Adjacency (reported, not absorbed)

- **`$HOME/.config/opencode` ownership ruling is still owed.** kotoba (24 files),
  kama (14), kengaku (9, incl. a temporary provider write restored byte-identical)
  and kumitate (2) all have artifacts in it; `PROVINCE.md` claims 4 of its
  children for this lane's handler path. Declared `unresolved` with `integrator`
  as the arbiter, and the fleet ledger entry D-96 already asks for "a routed owner
  or an explicit operator disposition".
- **Musketeer chrome profile / CDP-9222 lease** — contested in writing on both
  sides (kake `SKILL.md:161`, kake `corpus/lessons/round-1-aggregator-audit.md:72-75`
  naming kagi as the rival claimant; `ROADMAP.md:130-131` adds that the lease is
  "serialization, not an ACL"). The host **main repo** holds the arbitration
  record; this lane declares the profile `contested` / `presence-only` and pins
  nothing but the NMH manifest it writes.
- **Two symlink classes R9 cannot see** (reported to the integrator): kake's
  `~/.local/bin/musketeer-chrome` launcher symlink sits inside the shared bin dir
  (105 children, 2 owned), and the contested profile subtree carries a
  `SingletonSocket` symlink that leaves `$HOME`. Both are outside the census-row
  universe by construction — the census reports `LINK` for any symlink it
  declares, and neither is declared.
- **Routed defect (same class, another gate):** `corpus/surface-census.sh:75`
  shares the bootstrap silent-death class that round 16 fixed in
  `scope-gate.sh` (an unresolvable script dir exits 1 with no verdict line, i.e.
  a broken environment is indistinguishable from "drift found"). The one-line
  guard was not applied there this round because the round's axis-move is
  adjacency; it is routed, not silently shared.
- **Cancelled lane:** `ExecGateR16` was settled; `ScoutSibR16`/`LabratR16`
  re-readable at `history://…`.

## Hygiene

No vault access, no `op` item read, no `op.env` bytes into any artifact, no
handler start/stop, no Chrome launch. The only file-content reads are `sed -n`
over cited `basis` lines, bounded by a containment rule added this round after
the sentinel proved the unbounded version was a private-byte oracle. All L2
execution was scratch-only under `/tmp/kagi-r16/`; the only writes were this
repo's own files.

## Next target (recorded in `SCORECARD.md`, falsifiable)

Round 17 faces **depth 8 / coverage 8** tied. Named targets: for coverage, a
per-group breadth declaration (`ADJACENCY_BREADTH: children=N declared=M
undeclared=K` — today `~/.config/opencode` 20/4, `~/.local/bin` 105/2,
`~/.agents` 4/1) pinned in a ledger row; for depth, re-measure the standing
"needs a resolved reference" refusal, as round 12 taught. The round-15 target
(the checklist `--mutate` mode) **stays open and unclaimed** — operability is at
9, so the lowest-axis rule did not reach it.