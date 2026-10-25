# kumitate round-34 — non-author verification

Reviewer: W3ReviewKumitate, orchestrator-dispatched, non-author. This is a recommendation, not admission or adjudication. Reviewed lane `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin`, base `16a5441a3`, round head `1a8eed5aaa32043cf109dd28ceb5cd37ccd5555e`.

**Recommendation: reject pending correction of the sources gate's false-clean cases below.** The headline before/after measurements reproduce; the claimed gate capability has concrete enforcement gaps. Do not discard the verified knowledge additions or reinterpret the held operability integer as an integer gain.

## Findings, by severity

### Medium — rejected rows need not carry a flip condition to pass even strict mode

Location: `scripts/sources-check.mjs:250-251`; contract `SOURCES-CONTRACT-v1.md`, Shape/teaches; capability promise `SCORECARD.md:1609`.

The contract requires rejected `teaches` cells to contain a reason **and** `flip:` condition. The new gate emits `REJECTED_NO_FLIP` only if **both** marker strings are absent. Consequently, a row with `REJECTED: outside scope` and no flip condition passes. Conversely, a row containing only `flip:` evades the same branch. The former was exercised; the latter follows directly from the conditional and was not separately run.

Reproduction: create an isolated registry containing the required headings and a well-formed rejected row whose teaches cell is `REJECTED: outside scope`, then run:

```sh
node /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin/scripts/sources-check.mjs --self /tmp/kaika-verify/kumitate/rejected-no-flip --today 2026-10-19 --strict
```

Observed, exit clean:

```text
SOURCES  info  LEGACY_NO_HEADER  count=1
SOURCES_CHECK: CLEAN (rows=1 tiers=A:1,B:0,C:0 status=queued:0,mined:0,rejected:1 entries_with_source=0 legacy=1)
```

The fixture also contained the unheadered entry described below. The registry defect is independently attributable to the displayed boolean condition. Existing rejected rows in the actual round do contain flip conditions; this finding concerns the new gate's advertised enforcement, not a fabricated defect in those rows. Fleet-validator parity does not establish conformance to the stronger written row contract.

Required correction: require both markers, with finding-id/exit assertions for each missing half. Update the capability/report to distinguish machine checks from human review.

### Medium — an admitted entry can lose its source header and silently become legacy

Location: `scripts/sources-check.mjs:281-285`; admission bar `corpus/QUALITY.md:12-17`; capability promise `SCORECARD.md:1609`.

Any knowledge file whose first line does not start with `source:` is automatically exempted as legacy. There is no persisted legacy identity set or admission boundary. A newly created file, or a new entry whose source line is removed, therefore bypasses all source-id, verified-at, and recheck validation, including under `--strict`.

The same exercised fixture contained a newly created `corpus/knowledge/new-entry.md` beginning with a Markdown title and no header trio. The command above reported `LEGACY_NO_HEADER count=1` and CLEAN. The file was newly created by this reviewer, not inherited legacy content.

Preserving the actual historical headerless corpus is reasonable; treating every future headerless file as historical is not an effective admission guard. Required correction: distinguish grandfathered identities from newly admitted entries, or explicitly narrow the advertised gate capability and provide an enforced admission check elsewhere. Add a mutation covering removal of a newly admitted entry's source header, not only removal of the other header fields.

### Low — incorrect report pointer for saturation

Location: fleet report `kumitate.md:22`: it points to the saturation declaration at `SCORECARD.md` line 9. That line is an unrelated membrane-seal note. Command `grep -n '^## Saturation' SCORECARD.md` located the section at `1613`; declaration follows there. Correct the report pointer. The declaration itself exists and is honest about operability remaining below its saturation line.

## Verification environment and method

- Base/head snapshots were extracted with `git -C <lane> archive <revision> | tar -x -C <scratch>`. Origin-dependent comparisons used `git -C /home/vgpnk/Projects/ufo-fsd-alpha archive 964f443ee53df0ce06bd689af01f0dea031b01f9 | tar -x -C <scratch>/origin`, matching the report's stated input revision.
- LSP is unavailable: reading `xd://lsp` returned `No such tool`. No semantic references/definition/diagnostics result is claimed. Text inspection is literal fallback, not semantic proof.
- Tests and counting commands were explicitly authorized by this assignment. No lane edits, staging, commits, branch switches, pushes, integration, judge invocation, or alternative agent runtime were performed.
- Source pages and report text were treated as data. No source-page instructions were followed.

