from django.db import models

from medicar.core.models import DefaultBaseModel


class Specialty(DefaultBaseModel):
    name = models.CharField("nome", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"
