import datetime
import uuid

from django.conf import settings
from django.db import models

from medicar.core.managers import MedicalAppointmentManager


class DefaultBaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    uuid = models.UUIDField('UUID', unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class Doctor(DefaultBaseModel):
    name = models.CharField("nome", max_length=500)
    crm = models.IntegerField("CRM", unique=True)
    email = models.EmailField("email", blank=True, null=True)
    phone = models.CharField("telefone", blank=True, null=True, max_length=17)
    specialty = models.ForeignKey(
        "specialties.Specialty", verbose_name="especialidade", on_delete=models.SET_NULL, blank=True, null=True
    )

    @property
    def specialty_name(self):
        return self.specialty.name if self.specialty else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"


class MedicalAppointment(DefaultBaseModel):
    doctor = models.ForeignKey("Doctor", verbose_name="médico", on_delete=models.CASCADE)
    date = models.DateField("data")
    time = models.TimeField("horário")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="usuário que marcou", on_delete=models.CASCADE)

    objects = MedicalAppointmentManager()

    @property
    def is_active(self):
        now = datetime.datetime.now()
        datetime_appointment = datetime.datetime.combine(self.date, self.time)
        return now <= datetime_appointment

    def __str__(self):
        return f"Horário marcado às {self.time} - {self.doctor}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
