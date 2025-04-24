from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # добавь email, если хочешь

class CustomAuthenticationForm(AuthenticationForm):
    pass  # можно использовать стандартную форму без изменений
