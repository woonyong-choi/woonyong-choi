import hashlib
from pathlib import Path
import subprocess
import sys
import unittest

from update_profile import markdown_links, validate_profile


ROOT = Path(__file__).resolve().parents[1]


class ProfileContractTest(unittest.TestCase):
    def test_curated_profile_is_valid(self) -> None:
        self.assertEqual(validate_profile("# Developer\n\n[Source](https://github.com/example/tool)\n"), [])

    def test_retired_metrics_cannot_reappear(self) -> None:
        markdown = "# Developer\n<!-- project_cards:start -->\n[Source](https://example.com)\n"
        self.assertTrue(any("Retired" in error for error in validate_profile(markdown)))

    def test_private_locators_are_not_published(self) -> None:
        for locator in ("/Users/example/secret", "repo://knowledge/wiki", "wiki/personal/career"):
            with self.subTest(locator=locator):
                self.assertTrue(validate_profile(f"# Developer\n{locator}\n[Source](https://example.com)"))

    def test_links_cannot_restore_retired_blog_or_local_routes(self) -> None:
        for url in ("https://example.com/#/blog", "https://example.com/#/posts/old",
                    "http://example.com", "https://localhost/demo", "javascript:alert"):
            with self.subTest(url=url):
                self.assertTrue(validate_profile(f"# Developer\n[Open]({url})\n"))

    def test_public_contact_and_repeated_links(self) -> None:
        markdown = "# Developer\n[Mail](mailto:developer@example.com)\n[A](https://example.com)\n[B](https://example.com)"
        self.assertEqual(validate_profile(markdown), [])
        self.assertEqual(len(markdown_links(markdown)), 2)

    def test_heading_and_evidence_are_required(self) -> None:
        self.assertTrue(validate_profile("# One\n# Two\n"))
        self.assertTrue(validate_profile("No heading\n[Source](https://example.com)"))

    def test_real_profile_and_cli_are_read_only(self) -> None:
        profile = ROOT / "README.md"
        before = hashlib.sha256(profile.read_bytes()).hexdigest()
        self.assertEqual(validate_profile(profile.read_text()), [])
        result = subprocess.run([sys.executable, str(ROOT / "scripts/update_profile.py"), "--check"],
                                cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No files changed", result.stdout)
        self.assertEqual(hashlib.sha256(profile.read_bytes()).hexdigest(), before)

    def test_workflow_has_no_scheduled_write_path(self) -> None:
        workflow = (ROOT / ".github/workflows/metrics.yml").read_text()
        for retired in ("schedule:", "contents: write", "git push", "git commit", "GH_TOKEN"):
            self.assertNotIn(retired, workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("update_profile.py --check", workflow)


if __name__ == "__main__":
    unittest.main()
