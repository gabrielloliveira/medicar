from django.urls import path

from . import viewsets

app_name = "specialties"

urlpatterns = [
    path("", viewsets.SpecialtyListCreateView.as_view(), name="list"),
    path("<int:pk>/", viewsets.SpecialtyRetrieveUpdateDestroyView.as_view(), name="retrieve"),
]
