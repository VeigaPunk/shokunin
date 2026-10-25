# JjConnectorProvinces — which provinces own VCS knowledge, and where jj routes

Seat: `JjConnectorProvinces` (connector, leaf). **Report only.** No lane or PROVINCE file was
edited; no jj command ran against a live repo; no subagent was dispatched. One synthetic sandbox
probe ran under `/fast/scratch/jj-wave/JjConnectorProvinces-2/` (bare origin + clone, jj 0.45.1) and
was removed afterwards.

## Method

Read-only over the fleet:

```sh
find /home/vgpnk/Projects/shokunin -maxdepth 2 -name 'PROVINCE.md' | sort   # 21 files, 1297 lines
grep -rn -i 'jujutsu' */PROVINCE.md */SKILL.md */corpus | wc -l              # 2 (incidental quotes)
grep -rnE '(^|[^A-Za-z])jj([^A-Za-z]|$)' */PROVINCE.md */SKILL.md | wc -l    # 0
grep -c -i 'worktree' */PROVINCE.md                                         # souji 3, kumitate 1, game-dev-2d 1
```

Also read: `scripts/hyaku/jj-lane.sh` (contract, never edited), `scripts/hyaku/lane-addendum.md`
§4, `scripts/hyaku/closure-prompt.md` steps 1/4, `scripts/hyaku/inline.sh` head, the prior
`.ufo/waves/kaika/JJ-ADOPTION.md` and `.ufo/waves/kaika-w2j/*` probes, `mado-shokunin/corpus/lessons/round-14.md`,
and the lane corpora of kumitate / souji / tameshi / kotoba.

---

## Findings (observed)

### F1 — No province claims VCS. The ground is unassigned.

`grep -rn -i 'jujutsu' */PROVINCE.md */SKILL.md */corpus | wc -l` → `2`, and both are captured
transcript prose in kaidoku's provenance note, not an ownership claim:

```
kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-jq-provenance.md:27:  … setup jujutsu as the git
kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-jq-provenance.md:43:  - `jj` born 18:33:58.917 (agent-1 "JUJUTSU" lane; `~/.config/jj/config.toml`
```

Standalone `jj` in any `PROVINCE.md`/`SKILL.md` → `0`. Git appears in provinces only as a *tool
inside another surface* (worktree-prune hygiene, pushed receipts, gate history). No lane owns
"version control" as a domain, and no lane's corpus holds jj knowledge — the only jj domain prose
today sits in `.ufo/waves/kaika*` and in operator-side `scripts/hyaku/` comments/prompts, neither of
which is a learning-corpus entry.

### F2 — The nearest declarations, and how close each one actually is

| Lane | Declared ground (quote, line) | Distance to jj |
|---|---|---|
| **kumitate** | `Domain: orchestration & tooling` (`:3`); Frontier: "Isolation substrates for parallel agents (git worktrees, harness isolation backends) — `corpus/SOURCES.md` rows, queued" (`:21`) | **Closest.** jj colocated lane repos are an isolation substrate for concurrent writers. Cross-lane reading already assigns it this: game-dev-3d `PROVINCE.md:76` — "General orchestration and multi-agent tooling belong to `kumitate-shokunin`". Its `SOURCES.md` already carries `S014` git-worktree docs. |
| **souji** | `Domain: fleet repository & workspace hygiene` (`:3`); owns "dead worktree *metadata* (`git worktree prune`…)" (`:11`); **refuses** "Git history rewrite in any repo (reset/rebase/amend of published commits)" (`:28`); Frontier F1 git-native housekeeping, F2 repo-size census (`:52-56`) | Owns the **hygiene consequences**, not the write mechanics. Note the refusal: `jj undo`/`jj op restore` rewinding exported branch tips is exactly the refused class. |
| **tameshi** | `Domain: verification-fixture craft — the reusable method of honest checks` (`:3`); "a pattern is admitted from evidence in **TWO independent lanes** before it is claimed general" (`:14-16`); "Never edits a sibling's gate code (read-only probes…)" (`:17`); Frontier F4 golden/snapshot discipline, F5 hermetic environment normalization | Owns the **fixture-method rule**, never the jj facts or the helper. F4/F5 are the natural landing rows. |
| **kotoba** | `Domain: prompt & skill craft` (`:3`); `dispatch-prompt craft` (`:13`); Adjacent: "kumitate — orchestration/dispatch runtime and swarm lifecycle; **kotoba owns the prompt wording, not the runtime**" (`:27`) | Audits the *wording* of `lane-addendum.md` §4 / `closure-prompt.md`; does not own the semantics. |
| **mori** | `Domain: fleet & host observability` (`:3`); "lane silence grading (silent / progressing / progressing-weak)" (`:10`) | Its census reads `git rev-parse --verify -q HEAD` then `git log --since` (`tools/mori-census.sh:2197`), so it *consumes* VCS state. Probe-level caveat only. |
| **tsukuroi** | `Domain: host operability & system repair` (`:3`); 7-row Adjacent table (`:46-52`), **none about VCS**; "Never installs, upgrades, or removes packages" (`:25-28`) | Not an owner. `jj` is a user-local binary already recorded in `.ufo/waves/kaika/tooling-global.md` ("Already installed; configured per repo"). Routing jj there is a re-scope. |
| **mado** | `Domain: desktop & compositor craft` (`:3`); config plane read-only (`:6-12`) | Holds the **incident evidence** only (`corpus/lessons/round-14.md`, `LOG.md:1054-1056`). Not an owner. |
| kagi / chousa / kengaku / kaidoku / revenger / game-dev-2d/3d / audio / kotodama / lore / kake / kasegi / kama / tabi | Product or method domains; no VCS claim anywhere | No route. |

