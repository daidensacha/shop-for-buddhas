from accounts.models import UserModel
from profiles.models import UserProfile
from products.models import Category, Product
from .models import Order, OrderLineItem

from django.test import TestCase
# from django.utils import timezone

import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


class ModelTests(TestCase):
    def test_Order(self):
        length = len(Order.objects.all())
        assert length == 0

        test_user = UserModel.objects.create(
            first_name='first_user',
            last_name='last_user',
            username='first_last_username',
            email='firstlast@gmail.com',
            user_type='is_customer'
            )
        profile = UserProfile.objects.get(user=test_user)
        order = Order.objects.create(

            user_profile=profile,
            full_name='testname',
            email='test@gmail.com',
            phone_number='9856',
            street_address1='84956',
            town_or_city='8956',
            postcode='54840',
            country='US',
            delivery_cost='25.00',
            order_total='35.00',
            grand_total='60.00',
            original_cart='abxtest123',
            stripe_pid='abxtest123',
        )
        length = len(Order.objects.all())
        assert length == 1
        return order

    def test_generate_order_number(self):
        order = self.test_Order()
        self.assertEqual(order.order_number, order.order_number)

    def test_update_total(self):
        order = self.test_Order()

        self.assertEqual(order.grand_total, '60.00')

    def test_order_str_return(self):
        order = self.test_Order()

        self.assertEqual(str(order), order.order_number)
