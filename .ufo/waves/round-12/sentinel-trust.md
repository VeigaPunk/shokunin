# Sentinel — trust boundaries in the closure evidence chain (round 12, protocol lane)

Axes: fleet-meta / gate-integrity. All probes read-only; this file is my only write.
Facts re-executed this session (20:36–20:47 -03): `wc -l .ufo/watchdog.log` → **200** (brief
said 199 — one tick line grew); per-lane counters match the brief exactly; HEAD `6d27283` —
**aggregator r8 landed `6d27283` 20:32:43 mid-audit** (round-7 report + ledger refresh 5 +
SCORECARD/LOG r7 sections), so `.ufo/reports/round-7/aggregator.md` is now tracked and off
the durability-commit list; 4 untracked files remain (2 prompts, kengaku-DRAFT, r12/kotoba).

## Spoofable inputs

Ranked by exploitability (lane- or subagent-writable → flips own status to `ok`, or a
sibling's to `failed`):

1. **Report paths — CRIT.** The driver's completion signal is bare existence:
   `report_of()` = `[ -f … ]` (`scripts/shokunin-watchdog.sh:44`, read this session). Any
   lane or spawned subagent can write a 101-byte marker at a sibling's report path — the
   precedent is committed: `0a30b44` "fleet-1 closeout markers" (operator identity,
   17:51:04) carried the round-8/kengaku.md marker that advanced kengaku 8→9 on no work
   (PROTOCOL.md appendix "Marker vs report"). Main-repo write scope is convention-only;
   sibling scopes are unenforced. Exploit: a content-shaped report naming real sibling
   commits survives every check except independent re-derivation.
2. **`.ufo/watchdog.log` — WARN.** Mutable, driver-appended; last committed by
   `shokunin <shokunin@local>` at `609ecb6` (`git log -1 --format='%an'`), churning
   untracked since (83 working-tree insertions). Any lane can append a forged
   `complete <lane> round=N` or delete lines. Mitigating structure exists: step 4 requires
   the committed timestamp+text digest, not the live log, as the resolvable pointer.
3. **`.ufo/state/*` — WARN.** Churns every tick (all 16 files modified, untracked runtime
   since `609ecb6`); `round_of()` (`:43`) is an unvalidated `cat` and the driver itself
   writes the counter. A lane editing its own counter changes what "dispatched for N"
   means. Corroboration: committed `.ufo/prompts/<lane>-round-N.md` + a digest launch
   line — a counter with neither is spoofable.
4. **`MANIFEST.json` `rounds[]` — WARN.** Integrator-only by convention; anyone with tree
   access can append a `closure-correction` flipping own `failed`→`ok`. But corroboration
   is strong and external: every `ok` row is falsifiable by the derivable report path +
   ancestry; `failed` by absence; `in-flight`/`not-dispatched` by dispatch/complete lines
   + launch timestamps. A forged row contradicts ancestry and is detectable — which is why
   report-content spoofing outranks it.

Strong corroboration (checker MUST prefer): commit ancestry, `git log --diff-filter=A
--format='%an <%ae>'` identity, committed prompts, committed digest. Weak: log lines,
counters, report prose. Never accept "report exists" as `ok` without marker screen +
SHONEN grep + ancestry — step 1 as code, not hand-run.

## Durability-commit hazards

Live-race surface narrowed: aggregator r8 self-landed round-7 (`6d27283`, 20:32:43), so
only **kotoba r13** (launched 20:28:23, live) owns an untracked target
(`.ufo/reports/round-12/kotoba.md`).

1. **Concurrent same-path commit.** The on-disk r12/kotoba report (225 lines) is the
   lane's to commit under `kotoba-shokunin` identity; a protocol-identity commit burns
   attribution permanently (history is never rewritten; defect recorded — `3ea42cb`
   precedent). Worse: the on-disk bytes predate kotoba's own child commit (`71963e6`,
   20:28:20) and carry the literal placeholder `LANE_HASH` (kotoba report, Artifacts
   section) — committing now imports a placeholder into a permanent object. kotoba r12's
   mission IS terminated (`complete kotoba round=12` 20:28:22), so a sweep is
   protocol-consistent — but its r13 respawn may re-file the same path, as it did for
   round-11 (`f9dcfd2`).
2. **Staged-but-unwritten file.** `git commit -- <path>` on an unstaged path errors
   (`pathspec did not match any file(s) known to git` — re-executed in a scratch repo);
   `git add` first, and a broad add in this tree (kake's dirty round-13 report,
   l0-questions edits, 16 state files, watchdog.log) is the D-51 sweep hazard (kagi
   `ade32e4` swept AGGREGATE.md + an l0 line). Also tested: a staged-but-excluded file
   **survives** `git commit -- <other-path>` (still staged `A`) — a loaded index left
   for the next actor is one `commit -a` away from firing.
