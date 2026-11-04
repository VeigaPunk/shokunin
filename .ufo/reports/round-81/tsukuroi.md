# tsukuroi — round 81 report

Lane: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin` (branch `master`).
Landed lane tip: `4ffcbbd5c036718dc6ecec0e212901430c2c3fa3` (pushed; `git ls-remote origin
refs/heads/master` prints it). Measured work commit: `c6fd99493820947d16a3a1a4978efdf01ba20def`.
Base `96ad75b84160da58efaee4997576ce718fd72e2b`; declaration-only commit `80237118`.

This round declares **three claims** against three axes:

- **C1 — depth (8→9):** eight verified `/etc/fstab` → generated-mount-unit rows (MT1–MT8) over
  S331 (systemd v262 `man/systemd.mount.xml`) with three measured legs from S332 (this host's
  read-only generator capture). Counter: `tools/count-mount-rows-r81.py`. The 8→9 ordinal is the
  lane's self-assessment (SCORECARD "Round 81 — measured outcome"), subject to non-author closure.
- **C2 — operability (9→9, gate-standard debt closed):** the round-80 evidence counter maps
  could-not-evaluate to exit 2 through its public CLI and its selftest drives six gate-standard
  cases; six frozen cases must match. Counter: `tools/measure-round81.py`.
- **C3 — freshness (9→9, two inherited findings closed):** the knowledge-header gate's two
  findings are closed by appended dated `verified-at:` lines after seven pinned snapshots
  re-verify. Counter: `tools/check-knowledge-header.py` (existing instrument).

**Chronology defect, carried honestly:** the L1 authored and scored candidate files *before*
writing the declaration (commit `80237118`). The thirteen controls in `before/controls.json`
did run first, but candidate scoring did too, so this is **not a compliant pre-data freeze**.
The green final measurements below do not repair that, and no earlier claim is retroactively
admitted by them.

## Work performed

- **C1 entry landed.** `corpus/knowledge/mount-unit-fstab-plane-r81.md` (+ `.json` companion)
  holds MT1–MT8 — `DefaultDependencies`, `nofail`, `noauto`, `x-systemd.automount`,
  `x-systemd.before/after`, `x-systemd.device-timeout`, `x-systemd.requires/wants`,
  `x-systemd.wanted-by/required-by` — with S331 quote anchors and three measured legs from the
  host capture (`nofail` wanted-vs-required split, `tmp.mount`'s `Before=` from
  `x-systemd.before=`, and the `device-timeout` drop-in). Evidence:
  `corpus/knowledge/mount-unit-fstab-plane-r81.json` rows MT1–MT8;
  `python3 tools/count-mount-rows-r81.py --revision 4ffcbbd5…` → `count 8, target 8, met, rc 0`.
- **The wave falsified the author's first draft and the draft was corrected before landing.**
  Four sentences and one measured leg were contradicted by the host surface: the fstab count
  (nine non-comment rows, seven local mount points, five required, two `nofail` — not
  six/four), the `Options=` claim (`tmp.mount` keeps `x-systemd.before=local-fs.target`; only
  `x-systemd.device-timeout=` is consumed), "measured on this boot" (generator files were
  regenerated 2026-11-04 17:34:49, after the 2026-11-02 boot) and "up to ten seconds" (the 10 s
  `JobRunningTimeoutUSec` sits on the by-uuid alias while the required kernel device unit reports
  `1min 30s`; the consequence is now `[INFERENCE]`), and MT5's measured leg, which pointed at
  `var-log.mount` and now points at `tmp.mount` `:69-70`. Evidence: `w1/ScribeEntry.md` D1–D9,
  `w1/ScoutSurface.md` C1–C4, `w1/SentinelProbe.md` (falsifier fires on the token class),
  `w1/ExecRows/findings.json` F1–F4; corrections visible in the landed entry.
- **Line-anchor convention disclosed.** The `S331 :N-M` anchors index the XML with tags
  stripped (707 raw lines become 703 because the DOCTYPE at raw 2-3 and a `<ulink>` at raw
  84-85 each swallow a newline); the entry's Limits and S331's `anchor` cell both say so, and the
  per-line-strip repair is routed to the next round (`corpus/lessons/round-81.md`
  R81-CITED-LINES-STRIPPED).
- **C2 repair landed.** `tools/measure-round80.py` now returns `snapshot_tampered` and
  `snapshot_absent` as exit 2 (they were exit 1, i.e. a hard "unmet" verdict on evidence that
  merely could not be read) and its `--selftest` drives the public CLI over six isolated fixture
  trees instead of calling the reader directly. Evidence: `tools/measure-round80.py` docstring and
  `CannotEvaluate`; `w1/ExecGate.md` §2 matrix (base 3/6, candidate 6/6, and the two exports
  agree on every C1 verdict except the could-not-evaluate class).
- **C3 closure landed.** `corpus/knowledge/modprobe-config-plane-r72.md:92-101` and
  `corpus/knowledge/module-parameter-plane-r71.md:68-77` append a dated
  `verified-at: 2026-11-04` after `sha256sum -c SHA256SUMS` re-verified all seven pinned snapshots
  (r71 4/4 OK, r72 3/3 OK, rc 0 each). The filed header lines were not rewritten — the gate's
  last-occurrence rule is what makes the append operative, and ExecHeader's first-occurrence
  control (patched gate → 17 findings on the same bytes) shows the mechanism is load-bearing.
  Evidence: `w1/ExecHeader.md` §1–§6.
- **SOURCES rows added and corrected pre-append.** S331 (docs, A, `on-release`) and S332
  (own-work capture, A, `30d`) are new; both were still uncommitted first-appends, so their cells
  were corrected in place before their first commit rather than by a `supersedes` row (no
  committed row ever held these ids — `git log -S S331 -- corpus/SOURCES.md` is empty).
  Corrections: S331 `teaches` "the x-systemd.* dependency options attach … only" → the
  requires/wants and before/after options only (the "always applies to the created mount unit
  only" sentence exists only under those two options, stripped `:210-212` and `:246-248`); S331
  `anchor` `nofail :498-503` → `:498-504`; S332 `teaches` "only the /tmp entry carries the
  Before=" → "of the two nofail entries only /tmp … (the five required mounts carry Before= from
  DefaultDependencies)" because six generated units carry it (capture `:9,:24,:55,:70,:85,:100`);
  S332 `anchor` gains `pinned at lane commit 80237118`. Audit pointers:
  `w1/ScribeSources.md` V-S331-1/2, V-S332-2/3/4.
- **Lesson mined.** `corpus/lessons/round-81.md` carries `## Gate` (S331/S332 URLs, access date
  2026-11-04, located quotes, one reject: the disputed ArchWiki `nofail` page), `## Mistakes`
  (eight rows including R81-CITED-LINES-STRIPPED, R81-WRONG-UNIT-LEG, R81-COUNT-NO-COMMAND,
  R81-STALE-DIGEST, R81-UNMARKED-INFERENCE and the round-80-derived R80-C2-REGISTRY-NAME),
  `## Seat harm` (none observed) and the wave outcome.
