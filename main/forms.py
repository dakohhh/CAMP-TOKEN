from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    phone_number = forms.IntegerField(max_value=10, required=True, label="Phone Number", help_text="Enter a valid 10-digit number")
    email = forms.EmailField(max_length=254, required=True)


    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "password1", "password2"]



class SignupStudentForm(SignupForm):
    

    class Meta(SignupForm.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "password1", "password2"]



class SignupMerchantForm(SignupForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    phone_number = forms.IntegerField(max_value=10, required=True, label="Phone Number", help_text="Enter a valid 10-digit number")
    business_name = forms.CharField(max_length=200, required=True, label="Business Name")
    business_id = forms.CharField(max_length=200, required=False,label="Business ID or CAC No.")    

    class Meta(SignupForm.Meta):
        model = User
        fields = ["first_name", "last_name", "business_name", "email", "phone_number", "password1", "password2"]