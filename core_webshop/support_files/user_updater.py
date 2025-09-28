from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label="Felhasználónév",
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'invalid': 'Csak betűk, számok és @/./+/-/_ karakterek engedélyezettek.',
            'unique': 'Ez a felhasználónév már foglalt.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        labels = {
            'username': 'Felhasználónév',
            'first_name': 'Keresztnév',
            'last_name': 'Vezetéknév',
            'email': 'Email cím',
            'is_active': 'Aktív'
        }
        error_messages = {
            'username': {
                'unique': 'Ez a felhasználónév már foglalt.',
                'invalid': 'A felhasználónév formátuma hibás.'
            },
            'email': {
                'invalid': 'Helytelen e-mail formátum.'
            },
        }

        help_texts = {
            'username': 'Felhasználónév: csak betűk, számok és @/./+/-/_ karakterek engedélyezettek!',
            'is_active': 'A felhasználó aktiválása/deaktiválása'
        }
