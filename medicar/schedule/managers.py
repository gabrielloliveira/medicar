from datetime import datetime

from django.db import models
from django.db.models import Q


class ScheduleQuerySet(models.QuerySet):
    def filter_schedule_actives(self):
        today = datetime.today()
        return self.filter(
            Q(date__gte=today) & Q(has_available_time=True)
        ).order_by("date")


class ScheduleManager(models.Manager):
    def get_queryset(self):
        return ScheduleQuerySet(self.model, using=self._db)

    def filter_schedule_actives(self):
        return self.get_queryset().filter_schedule_actives()