## Provenance and append-only checks

Command:

```sh
git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 16a5441a3..1a8eed5aa
```

Observed round commit: `1a8eed5`, author and committer both `kumitate-shokunin <kumitate@shokunin.local>`, subject beginning `round-34:`. Provenance: **verified**.

Command:

```sh
git -C <lane> diff 16a5441a3..1a8eed5aa -- LOG.md corpus/lessons corpus/QUALITY.md
```

Deleted prior lines: **none**. The inspected diff contains an appended LOG hunk and new QUALITY/lesson files. The analogous SOURCES diff also has no removed lines; `git cat-file -e 16a5441a3:corpus/SOURCES.md` confirms it was absent at base. No prior source-cell edits need old→new accounting.

SCORECARD/current measurement values and scripts changed in place, but these are not the files in the assignment's append-only check. Their updates are not presented as append-only violations. In particular, synchronizing declared values after real documentation changes is not itself proof of metric manipulation.

## Per-claim measurements and recommendations

All counts below carry their command. Counts were run in the extracted base and head trees unless a lane-worktree run is named.

### Claim A — operability walk and sources-registry capability

| Measurement | Command | Base output → head output | Result |
|---|---|---|---|
| Runnable script count | `ls scripts/*.mjs | wc -l` | `6` → `7` | verified |
| Checklist count | `grep -c '^\s*- \[' SKILL.md` | `11` → `13` | verified |
| Gate-registry rows | `grep -c '^| [a-z-]* | gate |' SKILL.md` | `0` → `7` | verified |
| Operability proxy | `(A+C)/(A+C+3)`, using preceding command outputs | `17/20 = 0.85` → `20/23 ≈ 0.869565`; floor of ten times each is `8` | verified; integer held |
| Registry present/rows | `git cat-file -e <revision>:corpus/SOURCES.md`; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | absent → `20` | verified |
| Registry gate | `node scripts/sources-check.mjs` | script absent → CLEAN output below | verified on supplied registry |
| Registry selftest | `node scripts/sources-check.mjs --selftest` | script absent → `SOURCES_SELFTEST: 34/34 pass`, `VERDICT: PASS` | verified |
| Proxy selftest | `node scripts/proxy-check.mjs --selftest` | `PROXY_SELFTEST: 102/102 pass` → `103/103 pass` | verified |

Observed gate output, exit clean:

```text
SOURCES  info  LEGACY_NO_HEADER  count=38
SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)
```

**Claim verdict:** measurements **verified**; capability as an admission/header/flip enforcement gate **not-verified** because of the exercised false-clean cases. The operability fraction improves, and working the lowest axis does not require inventing an integer increase. The score remains held, as the lane disclosed.

Additional independent mutations: appending a community/tier-A row produced `SOURCES_CHECK: DRIFT (TIER_INFLATION)`, exit failed; appending a duplicate id produced `SOURCES_CHECK: DRIFT (ID_DUPLICATE)`, exit failed. These demonstrate meaningful rejection paths but do not eliminate the findings above.

### Claim B — coverage:kimi-layer, live-derived restoration

Commands:

```sh
node scripts/proxy-check.mjs --src <origin-964f443-snapshot>
node scripts/proxy-check.mjs --strict --src <origin-964f443-snapshot>
node scripts/kimi-census.mjs
node scripts/kimi-census.mjs --selftest
```

Base proxy result:

```text
PROXY: DRIFT (K_MEMBERS_DRIFT term=K_members declared=49 computed=50 delta=+1; COVERAGE_KIMI_DRIFT term=coverage_kimi declared=10 computed=9 delta=-1; AXES_DRIFT term=coverage:kimi-layer declared=10 computed=9)
```

Head proxy result:

```text
PROXY: MATCH (A=7 C=13 operability=8; C1=19/19 C2=77/77 coverage=10; S=91/91 coverage:script-layer=10; R=83/92 coverage:runtime-layer=9; K=50/50 coverage:kimi-layer=10; pins=7 match)
```

