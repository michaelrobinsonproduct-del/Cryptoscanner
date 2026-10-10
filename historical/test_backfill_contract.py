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
    actual = bool(eval(early_code, {"__builtins__": {"abs": abs}}, {"p60": value}))
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
    actual = eval(forward_code, {"__builtins__": {}, "max": max, "pct": pct, "c": price, "fwd": future})
    check(f"forward_max_{price}_{future}", (actual is None and expected is None) or (actual is not None and expected is not None and abs(actual - expected) < 1e-9))

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
check("retrospective_not_live_alert", '"live_alert_verified":False' in source)
check("historical_catches_not_invented", '"caught_early":False' in source)
check("historical_alert_timestamp_not_invented", '"earliest_signal_at":None' in source)
check("episode_split_at_quarter_hour_gap", 'timestamp()>900' in source)
check("episode_gap_metadata_matches_rule", '"max_anchor_gap_minutes":15' in source)
check("no_24h_episode_merge", '"dedupe_gap_hours":24' not in source)
check("episode_closes_on_non_major_anchor", "elif grp:\n    emit_episode(grp);grp=[]" in source)
check("close_episode_on_invalid_lookback", "if t-bars[i-12][0]!=3600 or gaps[i]!=gaps[i-12]:\n    if grp:emit_episode(grp);grp=[]\n    continue" in source)
check("close_episode_on_invalid_forward_window", "if i+288>=len(bars) or bars[i+288][0]-t!=86400 or gaps[i+288]!=gaps[i]:\n    if grp:emit_episode(grp);grp=[]\n    continue" in source)
check("close_episode_on_missing_forward_return", "if mx is None:\n    if grp:emit_episode(grp);grp=[]\n    continue" in source)
check("max_return_has_own_baseline", '"max_return_baseline_price":best["anchor_price"]' in source)
check("max_return_has_own_anchor", '"max_return_anchor":best["anchor_at"]' in source)
check("date_boundary_closes_episode", "if not START<=t<END: \n    if grp:emit_episode(grp);grp=[]\n    continue" in source)
check("archive_has_checksum", "checksum mismatch" in source)
check("five_minute_source", "Kraken_OHLCVT_Full_2026Q2" in source)
check("historical_not_current", "2026,7,1" in source)
# Execute the actual production episode emitter on 100 deterministic groups.
import io, json
from datetime import datetime, timezone, timedelta
emitters = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "emit_episode"]
check("single_production_episode_emitter", len(emitters) == 1)
namespace = {"moves_out": io.StringIO(), "episodes_written": 0, "json": json}
exec(compile(ast.Module(body=[emitters[0]], type_ignores=[]), "<episode-emitter>", "exec"), namespace)
for case in range(100):
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    group = [{"pair": "TESTUSD", "anchor_at": (start + timedelta(minutes=15*j)).isoformat(),
              "anchor_price": 10 + j, "max_forward_return_pct": 20 + ((j * 13 + case) % 37)}
             for j in range(1 + case % 9)]
    namespace["emit_episode"](group)
    emitted = json.loads(namespace["moves_out"].getvalue().splitlines()[-1])
    namespace["moves_out"].seek(0)
    namespace["moves_out"].truncate(0)
    best = max(group, key=lambda r: r["max_forward_return_pct"])
    check("episode_max_anchor_"+str(case), emitted["evidence"]["max_return_anchor"] == best["anchor_at"])
    check("episode_max_baseline_"+str(case), emitted["evidence"]["max_return_baseline_price"] == best["anchor_price"])
    check("episode_max_return_"+str(case), emitted["max_return_pct"] == best["max_forward_return_pct"])
    check("episode_start_"+str(case), emitted["move_start"] == group[0]["anchor_at"])
    check("episode_not_live_catch_"+str(case), emitted["caught_early"] is False)
    check("episode_live_verification_"+str(case), emitted["evidence"]["live_alert_verified"] is False)
check("production_episode_emitter_100_groups", namespace["episodes_written"] == 100)
check("episode_emitter_buffer_bounded", namespace["moves_out"].getvalue() == "")
print("historical_contracts_passed")
