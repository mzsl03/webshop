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
            'category': forms.TextInput(),
            'colors': forms.TextInput(),
        }

    def clean_colors(self):
        colors = self.cleaned_data['colors']
        if isinstance(colors, str):
            colors = [color.strip() for color in colors.split(',') if color.strip()]
        return colors

    def clean_name(self):
        name = self.cleaned_data['name']
        slug_name = slugify(name)
        self.cleaned_data['image_path'] = [f"{slug_name}.png"]
        return name

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.image_path = self.cleaned_data.get('image_path', [])
        if commit:
            instance.save()
        return instance