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

if __name__=="__main__":
    unittest.main()
