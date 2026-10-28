"""Bounded, read-only Kraken archive HTTP probe; never downloads full parts.

Only use on an isolated network-enabled research runner. This is NOT archive validation.
The 2026Q2 archive is five ~2GB parts; do not treat a range response as a checksum.
"""
import argparse
import json
import urllib.request
from urllib.parse import urlparse

HOST = "assets.kraken.com"
BASE = "https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part"
MAX_BYTES = 65536

def probe(part=0, opener=None):
    if not isinstance(part,int) or not 0<=part<=4: raise ValueError("part must be 0..4")
    url = BASE + f"{part:02d}"
    if urlparse(url).hostname != HOST: raise ValueError("unexpected host")
    request = urllib.request.Request(url, headers={"Range":f"bytes=0-{MAX_BYTES-1}","User-Agent":"Cryptoscanner-isolated-research-probe/1.0"})
    open_url = opener or urllib.request.urlopen
    with open_url(request, timeout=12) as response:
        status = response.status
        headers = response.headers
        if status != 206: raise RuntimeError("Range request not honored; abort without reading response body")
        content_range = headers.get("Content-Range","")
        if not content_range.startswith(f"bytes 0-{MAX_BYTES-1}/"):
            raise RuntimeError("Unexpected content range; abort")
        chunk = response.read(MAX_BYTES+1)
        if len(chunk)!=MAX_BYTES: raise RuntimeError("Truncated or oversized response")
        return {"part":part,"range_status":status,"content_range":content_range,"bytes_read":len(chunk),"verified_archive":False,"sha256_verified":False}

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--part",type=int,default=0);args=p.parse_args();print(json.dumps(probe(args.part),indent=2))
