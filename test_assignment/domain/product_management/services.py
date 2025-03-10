from typing import Type

from django.db.models.manager import BaseManager

from test_assignment.domain.product_management.models import (
    Category, CategoryFactory, Product, ProductFactory, ProductImages,
    ProductImagesFactory)


class CategoryService:
    """
    Category model services to create object of category model by calling factory class.
    """
    @staticmethod
    def category_factory() -> Type[CategoryFactory]:
        """
        Creates runtime object of category model by calling factory class.
        """
        return CategoryFactory

    @staticmethod
    def get_category_repo() -> BaseManager[Category]:
        """
        Method to call objects of category model.
        """
        return Category.objects


class ProductService:
    """
    Product model services to create object of product model by calling factory class.
    """
    @staticmethod
    def product_factory() -> Type[ProductFactory]:
        """
        Creates runtime object of product model by calling factory class.
        """
        return ProductFactory

    @staticmethod
    def get_product_repo() -> BaseManager[Product]:
        """
        Method to call objects of product model.    
        """
        return Product.objects


class ProductImagesService:
    """
    ProductImages model services to create object of productImages model by calling factory class.
    """
    @staticmethod
    def product_images_factory() -> Type[ProductImagesFactory]:
        """
        Creates runtime object of productImages model by calling factory class.
        """
        return ProductImagesFactory

    @staticmethod
    def get_product_images_repo() -> BaseManager[ProductImages]:
        """
        Method to call objects of productImages model.
        """
        return ProductImages.objects
