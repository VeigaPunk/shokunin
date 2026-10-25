# souji — Round 25 report

## Work performed

Declared claims: C1 — calibration (7), add a revision-scoped base-grounded-entry kill rule; C2 — operability (8), cover four bare/subdirectory/partialClone refusal edges; C3 — coverage (8), extend the F2 structure fixture to common/private gitdir and colocated/plain cases. C1 and C3 verify on their measured candidates; C2 is **unprovable on its frozen operability axis** because the actual change is coverage of input edge classes, not a new operability surface. This axis misattribution harms calibration, so the round is not admitted.

- C1 tool/fixture and independent measurement: `tools/souji-coverage-agreement.py`, `tests/fixtures/r25-coverage-agreement.py`, `census/round-25/records/c1-after.tsv` (`rev=7e4dbef94061578fca2f58621f87908c886cc431`; verified by `souji-receipt-run.py`). Base entry count was six, not the frozen draft literal four; amendment 1 corrected the literal before scoring. W2 chronology audit: `.ufo/waves/round-25/w2/ScoutC1AmendmentHistory.md`.
- C2 fixture extension: `tests/fixtures/r24-size-census.py`, `census/round-25/records/c2-after.tsv` (`rev=679e2d02f46ec06447d679d9395d6592c5e35f5c`; verify=ok). Red arms: 1efe406 = 11/12; regressed 778747e = 10/12. Mutation test: 12/20 listed mutants killed, eight survive (`.ufo/waves/round-25/w2/MutC2Survivors.md`). Refusal cases 11/12 report manifest changes but do not gate on them; amendment 2 §3 overstated the implementation (`CritC2Manifest.md`).
- C3 common/private-dir fixture and F2 entry/map: `tests/fixtures/r13-repo-structure.sh`, `corpus/knowledge/git-repo-structure-common-dir.md`, `corpus/README.md` Round 25 F2 row, `corpus/SOURCES.md` S124–S127; measured receipt `census/round-25/records/c3-after.tsv` (`rev=728b2ce71acbe574ae3036b456724d0a3d6f8f08`; verify=ok). Probe source bytes were unchanged. The extended fixture covers the common gitdir and private gitdir, not the linked worktree root; no universal write-safety claim is made.
- R24-M2/D4 marker, R24-M22/D6 mapping and Q57; D5 append-only namespace clarification; R3 receipt-digest wording; R17 post-stderr-shadow witness and historical lesson correction; R7 stdout-only refusal witness are recorded in `corpus/lessons/round-25.md`, `corpus/QUALITY.md` Q57/Q58, `tests/fixtures/r25-q57-check.sh`, `tests/fixtures/r25-slice-mapping.py`, and `tests/fixtures/r25-receipt-stderr.py`.
- Frontier step: S124–S126 admitted and S127 rejected after live opening; assimilation none. The C3 entry cites S124–S126 and the F2 study path advances `S124 → S125 → S126`; F2 remains frontier. `considerthese/` is absent in this lane.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no Souji round-25 misroot output. Fleet `.ufo/state/`, `.ufo/watchdog.log`, `.scratch/`, unrelated untracked wave/report files and `m-rev-vs-rev.py` were left untouched; no fleet-root/sibling files were written by this lane.
- No tools were installed or updated. No L0 question was filed. The L1 holds the planner seat.
- **Round shape / swarm:** intended two v1 waves: W1 32 seats (11 scout, 1 connector, 4 executor, 6 scribe, 4 reviewer, 2 critic, 2 mutation-tester, 2 sentinel; L1 held planner) and W2 39 falsification seats (11 reviewer, 11 critic, 8 mutation-tester, 8 scout, 1 sentinel). W1's `task` call was accidentally repeated with the identical spec: actual W1 spawn attempts 64. The first call's two census seats returned; the other 30 duplicate handles were canceled. The second call had 24 returns and 8 provider failures; W2 had 39 returns, no deaths. Total round attempts 103; 38 canceled/failed. No residual call, no replacement seats.
- **W1 canceled duplicate handles (last error: coordinator cancellation, no provider error):** `L1Souji25.{ScoutC1KillRule,ScoutC2Probe,ScoutC3Structure,ScoutSourcesOpen,ScoutD6Slice,ScoutR17RecordAgreement,ConnSiblings,ScoutScorecardLines,ScoutPreregAudit,ScoutSourcedClaimCheck,ExecC1,ExecC2,ExecC3,ExecR17,ScribeSources,ScribeLesson,ScribeQualityQ57,ScribeScorecard,ScribeReadme,ScribeD5D6,RevC1,RevC2,RevC3,RevR17,CritRound,CritFrontier,MutSizeCensus,MutCoverageAgreement,SentScope,SentSecurity}`. Returned first-call census identities were `ScoutGateCensus` and `ScoutToolSHA256Counter`; the duplicate second-call identities are the ones recorded in W1's registry.
- **W1 dead/provider-failed seats (last error, each):** `L1Souji25.ExecC3-2`, `SentSecurity-2`, `ScribeScorecard-2`, `RevC1-2`, `RevC3-2`, `CritRound-2`, `CritFrontier-2`, `SentScope-2` — `Cursor RATE_LIMITED_CHANGEABLE: You've hit your usage limit: You've saved $3102 on API model usage this month with Ultra. Switch to a different model or set a Spend Limit to continue with Auto. Your usage limits will reset on 11/18/2026.` W2 had no dead seats. The W1 duplicate dispatch is reported as a process defect; no seat was respawned under a replacement name.
- Routing: roles followed the host route table (no per-lane model parameter); W1 task progress explicitly reported `modelRole=m_flash`. The claims rest on L1-run counters/receipts and re-derived artifacts rather than a model answer alone.

