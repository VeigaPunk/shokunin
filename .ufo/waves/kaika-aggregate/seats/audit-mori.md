# audit-mori — mori-shokunin at bf7cdc4 (aggregator round 12, seat AuditMori)

Scope: `/home/vgpnk/Projects/shokunin/mori-shokunin` only, read-only. Gate: existing
`corpus-gate-v1` at `.ufo/waves/round-9/corpus-gate.mjs` (sha256
`e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3`, 53 103 bytes), invoked in
`--snapshot` mode. No lane write; no build/test/lint; no census baseline published (nothing here
freezes census totals; any census figure quoted below is the lane's own committed claim, not a
re-measurement by this seat).

## 1. Revision and working tree

```
$ git -C /home/vgpnk/Projects/shokunin/mori-shokunin rev-parse HEAD
bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a
$ git -C /home/vgpnk/Projects/shokunin/mori-shokunin status --porcelain
(no output)          # exit 0 — worktree == HEAD for every tracked byte
```

`git -C … log --format='%h %ad %an <%ae> %s' -- corpus/` head: `bf7cdc4 protocol-shokunin
<protocol@shokunin.local> round-12 verifier spot-check (integrator, kaika) …`; the only non-lane
author in the whole history (40 commits `mori-shokunin`, 1 commit `protocol-shokunin`).

## 2. Gate run — verdict

Round derivation: committed `LOG.md` at this HEAD carries `## 2026-10-19 — round 12: named
corrections owed since round 11` (:542), `## Round 12 — kaika campaign: …` (:643) and `## Round 12 —
post-review corrections` (:705), and `corpus/lessons/round-12.md` is committed. The lane round is
therefore **12**; selector `--round 12`. The gate default (`--round 9`) was also run for
completeness. Both runs produced the identical r4/r8 finding sets and **exit 1**; only the r10
filename in the finding text differs (`round-9-aggregator-*` vs `round-12-aggregator-*`).

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/mori-shokunin bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a --round 12
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=12
# expect mori-shokunin@bf7cdc4 ABSENT (no committed expected verdict for this revision)
# tree mori-shokunin revision=bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a dirty=0 mode=snapshot
…
# verdict mori-shokunin failed findings=41 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

**Verdict: `not conformant` at `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a`** — according to gate exit
1 only. Failed rule IDs: **r4 (39 findings), r8 (1), r10 (1)**. r2, r7 and shonen produced zero
findings (r2 is filename-keyed, see §6).

Exact finding lines, verbatim from the `--round 12` run (r4/r8 text identical under `--round 9`):

