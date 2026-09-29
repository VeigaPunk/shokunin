# VerdictKagi — round 9 corpus verdict

Stamp: 2026-09-29T00:49Z; main HEAD `62fdfbe`; child landed revision `4391b3b`; `git rev-parse --short HEAD` observed `4391b3b`; `git status --porcelain | wc -l` observed `21`. Verdict is at landed HEAD only. Worktree-only changes are provisional. This is an aggregator-dispatched seat reviewing the aggregator's own prior child-repo artifacts; under PROTOCOL authorship this is lane-owned, not independent non-author evidence.

## Dirty tree and attribution

Command: `git status --porcelain`; observed 17 modified + 4 untracked = 21 entries. Modified: `LOG.md`, `PROVINCE.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, `corpus/README.md`, `corpus/claim-ledger.sh`, `corpus/claim-ledger.tsv`, `corpus/drift-symbols.tsv`, `corpus/knowledge/{claim-ledger,drift-gate,janitor-command-surface,op-env-refs,surface-census}.md`, `corpus/lessons/{round-11,round-8-aggregator-box3-coldrun}.md`, `corpus/stamps.tsv`; untracked: `corpus/knowledge/op-ref-consumption.md`, `corpus/lessons/{round-12,round-13}.md`, `corpus/op-ref-probe.sh`. Command: `git status -sb`; observed `master...origin/master [ahead 3]`. The three unpushed commits (`e0a04d8`, `7c3377c`, `4391b3b`) are aggregator identity (`aggregator-shokunin <aggregator@shokunin.local>`); current 21-entry r13 edits are lane in-flight. Any decisive text in those 21 entries is provisional.

## Rule-10 verdict at 4391b3b

| Rule | command + observed | grade |
|---|---|---|
| 1 source citations | `git ls-tree -r --name-only 4391b3b corpus/knowledge`; 16 tracked knowledge entries. `git show 4391b3b:corpus/README.md` coverage map names entries and source basis. | PASS-intent; sampled index/source basis is present |
| 2 lesson round/evidence | `git ls-tree -r --name-only 4391b3b corpus/lessons`; 17 tracked lessons. `git show 4391b3b:corpus/README.md` maps lessons to rounds and evidence. | PASS-intent |
| 3 falsifiable/opinion | `git show 4391b3b:corpus/README.md`; entries state inspection sources and explicit bounds/negative claims. | PASS-intent |
| 4 count carries command/date | `git show 4391b3b:SCORECARD.md` L16 claims 16-row table/15 checklist/25 anti-patterns but carries no inline counting command; `git show 4391b3b:corpus/lessons/round-9.md` also preserves count prose. | FAIL (known D-65 stale count claim) |
| 5 negative carries sweep | `git show 4391b3b:corpus/knowledge/handler-on-disk-state.md` and `lessons/round-4-aggregator-audit.md` contain sweep commands beside negative claims. | PASS-intent; not every inherited claim is mechanically clean |
| 6 quote location | `git show 4391b3b:corpus/README.md`; source rows identify script/file surfaces; `janitor-command-surface.md` cites `cmd_refs L228–235`. | PASS |
| 7 index rows are claims | `git show 4391b3b:corpus/README.md`; map contains rows for files present at HEAD. | PASS-intent; no independent full parity proof in this seat |
| 8 literal secret/ref exclusion | `git grep -n 'op://' 4391b3b -- corpus/` observed 54 literal occurrences; all observed classes are prose, mechanism descriptions, sweep patterns, or schematic placeholders such as `op://vault/item/field`; no resolvable real-vault path observed. Per literal CORPUS.md text this is **FAIL-literal / PASS-intent**, not clean. No secret values printed. | FAIL-literal / PASS-intent |
| 9 append-only/no cross-lane edits | `git log --format='%h %an' --name-only e64e81b..4391b3b`; the three commits touch aggregator-owned round-8 lesson only; current modified corpus files are in-flight and attribution is provisional. | PASS at landed commits; provisional for dirty deltas |
| 10 per-round verdict | This file emits the per-repo verdict with commands and revision. | PASS for duty |

**Rule-10 verdict:** **not conformant — rules 4 and 8 literal text** at `4391b3b`. This supersedes the stale §11.1 row (`not conformant — 4 only`, 6 majors/10 defects). Rule 8 classification: 54 hits, all schematic/prose/mechanism or sweep-pattern placeholders; no real-vault path observed, but literal rule 8 forbids `op://…` text, so FAIL-literal/PASS-intent.

## Box-3 re-run at landed HEAD

