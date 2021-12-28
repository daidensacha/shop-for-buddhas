from accounts.models import UserModel
from .models import Testimonial

from django.test import TestCase

import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


class ModelTests(TestCase):
    def test_tesimonials(self):
        user = UserModel.objects.create(
            first_name='test',
            last_name='test1',
            username='testuser',
            email='testemai@`gmail.com',
            user_type='is_customer'
            )
        length = len(Testimonial.objects.all())
        assert length == 0
        testimonial = Testimonial.objects.create(
            user=user,
            user_testimonial='Aa great test website',
            user_rating='5/5',
            approved=True
            )
        return testimonial
        length = len(Testimonial.objects.all())
        assert length == 1
