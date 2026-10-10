import os,zipfile,json,urllib.request,tempfile,hashlib,shutil,csv,math,statistics,time
from datetime import datetime,timezone
BASE="https://assets.kraken.com/marketing/institutions/Kraken_OHLCVT_Full_2026Q2.zip.part{}"
SHA="fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
START=int(datetime(2025,10,4,tzinfo=timezone.utc).timestamp()); END=int(datetime(2026,7,1,tzinfo=timezone.utc).timestamp())
work=tempfile.mkdtemp(); zp=os.path.join(work,"archive.zip")
def dl(u,p):
 r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
 with urllib.request.urlopen(r,timeout=300) as s,open(p,"wb") as d: shutil.copyfileobj(s,d,8*1024*1024)
with open(zp,"wb") as out:
 for i in range(5):
  s=f"{i:02d}"; p=os.path.join(work,"p"+s); dl(BASE.format(s),p)
  with open(p,"rb") as f: shutil.copyfileobj(f,out,8*1024*1024)
  os.remove(p); print("part",s,"ok",flush=True)
h=hashlib.sha256()
with open(zp,"rb") as f:
 for b in iter(lambda:f.read(8*1024*1024),b""): h.update(b)
if h.hexdigest()!=SHA: raise RuntimeError("checksum mismatch")
def num(x):
 try:return float(x)
 except:return None
def pct(a,b): return (b/a-1)*100 if a and b else None
rows=[]; moves=[]
with zipfile.ZipFile(zp) as z:
 names=[n for n in z.namelist() if n.endswith("_5.csv")]
 print("5m files",len(names),flush=True)
 for ni,n in enumerate(names):
  pair=os.path.basename(n)[:-6]
  bars=[]
  with z.open(n) as raw:
   txt=(x.decode("utf-8") for x in raw)
   for r in csv.reader(txt):
    if not r: continue
    try:t=int(float(r[0]))
    except:continue
    if t<START-3600 or t>END+86400: continue
    if len(r)<7: continue
    o,hg,lo,c,v,tr=map(num,r[1:7])
    if None in (o,hg,lo,c,v):continue
    bars.append((t,o,hg,lo,c,v,tr or 0))
  if len(bars)<300:continue
  bars.sort()
  close=[x[4] for x in bars]; vol=[x[5] for x in bars]; trades=[x[6] for x in bars]
  pairrows=[]
  for i in range(12,len(bars)-288,3): # 15m anchors
   t=bars[i][0]
   if not START<=t<END:continue
   c=close[i]; p5=pct(close[i-1],c); p15=pct(close[i-3],c); p60=pct(close[i-12],c)
   prevv=sum(vol[i-12:i-6]); curv=sum(vol[i-6:i]); preva=sum(trades[i-12:i-6]); cura=sum(trades[i-6:i])
   vacc=curv/prevv if prevv>0 else None; tacc=cura/preva if preva>0 else None
   rets=[pct(close[j-1],close[j]) if pct(close[j-1],close[j]) is not None else 0 for j in range(i-11,i+1)]
   vola=statistics.pstdev(rets) if len(rets)>1 else 0
   fwd=close[i+1:min(len(close),i+289)]
   mx=max((v for x in fwd if (v:=pct(c,x)) is not None),default=None)
   if mx is None:continue
   control_sampled=(t//86400)%7==0 and (i%12==0)
   keep=mx>=10 or control_sampled
   if not keep:continue
   early=p60 is not None and abs(p60)<=3
   rec={"pair":pair,"anchor_at":datetime.fromtimestamp(t,timezone.utc).isoformat(),"anchor_price":c,"pre_return_5m_pct":p5,"pre_return_15m_pct":p15,"pre_return_60m_pct":p60,"volume_accel":vacc,"trade_accel":tacc,"volatility_pct":vola,"max_forward_return_pct":mx,"still_early":early,"major_mover":mx>=20,"control_sampled":control_sampled,"source":"kraken_archive_5m_2026q2","features":{"interval":"5m","no_lookahead":True}}
   pairrows.append(rec); rows.append(rec)
  # episode-dedupe major windows: new episode after >24h gap
  majors=[r for r in pairrows if r["major_mover"]]
  grp=[]
  for r in majors:
   ts=datetime.fromisoformat(r["anchor_at"]).timestamp()
   if not grp or ts-datetime.fromisoformat(grp[-1]["anchor_at"]).timestamp()<=86400: grp.append(r)
   else:
    moves.append(grp);grp=[r]
  if grp:moves.append(grp)
  if ni%50==0:print("processed",ni,"research",len(rows),flush=True)
outdir="historical/output";os.makedirs(outdir,exist_ok=True)
def dump(path,data):
 with open(path,"w") as f:
  for x in data:f.write(json.dumps(x,separators=(",",":"))+"\n")
dump(outdir+"/research.ndjson",rows)
eps=[]
for g in moves:
 best=max(g,key=lambda r:r["max_forward_return_pct"]); first=g[0]
 eps.append({"pair":first["pair"],"move_start":first["anchor_at"],"peak_at":None,"baseline_price":first["anchor_price"],"peak_price":None,"max_return_pct":best["max_forward_return_pct"],"earliest_signal_at":next((r["anchor_at"] for r in g if r["still_early"]),None),"extension_at_signal_pct":next((r["pre_return_60m_pct"] for r in g if r["still_early"]),None),"caught_early":any(r["still_early"] for r in g),"source":"kraken_archive_5m_2026q2","evidence":{"windows":len(g),"dedupe_gap_hours":24}})
dump(outdir+"/moves.ndjson",eps)
with open(outdir+"/summary.json","w") as f:json.dump({"research_rows":len(rows),"move_episodes":len(eps),"start":"2025-10-04","archive_end":"2026-06-30","source":"Kraken OHLCVT 5m","note":"historical L2 unavailable; not fabricated"},f)
print(json.dumps({"ok":True,"research_rows":len(rows),"move_episodes":len(eps)}))
