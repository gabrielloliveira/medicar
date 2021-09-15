from datetime import datetime

from django.contrib.auth.models import User

from medicar.core.models import MedicalAppointment
from medicar.schedule.models import Schedule


def can_mark_appointment(schedule: Schedule, time: str):
    today = datetime.today().date()
    if schedule.date < today:
        return False
    datetime_ = datetime.fromisoformat(f"{schedule.date} {time}")
    if datetime_.time() not in schedule.get_available_times().values_list("time", flat=True):
        return False
    return True


def can_delete_appointment(appointment: MedicalAppointment, user: User):
    if appointment.user != user:
        return False
    return appointment.is_active
