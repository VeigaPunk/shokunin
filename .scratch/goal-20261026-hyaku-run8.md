<!-- ORCHESTRATOR-OWNED run state (hyaku run 8). Not a misroot: lanes and seats never move, copy-then-delete, or edit this file. -->
# hyaku run 8 — inline swarm rounds toward round 100 (2026-10-26)

Operator directive, verbatim: "ok we will be doing the shokunin training, in the hyaku format; I would like us
to first estabilish the model delegations for each role; then, you decide the order onto which shokunins to
develop and train upon;" — then: "ok so start the training run, the goal is to get every single shokunin to
round 100; we will be doing it for the next 12h" (run start 2026-10-26).

## Routing (global role map, `~/.omp/agent/config.yml`; backup `config.yml.pre-run8-20261026`)

Probe 2026-10-26 (`scripts/hyaku/probe-alias.sh`), primary-ok: m_opus, m_sonnet, m_haiku, m_flash
(opencode-go/deepseek-v4.1-flash), m_zfl, m_mim, m_kfc, m_k31, m_glm53, m_antigravity, m_luna, m_swe, m_inc, m_beam.
Primary down: m_grok (402 balance exhausted), m_argon (429) — both route no role.

| roles | alias (operator choice) |
|---|---|
| task (L1s, closure judges), main, planner | @m_opus |
| reviewer, mutation-tester, security-reviewer | @m_zfl |
| scout | @m_sonnet |
| distiller, seance | @m_haiku |
| connector | @m_kfc |
| executor, labrat, scribe, sonic, simplifier, critic, revenger, sentinel | @m_flash |

