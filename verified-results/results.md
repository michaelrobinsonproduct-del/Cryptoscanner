# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:21:14.290570+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44956152793
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 11956805fc1a8029bd17ccd23b45c92a10014849 (atomic ledger/results publication)
**Ledger generation:** 1194 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 490.23 | 100.083 | 96.223 | +7.44% | -0.03% | 1.40x | 7.6 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04501 | 86.087 | 89.683 | +6.61% | +0.40% | 0.44x | 6.7 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 786.31 | 85.501 | 79.703 | +3.75% | +0.34% | 1.41x | 3.1 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7084 | 84.213 | 89.929 | +5.40% | -0.11% | 0.48x | 5.7 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | TAO/USD | 184.9489 | 84.032 | 69.245 | +2.46% | -0.04% | 10.51x | 6.0 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1680.88 | 82.924 | 81.581 | +3.80% | +0.01% | 1.13x | 0.1 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.8886 | 77.650 | 64.745 | +1.61% | +0.29% | 2.15x | 3.1 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XRP/USD | 0.92621 | 74.956 | 68.427 | +1.93% | -0.00% | 1.65x | 0.1 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEARL/USD | 1.9748 | 72.275 | 76.117 | +8.01% | +0.54% | 0.34x | 24.9 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | SOL/USD | 70.13 | 72.082 | 68.754 | +2.07% | +0.03% | 1.32x | 1.4 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 11 | QNT/USD | 142.23 | 69.802 | 69.340 | +2.50% | +0.43% | 0.83x | 6.3 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 60157 | 67.942 | 71.069 | +2.30% | -0.03% | 0.70x | 0.0 | 2026-11-21T22:21:06.345823+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.223 | 490.23 | -0.03% | 1.40x |
| 2 | UNI/USD | 89.929 | 4.7084 | -0.11% | 0.48x |
| 3 | NIGHT/USD | 89.683 | 0.04501 | +0.40% | 0.44x |
| 4 | ETH/USD | 81.581 | 1680.88 | +0.01% | 1.13x |
| 5 | ZEC/USD | 79.703 | 786.31 | +0.34% | 1.41x |
| 6 | PEARL/USD | 76.117 | 1.9748 | +0.54% | 0.34x |
| 7 | XBT/USD | 71.069 | 60157 | -0.03% | 0.70x |
| 8 | QNT/USD | 69.340 | 142.23 | +0.43% | 0.83x |
| 9 | TAO/USD | 69.245 | 184.9489 | -0.04% | 10.51x |
| 10 | SOL/USD | 68.754 | 70.13 | +0.03% | 1.32x |
| 11 | XRP/USD | 68.427 | 0.92621 | -0.00% | 1.65x |
| 12 | NEAR/USD | 64.745 | 2.8886 | +0.29% | 2.15x |

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

- Persisted scans: 1194; predictions: 9637; observations: 722311.
- Matured sampled outcomes across 1/6/24/48h: 12892; gap abstentions: 21526. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44956152793 · **Generation:** 1194 · **Legacy run:** 44956152793
**Main quote time:** 2026-11-21T22:21:14.290570+00:00 · **Legacy report time:** 2026-11-21T22:22:05.832773+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 490.23 | 100.08 | -0.03% | 1.40x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04501 | 86.09 | +0.40% | 0.44x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD ⭐ | 786.31 | 85.50 | +0.34% | 1.41x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.7084 | 84.21 | -0.11% | 0.48x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 5 | TAO/USD | 184.9489 | 84.03 | -0.04% | 10.51x | STRONG 72/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1680.88 | 82.92 | +0.01% | 1.13x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 7 | NEAR/USD | 2.8886 | 77.65 | +0.29% | 2.15x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD | 0.92621 | 74.96 | -0.00% | 1.65x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 9 | PEARL/USD | 1.9748 | 72.28 | +0.54% | 0.34x | MODERATE 56/100 | VERY_HIGH 82/100 | Watch |
| 10 | SOL/USD | 70.13 | 72.08 | +0.03% | 1.32x | STRONG 71/100 | HIGH 55/100 | Watch |
| 11 | QNT/USD | 142.23 | 69.80 | +0.43% | 0.83x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 60157 | 67.94 | -0.03% | 0.70x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 788.11 | 96.89 | +0.34% | 1.41x | 39914 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
