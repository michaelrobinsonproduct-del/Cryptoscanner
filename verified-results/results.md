# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T02:31:12.985293+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45928633538
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 57c98d13c092240ab82433b1985c7d8f2b0b43e2 (atomic ledger/results publication)
**Ledger generation:** 1946 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.77 | 119.054 | 90.180 | +9.40% | +2.77% | 17.35x | 19.6 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 64.73 | 104.394 | 81.693 | +4.03% | +1.54% | 64.68x | 3.1 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.8697 | 93.439 | 69.667 | +4.72% | +1.75% | 7.02x | 10.7 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 97/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | NEAR/USD | 3.1412 | 91.191 | 71.170 | +3.06% | +1.00% | 9.03x | 10.5 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 96/100 | HIGH 61/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1727.92 | 89.142 | 70.851 | +2.38% | +0.66% | 26.48x | 1.7 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 72.62 | 88.664 | 70.889 | +2.37% | +0.56% | 9.61x | 1.4 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | LINK/USD | 9.51589 | 88.201 | 69.950 | +2.67% | +0.65% | 91.64x | 7.5 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XBT/USD | 61594.7 | 84.866 | 67.681 | +1.81% | +0.44% | 6.69x | 0.0 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.96181 | 84.684 | 66.968 | +2.02% | +0.54% | 13.00x | 4.4 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | VVV/USD | 26.845 | 84.130 | 65.604 | +2.53% | +0.71% | 4.07x | 14.2 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 11 | LTC/USD | 44.57 | 81.245 | 65.457 | +1.90% | +0.16% | 4.53x | 4.5 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XMR/USD | 468.88 | 76.071 | 66.984 | +2.61% | -0.06% | 1.94x | 12.6 | 2026-11-27T02:31:06.214767+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 90.180 | 745.77 | +2.77% | 17.35x |
| 2 | HYPE/USD | 81.693 | 64.73 | +1.54% | 64.68x |
| 3 | NEAR/USD | 71.170 | 3.1412 | +1.00% | 9.03x |
| 4 | SOL/USD | 70.889 | 72.62 | +0.56% | 9.61x |
| 5 | ETH/USD | 70.851 | 1727.92 | +0.66% | 26.48x |
| 6 | LINK/USD | 69.950 | 9.51589 | +0.65% | 91.64x |
| 7 | UNI/USD | 69.667 | 4.8697 | +1.75% | 7.02x |
| 8 | XBT/USD | 67.681 | 61594.7 | +0.44% | 6.69x |
| 9 | XMR/USD | 66.984 | 468.88 | -0.06% | 1.94x |
| 10 | XRP/USD | 66.968 | 0.96181 | +0.54% | 13.00x |
| 11 | VVV/USD | 65.604 | 26.845 | +0.71% | 4.07x |
| 12 | LTC/USD | 65.457 | 44.57 | +0.16% | 4.53x |

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

- Persisted scans: 1946; predictions: 17054; observations: 1178631.
- Matured sampled outcomes across 1/6/24/48h: 37430; gap abstentions: 25463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45928633538 · **Generation:** 1946 · **Legacy run:** 45928633538
**Main quote time:** 2026-11-27T02:31:12.985293+00:00 · **Legacy report time:** 2026-11-27T02:31:56.400620+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 745.77 | 119.05 | +2.77% | 17.35x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.73 | 104.39 | +1.54% | 64.68x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.8697 | 93.44 | +1.75% | 7.02x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.1412 | 91.19 | +1.00% | 9.03x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1727.92 | 89.14 | +0.66% | 26.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD ⭐ | 72.62 | 88.66 | +0.56% | 9.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | LINK/USD ⭐ | 9.51589 | 88.20 | +0.65% | 91.64x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XBT/USD ⭐ | 61594.7 | 84.87 | +0.44% | 6.69x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.96181 | 84.68 | +0.54% | 13.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | VVV/USD | 26.845 | 84.13 | +0.71% | 4.07x | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 11 | LTC/USD ⭐ | 44.57 | 81.25 | +0.16% | 4.53x | STRONG 96/100 | HIGH 55/100 | Watch |
| 12 | XMR/USD | 468.88 | 76.07 | -0.06% | 1.94x | MODERATE 53/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.63 | 100.00 | +1.54% | 64.68x | 13529 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 741.09 | 100.00 | +2.77% | 17.35x | 36594 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.8588 | 90.42 | +1.75% | 7.02x | 6353 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.1354 | 89.81 | +1.00% | 9.03x | 13761 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 72.54 | 85.97 | +0.56% | 9.61x | 33627 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | ETH/USD ⭐ | 1726.13 | 84.56 | +0.66% | 26.48x | 30874 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | AKE/USD | 0.0015898 | 84.40 | +2.62% | 1.47x | 8156 | STRONG 72/100 | VERY_HIGH 77/100 | Watch |
| 8 | XBT/USD ⭐ | 61531.2 | 81.77 | +0.44% | 6.69x | 132712 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.96004 | 81.56 | +0.54% | 13.00x | 20885 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | LINK/USD ⭐ | 9.50741 | 81.53 | +0.65% | 91.64x | 7034 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | PEPE/USD | 3.587e-06 | 79.64 | +0.76% | 5.71x | 5329 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 12 | LTC/USD ⭐ | 44.53 | 77.29 | +0.16% | 4.53x | 14254 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, HYPE/USD, UNI/USD, NEAR/USD, ETH/USD, SOL/USD, LINK/USD, XBT/USD, XRP/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