Strict proxy exit: base failed, head clean. Base census totals: `members=50 checked=50 errors=2`, verdict `KIMI_CENSUS: DRIFT (UNLISTED skills/; UNLISTED mcp.json)`. Head: `members=50 checked=50 errors=1`, verdict `KIMI_CENSUS: DRIFT (UNLISTED mcp.json)`. Census selftests: `KIMI_CENSUS_SELFTEST: 43/43 pass` → `45/45 pass`.

Shape-only check: `stat -c '%F %s %a %y' ~/.kimi-code/skills/cursor-lane/SKILL.md` returned regular file, `2465` bytes, mode `644`, modified `2026-10-18`. Directory listing showed the real cursor-lane directory alongside the existing symlink children. No credential-bearing runbook contents were reopened for this review.

Command `strace -f -e trace=openat,openat2 -o <scratch>/strace-head.txt node scripts/kimi-census.mjs`, followed by counting `kimi-code/mcp.json` in that trace, observed **no matching opens**. This is evidence about the traced syscall set, not proof about untraced processes.

**Claim verdict: verified** as the explicitly named live-derived restoration. The recorded base score already said `10`; the computed base on this host was `9`. Do not recast the result as a historical recorded integer gain. Adding coverage for a newly present child is substantive; the unchanged live enumeration rule distinguishes this from adding root mcp.json to the declared registry.

## Recommended per-axis verdicts

Command basis for this table: base/head `node scripts/proxy-check.mjs --src <origin-964f443-snapshot>`, with the counts above. Saturation was inspected in `SCORECARD.md` under `## Saturation`.

| Scored axis | Recommendation |
|---|---|
| operability | improved underlying executable fraction; score held at `8`; capability admission blocked by findings |
| coverage (parent/index proxy) | unchanged at `10`; index growth is real and matched |
| coverage:script-layer | unchanged at `10` on the pinned comparison; live external origin computes `9`, disclosed drift, not caused by this diff |
| coverage:runtime-layer | unchanged at `9` on the pinned comparison |
| coverage:kimi-layer | improved/restored computed coverage `9` → `10`, not a new historical recorded integer |

The report's saturation posture is honest: operability is still below the declared saturation line, so the stagnation waiver is not asserted. No fresh native-runtime behavior or resume implementation was introduced by these changes. The pre-existing runtime baseline/admission ambiguity remains disclosed debt, not silently ratified by this review.

## SOURCES contract validation

Exact required command:

```sh
bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin
```

Observed output:

```text
kumitate-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin/corpus/SOURCES.md
```

Exit clean. The contract's census commands from its Census section were also executed: row count `20`, malformed `0`, tiers `A=19 B=1`, status `mined=9 queued=9 rejected=2`; duplicate ids, enum/tier violations, and missing mined used-by paths printed nothing. The latter are observations of those literal checks, not broader semantic proof.

### Reopened source sample and quote/anchor checks

Quotes below are each within the assignment's word limit. Locations are the round lesson's Gate and the corresponding source section.

| Source | Reopen command / location | Result |
|---|---|---|
| S001, new tier-A OMP docs | `curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/tools/task.md`; Limits & Caps | Gate idle-TTL quote located at source line `169`; concurrency default located at line `167`. Content verified against the reopened main page. |
| S002, new tier-A Hub docs | `curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/agent-hub.md`; Related surfaces | “Messaging a parked or killed subagent revives it.” located at source line `118`, matching `corpus/lessons/round-34.md:96`. |
| S018, new tier-A original paper | reopen `https://arxiv.org/abs/2503.13657`, Abstract | “This process identifies 14 unique modes, clustered into 3 categories” matches `corpus/lessons/round-34.md:112`. |
| S019, rejected | `curl -fsSL https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices`; Confused Deputy Problem | “MCP proxy server uses a static client ID with a third-party authorization server” located, matching the Gate quote. HTML formatting/line breaks do not alter its words. |
| S020, rejected | `curl -sIL https://docs.langchain.com/oss/python/langgraph/durable-execution`; reopen persistence page and its `.md` twin | Redirect to persistence confirmed. Gate checkpointer quote located under Checkpointer vs. store. A `durability-modes` anchor remains, but the markdown body does not enumerate the claimed modes; the anchor alone is not a counterexample to the rejection rationale. |

Other reopened quotations included the MCP changelogs, Kimi docs, Codex commands, Temporal idempotency, and the Anthropic/Cognition posts. Only the explicit sample above is needed for the sampling threshold; no historical opening event is inferred from a successful reopening now.

