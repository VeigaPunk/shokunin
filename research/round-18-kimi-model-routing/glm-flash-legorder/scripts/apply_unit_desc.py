#!/usr/bin/env python3
"""Repoint the glm-flash-shim unit's Description line at the new leg order.

M9 (round 18). The unit carries live key material in *commented* Environment=
lines (filed by M1 as a vuln finding); this script touches exactly one line --
the [Unit] Description -- and refuses to write unless every other line,
including all comment lines, is byte-identical to the input.

Usage: apply_unit_desc.py <unit> --expect-sha256 <hex>
"""
import argparse
import hashlib
import sys

OLD = "Description=glm-flash-shim - OpenAI-compatible 3-leg cascade shim (devin -> zai -> hyper)"
NEW = "Description=glm-flash-shim - OpenAI-compatible 3-leg cascade shim (zai -> devin -> hyper)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    ap.add_argument("--expect-sha256", required=True)
    args = ap.parse_args()

    with open(args.unit, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines(keepends=True)
    before_sha = hashlib.sha256("".join(lines).encode()).hexdigest()
    if before_sha != args.expect_sha256:
        raise SystemExit("refusing: sha256 %s != expected %s"
                         % (before_sha, args.expect_sha256))

    hits = [i for i, ln in enumerate(lines) if ln.rstrip("\n") == OLD]
    if len(hits) != 1:
        raise SystemExit("refusing: Description anchor found %d times" % len(hits))

    new_lines = list(lines)
    new_lines[hits[0]] = NEW + "\n"
    changed = [i for i in range(len(lines)) if lines[i] != new_lines[i]]
    if changed != hits:
        raise SystemExit("refusing: changed lines %r != %r" % (changed, hits))

    # every comment line (the commented key material in particular) must survive
    c_before = [ln for ln in lines if ln.lstrip().startswith("#")]
    c_after = [ln for ln in new_lines if ln.lstrip().startswith("#")]
    if c_before != c_after:
        raise SystemExit("refusing: comment lines changed")

    with open(args.unit + ".tmp", "w", encoding="utf-8") as fh:
        fh.write("".join(new_lines))

    print("sha256 before      : %s" % before_sha)
    print("sha256 after       : %s"
          % hashlib.sha256("".join(new_lines).encode()).hexdigest())
    print("changed lines      : %d (line %d, Description)"
          % (len(changed), hits[0] + 1))
    print("comment lines kept : %d byte-identical" % len(c_after))
    print("wrote %s.tmp" % args.unit)


if __name__ == "__main__":
    sys.exit(main())