- **Counter-attack scoreboard continued.** `SKILL.md` "Counter-attack scoreboard — round 81"
  records both counters' arms and survivors: C1 18 mutants, 3 killed, 13 behaviour-bearing
  survivors + 2 equivalent; C2 8 mutants, 4 killed, 4 survivors plus the case-A answer-key class.
  This is named coverage debt, not admission evidence.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no
  fleet-root file written by this round's seats: all twelve seats' artifacts resolved under
  `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/.ufo/waves/round-81/w1/`. Observed and
  **left untouched** (not mine): the 24-byte fleet-root file `after` (2026-11-03, content
  `== SCORECARD diff base-`, names no lane or round), `.ufo/reports/round-84/kama.md`,
  `.ufo/reports/round-89/kake.md` and the `.scratch/closure-*` orchestrator files.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Mount-unit plane entry + JSON companion (MT1–MT8) | Round81 "C1 — mount-unit plane (depth)" | `c6fd9949` |
| `tools/measure-round80.py` public-CLI exit map + six-case selftest | Round81 "C2 — gate standard (operability)" | `c6fd9949` |
| Appended dated `verified-at:` in the r72 and r71 notes | Round81 "C3 — provenance headers (freshness)" | `c6fd9949` |
| `corpus/SOURCES.md` S331, S332 (+ pre-append cell corrections) | Round81 + `corpus/lessons/round-81.md` Gate | `c6fd9949` |
| `corpus/lessons/round-81.md`, `corpus/README.md` round-81 row, `SKILL.md` round-81 section | Round81 "Wave" | `c6fd9949` |
| Wave evidence: spec, dispatch, ready/ready.dispatched, results, 10 seat reports + receipts, `after/host-fstab-20261104.txt` | Round81 "Wave" | `c6fd9949` |
| `SCORECARD.md` "Round 81 — measured outcome", `LOG.md` measured-outcome block, `after/measurements.txt` | the same Round81 entry | `c63511b4` |
| `SKILL.md` "Counter-attack scoreboard — round 81" | Round81 "Wave" | `4ffcbbd5` |