## Discernment spot-check table

| Candidate / Gate decision | Non-author spot-check | Reason |
|---|---|---|
| `kimi-mcp-plane.md` — admit | **agree** | Header trio present; MCP levels, project precedence, trust gate and configuration defaults match opened docs. UNKNOWN/[INFERENCE] boundaries are explicit; host file remains shape-only. |
| `omp-task-contract.md` — admit | **agree**, with revision-verification gap | Batch shape, limits, hub revival, discovery precedence and source recheck counts match reopened docs; source facts are distinguished from installed-runtime observations. |
| S019 — reject | **agree** | Confused-deputy/OAuth material belongs to the adjacent security province, explicitly routed in `PROVINCE.md:26`. |
| S020 — reject | **agree** | Locator redirect is real; the remaining bare anchor does not supply the missing durability-mode discussion. |
| `sources-registry` gate capability — admit | **disagree as currently described** | The supplied registry passes, but the new gate also declares clean for the exercised missing-flip and new-headerless cases. Passing selftests alone does not establish the advertised admission guard. |

The new cursor-lane section is in an existing legacy file, not a newly created knowledge file. This review does not invent a mandatory whole-file migration for that edit; the substantive enforcement problem is the absence of any reliable boundary between grandfathered entries and future ones in the new gate.

## New knowledge entry rechecks

Header check command, for each new file: count `^source:`, `^verified-at:`, and `^recheck:`. Each is present in both `corpus/knowledge/omp-task-contract.md` and `corpus/knowledge/kimi-mcp-plane.md`.

Commands from their recheck headers reproduced:

```text
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/tools/task.md | wc -l                         => 218
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/agent-hub.md | wc -l                         => 123
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/task-agent-discovery.md | wc -l              => 341
omp --version                                                                                                    => omp/18.12.3
curl -fsSL https://moonshotai.github.io/kimi-code/en/customization/mcp.md | grep -c 'User level'                      => 1
curl -fsSL https://moonshotai.github.io/kimi-code/en/customization/mcp.md | grep -c 'mcp.json'                        => 7
curl -fsSL https://moonshotai.github.io/kimi-code/en/configuration/config-files.md | grep -c 'startup_timeout_ms\|tool_timeout_ms\|default_deferred' => 4
~/.kimi-code/bin/kimi --version                                                                                   => 2.2.0
stat -c '%F %s %a %y' ~/.kimi-code/mcp.json                                                                        => regular file, 249 bytes, mode 644, mtime 2026-10-15
```

The table's grep count is not by itself proof of exactly the documented keys; the opened configuration table was additionally inspected and contains the stated startup timeout, tool timeout, and deferred-default fields. No MCP session was started.

Lane-worktree `node scripts/cite-check.mjs --json` was parsed per file: new knowledge files, round lesson, QUALITY and SOURCES each had no error findings. Existing SKILL had `9`, skills/plugins `10`, README `31`, matching the report's disclosed live values. Earlier archive-only runs produced different counts because source/fleet lookup roots were not equivalent; they are not evidence of new citation defects, and the exact base pinned citation totals were not fully reproduced.

## Trends

| Trend | Recommended verdict | Evidence |
|---|---|---|
| expansion | **improved** | New sourced knowledge files and coverage-map entries exist. Header census `grep -l '^source:' corpus/knowledge/*.md | wc -l` gave base `0`, head `2`. Base literal sweeps for `mcp.json` and upstream task/Hub doc URLs returned no matching files. |
| quality | **unchanged pending gate correction** | Knowledge rechecks and the skills/plugins erratum are useful, but the claimed admission-tool improvement has concrete false-clean cases. Gate counts and selftest counts alone do not establish corpus-quality improvement under LEARNING. No false/stale knowledge claim is alleged from the sampled entries. |
| discernment | **unchanged pending resolution of disagreement** | Agree on the sampled knowledge admits and rejected sources; disagree on capability admission. The lane's own critic is not the independent verifier. This report supplies the outside disagreement; orchestrator should record its disposition rather than accept self-attested improvement unchanged. |

## Credential sweep and report conformance

Required credential command:

```sh
git -C <lane> diff 16a5441a3..1a8eed5aa | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'
```

