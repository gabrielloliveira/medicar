from rest_framework import serializers

from medicar.core.models import Doctor, MedicalAppointment
from medicar.specialties.serializers import SpecialtySerializer


class DoctorCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "crm", "name", "specialty",)


class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(many=False, read_only=True)

    class Meta:
        model = Doctor
        fields = ("id", "crm", "name", "specialty",)


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)

    class Meta:
        model = MedicalAppointment
        fields = ("id", "date", "time", "created_at", "doctor",)
