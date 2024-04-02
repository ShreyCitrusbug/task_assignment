from django import forms

from test_assignment.domain.product_management.models import ProductImages


class UpdateProductImages(forms.ModelForm):
    """
    Django form class for ProductImages data table.
    """
    class Meta:
        model = ProductImages
        fields = ['image']
