"""Regression contract for retiring a reusable workflow without dangling callers."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
RETIRED = "autonomous-codex-continuation.yml"
REPLACEMENT = "autonomous-codex-builder.yml"


def dangling_callers(root):
    """Inspect GitHub workflow and composite-action YAML, including .yaml variants."""
    github = root / ".github"
    if not github.exists():
        return []
    dangling = []
    for path in sorted(github.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".yml", ".yaml"}:
            continue
        if RETIRED in path.read_text(encoding="utf-8"):
            dangling.append(path.relative_to(root).as_posix())
    return dangling


class RetiredWorkflowContract(unittest.TestCase):
    def test_retired_workflow_absent_and_no_callers(self):
        workflows = ROOT / ".github" / "workflows"
        self.assertFalse((workflows / RETIRED).exists())
        self.assertEqual([], dangling_callers(ROOT))

    def test_replacement_builder_exists(self):
        self.assertTrue((ROOT / ".github/workflows" / REPLACEMENT).is_file())

    def test_detects_both_yaml_extensions_and_composite_actions(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            workflow = root / ".github/workflows/example.yaml"
            action = root / ".github/actions/example/action.yml"
            workflow.parent.mkdir(parents=True)
            action.parent.mkdir(parents=True)
            workflow.write_text("jobs:\\n  run:\\n    uses: ./.github/workflows/" + RETIRED)
            action.write_text("name: old\\n# " + RETIRED)
            self.assertEqual(
                [".github/actions/example/action.yml", ".github/workflows/example.yaml"],
                dangling_callers(root),
            )
            workflow.write_text("jobs:\\n  run:\\n    uses: ./.github/workflows/" + REPLACEMENT)
            action.write_text("name: replacement")
            self.assertEqual([], dangling_callers(root))


if __name__ == "__main__":
    unittest.main()
