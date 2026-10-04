export interface Observation{pair:string;observedAt:string;score:number;displacementPct:number;alerted:boolean}
export interface Outcome{pair:string;maxReturn24h:number;thresholdCrossedAt?:string}
export function misses(obs:Observation[],outcomes:Outcome[],threshold=20){return outcomes.filter(o=>o.maxReturn24h>=threshold).filter(o=>!obs.some(x=>x.pair===o.pair&&x.alerted&&(!o.thresholdCrossedAt||Date.parse(x.observedAt)<Date.parse(o.thresholdCrossedAt)))).map(o=>({pair:o.pair,maxReturn24h:o.maxReturn24h,reason:obs.some(x=>x.pair===o.pair)?"observed_not_promoted":"not_discovered"}))}
