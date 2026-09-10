#!/usr/bin/env python3
"""Validate the human-owned profile README without network access or writes."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


LINK_PATTERN = re.compile(r"\[([^\]\n]+)\]\(([^\s)]+)\)")
RETIRED_MARKERS = (
    "activity_summary", "project_cards", "ci_status",
    "recent_work", "collaboration", "technologies", "recent_posts",
)
PRIVATE_LOCATORS = ("/Users/", "file://", "repo://", "wiki/personal/", "private/knowledge/")


def markdown_links(markdown: str) -> list[str]:
    class AnchorParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.links: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag == "a":
                href = dict(attrs).get("href")
                if href:
                    self.links.append(href)

    parser = AnchorParser()
    parser.feed(markdown)
    return list(dict.fromkeys([
        *(match.group(2) for match in LINK_PATTERN.finditer(markdown)),
        *parser.links,
    ]))


def validate_profile(markdown: str) -> list[str]:
    """Check presentation ownership and link syntax, not personal skill or live uptime."""
    errors: list[str] = []
    if len(re.findall(r"^# [^\n]+$", markdown, re.MULTILINE)) != 1:
        errors.append("README must have exactly one H1")
    for marker in RETIRED_MARKERS:
        if f"<!-- {marker}:" in markdown:
            errors.append(f"Retired generated section is present: {marker}")
    if "assets/generated/repo-" in markdown:
        errors.append("Automatic repository score cards must not replace curated projects")
    if any(locator in markdown for locator in PRIVATE_LOCATORS):
        errors.append("README contains a private or machine-local locator")

    links = markdown_links(markdown)
    if not links:
        errors.append("README must link to public evidence or usable tools")
    for link in links:
        parsed = urlsplit(link)
        if parsed.scheme == "mailto":
            if "@" not in parsed.path or parsed.query or parsed.fragment:
                errors.append(f"Invalid public contact link: {link}")
            continue
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            errors.append(f"Use a public HTTPS URL: {link}")
            continue
        if parsed.hostname in {"localhost", "127.0.0.1", "::1"}:
            errors.append(f"Local endpoint is not public evidence: {link}")
        if unquote(parsed.fragment).startswith("/blog") or "/#/posts/" in link:
            errors.append(f"Retired blog route: {link}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True,
                        help="Read-only validation; never regenerate or publish README")
    parser.add_argument("--readme", type=Path,
                        default=Path(__file__).resolve().parents[1] / "README.md")
    args = parser.parse_args()
    try:
        markdown = args.readme.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Cannot read profile: {error}", file=sys.stderr)
        return 1
    errors = validate_profile(markdown)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Profile structure OK; {len(markdown_links(markdown))} unique links. "
          "No files changed. Live links and claims require separate review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
