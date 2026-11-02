# Role A: strict Kraken early-mover research — 2026-11-02 UTC

**Research/shadow only; no production scoring, trade, ledger write or BUY.** Actual archived historical data, NOT a live PAPER scorer replay. Reproduce with Python historical/role_a_utc_gate_experiment.py strict-kraken-training.zip --compact --output replayed.json and compare with the committed result JSON.

## Source and evaluation

Successful [Kraken Historical Backfill #38029912468](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/38029912468), retained artifact #11662155953. SHA256 research.ndjson = 0f42814dcf1cc63167f24dbc571534964fbaad564ef3e5ae7ed321a19bda905d; research_training.ndjson = 766683bae34744d825f0ee68335fd2e474ccc77d77849e46b2e4a8ecaf81778c. Strict full eligible 15m research population with 5m continuity checks: **391,457 USD market/anchor rows, 180 USD pairs**, October 2025–June 2026, NOT November.

Chronological train before Feb 28, validation Mar 1–Apr 29, untouched test May 1–Jun 29, with 24h embargo across boundaries. Label: max 24h future 5m sampled **CLOSE** increase >=20% / >=30%; not executable fills or exchange highs. Features exclusively as-of 5/15/60m returns, trade/volume acceleration, volatility. Thresholds frozen before test. Validation selected high volatility by top-3 distinct positive pair-days then window hits. Conditioned rules fill remaining slots from frozen absolute-momentum proxy; negative control ranks alphabetically. Explicit false positives, unique positive pair-days and 24h same-pair cooldown mitigate overlapping-window inflation.

**Non-equivalence:** Historical rows lack Kraken ticker UTC-open, bid/ask spread, 24h USD notional and live top-24 OHLC preselection. Our price-only gate proxy uses the observed SAME-DAY 00:00 UTC 5m close, never future interpolation. Missing midnight is UNKNOWN, not a proven live rejection. The archive has ~15 USD markets per timestamp vs 604 live; top-12 nearly saturates. Do not claim exact live gate misses or actual production ranker lift.

## Test price-only UTC-midnight proxy (+0.25% through +12%)

| Proxy class | Test anchors | Future +20% windows | Future +30% windows | +30% pair-days |
|---|---:|---:|---:|---:|
| Below +0.25% | 56,385 | 870 | **442** | 37 |
| Above +12% | 1,372 | 423 | **201** | 14 |
| Pass | 21,875 | 775 | **338** | 26 |
| Missing midnight **UNKNOWN** | 13,039 | 1,746 | **1,102** | 49 |

Of 981 test +30% windows with known midnight reference, **643 (65.5%)** were outside this price-only proxy, **442** below the +0.25% bound. A concrete historical warning, **NOT** a quantified live exclusion rate. Upper-bound failures can be already-extended moves.

## Same top-12 budget, untouched May–June test

Each ungated ranker makes **66,961** picks. Entire test universe has **2,083** positive +30% market/windows and **89** positive pair-days. False positives are picks without a +30% future close increase, not necessarily losing trades.

| Frozen ranker | +30% hits | Precision | False positives | Positive pair-days | 24h cooldown positive picks |
|---|---:|---:|---:|---:|---:|
| Absolute 60m momentum **proxy baseline** | 1,962 | 2.93% | 64,999 | **89** | 48 |
| High 60m volatility | **2,041** | **3.05%** | 64,920 | **89** | 48 |
| Trade-count acceleration | 1,387 | 2.07% | 65,574 | 87 | 48 |
| Quiet trade-leading-volume | 1,941 | 2.90% | 65,020 | 89 | 48 |
| Quiet volume-leading-trades | 1,885 | 2.81% | 65,076 | 88 | 48 |
| Quiet low-move/high-activity | 1,956 | 2.92% | 65,005 | 89 | 48 |
| Low-volatility + positive-5m breakout proxy | 1,959 | 2.93% | 65,002 | 89 | 48 |
| Volatility with early directional constraint | 1,735 | 2.59% | 65,226 | 89 | 48 |
| Alphabetic negative control | 1,125 | 1.68% | 65,836 | 49 | 27 |

High volatility yields **79 additional correlated +30% windows**, but **ZERO additional positive pair-days** and **ZERO additional cooldown positive picks**. It is NOT established practical improvement. With price-only proxy gate, volatility selects 21,517 picks, 338 +30% hits, 26 positive pair-days.

## Secondary top-3 diagnostic (16,980 picks per rule)

Validation: high volatility 1,017 +30% windows vs momentum 951. Untouched test: volatility **1,812/16,980 = 10.67%** vs momentum **1,587/16,980 = 9.35%** (+225 correlated windows). However volatility catches **85 distinct positive pair-days** vs momentum **86**, both **48** cooldown-positive picks. Trade-only 516 windows, quiet/high-activity 1,359, compression/breakout proxy 1,533, trade-leading-volume 943. **No episode-level improvement.**

## Decision and next iteration

**NO GO for live promotion.** Archived proxy cannot reproduce live UTC-open/spread/notional/OHLC selection, and top-12 apparent improvement is saturated and correlated. Negative trade-acceleration result and missed positive windows below price gate are retained.

**Next experiment:** acquire actual as-of rejected-market snapshots (ticker today.open, bid/ask spread, USD notional, OHLC selection reason, trade-count acceleration, contemporaneous 5m features), without a second writer. Freeze a liquidity-aware volatility-expansion + signed-return challenger and compare prospectively at the **same live top-12 budget**, on disjoint 1h/6h observations, reporting unique liquid +20/+30% episodes, false positives and lead time. Do not treat June archive as November data. Six adversarial tests and exact-head CI, then independent Role V review before merge.
