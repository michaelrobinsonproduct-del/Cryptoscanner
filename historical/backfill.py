import os, zipfile, json, urllib.request, tempfile, hashlib, shutil

BASE = "https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part{}"
EXPECTED_ZIP_SHA256 = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
work = tempfile.mkdtemp()
zip_path = os.path.join(work, "archive.zip")

def download(url, dst):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as src, open(dst, "wb") as out:
        shutil.copyfileobj(src, out, length=8 * 1024 * 1024)

# Stream each part directly into the assembled ZIP, deleting the temporary part
# immediately. This avoids keeping five parts plus the assembled ZIP at once.
with open(zip_path, "wb") as assembled:
    for i in range(5):
        suffix = f"{i:02d}"
        url = BASE.format(suffix)
        part = os.path.join(work, f"part{suffix}")
        try:
            download(url, part)
        except Exception as e:
            raise RuntimeError(f"Kraken archive download failed part{suffix}: {url}: {e}") from e
        size = os.path.getsize(part)
        if size < 1024:
            raise RuntimeError(f"Kraken archive part{suffix} unexpectedly small: {size} bytes")
        print(f"downloaded part{suffix}: {size} bytes", flush=True)
        with open(part, "rb") as src:
            shutil.copyfileobj(src, assembled, length=8 * 1024 * 1024)
        os.remove(part)

h = hashlib.sha256()
with open(zip_path, "rb") as f:
    for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
        h.update(chunk)
actual = h.hexdigest()
print(f"assembled sha256: {actual}", flush=True)
if actual != EXPECTED_ZIP_SHA256:
    raise RuntimeError(f"Archive checksum mismatch: expected {EXPECTED_ZIP_SHA256}, got {actual}")

# Do not extract the entire ~10GB archive. Validate it and inventory only the
# intervals needed by the feature builder; later processing can stream members.
with zipfile.ZipFile(zip_path) as z:
    bad = z.testzip()
    if bad:
        raise RuntimeError(f"ZIP integrity failure at member: {bad}")
    names = [n for n in z.namelist() if n.endswith(("_1.csv", "_5.csv", "_15.csv", "_60.csv"))]
    if not names:
        raise RuntimeError("No 1m/5m/15m/60m CSVs found in archive")
    manifest = [n for n in z.namelist() if n.endswith("MANIFEST.json")]
    print(json.dumps({
        "ok": True,
        "files": len(names),
        "manifest_present": bool(manifest),
        "sha256": actual,
        "note": "archive validated without full extraction; ready for streamed feature reconstruction"
    }))
