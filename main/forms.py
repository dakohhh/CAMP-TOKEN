from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser






class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False), help_text='')
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(), help_text='Enter the same password as before, for verification.')


    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number", "password1", "password2"]



class SignupStudentForm(SignupForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    phone_number = forms.IntegerField(max_value=9999999999, required=True, label="Phone Number", help_text="Enter a valid 10-digit number")

    class Meta(SignupForm.Meta):
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number", "password1", "password2"]



class SignupMerchantForm(SignupForm):
    phone_number = forms.IntegerField(max_value=9999999999, required=True, label="Phone Number", help_text="Enter a valid 10-digit number")
    business_name = forms.CharField(max_length=200, required=True, label="Business Name")
    business_id = forms.CharField(max_length=200, label="Business ID or CAC No.")    

    class Meta(SignupForm.Meta):
        model = CustomUser
        fields = ["business_name", "email", "phone_number", "password1", "password2", "business_id"]




class LoginForm(AuthenticationForm):

    username =  forms.EmailField(required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), required=True)



class PayMerchantForm(forms.Form):
    merchant_wallet_id =  forms.IntegerField(max_value=9999999999, required=True, label="Enter Merchant Wallet ID")
    amount =  forms.IntegerField(required=True,  label="Enter Amount")