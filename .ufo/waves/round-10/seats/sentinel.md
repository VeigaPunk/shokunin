# Sentinel ruling — round 10 corpus review

## Write-set ruling

| Path / operation | ruling | deciding clause |
|---|---|---|
| `shokunin:.ufo/waves/round-10/**` named closure artifacts, including this seat | allowed | `shokunin:PROTOCOL.md:189-193` assigns the integrator closure-gate artifacts under `.ufo/waves/round-<N>/`; the seat contract additionally limits this seat to its own file (`shokunin:.ufo/waves/round-10/CONTEXT.md:60-69`). |
| `shokunin:SCORECARD.md` aggregator §Round 10 append | **forbidden for this seat; allowed only to L1 integrator** | `shokunin:.ufo/waves/round-10/CONTEXT.md:62-66` explicitly forbids this seat; the axis score must carry command and measured commit (`shokunin:PROTOCOL.md:483-487`). |
| `shokunin:LOG.md` round-10 append | **forbidden for this seat; allowed only to L1 integrator** | same hard seat-scope prohibition (`shokunin:.ufo/waves/round-10/CONTEXT.md:62-66`); append-only correction discipline is `shokunin:PROTOCOL.md:109-110`. |
| `shokunin:.ufo/reports/AGGREGATE.md` §15 append | **forbidden for this seat; allowed only to L1** | aggregator ledger is canonical at this path (`shokunin:PROTOCOL.md:308-314`), but this seat's hard scope forbids `.ufo/reports/**` (`shokunin:.ufo/waves/round-10/CONTEXT.md:64-65`). |
| `shokunin:.ufo/reports/round-10/aggregator.md` | forbidden for this seat; aggregator-owned report | report path/ownership follows `shokunin:PROTOCOL.md:128-129`; seat scope forbids reports (`shokunin:.ufo/waves/round-10/CONTEXT.md:64-65`). |
| `shokunin:.ufo/l0-questions.md` append | forbidden for this seat; L1 durability owner | append format is `shokunin:MISSION.md:58-62`; durability owner is the integrator (`shokunin:PROTOCOL.md:498-500`). |
| `shokunin:.ufo/prompts/aggregator-round-10.md` | forbidden for this seat; generated prompt may be committed by L1 | prompt durability is required at `shokunin:PROTOCOL.md:189-193`; prompt edits are forbidden by the seat scope (`shokunin:.ufo/waves/round-10/CONTEXT.md:64-65`). |
| six child `corpus/lessons/round-10-aggregator-corpus-verdict.md` files | forbidden for this seat | aggregator owns child files and must commit each at creation, pathspec-limited (`shokunin:PROTOCOL.md:308-311`); this seat says never mutate child repos (`shokunin:.ufo/waves/round-10/CONTEXT.md:66-68`). |
| `shokunin:PROTOCOL.md`, `MISSION.md`, `AXES.md`, `CORPUS.md`, `MANIFEST.json`, `scripts/`, `.ufo/state/**`, prior/future wave dirs | forbidden | explicit hard exclusion (`shokunin:.ufo/waves/round-10/CONTEXT.md:63-68`). |

Appending shared `SCORECARD.md`, `LOG.md`, and `AGGREGATE.md` while the protocol lane is live is **not safe**: concurrent appenders can interleave or produce stale evidence and attribution collisions. The named collision hazard is ledger row **D-77**, which records shared-main-repo writers (`shokunin:CORPUS.md:133-135`); the broader append collision precedent is documented at `shokunin:.ufo/reports/AGGREGATE.md:162-168`. Mitigation: L1 serializes one integration commit after both lanes have stopped writing, re-reads each file, appends only, and commits only its exact paths. The commit MUST use pathspec limitation and explicit identity: `git -c user.name=aggregator-shokunin -c user.email=aggregator@shokunin.local commit -- <exact paths>`; protocol requires lane identity for main-repo commits and forbids `commit -a`/`add -A` (`shokunin:PROTOCOL.md:465-474`).

## Part A — registry ruling

Creating `shokunin:SKILL.md` is **forbidden in this seat** (and not authorized by the listed write set). More importantly, it would not satisfy the gate standard: the standard says rows live in each lane's `SKILL.md` (`shokunin:PROTOCOL.md:382-385`), while this main repo has no `SKILL.md` (the requested `ls shokunin:SKILL.md` absence check is therefore `could-not-evaluate` here because the MCP alias is unavailable; local root listing has no such file). A registry row at `shokunin:.ufo/waves/round-10/gate-registry.md` plus a routed clause amendment is **non-conformant-on-registry** under the current standard: it is evidence/queue material, not the prescribed lane-owned registry home.

