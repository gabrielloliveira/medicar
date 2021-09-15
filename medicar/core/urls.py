from django.urls import path

from medicar.core import viewsets

app_name = "core"

urlpatterns = [
    path("medicos/", viewsets.DoctorListView.as_view(), name="doctors_list"),
    path("consultas/", viewsets.MedicalAppointmentListCreateView.as_view(), name="medical_appointment_list_create"),
    path("consultas/<int:pk>/", viewsets.MedicalAppointmentDeleteView.as_view(), name="medical_appointment_delete"),
]
