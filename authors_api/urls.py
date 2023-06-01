from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = "Authors Ocean API", 
        default_version = "v1",
        description = "API endpoints for Authors Ocean API",
        contact = openapi.Contact(email="johndbizz@gmail.com"),
        license = openapi.License(name="MIT License") 
        ),
        public = True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Authors Ocean API Admin"

admin.site.site_title = "Authors Ocean API Admin Portal"

admin.site.index_title = "Welcome to Authors Ocean API Portal"