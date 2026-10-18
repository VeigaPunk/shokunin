# Operator demand — souji mint (2026-10-18)

Verbatim operator directive (2026-10-18), the explicit-directive branch of
the mint bar:

> we will be minting a new shokunin, that's responsible for cleaning and
> pruning stale artifacts, logs, anything that's bloat from previous runs;
> here's some ideation onto it: The cleaner is drafted as souji-shokunin
> (掃除, "sweeping"), in repo shokunin-repo-hygiene. I rejected harai 祓 as
> too ritual and sarae 浚え as too obscure. It clears the mint bar on demand
> alone. Evidence:
>
> b2f2efa (Oct 15, 09:02 BRT) committed 15 scratch files to the fleet root,
> and they're still at HEAD. shokunin.conf.full-roster-20261015 is a
> byte-identical copy of shokunin.conf. lore has 19 dead worktrees and
> game-dev-2d has 5. kotodama has a 1.7 GB .scratch folder sitting next to
> live, unpushed work. No current lane removes anything: tsukuroi never
> deletes and mori only reports.
>
> Every removal needs one of three receipts: Pushed: after a fetch, the
> commit passes merge-base --is-ancestor against origin. Moved to Obsidian:
> a matching ledger row. Stale: the file is a known scratch type, nothing
> references it, and it's older than the lane's last admitted round. The
> default is a dry run. Anything removed goes to quarantine first and is
> deleted only after a hold period and a second check. It never rewrites
> history; that stays with kura (still unminted) or you. It never touches
> operator config, credentials, or a lane with dirty or unpushed work.
>
> The Obsidian rule needs one thing from you: nothing records exports today.
> I'd add corpus/knowledge/obsidian-ledger.tsv, with the source path and hash
> plus the vault path and hash. Without a matching row, a file never
> qualifies as moved to Obsidian.
>
> Axes: calibration, operability and coverage. A false "safe" verdict is its
> worst failure.
>
> First three rounds:
> r1: a dry-run census that classifies every item in the evidence above,
> with zero false "safe" verdicts under a non-author spot-check.
> r2: a souji verify tool that has to return NOT-SAFE for kotodama's unpushed
> state.
> r3: prune the 24 dead worktree entries (metadata only), plus a
> root-scratch removal list for your approval.
>
> Draft shokunin.conf lane:
> souji|souji-shokunin|calibration + operability + coverage (repo and
> workspace hygiene (掃除): stale/duplicate/preserved artifact census with
> per-artifact pushed/moved/stale receipts; dry-run by default, quarantine
> before delete, never history or credentials)

**Measured corrections at mint (orchestrator, 2026-10-18):** the conf copy
is NOT byte-identical to the live conf (`cmp` → DIFFER, 3859 vs 4092 B) —
it is a superseded snapshot; kotodama `.scratch` measures 553M, not 1.7 GB.
Both corrections are recorded in `souji-shokunin/LOG.md` and MINT.md.

**Risk noted by operator:** "its rounds may hit the same MISSING_BINDING
routing block as the other lanes" — carried into the training goal's stop
rule and the lane's L0 channel.
