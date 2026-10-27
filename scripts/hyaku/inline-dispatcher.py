# hyaku in-session dispatcher — the driver half of scripts/hyaku/inline.sh.
#
# WHAT: this is NOT a CLI. The orchestrator (main omp session) loads it into the
# session kernel, where the seat API lives:
#     %load scripts/hyaku/inline-dispatcher.py        (or the absolute path)
# Everything here reaches the host through session globals (`agent()`, `tool`,
# AgentHandle objects), so it only runs inside the session that owns the seats —
# no `__main__`, no subprocess entry point, no import from a test harness.
#
# LANE CYCLE (one lane round; the orchestrator drives every step):
#     inline.sh queue                 eligible lanes, lowest next round first
#     inline.sh dispatch <lane>       claim + render prompt + baseline + evidence
#     spawn_l1(lane, rnd)             L1 `task` seat, label <Lane>R<rnd>
#     drive()                         poll every <wave>.ready, register() its
#                                     seats as host slots free up, finalize()
#                                     each settled wave to <wave>-results.json
#                                     and message the L1 "WAVE-DONE"; returns
#                                     as soon as an L1 or closure seat exits
#     inline.sh verify <lane>         report landed / committed / pushed?
#     inline.sh closure <lane>        render + commit the closure prompt
#     spawn_closure(lane, rnd)        fresh non-author closure judge
#     inline.sh closed <lane>         hyaku closure rows + outcome
#     inline.sh advance <lane>        next=round+1, release claim, purge scratch
# bootstrap() rebuilds WAVES/L1S/CLOS after a kernel restart.
# Driving pattern (run 7; worked, run 8's long blocking drive loop did not): run ONE short
# `await tick()` per wake-up, never a multi-minute drive()/loop cell. Wake-ups are seat/L1/
# closure completions (host-delivered) plus scripts/hyaku/ready-watch.sh as an async bash
# job that exits when a .ready lacks .dispatched; an interrupted long cell wipes the kernel.
#
# NEVER run this driver and scripts/shokunin-watchdog.sh together: they spawn the
# same lanes into the same round state and double-drive every lane (AGENTS.md:
# one driver per fleet root). The watchdog respawns a process per round; this
# file is the in-session orchestrator.
#
# DISK GATE (operator directive 2026-10-25: every long run ended with /tmp at
# 100 %): before any seat spawn register() asks scripts/hyaku/disk-guard.sh
# `check`, sweeps once through the same guard, and defers the whole wave while
# it still reports pressure (the wave stays unregistered and the next tick
# retries); drive() sweeps every DISK_SWEEP_EVERY seconds. HYAKU_DISK_GUARD
# overrides the guard path; a missing guard is a logged warning and spawns
# continue, so the driver works on hosts without the guard.
#
# HOST GATE (run 9, after run 8 wedged the host at ~92 live agents, load ~45 on 32 cores):
# seats spawn only while fewer than SEAT_CEILING jobs are running (omp's own hard cap is
# 100 running jobs), the 1-min load is <= LOAD_MAX and MemAvailable >= MEM_MIN_GB; otherwise
# the wave waits for the next tick. FILL STATE ON DISK: a wave that fills across ticks keeps
# {seat: job id} in <wave>.ready.partial and, once full, on the second line of
# <wave>.ready.dispatched, so bootstrap() after a kernel loss resumes the fill without
# re-spawning seats and tracks liveness by job id. A ready whose L1 is not running is never
# spawned (tick status lists it as an orphan).
#
# Contract: the L1 writes <lane-repo>/.ufo/waves/round-N/<wave>.ready
# {lane,round,wave,dispatch,l1}; we spawn every taskCall.tasks[] seat inline,
# mark <ready>.dispatched, and when no seat is live write
# <dispatch-dir>/<wave>-results.json and message the L1 "WAVE-DONE".
# drive() returns on L1/closure exit events.
#
# NOTE ON ASYNC: proc_state()/running_names() (and the other tick functions) are
# async because they read proc:// through the session tool API. Inside %load
# cells await them (`await drive()`); from sync code use asyncio.run(...). The
# disk helpers are plain sync functions (subprocess) and are pushed onto a thread
# by the async callers so a bounded `du` sweep never stalls the tick loop.
import glob, json, os, re, subprocess, time, asyncio

