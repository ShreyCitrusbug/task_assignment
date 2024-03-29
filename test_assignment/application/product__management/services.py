from django.db.models.query import QuerySet

from test_assignment.domain.product_management.models import (Category,
                                                              Product,
                                                              ProductImages)
from test_assignment.domain.product_management.services import (
    CategoryService, ProductImagesService, ProductService)


class CategoryAppServices:
    """
    Category application service class.
    """

    def __init__(self):
        self.category_service = CategoryService()

    def list_of_all_categories(self) -> QuerySet[Category]:
        """
        List of all categories.
        """
        return self.category_service.get_category_repo().filter(is_active=True)

    def get_category_by_id(self, category_id: str) -> Category:
        """
        Method to get category by uuid.
        Args :
            - Takes uuid of category as an argument.
        Returns:
            - Returns category object id success else raise DoesNotExist exception.
        """
        return self.category_service.get_category_repo().get(id=category_id)

    def filter_category_by_name(self, category_name: str) -> QuerySet[Category]:
        """
        Method to filter category by category name.
        Args :
            - Takes name of category as an argument.
        Returns:
            - Returns category queryset if success else returns empty queryset.
        """
        return self.category_service.get_category_repo().filter(name=category_name)

    def create_category_from_factory(self, data: dict) -> Category:
        """
        Method to create category object from factory class.
        """
        category = self.category_service.category_factory().build_entity_with_id(
            name=data.get("name")
        )
        category.save()
        return category


class ProductAppServices:
    """
    Product application service class.
    """

    def __init__(self):
        self.product_service = ProductService()

    def list_of_all_products(self) -> QuerySet[Product]:
        """
        List of all products.
        """
        return self.product_service.get_product_repo().filter(is_active=True)

    def get_product_by_id(self, product_id: str) -> Product:
        """
        Method to get product by uuid.
        Args :
            - Takes uuid of product as an argument.
        Returns:
            - Returns product object id success else raise DoesNotExist exception.
        """
        return self.product_service.get_product_repo().get(id=product_id)

    def filter_product_by_name(self, product_name: str) -> QuerySet[Product]:
        """
        Method to filter product by product name.
        Args :
            - Takes name of product as an argument.
        Returns:
            - Returns product queryset if success else returns empty queryset.
        """
        return self.product_service.get_product_repo().filter(name=product_name)

    def create_product_from_factory(self, data: dict) -> Product:
        """
        Method to create product object from factory class.
        Args - Takes data as form of dict as an argument.
        Returns - Returns product object.
        """
        product = self.product_service.product_factory().build_entity_with_id(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            sell_price=data.get("sell_price"),
            category=data.get("category"),
        )
        product.save()
        return product


class ProductImagesAppServices:
    """
    Product Image application service class.
    """

    def __init__(self):
        self.product_images_service = ProductImagesService()

    def bulk_create_product_images(self, data: dict):
        """
        Method to create product images object from factory class.
        Args :
            - Takes data as form of dict as an argument.
        """
        bulk_created_product_images = self.product_images_service.get_product_images_repo().bulk_create(
            [self.product_images_service.product_images_factory(
            ).build_entity_with_id(**product_images_data) for product_images_data in data]
        )
        return bulk_created_product_images

    def list_of_product_images(self) -> QuerySet[ProductImages]:
        """
        Method to filter product images by product id.
        Args :
            - Takes product id as an argument.
        Returns:
            - Returns product images queryset if success else returns empty queryset.
        """
        return self.product_images_service.get_product_images_repo().filter(is_active=True)

    def filter_product_images_by_product_id(self, product_id: str) -> QuerySet[ProductImages]:
        """
        Method to filter product images by product id.
        Args :
            - Takes product id as an argument.
        Returns:
            - Returns product images queryset if success else returns empty queryset.
        """
        return self.product_images_service.get_product_images_repo().filter(product_id=product_id)

    def bulk_update_product_images(self, data: dict):
        """
        Method to update product images object from factory class.
        Args :
            - Takes data as form of dict as an argument.
        """
        bulk_updated_product_images = self.product_images_service.get_product_images_repo().bulk_update(
            [self.product_images_service.product_images_factory(
            ).build_entity_with_id(**product_images_data) for product_images_data in data]
        )
        return bulk_updated_product_images
