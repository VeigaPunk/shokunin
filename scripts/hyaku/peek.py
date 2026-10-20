#!/usr/bin/env python3
"""hyaku peek — summarize the newest omp session of a lane (or closure) for monitoring.

  peek.py <lane> [--last N]       lane session under ~/.omp/agent/sessions/-Projects-shokunin-<lane>-shokunin
  peek.py --closure [--last N]    newest fleet-root session (closure sessions run from the fleet root)

Prints the session model, tool-call histogram, every `task` call (lane count + role histogram),
the models seen in subagent transcripts, and the last N tool intents.
"""
import collections, glob, json, os, sys

SESS = os.path.expanduser("~/.omp/agent/sessions")


def newest(pattern):
    files = sorted(glob.glob(pattern), key=os.path.getmtime)
    return files[-1] if files else None


def main():
    args = sys.argv[1:]
    last = 12
    if "--last" in args:
        i = args.index("--last"); last = int(args[i + 1]); del args[i:i + 2]
    if args and args[0] == "--closure":
        f = newest(f"{SESS}/-Projects-shokunin/*.jsonl")
    elif args:
        f = newest(f"{SESS}/-Projects-shokunin-{args[0]}-shokunin/*.jsonl")
    else:
        print(__doc__); return 64
    if not f:
        print("no session"); return 1
    models, tools, intents, tasks = [], collections.Counter(), [], []
    first_ts = last_ts = None
    for line in open(f, encoding="utf-8", errors="replace"):
        try:
            e = json.loads(line)
        except Exception:
            continue
        ts = e.get("timestamp")
        if ts:
            first_ts = first_ts or ts; last_ts = ts
        if e.get("type") == "model_change":
            models.append(f"{e.get('model')}{' (fallback)' if e.get('resolvedModelIsFallback') else ''}")
        m = e.get("message")
        if not isinstance(m, dict):
            continue
        for c in m.get("content") or []:
            if isinstance(c, dict) and c.get("type") == "toolCall":
                name = c.get("name"); a = c.get("arguments") or {}
                tools[name] += 1
                intents.append(f"{name}: {a.get('i', '')}")
                if name == "task":
                    ts_ = a.get("tasks") or []
                    tasks.append((len(ts_), collections.Counter(t.get("agent", "task") for t in ts_)))
    print(f"session: {f}")
    print(f"span: {first_ts} -> {last_ts}")
    print(f"models: {', '.join(models) or '?'}")
    print(f"tools: {dict(tools)}")
    for n, roles in tasks:
        print(f"task call: {n} lanes {dict(roles)}")
    sub = f[:-6]
    if os.path.isdir(sub):
        seen = collections.Counter()
        for sf in glob.glob(f"{sub}/**/*.jsonl", recursive=True):
            for line in open(sf, encoding="utf-8", errors="replace"):
                if '"model_change"' in line:
                    try:
                        e = json.loads(line); seen[e.get("model")] += 1
                    except Exception:
                        pass
                    break
        if seen:
            print(f"subagent models: {dict(seen)}")
    print("last intents:")
    for s in intents[-last:]:
        print("  " + s[:150])
    return 0


if __name__ == "__main__":
    sys.exit(main())
