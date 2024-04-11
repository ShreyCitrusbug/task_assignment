import random
import tempfile

from django.forms import ValidationError
from django.test import TestCase
from faker import Faker

from test_assignment.domain.product_management.models import (Category,
                                                              Product,
                                                              ProductImages)
from test_assignment.application.product__management.services import CategoryAppServices, ProductAppServices, ProductImagesAppServices
from utils.test_helper_data.test_helper import (CategoryCreateTestHelper,
                                                ProductCreateTestHelper,
                                                ProductImagesCreateTestHelper)

fake = Faker()


class CategoryAppServicesTestCases(TestCase):
    """
    Test cases for category application service.
    """

    def setUp(self):
        """
        Set up for testing category model.
        """
        self.category_test_helper = CategoryCreateTestHelper()
        self.name = fake.name()
        self.category_model = Category
        self.category_app_services = CategoryAppServices()
        self.category = self.category_app_services.create_category_from_factory(
            data={"name": self.name}
        )

    def test_list_of_categories(self):
        """
        Test list of all categories.
        """
        category = self.category_app_services.create_category_from_factory(
            data={"name": fake.name()}
        )
        self.assertEqual(
            self.category_app_services.list_of_all_categories().count(), 2
        )

    def test_get_category_by_id(self):
        """
        Test get category by id.
        """
        self.assertEqual(
            self.category_app_services.get_category_by_id(
                category_id=self.category.id
            ).id,
            self.category.id,
        )

    def test_negative_get_category_by_wrong_id(self):
        """
        Test negative get category by wrong id.
        """
        with self.assertRaises(Exception):
            self.category_app_services.get_category_by_id(
                category_id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf"
            )

    def test_filter_category_by_name(self):
        """
        Test filter category by name.
        """
        category = self.category_app_services.filter_category_by_name(
            category_name=self.category.name
        ).first()
        self.assertEqual(category.name, self.category.name)

    def test_negative_filter_category_by_wrong_name(self):
        """
        Test negative filter category by wrong name.
        """
        category = self.category_app_services.filter_category_by_name(
            category_name="dasgkajhhashdkashjdaskasjkdhasjkdrasuuasiaiyuweyuiahasddiasjklskl"
        )
        self.assertEqual(category.count(), 0)

    def test_create_category_from_factory(self):
        """
        Test create category from factory.
        """
        category = self.category_app_services.create_category_from_factory(
            data={"name": fake.name()}
        )
        self.assertTrue(isinstance(category, self.category_model))


class ProductAppServicesTestCases(TestCase):
    """
    Test cases for product application service.
    """

    def setUp(self):
        """
        Set up for testing product model.
        """
        self.product_test_helper = ProductCreateTestHelper()
        self.category_test_helper = CategoryCreateTestHelper()
        self.product_app_services = ProductAppServices()
        self.product_model = Product
        self.product = self.product_test_helper.create_product_data()

    def test_list_of_all_products(self):
        """
        Test list of all products.
        """
        self.product_test_helper.create_product_data()
        self.assertEqual(
            self.product_app_services.list_of_all_products().count(), 2)

    def test_get_product_by_id(self):
        """
        Test get product by id.
        """
        self.assertEqual(
            self.product_app_services.get_product_by_id(
                product_id=self.product.id
            ).id,
            self.product.id,
        )

    def test_negative_get_product_by_wrong_id(self):
        """
        Test negative get product by wrong id.
        """
        with self.assertRaises(Exception):
            self.product_app_services.get_product_by_id(
                product_id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf"
            )

    def test_filter_product_by_name(self):
        """
        Test filter product by name.
        """
        product = self.product_app_services.filter_product_by_name(
            product_name=self.product.name
        ).first()
        self.assertEqual(product.name, self.product.name)

    def test_negative_filter_product_by_wrong_name(self):
        """
        Test negative filter product by wrong name.
        """
        product = self.product_app_services.filter_product_by_name(
            product_name="dasgkajhhashdkashjdaskasjkdhasjkdrasuuasiaiyuweyuiahasddiasjklskl"
        )
        self.assertEqual(product.count(), 0)

    def test_create_product_from_factory(self):
        """
        Test create product from factory.
        """
        product_data = {
            "name": fake.name(),
            "description": fake.name(),
            "price": random.randint(800, 1000),
            "sell_price": random.randint(300, 799),
            "category": self.category_test_helper.create_category_data(),
            "quantity": random.randint(1, 1000)
        }
        product = self.product_app_services.create_product_from_factory(
            data=product_data
        )
        self.assertTrue(isinstance(product, self.product_model))


class ProductImagesAppServicesTestCases(TestCase):
    """
    Test cases for productImages application service.
    """

    def setUp(self):
        """
        Set up for testing productImages model.
        """
        self.product_images_test_helper = ProductImagesCreateTestHelper()
        self.product_test_helper = ProductCreateTestHelper()
        self.product_images_app_services = ProductImagesAppServices()
        self.product_images_model = ProductImages

    def test_bulk_create_product_images(self):
        """
        Test bulk create productImages.
        """
        product = self.product_test_helper.create_product_data()
        product_image_1 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        product_images_2 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        images_list = []
        for image in [product_image_1, product_images_2]:
            images_list.append(
                {
                    "image": image,
                    "product_id": product.id
                }
            )
        self.product_images_app_services.bulk_create_product_images(
            data=images_list
        )
        product_image = self.product_images_app_services.filter_product_images_by_product_id(
            product_id=product.id
        )
        self.assertTrue(isinstance(product_image.first(),
                        self.product_images_model))

    def test_list_of_product_images(self):
        """
        Test list of productImages.
        """
        self.product_images_test_helper.create_product_images_data()
        self.assertEqual(
            self.product_images_app_services.list_of_product_images().count(), 1
        )

    def test_filter_product_images_by_product_id(self):
        """
        Test filter productImages by product id.
        """
        product_image = self.product_images_test_helper.create_product_images_data()
        product_image = self.product_images_app_services.filter_product_images_by_product_id(
            product_id=product_image.product_id
        )
        self.assertTrue(isinstance(product_image.first(),
                        self.product_images_model))

    def test_negative_filter_product_images_by_wrong_product_id(self):
        """
        Test negative filter productImages by wrong product id.
        """
        product_image = self.product_images_app_services.filter_product_images_by_product_id(
            product_id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf"
        )
        self.assertEqual(product_image.__len__(), 0)

    def test_get_product_image_by_id(self):
        """
        Test get productImage by id.
        """
        product_image = self.product_images_test_helper.create_product_images_data()
        self.assertEqual(
            self.product_images_app_services.get_product_image_by_id(
                product_image_id=product_image.id
            ).id,
            product_image.id,
        )

    def test_negative_get_product_image_by_wrong_id(self):
        """
        Test negative get productImage by wrong id.
        """
        with self.assertRaises(Exception):
            self.product_images_app_services.get_product_image_by_id(
                product_image_id="ff8aff50-b3b0-4b4a-bd89-8d7354aedccf"
            )

    def test_filter_product_images_by_product_id_list(self):
        """
        Test filter productImages by product id list.
        """
        product_image = self.product_images_test_helper.create_product_images_data()
        product_image = self.product_images_app_services.filter_product_images_by_product_id_list(
            product_id_list=[product_image.product_id]
        )
        self.assertTrue(isinstance(product_image.first(),
                        self.product_images_model))
