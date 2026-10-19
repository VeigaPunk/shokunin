# kaika W1 — STATE dossier: `mori` (森 fleet & host observability)

- Lane repo: `/home/vgpnk/Projects/shokunin/mori-shokunin` (read-only). Author: W1StateMori. Measured 2026-10-19, ~21:05Z, at lane HEAD `20e2255`.
- Web: not used. This is the STATE scope; no source rows are claimed here. Interface docs are listed under **Leads (unopened)**.
- Paths: **(L)** means run from the lane root. **(F)** means run from the fleet root `/home/vgpnk/Projects/shokunin`. Every count is written `<n> — <command>`.

**Method and deviations (disclosed).**
- I ran only read-only modes of the lane's own gate: the live census and `--drift` against the committed baseline. Both are documented as writing nothing (SKILL.md:73-75).
  - Census git calls use `GIT_OPTIONAL_LOCKS=0` (tools/mori-census.sh:1253-1356).
  - The only `mktemp` is in the selftest (tools/mori-census.sh:1887).
- I did **not** run `--selftest` or `tools/mori-silence-cases.sh`, because both build `/tmp` fixture trees.
- The first live run used a transient capture file under `/dev/shm`. It was created and deleted inside the same command and is not cited as evidence; re-runnable commands are given instead.
- I counted conf lanes once by sourcing `shokunin.conf` in a subshell. This dossier cites a non-executing `grep` instead.

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| Domain | fleet & host observability: liveness, wave settlement, kill/OOM events, resource runway; "Detection and report only — never remediation." | PROVINCE.md:3-16 |
| Rank | shonen, on probation. No MANIFEST roster row. The fleet README lists it as shonen. | 0 — `jq '[.roster[]\|select(.id=="mori")]\|length' MANIFEST.json` (F); README.md:108; SKILL.md:3 "Rank: shonen." |
| Probation status | MINT.md:30 says "Probation: >=3 verified rounds before a roster row. Roster row withheld." 11 verified rounds exist, so the probation bar is met. The row is operator-owned (PROTOCOL.md:48-50). | — |
| Branch / HEAD | `master` = `origin/master` = `kaika/round` @ `20e2255e7b3ebb05a52272f35a996421cab14848` (2026-10-17T00:28:33-03:00). The kaika worktree `.tower/worktrees/kaika/mori-shokunin` is clean on `kaika/round`. | `git branch -a`; `git worktree list` (L) |
| Remote | `https://github.com/VeigaPunk/mori-shokunin.git` | `git remote -v` (L) |
| Commits | 38 — `git rev-list --count HEAD` (L). All 38 are authored `mori-shokunin <mori@shokunin.local>` — `git log --format='%an <%ae>' \| sort \| uniq -c` | — |
| Working tree | Clean. Untracked non-ignored files: 0 — `git ls-files -o --exclude-standard \| wc -l`. Stashes: 0. One ignored directory: `.ufo/interactive-sessions/` | (L) |
| **Last round** | **11**: capstone audit, admitted with correction. Evidence commit `e4855e8`, records commit `fd90f61`. | LOG.md:530-531 "Verified lane rounds: 10 → 11"; SCORECARD.md:523-580; MANIFEST has 11 closure entries, max round 11, statuses closed:10 / ok:1 — `jq -r '[.rounds[]\|select((.lanes?\|type)=="object" and (.lanes\|has("mori")))]\|"\(length) \(map(.round)\|max)"' MANIFEST.json` (F) |
| Commits after r11 | `d677cf3` (2026-10-16): SCORECARD contract scaffolds, logged at LOG.md:533-540. `20e2255` (2026-10-17): SKILL.md +71/−4 and .gitignore +1, with **no LOG entry**. | `git show --stat d677cf3 20e2255` (L) |
| **Next round** | **12**. No claim is registered for it: the chain in which each round registers the next stops at r11. | 0 — `grep -ciE 'round 12\|round-12' LOG.md SCORECARD.md .ufo/reports/round-11/mori-goalwave.md` (L) |
| Driver counter | `.ufo/state/mori.round` = **2** (written 2026-10-15T04:50:57Z). The last watchdog line is `launch mori round=2` (.ufo/watchdog.log:400). That is 9 behind the ledger, because rounds 2–11 ran as in-session goal waves. | `cat .ufo/state/mori.round` (F) |

## 2. Axes

The owned pair is **coverage + operability** (SCORECARD.md:3). All six axes are scored in SCORECARD.md:8-15.

