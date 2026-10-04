export interface TimedQuote { source:string; price:number; observedAt:string }
export function comparable(a:TimedQuote,b:TimedQuote,maxSkewMs=15_000){const ta=Date.parse(a.observedAt),tb=Date.parse(b.observedAt);return Number.isFinite(ta)&&Number.isFinite(tb)&&Math.abs(ta-tb)<=maxSkewMs&&a.price>0&&b.price>0}
export function deviationPct(a:TimedQuote,b:TimedQuote){if(!comparable(a,b))return null;return ((b.price/a.price)-1)*100}
