import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def user(db):
    return baker.make("User")


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
