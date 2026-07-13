"""Tests for the GratefulMoments public pages."""

from http import HTTPStatus

import pytest
from django.test import Client

APP_PATHS = [
    "/software/grateful-moments/",
    "/software/grateful-moments/support/",
    "/software/grateful-moments/privacy/",
    "/en/software/grateful-moments/",
    "/en/software/grateful-moments/support/",
    "/en/software/grateful-moments/privacy/",
]
SCREENSHOT_COUNT = 3


@pytest.mark.parametrize("path", APP_PATHS)
def test_app_page_returns_200(client: Client, path: str) -> None:
    response = client.get(path)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize("path", APP_PATHS)
def test_app_page_has_canonical_and_language_alternate(
    client: Client,
    path: str,
) -> None:
    body = client.get(path).content.decode()
    assert f"https://ether-llc.com{path}" in body
    assert 'rel="alternate"' in body


def test_product_page_references_local_screenshots(client: Client) -> None:
    body = client.get("/software/grateful-moments/").content.decode()
    assert body.count("images/apps/grateful-moments/") == SCREENSHOT_COUNT


def test_app_pages_are_in_sitemap(client: Client) -> None:
    body = client.get("/sitemap.xml").content.decode()
    for path in APP_PATHS:
        assert f"https://ether-llc.com{path}" in body
