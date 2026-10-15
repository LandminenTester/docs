"""Generate GitBook and MkDocs navigation from one shared manifest."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
navigation = json.loads((root / "navigation.json").read_text(encoding="utf-8"))
summary = ["# Summary", ""]
nav = []
for group, pages in navigation.items():
    summary += [f"## {group}", ""]
    nav.append({group: [{label: path} for label, path in pages.items()]})
    for label, path in pages.items():
        if not (root / "content" / path).is_file():
            raise SystemExit(f"Navigation target missing: {path}")
        summary.append(f"* [{label}]({path})")
    summary.append("")
(root / "content/SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")
config = {
    "site_name": "LandminenTester Docs",
    "site_description": "Build, configure and operate the BlackICE panel, lt-database and lt-database-api.",
    "site_url": "https://landminentester.github.io/docs/",
    "repo_url": "https://github.com/LandminenTester/docs",
    "docs_dir": "content", "site_dir": "site",
    "edit_uri": "edit/main/content/",
    "theme": {"name": "readthedocs", "highlightjs": True},
    "markdown_extensions": ["tables", "fenced_code", "toc"],
    "nav": nav,
    "exclude_docs": "SUMMARY.md\n",
    "validation": {"links": {"not_found": "warn", "unrecognized_links": "warn", "anchors": "warn"}},
}
(root / "mkdocs.yml").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
print(f"Generated navigation for {sum(map(len, navigation.values()))} pages")
