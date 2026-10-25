# Round 10 aggregator corpus verdict — kagi

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kagi-shokunin:<path>` resolves in this checkout; bare `corpus/…` and `SHONEN.md` are
relative to this checkout's root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kagi, and it is the artifact
whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-10/aggregator.md`,
`shokunin:.ufo/reports/AGGREGATE.md` §15, `shokunin:LOG.md` round-10 entry, and the gate
`shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id `corpus-gate-v1`, read-only).

## 1. Revision measured

| cell | observed | command |
|---|---|---|
| live `HEAD` (short) | `587fda0` | `git -C kagi-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `587fda0470f2b8144618068839997756c65ddde2` | `git -C kagi-shokunin rev-parse HEAD` |
| worktree dirty count | 0 | `git -C kagi-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T02:07:06Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |
| mode | `live`, **not** provisional (the worktree equals the cited revision) | the gate's `# tree` line, quoted below |

```
# tree kagi-shokunin revision=587fda0470f2b8144618068839997756c65ddde2 (worktree) dirty=0 mode=live
```

`HEAD` moved twice inside this round: `shokunin:.ufo/waves/round-10/CONTEXT.md` stamped `2486643` (dirty 6) at
`2026-09-29T01:44:38Z`; the lane's round-15 commit `587fda0` landed at `2026-09-28T22:56:34-03:00` and cleared the tree
(`git -C kagi-shokunin log -1 --format='%h %aI %s'`). Cells below are stamped to the revision they measured (**P-s**).

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** — gate exit 1 at `587fda0` (dirty 0, live mode), `--round 10`:

```
# verdict kagi-shokunin failed findings=59 rules=r2,r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

| failed rule | findings | rule text |
|---|---:|---|
| r2 — a lesson cites its round and its evidence | 8 | `shokunin:CORPUS.md:19` |
| r4 — a count carries its command | 44 | `shokunin:CORPUS.md:28-32` |
| r8 — credential material, literal text | 4 (occurrences 1 bearer + 3 kv-secret + 13 op-ref aggregator + 69 op-ref lane) | `shokunin:CORPUS.md:43-46` |
| r10 — the round's aggregator lesson is present | 1 (discharged by this file) | `shokunin:CORPUS.md:21` |
| shonen — `SHONEN.md` canonical form | 2 | `shokunin:PROTOCOL.md` §File contract |

r7 emits **0** findings (no index row names an absent file); under-coverage is printed as a note, not a finding
(`# note kagi-shokunin r7 under-coverage (not a finding): 13/49 corpus files carry no index row`). The gate declares 7
checks not-evaluated (`--registry`), so rules 1, 3, 5, 6, 9, box-3 independence and box-truth semantics stay
hand-graded in `shokunin:.ufo/reports/AGGREGATE.md` §15.2.

**r2 attribution — 1 of the 8 is this lane's own file.** `CR-kagi-shokunin-r2-1` names
`corpus/lessons/round-1-aggregator-audit.md`, which `shokunin:CORPUS.md:47-54` makes aggregator-owned; the other 7 are
`corpus/lessons/round-{3,4,5,6,7,8,10}.md` (`node .ufo/waves/round-9/corpus-gate.mjs --repo kagi-shokunin --round 10`
prints each). The row therefore routes 7 to kagi and 1 to the aggregator, and the count must not be read as 8 lane
defects.

## 3. Per-rule movement from the round-9 pinned revisions

