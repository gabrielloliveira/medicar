from datetime import datetime

from medicar.schedule.models import Schedule


def can_mark_appointment(schedule: Schedule, time: str):
    today = datetime.today().date()
    if schedule.date < today:
        return False
    datetime_ = datetime.fromisoformat(f"{schedule.date} {time}")
    if datetime_.time() not in schedule.get_available_times().values_list("time", flat=True):
        return False
    return True
