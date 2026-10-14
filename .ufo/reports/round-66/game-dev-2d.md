# game-dev-2d round 66 — coverage move: rejection-clause surface map

**Stamp.** 2D lane, round 66 (devin host, wave `shokunin-train-20261014-w6`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `cb84d0a`, report-last `4a4def9` — identity `game-dev-2d-shokunin <g2d@shokunin.local>`.

## Work performed

Mapped the rejection clause's full behavior over merged captured output. Four new fixture arms on `descendant_pipe_probe.gd` (`--spawn-{allowforge,splitforge,seamforge,midlineforge}`) + a ~500-line `probe_error_clause_surface` meta in `run_battery.py` (meta-driven bounded Popens, never CASES tuples — expected-FAIL records are inexpressible in the all-PASS battery). Integration applied the simplifier's warranted `reparent_gate` extraction (6 byte-identical copies, argv-byte-identical proven) and **rejected** the `export_preset_missing` dead-entry deletion (coverage-unsafe). Battery **88/88 PASS, surface meta 34/34**.

**Measured clause model:** the rejection clause = per-line `ERROR:` scan with allowlist exemption AND-ed with two whole-blob conjuncts (`SCRIPT ERROR:`, `Parse Error:`) that **preempt the allowlist itself** (critic falsification → corrected clause order adopted). Allowlist is preemptor of the line scan ONLY — F/T/F across all three entry shapes. Evasion works across the full `splitlines` boundary set + `\x1f` non-split; seam fabrication produces reject-triggering lines — and signature lines (accept-axis dual: forged PASS no process emitted) — from bytes present in NEITHER stream, in-life and post-death. **Third direction beyond the claim:** post-death `\xff` → `UnicodeDecodeError` → denial-of-verdict (scribe). Dead-entry census: 0/40 in-run dead, 6 static dead surfaces named with file:line.

## Landed changes

- `descendant_pipe_probe.gd` +4 arms; `run_battery.py` +~504 (`probe_error_clause_surface` + `reparent_gate` dedup); `corpus/lessons/r66-rejection-clause-surface.md`; `reports/round-66/` 8 seat reports + verifier + adjudicator.
- `classify_process` (merged-blob) vs `classify_streams` (per-stream, stderr-only error scan) divergence documented — bidirectional.

## Before → after measurements

| metric | before | after |
|---|---|---|
| rejection model | "un-allowlisted ERROR: line → FAIL" (r65) | full clause map: blob preemptors, allowlist bound, evasion set, seam fabrication, DoV |
| forgery directions | accept-forge (r63), reject-forge (r65) | + evasion, fabrication both axes, denial-of-verdict, composite split+phantom |
| battery | 87/87, 29 discriminations | **88/88**, surface meta 34/34 |
| baseline archive | 1.4G recursive trees | **614MiB** (-56%, `tree/` untrack confirmed by measurement) |

## SHONEN

- [x] Declared falsifiable axis-move (coverage); literal-wording falsification absorbed honestly
- [x] Named non-author replay — verifier **AGREE 5/5** (88/88, 34/34, all arms + split-PIPE proof, 0 prior mismatches)
- [x] No axis harmed (additive meta; reparent_gate byte-identical; dead entry retained)
- [x] Bounded claims; UNKNOWNs retained (host/pid-1573 env; census bounded to shipped fixtures; DoV decode-bound)
