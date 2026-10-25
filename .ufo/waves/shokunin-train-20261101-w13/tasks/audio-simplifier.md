# r74 SIMPLIFIER (audio) — YAGNI deletion preserving verified behavior

Read SHARED.md + the r74 author brief.

After the diff lands: find provably-dead code, redundant branches, false-positive gates in the new + adjacent code. Every deletion candidate gets a byte-identity proof (run the battery/arm on a scratch copy, receipts must match). Deletion of evidence rows or load-bearing pins is out of scope. Record what you measured vs recommend.
Report -> reports/round-74/r74-simplifier.md.
