import random
import tempfile

from faker import Faker

from test_assignment.domain.product_management.services import (
    CategoryService, ProductImagesService, ProductService)

fake = Faker()


class CategoryCreateTestHelper:
    """
    helper class for creating test data of product model using Faker.
    methods:
        - init - constructor whenever CategoryCreateTestHelper class is called.
        - create_category_data - helper method to create test category by calling model services.
    """

    def __init__(self):
        self.category_service = CategoryService()

    def create_category_data(self):
        """
        Helper method to create test category by calling model services.
        Returns category object.
        """
        category = self.category_service.category_factory().build_entity_with_id(
            name=fake.name()
        )
        category.save()
        return category


class ProductCreateTestHelper:
    """
    helper class for creating test data of product model using Faker.
    methods:
        - init - constructor whenever ProductCreateTestHelper class is called.
        - create_product_data - helper method to create test product by calling model services.
    """

    def __init__(self):
        self.product_service = ProductService()
        self.category_helper_class = CategoryCreateTestHelper()

    def create_product_data(self):
        """
        Helper method to create test product by calling model services.
        Returns product object.
        """
        category = self.category_helper_class.create_category_data()
        product = self.product_service.product_factory().build_entity_with_id(
            name=fake.name(),
            description=fake.name(),
            price=random.randint(800, 1000),
            sell_price=random.randint(300, 799),
            category=category.id,
            images=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        product.save()
        return product


class ProductImagesCreateTestHelper:
    """
    helper class for creating test data of productImages model using Faker.
    methods:
        - init - constructor whenever ProductImagesCreateTestHelper class is called.
        - create_product_images_data - helper method to create test productImages by calling model services.
    """

    def __init__(self):
        self.product_images_service = ProductImagesService()
        self.category_helper_class = CategoryCreateTestHelper()

    def create_product_images_data(self):
        """
        Helper method to create test productImages by calling model services.
        Returns productImages object.
        """
        product = self.category_helper_class.create_category_data()
        product_images = self.product_images_service.product_images_factory().build_entity_with_id(
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            product=product.id
        )
        product_images.save()
        return product_images
