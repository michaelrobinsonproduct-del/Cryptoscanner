# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:22:56.437833+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46144086985
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8631375de54dfccada336042451e0bb7aca78b98 (atomic ledger/results publication)
**Ledger generation:** 2153 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 439.6 | 107.029 | 88.835 | +7.94% | +0.99% | 2.32x | 22.3 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | STRONG 95/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 27.171 | 96.164 | 77.898 | +5.52% | +0.65% | 2.61x | 8.9 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.05431 | 91.794 | 93.771 | +8.10% | -0.09% | 0.85x | 9.2 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004448 | 56.802 | 72.060 | +6.46% | -1.49% | 0.22x | 9.0 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | WEAK 33/100 | EXTREME 92/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024654 | 56.680 | 55.149 | +3.96% | +0.48% | 0.91x | 8.1 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | AKE/USD | 0.00112533 | 36.772 | 45.537 | +3.57% | -0.20% | 0.23x | 31.3 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | WEAK 13/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.07457 | 35.296 | 34.469 | +0.57% | +0.09% | 1.04x | 6.7 | 2026-11-28T12:22:52.821330+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.771 | 0.05431 | -0.09% | 0.85x |
| 2 | XMR/USD | 88.835 | 439.6 | +0.99% | 2.32x |
| 3 | VVV/USD | 77.898 | 27.171 | +0.65% | 2.61x |
| 4 | SPACE/USD | 72.060 | 0.004448 | -1.49% | 0.22x |
| 5 | SENT/USD | 55.149 | 0.024654 | +0.48% | 0.91x |
| 6 | AKE/USD | 45.537 | 0.00112533 | -0.20% | 0.23x |
| 7 | CC/USD | 34.469 | 0.07457 | +0.09% | 1.04x |

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

- Persisted scans: 2153; predictions: 19194; observations: 1303764.
- Matured sampled outcomes across 1/6/24/48h: 45817; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46144086985 · **Generation:** 2153 · **Legacy run:** 46144086985
**Main quote time:** 2026-11-28T12:22:56.437833+00:00 · **Legacy report time:** 2026-11-28T12:23:53.901572+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 439.6 | 107.03 | +0.99% | 2.32x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 27.171 | 96.16 | +0.65% | 2.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD | 0.05431 | 91.79 | -0.09% | 0.85x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | SPACE/USD | 0.004448 | 56.80 | -1.49% | 0.22x | WEAK 33/100 | EXTREME 92/100 | Do nothing |
| 5 | SENT/USD | 0.024654 | 56.68 | +0.48% | 0.91x | MODERATE 58/100 | VERY_HIGH 74/100 | Watch |
| 6 | AKE/USD | 0.00112533 | 36.77 | -0.20% | 0.23x | WEAK 13/100 | EXTREME 93/100 | Do nothing |
| 7 | CC/USD ⭐ | 0.07457 | 35.30 | +0.09% | 1.04x | MODERATE 53/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 440.25 | 93.27 | +0.99% | 2.32x | 17389 | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 27.171 | 86.58 | +0.65% | 2.61x | 7611 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07459 | 38.82 | +0.09% | 1.04x | 4656 | MODERATE 54/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