### F3 — souji's receipt gate is the one live consumer with the exact hazard, and the prior fix advice is wrong

`souji-shokunin/tools/souji-verify.sh` uses the detached-HEAD-sensitive command in four places:

```
231  # r6 fix: a pushed receipt also requires that NO unpushed commit
234  if [ "$(git -C "$repo" log --branches --not --remotes --oneline -- "$target" … )" != "0" ]; then
321  unpushed=$(git -C "$target" log --branches --not --remotes --oneline 2>/dev/null | wc -l || true)
671  if ! touching=$(git -C "$repo" log --format=%H HEAD --branches --not --remotes -- "$target" …)
952  if ! touching=$(git -C "$CREPO" log --format=%H HEAD --branches --not --remotes -- "$REL" …)
```

Sandbox reproduction (jj 0.45.1; bare origin + clone; `jj git init --colocate`; lane identity and
`snapshot.auto-track="none()"` set in repo config; one explicitly tracked file
`jj file track b.txt && jj commit -m c1 b.txt`):

```
$ git rev-parse --abbrev-ref HEAD
HEAD
$ git log --branches --not --remotes --oneline | wc -l
0
$ git log --all --not --remotes --oneline | wc -l
5
$ git for-each-ref --format='%(refname)' | head -7
refs/heads/master
refs/jj/keep/50080f5…          # five refs/jj/keep/* entries, abbreviated
…
refs/remotes/origin/master
```

After `jj bookmark set master -r @-`:

```
$ git log --branches --not --remotes --oneline | wc -l
1
$ git rev-parse HEAD; git rev-parse master
50080f535f85b9f1d3b725e02e0c2a3bf8e36bc0
50080f535f85b9f1d3b725e02e0c2a3bf8e36bc0
```

Two facts follow. (a) The undercount window is real but narrower than the kaika probe implies: the
helper always bookmarks before pushing (`jj-lane.sh:233-235`), so under the helper flow
`--branches --not --remotes` and `HEAD` are correct. The window opens only on a **forbidden raw
jj write** (`jj commit`/`jj new`/`jj describe` without the bookmark move) — i.e. the hazard is a
contract-violation detector, not a normal-path defect. (b) The kaika `souji.md` mitigation "use
`git log --all --not --remotes` if git-side" **overcounts**: `--all` includes jj's `refs/jj/keep/*`,
which reported 5 commits where only 1 was a real unpushed change. A `--all`-based receipt would
return `NOT-SAFE` forever in a colocated repo. *This is a contradiction between the prior wave's
advice and the observed ref layout; it must not be copied into a lesson unexamined.*

### F4 — The helper contract is the durable subject (read from source, not executed here)

`scripts/hyaku/jj-lane.sh` (operator-side; lanes never edit `scripts/`), with the behaviours a
candidate entry would have to pin:

