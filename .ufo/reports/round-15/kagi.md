# kagi — round 15 (operability 8 → 9)

Lane: kagi (secrets & vault ops). Repo: `/home/vgpnk/projects/shokunin/kagi-shokunin`.
Axis moved: **operability** — the lowest-scoring axis at the round-14 close
(operability, depth, coverage and adjacency all stood at 8; freshness and
calibration at 9). The lane rule is "pick the lowest-scoring axis, land one
verifiable improvement", so this round did **not** take the freshness target the
previous plan had named (`by_hand 3 → ≤1`); that is recorded as an open,
unclaimed target in `SCORECARD.md` with its number (`DOC_AUDIT_RATIO by_hand=3`,
row `R14-01`).

## Before → after

| | before (`HEAD` `2486643`) | after (round 15) |
|---|---|---|
| checklist items | 16 `- [ ]` bullets in `SKILL.md` | 16 rows in `corpus/checklist.tsv`, bijection-enforced |
| items that produce a verdict | **0** (`ls corpus/checklist*` ⇒ nothing; `grep -rl 'hygiene checklist' corpus/*.sh` ⇒ nothing) | **9 runnable** (`CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)`) |
| judgement items | asserted (and wrong): "12 checklist items are still operator judgement" | **7 by-hand**, each a closed class + a unique ≥24-char reason — `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6` |
| the ratio | no such measurement | `ceil(items/2) = 8` floor, met with one row of margin |
| self-proof | n/a | `CHECKLIST_SELFTEST: PASS (34 cases)` |
| wrong committed figures | 4 (`SCORECARD.md:16` "15-item"; three rounds-9–11 cells' "12 judgement items"; `PROVINCE.md:12` + `corpus/surface-census.tsv:22` filing the lock under `client.py`) | all corrected in place with the measurement |

## The pre-state (measured, and three ways where it mattered)

- Items: `awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- \[ \]'` ⇒ **16** (8 Evidence production + 8 Handler operation). Two lanes reproduced it; the item-count history over every SKILL.md-touching commit is 10 → 12 → 13 → 14 → 16, i.e. **no revision ever held 15**.
- Verdicts: none. Five items named a command in their text; none produced an outcome.
- The lock note: `grep -nic lock ~/.config/the-janitor/client.py` ⇒ **0**; the flock is `~/.local/bin/the-janitor` L12 (`LOCK_FILE`), L130/139/175 (`exec 9>"$LOCK_FILE"`), L131/140/176 (`flock 9`). Also the exact line split matters — the first correction conflated the two sites and was fixed.
- No scheduler: `systemctl --user list-timers`, `crontab -l`, cron dirs/spools ⇒ nothing runs any `corpus/*.sh` (labrat lane, read-only). That is why the operability increment claimed here is "each item produces a verdict or a declared gap", **not** scheduling.

## What landed

`corpus/checklist-run.sh` (`verify` | `--ratio` | `--list` | `--only ID` | `--selftest`) + `corpus/checklist.tsv` (16 rows; `id class lead check expect_exit expect_last reason note`). Three teeth beyond "run 16 commands":

1. **Bijection.** Each row's `lead` ERE must match exactly one of the 16 items and each item exactly one row. `UNMATCHED-ITEM`, `DUPLICATE-ITEM`, `UNMATCHED-LEAD`, `DUPLICATE-LEAD`, `UNDECLARED`, `EXTRA` each exit 1 — adding a bullet to `SKILL.md` without a row fails closed (proved by a lane's fixture: a 17th item ⇒ `UNDECLARED (items=17 rows=16)`).
2. **Declared split, not silent omission.** `by-hand` rows carry `<class>: <text>` with a closed class set, ≥24 characters, ≥20 non-space characters, unique across rows; the floor is `ceil(items/2)`; the ratio line separates `delegated` (rows calling an existing gate: E1, E5, H7) from `direct` (assertions this round introduced: 6).
3. **Policy.** A `check` naming a denied surface (`op.env`, `op run|read|inject`, handler start/stop/run, `claim-ledger.sh`) is refused **before** execution (exit 2, nothing run). The reference-path sweep prints counts only, because printing the matched line would be the leak item E4 forbids; `--only ID` prints `CHECKLIST_ROW:` rather than a checklist verdict, because one row is not the checklist.

Docs/harness landed with it: `SKILL.md` (executable header + decision-table row), `PROVINCE.md` (gate registered; lock note corrected), `corpus/README.md` (coverage map), new `corpus/knowledge/checklist-execution.md` (`Reverify: R15-01 … R15-05`, 12 bounds, 10 falsifiers), `corpus/lessons/round-15.md`, five ledger rows `R15-01..05`, four historical score-card corrections, and re-pinned count rows (`R12-03` stamps 44 → 48, `R13-01` sections 12 → 14, `R13-02` rows 18 → 23, `R14-01` docs entries 17 → 18).

