# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T23:02:21.768194+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46079884510
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dc10922b756bcbf87af3dc3a89538c66c615aa1a (atomic ledger/results publication)
**Ledger generation:** 2072 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 730.96 | 97.796 | 98.152 | +7.23% | +0.29% | 0.82x | 3.7 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 2 | LTC/USD | 44.61 | 77.635 | 67.802 | +1.99% | +0.27% | 1.85x | 2.2 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.0575909 | 76.818 | 70.095 | +2.16% | +0.21% | 1.57x | 0.0 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | UNI/USD | 4.826 | 73.816 | 76.154 | +3.78% | +0.07% | 0.73x | 4.1 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05012 | 68.941 | 77.832 | +3.40% | -0.10% | 0.16x | 2.0 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.79 | 62.886 | 71.879 | +2.52% | +0.13% | 0.04x | 1.6 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SPACE/USD | 0.004147 | 61.367 | 70.977 | +7.10% | -0.12% | 0.10x | 9.6 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | PAXG/USD | 3650.04 | 60.158 | 62.304 | +2.62% | +0.02% | 0.78x | 1.0 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94619 | 55.781 | 57.501 | +0.36% | +0.12% | 0.77x | 0.1 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 71.65 | 53.319 | 61.308 | +1.00% | -0.06% | 0.23x | 1.4 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | PEPE/USD | 3.543e-06 | 52.357 | 57.039 | +1.87% | +0.17% | 0.45x | 2.8 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.33743 | 51.203 | 58.707 | +0.74% | +0.33% | 0.08x | 3.0 | 2026-11-27T23:02:13.112888+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.152 | 730.96 | +0.29% | 0.82x |
| 2 | NIGHT/USD | 77.832 | 0.05012 | -0.10% | 0.16x |
| 3 | UNI/USD | 76.154 | 4.826 | +0.07% | 0.73x |
| 4 | HYPE/USD | 71.879 | 63.79 | +0.13% | 0.04x |
| 5 | SPACE/USD | 70.977 | 0.004147 | -0.12% | 0.10x |
| 6 | XDG/USD | 70.095 | 0.0575909 | +0.21% | 1.57x |
| 7 | LTC/USD | 67.802 | 44.61 | +0.27% | 1.85x |
| 8 | PAXG/USD | 62.304 | 3650.04 | +0.02% | 0.78x |
| 9 | SOL/USD | 61.308 | 71.65 | -0.06% | 0.23x |
| 10 | LINK/USD | 58.707 | 9.33743 | +0.33% | 0.08x |
| 11 | XRP/USD | 57.501 | 0.94619 | +0.12% | 0.77x |
| 12 | PEPE/USD | 57.039 | 3.543e-06 | +0.17% | 0.45x |

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

- Persisted scans: 2072; predictions: 18566; observations: 1254680.
- Matured sampled outcomes across 1/6/24/48h: 42335; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46079884510 · **Generation:** 2072 · **Legacy run:** 46079884510
**Main quote time:** 2026-11-27T23:02:21.768194+00:00 · **Legacy report time:** 2026-11-27T23:03:08.719048+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 730.96 | 97.80 | +0.29% | 0.82x | STRONG 79/100 | HIGH 62/100 | Watch |
| 2 | LTC/USD ⭐ | 44.61 | 77.64 | +0.27% | 1.85x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0575909 | 76.82 | +0.21% | 1.57x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | UNI/USD | 4.826 | 73.82 | +0.07% | 0.73x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | NIGHT/USD | 0.05012 | 68.94 | -0.10% | 0.16x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 63.79 | 62.89 | +0.13% | 0.04x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | SPACE/USD | 0.004147 | 61.37 | -0.12% | 0.10x | WEAK 36/100 | EXTREME 88/100 | Do nothing |
| 8 | PAXG/USD | 3650.04 | 60.16 | +0.02% | 0.78x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | XRP/USD | 0.94619 | 55.78 | +0.12% | 0.77x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD | 71.65 | 53.32 | -0.06% | 0.23x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | PEPE/USD | 3.543e-06 | 52.36 | +0.17% | 0.45x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.33743 | 51.20 | +0.33% | 0.08x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.057538 | 79.53 | +0.21% | 1.57x | 13327 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD | 0.05188 | 77.36 | +0.42% | 1.19x | 9393 | MODERATE 69/100 | HIGH 68/100 | Watch |
| 3 | LTC/USD ⭐ | 44.57 | 74.49 | +0.27% | 1.85x | 15345 | STRONG 92/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** LTC/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
