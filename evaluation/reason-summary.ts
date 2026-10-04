export function reasonSummary(rows:{reason?:string|null}[]){const out:Record<string,number>={};for(const x of rows){const k=x.reason||'unspecified';out[k]=(out[k]||0)+1}return out}
