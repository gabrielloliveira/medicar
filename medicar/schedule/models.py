import datetime

from django.db import models

from medicar.core.models import DefaultBaseModel
from medicar.schedule.managers import ScheduleManager


class Schedule(DefaultBaseModel):
    doctor = models.ForeignKey("core.Doctor", verbose_name="médico", on_delete=models.CASCADE)
    date = models.DateField("dia da agenda")
    times = models.ManyToManyField("ScheduleTime", verbose_name="horários", blank=True)
    has_available_time = models.BooleanField("tem horário livre", default=True)

    objects = ScheduleManager()

    def get_available_times(self):
        now = datetime.datetime.now()
        appointments_hours = self.doctor.medicalappointment_set.filter(date=self.date).values_list("time", flat=True)
        return self.times.filter(time__gte=now.time()).exclude(time__in=appointments_hours)

    def __str__(self):
        return f"Agenda de {self.doctor} - {self.date.day}/{self.date.month}/{self.date.year}/"

    class Meta:
        verbose_name = "agenda"
        verbose_name_plural = "agendas"

    def save(self, *args, **kwargs):
        self.has_available_time = self.get_available_times().exists()
        super(Schedule, self).save(*args, **kwargs)


class ScheduleTime(DefaultBaseModel):
    time = models.TimeField("horário", unique=True)

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Hórarios"
