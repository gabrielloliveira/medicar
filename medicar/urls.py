from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Medicar API",
        default_version='v1',
        description="Descrição teste",
        terms_of_service="https://medicar.com/terms/",
        contact=openapi.Contact(email="contato@medicar.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('token/', auth_views.obtain_auth_token),
    path('especialidades/', include("medicar.specialties.urls", namespace="specialties")),
    path('agendas/', include("medicar.schedule.urls", namespace="schedule")),
    path('', include("medicar.core.urls", namespace="core")),
]