```
CR-mori-shokunin-r4-1: README.md:93 count claim with no backticked command: "stay named.** The 28 cases run in a seeded-shuffled order" (CORPUS.md:28)
CR-mori-shokunin-r4-2: README.md:148 count claim with no backticked command: "re-pin additive-only — 8 inserted lines, 0 deletions, 28 ids" (CORPUS.md:28)
CR-mori-shokunin-r4-3: README.md:300 count claim with no backticked command: "## Known gaps — round-12 note" (CORPUS.md:28)
CR-mori-shokunin-r4-4: knowledge/audit-r11.md:41 count claim with no backticked command: "The evidence tree contains 56 files. The receipt-integrity a" (CORPUS.md:28)
CR-mori-shokunin-r4-5: knowledge/drift-pin-r10.md:106 count claim with no backticked command: "the lessons-distiller's independent 72 s pair measured 6 of " (CORPUS.md:28)
CR-mori-shokunin-r4-6: knowledge/observability-surfaces-r2.md:380 count claim with no backticked command: "Fixed by this note; the two round-1 files remain the parent'" (CORPUS.md:28)
CR-mori-shokunin-r4-7: knowledge/progressing-weak-r2.md:3 count claim with no backticked command: "lane: mori-shokunin · seat: authorship-proof (round-2 flash " (CORPUS.md:28)
CR-mori-shokunin-r4-8: knowledge/progressing-weak-r2.md:36 count claim with no backticked command: "candidate completes all 27 cases but the tally is not passin" (CORPUS.md:28)
CR-mori-shokunin-r4-9: knowledge/progressing-weak-r2.md:235 count claim with no backticked command: "clock). On the 15:39Z bytes the candidate completes all 27 c" (CORPUS.md:28)
CR-mori-shokunin-r4-10: knowledge/selftest-flake-r9.md:65 count claim with no backticked command: "### 1b. The real cases, replayed (all 56 case payloads × the" (CORPUS.md:28)
CR-mori-shokunin-r4-11: knowledge/selftest-flake-r9.md:109 count claim with no backticked command: "is **10/10 PASS, 0 false-FAILs** (560 case-verdicts); the di" (CORPUS.md:28)
CR-mori-shokunin-r4-12: knowledge/selftest-flake-r9.md:152 count claim with no backticked command: "the harness's assertion idiom since 2026-10-14, and r8's +11" (CORPUS.md:28)
CR-mori-shokunin-r4-13: knowledge/selftest-flake-r9.md:254 count claim with no backticked command: "not constants; my pre-fix run-level battery (10 runs) and th" (CORPUS.md:28)
CR-mori-shokunin-r4-14: knowledge/silence-cutover-r3.md:3 count claim with no backticked command: "seat: **cutover-note-writer** (round-3 flash wave, 32 seats)" (CORPUS.md:28)
CR-mori-shokunin-r4-15: knowledge/silence-cutover-r3.md:119 count claim with no backticked command: "## 4. Selftest: 14 → 25 cases (11 new + 1 reworked), all pas" (CORPUS.md:28)
CR-mori-shokunin-r4-16: knowledge/silence-grading-r2.md:3 count claim with no backticked command: "seat: **silence-rules** (round-2 flash wave, 13 seats) · lan" (CORPUS.md:28)
CR-mori-shokunin-r4-17: knowledge/silence-grading-r2.md:145 count claim with no backticked command: "- The verbatim pair match closes measured traps in the fleet" (CORPUS.md:28)
CR-mori-shokunin-r4-18: knowledge/surfaces-r7.md:197 count claim with no backticked command: "| grade tuples, run1 vs run2 sorted | identical across shuff" (CORPUS.md:28)
CR-mori-shokunin-r4-19: knowledge/surfaces-r7.md:259 count claim with no backticked command: "- The r2 note's own Gaps sections and the round-1 files' six" (CORPUS.md:28)
CR-mori-shokunin-r4-20: knowledge/surfaces-r7.md:273 count claim with no backticked command: "(byte-unchanged from r7 — no re-baseline required; the 28 ca" (CORPUS.md:28)
CR-mori-shokunin-r4-21: knowledge/surfaces-r7.md:276 count claim with no backticked command: "(7 files; the oracle receipt's set-close check re-verifies b" (CORPUS.md:28)
CR-mori-shokunin-r4-22: knowledge/surfaces-r8.md:7 count claim with no backticked command: "(1090 lines, **byte-unchanged from r7** — no re-baseline was" (CORPUS.md:28)
CR-mori-shokunin-r4-23: knowledge/surfaces-r8.md:158 count claim with no backticked command: "state_cmp=21 state_val_unreadable=0 state_val_unread_reasons" (CORPUS.md:28)
CR-mori-shokunin-r4-24: knowledge/verdict-machine-r4.md:241 count claim with no backticked command: "verdicts / 1 line; AFTER rc 0 / 1 verdict / 10 lines, same d" (CORPUS.md:28)
CR-mori-shokunin-r4-25: knowledge/verdict-machine-r4.md:323 count claim with no backticked command: "- **Regression: none measured.** All 25 probes that passed a" (CORPUS.md:28)
CR-mori-shokunin-r4-26: knowledge/verdict-machine-r5.md:29 count claim with no backticked command: "The round-4 oracle ran its 28 cases at source level in regis" (CORPUS.md:28)
CR-mori-shokunin-r4-27: knowledge/verdict-machine-r5.md:75 count claim with no backticked command: "- The shuffle is Fisher-Yates in place over the 28 ids, driv" (CORPUS.md:28)
CR-mori-shokunin-r4-28: knowledge/verdict-machine-r6.md:61 count claim with no backticked command: "- **Header-after-loop.** The runner executes all 28 cases fi" (CORPUS.md:28)
CR-mori-shokunin-r4-29: lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:160 count claim with no backticked command: "Twelve of the 21 lane ids are outside the 9-lane roster" (CORPUS.md:28)
CR-mori-shokunin-r4-30: lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:163 count claim with no backticked command: "the same file: it reads exactly one lane's value for its row" (CORPUS.md:28)
CR-mori-shokunin-r4-31: lessons/2026-10-15-probe-pricing-dwell-bounds-filter-drop.md:236 count claim with no backticked command: "mode-000 file, a hidden file and a second regular file retur" (CORPUS.md:28)
CR-mori-shokunin-r4-32: lessons/2026-10-15-selftest-grep-sigpipe-race.md:29 count claim with no backticked command: "calls (63 calls for a 2 292-byte payload in the traced rep b" (CORPUS.md:28)
CR-mori-shokunin-r4-33: lessons/2026-10-15-volatile-contract-behavioral-baselines.md:25 count claim with no backticked command: "- A **live** census pair 72 s apart differs on **32 of 33 li" (CORPUS.md:28)
CR-mori-shokunin-r4-34: lessons/2026-10-15-volatile-contract-behavioral-baselines.md:28 count claim with no backticked command: "- A **pinned fixture** run twice is **byte-identical** (raw " (CORPUS.md:28)
CR-mori-shokunin-r4-35: lessons/2026-10-15-volatile-contract-behavioral-baselines.md:172 count claim with no backticked command: "keeps 1 of 33 lines here; a field-level rule keeps 32 and st" (CORPUS.md:28)
CR-mori-shokunin-r4-36: lessons/2026-10-15-volatile-contract-behavioral-baselines.md:180 count claim with no backticked command: "5. **Keep the fast tier small.** Here 6 of 79 fields (~8%) c" (CORPUS.md:28)
CR-mori-shokunin-r4-37: lessons/2026-10-15-volatile-contract-behavioral-baselines.md:198 count claim with no backticked command: "- The implementation of the round-10 pin/drift modes is **no" (CORPUS.md:28)
CR-mori-shokunin-r4-38: lessons/round-12-verifier-spotcheck.md:17 count claim with no backticked command: "ADMITTED after post-review fixes a7f1ecb. Depth improved (SK" (CORPUS.md:28)
CR-mori-shokunin-r4-39: lessons/round-12.md:125 count claim with no backticked command: "| id | URL | accessed | SHA256 prefix | Verbatim quote (≤25 " (CORPUS.md:28)
CR-mori-shokunin-r8-1: credential-class kv-secret occurrences=4 lines=4 files=3 owner=lane at bf7cdc4 literal_shaped=0/4 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[evidence/order-r5-20261015T180431Z-sniffer.log,knowledge/observability-surfaces-r2.md,lessons/2026-10-15-run-order-spoofing-shuffle-nonce-limits.md] first=evidence/order-r5-20261015T180431Z-sniffer.log:296 first4="toke" len=34 (CORPUS.md:43)
CR-mori-shokunin-r10-1: no corpus/lessons/round-12-aggregator-*.md — the round-12 review duty has no emitted lesson (CORPUS.md:21)
# note mori-shokunin r7: 10 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note mori-shokunin r7 under-coverage (not a finding): 67/99 corpus files carry no index row
# note mori-shokunin r8 kv-secret/lane file-list: evidence/order-r5-20261015T180431Z-sniffer.log knowledge/observability-surfaces-r2.md lessons/2026-10-15-run-order-spoofing-shuffle-nonce-limits.md
# note mori-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one's examples")
# note mori-shokunin extracted with: git archive bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a | tar -x -C <tmp>
```