| Axis | Score | Evidence pointer as written | True at HEAD? | Verdict cells r2–r11 |
|---|---|---|---|---|
| coverage | 5 | "the per-surface notes are still owed" | **no** — landed in r2 (`corpus/knowledge/observability-surfaces-r2.md`) | improved 5, unchanged 5 |
| operability | 6 | "`--selftest` passes 14/14" | **no** — now 66 cases; `PASS (66 cases, 66 passed, 0 failed)` ×2 in committed receipts | improved 6, "improved narrowly" 1, unchanged 3 |
| depth | **4** | finding-id vocabulary; "two are proposals" | partly | improved 10 |
| freshness | 5 | "no drift pin yet" | **no** — pin landed in r10 | improved 1, narrowly 4, unchanged 5 |
| calibration | 5 | "`progressing-weak` is declared deferred" | **no** — landed in r3 | improved 2, narrowly 4, unchanged 4 |
| adjacency | 6 | refuses kumitate and tsukuroi | yes, but souji is not named | **unchanged 10** |

- Tally command (L): `grep -oE '^\| (coverage|operability|depth|freshness|calibration|adjacency) \| \*\*[a-z ]+\*\*' SCORECARD.md | sed -E 's/^\| ([a-z]+) \| \*\*([a-z ]+)\*\*/\1|\2/' | sort | uniq -c`. Harmed cells: 0 — `grep -c '| \*\*harmed\*\*' SCORECARD.md`.
- **The score table is frozen at round 1.**
  - All six rows say "Last change: round 1", and none carries a counting command or a commit.
  - PROTOCOL.md:420 requires one: "Every score is a claim: it carries the counting command that produced it and the commit it was measured against".
  - The lane stopped moving scores after r2: "historical scalar scores are not advanced" (LOG.md:158-159).
  - 4 of the 6 evidence pointers are factually stale.
- **Lowest non-retired axis:**
  - **depth (4)** across all six scored axes;
  - **coverage (5)** within the owned pair.
  - Retired: none (SCORECARD.md:28-30).
  - The stagnation nudge is unavailable because no saturation line is declared.
- **Trend furthest behind: discernment (↔ calibration).**
  - It improved in 1 of 10 admitted rounds, r11: "the first round whose core product is discernment; it was externally probed by the critic-of-the-audit seat" (SCORECARD.md:573-575).
  - LEARNING.md:42-43 says "A subagent the lane dispatched is still the lane." So even that single improvement was self-attested (see M10).
- **Adjacency has never moved** in 10 admitted rounds.
- **Saturation:** not declared. SCORECARD.md:590-592 defers it "to the lane on its next round".
- **Capabilities:** 0 — `awk '/^## Capabilities/{f=1;next} /^## /{f=0} f' SCORECARD.md | grep -E '^\| ' | grep -vE '^\| (Capability|---|— none yet —)' | wc -l` (L).
  - Four capabilities can be demonstrated but have no row: live census (r1, `7ca17b1`), `--selftest` (r1), the behavioral oracle `tools/mori-silence-cases.sh` (r2 `3da8414`, hardened r4–r6), and `--pin/--drift` (r10 `5be8943`).
  - Rows enter only through a round that demonstrates the capability running (AXES.md:62-64).
- **Planned:** stale. SCORECARD.md:23-26 still reads "Round 2: land one note per surface family…".
  - r11 hands its carried items to the operator instead: non-author SHONEN check, receipt-binding and role-routing debts, and the promotion decision (SCORECARD.md:577-580).
- **Admission style:** 5 of 10 admissions are "ADMIT-with-correction" — `grep -cE '^\*\*Verdicts\.\*\* ADMIT-with-correction' LOG.md` (L).
  - That verdict does not appear in any fleet spec: 0 — `cat ../AXES.md ../PROTOCOL.md ../LEARNING.md ../CORPUS.md | grep -ci 'with-correction'`.

## 3. Corpus

**Counts (L)**
- Knowledge entries: 14 — `ls corpus/knowledge/*.md | wc -l`
- Lessons: 10 — `ls corpus/lessons/*.md | wc -l`
  - Named `round-<N>.md`: 0 — `ls corpus/lessons | grep -cE '^round-[0-9]+\.md$'`. They use date-slug names instead.
  - With a `## Gate` section: **0** — `grep -lE '^## Gate' corpus/lessons/*.md | wc -l`
  - Spot-check records: 0 — `grep -ciE 'spot-check|spot check' corpus/lessons/*.md` (summed)
- Evidence receipts: 53 — `ls corpus/evidence | grep -vc '^README.md$'`. The evidence README indexes them in per-round suffix tables; audit-r11 hash-verified 50/50 of the r2–r10 receipts (audit-r11.md:27-58).
- QUALITY.md criteria: 5 — `grep -cE '^[0-9]+\. ' corpus/QUALITY.md`
  - Criteria citing a lesson: **0** — `grep -c 'lessons/' corpus/QUALITY.md`
  - It is still headed "Admission bar (probation draft)" (QUALITY.md:1).
  - LEARNING.md:55-56 requires "every criterion cites the lesson that produced it".
