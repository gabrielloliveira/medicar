from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from medicar.core.models import MedicalAppointment
from medicar.schedule.models import Schedule


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=MedicalAppointment)
def update_schedule(sender, instance=None, created=False, **kwargs):
    doctor = instance.doctor
    date = instance.date
    schedule = Schedule.objects.filter(doctor=doctor, date=date).first()
    schedule.save()
