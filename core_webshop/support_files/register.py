from django import forms
from phoneshop.models import Workers, Shops

class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=150, label="Felhasználónév")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Jelszó")


    first_name = forms.CharField(max_length=255, label="Keresztnév")
    last_name = forms.CharField(max_length=255, label="Vezetéknév")
    address = forms.CharField(max_length=255, label="Cím")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Születési dátum")
    phone_number = forms.CharField(max_length=12, label="Telefonszám")
    position = forms.ChoiceField(choices=Workers.positions, label="Pozíció")
    shop = forms.ModelChoiceField(queryset=Shops.objects.all(), label="Üzlet")