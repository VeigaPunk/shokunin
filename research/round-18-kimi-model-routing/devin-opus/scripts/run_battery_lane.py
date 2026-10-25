#!/usr/bin/env python3
"""Runs the M3 battery against the M10 candidate entry through one documented
adapter: this lane rejects `temperature`.

Why the adapter exists (measured, raw/shape-summary.json): the M3 openai body
carries `temperature: 0`, and the devin backend answers that body with HTTP 400
`invalid_argument` for `claude-opus-5-5-high`, while `temperature: 1.0` and a
body with no temperature at all both return 200. The live kimi client does not
transmit a temperature field at all (M2 section 3), so the constraint does not
bind real traffic -- but it does bind the M3 probe body, so the adapter drops the
field for this run and the deviation is recorded in the manifest rather than
hidden.

Everything else is the battery's own code path: same prompts, same warm-up rule,
same 400 s devin-class timeout, same grader, same one-attempt rule.
"""
import json
import os
import sys

# The battery's modules live in another mission's tree; importing them must not
# leave a __pycache__ there.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROUND_DIR = os.path.dirname(os.path.dirname(HERE))
BATTERY_SCRIPTS = os.path.join(ROUND_DIR, "battery", "scripts")
sys.path.insert(0, BATTERY_SCRIPTS)

import protocols  # noqa: E402
import run_battery  # noqa: E402

_original_build_body = protocols.build_body


def build_body_without_temperature(*args, **kwargs):
    body = _original_build_body(*args, **kwargs)
    body.pop("temperature", None)
    return body


if __name__ == "__main__":
    protocols.build_body = build_body_without_temperature
    run_battery.main()
    manifest_path = os.path.join(sys.argv[sys.argv.index("--outdir") + 1]
                                 if "--outdir" in sys.argv else "",
                                 "run-manifest.json")
    if manifest_path and os.path.exists(manifest_path):
        with open(manifest_path) as fh:
            manifest = json.load(fh)
        manifest["adapter"] = {
            "script": "devin-opus/scripts/run_battery_lane.py",
            "deviation": "temperature field dropped from every openai body",
            "reason": "lane returns HTTP 400 invalid_argument for temperature 0; "
                      "1.0 and absent both return 200 (raw/shape-summary.json)",
            "client_impact": "none: the live kimi client transmits no temperature "
                             "field (M2 section 3, rule 4/6 capture table)",
        }
        with open(manifest_path, "w") as fh:
            json.dump(manifest, fh, indent=2)
            fh.write("\n")
        print("manifest annotated with adapter note", flush=True)