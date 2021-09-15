from django.urls import path

from . import viewsets

app_name = "specialties"

urlpatterns = [
    path("", viewsets.SpecialtyListView.as_view(), name="list"),
    path("<int:pk>/", viewsets.SpecialtyRetrieveView.as_view(), name="retrieve"),
]
