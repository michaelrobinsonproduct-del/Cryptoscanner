# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T06:41:52.204422+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45953258792
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a7c70a52398c7135d95a2ea4a4495b434521565c (atomic ledger/results publication)
**Ledger generation:** 1972 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 748.49 | 110.587 | 98.063 | +9.80% | -0.50% | 7.55x | 3.9 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.92 | 102.398 | 95.109 | +5.95% | -0.21% | 1.83x | 3.0 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.153234 | 87.649 | 72.940 | +3.22% | -0.06% | 3.88x | 3.4 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0580047 | 81.163 | 66.088 | +2.89% | +0.01% | 3.40x | 0.0 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LINK/USD | 9.60221 | 78.576 | 78.645 | +3.60% | -0.36% | 1.18x | 3.1 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XBT/USD | 61616.1 | 76.656 | 67.929 | +1.85% | -0.02% | 1.88x | 0.0 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.96882 | 74.277 | 73.790 | +2.77% | -0.07% | 1.08x | 1.1 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 72.89 | 72.182 | 73.556 | +2.75% | -0.10% | 0.91x | 1.4 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ETH/USD | 1731.1 | 70.834 | 72.981 | +2.57% | -0.23% | 0.90x | 0.1 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | W/USD | 0.0096 | 67.509 | 73.125 | +8.97% | -0.10% | 0.49x | 10.4 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | PAXG/USD | 3632.75 | 61.968 | 53.856 | +2.14% | +0.03% | 1.79x | 1.0 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BIGTIME/USD | 0.00638 | 60.512 | 72.125 | +9.64% | -0.72% | 0.20x | 7.8 | 2026-11-27T06:41:43.495023+00:00 | Not calibrated | WEAK 35/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.063 | 748.49 | -0.50% | 7.55x |
| 2 | HYPE/USD | 95.109 | 65.92 | -0.21% | 1.83x |
| 3 | LINK/USD | 78.645 | 9.60221 | -0.36% | 1.18x |
| 4 | XRP/USD | 73.790 | 0.96882 | -0.07% | 1.08x |
| 5 | SOL/USD | 73.556 | 72.89 | -0.10% | 0.91x |
| 6 | W/USD | 73.125 | 0.0096 | -0.10% | 0.49x |
| 7 | ETH/USD | 72.981 | 1731.1 | -0.23% | 0.90x |
| 8 | ADA/USD | 72.940 | 0.153234 | -0.06% | 3.88x |
| 9 | BIGTIME/USD | 72.125 | 0.00638 | -0.72% | 0.20x |
| 10 | XBT/USD | 67.929 | 61616.1 | -0.02% | 1.88x |
| 11 | XDG/USD | 66.088 | 0.0580047 | +0.01% | 3.40x |
| 12 | PAXG/USD | 53.856 | 3632.75 | +0.03% | 1.79x |

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

- Persisted scans: 1972; predictions: 17366; observations: 1194269.
- Matured sampled outcomes across 1/6/24/48h: 38358; gap abstentions: 25583. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45953258792 · **Generation:** 1972 · **Legacy run:** 45953258792
**Main quote time:** 2026-11-27T06:41:52.204422+00:00 · **Legacy report time:** 2026-11-27T06:42:44.886956+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 748.49 | 110.59 | -0.50% | 7.55x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 65.92 | 102.40 | -0.21% | 1.83x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD | 0.153234 | 87.65 | -0.06% | 3.88x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | XDG/USD | 0.0580047 | 81.16 | +0.01% | 3.40x | STRONG 86/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD | 9.60221 | 78.58 | -0.36% | 1.18x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 6 | XBT/USD | 61616.1 | 76.66 | -0.02% | 1.88x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.96882 | 74.28 | -0.07% | 1.08x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 72.89 | 72.18 | -0.10% | 0.91x | WEAK 41/100 | HIGH 68/100 | Watch |
| 9 | ETH/USD | 1731.1 | 70.83 | -0.23% | 0.90x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | W/USD | 0.0096 | 67.51 | -0.10% | 0.49x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 11 | PAXG/USD | 3632.75 | 61.97 | +0.03% | 1.79x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 12 | BIGTIME/USD | 0.00638 | 60.51 | -0.72% | 0.20x | WEAK 35/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05029 | 81.70 | +0.72% | 1.60x | 9002 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
