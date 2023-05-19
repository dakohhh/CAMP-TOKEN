from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms import StudentRegistrationForm, MerchantRegistrationForm
# Create your views here.



def signup_student(request:HttpRequest):


    form = StudentRegistrationForm()
    
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)




def signup_merchant(request:HttpRequest):


    form = MerchantRegistrationForm()
    
    context = {"form": form}

    return render(request, "registration/signup_merchants.html", context)
