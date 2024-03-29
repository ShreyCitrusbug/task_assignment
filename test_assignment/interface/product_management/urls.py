from django.urls import path

from .views import (ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductListView, ProductUpdateView)

app_name = "product"
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/create", ProductCreateView.as_view(), name="product-create"),
    path("product/update/<str:pk>",
         ProductUpdateView.as_view(), name="product-update"),
    path("product/delete/<str:pk>",
         ProductDeleteView.as_view(), name="product-delete"),
    path("product/<str:pk>",
         ProductDetailView.as_view(), name="product-detail"),
]
