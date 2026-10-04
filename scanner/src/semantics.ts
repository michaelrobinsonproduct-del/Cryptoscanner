export type WindowName="discovery_baseline"|"refresh_1"|"refresh_2";
export interface PricePoint{price:number;at:string;source:string;window:WindowName}
export function movePct(from:PricePoint,to:PricePoint){if(from.price<=0||to.price<=0)return null;return (to.price/from.price-1)*100}
export function isStillEarly(first:PricePoint,second:PricePoint,maxExtensionPct=2){if(first.window!=="refresh_1"||second.window!=="refresh_2")return false;if(Date.parse(second.at)<=Date.parse(first.at))return false;const m=movePct(first,second);return m!==null&&m<=maxExtensionPct}