3. **Index lock contention.** Concurrent commits fail with `index.lock` exists —
   transient, retryable, not corruption; the hazard is an unscoped retry after the
   failure. One command, pathspec from the start, no wider-scope retry.
4. **Attribution consequence.** Any report under `protocol-shokunin` identity is no
   longer "landed by the lane"; §Invariants says record the defect, never rewrite.

**Recommendation: commit the two prompts only; defer both reports.**
- Prompts: `git add .ufo/prompts/kotoba-round-13.md .ufo/prompts/protocol-round-12.md &&
  git -c user.name=protocol-shokunin -c user.email=protocol@shokunin.local commit --
  .ufo/prompts/kotoba-round-13.md .ufo/prompts/protocol-round-12.md` — exact pathspecs,
  lane identity per §Invariants, one command, no `-a`. Both are 11-line driver-generated
  dispatch evidence for live missions (untracked prompt = non-durable dispatch evidence).
- `round-12/kotoba.md`: do NOT commit — placeholder bytes, live successor may re-file
  (round-11 respawn precedent). Route to kotoba r13's report contract; if it doesn't, the
  round-13 pass sweeps with the attribution defect recorded — same durable outcome.
- `kengaku-DRAFT.md`: never commit. Template with unfilled `{{TOKEN}}` placeholders by
  design ("every double-brace token is unfilled by design", DRAFT fill rule) — committing
  fabricates a landed report at a non-contract path. Kengaku owns its real report.

## Secret screen

**Clean.** `gitleaks`/`trivy`/`semgrep` not installed (`command -v` → nothing); grep used.
Classes: `op://`, `xoxb-`, `sk-`, `ghp_`, `github_pat_`, `AKIA`, `BEGIN .* PRIVATE KEY`,
`Bearer `, `password`, `token=`, plus `api[_-]?key|secret`. Grep exit 1 (zero hits) on all
five candidates — `.ufo/prompts/kotoba-round-13.md`, `.ufo/prompts/protocol-round-12.md`,
`.ufo/reports/round-11/kengaku-DRAFT.md`, `.ufo/reports/round-12/kotoba.md`,
`.ufo/reports/round-7/aggregator.md` — and on `.ufo/waves/round-12/` (empty at 20:39).
Adjacent committed artifacts re-screened: `.ufo/waves/round-11/` census/verifier clean.
Kagi-corpus `op://` references (round-2…9 reports, `AGGREGATE.md:102,626`) are all
redacted/schematic — scheme token in prose or pattern context, no plaintext tails
(`AGGREGATE.md:626`: 70 hits are "prose/schematic placeholders or the sweep pattern").
The kagi r10 prefix-match defect (`.ufo/l0-questions.md:4`) affects kagi's own tool
output, not these files. **No live secret found or quoted.** Caveat: pattern-based only —
a prefixless blob would pass (see Gaps).

## Gate-standard abuse

Audited all six live sibling gates (read this session): `kengaku-shokunin/grader.py`
(936 L), `kotoba-shokunin/verifiers/verify_harness_claims.py` (670 L) +
`verify_corpus_independent.py` (776 L), `kumitate-shokunin/scripts/round-gate.mjs`
(1426 L), `kagi-shokunin/corpus/transcript-scan.sh` (282 L) + `drift-pins.sh` (451 L),
`kake-shokunin/scripts/probe-delta.mjs` (159 L). Today: **no outbound surface** — zero
network classes across all six (round-gate.mjs is array-argv `spawnSync('git',…)`,
`:188` "no shell interpolation anywhere in this file"; kotoba/kengaku subprocess is
array-argv git or self-reinvocation; kagi gates are local sqlite/mktemp; kake reads a
local jsonl). Kagi selftest `op://` strings are declared-fake scratch fixtures
(`transcript-scan.sh:202,242`). Kengaku's endpoint harness (`probe_r11.py`,
`127.0.0.1:34113`) is not its gate — grader.py verifies committed bytes only.

Loose-writing abuse paths the standard must close:
1. **Registry-as-launch-list.** `fleets/registry.json` is contested scope (ledger D-86,
   `AGGREGATE.md:744`) and names lanes/missions — a "registry well-formedness" gate that
   writes or launches from it is an automation surface. Boundary: a gate READS its repo
   (scoped siblings when named) and PRINTS a verdict; never launches/completes/mutates
   missions, never touches `.ufo/state/`, `watchdog.log`, or the driver.
