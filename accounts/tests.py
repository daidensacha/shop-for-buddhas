from django.test import TestCase
import pytest
from django import urls
from accounts.models import Profile
# Create your tests here.

pytestmark = pytest.mark.django_db(transaction=True)


class ModelTests(TestCase):
    def profile_test(self):
        length = len(Profile.objects.all())
        assert length == 0
        user = Profile()
        user.first_name = "test"
        user.last_name = "user"
        user.username = "testuser"
        user.email = "testuser@gmail.com"
        user.user_type = 'is_customer'
        user.save()
        length = len(Profile.objects.all())
        assert length == 1
