from django.urls import path

from .views import (CartListView, CreateCartView, CartDeleteView)

app_name = "cart"
urlpatterns = [
    path("cart/list", CartListView.as_view(), name="cart_list"),
    path("add/cart/<str:pk>", CreateCartView.as_view(), name="add-to-cart"),
    # path("product/update/<str:pk>",
    #      ProductUpdateView.as_view(), name="product-update"),
    path("cart/delete/<str:pk>",
         CartDeleteView.as_view(), name="cart-delete"),
]