Under `--round 9` the sole difference is `CR-mori-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md
— the round-9 review duty has no emitted lesson`; `# verdict … findings=41 rules=r4,r8,r10`, `EXIT=1`.
The gate printed `# expect mori-shokunin@bf7cdc4 ABSENT` — `corpus-gate.expected.json` `frozen[]`
contains no mori entry (it lists only the six legacy lanes), so the exit-3 drift class cannot apply.

### 2.1 Finding attribution spot-checked against committed bytes

Worktree is clean, so `git show HEAD:<path>` line N equals the graded archive line. All eight
spot-checks reproduce the cited text byte-exactly (`git show HEAD:<f> | awk -v n=N 'NR==n'`):
`README.md:93`, `:148`, `:300`, `lessons/round-12.md:125`, `lessons/round-12-verifier-spotcheck.md:17`,
`knowledge/selftest-flake-r9.md:109`, `lessons/2026-10-15-volatile-contract-behavioral-baselines.md:25`,
`evidence/order-r5-20261015T180431Z-sniffer.log:296`. Re-implementing the r8 `kv-secret` regex over
every `corpus/**` text file at HEAD reproduced **4 occurrences / 3 files** exactly; the values are
`token="nonce-${MORI_RUN_NONCE:-0}"` (schematic), a concrete recorded `token="nonce-<9-digit run
nonce>"` in the committed r5 receipt log (:370), ``token: `results.json` `` (fixture path, knowledge
r2 note :144) and ``token: `assert_case` `` (case id, r5 lesson :108). All four values are
quote/backtick-delimited, matching the gate's `literal_shaped=0/4`. The concrete nonce is the only
value-shaped occurrence; classification stays the gate's declared could-not-evaluate, routed to the
parent. Separately, r4 is line-local: of the 39 r4 findings, **3 are Markdown headings and 2 are
table rows** (r4-3 README:300 `## Known gaps — round-12 note`; r4-10, r4-15 headings; r4-18
surfaces-r7:197 table row; r4-39 round-12.md:125 table header `… (≤25 words)`) — mechanical matches,
not count claims.

