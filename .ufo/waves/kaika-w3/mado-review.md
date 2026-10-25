# kaika W3 — non-author verification: mado round 12

Lane head `aeb33b5efe67bb09b4c057bd5ffcec8acb481488`; base `e1d81d480`. Reviewer `W3ReviewMado` (fresh dispatch, not the lane's seats).
Scratch clones at `aeb33b5` and `e1d81d4` (`git clone --no-checkout <lane>` + `git checkout --detach`). Lane worktree untouched (read-only; `git -C … status --porcelain` empty).

## 0. Recommendation

**HOLD — do not admit as landed.** Return to the lane for one blocking fix and two wording fixes. C1, C2 and C3 measure as claimed; the blocker is check 4.

- Blocking: `sources-census.sh validate` exits **1** (E04, duplicate URL). Row S030 re-registers S017's URL. See §4 and defect B1.
- Once `validate` exits 0 and the depth/adjacency wording is corrected (M2), I recommend **admit** with claim verdicts C1 verified, C2 verified (conditional on L0 #1), C3 verified (capability admitted on a clean `validate`).

## 1. Provenance (check 1)

Command: `git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' e1d81d480..aeb33b5ef`

- 8 commits (`a6528e6 … aeb33b5`). Every commit: author and committer `mado-shokunin <mado@shokunin.local>`.
- **verified.**

## 2. Append-only (check 2)

Command: `git diff --numstat e1d81d480..aeb33b5ef -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md`

| path | +/- | prior lines deleted/modified |
|---|---|---|
| LOG.md | 106 / 0 | none |
| corpus/QUALITY.md | 22 / 0 | none (hunk `@@ -8,0 +9,22 @@`) |
| corpus/lessons/round-12.md | new file | n/a |
| corpus/SOURCES.md | new file (114 lines) | n/a (absent at base) |

Command: `git diff -U0 e1d81d480..aeb33b5ef -- LOG.md corpus/lessons corpus/QUALITY.md | grep -nE '^-[^-]'` → no output.

Outside the listed paths, `tools/mado-verify.sh` (17+/3−) has three deleted lines: the `for f in … ai-usage …` fixture list, `PIN_MADO='dc7c4141…'`, and the closing `'~/.config/hypr/ai-usage.conf' )` of `EXPECT`. The `dc7c4141` pin is preserved as text in LOG.md and SCORECARD.md. The change is recorded as a gate erratum (S014). Not a violation of the listed paths; noted as info.

- **verified** (append-only on the listed paths).

## 3. Claims (check 3)

Measured by `after-measure.sh` (lane file, blob sha256 `096d3351…`; only change: scratch path substituted for `/tmp/mado-r12-*`), run in each clone with `REV=<rev> MADO_VERIFY_HARNESS=/home/vgpnk/Projects/shokunin/tameshi-shokunin/tools/mutate-and-run.sh` (harness sha256 `75ed934d…`). Outputs: scratch `out-head.txt` / `out-base.txt`, reproduced below.

| Claim | Command (as in after-measure.sh) | base `e1d81d4` | head `aeb33b5` | report before→after | verdict |
|---|---|---|---|---|---|
| C1 calibration | `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md` / `grep -cE '^[0-9]+\. ' corpus/QUALITY.md` + resolver loop | 0 / 5 → 0.0000 | 11 / 16 (resolver 11) → 6.8750 | 0/5 → 11/16 = 6.8750 | **verified** |
| C1 strict | `grep -E '^[0-9]+\. .*lessons/round-12.md#mistakes' corpus/QUALITY.md \| wc -l` | 0 | 9 → 5.6250 | 9/16 | **verified** |
| C2 freshness | `bash tools/mado-verify.sh --no-live \| awk '$3=="FAIL"\|\|$3=="UNKNOWN"' \| wc -l` | 1 | 0 | 1 → 0 | **verified** |
| C2 pass | `… awk '$3=="PASS"' \| wc -l` | 28 → 9.6552 | 29 → 10.0000 | 28/29 → 29/29 | **verified** |
| C2 claim-level | `grep -c '^> Erratum (round 12' SKILL.md` ; `grep -c '^## Errata (round 12)' SKILL.md` | 0 ; 0 | 1 ; 1 | "1 → 0" contradictions | **verified** |
| C3 coverage | join loop (after-measure lines 23–25): distinct `covers: U#` on sourced entries; `mined` row × entry join | 0/7 (`corpus/SOURCES.md` absent; awk fatal) | U1, U2, U3 → 3/7 = 4.2857; join prints no violation | 0/7 → 3/7 | **verified** |

Harm watch (same run):

| Check | base | head | verdict |
|---|---|---|---|
| navigation counter `bash -s` (sha `8b59b503…`) | `indexed=22/22 … exit=0` | `indexed=26/26 … exit=0` | no harm |
| `--selftest` | 268/268 | 269/269 | no harm |
| live gate `bash tools/mado-verify.sh` | `pass=51 fail=1` DIVERGED (include_graph) | `pass=52 fail=0 note=8` CLEAN | improved |
| `--regression` | PASS (target `dc7c4141…`) | PASS (target `538d178b…`) | no harm |
| gate sha256 | `93e43f8f…` | `ea798ad0…` | by design (EXPECT + PIN_MADO) |

Knowledge count (observational, same run): `ls corpus/knowledge/*.md | wc -l` 22 → 26; triple-header (`source:`/`verified-at:`/`recheck:` in head 15) 3 → 7.

Host dependence: C2 and the live gate read the live host; the base result (1 FAIL on `hypr.root.include_graph`, 18 vs 17 lines) is reproduced today. Host re-check: `sha256sum ~/.config/hypr/hyprland.conf` = `ce7483f3…`, `wc -l` = 32, `grep -cE '^[[:space:]]*source'` = 18 — all match the drift entry.

## 4. SOURCES (check 4)

Command (verbatim): `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mado-shokunin`

```
mado-shokunin	E04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules
validate-exit=1
```

Cause: S017 and S030 share the URL `https://wiki.hypr.land/Configuring/Basics/Window-Rules/` (`corpus/SOURCES.md` lines 28 and 41). S030's `teaches` has no `supersedes S0NN —` (the validator's exemption). Contract rule 2 (`SOURCES-CONTRACT-v1.md:49-50`) permits re-registration only as "a correction … whose `teaches` opens `supersedes S0NN —`". S030 was added in `5174e15`, so the defect is present at `6e3b75f` too.

The contract census block (`SOURCES-CONTRACT-v1.md:66-80`, run by after-measure) is clean at head: rows 39; malformed 0; dup ids none; tiers A=35 B=1 C=3; status mined=28 queued=9 rejected=2; enum/tier-inflation none; `mined` used-by missing none. The `validate` E04 check is not in that block — this is the gap.

Rows re-opened (all URLs fetched 2026-10-19 by this reviewer):

| row | tier / status | re-open result |
|---|---|---|
| S018 (new tier-A code) | A / mined | `raw.githubusercontent.com/hyprwm/Hyprland/v0.56.2/src/debug/HyprCtl.cpp`: line 1463 `static std::string dispatchGetProp`; line 1566 `return alphaToString(PWINDOW->m_ruleApplicator->alpha(), true);` — matches Gate (lesson line 72) ✓ |
| S017 (new tier-A docs) | A / mined | `wiki.hypr.land/Configuring/Basics/Window-Rules/`: "All props must match for a rule to be applied." present ✓ |
| S030 (new tier-A docs) | A / mined | same page, `hl.window_rule({ match = { class = "my-window" }, border_size = 10 })` present (HTML-entity-escaped) ✓ — but duplicate of S017 (E04) |
| S024 (new tier-A docs) | A / mined | `hypr.land/news/26_lua/`: "The old hyprlang syntax will continue to be supported for 1 - 2 releases starting from 0.55." ✓ |
| S012 (rejected, tier C) | C / rejected | `filipmikina.com/blog/hyprwhenthen`: "This works if the window class/title is known at creation time." ✓; no Hyprland version string on the page (grep `version` → no hits) — rejection premise holds |
| S011 (rejected, tier C) | C / rejected | local `fleet-ledger/MANIFEST.json:1767`: "training r1 (lane round 2): live-verification layer — 65 hyprctl claim->live pairs, 0 mismatch" ✓ |
| S019, S020, S013, S014, S015, S002, S001 (local rows) | A | anchors and quotes exist: `getprop-measure.txt` "0.97"; `terminals.conf:4` ✓; `install.sh:34` ✓; `mado-verify.sh:2193` Erratum above `EXPECT` (2203) ✓; `omarchy-drift-watch.md:285-286` ✓; `arc-synthesis.md:300` ✓; `round-10.md:65` ✓ |
| S004 | A | `fleet-ledger/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:45` "Write it only after opening the source in the round that writes" ✓ |

Anchor-revision defect (contract `anchor` rule, `SOURCES-CONTRACT-v1.md:32-33`: "plus revision (version, commit, or publication date)"): S006, S008, S009, S010 carry only "opened 2026-10-19" (an access date). All four are `queued`. S015 (own-work) has line numbers but no commit.

## 5. Discernment spot-check (check 5; `LEARNING.md:37-41` requires ≥1 admit and ≥1 reject)

| # | item | gate decision | reviewer | reason |
|---|---|---|---|---|
| 1 | `corpus/knowledge/window-rule-effects-getprop.md` (U1) | admitted | **agree** | Header trio ✓; `covers: U1`; every `S#` in `source:` has a `mined` row whose `used-by` names the file (S002, S016–S020 checked in SOURCES.md); observation/inference tagged `[OBS]`/`[INF]`; `## Corrects` names `arc-synthesis.md:300` (the stale "no rule-read verb" line, verified) and `config-health-report-r3.md:449`. Live recheck: `hyprctl version` = 0.56.2 `efb5099`; `hyprctl getprop class:Alacritty opacity` = `0.97`; `… opacity_inactive` = `0.9` (entry line 14 ✓). |
| 2 | S012 (filipmikina, tier C) | rejected | **agree** | Community tier C; third-party page with no Hyprland version; its rule-era statements cannot bind to an era. Flip condition written. Consistent with contract rule 1 and the Gate. |
| 3 | S030 (admitted row, `mined`, tier A) | admitted (as a second row for S017's page) | **disagree** | Same URL and page as S017; the fleet validator (E04) rejects it and no lesson records the duplicate. The lane's own gate did not catch it. Must be fixed or learned in the round lesson (LEARNING "disagreement left unlearned" = harm). |

Sample size is 1 admit + 1 reject (+1 disagreement on a registry row). The lane has not recorded the spot-check in its lesson; this table is the reviewer record for the orchestrator to append.

## 6. New knowledge entries (check 6)

| entry | `source:` / `verified-at:` / `recheck:` | recheck run | claim vs source |
|---|---|---|---|
| `config-drift-r12.md` | ✓ / ✓ / 2027-01-17 | host `sha256sum`, `wc -l` (32), `source` count (18) — match | S013 `install.sh:34` ✓ |
| `window-rule-effects-getprop.md` | ✓ / ✓ / 2027-01-17 | `hyprctl getprop class:Alacritty opacity` → 0.97; `opacity_inactive` → 0.9 | S018 line 1566 ✓; `[INF]` labelled ✓ |
| `hyprland-config-era-r12.md` | ✓ / ✓ / on-release | S024 quote fetched ✓ | S021–S030 quotes present ✓ |
| `xdg-portal-routing-r12.md` | ✓ / ✓ / 2027-01-17 | `/usr/share/xdg-desktop-portal/hyprland-portals.conf` = `default=hyprland;gtk` ✓; `busctl --user get-property … ScreenCast version` = `u 6` ✓; pacman: xdph 1.4.1-2, xdp 1.22.1-2 ✓ | S031–S037 mined rows ✓ |

All four: **verified.**

## 7. Credentials (check 7)

Command: `git diff e1d81d480..aeb33b5ef | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (rc 1). **verified.**

## 8. Report conformance (check 8)

Report `fleet-ledger/.ufo/reports/round-12/mado.md`: sections present in order: Work performed, Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes ✓. Cites round head `aeb33b5` ✓. SHONEN: four `[~]`, no `[x]` ✓. Fleet-root `LOG.md` contains no "Post-integration review" text (`grep -c` = 0) — the misplacement was restored ✓.

Conformance defects:
- Measured-commit: report measures after-numbers at `6e3b75f`, not the round head. Identical at `aeb33b5` (§3). Minor.
- Integrator notes say "operability, depth and adjacency unchanged". The lane's own SCORECARD (lines 239–240) marks depth and adjacency **unscored** ("no bounded rubric exists"). Contradiction — see M2.
- Seat-level claims (14 L2 seats, `/skill:godspeed` prefix, two refused dispatches) rest on `.ufo/evidence/round-12/l2-*.md` (14 files present); the verbatim prompt bytes were not re-verified.

## 9. Recommended per-axis verdicts (SCORECARD axes)

| axis | recommended verdict | evidence |
|---|---|---|
| calibration | **improved** (measured) | C1 0.0000 → 6.8750 (strict 5.6250); discernment part recorded in §5 |
| freshness | **improved**, conditional on L0 #1 | C2 9.6552 → 10.0000; the EXPECT change re-anchors a gate baseline to the observed host — protocol-compliant (erratum appended, `omarchy-drift-watch.md:284-287`), but the credit depends on whether gkeep is kept |
| coverage | **improved** | C3 0 → 3/7 (4.2857); capability "sources registry" admitted only after `validate` exit 0 |
| operability | **unchanged** | selftest 268 → 269 (both 10.0000, saturated); live gate CLEAN; no harm |
| depth | **unscored** (not "unchanged") | SCORECARD.md:239; the new entries may add depth but no rubric exists; known defect D7 |
| adjacency | **unchanged**, watch | Gate EXPECT now pins `~/.config/hypr/gkeep.conf` (operator-owned); reported, not absorbed; L0 #1 |

## 10. Trend verdicts (LEARNING.md)

- **expansion: improved.** Admitted entries on uncovered ground: 3 (U1–U3, `covers:` joined to `mined` rows, §3). Knowledge notes 22 → 26.
- **quality: improved, one registry defect open.** Live gate DIVERGED → CLEAN; triple-header 3/22 → 7/26; drift stale-entry re-anchored with an erratum. No admitted entry found false. Registry E04 (B1) is open.
- **discernment: unprovable-but-better on this sample; not yet promotable.** Agree on 1 admit and 1 reject; disagree on S030 (duplicate, unlearned). Becomes `improved` when S030 is fixed or learned in the lesson with a grounded criterion.

## 11. Defects by severity

- **B1 (blocking).** `validate` exit 1, E04 duplicate URL (S017/S030). Fix: merge S030 into S017 (repoint `hyprland-config-era-r12.md` `source:`/`used-by`, drop S030's Gate record) or give it a `supersedes S017 —` `teaches` with a real correction; re-run `validate` to exit 0.
- **M1 (medium).** Anchors S006, S008, S009, S010 lack a publication date, version or commit (access date only); contract `anchor` rule. Fix: add the page's publication/modified date or release.
- **M2 (medium).** Depth and adjacency are "unchanged" in the report's Integrator notes but "unscored" in SCORECARD.md:239–240. Fix: say "unscored" in the report and the integrator line.
- **L1 (low).** Measured at `6e3b75f`, not the round head. Fix: cite both in the report (reproduces at `aeb33b5`).
- **L2 (low).** Discernment record absent from the lesson (`LEARNING.md:37-41`). Fix: append the §5 table (orchestrator-recorded).
- **L3 (info).** Freshness credit conditional on gkeep status (L0 #1); adjacency watch on the gkeep EXPECT pin.
- **I1 (info).** `tools/mado-verify.sh` changed three prior lines (PIN_MADO, EXPECT, fixture list); old pin preserved in LOG/SCORECARD; erratum present.

## 12. Limits

- Re-ran every counting command at both revisions via `after-measure.sh`; live-host rows reflect 2026-10-19 host state.
- Web re-opens: S012, S017, S018, S024, S030 (fetched by this reviewer). Other rows checked by quote-grep against local files or not re-opened.
- Scratch `/tmp/kaika-verify/mado/` removed after this file was written. No write to the lane, the ledger, or the fleet root.