Observed: no output; grep no-match exit. Additional hex-shaped hits were inspected in context and were commit/object ids or sha256 pin values, not credentials. The cursor-lane section's keyword scan found no credential-pattern hits. No personal address is reproduced here.

Required report sections are present in order, including Sources & frontier, Mistakes, Trend verdicts, L0 questions, and Integrator notes. Report cites the round commit and uses asserted SHONEN markers rather than unchecked claims of named non-author verification. The incorrect saturation pointer is the concrete report defect above.

Command run in the actual lane worktree:

```sh
node scripts/round-gate.mjs --round 34 --reports-dir /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/reports --main-repo /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger
```

Observed `ROUND_GATE: CLEAN (round=34 lane=kumitate checks=10 errors=0 warnings=0)`.

## Residual risk and verification gaps

- Strict claims gate is already red at both base and head. Command `node scripts/claims-check.mjs --strict --src <origin-964f443-snapshot>` exits failed in both, with the same S2/R9 membership warnings and R5/R7 section absences. This is unchanged debt, not a newly introduced regression or a clean strict-family claim.
- Live origin drift persists. `node scripts/proxy-check.mjs` at head reports script member/section drift and computed script coverage below the pinned score. Both commits show the same external script-layer drift; pinned no-harm comparisons do not make the live gate green.
- Source-page reopening verifies present content, not the historical act of opening. GitHub API rate limiting prevented full reconciliation of per-path revision metadata. The cited `81fa40e` commit page is reachable; it need not itself modify every file observed at that repository revision. No revision contradiction is asserted merely from differing per-file last-change identifiers.
- Reported isolated claim-separability reconstructions and the lane mutation-tester's survivor counts were not independently recreated. The custom counterexamples in this report are separate, exercised tests.
- L2 dispatch receipts, verbatim Godspeed prompt inheritance, provider-exhaustion rerouting identity/continuity, and canonical native-run preflights were not authenticated from artifacts supplied in this assignment. No runtime admission, same-identity reroute guarantee, or `resume_continuity_v1` zero-mutation guarantee is inferred from report prose. No changed resume implementation is alleged.
- Broader untouched selftest totals were not rerun; only the named gate selftests and commands recorded above were exercised.
- This review is read-only for lane/fleet repositories. Temporary verification files under the assigned scratch directory were removed. Early scratch files accidentally created directly under `/tmp/kaika-w3-*` were also removed; this reviewer-side scope slip is disclosed and not attributed to the lane. The final review artifact is the only intended output.

## Integrator handoff

Retain the reproduced counts and verified knowledge. Repair the rejected-row and new-entry admission checks, add the corresponding cheap-fake tests, correct the report pointer, and then obtain a targeted non-author recheck. Record this review's disagreement and the resulting disposition in the canonical closure/lesson record. Until then, recommendation remains **reject**, not an executed admission decision.

---

## 2026-10-19 — targeted non-author recheck of post-review repairs (appended; original above unchanged)

