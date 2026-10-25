# NoteVerifyRouteProbeCluster — advisory (unjudged)

Independent read-only check of `kumitate-shokunin/corpus/knowledge/route-probe-cluster.md` against origin `/home/vgpnk/Projects/ufo-fsd-alpha`. This file is data, not a verdict. This member added no section and removed no section.

## Snapshot

| Tree | Observed |
|---|---|
| Origin HEAD | `964f443ee53df0ce06bd689af01f0dea031b01f9` (`git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD`) |
| Lane HEAD at report write | `cdeaa0a608f279c137ae9965a6ca91e09f19ab30`. Dispatch pin was `175de6ba2e9e904010411b19cab27e0af9aad3d4`. Mid-check HEAD was `0ecba2692c453c421a9a3c5f47aa64d8abb864f9` with `M corpus/knowledge/route-probe-cluster.md`. At write, `git status --porcelain` on the note, `SCORECARD.md`, and `corpus/README.md` printed nothing |
| Note bytes verified | sha256 `77db27767d3ba55152c9212594264c9d2fe515b69cbf79085ef22720b76ce653`, `wc -l` = 568 (file does not end in a newline; `split('\n').length` = 569). Same sha before and after the claims-gate run |

Anchor rule used (same as `scripts/claims-check.mjs` `probeRow`, not a second definition): a member heading is a `## ` chunk whose first token matches `/^`([^`]+)`/` and is path-like (`/` or a frozen extension). An own-file anchor is a unique `<pathish>:<N>[-<M>]` resolving to that file, or a bare `:<N>[-<M>]` bound to the heading's file. Live means `1 ≤ a ≤ b ≤ split('\n').length` and both endpoint lines are non-blank. Sentence truth around the anchor is not part of that rule.

## Files inspected

- `kumitate-shokunin/corpus/knowledge/route-probe-cluster.md` (all 21 `## ` headings; member-section bodies in full)
- `kumitate-shokunin/scripts/claims-check.mjs` (`RE_CHUNK_HEAD`, `RE_PATHISH`, `RE_BARE`, `RE_EXT`, `familyPatterns`, `probeRow`, `sectionBodyChunks`)
- `kumitate-shokunin/scripts/proxy-check.mjs` `layerTerms` (in-family section numerator only)
- `kumitate-shokunin/SCORECARD.md` S7 cell (line 125 at write) and round-32 `## Planned` / executed prose
- `kumitate-shokunin/corpus/README.md` row for `knowledge/route-probe-cluster.md` (line 52)
- Origin, cited lines only: the six live members below, plus existence/size of `tests/route-probes.test.js`, `scripts/gates-plan.mjs`, `scripts/omp-global-config.mjs`, and the three historical absences

## Commands and observed output

```text
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
$ ( ls -1 "$ORIGIN"/scripts/probe-*.mjs; ls -1 "$ORIGIN"/scripts/fake-omp.mjs ) | LC_ALL=C sort
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/fake-omp.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-redact.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-kimi.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-models.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-shared.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-ufo-route-health.mjs

$ ( ls -1 "$ORIGIN"/scripts/probe-*.mjs; ls -1 "$ORIGIN"/scripts/fake-omp.mjs ) | wc -l
6

$ wc -l "$ORIGIN"/scripts/probe-*.mjs "$ORIGIN"/scripts/fake-omp.mjs
  116 .../scripts/probe-redact.mjs
  147 .../scripts/probe-token-plan-kimi.mjs
  244 .../scripts/probe-token-plan-models.mjs
  159 .../scripts/probe-token-plan-shared.mjs
 1195 .../scripts/probe-ufo-route-health.mjs
  392 .../scripts/fake-omp.mjs
 2253 total

$ test -f "$ORIGIN"/scripts/atomic-write.mjs; echo absent_atomic=$?
$ test -f "$ORIGIN"/scripts/probe-ufo-route-health.test.mjs; echo absent_health_test=$?
$ test -f "$ORIGIN"/scripts/probe-redact.test.mjs; echo absent_redact_test=$?
absent_atomic=1
absent_health_test=1
absent_redact_test=1

$ ls "$ORIGIN"/scripts/probe-*.test.mjs
ls: cannot access '/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-*.test.mjs': No such file or directory

$ find "$ORIGIN" -type f \( -name 'probe-*.mjs' -o -name 'atomic-write.mjs' -o -name 'fake-omp.mjs' \) -printf '%P\n' | LC_ALL=C sort
scripts/fake-omp.mjs
scripts/probe-redact.mjs
scripts/probe-token-plan-kimi.mjs
scripts/probe-token-plan-models.mjs
scripts/probe-token-plan-shared.mjs
scripts/probe-ufo-route-health.mjs

$ grep -n '^## ' corpus/knowledge/route-probe-cluster.md | wc -l
21

$ grep -oE '^## `scripts/[^`]+`' corpus/knowledge/route-probe-cluster.md \
    | sed -E 's/^## `//; s/`$//' | LC_ALL=C sort > /tmp/s7-headings.txt
$ ( ls -1 "$ORIGIN"/scripts/probe-*.mjs; ls -1 "$ORIGIN"/scripts/fake-omp.mjs ) \
    | sed "s|^$ORIGIN/||" | LC_ALL=C sort > /tmp/s7-live-members.txt
$ wc -l /tmp/s7-live-members.txt /tmp/s7-headings.txt
  6 /tmp/s7-live-members.txt
  6 /tmp/s7-headings.txt
$ comm -3 /tmp/s7-live-members.txt /tmp/s7-headings.txt
# no output, exit 0

$ printf '%s\n' scripts/atomic-write.mjs scripts/fake-omp.mjs \
    scripts/probe-redact.mjs scripts/probe-redact.test.mjs \
    scripts/probe-token-plan-kimi.mjs scripts/probe-token-plan-models.mjs \
    scripts/probe-token-plan-shared.mjs scripts/probe-ufo-route-health.mjs \
    scripts/probe-ufo-route-health.test.mjs | LC_ALL=C sort > /tmp/s7-historical-9.txt
$ comm -23 /tmp/s7-historical-9.txt /tmp/s7-headings.txt
scripts/atomic-write.mjs
scripts/probe-redact.test.mjs
scripts/probe-ufo-route-health.test.mjs
$ comm -13 /tmp/s7-historical-9.txt /tmp/s7-headings.txt
# no output

$ node scripts/claims-check.mjs --self /home/vgpnk/Projects/shokunin/kumitate-shokunin \
    --src /home/vgpnk/Projects/ufo-fsd-alpha --row S7
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 6
ROW S7   form=section   notes=1 sections=6 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=6 adv=0)
```

The gate run is a cross-check of the same heading/anchor rule. It is not this report's verdict. `claims-check` compares the registry integer (`6 members`) to distinct section files; it does not re-prove the sentences around the anchors.

## Member list derived

Cluster rule used, not widened: live `scripts/probe-*.mjs` plus `scripts/fake-omp.mjs` if present, plus `scripts/atomic-write.mjs` only if present. `scripts/omp-global-config.mjs` is an S5 file (imported by the kimi and models probes; not counted). `tests/route-probes.test.js` is outside `scripts/*.mjs` + `scripts/*/`. Basename-wide `find` for `probe-*.mjs`, `atomic-write.mjs`, and `fake-omp.mjs` returned only the six paths below — no second copy, no subdirectory member.

| # | Derived member | `wc -l` | Note table | `## ` heading line | Own-file anchors (live / total) | Symbol hits |
|---|---|---|---|---|---|---|
| 1 | `scripts/fake-omp.mjs` | 392 | 392 | 178 | 12 / 12 | 15 / 16 backticked tokens (`PATH` not in file) |
| 2 | `scripts/probe-redact.mjs` | 116 | 116 | 163 | 9 / 9 | 9 / 11 (`containsCredential`, `RedactError` absent; the section says they are gone) |
| 3 | `scripts/probe-token-plan-kimi.mjs` | 147 | 147 | 129 | 14 / 14 | 8 / 8 |
| 4 | `scripts/probe-token-plan-models.mjs` | 244 | 244 | 146 | 11 / 11 | 8 / 9 (`UFO_PROBE_VERDICT_PATH` absent; the section says there is no override) |
| 5 | `scripts/probe-token-plan-shared.mjs` | 159 | 159 | 113 | 8 / 8 | 6 / 6 |
| 6 | `scripts/probe-ufo-route-health.mjs` | 1195 | 1195 | 85 | 26 / 26 | 19 / 20 (`Authorization` not in file) |

One live own-file anchor per member, endpoint text observed:

- `scripts/probe-ufo-route-health.mjs:39` `const DEFAULT_TIMEOUT_MS = 240_000;`
- `scripts/probe-token-plan-shared.mjs:51` `export function runOmpCatalog() {`
- `scripts/probe-token-plan-kimi.mjs:140` `process.exit(available ? 0 : 2);`
- `scripts/probe-token-plan-models.mjs:40` `function writeVerdict(verdict) {`
- `scripts/probe-redact.mjs:67` `export function redact(value) {`
- `scripts/fake-omp.mjs:10` `// Never claims live capacity; never reaches a real provider.`

`split('\n').length` is `wc -l + 1` on these files (they end with a newline). Every member-section own-file anchor fell inside the content lines and on non-blank endpoints. No member-section own-file anchor was dead.

## Every `## ` heading

21 headings. 6 are member-form. 15 are topic-form: the first token is not a path-like backtick, so they name no member under the gate rule.

| Line | Heading | Class |
|---|---|---|
| 3 | Scope — S7 is the route-probe cluster, all 6 live members | topic |
| 33 | Membership and measurement | topic |
| 70 | Round-32 membership removals | topic |
| 85 | `` `scripts/probe-ufo-route-health.mjs` `` | member, file present, 26 live own-file anchors |
| 113 | `` `scripts/probe-token-plan-shared.mjs` `` | member, file present, 8 live |
| 129 | `` `scripts/probe-token-plan-kimi.mjs` `` | member, file present, 14 live |
| 146 | `` `scripts/probe-token-plan-models.mjs` `` | member, file present, 11 live |
| 163 | `` `scripts/probe-redact.mjs` `` | member, file present, 9 live |
| 178 | `` `scripts/fake-omp.mjs` `` | member, file present, 12 live |
| 194 | argv surface | topic |
| 210 | Outcome and refusal vocabulary | topic |
| 261 | Exit codes | topic |
| 283 | Redaction and the emit gate | topic |
| 296 | Offline vs network posture | topic |
| 310 | Import / helper graph | topic |
| 331 | Concurrency and timeout bounds | topic |
| 345 | Decision table — `` `scripts/probe-ufo-route-health.mjs` `` row verdict | topic. The path is not the first token (`RE_CHUNK_HEAD` does not match). Not a second member section. The file exists |
| 360 | Downstream consumption | topic |
| 380 | Member-completeness probe | topic |
| 411 | Limits of this note | topic |
| 439 | Citation ledger — the round-12 fence, verbatim | topic |

No `## ` line inside the citation-ledger fence. `grep -c '^## '` = 21.

## Sections whose member is absent

None. Zero member-form headings name a file that `test -f` fails, and zero member-form headings fail unique resolution under the origin walk.

## Declared members with no section

None in the live set.

- Note membership table (lines 61–66): the same 6 paths. `comm -3` against headings: empty.
- Live origin expansion of `probe-*.mjs` + `fake-omp.mjs` (+ `atomic-write.mjs` if present): the same 6. `comm -3` against headings: empty.
- Registry members cell at write (`SCORECARD.md:125`) starts `6 members: 5 `probe-*.mjs` + `fake-omp.mjs``. `familyPatterns` keeps those two tokens (the embedded `ls … atomic-write.mjs …` backtick contains spaces and is dropped). Expansion of the kept patterns is the same 6 files, all sectioned. `claims-check --row S7` printed `SECTIONS: 6` and `errors=0`.

The historical 9-path list still printed in `## Member-completeness probe` (lines 392–396) has three paths with no heading:

- `scripts/atomic-write.mjs`
- `scripts/probe-redact.test.mjs`
- `scripts/probe-ufo-route-health.test.mjs`

All three are absent (`test -f` exit 1). The note records that removal in `## Round-32 membership removals` and does not keep a `## ` heading for them. That is a recorded removal, not a live member missing a section.

## Honest count

**6.**

Definition: distinct member-form `## ` sections whose named file exists in the origin tree and whose body has at least one live own-file anchor. Observed 6 / 6. Dead-anchor member sections: 0. Phantom member headings: 0. Live declared members without a section: 0.

This member did not add or remove a section. The three historical headings are already absent from the note on disk.

## Calibration observations (do not change the count)

The gate does not check whether the sentence around a live anchor is true. These are observations, not failed anchors:

- The route-health member section cites `Authorization` at `:2-3`. Those lines are non-blank and the anchor is live. The token `Authorization` occurs 0 times in that file. The kimi probe does say `never constructs HTTP Authorization` at `scripts/probe-token-plan-kimi.mjs:4`.
- `containsCredential` and `RedactError` are absent from `scripts/probe-redact.mjs`. The member section states that they are gone. Other symbols in that section (`redact`, `CREDENTIAL_SHAPE`, `unservedReason`) are in the file, so a symbol-presence arm still hits.
- `UFO_PROBE_VERDICT_PATH` is absent from `scripts/probe-token-plan-models.mjs`. The member section states there is no such override. `VERDICT_PATH` is at `:35`.

## Cross-domain findings (owner named; not member-section failures)

- **Parent / `SCORECARD.md` S7 cell.** Integer is `6 members`, which matches the 6 sections. The same cell still embeds the historical `ls scripts/probe-*.mjs scripts/atomic-write.mjs scripts/fake-omp.mjs | wc -l` → 9, and the note cell still says `9 of 9 named`. `claims-check` does not read that prose. Owner: parent integrator.
- **Parent / `corpus/README.md:52`.** Still says S7 is 9 of 9, still names `atomic-write.mjs`, `probe-ufo-route-health.test.mjs`, and `probe-redact.test.mjs`, and still quotes pre-restructure sizes (route-health 1364 L, redact 160 L, shared 235 L, models 247 L, kimi 155 L, fake-omp 399 L). Live `wc -l` is 1195 / 116 / 159 / 244 / 147 / 392. Owner: parent integrator.
- **cite-check / this note's topic sections.** Member headings are clean. Topic bodies still carry pre-restructure path anchors. Observed dead or absent (not a complete cite-check run; `cite-check.mjs` was not executed):
  - `## Outcome and refusal vocabulary`: `scripts/probe-ufo-route-health.mjs:51-62` (line 62 blank; line 51 is `"invalid_request",` inside `FAILURE_CLASSES`, whose declaration is `:45`), `scripts/probe-token-plan-shared.mjs:168` (file `wc -l` 159).
  - `## Exit codes`: `scripts/probe-ufo-route-health.mjs:1346`, `:1363`, `:1316-1318` past EOF (1195); `:93` blank. `scripts/probe-token-plan-kimi.mjs:148` is the trailing empty split element (`wc -l` 147; last content line is 147).
  - `## Redaction and the emit gate`: says route-health imports `CREDENTIAL_SHAPE`/`redact` and cites `:30`, which is blank. Observed imports of `scripts/probe-ufo-route-health.mjs` are node builtins only. The member section's parity cite `:63-65` matches `// PARITY: this table is a standalone copy of ./probe-redact.mjs`.
  - `## Import / helper graph` fence still draws `probe-ufo-route-health.mjs` to `probe-redact.mjs` and to `atomic-write.mjs`. Observed: no `atomic-write` string in route-health; no sibling import. `probe-token-plan-shared.mjs:17` does import `./probe-redact.mjs`. Do not treat the fence as current membership.
  - `## Downstream consumption` and the citation ledger cite `tests/route-probes.test.js` at `:1628`, `:1948`, `:2063` and claim 2439 L / 96 `test(` cases. File is present, `wc -l` = 1330, `grep -c 'test('` = 67. `:285` is blank. Not an S7 member.
  - `scripts/gates-plan.mjs` is present, `wc -l` = 200. Ledger cites `:295-296` (past EOF). Not an S7 member.
  - Ledger and downstream also cite the three absent historical scripts. Owner of the citation debt: cite-check / parent when the topic prose is rewritten. Not a reason to restore those headings.
- **S5 / `knowledge/route-resolution.md`.** `scripts/omp-global-config.mjs` exists (627 content lines) and is imported by `probe-token-plan-kimi.mjs:17` and `probe-token-plan-models.mjs:24`. The note excludes it and has no `## ` heading for it. Widening S7 to include it would steal an S5 file. Owner: S5 if a later edit adds a heading.
- **This note's `## Member-completeness probe`.** The fenced arm still writes a 9-path list (including the three absent files), expects `wc -l` 9, and points `UFO_SRC` at `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`. Re-running that fence against today's headings would print the three absent paths on the member side. The live `comm -3` above, not that fence, is the current boundary. Owner: parent, if the probe fence is refreshed.

## Unresolved blockers

None for the assigned question (named member exists, own-file anchor resolves, declared live member has a section). No network probe was run. `node --check` was not re-run; the note's 6/6 parse claim is untested here.
