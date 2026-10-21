"""Integrity tests for the research dataset and the parsing helpers."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.build_data import COLLECTIONS, clean, display_title, title_from_url

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name: str):
    path = DATA / name
    assert path.exists(), f"run scripts/build_data.py first ({name} missing)"
    return json.loads(path.read_text(encoding="utf-8"))


def test_sources_are_present_unique_and_linked():
    sources = load("sources.json")
    assert len(sources) == 1216
    assert len({s["url"] for s in sources}) == len(sources), "duplicate URLs"
    assert all(s["url"].startswith(("http://", "https://")) for s in sources)
    assert all(s["title"].strip() for s in sources)
    assert sum(1 for s in sources if s["has_description"]) >= 900
    assert len({s["host"] for s in sources}) >= 300


def test_every_source_belongs_to_a_known_collection():
    sources = load("sources.json")
    collections = load("collections.json")
    ids = {c["id"] for c in collections}
    assert len(collections) == 19
    assert all(s["collection"] in ids for s in sources)
    assert sum(c["count"] for c in collections) == len(sources)
    assert all(c["count"] > 0 for c in collections)
    assert all(c["description"].strip() for c in collections)


def test_papers_are_deduplicated_and_backed_by_files():
    papers = load("papers.json")
    files = {p.name for p in (ROOT / "repertoire" / "01_papers").iterdir() if p.suffix in (".pdf", ".html")}
    assert len(papers) == 15
    primary_files = {p["file"] for p in papers}
    alternate_files = {alt["file"] for p in papers for alt in p.get("alternates", [])}
    assert primary_files | alternate_files == files
    assert primary_files.isdisjoint(alternate_files)
    assert sum(1 for p in papers if p["anchor"]) == 4
    assert all("★" not in p["description"] for p in papers)
    for paper in papers:
        assert (ROOT / "repertoire" / "01_papers" / paper["file"]).exists()


def test_repositories_are_unique_and_linked():
    repos = load("repos.json")
    assert len(repos) == 36
    assert len({r["url"] for r in repos}) == len(repos)
    assert all(r["url"].startswith("https://github.com/") for r in repos)
    assert all(r["category"] for r in repos)
    assert sum(r["stars"] or 0 for r in repos) > 50_000


def test_taxonomy_sections_are_filled():
    taxonomy = load("taxonomy.json")
    assert len(taxonomy["owasp_top10_2021"]) == 10
    assert len(taxonomy["vulnerability_classes"]) >= 20
    assert len(taxonomy["tooling"]) >= 15
    assert sum(len(group["tools"]) for group in taxonomy["tooling"]) >= 100
    assert all(group["name"] and group["tools"] for group in taxonomy["tooling"])


def test_blueprint_insights_have_all_fields():
    blueprint = load("blueprint.json")
    assert len(blueprint["insights"]) == 8
    for insight in blueprint["insights"]:
        assert insight["title"] and insight["finding"] and insight["how"]
    assert [p["status"] for p in blueprint["phases"]].count("complete") == 1


# --- parser helpers -------------------------------------------------------
def test_clean_strips_markdown_and_repairs_encoding():
    assert clean("**Bold** text") == "Bold text"
    assert clean("[link](https://example.com)") == "link"
    assert clean("broken � dash") == "broken — dash"


def test_display_title_removes_numbering():
    assert display_title("2.5 SAST Tools Taxonomy", "https://example.com", "Report") == "SAST Tools Taxonomy"
    assert display_title("I. GraphQL Introspection", "https://example.com", "Report") == "GraphQL Introspection"


def test_display_title_falls_back_for_generic_headers():
    header = "EXHAUSTIVE RESEARCH REPORT: Something"
    assert display_title(header, "https://github.com/owner/repo", header) == "owner/repo"
    assert display_title("", "https://arxiv.org/abs/2502.18528", header) == "arXiv:2502.18528"


def test_title_from_url_hosts():
    assert title_from_url("https://github.com/a/b") == "a/b"
    assert title_from_url("https://www.example.com") == "example.com"


def test_collection_metadata_is_complete():
    assert len(COLLECTIONS) == 19
    for header, (name, description) in COLLECTIONS.items():
        assert header and name and description
        assert len(name) <= 40
