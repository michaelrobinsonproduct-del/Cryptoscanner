export type DataGate={scanCurrent:boolean;quoteComparable:boolean;twoSided:boolean;tradeFresh:boolean;secondRefresh:boolean}
export function failClosed(g:DataGate){const failed=Object.entries(g).filter(([,v])=>!v).map(([k])=>k);return{actionable:failed.length===0,failed}}