## Evidence (shipped revision)

```
bash corpus/checklist-run.sh
  CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6
  CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)        exit 0, ~2.3 s
bash corpus/checklist-run.sh --ratio
  CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6  exit 0, 0.2 s, no row run
bash corpus/checklist-run.sh --list
  CHECKLIST_LIST: rows=16 runnable=9 by_hand=7                          exit 0
bash corpus/checklist-run.sh --selftest
  CHECKLIST_SELFTEST: PASS (34 cases)                                   exit 0
# from foreign cwds /, /tmp and a relative path ⇒ PASS (34 cases)
bash corpus/claim-ledger.sh verify   ⇒ CLAIM_LEDGER: CLEAN (claims=23 stamped=48 ids=23 cited=23 labeled_ids=17 orphans=0)   exit 0
bash corpus/claim-ledger.sh cells    ⇒ CELL_AUDIT: CLEAN (cells=84 row_pointed=46 stamp_pointed=53 uncited=0 missing_ids=0 rows_run=19 row_failures=0 stale_pointers=0 self_skipped=4 orphans=0)   exit 0
bash corpus/claim-ledger.sh docs     ⇒ DOC_AUDIT: CLEAN (entries=18 row_linked=15 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)   exit 0
bash corpus/claim-ledger.sh citations⇒ CITATION_GATE: CLEAN (cites=785 docs=47 unresolved=0 ephemeral=0 labeled=13)   exit 0
# siblings unchanged
DRIFT_PINS: CLEAN (files=15 symbols=20) · SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)
OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6) · TRANSCRIPT_SCAN: HITS=2 (exit 1 by design)
```

Live falsifications run against the shipped gate (not fixtures): an untracked
`.json` carrying a reference-shaped literal ⇒ `ITEM-FAIL E4 … hits=1 excluded=5
raw=6`; the file removed ⇒ `CLEAN`.

## Defects this round found in its own first implementation

Nine, eight by lanes and one by its own selftest — every one of the classes this
corpus has been bitten by before:

1. **Silent death (fatal).** `dup_reasons=$(for …; done | sort | uniq -d)`: the loop's last iteration returns 1 when the last row is `runnable`, `uniq -d` returns 1 on an empty result, `pipefail` + `set -e` killed the script **before any verdict line** — exit 1 with zero bytes of output. Found by a scribe lane's `bash -x` trace ending at `+ dup_reasons=` and independently by an executor lane's two-row fixture.
2. **Silent death (second site).** `last=$(… | grep -v … | tail -1)` died the same way on a row that printed nothing ⇒ `awk 'NF{l=$0} END{print l}'`.
3. **A false defect on a correct host.** `H4` captured the front matter with `(?:[ \t]+.*\n)+`, but the captured body's last line has no trailing newline, so the permission matcher read one of two entries ⇒ `JANITOR_PERMS: DEFECT (entries=1 steps=4)`.
4. **The sweep's own first contact.** `E4` found three undeclared reference-shaped literals (`op-env-refs.md:14`, `round-5-aggregator-audit.md:19`, `transcript-scan.sh:202` — the documented `vault` placeholder form) ⇒ the allowlist is now *visible* (`excluded=5 raw=5` printed and pinned) instead of silent.
5. **A row that swallowed its own verdict.** The first `E4` rewrite wrapped `printf`/`test` inside `n=$(…)` ⇒ `ITEM-LASTLINE E4 (got '')`, no verdict line (scribe lane, verbatim re-run).
6. **A blind spot in the control-plane row.** `H8` accepted a **wildcard** listener on 40961 (only a listener *count* was reported); a scout lane branch-proved it on scratch ports ⇒ `non_loopback=0` is now asserted.
7. **Comment text satisfying a code row.** `H1`'s `grep -c 'flock 9'` matched comments (critic lane, fake-`HOME` fixture) ⇒ line-anchored patterns for both the flock and the `exec 9>` sites.
8. **A legitimate state declared a defect.** `H7` said `expect_exit 0|1` while `stop + rm -rf xdg-data` — the purge the item *above it* prescribes — exits 2 with `db not found: …`; the row now names exactly two accepted states.
9. **Selftest not cwd-independent.** It re-invoked itself as `"$0"` ⇒ exit 127 from a foreign cwd (labrat lane) ⇒ absolute `$SELF`.

The selftest grew 0 → 34 cases and each fixture is rebuilt from scratch instead of mutated by `sed`.

## L2 wave (14 lanes, one batched dispatch)

