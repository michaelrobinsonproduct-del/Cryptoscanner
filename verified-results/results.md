# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:30:56.032111+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45007793760
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 0a269561d367d964af9385871cbfc34b6c58485a (atomic ledger/results publication)
**Ledger generation:** 1264 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 190.844 | 80.841 | 70.117 | +2.75% | +0.75% | 1.70x | 8.2 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ASTER/USD | 0.50259 | 64.160 | 55.946 | +3.49% | +0.40% | 1.62x | 6.0 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 3 | ZEC/USD | 792.51 | 61.454 | 66.131 | +1.84% | +0.41% | 0.33x | 3.5 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6506 | 55.850 | 57.028 | +0.51% | +0.42% | 0.67x | 3.1 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9064 | 55.212 | 58.668 | +0.70% | +0.05% | 0.63x | 2.4 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | VVV/USD | 25.144 | 51.014 | 58.478 | +0.98% | +0.13% | 0.19x | 6.8 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 8.62978 | 46.806 | 53.425 | +0.41% | +0.13% | 0.27x | 2.8 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.002398 | 42.221 | 51.633 | +2.30% | -0.12% | 0.12x | 12.6 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | AVAX/USD | 6.592 | 38.212 | 46.210 | +0.44% | +0.14% | 0.13x | 3.0 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | TON/USD | 0.956 | 32.169 | 24.917 | +0.42% | +0.31% | 1.57x | 21.0 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | W/USD | 0.00815 | 26.500 | 27.452 | +0.37% | +0.49% | 0.66x | 12.3 | 2026-11-22T09:30:48.505430+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 70.117 | 190.844 | +0.75% | 1.70x |
| 2 | ZEC/USD | 66.131 | 792.51 | +0.41% | 0.33x |
| 3 | NEAR/USD | 58.668 | 2.9064 | +0.05% | 0.63x |
| 4 | VVV/USD | 58.478 | 25.144 | +0.13% | 0.19x |
| 5 | SUI/USD | 57.028 | 0.6506 | +0.42% | 0.67x |
| 6 | ASTER/USD | 55.946 | 0.50259 | +0.40% | 1.62x |
| 7 | LINK/USD | 53.425 | 8.62978 | +0.13% | 0.27x |
| 8 | PUMP/USD | 51.633 | 0.002398 | -0.12% | 0.12x |
| 9 | AVAX/USD | 46.210 | 6.592 | +0.14% | 0.13x |
| 10 | W/USD | 27.452 | 0.00815 | +0.49% | 0.66x |
| 11 | TON/USD | 24.917 | 0.956 | +0.31% | 1.57x |

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

- Persisted scans: 1264; predictions: 10089; observations: 764885.
- Matured sampled outcomes across 1/6/24/48h: 14512; gap abstentions: 22162. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45007793760 · **Generation:** 1264 · **Legacy run:** 45007793760
**Main quote time:** 2026-11-22T09:30:56.032111+00:00 · **Legacy report time:** 2026-11-22T09:31:36.499591+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 190.844 | 80.84 | +0.75% | 1.70x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | ASTER/USD ⭐ | 0.50259 | 64.16 | +0.40% | 1.62x | STRONG 87/100 | HIGH 60/100 | Consider small entry |
| 3 | ZEC/USD | 792.51 | 61.45 | +0.41% | 0.33x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | SUI/USD | 0.6506 | 55.85 | +0.42% | 0.67x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 5 | NEAR/USD | 2.9064 | 55.21 | +0.05% | 0.63x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 6 | VVV/USD | 25.144 | 51.01 | +0.13% | 0.19x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD | 8.62978 | 46.81 | +0.13% | 0.27x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 8 | PUMP/USD | 0.002398 | 42.22 | -0.12% | 0.12x | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | AVAX/USD | 6.592 | 38.21 | +0.14% | 0.13x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 10 | TON/USD | 0.956 | 32.17 | +0.31% | 1.57x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 11 | W/USD | 0.00815 | 26.50 | +0.49% | 0.66x | WEAK 38/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 190.5994 | 73.38 | +0.75% | 1.70x | 7076 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | ASTER/USD ⭐ | 0.5016 | 62.91 | +0.40% | 1.62x | 2053 | STRONG 86/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** TAO/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
