# Closure evidence sweep — round-13 pass (read-only map + the entries it owes)

Scope: read-only data set for the round-13 closure pass. Nothing outside this file and
`round13-entries.json` was written; `MANIFEST.json` was **not** touched (its digest is pinned below and
was re-checked after the sweep). Measurement clock **2026-09-28 22:21:00–22:25:00 -03:00**; every
command below was executed in that window.

Instruments and anchors at the instant of writing:

| anchor | value | command |
|---|---|---|
| `MANIFEST.json` | sha256 `db69d052c39d0dbb5bbe30de944c0ac7c65729f2217a49f26ddaa2321cd2477f`, 36 `rounds[]` entries | `sha256sum MANIFEST.json`; `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"` |
| `PROTOCOL.md` | 526 lines / 49269 B, sha256 `22cb61ce89ce6af42dfb7b753d952ca0cbc7a22532c5a01b0c9aca72b8ac4638` (un-compacted at this instant; the compaction is still drafted at `.ufo/waves/round-13/PROTOCOL.compact.md`) | `wc -l -c PROTOCOL.md`; `sha256sum PROTOCOL.md` |
| `.ufo/watchdog.log` | 243 lines; last line `2026-09-28T22:22:19-03:00 tick=37` | `tail -4 .ufo/watchdog.log` |
| main repo `HEAD` | `3d206761b6cd985ad50adae4930c10210e843bcb` | `git rev-parse HEAD` |
| child `HEAD`s | kagi `baec94fbc7dc40991b8a65ab4fb4217633c8246c`, kake `421410199fd5840cce64769a91a8fc7f6a265863`, kasegi `b021dc925f5cc17702ebff6ffa25c3b6e4efcf7b`, kengaku `e171cdfbdb350ee90bfc1c66dac54106a3a5e2ca`, kotoba `0f658ff276fe0076413c866d4b8694811b554536`, kumitate `637d1815bef717c9275d142fe746e51f68660063` | `git -C <repo> rev-parse HEAD` |
| lane counters | protocol 13, aggregator 9, kagi 15, kake 15, kasegi 16, kengaku 12, kotoba 15, kumitate 15 | `cat .ufo/state/<lane>.round` |

`.ufo/watchdog.log` is mutable and the driver appends concurrently, so **quotes are text, not line
numbers** (line numbers are given only as a convenience and had already drifted once inside this
sweep: `wc -l` read 236, then 239, then 243). Tow quoted lines changed *under* the sweep and both are
recorded below with their exact timestamps: tick=37 (22:22:15–22:22:19) terminated kumitate r14 and
kagi r14 and dispatched kumitate r15 and kagi r15.

## `closed_at` for this pass

**`2026-09-28T22:23:00-03:00`** for every entry in `round13-entries.json`. It is at or after the
newest evidence any entry cites: `complete kasegi round=15` 22:14:43, `launch kasegi round=16`
22:14:45, the aggregator's six child-repo commits 22:19:05–22:19:06, kumitate r14's report commit
`3d20676` 22:20:09, kagi r14's report mtime 22:21:02, and tick=37's four lines ending
`2026-09-28T22:22:19-03:00 tick=37`. It is a deliberately *tight* instant (≈40 s after the log's last
line at the final read) because the gate compares evidence timestamps against `closed_at`: a row is
right if it was right at that instant, and a driver tick at ~22:29 landing a `complete` line after it
cannot falsify it. It is also required by PROTOCOL that `closed_at` be present on every entry carrying
a `not-dispatched` row — the round-15 entry carries three.

## Lane-round rows (13)

`lr` = lane-round. Dispatch/termination = verbatim `.ufo/watchdog.log` lines. Report metrics: bytes,
tracked-or-untracked (`git ls-files --error-unmatch <p>`, exit 1 = untracked), adding commit
(`git log --diff-filter=A --format='%H %an <%ae> %aI' -1 -- <p>`), ancestor of that repo's `HEAD`
(`git merge-base --is-ancestor <h> HEAD`). `SHONEN` = `grep -cE '^#{1,6} *SHONEN' <p>`.

### 1. protocol r12 — debt row (entry #25, `in-flight`) → **`ok`**

- (a) dispatch `2026-09-28T20:28:21-03:00 launch protocol round=12 runId=shokunin-r12-protocol-r1790638100`;
  termination `2026-09-28T21:51:57-03:00 complete protocol round=12; respawning`.
