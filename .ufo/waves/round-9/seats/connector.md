# ConnectorSeat — round-9 corpus review

**Seat:** aggregator lane; this is author-side evidence for the corpus-gate work, not a non-author review. All behavioral verdicts below target the pinned landed HEADs listed in C0, not a dirty worktree. Citations use `repo@short-commit:path:line` and are reproducible with `git show <commit>:<path>` / `git grep <commit> -- <path>`.

## C0 — measured revisions and dirty state

**Command run:** read-only `date -Is`, `git rev-parse HEAD`, `git -C <child> rev-parse HEAD`, and `git -C <child> status --short | wc -l` for main and the six children.

**Observed:** `2026-09-28T22:01:04-03:00`; main `383ea1ac252ee4b1a9ed6700eb6aa981a3992d8b` dirty 48; kasegi `b7180b0303755212ea4b60e52152aa8bf010c5b0` dirty 16; kagi `4b8c0183bd57ec5d0033fd07f650e116d7e9f600` dirty 10; kake `a2094411fe9051ebf3c10929ed33c1b6c032ea39` dirty 0; kengaku `f09ff1fc4d9e1e106d07c02b5bf9c148579175df` dirty 20; kotoba `63ceba7a0f73f7a576230c54aa164886ecbe7c47` dirty 7; kumitate `7a099b2b7df98a23f8f443763bec05ee8593403c` dirty 0. The dirty counts are context only. Snapshot verdicts below use the listed committed hashes.

## C1 — contract used

`PROTOCOL.md:352-384` §Gate requires: an explicit code-to-verdict map; a lane-owned self-test command with isolated fixtures, no live/network writes, and assertions for exit plus stable expected finding IDs; committed pinned values independent of recomputation; a distinct frozen-input run over mutable state with committed expected verdict and named revision; one owner registry row in that lane's `SKILL.md` with all eight fields (lane/gate identity, kind, entry command, verdict map, self-test spelling, pinned-value path, write scope, owner); explicit read-only/external-effect scope; and an integrator who verifies artifacts without running sibling code. Fleet-index entries are *pointers to the lane rows*, never copies of expected values. Closure says …

## C2 — registry-row sweep

**Command run:** at each C0 revision, `git -C <repo> grep -n -E '^\|[^|]+\|[[:space:]]*(gate|probe)[[:space:]]*\|' <revision> -- SKILL.md`; repeat the same row scan over the working-tree `SKILL.md`. Scope includes all six child lanes and main. The scanner prints paths/row counts only; it does not infer registry status from prose mentioning a script.

**Observed:** no matching registry row in any of the six child `SKILL.md` files, at landed HEAD or worktree; main has no lane `SKILL.md` in which an aggregator row could live. The four audited tool owners therefore have no row: kagi, kotoba, kengaku, kumitate. Additional routed gaps: kake's `probe-delta` is explicitly a report/probe, not a gate (`kake-shokunin@a209441: scripts/probe-delta.mjs:26`), but has no `probe` row; kasegi's Skill advertises an external claim-check path (`kasegi-shokunin@b7180b0: SKILL.md:681-684`), but has no row and its external source tree is absent (C5). The aggregator corpus-gate draft is also unregistered: its own source says the current inline registry has no aggregator Skill home (`.ufo/waves/round-9/corpus-gate.mjs:10-13`).

**Exact fleet-index content:** one routing record per gate/probe, containing only `(stable lane identity, gate name/routing key, pointer to the exact owning SKILL.md registry row)`. The pointer should be repo-relative and row-anchored, e.g. `kagi-shokunin/SKILL.md#<row-anchor>`. No verdict values, exit classes, self-test assertions, pinned values, expected findings, frozen-snapshot outcomes, or write-scope prose belongs in the index; those eight fields stay with the owning row. A lane with multiple gates gets one pointer per row. Do not copy the untracked aggregator draft's expected JSON into the fleet index.

## C3 — Gate-standard adoption matrix (eight requested tools)

