from django.db import models

from medicar.core.models import DefaultBaseModel
from medicar.schedule.managers import ScheduleManager


class Schedule(DefaultBaseModel):
    doctor = models.ForeignKey("core.Doctor", verbose_name="médico", on_delete=models.CASCADE)
    date = models.DateField("dia da agenda")
    times = models.ManyToManyField("ScheduleTime", verbose_name="horários", blank=True)

    objects = ScheduleManager()

    def get_available_times(self):
        appointments_hours = self.doctor.medicalappointment_set.filter(date=self.date).values_list("time", flat=True)
        return self.times.all().exclude(time__in=appointments_hours)

    def __str__(self):
        return f"Agenda de {self.doctor} - {self.date.day}/{self.date.month}/{self.date.year}/"

    class Meta:
        verbose_name = "agenda"
        verbose_name_plural = "agendas"


class ScheduleTime(DefaultBaseModel):
    time = models.TimeField("horário", unique=True)

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Hórarios"
