from django.urls import path

from medicar.core import viewsets

app_name = "core"

urlpatterns = [
    path("", viewsets.DoctorListView.as_view(), name="list"),
]
