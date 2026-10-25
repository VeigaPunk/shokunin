# kagi — round 11 (calibration axis-move)

Lane: kagi (secrets & vault ops) · axis owned: **freshness + calibration**;
this round moved **calibration 7 → 8** (lowest post-move cell). Repo:
`/home/vgpnk/projects/shokunin/kagi-shokunin`. Branch/commit: `round-11`.

## Move

Round 10 left three calibration facts, each checkable against the repo: the
round's 62 report claims were adjudicated **by hand** (49 VERIFIED / 9 STALE /
4 UNCHECKABLE) because none carried a command; two committed citations named
session-scoped scratch (`SCORECARD.md:54`, `corpus/lessons/round-10.md:50`) and
resolved for nobody; and the score cells were self-scored with prose pointers,
so a reader re-derived the evidence instead of re-running it.

Landed `corpus/claim-ledger.sh` — three classes, one gate:

- **revision** (`corpus/stamps.tsv`, 28 rows): `path sha256 lines bytes`; all
  four columns verified; regeneration is a reviewed `stamp` commit (no
  auto-re-pin).
- **claim** (`corpus/claim-ledger.tsv`, 11 rows): `id command expect exit
  timeout note`; a row passes only when the exit code matches **and** the
  expected ERE matches the **last non-empty output line**; the command must be
  one simple command (5-entry allowlist, no metacharacters, no backslash, no
  empty quote pair, no `bash -c`, no denied verb) or it is refused without
  running (POLICY, exit 2).
- **citation** (`citations`): every token on every line of the 39 committed
  Markdown docs, normalized (`:N`, `#anchor`, `?query`, `=value`, `'s`, quotes,
  parens) and classified by shape (`corpus/…`, root docs, `knowledge/`/
  `lessons/` shorthands, `<lane>-shokunin/`, `ufo/`/`.ufo/`, brace sets);
  `UNRESOLVED`/`EPHEMERAL` fail unless the citing line labels the token, in
  which case the token is **printed** as `LABELED` and counted.

## Measured before → after

| Claim | Before | After (shipped revision) |
|---|---|---|
| Round claims re-runnable | 0 of 62 carried a command (hand adjudication) | 11 ledger rows; `CLAIM_LEDGER: CLEAN (claims=11 stamped=28)` exit 0 |
| Revision a reviewer can name | prose ("HEAD"), in-flight files reviewed mid-edit | 28 stamped artifacts + a frozen r1 given to all 9 L2 lanes; 3 lanes independently hash-verified it |
| Committed-doc citations resolve | `BROKEN` on first contact: 3 `UNRESOLVED` + 2 `EPHEMERAL` (`cites=268 docs=37`) | `CITATION_GATE: CLEAN (cites=515 docs=39 unresolved=0 ephemeral=0 labeled=13)` exit 0 |
| Gate self-proof | no ledger selftest existed | `SELFTEST: PASS (39 cases)` exit 0 |
| Sibling gates | census verbs printed `CLEAN` even with zero probes passing | `SURFACE_CENSUS_VERBS: DEGRADED` + exit 1 (fail-closed); `DRIFT_PINS: CLEAN (files=15 symbols=19)`; `TRANSCRIPT_SCAN: HITS=2` exit 1 by design |

## Findings (new corpus claims, all probe-backed)

1. **Four real defects in committed docs, found on first contact.** Two
   session-scoped scratch URIs (`SCORECARD.md:54` `local://round-10/connector.md`;
   `corpus/lessons/round-10.md:50` `local://round-10/critic.md` — the pointer a
   future reader follows to learn what the critic said), kotoba's file cited
   under this repo's anchor (`corpus/README.md:61`), and a bare host filename
   (`corpus/README.md:157`). All fixed; the class is fleet-wide (protocol D-19,
   9 instances in one sibling corpus) and is reported, not imposed.
2. **Three stale numbers in my own docs** — `state-shape.tsv` called "20 rows"
   (README) and "21 rows" (PROVINCE) while it declares **22**; the census
   selftest called "14-case" while it prints **16 cases**. Fixed, and the counts
   are now pinned by ledger rows `R11-10`/`R11-11`/`R11-03`.
3. **A quarantine gate with a hole** — `surface-census.sh --verbs` could print
   `CLEAN (pass=0 skip=10)` with exit 0, so a claim row could accept a totally
   degraded run. Now `DEGRADED` + exit 1.
4. **The gate's own inspectability has a cost**: the citation scan covers
   ~515 tokens in 39 docs and takes ~20 s (whole-line, every token). Stated as
   a bound, not hidden.

## The 9-lane L2 wave (one batched call, frozen revision)

planner · connector · scout(gates) · scout(citations) · executor(entry) ·
executor(bypass) · critic · sentinel · reviewer — routes per MISSION.
Highlight: lanes hash-verified the frozen revision, then reported which files
moved mid-window.