FLEET = '/home/vgpnk/Projects/shokunin'
LOGF = os.environ.get('HYAKU_DISPATCH_LOG') or os.path.join(FLEET, '.ufo/state/inline-dispatcher.log')
WAVES = globals().get('WAVES', {})      # ready path -> {meta, names, handles, l1, done}
L1S = globals().get('L1S', set())       # L1 agent names to watch
CLOS = globals().get('CLOS', {})        # lane -> closure agent name
HANDLES = globals().get('HANDLES', {})  # name -> AgentHandle (for outputs)

# Disk guard (layer 1/2). The guard owns the policy (roots, thresholds, liveness,
# exclusions); this driver only asks it questions and obeys rc.
DISK_GUARD = os.environ.get('HYAKU_DISK_GUARD') or os.path.join(FLEET, 'scripts/hyaku/disk-guard.sh')
DISK_CMD_TIMEOUT = 900   # kill a wedged guard instead of stalling the tick loop
DISK_SWEEP_EVERY = 600   # drive() background sweep cadence (s); the guard decides per root

def dlog(*a):
    os.makedirs(os.path.dirname(LOGF), exist_ok=True)   # .ufo/state is driver runtime (never committed)
    with open(LOGF, 'a') as f:
        f.write(time.strftime('%Y-%m-%dT%H:%M:%S') + ' ' + ' '.join(str(x) for x in a) + '\n')

L1_PROMPT = """/skill:godspeed

# Target
Lane {lane}, round {rnd} (attempt {attempt}). Lane repo: {FLEET}/{lane}-shokunin.
# Change
Read {FLEET}/.ufo/prompts/{lane}-round-{rnd}.md in full and execute it end to end. Your agent id for ready files is `{label}`.
Waves spawn in the orchestrator session via the inline spawn handoff (addendum §6 run-7 block): never call task yourself. YOU write <lane>/.ufo/waves/round-N/<wave>.ready (JSON: lane, round, wave, dispatch abs path, l1 = your agent id) after validating; the orchestrator polls for it, spawns the seats, and messages you WAVE-DONE. `wait` may return early when nothing is pending — call it again or keep doing round work; never give up for lack of a handoff. Do not file the report before WAVE-DONE for every wave you launched. Size the round 64-128 seats total (addendum §6 run-10 block; 256 is the hard ceiling). At most ~90 seats run at once across all lanes (omp caps a session at 100 running agents), so waves queue and a large wave fills in tranches as slots free.
You own the whole round: protocol load, claim choice and freeze with controls, specs, validation, integration, landing, report. Nobody supplies claims. Never message agent://all; message only your own seats by id.
# Acceptance
Report {FLEET}/.ufo/reports/round-{rnd}/{lane}.md committed via fleet-commit.sh --as {lane}; lane pushed (ls-remote shows final hash). Never end your turn before that.

Tooling authorization (operator, 2026-10-19): you and every seat may install/upgrade tools that help the task; first read /home/vgpnk/.omp/agent/RULES.md (official channels, update-safety gate; record tool/version/channel/reason). pacman stays paused per the addendum guard.
"""

# Appended to every seat prompt (run 9: a kengaku seat planted ~/.local/bin/git; a kasegi fixture
# driver wrote relative paths before cd and truncated the fleet root's LOG.md and SCORECARD.md).
SEAT_GUARD = f"""

# Host guard (orchestrator; applies to every seat)
- Your process cwd is the fleet root {FLEET}: not your lane, not your scratch. Use absolute paths, or `cd` into your own scratch dir before any command or fixture driver that writes a relative path.
- Before any git/jj mutation in a fixture or clone, assert `git rev-parse --show-toplevel` prints that fixture dir.
- Never create, modify or delete anything in ~/.local/bin or any other PATH directory, and never write a fleet-root tracked file (LOG.md, SCORECARD.md, MANIFEST.json, ...). Write only the paths your seat spec names plus your own scratch.
"""

HOST_JOB_CAP = 100   # omp 18.12.6 clamps async.maxJobs with Math.min(100, ...) and refuses a new job while
                     # 100 jobs are running; queued, completed and service entries do not count
SEAT_CEILING = int(os.environ.get('HYAKU_SEAT_CEILING', '96'))   # running jobs at which seat spawns stop
                     # (operator run 9: "more concurrency"); the 4 below HOST_JOB_CAP keep L1 / closure spawns possible
LOAD_MAX = float(os.environ.get('HYAKU_LOAD_MAX', str(2.25 * (os.cpu_count() or 8))))
MEM_MIN_GB = float(os.environ.get('HYAKU_MEM_MIN_GB', '4'))
PARTIAL = globals().get('PARTIAL', {})  # ready path -> {seat name: AgentHandle | _Spawned} while a wave is still filling

