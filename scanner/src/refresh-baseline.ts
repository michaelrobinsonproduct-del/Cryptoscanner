export function refreshExtensionPct(firstAsk:number|null,secondAsk:number|null){if(!firstAsk||!secondAsk||firstAsk<=0||secondAsk<=0)return null;return(secondAsk/firstAsk-1)*100}
export function newerRefresh(firstAt:string,secondAt:string){const a=Date.parse(firstAt),b=Date.parse(secondAt);return Number.isFinite(a)&&Number.isFinite(b)&&b>a}
