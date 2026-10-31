# Independent paper-scanner verification contracts

This is an isolated, read-only verifier for the proposed $0-hosting GitHub
Actions paper scanner. It cannot trade, change production, publish history,
or call Kraken. The tests exercise immutable prediction hash chains,
prediction-as-of ordering, source freshness, stablecoin exclusions, cross-run
nonregression, mature 1/6/24/48-hour outcomes, gap/liquidity abstention,
and checksummed artifacts.

**Not a certification:** A JSON field claiming Kraken source completeness is
not itself independently authenticated provenance. Before any forward outcome
is counted as a genuine label, the primary pipeline must independently
verify source identity, actual interval completeness, real timestamps,
artifacts and observed prices. This suite tests contract enforcement only.
A green CI result is not a scan, a mature label, or predictive lift.

The primary proof-of-value branch may adopt these contracts after review.
Never reset an absent remote history; explicit genesis is allowed only when
the history branch is independently proven not to exist. Require remote
readback after atomic writes and bound Git size.