class _Spawned:
    """A seat whose handle was lost with the kernel: liveness by job id, no output."""
    def __init__(self, id):
        self.id = id

def _ids(spawned):
    return {n: getattr(h, 'id', None) for n, h in spawned.items()}

def _save_partial(ready, spawned):
    tmp = ready + '.partial.tmp'
    with open(tmp, 'w') as f:
        json.dump(_ids(spawned), f)
    os.replace(tmp, ready + '.partial')

def host_ok():
    """True while the host can take more seats (1-min load and MemAvailable within bounds)."""
    try:
        load1 = float(open('/proc/loadavg').read().split()[0])
        mem_gb = next(int(l.split()[1]) for l in open('/proc/meminfo') if l.startswith('MemAvailable:')) / 1048576
    except (OSError, ValueError, StopIteration):
        return True
    if load1 > LOAD_MAX or mem_gb < MEM_MIN_GB:
        dlog('host-pressure', f'load1={load1}', f'mem_avail_gb={mem_gb:.1f}')
        return False
    return True

# --- disk guard hooks -------------------------------------------------------
def _disk(argv):
    """Run `disk-guard.sh <argv>`; None when the guard is absent or cannot run."""
    if not os.path.exists(DISK_GUARD):
        dlog('disk-guard-missing', DISK_GUARD)
        return None
    try:
        return subprocess.run(['bash', DISK_GUARD] + argv, capture_output=True, text=True,
                              timeout=DISK_CMD_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as e:
        dlog('disk-guard-error', ' '.join(argv), repr(e))
        return None

def disk_ok():
    """True = every configured root is below SOFT_PCT and spawning may proceed.

    rc 0 -> True; rc 1 -> False (pressure); rc 2 or unreadable output -> True with
    a dlog warning (a broken guard must not stall the fleet); missing guard -> True
    with a dlog warning.
    """
    p = _disk(['check'])
    if p is None:
        return True
    if p.returncode == 1:
        dlog('disk-pressure', ' '.join((p.stdout or '').strip().splitlines()[:3]))
        return False
    if p.returncode != 0:
        dlog('disk-guard-warn', 'check rc=%d' % p.returncode,
             (p.stderr or p.stdout or '').strip()[:300])
    return True

def disk_sweep(emergency=False):
    """One guarded sweep; returns the guard rc (None when the guard is absent). Never raises."""
    p = _disk(['sweep', '--emergency'] if emergency else ['sweep'])
    if p is None:
        return None
    lines = [l for l in (p.stdout or '').splitlines() if l.strip()]
    dlog('disk-sweep', 'emergency' if emergency else 'normal', 'rc=%d' % p.returncode,
         (lines[-1][:300] if lines else ''))
    return p.returncode

async def proc_state():
    """(running job names, running job count). The host cap counts running jobs only."""
    r = await tool.read({'path': 'proc://'})
    txt = r.get('text', '') if isinstance(r, dict) else str(r)
    run = {m.group(1) for m in re.finditer(r'^(\S+) \[\w[\w-]*\] (?:— )?running', txt, re.M)}
    return run, len(run)

async def running_names():
    run, _ = await proc_state()
    return run

def live(name, run):
    """Live under its own name, a runtime-deduplicated id (<name>-N, <name>-N-M), or an attempt respawn (<name>aK...)."""
    return bool(name) and (name in run or any(re.fullmatch(re.escape(name) + r'(a\d+)?(-\d+)*', x) for x in run))

def seat_live(w, name, run):
    """Liveness by spawned handle id when we have it (cross-lane seat names collide); by name otherwise."""
    h = (w.get('handles') or {}).get(name)
    return (h.id in run) if h is not None else live(name, run)

def spawn_l1(lane, rnd, attempt=1):
    label = f'{lane.capitalize()}R{rnd}' + (f'a{attempt}' if attempt > 1 else '')
    h = agent(L1_PROMPT.format(lane=lane, rnd=rnd, attempt=attempt, label=label, FLEET=FLEET), agent='task', label=label)
    HANDLES[label] = h; L1S.add(label); dlog('l1', label)
    return label

def spawn_closure(lane, rnd):
    label = f'Close{lane.capitalize()}R{rnd}'
    p = (f'You are a hyaku non-author closure judge. Read {FLEET}/.ufo/prompts/closure/{lane}-round-{rnd}.md in full '
         'and execute it exactly, end to end. Never end your turn before the MANIFEST rounds[] entry is committed and pushed; '
         'end with the one-line CLOSURE verdict plus a short bullet digest.')
    h = agent(p, agent='task', label=label)
    HANDLES[label] = h; CLOS[lane] = label; dlog('closure', label)
    return label

def adopt(ready):
    """Track an already-dispatched wave whose handles were lost (kernel restart)."""
    meta = json.load(open(ready)); d = json.load(open(meta['dispatch']))
    lines = open(ready + '.dispatched').read().splitlines()
    try:
        ids = json.loads(lines[1]) if len(lines) > 1 else {}
    except ValueError:
        ids = {}
    WAVES[ready] = {'meta': meta, 'names': [t['name'] for t in d['taskCall']['tasks']],
                    'agents': {t['name']: t['agent'] for t in d['taskCall']['tasks']},
                    'handles': {n: _Spawned(i) for n, i in ids.items() if i}, 'done': False, 'adopted': True}
    dlog('adopted', ready, len(ids))

async def register(ready, run, occupied):
    """Spawn a wave's seats incrementally as host slots free up. Returns (registered, seats spawned now):
    registered is True once every seat is spawned (wave in WAVES, .dispatched written).

    Disk and host gates: an unregistered wave is the cheapest thing to hold — on disk
    pressure we sweep once and defer; on host pressure we defer. A deferred or partial
    wave keeps <ready>.partial fresh, which tells ready-watch.sh it is being driven."""
    mine = PARTIAL.setdefault(ready, {})
    if not await asyncio.to_thread(disk_ok):
        await asyncio.to_thread(disk_sweep)
        if not await asyncio.to_thread(disk_ok):
            dlog('disk-defer', ready)      # wave stays unregistered; retried next tick
            _save_partial(ready, mine)
            return False, 0
    if not host_ok():
        dlog('host-defer', ready)
        _save_partial(ready, mine)
        return False, 0
    meta = json.load(open(ready)); d = json.load(open(meta['dispatch']))
    tc = d['taskCall']; tasks = tc['tasks']
    todo = [t for t in tasks if t['name'] not in mine]
    room = SEAT_CEILING - occupied
    n = 0
    for t in todo[:max(room, 0)]:
        prompt = tc.get('context', '') + f"\n\n# Seat {t['name']}\n" + t['task'] + SEAT_GUARD
        try:
            h = agent(prompt, agent=t['agent'], label=t['name'])
        except RuntimeError as e:          # host cap hit mid-batch; resume next tick
            dlog('spawn-cap', ready, t['name'], repr(e)); break
        mine[t['name']] = h; HANDLES[t['name']] = h; n += 1
        _save_partial(ready, mine)         # each agent() spawn takes ~1 s: an interrupted tick keeps its fill
    if len(mine) < len(tasks):
        _save_partial(ready, mine)
        dlog('partial', meta['lane'], meta['round'], meta['wave'], len(mine), len(tasks))
        return False, n
    with open(ready + '.dispatched', 'w') as f:
        f.write(time.strftime('%Y-%m-%dT%H:%M:%S') + '\n' + json.dumps(_ids(mine)) + '\n')
    WAVES[ready] = {'meta': meta, 'names': [t['name'] for t in tasks],
                    'agents': {t['name']: t['agent'] for t in tasks}, 'handles': dict(mine),
                    'done': False, 'adopted': False}
    PARTIAL.pop(ready, None)
    try:
        os.remove(ready + '.partial')
    except OSError:
        pass
    dlog('spawned', meta['lane'], meta['round'], meta['wave'], len(tasks))
    return True, n

def seat_output(name, w=None):
    h = ((w or {}).get('handles') or {}).get(name) or HANDLES.get(name)
    if h is None or isinstance(h, _Spawned):
        return None
    try:
        return str(h.output())[:20000]
    except Exception as e:
        return f'<output unavailable: {e!r}>'

async def finalize(ready, w):
    m = w['meta']
    out = os.path.join(os.path.dirname(m['dispatch']), f"{m['wave']}-results.json")
    res = []
    for n in w['names']:
        o = seat_output(n, w)
        res.append({'name': n, 'agent': w['agents'][n], 'output': o,
                    'note': None if o is not None else 'orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator session but not retained — read the seat report file in the wave dir'})
    json.dump({'lane': m['lane'], 'round': m['round'], 'wave': m['wave'], 'seats': len(res), 'results': res},
              open(out, 'w'), indent=1)
    w['done'] = True
    try:
        await tool.write({'path': f"agent://{m['l1']}", 'content':
            f"WAVE-DONE {m['lane']} r{m['round']} {m['wave']}: all {len(res)} seats settled. Results: {out}. "
            "Seats write reports in the wave dir; integrate, land via jj-lane.sh, then file/amend the report and end with the final JSON."})
    except Exception as e:
        dlog('notify-failed', m['l1'], repr(e))
    dlog('done', m['lane'], m['wave'], out)

async def tick():
    run, occupied = await proc_state()
    orphans = []
    for ready in sorted(glob.glob(f'{FLEET}/*-shokunin/.ufo/waves/round-*/*.ready')):
        if ready not in WAVES and not os.path.exists(ready + '.dispatched'):
            try:
                if not live(json.load(open(ready)).get('l1', ''), run):
                    orphans.append(ready); continue
                done, n = await register(ready, run, occupied)
                if done:
                    run, occupied = await proc_state()
                else:
                    occupied += n
                    dlog('cap-defer', ready, 'occupied', occupied)
            except Exception as e:
                dlog('wave-error', ready, repr(e))
    status = []
    for ready, w in WAVES.items():
        if w['done']:
            continue
        nlive = sum(1 for n in w['names'] if seat_live(w, n, run))
        if nlive == 0:
            await finalize(ready, w)
        status.append(f"{w['meta']['lane']}/{w['meta']['wave']}: live {nlive}/{len(w['names'])}")
    for ready, mine in PARTIAL.items():
        lane_dir, rnd_dir = ready.split('/')[-5], ready.split('/')[-2]
        status.append(f"{lane_dir.removesuffix('-shokunin')}/{rnd_dir}/{os.path.basename(ready)[:-6]}: filling {len(mine)} spawned")
    for ready in orphans:
        status.append(f"ORPHAN ready (L1 not running, not spawned): {ready}")
    ev = []
    for n in list(L1S):
        if not live(n, run):
            L1S.discard(n); ev.append(n)
    for lane, n in list(CLOS.items()):
        if not live(n, run):
            CLOS.pop(lane); ev.append('closure:' + lane)
    return ev, status

async def drive(max_s=1500, every=30):
    t0 = time.time(); ev = []; st = []; last_sweep = t0
    while time.time() - t0 < max_s:
        if time.time() - last_sweep >= DISK_SWEEP_EVERY:
            last_sweep = time.time()
            # non-emergency: the guard decides per root; a long sweep runs off the loop
            dlog('disk-sweep-rc', await asyncio.to_thread(disk_sweep))
        ev, st = await tick()
        dlog('drive', ev, st)
        if ev:
            break
        await asyncio.sleep(every)
    return ev, st

async def bootstrap():
    """Rebuild tracking after kernel loss: adopt dispatched waves lacking results, watch live L1s/closures."""
    run = await running_names()
    for ready in sorted(glob.glob(f'{FLEET}/*-shokunin/.ufo/waves/round-*/*.ready')):
        p = ready + '.partial'
        if ready in PARTIAL or os.path.exists(ready + '.dispatched') or not os.path.exists(p):
            continue
        try:
            ids = json.load(open(p))
        except (OSError, ValueError):
            continue
        PARTIAL[ready] = {n: _Spawned(i) for n, i in ids.items() if i}
        dlog('partial-restored', ready, len(PARTIAL[ready]))
    for ready in sorted(glob.glob(f'{FLEET}/*-shokunin/.ufo/waves/round-*/*.ready')):
        if ready in WAVES or not os.path.exists(ready + '.dispatched'):
            continue
        meta = json.load(open(ready))
        res = os.path.join(os.path.dirname(meta['dispatch']), f"{meta['wave']}-results.json")
        if os.path.exists(res):
            continue
        d = json.load(open(meta['dispatch']))
        names = [t['name'] for t in d['taskCall']['tasks']]
        if not any(live(n, run) for n in names) and not live(meta['l1'], run):
            continue  # stale wave of a finished round
        adopt(ready)
        if not live(meta['l1'], run):  # L1 was respawned as <id>a<k>
            alt = sorted(x for x in run if re.fullmatch(re.escape(meta['l1']) + r'a\d+', x))
            if alt:
                WAVES[ready]['meta']['l1'] = alt[-1]
    for x in run:
        if re.fullmatch(r'[A-Z][a-z]+R\d+(a\d+)?', x):
            L1S.add(x)
        m = re.fullmatch(r'Close([A-Z][a-z]+)R\d+', x)
        if m:
            CLOS[m.group(1).lower()] = x
    return sorted(L1S), CLOS, [(w['meta']['lane'], w['meta']['wave'], w['meta']['l1']) for w in WAVES.values()]
