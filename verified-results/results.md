# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T09:51:09.478390+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45009410769
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 6391cb7cc835d7cb5f3bcd5495d70a38e92f21f8 (atomic ledger/results publication)
**Ledger generation:** 1266 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 192.7566 | 96.686 | 78.326 | +3.78% | +0.67% | 4.99x | 5.5 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ETH/USD | 1707.04 | 81.405 | 63.135 | +1.47% | +0.65% | 3.63x | 4.3 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 8.71435 | 77.622 | 59.496 | +1.39% | +0.63% | 5.16x | 5.0 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6565 | 75.085 | 63.427 | +1.42% | +0.85% | 1.74x | 3.0 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PUMP/USD | 0.002432 | 73.360 | 66.280 | +3.75% | +0.54% | 1.44x | 4.1 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04481 | 69.505 | 49.874 | +1.20% | +0.93% | 13.42x | 4.5 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ASTER/USD | 0.50773 | 69.152 | 61.673 | +4.55% | +0.29% | 1.60x | 9.4 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SOL/USD | 70.35 | 60.366 | 53.242 | +0.26% | +0.43% | 1.50x | 7.1 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ZEC/USD | 796.89 | 57.959 | 63.819 | +2.41% | -0.08% | 0.45x | 16.0 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | BNB/USD | 551.49 | 57.799 | 42.348 | +0.75% | +0.49% | 2.30x | 4.0 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 11 | VVV/USD | 25.407 | 57.621 | 62.952 | +2.04% | -0.53% | 0.73x | 12.6 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | NEAR/USD | 2.9351 | 55.707 | 61.035 | +1.69% | +0.28% | 0.33x | 11.6 | 2026-11-22T09:51:01.404299+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 78.326 | 192.7566 | +0.67% | 4.99x |
| 2 | PUMP/USD | 66.280 | 0.002432 | +0.54% | 1.44x |
| 3 | ZEC/USD | 63.819 | 796.89 | -0.08% | 0.45x |
| 4 | SUI/USD | 63.427 | 0.6565 | +0.85% | 1.74x |
| 5 | ETH/USD | 63.135 | 1707.04 | +0.65% | 3.63x |
| 6 | VVV/USD | 62.952 | 25.407 | -0.53% | 0.73x |
| 7 | ASTER/USD | 61.673 | 0.50773 | +0.29% | 1.60x |
| 8 | NEAR/USD | 61.035 | 2.9351 | +0.28% | 0.33x |
| 9 | LINK/USD | 59.496 | 8.71435 | +0.63% | 5.16x |
| 10 | SOL/USD | 53.242 | 70.35 | +0.43% | 1.50x |
| 11 | NIGHT/USD | 49.874 | 0.04481 | +0.93% | 13.42x |
| 12 | BNB/USD | 42.348 | 551.49 | +0.49% | 2.30x |

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

- Persisted scans: 1266; predictions: 10112; observations: 766103.
- Matured sampled outcomes across 1/6/24/48h: 14548; gap abstentions: 22171. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45009410769 · **Generation:** 1266 · **Legacy run:** 45009410769
**Main quote time:** 2026-11-22T09:51:09.478390+00:00 · **Legacy report time:** 2026-11-22T09:52:02.852264+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 192.7566 | 96.69 | +0.67% | 4.99x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1707.04 | 81.41 | +0.65% | 3.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD | 8.71435 | 77.62 | +0.63% | 5.16x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6565 | 75.08 | +0.85% | 1.74x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | PUMP/USD ⭐ | 0.002432 | 73.36 | +0.54% | 1.44x | STRONG 92/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.04481 | 69.51 | +0.93% | 13.42x | STRONG 90/100 | HIGH 55/100 | Watch |
| 7 | ASTER/USD ⭐ | 0.50773 | 69.15 | +0.29% | 1.60x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 8 | SOL/USD | 70.35 | 60.37 | +0.43% | 1.50x | STRONG 75/100 | HIGH 55/100 | Watch |
| 9 | ZEC/USD | 796.89 | 57.96 | -0.08% | 0.45x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | BNB/USD | 551.49 | 57.80 | +0.49% | 2.30x | STRONG 84/100 | HIGH 55/100 | Watch |
| 11 | VVV/USD | 25.407 | 57.62 | -0.53% | 0.73x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | NEAR/USD | 2.9351 | 55.71 | +0.28% | 0.33x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 192.4013 | 98.65 | +0.67% | 4.99x | 7123 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ICNT/USD | 0.3608 | 80.26 | +1.55% | 2.30x | 3041 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 3 | PUMP/USD ⭐ | 0.002433 | 78.17 | +0.54% | 1.44x | 4579 | STRONG 89/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6564 | 71.33 | +0.85% | 1.74x | 7328 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 5 | ASTER/USD ⭐ | 0.5074 | 71.24 | +0.29% | 1.60x | 2066 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 6 | ETH/USD ⭐ | 1705.52 | 67.28 | +0.65% | 3.63x | 45241 | STRONG 99/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** TAO/USD, ETH/USD, SUI/USD, PUMP/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
