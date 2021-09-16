from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from medicar.schedule.models import Schedule


@receiver(m2m_changed, sender=Schedule.times.through)
def update_schedule(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    if action != "post_add":
        return
    instance.save()
