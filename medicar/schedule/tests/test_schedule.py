from datetime import datetime, timedelta

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status

from medicar.core.tests.conftest import user, api_client
from medicar.schedule.models import ScheduleTime, Schedule


@pytest.fixture
def schedule_instance(db):
    now = datetime.now()
    ScheduleTime.objects.create(time=now + timedelta(minutes=10))
    ScheduleTime.objects.create(time=now + timedelta(minutes=20))
    ScheduleTime.objects.create(time=now + timedelta(minutes=30))
    instance = baker.make("schedule.Schedule")
    instance.times.add(*ScheduleTime.objects.all())
    return instance


def test_schedule_has_available_times(schedule_instance):
    assert schedule_instance.has_available_time is True
    assert schedule_instance.has_available_time == schedule_instance.get_available_times().exists()


def test_schedule_manager(schedule_instance):
    assert Schedule.objects.filter_schedule_actives().count() == 1
    assert Schedule.objects.filter_schedule_actives().first() == schedule_instance


def test_make_appointment(schedule_instance, user, api_client):
    data = {
        "agenda_id": schedule_instance.id,
        "horario": str(schedule_instance.times.all().first().time)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = api_client.post(reverse("core:medical_appointment_list_create"), data=data, headers=headers)

    assert response.status_code == status.HTTP_201_CREATED
    assert schedule_instance.get_available_times().count() == 2


def test_schedule_not_display(schedule_instance, user, api_client):
    first_time = schedule_instance.times.all().first()
    schedule_instance.times.clear()
    schedule_instance.times.add(first_time)

    data = {
        "agenda_id": schedule_instance.id,
        "horario": str(first_time.time)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = api_client.post(reverse("core:medical_appointment_list_create"), data=data, headers=headers)

    response_list_schedules = api_client.get(reverse("schedule:list"))

    assert response.status_code == status.HTTP_201_CREATED
    assert schedule_instance.get_available_times().count() == 0
    assert response_list_schedules.status_code == status.HTTP_200_OK
    assert response_list_schedules.content == b'[]'
