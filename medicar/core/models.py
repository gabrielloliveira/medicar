import uuid

from django.db import models


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
