# LandminenTester documentation

**Read the public documentation: [landminentester.github.io/docs](https://landminentester.github.io/docs/).**

Build, installation, configuration, maintenance, API references and examples for:

* [BlackICE Server Panel](https://github.com/LandminenTester/blackice-server-panel)
* [lt-database](https://github.com/LandminenTester/lt-database)
* [lt-database-api](https://github.com/LandminenTester/lt-database-api)

The Markdown lives in `content/`. It is compatible with GitBook Git Sync and is also published with MkDocs/GitHub Pages,
so readers do not need an account. Existing Brewery/Mintlify files in `scripts/`, `images/`, `logo/`, `introduction.mdx`
and `mint.json` are preserved.

## Update from product repositories

Commit public source changes first; the importer refuses dirty working trees and records exact source commits.

```sh
python scripts/sync_docs.py --panel /path/to/blackice-server-panel --bundle /path/to/lt-database --api /path/to/lt-database-api
python scripts/build_navigation.py
```

Only tracked documentation, public screenshots, compiled recipes and the reference client are allow-listed.
Credentials, local state, database files, VFS settings and build output are never imported.
Review `content/sources.json` and the diff, then run the strict build before committing.
Edit imported guides in their product repository; edit shared guides here.

The **Sync product documentation** Actions workflow performs the same import and opens a review PR.
Settings → Actions → General must allow Actions to create pull requests for that workflow. The local command works
independently of this setting. The workflow runs only when manually requested.

## Build and preview

Requires Python 3.11 or later.

```sh
python -m venv .venv
# Activate .venv for your shell, then:
python -m pip install -r requirements.txt
python scripts/build_navigation.py
python -m mkdocs build --strict
python -m mkdocs serve
```

Open the loopback URL printed by MkDocs. `navigation.json` is the single navigation source;
the navigation script generates both `mkdocs.yml` and `content/SUMMARY.md`. Commit both generated files.
CI rejects stale navigation, broken page links and bad anchors. The `Documentation` workflow publishes `main`.

## Connect GitBook

The repository is ready for [GitBook Git Sync](https://gitbook.com/docs/guides/editing-and-publishing-documentation/import-or-migrate-your-content-to-gitbook-with-git-sync):

1. In your GitBook account, create/select the LandminenTester documentation space.
2. Connect GitHub Git Sync to **LandminenTester/docs**, branch **main**, with the repository root as the project directory.
3. First import **from GitHub into GitBook**. `.gitbook.yaml` selects `content/`, `README.md` and `SUMMARY.md`.
   Do not replace the repository with an empty space.
4. Add the space to a documentation site, set its audience to public, and publish using your chosen GitBook URL/domain.
5. Verify the three product sections, images and API links without logging in.

This account connection is separate from GitHub Pages and is not performed by committing these files. The documentation
is publicly readable on GitHub Pages while the account setup is pending. Maintain imported guides in source repositories
so a later sync does not overwrite GitBook-only edits.

## Licenses

Imported content and examples retain their upstream licenses. The importer copies each product's `LICENSE` and notices;
source attributions and commit hashes are in `content/sources.json`.
