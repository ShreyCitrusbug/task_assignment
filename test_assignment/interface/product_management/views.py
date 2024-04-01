import logging

from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from test_assignment.application.product__management.services import (
    ProductAppServices, ProductImagesAppServices)
from test_assignment.domain.product_management.models import (Category,
                                                              Product,
                                                              ProductImages)
from test_assignment.interface.product_management.forms import (
    CreateProductForm, UpdateProductForm)

logger = logging.getLogger("django")


class ProductListView(ListView):
    """
    Product List View for product model data. Inherits django's default List view.
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    product_app_services = ProductAppServices()

    def get_queryset(self):
        return self.product_app_services.list_of_all_products()


class ProductCreateView(CreateView):
    """
    Product Create View for product model data. Inherits django's default Create view.
    """
    model = Product
    template_name = 'product_create.html'
    form_class = CreateProductForm
    product_images_services = ProductImagesAppServices()

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        product_form = self.form_class(request.POST)
        product_images = request.FILES.getlist("images")
        if product_form.is_valid():
            product_form.save()
            product_images_list = []
            for product_image in product_images:
                product_images_list.append({
                    'image': product_image,
                    "product_id": product_form.instance.id
                })
            self.product_images_services.bulk_create_product_images(
                data=product_images_list
            )
            logger.info("Product images crated.")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(
            self.request, f"Product {self.object.name} Created Successfully")
        logger.info("Product %s created successfully", self.object.name)
        return reverse("product:product_list")

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(ProductCreateView, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error('Error while create product %s', e.args[0])
            messages.error(self.request, "Product not found")
            return HttpResponseRedirect(reverse("product:product_list"))


class ProductUpdateView(UpdateView):
    """
    Product Update View for product model data. Inherits django's default Update view.
    """
    model = Product
    template_name = 'product_update.html'
    form_class = UpdateProductForm
    product_images_app_services = ProductImagesAppServices()
    product_app_services = ProductAppServices()

    def get_success_url(self):
        messages.success(
            self.request, f"Product {self.object.name} Updated Successfully")
        logger.info("Product %s updated successfully", self.object.name)
        return reverse("product:product_list")

    def get_context_data(self, *args, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(
            *args, **kwargs)
        context['images'] = self.product_images_app_services.filter_product_images_by_product_id(
            product_id=self.object.id
        )
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error('Error while update product %s', e.args[0])
            messages.error(self.request, "Product not found")
            return HttpResponseRedirect(reverse("product:product_list"))

    def post(self, request: HttpRequest, pk, *args, **kwargs) -> HttpResponse:
        product = self.product_app_services.get_product_by_id(product_id=pk)
        product_form = self.form_class(request.POST, instance=product)
        product_images = request.FILES.getlist("images")
        if product_form.is_valid():
            product_form.save()
            product_images_list = []
            for product_image in product_images:
                product_images_list.append({
                    'image': product_image,
                    "product_id": product_form.instance.id
                })
            self.product_images_app_services.bulk_create_product_images(
                data=product_images_list
            )
            logger.info("Product images crated.")
        return super().post(request, *args, **kwargs)


class ProductDeleteView(View):
    """
    Product Delete View for product model data. Inherits django's default Delete view.
    """
    product_app_services = ProductAppServices()

    def get(self, request, pk):
        try:
            product = self.product_app_services.get_product_by_id(
                product_id=pk)
            product.delete()
            logger.info("Product %s deleted successfully", product.name)
            messages.success(
                request, f"Product {product.name} Deleted Successfully")
            return HttpResponseRedirect(reverse("product:product_list"))
        except Product.DoesNotExist as product_not_found:
            logger.error("Error while delete product %s",
                         product_not_found.args[0])
            messages.error(request, "Product not found")
            return HttpResponseRedirect(reverse("product:product_list"))


class ProductDetailView(DetailView):
    """
    Product Detail View for product model data. Inherits django's default Detail view.
    """
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    product_images_app_services = ProductImagesAppServices()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        context['product_images'] = self.product_images_app_services.filter_product_images_by_product_id(
            product_id=self.object.id
        )
        return context
