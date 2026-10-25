# kaidoku — round 4 report (2026-10-13)

**Shape:** tower-coordinated swarm on Devin — 16 lanes (`run_subagent`,
`subagent_general`) under `.ufo/waves/kaidoku-r4/` plus a 6-lane unlock wave
`.ufo/waves/kaidoku-r4u/` after the operator authorized installs. Lanes 01–04
audited round 3 on every moved axis; 05–16 expanded; r4u exercised the newly
provisioned provider gates. Parent integrated. Two expansion lanes
(signal-asar, real version-pair) were still in flight at integration — they
land as a follow-up.

## Axes moved

- **Discernment — verified by audit, strengthened.** All r3 knowledge entries
  re-verified (~34+ verify groups, 0 contradictions). Audits produced **10
  errata** appended in place (append-only): EVM `bytecodeOffset` = jump-dest,
  typora ratio 99.38%, list-* census 11 + MCP-only verbs, renderer-asar
  `grep -c`→`grep -o|wc -l` recipe + constraint census 29, managed AnyCPU
  precision, jq-shadow ~1ms timestamp, crash oversize error class +
  `coredumpctl` decompression, weak-dylib `undetermined`, appimage envelope
  precision, **evidence ids are `f(content,path,params)`** (three-lane
  corroboration incl. an independent revenger-lane verifier).
- **Expansion — improved.** 11 r4 + 6 r4u knowledge entries. New held
  surfaces: 1Password (hardened shell + 188MB Rust core), `.jsc` Ignition
  disassembly, 4 runtime-observation verbs, JS export-shape compare, managed
  IL (REA + dnfile/dncil two-tool map), binary-layout (pwntools), AppImage
  inner, firmware regions+extract, full Android surface (real Java decompile),
  wakaru source recovery, adb client. Measured walls: >90MB PE → ~900s
  internal deadline; RISC-V → REA's own preflight refusal.
- **Quality — improved.** QUALITY criteria 12–14 + weak-signal 6. SKILL
  decision table now covers the whole held surface including the unlock-wave
  additions; known-limits moved to r4.

## Headline results

- **Wakaru OOM root-caused and FIXED**: REA wraps providers in
  `prlimit --as=1GiB`; the npm node shim cannot init V8 under it. Bind the
  `@wakaru/cli-linux-x64` ELF. Verified end-to-end (`ev_4898906e…`).
- **All six operator-gated surfaces unlocked and exercised**: binwalk,
  unblob, jadx-mcp (correct JAR pinned by sha256), apktool, pwntools (now
  persistent venv), adb, wakaru.
- **Provider-gate diagnosis recipe** recorded: env key → REA's `dist/` spawn
  wrapper → minimal repro outside REA.
- **Evidence-id semantics corrected cross-lane**: `f(content,path,params)` —
  deterministic on same-path reruns, not path-independent.

## Errata applied (round 4)

See `## Errata (round 4)` blocks on r2/r3 knowledge files + LOG.md round-4
entry. Two r3 LOG omissions repaired (verb-family promotion, QUALITY 10–11).

## Round-5 frontier (from r4-16 rescan)

RISC-V deep analysis (REA preflight gate, Ghidra module exists); `.jsc`→source
mapper; >90MB targets with raised deadline/heap; sasquatch recursion; adb on a
live device; process-capture + managed verify/project ops; native call-target
resolution; capture-electron-scenario handshake bug.
