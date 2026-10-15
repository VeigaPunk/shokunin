#!/usr/bin/env node
// measure-corpus.mjs — census-executor actual-gate evidence collector, aggregator round 10 (resume wave).
//
// WHAT IT DOES (read-only, one-shot)
//   Derives the fleet root from this script's own path (it lives at
//   <fleet-root>/.ufo/waves/aggregator-r10-resume/measure-corpus.mjs), discovers the
//   PHYSICAL lane directories (nonrecursive, directories only, sorted), spawns the
//   CURRENT corpus gate
//     node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json
//   exactly once, and writes ONE JSON document of redacted metadata to stdout — the
//   only stream this script writes.  Raw gate lines, finding text, notes and corpus
//   content are never printed or persisted: metadata, finding IDs, rule names,
//   pathnames, digests and counts only.  Raw stdout/stderr are reduced to byte counts
//   plus sha256 fingerprints (identity without content).
//
// OWN SUCCESS vs GATE VERDICT (acceptance: never conflate)
//   gate_exit / gate_signal / gate_spawn_error describe the GATE process and are stored
//   as metadata exactly as observed (null stays null).  collector.ok, collector.status
//   and THIS script's exit code (0 = collector produced complete metadata, 1 = it did
//   not) describe the COLLECTOR only.  A gate exit 1 (findings) or 2 (could-not-
//   evaluate) with a complete, framing-consistent capture is collector.ok=true; a gate
//   exit 0 with a missing/ambiguous/inconsistent capture is collector.ok=false and
//   coverage_valid=false.  Per-lane exit=2 with findings=0 is labeled
//   could-not-evaluate, never clean.
//
// AUTHORITY and FRAMING (critic-adversarial design)
//   The trailing structured `# json` record is the ONLY lane authority.  The gate
//   interpolates corpus filenames into finding/`# note` lines without newline escaping,
//   so a crafted pathname could spoof an apparent `# summary ...` text line; JSON
//   payload strings are escaped, so a spoof could only ever forge an ADDITIONAL raw
//   `# json` marker — hence the marker count must be exactly one: 0 markers →
//   json-marker-missing, 2+ markers → json-marker-ambiguous; neither is ever treated as
//   coverage.  `# summary` lines serve solely as a framing cross-check: label SEQUENCE
//   (order AND duplicates) plus rev/dirty/exit/findings/rules fields must agree with the
//   `# json` lanes before coverage_valid=true.
//
// WHAT IT DELIBERATELY DOES NOT DO
//   No --repos/--gate override: default discovery must not be filtered, and the
//   operator custody boundary (audio, game-dev-2d, game-dev-3d are Devin-owned and
//   outside the configured fleet while remaining PHYSICAL lane members) means expected
//   is the physical-direct-children set ONLY — never equated with the configured fleet,
//   whose live config (shokunin.conf) is not sourced (wave contract).  No --selftest,
//   no rerun of historical gates, no second hardcoded lane list here: the lane set comes
//   from filesystem discovery and from the gate's own selection.  Runs no checks
//   mid-flight itself; the single gate spawn is executed by the parent after integration.

import { spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SELF_DIR = path.dirname(fileURLToPath(import.meta.url));
const FLEET_ROOT = path.resolve(SELF_DIR, '..', '..', '..');
const GATE_REL = '.ufo/waves/round-9/corpus-gate.mjs';
const GATE_ABS = path.join(FLEET_ROOT, '.ufo', 'waves', 'round-9', 'corpus-gate.mjs');
const ROUND = 10;
const GATE_ARGS = ['--all', '--round', String(ROUND), '--json'];
const COMMAND = 'node ' + GATE_REL + ' --all --round ' + String(ROUND) + ' --json';

const LANE_RE = /^[a-z0-9][a-z0-9-]*-shokunin$/;
const JSON_MARKER = '# json ';
const SUMMARY_RE = /^# summary (\S+) rev=(\S+) dirty=(-?\d+) exit=(\d) findings=(\d+) rules=(\S+)$/;
const GATE_VERSION_RE = /^# (corpus-gate-v\d+)/;
const EXIT_CLASS = { 0: 'clean', 1: 'failed', 2: 'could-not-evaluate', 3: 'failed' };
const GATE_TIMEOUT_MS = 600000;
const MAX_CAPTURE_BYTES = 268435456;
const GIT_TIMEOUT_MS = 60000;

function sha256Hex(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex');
}

function bufInfo(buf) {
  return Buffer.isBuffer(buf) ? { bytes: buf.length, sha256: sha256Hex(buf) } : { bytes: null, sha256: null };
}

function errorToken(err) {
  if (err && err.code) return String(err.code);
  if (err && err.message) return String(err.message).slice(0, 120);
  return 'unknown-error';
}

function blankReport() {
  return {
    schema: 'measure-corpus-v1',
    role: 'census-executor actual-gate evidence collector (R10Census, aggregator-r10-resume)',
    command: COMMAND,
    fleet_root: FLEET_ROOT,
    round: ROUND,
    measurement_mode: 'live worktree; per-lane revision/dirty come from the gate runLive stamps, not atomic snapshots; not a frozen corpus verdict',
    collector: {
      name: 'measure-corpus-v1',
      node_version: process.version,
      ok: false,
      status: 'pre-run',
      errors: [],
      exit_meaning: 'this process exits 0 iff collector.ok; gate verdict is data in gate_exit, never this code',
    },
    coverage_valid: false,
    measured_main_commit: null,
    measured_commit: null,
    measured_main_commit_error: null,
    gate: {
      relpath: GATE_REL,
      version: null,
      readable: false,
      bytes: null,
      sha256_worktree: null,
      sha256_head_blob: null,
      head_blob_bytes: null,
      head_blob_error: null,
      worktree_matches_head: null,
    },
    gate_sha256: null,
    measured_gate_source: null,
    gate_exit: null,
    exit: null,
    gate_exit_class: 'unknown',
    gate_signal: null,
    gate_spawn_error: null,
    gate_stdout: { bytes: null, sha256: null },
    gate_stderr: { bytes: null, sha256: null },
    json_markers: { count: 0, parse_error: null },
    denominators: {
      physical_child_directories: 0,
      configured_fleet: null,
      configured_fleet_note: 'shokunin.conf deliberately not sourced (wave contract: do not source live configuration); physical set and configured fleet are distinct denominators and must never be equated',
    },
    boundaries: [
      'expected = physical direct child directories matching /^[a-z0-9][a-z0-9-]*-shokunin$/; custody boundary: audio, game-dev-2d, game-dev-3d are Devin-owned and outside the configured fleet yet remain physical members selected by --all; the collector does not filter selection',
      'text-line framing is untrusted: corpus filenames with newlines could spoof `# summary` lines, so the structured `# json` record is authoritative and exact summary-sequence agreement is required before any coverage claim',
      'per-lane exit=2 with findings=0 is could-not-evaluate, not clean; clean_lanes counts exit=0 only',
      'gate bytes measured from the worktree; the HEAD blob digest is recorded separately so an edited uncommitted gate is distinguishable from the committed gate',
      'live worktree measurement is not atomic; revisions/dirty counts describe each lane at its own stamp moment',
    ],
    expected: [],
    direct_child_lanes: [],
    represented: [],
    omitted: [],
    extra: [],
    duplicates: [],
    order: { represented_is_sorted: false, matches_expected_order: false, gate_order: [], summary_order: [] },
    clean_lanes: 0,
    exit_class_counts: {},
    summary_lines: { count: 0, malformed_lines: 0, order: [], duplicates: [], sequence_agrees_with_json: false, field_mismatches: [] },
    results: [],
  };
}

function laneFromEntry(entry, idx, errs) {
  if (!entry || typeof entry !== 'object' || Array.isArray(entry)) {
    errs.push(`json-entry-${idx}: not-an-object`);
    return null;
  }
  const name = typeof entry.repo === 'string' ? entry.repo : null;
  if (name === null) errs.push(`json-entry-${idx}: repo-not-string`);
  const findings = Array.isArray(entry.findings) ? entry.findings : null;
  if (findings === null) errs.push(`json-entry-${idx}: findings-not-array`);
  const ids = findings === null ? [] : findings.map((f, j) => (f && typeof f.id === 'string' ? f.id : `json-entry-${idx}-finding-${j}-id-missing`));
  const stats = entry.stats && typeof entry.stats === 'object' ? entry.stats : null;
  if (stats === null) errs.push(`json-entry-${idx}: stats-missing`);
  const rulesIn = stats && stats.rules && typeof stats.rules === 'object' ? stats.rules : null;
  if (rulesIn === null) errs.push(`json-entry-${idx}: stats-rules-missing`);
  const counts_by_rule = {};
  if (rulesIn !== null) {
    for (const key of Object.keys(rulesIn)) if (Number.isFinite(rulesIn[key])) counts_by_rule[key] = rulesIn[key];
  }
  const file_count = stats && Number.isFinite(stats.files) ? stats.files : null;
  if (file_count === null) errs.push(`json-entry-${idx}: stats-files-missing`);
  const exit = Number.isInteger(entry.exit) ? entry.exit : null;
  if (exit === null) errs.push(`json-entry-${idx}: exit-not-integer`);
  const revision = typeof entry.revision === 'string' ? entry.revision : null;
  if (revision === null) errs.push(`json-entry-${idx}: revision-not-string`);
  const dirty = Number.isInteger(entry.dirty) ? entry.dirty : null;
  if (dirty === null) errs.push(`json-entry-${idx}: dirty-not-integer`);
  return {
    name,
    name_matches_lane_pattern: name !== null && LANE_RE.test(name),
    in_expected: false,
    revision,
    dirty,
    mode: typeof entry.mode === 'string' ? entry.mode : null,
    exit,
    exit_class: exit === null ? 'unknown' : (EXIT_CLASS[exit] || 'unknown'),
    clean: exit === 0,
    finding_ids: ids,
    finding_count: ids.length,
    counts_by_rule,
    counts_by_rule_total: Object.values(counts_by_rule).reduce((a, b) => a + b, 0),
    file_count,
    notes_count: Array.isArray(entry.notes) ? entry.notes.length : null,
    rules_failed_sorted: Object.keys(counts_by_rule).filter((k) => counts_by_rule[k] > 0).sort(),
  };
}

function main() {
  const report = blankReport();
  const errs = report.collector.errors;
  let status = 'ok';
  const fail = (token) => { if (status === 'ok') status = token; };

  const argv = process.argv.slice(2);
  if (argv.length > 0) {
    fail('bad-args');
    errs.push(`unexpected-arguments=${argv.length}`);
  }

  // ---- discovery: PHYSICAL direct children only (never the configured fleet)
  let expected = [];
  let discoverySkipped = status !== 'ok';
  if (!discoverySkipped) {
    try {
      if (!fs.statSync(FLEET_ROOT).isDirectory()) throw new Error('fleet-root-not-a-directory');
      const entries = fs.readdirSync(FLEET_ROOT, { withFileTypes: true });
      expected = entries.filter((e) => e.isDirectory() && LANE_RE.test(e.name)).map((e) => e.name).sort();
    } catch (err) {
      fail('discovery-failed');
      errs.push(`discovery:${errorToken(err)}`);
    }
  } else {
    errs.push('discovery:skipped');
  }
  report.expected = expected;
  report.direct_child_lanes = expected;
  report.denominators.physical_child_directories = expected.length;

  // ---- provenance: measured main commit + gate digests (worktree vs HEAD blob)
  let spawnGate = !discoverySkipped || status !== 'bad-args';
  let worktreeInfo = null;
  if (spawnGate) {
    const head = spawnSync('git', ['-C', FLEET_ROOT, 'rev-parse', 'HEAD'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], timeout: GIT_TIMEOUT_MS });
    if (head.error) report.measured_main_commit_error = `spawn:${errorToken(head.error)}`;
    else if (head.status !== 0) report.measured_main_commit_error = `exit:${head.status}`;
    else {
      const commit = String(head.stdout || '').trim();
      report.measured_main_commit = commit.length === 40 ? commit : null;
      if (commit.length !== 40) report.measured_main_commit_error = 'unexpected-shape';
    }
    report.measured_commit = report.measured_main_commit;

    const blob = spawnSync('git', ['-C', FLEET_ROOT, 'show', 'HEAD:' + GATE_REL], { encoding: 'buffer', stdio: ['ignore', 'pipe', 'pipe'], timeout: GIT_TIMEOUT_MS, maxBuffer: 1 << 26 });
    if (blob.error) report.gate.head_blob_error = `spawn:${errorToken(blob.error)}`;
    else if (blob.status !== 0) report.gate.head_blob_error = `exit:${blob.status}`;
    else if (Buffer.isBuffer(blob.stdout)) {
      report.gate.sha256_head_blob = sha256Hex(blob.stdout);
      report.gate.head_blob_bytes = blob.stdout.length;
    } else report.gate.head_blob_error = 'no-output-buffer';

    try {
      const raw = fs.readFileSync(GATE_ABS);
      worktreeInfo = bufInfo(raw);
      report.gate.readable = true;
      report.gate.bytes = raw.length;
      report.gate.sha256_worktree = raw.length === 0 ? null : sha256Hex(raw);
      report.gate_sha256 = report.gate.sha256_worktree;
    } catch (err) {
      fail('gate-file-missing');
      errs.push(`gate-read:${errorToken(err)}`);
    }
    if (report.gate.sha256_worktree !== null && report.gate.sha256_head_blob !== null) {
      report.gate.worktree_matches_head = report.gate.sha256_worktree === report.gate.sha256_head_blob;
    }
    report.measured_gate_source = report.measured_main_commit
      ? `${report.measured_commit}:${GATE_REL} (head blob) + worktree bytes sha256=${report.gate.sha256_worktree || 'unreadable'}`
      : `worktree-only; HEAD commit unavailable (${report.measured_main_commit_error || 'unknown'})`;
  }

  // ---- spawn the CURRENT gate exactly once (unless the gate file itself is absent)
  const gateSpawnable = spawnGate && report.gate.readable && status !== 'bad-args';
  if (!gateSpawnable && status === 'ok') fail('gate-file-missing');
  if (gateSpawnable) {
    const r = spawnSync(process.execPath, [GATE_ABS, ...GATE_ARGS], { cwd: FLEET_ROOT, stdio: ['ignore', 'pipe', 'pipe'], maxBuffer: MAX_CAPTURE_BYTES, timeout: GATE_TIMEOUT_MS });
    report.gate_stdout = bufInfo(r.stdout);
    report.gate_stderr = bufInfo(r.stderr);
    report.gate_signal = typeof r.signal === 'string' ? r.signal : null;
    report.gate_exit = Number.isInteger(r.status) ? r.status : null;
    report.exit = report.gate_exit;
    if (r.error) {
      report.gate_spawn_error = errorToken(r.error);
      fail(r.error.code === 'ETIMEDOUT' ? 'gate-timeout' : 'gate-spawn-or-capture-error');
    } else if (r.status === null) {
      fail(report.gate_signal === null ? 'gate-status-unknown' : 'gate-signaled');
    }
    report.gate_exit_class = report.gate_exit === null ? 'unknown' : (EXIT_CLASS[report.gate_exit] || 'unknown');

    // ---- framing parse: markers, summaries, version — raw lines kept in locals only
    if (Buffer.isBuffer(r.stdout)) {
      const text = r.stdout.toString('utf8');
      const lines = text.split('\n');
      let markerCount = 0;
      let payload = null;
      let payloadError = null;
      const summaries = [];
      let malformed = 0;
      for (const line of lines) {
        if (line.startsWith(JSON_MARKER)) {
          markerCount++;
          if (payload === null && payloadError === null) {
            try { payload = JSON.parse(line.slice(JSON_MARKER.length)); } catch (err) { payloadError = String(err && err.name || 'parse-error'); }
          }
        } else if (line.startsWith('# summary ')) {
          const m = SUMMARY_RE.exec(line);
          if (m) summaries.push({ name: m[1], rev: m[2], dirty: Number(m[3]), exit: Number(m[4]), findings: Number(m[5]), rules: m[6] === 'none' ? [] : m[6].split(',') });
          else malformed++;
        } else if (report.gate.version === null) {
          const v = GATE_VERSION_RE.exec(line);
          if (v) report.gate.version = v[1];
        }
      }
      report.json_markers = { count: markerCount, parse_error: payloadError };
      report.summary_lines.count = summaries.length;
      report.summary_lines.malformed_lines = malformed;
      report.summary_lines.order = summaries.map((s) => s.name);

      if (status === 'ok' || status === 'discovery-failed') {
        if (markerCount === 0) fail('json-marker-missing');
        else if (markerCount > 1) { fail('json-marker-ambiguous'); errs.push(`json-marker-count=${markerCount}`); }
        else if (payloadError !== null) fail('json-unparsable');
        else if (!Array.isArray(payload)) fail('json-shape-invalid');
        else {
          const lanes = [];
          for (let i = 0; i < payload.length; i++) {
            const lane = laneFromEntry(payload[i], i, errs);
            if (lane) lanes.push(lane);
          }
          if (lanes.length !== payload.length) errs.push(`lanes-dropped=${payload.length - lanes.length}`);
          report.results = lanes;
        }
      }

      // ---- summaries are cross-check ONLY: exact sequence (order + duplicates) and
      // per-lane field agreement required before any coverage claim.
      const laneNameOrder = report.results.map((l) => l.name);
      const sequenceAgrees = report.summary_lines.order.length === laneNameOrder.length
        && report.summary_lines.order.every((n, i) => n === laneNameOrder[i]);
      report.summary_lines.sequence_agrees_with_json = sequenceAgrees;
      if (sequenceAgrees) {
        const sumCounts = new Map();
        for (const n of report.summary_lines.order) sumCounts.set(n, (sumCounts.get(n) || 0) + 1);
        for (let i = 0; i < report.results.length; i++) {
          const lane = report.results[i];
          const s = summaries[i];
          if (s.dirty !== lane.dirty) report.summary_lines.field_mismatches.push({ index: i, name: s.name, field: 'dirty', from_summary: s.dirty, from_json: lane.dirty });
          if (s.exit !== lane.exit) report.summary_lines.field_mismatches.push({ index: i, name: s.name, field: 'exit', from_summary: s.exit, from_json: lane.exit });
          if (s.findings !== lane.finding_count) report.summary_lines.field_mismatches.push({ index: i, name: s.name, field: 'findings', from_summary: s.findings, from_json: lane.finding_count });
          const revAgrees = lane.revision !== null && (s.rev === lane.revision || s.rev === lane.revision.slice(0, 7));
          if (!revAgrees) report.summary_lines.field_mismatches.push({ index: i, name: s.name, field: 'rev', from_summary: s.rev, from_json: lane.revision });
          const sumRules = [...s.rules].sort().join(',');
          if (sumRules !== lane.rules_failed_sorted.join(',')) report.summary_lines.field_mismatches.push({ index: i, name: s.name, field: 'rules', from_summary: sumRules || 'none', from_json: lane.rules_failed_sorted.join(',') || 'none' });
        }
        report.summary_lines.duplicates = [...sumCounts.entries()].filter((c) => c[1] > 1).map(([name, count]) => ({ name, count })).sort((a, b) => (a.name < b.name ? -1 : 1));
        if (report.summary_lines.field_mismatches.length > 0) fail('summary-framing-mismatch');
      } else if (report.results.length > 0 || summaries.length > 0) {
        report.summary_lines.field_mismatches.push({ field: 'sequence', from_summary: report.summary_lines.order.length, from_json: laneNameOrder.length });
        if (payload !== null && Array.isArray(payload)) fail('summary-framing-mismatch');
      }
    } else if (status === 'ok' || status === 'discovery-failed') {
      fail('gate-capture-missing');
    }
  }

  // ---- membership against the PHYSICAL expected set (order + duplicates preserved)
  const expSet = new Set(report.expected);
  report.represented = report.results.map((l) => l.name).filter((n) => typeof n === 'string');
  for (const lane of report.results) lane.in_expected = typeof lane.name === 'string' && expSet.has(lane.name);
  const repSet = new Set(report.represented);
  report.omitted = report.expected.filter((n) => !repSet.has(n));
  report.extra = report.represented.filter((n) => !expSet.has(n));
  const laneCounts = new Map();
  for (const n of report.represented) laneCounts.set(n, (laneCounts.get(n) || 0) + 1);
  report.duplicates = [...laneCounts.entries()].filter((c) => c[1] > 1).map(([name, count]) => ({ name, count })).sort((a, b) => (a.name < b.name ? -1 : 1));
  const sortedRep = [...report.represented].sort();
  report.order = {
    represented_is_sorted: report.represented.length === sortedRep.length && report.represented.every((n, i) => n === sortedRep[i]),
    matches_expected_order: report.represented.length === report.expected.length && report.represented.every((n, i) => n === report.expected[i]),
    gate_order: report.represented,
    summary_order: report.summary_lines.order,
  };
  report.clean_lanes = report.results.filter((l) => l.clean).length;
  for (const lane of report.results) report.exit_class_counts[lane.exit_class] = (report.exit_class_counts[lane.exit_class] || 0) + 1;

  // ---- empty discovery is NEVER coverage success (even with a clean gate exit 0)
  if (status === 'ok' && report.expected.length === 0) {
    fail('discovery-empty');
    errs.push('expected-set-empty: zero physical lanes is a coverage failure, not a clean census');
  }

  report.collector.status = status;
  report.collector.ok = status === 'ok';
  report.coverage_valid = status === 'ok';

  process.stdout.write(JSON.stringify(report, null, 2) + '\n');
  process.exitCode = report.collector.ok ? 0 : 1;
}

try {
  main();
} catch (err) {
  try {
    const dead = blankReport();
    dead.collector.status = 'collector-exception';
    dead.collector.errors = [errorToken(err)];
    process.stdout.write(JSON.stringify(dead, null, 2) + '\n');
    process.exitCode = 1;
  } catch (inner) {
    process.exitCode = 1;
  }
}
