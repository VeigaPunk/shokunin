#!/usr/bin/env python3
"""Record every local shim service: unit state, listener, configured env, provider map.

    python3 scripts/probe_shims.py

Shim units are discovered from `systemctl --user list-units` rather than
hardcoded, so a shim added to the config after this census was written still
shows up. For each unit the script records `is-active` / `is-enabled`, the unit
`show` output (ExecStart, MainPID, Environment), the unit file, and whether a
listener exists on its `SHIM_PORT`. Each shim port is then cross-referenced to
the config provider whose base_url points at it.

Writes raw/shims.json.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def run(args):
    """Run a command and return its output with credential-shaped values scrubbed.

    Redaction happens here, at capture time, because `systemctl --user cat` on a
    shim unit can return a real key sitting in a commented-out Environment= line.
    A commented credential is still a credential, so it is redacted like any other.
    """
    proc = subprocess.run(args, capture_output=True, text=True)
    return {"cmd": " ".join(args), "rc": proc.returncode,
            "stdout": common.redact_text(proc.stdout.strip()),
            "stderr": common.redact_text(proc.stderr.strip())}


def discover_units():
    res = run(["systemctl", "--user", "list-units", "--type=service", "--all",
               "--no-legend", "--plain"])
    units = []
    for line in res["stdout"].splitlines():
        name = line.split()[0] if line.split() else ""
        if "shim" in name and name.endswith(".service"):
            units.append(name)
    # Only the shim lines are kept: dumping the whole unit list would drag
    # unrelated service descriptions into the census for no evidential gain.
    res["shim_lines"] = [l for l in res["stdout"].splitlines()
                         if l.split() and l.split()[0] in units]
    res.pop("stdout", None)
    return sorted(units), res


def provider_port_map(cfg):
    """provider name -> local port, from base_urls pointing at 127.0.0.1."""
    out = {}
    for name, pcfg in (cfg.get("providers") or {}).items():
        for url in [pcfg.get("base_url", "")] + [
                m.get("base_url", "") for m in (cfg.get("models") or {}).values()
                if m.get("provider") == name]:
            m = re.match(r"http://127\.0\.0\.1:(\d+)", url or "")
            if m:
                out.setdefault(int(m.group(1)), []).append(name)
    return {port: sorted(set(names)) for port, names in out.items()}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else common.CONFIG_PATH
    cfg = common.load_config(path)
    ports = provider_port_map(cfg)

    units, discover = discover_units()
    listeners = run(["ss", "-ltnp"])
    listening_ports = set()
    listener_rows = []
    for line in listeners["stdout"].splitlines():
        m = re.search(r"127\.0\.0\.1:(\d+)", line)
        if m and 8780 <= int(m.group(1)) <= 8800:
            listening_ports.add(int(m.group(1)))
            listener_rows.append(line.strip())

    record = {
        "config_path": path,
        "config_sha256_16": common.config_digest(cfg),
        "provider_port_map": {str(k): v for k, v in sorted(ports.items())},
        "units": {},
        "listener_rows_8780_8800": listener_rows,
        "commands": [discover, listeners],
    }

    for unit in units:
        entry = {"unit": unit}
        for prop in ("is-active", "is-enabled"):
            res = run(["systemctl", "--user", prop, unit])
            entry[prop] = res["stdout"] or res["stderr"]
            record["commands"].append(res)
        show = run(["systemctl", "--user", "show", unit, "-p", "ActiveState",
                    "-p", "SubState", "-p", "MainPID", "-p", "ExecStart",
                    "-p", "Environment"])
        entry["show"] = show["stdout"]
        record["commands"].append(show)
        cat = run(["systemctl", "--user", "cat", unit])
        record["commands"].append(cat)

        # Port resolution, most authoritative first: the port the unit's own
        # MainPID is listening on, then an explicit SHIM_PORT env, then nothing.
        # Several shim units hardcode their port inside shim.py and export no
        # SHIM_PORT, so MainPID -> ss is the only reliable route for them.
        m = re.search(r"MainPID=(\d+)", show["stdout"])
        main_pid = m.group(1) if m else None
        entry["main_pid"] = int(main_pid) if main_pid and main_pid != "0" else None
        if entry["main_pid"]:
            for port in sorted(listening_ports):
                if any(str(entry["main_pid"]) in row and ":%d" % port in row
                       for row in listener_rows):
                    entry["shim_port"] = port
                    entry["port_source"] = "MainPID -> ss -ltnp"
                    break
        if "shim_port" not in entry:
            m2 = re.search(r"SHIM_PORT=(\d+)", show["stdout"] + cat["stdout"])
            if m2:
                entry["shim_port"] = int(m2.group(1))
                entry["port_source"] = "SHIM_PORT env in unit"
        if "shim_port" in entry:
            entry["listener_present"] = entry["shim_port"] in listening_ports
            entry["config_providers_on_port"] = ports.get(entry["shim_port"], [])
        record["units"][unit] = entry

    common.write_json("shims.json", record)

    print("discovered %d shim units; %d listeners in 8780-8800"
          % (len(units), len(listener_rows)))
    for unit, e in record["units"].items():
        print("  %-24s port=%-6s %-8s %-9s listener=%-5s providers=%s" % (
            unit, e.get("shim_port", "?"), e["is-active"], e["is-enabled"],
            e.get("listener_present"), ",".join(e.get("config_providers_on_port", [])) or "-"))


if __name__ == "__main__":
    main()
