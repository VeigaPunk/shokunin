# hyaku (百) campaign — handoff (wrapped 2026-10-20 by operator directive)

Integrator-of-record artifact for the in-session training campaign started 2026-10-19 23:10 -03.
Everything a fresh session needs to resume is here or in `scripts/hyaku/`; the orchestrator's
session notes do not survive the reboot.

## Operator directives (verbatim, in order)

1. "train all shokunins to at least round 100; … 2-3 different shokunins trainings concurrently, each
   should have their own session, under their own repo. | swarm with high concurrency, using m_flash,
   m_luna, m_zfl, m_antigravity, m_haiku; the concurrency should be 64-100, per round | keep doing
   it, commit and push after every round done."
2. "i want you tro launch waves of 32-64 actually"
3. "you can also use m_opus on the swarms"
4. "do it inline, the way you are doing doesnt seem like it's working." / "do it inline with multiple
   swarms of subagents"
5. "increase depth of subagent spawn from 2 to 3 in omp global settings" (declined at the cfg prompt
   at 00:4x; later re-requested "enabled depth from 2 to be 3 on omp" → saved globally 04:2x)
6. "increaase concurrency to 64-128 subagent swarms" / "we are on the goal of pushing every shokunin
   to 100 rounds of training, through swarm rounds of 64-128"
7. "/skill:swarm you need to swarm with more concurrency /skill:tower"
8. "feel free to use m_sol also (should be gpt-6.1-sol max effort) …" / "and m_swe on code heavy tasks"
9. "we will be wrapping up this training run; commit and push as lanes finish; i'll be rebooting the
   pc afterwards. do not spawn more workers" / "please restore the backup of the agent.db on omp" /
   "commit and push to the remotes after you are done"

## How the campaign ran

- Each lane round = one in-session L1 `task` subagent (generic `task` agent → `@m_strong`) reading
  `.ufo/prompts/<lane>-round-<N>.md` = canonical `templates/round-prompt.md` + `scripts/hyaku/lane-addendum.md`.
- Each landed round = one fresh non-author closure `task` subagent reading
  `.ufo/prompts/closure/<lane>-round-<N>.md` (`scripts/hyaku/closure-prompt.md`), which writes
  `<lane>/corpus/lessons/round-<N>-verifier-spotcheck.md` and appends the MANIFEST closure via
  `scripts/hyaku/append-closure.py` (byte-exact serialization, duplicate guard, fleet lock).
- Mechanics: `scripts/hyaku/inline.sh queue|dispatch|verify|fail|closure|closed|advance`; fleet-repo
  commits only through `scripts/hyaku/fleet-commit.sh` (flock + lane identity + push).
- State (survives reboot): `~/.local/state/shokunin-hyaku/` — `next/<lane>` next round,
  `claims/<lane>/{round,attempt,base,dispatched}` claimed round, `outcome/<lane>-r<N>`,
  `last/<lane>` dispatch time (queue tie-break), `events.log`.
- Lane concurrency: 3 (start) → 6 (04:5x, operator "more concurrency"). Swarm band: v1 32–64
  (`scripts/hyaku/ufo-wave-policy.json`) → v2 64–100 per wave (`ufo-wave-policy-v2.json`) with an
  optional v1 falsify wave 2, round total ≤128 (validator hard-caps one wave at 100).

## Resume after reboot

1. Read this file, `scripts/hyaku/lane-addendum.md`, `scripts/hyaku/closure-prompt.md`.
2. Re-apply the session settings below (they were session-only).
3. Pay the closure debt (section "Wrap-up state") first: for each lane with a claim and a landed
   report, run `scripts/hyaku/inline.sh closure <lane>`, dispatch the closure task, then
   `inline.sh advance <lane>`. Lanes with a claim but no landed report: `inline.sh fail <lane>
   "ended by operator wrap-up"` and re-dispatch (`inline.sh dispatch <lane>`).
4. Loop: `inline.sh queue` → `dispatch` → L1 task → `verify` → closure + next-lane batch → `advance`.

### Session settings used (session-only, NOT saved — re-apply via cfg:// in the new session)

- `task.agentModelOverrides` (final): executor→@m_swe; scout, labrat→@m_fast; connector, reviewer,
  scribe, simplifier, distiller→@m_haiku; critic, sentinel→@m_opus; mutation-tester→@m_sol;
  planner, revenger→@m_luna; task, main→@m_strong.
- `retry.fallbackChains.m_swe` = ["opencode-go/deepseek-v4.1-flash", "devin/deepseek-v4-1-flash"]
  (global value is []).