Before columns: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kagi-shokunin <rev> --round 9 --json` (snapshot
mode, `dirty=0`). Live column: `node .ufo/waves/round-9/corpus-gate.mjs --repo kagi-shokunin --round 10 --json`.

| rule | `4b8c018` (round-9 pin) | `4391b3b` (round-9 alt pin) | live `587fda0` | movement vs `4b8c018` |
|---|---:|---:|---:|---|
| r2 | 8 | 8 | 8 | flat |
| r4 | 36 | 31 | 44 | **+8** (+13 vs the alt pin) |
| r7 | 0 | 0 | 0 | flat |
| r8 | 4 | 4 | 4 | flat in findings; occurrences moved (§4 note) |
| r10 | 1 | 1 | 1 | different duties: before = the round-9 lesson absent from that archive; live = this lesson not yet mirrored |
| shonen | 2 | 2 | 2 | flat |
| **total** | **51** | **46** | **59** | **+8** |

Both frozen expectations still reproduce (`node .ufo/waves/round-9/corpus-gate.mjs --snapshot kagi-shokunin <rev>`):

```
# expect kagi-shokunin@4b8c018 MATCH exit=1 ids=51
# expect kagi-shokunin@4391b3b MATCH exit=1 ids=46
```

r4's 44 findings concentrate: `corpus/lessons/round-14.md` 5, `corpus/knowledge/drift-gate.md` 4,
`corpus/knowledge/handler-on-disk-state.md` 4, `corpus/lessons/round-10.md` 4, `corpus/lessons/round-9.md` 4,
`corpus/lessons/round-13.md` 3 (same `--json` run, counted per file).

## 4. r4 adjudication, and the r8 unit

`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kagi-shokunin --round 10` was attempted at the stamp above:
adjudication **not-run at draft time** (the tool had not landed; the L1 re-measures and rewrites this section before the
mirror). Only the raw count is published: **raw r4 = 44** —
`node .ufo/waves/round-9/corpus-gate.mjs --repo kagi-shokunin --round 10 --json`. The declared false-positive classes
this round closes are `fp-entity-designation`, `fp-design-arithmetic`, `fp-quoted-refutation` (the rule-4/rule-9
collision, `D-141`), with the intent reconstruction in
`shokunin:.ufo/waves/round-10/seats/revenger-rule4-intent.md`.

**r8 unit and owner (proposal P-u: a count names its unit).** The gate's r8 unit is *occurrences*, and each finding
carries `owner=` by the `round-<N>-aggregator-*.md` filename pattern. At `587fda0`:

| finding | class | occurrences | lines | files | owner | shape test | locator |
|---|---|---:|---:|---:|---|---|---|
| `CR-kagi-shokunin-r8-1` | bearer | 1 | 1 | 1 | lane | `literal_shaped=1/1` | `kagi-shokunin:corpus/knowledge/handler-trust-boundary.md:39` |
| `CR-kagi-shokunin-r8-2` | kv-secret | 3 | 3 | 3 | lane | `literal_shaped=0/3` | first `corpus/knowledge/claim-ledger.md:86` (len 72) |
| `CR-kagi-shokunin-r8-3` | op-ref | 13 | 12 | 5 | **aggregator** | `maxseg=3` | first `corpus/lessons/round-1-aggregator-audit.md` |
| `CR-kagi-shokunin-r8-4` | op-ref | 69 | 66 | 23 | lane | `maxseg=3` | first `corpus/checklist.tsv` |

All four carry the gate's declared abstention `classification=could-not-evaluate (needs a vault read; operator-gated)`;
no value is reproduced here, and the two locators above are quoted by position only. Two readings this round publishes
rather than resolves:

1. **`r8-1` is a masked illustration, not a credential.** The cell at
   `kagi-shokunin:corpus/knowledge/handler-trust-boundary.md:39` is a table row of the form
   `` | `Authorization: Bearer jt******pw` | — | 401 | `` — the lane already masked the middle of the token, and the
   gate's shape test reports `len=17`, which is the masked string's length. Classification **schematic (masked at
   source)**; the `literal_shaped=1/1` flag is a shape-test artefact. This is a fourth rule-8 class the operator-side
   amendment needs (`D-125`, `shokunin:.ufo/l0-questions.md` line 12): a *masked* example is not credential material,
   and a shape test cannot tell the two apart without a vault read.
2. **13 of the 82 op-ref occurrences are this lane's own bytes** (`owner=aggregator`, in
   `round-{1,5,6,9}-aggregator-*.md`), so kagi's rule-8 red is partly the aggregator's — the round-9 self-defect 20
   class, unchanged. Historical files cannot be rewritten (`shokunin:CORPUS.md:47-54`); the forward fix (no vault-ref
   scheme spelled literally in mirrored lessons) applies from this lesson on, and this file contains none.

## 5. Ledger rows this verdict rests on

Rows owned by kagi in `shokunin:.ufo/reports/AGGREGATE.md`
(`grep -nE '^\| D-[0-9]+[^|]*\| kagi' .ufo/reports/AGGREGATE.md`):

| key | sev | defect (paraphrase) | status at this stamp |
|---|---:|---|---|
| `D-08` | 3 | bare `handoff-status.json` cites in `SKILL.md` (4 mentions, 0 absolute paths) | OPEN |
| `D-09` | 3 | `SKILL.md:28` `op.env` prerequisite row lacks the fail-closed stop note | OPEN |
| `D-64` | 3 | `corpus/lessons/round-9.md:175` + `LOG.md:215` "the delivered/committed **445**-line revision is green" vs a 451-line committed blob | OPEN |
| `D-65` | 3 | `SCORECARD.md:16` depth cell carries four falsified counts | OPEN |
| `D-66` | 3 | hash-policy sentence says 6 private `0600` files; the baseline holds 7 | OPEN |
| `D-104` | 3 | `corpus/transcript-scan.sh` documented `exit 0 CLEAN`; cold run gave exit 1 `HITS=2` | OPEN — reproduces at `2486643` (§6) |
| `D-105` | 3 | `SKILL.md:39` presents `the-janitor cdp-bridge ensure` as ordinary flow though it clobbers a shared surface | OPEN |
| `D-112` | 3 | re-keyed from protocol's `D-51`: the `ade32e4` pathspec violation, report-before-commit, no hash citations | OPEN |
| `D-133` | 2 | `SHONEN.md` box-3 `[x]` contradicted by the lane's own red gates | **OPEN, re-tested this round** (§6) |
| `D-134` | 3 | 0 of 6 `[x]` marks fleet-wide carry a `<verifier-id>`; kagi's four name its own dispatched seats | OPEN — reproduces (§6) |
| `D-144` | 3 | `shokunin:.ufo/reports/round-12/kagi.md` untracked at its contract path | **CLOSED at `b5fff81`** (protocol's durability sweep; `git ls-files .ufo/reports/round-12/kagi.md` → tracked) |
| `D-149` | 4 | `SHONEN.md` has no trailing newline | OPEN — reproduces (§6) |
| `D-51 ⊇ D-84` | 3 | `node scripts/cite-check.mjs --integrations` FAILs on an aggregator-owned lesson, so it cannot grade the lane down (P-f) | OPEN, folded |

## 6. Box-3 / `SHONEN.md` state, and the `D-133` re-test

The `shonen` check emits **2** findings at `587fda0`: `SHONEN.md` lines 5, 7, 9, 11 are `[x]` marks carrying no
`<verifier-id>` token (`CR-kagi-shokunin-shonen-1`, `D-134`), and the file lacks the required trailing newline
(`CR-kagi-shokunin-shonen-2`, `D-149`). Box-3 **independence** is declared `not-evaluated` by the gate, so the ledger's
hand grade stands: kagi's box-3 `[x]` **breaks** (`shokunin:.ufo/reports/AGGREGATE.md` §14.6).

`D-133` re-tested at kagi's landed revision `2486643` by a non-author probe seat
(`shokunin:.ufo/waves/round-10/seats/labrat-probes.md` §2), read-only, each script first swept for writes:

| kagi gate | observed | exit | movement vs the round-9 measurement |
|---|---|---:|---|
| `bash corpus/claim-ledger.sh verify` | `CLAIM_LEDGER: FAIL (claims=23 failed=3 stamped=48 stale=7 missing=0 unresolved_ids=0 labeled_ids=17)` | 1 | still red; failed 1 → **3** |
| `bash corpus/claim-ledger.sh citations` | no failing line emitted | **0** | **cleared** (was exit 1, `BROKEN unresolved=33`) |
| `bash corpus/transcript-scan.sh` | `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0)` | 1 | still red, unchanged `HITS=2` |

So `D-133` **persists in part and moves in part**: one of the three red gates cleared at `2486643`, two stay red, and the
box-3 `[x]` remains contradicted by the lane's own gates. `HEAD` then moved to `587fda0` (dirty 0) inside this round, so
the re-test is stamped to `2486643` and is not a claim about `587fda0`.

## 7. Commands a reader re-runs

```bash
git -C kagi-shokunin rev-parse HEAD; git -C kagi-shokunin status --porcelain | wc -l; date -u +%Y-%m-%dT%H:%M:%SZ
node .ufo/waves/round-9/corpus-gate.mjs --repo kagi-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kagi-shokunin 4b8c018 --round 9
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kagi-shokunin 4391b3b --round 9
node .ufo/waves/round-9/corpus-gate.mjs --repo kagi-shokunin --round 10 --json | sed -n 's/^# json //p'
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kagi-shokunin --round 10    # absent at draft time
cd kagi-shokunin && bash corpus/claim-ledger.sh verify; bash corpus/transcript-scan.sh   # D-133 re-test, read-only
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** It carries its round and evidence pointers (rule 2), every count on a
line that also carries its backticked command (rule 4), no credential literal and no vault-ref scheme spelled as a
literal (rule 8 — its r8 discussion quotes the gate's own metadata fields and locators, never a value), and it is the
round-10 aggregator lesson rule 10 requires. The L1 verifies by re-running the gate before and after the mirror at one
stamp and publishes both totals in `shokunin:.ufo/reports/AGGREGATE.md` §15.17.
