#!/usr/bin/env python3
"""hyaku append-closure — append one closure entry to MANIFEST.json rounds[].

Integrator-of-record helper for hyaku closure sessions. Under the shared fleet
git lock it validates the entry, refuses duplicates, re-serializes the ledger
byte-identically to its existing format (indent=1, ensure_ascii=False,
separators=(',', ': ')), appends, commits MANIFEST.json alone as
protocol-shokunin, and pushes. Closed history is never edited in place.

  append-closure.py --entry <entry.json> [--dry-run]

Exit: 0 appended (+pushed) · 1 invalid/refused · 3 appended+committed, push failed.
"""
import argparse, fcntl, json, os, subprocess, sys, time

FLEET = os.environ.get("SHOKUNIN_ROOT", "/home/vgpnk/Projects/shokunin")
STATE = os.environ.get("HYAKU_STATE", os.path.expanduser("~/.local/state/shokunin-hyaku"))
MANIFEST = os.path.join(FLEET, "MANIFEST.json")
STATUSES = {"ok", "failed", "not-dispatched", "in-flight"}
TRENDS = {"expansion", "quality", "discernment"}
TREND_VERDICTS = {"improved", "harmed", "unchanged", "unprovable-but-better"}
DUMP = dict(indent=1, ensure_ascii=False, separators=(",", ": "))


def die(msg):
    print(f"append-closure: {msg}", file=sys.stderr)
    sys.exit(1)


def validate(e):
    req = {"round": int, "date": str, "type": str, "lane": str, "lane_round": int,
           "lanes": dict, "lane_rounds": dict, "closed_at": str, "campaign": str,
           "report": str, "notes": str, "promotions": list, "minted": list}
    for k, t in req.items():
        if k not in e:
            die(f"missing key {k}")
        if not isinstance(e[k], t) or (t is int and isinstance(e[k], bool)):
            die(f"key {k} must be {t.__name__}")
    if e["type"] not in {"closure", "closure-correction"}:
        die("type must be closure or closure-correction")
    if e["campaign"] != "hyaku":
        die("campaign must be hyaku")
    lane = e["lane"]
    if set(e["lanes"]) != {lane} or e["lanes"][lane] not in STATUSES:
        die(f"lanes must be {{{lane}: ok|failed|not-dispatched|in-flight}}")
    if e["lane_rounds"] != {lane: e["lane_round"]}:
        die("lane_rounds must be {lane: lane_round}")
    if e["round"] != e["lane_round"]:
        die("round must equal lane_round (per-lane counter)")
    if "trends" in e:
        tr = e["trends"]
        if not isinstance(tr, dict) or set(tr) != TRENDS or any(v not in TREND_VERDICTS for v in tr.values()):
            die("trends must carry exactly expansion/quality/discernment with improved|harmed|unchanged|unprovable-but-better")
    if e["lanes"][lane] == "ok" and not os.path.isfile(os.path.join(FLEET, e["report"])):
        die(f"ok row but report path does not exist: {e['report']}")
    if e["type"] == "closure-correction" and "supersedes" not in e:
        die("closure-correction needs supersedes")


def git(*args, ident=True):
    pre = ["git", "-C", FLEET]
    if ident:
        pre += ["-c", "user.name=protocol-shokunin", "-c", "user.email=protocol@shokunin.local"]
    return subprocess.run(pre + list(args), capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entry", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    try:
        entry = json.load(open(a.entry, encoding="utf-8"))
    except Exception as ex:
        die(f"cannot read entry JSON: {ex}")
    if not isinstance(entry, dict):
        die("entry must be a JSON object")
    validate(entry)

    os.makedirs(STATE, exist_ok=True)
    lk = open(os.path.join(STATE, "fleet-git.lock"), "w")
    deadline = time.time() + 1200
    while True:
        try:
            fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except BlockingIOError:
            if time.time() > deadline:
                die("fleet lock timeout (1200s)")
            time.sleep(2)

    raw = open(MANIFEST, "rb").read()
    doc = json.loads(raw)
    body = json.dumps(doc, **DUMP)
    nl = raw.endswith(b"\n")
    if (body + ("\n" if nl else "")).encode() != raw:
        die("MANIFEST.json is not in the expected serialization; refusing to rewrite it")
    for i, r in enumerate(doc["rounds"]):
        if (r.get("campaign") == "hyaku" and r.get("lane") == entry["lane"]
                and r.get("lane_round") == entry["lane_round"] and r.get("type") == entry["type"]
                and entry["type"] == "closure"):
            die(f"duplicate hyaku closure for {entry['lane']} r{entry['lane_round']} at rounds[{i}]; use closure-correction")
    doc["rounds"].append(entry)
    out = (json.dumps(doc, **DUMP) + ("\n" if nl else "")).encode()
    if not out.startswith(raw.rstrip(b"\n")[:-len(b"\n ]\n}")]):
        die("append would alter closed history bytes; refusing")
    idx = len(doc["rounds"]) - 1
    if a.dry_run:
        print(f"dry-run ok: would append rounds[{idx}]")
        return 0
    tmp = MANIFEST + ".hyaku.tmp"
    open(tmp, "wb").write(out)
    os.replace(tmp, MANIFEST)
    msg = (f"rounds ledger: {entry['lane']} r{entry['lane_round']} closure "
           f"({entry.get('verdict', entry['lanes'][entry['lane']])}) — hyaku, non-author")
    r = git("commit", "-q", "-m", msg, "--", "MANIFEST.json")
    if r.returncode != 0:
        die(f"commit failed: {r.stderr.strip()[:300]}")
    head = git("rev-parse", "HEAD", ident=False).stdout.strip()
    print(f"appended rounds[{idx}] commit {head}")
    for i in range(4):
        p = git("push", "-q", "origin", "HEAD:master", ident=False)
        if p.returncode == 0:
            print("pushed")
            return 0
        time.sleep(15 * (i + 1))
    print(f"push failed (commit kept): {p.stderr.strip()[:300]}", file=sys.stderr)
    return 3


if __name__ == "__main__":
    sys.exit(main())
