from decimal import Decimal
import logging
import uuid
from dataclasses import dataclass

from django.db import models

from utils.django.custom_models import ActivityTracking
from test_assignment.domain.product_management.models import Product

logger = logging.getLogger("django")

# Cart ID


@dataclass(frozen=True)
class CartID:
    """
    This will create UUID that will pass in cart build entity with id Method.
    """
    value: uuid.UUID


# ----------
# Cart Model
# ----------


class Cart(ActivityTracking):
    """
    Django model class for Cart data table.
    Inherits Activity Tracking model that consist of created_at,modified_at and is_active fields.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return str(self.product.name)

# Cart factory method


class CartFactory:
    """
    Factory class to create runtime object of cart model.
    Methods : 
        - build_entity_with_id - creates runtime object of cart model with auto assignment of uuid.
        - build_entity - creates runtime object of cart model."""

    @staticmethod
    def build_entity(
        id: CartID,
        product: Product,
        quantity: Decimal
    ) -> Cart:
        """
        Creates runtime object of cart model.
        """
        return Cart(
            id=id.value,
            product=product,
            quantity=quantity
        )

    @classmethod
    def build_entity_with_id(
        cls,
        product: Product,
        quantity: Decimal
    ) -> Cart:
        """
        Creates runtime object of category model with auto assignment of uuid.
        """
        entity_id = CartID(uuid.uuid4())
        return cls.build_entity(
            id=entity_id,
            product=product,
            quantity=quantity
        )
