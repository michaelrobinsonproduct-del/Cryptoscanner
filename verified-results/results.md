# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T10:01:56.711779+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42597704119
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 6820092e845c0c311a65ea3f7ca1a155c9aa1674
**Ledger generation:** 190 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZAMA/USD | 0.06704 | 85.623 | 65.904 | +6.48% | +0.94% | 3.95x | 20.9 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ARB/USD | 0.1759 | 78.229 | 75.675 | +6.03% | -0.06% | 1.28x | 11.4 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | GBP/USD | 1.34158 | 63.154 | 57.953 | +0.45% | +0.05% | 1.50x | 0.4 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.1e-06 | 60.744 | 71.745 | +3.09% | -0.78% | 0.29x | 9.8 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 130.54 | 59.135 | 69.324 | +3.64% | -0.41% | 0.19x | 6.1 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PAXG/USD | 4082.01 | 57.275 | 42.169 | +0.87% | +0.02% | 3.77x | 2.8 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | RENDER/USD | 1.599 | 56.261 | 62.787 | +4.85% | +0.50% | 0.10x | 12.5 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | CAP/USD | 0.101021 | 55.074 | 37.143 | +1.10% | +0.59% | 6.34x | 6.0 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | LTC/USD | 50.92 | 53.769 | 56.461 | +1.70% | +0.02% | 0.72x | 3.9 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | QNT/USD | 199.86 | 52.176 | 59.566 | +2.57% | +0.19% | 0.17x | 7.0 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AVAX/USD | 7.991 | 49.255 | 43.620 | +0.78% | -0.14% | 1.63x | 7.5 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HBAR/USD | 0.06673 | 44.373 | 50.167 | +1.74% | -0.13% | 0.49x | 3.0 | 2026-11-09T10:01:48.932915+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 190; predictions: 1685; observations: 114848.
- Matured sampled outcomes across 1/6/24/48h: 951; gap abstentions: 4632. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
