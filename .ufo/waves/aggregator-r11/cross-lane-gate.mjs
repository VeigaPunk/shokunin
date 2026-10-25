#!/usr/bin/env node
// cross-lane-gate.mjs — aggregator lane, round 11 (final training-round re-run).
// Gate id: cross-lane-gate-v1.
//
// WHAT THIS IS
//   A committed, re-runnable verdict script that grades the report-durability
//   half of the aggregator lane's cross-lane quality axis. It scans the fleet's
//   presented round reports (.ufo/reports/round-<R>/<lane>.md) and, for each
//   report, checks three mechanically-checkable claims:
//
//     marker-overwrite         the report path holds a closeout marker, not a
//                              report (body below MIN_REPORT_BYTES). This is
//                              the round-11 report's "report overwrite ->
//                              273 B marker" defect class, confirmed live as
//                              routable row D-153 (round-15 kotoba: 14,715 B
//                              at 4419fb9, a 273 B marker today).
//     cited-commit-missing     the report cites a commit hash that resolves in
//                              no readable repo (the fleet root, its child
//                              repos, or a readable checkout under $HOME).
//     verdict-without-revision the report states a verdict without citing any
//                              commit hash at all — a verdict must carry the
//                              revision it measured.
//
//   Round 11's aggregator report closes with: "Round 12 works the lower
//   cross-lane quality axis (8): re-run the six box-3 verdicts after the
//   round-14-17 lane movement and make report durability an explicit grade.
//   Falsified if a marker overwrite such as kotoba r15 can still pass as a
//   current report or if a verdict lacks the revision it measured."
//   This gate is that explicit grade. The six box-3 corpus verdicts are re-run
//   separately and recorded in the round-11 seat file cross-lane-quality.md.
//
//   Hash citations are checked against every readable repo on the host:
//   pure-digit runs (dates, version numbers) are not hash tokens, declared
//   nonces (the reports' own fake placeholders) are skipped, and a cited hash
//   must contain at least one a-f letter.
//
//   name              cross-lane-gate
//   kind              gate
//   version           cross-lane-gate-v1
//   owner             aggregator lane (/home/vgpnk/Projects/shokunin), round 11
//   write scope       READ-ONLY over every surface it grades. The only writes
//                     are throwaway trees inside os.tmpdir() (--selftest fixtures,
//                     removed before exit).
//   entry command     node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --all
//                     node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --round <R>
//                     node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --report <path>
//                     node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --selftest
//   verdict map       0 = clean
//                     1 = failed            (one or more durability findings)
//                     2 = could-not-evaluate (no round reports anywhere,
//                                             round dir missing, unreadable report)
//   precedence across rounds: 2 > 1 > 0
//   self-test         --selftest ; expected values in
//                     .ufo/waves/aggregator-r11/cross-lane-gate.expected.json

import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { execFileSync } from "node:child_process";

const GATE_ID = "cross-lane-gate-v1";
const MIN_REPORT_BYTES = 1024;
const DEFAULT_ROUNDS = [11, 12, 13, 14, 15, 16, 17, 18];
// Hash tokens need at least one a-f letter: pure-digit runs in these reports are
// dates or version numbers (20260911, 101125103), not commit citations.
const HASH_RE = /\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b/g;
// Declared nonces (the reports' own "fake hash" placeholders) are not citations.
const NONCE_RE = /^(deadbeef|deadc0de|0badc0de|cafebabe)$/;
const VERDICT_RE =
  /\b(verdict|clean|failed|fail|pass|admit-corr|admit|not conformant|dirty)\b/i;

function exists(p) {
  try {
    fs.statSync(p);
    return true;
  } catch {
    return false;
  }
}

function reposToCheck(root) {
  const repos = [{ dir: root, label: path.basename(root) }];
  for (const name of fs.readdirSync(root)) {
    if (!name.endsWith("-shokunin")) continue;
    const dir = path.join(root, name);
    if (exists(path.join(dir, ".git"))) repos.push({ dir, label: name });
  }
  const projects = path.join(os.homedir(), "Projects");
  if (exists(projects)) {
    for (const name of fs.readdirSync(projects).sort()) {
      const dir = path.join(projects, name);
      if (dir === root) continue;
      if (!exists(path.join(dir, ".git"))) continue;
      repos.push({ dir, label: path.join("~/Projects", name) });
    }
  }
  return repos;
}

function resolvableHashes(repos, hashes) {
  const resolvable = new Set();
  if (hashes.length === 0) return resolvable;
  const input = hashes.join("\n") + "\n";
  for (const repo of repos) {
    let out;
    try {
      out = execFileSync("git", ["-C", repo.dir, "cat-file", "--batch-check"], {
        input,
        encoding: "utf8",
        stdio: ["pipe", "pipe", "ignore"],
      });
    } catch {
      continue;
    }
    const lines = out.split("\n");
    for (let i = 0; i < hashes.length; i++) {
      if (lines[i] && !/ missing$/.test(lines[i])) resolvable.add(hashes[i]);
    }
  }
  return resolvable;
}

