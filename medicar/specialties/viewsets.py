from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from medicar.specialties.models import Specialty
from medicar.specialties.serializers import SpecialtySerializer


class SpecialtyListCreateView(generics.ListCreateAPIView):
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Specialty.objects.all()

        if self.request.GET.get("search"):
            qs = qs.filter(name__icontains=self.request.GET.get("search"))

        return qs


class SpecialtyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialtySerializer
    permission_classes = [IsAuthenticated]
    queryset = Specialty.objects.all()
