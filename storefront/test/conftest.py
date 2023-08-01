from django.contrib.auth.models import User
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_authenticate(api_client):
    def do_user_authenticate(is_staff= True):
        return api_client.force_authenticate(user=User(is_staff= True)) 
    return do_user_authenticate

