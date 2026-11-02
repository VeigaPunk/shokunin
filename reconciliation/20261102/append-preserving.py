#!/usr/bin/env python3
"""Operator-only append of one validated closure without rewriting prior JSON bytes.
Original append-local.py and canonical validator remain unchanged. Dry-run default.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import runpy
import tempfile


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('duplicate_json_key')
        out[key] = value
    return out


def reject_constant(value):
    raise ValueError('nonfinite_json_number')


DECODER = json.JSONDecoder(object_pairs_hook=unique_object, parse_constant=reject_constant)


def parse(raw):
    return DECODER.decode(raw.decode('utf-8'))


def check_expected(raw, expected):
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected:
        raise ValueError('concurrent_manifest_change')
    return digest


def prepare(raw, entry):
    doc = parse(raw)
    if not isinstance(doc, dict) or not isinstance(doc.get('rounds'), list):
        raise ValueError('invalid_manifest_shape')
    old = doc['rounds']
    if not all(isinstance(row, dict) for row in old):
        raise ValueError('invalid_round_shape')
    if entry.get('type') == 'closure' and any(
        row.get('type') == 'closure' and row.get('lane') == entry.get('lane')
        and row.get('lane_round', row.get('round')) == entry.get('lane_round', entry.get('round'))
        for row in old
    ):
        raise ValueError('duplicate_closure')
    # Parse top-level values to locate rounds structurally, not by text/regex.
    text = raw.decode('utf-8')
    def skip(i):
        while i < len(text) and text[i] in ' \t\r\n':
            i += 1
        return i
    i = skip(0) + 1
    end_rounds = None
    while True:
        i = skip(i)
        if text[i] == '}':
            break
        key, i = DECODER.raw_decode(text, i)
        i = skip(i)
        if text[i] != ':':
            raise ValueError('invalid_object_separator')
        value_start = skip(i + 1)
        _, i = DECODER.raw_decode(text, value_start)
        if key == 'rounds':
            if text[value_start] != '[' or text[i - 1] != ']':
                raise ValueError('invalid_rounds_delimiter')
            end_rounds = i - 1
        i = skip(i)
        if text[i] == '}':
            break
        if text[i] != ',':
            raise ValueError('invalid_object_separator')
        i += 1
    if end_rounds is None:
        raise ValueError('rounds_missing')
    cut = len(text[:end_rounds].encode('utf-8'))
    prefix, suffix = raw[:cut], raw[cut:]
    encoded = json.dumps(entry, ensure_ascii=False, allow_nan=False, indent=1).encode('utf-8')
    out = prefix + (b',' if old else b'') + b'\n  ' + encoded + b'\n ' + suffix
    after = parse(out)
    expected = dict(doc, rounds=old + [entry])
    if after != expected or not out.startswith(prefix) or not out.endswith(suffix):
        raise ValueError('history_changed')
    return out, len(old), cut


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--entry', required=True)
    parser.add_argument('--expected-manifest-sha', required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    os.environ['SHOKUNIN_ROOT'] = str(root)
    entry = parse(Path(args.entry).read_bytes())
    validator = runpy.run_path(str(root / 'scripts/hyaku/append-closure.py'), run_name='closure_validation_only')
    validator['validate'](entry)
    # Same cooperative lock as original helper; covers hash check, prepare, replace/readback.
    with open(root / '.git/cloud-closure.lock', 'a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path = root / 'MANIFEST.json'
        raw = path.read_bytes()
        before = check_expected(raw, args.expected_manifest_sha)
        out, index, prefix_length = prepare(raw, entry)
        receipt = dict(index=index, lane=entry['lane'], round=entry['lane_round'],
                       before=before, after=hashlib.sha256(out).hexdigest(),
                       prior_entries_preserved=True, exact_prefix_bytes=prefix_length,
                       applied=args.apply)
        if args.apply:
            fd, tmp = tempfile.mkstemp(prefix='.manifest-cloud-', dir=root)
            try:
                os.fchmod(fd, path.stat().st_mode & 0o777)
                with os.fdopen(fd, 'wb') as stream:
                    stream.write(out)
                    stream.flush()
                    os.fsync(stream.fileno())
                # Also detect non-cooperating modifications before replacement.
                check_expected(path.read_bytes(), before)
                os.replace(tmp, path)
                if path.read_bytes() != out:
                    raise ValueError('written_manifest_readback_mismatch')
                receipt['readback_verified'] = True
            finally:
                if os.path.exists(tmp):
                    os.unlink(tmp)
        print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
