from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from medicar.schedule.models import Schedule
from medicar.schedule.serializers import ScheduleSerializer


class ScheduleListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        qs = Schedule.objects.filter_schedule_actives()

        if self.request.query_params.get("medico"):
            qs = qs.filter(doctor_id=self.request.query_params.get("medico"))

        if self.request.query_params.get("especialidade"):
            qs = qs.filter(doctor__specialty_id=self.request.query_params.get("especialidade"))

        if self.request.query_params.get("data_inicio") and self.request.query_params.get("data_final"):
            date_start = self.request.query_params.get("data_inicio")
            date_end = self.request.query_params.get("data_final")
            qs = qs.filter(date__range=[date_start, date_end])

        return qs
