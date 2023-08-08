from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Versatile Interview API",
        default_version="v1",
        description="Versatile Interview description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Versatile Interview License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("account.urls")),
    path("", include("chat.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api-auth/", include("rest_framework.urls")),
]

admin.site.site_header = settings.APP_SITE_HEADER
admin.site.site_title = settings.APP_SITE_TITLE
admin.site.index_title = settings.APP_INDEX_TITLE
