from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms import StudentRegistrationForm
# Create your views here.

def home(request:HttpRequest):
    
    return request("Esmf")




def signup_student(request:HttpRequest):


    form = StudentRegistrationForm()
    
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)
