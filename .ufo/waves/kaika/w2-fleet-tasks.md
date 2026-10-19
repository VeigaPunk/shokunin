# kaika W2 — fleet-root task specs (protocol lane round 16 + three operator-side writers)

All paths absolute. Fleet root: `/home/vgpnk/Projects/shokunin` (FR). Campaign worktrees:
`FR/.tower/worktrees/kaika/` (WT). Committed campaign inputs live on branch `kaika/ledger` at
`WT/fleet-ledger/.ufo/waves/kaika/` (PLAN, SOURCES-CONTRACT-v1, steer, lane-addendum) and
`WT/fleet-ledger/.ufo/waves/kaika-w1/` (W1 dossiers: `critic.md`, `driver.md`, `art-curation.md`,
`mistakes.md`, `protocol-state.md`, `aggregator-state.md`, `connect-instruments.md`,
`manifest.md`, `l0.md`, `elegance.md`, `freshness.md`, …). Operator goal (verbatim): "make the
shokunin and all related repos smarter, more elegant, they should explore, build corpuses, keep
the essence of the shokunin that's well outlined in the main repo; while also using heavy
parallelization to be able to research, refine, explore, develop, unfold, new techniques,
current art, learn by making mistakes, a continuous improvement; that builds a continuous corpus
and curation of sources of where to learn more from."

Shared interface, frozen for this campaign: `SOURCES-CONTRACT-v1.md` (one 11-column registry
table, statuses `queued|mined|rejected`, tested census commands). Every task below implements or
references that contract verbatim — none redefines it. No pushes anywhere (standing operator
rule). Never touch the fleet-root main checkout, lane repos, `MANIFEST.json`, or
`.ufo/l0-questions.md`; put operator questions in your final response.

---

## T-PROTOCOL — protocol lane, round 16 (main-repo lane)

Worktree (only write scope): `WT/fleet-protocol` (branch `kaika/protocol`, base `31baf5c`).
Lane identity for every commit: `git -c user.name=protocol-shokunin -c user.email=protocol@shokunin.local commit -- <paths>`.
Registry home: the protocol section of root `SCORECARD.md` above `## Aggregator lane`; log:
root `LOG.md`. Read `FR/PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `AXES.md`, `LEARNING.md`,
`CORPUS.md`, `MISSION.md` first, then `kaika-w1/protocol-state.md` (your STATE dossier),
`critic.md`, `mistakes.md`, `aggregator-state.md`.

Known critical defect: commit `31baf5c` replaced root `SCORECARD.md` and `LOG.md` with
kotoba-shokunin's bytes; the last good fleet bytes survive at `12f2da5` (also `0b1ac3b`). Your
round, 1–3 claims, each with a falsifiable before→after and a counting command:

1. **gate-integrity (lowest-axis repair):** restore the fleet bytes of root `SCORECARD.md` and
   `LOG.md` from the last good commit, carry forward every genuine fleet entry added after it
   (diff `12f2da5..31baf5c` and classify each hunk: fleet entry vs kotoba bytes), then append a
   correction entry to `LOG.md` naming the incident, the evidence, and the restore. Re-establish
   the protocol registry home and the `## Aggregator lane` section. Add a re-runnable
   section-loss check (for example `scripts`-free: a committed check under `.ufo/gates/` that
   fails when the root ledgers lose their fleet header, the protocol registry section, or
   `## Aggregator lane`), with a self-test that is shown able to fail.
2. **protocol-soundness:** amend `PROTOCOL.md` (+ an incident-digest row in
   `PROTOCOL-APPENDIX.md` for each new rule) so the continuous loop builds the corpus every
   round: the file contract gains `corpus/SOURCES.md` (contract v1, pointing at the `CORPUS.md`
   section the operator-side writer adds); the round contract gains a frontier step (curate
   sources, mine one mistake, ≥1 sourced claim) and the report gains a **Sources & frontier**
   section. Keep the essence untouched: per-axis verdicts, 1–3 claims, non-author verification,
   append-only, provenance. Never edit `CORPUS.md`, `LEARNING.md`, `MISSION.md`, `AXES.md`,
   `scripts/`, or `templates/` — those are operator-side and are changed by a separate writer
   from the same contract.

L2 floor: ≥8 L2 in ONE batched `task` call (planner, connector, 3× executor, scribe, scout,
reviewer, critic); each a leaf; prompts lead with `/skill:godspeed` + the verbatim bytes of
`~/.agents/skills/godspeed/directive.md`; writing L2s get disjoint file sets; never pass a model.
Report: `WT/fleet-protocol/.ufo/reports/round-16/protocol.md` with the template §4 sections +
Sources & frontier (`SOURCES: unchanged — main-repo lanes hold no corpus/`) + trend verdicts +
L0 questions; commit it last under the lane identity, citing the work commit. Mark nothing `[x]`.
Final response ≤15 lines: commits, claims with self-verdicts, gate output, blockers.

---

## T-CONTRACT — operator-side contract writer (operator directive, not a lane round)

Worktree (only write scope): `WT/fleet-contract` (branch `kaika/contract`, base `31baf5c`).
Files you may change: `CORPUS.md`, `LEARNING.md`, `templates/round-prompt.md`. Nothing else.
Do not commit — the integrator reviews and commits.

