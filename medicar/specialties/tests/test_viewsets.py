from django.urls import reverse
from rest_framework import status


def test_list_is_not_empty(specialties, api_client):
    response = api_client.get(reverse("specialties:list"))
    specialty = response.json()[0]

    assert response.status_code == status.HTTP_200_OK
    assert list(specialty.keys()) == ["id", "name"]


def test_search_specialties(specialties, api_client):
    response = api_client.get(reverse("specialties:list") + "?search=ia")
    response_one_item = api_client.get(reverse("specialties:list") + "?search=pediatria")

    objects_list = response.json()
    specialty = response_one_item.json()

    assert len(objects_list) == 3
    assert len(specialty) == 1
