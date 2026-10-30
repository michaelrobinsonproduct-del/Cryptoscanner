# Batch 6: Kraken OHLCVT source provenance and safe historical-label gates

Evidence consulted (2026-10-30):
- Kraken official downloadable historical OHLCVT: https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
- Kraken official 2026Q2 version / checksum: https://support.kraken.com/ca/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data

Verified official source statements:
1. CSV fields are `timestamp, open, high, low, close, volume, trades`, without a header.
2. Five-minute candles are included among supported resolutions.
3. Rows are emitted only for intervals containing trades; empty intervals are not zero-filled.
4. The 2026Q2 full archive's published SHA256 is `fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4`.

Unverified: these official pages do NOT explicitly state whether the first CSV timestamp is the **opening** or **closing** boundary of its interval. Do not promote the existing `candle_open_utc` caller assertion into independently verified provenance based on the CSV schema alone. Require separate timestamp-semantic evidence, e.g. matching known trade timestamps to source candle boundaries, and record exact archive identity and selected pair. Historical outcomes remain unverified.

The source states that absent candles represent intervals without trades. Nevertheless, the research reconstruction must abstain on missing intervals: absence of trades is not proof of continuous executable price or of the ability to buy/sell at an imputed price. Never interpolate or forward-fill gaps for hit labeling.

Other gates: `close * base_volume` is only an approximate quote-volume proxy, not executable order-book liquidity. A candle high after observation is not an achievable trade fill. The verified archive is ~8.97 GB and is not available in this invocation. Existing adapter rejects members above 64 MiB or 200,000 rows and may exclude active pairs; these bounds are intentional safety limits, not a reason to weaken them. For real reconstruction use a bounded verified source and choose one specific eligible pair/time window with explicit no-leakage tests.

No historical labels, improvement claims, deployment, production writes, scoring promotion, trading or Railway changes authorized by this evidence.