## 3. SOURCES.md structural observations (separate from the gate verdict)

Source: `git show HEAD:corpus/SOURCES.md` (sha256
`efe349d580266b8499d783d94b707012639d73173b57e09168a5a9df1d823ab6`, 34 registry rows). The gate
does **not** apply r4 or r7 to `SOURCES.md` (both read `README.md`, `knowledge/**.md`,
`lessons/**.md` only); r8 scans it and reported no hit there. These checks are this seat's, not gate
results.

- IDs: `S001…S034`, 34 rows, ascending, **no duplicates, no gaps**. One row per source; every row
  has 11 columns.
- `kind`: docs 15, code 8, tool 4, spec 3, community 2, book 1, own-work 1. `tier`: A 31, B 2, C 1.
  `status`: mined 12, queued 21, rejected 1 (S030, rejection reason and flip condition present).
- `used-by`: 12 of 34 rows name at least one corpus path; **23 path references, all 23 resolve at
  HEAD** (`git cat-file -e HEAD:<path>`); 0 mismatches between `status=mined` and a non-`—`
  `used-by` (and vice versa for `queued`/`rejected`). `recheck` vocabulary: `on-release` 25, `90d`
  5, `180d` 3, `365d` 1. All 34 rows carry `opened: 2026-10-19`.
- `## Paths`: 3 sequences, 28 `S###` tokens, **0 tokens outside the registry**. `## Search log`:
  2 bounded searches with stop rationales; search 2 records one *unavailable* lead.
- `## Leads (unopened)`: exactly one lead (GNU Bash Reference Manual, `pipefail`/`PIPESTATUS`),
  **no row id** — consistent with the LOG claim that the unopened lead holds no id. Per assignment,
  this lead is **not** used as evidence below.
- No literal `op://` and no credential-class hit in `SOURCES.md` at HEAD.

## 4. Directly evidenced study path from corpus/SOURCES.md

Path 1 (`## Paths`, committed at HEAD) is a reading sequence whose every step resolves to a
registry row and whose row `used-by` targets resolve to committed corpus files (§3). Quoted
sequence, then the rows (id → source → `teaches`), verbatim from the registry:

