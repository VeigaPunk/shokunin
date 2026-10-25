# mado — round 26 report

Lane `mado-shokunin`, base `96101be5`, one attempt (`MadoR26`, L1 in-session, hyaku phase 4). No
`lane-dead-no-report mado round=26` line existed; nothing inherited. Paths below `.ufo/waves/round-26/` unless
rooted otherwise.

## Work performed

Declared claims (registration `.ufo/waves/round-26/registration.md`, landed `05319e0f` before any control seat):

- **C1 — coverage (sourced: S175–S177, extended S158/S162):** new operation — the animation directive→entry
  expansion (`hyprctl animations -j`), held as `[INF]` at `corpus/knowledge/hyprctl-verification-layer.md:158`,
  becomes a tool `tools/mado-anims.py` and a note `corpus/knowledge/animation-table-r26.md`. Rule:
  `PRED-C1-r26-v2` (counter v2, frozen before data after the w1 critic found v1 meetable by a cache).
- **C2 — operability:** the round-25 bind resolver `tools/mado-binds.py` works on trees whose binds/variables use
  hyprlang `{{…}}` expressions while keeping round-25 behaviour on a 20-case sample. Rule: `PRED-C2-r26`.

Work items:

- **Host safety first (orchestrator ask):** Hyprland 0.56.2 cannot run headless-only (aquamarine has no allocator
  without a DRM fd: pilot runs 1–2 abort `CBackend::create() failed!`). Each nested Hyprland now runs under its own
  private headless tinywl (wlroots 0.20.2 `d7835334`, patched to wl_compositor/xdg_wm_base v6) inside bubblewrap:
  `--unshare-all --clearenv`, `--tmpfs /run`, private `XDG_RUNTIME_DIR`, only `/dev/dri/renderD129`,
  `LIBSEAT_BACKEND=noop`, `RLIMIT_CORE=0`, stopped by `dispatch exit` — `harness/oracle.py`, `harness/build-tinywl.sh`,
  `harness/tinywl-global-versions.patch`. Pilot `harness/pilot-receipt.txt`: `PILOT ISOLATED_OK`, coredumps
  1335→1335, live instances 1→1. w1 IsolationProbe (`evidence/isolation-probe.txt`): 288 nested pids, 770/770
  samples without `/run/user` or card nodes, live clients 2→2, monitors 1→1, delta 0. w1 OracleDeterminism and w2
  ReviewDeterminism: `ORACLE_READY stable` (hyprctl sees an instance only after its config is applied).
- **Repairs routed by the round-25 spot-check:** (1) M25-2 label-free case paths (random mkdtemp dirs, shuffled
  order; K1/K2LabelKeyed best 2/41, 24/51); (2) counter self-test with a drift-fault witness and an embed fixture
  that a ≥1000 threshold misses (`quality/counter-selftest.py`, green 9/9, red receipts per mutant); (3) M25-4
  population equality → QUALITY 37 + `quality/check-population.py` (red/green `quality/q37-population-red-green.txt`;
  PASS on both after-receipts); (4) M25-3 Q36 successor with `--counter-sha` and fixtures killing 8/8 mutants
  (`quality/q36-mutants.txt`); (5) R8 correction appended to `.ufo/waves/round-25/registration.md`; (6) bind-tool
  `{{…}}` = C2; (7) ledger rows `:1409`/`:1410` second-derived (w1 Rc1409/Rc1410, w2 ReviewRc: agree); (8) missing
  `exit=` of the round-25 before receipt recorded as a lesson correction note (exit 1 derived from
  `round-25/c1/count.py:298`).
- **Controls before data:** C1 v1 9 shapes (`controls/*.txt`), C1 v2 re-scores (`controls/v2/*.txt`, best
  K1NaiveGrep 9/41), C2 6 shapes (best K2LabelKeyed 24/51); landed `1b0b91e9` 09:16:22Z, before the w2 registry
  `createdAt` 09:16:39Z. w2 re-scores (15 seats): none met (C1 ≤13/41, C2 ≤24/51).
