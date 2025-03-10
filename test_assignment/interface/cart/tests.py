import tempfile
import random

from django.test import TestCase
from django.urls import reverse
from faker import Faker

from test_assignment.application.cart.services import CartService
from test_assignment.application.product__management.services import ProductAppServices
from utils.test_helper_data.test_helper import CartCreateTestHelper, ProductCreateTestHelper


class CartViewTestCases(TestCase):
    """
    Cart view test cases.
    """

    def setUp(self):
        self.cart_test_helper = CartCreateTestHelper()
        self.product_test_helper = ProductCreateTestHelper()
        self.cart = self.cart_test_helper.create_cart_data()
        self.product = self.product_test_helper.create_product_data()

    def test_list_cart_view(self):
        """
        Test list cart view.
        """
        url = reverse('cart:cart_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.cart.quantity, 1)

    def test_create_cart_view(self):
        """
        Test create cart view.
        """
        response = self.client.get(f"/add/cart/{self.product.id}")
        self.assertRedirects(response, reverse("cart:cart_list"))

    def test_delete_cart_view(self):
        """
        Test delete cart view.
        """
        response = self.client.get(f"/cart/delete/{self.cart.id}")
        self.assertRedirects(response, reverse("cart:cart_list"))