- Coverage-map rows: 19 — `` grep -cE '^\| `(knowledge|lessons)/' corpus/README.md ``.
  - **5 corpus entries have no row:** `knowledge/audit-r11.md`, `knowledge/lane-silence-r2.md`, `lessons/2026-10-15-free-lunch-measurements-counter-baselines.md`, `lessons/2026-10-15-oracle-honesty-crash-masking.md`, `lessons/2026-10-15-settle-evidence-references-with-artifacts.md`.
  - Command: ``for f in corpus/knowledge/*.md corpus/lessons/*.md; do r=${f#corpus/}; grep -qF "| \`$r\`" corpus/README.md || echo "$r"; done``.
  - The README was last touched in r10 (`git log -1 --format=%h -- corpus/README.md` → `5be8943`), so r11's entries were never indexed.
- `## Frontier` rows: **0** — `grep -cE '^## Frontier' corpus/README.md`. The only headings are `## Coverage map` and `## Known gaps`.
  - Known gaps has 16 bullets; 10 of them announce *closed/landed* items. It reads as a history, not a gap list.
- PROVINCE Core / Frontier / Adjacent markers: **0** — `grep -ciE '^(#+ *|\*\*)(core|frontier|adjacent)' PROVINCE.md`. The structure is required by LEARNING.md:66-70.
- **External sources**
  - SKILL.md URLs: **0** — `grep -cE 'https?://' SKILL.md`
  - Knowledge entries citing any URL: **0/14** — `grep -lE 'https?://' corpus/knowledge/*.md | wc -l`
  - Whole corpus: 1 URL (`docs.kernel.org/accounting/psi.html`, at lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:70)
  - `corpus/SOURCES.md`: absent — `test -e corpus/SOURCES.md || echo absent`

**Header compliance.** CORPUS.md:17 requires each entry to open with `source:`, `verified-at:` and `recheck:`. The table gives the line number of each field, or `—` if absent.

| entry | source: | verified-at: | recheck: |
|---|---|---|---|
| observability-census-r1 | 3 | 4 | 6 |
| observability-surfaces-r2 | 3 | 8 | 10 |
| lane-silence-r2 | 3 | 11 | 15 |
| surfaces-r7 | 3 | 7 | 11 |
| surfaces-r8 | 3 | 9 | 20 |
| drift-pin-r10 | 3 | 20 | — |
| selftest-flake-r9 | 3 | 13 | — |
| audit-r11, progressing-weak-r2, silence-cutover-r3, silence-grading-r2, verdict-machine-r4, -r5, -r6 | — | — | — |

- Command (L): ``for f in corpus/knowledge/*.md; do echo "$f $(grep -n -m1 '^source:' $f|cut -d: -f1) $(grep -n -m1 '^verified-at:' $f|cut -d: -f1) $(grep -n -m1 '^recheck:' $f|cut -d: -f1)"; done``.
- Result: **9 of 14 entries lack at least one field; 7 lack all three.** Those seven open with `seat:`, `describes:` or `derived from:` preambles instead.
- **Overdue `recheck:` before 2026-10-19:** 0 by date. No recheck line carries a date; all of them are commands.
  - One recheck expectation is stale: observability-census-r1.md:6 still says "(14 cases)", and the count is now 66.
  - Every `verified-at` is 2026-10-14 or 2026-10-15.

**Live re-verification (freshness), 2026-10-19T21:05Z**
- **The drift pin is red.**
  - Command (L): `bash tools/mori-census.sh --drift corpus/evidence/baseline-r10-20261015T2231Z.json`, exit **1**.
  - Output: `MORI_DRIFT: +FINDING:UNIT_FAILURE_OUT_OF_SCOPE +other_authored_commits -FINDING:KILL_SIGNAL_JOURNAL -FINDING:SEGFAULT_JOURNAL -FINDING:WAVE_UNSETTLED_AGE -attribution -example -rowb_files SURFACE:journal basis obs`
  - r11 recorded "aging risk named, not realized" (SCORECARD.md:568). It is now realized.
- **Classifying the drift tokens**
  - **Journal tokens = a new boot.** `uptime -s` → 2026-10-19 08:11:44 -03:00. The probe reads `journalctl --user -b` only (tools/mori-census.sh:741,759), while the baseline was pinned 2026-10-15T22:26:29Z in an earlier boot (baseline line 3).
  - **`basis`, `-attribution`, `-rowb_files`, `+other_authored_commits`:** `lane.aggregator` was `row-B` in the baseline (line 14); it is now `progressing-weak`.
  - **Wave tokens:** the baseline has 11 `WAVE_UNSETTLED_AGE` (lines 26-36); live has 10.
    - `aggregator-r10` and `aggregator-r10-resume` were **emptied by souji's sweep**: commit `e20f4fa`, 2026-10-18T23:58:39-03:00. `git show --stat e20f4fa` (F) shows `.ufo/waves/aggregator-r10-resume/dispatch.json` deleted.
    - `shokunin-train-20261016-w24` is newly aged.
  - [INFERENCE] `obs` is the changed wave-id set.
  - No token points to a census regression.
- **Live census:** `MORI_CENSUS: DRIFT (findings=13 drift=12 unavailable=1 surfaces=7)`, exit 1 — `bash tools/mori-census.sh` (L).
  - `WATCHDOG_ABSENT` and `WATCHDOG_STALE`: log age_s=403605, pids=0. The fleet driver has been down since 2026-10-15T04:58Z.
  - 10 × `WAVE_UNSETTLED_AGE`. Waves: total=43, settled=13, unsettled=10, empty=20.
  - journal ok (unit_failure=3); cgroup ok; disk ok; tmux unavailable (rc=1).
  - Silence: **9 lanes graded** (8 progressing; aggregator progressing-weak).

## 4. Mistakes mined (17 classes)

"Captured?" reports a keyword sweep of QUALITY.md and SKILL.md (L): `grep -ciE -- '<term>' corpus/QUALITY.md` and the same against SKILL.md. Proposed criteria **Q6–Q12** are drafts. Each cites the existing lesson it comes from, as LEARNING.md:55-56 requires.

| # | Class | Evidence | Captured? | Proposed criterion / rule |
|---|---|---|---|---|
| M1 | A claim was over-stated and then narrowed at admission | r4 SCORECARD.md:229-235; r5 :265-273; r6 :310-319 (the claim failed at the first landed revision `9ce164ec`); r8 :413-422; r11 :546-560. 5 of 10 admissions. | QUALITY: `sniff`/`forg` 0. Only generic criterion 1 ("falsifiable"). | **Q7.** A "cannot fake / cannot fail" claim names the enumerated attack channels it was tested against. Untested classes are named residuals. ← lessons/2026-10-15-forgeable-oracle-visible-fixtures.md, -run-order-spoofing-shuffle-nonce-limits.md, -run-secret-timing-and-content-freshness-limits.md |
| M2 | Under errexit/pipefail, a crash exits with the same code as DRIFT | LOG.md:212 (`:517`); :241-243; :301 (`:227`). **Still open in production:** F01 at `:1366-1374` (audit-r11.md:156) and the named `:1322` debt (corpus/README.md:226-227). | `pipefail`: QUALITY 0, SKILL 0 | **Q6.** Every probe pipeline is rc-gated. A crash code never equals a verdict code. Each probe has an unreadable-input canary. ← lessons/2026-10-15-errexit-pipefail-silent-crash.md. Also add a SKILL error-pattern row. |
| M3 | `producer \| grep -q` under pipefail: SIGPIPE (rc 141) is scored as a missing match | LOG.md:438-442, 457-465 | `SIGPIPE`: 0 / 0 | Fold into Q6 ← lessons/2026-10-15-selftest-grep-sigpipe-race.md. SKILL row: "capture once, then grep". |
| M4 | An oracle the system under test can observe is forgeable | LOG.md:315-320, 346-351, 376-382. **Still open:** F02 — a wrapper replacing the verdict word with `BANANA` still scores `matched=28 total=28` (audit-r11.md:157); D13 normalizer boundary (:208). | SKILL describes the oracle contract (`nonce` ×7, SKILL.md:82-102). QUALITY 0. | Q7 (above) |
| M5 | Pointers rot and corrections are not swept | F03 (audit-r11.md:158) **re-propagated after the audit**: `20e2255` added SKILL.md:78 → `baseline-r10-20261015T2210Z.json`, which does not exist (`test -e corpus/evidence/baseline-r10-20261015T2210Z.json \|\| echo absent` → absent). SKILL.md:75 says "56 → 65 cases", but receipts show 66 (2 — `grep -ohE 'PASS \(66 cases' corpus/evidence/*.log \| wc -l`). SKILL.md:107-108 line pointers have drifted: the tsukuroi quote is now tsukuroi-shokunin/PROVINCE.md:19, the kama quote now kama-shokunin/PROVINCE.md:45-47. Also F04. | `pointer`/`resolve`: QUALITY 0, SKILL 0 | **Q8.** Every path or line pointer resolves at the carrying commit, and a replacement artifact lands with a sweep of every mention. ← lessons/2026-10-15-settle-evidence-references-with-artifacts.md; PROTOCOL.md:348-350 |
| M6 | Tallies disagree with the delivered artifacts | F05 (audit-r11.md:160): SCORECARD.md:429 says "eight r8 receipts"; there are 7. | QUALITY criterion 2 exists; the gate missed it. | None new. Record it as a gate miss in the round-12 `## Gate` section. |
| M7 | A fifth verdict value crept in | 9 — `grep -c 'improved narrowly' SCORECARD.md`; F08 (audit-r11.md:163) | `narrowly`: 0 / 0 | Q-row: verdicts are exactly the four values; qualifications go in the evidence cell. Needs a lesson first (currently audit-only). |
| M8 | Admission timestamps are later than their commits | F11 (audit-r11.md:166). PROTOCOL.md:343-344 forbids future-dated evidence. | `chronolog`: 0 / 0 | Q-row: an evidence timestamp is ≤ the commit that carries it. |
| M9 | Scratch evidence cannot be recreated | 140/275 fixture fingerprints are not recomputable (SCORECARD.md:550-554); F14 (audit-r11.md:169). PROTOCOL.md:341-343: tmpfs paths are not evidence. | `scratch`: QUALITY 0 | Q-row: commit the fixture generator plus a digest; a `/tmp` path is never evidence. |
| M10 | Discernment was self-attested | SCORECARD.md:573-575 conflicts with LEARNING.md:42-43. 0 spot-check records in the lessons. | `non-author`: 0 / 0 | Round-12 lesson with a `## Gate` section and a named non-author spot-check. |
| M11 | Changes landed without a LOG entry | `20e2255` touched SKILL.md and .gitignore with no LOG hunk. Before that, F10: an inherited dirty SKILL across r5–r10 (audit-r11.md:165). | The rule exists (AGENTS.md:4) but was violated. | None new. Record it as a gate miss. |
| M12 | Seat status ≠ artifact | A seat reported "failed" while its 19 KB report landed (LOG.md:61-65). 8 seats were lost to a content-filter 400 (LOG.md:250-255). A quota abort (F13, audit-r11.md:168). | SKILL wave rows only (SKILL.md:16,27) | Domain knowledge: settlement = artifact + status, never status alone (candidate K5). |
| M13 | A counter was read from the wrong field | The text grep read 0 segfaults while `COREDUMP_SIGNAL` held 656 (LOG.md:38-44). Signal 5 vs signal 11 (LOG.md:67-71). | `COREDUMP`: SKILL 0 (knowledge only) | SKILL error-pattern row, cited to a tier-A systemd-coredump source (Leads). |
| M14 | An unknown was collapsed into a negative | A missing `pgrep` was read as a dead daemon (LOG.md:46-53). **Still open:** D05 and D06 (audit-r11.md:200-201). | **Yes**: SKILL.md:51 "A missing surface is reported as `unavailable`, never as unhealthy." | Keep. Add fixtures for D05/D06. |
| M15 | Baseline aging realized | Risk named at LOG.md:490-493; drift exit 1 on 2026-10-19 (§3). | `re-pin`: SKILL 0. Policy exists in drift-pin-r10.md (corpus/README.md:258-259). | **Q9.** A baseline declares its volatile set and derivation window; re-pin is a recorded act with a reason, never a way to turn red green. ← lessons/2026-10-15-volatile-contract-behavioral-baselines.md |
| M16 | Blocked attempt (honest stop) | r2 interactive attempt: 0 seats dispatched, no credit (LOG.md:100-178; SCORECARD.md:32-95) | Protocol-level | Keep as evidence of taste. Not a QUALITY row. |
| M17 | Sibling hygiene interferes with the observation surface | souji `e20f4fa` emptied `aggregator-r10*`; the census now counts those waves as `empty`, which looks the same as never-written. | 0 — `cat PROVINCE.md SKILL.md corpus/README.md \| grep -ci souji` | Adjacency rule plus frontier row (K1). |

Lessons not yet folded into any criterion also back:
- **Q10.** A deferred probe carries its four prices before admission. ← lessons/2026-10-15-probe-pricing-dwell-bounds-filter-drop.md
- **Q11.** No counter is read without its baseline (boot, scope, anchor). ← lessons/2026-10-15-free-lunch-measurements-counter-baselines.md
- **Q12.** A crash-masking fix and a real repair are told apart by a pre-registered expected gradient. ← lessons/2026-10-15-oracle-honesty-crash-masking.md

**Gate disagreements on record:**
- audit-r11.md:88-109:
  - the first FIFO arm returned a verdict through a malformed `df` token;
  - a quota-aborted battery run;
  - "r10 drift works" and "r10 public recipe fails" are both true at the same bytes;
  - verdict arithmetic and verdict vocabulary are separate checks;
  - desktop journal events are not fleet kills.
- r4: the critic's sniffer-v3 overturned the stated claim (SCORECARD.md:229-235).

## 5. Contract defects (19)

| # | Defect | Rule | Evidence | Owner |
|---|---|---|---|---|
| C1 | The SHONEN heading is not canonical | PROTOCOL.md:417, 423-432: `<name>` is the repo directory name | `diff` against the seed shows one line: `# mori — Promotion checklist` vs `# mori-shokunin — …`. Boxes checked: 0/4 — `grep -cE '^- \[(x\|~)\]' SHONEN.md` | lane |
| C2 | No learning gate record | CORPUS.md:17-19; LEARNING.md:63-64 | 0/10 lessons named `round-<N>.md`; 0/10 have `## Gate` (§3) | lane |
| C3 | Knowledge header fields missing | CORPUS.md:17; LEARNING.md:61-62 | 9/14 entries lack at least one field (§3) | lane |
| C4 | The corpus index is stale and has no frontier | LEARNING.md:59-60; CORPUS.md:45 "An index row is a claim" | No `## Frontier`; 5 entries without a row; last touched `5be8943` (r10) | lane |
| C5 | The province is a fence, not a frontier | LEARNING.md:66-70; PROTOCOL.md:415 (declared surfaces must resolve) | 0 Core/Frontier/Adjacent markers. 4 siblings named — `grep -oE '→ [a-z]+' PROVINCE.md \| sort -u \| grep -vc report`; souji is missing, though souji-shokunin/PROVINCE.md:40 says "mori-shokunin observes fleet health and reports; souji acts on artifacts". "Scratch roots" do not resolve: `/scratch` is absent (`ls /scratch` → No such file); the census targets ROOT and `/tmp` (tools/mori-census.sh:282) | lane |
| C6 | QUALITY.md never learned from the lessons | LEARNING.md:54-58 | 5 criteria, 0 cite a lesson, still marked "probation draft" | lane |
| C7 | SCORECARD does not meet its contract | AXES.md:75-83; PROTOCOL.md:420 | Scores frozen at r1 with no command or commit; 4/6 pointers stale; Planned stale; saturation undeclared; capabilities 0; 9 non-vocabulary verdict cells | lane |
| C8 | SKILL.md is not a registry home and cites no sources | PROTOCOL.md:383-388 (8 row fields); :414 (cited sources) | 0 registry fields: `grep -ciE 'verdict map' SKILL.md` → 0; `grep -ciE 'write scope' SKILL.md` → 0; `grep -cF 'gate\|probe' SKILL.md` → 0. Yet SKILL.md:59 says "Registry row lands with the gate". Dead pointer at :78; stale count at :75; drifted line pointers at :107-108; 0 URLs | lane |
| C9 | No frozen run over a real input snapshot | PROTOCOL.md:375-382 §Two evidences | 0 — `find . -name 'expected*.json' -not -path './.git/*' \| wc -l`; 0 `frozen/` dirs. The drift pin fixes live *outputs*; the selftest fixtures are synthetic. [INFERENCE: probably does not satisfy the rule; the integrator decides] | lane |
| C10 | Named corrections are still owed | PROTOCOL.md:351-352: "A falsified claim … gets a named correction entry in the lane's next round" | F03–F11 and F14 (audit-r11.md:158-169) have not been appended. LOG.md has 0 deleted lines in history — `git log --numstat --format= -- LOG.md \| awk '{d+=$2} END{print d}'`, so append-only held. | lane, round 12 |
| C11 | A change landed with no LOG entry | AGENTS.md:4 | `git show --stat 20e2255` touches SKILL.md and .gitignore only | lane |
| C12 | Reports were filed lane-local, and the ledger uses a non-vocabulary status | PROTOCOL.md:138-140 "A report under any other name does not satisfy the contract."; :290 | Fleet `.ufo/reports/round-{2..11}/mori*.md`: 0/10. Lane-local `.ufo/reports/round-N/mori-goalwave.md`: 10/10. MANIFEST status `closed` ×10 does not appear in PROTOCOL's `ok/failed/in-flight/not-dispatched/unadjudicable` | integrator |
| C13 | No roster or ROADMAP row | PROTOCOL.md:48-50 | Roster rows: 0. ROADMAP: no `mori` (`grep -ci mori ROADMAP.md` → 0). MINT.md:30 still says the row is withheld. 11 rounds verified. | operator |
| C14 | An L0 question was answered in fact but not in the file | — | .ufo/l0-questions.md:28 asks for a remote URL. Origin now exists, and README.md:112 says the repos were pushed on 2026-10-16. No answer line has been added. | integrator |
| C15 | Counter namespace is out of sync | — | `.ufo/state/mori.round`=2 vs ledger 11. A driver relaunch would reuse admitted round numbers. The census cannot see this: 0 MANIFEST refs — `grep -c MANIFEST tools/mori-census.sh` (L). Its `state_lag` compares only to watchdog.log (tools/mori-census.sh:263, 539-546). The same question is open for other lanes at l0-questions.md:27,29,31. | integrator/kumitate (mori: detect) |
| C16 | Stray native session material | — | `.ufo/interactive-sessions/` holds 2.5 MB — `du -sh` — including a session `.jsonl`. It is gitignored by `20e2255` and was never read here; it may hold credentials. | operator/souji (never touch) |
| C17 | Bloat | — | SCORECARD.md: 44,143 B, 592 lines; the same round narrative exists 3× (SCORECARD, LOG, report). Committed seat drafts: 34 files, 329,104 B — `git ls-files -z '.ufo/round-*/goal-wave/*' \| xargs -0 cat \| wc -c` — 9.6× the final reports (34,294 B); they differ from the finals (124–336 diff lines each) and have provenance value. The Known-gaps section is history. SKILL.md lines run to 666 chars. | lane (judgment) |
| C18 | Tool defects are open at the audited bytes | audit-r11.md:156-216 | Census sha256 `d7710981…` and oracle `448f7723…` are unchanged since the audit (`sha256sum tools/*.sh`). Still open: F01, F02, F09, F12 (leading-zero seed), D04 (FIFO hang), D05, D06, D08 (system journal absent: 0 `--system` calls; probes at :741/:759 are `--user`) | lane |
| C19 | An inbound adjacency request is unanswered | AXES.md:16 (adjacency) | tsukuroi packet TSUKUROI-F1-MEM-01 (ADJ-04): tsukuroi-shokunin/corpus/knowledge/adjacency-handoffs-fleet-r1.md:74-112, "Request to mori: place this exact capture window [2026-10-15T04:53:46Z] against watchdog/wave liveness" (:107). Its state is "prepared"; acknowledgement is unobserved. | lane |

## 6. Proposed round 12

Rules for the shape: 1–3 claims on distinct axes, at least one on the lowest axis.
- Claims 1 and 2 cover both readings of "lowest": depth (4, lowest of all six) and coverage (5, lowest owned).
- Claim 3 works the trend furthest behind.

**Claim 1 — depth (lowest scored, 4): a source-linked SKILL.md.**
- Before (L):
  - `grep -cE 'https?://' SKILL.md` → 0
  - `test -e corpus/SOURCES.md || echo absent` → absent
  - `grep -lE 'https?://' corpus/knowledge/*.md | wc -l` → 0
- After:
  - SKILL.md cites at least 8 tier-A URLs, one per interface family the census reads (Leads list).
  - Every cited URL has a matching SOURCES.md row. This command must print 0:
    ```
    grep -oE 'https?://[^ )>|`]+' SKILL.md | sort -u | while read -r u; do grep -qF "$u" corpus/SOURCES.md || echo "MISSING $u"; done | wc -l
    ```
  - At least 3 new knowledge entries open with all three header fields and have a tier-A URL in `source:`.
  - Folds in M13 and M5 (sweep SKILL.md:75,78,107-108).
- **Serves SOURCES.md directly**, and clears the SHONEN box-1 blocker "source-linkage" (audit-r11.md:232).

**Claim 2 — coverage (lowest owned, 5): the silence roster equals the fleet's declared lanes.**
- Before:
  - Live `bash tools/mori-census.sh | grep -c '^SURFACE lane\.'` → **9** (2026-10-19T21:05Z).
  - The default is hard-coded at tools/mori-census.sh:312, copied from scripts/shokunin-watchdog.sh:14.
  - The fleet declares **20** lanes: `grep -oE '^[a-z0-9-]+\|' ../shokunin.conf | wc -l`.
  - Driver state holds 21: `ls ../.ufo/state/*.round | wc -l`.
  - mori itself is ungraded.
- After:
  - The live count is 20, with a `roster_source=` field.
  - Info findings name the difference between conf and state: audio, game-dev-2d, game-dev-3d appear only in state; kotodama and souji only in conf.
  - New selftest cases pass, and the oracle stays at `matched=28 total=28`. The oracle pins `MORI_ROSTER_LANES` per case (tools/mori-silence-cases.sh:485), so it is unaffected.
  - **Parse the conf, never source it:** it contains shell code (`SUBSTRATE_CMD`).
- Serves knowledge entry K2 and own-work/spec SOURCES rows (PROTOCOL.md:154-169, shokunin.conf).

**Claim 3 — calibration (discernment: 1/10, and self-attested): the learning gate exists.**
- Before (L):
  - `grep -lE '^## Gate' corpus/lessons/*.md | wc -l` → 0
  - `grep -c 'lessons/' corpus/QUALITY.md` → 0
- After:
  - `corpus/lessons/round-12.md` carries a `## Gate` section: candidates, admitted, at least one rejection with its reason, and a **named non-author** spot-check (agree/disagree on at least one admit and one reject) → count 1.
  - At least 4 appended QUALITY criteria from Q6–Q12, each citing an existing lesson → count ≥ 4.
  - Without the outside spot-check, the counts can still verify, but the discernment trend stays `unchanged` (LEARNING.md:37-45). Report it that way honestly.

**Alternates** (if wave 2 prefers):
- **freshness:** drift exit 1 with its tokens → every token classified in a dated receipt, plus a new pin saved as a new file with a recorded reason → `--drift <new>` exit 0.
- **operability:** fix F01 and F02. Before, the BANANA wrapper scores 28/28 exit 0 (audit-r11.md Appendix C); after, it must fail, and a long-history fixture must grade `progressing`.
- **adjacency** (never moved):
  - name souji and answer TSUKUROI-F1-MEM-01;
  - classify `empty` waves using souji's removal receipts;
  - before: 4 siblings named, 0 inbound packets answered.

**Obligations for round 12 that are not axis claims** (protocol hygiene):
1. Append named corrections for F03–F11 and F14 (C10) and sweep every mention.
2. Regenerate SHONEN.md verbatim (C1).
3. Add a SKILL.md registry row for census, oracle and drift (C8).
4. Append a LOG record for `20e2255` (C11).
5. Replace Planned, declare the saturation line and window (C7).
6. Add the 5 missing coverage rows, a `## Frontier` section, and Core/Frontier/Adjacent in the province (C4, C5).
7. Header backfill (C3) is in tension with "corrections are new entries" (CORPUS.md:52-55). Prefer additive header lines or superseding entries.

## 7. Candidate knowledge entries (from local evidence)

| Slug | Falsifiable claim | Evidence | Fills |
|---|---|---|---|
| K1 `wave-settlement-hygiene-interference` | A sibling's receipt-gated removal turns an unsettled wave into `empty`, and `empty` ≠ never-written | `e20f4fa` (F); baseline-r10 lines 26-27 vs live; census `empty=20`. Recheck: `git show --stat --format= e20f4fa \| grep -c 'waves/aggregator-r10'` (F) → 17 | waves surface; frontier F3 |
| K2 `roster-truth-three-sets` | The census default (9) = watchdog script default ≠ conf (20) ≠ driver state (21) | tools/mori-census.sh:312; scripts/shokunin-watchdog.sh:14; the conf grep; `ls .ufo/state/*.round` | silence surface |
| K3 `counter-namespace-desync` | Goal-wave rounds bypass the driver counter (state 2 vs ledger 11), and `state_lag` cannot see it | `.ufo/state/mori.round`; MANIFEST jq; tools/mori-census.sh:539-546 | watchdog surface |
| K4 `drift-aging-after-reboot` | A pin from boot A goes red in boot B through the journal `-b` scope alone | drift output 2026-10-19; `uptime -s`; tools/mori-census.sh:741 | drift-pin row |
| K5 `seat-status-vs-artifact` | Harness status and artifact existence are independent observations | LOG.md:61-65; LOG.md:250-255; audit-r11.md:168 | waves, settlement semantics |

All five fit QUALITY 1–3: each is falsifiable, has a measured anchor, and keeps observation separate from inference.

## 8. Frontier seed (rows for `## Frontier` and PROVINCE Frontier)

- **F1** System journal: kill and segfault scope (D08). The system journal held 626 segfaults the census never sees (corpus/README.md:266-268).
- **F2** Quota observability. The fleet's real disk failures are `EDQUOT` events (SKILL.md:161-163; F13 quota abort).
- **F3** An authoritative wave settlement contract, with kumitate (D07): 10 aged-unsettled and 20 empty waves live; hygiene emptying (K1).
- **F4** Counter-namespace reconciliation: driver state vs MANIFEST vs lane LOG (K3).
- **F5** Daemon identity: argv-substring false positives (D06) and degraded-probe early return (D05).
- **F6** Instantaneous write rate, a measured deferral (D11).
- **F7** The tmux live arm, so far proven on fixtures only (D12).
- **F8** Attributing OOM/kill events to the fleet, with tsukuroi ADJ-04 (D09; C19).
- **F9** Threshold calibration using an alert-cost rule (D10).
- **F10** Durable fixture evidence: scratch fixtures that cannot be recreated (F14).

## Leads (unopened)

These are interface families the census reads with **zero tier-A citations** in the lane. They are for the ART dossier or wave-2 writers to open and register:
- `docs.kernel.org/admin-guide/cgroup-v2.html`: `memory.events` vs `.local`, `memory.peak`, `memory.max`, `memory.pressure`
- `docs.kernel.org/accounting/psi.html`: cited once in a lesson, never opened as a row
- freedesktop systemd `systemd-coredump(8)` and `systemd.journal-fields(7)`: `COREDUMP_SIGNAL`
- `journalctl(1)`: `--user`, `-b`
- `docs.kernel.org/admin-guide/iostats.html`: `/proc/diskstats`
- POSIX `df -P`: 1024-block columns
- `tmux(1)` FORMATS: `session_activity`, `pane_current_path`
- procps `pgrep(1)`
- coreutils `timeout -k`
- bash manual: `pipefail`, `PIPESTATUS`
- `pipe(7)` / SIGPIPE
- `git(1)`: `GIT_OPTIONAL_LOCKS`
- frontier only: `systemd-oomd(8)`
