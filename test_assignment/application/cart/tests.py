import random
import tempfile

from django.forms import ValidationError
from django.test import TestCase
from faker import Faker

from test_assignment.application.cart.services import CartAppServices
from test_assignment.domain.cart.models import Cart
from utils.test_helper_data.test_helper import CartCreateTestHelper, ProductCreateTestHelper

fake = Faker()


class CartAppServicesTest(TestCase):
    def setUp(self):
        self.cart_test_helper = CartCreateTestHelper()
        self.product_test_helper = ProductCreateTestHelper()
        self.cart_app_services = CartAppServices()
        self.cart_model = Cart

    def test_list_of_all_products_in_cart(self):
        self.cart_test_helper.create_cart_data()
        cart_list = self.cart_app_services.list_of_all_products_in_cart()
        self.assertEqual(len(cart_list), 1)

    def test_create_cart_from_product_id(self):
        product = self.product_test_helper.create_product_data()
        cart = self.cart_app_services.create_cart_from_product_id(
            product_id=product.id
        )
        self.assertTrue(isinstance(cart, self.cart_model))

    def test_get_cart_by_id(self):
        cart = self.cart_test_helper.create_cart_data()
        cart = self.cart_app_services.get_cart_by_id(cart.id)
        self.assertTrue(isinstance(cart, self.cart_model))

    def test_negative_get_cart_by_wrong_uuid(self):
        with self.assertRaises(Exception):
            cart = self.cart_app_services.get_cart_by_id(
                "ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            self.assertTrue(cart, self.cart_model)
