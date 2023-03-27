from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import SignupStudentForm, SignupMerchantForm

# Create your views here.





def home(request:HttpRequest):
    form = SignupMerchantForm()

    if request.method == "POST":
        print(request.POST)

    context = {"form": form}
    return render(request, "index.html", context)








