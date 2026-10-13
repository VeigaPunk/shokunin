# Round-9 aggregator wave — seat `GateDraft`: the corpus gate

**Deliverable.** Three files, all under `/home/vgpnk/projects/shokunin/.ufo/waves/round-9/`:

| Path | Bytes | Lines | sha256 |
|---|---|---|---|
| `.ufo/waves/round-9/corpus-gate.mjs` | 46236 | 888 | `68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8` |
| `.ufo/waves/round-9/corpus-gate.expected.json` | 16550 | 278 | `c358e79a0ea92ca2901ca794da4ae0c30bad5f1fafc38a4ffc37b28d5810f9ba` |
| `.ufo/waves/round-9/seats/gate-draft.md` | this file | — | — |

`sha256sum corpus-gate.mjs corpus-gate.expected.json` → the two digests above; `wc -lc` → the sizes above.
Node 24.19.0, zero dependencies, no network, no `require` (ESM). Committed by the L1 afterwards; **nothing was committed by this seat** and no state-mutating git verb was run (`status`/`log`/`show`/`archive`/`rev-parse`/`ls-files`/`cat-file`/`diff` only).

**Measurement stamp.** All cells below were measured inside `2026-09-29T00:47Z … 01:03Z`.
Main HEAD `383ea1a` at the final stamp (it was `62fdfbe` when this seat was briefed, and the fleet committed mid-wave).
Child revisions measured (STAMP-AFTER, `2026-09-29T01:01:42Z`):

| repo | HEAD | dirty (`git status --porcelain \| wc -l`) |
|---|---|---|
| kasegi-shokunin | `b7180b0` | 11 (was 10 at the first stamp, 6 in the seat brief) |
| kengaku-shokunin | `f09ff1f` | 3 |
| kake-shokunin | `a209441` | **0** (moved from `4c9a985`; the lane landed) |
| kumitate-shokunin | `7a099b2` | **0** (moved from `e0e5de1`) |
| kotoba-shokunin | `63ceba7` | 7 (moved from `3ea0e08`) |
| kagi-shokunin | `4b8c018` | 18 (moved from `4391b3b`) |

So at grading time the fleet had four dirty trees (kasegi, kengaku, kotoba, kagi) and two clean ones (kake,
kumitate) — not the two dirty trees the seat brief named. Per the dirty-tree rule, **every verdict this seat
reports is the verdict at a landed commit** (`--snapshot`), and every `--repo`/`--all` run is labelled
`provisional=1` by the gate itself.

---

## 1. Registry block (§Gate standard, `PROTOCOL.md:339`)

`node .ufo/waves/round-9/corpus-gate.mjs --registry --repo <dir>` echoes it. Verbatim observed output:

```
# registry name=corpus-gate kind=gate version=corpus-gate-v1
# registry entry-all="node .ufo/waves/round-9/corpus-gate.mjs --all"
# registry verdict-map 0=clean 1=failed 2=could-not-evaluate 3=failed (frozen-expectation drift)
# registry verdict-precedence 2 > 3 > 1 > 0
# registry selftest-flag --selftest pinned=corpus-gate.expected.json (selftest.cases[] + frozen[])
# registry write-scope read-only; writes only inside os.tmpdir() (selftest fixtures, snapshot extraction), removed before exit
# registry r8-classification could-not-evaluate
# registry check r2 CORPUS.md:19 a lessons/ entry cites its round and its evidence (commit hash, .ufo/reports/ path, or LOG.md)
# registry check r4 CORPUS.md:28 a count claim (<n> <count-noun>) on a line with no backticked command
# registry check r7 CORPUS.md:40 an index row (corpus-relative backticked path) naming a file absent from the graded tree
# registry check r8 CORPUS.md:43 credential material on the literal text, incl. op:// refs; unit=occurrences; fields occurrences/lines/files/owner/revision; schematic-vs-real classification declared could-not-evaluate (needs a vault read, operator-gated)
# registry check r10 CORPUS.md:21 the round's aggregator lesson corpus/lessons/round-<R>-aggregator-*.md is present (rule 10 verdict itself is the # verdict line)
# registry check shonen PROTOCOL.md §File contract SHONEN.md canonical form: header, exactly 4 canonical boxes, marks confined to the box char + at most one indented evidence line, [x] mark line carries a <verifier-id>, no other lines, trailing newline
# registry not-evaluated r1 CORPUS.md:18 reason=semantic (is this token a source?) + province tree partly absent (~/Projects/bounties gone)
# registry not-evaluated r3 CORPUS.md:20 reason=semantic (falsifiable-or-marked-opinion)
# registry not-evaluated r5 CORPUS.md:33 reason=needs negation+proximity NL parsing; a heuristic would fire on every prose "no X"
# registry not-evaluated r6 CORPUS.md:36 reason=needs the quoted surface (frontmatter/installed skill), which lives outside the graded repo
# registry not-evaluated r9 CORPUS.md:47 reason=append-only-vs-rewrite is history-dependent; snapshot mode grades a git-archive tree with no history; author-identity is a settable commit-time string
# registry not-evaluated box-3 PROTOCOL.md §Promotion gates reason=whether an [x] rests on a NON-author verifier needs the authorship graph of past rounds, which the graded tree does not carry; the shonen check sees a verifier-id token, not its independence
# registry not-evaluated shonen-semantics PROTOCOL.md §File contract reason=whether a box claim is true is prose; the shonen check grades canonical form only
```

