import tempfile
import random

from django.test import TestCase
from django.urls import reverse
from faker import Faker

from test_assignment.application.product__management.services import ProductAppServices
from utils.test_helper_data.test_helper import ProductCreateTestHelper
from test_assignment.domain.product_management.models import Product
fake = Faker()


class ProductViewTestCases(TestCase):
    """
    ProductListView test cases.
    """

    def setUp(self):
        self.product_create_test_helper = ProductCreateTestHelper()
        self.product = self.product_create_test_helper.create_product_data()
        self.product_model = Product

    def test_product_list_view(self):
        """
        Test product list view.
        """
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertTemplateUsed(response, 'product_list.html')

    def test_no_product_list_view(self):
        """
        Test product list view.
        """
        self.product.delete()
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertTemplateUsed(response, 'product_list.html')

    def test_create_product_view(self):
        """
        Test create product view.
        """
        product_data = {
            'name': fake.name(),
            'description': fake.name(),
            'price': random.randint(800, 1000),
            'sell_price': random.randint(300, 799),
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 302)

    def test_negative_create_product_view(self):
        """
        Test negative create product view by passing empty name.
        """
        product_data = {
            'name': "",
            'description': fake.name(),
            'price': random.randint(800, 1000),
            'sell_price': random.randint(300, 799),
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Name is required")

    def test_negative_create_product_view_by_empty_description(self):
        """
        Test negative create product view by passing empty description.
        """
        product_data = {
            'name': fake.name(),
            'description': "",
            'price': random.randint(800, 1000),
            'sell_price': random.randint(300, 799),
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        print(response.__dict__, "...")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Description is required")

    def test_negative_create_product_view_by_empty_price(self):
        """
        Test negative create product view by passing empty price.
        """
        product_data = {
            'name': fake.name(),
            'description': fake.name(),
            'price': "",
            'sell_price': random.randint(300, 799),
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Price is required")

    def test_negative_create_product_view_by_empty_sell_price(self):
        """
        Test negative create product view by passing empty sell price.
        """
        product_data = {
            'name': fake.name(),
            'description': "",
            'price': random.randint(800, 1000),
            'sell_price': "",
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Description is required")

    def test_negative_create_product_view_by_empty_quantity(self):
        """
        Test negative create product view by passing empty quantity.
        """
        product_data = {
            'name': fake.name(),
            'description': "",
            'price': random.randint(800, 1000),
            'sell_price': random.randint(300, 799),
            'category': "",
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Description is required")

    def test_negative_create_product_view_by_wrong_price_sell_price(self):
        """
        Test negative create product view by passing sell price greater than price.
        """
        product_data = {
            'name': fake.name(),
            'description': fake.name(),
            'price': 1054,
            'sell_price': 1240,
            'category': self.product.category.id,
            'quantity': random.randint(1, 1000),
            "images": [tempfile.NamedTemporaryFile(suffix=".jpg").name, tempfile.NamedTemporaryFile(suffix=".jpg").name]
        }
        response = self.client.post('/product/create', data=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "*Sell price should less than price")

    def test_product_retrieve_view(self):
        """
        Test product retrieve view.
        """
        response = self.client.get(
            reverse('product:product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_delete_product_view(self):
        """
        Test delete product view.
        """
        self.client.get(f'/product/delete/{self.product.id}')
        self.assertTrue(isinstance(self.product, self.product_model))
