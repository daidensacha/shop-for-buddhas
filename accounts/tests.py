from accounts.models import UserModel
from django.test import TestCase
import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


# Unit Tests: Testing Models
class ModelTests(TestCase):
    def test_profile(self):
        length = len(UserModel.objects.all())
        assert length == 0
        user = UserModel()
        user.first_name = "test"
        user.last_name = "user"
        user.username = "testuser"
        user.email = "testuser@gmail.com"
        user.user_type = 'is_customer'
        user.save()
        length = len(UserModel.objects.all())
        assert length == 1