The command spellings below are those documented by the lane's Skill/source and exercised in this session unless explicitly marked *not run*. A “frozen run: no” means the lane ships baselines/fixtures but the committed artifact sweep found no separate committed mutable-input snapshot **and** expected-verdict record. A self-test fixture is not that second evidence item. All eight `SKILL.md` row cells are absent per C2.

| Gate | Verdict map | Self-test spelling and observed assertions | Committed pinned values | Frozen snapshot run | Registry row / read-only scope | Owner |
|---|---|---|---|---|---|---|
| kagi `drift-pins.sh` | `0 clean / 1 drift / 2 setup-or-usage` — `SKILL.md:43`, `corpus/drift-pins.sh:19-25`. | `bash corpus/drift-pins.sh --selftest`; observed `DRIFT_SELFTEST: PASS (13 cases)`, exit 0. Source `:398-436` asserts exit and stable diagnostic tokens, but no registered stable finding-ID vocabulary is declared. | Yes: `corpus/drift-baseline.tsv` + `corpus/drift-symbols.tsv` (`SKILL.md:179-183`); independently committed host baselines. | **No.** Default compares live host files to the baselines; no committed host snapshot plus expected run verdict located. | **Missing.** Default verify is read-only; `--pin` changes the TSV baselines (`drift-pins.sh:365-368`) and must be excluded from a read-only verification row. | kagi |
| kagi `transcript-scan.sh` | `0 clean/warn / 1 hit / 2 setup-or-usage` — `SKILL.md:42`, `corpus/transcript-scan.sh:11-31`. | `bash corpus/transcript-scan.sh --selftest`; observed `SELFTEST OK (seeded hit + wal-resident hit detected; clean db passed)`, exit 0. Exercises seeded positive, clean and WAL cases and exit classes; source does not assert a stable finding ID. | **No independent expected-value file located.** Pattern/fixture expectations are in the script; no committed expected transcript DB/run pair. | **No.** Default audits the live transcript DB; self-test copies a DB into temp and does not create a frozen run record. | **Missing.** Source copies the DB to temp and does not open/write the live DB (`transcript-scan.sh:11-31`); declare this exact boundary in its row. | kagi |
| kagi `surface-census.sh` | `0 clean / 1 drift / 2 setup-or-usage` — `SKILL.md:34`, source `:48-72`. | `bash corpus/surface-census.sh --selftest`; observed `SELFTEST: PASS (16 cases)`, exit 0; `run_case` checks expected exit and token (`:747-768`). This is stable-token coverage, not a registry-declared finding-ID set. | Yes for live declarations: `corpus/surface-census.tsv` + `corpus/state-shape.tsv` (`SKILL.md:34,125-156`). | **No.** The default is a live-host census; self-test is separate and no committed frozen host input plus expected verdict was found. | **Missing.** Default census is read-only; `--verbs` is scratch-only but `--deep` can prompt/read a real custody record (`SKILL.md:35`), so a row must scope the default separately and gate `--deep`. | kagi |
| kotoba `verify_harness_claims.py` | `0 agree / 1 drift / 2 unreadable / 3 missing baseline` — `SKILL.md:199-203`, source `:22-35`. | `python3 verifiers/verify_harness_claims.py --self-test`; observed `0 failure(s) over 10 assertions`, exit 0. This tests its truncator/block-scalar model only; the r12 note expressly calls it a model-only self-test, not Gate conformance (`.ufo/reports/round-12/protocol.md:134-140`). | Yes: `verifiers/baseline.json` (`SKILL.md:191-203`). | **No.** Default recomputes live state against that baseline; no committed live-state snapshot/run plus expected verdict located. | **Missing.** Read-only verifier; its row must still distinguish test model from the mutable live-input gate. | kotoba |
| kotoba `verify_surfaces.py` | `0 pass / 1 drift / 2 unreadable / 3 missing baseline` — source `verifiers/verify_surfaces.py:107-110`. | `python3 verifiers/verify_surfaces.py --self-test`; observed `0 failure(s) over 75 assertions`, exit 0. Source `:732-913` asserts exit classes and stable `surfaces.*` check IDs. Default run observed all 7 checks PASS, exit 0. | Yes: `verifiers/surfaces-baseline.json` and committed fixtures (`SKILL.md:75-83`). | **No distinct frozen live run.** Fixtures cover self-test; default measures live binaries/surfaces. The committed artifact sweep found no separate expected verdict tied to a frozen host snapshot. | **Missing.** Source describes read-only deterministic measurement (`:107-110`); declare default entry and fixture-only self-test. | kotoba |
| kengaku `grader.py` | `0 pass / 1 mismatch / 2 missing-or-unreadable` — `grader.py:1-14`. | `python3 grader.py --selftest`; observed S0-S6 all PASS, exit 0; cases assert stable finding IDs. Default `python3 grader.py` observed `CHECKS n=280 mismatches=0 errata_pinned=1; VERDICT PASS`, exit 0. | Yes: committed evidence trees and stored summary bytes/hashes; Skill says it replays three committed probe trees and recomputes their asserted numbers (`SKILL.md:405-432`). | **Yes, strongest case:** default replays the committed probe trees and their expected summaries offline; the invocation in this evidence pins `kengaku@f09ff1f`. Caveat: the grader's stdout itself says `VERDICT PASS` but omits the measured revision; keep the revision alongside any retained verdict. | **Missing.** Offline, no network/endpoint (`grader.py:1-14`, `SKILL.md:407-409`). | kengaku |
| kumitate `scripts/round-gate.mjs` | `0 clean / 1 findings / 2 setup / 64 usage` — `round-gate.mjs:64-65`; stable finding kinds at `:67-88`. | `node scripts/round-gate.mjs --selftest` is the source spelling (`:45-48`). **Not run:** its self-test creates temporary Git repositories and invokes mutating `git init/add/commit/push/checkout` (`:694-746`, `:1061-1071`); this seat's read-only contract gates those host verbs, so no artifact was created. r12 records the lane's 57/57 self-test result at `.ufo/reports/round-12/protocol.md:159-160`; that is cited, not represented as this seat's run. | **Partial only:** expected finding kinds and thresholds are in source / `corpus/knowledge/round-close-gate.md`; no independent committed pinned-values file. | **No.** Default evaluates current report/repository state; synthetic self-test fixtures are not a committed frozen-input verdict. | **Missing.** Normal gate reads repo/report state; `--selftest` writes only fixtures, but the fixtures use real Git mutation verbs. Scope should explicitly separate those paths. | kumitate |
| kumitate `scripts/proxy-check.mjs` | `0 match / 1 drift / 2 fail-closed / 64 usage` — `proxy-check.mjs:79-82`. | `node scripts/proxy-check.mjs --selftest`; observed `PROXY_SELFTEST: PASS (55/55)`, exit 0; cases assert stable mismatch kinds. Default run observed `PROXY: MATCH (A=4 C=9 ... pins=4 match)`, exit 0. | Yes: `SCORECARD.md` `kumitate-proxy-v1` claim block holds computed terms and four script hashes (`SCORECARD.md:137-160`). | **No separate frozen run.** The block is a committed claim/pin set; the successful default invocation is not a distinct committed run record against a named frozen input revision. | **Missing.** Read-only derivation, no network/write (`proxy-check.mjs:97-104`); self-test uses temp fixtures. | kumitate |

