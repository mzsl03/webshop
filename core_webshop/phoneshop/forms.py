
from django import forms
from .models import Workers

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = [
            "last_name",
            "first_name",
            "address",
            "birth_date",
            "phone_number"
        ]
        labels = {
            "last_name": "Vezetéknév",
            "first_name": "Keresztnév",
            "address": "Lakcím",
            "birth_date": "Születési dátum",
            "phone_number": "Telefonszám",
        }
        widgets = {
            "last_name": forms.TextInput(attrs={"placeholder": "Vezetéknév", "required": True}),
            "first_name": forms.TextInput(attrs={"placeholder": "Keresztnév", "required": True}),
            "address": forms.TextInput(attrs={"placeholder": "Lakcím", "required": True}),
            "birth_date": forms.DateInput(attrs={"type": "date", "required": True}),
            "phone_number": forms.TextInput(attrs={"placeholder": "06xxxxxxxxx", "maxlength": 12}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name in ["last_name", "first_name", "address", "birth_date", "phone_number"]:
                self.fields[name].widget.attrs.update({"class": "worker-edit-input"})