- **Data:** ExecAnimToolA (first C1 file returned; landed unmodified) and ExecArithToolB (first C2 file returned;
  landed unmodified). ExecAnimToolB returned a second 41/41 implementation (not landed by rule).
- **Sources:** S173–S177 opened, each re-opened by a w2 reviewer (all agree); S158/S162 `used-by` extended
  (`corpus/lessons/round-26.md` § Gate).
- **Residual call (4 seats):** ResC1Remeasure 41/41 ×2 fresh seeds, tool audit clean; ResNoteReview `NOTE sound
  (0)`; CritClaims advisory: C1 and C2 "not admissible" (one seed per v2 control; C2 dropped env seeding) — see Gate;
  ResC2Remeasure (see Before → after).

## Landed changes

| commit | content | LOG |
|---|---|---|
| `05319e0f` | registration, harness, counters c1 v1 + c2 (before any seat) | LOG round 26 |
| `1b0b91e9` | control receipts (v1, v2, C2), counter v2, w1 reports, before receipts, quality repairs, round-25 R8 correction | LOG round 26 |
| `2b3487f7` | `tools/mado-anims.py` (C1) | LOG round 26 |
| `ca135237` | C1 receipt, animation note, SOURCES S173–S177 + used-by, PROVINCE row, README index/route, verification-layer pointer, QUALITY 37 | LOG round 26 |
| `a496b02a` | `tools/mado-binds.py` with `{{…}}` evaluation (C2) | LOG round 26 |
| `178d3353` | C2 receipt, end census, lesson, SCORECARD results/capabilities, LOG, w2 evidence | LOG round 26 |
| `14fcb814` | residual reports, lesson errata (M26-9, M26-10) | LOG round 26 |

## Before → after measurements

- **C1:** `env -i PATH=/usr/bin HOME=/home/vgpnk python3 -I .ufo/waves/round-26/c1/count-v2.py REV` (sha256
  `4ed70b54…6428`, oracle `680798ed…e441`). Before `96101be5`: `tool=MISSING_TOOL`, 0/41 (v1 receipt
  `evidence/c1-before-96101be5.txt`; under v2 the absent tool is the same 0/41, `controls/v2/K1DoNothing.txt` 0/41).
  After `2b3487f7`: `PRED-C1-r26-v2 cases_pass=41/41 verdict=TARGET_MET`, `ORACLE_VERSION commit=efb50993…`,
  `HOST_SAFETY delta=0`, exit 0 (`evidence/c1-after-v2-2b3487f7.txt`). Residual re-measures: 41/41 ×2.
- **C2:** `env -i PATH=/usr/bin HOME=/home/vgpnk python3 -I .ufo/waves/round-26/c2/count.py REV` (sha256
  `b92c32da…16a8`). Before `96101be5`: 22/51 (`evidence/c2-before-96101be5.txt`). After `a496b02a`:
  `PRED-C2-r26 cases_pass=51/51 embed_hits=0 verdict=TARGET_MET`, exit 0 (`evidence/c2-after-a496b02a.txt`).
  Residual re-measures: 51/51 ×2 (embed audit at every string length clean). Outside `{{…}}` the tool changed in
  three places (env seeding removed — M26-10; 100-pass expansion now drops the line as hyprlang does; an
  escape-strip rewrite fuzz-equivalent over 400k strings).

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: start
`mado ok`, exit 0 (`evidence/sources-start.txt`, 172 rows, 7 pre-existing W04); end `mado ok`, exit 0
(`evidence/sources-end.txt`, 177 rows, same 7 W04). Added: 5 tier-A rows (S173, S174 code hyprlang; S175 docs wiki;
S176, S177 code Hyprland/hyprutils), all `mined`. Touched: S158 and S162 `used-by` + `corpus/knowledge/animation-table-r26.md`
(old→new in lesson § Gate). Frontier: the `[INF]` animations row of the verification layer now points to a sourced
note and a measured tool. Rejected: duplicate-URL rows for HyprCtl.cpp/ConfigManager.cpp, a two-URL S174 row, counter
v1 as C1's rule. Mined mistakes: `corpus/lessons/round-26.md` § Mistakes M26-1…M26-10.

