#!/usr/bin/env python3
"""Reorder the glm-flash-shim cascade legs to zai -> devin -> hyper.

M9 (round 18). The live order was devin -> zai -> hyper, expressed by the
hardcoded defaults in `_build_legs()`; the systemd unit carries no active
GLM_LEG* environment overrides. This script moves whole `_leg(...)` blocks, so
each leg keeps its own URL / key literal / model rewrite; nothing is retyped
and no key material is copied anywhere (in particular not into the unit file,
which already holds one commented key line that must stay byte-for-byte).

Usage: apply_legorder.py <shim.py> --expect-sha256 <hex>
Refuses to run unless the file's sha256 matches the recorded pre-edit hash.
"""
import argparse
import hashlib
import importlib.machinery
import importlib.util
import re
import sys

DOCSTRING_OLD = '''Default legs (all overridable via env - see "LEG CONFIG" below):
  1. devin        POST http://127.0.0.1:8787/v1/chat/completions  (local
                  devin-shim; the body's `model` field is rewritten to the
                  devin slug "glm-5-3-flash-max" before forwarding)
  2. zai          POST https://api.z.ai/api/coding/paas/v4/chat/completions
                  (body forwarded as-is; model glm-5.3-flash is correct here)
  3. hyper        POST https://hyper.charm.land/v1/chat/completions
                  (body forwarded as-is)
'''

DOCSTRING_NEW = '''Leg order follows the operator's lane policy for glm-5.3-flash: zai is the
primary leg, devin the secondary/fallback leg.

Default legs (all overridable via env - see "LEG CONFIG" below):
  1. zai          POST https://api.z.ai/api/coding/paas/v4/chat/completions
                  (body forwarded as-is; model glm-5.3-flash is correct here)
  2. devin        POST http://127.0.0.1:8787/v1/chat/completions  (local
                  devin-shim; the body's `model` field is rewritten to the
                  devin slug "glm-5-3-flash-max" before forwarding)
  3. hyper        POST https://hyper.charm.land/v1/chat/completions
                  (body forwarded as-is)
'''

LEGCONF_OLD = '''  GLM_LEG1_NAME/URL/KEY/MODEL          leg 1 (devin)
  GLM_LEG2_NAME/URL/KEY/MODEL          leg 2 (zai)
  GLM_LEG3_NAME/URL/KEY/MODEL          leg 3 (hyper)
'''

LEGCONF_NEW = '''  GLM_LEG1_NAME/URL/KEY/MODEL          leg 1 (zai)
  GLM_LEG2_NAME/URL/KEY/MODEL          leg 2 (devin)
  GLM_LEG3_NAME/URL/KEY/MODEL          leg 3 (hyper)
'''

# old index -> new index
REMAP = {1: 2, 2: 1, 3: 3}
# desired list order by the legs' NEW index
NEW_ORDER = [1, 2, 3]


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalise(region):
    """Blank out the tokens this patch is allowed to change (index digits and
    GLM_LEG<n>_ numbers) so before/after can be compared line-multiset-wise."""
    region = re.sub(r"GLM_LEG\d_", "GLM_LEGx_", region)
    region = re.sub(r"(?m)^            \d+,$", "            N,", region)
    return region


def split_leg_blocks(body):
    blocks, cur = [], None
    for ln in body.split("\n"):
        if ln.startswith("        _leg("):
            cur = [ln]
        elif cur is not None:
            cur.append(ln)
            if ln == "        ),":
                blocks.append(cur)
                cur = None
    if cur is not None:
        raise SystemExit("unterminated _leg( block")
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("shim")
    ap.add_argument("--expect-sha256", required=True)
    args = ap.parse_args()

    with open(args.shim, "r", encoding="utf-8") as fh:
        old = fh.read()
    got = sha256_text(old)
    if got != args.expect_sha256:
        raise SystemExit("refusing: sha256 %s != expected %s" %
                         (got, args.expect_sha256))

    for label, frag in (("docstring", DOCSTRING_OLD),
                        ("legconfig", LEGCONF_OLD)):
        if old.count(frag) != 1:
            raise SystemExit("refusing: %s anchor found %d times" %
                             (label, old.count(frag)))

    # --- structural reorder of the _leg(...) blocks ------------------------
    bstart = old.index("def _build_legs():")
    body_start = old.index("    return [\n", bstart) + len("    return [\n")
    body_end = old.index("\n    ]\n", body_start)
    body = old[body_start:body_end]

    blocks = split_leg_blocks(body)
    if len(blocks) != 3:
        raise SystemExit("refusing: expected 3 leg blocks, found %d" % len(blocks))

    renumbered = {}
    for blk in blocks:
        m = re.match(r"^            (\d+),$", blk[1])
        if not m:
            raise SystemExit("refusing: cannot read index line %r" % blk[1])
        old_idx = int(m.group(1))
        new_idx = REMAP[old_idx]
        blk[1] = "            %d," % new_idx
        renumbered[new_idx] = "\n".join(
            ln.replace("GLM_LEG%d_" % old_idx, "GLM_LEG%d_" % new_idx)
            for ln in blk)

    new_body = "\n".join(renumbered[i] for i in NEW_ORDER)
    if sorted(normalise(body).split("\n")) != \
       sorted(normalise(new_body).split("\n")):
        raise SystemExit("refusing: reorder changed more than indices/env numbers")

    new = old[:body_start] + new_body + old[body_end:]
    new = new.replace(DOCSTRING_OLD, DOCSTRING_NEW)
    new = new.replace(LEGCONF_OLD, LEGCONF_NEW)

    with open(args.shim + ".tmp", "w", encoding="utf-8") as fh:
        fh.write(new)

    # --- verify the patched module's live leg configuration ---------------
    spec = importlib.util.spec_from_file_location(
        "shim_patched", args.shim + ".tmp",
        loader=importlib.machinery.SourceFileLoader("shim_patched",
                                                    args.shim + ".tmp"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    got_legs = [(l["index"], l["name"], l["url"], l["model"]) for l in mod.LEGS]
    want_legs = [
        (1, "zai", "https://api.z.ai/api/coding/paas/v4/chat/completions", ""),
        (2, "devin", "http://127.0.0.1:8787/v1/chat/completions",
         "glm-5-3-flash-max"),
        (3, "hyper", "https://hyper.charm.land/v1/chat/completions", ""),
    ]
    if got_legs != want_legs:
        raise SystemExit("refusing: patched legs are %r" % (got_legs,))

    # key material must be a permutation of the original: same values, new
    # slots. Only digests are ever printed.
    def auth_digests(path, name):
        spec2 = importlib.util.spec_from_file_location(
            name, path, loader=importlib.machinery.SourceFileLoader(name, path))
        m2 = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(m2)
        return sorted(hashlib.sha256(
            l["headers"]["Authorization"].encode()).hexdigest()[:12]
            for l in m2.LEGS)

    before_digests = auth_digests(args.shim, "_before")
    after_digests = auth_digests(args.shim + ".tmp", "_after")
    if before_digests != after_digests:
        raise SystemExit("refusing: auth header digests differ (%s -> %s)" %
                         (before_digests, after_digests))

    print("sha256 before: %s" % got)
    print("sha256 after : %s" % sha256_text(new))
    print("legs after   : %s" % [(i, n) for i, n, _, _ in got_legs])
    print("auth digests : %d identical (values permuted, none printed)"
          % len(after_digests))
    print("wrote %s.tmp" % args.shim)


if __name__ == "__main__":
    sys.exit(main())
