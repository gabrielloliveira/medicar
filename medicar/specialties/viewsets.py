from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from medicar.specialties.models import Specialty
from medicar.specialties.serializers import SpecialtySerializer


class SpecialtyListView(generics.ListAPIView):
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Specialty.objects.all()

        if self.request.GET.get("search"):
            qs = qs.filter(name__icontains=self.request.GET.get("search"))

        return qs


class SpecialtyRetrieveView(generics.RetrieveAPIView):
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]