Exit map: **`0` = clean, `1` = failed, `2` = could-not-evaluate, `3` = failed (frozen-expectation drift)**;
across repos and across a snapshot the precedence is **`2 > 3 > 1 > 0`**. Nothing else is exited. Flags:
`--selftest`, `--repo <dir>`, `--all`, `--snapshot <dir> <commit>`, `--round <N>` (default 9), `--json`,
`--registry`, `--repos a,b,c`.

**Registry-location defect (routed, not hidden).** §Gate standard says "the rows live in each lane's
`SKILL.md`". The aggregator lane has **no `SKILL.md`** — the same class of gap the round-8 ledger filed as
D-120 for the two main-repo lanes. Until that file exists the row cannot live where the clause says; it lives
in the script's registry block (echoed above) and in this file.

```
$ ls /home/vgpnk/projects/shokunin/SKILL.md
ls: cannot access '/home/vgpnk/projects/shokunin/SKILL.md': No such file or directory
$ echo $?
2
$ for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
    printf "%-20s SKILL.md=%s\n" $r "$([ -f $r/SKILL.md ] && echo yes || echo NO)"; done
kasegi-shokunin      SKILL.md=yes
kengaku-shokunin     SKILL.md=yes
kake-shokunin        SKILL.md=yes
kumitate-shokunin    SKILL.md=yes
kotoba-shokunin      SKILL.md=yes
kagi-shokunin        SKILL.md=yes
```

So every child lane has one and the two main-repo lanes do not. Owner: integrator/protocol (registry
placement), aggregator lane (its own row).

