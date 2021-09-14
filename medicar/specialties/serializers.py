from rest_framework import serializers

from medicar.specialties.models import Specialty


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ("id", "name", )