**Matrix tally from C2/C3:** eight tools evaluated; every tool owner lacks a registry row. Among the requested set, only `grader.py` has a committed replay over its immutable evidence trees; the other seven need a distinct frozen-input/expected-verdict artifact (not merely a self-test). Registry absence alone makes none fully §Gate-conformant.

## C4 — bounties blast-radius sweep

**Command run:** read-only Python wrapper over `git grep -n -i -E` at each C0 commit. For children the scope was all tracked `SKILL.md`, `PROVINCE.md`, and `corpus/**`; main scope was `PROTOCOL.md`, `ROADMAP.md`, `.ufo/reports/**`; `~/.agents` scope was every readable `SKILL.md`. Pattern matched the `~/Projects/bounties`, `$HOME/Projects/bounties`, and absolute-home spellings. The wrapper counted literal occurrences, matching lines, unique files, and files swept; it emitted paths/counts, not unrelated line contents. Repeated sweep reproduced the same tuples.

| Scope at pinned revision | Occurrences / lines / files / scanned files |
|---|---:|
| kasegi `b7180b0` | 86 / 84 / 29 / 44 |
| kagi `4b8c018` | 0 / 0 / 0 / 50 |
| kake `a209441` | 0 / 0 / 0 / 36 |
| kengaku `f09ff1f` | 26 / 23 / 13 / 121 |
| kotoba `63ceba7` | 12 / 11 / 4 / 46 |
| kumitate `7a099b2` | 1 / 1 / 1 / 48 |
| main `383ea1a` | 29 / 29 / 17 / 90 |
| readable `~/.agents/**/SKILL.md` | 0 / 0 / 0 / 4 |

