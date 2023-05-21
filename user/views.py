from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from utils.generate import generate_wallet_id
from django.contrib import messages
from .forms import StudentRegistrationForm, MerchantRegistrationForm
# Create your views here.



def signup_student(request:HttpRequest):


    form = StudentRegistrationForm()

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id()

            current_user.save()

            messages.success(request, "Verification email has been sent")

            return redirect("signup_student")
    
    context = {"form": form}

    return render(request, "registration/signup_student.html", context)




def signup_merchant(request:HttpRequest):


    form = MerchantRegistrationForm()
    
    context = {"form": form}

    return render(request, "registration/signup_merchants.html", context)
