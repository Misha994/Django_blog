from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=32)
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2')


