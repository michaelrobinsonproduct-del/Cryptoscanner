"""Adversarial, offline-only GitHub tag slot-claim protocol tests."""
import datetime as dt
import unittest

from paper_pov.slot_claim_protocol import prepare, attempt, OWNER_ID

S = dt.datetime(2026, 11, 2, 21, 0, tzinfo=dt.timezone.utc)
SOURCE = "e3fb5ec272d74a72f19e306c1825aae1b7960576"


def kwargs():
    return dict(slot=S, now=S + dt.timedelta(minutes=18),
                source_sha=SOURCE, main_sha=SOURCE, ledger_commit="a"*40,
                decision_sha256="b"*64, controller_run_id=41523180769,
                owner_comment_id=190001, owner_id=OWNER_ID)


class FakeGit:
    def __init__(self):
        self.refs = {}
        self.tags = {}
        self.next = 1
        self.fail = None
        self.tamper = None
        self.dispatch_calls = 0

    def get_ref(self, ref):
        if self.fail == "read":
            raise TimeoutError("GET timeout")
        if self.tamper == "ref" and ref in self.refs:
            return "f"*40
        return self.refs.get(ref)

    def create_tag(self, name, target, message):
        if self.fail == "tag":
            raise TimeoutError("tag timeout")
        sha = format(self.next, "040x")
        self.next += 1
        self.tags[sha] = dict(name=name, target_sha=target, message=message)
        return "bad" if self.fail == "bad_sha" else sha

    def create_ref(self, ref, sha):
        if ref in self.refs:
            raise ValueError("HTTP 422: ref exists")
        self.refs[ref] = sha
        if self.fail == "after_ref":
            raise TimeoutError("commit succeeded but response lost")

    def get_tag(self, sha):
        tag = self.tags.get(sha)
        if tag and self.tamper == "tag":
            return dict(tag, message="tampered")
        return tag


class SlotClaimTests(unittest.TestCase):
    def test_valid_dry_claim_is_bound_to_exact_utc_slot(self):
        c = prepare(**kwargs())
        self.assertEqual(c["ref"], "refs/tags/paper-recovery-slot-v1/20261102T2100Z")
        self.assertIn('"native_schedule":false', c["message"])
        self.assertEqual(len(c["digest"]), 64)

    def test_one_winner_two_controllers_same_slot(self):
        api = FakeGit()
        first = prepare(**kwargs())
        second_args = dict(kwargs(), controller_run_id=41523180770)
        second = prepare(**second_args)
        a, b = attempt(api, first), attempt(api, second)
        self.assertEqual(a["status"], "CLAIMED_NOT_DISPATCHED")
        self.assertEqual(b["reason"], "SLOT_REF_ALREADY_EXISTS")
        self.assertEqual(len(api.refs), 1)
        self.assertFalse(a["dispatch_executed"])
        self.assertEqual(api.dispatch_calls, 0)

    def test_source_drift_cannot_claim_same_slot(self):
        args = dict(kwargs(), main_sha="c"*40)
        with self.assertRaisesRegex(ValueError, "UNAUTHENTICATED_SOURCE"):
            prepare(**args)

    def test_changed_source_cannot_make_new_ref_for_same_slot(self):
        args = dict(kwargs(), source_sha="c"*40, main_sha="c"*40)
        self.assertEqual(prepare(**args)["ref"], prepare(**kwargs())["ref"])

    def test_wrong_owner_and_origin_fail(self):
        for key, value in (("owner_id", 12), ("origin", "schedule"),
                           ("controller_run_id", 0), ("owner_comment_id", True)):
            with self.subTest(key=key):
                args = dict(kwargs(), **{key: value})
                with self.assertRaises(ValueError):
                    prepare(**args)

    def test_bad_times_fail_closed(self):
        cases = [
            dict(slot=S.replace(minute=9)),
            dict(now=S-dt.timedelta(seconds=1)),
            dict(now=S+dt.timedelta(minutes=30)),
            dict(now=(S+dt.timedelta(minutes=1)).replace(tzinfo=None)),
            dict(slot=S.replace(tzinfo=None)),
        ]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    prepare(**dict(kwargs(), **case))

    def test_invalid_digests_and_ids_fail(self):
        for case in ({"decision_sha256": "b"*63},
                     {"ledger_commit": "a"*39},
                     {"source_sha": "z"*40}):
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    prepare(**dict(kwargs(), **case))

    def test_readback_ref_tamper_blocks(self):
        api = FakeGit()
        api.tamper = "ref"
        self.assertEqual(attempt(api, prepare(**kwargs()))["reason"],
                         "CLAIM_READBACK_MISMATCH")

    def test_readback_tag_tamper_blocks(self):
        api = FakeGit()
        api.tamper = "tag"
        self.assertEqual(attempt(api, prepare(**kwargs()))["reason"],
                         "CLAIM_READBACK_MISMATCH")

    def test_post_commit_timeout_does_not_retry(self):
        api = FakeGit()
        api.fail = "after_ref"
        claim = prepare(**kwargs())
        result = attempt(api, claim)
        self.assertEqual(result["reason"], "GITHUB_CLAIM_OUTCOME_UNCERTAIN_NO_RETRY")
        self.assertIn(claim["ref"], api.refs)
        self.assertEqual(attempt(api, claim)["reason"], "SLOT_REF_ALREADY_EXISTS")

    def test_precommit_timeout_blocks(self):
        api = FakeGit()
        api.fail = "tag"
        self.assertEqual(attempt(api, prepare(**kwargs()))["status"], "BLOCKED")
        self.assertEqual(api.refs, {})

    def test_bad_tag_sha_blocks(self):
        api = FakeGit()
        api.fail = "bad_sha"
        self.assertEqual(attempt(api, prepare(**kwargs()))["reason"],
                         "INVALID_TAG_SHA")

    def test_read_failure_blocks_without_dispatch(self):
        api = FakeGit()
        api.fail = "read"
        result = attempt(api, prepare(**kwargs()))
        self.assertEqual(result["status"], "BLOCKED")
        self.assertFalse(result["scanner_executed"])
        self.assertFalse(result["ledger_written"])

    def test_forged_plan_never_touches_git(self):
        original = prepare(**kwargs())
        mutations = [
            {"ref": "refs/tags/paper-recovery-slot-v1/20261102T2130Z"},
            {"tag_name": "wrong-tag"},
            {"target_sha": "c"*40},
            {"source_sha": "c"*40},
            {"digest": "0"*64},
            {"message": original["message"].replace("PAPER_RECOVERY_SLOT_CLAIM_V1",
                                                     "FAKE_CLAIM")},
            {"message": original["message"].replace('"owner_id":336805669',
                                                     '"owner_id":7')},
            {"message": original["message"].rstrip("\\n")},
        ]
        for change in mutations:
            with self.subTest(change=change):
                api = FakeGit()
                result = attempt(api, dict(original, **change))
                self.assertEqual(result["reason"], "INVALID_CLAIM")
                self.assertEqual(api.refs, {})
                self.assertEqual(api.tags, {})

    def test_malformed_claim_blocks(self):
        self.assertEqual(attempt(FakeGit(), {"ref": "refs/heads/main"})["reason"],
                         "INVALID_CLAIM")

    def test_claim_is_not_native_schedule_or_live_writer_proof(self):
        result = attempt(FakeGit(), prepare(**kwargs()))
        for field in ("dispatch_executed", "scanner_executed", "ledger_written",
                      "native_schedule_claimed", "global_writer_exclusivity_proven"):
            self.assertFalse(result[field])


if __name__ == "__main__":
    unittest.main()
