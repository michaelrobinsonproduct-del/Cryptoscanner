# Batch 8: actual source-evidence availability and strict stop gate

Verified on 2026-10-30:
- Research starting checkpoint: `18152c1155e464a45d0722ef5fa1bb786ac92f8a`.
- Exact research CI baseline: run `41145081769`, 75/75 **offline fixture** tests passed.
- Previously acquired Kraken 2026Q2 full-archive inventory: run `40814726443`, artifact `12871991601`, name `kraken-verified-5m-inventory`, digest `sha256:0f7477287adbaa2b2feb9b91734260a6c1d8ac84c2948d149760d6eda08532f1`, 43,190 bytes, not expired, expires 2026-11-05T03:59:07Z. This is an inventory manifest, NOT the 8.97GB source ZIP and NOT independent time-and-sales evidence.
- Expected original full-archive SHA256 `fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4`.
- GitHub Actions manual reconstruction workflow still runs offline fixtures only. It does NOT acquire the Kraken archive or independently sourced trades, and therefore cannot establish real historical forward labels.
- No verified, independently sourced **complete** trade set was available to match a real 5-minute OHLCVT archive member. `verify_open_boundary` requires every trade, with exact count, OHLC and base volume match; an arbitrary trade sample is insufficient.
- No full verified archive bytes available to this invocation. Real 1/6/24/48h labels **not produced**.

## Safety decision

Stop before claiming verified candle-open semantics or reconstructing historical outcomes. Preserve no-trade gap abstention, entry-only quote-volume proxy caveat, and 1/6/24/48h strict maturity/leakage checks. Do not manufacture sample results or loosen archive digest and trade completeness gates.

## Concrete next isolated execution

1. Obtain a bounded independent Kraken trade dataset with source URL, capture time, pair, full interval completeness, and integrity evidence. Do not derive trades from the OHLC candles being validated.
2. Acquire and SHA256-check original 2026Q2 archive on a disposable GitHub runner using existing bounded resource/time/cleanup gates; select a small eligible 5m member and time window.
3. Match real trade aggregates to the archived candle, including timestamp boundary, open/high/low/close, base volume and count. If mismatch or completeness unknown, stop.
4. Only then reconstruct actual 1/6/24/48h labels, abstaining on gaps, liquidity failures and immature horizons. Publish a bounded provenance-rich JSON artifact, no production writes.
5. Run exact-commit offline tests and inspect actual CI logs before claiming success.

No deployment, restart, Railway changes, production writes, trading, scoring promotion, or gate weakening.
