# run-15 orchestrator helpers. Reload after a kernel loss:
#   %load /home/vgpnk/Projects/shokunin/scripts/hyaku/inline-dispatcher.py   (own cell)
#   %load /home/vgpnk/Projects/shokunin/.scratch/run15-kernel.py             (own cell)
#   await bootstrap(); then loop: await run_for(1500)  (cell timeout 1700)
import subprocess, json, os, re, time, asyncio
from concurrent.futures import ThreadPoolExecutor
SEAT_CEILING = 98         # operator 2026-11-06: "you can match the 98 value on kernel and dispatcher" (dispatcher default HYAKU_SEAT_CEILING=98)
MAX_LIVE_LANES = 10       # operator 2026-11-06: train all 10 remaining lanes to 100 at once
FOCUS_MIN = 0             # operator 2026-11-06: "you can train the other shokunin ... until they reach 100" — focus band (was 90, Amendment 35) lifted
# Amendment 47 (orchestrator reading of Amendment 46, operator 2026-11-06 "we resume trainining each, until they
# reach 100"): after an authorized fresh start the 3-rejection pause counts only the lane's rounds since that fresh
# start ("the 3-rejection pause gate applies unchanged to their new rounds"). inline.sh's streak window also counts
# the pre-fresh-start rejections, so one post-fresh rejection re-blocked kasegi r79 / chousa r81 / kama r88.
# Amendment 58 (2026-11-08) re-based the fresh start for the four lanes it unblocked: the streak window
# now counts only rounds >= the lane's next-at-authorization round (Amendment 47's rule, re-dated).
FRESH_START = {'chousa': 84, 'kama': 94, 'kasegi': 79, 'kumitate': 92, 'mado': 88, 'tabi': 69, 'tameshi': 91, 'tsukuroi': 91}

def rejections_since_fresh(lane, nxt):
    """Consecutive rejected outcomes ending at round nxt-1, counting only rounds >= the lane's fresh start."""
    f = FRESH_START.get(lane)
    if f is None: return None
    n = 0
    for k in range(nxt - 1, f - 1, -1):
        try: o = open(f'{HS}/outcome/{lane}-r{k}').read()
        except OSError: break
        if not o.startswith('rejected'): break
        n += 1
    return n

def lift_carryover_block(lane, nxt, log):
    """Lift a 3-rejection streak block built partly from pre-fresh-start rounds; provider-failure blocks stay."""
    p = f'{HS}/blocked/{lane}'
    try: why = open(p).read()
    except OSError: return False
    if not why.startswith('three consecutive rejected closures'): return False
    n = rejections_since_fresh(lane, nxt)
    if n is None or n >= 3: return False
    os.rename(p, f'{HS}/blocked/.{lane}.run15-20261106-carryover-r{nxt - 1}')
    log.append(f'{lane}: lifted carry-over streak block ({n} rejection(s) since fresh start r{FRESH_START[lane]})')
    return True


def next_round(lane):
    try: return int(open(f'{HS}/next/{lane}').read())
    except (OSError, ValueError): return 0
IN = f'{FLEET}/scripts/hyaku/inline.sh'
ST = f'{FLEET}/.scratch/run15-state.json'
HS = os.path.expanduser('~/.local/state/shokunin-hyaku')

def sh(*a, timeout=900):
    r = subprocess.run(['bash', IN, *a], capture_output=True, text=True, cwd=FLEET, timeout=timeout)
    return r.returncode, (r.stdout + r.stderr).strip()

def claimed(lane):
    try:
        return int(open(f'{HS}/claims/{lane}/round').read()), int(open(f'{HS}/claims/{lane}/attempt').read())
    except OSError:
        return None

def st_load(): return json.load(open(ST))
def st_save(d): json.dump(d, open(ST, 'w'), indent=1)

def launch(lane):
    rc, out = sh('dispatch', lane)
    if rc: return f'DISPATCH-FAIL {lane}: {out[-500:]}'
    rnd, att = claimed(lane); lab = spawn_l1(lane, rnd, att)
    d = st_load(); L = d['lanes'][lane]
    if L['block_start'] is None: L['block_start'] = rnd
    d['live'][lane] = {'round': rnd, 'attempt': att, 'label': lab, 'phase': 'l1'}; st_save(d)
    return f'launched {lab}'

def close(lane):
    rc, out = sh('closure', lane)
    if rc: return f'CLOSURE-RENDER-FAIL {lane}: {out[-400:]}'
    rnd, _ = claimed(lane); lab = spawn_closure(lane, rnd)
    d = st_load(); d['live'].setdefault(lane, {}).update(round=rnd, phase='closure', label=lab); st_save(d)
    return f'closure {lab}'

