from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from users.views import UserViewSet, CheckLogin
from crm.views import (
    CompanyViewSet,
    CompanyNoteViewSet,
    ContactViewSet,
    ContactNoteViewSet,
    DealViewSet,
    DealNoteViewSet,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, "user")
router.register(r"companies", CompanyViewSet, "company")
router.register(r"contacts", ContactViewSet, "contact")
router.register(r"deals", DealViewSet, "deal")
router.register(r"company-notes", CompanyNoteViewSet, "company-note")
router.register(r"contact-notes", ContactNoteViewSet, "contact-note")
router.register(r"deal-notes", DealNoteViewSet, "deal-note")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", auth_views.obtain_auth_token),
    path("auth/check-login/", CheckLogin.as_view(), name='check-login'),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "openapi/",
        get_schema_view(title="Backend", description="Backend API"),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
]
