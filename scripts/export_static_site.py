from __future__ import annotations

import shutil
import sys
from pathlib import Path

import django
from django.conf import settings
from django.test import Client
from django.urls import resolve
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = BASE_DIR / "dist"
HTTP_OK = 200

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

PAGES = [
    ("home", "/", "Ether合同会社", Path("index.html")),
    ("services", "/services/", "事業内容", Path("services/index.html")),
    ("company", "/company/", "会社概要", Path("company/index.html")),
    ("about", "/about/", "会社概要", Path("about/index.html")),
    ("contact", "/contact/", "お問い合わせ", Path("contact/index.html")),
]

SENSITIVE_TERMS = [
    "千葉県浦安市",
    "入船三丁目",
    "金１円",
    "有限責任社員増田創",
]


def configure_django() -> None:
    if settings.configured:
        return

    settings.configure(
        SECRET_KEY="static-export-only",  # noqa: S106 - Not used outside static rendering.
        DEBUG=False,
        ALLOWED_HOSTS=["testserver"],
        ROOT_URLCONF="scripts.static_export_urls",
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
        ],
        MIDDLEWARE=[],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [str(BASE_DIR / "ether" / "templates")],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            },
        ],
        STATIC_URL="/static/",
        STATICFILES_DIRS=[str(BASE_DIR / "ether" / "static")],
        MEDIA_URL="/media/",
        USE_I18N=True,
        USE_TZ=True,
        LANGUAGE_CODE="ja",
        TIME_ZONE="Asia/Tokyo",
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )


def render_pages() -> list[str]:
    client = Client()
    rendered_html: list[str] = []

    for name, path, expected_text, output_path in PAGES:
        reversed_path = reverse(name)
        if reversed_path != path:
            msg = f"{name} reversed to {reversed_path}, expected {path}"
            raise RuntimeError(msg)

        resolved_name = resolve(path).view_name
        if resolved_name != name:
            msg = f"{path} resolved to {resolved_name}, expected {name}"
            raise RuntimeError(msg)

        response = client.get(path)
        if response.status_code != HTTP_OK:
            msg = f"{path} returned HTTP {response.status_code}"
            raise RuntimeError(msg)

        html = response.content.decode()
        if expected_text not in html:
            msg = f"{path} is missing expected text: {expected_text}"
            raise RuntimeError(msg)

        target = DIST_DIR / output_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        rendered_html.append(html)

    return rendered_html


def validate_output(rendered_html: list[str]) -> None:
    combined_html = "".join(rendered_html)
    for term in SENSITIVE_TERMS:
        if term in combined_html:
            msg = f"Rendered static output contains sensitive term: {term}"
            raise RuntimeError(msg)

    required_files = [
        Path("index.html"),
        Path("services/index.html"),
        Path("company/index.html"),
        Path("about/index.html"),
        Path("contact/index.html"),
        Path("static/css/project.css"),
        Path("static/js/project.js"),
        Path("static/images/ether-hero.png"),
        Path("static/images/favicons/favicon.ico"),
    ]
    for relative_path in required_files:
        if not (DIST_DIR / relative_path).is_file():
            msg = f"Missing static export file: {relative_path}"
            raise RuntimeError(msg)

    home_html = (DIST_DIR / "index.html").read_text(encoding="utf-8")
    for link in [
        "/services/",
        "/company/",
        "/contact/",
        "/static/css/project.css",
        "/static/js/project.js",
    ]:
        if link not in home_html:
            msg = f"Home page is missing link: {link}"
            raise RuntimeError(msg)


def export_static_site() -> None:
    configure_django()
    django.setup()

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    rendered_html = render_pages()
    shutil.copytree(BASE_DIR / "ether" / "static", DIST_DIR / "static")
    validate_output(rendered_html)

    sys.stdout.write(f"Exported {len(PAGES)} pages to {DIST_DIR}\n")


if __name__ == "__main__":
    export_static_site()