function roundNumbers(root) {
  const base = path.join(root, ".ufo", "reports");
  if (!exists(base)) return [];
  return fs
    .readdirSync(base)
    .map((name) => {
      const m = /^round-(\d+)$/.exec(name);
      return m ? Number(m[1]) : null;
    })
    .filter(Boolean)
    .filter((r) => DEFAULT_ROUNDS.includes(r))
    .sort((a, b) => a - b);
}

function reportFiles(root) {
  const files = [];
  for (const round of roundNumbers(root)) {
    const dir = path.join(root, ".ufo", "reports", `round-${round}`);
    for (const name of fs.readdirSync(dir).sort()) {
      if (!name.endsWith(".md")) continue;
      const p = path.join(dir, name);
      if (fs.statSync(p).isFile()) files.push({ round, dir, path: p });
    }
  }
  return files;
}

function scanReport(root, resolvableByRound, entry) {
  const rel = path.relative(root, entry.path);
  let body;
  try {
    body = fs.readFileSync(entry.path, "utf8");
  } catch {
    return { report: rel, round: entry.round, verdict: 2, findings: [] };
  }
  const findings = [];
  if (body.length < MIN_REPORT_BYTES) {
    findings.push({ id: "XL-marker-overwrite", kind: "marker-overwrite", bytes: body.length });
  }
  const hashes = [...new Set(body.match(HASH_RE) ?? [])].filter((h) => !NONCE_RE.test(h));
  const resolvable = resolvableByRound.get(entry.round) ?? new Set();
  for (const h of hashes) {
    if (!resolvable.has(h)) {
      findings.push({ id: "XL-cited-commit-missing", kind: "cited-commit-missing", hash: h });
    }
  }
  if (hashes.length === 0 && VERDICT_RE.test(body)) {
    findings.push({ id: "XL-verdict-without-revision", kind: "verdict-without-revision" });
  }
  return { report: rel, round: entry.round, verdict: findings.length === 0 ? 0 : 1, findings };
}

function readBody(p) {
  try {
    return fs.readFileSync(p, "utf8");
  } catch {
    return null;
  }
}

function scanAll(root) {
  const repos = reposToCheck(root);
  const files = reportFiles(root);
  const allHashes = [
    ...new Set(files.flatMap((f) => (readBody(f.path) ?? "").match(HASH_RE) ?? [])),
  ].filter((h) => !NONCE_RE.test(h));
  const resolvable = resolvableHashes(repos, allHashes);
  const resolvableByRound = new Map();
  for (const round of roundNumbers(root)) resolvableByRound.set(round, resolvable);
  const byRound = new Map();
  for (const entry of files) {
    if (!byRound.has(entry.round)) byRound.set(entry.round, []);
    byRound.get(entry.round).push(scanReport(root, resolvableByRound, entry));
  }
  const reports = reportFiles(root).map((e) => ({ round: e.round }));
  const rounds = roundNumbers(root).map((round) => {
    const rs = byRound.get(round) ?? [];
    if (rs.length === 0) {
      return { round, verdict: 0, note: "round dir has no reports (skipped)", reports: [] };
    }
    const unreadable = rs.some((r) => r.verdict === 2);
    const failed = rs.some((r) => r.verdict === 1);
    return { round, verdict: unreadable ? 2 : failed ? 1 : 0, reports: rs };
  });
  const anyReports = rounds.some((r) => r.reports.length > 0);
  const verdict = !anyReports ? 2 : rounds.some((r) => r.verdict === 1) ? 1 : 0;
  return { gate: GATE_ID, verdict, rounds, repos: repos.map((r) => r.label) };
}

function printFinding(rep, f) {
  console.log(
    `# finding ${f.id} ${f.kind} report=${rep.report}${f.hash ? " hash=" + f.hash : ""}${f.bytes !== undefined ? " bytes=" + f.bytes : ""}`
  );
}