- `task.maxConcurrency` 800; `async.maxJobs` 800; `task.agentSoftRequestBudget` {"task":1500}.
- Saved globally: `task.maxRecursionDepth` 3 (operator request).
- `async.maxJobs` is read at process start: the session ran with a hard cap of 100 running background
  jobs (a `task` call is refused while ≥100 run). Save it globally BEFORE starting the next session to
  lift that cap.

### Provider status at wrap-up (2026-10-20 ~06:00 -03)

- m_flash (charm-hyper/deepseek-v4.1-flash): credits exhausted (HTTP 402); seats die without falling back.
- m_antigravity: antigravity rejects this session's tool schemas (400 on `if`/`then`); its Cursor Gemini
  fallback hit the monthly limit (reset 11/18).
- m_zfl (zai/glm-5.3-flash): weekly quota until 2026-10-20 23:02.
- Codex (m_strong L1s, m_sol, m_luna): `turn_rate_limit_exceeded` when critics ran on m_sol — keep
  Codex seats ≤4 per wave.
- Fresh-process probes after the credential restore (05:59): m_haiku, m_opus, m_strong, m_fast, m_swe
  all answered from their primary provider.

## Incidents

1. **omp credential store corruption (02:40:33).** The 5-minute `ai-usage.timer` omp process found
   `~/.omp/agent/agent.db` malformed and quarantined it (`agent.db.corrupt-1792474833850-…`); the fresh
   store had 0 credentials, so every new omp process was unauthenticated while this session kept its
   in-memory credentials. Recovered copy (sqlite `.recover`, integrity ok, 22 credentials / 12
   providers): `agent.db.recovered-20261020T034408`. **Restored 05:59 on operator request** through the
   SQLite backup API (`.restore`, live WAL database held open by an interactive omp), 2191 frames
   checkpointed; pre-restore snapshot `agent.db.pre-restore-20261020T055856`. Root cause unknown.
2. **Host partial upgrade (04:25:16, mado r15 seat).** `pacman -S --needed --noconfirm libinput
   libinput-tools` upgraded libinput 1.31.3-1 → 1.32.0-1 on a host 413 packages behind its sync DB
   (last `pacman -Sy` 2026-10-18 14:11). ABI-clean at check time (soname libinput.so.10, `ldd -r` 0
   unresolved, aquamarine links it); revert package in cache. Not reverted — operator decision (L0).
   Orchestrator ruling: all pacman transactions paused host-wide pending that decision.
3. **Seat misroots.** Seat tools start at the fleet root; relative `Report:` trailers landed files in
   the fleet repo (kama r11, tsukuroi r12, tabi r15, mado r16). Each was copied byte-exact into its
   lane, verified with `cmp`, and the fleet copy removed. Addendum §6.3 now has L1s sweep and repair
   their own misroots before reporting.
4. **Job cap.** Several 64-seat waves were refused whole ("Background job limit reached (100)") and
   retried every ~3 minutes until admitted.

## Results (non-author hyaku closures in MANIFEST.json rounds[322..348])

27 closures: 22 admitted, 5 rejected-harmed (tsukuroi r12, mori r13, tsukuroi r13, mado r15,
souji r14). Mori and tsukuroi repaired their routed harms in the next round and were admitted; souji
r15 was dispatched repair-first; mado r15's harm is the host incident above.

## Wrap-up state (2026-10-20 ~06:20 -03)

Rounds landed this campaign (report committed + lane pushed; remote heads verified with `git ls-remote`):

| lane | rounds landed | hyaku closures (rounds[] index) | closure debt | next round | lane HEAD (pushed) |
|---|---|---|---|---|---|
| kama | r11–r15 | r11–r15 admitted [322,326,330,337,346] | — | 16 | `20e392ea6` |
| tameshi | r12–r15 | r12–r15 admitted [323,329,338,348] | — | 16 | `28aeef498` |
| tsukuroi | r12–r16 | r12, r13 rejected-harmed [324,331]; r14, r15 admitted [336,344] | **r16** | 16 → 17 after closure | `f871697aa` |
| tabi | r12–r15 | r12–r14 admitted [325,334,341] | **r15** | 15 → 16 after closure | `36240c70e` |
| mado | r13–r16 | r13, r14 admitted [328,335]; r15 rejected-harmed [342] | **r16** | 16 → 17 after closure | `4bfb2363a` |
| mori | r13–r16 | r13 rejected-harmed [327]; r14, r15 admitted [339,345] | **r16** | 16 → 17 after closure | `9de05bdbc` |
| souji | r13–r15 | r13 admitted [333]; r14 rejected-harmed [343] | **r15** (author: both claims unprovable — acceptance unrun at wrap-up; r14 harm still open) | 15 → 16 after closure | `b410186ce` |
| kaidoku | r14–r16 | r14–r16 admitted [332,340,347] | — | 17 | `b563c799d` |
| kake | r21 | — | **r21** | 21 → 22 after closure | `c2d8da86d` |