Round-8 lesson `corpus/lessons/round-8-aggregator-box3-coldrun.md` recorded `[x]` provisional at old dirty HEAD `301b9ec`; 26 commands, 26 ok, 7 gated (1 with artifact/6 without), 7 break points. Re-runs using archived `4391b3b` bytes:

- **Firm:** `bash corpus/drift-pins.sh` → `DRIFT_PINS: CLEAN (files=15 symbols=19)`, exit 0; `--selftest` → `DRIFT_SELFTEST: PASS (13 cases)`, exit 0. `surface-census.sh` → CLEAN `(assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)`, exit 0; `--selftest` PASS (16), `--verbs` CLEAN `(pass=7 skip=3)`, exit 0. `the-janitor --help/status/cdp-bridge status/tac-check` exited 0; `whoami` exited 1 with signed-out diagnostic. These are executable and reproducible at the landed tree.
- **Break:** `claim-ledger.sh verify` → `FAIL R11-08 exit=1 want=0; CLAIM_LEDGER: FAIL (claims=11 failed=1 stamped=28...)`, exit 1; `citations` → `CITATION_GATE: BROKEN (... unresolved=40)`, exit 1. Thus the prior `[x]` chain is not fully green at 4391b3b.
- **Break:** `transcript-scan.sh` → exit 1, `HITS=2`, `cells=888`, `credential` tripwire rows 0; this is a known baseline defect (D-104), not a secret-value echo.
- **Still provisional:** the prior `op-ref-probe.sh` command and its 15-case selftest are untracked worktree-only; HEAD archive has no such file. Prior lesson's 602-line dirty SKILL claims and 20-symbol dirty drift TSV are not landed. Worktree-only decisive edits cannot firm the grade.

**Box-3 result:** **break / remains provisional**, not firm `[x]`. The landed gates show executable surfaces, but claim-ledger and transcript gates fail and the decisive probe is absent from HEAD.

## Drift gate against PROTOCOL §Gate standard

- Verdict: normal run at `4391b3b` exited 0 CLEAN; selftest exited 0 PASS (13 cases). Exit vocabulary is 0 clean / 1 failed in script/docs; no undeclared nonzero observed in these runs.
- Self-test: 13 scratch cases are committed in `drift-pins.sh`; output asserts stable case outcomes and exit codes. **Conforms.**
- Two evidences: committed baseline/symbol TSVs provide 15 file pins/19 symbol pins and the selftest is committed. The normal run is against mutable host files; the committed falsified-baseline recipe is documented. **Partial/conditional**: no separate committed real-input snapshot artifact beyond TSV declarations and selftest fixtures.
- Registry: `SKILL.md` landed decision table row 40 gives entry command, exit semantics, and pinned paths; it does not expose every §Gate registry field (explicit owner/write-scope row absent). **Partial.**
- Scope: observed scripts use scratch temp trees for selftest/verbs and normal probes do not write the pinned host files. **Conforms.**
- Closure: red findings are routed as corpus defects (D-104 etc.); lane/integrator closure remains required.

L0 `cmd_refs` defect remains open: `~/.local/bin/the-janitor` L228–235 uses `v ~ /^op:\/\// ? v : "<redacted-non-op-value>"`, a prefix match that echoes any value beginning `op://` including plaintext tail. `surface-census.sh --verbs` at HEAD reported `refs-redaction-prefix-only: PASS unredacted tail rides out`; this confirms the defect remains. The probe emitted no secret value: outputs were counts/names only; credential tripwire was 0. Report only presence/absence, never values.

## Movement / D-63 / D-65

D-63: `git show 4391b3b:SHONEN.md | awk '/^- \[/{print NR ":" $0}'` observed four `[x]` marks. `git grep -n KagiR9Reviewer 4391b3b -- .` resolves only to the SHONEN line and historical lesson mentions; no committed verifier report bearing that id. **D-63 remains open; promotion mark fails.**

D-65: `git show 4391b3b:SCORECARD.md` L16 still claims 16-row decision table, 15-item checklist, 25 anti-pattern bullets and per-entry Source basis without inline counting commands. The landed scorecard is still the falsified card; worktree corrections, if any, are provisional. D-65 remains open. Compared with §11.1's 6 majors/10 defects, landed evidence adds rule-8 literal failure and confirms D-63/D-65 plus gate failures; movement is not conformant.

## Worktree-only safety

No child repo was modified by this seat. Archive command: `git archive 4391b3b | tar -x -C /tmp/kagi-r9` exited 0 and produced 50 files. Secret values were not printed. Main HEAD at stamp was `62fdfbe`; child HEAD remained `4391b3b` on the final immediate check.
