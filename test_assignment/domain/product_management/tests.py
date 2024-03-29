import random
import tempfile

from django.forms import ValidationError
from django.test import TestCase
from faker import Faker

from test_assignment.domain.product_management.models import (Category,
                                                              Product,
                                                              ProductImages)
from test_assignment.domain.product_management.services import (
    CategoryService, ProductImagesService, ProductService)
from utils.test_helper_data.test_helper import (CategoryCreateTestHelper,
                                                ProductCreateTestHelper,
                                                ProductImagesCreateTestHelper)

fake = Faker()


class CategoryModelTestCases(TestCase):
    def setUp(self):
        """
        Set up for testing category model.
        """
        self.category_name = fake.name()
        self.category_model = Category
        self.category_service = CategoryService
        self.category = self.category_service.category_factory().build_entity_with_id(
            name=self.category_name,
        )
        self.category.save()

    def test_create_category_model(self):
        category = self.category_service.category_factory().build_entity_with_id(
            name=self.category_name,
        )
        category.save()
        self.assertTrue(isinstance(category, self.category_model))

    def test_negative_create_category_model_by_invalid_name(self):
        with self.assertRaises(Exception):
            category = self.category_service.category_factory().build_entity_with_id(
                name="dasgkajhhashdkashjdaskasjkdhasjkdrasuuasiaiyuweyuiahasddiasjklskl",
            )
            category.save()

    def test_get_category(self):
        category = self.category_service.get_category_repo().get(id=self.category.id)
        self.assertTrue(category, self.category_model)

    def test_negative_get_category_by_wrong_uuid(self):
        with self.assertRaises(Exception):
            category = self.category_service.get_category_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            self.assertTrue(category, self.category_model)

    def test_update_category(self):
        """
        Test update category.
        """
        new_name = fake.name()
        self.category.name = new_name
        self.category.save()
        self.assertTrue(self.category.name, new_name)

    def test_negative_update_category_by_invalid_name(self):
        """
        Test negative update category by invalid name.
        """
        with self.assertRaises(Exception):
            new_name = "dasgkajhhashdkashjdaskasjkdhasjkdrasuuasiaiyuweyuiahasddiasjklskl"
            self.category.name = new_name
            self.category.save()
            self.assertTrue(self.category_name.name, new_name)

    def test_negative_update_category_by_wrong_uuid(self):
        """
        Test negative update category by wrong uuid.
        """
        with self.assertRaises(Exception):
            category = self.category_service.get_category_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            category.name = "Test"
            category.save()
            self.assertTrue(category.name, "Test")

    def test_delete_category(self):
        """
        Test delete category.
        """
        self.category.delete()
        category = self.category_service.get_category_repo().filter(id=self.category.id)
        self.assertEqual(len(category), 0)

    def test_delete_category_by_wrong_uuid(self):
        """
        Test delete category by wrong uuid.
        """
        with self.assertRaises(Exception):
            category = self.category_service.get_category_repo().get(
                id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf")
            category.delete()


class ProductModelTestCases(TestCase):
    """
    Test cases for testing product model.
    """

    def setUp(self):
        """
        Set up for testing product model.
        """
        self.product_test_helper = ProductCreateTestHelper()
        self.category_test_helper = CategoryCreateTestHelper()
        self.product = self.product_test_helper.create_product_data()
        self.product_model = Product
        self.product_service = ProductService()
        self.category = self.category_test_helper.create_category_data()

    def test_create_product(self):
        """
        Test create product.
        """
        product = self.product_service.product_factory().build_entity_with_id(
            name=fake.name(),
            description=fake.name(),
            price=random.randint(500, 700),
            sell_price=random.randint(300, 699),
            category=self.category.id,
            images=tempfile.NamedTemporaryFile().name
        )
        product.save()
        self.assertTrue(isinstance(product, self.product_model))

    def test_negative_create_product_by_invalid_name(self):
        """
        Test negative create product by invalid name.
        """
        with self.assertRaises(Exception):
            product = self.product_service.product_factory().build_entity_with_id(
                name="dasgkajhhashdkashjdaskasjkdhasjkdrasuuasiaiyuweyuiahasddiasjklskl",
                description=fake.name(),
                price=random.randint(500, 700),
                sell_price=random.randint(300, 699),
                category=self.category.id,
                images=tempfile.NamedTemporaryFile().name
            )
            product.save()


class ProductImagesTestCases(TestCase):
    """
    Test cases for testing productImages model.
    """

    def setUp(self):
        """
        Set up for testing productImages model.
        """
        self.product_images_test_helper = ProductImagesCreateTestHelper()
        self.product_test_helper = ProductCreateTestHelper()
        self.product_images = self.product_images_test_helper.create_product_images_data()
        self.product_images_model = ProductImages
        self.product_images_service = ProductImagesService()
        self.product = self.product_test_helper.create_product_data()

    def test_create_product_images(self):
        """
        Test create productImages.
        """
        product_images = self.product_images_service.product_images_factory().build_entity_with_id(
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            product=self.product.id
        )
        product_images.save()

    def test_negative_create_product_images_by_empty_product_id(self):
        """
        Test create productImages.
        """
        with self.assertRaises(Exception):
            product_images = self.product_images_service.product_images_factory().build_entity_with_id(
                image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                product=""
            )
            product_images.save()