| Surface | Observed contract | Line |
|---|---|---|
| binary | `command -v jj`, else `$HOME/.local/bin/jj`; **no version assertion anywhere** (`grep` for `--version`/`0.45` → none) | `:27-32` |
| `init` | refuses non-git dir; `jj git init --colocate` only if no `.jj`; first snapshot under `--config snapshot.auto-track="none()"`; then repo config `snapshot.auto-track=none()`, `user.name=<id>-shokunin`, `user.email=<id>@shokunin.local`, `trunk()="<branch>@origin"`; `bookmark track`; **warns** if `@` already tracks added paths | `:136-165` |
| `commit` | rejects absolute/`..`/glob paths and `.ufo/state/*`, `.ufo/watchdog.log`; skips missing with warning; `jj file track --include-ignored` for named **files**, plain `jj file track` for named **dirs** (so ignored content in a dir stays out); `metaedit --update-author` under the same per-command identity **before** `jj commit -- <paths>`; reads hash from `@-`; `bookmark set <branch> -r <hash>`; push | `:170-243` |
| `push` | refuses a conflicted tree via `heads(bookmarks(BRANCH)) & conflicts()`; `jj git push --remote origin --bookmark`; on rejection: fetch, `rebase -b` only `<branch>@origin..<branch>` with `--ignore-immutable`, re-point bookmark, 3 attempts, never force | `:100-131` |
| `state` | **pure git, zero jj calls**: branch via `symbolic-ref`→`origin/HEAD`→`master|main`→first; `local=`, `remote=`, `ahead=`, `behind=`, `head=attached|detached`, `tracked=`, `untracked=` | `:44-85` |
| immutability | the `::bookmarks()` alias is honoured if a repo already has it (`--ignore-immutable` only for the unpushed rebase) but **init never installs it**; selftest cases `b` and `h` cover alias present | `:116-131`, selftest `:75,:163` |

### F5 — PROTOCOL.md is stale relative to the helper in two places

```
PROTOCOL.md:120-121  "one that is not an ancestor of `HEAD` at closure is a conformance defect
                      (`git merge-base --is-ancestor <hash> HEAD` is the check)"
PROTOCOL.md:230      "…exists *and is an ancestor of* [HEAD]"
PROTOCOL.md:177      find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*'
grep -n '\.jj' PROTOCOL.md PROTOCOL-APPENDIX.md   → (no output)
```

The operator addendum and closure prompt already say the safer thing — ancestry against the
**branch ref**, never `@{u}` (`lane-addendum.md:131-134`; `closure-prompt.md:22-24`) — and
`inline.sh:33` states the same. So the fleet contract text, the only guaranteed delivery channel
("Text only in this file reaches the lanes that re-read it"), still encodes the pre-jj check and
omits `.jj/` from the activity scan.

### F6 — Colocation is already live in two lanes

```
$ ls -d tameshi-shokunin/.jj mado-shokunin/.jj
tameshi-shokunin/.jj
mado-shokunin/.jj
$ git -C tameshi-shokunin rev-parse --abbrev-ref HEAD   → master   (porcelain: 20 lines)
$ git -C mado-shokunin  rev-parse --abbrev-ref HEAD     → master   (porcelain: 5 lines)
```

Both carry in-flight round work, so `.jj` was created earlier (pilot) and the helper's
"pre-existing `.jj` may already track scratch in `@`" warning (`jj-lane.sh:156-160`) is the relevant
branch, not a fresh init.

---

## [INFERENCE]

- **VCS is unassigned because it is a substrate, not a domain.** The fleet's one-domain invariant
  (LEARNING.md, "Province is a frontier, not a fence") fits a split: the substrate claim belongs to
  the tooling lane (kumitate, whose declared frontier already names isolation substrates), and each
  *consumer* lane owns only its own consequence. There is no need to mint a VCS lane and no province
  text needs to say "we own git".
- **Routing is four narrow claims, not one shared corpus.** kumitate: substrate + hazards + helper
  contract. souji: hygiene/receipt consequences. tameshi: fixture-method rule. protocol: contract
  text. Anything broader re-creates the overlap the provinces exist to prevent.
- **A kumitate entry would document an operator-side tool, not own it.** `scripts/` is refused by
  souji (`PROVINCE.md:32-33`) and off-limits to lanes (`lane-addendum.md:104-109`); kumitate's role
  would mirror tameshi's "read-only primary surface" pattern (tameshi documents mado/tsukuroi gates
  without editing them).
- **tameshi's two-lane bar is not yet met for the `--ignore-working-copy` rule.** The only direct
  incident is mado r14 (`round-14.md`: "future read-only jj calls must use that flag"). souji's gate
  defect and mado's incident are the same *class* (tool assumes default git state) in two lanes, but
  tameshi should rule at its own gate rather than have the wave pre-admit it.
- **The protocol text is the highest-leverage single edit.** It is the only channel that reaches
  every lane every round; the addendum/closure already carry the correct rule, so the fleet is
  currently teaching two versions of the same invariant.

---

## Recommendations — routing map

