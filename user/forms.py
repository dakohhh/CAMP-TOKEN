from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    email = forms.EmailField(max_length=254,required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))
    
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}, render_value=False))
    
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}, render_value=False), help_text='')

    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']





class MerchantRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    email = forms.EmailField(max_length=254,required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    business_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))

    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}))
    
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}, render_value=False))
    
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend'}, render_value=False), help_text='')



    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']
