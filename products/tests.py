from .models import Category, Product
from accounts.models import UserModel
from django.test import TestCase
from django.urls import reverse
import pytest
import tempfile
from django.test.client import Client

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
        self.assertEqual(str(category.get_friendly_name()), 'testCat')

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


class ViewsTests(TestCase):
    def test_products_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        test_user = UserModel.objects.create(
            first_name='first_user',
            last_name='last_user',
            username='first_last_username',
            email='firstlast@gmail.com',
            user_type='is_customer',
            password="test"
            )

        category = Category.objects.create(
            name='testCategory', friendly_name='testCat')
        product = Product.objects.create(
            category=category, sku='25036', name='testProduct',
            price='25.00', description='testDdescription', rating='5',
            created_by=test_user
        )
        url = reverse('product_detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_product_anonymouse_view(self):
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create(
            first_name='first_user',
            last_name='last_user',
            username='test_username',
            email='testusername@gmail.com',
            user_type='is_admin',
            is_active=True,
            password="test"
            )

    def test_add_product_view(self):
        login_url = reverse('account_login')
        response = self.client.post(
            login_url, {"username": self.user.username,
                        "password": self.user.password})
        url = reverse('add_product')
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
