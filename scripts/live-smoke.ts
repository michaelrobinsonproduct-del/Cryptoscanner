const collector=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app";
const confirm=process.env.CONTROL_CONFIRM_URL||"https://kraken-rest-confirm-production.up.railway.app";
const sleep=(ms:number)=>new Promise(r=>setTimeout(r,ms));
async function j(u:string,attempts=3,timeoutMs=45000){let last:any;for(let i=0;i<attempts;i++){try{const r=await fetch(u,{signal:AbortSignal.timeout(timeoutMs),headers:{"cache-control":"no-cache"}});if(r.ok)return r.json() as Promise<any>;last=new Error("http_"+r.status);}catch(e){last=e}if(i<attempts-1)await sleep(1500*(i+1));}throw last}
const h=await j(collector+"/health");if(!h)throw new Error("collector_health_unavailable");
const scan=await j(collector+"/scan");const rows=scan.candidates??scan.results??scan.shortlist??[];
if(!Array.isArray(rows)||!rows.length)throw new Error("empty_scan");
const failures:Array<{pair:string;reason:string}>=[];
const deadline=Date.now()+120000;
let confirmed:any=null,pair:string|null=null;
for(const x of rows.slice(0,Math.min(rows.length,20))){
  if(Date.now()>=deadline){failures.push({pair:"remaining",reason:"confirmation_budget_exhausted"});break}
  const p=x.pair??x.symbol;
  if(typeof p!=="string"||!p.trim()){failures.push({pair:"unknown",reason:"missing_pair"});continue}
  try{
    const z=await j(confirm+"/confirm?pair="+encodeURIComponent(p),1,Math.min(8000,Math.max(1000,deadline-Date.now())));
    if(z.success===true&&z.two_sided_book===true&&z.executable_bbo===true){confirmed=z;pair=p;break}
    failures.push({pair:p,reason:[!z.success?"not_success":null,!z.two_sided_book?"no_two_sided_book":null,!z.executable_bbo?"no_executable_bbo":null].filter(Boolean).join(",")||"unconfirmed"});
  }catch(e){failures.push({pair:p,reason:"request_error:"+String(e instanceof Error?e.message:e).slice(0,100)})}
}
if(!confirmed||!pair){
  console.error(JSON.stringify({ok:false,reason:"no_executable_confirmation",scanCount:rows.length,checked:failures.length,failures}));
  throw new Error("no_executable_confirmation");
}
console.log(JSON.stringify({ok:true,scanCount:rows.length,checked:failures.length+1,pair,tradeFresh:!!confirmed.recent_trade_confirmation,tradeAge:confirmed.newest_trade_age_seconds??null,build:h.build??h.version??null,failures}));