Landed commits: `c6fd9949` → `c63511b4` → `4ffcbbd5` (final tip, pushed).

## Before → after measurements

All three counters read committed bytes at a bound revision; every command below was run at the
final tip `4ffcbbd5` and returns the same verdicts as at `c6fd9949`. Raw outputs:
`.ufo/waves/round-81/after/measurements.txt`.

**C1 (depth), measured commit `c6fd9949` (re-confirmed at `4ffcbbd5`):**

```
$ python3 tools/count-mount-rows-r81.py --revision 4ffcbbd5c036718dc6ecec0e212901430c2c3fa3
{"claim": "C1", "revision": "4ffcbbd5…", "count": 8, "target": 8, "finding": "met", "problems": []}   rc 0
before: {"claim": "C1", "revision": "8023711867…", "count": 0, "target": 8, "finding": "note-absent"}   rc 1
```

**C2 (operability), measured commit `c6fd9949` (re-confirmed at `4ffcbbd5`):**

```
$ python3 tools/measure-round81.py --revision 4ffcbbd5c036718dc6ecec0e212901430c2c3fa3
{"claim": "C2", "revision": "4ffcbbd5…", "count": 6, "target": 6, "finding": "met",
 "cases": [A-selftest ok rc0, B-met ok rc0, C-mismatch ok rc1, D-tampered ok rc2,
           E-absent ok rc2, F-noargs ok rc2]}   rc 0
before (declaration baseline, base counter + frozen table): count 3 / target 6 / gate-standard   rc 1
```

**C3 (freshness), measured commit `c6fd9949` (re-confirmed at `4ffcbbd5`):**

```
$ python3 tools/check-knowledge-header.py --revision 4ffcbbd5c036718dc6ecec0e212901430c2c3fa3
{"branch_tip": "4ffcbbd5…", "clean_count": 99, "complete_count": 99, "finding_count": 0,
 "findings": [], "note_count": 99, "status": "PASS"}   rc 0
before: {"branch_tip": "96ad75b8…", "finding_count": 2, "note_count": 98, "status": "FAIL"}   rc 1
```

Selftests at the landed bytes: `count-mount-rows-r81.py --selftest` 6/6 rc 0;
`measure-round81.py --selftest` 2/2 rc 0; `measure-round80.py --selftest` 6/6 rc 0;
`check-knowledge-header.py --selftest` 25/25 PASS rc 0.

Do-nothing controls (declared before data): C1 at the declaration commit is `note-absent` rc 1
(the entry did not exist); C2's untouched base export scores 3/6 with the same frozen table
(`w1/ExecGate.md` §2); C3's base reads 2 findings. No claim is reachable by leaving the tree alone.

## Sources & frontier

**SOURCES census, before → after.** Rows at base `96ad75b8`: **330**; at the landed tip: **332**.

```
$ git -C tsukuroi-shokunin show 96ad75b8:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
330
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' tsukuroi-shokunin/corpus/SOURCES.md
332
```