> kernel and userspace kill attribution — S003 → S004 → S002 → S013 → S015 → S014 → S032 → S007 →
> S011 → S016: start with the kernel's counter and event-time path record, establish cgroup counter
> scope, identify journal classes and trusted fields, then query mechanics, crash metadata and
> userspace paths that bypass kernel counters.

| step | id | source (anchor) | teaches (verbatim) |
|---|---|---|---|
| 1 | S003 | Linux `mm/oom_kill.c` v7.2 (`:447,935-936,945`) | Tie host and memcg OOM counter updates to the kernel victim path and use event-time kernel records for attribution. |
| 2 | S004 | Linux `mm/memcontrol.c` @ `c03c1a14…` (`:1820,1825,4965-4966`) | The OOM summary appends the victim and OOM cgroup paths at event time, while the event display reads the memcg counter. |
| 3 | S002 | cgroup-v2 docs (`memory.events:1448-1509`, `memory.peak:1418-1426`) | Distinguish hierarchical `memory.events` from `memory.events.local`; the documented `oom_kill` count includes processes killed by any kind of OOM killer. |
| 4 | S013 | systemd catalog @ `cf8ebfc6…` (`:66,604,884`) | The catalog gives distinct stable `MESSAGE_ID` values to core dumps, kernel OOM notices and oomd notices. |
| 5 | S015 | `systemd.journal-fields(7)` (`MESSAGE=:32-39`, `MESSAGE_ID=:41-44`, `_TRANSPORT=:204`) | `MESSAGE` is display text rather than metadata; `MESSAGE_ID` is the typed key and underscore-prefixed fields are trusted. |
| 6 | S014 | `journalctl(1)` (`--after-cursor:187-190`, `--output-fields:489-492`) | Select journal scope and cursor bounds, and request only structured fields for count-only queries. |
| 7 | S032 | `systemd-coredump(8)` (`COREDUMP_SIGNAL…:351-353`) | `COREDUMP_SIGNAL` supplies a numeric signal field so crash classification need not infer signal from message wording. |
| 8 | S007 | `systemd-oomd.service(8)` (Description; Options; Signals) | oomd selects eligible descendant cgroups and sends SIGKILL to all processes in the selected cgroup. |
| 9 | S011 | systemd `src/oom/oomd-util.c` v261 (`:269,274,306,313-316`) | oomd increments `user.oomd_ooms` before killing and records the killed-PID count in `user.oomd_kill` afterward. |
| 10 | S016 | earlyoom README @ `8477c902…` (What does it do; `--kernel-oom`) | Distinguish earlyoom's userspace SIGTERM/SIGKILL path from its explicit delegation to the kernel OOM killer. |

Evidence binding for the sequence: S003/S004/S007/S011/S013/S014/S015/S016 are `status=mined` with
`used-by` targets that all exist at HEAD (`knowledge/oom-kill-counter-kernel-only-r12.md`,
`kill-classes-by-message-id-r12.md`, `kernel-oom-line-attribution-r12.md`,
`userspace-oom-killers-r12.md`); S002/S032 are `queued` (no `used-by`), so a reader must treat steps
3 and 7 as un-consumed reading, not as already-applied lane knowledge. This is a reading order only;
it is not evidence that any step's claim is true (r1→r6 are declared not-evaluated by the gate).

## 5. README.md / QUALITY.md observations

- `README.md` (sha256 `acece436…`): index rows all resolve — gate r7 = **0 findings** — with 10
  backticked templates/globs skipped and **67/99 corpus files carrying no index row** (gate `# note`,
  explicitly not a finding). `## Frontier` FR1–FR14 each names a corpus evidence pointer; the r12
  additions (`knowledge/kernel-oom-line-attribution-r12.md`, `kill-classes-by-message-id-r12.md`,
  `userspace-oom-killers-r12.md`, `roster-truth-r12.md`) are indexed. `## Known gaps — round-12
  note` (:300) is the heading that triggers r4-3.
