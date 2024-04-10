from django.db.models.query import QuerySet

from test_assignment.domain.cart.models import Cart

from test_assignment.domain.cart.services import (
    CartService)
from test_assignment.application.product__management.services import ProductAppServices
from test_assignment.domain.product_management.models import Product


class CartAppServices:
    """
    Cart application service class.
    """

    def __init__(self):
        self.cart_service = CartService()

    def list_of_all_products_in_cart(self) -> QuerySet[Cart]:
        """
        List of all categories.
        """
        return self.cart_service.get_cart_repo().filter(is_active=True)

    def create_cart_from_product_id(self, product_id: str) -> Cart:
        """
        Create cart from product id.
        """
        try:
            product = ProductAppServices().get_product_by_id(product_id=product_id)
            cart = self.cart_service.cart_factory().build_entity_with_id(
                product=product, quantity=1)
            cart.save()
        except Product.DoesNotExist as product_not_found:
            raise product_not_found

    def get_cart_by_id(self, cart_id: str) -> Cart:
        """
        Get cart by uuid. 
        """
        return self.cart_service.get_cart_repo().get(id=cart_id)