planner, connector, 2 scouts, scribe, 2 executors, reviewer, critic, sentinel,
labrat, mutation-tester, simplifier, distiller.

| Lane | What it produced (each with executed evidence) |
|---|---|
| planner | the competing classification: a strict duty-vs-premise criterion gives `runnable=3 by_hand=13` (below the floor); flagged E5's delegated `op run` |
| scout (host facts) | 9 validated row candidates; the `ss -l` pitfall; the wildcard-bind hole; the lock-misattribution falsifier; pyyaml availability |
| scout (items) | the 16-item census + count history; the four wrong committed figures; six attacks incl. H7's purged-DB false defect and E4's silent allowlist |
| scribe | two silent-death diagnoses with `bash -x`, the H4 regex boundary, the E4 swallowed-verdict bug; LOG draft |
| executor (draft) | 470-line entry draft; 9/9 runnable rows hand-run; 12 fixture falsifiers |
| executor (report) | report skeleton from measured facts only, with an explicit placeholder list |
| reviewer | independent 16-item audit; the extension-class gap (an untracked `.json` carrying a ref literal passed the old sweep) ⇒ scan widened to every non-`.git` file |
| critic | three executed counterexamples: comment-text matching, an unexamined env file carrying the password, and a constant-`printf` 16-row TSV passing `CLEAN (runnable=16/16)` ⇒ the round's ceiling |
| sentinel | PASS on all four policy questions; confirmed no concrete ref path or pasted `run` output in the repo |
| labrat | scratch-listener proof of the port check; gate timings (2.2 s end-to-end); empirical "nothing schedules `corpus/*.sh`" |
| mutation-tester | 10/10 required mutations fail closed; two extra gaps (padded reason ⇒ now `POLICY`; a *dynamically built* denied path ⇒ recorded bound) |
| simplifier | minimal honest set (6 runnable) and E1 deletion argued; double-counting sweep |
| connector | sibling map: kotoba `verify_skill_checklist.py`, kumitate doc-coverage score, kasegi `anchorcheck.py` — adjacent, none an item → command → verdict contract |
| distiller | 9 unique moves, 3 duplicates collapsed, no unresolved contradictions |

## Bounds (why 9, not 10)

- **Premise, not duty.** A runnable row verifies the item's machine-checkable half and says in its `note` what it leaves to the operator. That property is not gate-enforceable (a lane read all nine to confirm them), and it is the only reason the 9 is honest.
- **Well-formed ≠ meaningful.** The critic's constant-`printf` TSV passes `CLEAN (runnable=16/16)` and clears the floor. The deny list is lexical (a built string bypasses it), and the ratio's `delegated`/`direct` split is the only mechanical signal against re-asserting an existing gate's exit. Recorded, not papered over.
- **Nothing schedules the seven gates.** Operator scope (systemd/cron); explicitly not claimed.
- **The 7 by-hand duties** stay by-hand; for H2/E6/H6 the contract forbids the only mechanisation.
- **E4's allowlist** exempts three placeholder vault names by name (`vault`, `FakeVault`, `wal`), counted and pinned; a live path under a vault literally named `vault` would be exempt. **H7** accepts exactly two states, one being "the DB is legitimately gone".

## Next target (recorded in `SCORECARD.md`, falsifiable)

Add a mutation mode (`--mutate`) in which every runnable row declares a negative
fixture that MUST make the row fail; the number that has to move is a new
`MUTATION: caught=K/K` line, and a row with no cheap perturbation must declare
that gap the way `by-hand` does. That is the direct answer to the constant
`printf` counterexample.

## Adjacency (reported, not absorbed)

Sibling verifiers are mapped, not absorbed: kotoba's `verify_skill_checklist.py`
links checklist boxes to dispositions (its predicates inspect the file rather
than execute the item's command), kumitate's `proxy-check.mjs` computes a
doc-coverage score inside a composite, kasegi's `anchorcheck.py` resolves
`path:line` anchors and exits 0 on findings. **None implements an item → command
→ verdict contract**, so this round is adjacent rather than duplicative; the
shared shape worth aligning on — a stable-ID outcome ledger — is reported to the
integrator. The CDP 9222 / musketeer-profile lease question stays with kake.

## Hygiene

No vault access, no `op` item read, no `op.env` bytes read into any artifact, no
handler start/stop, no Chrome launch. No secret value, reference path, session
token or transcript row appears in any artifact — the one gate that execs `op`
(`op-ref-probe.sh`, delegated by row E5) runs over generated plain-value fixtures
and refuses any ref token before exec. All L2 execution was scratch-only; the
only live writes were the repo's own files and one temporary untracked file used
to falsify E4, removed in the same command.