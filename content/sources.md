# Source revisions and maintenance

The machine-readable [sources.json](sources.json) records the public source commit and imported file list for each product.
The source repositories are authoritative. The imported guides retain their original licenses and notices.

To update the documentation, commit source changes, then run `scripts/sync_docs.py` as described in the
[documentation repository](https://github.com/LandminenTester/docs). Review the diff, build with MkDocs, check links,
and commit the import together with the changed source manifest. Do not edit an imported page directly: the next sync
overwrites it. Shared introductions, this maintenance page and the panel HTTP guide are maintained here.

GitHub Actions builds and checks every push and pull request, publishes `main` to GitHub Pages, and offers a manual
source-sync workflow that opens a pull request. Publishing to GitBook uses the same Markdown tree and `SUMMARY.md`.
The original Mintlify/Brewery files remain in the repository for existing users.
