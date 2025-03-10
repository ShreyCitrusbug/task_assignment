import logging

from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (ListView, UpdateView,
                                  View)

from test_assignment.application.cart.services import CartAppServices

from test_assignment.domain.cart.models import Cart

from test_assignment.application.product__management.services import ProductImagesAppServices
logger = logging.getLogger("django")


class CartListView(ListView):
    """
    Cart List View for cart model data. Inherits django's default List view.
    """
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart'
    cart_app_services = CartAppServices()
    product_images_app_services = ProductImagesAppServices()

    def get_queryset(self):
        object_list = self.cart_app_services.list_of_all_products_in_cart(
        ).select_related('product').values("product", "quantity", "product__created_at")
        product_ids = [obj.get("product") for obj in object_list]
        print(object_list)
        unique_product_images = self.product_images_app_services.filter_product_images_by_product_id_list(
            product_id_list=product_ids
        ).distinct("product_id")
        for object in object_list:
            object["product_image"] = list(
                filter(lambda product_image: str(product_image.product_id) == str(object.get("product")), unique_product_images))[0].image
        return object_list


class CreateCartView(View):
    """
    Cart Create View for cart model data. Inherits django's default Create view.
    """
    model = Cart
    cart_app_services = CartAppServices()

    def get(self, request: HttpRequest, pk, *args, **kwargs) -> HttpResponse:
        try:
            self.cart_app_services.create_cart_from_product_id(product_id=pk)
            return HttpResponseRedirect(reverse('cart:cart_list'))
        except Exception as e:
            logger.error(e)
            messages.error(request, "Product not found")
            return HttpResponseRedirect(reverse('cart:cart_list'))


class CartDeleteView(View):
    """
    Cart Delete View for cart model data. Inherits django's default Delete view.
    """
    cart_app_services = CartAppServices()

    def get(self, request: HttpRequest, pk, *args, **kwargs) -> HttpResponse:
        """
        Django view method to handle GET request to delete Cart data.
        """
        try:
            cart = self.cart_app_services.get_cart_by_id(cart_id=pk)
            cart.delete()
            messages.success(
                request, f"Product {cart.product.name} removed successfully")
            return HttpResponseRedirect(reverse('cart:cart_list'))
        except Exception as e:
            logger.error(e)
            messages.error(request, "Product not found")
            return HttpResponseRedirect(reverse('cart:cart_list'))
