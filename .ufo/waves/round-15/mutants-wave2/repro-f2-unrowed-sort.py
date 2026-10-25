#!/usr/bin/env python3
"""Crash probes for SnapshotExecutor F2 (untracked-prompt lane_round=None chain).

History (mutants were cut from sha c25957.., live gate since amended twice):

  v1 (sha 397754b9 / c25957):
    :1313 regex `\\.ufo/prompts/([a-z]+)-round-(\\d+)\\.md` -> ('-', None) row
    -> analyze sorted `unrowed` on RAW f["lane_round"] (:1435) -> TypeError, but
    only on a MIXED first-key tie: (lane_sort=9, None) vs (lane_sort=9, int).
    Equal (9,None)-(9,None) tuples never call < on None -- verified empirically.
    So one unreadable prompt alone was silent; the crash needed e.g. kama's
    unrowed_terminated row (also sorts at 9) in the same run.

  v2 (sha 265571e2, sibling F2 fix, current):
    :1445 sorts `unrowed` via _sorted_debt (guards lane_round=None);
    :1047 filters _untracked_prompts through _prompt_key_from_rel (PROMPT_NAME_RE).
    The :1324 unpack `lane, n = _prompt_key_from_rel(rel)` is still unguarded and
    crashes IF the upstream filter ever diverges from the re-parse -- it can't be
    reached through _untracked_prompts today, so this is a latent arm, not a bug.
    Repro below monkeypatches _untracked_prompts to bypass the filter and shows it.

`_untracked_prompts` is monkeypatched because it can never fire under --selftest:
`git rev-parse --show-toplevel` inside a fixture returns the *parent* repo root,
which never equals the fixture dir (the :1041 realpath guard returns None) --
so no committed fixture can exercise the untracked-prompt branch at all.
"""
import importlib.util
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "..", "closure-check.py")
FIX = os.path.join(HERE, "..", "fixtures", "closure-sample",
                   "counter-deleted-dispatch-only")   # kama r1 -> unrowed (9,int) row

spec = importlib.util.spec_from_file_location("closure_check", GATE)
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

# ---- control: clean fixture ------------------------------------------------
inp, err = cc.load_live(os.path.abspath(FIX))
assert err is None, err
res = cc.analyze(inp, {"citations": False})
print("control: verdict=%s exit=%d unrowed=%d" % (res["verdict"], res["exit"], len(res["unrowed"])))

# ---- arm A (v1 semantics): bypass upstream parse entirely, inject ('-',None)
# on v1 this crashed in the unrowed sort; on v2 _sorted_debt tolerates it but the
# :1324 unpack of a None key crashes first -- the surviving latent arm.
cc._untracked_prompts = lambda repo: [".ufo/prompts/kagi-L1.md",
                                      ".ufo/prompts/notes.md"]
inp, err = cc.load_live(os.path.abspath(FIX))
assert err is None, err
try:
    cc.analyze(inp, {"citations": False})
except Exception:
    print("armA bypass-filter: CRASH")
    print(traceback.format_exc().rstrip().splitlines()[-1])
else:
    print("armA bypass-filter: NO CRASH")
sys.exit(0)
