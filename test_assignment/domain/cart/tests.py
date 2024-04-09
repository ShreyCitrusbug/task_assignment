import random
import tempfile

from django.test import TestCase
from faker import Faker

from test_assignment.domain.product_management.models import (Product)
from test_assignment.domain.cart.models import Cart

from test_assignment.domain.cart.services import CartService
from utils.test_helper_data.test_helper import (CategoryCreateTestHelper,
                                                ProductCreateTestHelper,
                                                ProductImagesCreateTestHelper)

fake = Faker()


class CartModelTestCases(TestCase):
    """
    Test cases for cart model.
    """

    def setUp(self):
        """
        Set up for testing cart model.
        """
        self.cart_quantity = random.randint(1, 500)
        self.cart_model = Cart
        self.cart_service = CartService
        self.product_helper_class = ProductCreateTestHelper()
        self.product = self.product_helper_class.create_product_data()
        self.cart = self.cart_service.cart_factory().build_entity_with_id(
            product=self.product,
            quantity=self.cart_quantity
        )
        self.cart.save()

    def test_create_cart_model(self):
        """
        Test create cart model.
        """
        cart = self.cart_service.cart_factory().build_entity_with_id(
            product=self.product,
            quantity=random.randint(1, 200)
        )
        cart.save()
        self.assertTrue(isinstance(cart, self.cart_model))

    def test_negative_create_cart_model_by_product(self):
        with self.assertRaises(Exception):
            cart = self.cart_service.cart_factory().build_entity_with_id(
                product="dasgkajhhashdkashjdaskasjdhasjkdrasuuasiaiyuweyuiahasddiasjklskl",
                quantity=random.randint(1, 200)
            )
            cart.save()

    def test_get_category(self):
        cart = self.cart_service.get_cart_repo().get(id=self.cart.id)
        self.assertTrue(cart, self.cart_model)

    def test_negative_get_cart_by_wrong_uuid(self):
        with self.assertRaises(Exception):
            cart = self.cart_service.get_cart_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            self.assertTrue(cart, self.cart_model)

    def test_update_category(self):
        """
        Test update cart.
        """
        new_quantity = 102
        self.cart.quantity = new_quantity
        self.cart.save()
        self.assertTrue(self.cart.quantity, new_quantity)

    def test_negative_update_cart_by_invalid_quantity(self):
        """
        Test negative update cart by invalid quantity.
        """
        with self.assertRaises(Exception):
            product = -102
            self.cart.product = product
            self.cart.save()
            self.assertTrue(self.cart.quantity, product)

    def test_negative_update_cart_by_wrong_uuid(self):
        """
        Test negative update cart by wrong uuid.
        """
        with self.assertRaises(Exception):
            cart = self.cart_service.get_cart_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            cart.quantity = 101
            cart.save()
            self.assertTrue(cart.quantity, 101)

    def test_delete_category(self):
        """
        Test delete cart.
        """
        self.cart.delete()
        cart = self.cart_service.get_cart_repo().filter(id=self.cart.id)
        self.assertEqual(len(cart), 0)

    def test_delete_cart_by_wrong_uuid(self):
        """
        Test delete cart by wrong uuid.
        """
        with self.assertRaises(Exception):
            cart = self.cart_service.get_cart_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            cart.delete()