Round start (as recorded in the declaration commit `80237118`): census `validate --root` rc 0,
rows 330. Round end:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
exit 0
```

(W04 duplicate-URL-across-scopes warnings are printed and pre-date this round; exit 0 is the
conformance requirement. The round-start exit 2 case does not apply — the registry existed.)

- **Rows added by tier:** A +2 (S331 docs, S332 own-work), B +0, C +0.
- **Rows touched old→new:** none in place on a committed row. The two new rows' cells were
  corrected before their first commit (S331 `teaches` narrowed, S331 `anchor` `:498-503`→`:498-504`,
  S332 `teaches` qualified to the nofail pair, S332 `anchor` gains the pinned commit) — recorded
  old→new in `corpus/lessons/round-81.md` Gate.
- **Frontier rows advanced: none.** No frontier bullet in `corpus/README.md` moved. The
  mount-unit plane is new Core ground under the lane's own province — it replaces boot-chain
  *incident evidence* (`corpus/knowledge/boot-chain-r17.md`, S056) with a decision plane of eight
  settings and three measured host legs, recorded as a coverage-map row in `corpus/README.md`
  "Round81" whose own text says "PROVINCE and the coverage frontier are unchanged".
- **Assimilation: none.** The `merge/tsukuroi/` staged package still collides with the lane
  registry (L0 `tsukuroi | round-75` open: 114 of 147 staged ids collide); no staged row was
  appended. Nothing in `/home/vgpnk/Projects/shokuknow` was written, fetched or pushed.
- **considerthese:** every proposal in `considerthese/2026-10-26.md` is already implemented
  (QUALITY 103 adopts "Downstream patch-offset check", 110 "Seat-harm incident log", 112
  "Burst-aware reading"; the "Counter-attack scoreboard" landed in rounds 41/52). No new
  proposal was mined; this round continues the scoreboard convention with its own numbers.

## Trend verdicts

- **expansion — improved.** New ground under the lane's own PROVINCE: a mount-unit plane the
  corpus did not hold (`git grep -l -i 'fstab\|automount\|systemd.mount\|x-systemd' -- corpus/`
  at base found SOURCES, boot-chain-r17, degraded-triage-r4 and a lesson, not a decision plane),
  landed as `corpus/knowledge/mount-unit-fstab-plane-r81.md` + `.json` (notes 98→99), two new
  mined rows (330→332) and a new SKILL.md decision table. Evidence: the C1 counter and the census.
- **quality — improved.** The round-80 routed gate-standard defect is repaired and measured
  behaviourally (base 3/6 → 6/6 over six public-CLI cases, `w1/ExecGate.md` §2), and the two
  inherited provenance findings are closed with executed re-verification (C3 2→0 findings, seven
  snapshots 4/4 + 3/3 OK). Quality is not claimed as complete: C1's selftest kills 3/18 mutants
  and C2's 4/8, both named as debt in SCORECARD and SKILL.md.
- **discernment — improved.** The wave falsified its own author's draft: four sentences and one
  measured leg were contradicted (`w1/ScribeEntry.md`, `w1/ScoutSurface.md`,
  `w1/SentinelProbe.md`) and were corrected before landing rather than defended; the reviewer and
  critic seats died with no report and are recorded as receiving **no attack credit**
  (`w1-results.json`), and the mutation survivors are reported instead of smoothed. The
  pre-declaration scoring erratum stays on the record.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  pointer: `SKILL.md` "Round81 mount-unit plane, gate-standard repair and provenance-header
  closure" (five-row decision table, instrument table, coverage-debt paragraph) plus the older
  health-verdict/update-safety tables; every row cites `corpus/knowledge/mount-unit-fstab-plane-r81.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: this round's
  host task (read `/etc/fstab`, the generated mount units, dependency dirs and device drop-ins,
  regenerate the generator into scratch and diff it) driven into MT1–MT8 with three measured legs;
  `LOG.md` Round81 "C1 — mount-unit plane (depth)" and `w1/SentinelProbe/probe.txt`.
