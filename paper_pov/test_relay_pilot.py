import unittest
import datetime as dt
from paper_pov.relay_pilot import action, next_slot, valid_result, next_handoff, MAX_HOPS, UTC

class TestRelay(unittest.TestCase):
    def test_slots(self):
        t = dt.datetime(2026, 11, 15, 10, 25, tzinfo=UTC)
        self.assertEqual(next_slot(t).minute, 29)
        self.assertEqual(next_slot(t.replace(minute=59)).hour, 11)
        self.assertEqual(next_slot(t.replace(minute=54)).minute, 59)
    def test_handoff_bounds(self):
        t = dt.datetime(2026, 11, 15, 10, 25, tzinfo=UTC)
        end = t + dt.timedelta(hours=1)
        self.assertEqual(next_handoff(2, t, end).minute, 29)
        self.assertIsNone(next_handoff(MAX_HOPS, t, end))
        self.assertIsNone(next_handoff(2, t, t + dt.timedelta(minutes=3)))

    def test_gate(self):
        t = dt.datetime(2026, 11, 15, 10, 25, tzinfo=UTC)
        d = dict(run_id="1", source_sha="a", status="SUCCESS_PAPER_ONLY",
                 remote_readback_verified=True, production_applied=False,
                 buy_approved=False, as_of=t.isoformat(), max_client_quote_age_seconds=1)
        self.assertTrue(valid_result(d, 1, "a", t))
        self.assertEqual(action([{"status":"queued"}], d, "a", t), "ACTIVE")
        self.assertEqual(action([], d, "a", t), "FRESH")
        self.assertEqual(action([], d, "b", t), "DISPATCH")
        self.assertEqual(action([], d, "a", t+dt.timedelta(seconds=239)), "FRESH")
        self.assertEqual(action([], d, "a", t+dt.timedelta(seconds=240)), "DISPATCH")
        self.assertEqual(action([], d, "a", t+dt.timedelta(seconds=601)), "DISPATCH")
        self.assertFalse(valid_result(d, 2, "a", t))
        self.assertFalse(valid_result(dict(d, buy_approved=True), 1, "a", t))
        self.assertFalse(valid_result(dict(d, remote_readback_verified=False), 1, "a", t))
