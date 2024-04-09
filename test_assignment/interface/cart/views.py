import logging

from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from test_assignment.application.cart.services import CartAppServices

from test_assignment.domain.cart.models import Cart


logger = logging.getLogger("django")


class CartListView(ListView):
    """
    Cart List View for cart model data. Inherits django's default List view.
    """
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart'
    cart_app_services = CartAppServices()

    def get_queryset(self):
        return self.cart_app_services.list_of_all_products_in_cart()


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