## Landed changes

Each lane change is tied to the appended Round 25 `LOG.md` entry and to the lane commit that carries it:

| lane commit | landed change |
|---|---|
| `6e4737eab43d8fde1b85eb9f57023d29046705b4` | frozen preregistration and initial base controls (the initial C2/C3 bodies were later replaced by runner-generated captures) |
| `1814de557f76cf0a199fd062247b47c0b791f5e4` | amendment 1: C1 base count literal 4→6; runner-regenerated base receipts |
| `de736c258e6df4c5999360daac749721ae06eff8` | amendment 2: C2 red arms name both historical blobs; source selection aligned to S124–S126 |
| `6deb53561aace9aa14a399f88cf8150da4d4f4bd` | amendment 3: C1 k5–k7 and C3 red-arm oracles; runner-regenerated base-control receipts |
| `7e4dbef94061578fca2f58621f87908c886cc431` | C1 tool + fixture, measured independently before C3's F2 entry/map |
| `679e2d02f46ec06447d679d9395d6592c5e35f5c` | C2 refusal fixture cases 9–12 |
| `728b2ce71acbe574ae3036b456724d0a3d6f8f08` | C3 fixture, same-commit F2 knowledge/map, SOURCES/QUALITY changes, W1/W2 wave evidence, Q57 checker and source snapshots |
| `a8773254cff7adbcf7f121e3f60260fbdb011602` | C3 and record-agreement receipts, R7 witness, append-only correction notes and the honest-stop measurement/lesson updates |

Lane branch `master` is pushed at `a8773254cff7adbcf7f121e3f60260fbdb011602` (`jj-lane.sh state`: ahead=0, behind=0; `ls-remote origin refs/heads/master` matched). This fleet report is the final commit and is pushed separately.

## Before → after measurements

| claim | axis | before → after | counting command | measured commit |
|---|---|---|---|---|
| C1 | calibration (7) | base tool refuses `--base-rev` (rc 2), six base-grounded entries → `grounded=6 mapped=6 dangling=0 mismatches=0 kill_tested=6 kill_violations=0`, rc 0; fixture `9/9` inherited → `16/16`, control rejected. Red old tool: `9/16`. | `python3 -B tests/fixtures/r25-coverage-agreement.py --tool tools/souji-coverage-agreement.py`; real candidate run with `--rev 7e4dbef94061578fca2f58621f87908c886cc431 --base-rev a6d2d157755ef36b1dd4b9d53ad6d5b2ad6a3afe` | `7e4dbef94061578fca2f58621f87908c886cc431`; C1 verified |
| C2 | operability (8, frozen label) | `cases=8 pass=8` → `cases=12 pass=12 control=FALSE-GREEN-REJECTED lost_found=WRITE-DETECTED`, rc 0; red 1efe406 `11/12`; red 778747e `10/12`. | `python3 -B tests/fixtures/r24-size-census.py --tool tools/souji-size-census.py` | `679e2d02f46ec06447d679d9395d6592c5e35f5c`; unprovable on operability (coverage surface) |
| C3 | coverage (8) | `selftest=PASS ids=5/5` → `selftest=PASS ids=7/7`, rc 0; common/private manifests unchanged, `references.others.count=0` plain vs `2` keep-ref clone. | `bash tests/fixtures/r13-repo-structure.sh --selftest --probe tools/souji-repo-structure.sh` | `728b2ce71acbe574ae3036b456724d0a3d6f8f08`; bounded fixture result verified |

No 0–10 score mapping exists, and no numeric score changed. C1's count target is now six; C3 was measured before its separate receipt commit, with no change to the measured fixture/probe bytes.

## Sources & frontier

