from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, required=True)
    last_name = forms.CharField(
        max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",
                  "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["email"]
