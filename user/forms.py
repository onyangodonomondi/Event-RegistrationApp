from django.contrib.auth.models import User

from  django.contrib.auth.forms import UserCreationForm

from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Mpesa_Number=forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'Mpesa_Number', 'password1', 'password2']