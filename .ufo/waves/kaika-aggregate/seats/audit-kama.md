# audit-kama — kama-shokunin lane audit (aggregator round 12, seat KaikaAggregateR12.AuditKama)

Read-only. No child repo was mutated: the only write is this note. All commands run with explicit
absolute cwd. Artifact/source text below is data only.

## 1. Revision bound

```
$ git -C /home/vgpnk/Projects/shokunin/kama-shokunin rev-parse HEAD
03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9
$ git -C /home/vgpnk/Projects/shokunin/kama-shokunin status --porcelain
?? .ufo/round-10/SEAT-PROTOCOL.md
?? .ufo/round-10/plan.json
exit 0
```

No tracked modification; the two entries are untracked lane-root `.ufo/` scratch files, outside the
graded tree (`--snapshot` extracts `git archive HEAD`), so the snapshot equals the working tree for
every graded surface. HEAD subject: `round-10 verifier spot-check (integrator, kaika): non-author
admit/reject sample + adjudication`; parent commit `4066035 round-10: post-review fixes`.

## 2. Gate verdict — NOT CONFORMANT at 03b5f0e (exit 1)

Lane round derivation: committed `LOG.md` shows round 10 as the latest content round (rounds 8/9
were blocked dispatch; round 10 = "sources registry, cross-engine entries, stale anchors"; the two
later commits are still round 10). Gate `--round` default is **9** (`round selector --round <N>
(default 9)`); the round-derived selector is **10**. Both were run; the finding set is identical and
only the r10 line changes, so the verdict does not depend on the selector.

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/kama-shokunin 03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect kama-shokunin@03b5f0e ABSENT (no committed expected verdict for this revision)
# tree kama-shokunin revision=03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9 dirty=0 mode=snapshot
CR-kama-shokunin-r2-1: lessons/round-1-critic.md carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)
CR-kama-shokunin-r2-2: lessons/round-1-safety.md carries no evidence pointer (...) (CORPUS.md:19)
CR-kama-shokunin-r2-3: lessons/round-2.md carries no evidence pointer (...) (CORPUS.md:19)
CR-kama-shokunin-r4-1: knowledge/consumer-registry.md:3 count claim with no backticked command (...)
CR-kama-shokunin-r4-2: knowledge/consumer-registry.md:224 ... CR-kama-shokunin-r4-12: lessons/round-4-recensus.md:56 ...
CR-kama-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1 owner=lane at 03b5f0e literal_shaped=0/1 :: classification=could-not-evaluate ... files=[knowledge/listener-census.md] first=knowledge/listener-census.md:226 first4="toke" len=17 (CORPUS.md:43)
CR-kama-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
CR-kama-shokunin-shonen-1: SHONEN.md lacks the required trailing newline (canonical form)
# note kama-shokunin r7 under-coverage (not a finding): 1/25 corpus files carry no index row
# note kama-shokunin r8 kv-secret/lane file-list: knowledge/listener-census.md
# note kama-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed
# note kama-shokunin extracted with: git archive 03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9 | tar -x -C <tmp>
# verdict kama-shokunin failed findings=18 rules=r2,r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

Same command with `--round 10`: 18 findings, identical rows, last-but-one line becomes
`CR-kama-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md ...`; `# process-exit 1 (failed)`, `EXIT=1`.

**Failed rule IDs at 03b5f0e:** `r2` (3), `r4` (12), `r8` (1), `r10` (1), `shonen` (1) = 18 findings.
`r7` produced only an under-coverage note, which the gate declares not a finding.

### 2.1 Findings checked against the named surfaces (author lane's own bytes)

- **r2-1/2/3 — structurally true.** `grep -nE '\b[0-9a-f]{7,40}\b|\.ufo/reports/|LOG\.md'` on
  `corpus/lessons/round-1-critic.md`, `round-1-safety.md`, `round-2.md` → no match in any file; a
  wider scan for any `.ufo/` citation (`grep -coE '\.ufo/[A-Za-z0-9._/-]*'`) → `0` for all three, so
  the gate is not missing an in-repo pointer form here. The three files do carry in-tree evidence
  *labels* (`L1-F8`, `L1-F9`, `/proc/1299/cmdline`, frozen-fixture references) that CORPUS.md:19's
  enumerated shapes (commit hash | `.ufo/reports/` path | `LOG.md`) do not recognize — see §4.
