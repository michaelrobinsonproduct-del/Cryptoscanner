export function targetCandleOpen(dueSeconds:number):number {
  if(!Number.isFinite(dueSeconds)||dueSeconds<=0) throw new Error("invalid_outcome_deadline");
  return Math.floor(dueSeconds/3600)*3600-3600;
}
export function candleReturn(baselineAsk:number,candleClose:number):number {
  if(!(Number.isFinite(baselineAsk)&&Number.isFinite(candleClose)&&baselineAsk>0&&candleClose>0)) throw new Error("invalid_price");
  return (candleClose/baselineAsk-1)*100;
}
export function isClosedByDeadline(targetOpen:number,nowMs:number):boolean {
  return Number.isFinite(targetOpen)&&Number.isFinite(nowMs)&&nowMs>=(targetOpen+3600)*1000;
}

export function validBaseline(baselineAsk:number,baselineAt:string,dueSeconds:number):boolean {
 const at=Date.parse(baselineAt);
 return Number.isFinite(baselineAsk)&&baselineAsk>0&&Number.isFinite(at)&&Number.isFinite(dueSeconds)&&dueSeconds>0&&at<dueSeconds*1000;
}
