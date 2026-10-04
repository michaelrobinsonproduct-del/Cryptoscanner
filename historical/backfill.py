import os,zipfile,json,urllib.request,tempfile,shutil
BASE="https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part0{}"
work=tempfile.mkdtemp(); parts=[]
for i in range(5):
    url=BASE.format(i); p=os.path.join(work,f"part0{i}")
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req,timeout=120) as src, open(p,"wb") as dst:
            shutil.copyfileobj(src,dst)
    except Exception as e:
        raise RuntimeError(f"Kraken archive download failed part0{i}: {url}: {e}") from e
    size=os.path.getsize(p)
    if size < 1024: raise RuntimeError(f"Kraken archive part0{i} unexpectedly small: {size} bytes")
    print(f"downloaded part0{i}: {size} bytes",flush=True); parts.append(p)
zip_path=os.path.join(work,"archive.zip")
with open(zip_path,"wb") as out:
    for p in parts:
        with open(p,"rb") as f: shutil.copyfileobj(f,out)
        os.remove(p)
print(f"assembled archive: {os.path.getsize(zip_path)} bytes",flush=True)
outdir=os.path.join(work,"x");os.mkdir(outdir)
with zipfile.ZipFile(zip_path) as z:
    names=[n for n in z.namelist() if n.endswith("_5.csv") or n.endswith("_15.csv") or n.endswith("_60.csv")]
    if not names: raise RuntimeError("No 5m/15m/60m CSVs found in archive")
    for n in names:z.extract(n,outdir)
os.remove(zip_path)
print(json.dumps({"ok":True,"files":len(names),"note":"archive extracted; feature reconstruction stage ready"}))
