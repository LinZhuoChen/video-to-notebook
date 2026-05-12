from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_home_lists_courses_and_concepts(astro_server: str, page: Page):
    page.goto(astro_server)
    expect(page.locator("h1")).to_have_text("course-merger")
    body = page.content()
    assert "2 course" in body
    assert "1 concept" in body


@pytest.mark.e2e
def test_concept_page_shows_occurrences_across_courses(astro_server: str, page: Page):
    page.goto(f"{astro_server}/concepts/attention/")
    expect(page.locator("h1")).to_contain_text("Attention")
    body = page.content()
    assert "cs336" in body
    assert "gpu-mode" in body


@pytest.mark.e2e
def test_compare_view_shows_two_columns(astro_server: str, page: Page):
    page.goto(f"{astro_server}/concepts/attention/compare/")
    cols = page.locator(".compare-col")
    expect(cols).to_have_count(2)