Not reached this campaign (lowest-round-first order): kagi 22, kasegi 23, chousa 25, kengaku 25,
kumitate 35, kotoba 47, kotodama 50, revenger 61. Already ≥100 before the campaign: audio,
game-dev-2d, game-dev-3d, lore.

**Closure debt** (landed, no non-author closure yet — `~/.local/state/shokunin-hyaku/claims/<lane>`
still holds round/base): tsukuroi r16, tabi r15, mado r16, mori r16, kake r21, souji r15. Run
`scripts/hyaku/inline.sh closure <lane>` → closure task → `inline.sh advance <lane>` for each.
Routed items to carry into those closures: tabi r15 asks for a non-author erratum to the round-14
verifier wording (frozen `aria-loopback.spec.mjs:269` + `:924` vs launcher `runtimePinStatus`); souji
r15 is the repair round for r14's value-blind config refusals; mado r16 notes the r15 host harm stays
operator-owned.

**Operator decisions open (L0, `.ufo/l0-questions.md`):** libinput partial-upgrade remediation (keep
1.32.0 / revert from cache / full `-Syu` through tsukuroi's /sysroot update-safety gate) and the
host-wide pacman pause (tsukuroi r15 host-recovery question). Rebooting loads libinput 1.32.0 into
Hyprland for the first time — the first live test of that mixed state. No boot-chain package changed
tonight (pacman.log: only libinput was upgraded), so rebooting as-is is safe. Do NOT run `pacman -Syu`
before rebooting without tsukuroi's gate: pending are `mkinitcpio` 41.1→42.2 (the /sysroot move the
host's `btrfs-overlayfs` and `plymouth` hooks do not expect), `systemd` 261→262, `plymouth`, `linux`
7.2.11 and `glibc`.

Late-found seat notes: three agent-to-L1 notes that seats wrote as plain files at the fleet root
(`MoriR16.Lesson`, `SoujiR15`, `TameshiR15`, outside the `.ufo/` sweep pathspec) are archived
byte-for-byte under `.ufo/waves/hyaku/misroots/` — evidence for the mori r16, souji r15 and tameshi
r15 closures. Future misroot sweeps should check `git -C <fleet> status --porcelain` with no pathspec.

## Latest wrap checkpoint — 2026-10-22

The tables and launch instructions above are historical, not current dispatch
permission. Read `PHASE2.md`'s final session-wrap section and
`session-wrap-20261022.json` in this directory before any continuation.

Operator requested session wrap and jj publication. Training is paused.
Completed measured work and the prior64-agent publication audit are preserved;
Mori24/Tameshi25 proposed freezes and Kaidoku25 author finalization remain private
and unlanded. Kotoba48 has real I/before but no approved F/candidate.
Tsukuroi24 has real D but no measuring I; obey its recorded429 backoff.
Kake28 requires qualified distillation and judgment before any implementation.

All safety/source/rejection holds remain. A successful command or completed
native identity is not admission, actor conformance, privacy clearance or a
completed100-round campaign. Preserve unfinished worktrees; no replacement
workers, retry/reroute of held items, cleanup or host/service action is implied.

## Phase-3 leg wrap — 2026-10-22 (supersedes the checkpoint above for current state)

The 12-hour phase-3 leg (T0 07:56:36Z) is wrapped. Read, in order:
`.ufo/waves/hyaku/PHASE3.md` §"Session wrap (2026-10-22T19:35Z …)" and
`.ufo/waves/hyaku/session-wrap-20261022-phase3.json` (schema `hyaku-session-wrap-v1`).
The contract was `.scratch/goal-20261022-hyaku-12h.md`.

- MANIFEST `rounds[441..478]`: 37 in-session closures, 27 admitted, 9 honest-stop, 1 harmed.
  No claims are in flight.
- Eligible next, in order: kake r33, tsukuroi r29, kotodama r55, kumitate r42, mori r29,
  kotoba r53 (different frontier area), kaidoku r29 (repair-first).
- Driver-blocked, needing operator unblock: tameshi (r28, new), chousa, kama, mado.
  Held by the operator: kagi, revenger, souji, tabi, kasegi, kengaku. Item holds are listed in the wrap.
- Routing and limits changed by the operator this leg (saved globally): see the wrap JSON
  `operator_config_changes_this_session`. omp 18.12.6 still clamps running jobs at 100 per
  spawning session tree. Reset `~/.local/state/shokunin-hyaku/wave-cap` (128 at wrap) and
  `live-session-dir` for the next session.
- No promotion and no round-100 completion is claimed.