2. **Selftest reaching the network.** An "endpoint health" selftest is an outbound probe
   laundered as a gate. Boundary: selftests hermetic (scratch fixtures, as kagi/kotoba
   already do), fail-closed on missing environment, never construct network clients.
   Evidence-standard hook: "A status command printing configured values is not evidence
   of capability" — a gate never stands in for the probe it refuses to run.
3. **Exit-code map as covert channel.** Divergent maps (kotoba `3=no-baseline`,
   `verify_harness_claims.py:662`; kake `probe-delta.mjs` 2/64) make exits
   uninterpretable fleet-wide, and a nonstandard code on attacker-chosen input is a
   signal channel to anything scripting the gate. Boundary: fixed 0/1/2 semantics,
   expected values pinned in-repo (§Drift pins: "a pin only counts if its expected
   values are persisted inside the repo"), no private exit codes.
4. **Gate fleet-index.** A shared list of gate paths is executable-on-read
   infrastructure. Boundary: gates repo-local, self-declared, cited by hash, never
   fetched or enumerated.

Clause for the standard: *a verdict gate reads committed bytes and local fixtures and
exits 0/1/2 with in-repo pinned expected values; it performs no network I/O, launches no
mission, mutates no driver state, and no selftest substitutes for an operator-owned probe
(local-first, §Invariants; evidence standard as quoted).*

## Mitigations

1. **`.ufo/waves/round-12/` — `closure-check.sh` (committed):** the executable closure
   gate. Inputs: `MANIFEST.json`, `rounds[]`, report tree, `--diff-filter=A` identities,
   `merge-base --is-ancestor`, committed digest (never the live log). Checks: marker
   screen (size + content shape), SHONEN grep, ancestry per cited hash, report-commit
   identity vs lane identity, last-wins re-derivation vs rows. Exit 0/1/2, expected
   values pinned in-repo (round-11 baselines: 22 entries, 73/4/4/23). Directly
   de-risks Spoofable #1/#4 and is the round's own axis-move deliverable.
2. **PROTOCOL.md §Invariants (lane-identity bullet):** a lane committing outside its own
   pathspec set — durability sweeps included — records affected paths + attribution
   consequence in round notes before committing, and never sweeps a report whose
   lane-round is live (round-11 practice, now written down). Tightens D-51/D-56.
3. **PROTOCOL.md §Invariants (lane-authorship bullet):** `.ufo/waves/round-<N>/` seat
   files adopt the child-repo rule in the main repo — L1 commits L2 artifacts under lane
   identity, pathspec-limited to the wave dir + named writes. Kills the third-identity
   class (26 `shokunin <shokunin@local>` report commits, round-11 §Conformance 1).
4. **PROTOCOL.md step 4 (dispatch-evidence bullet):** `.ufo/state/*` counters are never
   dispatch evidence alone — committed prompt + digest launch line, else not citable.
5. **PROTOCOL.md §Evidence standard:** any commit touching `.ufo/prompts/`, reports, or
   waves carries a same-session secret-pattern screen in the report (classes + exit
   codes). kagi's cmd_refs defect stays routed to kagi; this covers the committer's set.
6. **SCORECARD.md (gate-integrity):** new M12 = closure statuses re-derivable by
   `closure-check.sh` without the live log; target 0 contradicting rows.

## Gaps

- The checker does not exist yet this session; this audit defines its trust inputs and
  abuse boundary. I verified inputs' mutability and gates' cleanliness, not the script.
- Secret screen is pattern-based: a prefixless credential-shaped blob would pass; the
  seven-repo `git log -S` pickaxe sweep was not re-run this session (round-7 aggregator
  report `:622-626` records it clean to its cutoff).
- `semgrep --config auto` not run (not installed; config download is a network fetch).
- kasegi r14 / kake r14 / kengaku r11 / kumitate r11 / kagi r12 were live at 20:40:45 —
  their in-flight rows stay open past this session; their reports are outside my screen.
- `fleets/registry.json` not found under `/home/vgpnk/projects` (kasegi cites it in
  `ufo-fsd-alpha` paths outside my read window) — D-86 quoted from the ledger, file
  itself unverified.
- The "defer kotoba report" recommendation assumes the round-11 respawn re-file precedent
  repeats; if kotoba r13 files elsewhere, the closure pass sweeps with attribution defect
  — same durable outcome, timing unverified.

DESPAWN: gx-sentinel-closure — signal delivered. Send me shutdown_request.
