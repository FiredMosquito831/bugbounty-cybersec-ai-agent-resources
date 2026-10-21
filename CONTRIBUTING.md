# Contributing

The archive is a curated source list, so contributions are mostly data changes.

## Adding or fixing a source

1. Edit `repertoire/_new_sources_full.tsv`. Each line has five tab-separated columns:

   ```
   <collection id>  <collection header>  <title>  <url>  <description>
   ```

   - `collection id` is the numeric id of the research batch (1–19).
   - `collection header` must exactly match one of the 19 headers already in the file.
   - `title` should name the resource, not the report section. Leading numbering is stripped automatically.
   - `url` must be a unique `http(s)` URL.
   - `description` is one short sentence explaining why the source matters.

2. Rebuild:

   ```bash
   python scripts/build_data.py
   python scripts/build_site.py
   pytest
   ```

3. Commit the TSV, `data/*.json` and `docs/` together. CI fails if the generated output is stale.

## Adding a paper

Place the PDF or HTML file in `repertoire/01_papers/` and add a row to the paper table in
`repertoire/00_REPERTOIRE_INDEX.md` with columns `Filename | Title | Source URL | Description`.
Use the literal ★★★★★ marker in the description to flag anchor reading. Duplicate copies of the
same work (same arXiv id or source URL) are merged automatically; the extra file becomes an
“alternate copy” link.

## Adding a repository

Add a row to `repertoire/REPO_MANIFEST.md`:

```
| `03_repos/<name>` | https://github.com/owner/repo | 1234 | One-line description |
```

Stars may be `—` when unknown.

## Rules

- Do not commit exploit code, payload collections or working attack tooling. Links, papers and
  methodology only.
- Keep descriptions factual and attributable; do not editorialise or invent claims.
- Do not hand-edit `data/` or `docs/` — they are generated.
- Run `ruff`-style import checks if you touch Python: `python -m ruff check scripts tests --select F821,F811,F401`.
