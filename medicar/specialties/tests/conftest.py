import pytest
from model_bakery import baker
from medicar.core.tests.conftest import user, api_client
from medicar.specialties.models import Specialty


@pytest.fixture
def specialties(db):
    baker.make("Specialty", name="Pediatria")
    baker.make("Specialty", name="Cardiologia")
    baker.make("Specialty", name="Ginecologia")
    return Specialty.objects.all()
