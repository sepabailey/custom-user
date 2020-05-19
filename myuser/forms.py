from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'display_name', 'password1', 'password2')
