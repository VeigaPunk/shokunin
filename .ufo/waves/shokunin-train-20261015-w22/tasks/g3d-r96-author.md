# g3d-r96-author — author the Jolt fixed-fps/determinism lattice

Custody free (r95 landed 0767b59). Read reports/round-96/ scout + boundary (15b765d: --fixed-fps Jolt WARNING variable stream position; --time-scale = stealth tps knob; Dummy-mode hangs/null physics).

- Author only boundary-surviving claims; encode the Jolt warning as expected-error class (allowlist exact text, variable position tolerant); time-scale as tps law; Dummy vacuity preconditions.
- Insertion-only run_battery.py; new fixtures under corpus/fixtures/.
- Battery green twice on final bytes. Commit nothing. Report reports/round-96/r96-author.md. Return: report path, files, rows, blockers.