**Reproducible sweep command:** set `REPO`, `REV`, and `SCOPES` to the repository, pinned hash, and scope shown in C4 (children: `SKILL.md PROVINCE.md corpus/`; main: `PROTOCOL.md ROADMAP.md .ufo/reports/`). This Python wrapper calls the Git object scanner, counts matching occurrences/lines/files, and emits counts only:
```sh
python3 - <<'PY'
import os, re, subprocess
repo, rev = os.environ["REPO"], os.environ["REV"]
scopes = os.environ["SCOPES"].split()
pat = re.compile(r"(?:~/Projects/bounties|\$HOME/Projects/bounties|/home/[A-Za-z0-9_.-]+/Projects/bounties)", re.I)
ere = r"(~/Projects/bounties|\$HOME/Projects/bounties|/home/[[:alnum:]_.-]+/Projects/bounties)"
tracked = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", rev, "--", *scopes], text=True, capture_output=True, check=True).stdout.splitlines()
scan = subprocess.run(["git", "-C", repo, "grep", "-n", "-I", "-i", "-E", ere, rev, "--", *scopes], text=True, capture_output=True)
hits = lines = 0
files = set()
for row in scan.stdout.splitlines():
    parts = row.split(":", 3)
    if len(parts) == 4 and parts[0] in (rev, rev[:7]):
        _, path, line_no, text = parts
    elif len(parts) == 3:
        path, line_no, text = parts
    else:
        continue
    n = len(pat.findall(text))
    if n:
        hits += n
        lines += 1
        files.add(path)
print(f"occurrences={hits} lines={lines} files={len(files)} scanned={len(tracked)}")
PY
```
For the home-skill scope, the matching read-only sweep was `Path.home()/".agents".rglob("SKILL.md")`, reading each match and applying the same pattern; it returned 0/0/0 over 4 files.
```sh
AGENTS_ROOT="$HOME/.agents" python3 - <<'PY'
import os, re
from pathlib import Path
root = Path(os.environ["AGENTS_ROOT"])
pat = re.compile(r"(?:~/Projects/bounties|\$HOME/Projects/bounties|/home/[A-Za-z0-9_.-]+/Projects/bounties)", re.I)
files = list(root.rglob("SKILL.md"))
hits = 0
matched_lines = []
for p in files:
    for n, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
        count = len(pat.findall(line))
        if count:
            hits += count
            matched_lines.append((p, n))
print(f"occurrences={hits} lines={len(matched_lines)} files={len({p for p, _ in matched_lines})} scanned={len(files)}")
PY
```
The counts are literal citation occurrences, not a count of unique bounty projects. Kasegi's 86 occurrences break down to 38 in `SKILL.md`, 1 in `PROVINCE.md`, and 47 in `corpus/**` (scope command above). This is the missing Kasegi claim-package / registry blast radius; it points into the absent root in C5. Kagi's zero is a real corpus sweep result: this ref does not touch its vault/op inventory. Kengaku's 26 matches include two `PROVINCE.md` route/telemetry references (`PROVINCE.md:15,75`), but both are references to absent bounty telemetry storage, not its primary evidence root. Kotoba and kumitate hits are historical corpus references; no other lane `PROVINCE.md` was hit.

