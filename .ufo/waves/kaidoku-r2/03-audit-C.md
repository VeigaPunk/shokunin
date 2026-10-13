# kaidoku-r2 · 03-audit-C — round-2 re-verification audit of round-1 knowledge files

Audit lane: kaidoku-shokunin round 2. Date: 2026-10-13 ~12:20 -03 (host plazir27, uptime 1:24 — one reboot since round 1's morning passes). All commands re-run live; nothing installed or modified. `/tmp/rea-jq.snap.json` and round-1 `/tmp` artifacts are gone (tmp cleared across reboot); snapshot mechanism was re-verified with a fresh snapshot in a scratch dir.

## File: corpus/knowledge/2026-10-13-rea-live-jq-e2e.md

### Verify: `timeout 600 npx -y rea-agents@6.4.0 analyze /usr/bin/jq --format json | python3 -c "...procedure_count"` → expect 167
- result: not-rerun — full `rea analyze` skipped as expensive per lane mandate. Indirect corroboration: `rea decompile 0x103fa0` and `rea search "usage"` both paid the full Ghidra import and returned coherent jq evidence (provider `ghidra` 12.1.4, `ephemeral-source-immutable`), so the pipeline itself is still functional.

### Verify: `(npx ... analyze & sleep 2 && ls /tmp/rea-ghidra-*/project/rea-project.gpr && wait && ! ls -d /tmp/rea-ghidra-*)`
- result: not-rerun — runs full `rea analyze`. Note: two `/tmp/rea-ghidra-{a6ke9Q,kfMwyc}` dirs existed mid-audit, attributable to a concurrent sibling lane (`/tmp/rea-pe-*.json`, `/tmp/rea-capabilities.json` at 12:19–12:21), consistent with the file's own coexistence claim but not a verbatim re-proof of self-cleaning.

### Verify: `npx -y rea-agents@6.4.0 search /usr/bin/jq "usage" --kind strings --snapshot /tmp/rea-jq.snap.json`
- result: drifted — `/tmp/rea-jq.snap.json` no longer exists (reboot wiped /tmp). Mechanism re-verified in a scratch dir: `search ... --snapshot snap.json` wrote a mode-0600 JSON with exactly keys `['binding','entries','evidence_bundle','target','workflow_entries']` and returned the identical usage-text hit at `0x1052c8`. Claim holds; the round-1 artifact is gone.

### Verify: `npx -y rea-agents@6.4.0 inspect-binary-layout /usr/bin/jq --format json` → expect `provider_unavailable`
- result: confirmed — identical typed error, `candidate_ids:["pwntools-elf"]`, remediation demands `REA_PWNTOOLS_PYTHON` with pwntools 4.15.0 + pyelftools 0.33 + Unicorn 2.1.2, exit RC=1 fast.

### Verify: `npx -y rea-agents@6.4.0 decompile /usr/bin/jq 0x103fa0 --format json | grep -c FUN_` → >0
- result: confirmed — FUN_ present (JSON single-line so `grep -c`=1 line); body references `jq_start`×2, `jq_next`×2, `jv_dump`×8, `raw-output0`×2 — still recognizably jq's `process()` loop. Cross-check `nm -D /usr/bin/jq` → 46 `jq_*`/`jv_*` undefined imports.

### Verify: `npx -y rea-agents@6.4.0 search /usr/bin/jq "" --kind procedures` → VALIDATION_ERROR; `--token-limit 10 --format json` → UNSUPPORTED_OUTPUT_COMBINATION
- result: confirmed — both errors reproduced verbatim (zod `too_small` ≥1 char; "Token windows cannot preserve structured output… use --filter-output or command pagination").

### Verify: `npx -y rea-agents@6.4.0 doctor --format json` → failing checks list
- result: confirmed-with-drift — `healthy:false` still; ghidra checks still absent from the failing list (still green). Failing set now: `hopper, ida-registration, skill:identity, registration:{claude_code,codex,grok_build,opencode,pi}` (8 rows). Round 1 named pwntools-python among missing items — it is not a scope_check failure now; the named drift is in the enumerated set, not the verdict.

### Verdict audit: candidate 1 (analyze→search→decompile pipeline) — agree — every non-analyze leg re-ran green through the same Ghidra provider; 167-count trusted from round 1's three consistent runs.
### Verdict audit: candidate 2 (ephemeral /tmp sessions) — agree — shipped source + round-1 direct observation stand; could not verbatim re-prove cleanup without `rea analyze`, and the live sibling-lane dirs corroborate session-tree shape.
### Verdict audit: candidate 3 (--snapshot is evidence persistence, not DB cache) — agree — fresh snapshot shows identical key schema and the search worked over it; claim unaffected by the stale artifact's disappearance.
### Verdict audit: candidate 4 (inspect-binary-layout fails closed) — agree — identical typed negative reproduced.
### Verdict audit: candidate 5 (stripped decomp usable for triage) — agree — FUN_/param_N naming cost confirmed; callees/strings still carry semantics.
### Verdict audit: candidate 6 (typed cheap validation failures) — agree — both error codes byte-equivalent.
### Verdict audit: candidate 7 (doctor red ≠ unusable) — agree — ghidra green, top-level false still driven by hopper/registration/skill rows; slight drift in the enumerated missing set (pwntools absent from scope_checks now).

## File: corpus/knowledge/2026-10-13-asar-surface.md

### Verify: `find /usr/lib /opt ~/.config -maxdepth 6 -name '*.asar' | wc -l` → 6; `find ~/.config ... ` → empty
- result: confirmed — exactly the same 6 paths (obsidian×2, signal-desktop, 1Password, electron39, electron43); `~/.config` still contributes zero.

### Verify: `cat /usr/bin/obsidian; cd $(mktemp -d) && npx -y @electron/asar extract-file .../app.asar main.js && grep 'app.asar\|registerSchemesAsPrivileged'`
- result: confirmed — launcher still `exec electron43 /usr/lib/obsidian/app.asar`; extracted main.js has `protocol.registerSchemesAsPrivileged([` at line 14 and the `indexOf('app.asar')` APP_PATH strip at line 35; `pacman -Q obsidian` = 1.13.7-2 still matches package.json claim.

### Verify: `file /usr/lib/obsidian/app.asar && asar list | wc -l` → "data" yet 54 entries
- result: confirmed — `app.asar` still misdetected as `data` while `obsidian.asar` reports `Electron ASAR archive`; `asar list` returns 54 / 380 entries respectively.

### Verify: `find /usr/lib /opt -maxdepth 6 -name '*.asar.unpacked' -o -name '*.node' -path '*unpacked*'`
- result: confirmed — richer than claimed: obsidian `btime`/`get-fonts` binding.node present AND `signal-desktop/resources/app.asar.unpacked` plus `/opt/1Password/resources/app.asar.unpacked/index.node` also exist. Claim understated, not wrong.

### Verify: `cd $(mktemp -d) && asar extract-file .../app.asar package.json && ls` → file in cwd
- result: confirmed — `package.json` (352 B) materialized in cwd, RC=0.

### Verify: `asar list /opt/1Password/resources/app.asar | grep -cE '^/[0-9]+\.js$'`
- result: confirmed — 407 numeric-chunk entries out of 486 total; webpack-flattening claim holds.

### Verify: `npx -y rea-agents@6.4.0 doctor 2>&1 | grep -A3 'name: ghidra$\|name: hopper'`
- result: confirmed — ghidra family green, hopper failing (`healthy:false` overall), per the doctor re-run above.

### Verify: `rea --help | grep -iE 'javascript|electron|asar'`; `sed -n '45,52p' ~/.agents/skills/reverse-engineer-anything/SKILL.md`
- result: confirmed — 13 matching help lines incl. `analyze-javascript-application`, `recover-javascript-sources`, `compare-application-versions`, `list-electron-targets`, `inspect-electron-page`, `capture-electron-scenario`, `reconcile-javascript-runtime`; SKILL.md still routes "ASAR or extracted JavaScript/Electron tree → `analyze_javascript_application`".

### Verify: `head -5 /usr/bin/signal-desktop /usr/bin/obsidian`
- result: confirmed — signal-desktop bash wrapper execs `/usr/lib/signal-desktop/signal-desktop` (line 11); obsidian execs system `electron43`. Versions: signal-desktop 8.26.0-1, electron39 39.8.10-2, electron43 43.6.0-1.

### Verify (REJECT row): `cd $(mktemp -d) && asar extract-file .../app.asar package.json > out.txt; wc -c out.txt package.json`
- result: confirmed — `out.txt` 0 bytes, `package.json` 352 B on disk. extract-file is definitively NOT a stdout streamer.

### Verdict audit: all nine `suggested: admit` rows — agree — every claim reproduced; the .unpacked finding is stronger than recorded (signal/1Password unpacked trees add native surface).
### Verdict audit: `suggested: reject` (extract-file streams to stdout) — agree — falsification re-verified byte-for-byte (0-byte stdout, file on disk); correct calibration entry.

## File: corpus/knowledge/2026-10-13-pacman-packages.md

### Verify: `pacman -Qo /usr/bin/jq && pacman -Ql jq | wc -l`
- result: confirmed — `jq 1.8.2-1`, 25 files.

### Verify: `tar -tf .../acl-2.4.0-1-x86_64.pkg.tar.zst | grep '^\.' ; tar -xOf ... .BUILDINFO`
- result: confirmed — `.BUILDINFO/.MTREE/.PKGINFO` all present; buildtool `devtools 1:1.5.1-1-any`, PKGBUILD sha256 `187dc04a…` as recorded.

### Verify: `cd /var/cache/pacman/pkg && for f in *.pkg.tar.zst; do [ -f "$f.sig" ] || echo unsigned; done`
- result: confirmed — 1556 `.pkg.tar.zst` + 1556 `.sig`, zero unsigned output; `du -sh` 8.6G (new `download-CCWD4f` partial dir is root-only, permission-denied to du — cosmetic).

### Verify: `tar -xOf .../jq-1.8.2-1...usr/bin/jq | sha256sum; sha256sum /usr/bin/jq; pacman -Qkk jq`
- result: confirmed — both `e8156675…7806`; `25 total files, 0 altered files`.

### Verify: `pacman -Qo ~/.local/bin/jq; file/sha256sum both jq binaries`
- result: confirmed — still unowned, statically linked stripped, sha `b1c22172…70f`; `which jq` → `/home/vgpnk/.local/bin/jq` (shadow still first on PATH).

### Verify: `pacman -Qm; ls /var/cache/pacman/pkg | grep -E 'elephant|walker'`
- result: confirmed — 14 foreign rows (13 `elephant-*` 2.21.0-1 + `omarchy-walker 1.0.0-2`); cached archives+sigs present.

### Verify: `ls /var/lib/pacman/sync/; grep -E '^\[' /etc/pacman.conf`
- result: confirmed — five DBs (incl. orphan `offline.db`) vs four configured repos; `omarchy.db` zstd vs gzip officials.

### Verify: `ls *.pkg.tar.zst | sed -E ... | sort | uniq -d`
- result: confirmed — duplicate-version corpus grew since round 1 (all three round-1 examples present plus many more, e.g. dotnet-host, linux-firmware splits); claim direction strengthened.

### Verify: `command -v pacman tar file zstd gpg sha256sum vercmp expac bsdtar; command -v paccheck pactree pacfiles`
- result: confirmed — all tier-1 tools present; pacman-contrib still absent.

### Verdict audit: all nine `suggested: admit` rows — agree — every verify reproduced exactly; no drift detected on this surface.

## File: corpus/knowledge/2026-10-13-managed-assemblies.md

### Verify: `dotnet --info && dotnet --list-sdks; which mono monodis ilspycmd ildasm csc mcs pwsh; ls /usr/lib/mono`
- result: confirmed — host 10.0.11 (RID arch-x64), runtimes 9.0.19 + 10.0.11, "No SDKs were found"; none of the managed tools on PATH; `/usr/lib/mono` absent.

### Verify: `find /usr/share/dotnet/shared -name '*.dll' | wc -l; file .../System.Private.CoreLib.dll`
- result: confirmed — 341 total, split verified per version: 172 (10.0.11) + 169 (9.0.19); CoreLib is `PE32+ … Mono/.Net assembly`.

### Verify: `file /usr/lib/pinta/Pinta.dll; find /usr/lib/pinta -name '*.dll' | wc -l; cat Pinta.runtimeconfig.json`
- result: confirmed — 36 DLLs, Pinta.dll Mono/.Net assembly, TFM `net10.0`.

### Verify: `file /usr/lib/pinta/Mono.Cecil.dll; dotnet tool list --global`
- result: confirmed — Cecil present as Mono/.Net assembly; `dotnet tool` fails with "No .NET SDKs were found" (fuller error text than round-1 quote, same meaning).

### Verify: `which ilspycmd ildasm ilasm monodis dnSpy; ls -d ~/.dotnet/tools ~/.nuget/packages`
- result: confirmed — all absent; no tool dirs.

### Verify: `file DBZMON.exe; find /opt -maxdepth 8 -name '*.dll' -o -name '*.exe' | wc -l`
- result: confirmed — DBZMON.exe still native PE32+ x86-64 stripped; `/opt` still yields 0 managed/native app DLLs (caveat: `/opt/containerd` is permission-denied to this user — same bounded read as round 1).

### Verdict audit: all six `suggested: admit` rows — agree — managed surface unchanged; counts exact, tooling gap still real.

## File: corpus/knowledge/2026-10-13-crash-evidence.md

### Verify: `coredumpctl list --no-pager | tail -n +2 | wc -l; du -sh /var/lib/systemd/coredump/`
- result: confirmed — still 175 entries (174 `present` + 1 `missing`), 174 `.zst` on disk, 4.0G. Core count did NOT decay since round 1 — identical totals; retention window held across the day's reboot.

### Verify: `getfacl .../core.waybar...zst | grep user:vgpnk; coredumpctl info 1728 | head -30`
- result: confirmed — `user:vgpnk:r--` ACL grants present; `coredumpctl info 1728` returns full metadata + symbolized stack (`raise→abort→__cxa_throw→waybar`); `zstd -dc` still yields `7f 45 4c 46` ELF magic.

### Verify: `coredumpctl list | grep -oP '/usr/\S+' | sort | uniq -c`
- result: confirmed — identical distribution: 133 chromium, 39 `/usr/bin/bash` (crash-godot SI_USER noise), 1 godot, 1 waybar, 1 localsearch-extractor-3. Three organic crashes unchanged.

### Verify: `ls /var/crash /var/lib/apport /var/spool/abrt; grep -v '^#' /etc/systemd/coredump.conf | grep -v '^\['`
- result: confirmed — all alt-collector paths absent, apport/abrtd not installed, coredump.conf still 100% defaults.

### Verify: `journalctl -p err -b | grep -v 'sr0\|Buffer I/O'; journalctl -k | grep -icE 'oops|general protection fault'`
- result: drifted — kernel-oops count still 0 and error surface still noise-only (TDX/snapper/keyring), BUT `journalctl --list-boots` now shows 13 retained boots (2026-10-03→10-13), not the claimed 10 (2026-10-04→10-13). Boot-retention count and span drifted post-reboot; the "no panic/oops" substance is unchanged.

### Verify: `coredumpctl list --no-pager | head -3`
- result: confirmed — earliest row is still the same chromium SIGTRAP 2026-10-08 14:01 with COREFILE `missing`; still exactly 1 missing — no further oldest-first reaping since round 1.

### Verify: `echo 'bt' | coredumpctl debug 1728 2>&1 | head -20`
- result: confirmed — gdb attaches to the decompressed waybar core non-interactively and returns metadata + stack.

### Verdict audit: all seven `suggested: admit` rows — agree — including the decay claim, which is now a stable observation (1 missing, unchanged) rather than active loss; the journal-boots count is the only stale figure (10→13).

## Deliberate REJECT audit
- `asar extract-file streams to stdout` (2026-10-13-asar-surface.md): re-verified — 0-byte stdout, member materialized to cwd, RC=0. Reject upheld.
- `mcp-config` reject: not present in the five assigned files. The mcp-config evidence file (`corpus/knowledge/2026-10-13-mcp-registrations.md`, staging `04-mcp-config`) is outside this lane's audit set and carries no `suggested: reject` row of its own; the corpus's other reject rows live in `2026-10-13-doctor-taxonomy.md` (×2) and `2026-10-13-elf-observation-jq.md` (×1) — also outside the assigned five.

## Summary
34 verify-command groups re-run across 5 files: 30 confirmed, 2 drifted (snapshot artifact gone post-reboot — mechanism re-proven; journal boot count 10→13), 0 fails, 2 not-rerun (both `rea analyze` — expensive). All 38 `suggested: admit` verdicts upheld; the audited `suggested: reject` (asar extract-file stdout claim) upheld with fresh falsification. Crash corpus shows zero decay since round 1 (still 175 entries / 174 cores / 4.0G / same single missing row) though its timeliness warning remains valid. Net drift is cosmetic: host rebooted once (uptime 1:24), /tmp scratch evidence is gone, doctor's failing-check enumeration shifted slightly (registration rows named; pwntools not a scope_check), and the pacman duplicate-version corpus grew. No round-1 claim is contradicted.
