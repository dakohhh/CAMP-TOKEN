from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from utils.generate import generate_wallet_id
from utils.response import CustomResponse, BadRequest
from utils.shortcuts import redirect_not_student, redirect_not_merchant
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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

    if request.user.is_authenticated:
        if not request.user.is_merchant:
            return redirect("dashboard_student")
        else:
            return redirect("dashboard_merchant")

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth.login(request, user)

                if not user.is_merchant:
                    return redirect("dashboard_student")
                else:
                    return redirect("dashboard_merchant")

            else:
                messages.error(request, 'Email or password is incorrect')

    context = {"form":form}

    return render(request, "login/login.html", context)

    

@login_required(login_url="login")
@redirect_not_student
def dashboard_student(request:HttpRequest):

    context = {"user":request.user}

    return render(request, "dashboard/dashboard_student.html", context)




@login_required(login_url="login")
@redirect_not_merchant
def dashboard_merchant(request:HttpRequest):

    return HttpResponse(f"This is the dashboard for merchant, the balance is {request.user.balance}, the wallet id is {request.user.wallet_id}")




@login_required(login_url="login")
@redirect_not_student
def get_student_transactions(request:HttpRequest):
    pass





def logout(request:HttpRequest):
    
    auth.logout(request)

    return redirect("login")



def choose_sign_student_merchant(request:HttpRequest):
    return render(request, "choose-student-merchant.html")



def http404(request:HttpRequest):
    return render(request, "404.html")
    