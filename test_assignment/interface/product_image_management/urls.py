from django.urls import path

from .views import (ProductImagesUpdateView, ProductImageDeleteView)

app_name = "product_image"

urlpatterns = [
    path("product/image/update/<str:pk>",
         ProductImagesUpdateView.as_view(), name="product_image-update"),
    path("product/image/delete/<str:pk>",
         ProductImageDeleteView.as_view(), name="product_image-delete"),
]
