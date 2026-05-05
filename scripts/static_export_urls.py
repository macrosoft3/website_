from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "services/",
        TemplateView.as_view(template_name="pages/services.html"),
        name="services",
    ),
    path(
        "company/",
        TemplateView.as_view(template_name="pages/company.html"),
        name="company",
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/company.html"),
        name="about",
    ),
    path(
        "contact/",
        TemplateView.as_view(template_name="pages/contact.html"),
        name="contact",
    ),
    path("admin/", admin.site.urls),
]
