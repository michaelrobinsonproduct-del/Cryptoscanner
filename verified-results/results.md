# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:11:14.915545+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44960390392
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** ed72fff6e3186c0d5af3839aa0101d23f069ca48 (atomic ledger/results publication)
**Ledger generation:** 1199 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7237 | 101.654 | 93.104 | +5.74% | +0.25% | 1.73x | 4.0 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 488.69 | 91.133 | 97.546 | +7.10% | -0.08% | 0.40x | 4.9 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | QNT/USD | 143 | 88.346 | 73.591 | +3.06% | -0.05% | 3.63x | 5.6 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 186.0806 | 86.184 | 74.113 | +3.09% | +0.20% | 2.11x | 5.0 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 783.2 | 83.836 | 76.315 | +3.34% | +0.06% | 1.72x | 4.1 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1679.53 | 82.987 | 80.998 | +3.72% | +0.02% | 1.19x | 0.1 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.9541 | 78.733 | 75.396 | +6.88% | -0.34% | 1.50x | 25.1 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04458 | 77.197 | 81.115 | +5.59% | -0.58% | 0.90x | 11.2 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | XRP/USD | 0.92738 | 72.907 | 68.789 | +2.05% | +0.15% | 1.34x | 1.2 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 70.17 | 72.429 | 69.162 | +2.12% | +0.10% | 1.28x | 1.4 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 61/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 60144.8 | 72.336 | 70.923 | +2.28% | +0.01% | 1.14x | 0.0 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0550411 | 67.432 | 64.763 | +1.41% | +0.12% | 1.21x | 0.2 | 2026-11-21T23:11:06.461200+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.546 | 488.69 | -0.08% | 0.40x |
| 2 | UNI/USD | 93.104 | 4.7237 | +0.25% | 1.73x |
| 3 | NIGHT/USD | 81.115 | 0.04458 | -0.58% | 0.90x |
| 4 | ETH/USD | 80.998 | 1679.53 | +0.02% | 1.19x |
| 5 | ZEC/USD | 76.315 | 783.2 | +0.06% | 1.72x |
| 6 | PEARL/USD | 75.396 | 1.9541 | -0.34% | 1.50x |
| 7 | TAO/USD | 74.113 | 186.0806 | +0.20% | 2.11x |
| 8 | QNT/USD | 73.591 | 143 | -0.05% | 3.63x |
| 9 | XBT/USD | 70.923 | 60144.8 | +0.01% | 1.14x |
| 10 | SOL/USD | 69.162 | 70.17 | +0.10% | 1.28x |
| 11 | XRP/USD | 68.789 | 0.92738 | +0.15% | 1.34x |
| 12 | XDG/USD | 64.763 | 0.0550411 | +0.12% | 1.21x |

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

- Persisted scans: 1199; predictions: 9697; observations: 725351.
- Matured sampled outcomes across 1/6/24/48h: 13013; gap abstentions: 21607. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44960390392 · **Generation:** 1199 · **Legacy run:** 44960390392
**Main quote time:** 2026-11-21T23:11:14.915545+00:00 · **Legacy report time:** 2026-11-21T23:12:20.740152+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7237 | 101.65 | +0.25% | 1.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 488.69 | 91.13 | -0.08% | 0.40x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 3 | QNT/USD | 143 | 88.35 | -0.05% | 3.63x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD ⭐ | 186.0806 | 86.18 | +0.20% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 783.2 | 83.84 | +0.06% | 1.72x | STRONG 87/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD | 1679.53 | 82.99 | +0.02% | 1.19x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 7 | PEARL/USD | 1.9541 | 78.73 | -0.34% | 1.50x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 8 | NIGHT/USD | 0.04458 | 77.20 | -0.58% | 0.90x | WEAK 39/100 | VERY_HIGH 74/100 | Watch |
| 9 | XRP/USD ⭐ | 0.92738 | 72.91 | +0.15% | 1.34x | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD ⭐ | 70.17 | 72.43 | +0.10% | 1.28x | STRONG 71/100 | HIGH 55/100 | Watch |
| 11 | XBT/USD | 60144.8 | 72.34 | +0.01% | 1.14x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 12 | XDG/USD | 0.0550411 | 67.43 | +0.12% | 1.21x | MODERATE 59/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7189 | 94.28 | +0.25% | 1.73x | 10582 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 781.85 | 86.84 | +0.06% | 1.72x | 39744 | STRONG 88/100 | HIGH 55/100 | Watch |
| 3 | TAO/USD ⭐ | 186.04 | 86.08 | +0.20% | 2.11x | 10951 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.92717 | 77.96 | +0.15% | 1.34x | 45566 | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 70.18 | 76.23 | +0.10% | 1.28x | 46733 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD, TAO/USD, ZEC/USD, XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
