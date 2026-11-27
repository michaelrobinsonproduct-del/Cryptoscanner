# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T09:32:09.967136+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45974149451
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6de0645b86c72ff21182324897be0c59f434633 (atomic ledger/results publication)
**Ledger generation:** 1989 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.08 | 114.497 | 97.670 | +6.20% | +0.37% | 5.76x | 1.5 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 755.75 | 113.469 | 97.683 | +10.87% | +0.16% | 3.06x | 4.6 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SOL/USD | 73.63 | 95.225 | 80.185 | +3.79% | +0.25% | 2.38x | 2.7 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.97817 | 83.071 | 81.249 | +3.76% | +0.07% | 1.15x | 0.1 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LINK/USD | 9.56486 | 82.920 | 76.307 | +3.20% | -0.08% | 1.70x | 2.2 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05007 | 82.178 | 64.670 | +3.30% | +0.50% | 29.51x | 2.0 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XDG/USD | 0.0582218 | 77.360 | 69.611 | +3.28% | +0.10% | 1.72x | 0.8 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | UNI/USD | 4.9036 | 73.768 | 80.502 | +5.45% | -0.04% | 0.35x | 4.5 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | INJ/USD | 6.527 | 71.843 | 72.968 | +5.41% | +0.26% | 0.76x | 4.6 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ETH/USD | 1731.14 | 71.603 | 72.997 | +2.58% | +0.15% | 0.79x | 0.1 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 11 | VVV/USD | 27.091 | 69.611 | 72.958 | +3.47% | +0.42% | 0.46x | 7.4 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3663.4 | 68.469 | 61.124 | +3.00% | -0.06% | 1.76x | 1.7 | 2026-11-27T09:32:01.569458+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.683 | 755.75 | +0.16% | 3.06x |
| 2 | HYPE/USD | 97.670 | 66.08 | +0.37% | 5.76x |
| 3 | XRP/USD | 81.249 | 0.97817 | +0.07% | 1.15x |
| 4 | UNI/USD | 80.502 | 4.9036 | -0.04% | 0.35x |
| 5 | SOL/USD | 80.185 | 73.63 | +0.25% | 2.38x |
| 6 | LINK/USD | 76.307 | 9.56486 | -0.08% | 1.70x |
| 7 | ETH/USD | 72.997 | 1731.14 | +0.15% | 0.79x |
| 8 | INJ/USD | 72.968 | 6.527 | +0.26% | 0.76x |
| 9 | VVV/USD | 72.958 | 27.091 | +0.42% | 0.46x |
| 10 | XDG/USD | 69.611 | 0.0582218 | +0.10% | 1.72x |
| 11 | NIGHT/USD | 64.670 | 0.05007 | +0.50% | 29.51x |
| 12 | PAXG/USD | 61.124 | 3663.4 | -0.06% | 1.76x |

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

- Persisted scans: 1989; predictions: 17570; observations: 1204520.
- Matured sampled outcomes across 1/6/24/48h: 38945; gap abstentions: 25734. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45974149451 · **Generation:** 1989 · **Legacy run:** 45974149451
**Main quote time:** 2026-11-27T09:32:09.967136+00:00 · **Legacy report time:** 2026-11-27T09:33:03.874959+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.08 | 114.50 | +0.37% | 5.76x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 755.75 | 113.47 | +0.16% | 3.06x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 73.63 | 95.23 | +0.25% | 2.38x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.97817 | 83.07 | +0.07% | 1.15x | STRONG 77/100 | HIGH 62/100 | Watch |
| 5 | LINK/USD | 9.56486 | 82.92 | -0.08% | 1.70x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD ⭐ | 0.05007 | 82.18 | +0.50% | 29.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0582218 | 77.36 | +0.10% | 1.72x | STRONG 84/100 | HIGH 55/100 | Watch |
| 8 | UNI/USD | 4.9036 | 73.77 | -0.04% | 0.35x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 9 | INJ/USD | 6.527 | 71.84 | +0.26% | 0.76x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 10 | ETH/USD | 1731.14 | 71.60 | +0.15% | 0.79x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 11 | VVV/USD | 27.091 | 69.61 | +0.42% | 0.46x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3663.4 | 68.47 | -0.06% | 1.76x | MODERATE 54/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.12 | 100.00 | +0.37% | 5.76x | 16203 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 755.61 | 100.00 | +0.16% | 3.06x | 40684 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 73.55 | 99.69 | +0.25% | 2.38x | 33671 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.97853 | 98.14 | +0.07% | 1.15x | 25752 | STRONG 84/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.05004 | 88.91 | +0.50% | 29.51x | 9367 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XDG/USD ⭐ | 0.0582213 | 88.39 | +0.10% | 1.72x | 6022 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, ZEC/USD, SOL/USD, XRP/USD, NIGHT/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
