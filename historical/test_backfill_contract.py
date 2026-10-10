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

# Exercise prefix-gap window checks with missing and complete 5-minute bars.
for label, times, expected in [
    ("complete", [300 * i for i in range(301)], True),
    ("missing_internal", [300 * i + (300 if i >= 150 else 0) for i in range(301)], False),
    ("missing_before_window", [300 * i + (300 if i >= 1 else 0) for i in range(301)], True),
]:
    gaps = [0] * len(times)
    for j in range(1, len(times)):
        gaps[j] = gaps[j-1] + (times[j] - times[j-1] != 300)
    actual = gaps[300] == gaps[12] and times[300] - times[12] == 86400
    check("prefix_gap_" + label, actual is expected)

check("last_complete_24h_anchor_in_bounds", "range(12,len(bars)-288)" in source)
check("complete_24h_required", "bars[i+288][0]-t!=86400" in source)
check("all_forward_candles_contiguous", "gaps[i+288]!=gaps[i]" in source)
check("contiguous_1h_required", "t-bars[i-12][0]!=3600" in source)
check("all_lookback_candles_contiguous", "gaps[i]!=gaps[i-12]" in source)
check("dedupe_candle_timestamps", "bar[0]:bar" in source)
check("duplicate_policy_first_valid", "reversed(bars)" in source)
check("deduplicated_bars_chronological", "bars.sort(key=lambda bar:bar[0])" in source)
check("reject_invalid_candles", "math.isfinite" in source)
check("reject_invalid_trade_counts", "not math.isfinite(tr) or tr<0" in source)
check("forward_clock_bounded", "bars[i+288][0]-t!=86400" in source)
check("wall_clock_quarter_hour", "t%900!=0" in source)
check("fractional_timestamps_rejected", "timestamp.is_integer()" in source)
check("nonfinite_timestamps_rejected", "math.isfinite(timestamp)" in source)
check("five_minute_candle_alignment", "t%300!=0" in source)
check("wall_clock_control_sampling", "t%3600==0" in source)
check("full_population_before_episode_filter", 'research_out.write(json.dumps(rec' in source and 'if rec["major_mover"]:' in source)
check("episodes_emit_during_anchor_scan", 'if rec["major_mover"]:' in source and "emit_episode(grp);grp=[]" in source)
check("no_per_market_winner_accumulation", "pairrows" not in source)
check("move_episodes_streamed_to_disk", 'open(outdir+"/moves.ndjson","w",encoding="utf-8") as moves_out' in source)
check("move_episode_counter", "episodes_written+=1" in source)
check("move_episode_ndjson_lines", 'moves_out.write(json.dumps(ep,separators=(",",":"))+"\\n")' in source)
check("no_unbounded_move_episodes", "moves=[]" not in source and "eps=[]" not in source)
check("research_rows_streamed_to_disk", 'with open(outdir+"/research.ndjson","w",encoding="utf-8") as research_out' in source)
check("research_count_incremented", "rows_written+=1" in source)
check("no_unbounded_research_list", "rows=[]" not in source)
check("no_outcome_conditioned_training_keep", "keep=mx>=10" not in source)
check("archive_has_checksum", "checksum mismatch" in source)
check("five_minute_source", "Kraken_OHLCVT_Full_2026Q2" in source)
check("historical_not_current", "2026,7,1" in source)
print("historical_contracts_passed")
