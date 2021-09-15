from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from medicar.core.models import Doctor, MedicalAppointment
from medicar.core.serializers import DoctorSerializer, MedicalAppointmentSerializer


class DoctorListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        qs = Doctor.objects.all()

        if self.request.GET.get("search"):
            qs = qs.filter(name__icontains=self.request.GET.get("search"))

        if self.request.GET.get("especialidade"):
            qs = qs.filter(specialty_id=self.request.GET.get("especialidade"))

        return qs


class MedicalAppointmentListView(generics.ListAPIView):
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = MedicalAppointment.objects.filter_pending_appointments()
