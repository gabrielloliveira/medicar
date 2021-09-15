from django.db.transaction import atomic
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from medicar.core.models import Doctor, MedicalAppointment
from medicar.core.serializers import DoctorSerializer, MedicalAppointmentSerializer
from medicar.core.services import can_mark_appointment
from medicar.schedule.models import Schedule


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


class MedicalAppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = MedicalAppointment.objects.filter_pending_appointments()

    @atomic
    def post(self, request, *args, **kwargs):
        schedule_id = request.data.get("agenda_id")
        schedule = Schedule.objects.filter(id=schedule_id).first()
        time = request.data.get("horario")

        if not schedule:
            json_response = {"message": "ID da agenda inválido."}
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

        if not can_mark_appointment(schedule, time):
            json_response = {"message": "Não foi possível marcar uma consulta para este horário."}
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

        appointment = MedicalAppointment.objects.create(
            doctor=schedule.doctor,
            date=schedule.date,
            time=time
        )

        serializer = self.serializer_class(instance=appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
