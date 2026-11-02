# Actual deep learning experiment: strict Kraken 2026Q2 data, +30% target

**2026-11-01, research-only.** This is a measured, trained-and-held-out experimental ranking improvement on archived data, **NOT** an improvement to the live PAPER scanner. Source: successful [Kraken Historical Backfill run #38029912468](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/38029912468), exact code `0a7e7e4d29bc676a506aed7e35d4b44ad1c9cd43`, retained `kraken-historical-derived` artifact **#11662155953** (53,537,974 bytes ZIP). It contains 148,495 compact training records; 22,518 systematic control anchors. This is the **strict** October 10 reconstruction with contiguous 5-minute history and exact 24h forward window checks. Do **not** substitute earlier October 9 artifact #11596344892: that earlier source lacked these strict gap checks and yielded misleadingly inflated results.

## Experimental design

Streamed the exact artifact and retained **only `control_sampled=true`** USD-pair anchors with all finite pre-entry features. Outcome: **max forward 24h price increase >=30% from five-minute *closes***, not exchange highs or executable profits. Features measured at anchor only: 5/15/60m returns, 30m volume acceleration, 30m trade-count acceleration, 60m return volatility. No future fields enter ranking.

- **14,483** valid USD control anchors, **112** distinct USD pairs, **884** as-of timestamps. This is a subset of the market, not the live 604-pair universe.
- Chronological training **8,080** rows (before Feb 28), validation **2,777** (Mar 1–Apr 29), untouched test **3,288** (May 1–Jun 30); **338** anchors in 24h boundary embargo days were excluded from model fitting/selection. Training 207 +30% labels; validation 39; test 97.
- Candidate models: regularized standardized logistic regression (`C=0.2`, balanced), histogram gradient boosting (depth 3), random forest (depth 6), compared against prior-60m absolute-momentum, signed momentum, trade acceleration, volume acceleration, and early+trades proxy rankings. Model choice made using validation **top-1 per timestamp** +30% hits, breaking ties by +20% hits. Chosen model: **logistic regression**.
- **Top-1** is deliberate: the historical control set averages ~18 USD candidates per timestamp. Top-12 would select most of the tiny control universe and create meaningless high recall. These are same-universe research proxies, **not** a replay of live top-12 ticker/volume/spread selection.

## Measured ranking results

| Top-1 ranker | Validation +30% hits / 192 timestamps | Untouched May–June +30% hits / 183 timestamps | Test +20% hits |
|---|---:|---:|---:|
| **Selected six-feature logistic challenger** | **38** | **51 (27.87%)** | **84** |
| Prior-60m absolute-momentum proxy | 28 | 41 (22.40%) | 68 |
| Prior-60m positive-momentum proxy | 26 | 36 (19.67%) | 58 |
| Trade-count acceleration alone | 6 | 7 (3.83%) | 16 |
| Volume acceleration alone | 2 | 5 (2.73%) | 10 |
| Early (abs 60m <=3%) + trade acceleration | 2 | 1 (0.55%) | 3 |

**Positive historical research result:** on the same test timestamps and candidate set, the frozen validation-selected logistic ranker had **10 additional +30% positive windows** over the strongest simple absolute-momentum proxy: **51 vs 41**, a **24.4% relative improvement in hit count** (27.87% vs 22.40% top-1 sampled precision). Paired disagreements: model-only 14, proxy-only 4. Eight weekly blocks give an exploratory paired bootstrap difference of **+1.04 to +11.54 percentage points** (95% percentile interval). This is **not** a claim of independent 183 opportunities; observations and forward labels overlap.

## What actually drove the gain — ablation

A diagnostic ablation **after** the frozen test (therefore exploratory, NOT another untouched test) found:

- **Volatility-only** top-1: **51/183** +30% windows, the same as the full logistic model.
- Full model **without volatility**: only **19/183**.
- Full model **without trade acceleration**: still **51/183**.
- Full model **without volume acceleration**: still **51/183**.
- Momentum-only model: **34/183**.

The standardized logistic coefficient on 60m volatility was **+2.372**, dwarfing signed 60m return **+0.371**, volume acceleration **+0.154**, 5m return **+0.057**, 15m return **−0.011**, and trade acceleration **−0.081**. **Volatility expansion, not raw trade-count acceleration, is the strongest historical research hypothesis to test prospectively.** But high volatility can also identify already-extended, illiquid or crashing markets; require direction, liquidity and entry-stage checks.

## Why this is not yet a proven better *early mover* scanner

- The 51 positive logistic windows represented **10 distinct positive pairs / 12 positive pair-days**, versus **11 pairs / 13 pair-days** for the simple absolute-momentum proxy. **The improvement did NOT increase distinct positive pair-day coverage.** It often repeatedly selected the same mover.
- Restricting picks to abs(prior 60m return) <=3%: logistic **29/183** +30% windows (9 positive pair-days), vs absolute-momentum proxy **17/183** (8 positive pair-days). This is promising but **only +1 distinct pair-day**, not a strong episode-level improvement.
- With a **24h no-repeat-pair cooldown**, logistic caught **8/158** +30% positive selections vs absolute-momentum **7/158**. The practical gain shrank to **one**.
- No historical spread, bid/ask, order-book depth, executable fills, or actual live UTC-open screening features. The 24h +30% label is a sampled *future close maximum*, not a realizable +30% trade. Data ends June 2026, and May–June regimes may not represent November.
- Models were compared to **historical feature proxies**, not the actual live PAPER scorer. The ablation used the test set after model selection, so a new untouched period is required before promoting a volatility-only rule.

## Learning decision and next iteration

**Advance a volatility-expansion + early-entry + liquidity conditioned *research challenger*, not the unconditioned 2× trade-count rule.** Freeze the proposed challenger before testing it on newer out-of-time data and actual as-of PAPER observations. Optimize for **distinct +30% mover episodes caught early, lead time and false positives**, not repeated overlapping positive windows. Collect rejected-market feature/reason evidence (especially ESPORTS/USD) to test it against the actual live top-12 budget. Keep existing live PAPER scoring unchanged until prospective comparison demonstrates better recommendations.

**This is the first concrete measured historical ranking improvement in the renewed research effort; it is NOT yet a verified improvement in delivered live recommendations.**
