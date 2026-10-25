# Lead-Authored r97 Guard Repair

Status: exact implementation contract, not an executed fix.

The source exploration is settled: the only three callers of
_wppol_r97_spawn are start_core, start_wp and variant; each has root.
The current helper ignores its root argument, loses Popen references,
and accepts a root substring in any process's argv or environment.
The kill path polls kill(pid, 0), which treats unreaped zombies as live.
These are the confirmed critic/reviewer findings, not new hypotheses.

Do not change measured policy predicates, pins, source hashes, runtime
binding, cross-witness laws, shared environment, locks or the historical
reports in this repair. The old required folds other than the narrow
signal-ownership/reaping repair remain open.

## Exact Source Changes

Add `WPPOL_R97_CHILDREN = {}` next to the WPPOL_R97 module constants.
Replace ONLY the following three function bodies with this authored text.
At all three existing spawn callers add `root=root`; no other caller or
public signature changes.

```python
def _wppol_r97_spawn(argv, env=None, log=None, root=None):
    """Retain the exact direct child and its private-root ownership."""
    if root is None:
        raise ValueError("r97 private spawn requires its owning root")
    lf = open(str(log), "w") if log else subprocess.DEVNULL
    try:
        proc = subprocess.Popen(
            [str(a) for a in argv], stdin=subprocess.DEVNULL,
            stdout=lf, stderr=subprocess.STDOUT, env=env,
            start_new_session=True)
    finally:
        if log:
            lf.close()
    WPPOL_R97_CHILDREN[proc.pid] = (str(root), proc)
    return proc


def _wppol_r97_own(root, pid):
    """Only a still-live direct child registered under this exact root."""
    child = WPPOL_R97_CHILDREN.get(pid)
    return (child is not None and child[0] == str(root)
            and child[1].poll() is None)


def _wppol_r97_kill(root, pid, sig=signal.SIGTERM, grace=4.0):
    """Signal only a registered child session, then wait and reap it."""
    if pid is None:
        return {"pid": None, "killed": False, "reason": "no pid"}
    child = WPPOL_R97_CHILDREN.get(pid)
    if child is None or child[0] != str(root):
        return {"pid": pid, "killed": False, "reason": "REFUSED foreign pid"}
    proc = child[1]
    if proc.poll() is not None:
        return {"pid": pid, "killed": False, "reason": "already gone"}
    t0 = time.monotonic()
    try:
        os.killpg(proc.pid, sig)
    except ProcessLookupError:
        proc.poll()
        return {"pid": pid, "killed": False, "reason": "already gone"}
    except OSError as exc:
        return {"pid": pid, "killed": False,
                "reason": f"signal refused: {exc}"}
    delivered = int(sig)
    try:
        proc.wait(timeout=grace)
    except subprocess.TimeoutExpired:
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            except OSError as exc:
                return {"pid": pid, "killed": False,
                        "reason": f"signal refused: {exc}"}
            delivered = "KILL"
        try:
            proc.wait(timeout=4.0)
        except subprocess.TimeoutExpired:
            return {"pid": pid, "killed": False, "sig": delivered,
                    "reason": "registered child did not exit"}
    return {"pid": pid, "killed": True, "sig": delivered,
            "secs": round(time.monotonic() - t0, 3),
            "returncode": proc.returncode}
```

Change the own_procs docstring to state its actual scope:
"Registered live direct children of this private root; not a general
descendant or root-text census." Keep its implementation unchanged.
Add `entry["own_process_census_scope"] = "registered live direct children"`
immediately before its assignment of own_procs_after in teardown.
Do not claim PID-reuse attacks or arbitrary descendant tracking were
experimentally proven by the regression.

## Exact Durable Regression

Create corpus/fixtures/test_wppol_r97_guard.py with these bytes. This is
an AST-isolated test of the actual helpers. It creates only its own
short-lived test processes; no host services, audio or network calls.

