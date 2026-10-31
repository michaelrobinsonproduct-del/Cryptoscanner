import copy
import csv
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
import zipfile
from build_reusable_ohlc_evidence import build, inspect


def sample(tmp, *, n=578, bad=False):
    archive = Path(tmp) / "source.zip"
    rows = []
    for i in range(n):
        rows.append([str(i*300), "100", "130" if i==2 else "100", "100", "100", "10", "2"])
    if bad:
        rows[10][0] = rows[9][0]
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerows(rows)
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("TESTUSD_5.csv", buf.getvalue())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    cohort = {"archive_sha256": digest, "real_labels": 0,
              "selection": "test_stable_selection", "selected": [{"member": "TESTUSD_5.csv"}]}
    return archive, digest, cohort


class Tests(unittest.TestCase):
    def test_roundtrip_and_mature_candidate_windows_not_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp)
            out = Path(tmp) / "evidence.zip"
            manifest = build(archive, cohort, out, expected_archive_sha256=sha)
            self.assertEqual(manifest["markets"]["TESTUSD_5.csv"]["retained_rows"], 578)
            result = inspect(out, expected_archive_sha256=sha)
            self.assertEqual(result["coverage"]["TESTUSD_5.csv"]["candidate_windows"]["48"], 2)
            self.assertEqual(result["real_labels"], 0)

    def test_wrong_source_digest_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp)
            with self.assertRaises(ValueError):
                build(archive, cohort, Path(tmp)/"out.zip", expected_archive_sha256="0"*64)

    def test_duplicate_timestamp_fails_and_cleans_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp, bad=True)
            out = Path(tmp)/"out.zip"
            with self.assertRaises(ValueError): build(archive, cohort, out, expected_archive_sha256=sha)
            self.assertFalse(out.exists())

    def test_output_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp)
            out = Path(tmp)/"out.zip"; out.write_bytes(b"existing")
            with self.assertRaises(FileExistsError): build(archive, cohort, out, expected_archive_sha256=sha)
            self.assertEqual(out.read_bytes(), b"existing")

    def test_tampered_evidence_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp)
            out = Path(tmp)/"out.zip"
            build(archive, cohort, out, expected_archive_sha256=sha)
            with zipfile.ZipFile(out, "a") as z:
                z.writestr("candles/EXTRA_5.csv", "x")
            with self.assertRaises(ValueError): inspect(out, expected_archive_sha256=sha)

    def test_gap_breaks_48h_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive, sha, cohort = sample(tmp, n=578)
            with zipfile.ZipFile(archive, "r") as z: data=z.read("TESTUSD_5.csv").decode()
            rows=list(csv.reader(io.StringIO(data)))
            rows.pop(100)
            buf=io.StringIO();csv.writer(buf,lineterminator="\n").writerows(rows)
            archive.unlink()
            with zipfile.ZipFile(archive,"w") as z:z.writestr("TESTUSD_5.csv",buf.getvalue())
            sha=hashlib.sha256(archive.read_bytes()).hexdigest();cohort["archive_sha256"]=sha
            out=Path(tmp)/"out.zip"
            build(archive,cohort,out,expected_archive_sha256=sha)
            self.assertEqual(inspect(out, expected_archive_sha256=sha)["coverage"]["TESTUSD_5.csv"]["candidate_windows"]["48"],0)


if __name__ == "__main__": unittest.main()
