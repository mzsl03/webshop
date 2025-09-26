from django import forms
from phoneshop.models import Specs


class SpecsForm(forms.ModelForm):
    class Meta:
        model = Specs
        fields = [
            'CPU_speed', 'CPU_type', 'display_size', 'resolution',
            'display_technology', 'max_refresh_rate', 'Spen', 'camera',
            'memory', 'storage', 'os', 'charge', 'sensors',
            'size', 'weight', 'battery', 'release_date'
        ]