Exact operator-side amendment text required in `shokunin:PROTOCOL.md` §Gate standard (replace the Registry paragraph, preserving the schema):

> **Registry.** The schema is this section's. Rows live in each lane's `SKILL.md`; **for a meta-domain lane without a repository `SKILL.md`, rows live in the lane's committed main-repo registry file `.ufo/waves/round-<N>/gate-registry.md` (one current file per round), and that file is the lane's registry home for this section.** Each row records name, `gate|probe`, entry command, verdict map (code → class), self-test command and spelling, pinned-value path, write scope, and owner. The aggregator ledger stays the routed-defect queue, not a second inventory; a fleet index is pointers to lane rows, never copied expected values.

Until that amendment is landed and re-read, Part A grade is **non-conformant-on-registry**, not conformant.

## Credential sweep

Sweep command (read-only; no values printed):
`grep -RInE 'op://|ghp_|github_pat_|xox[baprs]-|AKIA|BEGIN .*PRIVATE KEY|Bearer |[0-9A-Fa-f]{40,}|[A-Za-z0-9+/]{40,}={0,2}' .ufo/waves/round-9 .ufo/waves/round-10 <six child repo lesson paths>`.
The sweep covered every file under `shokunin:.ufo/waves/round-9/**`, every currently present file under `shokunin:.ufo/waves/round-10/**`, and each named child round-9 mirror. Counts from the companion count command over that exact tree/revision state: `op://` 131; `ghp_` 10; `github_pat_` 9; `xox[baprs]-` 0; `AKIA` 9; `BEGIN .*PRIVATE KEY` 5; `Bearer ` 6. Long hex/base64 matches were **could-not-evaluate** as credential material because the same sweep necessarily matches commit hashes, checksums, and fixture text; no value is reproduced.

All reported hits are `file:line`-locatable by the command above. Classification: occurrences in detector regexes, quoted commands, protocol prose, and synthetic self-test fixtures are **schematic**; no real-secret value was printed or established. The sweep found no demonstrated `real-secret`; any hit whose surrounding context is not inspected individually remains **could-not-evaluate**, not a clean bill. For safety, this ruling reports only the first four bytes conceptually (for example `op:/`, `ghp_`, `AKIA`, `Bear`) and lengths are intentionally withheld where the match is embedded in source text; no live `op://` item path is reproduced. The prior mirrored lessons themselves contain schematic `op://` and pattern text (for example `kasegi-shokunin:corpus/lessons/round-9-aggregator-corpus-verdict.md:18`), not demonstrated credentials.

## Push-scope compliance

Remote check command:
`git -C <repo> remote -v`; all six child repos report only their own `VeigaPunk/<repo>` origin. Containment command:
`git -C <repo> branch -r --contains <sha>`.
Observed against the round-9 pinned mirror commits: `kasegi-shokunin` `b7180b0` → `origin/master`; `kengaku-shokunin` `f09ff1f` → `origin/master`; `kake-shokunin` `a209441` → `origin/master`; `kumitate-shokunin` `7a099b2` → `origin/master`; `kotoba-shokunin` `63ceba7` → **no output**; `kagi-shokunin` `4b8c018` and `4391b3b` → `origin/master`. The hashes are the revisions named by `shokunin:.ufo/waves/round-10/CONTEXT.md:19-25`; remote state was measured at command time.

No plan here pushes a child repo. Leaving child commits unpushed is durable and correct when the child commit is already contained in its own `origin/*`; it is a defect for `kotoba-shokunin` because `63ceba7` is not contained in any fetched `origin/*`. That is push-scope durability debt, not permission to push from this lane: L1/operator must resolve it under `shokunin:MISSION.md:49-56` and the operator-gated conflict rule (`shokunin:PROTOCOL.md:490-493`).

## Refusals

- I refuse to create `shokunin:SKILL.md`, edit the gate standard, or treat `gate-registry.md` as conformant before the amendment lands.
- I refuse all shared-ledger writes while the protocol lane is live; L1 must serialize and pathspec-limit the integration commit.
- I refuse child-repo edits, commits, and pushes. The uncontained Kotoba mirror is reported as a defect for L1/operator resolution, not acted on here.
- I refuse to print credential values or live vault paths; all classifications above are schematic or could-not-evaluate unless independently proven otherwise.
