"""Fast historical reconstruction contract checks; never downloads the archive."""
import ast
from pathlib import Path

source = Path(__file__).with_name("backfill.py").read_text(encoding="utf-8")
tree = ast.parse(source)

def check(name, ok):
    if not ok:
        raise AssertionError(name)
    print("PASS", name)

early_assignments = [
    node for node in ast.walk(tree)
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "early" for t in node.targets)
]
check("single_early_assignment", len(early_assignments) == 1)
early_expr = ast.Expression(early_assignments[0].value)
early_code = compile(early_expr, "<early-contract>", "eval")
for value, expected in [(None, False), (-4, False), (-3, True), (-0.1, True), (0, True), (0.1, True), (3, True), (4, False)]:
    actual = bool(eval(early_code, {"__builtins__": {}}, {"p60": value}))
    check(f"early_return_{value}", actual is expected)

forward_assignments = [
    node for node in ast.walk(tree)
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "mx" for t in node.targets)
]
check("single_forward_max_assignment", len(forward_assignments) == 1)
forward_code = compile(ast.Expression(forward_assignments[0].value), "<forward-contract>", "eval")
def pct(a, b):
    return (b / a - 1) * 100 if a and b else None
for price, future, expected in [
    (100, [100, 100], 0),
    (100, [99, 100], 0),
    (100, [98, 99], -1),
    (100, [100, 120], 20),
    (100, [100, 0], 0),
    (0, [100], None),
]:
    actual = eval(forward_code, {"__builtins__": {}, "max": max, "pct": pct}, {"c": price, "fwd": future})
    check(f"forward_max_{price}_{future}", actual == expected)

check("complete_24h_required", "bars[i+288][0]-t!=86400" in source)
check("all_forward_candles_contiguous", "bars[j][0]-bars[j-1][0]!=300" in source)
check("contiguous_1h_required", "t-bars[i-12][0]!=3600" in source)
check("all_lookback_candles_contiguous", "range(i-11,i+1)" in source and "bars[j][0]-bars[j-1][0]!=300" in source)
check("dedupe_candle_timestamps", "bar[0]:bar" in source)
check("reject_invalid_candles", "math.isfinite" in source)
check("reject_invalid_trade_counts", "not math.isfinite(tr) or tr<0" in source)
check("forward_clock_bounded", "bar[0]-t<=86400" in source)
check("wall_clock_quarter_hour", "t%900!=0" in source)
check("five_minute_candle_alignment", "t%300!=0" in source)
check("wall_clock_control_sampling", "t%3600==0" in source)
check("archive_has_checksum", "checksum mismatch" in source)
check("five_minute_source", "Kraken_OHLCVT_Full_2026Q2" in source)
check("historical_not_current", "2026,7,1" in source)
print("historical_contracts_passed")
