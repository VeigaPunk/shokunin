# Kaika verification provenance — integrator erratum

This note corrects the opening boilerplate in the integrator-generated child files `corpus/lessons/round-<N>-verifier-spotcheck.md` that says fresh workers were dispatched “after the round landed at `<tip>`”. That value was filled from the worktree's final pre-adjudication tip, sometimes after post-review repairs. It is **not necessarily the workers' dispatch or execution cutoff**. The implied chronology is withdrawn for that generated cohort; manually written records retain their own explicit scope.

The authoritative verification boundaries are the exact base/head and dated recheck sections in this directory's `<lane>-review.md` and `<lane>-critic.md`, plus the explicitly named parent smoke receipts. The closure ledger's `commit` identifies the retained work tip, not a claim that every preceding check ran at that tip. A document-only correction does not silently become a fresh full-suite run.

Examples:

- `game-dev-2d`: outside workers reviewed `b0d2c499` / runtime implementation `ff32e252`. The parent subsequently exercised the bounded Q-ID join and SOURCES validation at `f67c64ae`; no full 621-row battery was rerun. The local round-105 spot-check has an appended chronology correction. Declared C2/C3 remain coupled and the round is rejected as declared.
- `kumitate`: the original review at `1a8eed5` rejected false-cleans and frozen-v1 drift. Targeted rechecks at `6336d71` and `0acb775` are appended to its outside review. The parent then clarified the direct-file-only capability row; that wording update is not another proxy/runtime measurement.
- `kaidoku` r13: the independent review reopened the registry at `5ac7860`; quote/location and trend errata followed at `3b5fea8`. Parent source validation after those documentation fixes is recorded separately. No REA target or ARM64X operation was executed by that capability round.

Other lanes' reports likewise distinguish initial work, post-review corrections, and the checks actually rerun. The named admit/reject source samples are bounded samples, not exhaustive certification of a corpus. An `admitted` closure is the parent's protocol adjudication over that evidence and its explicit limits; `rejected-honest-stop` retains useful work without claiming the frozen claim set verified.

New records must name verification cutoffs directly, or point to the source report without inferring a cutoff from the final work tip. No admission status, source measurement or historical report is rewritten by this erratum.
