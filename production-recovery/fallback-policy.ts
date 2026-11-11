export type SourceState = "WS_VALID"|"REST_VALID"|"STALE"|"SOURCE_FAILED"|"QUARANTINED";
export type Decision = "ELIGIBLE_FOR_CONFIRMATION"|"WATCH";
export function fallbackDecision(state:SourceState, restIndependentlyVerified:boolean,tradeFresh:boolean,bookFresh:boolean,tickerFresh:boolean):Decision{
 if(!tradeFresh||!bookFresh||!tickerFresh)return "WATCH";
 if(state==="WS_VALID")return "ELIGIBLE_FOR_CONFIRMATION";
 if((state==="SOURCE_FAILED"||state==="QUARANTINED"||state==="REST_VALID")&&restIndependentlyVerified)return "ELIGIBLE_FOR_CONFIRMATION";
 return "WATCH";
}