What the wave **broke and I fixed**: unanchored verdict EREs passed a degraded
summary (critic CE1); the `bytes` stamp column was dead data (CE2); the citation
scan read only the first token of a span and missed command-argument citations
(CE3 + scout-citations: 153 class-shaped tokens invisible); `{4, 5}` broke brace
sets (CE3); `IFS=$'\t' read` collapsed empty fields so an empty command column
read CLEAN (executor A15); `tmo=0` disabled `timeout` (planner/executor); a bare
`^` expectation passed an empty last line, and empty output now fails on its own
(planner); `..` traversal let the committed default root hash a **private** host
file's digest (sentinel F3, must-fix — now refused with canonical containment);
`g''it` / `g\it` / `o"p"` word-splitting defeated the deny-list while the
stand-in executed (executor A03/A04 + sentinel F2 — deny words are now matched
on a quote-stripped copy); `die` echoed raw file content (F4); the self-stamp
guard never fired in its natural form (reviewer C7); duplicate paths inflated
`stamped=`; an empty stamp set reported CLEAN (planner).

What the wave **confirmed**: POLICY never ran a refused command (reviewer C6);
the last-line rule fires independently of exit equality (C5); a missing
`stamps.tsv` is exit 2 and a post-stamp edit is `STALE` + exit 1, both observed
live (scout); the write surface is exactly `stamp`'s mktemp→mv plus the selftest
tree (sentinel F7).

What the wave **rejected as bounded** (recorded in `knowledge/claim-ledger.md`
§Bounds): the ledger is a reviewed command file, not a sandbox — no inline
shell, narrower allowlist, but `bash <reviewed script>` is still arbitrary
execution; a self-test cannot prove its own honesty (the default wiring is
pinned by the claim row that runs the real docs); the marker rule is
line-granular; a stamp is a point check with no mode; claims are host-state
dependent as a class; a citation of a generated file is order-dependent.

**The reviewer's first pass was WRONG on three of my twelve claims** — not
because the mechanism lied, but because I had written those numbers before the
artifacts existed (no `stamps.tsv` until 19:38). A scout re-ran every row and
saw the same. That is the round-9 "gate-before-cite" lesson recurring in prose,
and it produced the round's durable rule: **quote a number with the stamped
revision it was measured at, and make the measurement the last byte-touching
step.** The reviewer is re-adjudicating the shipped revision (K1–K10).

## Adjacency (reported, not absorbed)

- Four sibling lanes ship overlapping verifiers, none duplicating this one:
  kumitate `scripts/cite-check.mjs` (citation/ref/pin re-verifier), kotoba
  `verifiers/verify_corpus_integrity.py` + `verify_harness_claims.py`, kengaku
  `grader.py` (evidence replay), kasegi `ops/claim-check.mjs` (bounty package
  gates — different domain). kagi defers to `PROTOCOL.md`'s evidence contract
  and fills the gap none of those owns: a revision-stamped, command-per-claim
  ledger with a citation-durability verdict.
- **Integrator rulings requested** (connector lane): (1) whether these five
  verifiers should share a contract (token grammar, marker vocabulary, verdict
  vocabulary); (2) whether verdict-only output satisfies `PROTOCOL.md`'s
  output-at-write-time standard (kagi never echoes a claim's output, because
  that output can contain anything); (3) whether a *labelled* dead pointer may
  stand as evidence for an active claim — kagi's rule is "labelled where cited",
  and the aggregator/protocol lanes own the evidence meaning.
- Unchanged from prior rounds: the shared global `~/.config/opencode/opencode.json`
  ownership boundary, `~/.agents/AGENTS.md` (kotoba), the musketeer profile lease
  (kake). kagi's citation gate now *resolves* cross-lane citations
  (`kotoba-shokunin/…`, `.ufo/…`) instead of absorbing them.

## Safety

No vault read, no `op` exec, no `the-janitor start|stop|request|run`, no Chrome
launch, no write outside scratch; all L2 execution was scratch-only (`/tmp`
copies, fabricated values). No secret value, ref path, account identifier,
private-file hash or transcript cell entered any artifact. `stamps.tsv` covers
in-repo artifacts only — the `..`/symlink route by which a private host file's
digest could have entered it is closed and selftested.

## Residuals (named, not hidden)

Scores remain author-assigned: a reader can re-run every pointer, not the
number. A stamp records no mode and is a point check. Claims are host-state
dependent as a class (`R11-06` most sharply: a new operator session re-baselines
the transcript gate, it does not "fix" it). Nothing schedules the gate. The
citation scan sees Markdown only (not shell-script headers) and treats bare
filenames/host paths/routes as references by rule. The next planned move is
calibration → 9: make each score **cell** cite the row ids it rests on, so a
reader can re-derive the number rather than the evidence.

## Report artifact hashes (the round-11 plan, delivered)

| Artifact | sha256 prefix | lines |
|---|---|---|
| `corpus/claim-ledger.sh` | `8120f7d7d29a` | 540 |
| `corpus/claim-ledger.tsv` | `af31a5bbaeda` | 25 (11 rows) |
| `corpus/stamps.tsv` | `0e8e836ef47c` | 28 rows |
| `corpus/surface-census.sh` | `2eb86e1f0ee4` | 877 |
| `corpus/knowledge/claim-ledger.md` | `09dda83d2adb` | 232 |
| `corpus/lessons/round-11.md` | `ba239af4e4e8` | 201 |

All six are inside the 28-row `corpus/stamps.tsv`, so
`bash corpus/claim-ledger.sh verify` re-checks the exact revision this report
describes (`CLAIM_LEDGER: CLEAN (claims=11 stamped=28)`, exit 0). The lane-run
scratch artifacts of the nine L2 lanes (`local://round-11/*`) are session-scoped
and are **not** cited as durable evidence — the durable residue is the
disposition table in `corpus/lessons/round-11.md` §L2 wave.