# souji round 98 — report (attempt 2, SoujiR98a2; inherited from attempt 1, SoujiR98)

## Work performed

Declared claims (1–3, each falsifiable, causally separable, distinct axes) with their target axes:

- **C1 (calibration 7):** a latch keyed on the exception object itself (`exc._souji98_last`, a per-object event
  stamp; `WeakKeyDictionary` is unavailable for `SystemExit` on CPython 3.14.8) makes the 17-shape declared-exit
  table print `SHAPES-SUMMARY shapes=17 mismatched=0`, with q1o and q1q at 70 and every caught shape keeping its
  plain exit code; the r95 and r97 hooks on the same table print `mismatched=3`; the 278-mutant no-harm holds
  with byte-identical survivor sets (76 ids, empty symmetric difference).
- **C2 (operability 8):** the arms counter reaps only the pid the arm recorded at spawn (starttime-verified) and
  its ppid-chain descendants, or an orphan reparented to the counter (`PR_SET_CHILD_SUBREAPER`); argv never
  authorises a kill. The committed decoy test plants foreign sleepers carrying the counter's OWN T1 reap token
  and polls each sleeper's pid continuously; the T1 survivors count uses the descendant relation; `conform`
  binds `survivors=0` on T1.

Work items (one bullet per item, each with an evidence pointer):

- C1 latch build (object-keyed stamp, last-stamp==EH decides declared; A11 traceback restored, A3 kept) —
  `census/round-98/c1-survivor-search.py` (e8ba780a…) + `census/round-98/declared-shapes.py` (dcec0c9e…); seat
  `R98ExecC1.md` ("F1 — r97 global pending defeats q1o/q1q/q1i; F2 — N=0 measured").
- The 17-shape table landed with q1i pinned `declared` at the A0.1 freeze (`.`md A0.1 amendment; the
  `declared-shapes.expected` freeze note records R98Reviewer1 F3 + R98Critic K1 + R98MutC1 F3 disagreeing on
  the r97 limit and settling it here).
- The 278-mutant no-harm measurement: `SEARCH-SUMMARY generated=278 ambiguous=9 uncompiled=0 hung=1
  scored=268 errored=53 killed=139 survived=76` in both `census/round-98/records/search-r97.log` and
  `search-r98.log`; survivor id lists identical (`survivors-r98.json`, 76 ids).
- C2 in-round instrument repairs under the frozen A0.1: the decoy test now carries the counter's own T1 token
  and polls the sleeper's own pid continuously (M7); the T1 survivor count uses the descendant relation (M8);
  `conform` binds survivors=0 on T1 (R98Connector C-3); the CM8 mutant is a real argv-only reap (R98ScoutSources
  F2: the committed mutant signalled nobody, so the decoy predicate could not distinguish it).
- The 12-seat v1 wave (5 attack seats: 2 reviewer, 1 critic, 2 mutation-tester; 1 connector; 1 scout; 1 scribe;
  3 executor) — `.ufo/waves/round-98/w1/`; the L1 holds the canonical planner seat. No re-dispatch of w1:
  attempt 1's wave was still running when attempt 2 was bound to it, per the orchestrator's message. ExecC2,
  MutC2 and Sentinel produced no committed report files in the lane wave dir; their scratch was deleted, and
  their live runs are **not** cited as evidence here.
- Live source re-open (S075/S372/S368, each HTTP 200, sha256 in the lesson `## Gate`, byte-identical to
  `census/round-98/srcs/*`, occurrence 1) — `R98ScoutSources.md` §1 + `reopen-sources.out`.
- The connector incident is recorded, not hidden: its cleanup SIGKILLed 26 processes of sibling seats at
  ~12:33:50Z (`R98Connector.md` §6.1; `R98Scribe.md` §1.5 + F5 NOTED). The L1's own measurements are from
  post-incident runs, and no `rc=-9` result is cited as evidence of anything.

## Landed changes

Every change below is tied to a LOG.md entry (the trailing `## Round 98` block) and to the commit hash that
carries it: node `ca98ad08bd87d595367ed9ddb64bb46114209f36` (lane, verified on the remote — see Verification).

