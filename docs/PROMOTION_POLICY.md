# Promotion policy

The challenger cannot replace the current production control merely because it deploys successfully.

Required gates:
1. Infrastructure health and freshness tests pass.
2. No regression in market coverage or validation reliability.
3. Prospective shadow sample is sufficient for comparison.
4. Measure recall of eventual +20%, +50%, +100% movers, lead time, false-positive rate, and alerts emitted at <=3%, <=5%, <=10% displacement.
5. Candidate remains early on an independent second refresh.
6. Challenger materially improves the target metrics or resolves a documented reliability defect without degrading mover detection.
7. Release is immutable and previous production remains immediately rollbackable.

No claim of predictive success is made from historical backtests alone.
