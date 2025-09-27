from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        help_text="Ha a jelszót nem szeretné változtatni, ezt a mezőt hagyja üresen!."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active']
        labels = {
            'username': 'Felhasználónév',
            'first_name': 'Keresztnév',
            'last_name': 'Vezetéknév',
            'email': 'Email cím',
            'password': 'Jelszó',
            'is_active': 'Aktív'
        }
        help_texts = {
            'username': 'Felhasználónév: csak betűk, számok és @/./+/-/_ karakterek engedélyezettek!',
            'is_active': 'A felhasználó aktiválása/deaktiválása'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
