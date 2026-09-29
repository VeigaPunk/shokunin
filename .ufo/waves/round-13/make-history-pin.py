#!/usr/bin/env python3
"""make-history-pin.py -- write the append-only history pin the closure gate verifies.

The pin is `.ufo/history-pin.json` (override with --out):

    {"k": <int>, "sha256": <64-hex of canonical JSON rounds[0:k]>,
     "manifest_commit": <commit whose MANIFEST.json rounds[0:k] hashes to that digest>,
     "pinned_at": <ISO>, "pinned_by": <free text>, "entries": <k>}

Why: `rounds` is append-only after closure, but nothing mechanical proved it. The gate
(`closure-check.py` `_history_pin_check`) recomputes sha256(rounds[0:k]) on every live run and
reports `history_pin_mismatch` when closed history was edited in place. `manifest_commit`
anchors the digest to published bytes, so regenerating the pin to bless an edit also needs a
commit that rewrites the manifest -- a two-file change a non-author reviewer can see.

Appends never invalidate a pin: rounds[0:k] is unchanged by rounds[k:]. The pin is therefore
write-once per anchoring commit, and this tool refuses to write a digest no commit backs
unless --no-anchor is passed (fixture trees are not git repos).

Read-only over everything except --out. Stdlib only, no network, no env vars.

Exit map: 0 wrote (or --print printed) a pin; 1 refused (anchor mismatch, bad input);
2 could not evaluate (missing/unparsable MANIFEST.json, bad usage).
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime

EXIT_OK = 0
EXIT_REFUSED = 1
EXIT_ERROR = 2

PIN_REL = os.path.join(".ufo", "history-pin.json")


def canon_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def walk_up_repo(script_path):
    d = os.path.dirname(os.path.abspath(script_path))
    for _ in range(10):
        if os.path.isfile(os.path.join(d, "MANIFEST.json")) and os.path.isdir(os.path.join(d, ".ufo")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return os.getcwd()


def git(repo, args):
    try:
        done = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None, ""
    return done.returncode, done.stdout


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="exit map:\n  0 pin written/printed\n  1 refused\n  2 could not evaluate")
    ap.add_argument("--repo", default=None, help="repo root (default: nearest ancestor holding MANIFEST.json)")
    ap.add_argument("--manifest", default=None, help="MANIFEST.json to read (default: <repo>/MANIFEST.json)")
    ap.add_argument("--out", default=None, help="pin path (default: <repo>/.ufo/history-pin.json)")
    ap.add_argument("--k", type=int, default=None, help="entries to pin (default: all of rounds[])")
    ap.add_argument("--anchor-commit", default=None,
                    help="commit whose MANIFEST.json backs the digest (default: HEAD, verified; "
                         "refused when it does not hash to the digest)")
    ap.add_argument("--no-anchor", action="store_true",
                    help="write an unanchored pin (non-git trees, e.g. selftest fixtures)")
    ap.add_argument("--pinned-by", default=None, help="free-text provenance recorded in the pin")
    ap.add_argument("--print", dest="print_only", action="store_true", help="print the pin, write nothing")
    args = ap.parse_args(argv)

    repo = os.path.abspath(args.repo) if args.repo else walk_up_repo(__file__)
    manifest_path = args.manifest or os.path.join(repo, "MANIFEST.json")
    try:
        with open(manifest_path, "r", encoding="utf-8") as fh:
            manifest = json.load(fh)
    except OSError as exc:
        print("make-history-pin: could-not-evaluate: %s" % exc)
        return EXIT_ERROR
    except ValueError as exc:
        print("make-history-pin: could-not-evaluate: parse error in %s: %s" % (manifest_path, exc))
        return EXIT_ERROR

    rounds = manifest.get("rounds") or []
    k = len(rounds) if args.k is None else args.k
    if not isinstance(k, int) or k < 0 or k > len(rounds):
        print("make-history-pin: could-not-evaluate: --k must be 0..%d" % len(rounds))
        return EXIT_ERROR
    digest = canon_sha(rounds[:k])

    commit = None
    if not args.no_anchor:
        want = args.anchor_commit
        if want is None:
            code, out = git(repo, ["rev-parse", "HEAD"])
            want = out.strip() if code == 0 else None
        if not want:
            print("make-history-pin: refused: no --anchor-commit and no git HEAD in %s "
                  "(pass --no-anchor for a non-git tree)" % repo)
            return EXIT_REFUSED
        code, out = git(repo, ["show", "%s:MANIFEST.json" % want])
        if code != 0 or not out:
            print("make-history-pin: refused: cannot read %s:MANIFEST.json (git exit %s)" % (want, code))
            return EXIT_REFUSED
        try:
            anchored = (json.loads(out).get("rounds") or [])[:k]
        except ValueError:
            print("make-history-pin: refused: %s:MANIFEST.json does not parse" % want)
            return EXIT_REFUSED
        if canon_sha(anchored) != digest:
            print("make-history-pin: refused: %s:MANIFEST.json rounds[0:%d] hashes to %s, not %s -- "
                  "the working manifest differs from the commit (commit it first, or pin that commit)"
                  % (want, k, canon_sha(anchored)[:12], digest[:12]))
            return EXIT_REFUSED
        commit = want

    pin = {"k": k, "sha256": digest, "entries": k}
    if commit:
        pin["manifest_commit"] = commit
    pin["pinned_at"] = datetime.now().astimezone().replace(microsecond=0).isoformat()
    pin["pinned_by"] = args.pinned_by or "make-history-pin.py"
    text = json.dumps(pin, indent=1, sort_keys=True) + "\n"

    if args.print_only:
        sys.stdout.write(text)
        return EXIT_OK
    out_path = args.out or os.path.join(repo, PIN_REL)
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError as exc:
        print("make-history-pin: could-not-evaluate: cannot write %s: %s" % (out_path, exc))
        return EXIT_ERROR
    print("make-history-pin: wrote %s (k=%d sha256=%s anchor=%s)"
          % (out_path, k, digest[:12], (commit or "-")[:12]))
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
