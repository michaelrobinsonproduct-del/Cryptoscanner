"""Isolated Kraken multipart SHA-256 verifier: streams, never writes or extracts archive."""
import argparse,hashlib,json,shutil,time,urllib.request
from pathlib import Path
BASE="https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part"
SIZES=(2097152000,2097152000,2097152000,2097152000,583772104)
SHA="fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
DISK=25*1024**3;MEM=2*1024**3;DEADLINE=35*60;CHUNK=1024*1024
def capacity(disk=None,mem=None):
    if disk is None:disk=shutil.disk_usage(".").free
    if mem is None:
        lines=Path("/proc/meminfo").read_text().splitlines()
        mem=next((int(s.split()[1])*1024 for s in lines if s.startswith("MemAvailable:")),0)
    if disk<DISK:raise RuntimeError("Insufficient disk")
    if mem<MEM:raise RuntimeError("Insufficient memory")
    return {"disk_free":disk,"memory_available":mem}
def verify(opener=None,clock=None,disk=None,mem=None):
    resources=capacity(disk,mem);opener=opener or urllib.request.urlopen;clock=clock or time.monotonic
    started=clock();hashobj=hashlib.sha256();total=0;parts=[]
    for i,expected in enumerate(SIZES):
        if clock()-started>DEADLINE:raise RuntimeError("Deadline exceeded")
        req=urllib.request.Request(BASE+f"{i:02d}",headers={"Accept-Encoding":"identity","User-Agent":"Cryptoscanner-isolated-verify/1.0"})
        with opener(req,timeout=25) as response:
            if response.status!=200:raise RuntimeError("Unexpected HTTP status")
            length=response.headers.get("Content-Length")
            if length is None or not length.isdecimal() or int(length)!=expected:raise RuntimeError("Invalid Content-Length")
            if response.headers.get("Content-Encoding","identity").lower()!="identity":raise RuntimeError("Unexpected encoding")
            count=0
            while count<expected:
                if clock()-started>DEADLINE:raise RuntimeError("Deadline exceeded")
                block=response.read(min(CHUNK,expected-count))
                if not block:raise RuntimeError("Truncated response")
                count+=len(block);total+=len(block)
                if count>expected or total>sum(SIZES):raise RuntimeError("Byte cap exceeded")
                hashobj.update(block)
            if response.read(1):raise RuntimeError("Unexpected extra bytes")
        parts.append({"part":i,"bytes":count})
    if hashobj.hexdigest()!=SHA:raise RuntimeError("Full archive SHA256 mismatch")
    return {"resources":resources,"parts":parts,"total_bytes":total,"sha256":hashobj.hexdigest(),"full_archive_sha256_verified":True,"historical_data_validated":False}
if __name__=="__main__":
    argparse.ArgumentParser().parse_args()
    print(json.dumps(verify(),indent=2))