## Trend verdicts

- **expansion: improved** — new operation (animation table) with a tool, a sourced note and five new rows; an
  isolated Hyprland oracle capability (SCORECARD "Capabilities (round 26)").
- **quality: unprovable-but-better** — routed repairs landed with red/green checks (self-test, QUALITY 37, Q36
  successor, ledger re-derivations), but C2 removed the round-25 environment seeding (M26-10), a fidelity trade the
  counter does not see; three gate checks still have surviving mutants (M26-8).
- **discernment: improved** — a pre-data critic finding was turned into counter v2 before data; the residual critic's
  objections are recorded, not argued away; six reopen seats agreed on every new row.

## Gate

- Real rejects: counter v1 as C1's rule (append-only population, unpinned Hyprland) — rejected before data;
  ExecAnimToolB not landed (rule: first returned); duplicate-URL and two-URL source rows rejected.
- Disclosed against the claims (closure to rule): (a) registration §Controls asked two seeds per control; the v2
  re-scores before data had one seed each (more seeds came from w2 Rescore seats, concurrent with data) — M26-9;
  (b) C2's tool no longer seeds variables from the environment (closes the out-of-`--home` channel the round-25
  spot-check routed, but diverges from hyprlang on env-using trees) — M26-10; (c) the validator-rendered task texts
  of w1/w2/res were sent with the operator's tooling-directive block appended — M26-4; (d) tool-sandbox
  `/proc/1/environ` exposes the launcher environment (both measurements ran under `env -i PATH HOME`) — M26-5;
  (e) Hyprland coredump records 1330→1338 this round: 5 failed pilots before isolation worked, 3 from seat crash
  probes inside the sandbox; every counter receipt delta 0 — M26-2, M26-6; (f) the Q36 successor exits 1 on round 26
  (receipts are `.txt`, it expects `controls/*.md`); chronology holds by 17 s.

## Round shape

Two v1 waves + residual: w1 40 seats (executor 13, mutation-tester 11, scribe 8, critic 2, reviewer 2, scout 2,
sentinel 1, connector 1); w2 34 seats (mutation-tester 18, reviewer 10, executor 4, scribe 1, critic 1); residual 4
(reviewer 3, critic 1). Round total 78. Dead seats: none; cancelled: ExecArithToolA (C2 had landed; settle). L1 holds
the §3 planner seat. Wave specs/registries: `w1-spec.json`, `w1-run.json`, `w2-spec.json`, `w2-run.json`.

## SHONEN

- [~] SKILL.md decision tables / cited sources — `corpus/knowledge/animation-table-r26.md` (S175–S177, S158, S162); SKILL.md unchanged.
- [~] End-to-end domain task logged — LOG.md "Round 26" entry; `evidence/c1-after-v2-2b3487f7.txt`, `evidence/c2-after-a496b02a.txt`.
- [~] Executable without oral context — `python3 -I tools/mado-anims.py --home DIR` (PROVINCE row, docstring); `harness/pilot.py`.
- [~] No cross-domain bleed — PROVINCE.md `tools/mado-anims.py` row; `git diff --stat 96101be5 -- tools/` touches only mado-anims.py (new) and mado-binds.py (C2).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: `meson` 1.12.1 via `uv tool install meson` (to build wlroots 0.20.2/tinywl from the official
freedesktop source into `/fast/scratch/hyaku/mado-r26/wlroots`, for the isolated oracle). No pacman transaction.
Seats reported no installs.

L0 questions: none opened.
