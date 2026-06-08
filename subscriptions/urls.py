from django.urls import path, re_path
from .views import check_in_view, dashboard
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kutubxona",
        default_version='v1',
        description="Kutubxona API",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Mit Liscense"),
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('check-in/', check_in_view, name='check-in'),
    path('dashboard/', dashboard, name='dashboard'),

    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]