/** Single source of truth for quarantine decisions and health reporting. */
export const DEFAULT_QUARANTINE_MS=30_000;
export type PairHealth={failures:number;lastFailure:number;lastSuccess:number};
export function quarantined(h:PairHealth|undefined,now:number,cooldownMs=DEFAULT_QUARANTINE_MS):boolean {
 return !!h && Number.isFinite(now) && Number.isFinite(h.lastFailure) && h.failures>=2 && cooldownMs>0 && now>=h.lastFailure && now-h.lastFailure<cooldownMs;
}
export function quarantineCount(states:Iterable<PairHealth>,now:number,cooldownMs=DEFAULT_QUARANTINE_MS):number {
 let n=0;for(const h of states)if(quarantined(h,now,cooldownMs))n++;return n;
}
export function quarantineUntil(h:PairHealth):string|null {
 return h.failures>=2&&Number.isFinite(h.lastFailure)?new Date(h.lastFailure+DEFAULT_QUARANTINE_MS).toISOString():null;
}