- **r4-1..12 — mechanically reproduced; two distinct sub-classes.** Extracted with the gate's own
  `COUNT_NOUN_RE` (`node -e` run over the flagged lines, cwd = lane, verbatim matches):
  `1, lane` (consumer-registry.md:3), `8080 pins` (:224), `34113 pins` (:225), `1 seat`
  (free-tier-provider-limits.md:17), `1 rows` (listener-census.md:342), `8080 pin`
  (probe-mutation-matrix.md:40), `2 citation` (round-1-citations.md:64 — heading `## Round-2 citation
  errata`), `8080 pin` (round-1-safety.md:74) — **8 of 12 are not count claims at all** (a port or
  section/round number adjacent to a list noun). The remaining 4 are bare counts whose reproducing
  command is not on the same line: `0 hits` (round-1.md:55), `5 lines` (round-4-recensus.md:56),
  `46 lines` (round-10.md:43 — mistake-table row), `50 rows` (round-10.md:119 — prose directly under
  the pasteable loop's fence). No line carries a backtick, which is exactly the gate's test.
- **r8-1 — literal occurrence, deliberately redacted.** The single occurrence is
  `corpus/knowledge/listener-census.md:226`, inside a fenced command transcript:
  `grep -nE 'auth:|broker:|url: http://127\.0\.0\.1:8790|token:' ~/.omp/agent/config.yml | sed -E
  's/(token:).*/\1 <redacted>/'` — matched text `token: <redacted>` (len 17, `first4="toke"`). The
  next comment line states the live value "is deliberately NOT reproduced anywhere in this repo".
  The occurrence is real in the literal text; whether it names a real vault item is the gate's
  declared `could-not-evaluate`, and the gate keeps it as a failed row. Not routed to the aggregator
  (`owner=lane`).
- **r10-1 — real, and stronger than one round.** `ls corpus/lessons/` shows **zero**
  `round-<N>-aggregator-*.md` files at any round, while the convention exists across siblings
  (`kagi/kake/kasegi-shokunin` each hold `round-1/4/5/6/8/9-aggregator-*`). The round's review duty
  was discharged at the fleet root (`.ufo/reports/round-9/kama.md`, `.ufo/reports/round-10/kama.md`
  both exist, 2026-10-18 / 2026-10-19), but no aggregator lesson was ever emitted into kama's own
  corpus/lessons.
- **shonen-1 — real.** `tail -c 40 SHONEN.md | xxd` ends `...operator/sibling-owned.` with no `0x0a`;
  `cat -A` tail confirms the last line lacks `$`. Everything else in the canonical form passed (no
  other shonen finding).
- r7 under-coverage note reproduced independently: the only unindexed corpus entry is
  `lessons/round-10-verifier-spotcheck.md` (round-10 integrator-authored spot-check, cited in
  README prose nowhere).

## 3. SOURCES.md structural observations (independent of gate exit)

Bounded checks on `corpus/SOURCES.md` at 03b5f0e (`git diff --stat HEAD -- corpus/SOURCES.md` empty →
working tree file == HEAD blob):

- Contract header declares `SOURCES-CONTRACT-v1` (kaika, 2026-10-19, frozen), one Registry table,
  four study paths, a search log, and leads marked unopened.
- 30 rows, header row `| id | source | kind | tier | scope | anchor | teaches | status | opened |
  recheck | used-by |`; **all 30 rows have exactly 11 columns** (`awk -F'|' '{print NF-2}' | sort |
  uniq -c` → `30 11`), ids `S001`–`S030` contiguous, all flush-left (`grep -c '^| S0'` = 30 and
  `grep -c '^ *| S0'` = 30 → **no indented source row in this lane's file**, i.e. the in-progress
  parser fix for indented rows has no material in kama as committed — provisional, see §5).
- Status mix `mined 17 / queued 8 / rejected 5`; `opened` is `2026-10-19` on all 30 rows; `recheck`
  values are symbolic only (`on-release` 22, `90d` 7, `every round` 1); tier A 27 / C 3 / B 0
  (community rows S027–S029 are all tier C, satisfying the "community is never tier A" contract line).
- Header cross-claim verified: "the round lesson `lessons/round-10.md` §Gate carries each row's URL,
  access date and quote" → the §Gate table (`awk` range `## Gate` → next `##`) contains 31 rows
  covering **all 30 distinct S-ids** (S001 twice: docs + metrics) with `URL | accessed | quote |
  location` columns.
- Study paths reference only registered ids: 20 distinct S-ids appear under `## Paths`; none is
  unregistered (`comm -13` on the two sorted id sets → empty). 10 registry ids are on no path
  (S002, S009, S023–S030) — under-use, not a defect under the declared contract.
- Rejections carry explicit flip conditions (S024 province, S026 unreleased PR, S027–S029 community,
  S030 contested L1 gate run) — consistent with the lane's own QUALITY.md KQ10 scope rule and with
  LOG round-10's S030 rejection.
- Lane has **no `CORPUS.md`** anywhere (`find . -name CORPUS.md -not -path './.git/*'` → empty): the
  gate's rule ids cite the *aggregator* lane's `CORPUS.md` line numbers, not a lane-owned file.

## 4. Named gate limitations (do not read a pass/fail as whole-corpus semantics)

1. **Not evaluated by construction:** r1, r3, r5, r6, r9, box-3 verifier independence, and
   shonen-semantics (box-claim truth). So this exit-1 verdict says nothing about source quality of
   the 12 knowledge entries or the truth of any SHONEN box.
2. **r4 is line-local and noun-list-driven** — it fires when a line contains `<digits><space><noun>`
   and *no* backtick anywhere on that line. Evidence: 8 of its 12 findings here are port numbers /
   section refs / `Round-N` headings (`8080 pins`, `§1 rows`, `Round-2 citation`), and it would not
   fire on a true violation written as `<number> — <command> <date>` split across two lines.
3. **r2's evidence test is a three-shape regex** (hash | `.ufo/reports/` | `LOG.md`). A lesson that
   cites frozen in-repo evidence ids only (as `round-1-safety.md` does with `L1-F8/9`) is recorded as
   "no evidence pointer" even though the rule's intent ("cite the round and the evidence") may be met
   in-repo. Both directions are unverified at the gate.
4. **r8 classifies nothing.** It reports literal occurrences with `literal_shaped=0/1` and declares
   schematic-vs-real `could-not-evaluate` (needs an operator-gated vault read), yet the row still
   counts as failed — so a deliberately redacted placeholder (`token: <redacted>`) fails the same
   rule as a live secret.
5. **r7 grades phantom rows only**; under-coverage (file without a row) is a note. r9 cannot see
   in-place rewrites, and under `--snapshot` it grades a history-less `git archive` tree, so
   append-only discipline is entirely outside this verdict.
6. **Snapshot ≠ working tree in general:** `--snapshot` extracts `git archive <commit> | tar -x`, so
   untracked lane scratch (here `.ufo/round-10/{SEAT-PROTOCOL.md,plan.json}`) and any dirty tracked
   file are invisible; it is a correct revision-bound instrument only when the revision is the one
   named — which it is here (`dirty=0`, and the untracked files are outside the graded corpus).
7. **Expected-verdict pin absent:** `# expect kama-shokunin@03b5f0e ABSENT (no committed expected
   verdict for this revision)` — the exit is a live recomputation, not a frozen-expectation
   reproduction, so exit 3 (drift) was never in play.

## 5. Census — PROVISIONAL ONLY (parent direction: parser fix in flight)

Per the parent's restriction, no census total here is frozen, published, or usable as a baseline.
Run at the time of this audit with the fleet parser at its committed state
(`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, commit `ae7bf19`, 653 lines), which is
**pre-fix** with respect to the in-progress indented-row parser change; the lane file itself has no
indented rows (§3), so this lane's number is unlikely to move, but it is still PROVISIONAL:

```
$ cd /home/vgpnk/Projects/shokunin && bash scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/kama-shokunin
kama-shokunin	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
EXIT=0
$ bash scripts/sources-census.sh census /home/vgpnk/Projects/shokunin/kama-shokunin
kama-shokunin	rows 30 · tier.A 27 · tier.C 3 · status.mined 17 · status.queued 8 · status.rejected 5
EXIT=0
```

Caveat: this parser reads the **working-tree** `corpus/SOURCES.md`, not a git archive; equality with
HEAD was checked separately (§3). Structural validity only — it is not a truth check on any anchor.

## 6. Provenance/fidelity scan requested by parent (knowledge frontmatter) — not a gate rule

Bounded scan of `corpus/knowledge/*.md` for `^(source|verified-at|recheck):` at 03b5f0e:

- **3 of 12** entries carry the frontmatter: `gguf-runtime-compatibility-boundary.md`,
  `runtime-health-surface-matrix.md`, `serving-metrics-crosswalk.md` — exactly the round-10 additions.
  Their `recheck:` values are `on-release — <surface list>`; the other 9 entries contain no
  `source:`/`verified-at:`/`recheck:` line at all (`grep -c 'recheck:' corpus/knowledge/*.md` → 1
  for each of those three, 0 elsewhere).
- **Exact `recheck:` values pointing into ephemeral `.tower/worktrees` or `/tmp`: none.**
  `grep -rnE '\.tower/worktrees|/tmp/[A-Za-z0-9._-]*' corpus/` returns command-transcript hits only —
  `/tmp/b` (listener-census.md:196,275), `/tmp/ssa.txt` (:292 area), `/tmp/fleet-override.yml`
  (alias-endpoint-normalization.md:36,41,47,62; consumer-registry.md:61,327), and
  `/proc/2991185/cmdline` (listener-census.md:331) — all are evidence command bodies, and the
  `/tmp/fleet-override.yml` anchors are already covered by ring-10 correction A17
  ("current anchor: `none — dead surface`").
- The observed frontmatter gap (9/12 knowledge entries predate the declared field convention in
  CORPUS.md:9-15) is a provenance/fidelity observation for the parent, **not** a gate rule and not a
  semantic verdict; the gate implements no frontmatter check.

## 7. Directly evidenced study path (from `corpus/SOURCES.md` §Paths, membership re-verified)

**Health and readiness — `S001 → S004 → S006 → S020 → S017 → S021`.** Row evidence at 03b5f0e:
S001 llama.cpp server README, tier A, `mined`, used-by `runtime-health-surface-matrix.md` +
`serving-metrics-crosswalk.md`; S004 vLLM `/health` handler (`health(raw_request)`), A, `mined`,
used-by `runtime-health-surface-matrix.md`; S006 SGLang native APIs (`/health` vs one-token
`/health_generate`), A, `mined`, same used-by; S020 SGLang v0.5.22 release (health-routing fix), A,
`mined`, same used-by; S017 Kubernetes probes (lifecycle vocabulary), A, `mined`, same used-by;
S021 llm-d model-aware readiness probes, A, `queued`, used-by `—`. The sequence is therefore
directly checkable: five mined rows feed one live knowledge entry
(`runtime-health-surface-matrix.md`), and its last hop (S021) is a queued row with no consumer yet —
read the trail as "engine health surfaces first, external probe vocabulary last, not yet imported".
Caveat: this is row/status membership evidence, not proof that the cited pages say what the `teaches`
column claims (that would be a re-open; the gate's r1/r6 are not evaluated).

## 8. Scope, method, and residual risk

- Inspected: lane `corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md`, `SHONEN.md` bytes,
  the gate-flagged lines in `knowledge/{consumer-registry,free-tier-provider-limits,listener-census}.md`
  and `lessons/{round-1,round-1-citations,round-1-critic,round-1-safety,round-2,round-4-recensus,
  round-10,probe-mutation-matrix}.md`, plus `lessons/round-10-verifier-spotcheck.md` (unindexed file)
  and `corpus/knowledge/*.md` frontmatter only. Everything else in the lane was not opened.
- `lsp` was not applicable (Markdown/prose corpus, no language server target) — no semantic-LSP
  check was performed; all text claims above are mechanical grep/awk/node extractions whose exact
  commands are stated.
- Residual risk: (a) r4's 4 bare-count rows were not adjudicated against the rule's true intent
  (whether the reproducing command lives in the same table row) beyond the line-local read; (b) r1/
  r3/r5/r6/r9 and box-claim truth are unverified; (c) the census number is PROVISIONAL pending the
  parent's parser fix and `FINAL LANES READY`.