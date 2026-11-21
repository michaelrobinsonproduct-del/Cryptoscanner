# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T20:51:09.807692+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44948310117
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** a067b008ec526d2e832489f3b3f49e240ac0a785 (atomic ledger/results publication)
**Ledger generation:** 1184 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 488.81 | 99.100 | 97.239 | +7.13% | -0.00% | 1.19x | 5.5 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | MODERATE 60/100 | HIGH 68/100 | Watch | WATCH |
| 2 | QNT/USD | 142.66 | 89.553 | 71.166 | +2.81% | +0.68% | 6.44x | 7.0 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 791.06 | 87.274 | 84.479 | +4.37% | -0.25% | 1.41x | 2.3 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.93211 | 86.317 | 72.704 | +2.58% | -0.28% | 2.61x | 0.6 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | TAO/USD | 184.888 | 84.014 | 69.316 | +2.43% | -0.06% | 4.39x | 5.3 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 6 | UNI/USD | 4.6885 | 83.423 | 87.333 | +4.95% | -0.11% | 0.66x | 4.7 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XLM/USD | 0.129306 | 80.669 | 66.545 | +1.65% | -0.18% | 3.20x | 0.1 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04501 | 78.423 | 86.964 | +6.61% | -0.66% | 0.48x | 13.3 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0550766 | 75.544 | 65.103 | +1.48% | -0.13% | 2.11x | 0.5 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ETH/USD | 1681.3 | 74.769 | 81.763 | +3.83% | -0.13% | 0.36x | 0.1 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 60263.1 | 72.121 | 72.332 | +2.48% | -0.16% | 1.06x | 0.0 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SOL/USD | 70.32 | 65.379 | 70.691 | +2.34% | -0.27% | 0.60x | 1.4 | 2026-11-21T20:51:03.067090+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.239 | 488.81 | -0.00% | 1.19x |
| 2 | UNI/USD | 87.333 | 4.6885 | -0.11% | 0.66x |
| 3 | NIGHT/USD | 86.964 | 0.04501 | -0.66% | 0.48x |
| 4 | ZEC/USD | 84.479 | 791.06 | -0.25% | 1.41x |
| 5 | ETH/USD | 81.763 | 1681.3 | -0.13% | 0.36x |
| 6 | XRP/USD | 72.704 | 0.93211 | -0.28% | 2.61x |
| 7 | XBT/USD | 72.332 | 60263.1 | -0.16% | 1.06x |
| 8 | QNT/USD | 71.166 | 142.66 | +0.68% | 6.44x |
| 9 | SOL/USD | 70.691 | 70.32 | -0.27% | 0.60x |
| 10 | TAO/USD | 69.316 | 184.888 | -0.06% | 4.39x |
| 11 | XLM/USD | 66.545 | 0.129306 | -0.18% | 3.20x |
| 12 | XDG/USD | 65.103 | 0.0550766 | -0.13% | 2.11x |

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

- Persisted scans: 1184; predictions: 9517; observations: 716231.
- Matured sampled outcomes across 1/6/24/48h: 12676; gap abstentions: 21388. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44948310117 · **Generation:** 1184 · **Legacy run:** 44948310117
**Main quote time:** 2026-11-21T20:51:09.807692+00:00 · **Legacy report time:** 2026-11-21T20:52:13.644766+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 488.81 | 99.10 | -0.00% | 1.19x | MODERATE 60/100 | HIGH 68/100 | Watch |
| 2 | QNT/USD ⭐ | 142.66 | 89.55 | +0.68% | 6.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 791.06 | 87.27 | -0.25% | 1.41x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.93211 | 86.32 | -0.28% | 2.61x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | TAO/USD | 184.888 | 84.01 | -0.06% | 4.39x | STRONG 72/100 | HIGH 61/100 | Watch |
| 6 | UNI/USD | 4.6885 | 83.42 | -0.11% | 0.66x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 7 | XLM/USD | 0.129306 | 80.67 | -0.18% | 3.20x | STRONG 70/100 | HIGH 61/100 | Watch |
| 8 | NIGHT/USD | 0.04501 | 78.42 | -0.66% | 0.48x | WEAK 39/100 | VERY_HIGH 82/100 | Watch |
| 9 | XDG/USD | 0.0550766 | 75.54 | -0.13% | 2.11x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 10 | ETH/USD | 1681.3 | 74.77 | -0.13% | 0.36x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 60263.1 | 72.12 | -0.16% | 1.06x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 12 | SOL/USD | 70.32 | 65.38 | -0.27% | 0.60x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 142.78 | 81.80 | +0.68% | 6.44x | 11214 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
