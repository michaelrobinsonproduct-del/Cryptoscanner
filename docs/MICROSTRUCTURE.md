# Microstructure challenger

The challenger models a stateful two-sided Kraken book plus recent trades and explicitly records latest_trade_at/trade_age_ms. Compact snapshots preserve spread, 1% bid/ask notional, imbalance, trade count and aggressor mix. Consecutive snapshots form trajectory features instead of treating a single book image as predictive evidence.

The hypothesis that strengthening bid depth during seller-heavy executions can precede ignition is experimental. It must earn weight prospectively; it is not an automatic promotion rule.
