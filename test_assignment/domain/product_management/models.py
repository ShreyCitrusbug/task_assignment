import logging
import uuid
from dataclasses import dataclass
from utils.django.custom_models import ActivityTracking
from django.db import models


logger = logging.getLogger("django")

# Category ID


@dataclass(frozen=True)
class CategoryID:
    """
    This will create UUID that will pass in Category build entity with id Method.
    """
    value: uuid.UUID

# ----------
# Category Model
# ----------


class Category(ActivityTracking):
    """
    Django model class for Category data table.
    Inherits Activity Tracking model that consist of created_at,modified_at and is_active fields.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
# Category factory method


class CategoryFactory:
    """
    Factory class to create runtime object of category model.
    Methods : 
        - build_entity_with_id - creates runtime object of category model with auto assignment of uuid.
        - build_entity - creates runtime object of category model."""

    @staticmethod
    def build_entity(
        id: CategoryID,
        name: str
    ) -> Category:
        """
        Creates runtime object of category model.
        """
        return Category(
            id=id.value,
            name=name
        )

    @classmethod
    def build_entity_with_id(
        cls,
        name: str
    ) -> Category:
        """
        Creates runtime object of category model with auto assignment of uuid.
        """
        entity_id = CategoryID(uuid.uuid4())
        return cls.build_entity(
            id=entity_id,
            name=name
        )


# Product ID
@dataclass(frozen=True)
class ProductID:
    """
    This will create UUID that will pass in Product build entity with id Method.
    """
    value: uuid.UUID


# ----------
# Product Model
# ----------
class Product(ActivityTracking):
    """
    Django model class for Product data table.
    Inherits Activity Tracking model that consist of created_at,modified_at and is_active fields.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)
    sell_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


# Product factory method


class ProductFactory:
    """
    Factory class to create runtime object of product model.
    Methods : 
        - build_entity_with_id - creates runtime object of product model with auto assignment of uuid.
        - build_entity - creates runtime object of product model."""

    @staticmethod
    def build_entity(
        id: ProductID,
        name: str,
        description: str,
        price: float,
        sell_price: float,
        category: Category,
    ) -> Product:
        """
        Creates runtime object of product model.
        """
        return Product(
            id=id.value,
            name=name,
            description=description,
            price=price,
            sell_price=sell_price,
            category=category,
        )

    @classmethod
    def build_entity_with_id(
        cls,
        name: str,
        description: str,
        price: float,
        sell_price: float,
        category: Category,
    ) -> Product:
        """
        Creates runtime object of product model with auto assignment of uuid.
        """
        entity_id = ProductID(uuid.uuid4())
        return cls.build_entity(
            id=entity_id,
            name=name,
            description=description,
            price=price,
            sell_price=sell_price,
            category=category,
        )


# product Image ID
@dataclass(frozen=True)
class ProductImagesID:
    """
    This will create UUID that will pass in ProductImages build entity with id Method.
    """
    value: uuid.UUID


class ProductImages(ActivityTracking):
    """
    Django model class for ProductImages data table.
    Inherits Activity Tracking model that consist of created_at,modified_at and is_active fields.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    image = models.ImageField(
        upload_to="product/images/", null=False, blank=False)
    product_id = models.UUIDField(null=False, blank=False)

    def __str__(self) -> str:
        return "Images for Product: " + str(self.product_id)


class ProductImagesFactory:
    """
    Factory class to create runtime object of productImages model.
    Methods : 
        - build_entity_with_id - creates runtime object of productImages model with auto assignment of uuid.
        - build_entity - creates runtime object of productImages model."""

    @staticmethod
    def build_entity(
        id: ProductImagesID,
        image: str,
        product_id: uuid
    ) -> ProductImages:
        """
        Creates runtime object of productImages model.
        """
        return ProductImages(
            id=id.value,
            image=image,
            product_id=product_id
        )

    @classmethod
    def build_entity_with_id(
        cls,
        image: str,
        product_id: uuid
    ) -> ProductImages:
        """
        Creates runtime object of productImages model with auto assignment of uuid.
        """
        entity_id = ProductImagesID(uuid.uuid4())
        return cls.build_entity(
            id=entity_id,
            image=image,
            product_id=product_id
        )
