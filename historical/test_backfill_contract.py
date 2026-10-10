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

check("archive_has_checksum", "checksum mismatch" in source)
check("five_minute_source", "Kraken_OHLCVT_Full_2026Q2" in source)
check("historical_not_current", "2026,7,1" in source)
print("historical_contracts_passed")
