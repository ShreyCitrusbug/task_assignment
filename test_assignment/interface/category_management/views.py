import logging
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from test_assignment.domain.product_management.models import Category
from test_assignment.application.product__management.services import CategoryAppServices
from test_assignment.interface.category_management.forms import CreateCategoryForm, UpdateCategoryForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

logger = logging.getLogger("django")


class CategoryListView(ListView):
    """
    category List View for category model data. Inherits django's default List view.
    """
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    category_app_services = CategoryAppServices()

    def get_queryset(self):
        return self.category_app_services.list_of_all_categories()


class CategoryCreateView(CreateView):
    """
    Category Create View for category model data. Inherits django's default Create view.
    """
    model = Category
    template_name = 'category/category_create.html'
    form_class = CreateCategoryForm

    def get_success_url(self):
        messages.success(
            self.request, f"Category {self.object.name} Created Successfully")
        logger.info("Category %s created successfully", self.object.name)
        return reverse("category:category_list")


class CategoryUpdateView(UpdateView):
    """
    Category Update View for category model data. Inherits django's default Update view.
    """
    model = Category
    template_name = 'category/category_update.html'
    form_class = UpdateCategoryForm

    def get_success_url(self):
        messages.success(
            self.request, f"Category {self.object.name} Updated Successfully")
        logger.info("category %s updated successfully", self.object.name)
        return reverse("category:category_list")

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error('Error while update category %s', e.args[0])
            messages.error(self.request, "category not found")
            return HttpResponseRedirect(reverse("category:category_list"))


class CategoryDeleteView(View):
    """
    Category Delete View for category model data. Inherits django's default Delete view.
    """
    category_app_services = CategoryAppServices()

    def get(self, request, pk):
        try:
            category = self.category_app_services.get_category_by_id(
                category_id=pk)
            category.delete()
            logger.info("category %s deleted successfully", category.name)
            messages.success(
                request, f"Category {category.name} Deleted Successfully")
            return HttpResponseRedirect(reverse("category:category_list"))
        except Category.DoesNotExist as category_not_found:
            logger.error("Error while delete category %s",
                         category_not_found.args[0])
            messages.error(request, "Category not found")
            return HttpResponseRedirect(reverse("category:category_list"))
