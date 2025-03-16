# core/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('admin', 'Администратор'),
    ('manager', 'Менеджер'),
    ('user', 'Пользователь'),
)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Роль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
