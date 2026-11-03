export interface SelectedCandidate {
  pair: string;
  score: number;
  displacementPct: number;
  discoveredAt: string;
}
export function selectDiscoveryCandidates(scan: any): SelectedCandidate[] {
  const raw = scan?.candidates ?? scan?.results ?? scan?.shortlist ?? [];
  if (!Array.isArray(raw)) return [];
  const out: SelectedCandidate[] = [];
  for (const x of raw.slice(0, 20)) {
    if (!x || typeof x !== "object") continue;
    const pair = x.pair ?? x.symbol;
    const score = Number(x.score ?? x.discovery_score);
    const displacementPct = Number(x.displacement_pct ?? x.displacementPct);
    const discoveredAt = x.discovered_at ?? scan.fetched_at;
    if (typeof pair !== "string" || !pair.trim() ||
        !Number.isFinite(score) || !Number.isFinite(displacementPct) ||
        score < 80 || Math.abs(displacementPct) > 3 ||
        typeof discoveredAt !== "string" ||
        !Number.isFinite(Date.parse(discoveredAt))) continue;
    out.push({ pair, score, displacementPct, discoveredAt });
  }
  return out;
}
