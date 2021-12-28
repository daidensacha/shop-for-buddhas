from .models import Category, Product
from accounts.models import UserModel
from django.test import TestCase

import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


class ModelTests(TestCase):
    def test_Category(self):
        length = len(Category.objects.all())
        assert length == 0
        category = Category.objects.create(
            name='testCategory', friendly_name='testCat')
        length = len(Category.objects.all())
        assert length == 1
        return category

    def test_category_return_str(self):
        category = self.test_Category()
        self.assertEqual(str(category), 'testCategory')

    def test_get_friendly_name(self):
        category = self.test_Category()
        self.assertEqual(str(category.friendly_name), 'testCat')

    def test_Product(self):
        length = len(Product.objects.all())
        assert length == 0
        test_user = UserModel.objects.create(
            first_name='first_user',
            last_name='last_user',
            username='first_last_username',
            email='firstlast@gmail.com',
            user_type='is_customer'
            )

        category = self.test_Category()
        product = Product.objects.create(
            category=category, sku='25036', name='testProduct',
            price='25.00', description='testDdescription', rating='5',
            created_by=test_user
        )
        length = len(Product.objects.all())
        assert length == 1

        return product

    def test_Product_str_return(self):
        product = self.test_Product()
        self.assertEqual(str(product), 'testProduct')
