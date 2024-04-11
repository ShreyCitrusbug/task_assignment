from typing import Any

from django import forms

from test_assignment.application.product__management.services import \
    ProductImagesAppServices
from test_assignment.domain.product_management.models import Product


class CreateProductForm(forms.ModelForm):
    """
    Django form class for Product data table.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'sell_price', 'category', 'quantity']
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name", "max_length": "250"}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "Price"}
            ),
            "sell_price": forms.NumberInput(
                attrs={"placeholder": "Sell Price"}
            ),
            "quantity": forms.NumberInput(
                attrs={"placeholder": "Quantity"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Description",
                       "cols": "170", "rows": "5"}
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select form-select-lg mb-3",
                    "style": "box-shadow: none; border-radius:0; font-size: 15px;height: 55px;",
                }
            ),
        }

    def clean(self):
        clean_data = super(CreateProductForm, self).clean()
        name = clean_data.get("name")
        description = clean_data.get("description")
        price = clean_data.get("price")
        sell_price = clean_data.get("sell_price")
        category = clean_data.get("category")

        if not name:
            self._errors['name'] = self.error_class(
                ["*Name is required"]
            )
        if not description:
            self._errors['description'] = self.error_class(
                ["*Description is required"]
            )
        if not price:
            self._errors['price'] = self.error_class(
                ["*Price is required"]
            )
        if not sell_price:
            self._errors['sell_price'] = self.error_class(
                ["*Sell Price is required"]
            )
        if not category:
            self._errors['category'] = self.error_class(
                ["*Category is required"]
            )
        if (price and sell_price):
            if sell_price > price:
                self.add_error(
                    "sell_price", "*Sell price should less than price")


class UpdateProductForm(forms.ModelForm):
    """
    Django form class for Product data table.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'sell_price', 'category', 'quantity']
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name", "max_length": "250"}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "Price"}
            ),
            "sell_price": forms.NumberInput(
                attrs={"placeholder": "Sell Price"}
            ),
            "quantity": forms.NumberInput(
                attrs={"placeholder": "Quantity"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Description",
                       "cols": "170", "rows": "5"}
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select form-select-lg mb-3",
                    "style": "box-shadow: none; border-radius:0; font-size: 15px;height: 55px;",
                }
            ),
        }

    def clean(self):
        clean_data = super(UpdateProductForm, self).clean()
        name = clean_data.get("name")
        description = clean_data.get("description")
        price = clean_data.get("price")
        sell_price = clean_data.get("sell_price")
        category = clean_data.get("category")

        if not name:
            self._errors['name'] = self.error_class(
                ["*Name is required"]
            )
        if not description:
            self._errors['description'] = self.error_class(
                ["*Description is required"]
            )
        if not price:
            self._errors['price'] = self.error_class(
                ["*Price is required"]
            )
        if not sell_price:
            self._errors['sell_price'] = self.error_class(
                ["*Sell Price is required"]
            )
        if not category:
            self._errors['category'] = self.error_class(
                ["*Category is required"]
            )
        if (price and sell_price):
            if sell_price > price:
                self.add_error(
                    "sell_price", "*Sell price should less than price")
