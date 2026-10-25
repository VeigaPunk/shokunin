# audio-r84-author — author the pw-dump/pw-cli introspection + monitor-tap lattice

Custody free (r82 fold landed d6167399). Read scout reports/round-84/ + boundary 3db77b13 (folded corrections: two refusal shapes = one stderr-slice artifact; monitor tap IS visible to mid-run gain at exact x0.125; -D '' is argv-eating).

- Author only boundary-surviving claims; encode the single refusal class; pin monitor-tap x0.125 response; negative controls for crash/refusal classes.
- Namespace r84a_*; insertion-only measure_audio.py edits.
- >=2 green family runs on final bytes. Commit nothing. Report reports/round-84/r84-author.md. Return: report path, files, legs, blockers.
