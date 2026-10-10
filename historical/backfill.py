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
rows_written=0; episodes_written=0
outdir="historical/output";os.makedirs(outdir,exist_ok=True)
with open(outdir+"/research.ndjson","w",encoding="utf-8") as research_out, open(outdir+"/moves.ndjson","w",encoding="utf-8") as moves_out, zipfile.ZipFile(zp) as z:
 names=[n for n in z.namelist() if n.endswith("_5.csv")]
 print("5m files",len(names),flush=True)
 for ni,n in enumerate(names):
  pair=os.path.basename(n)[:-6]
  bars=[]
  with z.open(n) as raw:
   txt=(x.decode("utf-8") for x in raw)
   for r in csv.reader(txt):
    if not r: continue
    try:
     timestamp=float(r[0])
     if not math.isfinite(timestamp) or not timestamp.is_integer():continue
     t=int(timestamp)
    except (ValueError,TypeError,OverflowError):continue
    if t<START-3600 or t>END+86400 or t%300!=0: continue
    if len(r)<7: continue
    o,hg,lo,c,v,tr=map(num,r[1:7])
    if None in (o,hg,lo,c,v) or not all(math.isfinite(q) for q in (o,hg,lo,c,v)) or min(o,hg,lo,c)<=0 or v<0 or lo>hg or not lo<=o<=hg or not lo<=c<=hg or tr is None or not math.isfinite(tr) or tr<0:continue
    bars.append((t,o,hg,lo,c,v,tr or 0))
  if len(bars)<300:continue
  # Deterministic duplicate policy: preserve the first valid candle at each timestamp.
  bars.sort(key=lambda bar:bar[0])
  bars=list({bar[0]:bar for bar in reversed(bars)}.values())
  bars.sort(key=lambda bar:bar[0])
  if len(bars)<300:continue
  # Prefix gap counts allow constant-time validation of each 1h/24h window.
  gaps=[0]*len(bars)
  for j in range(1,len(bars)):
   gaps[j]=gaps[j-1]+(bars[j][0]-bars[j-1][0]!=300)
  close=[x[4] for x in bars]; vol=[x[5] for x in bars]; trades=[x[6] for x in bars]
  # Emit completed episodes immediately rather than accumulating every market in memory.
  def emit_episode(group):
   global episodes_written
   best=max(group,key=lambda r:r["max_forward_return_pct"]);first=group[0]
   # Future-labeled early windows are not verified real-time scanner alerts.
   ep={"pair":first["pair"],"move_start":first["anchor_at"],"peak_at":None,"baseline_price":first["anchor_price"],"peak_price":None,"max_return_pct":best["max_forward_return_pct"],"earliest_signal_at":None,"extension_at_signal_pct":None,"caught_early":False,"source":"kraken_archive_5m_2026q2","evidence":{"windows":len(group),"max_anchor_gap_minutes":15,"retrospective_label_only":True,"live_alert_verified":False}}
   moves_out.write(json.dumps(ep,separators=(",",":"))+"\n")
   episodes_written+=1
  grp=[]
  for i in range(12,len(bars)-288): # inspect every 5m candle; select wall-clock quarter-hour anchors
   t=bars[i][0]
   if not START<=t<END or t%900!=0:continue
   if t-bars[i-12][0]!=3600 or gaps[i]!=gaps[i-12]:continue
   c=close[i]; p5=pct(close[i-1],c); p15=pct(close[i-3],c); p60=pct(close[i-12],c)
   prevv=sum(vol[i-12:i-6]); curv=sum(vol[i-6:i]); preva=sum(trades[i-12:i-6]); cura=sum(trades[i-6:i])
   vacc=curv/prevv if prevv>0 else None; tacc=cura/preva if preva>0 else None
   rets=[pct(close[j-1],close[j]) if pct(close[j-1],close[j]) is not None else 0 for j in range(i-11,i+1)]
   vola=statistics.pstdev(rets) if len(rets)>1 else 0
   if i+288>=len(bars) or bars[i+288][0]-t!=86400 or gaps[i+288]!=gaps[i]:continue
   fwd=[bar[4] for bar in bars[i+1:i+289]]
   mx=max((v for x in fwd if (v:=pct(c,x)) is not None),default=None)
   if mx is None:continue
   control_sampled=(t//86400)%7==0 and (t%3600==0)
   early=p60 is not None and abs(p60)<=3
   rec={"pair":pair,"anchor_at":datetime.fromtimestamp(t,timezone.utc).isoformat(),"anchor_price":c,"pre_return_5m_pct":p5,"pre_return_15m_pct":p15,"pre_return_60m_pct":p60,"volume_accel":vacc,"trade_accel":tacc,"volatility_pct":vola,"max_forward_return_pct":mx,"still_early":early,"major_mover":mx>=20,"control_sampled":control_sampled,"source":"kraken_archive_5m_2026q2","features":{"interval":"5m","no_lookahead":True}}
   research_out.write(json.dumps(rec,separators=(",",":"))+"\n")
   rows_written+=1
   if rec["major_mover"]:
    if grp and t-datetime.fromisoformat(grp[-1]["anchor_at"]).timestamp()>900:
     emit_episode(grp);grp=[]
    grp.append(rec)
   elif grp:
    emit_episode(grp);grp=[]
  if grp:emit_episode(grp)
  if ni%50==0:print("processed",ni,"research",rows_written,flush=True)
with open(outdir+"/summary.json","w") as f:json.dump({"research_rows":rows_written,"move_episodes":episodes_written,"start":"2025-10-04","archive_end":"2026-06-30","source":"Kraken OHLCVT 5m","note":"historical L2 unavailable; not fabricated"},f)
print(json.dumps({"ok":True,"research_rows":rows_written,"move_episodes":episodes_written}))