def lane_of(label):
    m = re.fullmatch(r'(?:Close)?([A-Z][a-z]+)R\d+(a\d+)?', label)
    return m.group(1).lower() if m else None

def queue():
    rc, out = sh('queue'); return [ln.split()[0] for ln in out.splitlines() if ln.strip()]

def draining():
    # Operator 2026-11-04: "stop the loop, let each lane working finish their round". Flag file = no new rounds.
    return os.path.exists(f'{FLEET}/.scratch/run15-drain')

def fill_slots(log):
    if draining(): return
    d = st_load(); live = list(d['live'])
    while len(live) < MAX_LIVE_LANES:
        # A lane whose L1 (any attempt) is still running must not get a second L1 (mori r89 incident).
        busy = {lane_of(x) for x in L1S} | set(CLOS)
        cand = [l for l in queue() if l not in live and l not in busy and next_round(l) >= FOCUS_MIN]
        if not cand: break
        l = cand[0]; d['lanes'][l]['block_start'] = None; d['lanes'][l]['block_done'] = 0; st_save(d)
        log.append(launch(l)); d = st_load(); live = list(d['live'])

def on_l1_end(lane, log):
    rc, out = sh('verify', lane); log.append(f'verify {lane}: {out[-300:]}')
    if rc == 0:
        log.append(close(lane)); return
    rc2, o2 = sh('fail', lane, f'L1 ended without a landed report: {out[-200:]}'); log.append(f'fail {lane}: {o2}')
    d = st_load(); d['live'].pop(lane, None); st_save(d)
    if 'RETRYABLE' in o2: log.append(launch(lane))

def on_closure_end(lane, log):
    rc, out = sh('closed', lane); log.append(f'closed {lane}: {out}')
    cnt = int(out.split()[0]) if out and out.split()[0].isdigit() else 0
    if cnt < 1:
        log.append(f'NO CLOSURE ROW for {lane}; relaunching closure'); log.append(close(lane)); return
    rc, out = sh('advance', lane); log.append(f'advance {lane}: {out}')
    d = st_load(); L = d['lanes'][lane]; d['trained'] += 1
    if 'admitted' in out: d['admitted'] += 1
    else: d['rejected'] += 1
    L['block_done'] += 1; d['live'].pop(lane, None); st_save(d)
    nxt = int(open(f'{HS}/next/{lane}').read())
    blocked = os.path.exists(f'{HS}/blocked/{lane}') and not lift_carryover_block(lane, nxt, log)
    if nxt - 1 >= 100:  # Amendment 38: tag every lane round >= 100 and graduate the lane into Jin'i-ryu
        t = subprocess.run(['python3', f'{FLEET}/scripts/hyaku/jini-ryu-tag.py', '--lane', lane], capture_output=True, text=True, cwd=FLEET)
        log.append(f'jini-ryu {lane}: rc={t.returncode} {(t.stdout + t.stderr).strip()[-300:]}')
    if not draining() and nxt >= FOCUS_MIN and nxt <= 100 and not blocked:
        log.append(launch(lane))
    else:
        log.append(f'{lane} parked (drain={draining()}, block_done={L["block_done"]}, next={nxt}, blocked={blocked})')

async def step():
    log = []
    # An interrupted tick can consume an event before its persistent claim is handled.
    for lane, item in st_load()['live'].items():
        if item['phase'] == 'l1':
            L1S.add(item['label'])
        elif item['phase'] == 'closure':
            CLOS[lane] = item['label']
    ev, status = await tick()
    for e in ev:
        if e.startswith('closure:'): on_closure_end(e.split(':', 1)[1], log)
        else:
            lane = lane_of(e)
            if lane: on_l1_end(lane, log)
    fill_slots(log)
    run, occ = await proc_state()
    return {'events': ev, 'log': log, 'status': status, 'running': occ}

async def run_for(sec=1500, every=30):
    t0 = time.time(); logs = []; last = None
    while time.time() - t0 < sec:
        r = await step(); last = r
        if r['log']: logs += r['log']
        await asyncio.sleep(every)
    d = st_load()
    return {'log': logs, 'status': last['status'], 'running': last['running'], 'trained': d['trained'],
            'adm': d['admitted'], 'rej': d['rejected'],
            'live': {l: f"r{v['round']}:{v['phase']}" for l, v in d['live'].items()}}
