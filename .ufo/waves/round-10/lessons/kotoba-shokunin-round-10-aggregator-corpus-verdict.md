# Round 10 aggregator corpus verdict — kotoba

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kotoba-shokunin:<path>` resolves in this checkout; bare `corpus/…` and
`SHONEN.md` are relative to this checkout's root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kotoba, and it is the
artifact whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-10/aggregator.md`
(this round's report), `shokunin:.ufo/reports/AGGREGATE.md` §15 (refresh 8), `shokunin:LOG.md` round-10 entry, and
the gate `shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id `corpus-gate-v1`, read-only, sha256
`68939d0c70b6dc5ee9e2667b…`).

## 1. Revision measured

| cell | observed | command |
|---|---|---|
| live `HEAD` (short) | `0089974` | `git -C kotoba-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `00899744d602db71d7951c4da37002ad281ffad7` | `git -C kotoba-shokunin rev-parse HEAD` |
| worktree dirty count | 2 | `git -C kotoba-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T02:07:06Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |
| mode | `live`, `provisional=1` (worktree-only bytes differ from the cited revision) | the gate's own `# tree` line, quoted below |

```
# tree kotoba-shokunin revision=00899744d602db71d7951c4da37002ad281ffad7 (worktree) dirty=2 mode=live provisional=1 (worktree-only bytes differ from the cited revision)
```

`HEAD` moved inside this round: `shokunin:.ufo/waves/round-10/CONTEXT.md` stamped `0f658ff` (dirty 11) at
`2026-09-29T01:44:38Z`; the lane's round-15 close commit `0089974` landed at `2026-09-28T23:07:06-03:00`
(`git -C kotoba-shokunin log -1 --format='%h %aI %s'`). Every cell below is stamped to the revision it measured
(proposal **P-s**).

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** — gate exit 1 at `0089974` (dirty 2, live mode), `--round 10`:

```
# verdict kotoba-shokunin failed findings=83 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

| failed rule | findings | rule text |
|---|---:|---|
| r4 — a count carries its command | 69 | `shokunin:CORPUS.md:28-32` |
| r8 — credential material, literal text | 2 (occurrences 3 aggregator + 2 lane) | `shokunin:CORPUS.md:43-46` |
| r10 — the round's aggregator lesson is present | 1 (discharged by this file) | `shokunin:CORPUS.md:21` |
| shonen — `SHONEN.md` canonical form | 11 | `shokunin:PROTOCOL.md` §File contract |

r2 and r7 emit **0** findings (`node .ufo/waves/round-9/corpus-gate.mjs --repo kotoba-shokunin --round 10 --json`).
The gate implements 6 of the contract's checks and declares 7 not-evaluated with reasons
(`--registry` prints both lists); rules 1, 3, 5, 6, 9, box-3 independence and box-truth semantics therefore stay
hand-graded in `shokunin:.ufo/reports/AGGREGATE.md` §15.2 and are **not** reproduced by the counts above.

## 3. Per-rule movement from the round-9 pinned revision

Before column: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kotoba-shokunin 63ceba7 --round 9 --json`
(snapshot mode, `dirty=0`) — the round-9 pin in `shokunin:.ufo/waves/round-10/CONTEXT.md`. Live column:
`node .ufo/waves/round-9/corpus-gate.mjs --repo kotoba-shokunin --round 10 --json`.

| rule | before (`63ceba7`, snapshot, `--round 9`) | live (`0089974`, dirty 2, `--round 10`) | movement |
|---|---:|---:|---|
| r2 | 0 | 0 | flat |
| r4 | 61 | 69 | **+8** |
| r7 | 0 | 0 | flat |
| r8 | 2 | 2 | flat in findings; occurrences 5 (3 aggregator + 2 lane) |
| r10 | 1 | 1 | different duties: before = the round-9 lesson absent from that archive; live = this lesson not yet mirrored |
| shonen | 11 | 11 | flat |
| **total** | **75** | **83** | **+8** |

The frozen expectation for the before revision still reproduces:
`node .ufo/waves/round-9/corpus-gate.mjs --snapshot kotoba-shokunin 63ceba7` → `# expect kotoba-shokunin@63ceba7
MATCH exit=1 ids=75`.

r4's 69 findings concentrate (count per file, same `--json` run): `corpus/knowledge/cold-run-round11.md` 5,
`corpus/knowledge/opencode-offer-trace-round8.md` 5, `corpus/knowledge/checklist-execution-round15.md` 4,
`corpus/knowledge/frontmatter-trigger-surface.md` 4, `corpus/lessons/round-9.md` 4,
`corpus/knowledge/agent-def-audit-round6.md` 3. The +8 is consistent with the lane's round-15 work adding
`corpus/knowledge/checklist-execution-round15.md` (4 of the 69) — attribution, not proof:
`git -C kotoba-shokunin log --format='%h %aI' -1 -- corpus/knowledge/checklist-execution-round15.md` → `0089974`.

## 4. r4 adjudication

`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kotoba-shokunin --round 10` was attempted at the stamp
above: adjudication **not-run at draft time** (the tool had not landed; the L1 re-measures and rewrites this section
before the mirror). Only the raw count is published: **raw r4 = 69** —
`node .ufo/waves/round-9/corpus-gate.mjs --repo kotoba-shokunin --round 10 --json`.

No violation/false-positive split is invented here. The three declared false-positive classes this round closes are
`fp-entity-designation`, `fp-design-arithmetic` and `fp-quoted-refutation` (the rule-4/rule-9 collision routed as
`D-141`), with the intent reconstruction in `shokunin:.ufo/waves/round-10/seats/revenger-rule4-intent.md`.

## 5. Ledger rows this verdict rests on

Rows owned by kotoba in `shokunin:.ufo/reports/AGGREGATE.md` (`grep -nE '^\| D-[0-9]+[^|]*\| kotoba'
.ufo/reports/AGGREGATE.md`), status as recorded at the stamp above:

| key | sev | defect (paraphrase) | status |
|---|---:|---|---|
| `D-29` | 3 | falsified self-counts "22-row" / "12-item"; re-counted 20 data rows | OPEN |
| `D-70` | 4 | 8 unresolvable `commit round-N` citations (`corpus/lessons/round-{1,4,5,6,7}.md:3`, `corpus/README.md:23,24,25`), 3 newly added in r9 | OPEN |
| `D-71` | 3 | inherited mechanism claim falsified and unnamed (`corpus/knowledge/skill-activation-telemetry.md:29-30`) | OPEN |
| `D-102` | 3 | `SHONEN.md:14-15` box-3 `[x]` attributed to `ReviewSHONEN`, which the lane's own report lists among its dispatched seats ⇒ `[~]` at best | OPEN |
| `D-103` | 3 | `verifiers/fault_injection_corpus.sh` listed as runnable with no mutation warning; it clones and `rm -rf`'s `/tmp` worlds (`script:27-28`) | OPEN |
| `D-116` | 3 | `/tmp` evidence pointers in r10/r11 (self-flagged; still a defect until committed or reproducible) | OPEN |
| `D-124` | 3 | sibling trigger gap: 0/5 sibling `SKILL.md` descriptions carry a quoted trigger or arbitration clause | OPEN |
| `D-140` | 3 | `verify_surfaces.py` + `verify_harness_claims.py` are gate-shaped (75/10 assertions, live 7 PASS + 27/27) but have no registry row and no committed frozen run ⇒ classified **probe** | OPEN |
| `D-145` | 3 | `shokunin:.ufo/reports/round-14/kotoba.md` untracked at its contract path | OPEN at this stamp (`git ls-files -o --exclude-standard .ufo/reports` still lists it) |
| `D-148` | 3 | `SHONEN.md` outside canonical form: 8 non-box prose lines (38–45) + 29 evidence lines where the form allows ≤1 per box ⇒ regenerate verbatim from the seed | OPEN — the 11 `shonen` findings in §2 are this row, still red at `0089974` |

## 6. Box-3 / `SHONEN.md` state

The gate's `shonen` check grades canonical **form** only and emits **11** findings at `0089974`:
boxes 1/2/3 carry 10/5/13 indented evidence lines where the form allows at most one each
(`CR-kotoba-shokunin-shonen-1..3`), and `SHONEN.md:38-45` are 8 lines that are neither header, box nor evidence
(`CR-kotoba-shokunin-shonen-4..11`, one blank + seven prose). Whether any mark rests on a **non-author** verifier is
declared `not-evaluated` by the gate (`--registry` → `not-evaluated box-3 … the graded tree does not carry the
authorship graph`), so this lesson repeats the ledger's hand grade rather than recomputing it: kotoba's box-3 mark is
**`[~]` stands** (`shokunin:.ufo/reports/AGGREGATE.md` §14.6), with `D-102` open against the `[x]` at
`kotoba-shokunin:SHONEN.md:14-15`. Fleet-wide, **0 of 6 `[x]` marks carry the `<verifier-id>`** the canonical form
requires (§14.7, `D-134`).

## 7. Commands a reader re-runs

```bash
git -C kotoba-shokunin rev-parse HEAD; git -C kotoba-shokunin status --porcelain | wc -l; date -u +%Y-%m-%dT%H:%M:%SZ
node .ufo/waves/round-9/corpus-gate.mjs --repo kotoba-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kotoba-shokunin 63ceba7 --round 9
node .ufo/waves/round-9/corpus-gate.mjs --repo kotoba-shokunin --round 10 --json | sed -n 's/^# json //p'
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kotoba-shokunin --round 10   # absent at draft time
grep -rnE 'op:[/]{2}' kotoba-shokunin/corpus | wc -l                                   # rule-8 sweep, scheme spelled as a class
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** It carries its round and evidence pointers (rule 2), every count on a
line that also carries its backticked command (rule 4), no credential literal and no vault-ref scheme spelled as a
literal (rule 8 — the sweep above is written as a character class), and it is the round-10 aggregator lesson rule 10
requires. The L1 verifies the claim by re-running the gate before and after the mirror at one stamp and publishes both
totals in `shokunin:.ufo/reports/AGGREGATE.md` §15.17.
