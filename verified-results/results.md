# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:25:14.888129+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44258644128
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** eeb3943870e7ab1635e6743fbb25ab6ee21b127f (atomic ledger/results publication)
**Ledger generation:** 566 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2947 | 83.660 | 70.519 | +6.74% | -0.37% | 2.58x | 17.0 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | XRP/USD | 0.99266 | 78.997 | 62.167 | +1.03% | +0.37% | 5.38x | 0.1 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | PEARL/USD | 1.9029 | 57.856 | 68.849 | +5.10% | -0.95% | 0.38x | 5.8 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.019425 | 51.598 | 55.673 | +4.05% | -0.10% | 0.64x | 7.2 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 31/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.309642 | 44.960 | 44.359 | +0.56% | +0.16% | 0.98x | 0.3 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 42/100 | HIGH 62/100 | Watch | WATCH |
| 6 | AKT/USD | 0.518 | 39.185 | 40.504 | +1.71% | +0.08% | 0.83x | 7.7 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 40/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XDC/USD | 0.03088 | 38.812 | 48.151 | +1.85% | +0.03% | 0.05x | 6.5 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AKE/USD | 0.01017028 | 32.379 | 29.680 | +1.86% | -1.56% | 2.05x | 35.8 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | TRUST/USD | 0.04792 | 29.690 | 34.286 | +1.63% | +0.42% | 0.33x | 20.9 | 2026-11-18T07:25:06.441346+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 70.519 | 0.2947 | -0.37% | 2.58x |
| 2 | PEARL/USD | 68.849 | 1.9029 | -0.95% | 0.38x |
| 3 | XRP/USD | 62.167 | 0.99266 | +0.37% | 5.38x |
| 4 | SENT/USD | 55.673 | 0.019425 | -0.10% | 0.64x |
| 5 | XDC/USD | 48.151 | 0.03088 | +0.03% | 0.05x |
| 6 | TRX/USD | 44.359 | 0.309642 | +0.16% | 0.98x |
| 7 | AKT/USD | 40.504 | 0.518 | +0.08% | 0.83x |
| 8 | TRUST/USD | 34.286 | 0.04792 | +0.42% | 0.33x |
| 9 | AKE/USD | 29.680 | 0.01017028 | -1.56% | 2.05x |

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

- Persisted scans: 566; predictions: 4774; observations: 341701.
- Matured sampled outcomes across 1/6/24/48h: 4125; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44258644128 · **Generation:** 566 · **Legacy run:** 44258644128
**Main quote time:** 2026-11-18T07:25:14.888129+00:00 · **Legacy report time:** 2026-11-18T07:25:32.840318+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2947 | 83.66 | -0.37% | 2.58x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 2 | XRP/USD ⭐ | 0.99266 | 79.00 | +0.37% | 5.38x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEARL/USD | 1.9029 | 57.86 | -0.95% | 0.38x | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing |
| 4 | SENT/USD | 0.019425 | 51.60 | -0.10% | 0.64x | WEAK 31/100 | EXTREME 88/100 | Do nothing |
| 5 | TRX/USD | 0.309642 | 44.96 | +0.16% | 0.98x | WEAK 42/100 | HIGH 62/100 | Watch |
| 6 | AKT/USD | 0.518 | 39.18 | +0.08% | 0.83x | WEAK 40/100 | HIGH 67/100 | Watch |
| 7 | XDC/USD | 0.03088 | 38.81 | +0.03% | 0.05x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 8 | AKE/USD | 0.01017028 | 32.38 | -1.56% | 2.05x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | TRUST/USD | 0.04792 | 29.69 | +0.42% | 0.33x | WEAK 35/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99225 | 71.36 | +0.37% | 5.38x | 32301 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