| # | Durable item | Owner | Artifact | Must not absorb |
|---|---|---|---|---|
| R1 | Colocation hazards + helper contract (F4): detached HEAD, index reset, author/committer split, conflict push gate, `--ignore-working-copy`, `refs/jj/keep`, no version pin, `git worktree: No` in 0.45.x | **kumitate** | candidate `corpus/knowledge/jj-lane-vcs-substrate.md` with `source:`/`verified-at:`/`recheck:` (its Q1), new `SOURCES.md` rows (jj 0.45.1 git-compatibility, config `user.*`, concurrency/op-log, host `jj --version`, helper selftest receipt), frontier row `:21` advanced, plus a `## Mistakes` row in its next round lesson (`stale-premise`: "git HEAD is attached / `@{u}` works") | Does not own the helper code, the receipts, or the contract text |
| R2 | Hygiene consequences: `.jj/` self-ignores; `refs/jj/keep/*` keeps rewritten objects **reachable** (so an unreachable-object census misses them); `--branches --not --remotes` undercount window; colocated 0.45.1 refuses linked worktrees | **souji** | extend F1/F2 with a candidate `corpus/knowledge/jj-colocation-repo-hygiene.md`; add a SKILL caveat beside the "Unpushed-lane trap" row (`SKILL.md:75-79`) with a red-before fixture; keep the `--all` advice **out** (F3) | Does not absorb jj write mechanics, undo policy, or the helper |
| R3 | Fixture-method rule: VCS state is part of the fixture environment; a read-only claim needs an execution-inert flag; a VCS-writing fixture runs on a sandbox clone with a sandbox origin | **tameshi** | extend Frontier F4/F5 with a falsifiable arm; admit only if the two-independent-lane bar is met (cite mado r14 + souji F3); never edit souji's gate | Does not own jj facts or any sibling gate code |
| R4 | Contract text: `HEAD` → branch ref in the ancestry check (`PROTOCOL.md:120-121,230`); add `-not -path '*/.jj/*'` to the activity scan (`:177`); one VCS-neutral sentence that keeps the 40-hex git commit id as citation currency | **protocol lane** (integrator of record) | `PROTOCOL.md` + `PROTOCOL-APPENDIX.md` in an integrator round | Must not describe jj flags or become a tool manual; must stay true of both VCSs |
| R5 | Wording of the jj rules already delivered | **kotoba** | audit `lane-addendum.md` §4 / `closure-prompt.md` steps 1/4 for trigger/fidelity; report only | Does not adjudicate runtime semantics |
| R6 | Lane-head/silence probe caveat: `HEAD` equals the branch tip only while the helper's bookmark move holds | **mori** | probe-level note in its census; no provisioning/repair | Does not own jj or the protocol text |
| R7 | Incident evidence already filed | **mado** (r14 lesson, `LOG.md:1054-1056`), **tsukuroi** (`jj undo` rewinds exported tips, `kaika-w2j/tsukuroi.md` hazard 2) | keep where it is; cite from R1 | Must not grow a jj corpus or be re-scoped as VCS owners |
| R8 | Credential surface (report-only): a default-auto-track first snapshot or a named-file `file track --include-ignored` can admit an untracked/ignored secret-shaped file into a commit | **kagi** owns the tripwire; **kumitate** owns the helper rule | one routed line, no new kagi surface | Neither absorbs the other's ground |
| R9 | No route | chousa (method only), kengaku, kaidoku, revenger, game-dev-2d/3d, audio, kotodama, lore, kake, kasegi, kama, tabi | — | Do not seed jj entries in product domains |

**Delivery mechanism.** Every row above is a *routed candidate*, not a corpus write by this wave:
`PROTOCOL.md:244-245` has the integrator record one routing line per defect and the aggregator
mirror it into the owning repo's `corpus/lessons/`, keeping an open routed-defects row until the
owner's correction lands. The owning lane then admits it through its own gate — `corpus/knowledge/`
with the header triple, or a `corpus/lessons/round-<N>.md` `## Mistakes` row (class · evidence ·
captured-by · fix). This wave's report is evidence for that routing, not the admission.

**Sequencing (from the campaign record, [INFERENCE]):** souji r16 and tameshi r16 are in the current
batches (`.ufo/waves/hyaku/PHASE2.md`), so R2/R3 can ride their next rounds as routed items; kumitate
is not scheduled (next round 35 per `HANDOFF.md`), so R1 waits for its dispatch — the orchestrator can
carry the candidate text in the meantime, but only the owning lane may admit it to its corpus.

### Concurrent wave reports — what they already cover

Other seats in this wave audit per-lane git call sites; this report does not restate them, it
assigns their durable form. Four load-bearing excerpts:

- `JjAuditKumitate.md:71` — "Under jj, HEAD is a detached commit, not the branch: three gates can
  certify work that never landed" (a plain `jj commit` does not move the bookmark).
