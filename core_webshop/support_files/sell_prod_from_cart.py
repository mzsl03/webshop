from django import forms

class CheckoutForm(forms.Form):
    tax_number = forms.CharField(
        max_length=10,
        label="Adószám",
        required=True
    )
    zip_code = forms.CharField(
        max_length=4,
        label="Irányítószám",
        required=True
    )
    address = forms.CharField(
        max_length=255,
        label="Cím",
        required=True
    )
    costumer_name = forms.CharField(
        max_length=255,
        label="Vevő neve",
        required=True
    )
    city = forms.CharField(
        max_length=255,
        label="Város",
        required=True
    )
