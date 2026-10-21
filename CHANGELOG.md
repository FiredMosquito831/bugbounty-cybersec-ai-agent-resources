# Changelog

## 2.0.0 — 2026-10-21

The research archive became a published, searchable atlas.

### Added

- Static knowledge-base site generated from the archive: home, source library, 19 collections,
  papers, repositories, taxonomy, agent blueprint and about pages.
- Client-side library with full-text search, collection and annotation filters, four sort orders,
  pagination and shareable URL state.
- `scripts/build_data.py` and `scripts/build_site.py`, deterministic stdlib/Jinja2 builds.
- Structured datasets in `data/` (sources, collections, papers, repositories, taxonomy, blueprint).
- 11 dataset-integrity tests and a GitHub Actions workflow that also verifies generated output is
  committed.
- GitHub Pages deployment with sitemap, robots file, Open Graph metadata, structured data and a
  custom 404.
- README, CONTRIBUTING, SECURITY, LICENSE and CHANGELOG.

### Changed

- Duplicate paper copies are merged into one entry with alternate-copy links; star markers are
  removed from descriptions and shown as an anchor badge.
- Collection names, counts and descriptions are generated from the source TSV instead of being
  hand-maintained.

### Preserved

- The original research documents in `repertoire/` remain the source of truth.

## 1.0.0 — 2026-08-20

Initial research archive: 1,216 catalogued sources, 19 collections, 17 paper files, a repository
manifest and the autonomous-agent context document.
