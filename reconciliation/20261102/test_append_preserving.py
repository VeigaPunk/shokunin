"""Isolated operator JSON integrity tests; no lane counters and no real ledger writes."""
import importlib.util
import hashlib
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('append_preserving', Path(__file__).with_name('append-preserving.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
E = {'type': 'closure', 'campaign': 'hyaku', 'lane': 'test', 'lane_round': 2}


class IntegrityTests(unittest.TestCase):
    def check_case(self, raw):
        before = m.parse(raw)
        out, n, cut = m.prepare(raw, E)
        self.assertEqual(out[:cut], raw[:cut])
        self.assertTrue(out.endswith(raw[cut:]))
        self.assertEqual(m.parse(out), dict(before, rounds=before['rounds'] + [E]))
        self.assertEqual(n, len(before['rounds']))
        return out

    def test_empty(self):
        self.check_case(b'{"rounds":[]}')

    def test_empty_whitespace(self):
        self.check_case(b'{ "rounds" : [\r\n\t ], "tail" : 4 }\n')

    def test_nonempty(self):
        self.check_case(b'{"rounds":[{"round":1,"note":"immutable"}]}\n')

    def test_mixed_unicode_delimiter_text(self):
        self.check_case('{\n "roster":["日本"],"rounds" : [\n {"note":"fake ] } rounds", "nested":{"rounds":[]}}\n  , {"value":2} \r\n], "after":[3]}\n'.encode())

    def test_duplicate_closure(self):
        out = self.check_case(b'{"rounds":[]}')
        with self.assertRaisesRegex(ValueError, 'duplicate_closure'):
            m.prepare(out, E)

    def test_duplicate_cross_campaign(self):
        with self.assertRaisesRegex(ValueError, 'duplicate_closure'):
            m.prepare(b'{"rounds":[{"type":"closure","campaign":"old","lane":"test","round":2}]}', E)

    def test_bad_suffix_json(self):
        for raw in [b'{"rounds":[]}}', b'{"rounds":[]}garbage', b'{"rounds":[]', b'{"rounds":[,]}', b'{"rounds":[]}\x00']:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                m.prepare(raw, E)

    def test_duplicate_keys(self):
        for raw in [b'{"rounds":[],"rounds":[]}', b'{"rounds":[{"x":1,"x":2}]}']:
            with self.assertRaisesRegex(ValueError, 'duplicate_json_key'):
                m.prepare(raw, E)

    def test_nonfinite(self):
        with self.assertRaisesRegex(ValueError, 'nonfinite_json_number'):
            m.prepare(b'{"rounds":[],"x":NaN}', E)

    def test_expected_sha(self):
        raw = b'{"rounds":[]}'
        digest = hashlib.sha256(raw).hexdigest()
        self.assertEqual(m.check_expected(raw, digest), digest)
        for changed, expected in [(raw, '0' * 64), (raw + b' ', digest)]:
            with self.assertRaisesRegex(ValueError, 'concurrent_manifest_change'):
                m.check_expected(changed, expected)

    def test_bad_shape(self):
        for raw in [b'[]', b'{}', b'{"rounds":{}}', b'{"rounds":[null]}']:
            with self.assertRaises(ValueError):
                m.prepare(raw, E)

    def test_live_manifest_readonly(self):
        root = Path(__file__).resolve().parents[2]
        raw = (root / 'MANIFEST.json').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), 'ace00714be7fd19dcfe02ad565bc21bea62edafa29209c56a3ee2f3387e16584')
        self.check_case(raw)
        self.assertEqual((root / 'MANIFEST.json').read_bytes(), raw)


if __name__ == '__main__':
    unittest.main(verbosity=2)
