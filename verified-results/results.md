# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T10:01:14.357398+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45010193834
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 3fdb1a573c3bfa0e19d6cc2681f0dc88f603c8c5 (atomic ledger/results publication)
**Ledger generation:** 1267 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 192.1501 | 88.059 | 75.668 | +3.46% | +1.06% | 1.71x | 7.1 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.6578 | 87.728 | 65.594 | +1.62% | +1.43% | 3.80x | 1.5 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 797.12 | 86.815 | 68.468 | +2.44% | +1.04% | 2.32x | 7.2 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1708.53 | 86.683 | 64.928 | +1.56% | +1.35% | 6.77x | 2.0 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 60790.8 | 84.487 | 61.972 | +1.17% | +1.50% | 4.33x | 2.4 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | PUMP/USD | 0.002437 | 84.215 | 61.749 | +3.97% | +1.49% | 3.36x | 16.4 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 7 | PEARL/USD | 2.0291 | 83.764 | 70.408 | +4.15% | +2.17% | 1.25x | 2.5 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 8 | HYPE/USD | 61.91 | 81.089 | 61.043 | +1.09% | +1.01% | 4.38x | 3.2 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | NEAR/USD | 2.9388 | 77.890 | 64.837 | +1.82% | +1.49% | 1.56x | 5.8 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | XDG/USD | 0.055346 | 75.121 | 53.489 | +0.30% | +1.33% | 14.82x | 0.8 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | BNB/USD | 552.94 | 66.278 | 45.567 | +1.01% | +1.14% | 6.57x | 1.8 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SOL/USD | 70.38 | 65.948 | 55.674 | +0.30% | +1.06% | 1.50x | 2.8 | 2026-11-22T10:01:06.255844+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 75.668 | 192.1501 | +1.06% | 1.71x |
| 2 | PEARL/USD | 70.408 | 2.0291 | +2.17% | 1.25x |
| 3 | ZEC/USD | 68.468 | 797.12 | +1.04% | 2.32x |
| 4 | SUI/USD | 65.594 | 0.6578 | +1.43% | 3.80x |
| 5 | ETH/USD | 64.928 | 1708.53 | +1.35% | 6.77x |
| 6 | NEAR/USD | 64.837 | 2.9388 | +1.49% | 1.56x |
| 7 | XBT/USD | 61.972 | 60790.8 | +1.50% | 4.33x |
| 8 | PUMP/USD | 61.749 | 0.002437 | +1.49% | 3.36x |
| 9 | HYPE/USD | 61.043 | 61.91 | +1.01% | 4.38x |
| 10 | SOL/USD | 55.674 | 70.38 | +1.06% | 1.50x |
| 11 | XDG/USD | 53.489 | 0.055346 | +1.33% | 14.82x |
| 12 | BNB/USD | 45.567 | 552.94 | +1.14% | 6.57x |

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

- Persisted scans: 1267; predictions: 10124; observations: 766712.
- Matured sampled outcomes across 1/6/24/48h: 14565; gap abstentions: 22176. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45010193834 · **Generation:** 1267 · **Legacy run:** 45010193834
**Main quote time:** 2026-11-22T10:01:14.357398+00:00 · **Legacy report time:** 2026-11-22T10:02:19.592600+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 192.1501 | 88.06 | +1.06% | 1.71x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6578 | 87.73 | +1.43% | 3.80x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 797.12 | 86.81 | +1.04% | 2.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1708.53 | 86.68 | +1.35% | 6.77x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD ⭐ | 60790.8 | 84.49 | +1.50% | 4.33x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | PUMP/USD ⭐ | 0.002437 | 84.21 | +1.49% | 3.36x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 7 | PEARL/USD ⭐ | 2.0291 | 83.76 | +2.17% | 1.25x | STRONG 87/100 | HIGH 55/100 | Watch |
| 8 | HYPE/USD | 61.91 | 81.09 | +1.01% | 4.38x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 9 | NEAR/USD ⭐ | 2.9388 | 77.89 | +1.49% | 1.56x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 10 | XDG/USD | 0.055346 | 75.12 | +1.33% | 14.82x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 11 | BNB/USD | 552.94 | 66.28 | +1.14% | 6.57x | STRONG 88/100 | HIGH 55/100 | Watch |
| 12 | SOL/USD | 70.38 | 65.95 | +1.06% | 1.50x | STRONG 78/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.0291 | 95.14 | +2.17% | 1.25x | 8282 | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002436 | 88.89 | +1.49% | 3.36x | 4607 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | ICNT/USD | 0.3615 | 84.43 | +1.44% | 5.45x | 3095 | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 191.8784 | 82.75 | +1.06% | 1.71x | 7296 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1708.06 | 82.33 | +1.35% | 6.77x | 45887 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6579 | 80.89 | +1.43% | 3.80x | 7635 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD ⭐ | 60741.6 | 77.49 | +1.50% | 4.33x | 144013 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | ZEC/USD ⭐ | 796 | 77.32 | +1.04% | 2.32x | 27809 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | NEAR/USD ⭐ | 2.9417 | 66.75 | +1.49% | 1.56x | 12606 | STRONG 83/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** TAO/USD, SUI/USD, ZEC/USD, ETH/USD, XBT/USD, PUMP/USD, PEARL/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
