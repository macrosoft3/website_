"""Smoke tests for the public site."""

from __future__ import annotations

from http import HTTPStatus

import pytest
from django.test import Client

JA_PATHS = [
    "/",
    "/holdings/",
    "/software/",
    "/company/",
    "/contact/",
    "/business/",
    "/vision/",
    "/legal/privacy/",
    "/legal/cookies/",
]
EN_PATHS = ["/en" + p.rstrip("/") + "/" if p != "/" else "/en/" for p in JA_PATHS]
ALL_PATHS = JA_PATHS + EN_PATHS


@pytest.mark.parametrize("path", ALL_PATHS)
def test_page_returns_200(client: Client, path: str) -> None:
    response = client.get(path)
    assert response.status_code == HTTPStatus.OK, (
        f"{path} returned {response.status_code}"
    )


def test_robots_txt(client: Client) -> None:
    response = client.get("/robots.txt")
    assert response.status_code == HTTPStatus.OK
    assert response["Content-Type"].startswith("text/plain")


def test_sitemap_xml(client: Client) -> None:
    response = client.get("/sitemap.xml")
    assert response.status_code == HTTPStatus.OK
    assert "xml" in response["Content-Type"]


def test_alternate_lang_link_present(client: Client) -> None:
    ja = client.get("/").content.decode()
    assert 'hreflang="en"' in ja
    en = client.get("/en/").content.decode()
    assert 'hreflang="ja"' in en


def test_no_legacy_decorations_in_home(client: Client) -> None:
    body = client.get("/").content.decode()
    for token in (
        "data-reveal",
        "material-symbols",
        "brand-mark",
        "navbar-toggler",
        "cdnjs.cloudflare",
        "fonts.googleapis",
    ):
        assert token not in body, f"unexpected token in /: {token}"
