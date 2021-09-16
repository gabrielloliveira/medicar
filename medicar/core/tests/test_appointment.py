from model_bakery import baker
from rest_framework import status
from rest_framework.reverse import reverse

from medicar.core.models import MedicalAppointment
from medicar.schedule.tests.test_schedule import schedule_instance


def test_add_appointment(schedule_instance, user, api_client):
    data = {
        "agenda_id": schedule_instance.id,
        "horario": str(schedule_instance.times.all().first().time)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = api_client.post(reverse("core:medical_appointment_list_create"), data=data, headers=headers)

    assert response.status_code == status.HTTP_201_CREATED
    assert MedicalAppointment.objects.count() == 1


def test_hour_invalid(schedule_instance, user, api_client):
    baker.make(
        "core.MedicalAppointment",
        time=schedule_instance.times.all().first().time,
        date=schedule_instance.date,
        doctor=schedule_instance.doctor,
        user=user
    )

    data = {
        "agenda_id": schedule_instance.id,
        "horario": str(schedule_instance.times.all().first().time)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = api_client.post(reverse("core:medical_appointment_list_create"), data=data, headers=headers)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert MedicalAppointment.objects.count() == 1


def test_hour_is_re_available(schedule_instance, user, api_client):
    first_time = schedule_instance.times.all().first()
    schedule_instance.times.clear()
    schedule_instance.times.add(first_time)

    instance = baker.make(
        "core.MedicalAppointment",
        time=first_time.time,
        date=schedule_instance.date,
        doctor=schedule_instance.doctor,
        user=user
    )
    assert schedule_instance.get_available_times().exists() is False

    response = api_client.delete(reverse("core:medical_appointment_delete", kwargs={'pk': instance.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert schedule_instance.get_available_times().exists() is True
    assert schedule_instance.get_available_times().count() == 1
    assert schedule_instance.get_available_times().first() == first_time