**C5 — root existence check and PROVINCE interpretation.** Command: `test -e` on both `~/Projects/bounties` and `~/projects/bounties`, then on Kengaku's `~/Projects/webzites/repos/llm-wiki` and parent `~/Projects/webzites`. Observed, respectively: `MISSING`, `MISSING`, `EXISTS`, `EXISTS`. Thus there is one unresolved primary domain root (Kasegi), not a second PROVINCE root. Kengaku's root exists; only its separately cited bounty telemetry surface is absent. This sweep does not claim that a similarly named folder elsewhere contains the missing repository.

## C6 — CORPUS rule 8 literal sweep and safe classification

`main@383ea1a:CORPUS.md:43-46` says vault ref paths (`op://…`) stay out of every corpus, including examples. The count command was a Python wrapper over `git -C <repo> grep -n -F -I 'op://' <revision> -- corpus/`; it counted literal occurrences and printed only file:line locations, never matched text. Every `op://` occurrence is therefore a literal rule-8 failure even when its prose intent is benign.

| Lane | Literal occurrences / lines / files | Safe source-context classification |
|---|---:|---|
| kasegi | 2 / 2 / 2 | schematic sweep-pattern quotations; all aggregator-owned |
| kagi | 77 / 75 / 26 | 77 schematic/example or source-pattern tokens; no resolvable real-vault value established without a vault read |
| kake | 2 / 2 / 2 | schematic sweep-pattern quotations; all aggregator-owned |
| kengaku | 1 / 1 / 1 | schematic sweep-pattern quotation; aggregator-owned |
| kotoba | 3 / 3 / 2 | 2 schematic lane-description examples + 1 aggregator-owned sweep-pattern quotation |
| kumitate | 1 / 1 / 1 | schematic sweep-pattern quotation; aggregator-owned |

Classification is from file/line context and placeholder/pattern role only; no vault was read and no credential value is reproduced. All 77 Kagi tokens are classified `schematic-placeholder`; `real-vault-path: 0 demonstrated`. This does **not** change the literal verdict: rule 8 still fails, including examples. The independent corpus-gate run below splits Kagi's 77 into 11 aggregator-owned and 66 Kagi-owned occurrences; it does not classify whether a vault item resolves.

**Kagi file:line locations (all occurrences, repeat line noted):**
- `corpus/drift-pins.sh:22`
- `corpus/knowledge/drift-gate.md:108`
- `corpus/knowledge/handler-on-disk-state.md:14,64,168,216`
- `corpus/knowledge/handler-trust-boundary.md:271`
- `corpus/knowledge/janitor-command-surface.md:17` (two occurrences)
- `corpus/knowledge/janitor-env-contract.md:72,74`
- `corpus/knowledge/janitor-lifecycle.md:29`
- `corpus/knowledge/op-cli-surface.md:18,19,24,114`
- `corpus/knowledge/op-env-refs.md:12,23,26,38,46`
- `corpus/knowledge/op-ref-consumption.md:54,55,56,109,123,142,298,301`
- `corpus/knowledge/surface-census.md:168`
- `corpus/knowledge/transcript-hygiene.md:10,18,47,98,144`
- `corpus/lessons/round-1-aggregator-seed.md:48`
- `corpus/lessons/round-1.md:33`
- `corpus/lessons/round-3.md:53`
- `corpus/lessons/round-4-aggregator-audit.md:40,41`
- `corpus/lessons/round-4.md:36,52,55`
- `corpus/lessons/round-5-aggregator-audit.md:14,16,17,18,19` (two occurrences), `63`
- `corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:7`
- `corpus/lessons/round-5.md:29`
- `corpus/lessons/round-8.md:21,56`
- `corpus/lessons/round-9.md:119`
- `corpus/lessons/round-12.md:37,115`
- `corpus/op-ref-probe.sh:27,184,185,186,188,189,221,290,591,620,621,622`
- `corpus/surface-census.sh:41,107,562,608`
- `corpus/transcript-scan.sh:16,84,202,242`

