const collector=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app";
const confirm=process.env.CONTROL_CONFIRM_URL||"https://kraken-rest-confirm-production.up.railway.app";
const sleep=(ms:number)=>new Promise(r=>setTimeout(r,ms));
async function j(u:string,attempts=3){let last:any;for(let i=0;i<attempts;i++){try{const r=await fetch(u,{signal:AbortSignal.timeout(45000),headers:{"cache-control":"no-cache"}});if(r.ok)return r.json() as Promise<any>;last=new Error(String(r.status));}catch(e){last=e}if(i<attempts-1)await sleep(1500*(i+1));}throw last}
const h=await j(collector+"/health");if(!h)throw new Error("collector_health_unavailable");
const scan=await j(collector+"/scan");const rows=scan.candidates??scan.results??scan.shortlist??[];if(!rows.length)throw new Error("empty_scan");
let confirmed:any=null,pair:string|null=null;
for(const x of rows.slice(0,5)){const p=x.pair??x.symbol;if(!p)continue;try{const z=await j(confirm+"/confirm?pair="+encodeURIComponent(p),2);if(z.success&&z.two_sided_book&&z.executable_bbo){confirmed=z;pair=p;break}}catch{}}
if(!confirmed||!pair)throw new Error("no_executable_confirmation_from_top5");
console.log(JSON.stringify({ok:true,scanCount:rows.length,pair,tradeFresh:!!confirmed.recent_trade_confirmation,tradeAge:confirmed.newest_trade_age_seconds??null,build:h.build??h.version??null}));
