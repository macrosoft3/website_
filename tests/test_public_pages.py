import pytest
from django.urls import resolve
from django.urls import reverse

HTTP_OK = 200
pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    ("name", "path", "content"),
    [
        ("home", "/", "Ether合同会社"),
        ("services", "/services/", "事業内容"),
        ("company", "/company/", "会社概要"),
        ("contact", "/contact/", "お問い合わせ"),
    ],
)
def test_public_page_urls(client, name, path, content):
    assert reverse(name) == path
    assert resolve(path).view_name == name

    response = client.get(path)

    assert response.status_code == HTTP_OK
    assert content in response.content.decode()


def test_about_aliases_company_page(client):
    assert reverse("about") == "/about/"
    assert resolve("/about/").view_name == "about"

    response = client.get("/about/")

    assert response.status_code == HTTP_OK
    assert "会社概要" in response.content.decode()


def test_public_pages_do_not_include_sensitive_charter_details(client):
    sensitive_terms = [
        "千葉県浦安市",
        "入船三丁目",
        "金１円",
        "有限責任社員増田創",
    ]

    combined_pages = "".join(
        client.get(path).content.decode()
        for path in ["/", "/services/", "/company/", "/contact/"]
    )

    for term in sensitive_terms:
        assert term not in combined_pages
