from django.contrib import admin

from test_assignment.domain.product_management.models import (Category,
                                                              Product,
                                                              ProductImages)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImages)
