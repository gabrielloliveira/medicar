from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', auth_views.obtain_auth_token),
    path('especialidades/', include("medicar.specialties.urls", namespace="specialties")),
    path('agendas/', include("medicar.schedule.urls", namespace="schedule")),
    path('', include("medicar.core.urls", namespace="core")),
]
