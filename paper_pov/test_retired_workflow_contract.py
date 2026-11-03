"""Guard against dangling references to retired reusable GitHub workflows."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RETIRED = "autonomous-codex-continuation.yml"


class RetiredWorkflowContract(unittest.TestCase):
    def test_no_retired_workflow_or_caller(self):
        workflows = ROOT / ".github" / "workflows"
        self.assertFalse((workflows / RETIRED).exists())
        for path in workflows.glob("*.yml"):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn(RETIRED, content, f"dangling workflow caller: {path}")

    def test_replacement_builder_exists(self):
        self.assertTrue((ROOT / ".github/workflows/autonomous-codex-builder.yml").is_file())


if __name__ == "__main__":
    unittest.main()
