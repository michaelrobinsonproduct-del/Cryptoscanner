import os,glob,zipfile,subprocess,csv,json,urllib.request,tempfile,shutil
BASE="https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part0{}"
work=tempfile.mkdtemp(); parts=[]
for i in range(5):
 p=os.path.join(work,f"p{i}")
 urllib.request.urlretrieve(BASE.format(i),p); parts.append(p)
zip_path=os.path.join(work,"archive.zip")
with open(zip_path,"wb") as out:
 for p in parts:
  with open(p,"rb") as f: shutil.copyfileobj(f,out)
  os.remove(p)
outdir=os.path.join(work,"x");os.mkdir(outdir)
with zipfile.ZipFile(zip_path) as z:
 names=[n for n in z.namelist() if n.endswith("_5.csv") or n.endswith("_15.csv") or n.endswith("_60.csv")]
 for n in names:z.extract(n,outdir)
os.remove(zip_path)
print(json.dumps({"ok":True,"files":len(names),"note":"archive extracted; feature reconstruction stage ready"}))