**Other-lane file:line locations:** kasegi `corpus/lessons/round-5-aggregator-audit.md:50`, `round-6-aggregator-audit.md:31`; kake those same filenames at `:54` and `:56`; kengaku `corpus/lessons/round-5-aggregator-audit.md:56`; kotoba `corpus/knowledge/sibling-description-rewrites-round8.md:141,151` and `corpus/lessons/round-5-aggregator-audit.md:83`; kumitate `corpus/lessons/round-5-aggregator-audit.md:79`.

**Revision reconciliation:** current `kagi@4b8c018` literal scan is 77/75/26. The old landed `kagi@4391b3b` snapshot run is separately verified `MATCH` below; the gate-draft reconciliation records that landed old tree as 54/53/23 and the earlier 55 as one hit present only in the then-dirty worktree (`.ufo/waves/round-9/seats/gate-draft.md:270-277`). The same note says current 4b8 is 77/75/26, reproduced by the gate. The disagreement is revision/worktree scope, not counting semantics.

## C7 — aggregator corpus-gate draft (author-side, provisional)

**Commands run:** `node .ufo/waves/round-9/corpus-gate.mjs --selftest`; then `--snapshot <lane> <pinned-revision> --json` for the six C0 children plus historical Kake `4c9a985ddce711b564df9e7cbdc912b6f5e74756` and Kagi `4391b3b68de22efbfee8228482ac5a50de0dc1b3`; `sha256sum` over the draft and expected JSON; and a safe JSON `measured`-timestamp validator. At this seat's run, observed `12/12 PASS`; all eight expected snapshots `MATCH` (Kasegi 49 findings, Kengaku 28, Kake current 37, Kake historical 34, Kumitate 36, Kotoba 75, Kagi current 51, Kagi historical 46). Snapshot invocations return gate exit 1 because the pinned corpora have expected findings; the expected result line is `MATCH`, not an execution failure. Kagi's current r8 breakdown was `op-ref occurrences=11 owner=aggregator` and `op-ref occurrences=66 owner=lane`, plus distinct bearer/kv-secret classes; total op-ref count 77.

Observed SHA-256 at this seat's run: `corpus-gate.mjs` `68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8`; `corpus-gate.expected.json` `c358e79a0ea92ca2901ca794da4ae0c30bad5f1fafc38a4ffc37b28d5810f9ba`. `git status --short` then showed both files untracked (`??`); current status was not checked after Main's subsequent re-verification. The seat-time JSON validator observed 8 entries and 8 invalid `measured` values shaped `2026-09-29T01:0xZ`. This was a draft defect at that point, not a current blocker after the update below. The draft's own no-SKILL registry admission (`corpus-gate.mjs:10-13`) remains a separate §Gate gap; the standard cannot be met by copying its inline registry into the fleet index.

The draft's claimed scope is corpus-rule conformance (`r2`, `r4`, `r7`, `r8`, `r10`) and SHONEN form; it does not parse kumitate's score arithmetic. Because this seat is the aggregator author, these runs are author-side measurement and are not independent non-author approval.

**Post-measurement integration update (Main-reported; not re-run by this seat):** Main reports that the L1 replaced all 8 invalid `measured` stamps with its re-run window start `2026-09-29T01:19:59Z`, recorded the substitution in `_provenance.l1_reverified`, reran all 8 snapshots to `MATCH` (finding counts 49/28/37/34/36/75/51/46), and reran `--selftest` with `12/12 PASS`. Per the ground-truth instruction this update is accepted without rerunning. The seat-time timestamp defect is therefore not an open finding. This does not establish that the draft is committed, and it does not cure the registry-home gap: Main reports that gap routed as D-127 + proposal P-v and the ledger makes no conformance claim until registrable.

## C8 — overlap seam and r12 L0 answers

