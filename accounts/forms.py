from django import forms
from .models import Address, CustomUser
from django.contrib.auth.forms import UserChangeForm

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'phone', 'address_line', 'city', 'postal_code', 'country']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']  # добавь поля, которые хочешь редактировать
