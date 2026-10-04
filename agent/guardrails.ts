export const protectedPaths=["deployment/production","secrets","ios/signing"];
export function changeAllowed(paths:string[]){return paths.every(p=>!protectedPaths.some(x=>p===x||p.startsWith(x+"/")))}
export const autonomousFlow=["diagnose_miss","propose_challenger","run_tests","historical_regression","prospective_shadow","compare_control","promote_if_policy_passes","retain_rollback"] as const;
