from rest_framework import serializers

from medicar.core.serializers import DoctorSerializer
from medicar.schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)
    times = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ("id", "doctor", "date", "times",)

    def get_times(self, instance):
        objects = instance.get_available_times()
        return objects.values_list("time", flat=True)
