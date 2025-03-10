from typing import Type

from django.db.models.manager import BaseManager

from test_assignment.domain.cart.models import Cart, CartFactory


class CartService:
    """
    Cart model services to create object of cart model by calling factory class.
    """
    @staticmethod
    def cart_factory() -> Type[CartFactory]:
        """
        Creates runtime object of cart model by calling factory class.
        """
        return CartFactory

    @staticmethod
    def get_cart_repo() -> BaseManager[Cart]:
        """
        Method to call objects of cart model.
        """
        return Cart.objects
