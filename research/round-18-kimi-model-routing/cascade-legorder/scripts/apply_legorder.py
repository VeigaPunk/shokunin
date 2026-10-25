#!/usr/bin/env python3
"""Apply the operator's leg order to the ds-flash-shim cascade (mission M7).

    python3 apply_legorder.py --dry-run     # print the masked diff, write nothing
    python3 apply_legorder.py               # back up, rewrite, verify

Target order (operator directive 2026-10-15, verbatim context in LEGORDER.md):
  leg 1 alibaba-token-plan  (key 1 from ~/.kimi-code/config.toml)
  leg 2 hyper               (unchanged values, still the fallback)
  leg 3 opencode-go         (the values the shim already used for it)
  devin                     REMOVED from this cascade

Safety properties:

* Timestamped backups (`<file>.<YYYYmmdd-HHMMSS>.bak`) of every file it writes,
  taken before the write.
* The hyper and opencode-go credentials are copied out of the CURRENT shim.py
  text and re-emitted byte-for-byte, so the only new credential material is the
  alibaba leg's key, read from the live config inside this process.
* Exact anchors: the script refuses to run if a target block does not match the
  expected text, so a drifted file fails loudly instead of being half-edited.
* No credential value is printed, logged, or written anywhere: stdout carries a
  masked diff, and the change record keeps hashes and line numbers only.
* `py_compile` runs on the new shim.py before it is put in place.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile
import time
import tomllib

HOME = os.path.expanduser("~")
SHIM = os.path.join(HOME, ".local/share/ds-flash-shim/shim.py")
UNIT = os.path.join(HOME, ".config/systemd/user/ds-flash-shim.service")
CONFIG = os.path.join(HOME, ".kimi-code/config.toml")

ALIBABA_HOST = "token-plan.ap-southeast-1.maas.aliyuncs.com"

OLD_DOC = '''Default legs (all overridable via env - see "LEG CONFIG" below):
  1. opencode-go  POST https://opencode.ai/inference/go/v1/chat/completions
  2. hyper        POST https://hyper.charm.land/v1/chat/completions
  3. devin        POST http://127.0.0.1:8787/v1/chat/completions  (local
                  devin-shim; the body's `model` field is rewritten to the
                  devin slug before forwarding)
'''

NEW_DOC = '''Default legs (all overridable via env - see "LEG CONFIG" below).
Order set by operator directive 2026-10-15: token-plan first, charm hyper
second, opencode-go third; the devin leg was removed from this cascade:
  1. alibaba-token-plan  POST https://token-plan.ap-southeast-1.maas.aliyuncs.com/
                  compatible-mode/v1/chat/completions
  2. hyper        POST https://hyper.charm.land/v1/chat/completions
  3. opencode-go  POST https://opencode.ai/inference/go/v1/chat/completions
'''

OLD_ENVDOC = '''  DS_LEG1_NAME/URL/KEY/SESSION/MODEL   leg 1 (opencode-go)
  DS_LEG2_NAME/URL/KEY/MODEL           leg 2 (hyper)
  DS_LEG3_NAME/URL/KEY/MODEL           leg 3 (devin)
A leg's MODEL env var, when non-empty, replaces the request body's `model`
field for that leg (used by devin); empty means "pass the body through as-is".'''

NEW_ENVDOC = '''  DS_LEG1_NAME/URL/KEY/MODEL           leg 1 (alibaba-token-plan)
  DS_LEG2_NAME/URL/KEY/MODEL           leg 2 (hyper)
  DS_LEG3_NAME/URL/KEY/SESSION/MODEL   leg 3 (opencode-go)
A leg's MODEL env var, when non-empty, replaces the request body's `model`
field for that leg; empty means "pass the body through as-is" (all three
default legs pass the body through unchanged).'''

OLD_UNIT_DESC = ("Description=ds-flash-shim - OpenAI-compatible 3-leg cascade shim "
                 "(opencode-go -> hyper -> devin)")
NEW_UNIT_DESC = ("Description=ds-flash-shim - OpenAI-compatible 3-leg cascade shim "
                 "(alibaba-token-plan -> hyper -> opencode-go)")

BUILD_ANCHOR_START = "def _build_legs():\n"
BUILD_ANCHOR_END = "\n\nLEGS = _build_legs()\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def mask(line: str, secrets: list[str]) -> str:
    for value in secrets:
        if value:
            line = line.replace(value, value[:8] + "...<masked>")
    line = re.sub(r"\b(?:sk|oc_sk)-[A-Za-z0-9_\-]{8,}", lambda m: m.group(0)[:11] + "...<masked>", line)
    line = re.sub(r"(Bearer )\S{8,}", r"\1<masked>", line)
    return line


def unified(old: str, new: str, path: str, secrets: list[str]) -> list[str]:
    d = difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                             fromfile=path + " (before)", tofile=path + " (after)", n=2)
    return [mask(l, secrets).rstrip("\n") for l in d]


def extract_current_values(shim_text: str) -> dict:
    """Pull the leg constants the shim currently uses, without naming them here."""
    out = {}
    for env, key in (("DS_LEG1_KEY", "opencode_key"),
                     ("DS_LEG1_SESSION", "opencode_session"),
                     ("DS_LEG2_KEY", "hyper_key")):
        m = re.search(r'"%s",\s*\n\s*"([^"]+)"' % env, shim_text)
        if not m:
            raise SystemExit("anchor missing: default for %s not found in current shim.py" % env)
        out[key] = m.group(1)
    return out


def new_build_legs(values: dict, alibaba_key: str) -> str:
    return '''def _build_legs():
    return [
        _leg(
            1,
            os.environ.get("DS_LEG1_NAME", "alibaba-token-plan"),
            os.environ.get("DS_LEG1_URL",
                           "https://token-plan.ap-southeast-1.maas.aliyuncs.com/"
                           "compatible-mode/v1/chat/completions"),
            {
                "Authorization": "Bearer " + os.environ.get(
                    "DS_LEG1_KEY",
                    "%(alibaba_key)s"),
            },
            os.environ.get("DS_LEG1_MODEL", ""),  # empty = body as-is
        ),
        _leg(
            2,
            os.environ.get("DS_LEG2_NAME", "hyper"),
            os.environ.get("DS_LEG2_URL",
                           "https://hyper.charm.land/v1/chat/completions"),
            {
                "Authorization": "Bearer " + os.environ.get(
                    "DS_LEG2_KEY",
                    "%(hyper_key)s"),
            },
            os.environ.get("DS_LEG2_MODEL", ""),  # empty = body as-is
        ),
        _leg(
            3,
            os.environ.get("DS_LEG3_NAME", "opencode-go"),
            os.environ.get("DS_LEG3_URL",
                           "https://opencode.ai/inference/go/v1/chat/completions"),
            {
                "Authorization": "Bearer " + os.environ.get(
                    "DS_LEG3_KEY",
                    "%(opencode_key)s"),
                "x-opencode-session": os.environ.get(
                    "DS_LEG3_SESSION",
                    "%(opencode_session)s"),
            },
            os.environ.get("DS_LEG3_MODEL", ""),  # empty = body as-is
        ),
    ]
''' % {"alibaba_key": alibaba_key, "hyper_key": values["hyper_key"],
       "opencode_key": values["opencode_key"],
       "opencode_session": values["opencode_session"]}


def rewrite_shim(old: str, alibaba_key: str) -> tuple[str, dict]:
    values = extract_current_values(old)
    parts = {}
    for label, (old_block, new_block) in {
        "docstring_default_legs": (OLD_DOC, NEW_DOC),
        "docstring_leg_config": (OLD_ENVDOC, NEW_ENVDOC),
    }.items():
        if old.count(old_block) != 1:
            raise SystemExit("anchor not unique or missing: %s" % label)
        new = old.replace(old_block, new_block)
        parts[label] = (old, new)
        old = new
    i = old.find(BUILD_ANCHOR_START)
    if i < 0:
        raise SystemExit("anchor missing: %s" % BUILD_ANCHOR_START.strip())
    j = old.find(BUILD_ANCHOR_END, i)
    if j < 0:
        raise SystemExit("anchor missing: end of _build_legs")
    old_fn = old[i:j + len(BUILD_ANCHOR_END)]
    new_fn = new_build_legs(values, alibaba_key) + BUILD_ANCHOR_END
    new = old[:i] + new_fn + old[j + len(BUILD_ANCHOR_END):]
    meta = {"old_function_sha256": sha256_text(old_fn),
            "new_function_sha256": sha256_text(new_fn),
            "old_function_lines": old_fn.count("\n"),
            "new_function_lines": new_fn.count("\n")}
    return new, meta


def load_alibaba_key() -> str:
    with open(CONFIG, "rb") as fh:
        cfg = tomllib.load(fh)
    prov = cfg.get("providers", {}).get("alibaba-token-plan") or {}
    key = prov.get("api_key")
    if not isinstance(key, str) or len(key) < 8:
        raise SystemExit("providers.alibaba-token-plan.api_key not found in %s" % CONFIG)
    base = prov.get("base_url", "")
    if ALIBABA_HOST not in base:
        raise SystemExit("unexpected alibaba base_url %r" % base)
    return key


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ts = time.strftime("%Y%m%d-%H%M%S")
    with open(SHIM) as fh:
        shim_old = fh.read()
    with open(UNIT) as fh:
        unit_old = fh.read()

    alibaba_key = load_alibaba_key()
    shim_new, meta = rewrite_shim(shim_old, alibaba_key)
    secrets = [alibaba_key] + list(extract_current_values(shim_old).values())

    if unit_old.count(OLD_UNIT_DESC) != 1:
        raise SystemExit("unit Description line did not match the expected text")
    unit_new = unit_old.replace(OLD_UNIT_DESC, NEW_UNIT_DESC)

    print("== %s" % SHIM)
    print("\n".join(unified(shim_old, shim_new, SHIM, secrets)))
    print("== %s" % UNIT)
    print("\n".join(unified(unit_old, unit_new, UNIT, secrets)))
    print()

    # compile the candidate before anything is written
    tmp = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False)
    try:
        tmp.write(shim_new)
        tmp.close()
        py_compile.compile(tmp.name, doraise=True)
        print("py_compile: OK")
    except py_compile.PyCompileError as exc:
        os.unlink(tmp.name)
        raise SystemExit("py_compile FAILED, nothing written: %s" % exc)
    finally:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)

    if args.dry_run:
        print("dry run: nothing written")
        return 0

    backups = {}
    for path in (SHIM, UNIT):
        bak = "%s.%s.bak" % (path, ts)
        shutil.copy2(path, bak)
        backups[path] = bak

    with open(SHIM, "w") as fh:
        fh.write(shim_new)
    with open(UNIT, "w") as fh:
        fh.write(unit_new)

    record = {
        "applied_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "files": {
            SHIM: {"sha256_before": sha256_text(shim_old), "sha256_after": sha256_text(shim_new),
                   "bytes_before": len(shim_old), "bytes_after": len(shim_new),
                   "backup": backups[SHIM], "function_meta": meta},
            UNIT: {"sha256_before": sha256_text(unit_old), "sha256_after": sha256_text(unit_new),
                   "bytes_before": len(unit_old), "bytes_after": len(unit_new),
                   "backup": backups[UNIT],
                   "changed_lines": [i + 1 for i, (a, b) in enumerate(zip(unit_old.splitlines(), unit_new.splitlines())) if a != b]},
        },
        "leg_order_after": ["alibaba-token-plan", "hyper", "opencode-go"],
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw",
                       "apply-record-%s.json" % ts)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(record, fh, indent=2, sort_keys=True)
        fh.write("\n")

    # prove the rewritten module builds the intended legs, without printing any key
    probe = subprocess.run(
        [sys.executable, "-c",
         "import importlib.util,json,sys;"
         "spec=importlib.util.spec_from_file_location('shim_probe',%r);"
         "m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);"
         "print(json.dumps([{ 'index':l['index'],'name':l['name'],'url':l['url'],"
         "'model':l['model'],'auth_headers':sorted(l['headers']),"
         "'key_len':len(l['headers'].get('Authorization',''))} for l in m.LEGS]))" % SHIM],
        capture_output=True, text=True)
    if probe.returncode != 0:
        raise SystemExit("leg probe failed after write: %s" % probe.stderr[-800:])
    legs = json.loads(probe.stdout)
    print("rebuild probe: %s" % json.dumps(legs))
    record["legs_probe"] = legs
    with open(out, "w") as fh:
        json.dump(record, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("wrote %s" % out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
