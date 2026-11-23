# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T03:21:15.094839+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45105303889
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** a47c75d066510797d1892a69cabdc53a182dd4ef (atomic ledger/results publication)
**Ledger generation:** 1374 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.017424 | 82.605 | 61.714 | +8.27% | +4.03% | 1.07x | 44.3 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 94/100 | Do nothing | WATCH |
| 2 | ETH/USD | 1739.33 | 70.447 | 58.236 | +1.03% | +0.57% | 1.94x | 7.9 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.93229 | 69.569 | 55.849 | +0.51% | +0.74% | 2.00x | 5.5 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0176 | 63.475 | 59.947 | +1.20% | +1.10% | 0.80x | 7.0 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XBT/USD | 61421.8 | 60.898 | 57.872 | +0.41% | +0.56% | 1.02x | 0.0 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 71.37 | 60.280 | 61.633 | +1.05% | +0.65% | 0.54x | 1.4 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | AUD/USD | 0.6638 | 56.661 | 41.676 | +0.34% | -0.00% | 8.89x | 2.1 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0554476 | 55.244 | 48.310 | +0.30% | +0.80% | 1.29x | 2.3 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.413e-06 | 54.556 | 40.625 | +0.71% | +1.56% | 1.61x | 5.9 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 10 | UNI/USD | 4.7681 | 54.484 | 48.859 | +1.86% | +0.63% | 1.25x | 12.2 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XMR/USD | 496.92 | 54.029 | 54.079 | +0.65% | +0.44% | 0.78x | 10.7 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 12 | DRV/USD | 0.3699 | 51.654 | 46.512 | +0.28% | -0.01% | 1.52x | 0.8 | 2026-11-23T03:21:08.431320+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 61.714 | 0.017424 | +4.03% | 1.07x |
| 2 | SOL/USD | 61.633 | 71.37 | +0.65% | 0.54x |
| 3 | NEAR/USD | 59.947 | 3.0176 | +1.10% | 0.80x |
| 4 | ETH/USD | 58.236 | 1739.33 | +0.57% | 1.94x |
| 5 | XBT/USD | 57.872 | 61421.8 | +0.56% | 1.02x |
| 6 | XRP/USD | 55.849 | 0.93229 | +0.74% | 2.00x |
| 7 | XMR/USD | 54.079 | 496.92 | +0.44% | 0.78x |
| 8 | UNI/USD | 48.859 | 4.7681 | +0.63% | 1.25x |
| 9 | XDG/USD | 48.310 | 0.0554476 | +0.80% | 1.29x |
| 10 | DRV/USD | 46.512 | 0.3699 | -0.01% | 1.52x |
| 11 | AUD/USD | 41.676 | 0.6638 | -0.00% | 8.89x |
| 12 | PEPE/USD | 40.625 | 3.413e-06 | +1.56% | 1.61x |

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

- Persisted scans: 1374; predictions: 11255; observations: 831871.
- Matured sampled outcomes across 1/6/24/48h: 18131; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 89 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45105303889 · **Generation:** 1374 · **Legacy run:** 45105303889
**Main quote time:** 2026-11-23T03:21:15.094839+00:00 · **Legacy report time:** 2026-11-23T03:21:56.927062+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.017424 | 82.60 | +4.03% | 1.07x | STRONG 71/100 | EXTREME 94/100 | Do nothing |
| 2 | ETH/USD ⭐ | 1739.33 | 70.45 | +0.57% | 1.94x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.93229 | 69.57 | +0.74% | 2.00x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 3.0176 | 63.48 | +1.10% | 0.80x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 5 | XBT/USD ⭐ | 61421.8 | 60.90 | +0.56% | 1.02x | STRONG 75/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD | 71.37 | 60.28 | +0.65% | 0.54x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 7 | AUD/USD | 0.6638 | 56.66 | -0.00% | 8.89x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0554476 | 55.24 | +0.80% | 1.29x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 9 | PEPE/USD | 3.413e-06 | 54.56 | +1.56% | 1.61x | STRONG 72/100 | HIGH 55/100 | Watch |
| 10 | UNI/USD ⭐ | 4.7681 | 54.48 | +0.63% | 1.25x | MODERATE 67/100 | HIGH 68/100 | Watch |
| 11 | XMR/USD | 496.92 | 54.03 | +0.44% | 0.78x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 12 | DRV/USD | 0.3699 | 51.65 | -0.01% | 1.52x | MODERATE 46/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.017453 | 83.62 | +4.03% | 1.07x | 5704 | STRONG 72/100 | EXTREME 94/100 | Do nothing |
| 2 | ETH/USD ⭐ | 1740.36 | 63.74 | +0.57% | 1.94x | 43420 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 3 | XBT/USD ⭐ | 61595 | 62.08 | +0.56% | 1.02x | 136030 | STRONG 76/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93311 | 59.66 | +0.74% | 2.00x | 20005 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 5 | UNI/USD ⭐ | 4.7767 | 56.56 | +0.63% | 1.25x | 4744 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** BLESS/USD, ETH/USD, XRP/USD, XBT/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
