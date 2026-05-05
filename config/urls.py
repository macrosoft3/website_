from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


def _page(template: str, lang: str, page_name: str, alt_url: str) -> TemplateView:
    return TemplateView.as_view(
        template_name=template,
        extra_context={
            "lang": lang,
            "page_name": page_name,
            "alt_lang_url": alt_url,
        },
    )


urlpatterns = [
    path("", _page("pages/home.html", "ja", "home", "/en/"), name="home"),
    path(
        "vision/",
        _page("pages/vision.html", "ja", "vision", "/en/vision/"),
        name="vision",
    ),
    path(
        "software/",
        _page("pages/software.html", "ja", "software", "/en/software/"),
        name="software",
    ),
    path(
        "holdings/",
        _page("pages/holdings.html", "ja", "holdings", "/en/holdings/"),
        name="holdings",
    ),
    path(
        "business/",
        _page("pages/business.html", "ja", "business", "/en/business/"),
        name="business",
    ),
    path(
        "company/",
        _page("pages/company.html", "ja", "company", "/en/company/"),
        name="company",
    ),
    path(
        "contact/",
        _page("pages/contact.html", "ja", "contact", "/en/contact/"),
        name="contact",
    ),
    path(
        "legal/privacy/",
        _page("pages/legal/privacy.html", "ja", "privacy", "/en/legal/privacy/"),
        name="privacy",
    ),
    path(
        "legal/cookies/",
        _page("pages/legal/cookies.html", "ja", "cookies", "/en/legal/cookies/"),
        name="cookies",
    ),
    path("en/", _page("pages/en/home.html", "en", "home", "/"), name="home_en"),
    path(
        "en/vision/",
        _page("pages/en/vision.html", "en", "vision", "/vision/"),
        name="vision_en",
    ),
    path(
        "en/software/",
        _page("pages/en/software.html", "en", "software", "/software/"),
        name="software_en",
    ),
    path(
        "en/holdings/",
        _page("pages/en/holdings.html", "en", "holdings", "/holdings/"),
        name="holdings_en",
    ),
    path(
        "en/business/",
        _page("pages/en/business.html", "en", "business", "/business/"),
        name="business_en",
    ),
    path(
        "en/company/",
        _page("pages/en/company.html", "en", "company", "/company/"),
        name="company_en",
    ),
    path(
        "en/contact/",
        _page("pages/en/contact.html", "en", "contact", "/contact/"),
        name="contact_en",
    ),
    path(
        "en/legal/privacy/",
        _page("pages/en/legal/privacy.html", "en", "privacy", "/legal/privacy/"),
        name="privacy_en",
    ),
    path(
        "en/legal/cookies/",
        _page("pages/en/legal/cookies.html", "en", "cookies", "/legal/cookies/"),
        name="cookies_en",
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots",
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(
            template_name="sitemap.xml",
            content_type="application/xml",
        ),
        name="sitemap",
    ),
    path("admin/", admin.site.urls),
]
