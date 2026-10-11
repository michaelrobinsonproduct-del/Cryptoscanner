const collector=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app";
const kraken="https://api.kraken.com/0/public";
const sleep=(ms:number)=>new Promise(r=>setTimeout(r,ms));
async function j(u:string,attempts=2,timeoutMs=8000){let last:any;for(let i=0;i<attempts;i++){try{const r=await fetch(u,{signal:AbortSignal.timeout(timeoutMs),headers:{"cache-control":"no-cache"}});if(!r.ok)throw new Error("http_"+r.status);return await r.json() as any}catch(e){last=e;if(i<attempts-1)await sleep(500)}}throw last}
function first(result:any){return Object.entries(result??{}).find(([k,v])=>k!=="last"&&v&&typeof v==="object")?.[1] as any}
async function confirm(pair:string){
  const query="pair="+encodeURIComponent(pair);
  const [t,d,tr]=await Promise.all([j(kraken+"/Ticker?"+query,1),j(kraken+"/Depth?"+query+"&count=10",1),j(kraken+"/Trades?"+query,1)]);
  for(const response of [t,d,tr])if(!response||!Array.isArray(response.error)||response.error.length)throw new Error("kraken_api_error:"+String(response?.error?.join(",")??"invalid_response").slice(0,100));
  const ticker=first(t.result),depth=first(d.result),trades=first(tr.result);
  const bid=Number(ticker?.b?.[0]),ask=Number(ticker?.a?.[0]);
  const twoSided=Array.isArray(depth?.bids)&&depth.bids.length>0&&Array.isArray(depth?.asks)&&depth.asks.length>0;
  const bookBid=Number(depth?.bids?.[0]?.[0]),bookAsk=Number(depth?.asks?.[0]?.[0]);
  const executable=twoSided&&bid>0&&ask>=bid&&bookBid>0&&bookAsk>=bookBid;
  const tradeAge=Array.isArray(trades)&&trades.length?Date.now()/1000-Number(trades[trades.length-1]?.[2]):null;
  return {success:executable&&tradeAge!==null&&tradeAge>=0&&tradeAge<=60,two_sided_book:twoSided,executable_bbo:executable,recent_trade_confirmation:tradeAge!==null&&tradeAge>=0&&tradeAge<=60,newest_trade_age_seconds:tradeAge};
}
const health=await j(collector+"/health");if(!health)throw new Error("collector_health_unavailable");
const scan=await j(collector+"/scan");const rows=scan.candidates??scan.results??scan.shortlist??[];
if(!Array.isArray(rows)||!rows.length)throw new Error("empty_scan");
const failures:Array<{pair:string;reason:string}>=[];
const deadline=Date.now()+120000;
let selected:any=null,pair:string|null=null;
for(const x of rows.slice(0,Math.min(rows.length,20))){
  if(Date.now()>=deadline){failures.push({pair:"remaining",reason:"confirmation_budget_exhausted"});break}
  const p=x.pair??x.symbol;
  if(typeof p!=="string"||!p.trim()){failures.push({pair:"unknown",reason:"missing_pair"});continue}
  try{
    const z=await confirm(p);
    if(z.success&&z.two_sided_book&&z.executable_bbo&&z.recent_trade_confirmation){selected=z;pair=p;break}
    failures.push({pair:p,reason:[!z.two_sided_book?"no_two_sided_book":null,!z.executable_bbo?"no_executable_bbo":null,!z.recent_trade_confirmation?"stale_or_missing_trade":null].filter(Boolean).join(",")||"unconfirmed"});
  }catch(e){failures.push({pair:p,reason:"request_error:"+String(e instanceof Error?e.message:e).slice(0,120)})}
}
if(!selected||!pair){console.error(JSON.stringify({ok:false,reason:"no_fresh_executable_confirmation",scanCount:rows.length,checked:failures.length,failures}));throw new Error("no_fresh_executable_confirmation")}
console.log(JSON.stringify({ok:true,scanCount:rows.length,checked:failures.length+1,pair,tradeFresh:true,tradeAge:selected.newest_trade_age_seconds,build:health.build??health.version??null,confirmationSource:"independent_kraken_rest",failures}));