- `census/round-98/c1-survivor-search.py` (e8ba780a…): the object-keyed latch, A11 traceback-after-marker, A3
  fallback kept.
- `census/round-98/declared-shapes.py` (dcec0c9e…) + `declared-shapes.expected` (23111a…) + `shapes/` (17
  scripts; the 14 r97 shapes byte-identical + q1o/q1q/q1i).
- `census/round-98/c2-setup-arms.py` (0886271b…): ownership reap with the descendant-relation survivor count
  and the survivors-binding conform.
- `census/round-98/c2-decoy-test.py` (12e6ddcb…): the corrected decoy test (plain sleeper, byte-exact own
  token, continuous post-snapshot planting, per-plant pid polling).
- `census/round-98/c2-cm8-mutant.py` (a7760a76…): the CM8 ownership mutant as a real argv-only reap.
- `census/round-98/c2-forgery-probe.py` (e5724d19…; unchanged from r97 per its docstring).
- `census/round-98/controls/` (`c1-r95-search.py`, `c1-r97-search.py`, `c2-r97-arms.py`, `c2-r97-probe.py` —
  do-nothing bytes at ff254387).
- `census/round-98/srcs/` (live captures: `proc_pid_stat.5.html` 0f04d789…, `monitoring.html` 2b281793…,
  `proc_pid_stat.txt`, `live-field-check.txt`).
- `census/round-98/records/shapes-r95.txt`, `records/shapes-r97.txt`, `records/shapes-r98.txt`,
  `records/search-r95.log`, `records/search-r97.log`, `records/search-r98.log`, `records/survivors-r98.json`.
- `corpus/lessons/round-98.md`: `## Gate` (S075/S372/S368 re-opened live this round, byte-identical captures,
  occurrence 1; S075 field-4 attribution corrected), `## Mistakes` M6–M8 (each shown able to fail),
  `## Frontier` (Assimilation: none; the lane has no `considerthese/` dir).
- `corpus/knowledge/crash-channels-beyond-excepthook.md`: r98 correction appended (object-keyed latch, q1i
  declared superseding limit (i), A11/A3).
- `corpus/knowledge/deadline-owned-reaping.md`: r98 correction appended (ownership reap; r97 argv reap not to
  be cited as ownership; survivors binding).
- `corpus/QUALITY.md`: Q175 (decoy must carry the byte-exact identity and poll the carrier's pid; do-nothing
  must fail post-snapshot), Q176 (descendant-relation survivor counting; bind the count into conform).
- `plans/round-98.md`: A0.1 freeze amendments (q1i declared superseding limit (i); "every handled shape at 1"
  corrected to plain==hooked; conform binds survivors; CM8 naming split; in-round repairs M6–M8).
- `SCORECARD.md`: round-98 measurement table (C1 after mismatched=0; C2 survivors byte; no score change),
  capability rows (none entered), planned r99.