**Overlap verdict: COMPOSE, NOT DUPLICATE.** `corpus-gate.mjs` evaluates corpus/SHONEN declarations and repo-level rule verdicts; `kumitate-shokunin@7a099b2:scripts/proxy-check.mjs:30-64` derives A/C/C1/C2 terms, checks both axis scores and the four pinned scripts recorded in `SCORECARD.md:137-160`. Both read the lane tree, but the asserted values differ: corpus-language/structure versus score arithmetic and script hashes. The gate draft does not rederive proxy math. Seam: aggregator gate may record/route a lane's proxy result, but must not copy its expected score pins or redefine the `kumitate-proxy-v1` claim block. Current evidence shows shared inputs, no duplicate verdict or conflict. The r12 report says the schema remains kumitate-owned and a fleet-wide mandatory block would be an AXES/MISSION operator decision (`.ufo/reports/round-12/protocol.md:347-353`).

**Owner clarification:** the measured `proxy-check.mjs` path is `kumitate-shokunin/scripts/proxy-check.mjs`, not kotoba; this evidence follows the repository and actual script owner.

**L0 answered by r12:**
- `kengaku|round-10`: **yes** — r12 `:341-344` says landed r10 modified the gate and calls for frozen rerun/named revision; §Gate `PROTOCOL.md:352-370` defines self-test, pinned values and frozen-run evidence.
- `kumitate|round-10`: **yes, policy decision** — r12 `:345-346` rules `(a)+(b), not(c)`; it explicitly leaves porting to the operator.
- `kumitate|round-11`: **answered as optional, not required by the standard** — r12 `:347-353` recommends a lane-local block, keeps schema kumitate-owned, and says fleet-wide status needs AXES/MISSION operator decision. Do not turn the recommendation into a gate requirement.

**Quoted §Gate clause (`PROTOCOL.md:362-366`):** “A gate whose verdict depends on a mutable fleet artifact also ships a run over a committed input snapshot with its committed expected verdict, so a later hand-edit of that artifact contradicts the frozen run. A verdict names the revision it was measured against: a gate grades the tree it runs on, so a run over a moving worktree is not comparable to one over the cited commit.” The adjacent self-test clause requires an isolated fixture, exit-code and stable finding-ID assertions, committed independent expected values, and says “a helper-only or model-only self-check does not satisfy this clause” (`PROTOCOL.md:357-361`).

**Quoted r12 answers (`.ufo/reports/round-12/protocol.md:341-353`):** “kengaku | round-10 (gate convention) → landed, modified: three-valued verdict rather than a uniform code map, self-test as capability rather than flag, pinned values by pointer, plus two requirements the question did not ask for and the evidence demanded — a frozen re-run for gates over mutable fleet artifacts, and a named revision per verdict. §Gate standard.” “kumitate | round-10 (driver-level adoption) → ruled (a)+(b), not (c); the driver port is operator-side at `scripts/shokunin-watchdog.sh:44`.” “kumitate | round-11 (machine-readable scorecard claim block) → RECOMMENDED, not required.” The §Gate text answers the Kengaku convention; r12 separately resolves Kumi's driver policy and scorecard requirement.

## C9 — command/evidence notes and blockers

- All filesystem/revision scans and gate snapshots used committed hashes; no git mutation, host write, network call, or vault read was performed. The kumitate round-gate self-test was deliberately not run: source shows it creates and pushes fixture Git repositories (`scripts/round-gate.mjs:694-746`); the would-be command is `node scripts/round-gate.mjs --selftest`, gated without artifact under the seat contract.
- Evidence numbers above are paired with the commands and observed outputs in C0-C8. The bounty occurrence counts are not unique-path counts; rule-8 `op://` classifications do not assert secret material or vault resolution.
- Outstanding actionable blockers for integration: (1) all 8 audited gate entries still need their owner `SKILL.md` registry rows; the aggregator gap is routed as D-127/P-v per Main; (2) 7 tools still need a distinct frozen-input/expected-verdict record; (3) the literal rule-8 conflict needs an operator decision or removal of schematic tokens; (4) Kasegi references must be routed against the absent source root. Main-reported timestamp repair/re-verification is not an open item for this seat.
