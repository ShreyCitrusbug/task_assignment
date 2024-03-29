from typing import Any
from django import forms
from test_assignment.domain.product_management.models import Category


class CreateCategoryForm(forms.ModelForm):
    """
    Django form class for Category data table.
    """
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name", "max_length": "250"}
            ),
        }

    def clean(self):
        clean_data = super(CreateCategoryForm, self).clean()
        name = clean_data.get("name")

        if not name:
            self.add_error("name", "*Name is required")


class UpdateCategoryForm(forms.ModelForm):
    """
    Django form class for Category data table.
    """
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name", "max_length": "250"}
            )
        }

    def clean(self):
        clean_data = super(UpdateCategoryForm, self).clean()
        name = clean_data.get("name")

        if not name:
            self.add_error("name", "*Name is required")
