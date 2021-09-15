from datetime import datetime

from django.db import models
from django.db.models import Q


class MedicalAppointmentQuerySet(models.QuerySet):
    def filter_pending_appointments(self):
        now = datetime.now()
        return self.filter(
            Q(Q(date=now.date()) & Q(time__gte=now.time())) |
            Q(date__gt=now.date())
        )


class MedicalAppointmentManager(models.Manager):
    def get_queryset(self):
        return MedicalAppointmentQuerySet(self.model, using=self._db)

    def filter_pending_appointments(self):
        return self.get_queryset().filter_pending_appointments()
