/**
 * Shadow-only prospective big-mover evaluation.
 * Inputs must be chronological observations captured at or before their asOf timestamp.
 * Never treats retrospective labels as live catches or research watches as buys.
 */
export function evaluateEarlyMoverSignals(signals, observations, { horizonsHours = [24, 48, 72], thresholdsPct = [20, 50, 100, 500] } = {}) {
  const parse = value => {
    if (typeof value !== "string" || !/(Z|[+-]\d\d:\d\d)$/.test(value)) throw new Error("Timestamp must include timezone");
    const time = Date.parse(value);
    if (!Number.isFinite(time)) throw new Error("Invalid timestamp");
    return time;
  };
  const finitePositive = n => typeof n === "number" && Number.isFinite(n) && n > 0;
  const seen = new Set();
  const series = new Map();
  for (const o of observations) {
    if (!o || typeof o.market !== "string" || !finitePositive(o.price)) throw new Error("Invalid observation");
    const t = parse(o.at);
    const key = o.market + "|" + t;
    if (seen.has(key)) throw new Error("Duplicate observation");
    seen.add(key);
    if (!series.has(o.market)) series.set(o.market, []);
    series.get(o.market).push({ t, price: o.price });
  }
  for (const rows of series.values()) rows.sort((a,b) => a.t - b.t);
  const results = [];
  for (const s of signals) {
    if (!s || typeof s.market !== "string" || !finitePositive(s.referencePrice)) throw new Error("Invalid signal");
    if (s.tier !== "research_watch" && s.tier !== "confirmed_watch") throw new Error("Unrecognized shadow signal tier");
    const at = parse(s.at);
    const capturedAt = parse(s.capturedAt);
    if (capturedAt < at) throw new Error("Signal capture precedes event timestamp");
    const rows = series.get(s.market) || [];
    const entry = rows.find(o => o.t === at);
    if (!entry || Math.abs(entry.price / s.referencePrice - 1) > 0.000001) throw new Error("Missing matching entry observation");
    const horizonResults = horizonsHours.map(hours => {
      if (!Number.isFinite(hours) || hours <= 0) throw new Error("Invalid horizon");
      const end = at + hours * 3600000;
      const future = rows.filter(o => o.t > at && o.t <= end);
      const complete = rows.some(o => o.t >= end);
      if (!complete) return { hours, status: "pending", thresholds: null };
      const peak = Math.max(entry.price, ...future.map(o => o.price));
      const trough = Math.min(entry.price, ...future.map(o => o.price));
      const maxGainPct = (peak / entry.price - 1) * 100;
      return { hours, status: "matured", maxGainPct, maxDrawdownPct: (trough / entry.price - 1) * 100,
        thresholds: Object.fromEntries(thresholdsPct.map(pct => [String(pct), maxGainPct >= pct])) };
    });
    results.push({ market: s.market, at: s.at, tier: s.tier, buyVerified: false, horizons: horizonResults });
  }
  return { schemaVersion: 1, shadowOnly: true, signals: results };
}
