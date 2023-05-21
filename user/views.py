from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from utils.generate import generate_wallet_id
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import StudentRegistrationForm, MerchantRegistrationForm, LoginForm
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

    if request.method == "POST":
        form = MerchantRegistrationForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            current_user.wallet_id = generate_wallet_id()
            current_user.is_merchant = True

            current_user.save()

            messages.success(request, "Verification email has been sent")

            return redirect("signup_merchant")

    
    context = {"form": form}

    return render(request, "registration/signup_merchants.html", context)


def login(request:HttpRequest):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                messages.success(request, "Login Sucessfull")
            else:
                messages.error(request, 'Username and password is incorrect')

        

    context = {"form":form}

    return render(request, "login/login.html", context)



def choose_sign_student_merchant(request:HttpRequest):
    

    return render(request, "choose-student-merchant.html")