- `LOG.md`: the round-98 entry (claims, landed, withdrawn sentences (r97 "closes the trade" / "signals only
  processes it planted" / S075 field-4 / q1i limit (i)), the connector incident, tool installs: none).

## Before → after measurements

Counting command per claim, run against the landed commit `ca98ad08…`; the full per-shape output is in
`census/round-98/records/shapes-r98.txt`, and the search receipts in `records/search-r*.log`.

- **C1.** `python3 -B census/round-98/declared-shapes.py --search census/round-98/c1-survivor-search.py
  --scripts census/round-98/shapes --work <empty>` → `SHAPES-SUMMARY shapes=17 mismatched=0`, EXIT 0 (q1o and
  q1q at 70; t1/t4/q1i at 0; a1/a5/a5b/a4/a12/v1 at 3). Before: the same command with
  `--search census/round-98/controls/c1-r97-search.py` → `SHAPES-SUMMARY shapes=17 mismatched=3` (q1o 1, q1q 1,
  q1i 70) and with `c1-r95-search.py` → `mismatched=3` (q1i only). No-harm: the 278-mutant search summary is
  identical between r97 and r98 runs (`errored=53 killed=139 survived=76`), and the survivor id lists are
  byte-identical (diff empty).
- **C2.** `python3 -B census/round-98/c2-setup-arms.py --probe census/round-98/c2-forgery-probe.py
  --fixture-pass tests/fixtures/r93-k4-flagfail.py --fixture-fail tests/fixtures/r92-k4-flagfail.py --tool
  tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty> --jobs 4`
  → `ARM T1 exit=2 want=2 line=yes conform=yes survivors=0` with `--survivors 0 planted-killed 1--` in the
  T1.out, and `ARMS-SUMMARY arms=20 conform=20` binding survivors=0 on T1. The decoy test
  (`c2-decoy-test.py --counter c2-setup-arms.py …`) gives `DECOY-SUMMARY verdict=spared` (exit 0) and the same
  command with `--counter census/round-98/controls/c2-r97-arms.py` (the argv-only do-nothing control) gives
  `verdict=killed` (exit 1); the repaired CM8 mutant also gives `verdict=killed`. A same-tick timeout arm
  (e.g. a P1 arm printing exit 2 instead of 0) is recorded as that arm's end-of-arm outcome; it is not folded
  into the T1 survivors binding.

## Sources & frontier

Assimilation: none this round (no `merge/souji/` theme taken; the report's obligation under the assimilation
contract is satisfied by this line). considerthese: the lane has no `considerthese/` dir.

SOURCES.md rows before→after with the counting command: three rows were **re-opened live this round** by the
scout seat (no new row; no status/recheck/used-by change):

- S075 `proc_pid_stat(5)`: https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html, HTTP 200, 20647 bytes,
  sha256 `0f04d789…`, occurrence 1, field-4 ppid wording 8 words and the field-22 starttime wording both
  located. The registry row's scope is fields 5/6/22; the field-4 attribution is the kernel-side S332
  (scout §1.3, F4).
- S372 sys.monitoring RERAISE: https://docs.python.org/3/library/sys.monitoring.html, HTTP 200, 74653 bytes,
  sha256 `2b281793…`, quote 13 words, occurrence 1.
- S368 setsid(2): https://man7.org/linux/man-pages/man2/setsid.2.html, HTTP 200, 11555 bytes, sha256
  `52cbc190…`, quote 17 words, occurrence 1.

Counting command: `bash .ufo/waves/round-98/w1/R98ScoutSources/reopen-sources.sh` (live fetch + committed-
capture comparison + occurrence counts; exit 0, receipt `R98ScoutSources/reopen-sources.out`). Rows added by
tier: none. Rows touched old→new: none (no status/recheck/used-by change). Frontier rows advanced: none; the
one sourced claim in this round rests on rows re-opened this round (C1 ← S372; C2 ← S075/S368), per the
frontier contract. SOURCES.md itself is **unchanged** (registry stays 294 rows); sources-census validate was
run by the L1 at freeze (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`).

## Trend verdicts

- **expansion: unchanged** — no registry row added and no admitted entry on uncovered coverage-map ground;
  two knowledge corrections cite only re-verified rows (registry 294→294).
- **quality: unchanged** — two knowledge entries gained r98 corrections that supersede the withdrawn r97
  sentences; no falsified sentence ships in this round.
- **discernment: harmed** — the lane's pre-freeze gate missed the decoy-token mismatch (M7), the survivor
  metric defect (M8) and the kind-swap movability (M6); all three were caught by attack seats (connector,
  scout, critic, scribe), not by the lane's own gate. The disagreements became frozen amendments and M6–M8.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  (evidence: SKILL.md Decision tables/Error patterns/Checklists/Gate registry; verifier `endpoint` pending)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  (evidence: LOG.md:362; verifier `endpoint` pending)
- [~] Instructions executable by an agent without oral context
  (evidence: census/round-21/run-acceptance.py; census/round-21/accepted-matrix.json; verifier `endpoint` pending)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  (evidence: PROVINCE.md Round21 privacy boundary; verifier `endpoint` pending)

Stale-lane: no other mission of this lane is open. Tooling: none installed or upgraded this round (no pacman —
paused host-wide per the addendum guard; no uv/npx/binary fetch; no sysctl or sudo). This round's wave is the
12-seat w1 noted above; no residual call; round total 12 seats (10 reported, ExecC2/MutC2/Sentinel unreported
in the lane wave dir).