- [~] Instructions executable by an agent without oral context — pointer: the entry's decision
  table maps each observed question to a read-only interpretation and next action, the recheck
  block names the exact command and expected output, and `SKILL.md` carries the instrument table
  with its exit map and selftest counts; no non-author has replayed it.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: the round stays inside the
  systemd/boot plane the lane owns; `corpus/README.md` states "PROVINCE and the coverage frontier
  are unchanged"; sibling-overlap scan `w1/ConnectorOverlap.md` found only mori's incident mention
  routing to tsukuroi, no ownership found.

## Round shape and seats

One v1 wave (policy band 8–16, run-15 §6), **12 seats, one `task` call, no residual call**:
3 executor (`ExecRows`, `ExecGate`, `ExecHeader`), 3 scribe (`ScribeEntry`, `ScribeSources`,
`ScribeLesson`), 1 scout (`ScoutSurface`), 1 connector (`ConnectorOverlap`), 1 reviewer
(`ReviewRows`), 1 critic (`CriticFreeze`), 1 mutation-tester (`MutCounter`), 1 sentinel
(`SentinelProbe`). Attack roles (reviewer, critic, mutation-tester) = **3/12 = 25 % nominally,
1/12 = 8.3 % effectively**: the reviewer and critic seats died before producing any finding, so
the ≥25 % attack floor is met only on paper and is reported as a protocol deviation. The sentinel
probe and the mutation-tester carried the actual falsification. The L1 holds the planner role (the
validator forbids a
spawned planner). Evidence: `.ufo/waves/round-81/w1-spec.json`, `w1-dispatch.json`, `w1.ready`,
`w1.ready.dispatched`, `w1-results.json`.

**Dead seats (2), reported as they are:** `ReviewRows` (reviewer) and `CriticFreeze` (critic)
returned a single truncated "I'll start by reading…" line with no report file and no receipt;
they receive no falsification credit. Their duty was carried by the executor, scribe, scout,
sentinel and mutation seats, which produced the four corrections and the mutation tally. No dead
seat was replaced. 10 of 12 seats produced durable reports.

**Inherited state (earlier attempt of this round):** the uncommitted note, SOURCES rows, lesson,
LOG/README/SKILL text and the `measure-round80.py` rewrite were re-verified against the seats'
findings, corrected where a seat had falsified them (fstab digest `a265a504…` →
`9effc73c…`, `[INFERENCE]` marking for mount-time filtering, the four SOURCES cell corrections)
and landed; nothing was discarded unexamined.

**Stale-lane:** respawn-per-round driver; this lane has no other open mission. Round 82 not started.

**Tool installs:** none this round (no `uv tool`, `npx`, `~/.local/bin` or pacman transaction;
pacman stayed paused host-wide). Seats used only pre-installed python3, git, systemctl (read-only
`show`), coreutils, curl, sha256sum.

**L0 questions:** none filed this round. Still open and routed around: `tsukuroi | round-57`
(service-config falsification probe authorization), `round-60` (whole-SKILL non-author SHONEN
verification), `round-64`/`round-75` (corpus-expansion-1 staged-id collision path).

**Scratch:** `/fast/scratch/hyaku/tsukuroi-r81/` held 459 MB after settlement — attempt 1's
`l1-headercheck` clone (449 MB), the two dead seats' trees (`CriticFreeze` 8 MB, `ReviewRows`
1 MB) and three small L1/attempt-1 dirs — and the L1 removed the whole root (`rm -rf`, verified
absent; `/fast` at 59 % used). Nothing this report cites lives under `/tmp`.

**Concurrent writer (disclosed).** Two writer processes committed to this lane inside the same
two minutes: `c6fd9949`, `9e723336`, `53d1cece` and, interleaved, `c63511b4` (LOG measured-outcome
block) and `4ffcbbd5` (SKILL counter-attack scoreboard). The final tree was re-verified green at
`4ffcbbd5` after the fact: C1 `8/8 met rc 0`, C2 `6/6 met rc 0`, C3 `0 findings rc 0`, registry
coverage `122/122 findings 0 rc 0`, knowledge refs `dangling 0 rc 0`, source census rc 0 with
332 rows. No path was written by a third party outside the lane; the fleet-root sweep is clean.
