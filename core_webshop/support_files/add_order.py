from django import forms
from phoneshop.models import Orders, Products
from django.utils.text import slugify


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['quantity', 'color', 'storage']
        widgets = {
            'quantity': forms.NumberInput(),
            'color': forms.Select(),
            'storage': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product", None)
        specs = kwargs.pop("specs", None)
        super().__init__(*args, **kwargs)
        if product and product.colors:
            choices = [(c, c.capitalize()) for c in product.colors]
            choices_storage = [(s, f"{s} GB" if int(s) > 1 else f"{s} TB") for s in specs.storage]
            self.fields['color'].widget = forms.Select(choices=choices)
            self.fields['storage'].widget = forms.Select(choices=choices_storage)
            if product and product.category == "Tartozék":
                self.fields['storage'].required = False