```python
"""r97 ownership and reaping without running an audio family."""
import ast
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


class GuardTest(unittest.TestCase):
    def setUp(self):
        path = Path(__file__).with_name("measure_audio.py")
        wanted = {"_wppol_r97_spawn", "_wppol_r97_own", "_wppol_r97_kill"}
        body = [n for n in ast.parse(path.read_text()).body
                if isinstance(n, ast.FunctionDef) and n.name in wanted]
        self.assertEqual({n.name for n in body}, wanted)
        self.ns = {"os": os, "Path": Path, "signal": signal, "time": time,
                   "subprocess": subprocess, "WPPOL_R97_CHILDREN": {}}
        exec(compile(ast.Module(body=body, type_ignores=[]), str(path), "exec"),
             self.ns)
        self.tmp = tempfile.TemporaryDirectory(prefix="r97-guard-test-")
        self.root = Path(self.tmp.name)
        self.children = []

    def tearDown(self):
        for proc in self.children:
            if proc.poll() is None:
                proc.kill()
            proc.wait(timeout=5)
        self.tmp.cleanup()

    def plain(self, mention=False, env_mention=False):
        argv = [sys.executable, "-c", "import time; time.sleep(60)"]
        if mention:
            argv.append(str(self.root))
        env = dict(os.environ)
        if env_mention:
            env["XDG_STATE_HOME"] = str(self.root / "state")
        proc = subprocess.Popen(argv, env=env, start_new_session=True)
        self.children.append(proc)
        return proc

    def own(self):
        proc = self.ns["_wppol_r97_spawn"](
            [sys.executable, "-c", "import time; time.sleep(60)"],
            env=dict(os.environ, XDG_RUNTIME_DIR=str(self.root / "run")),
            root=self.root)
        self.children.append(proc)
        return proc

    def test_foreign_argv_mention_is_not_signalled(self):
        proc = self.plain(mention=True)
        self.assertFalse(self.ns["_wppol_r97_own"](self.root, proc.pid))
        row = self.ns["_wppol_r97_kill"](self.root, proc.pid)
        self.assertFalse(row["killed"])
        self.assertEqual(row["reason"], "REFUSED foreign pid")
        self.assertIsNone(proc.poll())

    def test_foreign_environment_mention_is_not_signalled(self):
        proc = self.plain(env_mention=True)
        self.assertFalse(self.ns["_wppol_r97_own"](self.root, proc.pid))
        row = self.ns["_wppol_r97_kill"](self.root, proc.pid)
        self.assertFalse(row["killed"])
        self.assertIsNone(proc.poll())

    def test_owned_environment_only_child_is_reaped(self):
        proc = self.own()
        self.assertTrue(self.ns["_wppol_r97_own"](self.root, proc.pid))
        row = self.ns["_wppol_r97_kill"](self.root, proc.pid, grace=1)
        self.assertTrue(row["killed"])
        self.assertEqual(row["sig"], int(signal.SIGTERM))
        self.assertEqual(proc.returncode, -signal.SIGTERM)
        self.assertFalse(self.ns["_wppol_r97_own"](self.root, proc.pid))

    def test_wrong_root_cannot_signal_registered_child(self):
        proc = self.own()
        row = self.ns["_wppol_r97_kill"](self.root / "other", proc.pid)
        self.assertFalse(row["killed"])
        self.assertEqual(row["reason"], "REFUSED foreign pid")
        self.assertIsNone(proc.poll())

    def test_unregistered_process_and_invalid_ids_are_refused(self):
        proc = self.plain()
        for pid in (proc.pid, os.getpid(), 0, -1):
            with self.subTest(pid=pid):
                row = self.ns["_wppol_r97_kill"](self.root, pid)
                self.assertFalse(row["killed"])
                self.assertEqual(row["reason"], "REFUSED foreign pid")
        self.assertIsNone(proc.poll())

    def test_missing_root_is_rejected_before_spawn(self):
        with patch.object(subprocess, "Popen") as popen:
            with self.assertRaises(ValueError):
                self.ns["_wppol_r97_spawn"](["unused"])
            popen.assert_not_called()


if __name__ == "__main__":
    unittest.main()
```

## Application And Verification

This contract is authored, not an invitation to redesign it. Preserve
unrelated work. Keep a frozen source-before copy, exact source-only patch
and all raw stdout/stderr/rc in a fresh proof directory.

1. Add the exact test, run `python3 -B` before changing source: expected red.
2. Apply the exact source bodies/caller changes/scope disclosure.
3. Compile source/test using compile(), then run the test again: green.
4. Do not yet run a live family or change historical reports/LOG.
5. Return the full diff and raw paths for lead review. No commit/push.

Later, after the already-running pinned verifiers finish, a separate
lead recipe may run the repaired r97 family once. A green guard test
does not certify the still-open hash, shared-runtime, error-class, timing
labels or cross-tree-lock folds.
