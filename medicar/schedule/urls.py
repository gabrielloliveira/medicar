from django.urls import path

from medicar.schedule import viewsets

app_name = "schedule"

urlpatterns = [
    path("", viewsets.ScheduleListView.as_view(), name="list")
]
