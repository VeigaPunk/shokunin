# run-16 orchestrator extension (Amendment 65, operator 2026-11-08: "graduate all the remaining shokunins",
# unattended overnight). Load order after a kernel loss, each in its own cell:
#   %load /home/vgpnk/Projects/shokunin/scripts/hyaku/inline-dispatcher.py
#   %load /home/vgpnk/Projects/shokunin/.scratch/run15-kernel.py
#   %load /home/vgpnk/Projects/shokunin/.scratch/run16-kernel.py
#   await bootstrap(); then loop: await run_for(1500)  (cell timeout 1700)
# Adds: (1) auto fresh-start lift of three-rejection pauses for the campaign lanes, re-basing FRESH_START
# (persisted in run16-fresh.json); (2) attempt-exhaustion lift after a 20-min cooldown, max 3 per lane;
# (3) closure relaunch backoff (>= 5 launches in 20 min defers); (4) a progress line per run_for.
# Amendment 66 (operator 2026-11-09): kagi paused (blocked/kagi operator marker); not in the campaign.
CAMPAIGN = ['chousa', 'souji', 'tabi', 'tameshi', 'kama']
FRESH_FILE = f'{FLEET}/.scratch/run16-fresh.json'
PROGRESS = f'{FLEET}/.scratch/run16-progress.log'
EXHAUST_COOLDOWN_S = 1200
EXHAUST_MAX_LIFTS = 3
try:
    FRESH_START.update({k: int(v) for k, v in json.load(open(FRESH_FILE)).get('fresh', {}).items()})
    AUTOLIFT = json.load(open(FRESH_FILE)).get('lifts', {})
except (OSError, ValueError):
    AUTOLIFT = globals().get('AUTOLIFT', {})
CLOSE_TS = globals().get('CLOSE_TS', {})

def _save_fresh():
    json.dump({'fresh': {l: FRESH_START[l] for l in CAMPAIGN if l in FRESH_START}, 'lifts': AUTOLIFT},
              open(FRESH_FILE, 'w'), indent=1)

def autolift(log):
    now = time.time(); tag = time.strftime('%Y%m%d')
    for lane in CAMPAIGN:
        p = f'{HS}/blocked/{lane}'
        try:
            why = open(p).read(); age = now - os.path.getmtime(p)
        except OSError:
            continue
        nxt = next_round(lane)
        if nxt > 100:
            continue
        if why.startswith('three consecutive rejected closures'):
            os.rename(p, f'{HS}/blocked/.{lane}.run16-{tag}-autofresh-r{nxt}')
            FRESH_START[lane] = nxt; _save_fresh()
            log.append(f'{lane}: AUTO fresh-start (Amendment 65d) at r{nxt}: {why.strip()[:120]}')
        elif re.match(r'round \d+ failed \d+ attempts', why):
            k = AUTOLIFT.get(lane, 0)
            if age < EXHAUST_COOLDOWN_S or k >= EXHAUST_MAX_LIFTS:
                continue
            AUTOLIFT[lane] = k + 1; _save_fresh()
            os.rename(p, f'{HS}/blocked/.{lane}.run16-{tag}-attempt-exhaustion-{k + 1}')
            log.append(f'{lane}: lifted attempt-exhaustion block {k + 1}/{EXHAUST_MAX_LIFTS} at r{nxt}: {why.strip()[:160]}')

if not getattr(close, '_run16', False):
    _close15 = close
def close(lane):
    ts = [t for t in CLOSE_TS.get(lane, []) if time.time() - t < 1200]
    CLOSE_TS[lane] = ts
    if len(ts) >= 5:
        return f'closure-backoff {lane} ({len(ts)} launches in 20 min)'
    ts.append(time.time())
    return _close15(lane)
close._run16 = True

if not getattr(step, '_run16', False):
    _step15 = step
async def step():
    log = []
    autolift(log)
    r = await _step15()
    r['log'] = log + r['log']
    return r
step._run16 = True

def progress(note=''):
    lanes = ' '.join(f'{l}={next_round(l)}' + ('B' if os.path.exists(f'{HS}/blocked/{l}') else '') for l in CAMPAIGN)
    d = st_load()
    live_s = ','.join(f"{l}:r{v.get('round')}:{v.get('phase')}" for l, v in d['live'].items())
    line = (f"{time.strftime('%Y-%m-%dT%H:%M:%S')} next[{lanes}] trained={d['trained']} adm={d['admitted']} "
            f"rej={d['rejected']} live[{live_s}] {note}")
    open(PROGRESS, 'a').write(line + '\n')
    return line

def graduated():
    return all(next_round(l) > 100 for l in CAMPAIGN)
