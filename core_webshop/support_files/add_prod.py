from django import forms
from phoneshop.models import Products
from django.utils.text import slugify


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'category', 'colors']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.NumberInput(),
            'category': forms.Select(),
            'colors': forms.TextInput(),
        }

    def clean_colors(self):
        colors = self.cleaned_data['colors']
        if isinstance(colors, str):
            colors = [color.strip() for color in colors.split(',') if color.strip()]
        if not isinstance(colors, list):
            raise forms.ValidationError("A színeknek listának kell lenniük.")
        return colors

    def clean_prices(self):
        prices = self.cleaned_data['prices']

    def clean_name(self):
        name = self.cleaned_data['name']
        slug_name = slugify(name)
        colors = self.cleaned_data.get('colors', [])
        self.cleaned_data['image_path'] = [f"{slug_name}-{color}.png" for color in colors]
        return name


    def save(self, commit=True):
        instance = super().save(commit=False)
        slug_name = slugify(self.cleaned_data['name'])
        colors = self.cleaned_data.get('colors', [])
        instance.image_path = [f"{slug_name}-{color}.png" for color in colors]
        if commit:
            instance.save()
        return instance
