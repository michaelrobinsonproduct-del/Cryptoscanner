"""Offline adversarial acceptance: no network, ledger mutation or score change."""
import base64
import copy
import datetime as dt
import hashlib
import json
import unittest

from paper_pov.test_learning_outcomes import fixture, START
from paper_pov.gap_recovery_audit import (
    REVISION, _source_url, _verify_page, audit, capture_bounded,
    verify_sources,
)

UTC = dt.timezone.utc
END = START + dt.timedelta(minutes=125)


def source(pair="AAAUSD", offsets=(20, 40, 60, 65), since=None):
    since = int(START.timestamp() * 1_000_000_000) - 1 if since is None else since
    trades = []
    for i, minute in enumerate(offsets):
        trades.append(["1.2", "10", str(int((START + dt.timedelta(minutes=minute)).timestamp())),
                       "b", "m", "", str(i + 1)])
    raw = json.dumps({"error": [], "result": {
        pair: trades, "last": str(int((START + dt.timedelta(minutes=max(offsets)+1)).timestamp() * 1_000_000_000))
    }}, separators=(",", ":")).encode()
    return {"pair": pair, "start_since_ns": since, "pages": [{
        "revision": REVISION, "request_url": _source_url(pair, since),
        "retrieved_at": END.isoformat(),
        "response_b64": base64.b64encode(raw).decode(),
        "response_sha256": hashlib.sha256(raw).hexdigest()}]}


def replace_payload(page, callback):
    data = json.loads(base64.b64decode(page["response_b64"]))
    callback(data)
    raw = json.dumps(data, separators=(",", ":")).encode()
    page["response_b64"] = base64.b64encode(raw).decode()
    page["response_sha256"] = hashlib.sha256(raw).hexdigest()


class GapRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.state = fixture([0, 120])
        self.original = copy.deepcopy(self.state)

    def test_real_trade_prints_recover_one_hour_without_modifying_ledger(self):
        report = audit(self.state, END, [source()])
        one = report["before"]["1"]
        after = report["after"]["1"]
        self.assertEqual(one["gap_abstentions"], 3)
        self.assertEqual(after["matured_recovered_trade_evidence"], 1)
        self.assertEqual(after["still_missing"], 2)
        self.assertEqual(after["eligible_after"], one["eligible_before"])
        self.assertEqual(report["recovered_total_correlated_windows"], 1)
        self.assertEqual(report["source_pages"][0]["pair"], "AAAUSD")
        self.assertEqual(report["retention"]["ledger_retention_hours"], 50)
        self.assertFalse(report["ledger_modified"])
        self.assertFalse(report["production_applied"])
        self.assertEqual(self.state, self.original)

    def test_no_sources_and_immature_remain_abstentions(self):
        report = audit(self.state, END)
        self.assertEqual(report["recovered_total_correlated_windows"], 0)
        self.assertEqual(report["before"]["1"]["gap_abstentions"],
                         report["after"]["1"]["still_missing"])
        self.assertEqual(report["before"]["6"]["immature"], 6)
        self.assertTrue(report["retention"]["archived_rows_not_evaluable_from_current_snapshot"])

    def test_gap_over_45m_cannot_be_relaxed(self):
        s = source(offsets=(20, 100, 110))
        report = audit(self.state, END, [s])
        self.assertEqual(report["after"]["1"]["matured_recovered_trade_evidence"], 0)

    def test_bad_hash_alias_and_cursor_abstain(self):
        s = source()
        s["pages"][0]["response_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "SHA256"):
            audit(self.state, END, [s])
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"].__setitem__("OTHERUSD", x["result"].pop("AAAUSD")))
        with self.assertRaisesRegex(ValueError, "identity"):
            audit(self.state, END, [s])
        s = source()
        s["pages"][0]["request_url"] = _source_url("BBBUSD", s["start_since_ns"])
        with self.assertRaisesRegex(ValueError, "identity"):
            audit(self.state, END, [s])

    def test_duplicate_id_timestamp_and_missing_id_rejected(self):
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][1].__setitem__(6, "1"))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            audit(self.state, END, [s])
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][1].__setitem__(
            2, x["result"]["AAAUSD"][0][2]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            audit(self.state, END, [s])
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][0].pop())
        with self.assertRaisesRegex(ValueError, "trade ID"):
            audit(self.state, END, [s])

    def test_no_future_source_and_no_source_lookahead(self):
        s = source()
        s["pages"][0]["retrieved_at"] = (END + dt.timedelta(minutes=1)).isoformat()
        with self.assertRaisesRegex(ValueError, "cutoff"):
            audit(self.state, END, [s])
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][0].__setitem__(
            2, str(int((END + dt.timedelta(minutes=1)).timestamp()))))
        with self.assertRaisesRegex(ValueError, "Nonmonotonic|Future"):
            audit(self.state, END, [s])

    def test_authentic_nanosecond_trade_timestamp_is_preserved_not_rounded(self):
        s = source()
        t = str(int((START + dt.timedelta(minutes=20)).timestamp())) + ".000000001"
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][0].__setitem__(2, t))
        report = audit(self.state, END, [s])
        self.assertEqual(report["recovered_total_correlated_windows"], 1)
        self.assertIn(".000000001+00:00", report["source_coverage"]["AAAUSD"]["first_trade_utc"])
        s = source()
        replace_payload(s["pages"][0], lambda x: x["result"]["AAAUSD"][0].__setitem__(
            2, str(int((START + dt.timedelta(minutes=20)).timestamp())) + ".0000000001"))
        with self.assertRaisesRegex(ValueError, "Subnanosecond"):
            audit(self.state, END, [s])

    def test_numeric_json_nanosecond_timestamp_does_not_float_round(self):
        s = source()
        page = s["pages"][0]
        raw = base64.b64decode(page["response_b64"])
        original = str(int((START + dt.timedelta(minutes=20)).timestamp()))
        raw = raw.replace(('"' + original + '"').encode(),
                          (original + '.000000001').encode(), 1)
        page["response_b64"] = base64.b64encode(raw).decode()
        page["response_sha256"] = hashlib.sha256(raw).hexdigest()
        report = audit(self.state, END, [s])
        self.assertIn(".000000001+00:00", report["source_coverage"]["AAAUSD"]["first_trade_utc"])

    def test_uncovered_trade_window_remains_missing(self):
        s = source(offsets=(20, 30))
        report = audit(self.state, END, [s])
        self.assertEqual(report["recovered_total_correlated_windows"], 0)

    def test_retention_inventory_is_not_fabricated_outcome(self):
        self.state["archived"] = {"scans": 2, "observations": 100}
        self.state["archive_index"] = [{"id": "archived", "as_of": START.isoformat()}]
        from paper_pov.ledger import seal
        seal(self.state)
        # A valid archived summary also changes generation, so verification
        # rejects arbitrary re-sealing instead of treating it as recovery.
        with self.assertRaisesRegex(ValueError, "generation"):
            audit(self.state, END)

    def test_mock_https_capture_preserves_exact_bytes_and_sha(self):
        s = source()
        raw = base64.b64decode(s["pages"][0]["response_b64"])
        class FakeResponse:
            def __init__(self, url):
                self.url = url
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def geturl(self):
                return self.url
            def read(self, n):
                return raw
        def opener(url, timeout):
            return FakeResponse(url)
        captures, errors = capture_bounded(self.state, END, max_pairs=1, max_pages=1, opener=opener)
        self.assertFalse(errors)
        self.assertEqual(len(captures), 1)
        self.assertEqual(captures[0]["pages"][0]["response_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(verify_sources(captures, dt.datetime.now(UTC))[1][0]["trade_count"], 4)


if __name__ == "__main__":
    unittest.main()