Counting command, before and after:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`

**Before** — exit 0, 31 W04 warning lines, 0 error findings:
```text
souji W04 S035 duplicate url git-scm.com/docs/git-repo across scopes
souji W04 S036 duplicate url git-scm.com/docs/git across scopes
souji W04 S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S049 duplicate url git-scm.com/docs/git across scopes
souji W04 S057 duplicate url git-scm.com/docs/git-config across scopes
souji W04 S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji W04 S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji W04 S063 duplicate url git-scm.com/docs/git-gc across scopes
souji W04 S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji W04 S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji W04 S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji W04 S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji W04 S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji W04 S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji W04 S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji W04 S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji W04 S089 duplicate url git-scm.com/docs/git across scopes
souji W04 S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji W04 S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji W04 S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji W04 S093 duplicate url git-scm.com/docs/git-diff across scopes
souji W04 S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji W04 S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji W04 S106 duplicate url docs.python.org/3/library/json.html across scopes
souji W04 S108 duplicate url docs.python.org/3/builtins/exceptions.html across scopes
souji W04 S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji ok /home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
exit=0
```

**After** — exit 0, 34 W04 warning lines, 0 error findings:
```text
souji W04 S035 duplicate url git-scm.com/docs/git-repo across scopes
souji W04 S036 duplicate url git-scm.com/docs/git across scopes
souji W04 S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S049 duplicate url git-scm.com/docs/git across scopes
souji W04 S057 duplicate url git-scm.com/docs/git-config across scopes
souji W04 S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji W04 S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji W04 S063 duplicate url git-scm.com/docs/git-gc across scopes
souji W04 S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji W04 S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji W04 S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji W04 S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji W04 S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji W04 S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji W04 S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji W04 S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji W04 S089 duplicate url git-scm.com/docs/git across scopes
souji W04 S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji W04 S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji W04 S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji W04 S093 duplicate url git-scm.com/docs/git-diff across scopes
souji W04 S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji W04 S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji W04 S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji W04 S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji W04 S106 duplicate url docs.python.org/3/library/json.html across scopes
souji W04 S108 duplicate url docs.python.org/3/builtins/exceptions.html across scopes
souji W04 S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji W04 S124 duplicate url git-scm.com/docs/gitrepository-layout across scopes
souji W04 S125 duplicate url git-scm.com/docs/git across scopes
souji W04 S126 duplicate url git-scm.com/docs/git-worktree across scopes
souji ok /home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
exit=0
```

Rows 123→127. Malformed NF!=13: 0→0. Tier histogram: A=117/B=5/C=1 → A=120/B=5/C=2. Status histogram: mined=100/queued=15/rejected=8 → mined=103/queued=15/rejected=9. Duplicate IDs, enum/tier-inflation violations and mined used-by missing paths: none→none. Added rows by tier/status: S124–S126 three A/mined, S127 one C/rejected. Existing rows touched (status/recheck/used-by): none. F2 study path advanced `S124→S125→S126`; no frontier→Core move. Rejected S127 keeps its reason and flip. Assimilation: none. `considerthese/` absent in lane.

## Trend verdicts

- **expansion — unchanged.** The new F2 entry deepens an already-mapped frontier ground; the map adds no new F2 ground and no Core transition.
- **quality — improved (bounded).** The new sourced entry and common/private-dir fixture clarify an r13 blind spot; source snapshots are pinned, and C2/C3 boundaries and survivors are disclosed. No pre-existing admitted entry was found false. Bound: the linked-worktree worktree root is not in the C3 manifest, and C2's refusal cases 11/12 do not gate manifest equality.
- **discernment — improved (bounded).** The r24 D6 disagreement is now an explicit mapping and Q57 with a red-before/green-after checker. It checks the four enumerated cites, not future omission discovery or truth of the authoritative table. No outside non-author re-grade of this round's S124/S127 gate decisions occurred; that remains closure debt.

Calibration is harmed by C2's axis misattribution; the verified C1 calibration instrument does not cancel that harm. Therefore the round is an honest stop, not an admission.

## SHONEN

[~] SKILL.md decision tables, error patterns and checklist — `SKILL.md:245-265`, `corpus/QUALITY.md`, and the round-25 fixtures. No non-author verifier checked this round.
[~] End-to-end domain task executed and logged — `LOG.md` Round 25 entry and candidate receipts; no cleanup/deletion action or operator handoff was performed.
[~] Instructions executable without oral context — `tests/fixtures/r25-coverage-agreement.py`, `r24-size-census.py`, `r13-repo-structure.sh`, and `r25-q57-check.sh` are runnable; limits remain explicit.
[~] No cross-domain bleed — `PROVINCE.md:48-57` adjacency and `corpus/lessons/round-25.md` boundaries; no sibling source trees were modified.

Stale-lane: mission exceeded two driver ticks and was progressing (lane commits and round artifacts landed; not silent). Open L0 questions: none. Tool installs/updates: none.
