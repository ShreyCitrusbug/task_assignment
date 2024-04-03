import logging

from django.contrib import messages
from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (UpdateView,
                                  View, DeleteView)

from test_assignment.application.product__management.services import ProductImagesAppServices
from test_assignment.domain.product_management.models import ProductImages
from test_assignment.interface.product_image_management.forms import (
    UpdateProductImages)

logger = logging.getLogger("django")


class ProductImagesUpdateView(View):
    """
    Django view class for ProductImages data table.
    """
    model = ProductImages
    form_class = UpdateProductImages
    product_images_app_services = ProductImagesAppServices()

    def post(self, request: HttpResponse, pk, *args, **kwargs):
        """
        Django view method to handle POST request to update ProductImages data.
        """
        try:
            product_image = self.product_images_app_services.get_product_image_by_id(
                product_image_id=pk
            )
            if request.FILES.get("image"):
                product_image.image = request.FILES.get(
                    "image")
                product_image.save()
                logger.info("Product image updated successfully")
                messages.success(
                    request, "Product image updated successfully")
            else:
                messages.error(request, "Image not found")
            return JsonResponse({'status': 'success', "url": f'/product/update/{product_image.product_id}'})
        except ProductImages.DoesNotExist as image_not_found:
            logger.error("Error while update product image %s",
                         image_not_found.args[0])
            messages.error(request, "Product image not found")
            return JsonResponse({'status': 'error', 'url': f'/product/update/{product_image.product_id}'}, status=404)


class ProductImageDeleteView(DeleteView):
    """
    Django view class for ProductImages data table.
    """
    model = ProductImages
    product_images_app_services = ProductImagesAppServices()

    def get(self, request, pk):
        try:
            product_image = self.product_images_app_services.get_product_image_by_id(
                product_image_id=pk
            )
            product_image.delete()
            logger.info("Product image deleted successfully")
            messages.success(
                request, "Product image deleted successfully")
            return HttpResponseRedirect(reverse("product:product_list"))
        except ProductImages.DoesNotExist as image_not_found:
            logger.error("Error while delete product image %s",
                         image_not_found.args[0])
            messages.error(request, "Product image not found")
            return HttpResponseRedirect(reverse("product:product_list"))
