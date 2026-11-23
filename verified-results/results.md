# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T03:31:28.689377+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45106289979
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 24c63ae659189f83441a57d4b3faa009b9349d6b (atomic ledger/results publication)
**Ledger generation:** 1375 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 71.35 | 78.620 | 61.435 | +1.02% | +0.44% | 2.67x | 1.4 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XBT/USD | 61415.3 | 75.326 | 57.798 | +0.40% | +0.51% | 4.48x | 0.0 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1730.46 | 75.203 | 57.182 | +0.51% | +0.60% | 3.87x | 2.8 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.93249 | 73.406 | 57.985 | +0.53% | +0.85% | 2.12x | 1.5 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 3.0185 | 72.869 | 59.992 | +1.23% | +1.15% | 1.71x | 7.3 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | VVV/USD | 26.615 | 72.774 | 50.793 | +0.29% | +1.40% | 5.83x | 8.3 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | UNI/USD | 4.7489 | 67.610 | 49.428 | +1.45% | +0.64% | 5.63x | 6.1 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XMR/USD | 498.07 | 64.933 | 60.981 | +0.88% | +0.41% | 1.19x | 0.4 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04956 | 64.672 | 49.957 | +0.79% | +1.64% | 1.65x | 12.1 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LINK/USD | 8.87488 | 60.917 | 45.122 | +0.72% | +0.37% | 2.39x | 5.9 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 11 | CC/USD | 0.07524 | 55.079 | 51.717 | +2.69% | +0.67% | 1.00x | 4.0 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 12 | PENGU/USD | 0.004282 | 50.660 | 32.485 | +0.42% | +0.63% | 4.09x | 4.7 | 2026-11-23T03:31:21.000464+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 61.435 | 71.35 | +0.44% | 2.67x |
| 2 | XMR/USD | 60.981 | 498.07 | +0.41% | 1.19x |
| 3 | NEAR/USD | 59.992 | 3.0185 | +1.15% | 1.71x |
| 4 | XRP/USD | 57.985 | 0.93249 | +0.85% | 2.12x |
| 5 | XBT/USD | 57.798 | 61415.3 | +0.51% | 4.48x |
| 6 | ETH/USD | 57.182 | 1730.46 | +0.60% | 3.87x |
| 7 | CC/USD | 51.717 | 0.07524 | +0.67% | 1.00x |
| 8 | VVV/USD | 50.793 | 26.615 | +1.40% | 5.83x |
| 9 | NIGHT/USD | 49.957 | 0.04956 | +1.64% | 1.65x |
| 10 | UNI/USD | 49.428 | 4.7489 | +0.64% | 5.63x |
| 11 | LINK/USD | 45.122 | 8.87488 | +0.37% | 2.39x |
| 12 | PENGU/USD | 32.485 | 0.004282 | +0.63% | 4.09x |

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

- Persisted scans: 1375; predictions: 11267; observations: 832480.
- Matured sampled outcomes across 1/6/24/48h: 18160; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 90 (sampled only; not a success-rate estimate).
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

**Writer:** 45106289979 · **Generation:** 1375 · **Legacy run:** 45106289979
**Main quote time:** 2026-11-23T03:31:28.689377+00:00 · **Legacy report time:** 2026-11-23T03:32:37.826438+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 71.35 | 78.62 | +0.44% | 2.67x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 61415.3 | 75.33 | +0.51% | 4.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1730.46 | 75.20 | +0.60% | 3.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.93249 | 73.41 | +0.85% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.0185 | 72.87 | +1.15% | 1.71x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD | 26.615 | 72.77 | +1.40% | 5.83x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 7 | UNI/USD ⭐ | 4.7489 | 67.61 | +0.64% | 5.63x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 8 | XMR/USD ⭐ | 498.07 | 64.93 | +0.41% | 1.19x | STRONG 77/100 | HIGH 62/100 | Watch |
| 9 | NIGHT/USD | 0.04956 | 64.67 | +1.64% | 1.65x | STRONG 72/100 | HIGH 61/100 | Watch |
| 10 | LINK/USD | 8.87488 | 60.92 | +0.37% | 2.39x | STRONG 85/100 | HIGH 55/100 | Watch |
| 11 | CC/USD ⭐ | 0.07524 | 55.08 | +0.67% | 1.00x | STRONG 73/100 | HIGH 67/100 | Watch |
| 12 | PENGU/USD | 0.004282 | 50.66 | +0.63% | 4.09x | STRONG 80/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.017637 | 86.07 | +5.06% | 1.67x | 5726 | STRONG 73/100 | VERY_HIGH 77/100 | Watch |
| 2 | JUP/USD | 0.23289 | 78.30 | +2.68% | 1.41x | 2718 | STRONG 79/100 | HIGH 66/100 | Watch |
| 3 | SOL/USD ⭐ | 71.35 | 69.40 | +0.44% | 2.67x | 29677 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 61389.9 | 65.80 | +0.51% | 4.48x | 137134 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1728.73 | 64.35 | +0.60% | 3.87x | 43872 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.93322 | 63.80 | +0.85% | 2.12x | 20127 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 7 | CC/USD ⭐ | 0.07547 | 62.99 | +0.67% | 1.00x | 3795 | STRONG 76/100 | HIGH 67/100 | Watch |
| 8 | CAP/USD | 0.095799 | 62.90 | +1.01% | 8.77x | 4598 | STRONG 76/100 | VERY_HIGH 72/100 | Watch |
| 9 | UNI/USD ⭐ | 4.7586 | 60.29 | +0.64% | 5.63x | 4821 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 10 | NEAR/USD ⭐ | 3.0155 | 59.97 | +1.15% | 1.71x | 13037 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 11 | XMR/USD ⭐ | 499 | 59.22 | +0.41% | 1.19x | 8286 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SOL/USD, XBT/USD, ETH/USD, XRP/USD, NEAR/USD, UNI/USD, XMR/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
