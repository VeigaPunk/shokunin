#!/usr/bin/env python3
"""jini-ryu-tag.py — graduate shokunin lanes into Jin'i-ryu.

Operator ruling 2026-11-05 (Amendment 38): every lane round >= 100 is tagged in
its lane repo, and a lane that reaches round 100 graduates.

Tags (annotated, lane identity, pushed to the lane's own origin):
  Jin'i-ryu/r<N>       the lane's last commit of round N (N >= 100)
  Jin'i-ryu/graduated  the commit of the lane's first round >= 100

Round commit resolution, in order:
  1. MANIFEST.json closure entry for (lane, N) whose `commit` is `<lane>-shokunin@<sha>`;
  2. newest lane commit whose subject names round N (`round-N`, `round N`, `r<N>`).
Rounds with no resolvable commit are reported, never guessed.

Idempotent: an existing tag at the same commit is left alone; at a different
commit it is reported and not moved.

Usage: jini-ryu-tag.py [--lane L] [--dry-run]
Exit: 0 clean · 1 a tag failed or conflicted · 2 usage/env (argparse usage = 64)
"""
import argparse, json, os, re, subprocess, sys

FLEET = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCHOOL = "Jin'i-ryu"


def git(repo, *a, check=True):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.strip()}")
    return r


def manifest_rounds():
    rs = json.load(open(os.path.join(FLEET, "MANIFEST.json")))["rounds"]
    out = {}  # (lane, n) -> commit-or-None
    for r in rs:
        if r.get("type") != "closure":
            continue
        lanes = r.get("lane_rounds") or ({r["lane"]: r["lane_round"]} if r.get("lane") and r.get("lane_round") else {})
        for lane, n in lanes.items():
            if not isinstance(n, int) or n < 100:
                continue
            c = r.get("commit")
            sha = None
            if isinstance(c, str) and c.startswith(f"{lane}-shokunin@"):
                sha = c.split("@", 1)[1]
            if sha or (lane, n) not in out:
                out[(lane, n)] = sha or out.get((lane, n))
    return out


def resolve(repo, n, sha):
    if sha:
        r = git(repo, "rev-parse", "--verify", "--quiet", f"{sha}^{{commit}}", check=False)
        if r.returncode == 0:
            return r.stdout.strip(), "manifest"
    log = git(repo, "log", "--all", "--date-order", "--format=%H %s").stdout.splitlines()
    for pat in (re.compile(rf"^round[- ]?{n}\b", re.IGNORECASE), re.compile(rf"\bround[- ]?{n}\b", re.IGNORECASE),
                re.compile(rf"^[a-z0-9-]+ r{n}:")):
        for line in log:  # newest first
            h, _, s = line.partition(" ")
            if pat.search(s):
                return h, "subject"
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane")
    ap.add_argument("--dry-run", action="store_true")
    try:
        a = ap.parse_args()
    except SystemExit as e:
        sys.exit(64 if e.code else 0)
    todo = manifest_rounds()
    lanes = sorted({l for l, _ in todo if not a.lane or l == a.lane})
    rc = 0
    for lane in lanes:
        repo = os.path.join(FLEET, f"{lane}-shokunin")
        if not os.path.isdir(os.path.join(repo, ".git")):
            print(f"SKIP {lane}: no repo"); continue
        rounds = sorted(n for l, n in todo if l == lane)
        first = None
        for n in rounds:
            commit, how = resolve(repo, n, todo[(lane, n)])
            if not commit:
                print(f"UNRESOLVED {lane} r{n}"); continue
            first = first or (n, commit)
            rc |= tag(repo, lane, f"{SCHOOL}/r{n}", commit, f"{SCHOOL}: {lane}-shokunin round {n} ({how})", a.dry_run)
        if first:
            rc |= tag(repo, lane, f"{SCHOOL}/graduated", first[1],
                      f"{SCHOOL} graduation: {lane}-shokunin reached round {first[0]}", a.dry_run)
    sys.exit(rc)


def tag(repo, lane, name, commit, msg, dry):
    have = git(repo, "rev-parse", "--verify", "--quiet", f"refs/tags/{name}^{{commit}}", check=False)
    if have.returncode == 0:
        if have.stdout.strip() == commit:
            print(f"OK-EXISTS {lane} {name} {commit[:12]}"); return 0
        print(f"CONFLICT {lane} {name} at {have.stdout.strip()[:12]} != {commit[:12]}"); return 1
    if dry:
        print(f"WOULD-TAG {lane} {name} {commit[:12]}"); return 0
    try:
        git(repo, "-c", f"user.name={lane}-shokunin", "-c", f"user.email={lane}@shokunin.local",
            "tag", "-a", name, commit, "-m", msg)
        git(repo, "push", "origin", f"refs/tags/{name}")
    except RuntimeError as e:
        print(f"FAIL {lane} {name}: {e}"); return 1
    print(f"TAGGED {lane} {name} {commit[:12]}"); return 0


if __name__ == "__main__":
    main()
