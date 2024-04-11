import tempfile
import random

from django.test import TestCase
from django.urls import reverse
from faker import Faker

from utils.test_helper_data.test_helper import ProductImagesCreateTestHelper
from test_assignment.domain.product_management.models import Product, ProductImages


class ProductImagesInterfaceTestCases(TestCase):
    """
    Test cases for testing productImages interface.
    """

    def setUp(self):
        """
        Set up for testing productImages interface.
        """
        self.product_images_test_helper = ProductImagesCreateTestHelper()
        self.product_images = self.product_images_test_helper.create_product_images_data()
        self.product_images_model = ProductImages

    def test_update_product_image(self):
        """
        Test update productImages list.
        """

        response = self.client.post(f"/product/image/update/{self.product_images.id}", data={
            "image": tempfile.NamedTemporaryFile(suffix=".jpg").name})
        self.assertTrue(response.status_code, 200)
        self.assertContains(response, "success")

    def test_delete_product_image(self):
        """
        Test delete productImages.
        """

        response = self.client.get(
            f"/product/image/delete/{self.product_images.id}")
        self.assertTrue(response.status_code, 200)
