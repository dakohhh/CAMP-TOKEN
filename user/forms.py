from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False), help_text='')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(render_value=False), help_text='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']



class MerchantRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False), help_text='')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(render_value=False), help_text='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']