function runSelftest() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "cross-lane-gate-"));
  try {
    const repo = path.join(tmp, "fixture-shokunin");
    fs.mkdirSync(repo, { recursive: true });
    const git = (args) => execFileSync("git", ["-C", repo, ...args], { stdio: "ignore" });
    git(["init", "-q"]);
    git(["config", "user.email", "fixture@example.invalid"]);
    git(["config", "user.name", "fixture"]);
    fs.writeFileSync(path.join(repo, "f.txt"), "fixture\n");
    git(["add", "f.txt"]);
    git(["commit", "-qm", "fixture"]);
    const realHash = execFileSync("git", ["-C", repo, "rev-parse", "--short=10", "HEAD"]).toString().trim();
    const bogusHash = "0123456789abcdef0123456789abcdef01234567";
    const reportFixture = (round, lane, body) => {
      const dir = path.join(tmp, ".ufo", "reports", `round-${round}`);
      fs.mkdirSync(dir, { recursive: true });
      const p = path.join(dir, `${lane}.md`);
      fs.writeFileSync(p, body);
      return p;
    };
    const long = "evidence: lane seat file with exact commands and outputs.\n";
    reportFixture(11, "canonical", "# lane round 11 report\n\n## SHONEN\n- [x] verifier: checked\n\nWork landed in commit " + realHash + ".\n\n" + long.repeat(40));
    reportFixture(12, "marker", "# lane round 12 closeout (marker)\n\nshort marker body\n");
    reportFixture(13, "missing-commit", "# lane round 13 report\n\n## SHONEN\n\nverdict: ADMIT-corr at " + bogusHash + ".\n\n" + long.repeat(40));
    reportFixture(14, "no-revision", "# lane round 14 report\n\n## SHONEN\n\nverdict: ADMIT-corr, report clean.\n\n" + long.repeat(40));
    const unreadable = reportFixture(15, "unreadable", "");
    fs.chmodSync(unreadable, 0o000);
    reportFixture(16, "empty-round", "");
    fs.rmSync(path.join(tmp, ".ufo", "reports", "round-16", "empty-round.md"));

    const all = scanAll(tmp);
    const expect = [
      { case: "canonical", round: 11, exit: 0, kinds: [] },
      { case: "marker", round: 12, exit: 1, kinds: ["marker-overwrite"] },
      { case: "missing-commit", round: 13, exit: 1, kinds: ["cited-commit-missing"] },
      { case: "no-revision", round: 14, exit: 1, kinds: ["verdict-without-revision"] },
      { case: "unreadable", round: 15, exit: 2, kinds: [] },
      { case: "empty-round", round: 16, exit: 0, kinds: [] },
    ];
    let pass = 0;
    for (const want of expect) {
      const r = all.rounds.find((x) => x.round === want.round) ?? { reports: [], verdict: 2 };
      const kinds = [...new Set(r.reports.flatMap((x) => x.findings.map((f) => f.kind)))].sort();
      const ok = r.verdict === want.exit && JSON.stringify(kinds) === JSON.stringify(want.kinds);
      if (ok) pass++;
      console.log(
        `# selftest ${want.case} expect_exit=${want.exit} got_exit=${r.verdict} kinds=${kinds.join(",") || "none"} ${ok ? "PASS" : "FAIL"}`
      );
    }
    console.log(
      `# selftest tally ${pass}/${expect.length} ${pass === expect.length ? "PASS" : "FAIL"} (fixtures under os.tmpdir(), live tree untouched)`
    );
    return pass === expect.length ? 0 : 1;
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

function main() {
  const args = process.argv.slice(2);
  const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../../..");

  if (args.includes("--selftest")) {
    process.exit(runSelftest());
  }

  const all = scanAll(root);

  if (args[0] === "--report" && args[1]) {
    const target = path.resolve(args[1]);
    const entry = { round: Number(/round-(\d+)/.exec(target)?.[1] ?? 0), path: target };
    const repos = reposToCheck(root);
    const hashes = [...new Set(fs.readFileSync(target, "utf8").match(HASH_RE) ?? [])].filter((h) => !NONCE_RE.test(h));
    const resolvable = resolvableHashes(repos, hashes);
    const byRound = new Map([[entry.round, resolvable]]);
    const r = scanReport(root, byRound, entry);
    for (const f of r.findings) printFinding(r, f);
    console.log(`# report ${r.report} ${r.verdict === 1 ? "failed" : "clean"} findings=${r.findings.length}`);
    process.exit(r.verdict);
  }

  for (const r of all.rounds) {
    if (args[0] === "--round" && Number(args[1]) !== r.round) continue;
    for (const rep of r.reports) {
      for (const f of rep.findings) printFinding(rep, f);
      console.log(`# report ${rep.report} ${rep.verdict === 1 ? "failed" : "clean"} findings=${rep.findings.length}`);
    }
    if (r.reports.length > 0) {
      const failed = r.reports.filter((x) => x.findings.length > 0).length;
      console.log(`# round ${r.round} ${r.verdict === 1 ? "failed" : "clean"} reports=${r.reports.length} failed=${failed}`);
    } else {
      console.log(`# round ${r.round} could-not-evaluate note=${r.note}`);
    }
  }

  console.log(`# repos ${all.repos.join(" ")}`);
  console.log(
    `# summary ${GATE_ID} rounds=${all.rounds.length} failed_rounds=${all.rounds.filter((r) => r.verdict === 1).length} exit=${all.verdict}`
  );
  process.exit(all.verdict);
}

main();