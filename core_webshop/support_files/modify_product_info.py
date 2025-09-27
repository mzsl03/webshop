from django import forms
from django.contrib.postgres.forms import SimpleArrayField
import re
from phoneshop.models import Specs


class SpecsForm(forms.ModelForm):
    storage = SimpleArrayField(
        base_field=forms.CharField(
            max_length=255,
            error_messages={
                "invalid": "Csak számokat adhatsz meg, vesszővel elválasztva! (pl.: 128,256,512)"
            }
        ),
        delimiter=',',
        required=False,
        help_text="Több értéket vesszővel elválasztva adj meg (pl.: 128,256,512)"
    )
    def clean_storage(self):
        storage = self.cleaned_data['storage']
        for item in storage:
            if not re.match(r'\d+$', item):
                raise forms.ValidationError("Csak számokat adhat meg!")
        return storage

    class Meta:
        model = Specs
        fields = [
            'CPU_speed', 'CPU_type', 'display_size', 'resolution',
            'display_technology', 'max_refresh_rate', 'Spen', 'camera',
            'memory', 'storage', 'os', 'charge', 'sensors',
            'size', 'weight', 'battery', 'release_date'
        ]