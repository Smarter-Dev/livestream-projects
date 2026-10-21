"""The retired DSPy demo must not offer an installable or runnable project."""
from pathlib import Path
import unittest


class Retirement(unittest.TestCase):
    def test_demo_is_documentation_only(self):
        root = Path(__file__).resolve().parents[1]
        demo = root / "building-ai-agents-with-gemini-dspy"
        self.assertEqual([p.name for p in demo.iterdir()], ["README.md"])
        self.assertIn("retired", (demo / "README.md").read_text().lower())
        self.assertNotIn("uv sync", (root / "README.md").read_text())


if __name__ == "__main__":
    unittest.main()