- `JjAuditMori.md:200` — "Output guards omit `.jj`" (`r15:1418`, `r16:747` protect `tools`, `.git`,
  `corpus` but not `.jj`).
- `JjAuditTsukuroi.md:101` — "`--revision HEAD` certifies `@-` (the previous commit), not the
  working copy; it can print PASS on content that violates the gate".
- `JjAuditKotoba.md:256` — "`git ls-files` is no longer author-controlled state (false-PASS
  vector) — **critical if the auto-track pin is ever absent**".

Two consequences for the routing above: (i) kumitate is simultaneously the proposed knowledge
owner **and** a lane with its own jj defects — R1 must not be read as a clearance of kumitate's
gates; (ii) the helper's `snapshot.auto-track="none()"` pin is load-bearing for at least one lane's
corpus gate, so R1 must document the pin's absence as a fail-closed condition, not a preference.

### Overlaps that must not be absorbed (explicit)

1. **souji receipts ≠ jj semantics.** souji certifies removability and refuses history rewrite
   (`PROVINCE.md:28`). jj's `undo`/`op restore` class is exactly that refusal; the prohibition belongs
   to R1/R4, not to souji's hygiene corpus.
2. **tameshi method ≠ helper implementation ≠ souji's gate.** tameshi may cite F3's failing command as
   evidence; it may not own the helper's contract or edit `souji-verify.sh`.
3. **kumitate substrate ≠ hygiene ≠ fixtures.** One entry, two consumers; no second copy of the facts.
4. **mado/tsukuroi incident notes ≠ ownership.** Both provinces are non-VCS by declaration; their
   notes are evidence pointers.
5. **kotoba wording ≠ runtime truth.** kotoba audits the prompt, not whether jj detaches HEAD.
6. **kagi tripwire ≠ snapshot mechanics.** kagi owns credential hygiene; the auto-track/`file track`
   behaviour is the tooling lane's fact.
7. **protocol contract ≠ tool manual.** PROTOCOL.md must remain true of git and jj without naming jj
   flags; the helper/addendum stay operator-side.

---

## Connector move (one bounded proposal)

**Evidence.** The fleet's own bars converge on a runnable artifact: `CORPUS.md:179-182` ("A fix is
shown able to fail before it counts"); kumitate's Q1 requires a `recheck:`; tameshi admits a pattern
only from two independent lanes; souji's receipt is fail-closed. Today the jj hazards exist only as
prose in a wave artifact (F1), and the prior wave's own mitigation (`--all`) is falsified by F3.

**Move.** Route the hazard as a **negative-control command, not a lesson narrative**: one entry in
kumitate whose `recheck:` is a sandboxed probe that (a) creates a bare origin + clone, colocated,
(b) shows `git log --branches --not --remotes` = 0 and `git rev-parse --abbrev-ref HEAD` = `HEAD`
after a bare `jj commit`, (c) moves the bookmark and shows = 1 with `HEAD == <branch>`, and (d)
shows `refs/jj/keep/*` inflating `--all`. souji's SKILL caveat and tameshi's F4/F5 arm then **cite
that `recheck:`** instead of restating jj facts. The durable unit becomes the command; the prose is
its annotation.

**Affected axes.** coverage (kumitate frontier row `:21` → sourced core), operability (souji/mori
probes gain a runnable caveat), freshness (PROTOCOL.md text re-derived), adjacency (no absorption,
one source of truth), calibration (tameshi's two-lane bar decided by its own gate). No axis is
harmed: mado/tsukuroi keep their incidents, and no gate is edited by a non-owner.

**Risks.** (1) The helper is operator-side, so neither kumitate nor tameshi can host the probe in
its own `scripts/`; the `recheck:` must be a self-contained snippet or cite the operator's
`jj-lane-selftest.sh` read-only. (2) jj 0.46 changes undo/workspace semantics (0.45.1 has no
cross-workspace `undo` guard; `git-worktree: No`), so an unpinned entry silently goes stale — the
entry must name the tested version `0.45.1-7c41cdeb` and a recheck trigger. (3) kumitate is
unscheduled; until its round lands, the probe lives only in this wave directory and can rot.

**Verification.** Run the `recheck:` snippet from a sandbox (expected: 0 / `HEAD` / 1 / `HEAD ==
branch`; `--all` > `--branches` with `refs/jj/keep/*` present); then `grep -c` for jj claims in
souji/tameshi corpora — the only hits should be the citation of kumitate's entry; and
`grep -n 'merge-base --is-ancestor' PROTOCOL.md` must resolve to the branch-ref form with
`grep -c '\.jj' PROTOCOL.md` ≥ 1.
