import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.learning_retention import build_seed,load_seed,pack_state,restore_state,write_gzip,file_sha
from paper_pov.shadow_learning_evidence import canonical_digest

class LearningRetentionTests(unittest.TestCase):
    def test_partition_roundtrip_preserves_order_and_rejects_tamper(self):
        state={"schema":"market_wide_continuity_v1","production_applied":False,
               "anchors":[{"prediction_id":"b","entry_utc":"2026-02-01T00:00:00Z"},
                          {"prediction_id":"a","entry_utc":"2026-01-01T00:00:00Z"}],
               "outcomes":[],"shadow_predictions":[],"shadow_outcomes":[]}
        state["digest"]=canonical_digest(state)
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp)
            manifest=pack_state(state,directory)
            self.assertEqual(restore_state(directory),state)
            p=directory/manifest["partitions"][0]["name"]
            p.write_bytes(p.read_bytes()+b"x")
            with self.assertRaisesRegex(ValueError,"checksum"):
                restore_state(directory)

    def test_compact_seed_exact_rows_and_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            sha="a"*64
            a={"prediction_id":"a","entry_utc":"2026-01-01T00:00:00Z","feature_complete":True,"source_sha256":sha}
            b=dict(a,prediction_id="b",feature_complete=False)
            o={"prediction_id":"a","horizon_hours":48,"coverage_complete":True,"hit":True,
               "label_mature_utc":"2026-01-03T00:00:00Z","source_sha256":sha}
            c=dict(source_archive_sha256=sha,source_authenticated=False,production_applied=False,
                   anchors=[a,b],outcomes=[o,dict(o,horizon_hours=1),dict(o,prediction_id="b")])
            path=root/"original.jsonl.gz"
            write_gzip(path,[c])
            expected=file_sha(path)
            m=build_seed([("archive",path,sha,expected)],root/"seed")
            loaded=load_seed(root/"seed",[("archive",sha,expected)])
            self.assertEqual(loaded,m)
            from paper_pov.learning_retention import pack_seed_release,unpack_seed_release
            pack_seed_release(root/"seed",root/"release.tar.gz")
            self.assertEqual(unpack_seed_release(root/"release.tar.gz",root/"restored"),m)
            self.assertEqual(file_sha(root/"restored"/"source-00.jsonl.gz"),file_sha(root/"seed"/"source-00.jsonl.gz"))
            from paper_pov.learning_retention import read_rows
            row=list(read_rows(root/"seed"/"source-00.jsonl.gz"))[0]
            self.assertEqual(row["anchors"],[a])
            self.assertEqual(row["outcomes"],[o])
            with self.assertRaisesRegex(ValueError,"original cohort"):
                load_seed(root/"seed",[("archive",sha,"b"*64)])

    def test_cold_archive_preserves_batches_and_rejects_missing_history(self):
        from paper_pov.learning_retention import compact_live_state,assemble_history
        old="2026-11-01T00:00:00Z"
        recent="2026-11-05T00:00:00Z"
        state=dict(schema="market_wide_continuity_v1",production_applied=False,
            evaluation_asof_utc="2026-11-06T00:00:00Z",
            anchors=[dict(prediction_id="a",entry_utc=old),dict(prediction_id="b",entry_utc=recent)],
            outcomes=[dict(prediction_id="a",entry_utc=old,horizon_hours=48,hit=None)],
            shadow_predictions=[dict(prediction_id="x",batch_id="mixed",entry_utc=old),
                                dict(prediction_id="y",batch_id="mixed",entry_utc=recent),
                                dict(prediction_id="z",batch_id="old",entry_utc=old)],
            shadow_outcomes=[dict(prediction_id="z",entry_utc=old,horizon_hours=48,hit=True)])
        state["digest"]=canonical_digest(state)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            first=compact_live_state(state,root/"a")
            self.assertEqual([p["prediction_id"] for p in first["anchors"]],["b"])
            self.assertEqual(len(first["shadow_predictions"]),2)
            self.assertEqual(assemble_history(first,root/"a")["outcomes"],state["outcomes"])
            with self.assertRaisesRegex(ValueError,"Missing prior"):
                compact_live_state(first,root/"b")
            second=compact_live_state(first,root/"b",previous_directory=root/"a")
            self.assertEqual(first,second)
            self.assertEqual(len(assemble_history(second,root/"b")["shadow_predictions"]),3)

    def test_durable_archive_rejects_wrong_hash_scope_state_and_unexpected_members(self):
        from paper_pov.learning_retention import pack_durable_checkpoint,unpack_durable_checkpoint
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            source=root/"src"
            source.mkdir()
            from paper_pov.learning_retention import CHECKPOINT_FILES
            for n in CHECKPOINT_FILES:
                (source/n).write_text("{}")
            state={"digest":"a"*64,"ledger_generation":7}
            receipt={"digest":"b"*64}
            with patch("paper_pov.learning_retention.verify_checkpoint_directory",return_value=(state,receipt)):
                archive=root/"checkpoint.tar.gz"
                m=pack_durable_checkpoint(source,archive,run_id="123",scope="pr")
                self.assertEqual(unpack_durable_checkpoint(archive,root/"ok",scope="pr",expected_sha=file_sha(archive)),m)
                with self.assertRaisesRegex(ValueError,"checksum"):
                    unpack_durable_checkpoint(archive,root/"bad",scope="pr",expected_sha="c"*64)
                with self.assertRaisesRegex(ValueError,"manifest"):
                    unpack_durable_checkpoint(archive,root/"wrong",scope="main",expected_sha=file_sha(archive))
                (source/"secret.txt").write_text("not part of research")
                with self.assertRaisesRegex(ValueError,"Unexpected checkpoint"):
                    pack_durable_checkpoint(source,archive,run_id="123",scope="pr")

if __name__=="__main__":
    unittest.main()
