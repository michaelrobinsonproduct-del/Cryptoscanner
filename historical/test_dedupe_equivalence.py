"""Exercise the actual backfill duplicate-candle algorithm on 100 seeded inputs."""
import ast
import random
from pathlib import Path

tree = ast.parse(Path(__file__).with_name("backfill.py").read_text(encoding="utf-8"))
matches = []
for body in ast.walk(tree):
    if not isinstance(body, (ast.For, ast.FunctionDef, ast.With)):
        continue
    for i in range(len(body.body) - 2):
        chunk = body.body[i:i+3]
        if not all(isinstance(n, (ast.Expr, ast.Assign)) for n in chunk):
            continue
        code = ast.unparse(chunk)
        if "reversed(bars)" in code and "bars.sort" in code:
            matches.append(chunk)
if len(matches) != 1:
    raise AssertionError(f"expected one dedupe block, found {len(matches)}")
dedupe = compile(ast.fix_missing_locations(ast.Module(body=matches[0], type_ignores=[])), "<production-dedupe>", "exec")
rng = random.Random(20261010)
for trial in range(100):
    count = rng.randint(10, 200)
    candles = [(i * 300, float(i), float(trial)) for i in range(count)]
    original = []
    for row in candles:
        original.append(row)
        if rng.random() < 0.45:
            original.append((row[0], -999.0, float(trial)))
    rng.shuffle(original)
    expected = {}
    for row in original:
        expected.setdefault(row[0], row)
    namespace = {"bars": list(original)}
    exec(dedupe, namespace)
    actual = namespace["bars"]
    if actual != [expected[t] for t in sorted(expected)]:
        raise AssertionError(f"duplicate policy mismatch at trial {trial}")
print("PASS 100 actual-production-code duplicate-candle trials")
