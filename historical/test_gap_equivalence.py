"""Deterministic equivalence tests for optimized historical continuity windows."""
import random

rng = random.Random(20261010)
checked = 0
for trial in range(100):
    n = rng.randint(301, 1200)
    times = [0]
    for _ in range(1, n):
        times.append(times[-1] + (600 if rng.random() < 0.025 else 300))
    gaps = [0] * n
    for j in range(1, n):
        gaps[j] = gaps[j - 1] + (times[j] - times[j - 1] != 300)
    for i in range(12, n - 288):
        original_lookback = (
            times[i] - times[i - 12] == 3600
            and all(times[j] - times[j - 1] == 300 for j in range(i - 11, i + 1))
        )
        indexed_lookback = times[i] - times[i - 12] == 3600 and gaps[i] == gaps[i - 12]
        original_forward = (
            times[i + 288] - times[i] == 86400
            and all(times[j] - times[j - 1] == 300 for j in range(i + 1, i + 289))
        )
        indexed_forward = times[i + 288] - times[i] == 86400 and gaps[i + 288] == gaps[i]
        assert (original_lookback, original_forward) == (indexed_lookback, indexed_forward), (trial, i)
        checked += 1

assert checked > 40000
# Boundary contract: final eligible anchor must leave 288 future bars in bounds.
for n in range(301, 401):
    indices = list(range(12, n - 288))
    assert all(i + 288 < n for i in indices), n
    assert indices[-1] == n - 289, n
print(f"PASS 100 synthetic candle sequences, {checked} anchors")
