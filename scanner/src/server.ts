import { evaluatePromotion } from "./promotion";

const port=Number(process.env.PORT||3000);
const controlUrl=process.env.CONTROL_COLLECTOR_URL||"https://kraken-collector-production.up.railway.app";
const kraken="https://api.kraken.com/0/public";

async function json(url:string){const r=await fetch(url,{signal:AbortSignal.timeout(45000)});if(!r.ok)throw new Error(`HTTP ${r.status} ${url}`);return r.json() as Promise<any>}
async function confirm(pair:string){
const q="pair="+encodeURIComponent(pair);
const [t,d,tr]=await Promise.all(["Ticker?","Depth?count=10&","Trades?"].map(p=>json(kraken+"/"+p+q)));
for(const z of [t,d,tr])if(!Array.isArray(z?.error)||z.error.length)throw Error("kraken_api_error");
const first=(o:any)=>Object.entries(o??{}).find(([k])=>k!=="last")?.[1] as any;
const tick=first(t.result),book=first(d.result),trades=first(tr.result);
const bestBid=Number(tick?.b?.[0]),bestAsk=Number(tick?.a?.[0]);
const twoSidedBook=!!book?.bids?.length&&!!book?.asks?.length;
const executableBbo=twoSidedBook&&bestBid>0&&bestAsk>=bestBid&&Number(book.bids[0][0])>0&&Number(book.asks[0][0])>=Number(book.bids[0][0]);
const age=Array.isArray(trades)&&trades.length?Date.now()/1000-Number(trades[trades.length-1][2]):null;
const recentTradeConfirmation=age!==null&&Number.isFinite(age)&&age>=0&&age<=60;
return {pair,success:!!(executableBbo&&recentTradeConfirmation),twoSidedBook,executableBbo:!!executableBbo,recentTradeConfirmation,newestTradeAgeSeconds:age,bestBid,bestAsk,fetchedAt:new Date().toISOString()};
}
async function cycle(){const scan=await json(`${controlUrl}/scan`);const rows=(scan.candidates??scan.results??scan.shortlist??[]).slice(0,20);const out=[];for(const x of rows){const pair=x.pair??x.symbol;if(!pair)continue;const score=Number(x.score??x.discovery_score??0), displacementPct=Number(x.displacement_pct??x.displacementPct??999), discoveryPrice=Number(x.price??x.last??x.ask??0);if(x.displacement_pct==null&&x.displacementPct==null)continue;if(score<80||Math.abs(displacementPct)>3||!discoveryPrice)continue;try{const first=await confirm(pair);await Bun.sleep(2500);const second=await confirm(pair);const result=evaluatePromotion({pair,score,discoveryPrice,discoveryAt:new Date().toISOString(),displacementPct},first,second);out.push({pair,score,displacement_pct:displacementPct,...result,first,second})}catch(e){out.push({pair,score,displacement_pct:displacementPct,decision:"WATCH",reason:"confirmation_error",error:String(e)})}}return {mode:"shadow",control_untouched:true,at:new Date().toISOString(),candidates:out}}
let last:any=null,lastError:string|null=null,running=false,cycles=0;
async function run(){if(running)return last;running=true;try{last=await cycle();cycles++;lastError=null;return last}catch(e){lastError=String(e);throw e}finally{running=false}}
setTimeout(()=>{void (async()=>{for(;;){try{await run()}catch{}await Bun.sleep(300000)}})()},5000);
Bun.serve({port,async fetch(req){const u=new URL(req.url);if(u.pathname==="/health")return Response.json({service:"cryptoscanner-challenger",version:"0.1.0",mode:"shadow",control_untouched:true,running,cycles,lastError});if(u.pathname==="/dashboard")return Response.json({service:"cryptoscanner-challenger",version:"0.1.0",mode:"shadow",control_untouched:true,running,cycles,last_error:lastError,last_result:last});if(u.pathname==="/cycle"){try{return Response.json(await run())}catch(e){return Response.json({error:String(e)},{status:502})}}return Response.json({service:"cryptoscanner-challenger",endpoints:["/health","/dashboard","/cycle"]})}});
