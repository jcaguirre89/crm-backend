from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from django.views import defaults as default_views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from crm_backend.users.views import UserViewSet, CheckLogin
from crm_backend.crm.views import (
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
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", auth_views.obtain_auth_token),
    path("auth/check-login/", CheckLogin.as_view(), name="check-login"),
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
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="swagger-ui",
    ),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
