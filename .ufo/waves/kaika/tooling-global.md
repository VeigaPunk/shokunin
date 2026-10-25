# Operator tooling authority and host upgrades — kaika

Operator directive (2026-10-19): every agent may install/update any tool that helps its task or is a strict upgrade, with all available privileges and without asking again. This is authorization, not permission to bypass package-manager integrity, change routing, expose credentials, or ignore the host's boot-safety gate.

## Persistent entry points

- `~/.omp/agent/RULES.md` — authoritative tooling directive, official installation channels, tsukuroi full-system-upgrade gate, no partial `pacman -Sy`, and version/channel/reason reporting.
- `~/.omp/agent/hooks/pre/godspeed-always-on.js` — keeps the existing Godspeed injection and idempotently carries the tooling directive in task dispatches. OMP 18.12.3 also injects RULES.md natively into task `<generic-rules>`; the comment now reflects that observed behavior. Direct eval `tool.task` was exercised; `agent()`/`workpool()` were not.
- `~/.agents/AGENTS.md` — documented Kimi cross-tool global instruction entry point; core authorization plus a pointer to RULES.md and an explicit child-handoff duty. `KIMI_CODE_HOME` was unset during discovery.
- `~/.config/devin/AGENTS.md` — documented Devin global instruction entry point with the same authorization and propagation duty.

Fresh OMP runtime proof: `.ufo/waves/kaika-w3/tooling-runtime.md`. A single bounded fresh CLI invocation had no authorization bytes in its user prompt. Main quoted the directive before any tool result; the recorded child system prompt contains the exact RULES.md bytes under `<generic-rules>`, separately from the dispatch copy. The child answered that installation is authorized without asking. The probe accidentally spawned four children rather than the requested one; that deviation is recorded. No package installation was needed for the probe.

Kimi/Devin destinations were established from current official documentation, not a runtime inheritance test. Custom-agent instruction inheritance is not guaranteed by the reviewed docs; the global instructions explicitly require the main agent to propagate authorization into handoffs. No persistent model-routing or sudoers configuration changed.

## Installed or repaired tools

| Tool | Observed version | Channel/action | Reason |
|---|---|---|---|
| trafilatura | 2.3.1 | `uv pip install --python /usr/bin/python3 --target ~/.local/lib/python3.14/site-packages trafilatura` | Existing CLI's isolated Python 3.13 environment did not supply the system Python 3.14 import used by extraction. Parent exercised real article extraction with `/usr/bin/python3`; expected prose returned. |
| lychee | 0.24.2 | Arch official package, `pacman -S --needed` | Reproducible source/link checks. |
| rizin | 0.8.2 | Arch official package, `pacman -S --needed` | Available shipped-artifact inspection tool for the RE lanes. |
| shfmt | 3.14.1 | Arch official package, `pacman -S --needed` | Shell-tool maintenance. No unrelated formatting pass. |
| check-jsonschema | 0.38.2 | `uv tool install check-jsonschema` | Actual draft-2020-12 validation of new closure and correction records. |
| jj | 0.45.1-7c41cdeb | Already installed; configured per repo | Colocated pilots only in clean, settled mado/tameshi after linked worktree retirement. See `JJ-ADOPTION.md` and `jj-live-pilot.txt`. |

No unattended full-system upgrade was run. The known mkinitcpio `/sysroot` versus installed boot-hook `/new_root` compatibility issue remains behind tsukuroi's update-safety gate. No partial database refresh was run in this campaign's package transaction.

## Shell reliability repair

`~/.bashrc` now removes fnm's broken `cd=__fnmcd` alias immediately after fnm initialization, preserving its other environment setup and the zoxide hook. A fresh interactive shell executed `cd /tmp && pwd` and printed `/tmp`, without `__fnmcd` failure. Current agent commands still use explicit cwd/absolute paths; the campaign's accidental out-of-scope writes and their restorations remain disclosed in lane reports.

## Limits

The global directive does not make unavailable provider quotas available, and this campaign does not claim runtime inheritance for every third-party custom profile. It does not start an unattended model-spending watchdog. Git remains the fleet's concurrent-worktree substrate; jj is not a safe universal replacement while those worktrees are active.