Risk: the m_opus fallback chain is mercury-3 -> gpt-6-luna:low; gpt-6-luna policy-refused L1s in run 7. If Anthropic
throttles, L1s and judges degrade there. The m_kfc chain has no kimi second hop (kimi 429'd at ~16:15 in run 7);
it affects only the connector seat.

## Round shape

64–100 seats per round (lane-addendum §6), as in run 7.

## Phase 0 — close run 7 before any dispatch

`inline.sh verify <lane> && inline.sh closure <lane>`, then a closure judge (@m_opus) for each, then `advance`:
souji r29, kama r43, kasegi r32, kengaku r36, kotoba r74, kotodama r74, kumitate r65, mado r42, tameshi r47.
Kama: lane worktree detached at sandbox mutant 873c5d77 (master 3e6fdbe9); jj-lane.sh refuses it. Repair before
its first run-8 dispatch.

## Lane order (orchestrator choice)

6 concurrent lane slots. Run 7 ran 8 slots against a measured live cap of 100 jobs, and three L1s (kotoba r73,
mori r49, kumitate r65) ended up with single waves below the 64-seat floor. A lane runs 3 consecutive rounds, then
gives its slot to the next lane below. Within a block, the lane furthest from 100 goes first.

- Block A: tabi (29, fresh-start), souji (30), kasegi (33), kaidoku (36, fresh-start), kengaku (37),
  tsukuroi (38, fresh-start)
- Block B: mado (43), kama (44), tameshi (48), mori (50), chousa (52), kake (58)
- Block C: kumitate (66), revenger (71, fresh-start), kotoba (75), kotodama (75)

Kotodama goes last because its open L0 kill-rule-vs-predicate questions (round-69, r74 frozen-claim conflict)
bear on its closures. After block C, freed slots go to the lowest next-round.

## Holds / unblocks

- The run-8 start directive ("every single shokunin to round 100") unblocks tabi, kaidoku, tsukuroi and revenger.
  Their block files are copied to /fast/scratch/hyaku-run8/unblocked/ and an unblock event is logged. Each lane's
  first run-8 round is a fresh-start round (addendum run-8 block). If closures keep being rejected, `advance`
  re-blocks the lane on its own (streak ≥3).
- kagi stays on HOLD. Its block is an operator content-safety HOLD that waits on a specific ruling (L0
  `kagi | round-28`), not a rejection streak. The run-7 directive was equally broad ("each shokunin that hasn't
  gotten to that threshold") and kagi stayed held under it.

## Incidents

- 2026-10-26 ~01:30 (orchestrator) kama worktree repair: the first `rm` deleted 3727 tracked files. Restored
  with `git reset --hard HEAD`. Untracked r35/r36 leftovers are quarantined in
  /fast/scratch/hyaku-run8/kama-worktree-backup/.
- 2026-10-26 ~02:0x: six tracked fleet-root files were deleted from the working tree only, not from HEAD:
  `.gitignore`, `AGENTS.md`, `LOG.md`, `README.md`, `SCORECARD.md`, `.ufo/reports/round-1/kaidoku.md`.
  KengakuR37 reported it. Restored at ~02:30 with `git checkout HEAD -- <6 paths>`; afterwards 0 tracked files
  are deleted, and jj `@` carries no deletion. Cause is not identified: jj fleet commits are pathspec-limited
  with `auto-track=none()` and the jj op log has no matching op, so a seat shell command is the likely cause.
- 2026-10-26 02:13:52: seat RefetchS077 made a stray fleet commit c16a334f ("A"). It reset to 9b84562b at
  02:14:19 (reflog). The commit is unreachable and was never pushed.
- Seats wrote stray fleet-root files and removed them themselves (GateCitations report; RefetchS096
  body.b64/body.cc). Several seats report `TMPDIR`/`HYAKU_SCRATCH` unset in the seat env, so files leak to /tmp.
- 2026-10-26 06:22:18: the MadoR43 L1-exit handler failed with `RuntimeError('Background job limit reached (100)')`
  after `verify` and `closure` succeeded. The mado r43 closure prompt was committed in
  34057c5334bf3cd84c026f155b7a78017f2365ff, but the judge was never spawned. `.ufo/state/inline-dispatcher.log`
  has no `drive` tick between 06:22:15 and 08:29:36, so no wave moved in that window: kama r45 w1 stalled at
  32/64 seats spawned, tabi r31 w1 was never finalized (all 32 reports were on disk from 06:07), and the
  tabi r31 and souji r32 w2 waves were never taken.
- From ~06:15 the host was saturated. MoriR50 reported load ~45. A `proc://` read took 30 s. The bash tool
  backend stopped answering for seats and for the orchestrator. Seats sat at "no turn in flight" for 50-85 min.
- ~08:2x: two eval-cell timeouts wiped the orchestrator kernel. ~08:50: the omp process exited, which ended
  every live agent: L1s SoujiR32, TabiR31, TameshiR48 and MoriR50, plus their seats. The run stopped about
  4 h early (planned end ~13:00).
- KamaR45 landed before the crash with 0 working seats; the L1 did the build work itself. Report:
  277ee2ef32435155212d48b1711413305f017bc3. Lane head: 0fddf257a0c574dc4a29106602fcfb489e6f7376. C1 met,
  C2 not met.

## Run end (operator stop after the host crash, 2026-10-26 ~09:00)

- Closures this run: MANIFEST `rounds[733..749]`, 17 rows. 11 admitted: kasegi 33/34, kengaku 37/39,
  kaidoku 36, tsukuroi 38/39/40, tabi 29/30, kama 44. 6 rejected: souji 30/31, kaidoku 37/38, kengaku 38,
  kasegi 35.
- Claims still open in `~/.local/state/shokunin-hyaku/claims/`. These are Phase 0 for the next run:
  - mado r43: landed. Report 906cfe709b7f539375942336b3bb4ce1171834fb. Owed: a judge on the committed
    `.ufo/prompts/closure/mado-round-43.md`.
  - kama r45: landed. Owed: `inline.sh closure kama`, then a judge.
  - souji r32, tabi r31, tameshi r48 and mori r50: unlanded attempt 1. A retry is `inline.sh dispatch <lane>`,
    which runs attempt 2 on the same base.
- Orchestrator salvage commits (jj-lane.sh, pathspec-limited, pushed). They preserve unlanded working-tree
  state for the retries:
  - tabi: ae15a37ee8aa43964179a676a087604368cd1c41
  - souji: 4e56c48b8fc828f9aba2746e324dc46aa538bdbf
  - mori: 9b8562a371dc916fdc0fc686619ea1e271a3e118
  - tameshi: 15b1521ea2e95d0d708059458c090e9f334adf32. This one includes the L1's draft round-48 LOG.md and
    QUALITY.md appends; a retry corrects them by appending.
  - kama: a553bd7cdfb72b69431beed04e71173520bab715
  - kake: 044048597d62f3199494b63b36e90dd57825e350 (late r57 seat artifact)
  - kasegi: cc692008b0cfd58d18275aa6c4aed79620120799. A run-7 seat left the r30 `ScribeLesson.md` at the fleet
    root; it was moved into the lane.
  - kengaku: d3a6277f188434458e1d2ce04aff59392c6f0dc6 (marker)
  - kotoba: 65a5c7a663249e0522cc49e4a148424200d9ddfe (marker)
- Abandoned-wave markers: `<wave>.ready.dispatched` files whose text starts with `ABANDONED`. They stop a fresh
  dispatcher from spawning seats that have no live L1. Covered waves: kama r45 w1, tabi r31 w2, souji r32 w2
  (gitignored, so local only), kengaku r36 falsify, and kotoba r74 w2. A retry L1 dispatches under a new wave
  name.
- Removed: the fleet-root stray `demo-cwd.txt` (a 30-byte `pwd` output) and mori's
  `.ufo/waves/round-40/scratch/` selftest temp dirs.
- Lesson for run 9: watch `proc://` entry count against the ~100 cap before every handler spawn. Keep live
  agents well below the cap; ~92 live agents wedged the host. Keep controller state on disk
  (`/fast/scratch/hyaku-run8/controller.py`), because a kernel loss wiped `ACTIVE`/`ROT`/`PARTIAL`.
- Cleanup before the next run (2026-10-26 ~09:00-09:30):
  - Correction to the "Removed" entry above: only the untracked `mori-conform-selftest-*` dirs under mori's
    `.ufo/waves/round-40/scratch/` were removed. The first `rm` also deleted 8 tracked files there; they were
    restored with `git checkout HEAD -- .ufo/waves/round-40/scratch`, and mori is clean.
  - Killed an orphan process group (pgid 1932374) that the dead TameshiR48 L1 had started:
    `measure.py --emit`, six profiles of `tally-audit-v3.py`. It was still writing selftest dirs into /tmp.
  - Worktrees:
    - kake: removed `/fast/scratch/kake53/exec-cross-citation` and `exec-quality-gate`. Their unintegrated
      round-53 state was first committed on the local branches as
      3ed0f7d6dd251a858076342542c294c7d96e8a25 and 958f46d1d258346a789410eea47cadd72c26ca59.
    - game-dev-2d: wt-r98, wt-r99 and wt-r100 were pushed to origin as branches (they lifted the souji r5 lock
      condition), then unlocked and removed. The branches are kept.
    - Stale worktree metadata pruned in kengaku (1 entry) and prymeagnt (4 entries).
  - Disk:
    - `disk-guard.sh sweep --all` with TARGET_PCT=1 and IDLE_MIN=1. Keep list:
      `/fast/scratch/hyaku-run8/disk-guard.keep` (omp runtime dirs, kimi-webbridge, ZCode dirs).
    - Removed by hand: idle plain files in /tmp and /var/tmp, `/fast/scratch/hyaku/kumitate-pin` (its dirs were
      read-only), and closed-round lane scratch outside the guard root (kama-r41/42/43, mado-r33-k2-receipts,
      mado-r35, c1r42/c2r42/c2ctl, r41a13, r41b04-tmp, revenger-r70, tabi-r19, tameshi-r39-w1,
      kasegi-r33-l1, m18-selfheal).
    - Space: /fast 218G → 177G used; `/fast/scratch/hyaku` 38G → empty; /var/tmp 7.7G → 1.6M.
  - Caches:
    - ~/.cache: removed seat strays (`PROVINCE.md`, `kake-r39a3-priv.path`, `cl65/`, `kama-shokunin/`), stale
      `chromium-headless/scoped_dir*` profiles, the pip cache, and the old playwright build
      (chromium/headless_shell 1194, ffmpeg 1011). About 1.3G freed, per-item `du` before removal; ~/.cache is
      now 4.4G.
    - ~/.cache/uv was NOT cleaned. Four `uvx mcp-for-blender` servers owned by the live ZCode CLI session hold
      its lock and run from `~/.cache/uv/archive-v0`.
  - Kept: `/fast/scratch/hyaku-run7` and `hyaku-run8` (the run-7 and run-8 records cite them), plus the
    six claims listed above (Phase 0 of the next run).

## Phase 0 resolution (2026-10-26 ~09:20-11:50, operator-directed)

| Round | Outcome | `rounds[]` |
|---|---|---|
| kama r45 | rejected | 750 |
| mado r43 | admitted | 751 |
| tabi r31 (attempt 2) | admitted | 752 |
| souji r32 (attempt 2) | rejected; souji now BLOCKED (3 rejects in a row: r30, r31, r32) | 753 |
| mori r50 (attempt 2) | admitted | 754 |
| tameshi r48 (attempt 2) | not landed | — |

- tameshi r48: the attempt-2 L1 stopped committing after 10:28 and never filed. At operator wrap-up its 8
  straggler seats and the L1 were killed, and `inline.sh fail` recorded attempt 2/3 as RETRYABLE. The claim
  stays open, so the next run's Phase 0 is `inline.sh dispatch tameshi` (attempt 3, the last before the
  lane is blocked). Its unlanded receipts and a2w1 wave were salvaged in
  8f2922b8d8615e26d382e775bd9821fdd9204130. Note that c1-controls, after/ and the c94-96 falsifiers did run.
- Orchestration lesson, operator 2026-10-26: Phase 0 ran with HOST_JOB_CAP=60. That was too low and too
  slow. The swarm ceiling is 256 seats; aim for 64-128 dispatched seats per round. The polling drive loop
  (`drive()`/`run_loop`) was slow and fragile: kernel state was lost on every interrupt. Replace it before
  the next run.
