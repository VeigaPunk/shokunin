#!/usr/bin/env python3
"""Verify that every number in ANALYSIS.md can be traced to a capture.

    python3 scripts/verify_numbers.py

The census claims that no figure in ANALYSIS.md is transcribed by hand. Tables are
generated from captures, so they are safe by construction; the risk is *prose*, where
a sentence can outlive the capture it was written from (review round 1 caught exactly
that in defects D2 and D7).

This script extracts every numeric token from ANALYSIS.md and checks it appears in the
union of `manifest.json` and `raw/*.json`. Numbers that do not appear are printed for
adjudication, and each must be justified as a *parameter* (a value the probe chose, such
as a timeout) rather than a *measurement* (a value an endpoint reported). Justified
parameters are listed in PARAMETERS below with their reason, so the script exits 0 only
when every number is either traced to a capture or explicitly adjudicated.

Exit status 0 = every number traced or adjudicated, 1 = unexplained numbers remain.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

ANALYSIS = os.path.join(common.CENSUS_DIR, "ANALYSIS.md")

# The invariant enforced here is strict: every number in ANALYSIS.md must appear in
# manifest.json or a raw/*.json capture. There is deliberately no exemption list --
# when review round 1 found two stale figures, the fix was to read them from the
# captures, and when a permission mode was cited without a capture the fix was to
# capture the mode. Both are better than an exemption.
#
# Caveat on strength: small integers (5, 8, 30) appear incidentally almost anywhere,
# so this check has real teeth for distinctive figures (707432, 12163, 1139432) and
# is weak for single digits. It is a regression guard for transcribed measurements,
# not a proof that every prose clause is well-sourced.


def numbers_in(text):
    """Numeric tokens, comma-normalised so '12,163' and '12163' compare equal."""
    out = set()
    for raw in re.findall(r"\d[\d,]*(?:\.\d+)?", text):
        out.add(raw.replace(",", ""))
        # also keep the integer part of a decimal so "232 lines" style values match
        if "." in raw:
            out.add(raw.replace(",", "").split(".")[0])
    return out


def main():
    with open(ANALYSIS) as fh:
        analysis = fh.read()

    haystack = []
    for name in sorted(os.listdir(common.RAW_DIR)):
        if name.endswith(".json"):
            with open(os.path.join(common.RAW_DIR, name)) as fh:
                haystack.append(fh.read())
    with open(os.path.join(common.CENSUS_DIR, "manifest.json")) as fh:
        haystack.append(fh.read())
    capture_text = "\n".join(haystack)
    capture_numbers = numbers_in(capture_text)

    doc_numbers = numbers_in(analysis)
    traced, unexplained = [], []
    for n in sorted(doc_numbers, key=lambda x: (len(x), x)):
        if n in capture_numbers:
            traced.append(n)
        else:
            unexplained.append(n)

    print("numbers in ANALYSIS.md : %d distinct" % len(doc_numbers))
    print("  traced to a capture  : %d" % len(traced))
    print("  UNEXPLAINED          : %d" % len(unexplained))
    if unexplained:
        print()
        print("These appear in neither manifest.json nor any raw/ capture.")
        print("Read them from a capture, or capture them -- do not exempt them:")
        for n in unexplained:
            print("  %s" % n)
        return 1
    print()
    print("Every number in ANALYSIS.md appears in manifest.json or a raw/ capture.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
