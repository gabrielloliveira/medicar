import uuid

from django.db import models


class DefaultBaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    uuid = models.UUIDField('UUID', unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True
