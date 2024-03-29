from django.urls import path

from .views import (CategoryCreateView, CategoryDeleteView, CategoryListView,
                    CategoryUpdateView)

app_name = "category"

urlpatterns = [
    path("category", CategoryListView.as_view(), name="category_list"),
    path("category/create", CategoryCreateView.as_view(), name="category-create"),
    path("category/update/<str:pk>",
         CategoryUpdateView.as_view(), name="category-update"),
    path("category/delete/<str:pk>",
         CategoryDeleteView.as_view(), name="category-delete"),
]