- `QUALITY.md` (sha256 `01afe954…`): criteria 1–25 are present and numbered; 6–25 each cite a
  lesson; `## Provenance of criteria 1–5` is present. All **22** `lessons/…` pointer occurrences
  resolve to existing committed files (`git cat-file -e HEAD:corpus/<path>`). The 12 `round-12.md#M…`
  fragments cited each resolve to exactly one row in `lessons/round-12.md`'s `## Mistakes` table
  (rows `| M1 |`…`| M26 |`, :24–:49; none missing, none duplicated) — note the fragment addresses a
  table **row**, not a rendered heading anchor. Quoted passages spot-checked at their cited lines:
  criterion 6 (`…errexit…:24-25`, `:101-102`), 7 (`…selftest-grep-sigpipe-race…:202-203`),
  10 (`…volatile-contract…:173-176` and `:172`, `:180`), 12
  (`…free-lunch…:266-268`) all reproduce.
- SHONEN.md: gate form check produced **zero shonen findings** (canonical header, exactly 4 boxes,
  all unmarked `- [ ]`, no extra lines, trailing newline; label `mori-shokunin`). The seed-indentation
  deviation recorded in LOG is consistent with this form pass; it is not a gate defect.

## 6. Named gate limitations (apply to this verdict)

- **Not evaluated at all:** r1 (is a token a source), r3 (falsifiability), r5 (negative claim needs
  its sweep), r6 (quote names its location), r9 (append-only / no cross-lane edits), box-3 (verifier
  independence), shonen-semantics (is a box claim true). A gate pass on any of these is not claimed;
  a gate failure elsewhere does not imply them.
- **r10 is not a lane-controllable cell.** The check demands
  `corpus/lessons/round-<R>-aggregator-*.md` in the *graded lane's* corpus, at whatever `--round`
  is passed. At this HEAD mori has **zero** `*-aggregator-*` lesson files in its whole committed
  history (committed-tree scan: mori 0; kagi 8, kake 7, kasegi 7, kengaku 6, kotoba 6, kumitate 7;
  the other 15 physical lanes 0). It therefore fires under `--round 9` **and** `--round 12`
  regardless of any lane corpus edit. The lane does carry a non-author round-12 verification
  artifact, `lessons/round-12-verifier-spotcheck.md` (added by `BF7CDC4`, author
  `protocol-shokunin`, not the lane), but that name does not match the gate's `-aggregator-` infix,
  so the gate cannot see it.
- **r2 is filename-keyed:** it only tests lessons whose filename contains `round-(\d+)`. Here that is
  2 of 12 lesson files (`round-12.md`, `round-12-verifier-spotcheck.md`); the 10 dated
  `2026-10-15-*.md` lessons are outside r2 entirely. Both tested files pass.
- **r4 is line-local** and fires on headings/table rows (§2.1); it does not check that the command
  exists elsewhere in the document.
- **r7 grades only `corpus/README.md` rows**, skips 10 templates/globs, and treats under-coverage as
  a note. `SOURCES.md` and `QUALITY.md` are outside r4/r7 scope; their structure in §3/§5 is this
  seat's measurement, not a gate result.
- **r8 classification is declared could-not-evaluate** (needs a vault read, operator-gated). The
  finding is a literal-text occurrence fact, not a verdict that a secret is live.
- **Snapshot semantics:** `--snapshot` grades `git archive <commit>` (no history), so r9 is
  unavailable and dirty/untracked bytes are invisible by construction (`dirty=0` is the mode, not a
  measurement — the separate `status --porcelain` in §1 is). No frozen expectation exists for this
  revision, so exit 3 cannot occur.

## 7. Provenance frontmatter scan (parent round-12 direction)

Bounded scan of `corpus/knowledge/**/*.md` at HEAD (20 `.md` files; `source:` / `verified-at:` /
`recheck:` frontmatter).

- The five round-12 additions all carry `source:`, `verified-at:` and `recheck:`:
  `kernel-oom-line-attribution-r12.md`, `kill-classes-by-message-id-r12.md`,
  `oom-kill-counter-kernel-only-r12.md`, `roster-truth-r12.md`, `userspace-oom-killers-r12.md`.
  Their `recheck:` values are executable `curl`/`journalctl`/`systemctl`/census commands plus
  observed results.
