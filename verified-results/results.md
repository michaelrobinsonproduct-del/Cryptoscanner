# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T11:52:04.940365+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45993610507
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 81b1bce08d46ac715da53e595176e9beee6f6fdb (atomic ledger/results publication)
**Ledger generation:** 2003 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.59 | 86.941 | 91.392 | +5.42% | -0.73% | 0.92x | 3.0 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 2 | ZEC/USD | 749.64 | 86.135 | 97.669 | +9.97% | -1.18% | 0.44x | 4.7 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0586054 | 85.276 | 74.852 | +3.96% | -0.32% | 2.20x | 0.0 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152591 | 84.624 | 70.426 | +2.78% | -0.16% | 3.08x | 2.7 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | FET/USD | 0.1285 | 72.020 | 72.538 | +6.73% | +0.55% | 0.68x | 15.5 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97456 | 71.695 | 78.568 | +3.37% | -0.24% | 0.43x | 0.1 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ETH/USD | 1719.68 | 66.410 | 68.244 | +1.90% | -0.51% | 1.07x | 0.1 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6862 | 65.256 | 72.938 | +2.77% | -0.32% | 0.39x | 2.9 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 61473 | 65.206 | 66.273 | +1.61% | -0.38% | 1.09x | 0.0 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SOL/USD | 72.96 | 64.450 | 74.247 | +2.85% | -0.60% | 0.32x | 1.4 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | PEPE/USD | 3.623e-06 | 64.278 | 71.871 | +4.17% | -1.01% | 0.75x | 2.8 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 12 | LINK/USD | 9.51386 | 63.408 | 71.634 | +2.65% | -0.41% | 0.38x | 3.8 | 2026-11-27T11:51:56.877231+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.669 | 749.64 | -1.18% | 0.44x |
| 2 | HYPE/USD | 91.392 | 65.59 | -0.73% | 0.92x |
| 3 | XRP/USD | 78.568 | 0.97456 | -0.24% | 0.43x |
| 4 | XDG/USD | 74.852 | 0.0586054 | -0.32% | 2.20x |
| 5 | SOL/USD | 74.247 | 72.96 | -0.60% | 0.32x |
| 6 | SUI/USD | 72.938 | 0.6862 | -0.32% | 0.39x |
| 7 | FET/USD | 72.538 | 0.1285 | +0.55% | 0.68x |
| 8 | PEPE/USD | 71.871 | 3.623e-06 | -1.01% | 0.75x |
| 9 | LINK/USD | 71.634 | 9.51386 | -0.41% | 0.38x |
| 10 | ADA/USD | 70.426 | 0.152591 | -0.16% | 3.08x |
| 11 | ETH/USD | 68.244 | 1719.68 | -0.51% | 1.07x |
| 12 | XBT/USD | 66.273 | 61473 | -0.38% | 1.09x |

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

- Persisted scans: 2003; predictions: 17738; observations: 1212958.
- Matured sampled outcomes across 1/6/24/48h: 39461; gap abstentions: 25815. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45993610507 · **Generation:** 2003 · **Legacy run:** 45993610507
**Main quote time:** 2026-11-27T11:52:04.940365+00:00 · **Legacy report time:** 2026-11-27T11:52:43.150749+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.59 | 86.94 | -0.73% | 0.92x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 2 | ZEC/USD | 749.64 | 86.13 | -1.18% | 0.44x | MODERATE 48/100 | VERY_HIGH 80/100 | Watch |
| 3 | XDG/USD | 0.0586054 | 85.28 | -0.32% | 2.20x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.152591 | 84.62 | -0.16% | 3.08x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | FET/USD | 0.1285 | 72.02 | +0.55% | 0.68x | MODERATE 61/100 | VERY_HIGH 81/100 | Watch |
| 6 | XRP/USD | 0.97456 | 71.69 | -0.24% | 0.43x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | ETH/USD | 1719.68 | 66.41 | -0.51% | 1.07x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | SUI/USD | 0.6862 | 65.26 | -0.32% | 0.39x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 61473 | 65.21 | -0.38% | 1.09x | WEAK 43/100 | HIGH 68/100 | Watch |
| 10 | SOL/USD | 72.96 | 64.45 | -0.60% | 0.32x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | PEPE/USD | 3.623e-06 | 64.28 | -1.01% | 0.75x | WEAK 37/100 | VERY_HIGH 80/100 | Watch |
| 12 | LINK/USD | 9.51386 | 63.41 | -0.41% | 0.38x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