1. `CORPUS.md`: add `SOURCES.md` to the layout block and a section **SOURCES.md — where a
   shokunin learns** carrying contract v1 in full (shape, columns, rules 1–6, census commands).
   Add a short rule set "from the kaika campaign": new knowledge entries open with the
   `source:`/`verified-at:`/`recheck:` trio (and `source:` cites an `S###` row when external);
   a round lesson that mines mistakes carries `## Mistakes` (class · evidence · captured-by ·
   fix); a fix is shown able to fail before it counts (`kaika-w1/mistakes.md` rec 2). Cite the
   evidence files the way the existing "Rules added from the round-1/2 corpus audits" section
   does.
2. `LEARNING.md`: minimal, essence-preserving edits — curation names `corpus/SOURCES.md` as
   where opened sources and rejections are curated; understanding names mistake mining into
   lessons + `QUALITY.md`; the expansion observable counts entries citing `mined` rows. Do not
   change the three trends, the verdict vocabulary, or the outside-discernment rule.
3. `templates/round-prompt.md`: replace the never-substituted `<{{LANE}}-repo>` with
   `{{LANE}}-shokunin`; add §2b "Frontier step — every round" (curate SOURCES.md, record the
   census before→after, mine one mistake or paste the sweep that found none, ≥1 sourced claim)
   using contract v1's tested commands; add **Sources & frontier** to the §4 required report
   sections; remove the stray trailing line ` | godspeed` (verify with `tail -c 40` that it is
   an artifact, not content). Keep every other line byte-identical.

Verify: `git -C WT/fleet-contract diff --stat`, render the template for one lane with sed and
show no `{{` or `<{{` remains, and run each census command from the new `CORPUS.md` against
`/tmp/kaika/sources-test/corpus/SOURCES.md` (a synthetic table; expected: rows 7, malformed 1,
dup S003, tier-inflation S002, bad tier S006, bad status S006). Final response: diff summary,
verification output, open questions.

---

## T-CENSUS — operator-side instrument writer: `scripts/sources-census.sh`

Worktree (only write scope): `WT/fleet-census` (branch `kaika/census`, base `31baf5c`).
Files: `scripts/sources-census.sh` (new) and its fixtures under `scripts/fixtures/sources-census/`
(new). Nothing else. Do not commit — the integrator reviews and commits.

Build the design in `kaika-w1/driver.md` §3, conformed to contract v1 (11 columns, NF=13,
statuses `queued|mined|rejected`; `watch` is not a status — `recheck` carries cadence). Bash +
coreutils + awk only, matching the existing script conventions. Parse `shokunin.conf` LANES rows
textually (never `source` it); also accept `--root` and explicit lane dirs. Modes:
`census` (default: per-lane rows, tiers, statuses, fleet totals), `validate` (malformed rows,
duplicate ids, enum violations, community-at-A, mined rows with dangling `used-by`, missing
file), `overdue` (ISO `recheck` dates before `--today`, default today; cadences reported, not
judged), `shared` (sources whose normalized URL appears in ≥2 lanes), `selftest` (runs every
check against the fixtures and proves each check can fail — seeded defects must be caught;
report killed/survived). Exit: 0 ok · 1 findings · 2 usage/env · 3 selftest failure. Read-only:
writes only stdout or `--out`. Interface the driver will call: `scripts/sources-census.sh
validate --root <fleet-root> <lane>` → 0/1/2.

Verify: `shellcheck` clean (or justified), `bash scripts/sources-census.sh selftest` exits 0
with every seeded defect killed, `validate` on the synthetic table
`/tmp/kaika/sources-test/corpus/SOURCES.md` (via an explicit lane dir) reports exactly its
seeded defects, and `census --root /home/vgpnk/Projects/shokunin` runs read-only on the live
fleet (lanes without SOURCES.md report `missing`, exit 1). Final response: files, commands with
outputs, residual risks.

---

## T-DRIVER — operator-side driver repair: `scripts/shokunin-watchdog.sh`

Worktree (only write scope): `WT/fleet-driver` (branch `kaika/driver`, base `31baf5c`).
Files: `scripts/shokunin-watchdog.sh` only. Do not commit — the integrator reviews and commits.
Never run the watchdog loop; test functions in isolation (source with a guard, or extract into
a scratch harness under `/tmp`).

Read `kaika-w1/driver.md` (all findings, line-referenced: F = this file, K =
`/home/vgpnk/Projects/kimi-shokunin/scripts/shokunin-watchdog.sh`). The committed fleet driver
cannot launch anything (dead `ufo-sighting` path, hardcoded 9-lane roster); the running driver
was K-shaped and uncommitted. Port K's substrate-neutral launch (`SUBSTRATE_CMD` with `%C`/`%P`,
roster from `shokunin.conf` LANES) into the fleet script and fix, each with a reproduction
before and after: C1 dead path; H1 singleton lock (`flock`); H2 numeric validation of
`.round`; H3/H4 PID liveness and kill of the agent process group, not the wrapper; H5
`report_of` content gate (SHONEN section + minimum size, case-tolerant); M1 `render_prompt`
escaping (`/`, `&`, `\` in axes); M2 the `<{{LANE}}-repo>` placeholder; M5 numeric conf
validation. Add the closure check from `driver.md` §2c, but call
`scripts/sources-census.sh validate --root "$SK" <lane>` (exit 0 required, 2 = census missing →
skip with a logged warning) instead of re-implementing the recount. Bash + coreutils + `flock`.

Verify: `bash -n`, `shellcheck`, and a harness under `/tmp` that exercises each fixed function
(render with hostile axes, round counter with garbage, report gate with an empty and a real
report). Final response: diff summary, each fix with its before/after evidence, residual risk.
