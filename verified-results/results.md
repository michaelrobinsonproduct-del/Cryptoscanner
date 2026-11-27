# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T02:41:24.939148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45929624752
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fd9140503e6d607ea590179cbb916fc52882b703 (atomic ledger/results publication)
**Ledger generation:** 1947 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 600; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.8 | 108.564 | 90.003 | +9.41% | +0.71% | 2.58x | 20.0 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 64.91 | 102.843 | 83.723 | +4.32% | +0.82% | 15.60x | 3.1 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.55277 | 91.127 | 72.186 | +3.07% | +0.79% | 8.05x | 8.6 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 470.95 | 90.329 | 73.262 | +3.06% | +0.60% | 2.41x | 6.4 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1727.35 | 89.233 | 71.425 | +2.35% | +0.56% | 3.87x | 0.1 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XRP/USD | 0.96314 | 88.078 | 70.088 | +2.16% | +0.60% | 8.20x | 0.1 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | LTC/USD | 44.72 | 85.750 | 67.715 | +2.24% | +0.61% | 2.57x | 4.5 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | SOL/USD | 72.6 | 85.576 | 70.691 | +2.34% | +0.66% | 2.16x | 1.4 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | UNI/USD | 4.8579 | 82.803 | 70.227 | +4.47% | -0.48% | 6.12x | 6.4 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 61524.5 | 81.437 | 66.869 | +1.70% | +0.35% | 2.28x | 0.0 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | NEAR/USD | 3.1293 | 81.154 | 70.979 | +2.67% | +0.23% | 1.90x | 5.4 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | HBAR/USD | 0.05497 | 64.136 | 47.033 | +1.87% | +0.42% | 9.09x | 1.8 | 2026-11-27T02:41:18.524869+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 90.003 | 745.8 | +0.71% | 2.58x |
| 2 | HYPE/USD | 83.723 | 64.91 | +0.82% | 15.60x |
| 3 | XMR/USD | 73.262 | 470.95 | +0.60% | 2.41x |
| 4 | LINK/USD | 72.186 | 9.55277 | +0.79% | 8.05x |
| 5 | ETH/USD | 71.425 | 1727.35 | +0.56% | 3.87x |
| 6 | NEAR/USD | 70.979 | 3.1293 | +0.23% | 1.90x |
| 7 | SOL/USD | 70.691 | 72.6 | +0.66% | 2.16x |
| 8 | UNI/USD | 70.227 | 4.8579 | -0.48% | 6.12x |
| 9 | XRP/USD | 70.088 | 0.96314 | +0.60% | 8.20x |
| 10 | LTC/USD | 67.715 | 44.72 | +0.61% | 2.57x |
| 11 | XBT/USD | 66.869 | 61524.5 | +0.35% | 2.28x |
| 12 | HBAR/USD | 47.033 | 0.05497 | +0.42% | 9.09x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 1947; predictions: 17066; observations: 1179231.
- Matured sampled outcomes across 1/6/24/48h: 37466; gap abstentions: 25463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45929624752 · **Generation:** 1947 · **Legacy run:** 45929624752
**Main quote time:** 2026-11-27T02:41:24.939148+00:00 · **Legacy report time:** 2026-11-27T02:42:16.217886+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 745.8 | 108.56 | +0.71% | 2.58x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.91 | 102.84 | +0.82% | 15.60x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.55277 | 91.13 | +0.79% | 8.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 470.95 | 90.33 | +0.60% | 2.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1727.35 | 89.23 | +0.56% | 3.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.96314 | 88.08 | +0.60% | 8.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | LTC/USD | 44.72 | 85.75 | +0.61% | 2.57x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 72.6 | 85.58 | +0.66% | 2.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | UNI/USD | 4.8579 | 82.80 | -0.48% | 6.12x | STRONG 71/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD ⭐ | 61524.5 | 81.44 | +0.35% | 2.28x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | NEAR/USD | 3.1293 | 81.15 | +0.23% | 1.90x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 12 | HBAR/USD | 0.05497 | 64.14 | +0.42% | 9.09x | STRONG 87/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.92 | 100.00 | +0.82% | 15.60x | 13831 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 746.37 | 93.47 | +0.71% | 2.58x | 37097 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1727.35 | 89.78 | +0.56% | 3.87x | 31388 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 474.13 | 89.55 | +0.60% | 2.41x | 18330 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.55277 | 88.32 | +0.79% | 8.05x | 6943 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | AKE/USD | 0.0015732 | 87.36 | +3.28% | 3.82x | 8137 | STRONG 84/100 | EXTREME 87/100 | Do nothing |
| 7 | XRP/USD ⭐ | 0.96281 | 84.63 | +0.60% | 8.20x | 21119 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 72.6 | 83.94 | +0.66% | 2.16x | 33988 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | BCH/USD | 218.81 | 82.56 | +1.21% | 1.59x | 2586 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 10 | XDG/USD | 0.0577167 | 79.98 | +0.33% | 2.62x | 5262 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 11 | PEPE/USD | 3.587e-06 | 78.85 | +0.45% | 3.16x | 5348 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 12 | XBT/USD ⭐ | 61510.1 | 78.22 | +0.35% | 2.28x | 133632 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, HYPE/USD, LINK/USD, XMR/USD, ETH/USD, XRP/USD, SOL/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