**Authorship caveat (`PROTOCOL.md` §Promotion gates).** A subagent the lane dispatched **is** the lane, so
this seat's verdicts on the aggregator lane's own artifacts (`corpus/lessons/round-*-aggregator-*.md`, the
6/6 class this gate's r8 owner field routes to `aggregator`) are **author-side, not non-author**. Where this
file grades the aggregator's own bytes it says so.

---

## 2. Self-test — capability, not measurement (§Gate standard, clause 2)

```
$ node .ufo/waves/round-9/corpus-gate.mjs --selftest
# selftest fx-clean expect_exit=0 got_exit=0 ids=0 PASS
# selftest fx-phantom-row expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-cred-real expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-cred-placeholder expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-cred-bearer expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-cred-token expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-r4-numeral expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-r2-uncited expect_exit=1 got_exit=1 ids=2 PASS
# selftest fx-r10-missing expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-no-readme expect_exit=1 got_exit=1 ids=1 PASS
# selftest fx-shonen-dev expect_exit=1 got_exit=1 ids=2 PASS
# selftest fx-no-corpus expect_exit=2 got_exit=2 ids=0 PASS
# selftest tally 12/12 PASS (fixtures under os.tmpdir(), live tree untouched)
$ echo $?
0
```

* **Both** the exit code **and** the exact ordered finding-id list are asserted, per case.
* Fixtures are built by the script under `fs.mkdtempSync(os.tmpdir())` and removed in a `finally`; the live
  tree is never written. Network: none.
* Expected values are in `corpus-gate.expected.json` → `selftest.cases[]` — a **static, hand-authored** file
  the gate only *reads*. The eleven `expect`/`exit` duplicates that briefly existed inside the script were
  deleted (they were a second source of truth); the script now carries only `name`, `round` and the fixture
  bytes.
* Each fixture carries a canonical `SHONEN.md`, so `fx-shonen-dev` is the *only* case with a shonen finding —
  the check is exercised on both sides.
* Negative pins inside `fx-clean` (exit 0): a README line `Credential sweep (round 8): 0 hits (`grep -rn`;
  token/secret/cookie/bearer patterns).` — the `bearer patterns` / `token/secret/cookie` prose that really
  fired on kengaku/kagi before the value-shape filter (`§7`, FP-5).

---

## 3. Frozen-run evidence — measurement (§Gate standard, clause 3)

Command per row (8 rows; each extracts `git archive <commit> | tar -x -C <mktemp -d>` and grades the frozen
tree, then deletes it):

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/projects/shokunin/<repo> <commit>
```

| key (frozen[] entry) | exit | finding-ids | rules that fired | index rows(r7) |
|---|---|---|---|---|
| `kasegi-shokunin@b7180b0` | 1 | 49 | r2=3 r4=44 r8=1 r10=1 | 0 |
| `kengaku-shokunin@f09ff1f` | 1 | 28 | r4=25 r8=1 r10=1 shonen=1 | 0 |
| `kake-shokunin@a209441` | 1 | 37 | r4=35 r8=1 r10=1 | 0 |
| `kake-shokunin@4c9a985` | 1 | 34 | r4=32 r8=1 r10=1 | 0 |
| `kumitate-shokunin@7a099b2` | 1 | 36 | r2=1 r4=33 r8=1 r10=1 | 0 |
| `kotoba-shokunin@63ceba7` | 1 | 75 | r4=61 r8=2 r10=1 shonen=11 | 0 |
| `kagi-shokunin@4b8c018` | 1 | 51 | r2=8 r4=36 r8=4 r10=1 shonen=2 | 0 |
| `kagi-shokunin@4391b3b` | 1 | 46 | r2=8 r4=31 r8=4 r10=1 shonen=2 | 0 |

All eight print `# expect <key> MATCH exit=1 ids=<n>` and the process exits `1`. `kake@4c9a985` and
`kagi@4391b3b` are the two revisions the seat brief named (both are aggregator-identity commits — subject
line `corpus: round-8 aggregator box-3 amendment`); the *landed* revisions at grading time were `a209441`
and `4b8c018`, so both are pinned. The four currently-dirty repos each have their landed HEAD pinned
(kasegi, kengaku, kotoba, kagi).

**The drift mechanism was observed biting, not just asserted.** While this gate was being tightened, the
kengaku entry was edited in the opposite direction (one false-positive finding removed). The next run printed:

```
# expect kengaku-shokunin@f09ff1f DRIFT committed_exit=1 got_exit=1 committed_ids=[...29 ids...] got_ids=[...28 ids...]
# process-exit 3 (failed)
```

i.e. a change to the gate — not to the input — contradicts a value frozen for an unchanged revision, and the
run exits `3`, a code declared and mapped to `failed`. The entry was then corrected to the measured verdict
for the tightened check, and the run returned to `MATCH`.

**`sys.exit` currency check.** `--round 8` with `--all` removes the `r10` finding from all six summaries
(`# summary … rules=r4,r8,shonen`, etc.), because all six repos *do* carry
`corpus/lessons/round-8-aggregator-box3-coldrun.md`: the r10 check can pass, so its fleet-wide red at round 9
is a timing fact (this round's lessons are not landed yet), not a check that can never go green.

---

## 4. Live runs — `--repo` / `--all` (§Gate standard, clause 4)

```
node .ufo/waves/round-9/corpus-gate.mjs --all            # worktree as it is; verdicts are provisional
```

| repo | rev | dirty | exit | findings | rules | live-vs-landed delta |
|---|---|---|---|---|---|---|
| kasegi-shokunin | `b7180b0` | 10 | 1 | 56 | r2,r4,r8,r10 | +7 (r4 +5, r8 +2 — 8 untracked corpus files, incl. `instruments/density.py`, `instruments/resolve.py`, `knowledge/source-tree-loss-2026-09-28.md`) |
| kengaku-shokunin | `f09ff1f` | 3 | 1 | 29 → **28**\* | r4,r8,r10,shonen | 0 (19 untracked corpus files that add no finding) |
| kake-shokunin | `a209441` | 0 | 1 | 37 | r4,r8,r10 | 0 (clean tree: live == landed) |
| kumitate-shokunin | `7a099b2` | 0 | 1 | 36 | r2,r4,r8,r10 | 0 (clean tree) |
| kotoba-shokunin | `63ceba7` | 7 | 1 | 83 → **81**\* | r4,r8,r10,shonen | +8 → +6 (worktree-only r4 lines) |
| kagi-shokunin | `4b8c018` | 1 → 18 | 1 | 51 | r2,r4,r8,r10,shonen | 0 |

\* the arrow is the *second* live run (01:02Z, dirty 11/3/0/0/7/18) against the first (00:57Z, dirty
10/3/0/0/7/1). The kengaku drop is this seat's own check-tightening (§7 FP-5); the kotoba drop is worktree
drift inside the wave. Live fleet total: **292** findings (first run) / **289** (second run); all six repos
exit `1`. The gate prints `provisional=1` on every dirty row and names both revisions — a live verdict is not
comparable to a frozen one, exactly as §Gate standard says.

Read-only: the only writes are the `mkdtemp` fixture/archive trees. `git` verbs used are
`rev-parse`, `status`, `archive`, `ls-files --others --deleted`, and nothing else.

---

## 5. What the gate actually finds — the round's rule-10 verdicts at landed HEADs

Command (one row of the table below):

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/projects/shokunin/<repo> <head> | \
  awk '/^# verdict|^# process-exit/'
```

| repo @rev | r1 | r2 | r3 | r4 | r5 | r6 | **r7** | **r8** | r9 | **r10** | shonen | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kasegi `b7180b0` | n/e | 3 | n/e | 44 | n/e | n/e | **0** | 1 | n/e | 1 | 0 | not conformant — 2, 4, 8, 10 |
| kengaku `f09ff1f` | n/e | 0 | n/e | 25 | n/e | n/e | **0** | 1 | n/e | 1 | 1 | not conformant — 4, 8, 10, §File contract |
| kake `a209441` | n/e | 0 | n/e | 35 | n/e | n/e | **0** | 1 | n/e | 1 | 0 | not conformant — 4, 8, 10 |
| kumitate `7a099b2` | n/e | 1 | n/e | 33 | n/e | n/e | **0** | 1 | n/e | 1 | 0 | not conformant — 2, 4, 8, 10 |
| kotoba `63ceba7` | n/e | 0 | n/e | 61 | n/e | n/e | **0** | 2 | n/e | 1 | 11 | not conformant — 4, 8, 10, §File contract |
| kagi `4b8c018` | n/e | 8 | n/e | 36 | n/e | n/e | **0** | 4 | n/e | 1 | 2 | not conformant — 2, 4, 8, 10, §File contract |

(`n/e` = declared `not-evaluated`, §9.) **All six are `not conformant` at their landed HEADs** — but not for
the rules §11.1 named. The differences are the substance of this gate's contribution; see §6.

Two findings are new in this refresh and not in any ledger row this seat could find:

* **kagi: 8 of its 15 lesson files carry no evidence pointer at all** (`lessons/round-1-aggregator-audit.md`,
  `round-3.md`, `round-4.md`, `round-5.md`, `round-6.md`, `round-7.md`, `round-8.md`, `round-10.md`). Verified
  independently, not inferred:
  `git -C kagi-shokunin show 4b8c018:corpus/lessons/round-4.md` → 2896 bytes, `[0-9a-f]{7,40}` matches: `[]`,
  `LOG.md` count `0`, `.ufo/reports/` count `0`; same for `round-5`/`round-7`/`round-8`. These lessons cite a
  round and a prompt path, but no commit, no `LOG.md`, no report path — the rule-2 defect class §11.3 named for
  kotoba ("3 new unresolvable `commit round-N` cites"). kasegi: 3 (`round-10`, `round-12`, `round-13`),
  kumitate: 1 (`round-9`).
* **§File contract: 0 of 6 `[x]` marks fleet-wide carry a `<verifier-id>`**, and 3 of 6 SHONEN files are
  canonical-form clean — all three are the trivially-unmarked ones (kasegi, kake, kumitate, all `[    ]`).

---

## 6. Rule 8 — unit, revision, owner, and the literal-text conflict

**The unit is declared and printed.** `occurrences=` (substring occurrences), `lines=`, `files=`, the graded
`at <rev>`, and `owner=aggregator|lane` (by the `round-<N>-aggregator-*.md` filename pattern), so the row
routes to whoever owns the bytes. Example observed line:

```
CR-kagi-shokunin-r8-4: credential-class op-ref occurrences=66 lines=65 files=22 owner=lane at 4b8c018
  maxseg=3 :: classification=could-not-evaluate (needs a vault read; operator-gated)
  files=[drift-pins.sh,knowledge/drift-gate.md,...] first=drift-pins.sh:22 first4="op:/" len=5 (CORPUS.md:43)
```

`op://` totals at landed revisions — gate (runtime) vs an **independently written python sweep** reading the
same `git archive` (whole-file `findall` vs the gate's per-line scan), plus a third pass with **no extension
filter** (the only paths that make the whitelist matter):

| repo @rev | gate occurrences | python occurrences | python lines | python files | no-filter occurrences | owner split (aggregator / lane) |
|---|---|---|---|---|---|---|
| kasegi `b7180b0` | 2 | 2 | 2 | 2 | 2 | 2 / 0 |
| kengaku `f09ff1f` | 1 | 1 | 1 | 1 | 1 | 1 / 0 |
| kake `a209441` | 2 | 2 | 2 | 2 | 2 | 2 / 0 |
| kumitate `7a099b2` | 1 | 1 | 1 | 1 | 1 | 1 / 0 |
| kotoba `63ceba7` | 3 | 3 | 3 | 2 | 3 | 1 / 2 |
| kagi `4b8c018` | 77 | **77** | **75** | **26** | 77 | 11 / 66 |
| kagi `4391b3b` | 54 | 54 | 53 | 23 | 54 | 11 / 43 |

The three `git archive` sweeps were run as
`python3` over `subprocess.run(['git','-C',<repo>,'archive',<rev>])` + `tarfile`; the counting command
reproduces its own value every time, and the no-filter pass shows the extension whitelist costs nothing at
these revisions (0 binary/skipped files, 0 hits outside the whitelist).

**Reconciliation with the sibling stamp (named disagreement).** SentinelSeat's early stamp reported landed
`op://` counts `2/1/2/1/3/55`. Five of six agree exactly with this gate (`2 / 1 / 2 / 1 / 3`). kagi differs:
**55 vs 54**. The difference is visible and explained by the same unit/revision discipline the L1 demanded:
this seat's own worktree read of kagi *before* the lane landed gave **55 occurrences in the dirty worktree**;
the *landed* `4391b3b` tree gives **54** (`53` lines, `23` files) — one occurrence lived only in the then-dirty
worktree (kagi was dirty 21 at that stamp). The L1's baseline for the later revision, `77 occurrences / 75
lines / 26 files at 4b8c018`, is reproduced **exactly** by this gate. So: no disagreement about the bytes, one
disagreement about *which* bytes — the gate's answer is the landed revision, named in the finding text.

**Literal text vs practice — the routed row.** `CORPUS.md:43-46` reads *"Secret values, session tokens,
cookies, and **vault ref paths (`op://…`)** stay out of every corpus, including this one's examples."* Round 6
(§11.1) recorded "70 `op://` hits are prose/schematic placeholders" and graded rule 8 **clean fleet-wide**.
This gate grades the literal text and therefore reaches the opposite verdict: **all six corpora fail rule 8**
(1–77 occurrences each). Per the L1's amendment, the schematic-vs-real classification is declared
`could-not-evaluate` rather than guessed (deciding it needs a vault read, which is operator-gated), and the
mechanical shape facts are printed instead (`maxseg=`, `literal_shaped=`):

* `maxseg=0` for kasegi/kengaku/kumitate/kotoba and for kagi's aggregator-owned hits — i.e. the matches are
  the bare scheme (the corpora are *quoting the sweep pattern*, e.g. kengaku `round-5-aggregator-audit.md:56`
  "`Credential sweep 0 hits (`grep -rn 'op://' corpus/ SKILL.md SHONEN.md LOG.md`; token/secret/cookie/bearer
  patterns)`"). `maxseg=3` for kagi's lane-owned hits — full `op://vault/item/field` shapes.
* **Owner split is the routable fact.** In 5 of 6 repos every `op://` occurrence is inside an
  **aggregator-owned** lesson (`round-5-aggregator-audit.md`, `round-6-aggregator-audit.md`); only kotoba
  (2, in `knowledge/sibling-description-rewrites-round8.md`) and kagi (66, 22 files, domain-intrinsic — kagi's
  province *is* vault ops) carry lane-authored occurrences. **The aggregator lane is the owner of the bulk of
  this red, and this seat is that lane (author-side).** That is exactly how round 6 graded the fleet clean on a
  rule its own files broke.

**The conflict is a routed row for the integrator** (owner: `integrator`/`operator`, rule 8): either the rule
means what it says and six corpora fail it, or it needs an amendment distinguishing a secret *value* from a
*pointer to* one. This gate deliberately does not resolve it; it prints both the literal count and the
routable owner.

Value classes at landed revisions (all `owner=lane` except where noted): kagi `bearer` 1 occurrence /
`literal_shaped=1/1` (`knowledge/handler-trust-boundary.md:37`, `Authorization: Bearer jt-test-pw` — a test
credential in a documentation table), kagi `kv-secret` 3 occurrences / `literal_shaped=0/3` (a grammar line
`reason=first-token:<w>|metachar|…`, a code expression `token = base64.b64encode(f"opencode:{password}"…)`,
and a schema field `password: string("OPENCODE_SERVER_PASSWORD")` — all three are documentation, see FP-4).
Zero `sk-`, `github_pat_`, `xox*`, `AKIA`, JWT, `BEGIN … PRIVATE KEY`, or `cookie:` occurrences at any landed
revision. **Named disagreement:** SentinelSeat's stamp reported `sk-`/`xox` classes in kagi; this gate finds 0
of each at both `4391b3b` and `4b8c018`, with a no-extension-filter pass and a looser
`\bsk-[A-Za-z0-9_-]{16,}`/`\bxox[baprs]-[A-Za-z0-9-]{8,}` pattern. Either their sweep ran on a worktree/revision
this seat did not see, or their pattern was looser (e.g. matching `sk-` inside prose like "risk-free"). Not
reproducible here; recorded rather than inherited. No secret value is printed anywhere in this file or in the
gate's output — only file, line, class, `first4="<4 chars>"` and `len=`.

---

## 7. SHONEN canonical form, and where the heuristic over/under-fires

`checkShonen()` implements the §File contract algorithm as amended by the L1 (strip one trailing newline;
header block byte-equal modulo `<name>`; exactly 4 boxes with the canonical text; mark ∈ `{x,~,space}`; at
most one indented (`^\s+\S`) evidence line per box; a marked box needs one; an `[x]` mark line needs a
`<verifier-id>` token after the box text; no other lines; trailing newline required). Measured

| repo @rev | trailingNL | marks | evidence lines | other lines | deviations (gate) | L1 amendment | box marks |
|---|---|---|---|---|---|---|---|
| kasegi `b7180b0` | yes | `[    ]` | 0/0/0/0 | — | **0** | 0 | 0/4 |
| kengaku `f09ff1f` | yes | `[~~x~]` | 1/1/1/1 | — | **1** (`[x]` at line 9, no verifier-id) | 1 | 1/4 |
| kake `a209441` | yes | `[    ]` | 0/0/0/0 | — | **0** | 0 | 0/4 |
| kumitate `7a099b2` | yes | `[    ]` | 0/0/0/0 | — | **0** | 0 | 0/4 |
| kotoba `63ceba7` | yes | `[~~~~]` | 10/5/13/1 | 38–45 | **11** (3 boxes >1 evidence line + 8 other lines) | **9** | 0/4 |
| kagi `4b8c018` | **no** | `[xxxx]` | 1/1/1/1 | — | **2** (no trailing newline; 4 `[x]` at 5,7,9,11 without a verifier-id — counted once, file-level) | 2 | 0/4 |

Fleet totals: **0 of 6 `[x]` marks carry a verifier-id; 3 of 6 files are canonical-form clean and all three are
the trivially-unmarked ones** — reproducing the L1's fleet conclusion exactly.

The §7-independent python re-implementation (mark string, per-box evidence counts, unconsumed line numbers)
agrees with the gate on all six files, including kotoba's `ev=[10, 5, 13, 1]` and `other-lines=[38..45]`.

**Named disagreement (kotoba 11 vs 9).** My count is 3 box-evidence overflows + 8 unconsumed lines. The
residual 2 is a *reading*, not an error in either implementation, and I cannot see the L1's basis: a
"blank lines are separators" reading gives 10 (dropping line 38), and additionally waiving box 2's 5-line note
gives 9. Both readings are auditable from the table above; the L1 should pick one and the gate can be pinned
to it (it is a one-line change in `checkShonen`). Owner: aggregator/§File contract.

### False-positive classes (the gate over-fires; this is the honest part)

| id | class | gate vs observed |
|---|---|---|
| FP-1 | **r4 non-count numeral** — a numeral + count-noun that is not a count claim: a compound ("task 27 tests", "27 test-timeout"), a rubric/box/matrix ordinal ("`\| 10 citations resolve \|`", "18 files × AD-1…AD-9"), a heading number. | kengaku r4-4/r4-5, kotoba r4-1/r4-23 |
| FP-2 | **r4 design arithmetic** — planned numbers, not observations ("Phase 2 core: 12 tasks × 2 conditions = 24 runs", "Floor: 36–40 runs total"). | kengaku r4-8…r4-11 |
| FP-3 | **r4 quoted claim** — a falsified count quoted inside a *correction entry*, which rule 9 (append-only) **requires** ("`"20 rows"` — the registry has 21"). The two rules collide by construction. | kake r4-1, kasegi r4-15/r4-32 |
| FP-4 | **r8 value-class documentation** — `token:<w>\|metachar\|…`, `token = base64.b64encode(…)`, `password: string("OPENCODE_SERVER_PASSWORD")`. All three kagi `kv-secret` hits; `literal_shaped=0/3` prints the tell. | kagi r8-2 |
| FP-5 | **r8 bearer prose** — `Bearer auth was`, and a lesson quoting its own sweep list `token/secret/cookie/bearer patterns` (kengaku, aggregator-owned). **Fixed** during this seat: the pattern now requires a token shape (≥8 chars **and** a digit or one of `._+/-`), which removed 1 kengaku finding and 2 of kagi's 3 bearer occurrences, and is pinned by `fx-clean` (negative) + `fx-cred-bearer` (positive). | kengaku pre-fix; kagi pre-fix |
| FP-6 | **r4 cross-line command** — the prescribed `<command>` lives in a sibling line/paragraph while the rule's form is line-scoped. The check is line-scoped by construction, so a corpus that hoists the command is red. | kasegi r4-13 (`7225 lines as of 2026-09-28T…Z`) |
| FP-7 | **shonen blank separator** — one blank line before a trailing note counts as an "other line" under the literal "no other lines may exist". | kotoba shonen-4 |

### False-negative classes (the gate under-fires)

| id | class | why |
|---|---|---|
| FN-1 | **r7 bare-name phantom rows** — a row written as a bare basename (`knowledge/`-less) that names no file is *not* a finding: an unresolvable bare name is indistinguishable from a province file (`SKILL.md`, `SUBMITTED.md`, `LOG.md`, `RUNBOOK-resume.md`, `CLAIMER-MISSION.md`… are all real index-column text in these READMEs). Phantom rows only fire when the row is corpus-relative (`knowledge/|lessons/|evidence/|handoffs/`). |
| FN-2 | **r7 under-coverage is a note, not a finding** — and this is a *real divergence from the ledger*: §11.1/§11.3 charged rule 7 with under-coverage readings ("kengaku index 6 rows / 8 files", "kasegi README missing `program-quirks.md` row"). Under the literal rule text (`CORPUS.md:40`: write the row when the file exists, *not before*) those are not defects; my r7 counts 0 phantom rows fleet-wide. The under-coverage numbers are still printed so the ledger's reading stays checkable: kasegi 24/49, kengaku 102/137, kake 15/33, kumitate 0/45, kotoba 3/43, kagi 12/47 (live, second run). **A non-author cannot reproduce the ledger's rule-7 verdicts from the rule text.** |
| FN-3 | **r7 template/glob rows skipped** — 5/8/1/4/14/8 backticked path templates per repo (kasegi/kengaku/kake/kumitate/kotoba/kagi) contain `*`, `<`, `{`, `~`, `$` or `…` and are counted, not resolved (printed as a note). `lessons/round-<N>.md` and `lessons/round-{1,4,5}-aggregator-audit.md` are handled (`{}` expanded, `…` ranges expanded, `<N>` skipped); a template that silently fails to expand is invisible. |
| FN-4 | **r2 passes on an incidental `LOG.md` mention** — the evidence test is "a 7–40-hex token, or `.ufo/reports/`, or the string `LOG.md` anywhere in the file", so a lesson that name-drops `LOG.md` in passing satisfies it. kagi's eight failures are lessons with *none* of the three. |
| FN-5 | **r8 pattern classes only** — a secret in an unenumerated form (npm `npm_…`, a base64 blob, a PEM key without the `BEGIN` banner, a token split across lines) is invisible; and the schematic-vs-real call is declared `could-not-evaluate` by design, so the gate never states that a real vault path leaked. |
| FN-6 | **shonen grades form, not truth** — a box claim that is false but well-formed passes (`shonen-semantics`, declared). A verifier-id that is present but author-side (the round's actual box-3 problem) also passes (`box-3`, declared). |
| FN-7 | **r10 is a timing artifact** — red fleet-wide at `--round 9` because this round's aggregator lessons are not landed; it flips green on `--round 8` for all six. A reader who quotes the r10 red as a lane defect would be wrong. |

---

## 8. Divergences from §11.1 (what a non-author cannot reproduce)

| §11.1 rule charged | this gate | why |
|---|---|---|
| r4, all six | reproduced (234 findings at landed HEADs) | same class, different count; unit = "a count claim on a line with no backticked command" |
| r7, kasegi (row missing) / kengaku (6 rows, 8 files) / kumitate (7, 6) / kotoba (7) | **0 findings all six**; under-coverage printed as a note | FN-2: the ledger used an under-coverage reading the rule text does not carry |
| r9, kasegi/kengaku/kumitate | **declared `not-evaluated`** | FN/§9: history-dependent; not honestly mechanical |
| r1/r3/r5/r6 | **declared `not-evaluated`** | semantic or out-of-repo surfaces |
| r2 nominal for kengaku/kake/kotoba/kagi… | kagi **8**, kasegi 3, kumitate 1; kengaku/kake/kotoba 0 | a new, re-derivable row (kagi's lessons cite rounds but no evidence) |
| rule 8 "clean everywhere" (§11.1) | **all six fail on the literal text** | §6 — the routed row for integrator/operator |
| rule 10 (stale since refresh 6) | **6/6 re-emitted at landed HEADs**, each naming its revision | this gate is the re-derivation mechanism the round asked for |

---

## 9. Declared `not-evaluated` (never faked)

* **r1** (`CORPUS.md:18`) knowledge cites a source — deciding "is this token a source?" is semantic, and the
  province tree is partly gone (`~/Projects/bounties` absent per wave context).
* **r3** (`:20`) falsifiable-or-marked-opinion — semantic.
* **r5** (`:33`) a negative claim carries its sweep — needs negation + proximity parsing; a heuristic would
  fire on every prose "no X". The round-6 rule-5 findings were hand-adjudicated; this gate declines to pretend.
* **r6** (`:36`) a quote names its location — needs the quoted surface (frontmatter/installed skill) outside
  the graded repo.
* **r9** (`:47`) corrections are new entries / no cross-lane edits — the one mechanical sub-check
  (aggregator identity in `git log -- <lesson>`) is not decisive: the identity is a settable commit-time
  string, an in-place rewrite by the legitimate owner is invisible to it, and `--snapshot` grades a
  `git archive` tree with **no history**, i.e. the check is unavailable in exactly the mode whose verdict must
  name a revision.
* **box-3** — whether an `[x]` rests on a *non-author* verifier needs the authorship graph of past rounds;
  the shonen check sees a verifier-id token, not its independence.

---

## 10. Handoff to the integrator (§Gate standard, closure consequence)

* A red gate is a conformance defect recorded in the round notes and routed to its owner, **status-neutral**;
  this file's reds are evidence, not verdicts on lane promotion.
* The integrator **verifies this gate's committed evidence** (the `--selftest` tally `12/12`, the eight frozen
  runs' `MATCH` lines and the revisions they name, the two sha256 digests) and does **not** execute a
  sibling's gate.
* Routed rows from this seat: (i) rule 8 literal-vs-practice → `integrator`/`operator`, rule 8; (ii) the
  aggregator lane's own `op://` occurrences in `round-5/6-aggregator-*` lessons → `aggregator` (author-side);
  (iii) the gate's registry row has no legal home (no aggregator `SKILL.md`) → `integrator`/`protocol`;
  (iv) `checkShonen`'s kotoba reading 11-vs-9 → integrator to pick a reading; (v) r10 red is a timing
  artifact to be re-run after the round's lessons land (`--round 9 --all`).
* Re-run commands, copy-paste from the main repo root:
  `node .ufo/waves/round-9/corpus-gate.mjs --selftest`,
  `node .ufo/waves/round-9/corpus-gate.mjs --all`,
  `node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/projects/shokunin/kagi-shokunin 4b8c018`.

---

## 11. Blockers / limits

* No `--json`-to-ledger writer: the gate prints one finding per line (`CR-<repo>-<rule>-<n>: <text>`) plus a
  `# json [...]` line; a distiller can consume either.
* The gate grades **trees, not histories**; nothing here can date a defect or detect an in-place rewrite.
* kagi moved `4391b3b → 4b8c018` mid-wave and its worktree moved 1 → 18 dirty entries inside this seat's
  4-minute window; every number above names the revision or stamp it belongs to. Nothing was re-measured to
  match a preferred answer.
* This seat wrote only the three files listed at the top. No commits, no child-repo writes, no host-mutating
  verbs; no check in this file needed one, so there are **no** `gated-without-artifact` rows.

---

*Seat protocol (not evidence): `DESPAWN: gx-gatedraft-corpusgate — signal delivered. Send me shutdown_request.`*