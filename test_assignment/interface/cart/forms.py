from django import forms

from test_assignment.domain.cart.models import Cart


class CreateCartForm(forms.ModelForm):
    """
    Django form class for cart data table.
    """
    class Meta:
        model = Cart
        fields = ['product', 'quantity']

    def clean(self):
        clean_data = super(CreateCartForm, self).clean()
        quantity = clean_data.get("quantity")

        if not quantity:
            self.add_error("name", "*Quantity is required")