- Eight older knowledge files have **no** `source:` frontmatter (`audit-r11.md`,
  `progressing-weak-r2.md`, `silence-cutover-r3.md`, `silence-grading-r2.md`,
  `verdict-machine-r4.md`, `-r5.md`, `-r6.md`); `selftest-flake-r9.md` has source but no
  `recheck:`. Pre-existing, not introduced this round.
- **No `recheck:` value points into `.tower/worktrees`** (zero occurrences) and none points at an
  uncommitted artifact. Three `recheck:` values contain the literal token `/tmp` only as a
  qualifier: `observability-surfaces-r2.md:10-11`, `surfaces-r7.md:11`, `surfaces-r8.md:11` —
  `` `bash tools/mori-census.sh --selftest` (hermetic, /tmp only) ``, describing where the hermetic
  self-test writes, not where evidence lives. `selftest-flake-r9.md:12,15-16` cites
  `/tmp/mori-r9-note/oracle-after.log` **in `source:`/`verified-at:`**, self-labeled “(ephemeral)”
  and paired with durable receipts under `corpus/evidence/`; no `recheck:` field does this.
- **Provenance/fidelity finding (not a gate rule):** two committed r12 corpus files name the now
  retired worktree path `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mori-shokunin`
  (observed: `ls -d` → “No such file or directory”):
  `corpus/evidence/roster-r12-20261019T220912Z-before-live.log:2`
  (`base_copy=git -C …/.tower/worktrees/kaika/mori-shokunin show 20e2255:tools/mori-census.sh > /tmp/…`) and
  `corpus/evidence/roster-r12-20261019T220912Z-mutation.md:25`
  (`cp -a …/.tower/worktrees/kaika/mori-shokunin "$S/green"`). Both are commit-pinned (`show 20e2255:`)
  or SHA-recorded (`4fe9786d…` → `3da5b098…`), so the bytes remain reconstructible from the original
  repo, but the literal commands are not replayable as written and the recorded working tree no
  longer exists. Reported as provenance/fidelity, not as a gate finding.

## 8. Residual risk / verification gaps

- The verdict is **gate-mechanical only** (`not conformant` because exit 1). It is not a judgment of
  the lane's knowledge claims; r1/r3/r5/r6/r9 and SHONEN semantics were not evaluated by anyone here.
- Not re-executed by this seat: the lane's tools (`tools/mori-census.sh`, `mori-silence-cases.sh`),
  any external source URL, and every numeric claim in LOG/SCORECARD. The assignment forbids builds,
  tests and lint; none were run.
- `--round 12` r10 is a not-yet-due artifact of the aggregator's own round-12 review duty, not a lane
  corpus defect; a reader must not convert it into a lane conformance failure. The same r10 fires
  under the gate default, so no selector makes r10 green at this HEAD.
- No census baseline, census total, or score is published or frozen here; the parent's
  `FINAL LANES READY` signal is still awaited before any census figure is treated as final.

## 9. Reusable paths and exact commands

- Gate, one lane, named revision: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane-dir>
  <full-HEAD> [--round <N>]` (from the fleet-aggregate worktree; exit 1 if any r4/r8/r10, 0 clean).
- r8 reproduction over committed bytes: iterate `git ls-tree -r --name-only HEAD -- corpus`, filter
  `TEXT_EXT`, and apply the gate's `CRED_PATTERNS` to `git show HEAD:<f>` lines (reproduced
  4/3 files here).
- Lesson/pointer resolution: `git cat-file -e HEAD:<path>` for each `used-by` / QUALITY pointer; for
  `#M…` fragments, require exactly one `^| M<n> |` row in the target lesson.
- SOURCES integrity: parse `^| S\d{3} |` rows, assert ID continuity/uniqueness, resolve every
  `used-by` path at HEAD, and resolve every `S###` token in `## Paths`.
- Provenance scan: extract `^(source|verified-at|recheck):` lines per `corpus/knowledge/**/*.md` and
  flag `.tower/worktrees` / bare `/tmp` targets in `recheck:`.