- (b) `.ufo/state/protocol.round` = 13 (advanced past 12 since; at the row's `closed_at` 20:55:00 it
  was 12 — the counter is not the status's basis, the complete line is).
- (c) `.ufo/reports/round-12/protocol.md`, 39404 B, **tracked**, added by
  `62fdfbed93d7a48837554b6a4db3669f057d63f5` (protocol-shokunin <protocol@shokunin.local>
  2026-09-28T21:46:25-03:00) = ancestor of `HEAD`; file mtime 21:45:57 precedes that commit, so
  lands-last holds.
- (d) `SHONEN` = **1**.
- (e) 28 hex tokens: **25 resolve as commits** — main repo 16 (`392b3c7 3ea42cb 46e9ec3 6d27283
  50b2179 7c56d1e 98735cc a5d6a7e c41e197 cab25dd d1e3903 dddb4ec df1b2c6 e0170cd e275d4a f520b03`),
  kengaku-shokunin 2 (`06cdc98 f09ff1f`), kumitate-shokunin 3 (`23452e7 64a27e7 e0e5de1`),
  kotoba-shokunin 4 (`4dd7753 633859f abef8aa d49dfa5`) — **every one an ancestor of that repo's
  `HEAD`**, 0 non-ancestors. The 3 unresolvable tokens are **not commit citations**: `391a54f4`
  (report: "dead blob"), `4028846` ("dead pointer" at line 54), `9b89166c` (mutation base sha256).
- (f) n/a (tracked).
- **Rule for the status:** PROTOCOL §Round-robin, "**Completion evidence** is a
  `.ufo/reports/round-N/<lane>.md` that satisfies the report contract" + "**Termination evidence** is a
  `complete <lane> round=N` line or the lane's counter passing `N`"; the `failed` rule — "`failed`
  covers every lane-round that was prompted or dispatched and has no report by closure" — cannot reach
  a lane-round with a filed, contract-satisfying report.
- **Defects:** none material (the `LANE_HASH`/`{{N}}` strings in it are inside *quoted template text*
  the report is required to carry, not unfilled fields — checked in context at lines 71/73/232/281).

### 2. kake r14 — debt row (entry #27, `in-flight`) → **`ok`**

- (a) `2026-09-28T20:05:46-03:00 launch kake round=14 runId=shokunin-r14-kake-r1790636745`;
  `2026-09-28T21:44:24-03:00 complete kake round=14; respawning`.
- (b) `.ufo/state/kake.round` = 15.
- (c) `.ufo/reports/round-14/kake.md`, 10417 B, **tracked**, added by
  `1dc7f6b81f86606e19d9c6c72f0a336bce4c291f` (2026-09-28T21:42:48-03:00) = ancestor of `HEAD`.
- (d) `SHONEN` = **0** — defect.
- (e) 11 tokens: **1 resolves** — `2a5502c` (kake-shokunin, ancestor) — and it is the **round-13**
  commit (`2026-09-28T20:05:41-03:00`), not this round's. Its own round-14 commit
  `a2094411fe9051ebf3c10929ed33c1b6c032ea39` (`2026-09-28T21:42:41-03:00`, **ancestor, uncited**) is
  never named. The other 10 tokens are digests/foreign beats (`0adbb105 0decd827 1a0de32f 4427b7f8
  93ddca9a a8f1e2b b74190e eddf44e6 fb365e38` are md5/sha fragments; `9c28d29` is a scribe beat in a
  repo not present locally) — none is offered as a fleet commit.
- (f) n/a.
- **Rule:** as row 1 (§Round-robin completion evidence + termination line).
- **Defects (status-neutral, step 1: "this does not change the lane's status unless the round's rules
  already prescribe `failed`"):** (1) no `SHONEN` heading — "a report missing the `SHONEN` heading is a
  conformance defect AND disqualified as evidence in that lane's promotion review"; (2) own round
  commit uncited — "it must cite that commit's hash"; (3) report-before-commit: file mtime 21:42:18
  precedes its own commit by 23 s — "written only after the lane's child-repo work is committed".

### 3. kumitate r13 — debt row (entry #34, `in-flight`) → **`ok`**

- (a) `2026-09-28T21:21:51-03:00 launch kumitate round=13 runId=shokunin-r13-kumitate-r1790641309`;
  `2026-09-28T21:52:02-03:00 complete kumitate round=13; respawning`.
- (b) `.ufo/state/kumitate.round` = 15.
- (c) `.ufo/reports/round-13/kumitate.md`, 16347 B, **tracked**, added by
  `a197445d0b06f463a188d22a28218cd10c302f15` (2026-09-28T21:49:18-03:00) = ancestor of `HEAD`.
- (d) `SHONEN` = **1** (`## SHONEN`).
- (e) 4 tokens, **0 resolve as commits**: `daa371583`/`4f34e7dab` are the *read-only origin tree's*
  HEADs (line 153), `8a6b5c9d`/`a11ead17` are proxy digests (line 137). The report's own citation is a
  **branch name**: line 7 `**Repo commit:** \`round-13\` (lane)` and the tail "**Cited lane commits:**
  the \`round-13\` commit (below)".
- (f) n/a.
- **Rule:** as row 1.
- **Defects (status-neutral):** (1) no resolvable round-work hash citation at all — "it must cite that
  commit's hash" and "The cited hash is the lane repo's `HEAD` when the report is written";
  (2) report-before-commit: file mtime 21:49:01.548 precedes its own kumitate-shokunin commits
  `ed991d072665ad0b0f84a6072c323c8f723ab57c` (21:49:07) and
  `7a099b2b7df98a23f8f443763bec05ee8593403c` (21:49:54).

### 4. kotoba r14 — debt row (entry #35, `in-flight`) → **`ok`** (untracked report; durability debt, re-grade risk)

- (a) `2026-09-28T21:14:16-03:00 launch kotoba round=14 runId=shokunin-r14-kotoba-r1790640851`;
  `2026-09-28T21:36:52-03:00 complete kotoba round=14; respawning`.
- (b) `.ufo/state/kotoba.round` = 15.
- (c) `.ufo/reports/round-14/kotoba.md`, 9463 B, **UNTRACKED** (`git ls-files --error-unmatch` exit 1;
  `git ls-files -o --exclude-standard .ufo/reports` lists it). Adding commit: **none** —
  `git log --diff-filter=A -1 -- .ufo/reports/round-14/kotoba.md` prints *nothing*. mtime
  2026-09-28T21:36:23-03:00.
- (d) `SHONEN` = **0** — defect.
- (e) 1 token: `29c17be` (kotoba-shokunin, 2026-09-28T21:34:51-03:00) resolves and **is an ancestor**
  of kotoba `HEAD` `0f658ff`. It is this round's own commit, so the report is a *report*, not a marker
  (gate `_grade_file` → `marker False`, 9463 B).
- (f) **Orphaned-report order applied, successor-first:** "An orphaned report is resolved in order: the
  lane's own respawn inherits and lands it; the integrator sweeps it for durability only if that
  successor mission also terminates without landing it, and records the attribution defect". kotoba's
  successor mission is live at `closed_at` — `2026-09-28T21:36:53-03:00 launch kotoba round=15
  runId=shokunin-r15-kotoba-r1790642212` — so the **sweep precondition is unmet and this pass must NOT
  sweep it** (sweeping now would also freeze it under the wrong identity). **Re-grade condition:** "A
  terminated lane-round whose report exists on disk but is unlanded is recorded on its termination
  evidence with the durability debt named, and the next pass re-grades it `failed` for want of a landed
  report if the successor never lands it." **Grade that follows: `ok` now** (recorded on the complete
  line at 21:36:52, durability debt named); **`failed` at the next pass** if kotoba r15 terminates
  without landing it.
- **Rule:** the re-grade/durability sentence quoted in (f). Attribution defect also recorded: "a lane
  whose report is still uncommitted when its mission completes has not satisfied this clause".

### 5. kagi r13 — debt row (entry #29, `in-flight`) → **`ok`**

- (a) `2026-09-28T21:06:34-03:00 launch kagi round=13 runId=shokunin-r13-kagi-r1790640365`;
  `2026-09-28T21:52:08-03:00 complete kagi round=13; respawning`.
- (b) `.ufo/state/kagi.round` = 15.
- (c) `.ufo/reports/round-13/kagi.md`, 9441 B, **tracked**, added by
  `383ea1ac252ee4b1a9ed6700eb6aa981a3992d8b` (2026-09-28T21:51:23-03:00) = ancestor of `HEAD`.
- (d) `SHONEN` = **0** — defect.
- (e) 3 tokens: `4b8c0183bd57ec5d0033fd07f650e116d7e9f600` resolves in kagi-shokunin and **is an
  ancestor** of kagi `HEAD` `baec94f` (it was `HEAD` when the report was written: report line 3 "commit
  **`4b8c018`** (pushed)"); `4391b3b` (line 4, the HEAD *at open*) also resolves and is an ancestor;
  `deadbeef` (line 102) is the **fixture path** ``deadbeef/0/0``, not a citation — recorded here so no
  false accusation is made. Report mtime 21:51:17.703 follows `4b8c018` (21:50:42) → lands-last holds.
- (f) n/a.
- **Rule:** as row 1.
- **Defects (status-neutral):** missing `SHONEN` heading.

### 6. aggregator r9 — live `in-flight` (entry #31) → **`in-flight`** (re-confirmed)

- (a) `2026-09-28T21:14:10-03:00 launch aggregator round=9 runId=shokunin-r9-aggregator-r1790640845`;
  **no** termination line (`grep -c 'complete aggregator round=9' .ufo/watchdog.log` → **0**).
- (b) `.ufo/state/aggregator.round` = 9; mission file `.ufo/state/aggregator.mission` =
  `shokunin-r9-aggregator-r1790640845`.
- (c) no report: `ls .ufo/reports/round-9/aggregator.md` → `No such file or directory`; the round-9
  contract-path sweep shows `kagi kake kasegi kengaku kotoba kumitate protocol` only — no
  non-conforming alias either.
- (d)–(e) n/a (no report).
- (f) n/a.
- **Rule:** §Round-robin "no lane may be recorded `in-flight` unless its mission was live at
  `closed_at`" + "`in-flight` is therefore decided from the absence of both a `complete <lane> round=N`
  line and a *landed* report".
- **Activity (progressing, lane-authored):** six `aggregator-shokunin` commits in the child repos after
  the launch — kagi `baec94f`, kake `4214101`, kasegi `b021dc9`, kengaku `e171cdf`, kotoba `0f658ff`,
  kumitate `93b0567`, all 22:19:05–22:19:06 (`git -C <r>-shokunin log --since=2026-09-28T21:14:10-03:00
  --author=aggregator`) — plus its own ledger `.ufo/reports/AGGREGATE.md` dirty with **410 uncommitted
  insertions** (`git diff --stat` → `1 file changed, 410 insertions(+)`), the §14 "Refresh 7 — round-9
  aggregator audit" section. Those uncommitted bytes are **reported, not lane debt**: "uncommitted
  aggregator-owned files are reported, not lane debt".
- **Defect to route:** the ledger §14 asserts "Wave evidence is **committed** under
  `.ufo/waves/round-9/`" while `git ls-files .ufo/waves/round-9` → **0 tracked files** (see durability
  list). The claim as written is false.

### 7. kengaku r12 — live `in-flight` (entry #33) → **`in-flight`** (re-confirmed)

- (a) `2026-09-28T21:21:48-03:00 launch kengaku round=12 runId=shokunin-r12-kengaku-r1790641306`; no
  termination line (`grep -c 'complete kengaku round=12'` → **0**).
- (b) `.ufo/state/kengaku.round` = 12.
- (c) no report: `ls .ufo/reports/round-12/kengaku.md` → `No such file or directory`.
- (d)–(f) n/a.
- **Rule:** as row 6.
- **Activity:** 32 files newer than the launch under `kengaku-shokunin`
  (`find kengaku-shokunin -newermt 2026-09-28T21:21:48-03:00 -type f -not -path '*/.git/*'`), but the
  **only commit** in that window is aggregator-authored (`e171cdf`, aggregator-shokunin, 22:19:06) —
  and "A commit authored by *another* lane is not the subject lane's activity — the aggregator writes
  into every child repo". So the lane half of the activity is the two **untracked** evidence dirs
  `corpus/evidence/round12-fleet/` and `corpus/evidence/round12-ladder/` (32 files, `git status` → `??`
  both) → graded **progressing**, with the caveat that if those files turn out to be aggregator-authored
  the row degrades to `progressing-weak` (a third grade: "named as such in the row, never called
  progressing, and never silent or `failed` on its own").
- **Defect:** uncommitted lane work in its own repo — "changes that exist only in a working tree do not
  count for the round".

### 8. protocol r13 — `pending_round` (entry #21's `not-dispatched`, `lane_rounds` 11) → **`in-flight`**

- (a) `2026-09-28T21:52:01-03:00 launch protocol round=13 runId=shokunin-r13-protocol-r1790643117`; no
  termination line (`grep -c 'complete protocol round=13'` → **0**).
- (b) `.ufo/state/protocol.round` = 13; mission `shokunin-r13-protocol-r1790643117`.
- (c) no report: `ls .ufo/reports/round-13/protocol.md` → `No such file or directory`.
- (d)–(f) n/a.
- **Rule:** as row 6, plus the ride rule — "A lane dispatched for its Nth round *after* round `N` closed
  rides the next closure-correction for `N` — never dropped, never folded into `N+1`" (round 13 closed
  at 21:30:00 in entry #34; this dispatch is 22 min later). The old `not-dispatched` row in entry #21
  was true at its own `closed_at` 20:10:00 and is now falsified by dispatch evidence — "No lane may be
  recorded `not-dispatched` while dispatch evidence for that lane-round exists" — so it is superseded,
  not contradicted.
- **Activity:** progressing — this pass's own seats/instruments under `.ufo/waves/round-13/`
  (81 untracked files, mtimes after the launch).

### 9. kumitate r14 — `pending_round` (entry #27's `not-dispatched`, `lane_rounds` 12) → **`ok`**

- (a) `2026-09-28T21:52:06-03:00 launch kumitate round=14 runId=shokunin-r14-kumitate-r1790643122`;
  `2026-09-28T22:22:15-03:00 complete kumitate round=14; respawning` (landed inside this sweep) and
  `2026-09-28T22:22:17-03:00 launch kumitate round=15 runId=shokunin-r15-kumitate-r1790644935`.
- (b) `.ufo/state/kumitate.round` = 15.
- (c) `.ufo/reports/round-14/kumitate.md`, 9116 B, **tracked**, added by `5fa216c` (2026-09-28T22:19:00-03:00)
  = ancestor of `HEAD`; **appended** by `3d20676` (2026-09-28T22:20:09-03:00, `+16 lines`) — a
  conforming erratum ("as an erratum appended after the filed bytes in a new commit and naming the text
  it supersedes"), not a rewrite of the filed bytes.
- (d) `SHONEN` = **1**.
- (e) 5 tokens: `93b0567` + `dffbf0e` (kumitate-shokunin) and `5fa216c` (main repo) all resolve and are
  **ancestors** of their repo's `HEAD`; `4f34e7dab`/`f65ee4b3d` are digest fragments.
- (f) n/a (tracked).
- **Rule:** §Round-robin "`in-flight` is therefore decided from the absence of both a `complete <lane>
  round=N` line and a *landed* report" — a complete line **and** a landed report are both present, so
  the row is terminal, and the contract-satisfying report makes it `ok` (completion-evidence rule).
- **Defects:** none material. The adding commit's author (`Joao Pedro Veiga <jpveigao10@gmail.com>`)
  equals kumitate-shokunin's own configured `user.name`/`user.email` (`git -C kumitate-shokunin config
  user.email`), so no attribution defect is determinable — but note the main repo carries the **same**
  identity string, so author alone cannot distinguish a lane landing from an operator sweep.

### 10. kagi r14 — `pending_round` (entry #27's `not-dispatched`, `lane_rounds` 12) → **`ok`**

- (a) `2026-09-28T21:52:12-03:00 launch kagi round=14 runId=shokunin-r14-kagi-r1790643128`;
  `2026-09-28T22:22:18-03:00 complete kagi round=14; respawning`; then
  `2026-09-28T22:22:19-03:00 launch kagi round=15 runId=shokunin-r15-kagi-r1790644938`.
- (b) `.ufo/state/kagi.round` = 15.
- (c) `.ufo/reports/round-14/kagi.md`, 15271 B, **UNTRACKED** (`git ls-files --error-unmatch` exit 1;
  listed by `git ls-files -o --exclude-standard .ufo/reports`); adding commit **none**
  (`git log --diff-filter=A -1 -- .ufo/reports/round-14/kagi.md` prints nothing). mtime
  2026-09-28T22:21:02-03:00.
- (d) `SHONEN` = **0** — defect.
- (e) 2 tokens: `4b8c018` (kagi-shokunin, ancestor of `HEAD` `baec94f`) — the **round-13** commit —
  plus the same `deadbeef` fixture literal. No kagi-authored round-14 commit exists:
  `git -C kagi-shokunin log --since=2026-09-28T21:52:12-03:00` returns only the aggregator's
  `baec94f` (22:19:06). Gate `_grade_file` → `marker False` (it names a resolvable hash).
- (f) **Orphan order, successor-first:** the lane's own respawn is live at `closed_at`
  (`2026-09-28T22:22:19-03:00 launch kagi round=15 …`) and inherits it; the integrator sweeps "only if
  that successor mission also terminates without landing it" — precondition unmet, **no sweep this
  pass**. **Re-grade condition:** next pass re-grades it `failed` "for want of a landed report if the
  successor never lands it". **Grade that follows: `ok` now, `failed` at the next pass if kagi r15 never
  lands it.**
- Note the timing that decides this row: at 22:21:02 the file existed but was unlanded and there was no
  complete line, so under "an uncommitted file at the report path does not end `in-flight`, however it
  fires the driver's existence signal" the row was `in-flight`; the complete line at 22:22:18 (≤
  `closed_at`) moved it to its termination evidence, which is why the row shipped here is `ok`, not
  `in-flight`. A row written from the 22:21 state would have been flagged `stale_in_flight` by the gate
  the moment the log grew.
- **Defects:** unlanded at completion (durability + attribution), missing `SHONEN` heading, no round-14
  work hash cited (if filed as-is).

### 11. kasegi r15 — `pending_round` (no row anywhere) → **`ok`** (drives the round-15 entry)

- (a) `2026-09-28T20:50:55-03:00 launch kasegi round=15 runId=shokunin-r15-kasegi-r1790639453`;
  `2026-09-28T22:14:43-03:00 complete kasegi round=15; respawning`; counter moved to 16 by
  `2026-09-28T22:14:45-03:00 launch kasegi round=16 runId=shokunin-r16-kasegi-r1790644483`.
- (b) `.ufo/state/kasegi.round` = 16.
- (c) `.ufo/reports/round-15/kasegi.md`, 15865 B, **tracked**, added by
  `f3cbdcf92a6136d2d16be9fcfd9157644ee0dd0e` (2026-09-28T22:09:29-03:00) = ancestor of `HEAD`; mtime
  22:08:22 follows its own lane commit `eb5b590` (kasegi-shokunin, 22:06:22) → lands-last holds.
- (d) `SHONEN` = **0** — defect.
- (e) 7 tokens: `eb5b590` (its own round-15 lane commit), `7483333`, `fc6d398` all resolve in
  kasegi-shokunin and are **ancestors** of its `HEAD` (`b021dc9`); `1307b8b`, `1cfbd86`, `37c3668` are
  HEADs of **non-fleet** repos the report names by path (`~/Projects/origin-work/open-bug-bounties`,
  `~/Projects/the-bounty-hunter`) — unverifiable from this read-only vantage; `ba5485ed6a5d` is a file
  sha prefix.
- (f) n/a.
- **Rule:** §Round-robin completion evidence + termination line; and "Write the entry for round `N` as
  soon as one lane's Nth lane-round terminates" — this row is the trigger for the round-15 entry.
- **Defects:** missing `SHONEN` heading (status-neutral).

### 12. kake r15 — `pending_round` (no row) → **`in-flight`** + `progressing-weak` named

- (a) `2026-09-28T21:44:25-03:00 launch kake round=15 runId=shokunin-r15-kake-r1790642664`; no
  termination line (`grep -c 'complete kake round=15'` → **0**).
- (b) `.ufo/state/kake.round` = 15.
- (c) no report: `ls .ufo/reports/round-15/kake.md` → `No such file or directory`.
- (d)–(f) n/a.
- **Rule:** as row 6 for `in-flight`. Activity grade: **progressing-weak** — zero lane-authored commits
  in the window and exactly one newer file,
  `kake-shokunin/corpus/lessons/round-9-aggregator-corpus-verdict.md`, written by the aggregator's
  `4214101` (22:19:06); "sibling-authored activity alone is a third grade, `progressing-weak`: named as
  such in the row, never called progressing, and never silent or `failed` on its own". At 22:17 the same
  probe read **silent** (`find -newermt` → 0 files, `git log --since` → 0 commits), and the mission is
  past the stale-lane trigger (>2 driver ticks: ticks 33–37) — so this row carries the stale-lane flag
  for the integrator's review, with the discretionary route named: "the integrator **may** record it
  `failed` so the driver respawns it on a fresh prompt", and "The integrator-of-record records `failed`
  only for silent missions and flags progressing ones in the round notes". **Not taken here**: the
  mission is live at `closed_at`, is not silent under the current probe, and "recording `failed` is a
  ledger act, not a kill" — a `failed` row for a live lane-round is the integrator's call on review, not
  this sweep's recommendation.

### 13. kotoba r15 — `pending_round` (no row) → **`in-flight`**

- (a) `2026-09-28T21:36:53-03:00 launch kotoba round=15 runId=shokunin-r15-kotoba-r1790642212`; no
  termination line (`grep -c 'complete kotoba round=15'` → **0**).
- (b) `.ufo/state/kotoba.round` = 15.
- (c) no report: `ls .ufo/reports/round-15/kotoba.md` → `No such file or directory`.
- (d)–(f) n/a.
- **Rule:** as row 6. **Activity:** progressing — lane-authored commit
  `63ceba7a0f73f7a576230c54aa164886ecbe7c47` (kotoba-shokunin identity, 21:44:36) and 90 files newer
  than the launch; the window's second commit (`0f658ff`, 22:19:06) is aggregator-authored and excluded
  by that rule.

### Beyond the 13: the other round-15 rows (kumitate r15, kagi r15, kasegi r16)

These are not in the 13 the brief names, but the round-15 `closure` entry must describe every round-15
lane-round — "a terminal status for every `N` lane-round that has terminated, `in-flight` for lanes
dispatched and still open, `not-dispatched` for lanes with no dispatch evidence **as of `closed_at`**" —
so their evidence is recorded here.

- **kumitate r15 → `in-flight`.** `2026-09-28T22:22:17-03:00 launch kumitate round=15
  runId=shokunin-r15-kumitate-r1790644935`; `grep -c 'complete kumitate round=15'` → **0**;
  `.ufo/state/kumitate.round` = 15; no report (`ls .ufo/reports/round-15/kumitate.md` → `No such file or
  directory`). Rule: as row 6. (Dispatched 39 s after round 14 closed → it will ride a round-15
  correction if it does not terminate before the next pass.)
- **kagi r15 → `in-flight`.** `2026-09-28T22:22:19-03:00 launch kagi round=15
  runId=shokunin-r15-kagi-r1790644938`; `grep -c 'complete kagi round=15'` → **0**; counter 15; no
  report. Same rule.
- **protocol r15 / aggregator r15 / kengaku r15 → `not-dispatched` (with `lane_rounds` 13 / 9 / 12).**
  `grep -nE 'launch (protocol|aggregator|kengaku) round=15' .ufo/watchdog.log` → **no match**; their
  counters are behind 15 (13 / 9 / 12), so at `closed_at` no dispatch evidence exists for those
  lane-rounds. Rule: "`not-dispatched` for lanes with no dispatch evidence **as of `closed_at`** — so
  `closed_at` is required on any entry carrying a `not-dispatched` row" and "required on every
  `not-dispatched` row — the counter the lane actually held is what makes such a row falsifiable".
- **kasegi r16 → no row.** `2026-09-28T22:14:45-03:00 launch kasegi round=16
  runId=shokunin-r16-kasegi-r1790644483`, live, no report, no row anywhere. Per the task's rule this
  sweep writes no entry for it: PROTOCOL triggers an entry when "one lane's Nth lane-round terminates"
  and none has for round 16 — it is `pending_round` informational ("round 16 has no entry yet ->
  informational (partial-entries rule)") and rides the closure-correction for 16 once one terminates.
  Flagged so the next pass does not rediscover it.

## Recommended statuses and the entries they imply

| lane-round | status | rule (PROTOCOL §Round-robin) | defects recorded (status-neutral unless noted) |
|---|---|---|---|
| protocol r12 | `ok` | completion evidence + termination line | none material |
| kake r14 | `ok` | idem | no `SHONEN`; own commit `a209441` uncited; report-before-own-commit (23 s) |
| kumitate r13 | `ok` | idem | no hash citation (branch name only); report-before-own-commit (6 s / 53 s) |
| kotoba r14 | `ok` | terminated-unlanded report recorded on its termination evidence + re-grade | `SHONEN`=0; unlanded (durability + attribution); next pass → `failed` if kotoba r15 never lands it |
| kagi r13 | `ok` | completion evidence + termination line | `SHONEN`=0 |
| kumitate r14 | `ok` | landed report ends `in-flight`; termination line present | none material |
| kagi r14 | `ok` | terminated-unlanded report + re-grade | `SHONEN`=0; unlanded; no round-14 hash cited; next pass → `failed` if kagi r15 never lands it |
| kasegi r15 | `ok` | completion evidence + termination line (drives the round-15 entry) | `SHONEN`=0 |
| aggregator r9 | `in-flight` | live at `closed_at`; no complete line and no landed report | ledger §14 claims round-9 wave evidence is committed while it is untracked |
| kengaku r12 | `in-flight` | idem | 32 files of lane work uncommitted; activity partly sibling-authored (progressing-weak caveat) |
| protocol r13 | `in-flight` | idem + rides the next closure-correction for 13 | supersedes entry #21's now-falsified `not-dispatched` |
| kake r15 | `in-flight` | idem | `progressing-weak` named; stale-lane review flag; optional `failed` route named |
| kotoba r15 | `in-flight` | idem | none |
| kumitate r15 | `in-flight` | idem (dispatched 22:22:17, live) | none |
| kagi r15 | `in-flight` | idem (dispatched 22:22:19, live) | none |
| protocol r15 / aggregator r15 / kengaku r15 | `not-dispatched` (`lane_rounds` 13 / 9 / 12) | "no dispatch evidence **as of `closed_at`**"; counters behind 15 | none (counters falsify the rows if they move) |
| kasegi r16 | (no row) | entry trigger not met for round 16 | informational |

Nobody is recorded `not-dispatched` while dispatch evidence exists, and nobody is `failed`: every
`failed`-class rule is reached only by a lane-round with no report at closure or a silent mission, and
none of these is either.

`round13-entries.json` carries exactly this set: **10 `closure-correction` entries** (one per superseded
row: protocol r12, kake r14, kumitate r13, kotoba r14, kagi r13, kumitate r14, kagi r14 — debt; plus the
`in-flight` re-confirmations aggregator r9, kengaku r12 and protocol r13) and **one `closure` entry for
round 15**, all with `closed_at` `2026-09-28T22:23:00-03:00` and with `supersedes.entry` present wherever
the target's `(round, type, date)` triple is not unique — the triple alone would be ambiguous for
entries #25, #29, #31, #33 and #34 (e.g. `(12, closure-correction, 2026-09-28)` matches #25, #28 and
#33). The round-15 entry carries `lane_rounds` for its three `not-dispatched` rows (protocol 13,
aggregator 9, kengaku 12).

## Verification — the appends re-run through the committed gate

The round-12 gate was executed against a copy of the live inputs **with these 11 entries appended**
(nothing on disk was mutated; the harness imported `.ufo/waves/round-12/closure-check.py` and extended
`inp.entries`):

```
$ python3 /tmp/sim.py
POST-APPEND: closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=1
counts: {'debt': 0, 'contradictions': 0, 'unrowed_terminated': 0, 'prompt_orphan': 0,
 'stale_in_flight': 0, 'unrowed': 1, 'live_in_flight': 7, 'pending_round': 1, 'by_class': {}}
  [pending_round/pending_round] kasegi r16 :: dispatched `2026-09-28T22:14:45-03:00 launch kasegi
  round=16 runId=shokunin-r16-kasegi-r1790644483` and no row written; round 16 has no entry yet
  -> informational (partial-entries rule, P:209-213)
  live_in_flight: protocol r13, aggregator r9, kengaku r12, kake r15, kumitate r15, kotoba r15, kagi r15
EXIT: 0
```

Before the append the same gate read `debt debt=7 contradictions=0 unrowed_terminated=2
pending_round=5` (`python3 .ufo/waves/round-12/closure-check.py --no-citations`, exit 1). So every
status in the JSON reproduces under the committed checker: **`ok / debt=0 / contradictions=0`, exit 0**,
with the single remaining informational row being kasegi r16.

Marker grades for the eight reports in the band (gate `_grade_file`, live mode):

```
.ufo/reports/round-12/protocol.md  39404 B  marker False  SHONEN True
.ufo/reports/round-13/kumitate.md  16347 B  marker False  SHONEN True
.ufo/reports/round-13/kagi.md       9441 B  marker False  SHONEN False
.ufo/reports/round-14/kake.md      10417 B  marker False  SHONEN False
.ufo/reports/round-14/kumitate.md   9116 B  marker False  SHONEN True
.ufo/reports/round-14/kotoba.md     9463 B  marker False  SHONEN False   (untracked)
.ufo/reports/round-14/kagi.md      15271 B  marker False  SHONEN False   (untracked)
.ufo/reports/round-15/kasegi.md    15865 B  marker False  SHONEN False
```

**Consequence the next pass must know:** once these rows are `ok`, the gate's *unlanded-report* section
no longer fires for kotoba r14 or kagi r14 (it only fires under an `in-flight` row), so the durability
debt for those two files lives **only** in these notes and in the round-13 protocol report. It will not
appear as an exit-1 driver again.

## Durability duty (untracked files that owe a commit)

**(a) The five untracked `.ufo/prompts/*.md`** — `git ls-files -o --exclude-standard .ufo/prompts`:

| prompt | bytes | mtime | dispatch line present? |
|---|---|---|---|
| `.ufo/prompts/protocol-round-13.md` | 1299 | 21:51:57 | yes — `launch protocol round=13 … r1790643117` 21:52:01 |
| `.ufo/prompts/kumitate-round-14.md` | 1335 | 21:52:02 | yes — `launch kumitate round=14 … r1790643122` 21:52:06 |
| `.ufo/prompts/kagi-round-14.md` | 1316 | 21:52:08 | yes — `launch kagi round=14 … r1790643128` 21:52:12 |
| `.ufo/prompts/kotoba-round-15.md` | 1321 | 21:36:52 | yes — `launch kotoba round=15 … r1790642212` 21:36:53 |
| `.ufo/prompts/kake-round-15.md` | 1313 | 21:44:24 | yes — `launch kake round=15 … r1790642664` 21:44:25 |

None is a **prompt orphan** (every one is corroborated by a dispatch line, and the gate's
`prompt_orphan` count is 0), so none "records `failed`". They are durability debt: the prompt "must be
committed to be durable", and the integrator commits already-generated `.ufo/prompts/*.md` for exactly
this reason.

**(b) Every untracked report on disk** — census `find .ufo/reports -name '*.md' -type f | wc -l` → **94**;
`git ls-files .ufo/reports | wc -l` → **90**; the four untracked ones (`git ls-files -o --exclude-standard
.ufo/reports`):

| report | bytes | owed |
|---|---|---|
| `.ufo/reports/round-12/kotoba.md` | 14009 | successors kotoba r13 (20:28:23→21:14:11) and r14 (21:14:16→21:36:52) both terminated without landing it → the sweep precondition of the orphan order **is now met** for this file (integrator may sweep for durability, recording the attribution defect); if kotoba r15 also terminates without landing it, the re-grade condition applies. It also carries the literal `LANE_HASH` placeholder at line 224 — a reason prior passes refused to sweep it. |
| `.ufo/reports/round-12/kagi.md` | 13620 | successor kagi r13 terminated 21:52:08 without landing it → sweep precondition met for this file too (SHONEN=0, cites only aggregator commits). |
| `.ufo/reports/round-14/kotoba.md` | 9463 | kotoba r15 live at `closed_at` → successor-first, **do not sweep**; `ok` row + durability debt; `failed` next pass if never landed. |
| `.ufo/reports/round-14/kagi.md` | 15271 | kagi r15 live at `closed_at` → successor-first, **do not sweep**; `ok` row + durability debt; `failed` next pass if never landed. |

**(c) `.ufo/waves/round-9/` — untracked evidence someone owes.** `git ls-files .ufo/waves/round-9` → **0**
files tracked; **25 files on disk, 356 K** (`find .ufo/waves/round-9 -type f | wc -l` → 25;
`git ls-files -o --exclude-standard .ufo/waves/round-9 | wc -l` → 25): 15 files under `seats/` (the 15th,
`seats/connector.md`, landed during this sweep), 6 under `lessons/`, plus `CONTEXT.md`, `l1-baseline.md`,
`corpus-gate.mjs`, `corpus-gate.expected.json`. **Yes, this is untracked evidence someone owes** — the round-9 wave's
closure-gate artifacts are integrator-scope ("committing the round's closure-gate artifacts under
`.ufo/waves/round-<N>/`"), round 9 was closed long ago (entries #12/#17, `closed_at` 20:10:00), and the
aggregator's own ledger §14 asserts the opposite ("Wave evidence is **committed** under
`.ufo/waves/round-9/`"). The owning lane is the **round-9 protocol lane (integrator)**; the aggregator
owes the §14 claim correction. Note `.ufo/waves/round-9/corpus-gate.expected.json` is what the live gate
currently reports as the protocol r13 mission's activity file, so the directory is also load-bearing
evidence for a *live* row.

Not in scope and left untouched: `.ufo/state/*` and `.ufo/watchdog.log` are tracked-but-always-dirty
(operator-side); `.ufo/waves/round-13/` is this pass's own working set (81 untracked files, integrator
commits at closure).

## Gaps / unknowns

- **`supersedes` uniqueness after this pass.** Four of the 11 new entries share `(14, closure-correction,
  2026-09-28)` and two share `(12, closure-correction, 2026-09-28)`; a later correction naming any of them
  will itself need `supersedes.entry`. The gate accepts an explicit `entry` index whose round/type agree
  (`_supersedes_findings`), and all 11 of mine name their target that way.
- **`deadbeef` in kagi r13 and r14 reports** is a fixture path, not a citation (checked in context); if a
  future citation sweep classifies it as a placeholder it will produce a false defect.
- **Foreign-repo hashes** in `.ufo/reports/round-14/kake.md` (`9c28d29` scribe beat) and
  `.ufo/reports/round-15/kasegi.md` (`1307b8b`, `1cfbd86`, `37c3668`) are unresolvable in this repo and in
  all six child repos; whether they exist in the repos the reports name is unknowable read-only (no fetch).
- **Live-mission grades are probes, not verdicts.** The aggregator r9 / kengaku r12 / protocol r13 /
  kumitate r15 / kagi r15 / kake r15 / kotoba r15 rows are `in-flight` by the absence rule; whether each
  is genuinely progressing is measured only to the extent recorded above, and the gate's own stale-mission
  probe is explicitly "an activity probe, not a verdict".
- **Timing.** The log grew three times inside this sweep (236 → 239 → 243 lines) and two round-14 rows
  changed terminal status mid-write (tick=37). Rows written from an earlier read would already be stale;
  the shipped rows are the ones that hold at `closed_at` `2026-09-28T22:23:00-03:00`.