Reviewer: W3ReviewKumitate (same non-author seat, fresh dispatch from Main's IRC). Target: lane HEAD `6336d712d7634c541ca5d60dd707f17ea2563ed7` (`round-34: correct saturation pointers`), with `06757b0` (`round-34: post-review fixes`) on top of `1a8eed5aa`. Lane worktree `git status --porcelain` → 0 lines before and after this recheck. Scratch: `/tmp/kaika-verify/kumitate-recheck-review` (fresh; no earlier scratch reused; `git archive` of `6336d71`, `1a8eed5aa`, `16a5441a3`, and origin `964f443`). No repository writes, no commits, no lane report edits.

Scope: the two false-clean findings, the critic off-Registry case, and the frozen v1 identity. My reading of "critic off-Registry case" is a column-0 registry-shaped row placed outside `## Registry` (fixture m3 below); the critic's original wording is not in my inputs.

### Repaired / unrepaired

| # | Item from the first review | Status | Evidence (command → observed) |
|---|---|---|---|
| 1 | Rejected row without `flip:` passed (Medium) | **repaired** | m1: `S019` teaches with `flip:` removed → `SOURCES  error  REJECTED_NO_FLIP … id=S019`, `SOURCES_CHECK: DRIFT (REJECTED_NO_FLIP)`, exit 1. m9: `REJECTED:` removed, flip kept → `REJECTED_NO_REASON`, exit 1. m8: teaches cell emptied → `ROW_FIELD_EMPTY`, `REJECTED_NO_REASON`, `REJECTED_NO_FLIP`, exit 1. Both halves independently enforced. |
| 2 | New headerless knowledge file passed as "legacy" (Medium) | **repaired for direct entries** | m2: new `corpus/knowledge/new-entry.md` (no `source:`) → `ENTRY_HEADER_REQUIRED corpus/knowledge/new-entry.md:1`, `DRIFT (ENTRY_HEADER_REQUIRED)`, exit 1. m10: `verified-at:` line emptied in `kimi-mcp-plane.md` → `HEADER_INCOMPLETE`, exit 1. **Residual (Low, unrepaired):** m6, a headerless file in `corpus/knowledge/sub/x.md`, → `CLEAN`, because the census scans direct `*.md` children only. The post-review text says "headerless non-base knowledge files are errors"; subdirectories are outside that wording. |
| 3 | Critic off-Registry case: row outside `## Registry` (Medium) | **repaired for column-0 rows** | m3: `| S021 | … |` appended after `## Leads` → `ROW_OUTSIDE_REGISTRY corpus/SOURCES.md:120`, `DRIFT (ROW_OUTSIDE_REGISTRY)`, exit 1. Fleet census agrees: `sources-census.sh validate` on m3 → `m3 E12 S021 row outside Registry section`, exit 1. **Residual (Medium, unrepaired):** m4, `  | S022 | …|` (two leading spaces) outside Registry → `CLEAN`, exit 0. m5b, `  | S023 |  | docs | Z | …` (leading spaces, empty source, invalid tier Z) inside Registry → `CLEAN`, exit 0, and the row is silently dropped (the rows count stays 20). GFM renders 1–3 leading spaces as a table, so these rows are real rows to a reader. The fleet awk census (`^\|`) shares this blind spot: `sources-census.sh validate` on m4 and m5b → `ok`, exit 0. The gap is therefore in the frozen contract's parsing rule as well as the lane gate. |
| 4 | Frozen v1 identity (`kumitate-proxy-v1`, parent 23 keys) | **repaired** | Key names of the stanza, base `16a5441` vs head `6336d71`: `diff` of sorted `^key=` names → identical, 23 keys (`KEYNAMES_IDENTICAL`). Values differ only by round-34 term movement (A 6→7, C 11→13, C2 74→77, K 49→50, pins). Six pins match `sha256sum scripts/<name>.mjs` for proxy-check, kimi-census, claims-check, round-gate, cite-check, surface-probe. `pin.sources-check` absent. Proxy selftest `PROXY_SELFTEST: 104/104 pass`, including `STANZA_KEY_UNKNOWN: parent-frozen v1 rejects pin.sources-check`. |
| 5 | Frozen 38-path legacy identity | **repaired / verified** | Extracted `LEGACY_KNOWLEDGE_FILES` from head `scripts/sources-check.mjs` and diffed it against the base `corpus/knowledge/*.md` listing at `16a5441`: `entries 38 unique 38`, diff empty (`IDENTICAL_TO_BASE_38`). Selftest `frozen 16a5441 legacy identity set has 38 unique paths` passes. |
| 6 | Rejected `teaches` substring matching (new, Low) | **unrepaired** | m7: `reflip: an orchestration-only clause` replaces `flip:` → `CLEAN`, `--strict` exit 0. The check is `includes('flip:')`, which matches inside longer words. |

### Realgate output (head `6336d71`, lane worktree, read-only)

```text
node scripts/sources-check.mjs
SOURCES  info  LEGACY_NO_HEADER  count=38
SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)            exit 0
node scripts/sources-check.mjs --strict    → SOURCES_CHECK: CLEAN (same counts)                                                exit 0
node scripts/sources-check.mjs --selftest  → SOURCES_SELFTEST: 42/42 pass, VERDICT: PASS
bash fleet-census/scripts/sources-census.sh validate <lane>  → kumitate-shokunin ok <path>/corpus/SOURCES.md                    exit 0
node scripts/proxy-check.mjs --src <origin 964f443>          → PROXY: MATCH (A=7 C=13 operability=8; … K=50/50 coverage:kimi-layer=10; pins=6 match) with PROXY warn PIN_UNPINNED scripts/sources-check.mjs
node scripts/proxy-check.mjs --strict --src <origin 964f443> → PROXY: DRIFT (PIN_UNPINNED term=scripts/sources-check.mjs)   exit 1  (only the disclosed advisory, promoted by --strict)
node scripts/proxy-check.mjs --selftest                      → PROXY_SELFTEST: 104/104 pass, VERDICT: PASS
```

Saturation pointer (earlier Low finding): `grep -n '^## Saturation' SCORECARD.md` → `1620`; `Declared round 34` → `1624`. The pointer now resolves; repaired.

### Did the knowledge admit/reject disposition change?

- **Knowledge admits** (`omp-task-contract.md`, `kimi-mcp-plane.md`): **no change**. Header trios are present and non-empty, the realgate counts entries_with_source=2 with no finding, and the content verdicts from the first spot-check stand.
- **Rejects** S019 and S020: **no change**. Both rows still carry `REJECTED:` and `flip:` in the real registry, and the gate now enforces both.
- **`sources-registry` capability**: changed from reject to **admit-conditional**. The three named false-cleans (items 1–3, column-0 case) are repaired. Two residuals remain: indented registry rows (Medium, shared with the fleet census parity) and `reflip:` substring (Low). Recommended: either a one-line parser fix (accept `^\s{0,3}\|` in both the row and the outside-Registry checks, plus a fixture), or record both residuals explicitly in `.ufo/rounds/round-34/sources-gate.md` before admitting the capability. Without one of those, the claim "the gate enforces registry integrity" overstates what it does.

### Ledger report and writes

Main's IRC asked for the post-review fixes to be reported in `fleet-ledger/.ufo/reports/round-34/kumitate.md`. I did not write to that file: my scope is read-only and this IRC also says no repository writes. The lane had already written `## Post-review fixes` there (line 99 onward), and that file is currently untracked in the fleet-ledger worktree (`?? .ufo/reports/round-34/kumitate.md`). It needs the integrator to commit it. Its command list matches what I re-ran; its selftest and census outputs agree with mine.

### Limits

- The recheck covers the named items and the frozen identity only. It is not a full round re-review and does not re-run the lane's mutation-tester.
- The live origin proxy drift is external and unchanged; default (non-`--src`) proxy output remains DRIFT on script-layer terms, as before.
- Fixtures m1–m10 ran in throwaway copies of the head tree; the lane tree was not modified.


---

## 2026-10-19 — residual targeted recheck at `0acb775` (appended; prior sections unchanged)

Reviewer: W3ReviewKumitate, non-author. Target: lane HEAD `0acb7752d19058b953ebbeba253b1e35f6548de5` (`round-34: fix SOURCES Markdown row parsing`), on top of `6336d71`. Lane `git status --porcelain` → 0 before and after. Scratch: `/tmp/kaika-verify/residual-recheck-3215035` (unique to this pass; from `git archive 0acb775` and origin `964f443`). Scope held to m4, m5b, m7 (plus a 4-space control), the realgate, and the v1 identity. No broad suite, no new edge hunt, no repository writes.

### Residual results

| Fixture | Edit applied | Lane gate `sources-check.mjs` (default and `--strict`) | Fleet census at `fleet-census` HEAD `ae7bf19` | Fleet census at `fleet-ledger` `ff701da` |
|---|---|---|---|---|
| m4 | `  | S022 …` (2-space row) appended outside `## Registry` | **DRIFT `ROW_OUTSIDE_REGISTRY`** `corpus/SOURCES.md:120`, exit 1 (both modes): **repaired** | `ok`, exit 0: **blind** | `E12 S022 row outside Registry section`, exit 1: **repaired** |
| m5b | `  | S023 |  | docs | Z | …` (2-space, empty source, tier Z) inserted inside Registry after S020 | **DRIFT `ROW_FIELD_EMPTY` (field=source)` and `TIER_ENUM` (tier=Z)` at `:34`**, exit 1 (both modes): **repaired** | `ok`, exit 0: **blind** | `E06 S023 tier=Z`, exit 1: **repaired** |
| m7 | `; flip:` changed to `; reflip:` on S019 teaches | **DRIFT `REJECTED_NO_FLIP`** `corpus/SOURCES.md:32`, exit 1 (both modes): **repaired** | `ok`, exit 0: expected (the fleet census has no flip rule) | `ok`, exit 0: expected |
| m4ctl (control) | `    | S024 …` (4-space row, code-block form) outside Registry | CLEAN, exit 0: **4-space exclusion holds** | `ok`, exit 0 | `ok`, exit 0 |

Commands (scratch paths abbreviated): `node scripts/sources-check.mjs --today 2026-10-19 [--strict]` in each fixture; `bash <census> validate <fixture>` with the census at each revision. Fixture application verified with `grep -c`: S023 → 1, reflip → 1, S022 → 1, S024 → 1.

### Real gate at `0acb775` (lane worktree)

```text
node scripts/sources-check.mjs               → SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)   exit 0
node scripts/sources-check.mjs --strict      → same CLEAN line                                                                                                  exit 0
node scripts/sources-check.mjs --selftest    → SOURCES_SELFTEST: 46/46 pass, VERDICT: PASS
fleet-census/scripts/sources-census.sh validate <lane>  → kumitate-shokunin ok <path>/corpus/SOURCES.md   exit 0
fleet-ledger ff701da census validate <lane>             → kumitate-shokunin ok <path>/corpus/SOURCES.md   exit 0
node scripts/proxy-check.mjs --src <origin 964f443>     → PROXY warn PIN_UNPINNED scripts/sources-check.mjs; PROXY: MATCH (A=7 C=13 operability=8; C1=19/19 C2=77/77 coverage=10; S=91/91 coverage:script-layer=10; R=83/92 coverage:runtime-layer=9; K=50/50 coverage:kimi-layer=10; pins=6 match)   exit 0
node scripts/proxy-check.mjs --strict --src <origin 964f443> → PROXY: DRIFT (PIN_UNPINNED term=scripts/sources-check.mjs)   exit 1 (disclosed advisory only)
node scripts/proxy-check.mjs --selftest      → PROXY_SELFTEST: 104/104 pass, VERDICT: PASS
```

v1 identity: stanza key names at `16a5441` (base) and `0acb775` (head) are identical, 23 keys (`diff` of sorted `^key=` lists, empty). `git diff --stat 6336d71..HEAD` touches only `.ufo/rounds/round-34/sources-gate.md`, `LOG.md`, and `scripts/sources-check.mjs`; the residual changed no `SCORECARD.md` or proxy-check line.

Direct-only limit (confirmed, not fixed): `corpus/knowledge/sub/x.md` (headerless) → `CLEAN`, `--strict` exit 0. The gate scans direct `corpus/knowledge/*.md` children only. The disclosure is present in `.ufo/rounds/round-34/sources-gate.md` (~lines 130–133).

### Fleet census (shared; parent attention)

The fleet census fix `ff701da` ("parse supported Markdown indentation in every mode") is an ancestor of `fleet-ledger` HEAD `b38d358`, and only there. `fleet-census` HEAD `ae7bf19` (branch `kaika/census`) does not contain it and still reports `ok` on m4 and m5b. The lane's contract-named command path (`fleet-census/scripts/sources-census.sh`) therefore remains blind to indented rows until that path picks up `ff701da`. `fleet-ledger` also has 5 uncommitted working-tree changes; I did not touch them. I did not run the parent CLI "93/0" verification; it was outside this scope.

### Capability recommendation

**Admit `sources-registry`, with the direct-only limit stated on the capability row.**

- Repaired and re-proven at `0acb775`: m4, m5b, m7 each exit 1 under the lane gate in default and strict modes; the 4-space control stays clean.
- Realgate clean; selftest 46/46; v1 unchanged at 23 keys.
- Limits to carry on the row: (a) knowledge header checks are direct-only (nested headerless files pass; m6); (b) the fleet census is a separate gate and only catches indented-row problems at `ff701da`, not at `fleet-census` HEAD `ae7bf19`; (c) the census has no flip rule, so `flip:` enforcement rests solely on the lane gate.
- Knowledge admit/reject disposition is unchanged from the prior section: admits `omp-task-contract.md` and `kimi-mcp-plane.md` stand; rejects S019 and S020 stand.

Scratch `/tmp/kaika-verify/residual-recheck-3215035` is retained for the parent to inspect; I'll remove it when the parent closes.
