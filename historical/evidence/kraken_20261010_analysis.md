# Historical Kraken evidence: why the October 2× trade rule cannot be promoted blindly

**Research-only audit, 2026-11-01.** Original exact model: `rebuild-history:historical_model.json`, Git blob SHA `7a082fdf394e06b5de6ceee50e09ade8c97b2b97` (identical copy in this branch). Original training run dated 2026-10-10. Source was Kraken 2026Q2 five-minute OHLCVT historical backfill, ending 2026-06-30. Outcome is **at least +20% maximum subsequent five-minute close within 24 hours** from the anchor, *not* an executable trade, +30% label, or prospective PAPER success.

## Actual recovered results, with disjoint historical partitions

| Historical signal or mutually exclusive stratum | Train hits / anchors | Train hit rate | May–June holdout hits / anchors | Holdout hit rate |
|---|---:|---:|---:|---:|
| All sampled control anchors | 513 / 17,523 | 2.93% | 182 / 4,995 | 3.64% |
| Prior 60m absolute price change <=3% | 334 / 17,028 | 1.96% | 99 / 4,697 | 2.11% |
| Prior 60m absolute price change >3% | 179 / 495 | 36.16% | 83 / 298 | 27.85% |
| 2× trade-count acceleration, regardless of prior move | 64 / 1,150 | 5.57% | 21 / 327 | 6.42% |
| Prior 60m <=3% **and** 2× trade-count acceleration | 34 / 1,061 | 3.20% | 6 / 272 | 2.21% |
| Prior 60m <=3% **without** 2× trade-count acceleration | 300 / 15,967 | 1.88% | 93 / 4,425 | 2.10% |
| Prior 60m >3% **and** 2× trade-count acceleration | 30 / 89 | 33.71% | 15 / 55 | 27.27% |
| Prior 60m >3% **without** 2× trade-count acceleration | 149 / 406 | 36.70% | 68 / 243 | 27.98% |
| Both 2× trade count and 2× volume | 49 / 933 | 5.25% | 17 / 277 | 6.14% |
| 2× trade count but not 2× volume | 15 / 217 | 6.91% | 4 / 50 | 8.00% |
| 2× volume but not 2× trade count | 55 / 2,913 | 1.89% | 19 / 747 | 2.54% |

All partition counts above are **derived exactly** by set subtraction from archived model aggregate counts; no reconstructed candles, invented anchors, or interpolated labels.

## Substantive discovery: a confounding pattern hidden by aggregate lift

The original October model approved `trades_2x` on a **1.76× holdout lift** (6.42% vs 3.64% overall). That sounds like a good scoring improvement. **But it does not survive a simple holdout stratification on prior 60-minute movement**:

- Among quiet/early anchors (absolute prior 60m change <=3%), 2× trade acceleration achieved **6/272 = 2.21%**, versus **93/4,425 = 2.10%** without it: only **1.05×**.
- Among already-moving/rebounding anchors (>3% absolute prior change), 2× trade acceleration achieved **15/55 = 27.27%**, versus **68/243 = 27.98%** without it: **0.97×**, slightly worse.
- Of the 21 holdout hits attributed to 2× trade acceleration, **15 (71.4%)** occurred in the >3% prior-move stratum, although that stratum represented only 55/327 (16.8%) of its selected anchors.
- The training period gave some within-early benefit (3.20% vs 1.88%), but it **did not replicate** in the chronological holdout (2.21% vs 2.10%).

This is a strong warning against applying the archived `trades_2x` approval as a universal early-entry bonus. The apparent aggregate lift is largely explained by selection of already-moving/rebounding markets. **It does not prove trade-count acceleration has no predictive value in better-defined, directional or regime-conditioned settings.**

## A second major discovery: the definition of 'early' itself requires revision

Only **298/4,995 = 5.97%** of holdout anchors had >3% absolute prior-hour movement, yet those anchors accounted for **83/182 = 45.6%** of all subsequently observed +20% outcomes. The same pattern appeared in training (179/513 = 34.9% of positive labels from 495/17,523 = 2.82% of anchors). Excluding all such anchors destroys much retrospective recall.

**However:** absolute movement includes negative drops/rebounds and positive already-extended surges; these aggregates do not reveal which. Therefore this is **not** justification to chase already-pumped coins. The correct next analysis separates signed 60m returns, time-to-peak, spread/liquidity and price extension, then evaluates early-entry usefulness on chronological, market-matched anchors.

Also note: historical `early_1h` is **abs(prior 60m return)<=3%**; it is NOT the live scanner's **UTC-day-open return >=0.25%** prefilter. These results cannot quantify misses from the live UTC-open gate or top-12 budget. That requires time-aligned raw anchors and actual scanner replay.

## Decision and next experiment

**Decision: DO NOT promote the October 2× trade-count rule as an unconditioned bonus.** Its aggregate approval is contradicted by stratified holdout evidence for the user's *early mover* objective. This is a real negative learning result from existing market data, not a production scoring change.

Next, use existing archived `research_training.ndjson` / `research.ndjson` to test signed prior 60m buckets (negative rebound / flat / 0–3% / 3–6% / >6% extension), trade and volume acceleration **within** each bucket, volatility compression, liquidity, time-to-first +20/+30%, and actual top-12 selection budget. Freeze rules on train, select on validation, evaluate on untouched chronological test; compare current PAPER and independent legacy ranker on identical as-of inputs. Report hits, misses, false positives and early lead time. Do not wait for perfect November 24/48h data to conduct this research.

**Scope and limitations:** Aggregates only; labels use forward peak of five-minute closes, not verified executable fills; correlated pair-time observations invalidate naive independent-sample confidence claims; old archive may not generalize to November; no +30% result or live improvement demonstrated here. `historical/aggregate_rule_audit.py` reproduces the arithmetic, Wilson intervals, and exploratory Fisher tails from the exact archived model.
